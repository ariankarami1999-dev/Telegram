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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 533K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 22:23:15</div>
<hr>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k50o01M4o1plzV76Y0Ixp5_QzbF4BP9nI49McDk4l3jgJe8GprtqBhy8YuTx34omZKhVjmssYJfWdrPjn80g-gCjFLEA33ivEjWO9w1xnxsqf3Su5YJqBEgAYthkyXlY8OXH1Z0JZMcxLESH0HIgnSOeim_L6OI3P1ODUKY_kz51Bo6LZINXtgpV0QGh4j7U6pkUAMLsyY_kqpH_e18i9ZIDuQ2rFYTEtYbGsu3XB12G0ZkNnSpit6Lpsawf2WGr0Cz70eAibiGfhb_cmUViNTPqIqaPqWUKDElTzQURvYwOtOWULRQS6twV_nJPkq55s-aIHcuSRBQnN2Mi9NGhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB9HU5ZK1y_pES4u6u2TlDRba_hyod27-NgTMHFx0oP92ZfocS-qG5dAHlXUgIPM69ryZlPIOqiSyv78xWbpokeNHP-7cb9bQYxlYR_HzfzGiM1cnqO9Z-EGEWR7q00njUyZ-Z_onyqOF9aopNSbSdMd8P8PnWkYFQ2Qv_Xyofll_FsrISJwJCvgdpjPAN2B8vZ7IW1lJFMcCw77ggL-q3jbXXW5lG3GiQRutVGs2Ngp2D1R7FnDbdiSXZLUlyoj7ogZ5clDiBCEb_YZsclE9Yk_HLhdQJnpojYw3uf0X1nemvqlSRklaxOPEY4qrDYjZDGAa0eUW9i19LtlAv0g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLOjewV3Gr_9ahfS_suOPBg73gCyBlbRqhpgwy22yZlTAnAxkEVzYzwIyOzLBkueCqqrEbHSIXy1394fSim0lDSXmZ3uuuN5uVubSAkCoud2hnoAjIcCV1RszoYxkAq-i2AgO6vllxDSk0KA4QzYnRq8fztI51RUphqkOtEX_YRaLFnUHOxQm8wOO6Ok5Gwh6z00RnptiMsqkCEmstx5oBZlAdt4ID3vg7IaGtfzNvnRQHnIC686JY999cxVORwF9lDqBdXHzoWlACm4Rc_hzviGvdIoMAMk4AFrxDp3i0_mx0HtrQ6kwTCabKj8q6pOhIsJpjWK7Or3BuMa7RycoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7xcj1BPSTC4zKjjtvBWx3p2iZVUdapcmZ_QCKhh2nEmdvFYbAGPsRuZE3RDecyFs08SCBotb0_TxWeSfj4zc4dk7YgYwViQZvaPu8GgYax7Jz-fFIzIhnUwOJbLH45S5tHbJO1IQ_g7ZcSJ4u0oMW7wzh2t4f3gpkretcU93n4DCYrbq_gpKb-uosH65kphijOZ0Jbhjyhw8egUPstGJT9nz2JjeL7MiiUTleFW3n8ed3Q6xuNOxPR76k-lU1OZpcec-ZNRq7euSIWQKMDEdmnszL6G9_hxBEgj5ZMm6P4nUuzzUCAwgBG1adFr8qYhKd4157ivekb-ElDtZbb_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxCLummXBRR0V8rQFq203bbTBfwxvOHnxGvh6IncwbAn2T3RF6RFaT5hNi8_Nlu1Q7yFA4wCQ3Ql-t6yX1cJOGHFrF6tQsSKz1amWbo0KAf6N3feXmVzwUCJVsMKXiE_zZODB-6dfL0L5_StTMd7VP0I0p5N1aHZEzhkOZ4EkvsGK5dlsK8JQHKiHsSn6QEmA56TKrDFp65ya1wdD2Jz9JxvZTgRFkcLzD8iiIhD38HG4pvRemf6JpZKOaQtbJQjELiFzccaoKuMQ3ReulN6GDjzWC-g-_o5iMVqLYbqRffT3OD1W4lok8lBscrvNOSPdGvMlQKui0f9r3fPpRWMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goKFsU_9TRN-ta3XCsY2vO_nFKzN-I6ZYRMLXxBB1CBMq5u_HTrwqK-cf_guu5WJ2EqVSUqktWAaz6sYxJm5EKqay97V3fQ3OH2mLTxwLZK5YMh1j9LyVKrs0S9RbMiTtcH070chnmr5Mxk8rjcOu7CJeldOMZqeRnwuUx0maJinlKGoaDDWZvrrebQh0cgn1oxMiDao9rqs4Kd84JxmIwJPvwTUKQ3Gh6bS1xFF-wL2LFG9MolQ2QhRhP0i4HSxZtKuJNEJOV_e3PVIVAGxvkzHe9JyjsfrjBMup3btJbxqW8UxFQYz8J8Nz0fJUCItJGg9lIMbCNdhhqyMn-4poQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKXB16wxGTL80Qr6VJzPhHpJ7A67Vhrkfsq7M7fwegkz6EXxQgbWMWkWxF-0ESVBCsjXk7oixamS3qI0iiZpzYdv01G08aurwuzQ_FbfQKBeVT1qqh6jg57zUdlk1e9Jw-KtPJRpRNoxCCg5Q-9dfrXShYw7Z_jnlFgOc0Q2SPy9kfXHC61Rw9DILrNnjgtma4U6b5RplIBaHIfwQ8DxsVJO1nQQBvtnRo3It0w4Zt5FWqeY6GQ19liYxXyUaRcdSh1IYO5AsSSS2Pfv8WIjceHapWQvpdfnu1T3CmHV3HMFrwWXN8GR6KYKmrmU3wA39-O8FwQXMoJzLpv304IEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJsqek0flmiukt4Z9w86SwvdsQoPf0wHxDBrmZSuiBGGk2uKbia1uH0R2WlgdyaBgOlsW2UQz8b68KyKDpnIczQ_Q0xMW18-2-sbAPM92FSdPXR1UZiqKgWnFb1Q2dQ9S9uanwwozZBoIwUk3TASLxKyYHP3V-6L10HE2PzuRDW8COAcX5IhQXPNMmhTShEvCJ8Lau1NGAjvi-XTYi5bkaxR2uO-Wc9SPQ9hzuxgL-cSKZaQPmWWdq4-osRT69uk2e1vCruZHoGajKh_FSFR_YKAe28JZvaE6d6Izzf8hxqvHlx6l2ZBj8TatxWQEwr-HBWZLY4E7QdTQP0CsHBDzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEux3hSr_EyLFEDL3A8Z_Cekj9EORJmiIH7nUkmpeh84ChE7GYx8Vt0UbIrnkP7UETzBg36TKT49RxW9Dj2aGwi0CDgvphIL-1diMlwNWMkvn2WLdB6jDRCqgdLErTFFBF5Ya6ph_DMNA37m5olyy9BdLu71LiW8Tl_OSZLLO4GONKPgcGMtCUc8JILJv6JtzJTljV1_7qYe_1Zi8RIXewbc53DyNIv1Fq7qMm8qEGZRq9QKIwJirpchaWIIi2TTOX8GieaE6JxFeqOC11yWxiPoGC4x3cv8jU9H0FCeTp9JejoDklzlbO9ajOTMjNYT1sqoukY96cHQAbDYAgJrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbhFBmq260arm3fEGDVcE0ASX5xKIVgqwTh9b4zcI2WjZAr8YKYqlD0ce_cF9Q9SpmLO8Nka7tPhWBlrN0Myn49mK-OS9cMRjXqHxxtqboll8ttCSX9BdhXfUY33H1QDvFdpD1uaYa41PsJiuBU8ES_AvKviigh9h0wVs-RLX8Pc_w1CsYnNrNNotLC0YiCtgFJpIUuvp08iKUXm0TFRlJuqVGmaKffoN2wgJdTmfgQQn0GGb5t5zl511JpxYsayWX3mlaCiHm35p-VSl5VyQgvGP-fc_F21XpM9yT8dWxZlIb1DMneABWmDKPx0rOU_PZsJN6GrZG_KHJW9THxa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3wsmScmC8GSoOd1umJuMyXs_IAoFkgVN2a8KvxZbPpjtwbaHM-_9Xa4ImnKUqRSEfFQoUfgRHBbTcImQG-7FZMqMJKZ7hXMPXG4dzEzpSVrUWwgSfth7ZPeqPmr0G9EHWxlWR8zNSkY_Vvrh7sQ1-DIwnNa3RiTEQsWtD3DEoLEBJS2xDgO9W-7NfIskcXe8wiYND7RyvO2b2pk7JLJGOoVUXh_yuvuoGL_MlNlAL4wiNO8CPNgmkDwPK1rexZnCsN7eCLM7d087a2M79Lc4KzWyngJu1VKJPNi-4x8Epi5JW2KiLUqW1q3xLTGwDnZY4QFXAJrN9lbxHYP3dZtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWN96zd9e-f4EDj-eq2KcxFj3S8VRosoActk10afebmAJHJi4dboBDktd7Yd89dFZPcHX3w0daS9q7KwmjyewzULnDug4HSm-0ueJG1bl2meA1aPZ-GT-BKZhEpAQjdvGIPEpf1UdLrGHoROmiP_wFmZQ7CteZ71cenomBp18pJQmF4rhpPmXhVWfL5xe03q-ScPK_iVrWPg46_bGox-T6idbauZYJcp3fpY7z4diUnWGIJO77JKC_u2dsLBuO-AOAMhSw5ylSX15tln1gJ26dytJ2H05j-2sm0o2ZjOKvpQq5C_dB9W8oXctajtz8_Z5bUxsOD3qQrBJG5IvyyDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4jUlj0SQCda3FQNcScC1W-xtJxYpNv3Rss0Lz3Wyw_Y2DXX7qMEVkUjCMYHYRo3q_SY0f0zaiZY4Oy19ognjlwVzYkam2QSODUR2dp4gaPjFZ_RKB-q4RneVnGnk7wFBhNQkbhkH44Oa3WXU-lzRumc9KpvMkhro2kHahmxycwPAXdWXjqYiRLynB-K1X1bjoZW3OHdIbGeyU8QxiZro6SC9YzhdVXEgB1n73EsSvAXa2hW_WSjRQtbXaLdBGuPKYFXhcJpXL2H4u6-2N-65L3ahsWR5KXzN7NmEZ1kfN6r7mqo5itubLLVAKLBxzC6J1ZchncTI6te-fO6aldR2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euCNY-lNNS7xn0eljc7imZXE-w2NH26cWJbGEi-QnDjRvuhImtBp-AVtPVTJVhdE4kfntyYmXxkUmc-1CkaVc5eEoB9inw02dD6ZhPi2pj-2B4QbesUaZP8Z1K0t1CW-NPseaYEq3cepU1elpjXcV-T7k0Kix5aEvbrkwJJNTpF6J3fyXZPHalV_cfDpJwRMs-oXiZSea8stsUN1xGt9YW_hcNNthLVxMQ_sfZZ8er5XVO_FthTjZVfSNXvmfTA4sSs2utOC2zro0kRCi-7h2rhjytXyrviF218afFX8osAQyB5jjcgGi7OescU3oYGjxg6dkbJkvs--1X2d_jgmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxgWjgkgr9xuw87OzQxUMfadcga7UksRFgaXu60ZW-_-YWDngYr2ze3g_dBhR4aDUR1RhXyAlrz38m7wM4QjvF7cH49Jb25g-gOtjhFTUaCLXBqwSWjUDB3EvYYAVaehi9cqD77wAM1gc3RW-bBd5tplfQL8pDNpnRyt_-ZsOw1gjJegf5L6yvNhwAh04WaQuf0lmzN2dhb3ynj40Lgy4w6cgGSsv5nn6-YI2GuYYPToQllAgqhF67TBFfGlq_GAsgzKvQSmnKnXwf4d3YCOA0lRBIOucmo0Kgw2jbX68DkEQzNhErwpCYRBrWGpnQatTycZcxGIR4UkuMyAbGvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZXiJ7ZJiS2KhB3shdLUZ3FxeTbHfU61clTwrxOgzXYggTCCdSuwiVnuF05cuNfp9M1Tb89FJ6qfbyZhLg4VIbchUgZyx4Hfs51E71p6vddVD5RMKzH18szM5vSxhkE52FeHzUDnwr5qTWUd4BLTYmWzsS8aWDmG2PPdCn4ouiX5bgEZlTyE_wQp7ednZHNv4ZcA1rnhcyxxODeTvYqfaDID2j_0WbjSkrMYC2KkK0ROYbCoZdMPlzyFOe1MPPFdbOu7_oiLBawCJin2bXCCsy84I1Xm189JzaYHwx1CdZ9T2H0EkOnTkCChadBY_wTF8fYhFoREY5sHkjkcCnbuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تونی کروس، هافبک سابق رئال مادرید، بالاخره درباره توییت «فوتبال برنده شد» که پس از قهرمانی اسپانیا مقابل آرژانتین در فینال جام جهانی منتشر کرده بود، توضیح داد
.
🔺
دیدم که خیلی‌ها از آن توییت خوششان نیامد، اما همچنان پای حرفم هستم. به نظر من، یک تیم واقعی فوتبال روز یکشنبه برنده شد. همچنین معتقدم هر کسی جام جهانی را تماشا کرده باشد، دیده که اسپانیا بهترین تیم تورنمنت بود و آرژانتین نه‌تنها شایسته قهرمانی، بلکه حتی شایسته رسیدن به فینال هم نبود.
🔺
به‌خصوص مقابل انگلیس، بازی خوبی ارائه ندادند. آن‌ها بیشتر مسابقاتشان را به‌خاطر قضاوت‌های جانبدارانه داوران و فوتبالی که مدام با خطا روی حریف همراه بود، بردند. به همین دلیل از قهرمانی اسپانیا در فینال خوشحال شدم و همان باعث شد آن توییت را منتشر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdetRpkX-IaULYBaMFuhqaCQrzGyOgx71P8vAF564fuB2P9kHWikff9Sg9L0TKiSQHHnrsFgAqjoPFRT8oGo2qoubM8qIFXhQnSOUFrkJs-iKvrfwSmbvYOWz6OSequ19uwYdzkWUBG6dYRuZZIwa3Qs_tSLbKzKOMXap3NDFEDrRApzapZ5r7H1rM8ZZt-M1lSc08axc_gC7pDJ_1Xd-DYw8jILdR_kwYNp7cdD4UpPZ4KLUgrvQknfjE8-4c0RU7rKFI-gbbWSInSmO3iac4e7jEwkr20AUI3b6lKd6dwYn-gNn0CVyl29zT2--K7K0whweV-fpjaKgz-IG9Z0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpImD531ym9jpkB9QMNCA9CfFX3SUQS1ZvvvzQPPNragmer-tZbz4OstlRfP__thLUc6qr7OpcKTLMEvWkHzQ_fJJ47VzbW-LuoM2Ih6GELHn9gGOe6dJxcZCv2voW7eRvjOA_A39vry8ZrEvPCtz9lRrDttFO5RkB_ptQskb_4lEziyPjZMTf-HUIlcvvle7C1S9PtuI_5SrzVaLpICb6SfgHvG0_AVPFT9d1zt6BUbFVx1eAcv6fYrf8BiHI1wsXh_KQnrIQjwcUjnpTbudAt4Y_XZXXpCsOxlT4viu_onxYb6OGsNonUTKSVUUxcWW9nuFJ97dt-q8ncYKK2A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkcUSJPywdAajBVBt0LBGKpnOslQw3d2gWhJm3y92NN-9-PTTkeknTkfoVfWgLKU1SquYO6OsiL8LxzU5T4xxBx3I5CMVixtAr8it2UDFP5KWoXEJ7XIbv4kpIYp72JgIMr3MzhJF63SyeCeOJlVdpyibrzXN_upGHIAgSDrDvXyneHnd97owWuVIaZ5epd01EBWUP3cMpzhqUIcF59fj2DRg1CaTnnRewWk2lfJkl21-ZqZ07r_4uLCr3u8TdzgZTTJ79NB5ZcvaAKN5O5AjxiT0YCOItkk5YFdCxLvoZf1qRgdGeL0v3IKKN4T6cwl9OyDrRGdN34Ymsm-_tmFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9SLn0myP8JiKbG_qF6fA2GYEhc8tbKS6tsQUyjwYIR5cyc-haf34YY2vJ4UqetMP--abVcZenk9WKMKVVLPsuREAGoR59WCpWpsGFsf23ZJpkBxcZgX1c-5qL6_gzqiC-s6WL5AM4-wfD09mJSjnjNZUOsbZ_bsYfrFIJe3brTe7r-tCcfND0Fp6qeNPitR9zEXQkUjE1lejdRMNvWJ3NTagb0qXNLwBxH508Ilt9dDqAJbTD0hWwoIqygFXb2giPWc5e2W9OD1Jrm6KD7NCWuhgNRcTAAYwoMhER7VfUxZUDaCz9MVQNa1n-lsURc8E_D3WbNav39ROEm_MrJnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FajfY-5QDaz6m6yY6s06MIWWPtxh5fFdI_FC0dnRIDusHz8tvIx-N3DEdi4bU6kqhqkGd8i07j9bLFjVkvrHa0QvUJgfE-sS6dzqOSIA0-GbE48EvZwPWWErd-dj8XseV5Y7dy1hnGFEq45m0R5cEaat1_9AjPFZWJLoIXSvpfoDbVijCXt9dB0rXajzQ901hapfpwfRCXlB5cb4hK-w91Zss0sMjUkvvq9698ZyLMSJjF-Sgouu41l2JStXBY7dGK7UcCTeLc2j8jrhemTDRXseJY6c0us99sHeSteQqHQJUUEipBPFXo7vnRTfMvMbpOHVE_HonfjD-zjMS8M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYoeN-9h9KLX8z72DC9XwKCPZUd5dgRgLvpO-nyXSUvpUd8ynbutZiEBIukOPdb_F1bsGG7KZEw0aJaTbgf8V1gba6HehzbawAa36zCMDqjLEjOOOHwZJ0F_RlLUayYAQnloAQk9VoRG_iqI-PRegvmCj2fg_aCIIBaLUH1eXog_h39DmcvJ9P5cwbiDv_LHX5v9DA0XWPIg0DL-_mvBWdiKwZudLrxiTXt766zuQBs6ANykRQU7l1yM6aZJ5WSPlCjsHHKcp9eV6NBmdx8vw9rLeo_RvksEYOf_rmvvmEm8jtFv3DMxzaT_o4iP9NcOsJlNiSKArhJkdneBT20ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyqw_xrrU-0-tM6kZorXwWoxh5JHTR4Aez_BfTjbT1iw6lkyNEhIsuxS0aX42s5UtgV8SYBfT9nM-0uUgrufYvTd8EppHYXNjr1BvApYWnVvnFpLyxfiwHe5IcMkNoHkRFVWEZDXJtzsRe_V-zQjVbpBSVfIFo5S89RCi4Le6FsM9CxqgboAWQ5dZ81kNI_YAbqoJIjqVBqzRoBuu8nqyiyWmdR7LSSyniYk2BH8dp3qewpPv1Z8oNaD8fRNG_VHI2C31VQXDikLxwSIsJd49qtIrROGnlCZxSLF2r-A1qBN1JB2Nc-rLO30FL3YeNvTeTbbhoy5VIvauKEelMt4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC_J6gGFX9scfc6dFd0AW5e1Q7gg4tL34dY8Kcn58gPrVZAmmuwnd1hftbMADkPRy5Vd7NzAKxIpRBi6YB-O8ikEdiEOkdZ-W_GRjyUF47W4BLnjQpW6KGzG6plg-eLFAhBxX2JF0KzI-cZHAhOSGW03tIPbs9FYOmbGoarxa9uu_T5AeVBK2ahAhI8Ztu058yirLfptMVgtpYs1iTYrT1KcYL7sxvvZXEiJ90D2WZ5RBYegkhievykP7ygTTibn2LT5g9Eku97wp9vZBq-IypU_jJq4nEqJtBVqeMLF9JDLBwZhdJRZmen2Lu8txclLmmF_B5fyxcnEP2s5xueQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGotLQSyOfkqnNoUMEvUoM_raBjMJapylDhu-CLfLFV4aq54TzIK7DzoyFA_frkveJ8ny0_7Ni4ux7UcoNpLHJ9zEU2P-udpDM8W-xGcbH0-4AUR8C-saIsP5JII8MRBsH6ATA88CHWJstLZHZ9SMIbZIcMABRtgdYiYhhE2_kTFr6Efl5M8WoF129jXjcdkCMd7QPdxMQrabjoVkRM3J2mSGNeKnqYqO9jJTOmVaWWrNt-TZrp_GzZpd4j6vwT3sfIqVSOzrVe9XNvO-frarI0NPmMMmDpW3jLRQn7VvKbrl4MJkNzYCivMHyFmKolB_9ft0l-AmOq_Cj5fu5GcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVQHCcx78PpN6lotQPJM11Hp_aPNe9kJGsi1yxqwGUsEYiSgqUWCwyQkrH7XOLLmasmgRYI2aOi1igpygeBG8LQX5S7x8cMoSuGeAGBHh0Ac_3jiWfom7Ffx_JOk1LT5d2YER9kJl8wrjPnczIUz6o8lu3l1UwoNd9N3zNmQrmrSRDzH0bxPSpsGJyII4qZ0RWGDgvX9ix_mF--TLalgotRmPhBqGl0PNnO6GoIrnBquxAqTXZGc5PnFs4O6pm3SWjc-7qVbDOGJ-5FiiL7vNzmuyKUlLM1NkaqbkYasf69UMINz0xaEc-_rQ0RB6d1QZzsD7BKyBEDCZwNx_be5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDyMCxWa_MXZ32hykJ3kGDrLWXHGOUeIZlhXbQki0rrBXTixQbgq9IEtlr_lfUN9iYg3KAJaXnmnMh-fpvjISR2QUSULRv6f0dSbcHF33gUgZgIbz-iDhcFLR6DH7i1aMm5P_jWEXNNIIOBa454Z2Tq7fHqPaJl11ULO-V6vGRaakt7KeTSMTHuo6kTC1jHc3Oihibw58WHcKtOHEYlejBnFewcTwpCSo77tEL9wMRJG0YsKTu1Sdhystl1r1vtCnv6ZzBFnoCUxFnz91A5SIXh-Xo50itJY9Rql88SmtC9xu6lncI4-Uf8tfhSkFuUc5v9imiiOF_gLdnIzqT0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYT-e6E-u-MQjy5jlesN6aYjZUy7UV7dLQpMyZfNtlAiikbDHp1BDBrnt4WT8pD2SjnCK3Ezxtg3T0iB2S48B6gZ8PjuSV2Z9yRz7curEit_doV1m_FWcUZoAorl_B6A86fjyO6VzcuYshyVj1tuy2-XST8_xPwDjU1qFG3U6KEdakusTuD24iFwRJ5sCR0gth06buRh3WOkxjA1aiboyWbDebDijPWp5dcbru8lHjtqlas87rOldCwYxBPwhcAAIvr5k3AytPy8U_L4h8uXE7-9u2nHMupPXJS-EhsOtwppPJK69OmalaQHp3d6u4l1O8dQCeBrIVQ2fEGhbZkKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeTRckbG8rf501Apoe_jADIbMkPG5k6Jua-PY-EnkCDOs6HHk6CY3qoCpZ6zYHWE7IJldiBkxwDrOBqKEBPVE9ir_22wb7uAsYlivdRCyv7Ihfz5Sx3gkHavJFG9K7yvH10AzPG3IBO-cerMq2qk6XjtFiEd6U0A7Il1TM5au_ehYPJzeWyYrYuCcbA_wyt5CuLYkyskDcrhieguou3z9mWveARJwh7NtqjHNMKAyye2zDYYa02617uDVw9Chqp7vPovzDkvp30PgPoNKoE41i6ToDuvIW3TMfVIGGw_6_RriLu9y1BmOY5Yacux49jszUU-BDREAPFQ3JYA90PDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFu2W1LxLl_tyNaYbEjhCnmc_PvM5h1NNvzARypqy6mlPA8uBJ-8Ea1eZ6Sa5WJUVqxL8ofGUVAXgjE7CR2mZFlHo2UUweNy0gIB0UOYWR2B2QZTkN-8pd94OS5sRqcwrzlmclHfAFRQa7MmBbL9_10KVcn0_xCjgeDQRrFf7R0A70KpDd8i6-Pn9A41GWMWHsTFXf707klsOGlXD9i1c5BMKJFIfyNvkCZiTWRbpzxvz_9oH5mdiUgOf_zE6G3SPJ2Uzj_iCxI7VbmXzu3HWGSkr-ZU6HtiM2BjBMM1DzRkicZkDlEN2DVDJ4kUF4QRK-CbJVjQ6yRW3mQ1AluPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCnNI-AV8aSsMeWS7Gml5b0CDsoGsromc6LrJlYoMuP__8f8ewSf_AYza3wQcFNPmveVUaJAjFZ-jFN5hiLx9zNfgvoJwkZuGGXXXIpct3tiw9NLPVrfjR_Tt4fZ1mE-8zFsHm-3GDCrAj7IEuiSp9u8G_2Q573ul92jlMhaQ7XlQxzMnGCHsmEWg1PE0mO-zV4_upagjIKXz4rPo3fc2kj00AJbaZfpYtd-llJdIr4iEsDWabcewgMFGcZfWP2XdpdyHzUTm9TMgP2WwrT1NlCv1q6lAaZbSbe3bw5Enm3gUK0zawCK-qgkJ1z9FMuJOBI_7-RHvDAUnIrQhc0ikg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnoKGlEEvvZ5NJFspNoAQjhWZrDLmQ0UtXD8-pauxgeiwt3bOBCyD-ju3orc08yW7d3AL5Z4ZUG7mCry7MK_7etdT9Z5raYcVxQGVM8ovKWp-VN2CaSVKbwwTQ-grSdo_OX2YImWoKwx3LquG2v_yyG-lQiqPhOljFqpuQPF1-lrOs9cZk-zvXGIVsYOXSnVL2e5Ov4uq7W5XYlUWO9AFzsCsjZsVmo9eHBOGM5zxqHEfm2-bCI0EK22v6rMX-H6tGxj7hQBoRzBeIsTGoy3JsaQ22wGIkBZlY-tzp2DGDYZpV91kJPX9YOM1RqYwFlL6N9tRMRSUKBHnLJTxvfx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_znP4s3fCsr8s_6r2faaC_mmBR0FXME12_t241SZqZt_pu_sJsbjSnj9YDPpF5IkiyH2zcB9KKFQSNBJuml_3F1iS4TtA2zm8N9av1qIE2atdhMYdydyrSe4W8lZV3cYfTB7Yh6Vck8ymMX1rPutlc7r9ujZ_MSc9762d0mSV1FW4WoUlNXrGQaXeInAZ4yhYenVsfovWu_LH-D8OI8938Lw6GvDpzbr-T9WH622JCHFtWihCPwEXB6OgLTTbyQMASqHdHydJQlVzj_L5TIu48CX9YRGMFv7arAZcIUFRtmTBRZUlpDlLQj_S3RpXDmqkYaxXDcbhfqwb3FPMHkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=PaTC_YWaZWV_e2QRJTBmA-gjW6qNbQygPv6Crrwv5cgCRBiaajRyDheQYau52NDR2FNXRXequHtrQxOwbk_hxZ65XhxHZTr7n2OZDrdg653V3A9MTcL2nRUOAmBs-pfOSryVP3_IlhJxCZogOHxsncC659R8UaeqtORrNwrBn33NgW2NzOhBHP-X6bb7dt8YMRLEQOQ22xEx9srZga8n3rVvGeevVPudFPGWuPnFvqsDgO2rqtGsNYQqQQ8sZtcdXMirnP4hdQnmG_lEts5PwTwVH2MXMVVAp-XoURUaecfKFcOUNc1G3k9cGQ2lCAWo-IA-FUMncIutdN9uxiR-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=PaTC_YWaZWV_e2QRJTBmA-gjW6qNbQygPv6Crrwv5cgCRBiaajRyDheQYau52NDR2FNXRXequHtrQxOwbk_hxZ65XhxHZTr7n2OZDrdg653V3A9MTcL2nRUOAmBs-pfOSryVP3_IlhJxCZogOHxsncC659R8UaeqtORrNwrBn33NgW2NzOhBHP-X6bb7dt8YMRLEQOQ22xEx9srZga8n3rVvGeevVPudFPGWuPnFvqsDgO2rqtGsNYQqQQ8sZtcdXMirnP4hdQnmG_lEts5PwTwVH2MXMVVAp-XoURUaecfKFcOUNc1G3k9cGQ2lCAWo-IA-FUMncIutdN9uxiR-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9B2DCE4Th6xLxSPv1vubzwMtklXKOHPgZihEH879abouLfkrwUYd-woPnbdyG7MQM4Nl_T0bb0cB31MQuD8MeBmqcldPu4R24HTfr2hjkZCQt5bvtiHhN79xJpsW7HusymDzQ-dbyijD8IIL7x-To5r4XbbulefixvQtBUiHpkzNMrgMNUXstgAPNWHaVZwQNN_4HIhH6DiaMHClN4ODGNaUJrnjvONa93XrMtumQGplfOYuVMC_OehTrYCsdwbRW17whG4mqUBztIO7f6Jdul_iw0XwTSWcaO1ma6PA_QT17cdISTOoYwiBenIYTSQDk5pIcJPnsi4Yr7TMvLV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewPwmcDrX0Y69VoMzSy6OB3Ur2f0iWgjnIIlXlPteAruMkV6k10mNwgbNKt7EjZ-AvMhajvnGqedy6G-sLxKB1dmNjcGmWJWea9Kxr1542UfCV51mG96iI1w8Vk4Na1GTZ-N1RtR6bmzEIusaPpdVFfG_ROhUi6-2u44fEPX6HXNiZ5BVizEk2ve8VutMsR7EYyYSqrR91tKhJojGkujhVh2RjsbUdyqQ8XbsSg3a0--oQQisex0MDNsabK5GviYuGBCfflPLRv2mi8VzHL6cA3rDBwJOWSSsJrI-rkv4UHNDJsZ2nBDXoKeO1xyEgB1fsou5Uh_Em-9sY9QM2l8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blFjT0z1byrrXQMlu2KVMUU6Wvw_c0Emi29sYV8L9LlOR0m001nuuELzG50bcIYSapWh6PgbBXlAUj5vqkl9r6rWUzuPcTX1CrxY2sOxc6xQ3ySNQhkLuilcMwp1Gcce75GomcmuD4Ojis4grdQt8jwIdnweh4kOg8ubl7bGsO06j4ZMRxDP8qKUbsf4w5ay5qLONNLXKyirfxcd5ar5NxN0MnJ0mObmpyjzyKHEZ1LN3btMXwDqL7Vx-3M52oMlwTIDDCgNf3JK_F4GJvRnVOyQr65R5-Wgh8wDyheMfxh0ol8S8Xe5bLMvSzUHy4DH02kjOWtsi1_1dnwQJpWB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV0Hu5Uyco2kePNvckgobnhYwi-3LpQO8DV3mppixXOZ99E2v0DaqRvprG6zGBExzoFSeOYLAuaVksXgb9q7J0fJkQ16hCWYJ1463fPYiH4RcepKcafHceDRkySHl5rC9qdXPdhwX_2zIOswf4hs7zl6yiNLJa-sVGGmQfpt0o-vi_GX1nN56a2PS-UrjzXt9qfZbBs1fxr5GWLYx-P7_GIHl4do_gnJW3MhERItOrJUzkMKrC8KMqvmioCK20usfuWyvO7vqpGJCVmFWT1X74S3x_fATacqq4cvXDB_fwqzuFkJLYH53z2DyLwejd3_v-HcLR6WWESMejCFylUiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3vMaLOkRrWi9aWXD7vDDE1RakL6_npqnbWbREOEtXrCPuMIWMl4r4y1xGwRUaNnjFP8Jni4IR1iGsPyLkgEdyjOMkNccGbEXDRHvbjB9Z9NgXG5jI_453UigzE61O1CZk_XoBYGsznXQc9aykCK5ou35yKzIPoWEHoysz_LdCUTR3WRCAhtUzgPZJu19KKgj71hnRM4LUVMz9R_-8Ti9073gawuAnotD2iHC0CqrqZTNwXEGebukvZOgfaISp7HDRW4TzI1FU0nCAyGtBEVtgkYR2l1nq-Cw1wYUb2xA-QOBz5BVE71ylNZPua6cSQD1uh5AOsJOH0sr_htgtB90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhpcgCfdosoUdpGnn2bEYJNnZk6ySyBKPZu11x_Gb19UC6KEAix9Ms8EaTfm7tiwEBjgxBpBewze_khKr_ZSZF481uhpx77ULGpghpipRn2Dac8EeokLmxbZYoMrnjbpjp0ug-_lVDuu-nJp0DILoWhfGUZkaA2v84ib7bdzNP9VRr0wzsD91rE9vYk0PR3c4KZ38EU-DZquMSX5jQ7LGZ_UGLdcXrPg8UXUvDGXVm79QWc2YNtSLDyIsoM1Qr7QJQwMIrTS6gcjfllzSWs_WGRHyon85apCPxd-RJ9JcsebrSz_agZFwu_Uv7gUwrIVvrOEGDj6wpJ5fHepB7qRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ZeBFzbKfnWw4m_aZCl03_jBSRa-K1Y2gtp43VT4H_gz-fYQG8DaCQ-hqGYB8jd2EempqfHZZbRc-Kvcjyswzml7xq85aLpB_eJ6__umV6Sxt62gHAAx9nnpUgn68s2Dai590sjOT1RHWShzOaP7e4fr1NxZ-c_91W8wTJ3GUmM-aSLIPQntjJlp2GJAQY2fEYxgJ6ynKD8pK_qQ2LbRMEt8kabSe8w2FsE9boqJabBH-UdQhgtunYuK5GDe4RmYvs4ophmm9eMvls5zD3A-wZjP7UzHYM_ZWyziiu-yPo-wdhG-O7XG_L7J3kLQDtfktz-d4xG13xJ4UScbsjSw2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ZeBFzbKfnWw4m_aZCl03_jBSRa-K1Y2gtp43VT4H_gz-fYQG8DaCQ-hqGYB8jd2EempqfHZZbRc-Kvcjyswzml7xq85aLpB_eJ6__umV6Sxt62gHAAx9nnpUgn68s2Dai590sjOT1RHWShzOaP7e4fr1NxZ-c_91W8wTJ3GUmM-aSLIPQntjJlp2GJAQY2fEYxgJ6ynKD8pK_qQ2LbRMEt8kabSe8w2FsE9boqJabBH-UdQhgtunYuK5GDe4RmYvs4ophmm9eMvls5zD3A-wZjP7UzHYM_ZWyziiu-yPo-wdhG-O7XG_L7J3kLQDtfktz-d4xG13xJ4UScbsjSw2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=INaSQp5rAmumBroTUnZos4nmuDEc5678CrZbjyiIpYz-Mv3TcgfRCgiYqU7GZGDb3-PzcQI5xshlQJnQWs-cB6dLfarc14sAEna_6wVLB8lzx4hllUH7UWcwgNox7EvraJnvhGchxpS2Oz9cPN5QcnvnpzbqihuT-ja9e4PsRGRJdkuaygi0YVtiB5Oyc1sczO6hzdevEqCbSDEMt9dfNBJX1W1uMK49slLgrXncZy53_uISsHTD1dXd6iFn-wq1PI40Og7zWJZi7lsDp2iz7Q-KxrZ1dXHCM3LuxRNnsxF2Uu5qE8loYNFq602w3HvyOhUgdXxeEVGPhBgaZ9bEaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=INaSQp5rAmumBroTUnZos4nmuDEc5678CrZbjyiIpYz-Mv3TcgfRCgiYqU7GZGDb3-PzcQI5xshlQJnQWs-cB6dLfarc14sAEna_6wVLB8lzx4hllUH7UWcwgNox7EvraJnvhGchxpS2Oz9cPN5QcnvnpzbqihuT-ja9e4PsRGRJdkuaygi0YVtiB5Oyc1sczO6hzdevEqCbSDEMt9dfNBJX1W1uMK49slLgrXncZy53_uISsHTD1dXd6iFn-wq1PI40Og7zWJZi7lsDp2iz7Q-KxrZ1dXHCM3LuxRNnsxF2Uu5qE8loYNFq602w3HvyOhUgdXxeEVGPhBgaZ9bEaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=uIS3VILaUJQfOdIPLplR955WuemGizkiDi1AjODC26TAjP6TSPmJj9Gms1NB3htrk0v_fQWjoq2OKdwFDN4cudEIBqj2gsszaz0uBMBK40NJJup_xw-lWIS2UvW2htjsZyRCVPzrPOy036YqDPSXjG4UkLPfZRn9UZ8CyLZw767PDBE9CsjtRAQH0hGX6_rh-6Do3i7BqZROJV7d8iuXRHercLpP6mZrXnt7NLzvFZHVke0R1CwkA1ibGpNG5rf-25ymEnI5naRoH53VQgfj1fvoXlCghzV-xb0G5qCpOq9xRoQH6shQ86gbI_9ZLU2eJxKtUGDAdXcM7KPkwkqy9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=uIS3VILaUJQfOdIPLplR955WuemGizkiDi1AjODC26TAjP6TSPmJj9Gms1NB3htrk0v_fQWjoq2OKdwFDN4cudEIBqj2gsszaz0uBMBK40NJJup_xw-lWIS2UvW2htjsZyRCVPzrPOy036YqDPSXjG4UkLPfZRn9UZ8CyLZw767PDBE9CsjtRAQH0hGX6_rh-6Do3i7BqZROJV7d8iuXRHercLpP6mZrXnt7NLzvFZHVke0R1CwkA1ibGpNG5rf-25ymEnI5naRoH53VQgfj1fvoXlCghzV-xb0G5qCpOq9xRoQH6shQ86gbI_9ZLU2eJxKtUGDAdXcM7KPkwkqy9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrcEwVXopC-iOuJm5lY3gEBPgtEMBES9QK4CtJ9wVk05doouABY5W7ceBwQq8ohmHin-wnyoMuNjvQ3pL9L34dk0uizy_vn9VMf6_bZ53oFA84wyW2c3Lyog10pzl0b5FTeFw65H2W6maiiHBQa42ZjFCz63_wiuzEsWx6KDDDbuLEV13OHtFiQxAy-y76xJqItkNzejtt1iauaT3OKWaYw0z_ajgjI1eXYxF6v27aAVPEQxzOeRmq71wfuUdHCWNMG_8vgvD8Si6K2Pv_jJMx-fF7n_wa4j2AiVurgpSPDsK7JmvTfGlJt-bMqgF4BaKemYlrM-I43U7LRZDVl3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=qUSKewdQHCGfYwZ_eLLH9AIjyW52STdZFq-mqFzBIbDDREXYEkM2nmdcQ-DYFIkpNdUhNwRJ8ZMsRTEQKxZzZvYci9soGJtQCwN_oPGEHvOD4xcSmp2cNI8V3vFCYkJmUlEiXmD8Tg4gn-RoRc-FgmU4mePd8vppmVc-KIvDHPKlIJk3hxRc69Sw-ibFLPQYpjpT1RuwOtB4Gj1qxenGZd_chwuJYN8EG_Haj8SlJopResgUeoeYpFBProfz4CN78AFv1PMNnHYnoJ6DTcpaPbzvHg0pIiSydTcwWKV4ZfKYgGHvEa0VhyPb0MYvpj_6SFfra-2_YnTElxNzFhUkwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=qUSKewdQHCGfYwZ_eLLH9AIjyW52STdZFq-mqFzBIbDDREXYEkM2nmdcQ-DYFIkpNdUhNwRJ8ZMsRTEQKxZzZvYci9soGJtQCwN_oPGEHvOD4xcSmp2cNI8V3vFCYkJmUlEiXmD8Tg4gn-RoRc-FgmU4mePd8vppmVc-KIvDHPKlIJk3hxRc69Sw-ibFLPQYpjpT1RuwOtB4Gj1qxenGZd_chwuJYN8EG_Haj8SlJopResgUeoeYpFBProfz4CN78AFv1PMNnHYnoJ6DTcpaPbzvHg0pIiSydTcwWKV4ZfKYgGHvEa0VhyPb0MYvpj_6SFfra-2_YnTElxNzFhUkwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=Y0ceriXWJ7ByeEBtxrC6neNOqO5hXf4xuYBtD6CKvmyIdcRtiigN21qLKI3lzOVDvNzNDaUUKd225W1mq8V5KCQMzmk2VCqAl5nq2CezKzqB0r4QI8zLbJVxhBjYSnOW2VDuoCiIxwYICR_kkJ42d1UNjsW5EXYhBllb6n1fiUKhwoqUbOE13RoWbwD1cqLwSQcaTaXubKc4jZ1nlWJh3B3Zk4jmQOVDJ7M2uDeJV2jO6-LjcZiF9rLHqtafMI_-C-zze9U8J_TMGsdUHy76F9YLfhPe5T6wM3q_9iyjxcZHGRjX1Sv507Sk-2DvlOySeowyXQdnEx9wnBswrMOvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=Y0ceriXWJ7ByeEBtxrC6neNOqO5hXf4xuYBtD6CKvmyIdcRtiigN21qLKI3lzOVDvNzNDaUUKd225W1mq8V5KCQMzmk2VCqAl5nq2CezKzqB0r4QI8zLbJVxhBjYSnOW2VDuoCiIxwYICR_kkJ42d1UNjsW5EXYhBllb6n1fiUKhwoqUbOE13RoWbwD1cqLwSQcaTaXubKc4jZ1nlWJh3B3Zk4jmQOVDJ7M2uDeJV2jO6-LjcZiF9rLHqtafMI_-C-zze9U8J_TMGsdUHy76F9YLfhPe5T6wM3q_9iyjxcZHGRjX1Sv507Sk-2DvlOySeowyXQdnEx9wnBswrMOvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=haq-7gTDDsHrS9ZAo_zfsFOjPFXiF7Vr60-Phauc4H9rDkAi-LpyXg7Fr3vvDgTpgcIRJkKAKArdYKi_BR2VZNCIlaxBvAR1rHWeRFB-3ofGW7OgUpH-anFOAOKYqg4c6J-bgagRz7oFsnDzo0b4ZC2869IzTEatAEjqTw0ImeEQ8IrSu7GZLVA13wMp6Ddl-yuZCY0fKzmgvUG5qr8FRhA9dxIVSFDlDKtFJm964kayU0t3cRWsmiVtByPNBuW_EwBnPvCs6NmeN6_MVc8V-Sx4J2Csxf5wfFyS74rHmmrtjiQyMUOBluirUAveyf2sWrR_GtDe2ISxphZPyhpLpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=haq-7gTDDsHrS9ZAo_zfsFOjPFXiF7Vr60-Phauc4H9rDkAi-LpyXg7Fr3vvDgTpgcIRJkKAKArdYKi_BR2VZNCIlaxBvAR1rHWeRFB-3ofGW7OgUpH-anFOAOKYqg4c6J-bgagRz7oFsnDzo0b4ZC2869IzTEatAEjqTw0ImeEQ8IrSu7GZLVA13wMp6Ddl-yuZCY0fKzmgvUG5qr8FRhA9dxIVSFDlDKtFJm964kayU0t3cRWsmiVtByPNBuW_EwBnPvCs6NmeN6_MVc8V-Sx4J2Csxf5wfFyS74rHmmrtjiQyMUOBluirUAveyf2sWrR_GtDe2ISxphZPyhpLpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHavaanr95a53tSubLZaaEMUmhbHP_Lkuyf-KL4bOIbi0CNRlBcTsxoYDqqyJ4vbQQnV9juRKIX9vwxA4YlMF31wpzLaaEdw3Q0zB4q0okpWFzfddeGI4gwvFVYNEBf6hdQtev6dFf16fIuxzceKjXqkPmY98ORqfjJ7u3vtTdF23sQf7xnzaKVclGZILTujmVrT0SKYs-LcR4D3YpV1BVxCH3471ubIKAK7sfRN0R7M_vMVzTp98O0mpP1O2ttAZnA_Jn-mgBVCo2lExUFqQr5ErLWN9jo3DwfcI2oOVSXR3X6o7YJ8dWocUAlE_LvX7Fz3Oyi0LcsWOI6aJFf4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIfVj12b9W-qBv1Wzxszh7x1IJz6j7f4bxxf8IkMPEVIPkbNIZbGpRpHAAsAOzPQxWX3mgv_d1B44NCUCuQqqC4i6oGUzh44wbqTvl666CrqRkUHOnX7CWC_T9epORyMAlh3vqxtpagI6TwUsP57i7tOH-BWqLma18A5EzkxKC4w61tfStAKifhVO4nlHhcacKyiDFtD5mbctCy4C5C5EkbEG4IDo2INdRkmqx1HnjNyKEHx4hNdCOCPi4EgTzxglsQViiqF_eU2oeg8rRaCM8-IqANmqPEUwOICol1oah3Jnpp2xOEH-CqEfxtd4z-OcmKEHsvtxAqkOk_XzZbwNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=W_dlgE-f3NjdxG5Z7J8ZuqJIIUhm3FHQKq4g3-XG0bBYdnsrI-5yB0Ay9BIMrg4Jk19W9ULhG_hv3Jhqjd42INoyYPpC9zKqMmjGcK8X9e-_YC92K3WXNSJBIqrIYQxSauIPQVKMMkelrwnKDVAdoCz2DcRSiApLmj5XglUpyKfYjip_FnFvs2OKVvP_UYwdLnjmpw67UkWECIWpX4UnOBA-Auo-zIQFHSqZF6KgFiJKXX_B4x5S-HpaBrnKIHz1SRXCok9IBMT3Kh6YVZMch8jFk8X2qvJV1qlrI0BWC931UBMN8fg4fX17HziJJGLTesvuFM1vTADjn4ezwvPeVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=W_dlgE-f3NjdxG5Z7J8ZuqJIIUhm3FHQKq4g3-XG0bBYdnsrI-5yB0Ay9BIMrg4Jk19W9ULhG_hv3Jhqjd42INoyYPpC9zKqMmjGcK8X9e-_YC92K3WXNSJBIqrIYQxSauIPQVKMMkelrwnKDVAdoCz2DcRSiApLmj5XglUpyKfYjip_FnFvs2OKVvP_UYwdLnjmpw67UkWECIWpX4UnOBA-Auo-zIQFHSqZF6KgFiJKXX_B4x5S-HpaBrnKIHz1SRXCok9IBMT3Kh6YVZMch8jFk8X2qvJV1qlrI0BWC931UBMN8fg4fX17HziJJGLTesvuFM1vTADjn4ezwvPeVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=S0q_8BwK78nIVY7IqCZ8Z-qhoWywqBNua4aC6P5ibS3aTUSMMEGWgZW7tWhQuHcDXvyw8UnmlFN_2PfOhSqy6iOdkRETotYOnO6ooJ04oahN7vQgejhGqkahVtRlSZo80ep9DEeGxtssk2dJMAK43h_nYUUDQKXUZN1UZtFwPLkXQO7Yqb9lzFV16lTcCvZb1OpfMDULIjDDuoPYphDRHrkG6q9VXId1rVfC67nOu2APRrowGFw55x97KVuAuf5pywUjx27ep28XBW-wjekLKUlI3AaHK_w721d7D9I9zhPxFS0o9oYagtRbNtRM5NKetLNZPZJN9qo8an4rEd1hfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=S0q_8BwK78nIVY7IqCZ8Z-qhoWywqBNua4aC6P5ibS3aTUSMMEGWgZW7tWhQuHcDXvyw8UnmlFN_2PfOhSqy6iOdkRETotYOnO6ooJ04oahN7vQgejhGqkahVtRlSZo80ep9DEeGxtssk2dJMAK43h_nYUUDQKXUZN1UZtFwPLkXQO7Yqb9lzFV16lTcCvZb1OpfMDULIjDDuoPYphDRHrkG6q9VXId1rVfC67nOu2APRrowGFw55x97KVuAuf5pywUjx27ep28XBW-wjekLKUlI3AaHK_w721d7D9I9zhPxFS0o9oYagtRbNtRM5NKetLNZPZJN9qo8an4rEd1hfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1u16fQTPCsx_VNslwPPEpIafDAP36-Cg5OibHw0agtu9FHsTYVbMfSDkJDvf8wABAe5tgPGePKYm4W3epKcFISkSnZygJDjSLbG2naTYhMFaUZqDL8KzJ-GPIuK6drSXZgaekOStS8uhu0XPITLXFOIstV7gnyyU0crUIj3WAOTu8-5WlQFH6JCRj6Jg0caBM9fOKPgvMtXX4sNuOaPITD-oeTQ_C63MOq83jmDdOUJkYFBFCFnic0fqUi0vQ4UA6sm5cEMGsS2hIruO9N0bg3r6Dx7EMS0l3CMR2p-rYFT2u4FXrHWCaEzpBNik2AbW8gLhB4fi68UZXNWvNppFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=h73ceEShK8cFqWkW0cSVvwUyjdzb-F5HxjOl2upMe_hoAIrAqwm3091Rm1LsuGtWhOPeijiPNsLBl117lKPU5wtw2JjGZwdsIsIKrkzcV0I-vwFC05CJ6IhbAPLhoBN-nbZQ0c6ARkidaCPwcGDzvoBtrume1nPM-LAtUwKw16B-R6wvY__kUgog0tz2jg-yBbA2s-JhsREf-bm9p_NQctZpUcOibiOgEC15qoqhKIqhulXwjsHB4Ni5jesJZVSD-0k2aVYjuDXQ39Z2LjvVS5gNDoFdiJQArV7C18Pk7-HybxOOq08lv9jsthL21JNcgZPYiH-nwY_FHzv_yyK0-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=h73ceEShK8cFqWkW0cSVvwUyjdzb-F5HxjOl2upMe_hoAIrAqwm3091Rm1LsuGtWhOPeijiPNsLBl117lKPU5wtw2JjGZwdsIsIKrkzcV0I-vwFC05CJ6IhbAPLhoBN-nbZQ0c6ARkidaCPwcGDzvoBtrume1nPM-LAtUwKw16B-R6wvY__kUgog0tz2jg-yBbA2s-JhsREf-bm9p_NQctZpUcOibiOgEC15qoqhKIqhulXwjsHB4Ni5jesJZVSD-0k2aVYjuDXQ39Z2LjvVS5gNDoFdiJQArV7C18Pk7-HybxOOq08lv9jsthL21JNcgZPYiH-nwY_FHzv_yyK0-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMvFLiHqetOIwkrxgYQ8KdbdETWsl7nAd9ROAIysr4drifYx0IUy4IiRDgXe_B0dJh9n2I-i1Vwtv_xnMU2fyPfZfrOYtW-urCNYPw5JofObU2bfL5tDGIsYXwpgl3PbkgPP2KsRRoaWO8mZcCgI1LhDIlv-xcWoh_-oYGjQ_YGjUhJ-MEj8LnyIBpuYgWupPNxSMYUTyN0BqlTY0U695S529nMQoiBo-0P0Tl7R16MklnzVdPC-a4F-j6nmNVM7SB0tAyFvMESvCsXWUrCp268aF8UXC_Wju1XxDoQhecGh4gT3A2AqrKC1lK0x5BLA1C7_iC1jTiHMPwFnAU5rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iC7yMqEDjnda36N5Vr5F2SvEVfezV8To6Qb1zNVEuO6_YaM5dPcRvYtJ-UPLJqI1LD4GqORbu4x0aat_Du1BTk4pLUThJw6OcfWsaPBQzB_sjf3DBhGMpPSxtumGjI970P_LoWS2qVJfrQMcSpp27HGfNCdGQCYvDkHXV9OuA_QTXwFIcYF5l_hgXaTXjXJqKSE4ACWkf5ooFnMIkO3LA0I1Dl7VpvJ9SnTS-yUFaaRC6h1tiG4iCD7bIOwkv8M8BA-0nG5cMAPXMybUVMk9eQNNb6eSKsvX-SZeu-48HpO3gKE6GY0WvdcCV805u4DidsZmO26PvcsJTIrUwN9jXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TR1PRo1lHN4mBAxry_BDC90-5nfs6fQsHgjp3UGPSUifQHv0_l7vHYIUf_adruRYduPiF5s_hxnK55zab6hMF9J0EjnQnybeNl8wRU4aRSZhQ_VYg7saEkwsWUhPCEUemKnSidf-oxxMOWI8arA4L7JvF64pVYAtg9Jn7MxAj6sg9nVIbqZa-2mid_w-zJTwS_ex0EYd6QNnOCe48846TLnikh02acUEerlL-PKi9XT0_Pos9rYM-fS7xxOj4e5SgUBLbUKdyqzrEqCyp-EAR5K1zJT8P1_LU0twI7D4TsmVXzb7_WRhRKs6I_TTffSnVI5LKZEuJvUMbNSEtjuMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZqNfRJElxwu206V0QWiKTn9c8Mw9G1idRrrmiSP3T1R4ByZKo5Ca9OqFaWiCHLDQFT0bAbe-3gBI1eCfPSoIvzWvSa3JECJxoD0tt5vZuRswTtcVblCzR40CTs5-E-z-DZuwPsjKnpz8EQ4i9XtmKx5QBI8NLVLpk7q173up3nEi1APm6gJnke7fn4ZCV9XpJ7TCedOjqYECuGDEKaLe1f96eQOirgA5UemgT-w2ZmxbaH3rgvQu7h5nDHaf0kMZQBGWJZD9dFia3MQtiFl4YofnJP2dSuztPtCjGQj_5JqEIujPvDN0PCovs-vadZOniLCt3-tFNQCR1BlUT0SrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeX8gsjWcDNkvFfBCXhn3kgdGqoxKJW-_jFN9cxagNWsqr5iiW8HzometX_-ImEiE87hdPcNGJ3Oq1I1c-cdMaUZpyrrX1G3RyltNTgekXIK6cVy3wKNHSaE1mJxzeR-iYm6E94jBAnaRtSgatEd0M34C1dmFZzml4iYHO6PVpnbE41k2gs0uq6D0NeXqA003GWtdudbJKdNrPqStdT2-mD5Byzlnw3KdOlt01urCjuUjAsFf4sG1QtFeEcENm83geI2s-989M0O1oUDgSyiLHZXDmg1REfGFIKruF1vOCAsjU3nm7FHatE_TjIU1VMWhTUOKLbXLorei6_2FTlEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmhBUyhmmbV6lT1nADDnbajhGSBemvzF2_YRcINwm7wWq5NWcgvJ-BsSnzxdLS0xWv1R10VngNx6QRcIzdsV4sPrlPTz4X1tfENAhfn61BCq2PyP0q-u83Az_q8Xo2h4srAa342tk_E2z6fLSw5tLaDEjboZuNm-RQMl5kZS_hgLQLer48OIzgEjS0dkjW_K7ADdeOt4irN2bsqX0aWYMmbdO73eGv6qK15B05Xg9geON60ypZSnFzIRfRgQqRqXLTWdSdyJaAwRKY_8--FeoCGQWqLASya_rQHkTAWpK-SJZo8ZdbmXJy244z2lrUslVu4T-a0_KU0sHbuNKqD15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf9roMvhfCTZmRJEMl5PEZjkN8MkyVVkPqHeC81y_1H7M9oCm4SJBrGKQj7IWmZpGZXRUedyHtwjyPCsrEKfVy-78HlGAdpFaWetB7lqC42jqDu9fRRNk_GUVlN_Ke33XqqUkzbBDrDg0N8MrpCFumQAy6FXOquVQzmxfxktjzDpaNe0AlxByuutRMWVGv_JzCjQBmEb-FQKzT3zndslU9VH1QdQ6JIi5_388Mf5alQcyx0jfBO0Z8Js6HQKU0biuIqvB6lo4XDK2MyIT4Rs_9hNP3H3a_PSMB-epfetJ7u9ukuSDaqQ37t8WTyyS53vny7Ue7r_DkVy7pSjFpmFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjasdwqW92DePe3kTUXIHItNoMJIwaeBAxzMYVCd4uIlaqmX256U09fVfNftBIBYjNa4l5PzJ_Dnn7EO4X1snuw9Bs0Y3cuK4AFcF2ANFVQQHU5srBIOPTXZezZpHfYNFqSWZJWaFIV4K7SnEiA1tBrDhK6evqvuS9iTJPTljZXiVesvVAmLc7bsDRyzOXde9iaBJQT14crA8fLv_e3TYbzo2F98nhGUVl5vOxk-pXYPkMW7kfG0d-YNUpondbokNxP0AfuExnHacShQWtoOFIEKD6we0h5zvbIrPRGGoLaebksQYIwrcanuZ0I8n01vgPQMMcCjVEvBLDGHj8mzzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=UEYw_VJ7S95dJKBwRm0qTsuH1jfSIfKvPQZvaZPzyir9hfKBYYWC1tdBmkMFiuOOv1YUu-oFTIrroeDC774uCgAizLo4EGXb815pW_QZnOvaypqS0n6rwF_JFJEE6yCaxtdQ51IDgoDDWAjh2NlMR7Fzyrz8Mu4MVlAYhkcaN2n1pbaMElRPZWIToLPru8fzE-NWCveznnAFingBOCMyqaDUPJgrmZBt0iDCQqvphD5hA6HQgvxWu0ZL1SvdnLzMRs0CAImydVlDMafGVwlyHDk6AtqejJ9DnhE_HXkCTtDWFs2nFS9aPqj3XOLs0JFUAUw6lOSisVgjcTeCwdLBJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=UEYw_VJ7S95dJKBwRm0qTsuH1jfSIfKvPQZvaZPzyir9hfKBYYWC1tdBmkMFiuOOv1YUu-oFTIrroeDC774uCgAizLo4EGXb815pW_QZnOvaypqS0n6rwF_JFJEE6yCaxtdQ51IDgoDDWAjh2NlMR7Fzyrz8Mu4MVlAYhkcaN2n1pbaMElRPZWIToLPru8fzE-NWCveznnAFingBOCMyqaDUPJgrmZBt0iDCQqvphD5hA6HQgvxWu0ZL1SvdnLzMRs0CAImydVlDMafGVwlyHDk6AtqejJ9DnhE_HXkCTtDWFs2nFS9aPqj3XOLs0JFUAUw6lOSisVgjcTeCwdLBJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=QB7_oJRdmYpB3Pcm2Ec6NrjpSQUefcbZicE1EbqSvHguSEHjE9wm9D4IcxM5dJiekULh3zJmpNqmfiK0o_tAIqp61CgLAyyMT70sVUHAEtD4xb7QNWSRTyIog-Nb6vaeFbu78QKz6U24rCOySLGILP8xOIsQPDkbLZNyHRSkbtyIGR0CoXKYbtxCKi9iZ33cNw5NcUwbgCcFIdVpLBuGK-cnL2-cD7H6W3saAlfL6Kc7TolrG5JPTwB-EhKgz6BaZSt7B8CmKzsa9YCMQcHLtj2oTFqlGFSqqjlpa6F-weB_lfyUa5aJ2ERtkA5ovZutAX-XqNar0BmkVdcWAMcIeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=QB7_oJRdmYpB3Pcm2Ec6NrjpSQUefcbZicE1EbqSvHguSEHjE9wm9D4IcxM5dJiekULh3zJmpNqmfiK0o_tAIqp61CgLAyyMT70sVUHAEtD4xb7QNWSRTyIog-Nb6vaeFbu78QKz6U24rCOySLGILP8xOIsQPDkbLZNyHRSkbtyIGR0CoXKYbtxCKi9iZ33cNw5NcUwbgCcFIdVpLBuGK-cnL2-cD7H6W3saAlfL6Kc7TolrG5JPTwB-EhKgz6BaZSt7B8CmKzsa9YCMQcHLtj2oTFqlGFSqqjlpa6F-weB_lfyUa5aJ2ERtkA5ovZutAX-XqNar0BmkVdcWAMcIeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxoStquMSTr-2-ewzyW39eitclURm6Ewvk1oBkfTyljJbKJC136tXwm5KeeU9hh9VLyRJlOs2485EBond6ucmmnZnvyyJkny-CIW3Q4VprmixBkOp9EdeEIZFRbPEfRJyvf-ilmtvbN9sMrvIDIgh2IWbCJ_WNeDjvaR53TH8lnPkn2HdvUebxLLP96E-Yj7XtIV7MBfIGZgg4W6QmA9d3pPYbgrehSh5YW5DlPDGykaG_ggtQRd66QnPHQFj7wzLdnu_PWHU5MwmamB0HveqCe4n4a0eIjdk7ynBPsCVwUAhjbdcN7SXjQBDdnY7ZyEuNQI-N2XoFpOhHDc7XcG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ri3DTidhcGviL74rWGxSUjC7dQdUq1X8zyhmPoNEisNw14kBLeh88RMtOmLyW640iMzUx7o9wVgR4tsATPuECIcMJcEbYRohGi4q2UJItBovfmqNQJqp5ij9Ont_Pgz0lMq4GQHBnZPAaD4kjcrr5NoA5mVDYVD0voMuTEVJy0mZteo6vq-Vs85iYSqKBPwdGOMEdgq1cZhQCNagDUg7yRhzuyej2eKNQe6K8NJnTblFwsckiiG_uCVCxh5H4kNr8RMlg6qJUQJIsml-2rMgJRhzqRH-Vt5J5UyX8vRppWJgu72v9mfODX-SDI6jIiY3JgdEanJyL2_IqxbTybbD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AE4sQVLbPZjyD2iLNoBaTIkrL15i6lGtneWiW-z7CwmjC8i-j7b5sYOP_ne0yUrNlvjIXq4sem8jBh_YyakVDgtaKXy7eDlLT_VquvG6mg0IV_7IG7271zqamV-eExrcGgwxENAvDaxqXqcUxCU2xJLlPTLWY2igNFkD7yhMTomXHZoHEE8ahiWTYT2yu6clQVA8QzYHnE3X_SU1Snu1rDLuFfQy5V1uVIuePwpXwensUFCzLqwJYj3J4J_jA3Fhzt2QSnkY3GzAsV4xArqloHpDdousCSXSXWmVdVAnbfGGXIX1SLgesHeC8YqhurelyStrhFHQpsAER2RPE4sxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1vmVb8KIwGBKiByFBBA1towsSGXhodwxFqCFPdQcYdk195XJWoyLQbk04xpxaZ21y_tlkHAsUEX39AE7O8OMZ7sE_VMuBLTEwJd8n55sh-bIIQaniw1Lkin5ivnLaZtVJ8yz-lCMu3IZDrHUTmrHVmZBEU7KXhPBC8ajPQ3C1_3sV2CtK1I8qRx1Jw-NulTvRpDnrvZZF6CNNOFlha4HG7nbLD28H4LvOX5a0m5L_WJ41K7b_03JAczjZxHhMQzYIsHgJUpLyWdB5Lq-ehxz-qH7bfus6joNKLi6qntZfTMlSGtUdr11WwcJwcAxxkOHpDH1N5P9Z6kS884AUvNyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LelcQR9xF0wxrJguPd19Ask_3fOZP9EAhlLv6SKUbHwd4w23Sjs9kQGx9AJ9vsRYLUl0s1_CEtcxLc8PR0LXf0zcazPFQ0q2Pw8vl1A_5QOkBwe5dzhpy_MWF99HKC5a6hBZqp4IYyGDhBW8xmYbWGv_qv97XKbdUKWWZlBNSvLLWJgRxxm_7pwSiKSllYgI1XSO-y67YNi3xMG03GvY4155LevOQOyVss_L_yYYAuWr-BlYIUsEUe1AUjj8cbKm33tyNHuUULGLwKZfobfrU5591wC2jKK-QxD4W0phJ1osDW4S20zrbm-ofCGj8Kp7XwPo8Msc96p1VOO3RQ1iwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbWvYpUKL95hOquptRGtaQuncLtjWQxuq-UJ-lG4v8wJw4hYZ0tsyo2vzKRPwZZhBnE7nYbZb2fwUs6DRJ7NIA7VSDkOiKcd7IWJ9zBBwKnnX1ISkFDSO5fgRO0xdfEfoREwfmHOfscRrRRdzmDx0yUONUjV79JTnJRLnzk9QMH2shL9013vgXKc-GY_4uScJGcTeptK6SBfmOW_dK39fhWDfaRSjZy_MKezAix9FcLTFYUof4zch-O0Lkm8JAPNpOzWonq3rOiVfsVZj1r-NBKNNvk-nfjZoxJbVXFL1D0tEuvo8AJKCW4z7fLQrVqKizX5r0OSpmU3d9A5CmVfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oImNxCJtpOGdDArJu_JvQrffTS9oJnZhY-4-3pc5ZxWP6qzfrNbL8FXy8pUgrUEKzd_mb8criIRNkOqg19FVNu5XZWT4yJNo933UVTydPpXgDPnEf7YWR11rUX-8mFSK6XQfykG0qdxd7Kcz-CYbWnHcC3mhh4sCqogK9HgAsdsmk2kLjqmlD0whOn__l0GBO1slkfJi_GQQVM2_9w5i7UpuOZEoaHgKNsxbQOJ_dODyLLW3jYzAoS1tqg15DGQgi-v5SUx2SW_xb73H5VhMNd3j0aCDIe70oBh8dnKBDD09GjWdpKRBjcf-AJyUgbDndjKdeWH9LtvT4bBPu3Ru8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOQTqYuW4Z3JseQdSUppUu24LxkErcUkDmKTaI2N5TETEMF2z7aICSFpmd2I2xDkT9qD05PxEE-EGbv027QVCmVTLMVPp6otFceXyJT8qe2NiEMEQ7mhKbGoKF3QOdswhIARfV5WKLPuPqG8ETL4JYmnMJI3865MvFh_mHixw8N2MqdiJKJw8REoW91VkL_2cKrilrPOoBf8Efs-nwiaabPFAi8dHRvPd3U7V5-qOuy86LHHDhgsambcT7flb1J1xIFpwjFYIz7cV4jEQ_rcnzm2gTrqcR2u20IfM8ntUXtpGjS1-5u1OkMmwvheJXGJOovDInPrBAI-gSynTXRbSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=Q4eGvPsFzgLWkVWTS9tZtTMnxbxBgBf6Wu0ANeuMTuwVliAUdzW2sTDvZagFx15uXq3B6miwGs-mPAb5TxBSdZ7dDgYiRr_chV1z3sauAx3VOXOeq4a9prMkj8txRADoT1OjVWEazKdnjJe2NTBASMbYPE3m8ar9Sno-N-Rvg1I20b7wEL2reHClrD7EfYhgvxrisndZ6RnIdWnSgG-gJJzI5Si0p5Fa9j0tI0jh5XWBytx1me22_FwIpNWnTbPsT7IcMakthwOOKMZr6b__JQ5PUk7gwpcyGt7IwVibFcFJtCisP5qv5IiXeGdWEGBt8smC7DCqJWVp02eNAKb2qJy0wx1uHJLsUaBPYA0loL1YV7kPxzKV_wx3k5DL9A6ycya8I--uD0Z2inXexGeZq2SS5tU75zdn_b_qwhbVfPzmJ-uMSf9EDP_Mu2aJ6hcZiQXAeCJBstH-7X1vzEcsThOSahCY3uFyylpeFfAxMaFdhaK-xLZKlbX0UTEX1jUlg45BwQDN-SGuov_uLIuxyAUn9xCOyNImuGBzaqfQ3Ocw5jLbRfEqmxaZm6R4yTTeyxLA875svf4NQ9LFKJj4-hHiV66ZTJadEPHDTxzr5A53Q2heiXkMuNNXf2xz2dRYFkx2eyjoaV8ypIDEWnm7PuTmwCQiopTSl3yAH6NsOoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=Q4eGvPsFzgLWkVWTS9tZtTMnxbxBgBf6Wu0ANeuMTuwVliAUdzW2sTDvZagFx15uXq3B6miwGs-mPAb5TxBSdZ7dDgYiRr_chV1z3sauAx3VOXOeq4a9prMkj8txRADoT1OjVWEazKdnjJe2NTBASMbYPE3m8ar9Sno-N-Rvg1I20b7wEL2reHClrD7EfYhgvxrisndZ6RnIdWnSgG-gJJzI5Si0p5Fa9j0tI0jh5XWBytx1me22_FwIpNWnTbPsT7IcMakthwOOKMZr6b__JQ5PUk7gwpcyGt7IwVibFcFJtCisP5qv5IiXeGdWEGBt8smC7DCqJWVp02eNAKb2qJy0wx1uHJLsUaBPYA0loL1YV7kPxzKV_wx3k5DL9A6ycya8I--uD0Z2inXexGeZq2SS5tU75zdn_b_qwhbVfPzmJ-uMSf9EDP_Mu2aJ6hcZiQXAeCJBstH-7X1vzEcsThOSahCY3uFyylpeFfAxMaFdhaK-xLZKlbX0UTEX1jUlg45BwQDN-SGuov_uLIuxyAUn9xCOyNImuGBzaqfQ3Ocw5jLbRfEqmxaZm6R4yTTeyxLA875svf4NQ9LFKJj4-hHiV66ZTJadEPHDTxzr5A53Q2heiXkMuNNXf2xz2dRYFkx2eyjoaV8ypIDEWnm7PuTmwCQiopTSl3yAH6NsOoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=BShfY40d8Jx3mzCl0uELhsZazlcTR3vjcvGxEvAOdLqRHH55Mh6yit6S2iX74w4ANaPl1t2s30ZdA1XHN34887eT8Fxp3SnxcvXv5ruGtQqMxVOSRui2xdG5C_yn23T5ErIu9O8tmtlZHzBNJIiX7rDlBdOvqklTT9joXw_yBVgrj3yn3md3qxHKbRHKxSLXuzuANsyrgYb0p9MqO23W7_CJHXOdL0G6kFWeypUmWERx_lP80eHOA1Nk6zjIBgbu8Ql_-5L6-1RIsVlZ9jlTLY1zwaYNNROmkOc2b1-uqN1V8rXc6THuoOaWeDF9km1nb8S6b7U1czNoaHseimsFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=BShfY40d8Jx3mzCl0uELhsZazlcTR3vjcvGxEvAOdLqRHH55Mh6yit6S2iX74w4ANaPl1t2s30ZdA1XHN34887eT8Fxp3SnxcvXv5ruGtQqMxVOSRui2xdG5C_yn23T5ErIu9O8tmtlZHzBNJIiX7rDlBdOvqklTT9joXw_yBVgrj3yn3md3qxHKbRHKxSLXuzuANsyrgYb0p9MqO23W7_CJHXOdL0G6kFWeypUmWERx_lP80eHOA1Nk6zjIBgbu8Ql_-5L6-1RIsVlZ9jlTLY1zwaYNNROmkOc2b1-uqN1V8rXc6THuoOaWeDF9km1nb8S6b7U1czNoaHseimsFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=MqbYd6uoHSgbq1IPNe6NOSAM_kadtoD5nIIAblC72D4Cp4HPA2NZxS1VwutQ3ofN3I3SC0QSza6IOdgJ5NC_4lv1JoZWBO-TsqD95F2TZQrNcjv7vEa8jB3s292BTyIanRB7k0wcsiIakvCki3YkmTjgv-aqG7UgEqRNQDTUWDkjf0FrUnXd7VGRngb919DqZr9bpJ0LrwSFmMyRGhCvt-tiwY4LEqX0mI1BpA-FSx2lJdZ8z4zIzrVtjdX8vGwFDd7tuXd8gtfFj--M04AQPxMpxqJKtLv0JqZnKz4RrynrRtgquXEYRfQiBt0KaV2vsdUmZzuruPJX66LUbFMrUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=MqbYd6uoHSgbq1IPNe6NOSAM_kadtoD5nIIAblC72D4Cp4HPA2NZxS1VwutQ3ofN3I3SC0QSza6IOdgJ5NC_4lv1JoZWBO-TsqD95F2TZQrNcjv7vEa8jB3s292BTyIanRB7k0wcsiIakvCki3YkmTjgv-aqG7UgEqRNQDTUWDkjf0FrUnXd7VGRngb919DqZr9bpJ0LrwSFmMyRGhCvt-tiwY4LEqX0mI1BpA-FSx2lJdZ8z4zIzrVtjdX8vGwFDd7tuXd8gtfFj--M04AQPxMpxqJKtLv0JqZnKz4RrynrRtgquXEYRfQiBt0KaV2vsdUmZzuruPJX66LUbFMrUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyfykRDbBhJ6lW_rTz9E7xYW2qbvQMOFEWaoL5s0CE9NOEEIcpGozRJ-UvdIKM64B8tAqjFiEfatxmti_sfXC9uUMWbs2ZpwdgNX-UXrAVbXdQowPjMvGO_JRN55MyGHRx6nE_fEQd9o309RzoiozbT0z3YYozInhigoOGD0EqzTVisB6yvl50vzn-X84dP7QHg05Zzx2V55I0SX2DME2BxnLr3ORlC4WR3pjRpDf6v0THQlZ7brohSHIHUbbOhut2bubGeaWmZSPE4saGLPodQDZB3WoG-_eboat_imDKhkEx_Zx7zda1bCoCp2b2fTUbae188XXvXfOkfwx9CWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1EF1dggRgSLzRqq5FY3RaCKUGTP9icr0RSkRxQN5H5xw80D_I3jgIO4e29tSCGrv-mNj2SmnCyMZNwlKjtdTR-7UCrDnYbrYpKxJ5DgDSTrjsgFhnpGMrw4vZL10IKnXigB25yPxgIWutI_lXDtj1ZpzT8Yq9SRjMU4qfipyy-hnp8CKo8Mu79DGwPvdhcG8BVEzVihDjZhP3VcQ-0j9Ev98e2KhieQ-naLhRQEseETtNY6uejmmtZBAxFbslkQa2wSz59LA6sc-9nb6vpSAyhMS8Y6G5wkG47b4Bdsnm2Lacny7bBsKIyiB7FvHKvgCM1y-trmKThDU21i_-2ECQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN2BD2PwcDsvY3dpmH8xIV0iPT5Tw42-_L_J93l3FJZFzwGRR1_JIdCXeapoIQ6n2wKxLxG1FRSSRJQwCHRZHnSTYNhVczo1y3GZqzVAh_j4I33QOSQrH7JS3pMXXFvJzfD1hdz9xSjC6wUvyvt2euJiVeTNAJWOxzaEwiSxIzC1mfbPOHZpGwVDpM9QNF04SdMc6J5V0A5NcyeP8ADmXR64gXnnxHwt9eMOrY-ZOeb5JA9aF5Ut5TaD9-_0_1s38005vZR2J5oookAJ0yarrysVJsL6Sc0Xi-Z--teKN8bz8XKjm-J-_F5H9xD5kuhSiH35vms573mPAuTzCIAxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiWVAr1Add1Ib6pqXqTOMIiSW7PKgLYXtW9RdLY6NdTpbFoqrlwvWs5mUdoXBG_sRdvVA6rymSiQtJFXPJI0XbCQmoqJBjAE-uBmnqEXErZnni1HhIVjbal7oE3hL5IS5WS5A432VOZgQfJX-kD6ffYYFaoWXxLAZLiFownx1Fk3x9ohd4kTvlkTIMrf0RHx7Omp9nQMY4YUZ0tqHqdcHz_kksfeYTBgfiXVH4tXfYYa2c_NyfWlstqCsScwkvERQJ9lkJiGGuZTNOiol9GbrPcDBwpGfbRetPvnCGN1Psb6TLWJiDTZS_4lNPrstG3WeWGeXEi5FZ2tzXCLBkLjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ5udTY3YZraoCPbelgAKJerOX1pAqWxQhgCE83yOJ52zVJB-DhWsv776VsDtOA45UDb2qiDe_2lqNBRJ0Cjhhqrf9w41M3jikgFvMl7ZBuG-RhOkcAC-P_A6XER90CcX4iVcjdbqKfeCIjXk_sei1FQ98gtEuyqp51z4uEy17ciSFHMY24Jv94jubKmk1YycjSv8g2pofXcJuJSUO1fAr39k2t6Qe4vkk3DLcqljM87-fKm0H-OM39Um2krlUgWvCAg59hnuC-FdH8xoPorIEtE42ExbZ29x18HT8gWUrjlHohvDDkZT3DLdb-v1VP17iz6RHIciAvQGyHhH-QYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjQyDxNLA59nkNmR_mecxE8xtysw9XfIkW3BPvYu-dgB3-rH0DP_iXPET5C8EIDQxi29VgPCFJPzs07eKf1M7O9Es5u0AYJX1hm3kY9SOrs_NyswpGaBql-B3KcvQ8G8F8jy2TPieiHxyI7VXFlul1YSEk6qcVETb7QFu5F8gaRMhA11XBtFBNFoHS3rSsbRVcN1ibMTM6KGUfm31LBXPJIh0V3dSgmHul1mZUe2XXL1EBXVf6z7X4gqltQ-sRvup7Ak4JvGwaOZBBXox1EAO-DuSktTmT4MQXMLX6njG_q6sdQGSWz2szz6UTpcrGtS_N8SlZ-l4XyA4u1lrlUKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J76loootRiLLwViF7zKLGD2sEb2CAZHZSxM_LWelsL7Jz5WFfoAl1ZxjXwyUgp4iPHrX4CSonqvvk3IDlu2DeZ68ebUmqVv4_6V8FW5q-N5HdFcgg9unZf3SvIEO1JAVWsnM33Oy19BKycY716ezTjiXDpRy44y7BDtrG3-j8hxlhTcJ3gYSDe6OruIhNLpubBLB3A1CCfM9scVENvPYUFzisLRsOnTzYhyCHoaMpUKneozcf47VimSVpvkh53Zqk0_flLwHnvZgZRkG1Z2HjWTCVB-8ZX8755pVnjToBDUq_IfcIFTEef77lVzHAY5javzsxp9aWt72le2PwBqVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jt4Sky5APX7vWyPq-HT2RgZ5uoLnv7FJctlecVsRB9jSZiaULE7GHHvrNmK8uzWgTJ2zqVYbh7xPjyJOzbhEqEa2BudJUZKToT0Uq8_Cyg-YnbSfA06oyM9WlF59KuLdhZtjMtPeB67OTuM9-4eCHL25sj7m1lVoZV71tWwUFbn-kFQQI0hY59u17TEa4A7gLkRZDEv2iI-GmSoPXNXd059WkYnNgp7Mvs_--iPAzSURcNsR5jADNNxTc1guIyKdN59yglvVXwAunes3SkQQBNt_ks4UXR6i0aTkEZ6Zwy4D1qkwaItzyfD1XAjNmIZsZoGBXv-8H0Xtn7IkF7stiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=ZIiyb7AQi5FJ8ZcRP4G0Pvz98_AbOpnYQADOrmqZPWC9K97Weq_ZZoi5CrhTudrFf8pxwNA2Mcg34vpaOk2tW0p-gOvGSbmA_ZldHN-3fCY3R6hKqgB2EKzOq4PLsUMlNDC4tGvHR6AWxHYdNe2IRbCsVrYGL26L1MidjzAkTWbS16KhXOJEpSdtvk0wgGrdLSdpZnPh_XRWEZOHywUMXnQVl_pxibUWb2ME5-cxDPvMDOwsnvql_fRXCnx20S7r1Um_B1Rxm3t1r3NB9rmfcIAfHkiTkxSXxmm4kvu29cCr28ENHBZs0BrQu4539wnZAR6RdV1lg7iy1tpTcwr5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=ZIiyb7AQi5FJ8ZcRP4G0Pvz98_AbOpnYQADOrmqZPWC9K97Weq_ZZoi5CrhTudrFf8pxwNA2Mcg34vpaOk2tW0p-gOvGSbmA_ZldHN-3fCY3R6hKqgB2EKzOq4PLsUMlNDC4tGvHR6AWxHYdNe2IRbCsVrYGL26L1MidjzAkTWbS16KhXOJEpSdtvk0wgGrdLSdpZnPh_XRWEZOHywUMXnQVl_pxibUWb2ME5-cxDPvMDOwsnvql_fRXCnx20S7r1Um_B1Rxm3t1r3NB9rmfcIAfHkiTkxSXxmm4kvu29cCr28ENHBZs0BrQu4539wnZAR6RdV1lg7iy1tpTcwr5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=gkgNGJ1TFvhTYmDWkefVsE3heyoPOUAZwIt36TmiG06IkDLT15bCw_1A2UjjUn25Zgp58FKR0snfTs0qQN55RUOSaLzF5z4mRQHdVL7UQAZwyY0VHvyf8DKV5-JrIdkjJGB_HSsoNNV2gKSNRfc4HXIeYyJU6DD3z59hjrzjiaDfDK3Er9EK6o9nMzduYq0w1FkQwl0U4jwUM3A-gWVCj71iyByVDEdHYt5_JhtDA_yqMyZ-WgAMwSaFo19_RkRSTb-qoHwOZsoDqmGgD5PiMr6vpCADAJsO9-Abg8Of8W8Zq8e2k9xdGfxxmI0dklSuNoGUkAVjh-TIni_GSs587KWKXKw5e6sh-nblnextGq0QLYMil82lSf8-xXaZYQiObku9IpOVPCq3tymAe_4obWLJZ7iIiblI8VZXuQSwLrMEnWmIT8ssaixg8u9sXVKBobgrmTuEeUbwMfY8BtAV6dVSq_9HJjJCPyeRf_AmX6JBZs3WrAMiM7WUJU2O3UuRH8cWcGDFUOr9rIAuZRdFIjaMGlH0ZzfrpBeNC86SYbkxrlYR9BDgaYtBw9UaN6DGtt12qn-QY7r4vUv4uyiHNT39qD3mWwDl1AFsBwMvitVZ59vx3gr_XIAjuKABnRmR7Vuwdslgv2O7Oo0LuX-pEwmGVCe1PwvHFNIAtYES0Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=gkgNGJ1TFvhTYmDWkefVsE3heyoPOUAZwIt36TmiG06IkDLT15bCw_1A2UjjUn25Zgp58FKR0snfTs0qQN55RUOSaLzF5z4mRQHdVL7UQAZwyY0VHvyf8DKV5-JrIdkjJGB_HSsoNNV2gKSNRfc4HXIeYyJU6DD3z59hjrzjiaDfDK3Er9EK6o9nMzduYq0w1FkQwl0U4jwUM3A-gWVCj71iyByVDEdHYt5_JhtDA_yqMyZ-WgAMwSaFo19_RkRSTb-qoHwOZsoDqmGgD5PiMr6vpCADAJsO9-Abg8Of8W8Zq8e2k9xdGfxxmI0dklSuNoGUkAVjh-TIni_GSs587KWKXKw5e6sh-nblnextGq0QLYMil82lSf8-xXaZYQiObku9IpOVPCq3tymAe_4obWLJZ7iIiblI8VZXuQSwLrMEnWmIT8ssaixg8u9sXVKBobgrmTuEeUbwMfY8BtAV6dVSq_9HJjJCPyeRf_AmX6JBZs3WrAMiM7WUJU2O3UuRH8cWcGDFUOr9rIAuZRdFIjaMGlH0ZzfrpBeNC86SYbkxrlYR9BDgaYtBw9UaN6DGtt12qn-QY7r4vUv4uyiHNT39qD3mWwDl1AFsBwMvitVZ59vx3gr_XIAjuKABnRmR7Vuwdslgv2O7Oo0LuX-pEwmGVCe1PwvHFNIAtYES0Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=H0R5S_U2gDXb07dQgbz3fZLdDol95cDxjVNT9B1YJH2fAIMUHPh7EpytArL-YwLsTO8RCQp3xgYOz8oV6FhiZmL4rhqo0eCicMoe18ntc3m_NN6Zvy_ZS7RZz--D2aZS8jGgrtja8cvjMBdzg4KVmLHx-RIsj1D8j0SEv3PrRjiqFyG-4Lo2W7Qa7LDAlssw1Q7HmsTIDx9ImgC1JnG-u1Vwo7o4hylFlrytNhcIpnEnH8HWRg1LKyIo_DdxVefgJx4f7cHUOVmSbLFzKM9Hc7hfIHoY3hbABH7rd9tdwQHKNheH8k8ElYznYrMuYDVK3A75T0C_kyfhJLQgZXGGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=H0R5S_U2gDXb07dQgbz3fZLdDol95cDxjVNT9B1YJH2fAIMUHPh7EpytArL-YwLsTO8RCQp3xgYOz8oV6FhiZmL4rhqo0eCicMoe18ntc3m_NN6Zvy_ZS7RZz--D2aZS8jGgrtja8cvjMBdzg4KVmLHx-RIsj1D8j0SEv3PrRjiqFyG-4Lo2W7Qa7LDAlssw1Q7HmsTIDx9ImgC1JnG-u1Vwo7o4hylFlrytNhcIpnEnH8HWRg1LKyIo_DdxVefgJx4f7cHUOVmSbLFzKM9Hc7hfIHoY3hbABH7rd9tdwQHKNheH8k8ElYznYrMuYDVK3A75T0C_kyfhJLQgZXGGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=ZIqdyFMz9dMMDVkqga6aqu7FfWOg0mT5LoMV3M9CQdXFZ2734PajNNr9iXCJNpVSZRawBjKrcLl72QJh-Uo7LjuDZN3wq2lDKH4v0ZpVFiouf0AGiRGf5KXZV3ZYNyyZt_hARgqwEFgoh1-ADofkpQLbWZ15U4w5DMlV6sQJG2fnpgUyaqMzU4F8uCf2-GAEUuBdQZfOSOynEnOPPj3Hi4X7sdO-Sz7brPTlZSQCoMk03rmy7RV1cMF2366_wti6eEXH9DizSeuAD28VJ8pKZSlKad930yKrrUpoJeb6NSZIUHyipf7ZdNgskSwho121h_f0CcIwf7w99uE1Tdpv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=ZIqdyFMz9dMMDVkqga6aqu7FfWOg0mT5LoMV3M9CQdXFZ2734PajNNr9iXCJNpVSZRawBjKrcLl72QJh-Uo7LjuDZN3wq2lDKH4v0ZpVFiouf0AGiRGf5KXZV3ZYNyyZt_hARgqwEFgoh1-ADofkpQLbWZ15U4w5DMlV6sQJG2fnpgUyaqMzU4F8uCf2-GAEUuBdQZfOSOynEnOPPj3Hi4X7sdO-Sz7brPTlZSQCoMk03rmy7RV1cMF2366_wti6eEXH9DizSeuAD28VJ8pKZSlKad930yKrrUpoJeb6NSZIUHyipf7ZdNgskSwho121h_f0CcIwf7w99uE1Tdpv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF2IDu0CR7CO7jntxNKRM_6XYALVfNmGH2CEIsirxpU3Dckp49Lw6_ox8suSIkKnBAfm5qnwI_SmxW9ClLMDCyeNAihguYFX64U1B7fmi9CVuSOyDcyqNGFHVftw3eWEvRtFxUXG_-yBVnoatZYQHf-kpQDNCoTd1DNOyde3z7iWCjAKOQa2VBdMsSZJrTTaourqBbdR0pIaqyXQO1B1DaKEey9emrWsP2wDsL5njJOkYtKqSuANDmy4F2BrIEvd72EJSbtJo5N7Mmp3oROVVvGT9TQKdRI_tPHUuweOOA42dPna9GIVNJT2V2MxCYfsVPO2I9yu2jLlpXsl-YaOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=gWYyyD79WsKrA60H5PmWn_7BqpPFHHI5jq4kRNXr5gGdQ8IqvM36B3qZmIZ9xDVwlbVx_9fkebAFC_P-HY1wDj14F0xHi19sxDBaLptg4-XpJFy2rJNKkM_W7wT2oJahDOOneIOgxTUZc9xuztKvfmo43KPWB48RSWi_fke5Unt59P2TNeHpBLXh_jtOd_ptnohcJzKqo41-qvh-ricgVXXASnfQ_yGqP8rLkuRVaeEZZAIFuQizlr1KSoG41i6altwY63XdJvsZpFKwZkZlrhHDxe-O9i3lP0J24CzDZqeyCRX7LryVns9x3J6omlmJWN0of7htmT8Q74QfhVsfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=gWYyyD79WsKrA60H5PmWn_7BqpPFHHI5jq4kRNXr5gGdQ8IqvM36B3qZmIZ9xDVwlbVx_9fkebAFC_P-HY1wDj14F0xHi19sxDBaLptg4-XpJFy2rJNKkM_W7wT2oJahDOOneIOgxTUZc9xuztKvfmo43KPWB48RSWi_fke5Unt59P2TNeHpBLXh_jtOd_ptnohcJzKqo41-qvh-ricgVXXASnfQ_yGqP8rLkuRVaeEZZAIFuQizlr1KSoG41i6altwY63XdJvsZpFKwZkZlrhHDxe-O9i3lP0J24CzDZqeyCRX7LryVns9x3J6omlmJWN0of7htmT8Q74QfhVsfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1LOWcS3qPLCI_fbJQOTLy7iJJKqvjoH4OCW0mz3uiom6312-vbTf0aUkrNKqr6tMei70RDRIV8YasHSBZAHTdGyP0GUHgDVNASr-quplhmZNj8_p5Hth8W2WZtqxdGeWJsKKFt8BFoEqJg34CcKANlsGkRDmSpX_LbOp_xyfWosj_FoovNLSX724erGF_e1r082XtL8bu7liPIjjzeuaD9Aih-emcPRpGik6Egon9_Ag4hZRjmFOgv-ncKRGmIwV8_ntqBQmbxutoQFirxvgZjMtGi9mtnWTns4jH1MOFUoye2i6jVgjyKZbydNVSONYsIkmWo06WnseTIT20RhyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4GOnDFnvuirAoEaFPvCxWMC6rqVzWuob54aeP3T8WK6UYKVoDjB3dSRHGH_iiN4nrJuYTj6nHqCjoD73npLt56m_xC-QwKrDqoLl3MNQTdxxoJprb57P_R6y0zhBU4_b1KtNNlD-lf0ACX5B_vas2rg76hlVxc85hMhS-w_7w1o9EG3D1HEETCOgpylz5KKOgHbjuzEHmC-CDhKVVRXosn54D6oI7MK4AVC6p7AHdeNaFTBoh3sZCMoiWbsb3-nB6Q1Vv08bvBgwvZWO1ZhZ3M9CbBJQWZE0f1C9MyjP6IMVgw3_p7-sWa0zkhK_21vQ7NDfBFaCyK60OQC4xwBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=CSybmRQQLZSMOyBLXjqqprdmDOrK0fF-f-4-AaSH0Axy6wgy4H1I9fVa7HAe4YJdbVYEvV3xK7lN2LvJJfprZ18YdEjoMl-RFEFiiKwchSKtJXi4ORtf-8WMcDpp1itngraKnG6wKj4NJrETfdZA7ksp27nBYoeK2caG4Un28hTSx-g9dfaaMQaAAh8-WDMLuftLaIx8n6NbqW2tJnX4KS4l4EvFzoxPGKLnas8OZFzQM2ViIEsHafOuErsM0CZ4Le_KIkpR6PRxbbgAf4LUJ_zqX-BLmBP0d9cJ6Iy35tgeBumEe86Lb9UaQJkT06yYgeZIHWjt1x40PNmVlz1oiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=CSybmRQQLZSMOyBLXjqqprdmDOrK0fF-f-4-AaSH0Axy6wgy4H1I9fVa7HAe4YJdbVYEvV3xK7lN2LvJJfprZ18YdEjoMl-RFEFiiKwchSKtJXi4ORtf-8WMcDpp1itngraKnG6wKj4NJrETfdZA7ksp27nBYoeK2caG4Un28hTSx-g9dfaaMQaAAh8-WDMLuftLaIx8n6NbqW2tJnX4KS4l4EvFzoxPGKLnas8OZFzQM2ViIEsHafOuErsM0CZ4Le_KIkpR6PRxbbgAf4LUJ_zqX-BLmBP0d9cJ6Iy35tgeBumEe86Lb9UaQJkT06yYgeZIHWjt1x40PNmVlz1oiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=eR3urukbWOwJh5j0GDQ2zPIO7Wt2vAO6SFqivHzLZPBcDW3eXKGCKfYDU-hOcLB42xZEi7ar3dntJreMM3dAyWt3MR0d277fVqZHpZM8yknNNuSifX7cXIjQkOkeeUPiPfW32G47uxEJ8Z--mLR8Bqwe-Liuo6TfOJp-NVm3bmFhl21YSfiXLQrEQjMyooIADFpjecfWYw3wJoqF-QregoukZRLQX4mpPTowBize0hFz8zWn8zbihvriYGub7JTkRf1hPtRQUdbkLKx4Y2UzYviycmg6T2Isav5cCpAChifg8Odo3nUMmWSOc38cfR7DJB2ohX_pNNsNS9QQmeDQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=eR3urukbWOwJh5j0GDQ2zPIO7Wt2vAO6SFqivHzLZPBcDW3eXKGCKfYDU-hOcLB42xZEi7ar3dntJreMM3dAyWt3MR0d277fVqZHpZM8yknNNuSifX7cXIjQkOkeeUPiPfW32G47uxEJ8Z--mLR8Bqwe-Liuo6TfOJp-NVm3bmFhl21YSfiXLQrEQjMyooIADFpjecfWYw3wJoqF-QregoukZRLQX4mpPTowBize0hFz8zWn8zbihvriYGub7JTkRf1hPtRQUdbkLKx4Y2UzYviycmg6T2Isav5cCpAChifg8Odo3nUMmWSOc38cfR7DJB2ohX_pNNsNS9QQmeDQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGh3HMyaOa5CuX94ppaRNtCA_N1_ciVlvvCcRJnkdnjjDacn1Qyvjt6BUlfWRKGIFOb3dAROO1qjAI_lISrSdnoMeM3tZyX4Obi8Dw2cqOudaZ24y161JNpHJ8mo7mBoxeT656PneWQFZUlG3d2BnXp_IpqxcWVttV2bUWPgx5WC5cYGCWB2aJ-Tgs063qBNb3hEM7LG7-qExsC1csijQgrW0_Nq6N-JMKQ9sT3Du96bg-DbAwMxSugFJdFl2K3AWqYNF8F1vx7R-GzETvXB9msjY5UqiPLawS_q1348Xtt3SKnuColFy-q-oPQ2hO-3w254PQMn_xyUJURNrVpkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEAvMCX9RqZYrn-Tn-JrVowQfKmA-SoS4sfNJetvVw827BN-Ol-3hg4BJSwZPEoo1tAchJ1neEk0swa0pm9Lux4WSHJdxH8-VhNTTlIUKBa89NQHkE6R0jP4hUM4IO2rBmhByw_UADme6T-gL4xObBdV5SYjrv4tjM21_Fn2tgijl8M-ic2O-hu4RqB1g0orF-E_icFRxU3lV-LROdmeFBHkRzLdWuVH6Jb4BntoubF_Xtljx6-uWtWnTL-PQDFbnf2xXYrzfNXhzlMGzzKO8mSEfe0buKVK4GAjKq9cvqUFZFYpW-VFYndaauzcpw22dsQyTXIImqkg8DY0l43R2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=baFKWZ0jUziMoD-JcCMy67VhEM5-3JqAmfv5FxWZwaUwvgjKi8Ast2evLpH0ZJCkTcFABi5uf9p5ATJbabEHnRBeNXFvHzV_gLRpxyHWxii0keQ54nZHM0tEFeYSfyG1CSi8kFTY_eS4W3d_g-5m32RZjuC7uA1vIFmK17dlNmFD3rs8gCiYTMpr4oG6led2n49-WrYAVG5iR65vI9A2GYz2aW60HvefCax2YMensWQOYQgMpDpmPjRejdqUxz9-4EAADmK4J1XYD_hEGVaBgQjuzmyMNBM60Jy0ocpgYal7X_Jw-1V_V95OD6-0XbBzKjGCCGjtke8YXqYrQ7u5oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=baFKWZ0jUziMoD-JcCMy67VhEM5-3JqAmfv5FxWZwaUwvgjKi8Ast2evLpH0ZJCkTcFABi5uf9p5ATJbabEHnRBeNXFvHzV_gLRpxyHWxii0keQ54nZHM0tEFeYSfyG1CSi8kFTY_eS4W3d_g-5m32RZjuC7uA1vIFmK17dlNmFD3rs8gCiYTMpr4oG6led2n49-WrYAVG5iR65vI9A2GYz2aW60HvefCax2YMensWQOYQgMpDpmPjRejdqUxz9-4EAADmK4J1XYD_hEGVaBgQjuzmyMNBM60Jy0ocpgYal7X_Jw-1V_V95OD6-0XbBzKjGCCGjtke8YXqYrQ7u5oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=NB6aOxAAXDH4rCFOe83mE8UvUmebYA5Gjr26AhlnYkT9kuqHA2oxJdq-IeuGQ8AIMRnYeJLpK3Ze9C0UXZYgQqu42fItCjDGdvvWlGb5oKKAAZcPk4Z3gAVxs85ilcuQC6wN3FVMTbqEhpKhPJHxEunB92nwiT1LmZ7s8ClAdO-HKvn3B02U3UhcJYn0lBzutz-fHI0ZHAFcetYt5BqIH1yT9Ksxb1OWvLXxOSgjnHgfnVoM4OsNn8WYvsknDRueq8ptMZjdNQZBaYtoPYlQFu2la-gASkrzf-thG8ovZ_BRf3UAeGcHeNhUzrh4vYEyHhGuwrY-wa3kXL2R-IVzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=NB6aOxAAXDH4rCFOe83mE8UvUmebYA5Gjr26AhlnYkT9kuqHA2oxJdq-IeuGQ8AIMRnYeJLpK3Ze9C0UXZYgQqu42fItCjDGdvvWlGb5oKKAAZcPk4Z3gAVxs85ilcuQC6wN3FVMTbqEhpKhPJHxEunB92nwiT1LmZ7s8ClAdO-HKvn3B02U3UhcJYn0lBzutz-fHI0ZHAFcetYt5BqIH1yT9Ksxb1OWvLXxOSgjnHgfnVoM4OsNn8WYvsknDRueq8ptMZjdNQZBaYtoPYlQFu2la-gASkrzf-thG8ovZ_BRf3UAeGcHeNhUzrh4vYEyHhGuwrY-wa3kXL2R-IVzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdFJgg0yqZi4zm-mpK_WTzTMXXfGMF4ipxToerYU48QhO-NjQlLUQLplL66BsNGQVAhNtKnvyzzR7pEPhGlQy1KSC_C7wjd2An4TjQxTHFbtVqzvFS_r6Argqh9oTaDenQVGs3Ai1pHTaDPXU3oflySZyRTWQ6Z7_PyCGIAw222lq6LZEy8pAj4fn8Z1h1ggcm9XGuSlHPX8Xt-_XUSgBNmDv6bOtOrt40IZTqQEia08HSMQ2SK0jqcEJC3MpwBBLcI1ig9hwOT6cRzG3AdYbTgXhTh03S-cyXBjwBzpVIH-3--aubqvAiXxZcQJZa4iQrPPZU26Rd30ietY3mq3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV8H_Ghz5GMaBATsNX8T_pjOd5qHOsPicLEKw03YjEz7xDBt8Yg915jNpYOqmq0pFxCx2YUfLS2UccE14Dxgpopzpg5MPwo_YK_jlRTcPnQ5d1q9_MxThIRuRryHsKHcIuqWpsD1L_3ewLElXgbfUhYiJWZFvn6gnLLZKGNV5Ipl2KD42yv2reGZCZzjMIA5gNYOGfqqDmM_z0pcgHz6eP5ZjRiEvXAMC9_DnYX44LG4XUZ5bFXxH3G9GDQCHYuf6PCs9tXllngbn35Uh97RYSbAYNzD-qrU3qDhE11vJSw4pwfCVq30xsZcmf9uqj2m59MOaaB6sjEN3HyjjqMn3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J84GV211YwfhjZZA-HmfLw4kaMm67BqIEQUWKpCv7EN-VLsXBFeLpXtebhSDs2tPDSMux8yM5dQruhal2lIODtrZy9qkKg3oKhLrXGRltHTpjFjj2qeHWf0kgeJmet2iCvmb0ys5MeuGsccdS_2KLZ7wAeNHQLt8lRpEEBxhXv0xlCbi--LSpU76EGbLsGLIq7i-moWLTxG99knhH-TPn7omYiU2RWxaJN_HcB9cd9sJD6iqEV-h8vBKEDGQUNSWEO0CFUidKh6xAIC6huYmLnLZ61M1aggEqR1DSMTC7Hzi-NaagjXE_GnQPnkpXrbgn8u13xXJX1ye0lrDStHZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcCrSRiG8bBJiD0hZrE-6h82EI4OeWgrp3aMd2Dgur4jj-YISVPXWxxuB991pdjKg9Lwtt9-ZVaLqkYuHX5--mzHZMTTiaV9fsyBgsRtTSYviSPladzcw-EfB4Z3TIeaNaH--u15Fbc9i0mnvxidTgi6SMw_2UhcblFoeXDKjSXAqP2IfFRyD3Bx2XCM3Jnfv3Kpg1pM-bzsbIEkxwBDmQLN9nUzkzDFBylTZVU1rSYc18HbXk_z7yZl2UaANcl0ugrqwSR4wPA3jrQy67TyJAp5QwlIwtvSNvMggiKH0DsYOsHCrUI99Edw7-Jn1HeuBCDimJSsjHTQaFtZyEV1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ4bQ-RFy2TcHGpFiwS11_C0Xo4ITut4YDzNQhx85_V5DQLV2IGL2FdfjYH3zAUH8MAnvbb_Di8EFlGX1PZdZWOw_EfvPCiWZ0vP0eis7Vltss2MxgmrPk3rSs7qENCBpwBbgRn4H4lw3l3zc1XxN8dlT72NDMACziI_0MmE5RWyjw_F_evN5WbN3Y4D1ab_eeZvttGJbJyy7kGcfEYCOu1VxdIICnqID8v5x7ChJNsIjR0tAQ7eClwgD2f1-5c9Lxw25y_T6_3fYYGa_4VtcAeqE2Dclut31JhiiMyciCdP8-APSFaAcByqNOIaK-VHbmktOKdwJgC6g916UimCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV0_ZSgoj1LLPDeKBQ3T8TQCWU5qfTpU_AMflFTMVXHBgQLbW3qbSDc7_0zqvnYBL8ItjN7LbRKnBOSGykF8-Y11xTh6nebRgIVWJXo7HMYK7SKY6SXT4EeWkb_z8j5DWsRPazvokpN85eK_7-yjHc2IMigYpZMuWm5JJnuHpsjXuqAp5gx6k2mlRxiEkmMMS9Be25eD7IUHeXM07fBxWkacTqv_kKV0iDGv_TI-7ACVA4PKZIciqRV64PtmsPPxJoO0cMQoTpueAfy79Q6hJKeZHmcS8G1JPv0yQOCedb3XaOkVWE2Im8mupvlH8PoKCzHtsUc7Tp2-WcxkV9NqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
