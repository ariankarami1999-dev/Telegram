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
<img src="https://cdn4.telesco.pe/file/Z0TKig1_0FQeIX0S6sF2CfITDVNLwyGcZuc_AdPWU4nEpn459E6T7RLACl8ZKkuKfK_Nreejl2ljTx2wDeTemKRd5Kvt6BDyMQQfTq2Gz_CbkaeEADrafctv41ewt55nBlm53geb4yvpcXNp2VjDifj_4NLf1bQh-ByxDmA4JPaIsW1wp30yqO8vTvdwfUTW62VJixZPmF_qQt-pBlbCwF3-NpLXEm55OMFiIBSUvrI9sNp-x01sAjt-O5-dBv-Vte6a233XZr2Q-jcvJp8MoX--tOZLO9uHOUE5aQExL4rHo1tiWiYWF13ZvzRPnh8liKbWe6mmUS7e6q-q6QtgsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 17:44:26</div>
<hr>

<div class="tg-post" id="msg-82553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=FEUSs3QNjqB91mzyuZqjgalblwjziqqbVZbuNYDZOPOClthMigWkFzuD-9SWkcuu2kXvkOIopyMGYkdLHWlTp0lTArs9V0aEEgoLnfSRvtmR8ovyMgL5KI2NSWYiez0bor0Yl5LRUwHnyY0Fl8vvYdUtxSAl9b9QJyZNckaZBypBZ2IpIYgVB10Pukpu5MzAfjvYwwHM0qUQCEFgrU9REVeCjS-1G7OHf5c2pGpGTBsr79kWb6nm1O9xDjNWglPrL4safMr0hrxG2evxjE06Uy2GILNCadrkNT2GIs_S2iTFA5o-fM8zMK6H4INd-P_HDjWiutfOjrI3uSWB2Rce1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=FEUSs3QNjqB91mzyuZqjgalblwjziqqbVZbuNYDZOPOClthMigWkFzuD-9SWkcuu2kXvkOIopyMGYkdLHWlTp0lTArs9V0aEEgoLnfSRvtmR8ovyMgL5KI2NSWYiez0bor0Yl5LRUwHnyY0Fl8vvYdUtxSAl9b9QJyZNckaZBypBZ2IpIYgVB10Pukpu5MzAfjvYwwHM0qUQCEFgrU9REVeCjS-1G7OHf5c2pGpGTBsr79kWb6nm1O9xDjNWglPrL4safMr0hrxG2evxjE06Uy2GILNCadrkNT2GIs_S2iTFA5o-fM8zMK6H4INd-P_HDjWiutfOjrI3uSWB2Rce1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایع فازشو داره ها قشنگ.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/82553" target="_blank">📅 16:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/82552" target="_blank">📅 16:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc-s40vpnwOhInR1biFpdw9frZxWlHBc9h7teX0rJIp1MPpvJkkhyWmS8WmMj_Zm2fY_-GQi5TRejBVk9-QAx1sroLKVOKoW-lRdsUqTeZCAQ5dzp3Ytjo-kELam3aAqr9kCJ7eC5JWGGSorkCsdrNxzkSCwpQaJv8GJcbdPhRW-5SZ7Il02SlPt7xouDUMMkwUxdFTD2EbayqifWLr7lIoQVqQT7bwIkf1dE880Tksdgys2uWnAiRjYgj7aiixHqJ0j15iQHwNxTdvhh0dzv9rUkQzpUqZjUzJoWQVfNnpBrtWTtJ7CVZwFtTAMP6VbNzx9IBG722exUTvsMplSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورمممم نمی‌شهههههههه
پسر ایران بالاخرههههه برگشتتتتتتتت
🥹
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/82551" target="_blank">📅 16:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=G_xXbCGkqPejh98ToF74KiZcujukbyYXJWWgwpdmylJV2sU1-lMV45ILiC1OTfRi4pzq1xfkLtqPiul0RJeichEF02bmPoHgW6p3-LXipyXjlbqhQiHxRRegUhZDNsOsGqC8JooHy5mSGoKWkCRWSek16_vIKWWLP-Dl5NNMSB4-4RWwu1OeNUPMQkzWe0x1PrMIWqXEy0p2b7jStgXraW2aOyCwLfwq7_8uOuo8kBJ3t-rvPw5Dz63iMg2d5ntKWHPtgXEMHucI-glz-sNtBMqYlCkS3gK6ny8wWwqlpg3zc_M6eBghg_K0r9lcxC4TtzaWzspfKUFyAM5pEEktJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=G_xXbCGkqPejh98ToF74KiZcujukbyYXJWWgwpdmylJV2sU1-lMV45ILiC1OTfRi4pzq1xfkLtqPiul0RJeichEF02bmPoHgW6p3-LXipyXjlbqhQiHxRRegUhZDNsOsGqC8JooHy5mSGoKWkCRWSek16_vIKWWLP-Dl5NNMSB4-4RWwu1OeNUPMQkzWe0x1PrMIWqXEy0p2b7jStgXraW2aOyCwLfwq7_8uOuo8kBJ3t-rvPw5Dz63iMg2d5ntKWHPtgXEMHucI-glz-sNtBMqYlCkS3gK6ny8wWwqlpg3zc_M6eBghg_K0r9lcxC4TtzaWzspfKUFyAM5pEEktJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب این الان یعنی چی؟
😭
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/82550" target="_blank">📅 16:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqbWUL6UcMChlMIjbHZQNGfKyALMt7QffbQH8VJ1i8gn1JElEX4dvg6A_PqXwrbdsFZQZGZ-x9P5Wk4xRWIPYPFU_17SB37ERqO5qKxiTeCu7q4jFWSnnCMiu4SarPXPcpdkLou5GwKamisWqLXjSlXhboW9j0y7kNNbTgHGHky24Jw2TRol_mIJ8XoNoq795EQa7B_PB1xQlQvVYl14ASIwob_GzD4le3gMfXJb-4a3Dch2C0Ay4_nu7BMuNHx4hTS-aVQG3uL1WFYabsfmOySd_sOsBrKeE79hd5f8tKxoApAq3LKDXS-RWrJX0yUSeKsFG3F0PdBHBUfmm-TDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۹  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/82549" target="_blank">📅 15:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5s9LVME8OiYW4teg4EYqPHVCLICf4fLXyqCfaoVq_QXsvH1CTdKLwojXru_RIMRu5riVy74qkKOfztEmtmi_EUp5htcSVCmfVt4O-a7G47Y9IKKfSosHDmCXpihs9KKCCnUCxHV3GJOFCDY75VN0Bi10dzx18RdT3RcMdNRqNkMGS-DN3KFGKvER4b1vGqHmD6hXdiUtPw0UZYmewH0eQJm1BoRERtUCRuRbtLGHYvAolB0b3ProHWyfWol-9Mxv8obymwJCffzda0Q9R9az2blIXaTfP-HKmIpvQ-rQcZgE74y5TEJ6mlPvaqUvdrHs9fsnlj1D-s-FEp8W60fSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی دور جدید مذاکرات؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/82548" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/82547" target="_blank">📅 14:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu2StN_WwLQ51-c22gI5-FBwM7Q4pu7vyaKbihHl56FzyNIaZVqCjJEbegdxO-zBUrzZtQgd-FCKviSSKS2tVezgu-gQ4FakpjdBiTzhAGBTmmRPEYT8xs5MvLrQSKMn_M9FOYRi0sHjjjtWLRMVxEM8G0yE55EqyK31e7WKF8ecyLJ8v_lrtn7bMZNTu_PM_Xeyg8zJuuj9xxIHGt6lFuOEqGU_T7C_us6bgL9nnj3_DaMMRidDL6w9bBm_qbHjv7Kuk5HjMxBdr_Mfz-bKOVrLFZwglbbp2rA-bN1pnN2fj1a8k332mJST_FPBnyBMWBq4IqjH3L_xlGiHrGiK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه از مهدیار لیک شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82546" target="_blank">📅 13:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=VEX8AiT9-xTXdB9tDsBnQR8ktlo4hqy5yE8JBaKI1bim5BithH4ctFTP69ACIS6NCvdVuHbHYrM7AB7_Ssl2EbdusT8wV8S8jpcqq4Sm6eT-MleD9dBGAadix57XaKeIVCXWAMyyDKVjK_mZAsB6eOLRJcoQKqpEQkd2nk09Ve23atWjdj0iTwycJHHxAVWkzDkEekmJGhlKSL7aV0XzR2l0kJmvHETO07B8pfYOJUDBBRvfGM-XOaCpFwOuqdxMw2C4iGoq6Z5NRp-u4uxo6HZ8WdFpU39t3ocTFgWN-Ro4V30w0TPuFgcyL7iHW3SqW22AlI8LJGnSUmvrYbkOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=VEX8AiT9-xTXdB9tDsBnQR8ktlo4hqy5yE8JBaKI1bim5BithH4ctFTP69ACIS6NCvdVuHbHYrM7AB7_Ssl2EbdusT8wV8S8jpcqq4Sm6eT-MleD9dBGAadix57XaKeIVCXWAMyyDKVjK_mZAsB6eOLRJcoQKqpEQkd2nk09Ve23atWjdj0iTwycJHHxAVWkzDkEekmJGhlKSL7aV0XzR2l0kJmvHETO07B8pfYOJUDBBRvfGM-XOaCpFwOuqdxMw2C4iGoq6Z5NRp-u4uxo6HZ8WdFpU39t3ocTFgWN-Ro4V30w0TPuFgcyL7iHW3SqW22AlI8LJGnSUmvrYbkOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82545" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=hevPkGKshjhX90IBSSZ6c_x0j4aA9A_XE7SkL3sYDDxLEQQh67PlI2dH71I0ih9NoP7cSeOXt5XYt1fa_t9t1xubf6Qqqb1hdWMvB89DdhP7t8LPhlGNYmD3fHx3fm4fJgDP_SOsCt6Ebq6BtCfabjw0aUn4rvLD9hrmbed3CZc0XSzi2WRQOEOFi5IRF7L33yWXesGnkKA90SKm4689gvaxw_XKqe8uI3al39aLnBBleNSHc6dDIIbfjpobDWlM0sCE2_11BDIdn55re2jCLyCG29meCfYJYNpNOdaJnRk--PdbJffpsSQ5W5n-vBA9N7u0OUIP6hzTnZGu4eruIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=hevPkGKshjhX90IBSSZ6c_x0j4aA9A_XE7SkL3sYDDxLEQQh67PlI2dH71I0ih9NoP7cSeOXt5XYt1fa_t9t1xubf6Qqqb1hdWMvB89DdhP7t8LPhlGNYmD3fHx3fm4fJgDP_SOsCt6Ebq6BtCfabjw0aUn4rvLD9hrmbed3CZc0XSzi2WRQOEOFi5IRF7L33yWXesGnkKA90SKm4689gvaxw_XKqe8uI3al39aLnBBleNSHc6dDIIbfjpobDWlM0sCE2_11BDIdn55re2jCLyCG29meCfYJYNpNOdaJnRk--PdbJffpsSQ5W5n-vBA9N7u0OUIP6hzTnZGu4eruIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روال عادی ایرانه، الان دو روز دیگه باز همه یادشون میره تا دلار ۲۵۰ تومن، اون موقع باز جعفرزاده میاد یه ادیت میزنه با آهنگا محسن چاووشی و شایع سلبریتی ها هم اونو اد استوری میکنن.
پ‌ن: البته خود این یارو تو ویدیو حرومزاده ایه که دومی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82544" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRQJTWMpnBJZcuVWfTD1fNLsWVnTifBexMQ75gxbE4LIWAcPfTXLfadZ1YXBaQ0RuT0WuqNmEBeNrGisBQ7uVTgLRj4KChgu7SUTUiT7GThWHOfUcjdcQYLirTxGgno3SKW0PIAtz0Zume91UtiEIJVhOOj50RWCeKjwtdaHlw4fEGeFngOI8uQKew5KvFjRrBzBwo7AqIRLEIStHb-jYKmnR4447dRReTwfF1HebdgJs8fn-mD9uf4YXsgmUbBtKm69mzF-tFZ6IH1csO-GCQT2dNqJ4jndYG4JJDZ9G6IHg5_zNKnJMYMafHwLM2sURCyTNiw41L69mNnQMo47cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لالیگا اسپانیا
💯
⚽️
در روزهای سه‌شنبه سوم تا پنج‌شنبه پنجم شهریور ماه، با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لالیگا اسپانیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/LA-100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82543" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzKh-DiA0iroGyAac--Z813DrYSmWKE9uhzBnpxub_WupVa3p0d5MsdTuZIssCEaoUxuhIBrwJ0BLh6BssxeWlM4m5rPXlOA57wVe4wVvSfWbZw-aaHh86ENQRftxpI6XqqbWrWWESLnfTTh0JDV-URtdnolWDo5V4DBLXn2B99BHIq65lH_YMTPqY5Q0D_UQR2i8CQMpDEDJf-mODZZn1mXqx7wwfFAuCan_WtzPO-1LDsCLo-bHkVJNI--CSXPa17N3bsu-pg3FU0YIqHVYFO-_fT0HXRKEvSuJWGqqWscLRxAVA3clzjvi4Ah_tfTnmj-dgdSk7o94EEDOt2d1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری نیویورکر:
دولت ایران به گنگسترهای روسی و مهاجران آفریقایی در کشورهای اروپایی برای ترور، ایجاد ترس و آسیب رساندن به ایرانیان مخالف مقیم خارج پول زیادی می‌دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82542" target="_blank">📅 10:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-_uIiFMSPt56T8Gin2nDyiQNXKpnqSIot7fY3UqAY6tk1PQj26SeSzudNV6lraDkNkCLaW_RW_ltmTx5Sdqvt_soJkbSOtoJqSPHTa6jn4E_WdU3RkEQ_qNvjn24g5xHDtKkOa5HE-77tCX_oXqUUMQvYi7SXBrz9WfCaoGpYf90gtIv8_bUzVMNfH5bpHdID70Dv8fwY8AjRfU6Lzlv2uN7hUsxV0UjfaRK7LIFISnzTpJvYeQtRLu_hbcqBZPnzqR1M4X4egSaHBm5-m6Ie6wXu4Nq-35qWSg8YnYt_90zm05lILdcBha197XYJOp_PclBoralC8SrgPAzCzu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82541" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">همین فرمون پیش بریم مردم تا عید رفتنی ان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82540" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBflW3NWGLtK_STN9ijasSSwjTrfdpBarnsj7mZl9wIflKomXJEf8oH0ov2zUQizGKCqqlbf593PiJgZrfs-dQXMwzzoXdGjrx12TBxurTZ3fNrJevFwbiitE5kYCfr0p4SbQjRgOOYCkl4gcGan_ZBL-U7UnsocZXmi6f7wIHPMx4_--llE2mPh9kNVdZdicx53JJkBzgvzr_gPI4Dj3Mi_KUsPa-8917Cxu-i-a7DO2swrUqXKOGuy4sqE79b3QZHlPs2rOcusM0Fycyf2ihFRt2pikCVWg-YcGn47i7hZSY3IXjlcl64uGEKCH73yQXFCQuvGgcsZg5uAIPxt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکای جنایتکار شیطان صفت هم تا ده میلیون دلار جایزه برای ارائه‌ی اطلاعات از سرداران عزیز سپاه پاسداران انقلاب اسلامی گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82539" target="_blank">📅 23:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عاصم منیر حتی نذاشت حضور پر مهرش تو ایران یه نصف روز بشه و چند دقیقه پیش از این مرز و بوم خروج
(فرار)
کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82537" target="_blank">📅 23:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vedV3aaZVAmiF0CyzAQzJ-VIL22Q05uG9_hLqmvAS5OqxeiFCksAaRxrVPNImo3Y0ZomEgxKmNzQNPDgaJjeAdPm796aSx28pIeWmtl3MBUTR3qKTdQGMAcLMOhqVgAhUU8-nDvYJccp2jD4aeHc90ouUcdHQBJhH_zJrhQlv7DtpNabwGvpAsTSrkrgqwlbL0blOPw4-8WtBhHemJYGctdn9OF2Xan0UVXw_7JQG9qCJjn3gEaCPVVXhobliXeexMB7JC2xQpvNV2T-xDKVZ1_rB5mQNefV26TKUrpoGxAshhYVzV1RqNNgVIZ-E2xUvx4mwJxXiaA1JlL7g8iI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAleIOLU_rbsXbpiOdF0SWlr7P2IEfr6kmr2CrQ-iKOvsTfaMWOWkx_BSfKFpuDnE8qlyf-_LbTjBEScg81c_GgUA9BvBieAUHIaruwSpHPy00MfiZYUigzf4LBtNoo9B2bo3r4Ysr_RuxZaynmBAJZoPyUlt_fzPzsm1gxwc3yfY2SJ9bKwTbvZ84tQqbUfxj3hKlerg6Nvtz2f-cZLfYLBor56erb0ECHl0p5M_e24qp0YHKGuWWv-zHLdiqrSmzHKr3NnLj0eyqg2JR1DjPUfnAUi3vpV1sQRc86BC9PnUuAY6iuTZjBM2EkefcrW_yeSJPG1-UxI8MvT9YB2cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به این بنده خدا واجبی دادن گفتن رنگه مو هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82535" target="_blank">📅 23:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=cLMSP6Q7uf3csTNGrtSPQ2irvOK2jlwXTJUbxilKhGMOzBS3aMjiSxLCTcFWwk_-Nxk70Az0D_47L2I65Vt6PvzmsXU0x9BYwJFgVymV0USrkgQEwQm0uONPLwHErOnGw3_2vXdfR466HG04Xw605Xl3DtQ4Byd1DW_T6cpR53UU7YeQpWo8-LizO3a5eNpspmD9rnTkw-N5ZUQwF4mDWnyIdhyV2kqa1xKQq87R_AuZTRX3PDneJN744BewiUfJqG3uWnrgxwucZJp2gUvBwxECo3Y--XUwVmh8qk_zM90tt-U5gg1Vlj6yrCa79HTTlgcPz-D9RT08DeCe2SQ0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=cLMSP6Q7uf3csTNGrtSPQ2irvOK2jlwXTJUbxilKhGMOzBS3aMjiSxLCTcFWwk_-Nxk70Az0D_47L2I65Vt6PvzmsXU0x9BYwJFgVymV0USrkgQEwQm0uONPLwHErOnGw3_2vXdfR466HG04Xw605Xl3DtQ4Byd1DW_T6cpR53UU7YeQpWo8-LizO3a5eNpspmD9rnTkw-N5ZUQwF4mDWnyIdhyV2kqa1xKQq87R_AuZTRX3PDneJN744BewiUfJqG3uWnrgxwucZJp2gUvBwxECo3Y--XUwVmh8qk_zM90tt-U5gg1Vlj6yrCa79HTTlgcPz-D9RT08DeCe2SQ0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این محتوا مربوط به رپفارسی هست
‼️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82534" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2adb2d63f7.mp4?token=JMwz--xCVJndn5eLaqy-FXbrZt7mO2s9xXrmu5AwBkwypwgFwdL92bjktzf_ZjLdNO5Tp4ARvcLZazFkt7PWU4dzwBqcwUB1E4KV6I9CZ4OtPvvVzad-QmDMSY80X5gqY3oRbZrACasP2uFfNP6v--sqmW8-U8SOmFld-wvG_y1ic1b7asqG5lJCJUqAlUjxEDgj4E9TaJcZvYmF9gtGGHykwVjIhmiwIE4nscGoMG8uez57bpARupl9-kM6HDtyg0S_Sb2QvblzzoSGzqlK8tVNXRk7Rj_ONvSo1hinzvEQEYmbOvJu9vdI_YCw70b1eZh4_p4RRpEJNChGBPYW8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2adb2d63f7.mp4?token=JMwz--xCVJndn5eLaqy-FXbrZt7mO2s9xXrmu5AwBkwypwgFwdL92bjktzf_ZjLdNO5Tp4ARvcLZazFkt7PWU4dzwBqcwUB1E4KV6I9CZ4OtPvvVzad-QmDMSY80X5gqY3oRbZrACasP2uFfNP6v--sqmW8-U8SOmFld-wvG_y1ic1b7asqG5lJCJUqAlUjxEDgj4E9TaJcZvYmF9gtGGHykwVjIhmiwIE4nscGoMG8uez57bpARupl9-kM6HDtyg0S_Sb2QvblzzoSGzqlK8tVNXRk7Rj_ONvSo1hinzvEQEYmbOvJu9vdI_YCw70b1eZh4_p4RRpEJNChGBPYW8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط باید پسوند اپیکور رو اسمت باشه با ۱۵۰۰ دلار فلکس کنی، خیلی پلشتی ایمان جان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82533" target="_blank">📅 22:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mli9_EPRULdfzHna5NxuVNPo4-S1QYktyoVt0WnucimJZn2mN8wvNmOPK7yJH2Dgz5BnJmiKgdogy2RVQNAeseewIA4LtfYkB8dTYoHxwbQLLgU2SCj-f1BgymknS2Z-W6yASa4nIpBaD9iySjKhx_180KucGgpTXvIx31ZfLU9E98sPqracJkoVMiPlc-abRTESJOiHl5bGBU4AV2utOb_Cyhh9WQ427dKzMfOpQqNSQY1xPN7W_LYihn_0sXD_Zlzp08ai4c8TPFrLmjKcjgcN_uuEB7msHhIVUAKAWC1NmUydFdl-nQlbSf0xlErMWWhAC9wfNBEnqD9VH67cNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش چطوری از دهه ۶۰ فیلم گیر اوردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82532" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZdUPcaxD8pkdiQ4w4y28LD_bA7R6dxXBPdAqX3cD2mnO5PokIS-UuR9a9uwZMXqAw7lWSkR1i44VV56zixYdMY9ZtNh_DWr-LrhtI2dxMjAwoUufEXlEjeuDh53Bc7pl7m6somLgOAKSH97UQiHKJRfCW6YRlVwlku00oqqhQkwFCPeIL0GqufeiSLRHX7qUeR_CJJvll1fYnxiPubQEVTXFAbM4Fd9XX2nyxqLs-N_hWDgn5Z01Cvto6NBG69X5gTyc0kKf17H8vURvUIf4xyg90wv0RRxRkJ-FVWPK4kn7WZXHrtPdrLvr9O8PiA6V72vp2zbZjOZL9cgdNcaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82531" target="_blank">📅 21:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0heM8xM-mJia3q5kHJVBXmILWxdqT7fOgu-HaOZTBdjDI2U_kry7hOVml08g2_8uHnQBpHrzE_Kh-6XqZ7gr9SmIToiuFuikv2-_VZGx-8_qAxZKqsZIr-CRNU6B26AXAqDyy6pqqZetYxaSVIQrc3aWIJ3zb7nhpRXQn7AOrUOtx3yNikB-gusJoONdehARdFLjbWzESb5l0AjbxmLU2wo-lsUkciH8xpY9dPiLz0SPwjElrQArT8CIqko4u8DxBrHQmgRn1lLj-AH59fC8AM_u_RlfsD6e4md6Uf_2Bom4jJaimGgo0chj6a178ItPmcPnZSG-34sYbrwu1oecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا به دلار ۲۰۰ هزار تومنی هم واکنش نشون داد و پیشبینی کرد اگه وضع به همین منوال ادامه پیدا کنه، دلار ممکنه به زودی ۳۰۰ هزار تومان رو هم رد کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82530" target="_blank">📅 21:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82529">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تحریم‌های جدید و شدیدی که ترامپ می‌گفت توسط وزیر خزانه‌داری آمریکا به صورت رسمی اعلام و شروع شدن: امروز، وزارت خزانه‌داری ایالات متحده، عملیات "انزوای اقتصادی" را آغاز کرده است، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران. ما یک عملیات اقتصادی گسترده را علیه…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82529" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3789f0e9a7.mp4?token=vKmO3d1Mu6ZPoZTp80gBYSYIwGHBdcNjglAjStwfv86oEPuJHdENoO22jUCLslYVKP9UU7Qm4mMkS0y5x-xGXkD-tExqSwr1CIp0HZBUS4Tw0h5A40dMXOpsBVr6G9YreoJEgcApTQTuEXhH7c_eyoWzhUTVbR-jGeANNWcaOLZeVlwcRPRRPJVWPwnKUSFvpS9skRcFGJDaUFouc1yzqyl6BS8hWAP8PRotPPQQjjDd3yDZBYFdnbgf7R1fWyfbMG9l7Fld-zrHlUIm7UZLJpsgY29sMkYcIyWw-R5_TkrU4QpjM7jFJ-WM-8Xo2kShn685Ew1J8OYFMJWyKilxGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3789f0e9a7.mp4?token=vKmO3d1Mu6ZPoZTp80gBYSYIwGHBdcNjglAjStwfv86oEPuJHdENoO22jUCLslYVKP9UU7Qm4mMkS0y5x-xGXkD-tExqSwr1CIp0HZBUS4Tw0h5A40dMXOpsBVr6G9YreoJEgcApTQTuEXhH7c_eyoWzhUTVbR-jGeANNWcaOLZeVlwcRPRRPJVWPwnKUSFvpS9skRcFGJDaUFouc1yzqyl6BS8hWAP8PRotPPQQjjDd3yDZBYFdnbgf7R1fWyfbMG9l7Fld-zrHlUIm7UZLJpsgY29sMkYcIyWw-R5_TkrU4QpjM7jFJ-WM-8Xo2kShn685Ew1J8OYFMJWyKilxGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحریم‌های جدید و شدیدی که ترامپ می‌گفت توسط وزیر خزانه‌داری آمریکا به صورت رسمی اعلام و شروع شدن:
امروز، وزارت خزانه‌داری ایالات متحده، عملیات "انزوای اقتصادی" را آغاز کرده است، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران.
ما یک عملیات اقتصادی گسترده را علیه ارتباطات مالی ایران در سراسر جهان آغاز می‌کنیم.
هدف ما این است که هرگونه ارتباط اقتصادی را که این رژیم مستبد را حفظ می‌کند، قطع کنیم، تا در نهایت تهران تنها بماند.
از امروز، ما فشار را بیشتر می‌کنیم و هر منبع بالقوه درآمدی را که به تامین مالی سپاه پاسداران انقلاب اسلامی و رژیم ایران کمک می‌کند، مسدود خواهیم کرد.
هر سازمانی که به هر نحوی، فعالیت‌های پولشویی را از طرف ایران تسهیل کند، از سیستم دلاری آمریکا حذف خواهد شد.
دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.
ایران تنها دو مسیر پیش رو دارد: انزوا کامل در سطح جهانی یا ایجاد تغییر و بازگشت کامل به اقتصاد جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82528" target="_blank">📅 20:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قیمت روز گوشی   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82527" target="_blank">📅 20:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82526">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEJrCuh5YJwXMc4jlXNvOZs9-Bq7KdUUunWbn_Upmfdrjmy7UM5ar6AH8HnHnRWdUixgMEVHYMCDeXY6UjkwXa87SJx1Ly-dujRjsreU4-lNoG9pDSMghc506wO0GNzvwg5BE9EAvHqf7rCJkbyiLhb0qX2VSAPImFynOirBhEgrl3mIh4bsgS5CSjl3WoYG-ZZ4d4w4AkaDbw4Ww9b_X9NiR4gSxee9RqYQ-Quw0_J_dcS2Pbo-1UnnUskZjmuhXR2Am-FfikD_OfMRmiymsxmPxM_572ygcvx0TXay4GI4pI4hqoItfY_gteLCI6-rxNofGjmilHQ3N_c6OQrCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت روز گوشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82526" target="_blank">📅 20:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82525">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82525" target="_blank">📅 20:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82524">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b569772aa.mp4?token=Dob-dXpRSl5_NwrOT3uFhYmfoJ6-FsMsd2NceBwa-VgjRU-A_-sr0VqE1fMBjjD9tpgpGWGSUVsF1hsUME1Z6P_5xjAhT7NRI-DVXo98S7VGbQY8YLwOQnLj6k_gzKou7mnJrN2wFx1GdvH31s-wlYL71bMTMHOgLS8ayZ4ftKL6zo80QsQRlInX-QtkqJ5kbs21LVfAEk5KkwC-l_LybUH2u9i4BEYYfkA9E6cj2z3DIHcgU0dOfOUO7vLDAFqAbPZbh2WVFMB-cRD-c7LzfOnLupfgcsLi4Sk9NiYZ4TAtfG1VqONegnA_QpP1MPMg5moSC6LMwYKY-TJlsrBgKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b569772aa.mp4?token=Dob-dXpRSl5_NwrOT3uFhYmfoJ6-FsMsd2NceBwa-VgjRU-A_-sr0VqE1fMBjjD9tpgpGWGSUVsF1hsUME1Z6P_5xjAhT7NRI-DVXo98S7VGbQY8YLwOQnLj6k_gzKou7mnJrN2wFx1GdvH31s-wlYL71bMTMHOgLS8ayZ4ftKL6zo80QsQRlInX-QtkqJ5kbs21LVfAEk5KkwC-l_LybUH2u9i4BEYYfkA9E6cj2z3DIHcgU0dOfOUO7vLDAFqAbPZbh2WVFMB-cRD-c7LzfOnLupfgcsLi4Sk9NiYZ4TAtfG1VqONegnA_QpP1MPMg5moSC6LMwYKY-TJlsrBgKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟
زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82524" target="_blank">📅 19:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82523">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlmGVi4NR37JxiYi-fLk2b6jAaKoqRy388vQFio5sCX1fjituKrFKtpgKwxaNufmuA5wMVH8Od_Fc3RAlA6sdH04PZcO1V9nUQBDtieILLDAXqWW3B1WBffBg7X3uaJQ1rnHdeJmIs-fmE2O4BXfk6ZIMYcN4PL0ZthToixASrVu7S3wPI1D_fxaWzwkPTNQLfSTqTwDcJ0XX3DAzt-6OlSuTdtTCIhCqmJbIQk2AGn_wu_bxt1THH-7uEfcf4fJt3a0Rp7Yyemz3_qXYPra1b9jXWR0_pcTZWOAeCLjcGH_7rCk3MIYg36C2HdruInanDL9HCBvshzEcBgqJw4X1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم قیمت دلار رو می‌بینن، نادر قاضی‌پور از سیاستمدارهای تراز کشور هم چهره‌های جدید اینستاگرام رو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82523" target="_blank">📅 19:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82522">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482bcfbcff.mp4?token=YpHcfBDp302PtUAeq_OOYrASiaCYaMTxbVDj8tjw9mTPerMAECdeaOCH7B5qphS824ato0tRxrOU04tMKzXITvJ0KAZACFsSXU-Tkp7UpubISSl_Cw6OzEMu106WMGy0Tleyish5mm2wBXtChISjCWbeF5ZJQD3Ea1VIdOQ9Cf4gKL1RFhFdccSzyBOJaaGlSQ9hSbpASObF8JY_IY_dNVuA8KVgZJRFZCXJJe9iizTNl1SUhkSFL4KUh59gbn8y-4nZ8J3Yjm8_Och48VFi2s0PJqjxFXGccG8ovFT59UXoVwUuo7nt-XuDpwR_BzaZOMEh_f2cX4hRFkrDX9qSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482bcfbcff.mp4?token=YpHcfBDp302PtUAeq_OOYrASiaCYaMTxbVDj8tjw9mTPerMAECdeaOCH7B5qphS824ato0tRxrOU04tMKzXITvJ0KAZACFsSXU-Tkp7UpubISSl_Cw6OzEMu106WMGy0Tleyish5mm2wBXtChISjCWbeF5ZJQD3Ea1VIdOQ9Cf4gKL1RFhFdccSzyBOJaaGlSQ9hSbpASObF8JY_IY_dNVuA8KVgZJRFZCXJJe9iizTNl1SUhkSFL4KUh59gbn8y-4nZ8J3Yjm8_Och48VFi2s0PJqjxFXGccG8ovFT59UXoVwUuo7nt-XuDpwR_BzaZOMEh_f2cX4hRFkrDX9qSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم قیمت دلار رو می‌بینن، نادر قاضی‌پور از سیاستمدارهای تراز کشور هم چهره‌های جدید اینستاگرام رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82522" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82521">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsiIWsAMm98xKAtJQtyxSkOhZc-Fl_IBI1Mn_MhRgsZhsVCeiPbeVULg1Gox8TLofY1RZmoMRVh5AmYFVmfCrC5tZu8uddPj0hQ-cin0awxdHmhygn1QTR80vaU1F1xr-jfxkwrXE2n9nMqcwQ5R5pxleCvu1z796yMlfyoLIKqTgn0fGtHmhnvhIHb1hce5K2M9ZOybNgTlnVXw7NFpZGvDPT-bCTPFa2ZIw0aKAqcV7IO_CAin4UxNJ-YXd4JGbBFgtQ4FC7dUdZLW-nHvOjm_KGg1NJ6QkZpExJceoDrO9u0tYbWi-6pJ59E-MXrLvHdY6rcRiRno5DVZVqjfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
فولام
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه کریون کاتج
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
فولام
:
۳ برد، ۳ تساوی و ۴ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۴ برد، ۲ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر فولام: ۳.۶ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۲.۳ گل در هر بازی.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما بماند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g2
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82521" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82520">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRJ4pDJU5DwgmI8hrjZBVACPl82LN86rT6isTw7PMq8kBkZM11dLK6RiOYCW7XqFET_7K7OxNOfIDBP4QICxpXtVwl_aLGBQzgVkd86m91sDtch3S6n0UmH1j1v-A9oIfzl68R_ygu5M5O7tDUBuXcdnRi406OPdQr3F59cCwQ8F7SFRvCXAHxCekIuWJCBRR4hWCsr9Jr2BgAIlsS7QRg1R4kocKx_imlOlTlGtOSYYvvTMBfQyqmlWEvnULWttMCNBwoUTybq-YislA9UEGBo1IsY0jtU2WPi6oNjO5QM3UIKFzF2mHpGsLOx70ooOeFM4VYJxvbJLuUrlQP_HNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ تا از پولدار ترین اشخاص دنیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82520" target="_blank">📅 17:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82519">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAK3dL3io4ezNk6V0uqw56fe1MouCJo8HvIoeos0GR4fEkKX0sGP-KL4VR5XgtF2qtjRAw22zhrZul7x81F3W-9mHete95n8jh11eOYt-X6Ntnz9LMu_AjtG1bSnCsbBMBsH24lePa2fRoo7N2twSsNSwSpiiqBGCE54KmwPUgzflLsL3lwqTZDbqifyQ_KXXPft6i0xZaPq7OmH_XEHGfXvRKpRET49xZUht4NywehUPUjaKVOqiMrt7wgD8i6CtABaO19YgFOYFhKycle_zveKbD1_oPWRPaRR-HrUpjNARNgbGyTgdfMQr9C042IgMxJyfUxo88p9lRoHWZ9sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82519" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82518">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این پولای عوارض تنگه هرمز رو کی نقد میکنید تزریق کنید به بازار یهو دلار ۱۰۰ هزار تومن بکشه پایین</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82518" target="_blank">📅 15:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82517">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlUimYsSG520WVYqxAJGVcLqHoeDisgGmj7nzMh0UTIC4IRjz-jzSHVAdwefr1eDEvEgrb8xBMN97GMwrgRvGyLrQa16AWrTwVLhNu7vMM-oAuv1wDWL5mzgAaoQr-1pCkY46KX-2SC3wj5CKXB8PrqIFV6pOalBuuXZ3Rb3mvndK0hlUElwGVq3hkpINpfFHLr8QLKWipyWT0cZXxH98_Mc9ydtLCreBrYM-MQBBoOlZM_luXZpMEe30J3YDftNvgDNtKRbuoxQ107_r9ofbTn7P6kSqShhrbzN7H7BSlH5xABy8kuL23bwEqwUFnd3ZaD-EeqhyWB5-UPfphkH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی حرکت کن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82517" target="_blank">📅 14:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82516">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">برای همینه نمیتونم از خنده بکشمتون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82516" target="_blank">📅 14:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82515">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YddV1Bsi45jg5oA97Pnt2nvP9m109mjAscTIYBJPVg59Hw74agWfx54fPrS-ANA2yYD8uDmDfa2Hwow5Mqrlsq9pWeb4Bs6j594i7SvoLgJDpnGtwLgTyNEQPVnVita4b7RY2laNe7Kj11XqKCMDp0uc_t5RWeYzCYM9u_rRxpkqA7OEfYNNgbifegzfvSZ4jjqSpSwppNsdJAlWrsR5SJSLf4ZOomiWnuQmVUg46JlMQ_wzKjXL0TRGDgaz2iIVDWaIMcRmHmVkINrWPdiazV_bXrGwfKOH3XIw4OHGtAfb3UT56YaO1XJsYfmLOGLYdJOCfJVZou2st2Of6n5xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه نمیتونم از خنده بکشمتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82515" target="_blank">📅 14:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82514">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b--pSU03Y3SwNLfqsDfCuMiQ0V3MJKtoXx7I90OiL4Pv30g1BsSmEl_Div-tg6yOa60zI2CVGlLZBVCLsnk40bV91iOzWx_YP-K2GGkUkykM7UYINKMKLx3cCSi7-03exCc8heBJ0XKf05GgcwCx0zjDybxnrP_jZXTPJMVa08vTOst45_5jZcLgnxFSEGx88kxcwd9liYcUJ2BixWUUE5xbsd3Uhi2xZ_4u3qsNots9WkAwFTVrIhH93qZluXIdLmwCOq9xg2eU7jPb5EUhyKktNc5XHJ9AvVxqa-T2P2g180lzDveDBfblwaAVFoCpwr4uWBF9ZKvlW1gI9lQfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی دستگیر و راهی زندان شد تا بهش بگن کصمادرش چه رنگیه.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82514" target="_blank">📅 12:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82513">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl8jTX5wd9GSXIPtpTvjO51aFxoDGO82iX49yQhfax2abKA8bI8UCPo13L7u2vje110NCv3XhzpabGDVV0ik9F0HxBvkFIchaxwi0UO42SA5jbtfhfcXumkxu2sQ4DKRhIuW_AzHLXDtBBhdnWBRyvfemmTds7jbP9UHs4DGLB-1aGHopf5lJMg5jLHQ2jrnxRq04DOk9famrp_13zEFV4ZzjLwnK0Erv_Lm0rG4PXbhUWheIN0wCEQ5L9_pSNMJR0IpT2FIZP2DHjmZyqUhTm43Gl03yA00U91zxc7_h_4wqvLH6Y6lcRJ6sHcooSJfvwvsvFvvKnvFRjPy1JFBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکسال پیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82513" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82512">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwY8J_1Ag7gSFKKoAyJ8mZTUCx3n3zCCSWM1H9HlxM6NQHuM0MVRnlT9s3St42X9RPor_FKMK_wpEy_B1t8fdJ_4aW28UC2kLQtscC4Un19Uy4wkOJ4hJyp1Lc-OkecJdJBjtJA4GYiPYDqpRUn2YYb77ZHIeO0R5ma7W2a9BfwAiwuMRTGstGtonhF3YzftwnJM2ciFKhOVizW3s7jmXiW76yW3y7BgHP7fWUn0qI5jYFcpzzNcSWw5aKMk47j5yEV96G_o82ciHCRIJ9NISHJwPUEaJK5WAXmJ9ZfyFnxix-FsieZKibznI2N4D_GVRMz8DN4uOIBROjLM4s5FjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
فولام
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه کریون کاتج
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
فولام
:
۳ برد، ۳ تساوی و ۴ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۴ برد، ۲ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر فولام: ۳.۶ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۲.۳ گل در هر بازی.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما بماند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r2
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82512" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82511">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT8lF3CQ6eENHfY6DPEeHbGy95ft2F98CjNmbOxgUwv2DvuJ92QiZHB7ORMwzF5uTShrAh5Nr8GtzKXPrDktvWe5zvacIG7tZPJuj5oa2bMQrl3X456OqO5T77halIDO6WZ1ZLwf1QtU56CFhNtj4AIpwxK7lP9aOXnYldRaJM7VMjlyimt0VFFTfvYpcGIeHoPOHk85C0E7PqpeMyNGHKxu9cxFzsvsb7P4ETzpb48-kozUMB319-VRosgxDJWCt0dxrB3Grw9CWpHyx7CQclU8qjCp2F-pD5u2NPipq5--JgRy-My5O8p7OC2nPBj7CPRw-_cRV8FyYMqTgAM2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمعنم تو این ۲۵۰۰ ساله کلفت بودیم یا ما شانسمون تخمیه به این روزا افتادیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82511" target="_blank">📅 11:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82510">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCEBvMX66cC4aO6anUZKNkXjWHbCYZU6lrOLGDYG6Befycnl4mp_73Pcr8xqy9HlSj3MMrvCzQxWfs_gZQ4MuqBV3MwXnNLOSbKrdpP6vzDKC5A_sDo7asCwmMYWKimJcSIteIIm3JhqSq4y00SkoUiHmlx1s35WOyTN5uU89tuZqgYaG-V2jqLSWSnm1HP_2gnJ4oICRUajx0CPyYiB95W0hdLZJ_wjasMJFdDg6Th6xMx4Yo040siG_j9lofp7gc0H5RllnKxY5MGBb0Eky_Lec5Y0MnDk_dFwgQ7HEkgrJy7o7KdeS-0hnfZzxZuoDYGYPfGoVi1SqefKpbuKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی حرکت کن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82510" target="_blank">📅 09:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82509">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQeqKokFd4oVa7ugcJiq5JkbTlFohk_c-Dbl_OxiOFSMG7NffE64SIlUsIRChWgkZN2LMOjTf6ZhBgv5zZQOYJYrJ1rWthh7XmYjmWV-jcqFsxDSNjJR8cvtRbXRZTJtiVer8UOOjXKpvJ6toTmeNYP96gsnXgdUSWU4yEE0pV2WI55McE62VmFyMiODu6VTUNJD_crKAhV9DPl1A423UgvuIS2XNbmcB7DWbYFR-JdUtRCHk6hDzRCxiN5JO-1DGh7UwSlDbOGQqj0euFQSxmn2F86YzOQWuVYdDSgWRZO9OgN4LfWIAwsyhV2Ikv6uzEVpRwPhlqARzb0DZx9JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره کلی فیلم سوپر دربیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82509" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82508">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
آخجون میخوان پول پرت کنن تو صورتمون
وزیر خزانه‌داری آمریکا : از بامداد امروز، حمله مالی به ایران را آغاز خواهیم کرد؛ بزرگ‌ترین حمله از این نوع در تاریخ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82508" target="_blank">📅 04:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82506">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYHEEUVt3BIZmY7OOdB2ecyATGN3qft9Jq1Wf646OYpSj7YPMZu9JmQEyHsRX_WujqTH3f1A9wTgg6I0w6viVkcaEyjmhROXoA6XFtkFszXI9U0q_QBAN-jRV81jUONv8-f2ogr_LnDTP9cZoDm0YD744sO7rQ-KyX3HcuMDJN-Mh_r4xnEXP7IUNfcI3Vbp45NLTWwZr6hFF2hhacQif402KRCbdEkM1XtjLH-aY1WtMPz1PVzTirPn-ZxxvG4i3mgu51RpooP8yM9YluHWZQU61486PXwvrokdH6uxbY7hL3V5JIw0zJtoEckleHLiD4ixPnkEGJBmbpxRxa7hEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82506" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82505">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvD8wq6vZ_dFC3MZOvKAugg4a-AU3aJpdcyVs2w88zTfU7Z8ZTrH5UkODRiumXCo_yrLGkNlYD73CRr0za27z-oU569gh96msGWH8DbCaJdBG2rUrPTWqq7zgYX0wdH2Ft-YoQE0H9L-xszxR2CtdqXr_8vN2ePCBcfkcKRTpTOdj4lWdYs9xmScRTbxU1Rfs287drzwOkg5M4vUzFX99H8tev905ykNFqO9Nrdu3r2bybI1M6g29vcZy-7NpWNv9lh6UuG-0DtfnhvMngWjoAdN4WBgDt0HoTC-c-2ytfkbeuiXVGWZAdxPRHSKearL_lyBRbSadQPy7n3lyEWUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس سی ال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82505" target="_blank">📅 00:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB2xxsFj-IFhZ7aTwgVEVjQqC4lQ2RV5eWZUDWH0AqlsloBvH_CDplbVaE-tQ0ZJ2b7tJdLmEj8VAFqy34yMnjvtBWKu6xUy49F2al3Jtrz87pTcwDrq01uBXtGHuODxMQ5grME6MDpSuWQ0EgC2PceNqBaKzZCHVIpYVKKV44PGDZ2gr6Vm03jHqqWZVmtzo9zr7RzBhhGlutw06ApDuOWYZrFY0-dJSVt1FYKKg9PKWh4DGCleM1EFNvDjbvq4FlobE53KW-eCn22Rr34YbODki-SEK9dtRUNi3edlL60kMCf__GE6UuL-olwwU94eNDf2DuHVnQe8YorP2fwL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر حوزه علمیه شیراز گفته زنان شوهر دار هم میتونن عقد موقت کنن و نیازی به اجازه شوهرشون ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82504" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG5hCCTYDEa4gtznHC6na6Jru5KHPDWgeEfaja0peTfd_ks-LMOQSaS4D5w6I9txW3JqjsRiqpV29tPjkr9fLYEC6w4ObHl3kbo8yTRuyS4kZmoyeFfe3tgOWHQyNINe1JgTaOEOD2QjNYMD95I8eO6o3d1eLig5dGxLwZ34Dg4M6pYXjQL-fAMY-teWOSwcXL6kncv7j21-DN6bhnrtgpPxA1SUFqokW7LTrwRJLcPUcqw-z_V3a_PrFU5KZJIqDsiPweF6oqM3mJtdE5qgg2uNNTLutJrQAbeNwCLasTKPtP7iucKnIkS-s-0pSSn_E6r0oj7rrFXdICzJSAEplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز بخاطر خستگی بازی واس اتلتیکو رو نیمکته امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82500" target="_blank">📅 22:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">زن ستیزی تا کی چرا مجوز ندادید دختر بیرانوند کنسرت بزاره؟
شیما کاتوزیان لطفا ۱۰۰ تا استوری بزار رسیدگی بشه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82499" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82498">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAMrO6-YHdIN8ZzW87mVNbtVMRybUCuiZTKAe4yfd8IsXNylSdUign-VkbOo6y69wLt9Gt-jbVHZZAFLljSGrIdIScVDkKywbUEhgbEb8TOvwX0jIvDXUwMOoOGMpJPJMHoUNlnDPkRhUdi63aAHWYOIy8lRxa-jgCO7-7MGVXt6alCFSEs-Rp03bHgvq3dSfueIrNIF35RXbQGGigFYDuT65QUOqd3rAWCiP-rFPO3Axom3g_VaQ0IR90atz9gqNeES4i6e5wqmqAw1hnfN6Fa0sgOMiaK-P_emEzsffZ0WUIIZnu8hfxy2DW9XTnmncnsGgtYkP1KLPMjGP0G2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجوز یعنی مخدر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82498" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82497">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5UkI-bxScy9kUyHG4uppkcerC8pvrXZMzqAwH-KHgtIinYqT5uz7D-FiMImA964g4QsMtbMS13u3VPB7aj2dB7wM3lNFI5O8AK58Pnd78eaJccRTddJLyJbBb9ny4Ma9AcQf3RoP5ZpAvxl4zyEI-9-63iAAF9Rr1NWii7hIQoWiXYUHhcz3OVcIoy7qcLbF_z9Dkc3swNUvaLNwbJ8LckFX7-hrBnaC7MvazSlHb-QIg2YAkUzJMiQN6yuWMsE2Uyaz2pb4M-6yEmAdYGWLRKRaOb7eynvUdi8sktybrbhfR_rRrWl22SiQq4aE3YAyw48Uhh3VaSKADLVIDQ1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر پسر یه چندتا گل به خودی بزن تا بزارن بری
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82497" target="_blank">📅 20:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82496">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عجب تجاوزی داره میکنه استقلال کبیر به سپاهان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82496" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82495">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpwicNFFeaSIUrU1YXa7_OYjGrE0I1897X7KwYHTEjc6_WQIaVNC5JgWARNlFP-TliqWY8wYocWp2zJ65oLd-4UnYk3Q5z7dJN-QPUkfiA4BQRWyISjYlgRX3vhZawjK_lLd0xwaPfD94HB0xrVSZ8DLfseb_uH5eC5eghP7YOaoW0DGru4eqp_5wGjU_EHTycwA0lQPcDfeYBNg-b9g2G0Z1OVhNxhL95_POZnyZfv_l_AYquAcRxeRZO1uIoRHDLUGpF2maFXjw10Lr4JQdN5FjfyAr4ZnuMA7_2kdz7Eb8g1L8bPMIkkKJldN_evyX4_tJtJB4U3w5q2HmMm9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپ‌هاپولوژیست چی می‌کشید بنده خدا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82495" target="_blank">📅 19:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82494">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=Q9cLNt9WaBDUyVXoEB4R5kj2LiafBRTQod629_0ZqTfjfJ1orK4oiIfhd9NYJ0TJbkUwYKdbd3vI0JS1QPdamnxM6q8tIA3WslludaG97O3RiV8Yik4WcmTworxyUp7exMMztzCnTRr1koecJjp08xxTldmYJz26hw0Xzw5TvmxZav243NXW7qq93sagmmGKpKtkwqOo0kFmE744Tf-pXKNvJY-6O3mG3wc4x2VviZtSKDEiInIkE6sp4jYWPy7zCiLm95aZKPAs8csu0gLpppPIXMU1IwBvX5CAiMlvyE0Z3m9EDpI37h1uTojkQ52v_xaTaTID6Cs-wEJtz_T7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=Q9cLNt9WaBDUyVXoEB4R5kj2LiafBRTQod629_0ZqTfjfJ1orK4oiIfhd9NYJ0TJbkUwYKdbd3vI0JS1QPdamnxM6q8tIA3WslludaG97O3RiV8Yik4WcmTworxyUp7exMMztzCnTRr1koecJjp08xxTldmYJz26hw0Xzw5TvmxZav243NXW7qq93sagmmGKpKtkwqOo0kFmE744Tf-pXKNvJY-6O3mG3wc4x2VviZtSKDEiInIkE6sp4jYWPy7zCiLm95aZKPAs8csu0gLpppPIXMU1IwBvX5CAiMlvyE0Z3m9EDpI37h1uTojkQ52v_xaTaTID6Cs-wEJtz_T7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آفرین ایرانی باز افتخار آفریدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82494" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c451060b.mp4?token=X6QB45n2YM6QCYA5uBV5QW9rubibUOzjIb1sg6S5ktvn1UHpxndXgdGKcrBgNW9eaiv_Jr_3TcWmHg_g6DSh_eJUplb3XrRmX78bPCfZVvRCmTi8yG4Hyg5PPYvzxC0gymC6qtUt1jp9mgQ4h4FB3tzAGihOkc0uUwMpfARulikHt6NAmG-CK9Kf-Rn3qi0J5qGjX7PeeTaBJkIBscbHt6auF2ojE9MqchSVCRGwhEbHoRoj8DD_BbSvocOXeaiV9Y5WO1-AzCA9dZoFlK6Skpi7iE_eqJ5rF553tmW2MbiHB7VU-Bn4ILsUQGnL2ACJxoowiRKOBCePWEe4WJsGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c451060b.mp4?token=X6QB45n2YM6QCYA5uBV5QW9rubibUOzjIb1sg6S5ktvn1UHpxndXgdGKcrBgNW9eaiv_Jr_3TcWmHg_g6DSh_eJUplb3XrRmX78bPCfZVvRCmTi8yG4Hyg5PPYvzxC0gymC6qtUt1jp9mgQ4h4FB3tzAGihOkc0uUwMpfARulikHt6NAmG-CK9Kf-Rn3qi0J5qGjX7PeeTaBJkIBscbHt6auF2ojE9MqchSVCRGwhEbHoRoj8DD_BbSvocOXeaiV9Y5WO1-AzCA9dZoFlK6Skpi7iE_eqJ5rF553tmW2MbiHB7VU-Bn4ILsUQGnL2ACJxoowiRKOBCePWEe4WJsGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82492" target="_blank">📅 18:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خداروشکر جلیلی نیومد که دلار بشه ۲۰۰ تومن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82491" target="_blank">📅 15:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوستان به نظرتون اسکرین شات دلار ۲۰۰ هزار تومنی و ایموجی قلب سیاه شکسته رو با آهنگای محسن چاووشی ادیت بزنم استوری کنم بهتره یا آهنگای استاد محسن نامجو بهتر می‌تونه ناراحت و نگران بودنمو نشون بده؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82490" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82489">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب بگم دلتون برا همین 200 تومن هم تنگ میشه یا زوده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82489" target="_blank">📅 14:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82488">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ویلسون ناموسا چرا به همه چیز هایی که تو مملکت اتفاق میوفته با ۶ ماه تاخیر واکنش نشون میدی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82488" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP5zT1skTmYkkpspyodYN7hwRIR1Czz0pS62Wsi-OsK7aHq3VByX3hp6kQcJKMqcwmi6ITLSeM9VesVNMMaQTB2N8cPPuCQACqVAvMi_9ZJ81ZjwOfRnEYk564tcxOqreAdAcd0a637AaJ8WuC4QFw0BXtEu3biEvfPyys87A2CPU_X1Hp7zA0Z-eRe9_4H2tHgHCWSTPPjEN-MR4Z4Cf_qdAy41Bbn27CrOdCmNdAxqJohgltn9yajfH9ryVDESnM2zyqs3ywVvktnpzhpz9YPXfFWxIvHbHYgLuiycKh2WtdUOsTGfhqPIyjAQPvPUON-8iQCvFD1TDOpsxRrzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار 200k شد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82487" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82486">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دلار 200k شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82486" target="_blank">📅 14:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dw3TCeZE6QT0bDlLHrmN6QIwV0V85hYvQRUM4xnSJsYauRb7ReS2wXHnl1RcIUFYXpbTwwDawdrc51NT1Jz3oKAjIbC5EYilPvuqk2SVnpUyNkrKeUgT9dn5FzisglOgDE9Ow0nXIv6h8Qz-ndruDrW0WdmbMqHuNYr5t6XLAaOSE3InXclQuj-eg-4fc0awgVqEdAzInHw1B9buGhW-OjxthsuuVahhitzU3XuNa46KUeNw4Zc8llK47RqWgZNmL4gf3nQCPkEarYjANCRFV_SUEhXJKGbIr_qOPOMIawKP59Q6m4oSHUwCLNvb0BmSLYClXD8-bf3nyt4cW5b4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9eh-7EzUxmc8qg_UVmD9mht4gm4XbiCuE6ESpN6mBqgOLJZVrwI3tQz5cUHdl8hNYRSJy9ZFq6Jj8OaZAPpshfo7iEREZIqCDFAa0M2JQ-Pply-mpJ8uFF3ibrPLNCWj1jreSAnW3CXbyPeUx2JmMK_gumHKSI2IRCBCTLhwhglBR1S15KxpdRQyFPsCSAA1NY56AxInYubGZmmmAROf4R4GJJ91JaQN7RWd3d6mnCl6fN5OV3fLebFkoFULS0fBndvvyMl1OeOX1BC7EpQrhldV-tIx9IEB8XQmtsvupElddG1ZhwwRhx9W8jLWlfyh4XKf56Pymy_U0SFha4mpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند کصخل موهاشو کوتاه کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82484" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trTotJ277GKyPRZJWLz3Vz2z1fEbaNSnCd8xlKHLfBPt2fTdZBxg1PCypL5ScZo6pRTRDAdUz_c4kNhS315Zig6WyvoHfHOSuph4sFOQKNVv5a9GGLfY4CTOuw6W6749ZZsw32U7XSnuLHkSHnNQBihglCYwvet7q_VIt0DunykV7OqnV6Kn-ecZijBczyMn20K3SBzHSg9N5ZDEh3jcYR6MM9FAxperc4mdA9Ukx9n4IEVFQB2geJzjyhiJyt66x7C2f3uHebQGf_O_bm-qWcvlxqDIrTNSYuw5ZcWr9dvnnCi7NVI37EM9o6OaDeWfUo1oDn_F0jDD4eHo-AsFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا ارومیه رو چطوری ربط بدیم به عربستان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82483" target="_blank">📅 12:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df1ed91c9.mp4?token=Dt-kbQYDsZ3KnF7TwJV0nwXN11H8qyP9cnFfCJrGC8sPE2laWGu6qg6InQlrNnTxd_zoNUwFwnpz5oAa1QxWRyFbSJdW8STGUyCCyxv6wkzXB_1wKe4bMpLFtPKsRLO6Ip3CdkLvJ6zaDD-ZpSNrgrkXQ5lClbypBE00NeEfh7HKVXgdk6NaMTcz-9PQWrI8VU9ugJvVybb05o6q3afWvymtOvpgRZbXGkCymJGmqqBeDivYAZLknDCgxOnHXc6p5n9LgJUkTV4IW8hPAaPd8M8pTZlSGFME6qf6k4DplbIM0CW1VJk-_Tauekn4919sLIfUtXbWmIFunpM9_6x8nFENsAq3Qs9-XtVRKoLOp9FVSVX_bVU3gQaZph-eApjWnUPtvweDMEApX-k2FF32kUtQ2fhTMQUpY8hqYI68E_5iPerVsLAbByXCj0eQtl5jAatOW36_dnfYBjJ56sBH_-ih5Fr-0EZX5Aw6QFDB8wp0eNJbIVxuSUIOkdmw3S5aoIf0QM5vGiXsF9cKrUD9lAxsA-txLVsB8sxqpCNkpIOIASySxigJwQWcQLT45hdGsdJM3mMPUgz4hpfuHbWVwqmX9zWT8ZXD4DN7rWWhGKH2nMTHPGFQmvLkM1ifm3x5GivUg0PGkpWHg_6_-O6_O4yJLXmTPsyc01myz-2fqvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df1ed91c9.mp4?token=Dt-kbQYDsZ3KnF7TwJV0nwXN11H8qyP9cnFfCJrGC8sPE2laWGu6qg6InQlrNnTxd_zoNUwFwnpz5oAa1QxWRyFbSJdW8STGUyCCyxv6wkzXB_1wKe4bMpLFtPKsRLO6Ip3CdkLvJ6zaDD-ZpSNrgrkXQ5lClbypBE00NeEfh7HKVXgdk6NaMTcz-9PQWrI8VU9ugJvVybb05o6q3afWvymtOvpgRZbXGkCymJGmqqBeDivYAZLknDCgxOnHXc6p5n9LgJUkTV4IW8hPAaPd8M8pTZlSGFME6qf6k4DplbIM0CW1VJk-_Tauekn4919sLIfUtXbWmIFunpM9_6x8nFENsAq3Qs9-XtVRKoLOp9FVSVX_bVU3gQaZph-eApjWnUPtvweDMEApX-k2FF32kUtQ2fhTMQUpY8hqYI68E_5iPerVsLAbByXCj0eQtl5jAatOW36_dnfYBjJ56sBH_-ih5Fr-0EZX5Aw6QFDB8wp0eNJbIVxuSUIOkdmw3S5aoIf0QM5vGiXsF9cKrUD9lAxsA-txLVsB8sxqpCNkpIOIASySxigJwQWcQLT45hdGsdJM3mMPUgz4hpfuHbWVwqmX9zWT8ZXD4DN7rWWhGKH2nMTHPGFQmvLkM1ifm3x5GivUg0PGkpWHg_6_-O6_O4yJLXmTPsyc01myz-2fqvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تظاهرات با چادر تو ساحل دریای مازندران برای اعتراض به بی‌حجابی هایی که در سواحل رخ میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82482" target="_blank">📅 11:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a208381aa.mp4?token=YKXh2n-XDRFHzOqS5D1UowxW2zrL3R2BoypK3Ilpehml9giThhgPXf10y_zRzQKI_SoA0gke3Yz9mZprfrxEi6gxIUuz610dlAq93bZiYdASOZLqZMhnRruTCFxDGElEb12_Fd7URVcF_jpF9k9xwSC41wrXw7bb1-lsnsflBIYap7lbbTFJclqSJHsqO-8TdpojFAq_u3fwS06CtDjo1I2Ky6yojGE7REGvCVOzanwaGGDDx4nzck7MmohfYvNfNTPfWgfTzh4FlURiVxYOslMsNRFO3j3edc_xSWjy-oJRugJ0N8j6CPj9K5QDGlmFQsHTgFx7tvEqYUIGhWG2LpMUcJmOmO3FSiCz634-JQl13gJJO2tE-2vzelQtPOlZtNWv4PMOaz-tOoXGqp07IwjdGVq1iSsJP-7zqmYif8vNDR65Y3bl2EGawefeWH9zEv53MKTlTVbofuQz60icmo57gddS1QUI4xCQJEqNJIJJDvfjzEpruX_VudqGcYvSfJ0BhZlpMR8tGDIvYL6-u_L2koODt0kFBXEjtZ8NPoYyoy_3Yt8nigKCVnuXGVtrz_9OfcSyc-l3gGnBD7k3p1_ofnMIhDvm1LzrldTZOS_20Pij_VIQwiSLpkbjefwNEfHofAaV7IqCSOSSBkM7LOOrEMSzK_PIKPM9YStLwuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a208381aa.mp4?token=YKXh2n-XDRFHzOqS5D1UowxW2zrL3R2BoypK3Ilpehml9giThhgPXf10y_zRzQKI_SoA0gke3Yz9mZprfrxEi6gxIUuz610dlAq93bZiYdASOZLqZMhnRruTCFxDGElEb12_Fd7URVcF_jpF9k9xwSC41wrXw7bb1-lsnsflBIYap7lbbTFJclqSJHsqO-8TdpojFAq_u3fwS06CtDjo1I2Ky6yojGE7REGvCVOzanwaGGDDx4nzck7MmohfYvNfNTPfWgfTzh4FlURiVxYOslMsNRFO3j3edc_xSWjy-oJRugJ0N8j6CPj9K5QDGlmFQsHTgFx7tvEqYUIGhWG2LpMUcJmOmO3FSiCz634-JQl13gJJO2tE-2vzelQtPOlZtNWv4PMOaz-tOoXGqp07IwjdGVq1iSsJP-7zqmYif8vNDR65Y3bl2EGawefeWH9zEv53MKTlTVbofuQz60icmo57gddS1QUI4xCQJEqNJIJJDvfjzEpruX_VudqGcYvSfJ0BhZlpMR8tGDIvYL6-u_L2koODt0kFBXEjtZ8NPoYyoy_3Yt8nigKCVnuXGVtrz_9OfcSyc-l3gGnBD7k3p1_ofnMIhDvm1LzrldTZOS_20Pij_VIQwiSLpkbjefwNEfHofAaV7IqCSOSSBkM7LOOrEMSzK_PIKPM9YStLwuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خانواده تبریزی تو استانبول عروسی فوق لاکچری گرفتن
یه پولی‌هم جلوی اندی انداختن پاشده از لس آنجلس اومده استانبول براشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82481" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صبح بخیر
ترامپ: تنگه هرمز دیگه جزعی از کشور امریکاست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82479" target="_blank">📅 09:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsOaZExyH07KQT6KHjtvMqoObFTfMfZoJBwwzHrqugX7I5Z178IHIefYXsaLUlw3my3CaJLBd5BQrjed5CPm2SSZqmY1LjBtETtgz-MMVpyH0n3jV21C15iV1MVjckTGQ5PFEwMYqUTV-M34qJY1py0jCYTXojyC5NALTwvYCyjeaNca7rq3VNyQl8jaMmrGna5WwIfoceyQJCFIDMSSKKGamH7_CI6ej4TFzUgJAg-8ZNeRuv8rFORSnt68HHDUxmkjqvH4jxcUp1_UjnYTH1mG6qLUv9x36PdMkHQPNp5YjTqaX82hgtaPqERLUF91V_hshlACYI3ydUxdS042ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82478" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کوروش چقد خشن شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82477" target="_blank">📅 01:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82476">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مورینیو یه خسرو حیدری و حنیف عمران زاده نیاز داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82476" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82474">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓔𝓻𝓯𝓪𝓷.</strong></div>
<div class="tg-text">میخواد یه ورژن ۲ بسازه باگای اولیو رفع کنه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82474" target="_blank">📅 00:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82473">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پدر آرات داره بچه جدید میسازه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82473" target="_blank">📅 00:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82472">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp0a3KVd0hknmPqKT9ZS77snQXBMBcktCteEaBnPaMN2aTau1jouGUr8r28_I3U3mThDue2F-jJ69gpUnuwB4kSLV6EGRbyR_o9xKk4LmY-7t_TD-rRaKjMP_99p-OM-nH41XT3JU_tBHJIC2opalkXCnOJrbKeQfVyv77VRBHfSdT9EUS0AV_Hfqc6JpwA94NBNIUbjfQ_RFTpQGPq9-3Of1BamRic4MUyVFcGD_Ou_ce0jzeKBO02skoGzOFcnOe2qukGCq_H30IeyU8IErZgIJDawnmlaem3-I0fjmGRbCAHylJE0QPWTmK0_O5lSREhr6K90HqIh9HL8d4STnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر آرات داره بچه جدید میسازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82472" target="_blank">📅 23:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82471">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کیه این؟</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82471" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfFZbyJnvsOQcAgv00RklekEdV6lItksIzvxvizRGP7Q2JUh7pCtlWhTwtWwaec__74kGwf6OBt9vMUSLm01GjFWb4XigxPn8-Daq4bvf5DwCt9YfUSL-yAQZYjLzB8NR86jr4O9p8Ipub8qBgvYEOqZoICglLoGYLpSOAVXgykc5fUgmr3ir5yR-2al_I5pksKuHncYuDIWQy4Sgcd7Machve-_0QlVapXkBzWDynYyFY1fmTPTZNplC73ogBhyXqpX3Xq0mC8XtbIF-1o9Z410kdMcPlCUvNRjD-zvwgzPAP-Cy36l3AARMk7r1vi_gWlDQki2nh380V06MH1r7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه برا خودت ارزش قائلی از تلگرام دور بمون دادا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82470" target="_blank">📅 22:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82469">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان که با کد تخفیف (
bakei
) میتونید تا 20 درصد تخفیف بگیرید
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82469" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82468">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uf-TsOd93Oenva94RfohAPrtqeui_nduUgq0XPmPStjvNeLAGudOsO3R_dNowZbeNMNs5F9Sown0gP45znqsKDmSYTWzJf3UNLWjz7xovqQAfCafhLhAWeBQ7-QzAoQz0Mpsac9pLTx5Zp12dEwTj-ljYsOsWjpwUybku9e2ZkbtA3fU7lqmk981xvck9ulNhwwr-uzO8yzYlO5SmmShr11spIqNr_2FOSgeuOzdMRiCuECB-k8X14_aMYwrZ_yQho-Jrxm--xLzaHfzj9VKUfKYVMDKDH-K7QCBdw3mU3egy3lVyAIvoF3_SsB0lEp22X3jF0aPiHx0GquoVSTfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتنهام چقد پلشته، با اینهمه خرج بازم گوهی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82468" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82467">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82467" target="_blank">📅 20:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82466">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82466" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82465">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCOn5OvPLgD5kkwU7mfm56T-_ij_g9Qpy_jVnJN_C2MTjrX64me1lS_PCWCOmqmMnwWu6PR18gNkS5KMogjEduafaXsG0nAMW526HkSO5pXN3XGswar7gKb7yaedB3elyclF6FUsk5ifO2bE0DdI_nnAusgSNP44934C44vAHEy6XYfq-nm9hnj9rRl9NuWvzSKNK28t5v_xDl1b_21LHpsBtSAYyjkL1AqSOK8bEp2T7XgO17XoLZssnLHR1aEfHud91RWD7nNNWBCdw5025ShRspGbfHzJQmzHP1XhG9CCHD0ZpPmFEHLtKinTe-QzSiMnnqwB40oQep9R8VqONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82465" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82464">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=Uuh9Q-JkYBrd9kABufg-3OSXxg5itK2IVb9TjEqNk6huze2cJnm1kyHqp1BSEcyjPbmMiD_KRKGVgRyEp2aZWJLGG2WokTbeM28lO7gNlvq4ws2arrNTlnal19w3sxSjqHSQmVh-b1kCIQ9JyWQr_-5J3k3SXhNow6YgGOIRaR4adbujUneNVQFnOymb-qO-vgNNemb-H4CRFAWYodOI8UxSsjI2J3eo4fAF2MCrnUFVHQEgVNrMEUiYjekB8ehjiVJb5BuzX8CHhF9yy50tyDfyCBo_Sdi7IUJnvuQkrHOi_1jGMWDNLxyS9pF7SiB7JIeQMRrDS1nU0-fmjvx2bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=Uuh9Q-JkYBrd9kABufg-3OSXxg5itK2IVb9TjEqNk6huze2cJnm1kyHqp1BSEcyjPbmMiD_KRKGVgRyEp2aZWJLGG2WokTbeM28lO7gNlvq4ws2arrNTlnal19w3sxSjqHSQmVh-b1kCIQ9JyWQr_-5J3k3SXhNow6YgGOIRaR4adbujUneNVQFnOymb-qO-vgNNemb-H4CRFAWYodOI8UxSsjI2J3eo4fAF2MCrnUFVHQEgVNrMEUiYjekB8ehjiVJb5BuzX8CHhF9yy50tyDfyCBo_Sdi7IUJnvuQkrHOi_1jGMWDNLxyS9pF7SiB7JIeQMRrDS1nU0-fmjvx2bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرمال ترین حرکت پسرا تو جمع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82464" target="_blank">📅 19:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82463">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaZofqwpkfgZ57Ec8jJyYtZL78XaWYA6IbOqVCZUrDJ-EfZPMbbpxiHFcTpH4_2ul0fgFIZ64Ky4gnZ7nf3G_UQiWllyGYP9ww40OFWYwsjR57E5oHbmexqRdkqT5tCtY74hp3aR1m2Mm-_Rr-lBdKPAZmQi-bSRHG6Vf01NnEyvI5zpogHpO88O4TlH5f4N5jWblj3bX0woIgb3wXccTn1pzgpQzDMMvStHxDFV8mCSfE8CwJbm7FW720G5dWnTWF9bOmFSkFi4baDXCysFlDtes9YvteTBBG9RZWpEu4NseI8r0ZnWRu8PdZMhr3QOAmBM4DtGKvtG_nTyU1rxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم برا گیر کردن سوزن حافظه‌ی تاریخی رو رضا پیشرو، دو تا کلیه‌هام رو بدم تا قبل از مرگ بهترین محتواهای تاریخ بشریت رو تجربه کرده باشم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82463" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82462">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ycoi1ZSG_gSDzaFf5tedz59jpJmLC_jMcR-1856CNpVKeYCg_NiGWtWxnAjAYz7SclMEFhr8CL9ySCZSneB6h4n4opCqwA-LnsqN4U9FI4FYLDRvjqPh7F8Xy4n-kcGxgC5ucD70fCl33vBezHb3NCJQN8J1Cs-ji_gr2TUIpje1VfsexmvxkGcUbCzop6Q4hoGBokjOfZAhklfgnRL0U9vuQptqkCBq_jIfsSchEXSBEfkK88jMWtUFjSr8GVd2Ospslo5ru__o1LjBslgJTwwx7m0h2Enx46RVxezQESX-ObqcYAZU6_daVFC7nD2aT4ybihDzvqSxriB971jbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به رضا پهلوی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82462" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82460">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b179e0b7b7.mp4?token=R9kN2tnG4mapMSou556nWgkUPnyUrlYhA025mjbNzjHjOWEffhQ4KyMZISRa2iNbydJQRhOxrJXdzEwQTNGZWORPn2zIKtdzM8vUUZJeCNA9Wejbcde86cSENvUhFHkem54WRYQ9ToOzLPDQAzq39qsUW0CkvBKUhuB8W5zFn2U6VO53HUouDGZutECILW5AClQsdBZX8W8O6hANH9DaLisLFJFWz_rxT5fUBJrEmM_1V27T7dhE4EmkXOJg36wle8pSrz4BLJNQZpj2GfBlZYdtStF5_IsI8xLzbaMX0D6axgCTi0XJ91pWgCJyKWBQbLOAlMRFR4ER1gXANE9hsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b179e0b7b7.mp4?token=R9kN2tnG4mapMSou556nWgkUPnyUrlYhA025mjbNzjHjOWEffhQ4KyMZISRa2iNbydJQRhOxrJXdzEwQTNGZWORPn2zIKtdzM8vUUZJeCNA9Wejbcde86cSENvUhFHkem54WRYQ9ToOzLPDQAzq39qsUW0CkvBKUhuB8W5zFn2U6VO53HUouDGZutECILW5AClQsdBZX8W8O6hANH9DaLisLFJFWz_rxT5fUBJrEmM_1V27T7dhE4EmkXOJg36wle8pSrz4BLJNQZpj2GfBlZYdtStF5_IsI8xLzbaMX0D6axgCTi0XJ91pWgCJyKWBQbLOAlMRFR4ER1gXANE9hsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وطندار عربستانی اولین موزیک رسمی خودشو منتشر کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82460" target="_blank">📅 16:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82459">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_J3XlsU34qLoWAdAHHzPjyl6WmaXHpnU8WZi1fcCzBfCWtQ8THC8_OFxf8TkCcsw7HlPWO3nV53oLpBYv6TZ_IX1ws8xAvpn2iD5EA-uP3P0tqb_WehvFpWR1Q1KbfnzJr1Pzpa6CPV0lwR2FXhxJNB6MyRaEnJ9fqY2hKIi8yYm1pn2rMmliMC_7Yo6MZo_RZYkTU8PzFttDUQNWqFwbKQ4dZA51Hf31-N6ss_N3iYPBIOYZRAZL54IJOJX6iiBpCvdzilV8xSv_qLLXW6cZj3dwa653OLRPMzw21h5DsbSjZNGdt1BJeSrX4GZ5s1oUFPmYV3a2jvlW5bOGNaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدسامتینگشاه:
تو چند وقت اخیر کشورهای همسایه از ما خواهش و التماس کردن که باهاشون قرارداد دفاعی و نظامی ببندیم؛
چون براشون مثل روز روشن شده که وعده محافظت‌ها و قدرت آمریکا دروغی بیش نیست جوری که حتی اسرائیل رو هم تو خطر نابودی کامل انداختن؛
پس فقط یه قدرت مستقل و مقتدر مثل ما می‌تونه از صلح و کشورهای منطقه به صورت واقعی محافظت کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82459" target="_blank">📅 15:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82458">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxwdIL-jGcF_EQv-9sD7_uDwijY_iRlLd-IjFr-Emoiqz-qpTVGyCNxYkyeN8MZ4BMMwGLw_REbF5rMUoe_9gTGSuvBgfKJ_E8DcuxIaGjpO-pNGK7reuhhinqEbGSUVMYTkwZsjtyBWWC3vvPWlTEwOfjzW-ePiWck2g7SKgMKvs_rIKbAd4nTp22ZqQFr6ZO0Wv-wl9H8r5Jmqe2te9y-v7lZcafXLiL-rQO_QcHjLJ9_4mE7P8jkb_JALIz-2hV2NZJB0-P610e-v6SroZDk7bd61Ur8Tc_tfW_E2L1mp4wd9GHZHC0SpHUmSkxVDhuKaPNyW9WIN0r-HBrpmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این دالگ شامپانزه رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82458" target="_blank">📅 15:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82457">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b87bf64f9.mp4?token=Ofy88DBRxdkfVL4svCz1M5NQJJLCBAAX7SJSPjejAk2fWMdAhXXluU3dgq-sPMBKiROE7eQAIDpOYD47GFIFldDFSfmRFiaPkb-D5J4pQkg8dgZ-_00DsCxx9bUfGuDeDGtQMRvStrcoMy3dr8YPWTh-P3OZlKKWFiy6oPaN5NKJE51vXtnzmC2cfWs4_yWlvm7F726E7XDk0t267f5ukD15v4nmPg6reh6s9hLKE9SUA_SGT3OHCh3O3zjU_qukxiAX62dFOubRZ3OAsfffKTrd01MLxnpQj5VN6Yx_joAvf3RHb8z7ZE4STo5M71GsO22TUW0r7-Fn5pEkR7NKEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b87bf64f9.mp4?token=Ofy88DBRxdkfVL4svCz1M5NQJJLCBAAX7SJSPjejAk2fWMdAhXXluU3dgq-sPMBKiROE7eQAIDpOYD47GFIFldDFSfmRFiaPkb-D5J4pQkg8dgZ-_00DsCxx9bUfGuDeDGtQMRvStrcoMy3dr8YPWTh-P3OZlKKWFiy6oPaN5NKJE51vXtnzmC2cfWs4_yWlvm7F726E7XDk0t267f5ukD15v4nmPg6reh6s9hLKE9SUA_SGT3OHCh3O3zjU_qukxiAX62dFOubRZ3OAsfffKTrd01MLxnpQj5VN6Yx_joAvf3RHb8z7ZE4STo5M71GsO22TUW0r7-Fn5pEkR7NKEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است  ده‌ها راننده کامیون تاکنون جان باخته‌اند  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82457" target="_blank">📅 15:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82456">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VcphsR4rIhCYU4zkiwA5R18RYAO9IWfv_inxA7oGUyf-Uf82bNLNnG0BZtZzaqlpJzKOZamdhE_l9UN6KNtbaVfuHhd8MO4441DH3e1vy57uQZBeHwZzShcdZ1Xbq-ZOWWLneTfpeQcvwFUTnrG5uQs7wgP5PDRfSBW4KvvrUAYfR2tpz7fLX8zAnLsbNB6sVzmSTnE5EcIcMHgqGvXRcw75w_N5E-p0a_CtyOD-LLJu_up-WLofAxlGUP1SNIG3ABjIjA2Hqa9Zc2v8GINWUGEaGenjQyTdmJRQNWOWXVmZzAD0Wg6HO3YHPHOCjaB2stZkWCyOsBB4XuVW7arA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم بعد از موفقیت ژانر «پشمام داریوش تبهکار بالاخره ترک کرد چقدر خوب شده»، الان وقتشه با ژانر ««پشمام رها وانتونز بالاخره غذا خورد چقدر خوب شده» چنلای رپی رو به دوران اوجشون برگردونیم.
#MFGA
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82456" target="_blank">📅 14:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82455">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpNd5Ww9hHUSiCnKSI8Tye0TZPCaYrm-yVCxq7Wd4SjyCptL3na6tNMDJ2pJv-ErngRPmCENYgWSZPAXaPtbVwndVnUdKUMcVEfOeTm38JW--d1RvImCpwL2_GULQmsjWmPcTjALVYw_gfh9qGEBIMVK3ssA5V8RqHWJnQRjxzRn81uuAXaP2jm7GhwULpcrfD0T1OnUUa8M79B6kx6hFbmXWrRs-w_5Yd2KOLEJ43tF5zuOcNiX5km4MNKYsiFxosxieeftsMy2h6pyACPTOMMJuMeLZiRADNNMdTlXEKPfTasoHXqfs5FkG7lVEjNQTil-hVNvRgmohes0tTffRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مرحله‌ای از رپفارسی هستیم که خود رپرای مملکت به یه همچین فلاکتی افتادن بعد یه سریا جدی زیر کامنتای این چنل درخواست محتوای ۱۰۰ درصد رپی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82455" target="_blank">📅 14:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE-2G74Y1IvQAl2xPM5yUjwD36LR3caKFpcS2tkZ10IY2lPKf7KGm7gjhjBtkfG6GrXIQ3kG7T9guCeuAvvGfnucgMQNhxz4e6oaN9Irmz1okkX4GNfLaLENE7_hsEq2FQZSD-YvaBG1DfHlpq9NTBnRvHNMGKKeUXrIks_AYv-_o7VgI0r5ElJyr_EmSURtpR1h7ob0LluSuofxABBX-Yq4XJ5pbCIHqiCuDucYMwjIUaEvbLqw0aZHTSQRMpWSZou1z_C18C2V_EVAzaacLXB9XhKdFLMWzVP_Hlgsu2S-snoGWcsKlaQHaNyun3-35Ma2Qtf0kRjuTWXdO2U19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خو کصخلا چون عقایدش کیریه دلیل نمیشه هنر طرفم زیر سوال ببرید که.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82454" target="_blank">📅 12:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسطوره تاکتیک های ناشناخته ژنرال محسن گواردیولا: با ادامه محاصره دریایی، ممکن است از پیمان منع سلاح های هسته‌ای خارج شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82453" target="_blank">📅 12:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82451">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ6KQJ4_GPkZMP-4x-aJYjiHztN2QXzUYQyfF5YB6UTrWJQFWtX0KwdXyG_y8GUjl4IWtUi5kDSdqiAQuu8fdefnLSVaaArppvJIEUGmkUhTaP1PsTDgOs6QFJKC5hd2GyWWBEt0GLTfez4q9aXUIsXsm8_gMFZ8ZM8o-tTTnbYt_QGmoPX3inRzc6ggLaZuau2wHDgIfVztrSyjYiqhagRBcDBST5k8aSkZE2QDj4XJK32TbJZTEj2e1LnaZII1jn4Rp1iucEGQjYafQz_OhFIiaEPggaHHvKguffipi61D9imDrFZfgUVreTS1boYOHaw7QiPHT8M9MwtV4p5bCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a203398b.mp4?token=XE9Osflwx92ksGZDCf0gs_Y9QKjNJ2pYN7liIfHOLh52oc_WG8ReqqTKiFxtzmfAHaZ9oFRQV0Qz2-VJaRsk5QAdtomm-a7VUxqxf91OMJezbLW0DQ5LMxuxv6qjyS59C3MJ1K7xrNcWQkyWQmtwB0ueSdrbfwY-vS7XuK8NSORLDVSCdkHO80Mcx9n135bceQUOgvk6rJMnuEYA3BTblT-tJ5OAyP6X6kiQ-briZi_GnkflE_mYPbTLcBy30-iL3xW6kkW-78uonXhpMWZu3InIhbkua1E4DO5yhBKfN8JDupxpzC1rIonuEn3rxUuJrXrx06aym5S3rRS7tEzHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a203398b.mp4?token=XE9Osflwx92ksGZDCf0gs_Y9QKjNJ2pYN7liIfHOLh52oc_WG8ReqqTKiFxtzmfAHaZ9oFRQV0Qz2-VJaRsk5QAdtomm-a7VUxqxf91OMJezbLW0DQ5LMxuxv6qjyS59C3MJ1K7xrNcWQkyWQmtwB0ueSdrbfwY-vS7XuK8NSORLDVSCdkHO80Mcx9n135bceQUOgvk6rJMnuEYA3BTblT-tJ5OAyP6X6kiQ-briZi_GnkflE_mYPbTLcBy30-iL3xW6kkW-78uonXhpMWZu3InIhbkua1E4DO5yhBKfN8JDupxpzC1rIonuEn3rxUuJrXrx06aym5S3rRS7tEzHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مینا نامداری با حجاب رفته تو یه برنامه داخلی و مصاحبه کرده
تو یه قسمتشم داره میگه پوتک بهم پول داد که آلبومشو هایپ کنم، اینم واکنش پوتک به این حرفاشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82451" target="_blank">📅 11:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82450">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f612890d7.mp4?token=cV75-ycOvI-YCHwPDa1TQS0K0F2AQTxmqBrcteBk4BWotxnhfdndx4swSHdHHYJx09nasajymwCcRv221D_rV3Dipr_Pgd-cfVXWiS710OCzuC8SmYYdCulXhFuktquGZyyNfKjIKneKE0RZTIoZ_DUqi1wdxypkUkqmuSu98WttTKftmA8NUYSmIMWCxCK20SXlU2nvK-VGWIwG5V0K-cI7bMWtW3vlEdugHkCgj6FhRToSG7f4LHQeBiVf3nlPlTING1M-LIeAe0Fpx7tnlaf7ULmh_6b3yrPmja4Rw-75faFayublisiUjBz6WKVJ_yJzdW9dBuk72lhEU35Izw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f612890d7.mp4?token=cV75-ycOvI-YCHwPDa1TQS0K0F2AQTxmqBrcteBk4BWotxnhfdndx4swSHdHHYJx09nasajymwCcRv221D_rV3Dipr_Pgd-cfVXWiS710OCzuC8SmYYdCulXhFuktquGZyyNfKjIKneKE0RZTIoZ_DUqi1wdxypkUkqmuSu98WttTKftmA8NUYSmIMWCxCK20SXlU2nvK-VGWIwG5V0K-cI7bMWtW3vlEdugHkCgj6FhRToSG7f4LHQeBiVf3nlPlTING1M-LIeAe0Fpx7tnlaf7ULmh_6b3yrPmja4Rw-75faFayublisiUjBz6WKVJ_yJzdW9dBuk72lhEU35Izw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی اتوبان بابایی تهران، یه پسر داشت با پژو پارس لایی میکشید، که این شکلی بگا رفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82450" target="_blank">📅 11:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82449">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bde28cd1.mp4?token=pFKDvL0verNF3xAY-P6xlHGHIeQJxWM2gRGESh-PJ9DiTairXeAlap65RFBVfhUoy-MbQWMTfE-ImVlRk862bZt1ivVV_aF74ZlRY-3L7wXVRypNpn6R2BdowaOqf5kxQrXluR8EHyT0xTVYYdCL7D7bN1cs9Jbe9hMZmhkzo9VIeZn8Kmtwi5Zu0-9s1AREetFnLuGjoFc9uNvu7MzkUUCKfNIM1GVUISvU6qQBQgIIpUp2i7WHbcdQ9Koo_xlhrk-78t45IqZTWK2IAdXXtRVwvyOV29qqHNtyG0Zbgr4pYs1sfvfd_Li6R0UT09MrmGlYOUwppeiSX_sjROKMlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bde28cd1.mp4?token=pFKDvL0verNF3xAY-P6xlHGHIeQJxWM2gRGESh-PJ9DiTairXeAlap65RFBVfhUoy-MbQWMTfE-ImVlRk862bZt1ivVV_aF74ZlRY-3L7wXVRypNpn6R2BdowaOqf5kxQrXluR8EHyT0xTVYYdCL7D7bN1cs9Jbe9hMZmhkzo9VIeZn8Kmtwi5Zu0-9s1AREetFnLuGjoFc9uNvu7MzkUUCKfNIM1GVUISvU6qQBQgIIpUp2i7WHbcdQ9Koo_xlhrk-78t45IqZTWK2IAdXXtRVwvyOV29qqHNtyG0Zbgr4pYs1sfvfd_Li6R0UT09MrmGlYOUwppeiSX_sjROKMlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است
ده‌ها راننده کامیون تاکنون جان باخته‌اند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82449" target="_blank">📅 10:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2eddcce9.mp4?token=JfU_z2HeDc40cT6fjBvaRV5wwWW2Nvmh_HzdFWjRo4XzKKeLLCCT5hoqgkRU9u2trxGUvwRxlhILnDRW7eBfXJEEIW-wwd6av3gsU4PV7PGGo9B-PvlrmjXR0dUzb6x-CsniaBCZ8MNVW2CjxXU6blD3Pz9-KaSvS2Ee_ztPmSuYdCFRPSfpLt_e3tnuBW5-_e2PFUu91IGXIK2gEPFpCGBonICm1THF45zRuI-Ik9w6VQ0bhUS2asvtVaAz244MVWYNv60mFCYxvunHhS-M-9ell1w0TQr1eiJ8IOzFhJRc7bYnKM-wh7vFDudYlZb4Kf4P_aE6zxlezbqDmxci3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2eddcce9.mp4?token=JfU_z2HeDc40cT6fjBvaRV5wwWW2Nvmh_HzdFWjRo4XzKKeLLCCT5hoqgkRU9u2trxGUvwRxlhILnDRW7eBfXJEEIW-wwd6av3gsU4PV7PGGo9B-PvlrmjXR0dUzb6x-CsniaBCZ8MNVW2CjxXU6blD3Pz9-KaSvS2Ee_ztPmSuYdCFRPSfpLt_e3tnuBW5-_e2PFUu91IGXIK2gEPFpCGBonICm1THF45zRuI-Ik9w6VQ0bhUS2asvtVaAz244MVWYNv60mFCYxvunHhS-M-9ell1w0TQr1eiJ8IOzFhJRc7bYnKM-wh7vFDudYlZb4Kf4P_aE6zxlezbqDmxci3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوید محمدزاده داره تمرین میکنه اعزام شه فلسطین.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82447" target="_blank">📅 10:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این کصشرایی که عرشیاس و چارتا پاپ خون شبیه‌ به اون میخونن رو میبینم به رپفارسی امیدوار میشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82446" target="_blank">📅 01:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82445">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpZcSfclszR_5llQy2D614xSCOOjYwBaS1AH_D52vs5Q5PoNSPvz9ds-7J0H2ug_Az2zHPsLyYIplNV8S3gR7aAC_mYnuOnZNTOEsTvkayMRiCcWwwrhrhdke7lq7LDPQExO97TBnLxO86hoaG4m0nC05Sc8_lwiXTBOwS4cUqcabNji8Cslxdot86XOGKFcdE3GgZyGYjHjadqLyeC-1wOD2YpnK3K-ksrBxovimmtQZzn3BJ9cFuQn8oxWcv6qKERMi3i8ffPOFXmRLUtyV1YZE-nFxTuRKzMcgMau-8IoHGra1_ZqM3uVYuiKZDyjk3H9SGZbH3vWIACXllmlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوتا بدبخت رو نیمکت آرسنال تلف شدن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82445" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82444">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">از ترند امشب جا نمونیم
صدای انفجار در امیرآباد، تهران
احتمالاً فعالیت پدافند هوایی
مرکز تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82444" target="_blank">📅 23:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82443">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKF0IHB5InerPOUE62sEKOc3A7qEpmj3xzWfTkjoA-wCWCqMwIf9LiB1EgddFN39jW0-_uEzHQyWQF9jI6f-n6DNunruXAGLu5Gt_WPp5e6eM8xaSeVSBz6HtkiHwp56N0hs1nAEmeUrRHDYfwQWDBHpK02u058KiG41chDfqli6VsauVCrPbtnlhpNELsd1jyeIhoW0KxGYbu80cQZuJM2UOAU9jxhwN1QVkNo6B2VU2GA0iIXGBwFzCEAvdLOXjcWl36gvugsG2T673MTCbDVegvrkFEzdTo9-OmSz4C5wAp4fzGFSmIYrEPmGr3HHIx03CUhH2v73ZP4PzQnCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زور نزن مشتی جام جهانی تموم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82443" target="_blank">📅 22:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82442">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFXul_wA0CmTtUnrFEqNN70jpPjm4gZTl9aU41cza9wXRa-wfLU7DIZkT_IiJr2U-Y8Y8Ni9F1CA9fJz5ta7O74iYu_X9S7TmxpQ7qoWwnVmr_k-n023fe_VPX3AkIrYjwXkNIt-17nOJil8m7_c9pUMakoWGaMAwkRJreoXFJ8iQ74F6eDts9MzjAy4p4i3Hr0GUy23LUk0Rt-W3JAcJENhrgv8_J1XX0EKsiL1ZBBDCJYB-ijheL61n62WWpR6T9SMcEd-gvdpW28KhBGunNfrx5OUhz6RAiJvQaX3g9CmkVTYtr5VO3Ko7-M0plEWq-h2HDPznx67aOHb3rHbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخی، قانون اجازه نمیده کلاغ نگه داری؟
🥺
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82442" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82441">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnErfwqGdNU54Jp_8MvzXeOPs1CpepuAaJvG8YM4efPzMyiPzfEG5BYX-o_dfHFp4EMtiUE6SAX5Vpv2maZb6eog5IZtzEYuVv8OQaKHzeNeQFH5zbtXk9jPJH568zjBmvPyFuaNbxTTceD14Dh2PtL6a-SCDk1_gUlaz1QMBxqjhixIBCaQMsiZwIkQvXA8ED4L6uliTN3HGjgGlyEApIAobj9nK7l2N_UZi-_r63QH8NxL93ALIlGwtRH2F1PRHzzA5jxbXFOQWT3WWXO8sAMpA9qz6u_7zzELjkJqi7v9OqqIoQSdNTrJRb1tJfzMhXGU_B0txTWVZ42GEzSl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82441" target="_blank">📅 21:45 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
