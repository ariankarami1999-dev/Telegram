<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/QvX0uhb0ClCPHSw-Xm2PJPLQNI0B3_pXXWi-7A76a7qjhRg82DsmhAOwB4E8UdYQi-JLbM7_sKBghWxKzVIqTHQDSCXItJ6N2OEFXv0UnTRGpRQ4_38Q3RF4QCzTALNrjBZRimvDTC7R-QQ0LRgakt0gyNJEyk1qQIDJn3zPv3ioj4WLH5if_BfIHfKJAexOJUoJVGwZrJPnyLoTHjAYQ6ynmohZVYBIPHCfzEQ0rssJ7b7NVMDG1fiSAhLnQ__ILUbT3WYz81drtm-Z0NbzbDDuCMFwVQtvfVA9tGlXa3TEhfook6t3NOM0D9oYDB12t0hl9Lt9bnN7POPUjMoU_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 500K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 05:37:29</div>
<hr>

<div class="tg-post" id="msg-31166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=XtFd3Edv3rDH3EorAoLZZXbOBSIVk5VCEICj9-NEVcu12-LbfT8Mim-ej01UvGQPeURY1tmQQVRKEkaEFO8SqDfOdIOez7MdUFTe1GW7auOorMl8oQk78JooGPeOUjUgWNF43FgrV3UtYfPIdQ4GlWemgNhCvn1c4l-tKWt-eunINheTfuMCgrLJKpurMNkVmQC3tI5XFhxAuHedRRm15RAPy1dZx7kA2dz5iRmpLIVgh9hEhHWthD3u_hQ_38E5ozCmTs1lk4YOyiK0mW3uYlXIYiOwYD4yxc8kJKVC9IXja7PAeYPgR_W5SOAujN0BYubYTuPqRFDoWV_OR8Xiig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=XtFd3Edv3rDH3EorAoLZZXbOBSIVk5VCEICj9-NEVcu12-LbfT8Mim-ej01UvGQPeURY1tmQQVRKEkaEFO8SqDfOdIOez7MdUFTe1GW7auOorMl8oQk78JooGPeOUjUgWNF43FgrV3UtYfPIdQ4GlWemgNhCvn1c4l-tKWt-eunINheTfuMCgrLJKpurMNkVmQC3tI5XFhxAuHedRRm15RAPy1dZx7kA2dz5iRmpLIVgh9hEhHWthD3u_hQ_38E5ozCmTs1lk4YOyiK0mW3uYlXIYiOwYD4yxc8kJKVC9IXja7PAeYPgR_W5SOAujN0BYubYTuPqRFDoWV_OR8Xiig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/31166" target="_blank">📅 00:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8K6lBDkSOK1jWc24lWFirJeRHOyPBcYktFWcTETESa9_bphMxMhUZRHBKC-cBFKehpENMpeuBPJdctXjeufsQnTHEgTe9VKUc3VUxNwyeYYPPiS0PalEGs1zCfMC3x21MULEc0d6epOyLdz-DXDpyPXiBjfEOPf6R07JAYRFCM0oB5NTF3Jisf0NkcsPICI1Y-SXcwDBfcIjKfi-ZySOBKTBoyOknCtC0LQLUpzeY4pW_hk8UUtDRSiCDtDBT7iVDzJUT73cYM7xSGDEiTKcki9mLrtsW9q6zz9AjtFDC84syx8sYrZR-J1UKKNjEZ1Dqr59s3Sa9eMzN7Bt0nBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ بازگشت فوتبال باشگاهی با تقابل حساس استقلال vs تراکتور در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/31163" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxtNolLQXhXkeGdwuMbchC0xMyEXE-_3xEdGAsjDT5BfHA9RdaZvbbl2wjLqG2yQh45p3ppzKMziKQLfcd5sSfdslpA6CC6ImWgjfDdcqsEC59pXK99slsqxQz-lYPzHvSAP0hBKTobiaTY3Dvj-ZJeidkPTHXNwGf3kH3XeJ_HeDXjwtztpck369MMo8BOoFeG6J02czPzFgez5n6Mv33JAMuVYP38XBqk6srkR90erMMeh4-B0Us1qmYe0Fe96AKxNoIcwmz7vCKhbUAqVMDQ9zGpgE85eKFnQn46HBufByPIKahf3ZqsniIHhLyMdQCgKV0D7i0EfqpVYYeN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ لست دنس مسی با پیراهن تیم آرژانتین با تاثیر روی هر 3 گل در جدال با بنین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/31162" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpoQp6k0w0owUIHswEZ4ImtjbAIwyGi15za_RIJF-MFVKVff8e_b6jbzEU43rrc08YgANPJ-I1BLYsMnfAqySCS58qp_q9qbQtdzPwfGYkxHWSZpX-3oKnvj_LSUl8_CgDi2B_UxdEqM0NevUtwgyxDebXSsM0CFVFiBxcIvUkuwLxdF4kVvrSxWRhjbgu_1gYTVl5YvNtPa5FvlPh0xqbTl5xzjdb_jfVwCwgxhE_R2icSST3qISiNcA4swHRZueiMeQSRirszv9UyE0iuakQo_ZIkmDPw1cPMin2CCCAgNhJAuDWqnkl-UgNBSlhC8ZpSXpaeMd7BV-zzt-r_Mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/31161" target="_blank">📅 23:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbs4H_RbZBDUNGYE8VbvNZ0Myf6sxjkWgvI3J8asxbaxeVWRGi5mlTBstBjeVoYfRYqVgst2j8gGH9sTGe13h-C9EOJkBSD0D5rBBX9GnxNwDAxGT3H-QUUbvBY5Gz7lsmW4zOHY_VZtLx4jbFw50X-TYVKUDbODss78toU2JIQ41G3L9MR66ms7X90qf7_cnukr-RA7eX0OhuhTql2SfKJugC0JS-FBZFYuLbAMGQuIIEMURBnt7yt6hG6nABhQzgcfX7HM6JCEKWcs2XLF_-rSUWFjhHG-PvpK4o8jWA-vR-jNCwa0S4hn9lv53vP15C08CgOwOnI-z7HP1F7YVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه استقلال به جمع مشتریان مبین دهقان هافبک‌دفاعی 21 ساله تیم الوحده اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/31160" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=P8a_wQ2wy0KGsIPxai4HowQ3KLKILtOsdNkNsx-x3ZaAEBKyKUsLO7kn5a8lQSBu3XEO1LsyQo0q6LVmHCJnHfBnihaArHkdaetx9KwZ1ccel5VlFznLDuE1ZxCRYY4HfFG6qIC169icZU9dobcJVXG6omJvLjVD2vo1E0_6EpeF63SnPNsnR1LOsKMJCreVqwOl9Ta-i2aOlcx5FXe48uuvD7eQEwgz3T_Msl5AV6IgsW9lnwNPkqwoJVAWhxC5Zt8KJvOvA8goIIz9FqcMneG8rJbeLCAFHHdxbfktJ2zMCuJ39Lft4KCgFFwaQW5rVl1p9O0iIT43wtw6tu6vAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=P8a_wQ2wy0KGsIPxai4HowQ3KLKILtOsdNkNsx-x3ZaAEBKyKUsLO7kn5a8lQSBu3XEO1LsyQo0q6LVmHCJnHfBnihaArHkdaetx9KwZ1ccel5VlFznLDuE1ZxCRYY4HfFG6qIC169icZU9dobcJVXG6omJvLjVD2vo1E0_6EpeF63SnPNsnR1LOsKMJCreVqwOl9Ta-i2aOlcx5FXe48uuvD7eQEwgz3T_Msl5AV6IgsW9lnwNPkqwoJVAWhxC5Zt8KJvOvA8goIIz9FqcMneG8rJbeLCAFHHdxbfktJ2zMCuJ39Lft4KCgFFwaQW5rVl1p9O0iIT43wtw6tu6vAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو زیرپست‌لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشههه موندگار می‌مونه. بابت تمام کارهایی که باتیم‌ملی‌آرژانتین انجام دادی نهایت احترام رو برات قائلم. یه بغل گرم رفیق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/31159" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB-mBCYEM2kpeFfaosmDDpRETgVlJYuZG-H0rF2DWzKaSJBrPyHssxdb7l9orwBrjhhruQ0kLduqun9SI9zuCxvsHKsxxAf30aMhPSe-7f3nk5CN6JQ9bK1x8yxvI5HnRpI1S8i2DWVsYzucbAQk2OxNjltRQ513pCpRAZRBYM3fCX0N9VYR--xAgHtG16bbS6b5ov2DOmQJZAO2FzoFcz32HYYcAoofu0hKasd01YNLsZA-qEEGPaXYGjUG-kLjCumN1kKbHtqw11HoF-QH2S7keJRVhqz01366jdMt0jOm0JFcfnXFhFLq3m5vKMzFmuBQiZx4GBkpDjO3A55ilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان
؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک ۲۳ ام جهان سقوط کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31158" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml9a7mK2bdtFSWvHjsdGP5ULkUOprXpc9bqCKS6T9i-zu3ZLApTjze7cn_KqNzilwb_6w9oTBv2bLSMugDgFb75OrjkAHr0OFN-DMtPWAIGRI7mCdAqA-0blzqu7N3mF_GyXEsje6Okjb7fsNZlV2gIOZbL-nDcT8hhwRM3qIM8w6BTMXSHwM755-O2CRq-P_7IZCyAbPAAG9v0IA5C4lKAENbHIG0HMO8vNQKjvbELSI4dnorBss8GHVzvUMDlfXJUYIltl1vXVh9Q_SDhmpER5mCFliW_UqIwTInIh5bQEjJSQBDeys9YVYixrV0QIpNPPbbJeUx9VYakM_pDL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان: لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/31157" target="_blank">📅 21:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lELgbs21LN3kBv1r2AR7oGmEqkczu0H7uQSphTGpiTltKbPAafXcrpLy7I6SztjzHpO_cnX9Pdk3BzF5Ajo6hOqoajbiyJsZaFFs-iVuaswfG2UQLv47A7wECEQrzJH3brE_XOudnofTwAcc1aOCHXB3k-sl10zs3T-h6KJfbhIJ95CW0kVqnnRpSK5IBTF3IlggUW2f3YWEYLmOFc43QEJ007H3QBl5XZLne7dVGEXq9zG_18eDmwIiaV1F4Z6pXP9q57PfzXR_utgPfKpZbbpjMhh-iL7olFNR8tObRd1yIsZCb5s9DddgM6Dj8r26qozPwxeSa7Xom_Y1UrbzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31156" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LydKul1Lysa2dI3CPaQVwSm__QSaMCmvynYj1avUPoZQgvoa95o3ctzblqaPNIY42UTNiOH9dun5GgQjfvQENMa_3fsE5E-jjeMEI0dxbEL5ilj0U6PQox04yIaNHTDCGz5W1bYzpGRmsPCo7GXmXLDIS32VWew-X9LTn9XNxp2KsUjMVr4FfZcs6ddrdve4zy1Vp7glkMwtEuAv4pw9KkNRszTUfK8yURlnYUvwjL_Js2q53nEKIfZVa66JwO7vGpnaedmJ1LG8gHgmoOLWvNk46E6qs47Q2mAxjdnsSfeg-WwKibJXb_yX7nfLmyZd5OT4HHPsE2uTrTZYkX0svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان:
لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31155" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
هوادار تیم‌ملی جمهوری دومینیکن در پایان بازی دیشب‌این‌تیم از ماریانو دیاز خواست‌که بوسش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/31154" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPlWzZWKpB96_hbeFNbCI94C8G2Vq13CnwVERBlMKS72ioYCIgpLGmuYT-muhJNgk7HAMq9pcXeoZJD6iCQksYJswjYRUmtMTBSTVkmzw-QPvI6JhmjxedoUbBjA170FEX5OZzs2HEEIDKYP4u4IfDYTn_2pBX2NP_ISBtK2EFCGCOAxIyw9oF1CLJm2eFDN1N7hbHN07ZPraM26EX0vaZkTqv5FpWixCms7-PCJY85J1D1l-MZPNn1u18spvzABtFAF1N6zl9soc2l2_pPNYJknfMEu3tniStObHEcygMfKo0kv4LguRCkw0ezbT7rPIa6_3uDoEeizIxcG-mI4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=gNeftPnxFtCtW3VsJnghVIZjoN04m9Mgz40DvAYG4YBc7WgYcStgJTlRmdjKnmFlsRgNxx503YwkkiB2aHGxRFw-vuO1Bt-tcFc43orH8tzlDTe61973pIYyPZpQguK3wmyp8DSfdSyESEFzS498YR2HlKtL6bMPoFUmKtFpdfBx7wCUEc29mTkzBi6jYEbQrt3r1_WTGJwuO_KkoTlm7PzdfZfqBSulHvVUV3stmUoPScXMf5hTA1lRzKPwAHs24SpFxCLPokkVfz9PusnWpSNs2N-VwgRrAO_-3ZF7aPnHZd7Wlrpba0HSNAprt87NYREi_NNsxctnr0HELcbP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=gNeftPnxFtCtW3VsJnghVIZjoN04m9Mgz40DvAYG4YBc7WgYcStgJTlRmdjKnmFlsRgNxx503YwkkiB2aHGxRFw-vuO1Bt-tcFc43orH8tzlDTe61973pIYyPZpQguK3wmyp8DSfdSyESEFzS498YR2HlKtL6bMPoFUmKtFpdfBx7wCUEc29mTkzBi6jYEbQrt3r1_WTGJwuO_KkoTlm7PzdfZfqBSulHvVUV3stmUoPScXMf5hTA1lRzKPwAHs24SpFxCLPokkVfz9PusnWpSNs2N-VwgRrAO_-3ZF7aPnHZd7Wlrpba0HSNAprt87NYREi_NNsxctnr0HELcbP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBISdLGaBq1-UQTOVGvsJblreau02yRfA54MCsWVHMTmPh1JyoOixe0ZO6TV4gkAu7moGIx6ZbUM_K8ZhiXJxKXYpH8AFSVbow8pXIUUJJLOAu84eoFs8W791s5JI7Kr6tuKUlxjwCxE41jNi8DE_q8grzb8eIHndioNGFfddQ9KW9uB09Bd0HDuVr7QyxPAmFgvg8GRy9ZxKPthKYQbvNQQrV9ZJZgVvC5UvtV8tLpXgLocqoq0tbl5Bc1XCM3HdfZpNeukULCwPh1rmgKQKaTadks2qnsRlfgxPt9OTJt-1oJZjsJ-QfrLpH9iuatRS3havYAIl8oIOEEEBXCHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=e3Mh9ZoWbiUclu_QTpb1RIrLSijbQL0_71SC1ytrD2kAOtLB2cjrDIQePOJwimWcjG5r188yrSMM3Lgtduep_Fa8kTVqcjQaQevRF_LI8KPRdPXplfYTt_Uw3oV29cGAFaXzH1DhN7FFxLo9nzlYmuRczjnMdhn7gByWTZy3RXTYGJmdxInYVEqpPIVrk3QA4qRqkc71hE4Dh0XSDbZ0pWZfpP6h2-NjcOobvaHn2N-1mPRsUWH4N2XvisXIZ_nCpnAPueufSSLBe6Ef9zCWaS1IoGnNLbyoOigeUyubFZtbCr0C_q-yTSfC-RYU-nMu6Lq0GHvT41hVxvi0Zuqrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=e3Mh9ZoWbiUclu_QTpb1RIrLSijbQL0_71SC1ytrD2kAOtLB2cjrDIQePOJwimWcjG5r188yrSMM3Lgtduep_Fa8kTVqcjQaQevRF_LI8KPRdPXplfYTt_Uw3oV29cGAFaXzH1DhN7FFxLo9nzlYmuRczjnMdhn7gByWTZy3RXTYGJmdxInYVEqpPIVrk3QA4qRqkc71hE4Dh0XSDbZ0pWZfpP6h2-NjcOobvaHn2N-1mPRsUWH4N2XvisXIZ_nCpnAPueufSSLBe6Ef9zCWaS1IoGnNLbyoOigeUyubFZtbCr0C_q-yTSfC-RYU-nMu6Lq0GHvT41hVxvi0Zuqrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصبانیت شدید نادر قاضی پور از سوال مجری صدا و سیما که گفت محمد رضا زنوزی مالک باشگاه تراکتور ثروتش رو از راه راند بازی در آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31150" target="_blank">📅 19:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ5VFYd03Fh1z9xYT0ND51vGq-mhxFqDsTclKrq5BQQMFjbnWG09wtbBIknMqQO2IutSDJfVUF8YyRkWY-Vjps2bsNlz6TKf3Q8QW9xxNtKENgPa3Rg5GUrhFJ-RaYWhKrvbg-pQk8G8Lk5p4hPkShyfNEASTwN8EDDU9TJu6DiS5x_gjr2dMOB5P3nu3plB0-hk2EEoYcO4rGyHCfeQdFQX3LKW9oZKfFWM-D2UtRQuISIk7-sLWUVn6P27rB1vnthRvM2TiF6YbW-46NQppqV8f4Uq1P8nF2ooU1rjWzmJN9FutD4vltMLYxOddQ49LdlLqVkVBzhIC-7XHHp7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رضاییان از بس گفت تو دوران حرفه‌‌ایم مصدوم نشده ام. این‌بار یجوری مصدوم‌شده که هم کشاله‌اش کش اومده هم از ناحیه خصوصی بدنش آسیب جدی دیده که ممکن تا اواسط آذر دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31148" target="_blank">📅 19:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6e0CMlq-7Bk0XlfJdjdBoyGf5i3Lr93DZUB_UQa3eLTRiC_8WhBoMEvGo2dRT9ZpH3gCX8uF_lGiwWxAP_7KXddcXihzasbeJCPcdAC-A21x-4ub-zL0p-eJXGrJA_56xHelMCn_y_tM8H0jWCm6u7qFRVk6LhGIJjPmfck8v9J-7JhsucXv7gamboN_-vLOxDN1jMdI99Ap4s2J6Dl1eReE9791AOmdrNkyCFJqbaCDwx8S0qHAqnWtXdH4KUzO27wpVnYg1mj_bqoKJGQ5OOfosSh8W7bpZYrpj7vHZdGMekf2Asvvh-D0sfbVL9xgIZ_LQFH8kFfvnfQJR0OUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدِ 3 هفته‌کسالت‌اور و حوصله سربر فیفادی به پایان رسید و از فردا فوتبال باشگاهی شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31147" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=s0L_lLL1QXvJ_C_Tv04njgoHEVgS1T6BfLA6rCtygXzx5SWQ7F545pD4ktEyT4kI5luWGZoGdn9DMTc-uVFoUzTWxPui9h6gSE8x4sH3luHmDAh3VR8EMWAWGc62N6nrNjJDHEsQAmOYCTY4VPsF4BWfKkOQXbMnwj3Rk5W6GAHFgE6cgKoithdp1q8J7_NJX16nuBnoWprx2jutKrpbr8COHOjruTZrj3ll-7FFt_Dp20fKKIQpKZNeKjQPrTeE2bnZrBJLwvXYy9zFCC6NE_6Uyw4zgUwaoSuUB584XLKHSPBEq6QYZt6Cd-xu-0p0eaxtASQxDpcUYV5pYdGD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=s0L_lLL1QXvJ_C_Tv04njgoHEVgS1T6BfLA6rCtygXzx5SWQ7F545pD4ktEyT4kI5luWGZoGdn9DMTc-uVFoUzTWxPui9h6gSE8x4sH3luHmDAh3VR8EMWAWGc62N6nrNjJDHEsQAmOYCTY4VPsF4BWfKkOQXbMnwj3Rk5W6GAHFgE6cgKoithdp1q8J7_NJX16nuBnoWprx2jutKrpbr8COHOjruTZrj3ll-7FFt_Dp20fKKIQpKZNeKjQPrTeE2bnZrBJLwvXYy9zFCC6NE_6Uyw4zgUwaoSuUB584XLKHSPBEq6QYZt6Cd-xu-0p0eaxtASQxDpcUYV5pYdGD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31146" target="_blank">📅 18:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuTBJw_BYnAnCQ_0YXB0Jd-cgM02QIaNGfb_j65IvzgTxWke0neYlci-JjJQCbOVztalh7eWFk5SltWzyctwEuP6Vt7SUkPigmAJ8kU70uYnUIiDgwXMA7YwgBhHhPAfim_1G69EuHJvZLkscxaXiF9hv2jrxXJJ_whw-m2P4IONAor9uVxjCyTk2qYl9KL81Jp6FClvXoxmn4_ySbV9lFf61NV8Ekmg7oaBHn94RicnIt0FpgwM-K459yOFHywJBR2CkGllb6cXpN7OOASFlXv-whayPgMmgRD5IOqEXwRFK46Gjy6r5g3f0a_zdSDV0Ca8W2sqI0XmqYqd6pQRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇫🇷
نمره‌ فوق‌ العاده‌ و‌ خیره‌ کننده مایکل اولیسه ستاره 22ساله‌تیم‌ملی‌فرانسه و باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31145" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=Sgu-YFZbbNG8WqGYlFC_f5UsNk2eCiZN3vowf1HhXufX8aBaRrvhaGY4h9PlFxcFkw84LfkkLg4WGbkqQfwZEmznbxPJqfM2dNlPefKEhhwpvRi1dn_lKCEQRJrY7Vlvj0c6bYRhz22zqYZ1_-FTTbiEZgJ5fXTb_Hlpv-RyRU_FBxz41qMBP5r6fIKLMPTLIQi_uIVphN20TaIj7BGxyKzoGCZtK0Y0VW_eYthx9sGoJfem7jCY3DOdF-mNwziD7tPMN_Cb8ytTVJ8W-O9uVBP3LEp6EN_MxlVn76pmOrBSveu5nqCYQvCWtWz1iFg1xr3o372ouuiJ-m1sxGu27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=Sgu-YFZbbNG8WqGYlFC_f5UsNk2eCiZN3vowf1HhXufX8aBaRrvhaGY4h9PlFxcFkw84LfkkLg4WGbkqQfwZEmznbxPJqfM2dNlPefKEhhwpvRi1dn_lKCEQRJrY7Vlvj0c6bYRhz22zqYZ1_-FTTbiEZgJ5fXTb_Hlpv-RyRU_FBxz41qMBP5r6fIKLMPTLIQi_uIVphN20TaIj7BGxyKzoGCZtK0Y0VW_eYthx9sGoJfem7jCY3DOdF-mNwziD7tPMN_Cb8ytTVJ8W-O9uVBP3LEp6EN_MxlVn76pmOrBSveu5nqCYQvCWtWz1iFg1xr3o372ouuiJ-m1sxGu27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
استایل جدید مجری ممنوع التصویر صداوسیما در عروسی؛ ایشون سال 1401 بعد از اون اتفاقات تلخ پاییز از سازمان‌صداوسیما قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31144" target="_blank">📅 17:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=oStreIUSmjq7Lxp7wiAD-aESc_rYCvg1-klkVYBQeJS_MsXVDI8UFXmGWo8X68GnOpcmA6bv26EsVUcpEQp1xde7ZdZugGX0ipoHQVAXKOix1diSg_A1jXx0hiJ_jP6HSCqZJYmM5Fx8dmFTDV7f9z4SXwzis_wFWt2OiHCQw_UCYESCdVEn5nZJ3-60w5ySBG9fRt44gpeNguds-brXWhfyBRTVJUMG3srQQ8toAImmSsOEva4vT6hp1C_YktKsnGyJNRWuSryDy8LaoUx_kydtic4jLh7u2pgrKcq7_n9OVkpcR1SA39kJYtmB0Dny26SM4jJFoxuRjiNFaex5Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=oStreIUSmjq7Lxp7wiAD-aESc_rYCvg1-klkVYBQeJS_MsXVDI8UFXmGWo8X68GnOpcmA6bv26EsVUcpEQp1xde7ZdZugGX0ipoHQVAXKOix1diSg_A1jXx0hiJ_jP6HSCqZJYmM5Fx8dmFTDV7f9z4SXwzis_wFWt2OiHCQw_UCYESCdVEn5nZJ3-60w5ySBG9fRt44gpeNguds-brXWhfyBRTVJUMG3srQQ8toAImmSsOEva4vT6hp1C_YktKsnGyJNRWuSryDy8LaoUx_kydtic4jLh7u2pgrKcq7_n9OVkpcR1SA39kJYtmB0Dny26SM4jJFoxuRjiNFaex5Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های جالب رسول مجیدی مجری شبکه ورزش درباره اسم یکی از پسرهای لیونل مسی که چیرو هست. چیرو به فارسی یعنی کوروش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31143" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdMh2pZ9d5Cy256DhUEN3WVexc7e0pdhLiIN8ErLR2nAGRRNKXv3BDphbzZhib3ZnMud_QLIwhcRZAGmaVEe7XA-WdrRhBfYAg8FNHei3B4ekwqF52Cbs2XUHhOoMdqQ6QbOdQUI-PZym4Iz-nmsoEeoOBrcJ8AbLGCxP1lde9z1jIVwcC2XCfWOVqpoNbYjkv_KzGUUFxiFSxnm-voLnR37_VvlNySKqI4dBtcFxmUFxyStuKLWjRiPt98_YcuQvg1gt7z7vdXnK6WRXVxpuMg2kRpgWKLhDoQK3s4O0NBMBI9gorWnbv6ka1HpmP-S1BhlLmaQGaulCXb7s665Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌عجیب‌دیفنساسنترال: کیلیان‌امباپه تصمیم خودش رو گرفت، اون آخر فصل از رئال جدا میشه و میره لیگ انگلیس؛ امباپه فصل بعد تو لیگ جزیره:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31142" target="_blank">📅 16:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=FDmRtarpSfqiOfAUCscJhaIsimAe-sBePokzHGhDHO_l33VquEHayLXngcL-HCUOA7G8K3bGkRCNPz4XtTrtrr4mnOsfc22Y1sZq_knuA6oZnYWokTnYb_teY_IsWetwGVffbxJhq_AX9iAKGktiqKFyNhwoHYjeczyQ8rR6CPNuSyDi1-HlboqIuoC3YfVkOD45Q2KtRqZ8_THm9Pn1tYkALE6c5gDSnW1hxbHrKqyHC47IaFlOrkXBBjFuHQlc26K9XxLOzwJAkgNOWAYUVA3ZpMcNl6j0F5wkPhHZ_j-LQgmQ6wnxXIpUu1A51aSzJx1XmfCFYvzAClrcYEFzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=FDmRtarpSfqiOfAUCscJhaIsimAe-sBePokzHGhDHO_l33VquEHayLXngcL-HCUOA7G8K3bGkRCNPz4XtTrtrr4mnOsfc22Y1sZq_knuA6oZnYWokTnYb_teY_IsWetwGVffbxJhq_AX9iAKGktiqKFyNhwoHYjeczyQ8rR6CPNuSyDi1-HlboqIuoC3YfVkOD45Q2KtRqZ8_THm9Pn1tYkALE6c5gDSnW1hxbHrKqyHC47IaFlOrkXBBjFuHQlc26K9XxLOzwJAkgNOWAYUVA3ZpMcNl6j0F5wkPhHZ_j-LQgmQ6wnxXIpUu1A51aSzJx1XmfCFYvzAClrcYEFzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی شدید علی آقا دایی اسطوره مردم ایران از خدافظی لیونل مسی آرژانتینی از مسابقات ملی‌.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31141" target="_blank">📅 16:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_UgXFnhO_n-v_nGSFZDekIDuC6pubj2SyzT8xZqb_5LoB2zdGiPUNn4jE4FpScJfscYnZYo5pHsVOXjl1uRDPDbT5XGv9Rog1b-GGn9APSHnwGhg-aQJH0_u-xBYXbFBaP18Mt-AckZ4ILMN8OJFvGMx8SslZHdQyuvKxmidd8frK1fHMOd8m-DDGfg1zB54cXjxo6SASD_JRH1jsq1ogBFYgH2xkM7NEuqCzAHcytLqgGNvoCUMK09bM4776heMpkeVX04r5adanMGBMd56BNwNk8-wlNoufm5MyevfY0G1LaxhYNeVU_VhpIvuexyUzMrMjSeMlJhrg3PCEJvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه آرسنال دقایقی پیش با انتشار این ویدیو خبر از تمدید قرارداد میکل آرتتا تا سال 2030 داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31140" target="_blank">📅 15:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpUZ-jiLt9g323vQd84kptra0Ysx5CvJ1rjELQxSPadZ2MThyesRi3gHPVsfSG9bwVZJeQz9lBSLtFZeAM-oSEfzCgUB4zsUKVBcCuQcDTYu8Io_qrB8y0ZLPUz8MNAmo2ibP8vLs6PBh7QnikzArDmR6Sss_qFgDaS8GsbrJsPAn81EFHNTixHbOoQ8AIb4u_XX0eG95A_uYc21r26oDH6EFgBWlx3LVbaZJ_3xtb2YyMux56jKNhTwAnssFFZuty2nlUcSNHbYfLxv1KROa5dHhhMLGlO_gvb8xeMipPO3b--8rB-U5pDVJano7xHag-lhESHOyVlUlE1N_ufFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10دیداراخیر استقلال و تراکتور در تمامی مسابقات: 4 برد استقلال، 2 تساوی، 4 برد تراکتور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31139" target="_blank">📅 15:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=amk5OZAs9zK6FqkK4ELm9iGQYDt2cqcX0XqwTHXTGC2W2xNTwWHh5gFNmT8naqq8RRFTTgiDW_E0ZRkPNZ98smL89Q_48k6PvjXvPKc2r6D5Xk4NVKNaqLsNu5lChABve8aPR4mJjcY8zSa933dYed8eK17xHF0syIw95KlVnQ4cheFRhM0kmTRzTbAk4p7BhHs3bL7QhdIX5eg8CLVKtY2rrWQcAzdPRKR3NkIE30W9in6vsRu3P7B4QfdOAX3QXCd6JxTVDitqh6QeVepVfEh3qcEoJepg4Kctu8vrbp5Rcpn11Q2MvsQnmiU8bc6SVaZYW9zsxMfb39hi1fhhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=amk5OZAs9zK6FqkK4ELm9iGQYDt2cqcX0XqwTHXTGC2W2xNTwWHh5gFNmT8naqq8RRFTTgiDW_E0ZRkPNZ98smL89Q_48k6PvjXvPKc2r6D5Xk4NVKNaqLsNu5lChABve8aPR4mJjcY8zSa933dYed8eK17xHF0syIw95KlVnQ4cheFRhM0kmTRzTbAk4p7BhHs3bL7QhdIX5eg8CLVKtY2rrWQcAzdPRKR3NkIE30W9in6vsRu3P7B4QfdOAX3QXCd6JxTVDitqh6QeVepVfEh3qcEoJepg4Kctu8vrbp5Rcpn11Q2MvsQnmiU8bc6SVaZYW9zsxMfb39hi1fhhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میکل آرتتا برای تمدید قراردادش تاسال 2030 با سران باشگاه آرسنال به‌توافق کامل رسید و بزودی با حضور در باشگاه قراردادش رو تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31138" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYCPCJS-7UXrBmSs3ZcuELoDoenxGnvDCMcwQ4nei3mU76OZLqhCgckpJV3UTy1CdyQ-QsL5HmRZirfhN0Qh-2YsYGW7bqiyBCOj_9_QRKxRfjpg9SpqlPaXgCVmuegwb2yOVGNpZc31f-U-5Xr0820NFT7TZnI35O8oLbWUIlfshOr037hqGpVVG-Hw6_rED9xZya_7sbfccF2g3xYF_EnWNEF9-vmtHSoiJkDoRO1Jmlc5Kmm_l9gQN8zDgwyH5ifl9C8MV8e2mMdLEMBmRqi9Ieov0A2GquwjKQZlXDU-xxMM7RMICcTpoND_dVNA97wCjgkkGeCF9QGU0um4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31137" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHbjQEDB8-pSlgTzLGyCgEmnBVsd71c3NOO7p4SpkgrDxyt1dEGEkj6Ub3scmz5douIgF7m_JUicaQq-9ic4X9lI9GasJXOdpiAQ2C_rBI8-u-hzVOZx4IHGbolwiaWgsAZCtCc9YADA7WwRJTlfJpFG_sJKUH28_qmUvL8jPMLD0PP-JWwV7vbMyc-9atMOiSV6ClaBRHmthUcEE4QZ4HIxq95OZgMpE4tug3UtaVJBchH5Jqstm7Qo5BpURJxvh5ttnvAXQfP9PeErP4lGFlO6L3jooGzbTczACt7S5UjfILqpRSspEqPc1IUhNataEpXOr5HrmduoxO5FPTF5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛ پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31136" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=ApLDTONZdRRC-jPC3U1R9VxokXik-Ws62sxgOSLey3XhECDkTgMb-Ctt7x62QjNTPtw41OqZQtqNXuzIPWdruG4PH1oz_WyA4KkB6yPfp8KFxGjkow9O82rNL-BlNB0m6zNbtaiWbLL1W5_39gnnmVioNaE5uCjRNuoX8YvbtjBu9OzfBd_bm_AQB7mgDs3fi_Cd32FCXwVp13trhQRVAyhs8G5qJZQwlg4BPao3hUPAC1fLdmfYkBvDbTunJXaibLPXjusPPaWx0XUtIEPcdWpJw0RvEmrLIhboXtqVSQHEesWUcHPEdYbmucG-UFpM9BQQGQlsTvcycUKJ1bJmEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=ApLDTONZdRRC-jPC3U1R9VxokXik-Ws62sxgOSLey3XhECDkTgMb-Ctt7x62QjNTPtw41OqZQtqNXuzIPWdruG4PH1oz_WyA4KkB6yPfp8KFxGjkow9O82rNL-BlNB0m6zNbtaiWbLL1W5_39gnnmVioNaE5uCjRNuoX8YvbtjBu9OzfBd_bm_AQB7mgDs3fi_Cd32FCXwVp13trhQRVAyhs8G5qJZQwlg4BPao3hUPAC1fLdmfYkBvDbTunJXaibLPXjusPPaWx0XUtIEPcdWpJw0RvEmrLIhboXtqVSQHEesWUcHPEdYbmucG-UFpM9BQQGQlsTvcycUKJ1bJmEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه‌ارزش‌بازیکنان دوتیم تراکتور
🆚
استقلال بمناسبت بازی حساس فرداشب دو تیم در لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31135" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31134">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=AiaZte48_mk0XFU_L1HAz3gdyahxDxcuziqut6rH-YHZg6atB01s_hBcgzZxs8uXxCGQEu5HYXxZ3lwzzaqckpML9xUnmOyCpX_CJwiNC03gwiI5T8QkPRxMKYgl33TaWVILmz9WlUKOIPCbRfSLGq8ct55Pn9QvpF60GDgwgbGbAn5UgIt9hDRHYYH1qDome0Kd_FhmJyfhJiSHKnIriXaJVwbnQjj2DmP58rFoYB_9S7DaJ8QJgfDnYB_Nd5msPUnSIb1PsAp2gNVx6Y6oJ3fOz7KNunilSF5L4pZDjhgASd7pqEmRaTeWv4TYA-cxZEp-pUx5Ok2yIsViCC1jG1J8HZ_U0Pbl-HaK3zORoc6xRY0jCDLQI5A2gWH412v-MracB8Pi9mPRF9guDHytwzg8wltv4VrT5ZDRPlX5lIV_mZOdgGahNKOX55UU_8Ctja0eSMKCUF_ypkfhXTPK0UgsuwtMyJAg7v7bVkWtJ84bmjr3ccICJnt-fRy070-5x19qLWCU-IOae6vn3Hs00yZ86xVo5Xl4m4f4z0CwAV6Ot_FFmYNdXQiCrOFJc1SzgS42XnOr0cjBoG_a8E8jXfjKX9Be9Dm6BIz4i98RZRVX--gS-5UYgKv_ThBzc4KSqQnFMZlemysyoqVcpZFEOLm8B7h6T_vjl6vEaACJ6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=AiaZte48_mk0XFU_L1HAz3gdyahxDxcuziqut6rH-YHZg6atB01s_hBcgzZxs8uXxCGQEu5HYXxZ3lwzzaqckpML9xUnmOyCpX_CJwiNC03gwiI5T8QkPRxMKYgl33TaWVILmz9WlUKOIPCbRfSLGq8ct55Pn9QvpF60GDgwgbGbAn5UgIt9hDRHYYH1qDome0Kd_FhmJyfhJiSHKnIriXaJVwbnQjj2DmP58rFoYB_9S7DaJ8QJgfDnYB_Nd5msPUnSIb1PsAp2gNVx6Y6oJ3fOz7KNunilSF5L4pZDjhgASd7pqEmRaTeWv4TYA-cxZEp-pUx5Ok2yIsViCC1jG1J8HZ_U0Pbl-HaK3zORoc6xRY0jCDLQI5A2gWH412v-MracB8Pi9mPRF9guDHytwzg8wltv4VrT5ZDRPlX5lIV_mZOdgGahNKOX55UU_8Ctja0eSMKCUF_ypkfhXTPK0UgsuwtMyJAg7v7bVkWtJ84bmjr3ccICJnt-fRy070-5x19qLWCU-IOae6vn3Hs00yZ86xVo5Xl4m4f4z0CwAV6Ot_FFmYNdXQiCrOFJc1SzgS42XnOr0cjBoG_a8E8jXfjKX9Be9Dm6BIz4i98RZRVX--gS-5UYgKv_ThBzc4KSqQnFMZlemysyoqVcpZFEOLm8B7h6T_vjl6vEaACJ6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از روزیکه جواد خیابانی وسط گزارش مسابقات یورو 2022 ول کرد رفت. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31134" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31133">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mczjF3Resep30tRbEkF8AxzIfC9K8r4_Sfc3PWZvOyX4Oai0w3K5DX_j1Fybw05zEaSOMkqUzDTSlFDP4zMzMDvaYNfItU-j5IpAYGxHgq7Ehj1SEuSes8BbMLlzmFu09fQOJVmwABGUg-hxtcyO9OYfd3NfA4UH2birmUdu7g-Y555EXm2EqnOdPNu83MhGMenuySUhnRUwmUK2Yphfoby_8_gWK2DEjMqpXOJFmMP6LdUN1ZN3f-Q42PWimRGE7H5mW_noMY8Rv4jA9xQFJYs7DQTLpaTlA5h_LCO9MayDx5w2W8pTbxLkr44EWR3a8d_CswWgrrlSJLJz8W25hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌ن
ام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری مثل قهرمان‌ها
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع و بی‌دردسر
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته، همیشه پشتت هستیم_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!
🅰
r15
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31133" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31132">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_NjULWZbleT4fNtlayzqeaLXakhgf4uEdpP5nD4lKxmERTttkzgw5WalUDTo1nfpdlmobx93v4FoVAu7aOtfL8AWK73pNCtZcyEF8tRoekYJwOMLtYq91GDkA8E501c98RJvz9npMEkGC8m3SRIxLrFNYXMRFsGiiJ8fLTJ1LfOs4NpC15NX-j26jqTadu8AeVaGSDw1Gg4_KnO8IPkZ8m5fudg_dnTNkT9-Rom42LFS1xGAADNZPiM-2rELaRMtY08XQiS0TOwoIzturRa_4d5JAddEVjoMV5zuF_d-NZpmL5iWUQcUUycNC7A60ajFmgIMnu-HkRJF341NWkhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانچسکو توتی درباره‌ افسردگیش:
بعدِ اینکه فوتبال کنار گذاشتم و پدرم رو بدلیل کرونا از دست دادم، همسرم‌کنارم نبود. بااینکه بهش اعتماد داشتم همه به من‌میگفتند همسرت‌داره بهت خیانت میکنه.
‼️
من تلفنش روچک‌کردم تاببینم راست میگن یانه، کاری که قبلا هیچوقت انجام‌نداده بودم. بعد از چک کردن تلفنش ديگه نتونستم بخوابم وانمود کردم که هیچ مشکلی نیست، اما دیگه اون آدم قبلی نبودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31132" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqbGRekIkNBCpE06sUzufrsQavVuZY5FgKsk-jnsth9Rptkc2A8y3_9FEfxocQL7PE0INtB6QFXFfOUwhL9v9KPZLD7BBNEwA3juRe5fjZxEoicQnMscKo60xZGadQnp_HBSUy6yxl-3X9uZtgPD9AWy0tCHoEUb6BRgm5w51_dDz6IpnkZ_UIA2kv1uLyEpdRoi99yzZ0pSg_u6UvNVsuV0SzRpKuTPBB3roz4orWbodfGn9Zu5jRnEjlrbuGgTTc4j3gchNIx0OkhSMzDmRRCjHyYgH_TisARIUrOtKVH-tU-K0KT3qWO7DiYdKnzt4l2H3VH1K0KToOOZZOZBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=V29ZdxP_wWPZW0htiKZXyM3kf5d7J6dVxVWAsIa-qaAWnw5P3UJuxShdhHOko5RyaEBQ75rFWyNbiHiJNjYc-I0xYSK4r5Qk_r9YhdiGXlZK1EuR3NAeRKKE5FKAatgEGMf71F5XDf1Zdt8qGaWjw-xaWL_Kp0AiyGTPfYyMwz8Ah3450vMfGXqi6k_Rne3bJ2c0gL0nQtJcqbWvGWdoy25zdeo5UAZI5uoCvTPbZ6n-YRNzrC8lTmYOqps-g_HSqfYh9UAczAaI5qnN4CXtu3fktVeJNKL4mibVvKZwqf1bR9KYMGWsZxt_EhB1o3JG1vUBCGA25DGuB8Kq7ncZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=V29ZdxP_wWPZW0htiKZXyM3kf5d7J6dVxVWAsIa-qaAWnw5P3UJuxShdhHOko5RyaEBQ75rFWyNbiHiJNjYc-I0xYSK4r5Qk_r9YhdiGXlZK1EuR3NAeRKKE5FKAatgEGMf71F5XDf1Zdt8qGaWjw-xaWL_Kp0AiyGTPfYyMwz8Ah3450vMfGXqi6k_Rne3bJ2c0gL0nQtJcqbWvGWdoy25zdeo5UAZI5uoCvTPbZ6n-YRNzrC8lTmYOqps-g_HSqfYh9UAczAaI5qnN4CXtu3fktVeJNKL4mibVvKZwqf1bR9KYMGWsZxt_EhB1o3JG1vUBCGA25DGuB8Kq7ncZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqNEMZedhK8ZEF1_E9ByTCUBXl2h-G62iJCN1PgR4SEgVI1F7FWypUvhYb8LljdwUdQ8Kahxqzgror7fmqGYPAyx7022ghTyOAR6MZretEBX9n-wN-v4rVDqWNDkJrh17NfLqufQPD6eztg4IyM0Qc5gD7dJNys0ql0MrZwcw8xhUkILqM3zbbPGzTQilKio1mLw66urCsXaU478WrZbs931jDaHeH2jSGKDwCRtsJFO4BS3OrXd9MABLcpzZTRZltWgzJdPAcjluJI0xNor7rhUTIOGBGqEiu-SkyzAvdvMd10MIDHUN20RZIQDr3zc-HrHr3u79pBdpCfgkLp0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY_m6NJTzjMcAORBEEsFfX0Hvj5E1bnJL0pBFQRj14ntEHZXNxIYqVBEJyG5E8eD9N_-sgTHHDREsAaYkRxL9_-CxuPmvvj2Ofw2p8sx_VuNBQSlpxREofBSVn4kMnQKvi2pySqxI-zJOqyx1DRpnVZtLUVmbKGDy6mIky7qOiHTSykMNAog5Iqsme5Qmrc-wOAGhhZPXQGi5RQf66HLvjpux7vYruvUWiUvDRIHSNStjMkwyux1yIBdR375JkinpvDuEdtWEAoR_tAjGYuSyGeXNntB9SV6c94qRAN7brrUEG3YG3FEGJL4-qOAMXJIUGRNqvI9s9Osu2rdAhh3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=n-pQrcbQoGJ3IY6CG7Z5QJslwGDXzL-9XF2wc-BujZioJD5cDKRswiQs7oki0Db_4jv--er8cGIF364Fq8wIv-1v0UXqBVMAfCr1ckBXj9uTzlq6eVnBsv88TXKbj847uvCuP9wQy6fUwzJJYja-s9Oq3wMeGB13KVhU0QOFRXLpVDaLyyVBemwFx9htet9d2CNfrY_iFa2AWPfq9HTLdg54Nhy-r-1YCwUPs_i4NEu_eqSkjAVREbKTQdCm_XYZ_Pne0_YAWXlIUNTsn3hKjL0EqXeuHYXibt_pH-TGujM7w2TmFuBSiKhkHUBR75eGqM3LS3mulk-J7wpJf7lazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=n-pQrcbQoGJ3IY6CG7Z5QJslwGDXzL-9XF2wc-BujZioJD5cDKRswiQs7oki0Db_4jv--er8cGIF364Fq8wIv-1v0UXqBVMAfCr1ckBXj9uTzlq6eVnBsv88TXKbj847uvCuP9wQy6fUwzJJYja-s9Oq3wMeGB13KVhU0QOFRXLpVDaLyyVBemwFx9htet9d2CNfrY_iFa2AWPfq9HTLdg54Nhy-r-1YCwUPs_i4NEu_eqSkjAVREbKTQdCm_XYZ_Pne0_YAWXlIUNTsn3hKjL0EqXeuHYXibt_pH-TGujM7w2TmFuBSiKhkHUBR75eGqM3LS3mulk-J7wpJf7lazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4lZXfg_yn7CJ5L1HUzBt37hfob8LjxeRsc5r8ln54vNCoMYIn4L-akzxLtXr4pvOLETORvpvZ12JYlW5p9z74eNCA7pPf6B00jr2eys6Z0hJodbfhwAAMvKNGVOKyY7NkxZnJ7eMI41QF5qJXbjTW4eyERrRhzlIKrtIWdaFciqePyPkkMYsCWkmxCqizfAtlAqfa7qHEwtHXvGUBt69hSrE6nLLG7OGjMKrWtuZmcns1WQcxLEeo0J1-p5_Mgf6CQObiCXCaeiTTBEkOiiTqvMfuX8negU6mjBP4xiGhNfViAdRChbDUpGb2QVlGzE9VaWPgBVOSuH-7xUPaoAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دو تیم ملی آرژانتین
🆚
پرتغال در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31123" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_hTLODPxzjN23RXizZ5QBlWvTDhe1RkGSfoFV-NYOdCxT_w5-eu0OlXk2goSmVMFyEwKExZTiPJ9uFa3rInfx1ysTOmOxcAmPgWxNVx4cFqwxM7-4eho3s_TOKuKiKXhtFCcgIHlT0SR9oxW6pPHUspfD5m3SRDfI-LSJR9fgC9Wz5SzLBSg5XRJxNhcaS67cXzrP9tec-d1KdDEeQxO5fo-dOQOmrWHdp8utq1LQYFzRcaUpT2shjcs0SRckEOeEapezYKXe1jXFMPyCqIgNOF_JOoUfreXGq6V443FVL1smghdAU9XdoYaMOJt8ocs6n2K3ciYLqzkXi9CD_SUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام 126 گل‌ملی‌لیونل‌مسی به تفکیک هر کشور به مناسبت خدافظی همیشگی او از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31122" target="_blank">📅 09:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awWF1dvZaNXfGoD6GnC5vASkeSugIjchDe17xkc9ZytCNGZ5wC_gcRaAdEACD1ed4ysmzww2S5vhCS8DqHkCyupcPm7FDRCnGxb1bHTS_svDmMtT_2eWPz0K-JjrFUg7AV0prJuGHj42fZ8ZAnjruqOp_ChVBYnOQBsi9RzyXffE2yefUOosk0lYko-6OTR0Uwqitk9SQUKbC1MGREPc4bQ6yqb2gCCl3F8lvF2x6Yw5gtrNrUd2p_D9_qzsUhRKOdqpVy3T29qgSeqL1Z76QVhQizQ4J8CkYFNO45HG4y2TVh0F7Swku8mmGdtbyJhHjenKnYeUkSzYpAKzsiQKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هایلایتی‌ازآخرین‌بازی لیونل مسی فوق ستاره تاریخ برای تیم‌ملی‌آرژانتین که بایک گل و دو پاس گل همراه شد. دقیقه 10 مسابقه متوقف شد هواداران لئو مسی روتشویق‌کردند مجریان شبکه ورزش فکر کردند لئو تعویض شده. ببینید خودتون عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31121" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📹
گل‌های‌دیدنی دو دیدارمهم و مهیج امشب رقابت های هفته چهارم لیگ ملت‌های اروپا 2026.27
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31120" target="_blank">📅 09:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFFjA-GZPD83EHef5fWhokjrGGwRzeWOg_tqKjj3mH5xFIAua80j0IJz6OBkHGY4qRz5KlePy7btKu7pPiUnc7VbFZaGgxi2mbOXVR1b0TvHEvE66zqP_YVi6ta2h4O-yALx4nNjybcTt2Y5ftKHpV3WTBFDpn6JhHyTIUa4uVwhCtgUYPNaGPsB9YxJMC3DF9Xyrbjh2oO0iJAmlBzjCEn3hUlWBGMqqXcRudf9_jkO5_Iawsb9SbDUWxykmF7zvwqIu1zn8sFNf0c_IzZLDfaEi0gG_X3IX6F1vCXj-c3X6mi--RivSGWgKy2aAxwd5icD_WlKKEkgo7TgT7Cb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfVVthnWsS4GCmFdp1jMgd-4e8z1SAu8WU99kMZfZitmhhColU9g4JPyHCro5j4H3CsB6i6He8cVzrXU_PBSLFCHt_jRTiM-93b8yh4DB8AAecibtym9gEftNM_Q5jfNqArbNxBZXdGUtupwIdzPcuAKNjjM_iZ8m5drwaWZIHrJzPc0NJEfGyDV5emm22d1nfCPrpx5iqhsGE2bDkON2UF__n6aZaVRSz1aNsAB7-JdiferHpGfIHyBmFO5j8uBnzjHhV0j-ePjS4Y7secGfX65_3CJyLyym4_xbteKnnPaacwjr7eh5HpQuILjrlBPqOa9LV6fQHDsHxJbo6BExw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4idZb4KWVX3ENIUFfbPn4-WKaS2RjxtyiRHxd6-8J-9UsRcMvpTsT2aABydnPG0AAKGqbvRKhrS_WLKIlRzfskPOjGMBl78jp4rACDlltXQzWPL6rzRNuHC6AvY4TcexUJlCcyL5I896ZoUkFmmNHYwafvh-zbVLOw5n-Ku6VzNOMMaU7v1X5K8OOkOA5dQcSEg7FxshH5rvrg-65ilsQH34fQ7xQn4gCYFv_LcUh9f3Yt9ewNGE7jZdA8u4yS-30B-3c9ijGC0NJiBFmwKl3KnVAF0HLToeYq-ZvF1X_oG1rFMuOkUXR6aD0uosyeN-I1mQmhBXdCWWOnf6K-KyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMTIFcruSexojUrEuKuSidQ4JVxOlznNc9Z-E_x2SMn7FUX6ya5BTblSjgCnp5T0wXfDIROcRbBLlRequDtfCJ-iFTtwQ19MiI5FslLAFLhWd22hkn5n-PYXTcsyycb1N1lodL8fEosd9hXEgB7UV4nyiYP9xaJPU_-tR7aspuLimJP6FbtHulYiKhsv8Dbw-KdaOusBaCSjRDvR2HsnxaHjOK7SVvKMkvMy3bqDQodUEUAkWnLBQsBoWVSL9HouZa2-f7wxjGbDsoT9swF2QAkRL-Tfvq9ujDD-_CeRpb7GD5LZF6Fz6bZsWCMEGcXhXUg0lIKJf-30uK7JRIW8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVCopghoKr2zspT-hySByyTapWCBFMdcFD8Cb_F3HsygtK-7cpyZ-jeHwltt7OAbJvn0RbImXR-PsTe-FIJ7rnx2NRmAJ5Tllwgt9VaJREjDnbrpF6-2s0L3w4Equj3-iyN-m0XhXX2HTrtyEhwpdKKOT9jDGD02enFYgqDf4Qn2kDDZpK_Wi8TmAEJp5o1lQ4OiRkefSRnQ4z9cFLWOGbNpzkukWnTJpiJVKt9SpzzTE7FAW0SbNiIiBREKJ9XKcIU8wrsNGPm9gJUIev4kjBHiFhj6MA-b-FoR1_1urBX36uAoTH0n28zj2EP6DAqMPS5KlnVLkBLsaoh1-9twDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31112">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3m1WVx_Zir5Hh2-qhpJD-K8yMKIqF-o5B_UZQw0RLbwTZWCcmdK5m0IcOQ5JZxvddl4afzC_mERo7kG0DGAaor8zKaMa7AHm_3ukUNwXt0Qu8Vqbx0ACf1Fzoq6hkBDKWn0A9POd29AqqCBwfQCTzCQEIEYibbF_FghJx7-bQti-0bAC44mXHjUuwhh4jxgRGhCvfmmLtZjEXtZQaAYR3WFsAM0-ol2ERb67gQH_fzjRpxa1E9ZSmUCAzh1jXTqfQfytmQJWiPds1fvz81lvjCJuILoISulKZq4Gf2F3kwOaDs2eC4dnquE4sFnUf8P4lZBc4WOGmruPJ-7Il2wSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBlC3AaiP-qA8UyAK5ZdVmAPyMzZmutB7OicAOgZnQQo9jEuAGFTF0HYrmU-iziQvktreJxHA5LqZVGNR6UoIAuhzinhE3L1Gfn78faqkXwah5jnvnqNGkLFxHOFWWdsTHgqKTLMY-mNLtvil8nSQOUoOSxkxOlP69ycIS9VFfagK4pdGLeKXct8DmG4SUNyYK9gqqc16CourrfiZqHhlJ6fI5Nv3FdIi8ws6EaRh4IAlBCEDCCHcTbTFB4ZITdh7VmgSV_EuacZXk0rZDefU7hHktZTf7j6te9xi4NpomqyCT5S3Vz-iOXhxmTaZXoOg6-kiaqw2pr-raoOd008Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در آستانه چند ساعت تا آخرین بازی لیونل مسی برای تیم ملی آرژانتین؛ دانشگاه بوینس آیرس دکترای افتخاری خود را به مسی اعطا کرد که بالاترین نشان افتخاری این دانشگاه محسوب می‌شه! دکتر مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31112" target="_blank">📅 23:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31111">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIsCCcTu_0wy789kgZSETSZFmY6_Zkk4Q7emQgDVxQJB0RcGwoN5RRalaBy0ePe-puSLJs6sxeBnMpSgUbzsDfgOISlAhmaBv262wQ0yQf1jbSPnisRrFAwIaG_Nnb_AfvTk7-RGVF_2EP6VYSwp2_dz61HcsDe7CuyCTtqzWCZUZCKmfEjqP8K-dv3y2Aivd0yiZWyb-wPGAonAQO7YsNYc6kLjNO6mkaTRPdF7pltNGq8xB7bzhDR29jYmKH-t3yuK4q_gAqs591DyWe10rgGPjlxuGnGainiMuZfzU51iYxXK66uCvl6C_JiT7D8eZQ5NA5XuXRBtLcPdyi8LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
مایکل اولیسه از ابتدای‌فصل2025/26 تا به امروز در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31111" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiuTf5yoRJL-y3fwCJj8D9sZRKBmiJ8OkxDZQsMz71ccBhZNpR6GPJGV4UrSBVac20ftnAKs24zA5PvYVOivF7cXHXG-8o4SfpQYkH_B4s5oNGakSBZcwu0722FPZQMK_pV9GpdjrOl30CbWt0l4Vyt8Ono8lzgcN7aLtiHbBr4rtjea8t5V7yytqp0ZkwxE09WvB4ZW97s0_QOyWFuYAwHW1mjYbptYU2BLWNOzv7i_4FvWFLIvhrB-AbLvI-n5vfoUf2AYz7sK0zJkKikZ50s9OhH9l9nspOiBhRjzrWyQRnMdRuP_xNkrf2hB3z4UnDrAK6zAxIR6_UOEdgBMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW1Wrr0hTrntqY9gX2avM9Xgb1YSRu_wXBuHxjX0ZXriThvnKoxIKRqKszG9Sl0w4qjyUbhT488fXJ0LnJt9U3gNnKaa-bfjZ2925DMaGlJx1_Kjlv65P-EAAVpRC2Pklx27JhI_p6FGhrV6kbnIa4uLu-xDzAhphoZB-k8pgCIuXBjk-JobHQ7GwT_H-HCKMziMqhEKofH3BW22slczgnyM_1gI3ymutiNtLTW45hu4EkTQH55JXKcPpe0oKNVK3q-QHt5Ykq0jbMqMlPJFUKTbCEHcO5IFqjK1aLlEKoYzAw7Qk8UD2ZsNR5uzEeiRzNvB1CaELRE_nYdiyw2b1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stNBjPJR9FtObunX2qH46OWovN0Y-7ihwuAUg2pV-QZDKi_CCd7lX1gRTKrjX6VVNp2uhm-MYhZzA5s0rt2kiMEhhm8kYTujYxxe1oD8ztZr1NALe_Fr5c9544_G2767EzWuI7H9OaQD6kpHMEM4VewtbM9s7h0-xCY1lUWwt_0HKxBoeFtkzVLZtNhSEgH5YVkccz4aIjV_Oskzme5COpjuALY9UWmoxNaZDoXmmUqRpwlGheBCoJ-Cim3Djc8OSfAvhdPrFuvGC9Wn586p4kGhGZWI8u_JtexT9K-q7WWCMkGqROyW3DJeficj-qkIPd3Jg6P_q-VAIlhftBFrBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaeUJ9hqopBFbkZ5cPhQForTESreOyw4vNawSIIh0NbDl5QE9p_jh4wHZ5uhZO8ng7wZOQWVqrKQS5FpuBE51aXFs4GHnBg1Sl38MNC7veuUlWMW3AmDaNQl9h97fy2OjCPjESlua47LYABy4WBO_IoIdniJ3tSXB81_5aVZi6JF-ur-aVoPIkLkaPJVbPsbVGLmvxVHWk3b7Q8HNyHGtkjkGvy_wG_jAgIC7KwNAV95J8unhoILktw78s6pQyQlCprpOjkC4zyDgEsodLsIX-zPF5koNjY8-0t8y7BYrA-Q4ZuufQSrZ22_bU7XRS_afgdof40DrAhv8VqVvXoIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=dTvLbdNTEbR-aOzOhhA2CUsMgueM9VlEA-OxiSe9KzWNGxy15rQDi68-9XJd0mtmPpezd1I-Ss3gFzYeTleB-CIuHQj6SY86IeM3GzWjb_vOpMxQ_UOS0xxNxtuv1jYQwXL1ZMxkNn35Um2iFrNRG8tVa3z69gxrW-OcaS_K1oxwofyyPoHO2ixd7fbCKswZ6NLdLKz-o9y-3w6DFGbAqh593zPFNva6c5wTitANeCh3rv9Fnw6-8F5_WmP08Kf0k8mJWKzkuopLmRh4eJ1rmb35Ed1e-troE3x4LnEzsUVd06jmGl-AoPlVv4md0OH2JYI4SbHtHl5_0FW_7KXzMzRUtbdFSScBrKBx0pfeK7yaCPt0vph5gKV3ixdSHjVJ9TpaM7JhTTIekq9zaKP8T0hlXJgwKlVS5vXlqLk9gJheEb0bCKBcKmQdHe_kSU1-A7R1e2a-4sCZ6LduFofaATvsnxIoKnX4RsTh4_9T5T9w7RADqbeqwhXtvaEMyfWG_MTCY9dQdno9D0-yCOZCjyjDUmO7jBPZdjFBBbbJB2DBCiiNbVH2jZ6TQn1riw_wsSHJoq5kR3kz7P5jDIVv3SQxX9jQ4zvms-DD-j_3uvQU2jLapXj1tQXJpCNRey9sxL6S0mfDQo59nzBUe8hbFHIt1WHdG-rSKG8GBSIRbNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=dTvLbdNTEbR-aOzOhhA2CUsMgueM9VlEA-OxiSe9KzWNGxy15rQDi68-9XJd0mtmPpezd1I-Ss3gFzYeTleB-CIuHQj6SY86IeM3GzWjb_vOpMxQ_UOS0xxNxtuv1jYQwXL1ZMxkNn35Um2iFrNRG8tVa3z69gxrW-OcaS_K1oxwofyyPoHO2ixd7fbCKswZ6NLdLKz-o9y-3w6DFGbAqh593zPFNva6c5wTitANeCh3rv9Fnw6-8F5_WmP08Kf0k8mJWKzkuopLmRh4eJ1rmb35Ed1e-troE3x4LnEzsUVd06jmGl-AoPlVv4md0OH2JYI4SbHtHl5_0FW_7KXzMzRUtbdFSScBrKBx0pfeK7yaCPt0vph5gKV3ixdSHjVJ9TpaM7JhTTIekq9zaKP8T0hlXJgwKlVS5vXlqLk9gJheEb0bCKBcKmQdHe_kSU1-A7R1e2a-4sCZ6LduFofaATvsnxIoKnX4RsTh4_9T5T9w7RADqbeqwhXtvaEMyfWG_MTCY9dQdno9D0-yCOZCjyjDUmO7jBPZdjFBBbbJB2DBCiiNbVH2jZ6TQn1riw_wsSHJoq5kR3kz7P5jDIVv3SQxX9jQ4zvms-DD-j_3uvQU2jLapXj1tQXJpCNRey9sxL6S0mfDQo59nzBUe8hbFHIt1WHdG-rSKG8GBSIRbNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgNbjtnewyeJ-Ftfs8cCkrlMtvMo8IusXa4y5y6ah77Td0L2gTuTB-YItoreTkqRHVGolnZlfMBDkUZWxrZ1b_cUuRQBSD_1vb7R2r3_4cRml9KL8YHipXhVO8BEPLDYpcKhnPrBBELgV9LBvqiqGWK5RoLA-1z8Y4kVz_ICkSsl7PNTWArDnowNS34Z6x-LT_t7j0Gs3WPCvv7y6VCX6dIQm0MqgChNnVk22CwCz8RV-ED0sHwFWELmyWHpuhP9_pzoey0vKPPN1K-A6If6_sDA964Pnh1dkgPrlQ8QXi0N_VoyB7TB40RuMgY-DZre0WMZVu6g8xY6AzA8Jk_S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYkK9bsMTUbpiFJg2OnWgl-7R6JNb1UnamaDxtKRsJNCE3iUTPBhZzy7GfngL6CieFxVIfasF75ATw4ZZkUyiTbe2OAKK2CIqc3lbwkZaBupUTyt97Dr-_aeQfhljWQvNeUGGO8KjQ8uobqW08racaw3haQKpagVVacmuzj4buawt_o0YOZjZOh9mhAkOt50mrSjUi1Kt76mrbRg3feBZqPCw0nRCSsq4omR3o4D9yNP3rsshAY3u2VqQa_0NkcoV2cFpT3sGfCeJbz4KeSbnxk172Dptf3ok8apobhqhJTXBzrn6LQu9L2AYfVJnfvG1mq8fqxPDIeIBcKBFfPgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXfWaDWmCQxkZvr9p5xudCn0JNEDubH78NeXK0b558qVhJPA5B9NJKd2_GHREpz4bnDUlyU3d4HyXDu9Nsc3smcOxF-Jx2V4ab6yWLtjSD2QiVskgelPW8ZC9raKtfOLW8Ltn-3_y93oQ5hgxiMkmMhPrm76oKaOGW9VqKCBHPItVQvCPoMdqXQ_zIhu0HDLEbHli9LWDY0_ocbko30dJpP8yzNsXsJ1iXxeY_B2cM3vYkrtgrPH41HeAwOOePi2gQJuoPF3IwGjuCPcZqL3iMffBLtAXiAF1LIrUmLdNgVFfmTbRrAwJYNK5F320DV0ENP3pglKd-e-lBqdgUI48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pta8S4-QQlqm-vQhTGl0fx2We0t0R9D46M_PVlBE_9wmvx2HvmM35AV74oWpkcNckP5BxmGzilIXDWQ6Mte5a4jLa-_Lead_ZqO58upEcil5mo_gZHT2Rq_MxDv67_wLoJU7EqloYFqz1LhkeAvNXGcTIpGEBXhLk5LVNea1QD8fHNbnWpfTtkTvxcEsKZd7PTt-t9FAwjoNyCsS2sIV0U-sTog1Ht536ZvlOhki1pR7Frwjinxx6oB4r2DlGkyW9AeiFV9osxk9AcnXL5f29FB5QSwFoTPjIIv0GU3ZZ9BHaWlCCBVgYsEXrerh6nIshF516EcmTZbR7_cfKXSbkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASDLBfo_oVoNoS9N_JPWakwmrB-4eRMQNEhQ_YzggxeoOLQwfVjfrFn9wD1Y8FAsmNOQhYlcs_JvKn3jitcOxuizRoQusi8yBjhOu4GOLUkdPp-z46xKEjI3ZV69xTX-Tq0rVb_ewjx6XLGnJMs0LpQR7V15N1ir6iWYeYn7CZyAqmZ3ibub5Uo_he7QRBdWMA3iaDrVWlTAPymibhmI8CvCfh8JxuhNTMJEKNYm-YKuJtmK-5azfihSBu7rQWuheqp_9VjMoaxPcaivg_qG_NOKZ0IhqqEbncGsgGh15y7xId3dhanZYNFNgGHBLmQajlr14FXwbBi1VWo6qQSVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5IG7_voAF4R2VfP8ohgQLdGotQ6IAOJAofYSdEbiG8d9naYV-nwutwGuHXZ1843BrPobF1RivgWvSNzkP9EsyL5eDoQpBFXkfxzjV-xIWzYE81DVy5GNBay79RysPmoYC2phevG8EEBmTmQz7Q3idRFKHhw_LrH0k2x6eslS8IwQeZhoVaiqrkMsHF7-oeG9Bqdl8q8oFXTypB9choZcppeydlpyP9lXEM-niLwbqlSgMbaCvbG3mzMFiT_9HQv-V7Eb7Etcg2796HMkrUpU_PzARyikcGLz9hzZRmsmiqB-xRxn0dGiKhalygeV6zcfGzQ3zX96hLlIzCynJYzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaJcJcKARNTQp-Vjm-oZbtGUTyUAaovflmsCfdtcChW7OKW-XLyP2Cf7kBASJfh53evcWDBMRmw4rIStNB2RB7d8-qnHjuJ9fb-RRfiPScHJU6RcQby1qzDfQSeNfgspvV05ToIhzyNfjnRUYZe9LGrTj3kqqOo9NnFZMpovLs2Gj4MxJc6qh0TqbS4dgmDeXbj6J9bE87bsz0olUpjkLud-rLKiaaySmAgxG0-QiNity9B4oyJMohXKuGg0teHg2Ygw_RPPz98YERxjDW6h7eFY-r7ApxLdxsZdZ0SK6_KzmdzISvfKAn8fdZq1royVqq0cqRewancvlnUfKLyAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUsgacZSkMco_SntVbULmZauhq253OTduStUlDruiiXJaD6MO0JRxLDQpIUoSlzM7e1QQbb2CFTLSn5l-dFHHSIL8tDTQ0qZFhscHO1M2tZ5y1FchwL_8CqU3ql5RiVe-ojeOhr12xbGC-5v_t_cHt1OoPhbXHHBnK0Sb1GbSqpxyN8KJellGEOp2aFDlmTHFX5PSfJ7EkdqjOIQQGqU5j1juiCeoJ6FCPaY_cB6g2mhLZ48je96R8GL0ek42JkfqAkkkpgQ_ya0emCd_UJy1tUkD9TilD8fLXC4ZiV2jXc45ZIPpKh60pL7CKM4F--4G4ttwl3PgFXmttH9x3CkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=UAfBnSmTCuZlQEw3OtBBEqiHmE5T7TPXeQ4piKoF7V3tla8vtVKd_nWHoIB2iQZyKa4f1MLyETtWLlbuLS-IvfPNa7nrwHCkA8T6qiS70wDAWnC4kEG3GGOPEmjoPm3hnWMLRacQJu9mk8wZlj3aXsdNwZZunihwdytPTAeLJCVqj6a8H1L1R0Psjn2MzHqzpgznz9gA2R0pwWyEEoO0C9dpRYLZwCuSK8WH_-s1VDjFM7BTvatHeu45LUsoVMJkG8u2_mtRZlyV5NjaI818i07J2MDpsZPNjn3fiQRHQh_c1Ma5eoptSFmJ2Kc8E_UcwFzfFgZ-gth-7zvvs80amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=UAfBnSmTCuZlQEw3OtBBEqiHmE5T7TPXeQ4piKoF7V3tla8vtVKd_nWHoIB2iQZyKa4f1MLyETtWLlbuLS-IvfPNa7nrwHCkA8T6qiS70wDAWnC4kEG3GGOPEmjoPm3hnWMLRacQJu9mk8wZlj3aXsdNwZZunihwdytPTAeLJCVqj6a8H1L1R0Psjn2MzHqzpgznz9gA2R0pwWyEEoO0C9dpRYLZwCuSK8WH_-s1VDjFM7BTvatHeu45LUsoVMJkG8u2_mtRZlyV5NjaI818i07J2MDpsZPNjn3fiQRHQh_c1Ma5eoptSFmJ2Kc8E_UcwFzfFgZ-gth-7zvvs80amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=QywmMw5h021TW9TnmjvBNBcob0KWARB7CMYsTktw_1q1HCS8cG3vDQWq025meqfO5j05qGcCZAC9AyOAdmzYFqkEolBsjU0euaIf8zsvTBefQNQ7rvT_j2RfnPDyT4jpXn9Ai5dBvT1zNtGhAcGKG9ERm3cRaMfAXYuJa6IqmS2DDRJaml1JCUjIMVHHPg8y3ru8N2_XwZcVJ2jWY-GsiqJWXxiP08Z9iQucFQt52czlBLnBHVVkYnflh0S8-SlG57TT4R0gCYCsIT0G3gWV-AnoI2oAF-os0t3ezFl5pLTkMJqyCCjMboPFZ73sGjJfRgvGXLhHx5uF4Mm305rMaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=QywmMw5h021TW9TnmjvBNBcob0KWARB7CMYsTktw_1q1HCS8cG3vDQWq025meqfO5j05qGcCZAC9AyOAdmzYFqkEolBsjU0euaIf8zsvTBefQNQ7rvT_j2RfnPDyT4jpXn9Ai5dBvT1zNtGhAcGKG9ERm3cRaMfAXYuJa6IqmS2DDRJaml1JCUjIMVHHPg8y3ru8N2_XwZcVJ2jWY-GsiqJWXxiP08Z9iQucFQt52czlBLnBHVVkYnflh0S8-SlG57TT4R0gCYCsIT0G3gWV-AnoI2oAF-os0t3ezFl5pLTkMJqyCCjMboPFZ73sGjJfRgvGXLhHx5uF4Mm305rMaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfXng0Ym5sVoEazkaGmvRNgHybRrQtJRbbkd-zmWqiV4zN8EB6SbDitEwyDOPHuZpujDvXW7iVwj0E5DooU4J9q2oGGxPoZ7wgRDzPYOQ_W281LJcUGJiQvPb4I7KpJeVCJHPlENqBPadpP4Qxr4-Iak74I8zochYqpopLYc3tpiax-2hv6oNjEHUDLARCfNhwFVSp8uzLEyriuy6XamuhbKtNi323ZDwb_BjL8yCHZtvIWeGtYHjVs9Mhqys36EpFjGJO_1gBhv2iZiEIVHnatiZM24xiJ1yJfsjLaUung-wU6e8Yey539NRfqjtBNFOyYPliZMT_tZSyu5ju9uZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=T84XdgGDs-SeZKYwBgdMvozum1oSJHZ1lBBVz10jh1EczY18e9ErITOXQOSwDyqw6acDSJGw3y0r3AWPaUH5UrgvD5l8xwNVwWQ8t_KVPzt561-Ir_gOcDbKa5n2ALSnsp1xYK2RtLZJlTbW1KbAJAPLHTjDHkPprxptGwnhqn6EKl0pfu3YyJAeToXyIJ7Ql-PJQjB9Kpmp4IJi5xEEqla6XVkfEcydINcVhu_66oY4A3IGlrlahOCb-o8RWEgRyMUaEcdVK8_KQHJWU49TzmQw0L8aLBmL9G4zY-RQaqRLS5qqvmWdwyqGQ-UjpVBC4BiOIBgEGs9HyTIJseFBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=T84XdgGDs-SeZKYwBgdMvozum1oSJHZ1lBBVz10jh1EczY18e9ErITOXQOSwDyqw6acDSJGw3y0r3AWPaUH5UrgvD5l8xwNVwWQ8t_KVPzt561-Ir_gOcDbKa5n2ALSnsp1xYK2RtLZJlTbW1KbAJAPLHTjDHkPprxptGwnhqn6EKl0pfu3YyJAeToXyIJ7Ql-PJQjB9Kpmp4IJi5xEEqla6XVkfEcydINcVhu_66oY4A3IGlrlahOCb-o8RWEgRyMUaEcdVK8_KQHJWU49TzmQw0L8aLBmL9G4zY-RQaqRLS5qqvmWdwyqGQ-UjpVBC4BiOIBgEGs9HyTIJseFBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKOpKdtFVJYcgnp039Wksfy5A03x6WgSrPqKkni3uZvrGz3vXON0NDdvm-7o5hWD7ahUsh03-T50veGY3xHTl2slcOknGeVRYnJMlRvlsPFBaIJ-fLIx4Z64C4QKq_OLczQbgCPeD8995raQCDyG8CNwff4cvSVtIY7pR9PM6zAtU8hAyGiT2mkxzwnYJQMCXTXoQO00y2K1q85eQqKeuxdL44VHJnHR-Q1d-B6OnAF0S4G0p3Wvqo5L52wT4xBPMoKbl7noR8uBzEM9YQWHLEbRL1ZvTCrT6VALt5Bjv1laCQbZE03QWXNsv-NjZIr8O11ewdMz9AdjmC0XVz8vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtWHyez8m5E4R3c1uNAKkpL_WCa4EQuG3pgVW9_Z7lbY8d8dIFbw2JXOjuYDX4p5LhM2HX1ZIMOnATEachbjM3kZoU8ddaGBMmke7NPPm9f_Wsz1J6lzbzJ_zZH8yTuaGIg6r_zxmwgPwfLaLpZH16xYHPSztDOQTxov6wr3JCWQbDaRHql81a35SQeXm1XCEptap6ZIdayWR187hofs4F9GRSbnUN_nHkZ1hn3foGxJXjmiAw9UTL4WtN7RShapIdrjJ69gTyJ5TfqYC5GjslRNEQUyvnJivZrjBaomi2elDd5-g-ikAqtbYwGHt3Imh-d5Y942dfWEShnU-c812g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=f7ldkGq0UitkXyWffrQbOKO38NLOkEcxYEGAwiMCrkV0JhTDszPeTdhevJTkoO6pZ19oJqOruNiK2bh62Df0XsjJhKDsdZfUH7-aBIsLe4UN8qQBvxXtYl8BxDHZgVbuDD0-kTGN_9laT9wVRVMEaXFE53oI2jt5AXXMIyxSH6bpaLpDGu0EAK0ShX5KcoJcL6KuGJeIUxxIcn45HSHiuju570y2OAQ6r9ioiTmLavuT-Vn3QKJIf38NSnZ4yAMzU9abhJ-UfHb3a--cmeJ7ReoL5jqff9bhX9n_FR-G0cXAq9IiV674MxsuZnJTVqlNus7I8DBnFDzMzsIPBgxGkj0YXeJSdyINY6R98xSQ69MFy3rA7UAOWF3-lBQ7nBkE6XlmLuEVnqLBDETja_PqWpyodSklB5Jq4VehMRObdtxMcUiRqUDzS54CIyfkLBrZjmniZS97dIlxW7aK2A0KykuAI4SAmzFdkq5Eb1ab89UsToRSdJepYtN7khAe9YRARDO-13suF0zy_-BaQoclW6EzSN7yUXRj66_eSlNxV_9-TdRJpYe5kyrGgI8x7iD4gbQO068vxMnSaIMqYRDS5nPA9lFRpjQQymJWlvZoknPYMpmzxPn_LK0cFPHY5PT94eleRIPJ0pblYWNKhRUIwARyK7NrPWJm4UziIcQvPGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=f7ldkGq0UitkXyWffrQbOKO38NLOkEcxYEGAwiMCrkV0JhTDszPeTdhevJTkoO6pZ19oJqOruNiK2bh62Df0XsjJhKDsdZfUH7-aBIsLe4UN8qQBvxXtYl8BxDHZgVbuDD0-kTGN_9laT9wVRVMEaXFE53oI2jt5AXXMIyxSH6bpaLpDGu0EAK0ShX5KcoJcL6KuGJeIUxxIcn45HSHiuju570y2OAQ6r9ioiTmLavuT-Vn3QKJIf38NSnZ4yAMzU9abhJ-UfHb3a--cmeJ7ReoL5jqff9bhX9n_FR-G0cXAq9IiV674MxsuZnJTVqlNus7I8DBnFDzMzsIPBgxGkj0YXeJSdyINY6R98xSQ69MFy3rA7UAOWF3-lBQ7nBkE6XlmLuEVnqLBDETja_PqWpyodSklB5Jq4VehMRObdtxMcUiRqUDzS54CIyfkLBrZjmniZS97dIlxW7aK2A0KykuAI4SAmzFdkq5Eb1ab89UsToRSdJepYtN7khAe9YRARDO-13suF0zy_-BaQoclW6EzSN7yUXRj66_eSlNxV_9-TdRJpYe5kyrGgI8x7iD4gbQO068vxMnSaIMqYRDS5nPA9lFRpjQQymJWlvZoknPYMpmzxPn_LK0cFPHY5PT94eleRIPJ0pblYWNKhRUIwARyK7NrPWJm4UziIcQvPGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdxBMdz3_tctRaf-ib80DvjkZEx6kpCl3fTUXH2mOTrj3IqdjBixGUdSpWQ7dEeOtm06CvH0e9kxzgq6KmNvE8bymOz0kTuLyJDZLhTdQVc9KUidMzcDtG9r8I91OjzSf4pdi_DIMHqTeEdEcLnNyaHJzaPnR3DCR3bXTmBnzceTk8y_6At8uw14P0s3MXi68QabZZQQn_ILDmmRLkqla_K3QGhZTx9Hgy8Vwbx1saOahDhmIFdwe91zAquqEuywOmfE4ebTaMRiIX-6f7j6VXXJacxh4k-2T-_4jKawt-KjeavJkiKs2vXhdnjSf61hiRUY2Yetf7zBZzub5HwIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMlUQhiUd5TRJn1UxUKRx0nLkz7AaC4fdrya5UxZ8ghxBzcM0kUMW7gK8nQHoPhBBcsMVG41xlzGXVYzB5TktAv7EIIDGgMwnP51FDA2kEqg8ezWBXgVCv-UiDx4euxF1GzjvzrS1wEaZ-1MPR4sJPH3x4zGQ_2MVbu8mCjXKsBNVz5uQU6CXharZUG_zg_1zST5voECBgb4mh6uWg3quqiJVedsvLS2qh6MobDdR05GqheJ1teQZfFgCUjJSDy9P7ha0dow7nZNuJt0kC2OE4vl645ZDyiPKxsGtXQTlUcVl8jLmhIxClfsAZjowWIZPBNlwOs4Ey9_opxViXJCYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGqiSGKs0s2lGs-EuuOcDNAfAMObt1lly3tELsXFiX2OLoouMpMjQZSMEm9mebtNI_d4rIg1u2QviSanrcNyMQnzORuZj5V2sY1AMfcbrAeazjLbgCgEUPE6JnDEFWNeX8_ic5Lm_hvuTdMSMKNQKnQ9Cyjcu18b3-uj-XgXhtSdTgomQ1wpU7BT2WqmWLKaqWtQMya5jcD5-PhXJ1y1T0bf2iDNvb47oNK3CwlEv3vSn9hYEUu2Ygh0m7HrEzqgUPG__hjcEkdXtCBZ6MrAK5VWMFsibLpjgnigrRRHOYZjcjHNS_wONXxor2FZKbZDDjEMPFigLq29LruWIYuAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiHTvfCWe2CEwntrOTdbZ68qE1vfDmfyicbOjZB9nCQ9O01kl_vCjeYCq87OjrxR5BqBymir1nitP5CSBIXQclzawA0m_pKyjPUaHwPaE-d951ejYP-au7d1rtI5QK8HwEjiYAzE7nd6GR0ARSU5ZQ-H75XUDsfLZ7DG6cSr-KDy4Sv08uWv1O23QwgM7bqXNTf_gUCaoCzmKAYJlxq5Fr7k5Y3sPoLXq3FOhEEdZ3St2wcskQKaL5yQgDZiBrTH3cfCwwBqmTtHCjm6FX6CeycE2lCOm7j0RRPNUL_8L7WhjTDWhPHievHz6jpiluU57szvIPzhHpiJMlv5Frv1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pr08S--c2HuFQN2Sp41s0vDTBDZiOux5xOgi0j_HpFFH1z-17KCdXPtIXGggJO3cuJKur8IjdnIQURKBbVsxDaIw-ZNRUJ8dPIixJbqxh_unGj9EONYhA0tXeMQ7rbkKCkV-WFxAy9ZTf-wlFHaGgGXyfyvcZVqx7x8_eiYS6LP8CjPomGJD9JTkn8X4IHxH_k-qWy2fe2O_-L-Fcy9pWTds8lddN_484R9gjfN2IiFDCXB3ymT4yx4xEAC6llTJC0AkDl7VfNkEUHwRjll5nZVRjlJaSBl693K-GNXxPlye3gcnVRjPwEPesBBDNR9DbEBI_UBegYF-jCArChoJmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkcG1FQTsPuj3N1pA0Ja51YF1XUUojl_M6eGaRW5dkC2vEyHwN09hMuGQSHY7jeknKnurxm-wSPnC48onLKj68rZ_2qHaA3O8m-bEV0WloPVSi6tY3Umt0QTBsHBx_kofViGTa7uCBhvByTG7zSOm_mBpM8p0QPOjZTy_qn0FYKiAkSSn-lERrOqevLwr0P74TyH2RNSTdhuTUSUlvXljwImachmBj7vvoCuBEwUL11Ta7ChW58rcy_o7eKfIn8TerN4Ii2LvSYpQGBrkRVoNRqT2UyOIGpU385ZYgZB9McC54ryb1jT_ICntGX7nV-c2RXkGoxXe5yI2mTjkTyB_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKic7HjwDqSu6i03mJahqvRzP1rtXgVi8jJ1pbDJ9P4DDgtet-M2Lxuk95tAKzmHh9Mp3jr6QO6td4yaXMKk4lD8g8Roqbjwa5w9QVPKRS4b86WQZwVcvMkuTvK7P9Bk_yNxPeCfcw9iR0aBBkE7MHKmSTntEPEQVU48KBMAz69W-BKHGn_uaOcstOhklgPoGcB1dW-k-SPAuIRkqbSk8nlTFIv4gDu7zTizUrB2c94b1pzFdo8skCkj3KdtcLTTVbod1cUHXIeA5XBSlfL4Bg-GMIOh2I3xa5DzxE0CXQG3Sxb0_vnvfAR3qkYe1Wvyyhi3hRAze9E7QLRefXFSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4bgVxzIb0BmVlLeKCsPqS9HsBNT6WZhPl-4FVrNmJuOyk8X132wlEEgmDmP5X-ZSChyRbUNjMIrFAAxxPk-yL9WniwxbyfUYk3311H99-Au0rl6S-VIJ3pPMpzpiB_DvNu8tIFAsL-WGxKqt6xISv1XvcUTRgWHb9bqQO1P3eqKvKcL3mJZRrxaCZKGAyfkPJPSr4MfzxdLC3k2g3-_Is24K6xM0T0jXy8KxCZEZT5GHqjqz3_1YpHZI46B5NemdSYrkA8SQtwM9tLDu5LEUkbrRdaH6szYgr8xgYxPfi08KGpflgMbcUp_i63YKbhvaEoSCKWTBaJRUgfrGk8T-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=mAxzsYvlbW4RMY8wKnjQ6PRyqz_Kngp2Z0rYcu3SaAfLohacp-za6Uwg7K5jJgg6vrBTEs0-NPyuEG4q7f_y6IE6GHPne0CWbQmO5wFunI8h7oOhLa5HVqKj60brehpYqG5F5WOVQxDp62WhOu5KCC4AlceMK1isuCPY5IqyWmmCKve9dZlci2PfNAbCds9IbxCZm72FX_Rkw_kv2afbwXOf1GlxYtis_nQc_DYxiaS7SNRw-6W9seVLtfXtEo1ttdSiuYtsqFX7kZcY3MeX8vi_KsO5SXWl8woyXBTFM5wkeOYgsw_bGMqjzjEvoiQPE1pSzfxfdkXtw1j-FGo12g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=mAxzsYvlbW4RMY8wKnjQ6PRyqz_Kngp2Z0rYcu3SaAfLohacp-za6Uwg7K5jJgg6vrBTEs0-NPyuEG4q7f_y6IE6GHPne0CWbQmO5wFunI8h7oOhLa5HVqKj60brehpYqG5F5WOVQxDp62WhOu5KCC4AlceMK1isuCPY5IqyWmmCKve9dZlci2PfNAbCds9IbxCZm72FX_Rkw_kv2afbwXOf1GlxYtis_nQc_DYxiaS7SNRw-6W9seVLtfXtEo1ttdSiuYtsqFX7kZcY3MeX8vi_KsO5SXWl8woyXBTFM5wkeOYgsw_bGMqjzjEvoiQPE1pSzfxfdkXtw1j-FGo12g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEo3IAuloSU9LPLOYaGetqMU-5Gui5O4Wf9XJgBn37sEpHCtlWazfYwupI2OH9s_1CoerJnRES85vJfKgzfDgCZxmG_d8nQa9oTmwG-h7M8_yGazboZEZWD3j440uIEqcHKOa5G7Ls9BFshhSS_Hzckuf6qy-Yw-Cbvl5x8hjS7Qj6hsSxhw4QSKIICK91wb_TmArc0De7FI_PudE-_wqQbQNqvncye4deRRgbqJxCYvkI3n3bbjFZ9FuAfbsWQFsG8FN6fAzFKeekcgiwIPJOn5hBI1l8g2cp-Hm3_pYGO6qEkMGJSX4xYgVs55CapfRqaD-UFJYQhnW8oVYFRONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=D2pQyTQACQSC9d2XOEat2G6QnYr6BqjcTKNzz1rz4yq-NNK0eAUWNS7wKIdH-gZQWhfybfK6_daq73wcemzXH1oSnp6kvLn4KWyZXGMx7rJ-z_U58AGc6uCJRTtxyP4J0IUApkEQOyRLZ3cViz37WZv5UaTvzpuwube2dqnUMdOnXxmspcc5YKtgdM6gqOKQ1YKnKo-isRCPtUx3whTlpIwvubk7yxrluvnoUe9viJc31p92yO_Q2jgHidEiEiopLLvJDQXszdH_v_wn_EoiJ5bfobAbw6fUAM7xEtdvIBP-6SZDaBgqXfwrJtCMDfhbq2ZGFNIHBEPkHPCAmSF45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=D2pQyTQACQSC9d2XOEat2G6QnYr6BqjcTKNzz1rz4yq-NNK0eAUWNS7wKIdH-gZQWhfybfK6_daq73wcemzXH1oSnp6kvLn4KWyZXGMx7rJ-z_U58AGc6uCJRTtxyP4J0IUApkEQOyRLZ3cViz37WZv5UaTvzpuwube2dqnUMdOnXxmspcc5YKtgdM6gqOKQ1YKnKo-isRCPtUx3whTlpIwvubk7yxrluvnoUe9viJc31p92yO_Q2jgHidEiEiopLLvJDQXszdH_v_wn_EoiJ5bfobAbw6fUAM7xEtdvIBP-6SZDaBgqXfwrJtCMDfhbq2ZGFNIHBEPkHPCAmSF45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAYk8J2payWQQu0wNVF399bWghUDXy_TEBBrpNrz-HSryMHMIM8GtyZy2AI-mGgRo54Wx3ijAmiiZZxkcQwvzLx5kCwNR8g93uogMgcdymoA1MNQ7qHemTi886QKdUbnGdChzN6TycPZubv87_71eJwKveJ6dZZU8a7f83zoNVvq8_NoPEwORwBg2cvQv2tkq04CzxIzWbGvG8zeZXbcwPPi8zUa48SuyjD58UqPiMKYl-Iz9xE35D-NfzcFOD9iDwILQQqnJhVN2XaQyad9CvoyTF_6OyzrTwVgZmWns3ZaJMRRei3XEHPBmJuajtFIyA4KVWelHWw7kLsg7DZMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=id678bIsicUiWUrP_3fb8GGYm1MlLyI2FAc5kio8u4d2cjeajMkyyJASfq3TDamgGiDybDWlI-oAKTVee-pEo_V4g5ANj97N6Y1ho85EiskXfq8vPtBV0jacLBkwmQFvELG_vwYlbrplw_YLxy46cWCSXDKwCjuJjdNC44Aqomoj5F9XI3sCCh6ej5kcCQ7eNIjjFD9cFPBWTJQGVfcwkdCkuGQFg-vXBJvAtAyzp46bK2OuBtZNqhHiO58OpTMu4n5dVivakLB0jfdjdZMAnYArauVgPPuTjPELXQBYJKMo0rfndpTYKIVq10zG2uSJGtJyvKQMfHKdFYgjMNoZ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=id678bIsicUiWUrP_3fb8GGYm1MlLyI2FAc5kio8u4d2cjeajMkyyJASfq3TDamgGiDybDWlI-oAKTVee-pEo_V4g5ANj97N6Y1ho85EiskXfq8vPtBV0jacLBkwmQFvELG_vwYlbrplw_YLxy46cWCSXDKwCjuJjdNC44Aqomoj5F9XI3sCCh6ej5kcCQ7eNIjjFD9cFPBWTJQGVfcwkdCkuGQFg-vXBJvAtAyzp46bK2OuBtZNqhHiO58OpTMu4n5dVivakLB0jfdjdZMAnYArauVgPPuTjPELXQBYJKMo0rfndpTYKIVq10zG2uSJGtJyvKQMfHKdFYgjMNoZ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eElOirTxooeOgz7z5ID7K9712xj9tK8yCCVnvbatQLRaWzH5mZ7OPbFUUEadVf1gkVuoR2YwY8s_XOMSs2g44YCJTcaFax1iRDWftJI4PBOf-92uEHopqFf3hPSAe5E6ZgorXnUaBXUbS1nx0AvMMTgOWCvzgGPL2fobZ8gEXEKsAQ4zkXpe5BfjWjHgCCWL1Tsl_h-ddBLchYZ8PObVXNdoIoL5FlqON9ZZHh2ancT0HAUuGD8Vzye18v0s_NMR2g_uqluQfXoYTQK6qNHx6G4mkmsLSFM2RRQbqSxdidWF4Zjot4CirwkEcnp-qRVNYJDt-6ohOkzGe8vo2idWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCwMzmRB4VSNu_QwhEq-oKaZ79r_ddsl0GZFk6IvB0RDdKNMi0KUxANj1TV8LOJ3ItKx0efXTFqybPU1VaLchwrNGwfInPczj1xgpb52Fb3QoBFYa1j9KXpAQt3IDx0SwDV9oBrhCWA6L8ejo0l35ytVJRUUN1lNJNWSoa5FU8A-YlRMFvDM5_hPJb1HLTUaI_30vpSuYz8ZBoyZE-YE2jnbUQ-w0Xn5dko7p-QKZXEVj1DwaRzOSp3zKpCwQ_HoZcXgDdZMbWPdFh8WgGGV3Mn6AOJe-edOFVJ9aejdgSBymhOmjQIOzNz4wK6gmByA8Hua9wjmRCBzB-CtrGRfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1OhvksG8H9qXLUbPUKpsZYZ2zobePivzPjOBFw590mqjqar2LtwvQKVPKkMkz9kCkYLzKTUHI8WY0pGl4_cCSjFHIfKEFg0X1IPFtZE7sDnTCUycobxZZnvvswXc8H7sG-vebY84dr0ePmGMlMaJruCAodiPnfL0OfQpeb5s2SP7uGStW_FtVZR1YCBydhewWn_dy4kG2g18U0td5bM6bXPpg_WFG0aSM2u9NkBHVeW_8cDp7x9nxmF8-cb6GTg3eSj-4VXXQSgapfucNEGQY2TBTf_Qp6Qz6ylG5jSm3i2xXcyCLztv1RC_sQBW7nxP8nyNJy896-gXic94IZaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvycFsM-YIoUVL7bGWkdrcOzeqh80ZxMzhfXsLanRirfpmKvmMkKKJ-M3VmYpPEQYvfdK_LLBXOm0lVK_dJnwlplo03seVz0Zcd4pcKu1RvsaWj_XWlBZXtmUcplv8Su7H-R0yjovD3P27snibjihqqkEr4shp_lcYcBbo5ijE-tmUskXk3175oidjqSyaAMiltFPdz6CxkHm_IWtkzi1EqzOKTz6MOLKnqWCWgD0aeEUeRRypQFN1cBigI-dXcwbNcdDB0pCw1LHFdQGFkgMsxnP49bIhWoNXc_Jgawwy72jQpumk2JU6kCpCF0IIaydxZ_ybm43rgqQyi98Hd8-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=hEQrm2GKracDdZRA4gTqBT8Jpntsnh-mHau-vA75HocR9L3UbXZFxS-CcQt5sptMK4gr-nJhFWNyN2Okxtgcf0lasdhBGU_e1s1Jrj28ZQMsGOITIJ1c-gEStAxU-1yBxRefhkiqe905nRkPjdZLKTwImMceeU8hJmYkSYGLa-F7lynfAEt4i-VC7hRUM5jLIH6kNgyAtPTqawyjjbR5uT8yvVMemCAm--nn7GuozXJDmSJdAvpqlyjqYGV_Ic8CHjdFXy2phOP9ICz_pD0iaG9GQ6_rY4_wOh8B5H8zfWN6bOHzyaiMOb2bbXC90Sd2BC7iTweAZ-BStHgmCq0R_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=hEQrm2GKracDdZRA4gTqBT8Jpntsnh-mHau-vA75HocR9L3UbXZFxS-CcQt5sptMK4gr-nJhFWNyN2Okxtgcf0lasdhBGU_e1s1Jrj28ZQMsGOITIJ1c-gEStAxU-1yBxRefhkiqe905nRkPjdZLKTwImMceeU8hJmYkSYGLa-F7lynfAEt4i-VC7hRUM5jLIH6kNgyAtPTqawyjjbR5uT8yvVMemCAm--nn7GuozXJDmSJdAvpqlyjqYGV_Ic8CHjdFXy2phOP9ICz_pD0iaG9GQ6_rY4_wOh8B5H8zfWN6bOHzyaiMOb2bbXC90Sd2BC7iTweAZ-BStHgmCq0R_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyRS77YPHQgJuxH8ULxWDChwGDAp11Jqu4YhBfCAyRGL12FsUjnsFhHKvjoSOmLG8wI4DT5vSh_OEjhD9D_e6OCosGD1Y9hdx6j_0HuHP86E2zYxVJSrJURMOOyXRcs0JRAscNJ0qLEuwtQB39_-oeIAFZb1eGWj2leM1DexbyUV50UZxUoR52iW8dExy4wm1S8ES0viUR7QQhl_bT2DImTZxf1lSLnOvpdgxYNZwJylKHOF9vRgmVWDgTUvCmhTo1Byafe3-ad7SqIGWgevsQ2kkkuflnpC2kjGBISXI9WoVXbcZIkGq5syKiwIWS6nUBT03Poo3uBe1dV4PUZ-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB3YdiRs3F7Kch0SH6KrXJEDE6T-Wyn_xQqRunDE0tEA6puFh79du041w28Slb3d9vsGbI_LRJ5MVqMyKFHgj0MG4Sj7-ftpM8y0WWglRPkM1bRxqQjxzFmBZGiD829fGaNi7YuWgxqgH9EzPYRI3Bj8huUj5UJscY-0v5PI-GZLvGDnXKKrKmOY-U7fy-AnAqclMSxkQBxqgmiRilk2g616vGH5FaRKu9RUXESMgVFtdd_tk9aMjxVG73FJz8sVtrQFEbr5SY0UKYKaNFUNDzRap5Fc_BwTwq7jQZN3zdSlFRSpjeIpOeR7Qsgj4qLV9PD_mFOk7gO_NvRec5bKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgp4KTHQMCEBFH314CfnrwvDFgBKpZGYxGzAoSTnv5tixTGC6K5J8xGpz5l9QUFwUv_AHsuvA-IAMMflYi-tHf8nr97Q5sJl_q0aJJRnSL-gTCFW92tZc1e8xriQRf7LbPt3NA20bBdqtzch_pIuvsjnKkcNt6mma5bf24hE4ahBtKT3kRjberKhNTAtW-NqGmsjDOpUHsWs-Gk5akoMnyTNloP7Qy_AuPH4XOm8DJoG_x975_6GJNGe7z1gyMHJMOrrOO4f19Go8Lkg8Enrf-sJ_fSJ9a1WPlv36hab9WnJEeOFg1VMON_UX0_MqXpv8xpIuK5Rc19tgdUQG4dxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=XA4dC98Npgg0faTj_YN5W45LGELdgUgrS92Qy68AKmPQGxIRtsKoxMFcQVkQL8FVbY_2MYUrjMdzO4denD7PFbWLn30pPKUa-xfLSu2Zem4LPmdZTUotmlsyYljjzX6zO7rqobWSjUNGknb2VluhLFv0BwC1vcBgxFCQ3Peazex-HkaZYoHjmibpZ9JzX9P6Fwflc7_tJSMY-74h3RBvgvYLoWW6olVKoGkdkI2laeTG0OG4em7iNHzzLaI2MT3q8yPU-LhLXlmq0Ke7zfvKNKkgAX_u93LlhzkVNcigygONVK9PCFKb9BdHr6x45rIydzidWl992j5UEZOp85G61A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=XA4dC98Npgg0faTj_YN5W45LGELdgUgrS92Qy68AKmPQGxIRtsKoxMFcQVkQL8FVbY_2MYUrjMdzO4denD7PFbWLn30pPKUa-xfLSu2Zem4LPmdZTUotmlsyYljjzX6zO7rqobWSjUNGknb2VluhLFv0BwC1vcBgxFCQ3Peazex-HkaZYoHjmibpZ9JzX9P6Fwflc7_tJSMY-74h3RBvgvYLoWW6olVKoGkdkI2laeTG0OG4em7iNHzzLaI2MT3q8yPU-LhLXlmq0Ke7zfvKNKkgAX_u93LlhzkVNcigygONVK9PCFKb9BdHr6x45rIydzidWl992j5UEZOp85G61A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AExdgXi5pbqE8f7eQyFQixkYgW5VzEfaTbRGQygRfJpWHZw0A0Rx_jF1FsPj-1Iu1ZrACOxYBbF_XI8tqsOMwOhCXJ3R7xqZudEllV9i53vFlJGkGaZg2D6IeYsOiyLgxwQ9UkYxfdWLTC2RwdqqlsW90VmS0hU74JlfM4MC2BTtn9eYwyRA6CYxe10xwyKT0e4hjO3v8azV8phLw1LeLdCcILblkAG--EeD1tUnGWIah3Tj6suEK2n7OdrhsmnSk4qQgmQemtbFjTs4k855y61hFH00nNttHcZEfnVWyVaU9In3eTYjxMEGzng7djIfJxyLxnoLSvnRLNoBiBizpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqWCUbhNQ8RKerovwlnYGYhRlhYoARXrHtGlIAaKRygLSJeXHyTrUiJTBf1H-0tV-aPdH29pcyChAvP3dGEN_YSJblukJmMZ30I-8HzFgQOgJOMYnbFzVWVKANERJBR61OAkml6H3hy6JcvKh2qlRwL3-SCtaqVYRtagjWQJAUFV9rmWEz9g3eJ_CQCBW5HRpVmvEvzHV81UJr8CA6rZerxV6jk6n5p9qMyi4skOKyS7KhcfecWxZlHvaAgYkZyy1BdUrIeL32EMsaV-kpoonBu869MLVELW79jqWZ086_8BCxPTmvXAovtMyfuJuNL0wlsuFrw-1-hXrNAQP-6J0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=FKJRaOPdwBGEOaVvwHLnUjxcAyEymQ-4qrt2iIZnRcSxYSqmcyp7Hd0Cx-zhOAoQLdJo1L7BhgWJXeNYYPBEKV97Pvp40FrL-URQ6K7ETCoN89NHRZTQkZ4aIVB0VqZLx6QKjv8LJZvCpHLjoxGQfD34-Dkt1zghTRlTSkkFgRR1PVzI30STQ4plC85ctcEnN-249RD2cg04EbsweX8DP1PRY8ZhMtn83Pes9z3dMq4J7M6gTz2v9IguI7dAkDwDqQYPR0XynFWtqlwC-Un2uWQ7O8ipFD6iRdd0HOw3EuKgPOvJcVvCOylmHwQehdndF2HqIP4sqrhFZ4B2jj68fTD4KZQrQDBmJnsfkv2kFT99LyRSyM-FO1zZEE7QgwijEZeQca1nHo8k3h8WqmZ5VNMKF_ci29GNVlM7R7IdcKL_Yq5ydh0fo3VqCdeHD9tdgWIBUzyk5dkPScl3tY6miRh_EHU37h3sMhjRQ2xw8LCV5S4dLIdTLvrOilDxfyulWEDyTW1GGJnG0JVKIMhDLFS3EtiyRjh_x8DzDlF44pW1t_jkFtWsfCFMgwBdE1fHFL3FM2dNjwdaLR1eEzWJTAncVb631xDC5LFfTbiu6L5Sf-Fx6Jg9aVznmw_ZB1YKGt0jtebVK8JWypePmO5sNE4Xq-4ryHeIYOAwytLzRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=FKJRaOPdwBGEOaVvwHLnUjxcAyEymQ-4qrt2iIZnRcSxYSqmcyp7Hd0Cx-zhOAoQLdJo1L7BhgWJXeNYYPBEKV97Pvp40FrL-URQ6K7ETCoN89NHRZTQkZ4aIVB0VqZLx6QKjv8LJZvCpHLjoxGQfD34-Dkt1zghTRlTSkkFgRR1PVzI30STQ4plC85ctcEnN-249RD2cg04EbsweX8DP1PRY8ZhMtn83Pes9z3dMq4J7M6gTz2v9IguI7dAkDwDqQYPR0XynFWtqlwC-Un2uWQ7O8ipFD6iRdd0HOw3EuKgPOvJcVvCOylmHwQehdndF2HqIP4sqrhFZ4B2jj68fTD4KZQrQDBmJnsfkv2kFT99LyRSyM-FO1zZEE7QgwijEZeQca1nHo8k3h8WqmZ5VNMKF_ci29GNVlM7R7IdcKL_Yq5ydh0fo3VqCdeHD9tdgWIBUzyk5dkPScl3tY6miRh_EHU37h3sMhjRQ2xw8LCV5S4dLIdTLvrOilDxfyulWEDyTW1GGJnG0JVKIMhDLFS3EtiyRjh_x8DzDlF44pW1t_jkFtWsfCFMgwBdE1fHFL3FM2dNjwdaLR1eEzWJTAncVb631xDC5LFfTbiu6L5Sf-Fx6Jg9aVznmw_ZB1YKGt0jtebVK8JWypePmO5sNE4Xq-4ryHeIYOAwytLzRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=ENNPU45vC1zF1_t6LWIy34zRbGWbNpPzyXXTlx-ISDjF92YPcP2W3HzLz37GSQmr-shmS88qHYPx6w3oc2Eg08dNQNHcaqUFgkGTGHtTo8iTAAYOx8f0DhJV2dlYO7-n4J0VGemIWf1w6zzGnZiQ7z5ZSh-1vZTllGSuYhQoUTlCdgHSQZ2qouQViMQnYvGZxOaIhQ40rZ3YA1so8LCxGizbi8N0ssKbFxd2-pvsAWTusDw-v2yOIgWPvUVCEamYCmD9821gzZBGbZ3o6NT5K-7HHj6E_GPBmRCXGhP2k6nxEKyrKczUKm8_O9qvAxGrMmEo7j6AcCk6zykaBNWUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=ENNPU45vC1zF1_t6LWIy34zRbGWbNpPzyXXTlx-ISDjF92YPcP2W3HzLz37GSQmr-shmS88qHYPx6w3oc2Eg08dNQNHcaqUFgkGTGHtTo8iTAAYOx8f0DhJV2dlYO7-n4J0VGemIWf1w6zzGnZiQ7z5ZSh-1vZTllGSuYhQoUTlCdgHSQZ2qouQViMQnYvGZxOaIhQ40rZ3YA1so8LCxGizbi8N0ssKbFxd2-pvsAWTusDw-v2yOIgWPvUVCEamYCmD9821gzZBGbZ3o6NT5K-7HHj6E_GPBmRCXGhP2k6nxEKyrKczUKm8_O9qvAxGrMmEo7j6AcCk6zykaBNWUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqqS48mPgQVGhXaGXEMDH8kzRMdxLisMig0ZpRikXheB1Id7sN2ofHI0MGGC2rosU0NV8LiKCNloX2XQXgI8V8Mmxs6ylD79rDIbMACOudG-IW7qQkvw2VvukSg7jYrcY0IYftj-6UvMvgeUnvcNLD-THjxgn11X0gV-Vc5llhwOxU_Wu4bWDIJsUT4x4z_pG8FMKtvd7Oq65iXDsdst1Q4QAoPjAhc3HkC0D-UmciERQeV-UkxE_MFy_ToU-uMvnnVGxp49uEgBo3sipoX-U14uLSYdjpVn4zV79oeVLjmyJ0WRKa3qPMtfL8HdVsRNcAzNUJhCLta80FJ-Enw-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=ZkdJydhDzWa801oC3n6Uvq4JDB_ZEFoNa4gykSu4uOc6L8KN__ttLrKS6Voo_ri5k_BYDF2RfgNudbKiqohmH-smj-YqBuySsjuoP5iaMVP-YP31fUFIc4K6Ie8gupVByJR1UQePTvJnpsbvPy7w0ZNESpeAwMx0t_OFALE5ZWITAIMytAIS4N2Cy6Q3uMU6lFvsQAwAXqOYtWnYf8tYf68RT4KCccEHuc6vG4Eiq7bYbPBancZTjL7s4p_mNz2AY3R4ikvp-ynEzRYhg4VGIL_reYfnlBrElhvNe-0eEd4l3D6dOmtdxg3tMrdHJqlavNZxplngeLNAIoRPFWWuaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=ZkdJydhDzWa801oC3n6Uvq4JDB_ZEFoNa4gykSu4uOc6L8KN__ttLrKS6Voo_ri5k_BYDF2RfgNudbKiqohmH-smj-YqBuySsjuoP5iaMVP-YP31fUFIc4K6Ie8gupVByJR1UQePTvJnpsbvPy7w0ZNESpeAwMx0t_OFALE5ZWITAIMytAIS4N2Cy6Q3uMU6lFvsQAwAXqOYtWnYf8tYf68RT4KCccEHuc6vG4Eiq7bYbPBancZTjL7s4p_mNz2AY3R4ikvp-ynEzRYhg4VGIL_reYfnlBrElhvNe-0eEd4l3D6dOmtdxg3tMrdHJqlavNZxplngeLNAIoRPFWWuaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtkkoZcAMRAmv-21h73OIVg5fnB4wvl_0luKZHMA9-2rlhiQo9dfUsgH4BLNgQ_oblQg4RdS1R88xwgHSa6jrWZrYKfzg47UjPGzEGHi7_bTcXSBnj3Fc2d9k23Oe88zR80kcadnf3o4SWXxNFgXvInu6S654S9PgiNZx40h_Qf8d1GPO_IxVZEAwTHCSHtbJ41YI8NtyuVrSfZ9Up8nCx5lkki59OJ3v0dBHn94O04Is5q88v-BPbF_ukFZ2CE2sxw4IHCcrpuqYqEK0os3YIOZh8-DXtq93PQXd3tHdJ5oNXPOzo0HHHtkmgm4ySdsH7pzvIy0NSAvVDGSf53ASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-l8ur84IJXMB02YelX5iAo9CJBLPXlZ-eAxljLAFlpUCUEyIw2kccFrYygx6YJbs9_TyEthdN8m9XHY1y6Upie5AdLo8N65eBweTCqIdOqxcYuznJk_tmSx9F1Gyxoqnkt-5afufjosyP7W_u9alJHbJQ_UqAaXcgjUc45Oi6fw1nw4I7fsKXGvEKnXuzMBC-OPUcj90upNAXJ5rz8MscsuwfkVDMaV1hpLjpA-xpaiokRljTxRUmR7xN5nP-Yaok44b4HPIsfmJKnIMzHAouhzGvyfNulh-nXOqt231l9fUYtBrfQ4n6JobavdbIixkZdT808OthuoVrJsyJrYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=Ftm-E58vz_UDl1gn20SbeJOmJURc_TSltlx-MrOfrZvklzJYlaUyaC25UDcCSK08dyTPd1dSzisACfcYm9iUvqKE6Qw3Rk0GS6YoYmCzRzyU8RwTm3HSlbBgxGgp8aQeTszi3LlzZ58dOD5ioqlk6zy0YMHB6HTtci3maP5LCPAkNWIh4m4AP5WChPumo0JMq0C3q5thRcp0Atg13vSNeiOwgYMvqQwUHw6dYpPlqy_8xGkBt-uGzl29YU3CL3UGRFnIH1DAwJ9d0hhCjcQW65wAXvmV1__Po_R7gak0voaWWrUQFtKlBmutDMTwElQ1mgsfmGnyOf3sEB2XYXjeQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=Ftm-E58vz_UDl1gn20SbeJOmJURc_TSltlx-MrOfrZvklzJYlaUyaC25UDcCSK08dyTPd1dSzisACfcYm9iUvqKE6Qw3Rk0GS6YoYmCzRzyU8RwTm3HSlbBgxGgp8aQeTszi3LlzZ58dOD5ioqlk6zy0YMHB6HTtci3maP5LCPAkNWIh4m4AP5WChPumo0JMq0C3q5thRcp0Atg13vSNeiOwgYMvqQwUHw6dYpPlqy_8xGkBt-uGzl29YU3CL3UGRFnIH1DAwJ9d0hhCjcQW65wAXvmV1__Po_R7gak0voaWWrUQFtKlBmutDMTwElQ1mgsfmGnyOf3sEB2XYXjeQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcZ0vqdK6mzuWkB490vw4cLPBdLMQfCKrKUh8ZJSq9uV_hyIcWmkq9axkdm4RFbz_4Tg-qtsqEpU8B-HNOlU9QQ5R32Yh2lgW77TXFpesMFVHaBqvINzGhbSdo3KmAoMMCWwJ1XD0fvLDyTedvAWJRr0_DYl0oCG9Y8yUwn4iFXp-s_wI7SIQfNAT9D4SijJ9GNVlSdXKCRQWNsV1Bf4QfwAk2cNa83FkuS64nqj2EpCKtTZplw3P8Xv3wBPen8WkwPN-tsGGTmvGAxfSorHA7qMn99s2bJJJ2k2yoQGmHwM-fkErirBMEO858RH22jW00Ak9sd8MvZnOJOTUjLufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M84ipUwRBLW5_260H_XP0H3UhEk3lxnJulaXqPEC8WK-yY0F_jJw2kt2H5WbXbUYZSmN4EjexbzKHGfUz4PkZOsXr5TRAAIxgSgh9FzuTltTbVz3vgdbgBuhuoaavWguSR4iZhmbV7IxSiDoXx2LUaNORwO7LNMvb0LsxJavJ9q5ClxpUC3TSa2A5FkrScCaDAVxesv3wN2Beog_UHteHZ_fnOEAtr7eonUTYoRcwIqqV4ZwqBxc2Z9OPzt-ie6mJWO5khqcemF7Xsy3UIiTHY7IjxrvQTP7hfiItqHOOm-6R4Em_1JsRWX9o-oyR09FkHiRFlo-nk_j3vghrE9s5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=orKTjXMhgYBxG83RjMq4m8UNyZxVl-rf8GstjWeolK20QVOhNdVwlxG-DQMmSM19frpEiPkLjRDw-8OwvIUeKqdZ89opMVyDKXYZ_GpPAE2JO5Z5MWiLZdQwVT0WzMaGPd1txrAXFDA6q8BCITGFCDqbO7fVf9KEnHZEge_hGT1BFDPGaMIi6JAueH2nGUUceBYKO0dG1arKsd2Gs6KbTCcQ-5YquRVhuwbj0ooRQBJuxixxe41c9Gqc0nIgghVdp0Ug7UG4FIPZIkndJTrjBZqWfIHckiVB1_q08-wWTIqNPbwvKUf1HvUB1eRFdvkBePnqts6nMBrmuRMCSJwmhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=orKTjXMhgYBxG83RjMq4m8UNyZxVl-rf8GstjWeolK20QVOhNdVwlxG-DQMmSM19frpEiPkLjRDw-8OwvIUeKqdZ89opMVyDKXYZ_GpPAE2JO5Z5MWiLZdQwVT0WzMaGPd1txrAXFDA6q8BCITGFCDqbO7fVf9KEnHZEge_hGT1BFDPGaMIi6JAueH2nGUUceBYKO0dG1arKsd2Gs6KbTCcQ-5YquRVhuwbj0ooRQBJuxixxe41c9Gqc0nIgghVdp0Ug7UG4FIPZIkndJTrjBZqWfIHckiVB1_q08-wWTIqNPbwvKUf1HvUB1eRFdvkBePnqts6nMBrmuRMCSJwmhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
