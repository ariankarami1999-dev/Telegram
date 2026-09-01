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
<img src="https://cdn4.telesco.pe/file/tH7D_vfb_xFyvns1-X4wHx-36w1UWVO1rWaZTMloPuodItnEVMQDS3WNFfHAJEhA220J2lQ2TlTZ_cQNLAkdE58RY24wQ7D1GHkNl-WfkQ9_CP_4bVCznuDjMK3mUopaeDmhJetyoCCKmNHiuu1y6-_qPeDNelCsrY6qgwYO37xJZzAxIWiDue55UfOdr65iiCDMpuX0qvw_ACU-BejIhLXJ6pcTQETCGZR4btl5U8oF57dZ9M-RUL-1JP7TVxU0cOAno9D-u8238rKMkhww7wR6cXXdVewq5AEwXYz91vnGN8hFo2rbG5f14QbUXNjCa00IdMbrJ-iimtuatOtPpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله آمریکا به همون همیشگی!
سیریک
!</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SBoxxx/20424" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/20423" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SBoxxx/20422" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله به عسلویه!</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/20421" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">موشک خمینی در هوا منفجر شد!</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/20420" target="_blank">📅 22:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آژیر خطر در قطر!</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/20419" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7gba8nAQt44qZ7TFjasTmITI3Mgymv9veEjDeLVRxvJRiBpx_79gieKzfiL71GD8jAytNWrVJ3BPfcCP9NXVOAI9HK-5a3wxVbhmRR7AeCeHuKNaUI4LijQWSt_pmk_T7KDFxiO7lgYPfwzLAqySG9gzrA_41GFWPXXsnhEoTVRd9mlpE1yfEFMfYG6MFcbB-vvm6HIvYc1DlJzH9MrzEXweLcj1MuXPs8YSJ-Vu9kVwsu5-owJVlNQPn_IaQjISPdQ-zwm8350NuVMSxkwr9YNqFQ8ct0IFFRPs_eyz_navMg8HmzqRAfjXQmLFCdV_xQrpGbtTtmIXF3IDNImhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن دو هواپیما نیستند پس احتمال حمله به تهران هم هست.</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/20418" target="_blank">📅 22:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">‏ترامپ:
حملات جدید آمریکا سیستم راداری ایران  و کارخانه های تن ماهی را هدف قرار داد
@Piknikanalyst</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/20417" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!  کور شد بدبخت!</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/20416" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/20415" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دقایقی پیش فرودگاه جیرفت مورد حمله هوایی قرار گرفت.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/20414" target="_blank">📅 21:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">موشک خمینی در هوا منفجر شد!</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/20413" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">موشک خمینی در هوا منفجر شد!</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/20412" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">موشک های بالستیک از ایران شلیک شدند</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/20411" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «مجازات شدیدی در انتظار متجاوزان است.  آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/20410" target="_blank">📅 21:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«مجازات شدیدی در انتظار متجاوزان است.
آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/20409" target="_blank">📅 21:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:
«ایالات متحده همین حالا در حال حمله به اهداف ایرانی در نزدیکی تنگه هرمز است. این حملات گسترده و قدرتمند هستند و در واکنش به تلاش ناموفق ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه هرمز انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (تمام مین‌ها کاملاً پاکسازی یا منفجر شده‌اند).
همچنین در واکنش به شلیک هشت موشک از سوی ایران به پایگاه نظامی ما در اردن که همه آن‌ها با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه، اقدام تلافی‌جویانه‌ای انجام دهد، بار دیگر و در سطحی بسیار شدیدتر و گسترده‌تر هدف قرار خواهد گرفت؛ اما این بزرگ‌ترین حمله از همه نخواهد بود. بزرگ‌ترین حمله همچنان در حال آماده کردن است و هنگامی که به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!»
— رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/20408" target="_blank">📅 21:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دور جدید حملات آمریکا</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/20407" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تسنیم:
برخی منابع از شلیک موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه خبر می‌دهند</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/20406" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">– گزارش‌های تأیید نشده حاکی از آن است که موشک‌های زمین به زمین دیگری، احتمالاً HIMARS یا ATACMS، از بحرین شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/20405" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده شروع به حمله به اهداف نیروی دریایی سپاه پاسداران انقلاب اسلامی (IRGC) در ایران کردند.
این حملات پس از تلاش‌های اخیر IRGC برای حمله به کشتی‌های تجاری در تنگه هرمز و علیه نظامیان آمریکایی مستقر در منطقه صورت گرفته است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/20404" target="_blank">📅 20:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به نظرم نیازی نیست چون خود آمریکایی ها هر هفته چند بار پیش دستی می‌کنند</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20403" target="_blank">📅 20:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">— سفارت‌های ایالات متحده در اسرائیل، قطر و عراق هشدار امنیتی صادر کرده‌اند و از آمریکایی‌های ساکن در سراسر خاورمیانه خواسته‌اند در میان نگرانی‌ها درباره تشدید بیشتر منطقه‌ای، «هوشیاری بالاتری» به خرج دهند.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20402" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">— انفجارهایی در بندرعباس، سیریک، قشم، چابهار،لارک، جاسک و میناب گزارش شده است.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/20401" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/20400" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/20399" target="_blank">📅 19:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رئیس مجلس ایران از شهروندان خواست مصرف بنزین را کاهش دهند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20398" target="_blank">📅 19:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20397" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20396" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزیر راه:
رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20395" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20394" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏نبویان:   اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20392" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏نبویان:
اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20391" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20390" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20389" target="_blank">📅 12:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20388" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssZqkTP10cx4kyUqPRsiqqm88ZbIS-R1cZQdF-8_G50dLPFi4NhePCOGP0J735yuIWVMBZBfm9qU2h7SwJ0-kfyeFQo9u3lGD-mcuMAZp10R6TXFiNv4ynqHq_x_g-4cVjPSFdmfcBB5kPdg3tOhRgYa_8GFFzQ9UnY1pthEVrCLWB60VLUsmtrmQ8oVeKjErK9o-cobKW0fwQjf_3jVXLYljQUexEeEQK7Rb256lgItyr6dyolZYJIjokoKlwVFEwKQHza2RgSaRZfV6stz-cc0vRGBT_JJqZkexCLwhOXHt5QwWWp-fDwR8BbDCa7bCI-DUJa_conH1LmroVvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان نیروی دریایی دیده می شود! حتی سرپرست فعلی سازمان اطلاعات سپاه نیز در این لیست می باشد.
⏺
هدف آمریکا از تهیه این لیست اجرای یک عملیات روانی و همچنین دریافت اطلاعات دقیق از وضعیت این فرماندهان می باشد. همچنین به نظر می رسد آمریکایی ها با انتشار زودهنگام و غیر دقیق این لیست عجله در دریافت اطلاعات دارند .
⏺
گزارشی مبنی بر نشر این لیست در مجموعه های خاصی وجود دارد که مرتبط با اعضای نیروهای مسلح هست، نکات بسیاری وجود دارد که فکر میکنم اگر بگویم برای خودم دردسر ایجاد می شود پس فعلا از گفتن آن پرهیز می کنم. اما جدی بگیرید اوضاع را !
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20387" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU2E7Fouphn6nBc19TzChJ4vu1jeUF57tU7KFA2h3qa3uQWtEEGktg4jbrWAC70cKAQK4S-PUAhLWfa-Q40jTDWqJr3tk9aO4e58rseAirYgP52XLIqE1QcsdYiN1vkG2RIisAnrNNYkEN5TZ_lwyJTOJbxBQdxScPuiG4-hPuCDVPoEF74PDO9GU6sgunwWETbsO_gBDkO4Vj-Un4Lv1XpS_3CYYLh-Gw2Drdoym2AJ7SJvkbvBPOL7mLsqQ6pYf2Yydt0L7KJk4LZjzxZrwLFuavp6D_cwtJ8qa7HTveOK6tO6O-JZM1OyJRvu7YlKnSW38y2TMNaj7Z6vd80cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر سردار حسن زاده در صفحه وزارت جنگ آمریکا به عنوان فرد ترور شده !
🚫
دپارتمان جنگ ایالات متحده سایتی برای دریافت اطلاعات از برخی فرماندهان ارشد سپاه تهیه کرده است! در این سایت لیست قابل مشاهده است که صرفا به چند فرمانده به صورت پراکنده می پردازد، نکته جالب اینجاست روی تصویر شهید خادمی علامت ضربدر قرمز خورده است به این معنی که به شهادت رسیده است! حالا جالب تر اینجاست روی سردار سرتیپ حسن زاده فرمانده سپاه محمد رسول الله تهران نیز همین ضربدر دیده می شود!
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20386" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-cBiyqkuRSaqsSDbd2gDMPmlMWakZXpl11OpnChPgocCkJ-m6ujXlT03VBwRj3Lzs2pSm55JqZGB19eNZd40Gq11It--N2k3DEAp9S4e9yUa5gyxFrCxe-O03JjZ_PupmydeKaEOUU1KmGFf8I_XTVanv8tHUriQfcbuyaYMYFN5pp3Xbg02MPm46qBLDzIgNd6Ctq1upvHz3KM5MC9MPSpq1v6sUxegLjrFZvQ_6t7-Ni6W9SHGVuYlsb_MZQFECi-so0WTuuQLBQMFGxUfsgIxzbCUcWMuSLaP43RLrVhpirkh5Z5qnBXxK1qfp1JzKtQbu2h5y73XTXf_S2FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.
با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20385" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این چیزی که ما اکنون تجربه می کنیم عملاً نوعی «تجربه نزدیک به زندگی» است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20384" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجار در سیریک</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20383" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایران یک تانکر نفتی سعودی را در تنگه هرمز متوقف کرد.
بر اساس گزارش خبرگزاری فارس، یک تانکر نفتی بزرگ سعودی در حالی که از مسیر جنوبی تنگه هرمز عبور می‌کرد، متوقف شد.
ظرفیت این تانکر 2 میلیون بشکه نفت است.
طبق این گزارش، در حالی که این کشتی از تنگه عبور می‌کرد، ناگهان سیستم شناسایی خودکار آن فعال شد. فعال شدن ناگهانی سیستم AIS نشان می‌دهد که یا به این کشتی دستور داده شده بود تا موقعیت خود را اعلام کند، یا اینکه در شرایط اضطراری در تلاش برای اعلام حضور خود بوده است.
امروز، سازمان UKMTO گزارش داد که گزارش‌هایی مبنی بر وقوع یک حادثه امنیتی مربوط به یک تانکر نفتی دریافت کرده است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20382" target="_blank">📅 00:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20381" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovrVLRQ9UGa0xGOLaN1BgQnEuxTT4DGm1zsiGTnWzkGEpa8Gk3xklqL8bRDOzjQXbR3-lEq5p1OvDlXXLimq8Ao_FzKBMpN2SxOkrKH7KyUX5il3ON1APH8xIEhpLRzaPJP5m0jQL5JWNshfzGfN_p91cOz9RPnEMGdM5JWDycW5uCtFtMIQXePZhLuWVFgPmSAmeEbg6YWrh8ckZegWQXBhMuAFplVBBV-NpLWibLbfmkmyGxv3b46QfYEMabuZnidfZLlmNXhPjqSC2rZgBxweMspkCVIiG2PnUmoh_tD_VMYTk_n3x4DGCzhE_ICX498d7FEJb_X7gU76Hes5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار رشدهای عالی را در طلا شاهد بودیم.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20380" target="_blank">📅 00:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش های اولیه از حمله موشکی آمریکا به یک نفتکش ایران در اقیانوس هند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20379" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20378" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20377" target="_blank">📅 23:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDe8MHjy1vHw6FDb4Rmg7OGJwIFFUZO12hdcnwhOPDRfPRblUZHJitZuSiw8OEZPS9GSW2m-Rhtcx9VPBJHZkiYNkBhgY3gEYxVIhAu4XAcc1t-6RDtwb80eweYNjhCtBhFCSQHQBZHgLYVquizWjoTKdmvrG0EyHiL5W60D4ak_gLCp_dBzLaSfSZqhvFxGtSL1Ycy03Dw2f95LWWQ8aRCpuLTyGY-PV5PZVkskrro_go8iRlz-OctermcZb3tyvtx5fHqV7v8-dtfRM2cdvrnkpe5LuwNx1j0te4x8WDRXGVFsD4Yf9Oz62XgPat8vAzBcvIn4xy1GIbl_7MyNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوک‌زده شده‌اند.
ما شاهد صف‌های ۳ تا ۴ ساعته در جایگاه‌های سوخت ایران هستیم.
ایران به دلیل از دست دادن توان اقتصادی خود، به اقدامات نظامی روی آورده است.
می‌خواهم از اتحادیه اروپا بابت حمایت آن از عملیات موسوم به «Economic Outcast» تشکر کنم.
خبرنگار: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
بسنت: لازم نیست اقتصاد ایران فروبپاشد؛ فقط کافی است حکومت ایران به خود بیاید.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سرتیپ ابوالفضل شکارچی، سخنگوی ارشد نیروهای مسلح ایران: صدها نیروی آمریکایی در طول جنگ کشته و هزاران نفر زخمی شدند
➡️
در این جنگ نابرابر، نیروهای مسلح ایران با استفاده از تاکتیک‌های جدید و نامتقارن در مقابل توانایی‌های فوق مدرن آمریکایی و صهیونیستی صف‌آرایی کردند و ضربات سنگینی به دشمن آمریکایی-صهیونیستی وارد کردند.
➡️
به عنوان مثال، هر زمان که یک پهپاد ۴۰ هزار دلاری ایرانی به سمت اهداف آمریکایی یا صهیونیستی پرتاب می‌شد، ارتش آمریکایی-صهیونیستی از چهار موشک به ارزش هر کدام ۴۰ میلیون دلار فقط برای رهگیری آن استفاده می‌کرد که نشان دهنده میزان خسارت مالی وارد شده به دشمنان آمریکایی-صهیونیستی توسط ایران است.
➡️
با وجود این هزینه‌ها برای آنها، پهپادها و موشک‌های بالستیک ایرانی همچنان از لایه‌های دفاعی آمریکایی و صهیونیستی عبور کرده و به اهداف مورد نظر خود در پایگاه‌های آمریکایی و سرزمین‌های اشغالی اصابت می‌کردند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20371" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد!
ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20370" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">میگویم اینکه خارج نرفتیم به این می ارزید که موقع برگشتن زیر تیغ «حافظه تاریخی» نرویم!
سبحان الله !</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20369" target="_blank">📅 11:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geVXf7m6qVNo_0sYtg3GZ3HFbkfkhbTHSV_GF44_8B6Qvmt55ylUVbDEPbi3Qlb9PDKl9wNBqSxGZUxZM-jePV21J15ZjXZeQhafSxUGBq--KuneVaFoF4dOUN6sCIRNUBx0u_RhXD3d6QdR4xdt3HTGuaO0s0bn1udmuKGSKMu0xKHyvCjWadvgVxPlEAIAZkXcongKPQgFFTd75uz3pyR0hA_-yE4lYLBjySRfewbnELGqwz4PHVMYYKot4IzcU03jOpZ07boH0la7hSDulaBAb-mGDFZiZIGbVMdwWRth7WXJT3LTQhpzgmt7kgNkJ9uaHT6otHr_JNUsF07Eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20368" target="_blank">📅 10:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که با یک پهپاد که از ایران به سمت آب‌های این کشور پرواز می‌کرد، مقابله کرده است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20367" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gENEectD-VB8iJRJqvRyiVqo3CBl2SxNWui7u-pVcT9YRHyrxCLPVr6f-QQUcLKwv59vF7B8KncBwOnUKEo4LZNo7xH1IAKciVVDjRPObmY0psd0ENT78kaXvAqZ8I7lE7Qw1QMWVkJx4BsxcksBic0svQRgWAcR5k-Ahfi-hJLYIzLlH3frvXELKU6TI_M6EPPVUd9gggd3KjZEb5FRBYm5JlQcjBOZ0BhD0Le_9c_Y9RU4ydLZl3y7SO6Vy6HxbdTrs51mUf9PsM0z_gJQnIcDQq6TlWvj4M7WOpIY64hNpJonNTqeo3RwEFxns0-XD_f6UoSa88grqQgskkOPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20366" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔺
پایگاه آمریکایی «المنهاد» در امارات هدف پهپادهای ارتش
🔹
ارتش جمهوری اسلامی ایران، محل استقرار بالگردها و نیروهای آمریکایی در پایگاه «المنهاد» امارات را مورد هجوم پهپادهای انهدامی قرار داد.
👤
روابط عمومی ارتش:
🔸
از بامداد امروز در پاسخ به تجاوزات اخیر دشمن متجاوز و در انتقام شهدای دلیر سپاه پاسداران انقلاب اسلامی و مردم بی گناه ایران اسلامی در جزیره لارک، ارتش جمهوری اسلامی ایران، محل های استقرار بالگردها و نیروهای ارتش کودک کش آمریکا در پایگاه «المنهاد»  امارات را با شلیک دهها پهپاد انهدامی، هدف قرار دادند.
🔸
پایگاه المنهاد، یکی  از مراکز مهم پشتیبانی و جابه جایی هوایی نیروهای خارجی است.  روابط عمومی ارتش، با اشاره به تجاوز اخیر دشمن به جزیره لارک، اعلام کرد، رزمندگان ارتش جمهوری اسلامی برای تامین امنیت پایدار و حراست از سرزمین ایران اسلامی تا رفع تهدید دشمن از متطقه، ایستاده اند و انتقام خون همه شهدای جنگ تحمیلی را از نیروهای ترویست آمریکایی خواهند گرفت.
☑️</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20365" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBx-S5RCvSJh5DmBFHCXOD8Zi_TAdY8sNCFnPdxEH188TxVYgFUYHMEWAD3oBtp2eZEwWXUJO-_wjyMJfmVnLPwx6iqOPC0EUBmXgLYJDCSJbRicuBw9P5jhEH9z8Jz-ac3VlXOhKkMwFiIXCOhhPxanACDKGn3uUWV1glrFMQ-P9z8uia2Ggu0ccuo4eqOKhKfe1p0Q8zEwSCswD48yf1-CGjRw_EdQP_PnJK6XxSRa0qkPhn739Jk88lALMcw7QaJN4ziZJX-x7wIedd5BP42X9gktYaAvFAMuI6UNZRm2_UXfKJtAKo_lSrdeCiBDsfmz1e9KCArHt_ZuSHp07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20364" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
دور جدید عملیات نظامی ما در ایران تازه آغاز شده است</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/20363" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش هایی از حمله ایران به قطر</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/20362" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مدیر Secret Box بر این باور است که این تنش‌ها هنوز به جنگ نهایی موج ۵ ختم نمی‌شود و چند هفته ای دیگر زمان داریم.
لذا اگر تن ندارید لااقل آماده باشید.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20361" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادامه پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20360" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20359" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دلار ۲۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20358" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار در جزیره ایرانی سیریک</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20357" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارهای پی در پی در اردن</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20356" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20355" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAXLPyuYgAv53p4UQWKoke0AI8p55Cy5qDDZxpNIRkHU6VEvMc2FB3WvIzPxRBBpeYG1J4mZpBP2-iYPsHcVIJuRqftTlEWbqBzOcvUtZXktonSsVXfHdAEouFkf0ufEsBQy9hGZi8s3rf8AUY7FJMK-T0SVVpXdEDpo5tG4kHv6qZ0qU1MANFnR5hvHNjpbjH5y0jc5M6FymaVKYgM631L1IGtxhPRTkPpnwEWE12JbmcY-EvlW9NPWRvfGxeaUz0I3x2Zr2ghZbi00CANvDG9Uc0wfnT4_zzK1MIpMr23cMeafKWV9dwonPq4hoM-RSGmjIvrXLrFmYokexpsfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان
بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20354" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc-RCKkPj5L-HR3eDX5v3mSNr-3JRm45FVNFX_hki1hvjzjfYfvt0S47Fhpwd5CakdlBQR89HhbE5y8y3zwYFkb7C03lt99mXR6cVBmKPQ6SemYpC1zdpXTm51SzuXv6oWs_dGK6VXBaIA9IKtitGQsY6EDyt24wq64f_6F1y2HtEi0hR2HH9mAztTn5LDzQPnmbJ42lh0BQhpsCK9hNIvnN_Be_2B2TYakI2BzTQ42v7lCtmAoP1omaBWOpmKPGf9xWDvhvHOnl0sWgvc8lxcowAgp7HtEglG3EXZUUBwhBNFXY34WtexdjhiZ96vnJO19eWdXsRnzXLQu57OuJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20353" target="_blank">📅 00:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20352" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ4yoOdZ7DH7rIYqMmHjRGVkrStsGI5gHo3XQQ1BTTNGxrZSNvVkgopVYY5j9CgNHyzZs9XtyVGpeaplOWs44euylWzVLhlszPT7Q5uV0jl3D3MVKZHfXLViXGs3uCQnz57JhOqmDcqGMFaWwkRCuDMSTXioUqLy4OLom-RStxISCYc6w6YpEnW1fzVmXPlo_zH7DkYO3U-bwT2P3hBm_xTpACjRKY_83kd3rATHKZ93jaModKbdadQgB4zjDsboV0aGXkpHbvTHNbYGRm5CuYTwA5QeWe9fceFD2HERHbB57FMjx5V3x63pPBuikhLH_qqcSBy3T40OitTvUqRoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20351" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20350" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20349" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20348" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برخی منابع خبر از کشته شدن 70 نفر در حمله آمریکا می دهند که به نظرم اغراق آمیز است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20347" target="_blank">📅 23:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار دوباره در جنوب کشور!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20346" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20345" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وضعیت خریداران نفت در شرایط کنونی</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20344" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=gE7rNroXMqBYG-vv2lgJGJJRKgN4WkeFOEg2iTOWPFy8CY90lGF0SXhzXsKmaSnSb2ZF80XHA2c_R4u827J28VFX3zpXIB5pQlR9NcruUZUFWZWECffcImGCHtSAspBsVpH3ERxic84206swbRi0pmMsmicmXfHl-LB4Tu8eVlUAlGkphkpMUdqttfbtY4y3dz35_ImIegGXT8UX-ArIzmXrAAXt8FlbEgUn47z1WwQ9oDhr9cNPPl62ytL2ae-HbYkGvynMIBYDnPBlntKOzqHyHqxHQHbMT52ZOhcg-uVJDy4ZSPKTnmLlZIykOolvul0c2Duh8iN1NMcqj8nP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=gE7rNroXMqBYG-vv2lgJGJJRKgN4WkeFOEg2iTOWPFy8CY90lGF0SXhzXsKmaSnSb2ZF80XHA2c_R4u827J28VFX3zpXIB5pQlR9NcruUZUFWZWECffcImGCHtSAspBsVpH3ERxic84206swbRi0pmMsmicmXfHl-LB4Tu8eVlUAlGkphkpMUdqttfbtY4y3dz35_ImIegGXT8UX-ArIzmXrAAXt8FlbEgUn47z1WwQ9oDhr9cNPPl62ytL2ae-HbYkGvynMIBYDnPBlntKOzqHyHqxHQHbMT52ZOhcg-uVJDy4ZSPKTnmLlZIykOolvul0c2Duh8iN1NMcqj8nP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:  بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.   این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20343" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:
بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.
این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی اجازه عبور یک قایق ماهی‌گیری را هم از تنگه هرمز ندهند، هیچ مجوزی به هیچ طرفی داده نشود و هر طرفی که از دستورات صادره تخطی کرد، هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20342" target="_blank">📅 23:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20341" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اسمان ایران و منطقه  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20340" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ao52_cxJjFk-f5GKteB90DzuKzxi_G_mLrCq3TVT7pBJTDTZKc22Ru2JbXrjGk6pnYSiLu2vboEwuex_XGIvQf5m2q3XuZ1u0E3ibOzQeS9_uBtVjVNN-ycaUdILHT2zuG365q8f0IMjXgsvgvlGgetKmrFxJbQuyGxx3rPXZhb7x1XOYia8CS9QyZQ3CzD4CZHnY_LBBXA1oyPXyK8Otas2iW5OHFzgFSYFBghyGE5wC2k8u32wFIreTjdBCbGdy1DBOhL4pl9vjTg3o9gTXA2TLUTsNi-2klANfcfBZ4dESh-GGSBeFQSjfEA74COaiBp1xvbnRtZFHne3wpZ9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمان ایران و منطقه
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20339" target="_blank">📅 23:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20338" target="_blank">📅 23:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_8l8wtWdzW5fnrbEV7MPOQD0HhD4Gwmr3J3cwPxhMlTrT1LiyHz9NS3TGopBA1su9DS0r3FZbccXeznqGlgzu0AZBZ0A_EvFrNi-4Gft_rNc2ypqnqpPu00kRvU-qGKyNlCEND1drbRT1zJ7_1w9j2urbjNdw02cxO5xGPdCg8O5kw44ihQyORE00vXAKuJ-jMlrcmsB9MIG41aF15NDoQiBq8Jzh3M9eOVWDsyY1cdCV-1e6yan8nIYbNll_vxCJxq1ilEEpzQ_iWktR-f3coUac7QypqgOW3zCce0d9r9Jqaeh2DcOu-Ro3BT-eNmcMsWkQOrOo5Tjco9W8ivmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدافزارهای داخلی از آنچه می پندارید به شما نزدیک ترند....</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20337" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مرندی :  رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20336" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این صوتی را عصر ضبط کرده بودم و اتفاقاً محور آن همین وضعیت سیال و پرنوسان خبری — خصوصاً برای یک ایرانی — است و جالب تر اینکه از مرندی (خریدار سنگین نفت و خالی کننده شبه جزیره عربستان) هم یاد کرده بودم...
برای هشتگ گذاشتن تاخیری حاصل شد و در همین فاصله دوباره جنگ شد و مرندی و ....
سبحان الله!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20335" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB50GhFok70_saXQAlhaMqNJ3RJnScHMMLfW2SxPq3vBwEi5tyKbY2GjrzkoFrxeG3Fab_3xl_c_cEy_fiSb_t4R3BDOj1UMOHHyY4dvvX7Pn-dr2IhGZFAmZ7_wPvNWmGxP0Y2xg7RbJXiP8zvH5ugocmvLcUDN3Sb2jATmeH2qFNcLlXd94ixFIiChxNOy8r17pBoY2o-VFk2CDlfR3hMgzv-vX0IG0QrCA9_0C4G7Qdjn7LXq8-izKSygD7fVfmrZQdaY9_flFqkttAm4eaEdzLUP9dQyRH78JsJgEiQ3UaMf3Wp9OtZmpjhktB57AyvxnU76wW9betrx2MtfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی :
رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20334" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه عراقی به نقل از یک منبع ایرانی:   شهادت شماری در پی حمله آمریکا به جزیره لارک در جنوب کشور</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20333" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20332">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال Secret Box بی تردید ناهمگن ترین کانال سیاسی فضای فارسی زبان تلگرام است!
از بسیجی مبعوث شده کف میدان تا شاه اللهی مخلص اسرائیل اینجا هستند!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20332" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خب گویا لارک بوده نه خارک!  مقام آمریکایی به شبکه الجزیره اعلام کرد:    نیروهای این کشور امروز به یک پرتاب گر موشک در جزیره لارک حمله و آن را نابود کردند. مقامات آمریکایی اعلام کردند این سامانه آماده شلیک موشک به طرف تنگه هرمز بوده است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20331" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=Ex0qZ1ER5QevJlDWS0py0W4qk-Wcn2kTMePyqGTUyNyyUBYkwNzM5H6Onv-eN0fD8H3GUs7bVTwkFufr7LdNMETUcSGP--GO_mJguzcv0iwLye4wSQh_lM5NmmlfBgoMkkdTfscycV04LTm6ifSrFRQIWuyeYG4mr3RfoYfWMXwnYJUzM1F-hqOQC6rsrtfn-i5xbZyONw_CbdwiGFqlzKeK1CxlqKrlqth0j_qkgW91KtYhIbINJ-mY_4xlOOw2QfSdjBBoVIB1j7dNUvVX-tiVyPv6SovmlUXqcRpbTAimv1gxoWMhquuPkjyuI00l8gKXciKvnhLZ97G-gDDI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=Ex0qZ1ER5QevJlDWS0py0W4qk-Wcn2kTMePyqGTUyNyyUBYkwNzM5H6Onv-eN0fD8H3GUs7bVTwkFufr7LdNMETUcSGP--GO_mJguzcv0iwLye4wSQh_lM5NmmlfBgoMkkdTfscycV04LTm6ifSrFRQIWuyeYG4mr3RfoYfWMXwnYJUzM1F-hqOQC6rsrtfn-i5xbZyONw_CbdwiGFqlzKeK1CxlqKrlqth0j_qkgW91KtYhIbINJ-mY_4xlOOw2QfSdjBBoVIB1j7dNUvVX-tiVyPv6SovmlUXqcRpbTAimv1gxoWMhquuPkjyuI00l8gKXciKvnhLZ97G-gDDI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20330" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو :
طبق اسنادی که به دست آورده‌ایم ایران بار دیگر می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند و ما قبلا هشدار داده بودیم که اگر ایران برنامه هسته‌ای یا موشکی خود را دوباره شروع کند ما به آن حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20328" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20327" target="_blank">📅 22:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حمله ایران به یک کشتی بحرینی در خلیح فارس</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20326" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20325" target="_blank">📅 22:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سناتور تد کروز:
چیزی که من خواستار آن هستم این است که رئیس جمهور ترامپ و دولت او معترضان را مسلح کنند تا مردم ایران بتوانند این کار را انجام دهند، کردها را مسلح کنند و به معترضان اجازه دهند این حکومت را از قدرت سرنگون کنند، نه با نیروهای آمریکایی در میدان، بلکه با مردم ایران.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20324" target="_blank">📅 21:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل طرحی را برای سرنگونی نظام ایران تدارک دیده است. در راستای این آمادگی‌ها، هزاران نیروی کرد به اسرائیل منتقل شده و سناریوهای عملیاتی مختلف را تمرین کرده‌اند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20323" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
