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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 14:00:23</div>
<hr>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پاتریک پویان، مدیرعامل توتال‌انرژیز، اعلام کرد تولیدکنندگان نفت خاورمیانه به‌دنبال فروش نفت خام ذخیره‌شده در جریان درگیری‌های خلیج فارس هستند؛ با این حال نگرانی‌های حمل‌ونقل همچنان بر موجودی بنزین و گازوئیل فشار وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/131729" target="_blank">📅 13:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مهران رجبی : حسرتی که پس از دیدار با رهبر به دلم ماند این بود که نتوانستم پایش را ببوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/131728" target="_blank">📅 13:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی : تاکنون هیچ حادثه‌ای در مراسم وداع گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/131727" target="_blank">📅 13:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKxfyIFFweOqd4_2kOR4iB-DiRacTStObbx6_RJlJPkmeluyLOfo3D4wPVd2LyKDIVCvo1YVcSksQp1e28YYGGpI5F_K42DW9OogpmrLx3VbCsegTQejuBtDxN5mc1Eu6pKIt2WDEwqWjP0Xs7a-CFRWr8Nc5XMmbHaMeCWHCy-9Q4cElFhv_tuD9FFS79h1KN0HLA73Cx3_fNDrcQGe3OkHdydY_5NlMqEqlvLI4GCNTn9zXlTU9Yb4MhelFSQ533Wl8kl_08aUZDfKdQt-W3H-iq2pbYdHay2Oj7rVu_b0fHwT9Q4Lr18RMlihUlgLxLUXTzI55OZqTw8ELadJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز روز استقلال کشور ایالات متحده آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131726" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X53spOYrWcvT-hXyOHbqrrj0hYCg46jWg4kzSisaCwb9XSRITItUYISiuDRgnvmO5EVa91qhpvnixGQ45wLAP1HRevPPgWXuYect7vcgaIsp-B_gkNp2STUczZoQOZx9igGHUUEt3IPfBfyRicpI-GqXSiINIEkKW8EVv8btBRSBrXjXjEzU0nzLY4Rm9OeCnGqHMM9zl6QMWSGPJk4xa8JFqBSw0bwGFH9aMIzHeDbd3Pyob80ZEC6JByDEm2SpvAzSvLQlbFa2o8CfJDcg9QAtcQU4n2GUDw9aTJ_IYpmRgxwJPFpq3mnNGDU0AUcRf7I0VKWaY60YUxYb-D09LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب/برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131725" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
میشل عون در پیامی به ترامپ : از شما می‌خواهیم که همچنان در کنار آرمان‌های عادلانه لبنان و نهادهای آن بایستید تا بتوانیم فصل جدیدی از امید و صلح را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/131724" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ:هیچ کشوری به اندازه ایالات متحده آمریکا، خیر بیشتری برای این دنیا انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/131723" target="_blank">📅 12:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آلمان انتقاد ترامپ درباره صرف هزینه‌های نظامی کم در ناتو را رد کرد
🔴
فریدریش مرتس صدراعظم آلمان، انتقادات تند دونالد ترامپ رئیس‌جمهور آمریکا، در مورد کمک‌های ناچیز آلمان به ناتو را رد کرد.
🔴
وی پس از دیدار با سران کشورهای حوزه بالتیک در برلین گفت: آلمان در حال حاضر بودجه دفاعی خود را ظرف چهار سال دو برابر می‌کند. این بزرگترین تلاشی است که ما تاکنون برای تقویت قابلیت‌های دفاعی خود انجام داده‌ایم. بنابراین، چیزی برای پنهان کردن از کسی نداریم.
🔴
وی افزود که این موضوع را با کمال فروتنی در اجلاس آنکارا در روزهای ۷ و ۸ ژوئیه ابراز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131722" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwBkcSMna5liEHzgr9WEQEzDrshmo7gbX1jOPPsHMT1JU2hi-6xYj9ZhZ9GGQZK-9lZyPtACJC34H9ZqbcNny0FGEhsZ3VJYbRjJAzW3HuLXuS4oHfXF5Z9kF4enS63j9Cwfg0XvQecxrXW75FKEYXe9EHmRtUhOsMzzInfh6wFt92U1edkzvY3RCdOxxaRvlBCmDPcuRdaFyc31BddX2zldAWQmOln2R82d21KoYNH17d2gmAK2pagujB2W_V2Prru7eMlNgMF8L1052chd_bCTXnr63J0SNsKtDR0ftaK-YBoouB7YaYILXh2qtPmLV30q4St2go0ayG4SsSKBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atoXGr6uLVOpZhb8laFE-2q8HVdVhYlpduKNsUuFbBBTaouNHx_t-MUK8CUl9KR7MbJ80spXKhx6SN62HLUYt15Fp9EIKWIsv0M8W5qNo9DOYpqxRYz-faLjofysBm4nGk-VRFDsveEcZz1992-FC5y0cQqr_gT-M9tw0c49JLhb50Xiz8VH1V38EWLrmz3CB68UXcF23vKfpG-WwKn-zNR8G3CsDFZ5PfkbbhUOykFvdgbw2Rftwz1m9MEsZG-XMS5iOcf6UGloZ7estZHUW4jLg3DDom8DylGIVdnZYEMSleaxMsiFOwtc4Y5eOHHl0KNF472qSOYCHdAirEEkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKNRmP0t8OVvun3qCgjwCrvD-TjERSvm9e6YNhl2yUtNiaqcwiZ5jja-IGtUZEAp3Tw6I87AJzFSEAs1eoEMhwWs9Uqr8pLCjvzLmayl6udGPyWmuYGjaXR65uPoRcP_SToZJahfUE-EmqHJWgYEe7Od8WxyXodWFJilkuqJO8w4uIRJGT-_vt_ObGs_8iL2FVF_b4VqyizE81G6nGM8C70DGAJg5_tj3vIfSGca4Kt2QwCPJD1FTJxFNPU2vo1CuWRPpROW2DC54YD4PfMI9NSl-0J46v8EYpdOTvclTeFaFJ8Zokb3ClZBPV1a_ilKKjkLox91hxnCXcsb22FldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vx14sjFM1WKGp8WklFCPaO8o7hyLDhUucxzJfzEgEpN9wsXfDhkOcT5AlukvIY9gXWbqSKjpEBtnnSpDfdlrYIWmFmk5c0GYA4jUgAulKxfuaJcjcepBPTGpCNdmvJBcMAC441Okqk2DGQ_XpgNDZQPK0esCYqpRFXlbxxvB6AI36x178XzurcAI1AU2Bi1oCw7Z8LFLBzzmT6wFoSZUe4X17r7WH8gI5i6Hk8trR8xOgqku1G1G_Y4lW5QrvdsuZWQB-B0C8OTSSCkZp0DeD5TptrMG1fI1lx6F0sl3vodYR3jPCdN-YlCENJXIbVTHS1mqrR_hLInQ1q8wgzvjmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به‌روزرسانی (تنگه هرمز): چندین کشتی به‌طور ناگهانی در حال تغییر مسیر از کریدور عمانیِ تحت کنترل آمریکا به کریدور تعیین‌شده از سوی ایران هستند، یا حتی دور زده و بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131718" target="_blank">📅 12:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
منابع لبنانی از حملهٔ پهپادی اسرائیل به اطراف شهرک «صدیقین» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131717" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: به سایت‌های هسته‌ای ایران باید دسترسی داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131716" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
زلنسکی: زیرساخت‌های نفتی روسیه در نزدیکی سن‌پترزبورگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/131715" target="_blank">📅 12:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBTCkqxe4fNo3oh3E_ef9G_8bfEcb064zEhIiHVEqqEezSLRV2vk3_74um5YSV0xQsxgJMb9VsV6VJZzw3mPAsnmD_HZlAIejhoPIaKkZytXjkFV51qB0kHICShxx1FaVbbY5DIdEox9h46XS3XxKao2n6ULBZG9nBwg-O-PVcGkTSEsgQdGwJad2bDZ-fEyUILW_2Bbaux7ZNN_c6y5OtvRZI3eTma8DQ4ltLnS9MajBWAGbMTVyP_Arm0vIWZS4jChgtjsxjv5wxyk5EurLCOCSN7BxjiGi8k2i7KQIB8i-KjEJeOaf4cBAUZ1gEv7Jezc6MnuXvxl5K5KKsMC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ پهپادی گسترده اوکراینی ها به یک پایانه نفتی در سن پترزبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/131714" target="_blank">📅 12:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تولید نفت اوپک با بازگشایی تنگه هرمز و ازسرگیری صادرات تولیدکنندگان خلیج فارس افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131713" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxDqWPt5m7I3dseT0H7fYgBkIpS6i5kse99uo7uhn3aDtHSfuX_vIzJMtIJ06dzeWnAfPM5JnXWwwEh63FwmuSHY_ZTinKlWoa0N_irmzslh08FuY6WBXREiExIrIRwPd6ice6PofzFkVh2s6vCssZREHObdBp0ngjkALNDFgKpTuD4bRn8RiVuMv6GuY-NqQrVq_jdfJNBiw5NeJf2I5chJ4tUsh6Pc9Q6_Lw74Y0sjKbgVKTAsrysEyqzGWJsq6fXB-xT-PC6r4nDBPmhcLqIazA4nb0DjW6EZZ0eZ9pH2d8id_a1FMCOt6sMKhCK3eRlcqnAGITZG2HUOgXQ9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: به گفته سه نفر که از موضوع مطلع هستند، مجتبی خامنه‌ای در حمله‌ای که منجر به کشته شدن پدرش در آغاز جنگ شد، جراحات شدیدی متحمل شد، از جمله سوختگی در صورت و بدن و زخم‌هایی که نیاز به چندین عمل جراحی روی یکی از پاهایش داشته است.
🔴
انتظار نمی‌رود که او در مراسم تشییع جنازه پدرش شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/131712" target="_blank">📅 11:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRW84rlvx_Xww8fnAOyUubBr55GLXhcggYWijWMxvrgilCO5rB4IklWuFJs1mUQoSk90kZEUdw2AbM-SReNaRzWPrILGmZJ3d88jVBvqPEytLqcA7cEFl-goPIMIm0ecPtgILRNzWPzSigNa-FoNQg9xWCzERfIS3mBwEuXUxUre53vcdGTfAz43gI6kevRVBhXfrR8o5ARvXl7o6bfXuFpbPYw7YO87o-dLfoFghBDKy9l5N0jGfYCWBrJhKDpJXkRxdK7JJCSNwGZZV4JTcGF7MUwGxWuIuCtUMRzlPPzEr8-Zn7VWKb0tqrMsHQD_OZW9jQ0OPDH454SxIv1qYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک
کاربر اسراییلی:همه کشورهایی که در طول جنگ توسط ایران مورد حمله قرار گرفتند، در مراسم شرکت کردند؟
🔴
چه آدم‌های بی‌اراده و بی عرضه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131711" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
محمدباقر قالیباف در دیدار با رئیس پارلمان عراق: درباره مدیریت تنگه هرمز موضوعات مهمی در تفاهم اخیر با آمریکا به امضا رسیده است و بر اساس قوانین بین‌المللی، اداره تنگه هرمز باید میان دو کشور ساحلی ایران و عمان انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131710" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
انفجارهای کنترل شده برای امحای مهمات عمل نکرده، امروز در جنوب اصفهان (ارتفاعات صفه و بهارستان) انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131709" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0S1hKT_xPq7Sp82zVQd0CwynUuRvrxWAz7FhHLzaMsXNuD4GfCI5dGGJTvts5fGWS0cm_Miu2_i03gvE8i7O_9qZUwd4M6ZoiemquTq3_KIQ0fDk3cJHwaWYPTmYrMOrLyR93KrYgC8AdPnTu0_oofT9uLVepzlv9XBlBodS89gubjB-hB9CRP4vnrmFqN5gk_hvylNK5QA0BKdSHM-eMKxpZwC8IqRllIDTAxj-_AuzkXOOdAbUrRwoA1eN1Yuow87XE5jVPJ6m9RC1qMENXW5w7XXv3ZWHiAspcYAM9kDt1dQ2H-mjhfiUKOIRVcKyJZXUpvUW5sl-PPA6ioKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در رویترز از مراسم امروز در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/131708" target="_blank">📅 11:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مدودف: تنگه هرمز اکنون برای ایران به سلاحی تبدیل شده است که از نظر اهمیت دست‌کمی از سلاح‌های هسته‌ای ندارد؛ اما یک «سلاح هسته‌ایِ» دیگر نیز وجود دارد و آن تنگه باب‌المندب است.
🔴
روسیه، ایران، چین و دیگر کشورها می‌توانند درباره ایجاد یک پلتفرم مشترک برای کشورهای تحت تحریم به‌منظور مقابله با محدودیت‌ها و تحریم‌ها گفت‌وگو و رایزنی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131707" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش اوکراین کنترل شهر کوستیانتینیفکا در شرق این کشور توسط روسیه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131706" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131705" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فرانس۲۴: عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند
🔴
از آنجا که‌ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد
🔴
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131704" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIYKnCFsitnicjchj1lmbm0XgEyMIagtr4VU6xuSiil0KzfvpabPK-pYii323d8dTBoLzadd2xO4SKyY8GirwU2Bq0MBTGEp3OEd1rmo1uq7JVjTxORDJq8Nk47qSNaL1_inG5EvIscs2WpLl4br2glGd49kO_u8cljGgsxh9uAfPw1k8krKN5Z_gdXabVlIJy6fF1cePOHPNpYhjre0LBJUwuRXxG8QMTG5ItCyRW_FKK2fvyI2rOAj_MjnHDKPLyelUAhTEXhGyE3ZjwskMwcJLl7RzrWHBY-q3bOTdDmbvZmB08ItWlHBkG2U0qPGSKqnm7s_Ap7l4Lmlk_Y97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت سنگین نیروی هوایی آمریکا در خلیج فارس
🔴
نیروی هوایی آمریکا در حال اسکورت کشتی‌ها در آب‌های عمان و جمع‌آوری اطلاعات درباره جنوب ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/131703" target="_blank">📅 10:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
🔴
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131702" target="_blank">📅 10:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxieX523kjDauR7BsGGOUVHRzQV09HVLzCYDcWIhjIwojRRCR35iLjJHojglfrV6MyxZzlUVF_4lZZotKnTYhH3t0Db1RORinu1R83-5y04re_3EjvLJekTN8TP2CLPQW7EusI6RfFsALoNgiti5fVTVkMabhC7SVVDKP-3Fh_contz3Z26Qkbrn1DWP-SXdmtfgUBTYr60EYh1r6vUskL9MWB1sU8qBbMnImvGUXa0ehVG4KRruLMYLwnrdjciRYPqK7jXYLHLYiwQwtIckX-_VWWuwAx-3dVvASaq9qwIWlYJoYBau_Aelz_63SAwC-gqQGzTJNijw8rvYeo79xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
🔴
معاون وزیر امور خارجه در واکنش به بیانیه مشترک فرانسه و انگلیس: تنگه هرمز میدان نمایش نظامی قدرت‌های فرامنطقه‌ای نیست. ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگه، نسبت به هر حرکت نظامی در این آبراه حساس هشدار می‌دهد.
🔴
امنیت هرمز با دولت‌های ساحلی است؛ بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131701" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گروسی: تاکنون نتوانسته‌ایم به تأسیسات هسته‌ای ایران دسترسی پیدا کنیم؛ این موضوع به مذاکرات جاری میان ایالات متحده و ایران بر سر تفاهم‌نامه گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131700" target="_blank">📅 09:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرنگار الجزیره تأکید کرد که تاکنون هیچ اظهارنظر رسمی از سوی واشنگتن منتشر نشده است، اما رسانه‌های آمریکایی به نقل از منابع آگاه از وجود «تفاهمی موقت» میان ایالات متحده و ایران برای کاهش تنش خبر می‌دهند؛ تفاهمی که امکان ازسرگیری روند مذاکرات را پس از پایان مراسم تشییع رهبر فقید ایران، فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131699" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: دو شناور مین‌روب را به خاورمیانه اعزام کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131698" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJjwxtf7iYr2VbUTILjnG3fW8vbs29wkIjue4tSCMX2zjsNdRGpn4STzJJ3YJF2gstmli72EWTnClQPaSZz7_5GENyqf4PXYZz6o82OoMn-S2nMII8epdLRcLCg1gAgpW_jSgNZNvhGYIi6ry6_r-uvrwJdoJr8KS9ZymU1DXloY0b34tqlmseVIRtf6UVIOiqlsRa3z2TYvi1yWpDuJcXVjVzSwcqdH-NAtTwIZ-8PSiioUQOYkAnNZD35t__OGmEUjEcli066_sJZecP98H9xAtlj3tVKJZfz2d2eLm48n81AXq1tPOe2DnYt_FLlAq8RKSWhL-L22SJDEfOQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی از پهپاد انتحاری دوربرد «SKYWASP» رونمایی کرد
🔴
این پهپاد توسط شرکت SR2Vector توسعه یافته و برد عملیاتی آن حدود ۱,۵۰۰ کیلومتر (۹۳۲ مایل) اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131697" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131696">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فرانسه و بریتانیا آمادگی خود را برای استقرار یک نیروی چندملیتی به بهانه حمایت از آزادی دریانوردی در تنگه هرمز و تضمین عبور ایمن از تنگه هرمز که یک موضوع با اهمیت جهانی است، اعلام کردند.
🔴
فرانسه و بریتانیا هر دو همچنین بر تعهد خود به ثبات منطقه‌ای و احترام به حاکمیت همه ملت‌ها تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131696" target="_blank">📅 09:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131695">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRZNcM57R9BtrxJCPDuxLVghPmEcZvoFdNFskEiaK7fpROzBpzN6QezYxSVcxqhysv1tTgGbmc-Ynx3MO1QGaujD_PAWKT8mR_P_KlpA_jxelC-HDImnW4vD0B1BYuR-xT9V3HPQzS5GMT_0x5kLrASs0Nq6Fl-vZU2E8UYsLqjuqdmGrbg-gEoQ2iU-VV1PEHix13aWewlYrt2bQeb0pLWFuWtNtf4GX6ggwkbvDq26btQdR2rWhG7DaQS9QFp9kIlR6r5lcDyxF9QrgPKkbyMjH7sTDDJKxwnZH6oDAT_5X7fgpqTjtGiNms2C3X5smGBzhGHvGfNrnMJbiv52Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل در نزدیکی تپه استراتژیک علی‌الطاهر، در جنوب شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/131695" target="_blank">📅 08:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
متروی تهران از امروز ۲۴ ساعته شد
🔴
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/131694" target="_blank">📅 08:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع محلی از حملات توپخانه‌ای اسرائیل به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است اسرائیل این منطقه را هدف حملات سنگین قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/131693" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=M5PeEn7qv9-Jvnzflazn47EP1zv0O4prOGaqMZUw0TYZkc_OLa78WFAfqPowrv8Gg7KoR4H2plFR3VHn-g4M9pkZMWBX8WWgKjJYDCYZiCMFYvZPLmGohxSwOgKCtlsEOKIpAmuTvcq-0Nqx4I2_6LNhHifPGjz7JDTEAZ5nuhTJSgtG56KXbrnRWKyKlIYpc0LuS0TGNHGikEYj-r3yfcAKcQatiWrqiKl6Ka35gq9nvJfcd7u4I0YAUSPn0ImHg0bReG25yZoxs--r4ahUivk1wviGLJXkObu4VVCnhY6Fi2vXNzUka6tI6r_TNmGDEQ43oklt1Qdhq5HQEV7VlVz19BrXpMEzAP4mrlvNZNmJTfcLYVhaKAb9UY92I_vdjm3WpI61BQjP4NbYrhoURq7wkjkxlpSiJINXlaOdgfZHRcwoIRdzOnanZqa4zh0LSoWlgxyU7ymPN-vKKTqunly3cllyB8p-OGeE06lLXH7kCgMOV7dT-0J1SaHjOko58Oho5w4xF8gaL487ccDlI1lfv-ipGsDNrBi0FKdvWyzT8vNokDktB3eGQTPnC_2sJa-SqpP4L0-YM2dzm40Eez5islWZ0nM-ORN-EbZowid1nl5K-bebAR8DxveDAalb3AU6lzFeWgrU3C_SdFTF6WPqWIEljzvjO6JfpRWn1q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=M5PeEn7qv9-Jvnzflazn47EP1zv0O4prOGaqMZUw0TYZkc_OLa78WFAfqPowrv8Gg7KoR4H2plFR3VHn-g4M9pkZMWBX8WWgKjJYDCYZiCMFYvZPLmGohxSwOgKCtlsEOKIpAmuTvcq-0Nqx4I2_6LNhHifPGjz7JDTEAZ5nuhTJSgtG56KXbrnRWKyKlIYpc0LuS0TGNHGikEYj-r3yfcAKcQatiWrqiKl6Ka35gq9nvJfcd7u4I0YAUSPn0ImHg0bReG25yZoxs--r4ahUivk1wviGLJXkObu4VVCnhY6Fi2vXNzUka6tI6r_TNmGDEQ43oklt1Qdhq5HQEV7VlVz19BrXpMEzAP4mrlvNZNmJTfcLYVhaKAb9UY92I_vdjm3WpI61BQjP4NbYrhoURq7wkjkxlpSiJINXlaOdgfZHRcwoIRdzOnanZqa4zh0LSoWlgxyU7ymPN-vKKTqunly3cllyB8p-OGeE06lLXH7kCgMOV7dT-0J1SaHjOko58Oho5w4xF8gaL487ccDlI1lfv-ipGsDNrBi0FKdvWyzT8vNokDktB3eGQTPnC_2sJa-SqpP4L0-YM2dzm40Eez5islWZ0nM-ORN-EbZowid1nl5K-bebAR8DxveDAalb3AU6lzFeWgrU3C_SdFTF6WPqWIEljzvjO6JfpRWn1q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در آمریکا، ما به زبان انگلیسی صحبت می‌کنیم، زیرا این زبان، زبان بنیان‌گذاران ماست. و برای هزاران سال، این زبان، زبان آزادی بوده است
🔴
یک آمریکایی همیشه خواهان صلح و آرامش است، اما ما هرگز از خطر یا تهدید فرار نخواهیم کرد. ما همیشه خواهیم جنگید، جنگیدیم و خواهیم جنگید، و همیشه پیروز خواهیم شد، پیروز شدیم و خواهیم شد. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/131692" target="_blank">📅 08:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131691">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: شما می‌توانید به کارل مارکس وفادار باشید، یا به آمریکا.
🔴
شما می‌توانید یک کمونیست باشید، یا یک وطن‌پرست. اما نمی‌توانید هر دو باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131691" target="_blank">📅 08:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=f6lU_bd8BnYE4r4OHQipMUJHW7XgrbZRsMmBuGDGD3K6NzvqyUIY5wQ943s9vI4K56kGmJvPboGTAxarRaODpH6UbzzttsefsEF3EnV0u6_yy61PFDvvtX11pFmB5wF_tteVVw3Jgm72FRJhKc6wNyQb47FpcrFhut4MiRAMWFqvZDUrrV9D2FWqmJnDuAKRVPTzwSnulckErvdoJa5bOuID-_xBX774FaMrdkCrLxHC6WRiUCX7tNWC6rzHLh3W31xOC7fqr9DmKPbJ7WIYoC6N7Gp4jTJwi6jHVB6U7sP17ORZbpyaEHqMtAxwWmAYj9bftJsxELvlGvANT5uJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=f6lU_bd8BnYE4r4OHQipMUJHW7XgrbZRsMmBuGDGD3K6NzvqyUIY5wQ943s9vI4K56kGmJvPboGTAxarRaODpH6UbzzttsefsEF3EnV0u6_yy61PFDvvtX11pFmB5wF_tteVVw3Jgm72FRJhKc6wNyQb47FpcrFhut4MiRAMWFqvZDUrrV9D2FWqmJnDuAKRVPTzwSnulckErvdoJa5bOuID-_xBX774FaMrdkCrLxHC6WRiUCX7tNWC6rzHLh3W31xOC7fqr9DmKPbJ7WIYoC6N7Gp4jTJwi6jHVB6U7sP17ORZbpyaEHqMtAxwWmAYj9bftJsxELvlGvANT5uJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
🔴
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131690" target="_blank">📅 08:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHk3sVp09VgcZk8h4q3YQgTJfEeF4S5KDoULPDIPVM7Oc_7xi-7r0VUAHHHxGBDx5i9Q005_wVUaqsiENW3t51BEwh3DOIRYJ_t9hmyMqEhOyeXTAa8AQWjrrbD8s79_Bizy1cyOxk9mEXxddMjouh8s23WebkVeFuwQaKR8Nc9tM7RyZMwDGuov8oPWhoYf8P2Ps4hUlF47EvIz3eTYWOE8tgK4EUSYpJnaIK2BmJf2jTIA7xAH8NfH-dSRuBTeHCgIGNdYvIXFtOkfSl6sAyCGryJBhNyt-bj6oqGFlqaa76FOrJQAo__Kdm5vtLrZZ3qE-7Fxn9lAybsnQX_-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین سایت کاریابی روسیه، برای دفاع از آسمان مسکو از دست پهپادای اوکراینی به دنبال استخدام داوطلبان اپراتور پهپاده!
🔴
وظایف این شغل شامل آماده‌سازی قبل از پرواز، شناسایی و جمع‌آوری داده‌ها در روز و شب است؛ تنها مهارت‌های فنی اولیه رو هم داشته باشید کافیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/131689" target="_blank">📅 08:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prgNmX9H2Kr_Tj3vw9zhkbLcvRjDX1E98_vQm7-eFKNR4RnYZa-89JBCfKoS6JMvk4WAjFbeQQzGMapOdBeTnyhPzVQ-xYfLi1ICDIFkk_7PrwP6INwlbK4U35M6G2t9uIrmg1ACnUOSDUqjQs-EsVOSQQZ3-mjDNRQGmRMmnqR35m272pYB5ZWsTpYCqkLA4ekyfII5nseIVPd0CP5LBLJQOAYyzy71C65W4R51dGqfpk0Vl5eMuMDBRWoL23IXFJOODms1G-81sHtlv6c4KoFkOsZsRZ1nhy-THzX9nye_363X7iNdesFCC8ZQaE1U2aZdNsEWBeZDWr_zVZkgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk1eKhpx_A6YTa5gl89rretYos67CqV66s8Qp9UyOSeUS7njvbY1ANha_dgIVrTRMRz5BhfwujEMN7p3jpu7A2Dj72W83RZBgjeHCPtODbYm34kiBHJ4DGdHdyFutlcavwGSVJwFyitSeVZTOREmjsEsg-LvbSf2iInsj6ed9UaH8Z1gDz4sOc538qLP6inYGKGlkk2v8tv2dZq8MQnzGn70Y6aRTnckisCCEtKB3nQHZcF7tExlZc8sn1x15LK1l3oy9d9EJ9IJCRd9ZNTM4bv1GdaDjjkepRK7QGZHkY5J8yYS2LwYnO52Ns3LqwrMrW1DH_ZH8SJbkl8B_LJqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3HwToLVxFasxwAh44xLl3CS17vz1RHoMKsf0KjnFLRhZ2evvH3_qcF1OQbga8QOEpUSFf7tKxvdBhw9jp3phMUslPyQzz38VvzBdkBnnLhRB49GO6VVLvP08_srv5dwUl_cjbwjjpC-05U7GLXzHf379ZadtC5lSZu92qhIjhzFVB0HoIw_e_b3qJzhTTHtsJb26FmTW9neRca5yMszJkCPGCaCPiMiI8DLUqDmh6e--xyREWI3B8XVRwcc6eQABohvekBrVCE1InyRinea0t-e_iRAIbli2MOoqboN6QCUn-2Y0eeKPvbW-T9g8VecR4FjwNXEOjaAZ3Roh8ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/131686" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس :ساعت ۶ صبح بیاید مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/131685" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/667106b64a.mp4?token=kz810Gvf8Mwf30Ra5_kvfIYAsJhiFxtjmbSQy3ZfBBxJQGT7nF98mPUcPTSzyMALefRjqaGEWaaK_5IH8fQ2yv0TEKc665Zz6nfKBSy_M5I0e6yRow8FY9-J7BmX9RZxKOnmYwW0tl9AsYJhGZknH_huWZdfActUyabzudRFp-pWUlMKNP6NrlPhoYhNr4I_aDzQXb8bvH9_q0FcXYlW5Bkh1WuDGumajeOBqxBBFXdRppfhlILC4Gn2Pp2u2rS0Ecni0_SS81uObl5OTaLQZscgJG0dqxFtD7_YzfF83x6HN0Kr4NnAX0OIYuvQixcj9SOOVK0EKp2YL4-hDwds-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/667106b64a.mp4?token=kz810Gvf8Mwf30Ra5_kvfIYAsJhiFxtjmbSQy3ZfBBxJQGT7nF98mPUcPTSzyMALefRjqaGEWaaK_5IH8fQ2yv0TEKc665Zz6nfKBSy_M5I0e6yRow8FY9-J7BmX9RZxKOnmYwW0tl9AsYJhGZknH_huWZdfActUyabzudRFp-pWUlMKNP6NrlPhoYhNr4I_aDzQXb8bvH9_q0FcXYlW5Bkh1WuDGumajeOBqxBBFXdRppfhlILC4Gn2Pp2u2rS0Ecni0_SS81uObl5OTaLQZscgJG0dqxFtD7_YzfF83x6HN0Kr4NnAX0OIYuvQixcj9SOOVK0EKp2YL4-hDwds-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موزیک ویدیو کامل آهنگ جدید توماج صالحی به اسم «تو چی؟» که تا تونسته به رضا پهلوی دیس داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/131684" target="_blank">📅 01:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم  «تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/131683" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiNsjJ1iavbklIhh17lVhazii-izRmAG13PmIqfUhLeHA7TTggndo8hMaRkAa0npv-jdtWon8-PolzpdWxfF5UxYHmyhwziPZQNwB5cA0iE_2Ofuwtf30kjHlvDB1WA6Aklp5ZWtSmnFocIz4FE1y5lFoLBJRxRQVtHgtLRVshGvXAbeP3_iMRjmBQNT_wofMpvjpkxsKa7CRXCxaSm-MMDFLTMroGT0M0JelrG5MDzpIb0ZcgTi6tUdAp3yk5LWELElkCQVVj1xCEqyRiPwvJiFBgiT5QsYMgGeQ5Ou6vxmyfnvfAvMXfHwBwMiFSaoqn0zJFPHyCRvchrNWI7LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/131682" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=drwhBEDjuPy4H2IOYPXmhK4M1jvZ3HK89nuS9OArC2d3I3xz-U09Yfjhncj0BzWO9HDE6kFQPTYJfBeJwm4C_k_Auh4rldP0tpjMbUnIAWCA6DVy9EWXZdHSFnFq_ECIMWSWvb80EEfMGd7CFkwhOVaz04UeJE3pKVFoIC9HHAqJcaBZrRDuzO7JhxoC70U2fakt_h2o5DDjiv9K6itPbGNY5EJ8jGI32ej3bOeRZxFosurulf2qQtikLyje6FQVwDFXBCiEtYCPMcCUlZakuK_GdAg4e8ZGh-dxZNlR8xTzxBWxba9_KFtyJ6FHOhB0UB7OiswBPAmgz7kMm3CSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=drwhBEDjuPy4H2IOYPXmhK4M1jvZ3HK89nuS9OArC2d3I3xz-U09Yfjhncj0BzWO9HDE6kFQPTYJfBeJwm4C_k_Auh4rldP0tpjMbUnIAWCA6DVy9EWXZdHSFnFq_ECIMWSWvb80EEfMGd7CFkwhOVaz04UeJE3pKVFoIC9HHAqJcaBZrRDuzO7JhxoC70U2fakt_h2o5DDjiv9K6itPbGNY5EJ8jGI32ej3bOeRZxFosurulf2qQtikLyje6FQVwDFXBCiEtYCPMcCUlZakuK_GdAg4e8ZGh-dxZNlR8xTzxBWxba9_KFtyJ6FHOhB0UB7OiswBPAmgz7kMm3CSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم
«تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/131681" target="_blank">📅 00:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت
🔴
پ.ن : تاثیر گذار بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/131680" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuVr87DN48mRkKzD-3lTLZrsNu89ecgxAHRaS73QpafudGMGb6x7TePo1Dvq7f20Fhdb7og5Z1X5DyBbUF7RppkUvQoLy5doKTyByOFvp5i_FL1kwXoQkCCLEv6egclqgqYacJHJd-w8ntckIRo2tb6QEvZpXadp-0YONTP31mI_5YtINdS1LZSgqo1QFm2XWizXkK6Ac3QLnpTnFphxmXMf_4s4uIZQkZrRIcFwQ7qQq48-2AiDYg_vyA7kz9Zs7J-hqqxZrqf1_lzyshijDgxJVQ2x8_oBib8kRojkrwLOaS66IjEFTAQQGM_aouLHInDpkCA8GcJv8sCSUR42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان بعد از ایران به ترکیه رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/131679" target="_blank">📅 23:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/131678" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/131677" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brMBg6fgltoVq7NRa8ynlR4mSt2XX9UQnbrYkSbPsGoiGAz73MgVpRHjczbkV3NHc-5m8NAOexCrcugZhzgLqqc2m7PcAEPRtvJrQm90w3WZKCgCCUtoAJ9R507bLE6q2zLlIY1vN7e2WgCcBwmw5Sbvlgm0jbZYAAsz7AAdQrFRoq5D0fbGRL0wE11OReq_yjKNUoVk5PB8bpXwyQ3_HJa9_KuDtvTF3e7R1IbJ94hHNI8l_FaSbpRSI4SPQYe9pbUyBXA84Qh9ziVuk9p3MizjtGnQnJAv4lnbq2TfAGfx4OJXNGEUzDzbAcP_WC2bEFTQ1xeuu7dxVBw5KXW7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی: ابراهیم ذوالفقاری چون تو مراسم تشییع رهبر شرکت نکرد،پس صد در صد مطمئن شدیم هوش مصنوعیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/131676" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrvzamxIC3wOvA446rIRbiZ_bexqkNA7_iVBv8bdc7HSmXlufCIhyLNbQTThzofAArM1DKV9E-I-MPJQAmu35KPUuMdmrHDkAqXHuYM_aMkvr_R-w7euXEKqm4HonR78-Gf488zWB9mSMzdrhd22wGN91xtWzosrUJ4zyX3dugu4P6cQZNBZkQyJjiOZ-p5zakpTyQBLoY8zSS91oOvhuG0eancsYU87r11mzbfx6b8bykMY8fPUEIW_Q0XrKyKeSltQocMNQMUvbSDZiFWjkebLJDDyzTdiOPOS_fKGP4LX0hRFGe6QKAehyoUpqzagle9tCaePjEWARrQisbX3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/131675" target="_blank">📅 23:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=b0W5o2yKFNszC8w0oHx3achW4XVcbjZsuVf_8cSjAZkmwqwOP0VjTUUezjdVhYy7le6eYwFpFI1Gpf15FA0M57-m_oK1zKFJBiafTzLuSKq_M-H6GYOhm7Cg-TODXhBPZ9T3fdF7nWZcLonYtupYKcP-sIYpv4kA1teNZ4wiReJWZC5Lrj-yFhLWqFogBZejYgSZuNIpFCN4rqMzacjAUz_EEauOttEq_SqYH2YTtC81VXMfC3Kz9SZZvs1SeUucBRas89ygqH1IkxZ3GpOkcyGmjrLrOPBvp26uxyvLdXY2sfx0XGQaHD-aGuqNZDeJkSJn7PtzxkxfKVoJ8Td1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=b0W5o2yKFNszC8w0oHx3achW4XVcbjZsuVf_8cSjAZkmwqwOP0VjTUUezjdVhYy7le6eYwFpFI1Gpf15FA0M57-m_oK1zKFJBiafTzLuSKq_M-H6GYOhm7Cg-TODXhBPZ9T3fdF7nWZcLonYtupYKcP-sIYpv4kA1teNZ4wiReJWZC5Lrj-yFhLWqFogBZejYgSZuNIpFCN4rqMzacjAUz_EEauOttEq_SqYH2YTtC81VXMfC3Kz9SZZvs1SeUucBRas89ygqH1IkxZ3GpOkcyGmjrLrOPBvp26uxyvLdXY2sfx0XGQaHD-aGuqNZDeJkSJn7PtzxkxfKVoJ8Td1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین یبار دیگه با لباس نظامی ظاهر شد و گفت که نیروهای روسیه ابتکار عمل استراتژیک رو تو خطوط مقدم جنگ در دست دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/131674" target="_blank">📅 23:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی کرملین دیمیتری پسکوف:
پوتین دستور داده تا به دقت تحلیل کند که کدام از متحدان کی‌یف در تحریک ادامه درگیری‌ها نقش دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/131673" target="_blank">📅 23:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejKSmXtOZvt1p3Y9bGHQBMyToEQfRH2IuwVtvmiRxUDhUfgL4SVmABKldQ7W2v9mj9U_OSaEexqAjUU4EmhFxoljOimcG3rcU0qFNHy-EkOzdX0H6jd7Ab9sJGrX50Mb5105P6xe5Y8p8ufwQKx2uTK3Ma5faFyqDXa2PcOkNJWZlHQQ7lDxnh4AXZUdu4X0sqkbVgpGFJkuby1ifRy8975UeOLAx9xcRvZlmDZd0r-2YlDFljBSSPn9B_65iBws7NIv_lWjiSGegKOvvLL9BXdpAFHAl8wv6DY4zWDFQtf5ezZRjyZ4w94wvhVgNmgWzj8L7NvLqtRP_QzwrsVXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: افتخار بزرگ من این است که همین الان برای شش نفری که توسط دولت بایدن آزار دیده بودند و در زندان بودند یا به زندان فرستاده می‌شدند، به خاطر «تعمیر ماشینشان»، بخشش امضا کرده‌ام.
🔴
در حالی که می‌دانم این موضوع مسخره به نظر می‌رسد، با این حال یک واقعیت است و بخشی از تسلیح‌سازی و احمقانه‌ای است که کشور ما مجبور بود در طول چهار سال طولانی خواب‌آلود جو بایدن تحمل کند.
🔴
من همه آن‌ها را همین الان آزاد می‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/131672" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=ixas-OZBS06wVB0oHDOZhyhm85gDaSH7KxrNVfWFlSNrDOaFNbyd54sX7XgKmCLn3AuWuRZowKE67Akpd1_X5sDnO5loqybnfXzgcsT7Mb0F6CODDjlmxJ9Uq6F4h5tKhUb5XxscMyo9RxO1CQgh0OOO6gnJyuKeA-ZLPCGyqiWx7tmLlEimXFBXufvyZXGbQJEsZU7ougVPTft9feGn1gQgP0EPjyVAWeSACEpZt2mQMz9OKo4RPdyXlQOEpv5P6x4PDEgC_S0f6RFpW2Xt4TwvxP2E-DFnvR9jdgLYcO4MNfSdkz4uHswL4HenabJZolbEWvk-eiV1Qf0X0ulVgy4hOFUdfnsm-s-ni-nQgRTnHR8xrJRCG919NsVkraBRZNBG5cixACQWjpxawuxg33Th0_kftPDO9cv79ZAkh8M0_14esTCmmaWotuTFYNDZxpBg0cggyEh2eTpmR2MrrFbd255jtTtXsvJPDQwSR1bbKLVWXGkP143WJCnKRVNgU4a_P2SUmlXLZg_UkZHMZ-q2_is3BxbPBPpzkTRKrS1eKESRLSFHWp8sgviySGgJ6yzpB-k0JaWjRhXtYdAaGWGWcsOJ-YQJ5BvWnTG5rT5AWqgMyY9mHHEeS0iU6zJcVyCWPnqy0e19XR0zQKBNdvxyhvqlKOo5uI6UYSsIfN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=ixas-OZBS06wVB0oHDOZhyhm85gDaSH7KxrNVfWFlSNrDOaFNbyd54sX7XgKmCLn3AuWuRZowKE67Akpd1_X5sDnO5loqybnfXzgcsT7Mb0F6CODDjlmxJ9Uq6F4h5tKhUb5XxscMyo9RxO1CQgh0OOO6gnJyuKeA-ZLPCGyqiWx7tmLlEimXFBXufvyZXGbQJEsZU7ougVPTft9feGn1gQgP0EPjyVAWeSACEpZt2mQMz9OKo4RPdyXlQOEpv5P6x4PDEgC_S0f6RFpW2Xt4TwvxP2E-DFnvR9jdgLYcO4MNfSdkz4uHswL4HenabJZolbEWvk-eiV1Qf0X0ulVgy4hOFUdfnsm-s-ni-nQgRTnHR8xrJRCG919NsVkraBRZNBG5cixACQWjpxawuxg33Th0_kftPDO9cv79ZAkh8M0_14esTCmmaWotuTFYNDZxpBg0cggyEh2eTpmR2MrrFbd255jtTtXsvJPDQwSR1bbKLVWXGkP143WJCnKRVNgU4a_P2SUmlXLZg_UkZHMZ-q2_is3BxbPBPpzkTRKrS1eKESRLSFHWp8sgviySGgJ6yzpB-k0JaWjRhXtYdAaGWGWcsOJ-YQJ5BvWnTG5rT5AWqgMyY9mHHEeS0iU6zJcVyCWPnqy0e19XR0zQKBNdvxyhvqlKOo5uI6UYSsIfN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع  می‌گوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/131671" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بر اساس گزارش شبکه NBC، حساب‌های سرمایه‌ گذاری دونالد ترامپ، رئیس‌جمهور آمریکا، در یک روز قبل از توقف تعرفه‌های بزرگ، 327 خرید سهام پنهان انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/131670" target="_blank">📅 22:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/131669" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=HScSJyYuVAGSCL7HN7LApX9MgrmIr8Nxmy47Zxm98Bt48mwpRItYfFbQk0Kca75SFjOeHdstoAHjB9VmU-rc62pLr1clljuUM9AIGo2ppPwrPqVWTR-wnQ0uMX7R_E6ua0MPemFWTLueVBMhvhBgD-yE1ppCPxk8o9dVPyjgzi0JHqOZ6GdnVVqMQgW_ep7DtsRfAs4vyErO1X4tWsZSHECQqElWlJ7qA3rONWNyZR0FYTXHvO3lJdh7eph5nCUb2sFHwDVnILiO49THCNmitMKqvqIM6MwJA8acQKp78U2OdEnrCywHyCvBk4mN11pTn9FvHyM7qVgjwKc3fjUoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=HScSJyYuVAGSCL7HN7LApX9MgrmIr8Nxmy47Zxm98Bt48mwpRItYfFbQk0Kca75SFjOeHdstoAHjB9VmU-rc62pLr1clljuUM9AIGo2ppPwrPqVWTR-wnQ0uMX7R_E6ua0MPemFWTLueVBMhvhBgD-yE1ppCPxk8o9dVPyjgzi0JHqOZ6GdnVVqMQgW_ep7DtsRfAs4vyErO1X4tWsZSHECQqElWlJ7qA3rONWNyZR0FYTXHvO3lJdh7eph5nCUb2sFHwDVnILiO49THCNmitMKqvqIM6MwJA8acQKp78U2OdEnrCywHyCvBk4mN11pTn9FvHyM7qVgjwKc3fjUoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های آشپز برنامه "به خانه برمی‌گردیم" صداوسیما که تغییر جنسیت داده و دختر شده :
تو 5 سالگی، یکی از آشناهامون بهم تجاوز کرد!
من کلا تو خونه پوشش دخترونه داشتم و این عمل، تغییر جنسیت نبود، تطبیق جنسیت بود.
من حتی دفترچه خدمت هم پست کردم که شاید از این حس فرار کنم ولی نشد.
تا 25 سالگی به کسی چیزی نگفته بودم ، حتی اون زمانی که تلویزیون می‌رفتم هم از همه پنهون می‌کردم.
2 تا خودکشی ناموفق هم داشتم چون اون موقع حس خوبی با جسمم نداشتم...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/131665" target="_blank">📅 22:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید کاملا مورد
تایید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
➕
با کد تخفیف زیر میتونید با ۵۰ درصد تخفیف خریدتونو انجام بدید(فقط100 نفر اول)
✅
🎁
کد تخفیف :
Express50
.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/131664" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 100,000 تومان
▫️
۴۰ گیگابایت — 190,000 تومان
▫️
۶۰ گیگابایت — 280,000 تومان
▫️
۸۰ گیگابایت — 370,000 تومان
▫️
۱۰۰ گیگابایت — 460,000 تومان
▫️
۱۵۰ گیگابایت — 680,000 تومان
▫️
۲۰۰ گیگابایت — 900,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 1,150,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 190,000 تومان
♦️
۵۰ گیگابایت — 280,000 تومان
♦️
۷۰ گیگابایت — 370,000 تومان
♦️
۱۰۰ گیگابایت — 505,000 تومان
♦️
۱۵۰ گیگابایت — 730,000 تومان
♦️
۲۰۰ گیگابایت — 950,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 1,350,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 480,000 تومان
▫️
۱۰۰ گیگابایت — 555,000 تومان
▫️
۱۵۰ گیگابایت — 785,000 تومان
▫️
۲۰۰ گیگابایت — 1,010,000 تومان
▫️
۳۰۰ گیگابایت — 1,445,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 1,650,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131663" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ety9PNakdV7hRAInyo7vxcVbC7yc8YT_XUXu1LP7J0a6EpmxsHtsrIBrv6tgyLfgvP4nvjgNKViUp83NYUcWES1uhQ0QADChgXSQOwjp9ly3YxSCBuiulWItWTOhJ0CCzDn8sZB9CKkFUg5FRTlnN4KY1VrRhwlsTkubDGRCbP-UDWD56QsP5Xz3kGkiBiGBeb9hhVYkrXvBvWL4B05--6oTZ8Rt0DYtJubtzH5kJU68a6raIQlNkt5voFVVhRwoJXRQcm9L5a5U-mJcVAxAXuSP0dZhgw5uRLJSUF9k0fEWZ9FkKNmepX9_nL8ieeUVsGA7yIYPOcwsf14hzqx14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به ترامپ: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده.
🔴
ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131662" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131660">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/131660" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAEAE-DFPTvtxuRWSyhFeYq6RIphhJ8MGmoakALLVleuAo8e_Kl13oc0LZb1-uQsbGZiOTcbxPVOjYi-xYxG5tIitJGzqHiAx03m_DrOihTpQrcF1nHo771UmW3Zo79qSvEMI5yh85zm1AJCa8Pn0rW0XeW7r3UOhUNGB4_SXwJYSSQD5BQPbd0Hg_ArzRwjzLJRMKh4u3VFsZ-X0ShXp4ajQ1a4pLwNeOF-WPw6nNUDTPDHoNNEwhOi8Kg5i8Mu5Tzb8_q9b9SeLylGsNpfg2rP9oCGOXA6XZNmeUCFaj_h9g-9LAbzKqdvS_kVfcnfrCsYiA6T9BKjdfti6ZDEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال قبل در همین روز، مجله تایم عکس سیدعلی خامنه‌ای را صفحه اول گذاشت و دقیقا بعد از یک سال روز تشییع جنازه علی خامنه‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/131659" target="_blank">📅 21:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: اولویت‌های دفاعی تعیین‌شده از سوی قائد شهید امت، دست نیرو‌های مسلح را برای پاسخ به دشمن باز کرد و پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/131658" target="_blank">📅 21:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/131657" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان: رفت‌وآمد کشتی‌ها در تنگه هرمز در حال افزایش است
🔴
هفته گذشته ۳۳۵ شناور از تنگه هرمز عبور کردند و پیش‌بینی می‌شود این هفته نیز تعداد عبورها در همین حدود باشد؛ به‌طوری که تا پایان امروز، شمار عبور کشتی‌ها به حدود ۲۱۵ مورد برسد. این در حالی است که پیش از آغاز جنگ، به‌طور متوسط روزانه حدود ۱۰۰ کشتی تجاری از این تنگه عبور می‌کردند.
🔴
اگرچه روند کلی فعالیت‌ها در حال بهبود است، اما بازگشت کشتی‌های تجاری بین‌المللی احتمالاً با سرعتی کمتر از ترددهای محلی و منطقه‌ای انجام می‌شود؛ زیرا بسیاری از مالکان کشتی، اجاره‌کنندگان و شرکت‌های بیمه همچنان رویکردی محتاطانه در پیش گرفته‌اند.
🔴
ابهام درباره خطر گسترش درگیری‌ها همچنان پابرجاست، به‌ویژه پس از آنکه حمله ایران به یک کشتی در هفته گذشته، عملیات تخلیه دریانوردان گرفتار در منطقه را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/131656" target="_blank">📅 21:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
باراک راوید: ترامپ امروز با نتانیاهو تلفنی صحبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/131655" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pmUtrMVHpyJIi3jVFE7v51Au4ZxKFss4ok7NCSwLlC5GOku1lqXQhSmMIGPVbwMTUP6jicsCBv-Fp3mKyAYc7_MhH8pHTDB2O9ArOqJoe46ccn11OwO4A0tHZV3KzO8RnKMZm3CixvzURU7psWwl9kCVQM_gd8OvApvB7XhrnvOvzwzgIpruY7a0lOC-lCdQvhU4ylpmKCCOy493Z1OdH42B4fRx39piqD1BK2XhKCGvGStIZrQHAZ-P5wW_Vhg032gxf4FMDtqpOKdwkU4EDkjiJW5bUj1ME56Clene1APioqSF5nAY2h4sjYBfPiE3phgKu7CFy1q0pnA8WcJRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@AloSport</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/131654" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JvNn7Ee_4Y1ijFKbvKiyxlJEY1tPcKF7rI9gMrJbFyTKebNSaax8jG9tOqHjbRNQR3KabNOTF7YJduq2BzycfMcmrzXT2ZlmVHEAh4f6l3C6U6VWrcKG_ycg5Xjnw4IqhmulFKTuTmYD5ugVD_s1ZXeANsHEJGJ2n4FUSBJXyQyVzeoBqw5CgVfVRdWE7aRF-aUpvhJDZqAIX2taYNOROGyKKMOvag_yOpasVWeJNlXKG4ba6ShdUBwlQiu8azixsMfkhW5m2fy6Z9LT-u2G-_h2c8RPB-8ulAuiZGxTnIHahLPKz6lSpzXqZV-WHvNb3h3AhIeC00gApuhEMmuAqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JvNn7Ee_4Y1ijFKbvKiyxlJEY1tPcKF7rI9gMrJbFyTKebNSaax8jG9tOqHjbRNQR3KabNOTF7YJduq2BzycfMcmrzXT2ZlmVHEAh4f6l3C6U6VWrcKG_ycg5Xjnw4IqhmulFKTuTmYD5ugVD_s1ZXeANsHEJGJ2n4FUSBJXyQyVzeoBqw5CgVfVRdWE7aRF-aUpvhJDZqAIX2taYNOROGyKKMOvag_yOpasVWeJNlXKG4ba6ShdUBwlQiu8azixsMfkhW5m2fy6Z9LT-u2G-_h2c8RPB-8ulAuiZGxTnIHahLPKz6lSpzXqZV-WHvNb3h3AhIeC00gApuhEMmuAqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیم نمایش‌دهنده جت‌های جنگنده F-35C نیروی دریایی ایالات متحده در حال پرواز و معلق ماندن بر فراز نمایشگاه ایالتی بزرگ آمریکا به مناسبت روز ۴ جولای و ۲۵۰ سالگی آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131652" target="_blank">📅 20:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=RkYUrdNIUKV2p_B9C5h4EK9kiJZDxPrcGKiD9RjmbFv60I5SGg9VDzLjLpwCRlWV7nluMrhGG2f4wXnaHZPW1heVpwb3GovMTKBl4xVLIq-QRYOIu2oWe_982heLlgPUEIVYjC7xBIDKqltaR_tG2LRqpm9f_G12YlBAL0QnvUhM3sRAH8fjBMZ-RGqLIJUqK5P3AiO66nJY1ebq1rRC2QDEbZgHLAB9RwwMErKn1FZZae5koB8DCD-2vVFGdS2T-OnekfdEyZY3FCT720GRynbxK5tA9GQmn5bHr5ECHJ2WserKyWQgKWplHJZ9wtqllpHYpWOQRmg-tK13UpDHLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=RkYUrdNIUKV2p_B9C5h4EK9kiJZDxPrcGKiD9RjmbFv60I5SGg9VDzLjLpwCRlWV7nluMrhGG2f4wXnaHZPW1heVpwb3GovMTKBl4xVLIq-QRYOIu2oWe_982heLlgPUEIVYjC7xBIDKqltaR_tG2LRqpm9f_G12YlBAL0QnvUhM3sRAH8fjBMZ-RGqLIJUqK5P3AiO66nJY1ebq1rRC2QDEbZgHLAB9RwwMErKn1FZZae5koB8DCD-2vVFGdS2T-OnekfdEyZY3FCT720GRynbxK5tA9GQmn5bHr5ECHJ2WserKyWQgKWplHJZ9wtqllpHYpWOQRmg-tK13UpDHLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توکیو به مناسبت ۲۵۰ سالگی استقلال آمریکا آتیش‌بازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/131651" target="_blank">📅 20:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/131650" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Q5Xy1NcdYwFmULYuCJyJOvC8ooufsWQq0dFxj2KHRlt3jKMiAddi0Xogm0Hqbg_CZMrcxjhczM-H751jWUT7OzYk_Ivr_wdk89mm5SnR7gaJYe0fOacGAcSjTOBf9Vt9aAdgWfEOOkP_fsCW2tssKewheFx218aFL-I0EP3Npt-TbEZZsOhp7ziYLY6ccAu78DKUX2a90RDDQtphRqw9ZQ0hXJuxKdktOLElUj8sbCCuJUXQjTUMc9fm2zgfDt1MNqHyzNP1SVB0FT0290z9ekFStZqUbjtyGnk08q6keI_pIpfS25ORSe7t6BDOoj2hUBxSG6MtSkOSZ_8yviXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: رئیس‌جمهور سوریه یک بازیگر زن محبوب تلویزیونی عرب را برای مجلس انتقالی جدید کشور برگزیده!
🔴
رزینا لازکانی، ۳۶ ساله، به‌عنوان یکی از ۷۰ نفر منصوب‌شده احمد الشرع در مجلسی با ۲۱۰ کرسی انتخاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/131649" target="_blank">📅 20:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYwINhrYDK2RErG9p8aBLOkh1Uk9HCnr-trplYgVNi00leuq6n3Q-ImL3fA83l_s5pY2B9Y316hYVRJtc4nIKOeXFwtxsB7oQQ3FV609I6255l3lK1_7idGBEA71EmXhx2lu6KpGP_IOkAG2l_5KULdSWgBKNy6-wagI26xqtJdgeTCmKwNAZc2ECufk5Xb3VEi_dZos6qKU7dQ0eRjPfB67eHOV20vw68hrVd9hXMaDBmoVkx3JKdC4rn9nhxYM1o1-35T2HNiiDFnOUH4CL0Von-L8moieAPlsxA4XQ8Hg4drNKJXsoK6JZ39JLvqbzD3yTU-G9JVCeCZJiqBVmhFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYwINhrYDK2RErG9p8aBLOkh1Uk9HCnr-trplYgVNi00leuq6n3Q-ImL3fA83l_s5pY2B9Y316hYVRJtc4nIKOeXFwtxsB7oQQ3FV609I6255l3lK1_7idGBEA71EmXhx2lu6KpGP_IOkAG2l_5KULdSWgBKNy6-wagI26xqtJdgeTCmKwNAZc2ECufk5Xb3VEi_dZos6qKU7dQ0eRjPfB67eHOV20vw68hrVd9hXMaDBmoVkx3JKdC4rn9nhxYM1o1-35T2HNiiDFnOUH4CL0Von-L8moieAPlsxA4XQ8Hg4drNKJXsoK6JZ39JLvqbzD3yTU-G9JVCeCZJiqBVmhFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چتربازان و هلیکوپترهای گروه "گلدن نایت" در حال پرواز بر فراز نمایشگاه بزرگ ایالتی آمریکا در واشنگتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/131645" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuI3NAAcmKyH6Hr9FdOPCL99-lQh-Cu8oG5msBz5YycB-sQmYJu0mGo_52-NXlSis2E8oXPhqCRiEWsh8qucH-HwCrTXAosK9tcgEWa9bz6hNltLlzpjvXUW1bYZx314lJgk-FTVLwn7A5R4P-clAI4dv9U1gdJi8Nu4gEFyYKa3hHel6XV_fn_1dflByvy6YnL_Ls5HjaBiJFaD12gAfv570N04zC3k2lRSoRL5mnusQrG0oa_Y3IqfBnd3Bx_TqzpK9Myef3NRPn8nnOcqgYsYGM2noK9VQlx4S0ARBNXLtq7rbQL8dwWWeolU7MNIjnT-lHxN0hTlowVlv2lwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عاصم منیر با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131644" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/131643" target="_blank">📅 19:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: اهمیت نداره که چه DNA تو بدنته یا چه چیزی مصرف میکنی یا عمل میکنی، وقتی به عنوان یک مرد به دنیا بیای هرگز نمیتونی تبدیل به یک‌ زن یا جنس دیگر بشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/131642" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
حوثی‌ها اعلام کردند که جنگنده‌های سعودی را از حریم هوایی یمن بیرون رانده‌اند، پس از اینکه این جنگنده‌ها تلاش کردند از فرود یک هواپیمای غیرنظامی ایرانی در صنعا جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/131641" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pluuGgYpwd3178dBP9XJMFRQ9g0iCBll5kqQJuCVop6a-uRyNX_yitjpEwhCHE6ymV2oPCvCijCJPxeSZ12W38QDj7q49-NQMxBlT6G87JKFkYT8MT5wTtHGtGRFqCPb-w_mQU1jwNWdJFkrjeAByW4d9658nLUEU_sq06nhm-otwDiJPEZnH5i9751K4N8AL7rQRwQtytksR7G5msLWxeCgblJ62rrzRIAI0pze9VAUxUECQRnVQSdcWs2AX574fbB5OboWpaipKv_wS5E95xy_RjMZoXi5vZnZfT96Tk4nYhiyCgB6Tq58V1CYG4yh8vX4yk-6BvSlCFLwiZGTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل، گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/131640" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگویی تاکید کرد که افشای درآمدهای میلیارد دلاری اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا از حوزه رمزارزها هیچ‌گونه «شائبه یا تضاد منافعی» ایجاد نمی‌کند.
🔴
بر اساس گزارش‌های مالیاتی و افشای اطلاعات مالی که اوایل هفته جاری منتشر شد، دونالد ترامپ از زمان آغاز دور دوم ریاست‌جمهوری خود، حدود ۱.۴ میلیارد دلار از فعالیت‌های تجاری مرتبط با رمزارزها درآمد کسب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/131639" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/131638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
ویس لو رفته از ابویسانی، مشاور وزیر آموزش و پرورش که دانش آموزا زنگ زدن میگن بخاطر مراسم تشییع خامنه‌ای باید امتحانات عقب بیفته و در
جواب میگه خامنه‌ای و مراسمش چه مسخره بازی ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/131638" target="_blank">📅 18:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJGSzxA6cKsK7mGcL8dEIpW5X-LwZtZhcg6KVsoFWjxrp_cJFN1WIK81bocUX95kMc0_IPavf0gxny1qb6jhttsgmoAwMbUGdmY7IPCzsW0EjIYrWg62vP0QqdhBYnJ3Hq1kbqSuWDJBGCwzjkhQfq-0qry-7g3boHBYRu9zowv1nWFz9Jmq3CuW0Q7fhVfr2qdUNA_XRyGpLw95prwsgQexCOaUB_NeM1skuQsjOHUpR7nUD2to6dbHQ3S-hojSQfZ1GCNDL4SlxeETMhc8IWTA3f9NCawXsrzOv86ofo5T_BAvINSCuDCdabZBlNfk2u3VY1Rkr0e7PHzZU6Eh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاه و تعجب عراقچی از گریه قالیباف که مورد توجه فعالان فضای مجازی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/131637" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دونالد ترامپ درباره باراک اوباما:
من نمی‌دانم که آیا او یک بازیکن بسکتبال خوب است یا نه. من شخصاً شک دارم.
🔴
در واقع، ورزش مورد علاقه او گلف است. اما او به زودی در مسابقات "ماسترز" شرکت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131636" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور آبراهام لینکلن از سوارکاری با اسب لذت می‌برد. من هم دوست دارم سوار اسب شوم
🔴
اما وقتی از اسب می‌افتید، من شاهد اتفاقات ناخوشایندی زیادی بوده‌ام. افتادن از اسب اتفاق خوبی نیست.
🔴
بنابراین، ما یک اسب پیر و سالخورده خواهیم داشت که بسیار کند و تنبل است، و شاید من هم سوار آن شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131635" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=X4aKGPPeO7o5aA85pZ-gGWGRRpfJhqpVc1qVIZxgAmGbmrl-umT3J4TC3hnRl_x76ojDjEHL4TUK2zexfg43Ti50HGg2hmBP6kLodOvsFJaOK1MVFtTNZlLx-xIaXP3cww0MM-onUFVXw7YpBP80ZkkddnlRdCOhQ9Jow0DpxlkkM7_AXUCNFaRpvFhv5SKFpfSmyi2vQWYCyV7b3kdqHA_4W02k5hvHxo3rLS--GrXHE2T5vaGknFXwlTqHBV_87N6HHuDAzF1vI9nuLKmYG1CUy_V3_8TxTYCyKcqjnakZ_jAEx0QCfz-8nRlywW2re1cLSEgNnBQO3JxDgo2tmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=X4aKGPPeO7o5aA85pZ-gGWGRRpfJhqpVc1qVIZxgAmGbmrl-umT3J4TC3hnRl_x76ojDjEHL4TUK2zexfg43Ti50HGg2hmBP6kLodOvsFJaOK1MVFtTNZlLx-xIaXP3cww0MM-onUFVXw7YpBP80ZkkddnlRdCOhQ9Jow0DpxlkkM7_AXUCNFaRpvFhv5SKFpfSmyi2vQWYCyV7b3kdqHA_4W02k5hvHxo3rLS--GrXHE2T5vaGknFXwlTqHBV_87N6HHuDAzF1vI9nuLKmYG1CUy_V3_8TxTYCyKcqjnakZ_jAEx0QCfz-8nRlywW2re1cLSEgNnBQO3JxDgo2tmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بیل کلینتون: او در واقع آدم خوبی بود. من بیل کلینتون را خیلی دوست دارم. هنوز هم همینطور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/131634" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpUjqaH84P2KH-2mVZKsN3VgAQNAgXoPcgl48Y1dJxQia3WXi4-UCxsz2q32XX4GPC9C2KvH_9Jv3480Q5rkYZjr1ea5rm5Q3qDZ3Ghzwu_HGUjMWrU-1n4LntJQIfbZ32uCwedbeSz8mjQ6KrE3i2uekxFSXlFJTwCCj6Nwz6xN1CudIedLGhTdvJCh0T0ArixgQtb1cfwUNK728RT66v55VMK8iqb8H5P1KALvwOThtsgCTiJNivtSDtU4N2aaMEJq_E18uvgBHBt5fWngmtKgXvSkr5jRppuXTMGEKOuVkOWOn360TE_nwjy_ZAn71URLkJbOaV3Spl_jKtqNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تو این چند روز اینترنت رو قطع کتید تا دشمن سواستفاده نکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/131633" target="_blank">📅 18:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131632">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY1LMFHv3Nx2zNiyDvJmQv5pol0mwFtb9GuLjWdhffXaoQIWqfPlUyjpUuFIjlgBcZSFpLq_CBjAb3SC9yFn1hg_GzcDXBe71DyGkeVAGwKoo-pjlYFT5pfcX6oCNHs5OZc8BIrXZkNhyDHhriQCLh2QdNqSZgap-QyMUZkzSBu95IL_oqtVtNplRRaP4_9Yc4M8PS2zt2Ftko47BndLhftBDcxml4XaMKwQseenBL2h9xN2Z6wmkbcmsj7-NRwwwhf273PLvxNpvECYQNWU_pE9VuP6iNVUg4WuX7gxglbWlbZCVi_m-GuXOHKXjKXN2hVTezuL-TJDBmWZ5yBiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس برآوردهای کارشناسان، هزینه جنگ ایران برای آمریکا می‌تواند تا سه برابر رقم اولیه کاخ سفید باشد؛ هزینه‌هایی که شامل جابه‌جایی تجهیزات، خسارت‌های جنگی، استقرار ناوهای هواپیمابر و سامانه‌های پدافندی، استفاده از موشک‌ها و بمب‌ها و حملات بمب‌افکن‌های B-2 می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131632" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
🔴
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131631" target="_blank">📅 18:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=K5NPbt4a7VIb3kFvjJo_hOvsX2h5elqKg3fJ9w5Db3QM9vvN_wPSaowkJrLqeOqgOD5Svb2V6wa5NuqPdzG7MFcgl-WJDjTvAbjJGPWP9QKbxBAnCzsvl25IBFJ6Uzmw72HBhz8DvbVZkccy96ezXpuZLFdQPwrXQfok94U_Q4bgHvEauRFF05GenQsmXlZg7hCYjcpOiBRihCO6-4BBIlw-L69K6_4Jlew3QQHy0cZYF77cSIGRefQCaTwEwlGfTaeodLmEl2hkmZbPJ7Q8OuKYDzjVbHqQrVXK6BgfGb1RdRGHK-zsN4J6jwDNsuQff-_3xVmE5qCqn5WfQZTe4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=K5NPbt4a7VIb3kFvjJo_hOvsX2h5elqKg3fJ9w5Db3QM9vvN_wPSaowkJrLqeOqgOD5Svb2V6wa5NuqPdzG7MFcgl-WJDjTvAbjJGPWP9QKbxBAnCzsvl25IBFJ6Uzmw72HBhz8DvbVZkccy96ezXpuZLFdQPwrXQfok94U_Q4bgHvEauRFF05GenQsmXlZg7hCYjcpOiBRihCO6-4BBIlw-L69K6_4Jlew3QQHy0cZYF77cSIGRefQCaTwEwlGfTaeodLmEl2hkmZbPJ7Q8OuKYDzjVbHqQrVXK6BgfGb1RdRGHK-zsN4J6jwDNsuQff-_3xVmE5qCqn5WfQZTe4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایا: تصاویری از حمله امریکا از خاک کویت به ایران، با موشک‌های هیمارس در زمان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/131630" target="_blank">📅 18:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ارتش باید در هر زمانی که لازم باشد، آماده انجام یک عملیات مستقل و اسرائیلی در ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131629" target="_blank">📅 18:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی - دیپلماتیک اسلام‌آباد جواب داد؟
🔴
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131628" target="_blank">📅 17:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=AgwY3DBe4KEPVlv1xiTimngV8ofj4-8q6FFuEVb3079Ese5seDSpwcvdVJI3HmbTT-swG9eEd75kJAFi3MKWet7zwfMTwNvfWy5fn4FXpPdJ0xP6U9e66GNI34oaWQZ4JqoV-0e-5DnQZFdiTNy4XALajTOkWrNuDm7sJt545UVwmLMDZFJtGdJdBg_b3WmOzhQOGEldUjxbj2a0KUey_8iT1jC0zPPDlRCYC3fSCaN-c2V1RAxPn92uqLU3nxJxmazqDY2XcRPylWB_7TMAjgDuiomwCzyhN4OSUceN_RjreBh2W8o9bXzzoPqqJywyJIIp-LuDnEIBQ98ObDnbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=AgwY3DBe4KEPVlv1xiTimngV8ofj4-8q6FFuEVb3079Ese5seDSpwcvdVJI3HmbTT-swG9eEd75kJAFi3MKWet7zwfMTwNvfWy5fn4FXpPdJ0xP6U9e66GNI34oaWQZ4JqoV-0e-5DnQZFdiTNy4XALajTOkWrNuDm7sJt545UVwmLMDZFJtGdJdBg_b3WmOzhQOGEldUjxbj2a0KUey_8iT1jC0zPPDlRCYC3fSCaN-c2V1RAxPn92uqLU3nxJxmazqDY2XcRPylWB_7TMAjgDuiomwCzyhN4OSUceN_RjreBh2W8o9bXzzoPqqJywyJIIp-LuDnEIBQ98ObDnbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر وداع عاصم منیر و شهباز شریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131627" target="_blank">📅 17:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDiflqEMaZek6s6RqWhpEtmEleLEM8wvgZqwnFEGDLW8PNAyJB5LLkWvg9q5Z9XFQSlhV16hkZZH0gw_CGJi0-9_7vXUxOl7NA_zX8JrIKh2UY6Ejp4kC0nu7xCXnPUsQEtM1z4sqarqqmajceHuZrJJ85e-PdjTamT1ntSxkh1jJ4lJPBsU4vdlAzyUbwLEzumIp7O0EJ-ghWREDkvgKI0GFTK0Q7FWGRxJNOKfcdjwlWwsuFWy0g92IEZ4kaxoxDL5AQjYYwwB2qp9K3mrWtUdIaGTK-EOHkDgMGpGQkZVq6YGs0IXIDzaiP0Pf2DC0EPsHY8SIdrR2rxVDS1frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
:
به سه منبع ایرانی و غربی استناد می‌کند، ایران مذاکراتی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است، اما خریداران احتمالی به دنبال دریافت معافیت طولانی‌تری از تحریم‌های ایالات متحده و اطمینان از ایمنی تردد کشتی‌ها در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/131626" target="_blank">📅 17:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=YXP20LRYQEKaYk9CwoSd7ABpHGoqSZoQd6U0yu3mNHvn0j9_JvZNPiSq0Udmzj2WxbWnkVtDFV7R_HSLT8h4PdYjxb_y2RH2YkvxNSg473j82Ih1mCYN5_CGLZQDLmzAnzA1IoD-F87My0p5zFfwMVLIXnhjRAbVox6WDU-g91oeJUCbbgs1X6TDysiT644mPpBZKOEG117zKda5J7f4dejOXXTGTCRK-WazD7DXCOCUA3Lu3DNJLCj7YClDz8Y1hqH03UDW8mciL1t-g2wqQuR_TeBO1J9PxR6ZlVkD_b6MzIO_qO74JPRlsj_-8Qtor8Es9bvwubdc58IvKvLH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=YXP20LRYQEKaYk9CwoSd7ABpHGoqSZoQd6U0yu3mNHvn0j9_JvZNPiSq0Udmzj2WxbWnkVtDFV7R_HSLT8h4PdYjxb_y2RH2YkvxNSg473j82Ih1mCYN5_CGLZQDLmzAnzA1IoD-F87My0p5zFfwMVLIXnhjRAbVox6WDU-g91oeJUCbbgs1X6TDysiT644mPpBZKOEG117zKda5J7f4dejOXXTGTCRK-WazD7DXCOCUA3Lu3DNJLCj7YClDz8Y1hqH03UDW8mciL1t-g2wqQuR_TeBO1J9PxR6ZlVkD_b6MzIO_qO74JPRlsj_-8Qtor8Es9bvwubdc58IvKvLH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام دیمیتری مدودف، معاون رئیس شورای امنیت روسیه و فرستاده ویژه پوتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131625" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63e838adce.mp4?token=GAoFyGg6vNk3taIKVgM_gdJ9uS5slS4p8bvYoXtHQoAigVQoMQKDdT6o1SkpylPAsf8NymmnslMJKYCDcGcKUEi6cTsRkaCeLaiIECIV70osUhxG4zKI0p8sVwPQw-u3wTI_yyVVjvhsP3igXgLI8w__7y7PQ-q_dC3ldRD7L76M5MJxgPjtewtveMVcuYhFV6pfI1sqnLxGGTZEx-asykNKFOpbaSF_JHbB8tbe5dBS4fyeGAJzLZBRJ_xGpEe_tl42cBf2LLkDib6HI-QC3dTYCO4WUCxKyNmghAATumEs7prBbbaSiooO4Zvvxye6RrmghnlpUNSKhQz5AyNFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63e838adce.mp4?token=GAoFyGg6vNk3taIKVgM_gdJ9uS5slS4p8bvYoXtHQoAigVQoMQKDdT6o1SkpylPAsf8NymmnslMJKYCDcGcKUEi6cTsRkaCeLaiIECIV70osUhxG4zKI0p8sVwPQw-u3wTI_yyVVjvhsP3igXgLI8w__7y7PQ-q_dC3ldRD7L76M5MJxgPjtewtveMVcuYhFV6pfI1sqnLxGGTZEx-asykNKFOpbaSF_JHbB8tbe5dBS4fyeGAJzLZBRJ_xGpEe_tl42cBf2LLkDib6HI-QC3dTYCO4WUCxKyNmghAATumEs7prBbbaSiooO4Zvvxye6RrmghnlpUNSKhQz5AyNFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر آموزش عالی گوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131624" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
معاون اردوغان از سفر احتمالی رئیس جمهور ترکیه به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/131623" target="_blank">📅 17:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obXk25aNFwNlmqUJBjXM4aOMV5ew2gxGJGrs0rd6H1G9LSjRimCfq5juEt-aLRwsISDmyGk5AJcm6uLF5tZgj-0srXJQAbu-msA5Mcfua9XMwAatVktpAA4Q9wJ2FaQBDD6nlYjYLd8UzI0gyGVzkl5ayzvJ__51HGXNjV2D0Hivc8f1U6rCM1KUjHsnc4W2kncIllvm83te6RCQr7XL__sqjgkGrQM771FUblWLn9UJeUg-kmMXbBZkuqyL9RVe_zQpT-VO5dOtrHZVBts_-KRVZeNuuWn5O9jEqlqSC0WkLL4F-7nM_oK65fOw6p5daI_n81wezJAq09lIMQxR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز یک پرواز ماهان‌ایر جهت انتقال مقامات انصار الله به ایران وارد صنعا شده و پس از مدتی به سمت تهران بازگشت
🔴
این اولین پرواز مستقیم ایران-صنعا در حدود ۱۰ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131622" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رایزنی احتمالی OpenAI برای واگذاری ۵ درصد سهام به دولت آمریکا
🔴
به گزارش تایم، شرکت OpenAI، سازنده ChatGPT، reportedly در حال بررسی واگذاری ۵ درصد از سهام خود به دولت ایالات متحده است؛ موضوعی که می‌تواند ابعاد تازه‌ای به رابطه دولت آمریکا و صنعت هوش مصنوعی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131621" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131619">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز: ایران گفتگوهایی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است!
🔴
خریداران احتمالی خواهان تمدید طولانی‌تر معافیت از تحریم‌های نفتی آمریکا و همچنین دریافت اطمینان درباره امن‌ بودن شرایط کشتیرانی در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131619" target="_blank">📅 16:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=PM8-yYV7JvvhKuOPP_5di4gywmArKTabWsNK2mysOgVWoTItotHADWcFp9f9wZsoL88GwkAbAhHnrop1agmIkFOiKLfdmZYtGwJCTjFMae7QVP_XXvrOTV8lw3MaIJdz_UF3N7JPgIw0sHER1gHVyWU6hqEGxh_em56s8uLmsL8Na-7kSiDgh0QQh33fobqj_LCh8VYr0fPlyRuUKEZy-q1Pj9cjRae-rd6ORQrTNeaOi1Wdk2NJSGkweR6nq1MQhdqaNvBW9_6_ceIvIR-tcP8Pc-IwMSGDMNLi4T56O3q0MgeTG-E0RxImUuxAzvKMrs_4GB8At62a1sUqWxfvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=PM8-yYV7JvvhKuOPP_5di4gywmArKTabWsNK2mysOgVWoTItotHADWcFp9f9wZsoL88GwkAbAhHnrop1agmIkFOiKLfdmZYtGwJCTjFMae7QVP_XXvrOTV8lw3MaIJdz_UF3N7JPgIw0sHER1gHVyWU6hqEGxh_em56s8uLmsL8Na-7kSiDgh0QQh33fobqj_LCh8VYr0fPlyRuUKEZy-q1Pj9cjRae-rd6ORQrTNeaOi1Wdk2NJSGkweR6nq1MQhdqaNvBW9_6_ceIvIR-tcP8Pc-IwMSGDMNLi4T56O3q0MgeTG-E0RxImUuxAzvKMrs_4GB8At62a1sUqWxfvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر کابینۀ نامبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/131618" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=ajy3akPmnx8wQaIFOwgkyJSdKyEvHrnSQv2eqUX_8OrZmuQr00MEmWUyO6W0073y9Ety9Pq0K8Z1QYa98zDGbObGPzuwlTK_N6uLZCdjU74FC6kZbe5dYxYafidKRIeIRYWKE0XOTF34JPOR3MDxh8-wLVb33tjEmZbG16IyUs5jUfwi9WzpyXgawLzcM12hrq4erWWpyNElbl4uduPkPPf7ZpzT3MDjlCFul0c8TNpqYLnG341VIDQBfx7q1xDAZK3cFMTa-u-M78ugh6RrIO0Ga2eomzjWyQDtz5y5J6WA6BKjgLPLyAUUK4FPYrPrb5SjPO_NQaEJ5nW36GeEug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=ajy3akPmnx8wQaIFOwgkyJSdKyEvHrnSQv2eqUX_8OrZmuQr00MEmWUyO6W0073y9Ety9Pq0K8Z1QYa98zDGbObGPzuwlTK_N6uLZCdjU74FC6kZbe5dYxYafidKRIeIRYWKE0XOTF34JPOR3MDxh8-wLVb33tjEmZbG16IyUs5jUfwi9WzpyXgawLzcM12hrq4erWWpyNElbl4uduPkPPf7ZpzT3MDjlCFul0c8TNpqYLnG341VIDQBfx7q1xDAZK3cFMTa-u-M78ugh6RrIO0Ga2eomzjWyQDtz5y5J6WA6BKjgLPLyAUUK4FPYrPrb5SjPO_NQaEJ5nW36GeEug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیمیتری مدودف، فرستاده ویژه ولادیمیر پوتین وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131617" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2Jmr4mhoiIr-C8NS1z5wGdX4NfOEPBdsp5jWwB13pTcy-XIDsgV8xRwtMCpVv6QDrYD2DEoQVyql7wNYOqHHLq2vRYWYgT3ydGOpKdNd0N9MEU9aMplfdfRzVbqJ_YoANidDy5Ezquwric-Pd50m67lvFYNRrcxlFjtZnHPRJBmXiiXoR-hdUBw6PzvWyy-Xl5WE0Mh2uBmnPChJnosOnGRWQHXqUswVvveadq6PE9wnC02FSlPWKxN4YjaLVM4SlmR0MO9ipbj_Lddo36_SHqRpfADXH5affXQTAPcjnNLYIVixktkwBNZEeLY1oD-VnyZplAZr-0VlpJLi5bMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره ناتو : برای آمریکا واقعاً مسخره‌ست که همین‌جوری توی یه رابطه یه‌طرفه بمونه
وقتی طرف مقابل هیچ متقابلی انجام نمی‌ده، اونا هیچ‌وقت موقع نیاز کنار ما نبودن!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131616" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
