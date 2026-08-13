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
<img src="https://cdn4.telesco.pe/file/fqcG5RfpsVYHIqZrI3_9H4bDSdhiTiZg5mSHK-bHT9QE8ob1bFnFNFRMfguH-WLyBjMPtg5LVYKJcT7r2T0YIzq8iXz9V6CykhXiP0QkJhY9_STBEqrXr-nwA35b3sWLggBrHJE5WGRJLDUAgXsisZsHu7-cBvcP1Ns4ZfznKbAv08Vxj34xHNuUfVzq0Dj1q39lfLwSe_SsSMeZqVOIWaiWHtLQryQK-RxOqflpGFFXLj7yDiITIU4w8q0Pt5i18V6KgYGJaejFo5fruS9otrJIV36y-G0FDhc4vpb0hS74M483R1Ig_cguJGlC1M4KZbeND3eWJV3epF6X0Onn3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 125K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 16:18:56</div>
<hr>

<div class="tg-post" id="msg-69985">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcmagH-lRxxRIzXaBUeFnmvYSVcJXHxQpTYYqYqD8h8dLz_VhAFKP1rK4TTk5bwuSUSZ9zTUFCDNfOiJVRj2tUp29vM3gDK6TWAtUOOFFsa99zlJfAjBva7X5Pu1bW8Z3u8uF9GPbSpu5lHY4hzQiFiiU0zO5du0npCdaFcj6Sj656iQLO0QAaNaohkAoPFsXmA08IUvlQ8AgE2E0Lv_XUeY0B43-nWWmuMORKmxVrKEKi_kUuRDjk6gNPttWPXiWgRMVS7eEtOZKiOtBrvUkTQ1ik9qqnMnHgz0_lTBG9cdtY4fNESWxe-Tfl1EJSrN5ABM9VicRXAIKvvce-r67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKVc7WUlW5pNAtLXCWu6dRBFCDqZaRPEziUd4HyTs4a6fRALj2V5gcmaiMbXdEBq5MkQyKG-iiTTub3D7nK6D0_N_ofOUVNBsythzfH_XrFCvUvlddMQnscWIOCrH-LEkINUC7QlFGd6xca-IxB1OnXf_49HGKyZvEYheQkCjbvpLIu4VEcJCEqi4Cf3tFgcO6ISlIwKiSvEr_qZtuTgkBncXsyWXh9jXCty-Zm6Jx7Bdruk3neSu4m5AY7C9_iqyWFpxWeevp9aaPL20In_-NNhTJagyyHSbaPZUM8JXcpLwJ8kPNpaHpAY-Qq33uQbh_s5dk-liB6z_CE20JEeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWUg_NKvR8EiV9oDsAnTtPLJB5Wq6O_o6EZYYrz9TomxDZJFCAXqNcYx9xgsjhcsAITga4hnEDy6H4uBfLx4xW7IyhNLzzGE7UlmNjFrefNWAUHSxg5KG73484abzXGLFLB4d1pcLXSHYcQjzRedKWNptCwbdiLpBZkYFQ9PONumNUmelzOy3nSHKdVTr2AwAtkNOswb0EWxihvKtfRLtcxqs42kKe-odLXj4zTtSTsgjybo0h9ahmGlfOae0Kt6dNbobbAnE5gWtfsmLg1Y6qrE6TGm3qUgkR7skE69-7vp0_wcLNJJZQiUfBbwBkhHccsAWMA6hwDZtZgJ2brDYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
❌
#فوری
؛ناوهای جنگی یو اس اس جورج واشنگتن (CVN-73)، یو اس اس شوپ (DDG-86) و یو اس اس رابرت اسمالز (CG-62) از تنگه سنگاپور عبور کرده و در حال حرکت به سمت خاورمیانه هستند.
ناو جنگی واشنگتن، ناو اصلی گروه ضربت ۵ نیروی دریایی ایالات متحده است که به طور دائم در منطقه هند و اقیانوس آرام مستقر است.
عبور از سنگاپور به سمت غرب، این گروه را به اقیانوس هند می‌رساند و مسیری بالقوه به سمت خاورمیانه را بدون نیاز به عبور از شرق تنگه مالاکا در جهت مخالف فراهم می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/69985" target="_blank">📅 16:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69984">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=b0EB1lpubpyGr_L_ssXlhpTEkMdmd5Aw8iIlqxDsIx48OLgfUTFANWimhlQn5ixOYhanBIE5aqTDlmZgWTLw6oI0cNqx8OUIdk_JusRa4mch8XAG4cFP26qDuocN8UekpaVe5UMhrcgTYqIE8zDV5JO2mx-IiUPWedvJw8h-Uy7258sTAbR2sqDepSNlx8pV62f0JIvxBrcdVpWrt_klAKxKv-JjAWowP9G8YgBMZUVkYhM-OAdX54ASAzQY6WhzoB8GViQPl3-8WZtYjujbH7wkR2PeGBx-FO6qea-ZIPGbL5k3RlJrNJ_gMxD816LYQIx1KMFN-NaOCthGfVXGDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=b0EB1lpubpyGr_L_ssXlhpTEkMdmd5Aw8iIlqxDsIx48OLgfUTFANWimhlQn5ixOYhanBIE5aqTDlmZgWTLw6oI0cNqx8OUIdk_JusRa4mch8XAG4cFP26qDuocN8UekpaVe5UMhrcgTYqIE8zDV5JO2mx-IiUPWedvJw8h-Uy7258sTAbR2sqDepSNlx8pV62f0JIvxBrcdVpWrt_klAKxKv-JjAWowP9G8YgBMZUVkYhM-OAdX54ASAzQY6WhzoB8GViQPl3-8WZtYjujbH7wkR2PeGBx-FO6qea-ZIPGbL5k3RlJrNJ_gMxD816LYQIx1KMFN-NaOCthGfVXGDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد آپاچی ۶۴ در تگزاس آمریکا سقوط کرد و خلبانان کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/news_hut/69984" target="_blank">📅 15:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69983">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=k93NLyokREnYbbFyvUPUMT8nAD7wdSOrqqU37034RC6y0YkA8752yMvDxIzDy9Z5Upyq3vIb6NNkvRzw0k9B2E44HhyafnNu4jyKKPr2wTgtt9YfrzWCUKQQVRL3CBCowqhx5v9XDjG3bTK-XmujQuo9OAbkpIXvSaGZPybRceoOHKptosT2cRLNKkD7rQxN1EXvNFQ4QC9ayFD28mcHpQWZG5D4B8JE2fqX6KpRgBzVY0MLEuAwCqBnFm0sacd8RAAMlaHzKWz1awJSU0ONnIYWOMBped96jeA5KdikAD3qapK94HwcJsn0ASuV_LzeWo70qKQrJY2c5PZU54a-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیکی که قراره برای بنزین اجرا بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/news_hut/69983" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69982">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cea94911.mp4?token=v7wWXJFkCf735lNmQqIlUirBpQITuTvmxmb0HSvMuYtDMwhwGPyG0I-nMsZqrom2ykSsSZAgdfAd6Kd142VS-CwSm72C50T7aqqhmH_bBPc4ujcsHnTa6Co_V_43fOXPVr7AILNAWH-nM_OzQXVCSIXyDHYfpH4uRbR80pXY3_DVANpAai5GMJyNX7iBhfUYLC27LVSzHq7rWY__NousbLcQmwfEVNECzbmF_E2LJaIW4vBkczi_s9sXIIGO3LWAVX4b3Bpl0_gaTOby-e5aMKCHqKxOIqbsq9bzxfsgzf29MX-C1iJUItWSytgSZVFylLCsf5EirdhXAyU-6c8DRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره بریتانیا:شاید بتوان بریتانیا را «جمهوری اسلامی بریتانیا» نامید.
کسی گفته بود که نخستین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما اطمینان حاصل می‌کنیم که مورد دیگری وجود نداشته باشد؛ می‌دانید، در ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/news_hut/69982" target="_blank">📅 14:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2XH_lCAApFhQXOZ-z3_3xipA7IYIKRSzal_7EmAh0LzYU5UDMwEqDKsg-QEPEB4ktFrlN19NvQ_NL203rDZbfdcNMpFN91AgiQKn50IVQZZZnuqrOF8spI4BoZAcWxWBBRM2QccNGu3kCKvMEKtC80OShu7K36x874Qs0Lg44RtOnF682L6ugVymyoPs1vgMdg8voJsw5h9J9koW9qGSbV4nTf8KaVoslgjL4F5PkSG0_vx4sj1-WEdXrTSxSAl6Bo7jfc6zE30FlX74BT73pK1JkydiqbpCMRSadFgTJjsuM4gEC-Mfzh_XgV11SnJx5RGfirqGiJuRwXnYTm5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohuBpCvW2IfxdCgC-w9-AVJdCsBA5ijutWN8yFScQu_OI01FnI9wGeo9IqKLHsK7qOTPC0EGix1TGYXvt2d8U2HpUBiK6brsJH98WfiDXf0FP3JqyW2KLV8HvWm5ZY-W0Hy6JG4OdIMA8HS8IU-JMNE42jWQBSJBMJ5M1F0CzQJ4CnaWsqQKUrqWumJNXplD7EdlkYWH7qv90nHhFYonW_iWTVQ0ToKdwQxmDPsvgQ7pXT0YCd_HKr9C7v2YvCSs0HBGtpMvJSOseGXsoiGhlytvcxHSyM8D17hQ_6iWynxMIQTAk5fHDg7HElmx_JtPNrvPlBjBZcOOXVBi2LRTeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=FXZuK87lSP5UOHyfAPKcx9tBsDhEU9xmK5zrucIAAJV2vHvPQKh1hZXodh87Etk3UKZFBm5tNKnqa5pDrEwz-EXwGCh5JCFDtXSpQQm3v2UpiTpFjyAZm1AibXPi-hjPOhTu381MNXa1uFoGTitxLDQgzdLFGOON8OpYK9RG0qvxzNnrYzBZ3-5wzGMAYRti4cW-cMYSdXjIG3DkAztvC3pbwxKtG7ADRZ9NGDqrt24eSUuWU4vDbVD4c8rgZPvRnTrf8ZwZWE483L8A1MYi4_HkoUcx1f6EFWXMB8w3NXzfzyj8dOf75O-ERAsCqMCbIGXFOA9JmOE08uS7jNoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحنه‌ زیبای خورشید گرفتگی که امروز در اسپانیا و آلمان رخ داد و لحظات زیبایی رو رقم زد:
@News_Hut</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/news_hut/69979" target="_blank">📅 14:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=qb7llvrpUDrA6QJml6vvbWWeVeRKtuqSa7guM8akvxvbVaCNNzJOudoEVVVundhar9YYAboimpQ3JpCY0uJgziBZyRBga9oFVmTMeEsqRSSdH8szifJjA8D6a7erEhBj00fTzoh4DuACWjWAEUOhsQS3Mj7tSALDHI9Ob-so0wsCO8RAoJEZoBChog8uhamcaVBMevuDGwNyoDy5knc_mQP7hMxuEBeuQ_fqCqXwKX3Bb0fIqoGiSrOjlOTa73FKoLpDGc3xm5TggQdwHCZErJDSFLF2z2_Q1ScP12AgaR3PofPdk4PkoanYZbCw659HFaM_eGSi99mmHKhZPeUcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=qb7llvrpUDrA6QJml6vvbWWeVeRKtuqSa7guM8akvxvbVaCNNzJOudoEVVVundhar9YYAboimpQ3JpCY0uJgziBZyRBga9oFVmTMeEsqRSSdH8szifJjA8D6a7erEhBj00fTzoh4DuACWjWAEUOhsQS3Mj7tSALDHI9Ob-so0wsCO8RAoJEZoBChog8uhamcaVBMevuDGwNyoDy5knc_mQP7hMxuEBeuQ_fqCqXwKX3Bb0fIqoGiSrOjlOTa73FKoLpDGc3xm5TggQdwHCZErJDSFLF2z2_Q1ScP12AgaR3PofPdk4PkoanYZbCw659HFaM_eGSi99mmHKhZPeUcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی اصفهان، چند تا مرد عرزشی، یه دختر تنها رو نیمه شب خفت میکنن گوشه دیوار، و اونو مورد آزار و اذیت قرار میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69978" target="_blank">📅 13:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo4kcRBf3Qs60g7rp_1Wx8oVop-L3e6x-AZLsxDaORlbNmAAZKO3BqxDGA10p_XCCI4QoIisti7scTv2NnMvRWRX54HB7IA6DmpJHgxLIyKZFo2cJ31OTexu9T-zIX7vWfY0y2uWwVGGjL64njN92NcXFxEp9YJgFTbQXgpotdvs7dbVkmCu6YZuh_gNTtoeN7AdfET1KQSunOe9tTHYt2ZMdFSgmA4TlABUNjdpc5rEzBBBOEjRct7lxiveZ9tjqLn4KprG9pePfy1HwhbNwYOqIWxREgi8264L6FaND9iSoLACblXRklt_PAUtQlHmIAu6XIu877ycmR-Wq50FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به گزارش نشریه "آتلانتیک"،
دونالد ترامپ، رئیس‌جمهور آمریکا، رویکرد خود را در قبال ایران تغییر داده و به سمت یک استراتژی "منتظر و مشاهده" حرکت می‌کند. او به طور فزاینده‌ای به تحریم‌های اقتصادی و محاصره دریایی توسط نیروی دریایی آمریکا متکی است تا تهران را تحت فشار قرار دهد و آن را به سمت مذاکره سوق دهد. این در حالی است که تهدیدات و حملات نظامی نتوانستند به پایان جنگ منجر شوند.
اسکات بَسِنت، وزیر خزانه‌داری، استدلال کرده است که تشدید تحریم‌ها می‌تواند در نهایت ایران را مجبور به سازش کند. در عین حال، کاهش ذخایر موشکی دفاعی آمریکا، گزینه‌های نظامی ترامپ را بیشتر محدود کرده است.
بَسِنت همچنین به ترامپ گفته است که تنگه هرمز ممکن است ظرف دو سال آینده اهمیت خود را تا حد زیادی از دست بدهد. او ادعا کرده است که تا 70 درصد از انرژی که در حال حاضر از این آبراه عبور می‌کند، می‌تواند در نهایت از طریق خطوط لوله زیرزمینی به مسیرهای دیگری هدایت شود.
در حال حاضر، دولت آمریکا بر این باور است که فشار اقتصادی مداوم می‌تواند به دستاوردهایی برسد که تاکنون اقدامات نظامی و دیپلماتیک نتوانسته‌اند به آن دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69977" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=GUum3lt-hCK498YdJrR5linZb4VrE3qCaaImzHtHDECHRwbWizjgMeKUNTq_viWOT5Q6uFGwwZMS7y1tAUcic8YSEo-fM6uGsc0hDDeXE_9UQE5UnoGnM1W6hhznqO7znBqn7OWEuoXsetm9qpRCMBQuQTqvRzhyuZpJB5lmG7uG_kw3uWatoOLeuRubPrbTjbuPHTEjYnI-yeia9sX4_UyQoipsMXR9oZhfxfxR6O-3kWP8XBhKFjd7priet4pX0RHtJyn-OlWNnjIdiA0kAX4Ej9AnlkhZBrAOTKyCIKQi2Jm4wBppNidnMHXdK0Jn1a8W-bqOUba-FkWsWhacVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=GUum3lt-hCK498YdJrR5linZb4VrE3qCaaImzHtHDECHRwbWizjgMeKUNTq_viWOT5Q6uFGwwZMS7y1tAUcic8YSEo-fM6uGsc0hDDeXE_9UQE5UnoGnM1W6hhznqO7znBqn7OWEuoXsetm9qpRCMBQuQTqvRzhyuZpJB5lmG7uG_kw3uWatoOLeuRubPrbTjbuPHTEjYnI-yeia9sX4_UyQoipsMXR9oZhfxfxR6O-3kWP8XBhKFjd7priet4pX0RHtJyn-OlWNnjIdiA0kAX4Ej9AnlkhZBrAOTKyCIKQi2Jm4wBppNidnMHXdK0Jn1a8W-bqOUba-FkWsWhacVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال های اخیر با ۵۰ هزار تومن چقدر گوشت قرمز میشد خرید؟
سال 1390 ؛ 5 کیلوگرم
سال 1395 ؛ 1.26 کیلوگرم
سال 1400 ؛ 355 گرم
سال 1404 ؛ 64 گرم
سال 1405 ؛ 28 گرم
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69976" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=YVQrQoVQT1VSxZlkESbUHbLjk2mCn3zPKEt7s3xWCdHoiEiYA9Sds3woyNxvRWWHlRZFSWw7fkQJzYQ6EWIB6yVB_qYJmIoXAq-txWV2qWwjLe16GxkhUJaJWWiw7mZdhrB6jVRMTEFG08Er13ORzI73lrQRG3PB-8beXQaUYmr8Z61hSSX1kpZJRAg0SbHxUuib7uuA_vudg9Y9gtHgNxSRMV_Io4Wb9wrzR3LMAHj1ckSc2rOlcD-XsQKr1QD28UmWvsb47RKv8g8-np2legCjLf8lhlmDC9nMpnoQBOnjdpCom0e2Gkm5S4C867nm1jNzbDPelINpiReGBvXTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=YVQrQoVQT1VSxZlkESbUHbLjk2mCn3zPKEt7s3xWCdHoiEiYA9Sds3woyNxvRWWHlRZFSWw7fkQJzYQ6EWIB6yVB_qYJmIoXAq-txWV2qWwjLe16GxkhUJaJWWiw7mZdhrB6jVRMTEFG08Er13ORzI73lrQRG3PB-8beXQaUYmr8Z61hSSX1kpZJRAg0SbHxUuib7uuA_vudg9Y9gtHgNxSRMV_Io4Wb9wrzR3LMAHj1ckSc2rOlcD-XsQKr1QD28UmWvsb47RKv8g8-np2legCjLf8lhlmDC9nMpnoQBOnjdpCom0e2Gkm5S4C867nm1jNzbDPelINpiReGBvXTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لعیا زنگنه، بازیگر:
سال ۱۳۷۴ که سریالِ «در پناه تو» در حال ساخت بود، آخوندا و مسئولین میگفتن که دخترا با زیبایی پارسا پیروزفر به فساد کشیده میشن و کارای بد میکنن!
برای همین دستور دادن با گریم زشت ترش کنن و آخرشم ۹۰ درصد سکانس ها رو حذف کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69975" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNcWq1hROnGpAF9ez7FfW8qUp1WJjVE-Etipqg0EYSX9Dlc32AEC75kUIL4MdZyzGjya_n1YO_VVptoPvOIhhzglvNNGwfhs4rngVUdCpq2AIlQo6gwXWug7mkCUfezJa6pycveJ07Pr5DHjPBGdarrZ0sU1N5JPGKR3NNY3gYGu1Z_PvZGHmLQw9uoShRPkndh6zqm29w_KnB_Iz_sy6uAMw35ltfr2zv-PbLHgIEj3OINNFSvOQsWsov6aXlwmnl5JkQuu8kfWRG1GmbfhHwcP6w-hFUb7OtavEEWd6wmrrE4t_qaEf72nHi9GFH3-U-7Qw8CNk_YjyFlC_4IkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
ایالات متحده مدت‌هاست که به دلیل ناکامی‌های اطلاعاتی، محاسبات نادرستی انجام داده است.
مثالی واضح: جنگ علیه ایران. حالا، یک محاسبه نادرست حتی بزرگ‌تر در مورد تنگه هرمز.
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باش.
الله بزرگ است، بزرگ‌تر از هر قدرتی روی زمین. ما به الله اعتماد داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69974" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69973" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1IKHhLpFzB1JHO8qE-909b5SYVF5AvXvXH2ryqOlCl7JUxLq9CQvcr4cVwhu54TRvGP2FS8TTFnBPoGVWanOH_Z_DIkR3XEMEwFUbfrdLjQV-9AAOF0zHmJE4zDuHi8kRMx1ZPhP6l30H8m1tEm8HfbpA4jMKVEp62OG-XHJl69z84R_8gVEfVO_1BtEOB5q3Lox97V7toMJngitPakVJQ5z9ZEIiyHfKNgwf3wtbOkeWmcKWRFb1Nnix0nrc8nFMwDvBi_KryisRn-2GbhA95s1fWNqfXqgxNP9QQ9puXHjwxTUfePOBtF0BGaYBR7Sla4uC1gqgtYtSb0sIw2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r22
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69972" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=QG9oCgz_7ES11IwRfq-8AcHzKGENjY0OyRjJUJtLxKGWTMbSKHYVq11rbj9GoHBIvE89E9k-BlYFwVzTTL9W8EjSkIKN4FW6JvydBMSr4W6YBz-AkSBqmBfTWtApQ07Hhz5hFKoCGPwNvfcELe-WNalQn6cHj2D9uGA4R_dWMVek4enaELqcE-fqrC9UQEyo30zzjpOiIhB7rl1ZqHxNbuN73NcjeOR7kR0I4d-1Ptg2Vv8oy8J7Wi-mXmx7o_544xBEhXriVkzol_UMlV0UWdVBguN2Z4xYx7IEbdtsR67YkPu_qYxCcC8iDev8ccsQI1k-LwgvSMv8wIWWZ3t5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=QG9oCgz_7ES11IwRfq-8AcHzKGENjY0OyRjJUJtLxKGWTMbSKHYVq11rbj9GoHBIvE89E9k-BlYFwVzTTL9W8EjSkIKN4FW6JvydBMSr4W6YBz-AkSBqmBfTWtApQ07Hhz5hFKoCGPwNvfcELe-WNalQn6cHj2D9uGA4R_dWMVek4enaELqcE-fqrC9UQEyo30zzjpOiIhB7rl1ZqHxNbuN73NcjeOR7kR0I4d-1Ptg2Vv8oy8J7Wi-mXmx7o_544xBEhXriVkzol_UMlV0UWdVBguN2Z4xYx7IEbdtsR67YkPu_qYxCcC8iDev8ccsQI1k-LwgvSMv8wIWWZ3t5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی کره شمالی اینترنت قطعه و مردم فکر میکنن رهبرشون خودش میره با قطار براشون غذا میاره و تیم ملی فوتبالشونم هر دوره قهرمان جام جهانی میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69971" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXL0olgyLijSdR2lRWFJZG3JG_H_gw1qd32CzqsTUZK4FAvD22ke72iucugPltPUkhvKCXqPsSEyR0a9HRMv89d43VIFyrAORnYBiYQu36Xxj6np0JnK0rfrIdkG9UZMQR0SR9MboqIM0mc-h_hYEke_xTOQv_yaKaQXZzEUpkyE397PBCeat-Uhqzbifc4ec2t_tGpkZ9gzbLdX_Aa0GbMWklCom3iVPWfG8nXwwE8vV1xwqINect8vVaLF2JSNZOeSuX79pULxpPq2Zdfv_YilePHnZdduQlMba8G5nZ599d11mvJ0O07mmPtEBNFD6Txy5pO71X9xJkvBZBG8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نشریه گاردین: چندین ملوان حاضر در ناو جنگی "آبراهام لینکلن" تلاش کرده‌اند تا از عرشه به دریا بپرند، زیرا خدمه این ناو با فشارهای روانی فزاینده‌ای در طول این ماموریت طولانی که برای پشتیبانی از عملیات‌ها علیه ایران انجام می‌شود، مواجه هستند.
حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو، در ماه نهم حضور خود در دریا هستند و رکورد ۲۵۰ روز متوالی بدون توقف در خشکی را ثبت کرده‌اند. خانواده‌های این افراد نگرانی‌هایی را در مورد فرسودگی شدید، شرایط زندگی رو به وخامت و حمایت ناکافی در داخل این ناو ابراز کرده‌اند.
گزارش‌ها حاکی از وجود مشکلاتی مانند سرویس‌های بهداشتی کپک‌زده، توالت‌های خراب و امکانات شستشو، کمبود آب گرم و محصولات بهداشتی اولیه، و محدودیت در تنوع غذایی است.
چندین تلاش برای خودکشی در این ناو جنگی خنثی شده است. یکی از همسران گفت که شوهرش پس از تمدید مکرر ماموریت دریایی خود، تلاش کرده است تا از عرشه به دریا بپرد و افزود: "او می‌ترسد." او پس از اینکه شوهرش از عرشه به دریا پرید، با او تماس گرفت، اما از آن زمان تا کنون هیچ تماسی از طرف نیروی دریایی نداشته است.
در یکی از حوادث متعدد، یک ملوان که در حال نگهبانی بود، متوجه شد که یکی از همکارانش قصد دارد از عرشه به دریا بپرد و با مداخله، او را به عقب کشید. در حادثه دیگری، نگهبانان از پرش یک عضو خدمه از عرشه جلوگیری کردند.
این ناو جنگی در اصل در نوامبر ۲۰۲۵ برای انجام عملیات در اقیانوس آرام اعزام شد، اما پس از آغاز جنگ با ایران، مسیر آن به سمت خاورمیانه تغییر یافت و زمان بازگشت برنامه‌ریزی شده آن بارها به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69970" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ndCl6IIdu8BlcU07A_fqpR8lN0EOxBUSzG0bznwSsQTzy4c-bTfEjr7yWTxqZa4xD22e5C4UBbBMujhPUHiKurY1ydoEMs5ikPp31vGMKKortWvkEzhV84dfoDwIt3r1T6SmQ1C5Gj1Sp6GeZhHrO4Rx5PL-EpZz8c76CI6xP87wnWbeAzNnZf8kTlSzr6ML_6WnSm3uqQ-gk9PsF4cQM3zsB09Dl3UVZJWiw-cDNMdZfWByfsyvfcTUvjSk3Dym0f56YeVKn9jeG9WJ8RnMT7kEJHkr18ZlVX7Mcltnff-2OMpJLT-W3NZOIslnRfrMwDuWT8CzfM7teU7Wq0MEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=ndCl6IIdu8BlcU07A_fqpR8lN0EOxBUSzG0bznwSsQTzy4c-bTfEjr7yWTxqZa4xD22e5C4UBbBMujhPUHiKurY1ydoEMs5ikPp31vGMKKortWvkEzhV84dfoDwIt3r1T6SmQ1C5Gj1Sp6GeZhHrO4Rx5PL-EpZz8c76CI6xP87wnWbeAzNnZf8kTlSzr6ML_6WnSm3uqQ-gk9PsF4cQM3zsB09Dl3UVZJWiw-cDNMdZfWByfsyvfcTUvjSk3Dym0f56YeVKn9jeG9WJ8RnMT7kEJHkr18ZlVX7Mcltnff-2OMpJLT-W3NZOIslnRfrMwDuWT8CzfM7teU7Wq0MEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستانی از زبان یه دانشجو-معلم در زمان پهلوی، که برای اینکه مخارج تحصیلش رو بده، شب‌ها مسافرکشی میکرده، تا اینکه به محمدرضا شاه برخورد میکنه و...
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69969" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=IU-KL0qoe2_-7fRmDHXSVQG89vVSqSmZJUDoeX5_Tv6v8CTfG9EJUsuz4aLdoPHPawPPfNc9RRgCOVvn6uqoX3PS-j_6q4MeFsnROzzGAFQoN4817d6lxd98680S69ie7bczhQFWRW9tz7kl47TEzngqHHiE0QdXU8-mQC5twSjy8bwdfOWCCStPLyMurg3ZD1XAoAxNgV24HMGVDyle-ade96MQuT-ro9Ojy5rkNg_x-h-d9Gxsw6IZxxB_Hof5tQggkCNi4n35pCdqlQsHZPXgZa0c9Y-A2N948g5ftQJGkbf5MNkCP34ze4VvwxLNl2rwjpwieTtJdQwo1q4u5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=IU-KL0qoe2_-7fRmDHXSVQG89vVSqSmZJUDoeX5_Tv6v8CTfG9EJUsuz4aLdoPHPawPPfNc9RRgCOVvn6uqoX3PS-j_6q4MeFsnROzzGAFQoN4817d6lxd98680S69ie7bczhQFWRW9tz7kl47TEzngqHHiE0QdXU8-mQC5twSjy8bwdfOWCCStPLyMurg3ZD1XAoAxNgV24HMGVDyle-ade96MQuT-ro9Ojy5rkNg_x-h-d9Gxsw6IZxxB_Hof5tQggkCNi4n35pCdqlQsHZPXgZa0c9Y-A2N948g5ftQJGkbf5MNkCP34ze4VvwxLNl2rwjpwieTtJdQwo1q4u5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زاکانی:
موشک دقیقا خورد تو خونه مجتبی خامنه‌ای. زنش که معلم بوده اون روز سردرد داشته نرفته مدرسه که اونم شهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69968" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=dLXA4XCQPFKob_d-SUGq72llxlkz6UvmqcaDCGLV5SAfY1zairf3vme_HH5VjhCu8EV_RQjaCHCTElbFSOW1m0pwxTmPOgD1H-Rdxey10_tMGujFrYsLVKpgznYFyL9axVkDS1SYKYUP_01mEe8caWWePKNsGFrPyBBu23fMMr5v1wT9oQjjSQiYaci3E1S-rUFK-k1GcWJ6U7fhAFEbN4l3QiJgUwc4tkkOdM19aTVx8JY7vpXga9fIk1Lei8fH-xmKIelPDBf7Mu8EBMBBIbpUCEBpBS0fdh2kNE7yMlzPbfzL_h1SQEFCLDxN8eJrXcDYT5RBySU8J5RkRH0MPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=dLXA4XCQPFKob_d-SUGq72llxlkz6UvmqcaDCGLV5SAfY1zairf3vme_HH5VjhCu8EV_RQjaCHCTElbFSOW1m0pwxTmPOgD1H-Rdxey10_tMGujFrYsLVKpgznYFyL9axVkDS1SYKYUP_01mEe8caWWePKNsGFrPyBBu23fMMr5v1wT9oQjjSQiYaci3E1S-rUFK-k1GcWJ6U7fhAFEbN4l3QiJgUwc4tkkOdM19aTVx8JY7vpXga9fIk1Lei8fH-xmKIelPDBf7Mu8EBMBBIbpUCEBpBS0fdh2kNE7yMlzPbfzL_h1SQEFCLDxN8eJrXcDYT5RBySU8J5RkRH0MPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید فک کنید هوش مصنوعیه ولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69967" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=DwBxCnhSIWFuYYMaRtl4vj6GMDuWjtJdf0uEttd-Kf4iYPJeyLDpDoz4Qepj-t2PFq-YrFxNUJ1FrRJ2lY2WBiPt4l4-EP6V0yscAYvXrRbV8uiqk_YshoZ-ROIMsY_9d8HJ2oKPc3g3hv-AogQNPXDVTUdfQZeAu0GhTj1TTSDaHeeJAlnK6KlRsmrx8dwfbW4LAdFWK387pPSngayWqAcEC9gKombgxNFFj16d7aOOMj5e4N1w6WIDKgEEkGjPujWARXYpTb-o1i0GhWDPFufA_OzWJs254VW6a-JSjWQCxYEkZg90BBiD6oC2RN7_5jMSb7ahfDFxhB-BK8m-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=DwBxCnhSIWFuYYMaRtl4vj6GMDuWjtJdf0uEttd-Kf4iYPJeyLDpDoz4Qepj-t2PFq-YrFxNUJ1FrRJ2lY2WBiPt4l4-EP6V0yscAYvXrRbV8uiqk_YshoZ-ROIMsY_9d8HJ2oKPc3g3hv-AogQNPXDVTUdfQZeAu0GhTj1TTSDaHeeJAlnK6KlRsmrx8dwfbW4LAdFWK387pPSngayWqAcEC9gKombgxNFFj16d7aOOMj5e4N1w6WIDKgEEkGjPujWARXYpTb-o1i0GhWDPFufA_OzWJs254VW6a-JSjWQCxYEkZg90BBiD6oC2RN7_5jMSb7ahfDFxhB-BK8m-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های داخلی با انتشار این پست اعلام کردن که کامنت گذاشتن و لایک کردن پستای رضا پهلوی و اینترنشنال و... جرمه و کسایی که اینکارو بکنن دستگیر میشن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69966" target="_blank">📅 09:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69965" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Tl919HmpdevcSjh2xs8RwfrLPgIVl8fZ8cCkW_c8MlOQGmjNEHqwMGEEYUb3RmzQLXNOTyxA0DZXwYrIbGE7clEl3nI8WpN1jXibMnbSFqgN-EkMmRb8tCMIap-92qh6kTz1i9aYw774bTDYEunE005l7BxTOfGCcuaXgEs57GIe6P9fz9xUWVpMEKTRmEdVV2DgQngZwO7uKcc9t55Dfd4CZLtHSR6-_AX82a8JDCuSYrEYw83YqkUDlvXNg4Un1MFzzkVwYTP4Y4cQHbKtrpbSQbPUvxPTjupwfqXuH0CL6k8cL55JGuL8dXGQn-yUbwSE0JiYv7gS0WXBWbk8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Tl919HmpdevcSjh2xs8RwfrLPgIVl8fZ8cCkW_c8MlOQGmjNEHqwMGEEYUb3RmzQLXNOTyxA0DZXwYrIbGE7clEl3nI8WpN1jXibMnbSFqgN-EkMmRb8tCMIap-92qh6kTz1i9aYw774bTDYEunE005l7BxTOfGCcuaXgEs57GIe6P9fz9xUWVpMEKTRmEdVV2DgQngZwO7uKcc9t55Dfd4CZLtHSR6-_AX82a8JDCuSYrEYw83YqkUDlvXNg4Un1MFzzkVwYTP4Y4cQHbKtrpbSQbPUvxPTjupwfqXuH0CL6k8cL55JGuL8dXGQn-yUbwSE0JiYv7gS0WXBWbk8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69964" target="_blank">📅 01:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=WPiTORhrrej3zwQVMCg4OC9IrnkcyHVouNc77EbF_fo9CQaO_ywvDgV9v_IzlHl6-ZQa5FaknncmvmnixS17oC9A35eQ83-uvNn4Rg8Bb0ZlA136KnyqrMKOIlNQyt4bZiQ7W_cpTifGdYP38_w3MBG_K-0tVou0So3cEbHYf0org-WYfFV-N0XQH74IiOdd94ybTjBE_JHeqoXC_bbnKTz6DS3xRAhenKdLzIWf5LawV2GLAntKby0idQj1_u1sI-K9wmR4-HQceCV2OZA26bLDflMUeHVeVIBrlPDKqI31GeX8ATsn0M3bjqbvXHiN4VdczjhnaxZWv_pTFsQXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=WPiTORhrrej3zwQVMCg4OC9IrnkcyHVouNc77EbF_fo9CQaO_ywvDgV9v_IzlHl6-ZQa5FaknncmvmnixS17oC9A35eQ83-uvNn4Rg8Bb0ZlA136KnyqrMKOIlNQyt4bZiQ7W_cpTifGdYP38_w3MBG_K-0tVou0So3cEbHYf0org-WYfFV-N0XQH74IiOdd94ybTjBE_JHeqoXC_bbnKTz6DS3xRAhenKdLzIWf5LawV2GLAntKby0idQj1_u1sI-K9wmR4-HQceCV2OZA26bLDflMUeHVeVIBrlPDKqI31GeX8ATsn0M3bjqbvXHiN4VdczjhnaxZWv_pTFsQXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنر نصب شده در تهران:
پزشکیان راستشو بگو، مجتبی دیگه نیست و فقط وحیدی بهت دستور میده؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69963" target="_blank">📅 01:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
#فوری
؛خبرگزاری فارس:توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
تا اطلاع ثانوی، فرآیند عرضۀ بنزین در جایگاه‌های سوخت استان مطابق روال پیشین ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69962" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184379545b.mp4?token=LmUdyhspnOp7Fj2vuZwvEPXesW6ONTzsNvJySy833ZGhrt-GCoeEvK5vBZ4KtHBkOIofTaqrSVtm50imqK4-Yk5cmTKAKrin3dbfWMAN5peKkMNZsQdTPnKsT2tK8rTTUmYBLLOJG2lixkUL7i9rf6768R3Vt7sPt5NZwfheVzIKkBiuWtV95eUPA-F9g36aLvH72TdMpevcGy6mdmoeaT-ln1Bmo4CKJ4s_XML0-T4VoNW1fLiLDoUFu6vKmEMM33t8TSPvOvW5ZOB1FRkQx5vnLhyih0huMZ6bM1FQyf5yzL3WMyoEA0LstEP3g35r6y2hFlAwOML3awF2ZqB74Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184379545b.mp4?token=LmUdyhspnOp7Fj2vuZwvEPXesW6ONTzsNvJySy833ZGhrt-GCoeEvK5vBZ4KtHBkOIofTaqrSVtm50imqK4-Yk5cmTKAKrin3dbfWMAN5peKkMNZsQdTPnKsT2tK8rTTUmYBLLOJG2lixkUL7i9rf6768R3Vt7sPt5NZwfheVzIKkBiuWtV95eUPA-F9g36aLvH72TdMpevcGy6mdmoeaT-ln1Bmo4CKJ4s_XML0-T4VoNW1fLiLDoUFu6vKmEMM33t8TSPvOvW5ZOB1FRkQx5vnLhyih0huMZ6bM1FQyf5yzL3WMyoEA0LstEP3g35r6y2hFlAwOML3awF2ZqB74Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خانعلی زاده کارشناس صداوسیما:
افزایش نرخ بنزین و گازوئیل بالای ۵۰ درصد مردم آمریکا رو شوکه کرده
زندگی اونا فیکس هس یعنی پس انداز ندارن وقتی بنزین یهویی از ۵۰ دلار میشه ۱۵۰ دلار ورشکست میشن
مردم آمریکا مجبور شده ماشینش رو بفروشه خونه اش رو بفروشه بی خانمان شدن از گرونی
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69961" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7326381213.mp4?token=U7H5Xht-PnTp3Umq-AMJjDWJUq_mW3_thv8COUbam8cjdDYzRFi3JKzrrtyFei4PdF2sfdPQLF34_CX4fdzd6CJwcHyAfUUVVXtRI005z-Og2EgF9TvFyTOPqSvt3KOo74w9ONlbteGlwq8lcBR6NDhsYeLebeyXDSszDME2Abv4xt0RcG_0fZJJNYH9et796-5oFEm1qzODVLpMuuPC0qocwWL6faZjez1GWyvKK8pQ-TiEZcKuCT9mjXJ6Su_rzCDovqUL602mDtkdRAIgvC4hltPrEzCClLlSdRfaiMWW7ghLG5eov57_Y9tKqS0xW-Uzw6j2sHiWD2QuuFDTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7326381213.mp4?token=U7H5Xht-PnTp3Umq-AMJjDWJUq_mW3_thv8COUbam8cjdDYzRFi3JKzrrtyFei4PdF2sfdPQLF34_CX4fdzd6CJwcHyAfUUVVXtRI005z-Og2EgF9TvFyTOPqSvt3KOo74w9ONlbteGlwq8lcBR6NDhsYeLebeyXDSszDME2Abv4xt0RcG_0fZJJNYH9et796-5oFEm1qzODVLpMuuPC0qocwWL6faZjez1GWyvKK8pQ-TiEZcKuCT9mjXJ6Su_rzCDovqUL602mDtkdRAIgvC4hltPrEzCClLlSdRfaiMWW7ghLG5eov57_Y9tKqS0xW-Uzw6j2sHiWD2QuuFDTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🌓
لحظه زیبای خورشید گرفتگی در اسپانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69959" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69957">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAh2tS-sz56dnkjvHkpL9hHqJFLIPT-u1CPbemsg1M40dQD3KwnJ1lxcnXPhOnldFNnlwkoVXXplMgXFueJ6Wu8X7AtUJgKWhqQvJ7sPNKD74t-1C7XdV6_FBzvc0FzdKW3jTqlrvCcH4f4Y3uBhbm-B0aArj-3rejnW_dRSO35U6VfgLaOG96F48CYjCThSOqCklVExlkMGBdQHB7Kh0dv6gRYzT0Qb58clHrIp5TGY5fNUYdCH76mgBXorn5I5Zi0O78cKuVHchLfbOog_B35D0AmzJdkCoE8vpP8es2CbviAhMYgHCacy4FlI-tEK7mnMlRMlnG0rhLflQLrOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJ05E4FoG7NDRIKeIt35T5jI3z9lBXWw4gbLeHPMS9AFwt-y1YXKZRBxsHncMr5xsFW0tljJN4kPD9VZpFdO5rVNwIOP2azOYjxPrBcNQoxdHLQDp8eik5mqGZZyHARLc9M7x9NwNGJc_iBMJhlkNdwKDlk7HJYIrRgYq9AFQvaU331dbJJhD8UwaaNCHanvThKgnERjs9xTmGpe1HUaIVgMkO_na9K34kIabeOBpMtDpTmtjp8twfCERFuqUk-eZ5zIJCkH2e0V5-xM2gb6OEs821GYrVJmEaFr_uVIewh7P6zVM97c7opnl2Ds1khQWFjIcEQ19RzM4GFcJSNmhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇺🇸
🇺🇸
با اعلام ترامپ کارولین لیویت سخنگوی سفید کاخ سفید این ماه بازنشسته میشه تا با خونواده و بچه هاش وقت بیشتری بگذرونه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69957" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69954">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUK5bGKadc4ZMBNZFZshFSYrhTm8_g2AI8lbYYj1dNr5ksKgPVDr3Kv7HlSEfm2xcbjepuXrNFOp72BfTWwy2FqLNo95TRrUif5M9LnLjrJZ9bDHh7j5zEtfqHoYoaZw1MyXnVTEsvisLovdjSL9U4xm1aIAm7jOjVFPfb5WQJnl9zxEJPe28iYYgjFIU6_ykOjmmFa5d3a4H7dCrMkStKZsXc_5C3zna-LtOk3g6FRBTRUm35a4zfvjTAsRvuKV6AifHzaIRQJTT-Qd0hAX0d0M8-sFH0llxpLk2tdVc62eW8eLsdFOA4utzgAo3cpwNADBJMuCSDWd2QT0BhBtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRo7CbM-x3BVMB12PAsnV56yLGG_RGYxxEFHJd-xMeLR1-uOWZzn68MbGfM_6R3r-CtSKbfZtDkh08wg85Px_JiG9DFkplKvfaCrIZoktvPV7KQPEzgWlfp6mmVn9rY3PRuQQIrqrD8cFDRYJryTGbdSLJVjZeF0LTq7A05Z34hWsNPC-2Nzci2m3LsVxI0muob3Xsiwbh15Zb1FfMLGqSGhDTDTOKe-ud5LXZHV7GvkBYxgnt51IbaQbGV9SGYGcZcbWZFDIRBDHRxl4avZGmuEf6BffAg1U2q7Y7Jfr-JHEZn2qQkkie3sizE1aXx9X9NIxCEOTxbhdkDGz8JPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0z26cQ5nie_Oq38UqDMYLGBzxwc9mh8If0C2E6Usa7xOmEZY5ieOtCH7o-nP_wskLcEC14mtoZuFt0YEvY5-zUymOkMqPJUgHHpuCK7lGqB4R6RIDzhSuxlUNeJDC62nZjySpzSGN_gxPrKN9goe0Qp9qjg-hmClyLUwsrFIo0tVwrqxdE8x0IGK2VnSjZkcQhLdPWhucBunxU2zsZxRicrM5VQmC16WtKDxMuVomIwqIsS5eUaMpmjqYEQUoUEznSyes1sj4xaxpajt-YEs8iRbtroVgCx-cbJDMdJNA6FSBp50c3-eErtLNKcBEALD2-nYfCtsw2hDq2Z_GO_9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69954" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW2_BQ7qgc3DhRGumID3RJ1PHXXWov_cZpJ2URPQWnnST-5icDSevcO9Ha_PzLSKDF8BO3egInYGMgTTdce2gXg9szK3t7PkBkSU2fOWhtZN54-C59zP1D2GW2V3DPI8FpFGlzi9mFSB4A4nOFfwGlyqLdTr2qe1RMLLaaNjsFh6mPx10mYUX2FyWDDm8ee--_adNm2AlbQ3tc4ZycHLUb3Q9R32FbJOZD8tEWViB0R_MI_iKiKSEDzn-74OnHl4BOWwzllSVnBicKnbrWyo1nS2gZzCi8_9P9ubqPSkl-1dk66bjYpOHewvDZqv26CJ-VCRxk5jUfG7rQYKgHiOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
یه اکانت تو ایکس:
ایلان ماسک باید بریتانیا رو بخره و آزادی بیان رو به اونجا بیاره.
🏴
ایلان ماسک خیلی جدی:
[بریتانیا] چند
؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69953" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LleA7F26tngJJsXT4NO8V0CQToxfh70C-i0oC3y7rrpSwip0BcuFCGLFBu5LlfyDnTRReLnRH7trLPYCSlW6nwqvd4JlfGwIVkg8J1vLdCdD_VexHWjIZXpJRLdJoZ3CfIiHebI1zXsi3hC5uIaPxkistUZrLKT7F1QL0D4mxqzo0rH5V17X21KhBsdDHNGys-_5fnoODCNlQHL_nPZ8OGqrIdvwD_ppEI3-UklbiHgfZY3TKTOnHcnyWIfzCqAuMDQMvYfXtG4exSm_O4lS_zLvLvVlI0S9YTpPn0QGoqv049HHZ5zYLT2d-Q8vp0RTQhXYLhQbY0Q8AfVmmTR4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=lKrSuZjn3rAZrgcLDTinsK-A_1XOjLRuLt0FbAqCi9fjfCZBaRc1rE4nv_nYdCpnYzm5S1MuM8EcPZJn8nXlc2qrnhZln43v5D4tiZ7UgRFlDDSQTi_qT0_b_pu17Kp6tUMaoRhJrGBIFHHpDy9ttAlhYawh8w0kPJEbHn1LSRFRSsl-YlP9O1klMmjihyM2u1gEPXhr3pvr22vQOSBeF-7-mDKi7wUyiJ_BQeC4VVowW77izIyBe9CxSBReB0TQTK6tel4z65XkYbrK3uDX1KYYzx99mD1FUWPp0WUbcu_XC19uUeUsmnUQCu0Oghht7-2rqB1O3NDpvBiUhhQ2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=lKrSuZjn3rAZrgcLDTinsK-A_1XOjLRuLt0FbAqCi9fjfCZBaRc1rE4nv_nYdCpnYzm5S1MuM8EcPZJn8nXlc2qrnhZln43v5D4tiZ7UgRFlDDSQTi_qT0_b_pu17Kp6tUMaoRhJrGBIFHHpDy9ttAlhYawh8w0kPJEbHn1LSRFRSsl-YlP9O1klMmjihyM2u1gEPXhr3pvr22vQOSBeF-7-mDKi7wUyiJ_BQeC4VVowW77izIyBe9CxSBReB0TQTK6tel4z65XkYbrK3uDX1KYYzx99mD1FUWPp0WUbcu_XC19uUeUsmnUQCu0Oghht7-2rqB1O3NDpvBiUhhQ2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phkw442N_bBay90YLsF9scJbuEUZxXfuuTQm8ntZyaim2X19yOletzI2XrpFSK3TbPg9y9n3aP94fib_ax-ejOPgYkm7scIC24OyxPEjTZHID7g7Pl9C6544yzPLABYzQ5uyu-s88ADhocrWfKD8nlMoeOkByxS_gm2B_tE2Ivxsa11plrHaSFLN5rlwkpi92qGxJTWEete9E3xMlQ2apsLBdi8I2WiQOfvnixoKOztfpYUjPlHqArg4G25Gx5yunBP9WJW8V7wf4XrbV8ydCU50_yKlpBNaAgNeF_RVsWoFbpyxzKZGiNT30rz9CdgMqB_oypHbQ1SUDbDZkwyc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et06YdsKblZNEbnI30xcjHRLCeHm-D7P3InAioByjMX-7Mpwe-WrsN_pHBFlKYx3nZRIxhiQtp4zvYzNfLRvV5Ztk9ECYygL19Y02xktiNotQj5-hVLl89GafYrvmRQkJUXZvbi87v5juynh-2nFngUDgQeOjQpyIpfPncYooQbLw4UiGHrU8-KO6uxHpOaFr8HbqONz8Ooy2OM9b_Ko14_PzdyUNjTIxibcU1ksj82wN8yE13z2F5v6Ktzs73-6RD7resQ-2TmbGM8Z2P_YHjV4dd329UCIOMAKzS8XQQ_5aHehFuaE2XOB-xlho6P6d-EIVipH110uwxIE-TSghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKAconwtuxKAgYmF3RlMpzZJOajfOdJ3KUivsEeSUIXcPs-HeL3mciRydSy1nLT5iaHhCoebC3_Q_2CTDIzb-0P6QOMEIX7DgAP03_4Wej-SvWLZ2EfFozvLYJWP0OkdS3nzZitocIq9hp78A7U8PTc16n4sHzlM4CYwLqn4isoVUVySkQE2WINgYhLUiVgJfmlhSp5fHOytukjyUplj5krWXh1GPzv4fsJdTnTdhv_5Tj0jU263TjkV4b3fSBH7FPLHKZ4pT6AvMPVK_3nIZcjbi7N__YqWqHw-RP51dnXj7M_bL6JfuhboOF_mgRighGE80N7fjJnRBIbYbCwTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oFk3SLm1P3IiPkCLw7RtL6LoTzrjq7Q9vekMiVjc1_OH52gZ7D5tjyvniHHuh68ERVF-l39A8j1C9ZGRXi9D7yH2MvSSOwhRqIYYATItuP7bLyzpng9vDsqx_RDeZljVAaItas7bABXG-jlglOxXoG4K0IKxND4IWn4f78QNQyOnRO2bJ5OgK9ALhQehnmYst3OhuWKsCMJctYLxMoXUygv3uI0UgJJcslDa2YswIHHXyhBUQT4hdiLxQ5RdXVAudGJdxyp_oqNiYsJv8qH4QNt3VEWORBKsZTUVHPC6C8UZCvUt481DgJ7IB9qH3LiQ67UsOf7mo4vk1wCVB3d3KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=m1NHS7AypvnrjNFervCvnFj52XX3kArYJZgkTaH5yc_1_0eDUWrxePDHFe3bpjbziGlPFZquGbeqAIHreeFwvQD_vUkPQvmJGQSk_6uwDqZNVh5hb1SnMAWwCljKVicRHr7oVRIMSQh2GjZYHylT0fcgjoxfp2cYUBtRs6hjItM246SjllhUUsjZ5ZQIF1qbLA_l5G17wyGxb2V1ACWMtHtui5CB_pPpW7PPFjlsr-j1ZpnMvom49DvgPLZM5_SsmTb6N3Q0PLU6witjUOZK8o24r83Jccpotod6C09B-r9VwawjyKp6fIZ9My2vCxk_SSz1_rmB5o8l9-3Gbk9IdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMo031n12AHsRO78pIvDlLta1CDdlvWSXp3kSz5wp2YywxV8gT8_0NcHI4L_gxSPHiLZ9tuvRYFG3PzhVwJqo2nZasxaf3Qr1KU_Ak4RGccV2ioiinWGrHVN9t0eBW-lYuuWkGBnN3A_4us38lX13v400HBRG19CQYkvFqUXhEj2okAHBra-QkshAMN_LsqmhSGqHM5vj8dZkxKGOiKawcRa5fWXuAgC0dIwA-ACovNPpFND6tWroelo63T6pzcXfCm_ivPULnLcxSGmI4Duio8PuUZFM9fU-0B6yA1eixg1wFi9NZiHnLob5Ra9Wl2_XvZLZxKa5Y6cToCRrZNdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=UgEC7EVbaN3ghe2uS0MJWPQGZnm_6M7RWzN3kqkgWFzjWYIyVOiJOobIw-Q75ddKMEB3OtuciXdOZ6Jk-7OdWIcuo-0MWxj0iepLibK1uXyivkIxpbtfhQyYtLe1DGKXivglGJMe7BbrnMK_ZHBfW4gEFIOXr8_bhHgUmh-TS9N3BeQRrPgjC6DYh_0MZ-TjIrxndAqg7BLg44DB-ROuAXaOzmhR-Cd5Wt_gIkZu644PCZha49cRszzsa5E6_-wv_Ht7aUaQOs_toYjXBzG9mc4XJOoLQCWrsRYd7zfe_aQN0RA0Gmko8NxZbRXE28D7uGcWuagtcSJUm79uuNJ2pilvBUm0Ug_Ubr0dGyeGdxXuzymPLvzp7xbw_SSNioqHDQNxmCo47km0Qs4aWC8FedoQi6BWHjGQCVqklhlG0TwQeuhswq_rsLDZEI6LA2_3UotXemK9nekM4dKxCsNMqpbhQt8Afk5Bec9AE_CDUSGonqQjrXcdwKmDPmD382EKs0xKfVN8auZ_ZU8oA9Gi9g2vro-gpGLPzS4wksP2YDr4Ik4FfBBbUXTHps7jya0ZmUw2dlfhP8M87KXtfF5vdgT7CKHktdnCfR5QagnBgYexrRW8AojlMsrYeTbSIEnVk4vVTpr8OfOM9Sm5ZKQRJxa1mLgQmnMIL20HZ-0jmgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=UgEC7EVbaN3ghe2uS0MJWPQGZnm_6M7RWzN3kqkgWFzjWYIyVOiJOobIw-Q75ddKMEB3OtuciXdOZ6Jk-7OdWIcuo-0MWxj0iepLibK1uXyivkIxpbtfhQyYtLe1DGKXivglGJMe7BbrnMK_ZHBfW4gEFIOXr8_bhHgUmh-TS9N3BeQRrPgjC6DYh_0MZ-TjIrxndAqg7BLg44DB-ROuAXaOzmhR-Cd5Wt_gIkZu644PCZha49cRszzsa5E6_-wv_Ht7aUaQOs_toYjXBzG9mc4XJOoLQCWrsRYd7zfe_aQN0RA0Gmko8NxZbRXE28D7uGcWuagtcSJUm79uuNJ2pilvBUm0Ug_Ubr0dGyeGdxXuzymPLvzp7xbw_SSNioqHDQNxmCo47km0Qs4aWC8FedoQi6BWHjGQCVqklhlG0TwQeuhswq_rsLDZEI6LA2_3UotXemK9nekM4dKxCsNMqpbhQt8Afk5Bec9AE_CDUSGonqQjrXcdwKmDPmD382EKs0xKfVN8auZ_ZU8oA9Gi9g2vro-gpGLPzS4wksP2YDr4Ik4FfBBbUXTHps7jya0ZmUw2dlfhP8M87KXtfF5vdgT7CKHktdnCfR5QagnBgYexrRW8AojlMsrYeTbSIEnVk4vVTpr8OfOM9Sm5ZKQRJxa1mLgQmnMIL20HZ-0jmgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TholqMOu9FC3VQvZKKVNN9NPiPW6wxkAcjt3nLS6knMCseWJrkM_Tua8eNkdOyTbe6QjKzq984HOLDBqnL2O4h1lRxQlJ8FKpXnVoemLmTcg1b5imZ0FoMzDBTEzJzLj4R5TPxqwhESLixuSFwyl54igNWHG8xX83mi1XzRlAzE4DMcBhhaazdTzAkkIeJKRxZFPmo_WJRRrlGwtrf1cQv7Ywr3QmiWNd0h1DXofGO4scK8YzWoxiMZUNyykuQoAqY6aP3HuFBrA-Zi9Ubg-W1h6_E8jg583E4uLg56jAqTKUZqPdnmz0QDDkzB2VoNCpWAcUVsjeXEKXK7dFWoivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=XCqwvx9qlTV2uv6MDBaBnXnPwCzfKn53oaiYnacMx5LZ8o6bqdlDkoa5DYFIx58P8JtmfgPZ_WFmPQhcUQxjVr70BgzGMlFY3-Z0cOXwP6qc_LJD7_rZIRW_PYp1PwevnrQIwtzLnySPSJV5F14xDOmJGG2fzcTI1_xSgxuyXqdvFnQKl7tGJvCtgCtpFZCTV4tBDV_xX8ORP3kPbQY_tLqHGGWTlNQ5I27WDKbX8A8Z3nhDWje4eL2ztaZkEW3Njbl1X_Zc7I30zk-QCDYvOpdmWi2gxRTd5V69ztjUvAnaneStoCOLMhMk3xOycM0SgaT5USOtTXAQkNQaXFuNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=XCqwvx9qlTV2uv6MDBaBnXnPwCzfKn53oaiYnacMx5LZ8o6bqdlDkoa5DYFIx58P8JtmfgPZ_WFmPQhcUQxjVr70BgzGMlFY3-Z0cOXwP6qc_LJD7_rZIRW_PYp1PwevnrQIwtzLnySPSJV5F14xDOmJGG2fzcTI1_xSgxuyXqdvFnQKl7tGJvCtgCtpFZCTV4tBDV_xX8ORP3kPbQY_tLqHGGWTlNQ5I27WDKbX8A8Z3nhDWje4eL2ztaZkEW3Njbl1X_Zc7I30zk-QCDYvOpdmWi2gxRTd5V69ztjUvAnaneStoCOLMhMk3xOycM0SgaT5USOtTXAQkNQaXFuNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=CXH-wJZeguasAfk0kiuPg126yFnYu-D0pkvSOkU1b8NVSzoQDZZO9ds1Ja74yfroo7hHWE1YMLSfwwh24vgNyWN3_mXIwXCugizhA7u2o8IstJzgXQgRDTOiLZxejUZAIks_PRJA_bJNaQ7wRO_a8b28lfXFme5i_o31PQZufvf7DREe2tj37t-ZGWxNvJ-Tg05Jd4mgYtVKeINizt7dBrMOX9pY0hCl4JPA_IOpQyKTzyqT1dAklUcbNDaIvn0_SBrHa1uw6NVy31TLsj7XKvFa8Sjcavd9hpRPz3w3Dh9u9V7hBB-TY6Jg8UNQN__VpoMWQ6DfORpPn4M4mKbmzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=CXH-wJZeguasAfk0kiuPg126yFnYu-D0pkvSOkU1b8NVSzoQDZZO9ds1Ja74yfroo7hHWE1YMLSfwwh24vgNyWN3_mXIwXCugizhA7u2o8IstJzgXQgRDTOiLZxejUZAIks_PRJA_bJNaQ7wRO_a8b28lfXFme5i_o31PQZufvf7DREe2tj37t-ZGWxNvJ-Tg05Jd4mgYtVKeINizt7dBrMOX9pY0hCl4JPA_IOpQyKTzyqT1dAklUcbNDaIvn0_SBrHa1uw6NVy31TLsj7XKvFa8Sjcavd9hpRPz3w3Dh9u9V7hBB-TY6Jg8UNQN__VpoMWQ6DfORpPn4M4mKbmzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=aG2chXoPXpWZPwScdRz71RiCZBJ1bMHcCBjThSBkQ65b0ZJW59dPfgnegmts0epq-crboBawx-nZrRJYLuD03q0eu78DEtT4_E-v_3k8TlZhgD47g9GUfTB-htqWx6vVxdvR20MWiGqv4p0vCem3WsvwCssQPnGsJogEvmSe4qAI3nly1Fg-ZaY9QzG0dA5GfzBrGS2r1IboEAVX0cHMKTXQ0eYnRzeH78rZZn1gQ1m83hUFLRMtImWt3abjLTgncwSRuSVlO2kjUtG80vxd84YhcB46_GBZ3bB9N0Cwa2wp1oZgFXmrupsxn6i38vwmHAdfFLCNgkTZGdeeXAAN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=aG2chXoPXpWZPwScdRz71RiCZBJ1bMHcCBjThSBkQ65b0ZJW59dPfgnegmts0epq-crboBawx-nZrRJYLuD03q0eu78DEtT4_E-v_3k8TlZhgD47g9GUfTB-htqWx6vVxdvR20MWiGqv4p0vCem3WsvwCssQPnGsJogEvmSe4qAI3nly1Fg-ZaY9QzG0dA5GfzBrGS2r1IboEAVX0cHMKTXQ0eYnRzeH78rZZn1gQ1m83hUFLRMtImWt3abjLTgncwSRuSVlO2kjUtG80vxd84YhcB46_GBZ3bB9N0Cwa2wp1oZgFXmrupsxn6i38vwmHAdfFLCNgkTZGdeeXAAN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAlhFF0NBPL3YzqknkaKm46AkBhIsIYMQ1vJyUlr58_Wiz3vr5lBsewITtTu9YVXeLE5lkaeZf-yWjR_5BJx_ULErkqHKQbcNZV1DSl7rUuJAjsTQQktQNIve6utpY26XjGJFjLOwsO46-nRUGoX6XexsFUFTBhuM93z4hM2x-5mYaCaD_mhx8uK_pfcxwSZcLZJ8BNi7AqnaPeA-h88Zj_3jMzVpbj_doIkZ1crN5y2wfUEL5l556B0DQBVrRfmxrsCtnaTWpO2ol35GYf9hYMAgQDpMEohHhjwhulirBtAAXAQvOpclv6vC9fckyMVkjh3zKptXi7F6DxzeW_nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=Ht039rlGj66RWn6a9v_zTIVpLU44iIu_aqnCih7u39EaK5QxmxJ_jga6wFFSkvyh116clKkL0eYSzDCkSO4C8-qEVODUWcn5KQRVqAadPD14JMcg7CEQLVMvvEucsorjGgsFFmkKpeJQp8HArfkKjY4ge5EYo_UlBb4YEIEC6V7j7SeLWEfCf6e-OREgqr6GWzE2DEP-4bNLhPE9_1TxqNhOrUMIXY7rDJE-GcHtxTx77fOkzH2Xf8SQv9oHwO3veSyOxDuU4W5xTr3BgATGyAdEaYbwBpEgVddTPZutVXs56wkH30Lv9mVTN6r2iNXM6nMrDc_jPIVvYEb6XrSYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=Ht039rlGj66RWn6a9v_zTIVpLU44iIu_aqnCih7u39EaK5QxmxJ_jga6wFFSkvyh116clKkL0eYSzDCkSO4C8-qEVODUWcn5KQRVqAadPD14JMcg7CEQLVMvvEucsorjGgsFFmkKpeJQp8HArfkKjY4ge5EYo_UlBb4YEIEC6V7j7SeLWEfCf6e-OREgqr6GWzE2DEP-4bNLhPE9_1TxqNhOrUMIXY7rDJE-GcHtxTx77fOkzH2Xf8SQv9oHwO3veSyOxDuU4W5xTr3BgATGyAdEaYbwBpEgVddTPZutVXs56wkH30Lv9mVTN6r2iNXM6nMrDc_jPIVvYEb6XrSYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=Touz0T4P2yeEYHYeN4CCl0AIk159RACmpkE2PFZXD5l_N_9AZFWdp0sUVb--irA53e-gYpWZo8QXOYjrxWE1PVoHmfjPJdWGbSdjZuBjkZNrgD3383rQ-xDKdAvudwtOZoRIOsfiEir2jw1aNn1oo71yy26p1TSzA9I-FY3GuRKmvFnnzCjLTf6FowRRN0xtWKxnCSmn2ZutFCL0WkQPzFDOgKFsVSMnPzJ6jXZWqdEylhPAEGg9jtnGg9TvCiVJb0AOXj9rFqvXkiqxmZ_bu1FCx9Pkmv1zUxQeIdjzjHxAI28HVEp5TQXeF165MmdK2xNd-WxR3DQ7dx_CS3ne_TRGYDOz0JKVubeNl7MhEZiWx2emkeKK-eANFpiQb2bRJp--zf49IBttC4QztueUuxDVDf7bKhWYi12RaXXHC2VUpW48lmOou2uMcHIs5_oOYgOnyL2Zf9EmLOtJBChpermzxwM2Ms3-dzclokVyR-9rKqQO3ab41YHP_t0x7hUNO7gsp3dZ7jp7f1wCjpkb_OTctAiISpHa_VhkVw84Zy3fsaTeBmHUq2M9CiXFt2fj_myZbMymFWfB23-_67F5ECSVx58S0RvJffPAJi4G9IrjKRJpiMd4oRgYEYn12dbpUW22viMQY539WbqvtudrMtjLNy58Er1xJaRlV-Fcarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=Touz0T4P2yeEYHYeN4CCl0AIk159RACmpkE2PFZXD5l_N_9AZFWdp0sUVb--irA53e-gYpWZo8QXOYjrxWE1PVoHmfjPJdWGbSdjZuBjkZNrgD3383rQ-xDKdAvudwtOZoRIOsfiEir2jw1aNn1oo71yy26p1TSzA9I-FY3GuRKmvFnnzCjLTf6FowRRN0xtWKxnCSmn2ZutFCL0WkQPzFDOgKFsVSMnPzJ6jXZWqdEylhPAEGg9jtnGg9TvCiVJb0AOXj9rFqvXkiqxmZ_bu1FCx9Pkmv1zUxQeIdjzjHxAI28HVEp5TQXeF165MmdK2xNd-WxR3DQ7dx_CS3ne_TRGYDOz0JKVubeNl7MhEZiWx2emkeKK-eANFpiQb2bRJp--zf49IBttC4QztueUuxDVDf7bKhWYi12RaXXHC2VUpW48lmOou2uMcHIs5_oOYgOnyL2Zf9EmLOtJBChpermzxwM2Ms3-dzclokVyR-9rKqQO3ab41YHP_t0x7hUNO7gsp3dZ7jp7f1wCjpkb_OTctAiISpHa_VhkVw84Zy3fsaTeBmHUq2M9CiXFt2fj_myZbMymFWfB23-_67F5ECSVx58S0RvJffPAJi4G9IrjKRJpiMd4oRgYEYn12dbpUW22viMQY539WbqvtudrMtjLNy58Er1xJaRlV-Fcarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=tZy7tTT4XWAkpxFHIYKeha2jEfhyv6_qqxiFRokN181d0moPkFhrY5w9MNkxKHti5bAsVW46psESn0Lgw_Yy1DDMRtlNTpzaE6kNs7nnfMZYT2WcnOiEDRkNS7ykD8xlK1OAon_zJN4Ox2xj5iJL1uckP6BBmlWWITt4Gb5PFVMZlzkmUSt8pneXolsty3M4PGJRY813id2Tdt3A90yngB1N6oUtU6wrcVJC4hWl6DEtG8lpcPwwBA9qP9TVE7BLrQ1hSPaPhxag9yPj2vU6lIupZPnVcGCiXyzCTgYs6caOYkCMBL1ANA8qHPaw0tyzuUBH-j8w2oyxnUtUNDjXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=tZy7tTT4XWAkpxFHIYKeha2jEfhyv6_qqxiFRokN181d0moPkFhrY5w9MNkxKHti5bAsVW46psESn0Lgw_Yy1DDMRtlNTpzaE6kNs7nnfMZYT2WcnOiEDRkNS7ykD8xlK1OAon_zJN4Ox2xj5iJL1uckP6BBmlWWITt4Gb5PFVMZlzkmUSt8pneXolsty3M4PGJRY813id2Tdt3A90yngB1N6oUtU6wrcVJC4hWl6DEtG8lpcPwwBA9qP9TVE7BLrQ1hSPaPhxag9yPj2vU6lIupZPnVcGCiXyzCTgYs6caOYkCMBL1ANA8qHPaw0tyzuUBH-j8w2oyxnUtUNDjXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tiaxcKyIpUM57JYVcxMbbD6S4HL9VWaWLZMPnVk-Ms0-PSLRUVU6uUBafICxgmysvi-juavJLQ-8GdLvygc78eCfbiOCzk71-zed1E4f83JsjDdMqfe8znHmsWAWNQdFKOIpz44jwy8riusHPxyl7IkRYAaEPYv8LNYB3EDHs-bvrwncnFAfQCr9pW1IlK6Io-R5pEIEBsxMMqzLCacJiHexSLgq5bdhZffII8AJ6gzvPpHxeRV_qAef3uhUf6bXbygv2fRekQ3Oobc8bKKnraH7FNt6TK3MlZ_W3tY5C3XYUPDQUJCr7ivuSla13LSnhrTFxMAjlDcIkAjVnBcb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tiaxcKyIpUM57JYVcxMbbD6S4HL9VWaWLZMPnVk-Ms0-PSLRUVU6uUBafICxgmysvi-juavJLQ-8GdLvygc78eCfbiOCzk71-zed1E4f83JsjDdMqfe8znHmsWAWNQdFKOIpz44jwy8riusHPxyl7IkRYAaEPYv8LNYB3EDHs-bvrwncnFAfQCr9pW1IlK6Io-R5pEIEBsxMMqzLCacJiHexSLgq5bdhZffII8AJ6gzvPpHxeRV_qAef3uhUf6bXbygv2fRekQ3Oobc8bKKnraH7FNt6TK3MlZ_W3tY5C3XYUPDQUJCr7ivuSla13LSnhrTFxMAjlDcIkAjVnBcb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=eazNROgSt1opMgwK7Lmh1vtUbqSQyhhl5b-j9bobtf7AOg1iirv-lh0metgM1NYV8MbOmJTKHmh-0d-sRCzd-V5l_4jl034i0iu9XUhbFZ2Sh8KADMpT-GFKKYXu2-fqWLyzT7IZg4woQ4i0RLsbI99zznDNvYOepasvOMS2LYeVqWy-Te5yUsYc3RUj1mXhpTcyWGyc_St1F5ATdKRXOXVT_3-Ue2KsbH0yF_QhAUBH5fZw-pFO98V-aj6qa88tA6AiFra8j7FLlBwPF7HQlty2pJAhc3DEvGOlgPIXSBSzTkvWqMSv8yqCtBmn_5jzcP2mrB6D-3G3vJ3-H2PwCxA_tqaZKiqH2-JMZgRqlE7sJSzM0SUV2RPsQ4FSnQ2G94-Y2MotVoceTJe0Q4jwz7jS6xnvg9pvntu5cC1K8-4LTmk1RlKjGSf8nhbf26cxGnxX-hxzF_gT7e-Q8NQMuF6_9vUkj03jX77DsrfoV5fVAXbsY63k03-VnhOyqu9XpsX_d3PwlNVS3s1J9i-bxRz9jizl6CtkYhPevzGOVnOQ7NlQ4G4Dqr86NeM_VPmfdMtvhDYhXOvvGEkaVT4cnObo2W82P5RmhJeqzIO_iYsVt6NxI1hz_rm0UFsyZ3yaJEmSZnXM038kJZfWJh0HcaKT3hzhAE5plgtwH8E6nrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=eazNROgSt1opMgwK7Lmh1vtUbqSQyhhl5b-j9bobtf7AOg1iirv-lh0metgM1NYV8MbOmJTKHmh-0d-sRCzd-V5l_4jl034i0iu9XUhbFZ2Sh8KADMpT-GFKKYXu2-fqWLyzT7IZg4woQ4i0RLsbI99zznDNvYOepasvOMS2LYeVqWy-Te5yUsYc3RUj1mXhpTcyWGyc_St1F5ATdKRXOXVT_3-Ue2KsbH0yF_QhAUBH5fZw-pFO98V-aj6qa88tA6AiFra8j7FLlBwPF7HQlty2pJAhc3DEvGOlgPIXSBSzTkvWqMSv8yqCtBmn_5jzcP2mrB6D-3G3vJ3-H2PwCxA_tqaZKiqH2-JMZgRqlE7sJSzM0SUV2RPsQ4FSnQ2G94-Y2MotVoceTJe0Q4jwz7jS6xnvg9pvntu5cC1K8-4LTmk1RlKjGSf8nhbf26cxGnxX-hxzF_gT7e-Q8NQMuF6_9vUkj03jX77DsrfoV5fVAXbsY63k03-VnhOyqu9XpsX_d3PwlNVS3s1J9i-bxRz9jizl6CtkYhPevzGOVnOQ7NlQ4G4Dqr86NeM_VPmfdMtvhDYhXOvvGEkaVT4cnObo2W82P5RmhJeqzIO_iYsVt6NxI1hz_rm0UFsyZ3yaJEmSZnXM038kJZfWJh0HcaKT3hzhAE5plgtwH8E6nrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TJG1qV2y-bcmQKmOx0FGaIPnzWKEH8tmtMzZ_5oJOcaafk7cTAgseDz8JDInHSxEgOlqISft2fyxXeTcFrg5f7Dl83psUu0oP2eH7q0VTqvZAjwNLjbcTu8fzjYS3XCEdCdvyd5h9ohuEKJNOdSF3zlnsC3-l9iCdOy0mM3takyPGWJY1nIouC4UlnO8YdzWb4LGo1-YdwEuvWCILVTQ4HLa6LmD2GO82RvOtp4gtrJZE0Pw0nVGMXoa_frna-xeZC4XttlJKti0qnFqIUAnbgbM8QXpJqqQol3S6QaTrgbcpFE_3O5ULMp1tb4MiRM0NusXpfP3Kw-o9Mbh21u5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TJG1qV2y-bcmQKmOx0FGaIPnzWKEH8tmtMzZ_5oJOcaafk7cTAgseDz8JDInHSxEgOlqISft2fyxXeTcFrg5f7Dl83psUu0oP2eH7q0VTqvZAjwNLjbcTu8fzjYS3XCEdCdvyd5h9ohuEKJNOdSF3zlnsC3-l9iCdOy0mM3takyPGWJY1nIouC4UlnO8YdzWb4LGo1-YdwEuvWCILVTQ4HLa6LmD2GO82RvOtp4gtrJZE0Pw0nVGMXoa_frna-xeZC4XttlJKti0qnFqIUAnbgbM8QXpJqqQol3S6QaTrgbcpFE_3O5ULMp1tb4MiRM0NusXpfP3Kw-o9Mbh21u5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=alb-H6dCwME6OH-1n5BwN7ZeusGTBroDKqsJVv7eeB6d1xL9yXyUR7hoB7UBhYrp9HEeh3QRTh2fVTLs6KrJ3t3o8zXExgUds2qXRVoiqQN8IZtr-gau16YMgUAjyTKn40TNpbvNmGDV3nlDvZNZdhKDk5fCcjEpFcJdiHfEBkUgUAUodBOFkjYwGkhHMvNb2JCxXF3eVHjcor3KxKLqVaPXQINWMw_Evei7bkRTJZaFlQh3bDvIK1d5frhiyu9GMdjGeMSt-IXRkIU8JTgcXbtlM2e5y-FFL48dxElea1X88BHfE1v8qWuYL2uU1MXp6HGI9Qv14IHOWI6YYvkskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=alb-H6dCwME6OH-1n5BwN7ZeusGTBroDKqsJVv7eeB6d1xL9yXyUR7hoB7UBhYrp9HEeh3QRTh2fVTLs6KrJ3t3o8zXExgUds2qXRVoiqQN8IZtr-gau16YMgUAjyTKn40TNpbvNmGDV3nlDvZNZdhKDk5fCcjEpFcJdiHfEBkUgUAUodBOFkjYwGkhHMvNb2JCxXF3eVHjcor3KxKLqVaPXQINWMw_Evei7bkRTJZaFlQh3bDvIK1d5frhiyu9GMdjGeMSt-IXRkIU8JTgcXbtlM2e5y-FFL48dxElea1X88BHfE1v8qWuYL2uU1MXp6HGI9Qv14IHOWI6YYvkskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=aL_vQaohqZ9pmDs5AZ76ekyE2RRSN5Ts3R3qT_6Pm6Y0OtLhoTtJKr9Dpq0yB9pmO9sv10JEY3f940AvmIQwdDo4hOrf0SosVvQx2RjZRTb-5KOUiuSMTjP9-JRhgI1DJQdGO2dLpyPEIHCWz-L5MIAO0m__XtLi9t6p95vLbIzS0r03PiTeYa_vVLqyTZFe5fE4JRzlliT_7dL3WI6__4pFvJAmvHkG3zbCl-MQHkVwg9dUCHtVCipbjA2uyAXbzq3dhcl3-in00vqbOV_JW7y8y8ZU5n1_iW2S7e1Rgg7rSV0fHRuqPaPp7eERFk24cpgAvUYX4XVfUx9aUbLcYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=aL_vQaohqZ9pmDs5AZ76ekyE2RRSN5Ts3R3qT_6Pm6Y0OtLhoTtJKr9Dpq0yB9pmO9sv10JEY3f940AvmIQwdDo4hOrf0SosVvQx2RjZRTb-5KOUiuSMTjP9-JRhgI1DJQdGO2dLpyPEIHCWz-L5MIAO0m__XtLi9t6p95vLbIzS0r03PiTeYa_vVLqyTZFe5fE4JRzlliT_7dL3WI6__4pFvJAmvHkG3zbCl-MQHkVwg9dUCHtVCipbjA2uyAXbzq3dhcl3-in00vqbOV_JW7y8y8ZU5n1_iW2S7e1Rgg7rSV0fHRuqPaPp7eERFk24cpgAvUYX4XVfUx9aUbLcYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=Uxwuf6mbjSUTJ2ms8sL9mUxR6rVoP5YmIZqMGOqnvCEYja2vu1NpO_0sr1pPY0DZMadEocEdzzDKXh4H1IVtH06ykjsv2_xhi3hvGLQ76P96pXdJPu2WrV7CJSNly-tfqego3U1qnt28jXKlL3HQRir1jjXbAFCI1OcjEVqP6Lu7T3dVY7rCq1__BLibrLkDVrGd4ftwFYhafUzY-CtCHrNuv8-pMwbBhLz_5yWXHQu5ZMmJ31SkZYiFs5RmXJo0TmxMYPgi7KqnX0ACchDaKZVSVU2B11tKYjkXDiWbPOFrRh8vxj7wH7bwViYZkb7RZnyJGiRgAtbO7ZsDLy-B1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=Uxwuf6mbjSUTJ2ms8sL9mUxR6rVoP5YmIZqMGOqnvCEYja2vu1NpO_0sr1pPY0DZMadEocEdzzDKXh4H1IVtH06ykjsv2_xhi3hvGLQ76P96pXdJPu2WrV7CJSNly-tfqego3U1qnt28jXKlL3HQRir1jjXbAFCI1OcjEVqP6Lu7T3dVY7rCq1__BLibrLkDVrGd4ftwFYhafUzY-CtCHrNuv8-pMwbBhLz_5yWXHQu5ZMmJ31SkZYiFs5RmXJo0TmxMYPgi7KqnX0ACchDaKZVSVU2B11tKYjkXDiWbPOFrRh8vxj7wH7bwViYZkb7RZnyJGiRgAtbO7ZsDLy-B1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkDNEjMidVv65Q4FBKnoTMMxdjJLEr_NX2B8yn5eE0GAs54BVXik6QWOELMFEl6cxWctxffLoV_nv9v_WhS6om8u7kjck_YReKjchvHQBWfsA_LMleCufMJJvdLCD_jsr8vCepMSxNj5GfXbzP4JwL-_2YUVqXonDdSmFSLR0IKaSdfxT4wDj8ME5M9W9zplG7QI8bPLD06iyfjfHne7ng8-OM9nCquyzjWzoBzurwOJHC7gNpSXhoeeJuAmzmwPqMAfyIbKEPiu6-AKnXse-52GqL7lI5DT5B5wU8zVsR7YGfqWYgrXRl-xPywfpOGsBpQ4ivhhvMhk2oSZrVjRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75M_HiIZhuIEJgLa_nNqd_sDEdD8sTJ8q9T-OvPt7X4BmeCgZ_qO0Wc44AAbkY_t0Lav_Qurla6cnIl7xupY5bbdZhTsxtxMNjvQCnyq7mn-YYODCQqpaVWHQzEZLl1YeSD3D7EqMoJ9ftmkvd7IlxpSuVx7YyqBOLeaI9CLI4c54ydvCg_oEqMnxNLAV_qZS6mJ9VJ0mRP3qtsm2cOF1zB1hJ3MVpO4SMJmhWbbm_ztjP-9-XqrHJ7SM0ZgwTe6P0poqr6ZVEPh6r5llXY9cQDjCMC7MIHwkDHmVrRjP9Yw0cKW3bbXoQD9jXK1ZgpV_pQSm4haSWA4v-133o0qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=Hl__hwqGUtjjP56QeDMKr6a2ydm-fj2w_l2wUOGZ5CUFq4Pm6I5JtyAqqbP6qCnYw5qh9IGFdeNSMtmEnuDEuaWbT6ZjRw7rrIq8-Xwu3TBhU62btKBQBjM9fdfBElq1sUCkWT7HMw2bjhr1Dz-alhBbqGASlm2fztQ8a-A4_LnYJXOXFwK8Dev9VbA3go4PnnIZHtSlcdpLx7K1KRk4QnnGOoSpn_Q4F5bby8TSfRE0OTW12LVESm6xMnkIDP2jW1hAA7lN06wkQNBp8i7xHh-WLVun-K_Zis48TIOYtHQq7uAufyPPzA-GPCDMNpJyrKrvxR1TT2pgMifsHWCrBzE8eN7OwIdbBLpvydlQLZf6EIkc2oyWAZ14gYz7m5EYUMn4sqGqqEFAnIHXfDq3orrw0pN05TMWKT6hE-h6YghzGy1p1urM3BdTSBQaQEJMZfsHw6FX2cDPpELEoL74QUdc8AL8_RLeJQgwV8qvRfXzm_xZAQUd7hEk8gLDnI5kDGUuZiUEJYqVGtQmYG5nyYx_cZC361Eq5MYbl6HN_iUfaQ2qpS1XsHlxfe_nau1B2VI8TTeJr_ve8UpKHoJ70oA1obQ9zEKwPZDj9j7sJoLam_48jECKo29zGfEPZUBSmDZquAwAagAb3V-Ny83CrO0y5NacCYnHT2CXI_ULW7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=Hl__hwqGUtjjP56QeDMKr6a2ydm-fj2w_l2wUOGZ5CUFq4Pm6I5JtyAqqbP6qCnYw5qh9IGFdeNSMtmEnuDEuaWbT6ZjRw7rrIq8-Xwu3TBhU62btKBQBjM9fdfBElq1sUCkWT7HMw2bjhr1Dz-alhBbqGASlm2fztQ8a-A4_LnYJXOXFwK8Dev9VbA3go4PnnIZHtSlcdpLx7K1KRk4QnnGOoSpn_Q4F5bby8TSfRE0OTW12LVESm6xMnkIDP2jW1hAA7lN06wkQNBp8i7xHh-WLVun-K_Zis48TIOYtHQq7uAufyPPzA-GPCDMNpJyrKrvxR1TT2pgMifsHWCrBzE8eN7OwIdbBLpvydlQLZf6EIkc2oyWAZ14gYz7m5EYUMn4sqGqqEFAnIHXfDq3orrw0pN05TMWKT6hE-h6YghzGy1p1urM3BdTSBQaQEJMZfsHw6FX2cDPpELEoL74QUdc8AL8_RLeJQgwV8qvRfXzm_xZAQUd7hEk8gLDnI5kDGUuZiUEJYqVGtQmYG5nyYx_cZC361Eq5MYbl6HN_iUfaQ2qpS1XsHlxfe_nau1B2VI8TTeJr_ve8UpKHoJ70oA1obQ9zEKwPZDj9j7sJoLam_48jECKo29zGfEPZUBSmDZquAwAagAb3V-Ny83CrO0y5NacCYnHT2CXI_ULW7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8Mv8dX-CDEcKHFbMZlxExsFmY-SZR0bYA__MMfvWSwPhB2zKIqPPiYTNde2KMlJ0a63hDh51r2sQx3xvx3SOAgT3eHAPr0O7t42dqxDW1o16XLLEnDboDQJlaEDMfgwezcw9VnO0XiH38T_NMtJJ8dLnt5eHTusVI2N7u5yKYVj7cfCwXUjNyhLxa-LhyDy429oq3Ex4sWDLlmTyjIkPqpl5rgBOiKzk964eCTR_O_kOe5YIxaApNYD4284a-abhLNi-TP5J3RsH0oFfOzkTxqL3t5dUdXQkZINUIh0j5OPsBTwKLN5i54MUyFdCZtNgVXFFc8N3mDKa-vzGw_N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLYE6454VuX8BTyGaLpbVDPyDosiKCwnGVIvT6kF4jbuTjW0Rd1CYyTlfjaecypK103hgThBNCaAS57cy4HDjM-L0g5YQCNB4PJMPXtCUy7BvAI8wV_o5wNoQa2j7yIlAjs65ztFwMcUpPm9d3W2f0CEXGMQLwAgycaEjOitqo_-Qiwa7P4tXe2xrNoScLVOSQPYKFWJ86AqBQ_EDxtizAgusrrtznxSKzVgb8wqpI8d4NX0GW_72tm0koHlumjiOVJn4ScKDN0GlhmLBGnpNc-SmCGNVFG5XEQvpyrb4QS_5DaaMpH3ScMwmPYP53aXkpnOq93e8GfWtw0IdgbwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2c2yrYQ05g4aoV0Kosei0t_q--sp93HzlMJE8g7YOghI2geAvsywzozRMYXtIx-sEAdJW-8B26R_KCbahTv63SmjTL7_VZmnt9M_gKiTEhMYYzcX1qxLiMdN4vwOnJIFC1nsKKbw37kIlfQnorhgj-5DZoGYgEeGwom1YUfakyxrTtgGOhKP_VkT_iOpcLRiPGcdA0bnf_kI1s2EGhZK49PQk7yZ2JyIQ_JaUtif4022LOWVPyi4cevwQywFmpbWCExorMZKrEEu2kvHgElPznP0h6dGhIExMewLvy73ZiqxmHP-IaP_hsl0sjImFXpjRqkOd7tZN_iDgFaiyQc5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=kYw4pmA02q64KRTnYSsoP1EY5Zs3SKqIaungPVBo81BskowsegP-yobdWpa89K9oriqVaSKL7LlkLIAztyC2Mvu1ZFsfOfabFY7bjONtkFyyYicCrPnPNqk2pQVAtl5u7KCeU3FAsFG8L3ndvipOaNfVxbH0qrUQ98HGklIw9pQwNZmDpUrkGfh6pqYeAIhPzhtCC8KOKxfF0iUk0RBHZCh2TnakFJzZjpPSIcntQJLIdjf3kUhNVofxvur_kWcHZMOCPdo70hdnfEUFINwGATEiCWRy7oeHbCXdX2clpc8S2QSbZd4O7va00Nrj7O3I_YqWpnsYioXjzafLjvzzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=kYw4pmA02q64KRTnYSsoP1EY5Zs3SKqIaungPVBo81BskowsegP-yobdWpa89K9oriqVaSKL7LlkLIAztyC2Mvu1ZFsfOfabFY7bjONtkFyyYicCrPnPNqk2pQVAtl5u7KCeU3FAsFG8L3ndvipOaNfVxbH0qrUQ98HGklIw9pQwNZmDpUrkGfh6pqYeAIhPzhtCC8KOKxfF0iUk0RBHZCh2TnakFJzZjpPSIcntQJLIdjf3kUhNVofxvur_kWcHZMOCPdo70hdnfEUFINwGATEiCWRy7oeHbCXdX2clpc8S2QSbZd4O7va00Nrj7O3I_YqWpnsYioXjzafLjvzzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PscLmmb2l7O0atTMjicCj3mZ1DmbQ_L5gQmSJfrvDkEncVVEmfzjTOafu1emeYFYWulZsuR6Vmk1eO075Ru36PU8-ma8grTYeioEqStsA4Rd5eZSCdTJjUMDGs5HydG0FjALbIIR0Yo9XCRVwXrPfvYfHIeas7Mmuua0BqSYEYEVa7K83OwXQWLIrgWOqLdYeAHFX9cahqTBTJcT7_6JVX9B8k8zlhmR4bftKH_hTKpVeRh9H4ZCYVLNTif4CNJLEe7JfVpdB12XZfZ0T4B_JbdlDPcTRwk5IKokTrCdhFMxFNMCUayIU838mxFdx3WR99kVJxIWCltB5dnB9hyKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=pv7rn5_5DJhCbrsH6SNP3SaJqZ8VqXCdo9tt94FmCqoWhyPX1Oda-kUFd685tNhqvpfIdUbImyCluoetRxz8AHq7p4prUbEzm4EPe8dHzkUAaBww8_Q-aIGrnWFvQYwdTz5qDDpdFl_1O4KkTqcVFd09tkpnBNaAWwNTTz2uqrtoc6BJzsQ7-Pxrm9ZynylxMaapbu0YyHLX36PzPZ8iDmEYAE20oJwieVTCvp5I2uDlMNVQTOqkW0L3NI89CoUVYBy31tjDLiEAsuDt6UEIzBnOKu524lN5Z-e3a9WN9pFFuqeeyejTeNyvshHSVo78ahMZHQEecDHw2zg-IkCrDLIFdgRf-Igyo82B1YG7uALwOdYhUN-S9_bYskeyiSdVR376DpuTL1vxlOdi41P0sEtGx11l6VcKG-_jdo5aianUBAsl_312c4PIuUypfJj2h7kY6Qnlno4c-90sp2GI95meBbqy4mhY5L2wYbtnVZkuAlPhlZGc94TdlMFmKL3amgqQ7d0DTR6z16Sedj5rFWtWnCfvxq1ig3m9YH0Fd3r9UQ5VsFThAeQoaGt987zpPX4G8MGO1lk76qHxaQFN7biZJ9IAQq1XqujrJsQT21j2HTBbuYaA6dhXXseqMDMncH1v2-wGG1JueVFsBy9tGv9ePv41khaLdBd4h7VZFtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=pv7rn5_5DJhCbrsH6SNP3SaJqZ8VqXCdo9tt94FmCqoWhyPX1Oda-kUFd685tNhqvpfIdUbImyCluoetRxz8AHq7p4prUbEzm4EPe8dHzkUAaBww8_Q-aIGrnWFvQYwdTz5qDDpdFl_1O4KkTqcVFd09tkpnBNaAWwNTTz2uqrtoc6BJzsQ7-Pxrm9ZynylxMaapbu0YyHLX36PzPZ8iDmEYAE20oJwieVTCvp5I2uDlMNVQTOqkW0L3NI89CoUVYBy31tjDLiEAsuDt6UEIzBnOKu524lN5Z-e3a9WN9pFFuqeeyejTeNyvshHSVo78ahMZHQEecDHw2zg-IkCrDLIFdgRf-Igyo82B1YG7uALwOdYhUN-S9_bYskeyiSdVR376DpuTL1vxlOdi41P0sEtGx11l6VcKG-_jdo5aianUBAsl_312c4PIuUypfJj2h7kY6Qnlno4c-90sp2GI95meBbqy4mhY5L2wYbtnVZkuAlPhlZGc94TdlMFmKL3amgqQ7d0DTR6z16Sedj5rFWtWnCfvxq1ig3m9YH0Fd3r9UQ5VsFThAeQoaGt987zpPX4G8MGO1lk76qHxaQFN7biZJ9IAQq1XqujrJsQT21j2HTBbuYaA6dhXXseqMDMncH1v2-wGG1JueVFsBy9tGv9ePv41khaLdBd4h7VZFtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=edHIFZQSOLWYfOTkt4QbqS8nIq0LLhpwxCRvCrRLJljOk9GKkKG-gnOZcdiIaIEkKoYY7UW-wZpk_gxNCUoePfP9dEGEbeft3kLH2YntmEO3lAfU932jeZNFephYlajypLrtwoXE7UrXjjSDTV81zlqYWFR91rrQkhueipcnBCcZGc2_y3yhSYGbC6Y81wD6xLN9PPzDo7BRZvoq0wW4dx4D_9KnpTeXSvFazpy5TLSX-AwyaCHnW59ZoGqrTDOVuT2BfR4ovN7of3cq8GImfSOa_ucQE5QR0KGlqm0rdVlJqytnTuFZBD_LQXIe-cKxNfA_oq4zCig4M71JxImZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=edHIFZQSOLWYfOTkt4QbqS8nIq0LLhpwxCRvCrRLJljOk9GKkKG-gnOZcdiIaIEkKoYY7UW-wZpk_gxNCUoePfP9dEGEbeft3kLH2YntmEO3lAfU932jeZNFephYlajypLrtwoXE7UrXjjSDTV81zlqYWFR91rrQkhueipcnBCcZGc2_y3yhSYGbC6Y81wD6xLN9PPzDo7BRZvoq0wW4dx4D_9KnpTeXSvFazpy5TLSX-AwyaCHnW59ZoGqrTDOVuT2BfR4ovN7of3cq8GImfSOa_ucQE5QR0KGlqm0rdVlJqytnTuFZBD_LQXIe-cKxNfA_oq4zCig4M71JxImZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=i6njTgPGuwV5uOK1MmXS4NssecdeToeZuT2R2AYPG0S67h67pJOhr43k8or7McljL01qVkyc2yHkY80SMoyNng_wSCArYtrjSKAmZuGvlB_SnQRj0yuIRZimH1nle19ok_vaJn5Hu7WsaNooU4IUNS_HHCSoytqRZo9y1FFZAiA1M3vNjfrN5mS-Dj0xqIvR2DHnIDwfgOtWfhBLygI57SLCleDS-vaZqnTS3VmyuWjulPh7YEKJnJ54PX1HBrIz06WSUEkbdS7e0Tu1puQ9ugUEKetXrUz16rtNfmoC42WbiQyTyc6cDCDWfU0csr6e8RgFViP6iGUfRUmcUrEx5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=i6njTgPGuwV5uOK1MmXS4NssecdeToeZuT2R2AYPG0S67h67pJOhr43k8or7McljL01qVkyc2yHkY80SMoyNng_wSCArYtrjSKAmZuGvlB_SnQRj0yuIRZimH1nle19ok_vaJn5Hu7WsaNooU4IUNS_HHCSoytqRZo9y1FFZAiA1M3vNjfrN5mS-Dj0xqIvR2DHnIDwfgOtWfhBLygI57SLCleDS-vaZqnTS3VmyuWjulPh7YEKJnJ54PX1HBrIz06WSUEkbdS7e0Tu1puQ9ugUEKetXrUz16rtNfmoC42WbiQyTyc6cDCDWfU0csr6e8RgFViP6iGUfRUmcUrEx5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=EuglyWbFz7y_Km_OwH9-RKVqNPQjYQaBCH8OVvxc9-zbMdvtB1yEggLpNLAI5tK3YayLIwtbyVjDIYElDNd61YT2oLKt1ucnPpe8b34Un3V8oiZxedTmXIMmTwajiDcYz0CEnNevzpI4OofVMu0I_YDXZ1XX70i0mIotEPOwOkyk0FpKBnr9TQQMk-fCwGpYkM891gZ03bpInAngRVEoV3Z7MbxXqV-O2fg1PqVjyxp4jHm5Ik9wkQVM5FKns1CcEKLXt4HUadB55xuPMGoqOSZDIL1kps_SL8Nw46k-xYbfT4EamADeRyhHZzX9iOCuN0VctKkaId3oRChXorbYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=EuglyWbFz7y_Km_OwH9-RKVqNPQjYQaBCH8OVvxc9-zbMdvtB1yEggLpNLAI5tK3YayLIwtbyVjDIYElDNd61YT2oLKt1ucnPpe8b34Un3V8oiZxedTmXIMmTwajiDcYz0CEnNevzpI4OofVMu0I_YDXZ1XX70i0mIotEPOwOkyk0FpKBnr9TQQMk-fCwGpYkM891gZ03bpInAngRVEoV3Z7MbxXqV-O2fg1PqVjyxp4jHm5Ik9wkQVM5FKns1CcEKLXt4HUadB55xuPMGoqOSZDIL1kps_SL8Nw46k-xYbfT4EamADeRyhHZzX9iOCuN0VctKkaId3oRChXorbYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=qE4EnJW0FmddjPwuFek5anmK9Rrn3873071JwSsG5f39QFquAciWOPq4lJVauwFaj9NQaIbBvfMtt-6Pe8FAh9RCCefcbu9wu3xC2EJl1a7ETtUskp5CAlwn_HPOG48txYgdLrIukuFqFDaXulhFn_CtkxTvJ2U4aMhUa9AHR48Ewl7rQAoKRc6DlCaws3-_QeKB5ghzDOYo9Mqya4iOEr-PpWnA9X8gjrtnsqsjHp4uDe1V7qLLPcbUgWpU-lytJFLHP4nWktIWdfGx-4FIoh9CSpj8zOpTzmpa3LNkygojrtY2a-q1GyE8cOue1dxFXMKUn2RtcLXG1InIxrINOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=qE4EnJW0FmddjPwuFek5anmK9Rrn3873071JwSsG5f39QFquAciWOPq4lJVauwFaj9NQaIbBvfMtt-6Pe8FAh9RCCefcbu9wu3xC2EJl1a7ETtUskp5CAlwn_HPOG48txYgdLrIukuFqFDaXulhFn_CtkxTvJ2U4aMhUa9AHR48Ewl7rQAoKRc6DlCaws3-_QeKB5ghzDOYo9Mqya4iOEr-PpWnA9X8gjrtnsqsjHp4uDe1V7qLLPcbUgWpU-lytJFLHP4nWktIWdfGx-4FIoh9CSpj8zOpTzmpa3LNkygojrtY2a-q1GyE8cOue1dxFXMKUn2RtcLXG1InIxrINOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOy_R3Cnj8iqsebVTe7dHTqJDDRZsxzsTkB_6JBUsUJIf1_XiGi7WnyYcgd46jwPDwjjBo3Y6SntIBXTX5I-OJeSIG4zJ_AqiAdR7vr4sWpE9vadiFDxXbz17bEL4a4t4VQoq5_N_r0eiG0oHjrQ17ZKSg1LaXdONDRKuKYwlB1TSTsq9cpIXeSCJOnWGOYk3UhPXUzgZmu34FfB9yVJFAvAwQg3Vk6eGqEy-4KvOzGo2iGjYdbsDZvn1avkoGrOe7TsVtjPi67dpKHhWkOhLWA5LsAwxFzYE_4HUfcmfwYdZr9tpoQ-ToXUmw1Uadquuryb27CA-dsnpZTJCLSRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OggyxV9Bvzl4tMRCcbiWRfpE-xmG_oCALcteHIJJKwmQt-qyEAx3j2m21yVKitxVHbmzW8ZdNlWG3hhTc-oYRBJs8NPc7VGLOS2sW4uS-vXsmXa1gwoXQGQ03NcGrDv9iPo1-B8ec1607zVPmTeOnenI7JkMGCpZ9vEib6Ro3ndjvAJnMgJbP0BKJACPZ5I5nxRVIOUTIs5fmIRChYMmwFboW5dXD8nNm5HyGW560cia8XVcwz5S8uzLSXPvv7lUV-zXjSSK9FNehHJeL4Y6e6YPKUHYClZK7qno94tEMIMEEkC0xUYKx_yMepbeSjKjFSqAdui7eaSGMIUpvB3Snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=fmlhSWyaQSkzqmk7Qb6cOqcvae_NN0VwrhUERrGlYR4cZpZxHBNy0nP_YzEYtrhksMvMEoC2FNB4E0Au24WmSI_R-C5_snENp6yQ_OVQpCHRd7zXa1oTUI9c3YM4oP_V6cNCn0AnyEXe0zmHqYTVruQmLO64J8RZ7WtugzPHHaPEVETYS7fgk6kIf1bttQ0-2wXYWxhqRspKongQ54laOf-ixP_Zfga-Xp_esrdbQg7Lw4H6NmS4e15HBgDxPYQuL14-7PqDezUAj9k3w5Pewnji09yWvad6GN3BHVeeAwq-tld7ZIORH-z69mzI7ZvPNRQ-vVJvczhUzkr_wBN4LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=fmlhSWyaQSkzqmk7Qb6cOqcvae_NN0VwrhUERrGlYR4cZpZxHBNy0nP_YzEYtrhksMvMEoC2FNB4E0Au24WmSI_R-C5_snENp6yQ_OVQpCHRd7zXa1oTUI9c3YM4oP_V6cNCn0AnyEXe0zmHqYTVruQmLO64J8RZ7WtugzPHHaPEVETYS7fgk6kIf1bttQ0-2wXYWxhqRspKongQ54laOf-ixP_Zfga-Xp_esrdbQg7Lw4H6NmS4e15HBgDxPYQuL14-7PqDezUAj9k3w5Pewnji09yWvad6GN3BHVeeAwq-tld7ZIORH-z69mzI7ZvPNRQ-vVJvczhUzkr_wBN4LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=SD0Be3CQePl0r0yOsmCCF4Cl0IPoFGOeUEWTJUGELjT2ywsLzN7ss9zE33JazYg6-6YPNGET9447nMxZXM8WN84qOu9Jv1PzHLUeRIwGclgTbRbQy8P2o3CyC7if0nNx0NNs-1ib5W6A5BfrRJwKLO5ko_ApMmizCDd0K-3aC7njyh3SIDbKJEB_SS5cFRBUCfOUoBdP9EmMOJCjcahRtGREqiZHO7DPBlbv4u5Vmbfb1A2KiglZlP1W8mbkGhf0ru-ijcRuBRSvIa01FHizp9-oBjHZ61XBcdsOobStT9igDlgKDdwv3ELzYZE_z0NfbFFN05GvMOADY2qoiNIISw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=SD0Be3CQePl0r0yOsmCCF4Cl0IPoFGOeUEWTJUGELjT2ywsLzN7ss9zE33JazYg6-6YPNGET9447nMxZXM8WN84qOu9Jv1PzHLUeRIwGclgTbRbQy8P2o3CyC7if0nNx0NNs-1ib5W6A5BfrRJwKLO5ko_ApMmizCDd0K-3aC7njyh3SIDbKJEB_SS5cFRBUCfOUoBdP9EmMOJCjcahRtGREqiZHO7DPBlbv4u5Vmbfb1A2KiglZlP1W8mbkGhf0ru-ijcRuBRSvIa01FHizp9-oBjHZ61XBcdsOobStT9igDlgKDdwv3ELzYZE_z0NfbFFN05GvMOADY2qoiNIISw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=r8zkwh6Ek0b6JOTkUUlpajhqEi3jmGO1dW4xOMNuGp-nyARyM36SttOUkYc_EVpjyG9F95mmXRW7Rm_uqLegTGX_OHa0emshgPbmeZn8ohS9zvUBs7FkuPiZtiHwJa2XJW3w6JpJsvTRgwNYT72hxX_kXiH1FgpRHy-0gG4wE-Yv0Rbqf_A0yjpihdtphkJfG1MGUCAIOXg2D5zJWwcfTxUvJy-6fxZ8w4U7YA5rqJIHCySLn1dOLD__Loa3kl7RqtOq-d4QjpnGRfb0ZhZJRSLwM_lzZ3AiKNLlolw-jMiKOX72u1Y2UBEyXdFUYJ3RNwpUk8VbRoDV00Ul1KsbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=r8zkwh6Ek0b6JOTkUUlpajhqEi3jmGO1dW4xOMNuGp-nyARyM36SttOUkYc_EVpjyG9F95mmXRW7Rm_uqLegTGX_OHa0emshgPbmeZn8ohS9zvUBs7FkuPiZtiHwJa2XJW3w6JpJsvTRgwNYT72hxX_kXiH1FgpRHy-0gG4wE-Yv0Rbqf_A0yjpihdtphkJfG1MGUCAIOXg2D5zJWwcfTxUvJy-6fxZ8w4U7YA5rqJIHCySLn1dOLD__Loa3kl7RqtOq-d4QjpnGRfb0ZhZJRSLwM_lzZ3AiKNLlolw-jMiKOX72u1Y2UBEyXdFUYJ3RNwpUk8VbRoDV00Ul1KsbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LASmtPS7qBeqjNJ1n_yZ_-cza1-tuMLORnnib-E_JAKty0ztMLln3Q6T2fOEHV-gVVqGRmQ38CKPpuk1E6VJKP2DMAnPi231XHZWW9F8gt3pk4QVYRtJs33GLpGtGVTFsBMK7ajwmtq99x0pky0DqJNOdfdDHYly0W34AYiGNqABP-9IVJiFLTImCz1T9APAjIaBDTCV2w4dZS-9Oa3mAGq-f7ZDcKw3dPbX-_sc0CZ334V8kNKZp58AHkhMkcOmaRl4clrRMInDWgp5U8gOWm2s4HR46WVVmuRFg31YLBn3DJmjCK2aSKHHHXTtGK04ShqO1j9viffbkFcrV-Ehxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=PFnLoPy00Xp70VSsNV5zPvC5xA4-RY-u7YUdgyYw0TGSkBa8vFM-h7RuiKNfCpp3OWwKxm0bsX7eIbfMqPXp8TAVMvneZjniCUMr9uYd6xssLr8xxrjN9pfupVCghH7zitvf3oSzEWz8XsCO9haTFeqDg9eNieK1Ystmo8AQoXQAtOSsAJdPk6ManTlZZ0qfuuwAiipySXNQ5J77BuPeltJcDOzsY2RSodrsxz5Yq7YCI6r76RrokCVFHvdkqnwdo6x9JxddQvtW4FSiVitM646YJKr-wN0c4jOx6LW4rpbnTUzxDA_b2x9-IQE7Ps7QGIy_pvzkO72Fstw3CkR0kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=PFnLoPy00Xp70VSsNV5zPvC5xA4-RY-u7YUdgyYw0TGSkBa8vFM-h7RuiKNfCpp3OWwKxm0bsX7eIbfMqPXp8TAVMvneZjniCUMr9uYd6xssLr8xxrjN9pfupVCghH7zitvf3oSzEWz8XsCO9haTFeqDg9eNieK1Ystmo8AQoXQAtOSsAJdPk6ManTlZZ0qfuuwAiipySXNQ5J77BuPeltJcDOzsY2RSodrsxz5Yq7YCI6r76RrokCVFHvdkqnwdo6x9JxddQvtW4FSiVitM646YJKr-wN0c4jOx6LW4rpbnTUzxDA_b2x9-IQE7Ps7QGIy_pvzkO72Fstw3CkR0kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=Qnbuda2dQUYazStQRXZhgWofJX0i1XjrNvIkUmUptZcCVwNh7jsmOpnP-e-3ehbGWkqFw0S83mnwkcuKTtf84kEuulc5YKAZZwHjGvKgUNMQTyGt59hdsTYhGe6blkPmT_p-RyvDDzoeKGSyG5fM612ZA_PbODzy4ChPP7cOURI0kGVMW4YZ_Hy38K9XyM2upVMfvSZtBl-n3LrCH1RUCVrKkKux6nOreswQiWFjDa-UaF92PmdwsvvpO4mSuX6f1_jk6hqkj945scwmBFTVIiJnX9NZtTW7WcasAGkoBZLXrcGMxKSuRRSbRmWVhMlJQziswfSJ-tVLlUyHvbMTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=Qnbuda2dQUYazStQRXZhgWofJX0i1XjrNvIkUmUptZcCVwNh7jsmOpnP-e-3ehbGWkqFw0S83mnwkcuKTtf84kEuulc5YKAZZwHjGvKgUNMQTyGt59hdsTYhGe6blkPmT_p-RyvDDzoeKGSyG5fM612ZA_PbODzy4ChPP7cOURI0kGVMW4YZ_Hy38K9XyM2upVMfvSZtBl-n3LrCH1RUCVrKkKux6nOreswQiWFjDa-UaF92PmdwsvvpO4mSuX6f1_jk6hqkj945scwmBFTVIiJnX9NZtTW7WcasAGkoBZLXrcGMxKSuRRSbRmWVhMlJQziswfSJ-tVLlUyHvbMTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=cnT1cl6RPulY5k2xsm7N1gcl6kabdZvC8QoHIV6dt7qypv7gktsXnroe5Qx-0WyjsX0zXV2zlmddJ2xP1tb1ZgeO5XqKPva8DmbnA3rvEhkqe6SyaiqrqG7rjDbOwyy7T_FQJwiI7pXF9IhfKWGn8AF410kyLlGmdddt4w3dWkciA2Q8D60ELiGMrYNX_V_bseLm7PDvzmLKrqpGqr7eCCddkPShiSfIf-uUTrjl3G9JL2JDmuEOF1r0meEgZmTSijLkdL4RQtpfeAnTVR_i3oANai3qNM-76raJHad1xWg9qbJa9Env4j-0FB7qYmfEBHkNANBVBYprxjEXgdeeWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=cnT1cl6RPulY5k2xsm7N1gcl6kabdZvC8QoHIV6dt7qypv7gktsXnroe5Qx-0WyjsX0zXV2zlmddJ2xP1tb1ZgeO5XqKPva8DmbnA3rvEhkqe6SyaiqrqG7rjDbOwyy7T_FQJwiI7pXF9IhfKWGn8AF410kyLlGmdddt4w3dWkciA2Q8D60ELiGMrYNX_V_bseLm7PDvzmLKrqpGqr7eCCddkPShiSfIf-uUTrjl3G9JL2JDmuEOF1r0meEgZmTSijLkdL4RQtpfeAnTVR_i3oANai3qNM-76raJHad1xWg9qbJa9Env4j-0FB7qYmfEBHkNANBVBYprxjEXgdeeWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=anWIf3mhNwQyvAb3du7Oar283nsgBrxM76PLqzJJxjFSp9Lz6TEqmAyILJRW2xkz4wQzAqwnS46ic51kdoPhzTwQCM60cBzeU6CESrrHXEz_m8n69WikqsSCMDP1m9MH02eyhnR57Jc7g5tNjUUJX3ijlj40SlZ4pZyXaz_Sz4vi5xOGODfMCsdLv3etW7fdru8877hnyUiyRFII_vE1MOAQzvMpjVySlLsT9G2Vmu3f_gdYXJOfIWCyfpj71HeG-ZGS5oPKW1a9sPBoUeeYm4jOYivC2WeH9MCqdl5uJFDfrtHqkor8C_QxmYvu5MGCA5e_IEQMIAVrrYG0-ONQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=anWIf3mhNwQyvAb3du7Oar283nsgBrxM76PLqzJJxjFSp9Lz6TEqmAyILJRW2xkz4wQzAqwnS46ic51kdoPhzTwQCM60cBzeU6CESrrHXEz_m8n69WikqsSCMDP1m9MH02eyhnR57Jc7g5tNjUUJX3ijlj40SlZ4pZyXaz_Sz4vi5xOGODfMCsdLv3etW7fdru8877hnyUiyRFII_vE1MOAQzvMpjVySlLsT9G2Vmu3f_gdYXJOfIWCyfpj71HeG-ZGS5oPKW1a9sPBoUeeYm4jOYivC2WeH9MCqdl5uJFDfrtHqkor8C_QxmYvu5MGCA5e_IEQMIAVrrYG0-ONQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSoGhcjZt7AXW99wjSrvStG0zIypeMZYvK3fNVSrd8rgVbDBdBl41qh7L41ox_-TL4DQbHP7Qhp1asROkqj-5QyMyun55mjgRE5_OZ6xzsotV677TAMrqrnRrnrmIpgOibBnb9AIJeVw-N7DegTV0sjGoicflF_Fhfgsju104841rSbyBnajhnPldYM4b0xas_GbfvSg_dGdB-IU8TcU2PDVkZx1SIuUWdIGe7a7SVB8_Kw9k5cQk7plC6_fEcX7WY3V9HuLmImfweF_i4Y3GqploGpN4LH5Oyxl964OaP18Vj1fnrZpJxdR88uEQUCHg89SPDuf_U4VNxJWB2JSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=BktLCAa71HbOjmGRtBRSG7qPNm99na0ieeC-S5vPwmS4akc1Z5Aq7kx8lZm-ArIIOvoHFo-xVUUaOQwTmRclrnBfa0lNVtjbYxee-LezPhdGyGcj9raJzqZGqnImQS7p-invoJeAJyRVKj8Y3EE6ZojAc6ai45GVnDOqQt-uQ_GAnExnyLGem-Lf8INhhKMKJASOUTK0TJpAqGSiHBikNIE6KOzN_nyXRZID8tfo62K2PxGXSB2lF2_g2B3FUL-msHJCZlfT87OKEfmvymnIiWmhoYizC4sZYBDW3JjbiJxk-RvD-_IKQ-vg0aUJyB9Q3V8KXXaly6WYIGf26ZfyvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=BktLCAa71HbOjmGRtBRSG7qPNm99na0ieeC-S5vPwmS4akc1Z5Aq7kx8lZm-ArIIOvoHFo-xVUUaOQwTmRclrnBfa0lNVtjbYxee-LezPhdGyGcj9raJzqZGqnImQS7p-invoJeAJyRVKj8Y3EE6ZojAc6ai45GVnDOqQt-uQ_GAnExnyLGem-Lf8INhhKMKJASOUTK0TJpAqGSiHBikNIE6KOzN_nyXRZID8tfo62K2PxGXSB2lF2_g2B3FUL-msHJCZlfT87OKEfmvymnIiWmhoYizC4sZYBDW3JjbiJxk-RvD-_IKQ-vg0aUJyB9Q3V8KXXaly6WYIGf26ZfyvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=ZCEum0Zr_Oenyt8V9I9VxqzOcjkc9qZj8sf1JEbsYMaFwY_fEaFZGFdV3fXyhmaw4tkQirHY8j0UCiKWOFdOzkZg7U3DIDuW3KK-eoUVzUJqOho04rJQ3vMi-Ng_A51OHoORxygp1h_huX1NnBmOJjrM6h0E_C9R4AZ-VqIvVesKAsjMEsuFzaackxRr7Th9MD5xYlxApwB5qBvN5QKTDiYpM9wyPcv7kinvRFpBEvNQ7eGal9oKl2bb1T2fhkjR3MLt0qMAlQEEVGxRBlOGWm4nT2k_CzKvlECHVu4T1ktOF6960lhkku6kbntbntn4FuKJfN8VHLq9Jth8R-RGSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=ZCEum0Zr_Oenyt8V9I9VxqzOcjkc9qZj8sf1JEbsYMaFwY_fEaFZGFdV3fXyhmaw4tkQirHY8j0UCiKWOFdOzkZg7U3DIDuW3KK-eoUVzUJqOho04rJQ3vMi-Ng_A51OHoORxygp1h_huX1NnBmOJjrM6h0E_C9R4AZ-VqIvVesKAsjMEsuFzaackxRr7Th9MD5xYlxApwB5qBvN5QKTDiYpM9wyPcv7kinvRFpBEvNQ7eGal9oKl2bb1T2fhkjR3MLt0qMAlQEEVGxRBlOGWm4nT2k_CzKvlECHVu4T1ktOF6960lhkku6kbntbntn4FuKJfN8VHLq9Jth8R-RGSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=cZFgmS8p0DOvnBW3wY_k9B-arNEOy_Nf6-wNbG_bXofuM4UohiKGjBxboUPVG2bQXKEfwR433v5U7nyh9gv7FhrQm-9B_ugFUvFyHxutJAfzXYNnypLSW5ASP1JkA2yyI5Ljdx1WHvTBb9matSOrFI4mO0NFNPXp76w75JUttDV2DSWb8RCBbOWf_j7xwNP6HrU8JGRhl2GFgZjjMUVQ00wyZOCUfK_-v4UX1sP07c1ep30zZBqOp0IDOO8J6vc6y1RmHb2sg8fhNGG1ZbaAQ_LzEJwSGY2bKsIxjT2dYJi36qtOHmLgCf_A8pf2nIH-AUlfzj7wwXD0eyKQGW9pSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=cZFgmS8p0DOvnBW3wY_k9B-arNEOy_Nf6-wNbG_bXofuM4UohiKGjBxboUPVG2bQXKEfwR433v5U7nyh9gv7FhrQm-9B_ugFUvFyHxutJAfzXYNnypLSW5ASP1JkA2yyI5Ljdx1WHvTBb9matSOrFI4mO0NFNPXp76w75JUttDV2DSWb8RCBbOWf_j7xwNP6HrU8JGRhl2GFgZjjMUVQ00wyZOCUfK_-v4UX1sP07c1ep30zZBqOp0IDOO8J6vc6y1RmHb2sg8fhNGG1ZbaAQ_LzEJwSGY2bKsIxjT2dYJi36qtOHmLgCf_A8pf2nIH-AUlfzj7wwXD0eyKQGW9pSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=LrSlDqVq-xaMbvSAqgixvKDfh61jj5himl2FcZbVJacjSpm9EPL-6XjB0Sp8RgvUI55o5HD6bWivKcyfG_R7sboJscS1AAzC2KVLw-uw97IXyknwvqOspKJYoQuDocrYMPYgB5k6GJBhQB9i7QTc-DGoEZdTkjhX0s4X1CqMxE3VWkA-b5LYorcfwLfPl8OiovT2hQcK66GybyvuuVIjbAH0GqV-D2aW9LLC01hTQss_OrLkwZQXQp6wn-IC-_Z04JimpGldlHsfXhkN0y4KAd-RLvtSD9E-_fSP9XVEbvVvibF0KtFJZ1b9nCsTdOf2BCNYSpBzlnfseGMoS_bBNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=LrSlDqVq-xaMbvSAqgixvKDfh61jj5himl2FcZbVJacjSpm9EPL-6XjB0Sp8RgvUI55o5HD6bWivKcyfG_R7sboJscS1AAzC2KVLw-uw97IXyknwvqOspKJYoQuDocrYMPYgB5k6GJBhQB9i7QTc-DGoEZdTkjhX0s4X1CqMxE3VWkA-b5LYorcfwLfPl8OiovT2hQcK66GybyvuuVIjbAH0GqV-D2aW9LLC01hTQss_OrLkwZQXQp6wn-IC-_Z04JimpGldlHsfXhkN0y4KAd-RLvtSD9E-_fSP9XVEbvVvibF0KtFJZ1b9nCsTdOf2BCNYSpBzlnfseGMoS_bBNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
