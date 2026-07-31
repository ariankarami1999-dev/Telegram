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
<img src="https://cdn4.telesco.pe/file/j6PzST_iXo0RLwSp6uOcTIH6kHpNRA1-buwUXEUmAwo4mIBlPO1MPk4s67Z2IMKhw1NI7xJYoU9wCS1AeGblvPJDtfswE3bQLOOMSICfQ2IncnsKpVo5tOOIhx0v75IiOQB5qvWOL6KCuwCVOz-1aywQMB3ay2UWevX879SIvkYhrZTwWJBzR1BLabAk1QKy_NVOJ1J_Uk3t7vSJGwN4pvnAiCR0OdnioyFjLhIRNZSFvZ0aP7QCCn2rd90baKrB4inLI8ARr1p_6Ib3OAXAmhNJQsaDeHATClAoyWcWTagtGhKGmaLHajj1Lg1h_S2eouwI8TjJWPtlVrKo2M2F-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bckTSMBeY8MLsCjfoY2QnVprQ_FHIMdZOWASkjaI3WmLgOtF2o198SKi8EsfcmSW3-KEmqKgxYyvd7j9ueWUQso-Je8nQ2yu1KX9ElwSPoaUD_VaRrgWwa1j4MR3ofjH-90gGoAY0EBHtPnxNLhU1qX0OnpzbM7AQzd8YhExjaF_-lvF16AY6BwWcv2rdjWvZkHizGHCvymzmojEgFd2Rinmf2K9HU68-t9TNtQDypubabfx-tolxSQIfuIzJv5hnPQGAK9aIF2uLrHhI4llj19veWhCQ2BIvhrq0dRJX6S2VZHQHlDqYGo9blUaRwW2KeYq4BIpv_oGcfDfuq2Iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 153 · <a href="https://t.me/SBoxxx/19511" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خب سیگنال پایان موج 2 از 5 دارد صادر می شود:
استاد خوش چشم: فک نکنم‌ دیگر جنگ بشود</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/SBoxxx/19510" target="_blank">📅 12:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پلیس:  زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/19509" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پلیس:
زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/19508" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/19507" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19506">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmhJ70I6ORZBeBFrZIWlbuvj-9S1gd_20kzmhwYzQpkzSVc_dIWAY9QkOE3h7LaQ9EHETRtYB8mvfe9tISfECd6fzZESo1NHH-DL14Q3w-oOiGJyHgMZYRVcpkkByOzV6YA4SpNCykeAP3bwP5lYwrMDtNjlsbrz71xpfMrL91oQImntc0LecqciKJMDYsW3UAcBj2wfx10IPfoodUEvBCxKGk-3EQnY9cd-HpelFHo6sNWWol9zoytPBh03VPiTkdENT-jj_zlAXsJ1Uf9FXO3ro9F6xakEK_S42smDyvTCRllc4xGWjE0DPL13aRhkTfWxvP9to7kF93NnnTuopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/19506" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afWQRPlAAHjYlHyY0y7lbLY2amo_Beu7Jx1db-aIXtF-dp-yKGU0nkep7xNArOJNshNRwIw7jDhERT4W9tgnz2z_H_KpiEQ0-iVneMjxknWJgtSIshomKVKn7LFMXX5-VAMXkLoZwk4WvhkAWOyUlVKGeBpRaG8WUyi1i3y2sbLOkEaE35-PcPfV0QaTOMpamao9HUOfx1gUYyTa2kOfaJiM4ucft3zLIaPe7_xo26HqSEOITZLM1NnMD7-GY_UT3I3QUpSDypYY9HObcDCS6_vVWjOy_a439BGJTKECsDIZwQomqO0rkbB6C4xMT10hH46GRMwXbflbpusd3YmNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/19505" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شلیک موشک از ایران</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/19504" target="_blank">📅 10:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجری
: آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی
: مجموع تلفات روسیه ۱,۶۰۰,۰۰۰ نفر است و حدود ۷۰۰,۰۰۰ نفر کشته شده‌اند. تقریباً.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/19503" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قالیباف:
ایالات متحده هر روز دست‌های خود را با جنایت جدیدی آلوده می‌کند؛ حمله تروریستی به خانه‌های مسکونی غیرنظامیان در جزیره قشم ادامه‌ای بر فجایع میناب و لامرد است.
آمریکایی‌ها عادت کرده‌اند که با ریختن خون بی‌گناهان، برای ضرباتی که در میدان نبرد دریافت می‌کنند جبران کنند.
آن‌ها بهای آن را خواهند پرداخت.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/19502" target="_blank">📅 10:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ اعلام کرد که حماس به طور کامل سلاح‌های خود را تحویل داده و غزه «در دستان یک دولت فلسطینی جدید که در خدمت مردم خود است» قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19501" target="_blank">📅 02:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مجری فاکس نیوز:
آیا کشورهای دیگر در منطقه که توسط ایران مورد حمله قرار گرفته‌اند، در حال تماس و تمایل به شراکت با اسرائیل هستند؟
نتانیاهو:
بیشتر از آنچه فکر می‌کنید. بیشتر از آنچه می‌توانم بگویم.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19500" target="_blank">📅 01:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نصب سیم خاردار روی پنجره ها از سوی مردم اسپانیا برای مقابله با موج سرقت و جنایت مهاجرین آفریقایی</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19499" target="_blank">📅 01:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsDKJGeC99y1ybF-sodWchtKpwbbP8hYslPFH7x_hqr-nlCG86nJ97BndTgNhn03C6PY3YqGVzp54fVvZIG1LZ9ZU1ZUFi5qz-3JJ9LUwCHXQuxkpE36Xt9eK27MYq8LBiXkQeBU0pSgUNrvpDwlIUcTSUtU1ks39mvH22pgojACBzsDMzE9nGQxi2L4m1i1GKYoFiUw1qG1TYxSpoN2N3Z6yN8vphKRj-lWuieGm1qJxahrJwFmzwAX74ui_fiE5_yzJoSzhWyGVfp4owepNKTpIH1g0hHMsAMxvTjJiRU0txbYYRI4KWlH1j3sWHriVixdvWqeJ7_pbIV7Ewn-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19498" target="_blank">📅 01:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.  @PressTV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/19497" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=KCzXQR9l-Re03DAhiuj6gRd1-070uhTZGlqUyobck_6_fLt5YhmTgmI9p8rekAJMdPurzYL6GG0JPDeh7S7XDbXqSzz-NYQV0mP64TNEJzD1UYtoQJIjp2kYBc7aAtHxbxoZMMiGoiWqPhg2boZtbsVWYX6LmesSEakPVPBqAdvn5KUuCjG4hV7bLgG8Q2TLblsmpIsohsP3dVABjtD0xHgSw1r_TuObEwTXv21jrehDP1Bks2DCKYR-xighIxfOafFt_gyCvoRx_RHErzzDN0aknUrxL8OrPWSmVKlLJk5x6NZ4cLKIwaSHdku93o8Vk0y2BDZDsoKCHbXKX0IGpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=KCzXQR9l-Re03DAhiuj6gRd1-070uhTZGlqUyobck_6_fLt5YhmTgmI9p8rekAJMdPurzYL6GG0JPDeh7S7XDbXqSzz-NYQV0mP64TNEJzD1UYtoQJIjp2kYBc7aAtHxbxoZMMiGoiWqPhg2boZtbsVWYX6LmesSEakPVPBqAdvn5KUuCjG4hV7bLgG8Q2TLblsmpIsohsP3dVABjtD0xHgSw1r_TuObEwTXv21jrehDP1Bks2DCKYR-xighIxfOafFt_gyCvoRx_RHErzzDN0aknUrxL8OrPWSmVKlLJk5x6NZ4cLKIwaSHdku93o8Vk0y2BDZDsoKCHbXKX0IGpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.
@PressTV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19496" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران:  "مصر یک دوست و شریک مهم در منطقه است و امنیت آن برای ما از اهمیت بالایی برخوردار است.  ما همگی باید در برابر توطئه‌ها و عملیات‌های فریبکارانه اسرائیل که با هدف تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.  تهدید آشکار،…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19495" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به نظر می رسد مصر هم کم کم به لیست اهداف مشروع ما بپیوندند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19494" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عربستان سعودی ائتلاف چندملیتی برای محافظت از مسیرهای دریایی کلیدی را اعلام کرد
عربستان سعودی تشکیل یک
ائتلاف دفاع دریایی چندملیتی
را اعلام کرده است. هدف تضمین آزادی ناوبری و مسیرهای تجاری بین‌المللی در
تنگ باب‌المندب
، در
دریای سرخ
و در
خلیج عدن
است.
بر اساس وزارت دفاع سعودی،
۱۴ کشور
در حال حاضر از این ابتکار حمایت می‌کنند:
بحرین، جیبوتی، مصر، اردن، کویت، مالدیو، پاکستان، قطر، سومالی، سودان، ترکیه، یمن، عربستان سعودی و شورای رهبری ریاست جمهوری یمن.
بر اساس وزارتخانه، سایر کشورهایی که در مشورت‌ها شرکت کردند، در مرحله نهایی رای‌گیری‌های سیاسی داخلی برای پیوستن به ائتلاف هستند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19493" target="_blank">📅 21:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— منابع یمنی معتقدند که عربستان سعودی در حال آماده‌سازی برای یک تهاجم نظامی بزرگ علیه حوثی‌ها از طریق دریا و احتمالاً از طریق خشکی در یمن مرکزی است تا گلوگاه صادرات نفت خود را در دریای سرخ جنوبی آزاد  کند.
— گاردین |</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19492" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.
این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت می‌گیرد که درگیری‌های مداوم در ایران و اوکراین، ذخایر سامانه‌های پدافند هوایی آمریکا را کاهش داده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19491" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">329.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 15</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19490" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19489" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در صنعا توفان و رعد و برق شده، فکر کرده اند عربستان حمله کرده !</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19488" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رهبر حوثی‌های یمن، عبدالملک الحوثی، درباره عربستان سعودی:
آن‌ها دام‌ها را نابود کردند؛ شترها و گوسفندان. حتی حیوانات بارکش و الاغ‌ها نیز از رژیم سعودی در امان نبودند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19487" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19486" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICtpbGXJfmrC1ii6U-EKa8oYff2h4Tb9ri-MwHz-z_uuvm4tGTEfsg9WmGNjsyVcc5uy6mhVppSmGJq1bD20VYmLrEaxgcDFPVXDfEMhGpfZ-0W5PEEYuzi-7-Hb38LcJwp8QvMHaSCzBokZAdOTBRNQ8inyAPNc62zxw76mrwPKdvJfkq65BIKhmEUNCK9mWTb1JJmnR11vz-aq_7kN_jCxucnem35_Ru2w0bSOkZpyrT2_D4WeR_LMGv2LLSv2oQXsnHCKiNceIzlPT2CgGososZFO_6jyYjmGEReHTqeDrhcRxEN3whpRvxUDPU8xBx-tO_x0laEwMcYuCWeUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما ببینید در روزهای اخیر اینها به لیست اهداف مشروع ما افزوده شده اند:  — بلغارستان — بریتانیا  — اوکراین</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19485" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t44rpvNeJjk_S1zRd9Pj4wibYpZXGuQbmemqrDRroNFFpLaQJT_uSo0wP9eht652a-kdkdX7G9kMoGSniTZagZ7BE2Gz1v5NuvmZ_9tr1FbgK09kvKYY9YTUlAdEUwt0KQOAXUjV551mbHNLkMaYKpISl-s3CHn6nYN0Z4yptMSw-ktgrlKNOsb4jBP5K5AYKATBzxRtL9gtMfMINbS5DNUnMRwDZM9KrxxxbNpZNltMyD71YWCOMKTWnZkXMu4de4XhHovIl0cBjGPxQxYQ8VNRIJ-1V4VyKUdH5PQHy-KUy-Ao21U3xjAcnb76PCWbPlb35y-zC3sXTDlH46kKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19484" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19483" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">— مشاوران و اعضای کابینه ترامپ گزینه‌هایی برای انجام عملیات نظامی گسترده‌تر علیه ایران را به وی ارائه دادند.
— فاکس نیوز</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19482" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 15</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 15
پنجشنبه 30 جولای 2026</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcOR95YNdcj9srGqlBatQ9GwVM50fmoiNZpPIxnf8lf06R69RkZgNpQdQWXm-WN2zirVe4HPyQhAqHikIdwl2wRc35gH4gxd1z4C8Db7p1_x-bLHhLubVighEan7KfzlAW7k0y0Kfb-tmuLvGnEiHrodTLNTQASQVtL-pbDDab-qvaIRe4yt9T2MJBP7Z5o4MxLUMrsfm5XxN4iqdI6Snz8S6_K9Vhx0gE2auoAgI0hkHHALuwZWymqyg9SKSxDZZUeo8DTxquLJIfB8MnGd0wx1a58LnfI-ZNTjSm-SZX1NI4bnYyQNcCpaGCbQH2cHEIsfqxnSK8yAaX2rwtEygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=QVaWF4QNRjkW2rLyrz123TgsZltBv2lt6PD9tGWKh9k2mBJTSyVrS-NOY7ZkROdDdzEaB2rP-iHlVRZ5jCzPf9XRfOaAggt8BWqQHNHfDwZ37lE1CnmET3ldRncrdf-Ob5ENe4Yk3XI49vbKxLvAvVYZqYPt2zHpAPe1S5KYBfKwHfSHQ7ARup9szcCi2I6ikul-QOqCKJquK0KDiTW6ynznT2GAmhiDwPQYUclV9bDdOe49JhdUMBKVqXysSSFtqtQdY20LlaUPiQBBdWqZHKg8MBXCedlC2RG9MiWuGgGoj0Hq-hBNAUCJIbIA5G_IcHqXymJO5KF-anOZ2bsRMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=QVaWF4QNRjkW2rLyrz123TgsZltBv2lt6PD9tGWKh9k2mBJTSyVrS-NOY7ZkROdDdzEaB2rP-iHlVRZ5jCzPf9XRfOaAggt8BWqQHNHfDwZ37lE1CnmET3ldRncrdf-Ob5ENe4Yk3XI49vbKxLvAvVYZqYPt2zHpAPe1S5KYBfKwHfSHQ7ARup9szcCi2I6ikul-QOqCKJquK0KDiTW6ynznT2GAmhiDwPQYUclV9bDdOe49JhdUMBKVqXysSSFtqtQdY20LlaUPiQBBdWqZHKg8MBXCedlC2RG9MiWuGgGoj0Hq-hBNAUCJIbIA5G_IcHqXymJO5KF-anOZ2bsRMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INyVj49LuvpCO26MA3Xd0Xd7R6UzWr588g5S4j8NQVuyMIEj9FLGlQqv_G6R8ETBtRKcjvZBS0EMu3gvHDbde8njX7jOvvqNITw8ZJa0-pZz8_6GSNWSaQn5pZwRTGieUM-U2DiTslnk9w_pLK4XBt_-yeVuUdNzF9khRIfXFt76J9gMpj5BimfDXHk5hhLvuakamBO_9qsM4ShJgUdP14Rwmxy0cRzQaq2_n_POAzpRG7i1EK5xddh9Vlebwtc-TRZkY3Z_5SvHMugTx4WY3SMk0A3AUet4qM5UyL0JT_X_cAZwX3a1KOYMvW-Rz_0ea91vbxf8FdsYazLBT-5tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNv6ELaQZbc-_-2k8fyhoelzFiYJZBHhce3jSG2-ZGC6meOMK_Nb1EcueQH5hbl_TJX0sXXZh3H9YoWAQ6YiQjks7-MqX6iLoqJeA45k9Fz4ES0ojnM1i1Bg2rQqMjSMQlxnXsgfVLHD8zFpuu7Vfgi8NLK8Clf-53Kd2nlLkcMXWV7ddKEOumMBVUH-DlQahmwLKhO-d7Tq1lh7VnAuLdeiuAm3-6-n7pPaiyVfK7BYO81VSZBQiu2mxIlZ30AZ-VwFgZWJSwNcXeDAeAThSI5sAokJEoGPZcLhRV9LlFPshZNYdo-c62r30ZmwviWR9TUYr1zMWyTvrkRtJg2fhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها چهره سیاسی، حقوقی و عمومی اردنی، نامه‌ای سرگشاده امضا کرده‌اند و خواستار خروج نیروهای آمریکایی از اردن شده‌اند.
آن‌ها حضور آمریکا را یک خطر امنیتی، سیاسی و اقتصادی می‌دانند که این کشور را به جنگی می‌کشد که تمایلی به آن ندارد.
این یک اقدام نادر و علنی است در کشوری که به شدت سرکوب‌گرانه با مخالفان برخورد می‌کند.
اکثر رسانه‌های اردنی از انتشار این نامه خودداری می‌کنند، و برگزارکنندگان هشدار می‌دهند که امضاکنندگان ممکن است به زندان محکوم شوند.
خشم عمومی در حال افزایش است، زیرا ایران همچنان به هدف قرار دادن حدود ۴۰۰۰ سرباز آمریکایی مستقر در اردن ادامه می‌دهد.
آژیرها در سراسر کشور به صدا در می‌آیند، و بقایای موشک‌های رهگیری شده در مناطق مسکونی سقوط می‌کنند.
این هفته، در پارلمان، یکی از نمایندگان به دلیل پیشنهاد تسلیت برای سربازان آمریکایی که در خاک اردن کشته شده‌اند، مورد انتقاد شدید قرار گرفت.
یکی دیگر از اعضا، ارتش آمریکا را به کشتن "کودکان، زنان و سالمندان" متهم کرد.
دولت همچنان به این ائتلاف متعهد است، عمدتاً به این دلیل که واشنگتن سال گذشته ۱.۶۵ میلیارد دلار کمک اقتصادی و نظامی به اردن ارائه کرده است.
اما جنگ بخش گردشگری اردن را نابود کرده است که تا ۱۸ درصد از درآمد سالانه دولت اردن را تشکیل می دهد
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt1nasteLqL3JMzcGgRT1tYRR7MJlxBpgJjaI9R-9XCJjhSg0hQMaKBhMJnhHJ01PLMc8bRKXa4B81BEwXTt423iw5Y_5LUG4asHMJvo23hFH04VONykU5fvebnMGCD1ype9xCNbellE9P4Es0gV0MiGimLsHpSU1UWOi8ZfMLyLIwsA2wP9odc_PTiRUzfK_lixFNSeX0ZmtFdMR5mpKvOhiJhJ2BChgp3-6ewJYOqBWrJ-4RATZbbCBW74ggtuvK6Jhpf-LpWAGwzc_pVfHiOCrUO7kSgg5kfw4WfYEx8xbuPBlgDAeqJqS6Iwk4-zRDRoNI5-_tamFE3FVgFjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go5VayZsnKzrMUNy08zPbEKFeSa0-DBAVRrag8N6mvPks8Wp6s_gg_UVWoZfG5QScgrnzZkH0BdCRx4QqzCCgsHgNfLLuziLBjdJbUqYTuywytVpmlCRYbaE0XNb725rPD13DzZS6cayS3OybqZmmo8L2-AdHm3RA-WT4BwEOCsdK5rjcCuORH69DAYmaWRkpedq7GHcvvKT0fgPAs_KDxpnYogZfzL5XW-iYDpdoI3SbKxfs8MeRX7UQK8JFA9LLqWp3B9EQYSs00M4FFFFsJLKsnhg_2NDOcCqqGArM_UGpBFpK8aNDOTwqFyLU6qCmrl62ho92U0ElvZ-c7oSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVRRiMnDlHuvP97cgNqCDdI2HztvmoJhVYYo2p-89bldimqcyR6PGKrsd-fCj8OVRfqCoHn3HVvEc32LSdnaTtUyyLqXw5MkNrE_xPfkD0T_7bwWixIm7mg-63JjvqhKfWvjgVosRIxRpV-3Ys6N4lwtSy8bYznB2vNDZGWCa7QA4JwmeP_IqnwJ7Us2SH9qXY3IpRQPQ5ChBMznkH4jC1mxHl3CkhxqriUTD_O0JDz8y3wHwzwuOZYMB31pxMFfk6MvPvpNVPFBNJxSQdnoGi-nizbbaCzQhXGopf4lycFSouvkvETPtFlIr2GF4lRwMmmmIboRsf9OouZWHWZeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTDVqK-c4Morph4k3upzrt5Lgg-yML8mNav2R0LmuEj2lYRwTr1x_JTZN7lLjJIZqtEiOI-h2x4td0AyQiorMR8PmrpKpwkRMBnqxt6ze07XgyXUM_Z9JVwrW0T16D4kT0yXjNk3sVQqqS5JYHTiIlDPdTOi1MMUdwzq501gSBDue8LiKUynt1940jkHcZiULo15ohP1mBDrdQe5c1Psp-IeLWrdMifpTT8GWNDWyWpS1e7IRqHZofkU9dwy8E950MA31hdBpw6C_lSJH-mfoUx5Gv3axZmyXt9Wygcp10Zpdk-iGl0V2sFQ9v3WHk0TtySm9UZ2wSAKXchUY-FI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlaawRPfquq1s18hzARswzrWUNeyf-i99p3pDjhYFPyKguCr3fBZsNVybeQ2krOx4UoQwdQQPIPYn54xIrrYaaYKZIHGvATTb4vfrMCOjH8lJ2CPmcsPWaHkuc0heGgMCrdnZ-rFuratHEdnq8zm6w01ef3NcsT7UxMIqe-MymJJrwENKmV-Oin23YaWsYokag23ATn5GzF5vulSNxKNiMtnkU-tpe0uqTQ4EEkJIBJ-S2NBgyoxYRVI9ODGGq4jOgUTdjgfUX3GsHbkZ6xtaKDPm-UisowQMYowO_XEAxx0GqS7yGPnpWS_kcZmSQVCAu6loeVpq7ZJLyxUVQyQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FunrFW5lpREvg3ES-K_aaoTu4q84NA0D0QJzD6k7c5DLP6P1YPmrC1DLtsE6cP9a1M3ZNb2rezFfjIncjPe38OGAOZd-c4ChVxg7cxsf21sF1xFxLF8ddCMQSIJ6KXeljjZdJ3UQpkzxZ-tlg3bqS4KDn0C2V7OW-uJu9mPo7WNnra5EjeqZva_ksbuxHwdHY2T54QBb6CtkIR0wyu9NtSGLuyb94-XGxNIC2d5XMxP1vDiJr4xQj_v7TQE8kn6k0dcpVE32AoBR_yBxNbJgZdgr6Eronx2m1U05s5M8sCaytkvl5GMDRtVMCjhsrTpNXrQYTSzCnwwm40lyHt-bjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSn8VPeOe3RbYsZfesrN9YmUqVkH5WFJmfZScCa7WNhoKeT1zBTIprs9Mwy0RNFA5BUPXcfrygVWhpFmyq921maHiU2HDr3qj80eAGXTn7nazO2H68X9ZWhk6vlqDY011zWpqZ3TqoQPALwnUiCoKSAyDbTSDBE21H0c_DTRCZh9RnNkE7m50ZH8gKTEAHr1l9b37lwYK27hRhxaBQh48qe8mBUGJ44egut_hPmGsAnEltttv20nszsB0KHhJ1IKo0U0BpJ16UHDtoDjpX3QmhVTyL4iuOEoGPTX0ZtHB5mwLYpN4F3cCu3TZyaQW0IDZemvgW2Gb-LmvQ54312-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=qjeHBETvkSHO2FEv3pIZL5R-7BOie39RojkORd15xwZdnqMNnMwhCdn9X4sB4_g52Q-397FrGOq3Np7xHfIeDrEvfc_wv1iWNfk0sMxV7PJ_--i6pRKdWdFWUsZ8CqyJn4hoNHfMsfemzmCu0Am3ZBOPV0FeoBOmOsiZAvxPsNrjzGO_EMD8PsEGX4HVnlr45TezeTytkB-eZ3REMVEhRNA2kxJITWtPsMVH6jqNEj3-_Of25y2D78nbP3bg-lmkf2NO0iqe1PsKGzbh9OjPAOwfLux7CVjPxVXE9z-Io2yjTkK9Irczu5RX02G0N-8RH8EsFtSv9E_Q17H9-dXAZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=qjeHBETvkSHO2FEv3pIZL5R-7BOie39RojkORd15xwZdnqMNnMwhCdn9X4sB4_g52Q-397FrGOq3Np7xHfIeDrEvfc_wv1iWNfk0sMxV7PJ_--i6pRKdWdFWUsZ8CqyJn4hoNHfMsfemzmCu0Am3ZBOPV0FeoBOmOsiZAvxPsNrjzGO_EMD8PsEGX4HVnlr45TezeTytkB-eZ3REMVEhRNA2kxJITWtPsMVH6jqNEj3-_Of25y2D78nbP3bg-lmkf2NO0iqe1PsKGzbh9OjPAOwfLux7CVjPxVXE9z-Io2yjTkK9Irczu5RX02G0N-8RH8EsFtSv9E_Q17H9-dXAZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqnikbtQtzmFuNWjCOWNDoP1bdy33_gOIbrqQRULDqCGn6WoorY-O9fdd2sbVa95nqgbzs6BSvzPKBA-bFroL9KseLpYOxzCrdlQhzPHt82_rLXssNfnfspuT8DFIDibyByiDKwMH-5db2ZwuVzKiYCgeCWKUUeWQu6GTh31gqH1XIm_8CGQEbVKYbjI68ObOS4Yh9jNcEVPQjRU3sxcxcOj3avDzHzNiYwO7E4bnAcyrbtm16D93MzABgH9e_nXhmlhlIrEInV0GbxCiYsh9pTuahdVjAB4VuBHn_Ect6kj1_6mxdbKbPplA1y4Qpm28aeHeNFmMyCGorNhw3nxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAiuHSp_eF_4vmjAb3NgVVVqcEFNJNOJS99V9t7mnSpHRNTjizZZ0h1XLeckhc_-lYVLx74xh0xWElk3LoTTUPre9-34KhlS9uBNyZ2BuzpodfUQ69RZxhUz_UZDdD4h1RBux5qfr2yF7db5790F-rCzdGno-y5_1hqa9d_XYQHeqQbIyq6Ul2jsLeFUW8xC9nKD0ebutOnF0-x1tAM_yP__c7NvL9z11-TNCDR_nbaTuhp_lOStDkKn6sbjj7DTAt9vPcFs7xbRHdpibWlaKVWrUfjK8NRjYgfAMOg-3WGgL8de4Trr8FJx_IQ8T62MnV-sToNcddTNtEyHPQIWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به خبرنگاران گفت:
«ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار دارد.»</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19435" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتنياهو امروز با پیت هگست، وزیر دفاع ایالات متحده، دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19430" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19429" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9ANzCZT1DkHHbHS5Ft4pWU0poLIktOcdwJ_Yi_IiLabAffSr9dgJZSj9hJQDVIXoAfZikcIW9Ks9-vS8WBifmc6M6CdiAnJoaMw9S2VKum_WhisFfkEDtZL6pvyR6yZB9apyAGsTMYBJ3OAantoLuR5QOc7IuacVzOWqauwml2-vG7L8oHoqkUM3mBJvDeM1Q8Zo9TEamLVNzC3yblbQkFsJj_Oifa9qWK4dH-a45G5Yy_ZpWOVWP95Bg0XSTNT6K9JSkB-4AwIYv4mqieFptJIwzkkxCdypLmj-cACxYvwM-lTu5kUkntD_N5CWPTIrxFPsD01iRGfbOS8igcDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وزارت خارجه در هدف قرار گرفتن مواکب زائران حسینی در حملات دیشب سعودی و آمریکا!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19428" target="_blank">📅 16:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19427" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19426" target="_blank">📅 16:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انتظار می‌رود که اسرائیل امروز به حزب‌الله پاسخ دهد، اما این پاسخ احتمالاً مناطق جنوبی بیروت را هدف قرار نخواهد داد.
— کانال 14 اسرائیل</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19425" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:  «حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19424" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:
«حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19423" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19422" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ue4zPw-gn8XwFEbFtz_NpfdNBxXuAG2-uMCWVyaXkd_0_KzraPMEVCl5WShScywcFIg4xRIfEk8Rt9euuEWiVSJWYOCrmXpau47cP_QZprIXmvTDc6fQ_DFIGhA9de-15BVfTkY2gRV1Y5y1LOhqjee_t64IgFIspfiXruRH5sIi-dYdQeLPvFd1iITl0MrPHJ4LAF_s-M88wc2gJCZHQTARQqiSmZirSU6xipg6VvQVZsx8Tkl7-4gajuPzZkE15AqdRtZlglgQvNHyqpK1Iu_eGdG3Tz0cZ6lwogX2QA7Iw_8P444LsckjCWqIN2sD11Hm3Qd2NGmhYQuFL2SgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAu3NSiTxtsJMrbxnocCVe-YEVEeAQbrCKkqdHonFKD49Bz30V0GE3hSZB9I0VPjvuyj40XPh1RXdp03WPHwCojYmm-NAIIoTWFIwyYU59D8_AYiHo8iwB9-FkBed0gbvz1WOLZRED6bRD642rqL07LXs7YSLwejxNApAktklo2mE_2zT51FFPhFV5JCf2VMA2pJuTdozuuQPfbJ7sBLyVGNnvmWEcZtvq-Gv4GuJjRj8DwjHKgYTcKrJK76WWiqQTl9-QVzMfUG-xkmKoB8ld7pmatlBoG6Me3Vzk59Lh-eHFWwhlanWhpv1RAKc7XmMx9iP_KRsEta5XIP-Gdm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=q8_HfhzfbZTfWXD9XoMUgLl5ZvAuA274TYWjJxFzV34zHHfcMiNS0D9OQ-uAJ048ZMxc6O4MqPNW1gPZ2Ase3ieciIfBrJjDer8l9YYErswSq4XiB_NJzeFo1lxn4g_zkgAPfEkJ2obPL6SvUAOaDfhgHzklx4OuNImaaOp-NUBvDxn-Q3ix61eJpRPxhvB7NaRDx-2GdfhXkh-_s_BOGFByODA7tplthihlrt07x2aLNQ03sBAyMVnQ6umSGAhfMd2JFwzJ9pcXrOgXvFh5j7W3DiCR0Hgk1Y7uHADDU9_tF0jVHCTwKLj4XckZtvGaT6kLyuY9Jp1noNURqzc6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=q8_HfhzfbZTfWXD9XoMUgLl5ZvAuA274TYWjJxFzV34zHHfcMiNS0D9OQ-uAJ048ZMxc6O4MqPNW1gPZ2Ase3ieciIfBrJjDer8l9YYErswSq4XiB_NJzeFo1lxn4g_zkgAPfEkJ2obPL6SvUAOaDfhgHzklx4OuNImaaOp-NUBvDxn-Q3ix61eJpRPxhvB7NaRDx-2GdfhXkh-_s_BOGFByODA7tplthihlrt07x2aLNQ03sBAyMVnQ6umSGAhfMd2JFwzJ9pcXrOgXvFh5j7W3DiCR0Hgk1Y7uHADDU9_tF0jVHCTwKLj4XckZtvGaT6kLyuY9Jp1noNURqzc6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5gFRP3p3PX-tVP_tehDLNRXioFfkQ6N1U3ToXsQCHNQJN_PD0qwW4cN-VEXC6v1bFKahT-Rlaqo8mVgo7IZdab32PIsYmGQ5v8P9ZX-gjf7k1QZdtO1mKgeBW0SC8DBtpCOYQItBPzzazrvhTClBMZXwzIBLW6TcPAn7Zen3otKfkGax8B88CANYzKAKnxEAwPCqY8Kb2642VX4Utx3aoI6enEnhCbewoZ0BYEoPDhmPX7OTGUkwWa4s0ZkKNxMc0ltxvmGWYEEou1FfplHjwtjBkdBz_7yjbAu8aTO2xuMFlKnjqAxvubL9W3Ouh-51mbByTc-nc8lDezBlngD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUoTvnfBprox9Nj55R_PYXkPd9-Snrw3LXh5qdxdXTKXQSbVYeLnmnIT_x2IotBPcSeeN9dzRYjXoNTz8AMmcTluoBFk-58Mm5UC63AzYF1hcJPrjeFO0k-bv_hmIMT76EX6uB27DeiCZKJtCt9pvmxuTNJxQzTwdcchv9c5OJ7ck3ZTvdQ9a5cL7KsZKl5B2fzJjNlpeMUOatL5q3k0PGchnE8EpefMbgHUVx1hS7R3kVJn9u2O9WvW91oiKxW67QWdvEcNQVduwegAUSZcdzMlSCY21-6UGzG2EYUgFFaEhm3ZDlxGVPod8Yp_XvaCMb03bXvLuVDVTSIYjPGYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
