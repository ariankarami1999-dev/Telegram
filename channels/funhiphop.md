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
<img src="https://cdn4.telesco.pe/file/X_-e6lMsEVsGECStl2MxiYm7fD5NtfG667xkgdFURD5mblanx61_mvDNFT9CHpF3cB-0FOLg9ebGqwSypLaBxUod352XvDqI3NL7SQMl6P5fHLujekxhCn2JeZ_DOtXkhTfSFid1dGKXZGcCy8YG_lPZWnuZ5qH9auzhJXZ-q8sQ15AVg6ZlxoFiwQ6g8xgWzZcyywBagCuggXckN-KxulGg8lEXbvUJPdnn7kkl6_yRYzyjpz-UL6z50cGhlFAL9IgYaqXxr9GVB_w0LUNbHLYa1VTxz-RQ921WUYqBeee4XdsHJmnGfmweOci7pJgVe0A5yedV9cnJfHaNp9z1lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ژنرال محسن رضایی:
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتونه آمریکا را اداره کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/funhiphop/76848" target="_blank">📅 19:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2HVN2cjqxebKmsMc-GalUwnJq-27Z6jncbRW19Rh979n38EmxTZajHOK9EEos9JYxqN67ya-ZvPW9kKz1Nit6ziVaMpCA-ZFzMlvEz5_UduuHqe-1bbFCyMHeZeEG8S_a5mzIoS63VrO3q197KqrXr0TJcvUyniY6gQXT9iibyECSS1hrY-uQwNCh_a0qpEcZZhDWUXBRlRVRYwk9zNuFGkTv4Txpm-GFr1wz_SbzoeMc7paxujzC4jE4S707CsRMi-0UiYbo_yAGYXuZEugwkgG1LSjVkrq_ib1TYSMXhe9SlSR-U0Bq7uAd_OPmPztyjDaIfK61ngLkdVn2WM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷ سال پیش در چنین روزی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/76847" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyEFqLZRSxyrn1AvP_N4GwsNKZd9sz6hDtH2R0LzGGsI5OD5jRYK_wh5oc-cAhjODNHyLJ7p8U4hz0TykGgE8TMTlwYkdkt6HMr3nbo77p_M5mPA75EhNLFgyHKLOCTOFyBWafVaDuqhDODiCN6g2wICxe_Eer3diyVvLabuBtSrzAJIz1Ruvqzk5SS5WyUeqOT-sUG-SVK_90taxo0HOJhjpIEytzgU0KEG_6axLxUlmT-B0xfTe3Eh5rBJ03KO0eoDclVufLczQwedM9SMi6-ikOkaf48JwhGbArXB2XJMNG9jMcpnbBq3R4WDyRKXtjIyNHp_PGYyARtBa8urjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/76845" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حاجی کاکولدی چیزی هستی این کارارو میکنی؟
- اولین سوالم از حصین وقتی حضوری دیدمش.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/76844" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=RfEsslAbvxdPzGSqCS9JhaGGl4KJ6K8m3UqmQRQrUElkTXxwi7WKY-fQZw2G8W68LnFUNWEOs5oF6nc5tkDR8bpXr4Sr5Ml6o_6rI3o3tnFVau2--cUGa_DinoTgBOUEYXZ1LzWLd5Oy_r-7pSHreLTgyiP7g0edGFtxWNzeoH6qPsItHwXrQiLdL2M30A3J9Bd-3vrFZH-Qq0-Tc-idF2AA5r5mNDWz5WaLqTWC9bAU_G4dKp7bxEK1A88gy5buqVYjV_SWmNgQEjo0IfeQfpsAYwJUyYrgv0v8j4AQbh7RivmMqeSTVsfaeegvoQQ5ySeR5iJExEpshdxLLk3Adw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=RfEsslAbvxdPzGSqCS9JhaGGl4KJ6K8m3UqmQRQrUElkTXxwi7WKY-fQZw2G8W68LnFUNWEOs5oF6nc5tkDR8bpXr4Sr5Ml6o_6rI3o3tnFVau2--cUGa_DinoTgBOUEYXZ1LzWLd5Oy_r-7pSHreLTgyiP7g0edGFtxWNzeoH6qPsItHwXrQiLdL2M30A3J9Bd-3vrFZH-Qq0-Tc-idF2AA5r5mNDWz5WaLqTWC9bAU_G4dKp7bxEK1A88gy5buqVYjV_SWmNgQEjo0IfeQfpsAYwJUyYrgv0v8j4AQbh7RivmMqeSTVsfaeegvoQQ5ySeR5iJExEpshdxLLk3Adw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آه فدایی آروم تر
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/funhiphop/76843" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=X8jUM5xjl-xowR1IjQ8aD7DZ_lOCuhYI6SMyrnmu6aeVcAkgwE0wDglW8U1LwO-whfgO78qtWCKnvnQc6f7D3PsrHgrXkF9ZVDO0nyUUyNJ8iHzLLuI30t7A5h-9MxgGmidRBrObFJ9HYnYnjVl4Ktr0MnfOUgTjAsb2NhHdSJgM_AWx3ZXoa-3VCnMfUZpAT0gxYmElDa9wB10QLL5V1lYf2RaeHxbmS_WITwDQL9u7B19h5ixE9Ddgh2RvEm6pk4nCJuEIAN2Axilwujq-U0bizT9DCtfRiFYRpvcSAArvHGX774Jnr6Pcq4QZVAQmEYt_CZddj4kjU9aSG1vyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=X8jUM5xjl-xowR1IjQ8aD7DZ_lOCuhYI6SMyrnmu6aeVcAkgwE0wDglW8U1LwO-whfgO78qtWCKnvnQc6f7D3PsrHgrXkF9ZVDO0nyUUyNJ8iHzLLuI30t7A5h-9MxgGmidRBrObFJ9HYnYnjVl4Ktr0MnfOUgTjAsb2NhHdSJgM_AWx3ZXoa-3VCnMfUZpAT0gxYmElDa9wB10QLL5V1lYf2RaeHxbmS_WITwDQL9u7B19h5ixE9Ddgh2RvEm6pk4nCJuEIAN2Axilwujq-U0bizT9DCtfRiFYRpvcSAArvHGX774Jnr6Pcq4QZVAQmEYt_CZddj4kjU9aSG1vyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/76842" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اگ دنبال یه سایت با هدایا خفن و کاربردی هستی اینجارو از دست نده
🎁
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76841" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SttY_bxDk4CZii53zrfIZBabEkR95Opn-oOXl9f0xpDo3NKaW91gcSMoxytAYet5S21DrArcQ2JAEipeF367cxGNTmPrRw75dl6BKVjl_EZaxlO26uDTyAXirTcwn3jIrrYmagXVQdDVfsaezK9c1-lNr6JtknCccCKAXR0isWiqF_32WwfwPxFVtH8mMuZuFm4s0rV3QQEWAZXJ4aQSdH3Jt5aUZUffgRe7QgS8UUHHGQd-A7AjLRXLzH7Bx0nvfWNe8BjbIRFuIctxt8xjJLUoRMmovrKD5fQcrrlUY2OtYtqjfP1BfavnssFfaSnmC1dp26u36Gkyvbis-FXY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g14
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76840" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPTFunUHtoHcovF318j51xl5aWK63mSi33dZfNOy08M9ESFL5VfjO5FpguqPMKEAwBlRaevup2IKuTx3trgY5MXDQ1l26VTxi3GrKUCuI37buDqX4BOvdp3DrUksUDC7SpH3JR9nm8Svihaao1R43DkL6GSelMR-P_wS-CeT3fOj_aUtNyEqI7xrM7cNqCfiVwzQLQhK8cWt6-wS_8H8PS23w_m6EFPSKIojCfE3_6pBD64WFnn1prD-660npPAw98fTN5ojnllVSvvBuLHxFFv2CncmRperp9iMKOS4QpS9fjgXZ8dGgNnp_BdBQutLuKUNsFacV499iotyriU3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Xf9cLy19eiFf1OFx-fTVtxBMOr5cqf0R7MGYvCvdpnJYj6SKBrWsv0ckGze3mY8IVzZIjxXXpVsJLWWCQ-4W5E27hEnDiB9FQHSnUuJyart19SAngrX46kUjk5EPBNEd8Bq9cem37JoY-OYYydZpuTWZikfkTSEOGjZDJYcrEHcEh8zv1dJNEV5KT1qX1JbhfAkTJWE_-OQVrYBDUzefZRfWDdbTxpzHl97DHOHaNCRs9m2jJHJc_TwP16Ab-Mmu1gy4FPHy7beZo7A6Ui-wC619ZbXlhKEwQpE8fqak26vrK157McCxMKifEPnR4s9Q8rfE7Jvm4gmZlEJ59g5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODODr8wZNL7nJnqRWYkVfKSc-FmsL2MOP0EX6jBAwGOKFmo8rvoAvdawkYeryfK_tTM_W43OXTAOwqsQZaddPq50sqKVPNuN7K2YtLBDfXp99n2Q7NNFXDAW9FSNOXFOtjRjoTSaFI0dBfz0HIckNeiKdtz5yzPyNdLZOYBJXNXZVlpuqwL0T8uxblp2aGcYEQNqr_OV8Jck-mxyUWaIjaHk2fXa5U5KiBKRpCfCFX6jwlQPDUIUPRk6S6bGqiQhrAE6aEpSkkDip4G_m1D-RXTbvm2q3nYVViJNnH2QJiBf-ggO94ZH3vzUR2ztS6E0Hk37FKs2m84N8xXWah5tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaIYLhCAoVa9XSeiOWSsWjxybpubAGeRVW4ZPiDUaxmpU9W-cbL8uVHwgfMeRwgwEvX5caNsAIaKlXMB2MDkjY970SedveTGwEp_vxHVYzOsNv_8Xs2YHWPgPv6lk7CPUNDlFuuA9OK4j7gsOx5pkdyDt9BvXBbHatlKQv5pey2ZHVCw5aGFFP1HOJai5sphKcpvlsK8EJ_HKI6asLhye0fDBg_yPUTIFqCdZljH_HESC_gmdtmZof8lSpvOeqSPO86hobjI-Ckep4hOfxr3oAugwqzYjNd6chOENyPYI4YI9znRmDsDZL9vEvEQdaNprqgSijc6EcintB_QXCDkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBrPE0_RJwZ14XHWl-3_jQ27tXn6bmdXzV8l2n2SxhdnSGf8tfxY_Urf6oz6BzUSEEGc5PamiYxhVOMCi-FUMCm1TYom5G_Ot0nR3-Tfpa6mh5KQyxPSerpnZBpMGHDbf49a7N-JKfmvLvDkFkppn_UBfvZkXVVPlK6HhqDBpBVPyaztLrJHZeT8znEWdxjOVQNX8Gk_gHxqR3RL9KNu8j0p1FCTXIokA70YrFMG4cT-_5L0PnYhwC_2nblbVbsXwzEtm8jxlG1hx-IABjbIcc5xDaosishvQvRid6t-ctxln0V5LkBj7mLQFRVAdATSLFwJOqnafPBRaR_cMpPrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=cGHxY7cnILd0fr299QqMf0EvEnqllYYwOi_8bq0t93Pc3Sn2SvMO7MJL2CdlMMrHa-pmzzLOPNyiuE1zQNPrzqdTXinxTMQhDT440DXB3sCSPItu3yNKfoAEYGlq0k7tpjxXQvW-t2acAh7owpGy_rZUB-txkliT_fvphk3DDQMF_eKs0QVleUdzm-75sIjBzOjH0XxaP-X0cPreGe60eT-46ex2deGab-vNHULruymOLTyczRTcBENY4mndpKWY7Gp12M6zb0nta1dewWjYwOmJ9jpWr0euTQVVo1jG2lr3VSapLbMp1Yv3cUTIQkym9rfd6Y1IIUMszSLpY34DmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=cGHxY7cnILd0fr299QqMf0EvEnqllYYwOi_8bq0t93Pc3Sn2SvMO7MJL2CdlMMrHa-pmzzLOPNyiuE1zQNPrzqdTXinxTMQhDT440DXB3sCSPItu3yNKfoAEYGlq0k7tpjxXQvW-t2acAh7owpGy_rZUB-txkliT_fvphk3DDQMF_eKs0QVleUdzm-75sIjBzOjH0XxaP-X0cPreGe60eT-46ex2deGab-vNHULruymOLTyczRTcBENY4mndpKWY7Gp12M6zb0nta1dewWjYwOmJ9jpWr0euTQVVo1jG2lr3VSapLbMp1Yv3cUTIQkym9rfd6Y1IIUMszSLpY34DmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0WBXw4-eG5s-jZrIWFkfiumy1_7Hu-uC7oNvlrDFdwpvVxaUXpTyDcPb0g4wzq7-HXjdaZw8q4zJ8XNVhB3xDDNajjEb6XAceeJPG7N5wp14cEIcPFsYK632I2yUh_Cjqhx_9yls5xkFzNLw_ky3nxu-YQ1KTSGh-GvIyqVcvb6iIvFcNlySdNIWhR26EIKCER4jiZgXekqdM6I2GW0fsPrg3DBhD3uBl0mU3TMOlcGI3BQrA8ScuiAa2XcDt1mAUEKtp-uy6WgkK4igDEuvaAIwBPHGs7q8BexfK0n9SEcQYw3LW1tUL4FZXVtoO597lIPxFklU75pB0-zgI0XdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76808" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqXxDi9FwUwbz5BXkt36ofYxRpVzx5etwmIF_UAPVVGKcaZHCVj3vUrHoGttuIQ8_U47A6oGLVb3yExupdihgnj2DDhk2pLgi_flsMhaPH5MMBv1RRqIrS2ryWACeQY2CSVO_tP7ePH2twoenE5FdTbKJVRS9dCvs8J_zHSW357RTuPlUlOoRVYGMKv2Pl4EbG3BuM5XjgQStko8K7lQSMIYOLR28y1CE4pQrPt1oq6OCQpLKfw13LZ_PvMTy8hlcDUnWtnQw26wjsXxcR5zvAa8G_Q4Jdrxee1SOaFAv5Cxt6BMFqqvcJHXMzvrN_l18Q3ggpVQC8hdGPNfdNmizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
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
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r14
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76807" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=neYLAU71nUGsyGpwwTSwYbiRuvaDAYutKzFgHAAO6y4MBJ3DudesnfXdPEtR1rB2DStDXF6YRtqtDh5DuFC7UnH0Og6i4mOMaPilspOKaidO_309xU4_naTjf2XHXtuR3c9RQCs4zWhkPmJPnEgaUSY5sxk1njg7iGjt8moxn7fuIjoSl2CSs9ZsZygIQGvRStHQGclF3C29HhvD7BTPSLtExBF0BA8dkU5A2x_oOX1wEaK_zoFvFKJcaCyjs0Wgo88DWcVmEWoIQxlqakdeiDwvXc-94cp_6XxGC9mhYU9gQ_-dGy8RpV-uPgmmDJ1pDPn_tIRWKijbigUhWSFaPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=neYLAU71nUGsyGpwwTSwYbiRuvaDAYutKzFgHAAO6y4MBJ3DudesnfXdPEtR1rB2DStDXF6YRtqtDh5DuFC7UnH0Og6i4mOMaPilspOKaidO_309xU4_naTjf2XHXtuR3c9RQCs4zWhkPmJPnEgaUSY5sxk1njg7iGjt8moxn7fuIjoSl2CSs9ZsZygIQGvRStHQGclF3C29HhvD7BTPSLtExBF0BA8dkU5A2x_oOX1wEaK_zoFvFKJcaCyjs0Wgo88DWcVmEWoIQxlqakdeiDwvXc-94cp_6XxGC9mhYU9gQ_-dGy8RpV-uPgmmDJ1pDPn_tIRWKijbigUhWSFaPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=TUWFDDzA2EnYLaRrmV6P5g5Z0eqi1k_2gZfc8BGIkq-lVGoux4GwrO_6Y6_0H-ForZDqV4mettsgB6t86VTuJU5d0fJiwMACDnby9msHnrSWFWrMwuMFqd1uuF5ROvxN-b_nNQNiGyVAQrfgS-3BrgopdBE5Vww1eP2JY4qnDKFPTjYrJCyUUkL0FaSc35z18SiPfgmHCKZjNnd0vTkabgFs0mvSyzVZXUPOVtZnCXxwZ-uV0dYWZ-_EJoI1MPFlYf1wy4vOgI3_I2paS5OeqY4TVf6fCQ3RpVmIurytZL90lqqLQqGAyNCdC9PgYHFSYeaRTE1DuJN5xw9qw0nm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=TUWFDDzA2EnYLaRrmV6P5g5Z0eqi1k_2gZfc8BGIkq-lVGoux4GwrO_6Y6_0H-ForZDqV4mettsgB6t86VTuJU5d0fJiwMACDnby9msHnrSWFWrMwuMFqd1uuF5ROvxN-b_nNQNiGyVAQrfgS-3BrgopdBE5Vww1eP2JY4qnDKFPTjYrJCyUUkL0FaSc35z18SiPfgmHCKZjNnd0vTkabgFs0mvSyzVZXUPOVtZnCXxwZ-uV0dYWZ-_EJoI1MPFlYf1wy4vOgI3_I2paS5OeqY4TVf6fCQ3RpVmIurytZL90lqqLQqGAyNCdC9PgYHFSYeaRTE1DuJN5xw9qw0nm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTqDSJ7S-x338Boiw2vzxehd1b5fq9AGe3-E7P5euhPkOwbDJc2HxF4AYcTKtZ-SPVz1EZx7rcMmvEMF4sCythx7cUEfP_oLNeJpDFJg5eGB7_yzApZckjmi0UHxfx42vK0e5p7f73Z9uMHTBs7t7uHR0DK4iAVEk2cJG3wR8FOMc6S1lKQjTAaqDO9s-piU00LRJSedDHuJcI4tg1vl9B7_0DRfUZ9NRWoK5_h4g3MYb6kMDEE70Z2YF45uuX3Vg0L8er7ilVW5HDVV98cwjUHNi-4363MyJrozAStq6VI2YFmkt1lzT8fY8JwCLpgcUAx-U-jY7tbe2hdCvcwPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgV2tAGrDatitFclEldcxdt6KAZPKAcr1FSFX1oDzczfYEPPcHc-JFFbr3daDSe3g9iSv57XeR2xAwAPPd7Cx4hqvmiiZSmJfLchQ0QhPo8ciUedwQlB32yzqSK3t_L8Ed45hv1DA8yhR5XDFUopu3KFBMXoJqwx_Pz5opWfvd4OyuK5CwL9LbMZj5cAPvPRU-JBa8imwGaJjY_mC6yDQtdmCwmXZBDeNBP2_9AII7k47hBAcfKrVGGUWzQ8FWIHT1EpwmE4ke4UXN3vTKtiuvw137OoajcsKzWCaaaoVQiqTjmkcgA6nPrPQLLaXd1IJR2FGFjL00YSVxa5NDlfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGjawiJaJXfmIOYUV8-UccOWjD605O87-onMkMpmbZ0hO6IZdjmJ0e8h04s5HCIBmV88mOfzidmJz5m8etwp8ss5Q9ChmczfCttrZ2Ls7M1iNvJ8modklRsw3fCUI6br6E_mKO2a4G27dMc_rL3QRTXFFR8zua7CJqqiEc1_RL7OyYB7-4fjZbxqJkoL3rxldOVIsbt6TrDHMP5yrDIgE6KpDWXGrjrjt69UUQ1JrnKnssmtAm0BTiQdKBVpwEmQ3BVeh5yVDbfP59wFz5XmFKiIM59khFR1mo11pmM8hNe4CzO0ef3FqBM4cCqW6yczO50j44tDPfUdnoRqH0RLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=aZA_UqoQTSL5_8XB9BlQobmO1QCjcON2A9wmtSyWGD71D00EZsAB2S5l4b2ikhqOwpjwg8WICCuwNvYto7urrNkM0NmQ_dHVqbij1TD9XGh3mn_nhFEenCunAQj1VS8V6NC4HhcLa3HTMrEjkF91R2ukdqG1n3Or1W2D8JY6AamFKt4MDTEX-IsyblRTCogtVXmDYirZHupY9na8ICitVtfJK350LJcwSpEbK0wBZjSbIj0p_esDnRVw5SYYcx42r2MoImKzn7cxSmeO5_LLskFlGOqaOneTzFK498Nx-Iw5QjmWsO5xUcWcSdLrP0kEWgNPPuMlU9g8mUJ0_5Q1Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=aZA_UqoQTSL5_8XB9BlQobmO1QCjcON2A9wmtSyWGD71D00EZsAB2S5l4b2ikhqOwpjwg8WICCuwNvYto7urrNkM0NmQ_dHVqbij1TD9XGh3mn_nhFEenCunAQj1VS8V6NC4HhcLa3HTMrEjkF91R2ukdqG1n3Or1W2D8JY6AamFKt4MDTEX-IsyblRTCogtVXmDYirZHupY9na8ICitVtfJK350LJcwSpEbK0wBZjSbIj0p_esDnRVw5SYYcx42r2MoImKzn7cxSmeO5_LLskFlGOqaOneTzFK498Nx-Iw5QjmWsO5xUcWcSdLrP0kEWgNPPuMlU9g8mUJ0_5Q1Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbSPRSNC7tLrcG6H6V33TMo-XJZ3HcPn8mPTrNHI4LgmqnWlkM1hggoG_FQ9H65G0tLsmeP8ghRPTubG0ggVIgDrYuUz3WAbiFGI9llelwmJViD5XBWhfaE1jwLN1ispPSCi-0wX_9Av4EqVrsSySRtEYo3RwDn3L5cLdCq9iSWdcMqAfQUyW_vZlf1ECpzH1RrWyBGVJMsMIrevRs6byiGkCr4oqgqaq49d5JP_vA4CvBq0mW45IiCAg2eHgFOVZVJWBqsGUY0f5eAS-FOwka2gBnFkMP8YyEoZR5cn-u8tEycDzORsdu4FaNfgE6cXrO_-LDjmkjNfLx_Wpp1JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=tGxPZWgMaoa6FC6AcnF98xjIKFuKYuRXOIDtR1m52kfuYI00qZ9-6iy0wW8OuTOjAvNoSHdy0zppJd2aQD6WSPiZxq8uyRfdsj3MKjUlb9MEd7DtMQm07155iSx8tqpcX_WdXhOLG8RXrukme0-hh8de10cO7IPAiZjT7NT-w6KdZABoRS9UbZ9tVGmZOxqxVE2nmmljS7sfUXMPonJlCrAdaZGfRKseV0AdaPB8bZFPvhyq2vc62IV-L2J1WL30rTj1UISyJREBpHz-dE3tMOxiYJXNZShMKc6sAxnziROIlx_vtg3SWaMDok3LSSABmGbv8U6_JceemphbSy1Cdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=tGxPZWgMaoa6FC6AcnF98xjIKFuKYuRXOIDtR1m52kfuYI00qZ9-6iy0wW8OuTOjAvNoSHdy0zppJd2aQD6WSPiZxq8uyRfdsj3MKjUlb9MEd7DtMQm07155iSx8tqpcX_WdXhOLG8RXrukme0-hh8de10cO7IPAiZjT7NT-w6KdZABoRS9UbZ9tVGmZOxqxVE2nmmljS7sfUXMPonJlCrAdaZGfRKseV0AdaPB8bZFPvhyq2vc62IV-L2J1WL30rTj1UISyJREBpHz-dE3tMOxiYJXNZShMKc6sAxnziROIlx_vtg3SWaMDok3LSSABmGbv8U6_JceemphbSy1Cdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=DH40ckkYl4lfhzwQ4vJ83vA_0voPoBY8_xm-p0X2B0kbr3zI_HXbSpVqxaSYXQtduK4GdDqiosspr1GiJj0GI68OD4kpdh7EpLEfobxMm9__flZWU-S_2qCPZeIHY93IhzKGPvKnMBkBKivOHKf4p5oEMBGkAAmQLV7Hkmoq6x-G-7j4JwdtdGhQcR3YJt1Usbq-xqyTNWrsYaHwjaCL-faulPoMfpa9h0BwVJy4Edj5zLzU_AuBYZFwPqWb5zachfAxbthMPT46zluJkq2RMgDboVWBDC2Gp_axHTtJXz7YUCmAe6mfw7edP4hq0bGNt2EVjrVH1gHtlgAHs-hicg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=DH40ckkYl4lfhzwQ4vJ83vA_0voPoBY8_xm-p0X2B0kbr3zI_HXbSpVqxaSYXQtduK4GdDqiosspr1GiJj0GI68OD4kpdh7EpLEfobxMm9__flZWU-S_2qCPZeIHY93IhzKGPvKnMBkBKivOHKf4p5oEMBGkAAmQLV7Hkmoq6x-G-7j4JwdtdGhQcR3YJt1Usbq-xqyTNWrsYaHwjaCL-faulPoMfpa9h0BwVJy4Edj5zLzU_AuBYZFwPqWb5zachfAxbthMPT46zluJkq2RMgDboVWBDC2Gp_axHTtJXz7YUCmAe6mfw7edP4hq0bGNt2EVjrVH1gHtlgAHs-hicg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trtp8QKfhh5PxPxk9Sgmm3yzGg4mUZzizcelVJ5U33GiPY9M1t-p4Yn4WVHLZY4izPwvh7XgRfm-AZ8VxFXz08ZyH5DeogWJBAiNEt7hJNZpcUUrVz99ntJjzGA5mH7857ActHVonQtgquybSSmnkPlO5DwqLYN8o5E2HtekxUZ1ZSAJpVx7cGTidcxnhyMzSVznpVAAA2wlcBSppepo8wdNENt8Zs5CCeG80KdsSBkG630PO7QNUA-soCFzsSsTS3-LvxZ4jANbaTOxboWajiky84yI83SaPcT_VVOJ7xvI25BBS7BfazQumKDhwmNpXX7XD2iZxNANph3TCbf1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=np4wXGd7MV6_4_hJwUpPzvi6zu6yJ3id2aU5Xl09V3VEDlslmSYCt1FwEE00lWF8Z6K_cV0VlNZI2emFVwDnXBqSie4nqGo5PB0I6_msqXWwoWYmcT1yvDNwdKptQTGte1WOKt1V2BgniPsI95fSdQaJo0DrpQdkx22LltrYDohUVNHcFMgp3dRQo0lzdIzEzTkgdi1w1F2rYzS0J8v5JwddcOlRKxzCVUxXaBAGzQY_SvwDAvKwiKDjvl1eedJKLFWjm4D8BORezyccn7KJufiwBb-ektj6TgGh3A1aUBDVA4SSlXvKQpMSjSJT5rJpvnoeF9WuxQ3NBzPw0Iavuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=np4wXGd7MV6_4_hJwUpPzvi6zu6yJ3id2aU5Xl09V3VEDlslmSYCt1FwEE00lWF8Z6K_cV0VlNZI2emFVwDnXBqSie4nqGo5PB0I6_msqXWwoWYmcT1yvDNwdKptQTGte1WOKt1V2BgniPsI95fSdQaJo0DrpQdkx22LltrYDohUVNHcFMgp3dRQo0lzdIzEzTkgdi1w1F2rYzS0J8v5JwddcOlRKxzCVUxXaBAGzQY_SvwDAvKwiKDjvl1eedJKLFWjm4D8BORezyccn7KJufiwBb-ektj6TgGh3A1aUBDVA4SSlXvKQpMSjSJT5rJpvnoeF9WuxQ3NBzPw0Iavuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=U3MbY9ev1wtjPwaT_ZBX5BKXHGegwhKazWsKxaUw5KpooGp4L16_rQNKCk6FamCPzKtAoAP9GZlHM1d1Rm8yBTPeOzYEoEEwsiUTsCPS5pYa1yF6L6kEobaDMzpISf_qlc-30M5qTkGQESvaozumLLDg54X508nL4XZtKebIyAPrMQJoEDGVTMsKC2eos8LSaVHAhuLkB5L9zNBUfw6WH_554wSAfSf2WVQyjfhrlb41aMHXSxpaOQI9y6Qv-cghUiqRCPiiNHh2aeRkBEwNztL7uqqtRRyNx6rV2soE9Xwa4VeUUBbx37u-IeWZNVP9GCnBHugueIGXtxV-Uhf2jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=U3MbY9ev1wtjPwaT_ZBX5BKXHGegwhKazWsKxaUw5KpooGp4L16_rQNKCk6FamCPzKtAoAP9GZlHM1d1Rm8yBTPeOzYEoEEwsiUTsCPS5pYa1yF6L6kEobaDMzpISf_qlc-30M5qTkGQESvaozumLLDg54X508nL4XZtKebIyAPrMQJoEDGVTMsKC2eos8LSaVHAhuLkB5L9zNBUfw6WH_554wSAfSf2WVQyjfhrlb41aMHXSxpaOQI9y6Qv-cghUiqRCPiiNHh2aeRkBEwNztL7uqqtRRyNx6rV2soE9Xwa4VeUUBbx37u-IeWZNVP9GCnBHugueIGXtxV-Uhf2jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1VEGQsDRh6c91qdOhDv0sxtvDrBz2D-0_sTC-kX9ri-Kv74nMN7GEcstBJ4tecLfCZtoQUyXhtiLZK1AMESC1H_aJFcINgDX4GHBv2Bq7MYKnh-CVG-vKTg2QPTjLG7c0H5OPtb5bbOS0ahc9qpwiagc2eImWOteLtOzWJncveBEVSNcqk7PIxhoUn2Rzm6KnaM0jICO4mGzwsbGFTkrSNZzj2m9cB2OceTDRt7hkEJPwzwgL0V7gTzB2AiW7_ouQ1yZB5cKZblykD46-UGnPGuUjvZqpCqY_UEZwPpOBuZ1n7rBn2g6_RW9gDuKExWJS9L83Z4qvRXbw38EYOPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcCDFTx4ta_vIvym9Li-wCzgY2RecMMsw00g8zFbHx7EwiIwOBy9CpRV7UzVlhjXG8KGV7g-Zj0ddVFPni4cMF6JHk-kZYf5KFYhAafH4CQGtW8qxc5dJi6o5TO19L33fYS85RF4Bz1FW53TI-l_immYPB6W1EsRjdlbdaQlcULFTYarhsFPCjVvO_6kdNNSWlEOlBf46uAkJF9s4VSDQv63Y8PI12DQwCGASIR1Kw5GEuE8wkwJC3WYdxa0cbE1IJosC2ySIjoQ_Zk_BHg4qKh8vk6F4SkHbqF0b7IEcUMWZwYE_OO_A_AuU9Tz9yRnX9wXUmAEHcHhdWlzMPrJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJO9jCP6AfD7zb1rLIvIN4pV01CblX3gjMDx9OGlUKCqkUHtVyXSuD8bhOxM7_-ujM2fDeZZ1WvkAPg5G-FEyacpEF9E2RDPranUNnDbVg80F11bNLfirkHwpbmTUmqN4LALXJ5Cap3aJbjx702K3hMDeO8-4TJ8tBaBjTIdKprO3Sp_r9QgFhpNRp1Wkrt81cASTIEKQ9tWbxqhq9DzefLcqTrzHJs1IQIp0-8AGj6zTbmacDZVZpzGcMjG_aZtqk2OZlz7rJH-HotmTeCrkqTVW6BR6XnH7zPe6Ufe-DqcwcHEvQ8VqTd2vvE0KwG8jbU2GqnVoBI6qLJna7jAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWlHIlzqhqaqESExd-prqZAb28THjS0dWgy4wKva7tLfOEeXEJjDT_ud0Ox1XR2G0gUTio0g-ldnTRnN2ouKg8XRz6zVLttaN9bXafCX_DtcAHEePHGMRdXF2HCt-hx4eddJMDxJSBgjiq-zxxBHYH_bGNOgbDv0h2bAQ4qcvu8LENRz4qAeCv6zOVGq5BA2B4deJMrkes-Lc_VbLB9n5SqolzVpbsPG0eqBQl2XGSXIKUZ3r3jvE76sNeHpm3jQ3s0FPVUo_Dh5Xtuc7FhqpAacX39SImY5WcV0LfIIi3ALXZaC4T32ZOXO0etekTgEOTFZYGdmOMKWgjDclyPJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=VGnvzsO3b0wXOjmiYwIprUpVBxSw06LqExnJgpu3AYHHg2J4ZK6XSOPguTfgiEp55pefG6Y-kHEHMLwg0LfHWw_CL4QlHVrFxHxCh6GXt6F5wSg7_McNto1UlQ-DFWTO1W5KQBMedwG53wdUyXcaMMkDTeaAHwOtdnnVhtoPhIT7UI2aI3BXWpL9ehd2u511ZQvWhe0148zzDSlNzOQrVKFG51xxhdSLWfubaHQ9ap3sDvfRubAD2hvhPJ1FVh6xSqK1zxo_b5_qVUcpOR-Vau34Z2BYKYMkbJXpWGU3d5silrVoNdcSu-sGY8rDZ5ioVDAmH6A_QQPCMSqmlfLB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=VGnvzsO3b0wXOjmiYwIprUpVBxSw06LqExnJgpu3AYHHg2J4ZK6XSOPguTfgiEp55pefG6Y-kHEHMLwg0LfHWw_CL4QlHVrFxHxCh6GXt6F5wSg7_McNto1UlQ-DFWTO1W5KQBMedwG53wdUyXcaMMkDTeaAHwOtdnnVhtoPhIT7UI2aI3BXWpL9ehd2u511ZQvWhe0148zzDSlNzOQrVKFG51xxhdSLWfubaHQ9ap3sDvfRubAD2hvhPJ1FVh6xSqK1zxo_b5_qVUcpOR-Vau34Z2BYKYMkbJXpWGU3d5silrVoNdcSu-sGY8rDZ5ioVDAmH6A_QQPCMSqmlfLB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSJHDkKLPF762PCTy8reDud9K8-kOhZGnj5JUEirBbYYyo9DiTB455tbC_5acMI4jbS5IaHOgRnkxW4AY_LOAZHhpDqq2vvTOFlI0h6v23l0AUGar0bjkvypWzsv9IztDv0ugsYy6KA5eGUzHc_P0Z8ZyB_LQaVNx3s9xAk0n47LEJTiZxn4PypNf9p01fzRXvfgYvU7n4jaCr01HB68lctbPuv-UfU8-v3HnEWUyLNNCRjIpE2DGofkiG8FoIRzPFqb6BC9O_ZVsU75dhWjQO1AnD3Wqw9R373enP6Yb79ijRqv9UIzOgDN0wr3DSFm0qh1yJeTJxuyiq3TuSZKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=ViRdZxS3tlQkPP__kG5N1uJBKGKX3c_0969vgeLVStkMOSvSltyJ9qTHR5ugNigNfTMvHPar3yvhjB8seOQwI3cHiWuwsz1RLTAIKxF_xqDtvRwdIBZv_-mAVDZ3PTqiMCwr-OOtgXWpmPYlRaiGQtur8sqATBH6g4PufQlEws0bbW4KociGmzH4-Zb1ylk4L-dqG7MPPB4UzB5DGp_z0x-V6zka8bxaVOrok9BPf1Y35ajLRS7hgQ-yoMRc0_vRDJKy1w0jXT0p4nYjlG5JSBWkGDl90ifgZxJLcjJUEyEeS2pGZMjJhJeFFWyls2ibliot_48xOnjrvBWjh3WPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=ViRdZxS3tlQkPP__kG5N1uJBKGKX3c_0969vgeLVStkMOSvSltyJ9qTHR5ugNigNfTMvHPar3yvhjB8seOQwI3cHiWuwsz1RLTAIKxF_xqDtvRwdIBZv_-mAVDZ3PTqiMCwr-OOtgXWpmPYlRaiGQtur8sqATBH6g4PufQlEws0bbW4KociGmzH4-Zb1ylk4L-dqG7MPPB4UzB5DGp_z0x-V6zka8bxaVOrok9BPf1Y35ajLRS7hgQ-yoMRc0_vRDJKy1w0jXT0p4nYjlG5JSBWkGDl90ifgZxJLcjJUEyEeS2pGZMjJhJeFFWyls2ibliot_48xOnjrvBWjh3WPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inzmzKN_5kY8Ni5P0iahCPSzfXFkAhbTjphMtKntva4S28txAqoA99Lp-jF9eYQNoksgawvDlgNmY_nHYxs2jj3tCBU2scmW_bPH_pFUrh95SJQUkQoK8s37Pfff9-ILk-JTilEJFDDFdweURH1nxs7amC6udGrPGoqIcnkW5zNF-mMbimwd8mpy9u9IvjaN3Gko4z78DLL7XfAXgVRgwRA04henatQi1y6-tgYx-YXKXCVlbxrhrHYifbMkH9OAL9lk_hpAMebdcguLEhA8D52URi46Qj45KQG6EK9WMuRGJ3bteS6GASUlcwmeREM_YjztLww0kwegFvKbsveMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=tMK3ConTgNi2PRmbPn7fFweKlIWiVO2YdC1fYJdshiytG1LHM_b9t8BfCE3K0fjNhWnpUKeqpWbeBMyXIzMygIN37hf9P_mheiq2KgKENveBrIMPy08olm2n-uXZZpRcRFz_h46cDg7sVRGo8q714ilewM3Sd4RR5UTjSNFII-z5NjvOOpIA7X0DtO8Olay205dPdEsdeeAbjco6n1aPGX9bJisdGoM-kPKY_klqX3UdeW27nz6I1vtWBiODdWmkOKFP1AEOFH4D-7Lr5OYn6IHQzoNFTtaiSQddb4tQvZKCCk0Ku1sB7bAGIeeSrXdL8jxW_bO-YSGHRX-nye4tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=tMK3ConTgNi2PRmbPn7fFweKlIWiVO2YdC1fYJdshiytG1LHM_b9t8BfCE3K0fjNhWnpUKeqpWbeBMyXIzMygIN37hf9P_mheiq2KgKENveBrIMPy08olm2n-uXZZpRcRFz_h46cDg7sVRGo8q714ilewM3Sd4RR5UTjSNFII-z5NjvOOpIA7X0DtO8Olay205dPdEsdeeAbjco6n1aPGX9bJisdGoM-kPKY_klqX3UdeW27nz6I1vtWBiODdWmkOKFP1AEOFH4D-7Lr5OYn6IHQzoNFTtaiSQddb4tQvZKCCk0Ku1sB7bAGIeeSrXdL8jxW_bO-YSGHRX-nye4tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ8GUQwMINeeTfNKJLluNsgNVkqUqW5uI-EvBXJy6NFmHNURK73A6uTVYVVMC7IUtsrcz3LqygsIWHy-wTm8tF7frEUgfwAJkVJP7GIPWuPuCTQwrI3oIRhhGyOdnTAQk3XUeVeulEJPH_r_wCA8vD4gklPDTuLEhyCX-X-UqtR9FM4xyNJPDRpN7Bgod3_J0Sl9WTFn3B9t1OmYG-4HvC_tURoblasZ9kmDDqCipkLntrB6fKqLVEf-A_50zSBeqr4hF-9_4jaRupi0o2gXmUwn_VHtMZKYQ8ycOiQdPxsaqv9kahhs8cQSAlb-_IEqFpVxK6Z-ZJIHTn7Rrq2Fbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSspIZmNPKHyp9r5_wmMq5obREnJ71YIEvnZScPMcNU0y-gzL8_BJ65XzbIR_P52_w8AVyDyTdoT6LqmCiiTfzO0bXn-Z0n0zJCSVkLvscVy64cKR1pjmV4cls_CVVr3Q7wLe86VlR1UOXpt7Y1W96TnrOAIWRlTEpFmq3TC_-IoSfwjVtRaMCjU3O9zWIJHxc79kFzHy-McqzhmCE17uZZ7ONr5LKlREv32KZUrjFK49z1fsPHVj2IRQYNTQ0QUX0cNygevJRZMx805M1Gau0UOR2Aynnu2jUrHBfmD9Lh5cQTRslWqJA9M5HPNnNLf3C68Zj6Q20hvaAy_HNh_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB6lfyrr2PPFh60gVTDsBKQwGdo7jIt46MfYggorgzeR0iB2Ykah3wgCOlpYR6Nw9d3TlCIDs7n_cHmO8wS-U1HnGP4JkWMijicGPwLRZyRZexD4-rD6Sf9bkyEWWLB1vM5696w2X5SYaKcXGN7BYl37TN3xax2nrcOPO2xECwxHgO0OBY0rogeWzbzHMPdCHY8koY7ecHDUYOkphGonaJxfcDFPAfh5I1ZBbSlFB_aPv_ZehPBvfKVz-t5PkayWkaFDS-jc7kjhRPsYE0PSNE9VX-em2eRu0LM08XifbSppSMYN4PF4Uxn_W55QIUFaP9z_c6PWVvcdg4g_Uv7_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLs0kadZTtrHIoZAu1vhI7-zbEIhU_ZiSLmNqWAy7Z7srMPWgxLEyiryXJt19TR49G77TtKPq8hqYNPjF0h_lgGSuxKWX0bEb-RilLQS1DrIRRjgPEcuDQhqL-oxPj5UQxbidmhS5vtyBYc-9LcOZw88NASXVj1G-u79lYsi0anFTo_89Wi46bZOGXJ7leOUWm7xpm2TovIh5JxAl0m2G_IXGzi63BJm1PAgIF7VsO42Z5qM0QVqvH2E6EHp8HXft_3cBV8vD4Dm6UQ-66uKcWp8Nhk385FMLZEVSfyjoez2WmaCAqwN7rrAKDmfWskD7ZfU8ITqWjtZKXVHA-SKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blUas8fwjabJq80OT3yKZ85reznq9n1pX-YujTSO1Ewoj0-o4Bo0UXPtXqU1yQn41S3BOjHKnAfLe3WVO8Cez7MtbJhpa7yX2WoNwpLrJdCymz_wN6LYgpgsq80254rrqW0c9ElwuDKR_FaCZ78if4nEz4y5IpYcJ5DSQHsQRwvS55funZ7eMV_4o-1IUSYlj4au2dRovYs16GEGMB75MiGim6bIiajsnMHKgMpjYK83YX8VAz0qVucm61RzYYkcyJOhgGf1z8lqoJ8XBI9py3cvathbt1vBXnfHkGFa8FJNFTCYWveDD-EZC5kPVnKxexBMw9mC0mxHf3Vv00eK2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
