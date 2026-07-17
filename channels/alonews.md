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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 19:23:01</div>
<hr>

<div class="tg-post" id="msg-135105">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
بیانیه ارتش : نیروهای ویژه تیپ ۶۵ نوهد با انجام ۱۱ عملیات و ورود به خاک کردستان عراق ۸ نفر از فرماندهان ارشد گروهک های تجزیه طلب رو با موفقیت ترور کردن و ۳ مقر مهم نیروهای تجزیه طلب رو بصورت کامل تخریب کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/alonews/135105" target="_blank">📅 19:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135104">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تردد در آب های خلیج فارس و تنگه هرمز به پایین ترین سطح در 3 ماه گذشته رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/135104" target="_blank">📅 19:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135103">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کلیپ وایرال شده از تور نقاشی! در جنگل‌های رزکه آمل...
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/135103" target="_blank">📅 19:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135102">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Si_3vottYeh8EJy7bpgP5lTbTl2PafUvJAVKEL76fnO5vpY7oXaSd2IQObmPW_knhzoNr1n3nrp0CtAtmIdQxesCkJDsb0aEC6Kc1FDf-_qu9j8nm0kTHCf7KCCvFt_7xTY5z82nLE0_VbL1N43reGyKl9ZjIgnDN7XaE1vTitReJ7RGOqVOqW2C-6PJbvFhNse6d4R9DowiMKOQaKrdkYfTKYQrIaS-ZqAbhTfs6hZvTUCYJ7YOYR7NvlB3AREZcEHT1mDkagnbtO06G2DRru40l4HCid_HOtTFj2pS1HHvfYaIZfbgm8OduZVzWymGVVcUW3J06r-BzPg_rTSg2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطوط ارتباط راه آهن که شب گذشته در هرمزگان هدف قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/135102" target="_blank">📅 19:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135101">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4Ky18UvNvtSpTfixxJ55Le-j3xKBZ1Z3EcSrCeXEd6T4SoS40sfhSihH0_oQsibnpHZEj487IXY3QERPX339QCpUuzDK8bX6ddCipjRh8rg4UdSI9u7bczIiQ3g6RrP1KzLuzP2WiM2UjDO58wFpXqx3RTsZqPwgfSt-f5EgYV1bKmC_jHO69riCiv076S4EIuJjYRsdOXDiV2KD9u-x-UpovKIcWai-yK13-1dXqhuuomKTbj2qPlEAsAnRqWI0FSj3oc5sAwmWWDXJFcko_l7MswwYCSiJHcpfygbd9UI0hBPHtH4zzgF6iJlDrF6NZ4aqpwTsR4okfYon9pv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز یک پهپاد شاهد  انبار لجستیک شرکت خدمات میدان نفتی آمریکایی هالیبرتون را در منطقه صنعتی مینا عبدالله کویت به طور دقیق منفجر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135101" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQnl6pXqdRlNINWOmuqaIxIZuRqWXmuhQ-B5tgd2STS_Sm9Nt_mLM20h7Lt2398Apj9iBp5bOApr1H725ydnJxdPAAZagkqvkXoPHfZx_mW2Rxat6Ed1CvVFIihvYoicsod_vKsuO6CdQ1ycsXVCUK3PDO26hKpGwsIrWwrOSHDT22TEtkpPDqjZFB7II9m7Z9la3EOFpXDwM-91QOqcBlSoryFLn2tFeMPXs7X80oJcbvVqNUZgbM25iUWCv7ZUlDvdvaHtDt_pQNeIZ0DyOzoRqPb8oxa2c-CelbvcfGkK8uFLOawSYEPWQs_6d1bb1WrAlUph3qcHr8ymnoLd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش سرویس زمین‌شناسی آمریکا (USGS)، زلزله‌ای به بزرگی ۷.۴ ریشتر در سواحل جنوب غربی مکزیک، در فاصله حدود ۷۱ کیلومتری جنوب غربی پورتو مادرو و در عمق ۱۰ کیلومتری رخ داد.
🔴
هشدار سونامی صادر شده است و ساکنان نزدیک به سواحل به عنوان اقدام احتیاطی به سمت مناطق مرتفع‌تر هدایت شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135100" target="_blank">📅 19:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135099">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd46584c7.mp4?token=IBSTdFiorXRiBUq3jK9om0Mhz75yTUfppZhjhtdf6VYcWHgK6GQOMMnEE2b7RGpAVSYOY0EK5FzeqxgFMHD6P2w7UQ_RKTfztpmQsdju422QS0d25JeOxAAdQ1icnYeMZ9DNutg8kJdkjB3YMbrwBvqrlI48mxR45SLsqLQAh3BOvts9Z_J0fEdEEFx2EKxYCu0aLVl1YlX99KIBR9923L-77qG6_VCscBygridh4pUF_NFHJo_ag_YFFDxcX82DqYkS9TfCJ6-BXnrkXpBdh69XGUY8uOhhBsanIc6SuJbJ2y9UNqhnox7je92KesNVk2jZvFK-2Yq2eQXz4WM94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd46584c7.mp4?token=IBSTdFiorXRiBUq3jK9om0Mhz75yTUfppZhjhtdf6VYcWHgK6GQOMMnEE2b7RGpAVSYOY0EK5FzeqxgFMHD6P2w7UQ_RKTfztpmQsdju422QS0d25JeOxAAdQ1icnYeMZ9DNutg8kJdkjB3YMbrwBvqrlI48mxR45SLsqLQAh3BOvts9Z_J0fEdEEFx2EKxYCu0aLVl1YlX99KIBR9923L-77qG6_VCscBygridh4pUF_NFHJo_ag_YFFDxcX82DqYkS9TfCJ6-BXnrkXpBdh69XGUY8uOhhBsanIc6SuJbJ2y9UNqhnox7je92KesNVk2jZvFK-2Yq2eQXz4WM94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع ایتایی: جان فداها به جنوب اعزام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135099" target="_blank">📅 19:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135098">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0e44244f.mp4?token=r2D7zU7uLyMMed2NoVyuVdxUGnBO8Bk5z7Z0KxgQPaKhZaBnU0NaUQE_huhhwaNqVZFO-haSn6jdnwcRHW-Q7giGQMNIVYBrhf1YfUs3D6NfTkbmKdaLbLeUiqnzQ0MboE9zPedNpZrIP8QmlBhwiZral393HSO1PSYNdD7tYBEDOYOrNPwkgyqnhtiwzZokXpxOOh7FzRa7kKYHAZ8nTzpK7z078QRc6x-kOCVZggdxroLyJS13ZzIErC1oiEGpsG9tIvvpbMYNdB8QEFWDeNgaiVP0ZkGoCAbc7wRRKQBdsghSSR1M9mScbJ1wa88fPDkyPHPNqMycUmtAcoBjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0e44244f.mp4?token=r2D7zU7uLyMMed2NoVyuVdxUGnBO8Bk5z7Z0KxgQPaKhZaBnU0NaUQE_huhhwaNqVZFO-haSn6jdnwcRHW-Q7giGQMNIVYBrhf1YfUs3D6NfTkbmKdaLbLeUiqnzQ0MboE9zPedNpZrIP8QmlBhwiZral393HSO1PSYNdD7tYBEDOYOrNPwkgyqnhtiwzZokXpxOOh7FzRa7kKYHAZ8nTzpK7z078QRc6x-kOCVZggdxroLyJS13ZzIErC1oiEGpsG9tIvvpbMYNdB8QEFWDeNgaiVP0ZkGoCAbc7wRRKQBdsghSSR1M9mScbJ1wa88fPDkyPHPNqMycUmtAcoBjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارین ترافیک:
تردد در تنگه هرمز در ۱۶ ژوئیه به کمترین میزان خود در سه هفته اخیر کاهش یافت و تنها هشت عبور تأییدشده به ثبت رسید.
🔴
بیشتر شناورها از مسیر ایرانی عبور کردند، در حالی که
هیچ‌یک از مسیر عمانی استفاده نکردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135098" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135096">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6725a38702.mp4?token=OFJZEjrkobPq_EuKx1rrbcOIttqEzgHbMyTU3B8ioMto0wMk_WzSN4vLdR_1z42Eb5xJBlcunuBG-O8ExYJpvDkuowYw75zxu6vDnHSWI74GdVnT5oLsXHaon-tW-zUg-mXygHH7i40b1wBW257Mo-ZB9WMBe7DlZlovTzSqFsBixSUQecviL534dz14P6DhHoVIzFekHzG-GJ3DGs5E0wT-hDX8HzhJgHPrm73ix0IP89iJGZiitaugRdT5xomvPAFwN9N69YYZF2WDFErN0o9CgYAAAE5OI3BBHtIyofjF1szj2oZ4OWiIFLICBNRrAUvFQOFq3J6c2nJznrC3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6725a38702.mp4?token=OFJZEjrkobPq_EuKx1rrbcOIttqEzgHbMyTU3B8ioMto0wMk_WzSN4vLdR_1z42Eb5xJBlcunuBG-O8ExYJpvDkuowYw75zxu6vDnHSWI74GdVnT5oLsXHaon-tW-zUg-mXygHH7i40b1wBW257Mo-ZB9WMBe7DlZlovTzSqFsBixSUQecviL534dz14P6DhHoVIzFekHzG-GJ3DGs5E0wT-hDX8HzhJgHPrm73ix0IP89iJGZiitaugRdT5xomvPAFwN9N69YYZF2WDFErN0o9CgYAAAE5OI3BBHtIyofjF1szj2oZ4OWiIFLICBNRrAUvFQOFq3J6c2nJznrC3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی تاج: قلعه‌نویی در جام ملت‌ها هم سرمربی تیم ملی است
🔴
رئیس فدراسیون فوتبال: AFC به علت شرایط به وجود آمده میزبانی آسیایی را از تیم های ما گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135096" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135095">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf3d1e739.mp4?token=LGsqPyA1hnzKQKdm9K6nWrdrK6vT21vLmz_3BeBpxrvHlgilNVbKCW5YsghSpDY-ld35zda0Wxjt-bKqziAcqBC9HyjPrTG2kIm7rmoKqUKJfJ-cwUnMRghlNB2DefmQHMQW40LL8pmgNj5rlzXFij-Df_wKpZWO2RGR-BWSkwVNP4P7Bnku12gMVbX8at4r7FalsmY0HJPn8SJE2r_0ZFoDlh7E1LdG4tS7vD40H6DjxaNJwh6QO2wk-ozAYsHX_-zmDifq-uvUIo0B6ck5hS-euvyjCPu8qBzDEZ3OdErfQRwhoAQACDzOgP4CfunP-3jUH4tWcpCwJ4dVzGFiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf3d1e739.mp4?token=LGsqPyA1hnzKQKdm9K6nWrdrK6vT21vLmz_3BeBpxrvHlgilNVbKCW5YsghSpDY-ld35zda0Wxjt-bKqziAcqBC9HyjPrTG2kIm7rmoKqUKJfJ-cwUnMRghlNB2DefmQHMQW40LL8pmgNj5rlzXFij-Df_wKpZWO2RGR-BWSkwVNP4P7Bnku12gMVbX8at4r7FalsmY0HJPn8SJE2r_0ZFoDlh7E1LdG4tS7vD40H6DjxaNJwh6QO2wk-ozAYsHX_-zmDifq-uvUIo0B6ck5hS-euvyjCPu8qBzDEZ3OdErfQRwhoAQACDzOgP4CfunP-3jUH4tWcpCwJ4dVzGFiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یکی نیست بزنه در گوش این بگه کمتر هذیان بگو!
🔴
صحبت از کدوم اقتدار میکنن؟ فکر میکنین اینا اگه میتونستن ناو بزنن تا الان این کارو نمیکردن؟
🔴
میزان مگه رای مردم نیست؟ صندوق بزارین اگه جرعتش رو دارین بعد ببینین ملت اصلا شما رو قبول دارن یا نه. برادر من خواهر من بفهم اینو، مردم از جمهوری اسلامی عبور کردن.
🤔
خوبه کاپتاگون کف خیابون نیست وگرنه میزان توهم اینا رو نمیشد توضیح داد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135095" target="_blank">📅 18:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آکسیوس: موج بعدی حملات آمریکا به ایران، شدیدتر خواهد بود و ممکن است تهران و شهرهای دیگر را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/135093" target="_blank">📅 18:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135092">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFST2ZJ_zVTaB13nvRdbnpaROjhjhfey_OVexw0tgYU_b2nICGTMSJ2ZP-5G0HBbz01sZ7ZiydIAn93Zouo7-AebFGeLvjhpvCXRe-WpNVnBz2uDuFTEZYjutgcXPYDVnXAFCmJdzR4dW2KqgOE3TQWeKiEXs1qiFyJeyOvcktqPkAA7R2_4hxgOiJAQm-MyMyWi4j03F72ttR6aBcDRMpk0s6Y5HBjnnGwuX_OLt3Bh_3gQZIgkx7H6VKllEB5pe5GSVDNUAjWCEeXNAi1n_YLM3GPM5eWN2KtPs7gsVF1lYFrxusDvspD3s6ZW6UkjmBntnbDE83udaE8EF9WXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۲۴ فرانسه: ایران از حزب‌الله و بقیه نیروهای هم‌پیمانش در منطقه خواسته است تا برای هرگونه تشدید قریب‌الوقوع درگیری‌ها آماده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/135092" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش کویت: چندین نفر از پرسنل نظامی ما در حملات اخیر که «چندین تأسیسات و اردوگاه وابسته به ارتش کویت» را هدف قرار داد، زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135091" target="_blank">📅 18:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
معاون استاندار بوشهر: یک نفتکش مورد اصابت موشک آمریکایی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/135090" target="_blank">📅 18:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQG8CPX5o5QuPo1cCNpdkbui3bqr0Dz0T63WBDVBKWAHcWF1BUJ7EoXperZjLOyVl9EqN0I3VleVOtWrf_K-wJpMC4bSbbgOLCmbKrNL9lFOL8JBsqtZxLCYhTtayEr4T7A1RfdzpPdfZ9xsZRaJHEl-t0fMrqiZSqt6B-5iVxgM-BpkJF1uGIyV54wVpCNl-EsPQLmmmomJEEIMG3Ai_JC9oJNOmSfmE8Cf_D3XhmRG_IjrJkxlhi1ir4AIqRQaJZN9LH6WY9kIfxymYQAXS17wwsUYsEt52BvGrR8u3h_MQF-ut4FrZJQ7QDoCZ9JjTcLJoVJA5TSy7Ldxi_3PIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هجوم بی سابقه جنگنده ها به منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135089" target="_blank">📅 18:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
قیمت نفت در سایه تشدید درگیری ها در خاورمیانه، به ۸۶.۵۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135088" target="_blank">📅 18:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee03079d69.mp4?token=NDyAFAs9nCNQvnMqt4RiNwJa1M_Q8O8bsgXbu6UWWKZyY_MrcAYbh3ygOKURsstd3wL75BfyEv-MUPYLbk5UciElsfefJPLwqozHeBFudz7TF1bX-kXbAkpDXAYlb4UXU1znt7TpU2hVRa5mZUTEjnbtiKWA2lpXT5lxXr567KPCh-qMKUgw1cYiSSPwsOWJZ9wMbpGL--g0meqJL_AsDzBiPfkoEde_8E25G2V9f0kFNew6LW3S9zJCQvSkhNQ1N97z_0RvGYeeKL_7MiRi41QnDmQM5xfs54rTmSi-WkBVo7v7rKYxAvFia0F7-3fTWw73goWDcJdezSuHc0mhvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee03079d69.mp4?token=NDyAFAs9nCNQvnMqt4RiNwJa1M_Q8O8bsgXbu6UWWKZyY_MrcAYbh3ygOKURsstd3wL75BfyEv-MUPYLbk5UciElsfefJPLwqozHeBFudz7TF1bX-kXbAkpDXAYlb4UXU1znt7TpU2hVRa5mZUTEjnbtiKWA2lpXT5lxXr567KPCh-qMKUgw1cYiSSPwsOWJZ9wMbpGL--g0meqJL_AsDzBiPfkoEde_8E25G2V9f0kFNew6LW3S9zJCQvSkhNQ1N97z_0RvGYeeKL_7MiRi41QnDmQM5xfs54rTmSi-WkBVo7v7rKYxAvFia0F7-3fTWw73goWDcJdezSuHc0mhvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدیو حمله به برج مراقبت دریایی در چابهار رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/135087" target="_blank">📅 18:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
در صورت حمله زمینی آمریکا به ایران،
احتمال حمله زمینی ایران به کویت و بحرین نیز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135086" target="_blank">📅 18:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxwjn2cXJcc8Sj5vqJkwxqh_rpDuTIJkHMmTVUYdxwYr3MLUoWWxZ6x9pPbwWonTEVOQrsyM8Csy8rtrNeSd8gfTs6l8KbgjlBklvcyIC17nI4XGpCrO0VhlF8oQ34jC19PSuPKeKxKZ_jjCJDwsTLS04fiFg6ToihxQ748JrKgw47_wjB6dF0r1oUkliTFMMUQ6YEzwItmmSCnnregTIJTl-Rgyywr-XJtkE09EQ4JjPzz1wbbf2lOsgT7vxDICjS4_qPhZ2VVXcu_FefmmEmhoVnyBs8X78hiREubxln6CYZPFcQCO3FbdJEw3HTjoGjE7YlzUjnzVv1PSqc3Eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی از پاره تنت فقط لباس سربازیش برمی‌گرده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135085" target="_blank">📅 18:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2b-0YsxWlNV7wAJy2CGeWGH3SS6SVPD4R6-26tNPaLJ3lrgYl6Zobshj_pBy-jITgOLQyzVAPXQMZ0PArO1EpSjc5uLZ2D3p1sF1auXYxF-mCBQtoE65juGT7a_Lp4_UAOal_TVOBZjqx-nAv44us_P-OX9tPP76Ou20nj4nUrvA4tiXYTJVXCnYPu3Idxmqx-OB9JKoEgm8Y9JSenD7Pe2C0ZfkOvRw3HhK54yX9mlvgMP1NzhIIlgWB8vvuhEzOH5_73YaUh-odyfPpcFA2MnQvqUlCfAyGqEptA2c_Y4Q535V-W9gjiKUu8KcMkbd5-GdkAYrct6D9jLhdILXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام یکی از بومی های بندرعباس:
تا الان شش تا پل رو زدن. اگه اون یکی تونل ورودی رو هم بزنن؛ همه حبس میشن و دیگه هیچ راه فرار زمینی وجود نداره.
اگه آمریکا تمام راه های زمینی رو مسدود کنه و منطقه رو هم پرواز ممنوع اعلام کنه حتی به صورت هوایی هم دیگه کسی نمیتونه وارد یا خارج شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135084" target="_blank">📅 18:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
در پی انتشار اخباری در فضای مجازی مبنی بر ابلاغ دستور به دیتاسنترهای کشور برای آمادگی جهت قطع احتمالی اینترنت، پیگیری‌های سیتنا از چندین مرکز داده نشان می‌دهد که این ادعا صحت ندارد و تاکنون هیچ‌گونه دستور یا ابلاغیه‌ای در این خصوص به این مراکز ارسال نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135083" target="_blank">📅 18:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ثابتی :حملات شب گذشته امریکا به احتمال زیاد مقدمه حمله زمینی به کشور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135082" target="_blank">📅 18:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzMUg9nk5cAIBq1p7NnPBOj9GSb0grFuB5eRSe8wE3zV46buNRGbAIKjqzElT5RmOibY-3BQ8KYAsTqrvuFseSnW73soPiEN9BX6Oq0v_GAZ6rCIfh2euyMU6AOpt060AUCJMOk5JL4R_IlMG6ZtSj_22ZbzRym7VmSh4VVCLB8c7O7rfNr3RZ-Bb1geNJwu4NKmRdFGeqOtVRqP7ddaN5-iCQPAefGwabuSj0I7XvcEGlgKjMKtjHXC3KBqu4mkMZWQYL1bDhbLAoLcpI0TytgGrAADylEZ9xNfdzaYe4kevSKr6YGSwt4cxjPOcX2H4BbF_zRQ4-Tx9x2UaLpKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی نیروی دریایی سپاه :آمریکایی‌ها هر لحظه خود را به ساعت صفر عملیات علیه یگان‌های دریایی سنتکام در آب‌های منطقه، نزدیک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135081" target="_blank">📅 18:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PVIOhvMWoAu4pg-Xja7f46rE7I2Es7omuF2TgigyLrYUvTMkxrnmMBj-fE9dndI7f7KF71aEDZ5DTpJIhjb70FisTjPJ2P8WMmhYRE_sncOeXouTVVbPRB7JUSGDYqe7PRZ1TT84QRT0ZEvGqk-E2oSYfP8BgoTofepQKsLRJu4rIHGT5lbFmlm-SO7_nJqZ8bIdWtVUiLamXQCETFJhgxHnvghQVDViPM5pGRHull0ZUsAlAw5PO3z6zzxdVvvlT95OttgabhhDLNEsL6ImLZaF3WJVVqz_UMnlXx3AY9zfi-iuv4TGxsdLCLRy_e3vzOiO3r0DFfXJNHgl6DPGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mfX79lEtdXyPx5TYJc4U8k6HUm_pZMolXRj9PngyD61fXZCEUpwE-uBiedanC6C7_P7ShHAO25DMlJ_0pkKQLX0lQC9v_ujFLRDQr_5LftotiRmlE0t8V081b1lnbtFabrpxKdwG6lhogLY1esVMh63W-MPJPdvJwRTby50Wwl59jlAlrM4tzKkxkqdMy2MJ9tgmsr1dE2wmsahbPyPy0dVLSmCi0_I715bwAgABxs96KbtQJ4xTEuvD6KKOPXrNVKXivMGopDFHYwzr_ayyfAvQc6P9e3ZlJ8gLRjHw327wb9LMm4PF28R1jdKS50JByVsdUChgR5a25kyY8u82Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dn_FdyVaDgmUM8dWavKotacVAgoM25-G1KN9A7g5d-Y_Ce-77-JrsujzYXVBXRyYk4bxVngv7MFnWNnJ5b6klL2aqwBRiu5jkLR2K36siAd8LMU9KI2g1cMLLcd_7DeH7kWssDsPva459mOyENvxy1bjh40CCnD34C_4DN6nK6skUqkJVQhJ8ylrqUXRdCxxuYV2qoSTnF9iQx4I2_GWF3P5mbIs5XpqdNVulWl_fJw3_MWJ7i3rvS_premax691y7xWBiHQQmpJB3y0B29qsu7fOQO6ylyWzPoCoeN-Y4honp0JRSLKSIA0cHLvUyoheOIwyy1gYaGTW2TdmAtY_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر هوایی از حمله آمریکا به پل‌های بندرخمیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135078" target="_blank">📅 18:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ارتش: زمان حمله به ناوهای سنتکام آمریکا تو آب‌های منطقه نزدیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/135077" target="_blank">📅 18:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5927edea37.mp4?token=DbyLLGw8uZxiBU6dFvH4TdpQg0V0RQiqgwrh4l4lUtaNo-ZHptfaPtvqFQQjHwWjLU3X8ijqBkDYgUxxjddi2W7R3j1dxT-XoePxEmzrovQH9U23fnOOK2yUq_KB0mKOaqJU2tMak63wJwqMTeujCxFMf652vo8ELMPXvWhvTtQwdEHKtw_x_m5DaWrhF_Vmb8WGHQomDTxFd1iRtbcXvDLdTFJC_ZSNOD8VUS0U1cXuRcIsq2LfWR0Lw_LcQZyuKy02N_igotoTVQf1AEQu8ZyDwAXLbbhJmh3zHyxaPsm622oOjg03_7AjfsKIIU7dwYQIYtwd-RBLk56-h64oSYw7tRgEoUcxAKPrr6MIEvE6zTaBV-uVnpluccqmTfiZs8gpLmuqwZ4CxXEE3KrpJ2Xfn6IRfNugm5WfgGG9EamLVJOHFu-XbOaUrq54ygCszGaAXwT9YnHiKZc_-7-Xn8na3qNxsPYYdcBzIY-cdYkKbZSWtwckao5CLSr0RDMfrROrBes-HHvaUn5L5hKz7RAYRH4fi8i1kwDC0ZELG98sPRdTgt8p2h2mzNSbPF3gwh3rqC1PoA8hV7NJUJtg2-n5B7V9ux9kHQ5NVZjZPxJgvvk6qZoBViUgFKO4s7qqa-wB20Y0f3QYNKPhRNF-F9dm8qge7qKMHJ12I0Au3Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5927edea37.mp4?token=DbyLLGw8uZxiBU6dFvH4TdpQg0V0RQiqgwrh4l4lUtaNo-ZHptfaPtvqFQQjHwWjLU3X8ijqBkDYgUxxjddi2W7R3j1dxT-XoePxEmzrovQH9U23fnOOK2yUq_KB0mKOaqJU2tMak63wJwqMTeujCxFMf652vo8ELMPXvWhvTtQwdEHKtw_x_m5DaWrhF_Vmb8WGHQomDTxFd1iRtbcXvDLdTFJC_ZSNOD8VUS0U1cXuRcIsq2LfWR0Lw_LcQZyuKy02N_igotoTVQf1AEQu8ZyDwAXLbbhJmh3zHyxaPsm622oOjg03_7AjfsKIIU7dwYQIYtwd-RBLk56-h64oSYw7tRgEoUcxAKPrr6MIEvE6zTaBV-uVnpluccqmTfiZs8gpLmuqwZ4CxXEE3KrpJ2Xfn6IRfNugm5WfgGG9EamLVJOHFu-XbOaUrq54ygCszGaAXwT9YnHiKZc_-7-Xn8na3qNxsPYYdcBzIY-cdYkKbZSWtwckao5CLSr0RDMfrROrBes-HHvaUn5L5hKz7RAYRH4fi8i1kwDC0ZELG98sPRdTgt8p2h2mzNSbPF3gwh3rqC1PoA8hV7NJUJtg2-n5B7V9ux9kHQ5NVZjZPxJgvvk6qZoBViUgFKO4s7qqa-wB20Y0f3QYNKPhRNF-F9dm8qge7qKMHJ12I0Au3Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
چیزی که امروز بد داره مخالفین خاندان پهلوی رو میسوزونه همین اقتداریه که حتی توی توهمات خودشون هم ندیدن چه برسه به اینکه بخوان توی تاریخ دنبالش بگردن.
🤔
ننگ بر فتنه 57 که آینده یک ملت رو به تباهی کشوند.</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135076" target="_blank">📅 18:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqCxN8mLtAMsCYY9qMFI7YNyj9sXsv1_Bp2uGnksG9BX4genb2PfuIGA8ooND-qPnwjtBTobMXMuvEUGaXZdOZerMULBttx6fVohsrM6EIgDS8Y6EkQvlUGhya-Xibgs65mHLnIveZ7NgAITtrDHkq2hOSkJz-08ruFXOnaTCOyTeG4OcTFI_Q6s52bZuxxWn1PrrB1zZcsycpP4hsit-7XyNVWW6pkdWpx3fLoqwPgowKv3wjSWvyMF3d8t7UmJGsOSft0jdAzmrH_KlSYC7avUU9dGEt66hPP96iNX9ZZgXxbBWB8yKdZcEyxtF7L9Ppw0wegMpOyTW0_1Lchy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: یا با ترامپ و نتانیاهو هستید یا علیه آن‌ها؛ سکوت یعنی همدستی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135075" target="_blank">📅 17:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سنتکام: اخیراً هیچ‌یک از نیروهای آمریکایی در منطقه کشته یا اسیر نشده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135074" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/ رویترز: پس از آنکه جنبش حوثی، که با ایران همسو است، دوشنبه یک حمله به عربستان سعودی انجام داد، پاکستان، به ایران هشدار داد که هرگونه حمله به این کشور را به عنوان حمله به خود تلقی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135073" target="_blank">📅 17:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز: پاکستان در حال مذاکره با کویت برای یک توافق دفاعی گسترده در ازای همکاری در زمینه انرژی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135072" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدر اعظم آلمان : خواستار آتش بس فوری و آغاز مذاکرات در خاورمیانه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135071" target="_blank">📅 17:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه: مسکو با همه طرف‌های درگیر در بحران در خلیج فارس در ارتباط است و از آنها می‌خواهد در سریع‌ترین زمان ممکن آتش‌بس کنند. امنیت وضعیت در غرب آسیا همچنان شکننده است، زیرا تفاهمنامه میان آمریکا و ایران در آستانه فروپاشی قرار دارد.
🔴
رهبران اسرائیل علناً اعلام کرده‌اند که به مفاد این تفاهمنامه پایبند نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135070" target="_blank">📅 17:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شش فروند اف‌۳۵ از گوام اومدن خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135069" target="_blank">📅 17:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5b7c49ce.mp4?token=k-e_hzgp35lzX9ySlUctubVte5i278VGKzzocRLMqiLk-Eax4t_1t2hFlnuQhTmlwezCjV58hW9c0iHukj8JKe6Rfrs-80Vq6pfNp1M3xuzYjABxnqThnNZM2XLwXIov7TuoQHKDOfQlGon3AC-eWxCcyFBniJpryB02EvGBAsH3NDnRGVdVMHwYfsHmdJbVgY3KQnyYw2zaSV1JzJT049Hh9bsGeHkzgzzjCOCxLMdZx-1CaGMt0Ps3dBoqRa6xNH7cfXiaBg9xCq-EVNhyHU6AJTIcmoK2p3RTONFEXhIEZ7sIP4sUeldYfKMKXhJbz_9v0CNQO2cPBGvWKowyWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5b7c49ce.mp4?token=k-e_hzgp35lzX9ySlUctubVte5i278VGKzzocRLMqiLk-Eax4t_1t2hFlnuQhTmlwezCjV58hW9c0iHukj8JKe6Rfrs-80Vq6pfNp1M3xuzYjABxnqThnNZM2XLwXIov7TuoQHKDOfQlGon3AC-eWxCcyFBniJpryB02EvGBAsH3NDnRGVdVMHwYfsHmdJbVgY3KQnyYw2zaSV1JzJT049Hh9bsGeHkzgzzjCOCxLMdZx-1CaGMt0Ps3dBoqRa6xNH7cfXiaBg9xCq-EVNhyHU6AJTIcmoK2p3RTONFEXhIEZ7sIP4sUeldYfKMKXhJbz_9v0CNQO2cPBGvWKowyWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله اسراییل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135068" target="_blank">📅 17:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بخشایش اردستانی، عضو کمیسیون امنیت ملی: در صورت حمله زمینی آمریکا، احتمال حمله زمینی ایران به کویت و بحرین نیز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/135067" target="_blank">📅 17:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6c614a1.mp4?token=uIqeqy7kpMJj-hBVCHV8rrjWLUDR1HUGM98vapWU_CZFKeQZ1pMrA4fhjkYbg5-DR4f1aBU8u_hDU5tfBkBiI3Fx5NbPeIp5GYkpoRcsHZ1xl7fBTDbIG27QfVy3XFYMwxmU3Gnzt6tb2GrhMwqe2nuyVlkKolQUKvF8a2Y3sRg5MxIKB3Db9rFNyrnyj5MSCcRfN34mv0theKeD2ewkWnxvBjVFRJNCVp6YxkpDB7hJLvi6BaFjV9kvaFkLvubagKmyUHN3IOte7ef90_AoPo0t-ukV0N151foP39jNiL8cf_8pht65PYwhTJdt3NLgg23MRwbrgduOrN4myjRjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6c614a1.mp4?token=uIqeqy7kpMJj-hBVCHV8rrjWLUDR1HUGM98vapWU_CZFKeQZ1pMrA4fhjkYbg5-DR4f1aBU8u_hDU5tfBkBiI3Fx5NbPeIp5GYkpoRcsHZ1xl7fBTDbIG27QfVy3XFYMwxmU3Gnzt6tb2GrhMwqe2nuyVlkKolQUKvF8a2Y3sRg5MxIKB3Db9rFNyrnyj5MSCcRfN34mv0theKeD2ewkWnxvBjVFRJNCVp6YxkpDB7hJLvi6BaFjV9kvaFkLvubagKmyUHN3IOte7ef90_AoPo0t-ukV0N151foP39jNiL8cf_8pht65PYwhTJdt3NLgg23MRwbrgduOrN4myjRjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد آمریکایی از نوع لوکاس روی آب‌های ایران شناور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135066" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdmecwRzN65wEKaW5P4rrn7TOvzatYpAVGi_UBv3eHoxSp5fMlI7kslM23LF77tfXNps6aZBSYJS3M8tx8HVzOPkRonscg86C0yud0vEq-1RcuAZcNwlWdWat9lTYFwNCYRDImhVoteHZwTw1WuBzezqoT7vN9TL8uLT03h5YndfoSa9w-7p1gUYJG5X6JWw9ll337gGXfzA5O45zi4jZN8DFrJeSez3qhl9vMsxmTCPCZKpOlVNTi_wGvAdwMwM00ESI7GtmsEHA5hvfXknpzrPMAvA5VWpDR4KjKDYyxNKKGPCAIpLvRlgFTe0sIGzyBhDe-HhqPjbxzsff6EhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
نماینده‌های مجلس فقط لب و دهن هستن و الا میرفتن تو جنوب جلسه میزاشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135065" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135063">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKaxgPxsTsJZi5a7RMAkPb7LoL22NyO1U6j0HQUUBfQGzLLEeyeAhKSzG0l61wUrTKYwkwPL6puxe4SSWreewMyShXTmTF-VJAMgwnU8kERKxYeaVIx1bviVFFH5lYP7fycbjjbh7_3QUECCKoPTjj0XkK1IJjts8Fj-bTjUEh7WmJ9-fcJAOavinVHEPH23nCqtyDnEyuOjOYBeod1BbNQo-iEnMBlpUm7eUSLlsvtwHiIMPqnUz__8V5cKr4SdL4mkZiNYt4b_m6GhfnazdJinRe7qPT9iup_xRrA3CBLjuUhWsx9Y08qs3ql6lD72FLO8PiYn_Y1BMvl96_I7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788a242c29.mp4?token=VovmR-VcQrZB633WH8sq6nFjc0vi9euSDDa6yz4KWsGljqi_mS2CVDTbRA6dLEXFMzAdaFSADzXsALXJ0v4Ln8dr8Uv1WYSJ2ogpotqB0gaX-K-xT190HNFFzRdNd-IamxjMY1h2lg9PSEwhluABUPSe8or62y3TaXJSBaNFwSrjs8YapPXv7_SwqE4HyiK_0TA8qGxGJ5mN9rrQLYBHKWBFCLjpoSUI8kmof7kLsizh1JyT42L2KLceucGaGKUJ-8S3ew-YXZMQTOCUSuK0xtbwvkhwWBBmp-DptVV9nt-nUWKQAWCNfRktNIcn2i2HJPM8DgOGk9GAz2LMBHdg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788a242c29.mp4?token=VovmR-VcQrZB633WH8sq6nFjc0vi9euSDDa6yz4KWsGljqi_mS2CVDTbRA6dLEXFMzAdaFSADzXsALXJ0v4Ln8dr8Uv1WYSJ2ogpotqB0gaX-K-xT190HNFFzRdNd-IamxjMY1h2lg9PSEwhluABUPSe8or62y3TaXJSBaNFwSrjs8YapPXv7_SwqE4HyiK_0TA8qGxGJ5mN9rrQLYBHKWBFCLjpoSUI8kmof7kLsizh1JyT42L2KLceucGaGKUJ-8S3ew-YXZMQTOCUSuK0xtbwvkhwWBBmp-DptVV9nt-nUWKQAWCNfRktNIcn2i2HJPM8DgOGk9GAz2LMBHdg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که یک انبار لجستیک متعلق به شرکت خدمات نفتی آمریکایی هالیبرتون در منطقه صنعتی مینا عبدالله کویت، پس از حمله پهپادهای ایرانی در اوایل امروز، به طور کامل تخریب و آتش گرفته است
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135063" target="_blank">📅 16:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135062">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO7K22prbm3ehOhav7cDI1vf2-bXdL2WXHVL6ljuWdYLN4jQPC4NGP1U15pN1KCBpLpvfifQSzsqJ2W_414GZfwzRAiGOo8Ssgc_b56j7919DiyCJMZxkFWkEl6-Om1TtHsvhlO69oEWVt2m2tvADh0kmswxR1RD53AphBrbQXTWHwYTYjU8_6XoNIQTNzN186QnAVB8AjweDPG6rkZpTsKuhUVcumfwjpcYanEJuS6849I15vMmWWziy3PF1znp6npXaIqIt-R1xMyqFxbq-U9iMZggO3saruteqH2O9lFNA9Cpp371rLp9x_Iz5B5OOoS6S6nrqOQe3ZO2ASvdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا الان سه مربی تو این دوره از جام جهانی نباختن:
@AloSport</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135062" target="_blank">📅 16:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFLLnvQqkm5Mw0d7QTBbcZPsv7JbOHv8JLigG8FixkpsHq5nrSm0vnBLFupz4ZUOKAAjn0nnmCP9Qwx_FaG30XDGSwpfB8G2abuVURHJvLKGDgwdnk4WlFJbiy4TkWpTMEt9STfZxFOsXu5Zm95lA2LL75g6yk_30FPGjmyQWaczd7LVUBu89N5OkD83752rup01mIQJdRv0hZ6bEPuEv8sbbxhXt8U01dhnSI0BBqQvqvIgEWzxb6yxKEmDuCdVGzEOFKuEgWivpryRUNIGhEQEnFOZtmh9NA--CACvGOg0b7JafdOs4fWB3WA54XRNAEq0MivApLA-jgTenUNPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق اعلام برخی منابع پاکستانی، فیلد مارشال عاصم منیر قصد دارد به تهران و واشنگتن سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135061" target="_blank">📅 16:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
روزنامه الاخبار لبنان ادعا کرد؛ تحرکات جدی مصر و اعراب خلیج فارس برای بازگشت آمریکا و ایران به «یادداشت تفاهم» و ازسرگیری مذاکرات صورت گرفته است
🔴
قاهره به شدت در تلاش است تا درگیری‌ها به «نقطه بی‌بازگشت» نرسند
🔴
فشار سیاسی - دیپلماتیک اعراب به واشنگتن جهت جلوگیری از ورود تل‌آویو به جنگ بیشتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135060" target="_blank">📅 16:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or67Ip1rKItkElT3rA6TtXWKNF5I6RD8YCHndZHCXrrpQCQzCQT4i97eqHW88cuJsKoN6LUrJNWW9Tyg2aY06cyPaotXKH2B2S3Oj2MWxKCLvaVsSM4L2zFDFxThhw16aRwil9NLRC_DneGzi7d6YZbv2GjyxboRtB3Dqcvn9o_zydLvs3-fYBXy8_PlOvt7K7y58RgdQ5oeJfLXXAbjcriej9rlTQGb1ceACRsSTt7pgh3PGdhv_xM5IT25xjZDbLJJcrILC44IJTSO_JXI3-bcKZlWEycaHH-YMRT5P40NGqTY4hM4O5Fuc4gq-2d0dDqMFCQ8kNZDhKhJqg-8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقت کردید از این ۵نفر خبری نیست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135059" target="_blank">📅 16:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
گزارش انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135058" target="_blank">📅 16:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=o_aK5o0MnYc_UoVuJX019wc7wHEcGXdZnli_ClojtEuqveCYxr3VjA4Pleeq0hUETTwDgFDEEbJZ-QdH2mFyW6pC6eQpeNn87_DEoK_FwFptXWNDSpwEYQaygVwm5wpc861n1fZpJWeG_mwYuIM2ftXDmgf88cU9QUMgsfwLdRLCUyE4pCYpyL3SQ1gydhEX-7jIB7WNpM8nxEctupQg6CZDQsM1SRrU9HGG1saCO4kzhFqpUNr_B6w4kpfMu07gTQAc98Bkjzy-wd9rqzj4msYCCcTjKshMO_pUrWucnGaiRsc_7ojiu7qtPCwrEVoMbc8fNV-WeAjl4wYK2-yzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=o_aK5o0MnYc_UoVuJX019wc7wHEcGXdZnli_ClojtEuqveCYxr3VjA4Pleeq0hUETTwDgFDEEbJZ-QdH2mFyW6pC6eQpeNn87_DEoK_FwFptXWNDSpwEYQaygVwm5wpc861n1fZpJWeG_mwYuIM2ftXDmgf88cU9QUMgsfwLdRLCUyE4pCYpyL3SQ1gydhEX-7jIB7WNpM8nxEctupQg6CZDQsM1SRrU9HGG1saCO4kzhFqpUNr_B6w4kpfMu07gTQAc98Bkjzy-wd9rqzj4msYCCcTjKshMO_pUrWucnGaiRsc_7ojiu7qtPCwrEVoMbc8fNV-WeAjl4wYK2-yzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135057" target="_blank">📅 16:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135056">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f17c95a2.mp4?token=uhq-oQaxGP50p9fKpiJTbKNicqcrGiEIeOI8iydz9l0KqiMTdS9S_CZjkoSkDLKTE0cPaFfyj6SNwYJVj_ZhtXn4NpC3iTi7QDxuWxiyVxCGcX4rJFU_1ZtVI1TfltjDpdy1_SnuNgNiv3vdfH14XCXU_ayKggS6kqze3e4RRpx2eH8jtQBoHYPJJy1e5iuWIdDWBmmTPOnbUM199aAIPapAid8iptlAqiGHUIbYBQeKNihCGQn6Ibyi2Sq8Cn0mVz4jHuwLrUwuPi8IvIgWnNNbiMyPgCO_rBHg3OKxutldhDtV0vnoiWCr-DLAn2puuCKoJUcnpEhD5jN7tZrbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f17c95a2.mp4?token=uhq-oQaxGP50p9fKpiJTbKNicqcrGiEIeOI8iydz9l0KqiMTdS9S_CZjkoSkDLKTE0cPaFfyj6SNwYJVj_ZhtXn4NpC3iTi7QDxuWxiyVxCGcX4rJFU_1ZtVI1TfltjDpdy1_SnuNgNiv3vdfH14XCXU_ayKggS6kqze3e4RRpx2eH8jtQBoHYPJJy1e5iuWIdDWBmmTPOnbUM199aAIPapAid8iptlAqiGHUIbYBQeKNihCGQn6Ibyi2Sq8Cn0mVz4jHuwLrUwuPi8IvIgWnNNbiMyPgCO_rBHg3OKxutldhDtV0vnoiWCr-DLAn2puuCKoJUcnpEhD5jN7tZrbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط یک کوهنورد، امروز در علم کوه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135056" target="_blank">📅 16:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Ux0mesDdiAf2--Gj_1mh-w4QbDUaf-5mD-Hzu_ebgd20eOKscOzaLqf3A9W9T_EGUYMB0AQUd7x9Jwi3y6QkGDgpQT-agS8b8paR--o7mGzsJumrmUBugfzpP6Vh8En90tCQSXueMehLDgMJfz5D2niU_U5bGiCDlvvPyWt56TqWT6iB84iNDfNLYcMcsTBhRMr-dFPWISSai2EkYm4YZiq-H4nvLtbvqgwf4JwPF-mWICDX0QmUp__W4uTuPWHnVoPjcyFeK4x_NuUC0CebDzdKZD-Kf5VNIsxwPXBtSFSAnKu66ZoSnBU8jnjgLgAzHIWkpTdHAuWL6j2R8j6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیامک مادر یکی از شهدای سرباز تیپ ۳۸۸ بمپور:
🔴
۵۰۰ زدم برات رفتی بیرون چیزی برای خودت بخور، به مناسبت تولدت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135055" target="_blank">📅 16:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ca36696d.mp4?token=XeNCz1CxXsfN-bQwT2Q_tbecYikRLc4GsQK7JsphT2QVk-0nre74A0MhdyOTJyhJgNA5_Sr9jADi0afXG8HmOc20FiSSMeWzls3zjXgqQ1vVZtYWpeEjjBv_pWVM1RX3m0ZTH5tEhT6sjY5DerWD0se2Hh8ZPFLQRvM1axSvjpG-Hb_4RJrDIwpO-rzD50PKHChR6CIDRP_8owP1S2GLyxjle4XsrKkKMjCBK3uE5Dj8DxokAO2X1vZI-eROnd6uBMEbiKcq5L6KaUCiZzfws5BNY2HbV5XmDmG66VxzdqY07IiWjIESSk8-SrF6YJ5ytuJy7F9dgF7g1OBubhQd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ca36696d.mp4?token=XeNCz1CxXsfN-bQwT2Q_tbecYikRLc4GsQK7JsphT2QVk-0nre74A0MhdyOTJyhJgNA5_Sr9jADi0afXG8HmOc20FiSSMeWzls3zjXgqQ1vVZtYWpeEjjBv_pWVM1RX3m0ZTH5tEhT6sjY5DerWD0se2Hh8ZPFLQRvM1axSvjpG-Hb_4RJrDIwpO-rzD50PKHChR6CIDRP_8owP1S2GLyxjle4XsrKkKMjCBK3uE5Dj8DxokAO2X1vZI-eROnd6uBMEbiKcq5L6KaUCiZzfws5BNY2HbV5XmDmG66VxzdqY07IiWjIESSk8-SrF6YJ5ytuJy7F9dgF7g1OBubhQd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
این صیغه ساعتی های حکومتی الان کدوم گوری قایم شدن؟
🤔
یکی از یکی حرام زاده تر</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135054" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135053">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آمریکا: حملات ایران به کشورهای حوزه خلیج فارس هیچ تاثیر عملیاتی بر نیروهای آمریکایی نداشته است
🔴
سخنگوی سرفرماندهی مرکزی ایالات متحده، سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135053" target="_blank">📅 15:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIvR-PgRVYjHm9YRuI2q-6bz8lheAojZpStDlOoV5VBAkK6tOZG2h66j_mzjARs7iFOC7o5w693o43V7aX_AxwNE9koZv142qxOEXLwSj1hx0jtfHASthzhfYjIT7QIMRdciY59sQRmkjjb4aLZyOr3l0mO1UngF1jJ_wG53cURCV3Y9WQ8_xO4AAh1hFtmuB1CtGU3HOwQnpsq2DKaAiXAAt0aPWRxXizAQZnY0xrMauK34sWFoG334rqnHbkpzBXE2B4b8GQE3mcwbVKplQrtJRG-_Sn7pHDJLX87UMbSui46XORhhnWe1qUQyDsQ7ZsfUwT7kWWDn8l7UrounTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مداح پاکتی الان کجایی ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135052" target="_blank">📅 15:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=Ql2zaOoLzKb1KH-Sl3c4pP_fkKepuND4cANbsA3ymdfW4t_2d-hq7rp2K8wFR2aWmLYEcLV2w1zXtTHEZ2LmnaoGr_yvypWe-A0dPJt-f4thhKq1jihUo3qBAgg2jj9XHCJuQ20yGU7prYKx0622Ao-BTeKg50F2amyFNp1wfz4PWkmmsG617M9i3b39T8q95K0VDmwELvQ3UIiz46pthEZPELrWr_djOH52ws9wqcxRjG2nZGIODA3Pz2aAohW3FRaX3EOZInJCK3jyp1mFMLC05l8r4RXXYLMx2lZOtHjxybb06XRljVQc6dJycamwyGR8SkpAxdVGgnwxy-CrZS-l-c-Ee5UAa1TEmCGtNPMl7S_JBSYxevRXa4qmizgqtHTwjzG9kQAPlTQ9rmRzr6AgtElnegp0agx3QXZVKkhbeB2j1b3dAutCN0vRi15wVqHjEBCjBSrTRaUn2Ywa5pvNvPLZCnj2FLNUWdIEYJvSiVwaXOXa6kqAyHZnvBkN91uIa0hpSAdKCvFv3Qz5Cl_TmLcUhn2eLt53dx7mO7P78Yj28enqcwNx4Qmmuul8zqBXj_JgKiW_-Iw48dbHLtc8gNWaMxQsP5vj78A5--fguj7baD_JF08qrYiQqmtMT3XVn9f00_HYahxeShYWjFZzg5jdfp7SEEx5Oa05mBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=Ql2zaOoLzKb1KH-Sl3c4pP_fkKepuND4cANbsA3ymdfW4t_2d-hq7rp2K8wFR2aWmLYEcLV2w1zXtTHEZ2LmnaoGr_yvypWe-A0dPJt-f4thhKq1jihUo3qBAgg2jj9XHCJuQ20yGU7prYKx0622Ao-BTeKg50F2amyFNp1wfz4PWkmmsG617M9i3b39T8q95K0VDmwELvQ3UIiz46pthEZPELrWr_djOH52ws9wqcxRjG2nZGIODA3Pz2aAohW3FRaX3EOZInJCK3jyp1mFMLC05l8r4RXXYLMx2lZOtHjxybb06XRljVQc6dJycamwyGR8SkpAxdVGgnwxy-CrZS-l-c-Ee5UAa1TEmCGtNPMl7S_JBSYxevRXa4qmizgqtHTwjzG9kQAPlTQ9rmRzr6AgtElnegp0agx3QXZVKkhbeB2j1b3dAutCN0vRi15wVqHjEBCjBSrTRaUn2Ywa5pvNvPLZCnj2FLNUWdIEYJvSiVwaXOXa6kqAyHZnvBkN91uIa0hpSAdKCvFv3Qz5Cl_TmLcUhn2eLt53dx7mO7P78Yj28enqcwNx4Qmmuul8zqBXj_JgKiW_-Iw48dbHLtc8gNWaMxQsP5vj78A5--fguj7baD_JF08qrYiQqmtMT3XVn9f00_HYahxeShYWjFZzg5jdfp7SEEx5Oa05mBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی مطهری: یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد/ پزشکیان می‌توانست فیلترینگ تلگرام را رفع کند ولی چون روی وفاق تاکید داشت این اقدام را انجام نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135051" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIttBMZO92UTcLO4cFetnY3sYLc8pvSRSZHkqYmb5cNcvoItIkUiQtIXZVTgAhU_c9LYm8CuuzEIEINQu23FVU6oappFjtVG7deQJIy4cpcRxYXYsXNfc2p9-MXbkixCODfr-IWrykL3JBNyjeoZAmSlWjn9w5ApHfYRBLiicSdi_eoOP04HjyUPv-PPgm-SHnHSfM_EqxZ_IzRO0vIPeQeIdwx0cKvV-c9ylyqQJghWmRi4-o2c3eMtZiXTa6JpfiRFrfZ1AG0QzL9PfVU5XtvG5nD1DKccm-v0aeREuhotdmZmkmZowCDX4ANSOyT0_S0TPgIUOcz4wpP0LdwOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی در سکوی پرتاب موشک‌های هیمارس، احتمالاً در پی حملات شب گذشته با استفاده از پهپادهای انتحاری در مرز کویت و عراق، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135050" target="_blank">📅 15:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135049" target="_blank">📅 15:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه قطار در ایران موردهدف قرار گرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135048" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD5LK6UvJWG-SaH8tL-f_pUd9Hkw613C5YgsPSq0KQ0Pq7CksxxNiOUhHh7T3pk4FfqJzM_xeCzk0O3BIlWp0pH44HWjWajqF18P-w0tZ7hXHuvSOoCyr3xeAiy3yNmZ8Djm3EvfD0okU1jzLvGq9xJFNILpv7f6uUMP8duEMtvCSEOYgLkmFJnKzj5dNKu_u9qZ5LfcKLWy9cEqURl60TGmel6fdfrxXwaO6tIKKoq0fdqkMoUu-AMt_coRTcf3snz9yS6iVZnlT3i7HWYQ0IZjvaTkfa0ZybzOaNOEaHmzzQlGdv-Vn1IueQISB5rqIRYxEkxyyNLGxZ0A_ig-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: باید بریم پایگاه آمریکا تو کویت رو تصرف کنیم بعد تجهیزاتشون رو به غنیمت بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135047" target="_blank">📅 15:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUEKJ7HYAVExQ2WPcCocqMWmsRn2-csfR3XdxGtU_J0yxoyLDlSQR5rCs430tpOWpUobg4EPfPWsRGcNQF0KNclVNbwmpJGeHN38Mg_YwZRMW_b8gPq31d-hy2RxnrrdJiA7OVbXcQpN9M89-7j4BKEC9cXx1jVYTpvpfx7G6HWIL0XYMPUmYKmvaKp5FM4KZELnBsOrJnNwQjcLw9-efPTibeatRpx4NUFcOaMhYBPv5scVxpJnCZwSMdi8CvvF2VA2nyN_BiSUkGQBaVEgPBm_m5iBVkM9QNsJTGZKoVHfdaptndEC0jtrfpyRoa7b_k-NVhA-WxBtAAU9h5fR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بندرعباس مردم قایق‌هایشان را جلوی در خانه پارک کردند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135046" target="_blank">📅 15:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135045">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صداوسیما: ارتش آمریکا برج مراقبت ترافیک دریایی را در سواحل مکران به کلی تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135045" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135044">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZd0wwJ43NPHVIAyPZRrbL4Q-iAnwHjFU9DoEeNoM4WYQrQQeyVOPWud1HEwXBT4htGQfdgY3qbmhRv6dVuGWijJ2H1hCvdqRnWXxgtRXmxxkWrQLf-2w5BnCjass68F1KFzimVu5RyozoaLNAgO8RbcH87-ZqK9T8sH6nqw0jxEEFHdfeSIrEB_fkfIK9UQIEQdyW_kBVcurPj4pLynqdoe82X3k9KspEYWcBLJLekvCNU0IVnc1RaB5UYbBEJLBYagTroyUOgMH6ZwFHb-UpAfEDCWu5qW4ksDsFMaMMmlcaoZS8duXe0WcbgxxHvehmOghHXzTgou5HrfeBLE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست‌های عجیب در پلتفرم ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135044" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135043">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
دولت انگلیس:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا به آن کمک کند، ممکن است با ۱۴ سال زندان روبرو شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/135043" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPlYNPyTYKdEzyhpygobV4n7oe85TzkjX7NqSIEDLywJ1eMdLnxb8oNC63fauEYQi_CILJguC9JYUB4ui21d8AA-T04vqMccxAXnC5xpA4TLtS6LCo-d_J--B-cg0vR7wAe5ElY4738_jEHrrrPR__5CKFnW9YaaVY79tHy-HSZdOUi_Yo-4c5Hzhayylzw2tflYzPxUVd7293p2UpiaERg7Pjx852NAcBRB2iP_eJayioLjO66YGj4nyVxHvfJ2sF273XS-VwNbZsIDulaXI0-T-2yRlDKNmybJ_YkO75OGM10hWPqyfXeaWNGjKsJifQHJ5ET5DpwC2y0aPF9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعک‌های شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135042" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9aa080b85.mp4?token=MB8bEogJ3lYMCdj7kyXzf3wpBL0uVyuAf-sPB4zdI01XcQFn1-mbLWiJB5WqqmITjjMxE4pqB272fmKlMRMlYM0wbiZfdYL2MhMmWQis8ZwaNody4OJIU8Ib7DVHb8hsxLVLhtLYiIQNDt3ZEO88il0kBNPx-hQqD4KLH2TW50yCO6hBZ-9MwvLa3kPNwM7P2vsd5ZjBXNe5zR9FP1UFNHm0wPXh5_E1P92cAZkdfX82qVDAwbzNuxmIboKUms7WVClSEMhCwMqx0FUoHLE46lriIx_pYlnaS4vsQTPGPkNZrUBccCc83WmVjV-ufnbG6hPBuUBOnd3uqww-NHm8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9aa080b85.mp4?token=MB8bEogJ3lYMCdj7kyXzf3wpBL0uVyuAf-sPB4zdI01XcQFn1-mbLWiJB5WqqmITjjMxE4pqB272fmKlMRMlYM0wbiZfdYL2MhMmWQis8ZwaNody4OJIU8Ib7DVHb8hsxLVLhtLYiIQNDt3ZEO88il0kBNPx-hQqD4KLH2TW50yCO6hBZ-9MwvLa3kPNwM7P2vsd5ZjBXNe5zR9FP1UFNHm0wPXh5_E1P92cAZkdfX82qVDAwbzNuxmIboKUms7WVClSEMhCwMqx0FUoHLE46lriIx_pYlnaS4vsQTPGPkNZrUBccCc83WmVjV-ufnbG6hPBuUBOnd3uqww-NHm8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تو تجمعات شبانه : جنوب لبنان و جنوب ایران اسوه ( الگو ) رزم همه‌ی دلیران
🔴
عملا دارن افتخار میکنن که ایران رو به غزه و لبنان تبدیل کردن!!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135041" target="_blank">📅 14:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135040">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZqb2jIEB61EpPdnjkmbsSV-Wl7_vGgLVjLL1gbKSX-Xd7MLEvP6pUqvBt0tQt6Gsr0JFB-G-aGexgfVllMCIJ1MGY9pXC4w3Z2_CdJyvcQFHamYyjcr3VdiG6r89vIKJ-ke_Fual-s5nI-0I6KGKbiGNJlJ1rpGuT2Z6-MH5lnqCxcW51o1arNcbwjhaKBrFlsH5TAkx_niW5VD8L9y5QASgMWOYLFVozc3Iv864G27xsNVF3ntAWMVi8J8AZo1-b07J10mUEHuTsYoQgg9s90K9RKszYemtcCMNOgTXIFj_998ZeTL2mrvrkTj_d6uuwGK59uwlSCxfhIYEi1UJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپ جام جهانی رسید نیویورک
@AloSport</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135040" target="_blank">📅 14:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135039">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkn5flYtEE8Smy4Ay5gLAm6CXzcDuh4wjILUHlXIeLBg-1uUGW2Tx7WW_AothoH5H8-d-cX5Spy3wR5vIuFbijwH_4zrb4GhtEU29NjE9zYksJjuviuQ6y43FaQKxGNmP5zR61Lh53N3XMOVm55cl7PIGy9Mnyftf2x77UKnszmbcSn5v6bsaAT7xMgsaOzXxll2rU6GhsrZKjZsygOatEbmqfjrooP8TizHPxkOZNVCxwYyfjn9qMp71rVugAlj0kdTK6aohIun9aWUv-Lr2MNZqR-M1_NqTR-sgBuUdxCf2OjUonL7lLKFzxW_afxDDK3mP19yjuR_c9rwYSKH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی از یک حادثه شامل یک کشتی تجاری و نیروهای نظامی در فاصله تقریبی ۱۰۰ مایل دریایی شرق دوقم، عمان، دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135039" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135038">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=Hztwv2p6-O4Je_EwTzpg6jhjiDNN8n5Qk_iDL04vqiYT44cEwslZvNkxLJSTFzT9VpgZHHauOOkWmiGwamP17v18eHzXAr-5q7H9G3kLPEB5Qj0erQYG-VFQxfthoCeqwlyivWpoSZT20elRcFsFdNB7b_-VwroOsfYeDGG7FxqwZj6q_Tijk7zrb4t2NiugazIIzolpbxtQ0yUmuipIvCMhH1Y9t6170dZOLPq3hIB2ZTznxjEmPYO4KiSImKX82OLcZKr7oil4dsaGXnzvnrhcrzOt6VwzQ5qJWfFMvXsItoeUgo4Ac3ifP4_B8gOUsWOTsjUVkFRD8h7a1iQ8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=Hztwv2p6-O4Je_EwTzpg6jhjiDNN8n5Qk_iDL04vqiYT44cEwslZvNkxLJSTFzT9VpgZHHauOOkWmiGwamP17v18eHzXAr-5q7H9G3kLPEB5Qj0erQYG-VFQxfthoCeqwlyivWpoSZT20elRcFsFdNB7b_-VwroOsfYeDGG7FxqwZj6q_Tijk7zrb4t2NiugazIIzolpbxtQ0yUmuipIvCMhH1Y9t6170dZOLPq3hIB2ZTznxjEmPYO4KiSImKX82OLcZKr7oil4dsaGXnzvnrhcrzOt6VwzQ5qJWfFMvXsItoeUgo4Ac3ifP4_B8gOUsWOTsjUVkFRD8h7a1iQ8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی جدید از پل کهورستان شهرستان خمیر که طی حملات دیشب منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135038" target="_blank">📅 14:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135037">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135037" target="_blank">📅 14:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135035">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=f2E0GB_gS18AbZoLy_IBDtFcG_pfSavo6qUIqhdkuiCYHRz5q9BwAUpceGTMtjFzWdGiv348uDOd1w9aOYwnG3zmIs6TFUuF0tfwtYQO521Tl5_GvbfMx4tw8i6LE6joNyVjdwzopl8Oud9bsvRR_fSSAW1u7WpaeSSO5Xfc_4ce507VJnAYtWdCGeg89WAcT22O_g8mZpU3lMFzoFfbz2vTgRdvodbS8UGIAfB834YoHfYaI0B1Q8UT6FxmCPpH2w0ltC58EOLsRe9w16bOcEAkUzshFk2XmRGmb0I-LWUivturCh6ukJAks-w2JuC5RM7uXJ61Fh0v3GBYpw1QUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=f2E0GB_gS18AbZoLy_IBDtFcG_pfSavo6qUIqhdkuiCYHRz5q9BwAUpceGTMtjFzWdGiv348uDOd1w9aOYwnG3zmIs6TFUuF0tfwtYQO521Tl5_GvbfMx4tw8i6LE6joNyVjdwzopl8Oud9bsvRR_fSSAW1u7WpaeSSO5Xfc_4ce507VJnAYtWdCGeg89WAcT22O_g8mZpU3lMFzoFfbz2vTgRdvodbS8UGIAfB834YoHfYaI0B1Q8UT6FxmCPpH2w0ltC58EOLsRe9w16bOcEAkUzshFk2XmRGmb0I-LWUivturCh6ukJAks-w2JuC5RM7uXJ61Fh0v3GBYpw1QUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی، تحلیلگر اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن
🔴
الان هم اگه سپاه تو تنگه هرمز حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور مارو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135035" target="_blank">📅 14:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135034">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvwRkM-rawA0cJG59hLMFveyE9ftclITBpbWib4flgd_aGXq3jmwyXB3HmymOzCagWliAhokFTbQs2plmitZVpuQ4VxgcgS9xGoLYaiZHcd3kTkQQabUpXz9M9CsQeGW0TkgZJKgntM-QAAT6hHpqucF2lI-KLIUaHhJF4WJJiVWZp_7wjYepEzBd548pPUcS9sy8reqXISH_469Cjs6mNNj8hQOfJX-WhZrza1e2_fKxcssQ9r1gYPlgpwHgy8-KtZtxvbUuu-NaBEIEfVMdzjS6tLnXMQzJg10ZKFHCdsv-c-gAY0__1MuNo7yjDG4C_HsRXMCN5wGJZNRavYC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل هم در حال تخریب شدید زیرساخت‌های حزب‌الله تو جنوب لبنانه. (زوطر شرقی - غربی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135034" target="_blank">📅 14:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135033">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/135033" target="_blank">📅 14:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135032">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lja31KU_fr_egVxKyeuhwGOp0RjPPAv4hEsM2l97301tLQ9_A22n-MhDymTOLMJKbbtVNFrNg7T-2fJPyeX03ZKbZHkGUqYCytXC_RrcfWP1QvSpiumHtFS9ZhmMdfSjbAcge-NQGZ-rxyYQ0RMP-MsYZ7SkeTJWhlyexXI65JEuVgP9Pfzfix49z_OeruaLhyXGN-6uJyTumCK-i-_vnuRN0sL83ieeQGUwph9EClZjVN5EvFiOaU23fX5H41ES6u9f4amWLYUNI3LNQDves0wuFA0OkoAMM9gbHKyG00NrnfOakywfySE5k6qaQN9w-lxT8rFcAqU1RKVQav-3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+اونجا رو می‌بینی آقای رنگو؟
اونا می‌خواستن برن فلسطین رو آزاد کنن، اما حالا از ترس حمله آمریکا حتی وجودشو ندارن برن جنوب کشور خودشون
اونا خیلی حرام زاده ان آقای رنگو.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135032" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135031">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=FsVgheO6YRcUhtAYQw-SiHwUiC86ZqIM1M6i0cBi5xdk6msojzJ3XofNqIGu_LF-pmUJF70R3W1tHc6MYtaDMzSTgvis4BNXnP5qzQZfBQCJw5hSN6n-peSfSX8aALW0qDYMZkqr1UBLI6xF5F8cCtAtqs13YsDe2R1oJeoq1xoy1QFTcqdPzXbQtHHCGTP93fMepajqT2NJzQ_g2wxQPXoB3IJQfGMGg7_lUCHxGMeiL1kKKYCCo6YJWF5FZUyzNCjbOjvdxm5rb8kXj9awqEapNLJLUjA3naoQdglrmcjJ9eJDQYxuiXUkHegc7cYrAzBePIJGNEWAqxq3aWkA1TkCl8DC6wukl9HrXQ6EV-LIqZb1OGXFJz0IYzUoUXUCRTFLK3qUqLdZfbYb7CklexehRs3sRGicNn4fgBrnaois3RHaeVYSYgPo3Ql0MzGkSPKe_aWl0iYVftLOsWkGT-ZlnukFMPbPuMMuin6UcFvrpqQPun_6jzj_1XnDJqnEH9ch7L0YQsXTdsPfEJh43eHCtYfY4ER7MjUz-uh7Bji1ppSY3tVqAeOQKyFn7AojUhwkoH5OIdmZDlGBub6Uj1S1tQZR8H1WFG55LIluUuDSJ8tAIougsD_Qa1yr5ExZVfx4tqBOoqquPnkNgo1yhKDVOQOBB4maZBQUmIDV5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=FsVgheO6YRcUhtAYQw-SiHwUiC86ZqIM1M6i0cBi5xdk6msojzJ3XofNqIGu_LF-pmUJF70R3W1tHc6MYtaDMzSTgvis4BNXnP5qzQZfBQCJw5hSN6n-peSfSX8aALW0qDYMZkqr1UBLI6xF5F8cCtAtqs13YsDe2R1oJeoq1xoy1QFTcqdPzXbQtHHCGTP93fMepajqT2NJzQ_g2wxQPXoB3IJQfGMGg7_lUCHxGMeiL1kKKYCCo6YJWF5FZUyzNCjbOjvdxm5rb8kXj9awqEapNLJLUjA3naoQdglrmcjJ9eJDQYxuiXUkHegc7cYrAzBePIJGNEWAqxq3aWkA1TkCl8DC6wukl9HrXQ6EV-LIqZb1OGXFJz0IYzUoUXUCRTFLK3qUqLdZfbYb7CklexehRs3sRGicNn4fgBrnaois3RHaeVYSYgPo3Ql0MzGkSPKe_aWl0iYVftLOsWkGT-ZlnukFMPbPuMMuin6UcFvrpqQPun_6jzj_1XnDJqnEH9ch7L0YQsXTdsPfEJh43eHCtYfY4ER7MjUz-uh7Bji1ppSY3tVqAeOQKyFn7AojUhwkoH5OIdmZDlGBub6Uj1S1tQZR8H1WFG55LIluUuDSJ8tAIougsD_Qa1yr5ExZVfx4tqBOoqquPnkNgo1yhKDVOQOBB4maZBQUmIDV5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت پل‌ها و مسیرهای مواصلاتی هرمزگان پس از حملات آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135031" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135030">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هم اکنون یک اسکادران بزرگ از جنگنده‌های F-16 آمریکایی با استفاده از چهار هواپیمای تانکر سوخت، در حال حرکت به سمت خاورمیانه می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135030" target="_blank">📅 14:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135029">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فرماندار ایرانشهر: در حال حاضر، عملیات بازسازی خرابی‌های ناشی از حملات آمریکا در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135029" target="_blank">📅 14:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135028">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF-0gTEUbr5b5K1_EMsN3AsO8g0ABN-4JKTTCNUpwe0YJO9gv8E03RkvyLYY-GIBJ8v2K5fNnmMtg12WK1JeuuyM5VnWmL1sqlyPqNgcgHbAy8xrLWHZywW3MZYV209DtJ0WbeSVY4ql4Sb_O8A9MlFfwgaCLO-qhrHpYGnUakNKRPStHM6p_d3O1q6PT1BiP1rB4mbKkuKIUhhNa1mXNN8w9YYPYXzfneWDpUQTB62D_aRaM7sCdkp86ChZJzjvppoT_cr6QAf4F8amnLgvw3gl01QLVoY2MN191up6yvstPK9g5NmJNm6zmQ41uOTJFTli-1lVA0KOAci9YFfxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کامنت‌های پویش جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135028" target="_blank">📅 14:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135027">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سایت داده‌های کشتیرانی کپلر:
ترافیک کشتی‌ها از تنگه هرمز دیروز به تنها ۸ کشتی کاهش یافت که پایین‌ترین میزان در ۳ هفته اخیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135027" target="_blank">📅 14:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHYREC3ytBPPtBFyrLaeipdy_LGutk-5N12asJOJe0Ms6nbuHiJdiiiBjONaFer8rezvUEMvwd7EzaIGC3Ugpc2juQMU4-6YjC0Y_cLWaRLgTM6kAk4-SLqpJN_ziBj6TuqDdj2rJi3JCHNWReaMuj1tl-ucDxpQfCrQ1GHKkobDATFyKnZkvvgKFC1Ia7H5VOvmc1GmqIECjE5A8V-ALMMh5IXaEzzHX6G-XoBcYdt3xBl-0oWSI8Y3TGoxvzsyiau4TZ6YTDLYCCKjWUFCfZwXe3mwBNKqoolY5ycQe-6ktlTd1ASQku8bOQ-FQuWjjpiqLhObtYsTK_a1RuC50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135026" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135025">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدخشان از دست طالبان لغزید
🔴
گروه تازه‌ تاسیس مخالف طالبان موسوم به سپاهیان میهن صبح امروز موفق شد برای مدت کوتاهی کنترل شهرستان یفتل در استان بدخشان افغانستان را از دست طالبان خارج کند
🔴
این گروه همچنین مدعی شده پیش از آغاز ضدحمله طالبان، بخشی از تجهیزات نظامی مستقر در منطقه را به غنیمت گرفته است
🔴
اگرچه طالبان در ادامه با اجرای عملیات متقابل، کنترل منطقه را دوباره به دست آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135025" target="_blank">📅 14:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135023">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9pBK0O-nr2F8dwqlVl78DEdf9QStVD_I_rjf5mX3wn9NgWU9QjoeMdI1HC3FgJv2Kg8O1ZZ1SJFq5biV6MHbRbLH1C9MZ6jtGMUIal6rdpDZB0ET-rR2jWSYyY4q3sODLKhnUJYeEPEDWpKmSIVFqZMZJQvNlh4687UKCNXLryn2_W_H8tGMHHj8WiulP-r6bVRwnpTv-mzneujqW6LP3fYZwsCE4_7FavjzkAjSS_DoFvmcH2WPK5NzcmWeq3kvqhH7CS3Ti8gWX3fcyFIH1an4PS5wT90QcsHStl5ZVbZ1eYydKTzq4WI7l_LuMetfjNCr3Xo221JOmJbjSqkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر دوباره همه را غافلگیر کرد؛ بازار در تب‌وتاب افزایش قیمت
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135023" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRsrTGfQVNTLhI4zCrv8QkaN6PqcN8oa-1G_dJ0bTKRXKnIfsd1fzlyJVk64BEHJJwq2V2llLqbxnsBZBG-AVh10K-3qlYvAreHuQrxBRzlavqBKwUgz2BIA8uhh-PqNtttGlLWHxjRrwnpHXvyViKLaidtBFfTrREPsDkjaS1ewpM5PwmkLsdhOSS54J5nj2E8Zu_kPbEp704LFCBRlqGU4IeD7otmN3tJVx7aHymALAQIQm2El3aHd_dFYEpbll_mzeOceie04beWrwDK-ok4JkWtlAe6F-BJiQP0jjg6VHQmsJKcab84FPGSsDB_pnk_beUgY42-rqHWmajG7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۰ فروند ترابری نظامی C-17A به خاورمیانه اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135022" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
توانیر: همه روزی ۱ ساعت کولرو خاموش کنن تا به جنوب کمک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/135021" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135020" target="_blank">📅 13:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سفارت آمریکا در عراق سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135019" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در سخنرانی دیشب خود که در ساعات پربیننده انجام شد، به‌ندرت به درگیری با ایران اشاره کرد
🔴
رئیس‌جمهور دونالد ترامپ در شرایط جنگی به دنبال یک سخنرانی نادر در ساعات پربیننده بود تا مستقیماً با مردم آمریکا سخن بگوید، اما او از این فرصت استفاده نکرد تا به‌وضوح چشم‌انداز خود را برای مسیر پیش‌روی درگیری با ایران - که در روزهای اخیر تشدید شده - ترسیم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135018" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
دلار هم اکنون 188,250
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/135017" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFfjEPBx4jbrTSnn6ES6ptA7D_qfM_sgzh2Uvlx2VvTy_tQJqiPcFzqqJ44yUmy10nDiBZrBw-Td4LOoNI1SfNGYyTTiqlJcLRj-_lyWAosDW_eBgpkFKyrTIf_09wYH6sgZOhiMy01Z_ylIwf_IDUu6I90XJoyyzB3C_NaSQft680s_ojsPVH9pJSbfSvf1MVt4LXPv-yoYAdlkyEFjo6TCx09rcyKNFcepGhAPkEe-AKgqCCzSoGu3KXXYvH92tcXWC2kXsnaWVnusf5jfU9q1iIBvesjORtafxbUAP9rPDgWYN2abIFCFmt0Pjm2fArqip5jxBmQ5EAwk3uQLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در همین حال، ارتش اسرائیل به تضعیف زیرساخت‌های حزب‌الله ادامه می‌دهد و گزارش‌ها حاکی از تخریب گسترده در شهر زوطر الشرقیه در جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/135016" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135015" target="_blank">📅 13:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع امنیتی دریایی گزارش داد: افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135014" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/135013" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135012" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
آمریکا: حملات ایران به کشورهای حوزه خلیج فارس هیچ تاثیر عملیاتی بر نیروهای آمریکایی نداشته است
🔴
سخنگوی سرفرماندهی مرکزی ایالات متحده، سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/135011" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لغو پرتاب استارشیپ؛ نقص فنی موتورها پرتاب اسپیس ایکس را متوقف کرد
🔴
شرکت اسپیس ایکس دومین پرتاب آزمایشی راکت ارتقایافته استارشیپ V3 را به دلیل روشن‌نشدن چهار موتور رپتور در فرایند احتراق به‌طور ناگهانی متوقف کرد. ایلان ماسک اعلام کرده است که سیستم خودکار لغو پرتاب به‌موقع عمل کرده و تیم فنی باید دو موتور را تعویض کند. پرتاب بعدی این موشک غول‌پیکر زودتر از هفته آینده انجام نخواهد شد.
🔴
این حادثه درست در زمانی رخ داد که اسپیس ایکس پس از بزرگ‌ترین عرضه اولیه تاریخ، فشار زیادی را در بازار بورس تحمل می‌کند. به دنبال این لغو پرتاب، ارزش سهام شرکت بیش از ۴ درصد افت کرد و به زیر قیمت عرضه اولیه (۱۳۵ دلار) رسید. این مأموریت قرار بود ماهواره‌های نسل جدید استارلینک را برای راه‌اندازی پروژه دیتاسنترهای مداری به فضا ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/135010" target="_blank">📅 12:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otUNFHIq-Czsj7HRzFllij3-Uuwq_A5Uh-BUKu_hBT6JbH-OwEJZ1yPikFnI4inuE_LXUZ-n7rTf8dzAAO2EMPwjH_y8Dt5UjHZ3JOS36eWjHeyKusjf5glV_jZ-5jPqJbhuPon43DHE2UnJ2iiAQj2uS5lRr_txQ8umi-rO4yaaOYA8GQ_sbEoHs5owi7b7ff5f21G2WhSCluKVs8wtBspJmrz0OXXujPv1ihLTB67iZW7y68D4hgjWoEKW4OulaUNzx0YHegJWRRpoVrhambaS-Gy4Jw4IXDSr_B8KUrg1Zn3KlOBPTdRUwvnMzAgXKuEQZvA5vAhP-OI7oxMA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد برای اولین بار در جام جهانی، علاوه بر جام؛ انگشتر قهرمانی هم به تیم قهرمان
تعلق میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/135009" target="_blank">📅 12:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/135008" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N11mXOvQQGXXOgvoqqmybRqUKOr6G1_0aeCgPM7Bxwdw7ufgOicUkYOiz24gQaVZjCHYlod7WtUBF1Pq0rlfS7S-9kXRND57eFIWRvNNen8boZFrQgsfQXRa5Q0Q9OQB4tTeh7io-Jr88nH5fzGqtXK8ueyPFreSjAyLZ0twQXumoLB9WFSJdJqOOUSWGnDkmy4ASSzRQrWaE_Lt4B414lD7ub1aNk1Jh-OvaFPQ5oMoKbZspFokECBC1EXEXi1-tdsyR49MAyFbdlQa2BklMhQtYp8oQGJCBWoO9z4zM7_n3oKEvjj2NafLpu0Yu6ZfDTE4wstNx737QhW5rtm02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست کم ده ترابری از پایگاه‌های آمریکا در آلمان، یک پرواز اطلاعاتی از خاک ایتالیا و یک سوخت‌رسان و یک ترابری از آمریکا به سمت خاورمیانه در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/135005" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/135004" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135001" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFTsyCF-4RjihZFp5G5ox4iJvq6lCZpGjtclfuEdHP2SjFZ1012QsofxjxRjEMajeBehXTGFygnOc8mnUGdUsWIcQogWdUSg_U03mbDIVeKB0fKlykQphWyf4U1ax6GsGf_QQCjaBQDu9F6KYr5_8o7KxBixIawvBIdmAyj0iucauFSuDimgnCB089BGoOVdqpf0vinYMbQdbOlfe9zSTH8OTmHIDJG5jCk0pgZVsUDXO6blaNEghnivf6KPS9AZI12xWwUsTSxtDn83Ub9I0iM1A5DVZwDqWEmKecQ6WKdVI3fQgwd2wKu1-wNCcCebrXZO-3s29pLEne5zLAlLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا صدور گواهی امنیتی SSL را برای خبرگزاری فارس مسدود کرد که این موضوع باعث میشه اخبار این خبرگزاری به مرور از گوگل پاک شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135000" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سپاه: چندین جنگنده و سوخت‌رسان آمریکا را با حملات خود منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134999" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شبکه‌های تلویزیونی که این سخنرانی من را پخش نمی‌کنند، باید مجوزهایشان باطل شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/134997" target="_blank">📅 11:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس پلیس راه مازندران: جاده هراز به صورت موقت برای اجرای چند عملیات عمرانی ‌۲۹ و ۳۰ تیرماه جاری مسدود می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134996" target="_blank">📅 11:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
🔴
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/134995" target="_blank">📅 11:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اسرائیل در مورد نقشه ترور به ترامپ چه گفته بود؟
🔴
اکسیوس نوشت: در جریان سفر ترامپ به آنکارا، تل‌آویو به واشنگتن هشدار داد که یک مقام ایرانی درباره تلاش برای ترور رئیس‌جمهور آمریکا در زمانی که او در ترکیه حضور داشت، صحبت کرده است.
🔴
این اطلاعات باعث افزایش تدابیر امنیتی شد. از جمله این اقدامات، جابه‌جایی ترامپ را یک هواپیمای قدیمی‌تر «ایرفورس وان» (هواپیمای ریاست‌جمهوری آمریکا) بود.
🔴
با این حال، مقام‌های آمریکایی گفتند این اطلاعات بر اساس یک منبع واحد و تاییدنشده بوده و جنبه برنامه عملیاتی واقعی نداشته است.
🔴
بر اساس اطلاعات اسرائیل یک مقام ایرانی در گفت‌وگو با همکارانش گفته‌بود که ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🔴
نیروهای امنیتی ترکیه نیز این ادعا را بررسی و اعلام کردند هیچ طرح مشخصی برای ترور ترامپ در آنکارا پیدا نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/134994" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
