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
<img src="https://cdn4.telesco.pe/file/BfD5Scqb9-lcxgvvsVgL11eeyjZEiEPfFq6aJzYmBaHPtRZw8IkbdBZz9nPD2E6Ai4wgxOO7C6nbPu5uL73MravNhUYyR8-Rw7NyEn7V31dxihfY_Zea8qfiut3M9gMFXua-ZExgkVx1eWolWjAipX3N3r5Lg-t0uqYlm47eGpfPzufKhxa7Gmgsrnlhcyualh2tJWW7zH_i9NOwNQKUs96_Cp9lgSCNmQ2xEQMuT-AgfUewVV2bubCeyiJQDHC4b-5r8ExaCt-pVgFivzopkmcxbs8mH5UckaCYnpnMu_WEr-TOaOX_oQBayCGuK5EgqQPEl9JCRKdfcX61HxXpBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4riYTDC4yDFUPNAUHZqDyCgPV48GTD3j3XutjSKPy56QAoPWBG5jA5JKsdfI6aKthUJc3hG62wMcYlqj_IgvFfV-90upLv0LTpo9RNfznXaDYFn1IAFuJav70E637rPDT5xZlZTJZPMoOEjGhL0unDEP6R68iyEHVFbwG6CFuNQdMbAtqq8cN_E3wO3GX9bVuZtW5HQB_yYaIX9QtY8-Rh9KS9K-OMVqlq9Tv2-SSeZ5sswP4NcvQepzh37AfZ2hurl8fmGXpbrprrAD6RhW489PPy9G0z1KYJ-8IojoJHHM2fewmtSO5gZ1-zc5HJ6XXdoEwrHzo5jpJFBOiPrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUVrrt4Ol7Z3FYenRbwJYYFVS8ceTcOIxAKNxvRt5lUC7A0FBqQz5GHrTpZeC6Dc3WZeqohNvhlzk1AQL8ro2JVywobtMZt3z3SmJyd-NBgiuEE0puglT5KGepg23gFbYZD6lyC4OW0D9GcjAAKSE2N_FFajhwb-pANl2vkgMAvIXNRLzrfgfLaXHi2AumDqjNcXU7COMrtMVIsDMd3C9opVZWKzJrMMw1NhlTLdi4PP1f8-pZI_GcxZzLi7L2AVlm3ITQDhv62kJPrZXy5osKPT5NLFv-q2jGGWM5t9q9AJWZG-99rEhS4RfUtrPcolediSSCKXZhIYa7lTDVlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwJXJR5m6e9uYhw9s6FadlujpPdY_sBPZIYj85ACi8qkWmMeL3qhNooKuqWsmcdqdPXaM7HvaHgzGr8fvV2JXAOqgWnOuHaJq0pLP085jbjjJL326P9e0yeBR6887ir0LYIGQ3uULXDmKj7jVm1EeU6bwf3UgGssdnv33n_9lfr06BjRb3QYHjjz9J55vGeuJB0VfsZKH4-m_X9lFJpahGzK8ystzjOQ2uNklp0UpDgA5DbCsY31vdc0qARZFu8xO5q3X2vxeYiwHTUBCM9u5kkvr1PyznflvGSJPpvkQpStWUOH-stseVIJnK5W0jLfBRYUbyQBT4lS9dtkwiboiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKiyFi60XPc22hIojnncUbJVQG6b6UfYE61jWlYUsoZDyj2Ei1a-oRcISMY76KvjSjD0e_zxbjyzazPCoQC6tJT6YQ5KT0iAN23eLqfR0zcUBy3NbYkI3zf9oS045oxl3hhoqnFqHOBr9ZLOhkUHYrHO0NY3UQvZoQ8epGNcql1tOcnV6-7VnDIU0jClXuQHhCfoZNNgNEULhAEai6nf4vRTwqFF7nA1-XzRBi91PG5xnmM2E3UYbBNdNNwKiNZITUhqi44xMUYFd1byPaeUwLNTeYW7XeanedW78rRQ-VHElaiq55VQxnTnZ_aOqJpCdsRaVZeRefM-uD9dyiesmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-PaOvOY3Y2wN3x0Tp_Z458ervsMYibF-scxUkOSua1qYWJuRTW0Rcff1vxtCEf8_8rMVU09_JyM-5zOE6MYgdZ4JJG0Hhyvs_hJYkEkSrn9hJj_FF_TrmVVWPr1UE15h6yQvLbiD_3j6e_Ujd_clRKqBEn1c0pSf04tE3U8r2ocRMK4clHpxDzjIWJBnW9XisnOZtkP7iES3NJavuxyB0Vo_506uWpTURJoz_2keksM8T1YprUTQR8u70HCNuHGqofoat50e6_ZKpRnASdjUR6BH-yF-T-EdJ-WyDJ-ECdMa_VrwSjdGhvDknZyVWQ9DtZyOS5ZEs8iRWWcr8AAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzfX7WI-NjdhlnTluU79edx5PMvfuOeRW0con4XcV6d6QdaqIoLVge1DjlmPQ1YrvvQnorrZGlOWRYKHu9FA_9fxNEIFNOzPWO50QWMbTP3lkDscZ43fYEQTkif24gpHxC0U5V4nnGaoqJTlFbDCJ_7a-YyUUgrdcfJcQ2nveX_jy6s18HAoIk6qEUlU28_xJJusQpwqn65x97ly1u6ky9tdNG5aUMgkML_yTgRltar6biV57nyZtZ0qHVv1KD62feymovS83X2SWJ_dKUeW4vBccgMH9hhzV2VIQIMjk56KnzH3VlQpmtzZerwRn-Nd_Me7bi6Zp82YH7IW_n9BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td-RTQg0GPaX84KS_vQHby6URLhicIkgZBVHrJXJKjgi5W_TkTTG-VIStbPYf2Xi0tV7_FRzTA0wueyFejwyJTXY4eYmwNVCWLOaUxxa8LuHPG6XnQSawVe7y2JK3f-GCQqCcGNFkG12dmVIYWkUu2uEFlKkca1uoTkURG6zAxIub11szgYWT1uDF4oMhEIRSpv-IDiWq4CcK5NncfKrXVAMfleUq-3mrWLf4D7lIS3KzL8EWIxWaRtM_RU3EG75vnJNkW7ho5x8TE-_R27ns1nBVodwC8QODrr-XNKkohz4N99BxOtxxKnk6EPwIAGU8amo5n6AJaqV7Cpyr5wQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWVHknxVAwzzVtJ3aTFg4WOJ_SuqeZ5_a45lv-ThVVbHvEKlIS0zUxa9nkxFJzPiJW9qFqyqUiG24Szvd4uAwo_7IAw-Ll_4k5xyOlTobxfRg4AMewSHb3I9Bo25Za1F9UZcwPZx6ii_Lr-hE87kCA7Yyo8Te3c2JV7eF4YXlI7B9Elua8oyz-LdmJWTYjUbUcaK5agvzBN8Z-2aDCqtSZuqOhhR4NvgJZXatj-yzBiQ7V-8wgEXsIpSWM6V_gfgx69yup15IUoNzP7tqITWVADBsoxxornpoH417yJ2I4uBt57aPY9GtIkN7tglWZ2EeSopSPjj9tjBYKKHzsp_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvVHn5NLdR45cVaIjPWVcaNnO7hRfBLdb76MpToopVhjk2KtX4nthTYaXjFRdPPY1mBxum6fJLL42RySkGCCeky4bWI5zW-dIAqQnaUec4SBDdhwOspl7uOOmSZRkw88YDuWE5z9pyYDzYX7hlM-XT9nNuW_YoQLY09kSKcfHmFHyd0AcgbR1zGSur1OEDEHBH6MmtaKPi2PJNWiTvlJ8BWOgxfzqNle6O0SKRGJPliZ8NMJjBMu4U8b7aHLBF9dDTMFI1XSfl8T7V92-7i_jv5afoL6cSM6i9wb8RVIb8_4SlS7MkIhjTEur3mcuEfBW00plZDMn4Upod7uHc7hYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=iAnP9eGwPao22Porxe_UJDmKTQpoYj67iJlRMdsjimGe5wbxvKPWOK2M692j2EPzYLOw-vOcsasaaMgx_TtOwoWvPP2XnTqZeg2QQ1E5NAoTgeHZ80TpxUsd9Rt4KS-OACW6YVcxpF24ZHu_R9vqdmaZyGVCcWeSrEYhdJ2TU4YQxIDKSoQAluycWG0fLu_LGU5pIC112VnSbY-u5EwX0rqVNqVx3GSwQxbBzgpceoh0B64oR0NUZ1B6rXFz6RaWw_RFuq9O-IBuagSVtIzyc12n0HPJN0HFN0Jf_sKejPXeBZS75j79UfGKCFKgwR2uP5L10BCIDp4xAxrd-zjh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=iAnP9eGwPao22Porxe_UJDmKTQpoYj67iJlRMdsjimGe5wbxvKPWOK2M692j2EPzYLOw-vOcsasaaMgx_TtOwoWvPP2XnTqZeg2QQ1E5NAoTgeHZ80TpxUsd9Rt4KS-OACW6YVcxpF24ZHu_R9vqdmaZyGVCcWeSrEYhdJ2TU4YQxIDKSoQAluycWG0fLu_LGU5pIC112VnSbY-u5EwX0rqVNqVx3GSwQxbBzgpceoh0B64oR0NUZ1B6rXFz6RaWw_RFuq9O-IBuagSVtIzyc12n0HPJN0HFN0Jf_sKejPXeBZS75j79UfGKCFKgwR2uP5L10BCIDp4xAxrd-zjh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjqRjP8bhvByhu_5sC16df0m1a6Evy22QYJDyMEWVp38QPliPzRjDShnzYbIVI605GFW-kkGHtmXlP4jTZzdBhBSwOFI8M4w9MXhcQyR-676PM1rS7jPif59Rqvw1KlIAFfHgHfHu6Oz877ihyVJr_vp5q_Mn6A86q_LvRAA4YtzDuCsflQCcx0Gdp1M1w3cgdIDQqDO83dTcCb-5WWIXmn-edGmo2JtieA5tjYSDYTKFgEPhshHrdA7t7HsNYXVZCbWrZTXBdB-jIstz_4QnZboV9jDt2fyIItJZoXsgKTdwBU61fBFfJ57TnVmRoAQegaXZH5Tvu3O9tbxoMSZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xze51gKGFiwnpu9nZ9wCQyJYYAfm2pj7nAeKdt_hbUaasENIfJCCsOZ3v3LTtXLKNWg1a3QxSkeUKhLBqnZ4RYKkfw-A1wlLvOm0tC0rNGpKfYJlhwbs2OJRTEooMpith0B4yAIjp-DE330pl9gj5uWf7wnzPjTUGtGAgVgSrhmsdICsuL6sXCULNesIjJZfxjfUD5oG_TrB5VY7_4Y65yX5BcrBvcc346BCuaqKkj_2E3no6nufawsMItcmPVCTVFltqJbg87NSAg5xiyoTV38lsSfRZl8lBHQemqAi0t4imkit5nox7yFbrJEV4lttTF73B4JuxRK6zbzPrNd4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JApLnfQnSWYdZnBRgt-iV72CD5Ry4e5z7ajhOeORylerm1rtV7NvQfSZcAUE4oVs9uxEoqal9oML9e62xK_uOf_lXa4FRXWDW_FZSLI-KMUEkdCJEqmER92MJzMZfXEEPPD5wImYIWJJtCMjtjBs_FVPW2294rd_ESM4QZUVi_5ZwmkHMmtJszVIcnxFnwIjBEMe-eJIaas77rv3WGYGwhQXHKvJLmowXfJ7RwJNlkjCmlvuchb4jaIUOhgUaaBmiCohAxFlOLWFYYou9vQyyWf7zwLJnxuvN0YdUjHcwU6xBvpvecfELwystZ2fgavv93s81pIk-xSxrOn20TTOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThzOEO8dWWjAVmJBydYbNcpsuH9GPUJvEn8EkM-i1p_29qb8br_cbeE2joqTk5io6q_Hl09LOYo_ki_4NJS0SxxyE5hxgGRWaBfiky8AG88w1Qlk-pjiMClV3EQxa8IIgMUBfUa23QQpyDohnBCnC8VNV3ojW9dNpQa0LY13kfMqx5j27q0cs6ZzgC8B5JU6F6J0_ie_jmc-Wm6Jebbvvz4IlCvypPm_zNhaeXhVP8osg2MXztgec1gA77VN4GBRXg8G-vKc591xeTkcuG2GMpgCyIayXcuEFDi41280OBXjAETmuUdexFDynXqZb7VceO_xHVZ3Ef2yttZQJ78_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQbe38C1b_JLnMcKmDx6bGVByeU-Fm5w3a4R3hHpR9xr9c6zjp8tSUxnAZx9qApPv44FROTZpq4EaGOi4jwAMOrAQIMJDuwKxetmFeVaD89_rZwKlmFVVl0zoyfCU5uWL3tD5ivModp18CdOxRKgs7d4Yl3sfS8CCvYRqzl8yRgMPPR0cilhltGZ03_NqP_FPacd1ObzIKF3dODtlh5Xxu_XEjthCntsFWhnJrL0ToVywSd0AEDIYhqh4sDCqMfL4Umu3JHhfTOtf7RyqvVwDe78Zza03vQOJdOEKnYNBDrSwfzOJ2TtxDyE2WvFgpv8ObmtXkYuNP9bSZLAwDlRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-fKR9yms4t8ob8FxiTj_TXbJXgXR13Z1nIlbXj3_xbIY5H608e3SwrDqSAL2Qd72y2CgAXf6Sy23lTZz7mMwL9ViAvI23MFn0pQbbStFN8-fSxIhhE0M59L6aqD-LW1KIN4uxhlnpQyEmJ-l7CUxU1dT08LdJe8oZn1JX30dRCthZeUB4G2l5HI1dwS5eDLZJmmvbWCSYKMA9JbQONPLoW0bjsHg46Rc61OgeyTJ8IZzaRecTgwKu60L9GToRKCgJ-3n760-oybDUo_xrNc4UXy1-8YL1rq4EjNcADzkwVVr2JE2Hwn3fCNCDIfqgg6oMm5Exk08qGTUSXJJHF2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=lXJoSYd0R75XDdo6r-u86uSagQGWfKf0hRGm7dpCStV-MMpBFH25PotD_F0kANLHDNpXXTrAyNWAvsAIqgwBQjLucmhgwRvwXIWyxYRnio1ioaN_G59KHV3vLVkLYm3axxEFGnaaK_HPRB-lZDSrKORqiAXaZzkUN0HIDhFIuFyGnZIgDxPrC5gUeL5A7g70xLFYYnNtIYZkZbLRLzWq9BCR-f1WwQpGrnEExL5tx8tSRuIFTg5Zu4-psXCRxOBIzbYJ7ZEg_FPvXz7dFQfESWjGTnGQmW4pLMj7d9jGTFq7kKQfWSJPLGjWYWGtnphpgRDZaqH9FBIRxrgB_OPLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=lXJoSYd0R75XDdo6r-u86uSagQGWfKf0hRGm7dpCStV-MMpBFH25PotD_F0kANLHDNpXXTrAyNWAvsAIqgwBQjLucmhgwRvwXIWyxYRnio1ioaN_G59KHV3vLVkLYm3axxEFGnaaK_HPRB-lZDSrKORqiAXaZzkUN0HIDhFIuFyGnZIgDxPrC5gUeL5A7g70xLFYYnNtIYZkZbLRLzWq9BCR-f1WwQpGrnEExL5tx8tSRuIFTg5Zu4-psXCRxOBIzbYJ7ZEg_FPvXz7dFQfESWjGTnGQmW4pLMj7d9jGTFq7kKQfWSJPLGjWYWGtnphpgRDZaqH9FBIRxrgB_OPLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5gswZDb8_H40fpFGWC09U_vANcpA5_tArJX-FZ47Y02TcL_K58PhfANImWIe03E_M7CcB-_8BeTR5tKUMqNWAMum-agbo9_KagLnaD5a55uuRn4YrohwlFSGzxajK_kFdmUTFl4qbCTYp8xe6QBaERtubl_QB7QeIsmFFlPQTitX3yNfFcMxbo7ysNe6RpIElcF9ZLe_N1d-6EaqAF0KR72RyTSV1WJmo7qSBnA21YUg3goVWEHWq57goxFFIOIdGPXWdwCgSM826G93AQWyV0yK2iiXy4TuWI2yHRiQ9Bh_jf6lVQd-S8brCU6lVD9d0ctYRVD2lly7XBKViQILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajk-l9Nrkkc5GFAn2Sv_75ope-09mM4SxJ54oNyy8n5jeQ-k6uP4HE7o6VwgZJJohVjbuEySqpIYWY9FB3ouqSYnW_V0ipQrLif5zv2qq4CqlbpwdDtfX_SCOCBgxrvLEhDkqciOQeNmTjMM7cGLcKYQW2LyTk9ZuYh3O44_JjYaoIQem8mq0fLK57EjIX1r9qCKHWao4syEhOIgLRQkQV2Hv-F_xKSNsLmrXJYPdjjJ9sbBdn8d4prBs43nhwaqyfH3BqvoKtXnvxVDJFzlVFvdEZb0Dah0YmK9d0XYNN5z_UH1VBG-JtaHh0vHLg_4-cpEHymR_o026n7OcQ8brw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxFlmoVLukn3FPOfMT141oN6gGWMULnpdaDRiG0QkuRiD9aO8EU9ANEai0dScZ6WQdb9_mUNhjWJQ7oYDEiuojo-uD8X4dzL36LmH4jkLpiIasz2Q65kYa4FQ60ja4s8zjy0k4dxFBnrbiUXoLJksbVLVHFBav8WTeOEa0bjBwH08Yo_GHltBhTiU6pAtyVDcvrm3d0AcIU5ZM-GiOfS4gi5PoIshw5BKJo_THvSVNoOWDw0VCPypUwzDSYXvaFgkzUT27q3MVc6RnZVLAjDkgum2dqqt_HmMFGzMPfis2SR4_2ujYaVz4Xbo4AWXQyJimxz5F899IvxlmRZIRlVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=jPnpF0LEfC3rb2y_30LPtJDUmzpdmmcmSqP5yIrtpiQS7xsJQuzkTsdQChIpl6PNuGZ4R5XF9sCHqyLukTo_jQ78gKXBCOE6wcQcstpMfaOOyhIg8e6o5WT-h5HtVyLjFzY0-b1P7nLHml4Xkbx9pjqhVUx3bkTE3x_f94SMTEN2Kr6A0SECQhmhReUGi4RcVDzxdCWSMHxIfWx38MtvWapGQnWFuxSLsDuqFTt6qiTL69A0QZlUnt0tC0OCmCzReLEje74-Bw5gdGyOix54LFAScg0WnR7fRDyMEEwgKwArToTwqw_TgO9bRa7h8hVBinBjeud7-CoJ68i_gYWXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=jPnpF0LEfC3rb2y_30LPtJDUmzpdmmcmSqP5yIrtpiQS7xsJQuzkTsdQChIpl6PNuGZ4R5XF9sCHqyLukTo_jQ78gKXBCOE6wcQcstpMfaOOyhIg8e6o5WT-h5HtVyLjFzY0-b1P7nLHml4Xkbx9pjqhVUx3bkTE3x_f94SMTEN2Kr6A0SECQhmhReUGi4RcVDzxdCWSMHxIfWx38MtvWapGQnWFuxSLsDuqFTt6qiTL69A0QZlUnt0tC0OCmCzReLEje74-Bw5gdGyOix54LFAScg0WnR7fRDyMEEwgKwArToTwqw_TgO9bRa7h8hVBinBjeud7-CoJ68i_gYWXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIhWv4Grfy2KLWOGPH33yvLFYDXiUYkL5T7zm2wAgj7EjM8rm_RxlTLbtBdAHBbKDoSz82fmnaufbMWJXIUFznp6HdlWW7bXY_VhjSwduppbNKVdgKduXxagekPXE5AhcnKyP1r_tsBIo1wi6wgLxjpyxSHEV8JDpInV5rvBFZO2W3oqxyzToOddQqqawgtrrWuGHCUojMvIqE8yobHG73iztKGGnXR9_xIILDduJCZmPBfzQEsJ4sladAVzpsadVyHd3TFSxmXeZNoU2woYUPIuweRnVi0tZcKgZV3FR_qzd4biVPjPUtXctzNWiEOJmLCG5gbdQliXpqhyMee2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgA39_mpZBJhqAsb0rcrTU5Zl5b3hGwHA7XS-q7xiulG0hBTZwEQ4zSsnlXGu05sVjZcXsVW7nEuS5LhslhQaCJZNAWlVJwW5R2etDOfCWXASgZh7O_hwvt3ZqKWPAACAIOGKXTNtPMP3qHgqMyOkKbvSA3MeNKZ2ai_CoisCHL7-UKZzoS1-6yNSKUD33UMpvLT93aZsy21pOLXmfyfuzfEXaYKUNHrDUpl9kxgSK_tNTqmzZ1sJW2j4KYIF1zfZuBpXm-Zgl55gRZeAjqkTL2nyhrvX0fy_yN-vLf7RCu4oDtIEBtFfe672yOXPhCXAwIvw579bP0eXVi9_hu4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwCC13xiDJ5ANKx1u98nwYiT2uMZdiTuI0qL2n6f0GQIyDP29iOJCUTWUPnr7ICQcDhLqKtVOexW-1dygKO1bHhV8RoMXsqGQ8OwaSiaoatQBwnA7V_OYUmF0fhijdnmBy3WDjMWs0gqyh7yQpQ58ckgwF1QJ_gy_Wu0sPIz1Y8dXfrxpz4shPU5JNOPoen1tkHqf7qqhltJLHqDTh0SR_i23zNzAQ3gTRuhPy617ShVr2_WuFFrO1Y6MXcFjkUKFvEQ48TVpfuZN3J3AUZRf2CD35xeo-S4ACSHU9xdl0iGgnoaZIHUPhnDJ-hzfndiuTBVjr3S5wRl3nRQOZf-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=UUrPEMK52wl4iHJM0ybSvdTc8ylrEacBywpriih2Pgl5E7_kMB-ylzkl_d6Z8luvbiV7B6H9eYkD9DGRHehzH7r0MyyVP_wc4pZJ7B4f7UNK-E4E_8lJmBHNG3Cdc3U23qa63BYP2JbE11t9JoarUUXIrQ6piWIyF5Ik7dYKB54yAUG07IBpLtRkqw0PynKLyS7imieEhLaw6-zbJJ58zIls8jjk_xOJBd4PT-4X1x1RT7s8nv0xyMnW1GND-6WDbHaoNHHKt1yzX9amxB_uNlGatEiOUmR4VI2AUUoOx5req1A3GmFI3T6nsa4040ELIwTPwe9EvJPh1lSSbSnMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=UUrPEMK52wl4iHJM0ybSvdTc8ylrEacBywpriih2Pgl5E7_kMB-ylzkl_d6Z8luvbiV7B6H9eYkD9DGRHehzH7r0MyyVP_wc4pZJ7B4f7UNK-E4E_8lJmBHNG3Cdc3U23qa63BYP2JbE11t9JoarUUXIrQ6piWIyF5Ik7dYKB54yAUG07IBpLtRkqw0PynKLyS7imieEhLaw6-zbJJ58zIls8jjk_xOJBd4PT-4X1x1RT7s8nv0xyMnW1GND-6WDbHaoNHHKt1yzX9amxB_uNlGatEiOUmR4VI2AUUoOx5req1A3GmFI3T6nsa4040ELIwTPwe9EvJPh1lSSbSnMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyg4LZu4p17wugoVa_Tt8e6NlJmDe4V0jHfAPYSEhfzSbOOimTjq4nBxWhJsGMRpGKNuh1At1bjvS2FzMkdW9VTad721ObWVsOeZJ0LJKfq8Z6WyUdHueCmhOpMYZ4mCzHJeG2rC-68JxrH0p031v1uvifWWNgt9CvByQ2310pLF7p2jVU9mHQTPz29oj7a0Zk8zNsBjXNiRZ1xudPjjaK-7SLkZOE7-_JU91iZVXuv2hn7PtOWta5FfV2sbBigslKdAK0LVpdWJrwVDHdXNkv9FJ2bzs5imByZzASyoA0gpuXkCGZpVtgSUcHqaDnx-dItMLrQwqCQK98-xTaQeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-7iQzAvLC9FaONHj8uMzlNzCXJHI3z0D6LGqFe5x0OqXpV48C5ZA6pt9cop9QnMoOwjKphQ2P_Y1K_78RbcpE67PY9Rc5uyDkxA_6xGtk-KYv7_L_S6wIz1gLvRIaZ9w1W5uao0M3UJDlEw_0AxK11cc9SFf7ox1rZWscpaJJu0_0v7k_o6lB1MrkM1WQrspDtrhd9BMiw9BH22zyQfVqqRYO8FpCsJ5gCmnqujaUr_gA4TUI7j6xiZT_I9y1XNnvRR1mzkbxrXVUHDst5zhw9dLq5Fu7FHF4weQGvCM2RtmGA-Yy2D-NTHzClR4s7f2pzN6zfsytbPdppBYVc9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/muFqhUgz2MD69sqMGmB3C0BTolic4wbHk7PCou5eF3yhJEnewTzeN1FFhdVL0heShnk7pLBgnRxQLe_4BTbtskJay6LJDW4Xtmg7m3IyY-UiY3JxTbJTSTMn8qjc_BqX4_dgg3KDmui3rv9UtQyfSaVI46p0DSfk1WX1ipklSmjt_lLVhF9kDw29qmD684GKHqK_QEvp5l2QAsvQ_iQhBBV_L1K2I_zMU0VxXSgHYRcvzT_ZR4hDvPd52k1eIPX2cLHzU-N3xqQPHhSrF9pPxqZLeulyuxSqBOFP1omi0HImZU_gQIVnhR2h1DqSUKiSRHzSBo-Yr9Xcql_DXQhxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوووق جذااااب
سوئیس
و
بوسنی
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6ZsJLNEQrNQYXeP4fI-oL1XndMTl7bPKiHR0yL_z0XhaiH5m9R-OeRvP0jkgIxkbtfrPBAvjAOHWRc9V1fdOxqVILlWkK9LlrSeOCiMHlRLV57lXhExosPkHVta6ibfVbEnz2VvTbR6opNhVdseGtv3upZYLIcKPWjbnrpZ56Smt9YhwKphaXWD15QBjhk2L5NttaKnW80b9fwoH-2CwPDiFk804vfKhcMnWC28yPKQLlQEybCBoYVrd8V05W1SM1BriPR5BUMSR_di80gG1gMk0wdgw9D4lnh3wciUiwVF5d0ru9vKIOj8A-QKh77IXxUZFpb7i7w5nByu6a2uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Xc1Vw2e-NIs0eqbzHD3DODQUxYKeMl7dqydW71osdUtJfLBwBpQ4T6zMauOwLG8k-pxHxT50KSwMfMUBfL9qptAJ1CgWngNwHXDWZ54NoFaoN5ZUGR-LE1R9Rk4faYShBNYqp7vG3imcJRjuYJ5R9jap9Gt30w82EMoRCeJbpjX0qkDoWm_MuLzjL38Nr5z7WXqdrFepHFPmfxzdhmEGXatoP6vnNlUFxhZOpaNOKYJYe1TDHlSj7dcWZoD0M1YvtZfDtrd_0aCFZzS7ikhO0nIZRfAS7jvsczz_4VbRF-XLDu8o7DflQwY_gi2NEkLnisVG2img01OSS-qZtHakeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Xc1Vw2e-NIs0eqbzHD3DODQUxYKeMl7dqydW71osdUtJfLBwBpQ4T6zMauOwLG8k-pxHxT50KSwMfMUBfL9qptAJ1CgWngNwHXDWZ54NoFaoN5ZUGR-LE1R9Rk4faYShBNYqp7vG3imcJRjuYJ5R9jap9Gt30w82EMoRCeJbpjX0qkDoWm_MuLzjL38Nr5z7WXqdrFepHFPmfxzdhmEGXatoP6vnNlUFxhZOpaNOKYJYe1TDHlSj7dcWZoD0M1YvtZfDtrd_0aCFZzS7ikhO0nIZRfAS7jvsczz_4VbRF-XLDu8o7DflQwY_gi2NEkLnisVG2img01OSS-qZtHakeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=O8d38wAJyqAhRWlaBzh2wE47ltrShuYHTL24kiGg-AJAq3w__vlBf-bwns6y08wFW5vTWPY7vTwkIt1mlCYS6-wipjHGBtK5g37BaV-ONVCWgZREXsN3GLYRfXfqlB7xhtjMDV7fXc3ow-2mmZk3tm3shcyrA19kfXlLdAI7A0zEnhvzoMzCLQx7YgpieYnBg4s54pwl4GVE0AFaPDlaxvjwkERGr7aWGMkD6r7V76yE61PFcxyEi6YNA8PkqsaUaosic6Pkn-lmqDI8TFGWbVkqHrDLexeh7FGc3cVZgX0nol76s_zd_2w6tb7UqlzzCEZod8Bei9m08HXUantVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=O8d38wAJyqAhRWlaBzh2wE47ltrShuYHTL24kiGg-AJAq3w__vlBf-bwns6y08wFW5vTWPY7vTwkIt1mlCYS6-wipjHGBtK5g37BaV-ONVCWgZREXsN3GLYRfXfqlB7xhtjMDV7fXc3ow-2mmZk3tm3shcyrA19kfXlLdAI7A0zEnhvzoMzCLQx7YgpieYnBg4s54pwl4GVE0AFaPDlaxvjwkERGr7aWGMkD6r7V76yE61PFcxyEi6YNA8PkqsaUaosic6Pkn-lmqDI8TFGWbVkqHrDLexeh7FGc3cVZgX0nol76s_zd_2w6tb7UqlzzCEZod8Bei9m08HXUantVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=q63Js_BPnDnRpSs-cOhLCFW4tz9c3g0xOYPIZblGeFS911JFOyScRpgYIi-hpCjmLvCwbEjddmq-VsSWVYU5Q75B-_sTr36DwKIvCVseFUgf_QIGXc-cY4ZrTrXzfdO53WixGdTLkst6e-tyhyWR2tBGn6VDEEdYVRmXMtKdLElK2rgZX7faUuRGs3rJh_JGagBOSJHTuW_eEndMtSXwCvrdRwaDKZUa8EAFUn3_RLM4N-2i4JgNzMyGm1RgLWmFqopiRDVI5_f2MVnA8gOiUNW8pQjHuhlL0Dz28K3_hzhTOr6QHYRgD_njXEstPCHmIzvvhiFFKBR17tCJEl3yIb4BAB7RWI6EawaykeXkmQBEJmX3wzKnfxZ8z6yozMmsIqzyl7TcUevkopGM5SLyYCByWAnLh9z9rmQrOPyIy0CyCFjsilt2TimeDtgm_MHvT8sjj9UjFcH4pUkLOfe_G-_Mn2XHhu5yXKW5d-23DUvFTLuYlhzDk7G9h2enOhacCrapAVE5U89IUaVQR-RD-Llm42Wp09GSdB4xgnUV4ePeKQAtCjc7K26d9zjcstpX8Epxrz0qOo5raMw7LXEpHug6xPva62hoggal4zRcTZPcV__eGguJ7zvZUc1xcFgEngWz5Wl5yYYRjDbjFvXojJh8jiqL02G0NNGyb7t8BPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=q63Js_BPnDnRpSs-cOhLCFW4tz9c3g0xOYPIZblGeFS911JFOyScRpgYIi-hpCjmLvCwbEjddmq-VsSWVYU5Q75B-_sTr36DwKIvCVseFUgf_QIGXc-cY4ZrTrXzfdO53WixGdTLkst6e-tyhyWR2tBGn6VDEEdYVRmXMtKdLElK2rgZX7faUuRGs3rJh_JGagBOSJHTuW_eEndMtSXwCvrdRwaDKZUa8EAFUn3_RLM4N-2i4JgNzMyGm1RgLWmFqopiRDVI5_f2MVnA8gOiUNW8pQjHuhlL0Dz28K3_hzhTOr6QHYRgD_njXEstPCHmIzvvhiFFKBR17tCJEl3yIb4BAB7RWI6EawaykeXkmQBEJmX3wzKnfxZ8z6yozMmsIqzyl7TcUevkopGM5SLyYCByWAnLh9z9rmQrOPyIy0CyCFjsilt2TimeDtgm_MHvT8sjj9UjFcH4pUkLOfe_G-_Mn2XHhu5yXKW5d-23DUvFTLuYlhzDk7G9h2enOhacCrapAVE5U89IUaVQR-RD-Llm42Wp09GSdB4xgnUV4ePeKQAtCjc7K26d9zjcstpX8Epxrz0qOo5raMw7LXEpHug6xPva62hoggal4zRcTZPcV__eGguJ7zvZUc1xcFgEngWz5Wl5yYYRjDbjFvXojJh8jiqL02G0NNGyb7t8BPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8XhYfdKzyI0EpXhoy74ksE4GUjjIv5hc9VfyRNncp9dT0KUw4qsi19k-OsVMFX1w_GBmwpE6YZL3YqJPrE2BqntsvK_v0TVi0yoKsmX2t8wnETo0jWAcxg7dHHoGsXr7ZkAD1INyWEr-tPEip-Kjs6eQ3LMsun1YgtceR3pVT2RYPlmEBuleFJctKLihs07LJr_DaWlSxJ7-IS-hH2RV8yC86mBa44309NOaUn3y3fIjQ3G8CXvEeBWZRSZd8d-20i429UWiqxWETL8IcWywa5Sx6YDUaJZIXu0Exw7pb8mzYwuvgv8Z-YfCU7GoJHBC_6E601J-_8Yp8WtX3tQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOAqdNHMJrp97NOkPD6MqfHtdU_Unx3esDEJjF2JVGt_65h6xruhY76Z4bSUfzMYSruvL610oJjM9DMRA1AEPRzM4DE37V7gy05aQglu14m8LachlVPf31QdH6j4mw7nZC4Kwpdo7O4lt3sB1olGRPKPsAl5VRqHI93jrRggB3ZHg4IOP7TbxgauCUTmunAiHxGERyVHruNP4_yDArEwSxVMePgBdfEWQmJBMHjir8vRVNUeyJTd2ZtwYDnVEdLM_zJPWa5otv1QPJ1AReiLUXaH7Ye8m6o-VxHPKXmg3rcPVq0j9Qr-4dTr8nwUdRrqeADcFZ2AAg0Ix_AZI010nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsgrUmV4aJ01PPjQOiMlRc46w8Mc-4oY1xAh7eRTPui8OtVkMTJUs5Uev9CxJ28pYWQdWSgUnEXDlL_LUVsyZ9TaxY7pBAkr6529SelnhAmG_sQgKxZUx7ItLIvKxyX0m386HQIJzPnUNe9ZpISCI38_l17rAPNOMMnNu95F_caOPid4xCIPeLGQ10feiOR5zAcREs0BzfVkAVzZprbrBWcqeGBObGw1pyJoSSG6xlwHroHofvjPYRHsp4MvZZocDp7GS7N8i8ffK2SYxDhCtt7gckzjHVGFn5lI7FT7RSwI3b-H6FWarKCXH0UhU3YQxPB37dXVuMf3wUZTDJojcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KS1EcFKiDIh55_qm287Lz-iMY82tbXw2o_uP0OcDmf6rdWv_mwmWNTtm-pjPxvSnZxoY6i5JL5kFDpWNbInLkhyG06ZyTlmM4oOsFxgPansR4YRuyrXVvLh_0DSEYKndWCAyUZanZP-m4AT-GsIz4fiB4SQzoaiT7uOB0elzNxA8Gpeay0qCNTSeCGguE-bnck2HvKwdFeI0Ex6FoUbpmUnRLv1Hi6o-qZ12yzjOnDcpXTzyMZ1eIGgqz2p8981MYoLnvTO6l3-u3SkiORXpTpScKqDl1-GFC9SZdHz-IfjmPQt6JD11Rh2OtKgTGwL-l-zF-DQ8UnrT-2w5txZ-jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO5jqx6NPD0oCnUZcVpc1kRnrkhUElno6wyL4k_dfiaTZmjOkmlxZETiyz2cy4d2NL66aLLvEgKv6zOEBAr1AsK4zOUxtt8irjd77NEujzTYe1GrhLx2yTlPofZPs6N9QLw3d5uv22ZVKDn9uSMVBJA2RtjV-HdDOMGV2XGkfAM_AcMVdpHsZzjvTJ_q2V7Z4zXWh8Z-Q3NBiJ_1zUbxTP7W7UZVoZiJSgoj7Lo2EThTy9SYpGheFthT9Gnb7Rbi7ECZfVitrTkVlElMzr5RLMn5Dpn2B0z7WqsnINUbFo2aKNZjBlahQlLJ3DtRG90CCV2wOrQY7ZRI-58YHUGi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0LFRcBIYIAOnhx-qVDX5pc3zbe55eDvwN0pNnpw2ZU9VTnCPi4eNHAIdO-LcZK3e4gzXAkRLIU5gAyWWf1jkyHSeRZBtv4VwkpSyYaLjQkq3XgzXPm3Jvzk7i21rRFIIqK0PNruf7t-xiNqdtTaEBbvo-JcdLSSGiE2V1o3ouHa5RYe2QoPur4PuuACdWMIRifPI3PQJzunReYvXfbjijOwAhh0Xr_APcWQ1pg4rGpKaS963T477-OUJ9B8LfuvNnNtU9N_XYXVPYU0S8IjuyG2E6I8kA9yRaRcwjNxvrf2daMk1MXfgoQM-UQ7le-gobZy1mglFUb2oMtJ8IrLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7-_def8oVEWvbygXSxBdJp6H55zOjiOLMJV7Q1b7h2Q0J9KhwOA17Nal16Wy-iBAP8YFPcxjJIkdYid-CsQWHYll4PuOG8CGYwldjrJKzuqINmSu8_HSmnc-Bmiu4vsY5_srnXq8sPyzFpxByard6sYmqzHA1alnmEXDImMOhL6d5lfLgA_Piq0MCLfrKBorvRBYSYoMCvad-va9ZEtu4C7vubObk1ZJFWaWxD3Wmic8FsWyHizRhSK3NGqCTIzmpiJH6Cr8hqrX6Qd-RnN1T8003g_kiOlxeABDYoRGv7VkE8DvRMH9-0gogkzLTqPlbqXDA0jAGq1J4yIX7eA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBnvpo-c-IxT-QoZzf1LOlO8AejDx4TsefRfcUBIbrPpGUSU4Z4jMS9YtLN3vjNtoamlnvDl9GsiTEXyaqs5uZWzE_GC84qLt1orBY10sEf1pJoS3u2KFlQJ1UHe60hHRYP5Esk6cGYbfXAjwr4kuPaIUUTpKgO-cLxYYBzTkAVQ_sCiOoPJj9KLlcRf4zjqvwCKNRR2Vd6iC-QExskInaHWc4eciIyXOtdDDK0JTavP2M-Pht8RJeLSkXEwOm5smlTNUWsYf_xnX4SVcEq7MAgKEDiVCPjTBdAVOogqBJc0ort_WXwmR2-b3vUSAqpnSWbpn3cRv8AMELGIgksZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=iqopkomDnT4sv0pD_C6OkX3QUa7U7JDmLKoNO-woKmoEC9Vtct5Non3n1S6Z5nnrbxMa50gbfUxLImXq_awKvFnrIUhdsF7kM_sdZ-WXEVLf3FphL-8EN3Fz68NQgQxclLawjIh-W2A0KfDsdiIFQlo1H_CpitL9xq7VwEJh-97tnqbjQH40KQNSnAP33AOC_C4T4tGNGllw1-yGa_7NeVZPhPoCJl9EosKNlWHjHx7TpKXO4oVJtJimWumqoIUFW6f6VLYGW4HvIpmY_eF4gRAdxKwmkaSHph2oG8UZsXeGDSWkUxbTSKm9ccC5L9EJJf4_s-oqHUceG_IkB8OxGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=iqopkomDnT4sv0pD_C6OkX3QUa7U7JDmLKoNO-woKmoEC9Vtct5Non3n1S6Z5nnrbxMa50gbfUxLImXq_awKvFnrIUhdsF7kM_sdZ-WXEVLf3FphL-8EN3Fz68NQgQxclLawjIh-W2A0KfDsdiIFQlo1H_CpitL9xq7VwEJh-97tnqbjQH40KQNSnAP33AOC_C4T4tGNGllw1-yGa_7NeVZPhPoCJl9EosKNlWHjHx7TpKXO4oVJtJimWumqoIUFW6f6VLYGW4HvIpmY_eF4gRAdxKwmkaSHph2oG8UZsXeGDSWkUxbTSKm9ccC5L9EJJf4_s-oqHUceG_IkB8OxGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=j5hh-loNKqz2scjZ1SL870tkIVIEC_3R_V0W9-PbZ82vqypX2IuS4cJph3w-joSo9WebipUUIdK95IhbJ3ASLd6RlGWPUbMHgfhgSACkFcxudKmvhwFUJkBIu5yZ8MjyYGi6uyw0XrQY_xFMEXhiBheddBe3AUrefzbd4IwRqe2iAjtt5fQ1uwusPo_V7KY2Aqx0OrHRj9BmU88UZ8NOk06AhPu0of1SIDaYqFd87e5-dF0YJFpgpj3LzPftJAF4odFMnWpsNeVQO7PxwydJZprcyf5cWPDIzqrKXeqQzH7Fh5UmW9-o8VdEmclbQojOh5dI8NgH9x--KOuJljJoJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=j5hh-loNKqz2scjZ1SL870tkIVIEC_3R_V0W9-PbZ82vqypX2IuS4cJph3w-joSo9WebipUUIdK95IhbJ3ASLd6RlGWPUbMHgfhgSACkFcxudKmvhwFUJkBIu5yZ8MjyYGi6uyw0XrQY_xFMEXhiBheddBe3AUrefzbd4IwRqe2iAjtt5fQ1uwusPo_V7KY2Aqx0OrHRj9BmU88UZ8NOk06AhPu0of1SIDaYqFd87e5-dF0YJFpgpj3LzPftJAF4odFMnWpsNeVQO7PxwydJZprcyf5cWPDIzqrKXeqQzH7Fh5UmW9-o8VdEmclbQojOh5dI8NgH9x--KOuJljJoJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uba2sHVktDqvO2wRrCS-RCLaA5U5iBcHUMiIra0BlFUGJisprlFB1Qbd0iBeahKX9js0r6drukk_vJWRopDoSlcgiKEwVJdOb6uqAPTiXrIwaBnOtIA2bMAhyOe5zlYxPDc2vELGziHn_W3PT19CEIWcNZvbHuH66jherCKz50WsWQPmzZY1M4Y_UWMNtFx5TzHO6iSFfamsK-nZlak4vqvbek6RJPgdLr1J-Ujk4deEd9LnTwYaMvnG8EN6Qg2EMgGLny56_Iuu3Lkvi1MJF2_K9C2OxqweUMLOJYe63Qm2B_j4s1RV8eY2jvOsMcehkXOaSSGsirM3z0mKCXRc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=s_11SgquvUTcgMT7sZDLdku-JYfcpkTthyWPGKtsDKQ1qIadkRipwAqCax5XhDH53jae6BpGb5kPVouH4eI1TJo4lG2mfyijWKMGURlX6YYhTc6ac482zRtYZR-SmzdorWyOMbX-_7tRRM7Tq9skDYlN5kRsbllXvbYm7ui14p48GaV6-ICuZfAFDHx5wTIRQqk-3contMdFPj_uV8RUbD9-PAHGVqO9sDZAI3uFGpP3BNgvPCzXfQhDl7uSK8vwQih9M6MrP9pe1tAVmFB2ItSdSZ1NeZtPpwqgep7MQD5D4xRGaaRO2eDBClH5GmKhgbooC9vEt6UUHTQ1HRA1bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=s_11SgquvUTcgMT7sZDLdku-JYfcpkTthyWPGKtsDKQ1qIadkRipwAqCax5XhDH53jae6BpGb5kPVouH4eI1TJo4lG2mfyijWKMGURlX6YYhTc6ac482zRtYZR-SmzdorWyOMbX-_7tRRM7Tq9skDYlN5kRsbllXvbYm7ui14p48GaV6-ICuZfAFDHx5wTIRQqk-3contMdFPj_uV8RUbD9-PAHGVqO9sDZAI3uFGpP3BNgvPCzXfQhDl7uSK8vwQih9M6MrP9pe1tAVmFB2ItSdSZ1NeZtPpwqgep7MQD5D4xRGaaRO2eDBClH5GmKhgbooC9vEt6UUHTQ1HRA1bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ5PnC_jIgrNyayAuWD4MVuJBYMkmgzdzra3eFuODUJ3k3HU42_LJhcvxX80YdoZ9pHUNGMQy84xyX9Nrm_ZsF8nwRUUA57jP_LCx1pOCDmz-ByBnCOgJgm4iX-xQkJCEPiDAi6FZMaVQTK7sf2CYeLyeYZLVbs7QjsW6LyoUyOhn85L0geo01w-XJwDH3IQQSkleVn6nezfaYQTOYBkBvBw7fh-rcUErGTqJ9xvPHhvWYOsguqvMLINDErna4V3jyeSCSKIG30ZfEvg3XhSjgkzErmvO28u0TxgVJA213n76l-qcY7SDpVUbsP7MEGn5OLO27ATh1fKAUGgf07m7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvDty0vuNO3IDHm-hvNHLqjnXqGn8R0Q5FF79ur13skTfcL27OQomETgQ3g3LDQ0UCXd7n2RwX9x7kU05KLJ25o8UeEqzNnLBVVGafLKvDHlGzlT4SWJ99gwTUxxClXT1SJrLpN40Nfa2C8lr6F2O7-Szp39y3T0rfOgvYfVhj6q1qlDe-cQ8oJ6YHYE9aMCUty7Y48I3uhVUZGCJi6BmCCVBbjKu3CyELHldxmlyM3JSwDHPsk_t43sxD95uCrOsy-audlu4-D_8pa4sfF-LgwHDkQkzPNhLBEwbcw1DcjDvaw1lvD6BNVsMZ_0mTU17jso1u9ZnghtfUbzIozakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE0DKaHzyO_Tpa4FavvleULdeFM9fm37laloQjX-gOUuJrdYISQakBsMlw69kzShdQYH1aPLENshSKiqhqjvXgYeOCEx7hwAVbbCSjqMfd7sb0pGVTn19DKwhy-elcdY5XeaS8wQAAmV-xlAer7P8OCWDSZG5Ev5o1MUlJdmPh9VZyWfE4kgNfc_va7k8vul79526zEDVYA6QdRk5fOulUtNfQS0wGs5V3D-EZBEDCzdzRTuFEHdaZjxxwg3mV8CoTX1IClO3LQYqCVIfHmL4WmY88TnPDqmLnhg4ynGTlFFGEPImZpkw-O_y3TrJ3jWaxrWpGxpb-i844vsnHKu4lv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE0DKaHzyO_Tpa4FavvleULdeFM9fm37laloQjX-gOUuJrdYISQakBsMlw69kzShdQYH1aPLENshSKiqhqjvXgYeOCEx7hwAVbbCSjqMfd7sb0pGVTn19DKwhy-elcdY5XeaS8wQAAmV-xlAer7P8OCWDSZG5Ev5o1MUlJdmPh9VZyWfE4kgNfc_va7k8vul79526zEDVYA6QdRk5fOulUtNfQS0wGs5V3D-EZBEDCzdzRTuFEHdaZjxxwg3mV8CoTX1IClO3LQYqCVIfHmL4WmY88TnPDqmLnhg4ynGTlFFGEPImZpkw-O_y3TrJ3jWaxrWpGxpb-i844vsnHKu4lv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc1lcr3ylWjvRVADmAR4m0pBJbeBwA2SmJLuw4BK2DXbMUqRXTFb_RvgfcYyL7cPGzrcH45_aRXlaEp6Syz6Tr-nFD5WsxPHTKb-s0mZvQtbTKe_tDj5j2H30_bMB4_dFsNfCKVIx1E-vKFZCQKFC8m9zcfiVCngmBYTN18iNOgZK0Ds-l4l3k-akg1bjw4OcnBxfcRVySyT9p3KQVr9_q9KddRwiEzADzCSrkCP03HQE3ZKI9v-4HH8cznRLcYoli4ncQupq0YkLpNJQFJZGq5fUOTE_vWs4wL1hQQdkYYTaUI1ToTgC0VsPJd-zE_QmuGTMq0OXI7UYGHalRZJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/roY4uu98CaAZP_P4kNrzgXsIIff2yKfWcTucDYKp2k9KSgjwGLuMm9Fb2ow8sk6J0ViNtTxPRJLDueC7G6WAahbfW99dwz1K7emIs0iav5I1vBdAJUoIiHeE3Xhzh3cg_DbCMsbQ-BhvybMyoxQdl5RZLOD-IpshGklEeqIS_HjWmcRI3rNpsFJwtQvzOB2uFr4c3u-E8xc2FIri34GXvPDE_rTCCY6L7EvumNXXgROG2B9MIBzZAK0u87DoKZQi73q3dhVma2bb1D7n8lgjgMSvXuuMpbMOkvuJJWl771UR3Yi7Nn0wZQXh0TFnjmGqEAm999xT0zdC8SsP7FSE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/POi3NkxuPRhCuDM8VDMkCKGafKcLNEYiWZ8Vw7SqjTLaKqv3726-Z-0PkVqHd0V0lzR43RztAXs7DGqLZqLWPR6-_SDjxOO3BroskvZla1uSqPKoUR66FcI3QEnwIEDTKoC4TcjaK4Khg6G_1Kk6kVWG6N0RMqzpg6oJrEIYXwvCp11wgi96HfjA5Oh3X4MvwPYCgLo_jr6rlrTAWmvlncc9aFCZakJ1cw9IB3mvYPNNCP86UbiAaQ0fXgm0JZkR-oF95bARoWmOfr7WT22-5Spzhj7K0jo_bGgGLGoHWQ8yQKMH2Ga2Iu30BznB7wsQdTj-1FyqWJDPYxQWT79P7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Mb4JZksCo-9wRixBnJ6VJURPHh-OVL20_o53ekGmZnYhBwXyIEDYVP3NptgH7Kbb8Jid8ddFI4IZkZEIYH8zITklV-aBx1odZ5I25OKPHbFs3zWvK9Bu-Dysxp8O-VdsPN38rAvKcEuj0fo1ZXEVUdibs9Z13xFmxirMM5B0Lcs7Znfyfq-g2TTQ5nnntfxiEgLfqSJ0374qhCKx9Ts2-9I9UihwNNQddOvAIA5NX1KaoibEGgIAMMvbFhprA9hq_YmvALrnuUa1QCmAVbvCwcgrdariJIPHRiQjQzgCW3_jMvZR4pVd9kJw6gL_4ZfANERSYVxzZbZzJunNq9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKQY6R2BfACK3DnI3wjhwgUrreKmwdIk9MBpI-HDkdbllosOubf1EfiOJzLhx_6rlqPrZ-fQqTE4QUzAmzPyQgejIT-z_IQ0eRoTrtn8ZZO_1pXX96e8Q59soi98UtqhiTJfL7DSRh7a2ZxMSbCUyY9M8URNg0wtWudCSE57efpyLEXEZ7f59mZ-vn2jD3yhPqC27KcWNWIMkFOIYKlzKj5_Sli8isUXf0Fqdw_jyWoF5Sf_Pu-1NLQP3W5w7iKY2kVAWbQgf3UNM6aok-ZK253yuB4QXSoQS3zrGgOSsudUzTSRlDCH7ixHdMj9lx8X-nYKSaKdfTFregvnNwOggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaRS39G5h3S1AvA867v5gCWGJurjInEqw93YyQbhd7kU2FE4K4pHvLSMSslsZBSNIrW18q-PsNDFB0wa2vzGyPeV7-t3Y2MLK1keiNncX3AnqLCtTH1BYSVDyUerjmlAiRTXSnhrzMZDvHqtY3RE3iXfPg5jkCfYu1e-30Eqsr_zSJa3edtFGCC9pkLPaFW_eNHpcRbf9WdLshs62nvmfvMluschPTjwuUE_mWeg9BQMJE4SYapS4wJXQ2uUKOoHgJGfhkSK1LBrNqvpU0waySN8v_7EvU6LxDkAd5tce-b4r-3AkqD0RLtXMY3-v0HUJSmidfHb15CO0XJT6-wA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbfaW6H7YWLHWeZQBNZsVo3WteF_IU_0ByEztxNSG5wc0Wc7OgKeo3m4hCB8cFKkC4Lnfyxl6EzqKj3n5VoBlRNlugEAF1JV4rxXppI8vrpXfSJqHSP1GexgHbOpWZNq6gTPDEwc7Vh29dqdTJyON1se24QC6zoK3c72OZl-Bv33ffAOIxMj34MhnGuDRbC_IN2g2_2gjhlXiBp10u_hWvEd2EAvovlmuixsaSa1HPPhqgwHdTHUJZtcZJu33nJ_4smcK4_b-rHIqmkwZeuSHgVzLJ-QAeJuw7-OmhB1z48hJEjSjObEaAYKAxMoVmmmjvC9zqdOs1uCTZnOW0dmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmvBDYCTMDjypU1VBHlewJzviKrLegSXWg9DUMwwngPmpZ9aFlvjSvjWPhCHokk7CsLvyumVEhEiiC8WcIZxw9zNNCpt3TaInNIlLxykKLehHWFLSs-aj9b3drbU4h4xI7VZkTKg2D7vImb9mLGvmApgZzsHJEibulqq13D4JHwsZmiFDgrPr-airaOrDZmWnNzvcX2a0tR9SxejLTDB_e3DSEEdBw7HGygOX970Ik3ulmIJAb0yds8iH9PQtT4_x0dhklTbjxeIIyUzOJnDmO6HGvyTUuSPBcVTDqOGRPuzXjP2Qouj2cF8cy10_NxM9-7z9JK3oLM7aXvzzgaskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cErvE9SpA_8s4D-j379iIH_hwHIWRhiOnFP2sNBxHmY4ElK18kzPP0tv50HX1-w-H3i8IC0W9AuRCLK1vTEULUfF_tEIicki6Kf8rRU0DpVRG5lMOjFaKf_g2hPFq8ocPOaBcto_29bUDCnocjUW_wSVwav_-nLDSIiTBNVmHZU427IL9L-5KKd7iBXD7kZPBgIqB6N8za3mHx0J8cLclq35ZoqdKczKa0e-vJY5wl_LyMYXQ_D0PrXlG7IpWL50nCIXqz6vcvWJT87BtMO80ikmafAJQWNAj8_oDeR9jGxJpjBOMib1jx3jW4AGVjmy88bhRDc2zHr_46jS9sKkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSXe4L7NIVwcyb4x4-oof2ct5T2cglbSE4BIm0U2rZ8zbMsMrotd_JjdgaN2Jec5PDqE_Dsd5-f-LGBJiEAtGSfgj1outZOjhgW19akhcJBw1LVXGBifm9QGvvx1Dt0CxLOkONhkAGXlx5yHw3mqtdMs9AWcik2f3X9IstSFdZXQFDjWRCsH71DKKp1KLRJD4-6gFHzADVXulXlgkRECOVwhJxNaRH8WLj93aHJMbWz1D2-1ojC--jWjzJKrB5ujaIB3zKgq2DmU145R9Q3hYeCGA9IlbRlNZk-zcJTPkACoj9obiZ3pngNb26FehTppnoIBWYKRTeUP3O94QBzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1TMvU3wpyNCyX5AG6SGfBzR2Ez4BG0mbIDVZu4Kdgn-RUrpE87Vo87IPkVeZDaUl66N5UMGq4ZW6Yg1DJRR2K3XimRG7KPSTdG64SXTJCqHiOcnupLY9vtRQhuFmexj01U76bapUb346ojYvYbnsv_aiu_xgCL8AqOAUlHMwbAqcXz2Ujueg4wQyY8qPwu2moYpisN7rGMTGZpZlyivk9V69BA_cjaJrmFdp1TtqJMzaI_8TIQSpT4iRjmnp3rgb6wF6tcSm2uELIGmXAet_g8HfULAGd8agBPsvJwsMm09RKVq39PSG4TnAMq1DwnJij84kzwNR32iblerL_OaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeHZb0jcDGeZAwRL7e8Dhk24LV8Db1DOK5xSLxd7Lzovr-T-jnS0EDHFlp0TltjrnzTN22Sre8iAZZXrVlBvJvkfH5yz8FB75oGz-R8fg2nB-25DaGMs5rKs2cKrdUzgLn8CgS80ylJTDiU0x81Tw7hy7wsyqYjglnyJSB6FNXnNMki3S2ySyzCvp3fYs9YeRvdI732UAUnnbIrQfF7fnREelKNWJkcSel28wDt_6VA9cS9Bl8KT-fjnY2kxk0-vYSMLcO-722uPwoW3myZgMLVz1UrNj-q7RwHI8EX9dODfCp552_d7tegOA5bbAgOKuv1biVvmpI0VpHBuFEWt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq9pkXB8zf_8kiJwyPcoyQYln0dax3_yaYzNEicwxz4YD4qZyIdR2hMYfQRvThBLxAzPqEUyounos9cX2FO69Uo_121NizTEyMCpiejTpNx94XpL6nqjy5832DePtpiQAnHNM3sf-XmjMCAZfwSldXfe2Ibzx50uFmH6ct00QzJDfD2RpRHx8n6O3GwbB7bAKBkpvjOJXUDeuS37cWofTdxYN0ebtWRJ9gxTlCgPXoPxPU5aNxWwqWtKDflJ2hF9dRCQRMu86xrHKEY5-8c1lnbhPxa5xEzjqmvQBB0yyvzVRheLpqAecyqLQ3P4IH7YYk5T4Ts89DtNZDO3FFhHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g93Mq6eTnmW5p-vh01jTE353YZQ0RnpMFR-KqCcMfhqfBcp_w5LgtO0jdSv-TqRHpbY7Hgb6_UoINC17D58abIOnqzQLtRoCEzLorySGhZW3HAvntRIxabz-EzCbm0yeFlZDEeXaVy30VLUIBgB1F7-MgP58W4lBz0rWHa1GKGfRIgvlrxyB2x-eQ53QctD6nk6qPkBiHsgLf5C1AAsbxtWN1ZkdIVb5jGtALPtkbPrEiw7q_rj9eaGHuma8TOKwVo9C_OqJLef1qKTy9ExJCxQ0O-JZT2Hn-O0SXNXETl0TyTYBmfY8E6Eaygh8CRiuFKfxC9Qh6aBlXXi6u-LoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0yetsLkIBJMUrSdgvYrjA5WPVBAhpyvnKC3L8svncUP0KBQk-pvpNCDoirS0RciOorIPeme9MznK0yjJAj1nUO-GeLvRVGsJsp-MpmQjTdBxJg8rerpg_mA8h5Tmeaqdpo-bPTkShpEwWnRgC5nzS0sbh6wYXJf-uCpWAT84iy430cnxVfSgl6vQT3aI6I2lz2ymtwhpowDIHhYciiOOGLsGM4sbPVw9wdYNk2iU-MD32064HzBGrd2oJxOVytFtCl42XQTZi_9bTFIyT0c8fKHCWGKBnh86ckgcwiduhpedpr_0kFQwmnwM2Nc-ynCulJE9zuIZIO7uhtdT1uB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHf2lMVjkeAKEKiz48y_wDY14MXLMT4zp6YOiVU3BWoY7OvjBA3mV_3pShvZZloBz4G5nfSfndm8gbpLYWrqdjK09CI4O1cWWouLzmr0QFPK6w-HG4WM0MYMJfpPEsAzrKzquzYmLxlMlFJ9awCB3oTeBo3tuZB8sIa_9IFqGrqPRQkSdcPjGvE8QJS-wc98xMRE-Juz_y_NOr9UVhgrxVZdSuP5QisuL1muBU6UgEZR_-3Qqp03sWlyu2G1Ci0wG1VoSyYNK2zgcxMPw_wsHfjLifKKtuz_KvMcPz-NpV_7ELxRo8mQiECAYfzbHPjN_LWs_O9zyDQhW9RBTgSBSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw46utpipTLV7b8JG6Z_1H3sFkCXxLfqbuj9aTsQKKm2KqGnkkyLSsOsingG-Z0x1HiK6SuCT36PDcW_qQgTAbXvDjLArYLUnnpqQ42R8npRlYRaVPRqjFruwgYG9VkHFGxD4jOlC0JpjTAv4CCpdq8x2FjiqvDm8mQeIcYi1l-CoIudng-l17CQnPnc8YSRofQ6mmNHfgbzGw7lldQARGP0RH5gFWFZkRa-kc9aI2Nnnmp9cpGNQzp7uEGV4Haglhp_cHBQWhRBmFlB14uFre9wWiuJMR9BeCQHOKYb3UBYUXO1JHyD346PgJUbBLlnZpZd-9HdMC9Lve5JyFbgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nde6hAY_qM_iY0lS7UiTL51to3kPzDKw3GHCyUN3m0_eqQx5cFt6XdSfPvi718ahZeSdI0HUgR99CgI-ela2ASBnMo8wVTc7JNHlhkrUleAiYkkskjlenuMljpq0ZWKJFvFR252YO-D9e6Fel94K045lgCxVxRVElzdQQ5AzJnR4EHp5GciVsc8Ng5c78F1nIb6X0AMNbGzaN9RDNCXc__7c-VaKnj8vZeaLfWQbh-PEG0mvKuM_q85NsJUaMqm7dYzMISLPqGx1lQkyCs3hnkFosDzoNOsjBHIeDTYbP1T2gAO6y6-mecHXHOGv9_inUqoHK69JjREvbQbKtHd5Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDgqq7K3q17tZkUhZrkELWDGu6zpojBJS3AkV7zLqScwgwgXaEIqp3L5X_eSgDdaK-Es5JZro5xvcS9Mx8uB5S6-DWM278LL1xs97P_MfRd-Ga_Lu0MNtdxSjCYLxPO0dRxdzY55h43CoLRL4P_nZlRmRl8fs6zV0asSmijNOfIrmVH-GSWKwIa5qaQtx2j_r1yHuEm_Ex6dNv7p4CQVSQT2pOxxV-h9ICqBVId6uLf4Qh5LGz1UI3mhhfcjX0IQwH--jK0sUywmHhgpOQekmXeJqb3Ryt8UIAbX7N_iZddbjx__qy2QN5WRQ4aBJwXJS09KQTyxCn1uypXjSWAYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWe5h5JRtYM0H8wizXpUdkgEEcOGoIr7o6EMqnb9P9jf0bbdfOn7EkqpihnV0eL-CLz6MicMQNZ5dOvISC43sm3wYEaXf0NHLR2QW7tJCCXIXhrQObVM8sbsO6EUXOFVTlQhJPTRBfAMkehCyHjUe0X--eq7F1WtKa68O-PkB9BlL2Y-PiJYtNWsB_8tyF1x8cHlv7ppgRdwdavPCyrrqUDRHeHsUTBANN8yU7O07WI-OK70zKY7_wSmbCgeiJyC5inxkKfhKue3CQzMcuINcEJOK8UnchKSIofWssJLtYbLunNGHKSsN3i8j6WnvMZ0YN99CNaBZbpZ4pMM3706oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=C8A5s1PuuPzVmpxs3mH9k6ZkIf_rbIfFst060y5N1gVMwP74Tf2SfOvBuNSScR2xQbaBuohrWlUeTkZ72lR37SLG9CclxbzG1tETnJ0Wmh8tPTwVwjbPIbnVo7UPz-HTMif_VReQoY5NMpPlPRHnmiZwHIbtnjR9hGkqh_o6zLC5Q76j5HySKljyTG98q2qGjPBKxd7k2CqeiIROH0kvf3JcoKfQGU9PDoQWG84EaJGBwbZYedU0QPWmYiSwk6HamBVXiZdoysbGyULjeeyeB-JovuFTUL6KyqLlnc-iBL_3XWv3eBBzw5tzg2m0IOjAe3tRTLi3laxSAlwTQOeenweWz-nff2cJeZE67Y6yYCNWnhId1v7EVAEUlBnBRvry0SUYIv85vIoqObm18wQpWYbuoMudAZeprDyALmy_Y82LjsntTR_LwlYREG4F9puDVaNb-1Ge4EkOxknv_OMxW1J79-iJ9-DI5W4ScIsEDKdlm7TMMD0kmnJTHNXj1zeHo4Xu4O2jj7bj-b2n3R5X6dQhQnccuXwMZ8C3A3LXujiCgjnlOTxzh2_Hp8v8fgU7mA_X_1vyt0YWSHVNu68P-WIIUxyt4IF6WkU40MrqlS7B5HZfSJZwMT50uVKxY38TA9k5HeuF8mUQ7jDmjZjDpfQ1AhnLhX85Woo77aAgmGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=C8A5s1PuuPzVmpxs3mH9k6ZkIf_rbIfFst060y5N1gVMwP74Tf2SfOvBuNSScR2xQbaBuohrWlUeTkZ72lR37SLG9CclxbzG1tETnJ0Wmh8tPTwVwjbPIbnVo7UPz-HTMif_VReQoY5NMpPlPRHnmiZwHIbtnjR9hGkqh_o6zLC5Q76j5HySKljyTG98q2qGjPBKxd7k2CqeiIROH0kvf3JcoKfQGU9PDoQWG84EaJGBwbZYedU0QPWmYiSwk6HamBVXiZdoysbGyULjeeyeB-JovuFTUL6KyqLlnc-iBL_3XWv3eBBzw5tzg2m0IOjAe3tRTLi3laxSAlwTQOeenweWz-nff2cJeZE67Y6yYCNWnhId1v7EVAEUlBnBRvry0SUYIv85vIoqObm18wQpWYbuoMudAZeprDyALmy_Y82LjsntTR_LwlYREG4F9puDVaNb-1Ge4EkOxknv_OMxW1J79-iJ9-DI5W4ScIsEDKdlm7TMMD0kmnJTHNXj1zeHo4Xu4O2jj7bj-b2n3R5X6dQhQnccuXwMZ8C3A3LXujiCgjnlOTxzh2_Hp8v8fgU7mA_X_1vyt0YWSHVNu68P-WIIUxyt4IF6WkU40MrqlS7B5HZfSJZwMT50uVKxY38TA9k5HeuF8mUQ7jDmjZjDpfQ1AhnLhX85Woo77aAgmGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVw-HKlxcdQy7iI1lBGGzCga_17mC_sB55uqniGY0l3GkQzKUDhB9KurgqmM4ZkM3KagxUoFzGAjBmsWa7krJfrMwsLsdDGI4DldIqZHdquBSJL7_jQaqhAZU17h2D2uxCwWm-6LRKvDYNHQy3AjTQBTbkDJCosdXkqiFgOv0G8RD-d1x-BW4myprstyprlsi9Bvy99AdEvKXtby8DufjcvWFoRZ0Cz2mWlVS-ph3pKQXgu29KwMAbZqeIpapCYmWwASmZQRSvNNIFvZyfz2kLSv9IkDWgwQ2alOnBxecwsiv6wsg6w1Stb4HCdZZDOsFZuvklaPoKjszGGEbBILbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_AvckDbJRTuudCodwI98_TEvvD0-vBGyzw5Eg1Dff4mEDhdgzsWEurcIb6SlrRKr4GuSjy01-nzO-OEXs30ZvHbm6XGPKQlhdnSjJnaUkKPFyX8qpLWOaAjnrMD3HPlucpjFv2L0g8DF-FPTqSNTDT_QVTJz3k6H4raimaiEERSnXee1X7Dp0rjEd2nm2-RlHGTZmngRYUI6l4chu4H5MMDrceh2Fu1Hs2lojILit8kaNLa0XszqcvFawMkwJKXG3cV_UJY8A2G9BC3B9CaJ2wpPzMvLE9yzjNrT4_dzwpfoFmKeubJcCUw42siXts8nqwO_mbcGGInc4_jv1R1gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h24Sg3AFICkUAgxdQGgurWjtuI2AQ0loyF5MK5bO1KUZA0kW_BMfrHVyhZT8E5QlOiPytV3kSm61gjN1Qy4nN8kNQlS4uNEUtvhd7LL-uHY7OCvjzhoA5PbZ0qFlc6wB9U_PeLO-BFBoA_AFukpum3ClDRBfW1cRKl3w9PdTjFKYZupkzPfD1kEz5zx1ra33Bc-ezA9aFOMeEIyD5Ud-PJIq1BNEDm-H_9K5_z5zXMl0qfVJeCSo35lqpGb7pa6vv5gpBVmb6krYLoyVoIUTgXSWi98tK1etxSMx3vTniqOiBNbMXjgq6DP36MUtFeoOZ9ERCm2XPjud4cCcy4IBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=dq2exyRC6JLdRwFJtdFmu5MK_JZ0-eRXaMwsa0CjrI4HVM2igyMDGYrVJp6uZ_bJa5P9LYSSgTRzPNOZb4-F6C-JE7vYFpbajCHCNJunk2ikx29gFxEmukG-0F_xZ4mJuLNsIciV1J3wa5TB4ZKXCc9v1gP79De56RFAaZHtdKTZ-xuAXkVhkZ4B8GzReqTdk-1hFWrFTpdOjCuwNm9JB85CRUYVzIjTOsk5QoBwlzGzAnP4cWv2ebHJ3QW-CWiYDt4jkea2lsjXMCsvowBL5uAZ6bpzK6XG6VTHRABAPEC97f8hBEfns8jtjwu8ncdhyBnn3kF4b9FzYPJ8DYEEyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=dq2exyRC6JLdRwFJtdFmu5MK_JZ0-eRXaMwsa0CjrI4HVM2igyMDGYrVJp6uZ_bJa5P9LYSSgTRzPNOZb4-F6C-JE7vYFpbajCHCNJunk2ikx29gFxEmukG-0F_xZ4mJuLNsIciV1J3wa5TB4ZKXCc9v1gP79De56RFAaZHtdKTZ-xuAXkVhkZ4B8GzReqTdk-1hFWrFTpdOjCuwNm9JB85CRUYVzIjTOsk5QoBwlzGzAnP4cWv2ebHJ3QW-CWiYDt4jkea2lsjXMCsvowBL5uAZ6bpzK6XG6VTHRABAPEC97f8hBEfns8jtjwu8ncdhyBnn3kF4b9FzYPJ8DYEEyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im-v7iBClF1Yb1mtlvFJq1StRkMlNVg114FrHPa7ep0bCo_wMDz0Evm2nmEo88r-sPnyBA4NL4cxH4dCITii7jHhpBAGV-SkLVEI1mHryVSz92IlgdH7H7NV62jHqNlv8Vg39kA5q7LMBedJhLhTqYrIdlEE3AmRQemU5mVxcifHn8c6Sh_ZB9PYthR_bpyMFRUCDuVBEOOOeIWTOzUI-IiiBvVIGcoArMdMJBXG_Fklo_LzFhieXhMxMq_zTQ9OPyp0Xh-oblzoJ6v2Os5BsX4triwvmBAfdiT6JrpDPGKg4-AbWNxI3hK5KqkjuyMIWaqAmNX9riMdpQT3nH7B6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=VRd0UCFD-R2PJOGUDITkiLbJSeiM2rUFAeHAN7lTCkCSkaBoCk3luLBJC0WTZcIwyQOTMiwXqbhAKY9ZvA5Ao4OvSyQv4Cr5nDTXMXR3i1E6iaveMIfdCGMtxQua5SRBJRI5gJnZitRXownI194K2RUx5BL7RxxKGnmnr4gCddmhZoArvt-arVwqkvsivjKxFmxHQ4ZUlGVWWnUKwmDKEzaRSZu1pBZ7rFcOYhI0DRv0RUcPWl-TMJCNhiuD5VCvKh83FIH3tpJe_a5LZtT8yZurISpdYDs3HHNvXqDjjKbFPqGvrKiJ9gGoI9cJYe37WcCbZxYOkuP71cA1c18uvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=VRd0UCFD-R2PJOGUDITkiLbJSeiM2rUFAeHAN7lTCkCSkaBoCk3luLBJC0WTZcIwyQOTMiwXqbhAKY9ZvA5Ao4OvSyQv4Cr5nDTXMXR3i1E6iaveMIfdCGMtxQua5SRBJRI5gJnZitRXownI194K2RUx5BL7RxxKGnmnr4gCddmhZoArvt-arVwqkvsivjKxFmxHQ4ZUlGVWWnUKwmDKEzaRSZu1pBZ7rFcOYhI0DRv0RUcPWl-TMJCNhiuD5VCvKh83FIH3tpJe_a5LZtT8yZurISpdYDs3HHNvXqDjjKbFPqGvrKiJ9gGoI9cJYe37WcCbZxYOkuP71cA1c18uvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=rc54T-6I1CUVVxL8_vUXOndYKm0PPPIHW4iHcOgEVUYv02iL49aSJUo4U4sKgh5wxXejm2g2rxKUitJy36nLHWBp90Q6nXKG5X0zH13gEC3uqNpZ4q9s81K6wR89s6vmrPQT3ZMkP8BM0WGA-qWli-goUl-0E_d4IaxGPiM6ZlvwHHEI6pgkZz90-9FRPVsDmYY21hSuq4-c6DknkdgYb9A3UNllmTPW0caIp8Rt2Xva_TFQeWp6V-WN04srmT1wGyMMr_qXP4KRkMxRO5oZgB0pL3VYdUrRRExAzG84QX2eece7cx8lRB5o19TBEpJK0BWEyFkLi8ArnB7t4iNbyYWSIOs-H_YEXaN9T1SscbShSSuj0Lb7Yz5fGYsCZEzXwLiDz-F3mVzcNX79YKqnlXbR4nDQMyoq3Y-l2O7dLt0CEYY38L1dK9wqh3lnAE5jA0vlnOxY5pC2zus8YISZ2jOMuvr9MU1Qoj9ue3fjpa1YUgklmWDpvXR2GQaeZUCfjbOMD9LeP0tSmfbKQUykLUFwl62BGfSuFEe79hpRJI26VG807zs0VHwNCAdq-tb5yv8b1xr0hRdyabuLFOEwqPO_nAPHi4RfPEoiZboXEZnp1jyZds-2KwO7vD2D01NJjPyOfqfbQAr_v-f5pNCg7dn1h29wKxaTjyXtnseKIKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=rc54T-6I1CUVVxL8_vUXOndYKm0PPPIHW4iHcOgEVUYv02iL49aSJUo4U4sKgh5wxXejm2g2rxKUitJy36nLHWBp90Q6nXKG5X0zH13gEC3uqNpZ4q9s81K6wR89s6vmrPQT3ZMkP8BM0WGA-qWli-goUl-0E_d4IaxGPiM6ZlvwHHEI6pgkZz90-9FRPVsDmYY21hSuq4-c6DknkdgYb9A3UNllmTPW0caIp8Rt2Xva_TFQeWp6V-WN04srmT1wGyMMr_qXP4KRkMxRO5oZgB0pL3VYdUrRRExAzG84QX2eece7cx8lRB5o19TBEpJK0BWEyFkLi8ArnB7t4iNbyYWSIOs-H_YEXaN9T1SscbShSSuj0Lb7Yz5fGYsCZEzXwLiDz-F3mVzcNX79YKqnlXbR4nDQMyoq3Y-l2O7dLt0CEYY38L1dK9wqh3lnAE5jA0vlnOxY5pC2zus8YISZ2jOMuvr9MU1Qoj9ue3fjpa1YUgklmWDpvXR2GQaeZUCfjbOMD9LeP0tSmfbKQUykLUFwl62BGfSuFEe79hpRJI26VG807zs0VHwNCAdq-tb5yv8b1xr0hRdyabuLFOEwqPO_nAPHi4RfPEoiZboXEZnp1jyZds-2KwO7vD2D01NJjPyOfqfbQAr_v-f5pNCg7dn1h29wKxaTjyXtnseKIKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=WlySM_20b44yA8iVTN3SeQg9SgqJ98jz8GSCbDYbPw8ah_CyV8WkcP7QgrRnpOiM_EyVPSYbG5TCX5BsbfmqrpnsghcMSAdES2DREafcznIGhJyMbmJeaYDdNSw3kKQEhkn6df-XSQC7EQlgAVDUBmPiEF2OwIhL6zAFPGmnHV3A7isRtugCGZyXgLrttGqqf08aue85SXJWlNj_NlakQuhQ8vBjC1pjVYsfrczBT9WfkEKGK98QsiRwxw6GskDoj3N_5LAnDNuRBU3Tn936cN37QfS-NIV3ZOmWYfxHnKi-UMHj5WMMySwnSQjsffZUKfrs09H-5mz2dJNgTszX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=WlySM_20b44yA8iVTN3SeQg9SgqJ98jz8GSCbDYbPw8ah_CyV8WkcP7QgrRnpOiM_EyVPSYbG5TCX5BsbfmqrpnsghcMSAdES2DREafcznIGhJyMbmJeaYDdNSw3kKQEhkn6df-XSQC7EQlgAVDUBmPiEF2OwIhL6zAFPGmnHV3A7isRtugCGZyXgLrttGqqf08aue85SXJWlNj_NlakQuhQ8vBjC1pjVYsfrczBT9WfkEKGK98QsiRwxw6GskDoj3N_5LAnDNuRBU3Tn936cN37QfS-NIV3ZOmWYfxHnKi-UMHj5WMMySwnSQjsffZUKfrs09H-5mz2dJNgTszX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX9qSe0F0Oy7DCl0DTF7WTqjBB3jML2-sEVTskWNGcD8LoLrGFXD4ZnTmE7zP2ugROxPkniBhgY_7eeF1_5jKwLxDYNEcRb4pdxGeM6oWUsccLGjlV8TZAbbAXSE8OybcTVEJxCVmWTidVZG2avvY_ulUWdbFVrgVioVvm8Yy6xt5tVQQFBu5FRMNgvXKz16QUySMMV0al-U72exxpXwS2b8qlTjsEMYZ2hkUQiVoYv6Jv0Iaoccaz03UYrrAEqouNVCHRZvVEvMTlpjg9Mi7VBJhglFy596TPgERfo52lwMYRV3K-hN-HQsRnJpfXqyLYANI3_FxFGHh0q2lwpFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibKRFSVxl30IK8hcXs24UHy3Y4rX7i3OswsADN5C-phBGRiCMGBphZf3W05etszYsWMDuHf-1jGFUXyjCZWAWs36Bi7v-v5rtUrvw-JmlNYM4UjeCO9cmuojPVJtDRsOOaDC2DpkdTNlSiAenGvESItwzZ1bE0S_uCaSUyTSNEMOmMcnr67OT_eQoMYuR3zpQja_U6AnPyiDH75hyFLPkJmy_BsK6M-MkAQS5NenJUVzGlpSi6T9xBKfBTcTavVGL_OIIvFlUV6_BIyg6v6RdBIJ9Q6s6aVdmgLiWUmqttgAPqXYn_TPn4a1w2NDapyUE_qxWh16Jl4JdPnOSOD48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMLMb602IpoPhMJfk3e4NFyyCrAEt6YT9gU19-6u5My1RlrLmsQBoKrn-Hln4v_ic-pgRSyPtrVBczlfTOuxd9pxFRYJF3-hmg4Y2rjrAYfa8Yb4GhZIZiu7I9AJjKz9LhH-VpNQXpRrFuQB4Zs48pcBdkloJtsTIpTHggK7BZjBAftxqHXA7-yJ2WgN9CtTqC2FhQz6TV2z8BxINLRzKaWyoeKsTXNH0lIq-yJgE55kXta7D9a1oLI265zehOsw5nCK_m-GMmRk8tEtfBQaxS4sW86NWFt0G9EFfSdAZPhbpFlJnGj1X-Qb5liion7tpPZHz9Eyn1kzyG7EfsHYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2PzEU-iw4SFUnMiIlxniWa7OQgxB39LgT8Hkgmnp6SMgsIYVpqwkNc251wHT67C1DM5SsryLHrGM0YY3ABLd0NWwmezQ86cUiBvSA7KuKT41fdB3HlKh2MVR7b9kRJJ3SGD6bPIDuyxs-atYymtwRzTpoNs_zdu07brZ1ZSxhgjWVT9divHpfgQfrQcaWduMmLdCdVD7t-OXR38pPtRjeWossf2EZPSwmezBv8No4f7zPXBxywrfQnTw3QfdhGGxDY4k9dYj2k5rta5EtfLYM0_eyEuZXFPgHTFNDBDhotlfVapFc82dCxR9jTT-0nvQsYf8ZYsx-lsjnHOKEzChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSuvPO70nB96O3S2EAT0XbV5N0WIFuOWqpZtOzMQQ75ejHLYGUmKdtEioZ2FXFgDZyEe1TZJPkKFNBsgZcbr61-5YdCqwodtZHGeeiQHH86GbgXf-c-l6SZGEZSVsiUgfUjV6L9jqhCT0vuwQxTwzeJoX_rLhpQyBkYSpPTpN3yeSYgTTzTx_KrxmOGiwXNa0V7UUmLE8Ly_n3lXoNAYKnIgEo29vTjaXyPVm9onNFHjNFLc-IvqNZskcp2dBXZsqK9coArzYViK8ilrh2QN_u2H2zxjU2ktiytRU0ZqdGhYaSYAbwnffEc6JHMtRTWRIw1XEIh0B2yRUEkcysrr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnWGC3VL7S2KYVGLP2-8_S5GVNr89GmaqVKnP-GGl-PvYYgqReBHgNtLubfp8rDF4ANvXQGv_SlO35E9oEWXoiBMrnT7IC1-diucK5eT_23zoxy1Imxsl58fIBNJ7elWpPn431QVLPIBcKX2XY1ElBPO-wW8XyXB2D-B6YwMzC7wAqa34BVCIBUq-wjIWZiuSOX6XBC62s0fPkFmhcxSJSu63S6vErQngUkctBIK-fa9wWiuaFsKkBePpKgDLp3sRqSjR-aWxXFxkF0Mz87EGeadg0p38nOZHnl2IZZaUBxj7y3_gg4DROydvsZIIImJYdP4aUlUUri951G6i914Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=bK2vk08X1btIyr35a49e9rxVudhdyHWRx7JglcgNAynRojWi2i8NzVpTQ6qSpGJwMGabjfCSS3J8tFKTjCgOIf5aTwXzJhY-Pf24PB5GlPxE-6gyoJ8HaRxsgqnIe0ChAFVZOW4tHwdV535_sLBh5GQSv2ODHJp3wpoG2ECwOhytepl3Y08mKbhyyNUSHcG4vAheBEWwFWzQdgQ1_-0Hprcaq6JywT8kwqnXUqmVM3tD1aFKXmp4EH-GYsTj8ZhBl9aghxi7_QjGRjZcdMbCg7eGNCSzip7r4CSDNanujPQMwCX8_QrbQR5yMAHo4iCS8XLW0eAoPzD2NPaw3IhaM6uyCuv6z2e79KrxFqz1Hlp3RAw1Y81xzaM7MI0vHSPCmvOq62671K-SBUy-_7ssH-ANwNfKYA7M3Flqj8SMWkzfOoPMgN9BUlwRrYbZpNqgtofNgwhul8h0u7CYVBCKxrBAQpEnx5kCAUcgd2f2Yykk6NK8udhiVLaZQutb9V08hEtZuE5v5NmhH_7yEhZx3UqtiemJ21aWBf9B7qK3WsPE8oEVnYDb6ki_6EgU4SrhH0r2KEV5UE_fDebZI5D2Gvqo_yHkIWT3MLIkQDPtCnVmz0cL86N7irgF6T9bl4nS1RVI1vLgvTWpXSKk6Kzf_-E3Tojj539OnUbkpZ0qeDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=bK2vk08X1btIyr35a49e9rxVudhdyHWRx7JglcgNAynRojWi2i8NzVpTQ6qSpGJwMGabjfCSS3J8tFKTjCgOIf5aTwXzJhY-Pf24PB5GlPxE-6gyoJ8HaRxsgqnIe0ChAFVZOW4tHwdV535_sLBh5GQSv2ODHJp3wpoG2ECwOhytepl3Y08mKbhyyNUSHcG4vAheBEWwFWzQdgQ1_-0Hprcaq6JywT8kwqnXUqmVM3tD1aFKXmp4EH-GYsTj8ZhBl9aghxi7_QjGRjZcdMbCg7eGNCSzip7r4CSDNanujPQMwCX8_QrbQR5yMAHo4iCS8XLW0eAoPzD2NPaw3IhaM6uyCuv6z2e79KrxFqz1Hlp3RAw1Y81xzaM7MI0vHSPCmvOq62671K-SBUy-_7ssH-ANwNfKYA7M3Flqj8SMWkzfOoPMgN9BUlwRrYbZpNqgtofNgwhul8h0u7CYVBCKxrBAQpEnx5kCAUcgd2f2Yykk6NK8udhiVLaZQutb9V08hEtZuE5v5NmhH_7yEhZx3UqtiemJ21aWBf9B7qK3WsPE8oEVnYDb6ki_6EgU4SrhH0r2KEV5UE_fDebZI5D2Gvqo_yHkIWT3MLIkQDPtCnVmz0cL86N7irgF6T9bl4nS1RVI1vLgvTWpXSKk6Kzf_-E3Tojj539OnUbkpZ0qeDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVYl_ZJIBG1G8RO71AcEiCZ-AWhycnT9aTbkxygPlr7HtzJ14tWcWx5Ohhw4gzHe7423z3BMmDf8z5EsWVgEMlWA26qRfyinSyj6Lcv1IN6YFq18TfS8pq5KYpWT7XnWqJfOhLJCtGN28QYUbhAh6KO9DwEkkxa9ROgCzUi5YQ0lftcujMfrin0X5D3YYQG7cGmyQ0dMjZikOB_5VtuI0cIueZ74Ddw7edqLFB4kQ6OZe0wZ_daBLqEnOxoJDnYa8aIYRWqcDPRrODOBCzF6WSseapcK3UyGg8jxNkb6B8eUGD3HGxPSZy0F31rjOu_976BAa77ZovWQsG0QhcPraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llKKtA6fDbH1-6HoJmkQOrVWk-j0I_9PVQARmcGwQFsao4qFBS_DhY7_kp0se4vLRqyIc6lfBo9VVrJNDDwdwKx28KUMcFHWaFNkor3RX-6ua2F5IXHDemyPLTuRTc3mw-c_hfRMB1DVT8ek1B_8irtkHmM9OZovxonevOi5hKnFm9gU-y6dPHhFjDNgSJHNasrWXBB0aUULJ_JqWtbcrhhx1gbmmSn76LJiB18M_HYmC2w2fB3zTrAfvUDGfN8f8arBY2bHk4y7V9pafF0v0E9MlPTphbe-O6pgrftkhKg23KYk7_h3st2e8hBdUzUeYR2Ay1ffkf5ETD2W5zau0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajKzlqCwJsQ7i87I7ZBj30iq4zpEAuKGvEakkasiI6cNdem_skm5aF9iM6U3R_7w_Yw3icau_YboFkL-Z36c1rNfHL7YEMpbte9er0RiNdAypHzJe7sZOZDxDNqpke-v179gqspry8NbvLhPdyw42qcxdRbHMgQxnodlZHrrwph_GDmkmgvmpMPsgDuuhCfE4pGXvh3-b8i5Km5VCXZRyAhnMDpuVr4wFfawJIz13Uk_OcPF9Gg1V3fsAK4nfd5oA-z5V_LqGCIUbX7jcS_NO95LPX92kP4L_yhrcHFw1bDaWWHattHSJ5AcCiGxfy3xztI7MNKCHGqLDhAdjipQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7KBvfr3v1Eg5N4Jp6F7oLEzOqkV3sl59CF7jWjaSBVOfY5YHER-rP_EGjDMDa8S8nChjJEI_EAO1No3SoEr6ZZkn6qaaRBdVLCQDG79UV5XJB69ZmaALOlfbxB10nBhIjTkcImKaa1fX6sRFYnCThsprMJA3_mU2CbaT-E31s02fcXDfGA17JrTzkbWjywCqF0LXubngXtqTSJ8fdOX2wOIrjn0iMxVjDssJaeCajnuWUH3FxxMSMCnvocRUErEXgm332NoQC5WGe_td5DM6kQlsexW9KR3UQ5pk7s6uPHr9sGrQyM_2iSyPtpsIZg-CXqhdapQn2kiRUlIYgBpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG1O23HoFSP267RAGDoHRpmB6baTN1yC4n8VXkJA3UivPYFC13--gJlQIu-jyhlEwuJCRt-81-4J6MwEawxq5NyGNMXBszOyUUK_9SBUhPog5Hg2v86Z3f9_E1Aj9-3lBV6D3dZzpMgzN-WfrDCCDoglHxDKefspyWl8Ywup5FLv8WZwhiqrfS-BFr5QbmVMZZMXMLWZeGInEbcMyhrb0Qe0UUkIlDnF3qtU12_fYtEqGj4idqSHT35JYYY23Xa_8XNv1TN_jatXh8gVL-i7wXQWjBsRDHUR8fEcjzkfxzYLzkivBFIQFlzO0_SeWyV6Ummx8MGbcD-2tFrHvYY68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKSU1eBUrfqt3RFj1k6vF1pGuarVCXREdG93yzZjmTAX_qw3usfCfRj8QWLBUfAsxQc23ocn9hxKAfkFw5QsJO9IHH6Dj3yKltUF8M5-Hsd56RnmnH2dtJbDC4Lxx3ufahLDdcFkcCoDwo9mLpqxNg6TP2c70khOUDGkFuXZE-UECfKzGYIgHd1wrc65i6X5275DMrmRb8ff5qUVMuQnW7-P-OyZVf-MdgumJdHlUDS462brsa1L4wmQ-RQmHuMrHyFBpkKS_BmnnGaM3EqAGTM8564qEzy76h6o8G65VnJEFtfUm3GVy_KsAWGI5KaW_7RrTTe4QG6XzVf8I2034g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyHAVNlklYrhIewzu3wgeZQyJh0DwGFMdx2fMq1JuPotsm3aN1iTjpIYgl8JXfJt_xAKuijjt_n-hfRqLphrGc37z-dZSfrB9RT9oOiQUIP8KifvI1bfo44NcjWh958Wx9F4QnFv7JdzNlR-jYNkXs3V72cadiniuTxJBGFEsgpedJ6wUG-HC0rcbJmLO5vR2NPiW-Mhfv3cstmLKeINbRIZOZCcSomjVwS527x5ciN05bo1BG13-15_FKFBc6SBy182CAibSuPUYN5qby8H09fZLltli4gGnhyH1fnoi6Us9MsQKxsvCX8StaXOWFIsONLcnzC911BCF_xTDqsDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QScjj8PT0dMprIcPZynR22RJA7P9s36IG0UCLM_MJJoLTwInoRtDxUrj3jP4cF0LDq-Qo3PF57_xWXJ_GhfeJPBC4791nDI9u_5gy_lJQE2rO7QYUc1lEVQBg32HXDGjOcbtJMGpgx_sC2O12gDCiZJKnlhNxIWM6Shh3Z7U80WEWY6sOblZFKR-KauxFNIp6MYcrQIl7v8946_fEMlqI-LtEiBZY2InX0puaXw1z3jzQVcTsdqvquUp11Ece2MvtjH1R27skPX-vbxDHzq7B_KAcR10UwmsQLgjgMHLLkPtdq_JsPJ3jswqlKrKohQ7poRRE8vwMYaAYAO7N8KXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMbM5TT6f6suYWgcYHESYVxJCywdemoOYgnHHS9LLcraaCPTCS9aBgIc_hhFsyWB2yc5SVEs1FowOk0Dc0BGSZH3Nem5VFcJzq-s8kxubllc0gQ2GVXS9u5OxQHTpRTqQtXQMDes0wZNT-kP2RDRJB9e3H1_KCalpuH1N-dYGlp7zxgjo0BlYsiOtbMtDzR_okwDpADt3OdNxF0CGPXrmY-R0pOmj5Pfi99V11hifmDnYQxmLI7auKDwwlDKjd1UxKN0DMBjpU56296MufZULSW66vfPmXAKY7f0HtAUF6w394Vnlvpyoerftg6uAnMDrLZlTOjNoh9WoHH2oERFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO0NXmmh3HPUvc--PppeLCW8-C9B8eaGItIZfxrk5G60UWykZysX4XX9Aa5xOg0J-iDAVGx7Rt822PYzobpb3y-nnnPrN6AkHprt9T4LyWCzJMw1ZLkD6DfqvrMFk98LZAT4rvF3h__56UIugwCzI0WnVsC8ciDxts_8fvjw3oxKcwnUVRu5FRccK2oGlj9-BhncAsbS02rEWaBGhmJjySuhnVOsSkNljusgWVPD84mWcLiT_CRoJAMwR3b7qFEAvqxwAbdc4rhLAKwgYS7pARi_-IoR9NYZ_TEyhIZ0QacCv-4Oj7KuJefT6wcrH3SAJotMCvB7-DYGNttV6_XXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL9-PDvwwNUANvTaYsnkxm_hGjA6zRRk0Gw9Lrx51LA6-usjLI7kEZe-mWNqNe6UqHIkSG33GzVDvVWduPpSdO4hGxCQqZ7VmC2zbx6vbvzNYQy_pHGPDSHreHZOUWTAjnLlZNp9EdBr0_EI8nbRemkzuoMWQ6PfeyuyV-bPa_0mu2UJDZTYtd-Mb3jnPDJV_NZk7vIVlrXv29rN9PV5b3phDpu2ilISstCrfS0qGLvojZjGjQPYebP3lZqjScI8lc1GcOCZ_-SdrEjitmdgX45s-r3SVeBiji1YVynD8X6AfiY1fiMs-PUcPqwjeI--VDHLI1rFOLKLl4n-D3qL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEHuc8m8oV2dFqj9Z-vckAeRY4EFuzzNiJ9s7EWSKqpPXohlqLPtA5EpQVz7fVgFBi2Hylz_XZx0L0I2Skd0OSHOUX4Wb9KBhGRTnpLAEJ0KHYF22rFPDtzzh3FhXB7wIiJkdNsW1ud2XLSwx6XMat8W18ShIhfOhC_5pHsXldRtWDpqIGNu5xkXedcHosBTcAS7UmxVgmEhtuADU2MQgvdRZlY1XSzvc1yEouQ0B8ex3aTkAKoFranIaZZw07O6eR1DE5_tIDY5yG84-whzdHaQOwku9hjVBYGSKcLTvqrniar3DfdVGajwMuFxuCXSq6xntHdGGAn1J9m6p4Txmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfMbziyOlQiGWnb0zJSdStybr6ZMrl6M5CnVvAEx0RyYAV5qTDsKsrIMDxbinIP-42I67M8X4KK4EOLeAX1K7pVKkr9i-5wIs7y_PxauLgNHEljBuMFgk4fH-uJzYlHSCIY3YC7Hvi9OdviogWCAE10jp2l7uvzPwjFDn2Wll224965xwU6g0Mnz37l2LGoR5gH4k7Ft7uE8KVC-CQA8au9wrgVOF6rAug6nU2KIBijcJNYd7dGKl97w5Hp4zufKuESpjcBphTfz91hqmXLa1ydIRbnQHc229FGrukXWoKy86Nsm0oEvbXnLuLgRMazn92SICU0AQUK0JhsiYXZMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOT5kjHFeEt0Ldnojz1TtMoZaaUfzsO_bs8FZKaiG5XWH1y61g3CisZO3aYsomCSCJRQnN1z-tF2o7pTlgGj6xxE9sHI9t5T_dmdWImv6r11W01XJ9XCrjHpZwlureqL0T_YxUzSwjVSPBqau7e4lBrWZSSoC-wJ1qz-u9IjKYsAJCR4Gcu3-tL1mFCNZW0mxsKEoEZPC_49VXhAZpRWQM0quzBGFl46RAQ7UQ27SaY9vxzkpouRS1Bus35kIDQu5VzzobkPdw42-1Y9VByiZrf9R1ut_9fbD72GaLays3lvmPgntXdzAhWtYbTH5oDA9bie-d_MQP9VywGNoxK5Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=VCOIOCi1fXXoeaK_vCduy1cegsGSLuV9cqMWoOST6S0mT0LaBolM17Cus6L3LDVQyTRbnN3PVhCFaIEElbtpPLlo7KwsYmeV9mdN8tODom3beYY8J5u3_sL2o3ALDcKTKSUQ1GKA8SJTI3anVs-jfkFKxq8R4wZEh6Corut2-Jp3pCYtWN9pGyb6pI7MG5YnAGDWdSykQRKYOtNVS3MjrWWvw253RodhCNUzZt55P5c4kZkmO2iCBvOr7yHoefyQdRafKJnbx8U8w3ypkhcomBbXUcYuAOuvu6XKdZ50LD4R_e_bDr5PF_I1HzCIwB5EhF3sKV_Z9IxnfKysuXTIvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=VCOIOCi1fXXoeaK_vCduy1cegsGSLuV9cqMWoOST6S0mT0LaBolM17Cus6L3LDVQyTRbnN3PVhCFaIEElbtpPLlo7KwsYmeV9mdN8tODom3beYY8J5u3_sL2o3ALDcKTKSUQ1GKA8SJTI3anVs-jfkFKxq8R4wZEh6Corut2-Jp3pCYtWN9pGyb6pI7MG5YnAGDWdSykQRKYOtNVS3MjrWWvw253RodhCNUzZt55P5c4kZkmO2iCBvOr7yHoefyQdRafKJnbx8U8w3ypkhcomBbXUcYuAOuvu6XKdZ50LD4R_e_bDr5PF_I1HzCIwB5EhF3sKV_Z9IxnfKysuXTIvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSnE0e5nKycBQ9NupP7rDTV5BXDHuZz_g8CK-25C1HdbB2vfGl_6EWYhvvvRi_KRxaplC_I_Go2WjsDEsbS5ivMjizn-uETQZKRZO4Fz8mVPJmCWZszqvyyh-Kvlib4ohBzmSH4RczLB2M57dtV20TkjUu1mAYoid3YMr8kpt1akhH9v1zvm9qSMAKyX4jo51VeKEEWIk5ZcLY442tuujnQhDdkZVWDmOrGGE8uim1uDJrNc93KI7TkXT27Ior6F7a3aJU8xRvWuqkIi4ssCrYbic2cqUPMKv_QHmCbCukvVULfT8erdo7IWo8X3FKgWsFyWw-q42o5KoVWudpw-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFVl9NlGSHlWU_sP2xk55paXcvGCAJwwwoxNWJd5LSpnQE6EsH2jUgqFV6VmxvGe4jWK_eIDeUOLqqUgKOvKTzeLOk5p-B7CoQ1r3Y54BV2ZWWeambpjHzPgn2jQPuPaIa87UqRBwxXKJLIVcBX7YxN2S6FTRgASW5dBdTmhRVlcj8TiIQOdwPzLDze1_VXUGne1pk_bFJwSts4SH46fWtqOtcnzZ-XWDvGzE-7ksZgy7vGNJI6cetVvRrqIHKbuZwvPaguixbizsGnneYsq1PrZEnURqvrDEYXsjG_7Ii159wSGtUymdeHyEopnNzAElDZYzQiiwrfvhFAcBfOL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WInkIHe5N3bf_UQC6aWJl8jt4mVBfOVTsnMS5JHsf9Puzks1Y1O_JN3ooN2ZBZtD0fLrqVilQQ8vqH0_Vr0ibEYGRbQGBghq54BhJ6Glhg1u-GFJ2J3U-HQrmRJUyrlDtV-YkfmSrz1qPnDRipxgWRclfxhTE0JdAkSjOcdkTuyCpET208oeLsyeJmBMngyriCTKRwKOG-JKJDJZcEVrnkNn93ckke0VKN5k8wdMZiy4QtM5kcJn50KEsYNGaEvIDpvB2cD2OdqKo9lrpftqPmVA4SrRPGNAZEv93q9P_KZhXD5SmKJq5fIJsUkpVniYiEBlUrO-Vqo2m29JvvcJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
