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
<img src="https://cdn4.telesco.pe/file/Srx4A3R2-yP7fkCt3oks6v_x6h8FgJaxkfrNNZoQcFKyLUpMxFIPb9BHk7ra0FZSmSsPk2H8nHu7Ikd7p_wgTpYIdPHk7nEtLaKkOqPiwm8FeR5N5jIh62uYuMXLDIABDCKCmx_3svbrZS8pU3yGO9w8qNEtK1pG-4kuNADjoPAYLhEaBs4aqUWuFDwp5zBfyGvmbdG2H9aklRW6wEH5VN42EGXcxCBpeNcSn56b8kMmApf-2iZXaGXTW60TfjY19KiyvDl58WwOdq-FoCTVa7LCPvL6XSoVZarKYONQJokyow5WYA-ac_KLc0S4J-c94ob4aprqKdYKuLiuRzJV1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-436373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPfluk8emtv_fVsJXjAzIqay9NFXRjMstH7Zkm69x0rD_CkooZ-IonFLKVa80RVmKikamSdBqwmjKyBlFp4eEhW339-aysfWWhxN6V5UdmOLSrn1b4DZWAuT8Wa3RsjdOk5YgX90_VRUzU52vq6TZdULBNNjadibhOeG3_XongVsb5GN321ZTs23W3xsYlGlSeW-0R__FbnjhBRDyk5XOB6ICYawM4pRz7mGIaBTzJRVxVEP364WcWvVvoQaS-RVRwWoDgEIeJoSoIaC5uU4NCiUYY1xTFyxHhPzOh5N_z1J0zKad5too2MVeTbd3fyPpqRaVO1XyF0EQDJl1VZaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانات رهبر شهید انقلاب در مراسم قرائت خطبه عقد
🔸
ازدواج و تشکیل خانواده یک نعمت الهی است و باید شکر آن را به‌جا آورد.
🔸
توصیۀ من به همه عروس‌ها و دامادها این است که با یکدیگر با صمیمیت رفتار کنند.
🔸
محبت، وفاداری و همکاری زن و شوهر شکر نعمت ازدواج است.
@Farsna</div>
<div class="tg-footer">👁️ 169 · <a href="https://t.me/farsna/436373" target="_blank">📅 17:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfaqjZYZWvF8qqO2aVvLkdasSbjw3gkrbAUAcPBZR_p-WxHPDmL-qW4GHD1QyF8z0b8UDLhJfbSJKzdnq_pNzthjrm1TytVUlVaFnuX4IZn9yKPVbaxQ-cm6xYpiWdCaQmffJiJXQWlQufGS7tR-drllZOMGdRBuQ8ExsjeX7G86w0OSm8S55mJvL1U7EY3VAsL8GIitk0SpozVuGeBnaJQfoL7jMkz3gGr86V1mahi_qGWopJ3C9CnsGHU1i68sYGe6EC6uOo7XwgrEeNunBX_HciWoPEfLFpQ5xhlHuCiqt2BuS9ULYcYeXvXtwYNe9z5Btb-tfEi5WfVGulo3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حساب رسمی مدیریت آبراههٔ خلیج فارس در شبکهٔ ایکس راه‌اندازی شد
@Farsna</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farsna/436372" target="_blank">📅 16:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e90bbc20.mp4?token=I4JsvOZsVf6NoAAcboKR8nY5s0fCz1Bf6F8Yh41MKW3-ci59eFnyeP8FjUvF9YRx--NRGY9eg1IAHX61z7sX8XMtpSLw61x_p8Z29WXO6ruXyNFL5FzvOXQPrOzD88YTaCC54rRxBwXSYEV_84aBjiS0ofQEL4DcFplcJqnSTKcyu4UUYOmBsMuXLHBhkLilGleBv11cdS93Ms1lQXAxW8dpM_2se9Fvj94vdT3ys_XSg45cCSsXLhWzAJFxxxtsmba0Dw10GeGuL-Yu6GkN9KDfT1b0lT2G5kYKLo0_aswzvylsNQQqBvKXpgB60_CNyQntzjEUugPdNZ88ckcWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e90bbc20.mp4?token=I4JsvOZsVf6NoAAcboKR8nY5s0fCz1Bf6F8Yh41MKW3-ci59eFnyeP8FjUvF9YRx--NRGY9eg1IAHX61z7sX8XMtpSLw61x_p8Z29WXO6ruXyNFL5FzvOXQPrOzD88YTaCC54rRxBwXSYEV_84aBjiS0ofQEL4DcFplcJqnSTKcyu4UUYOmBsMuXLHBhkLilGleBv11cdS93Ms1lQXAxW8dpM_2se9Fvj94vdT3ys_XSg45cCSsXLhWzAJFxxxtsmba0Dw10GeGuL-Yu6GkN9KDfT1b0lT2G5kYKLo0_aswzvylsNQQqBvKXpgB60_CNyQntzjEUugPdNZ88ckcWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری دانشمند فیزیک هسته‌ای: از تسلط رهبر شهید انقلاب به مسائل هسته‌ای خشکم زد!
@Farsna</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farsna/436371" target="_blank">📅 16:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ جنگ رمضان در قم
🔹
سپاه قم: تا ساعت ۱۷:۳۰ امروز عملیات انهدام مهمات جنگ رمضان اجرا می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/farsna/436370" target="_blank">📅 16:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuqivJiDts25ROqqX_u3-eMVAvUPUXOvYgHOouOHOyHEJYk8Vkf6J1UvU_swJHurqC2IU2rcofawo17NoiX0bPvz4Cm8o21BOwU8-3WZpMKJybViIjnTNjwBFi8bMf9YwqeWF5WTQPt_17jEbdV2-4GJqGeLqGK107zAtzSOC4Gs0wd_c92MLlVm_TW-UmdvIikcQWm3Gj9GHbPZeZAjeValVEZ1NmQtWff2jvtB_zrW9HK6szd_l-H6cE_4_PATPVGPHI6_WVBANSfSiGuZqawm1bz_X75Tsosv-G4abNL9LTYOC2YzYBlo-K-VlZOW-2LVL-XiDop_ppkKmp2BFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای هفتمین بار از آغاز آتش‌بس با همتای عربستانی گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/436369" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBEFQN6_lrbY6T6gKh4nzULTxShEfQEDRyVnw03Vfnz50F4tPe_2wFYcm2JSitTQed0Bse_5lbfkJnEcs0Q2VEPK8itlwR5XkQ00r3i-ry6LlXxrfnAzG4MRXJEWM6plfmio5dLwnSjDbh-BaLHep6A2poLdFKla1nOxfrtQjIY0WDNPDxTFf2F-Ox_dxLN3HYH__kKiK1XrFmEQd7rJIymt7edlKpySSqjf5g69w6Ng63K51PkUQbeertkYolAJyusu2LL52AYCsyCuYgsIYoc6eLFcaHjEfVVHE3zw6tHFT_yaKGkr2W1agh_nKjVcji6j2Zk_B2fSzlyMk7VTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نماز را در ۱۰ روز اول ذی‌الحجه یعنی از امشب بخوانید تا در ثواب حاجیان شریک شوید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/436368" target="_blank">📅 16:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ ۴۲ نماد بورسی فردا بسته خواهند ماند
🔹
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔹
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/436367" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436364">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
رئیس بورس: بازار سهام با دامنۀ نوسان ۳ درصدی بازگشایی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/436364" target="_blank">📅 16:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjXQcT6FuiXU0UXweDSpWYjqxUiSZlPSD1CBogh_pZyfeVNcT-mFk-jhUJf8lrhVgX04nuSDLxcogCcoEZDA5awKajFVaQTo1LskoJ8nC6qTqU1BM64WvoqbrTjNDMz4c_QBHw1EiXc-d2sq5gOV2P5DwJ16eKi6yHLoj6z3sHFDOoJmaKLHvhYUHMWFSHz05TmGggRyVbel4yjFwFUfX53cxqe6Mtd_K3EVJo8Jztx7uBEjv-YxBP-4xRohWivDg-JHxbMQS0_F3ur2WUjX6y5VrpkYEKu0m-NrBCXMcQ9lyUcdu3eWDPhbIQR65ti2i7d_xxTnlzJd9oYTCtegcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان هنوز به ۱۱۵ زائر ایرانی روادید نداده است
🔹
یک هفته دیگر مناسک حج آغاز می‌شود اما رئیس سازمان حج می‌گوید: هنوز ۱۱۵ نفر از زائران حج کشورمان اعزام نشده‌اند.
🔹
باوجود گذشت ۲ روز از پایان عملیات انتقال زائران، سازمان حج می‌گوید «طرف سعودی قول مساعد داده است، اما تا صدور روادید باید صبر کرد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/436363" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705cc3ad13.mp4?token=TYOIGf3H6qARnq1-tCMzrSxUPrCtmvheWfcdJ6abj2SfI3achHpuXRbQ-NuBctwpat68nx8I3V4ktesjuGHF90tdKgtZ-gZCAp1KPFc4BiTM-01XcrrrSlLVIwKQPeAZWu8KmHvu2hNW2si4waxdzTtU_3FgOGuGE_n-eodysb_YQbvQaCmYgyJj_WITDhDGCr1H3BRjwUtj3VYH7jzW9tmA6nJ_sQwD70IvTERkHtST2JzvHzpergKAQBjXtamVKYU25zV_IKwRZsqomhbvXWfkK9QwpAU0rG2EaKf7M8sdZYgV5hHOPaaBmGmku36_CaIh53-rNOSYbSLeXpDDIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705cc3ad13.mp4?token=TYOIGf3H6qARnq1-tCMzrSxUPrCtmvheWfcdJ6abj2SfI3achHpuXRbQ-NuBctwpat68nx8I3V4ktesjuGHF90tdKgtZ-gZCAp1KPFc4BiTM-01XcrrrSlLVIwKQPeAZWu8KmHvu2hNW2si4waxdzTtU_3FgOGuGE_n-eodysb_YQbvQaCmYgyJj_WITDhDGCr1H3BRjwUtj3VYH7jzW9tmA6nJ_sQwD70IvTERkHtST2JzvHzpergKAQBjXtamVKYU25zV_IKwRZsqomhbvXWfkK9QwpAU0rG2EaKf7M8sdZYgV5hHOPaaBmGmku36_CaIh53-rNOSYbSLeXpDDIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مدیری که می‌ترسد نباید مدیریت کند
🔹
کسانی که تنها در زمان امن و امان حضور دارند، بود و نبودشان دیگر فرقی نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/436362" target="_blank">📅 16:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
گوشه‌هایی از زندگی شهید علی لاریجانی
@Farsna</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/436361" target="_blank">📅 16:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حملۀ تروریستی گروهک پژاک به یک معدن در سقز
🔹
حوالی ساعت یک بامداد امروز گروهک تروریستی پژاک با ۳ خودرو به معدن میرگه نقشینه در سقز حمله کرد.
🔹
تروریست‌ها ابتدا دست‌وپای هردو نگهبان معدن را بستند و تلفن همراه آن‌ها را خاموش کردند، سپس اقدام به آتش‌زدن تجهیزات معدن کردند.
🔹
براساس گزارش اولیه، یک لودر، یک بولدوزر و ۴ کانکس شامل امکانات رفاهی، ابزارآلات، وسایل تعمیرات، قطعات یدکی ماشین‌آلات و موتور برق دچار خسارت شدند.
🔹
چند بیل مکانیکی و خودروی سنگین نیز مورد هجوم این گروهک تروریستی قرار گرفتند. هدف تروریست‌ها باج‌گیری به وسیله گروگان‌گیری نگهبانان بوده است.
🔸
گروهک‌های تروریستی و ضدانقلاب با هدف جلوگیری از توسعۀ اقتصادی و اشتغال‌زایی در مناطق مرزی، زیرساخت‌های حیاتی را هدف قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436360" target="_blank">📅 15:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIRBrsr9nJ_qe-q85LmlBn8XfUM-xnhjdIjwvm5Sv5_48oWcSV4bc0cOLF1nNA6tUUiHEaLVkVrySFYAYCyEn1hAXsn0oBCtFDp7CgjogHT_xq4DFp4Yc9uwpTPnjZ2HIur6VW8jkOR3jl6AOUqk8ZUbrTf_jT9v8SUXWuyazic8yRwtO_ye_l5ist-_6zZemaQSsIiqL-KlFiTbz3Xc7DSc6tWtetfYCpUvqSOVntcayawHW9wciWOe3uyeKhCt0E5WiotgW4YuNLr4juJIu7azFyJ4pbmHg7EHC3MFlxorHPCDZ8Tu1UJdU9Mc4tfHHUmfMaIRRW6-ZeXFgz05_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدارهای حملهٔ هوایی بر اثر حملهٔ موشکی حزب‌الله در شمال فلسطین اشغالی فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/436359" target="_blank">📅 15:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqg11QB3wMiLnuv4hDbVYpQVFZnjB9h1VdWbNyoQhiJgLgWL0pWYAOPgCr4AqozYzNFSuWMAp_CDc80bZy8D5NRY1LbrijVWFJGJ5uRpGY5dui5u_c2Tskb1PXOjxihgo1C3XNkt_KpukSGScHEy-ujSV8nmMNJc-A0P9RZNjQXO-xr9snWfNAzHfEqxjf0zu11AoRkEsPwPEPKPND-aGQiWzUzGWH57h1A0UGGMVE1yGCjsYQrtcaWTpCOKfUwyeY6MXfoW-Dj179yk2yEoMKO-ovcO1hSO1j71ZwvEE6F5xgkZgOBALySHR1HHMNXfEXkscrrhv6b0rg2opB4UFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: خیام تجسم عینی تلاقی علم و اندیشه جهانی با ادب ایرانی است
🔹
پیام رئیس‌جمهور به‌مناسبت روز بزرگداشت حکیم خیام: حکیم خیام نیشابوری، تجسم شکوهمند تلاقی علم جهانی و ادب ایرانی است.
🔹
خیام با طراحی تقویم جلالی، دقیق‌ترین گاه‌شماری جهان را به بشریت هدیه داد. روز بزرگداشت خیام، روز پاسداشت خردورزی، پژوهش علمی و آزاداندیشی است.
🔹
امید است نسل امروز با الگوپذیری از خیام، در مسیر تولید علم و پاسداشت فرهنگ ایران گام بردارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/436358" target="_blank">📅 15:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460271a4e2.mp4?token=qU4akgTzdk5HP47c3PT2W5A8ges0ulwprsH_WEdup_yhNL5s_ywcUtBmksC880-i1t8VtgrB2fJgenAQ0DJMQc9Q0Kw99K0jSlzYHtEsNsPW4--9_yjuQ4kpd_k-z_MIio-pXHZTzvU4PJuQjMguEipJxNW60-ee3fgEBVbVHmflXNMmrE9-vrIJkn8_S-UG3TvIQ9Fjxpfs-h85DC6YLMonB3HqY5UnIeMFgLiKlaVJ039f1h27r_iisd5cU6bvz1OzB1RqQXeuqTYc1xk32tvjNMFrTBwpTgx3NQ86TZQkBtKfDmEW77WnXb3ntp0SkZ3BSXwVnKRIQ_oHom6ldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460271a4e2.mp4?token=qU4akgTzdk5HP47c3PT2W5A8ges0ulwprsH_WEdup_yhNL5s_ywcUtBmksC880-i1t8VtgrB2fJgenAQ0DJMQc9Q0Kw99K0jSlzYHtEsNsPW4--9_yjuQ4kpd_k-z_MIio-pXHZTzvU4PJuQjMguEipJxNW60-ee3fgEBVbVHmflXNMmrE9-vrIJkn8_S-UG3TvIQ9Fjxpfs-h85DC6YLMonB3HqY5UnIeMFgLiKlaVJ039f1h27r_iisd5cU6bvz1OzB1RqQXeuqTYc1xk32tvjNMFrTBwpTgx3NQ86TZQkBtKfDmEW77WnXb3ntp0SkZ3BSXwVnKRIQ_oHom6ldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گشت‌وگذار پلنگ جوان ایرانی در طارم قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/436357" target="_blank">📅 15:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb65ec73aa.mp4?token=fj7cVafxeQCk1exEBde2TIPo63t4SA8oJ4aSo1Hp-Nn6mLKbGFW59nfmSURCBvvmnU9eHJhrnijkW2ZSKQcV2oRQ-IFJKtlml__ze1Uaognpx44mecW15H-PF8J-6XWRB0YgaXTfT7hEe3zDxq6kNGd8S3fRpF9u82Nh0-X9pBbItxev3ZLcRmf19UVXVCg27WX4K8JPptABZRmxUntv_Zw_aBXVM6tvnpb8sJjKXqRbbgsnkkwHnqjtTr18JjHHaiByz1GO6ZF_tMBg1paRuziZhRcGNtv8y500lmuoXjS8QQ7vch4VLvQdFjEQq4oMNAGrRq2f5hEZHHAsdvix0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb65ec73aa.mp4?token=fj7cVafxeQCk1exEBde2TIPo63t4SA8oJ4aSo1Hp-Nn6mLKbGFW59nfmSURCBvvmnU9eHJhrnijkW2ZSKQcV2oRQ-IFJKtlml__ze1Uaognpx44mecW15H-PF8J-6XWRB0YgaXTfT7hEe3zDxq6kNGd8S3fRpF9u82Nh0-X9pBbItxev3ZLcRmf19UVXVCg27WX4K8JPptABZRmxUntv_Zw_aBXVM6tvnpb8sJjKXqRbbgsnkkwHnqjtTr18JjHHaiByz1GO6ZF_tMBg1paRuziZhRcGNtv8y500lmuoXjS8QQ7vch4VLvQdFjEQq4oMNAGrRq2f5hEZHHAsdvix0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قهرمان کویتی از روی اسرائیل رد شد
🔹
جاسم الحاتم، قهرمان جوجیتسوی کویت، در اقدامی برخلاف رویکرد دولت این کشور در حمایت از مردم فلسطین، در سکوی مسابقات جهانی ابوظبی از دست‌دادن و قرارگرفتن در کنار ورزشکار رژیم صهیونیستی خودداری کرد.
🔹
او در پاسخ به این اقدام خود گفت: ما نه‌تنها با آن‌ها بازی نمی‌کنیم و به‌صورت آن‌ها نگاه نمی‌کنیم، بلکه ما به‌عنوان مردم کویت اصلا آن‌ها را به‌رسمیت نمی‌شناسیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/436355" target="_blank">📅 15:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حزب‌الله: یک سکوی گنبد آهنین، یک دستگاه ارتباطی، یک بولدوزر و تجمعی از خودروها و نظامیان ارتش صهیونیستی را در جنوب لبنان مورد اصابت قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/436354" target="_blank">📅 15:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye1fhPQgtXvd86p9WxIRX3AEuA2l05j9Oj77GShDl6iFXlBB2kdsYpR9V07KSZYP331KTsyCEWjvGkGbLcT2mfLwlm3XL4015XjQuOI6dF5xJKHtprVCzVjOkBGSQEM_M49QzwCqdpRMefUmAQznyu0pSrG9B4RhpjOnQzTr8sJYBE0AqepELqIa_XZsLGD946qdNE3Eu2DzfS-g40EFHa3ZdTFia3ISbjTr0D9KTvQNxBvhXvuWrHAviqgxtdueINHui2m9CikmEY5_jsKSjPjTxoHHDByzmJq2oKBs0bK6ap9D6cNMqzr77X38zztMZAknCUpGmsmU0IGUbV08eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای سبز ایران قفل اروپا را شکست
🔹
اتحادیهٔ اروپا پس از ماه‌ها مذاکرهٔ فنی و سیاسی، محدودیت‌های وارداتی پستهٔ ایران را لغو کرد.
🔹
این محدودیت‌ها از سال ۲۰۱۹ به‌دلیل ادعای وجود باقی‌ماندهٔ سموم و آفلاتوکسین اعمال شده بود و باعث افزایش هزینه‌های صادرات و کاهش قابل‌توجه فروش پستهٔ ایران به بازار اروپا شد.
🔹
به‌گفتهٔ معاون امور باغبانی وزارت جهاد کشاورزی، این تصمیم می‌تواند زمینهٔ بازگشت گستردهٔ پستهٔ ایران به بازار اروپا را فراهم کند.
🔹
برآوردها نشان می‌دهد صادرات پستهٔ ایران در سال جاری به ۲۵۰ هزار تن برسد و ارزآوری آن از ۱.۸ میلیارد دلار فراتر رود.
🔹
همچنین بازار چندصد میلیون یورویی پستهٔ اروپا دوباره در اختیار تولیدکنندگان ایرانی، به‌ویژه باغداران کرمان و رفسنجان، قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/436353" target="_blank">📅 15:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0b356f82.mp4?token=j-FtuTrwx41mp_bZfL4U8W2Nld__DJvKbialampF_y9lfBr_D2PCC9moCZDf9PkykyIis4DylRd_2Y1-YspBi_24fm8fsvbOnHzxxL78lcw72iyYyXTOzT8E-N3xIIFf78KAWaCbhxbn99h6GWUtOsYu6j2AxpbxjkI2tQ4pk28xy39XWC-P__DGaF0zPY8cRJ4lQxsd4rIZk4Tm69aNgUgBNqHaJSPe9YyzeaUn3lg-6LGgMPWeUXem9B3pLFsrTtqWCbkXMy8FyocbiQT3UIPdSFBxC1l-AK_mpoUkf8YZErbRdsShBS_6cqPvvys7d_etJ46gI1WNZHUh3_CeLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0b356f82.mp4?token=j-FtuTrwx41mp_bZfL4U8W2Nld__DJvKbialampF_y9lfBr_D2PCC9moCZDf9PkykyIis4DylRd_2Y1-YspBi_24fm8fsvbOnHzxxL78lcw72iyYyXTOzT8E-N3xIIFf78KAWaCbhxbn99h6GWUtOsYu6j2AxpbxjkI2tQ4pk28xy39XWC-P__DGaF0zPY8cRJ4lQxsd4rIZk4Tm69aNgUgBNqHaJSPe9YyzeaUn3lg-6LGgMPWeUXem9B3pLFsrTtqWCbkXMy8FyocbiQT3UIPdSFBxC1l-AK_mpoUkf8YZErbRdsShBS_6cqPvvys7d_etJ46gI1WNZHUh3_CeLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: وزرا و کارشناسان ما شبانه‌روز سرکارند
🔹
از هر صدایی که بخواهد تفرقه ایجاد کند بپرهیزیم اما واقعیت‌ها را هم ببینیم.
🔹
این‌گونه نیست ما صدمه ندیده باشیم، این‌گونه نیست که دولت امکاناتی داشته باشد و خوابش برده باشد اما مردم در مشکل باشند.
🔹
برای عزت…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/436352" target="_blank">📅 14:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr1bG-sES53PyVGrLXKNvV-vGb-Qli5D2LK6lcuhUPlb9hf-KFAT9N3jYbh8Fhhve_UXecS-05I7wwnAK_E-zbNYBdMstQl_JZ-oxcj9KwR9KhQ6Apu_AHq2SPwdLHHhJqkwVxh2GAtblrSpQDSIaTm18N90l8nf3TFCAPfT3t47-I8RZoRNAEZVbV0TFuFfswHGAmqdzrHkB0QVfYjyukO2LqIbIL1QT7f6d8HBcGS_cdxxEbwwDbnWAqbAiA3hErKNId7U2uxCSnwmswfwc_ZyvYdb0RCVxPtEa8IbSKs89i3GKCAKeKacG_yAGld3z3xBcG0Hde5DLqKA92NYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ روسیه: ایران حق غنی‌سازی صلح‌آمیز را دارد
🔹
مسئله نیروگاه هسته‌ای بوشهر فقط به روسیه و ایران مربوط می‌شود و هیچ طرف دیگری به آن مربوط نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/436351" target="_blank">📅 14:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436350">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFhr1CmZJJpKqX6oZtzeuq_H0OdaIsMuWAG5rhMVAfCJ83uJrDv3ETt4SDGLuGooywRuHlQlAH_-A6jzcyZ_P3asUexXabFz7a6zs2C729mbtOY-HWJNb9WGWsa7i72Eu4EBCXLvxCGo4u8N40RrQDSFn6rLaROO6q1Da7FQhkj6kfjIN2o1wGp_Lhc3ZAwLBGqxGVlNCzj1PfWjeooJT_PeydiDJt5_HQdhOC8P3dVqDF90PfclAoRy-bslWyjUFHWjC31Rm_UUyzESx5xmP1Vnw8dSGhugKa9-7wQ0DC5QB-mfCff8z6U5eG59uCXNPOvRSIt6ayZ6cYcLeaMYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آسیب‌دیدن کابل‌های فیبرنوری در تنگهٔ هرمز، چه تاثیری بر روی اینترنت جهانی خواهد گذاشت؟  @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/436350" target="_blank">📅 14:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436349">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63673ef16.mp4?token=OQyeUg4fYAq_Kq86VWMh3L6-24GakUtlYS53RswdYvBjfmJScDOQDvwpIeWbHYjXXYWqsKZQCcpCdRRy3ZAcZrWV43QH8apoOOlvD5KQwtCI1w8mECl2SBysBsmhs0YlRhwzgfRarbtEfn2TfrocOKTHr37VXbezCbikXowJMRwFAcoqHBCdm-yRG_JRJ91-T_oCMIh3Hj7X2K89VKFZoeWi2xcQUpIg1URmcrtAN3LNmsjcs4QMu5-kF63VWLW9bH6PECPQZZVrVbIjgDJMewVMNjJ9aOVqu7ljFlDhVtnt8fVdmYUn97t9H8oI54NQaE53aPnumVnLc72Sra8bow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63673ef16.mp4?token=OQyeUg4fYAq_Kq86VWMh3L6-24GakUtlYS53RswdYvBjfmJScDOQDvwpIeWbHYjXXYWqsKZQCcpCdRRy3ZAcZrWV43QH8apoOOlvD5KQwtCI1w8mECl2SBysBsmhs0YlRhwzgfRarbtEfn2TfrocOKTHr37VXbezCbikXowJMRwFAcoqHBCdm-yRG_JRJ91-T_oCMIh3Hj7X2K89VKFZoeWi2xcQUpIg1URmcrtAN3LNmsjcs4QMu5-kF63VWLW9bH6PECPQZZVrVbIjgDJMewVMNjJ9aOVqu7ljFlDhVtnt8fVdmYUn97t9H8oI54NQaE53aPnumVnLc72Sra8bow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: وزرا و کارشناسان ما شبانه‌روز سرکارند
🔹
از هر صدایی که بخواهد تفرقه ایجاد کند بپرهیزیم اما واقعیت‌ها را هم ببینیم.
🔹
این‌گونه نیست ما صدمه ندیده باشیم، این‌گونه نیست که دولت امکاناتی داشته باشد و خوابش برده باشد اما مردم در مشکل باشند.
🔹
برای عزت و سربلندی کشورمان حاضریم تا جایی که ممکن است فداکاری کنیم و باکی هم از شهادت نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/436349" target="_blank">📅 14:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPB2OV75DDLad2F0O4prikd-3ACNRL05yfajCizEXmwkQ1awshmA1gAPQbymx23QsJscmTP062MttwDIudwHPwXui19Bm-PDxcOlRnVt7skw34ZkH6NvSDfPu2YqnMG2-Y8dbO2hm8By2brtIlTiy8uPxinBlA4h17qphJLmLWoDIo0f5bLP4u3rS_2n_ij1w6PTMbopJTWU-oNLfD17L1J81_ox-a387RX0klqPCJNrTTTlZcidg70tn5h4ZvfufRBLQ4KTx_ngpk4MCWUzXkOJRjyipIL2wdg0kok3Dm-BohWY8GqVtB0LjnuTUXVXufdcKRTjz_scHjuYIE1hvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-kfmjEIEDqRs93SqObGlN56mmKsUXgA5h_Mu4LjzX6B6OXmC2NzoAPQ6bb5inhWYTgWrH3dvS99aqz0t8SldG3bWudvb9KhzjpUGYfdHaRcaTybr8R0hUmHU8SbZqR7M05-2hHd24B758ExWvm5bG6GBJWfuZ2ULbhter925g2ib-ReI8nWeU6RFa1FodQi9fkRDtW_BdipxksgkNvVvitH1LwLLRmoYzE2LZbucLysNjvSMPrNyJ8GIJaPNAyQz9qUN6fUMmHpHofnFKJ4HGbOYBgN99SsJo2pIzd1_As3u2RUK6UZB4dy4QNbnjyRk8fd2fJAI2fTmcA2Yflwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSWHnMb2M2S15Hb0ocYym7bb4VqmBm-lOx-_j52146hqjqz_qBxhFnJC6U-jRxKl2_0JGDW5E34aXs6KLnl8-qsmFXsUMwtAuA1wrZhKHhrgBUaRwEHikHG5HkL6-Ewkke_HusBqjB7HkD-C-W223v3dEIZb3CDOzKamlOJDj4J9NbCLDQ8WQA1DDBKIHeZ_K7RSWICN5G03XsfG2nhKjLs6-OgXkfmN64PK8FUZHlIU885slZZ52T5sc0KbJcvzXs6x-J5r2OABSMhKDrxPLuTEaqR8xW4HoVfUGc9miqO8AIGBmtf5l3sXdnBCDGEIW9sF_vdjuSuiwbOqsAeItA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دستگیری زن و شوهر طلادزد
🔹
فرماندهی انتظامی تهران بزرگ از دستگیری زوج سارق حرفه‌ای که در ایام جنگ به یک خانه دستبرد زده بودند خبر داد و اعلام کرد: بیش از ۲ کیلوگرم طلای سرقت‌شده از این زن و شوهر کشف و ضبط شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/436346" target="_blank">📅 14:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دستگیری عوامل وابسته به محور آمریکایی-صهیونی در ۳ استان
🔹
طی اقدامات سازمان اطلاعات سپاه در استان‌های قزوین، کرمان و چهارمحال‌و‌بختیاری تعدادی از عناصر وابسته به محور آمریکایی-صهیونی که قصد تولید ناامنی یا اخلال در نظام اقتصادی کشور را داشتند، دستگیر شدند.
قزوین:
🔹
دستگیری ۲ جاسوس وابسته به رژیم صهیونیستی
🔹
انهدام یک شبکهٔ توزیع سلاح‌‌های جنگی و کشف مقادیری سلاح و مهمات
🔹
کشف ۱۴۰۰ تن مواد اولیهٔ پتروشیمی احتکاری در یکی از واحدهای صنعتی
کرمان:
🔹
دستگیری ۸ تن از عوامل اصلی اقدامات تروریستی در سطح استان
چهارمحال‌وبختیاری:
🔹
دستگیری ۲۲ عنصر در قالب چند شبکهٔ وابسته به گروهک‌های ضدانقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/436345" target="_blank">📅 14:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe985ac16.mp4?token=iK05zNOZPk-FvFMeLivmGbydeyZpZVhKZ95l7jfs42GmCPNh5tiOzndTR2R6bjX0U5MBGYa-mE_OIfkyigLN-1pcUQpLojluC9IzPHv5FukL0ADqbqCDCVc22ox6H3uoUuw0k0Lwp689Z6a3edUoFm-08RxxikJuzy9xqbGvN2s7LRfZ3chuccSGNvPLPPgde1X6jhmIClYYES5fe4TWtVRLrjukJV7ZIvokDcCgVRN8_guLxgp0DzhzCkQzf-r-CmWl96ghw-1IqX3mnuXaL9HlmK4i99pB2HB9x2r1M4wbmwndakbkDeBAQkt48qs9CJApJyQnTHZkUfet_96g5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe985ac16.mp4?token=iK05zNOZPk-FvFMeLivmGbydeyZpZVhKZ95l7jfs42GmCPNh5tiOzndTR2R6bjX0U5MBGYa-mE_OIfkyigLN-1pcUQpLojluC9IzPHv5FukL0ADqbqCDCVc22ox6H3uoUuw0k0Lwp689Z6a3edUoFm-08RxxikJuzy9xqbGvN2s7LRfZ3chuccSGNvPLPPgde1X6jhmIClYYES5fe4TWtVRLrjukJV7ZIvokDcCgVRN8_guLxgp0DzhzCkQzf-r-CmWl96ghw-1IqX3mnuXaL9HlmK4i99pB2HB9x2r1M4wbmwndakbkDeBAQkt48qs9CJApJyQnTHZkUfet_96g5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک‌های ارتش صهیونی با مخفی‌شدن هم از حملات حزب‌الله در امان نیستند
@Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/436344" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7655843800.mp4?token=EEG2h-_GPYlx8cIDR_aHFw3rwgXQ6mc_PwqYx6RFQd9bqjlTWWoyILW0BWnNSP0CFI2yACm-XwgM1a6IpSvNb_2XqWfhqXiJjI9_wLjB_sOvQyQ983jZps8C-nn2Lnf-azMknsOAUaLD7tmMJvIeiieDBTX5LTtUnAjWQY1pnU2qWwNf-vgDpZnYsaDTdxdR-MEkOmpE-Q4iw2UFM-KIAkHzTSJvlqw7TMQDoyD5GKqU8zLLdRWiG7OFnVH3kBdRmDTXO26e1C2rOTS820tAaE3LQ9Jmck9loiDZNpkVIcqjjcBN86COgpaeUcDXaIRy_EuGPvRUMbE8p22BVlUOMAHdVyyMxSocIRO9Kd5vtJFQJRb3UuVFZYHkEgd18Zvc5qQ_V2SMajLuaPrKldg3CPbPLCW9gX5kOGIcQDRxJZQ_dWGEbnsJt7eN0mHPzjjqwmA1f3TCqlM70HUcQXkUAv4_OVEOFPikmYBO9HZ_KX7TZi8xlc2MUBIjddGwAehFWNwtm3wVase9EpxQksZ68uBNOU6FFtg2QsSfTaZVp8ddGtB2o4tphXF5mLUjfcx-fgA_MT8gwa5mjEBYnYUP_gdMKDSMxdeNcmiPL6S_b8IcCgOw2owZpJ-OoxDV3ljvLYkuJB1LCuHGObJl4yn1vRwN5lbIlK8Ct-W-19U3tuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7655843800.mp4?token=EEG2h-_GPYlx8cIDR_aHFw3rwgXQ6mc_PwqYx6RFQd9bqjlTWWoyILW0BWnNSP0CFI2yACm-XwgM1a6IpSvNb_2XqWfhqXiJjI9_wLjB_sOvQyQ983jZps8C-nn2Lnf-azMknsOAUaLD7tmMJvIeiieDBTX5LTtUnAjWQY1pnU2qWwNf-vgDpZnYsaDTdxdR-MEkOmpE-Q4iw2UFM-KIAkHzTSJvlqw7TMQDoyD5GKqU8zLLdRWiG7OFnVH3kBdRmDTXO26e1C2rOTS820tAaE3LQ9Jmck9loiDZNpkVIcqjjcBN86COgpaeUcDXaIRy_EuGPvRUMbE8p22BVlUOMAHdVyyMxSocIRO9Kd5vtJFQJRb3UuVFZYHkEgd18Zvc5qQ_V2SMajLuaPrKldg3CPbPLCW9gX5kOGIcQDRxJZQ_dWGEbnsJt7eN0mHPzjjqwmA1f3TCqlM70HUcQXkUAv4_OVEOFPikmYBO9HZ_KX7TZi8xlc2MUBIjddGwAehFWNwtm3wVase9EpxQksZ68uBNOU6FFtg2QsSfTaZVp8ddGtB2o4tphXF5mLUjfcx-fgA_MT8gwa5mjEBYnYUP_gdMKDSMxdeNcmiPL6S_b8IcCgOw2owZpJ-OoxDV3ljvLYkuJB1LCuHGObJl4yn1vRwN5lbIlK8Ct-W-19U3tuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک با اسلحه در برنامۀ زندۀ تلویزیون!  @Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/436343" target="_blank">📅 14:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMth4kxrh8uuvvJ8jw3J8USHNBgjTkOY16h2Q1ZnZNYdxA55al8Itp-k6tvqW0dBWOHDZoihvDwlKYN-sbERNC1-7_3EEnwYDiuhEL7Em0Ie7YXvDvxLdCSetX0mgf_3-Auu1FukjJuX0QLnKMz27FpNWLaetHt2sBIzHRb19YABP6tIAbafPIjPRf5c5UkpXNFraDjpMSjSJFvIMfPI5IHDezTYxq1UXgVXN7BYf5ZnJ5Ds5TO-N7Em0WM9PxC5lM7Mf4pfJ7hvbxRo8vEXNMJ0ewSHmNutE4mX6sggKv6Am5SNiBvc4ohhSHD_VQyQG8vAsqkSGpfNSo9v7ykrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها پای کار بورس آمدند
🔹
براساس اطلاعات رسیده به خبرنگار فارس، سهامداران حقیقی بورس می‌توانند بدون چک و سفته، با توثیق سهام خود تا سقف ۲۰۰ میلیون تومان وام ۲۴ ماهه با نرخ ۲۳ درصد دریافت کنند.
🔹
این تصمیم پس از افت نقدشوندگی بازار و افزایش نگرانی سهامداران دارای اعتبار اتخاذ شد؛ در این طرح باید ارزش پرتفوی ۲ برابر مقدار وام درخواستی (تاسقف ۲۰۰ میلیون تومان) باشد.
🔹
بانک‌های صادرات، ملت، تجارت، رفاه و پست‌بانک از جمله بانک‌هایی هستند که قرار است فرآیند پرداخت این تسهیلات را پس از ثبت‌نام متقاضیان در سامانهٔ دارا انجام دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/436342" target="_blank">📅 14:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxLGex5X458UVC8eelzc1IhR485lZ9y2XnwyuHq3HcJRNu14FLFH8Ptd5bvI_lrwI6GrwFNc0ZM9x_7FQm2U7ZqrkZ3O-LZodD1Q19Qvfh7AKHxcDTz0hPbLWkqwHalIZuOTxmp-1-YIYCXhsWM0pmguiV-6ftLzrF1ZQzTjQncKoQiFy5cDI8bGtXkIwKZK249231efC8-5IXsCRHs1D8a6J1CTp15EP0EbYYM2hYDpDo2FP2igg8wxIxceGushR3GkBkj8bWhZqgWI4nJ0tf0EKYj3pIFNpq-w-LygoavlHGLTAQKX68cKGAZYKUcDVQXHlx6AKOmKOThSIscNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
گرامیداشت دومین سالگرد شهادت امیرعبداللهیان
🔹
زمان: دوشنبه ۲۸ اردیبهشت، ساعت ۱۶
🔹
مکان: تهران، سالن سوره حوزه هنری
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/436341" target="_blank">📅 13:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmZff9dJkTkIlRCZpQsaVMZVrYYhf5Qz_zTrw6kUKuH2qtcJVl92uuZyyUnvNbPwERGk8-SdEvZDTnsF8IS220iQ74qOs1KZ2rxTTf-fvKByYwIjp8O6qPuzJD9HjqLV3RSUhXFQmCuneVxDv3rHCPOdcNs6crglh9NlBp5qfy0F02DQflfd6UfcdEELYtRGAhQijG8ye2jSfTj9tjULidXATlUE5XD9PwE14bWIbcxrrQuRTuY2vZZA6IyoC01wT3zd7gjwJEql5S8c1Vrd3uxegekE4Ovb-WZHKe6RT-_FcrRD1yQwErTPI3cQdXHhVPEaXNK0QOaOrWYKxf2Evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5RWvVE3Pm-G-TQ6Otpw16FpDCVoJR7LG1kL5Ilyw4EX_aHYayNeHuYznUL8FSfqIta-IoZ2NmWC81yr5sLDxDIbHIh5SpUORnxCvvcPMws2_JLMvt8FP33PJ8ALOa7HHp3UZ4P4_Px2GImm66G2tViLXNd-tFVJM9rvo0HGfcS7h0_Z0V1cR7Lulob4jr135RLO8QEJ13OSALVNmOmHyvdJhgDIfqBnP1ipZq08oaHoWG0VmtSAMTy_L_EGSwBLy6tpVEbTcvkhUvfVgfQz-EzclPQy_pdUgVtf7tY-M5z3lpHzZBgPkSB7nL2_vURLmXWdnOSJuaEEZMBBldtnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmbGVR5U2orokqcwyjWXK1Ur7-oQkfzj2DxjiDlk748Vdg6_h2F2x17KRVWFFwA6pJJvymlJCEjcqv3dHqeXPsaLXxHMtuk90TlaTZr76TEz37VhkOPl1pXEvk1zCt4orQaHGvDRXlMWKfCV0T1pyhSMy8ioby-LZPYXEGLRdyKcQ_2fosigXa6gp-nZp6TDk7kUK-IucPI534MvzOeGRh4r_A8GPYQjc3smuCt380KB-qBbjnvA04YUEIoembyGgvAr_-sUR4lh9cdhGLwDg8Oh1hZouY66voFLwH2Wgqh8FO8fNiQ1pXe1X6BFk30Q3aj2LrPcGxLvuhUIc9psig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ضربه سپاه به گروهک‌های تروریستی ضد‌انقلاب در شمال عراق
🔹
قرارگاه حمزه سیدالشهدا(ع): گروهک‌های تروریستی ضد‌انقلاب مستقر در شمال عراق به‌نیابت از آمریکا و رژیم صهیونی قصد انتقال محمولهٔ بزرگ از سلاح و مهمات آکبند آمریکایی به داخل کشور را داشتند و در استان کردستان مورد ضربه قرار گرفتند و مقدار زیادی سلاح و مهمات کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/436338" target="_blank">📅 13:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e997a2b245.mp4?token=ftWOX4atMEfO4KD6tzOxmCE-yFwEq31VItMP3fyqGHfZYd3BarNPHSpZ55ODfI90ZvHnVi3OqPMObYA0mU5HaT76V9oFtfYWOXbBA4MqPevscnUBvC75c70fO0NDgarymvL_PN723TmQURjypGHJrQE6D8J9bk1YnQVwhAeMqXlwLuJYpfD-aAHb4aXSzlm9nNgvxArMqg-ZGEbQ2e-nVcVXONtQCIvhp6N6l3wToIHyAm_JLJtYuuss6lpckKZyyb8LdbgMRZj2ji13d0r-RCdp4brE3XxUH50p0HkD8qvKV1rS99xCHc-VpgCE8WDjeCBKYlJf5GmglCWQCLf4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e997a2b245.mp4?token=ftWOX4atMEfO4KD6tzOxmCE-yFwEq31VItMP3fyqGHfZYd3BarNPHSpZ55ODfI90ZvHnVi3OqPMObYA0mU5HaT76V9oFtfYWOXbBA4MqPevscnUBvC75c70fO0NDgarymvL_PN723TmQURjypGHJrQE6D8J9bk1YnQVwhAeMqXlwLuJYpfD-aAHb4aXSzlm9nNgvxArMqg-ZGEbQ2e-nVcVXONtQCIvhp6N6l3wToIHyAm_JLJtYuuss6lpckKZyyb8LdbgMRZj2ji13d0r-RCdp4brE3XxUH50p0HkD8qvKV1rS99xCHc-VpgCE8WDjeCBKYlJf5GmglCWQCLf4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گنبد حرم امام حسین نو شد
🔹
هر سال پس از محرم و صفر، پرچم سیاه عزا از گنبد امام حسین(ع) پایین و پرچم سرخ جایگزین آن می‌شد اما امسال یک ماه پیش از محرم، پرچم حرم با پرچمی نو درست شبیه همان قبلی تعویض شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/436337" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c851ff707.mp4?token=tYGtQMmnbHc0W10QGeA06PaxTsHzGock_gZEDQvuM6ZGEjyhO6f34YlhLRdMPUDv-WOH1G5XPwhpmCFy4MKbh0nMeNy5N0Lq9M91yNxvgrvUFT9bT8UBg45ePU6Xn5H8UyqGMd9EaGqU9DsmisZRJfIPB_AvbAy-J5fhYX3FEekXnAJXXk2pXB1dShoeTTO-soJ64Qo8ew0hDVJVRkfjohPJyazHYE5UAlfNERWwEr3CtX4zrHFVoAYgAe1tHqtC-sh-whRtFp-AcwfmDKSQ74N3SudBJ4HspC3aknw4eeYTTDPnybuIqLCyFsrFMRKqwsiYoiRq-DXi88mgrM8aLaZX4BH-hJRw7GiN5hgpS3397U9aIhISzDHhg4nU_FkfE2IJ9hpNAsNMNtaGADf3SeLvmrlAdhVrWIXlCC-n-yprt256zhWfScT7ijAVpNi_e-tG0J0RzvFhVAnrKZ0md7u3CMrrskoynHAk-aQvbvM5mS9z1hF_A1zNo9Enr2kyzJSJ3R_iqKLdilv-dTYNyHU1Rp9iLpYyfeANcArsm-M_uM62T0XIB7GVdQaCdRumL-UD2DBa60n11M3nvS8fGM_08Ehha2hgpT57VGh4JGtkrw-X14q4_6RU3zu0FRYA-F6zD2D0_a-1xDAmxBbEXhe0GPBo6dGQlsUPadx1Mmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c851ff707.mp4?token=tYGtQMmnbHc0W10QGeA06PaxTsHzGock_gZEDQvuM6ZGEjyhO6f34YlhLRdMPUDv-WOH1G5XPwhpmCFy4MKbh0nMeNy5N0Lq9M91yNxvgrvUFT9bT8UBg45ePU6Xn5H8UyqGMd9EaGqU9DsmisZRJfIPB_AvbAy-J5fhYX3FEekXnAJXXk2pXB1dShoeTTO-soJ64Qo8ew0hDVJVRkfjohPJyazHYE5UAlfNERWwEr3CtX4zrHFVoAYgAe1tHqtC-sh-whRtFp-AcwfmDKSQ74N3SudBJ4HspC3aknw4eeYTTDPnybuIqLCyFsrFMRKqwsiYoiRq-DXi88mgrM8aLaZX4BH-hJRw7GiN5hgpS3397U9aIhISzDHhg4nU_FkfE2IJ9hpNAsNMNtaGADf3SeLvmrlAdhVrWIXlCC-n-yprt256zhWfScT7ijAVpNi_e-tG0J0RzvFhVAnrKZ0md7u3CMrrskoynHAk-aQvbvM5mS9z1hF_A1zNo9Enr2kyzJSJ3R_iqKLdilv-dTYNyHU1Rp9iLpYyfeANcArsm-M_uM62T0XIB7GVdQaCdRumL-UD2DBa60n11M3nvS8fGM_08Ehha2hgpT57VGh4JGtkrw-X14q4_6RU3zu0FRYA-F6zD2D0_a-1xDAmxBbEXhe0GPBo6dGQlsUPadx1Mmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کسی که می‌جنگد پای همه چیز می‌ایستد
🔹
ما وظیفه داریم که درخدمت مردم باشیم و تا جایی که نفس می‌کشیم به ملت عزیزمان خدمت کنیم.
🔹
کسی که می‌جنگد باید سختی‌اش را بپذیرد. کسی که شعار می‌دهد باید پای شعارش بایستد.
🔹
از هر صدایی که بخواهد تفرقه ایجاد می‌کند، بپرهیزیم اما واقعیت‌ها را هم ببینیم. این‌گونه نیست که صدمه ندیده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/436336" target="_blank">📅 12:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1f3d1ef3.mp4?token=EqQRJsH-7sWoCA3eBM4jEAM8KOQRV2D1G5wqf1u2HDthUKLJY0sSnOxfBQpMaHFJbY8BkY8kMFSo-qH52CpP79zT_znAWbEvcQLtFh_GVf7FHP07aWaR0AFQip1j0Rl6lmEySSQD7AodsWwKt2smOoQx-0QpBMzuwbPZw-9FdYxs9Q8vBCZzILQCkU9qPoko11EK5vuzaL8JKXLv4wPoTL8KwIGYlrUo2-Tgh9XCR1zCqVV1icSdkFVhwTv_ON4lagckm0vGDCEBtKAXR9pJF3u-y4AbJlyjS8AV5998ONiroFA8Qbocn1fq1TIzoENnUEe3KQME6cOVh16yjs6G7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1f3d1ef3.mp4?token=EqQRJsH-7sWoCA3eBM4jEAM8KOQRV2D1G5wqf1u2HDthUKLJY0sSnOxfBQpMaHFJbY8BkY8kMFSo-qH52CpP79zT_znAWbEvcQLtFh_GVf7FHP07aWaR0AFQip1j0Rl6lmEySSQD7AodsWwKt2smOoQx-0QpBMzuwbPZw-9FdYxs9Q8vBCZzILQCkU9qPoko11EK5vuzaL8JKXLv4wPoTL8KwIGYlrUo2-Tgh9XCR1zCqVV1icSdkFVhwTv_ON4lagckm0vGDCEBtKAXR9pJF3u-y4AbJlyjS8AV5998ONiroFA8Qbocn1fq1TIzoENnUEe3KQME6cOVh16yjs6G7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: اینترنت پرو مصوبۀ شورای‌عالی امنیت ملی است که آقای رئیس‌جمهور ریاست آن را برعهده دارد
🔹
پاسخ مهاجرانی به اصرار یک خبرنگار دربارۀ وضعیت اینترنت: در شرایطی که ترامپ اعلام می‌کند آتش‌بس به دستگاه تنفس مصنوعی وصل است پاسخ شما چیست؟!
🔹
در خصوص اینترنت…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/436335" target="_blank">📅 12:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436334">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca68ea7e9.mp4?token=GNpVnIzxZh65hav44rZSkZVFUo8qE_lw2Jp1Cvwy5q_PkYjWH44b1pk-Wg9B2I0Qpu-OlxcqPmosv8SEV3WTiPOdQwOP9iAHxBSQYE9hiNQb3JyWGFHimIlYk2fEcI-44jTAcNDZj1IsYbcvatCr5FnmeT-s0hN600m5bH5sZ7DYEebRJVI7DNlanrAIDzx2iBKLzjCkklibccYXPkLngXD6buyw8MrgM9DRm8bCWG3K_8_tcdv41caJFteNluB8mUUo3iB4UjO2OT8J5lWB-r_a5WfNn4JMKhHQ4K16zPPtVzd2TuzmcDz74TKFd2hZbWhVnIzccKQfQZnxPLbwDWvHEpu4kBpvvBboHr_VxCHdEufASqNAWFdcbf5d5hLX5U7OI8Xw1ctanXCMxZzwiyLOAjsmVbT_b74-SS0vtS1GUuMwq8ZCNX9lHSikTYb3HSjnyYF6pVF9bQLNeLZ2bWhDLnDpsERbQm8WWBjU0v7stxoI8BQAN0dhLlPfSg6_vrXj-u8YnATzLo_FVMs2EZvMviDM0sCCW6R-b3mEtTylJ_vnFNPIXP0yxp96QyaTWlk69Ni3qPljxPBHwYzfhOiih40HNkqtco19Mz4NEUQHIfl600FKGh3mLxwc7bqMklF7YeaECanzdCxpDFOOSuJaf8ieWVV3uZa0QB2QXiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca68ea7e9.mp4?token=GNpVnIzxZh65hav44rZSkZVFUo8qE_lw2Jp1Cvwy5q_PkYjWH44b1pk-Wg9B2I0Qpu-OlxcqPmosv8SEV3WTiPOdQwOP9iAHxBSQYE9hiNQb3JyWGFHimIlYk2fEcI-44jTAcNDZj1IsYbcvatCr5FnmeT-s0hN600m5bH5sZ7DYEebRJVI7DNlanrAIDzx2iBKLzjCkklibccYXPkLngXD6buyw8MrgM9DRm8bCWG3K_8_tcdv41caJFteNluB8mUUo3iB4UjO2OT8J5lWB-r_a5WfNn4JMKhHQ4K16zPPtVzd2TuzmcDz74TKFd2hZbWhVnIzccKQfQZnxPLbwDWvHEpu4kBpvvBboHr_VxCHdEufASqNAWFdcbf5d5hLX5U7OI8Xw1ctanXCMxZzwiyLOAjsmVbT_b74-SS0vtS1GUuMwq8ZCNX9lHSikTYb3HSjnyYF6pVF9bQLNeLZ2bWhDLnDpsERbQm8WWBjU0v7stxoI8BQAN0dhLlPfSg6_vrXj-u8YnATzLo_FVMs2EZvMviDM0sCCW6R-b3mEtTylJ_vnFNPIXP0yxp96QyaTWlk69Ni3qPljxPBHwYzfhOiih40HNkqtco19Mz4NEUQHIfl600FKGh3mLxwc7bqMklF7YeaECanzdCxpDFOOSuJaf8ieWVV3uZa0QB2QXiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرایط بحرانی سلطنت‌طلبان بعد از وطن‌فروشی
🔹
با انتخاب رهبر جدید شادی‌مون تموم شد/ نه رفیق داریم نه سرزمین/ آرزو میکنم نفس آخرم باشه/ همه‌‌مون در شرایط بحرانی روانی هستیم/ با جنگ، جمهوری اسلامی قوی‌تر شد/ مردم ایران و کل دنیا حامی نظام شدند.
@Fars_plus</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/436334" target="_blank">📅 11:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf132fa956.mp4?token=Bbrua-7h1guQntnK36I6HMWccMJVDkljBJ51NkYEuYa2f5AyaD15lQ-OkLuoh0uLf0tqHV2VlxdwucXWlR4mzEu9c-KgPjz6sH2hpoJn57R6iMf-SpelF2yWJryRxlmidu9pUp_JsE66kigN06eyEdFXDTDtykPi3oH72GQmlem42SFKi3dGqiNqwKAYxwyqmpAqAndzKqNlq90v_vJpu0L0n89YRm78W339Fcr8l8Xig-yHHDcZXFJnn6JTuypb77QV-StUC-gim3fswNxoB4K7iogYflqk9hzMBFKkynWtrp4u3KEObn-TMyIGpL21EKMy5If_8ZhEUL69iBOpeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf132fa956.mp4?token=Bbrua-7h1guQntnK36I6HMWccMJVDkljBJ51NkYEuYa2f5AyaD15lQ-OkLuoh0uLf0tqHV2VlxdwucXWlR4mzEu9c-KgPjz6sH2hpoJn57R6iMf-SpelF2yWJryRxlmidu9pUp_JsE66kigN06eyEdFXDTDtykPi3oH72GQmlem42SFKi3dGqiNqwKAYxwyqmpAqAndzKqNlq90v_vJpu0L0n89YRm78W339Fcr8l8Xig-yHHDcZXFJnn6JTuypb77QV-StUC-gim3fswNxoB4K7iogYflqk9hzMBFKkynWtrp4u3KEObn-TMyIGpL21EKMy5If_8ZhEUL69iBOpeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای پنچری خودروها در اتوبان تهران-کرج
🔸
ساعاتی پیش فیلمی در فضای مجازی منتشر شد که نشان می‌داد به‌واسطه انداختن میخ سه‌تکه در اتوبان تهران‑کرج، تعدادی خودرو پنچر شده و ترافیک سنگینی در این مسیر ایجاد شده.
🔹
رئیس پلیس‌راه راهور فراجا: شب گذشته در جریان یک تعقیب‌وگریز برای متوقف کردن یک خودروی شوتی بودیم. این متخلف برای جلوگیری از تعقیب پلیس، اقدام به ریختن میخ سه‌پر کرد تا بتواند از دست پلیس فرار کند.
🔹
در نهایت، مأموران فرد متخلف را شناسایی و خودروی متواری‌شده را توقیف کردند.
🔹
ادعای مطرح‌شده مبنی‌بر پنچر شدن ۴۰۰ خودرو درست نیست و تعداد خودروهای آسیب‌دیده ۲۰ دستگاه بوده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436333" target="_blank">📅 11:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8488a5fe75.mp4?token=L84akMxMXkmQ6dkkhM4NQ-h4waSoP71fh1BSE2EKDLkcxgwL2yDtRdEBEq9exiEKKZ8xLJ2V-1b0lI6V0Frfrksibcstuium6-zqjBH8dnutUu2dudHrienfdwiE-qp4kHKAEFI22qy7rptlGYFHn8NZELyDBqffI2NrbheoZOEYsBl5m547UubsatNaTxN2SKvyK5e53OZh-pnKrNQCvjQyd7BAqmqPjgyBQqop2HYIndJegfs96ieCMOQch7AciQmDJlITiuhlx3fuc2b3QiVsF_Sv5Hp3QnthpZZCUr-L8jLH26iuOLGsCgcNgnYOkw_NGUThZ9cflopGXik8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8488a5fe75.mp4?token=L84akMxMXkmQ6dkkhM4NQ-h4waSoP71fh1BSE2EKDLkcxgwL2yDtRdEBEq9exiEKKZ8xLJ2V-1b0lI6V0Frfrksibcstuium6-zqjBH8dnutUu2dudHrienfdwiE-qp4kHKAEFI22qy7rptlGYFHn8NZELyDBqffI2NrbheoZOEYsBl5m547UubsatNaTxN2SKvyK5e53OZh-pnKrNQCvjQyd7BAqmqPjgyBQqop2HYIndJegfs96ieCMOQch7AciQmDJlITiuhlx3fuc2b3QiVsF_Sv5Hp3QnthpZZCUr-L8jLH26iuOLGsCgcNgnYOkw_NGUThZ9cflopGXik8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف نمایندۀ ویژۀ ایران در امور چین شد
🔸
پیش‌تر شهید علی لاریجانی و عبدالرضا رحمانی‌فضلی چنین مسئولیتی را برعهده داشتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/436332" target="_blank">📅 11:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d76ab538.mp4?token=LfF5KRfNfOFu2igeC81cnsxXQaORO2uydn_W7-JAfNkWeYZF77KIQuMifTuTyEJ22CGY0C-4ChP-GT4bWQBeZZlbwstf8rghORjG-TyAqro_SLXY7vZWOfrxqhipRgYIl_QmyhlpvewjWyPxp-q3AJ38GO6EMMkuew744BEDi8QnhkS717Zzun70hL3r6SmkSEL4-KIhel6OO1-XjDy0zrELD03wr6la-leuL9--HXB_-8h8eqVTYugjtcE40a1NucNdmlp0BTrutF0HgxDc9l7dw16DCH25FBhHf7n2W2a7y6oVCD00eksfonVrewnxeYefrqK4wXgjyWsPeJvoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d76ab538.mp4?token=LfF5KRfNfOFu2igeC81cnsxXQaORO2uydn_W7-JAfNkWeYZF77KIQuMifTuTyEJ22CGY0C-4ChP-GT4bWQBeZZlbwstf8rghORjG-TyAqro_SLXY7vZWOfrxqhipRgYIl_QmyhlpvewjWyPxp-q3AJ38GO6EMMkuew744BEDi8QnhkS717Zzun70hL3r6SmkSEL4-KIhel6OO1-XjDy0zrELD03wr6la-leuL9--HXB_-8h8eqVTYugjtcE40a1NucNdmlp0BTrutF0HgxDc9l7dw16DCH25FBhHf7n2W2a7y6oVCD00eksfonVrewnxeYefrqK4wXgjyWsPeJvoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مطالبهٔ غرامت یک خواستهٔ بسیار منطقی است چون این جنگ غیرقانونی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436331" target="_blank">📅 11:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1625c51ea2.mp4?token=jWD8G_TXuA6LGIlaL6HMIubtm1oYrBQ7xn9LyKEKwFbpygzPLQ4jJLJHKEKrj6g-PR3vOOKc02nn1sfycsvkyMYqXonzFOXQmIVZbX_a6nwcVPPxzw21VijFZx-xf1fRsWsJqBRdJ55O5fIi4AiqH-w5vNXbaToVEoL93iSMVxWuNMg_kPv0XgFJeb2XzjqQ0P0oljdzlWVPQRPEI3wge3TSKpu4m37LWmFJ9JQ_8AN1_X8o7grSuU5pYjBeqS7xTfUcfpJ0zPNvI1ONOpnVw835lTp0DKMwKSxXE8_Zqwnfg5713gOUxHlh61jOIfPwBiBlx-9PRLoEN_J2KDi4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1625c51ea2.mp4?token=jWD8G_TXuA6LGIlaL6HMIubtm1oYrBQ7xn9LyKEKwFbpygzPLQ4jJLJHKEKrj6g-PR3vOOKc02nn1sfycsvkyMYqXonzFOXQmIVZbX_a6nwcVPPxzw21VijFZx-xf1fRsWsJqBRdJ55O5fIi4AiqH-w5vNXbaToVEoL93iSMVxWuNMg_kPv0XgFJeb2XzjqQ0P0oljdzlWVPQRPEI3wge3TSKpu4m37LWmFJ9JQ_8AN1_X8o7grSuU5pYjBeqS7xTfUcfpJ0zPNvI1ONOpnVw835lTp0DKMwKSxXE8_Zqwnfg5713gOUxHlh61jOIfPwBiBlx-9PRLoEN_J2KDi4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: خوب بلدیم چطور جواب دشمن را بدهیم؛ آمریکا فهمید که با تهدید و فشار اقتصادی نمی‌تواند ایران را از پیگیری حقوقش منصرف کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/436330" target="_blank">📅 11:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7QhSZIrp8nzfqd6I2Czp0HU-uMiU6cYkN3ndT0UnJ0IhxmZvo8n5TYJfq4FxqGda3hLmukLW-XkMqrimJ8mZ9dBJ13f2oc7qP5rhirZMJKOxmNII5MNT-yc-ic2MTJpW5Pik79ZYWXzykzjQg-nfGlEoy6fsNwzmDbImojqirD5dhV9v-nBvFSq8GHy_OsK8BmTDJicDdkRoij3hgsuyePX_MSFzkKdnU3mDl7Uq1LWikPCdEBW_llwKCTmQq3Q_Bt_w4ztNWbiuYjok0rdGsTr0Edi-4lo_vRzjGocHv6ijthWYwIjwIR3GPoSjbX11KDH5N5MDHIJuvsc3nGqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روایتی دربارۀ آخرین پیام رهبر شهید به دانشجویان
🔹
مهدی عباسی‌مهر، فعال سابق دانشجویی و مدیر امور سیاسی نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها با اشاره به فعالیت‌های تشکیلاتی دفتر تحکیم وحدت در سال‌های ۸۶ و ۸۷، به تشریح روند دریافت آخرین پیام مکتوب رهبر شهید به جنبش دانشجویی پرداخت.
@farspolitics
-
link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/436328" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297099f648.mp4?token=ob0vpo3n8aqu7wsgf1saBoWccKeirwecthgyRICoV36rjnLAOngOzjG-rf_v91IiBGIzT2zblzqehgXRO7hk4y-zFHjT9Po5MB-dNKj_jIc6mpI4oYVX8h6dEjmijo3N22DE_zY7BHUXAfYL4V4ERN_xTd1kbDVCEdWG6BWXBK0RYK3QorVW-DN7Qw7b0fin_4IYagZ3wTEDpw_hRU9t11mehZkVhI84gIkZLSMA2CgK0fRYHies_OFmcfNeKwg2Ha3sD4-jHKlmEY-Z67vu-Qn4T_j84yTWJnsn7RfIOXpBknTvqnHqaXONARtN2d3lv0T5l1PAZRQCeKLDRsLJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297099f648.mp4?token=ob0vpo3n8aqu7wsgf1saBoWccKeirwecthgyRICoV36rjnLAOngOzjG-rf_v91IiBGIzT2zblzqehgXRO7hk4y-zFHjT9Po5MB-dNKj_jIc6mpI4oYVX8h6dEjmijo3N22DE_zY7BHUXAfYL4V4ERN_xTd1kbDVCEdWG6BWXBK0RYK3QorVW-DN7Qw7b0fin_4IYagZ3wTEDpw_hRU9t11mehZkVhI84gIkZLSMA2CgK0fRYHies_OFmcfNeKwg2Ha3sD4-jHKlmEY-Z67vu-Qn4T_j84yTWJnsn7RfIOXpBknTvqnHqaXONARtN2d3lv0T5l1PAZRQCeKLDRsLJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیاتی از درخواست‌های آمریکا از ایران در مذاکرات
🔹
براساس شنیده‌های فارس از پاسخ آمریکا به پیشنهادهای ایران، ۵ شرط اصلی واشنگتن به این شرح اعلام شده است:
🔹
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
🔹
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/436327" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f44c6199.mp4?token=rm9crY7QXYqYayagOXDGNnb39EYNskMPhOsD_f4Ptb7kdz0t1URrt67_iHLuvW-xAtmsrT9RCA4vkiRXlLvqyxiWE_XubdWIGSi0AcD50Ub-z9_lQgTmvlrcA-xD5yO4skMgMhdl_T8AkWrX8O-jYEUam4-gtBc1T_0deZAQ4WjM3A_qmX_Q7gb2RVr6Ps9YuLPm2HzlkgeylrZ6PLvmMMbkC_J4JPFzemAsUbfhuIvFkVoaF2HtVtrsBaepv3Qs5A_0pW_aP7KVOLUCqTQyBDI5NGW-_BR_IVJf07ZkOXg8BNm6MsKj_8CphanCTknPBDGjrVi-Tr5jXMOTBTh3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f44c6199.mp4?token=rm9crY7QXYqYayagOXDGNnb39EYNskMPhOsD_f4Ptb7kdz0t1URrt67_iHLuvW-xAtmsrT9RCA4vkiRXlLvqyxiWE_XubdWIGSi0AcD50Ub-z9_lQgTmvlrcA-xD5yO4skMgMhdl_T8AkWrX8O-jYEUam4-gtBc1T_0deZAQ4WjM3A_qmX_Q7gb2RVr6Ps9YuLPm2HzlkgeylrZ6PLvmMMbkC_J4JPFzemAsUbfhuIvFkVoaF2HtVtrsBaepv3Qs5A_0pW_aP7KVOLUCqTQyBDI5NGW-_BR_IVJf07ZkOXg8BNm6MsKj_8CphanCTknPBDGjrVi-Tr5jXMOTBTh3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: دریافت هزینهٔ تردد در تنگهٔ هرمز هم مبنای حقوقی و هم مبنای منطقی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/436326" target="_blank">📅 11:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuz_okSCCeFORHkZFo18hrsdguECrFHk55HbU29pHvjXFKGbUlGi4J-TUPdr3CvUneuxS8FXSXwv3IQCu0gcedb5WyMaZFNRTsq0Bi3x_csNol9Z_cIcHH_YMpZAsjo68C7-57Lw8oBQBmw2PUZjkuNpWGbGzU88MOez63IRh8oxsVhFuwQLx6yrJZQy6Cp_tdmjyMm2Seo1ml7g2g0DJYpOTHVi3vmkGPfYBbTDhNhYMiTbs88sFDCOtIrlXJx-6hBaronZd3SKV_0X3HRSMqL-jbZWiElkJ7W5Hu5rphwLAirZB8psdTaEFPeTkE1_WoyDsKhd7vRNVNqF2T6hHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNxAq5PrqP4VOJs5LxZMvjSPhjpeGvOQLyXLMIPziYiaZdY1G67OmVcg_fuySQvFU2fwULnikXvkztJQY7kvsIOBY-dYmWoqUER0waHPmHbTRCaEPmH0y8m2Kgk1jcLIMPHxnupwXEG3zRPzEWg5CrL9Ony5JJaicZd31HfwIFjWeMuCXVKJLx4vUZ23jbiYDxIrOL2_m-TsOjWHTVlDP4DVs06Gusk4qNNFKpFe0iAGUQQjpVuD2rujyVKXFEz22Yd7W9YaSV5Y_PqJfAuIK4fEfm4djtwIpLUKMd6wD2NPtHCZaDFeEQP_f3-Rk2Gagk1zzoukkjTVKrzQnBKx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwFSl6ajNgSbyehHnPFQp2sHgD3m4irzJ_PNXa-0fe8Jdbwu8fL2XC5m_EcBMjzsiuY7dYF9JYaqWUEwL_AMwG_HDdRoD0MVMQD0QFZE3zCYHmKhmpZ_o_t7gXNr-98G-vgjPa5s3S3IrbbIfLzuSEOcwZ4kLQWRsjDNhNMcH4vNpjewdH03ilLbCf2pVNMFxUl_Ih01Dt1TxJ2vVF6QQNmKxG1JM3nFYPbZkqXw--bwvCJS4sjAFG75j18PEPk2NFK3PeZ4ZV6xJRwevTEkQ3bQ33c6njcuYkk7RDtgh3yo788cUiEIpz5dTk_t3eBnm5ebI6aJKm-V68Pcjl3B7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVW6uTvn9GfjhmrdnKC_HVtgdUz2k0kv3oc2eNHX6m8Il1MayolzpaFxJgS3To83mzdGkvm-rPQfpRnO3y47DjwHEHrTY8Burfcan1-_7TxHPYEzM1WDMKzWwr_8Sb3fk0tL1TzvDpkTA9KDn4gUNhynjLsf1Ix6y_1h5zEDcRcTygDLYMlFWL3WmsBc6wRSNX3DkUXcreoVDJq6atYOLQOnL3R0C84qWJEvObgSk-HBRxpqc6Ow5KTL50BJCcoMY9iMqcGH_uHwppo5zlLozG17nkgDZy2RlYkOZro8WlFyEV8We2J06TY66oEwjPZQmcL1qMNpGZB2KaXScZYSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djEVhuYqzPAMmgVZGwsnMRg2DwJbieW5bjVi-D4CxegqIV1VrEneuLeK2w88byGxgE4OjxU2kvPgb8ChdGskr5yxbLcmtzTkgQvtaST7CcIgXa4JIFjr34LG2AoU05j-sS1U-eo3APA-IJiz8fT-owyOTyMOAMgujpX7yQ-QYBiy8CylnKfatCszlEMoDw7O54in9ZB8zoA4poCFShyxAjCGAmRQeeyruroSB6-K_wvg-cF9Vy9Ox1V2SFYPaY1iYc0INGitzNNA00_wdeYx2KyIIWdw_txX2hflj5R0ml6QnQABEbNn5_vONIm883FJ-tIVhrwzWg66Po5C1uDobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iH54YlDc4KpjzC6aA7VIjCKqwPOMF8NegsNLhWYOqr5HvjYXgMv3QNWu0DMlLsoGx5WJJvXCY9EZwdl2EIEd6OW8lvZ14q6Rwe734RUvK194klCM6cmAMzpFhMoxZv3sTT5MRTc22VYVpH7lkYMn93SH8j0JAqchBiWTdULNxrzJ4srvMa5VpVbZQhE9sAurhHdCXHFrRy5lVmOta9pkcJHJtOUeyzMKdLJAyO6QlmZek5gorIYQMA4tXPHt8oVSPqq4kdeovDQLn1__bKXlPcvohGwZWKuGsGi66fVxxc6uHxyTGVWvkekaWkBQtQS_3eOz4DNCOIei7s0t-6Rg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Nw3LQNLJkuHRmhEFfaP_Wn5MM_kbpsO1YRsEBAOhAhy-5DHgYJhbV8Mun189iZLsJ4CrsWPFiaSyVtmCcwCDmCe52PZ71UxTEpx1SVIiphO1DEF3IQ88BCpMlilFj-xEl2a9IBCzYiuw0wqJHsUTtafnCBrlMEhELaK3cWms9WOUqiBLBoD7Y4tK-qaEa07gWgnGXO6t_QtCTOMg7z4pUjVXVF57rikMCj_EP7XY1pQz0KDj8hH-neZwHaiBNVSWHnHJXDEYWEESAhP09YoHm7aALIBSFiS8-1YQyGfqydna1O129PByOwI_wKP4AqFSoCa-6LA9WTUhcsxKtDjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت انبه در هرمزگان
🔹
انبۀ کال هرمزگان در میانه‌های اردیبهشت آغاز و عمدۀ آن صرف تهیه ترشی مشهور جنوب می‌شود.
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/436319" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720508ae65.mp4?token=IowpEsaOyQo3QcvzqBKn8z2RBUhUo8L39nv2eQIr1KIeqfzY490A2-1o3zfDe-nDnK9j_WcNVGnZpzNVxEkRH0jOojIWd6BOd_zbsQRHHNlMWfVzfA-r3rTLlMW7a7wU3JHNgNMoNiPih7cCtIHKmOrD0o0afO_eJVNtZDBEL7XyZixdqTF-FRnEe13saNL5S5jdtplfgclkkZsFl39sEWCNl_MnXt2d_x2W1jneJyqoAQgd-nLQ2fGg9rYM9s1Nw5JFNfEe-fhdL7Oo_XmdFNO4OPtQtMYoe5EJdaEwIRoVPpOHf4jrFoVGFiDGQEwc8cdJZjPBIAdtGn3VC4JhUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720508ae65.mp4?token=IowpEsaOyQo3QcvzqBKn8z2RBUhUo8L39nv2eQIr1KIeqfzY490A2-1o3zfDe-nDnK9j_WcNVGnZpzNVxEkRH0jOojIWd6BOd_zbsQRHHNlMWfVzfA-r3rTLlMW7a7wU3JHNgNMoNiPih7cCtIHKmOrD0o0afO_eJVNtZDBEL7XyZixdqTF-FRnEe13saNL5S5jdtplfgclkkZsFl39sEWCNl_MnXt2d_x2W1jneJyqoAQgd-nLQ2fGg9rYM9s1Nw5JFNfEe-fhdL7Oo_XmdFNO4OPtQtMYoe5EJdaEwIRoVPpOHf4jrFoVGFiDGQEwc8cdJZjPBIAdtGn3VC4JhUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارع‌پور: شهید رئیسی شورای‌عالی فضایی را پس از ۱۱ سال احیا کرد
🔹
وزیر ارتباطات دولت سیزدهم: شهید رئیسی دولت را در شرایطی تحویل گرفت که عده‌ای اجازۀ پرتاب ماهواره را به این بهانه که مذاکرات را به هم می‌زند، نمی‌دادند.
🔹
شهید رئیسی اولین رئیس‌جمهوری بود…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436318" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsX3b4IMcR3rvX8shwhDn-s6XNykthdw63ytVY0qZPJ9LcnRNBBqtVcxaSETZIVEFkvkUhM9m_KyDbPwjBxWwWwf2HsGkVyZ49LYrtrwTHHdn0LfgWPcyz0Vywg2B8c2GEG4AYfwJNI_VyxkVLhgCTOnS1t24jIixpumqokPVRypVZDv5ij3fA233e-IBhjANg9ez01bujeZ9xmFCm5OdZ1Rap77zCJHYYcocwmYPG6VO-eiBaIaAOjqIoi_5jHlHCsDbazzixcihopStwb-6D7_L2rn3PcMmV9aLxee0-jqRRIxDUSjaqwvMkCbSZzOhO5OEIHoGNnOHqL__t5Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovQXVKdGuMIaIdJnJGwjmOAZPCtYDpsZr4EO2CtsvPD9QRvBrqKQ4BT5JR_8u3mIpfK5Omn6RLtAJyyC9v8sfemKTfJdUmdRfi6J20VN2o_54XP40H8pEj1WW33DVS3GpZnpZ7_cW5rtjOYPXvY9lYCiM3mb2EZ0gs-XtF-Ek4InbAw8IlIXPLeXJTT5h5hgQsCEBLbQEm4nsb_ZoqlRWVGe619yCKchWWh2QtM4oplxoide0pzNOE1OZVjunCatOgX5N89yonSFpN8mqIvySxgQyCVpoHsDvHFOqlGkzIRHwgM0aRew6scpvy7xaQfCMHuF3Ej3FT5Q1CvjEY77Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvRwOW3iM2IOmqd5ElJlnm-x9D8xqVkaLPp76mh6L9FF30ZB9YDT9l1YPaX4DiKhLSMy40ihFIjAe_VR5gQLteqYYtewFWuPDCZ2egEDqG60LwHnt08xE54Fj0NXBzWxiowoTKFrZZBfiz1YCZ4D0MFzyb2wIYu8wqufR8lnoRrpUds1IadeHNOj_s9UJ9L6dh79y8wutDfjnqqfLCRt3nuHLmvcvfdikrV51oUgmBWhldOxn_w-Lzdgyy9i6sW6EGqolY5MNiAEOTT_Le15-FOTCLwLWBFdIhYMuEExVJdpf43xQZq2vWzFiNyQBjsEk7YTwbfNuo3rvR3cIyuTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Chu8-djWZ521JBOViWKxs3VaGyGW5EUH56ZT-WlVOHmYQi-_KAu2FPFTc5qI4RoVmwuFv9Rt8VVNJAMHiMS9RFJTsEmQX-J6qmRxOyp-PCoUoAJuXbptvVFcbM5R6hP1XlYJzst4FppzcYCQF1n2n-gZvOipPrZuCo-z8eOdV3BVHYZ2Pj6qkWXbS3aHj231JoC-CCL--xji4ZDD2qGZCmgvNjf_n0JAaKZZs-U4p6dEeAAVjFSKd6Hn1Dtkvy6lZUSVDAcCZxYsbudaKTRAylgQF-M7-UehCl4c8GmbiaIZwfZ5XDlpeBiedhvSje4u--7SFeXMaYFQLy6s2-PaPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قلعه‌نویی: امیدواریم ویزای ۲۸ بازیکن را بدهند
🔹
۴۰ درصد عقب‌ماندگی بدنی و فنی داشتیم که ۲۵ درصد آن را جبران کردیم.
🔹
شرایط سخت است ولی نباید بهانه بیاوریم. @Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/436314" target="_blank">📅 10:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436313">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc49b0f7a.mp4?token=QKMp7mV1ZgtgytBIUKsMNJexsVA6i462oxsle66LHTEaDe86WXfiN2p7erIptmMeBGwWH6nxG131i66oxQ5KfeDjpjbX5lGWD3B7iQbvseyGCJ-Yz3yZrMo-tsAGmanHwzTQa-GOmjZxIlXKYLgyhmRufnZ2Jx4j34e_Sp3Vdbtf98KW28ajkrUy0oHdzTZd5AB8cvJURxmV2BtjoYZM3y3xD3uthJGesZ_TjO7Dev-m8_7q7gjdBfG8uyE4W9J81mz5ikQjr1NxtnwXl7rLKUBwb00t-RrrQ3qG8r69oFBLK_B1VIL9gmrXGodH902OtH1fjaCx1A7wrX2f0Bw9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc49b0f7a.mp4?token=QKMp7mV1ZgtgytBIUKsMNJexsVA6i462oxsle66LHTEaDe86WXfiN2p7erIptmMeBGwWH6nxG131i66oxQ5KfeDjpjbX5lGWD3B7iQbvseyGCJ-Yz3yZrMo-tsAGmanHwzTQa-GOmjZxIlXKYLgyhmRufnZ2Jx4j34e_Sp3Vdbtf98KW28ajkrUy0oHdzTZd5AB8cvJURxmV2BtjoYZM3y3xD3uthJGesZ_TjO7Dev-m8_7q7gjdBfG8uyE4W9J81mz5ikQjr1NxtnwXl7rLKUBwb00t-RrrQ3qG8r69oFBLK_B1VIL9gmrXGodH902OtH1fjaCx1A7wrX2f0Bw9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه‌نویی: سخت‌ترین تصمیم دوران مربی‌گری‌ام را گرفتم
🔹
انتخاب ٣٠ بازیکن برای جام جهانی از بین همه بازیکنان شایسته تیم، یکی از سخت‌ترین تصمیمات فنی دوران مربی‌گری من بود.
🔹
خدا را گواه می‌گیرم در انتخاب بازیکنان چیزی جز معیارهای فنی موضوع دیگری دخیل نبوده.…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/436313" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owJThNQcmKttPI5PgYe-V0UH9jyfC_7MZGa0jsEIhizCW3qI84jvg4YNJtRJQhtYK9NlvpDItIdUsR1gh3RDlvGT4_o0_tz_5bTdValMwo-h-45FzTBKku1X_V9vPOxSiFu2Ob5JUX7MT1c4syCFaSp269v20HcV9kU8YC9MV-4Oc2dA0LpcbQtcA1vn1Ypqqiipt4pr2d_kLOTR8yNuwlZ2B2BJ18O5Uqo_dWb05DUc35HZiixB4bK9q2TTn0IhXV9ppGlha8e_ug9Sy_KVHGU98NRZwhWOcvKN01TfkHvZQT23fSZmXM3cAZ-7cx5YETo_TIFcvfVNFHGbeahbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشان ملی «روابط عمومی برتر ایران» به ایرانسل تعلق گرفت
🔸
همزمان با روز روابط عمومی، سیزدهمین دوره «جشنواره ستارگان روابط‌ عمومی ایران»، ۲۷ اردیبهشت‌ماه، برای ششمین سال متوالی از ایرانسل تقدیر کرد.
🔸
در مراسم پایانی این جشنواره که با حضور جمعی از فعالان ارتباطی ایرانی و بین‌المللی در سالن همایش‌های کتابخانه ملی ایران برگزار شد.
🔸
در این رویداد، نشان ویژه «ستاره ارتباطی مدیر ارشد»، با کسب بالاترین امتیازهای لازم از ارزیابی‌های تخصصی و به دلیل شخصیت و منش ارتباطی، روحیه تعاملی و نقش تعیین‌کننده در بهبود ارتباط با ذی‌نفعان و نگاه تعالی‌جویانه به حوزه ارتباطات، روابط عمومی، رسانه و افکار عمومی، به مهندس محمدحسین سلیمانیان مدیرعامل ایرانسل اعطا شد.
🔸
همچنین روابط عمومی ایرانسل، بر اساس رأی هیئت داوران و به دلیل درخشش در عرصه‌های مختلف ارتباطی، به‌ویژه مدیریت هوشمند خوشنامی سازمان، موفق شد لوح سپاس و نشان ویژه ستاره ملی «روابط عمومی برتر ایران» را دریافت کند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436312" target="_blank">📅 10:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps6dpvSGXl6YLHWXv7cEn0hkv97wJUnFJPMWq8ZP5X7qkrXkOnh-7p7U3jI1XoRjPf-USqDk28nfsRHhq7rBPBu9YmqXGDJtsTkF8GjoxZFNCD3DwAuNu-FUPe9eYfugzPiCj6MmjVHpCiaOF_Uk8v5IT4E335nFp7_CncDytny0Gmccx-pGdP-A9de_zhV3dhN-5idja5rn6P2wALZLWGM_vpWlr2k95Vmyn21D-x75fQqC7ohFeo5B8msrTRHdlbqYx-MVmNO2hqgGF7IkeJDIRwSHK3F28oBybR5AorBY9gzt6T2MUZgrdOxycTALomr2x1G7d2C_h1Ak64E7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر فوری: کوچولوها مهمان ویژه پارک آبی اُپارک!
🚨
💦
فقط تا 15 خرداد!
📆
میتونید بلیت هدیه اُپارک مخصوص خردسالان رو دریافت کنید
😍
🎁
برای دریافت بلیت هدیه روی لینک زیر کلیک کنید
👇
www.opark.ir</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436311" target="_blank">📅 10:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/436310" target="_blank">📅 10:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eb18e991.mp4?token=YC64ABiIh2or3QCXbtsFM0wybfAXWrqOsO14ap2kYxYTcpJTTbPYGDApZjZNeOjuwG-2wU3CwbtHRyWFGf_BLmzmOse0TMTocKtPHgN3hLoDKcsQvx9vpvDJY4pmoADNUP4lzsCAXmtwcoiw7vs9keRtJJx534F2XI25vlCXs_Et1DCWWRolEoOuXYIVP9TRGxjS_30N2RSFto86OfBGiUvFFyhEbKFtjdke_LA_QGYfZdTwcYJ20ZyrKli4tLApOz3GTNrb_Hrwx_cbRny2Dc4JXkQUlE6RXGejQjjPF3-HeM7afWkBe6NcftJXfuqaiKXCiPJzegdXwYnEMtHz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eb18e991.mp4?token=YC64ABiIh2or3QCXbtsFM0wybfAXWrqOsO14ap2kYxYTcpJTTbPYGDApZjZNeOjuwG-2wU3CwbtHRyWFGf_BLmzmOse0TMTocKtPHgN3hLoDKcsQvx9vpvDJY4pmoADNUP4lzsCAXmtwcoiw7vs9keRtJJx534F2XI25vlCXs_Et1DCWWRolEoOuXYIVP9TRGxjS_30N2RSFto86OfBGiUvFFyhEbKFtjdke_LA_QGYfZdTwcYJ20ZyrKli4tLApOz3GTNrb_Hrwx_cbRny2Dc4JXkQUlE6RXGejQjjPF3-HeM7afWkBe6NcftJXfuqaiKXCiPJzegdXwYnEMtHz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگۀ هرمز
🔹
عبور فقط با اجازۀ ایران ممکن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/436309" target="_blank">📅 09:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">ذره‌بین بانک‌مرکزی روی معاملات آنلاین طلا با سامانۀ جدید
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد ورژن مقدماتی سامانه‌ای که قرار است بر معاملات برخط طلا و نقره نظارت کند به‌زودی قابل دسترس خواهد بود.
🔹
با شروع به‌کار این سامانه انتظار می‌رود از بروز تخلفاتی مانند خالی‌فروشی در پلتفرم‌های فروش آنلاین طلا و نقره به شکل قابل توجهی جلوگیری شود.
🔸
هیئت وزیران آبان ۱۴۰۴ بانک‌مرکزی را مکلف کردند که برای نظارت بر معاملات آنلاین طلا و نقره سامانه‌ای طراحی و راه‌اندازی کند که گویا بانک‌مرکزی مراحل نهایی این پروژه را طی می‌کند.
🔹
پیگیری‌ها در خصوص آخرین وضعیت عملیاتی و اجرایی شدن این سامانه نشان می‌دهد فرآیند پیاده‌سازی آن، تکمیل و تأییدیۀ اولیه از مسئولان مربوطه در ستاد مبارزه با قاچاق کالا و ارز دریافت شده و در حال حاضر، سامانه در مرحلۀ انجام آزمون‌های نهایی امنیتی قرار دارد.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/436308" target="_blank">📅 09:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436307">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
مأموران موساد در تور اطلاعات سپاه گرفتار شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/436307" target="_blank">📅 09:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قوه‌قضائیه: اموال ۱۲۹ نفر از خائنان به وطن در آذربایجان‌غربی توقیف شد
🔹
رئیس‌کل دادگستری آذربایجان‌غربی: اموال ۱۲۹ نفر از عوامل دشمن و خائنان به وطن با لحاظ اقدامات ضدامنیتی و همکاری با کشورهای متخاصم به‌نفع حقوق مردم توقیف شد. تعدادی از این افراد عوامل اصلی و نفرات مهم گروهک‌های ضدانقلاب و تجزیه‌طلب هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/436306" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام تقدیر فرمانده قرارگاه خاتم الانبیا از مجاهدت کادر درمان در جنگ تحمیلی
🔹
سرلشکر عبداللهی در پیامی خطاب به کادر درمان نوشت: به‌استناد عظمت وعدهٔ الهی در آیهٔ «وَمَنْ أَحْيَاهَا فَكَأَنَّمَا أَحْيَا النَّاسَ جَمِيعًا» هر کس نفسی را زنده کند، گویا همهٔ مردم را زنده کرده است.
🔹
در این لحظات بعثت مردم ایران عزیز پیش‌از هر چیز یاد و خاطرهٔ رهبر و امام شهیدمان را گرامی می‌داریم و به آن فرمانده شجاع و حکیم که با نگاه فراتر از زمان، مسیر خدمت به خلق را به بالاترین مراتب جهاد پیوند زد و ما را در مسیر مقاومت با شعار «حفظ کرامت انسانی» رهنمون شد، درود می‌فرستیم. همچنین یاد و خاطرهٔ فرماندهان والامقام شهید نیروهای مسلح و رزمندگان فداکاری که با بذل جان خویش، ایثار را تفسیر و مسیر هدایت و ایستادگی را برای ما هموار کردند، با احترام و ارادت یاد می‌کنیم.
🔹
در این مسیر پرافتخار، ملت قهرمان ایران و نیروهای مسلح همواره از حضور تاریخی و پرشکوه شهدای کادر درمان بهره‌مند بوده‌اند. قهرمانانی که در میانهٔ جراحت‌ها و خون‌ها درحالی‌که خود در معرض خطر بودند، از جان گذشتند تا نفس‌های مجروحان برقرار باشد. آنان که در میانهٔ «جنگ رمضان» علم و عمل را با شهادت پیوند زدند، اکنون در کنار امام و فرماندهان بزرگ شهید، شاهد شکوه ایستادگی شما هستند و بر ملت بزرگ خویش می‌بالند.
🔹
فرصت را مغتنم می‌شمارم و تلاش‌های مستمر و ارزشمند اساتید، پزشکان، پرستاران، پیراپزشکان، امدادگران و سایر کارکنان حوزهٔ سلامت شاغل در دانشگاه‌های علوم پزشکی، بخش‌های بهداشت و درمان نیروهای مسلح، بخش‌های عمومی غیردولتی و خصوصی و داوطلبان عزیز عضو بسیج جامعهٔ پزشکی را که در جریان جنگ رمضان با مهارتی مثال‌زدنی جان بیش از ۳۴۰۰۰ مجروح را احیا کردید، صمیمانه ارج می‌نهم و سپاسگزاری می‌کنم.
🔹
شما نشان دادید که در میدان نبرد، مؤلفهٔ اقتدار، تنها گلوله نیست؛ بلکه دستان مقتدر شماست که در تاریک‌ترین لحظات، نور امید و حیات را به مجروحین باز می‌گرداند. حضور شما در میانهٔ آتش، تجلی واقعی آن وحدتی است که علم را در خدمت عقیده و دفاع از میهن و آرمان های بزرگ ملت قرار می‌دهد. نام شما قهرمانان مجاهد، در تاریخ این جبهه به‌عنوان «حیات‌بخشان» ثبت شده که در سخت‌ترین لحظات، به‌جای عقب‌نشینی، به‌سوی جراحت‌ها شتافتید.
🔹
بدانید که هر تپش قلب مجروح و هر نفس بازگشته، گواهی بر اصالت رسالت و شکوه خدمت شماست. از خداوند متعال برای همگان سلامت، عزت و پایداری در ظل توجهات حضرت بقیه الله الاعظم(عج) و تحت زعامت و رهبری‌های حکیمانهٔ مقام معظم رهبری و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای(مد ظله العالی) مسئلت دارم.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/436305" target="_blank">📅 07:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuWHbZ18V6gI1lPv-g1WEgwB-7igBMugK-ijI29ZOjU2lXRGUXc3cjrq0BqTDWtJNcyFF4JQjkEDvhBcz20uIrHKWxyC6mqBnCrKo2FsVMlZdJiThDOUrzUZnHa7KiZSLY-yIyDP4QvxgmWoczcswGHEHTCooUeI4gBvvagcsF-8Xb4_KsgJUoxeOhWrURT-VW-vUtYFRQRZ13P0U7D_9x26kqqwim_8FSx7vrpPMz_45kFtY2KwvoIq4zXO-wyOmcRTKd6r6ksS1KQxZNNPin2xLrJ7ZTy4Je368Jymr2vvY0mJ9ctN9e4vxs6F0Huy_-U_jHTMJmoQJBP9Oqq4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت در اولین ثانیه‌های بازگشایی بازار
🔹
دوازدهمین بازگشایی بازار نفت پس از حمله آمریکا و‌ اسرائیل به ایران دقایقی پیش رقم خورد. نفت برنت در لحظات ابتدایی بازگشایی بازار به رقم ۱۱۱ دلار در هر بشکه رسید.
🔹
نفتی که تا پیش از جنگ رمضان کمی بیشتر از ۶۵ دلار ارزش داشت.
🔹
همزمان با افزایش قیمت نفت، کارشناسان از افت چشمگیر ذخایر راهبردی نفت و سوخت آمریکا خبر می‌دهند و معتقد هستند، دنیا در هفته‌های پیش‌رو منتظر شوک دوم به قیمت نفت در کمتر از ۳ ماه است.
@Farseconomy</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/436304" target="_blank">📅 04:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxivpoNXOMm9MF2-TRvaTUe8KpJj7Vc4-I4cpHQT6_Qk5CUYSUjmQyAMouKdBaX0d574OfvT8e7k349AvK-cAubJg9usenw7TWc0UU6vcCfLIyqxMj5LM2VpMmts-DgH_bWsQAd5ElNzPmOeCOtG6ZMS-IHApMayjGEUQ03Hbg40kWIjzN6iRke09B-F9jSQjzZeFF5d3UEvPuiISxcw2P5cw3td8WxNgpk2VSzrqtzvoa3u1I5NNY2UxEXf-rQOC5PJQ45CF0Qc-6qz0J3u_9Un_eFkrN5wzTsbeDdAb2MTofWkDOM8SwWduq2amZF3R1ll6nkxgahmJpDczaH0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjSzRsMe-eRTMCtvsq1EnvAXr6yFGuFqkdgB8Pi82MRgc8CsS4WA238zydXDDH5XO3c5EgH0i1bjYq15qfQWrIAZCm7q6hg0c-z4GTKwnHqzLP4bnhMz_DxAL8Bs1OC78XVGDLlbd4rbcUg2HYTigKjUkqfTvVDex8lc_2uVANgAdCsPmdOeR5XpPx51FfL6kIex3CX8wUspGy4evSIlv7JUyOiH88L-vFGT6EPGKYRWaA3E-M-L_2RTiP4rFCCKacQMqDYkbtqRG6B8c3TCgEJcSjLj9RByX2wml09q4pRpNCgZBgVGqHZESiepqAGGySB2A30G2R5rjzz2Oh96nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quIpD177Cr8d15sasUOEQcx9myRwFnsUx4fKWNeAK9E2mXStXNO0ycrFSThKOrUoOFZYv2Qh5NiZKjjq_emMIEQTtYFUYJgfeLCPOd-SxjScK7-A7C6qy3CkeS1G2ed-XUuvgAEQ_WeBosgznqLDs-qipL9qFGDa8Z8bHyIW3-UV1b0kJkVJQn2UucYWUoGlhL82AUbWODYH6gI6YMxCrwXHOy0MOSfs4B-YMN44t7aqYT-YMr_yutuya8Ft7sHSctcAOxFXfibU7bXTik56f4QtVpDVv_xy4JKlw3aOZCFzOuzF6Vml9qauLY5-tcJWxn-6ip_DZPyWfYRdXzOK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARq4oaLExXSl3kMrUv2gwldwF_Wfk8F5ywzqRZSJgvoXi7v_lrMb8RMMbuUqWIhw4RFZo4dfY3xgsub375e9RBF-rfIrKxUNHWB-ztQolRinlVXxUERB-BjiM6dZcH4RrG5ajC4nf2oM0JLVQbofVRVSTx8dy-nUa5LF1CAkeXzUOSQgo_J9ZqGTb4sLVKkuyrePvxvlZSD7eA-uvZJO6yTd3xnlB6w0JLpfStMwOjRkLrDae5LjsBBTZE32xM_lJvWFzQgn1NSjKp11mLpcGKHytoNv5L1MJ5V3m4vhyXNpbKBVAo7F1skYT1VZZx_XCGkB68qh6CSQrD5SEsXz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdVz2L6bXEZFhU7P0vwlYScoi7iUd_nj_uBeslrT3cxtuleRMMPiwvLEYQ_33W9oTIp57tjG8uMH-n1hxblWr3YsnLGSzFzCrCN3SpBpcxONPalbHqzYQeogPKIwLqhBWyI7ZzR7gv9krkS_DkXoiqn1sXC0qGEXrlInBAX4L8NEpnCYfUOeQfRZsZIWv6x5UKkyY8vDlf8iakzXFCR8kcDMo8E56kES1dxvWxg9iTInRnq28ngIOEZgnTpUZfDVa8nCSvSkyQYIcjK9ksuClUYaGZuuZ78UHm5LxTHhIF5YFmvDInUe6AUBNRABfEv6b9Xr9vWuK2NTw_Wp1tI45A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میدان‌داری اهالی باقرشهر تهران در موج ۷۸ اجتماعات ملی
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/436299" target="_blank">📅 03:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436292">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1M6B_8d9zGKglenpURe7HR3EGRiI7jsblhAKZbWBhxM6RGS7EOf1kOGnIKhnYp15K3EYyN5KzWtoBw5He34uXZLPXjyjJanFjfbMN7lqlflWkuFqlDtdUUrGnDPwPBRpgx93LD1G6V01EGyE8Ixu7H6VvTXn31L1-usUZtSHlTTYzZE_gWww-00wfMdYZ3gSCMg1I4rQTMZObMPooj95p5TtqROl5D4lCR5248wD2WvSXNkN-tMmqLolziWXJrjQ0je_R0SQSduKQvsSi69e7Oev0J3qj2FDCjADSqDEwznloDkpJ890mDtyA3SA1c_9ThGjdzvHEQIXo8W_N_gUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ib5QiT2mTZijTA9fv94HYU3NaIlzcTmnB78Towkvk4Y4MIK4v9XEY0R-oKzu9qOWaAD5nT5F9GDgi1yKCM6vuOFUPnypUPyxJD3zc65oGi5P7lzplPsZqX9Eib5dKDW4zHIjaYus3xqxTJf3ZRZqKag5CPGMRgFWCVilodz4M-JeUSzpjmW9GLyR4gHRAi3RK8Ai9BmF9KcSHyyL7DJJk3tqevbN5cd0wRKBfJN7X1PH1H8ysQiBFjKOhqjfnPOEq3PuHLU_DuvtyHXCdIXigPrvMpYyN-AOf28kiPh_CPTKxh8bCNy5LOq4rXsWqpkwQGD8owgN8xSCSZucoMPANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vktgAVYywTaB2988BiS8HIQhP3Y-ic6r9wf5sEI_BruJ2DCGwhAo3vtApD-fGLL_PvJG6xX0O9HuB1UsB1fium_RTtjYTEMLEE0sgYGQ9Cf-BUc1a9G-wsIt0H0_qoz24s726zhcYuUgZDn_7D0FYYPUp0DUQk1cLWLeBGCOU9z_1pvf7dhjTMNv-rX5Tpj6NV91392DdiTTE71ctYZgerpLXMARDN6hLpqRETa_0ZcyU6br9sEx0SxGAXbj8xFgpEXbe9zbPIIQGC5FSqAQq-out9zjT-7tZFnTASm5ntfPlP2PtIwnQa_KtKpfhBPvaFa8pVc3Xz5_BtvZmwlFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfYZF9_8Vs4I6E19PA0vVq5dMJkj4Mrs50vDIOdrepdX8UvIEJ2x8T6ESCTwbAq9qdrGdeFwCdYHfCSKTPO9lPeH_M5ALF7b9IXD7wTW8nV9tV_PWH9jDwDHxdt3CsABi7HPQbqxN1GBTRWJ6oxDH6seTry8zVKDaQKcgOl80vABJla1EH4WGwnV8Y1CZS10OnDsQkR-4HrovFhQbR_wIEfVdUMjNlLWStnKQhbyFuH51OBI3OgHaAdjKkk_fU_JcXmYXpHBbjFd91rU7x4_a32j2ZVTInuHth109wkjuGvzODxF_E9NmOoRVIL611HetlnG25FMbsQTsKZBWQZnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVAjmOqf658XLixAx_4lRlpiYy8VAQsDip083LSNaQPeqTFRN9SFV6tKafK04pKWoOQszyx6Nm1p6WebF28IwDDn-rdwqY9pTPx7Rr6JmLpJD-5JvxdvSqDSFSOt4KUQgn5wCAg-kUQdMwGu1hYN2KKaDU5wqzl446e6zywkvT_aRf-gufEre6koqFOhXM4tc1CzXXbJa9A1BjGN8XOtP_uw71pAtY2PFvZkMM7FrARizGLcHe8RO_C3QrzMzROhJOe6Qry4F5p29M6sx5nHNOXJe9JeC6A3GhVjYlPY7svbtAawhMUY1ec8zjtEH0puneytQycFC_5-HhtQ-SMHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srhNrbOILQ4OURFnNsj2YLwXmQT2wjxoWTyaQBuQXaXPhvjziX3LDK935lk6kFE3Hs4AvTK2Bl5nhiR25DQrsBH9K9YYMm8BcBQh1bYfXOfFDzcNI85BW9t43A-4zWN7KXGWcduxag95cH57IbyXWKEyfC5ikhZmMiCeBR-wHYqkJqX17A-UBxOTwQn0ZqAPp8iyzwzq8oPddiEaUo4tBr3c7ZjT76rKVCd8V35_T5vIXKeaRhEVTpn5qJ8HV1-pp61oGPlOOC6SpmJmw2tiYIC5iIpvQmTHEbkJxMJtsTqHS-EtcNm6662z3aOleT4jSH-8BxLQi5w39J949zbu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBYExlX7tvz2CLvzJ6UoGd6uBovcXg-HmP3M72-uzlrvPPF3RP5AwrWwqYXZXDzID5abk4qMicCvMpjPD0Smpw9SwfctVY7csp9QpNZNMwsj61fIMa7R1lK5Wno0e77xhtVrSZmgOvUfvO830tMBnal0wwR3TKr1FF9dZWvfuSF-GJG0nFF9D1jZ_6cZ3l0ImOpJepD5z9DyW9tZil721wEyy7vwo52WxyIdJpaaQuR8sBO_HiDJzn7W8L7cvcudhCoxJVpIPTlIB-Sz1AFEKzI96BWj0CUdJhV2MlXOokt9MgXPjQ5ZfYR8iojscC__wA-L0m5syYUNUwbo8V_Xpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب ۷۸ تجمع مردم تهرانسر
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/436292" target="_blank">📅 03:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436291">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDLtonLRKug_HhJ0FKyRNApMefGVtUXaxOUWifwUsiFhiS9B3oZJ1zU6-D5gbnkbD9I3WYxZMdh0MboLrztcFHldTZgwCoC7QNopy-MKRDbWBZjO7V4vnz7UYUqwQPKCNvSk0Md0uMAepru_7oW2lnQZmgts0WT1X72sVh__2tXaO4llKrpNb6PHCifd6EV9HDVdu4O6NKMkNIFAHLDPOtqAD6wI-aFyGdP6wusMQjKtblOJ8todjMC1P6JMfZlHCdBDRg2ucREU0uxg_YZm3jCkseLH3rCD8YJBN6bLeR80UUEPTEqS4XxHVd-NUped8vnbLzVtUHhbNu9puMJIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجبی دوانی: خلق اثر در خیابان، نمونه‌ای عینی از بعثت هنرمندان است
🔹
محمدعلی رجبی دوانی، پژوهشگر حوزه فلسفه هنر در گفتگو با فارس: ما امروز در مسیر اتفاق بزرگی هستیم که به واسطه خود مردم محقق شده است. بعثتی رخ داده است و به پیشگویی رهبر شهید ما مردم ظهور کرده‌اند.
🔹
هنرمند به ‌واسطه اثر هنری خود می‌تواند این حرکت و جوشش عظیم را بر قلب‌هایی که هنوز فتوحی پیدا نکرده‌اند، بتاباند و این قلب‌ها را هم دچار خطور و بازگشایی کند.
🔹
تصور می‌کنم بیان حقیقت به‌واسطه قلم هنرمند و یا با هر وسیله دیگری که بتوانیم آن را زبان هنر بنامیم، خصلتی تاریخی و فراتاریخی پیدا می‌کند؛ چرا که زبان هنر، زبانی در تاریخ و در عین‌حال، فراتر از تاریخ است.
🔗
ادامه گفت‌وگو را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/436291" target="_blank">📅 03:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
آسیب‌دیدن کابل‌های فیبرنوری در تنگهٔ هرمز، چه تاثیری بر روی اینترنت جهانی خواهد گذاشت؟  @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/436290" target="_blank">📅 02:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5e95c34e.mp4?token=O1o6Adv_OpvGjF8SlJvy0k1syz8trIPsnCor-DhdG7z2MI42bLZm9NavJoHSrM91nADLBMRR4InViHXVsuvEdba2lodDOqjbMkgI7skFWy1Btsw9nAQAHhdPduDEvawrptglcV6FP0IWCOxMpfOHeTVz13MRYi4AwVbqlNCmeuwdTBz5dWhGLxryIUnzcEYBv6ScsG2WDSf3nLVlDteFQansLFzk9XUwPH9hFyKufNpSXrKayFOOme7CIPR6W0XwuFVpKxUKMCMWiEXdR3kb05nyf7ZK4mXWdFTiGCbVRMp0t5omfxtjAMzO9fpWp6druPs3A_68xPjiZ_Q-_taPNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5e95c34e.mp4?token=O1o6Adv_OpvGjF8SlJvy0k1syz8trIPsnCor-DhdG7z2MI42bLZm9NavJoHSrM91nADLBMRR4InViHXVsuvEdba2lodDOqjbMkgI7skFWy1Btsw9nAQAHhdPduDEvawrptglcV6FP0IWCOxMpfOHeTVz13MRYi4AwVbqlNCmeuwdTBz5dWhGLxryIUnzcEYBv6ScsG2WDSf3nLVlDteFQansLFzk9XUwPH9hFyKufNpSXrKayFOOme7CIPR6W0XwuFVpKxUKMCMWiEXdR3kb05nyf7ZK4mXWdFTiGCbVRMp0t5omfxtjAMzO9fpWp6druPs3A_68xPjiZ_Q-_taPNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ مهدی رسولی به یاد شهید آوینی در کنار دانشگاه تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/436289" target="_blank">📅 01:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436288">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9XhqJ61MepjagxJisU85BpBCHa98YK01V9_DGKxwK_s7In5WPpKfrrLRrCLcjtvXgUqPTRySBUXb0paDhmAPSETK6WZ1K6Ha9K0XuqvwMcNZv6k-cWAzRWw9d5JYChpSrQ2H35N3fPY7rWv0Hg_XGamOWlQKNO0CZfQRKdm6eDRjn785OLdWe6VrRBSE5XiMyMrSmqTIgSKz8Ai7RGsa03yzTmSZMxCG5kSWK9SVwB5c8mSB6gVDeqCw7HVlU8mrEU-XLe_gkz5C4h9is-xwnnTexBIg-Z_am8uagzp_wUQTslUBTwlWNHdYGroSl3TKilcTGaMbWRzulJCVry-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام سردار قاآنی درپی شهادت فرمانده گردان‌های القسام
🔹
ترور خائنانهٔ فرمانده بزرگ و مجاهد، عزالدین الحداد از سوی صهیونیست‌های بزدل، زنده‌بودن مقاومت را به‌ویژه در قلب غزهٔ قهرمان نشان داد.
🔹
این خون‌های پاک الهام‌بخش مجاهدان جوان فلسطینی تا تحقق آزادسازی قدس شریف و نابودی رژیم اشغالگر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/436288" target="_blank">📅 01:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21042a8574.mp4?token=gny_s4pRgR_nCmqSzOCBNTPGvjL9RIqHCJrKpBMMnafNlYpj5BOaY2vHB6oRW4fKyidlzCsAfXAdwO7xgaylEv3CASmapPnphU1XRBP8MAkPx9szwubeQmTPqzASedbV_h4OyXnRDn-rf1rPCyphQ-VsSAvPAHXmNeNZxnHkjH56RqF9T5ezdAOFYsKoFvziM3rcu8rNXUKuO2t6UrFkFziFJEIDwTptk7zuIkF_cAQkwVunGYXqp9TAtRY7P4TK17OqEihbhd6xA7BfvO94OA0AKAACmc418KRuBR27lf8hxsK6HukXfV-qME5drjHwz-abqvS1c9dFlLJ3cwm-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21042a8574.mp4?token=gny_s4pRgR_nCmqSzOCBNTPGvjL9RIqHCJrKpBMMnafNlYpj5BOaY2vHB6oRW4fKyidlzCsAfXAdwO7xgaylEv3CASmapPnphU1XRBP8MAkPx9szwubeQmTPqzASedbV_h4OyXnRDn-rf1rPCyphQ-VsSAvPAHXmNeNZxnHkjH56RqF9T5ezdAOFYsKoFvziM3rcu8rNXUKuO2t6UrFkFziFJEIDwTptk7zuIkF_cAQkwVunGYXqp9TAtRY7P4TK17OqEihbhd6xA7BfvO94OA0AKAACmc418KRuBR27lf8hxsK6HukXfV-qME5drjHwz-abqvS1c9dFlLJ3cwm-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطریانفر، فعال سیاسی اصلاح‌طلب: وقتی رهبر شهید، ۱۸ و ۱۹ دی را کودتا دانستند ما آن را باور نکردیم اما بعد از شهادت رهبر انقلاب تازه به حرف ایشان رسیدیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/436287" target="_blank">📅 00:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الجزیره از حمله هوایی ارتش رژیم صهیونیستی به حومه شهر راشیا الفخار در جنوب لبنان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/436286" target="_blank">📅 00:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io0_NaIIw_esONcbMj7O2lczRq-MqZHsbxYGq6WMmXqGkt4xnGLPLeZ3Lu1WCKcd-NMAsZ8PTQZIKUsCwy8tVeckBtjWaOWysuUxNYXaBDVEvDDzBOaGB9V_SYOP5dgdhuFyOKXzocktD7I9MmvY5wEeNWymWTYQlfRC6CfUWw2epsPHhB7SJFQwv533-f1bbrpvrs4YgtYTkTwMCVJ7tKRDUdmWnWyr7dUcg1rE109ffj4iGWeL6DxwPzFqu-XDBq215VuUhiFj2YQ5s5tE19lG0o6hDw1ehI2katQQ1GQSALORK7EI-SCqNWGTISwnnmgkS0YK7Ku26-GfDGokjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه‌کارهٔ جهنم!
🔹
شخصی از ستم و بیداد حاکم شیراز، که از خویشاوندان اعتمادالدوله بود، به تنگ آمد و برای دادخواهی راهی پایتخت شد تا شکایت خود را نزد اعتمادالدوله ببرد.
🔹
وقتی آنجا رفت، از ظلم حاکم شیراز نالید و درخواست تظلم‌خواهی کرد. اعتمادالدوله که ظاهراً قصد داشت به نوعی از سر باز کند و مچ فامیلش باز نشود، به او گفت: «اگر از حاکم شیراز ناراضی هستی، به اصفهان برو و آنجا سکونت کن.»
🔹
مرد گفت: «نمی‌توانم، چون حاکم اصفهان برادرزاده شماست.»
🔹
وزیر گفت: «پس به کرمان برو.» مرد پاسخ داد: «آنجا هم نمی‌شود، زیرا حاکم کرمان داماد شماست.»
🔹
وزیر کمی فکر کرد و گفت: «بسیار خوب، به تبریز برو.»
🔹
مرد با ناامیدی گفت: «حاکم تبریز هم که پسرخاله جناب‌عالی است!»
🔹
اعتمادالدوله که از این همه اطلاعات و پافشاری مرد کلافه شده بود، با عصبانیت فریاد زد: «اصلاً با این اوصاف، بلند شو و به جهنم برو!»
🔹
مرد با خونسردی پاسخ داد:‌ «ای قربان، به آنجا هم نمی‌توانم بروم؛ چون آنجا هم پدر مرحوم شما پادشاهی می‌کند و مشغول حکم‌رانی است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/436284" target="_blank">📅 00:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da2f1f057d.mp4?token=F6cXbuMM8sBW1dZydB17ZtwxtIMU-G8v86_8zmThfeWTXnHWRbjX1yeLFyIz_5B9lo8Ol_RZZETEs2qfkudw65RMeLHkXOsEmEzkgCQUxW61DevYF_BiD3g1Duq0p89F93YOtcYlNPystRdnrtHEUiiZPKpCHWSeppM87uWKD8kb-yv7_33wROJ4VxpXJCVeiJU6fMOYJK_wFlzjilexibZC34uUekMrxSYB5Zx5O8GmmzO-wKhKe7SKwb8RpvfNYue9-8mgE7ZOVEmV-PPFOn9aCIzZI528iK7wBsaR9_z8I1arndr_Zn3Hn8_baM6Pg-RADLy8hKAmJ1r3YcpVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da2f1f057d.mp4?token=F6cXbuMM8sBW1dZydB17ZtwxtIMU-G8v86_8zmThfeWTXnHWRbjX1yeLFyIz_5B9lo8Ol_RZZETEs2qfkudw65RMeLHkXOsEmEzkgCQUxW61DevYF_BiD3g1Duq0p89F93YOtcYlNPystRdnrtHEUiiZPKpCHWSeppM87uWKD8kb-yv7_33wROJ4VxpXJCVeiJU6fMOYJK_wFlzjilexibZC34uUekMrxSYB5Zx5O8GmmzO-wKhKe7SKwb8RpvfNYue9-8mgE7ZOVEmV-PPFOn9aCIzZI528iK7wBsaR9_z8I1arndr_Zn3Hn8_baM6Pg-RADLy8hKAmJ1r3YcpVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: تامین پایدار کالای اساسی و جلوگیری از گران‌فروشی راهبرد اصلی دولت است.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/436283" target="_blank">📅 00:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای عربستان دربارهٔ حمله پهپادی از عراق
🔹
وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شدند.
🔹
عربستان گفته حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/436282" target="_blank">📅 00:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSus3I9vJLCzwOLf-6E18PKFWjhmkVCEheLIUZqsYwm3rBCAkcrnZun4xp2ffSvKPoG736iOiDuzkVuqkK9jJ37hiS33EFUo-rsz0zFniMfa_Bn1yWKfurIhPvcKNosviC0RiCbLRAuPr7YU25uvkR3jWs-inlHoY4rjd3lRYVl68RxDDbvKIm6MpyKb6wzURAtPISDg7YS3E9nmSrboKnCwL7Tyh6_Xq0MbyAy3EK3oItt6rJszrv-8YHjpTIBY8EkY1vMRuR5q57YORhOnhpB-O_-8-rVXEa0Eu88vLJhmte49XDnWICMiakB7AimqZwQIlqGlORc_0w3y-EBz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoRhjW8sd0Aqp9r3Mv3RRBRNIW0CZf0N-e1OyrJh8aJNuPFpWYWmlYwfPmd4Z9Gzg44kCvqnZBKLZJ_qcAb2Y9dKGmnUCxhvN-mFgaa99GHQd3QD-GmDUQiT-xy26rtTgPFuuvEv6zM2jdji0oyXosvmN5OkdZlyDhgp9sQjHrYEWF3r1v4QvPuoFa7DIPBBQdNrwxMETFLrlX_0aJlZtwU6Ah-1F2V6wLMDUVjh64B1SGWlHBfSKVjIXM_upRARg7lnKQfJE5wn0zP1ybXJfXvjiSzOs_HPi3cNaZ0zIimhNLS5WLuN6aMmDtDW8QxAI5E-tms_VbigoH5DG94Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3JenI_MKu-nvULSagchAiLtHd6gXhaW98cJZYK95Doy3PEsnBl1h9hMC4E3zPm4mYGwWQPEUNDlI8qU0RaNa0WdQAhmivbr1deF0h6VjMTrqH2m8GDQ9Bn-5GD_qX32QfcZuaEStf7sQhiEiB2MIULZ0jEMxnNRPIDZR9LSE1lJU5OwyOdB-x_lvvvrx7ouRZZnRnA_2yVa_QlETuu2V4bfHvO3TDw8VjPsvZjaUDePIy3cUvYdA1pDrnFPUNma6tFDEYC90zeDfRYd2AUvDLREsH519SyYlgY-PvhaH4JZA_2_3wD1LIiXYpQTFEdEeRv5Qmx_q71YnSi5zf1RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqkP0k_8ngL4lfJitB-bQsfu3p1gmZTt4MqSeuphtyBXPfwjDOSIpB3UUzYgTLwuyKhtKAdBnoVAjeRFuNxucFg5jOWKa_BapSQ8DPuCyZ2SgGMeNHo1nAAuCtV8Rk0fe0p0fi-kjunWTIAELegqfTDL_Ib7osF8S9BZY-NFTGraBO360IIuHkca0KAGOZ368KZ39Axf_gLXRXWS2ic82GHkKyMfuttd0hKLDYpSzm1SR2PgJLmL-YlGBrkb-H_piuyCCdbM0wdFJuh7rLq9eMFsw6gJPxudTf8KlPJ6YIrM-g4ourTN_vvCG_ECDfJup_UFy1v094Tm3Twaq8Ri1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXYL3ix1h8sxxOzWWMFfKsDObmpRTRA6Jllg7i7OpP7p0t1EET1Z8VqSKqaZri_VREeupA6_PxkMaBK4nlasQ1NkyPp2bBAZ_xf9bymRmz_FiI16q8-_9bOAS65bsIe4520kSZMFFSFrv_5pe2Z8cTeQQBmNN1jstUlNOlyGDZEPiwwnOyOUh5Aka51XjDqYy73_WNvHWlVhMPB3chZ31K4cnQvVICgY1DgBRXcFy1zPPDTWllTMJ-3STlWbdT4mU9Dw13GUsVG93gKCwUDDIz32V2maJoDowm8oBapL5iQ45rnCOmcXS1tlR1srVwqbWr3JcXo9tHMeKPL4d1sVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC4c7LJjBpbxsg2cXUfhptHxTf56NYJuMYz0_7XxegxvVumrtPGHKC9_jfaUnfvY9WC94PbXvHdPAqqGZG_XDcrC11RVTjDx7rCvhV137i6T-YJJNSalBAIuImvaK1BxJv-VqfGDR7z7HSwuTGFVtX7eQgM-NsX9GzlRyotTWy5jTQ214Xw10fUVd9bWqaYFMAQ3g-Pmmxf3jUNDlY2TBKonxklrl_-iVQ8eK2M6RMG6xT6epmqNVxoVO7QpKsF3-cGC2BuJBHvrUohkBNr7r9Sw0j3JsPxHTAhntO6F5XWrY3FX1n1cEfXhCwhCaMOJ4R0slN4M44AaQm1hP6lS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liAjq4-eL5YRSwewL4Iro6MkuPRu-WWTSMz1vfJep2R32kzX2i8GvHj5H9K42ymceR70fbw2NTJZF8TQV9DMzkt5oM4SjYPUf4uXvh50m9SeY_nuj1KjVDXytC6UjLuCri4220K0t2eho1cSwW21akgPe71OIDfEE6oRa7vz6Y2dw_h-o5c7nY6nj46AnM4O3guKqTcAts5hFJooefGXzadp7lQILDlAhiOx2B0gzFoSTooPt4qb_HQeeSSgG7-5E8EJArZ2Zp5z8SJsTAfkWxVnaxSCfo7qPy_CcUnDQrj7-FCtcC3Rv26cZwMQwcTy6PdvXlgAZgQUQoW7vSV37g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موسم برداشت گل‌محمدی در خراسان شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/436273" target="_blank">📅 23:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa34ad2374.mp4?token=o1b9I_6mPe8Oy1YObnKl8sexmYcK7SGkkBbuj-fW_TrGOBPI-yFY5qSoYe1rDi_-HwIkDqZMKpfIopPLu_msNLywfhoKiR-4bd2SAJsrOL2V3WVx7ef3EDDEnUQO22_T7izrhpWwQE4OtjX7ZJpGvgqvW6N85Q9PkOj0kPVmhuwBf0r_Uxx-5BR3GDvGJ9Pxg5UOF78McXUwCaJaLmtUOsLZ3OK72Nnp6I3G4wJHuxmhBqc5p7XMNpfIgNI5eFnAlPNy9grC5qzZTQu_eyLs4Ry3e_Jnch_HIYWI1Tm9bXwvTs1qJxNavw8eIjDY8cqngF52ZvVeiRnvk0TblE9GIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa34ad2374.mp4?token=o1b9I_6mPe8Oy1YObnKl8sexmYcK7SGkkBbuj-fW_TrGOBPI-yFY5qSoYe1rDi_-HwIkDqZMKpfIopPLu_msNLywfhoKiR-4bd2SAJsrOL2V3WVx7ef3EDDEnUQO22_T7izrhpWwQE4OtjX7ZJpGvgqvW6N85Q9PkOj0kPVmhuwBf0r_Uxx-5BR3GDvGJ9Pxg5UOF78McXUwCaJaLmtUOsLZ3OK72Nnp6I3G4wJHuxmhBqc5p7XMNpfIgNI5eFnAlPNy9grC5qzZTQu_eyLs4Ry3e_Jnch_HIYWI1Tm9bXwvTs1qJxNavw8eIjDY8cqngF52ZvVeiRnvk0TblE9GIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین سرود ملی در موج ۷۸ تجمع مردم لردگان چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/436272" target="_blank">📅 23:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60755d3540.mp4?token=WYImuCo4TRVyt1SJnQlZFPvZom3TD7GIXQDt0pVUThMusd24qeQhlYH9Js9z8vbwlwUzfszSuinG-bjYE63OsDh4rgSOstA3NvgsqN3VtnrJvFpA0gCPsM-RPN9xvIioP012_Plcoyn46umUiNgkAd1Gku_sRIfg72CSH3NXv1mN45bM7lRuPJylBuhO2kMa__hSh_xCeljG3SMqdTwaArcnYZi3u7V6lBDQQ54zZzKC3ko1gONBFgycTcEfdDMTU9qqAQdAQ8V2I5AKi9d6Oc7bnBiwbLMFAHKS7_vFvqeoMq1LlCD8x8Gssv6s70BVae1B8l96eT4UQS8tY4GxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60755d3540.mp4?token=WYImuCo4TRVyt1SJnQlZFPvZom3TD7GIXQDt0pVUThMusd24qeQhlYH9Js9z8vbwlwUzfszSuinG-bjYE63OsDh4rgSOstA3NvgsqN3VtnrJvFpA0gCPsM-RPN9xvIioP012_Plcoyn46umUiNgkAd1Gku_sRIfg72CSH3NXv1mN45bM7lRuPJylBuhO2kMa__hSh_xCeljG3SMqdTwaArcnYZi3u7V6lBDQQ54zZzKC3ko1gONBFgycTcEfdDMTU9qqAQdAQ8V2I5AKi9d6Oc7bnBiwbLMFAHKS7_vFvqeoMq1LlCD8x8Gssv6s70BVae1B8l96eT4UQS8tY4GxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام پهپاد آمریکایی در یمن
🔹
برخی منابع از انهدام یک پهپاد MQ9 ارتش آمریکا در آسمان استان مارب به دست نیروهای مسلح یمن خبر می‌دهند‌.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/436271" target="_blank">📅 23:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dee5d0d6c.mp4?token=lSXbJfoYnt-JX5KVmUzky_NLoSgyHUE3pDKL-St2NcsqqhB0W8mH3f2zaYdN9BRDJAP8HWYyU_rqdwB21kIeNz9MeHkSwkUfpmura4rxP_o1uxCep-8ZppS2P25NBgIAUcjf5mUVhZ-XM5ibeJwwZgLnv37yCiU77pHCPrtSNQJ-hJ1TlxitNoj_tiRhHgUDDIVXRRnI45WrY1YmGR9cQcnEDXGkPm1E0hkNUM2eDWn6XpIcsT99m1OV4IaCXyodOgHYSh071JhPoQB4uV1s6gRCGF5x9kug_zfF9E5ppo_tKdL4xHvXhsjMb4he2HyU9JPl12vjpfiQw-aowB9qOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dee5d0d6c.mp4?token=lSXbJfoYnt-JX5KVmUzky_NLoSgyHUE3pDKL-St2NcsqqhB0W8mH3f2zaYdN9BRDJAP8HWYyU_rqdwB21kIeNz9MeHkSwkUfpmura4rxP_o1uxCep-8ZppS2P25NBgIAUcjf5mUVhZ-XM5ibeJwwZgLnv37yCiU77pHCPrtSNQJ-hJ1TlxitNoj_tiRhHgUDDIVXRRnI45WrY1YmGR9cQcnEDXGkPm1E0hkNUM2eDWn6XpIcsT99m1OV4IaCXyodOgHYSh071JhPoQB4uV1s6gRCGF5x9kug_zfF9E5ppo_tKdL4xHvXhsjMb4he2HyU9JPl12vjpfiQw-aowB9qOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رقص پرچم ایران در ۷۸ شب اقتدار در میدان سلیمانی کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/436270" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b69b398b.mp4?token=Jo882VMW_s9WbkNTqrh0o73bbmqxG_-jary7LWbqoyabFgVUzHW--ATaljhCA2HuSy3lfK5V0F5wI6iVcj7gXSdspitGNfrE4kFFHJdyd_Jwt2FGpCXj6WI6uDthGMk4BUV1TgvtaL1QJPNQ-gEJMBPEEO-5BlalNfXTgov9hPJanhfdoGK-W6vRtGRzdBe50DBikWKinjcKCnxzb5ddk7vmLZJqSMRgLLm1bdiI3LP9IJaynD2fM0ZJIHnjsOYXEn2ASM1-nvBe7RGCkriX4cMeWU6Ixb6ceIs8zOZLQ6pnHdlpt2Q6aIsn-8K-0xlL3WmcQu1sKwNrb0JaRiJ-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b69b398b.mp4?token=Jo882VMW_s9WbkNTqrh0o73bbmqxG_-jary7LWbqoyabFgVUzHW--ATaljhCA2HuSy3lfK5V0F5wI6iVcj7gXSdspitGNfrE4kFFHJdyd_Jwt2FGpCXj6WI6uDthGMk4BUV1TgvtaL1QJPNQ-gEJMBPEEO-5BlalNfXTgov9hPJanhfdoGK-W6vRtGRzdBe50DBikWKinjcKCnxzb5ddk7vmLZJqSMRgLLm1bdiI3LP9IJaynD2fM0ZJIHnjsOYXEn2ASM1-nvBe7RGCkriX4cMeWU6Ixb6ceIs8zOZLQ6pnHdlpt2Q6aIsn-8K-0xlL3WmcQu1sKwNrb0JaRiJ-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: وقتی آمریکا می‌گوید ایران نباید دانش‌ هسته‌ای داشته باشد باید به این موضوع مشکوک شویم
🔹
این شک به‌وجود می‌آید که نکند این‌ها در چند سال آینده کاری می‌خواهند علیه ایران انجام دهند.
🔹
ممکن است بعد از این بگویند ماجرای هسته‌ای حل شد، حالا برد موشک‌هایتان…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/436269" target="_blank">📅 23:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b4ca0bb.mp4?token=UhW7XkUZ7iQ1RvrpLMu0la3fXYlRN9Z5al502IvxTJijDmy9gOOJ-qGnrISbxdSmoWAb5KxUJIA7pIf2LEwYMp0fS8O48WfW_uieKxWiJm3HHE8f2j6KjcqWYK72zSwpAshaAQfzdUtla-hApvBF6sRQpurNXYSr74iM9012LzsebJl0wL2UeWOi_SVWX7nzQ67egnbIemSNJlidBEqV3cRYRr4jMM4MLBHKRDGI-tUZtmZlOme70noA-m3h3apRoD07JljPOUBRddntfvkiw2zWeutfxOXg1eqK0DAnVCqTz5EfCMf4K9JxHlP1uaMJ18iAi2lcEMoXiEo-y7v3YZ0oN66Crz9aqpOKIzkNSWhAmuVbm36qywt6XSMGlFgZQE1PGO8LWf-AliuEIVNsv9DydB0YtOFq9vs78Czba373y5FnxWuiuC62H2rWLl2iEBK9qYuY2qxac07KjgIRnB7YRdolZZLQkoTZ7FsjhOJB4U18TrboSTU-9-b6NFZpWkJseMZFL7smxneVXn0-7xgx1ZfVgdVXNiIXxOHUQlPUVLDURT_ZwANDfVQo8xa9YBzJe1_FoUfLbpb9sJXYbRPnvOH6C_6LD6dPlK00hai97RDDKK90V-6kxW8LaDUKC0py3tf5AJYTAyGh7hOtIkHkVdUr6ufztiS_AGCGVwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b4ca0bb.mp4?token=UhW7XkUZ7iQ1RvrpLMu0la3fXYlRN9Z5al502IvxTJijDmy9gOOJ-qGnrISbxdSmoWAb5KxUJIA7pIf2LEwYMp0fS8O48WfW_uieKxWiJm3HHE8f2j6KjcqWYK72zSwpAshaAQfzdUtla-hApvBF6sRQpurNXYSr74iM9012LzsebJl0wL2UeWOi_SVWX7nzQ67egnbIemSNJlidBEqV3cRYRr4jMM4MLBHKRDGI-tUZtmZlOme70noA-m3h3apRoD07JljPOUBRddntfvkiw2zWeutfxOXg1eqK0DAnVCqTz5EfCMf4K9JxHlP1uaMJ18iAi2lcEMoXiEo-y7v3YZ0oN66Crz9aqpOKIzkNSWhAmuVbm36qywt6XSMGlFgZQE1PGO8LWf-AliuEIVNsv9DydB0YtOFq9vs78Czba373y5FnxWuiuC62H2rWLl2iEBK9qYuY2qxac07KjgIRnB7YRdolZZLQkoTZ7FsjhOJB4U18TrboSTU-9-b6NFZpWkJseMZFL7smxneVXn0-7xgx1ZfVgdVXNiIXxOHUQlPUVLDURT_ZwANDfVQo8xa9YBzJe1_FoUfLbpb9sJXYbRPnvOH6C_6LD6dPlK00hai97RDDKK90V-6kxW8LaDUKC0py3tf5AJYTAyGh7hOtIkHkVdUr6ufztiS_AGCGVwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها امشب با شعار اقتصادی به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/436267" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g61E_WpTFgNyfHUoj2lkYAKAvO5_3d7nSOKaxNGw3rlPPc52WTRzgn1gyflZULH8C1jajEJvKRFO7aIHGnQn3JnVHRdbtJ4XYgd3hyshWE5TxtEh473o_lrKeL0WRgRRGLuGwhB0tFST5oMnm4_uldemTw5Bw4O-vHY8l4ElSr1v4ewtCSEU3GqxiAAjAsG8tLdn11hbSkrayX1Ra-mpJ98xFkGT3TojS-ZL5PfU2E_hYjyjW36nrbGnCnz4jiYj9vLlQp6b0vAl1BXBFh-tvqM19FtMAIfJT62GLp1flEfL3Td0Yz3CUy3if9fxPEf_o2nIs5FLKruAEWoZK8nVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینه‌‌ انتخابی دولت برای مدیریت بنزین در پساجنگ
🔹
درپی آسیب به زیرساخت‌های نفتی کشور، افزایش مصرف با لغو دورکاری‌ها و اندکی اختلال در مسیر واردات، دولت مجبور به گرفتن تصمیمی برای مدیریت مصرف بنزین در کشور است.
در چنین شرایطی دولت ۲ گزینه اصلی را روی میز دارد:
🔹
گزینه اول: افزایش قیمت نرخ سوم بنزین موسوم به نرخ جایگاه (براساس مصوبه سال قبل)
🔹
گزینه دوم: کاهش سهمیه‌ها بدون تغییر قیمت که طیفی از بدنه دولت آن را دنبال می‌کنند.
🔹
طبق موضع رسمی دولت و گفته‌های معاون اول رئیس‌جمهور دولت قصدی برای افزایش قیمت بنزین به‌عنوان راهکار اولیه ندارد.
🔹
دولت درحال طراحی بسته‌ای برای مدیریت مصرف بنزین است که در اولویت آن، افزایش قیمت قرار ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/436266" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
ستاد استهلال دفتر مقام معظم رهبری فردا دوشنبه ۲۸ اردیبهشت را اول ماه ذی‌الحجه اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/436265" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
۷۸ شب است که قرارهای شبانهٔ مردم شهرکرد ورق می‌خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/436264" target="_blank">📅 23:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
۲ جنگنده آمریکایی یک‌دیگر را سرنگون کردند
🔹
۲ جنگنده اف ۱۸ نیروی دریایی آمریکا در جریان یک نمایش هوایی در ایالت آیداهو، در هوا با یکدیگر برخورد کردند.
🔹
هر ۴ خلبان موفق به خروج اضطراری شدند، اما هر ۲ جنگنده سقوط کردند و منفجر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/436263" target="_blank">📅 22:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎥
محسن رضایی: بسیاری از پژوهشگران عربی می‌گویند ابوظبی برای عربستان است
🔹
اگر امارات در جبهه صهیونیست‌هاست، پس قبول دارد که نقشه غرب آسیا باید تغییر کند. آیا بن‌زاید می‌پذیرد که ابوظبی جزو عربستان شود؟ @Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/436260" target="_blank">📅 22:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
۳ نفتکش ایرانی دیگر محاصره آمریکا را شکستند
🔹
تنکرترکرز: ۳ نفتکش ایرانی با ۳ ترفند متفاوت خط محاصره آمریکا را شکسته‌اند.
🔹
یکی موقعیت‌یاب خودکار خود را خاموش کرده، دیگری پرچم روسیه برافراشته و سومی از خط ساحلی عمان استفاده کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/436259" target="_blank">📅 22:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a645ff3278.mp4?token=Hr_7B7AYm6froDILoxycQIqMYELXPYpZXzyTBa3c0B7S_JFmwokvPpKZOkr4tte83r0EvmMXz9kWUkeAorfIJu3NKOcVQq_WsZYOk48N_FBPBYJofE6qOKoNjt9xaJlDhWVuNK9tWuWnfgEW9wwtAF5ewzgl8oN7MRBoQ89jFyJ3GTPqkfQa0YX3pzxs1Fo8F_Q5FIDkGa9acLUouPyi-XR4cpgiZEN0Dt8JXtvAA3N4K52gGYZQjZTT6uodtvhchcwCjFdyAITFUOzeME5GIJkbIPNB2UnAKTsOnb66Grv01kx4Yno1d73b1Jx51dTkyrNgWidHRKWmDG6QCnPdcnJ8urmnekkY6Pwi2h_oje1PMkYp39ulGTnqHGlIUdk4MGz0Fsuqh3FLE4zYKMHpQkAhc85bEPcaExySvgqWg8qyj98Vt2_imofVgkIJ6LmAiD8Cg7iQnCtKxs077fkcXU038wYWwdLa1wF7-9NfdNJay9UNs4B3cBNkOhzMGTM4es67nKZYP9n7AEDTJ22ht7BObtXIFPz63t3h3nuARILTuEgFalk7inqvMvc6mrWqHOkZuhn_fqM-ib4ocex6WKS208APvwvYECzYFhc1pwNzseqFryGD8OcJ4PtgfF9HE-s1lsDLlJyRiZ0Fh-KiJJQSgt4vFtt6YTubcMxuJ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a645ff3278.mp4?token=Hr_7B7AYm6froDILoxycQIqMYELXPYpZXzyTBa3c0B7S_JFmwokvPpKZOkr4tte83r0EvmMXz9kWUkeAorfIJu3NKOcVQq_WsZYOk48N_FBPBYJofE6qOKoNjt9xaJlDhWVuNK9tWuWnfgEW9wwtAF5ewzgl8oN7MRBoQ89jFyJ3GTPqkfQa0YX3pzxs1Fo8F_Q5FIDkGa9acLUouPyi-XR4cpgiZEN0Dt8JXtvAA3N4K52gGYZQjZTT6uodtvhchcwCjFdyAITFUOzeME5GIJkbIPNB2UnAKTsOnb66Grv01kx4Yno1d73b1Jx51dTkyrNgWidHRKWmDG6QCnPdcnJ8urmnekkY6Pwi2h_oje1PMkYp39ulGTnqHGlIUdk4MGz0Fsuqh3FLE4zYKMHpQkAhc85bEPcaExySvgqWg8qyj98Vt2_imofVgkIJ6LmAiD8Cg7iQnCtKxs077fkcXU038wYWwdLa1wF7-9NfdNJay9UNs4B3cBNkOhzMGTM4es67nKZYP9n7AEDTJ22ht7BObtXIFPz63t3h3nuARILTuEgFalk7inqvMvc6mrWqHOkZuhn_fqM-ib4ocex6WKS208APvwvYECzYFhc1pwNzseqFryGD8OcJ4PtgfF9HE-s1lsDLlJyRiZ0Fh-KiJJQSgt4vFtt6YTubcMxuJ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: محاصرهٔ دریایی آمریکا را می‌شکنیم
🔹
صبر ما حدی دارد و نیروهای مسلح درحال آماده‌کردن خودش است. @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/436258" target="_blank">📅 22:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4a9d33f9.mp4?token=k7SczZJVuVN8QNWhlQitoXHOtN9CFrXYy4XzfXinPbjQStQIJuA3Rj7uONkK4IvjJ9-N964B2vGMtjbXNCwRaqbsukZz6Xe98crVDEXSXDdl1XpJy98JTzQTwCd-mc0rfxhId1GWhyYOUnmSf6vICYYmrD-GW_KYPPgAG-N_vx4rBZHTmRLzpWFfUUaphOiNwZE-63J-kMoLP6dMRFwiqdtxaAlajZ9dZVM3FygSDZiXsYn0OVYh0lLyRFNbakGazbGBXx7OOB9rNQXiXNONsFeeVy0wSUm8P7moCoKHBqFXSm3AkOw_6VYqY2i936KbU-NkBw4cfxjWDhO5FLop9Z57P3y_-Ldp77rsj9gs62Ry6EnbiuGQaXdGD6_jC9eIIXZrdBy-nxalVFsBv4XJ0oN2dmE6bTgO9-b1AaeYkDCGdkbed_0-dJcUB_156BQ-E6ELBktlSkFToU566BAAANoHHkVVHyAts-I_2zUMa2SoewWimOhepQ__WlL6oFbqTfY5IiJD-57o6rbJtDPn7987okpbQQMzQhJ2wqshxw456eSTui60CJ1qsEh8KmLGaOpgRTEmbyE7Sn8M8ReC5_A5QKO6mNJUk3mXouJAh0aewQ19Gonekc0Q_ZdRhJAli0OP2538zPPNitaq3mficmV7AG-BhB3oj6n7brBtAhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4a9d33f9.mp4?token=k7SczZJVuVN8QNWhlQitoXHOtN9CFrXYy4XzfXinPbjQStQIJuA3Rj7uONkK4IvjJ9-N964B2vGMtjbXNCwRaqbsukZz6Xe98crVDEXSXDdl1XpJy98JTzQTwCd-mc0rfxhId1GWhyYOUnmSf6vICYYmrD-GW_KYPPgAG-N_vx4rBZHTmRLzpWFfUUaphOiNwZE-63J-kMoLP6dMRFwiqdtxaAlajZ9dZVM3FygSDZiXsYn0OVYh0lLyRFNbakGazbGBXx7OOB9rNQXiXNONsFeeVy0wSUm8P7moCoKHBqFXSm3AkOw_6VYqY2i936KbU-NkBw4cfxjWDhO5FLop9Z57P3y_-Ldp77rsj9gs62Ry6EnbiuGQaXdGD6_jC9eIIXZrdBy-nxalVFsBv4XJ0oN2dmE6bTgO9-b1AaeYkDCGdkbed_0-dJcUB_156BQ-E6ELBktlSkFToU566BAAANoHHkVVHyAts-I_2zUMa2SoewWimOhepQ__WlL6oFbqTfY5IiJD-57o6rbJtDPn7987okpbQQMzQhJ2wqshxw456eSTui60CJ1qsEh8KmLGaOpgRTEmbyE7Sn8M8ReC5_A5QKO6mNJUk3mXouJAh0aewQ19Gonekc0Q_ZdRhJAli0OP2538zPPNitaq3mficmV7AG-BhB3oj6n7brBtAhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: یکی از ۳ ناوچهٔ آمریکایی که از سمت عمان وارد تنگهٔ هرمز شده بود بر اثر حملهٔ موشکی ایران آسیب دیده است و آمریکا صدایش را درنمی‌آورد.  @Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/436257" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055b2b9f77.mp4?token=APNZqY60QhAYr1f47ctBWs7MlaqfHrAJnAOyuRqlaqfauDUIQIyXBqeBc-PIPROD40BGUeeKrXsx29q1GEMdsO2cowTefZfbrnt_6cc1_-9TMB_TXcBABalxgjzlNQvkBTDxwmQeskYAGBNb-Lo21wOibLvUPWG3TT1zil_5tVkrjISIXjddk5hGFekyDMCC_VISqnju2KybGNp3Q8sHuJYUQlooBecEm4SiTK1PbE6nq-HNN_GjHzLLBB1cozaXy4nJZ62z7tKCV0lGWrp7V6vguSrsNwPdKNpprdr7Cd3OVD3l8TlJTVwNLgkZaNTI_f4xNJqSuPcOnszdX64ziD6NiEEH489X1cHohs6wovq4nZkQpYdyC-TDfxWXVjbFliw6-nAHzYc-hhkJTcu7v7IubY-oMTDjkYMwIZIgabW95Ouf-4aFop_ZzO9uy5gy5M4LoI_OAgZHwG4VePgJkOg6kCINnmy26Yb-zgs8e4DbLud3UqA0pANFUWxqiKlv1ddtOGJMZzAFEp5cnh-oLbQwf4ulVPr-cY5re9L50na4ziDG2t361MgnV7KI0CZ3oHSkgMnnVKsSjQJjASRsCn7uxyitVp5Dd0SnaZKI_thRxbVqwJIMVjsHcjXiNsF-7cq8CNZDfhN1_QZBtKoL9h-W9bD8h2jArEaNX90ABq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055b2b9f77.mp4?token=APNZqY60QhAYr1f47ctBWs7MlaqfHrAJnAOyuRqlaqfauDUIQIyXBqeBc-PIPROD40BGUeeKrXsx29q1GEMdsO2cowTefZfbrnt_6cc1_-9TMB_TXcBABalxgjzlNQvkBTDxwmQeskYAGBNb-Lo21wOibLvUPWG3TT1zil_5tVkrjISIXjddk5hGFekyDMCC_VISqnju2KybGNp3Q8sHuJYUQlooBecEm4SiTK1PbE6nq-HNN_GjHzLLBB1cozaXy4nJZ62z7tKCV0lGWrp7V6vguSrsNwPdKNpprdr7Cd3OVD3l8TlJTVwNLgkZaNTI_f4xNJqSuPcOnszdX64ziD6NiEEH489X1cHohs6wovq4nZkQpYdyC-TDfxWXVjbFliw6-nAHzYc-hhkJTcu7v7IubY-oMTDjkYMwIZIgabW95Ouf-4aFop_ZzO9uy5gy5M4LoI_OAgZHwG4VePgJkOg6kCINnmy26Yb-zgs8e4DbLud3UqA0pANFUWxqiKlv1ddtOGJMZzAFEp5cnh-oLbQwf4ulVPr-cY5re9L50na4ziDG2t361MgnV7KI0CZ3oHSkgMnnVKsSjQJjASRsCn7uxyitVp5Dd0SnaZKI_thRxbVqwJIMVjsHcjXiNsF-7cq8CNZDfhN1_QZBtKoL9h-W9bD8h2jArEaNX90ABq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم حضور شبانهٔ مردم مراغه در رزمگاه خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/436256" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed901ee5c3.mp4?token=WacjwXDqANpsLg032hJjeiD5ERGeC2s2z-fJszPQ-Qxrd1J5YgeR5pxGqHz7I0yZ--o7kGotD5HYE8cMAuGBEB1bLET7RIYNF4echjuty1X4VMUEkQZ4g3RIqxFXLaCw0oipdTxv-p_SvJKAML7KTkK0kniyM6tw8Hu-FqWGTdaoK96Zgqy1I7g-XmUWiabxcLU3lS6Hd0ie_ry1Ek3aUaiON71hAOMPNm_LC8W_aTiUBcMhXSM-pHrSlCPc_K6-aGCyE-9bTfI9ZipQkrVK5h6_YYWjj0mH_zTvD0u1zNN_BYjxStrI2IAvuSE1SH8qbLLbhGRKAz9seNItn0biMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed901ee5c3.mp4?token=WacjwXDqANpsLg032hJjeiD5ERGeC2s2z-fJszPQ-Qxrd1J5YgeR5pxGqHz7I0yZ--o7kGotD5HYE8cMAuGBEB1bLET7RIYNF4echjuty1X4VMUEkQZ4g3RIqxFXLaCw0oipdTxv-p_SvJKAML7KTkK0kniyM6tw8Hu-FqWGTdaoK96Zgqy1I7g-XmUWiabxcLU3lS6Hd0ie_ry1Ek3aUaiON71hAOMPNm_LC8W_aTiUBcMhXSM-pHrSlCPc_K6-aGCyE-9bTfI9ZipQkrVK5h6_YYWjj0mH_zTvD0u1zNN_BYjxStrI2IAvuSE1SH8qbLLbhGRKAz9seNItn0biMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: یکی از ۳ ناوچهٔ آمریکایی که از سمت عمان وارد تنگهٔ هرمز شده بود بر اثر حملهٔ موشکی ایران آسیب دیده است و آمریکا صدایش را درنمی‌آورد.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/436255" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
چرا باید پای ایران ایستاد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/436254" target="_blank">📅 22:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnR7SBMJ792iWkd6_9xR4jCC5KLhcxOILeXUjUg2Ab3gasqZXLRB4d5tYbjog5Z4dicot5_kgOJON4Ye_pj5QSGCwlnWU2HpDX-ej_KVbc_xeZCwsJlF_wkp9ZiwsV0RNYHR89sg9KjRnpA2XQRi1h8y0eKrO5AV1_VdSx4exxrLoKFK53ptjmUv4UhvgIFxWrE-Bl-c54Vq5PwLF5D1H6NMRttJVPs0LMvpYFlqoWGZtXYNpvIekf2kNoxqc-jhrnnU13iY7Se0FvaUxEMRiMYj4DoFrzGGFUFiOLBaOv-ZbNo7i68NJT3BLNCblQfKdHAkdkDUT_U3I6jo1DyBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پلتفرم‌ها در کشور خودشان از اینستاگرام و ایکس هم غول‌ترند
!
🔹
شبکه‌های اجتماعی فقط اینستاگرام و ایکس نیستند. در بسیاری از کشورها، پلتفرم‌های بومی آن‌قدر بزرگ شده‌اند که میلیون‌ها کاربر دارند و حتی از رقبای آمریکایی قدرتمندتر عمل می‌کنند. از چین و روسیه تا هند و ژاپن، هر کشور نسخه بومی خودش را ساخته؛ با فرهنگ، زبان و اقتصاد مخصوص همان کشور.
کره‌جنوبی
🔸
کاکائواستوری: اینستاگرام نسل میانسال‌ها، مخصوص کاربران بزرگسال که با کاکائوتاک مرتبط است.
🔸
بند: شبکه گروه‌های خصوصی؛ محبوب مدارس و شرکت‌ها با بیش از ۱۵۶ میلیون دانلود.
🔸
سای‌ورلد: پدربزرگ شبکه‌های اجتماعی با آواتار، اتاق مجازی و پول دیجیتال. میراثش هنوز در همه شبکه‌ها دیده می‌شود.
ژاپن
🔹
میکسی: شبکه دعوت‌محور با نام مستعار، محبوب سال‌های ۲۰۰۵-۲۰۱۲.
🔹
لاین: اپ پیام‌رسانی که پس از زلزله ۲۰۱۱ ساخته شد؛ با استیکرهای بامزه و بیش از ۷۰٪ جمعیت ژاپن کاربر.
روسیه
🔸
اودنوکلاسنیکی: شبکه هم‌کلاسی‌ها، محبوب نسل مسن‌تر و مناطق روستایی، ۳۶ میلیون کاربر فعال.
🔸
وِکُنتاکته (VK): فیسبوک روسیه، ساخته پاول دوروف؛ صدرنشین شبکه‌های اجتماعی روسیه.
چین
🔹
وی‌چت: سوپراپ یک میلیارد نفری؛ پرداخت، رزرو پزشک، خرید و خدمات دیجیتال زیر یک سقف.
🔹
وایبو: ترکیبی از توییتر و اینستاگرام؛ ویدیو، استریم و اخبار زنده.
🔹
دوین: پدر تیک‌تاک، با الگوریتم «For You» و تجارت الکترونیک داخلی.
🔹
شیائوهونگشو: راهنمای خرید و شبکه اجتماعی سبک زندگی؛ محبوب نسل Z.
🔹
کیوکیو: پیام‌رسان و شبکه نوجوانان؛ پایه درآمد و کالای مجازی.
هند
🔸
شِیْرچت: شبکه بومی هند با ۳۵۰ میلیون کاربر ماهانه؛ نسخه محلی برای کاربران غیرانگلیسی‌زبان.
ترکیه
🔹
اکشی سوزلوک: دایره‌المعارف زنده؛ فضایی برای نظر و تجربه کاربران درباره سیاست، فرهنگ و زندگی روزمره.
جهان عرب
🔸
یالا: شبکه صوتی زنده؛ گفت‌وگو درباره سرگرمی، موسیقی و مسائل اجتماعی، محبوب خاورمیانه و شمال آفریقا.
🔹
موفقیت این شبکه‌ها به درک دقیق رفتار، زبان و فرهنگ کاربران محلی بستگی دارد؛ خدماتی که نسخه‌های جهانی نمی‌توانند ارائه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/436253" target="_blank">📅 22:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b447f158d.mp4?token=swq247jKoeyhoa0cDba64g3ykIGEcDzCbYtZJCNSNz6SqxVXoI-ktfpmlfI75zeRkx2t8p7pVrh2BFdkiRF_hB_6x0dg2hCIxSiV9SQvIlaxxWHXyT3_TyM1fF11SgDPgfO_mZ7ygWgX40hXqeF6-QtBAcSPPdodp7HYB4GyvTXRVw1AYOh5iXv9T7W6LHqxqz2peKQAsDu4Yoh3JavwxA-kHe_nZzqpt66Io4mxhGUAFJ5h7qsUdbzF37phy3QlkQ8FJd3b72GgtQZbTThwFdnSZh3Ar3FIJb7uUwvTZYNWFTfGugrlI1i5PbzEP1EOn7yJoUgkaE0HZoaTm1Ocgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b447f158d.mp4?token=swq247jKoeyhoa0cDba64g3ykIGEcDzCbYtZJCNSNz6SqxVXoI-ktfpmlfI75zeRkx2t8p7pVrh2BFdkiRF_hB_6x0dg2hCIxSiV9SQvIlaxxWHXyT3_TyM1fF11SgDPgfO_mZ7ygWgX40hXqeF6-QtBAcSPPdodp7HYB4GyvTXRVw1AYOh5iXv9T7W6LHqxqz2peKQAsDu4Yoh3JavwxA-kHe_nZzqpt66Io4mxhGUAFJ5h7qsUdbzF37phy3QlkQ8FJd3b72GgtQZbTThwFdnSZh3Ar3FIJb7uUwvTZYNWFTfGugrlI1i5PbzEP1EOn7yJoUgkaE0HZoaTm1Ocgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دهلران هرشب برای ایران پرچم‌دارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/436252" target="_blank">📅 22:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7582a2e9d.mp4?token=pm0NWIxENWA4d1_Xn4BYQ2Aw2ntNcokV5BpXQzSGN2Nqm3NwdK7G9CH6NNjBEQ7Ibn1yLjD42H3fG5yRwAgHt-uFT4XYbto1MCOtJsnAd8cLTl1rkUo372pty8AyQH_anGWUPcCqaCtiycWypvKoRtMKfsVBfPDF8k_fCQ5mntaa3lYfZPwdAJlcOdFtwgowbsC-pBqu59w6C_oqQfXGynX09mGbYyFJAyYZ-452TSOYGJEL8DNfsrnlwEpGChH7j4EVA5FJxVGMMP8I7h1SKTltjrzUaUwMgY4mU9KECSo-2KnucmclTQ-0Ld3BtosaJNd7Dj_GRLHjPGxMjdirO7D_UgjLp8I2NkpgMHOefx_JbJiEzQkG613wMz-i9PQlWHSfe19sNQhtePnRlKKqQpsNp4zl0NuB1zyiIyJsQ-e_3LE6IxszBANxEhheBJWgicydouBKwjKmgi8cRSx5vhpME_Nju_5H9A2VlohYz-LVKcI1pcnw-t4usKCBLhBqZn68I_v5QEHGiA-xek1l8HCciOdhN_w5WaNsbemlEEQUMU9dayqQ5azMI7EmxTbfZsBsQCK27c0EqYWZSMgtVA2Hf67m3lm8iyAvtqWOTwYf4S7u06MK1CiIb8_A8QOV_Nj4xWnOWtTnMQu5nXn1MbLOMzK2izWDoXvK4rlyLlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7582a2e9d.mp4?token=pm0NWIxENWA4d1_Xn4BYQ2Aw2ntNcokV5BpXQzSGN2Nqm3NwdK7G9CH6NNjBEQ7Ibn1yLjD42H3fG5yRwAgHt-uFT4XYbto1MCOtJsnAd8cLTl1rkUo372pty8AyQH_anGWUPcCqaCtiycWypvKoRtMKfsVBfPDF8k_fCQ5mntaa3lYfZPwdAJlcOdFtwgowbsC-pBqu59w6C_oqQfXGynX09mGbYyFJAyYZ-452TSOYGJEL8DNfsrnlwEpGChH7j4EVA5FJxVGMMP8I7h1SKTltjrzUaUwMgY4mU9KECSo-2KnucmclTQ-0Ld3BtosaJNd7Dj_GRLHjPGxMjdirO7D_UgjLp8I2NkpgMHOefx_JbJiEzQkG613wMz-i9PQlWHSfe19sNQhtePnRlKKqQpsNp4zl0NuB1zyiIyJsQ-e_3LE6IxszBANxEhheBJWgicydouBKwjKmgi8cRSx5vhpME_Nju_5H9A2VlohYz-LVKcI1pcnw-t4usKCBLhBqZn68I_v5QEHGiA-xek1l8HCciOdhN_w5WaNsbemlEEQUMU9dayqQ5azMI7EmxTbfZsBsQCK27c0EqYWZSMgtVA2Hf67m3lm8iyAvtqWOTwYf4S7u06MK1CiIb8_A8QOV_Nj4xWnOWtTnMQu5nXn1MbLOMzK2izWDoXvK4rlyLlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسیب‌دیدن کابل‌های فیبرنوری در تنگهٔ هرمز، چه تاثیری بر روی اینترنت جهانی خواهد گذاشت؟  @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/436251" target="_blank">📅 22:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سردار رادان: از آغاز جنگ ۶۵۰۰ وطن‌فروش دستگیر شدند
🔸
۵۶۷ نفر از آن‌ها موارد ویژهٔ مرتبط با نفاق، اشرار و گروهک‌های ضدانقلاب بودند.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/436250" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_1qsyjuxOrI3TfW5gStFVVGL9iq9sZtGWc_Jd0O8CjRL3rHoplGVe3P8MKEaCrAu2GfZGpCtfVNxWpWxJKy2XnVMqmIEOe6Is0aI80qpHnG59Q8wiSh57Hw4O31JkNF4suG7yGuTAjN-c0506ddRuavNwSL2YBCzQFQDN1g0F_sd4fsznvbFjYkd95fgQg6YNW9oSErqi3SNzXZQTUY_zBCoTV8E-eifzw4MdvggJcC6q6Vu-V-fvyvoUFZB3wNK7GXuvNn_-y6Zq7SL9QnxzJoptp1q_poTpnCfTZb3iybPIa52cDM4YJ3_C2upPm60PIX3r4cLKJtQmRM2yFz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FM_yKb4DOadW7xdRaMi6daFl6ByLi2XqzTB-lK0XvhqZKONFQVWlhua8VZY7DrQ1S7Af9bHVHMcdiK2c99njX4NDIaksHLFT91TLK-8trs0pAwhU9vObUpNrwSFdoJPQ-37QvylFVdbxw-jdHwagfrRRQqVm0dNCjE5iA8M6GhGih3l4jlkm-Sph_oDP7cVXNy7bQ9IVc2-atGhrsP2lRVOT9rr8Pfwy5_fSm28Mg9wL5WGQC9IhoLqR6KReTu7ougoUyB9zx_NLHGTn6HBcaCUZcKkOibbe1zE3LAym6e06LtOSJyrvdraWEAepdTg_R6dE1f32W5OgbVGEEamGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmtmgKj4oLphWKH76063Kxl1IFTqULriQbcvt3EqSJf3ip3t6loDVZYpBFV2sUgnmvE03-dY0hH1Fox2VGrQ4D8wnGohyBs2Guqs2uytcqATLnY_EmfjtdJ1QQTfT353OWMS4dyQVJ9KYEbiv9_5_OusdfQ1A9MOazDrJjzxnA4zQbn1v_WOHeKXCYEn28hfFTqjdxD4UkI5WuQWzwET9rEDNldQ9yNqGo1lB1MHcv5i3agUKPV4xvcH8944GibaFaoN9bkyTvpP8fJ25Wym7UXTJL0DVRj2AJjXewEJl5MlHDOFe23f3LvTHwSFgJPcKaHhZcmJ-e5WVND2AVIZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHKngJGuGqzZDyCinuEla5vdLQMuxiCy9A51r68zmvifsgEiHqrZFzECK-9rJH32PZVB-M2FIhuikW3Ss2fnAAtoLaz2kwOob3Ph_TwK3tikJd_nhrMg52WjkLF5V9M_Rui_Fc0XylQj6gkQWm9na2mahGkrywFhxTbn3cFRZcehPEcybAkwr9ciiN1IzRVO3-nz3InR_ZGLe7bTd9CZIbpUKIfX6D6ShUfJIUYEbhjh60BpRlPFQvyQpY5Dq1HWRtnPrdsyv1FziT-KWebm5HF3aiJ4YQJ5ziRnp_LYXkRbHnYhnMk10P5wgMWP9wDhl1KBg4AVk5uAvVAJpZjK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWVvkMD7UiKNdN-nPpisviWOzc0VROkuTgdlkBtD_yPJJSdH8LB66B3Xj-88zrHuyyDhr0yAkdBBvLLLlNcgJPzsLktJFBU6QT6koEFIGixuo5Dqr36GAKXnlVWsCntiRdDVLjwzkeiNSNQYUnQYDX5aYBQhKyrWJDHJ8U0mP__cBXiOauNgeW-sMecxvrAvQQN4im5nwhbepkRaI3DAroPt97NsO4kom9XTda72_Mp26WzzhFqS6jhm7dg66Va0Qyr3UdLCHdiItmxB2LXVfa-mwb4rZWJJwBsPATXQvJvK_RpmMnT49znZMOnvuCs_cRRJDM8R4U0GJWpgpo-fbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vo3s29WELyWPFZlukmpiBNfb-VJPeE7O61n4VspLpbu08VpM8uqISx0Bv0YqhibMc6src8DX05F-ggtCvxK7DAb0T7KRFkJjFxfGX8UABNr-qrJDknbicwpH3Xrye78otFGSL5IBi4swvAqrFOYamrLc1y6WUSZc_DRlZK7oAIc7kFeaZiAJn2W3Z3gkTNHgNFic-D_rLPT6uokdes2CW1Z_T9tzbiUQuUPS_DilN38pamURxlAat1BJjIp-Ca-a-y7yI6GQ2cJTtdwr-PpIa-PqIJHXrNZNgiuyk8yHh9etfXRuapwu3ZtIIbJExQpXOqTyCPN5_ySnDE26XCDnRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI1kvr33jCvS_LSVo4d1hRVsnqwLRDRmTPChYg7wzrvfyTw1gxTkwCIsOzaTeVqL7RT9LVQ4c8M_CteSO9ukRspjxFuskB74mUe2U9qwgbrBP8j6UZkPIoDp26Xrqg_7dX9JlY7Or8SrtqdyDauX9RhNoVLeZ5otThOCoLpRHd0ItatQquxO-5M2jKDJc01VID7Ta07Y-9Ecs9x9PfiZJ0o66ijY2Derw0FTk-onIEih-eqpraEGDSovE1C0pd5SK7sydXy3skEHVEsrLJ5HzmXPuhFUopJ9MFTvfH2vHb8v-gqec5a1pc035kgEFI5-mMqoRI3bal7yKnXL8dPXvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سنگر مردم بندرعباس به روایت تصویر
عکس:
عماد یگانه‌دوست
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/436243" target="_blank">📅 21:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bad9e4b7.mp4?token=lvWpZDgbpy1PyalRedqCqPalhpsD6HrQ3NpOauOPWQXewtHWbwecVyxBnVIrCfOYiM8dzw-BQSxuOewNiQmhrjwUVkIz3V3pAjJ0U5MVxhPoJn8MBqh-vOakIFOuHD6eAUVUEyHn7USQiKt3ycX3NWhRwmyfBj7GzBdKbe9jL0AV8ijkpuxFBAmadCjFWbDMBRmElqM0E_4L081MJYGmb1DqEqr_56-KD-6FhGihUrCWmmvRUjs-0KIFm-2KVUM6-K1bsxx5Na8PFf04GZWpuOJ97X9kLJ8AaSzNURQXKE8hzaMAjSYymQYSxgd6ubk4jEjrIypcu1HS8J-kneLmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bad9e4b7.mp4?token=lvWpZDgbpy1PyalRedqCqPalhpsD6HrQ3NpOauOPWQXewtHWbwecVyxBnVIrCfOYiM8dzw-BQSxuOewNiQmhrjwUVkIz3V3pAjJ0U5MVxhPoJn8MBqh-vOakIFOuHD6eAUVUEyHn7USQiKt3ycX3NWhRwmyfBj7GzBdKbe9jL0AV8ijkpuxFBAmadCjFWbDMBRmElqM0E_4L081MJYGmb1DqEqr_56-KD-6FhGihUrCWmmvRUjs-0KIFm-2KVUM6-K1bsxx5Na8PFf04GZWpuOJ97X9kLJ8AaSzNURQXKE8hzaMAjSYymQYSxgd6ubk4jEjrIypcu1HS8J-kneLmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تنگهٔ هرمز، کابل‌ هم حکم کشتی‌ را دارد
🔹
رئیس اندیشکدهٔ اقتصاد دانش‌بنیان: در تنگهٔ هرمز طبق حقوق بین‌المللی، ما این حق را داریم که همان تصمیمی که راجع به عبور کشتی‌ها از تنگه گرفتیم، در مورد عبور کابل‌های فیبر نوری نیز بگیریم.
🔹
یعنی شرکت‌های عبوردهنده…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/436241" target="_blank">📅 21:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c115053608.mp4?token=eqnSUw9tdJF-h7dL5hCNDyf0af6FCEnIx6M5cTZ0d7qndbeHJs2elzBMaN2-GlA5EajaO6-8MBcN8Tad0Go3CrzWe-DARjUSGPqi2C5JTUehF4mU6rUG1jrLIs9MQZIFBFhtB1qWjhqqd_q66mA8aDMvwuSjHFIdWskf0dvIt7KvCdrDK5pckbUtrnU3G1QukcZKyVYyIztTsCedK3infz6A_KktKUataXsooDsByrMvHQsDksh_vcviQtHVUO5H97n3s6de5QQwhJhBBPSP4TLv6DCY1fZg5z8PZfDXAD_MHixyOvJIcIZh9HpJ2tssAQO7-RnLXtQaat_pG0dwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c115053608.mp4?token=eqnSUw9tdJF-h7dL5hCNDyf0af6FCEnIx6M5cTZ0d7qndbeHJs2elzBMaN2-GlA5EajaO6-8MBcN8Tad0Go3CrzWe-DARjUSGPqi2C5JTUehF4mU6rUG1jrLIs9MQZIFBFhtB1qWjhqqd_q66mA8aDMvwuSjHFIdWskf0dvIt7KvCdrDK5pckbUtrnU3G1QukcZKyVYyIztTsCedK3infz6A_KktKUataXsooDsByrMvHQsDksh_vcviQtHVUO5H97n3s6de5QQwhJhBBPSP4TLv6DCY1fZg5z8PZfDXAD_MHixyOvJIcIZh9HpJ2tssAQO7-RnLXtQaat_pG0dwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: مردم صبر کنند؛ با بالارفتن تولید، آرامش به بازار خودرو برمی‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/436240" target="_blank">📅 21:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3032165313.mp4?token=nc7qpzRD6sAjnA301VCvfa4fgeCvTwD6KDgLG2-wqW3fsD8y6OoKS5fThlTepzEXBFJ0olDebmP_ux4yZqtgTzr6MrbsBNAjXZcJOJHSbhk7F3bM6Nnot3H9m8Y-fkh0kg5u_BV5lfR-K9sV0_JRrH_M-IetIUcqNxHRLHw9vAD_zwHExhLqH6rTmpVYbsF9oEYWUIG8a56lAyCbRS_6XRiksfKLHzmags_8Kd2lbMNRGl1w1v4e0FL0g3QEJDqoQMEqUCSG9gqFumbToLyvgKS6vt70igToxFzmX370Zqsb6LVJrb6RWfwjD5aFc2gM-a0U-LhTD35qhYMCTwxtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3032165313.mp4?token=nc7qpzRD6sAjnA301VCvfa4fgeCvTwD6KDgLG2-wqW3fsD8y6OoKS5fThlTepzEXBFJ0olDebmP_ux4yZqtgTzr6MrbsBNAjXZcJOJHSbhk7F3bM6Nnot3H9m8Y-fkh0kg5u_BV5lfR-K9sV0_JRrH_M-IetIUcqNxHRLHw9vAD_zwHExhLqH6rTmpVYbsF9oEYWUIG8a56lAyCbRS_6XRiksfKLHzmags_8Kd2lbMNRGl1w1v4e0FL0g3QEJDqoQMEqUCSG9gqFumbToLyvgKS6vt70igToxFzmX370Zqsb6LVJrb6RWfwjD5aFc2gM-a0U-LhTD35qhYMCTwxtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌آفرینی گرگانی‌ها در قرار ۷۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/436239" target="_blank">📅 21:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8DvKvuoPIIrfVscBzkIn4Bs3SQ85ANbB7EmRRLtGdWLDQwYoN8Mkdjbd5pD8TlMSDihxaICj1ownr8lkt_Jnh4-872JTXpqJBkJKp1JFKbtXXqEVnDnF7TfCLIjgEUffsJfvBEt6SyrvegvINz2_LI7XyG7eOaxZTdWzV26BEVw2ikrSW-nFuOkY9QFIzLvyIr0INNqg0dbYrp1fiEZl7FeMklsZBluLdX4ENKP7vEmPu313sR2XrzNm0TsNWhPnTKRtwseUmeaI50VQzK4GIRfgn9UIgFAWmBNqayFTJ5aFYSSNDI9W5FFfUcbiEP7Dry6x-FxU0iFHAXZ2Y6k8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ای‌اف‌سی سهمیه باشگاه‌های ایران را افزایش داد
🔹
طبق رنکینگ‌های جدید منتشرشده توسط کنفدراسیون فوتبال آسیا، فوتبال ایران در فصل ۲۰۲۷-۲۰۲۸، در لیگ نخبگان ۳ سهمیه مستقیم و در لیگ قهرمانان سطح۲ آسیا یک سهمیه مستقیم خواهد داشت‌.
🔹
فوتبال ایران در فصل پیش‌رو (۲۰۲۷-۲۰۲۶)، ۲ نماینده در لیگ نخبگان و یک نماینده هم در سطح دو قاره کهن دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/436238" target="_blank">📅 21:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
رژهٔ دهه نودی‌های چنارانی در قرار شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/436237" target="_blank">📅 21:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6z3iIusLUuS-WIpQsvWRbNWiWhLFM0_rz-T1-xTSQMow0bG-uDxuUcrtlpJlVRB0DfWt2vmpINbKFfyijELKGKZnEX3NTRdq2NmvSYjMOVYeYhSTqma1ENbpiAhNARazzbxU2q5Dtrosa0zwxMNtTlSqjpQlC_riT75C4uvbj7DSDuKLW1PytKae4gxlf34tbUVsGHC8Uqprvr7OUMqZ03ifrBV6f0JRwIpiXyHrYcxMxSJQWqvu-axNo-kepdpHyxr90zjDvhgaWbbqsdDHlo694lnSMX3ZYdYIKWgP_ga4q_fDh2EoFJzL25JbZTjTXvsGSgWsS6Zny6itJTJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همای: دعوت رهبر انقلاب به بعثت هنرمندان، فرصتی برای همدلی است
🔹
پرواز همای، خواننده و آهنگساز در گفتگو با فارس: حالا که رهبر عالی قدر و جوان و ادیب سرزمین ما سخن از فردوسی و ادبیات و زبان پارسی بر زبان می‌آورند و برای محافظت از فرهنگ پارسی و تمامیت عرضی سرزمینمان در مقابل متجاوزگران و حتی سرزمین‌های عرب که به مردم ما خیانت کردند تا پای جان ایستاده‌اند وظیفه‌ همه‌ ما هنرمندان حمایت از دیدگاه ارزشمند ایشان است.
🔹
شک ندارم هنرمندان به زودی سکوتشان را خواهند شکست و پیرو دیدگاه هنردوست و ادیبانه‌ رهبر سرزمینمان خواهند بود. این تفکر همان اندیشه‌ایست که سال‌ها هنرمندان در انتظار شنیدنش بودند. حمایت رهبر عزیزمان از هنر و فرهنگ پارسی برایمان ارزشمند و بی‌شک به حمایت هنرمندان از دیدگاه ایشان خواهد انجامید.
🔹
بعثت هنرمندا یعنی هنرمندان و مذهبیان با هم پیوند بخورند و برای خدمت به مردم مبعوث شوند. با این فرمایشات مدیران و هنرمندان با یکدیگر آشتی کنند و برای خدمت به مردم قدم بردارند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/436236" target="_blank">📅 21:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
کفن پوشان پیشوایی جانفدای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/436235" target="_blank">📅 21:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZC4rfBzbPolocj64kXbluzEBkkGVxd9v0Q3NWEhfHkXwpagAcncw6yURO8dR6oaR3XgANYHAPlv2q8GPWSMqk9G1WZc4rEdwtK8_2kgWjhywgkLojdw39z6_rxXubQFUa-D3WyXf0EbdNuUIIAMyDC7Dbeo8d67udRn75yIqMoqEYRvJFvgrAdpjv55c4nsaIOPtU_5Sl7hGvi7qmBlhuhy08ALYSw8AJMn0HfUWLCLGyCCGN6Mr_KM1SCVOHAonPr9Vtn5kW-zVhgA-OcgDDk2NymMmSfoVGW3NO764pW9kpD7Vpb4227SZ5ueLBI8rDmO0B0uX7BSOmo5V688gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیلی: وقایع دی‌ماه کارِ موساد بود!
🔹
روزنامه عبری وای‌نت در مقاله‌ای به موضوع اغتشاشات دی‌ماه سال گذشته در ایران پرداخته و حقایقی درباره آن را افشا کرده.
🔹
وای‌نت آورده: از زمان شروع ریاست دیوید بارنیا در موساد، عملیات روانی بر افکار عمومی جامعه ایران به بخش مرکزی مقابله با ایران تبدیل شد.
🔹
ژانویه امسال، هزاران ایرانی به خیابان‌ها آمدند؛ پشت این تظاهرات، «کار عظیمی که اسرائیل انجام داده بود» قرار داشت.
🔹
برنامه اولیه اسرائیل این بود که جنگ در ژوئن ۲۰۲۶ آغاز شود، اما پس از شورش‌هایی که موساد در ژانویه سازماندهی کرد، نتانیاهو به ارتش اسرائیل دستور داد زمان عملیات را جلو بیندازند.
🔸
نکته جالب این است که پیش از این افشاگری، با وجود همه شواهدی که اسرائیلی‌بودنِ ماهیت اغتشاشات را آشکار ساخته بود، جریان سلطنت‌طلب و رسانه‌های فارسی‌زبان اصرار داشتند تا نقش اسرائیل در ایجاد و هدایت این شورش را به‌کلی انکار کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/436234" target="_blank">📅 21:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">دسته‌گل جدید مدیران استقلال
؛
قرارداد ۲ میلیون و ۸۰۰ هزار دلاری بازیکنی که به ایران نیامد
🔹
شکایت کارلوس استراندبرگ، مهاجم سوئدی-موزامبیکی از استقلال که به‌دلیل ارسال قرارداد با ایمیل رسمی باشگاه رقم خورده، حاشیه‌های زیادی ایجاد کرده است.
🔹
طبق آخرین اطلاعاتی که به خبرنگار فارس رسیده، رقم مورد توافق استراندبرگ و استقلال بسیار بیشتر از عدد مطرح شده در برخی رسانه‌هاست و این باشگاه مبلغ ۲ میلیون و ۸۰۰ هزار دلار را به‌عنوان دستمزد مهاجم سوئدی برای دو فصل تعیین کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/436233" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa837ee13.mp4?token=kojS-H0Vp64UKqdbxNKLVeDKOcf_VgQUND4sVRdvEMfpp8gwrPKpdARxu_6jNMHCTLc2WrufMPY3ToKh2jHCHHC0ZQLpzKWhsb4uKJJDWf2JNvfNIuVMajAcOM7t6f-_pHekNQ8mJwkjn2HeR97AVvbA6HwT1hAWU5rVXSq5ixv5Nl2elcSULCNTeg_eRrokfauHQV5dd4x0GMZSo-j38NO6yGDBWlW-k_Cob9dyEf3QmVjfPO9QavRd3WGAA6jee-2LoLCOiH1SFjXHjbU9XeXHpGTVxAZSNS5ejbWaAxLEZQYoW-uyNVqES9liN2Xll9ciOylPZGZeqSkbv6zk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa837ee13.mp4?token=kojS-H0Vp64UKqdbxNKLVeDKOcf_VgQUND4sVRdvEMfpp8gwrPKpdARxu_6jNMHCTLc2WrufMPY3ToKh2jHCHHC0ZQLpzKWhsb4uKJJDWf2JNvfNIuVMajAcOM7t6f-_pHekNQ8mJwkjn2HeR97AVvbA6HwT1hAWU5rVXSq5ixv5Nl2elcSULCNTeg_eRrokfauHQV5dd4x0GMZSo-j38NO6yGDBWlW-k_Cob9dyEf3QmVjfPO9QavRd3WGAA6jee-2LoLCOiH1SFjXHjbU9XeXHpGTVxAZSNS5ejbWaAxLEZQYoW-uyNVqES9liN2Xll9ciOylPZGZeqSkbv6zk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: یکبار یکی از دوستان گفت اگر به تهران بروی چکار می‌کنی؟ گفتم پاکبان می‌شوم.  @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/436232" target="_blank">📅 20:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
روایت دختر شهید دریادار تنگسیری از پیام «مشت گره‌کرده» پدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/436231" target="_blank">📅 20:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5240e3c605.mp4?token=ALWGCpxfAGCwl6rDLgCze6z9EIFxD-UQx8aTS6KjGLsaWWOpnkwSgij9N0MnMDSqcD3Jfcb3nyPBtYvpXqoTBexQP-MM7WIYFXlRtthK7YWE0XfUVeYH6YK6867KjJlQl5XRYGiXO622xaQzaUzhP89gc4UjVJL842f64luDlPK2CadozEgzI2ZEps5C64X-N1ntjyhbfFGvOrpkWqxKvL8bUzmWc5jx4BQRLHmy5r0pYPXWyeE3PmWQ1SkCC9fCRaepmuC8glCy-x3cXHYk3qAQREk2ltDKtv4wQxgjyAcCCfA_z1EnRs1BZtqO2WMHzqZ52cj-ZlGuSGBlTPOkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5240e3c605.mp4?token=ALWGCpxfAGCwl6rDLgCze6z9EIFxD-UQx8aTS6KjGLsaWWOpnkwSgij9N0MnMDSqcD3Jfcb3nyPBtYvpXqoTBexQP-MM7WIYFXlRtthK7YWE0XfUVeYH6YK6867KjJlQl5XRYGiXO622xaQzaUzhP89gc4UjVJL842f64luDlPK2CadozEgzI2ZEps5C64X-N1ntjyhbfFGvOrpkWqxKvL8bUzmWc5jx4BQRLHmy5r0pYPXWyeE3PmWQ1SkCC9fCRaepmuC8glCy-x3cXHYk3qAQREk2ltDKtv4wQxgjyAcCCfA_z1EnRs1BZtqO2WMHzqZ52cj-ZlGuSGBlTPOkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: مقاومت و تاب‌آوری ایران و حضور مردم مقابل ابرقدرت‌های دنیا کشورهای خارجی را متعجب کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/436230" target="_blank">📅 20:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436223">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPDhErKxGXbPG2PBy4ybCMOzv_A1MlR0aNT9l_4omfjim-tczVK222gfh5nyC5Op35loloXMyNZqEl6pmw-U15Vfx6Q4r1Jv7EgVprqbD8ylj0sdzaFAnF6pS-ULMwZyW8XgOkeEP0PSNQ9SQLyz000t8L6KzKYDujWN1VpGJZf7byoLfq3agYv9H2xGJkKtdVZsnLyUw9MpIXV17X3VVfYmKZvAx17plBBH1_uuG2n2OTk8BtHP9KjB4lePNIeBfu1F1lZde4ypMWwnWujA_mVM94I0QMJtTbBkz8TWkjSaapCNR4GlliZYMH5V1A1RNF5iBq5rfxB2DE-bVx4pvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVB3VASMm_xnvw0wR6ywScnIwzM-1KLzJq0zLICXvBCnN1SSzQF7085Es737RNwX2O1Bme-Nuu_RZ7cK6Hqs_Zh1x-kFwkoFIIyDWNoXqqMfVVMa7HvO8JTRJJQmz-pRJcPx_dutDmWOls2U-KL2O_HXZduw8cwSq3eCriOFTbJrYk-qGJHe7ae2ZqxHxFT9eOeUxV3IvGnJBXEMUol3CKhmPU82py375OVxayGHQ84Z-ZlEHQZ1BDKj5COCYTVf3CrQ8Y6Xjz4s33KVQMaWmyWWFiQMayfGXpAF5c7EloJvvVahH_nW_QH9_UyrAKjpK3CNlvLhlbJT-PYdHvySHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7lbJbvCbPZSUoxOPpRAhAsloQz9dXN3tfP0h0X3KCqJ6C62_JzgR9yovnOxV_YB81DOcknlHJcNIBwHEHQD7m6o6D-m12wTXSJXEg1WqRc8RS8rWsUjtD4jvcL-r3x0J-TUeH9MLJBD7fVb2jyZKQzotEVYwqRJduWfUBNib2a6gsV7z8ovJcfqaZUaNOSH5rD4a57qt6ayhih5xWRqBsx7xtVUrTjJunemzgGLtXdV4v4CsVQ9kzxnRISGLOOwM5-eSRRjWw1l-27wA32I2GvjOgDHRNOa4eXinTlP1QMlpMDf6Pa4aTbLlVIPPUuN-Ndwuli9ciWukZ23BZU_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkXdQwe5CpGj77VDR6sznix6obOYZD-ZvJlz9xduU-JgTPLO-f67kfHCKkaqIJfG1VrQcvZM_rqtPqUiRyV7pt5ZcdLqEXdtfE-WcDGJRwwgXTRrYtKcZcqzyJGkmnB0asKcw-ry6GmIyVE7YFmqxRC7XBdg35Eb32UZygT1Xe3zplso-xe_VLH5bWSIhi5xqUVOCj0KAeEbe_TMHQzFgTbz0HK_eBdeJ0yOPkiZYCCPROY6qCqoJB8GVyJP4g37dkjaEQMwpUt5xdS_NYwX1KjVkpsU-xJEe77QXb6B-Jb6BNqGJPv8mthETp2sZkZc_lCQDUZ9mWhcRNFLomUtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnVeayMoTFLMYS7bvj_gCdiIIQ6hV81nglKDzA3DhW-dXdg2pYoVhL-GReEtkO6DEYYKpXYs4lIntbTG_A88UBxVpjo9XKNLxZKWySigDIEWcwKeU_ot-NsJIMEwDWbpsDEypiP6iaWG4QqpvE-n62vddoSA7F1YO8IlAwVLGKh52QJ0feMNyDRF09W0Q22SuSdPxnuaKgeHC3mPwl1nYBIbyQx8pYEd0lC9Y2xutmU8j91MJ2dlfkT28oypwgOoI08AnsuHuB3_8TZv3IEUOCgYJdIwQKdnVl-yl4tlFXJ29Z8PRur7014PMGj2o9ZHXYFDaTS0vpO4w3it41MGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7FJ2O8PNVlqfjskkmC4D6p0kndcrCUa1EOf1rilbm1F57gTkogee_g5gUogxIE09kl-D0pqC8hRrXAb58C-MM8aWuJQj4Q8Yc8pvLJ-ejEtF_PLgM0fnVqM2u8A5R4d5py3u92Ba-4p1pFWF74BEFkOGDB5bYcHgLQF_gBZk3JFWXIzHd9D_Stfh_iHUIjTLV5rzqsVgywBKPHE9N2I5U3QL5hgVqXOKBi98eV7xfx9iX2cscABDQkgdiLuR9_1NlznI5b0bK8qcmiIDQAVgaGOPi5U7s1Q_BoXvy2_6VF8rfgqGa4XY4JulxcI97oMZ3R4YJ5ht0lbBmUQOQmDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOHSiVmPRed6ts1GKlGY2u8s4a1tPX3Soe3vTnqX0Ex6eWsF5CffX2rDY-lfL2qYIf9WlYpv1B2dF3KQvXxlHBJoYrNADZkqULlxz9k-82JvcoP4BW6y43iMWqwTeNH0ktBE3fSEdvsdr9mGNcwJooOKkpOzVW5Qo2dCaXu1Bkw9mq9KY8iQ_JeZH8UDBMEFsjuQCIsZqmVViUFghoqjKfN9jUPgJl_zDaUcyeunq8SyLz63SEQZm617Kr1HsAyTXzoykkpEscts28HxogxzbfWPA6DJFhDMQ-LNt7n84wCrmEP6JBW8jxWlZqfXX_xM05pfaLyyQcHDpAo0izxLMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت وزیر شهید دفاع در مصلی حرم حضرت عبدالعظیم(ع
)
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/436223" target="_blank">📅 20:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436222">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مسیر جنوب به شمال تونل توحید امشب مسدود است
🔹
مسیر جنوب به شمال تونل توحید امشب از ساعت ۲۴ تا ۵ صبح روز بعد برای تعمیرات مسدود است.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/436222" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
