var gulp = require('gulp')
var rename = require('gulp-rename')
var jsonminify = require('gulp-jsonminify')

gulp.task('minify', function () {
    return gulp.src('plugins.json')
        .pipe(jsonminify())
        .pipe(rename({
            extname: '.min.json'
        }))
        .pipe(gulp.dest('.'))
})