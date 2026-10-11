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
<img src="https://cdn4.telesco.pe/file/X2vhO_RfsG2FwHv5iDTvgW6gK4QqykL8bfl4iWAgj6dvkaEgStGoYHQXg7XZIdPx8_MknYDkT2a60EiObWiUavayGIgUN2yFslGJMfquYbqkMtNvcz737fh25Vo3_S2v9xmIdytAXpoDcYmNOfwKueHmXe5kyP5bZf85gv0AMrepQh86RL9vbDZ8pUeO5kk77zzaoxsAs0UMokNlUhNQyCA3sB9Q2EGRuV4aofzMYOpFKJ_fJn6-HOJkH9DIoZEyIU15JjflI8HU0flSIUqeP0SgdvQaEnUTrX1VMyL19zErvzlQW17Mqe2oFZycM_vsrg_kBN0dGlaXEDTeKs5nbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 267K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TyKi8e8UNBxn2irITQ8qIR8PbNk8dnPdMoKqfMcqNwk7dU0e3XktaDqebIn72zW5yR7Ytr7qU6GL6-eut3GTOEvKcJ4mW13dDdnyJ86VFS6rqteGZFt-kVqDRB5xkH0CWsVtaoq1ywQreAXevaBkvfcrwsBBoysDha96f9_lt_oAI3GAedwlBHg-FLMw6UNpQF_wwbTmDMytmiq4Lr6GO7h5xM176c-DGVQgwOyjxJe15eUaMPINf0Xk3h7Ngp_gMM6NGRwym72hM3MBUwyVznyTH_MDmNDtXx6KZH_5VDtHI-4L26vqOQa16xC3f8C6y56_U2vniYoaP8Wk2WUD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TyKi8e8UNBxn2irITQ8qIR8PbNk8dnPdMoKqfMcqNwk7dU0e3XktaDqebIn72zW5yR7Ytr7qU6GL6-eut3GTOEvKcJ4mW13dDdnyJ86VFS6rqteGZFt-kVqDRB5xkH0CWsVtaoq1ywQreAXevaBkvfcrwsBBoysDha96f9_lt_oAI3GAedwlBHg-FLMw6UNpQF_wwbTmDMytmiq4Lr6GO7h5xM176c-DGVQgwOyjxJe15eUaMPINf0Xk3h7Ngp_gMM6NGRwym72hM3MBUwyVznyTH_MDmNDtXx6KZH_5VDtHI-4L26vqOQa16xC3f8C6y56_U2vniYoaP8Wk2WUD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRvVFJiOxBDM0ayAFgPTL0_0AY6Ndk6_dW6VYqIFnjvdRKqMUE_4CO2rj_DzBwe775q2LiAmAQBYeDsBoPNjtVD0_tRmZL9TjaROcni8NrKAmDcwVgIWXSCnMGAcqpBStfRS009-qFDbyYtpzYG154uZID2YHElBSmb6GQHHvncgqhmGrXmvCHIyGrFpd2MFB-YtA88lR5-Cnl7fTBDgBCDHUkhDISoDOudocMsnpLLyXyc1P3TJGriPRj8xyQ-bv_hcf597EE1qrFj9SN9eEaHy8wMoJVUU8HB6K98j6AlgcQGv0oqqBmuPHwXqD5jlGDyBYSIFTpuxmdfpDEum_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAyzh6NaUdRrwRYCWwuHVWGbbNWrPQZMDaXzMObiJRakzd8pTGqUTAqotLYaOx3bH4JT-lcxsrhUdcNd0oqK8mr8z-Tom3dpsB8WYFffc4Q9v5t5e7k2VL-SAjBRYtRP72O44JYITYXjeVhNfYJ_kIzJvaoKYq_i7q4wUn4YDJteg2XHu9Xr1ocHAAI-5qaKj8ZNtRyuNsrcm6FN_Y0QiF1qYL6Q8-XuEDu1RVokDXwiqRwxEx0wcGTgpwJvQ8WPnAbq0ZF10cMF0ZUxc8F72XzPRecncj12xO4JotGcGfDm0dh45e6ZRVewGWQgIMtH-UiiKxLahKbYHApYK31KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=bAd7OxmF0SNLhXRYeOh_t_Y9h82TXzYe48qcrx4kBDAsouUXI6HTiwlP6S5LJThgvdzWCh9iKBApIg0wzBjSkm8phjQE5GFi0-nIkUyN9Mpur_F4jllPBm15Frwa7f1DMXM23txibZqqEZ_zOodxdr7LWml3-AzUpjcMakabAvVCXg5CLcld6ZVIvWmQNsXTFsTFt-3SJTkrDXomup4pFzzbOmfvog0uDv_yBGBU2B8OpYeAh_rpGdbfGiLal9gYgdQZ7MBAESL1Gepx0VR-lJvfp5YgTxDPEx1hoD6XttLOTf-fRtgaxSgQIXAz4ouGXvGljBg7kMivHVX_ayyJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=bAd7OxmF0SNLhXRYeOh_t_Y9h82TXzYe48qcrx4kBDAsouUXI6HTiwlP6S5LJThgvdzWCh9iKBApIg0wzBjSkm8phjQE5GFi0-nIkUyN9Mpur_F4jllPBm15Frwa7f1DMXM23txibZqqEZ_zOodxdr7LWml3-AzUpjcMakabAvVCXg5CLcld6ZVIvWmQNsXTFsTFt-3SJTkrDXomup4pFzzbOmfvog0uDv_yBGBU2B8OpYeAh_rpGdbfGiLal9gYgdQZ7MBAESL1Gepx0VR-lJvfp5YgTxDPEx1hoD6XttLOTf-fRtgaxSgQIXAz4ouGXvGljBg7kMivHVX_ayyJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXrhoQt48uBZQRVcdMhtYDvd_KCaquVOcSseJ2aoaDCeasKAKxdPZx2x3wP-kgaLYJdFMaEscRYuYvrTNwikf-rJYUz5T3-JZ8WWOrXw-yanLqdLd240Xus7lOFa163XoDvDETCH_oalxJ1uJRyhGmz0-0bKJPRaqEbwcmPT5lWvNGJb-Jm5mwh2SoY9lQqJuR-kxPrTadb9FKpQx-qHFHTuP6F9q0kA4hLqJ8ys1NWOlMlijJfBEnmAUIVDePv7P4kPoYR9RKnnDtQ4RDg1A-qq4JINJr7ibKB5XfRM5T4hgyIE9DjWZEtaVq9-hr2q4YjfUm0uXcTFQh271fchjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84690" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtCiTpyqxSc2vG-thpR06ECyI0mMCl7MwmqrDV9MH24u5HRrZ2t1253Y_BLOrneFspUBQffs-XBeKOzqN5V23pz0fRuj4D5WKtao-NFEtoT6VXxFh7nPoA0Pllhg6afJufuIV0zhEcCAdydpnpb2kaorWLOsRYLJ3xLlMQTr6OBx-WwPU6siYLyfhS7LXOzBJAbgbSVyLor7LkltpFdcI9zkgvRaH_dJxt4rOHyHEWePasyn_c6XIj8p4GmN15BrGuJJVdsac6fdLcZZ28viNqiBhL6wLVoeS2_MvSlIEwh-GcRG-ip1_0t7_qhARJGXQ7IgXlOeEYwboRaTQkacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/84689" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp_qqoZos2FSUyoCO8ZYdSkZ2km3mVIV0f44-NS-vVDFtQM-rQqdbzu84ddX-hfuk-F1I2ANP14-K8MVbwikLesYxffyu5V2Fep-e2NgAVjRAR_o0h81Z8s3aHNpNAn_0l0BLZmTJe0hRrL1PNkPDvLHECQ-iwE5cmg0twvOmw2LFWNZCZ15FB6a_D6jGKFBJw4fUbn31PBlj8jOsv2b2Mpq3030U0xJUNqcROnQDP3-X1RigwD3It9wutw6jRVqtKGDgskQ6FR3yEwaWnmhMh9NebopV75iXE0mRwDAMNhXufAiG2Bt_Jdt6E_oH-0d6QPkn25USGdvhbnoPBDZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJtbqiyHTR2XOmtxkgwzp3CI-fyevt-LsXufhwgk0DWcAlZEbyluC_n8jAytRG9OsUX4Q8HmsOEEl2k-ajxp7mplclFNJiqdIbOW8oATxO7teSajWKBj_il1ibhpR6NfjXen6-3_Bngu4tdCeSpPk_P1_qK6chuI-grhyGhFLHToBk2cPx3LEt8qoSt3P8VD0NGXqh2f3oiIUqrWdgTykyJ2NarGWbG13Wlp8jIjGinqrMXYvhMLYy-XSOaJ3UVS3o9GFgbPpFUFRAJrPkihzhNvRwf2kTNpGoxK7zZn36MQ28Q-rASoNGjdXQHgYy_0ji6lWs1-a2UEWv99Pi-j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cpSeOdt6cYb1rBZvwMdVAiUa1Jp5X8GmVNdnBpPEk3BOJG7MTsBmpy-kS6w63AJ0PNPOsSyidGRaPQQAPM8xaf2tWgme7zIO6yVy_x7l9amHqqtWSKsrxgvKfMli-hByDdVgbxdsz5yYqUY8cQobp3b8xBMU2-0xhMWvRwAsk48TclQN2AQWx_gyS9xkZnlGJsP5pKuXMvvNeuo5TzhUQAiC7jBCnbaaUXW9GeEPJUS2-L8LaRJ9l4NdNW8NhiP8QNTfaDa5CpMrXf2W4IiFMuzD9RbvoWgNG5iKtmdOpCyVvVxZGehPAka3mJa5O_mZjwFuBjEXpdnFW6FSmzOjF5Pf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cpSeOdt6cYb1rBZvwMdVAiUa1Jp5X8GmVNdnBpPEk3BOJG7MTsBmpy-kS6w63AJ0PNPOsSyidGRaPQQAPM8xaf2tWgme7zIO6yVy_x7l9amHqqtWSKsrxgvKfMli-hByDdVgbxdsz5yYqUY8cQobp3b8xBMU2-0xhMWvRwAsk48TclQN2AQWx_gyS9xkZnlGJsP5pKuXMvvNeuo5TzhUQAiC7jBCnbaaUXW9GeEPJUS2-L8LaRJ9l4NdNW8NhiP8QNTfaDa5CpMrXf2W4IiFMuzD9RbvoWgNG5iKtmdOpCyVvVxZGehPAka3mJa5O_mZjwFuBjEXpdnFW6FSmzOjF5Pf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9XjxeD5QwgdZDVuXSLQIhB-1_WBbmPXO9gj3-lKBtYhXFGRodbMuzylTpr8f8HR1ZBafWP_rtgPhSke_vdd--fnC7M8-DrGD67-D-56syY7KvaPzc8wxf6PxEWudr1U7CsSRdDtoBsZ6BraSG8UIqKFIIndcwfN5PwWmyC6JkffnWBSzgj8bgfSmEB8RzYS2CPSfP25fM9idPUOzsuVlWBR9csKkTHiA80qQK13lP-mm9TFQzKccbFXfFJzWaTAg_XLqQTahWK6RlDS5V4p1hwR88-5KH2e900rvguh1PVttN3Amr_1Gnkqzu5QyVb7zIP9rXdQPexsHrdtQ0YhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fliGJEG1L-6K2DGNVtfHoy0Ht6UhHWx6wguFTScKZd-GxyzVhRWp9dox1_VmKGMoRQcqobEMa_9aECL7uipbTGC42u6Qd41JByoToH_Y_fESoaUpJnZG1Op5K-2rEAuCn4CXCSqAxz31HHvUD_9TOdQBgxrmWkDPea_aR__KVyKBGp4aDjdDtnzjSHDQJlvuU2111U28O3TBEdR4bL27Bvs7VXtVFT3RPVrTC5RT-AoV61jVN2SSfSvNv1hZncTYrpzdu3vkbOR3cUNR_VfTyiy7ZRdBwkDtG2zUrH0PZPlwD0HaZapSxh5RZqbIwK2ldxY6nq9npxO726qTYsjNaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iizZ0yTFdfnWqq1iEQFQdsrxF5yHf2pXCS8Rt8pY1ctXSfQIuxEapY0WNI4bbOe2BiWns2f-zoLB2VQ1sGw7MBTr4VHgspQcqEJdLo8okZ3R_YoCzeb3VVRDgErJAJzr3PJCBakr8tMbs_5Bb2jKM2PFvcPVgf0PSZeku339TdRAV8B9OjbEtRf-vG32Rk1En-9RLjzUfIPI_7C1xVLVmQ4C3_EjeiKpHRvxoEzW9Xz3qJPLxlmnv5LnTlocIUtOdv6XMy1hhPC6bTzrXxNC3UYZ4pEikGC37sXSdkedukCw8i0WMd_PCCdbSOfURuaw5_2WEBSau4F90TtEBNQqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bucuMaHf9c0Y00Wk5FeHMhLKVshGvjFseNmsTS0l1TUC-6GsqnPPJsqC1QjfMKRT9AeGIP-tyKkV7ra88mgQfQ74o8P-UYGmTBZVsic9PastAaeLu32L1p-dyiSu7bvqxIOLKE8rwThscqSlymnJl1yxIwUHXOu1hjS9NO0s4pnep7nkDc69ov71IE4So2WZnRGQu3gYZdcvMdv5tC1c2A3wLhx6L_GPvNgLWbpxiWiIY5odQmC5ts9iizngF4Rj7Lsypu9GIBwVQ8ZXRxesWLgqdTaVvm3hjW3Fwe_skFolhVNiWCtLsU6U4OTbCKw8p-CNkOqZjoOMepVZUr_Vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgWWVD3SYaRQclvQVyuIej1RBjjgEoR10PUiaEe6f7b9hc3c_113XwjxKtAYkSmJg_Pm18lmTaWYu4osg0bJw0kpGhAm7MNzvWMW7NRxXRhgaTMdU33fRST5qr3W8x3uEm2syd3GeDAcEnRnYuMJeg7pHw9xK1k5WkwLNOEBMQJpfPTOelP8loCL_1SwptOmvo3Ha8UDcl5yZzL5mpDUXMF3Ed7-ZAFsMl-YwZhoDhM_AJo4Kn4_r36LnwhLi4QgXAC68Bax_CETNuJFFJozLoDvYl-VxLCEdCE0Fk0T7Bn3CoWRWka2LVpH9Sf8GmcjlW7VU-jDz7glcPxhXdh25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPdFVSjOW_m2ojb4RnsHSgbdMTTLQjnMVNyv6TNkkYppLhOlAYCmSS-6KcTM6tY22I-tbrWD2k_o7Mt2fUq_pc4hIl1O_QStBDZlGYpxrOozwQle2xsKCM2tw0-qTYoOUfdn71wwFAurvi_Iy9tgxBuztuvJDukqlA65nEEj0rLk4Xy6WACbkJERv5TCPamSZsIkWprkOjjriDzq6qO_Ivg-9YxdvfBSeSgswaV8zEZ2DrtBZcOtOOYrOed2BpOa9iYwkXU_rKECQ5-KpQxEbMemvOlWMIus2v1NuDkGAGlb6PxwWoFzsG3HRz-mXuYUMhQgBb1JyY1i7WcP3VsMUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=mCSYx6v3MWt7EXq4mwmETzSWp9FPaDt0jqVhhcLYYGGTz0-Et5NfTvnuo1-e6D8Pv8RMM5u6vPaVUFqBLKvEEhlDxugCY41ZiT4uIciSB7nNOoC4ikMc7xmloDixp2e04Cu0p87uVGOpjhs_WHH44dWNcZRRSZunkPTSCcoSAuXa-kjYryL8SuxNiiIbVHM6crZ4SKqeNl7jAyR0uNidPNqxmKPsehrgLKtB0J3827xhGauh8HKcWyrXM7kkbNIHXw7j5z61cddYiJH3rHnp88YjfGo18BPnteip6YnVKMxeSmTXG5sBycvz083xnMBHNKrYBhdMcpfygDDuwWQUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=mCSYx6v3MWt7EXq4mwmETzSWp9FPaDt0jqVhhcLYYGGTz0-Et5NfTvnuo1-e6D8Pv8RMM5u6vPaVUFqBLKvEEhlDxugCY41ZiT4uIciSB7nNOoC4ikMc7xmloDixp2e04Cu0p87uVGOpjhs_WHH44dWNcZRRSZunkPTSCcoSAuXa-kjYryL8SuxNiiIbVHM6crZ4SKqeNl7jAyR0uNidPNqxmKPsehrgLKtB0J3827xhGauh8HKcWyrXM7kkbNIHXw7j5z61cddYiJH3rHnp88YjfGo18BPnteip6YnVKMxeSmTXG5sBycvz083xnMBHNKrYBhdMcpfygDDuwWQUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS0kR7gqPXRb3GRcBW2UAKNum3-3mMyfdDi_mbgArlNhqAI7EB_upzP4vc5TQiVLaPp_2t64sZvuC_g8AdP_iIyu2F-VYINI3pSZcvjwIHouRsvSRVkqRJTu8fRH_gVJUZVa1tDSQNwr2sCI3s9YNcfGFhbsS6TvzHJ6Yq6tdVyETCos9JGD_Yo82ay19nCZSlt_sh2tQYjEVixQEYST42M8j20vm9fvBUua7N_6R8Ab-aaIjvllKOxLm4u1XQiaZN0URA1Q75r4xy6FQfQ0RJUmPoz99AJKEviyh3PHZS3x5Rbgk6IkVj-RIntyQQotlBz1yX5L6USKwBwQD_yN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKVvUOM3OkQoKERB4259ECKRuuc-Z-25iJ5CsIJGJeSjPqgGyoypMG-N2hm6CAjg_lhcj3hvgE7dr2d3TCcRodu7bELI5ofYxkylcOiYODWENtZoUVx3RD2m6OfvusFioko1yLDDrAOQqGQR8zzbcqce--zpWw_6xYv_gWMaLLpEYolJsrLIRWKyVsuenfApggJUHZ6EwZbJrJSB6wUYkyUuM9OvX_4-1NdLsc-lGtjv3FVZUFxsBccOkN7GSHnx4NmmZIFQcQCvCvStv9x0JH3SSKcajIy0WZ5Mm_ugeMtMbpbS3g0K0Y0Ib5pfbwXehgeG9NWjR651E7qkRpGHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=bizNDSAaY1KMEXyn6pWCwoB8GQISLnpFMAWIGWGg7f1eHI6MsHxBrAM212dwmCX8wFn4y5TFAzwCkM2kk7m4YgY4FmWIEtS0saA-1AB4TImMjnh4z6D81f9GVXljA8gzsS1zajH3_g-A7rax5SUUjj4A4Wt9Q5FmIGDVoPSNhqCxImbZoMDdOUM2Zis6vVSFLBFK5lEHL884KqjWKAngYkOiISRBQvSFC3a8aTJDt4mePcQ--hMTqEv794H2ooinYFRb5-auxemnI-fK3Cj_l2vLQHFgczzXy-tgNmvDuXfHRrltgbImavNMm6ZRg_5USu9jyTEARn15J7qtONVYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=bizNDSAaY1KMEXyn6pWCwoB8GQISLnpFMAWIGWGg7f1eHI6MsHxBrAM212dwmCX8wFn4y5TFAzwCkM2kk7m4YgY4FmWIEtS0saA-1AB4TImMjnh4z6D81f9GVXljA8gzsS1zajH3_g-A7rax5SUUjj4A4Wt9Q5FmIGDVoPSNhqCxImbZoMDdOUM2Zis6vVSFLBFK5lEHL884KqjWKAngYkOiISRBQvSFC3a8aTJDt4mePcQ--hMTqEv794H2ooinYFRb5-auxemnI-fK3Cj_l2vLQHFgczzXy-tgNmvDuXfHRrltgbImavNMm6ZRg_5USu9jyTEARn15J7qtONVYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF9SPTF8lc7ilEsTXTJB4vLtjH3cKC7dyx602Hx0297CHVEfRyzNxRgxE2n-SgpSvIHpYwXJNgWa6gmOqvTyS7o-lh0iVHlqQuqigwxLOHXsNjnJBupVNTSGI4fYcCu3ekVRvxHZc51oTyxiMqPvVn89zkxWuGPK-RRJibPNvp2MCse0zDdOqT20NQPvPZVCAxMazrpkHZ38FP0K2ARdwwUcXaL_TNALjW6w_xHe4keRf-Ru-3_Ti0RONt9dSy5vqzMBZufSHkCbVw5OfGXQuzi4heFT305krx-2WORe8P6Z8phe6rX1T_w6eQeM90Zn7G3FrRhptPB91yPXt4Y_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhs7hFyGMc1XISk6857o-IQW_F79wUFLt1iie6Rog02qMqjj4bdjcb3eSzgoCSvwua_tV2kG0j4IIQBDemc3yN7zaP4DAcgW3Qs1Gd6Zj1XquVIx-D084AmWJ5uNGkhwGpF3yRgQour6Xag3GH8LbcZYcsNDub5krcLdblHjnSMaDyAEhBvPs8O9EOMasymkIBXiFuYcSirpQvlq-3FsvyWflp0qnvEh9Q0l2H9aGPmV2AGC4USzqW-ZMLC2hudXDIXu7atVTw17qZQzf9c3pyCVbU31am_KLReoFFSNVC5C2EnXih1fGJKmxXg9eDz2iChtdhjIr-rqSSbQrijYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=AyTrHE_K1kK9Rqi6qIfVtt95XV06AZKAN_kJoQeKoMqfSdWOtOP2HN-ws8FZcKfz7SlOJDRb4Yk3xDjn7NXZyPS1lxqLF_D4F6UAO60a-TtotDucL54FpXceALdjLzzzM5_Hpd15GzcJKKsaRvAMR2rmdbSxVa7FO5f9Iyeydz3mF1xoX3pyoR2lDz6FqmIca3M8LQLX9BR2PtshYfGwgtjT0x2XORn9-Du912PIY25bQly5gsBTGQD_-E744HEx-nlBKVgJ6_iC4DuvJbpct_d1MmlnjtldQxEXpHiy8QuR8xgyNdC_8cJhFvT6EznwOUl28fC-0TGUzV34Jltfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=AyTrHE_K1kK9Rqi6qIfVtt95XV06AZKAN_kJoQeKoMqfSdWOtOP2HN-ws8FZcKfz7SlOJDRb4Yk3xDjn7NXZyPS1lxqLF_D4F6UAO60a-TtotDucL54FpXceALdjLzzzM5_Hpd15GzcJKKsaRvAMR2rmdbSxVa7FO5f9Iyeydz3mF1xoX3pyoR2lDz6FqmIca3M8LQLX9BR2PtshYfGwgtjT0x2XORn9-Du912PIY25bQly5gsBTGQD_-E744HEx-nlBKVgJ6_iC4DuvJbpct_d1MmlnjtldQxEXpHiy8QuR8xgyNdC_8cJhFvT6EznwOUl28fC-0TGUzV34Jltfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VofaVgYUJUJOGTVdra_3qQB2zNLtysKNXadJMNeMOXlmJlpDxfQBcOWRiObZsn_kWzm_F8zZd3ic630wFRQJoqgElLq_XeCrEN2_Xxc0cHXldG31YirUQnvSEVz8j7H95fGvo9tpZ3DF2nOIu2I0zOgUosZck5WrYLIYrIwczeia3Sk1RawYahEoa_jBXGPLUruXm8pQ4O7YpRWYrjBPIr9x9iNzFqQspV7UM4d4YbQ17tx6gIew7Ap6YLvAHgDRk5dQulxxBitqRDhodtWDD0rqTIPmJQ8-WbX64JV2qiiKrIRkU7_cG2mRBiXUc8p_rLqJmjrWXX8nW_QAKo6-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGv4VHXfZ9j4Rz_oWHgbNxA7bxTQP9Q69-KN3APRt2cCIc3cy80doc2utDJNUzlCrUxQVyRP5_k2bHL_r_XzlvCDIJIP0vVR0w76Bim0l0aEXmFWyOri4A8-kGwWznOEeyOmsleMn_HBfGoxCc_8a76WSWffQQc6Ad7TPgTmr3lLo8zHSNvu1oCGlSAUPpAosNY3pBZN7Fq3s98NuXGXglchsj_E4PT4Ogzqq36ILqxjHohJ-hWjm7RSa9aVWY9C3OShU6NLMhI-7euhUhZ8LnEK2RajtPyKnnH882l6yKLsBkfZ9UQ1duWBD25cYNTSgVrfJdUrHqo29-KMrEwnMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIJY1aKrwxwk_RL-UldpbgnEfF_IMsQeMgr_LuEQowyqGJbP5urfdXEmgILaaF7PEnz3S6ytHKpJajkm8kdRhtsXvsjZjoXYDI8uJbzW3fJ5PCGAJXh5oza06BzLibVTvadPas9AaF39UrF5mIKNNMdAj_gBA0UwhEwTPU-GilnMr-IGl_SISE4yc6iL2oHWWH4gAoVILsLsFysVgg3eUvmlBpVjMbFr0T6MDTMr9qYmDV5ZCJ-djuJDxpcMqfgKfMiFhB2IdUzIntnhL1lNSA0i14GH2B0DxKvUQxjGmOFe6lq8kA_iCzRRbHMFHi56ktWuwqtDYXxtU9Tn5hvTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h79h__I4BtGMvoT77a8n5phLjG-mMJjUGJR-SH_5KtPKHJrNTgaNKFeaQjIRHtIRVcwrT-1Kr8xNl6ZLBxl1M3BaVZCCZDTF4k_FpIEGqYn-IoGOxOh68ahKgLslWxHkfmaaKyraRFkMqHerUQlk5shVWXe5tqZThR5Qhr2zS2pXfvYaQihOWn-GrPyxIWeKQmbYeFaHEbjVvtsWQcIzDT4yimsgmdhAQ-BkHPmvggcYQgpaboDRFUOhgcl22nqAiYg8ZeejkU5URL0uZJqrg34Z-cmngAocIKe3PaWiwHoD2ZRzGf6uHYx5Y-JBMh54F2CIPXFyAy_nNH_Sj0zqXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv2poAaeDNcA9cinfdGohkLHIHivDtPSFVh9vKqwfoOwOTO-B8NVvmcBHjusehPv4B2PK65ZbxJ1ElcFmXBNMc1okLhW9vXCU_4p90-dQPt0UAYjtmSsSUYworkLjhxtx89HuD2sy4dSGM2l2tNlkEjYJI1-j_obITVC3U0VcUfa3wjW7HOaguaKye_Ba8zKeLGDi5bV2EP-4rkcsp9KZ7XACFxqWy-FFiyTh63tOKz0w8JnHItQOHGl4V-sG1krRfeh1NwnGeDrRBJfXRppR5JE3P3dfl0BRSG5exTFQfmbbD5KkoZWhYgOdqmMSmpAJExg1RL72NezW-6iz4MacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRtA06HTRN1hwQx4RtXVxP55ttwo49VMhDX1dZw3vNfgPH1UnS8bQBZQQ33vyT16b2kK_sSea4twWcbp-qOqBTP9qZpJ-7L-Aaxu_rQl8n63W4VRlBeirG0isZy1XyHHzoybr7sTTaraIZlsisBiMAgSl_ORfDsG7sWsQwqYZU2fyb4GgsfeCM8t5QHP87e54AyUJNaHQU5Eni_4xbx8ygJwZxYRURlAFkJIy3jyMC3hRNbgo3FxREdbOPytQpRm3onQF9gCjunTez0yQD_xzwAugQu4pCWaNhpziLhM8eXpxKXjo0nZHdSkHH3-xgzKAtO4w3wD053drHEQZCuGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=eZYJRdWzBwNUMYcqOU9wazSk6wa6Lbtw0EAgxsz1SiFHzB7VuMMP4wdM2P6prI6e6Q-skRV78dPp9oC9nE38WRb1FxwA5oq5WD4cy6t5ZWVF2hjInqcGin3VqWatdIvmMTLNzfmXqn_cThbUnfFb5SClEEI16qdVpPEItF3u0sbx3hfOaEATaOE8Fu1fXLjvlU3usULr5Si59FKwhM0hS7Nv2FI9pt49X_yE-GBiknigkzV_ed9IV2n6XfscCR1cNuCWbMCvWY5V2hG0hc0LK0dSifUxAnfvP2DTyy1mNJ3FIkjpuOwVp_YlPKUNRD_JlS8XId6EMRnvGE-GXpZZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=eZYJRdWzBwNUMYcqOU9wazSk6wa6Lbtw0EAgxsz1SiFHzB7VuMMP4wdM2P6prI6e6Q-skRV78dPp9oC9nE38WRb1FxwA5oq5WD4cy6t5ZWVF2hjInqcGin3VqWatdIvmMTLNzfmXqn_cThbUnfFb5SClEEI16qdVpPEItF3u0sbx3hfOaEATaOE8Fu1fXLjvlU3usULr5Si59FKwhM0hS7Nv2FI9pt49X_yE-GBiknigkzV_ed9IV2n6XfscCR1cNuCWbMCvWY5V2hG0hc0LK0dSifUxAnfvP2DTyy1mNJ3FIkjpuOwVp_YlPKUNRD_JlS8XId6EMRnvGE-GXpZZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=VoqyglSOF05PK4suoOazfBCvSpGhNT13JCEwamaQqK_UensDystsggtWKT_A9q1G5YgsQZ_Z2IqZW1zwlF_XZHQhZPtAjB5Wa1anb7d-d4zerMGjmkwheTXO5G6JfD3Snrd_6x30HhzYnutRQTq0RQo3QotSHJXwR963QVXqeCtc5NhdxMhAFlqD1A-aLlQox-mmvghEgCFaCZ9GnhzDIAo5IojvjCFnur5Hzw5Ufs1A7rtoRxsi50hy6IXUWAK5Ny3YDXw8-SW-nllD5_7qtjg4zMSJ3e0vf3spcawEThjptxFKocDh-dTmIYTgSUbSgF7vD57GFfFP8sEIpcm4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=VoqyglSOF05PK4suoOazfBCvSpGhNT13JCEwamaQqK_UensDystsggtWKT_A9q1G5YgsQZ_Z2IqZW1zwlF_XZHQhZPtAjB5Wa1anb7d-d4zerMGjmkwheTXO5G6JfD3Snrd_6x30HhzYnutRQTq0RQo3QotSHJXwR963QVXqeCtc5NhdxMhAFlqD1A-aLlQox-mmvghEgCFaCZ9GnhzDIAo5IojvjCFnur5Hzw5Ufs1A7rtoRxsi50hy6IXUWAK5Ny3YDXw8-SW-nllD5_7qtjg4zMSJ3e0vf3spcawEThjptxFKocDh-dTmIYTgSUbSgF7vD57GFfFP8sEIpcm4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwI6siNwypN6M1yrAZB836OVQve2k1fJZVs5zqbdVX5qOT32EJQU5OIDLI1QMyqOlxjMzhijsJ3ZMiVFlYVbjGNaQklnBxsJgdA222CNAg6pu8-WPHfIAhIJ4MAizUFst3EkVMb8mpuD-xdHLPgK1F4D4HJKXeIC4k9VKhX1xc-H-k-XSBt9NUv7f_wbckg6x0SEGJklF2fKTf9u7vcMIT5W6qO4QUwVraMvIQEr_fCvEJfeg5X0-9UgJq_4vKxFlt_AqGpA8WOSVpvNg5Zu_3Im8ODGjvHXIqh2gQJJbqVwyLyMJSolRvKOyA8hGJ71o-lMjfQcehhZLCQt1QFcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbESoTc5BLaLQrk8uufxGMp3BDJTaKtYR5cHNHxGGSQuxphMktn2hvbC1T78158PSGzxKxk-AlMSODftJHODgjMNPb7Jn_1XcFqUnWhubz_d1zXj7f5H7H1ZlOETEXXV9BCn08VLQG1dPJ1-TnbnOBFUq9XrNJ4Bd6h3EaU98xIijoSEZfTgmKDiV_b_TfajNpuSODyh75I5eXQYkkm3v61f-G_ho7JJOcjxEAtCHKcy7QncttTMXTaN3E_BiC6JXK-6yXmzZmyXMRnLMAaT9OasDyrOok1HeQWhS3A_ik57yDkXST0c5hC2wyY7toixBbzJ0xJv4RqwSOlpXSyC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BO-AM3Ji4jpeEAKfPPn0lVGoVH4JDOpAYF6lGXaKo_GmZw1WnGzlJqe9_wh3ksQhbObtqpj8qm0ihkbDPAtb-ADXUiR9NcVQl6Wi5JdbW2lVv7jCPR9u0Z_fUfV-N_e9Wxac-a05qehFFaDnP7Osey-6P_rWZVgBDYBMXormSiSIWNq_rDzuFL_266MgW724q1sCOf9_Qh7o2RPwDkVPmSUXR7ZN7wZ22eNclUaZ0f9B2-FDrMSISPckhnDIdfZ9nG1u_pW6bot4_7udG6miBBhmo-a0Npu5t7JuugnR-jlx4bb8M6_4SHUJ5G5NkVPkYA5XoM_z8mjXeoiS1v-xsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bg3TISlzm3xJJc0GWq1RZyy7pys5EXt0RDxfc7UoNXpHFgnpNN6sWW3DOVIAzVJy1KZlf7wOjo-G-Cca4YdiVlHxGQ1smXhB4m2bBI7gintppf3bUMV-G7l82xmIOufGbFOdE0LTGQd250QcUYrvLlukDh0HaUozZMiRarmjA3g979L-5JVNEFOxKEM5fq6LU93wVoPNLZstMK5riG6VPsFcEM00MW-njA4rib2wdzmVP_t1J3OomTk2aQxMGdeBnJq3XBVOzPKoXuHoCFLVftLOT87JzJTNCW23z-NfvPQ9DaCrZIPV3bDCo3pj_YoHpFPFSAe9rMTm_Dvnshe-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JeeoX9GpWQrOEPNDPOBVjZUgM6mV2PlzNrViep0qAn50OtdFlsbuCZdO6IndePXkp7ZP98H2CBDkBH-f-4rPRtGi068a1uUyrNKxLYHRq4qCKtQzhcaDmmuUbS89YaifhIyEpR6ulRkcSBe3gOn9WeN8Q_t7RqQBeFgOQuEngcoLoBW26TaSFd_tadSfxIwaP_8iSwzZCeLq5GDOnrPPX2-BTbzEP_H1AAq6PLe-9bJlhIslda8H0bi-GIvLloyiWtRg1XRsruRoW-Qmy5JWYnfYjHJa5nHlhjMDII874VLz3NpQ-2rnFnbC5M6N5kaAJMqF6NhU9Fe6BIHs7yL6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SSlBoNk61S_ds3IdgMKXY-_sYjPDGtGvWa6loxn51C0aWfCKkriJuICS8R7Qhme4l-xFOK2CDOYmx_szuOlhnJd-59syQp2QaOozLlzT4Z_tA0q_wXKh50gN3Q8xJ1loxLnVegsyAOSUCli0jvFtHPvkGvgxXMF7J21y5T-rkQHWqBZ79HcBoiu-gs3PeX7jTcYWXE8KYh1-rwpDoROULzqjmmimXgPQd-7WFupnCsi9iCwk_c0qlR-NDWHyX_7TofhPeJ0Uab-GByWnuGluE6otlfSuoysyJFeQfdi0SfD1MYv__liOJ7KxNpchITod9_rXbLHJPnkZDEfTpDfEog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2RlMtJgsveNEbo5YI0209ij2b13ui8IYlvxGw_9skYWmYlkjFjfYzEDuJx7eM_uv6qU0ISIC1P20tbJgnO3cezztfO_NUAdXcSoiXE73cjJ31Udv-r7l5QCYmeo-m3P3OFo2c7ycqXVkQzrn_cPBVBm-YfryeJ06b_W8C7Qbwi4d9b_Ln_WKsKuMM9xfyuWnT9fo7jBbIGve-dRGe9DOg33Nzb5qoBbYaadId9TIwqaWua3ZIxJMaORL-sJm5HnvnRlEpVzR1mr5fQzjhkprDPT7kXFjckSiB3SjC05T8moQJRVeIGmpsLkQTwidVFtvjf4i78EKhjBPErCq4pZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2AdyUwpK2xbTMmkm3zulpeyieWZYH47Dy77VBybAGqMh6hP2g8rJ6myoiFTqeSelp51U4CO54ky8nVrkWAL-zO10C2Z3cPWaCZKBlzaNasXyl9kc33SKdS2QZdRbdfBIeA85Nliyei2M-u_WZpxqeB5y4aTWldFZcNAxotgfmJI0als_GAQNkgaKICFsiNiWJ5wCsvrLTUVTDs1SW8P8MxommSZmoiZYVJ8NhBggT2G0bUtLfp_C2vfNWRk1M14pKrtES20UQX6eBJTuP7y3u6BxNVuB5bkgryG7WVRvCxpgYUDrMEfHtElw1lI2w6rnZnUTHktueCEBvAdK64P1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tub6Ek3oE9ZozJvu2mr3Wcm1LquhnEOVfS5PfHXuxiAhgPAi7ehydBJbYFg1VuIM4NVSZwX13PveE1hGKhZrLwPh1TI3jDJwgLwJoBbYXowvypx8VSzcI6oGXWNRmVXtGuMSYREOdRIdb5MenqV8D7CMHde7AoUBodAHJ5-ItWih3QUogZcfwSptGLC-Ms4W73GS_x3isGL8neGwcHyNba1h9aY2_tvOmIp29P3APk9GKS6kvKFMub_ZYjwMUPigtIiGLyYplf3aIDx-ALj0mYUH1LppH10Hv0GDdXg4ZJu7ueqplxUm9v5NHDMZ3bEm_h52B00RXQaU-EsFw03Xig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEoWiRpAbtK5XzudnF3H9msRfnxTIZ-gVJG0gjQ-GJbbGyxjE9_kCLr7IhUiDsEYttDhmIeIbuTbIvrDXSBL6uY_75eOVmeYWi0ZthXp8wLfRmXZ8dHR-qIe-wZNVrc8uXEsyMo7hoyzXY41wWIXIC0FofysydIQOcBzonu18o64Ck29DEQ89IYk9adIc4MZNkBZeaYM7PpVArq39EoySIRCEJMi47ouLaBhDUTYVzN1Qgkkxc2_0XPFqnyzFJtccsjV7AY7ozzEOoKLHdO1PfLlICGcI381LQRQyTBJH8nQQi_60AYh2JmLYtsWGerHfIkIRD88KoFQ5weiN3pAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur8RXybTQwWcHIejX76QwgLrE0wmDnSXXMkv_U_cMxqflWnSiMM8ysaPIKtoq_J-L2ofpBxbakUUCBhMGKbushpCPnUt4A4pagG0xHrMRfkUvngjqoaRKRm2w6DfrjJ8F5aGPJnFuR15HZrJedyMyHl2XjPE-PWpvNbDYewo_pgjn_EHI0UJa9hbDYwzEIVKldTauIvQb294AJon_ehI_x3vvl5Ihmx1j7wkLJeQp46y_BFFGL1yEcVsKFXpyzrgvDobx2Yp940wop-XtGx2tV7pj7QF4XLk_Gk_JPzr4o6Kn-oOW44W4oCxjwBkFxXF21lbxaD-cm-DtvQv7z736A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2AhBvYNrlRaP90xut-IhNevm6MXGctYT4hyhi8pcyZXzGbJSPrIRQUx4h8vSMnFelAAmZs5l5noRSfG1xhSfJvMUnxkn1rkrJa_foeUr80NPEhUjzHJHQ0SM6KxDsz9cOzIZaU9a4Y2Ll8CjVUqCVAA72IcTU1PmrFLuHDRK_6aJholrtHxWhjDAB4Cx13xQSSQvmgQjXTfTNa6Tc5I0laG--eTZ0SHqSE1emabrYnZw5AfSO1dK6fc8KVoGDzNeDZDcbbI0I0U9qBOTuUGtdAakYNnoZFyg1XvLv3krVHpPlw3Uuj0rI_6Cm2u6gKvg138bOyG657Tj_1tfYNQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KibVG5Bu49lKNu3tASar-Q-jHb60jrvvzw0Vebl7Z7AqYaU9V9rulpFflSbmW35JPhipxBM4PnJwHN61poTlCWtStOIXMs8v_tAKEYOHDLyJS8D0jdN0oqdO2cx-IODaAlrJKr7Ro422dY5fL4o-U_YKUrUx-OQFub21JVJlF4jtmnoQqXLM35w-kitwSuhjjEitP0mUMK0J7A7g7h-VEJwyI4L2laohuXQ0F_He7cBa1Z8287bm0SyPilg5nXTKQZEFhxgTFg05J6tZClBRnHIeVPn-gytu888Gda_GKLaNKXXzI9M3PwRjanALmAXgTY4GZ3jdvc5Yz6EPCzq-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvB2DsgVBZr6Qgdoi3nvBh1T0L6n_knXtB4e_EU8Ub-mQTcR3kD2sKHB3q6tFeTDMYEJSfj2toqo5ec4Nq4D3sCBmuBg5UfxOxVkzl14McvnLjoGF8uDmoG_uQK5gIYqw4UQMCcjxWc7xaoS_5SVxnwa7LRX4aQMe_9HdXyqo416FxON14d9ecUiOPpOlAnL6H7od8QBGSh9-EmlCLKyWB8tiobxU_Qf3ObPYKy4PthDJU49TsihbThohYkgY1jkSMxhWhP0MUggxyPBVFPWsH7C3ev13zfT-wKEDZTWUT7lT_pu74XjirBoYZunCMgLYUZwMqJOiq8Z4HZvWmMgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puYdXHSKiBJSsgdMQFDFlHWDX2ifW86BRA64BSVUjGP2pRRIJGiMKONghIoDdOzu5Yqj4_VNLz-TKvi-vaVj8Gec_5QZ2sGyT4FycSyP2mqQITX4Nd1pPcka8LHIGy-fYJiPdsCyPqbPfJ2NZME1n_ilGUdjdDOSi-MKZKYyF4WfA3Mmyy03Xr7XZqrhFOWr1NXx8QFoJ7srlw5YhYmS7GgGyxcGpgod00djmkwjmmCX4Tj_GMxr3YY_Ck0sQv9kqySQ1nm65oh03JFVeDS_9LEF0XFYuH7dDgH7WTbQrPU9pZXb41-Nt36XweMqZaGafdDd4hXfze7xe85D6T66Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK5rU-MYlx3ey6_5EUX2XjGKtJCYhW2I9d2ZbU65zxit5CMvHn47cwR7GUzGzPRJqYO6FnQPzIjE6fxk2bmD7gdELe30PXbIXxGgNamzwmXLdpt_SsLueV3Q6LTONB4nRfi2OaHbJuUw0rH_TKrLunO0gTRB3vxAhl3q4yMt0dTv14EVb3xM8v5_J60xKrJX25be1neCecX03eNWfnMs5Pk17_orKLu0iWY-H3KTejW2GCUJofEfgPbRuc4ozB-cLMUAp4pOYHZSGsJWxL0bQwOeqwva6OXIspUf4Z_Uti1h7hZrda-NzL5UzBctXWuAakbUGxeoH4AvzZohSxiBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=E7C7RwP7oVRWIXKc032HKuHmT1pMQzJ80lksSJMSXwEzkiUS4tIUsOaVfBsxnh3UhFCDs4CK_IYAW_SftskM8rQyxN4bx-1UF9DqlL4yVJNibH4VHM3_obnh3IetwHrGf955tQ390cKbgv-wUrTLuZSwcRVhB2fnsgfYDkth8z7hb-pp8oIqTtmzv3f98CJODT1iis4iKfu1NLCEieVsg4g0UHSPIulxFZxhhwVuvmQXqs6qDRgl-K1oySOD7Ugzr9J_QxWG26kBwwMAv2aTjqOUYOdsJtmgnrHi7EekQOAtkvLGDWmGMaqpUYqwh-WnHm7y9SnpVAbccVsgv8yQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=E7C7RwP7oVRWIXKc032HKuHmT1pMQzJ80lksSJMSXwEzkiUS4tIUsOaVfBsxnh3UhFCDs4CK_IYAW_SftskM8rQyxN4bx-1UF9DqlL4yVJNibH4VHM3_obnh3IetwHrGf955tQ390cKbgv-wUrTLuZSwcRVhB2fnsgfYDkth8z7hb-pp8oIqTtmzv3f98CJODT1iis4iKfu1NLCEieVsg4g0UHSPIulxFZxhhwVuvmQXqs6qDRgl-K1oySOD7Ugzr9J_QxWG26kBwwMAv2aTjqOUYOdsJtmgnrHi7EekQOAtkvLGDWmGMaqpUYqwh-WnHm7y9SnpVAbccVsgv8yQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjovneQT2tCok4izB4466PYs7VPfAiZXiH05vXunIvJpqT8orInJfDosU2eazSszm5GxzN1bhTBFPBu-_UqNMmDCwsmfgFg-Sdu3b4pnJueAEyy2DL8v9bOu-cyHZMFoc5m10QxNHNT5JE5-7i4C7snGRQRNVppdzngmi_RGQ8aECici-UEUqm4dx1537R5x8LweV9sRY9qhmTCUfrjJK0-tSpzyHf5VPxT8RgtgxBHTSFdvi1rfyhrDJlPqymnvQlbOxD2QEJkI2qw3-N9R2rF4YDrWIkavLzvMdtBfpU7Caykl6MOzJ36Wj9rHFZyXvjOn5qnWS15UU40kKX4LBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=m_RGTcC0i0chjDroC07J_ds8ttjWi6i-271QvDuNe1M5fogaPuM9Q4YSsZ0okkcZ1gWidoynrIx52pL6G4SpVctQhgplZ5pVUFzUj2yuHWGeaksCkiPkhG1Hbt_TGzLfKnztSIDyg86TnizLFxqL9wEnKA465n57w-kauijlP8WSFHC6uv3y8rwlBwu8m6DZL9iuwBrvYd15cCGK-VkXeEAiq87UnzM-SnTTWgbq4gpYdaEjKjogxKRxySpS7g9IzzYVs-3O_s7NplwWNUIyakox5usKGS9_hploTQMaVIalIDMg2T7zDCqRa7ptOvDxaEhwN9hXUo4rmUrBYd8siw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=m_RGTcC0i0chjDroC07J_ds8ttjWi6i-271QvDuNe1M5fogaPuM9Q4YSsZ0okkcZ1gWidoynrIx52pL6G4SpVctQhgplZ5pVUFzUj2yuHWGeaksCkiPkhG1Hbt_TGzLfKnztSIDyg86TnizLFxqL9wEnKA465n57w-kauijlP8WSFHC6uv3y8rwlBwu8m6DZL9iuwBrvYd15cCGK-VkXeEAiq87UnzM-SnTTWgbq4gpYdaEjKjogxKRxySpS7g9IzzYVs-3O_s7NplwWNUIyakox5usKGS9_hploTQMaVIalIDMg2T7zDCqRa7ptOvDxaEhwN9hXUo4rmUrBYd8siw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=n7qHajmc7P0C51hOKXi9ne4Uh87LIBXHPlYwCH7kYK7wby_NpJSZqfgCmlXZbd_FylVahKJJXNJTs2Dxl6SQTUk-CQwJehCo6DeEziT8rsMkfW7iTe1Oa813z_Dhxv0qM1BpLHa573IC0a1L9mpUBdZyLD8i151OYKhNe3E0H7LpKJs5GCv5O3maWHRgoHrdghfnjVQ4BKrZLoUbHM6_NsHelFSHLm4BXT1poWkAOyBTXh9T6u_yb9S6WTfYHIXue5vkjtOgYO1CVtqiN3xR8JCygxrAghPu4N2aMijBpWoqyj4lJ0_-5R2RNUd6GATvJiJz5t3mqs38LK9ssEgnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=n7qHajmc7P0C51hOKXi9ne4Uh87LIBXHPlYwCH7kYK7wby_NpJSZqfgCmlXZbd_FylVahKJJXNJTs2Dxl6SQTUk-CQwJehCo6DeEziT8rsMkfW7iTe1Oa813z_Dhxv0qM1BpLHa573IC0a1L9mpUBdZyLD8i151OYKhNe3E0H7LpKJs5GCv5O3maWHRgoHrdghfnjVQ4BKrZLoUbHM6_NsHelFSHLm4BXT1poWkAOyBTXh9T6u_yb9S6WTfYHIXue5vkjtOgYO1CVtqiN3xR8JCygxrAghPu4N2aMijBpWoqyj4lJ0_-5R2RNUd6GATvJiJz5t3mqs38LK9ssEgnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=g6qTLCjPOPe2Pa_eFu6TBDiZTZD_wq3npawBGo-oM6bGCHmNvKaSMqZMulwr568t9v0TX-UUCpxIPZOtmu37wx4wuADnw-LXEUUZhfwIlnSlfubB_i8KH5CwEbU47R7ucl1xHrlYO2U_MBi6x7z2SS_Wws1aFQXlX-rNV6Ls2L8sQuuIs8pUPBXov8ZdVIlNGa3Hmy_uLbQbtatgxKq_25XIWwvdvs9_Vxh_RPj1quPD5vdzmeSqXH_MPiDtih03Q0mjcSbz6Zbt9y39qxsH-v7uJw388liMHvSGEPnOKCJC8Y-HZDMAI2a_1K6gd9JeONFFXCHa7RKaIVhbwGU_8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=g6qTLCjPOPe2Pa_eFu6TBDiZTZD_wq3npawBGo-oM6bGCHmNvKaSMqZMulwr568t9v0TX-UUCpxIPZOtmu37wx4wuADnw-LXEUUZhfwIlnSlfubB_i8KH5CwEbU47R7ucl1xHrlYO2U_MBi6x7z2SS_Wws1aFQXlX-rNV6Ls2L8sQuuIs8pUPBXov8ZdVIlNGa3Hmy_uLbQbtatgxKq_25XIWwvdvs9_Vxh_RPj1quPD5vdzmeSqXH_MPiDtih03Q0mjcSbz6Zbt9y39qxsH-v7uJw388liMHvSGEPnOKCJC8Y-HZDMAI2a_1K6gd9JeONFFXCHa7RKaIVhbwGU_8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=frTLg12AVsxxywJYwbzPqH3z7e4laEm2EpW6n-AYu9FLkbKZsAIaj6qwunp3rSX6_3seZXgxcqupmbMqY27STrTIcmXwgdU77RCxjviF7wuqgS-f0ZGERZ0eLSh1mg3uieElkjCcZHCX3SJyH3ih6FfBI8xiwQgWKHyBXVAOdjBRTIXt7h_1qp3HBJsf573YHDdLM-h0FofApYaS2Zq1z-8RT2kIthfxaypR4EMxHt_JcNRhpWWyEuQ6lWyS0hiyP6Rc2lrzCUCJ6Idv-PiWbozI3w_rhay9bDBc9BjjK04bPOr9Ulm9gl6cc_SDWip2btPSegm4Ljr5IH4zOEUS_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=frTLg12AVsxxywJYwbzPqH3z7e4laEm2EpW6n-AYu9FLkbKZsAIaj6qwunp3rSX6_3seZXgxcqupmbMqY27STrTIcmXwgdU77RCxjviF7wuqgS-f0ZGERZ0eLSh1mg3uieElkjCcZHCX3SJyH3ih6FfBI8xiwQgWKHyBXVAOdjBRTIXt7h_1qp3HBJsf573YHDdLM-h0FofApYaS2Zq1z-8RT2kIthfxaypR4EMxHt_JcNRhpWWyEuQ6lWyS0hiyP6Rc2lrzCUCJ6Idv-PiWbozI3w_rhay9bDBc9BjjK04bPOr9Ulm9gl6cc_SDWip2btPSegm4Ljr5IH4zOEUS_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn2TglRb4t4_1jpHl76XPg6bWnva7KTDSi6kii24YfTPsbhAORMfj5KLgGpUSE3R8yY4jjNcZVn3KxpyLWtPVzKYmkxkkoTK803k85gjgEoih2NbtXOV1XOKD33QXbApIPOAtusnBtb2Gsa4I-itxYirBaOG_0fN1eSIbYW4hVxN0O7kp-ZFJms268owXdkcjYDI8Tcc7Jsy71GNaLFMFnHld8WRKGHrK4DTnJDQ_ARlx_WwDbkmRoPHxrYtZvg9TVZiw3x9Qe-MGc9TskqTBn4MPI17qXxyi93qntvF_XHAeGUiLf5WJVyuy5TudcOJcWTn8bqvSTlw-NWyxZ0JZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6ESk96AGblGfPN6XB4EGwv_XYl3LgDWRXPN2d94MnrAo8tldF2MCbKjIk4zKmq1pdCjpMGrYB2LtAr3q91RGUyuvAApFjSS0-bx9m-RDBo5G_ZeZSx2mISX2ruHTGdo2zRMADweEY0CaYtKya851g_H_bwMf-AGmdm6EzA2b3ZGHdUM4Ko4H41cvv90P2u6FCk7dczLCYRcgdk-iVznDoqMUYXsDiTmbV6kef_eKwpzpQK3kYRfVs2RVSUC7F_YmABGwLDh_pOXJHPmEFyuNrveTlTNk2nYTMT038qE2vPewNXb6KUIcDkVEduLxv0TN041MeYWBM2xYyoSSEZPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmtRtTtbhUhTao2Y1NH3sGahb-809fB19rGe00EOoThwnOxohpJ2ujvbavBVfi8O094iqJsdzws2EDkLPf5UKYeZhkxAOHIV2dvmnWoBMBkgmH3L8x9z238G8OoxzIRPI0-0NHiJD7xvlHUPqBzD99hbGyfICSHc9PxRIGJ0pC8c0PLiR9LhEs45A3rKlu0ka56O5sxFQ1-1dg35Yie_ha1Wi1jnPDPGkLaZVOoqcq-LbXHWOYLF_32EGT0nxzodh4vRPm1kMOMGFVvAvUDSuKBwyMQ_8xXDH4SX5vpr-bRUfVMznJNeEVm7Khd_ERYTXaDCgnbpLvswsG6oqQZbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=o4WMLdvMARxDhkKNCJ1nLKU6PZ3fMN2RA86EhaE68XRbcPqtC_fTFwWCLn7rI4yC9OaLEt9bI2zCwRWysUvxCau1XduhzdybXbet4ub-TP-blRzTQO7ka4BUdfeAhmVnavFCwKMLthVf3AmPA5h2sjOa46t_zyMA2eQdDPnbqn08mq88Ljlyte6yTtRkDI4ylxYVb9gIODUe69FlgXmCKbRp63wB4GmksaiArvK4YM0lSw8FRmvQ-MafHIgL0rkQjP1Pvo_8Q3lx4wBTi_bUegleiHeitrmQ2H59yLn0zSqrtEx2Ta1qsHbxGHWp_r_kaNMA-06AaxAOZxXXy3zdbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=o4WMLdvMARxDhkKNCJ1nLKU6PZ3fMN2RA86EhaE68XRbcPqtC_fTFwWCLn7rI4yC9OaLEt9bI2zCwRWysUvxCau1XduhzdybXbet4ub-TP-blRzTQO7ka4BUdfeAhmVnavFCwKMLthVf3AmPA5h2sjOa46t_zyMA2eQdDPnbqn08mq88Ljlyte6yTtRkDI4ylxYVb9gIODUe69FlgXmCKbRp63wB4GmksaiArvK4YM0lSw8FRmvQ-MafHIgL0rkQjP1Pvo_8Q3lx4wBTi_bUegleiHeitrmQ2H59yLn0zSqrtEx2Ta1qsHbxGHWp_r_kaNMA-06AaxAOZxXXy3zdbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTp_8QZ34w2QfFdS8b5uLhNUqS2YKHUr4EVGj_V6Erzte0FP2gNccaOR-6t7kCRTW4ni0EofZGjbF9HPVHO9PGaPoPVedUXR7ZHD613gmk9Msb_Fdot-Yu5v-KQe4Ee-iYxJhEhqqRFbD6lbpxrK_2WNkCvisPAdRg9gGMlzYvwQHFk5_1hg9HJH3Ilwv35gha6d6IFDvKB8z2oAWvXoKCtebMpZknQnoBFMSjCoCmsV18z1HyvMIX-SW_ZS7u5C3_kmsmrTNydAUiEsEqbrQhbqUIeKQr8ZxUemcDTokcOiH0caSpf-V5TYNO_lQChUCOm6u_npe8fYq3oNjTzPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-ygPteajGEcRXb8wSFY925MK6upbsgQyPAWpjuwmI0yL_RxZ9CbFvqtsaGwIJcHYxMLDqvpklqwqrTJA4eU3LNtbwYzDDv9_RNSbuwzMhguApI_hIEimDH27bL-wFD66HZVqbR-Mum9Arv9sThXCvk1Q26f86tK8PE7NwgbQS2V0hJAcQoU5Qdh8X_FXVyUSVGNhyIH9JRUXnQJl4qYjOVzCES2OYR5E-imivZ8NxkvGpHRYOtXoasgOYTwn6igxjvzwN0ka5YqI2NhTNAM6CJ6JQ_iheJB2Z9jPGJCNYPjWtfsv0Xmm43pWcpuVNmdAqO6EnwdYQREiUTZgw17uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXadV6s7n8q-oPF6HyA4k9XuB6dl3IQ9qNP5HO5OMKLZPi-ZhOCcdr4DP6qluAdpxWxbnpwKoo8yTOH_WsYe31KpLRCzwdJprIzEP_x8_amHM2DUAQEcjTYhJkFcqGiHd1XDbBoNWzZsUYxHXE8Cp6DhA_QcltSDbiK8dAr8ozFluWR0Q-lDBPQsuYBhRVnlzErCPQT4Uq01acgdO59mJpBByUA3Y0I8TznweQ7VHLj4fjv-Uv7AhLphKIKMYBVhiZqWsGvTJDVyVJCSKhXx7KodiYxVjhrz5sSyJJMLZrFrE26GKbLa49wCIQ5fxU8Fesb91h3vqpjE0lSWgcwWyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=OK6PB86T8nq1VbZeGlmfuG13mq3Dq_9o2bmLyGLSfnQcFbLIbH8GLzphQ24jLygNKiezQ1t9sZEuWWtt2RzU7_TMXPWtOAcUfxGT3LFpkmBaf3yNBGbibBStbwLNvM7-tJNsU1W34RM4Ul-OMYOwmwVObILcnb8poLtTTXVnD7dzY4dBb3DU7l06dZ30bCKQA13yG-Wm69_KXs4juL9KnnYEH7QqBUyRZN8JxxREmzVfphsGrj9AgyH0ikEGzYr3e2bdIATCHrGK9v6m4gNL6bFl9-UNj05NaWw4BFG2wUVVrbEmPVVv8KAf33urfOeGgFRc2EGi8AFMoNnER7EC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=OK6PB86T8nq1VbZeGlmfuG13mq3Dq_9o2bmLyGLSfnQcFbLIbH8GLzphQ24jLygNKiezQ1t9sZEuWWtt2RzU7_TMXPWtOAcUfxGT3LFpkmBaf3yNBGbibBStbwLNvM7-tJNsU1W34RM4Ul-OMYOwmwVObILcnb8poLtTTXVnD7dzY4dBb3DU7l06dZ30bCKQA13yG-Wm69_KXs4juL9KnnYEH7QqBUyRZN8JxxREmzVfphsGrj9AgyH0ikEGzYr3e2bdIATCHrGK9v6m4gNL6bFl9-UNj05NaWw4BFG2wUVVrbEmPVVv8KAf33urfOeGgFRc2EGi8AFMoNnER7EC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghxjtQxoLav_W2p3mLnrPYBeXBjDXdAOUoYalM-NVw73GHWqG4ko-RahWaLj2_GR02o2SkuNmvSxl_lOt4LpFLCHd1vMS06j4B8JQvI6uv6zbgRH9U3QFSq_xLDZ5Rm7CjrH25-_6-B6PaCqFv1xuPYyOJZVQuPXNTJ8k-x0-T0jUbil5KvOg0AkLapoWUIu0vsVEg6skLJF7kiYnbM4oEKBgXV5tqbpFyj9R22YResG_U_Y0VyfbE7AkUpKaN9aYaj0TnlNB1S6MrSjbcbDEcnXCH6rI7u69TrflMEbcCe0-qSd8PYo0i9o33FNOImi7Ou3cCN5jVNouhz3u9-w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=mxAy87iseDhRyrIr2dqSkZT7SxF1AvkidI9knQ330Aj1V_anZ9JufjIu3yHQ8BBHYJPZjVJnRWauDd2ZLWv-Hr4aasNV-mXv12uiYxS7BBDydHNUypKomQDRD_aFB1bBxz7Xi598m8P0JWYmyGPk3nNBiMLgj5wOW0wbuno5QpB1e0pjCTc-KM02HgzbX05mDZEhloVpDtZQsUTshTx-bTjxagbYTwDu6W-gRddzAtlmm2pDF53KbfFB_H4edoYuRVKIUgRySNO50F3zIVwyYXEw4U--j8yR1CnunETMYAa6Kzp4pJt09OJtT1flXG4JjNImXHN8FTfMwUUl89QoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=mxAy87iseDhRyrIr2dqSkZT7SxF1AvkidI9knQ330Aj1V_anZ9JufjIu3yHQ8BBHYJPZjVJnRWauDd2ZLWv-Hr4aasNV-mXv12uiYxS7BBDydHNUypKomQDRD_aFB1bBxz7Xi598m8P0JWYmyGPk3nNBiMLgj5wOW0wbuno5QpB1e0pjCTc-KM02HgzbX05mDZEhloVpDtZQsUTshTx-bTjxagbYTwDu6W-gRddzAtlmm2pDF53KbfFB_H4edoYuRVKIUgRySNO50F3zIVwyYXEw4U--j8yR1CnunETMYAa6Kzp4pJt09OJtT1flXG4JjNImXHN8FTfMwUUl89QoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApNCezZ0QU71SHMEnwxWW7j_9x2Cv9PAp-AqDH6xDxo-rItwBQ4OK-hHiQLfBj916gOf8te9o5JjTBXL8uPdPPRJsvnvs0V9UFg6GFVCAbNB0NXRNec1qCp6m-_XcZHrVrDKP3_zhD1F9lIT53Yj5B-qpQ0rQkqOBL0UXkgGzCrcoulTeu-gSnxnJ3hvF0af61H7e3rXziBy0F1X3i4egawaSGCOMvJ8Ruyq07YJJfVYUxgjT5vPmH54_kiBeehoxycQrjOK9P1T1w1YpDdFyV9P2NY_xgeMiazR4HjJHcCjeQgDkjhvAPEv35pYvln1w7SwTKPFeytznTaIhWaSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
