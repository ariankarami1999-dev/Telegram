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
<img src="https://cdn4.telesco.pe/file/fU4hspDVuP7VkSyKzlo_4n5Ie6uNIOzVeSOA-uFLhAlZvkUru2Xi3C-Qxe_w1tOpMNNKhA8HoJigl2rFWS2pKKjyjQTGtoNTEOHcT2a2b8gK_hlWHyiWT_2pDINJdMIeqEvSAhl9vatHwOrp9UxdpM_GOImoHGUbkPA0cAZoIyPmmww28GCK19TK-eRN4Z4HzZy-OqPqGh6eaVV8cuzA2rrmyFqW98qD65lwWxFzAZ4FbPSE824xLn8MYg3tp9w1tFuWqkT05yjXhSYAxvjEeFxOwJLhER6hjGnf27V3vryZBJN1exlP5Ws-hUZ_Whvfr5hzXLWJ30lgaYFv9opqYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 19:50:17</div>
<hr>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=gAbB7wrGw1gozurqZ3gJwDLzNE0OwTiXUEv4xf9HBGEFyVM22uhw2xqpxzhzxW2-reAhk7oM6fT0jc2r4g0AVWNUKkuPoHOZ7YLSxZgTMSzBL0OF0JClSYMxa8FM57IqdfaiNBgNRdkeH_JcskszHXkyGGrRy5AD-HbkTnNrSYDJEkRxb4GKQsDnx0UqY4lv32qLIAF2tFGru5-M1Nm78mJDThA480W9LNsogzk3QuPyrTKT_uNAEoF9vLZMn8-pNAsbDm90hGvAU1SEsdVOw94SonsfrG87PmTUK3Tfhr7inxjtuJhNpfBNxxaHy9h__CIFzSIlFmh4VPTruarQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=gAbB7wrGw1gozurqZ3gJwDLzNE0OwTiXUEv4xf9HBGEFyVM22uhw2xqpxzhzxW2-reAhk7oM6fT0jc2r4g0AVWNUKkuPoHOZ7YLSxZgTMSzBL0OF0JClSYMxa8FM57IqdfaiNBgNRdkeH_JcskszHXkyGGrRy5AD-HbkTnNrSYDJEkRxb4GKQsDnx0UqY4lv32qLIAF2tFGru5-M1Nm78mJDThA480W9LNsogzk3QuPyrTKT_uNAEoF9vLZMn8-pNAsbDm90hGvAU1SEsdVOw94SonsfrG87PmTUK3Tfhr7inxjtuJhNpfBNxxaHy9h__CIFzSIlFmh4VPTruarQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا بابکو که یادتون نرفته؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/funhiphop/82328" target="_blank">📅 19:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKpKGTWIiveT6bGfTayKPajopHIuh_S2RrekqKr3eVWsNCmdzYOgS5yerzY56baq_lKyDVSRi6uUfWwKhgwySlUhF0QGZqD034YrmF9BRjHZ0pgkAe1bAbGaFUyvPg4xfYU8_9P0ZjG4sRNnAWQkBxp4AMlPhAEo1_6xFN2J_u-pjhmVAeuoovosBCJ6Vwse43nuPBfXtXjC_HFJSXt93gDSRJ1BdGXmQuumocOtjalSDwkM-j6afE97kgR-dVezDpJMkHWtPMsQJ7_xcsw62oTlDyQ7rcWsUIGMFjpsqXtdkn90FGu0hjMWodoBHw4FFhhxLYxvkqMY9y2_zzAEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای خدا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/82327" target="_blank">📅 18:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=KPEskAQxAVqgLXBUs2JwzVMiZwfy_XV0IuYqf7ZMpcglwa_25LDwM1urJhG7-eC7qnBDj914iWH_0oy21GAHwflYnqG_Y6LVNo-BjxvSAZ9UVVFJ8w7cfpyMnv6KMbGNRvT9OvYgou7TCG87uzAXljOusSKxEzYRPXjcfEW9FqS1rNR5S71yFanwn-21-YLfYhR1AT3cAO-iT3JF8AB2WEjMEZ20pY84B-ttkxbgNSQ51m8HLDXftdHpA1smVGDgPOBm3HVcNRCnjI7CF99C67VBrH0lEoLQoEc705i4Q195Ki6hoZATW3C5MMCoyj64PTxGVCCW0vTvBV5FQFqA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=KPEskAQxAVqgLXBUs2JwzVMiZwfy_XV0IuYqf7ZMpcglwa_25LDwM1urJhG7-eC7qnBDj914iWH_0oy21GAHwflYnqG_Y6LVNo-BjxvSAZ9UVVFJ8w7cfpyMnv6KMbGNRvT9OvYgou7TCG87uzAXljOusSKxEzYRPXjcfEW9FqS1rNR5S71yFanwn-21-YLfYhR1AT3cAO-iT3JF8AB2WEjMEZ20pY84B-ttkxbgNSQ51m8HLDXftdHpA1smVGDgPOBm3HVcNRCnjI7CF99C67VBrH0lEoLQoEc705i4Q195Ki6hoZATW3C5MMCoyj64PTxGVCCW0vTvBV5FQFqA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ معلومه سگه پشماااااش ریخته
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/82326" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP_YZx5h5x1BCcmJD3AZiWafuGGHSWeULQ1YLHX1l0wysmLGke7OM_8tfMp7g5gpy1N3epN1T2dBFgAvMP-Hkf0ID1zYHys-eVzBrIPKJIySej88x5n9MKZmDevoFcInqeq9yr8r5pyfrHsIephAWVPXPvZloCw1xxgxKFHwBbIdc7-llOaRjKpBmn4jKPIPP-vbg9UCkY6qqZ3LyxlihVpXHX3nkCPpunU4wWJlXwyEMrnRSeUdVyKzt6CSUGOQkJVonekwVS80wqDrKW2RlkDFlRGR6-wtYRojd_vcLQ2S8oUuFftQz660ZQPpmKm-gbqHAn1T3fdrkFRButTATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQu0-bvoq8H1_q0rsOSpAivHee-PSs1klLLKuxTLEV6wvZDDcAKahqT3IVdKxHaKWJJAYHgnJERZEShBARgAV9Qnb_xmbIjq62bUZZV9jPSO1jz4RZfZHl_Olr06rJ2GMwqbTd6rERiiID9V5bShh6U17pa6RwvD1KcrRuTy0N8tqj6-SX_D6jqNcttrbj4fbVLAIox0j5S-8iZcs8rHZjAWl6tHT22t2iFSZi2ZyCEHyY3QRUa2WZqrlspl6hLHF-auGSynPYYh6wjRBcxF-a2LhfZpOi_wlGqDhWCf-XwcTBKzDFG_O8ZiXPDX2C63vTPcUVgXlLX8SBR2LC63kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جام‌جهانی با ما چه کرد.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/82324" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOBzwQOlUSe32jqUUC34nKE0d8ols-PZ03p5pNbIM7jMGHucEG3UDrP3XAebs4XEstPmSZQHL1ZhhshZ9ZEq6SpnbZ1pLfETE2wGkFZBuLms1_uFnKsPoEMwMqeMI7yzE4TcI_92Q3IgFvxebB0Lbi39k06TGdIE9MuXHnloJJlLOwwt7SDXLfsUajY-XV4P2RXgECpXmTAyVA0OgaPdlky1tRltiqFYSRYDQ3xNZhXKWJouwEy9gkA0cFxhye5fXT0bXwjUkOZIudAgrTfCSm8sWYU8VOnwVp_WyF0JpSKU3lnVp897mQ1Yj9GhtwMwdgeyh3B7Dw7xSF69UkIhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/82323" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شورای شهر تهران: به زودی اسم فرودگاه «مهرآباد» تهران رو به فرودگاه «شهید خامنه‌ای» تغییر میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82322" target="_blank">📅 15:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طبق تحقیقات جدید محققین، افراد باهوش هرگز ادمین فان هیپ هاپ نمیشوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82321" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD3KXhJcWBVVqLHUE-oV9qAL8_R0JiHYkqAbG4EEOuJdrnCiTD9HAQWeBLxnKQYc_XYjjCheKYjXYdk_p55f-ITO6oMl-UGqpowI3X-1Wo4Ctk80auWgPoJU2VV0pNL-9mTsMnR5bv7KSUhvA44qe8WjlV1GllDXFCrKrLac_fEW20TVtkCko-lSgs3pmmz9lzzaraAcyJzGEAG-9IJUfAm4qzKuHSFG0f5LGTxkHtnU-PyoJjjzlyngCFBkqnv95k0I1F1dp2LQVfflNcpJZIChdgXh0I38QQVgjEFqH51CeS6AzfmKImr6hl65soWG1r8yV1RMdfkJ87imPheBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی کاپل هاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82320" target="_blank">📅 13:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTNDAaGVUF2uOS_n3qAeGTuslbTJL_LtucwvrdG_3l7Wzt_rFL-gcVgbluuoS9Es0_OVHAltgUwTiwIhhN1tSmlI5OKxZkjE_YCQGJ4HDvWKVgJyXG79TXbBWMgghTlkTI_oF2flPkUyKmT9FUCHuhsNWUaARBAiqFnMq8-vNdL3w2J3WEyE-xAxKs2X9s4yHjSgLNwX_rU17w-zNGAtMLbxQ2--p1Q9by_NdKBDrsbn50nRDiFEY8XAu9bjohk2vJl_jv4GWALQ6TwQSS515xp3YrRu2i49Xbyo-L8aHFOZofkmAjM_ByBMe54R-5TRkuRGb8jpHCDtPb5Pzlca9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۸  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82319" target="_blank">📅 13:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombRoKe( Leandro Trossard)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAGfi3yPmiCiL6j8ZTypn4IFnQLbnDIyoNOGBYPK_PwQCb5oboT3U52fRAH5pxEjSjFyo0CV1TGP_uIIC_xLCyGKl23eyeSwNMEqZbMk4FJSjskkXaggyvStzohBopSUhqjWvhcQXlllrwWoa-lAhH4QPrZOS353t0cFqZI396Lfby1KYj40Bc77ToXDvLlg8QzUuM6P8SvKB9FDWzJYJsZPoSQS8Zdg_qy3BAxlOqJLbAg88xUhvAcS50-Td4JuU0i_UxuhVyJZsZEYrZ4V0GBOWctmDKqz3GPu-gZ39M1PQ2VjeIiXMg0WgLqPrl2SAAEaptu3IgB_u8t1TtV2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه (رونالدو) رو هم تایپ کنی نمیتونه بگیرتش
😂</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82318" target="_blank">📅 11:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1Kd8XbUXkFkSZmyGviPUKUVD_SVFQlBci6ZqK8jbg-McITs7j3h7kJ4V7RwXwtgPDsR31K2UVRy4lNO_hZc7_DQp-0pePJ2k6ppyH-uTt4J1d90ur4tcbG5lMPWbFFSzBOdy8Q3AqBSCqTxFcyYmTy-VbxKeat3KBS9ukTHz7RJgzE7Dm6w715Xyve6sYU6-joaUbbxdAdAPY_QDZVMTxoonlIx4-w7wN5gGrhdBLSxZuOOC0dViKblp6Gbt7GE4YsPWZsWJPInTOOMLGQyn9S5EV1sg-CcRZAWZ99CwqxS6KSVR2fWM7xfGxHSuVC87u8B_QeaqlhqSd_wAUKTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه «مادرید» رو کامنت کنید
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82317" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEcKen9UCnhRrbIdgqEliAFSJL7IIONlYV8SbqunYmyXCuTbsCkPe9qHal8M3Tzra2SoVv9FCbKBeWU-LQXtFRptA4uOErB5-5ubK-T289espOexet8lsvIArcArrLd60UW56QoJpIze-b7AmB35A2rUU33IVEBibBAAEioFS_A9JteezDp5C8sdKpa3nJqFoGDeW8Z4jgpMAv0hppKIFYSB8k9tfLBlViVmfpqRbkKJoxOEgrLv2bjSL6_Wca9P47llaw2CbiTB9G0HZy2MyUjulvoV0KiZz2tGV55PUr-SYJYZkaxdq4vqyqw1UjfvBdER6hMErfyuVYjtE5iYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82316" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترکوندی شیر
👇
🫵
🔥
🔥
ماشاالله شیر
👏
👏
👏
👏
و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82315" target="_blank">📅 10:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82314" target="_blank">📅 02:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=QD6K1JA3AOoVLhq8fjDxFr4FhxUF1ewaWM1BSn3eXXTvq_nUOmeSCgVBl5-Zynmtdi6PcgSPkKuHovx9Uvqrz0MF2p5-zt9QbBOA9hP0MEBSpnFCVCfM0D-fdB9P6_uqCPVfB7TxfNelPa3PnKVDqJWoEg6_a8AE0vBjcmfUKY5dDcPdeqXsCkjDaDprbSZPuQ9G7F2H0zazie9GulZ0unqMrqG3QSMOVw7V3XrkZ9PPbZoXKopH1C_YnaGO7AN_l2-eCwLtA4gK9EIcQ6WsR6y_HmGoCPUg3zsOnHtIFu5dFoWRzubiti-mYHPQSN-yFZl8JAQ8HpsF5iDD7jB99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=QD6K1JA3AOoVLhq8fjDxFr4FhxUF1ewaWM1BSn3eXXTvq_nUOmeSCgVBl5-Zynmtdi6PcgSPkKuHovx9Uvqrz0MF2p5-zt9QbBOA9hP0MEBSpnFCVCfM0D-fdB9P6_uqCPVfB7TxfNelPa3PnKVDqJWoEg6_a8AE0vBjcmfUKY5dDcPdeqXsCkjDaDprbSZPuQ9G7F2H0zazie9GulZ0unqMrqG3QSMOVw7V3XrkZ9PPbZoXKopH1C_YnaGO7AN_l2-eCwLtA4gK9EIcQ6WsR6y_HmGoCPUg3zsOnHtIFu5dFoWRzubiti-mYHPQSN-yFZl8JAQ8HpsF5iDD7jB99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: ۸۱ میلیون تومن جمع شده برای کشتن ترامپ
ترامپ بفهمه براش ۴۳۳ دلار و ۴۰ سنت میخوان هزینه کنن برا کشتنش خودکشی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82313" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlT8JqelOkn0DS_W0fbUv9nzxBkKHWlrEvYbxoNjP0dPpP7oT76Zxr1AaOlxT6KZpRNgxWHBjdYGqRwGJrUhoU__iSrQdruK96meo99v_TCsS1WIRbY01_lFdnUZLCVVljgXB5iTPkogjb-Qo3eQGPAJlxUkheWbnTRXBA_N4W8Ml2Ifp2sdEfoQ-vXNFEqBVLiOMobHj73b1kioj9wC994Mg6brm2GrbqWu06LBn_81rjbODx2YVTTvXsD-y2pTzrsSq5-1jNycOXuRVeUnjZMGuderB_4zTu0-XuJehuQVlU0Fsi5S31UYrLn_LTL8Io3KtBim4UtwzqOK77j7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم جلوش شلوارک بپوشی بی احترامی برداشت میکنه میزاره میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82312" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رودری تو این جامعه ای که زندگی همه وابسته به فضای مجازیه هیچ پیج و اکانتی تو فضای مجازی نداره و هیچ فعالیتی نمیکنه توش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82311" target="_blank">📅 22:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqso8pHKVGv4X1z6O9QMtHsVDebyASJ2kZknfwch8Hj6zq_Wud8lFtvt-vnSw7E9cO7ne-Vv-7qWplh4dXB8BTQVEAxK5Znxf8iDI4OowNmKpjqDQ6QJT-YiDZxuILkerXlUGIbg8We5089xrGGpB78T0qV8YYKRDFsuCQssf4Ex7JI4GSBwNf_IkOawwSBsXXxBJVInYhjlZQveqO7cbcDxvSadkvISJoSvFA-jE02i9sxlruFlJF-DxtUXeL-hXIHEpkGPX3MBj7lUTxkbLvTGFZS8GvH7UznQ17LeYNQnlKPHaD11ENrWp53JJ0lxATmra1Qa52gohAjQHG5TmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی همه جا مالباخته هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82310" target="_blank">📅 22:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82308">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTaxrHwvjyDIX4VnDeoBIn-ocQYNw4_wgkYTQIoG9sqsVqcjJg0YmU6Mlue7fjaWgNnVV85WYUKy8eazOu2bRPmoy7RiFHDXxHESIUhL9wbE6hO_utRUMm12TucvHWyrYZvxGTt6r4ZQ-YLGQZXamBrRO_M6wqwvdxLsnaU17nrS6pH10vPV-6utltvJWF6heBBYtzB8R8c8-HgQ4BESvdeQvnGNDUDYKy70DYaydRgg63ET4kk2hdKdr8ND9w4cqKQNkNbboYDhNN-gyrmtoEIKFE7VzT-frKolCwx6Jr_S0XBxmrU_M69qo4iekZ0aSsEXeR4VI1ubJftV05zSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7oYtnNv3ojmAxPTyBNjXcmPKno_w2b7KDK-BW8zwXS4rLndtgxoOjCJypZwTtirIdidqeb2-WvvvRt4ZNw4-rs9med9DX3Ff0Ma9G5g-GxdlYAtN0imgQI2L2uM7bClMdApwYOK-E8l8drYPLItyJHij9b0VOvvDPr0Ox3KIhmBW2r_8Pb_YgxDGfnbrc5psisCeBMxvu7d1s2atiAPPrDtqqOsKEfpb1Xp4Qj9FW8C6i5YEqp_jJyYm8mP8SMWpjnTE3YElfShLNe0X5qCr8PnbGFxhm2eTFgz49S5QutUIJ6MFoVZLRCHBRs46xR1SVX1pJFMqVUNnLmt97V98Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونفر تو عروسیشون خودشونو شبیه شرک و فیونا کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82308" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اسرائیل مثل همیشه جنوب لبنان رو زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82307" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82306" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82305" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ9BmZ_xJBIUu1aMWFzdj3R6vlIYNX_za0DQXR3Q49n9KlCSHxP0d1ed1IfeiHTAz9HDh15-uEro-8hkFNH-fWfH8HhG1oQwKF1HE_FD1VKA9vaTlTuy21vJY2iUjWXdeH2Hk9QlIXGiHVZl9r_X0PuiuXXCjSaRVWjuPzMjDyXCSw5WNmgjcpZDt4pYL6f277XfCPUmOFlgWiUkAgu8d1q-yJCdqSbFWB4n_ki1CloUUeCRDXIt2K6LyZdWsp4lAr2AToZRuu2tq0WTU-D8QM7WdqApHWNextWFlaoTZOVueP8eWUXtcJumREEdwsBt5LlNjE4RHfGHiGg9wRsU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لرا پرچم بالا
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82304" target="_blank">📅 17:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr0nf04b_sQ_sU0kpTIQISnf0wY12jwYZr8cMEEND2Dn3v4Xee6dsuODeyqBepEgUFyK7XLxDZK16uVQaqPBdw-463D3Ygq0dox-vXEd5IzxQ1sKdwypaAgQ3pZQ2kR3XXPeUbrvU-2y3NFLCX992qDd4HRMtoyyjjT5myxSXVd9jxdHcMKSb6hrr7QlG0-5WvMBJxi8Sd_e-bv5jK7fxrlhvrPVdO893Luh9_SjkPTGIdMtc6EwFUVdXHFr8nSZK9Q6Fdq_UYu1uxOR-VsOuQJ4mF_3334BTUUOVVmucYBd0E7Rf5HOUaeX5zd2tyChXveOfOf1UgG7GOM1voefzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تجهیزات و پوتین کماندو هایی که قراره جلوی مجهزترین و قویترین ارتش دنیا رو بگیرن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82303" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=CH2ti6SBQzew9Pe_6a5FHrdDTblqkTIZ_Aq4u10-nXy7YF9hJGoedQrQ09zruNo9012i5c97Mr_jCu_V7AGTZ31IqU_Q6Q5KmVB4nyKQlP4MospaW2gbNqtKxAKh_3GpzJQykgknrVQTQEadOpbTka3Pv1kcyKvGpnuTcOM9NMlGdaD_2s5SCV-HUCENPjQ_8SZ5tUTzl7yC5Xsvmk-vt9wo6L1mxD6-5I3XS9ZEW1nc7lMafc8GbUbRUQ-x_rC_jfFOJIyG0Pz3tmpVfFqz4yk8qT-nK1h2feSdLSQsBdqvrFtpmu1GrKo0SKxPagHA8U7AJ9W3eJgAsNdU_TFwPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=CH2ti6SBQzew9Pe_6a5FHrdDTblqkTIZ_Aq4u10-nXy7YF9hJGoedQrQ09zruNo9012i5c97Mr_jCu_V7AGTZ31IqU_Q6Q5KmVB4nyKQlP4MospaW2gbNqtKxAKh_3GpzJQykgknrVQTQEadOpbTka3Pv1kcyKvGpnuTcOM9NMlGdaD_2s5SCV-HUCENPjQ_8SZ5tUTzl7yC5Xsvmk-vt9wo6L1mxD6-5I3XS9ZEW1nc7lMafc8GbUbRUQ-x_rC_jfFOJIyG0Pz3tmpVfFqz4yk8qT-nK1h2feSdLSQsBdqvrFtpmu1GrKo0SKxPagHA8U7AJ9W3eJgAsNdU_TFwPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صداوسیما یه برنامه جدید به اسم «با عرض معذرت» ساخته که توش ترامپ و اعضای کابینه دولتش رو مسخره میکنن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82301" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8qYMlnmEnbfAuGC_5cXGBQVuaPKKVzfAgWn4RGJn5dX79Uymyc9Z_RMZAJHmsIRwIdw5QEm-pLkKHvRZFA3FZP4vWLhc9cHuq8lC5VX3-upwSsHAoKZs76XqfvfBj_i3IHU5qf5aE_jzlR3qi6U7z3CsfxvO2P1lsD_H4UBFGwl6dVVzqNNU0Z6tpOxano8nYleSgzMetxBub_HY2UXhneV3RPhrRLdsuFhEU50DSccKvI-Uv30C7X304zwOkR9d_SfdZJGRi95uqZ9mWacAOjX52ranFvkXw60EBnHOQmxSRgyWbQt-ZonbypiVkrKilublA0dDl17iLiI_rcjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82300" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شایع این پست نوید محمدزاده رو لایک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82299" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSAycQOKKjkEsCa1HGU5P1jqICEX0T_EzvAIDNq6SYFNBDnHyrE8BGSckV7aUAk6RnzVQlZWMoDrp2sQ8cNC_njeJ4q4hRK8agbmOa6PEkqWqPL9MDQGX13XyY2lfSTlHlx-dHMKiyci_NjBu2jiprLgfvLdxdMZh0BC8u44a9kt9j3fwIu3EJiYY1VYHDzy-7CwUTe_K48ykUGLJDM0n_ZNY1SZUjxgGhOKNECPoVTe3kqeXUo267-VU9lrkySL4JOJ1qzrYz_VH0pCeWoGynWeLiQ0ghOzPkkHRUI2bMT0qjKAGF5dG8deDt1lSkVVB70A4wUs-DrR6OMtVckH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82298" target="_blank">📅 15:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82297" target="_blank">📅 14:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETgn0BkeoT-U2zehEYisI1lbxO71COOpnbchJDQ3zGnHt-Ay0MSmTuvXTO3vZ_6XbGh3Ur-6kNyJF8Q1jfuabTfhv-dw78VwbF03UlvPXjtL_hYSVmU9BvOxBe4XjOIJcOax1DpfS4z77J9yhvkW_IwcZSfV55iGBmszBaBM5Sv0rZax2vqSjXPMNp1fQC0ftfgCbuqR7JdlJ1xY9TCoHlOBBAEzx4DJcUqL8NHu2fSIC-tBUJ3hmF12EoCzf74f81Aqsjt7DRQ_YI7Xo3wjZeP_DqPIlDOcSuukX6vveF2-r6szV0SjAK7siym-sRMxEICugbsFkeMP5tP3RB2miQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82296" target="_blank">📅 13:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzYiphZ3IBqcXwaM2VCfocNYeGBjjJ7IbCWFDJMG1M2yj-GTAM3-yxvr98FRkHNxCEib3hybdqILCoWGUJtkv16J83M3AnHEf4U7M66NfNw3V-o7OK_F5cfiGmGgdbKFwerFxPwMnMkNVstXNqLaM-x5aY15HjWT4Mf_eSEqzgbQbiq4G7ya-AVNoL07L9qXRi88yBLBgcb0-qh7MzcfT49rtMuLJ0i8WDnkDgawS5-HTDwdQhOfQB7MaL2Hx_CCqLUfET094_lHM_DmkZGk8NFP4mBSBf7-bMzbK_0kKsn_VKy86CcT2BUoi1hfvJGNZXS2YgpTfzgpUPPCeXahFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیون نفر نوید محمدزاده رو انفالو کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82295" target="_blank">📅 12:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFGKU2rhHBByYxwF7Qt7mUuchf1UngKJSMHJ6tcp73eV_koYTy7KJsw5Y0ihck33-wh927O28oqfjwyXzmLxrQ40R43VvmLw3Pcalfv7xJIMRo9_iOPBgTcpf66oSphq7B6iT6du7Vqbmm2EwpBslbiYy6vcFrEKgFjBkykw1xxPq0Y0GZ3RWULxUXkJZy9fABL_2Q3vr14uLYKYTL4LOZTCMJsPXU61YKE8tr4DL5LLH7MWz-tB1LNYDBGd93nsmGoaA25U3ZZu_EJVktWUM8ePLGYv7YtZC6jAUIkWX0V1krXgW_G1Zgrvil01kBQX27Wea2Rn3tYQyk2LTV-rew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82294" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHXx6___OQvBeRvWre_Blh8YC3Pc6kOOBkxNsPhHK_gNSVZseGBA9-6QnxfgN5-Jyu-nKsgQwvfO7itzldAosFHTHNHWmSBKEqvXeVYq0V_cfJ206iI1qWif0owKtRH8xcDj4--UQ8t8mky_QBIU5IvcAh4z5ISn9KYoGJ4GDfc2kzCECh4U-5nGCANEKYHqquykI5wYBq4_-5T5X8LDEQlriwiTE42KDWaVattNLQOTS8jzJDvCQ362l-DAvcRf1B_uCIZuyxp4g1ALEQ93J41zbVQ3DOMc3qYjjsuuBDWq8cZ2VDmo558xHP6ASxJgEp6odqutLyAyabM-YpZ3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو : احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82293" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVVliLYfdXN5EXmKUwbFnpj0stLkgoCW6POEBcmmmlAGQqeFLEr-xVblqOCYb5bMmjFG0L1tXynzGtNlNEEWF0U4pnEfSuiEzlZ032B-jcGYB7Fju2vUFj6tUIRTOztVrC5KkNlkk4G-R7dpM1t7AzYIowaP6DiuS8UjrUZ42wj4lWIeAfbq3IArypKw0ujGutwOTKo2AKmv4Ewmwbh4jPpEFmRiYZArUHtPJUSxixvXc1EXRTRnD9JbYfWgP1LlEcBUY7CCrQ_wMaz8fwYMGwmtUmZXKTU_mupB5cLgGd48Yw6MPzgVZjMFpXwpFlFNbFYUIGICBo4QXFmasRcYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82292" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoDKQQwTKxd9Z5KJfcSI9BPd7GeEo6P07Cj9WZ_-Q968QyrvFDL8kFAqfV-IxOeuJu6fHfnCoQvfYE_H__HJO49YhGvW_-CRmiswf5VDJNvJ59IOSiyynsnhDMt1vfI4MS6LH8rC7cQ3Ji5Mz3rMaZsJhAKCc1uycBWhX_rUYas1VWGYkCz_YLrhdzhgp1lPcpOK_nvQVGbAoW9k4DTUjX3J3CXhkCJgs_UihUGaxVBkdcx2uKABLdnrVRMBE1hDSmsv607y79A6UnrEXyFn7Us-jNBfD76PWA8ICsJzyShB6ceYKCetoiF_2N9wDhWxbHLZA7OCMZjdesfiFPX2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMk4AcwrrbCk2HVF_qzT6OPDSM--DwjDalhyPCNH-dwIjFfrrU4g9J6OJ4Ry0PJG2KGfxOURqZk6Bcxg302pjqjNon5eRz5fPkIvo0KFnpVN6qsGW7MbEcXLLWgiSu2oFn4R0nBC4sWyZyZ_26bfUYDVG9dLVeIo4NIo4KCMD99mRgSGiGa8W_XtNHRHTCe7I1qZyUXWsCE-HXPK28-YGOxjEW8mL6PCaPUG674pv1jzdiKii13sWaHqFIwWhAT0CwU_vv64LEtyim-6XEd7H1g95HdpgwKDLn9wbpA4yBXAgb78JHfYYTQBiArZqLd1Y0-dn3bX4qtK220i6qpnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZvU4oAuGaYv4s_u30AREmFgdqrJFlxy6OEJBks-VWBxY4VuoEuD9XNDUYG9iZWdh3AmW8xX6mUziDFdODZ4E8UWL-T_5zR2zAgaiE8_j6XBRelJH72te6UOZUh8L_7q0FTKnBIvieF2mboQrJDWOEaj18PgEu7NjyBbQqj5AsvX8MnOTKmCKJTUcXap2zU8mHu3Iud-e_ddpjZNIdpfuSExg7Rqgl9UT6WG8Sg_4GNq9y3rZa3XgZIXY46KCAcLxXISoUouh4tX4n1cHeegch48shxE81FPS3kjPl1nFJx9EZS2n-IZ64NVXTH3I-RyxQ8x69U2Om-dC2Nh6Gld7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVRFXinZGRWCKmNYkBOzz4qYXYQzJSkiFIXQlGAaM8FRnal5AQJJWZeHj3ArrXRNpGqbyUF5RDVEh4uyn_DP5in7sAPnBj3MUv4zdf-AxQsKXAtCC4wy2mv08SHFdEhBpKh1Qa4aL4rNqP3a-tah66mBt-_Vhma6zUkukK-3IOtQgjeAp979yuA--yGekmi3rQlPPvsL5GJRqVsp4AhbuEdGvgUMDHXCMNiE4O6oyIGsCrJxyMScabBBHcCr4UbWnZ0FHzbhpanuCRzU4Z2cw00q6VwTUXQGmlZ-ZSYo5OjoQEVKLHsmIByGii5_z-5eeDnYmtt_ClZw64biNW1vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=UQg0XQiKmi_gA4hD47_Awe7Tk1OACNI5jrc2ymBNcFooGufYwM1ufMYzI8mmCQZIbCBN456hlpVls5e6vFEa_Gf7lR2AzuXDOjzn1lKrE_Irf78YFePj5FUSfT-So36YxzOSb8stBrh6HjmzzguZfI5-bTHgZiNRVWW3Wm41QvoYUoknujEjeWJ3rvW37Wdq4vE2c_7G0cIfa9dT6r-5Wwhah4iZuQ0z-udM_wEIJUwj2jaJf6CHP7JFtXSBGhISAgA_NfSyhCakaAFHgmpurLo_rqndx-BZBJloaIr7LXncS2cZGFYcRQU6_DzmCAcWaJrYoeZPaxUfh9b-DXURq56JRxSOx2KMY6Pj4xgColSokaJgVzp8XgTyXLYGeuUIBD19VNyaxwTKiBGvNgcpl5oNcEmhvH2x0v53xNav87TApc74VpBBoOyOXEsmvT7pqKjx0zDPOaiYZM10V8cU1N_brfPlAKDcuwBBUJqvzQBVsQZDQHcmHjC4yyxf5VD_C2TcZOlV8bMSYtZ-Cb0hF3CXvoiFqeiQj_FmaDeW5bvfNBoscyTrMBmFQ3zYod8lKXHS_JV5T8wUXrvEruv_YCaW3nDuoa9DqgC8HRd83-YeXtqoK51fENlGJU7Fsbmck_aj688ZVrT-KQbH17GRmD7rkgl9w-mAb4MnvcRt9O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=UQg0XQiKmi_gA4hD47_Awe7Tk1OACNI5jrc2ymBNcFooGufYwM1ufMYzI8mmCQZIbCBN456hlpVls5e6vFEa_Gf7lR2AzuXDOjzn1lKrE_Irf78YFePj5FUSfT-So36YxzOSb8stBrh6HjmzzguZfI5-bTHgZiNRVWW3Wm41QvoYUoknujEjeWJ3rvW37Wdq4vE2c_7G0cIfa9dT6r-5Wwhah4iZuQ0z-udM_wEIJUwj2jaJf6CHP7JFtXSBGhISAgA_NfSyhCakaAFHgmpurLo_rqndx-BZBJloaIr7LXncS2cZGFYcRQU6_DzmCAcWaJrYoeZPaxUfh9b-DXURq56JRxSOx2KMY6Pj4xgColSokaJgVzp8XgTyXLYGeuUIBD19VNyaxwTKiBGvNgcpl5oNcEmhvH2x0v53xNav87TApc74VpBBoOyOXEsmvT7pqKjx0zDPOaiYZM10V8cU1N_brfPlAKDcuwBBUJqvzQBVsQZDQHcmHjC4yyxf5VD_C2TcZOlV8bMSYtZ-Cb0hF3CXvoiFqeiQj_FmaDeW5bvfNBoscyTrMBmFQ3zYod8lKXHS_JV5T8wUXrvEruv_YCaW3nDuoa9DqgC8HRd83-YeXtqoK51fENlGJU7Fsbmck_aj688ZVrT-KQbH17GRmD7rkgl9w-mAb4MnvcRt9O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA5gbuLw4LbhDeuyb6U-nHsqCAqZ7DAz8zWYTYK-dVLklOWwiSUBpaf01DxcWzsxVh5F7qMK-nmQ_8tGsgziuOf1pV8sQyhg3G1yzoSVHEmQx3CzOxFrnEiuEWeWJ89KgrTv3t_8Pc7dP_kj7TRfpjhReNjXiGHHqP2n4ReQUv5AO2b6JsxAWbsgZLh_U_pTbO5Ic6HIZpZ7FVAAl5cdJlo8nQVhtmBC3qEIi5eD7ufsSq5asukv1-JXBjnMzI_Un21toV5kuMm5uH_c5CALeczzCmGUQsp1rS63xymJgWlxKqUNePbu-du3_EXtLawHZT9Ipc6X5OOGjqz8w5sjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTFur3YkL7pSPsb8UU0kxuD_HV8-JzpiyidRFNpX3EQwBFY9FGfG5CK5l1rHAEW7h8zpLPwszKMAfcsnEAOtt_Z90ePsJwXPgWlgG9t5Tg0VHGkaRFZU1DKA3Yh_vzAqLX5kItIYN3uWCdmLFf3w1zmupV6eYxYVDZPkcwJFqA0OLv66NzOB2k62trOm7iA-j-urOoSEoi2ilUTCUrjpepQtn6_cpEvFHJJNeqJ9Fz1LpYjhb-mtOj3VlLz4EX2ki-dzbqDD96wTvCvZRGJHLiS1nqO4EGnxTXlyEA9kwGH4sbAPZfQ1pPqxlhd5Ml22CTHPZRBpDdqoPv6wm_uluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krB7vC2mhjBe6yZ7PBtEFVGnUHTLxF-tgZTLoq7Qcqyrhj7c-LaRZltOmF4m1Rw-_J5I4JIHBD9T0MADOus7uZ_oZ3RZ1H4nKeqpzFyB3cWi_e_hh5kT_m2GoY5E1j36PUlrb_uEUzObL4DQSSVNtpIncMR4q-kxF8ZmJciJ0Q3p-ERbNtORBtBr6OK_MX-aHJNTcLLjsZ_96oNLFZ0DMPpIcZRQ7YeQ1-xo7ORXNk0i2cO9RKowXZxav4L4w_yBf61XTIAN55vzg-wrv2U37mcezajC4eMxHapfdrCHKLF0Qk5PvDCnePHB543623FnGxIVgP1_kjV4U6gDCDMo3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSN-vvd3-UuIKTvRrqisho6ObJyaVUphjPbdgDoPW5bZdjQOCf6RBu1hfIYSIGkVmNhGhvqYNIcZz3yHUNBKMMuVwhh-Og9SkCWNPkQGEtDH4roUBKG7Y3XEp9ziaE8dXiqclXJK0nrvDHHZSuwVCTY2pLEAuHtY3Xt6QaUAsUJeg5m9JMZDgpcyLaxUqf8O6qZtCroK1aMEjPMB0gEskK6VkIxyr1IO0fuzegWea5Ryu76hbvaHg6-ryQAlnw73i2YsqAl7bhRYdTWZfalum0honxQdPQj9MyPynI8SnqcRESdWd5R7VgRaAuGBM6fIYzc7qzVkDL90cFWzBds9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khAj8J79eB6ZhhuaYtuSkeVgURmgCwRY87AKkxQz-pTxc0-HKvKlaBkRgCDVn-By2UwikiGorBUSIW3ag-M6ezEclOK6heDjcrgXlea4B9cCGBQ4TPCi6xXxI3MB4OV2EZTO5aXJ8Jrc8KmNl7NyV76-6sItYo57W1EDozW9A5IvVmiE85vCVMhWzCSASlKlUGX_t9O0DUJdxqjO7_nFFKiP8GrZBaeLv5TDnWh-i_UDPuLTaGfaqVhxWOPsasK3C56KA7pPYKqhhe8PPcevngUA9sKgsyIU3AQXpLh5aAl0aXZtgT96jo1UVfhSNhgsJPyB7qY_ZpNof32ZgYDbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqP_l3i77-G1HJDmB3ZPQoF_e4GnxKUYY3tlMB9FGlqCfOPm39ALn1FuLUtfXvQlJPvPhhbwoJ96gqNFNDbg7kkDbjx2boZuX8lBx-r2X9BMyRc6cEkuWYjdpwMH6wnpSv8FO_c8w0rPkVxrw47zcKFInnNiG-RnORh_ppIUPyAvVvLdHR32B-OS0qGOXBnUOTbC49RFIjS1VSpCPpVAgJuZDOhkyPSgu4LqX1KqJja-VtW23gdywzOQG1ymz7kh-l9Tk9l3F2wqTHwkK4I6qLG6YLV4eDHvJ4Z7AXHHIm2DMj-IosgoGL5bol0rWMsdrS2Os7SZt3cqtsEruLGoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g24b_1e7a9j4kYB6Jf6mdNHDApxEwdJLcppbWTeXeSh0wZSQY3l4me3YnAY04qnFCH4mLAonvfN3VL-gpgE3s9cKhmzf72LP5wW6UBwAKRsfQor3O0k9rd9titUwrZmpWzb0U1wV9UMVo6j9bm0yDxnIkctYc9QI7Dpx9f4upIoPF0_o-ToyvH-e16duJvjCg3lqtwvZovOt5oOBnLKIWAlfyNNYDhncjcWcAM0XoOm_2JldZKs0IDgNJPgfDBPwFz7wxs_axEyGdl_Qu_pdebRyTJCBVSU_Wzxg0wiQW_ugci1s0FWSTt6qgJDzr1gHv25S1j5nG9BIh1q7lpIWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3Eco9dwLCP2LZxPY3HQMfk3llbs2YocOiBHHEQNqSaFiFacaPqZIajR-3rp3JE4vh0poDv9HY4tylqvLli3a-6q0wmVa_Ims1vS78JKWq8KdocOaXBK2Q9GybgPdCZkoUNMHrsKg_RUjMigYFYrhpAHhh2hIOpdvA-w4OkBceo8YuAwbL6OodI6cO0KF1QgxvEI39K2jGJSUCzvKdYiIOCWE5MTAxsO9E92DQo0Hz5P8nQb31zgqvUWBndV0YsfcKacPu7nLhr3i1YspGtON2qOOIigQJdi9Rjj7l6RyKY6vss3uF9DDP5e_NrgWyIROt_94ie6X1F2AryLqAaa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=ITV0S8NopcTbF0lKEl1l4X_ygW8sHEpQpDV0ELhkgMQ4x4c2EWcMTdM3wrVYyyGbNwhjhrctF11VMMhs2B5zUy4A98awU4YtBu-CI9lG97lPiR09j9CeNWyVyJuT9VTu_n4_WPPjIM7uf7O8Q284IK7iQ7U6cTBqfnuHXk8ittkBdPTgyX2393vSqeXvMJ6H7D6XfWUDQF-1No8o_JzA4vbFbLXmlflYgq7KNE18gTO9kKu0YurC1kPYLWq0X-q1OLiM2O2nADvOoBqw5ZLhgPN7GIB8WnduPNQcoxyh0v41Bfufnn4J0de-vV8ezzkMbcjvyhbbawf5Hu7L1DhNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=ITV0S8NopcTbF0lKEl1l4X_ygW8sHEpQpDV0ELhkgMQ4x4c2EWcMTdM3wrVYyyGbNwhjhrctF11VMMhs2B5zUy4A98awU4YtBu-CI9lG97lPiR09j9CeNWyVyJuT9VTu_n4_WPPjIM7uf7O8Q284IK7iQ7U6cTBqfnuHXk8ittkBdPTgyX2393vSqeXvMJ6H7D6XfWUDQF-1No8o_JzA4vbFbLXmlflYgq7KNE18gTO9kKu0YurC1kPYLWq0X-q1OLiM2O2nADvOoBqw5ZLhgPN7GIB8WnduPNQcoxyh0v41Bfufnn4J0de-vV8ezzkMbcjvyhbbawf5Hu7L1DhNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهی دیشب با زنش رفتن کنسرت د ویکند.
یه i love you هم تو استوریش نوشته که من متوجه نشدم با د ویکنده یا با زنشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkTIC-joUQwsBo187ZTuRVn3b4i-KEnheFHM2K3py_rN6g7IH1dHX596qXFLwikaiwe8Vz4KYTd3rhvqLg63puDike81BqR1GD8-8YUc1jtHyq7sX_fg48nO-Tx8NLwYYSsynnsQCTHkO4Nj4Th21sHmxW87wWflBpeV2QTjfz-bgK0xAUeEq1q9PJZ2fFtuJxHdSkP45VDjkrAT8zvQ_Sneu2OErfu5HW6a2GMfOrti2XZpn6Z1B0-ZznCFe-Dia_kHBj7LWcuqsvb925h0ayuDVuys22s_nxEp23fSgtHftt80Ji4OiVMeu-c7oFaCMns8eNzrY2gZtf2Mz0WRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT_EQXZbmADSUeXU9hQNcFZiaBeG8CR6H9GaugG8VZzSs-NusPGCk52DL7-kz57kLq3U0dfnCRf0CctwLDQv5Qqp8U-k4k2nNdEVxnLvk817PGbGJFQUetArbPcjgFQNyEq3kZyQUBHFJyJkPVIwrNDg_NuN4stlCdBM7-S2ZZ2nT1F5eHvUGmpBzu4ISpLrXOKxZtxIDesvUVkWEKGuvYxDxpPZ2eXpViQ1i5zAO7NycMAKw64jb8D6Kb3ZoXU_UykXaNDMfZ20hikML5IfroSh9pTMfzBOMqkUazsh1X9xeBBySSTti9LXLueAvZR18A2o6KciH_vT29hpTTp2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaT3caO2C8ANBPdNZOQblnYgOgie6Vlqt1jClaDidAib6LAqZeAM8zKS9w0ApBdITvaIo2CrSvI3Mp0mfcR3bceCMMeoM0A8N1gRAQ5sX2SRqKYTE29q2El9pyLOxYsrKIQqX58uimHiCR32D03Rh_bzi1odhlJ_6A8G3f-GmxbkApom_WWUE4OjYGv1-LIhewvD5LgV2-nckLyelrxDJFTLxVQB-atpgEEte4ziqH7VDR1I-MwJgJlZtaqgrd0vW5mzwyA_afeuPCZK4fScCYOOtgSC3kWs2Ziqmij6bJOp3S880GV2SxFwaNf9zo1nmOqdUKY5If_9XPEPWKChFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnVVrFCr5VFSg91cfcWTaxOCXWoK2GXmnFQsNGYI-GR8Rldl47CguAKjeV7mxKXXswXoEYlsrkvCLRFAvRoYoedUB9bUbSBqBUV0M3Pt3LWBTSCLsfPH-T-OJ07S9Wq4biMNdhvR29OC0GYc7vGSyRrjR2ZrntdZDxpUIPS1ePM3uIMBRxbVs1dADMLORD7DfGzqceFSzZ57JFx_meEBPvOZLtLc7flSHsIp-pwCw4tzkZAzipZmTTTSKrOam65uZCGfi4YnzHB_h5sovSqJwzKrA26o07-4DYZal5vKhmqyGXLuXlNVksBUT2V5UpXs4G1cfDyDh79CF82cj7zgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUMMHtJuqZAPR63Qzv8T9U0eJiNOZ826TkJQCUbbTJmRtGfX8DPAyFhuPRxy3_36oloLbNPWjR59OMXMU5d4dXY9HAF0NXrnJK2XTKTXzHJN9252Dw6FzuIlB3N0LfZkxlBocjhx-9jjf0uRzFRyB4-yPp536vTILp4gQ-nkM0Kl2_evsdtj6b0lx8AEjOqoZE0ruGLBZzmcVfpcwJeaZkK2BxZxDMe_u2KqtAys095d4NKbQD2nU6oeEagNtQfSpISy58GmD2v1PCpEodt01t_dK5OX3bN-ZRzSsFvK2O91LzCVfBAPQcVm-JaHhLSkS8WpXVXJozM1cL6HnaSJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcw40m-jgZ_HUPjuJyfEgB5drEfE1vbNn-Vy90AkvliF2-JWxz5VQuCItTQkII70Wh4bWiCR2Vq6HWOi-S_PmK5zdiaOmXbZSb2_0E2TG1MDw8pdJNBugv8EujGu6DPgLvzBAdhn9nuVdZlwdx5HyWrvbnskny0hZlvemWHnmXWLrQTaYbzu76OSqrK-O9hSSyROzQaoS3S9Co6LmisRaDPVYr49gB48AFo40uNnMgZ3_5UAxa5s1zXEQcphWKjhB0G_lTNUxLWM4VNMMytClnvhaLsTDSyyHmfqoihqVhM0ZC0gXEKy6gVPQKTlIKhproqIPcJUq4LvDXQW9-voVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z56oUtZ1Lvrkkyj3j1KMEKL0PurGJCPp4GYrmMxpLxROsZZexaHtX73B1kDY8UfczLvhWhuWEGBL7fdW402fW4KC1JDhYPgQMSCIbIGzurLNjT5YI_bBijCBpNTAWMxuur7fdL2x0k9boA2bBjBbO8aoOA782tpLpEeQFDrPerMH_OEQYqINOPMMhr7bvgfOuXVIM64-x-JWQor9MhvZr8DSahRDgaOeCkDmLbdRe2Bqe82PX6T7cEc17dzcSTehmsL4Kofih_B49ZgSS5b8I6rIt61tu-niTNEK69kO_7qVMmRA_XTnoIkxgubUwv1Zk_fawS19l9Qd9nWjozos_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feVqMBsa9-YCTWw_8MPdfZheGavdew48Fl1ih3eHmp4lz7nmm9zzK70Bb57FAEVmqQH8jHhE4etRn54g4Eo3alexAqgMxkxGT3T0_lwhtv23eIttoK64LNEZT4HIF_GmeBG8Ze38SoyL-8fLD5VD52aOesRLZramKSHxWP6BUR8kbZWwhhBAOplzP81BZo79YPDKyU4qwxRkBFcgPo4wELePWk0FzfCrPM4R0HxM6otEJweNG7pIGKqXgMR8y8upb1vMXeQsacqVotOACiKQ0a9ZNTAI04xpjRbujawP81gtS--4wwxrsXlnmoDH0XqwlpapM0EUpQGb5PsJLleyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpXIRTZ_fum047Z6KlCnYwWr4l6-p75e_1BrU7DiZd9375ItXczDb9rmad9PTMqrFcEnSuJIYtF4zg61NnxACjVtMTeH6BsrOt3mnqP2xhro3CIn8gzxi4fUQVeQoDw_doUeGNVh5nmau_oI_Zm923Jal52am0eSE-_dcWpG9lbVv9uqdBOKLi95MBEqXkHtjg-IJx_04---ZlT7jwSDNTK2UmIhH19hxCSgcERm3T7ZsRjncBEFv8xP7zxNeDtWWrL6WeVnslZC5vSX6JcAbl4e6f6u0B09GlTYI4DJgctiaBEaOZG8SF61X3U-AE6_5eH_3Kn88UaXjJSANCunBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2cMPw99OwEcDcFMS2IvD_uFHlAW1qtTxgItebxa8JRV1eQoaZjH8CXWwNgM41FOT-TsDgxtY4leUMUJ-udIZ00rzdN76wPz1rwfbDVWFcg3U4RBz_R03kTsNupxZDp1A9ueX9S8Wwkd9kzEuj-kDNzp7h1aVV7rYhtUJETaxwh3hXMPwn30fR2gh7cekRySH9FxCOzpoqJeqqsab3Mi9eiPgS_iIj-81tH74UnBw0W1hzWqS_WixNal1B41zrM8Mq5my0JYWTY8_2TKz6yeIF6kG38_aTWcZ2VkbjPHE9xm8U2tVwf8BDmjV2PeAjHDlz8Lm8xAse4-KXCAFnm6Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=aka-ypu3aw31C8p7iAGRxZ2UvTWB1aE8BWNTfhWuDlAXBLrKqM74Xjf5J-CgWWvQmOAtq51tIDnNXPL6vinwXh7gYwj2vgYOx53i2kuOj6pUO3EEST1t6bYconXCjVX01JH_Roc3E-zugOW5olaCqYsXJGGvlqPTXDEjRjsz8VhH-gxYCOGEeTi2wT1OlHrSpvj-LOg5nZTKHa-UXbHQkLnGsvvmoIwL2T3ZiG4xOkgdt9LH9H9zABxuoSbJZxxulR35n3a_77e47-uPrrfft2BhpB4JF6e3gFkR2GmmVIBX--4E09DeW5IyCh5EdEH3Rabr5DqNc7hLKtcGE2XM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=aka-ypu3aw31C8p7iAGRxZ2UvTWB1aE8BWNTfhWuDlAXBLrKqM74Xjf5J-CgWWvQmOAtq51tIDnNXPL6vinwXh7gYwj2vgYOx53i2kuOj6pUO3EEST1t6bYconXCjVX01JH_Roc3E-zugOW5olaCqYsXJGGvlqPTXDEjRjsz8VhH-gxYCOGEeTi2wT1OlHrSpvj-LOg5nZTKHa-UXbHQkLnGsvvmoIwL2T3ZiG4xOkgdt9LH9H9zABxuoSbJZxxulR35n3a_77e47-uPrrfft2BhpB4JF6e3gFkR2GmmVIBX--4E09DeW5IyCh5EdEH3Rabr5DqNc7hLKtcGE2XM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbXLkjWcE0xMEecT-n43C2YgCcMl14TyrY6myFG81nV9I_C0s5dJR5qXXBsalIEu8dVbLWpQvkvQLgEJd6iXVaU0JCbS4ak4_-q9It0SnHEeNq744WgorL9mH_o_sSfE9-YfoPzWk9BpBNRWDOvH09LBHUQrgiBy7fyJrhwqw4ig-qZx27tmAxv2SOrByZ16UvUu93KHfoE-9PHYfBkEh9DwytdQDIt0duSagrVvgqYIA8K6lQyFSi0NbdQ1zD5MhBeCgY5NGrT08_1qp2UV6frU4_MEFbpKmCxNBxcTAxBE7zDCcW1WuELj7ySeKqMWYJRneRRiYGUFTCoApqHM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MerxYNaTRVLNgf550QcSJ2NdX_zfIMN88YkBDpRmGxHtB-fOWsnvAIajQbZx87UudX15CJD1ISGMlXTXzYNXkdJ7ZvGZ6VNlOVzk-RybX7d2Pp4VWsUImgLcNErWZKrP_cAiTbHSIio54ZnGlmziAN9cKMJ4LAekCFnrVVbMyv3DYUONLmO2--NuHGyyuxVx4t3OEgKARiTjbpIAsVchA51FHoY-mpiYigHz9DdSfYYVJn9icxkyVmT5Yju4vpi39G3Cs7MXjsU1g6CwojJuLyT7Pv20mXNObVjaW7M-VvF3OBhVtMmlAB4U336sYaZpFzlwJ4ylBG12PzzX5m1yRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfKiCF1QsJ2LO8d0oRG5oAV2N1ZkBMcid45joyp22Fzj_k9o-ir9IQIjS4coB2VEnixZS7dc61EPT4jijcH7DiRywC63LPGP6RZd-Q-E7KGHQVFbMokCQ3P4m38tTFPHnCwCAkZ62RwRya3tguc0h_v2veQzbwz4TF1kgrKVw8gBPUHGPYTc97ICLXmxXpjvoMysiEHxkGgHYLQ6HPFl6Rowx6s49kdZuZlHIuyNB7kNAKZ1p_U04ueAPxIKkHd6oX7UAdQssIH-XTpJ3hHlIprnAjh7UBrMnmq7jiB9PvmMwGFr6RniietydIVAIsUH9R2yqI1E0AtwZi9OhgPdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJimePeCvQsjzMlXU2vbHXUGcQG5fRxjgKrNt4dgtggZB5JcmiUhgoq8EREyxRTMD0ihj2bXr9x9WMm1w_pVFEQFW3degQ8gW63csGzjVtRjzc8uIKJhjjaYCVzq8T3E0kcAj5GH9MhrMaALC9Ik2g_uM7yQSoVDQGp1NOFeR-KX8H7s1uCyHhPJB7bnt_rjYg8aINexxQD3liUuZACeieUKvsx2fgQF9AA9HL1amnHmGIwDaNpBbrs6-zu7A4YyphR2ay65x_u-PS72PbrH5W4JwEumpTtD5xEsjZi7-pGJpMLPMiutsUzb2J2ItlmC2ZfaeaMtJkwFLRAsWanOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCKovXiEYgZj5H7PUfFeGWk7G92II1BsqH5XNONvin3ya0DEh4sGALjEntsrq5NvMwtpve4se2NxY_zOpwmZ4ixcDqOM0yRTmqIz4lWI5GgsuDABWfy0bfehjPwoPxv-NIpvYL12g9Biw3H64RVWNozmbbTOpX6FKvrpDDbHNeRNKBiy9NuGoMsBjTDAY4yWckNzi8oVA10y1YIkwDsqYUZq6l_JNEZHX9NXSZbIYQnmCEdOmA2-3wHU3m-nGOn7Erl763qxJXumqZ_Q4l-Q9MOPj9nvyihdyMuA92C0cSx5HntyaduQbLX9V-2D0fWQ5rYaXmhCptjiu8gNHSC7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqLYww-7JOzSTGS_xeiXWvxkutJhMgqejdulP4z0_VpTl1Td-uBd_g2jmI-2Gnf1p39FfE10TNG7jxD--slNKptmX6n9M4DxdfoHAv-_deURk-BXs0SZiMa303csYL0H8r-JJjpUWwbqmgI3I2tRrQQHOJtrvBN9XFDp2GUYdexvoTPn2-CDBewHTOECz_9o6bVxFGedJhsZ0KooJz4qjlN9H1tJmi-0SDjbYObZEbTH_mMuDj4nca7fkR7c-oVYQZqT03y7ksr2zTnliW--9MI_-vluAKvBNoJKU-q0qW1j5Sywko7SU_UB9hQO42IXupHaifPT7WfmU1stw2k03A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soeHMFiavHGGkPbz7byCnYESfa0_PSYngg8VOrIIDzh2pMw1PpUl1I4djc9pYYjgdpVlQxhwQaQfTXtEjY8p1IX1D2Wn4-oglalDH_rLN8VGyQ1emsKM9LsRBd97iF6ft9UdNzXxRHNpHCjnEDSWNrM74DCVtfdB5bsDXey2Wlet5C7ZqdjLOtDTLjl7dUC2T-CgFX8N0kIGSjoy1nj105EMG_KY_KIfYfpUnX6Ux6GFb4-IHN9T58oyg4YKWHjSIFQvZu2L9FcyYC2USU7GEkphvTxMMnfUlArdnb6B6LWw0qTt1S2M7pK5i-F14poUFhQBJeJZRIsVHbmvB_Rd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=G-TKSBp3OLMVypZxfLD01_5Ydrp5hPj5cVjSGznXTOySKA8G6iPJwrMSS_9FOl_jidygBaMas8oSubkehNJuxFjLtHlWACDs1jL_a45Q9nQVOKQSZUkYLiKk4ZB8hoivezaBegJFaxuyOOAvdEroFPNL9t0sW7exoHTo6F8PhExZEGGyM89WVV_w2asB_izFTIak8XK2IadGnfF1GQjh0XGl3RJei4nHq0tOEUvjlyomwCFT9mZlll2B2b6eo6pPK8jB9p6fzFNqRG6CSK_jcPwPeSx-ZtiLfw6YoLC9Kf_v72bWcNUE8cLEwYqkTUShZhJvS0Qquw1iZgGQM87UaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=G-TKSBp3OLMVypZxfLD01_5Ydrp5hPj5cVjSGznXTOySKA8G6iPJwrMSS_9FOl_jidygBaMas8oSubkehNJuxFjLtHlWACDs1jL_a45Q9nQVOKQSZUkYLiKk4ZB8hoivezaBegJFaxuyOOAvdEroFPNL9t0sW7exoHTo6F8PhExZEGGyM89WVV_w2asB_izFTIak8XK2IadGnfF1GQjh0XGl3RJei4nHq0tOEUvjlyomwCFT9mZlll2B2b6eo6pPK8jB9p6fzFNqRG6CSK_jcPwPeSx-ZtiLfw6YoLC9Kf_v72bWcNUE8cLEwYqkTUShZhJvS0Qquw1iZgGQM87UaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم دیشب یکی از هوادارای استقلال داشت مصاحبه می‌کرد که یهو رفیقش جلو دوربین انگشتش کرد
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXC3WKn3mnGYKQQjlyzo0I1aUmf6hR_pibQ-O6_6jL3kfcGBk9ifoaMejYGvPHiLWcfYkX89wahr_ey6W2IJ1GK-doj3qY2aPZcfeutNs2NIr2snmrJbRa5xKlLbrV17mwU87WHIBuk1jhp0fQmXaJUZEK75AC8ysKdnmW5dNbY9oea7rPqLVAInwDgABjZBC-CEE359-eoVlm4C1PiPT8PKlSNq2eqAzTL3KCfg32Qz9zDOpUsxnJr9tqGwlv41s_61q5G5AT0A3bOQC0aFH7K_tuwanEKOZRQJqYH9_0mm-bgV8fVHjec0SEWmEvSAqNX6DHMacjocyni65ZaVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=amdSPzhVpuHNyvr0gsSsES7AUnKnRfKrRofGP2n7yLt_d5xj4v4hHZaAj4BiuQt0oEY2yBbzhHNDcUhHgwLnY02b1lZ7wsyx-b_e70qrMSl2qvcIfkPykHkUAQYOtOra4bHuUG3MBPaUl2LalshY5uejmcA5VYSBiMQiU_WmqNmbGnexpWOvoQboMqrJKeBnMLE9BgKaYOy3HOLAM4brIttm-TKGyJVd8X9Xxer3uFgo67OeWl9NB9HDvI-L5k_vq1DULzM_b3_Lhspz826DjiyGfMBDrzkguzviTNu0MaqnYGYw-xUCxkpjtGE3Lr7AG8ILKpVPzq4JEMSx5IDYTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=amdSPzhVpuHNyvr0gsSsES7AUnKnRfKrRofGP2n7yLt_d5xj4v4hHZaAj4BiuQt0oEY2yBbzhHNDcUhHgwLnY02b1lZ7wsyx-b_e70qrMSl2qvcIfkPykHkUAQYOtOra4bHuUG3MBPaUl2LalshY5uejmcA5VYSBiMQiU_WmqNmbGnexpWOvoQboMqrJKeBnMLE9BgKaYOy3HOLAM4brIttm-TKGyJVd8X9Xxer3uFgo67OeWl9NB9HDvI-L5k_vq1DULzM_b3_Lhspz826DjiyGfMBDrzkguzviTNu0MaqnYGYw-xUCxkpjtGE3Lr7AG8ILKpVPzq4JEMSx5IDYTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=UrvFu7agD312yd3lngIyOB17iadrwlLzG2_1DftFXCr6sJzP_5wk07sED3RH5bPx_HAA-RK2YchsqT3Xfxi0qSxhGWTIXLqQJFcmByOOFVGcV0UMaUbfR-EjAvv7VBun67Sx_Z3HlEwV5ejRZ1wd4fh74ONVtVF4JNSZa1kYNBxOUuvukdDM2axVX1ulDyG-sCPBiZNZ4bY-FIWWCkNBf2rs50pgB4gjvvig76W3G36cNrXl7l7LEcTBNYmKjnU6zRv3Zl23JyY2mXEcQfOJUGQg1czXptTMi3ph6MZcj0vHNMKj20g8cQmyN5T7pGkF08OH7dTC2bxj9fzEVnuXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=UrvFu7agD312yd3lngIyOB17iadrwlLzG2_1DftFXCr6sJzP_5wk07sED3RH5bPx_HAA-RK2YchsqT3Xfxi0qSxhGWTIXLqQJFcmByOOFVGcV0UMaUbfR-EjAvv7VBun67Sx_Z3HlEwV5ejRZ1wd4fh74ONVtVF4JNSZa1kYNBxOUuvukdDM2axVX1ulDyG-sCPBiZNZ4bY-FIWWCkNBf2rs50pgB4gjvvig76W3G36cNrXl7l7LEcTBNYmKjnU6zRv3Zl23JyY2mXEcQfOJUGQg1czXptTMi3ph6MZcj0vHNMKj20g8cQmyN5T7pGkF08OH7dTC2bxj9fzEVnuXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مامان ددان تو اینستا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=J2sWLzGYlCaTjz_RrXHlOkMr_9TBytIHG6Lz80KRWXK4_D_jXSZ9nLnRQa0oXQa9v73wHE8S1z7qyYfbHuYEvHC8nPg6wfnBoRUfjn43m8cZrKOOquHkrknjotXDN0k7uXgE-EFWZ6FGNxG2M4DdalXSLDRHI2rlkgMBXEj0dFdO2VrHFaNiFpTeK_d-NbiUHxMnZiZXzklfeeAnrPAhD_9EorurfZXc77wW3uiJ_VwRN_ck-iE8AjkVBnpi2LnN8yhcKMwhYq0CAnUi2ZqGLiOLU1lHtmBkYZzrVLM6A3fFeOceA4CZ3kr3Z4Qp7etUX_mRLgroajlTbFn2ezXjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=J2sWLzGYlCaTjz_RrXHlOkMr_9TBytIHG6Lz80KRWXK4_D_jXSZ9nLnRQa0oXQa9v73wHE8S1z7qyYfbHuYEvHC8nPg6wfnBoRUfjn43m8cZrKOOquHkrknjotXDN0k7uXgE-EFWZ6FGNxG2M4DdalXSLDRHI2rlkgMBXEj0dFdO2VrHFaNiFpTeK_d-NbiUHxMnZiZXzklfeeAnrPAhD_9EorurfZXc77wW3uiJ_VwRN_ck-iE8AjkVBnpi2LnN8yhcKMwhYq0CAnUi2ZqGLiOLU1lHtmBkYZzrVLM6A3fFeOceA4CZ3kr3Z4Qp7etUX_mRLgroajlTbFn2ezXjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فیلم Avengers: DoomsDay منتشر شد
۴ ماه مونده تا انتشار خود فیلم، این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD0QEAoJ_J8d-seQEv0BoNXUZo252tu_1Ita-R5FMCISVdutt5Sd0hIcbma6W1_b-DOC6Teifi7WeWhlY-981y9pl-8XW8vIc24QoT3ZwtCnTuxflmpijg_HndTKjP6-9HOCvrYcdB5si4JOwmc7-ukVbs-oXG1ZOIIYBtbnFegc86fiZRMhw4n9oAmuDBT8bzWqzcwgBg0XnAifCaXFO0QR-udarAadW64uyu8iZv_QbggDZ7f9CxNCUidpxfnxNVsUPW3mYgLkZQhS2-NLpK1I9sFpYi-eZWVH1ej4F80XZTJkpAPvSxTm3_z15McS-1x95fSGKGYruOZokXH3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8bjNKGHYjOXVKysc4TndQiX0S9JSicHDii76XlNJMw32K0J4iCOO86hjwoqUVjb8Mw_s-MaWyy6Q6qtDmBynqdt_6W34fvmoC9T0f6rO4_YB1Egw0d3QydHQkiFYdCQnDVafu0PengLC8p97lAq3YG9g9jRW2eQlzpAKPfaZX4NrINxMSPL9pdPu293X4xpdxr0oXQsnQYVEisuI5kxE32AlcfAMDsz2MvI23tB1XFH9atnn6VgPhNwbNZZeFo8tuyZi79ET8svB4T5SjxEb-fL92sTW-RKrYttnQfrZ8TVGuLqM774eovj-vK3ivukhpzLS8l3e4HjlvC1alIk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDPdW6u3fAEJLKRXAf45B5S5MU1qrRSvpD6M20IwzrgKMr-QGR9ID2_OpPoHXQgOe3TlKnFe071L-mlfycAs1Gkuo_l0BKKlQacWgLluRH5-TD0yAqDPViUquQx40apgldNnHW_QppB8kBs0cjrNdsNrhwcMdLkBtHm4V6YxGELK9zWaIrFRdAVmhDvFMeduBDgGbZVFEr7gW_F4GlVO5kLa_0Nr678RbkcNHEf-R9vW1WbTzF1FhTKAMexOxk5_U9QQbFElngqk-rXdglKtgTlMU5x91SFvgFZAoO4veq5YImO7XOmnlGEy-zdshPs-jT5TpPJ-vyNhfkSaNS0qGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5WckhJrpENNhYp85e5rZj5s4d8jRYCNAHqBtwoYskrIFji69LkHc7QVnuyWTrlfLvQjUbmzefWa-03DqelZhXBv9tIFod6MOa5H-qMJl9bZ3-XXP-z63vgLS-7tbynZwHlzfrvshtQx9tQKIfBW41rmYNp3fYwik7hYr_24Kk8XRi9dWowMplIAV1nHm5ABRM3FMuynejGKA7cFmuVC2nikTz-PNP88hDEekzo5KcAfVGE8MktsWUfD45IbYRmbwMESg-PfOCF0gxnHRI8fFOksbGTgz6uF7myKY67LDPbwKWP3gr8dPBfxvhfhO_-_0w436qewzIwBeFjyBbFR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8R9WWTcdylDz2hKKU68o_yM1ANI-9GMEOYnVm_NKgyi9aWeiwSkgPCo1e5NHW4NNploEeqzz01wfXmmC6dbvCq2RYY9nT6TiX0Wtz_uVjfejVru37j8C32Ejr3pEu7o0NpL6cgio6m-D-rnv7komNoPPNJNDcltoMHnYHbe-s48ihYT2dHjyqsA60eoEI0zOi3buU6s9S9uMNPnnZf-F6WWhL5lB7JFaWwqNqH-tFHwn62-DNRG65LslAqGPeLiOmmnKE0i3pHYEaTbzyyFuhfAZycovcp5zLKezFX72tLILk25N4V9nh_ESnP8Qy2XRD4exFZrdAwpCbifDmtjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Htb9RA1PwiNqLgB4IuFLe2gCBK3Hz3ebIPFqkQVDpnmVLOhA-0rvuklkYvEqScgTcX9utmo_cnLRpznVhyFohUoRRRdPV7EOpX4sVp9KFByv8INECK0x6niKxJC6aISkJRdHWvb8mDp-Od7F7HBI7aMWa20XBr7mDzOH1Q7JjTsakO5ljPX928CnnA1SvPAosC6g3I11bpbWTuR3dTpKZNRLD8zMK_2CxExLlv_fnmaaquhtqAOZftlwXPzvGNE6TY8ofoXsW0KcLc8_xplWWgVKUnOuyYz5bfcEBsqJrj4dX4aUV3c6Car_dZe3Qzhl6zRrJ3MxyfewA_XHEWBmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m--uhTVjTmlu57l8uRCyacpcqIovWtRIAtOM_vRJFsbmDYAQLT_y-y0RcwPWI8GkBGF5UgrbIzQqDqlgfv8G-6G2XMGdUeiD7PvMRJz-qFAzK21Jii8zCMd3bHLlTVYkiqbBK0FqigBJhpha8nhsfzvAJPP5vKqIRXHxPb5vimod5eCUMXzrXv_UjewbZ_WzihKJ4MW9tbVhp7O8aKRN4C7JdYnEaqdM1Sr_Uz5pMs4vjvDwY2AevA4-G7jl19fmcGiqIhY-XwyK8RQb7EYCK0ohuoJkncAlo1zDjH4GawN49fb5gzuOXzpUNPo_NGQVEte0H51tPSLPX89KfaMYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=TaC4_deDxWSm258rZd8s0Jv-byEiZu6-XtgITz6OcR_twDvLtFgtzY2GIWCB32frKSaaJPQr-cTbqJPW2n2dLe7GQmWsz-YNe_-ivGZEj0z5FX8OwqmjcopaSRLbxknJqkK1qiAguLKRC7DJStpwwtySVhmpnBAjQyuASFYfQUhyTc6rgYySjls4W8GfaDuz7_IAVotYD2jtasz167xDdz7dxbXrVrTZklcCCiIvpqArjtZfPR17XvOrMbxw-a0v5EKgnCUmvDr5r2ux-R-O8dgtvKS9CtO_jfz5_w0KMRC3GSQSpdLDn5CQm1Pmy3jqIVrmtyVALQMJNt7ROeJ6SEYASEU7gKJwzDOPFwsAtYt9eLRCJBeK6NvVleHJtLD_3q6h2DIpWRrbXKElu49_WtG7yfB1xjXiRSAmdSICRz6In02Eh6ocEaVuckBW7_g-4UZl4ZIGpy2KoUj9Qc6w63R4r3R5tSCNyoqIcxq7SAXQBY7gKZeNcbeJH_bAB-8cPoQ5SteTEgbj8AZcZcKms77jGbKCzKMp0FpsERNV_pWB1Unp0nFd_71H1VSNS3bH5O0h7m_ErtotH_zS9J-r3lY2dZAxppzzLPU4fHVWEfv4SrDNgcf-psvD1nQ3dLBYnQF-dlmaZjinpe5RFq3RVNvGkTIX5r5DUeUkJaEnhtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=TaC4_deDxWSm258rZd8s0Jv-byEiZu6-XtgITz6OcR_twDvLtFgtzY2GIWCB32frKSaaJPQr-cTbqJPW2n2dLe7GQmWsz-YNe_-ivGZEj0z5FX8OwqmjcopaSRLbxknJqkK1qiAguLKRC7DJStpwwtySVhmpnBAjQyuASFYfQUhyTc6rgYySjls4W8GfaDuz7_IAVotYD2jtasz167xDdz7dxbXrVrTZklcCCiIvpqArjtZfPR17XvOrMbxw-a0v5EKgnCUmvDr5r2ux-R-O8dgtvKS9CtO_jfz5_w0KMRC3GSQSpdLDn5CQm1Pmy3jqIVrmtyVALQMJNt7ROeJ6SEYASEU7gKJwzDOPFwsAtYt9eLRCJBeK6NvVleHJtLD_3q6h2DIpWRrbXKElu49_WtG7yfB1xjXiRSAmdSICRz6In02Eh6ocEaVuckBW7_g-4UZl4ZIGpy2KoUj9Qc6w63R4r3R5tSCNyoqIcxq7SAXQBY7gKZeNcbeJH_bAB-8cPoQ5SteTEgbj8AZcZcKms77jGbKCzKMp0FpsERNV_pWB1Unp0nFd_71H1VSNS3bH5O0h7m_ErtotH_zS9J-r3lY2dZAxppzzLPU4fHVWEfv4SrDNgcf-psvD1nQ3dLBYnQF-dlmaZjinpe5RFq3RVNvGkTIX5r5DUeUkJaEnhtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فصل دوم سریال Mobland که ۲۷ شهریور منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNCa3Wj6e2Jj4aXBsS1ayArRbpdZUiS87VNyeyehYqIP90OAkqvoULCvj1uD_C6KKoJSUGjx2E88W6aodioctqSEvONpii_pNKH3UYeBQWmhPgghTHckepu52l52BD1xunbOAZlzwYarM6y0H_y50gCtSRBf-ZIFXxxLK1eYieRmOA0BFy7yBh5WpihCH8y9FSj3zNOquZGv3UmtEhw9BaeLPVVWCtFupOPgS8YFkyasYDUdvlfjLJiOKmNicF6v2Wc1MlDGmxR6qtv4hohG8khcBHl-zLwKqH-l0BYvcx1mOLBlyGHTQK6nEY647QKiU42JbSv1etszhCGSYN8ILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAwOCqm14MZdxS4boLiFYWfdgAYPWgjA9tqkbNjSOmu80HrP53EUpxUSCR4wOpAv_tXNNLZQJgFKvTTMWxZTZ0KDL5LKojj6QRM4j024FnzjmDrQC-5T3aXUKDKjvK07-TTtNtGSolmioN0X7xlEtjg3RiIyp894d80oGZoLvD4B77BsLEvaX012tuI5T-GuUiQUGNZaXD3RfZhjBi9XzP5OMBjoVkJgIFOHmxnBPXIKU-reI915IaMhGqJuIabnhS8HCxvrACU3hmMkoFRtxfnpSzuM3tpO15j-Vm28f-tb2qxYZZhFiVvx_iE5INZ7tAT1TGotL95ZMxuBNf2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnRPvGsx64POBn11VUBsOJEnfqgxbYsykDMqzhE722w_IXDbFsO18HOQm92avdDEMM9Ss0XDbCTM1_C9w0B0QVWtX41Hr2pvlU15upM0qfg-WLUt-2RZWp8odK-VmZ58PWSnp-digEW5oP3Qlp6aREOT1by2qnM60qDAxG4E2-zzdfiNLrJMltR_OYBYBzKUFbd0LoyF7jkVvVaNt8bCw-sszpbC1HNj6wwFW1zFeYPytvnILkbGjQFVJ8saRymG2PdQYQXPtw7yoGufCADrh5TvlTEQ1F9udbFAfWivE70xawp16cF0F2uTQT-5y5wo6Ipm3hvSQ2MTbN5_7BVzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
