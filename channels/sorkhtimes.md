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
<img src="https://cdn4.telesco.pe/file/Znc5Ez7D2EcnZAIT-wOU_XmllE09aud7leeRyX1G2ADfrJ74XK5LmAK5uDiFFcyjFKsKFl6P7fKfdi9-2nm6D7zQ6qr9BwnL-GuForAMJnacC_Wz9HkS9iYfUD7rWJVlZI1lcyYEyy42HCtIf3nsPkzsDuHe68pMmhHRyGbleruSzFl7IeHz64fJcwUtq4pVTtrBet8wiOSiUoD77YGZ00w3IaeaD2wzBp1qc2MZxSxAo0FgZpQFONwoH30IPmmI-SW0OWGkBXa4waZ6Tv6G32deIMN8V4950g9pPF6cxT3QGZbg6xNTSnyhnSEQgfGchih1NVfBZEqxMfxjBcuD8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-135892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 635 · <a href="https://t.me/SorkhTimes/135892" target="_blank">📅 23:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/SorkhTimes/135891" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHRHSRZvWAacxVORmfSfwUK1Qz60kHoTdp8r5IlTdIhzfvYOOJYtSGSH1F9_ogc1zdg3GVcX-FWT82OPKaTKFkTI2MesgeK0-OS4a1EBParY43E5C6VF21MAl7y0OCkFZ_cvU7jwF-Cb_1NXYn4FlgsTrCNlhxulBrxbOO3nXaswIxcGbrnoKXEF6weqOj4bW4-wX2LmaJY6MzYjKyAZzcPrJlM0zuuE_0bDW0qtPgi4gFvjKUjxJgpgw73dKkpxsFRiSB_Q9msqxjTpyEFTChpCSLUgwFPZ1QYDtr75JmafjhCphrQUyQeT7HJgEum821CMK7R3VhoVTjT2NBXYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/135890" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
🔹
آغاز بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/135889" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=GRWuuac5gOJcCDBdAF_nYmKpUJsyiTcKiw7c3_N86atur11GaVKU8E5e7_K8ABtZCTjbLgBGkjDEdRWmcWG9gSt4JhmgJ4IXG0qsF6efbyxIG0F0g4lcIPrBK4X0HGxMImAevZFiKiHtt0M64afd7nwaclrZCvUEzhV0_7we33Q1ltrCvOo1GsB25sSa9cKVNYL5ME6AnYXITlbyqfk_1SRga2qBcrsi3sE_K0D4EwhuQDd8ZKqVl9y4bV7RP9ZuI9Q6QyLSq4oF7Zj-scZ4D7Em7NiS2ipPBaoxgqz_EvAMZ3S5nkQhd5H7LMeh2201_7vKp1ixKpQcVrBTRv5Ycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=GRWuuac5gOJcCDBdAF_nYmKpUJsyiTcKiw7c3_N86atur11GaVKU8E5e7_K8ABtZCTjbLgBGkjDEdRWmcWG9gSt4JhmgJ4IXG0qsF6efbyxIG0F0g4lcIPrBK4X0HGxMImAevZFiKiHtt0M64afd7nwaclrZCvUEzhV0_7we33Q1ltrCvOo1GsB25sSa9cKVNYL5ME6AnYXITlbyqfk_1SRga2qBcrsi3sE_K0D4EwhuQDd8ZKqVl9y4bV7RP9ZuI9Q6QyLSq4oF7Zj-scZ4D7Em7NiS2ipPBaoxgqz_EvAMZ3S5nkQhd5H7LMeh2201_7vKp1ixKpQcVrBTRv5Ycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریم باقری: اگه جام جهانی رو 64 تیم میکنن ماهم به عنوان تیم پیشکسوتان تیم بدیم بریم
😂
😂
😂
🔴
+ خنده های علی دایی رو
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/135888" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
یاسین سلمانی ماندنی شد
🔴
با نظر مهدی تارتار، هافبک جوان پرسپولیس در جمع سرخ‌ها باقی خواهد ماند و فرصت دارد خودش را در فصل جدید ثابت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/135887" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/135886" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/135883" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135882">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/135882" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
🚨
خبرگزاری فارس: پرسپولیس علاقه ای به جذب آسانی نداره
🫤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/135881" target="_blank">📅 22:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
مسئول باشگاه مذاکره‌ی پرسپولیس با یاسر آسانی رو تکذیب کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/135880" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P43hg5eATSPJl_axdBdKI7KMtWjuEe_wQKvHlMzVd1_ZZD9E_-eGvyOhJaqiYTZqEcmFUTVaDkjezudV4dPvhPlYpc1c6KgRYKaoO_xcJxXC4OydbdqlSryfHYaQIhupkPcSH_hA7DRCNFbLeWg2QuE8x6sPw-uaEJmEdyGul9QqDbQmzDFTMBZBH_BDVVNheOMlvFf-4TNEc8yByPcKJBx54f_t5eo2Nq-ZcXnOFln3l7YZ_X4tgwpUGnMpt9SLWJxCerGOh_qKkBEZ2Tk96dCugoOKzVIAT4obAUUEpxxpB106Fqu8DXFkDNUYwrQ7yuELj_gcMh-7MRW5c9sbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/135879" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
🔹
تارتار هنوز درباره‌ی جهانبخش و قدوس نظری نداده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/135878" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/135877" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/135876" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
#فوری | ترامپ:
🔴
🔴
ایران مدتی پیش با ما تماس گرفت؛ آن‌ها می‌خواهند یک توافق انجام دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/135875" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135874" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135873" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135872">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
فووووووووووووری
‼️
مدیر طویله استقلال: ما برای جذب دانیال ایری با باشگاه نساجی تماس گرفتیم انها به ما کسری طاهری را پیشنهاد دادند و به ما ثابت کردند که قراردادش را با این تیم امضا کرده است! ما هم در نظر داریم هر دو این بازیکنان را در صورت باز شدن پنجره نقل و انتقالاتی خریداری کنیم در غیر این صورت آنها نیم فصل به جمع اصافه شوند!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/135872" target="_blank">📅 21:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135871">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135871" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/135870" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=EtNn8ix2Ku3GQcl50exYI_6BEHAlO3CqoU3DzhAG9Zd3JvyOAlLj0nqLTW039K7V3-X3NTJyeLXuzO5g3E0zaZa2dSzfpDD9BtbXwNOG7hHp6Fp1nW6nUl-9IOVT9427R-ueHfeRV7Y5z9VqHc_hZBX8_s-p8K-s_CbG6IjEpZ5_uYq_2F_XNdkqzXGZdIwNbHAOt5x0nHB_CuUstG5Jw8i1HbGp0Oelt3PLW4yAinOs6XgwEnsNF028vjMbRw-aILWgsQAYDMbfYsOaEUbyxNvLx6JIeHSTLfpBj-6Lv_f_T1x9bqj2doCY333EloUgTJWa8VVMTYFm8tvoL7TWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=EtNn8ix2Ku3GQcl50exYI_6BEHAlO3CqoU3DzhAG9Zd3JvyOAlLj0nqLTW039K7V3-X3NTJyeLXuzO5g3E0zaZa2dSzfpDD9BtbXwNOG7hHp6Fp1nW6nUl-9IOVT9427R-ueHfeRV7Y5z9VqHc_hZBX8_s-p8K-s_CbG6IjEpZ5_uYq_2F_XNdkqzXGZdIwNbHAOt5x0nHB_CuUstG5Jw8i1HbGp0Oelt3PLW4yAinOs6XgwEnsNF028vjMbRw-aILWgsQAYDMbfYsOaEUbyxNvLx6JIeHSTLfpBj-6Lv_f_T1x9bqj2doCY333EloUgTJWa8VVMTYFm8tvoL7TWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/135869" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/135868" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHvP4pFRP_uhBY324L-coDU2L_b_D-IgGPv6CDpQmpgT1bqNUKU49yBGseHqlVEnlX9hS3lLD3mmvZBxXdO045JkX8qZA4P_ylsC9kfbJAjnemT64aNh5844nPm-e0pT7y4aWSFpG5mQU5n5IZBgb8GMN-jN6eABmbdZRHqXxMd0M8VfgxjHweRrY5SUkyI8QpotljSPULqhexgqL0XXaM2kCpoX4dGlSUUfYD572NL2JLecONe1JKlDQnTRPzcQXEQPrBFbpZTXjpXMAqf1LgR4zK3sXsjyOWFe_OV_G3vVfwGyea1c7WyxcosaQ2Rwj4MDxS2Cm-4zZCfBRHB_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/135867" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
🔴
ایجنت محمد مهدی زارع دقایقی پیش از باشگاه پرسپولیس خارج شد و گفت به زودی همه چیز مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/135866" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
❗️
با رضایت مهدی تارتار از عملکرد مارکو باکیچ، این هافبک در جمع سرخ‌پوشان ماندگار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135865" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
امیرحسین محمودی ستاره جوان پرسپولیس امروز ۲۰ ساله شد
❤️
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135864" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135863">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📌
مارکو باکیچ امشب پرواز داره و به تهران میاد و از فردا در تمرینات حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135863" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135862">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🟨
🟨
دوکو بخاطر زایمان همسرش اردو بلژیک رو ترک کرده و احتمالا بازی فردا شب مقابل تیم قلعه‌نویی رو از دست میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135862" target="_blank">📅 19:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135861">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/135861" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135860">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135860" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135859">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKrxXOPvlnnppd_X9PITTDwx1maVq4fUox1oAwyqbkr5gbzcedcLwafulRLxrC5d4liV73PdJcLlTtYBTdj2lOUtcxXO1szGXCuaqipphaCrOjkT_RYD_gClPVPFTKxjMFVpXLRh6bSgDZTsTUiFrxLEn6kLbM2z1xaf59KXr3UW-ykHgtuNYtnnJ-MJrTeX_PX5cfviDqgHdMeKnT-DmvmNtEDn5nVT-9RaT_XPmPiejK9pAJHOoZxrwTi7hKgggb4DcO5eaBeSHSqLxLLta5oMS59oqmC7JpQlOwSSQ7o29Oa8PMgsqNuMXyiX6OFfCChviXe5tfcSo7g5GrIe6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قرارداد پورعلی‌گنجی با پرسپولیس همچنان معتبر است و هنوز فسخی میان طرفین انجام نشده است. از همین رو، اگر باشگاه در جذب مدافعان مدنظر تارتار ناکام بماند، احتمال دارد از پورعلی‌گنجی برای بازگشت به تمرینات دعوت شود. ضمن اینکه خود این بازیکن نیز علاقه دارد به حضورش در پرسپولیس ادامه دهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135859" target="_blank">📅 18:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135858">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">😀
😀
😀
😀
فووووووری؛ زهره فلاح زاده خبرنگار معتبر حوزه استقلال:
🚨
🚨
🚨
مذاکرات پرسپولیس و یاسر آسانی از شب گذشته آغاز شده است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/135858" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/135857" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
#فوری | ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/135856" target="_blank">📅 18:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
علی دایی و کریم باقری امشب مهمان برنامه عادل فردوسی‌پور برای بازی آرژانتین و انگلیس هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135855" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
طاهری رویای بازی تو پرسپولیس رو داشته و توسط شهاب زندی مدیرعامل نساجی گول خورده و حالا هرطور شده میخواد فسخ کنه.///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135854" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
🗞
کسرا طاهری بدنبال فسخ قرارداد با نساجی تا ۴۸ ساعت آینده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135853" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135852">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135852" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMYtd4vayrN2nCQodd5xNSe5KFqZMtIaRE8-7sD-2qp1GYXyGRK2EUo5hDzJfxeNmBl9W2gM_CDV0CV3MOLQSRbWE-y4eVqbZR1xgpsgPFGdisIzTZIhCcrSU_ZSOMZ0Fw2dF--Hu0IC0wqcSEPn6jLLyZ6eIQsl73DijCIW1SI1vKmCM7JWO_VaQ344dNUreFRyRtERllwgfl7wZzbTmwNxRNvjYcbG4dlyswJUZyLB0-RZSdpTnBRt6qVfs36MODGQd-tF8n71syBc0c1b1exs0pec4lv6TWwUBDB4ljbqggvJvLUapoFHGTjelEL3ruxUiINFsRljJ28xRufUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
😀
😀
😀
فووووووری؛ زهره فلاح زاده خبرنگار معتبر حوزه استقلال:
🚨
🚨
🚨
مذاکرات پرسپولیس و یاسر آسانی از شب گذشته آغاز شده است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135851" target="_blank">📅 16:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135850">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135850" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135849">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z29o6YODsI8L8xmO_UxeD_hqt6CB9qx7wtQmVxOPb6GlT5kW0ndXvkuBFX9BFhbQpWpnL4IAcodu3Iw_XQ0b-tlWkj_MaUe1IBZUBIolWHRWDzOif70Zh2nPmIa3SKSZteQRRuLrZt_dqihrNYsm986uHCCLRTIubIyOgc2_yi9TnLZdsGMDfF8Co2dK60SC5eTIi1N1RpY3qZjMCX31KasUk_lLtNBoLERir0bHIgRQiWtXxJAIuNhIncwJ5QdZjsgQHeUmmsXUUXbpvaGRNb10qXGa89HgSD1BfEYMGaia-UhC0nZEPbSoEyWHiQ2_YDeu69ltUoQRiFmM70LF_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135849" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135848">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135848" target="_blank">📅 16:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135847">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
#فوری
🔴
یاسر آسانی ستاره آلبانیایی فصل قبل استقلال در آستانه پیوستن به تراکتور قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135847" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135846">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
پنج کاپیتان پرسپولیس در فصل پیش رو مشخص شدند
⏺
1_علی علیپور
⏺
2 _حسین کنعانی زادگان
⏺
3_محمد عمری
⏺
4– محمد خدابنده لو
⏺
5_اوستن اورنوف
🔴
پ.ن: در صورتی که وحید امیری به پرسپولیس اضافه شه، احتمالا کاپیتان اول تیم میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135846" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135845">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135845" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135844">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135844" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135843">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135843" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135843" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135842">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMOvsN5W-vMlOvOqbi9NRdVQndFZMv1ogg-lHT-aIDKXk3Qb9Q59BgUuWhLktxtRXnppw1ltbUV-OCxRkX9vdXy3lobrLUugrxZtw5pBkjn9PmerZs52WgeJOdZTITybMjlt1lFPKDCyS7ouu5g8QpGSGju_hlcamaiddNEheYyIlnb7SRj91G8YhmvpcAHwrLez_-fhtBM2K6bM0TM2lzvVe5U8HsOqAmU-yHf3byWzlcQy8xqfA_I73ueug2X0PYNQ783xl_ZTHskM4Zg7opQutUlBREM-gcOArxyvCNfSDoPLBUjtJCLX5blJ3UoYXWKxSuPDr7DDM2jwEKHxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
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
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135842" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135841">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
#فوری
| ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات به اهداف استراتژیک در ایران، متمرکز بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135841" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135840">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
با اعلام فدراسیون فوتبال، کمیته استیناف درخواست تجدیدنظر باشگاه پرسپولیس در پرونده علیرضا بیرانوند را رد کرد.
🔴
باشگاه پرسپولیس نسبت به رای کمیته وضعیت بازیکنان فدراسیون فوتبال که به موجب آن حکم به محکومیت به پرداخت مبلغ یک میلیارد و ۲۰۰ میلیون تومان داده شد، اعتراض کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135840" target="_blank">📅 14:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135839">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135839" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135838">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
شنیده ها: یاسین جرجانی، مهدی زارع و مسعود محبی سه گزینه جدید خط دفاعی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135838" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135837">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiARCvCwAKis3ScAfWLwJve3cw0UnlvCeKrjH67ry5Xh53jGwVPzbwVCIyS0_wOQvPYxcTR2vugHWoYo7hRlxnblQesNY3q4L_X0nhQSxhot3MGL2TKm31RaVLI78nXaryhg6gOgFZoNLvY1lxe6qcyB6zvELpYyvmC0lSwZs4yN2aib8oTGciuj-ql-54dw_5iaJ8_5h7FW8zpqB2eHbP_YmcMVep3v2BzscC3-RhkKVKO7Ej4f1bFUSdH01gFUrenxHKWmp8eIhbI949ECMZ1VgUfgGlwS9v3Ey9Duwy35GdGGuIWFNAm4En_8IjSKZ6gitoqJpbBojaHKCljkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: یاسین جرجانی، مهدی زارع و مسعود محبی سه گزینه جدید خط دفاعی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135837" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
نظر و حرف دلتون و بگید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135836" target="_blank">📅 12:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_zEi2Iw7sH5I9AaoLqa9JAes6MB9HhPniJYO2MC90uzY6SRUc0n7roSgBX7jmttbAMAKspFd2kqp0_G6wVHgF7T-w0vpfp6DX5Yn0lkO55kNgAVBeHOHo6aRNslM__QTxffdB34GXDUap7qbSMLaMUptuUnQaWjIqN93PU32slmDeEFSw7AndaGjYXVOC5-x_nzckNPZKYNv96QEn90OYuMMEqg51vjX9BKZGh3Vs91cUsE9oQa0jVRYbWyPAp34KTQL5vVd8EG_nDAIZkSm82eIbH1VcgCCZ_cs1DWgUVD1jxBWs5w8FI58kC8qQuswUE4ND9soSHhBN0ePy4VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
؛
بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135834" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135833" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135832" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKbW57egbHGy-dqHbnkTW9ZzwvLS0xcZfYn2cV0zbm30Ex0io-VC0petcSZztV_yjo4kVqKELwI8_hALyWQqKQxBFbt27FMGZQbcx4mDJmFLFaaoKGeP6-4xd8pWipoT2RPxdcupRyCBJrm14qzK1XfHma-6A3BKByP3acqkUlfSasqs5cIYe3aJpAJEHaO7R59M_iULykCzEEka3zShGL8CbkGinsHJXtWIinSSbcP6uMoC92cJNu-rAYCLfSlbq39dY4TuymdrlElywN9EzseCKHb29BQXOiwpkbR36GAq3PpXkQLhxtSp0EcFxr_D7j5vrixUw_JWA6gL80ijCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135831" target="_blank">📅 12:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135830" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135829" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135828" target="_blank">📅 10:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روز گذشته جلسه ای برای چذب پوریا لطیفی فر با مدیران گل گهر سیرجان برگزار کردند و با این باشگاه به توافق رسیدند / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135827" target="_blank">📅 10:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5ia7UbLkQRUk9GM5VIVc1UQWhbB6Qw26LCvnOq6HdE9A4k6jGph7y_KA1N7BGOBm_xsGRVb3Auq3NSxzbmBInz4tYHHORh8-JSKNXW8EQizkB8DpCFVsFeCvbE9ezzrer0_bVpht6qbRPJGFy0kfBsGaeM2QqIiJKE2dI7tsAna0UVJdgSqWVNNq5bEfvqvyWi3nu5JEUkgKiOUHQvbQYrCEwcwO35wbKj6cT1A6cq_410ptujP_-rzbmY7VQYNKGCqO_GjfepMzIVXd9Z1poA6_SeRkvb-4iJx2SZj_1O2_83gfoDLXJVBtpJv0W3WypDNIlSzkNyJRSbBT3hNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135826" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
🏟️
ورزشگاه آزادی تا دی ماه در دسترس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135825" target="_blank">📅 10:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135824" target="_blank">📅 10:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
پایان بازی، برتری در دیدار دوستانه
🔴
پرسپولیس 3 _ 0 شهدای رزکان البرز
✅
عمری، تیکدری، میرشفیعیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135823" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
❗️
فرهیختگان: مهدی تارتار با جدایی محمد عمری مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135822" target="_blank">📅 09:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135821" target="_blank">📅 09:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLRfmWAlfMToyI75C_6VBFuBXMIItbyyDck0ng4t9ME1HDrQdFlQqxA62w560yhPBCREubUlBX4xXOOisDa2MUrvRvMa_qPDdK5XNt9B0o9ncRt4xuVb6yGjY3Q_47oCJzWRz5Us3AzDIMAsQGJcNaA8a8kbLTVpVawyGnMHY4kYvzSAFa9UgkuuNkrzTI6Yqh2ANKWDQIdyDqs3T8Q4kfOlCFpE5lC8gX3td_imrqX8lSxp-aJDaZR2tR3fY45jyQkxqRx18hlbT-TtURvg2EItrRiZ2z0TqD4c13lsZjuP5ATEqQY3vBxyZEdYOrRH216PUopPBquVri3rUrqmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135820" target="_blank">📅 09:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان وظیفه جونشونو از دست دادن و امار مجروحین هم بالاست
🔴
🔴
همچنین درخواست فوری از مرکز انتقال خون ایرانشهر برای اهدای خون در شهر بمپور برای مجروحین ثبت شده
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135819" target="_blank">📅 09:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
ترامپ : امشب و فردا، ایران را با قدرت مورد حمله قرار خواهیم داد، توافق‌نامه همکاری با ایران یک آزمون بود، و ایران در انجام تعهدات خود در این توافق‌نامه شکست خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135818" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKC0qayJ1uhziRIhXejj8AiekJ6TnGhGmRDKDd6H4VAeyQ43JvUkQoJt5KOVK7CearOdCufmVpGLW8d_JHcM6-SFCKWOmW0XNkNFoUggGRXv0snUXNYrEWTp0GnQgBNq5ISULeVUBD8OWj4OV2kXeJl5GE9fqzh2HZWskO6dUE1I-A9V-pVfWsZrtRTd2_ac6_RjUdgGkwvv8SjwOFw_LOETwT-cA2U7jYpJbKLn-xH9W8MfikpzG2KDS7uiSfPC-pdYQvbi9B5VFsMzpkw6PvVm8UuHYRvUiKwDppgV2CPoJZeuRhNq2F65_sA3e2mrTxs8Uoa2gvBuq1P8ux_KuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135817" target="_blank">📅 09:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135816" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135816" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw-KXpdUiRRgR9Lp4-GHp5Bp3_-TLq8Bqfb8lOwawKscOKipSjYC5nHZT5Ttc5HPGZ46ItWEHhYKW5TCsDnbEqC0gVbldBteMz5UbgSEQqXvUJX60nU5z13Y1QcWp35qLFcHFZUPKbpelQ3K90Q5H6YxY_S9Uc3sQ9G9psDg0mpEIcVO6erNAs4ywNoewtNUZ0QOS10US_FJJi_N8fHP7W6ez_S2zadynrFj8HwOMdNuxdIhwVoGfc1Had6-f16PcwP91xgX0Jet7MhYdu1M_wm8tpey4e5eEgCoao_6KDV0EPmOBrHTq1QxWwmEa4wGeHmJ8WTwk6CY_ozeXX7iVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135815" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
فرانسوی ها ساکت هستند و حرفی برای گفتن ندارن تو گروه  پ.ن رفتن اسپانیا به فینال فقط با یک گل خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135814" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
خداحافظی فرانسه با قهرمانی و رفتن به بازی رده بندی ...خداحافظ آقای امباپه ..سلام اسپانیا به فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135813" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135812" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkaJ2x9-Bg7Du9Wc4bCc61lPzl4kCaUTMwpjafuY6_UIXcoJwpTz_mZ-TM4sJLVCBCqI03KfrqIKd0vAxFmCmCnpzNLqXunrJdNOJb3xsrqknR02X4ULAxC-e49X5hOYRnHuTIJXJcswIzg_P-nrLFQ4FvtZ5CICxH4LlYXwxVFPsCH3JB2xPVmErxFyGR_lctdz0V8N2GVHnG0LiMg2x3wBdwGgIQSfZcdYVLsUCsNd4WTsZnCCtyEvpHe1j__Xp5Km2D4bBby5wYwPZhzfShIDbrgXc5x3zr-hps0dtpSRx402tmWWHlqFMgOIXaXpQhXNFSWuoy-XWwk84DBiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135811" target="_blank">📅 00:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135810" target="_blank">📅 00:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135809" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135808" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
❗️
#فوری | محاصره دریایی آمریکا علیه ایران از دقایقی قبل مجددا آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135807" target="_blank">📅 00:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
گل‌های پرسپولیس در دیدار تدارکاتی مقابل شهدای رزکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135806" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135805" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
گل اول اسپانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135804" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
❗️
مرکز مشترک اطلاعات دریایی به رهبری نیروی دریایی آمریکا :  محاصره آمریکا شامل همه کشتی‌ها، بدون توجه به پرچم اون‌ها می‌شه
🔴
🔴
محاصره، کل سواحل ایران رو شامل می‌شه، از جمله بنادر و پایانه‌های نفتی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135803" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135801" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135800" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135799" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135798" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135797" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=XKIKaXbi3UCYowIa5u85IJC7TyxFTydz4vn80EH27N0w1XL-uFkJpDLREpDXwxR2JABKu2T7AO3dnW-e4XQ15L7QRqRKkZHWQ5ej7PXh6QDeMpkUeEDGnWA5yeL2zFW79SccSGR9NC2tMArdvCtUPAXsBA3g5C40Jp4oMAaWojSc_usxKYn8rPKjun6yPTRUoy-pDT6fzlPzLQw-qHTeX9leoNA4dWONFnmfCTu4noyKbX-jTZYXqVj7cMvoDAOgDR_8blzmCPCyB-W8Y9CCJJ2U5XjklAflgZdU6TXWqDihnXtRE7go8cCQDpgh4mxCAzoAJ5iMRQZk-raczgeV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=XKIKaXbi3UCYowIa5u85IJC7TyxFTydz4vn80EH27N0w1XL-uFkJpDLREpDXwxR2JABKu2T7AO3dnW-e4XQ15L7QRqRKkZHWQ5ej7PXh6QDeMpkUeEDGnWA5yeL2zFW79SccSGR9NC2tMArdvCtUPAXsBA3g5C40Jp4oMAaWojSc_usxKYn8rPKjun6yPTRUoy-pDT6fzlPzLQw-qHTeX9leoNA4dWONFnmfCTu4noyKbX-jTZYXqVj7cMvoDAOgDR_8blzmCPCyB-W8Y9CCJJ2U5XjklAflgZdU6TXWqDihnXtRE7go8cCQDpgh4mxCAzoAJ5iMRQZk-raczgeV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است و او زودتر از ما سر تمرینات می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135796" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
جااااااااااان کیسه سوزی باشه؟
😂
✅
جلالی : دربی حذفی خیلی اذیت شدیم و گل عالیشاه خیلی قشنگ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/135795" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135794" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
خلیلی :
🔴
دیگر مهاجم جذب نمی‌کنیم و با سرگیف، شهرآبادی و علیپور ادامه خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135793" target="_blank">📅 21:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135792" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=k3X3vBPZaE8B2JXT-zYBljgMayka8QP67uMuXSThNW8IjfCK0fez3505JyJWLassu2_g9xOtIcsNwNn0r1GsjCxFC0JIiEeNYyO3hL2DnX7GbbiKjF8TGics5yLSCUtlSRZGjSdw-eU43HOjoPYnBufivpPEr2yTvDtIeL3OqP-a3JaQutEdC9jy854kXY4TjUhMTMU-PGMmbdqrGsmEvIxz53TNwFO6pC-YVcxib5mE34D2r6fAEeiSj4_vdyXjjVDHsfzlxyD8zcTFfO7-wGNmPY7C97_LIU4g_MqEWiomfi0r4sVTPR4cwHDuTAn57sgXWhih6PJSAakWHF06VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=k3X3vBPZaE8B2JXT-zYBljgMayka8QP67uMuXSThNW8IjfCK0fez3505JyJWLassu2_g9xOtIcsNwNn0r1GsjCxFC0JIiEeNYyO3hL2DnX7GbbiKjF8TGics5yLSCUtlSRZGjSdw-eU43HOjoPYnBufivpPEr2yTvDtIeL3OqP-a3JaQutEdC9jy854kXY4TjUhMTMU-PGMmbdqrGsmEvIxz53TNwFO6pC-YVcxib5mE34D2r6fAEeiSj4_vdyXjjVDHsfzlxyD8zcTFfO7-wGNmPY7C97_LIU4g_MqEWiomfi0r4sVTPR4cwHDuTAn57sgXWhih6PJSAakWHF06VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135791" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=bvAdC9DAyKe3mXAOnrp-PHRgw4yNQWWDlelXSOmWbB3yGHS3aRC-1e_eKVuqNWiqPaTM1vFpCb3jBih2KvyuzvGqVdYG1j9E5RJoHi_IVPh1GHDlYX75k1VQjotS3TALwblfbyn7ZP2U9OY4I9L_HP700XO_-fHCTeLjMpblHk_58NuWbHj4--1eGzTRCeERFOhZT6V5i6RlnsoqdvwU7dpHMPYrFm0caGLeNssNZ1DwQ7YfO3GEcgDJZFsy85_OFPa7uQm04GMPfHcqCJMlQZ3g4Bol1sRJMhuVWOfe6QMc8ajoFyrSe7oOB81pDwnGgtq-HsG34vLKRYCIFr5Idg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=bvAdC9DAyKe3mXAOnrp-PHRgw4yNQWWDlelXSOmWbB3yGHS3aRC-1e_eKVuqNWiqPaTM1vFpCb3jBih2KvyuzvGqVdYG1j9E5RJoHi_IVPh1GHDlYX75k1VQjotS3TALwblfbyn7ZP2U9OY4I9L_HP700XO_-fHCTeLjMpblHk_58NuWbHj4--1eGzTRCeERFOhZT6V5i6RlnsoqdvwU7dpHMPYrFm0caGLeNssNZ1DwQ7YfO3GEcgDJZFsy85_OFPa7uQm04GMPfHcqCJMlQZ3g4Bol1sRJMhuVWOfe6QMc8ajoFyrSe7oOB81pDwnGgtq-HsG34vLKRYCIFr5Idg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: امیدوارم امسال بتوانم دل هواداران پرسپولیس را شاد کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135790" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267f8866.mp4?token=t59As5AAgQg2ZIMFGoPkBrc1DHCtPAgXwETDu_yQB9Gtaom7yDKirKKtBe7WjGhDeIkBTmi-ZCImcw2tDBrW25IQWEXZ0pop3RNktte87GZY-zwt6-IPCqtSE3bsk2aYop5ticOdxEeI8SqfTs0eilIs3N0Ff37u8VnPEPWMuxcV1A93tE951wHqwSdMQG5IqBTY5Fc1dFQ8ScpJLOwmHnf32uzs7tm4neL3-gabPuBumKx28NtwXw3L-Y3xosmtAqjK8pSSt-DkUKZyEDfrQedQcE2Mg9moiHqx997nXX_JTI38pdr9w2dDYX1zjNmwK-NsFM6RA6r50bJtrnfJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267f8866.mp4?token=t59As5AAgQg2ZIMFGoPkBrc1DHCtPAgXwETDu_yQB9Gtaom7yDKirKKtBe7WjGhDeIkBTmi-ZCImcw2tDBrW25IQWEXZ0pop3RNktte87GZY-zwt6-IPCqtSE3bsk2aYop5ticOdxEeI8SqfTs0eilIs3N0Ff37u8VnPEPWMuxcV1A93tE951wHqwSdMQG5IqBTY5Fc1dFQ8ScpJLOwmHnf32uzs7tm4neL3-gabPuBumKx28NtwXw3L-Y3xosmtAqjK8pSSt-DkUKZyEDfrQedQcE2Mg9moiHqx997nXX_JTI38pdr9w2dDYX1zjNmwK-NsFM6RA6r50bJtrnfJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135789" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
