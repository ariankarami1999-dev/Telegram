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
<img src="https://cdn4.telesco.pe/file/QkUjTdJfmXPmj6B_5Z2mrS2vN_ig31IMWS4xzimbWD4o7BmzEKtfVCgiaSyMHRTmDUuB3Wu0zWJ2evNNkjsMs-LyVrlkqQxjvdBtmbp5dp5oCR1DMP_vuTRaSMmZ5nvZLl709kIlVcRyktfeSW0sWDKGO0ViR9U-PX178EjrWV6Qn6ru1KdvUb0yTCVae2l9Pl-0dCVrgXBuMvwNz4jpcNV643dqRd0GaNdd3FiLEeQ9aBn-vHJBYXI1WCFpd6g2dbtqbw27krCh3WNm0QH2YrQFlEbKSEXpARNPoi5m8Hkgb37WDWG9Xw6unqENEPe4GLiluRgpm1OAZiOfLn13Yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/funhiphop/83967" target="_blank">📅 18:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=qWS8Id2905AqN-crspFgdXd2Km63Cx3bd7CqOPBaAPf9ygsycVuxYGwDsA3jTax84e4tmPozvgMTJUS_OEFRsw5RFPJDzRluHw2xt-iFik0uV4i4Qxjm63uWsb93dxLpidxGrovhbpmz4HKnPzFKba4cv-aUz51mY24312ghCb8Sb3HL3eFX-AueRAbLST4gqb176hkeM6rdMAFsHkzeXUh_2OxWzdAVjOrhzyb1mpJ8_zAJm_HfosGw2IU9tIBcVy1sMrmtZ08zlqxhEq_fUl5Tau_Fp60gwwE9PIqDEDSkrBH4v1FvW1dZLM9E5qtq-FLeAWXQRPpdTWPpXJbURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=qWS8Id2905AqN-crspFgdXd2Km63Cx3bd7CqOPBaAPf9ygsycVuxYGwDsA3jTax84e4tmPozvgMTJUS_OEFRsw5RFPJDzRluHw2xt-iFik0uV4i4Qxjm63uWsb93dxLpidxGrovhbpmz4HKnPzFKba4cv-aUz51mY24312ghCb8Sb3HL3eFX-AueRAbLST4gqb176hkeM6rdMAFsHkzeXUh_2OxWzdAVjOrhzyb1mpJ8_zAJm_HfosGw2IU9tIBcVy1sMrmtZ08zlqxhEq_fUl5Tau_Fp60gwwE9PIqDEDSkrBH4v1FvW1dZLM9E5qtq-FLeAWXQRPpdTWPpXJbURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت آمریکایی در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخنرانی می‌کرد، سالن را ترک کرد.
این درحالی است که نماینده ایران زمان سخنرانی ترامپ محل را ترک نکرده بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/funhiphop/83966" target="_blank">📅 18:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQlowjNrAj9ghhEjRRohHZo7X0IzpC3yULyJy6X-6R2cZkhKazlerJ9u2lD23z_t6vucKAcMlOT8CZ8f9xkbZThCIZyjuAKrnP3ws5_W2E45RoTxFKcqeOAc5KSPYdAuN6a2dBwPehBX-NMzphGKscdmOOOOm_3JSDQV5R-7CP121PKF9JgaYbGNxU4BX-8Ww85OLKamfcU3Y2i2hduzpDIwgZ4X_IDNKpnyW8dXtdvgI-EFfUQ8BqG7I7UgzaYEpuq5ChhvSRL5CLrgA13AgJiV8TH8xn8QVibtruNhOj_UHsMs2bE2dRTEJepXNzBF1_dGU3xpgyPr7mDzpaC5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/83965" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOQCUqxlBItLEcGLQMqj0B4aoAujkKDur51p36Qoc29Tz4MpwyWNzb0PgNCEoUH40TtNvkznTOVs2yfJDgbKf4TevaBNurD45v4LKDYrO7kELtujIm_7sUc9EGom60YSY1zXNVAQNAWmCENuXdCvVlQ43aPswUdcvPJeONAHyj1E00LMxlDs2gM81trzkO825TnFRzDYjfvM6rJspUaFqWzh607xG5Tx3DHNkR3pxg1bx8E0A3AubYJDrg2h2K9S8KWi72G_OJSl63iWUtfFDV5DMVSPd5J-Vwp8hdIXnXOI3LXeYhe5tIRX5bZz2rLrvGpFI2yIO1ibRvjZ5ceH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار کوروش از فناش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/83964" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تو سراوان باز بین نیروی های نظامی و افراد مسلح ناشناس درگیری شروع شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/83963" target="_blank">📅 16:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🕸🕷</strong></div>
<div class="tg-text">اقا تر بزنه ابرو ی مملکت میره</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83962" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwNncMb0fHRNhbAQFPyhmTaY_9MoqviAqM_-z474fA2Kcf4EJFNWuFU7t69knTwSvHeEaAsU78LZp1xefF3AFdCLWg5C5ALjQdz-RCMTOiMf5uvRJipFYB__S0lCn7-nBepsB5sMe4WhxqTGEDws5fPgSaXFbbG9rqDAgGT3O-8dy6TYubXw8Hgt1OoFuH_FJyhoOPo88SLwSEByeDgJpVMNRYFH1pPhs31tmbKcn3pqIbnCQ8er-vlZvTI67IMILVgCxKcHMVZVWs8wfHQmF1VmxuOeM2QkIkKJwMUMk8TG26dN-nGKnMaRMQxM7lPj7uq8E56MLn1LAVNUsWr2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بترکونی رئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83961" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کوروش وانتونز:
به زودی یه برنامه یوتیوبی میزنم که هیچکس دیگه نخواد چنل پوتک رو دنبال کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83960" target="_blank">📅 14:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">استاد خوش چشم تحلیلگر ارشد صداسیما: کیری قوی ایم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83959" target="_blank">📅 13:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شرکت کننده های عشق ابدی قشنگ ۲۰۰.۳۰۰ سال وسطن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83958" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJhu6J3jHDBCmyMueSNJKbEvQoEAMQE8xa_CXAOegg19AKG0JRbcBVSmqN-_w0X5p7rKqfNWvDs7LqllNYeKuvGBISUHm0x1PQA8Lx5D9j_DZsJDMcQRHQbL-H07TLkUGwBn4__Ji_di2fEpldbWKYY1-sb3U8MtziNWRu23_QNnOaUtlGOgVia-D44AeMv0s5dsSXwXEHHJ62d2e-0Fxu9y0WGsYQaS5gjXLudq2Tp2P_cUAKjSe8DVfqUXp5lj3wLgO6GrjYodMfNELhaLOA3ITcmBAAsl7Q-8R-cVCgP5YySavplHva7w6YUkjje-vBXA5vYTInX5mfXawHq-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالتی هستیم که تورم به ۱۵۰ درصد رسیده، محاصره شدیم و هیچی وارد و خارج نمیشه و داریم بگا میریم، به دلیل بگا رفتن پالایشگاه ها و پتروشیمی ها و کارخونه های فولاد بعضی اجناس تولید داخلی حتی ده برابر شده، تو پمپ بنزین ها باید دوساعت صف وایسیم که ۲۰ لیتر بنزنین بدن بهمون
و تو این شرایط دغدغه‌های ذهنی ویدا سادات:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83955" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7M-qXze2kDPIu728Pca7Q8NWCq5VqdY587arh6uMVIZ93Qn4ZfUeQmKDeL3qautYq3dY8fIgqlcF_dlACeuXi0Z4iFzBdvoFSnixRAJQmOJO1CaA6l_N-gzZ9x-almwOqCprNEu9QKjzmsLhco8TO3gvVsCkpUEbQCbQi4vyy9OZVcYTdZGRpy6EiPcNFfxd940tim3kdgQ255_F3DCkOm9VZVIL05DSZLhwh_7IzR1BRb8f5kNOwk108vT5W76z7xlVTUwCLV_BFb5spgr35elOwgDQvxNqeiJbQkx-LJPlbPY4abukYZ4NGKCwrXGPJbdVVYkSLNC3JB1AgNvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - اسلوونی
⏰
ساعت ۱۷:۳۰
🌎
📲
ایتالیا - فنلاند
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R1
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83954" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPvv9_aH2D9QCYgYErGO-xyZludoaysL39HLMZGT_yuiq6udIr6BW270OEyYEI0IrxoxasDBZ8UCmmSyWVeuBgLzxY4P4AmvvVPdEUUGaIzx2NIUy66gevzic8XEwFmYJ1EN1HY2CtgIa1qtnhMgKOfpkWWZIU8X2l3JEVnfJstWXXo9c_4NEjSEXUvnCwNQYSLTfR--sfIsIqwKtc2zsGd3szoiiqszVpuuzQ9YaNWoey3VEb_z4kPpoDhzvPSfY6O8OIn6TjmtAnEmmxV-4med0r_vL1dDAod3UnHlKfs_EWJ9PitBpktnTmigYrbL4PqWoBv1sLMdbNjcxTmS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان بیژن بودا، از خلبانان نیروی هوایی شاهنشاهی ایران و از اعضای خانواده نیروی هوایی، درگذشت
او سابقه پرواز با دو جنگنده F-4 Phantom II و F-14 Tomcat را در کارنامه خود داشت و از خلبانان باتجربه این دو جنگنده به شمار می‌رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83953" target="_blank">📅 09:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اونی که امروز نمیره عقل نداره، بچه زرنگ امروز میره با معلما رفیق میشه از شنبه دیگه نمیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83952" target="_blank">📅 09:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مدرسه چطوره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83951" target="_blank">📅 08:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7rpJqd_2VdiV1TGl7ZeqFBoCbShFSPKBygllcIncvHVqbxqEBwCfoPM9gsARY6Afa2qgI-5SdkpSEaFwFjy4oohCHkghPtY1NhJBRmF4U7c5nlvf7rWhR6Fy4a2rvFpud-DLEcZ7cM__vK9wmcq1dKyTkv6mlKTMyFnITvCBs1MPQ_0PLiwuQ2SR08FttdwlDujXxWA57aImrDWz6-opHQfASHKbH6qA5PUQxjCpzBa2Vb2lF7bx6IqwTNMeh5GRScgEWb2eWN3JFjB1a1w3bvFlaQuYqNushH5Pp4NIi1n04RKSEckmCNWIcmgFuJIYc6sWjlAud4iltbPjXu-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نیویورک بگید مسعود اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83950" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آخجون ویلسون دوباره مست کرده</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83949" target="_blank">📅 01:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر پسر عموی مهدی چیکارا میکنه سپاه یه موشک ول داد سمت یه کشتی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83948" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044b34344.mp4?token=uLHXPNb691m8cjxivOJ_C5V5RyIwm1B6iJ-EPmRoZGnFyLi_YAx4qpJh4YFHxLlKAASbXUEV0HxqqY6kD9OB6VnNZ56apKGVGZ2aW2vmsxiOPzXV8Ud4tul5QCjoNhRV2pVFRtPh0OcKP47iVWuE6AcheP66eFMx7BJOLqs6irrvFGtCijfWPDGg7WPpuUnD-2RlPoc6CnAfdcMxBRnoKdS2mwbu-V9yrks2ilm-7VjbFoo5UBDexCvfrHsluVw-CnKuSTPNPOR0lRUF8jAo3VVir4ymhfWZ8J8Q_YmBBkn3LzHmpm5JuRWpX6fdwJhNWoRFgW6lJ-R6FOBvHO_9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044b34344.mp4?token=uLHXPNb691m8cjxivOJ_C5V5RyIwm1B6iJ-EPmRoZGnFyLi_YAx4qpJh4YFHxLlKAASbXUEV0HxqqY6kD9OB6VnNZ56apKGVGZ2aW2vmsxiOPzXV8Ud4tul5QCjoNhRV2pVFRtPh0OcKP47iVWuE6AcheP66eFMx7BJOLqs6irrvFGtCijfWPDGg7WPpuUnD-2RlPoc6CnAfdcMxBRnoKdS2mwbu-V9yrks2ilm-7VjbFoo5UBDexCvfrHsluVw-CnKuSTPNPOR0lRUF8jAo3VVir4ymhfWZ8J8Q_YmBBkn3LzHmpm5JuRWpX6fdwJhNWoRFgW6lJ-R6FOBvHO_9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یعنی کیرم تو این زندگی ای که من میکنم
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83947" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ناموسا بعد از بیف وانتونز با پوتک هروقت چنل کوروشو باز میکنم یه کصشری به پوتک انداخته، بس کن کولی خسته شدیم</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83946" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvSAKb5arB9HY5L4k4uWlQxtXPUQa3GlTCkcc7PyXoLLkXKX1ybnOwHW7pZVNGOmZYkbpxI4lWYzIJclHnTbHn9IzcGmB0WgSSalkQ7Bp3qWAIeWSJGvU0ZXQBl4A2aSNzrMpNQjGwAufbRwoSdSptHxY7KLuArHBDeZFKXhU93Dq9Ygm15-IJc3P2MsklAkUqXwNI-zrmrG5kzJyHvwBHdvw_Eaxb34pBI6i_3WTgIuR1JlS5JanAC2pr5rgEsOyGADcs1KgjwtRsaTp10EQRBOZIfX9F7Qa8hw0fr0xtcKGQwa7kHtgUX5uvCxITFikTZgIvoFDmdrFe0hfeIVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKoEpqwNw0MWu1-gSoyW3pwy9-aEiZENopWnhPfxRTM-GsvbWx02tif47Pj9kFv-Cb6EGLEt2VMMVX7knBmtAGYCx1ejwFQR_JYwXe2sGZvE55QGv9hVpZPeBmreJE4WJpEaxAnaiuwlPS5sux_XHeZa-OMbqoLegRVYRpnwK_wI4lj1GDTJwqMP2LBEIR63yEp4IOFGaPgzq31zDFc7NLEB098ehFBWjXv-hHDQk0qfdlAeENj-PwzCg71Jn0ST7QKxrZnP5J0qwiqdPyyj7Po13wuIKQnyqLMSPWFExfyyQFaQBWWYS_7cDIbWmX-vv3WT8awmu1ozWiSyWNRCfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پول دونیته ها حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83944" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=Y4Onx3d-2-L8RQ13xh2JhOLKjYUgVwx1jq82pBANn5lY2Y36NdQ0H5HjOU242Nj4Jf7_8FR1bR4qjVxc9Y5GnvpKK5VfYb_VbPzmVPQ9rwTKuH8mp-0ht7Xzqyb7wIWKOI6FP-WcjIipsyhPgMkldo-9yKuE3zgPMX0XZmuVhJvZmeZ8a51ZT-xwAu5eGRN5tMcpfv2ysDSJP3tifyuaf8AgiVH0pvck11RCKoJsEgxiF5LxrU0Z929NVU-cmjaoMpg-As2UcFhVzuZfQOwmPHP_fWYAP9xhaYqorrzpUAP-2dEUBi1r4_WX6re3G-tzrfUEvVrUqdkKF2r3pUhNsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=Y4Onx3d-2-L8RQ13xh2JhOLKjYUgVwx1jq82pBANn5lY2Y36NdQ0H5HjOU242Nj4Jf7_8FR1bR4qjVxc9Y5GnvpKK5VfYb_VbPzmVPQ9rwTKuH8mp-0ht7Xzqyb7wIWKOI6FP-WcjIipsyhPgMkldo-9yKuE3zgPMX0XZmuVhJvZmeZ8a51ZT-xwAu5eGRN5tMcpfv2ysDSJP3tifyuaf8AgiVH0pvck11RCKoJsEgxiF5LxrU0Z929NVU-cmjaoMpg-As2UcFhVzuZfQOwmPHP_fWYAP9xhaYqorrzpUAP-2dEUBi1r4_WX6re3G-tzrfUEvVrUqdkKF2r3pUhNsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکارو یادشونه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83943" target="_blank">📅 23:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRapBadVpn - فیلترشکن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_9Wdf6ijNgU9m9oxWK-0OhPyyXtyXkBcIw77NFD3sf9z6hd7ZGo_AojFu7Ns_5MA53JCql3k3HKAwZ__fQIGBBZEn2H-r1CjA0mcadbUEP4uJcLvwfGycb3GIw2mrrN62YeRC2s5ezgBoOS8uU4iEjnTo-pg9zJlVcpyC6Zks7VMZai9E-0Zi60Y_BLQJPb-z25NI01lEgosM0QgDZfjhFnnE-Y_zzBSlr8_JS1WCXCM9PFdXmWL8cDPlVdXmNjRobS63I2KRafCWR6yM3mkx5jOrXxuI-Rd4sPB-WLGlVeq4sf6lwZ9krsAEL9QPesFn4z0pUKu-MZIbnegqzQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
وصل شدن آسونه؛ خوب وصل موندن مهمه!
اگه از قطعی‌های پشت‌سرهم، سرعت پایین و عوض کردن مداوم VPN خسته شدی،
RapBaad VPN
رو امتحان کن.
🌍
سرورهای متنوع جهانی
🚀
اتصال سریع و پایدار
🔒
امنیت بالا
📡
پینگ پایین
💻
پشتیبانی 24/7
🔥
بسته‌ها از
۴ تا ۱۰۰ گیگ
💵
هر گیگ فقط زیر
۴,۰۰۰ تومان
و مهم‌تر از همه؟
لازم نیست به تعریف ما اعتماد کنی
😏
اول تست رایگان بگیر، کیفیتشو ببین، بعد خرید کن.
👇
ورود و دریافت تست از لینک زیر
🔺
@RAPBAADVPN_BOT - Test
🔺
@RAPBAADVPN_BOT - Test</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83941" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83939" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83938" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83937" target="_blank">📅 21:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8382999db1.mp4?token=MQvfK4cb2f_dn2pG9fED0aygx9RqlfhofB09ZD41oK2jRqskm_qSMxLZ5JQqHx4y89EPYFsT7VFvxyuNy5Bb8XeukNFSLeXhqZ-ii72wXYlcUL7Yk9qidh7X8gw5r0v-KVAiMfvis-PKhluVjq_7zB3G7Q14oHFGuL0tVICAN7xkZ9deZAKI-gRUucdAR5g9H6ETkU3MpV8aUAfLxiR0ZLcmFHZRDxsOOK1FGcgHHIKNrG1w2GtrdMkUox0fq2awxlWKEq9PiTWaqe2ymOCg2B33r2n9lDSgrWqi-qUBvMLEhTP9a4bQaVN-GJm3h9b6-oIwaXT7SofDx1a2_P0bdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8382999db1.mp4?token=MQvfK4cb2f_dn2pG9fED0aygx9RqlfhofB09ZD41oK2jRqskm_qSMxLZ5JQqHx4y89EPYFsT7VFvxyuNy5Bb8XeukNFSLeXhqZ-ii72wXYlcUL7Yk9qidh7X8gw5r0v-KVAiMfvis-PKhluVjq_7zB3G7Q14oHFGuL0tVICAN7xkZ9deZAKI-gRUucdAR5g9H6ETkU3MpV8aUAfLxiR0ZLcmFHZRDxsOOK1FGcgHHIKNrG1w2GtrdMkUox0fq2awxlWKEq9PiTWaqe2ymOCg2B33r2n9lDSgrWqi-qUBvMLEhTP9a4bQaVN-GJm3h9b6-oIwaXT7SofDx1a2_P0bdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو سرحال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83936" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستان تروخدا شوخیاتون با باز شدن مدرسه رو تموم کنید، اینا انقد تعطیل بودن الان از خداشونه مدرسه باز بشه چند روز برن مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83935" target="_blank">📅 19:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سالی یه بار یه خبر میاد که یه زندانی حکمش اعدام بوده بعد از چند سال عفو خورده و آزاد شده، بعد از آزادی از ذوقش سکته کرده مرده، نمیدونم چرا این خبر هر سال داره تکرار میشه، بس.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83934" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کی فکرشو میکرد یه روزی نتانیاهو، پزشکیان، ترامپ و رضاپهلوی همزمان تو نیویورک باشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83933" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=kEmsPUNYsPvxMrAhJYfw5JZhtk6T4PB12Oik3gO9B-V553Aaw6Sxm_Y3ChgVSM5LO5lJlsKQfNvE8aioSCZDG0irRJiHva9bMqLEi5kJb2o3Z1RCSXrvMTtQp9xHbriXGYvylONTVj0RfOQ3vvVCBPdZwmcO6OEXouW7U7yXWJfwoOvWbKO30BAffWh84gaMD8ekYnty2EQ5WSV9yEr4NS9WCbsgUSuSX6wZuL0WPNSdnHdPf462xY8NqzpH06MyX8fveTypziz6FD0I9oM4nSaAwROmj0ti5iGQko813f0fF1t8ZZd3mX_LrzdxOHb-acZGnpfLs_tXpa1Q-mYDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=kEmsPUNYsPvxMrAhJYfw5JZhtk6T4PB12Oik3gO9B-V553Aaw6Sxm_Y3ChgVSM5LO5lJlsKQfNvE8aioSCZDG0irRJiHva9bMqLEi5kJb2o3Z1RCSXrvMTtQp9xHbriXGYvylONTVj0RfOQ3vvVCBPdZwmcO6OEXouW7U7yXWJfwoOvWbKO30BAffWh84gaMD8ekYnty2EQ5WSV9yEr4NS9WCbsgUSuSX6wZuL0WPNSdnHdPf462xY8NqzpH06MyX8fveTypziz6FD0I9oM4nSaAwROmj0ti5iGQko813f0fF1t8ZZd3mX_LrzdxOHb-acZGnpfLs_tXpa1Q-mYDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برا کی ویدیو میگیری مشتی فنای تو ماماناشون گوشی‌شون رو هفته پیش گرفتن ازشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83932" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83931" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=A9cGLBEIzHYnq7C4nI1LqfaLuQpd2cJ71lFPTF8lLOTQ1wadRKcOKjuwKGoMHV_wF175sevnBOzywQQLYlPWOrUYNpLVXMhV_SxgQdxwVVhF2k_gp10E0AD1-QrCtt_zzMafIjDoZnYAFUXh9unNlE-JqT6Un0cDx-Ccgo2kS6aQSmVG2w_ctzN0mJuUx-rZEAUEdZ-4uZSrP2AXoodxNOISMnX6fHZZTtDstzQ5nQw0yalIz45c7n525uq6zMcbzXKxyxVAHRZzJQRgYD0qARvdR1HR_NOexOL8VbiEzTkJ9RgSRWV3jkFpdHfaWqfHs4qF3e_KHIF_uJbm013w-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=A9cGLBEIzHYnq7C4nI1LqfaLuQpd2cJ71lFPTF8lLOTQ1wadRKcOKjuwKGoMHV_wF175sevnBOzywQQLYlPWOrUYNpLVXMhV_SxgQdxwVVhF2k_gp10E0AD1-QrCtt_zzMafIjDoZnYAFUXh9unNlE-JqT6Un0cDx-Ccgo2kS6aQSmVG2w_ctzN0mJuUx-rZEAUEdZ-4uZSrP2AXoodxNOISMnX6fHZZTtDstzQ5nQw0yalIz45c7n525uq6zMcbzXKxyxVAHRZzJQRgYD0qARvdR1HR_NOexOL8VbiEzTkJ9RgSRWV3jkFpdHfaWqfHs4qF3e_KHIF_uJbm013w-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g31
🅰
📎
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83930" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه سوالی که هرچند وقت یبار میاد تو ذهنم اینه که کوتینیو چطوری دلش اومد هفتمی و هشتمی رو بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83929" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d48Yn9k4FnF1q8Okwx2dQ3z5kkRdMer3Dhe5qrbbIDD5P_3dgMNFAbZ4sO99pKJ0FUo-Mn7dS5p2ZhhI78Jm9INUxBVI1rMB6hltsQ2IBDSSrDa71apejASgNewjwu0TKYTm1gPA4BM5dayvJfqay0Aob_b0yHb4P4lcviGTVJ-g7iWTX4UzwoTyFS9anICxQJJNMPXTJBlBFDnxYqWvcstVLBXhbeV4jrKNaKDTiuPTcVJVZoHcuhdil6LCgsbDhFYqCErnwLdXNiw2BrjUEExeSzYwzc5kQAXgJnDQlwELx_o-5EvWXcpHTiQBnNF4OXReR9S7u3vGFUpYguz2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین خاطره ای که از جوونیت یادمه با حسین خاک تو ماشین بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83928" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83927" target="_blank">📅 15:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huGoUI0FlYb7dKiKvqgFjom-YZj-Bkwy7V6ebDTJT2MjPRIipR-mgSg5jWFR1zk-QHZfSqahCFV4uS7svzdokr2JAMn_hu_LEuFrXjnWuYP0uDYCoMvP4LlfOcmAyEw_21_I_Xe9vFp9I6tqlKWEfgRNxi8-7R3RQOE_IzTKZjJULnxesHEYKc-sPMO-M-lJjvMYYNQcaZKg6u1ricPXkSmisHQQQlYEJodnHjWYxq3VqMKXjXnb03kfJENPSCBEGiGhii-fPFnZIMDCuqjwaSKV4usZhtd96jjPOCJ8DH2jPR4CcqxJfwIVdC41tR9GP48OpYwedzjlXZo4NPzCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83926" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شهریور ۱۳۵۹؛ روز آغاز تجاوز عراق به ایران
ساعت ۱۳:۳۰ روز ۳۱ شهریور ۱۳۵۹، عراق با حمله گسترده هوایی و زمینی، تجاوز به خاک ایران را آغاز کرد. ایرانیان در دفاع از سرزمین خود ایستادند تا ایران به دست ارتش متجاوز عراق نیفتد؛ جنگی که پس از نزدیک به هشت سال، با برقراری آتش‌بس در ۲۰ اوت ۱۹۸۸ / ۲۹ مرداد ۱۳۶۷ متوقف شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83925" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بکیرم
ماکه پول نداریم سفر داخلیشم با هواپیما بریم
🤣</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83924" target="_blank">📅 13:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">از فردا محاصره هوایی هم شروع میشه و هیچ هواپیمایی از ایران حق خروج از کشور و هیچ هواپیمایی حق ورود به ایران رو نداره
احتمالا بعد عملی شدن این بزودی محاصره زمینی هم شروع میشه و کلا زندانی میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83923" target="_blank">📅 13:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83921" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسعود رفت نیویورک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83920" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=kSjMcN8kTOt6Swoe-w3naOLtWEUCjB4ebCJ0p3pfb_GlxOB3RNabxNTqbbbAYlvPnlPIWE4YbPNmT6GThqMvawKz9VZ_52ojflrxk-zhpM--tW-xc3GMAyN8KMRiAOPP_Yt18P8_hFV8zFCP6fMscUFo1So1rz1OUIJ5xAVaf491MMwjyR_RdnHdIgZHSo6XBem92ggO7Cawl8QiW1NVi2uHyKMfFICjSkb6eOb49zNpKVniKTmZzSn6zqxhHUz2mBck9elWVaaZAffe2qdxraOaasIg3VdF0pTUUjKc7FiGD63dB1OVI2EkV97Sl2UTxVMl45LuLjNzDluVn9BR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=kSjMcN8kTOt6Swoe-w3naOLtWEUCjB4ebCJ0p3pfb_GlxOB3RNabxNTqbbbAYlvPnlPIWE4YbPNmT6GThqMvawKz9VZ_52ojflrxk-zhpM--tW-xc3GMAyN8KMRiAOPP_Yt18P8_hFV8zFCP6fMscUFo1So1rz1OUIJ5xAVaf491MMwjyR_RdnHdIgZHSo6XBem92ggO7Cawl8QiW1NVi2uHyKMfFICjSkb6eOb49zNpKVniKTmZzSn6zqxhHUz2mBck9elWVaaZAffe2qdxraOaasIg3VdF0pTUUjKc7FiGD63dB1OVI2EkV97Sl2UTxVMl45LuLjNzDluVn9BR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی تو تا الان همچین استعدادی داشتی اون کصشرارو میخوندی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83919" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83918" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWhnHLlPo4iqvdR4df10TLn14DUMUtiLY5RQAq0Swy5rNgYJzpET094NS9CrZ1av9gKgbeooOHMg2k3Ph6m-TGEo9Lgbb-YsGTsWjCNBp-Bkxprb7frmJnsIVPHbkgLyHbFFEWkhjVEtT4mbYfV0Xa4neqRo9EhSGyNahYdri2M0opNhnocfkT2JCE7xaclyeu1SjxKEo-IvOFDtmtXLdyj1Fh2uKnWO5Lv403Mg9r_VhumfHSFVKxdkNQkZKPDWfHjVgi-Z3V-BYrcOS6oDZoz8bVrHWtSAtlS_Yn8UKn23bfE3OCnNna5rKJxmElM-dLRj1FKaTzBjxoiADL3_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - رومانی
⏰
ساعت ۱۶:۳۰
🌎
📲
آلمان - لهستان
😀
ساعت ۱۹:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R31
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83917" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کوروش وانتونز گفت که می‌خواد یه سایت بزنه که توش رپرای مطرح رپفارسی (مثل سروش هیچکس) به صورت ناشناس رای بدن که کی برنده بیف بود تا امثال پوریا پوتک با بات خریدن و جو سازی نتونن خودشون رو برنده بیف جا بزنن.
همچنین در ویس دیگری در ادامه اعلام کرد که زنش او را به خاطر فحاشی‌ها و توهین‌های زشتش در بیف اخیرش با پوریا پوتک سرزنش کرده و به همین دلیل او اکنون یک انسان باادب است که از توهین‌های ناموسی و زشت خود به شدت پشیمان و به طور جِدّ در صدد تکرار نکردن آنهاست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83915" target="_blank">📅 01:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب برگردید بخیر گذشت
صرفا رادارا یه تهدید نشون دادن برا همین جنگنده ها پرواز کردن، بعد فهمیدن خبری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83913" target="_blank">📅 00:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من به شخصه اروپا رو به خویشتن داری و کاهش تنش ها دعوت میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83911" target="_blank">📅 00:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/83909" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/83907" target="_blank">📅 00:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نخست وزیر عراق اعلام کرد همه گروه‌های مسلح عراق سه ماه فرصت دارن که خلع سلاح بشن و اسلحه هاشون رو به دولت تحویل بدن و اگه ندن باهاشون برخورد میشه و مجرم شناخته میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83904" target="_blank">📅 00:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PClR-Lm2bSFHDz_ob_hdRdJB8LnJVi2NEr-ctS6xJ48-Ub2JNH-iJ32NqcUzGQxqykqh_gKB8Sm5JLgro5-nMcqhdcG2RL4n3Sl5ccogyqeXqpJKMWy9oIN_ZnJSvPMdVBhGJEVBkYbJfA17YNrrm29nyIAolgQdvZo_-_QIdOTPMFYZIo5oMQsxpHhYicpJVvW2PcPbN_IDSF2cW0AuhFa2CmsDF7bRMfeFfzapS7B6CEYCg_Ejy3STvCNDY7fvWyPnNopZOOO7IY5tUDubtZgmCr5y6wo9H7qPzBhKhxTe8IUw64f3K0TeCB8fUvg9nMvnvQ1aOOT0z7qJdQpFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح حرفه ای بودن نیرو ها رو میتونید از کلت توی جا خشابی تشخیص بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83903" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUAdW7rnAzQxwrsMki1ZFS7CLJj-b5f6iZnZrd1AhpYuShjBnuGyYpCnkeDSKjciVaCA5aoE0Ug_oUNLSRh2reyUHBygaUAVYcIj5L2WD2Cy7gOPvPfE1QeF0Prr1y75EOWFaRFpCnyFLwtx7z5qc5xQLa07rxeExG8Y9GmSJUOEYob186hGfUodcQclLuOJVeDP_ZB0N-AbFIwpc3GgQvB_gry3fzTPCOfXcV4yigI_L325ljhggWBn4IUVLx_6WySr0BO_29wCuf46RA8dJwQeCsCqHM__uozP_aQF5OojabBy0xB360ktQivXaZeXgouHEugGtdbIGnjUuIW-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف نمیتونم به جیک پاول فحش بدم اونوقت بسنت چنلمونو تحریم میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83902" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=tJUaKyFPVcvkDwm2Yrhm4hVY5MXaVE170Lbpd2qaT9yUFmZZ_tccnCHwAcyB1U_BXJ0nh2FYY3GFci0ia5T_u_N2tD6FgwDf6qQs6rsnTVa4HLbEIo1tlaHpPLm1-g18hsy_N97-avbli2ChlNIySOCIrai7_1jRi78ZWYE3GjyzhYVKJ86TBSagqTzL9Wf3NFVHILZ1B4VEjawkbMrRdqo97FE1STlx9rkWgu2qKNPc335E2_i1TaqbFMB_G156qOKQxm9mL4u0S5nSiFrxDho5XE-ETApl80_f_wY1QiJQONyKplumSALaFtE33aD-ZcuI_zKuDtwxgNzsL6FA0YE2uBZKOx4JAyLbfa2_7nCrWHQh2B7wQtiqiBg9KBqv0VVmggASZuXcdBTTLmo9n2jsv3hTkNPDx0QldgJRgDY7zi3sBNpE1CwtX5O1_xy2GDg6OWhAP5fJjPtoxnzGWrqSxYG8RiApwX40zwUFwj7pSU2KwVVWrGCFmH-kJDnncBiX_A5jmRNl2BMDMlAV5eZynzKYDpyStLffJFMcn7pvBSpNLw5p5lD-AlfejmJtcl9yyCNHmeEb2osnLOcAL0noDALQMBUKz02-zB7RcLLnW5oblKlfG2D-8eqMzunap6hRtABczDI0jG0vhBY0MPMKIVB5swiF1ZV8yiR9jy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=tJUaKyFPVcvkDwm2Yrhm4hVY5MXaVE170Lbpd2qaT9yUFmZZ_tccnCHwAcyB1U_BXJ0nh2FYY3GFci0ia5T_u_N2tD6FgwDf6qQs6rsnTVa4HLbEIo1tlaHpPLm1-g18hsy_N97-avbli2ChlNIySOCIrai7_1jRi78ZWYE3GjyzhYVKJ86TBSagqTzL9Wf3NFVHILZ1B4VEjawkbMrRdqo97FE1STlx9rkWgu2qKNPc335E2_i1TaqbFMB_G156qOKQxm9mL4u0S5nSiFrxDho5XE-ETApl80_f_wY1QiJQONyKplumSALaFtE33aD-ZcuI_zKuDtwxgNzsL6FA0YE2uBZKOx4JAyLbfa2_7nCrWHQh2B7wQtiqiBg9KBqv0VVmggASZuXcdBTTLmo9n2jsv3hTkNPDx0QldgJRgDY7zi3sBNpE1CwtX5O1_xy2GDg6OWhAP5fJjPtoxnzGWrqSxYG8RiApwX40zwUFwj7pSU2KwVVWrGCFmH-kJDnncBiX_A5jmRNl2BMDMlAV5eZynzKYDpyStLffJFMcn7pvBSpNLw5p5lD-AlfejmJtcl9yyCNHmeEb2osnLOcAL0noDALQMBUKz02-zB7RcLLnW5oblKlfG2D-8eqMzunap6hRtABczDI0jG0vhBY0MPMKIVB5swiF1ZV8yiR9jy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار رو به جلو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83901" target="_blank">📅 22:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1RO3UgJiRQsDkm9py3Tiu1dGGpx3TkzLFzhMZHIjzyZ-CjimRORa7DYNS9ty4t9LvCcmAU2Pz7-lZgDbD7BPPZBMmjWifIPsCBr-zpPtnh86mIieJn3vrzX-dEGmn_xu6mQ63WKfAP_kJSZOnKVhR7Fh8y2nXqcJg07mfoFEnowuuOgwUIQmhJCr2KS5wBH4PdBlGEjYt6y8V2aJanF16rCgiz5t-OswNY-UZpCADpWhemmCbrzlTABwyX9IkZO_bKSOIJvJkhRkNdK1PWdpuUdGIhxzDm7LKo_bEwBfI65jDWkYpTXsDkmg3JU5Sbq0zp7LMevmA_x1YLGOHe1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی چیه این؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83900" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: کسایی که میگفتن "۱۲ سال دیگه بخاطر گرمایش جهانی میمیریم" الان میگن "هوش قراره مارو به کشتن بده"، در کل به این کصشرا گوش نکنید، هوش مصنوعی خیلی ام چیز خوبیه و قرار نیست بشریت رو به گا بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83899" target="_blank">📅 21:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83898" target="_blank">📅 19:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=CCojtvAVM7l1SCrWj0motOITDG0Pj1xufDKLOwXv-a-nYDIp8c00IiE22x5JPyoiDcCNPDFDsgOz8Grc91lzcQ6RDdU1vRhIsundA6IEjXZaRM4qle64cLcHIjlZz2lDNnceoeMkAydiaGVGpXmyDgZv9RJ1wAdMRb4QBOk1vqYcjQTUQcyl-ZKHV0oRSXF3rDfBlIxcqp_CB5TVZ7UiFiYf3sae8OTkH1LrxU1YsK2FC990IS60ZioN97lcxzfyeDeGvJhkLBRTg4a1LRMpUDchbA42mAG6oh5WAiIX-NxmVf6dxb0k-wObKob6pvl5ID9Mx1Ut4H2jRFkB-qQSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=CCojtvAVM7l1SCrWj0motOITDG0Pj1xufDKLOwXv-a-nYDIp8c00IiE22x5JPyoiDcCNPDFDsgOz8Grc91lzcQ6RDdU1vRhIsundA6IEjXZaRM4qle64cLcHIjlZz2lDNnceoeMkAydiaGVGpXmyDgZv9RJ1wAdMRb4QBOk1vqYcjQTUQcyl-ZKHV0oRSXF3rDfBlIxcqp_CB5TVZ7UiFiYf3sae8OTkH1LrxU1YsK2FC990IS60ZioN97lcxzfyeDeGvJhkLBRTg4a1LRMpUDchbA42mAG6oh5WAiIX-NxmVf6dxb0k-wObKob6pvl5ID9Mx1Ut4H2jRFkB-qQSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حس میکنم بعد قطع شدن ویدیو کامران و هومن به شاهین نجفی پیشنهاد تریسام دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83897" target="_blank">📅 19:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=ljIdVTtKZuX3mPXhQwGnYgTDQ96RFLbT2hV2KgSG5nq8dnDAnuVhy4h9tWgQ35iL_SCvLP0l9pY0ipfGDNUu7USVySUmv_FkH7GLgrEC_QtHcFsmFPdmam0TZ35gbrJBH7cjGeE6a_jhBhqoP2HeuiwVIK1eJdFQfj3Z5P-TUpSnlN2xcggLvpq8oPE74IedSSFYTjDC48q_ELbX_Frv1L0QrEOQxhFP0TTFW4QU07zJbzouL_-smrXxHmLbxaGt6O1MPxVkTIaDZVaoFXqFbqu8diTYGX7oxYtfWbpZIdXEg2dQi7QZk8dRBDdB6blN11V4SapC-k-lQCRg2Hnfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=ljIdVTtKZuX3mPXhQwGnYgTDQ96RFLbT2hV2KgSG5nq8dnDAnuVhy4h9tWgQ35iL_SCvLP0l9pY0ipfGDNUu7USVySUmv_FkH7GLgrEC_QtHcFsmFPdmam0TZ35gbrJBH7cjGeE6a_jhBhqoP2HeuiwVIK1eJdFQfj3Z5P-TUpSnlN2xcggLvpq8oPE74IedSSFYTjDC48q_ELbX_Frv1L0QrEOQxhFP0TTFW4QU07zJbzouL_-smrXxHmLbxaGt6O1MPxVkTIaDZVaoFXqFbqu8diTYGX7oxYtfWbpZIdXEg2dQi7QZk8dRBDdB6blN11V4SapC-k-lQCRg2Hnfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بین دخترای دبستانی:
میدونید من اسمم رئیس جمهوره؟!
دخترا: ببببلهههه
مسعود: میدونید پدرم کارمند بوده؟!
دخترا: ببببلهههه
مسعود: آفرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83896" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یکبار امتحان کافیست
👆
👾
🙂‍↔️</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83895" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83894">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTyJAXdLtsaQ4wxfNb7E8-rLD9mljAbsEo4Cb9kP2dc5DRlFPWNaVT_qUgObzobK0d8tOZrC5maX1VWkS_Myx2Or7EBTx2kVSa9UeXQWUKMlCEewZcc4wVT9rzJqnM6VTdGrHB3LvBawyXgSqY5RvSmy7csH3ah3Ypdk8bQnCM9honV5zOdzcTgfa2vBHqH5fL2UdsdXmb5bNbvOTvdTWicgaeuVyXK6aMRcggt0teT3X98UMxPSGrpyGeAXp0dx5uJWBIyPS2hSI66fuqRW9F8c7pVZc2oqwq0FCQG4bALjkxuR4DKj2A0XTQEjGyiuAw1Rv6ECZgLyNSzKUx9nnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g30
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83894" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZpUq-VxgkJPA4tXqQOqpStXpzNDo0R7ZQPDWa2-PCBmCAO6hKCobVK6chuz7PohTbB6RqDSf1EOJtx8faTlpyIalXMqZ4CZQYdq1X9w4NKjRaB18bZSexdwsTPjkvTon594COOinBDZOUuTkMaq_ePmRLZK12nmPtRAVjnm8qDPWBJWcCa3Y-tkjuGhuzhQno5xmJI1n8wyl1F_YCFw6r_QtkDCwQmxppMJEPS-px9BcSpLQtCSYP5NTBkESOn0xOhfsa3GEsF7kv0W5iEhj_JV4ILW4QGYM3JGYgV6--id7csHWP7f7VRFAtv5lGNZL0EzU6k29hi60QtyxJzpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83893" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzfYwmAlBzW3mi5XBm_7AZy_c3l_NpxCAjQYrTFFtj23J_JGoFaSSEM-4jj1sYBuOuQoSnuOsKUGNiHI4h-NAYruk8oCYEk6CYlKg8o0GgZpd7-qGDPD20pVWeScgkt3A6K_OmizpqqUG6l_Tsl8xU9dJXdY_NpVUqPPT8ETvpIGAejAGutEJfSq2BgfGNAbR-_ThngSQXyYEOHHhRdEyLgFpJX-jrOuMlaHJc4Jm7X26PmswhfO-ect0TqSNaoz9BUtGPGwcSowwFeaGXvCECSlDiKgMTvHPEyh-p5RNs9Md61_-VQ2SLg0fvDIhroUNAWGtyMRiMfDUmAs0ZtKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=nD4kocpWOKM1QxepNR5JR5NEm-05X20HaiEusNuTMSPGdQi3kvd8Dbnwa4f0rg2xLGw2-WmvcN3531K3Lw5D1KyE0py-UjhXqpiyciw_QD9U4X8u8XsrEs5mRxBXVxxzYZ7QubYjcY9gAhtWB1G6aLFYaF2WDiDCIb9qA79QIXvDerKkaZLAdQnxnTsjm2AT8aVou3-TS2_t7iOoYLiFpnHIx2FzsEbiQGGeMVrZ8AYyTqvABW68uWfQE45E6OEPqXcGSukGdSkpRuMeb7W0as4LspJJshFDOUBDAIoeNZriyVoTxPqzChcDLWsNDC8IWNas1ztX_xaC4dAc0rVwaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=nD4kocpWOKM1QxepNR5JR5NEm-05X20HaiEusNuTMSPGdQi3kvd8Dbnwa4f0rg2xLGw2-WmvcN3531K3Lw5D1KyE0py-UjhXqpiyciw_QD9U4X8u8XsrEs5mRxBXVxxzYZ7QubYjcY9gAhtWB1G6aLFYaF2WDiDCIb9qA79QIXvDerKkaZLAdQnxnTsjm2AT8aVou3-TS2_t7iOoYLiFpnHIx2FzsEbiQGGeMVrZ8AYyTqvABW68uWfQE45E6OEPqXcGSukGdSkpRuMeb7W0as4LspJJshFDOUBDAIoeNZriyVoTxPqzChcDLWsNDC8IWNas1ztX_xaC4dAc0rVwaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشکان کاگان یه ویدیو از حضور ابوطالب و رپ کردنش تو استودیوی کاگان منتشر کرده که به شدت طبیعی به نظر می‌رسه ولی خود ابوطالب اصرار داره که هوش مصنوعیه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83891" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">منابع داخلی میگن مجتبی خامنه‌ای اجازه دیدار پزشکیان با دونالد ترامپ رو صادر نکرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83890" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHALAi9HVqr-RBuusMiZcv8voQs2xAefWacfgGRjj2RKWUkDZ07xYHpb0R_Q8UfQFnNqzO4H4gGiCAkGrcjp8w5k95srIRlPOo-5TXcIEjHWjLtVHXI2XlhzzyTeXJ9YgXIAwI3zI3v3p_IxcIHY3vhRjRZVxHWaD0RgC4r_9KylqddRk8uFG76F7EoZ118Y8b7IE66xp2s_KZ33625sq9RF999VLCBlLVM1_jRsPqF2hI_f5Eb_u8e7oi4CAbQmJwTgdkqobSsvYF1dGDTmNTcQISIvOMl4miKWQP7O1SeMxGOWpQQzXay715mORhLxA8TK4FKox4lrIlsMGwwGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کپشن دیگه‌ای این زیر بنویسم میان منو می‌برن پس سلام
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83889" target="_blank">📅 17:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFuowkIZTdf6CMewIB1c3DCGp0S0Rhvyh4v7mQwKym6R3tZNvfICpfXTPLWOWpqfIsbG1-RRR4drAx4tNmqAsY224yesnPGoLl7mjX3NmlezdcN08xuKnyF1gjDZxbyRXqD0vx3r1n3eewNXIDxjiWxoaaq_4qKpyEc7bf9wQO45F8i1kW-9pLAEuPcB97GYlH3FQm-AmUlcD3FAoiwip0VRXNUqsm-PdEmlRgSrjwA5UqN3g9gkqmJY7soL8MkCVygqZNQD5ZjWO6nOeTrGZ0moYTflrXerOFjbQi76v1HlUHE4ANJ5HFLyL9eNk_1dgLC8bX6OShSSTvGuH1-YLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بازیکن فلیک بود میرفت نیمکت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83888" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO5E6DtFP1ia1pWHcaGh5yTivCfLXsQL3P2N1_5yD-INAxjICNkuz3dUfL_vy0I0v_mg5k2ARze6CYp_HfY34x0Nhd-WnkBKEwQeDHkQ7xlOwSSDmHzDVjMvyfuCayeduOga_B-ZZCemrqKdkCIdHFIxjAm8-ksxDM3u8Y14o5hVn8fFv_3z0ezm0pq9JYT7wE495Uhtq4qzfhnQDzMB_t1Qg5KLyfBiSCbc5v5dRtE9_rIvUcaLlfSfg5YoHGL0J_U0S-HN7bSX6RQjfLJdEqXMZxocTFKu96A76tSNF1xnKdAawQ1ocOQQojnCiCc2S-_hqUcwYXsIrqEI4yTYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83887" target="_blank">📅 16:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=hMYYZMqQG0UyRLjbYangMuecLvFZoP-yG-CV3Yd7AgfRC_nlC-y-f9DGDTJWyonR4BBrUQvjnOgeM1PooSf_JJIRom7162tn7lDyDxisLXeu--BTm5pp_gIYGtvcHyDoWYbxua1vhZw4c0zSpXl0M3KtbjkqXCYvTeNpgsYAPYnYymfaR62CFH34Q01VmfOLkxgy2Gfi8LFpHZifbkSgXyeKXhV2HzYEF7cxLwI_7G-HsYU4JQ-S-oHa4-hqugoBonlrbJvXGz7zq9dplRcbBxucRvD5pWBTdvr0gCqaGKvUP-At2QlRVpjevWLw1k7hGgEEh6GMTA1FPYgEBypSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=hMYYZMqQG0UyRLjbYangMuecLvFZoP-yG-CV3Yd7AgfRC_nlC-y-f9DGDTJWyonR4BBrUQvjnOgeM1PooSf_JJIRom7162tn7lDyDxisLXeu--BTm5pp_gIYGtvcHyDoWYbxua1vhZw4c0zSpXl0M3KtbjkqXCYvTeNpgsYAPYnYymfaR62CFH34Q01VmfOLkxgy2Gfi8LFpHZifbkSgXyeKXhV2HzYEF7cxLwI_7G-HsYU4JQ-S-oHa4-hqugoBonlrbJvXGz7zq9dplRcbBxucRvD5pWBTdvr0gCqaGKvUP-At2QlRVpjevWLw1k7hGgEEh6GMTA1FPYgEBypSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی سطح طنز مرجع تقلید هامون»»»»»»»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83886" target="_blank">📅 15:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آقا کامران یک نسل چهار</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83885" target="_blank">📅 15:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آقا شما بد جلویید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83884" target="_blank">📅 15:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzX-dILP_hihfO9bazm-pekfLI_jZsl9gIRr6ZSmwYWXlYec2MlI1NhXwTsCyvhvsRYPi_45AU0qnAjAfRqXXuOnE9d1H2X6wvzb5xayDMANXFR9UdtuBlry_8O6NbFcUIsx3Z7DjtcrM_JPXoMwazUsRRuDzvHklhczk64ds14cXNscDVyfMI1akDzyDfQQs_kODnZvHYHOK_3gcCpJQ37aavBv2vysREeVXWd4STO_wQAQYNmOfmbtreCi3rKS-9O4xPzUMv0Ftdb1JboHEErA0LXptudI1_MwMVeaPU6HEYPqwPnNqKmPL7jwIez2X6bYEA2V4Yuq2RHkXecDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا شما بد جلویید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83883" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یا یه رفیق دیگش سرطان افتاده بود تو خیابونا تهران میگفت چرسی پیدات کنم زنتو میگام</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83882" target="_blank">📅 14:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83881" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83880" target="_blank">📅 14:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیرانوند گفته چون تتو دارم مشکل اعصاب روان دارم، پس معافم کنید از سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/83879" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خیلی وقت پیش ی پیشگو گفته بود ی یوفو میاد و نیمار رو از زمین بازی میبره، احتمالا همونان فقط تو ترافیک گیر کرده بودن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83878" target="_blank">📅 13:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC1LhFMu5FaSqkg7F80FB5NH_IEcGhtk2GclclxiyOrzm9AuaXlv2VenrWf2Ex-6z-YsmR7AzL7LLQYYI5hJWCHqgvxQiRrPytEm1rYZ7omx-uroulok7KujI7nuSofNA1uWpvY4vqYcNGLnWlZlYyY4LkfglL4IhKurmWAQoNlag5pUyYSeIz31UV_nSngZLeqPhPSkjfkPyQv4peWuXhvPXaonvHxZC1moiUnA4mN1kOZcZ6QzEx8Ts-BunmfVvjIGM6MQXX2rlLeXgvt4IpZhB6jAEGPDJepJSdvI1rMiV4POTPb0b18d_cPnGPfgK_rN4xusbyVhLgxX1I1nwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادرا یوفو رو هم گردن گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/83877" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=jvpWimFlTsOavdGqMiWwPJxnbkKrRnPciN-1bYC8PR7IPi8fDwrZiD9mtd15PRVTb7-8mEIaRuNqTFgQwtOZs_52VsvNr0pppjRZfdYQSdO7dcYCdXiA30KbRC3baWnglnafpUFcd7JXKCOd311NFPt_wRkT7b29-P66185advmF34NQnbjzOfeFy0KGGF6XYjEatAs9dQySSa4ZG1jtvPhmyvp7uBxRUH6WTLkexZqRRgT6whh-23OxLLE8jTNn4xT0YXcV8Pn90KBxs818fIhbxi_nxqPR9aOtdxf82l7UgZccw5-FilnxEP8dPF0nX3gCvrhcPAG6XnEH434Tgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=jvpWimFlTsOavdGqMiWwPJxnbkKrRnPciN-1bYC8PR7IPi8fDwrZiD9mtd15PRVTb7-8mEIaRuNqTFgQwtOZs_52VsvNr0pppjRZfdYQSdO7dcYCdXiA30KbRC3baWnglnafpUFcd7JXKCOd311NFPt_wRkT7b29-P66185advmF34NQnbjzOfeFy0KGGF6XYjEatAs9dQySSa4ZG1jtvPhmyvp7uBxRUH6WTLkexZqRRgT6whh-23OxLLE8jTNn4xT0YXcV8Pn90KBxs818fIhbxi_nxqPR9aOtdxf82l7UgZccw5-FilnxEP8dPF0nX3gCvrhcPAG6XnEH434Tgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83876" target="_blank">📅 12:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83875">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUmfiQ7wkZEOON_jEQ5fCUMLtH-p2ppQMP1bk7Qrv_zpIvzmiG0nXGfep3RmOwAlWQaQ-gJHRVyS6J3aRucdhf-h9YK51VJIo6fkU2Vr_dlRVjii2IqkoWEHIFpKghjN_MkhmJDNCrXVJQIurvTmOvd5HIzyImfPgzWAqRydT1SMIUw-HPwdi9YxaHalTKJQg5Tj2U_qfLP7I-VWnf06u0yU7Z3pyRySPUfoWi2GdcNrAdWAfufEDYm0ZihIscF8q7jTWFWzeb2fBEpz35r2eBGgnfSogB6byw7FV719rO-YLiBxy9X3JbyAMUA71xwo4n6q7jN6iQvKHFI3Oqko6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجوری حساب نیست اگه میخوای علاقتو بهش نشون بدی یه کار دیگه ازش لیک کن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83875" target="_blank">📅 11:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83874">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=qHcP8DUNimcTvRXQN8NCVU_-eKxOldzBOFLZmsM6kMPFr2SyXWOrb1U2Y2ebXUwVtpwLDUB9TdmklJrUkO5kHkI9tvOlV2TmtFXqt9GI_kVO7ZiSvAP4cXwo6gcmUxoWn_eRUnQRZuCTLEZOJxxF6RO1_zPtNcFaNE1lOzScaaQuDGgNEV2SwK1SntMuOLNUV6m9tp97Fp2FnBh_Wt_cbkuOLohVOAF3j2Ywn4KkxKzNZ6wYOPbISssEyQZnmzXp5jTdHKoke1ry2syr7E9ad99wGAIFK0BYxgHod33hwBYZ65_PBljLahRT6Tses9k_MISZ1B7_6g3PBfFzE1lQ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=qHcP8DUNimcTvRXQN8NCVU_-eKxOldzBOFLZmsM6kMPFr2SyXWOrb1U2Y2ebXUwVtpwLDUB9TdmklJrUkO5kHkI9tvOlV2TmtFXqt9GI_kVO7ZiSvAP4cXwo6gcmUxoWn_eRUnQRZuCTLEZOJxxF6RO1_zPtNcFaNE1lOzScaaQuDGgNEV2SwK1SntMuOLNUV6m9tp97Fp2FnBh_Wt_cbkuOLohVOAF3j2Ywn4KkxKzNZ6wYOPbISssEyQZnmzXp5jTdHKoke1ry2syr7E9ad99wGAIFK0BYxgHod33hwBYZ65_PBljLahRT6Tses9k_MISZ1B7_6g3PBfFzE1lQ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83874" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83873">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83873" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83872">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvjs6gYct8PVkd0JFTimt_96qqbemG4Yjswv-4CcXSFef0rB1VOJFNlPMAUrWqubtISTXGeRKrFNciKflu4-koNYrdrUYtH0Bot6728oAnP0oo4uSOFvsFSKhJ_ITQdYqbS8LWz8mCcvnS5Ociqf4duBD0_IlQhpUNjxFcGt7yDdkj9APYCRc8GcrUBhPzJ4o_de99Hfb9FqG5xayB31IeJ-WI2_jeSwKHuSIrjfXzciRI5lxk_6KeHAMnJsdcDa8Hh6RclW_FZ9Zhy4_QTmbvppc8kDn0YINhLCj5vSKvQSESto4E5haXzoS_ZmR60kAVx1zA2sT4T15jvp648CYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - جمهوری چک
⏰
ساعت ۱۷:۳۰
🌎
📲
اسلوونی - صربستان
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R30
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83872" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83871">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf80PpWD_78x5R-JZ_kTfjAdYsES5NOpUhcdiWOUtFRMUSJXq2bN-RLu80H9qOzA9ZCJEIh77sKtFT-jq7yCDwoR82_JPemTEpX30uShfl0W61pRDovenqc2nghQOqv27BjelG8AtiHdNYc3q6NFQJl88B18qA529qFxhQoV8PJEPY4AcIvuJXfYghBMf1DYq914CzwvCLN5Y6QS23_jhrOAPytTequ7xQEHLYxqBnGjx2tTt4C3QgFI_6HqB6vLdo6k-67WVIx692A2AebnMF6RLQ1HQwqzrCDY0dQkQaP5sZh_yGBG-FNudfLPrtWKWMZArw19G9aqiRrYbfgnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممم عجب شب عجیبیه، دیده شده در آسمان تبریز.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/funhiphop/83871" target="_blank">📅 02:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTq_oUDXlXRE7NdhFJgqdzBU5xQK5i3ukbH_liOfHJJm1D9lRxPy7BBB0_dCsMLwbXGO1JTogWHnwUZRFAQZFK7h5zF8mwQAgaR0ibqjMJ-rnsu4ycSBR47YLxfIevCu8gPxBDiqariEpSTxggPn6CxLGd8jZiCfECv4fwPItfH-l1nNOvoLrgInWgvWBwlB8IPe3Ous3VbjO59rfloDjNX1xobtv9JxF8zJijXptbEzWvAfIlL6owGkEZVb1je_VYEnvDiSgFGaj_1hTZ0xYYbxbZt6PwwkVSYiTha1Gb7-TBMccnFMHnQz-A7_JMsDCcnkMrxc4KhtThUQJtARFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/83870" target="_blank">📅 02:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83869" target="_blank">📅 01:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/83867" target="_blank">📅 01:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/83866" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شاید یادتون نیاد ولی خیلی سال پیش ی بنده خدایی با فوتوشاپ ی ویدیو درست کرده بود که از آسمون بادمجون میبارید و تا مدت ها مردم فکر میکردن واقعا تهران بارون بادمجون اومده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/83865" target="_blank">📅 01:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83864" target="_blank">📅 01:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=vehokxLwJh0zLw0zVzforNwTsXdI37oUEqyPjMXHTwx56Gh8HiJq3imMOhJjTKAaNlk_KwGeCv3r7qS9uKnqi7t_dETKdgIobwgprAzTxsxzdxpfkFxtY95bWN5yA0n0glPyj-orutLus863-C04QERj3z1rfWsHU1emvdXG5f0xsN7HS32z1Yqaeo5FNTzDU4C8lF4V4dcs2zV4t7espjXb6mDd8MqE07deT6Da7-zZN9VyADnqnN--vzs53nfHG-m9R4KPWcECxOzBclbXWjv_bjDnSKKVYlK5VmsOenIPHlp9qv6CwB0e47i6WIIjss-YDPUxsYl2bdNvQCEAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=vehokxLwJh0zLw0zVzforNwTsXdI37oUEqyPjMXHTwx56Gh8HiJq3imMOhJjTKAaNlk_KwGeCv3r7qS9uKnqi7t_dETKdgIobwgprAzTxsxzdxpfkFxtY95bWN5yA0n0glPyj-orutLus863-C04QERj3z1rfWsHU1emvdXG5f0xsN7HS32z1Yqaeo5FNTzDU4C8lF4V4dcs2zV4t7espjXb6mDd8MqE07deT6Da7-zZN9VyADnqnN--vzs53nfHG-m9R4KPWcECxOzBclbXWjv_bjDnSKKVYlK5VmsOenIPHlp9qv6CwB0e47i6WIIjss-YDPUxsYl2bdNvQCEAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد  @FuunHipHop | FaRib‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/funhiphop/83863" target="_blank">📅 01:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد
@FuunHipHop
| FaRib‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83862" target="_blank">📅 01:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبیری زنجانی مرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83861" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLlB8owUqcbrLrnML_dnfUdvLaE4Zd7uz_ZkGzo3oilJrtk7WoYH4AIhQ3J83Vnbt_awv56-m-IfxPIhHhhSG5iMbSdNGJpzbXbzHCdzZgsKu_I3Tgx1jC4DcBglniqUvOzKfNi0ZEvmH-Lfw9h8SWlzSpYrGqz-jakvki91vJtEvsQP0cMX2SKXUenvqdXRdqWXLDpTBdc6q67xe7l7GYfsmOvSlqVZInRYnydkMGdOTQOCDZqLQUXn3C2otZBrRxbnQoY8UqTCDRRCcmkozasDwHK19GDeV9rk77JUR9pKYSg9GVMpml62lHA7fx_PqDNz0Gfs4l1_YPkw5-Rwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبیری زنجانی مرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83860" target="_blank">📅 01:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfsQ4y-yQgZJKgC0UAwfpIe0_lNyI4YPJzNN9GzNWc5E4TC-1yTxMt62yBWWvIJ3BTrE08jk5JnhoMUgGM9LYWua4tOpdTaOtUZUCpOMjPDESQceLBhrzsk1DcDaK-OTmhpJtV2RNS3ZhD4iLUURLjLXkVwsBz4VJX6C6wtVH7-YZV4OqecfRm8p6-zvu6KPe4S50a4902q7fgHyC_5JtVlDi3txX5LnxtUVxL1NQR2oSy0TLr9GE7R_hlvsPw_QOyZxU0yZSsg0kW-7NrZ5jCxp3bmKNRhz3XX1r4EkkoiUW8qY0tr3jcJVk_2XsQku-rCkeC2gOm7ozXeHWV9lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3ce3tA2kSkc4QslVm2dBVM_yLRsupGptzFBgeAiY2yZvuY7d2JA5JoFEEyvTZlg-FswLRhmwbI7jFq4OTxmjnZ40ZiXCeyXbd52ouirKiszexvLLhgTRDQDULrxNnAG1OQXqPNEho-4fFo5WFMd7txfJN6g6Ei8kyXbNrHG-GK3qEhZeT0qxhyOsp_JnW9OKji1JzdVBVLPe_ymYoZR0SellcGFLPscbQPmbH_amxkvQ_KWbYpAQqE3zOnM-jsM4lS3xA1YivJTyzdDndZYeRRK5MkYOjFL4h4chs90NNgyZuMHZMjlbs8g1WYbv5ardamIgdNXzeIRbgVTj3Extg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چقدر زود پروژه حکومت لو رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/83858" target="_blank">📅 00:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw_sRscSOgc9AfhkZULPYQwA1DO1yovFLvgfGY_NpURlXX_gFWtDVRKs9hwBnJb3RZltdGcmYOVr3r9zaB8FohVju8TKcgQRn2zpD-8XAsfXnKMwk1b1XEn6CJnmxMJNfJz4r7spGSD_Hy6QXtPPk3eUcXusXcuTz77-3zVDVpAIyqjun5eOApuPVbhVK6yhZZ8o5GyuFIHaiiuFQ15tsh4ZxvYNzsl83zZfT1uwMYZwtPLBfwif0tha2CX7fXENErFdEjOvZt3XTdQL2-DbB5JizOP3Kufj2YzjsbFwbC34awEt-KOVD84jcgoEjFj0zIZKHGuX7FwQaJpYScSuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان امیر تتلو را آزاد کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83857" target="_blank">📅 00:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">همون منبع
کیری
به طرز چشمگیری موثقم گفته که صدا پدافند میاد و جنگنده های جمهوری اسلامی دارن بر فراز تهران گشت میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/83856" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">طبق منبعی
کیری
به طرز چشمگیری موثق بزودی جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/83855" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4rMFEeYfCpfbiCV-1oGhulc6-jtAFmGtXp5k0LM3H2UVPN-FP8EsPdEWHdU5mQpT2vZve3l0uyoJMAjm-TnQTRAEEvLJAHwYzeYIBkmV_R5gZirFYmDyf0BWomMtIOOb6p0VlNbIVYR7gUC0ArXybv01MES8zKZZkVEyrVheZqeozjbHPOi4WrCbIyfz9ssfZQO_kknr7yYKjwLp2zkkMyGmOFxMihN_UgnXy_5IprhJAKcLmbvGzzrwtFSwIhITB2HNFOIL4BWhiheUlaUfRHVT7Yjw8aYeDsidwDpU7mby145qc4jmg2y5PuhCCT78baDpDCUi_GGb7_QYoDRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که براشون سوال شده امیرمحمد بزرگ شه چه شکلی میشه داداششو ببینن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/funhiphop/83854" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به امباپه اعتماد کنید، الان میزنه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83853" target="_blank">📅 19:49 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
