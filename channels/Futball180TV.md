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
<img src="https://cdn4.telesco.pe/file/M3Lc7DoSsRsDErLymv2eIsiqFr-_gPL85YH40kXJqNX_gm43cwuhYDNtDqY0Kys0e_2tdj9cHK-ztXObNFAD4mF5SQ2WJq2SFPKgpoO4nvJ8RiUj9Slc-YquExwakr0g1R93qNo0qNBeT67ZV_Gw6VmDU9-Yx_Zy8t0Ct4rdczR-Y70LPWXXTdIS9uX8pPCqd_OUtALyHeR3cvg56eYq6oC6RkWxaikneFhYD5xCUNupUD9n_dHFjjsQNNXTuFnLy_XiWJviKRQ7eidMc2MwLVOQUAXoTGTQp37XaL9ugaetIUV_D4T6A6QVRTTZvCowEwRmPJ-E-bMzaFRgc_MBig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 137K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 13:52:58</div>
<hr>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVHAx-WURhZ2PXGipozixvhKzrLFH7Xsa8TEmj2XXuSDmao7IgiFlGAUfsB_Xs5FsPQ6uUvSDsVopbs-5XDVrlHcgqoIYU_43tsV-oy7fjzpTzKAwhjvUKjgM4yehPjbBVatcOxQfa2HUy5PDFfeSnbvKLqOME2Sh3dG_JJwobfSCJ7feeg8tj01CGTmhWoj5gaqE2mXtvCHOV8gzZ7ld921nYdP8tq85XZgBoNHgcmaCfStyrVp3UA0dU_I4ikllFXF8IQiat3SvhCcxOqEvflp60a30-lX3lIaAxK98AVpqv5yM9UPsDkStklfu1KqudJL5ym5oEuFmWzdv7K4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WON2YUveRHMBvBKeAg43Pv2ztIpMpctyRbj9XXgT8RD2d1GEWR9TmD73q-MHZ-uaedo0C7PUMQdSXiWIlqNBJSOVlLCL1jP3xZ2c4LA_XQc3a0azJACZ3LAfbN59MRacKMIhb2bX3Ggp3FgJYfzX70Jh6gxO33M5rQChViCMSnmSHcW-L78coRDLQQ-j0ZPoZ7CamI0AHJlG_TJGed41mmMKYm7NK3cZV_m7v1M3sIh-hjPdQQ6-I9CQih11jFphyP5lwuFARrhxe_SaXeByoEEuBeREpw6qKyTtwFRxkpVt_b3-nTFByXLSlwPfHlkysa9_UtJaO2Gd9cDY4rxzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amZ-Z_qPa5APz5eCp3Qp3uzIEuKTpu-pHs3rIWckk-SnYhIgAk5Sb-RcJoKz4FDiJh2DKQe6esn3Hm7D6KvDMzTQchI8w1zQ-UAAE0LFrKOC1VoQzh73n7F4b1Ro9aBgSrhND9Xm4LcDq_aDsP_LfyxSzmbaID3Lldxy6gmB-S-8zrcfNBUp82cLCrvVwHxNJpuLalhH8L1n2uzhQv50PZHtXaDyMBi0vkej8LAGzyIrRB73EmP0hNVIg1zvO2x_bTLDXg5AvZDPCK7D9b-HhGKhR8LMJLnT406aAgWhBUYDkxdBtmj_ggDycj9BAO4qtmb3bfxHz_GnrdnFvcNFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89899">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89899" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/Futball180TV/89899" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRnxuRGEy2NJbwmpwYldFbQK6LvcuOzzPpBONx-TfqYoJhBeUfEGEAarw-xHFhSPPBVSUKHuF8M4BCs4gUxEvP4E_mm_13D3uARg5Iv3VuoznCSFmSfTBnuW3Zvr1xHa-wwLLybeU4YUM6taNP9GQaDgo8ze7J3gdFVO_ucjI8-lWalr1Ocud9pjf-14D0d-lgKmHDcAvWlX63bh4BL226Jnyvx6VZnNAly6RRgFf3LSs5XLZ5qzYtYrtNH5TtSLv0gXp7UIXv6oBdVfWLdBV1Zh6RziY3rYyp3U8WekSMxBli4A-nNgo1TT4ZYqjuUv-U5BSdD9VrO5h2r-biURZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/Futball180TV/89898" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZOKYdrCQLGiD1tMR7u-37p1IIJPt1Et4os02yi1UEb7WoVSYCxw34VUKgw7jK1FtvYQrkbEI7JoiUcW695RCYe-VaRkuz26EXMJvN9KBocSQKqyZyDnTQT9DKG9UGYiuc0GDrdrHcdsTwc0YWnIuxz2AcajS4gIqIOznX5Ec9w-nk6Ao5YuGrTuwnPUQd0xIIPXeAbKeM-9cdAoFVvswTaRID559f54TNKGV-PDsYhpHmVZ8t2kvwndCXxb7BSt7n6qUyvVabcTKpXv23vzYs5I9N-F3tt9Ml9ci9_3EzxIoYx_h4WAMoBm5koI-KGSNOYRLv0iSxwa8G3ACS_y8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKk1ZSqCkdQ7gC5zLnwrRR40jXs38KmR3XB7dIbCLUlo7bvG2C9N95TWtcKRMY_ozGPoWF8-SUXPBKFWG0S8KO6oLr-l54pceB4UbKxrywHFGaKl2dmDiHb9jgqUBCELxpRkVy1UQhYzG93tuEPOVDXKnNBn8ptGP00DRKyCJTnX5FYB0qQvkwY59V8w4ZE293El316zK-mHVh1PKd_1iEhW3d4EVI0Cr-7QZGS9wovG4VPFDfKuRyqEb5mgS9Q92H7PQ_Kqn-5QXDloT8X94oaEI7jZgGiEQVsw5GCTQUBBVy4V4Pawqc46jLlpWMSZk8uiLNzwdA4v7IHyFU4LEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcmCMnbXGpkfGN4hSqSQAyRlv7j6cfcZNGcuUVD8epgyZsYVHtHSG_Io8GsGZ5e6FvzfoNW-wwR2elXUuSLNGaBprFRdNbdI1s2wmw69bd4XGYcl7h6BPK6QB7oPZCbx1vyvlZB5hxDNITOe-V83GO_kTc2QX7uzJSthYgD8CJV3Q1XNTdiqR_CXT3-0MaAFfDMr2b7zFSJ3OSrOMnza6iswMVXNUB0z1Dp_lmey6GKLUciBXjSRx3TGLgoh6NA9vVqRdFrVPcwzQ1IH7DNtaEeVnZWHJsMyFXq9AYUJAx0i7U-_SfOXjkxsJyaSygC9TjZIOFinnBK3M_h5ttMLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=KMpm5gdz_lVuDiMSxYA0OZj4tmnCag2QH3uWJwt9KeXyrsuTNmIA-DAWRJzdKKTOIjd6QEfqTpHEPvQMvFYcW_PuCBQF_J7m87GuDykzqEVUAhBVV_ar4ZiZW0LShSILshP6TxOlldpYhz17V8uAiyXh_bh7CrmE__y7JBo9-7YaF-b0yViazUcBr1bOJWAEIVVkiuLj8Hn57-ZwM5e8e5PUn_fZmrkaTuPL9Fh8D8XCwBYKKlnrVteyN_l00KfW8lCnOxZbXr_siO5e5Rzqht6LGMg5sKnnXKqod5jydehmUH1RVo0iPWzFG2urnzeNlXMw1hrGL9KA_KSkgBHImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=KMpm5gdz_lVuDiMSxYA0OZj4tmnCag2QH3uWJwt9KeXyrsuTNmIA-DAWRJzdKKTOIjd6QEfqTpHEPvQMvFYcW_PuCBQF_J7m87GuDykzqEVUAhBVV_ar4ZiZW0LShSILshP6TxOlldpYhz17V8uAiyXh_bh7CrmE__y7JBo9-7YaF-b0yViazUcBr1bOJWAEIVVkiuLj8Hn57-ZwM5e8e5PUn_fZmrkaTuPL9Fh8D8XCwBYKKlnrVteyN_l00KfW8lCnOxZbXr_siO5e5Rzqht6LGMg5sKnnXKqod5jydehmUH1RVo0iPWzFG2urnzeNlXMw1hrGL9KA_KSkgBHImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89893">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/Futball180TV/89893" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89892">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/Futball180TV/89892" target="_blank">📅 00:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89891">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drDYKRxa9pzjwmmCherLLaxvLAJPyMwHHRrgXafYImFxX6VDYJoLzDolMk1BVGLWoqRd9paBjOB4Iv0FasfvMn2E2iXvXXlUrhhKkAgzF6CpwV44eYwAL_21T4YT-cV8D-97C9B2hSGo3mv4WDdXd-qV5O6JSUUO4IEdQvUpw186jQaS5caPgCEH1D1t1QmRGbBDz72IOXHt6V-HnENnScOTUjLKE3UPUPhYitNUIi0oQi_Qila3GbUzTGI4K2odXm5SLmON8cNd7MHQ1p6E09qY-FefrmUzmtA9sACrdWj03r7LQzTVNnO-jGOB0pUIY4VYRympqzJbLsdGP0xOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/89891" target="_blank">📅 00:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=OgR8k6rFXZ-U4A8nuS3h41Z_9VZbFRXECJi9bi4fpqPHFttuq6rOWnO9x069ILflJkPhjGLYkorOeQBDFiX2Ef89QbobFUBGuLdeX1SwnylfLadKyjE1tpSFBW6i5HwTyQVfKt19GoJqkALbumJd5bDjd5PjGiBjfmBMkcYBLYaFAIJhfVzOYvFtC8KBVBX1m9S5U1MTJ_4bAP7qAldmFlfiYF3wZM7yQutmvNky-F29lJoWlEaJVlDDTL-jZ2SyXGZSMnxPquXmuQl0k7qul4F1beC61SuX7WjMwVZ5QItYyH2d10_UrsOiw5LqeAthe4kvoAlOLVfQI65I9MmeoGPyfIXcAzm-98BfHOoWDCCHaITe9T2vjFWz0D8K8wL7bs32_U_15_LUSYQ1Tu6W7z3GY_GMzTd8fEHGkMVVkzviwMHfAn_QxK-6pKpbiWBTIKokPlk2fLu8quzddMnX0p5Sg_JbzoulXrGo2vIi0qi7FQV8vn7cfMri7vxPdlvZc3aZl_FyFiOUiz7Eo-uptIuJgpcU7kqp-i99snhTHmNxPPIBOprITA6LE4r7jFnrM-Ah9_QxrSKex9HtKpgOZcyq9VEZ87DxufGOfXwar4x508yw9XBWMdEoWoL9mIMsPyABaI7Xzn4q6u9ZvmOR4NA0zYHdWdTIjVRZ6ctBTrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=OgR8k6rFXZ-U4A8nuS3h41Z_9VZbFRXECJi9bi4fpqPHFttuq6rOWnO9x069ILflJkPhjGLYkorOeQBDFiX2Ef89QbobFUBGuLdeX1SwnylfLadKyjE1tpSFBW6i5HwTyQVfKt19GoJqkALbumJd5bDjd5PjGiBjfmBMkcYBLYaFAIJhfVzOYvFtC8KBVBX1m9S5U1MTJ_4bAP7qAldmFlfiYF3wZM7yQutmvNky-F29lJoWlEaJVlDDTL-jZ2SyXGZSMnxPquXmuQl0k7qul4F1beC61SuX7WjMwVZ5QItYyH2d10_UrsOiw5LqeAthe4kvoAlOLVfQI65I9MmeoGPyfIXcAzm-98BfHOoWDCCHaITe9T2vjFWz0D8K8wL7bs32_U_15_LUSYQ1Tu6W7z3GY_GMzTd8fEHGkMVVkzviwMHfAn_QxK-6pKpbiWBTIKokPlk2fLu8quzddMnX0p5Sg_JbzoulXrGo2vIi0qi7FQV8vn7cfMri7vxPdlvZc3aZl_FyFiOUiz7Eo-uptIuJgpcU7kqp-i99snhTHmNxPPIBOprITA6LE4r7jFnrM-Ah9_QxrSKex9HtKpgOZcyq9VEZ87DxufGOfXwar4x508yw9XBWMdEoWoL9mIMsPyABaI7Xzn4q6u9ZvmOR4NA0zYHdWdTIjVRZ6ctBTrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=gQ1qhrMADNeYTX15spajNXZPUEkA1bV-PbRFs1e_CO1v-TRKJldBW149YQSek3WCzi8IEesTdQFM6SEQeGxEiVGlJhzc-yT3TrBEF0jMjw-g7vR1UtPQ-YkpHJ0gvfzFspWFkH_rM4J6CwvMh21xNG86OXu263ZY6kbdhUlDqVrpQPA9S_NWwxdVt1CsLQRGZHx-v5QLScm3V-bvCc18XkqjDfUMh2nPyL9nj2yfBXMVys4A7zKNI2g93XOiso5-MnL0j9L9g4ZA8kiVbi9Eq2uikLOGaR_1qb-wfOvOMJdUTT4t9xJs4McsXdOVZDtvP2JV-VwnLLXbSzoHiFlgOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=gQ1qhrMADNeYTX15spajNXZPUEkA1bV-PbRFs1e_CO1v-TRKJldBW149YQSek3WCzi8IEesTdQFM6SEQeGxEiVGlJhzc-yT3TrBEF0jMjw-g7vR1UtPQ-YkpHJ0gvfzFspWFkH_rM4J6CwvMh21xNG86OXu263ZY6kbdhUlDqVrpQPA9S_NWwxdVt1CsLQRGZHx-v5QLScm3V-bvCc18XkqjDfUMh2nPyL9nj2yfBXMVys4A7zKNI2g93XOiso5-MnL0j9L9g4ZA8kiVbi9Eq2uikLOGaR_1qb-wfOvOMJdUTT4t9xJs4McsXdOVZDtvP2JV-VwnLLXbSzoHiFlgOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89888">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PHIqW_kKwIuNjJPFl-nJCiEsa4m9cX5_ODDewOqhhhWvaDXLrG8tKQFhQ68VRp3x0cv2md22OOZvEvDttNHLo0sUW43MzQPtrNsju4fW909gcb5QmCh2foBINh65AfsuDwyzTPyfxE5IH_O1sMWmFKqnu8iMH5-j38jDxjOcA9MwSbVWjAtqPBV3Jbv4-PV-L3UDnBuyABcYVNhVmQmXs3VUAY5vbHHjRdR7x_Ntc5jL-8bJ6g5-HwGhvthIs9DzSEcj1v6W-ENRjRDbIkm0svoSC00pn4n6ofQ-8m7hu21K8N7PMK7U8jRU52ttFZFVcVjw09R6LWe161hdgLDY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/Futball180TV/89888" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=ZQkz7ejHxnOtsdLwnDFlSqNHSS9rYHIGb1R4yIcImGWVvHWYlrQpVYzasrnaX6WqVqfN9lwqZKArebiNvNFKS38zOe--jvgqa3k1N8F3gPjF9ooI6LzrFd7oVqdjaaBkuKPTi0ntCA4yD6iMQZR1VTlDz9Pw6KWYcNku4NFJY0QI-Y_T4KVCssrLIUuL5uCz2Keg1QN_KpfoofODxJuIzQc1F31be2Sq5EVvO5wEPeHVtsSdU0H4wJYYsghu5j7i04jDzg1NgzuLiosSYQHG7H_DQ_iXyhT8kyxU29ZtAWp-ueK8K9Gzu5cH7b3w9ljAzda-7uE2gNZBBZmg6TLRMJLnTqPh5bKL1hprIC5nWFfUsfmY73j4_UXXK9gjfVLm1evLhZmNkLkcNNoZBK24eb-h9eC6Zfr3mRPvYFyKZpTg7TZV8g_sACBy7t4k0m6t8lG2XTjWM7Aa8HUKqEMFIHP4vhiyJdqvBTesvswthdSt8zw5JvrFAmvIbDxDOgzLikTm5IWoTjVaPCADGnYoqf8Fmq8TAnK67c1HjTgqYYzkw3SppQfbwjWPg9dB4BVgTfLQmS6JMFmwugHSCJVnJU6Kl0HRwcjiEuyzSIEMMax4hgbWJXL0aPVdmBPJSdhk6GNkWqRrI5evjdPy0ex0HvS1K4KtqtnPOpfxRtJcio0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=ZQkz7ejHxnOtsdLwnDFlSqNHSS9rYHIGb1R4yIcImGWVvHWYlrQpVYzasrnaX6WqVqfN9lwqZKArebiNvNFKS38zOe--jvgqa3k1N8F3gPjF9ooI6LzrFd7oVqdjaaBkuKPTi0ntCA4yD6iMQZR1VTlDz9Pw6KWYcNku4NFJY0QI-Y_T4KVCssrLIUuL5uCz2Keg1QN_KpfoofODxJuIzQc1F31be2Sq5EVvO5wEPeHVtsSdU0H4wJYYsghu5j7i04jDzg1NgzuLiosSYQHG7H_DQ_iXyhT8kyxU29ZtAWp-ueK8K9Gzu5cH7b3w9ljAzda-7uE2gNZBBZmg6TLRMJLnTqPh5bKL1hprIC5nWFfUsfmY73j4_UXXK9gjfVLm1evLhZmNkLkcNNoZBK24eb-h9eC6Zfr3mRPvYFyKZpTg7TZV8g_sACBy7t4k0m6t8lG2XTjWM7Aa8HUKqEMFIHP4vhiyJdqvBTesvswthdSt8zw5JvrFAmvIbDxDOgzLikTm5IWoTjVaPCADGnYoqf8Fmq8TAnK67c1HjTgqYYzkw3SppQfbwjWPg9dB4BVgTfLQmS6JMFmwugHSCJVnJU6Kl0HRwcjiEuyzSIEMMax4hgbWJXL0aPVdmBPJSdhk6GNkWqRrI5evjdPy0ex0HvS1K4KtqtnPOpfxRtJcio0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=p_6oFHPoVU1e5a75U_eLP8xeAwkoBYoYHu7HGyx8-GQwxflEER3cncPIWiFy4EK3OvcjYMZ7NBen82DXuLha0o-HdTJuFsdFiacuTvngEbOxtn1VfCDbnVWJeXy2uioEe5kJQoMQYXyj4KExODjsnFp8bwcsVWIYpm927qUjqLh2k2E_bgdmJecZFr0M2a0xqNr9HrKXBUrKAVUV2Y3YZJD1Kt_qIhE9C6Tq1tyl72RscM7gAulB41TvedjB77M_Kn_0VJWnrLWPfspGJpNetJ--0OdpHFSM6VX1cAExZoPDy1W8V8jNeoorSuvW2qNlMZeFd5JnvqOTtbI2wPeGZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=p_6oFHPoVU1e5a75U_eLP8xeAwkoBYoYHu7HGyx8-GQwxflEER3cncPIWiFy4EK3OvcjYMZ7NBen82DXuLha0o-HdTJuFsdFiacuTvngEbOxtn1VfCDbnVWJeXy2uioEe5kJQoMQYXyj4KExODjsnFp8bwcsVWIYpm927qUjqLh2k2E_bgdmJecZFr0M2a0xqNr9HrKXBUrKAVUV2Y3YZJD1Kt_qIhE9C6Tq1tyl72RscM7gAulB41TvedjB77M_Kn_0VJWnrLWPfspGJpNetJ--0OdpHFSM6VX1cAExZoPDy1W8V8jNeoorSuvW2qNlMZeFd5JnvqOTtbI2wPeGZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAO6aZMzvGmJW5BprU8jAqNZpoYLMRNrAg1UydMJl0eaJ6HShMNq70CLaZyNz-1yfNV5dgaLVOdvF37W1fcf0L-uVcfyD7knusI2Mez5fHz1yfAHFGtVlpur-RCf_cqhMG3ga8jDY9HbSm52JOFTkT42vCaPAoARI1f3jNn2bjMtrCZw7THOXYPHZLe2aN1Uoh9JViC_wcEk1bhIkuOWG7BTl42xn5nnbfrBsWGYyx_hVTOCEXlZQTup9p4RsEl-Zufq_8j5hK3ew7YTxa67650M-qFnUnrb6ch2UqIbwyn5kRkgi7r_WerttFWH7tM-ShQWwNri2mNZiMiPFCLK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpm_SbLcGXZWDuuE2kHCY7pWKgSJN72Rdij7ydt7TKK8Q2KcgF4zgdMx1RCncTuRhd7dqQsZ1TGioGWyFdyAnC0dgCVHRMDe4ToSMuBsIigA7HqMkSXm411Gj1TEDdPEB7BSWWCzT0h17tKWIweKmIkd5APOd9MrIBLHGGErtF0gxT-uOVxNEXUf_p3X3BC0HwXOPv3kD_f-5cK9EsuYTeQv1vO1_Fqu7VlaqxDWGzu6xP_Q8n1zt4DpD-H00HIdcy9JFNNeS4kJrzXXwJAO2UpaMoz4cr1pxI7uu8h95QTq-82nuNBMNSuWPeYc9EW_iJnCTJasFnD9EwxjOPoQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY9g0rBIDVPjBE_RhlLWh1D2eESfjnludMGdsZ9ocrG28vVhN8PBjaoEnwgbtZmznItyYNCxdGdgZnM9XtyUB3ENydCBThyl1IbMJumLWJlh5b4G_h7Jg0nEiZmjyQVKa_RGH_Y_kMXadNU8leJGXIgBgQH6iAiclvTikdGCHgQTQX6RTEOqrUUI_4XslHzPI9pTCouHV4HduaWS_fLj7CKTCVKaJwhtvKVbVuSogPxciRfgHkVuMesgk5zyHIi3rHGRIzKkEdWfA-RfgOP_mys-zkReSMRKxs1Cz3zGuJnZBjVUOozGTngmelonEf3Y7TDPYG18f2jY8UmaYlfmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOdEnbI7DYmL4EslOGD8sAAbdhSlAUZdk9-Ot_Ka8ZQFPsIUE-VD45h4PHNuToBA29lmU1zW22bZ3ML5pDhcvVzJ_i9zSs3LPOtvtauIxaCJYaFt2-Z_i5sQYk9J--pJ8B5-G4UniDyEojdDpgKC5ya85s7nI-PmZLVoU_zGvg1E_ucxzaGKkxpusLL0dIaBv23jslsRvFiBIvaGVIwh7O563YYXXGlz9EKnfFGunWmpHqgR3gnH61Wx9UlLKj8wnyPm4y6rL8Snbx5a9pszLBUl5z0vOk1CpxZA_cztq603krigpdRhB3W0CNDCKMO0N3-XZI3gzlMgGZxWaNIAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3MiNDIrizhB3z8SqEV6mxS2OltlRlsEk2_nhm17TOFzJW9ttcn8KHA4nrFA2XA-nPX7NH8OdYMsRYgnUvC34eexdSKtNRQXhQKASwlo8qr0xUsEFIqYImbu7LpwBFBFUpHTl8nOkKDjbQ8J2V9riUQ8mpghVa7e9XKSz3SbmqHgWjaLRyRH6zDbULsvZOJ0X-qLvR7BKmKBGEnfkk8SMyqp1KSys9_J0Oo2wAULMbHNEIeSRcBCx6GGt6bu1VcC1fq72WMtI7w-OFzMEZc4bXaqlZG_ViUzUsxBTov2X26clbJbb7IbDjMewMHtZuYxPmDqCpb587P7sYYHL7uFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAccyaJ46bEbsZPK0P7D0YpMR908CQoFR6Fv3nhqD_0Bp6FIAS5jXE2g__Zmf8Hpaqzfoy-UpEwhnKN3H_jThVKnc199H7ggxcc8AhqqBm8ptZ3Qbm1waincU3CfmdzaS-9C02szqq-0lqxhViO7V5E5oMT8Sizito4gKL3VFsSgqCWk74b21bBxm6zviP2lVVLqxJDOU37JWqGbWaV6nyM14R-P2pdIefIWEjIXdV8JCEdvJ2QO-bevU9omIcB4R39UlvqIv2vOn083OuNItlcgSPNxTeQDlzOi72-UoOTNf099gOQY0IUzyE-XQG_lZFCQMhOgfhYb3le0xa2Crg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nasND3f_xZEJJh1IvFJHDxuaZ4XhPoYb2vM1blDcimDKRiL66ser63vRDj8HqUWerQaqyCcRqupJ5FYfUqnjqm9MCI2RKaEGcYtenxDqqgJvNUlcqgqNYbRRv7QpyNI6936YdNMN7kN-2yJq54shcI-Jj5NeQqfBvXpvEv7obvq_xWRXwjh5sQc6qtR7N5wT1Uq6EmZiESlsI1Xl7ZxlWh-9G39VHkGJmGfdjo0PxyDt38WZneUoE2AJRC7PVOelz5zeYdCMHO2zXrvi5oti7xBpmaCgqK2k7vuURfP_14j-a3Hvfa_lP3ItFuYlph_XuAVz01s93mZkXkMuEdMNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZSau9GKI_YO7S0haJbyfBf0dIiFNKpDMkGich8ptE7CTLWkHdOur0jjRkmaPD5_TN8eH0FnqPAE2T8YTf11D5ybjXofwOs-u5gXObzOvQcVtuKYy4n2my1XL2tvoadvma0_t9dGQd1wDAHkks7QhmaxzehB3Y7AbtKT2WgAe6LkKrY0UsWUgxCeQm3HHylObcIU91fghjP5H6-AasaFlGJK7BN5E-nmYvmaN7pgaB8VRIaYP02pmbmiY1lon8RJf3CFaNwrghmW-ysCvfCpFhsVO58WSCkmf1-ejexXGqoUTwLc6rBge8H-1MQWEiXl2zASiCw25GU66DHqNIR6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFsZvTwpfXJrNb9Da0I86tZmPCIiRRy5oJaiMq9_Vxlvs_P0hIO46VZI4IRjgj3e7EpM40XYwGLTXivSc23sHQv_El60edUpv9KcSYrYDofMfF_w0whmYhZYLL23p-n_U80eC73Gs1OE8obdqlz73jXllEkd8DxUGm06PnzCDw4BSFSj7IA3NB0gZU7cUmC8aYfDcG9CZx2xs2XgW4zJRMdukmrVPd2wBDGoS8nPpWTerSqbhvrzmkan7LPcmCVYaS9WEZUFersJBtKSYFWUBXkHuoaC1DNjgY1u3Qk-BNR8pc582cMIQ1ZjmgOPJuoGrTq6B7Yfcib4JX7YZk6gbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBtFQ7dv4FD3RkhH-hrtOv1gsBFLtd1ZJREtB9oQn1nt4Ob2kW8mVqOY4MWf6wj_Ek2P6L01qygCzHy_YHFrOfAAvdfUE6L6XgzDpfv0To3d-w4Z6UmBGEYVzo1_jcxylIom4aKCUxAvcPBVxtqkvnl9S96lsRY1LCNRXnn5XvckPdESIbmX_om2I0arU2IeNLE7SNf22uX4nt1kBBrwvGwzZXeyPeTVNcaeCdlTo10vWpvSWjZEnZjLdVedTGxoY2PpAyZIDknb2iu8moKhIS2U9DBDaGpMu2YmxDHKludDvwPc5wBYU8Fl_O9ReXxiooXT9S1koEIbk_nrwVBnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89873">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pytTHRuTUKu1EAs4LyAs91aTFgSaJBWDEq7cb3GOMCDC4w9HiSAxI0OLTAc9HuSQU_KXEg2k8INdIsemOrWQuHi_g-ER74p7DUQoucDj9UU6vEioEuFMxk9V3w7uaMfNsXHkBmjzJCRRjDuAm2AcBIGzGaDo7BZosr7W4TwsnGFq1cKuyrItoQzaWg7Fm1aJokTDYQIcmWn38952FltTTWEk6gQKjL8AkoTZ4m4lVNq6cP6-KRiKazr1Bcdo2CRdflB6-dVp-qy2zqnJ1z7g5NtY2Q4wZNBzvBvSA9bOCgmO-WIhSuezXNXR-UqVlwvUlXy-o9WPLOEqc1U7-QcTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/89873" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=V6I3gEN-X9lNQEScSNbRa25VCWdHn7mZ7tyjSKG8U_EuPpwxS_Z4uX_7u7xQPC_JHXjDvmaINc5s8nPoSmJWZMT3jwV_FlYUUArmowHxuZW91q4mQSaK5Old9mgf3c0GrwGiyzhgZz7vCl8wiT-NbGEA1q82XeJU6oA0cx_-QDp63uebSwABHUzaaYVapCA2JtHmUeIfbLNFe_nDEEHdYnQJLe6zQGyx55KU_EgwCB3_67goKkRGfqstudcg2cUAu5z4NZ0LMI0obv3DRcSsiJPBExPcjSXnGqsri0SEJ8L0yyQg-sDLCvgkgW7LrBRCkBBkc344sJivAMKbuHAK0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=V6I3gEN-X9lNQEScSNbRa25VCWdHn7mZ7tyjSKG8U_EuPpwxS_Z4uX_7u7xQPC_JHXjDvmaINc5s8nPoSmJWZMT3jwV_FlYUUArmowHxuZW91q4mQSaK5Old9mgf3c0GrwGiyzhgZz7vCl8wiT-NbGEA1q82XeJU6oA0cx_-QDp63uebSwABHUzaaYVapCA2JtHmUeIfbLNFe_nDEEHdYnQJLe6zQGyx55KU_EgwCB3_67goKkRGfqstudcg2cUAu5z4NZ0LMI0obv3DRcSsiJPBExPcjSXnGqsri0SEJ8L0yyQg-sDLCvgkgW7LrBRCkBBkc344sJivAMKbuHAK0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBuAXRH9MP3Fc3Yw5RJGUZ-KANW5Rymr-UTupgwfyZHZ2mTWlSJW-kOzNcFbCLAEEj0QAifLTVDXyDi2TmD2nmI6OPO_VoatDGGu28Tw68ZJy5p9-rn2Ccd-gR3M6IHeu_UaerM8XKGm1A4H4C7PrsHAuhA_5R_cttIKe2_vlODQgYq5x13NNK7tSGsq-PH7pPELR10JlqJj7KbZBEc6iDZcEe9knMY-X6dZW5cWRaN9Lsk3tLmsvMxt6MXp4dxJqWyzuYaFQr_t4kL9633c0hO0Gfu2BTZNEsvoOzeU_0IqDswjAKtSRNaB4BNa5Wbl6vrap-pPK39NeSxG6rS0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrMdEAf7q9G-PMla4rceWUsNP5sGQYPYxZ051YQUq2WnPBHAoByVGpQcnIXzgVFiZM6U3t2V4FF3CwNmIxNmxWT3fwT6gAV0yt4H_IsIEdXwET8ZyNsyW5vckTO427rJ6k4n0pwPTaGNgMIIkzDWXpImlF-ELhFLQEBESpafOK4rtTzoN1bJbGppnp02Zim8aOBZ8kj_LpnvwcXmrCtU9_sG-HLmeH5BE6LnW5R5VV36uYUm18mxskzOI0V1fT_w97CgZFr0dEAvQ-P2CTDbcqOK3Yykqe9J-fiQfV-cZYnBjvxtAsZxLkNLf0f5aBEFLpUQLSivP64QvyGK_F62QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le60t1S9_53l_hGpNonEB14ph6CqOQNKJfMZD79p3WmsuL75qwFDo97DvmEPajp0wkR9fREN-ocbvvHqIQj-3p74XI3_wVoeFmM_QkE7H1kCQiq7preKpgf1JMGaCxJgXotvZwXfMu_A4wvphKO0Z9pJE-6JevbU8TAVz_9JOTWFMRWP5WOa_ef0q8vtgd7RRqEWOGIYws3-ouUhZe4XxnOW9d-F_sqsVFgfBPnYyamVA5MLsWpcRh3FLpR1mqeXkEEUgfEgZ4ofvb9c1dLXwY-RJ66yvXlLAi7Hw48UFMnJiOKL8cnF_FMiVKdXx0kUYnDBt_a5j98_vJbcXRVAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmdpbF9P2NSBNlSv0gVie6h1IN4YOrJZgSEtNDY9BvMo477CR4DlU_PVN-B0dTlI70J0xj8NppDyEYiyHjkA054-mHGIgOhKbxT2WJcZDreDC3kP79aNeMaHNS-y6bhHeMHCgtyoRnyO3KddFdKDHuxtBzfnuEymjkiai83OzFSxYahnEiqxd6k_1PX_om1c0gZE9XtWvK8NQ4Bg4WwJTrDw-YWSGTHBciitPKzBAUDctWZ3HjOJ5KXxxtlI31ht1gEV45GXumrJTaSwE5hpWfmJ97ly6YesVnEb3KvOjIhoQwUt7MZIXaRPVwRXO0dX2VO6WuBWiyBtX7Jt7SgRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgDMCBFa7G5o86C5lEQN7IDXXcYclUvAZRHMovs531ZCSUTgXRDUfNYwHiRG3zlF46Mk9pWQv_KEedpSDEYj5YBJd6kzgGh-Zu-JiZ59GRTjEFVbrWzxa-buxfnhUwxNRtAbHXJiR1gVxTzKmUPNbTtC1jS7lMCI1tVUYyN0_LN8CIPmxISywqMyzpUSTJqz4BZzWtu4kdCB0TJf7kBF-1284t8y8J3tesFSfYAhzcfLmLgUGIl-VUsdIapGLVDFbCtoIu_cyGuw-bfm2QH3YRCxvJVDoHzi_2a1EkHLs3FI8wefUUqn9SBPazHmLsKZN_NagP3xtlgOUHxI61itEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnJBIRoX4ZeiMM17N9TugYkqmrjhonWBLXQOiV0Vd45ZJkZKtDPPk3xeGMcPon8XbjZnq2SbyrKvYQ5FljMIbGzD_eHBmbRdH_0qMZFiBzMop5UVriKWhK0abb21oi_bUOSWA76SEvhwDhkWMqRqjjgMAGT2M0IGIq4IwWWmRvsc9mb1rGVUqk280OMl9ss1EsI_6OgewkB6j-zy5Sqo7dzd4FjJY51RHCCubjKwAGLcgbgLb8KfUU6kD-YtKeBG7c697rGrSu3S0DArNcFLPOfPw3TcZS9r6hgvO4CEITR7XfhzsYOnwkDzjFNp9VHsKmH2I4oP7VzAcN30vu9C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
یه آمار جالب و بی‌اهمیت
📊
لامین‌یامال ۳ قهرمانی لالیگا
⚠️
کریس‌رونالدو ۲ قهرمانی لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1xduyenQLc2HpxlH4eIeTssm_1A0-HmosNWI5_u46kx_tRazoDrIXO-2z4HAEh5qAjM-Dm9XZdwp1wGwTb5EqiQ06373enx-lmWSJNiqlFy4O38OKPocg6uu2FGnj9eJAnqOkJDuue3Ly6-3jEnAwUvHghc5jf7obqMpe8HbEgTyZNuwERZ0ov0MpmtV3KaT0VBXsR4CUd-SYQ7UsDdoYtGSeh5oIC6hMQXNkOQ4AezGSFrWDhmFxP6kkOAPQpXmhIWQphEXmfEhxjXAW1VXhTla93PoTSs3omJY_auT66Y-VoyOhKtr3n3HN2lZpc4LH3ZcZojhbZrMX40wITNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKHMBCS6YBQBggvZQIKSk_xFoyLtK6nvmsI5Bob75dK5eK6NHgUpsxgLqtEX54v8Cv4DHqqHVRKZu2i4RE0a-6V3p_xS_zPd3v47fAANExIFzW6hQKjs1q5YEMH1Cc6qlqngbgdD9GZGJD0NnH8VrZHq6q7sFkjzcw7UWdmqg2_NhFAyEGQluf6r4RE6rytSZkV72B4iTW_d6MoXDBz1z3ONEBU4iUQ4q1c0ucv78EeTkG7qaIhSpp3mObx4f4TblmkWy88SrBs1B40RUaRDZANGjzEauECJ2Y7XmIqcJU-aE26vTnSSQVUC6jEDXqc5-xZubJLO-QXM193iwOUe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D325j2fXu97-DG6y4GhEC2qlHSw3c0F2GzVQCvl52w3q5qvYV423UeT6szqljAA9AXEdCJO1rvKtbX9Wl3vJQV9STRplFxtMULDIhq4s_2sgEmSavdsBVQ_p01B9PkGgrEexn8SEBAlwEzmDBGjMLjNUO3LeEqZwdQffmKomBhbZ6vQIiFExCrHZihF1ZcwxzUvvmj6cHvoV72OaIMjrhfQJBaOH-KAART3wBF6EbX-Xd2v7IEhoqAZePu6kaBEmuLNIRKyV__BO3-UlSJ2r-uo266Taw3y6fQWnbqTrptRYjnW-73kXiQdnA5nZ6Qf0rZq-xNm4MM3sLbUdaS5z-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsqgZQn-gNNI9gsq_Io5L6zXUA_osBbz3uToTHFViHE15HK8V7kD29uXN9GTO9flVAA42t0CD3dE5mzpnlb1hknRpiTMc9FEO14vomMPW9210CbSNMIfb070GLx9hHzA0XodEMqc1kx1QHvFpNjfE9L0jCdmwRXmKfkj6dh9IMb9-U4hq-brzH1oRzi_Sy6HuBOPC9zu7K6JeG0VSNFQchOOOqtxA4aZvBJTHlgOianivKuAT2sOKTg4LAOhL4173E81pn8UA1XmfZI8efMtp1FXkMd6SZUgBV1bqlvu25f2Yy9kbvdPDBN98YoztFQFzuDjzGnHn5CHdx22GY0gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ ترامپ: از پاسخ ایران راضی نیستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/89860" target="_blank">📅 23:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnD32hImGezVjyb2ntO1qYvRm8YJ-DQwds8Bv4GY74gK706ssgJYlgi6lbMxtEYUx6KUuz07Sr8HhcJzBI64YAa6IkhjR5F8j_BXbxPzmNiqqJbaX8PH7fHDUSwuei0wUcLKrky4xO7BxjnZas2YQfHAGmnb4IlS92w7VmpsSfeA6FhyF2v-7a5hDKOINkOdPAlofG_VsstrtuBpAH1IzQe-m0g2-RNJifsTYCFwZkt-Rrw6N_HoyZMQIn6NcIQNNBcwFBj_oD7I5HB1KrSfTTwvST3tjDEUpUz7EDbRxEk6jBEbDATI8CmYVpPDj0sRPOA7v9ExYteEJI6-guKHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری امباپه وسط بازی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89859" target="_blank">📅 23:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=f7rm-tBze91JkIsutyBxqg2Vj_rg7LBaIWNPj_5c1asH9W6fsfsX-Oba52J8FUsjlo_8pZCisIyBG5ssZ9VILjjuB1lj66cXnB3v_ASXDhjlEdP5m7RVNCA_By2p5haoUYHNLcfgrHcapUsG24GqnE7hhzlOJVPImtev4RKMEl4yld7P9mpVrnw8V7vh2nxqONeHuDPI9JQi7n1Dsh1r0lnMahhMfItDpAeOvouTRcaUaWMsdpmP4d4VWuR8p0zuQnrauDQPS3s0W6XviffWaePheIelLksTo2zLv2jy777xneqjBtlrZ-bfBp96QIzw3F0ZF9hEfdYRT_MViO8JvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=f7rm-tBze91JkIsutyBxqg2Vj_rg7LBaIWNPj_5c1asH9W6fsfsX-Oba52J8FUsjlo_8pZCisIyBG5ssZ9VILjjuB1lj66cXnB3v_ASXDhjlEdP5m7RVNCA_By2p5haoUYHNLcfgrHcapUsG24GqnE7hhzlOJVPImtev4RKMEl4yld7P9mpVrnw8V7vh2nxqONeHuDPI9JQi7n1Dsh1r0lnMahhMfItDpAeOvouTRcaUaWMsdpmP4d4VWuR8p0zuQnrauDQPS3s0W6XviffWaePheIelLksTo2zLv2jy777xneqjBtlrZ-bfBp96QIzw3F0ZF9hEfdYRT_MViO8JvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوممممم بارساااااا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/89858" target="_blank">📅 22:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
فرررررراااااان</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89857" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بارساااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89856" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گگگگگگگگگگلگلگگلگل</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89855" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=eYJmIt4bD_qaNViqa4sUvoGqy7NLozklmDmZh2kxWFSxJRZlFIY6m3yCzgJUNHmWRg29IiLzoAwB8nuOdwWFj5pOelo-R9q0Zhq9vSUFBa_kUXSRB5Uc0we1VWFcGqI8c5c74KuHUmsFWbEKq8qDLnYfeO_5xlekyOeOZRml1kn1-a58hodwUpWj6hiaNLvSIET3dvb4czLJrbsjJHvAubWFkOF_AQ1EOLAVMDU2UdYJCQyuZNOquqJc4NuM47ASBNrid-ftc48dFWzrX7cIsdyleH9JLUUT8A9cEIU7X1Oq7Vyd717jKNN_gjIwQTBuB3U1JvNAYLAp6HIrD03S4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=eYJmIt4bD_qaNViqa4sUvoGqy7NLozklmDmZh2kxWFSxJRZlFIY6m3yCzgJUNHmWRg29IiLzoAwB8nuOdwWFj5pOelo-R9q0Zhq9vSUFBa_kUXSRB5Uc0we1VWFcGqI8c5c74KuHUmsFWbEKq8qDLnYfeO_5xlekyOeOZRml1kn1-a58hodwUpWj6hiaNLvSIET3dvb4czLJrbsjJHvAubWFkOF_AQ1EOLAVMDU2UdYJCQyuZNOquqJc4NuM47ASBNrid-ftc48dFWzrX7cIsdyleH9JLUUT8A9cEIU7X1Oq7Vyd717jKNN_gjIwQTBuB3U1JvNAYLAp6HIrD03S4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گل اول بارسلونا توسط رشفورد در دقیقه
9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89854" target="_blank">📅 22:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89853">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAloiOyKV8YC_oIKCu8P7C0m-MYXXSzlRNq60ZfoyZQNBzkdCmWCcGoddk7qWSsQ9IeQX9pKWIR7bn1wdaT5SkC_eu-hHWXDPwOmugvF846nAG2XrwkrB49lAuxDA7o6YYFaEexVUoWdKylXDEiCOJtPGMqdUdYG3abDyo-taNv_yW9pwFLbUt5Y0xi1tiCaieqAjzkiZoZoU2rylV3zT8sC8h4dZ-b5vAU3id-Gs6YOOIxl2HhhzYCBEI8Dmb4CuDHN0KtAtsXu3X1MnkbKWkPYaQJ7sidB_FkmgJJ6eCTPcNhodMDzkOk7n5BvRZnhJnHI8zhtIEygo8znVk-2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزيدنت ترامپ
: ایران ۴۷ ساله داره با آمریکا و بقیه دنیا بازی درمیاره و هی وقت‌کشی می‌کنه!
تا اینکه اوباما اومد. او فقط با ایران خوب نبود، خیلی هم بهشون حال داد، متحدای ما مثل اسرائیل رو ول کرد و به ایران یه فرصت بزرگ داد.
اون ۱.۷ میلیارد دلار پول نقد هم با هواپیما فرستادن براشون، کلی پول هم در کل بهشون رسید
انقدر پول بود که خودشون هم موندن باهاش چیکار کنن! ایرانی‌ها قبلاً همچین چیزی ندیده بودن.
اون موقع عملاً احمق‌ترین معامله تاریخ رو انجام دادن، چون یه رئیس‌جمهور ضعیف و بی‌عرضه داشتیم. بعدش هم اوضاع از اونم بدتر شد با بایدن خواب‌آلود!
۴۷ ساله ایران داره ما رو اذیت می‌کنه، آدم‌هامونو می‌کشه، اعتراضات رو خراب می‌کنه و تو منطقه مشکل درست می‌کنه، ولی دیگه اون دوران تموم شده. دیگه نمی‌خندن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/89853" target="_blank">📅 21:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89852">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0gxt67bjJ6WQR5oyU_U7--B75KZBE1SHdzbcnUVxym-Ku3xYf48bcl4w67Me4OKvAF_-nUysvvxdGjhmgPGINPYS6y-7CGY122SpRyyjDA762F_O4kW4gqott8BiQlYy4Aw1Gkc5Hkmef2L5g9OZOp-B_prH7unDfqWJtoY88yv_oV5PEEoa69lgYNX0q3xYeNW9-Zfs6gOWlfxMG6QbchYK2-VzqkBiZ3cOPZY02vC9SKosNHXcSwu8DkNfOPga3IrXPC73oOv2buH2lQ64ShvbYMSm7LHQ_cO-1xpqshA51EwGPz4y5AMxDWmFuwM8JBiOnY7fu_VmnP1vXFMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/Futball180TV/89852" target="_blank">📅 21:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7AhmCmkKfP7dJQpxtAMv7jffkidQD9djW_6z7TiejCgZlwbIMGFJOd0GN-NhQTy0qNKGworXgPf0dwCZgGLXHOzJhSdi9Jt1Ue5L-Ew2S8rYPRj9Ev82MEZ_XXgDBfr4KifLQkKUPnm4BdBI_PhZ0XQgfAgtX7FMQ8L-R66JP2zkl-WQ_xH_FzpzRIwZsZ5yqfCx_QCU4xHcuUc8w8TNBeEZi0AJulPxE8sIEcMeuOmpf24hDlUSuT7CV65sIcDpkubN--kZBkSJgE0KKL7qP9DRGSp8KoQoZgixt_fPlSAbxs62nBhk6t5c_YLjFWCjTadNLeoSYbNilhcOHcYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/89851" target="_blank">📅 21:06 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89850">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
آرسنال با برتری مقابل وستهم صدر جدول رو حفظ کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/Futball180TV/89850" target="_blank">📅 21:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89849">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=AM9WW8cN74uZZeV08bfzqqjHTg0AZe6KZ4rGvk7gRvPsQotXnfFKcZauZOlDv8ANRCj82duZ4cH1-4CwEgMHjrrEitn2IOAGnDyqZdI0th33m1EbUqHcEkcdXFA01R6c7WO1tzx7Vr27q4XHoj_T0J74BIRjAykrwjACRypADcyzcgLrF2hC5Tk3OgP51EpNR13i1nSQsgFVnm2IAthDeuDrlfZGGARlk1aYszGuFD8oE5WpMJaKZqYqz1T2IBmGFeF1-dxQ1fGBZ6dKBI9ejw_snHEQFD8HG-qQZ6zEK362zAoD4-6cTPXrt2GTrZxQfzHnt0DsNrV10yNCdV9xfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=AM9WW8cN74uZZeV08bfzqqjHTg0AZe6KZ4rGvk7gRvPsQotXnfFKcZauZOlDv8ANRCj82duZ4cH1-4CwEgMHjrrEitn2IOAGnDyqZdI0th33m1EbUqHcEkcdXFA01R6c7WO1tzx7Vr27q4XHoj_T0J74BIRjAykrwjACRypADcyzcgLrF2hC5Tk3OgP51EpNR13i1nSQsgFVnm2IAthDeuDrlfZGGARlk1aYszGuFD8oE5WpMJaKZqYqz1T2IBmGFeF1-dxQ1fGBZ6dKBI9ejw_snHEQFD8HG-qQZ6zEK362zAoD4-6cTPXrt2GTrZxQfzHnt0DsNrV10yNCdV9xfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
هوادار گالاتاسرای در بازی دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89849" target="_blank">📅 20:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89848">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57353990a9.mp4?token=mK7Dr-JH4TZMrkwD22AzwfB8G_SPMtDN5c4mtCLeh31S7pJST8mbwUzT-EtOQ33zhIaZj3MEQW5KTmcsAV_VsSbmcSDXVVcfxytFNeWdt6dbCREkFVP88l_x7_Eu2hfqH33BvPY5vuB9fU3V3mNyIlqiYCMvM9QTh-gmJ-9Ci3YmqzJsPhR_XfyaYrDUTWB-ET4pQNMF7O169o7yerpu6Zj7uMx2RaFaOXnFE-v06NqhODl6GGE6vkKZ3KyEJOm_aNtnXTbJsqhvQrZJg39E1tXkUukC_EJNWzLm4and7SUeoNGKo3_7JpVKjOdM0bdi5uqOTb_Wjbqx_b7ZLc7H2bP2qds5HVhufCMzlCf40r2un9H7GBlKa_82zNntcnrpbViPv48-qPazMI4RIdPWpzoT7Mx-1mjZ6nhHwNeHdnEu1UiXdlN_frZrRWOlQHJIGhBVjXtC9ny-4QcI4sjF60_9zMFowZkejCmJJ0BzGVAgiaVSwHhB10BqMJ8DjSBoPbipltY64nQbmheDOp73r98o4kPBc6JKDkdCznQejWK2a79Mg13Fmg1tQD_V_zd1qsaDDvBRBG0Q2pxpP-mhiibHQzXFqjqIwOFLjAQRixh1TZPCLYUCAs--h0anKvHavEVJQkOb8Hr8d7frJUe_yk64Pu2_PByAenVLlWStlO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57353990a9.mp4?token=mK7Dr-JH4TZMrkwD22AzwfB8G_SPMtDN5c4mtCLeh31S7pJST8mbwUzT-EtOQ33zhIaZj3MEQW5KTmcsAV_VsSbmcSDXVVcfxytFNeWdt6dbCREkFVP88l_x7_Eu2hfqH33BvPY5vuB9fU3V3mNyIlqiYCMvM9QTh-gmJ-9Ci3YmqzJsPhR_XfyaYrDUTWB-ET4pQNMF7O169o7yerpu6Zj7uMx2RaFaOXnFE-v06NqhODl6GGE6vkKZ3KyEJOm_aNtnXTbJsqhvQrZJg39E1tXkUukC_EJNWzLm4and7SUeoNGKo3_7JpVKjOdM0bdi5uqOTb_Wjbqx_b7ZLc7H2bP2qds5HVhufCMzlCf40r2un9H7GBlKa_82zNntcnrpbViPv48-qPazMI4RIdPWpzoT7Mx-1mjZ6nhHwNeHdnEu1UiXdlN_frZrRWOlQHJIGhBVjXtC9ny-4QcI4sjF60_9zMFowZkejCmJJ0BzGVAgiaVSwHhB10BqMJ8DjSBoPbipltY64nQbmheDOp73r98o4kPBc6JKDkdCznQejWK2a79Mg13Fmg1tQD_V_zd1qsaDDvBRBG0Q2pxpP-mhiibHQzXFqjqIwOFLjAQRixh1TZPCLYUCAs--h0anKvHavEVJQkOb8Hr8d7frJUe_yk64Pu2_PByAenVLlWStlO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جو اطراف استادیوم نیوکمپ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89848" target="_blank">📅 20:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/89847" target="_blank">📅 17:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89846">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89846" target="_blank">📅 17:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89845">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgAHrRfMPCaT_BWlQIGq1oVSrM873itqd03PbAfyCpUZ9qVwjNCCy0mCbtY3ksnB48wCXVmPZzw9U4zbYteOdziI5yYB-AVil2QFm0oHkw8n3Dy2pGVXyLYCYwzwiWRVrVGdM8d8QwLVbSKqTd1dBd7TRChKF-2aMg2c-pBoNCPj5ylYL4EkREz5ZpXFrzOMqeMDC2OdJDpuJVkbxLb58WHWZGmYEa4_9s_Ctn9DAXerZieR-Jk_v6Pgusmon9QGaW7I4Y2FNFA3y0PWXpQjVm69p75BCPuyzJGXiid4DICL-Z4LlNkDzaMCc0wGgvjplZdHtf4TQj5K7rEPxw1Cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
منتخب این‌فصل رئال‌مادرید و بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89845" target="_blank">📅 16:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89844">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYmsQWebOrHFidn-kp_BpoU62h_KUk5tI6Ace2v6YHmwibP4scBO0lPmkDDZwshLmK0xpT79nbLmD2z8gsXKtIGgAxui_vkdrKAzofpeuWNDoWILZHzdqDONLylrP6biPLwQtqBqR5d-xvXmcJzYjQN4GUXwzy35fSbdK6lu7d8bIDqkuR2t_jW2DKFwLueVFFFNw0Vp-Du5UvRs7fnQno9s3fya8h4bb08eSwSCd5BGHcXEeMGFuQXuZPhBBILIXY6nrY4ztxv6q5UQpHO5vJ5VFOcEBfTNfo6dG103b6pVwfXOHbET0cNiRiz4yHivEfWBgO_3EuHPfxNPTf-q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
هانسی فلیک در الکلاسیکو:
‏۶ بازی‌ها، ۵ پیروزی‌، ۱ شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89844" target="_blank">📅 15:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89843">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgISXiLR5ca9WkGbGv2Vqjv7qv8oqUqHUhJjc19Nv1d_402q5JZOblhM2_O9Zfn2qDqu9x5_52k0yLNfWYRSnbsxCvWZMqAIUuPMKSkJOrcQetzuPrPpF_LXrNnD1Wx2y1rLK7cI-m5rYFagLktXnHx9ZWFJJhtxBXfZOOUGDzinO7WjqtU8EmxrvuMVpUiiNvuoUbYlKkrJzfDY4-KeOMA9-4oZyz3J7SeDJJJZzPpxZ9ODWkhXV2ZPJHFSl-ym80lFk1nWav5Bu8G8Kb3osES7WJwvCFF4NMZLHQNQqpL1yVIC-WkIiQTIbSnaTH_96kL6QI0flw-3tGbRsbr0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89843" target="_blank">📅 14:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89842">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
امارات اعلام کرد که با دو پهپاد مورد حمله قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89842" target="_blank">📅 14:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89841">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9MyBppLN9sT6B8gVWnCEN2t9GfThUUvZ3g9pUuYSQMYurJpKqBV9VpxUFO9DMwE4jzUWlphTH3GY9j93uq0vR-B1Q9X0ETr56dULwVEwGfhL2Zcp0A8Zfkj4OEfUjQZgfo4nvucBwQn9etWdMQf_j2T6AmPQbxK9GJkR2adSRz36rw-oj3aivg5Y2mCrB_HS22WEIHM8FL8XrM36z5yu7cGtl0NNe-T6Yr9m1Fwmltbq0PzB2ZSCjIZAAnjOlnDKAnct5Owyp0Aybo7PksmkvzZi3SYdiU9r0ywogg_aKuaeGYni99W2tpDhN_eD_oLaR3SZYDgArvboxZNl9E8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پرگل‌ترین‌پیروزی تاریخ رئال‌مادرید در الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/89841" target="_blank">📅 14:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89840">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKPIZI0dCnf6j4WeGSEvMErfkqh747blnSJgFYj-j5lPt-16l5TBc7N0qALJmD0v5SPf6LjD3ihXGQa9_n-N9INfWGY3afvJRy1RbLI-QEnhe42tsWSteE-ClmBM0LKhfsJVhWZGv112voTfG4j_Sb8tn9j0usp_RvUMsIOfmgb96Z7smOuGDB9eDCAFOHaqcEi7UdtqxLOGnvC-4bEhNPCDMvuE44Ln_SNzgfkBTccgsZBZxFmK2emQZvX87LPFMh36o4nu04uU0R-EnVm8XRT5Y6o9874X5Q2JmHKAjtBU5vYTO548O8MWOgFo40xge2X2Ogz99BhYkAUQ7u1tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
در الکلاسیکو:
- بیشترین گل زده: مسی.
- بیشترین پاس گل: مسی.
- بیشترین تاثیر گذاری: مسی.
- بیشترین پاس گل در یک فصل: مسی.
- بیشترین گل از ضربات آزاد: مسی.
- بیشترین هت‌تریک: مسی.
- بیشترین دریبل موفق: مسی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89840" target="_blank">📅 13:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89839">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISHMgTCcdNIgJbD3-ANlFsMWMsXDmgiPsWUVk9OGSImQ_Ixfm39fDGyx9TVDVcPTO5BxgeoYNDq30ItFMgLh8mjAAWLrxwuz2ncWWOXytolLeQ-XalyL4ZkjXRfImyo4B674-1dqkffbUhdRq_6HbpQFfVrefwdz2Vs-yNacfm9AR6e6Ade36W4-7XVPiLrybeRbNSuh1W-FyiorWlX_gRiE53BhjBUzjg5DadBOcHfoy4vRX6DAwlSkNcUjuX-MqFPA0bNQrM13nZiRnvL6D1OlzmyBrrgyQP6xa-QyPG-nznxzVYgjXS5CS5oAC_VvHfoxqwPoaOwd03-xHd6MVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/89839" target="_blank">📅 13:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89838">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVvDYqT2_efAQEzHjmJx3D_nyyVvp_nkSw6DaD9Cdl-Qh7TYSW1N8jEAYlxOgrzst0nER9uSiU5yj1xVJkKXNiBbLN9VW5mZb_vfi2grwDlv88Gpynr0l8Dvr5JN5rjcyKtxc5wK8O3ZQaoHkZYyZAOJLmWzGEgLz_RPq2LGV659sWqHvmhfipZgUP-4AGdvtyI00vMXScX7dPnH9RB0x9sP25y8Fw7p3bDyr_XGz8YhHSUootdfwNFFc2XVb8D2_rhc50gybGlYncc4o9gJqP--053ytPDMfJe0P3fINv4mAT-xmiw9rpijuGw7cetf7HDUXzzsx9AbzGxOPlbEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین گلزنان تاریخ الکلاسیکو:
لیونل‌مسی ۲۶ گل
كريستيانو رونالدو ۱۸ گل
آلفردو دی‌استفانو ۱۸ گل
كريم بنزما ۱۶ گل
رائول گونزالس، ۱۵ گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89838" target="_blank">📅 12:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89837">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=RKKtrZEFwkvPrUDhGrjLiz2NFUbRzf5u78aTJO0EiQDlJGNaO7YLx3KGjaB9_OGR9veNpoyrgXytVs1ExY0hFjOqWrhV5qv1U1hoOJHyX7M766Ux0lAS4INL3rG6kG7DQcaqSgp9Wocr-t1dSUcXSFz8WU0wl8_xcx-0DAWowZQgRFbl8flCen9yigdWujuF_z7Rzwlvz8AD4yyXnr986yyc5rcvVgP83ajuiK5LMgdIj4j_qN5fuCNHIMfG_-G9Y2qlHtTuT0qgW1WY5FSWlVkXjywqm5MR5GyJZqpKIZ6hdXIXqPcz4CXJrz0BXW7k1vWsEFFvmc76m1UKsNOAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=RKKtrZEFwkvPrUDhGrjLiz2NFUbRzf5u78aTJO0EiQDlJGNaO7YLx3KGjaB9_OGR9veNpoyrgXytVs1ExY0hFjOqWrhV5qv1U1hoOJHyX7M766Ux0lAS4INL3rG6kG7DQcaqSgp9Wocr-t1dSUcXSFz8WU0wl8_xcx-0DAWowZQgRFbl8flCen9yigdWujuF_z7Rzwlvz8AD4yyXnr986yyc5rcvVgP83ajuiK5LMgdIj4j_qN5fuCNHIMfG_-G9Y2qlHtTuT0qgW1WY5FSWlVkXjywqm5MR5GyJZqpKIZ6hdXIXqPcz4CXJrz0BXW7k1vWsEFFvmc76m1UKsNOAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آخرین تمرینات بارسا و رئال پیش از الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89837" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiiYDWTcl9kyQ8OkgbUJ-MaJNf6ijxlcVRz8VAgvrZ45yyfaynYA_gJaBeqduDVr8CmMS_Nt4K0i7voWcfL82P2DsS9g7Y3-CDvk-aWByV0GQrzT_sBASCIOwFuuwQi3fjl3zzutHygz82zs9niv3Qc170gBReGQ4Mw-KsV9XfibCGZhf2X9SBAZ4eZmdYgqRQMAfSUWWXLmPge2TmZcs7xY9qICfytxkotQgz1zEfrw3D2CERk7W6J4elPVwl_OJAyMMzLKQ7WidOY6323O9lZzbtFu2XkTztGFJAfFppfMiBGuL1ORUvACXC-u--csw7REdp8ivEoPr5jZS66GRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رسانه‌های فرانسوی: اکسپوزیتو از کیلیان امباپه حامله شده و دلیل ارتباطات زیاد اخیر این دو نفر همین موضوعه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89836" target="_blank">📅 10:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgKgpZSl6Nb1EhXsOceWPRdyW6zFtD4cqQboagt_YyBBJW7X75D_MNYEGtrdatfqw5RyBVJkzkD-uOukkzadRif712v_kCKmfpJ_HMypIqPUaXrjSR2L3FgaNLHV2BAGLKFgOcLVeT5trl8nX61BFSOpPGbXu2iZbiCY3FgJemEjJ2CSjyJHnvEzm__05wyaQGA-_t-fv4CVkDulK-XM0bYv5VWDB-U4ZoO2ljqyVE7NmZ-73Ek7xESbk5LZYKZqNHmGVOx0lQ39CTk7FOPBjxlIVxCyHfXxupxjgNbNbdhed8cX4lM-LCn9RWr9SEKg07njfSt_m1sYO4DNVhTARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوتین: پیشنهاد روسیه برای خارج کردن اورانیوم غنی‌شده ایران روی میز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89835" target="_blank">📅 10:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89834">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetUnblock</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkx_qOJqahvFC-7jGWe7HTKHnKj5Wbjp6ramMC_6izIgg1KPv4mQIcF9aHpqoSVUj-4MMpbRTqgpwhVep8sa1I8U663vFlg5qq886B8vcGhfm2qHeaIJaC_6bhg_9crbsGbNg_mQXEP2Kfr2dBLyqNb0RjSgVj1O7Cne_tlQb5kEiVbgW5NbLY32nzIUAASbjc4larr2bAS5kl-200lnsxOHS3EKaS43N0wAsTiiOKx-BIOvw47Ra_pPWKbETRoyXhTo4KIm1jikybgciGzQWf0QnljzIRcjAfKbSyoPwWgEZOXWokgypSSS5Y0JillbgCEGjekicHXKjlBxqHvDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">[
⭕️
]  سرویس ها با تضمین کامل ارائه میشن، بدون قطعی و با سرعت بالا همراه با پشتیبانی کامل تا اخرین لحظه
✅
امکان مشاهده حجم به صورت انی
✅
تضمین بازگشت وجه درصورت قطعی
✅
تضمین کیفیت ، سرعت و پایداری
🆒
با توجه به کیفیتی که ارائه می‌دیم قیمت‌ها جزو اقتصادی‌ترین گزینه‌های بازار هست .
برای خرید و مشاوره پیام بده
👇
✅
@NetUnblock_Support
کانال مجموعه
👇
📣
@NetUnblockVPN
🤝
همکاری و فروش عمده پذیرفته می‌شود
.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89834" target="_blank">📅 00:27 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89833">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: ارتش اسرائیل طرحی به ترامپ داده که ظرف ۲۴ ساعت تمام زیرساخت حیاتی انرژی در ایران رو نابود میکنه و جمهوری اسلامی از پا در میاد و وارد مذاکرات میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/89833" target="_blank">📅 00:20 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89832">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUcP2gl219nD_BpVvfkf43EPK7v-uKnTV-FiF-ANhgCpAaQWOzrpMmWYKfBF5H3rWnbuQ_sufFldx0cv-aKSSm_4Kuqql3GK5KL281yQkMy7_yMdoTFaTa225c9NYaTKoSSFFvVfVv59I6zAbH40THmlOlhrK5Ntkjas_P-8oEFqluXT7PdnZATAp9SXiQHVxiKxu9IOXc_WheamtoKS9or_y0LQKnifboKmDoVjt1CxZTiixHQhyV2fiYq037LkIpM3jEcp7zWO2_NscW4j3tAIlhFN8cGViZ77VtciY9MEi-QqibFaZN29Gb8oRXn5M18SEnIJPtkL_uaguuS8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آخرین رده‌بندی توپ‌طلا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/89832" target="_blank">📅 22:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89831">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800   برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/89831" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89830">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/89830" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89829">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تبادل آتش میان آمریکا و جمهوری اسلامی</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/Futball180TV/89829" target="_blank">📅 23:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89828">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=Je3ULhp5O0YswdCIgIRK0rfML2AVe0vBECrZfrwM_F2-wNM_uuILB3FEuiyugouFhep0hwwW_1O0g4W612uja34FEmWp-COXQsg1yhflg8XT67wMr8Rok6IVG-Rs1e-_husmuVBYXBjXcemeFjaQV5AD7RKPp6c_HE1_kuSIwg-TMV1rozy_yQYX8-qJeeL0axJaCWU-k7V51fnpGzR-DN0ExNwk83xvHjUUUHCb155M9pekMJ2nD774MdYqOfm8wbQa1IJz-KRj2jHrCd1PIHkwxRg60sP6Y0kBA_0oKi6nDmJvk-9RrPtEtJQ2I0xPuMTwjSV61MB0YYylDnjQUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=Je3ULhp5O0YswdCIgIRK0rfML2AVe0vBECrZfrwM_F2-wNM_uuILB3FEuiyugouFhep0hwwW_1O0g4W612uja34FEmWp-COXQsg1yhflg8XT67wMr8Rok6IVG-Rs1e-_husmuVBYXBjXcemeFjaQV5AD7RKPp6c_HE1_kuSIwg-TMV1rozy_yQYX8-qJeeL0axJaCWU-k7V51fnpGzR-DN0ExNwk83xvHjUUUHCb155M9pekMJ2nD774MdYqOfm8wbQa1IJz-KRj2jHrCd1PIHkwxRg60sP6Y0kBA_0oKi6nDmJvk-9RrPtEtJQ2I0xPuMTwjSV61MB0YYylDnjQUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
شبکه خبر به‌نقل از مقام آگاه نظامی: به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی، یگان‌های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/89828" target="_blank">📅 23:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
اخبار منتشر شده از حمله امارات به ایران</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/Futball180TV/89827" target="_blank">📅 23:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رئال‌مادرید به مدت نامشخص والورده و شوامنی را از تیمش کنار گذاشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/89826" target="_blank">📅 19:43 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇪🇸
شوامنی و والورده از لیست رئال برای الکلاسیکو خط خوردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/89825" target="_blank">📅 18:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رئال‌مادرید قصد داره بدلیل اتفاقات اخیر، شوامنی رو در صورت رسیدن یه پیشنهاد خوب(احتمالا از لیورپول) به فروش برسونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/89824" target="_blank">📅 17:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
جزئیات درگیری در رختکن رئال:  منابعی از داخل رختکن گفتند که والورده از دست دادن با شوامنی در صبح خودداری کرد، و پس از آن جو بسیار خصمانه‌ای شکل گرفت که به درگیری شدیدی در داخل رختکن انجامید.  در جریان درگیری بین این دو، و بدون قصد و بدون هیچ تحریک از سوی…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/89823" target="_blank">📅 16:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lodM6BNbThWnud7WqRmEgh-TlR7xIDW1jHO9do2QewrjT5o0QY3iQOiMhq8O4RmwStHqqB0ukz-thDG707q9-5tSL-AxaTDLq2iU0Dlq5m7mks5hOIzXiNlFgw9p1E-dqLA_EA2uiRX5uCXYRwWaNrlqVhCRYra40nQUuJ0T7sV77h9S0uBvznqo7UxPA5HseE0QwgbeICeayBwz1ISEKjPi1Sm0gluikGj74Zo9tniZQ0IsdtE_Dne5OSlHNvdj2xh4J0vMDaStWMC2hNJZPPD9kdZazqC3tS7NC4tvivxHYDRUkA2j8e6JCoNec6nmXCq7oZaFZYZXK56t3fuBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فرلان‌مندی مدافع چپ رئال‌مادرید به دلیل وخامت در مصدومیت تاندون خود، حداقل یکسال غایب خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/Futball180TV/89822" target="_blank">📅 16:48 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووری از مارکا :  در آستانه ال‌کلاسیکو اورلیَن شوامنی و فده والورده امروز دوباره با هم درگیر شدن و دیروز هم دعوا کرده بودن، ولی امروز بدتر بود. فده بعد از درگیری راهی بیمارستان شد. رئال هم جلسه اضطراری برگزار کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/89821" target="_blank">📅 16:45 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFw0swaOXaJ-wSRfFOcNy0KIqApkp3BL1D8wHCCEWx_mPx20ehy4svqTEszJgBt4WIPG5I0KoB2Ya9Bg5iKw6KaCOhnpejGncoW5UOyFQlZPJC7JyPZPE5YYRis0b4UpnNqGixrNWjdEUOZWY1KX9I8ysAlUe7GKCIEAvOoDJZtpYgUtiM5IxhJLVVAodXFBJD6WYDUqKUyS17qo95M28CstO5YJQpnG5zMmZSTa07-8Nk3O7JXuKa1MaHiK6N1AGB-rAukkztUpeVgQK8Y0XSeKpKsh5tI6Vvl-2CCKbfGZegM5QW8TbEB-SKTLoCgJG0X1TR7GnWBdjBnsnSozpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت خونین رختکن رئال‌مادرید :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/89820" target="_blank">📅 16:39 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووری از مارکا :
در آستانه ال‌کلاسیکو اورلیَن شوامنی و فده والورده امروز دوباره با هم درگیر شدن و دیروز هم دعوا کرده بودن، ولی امروز بدتر بود. فده بعد از درگیری راهی بیمارستان شد. رئال هم جلسه اضطراری برگزار کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/89819" target="_blank">📅 16:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89818">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeJdqSAch-qdzlIrn637ng8ZQvzVbtWobjRvJLUSr3A6aOyKIhfHcpjxw89whx9mIRTaAT-HLCMpfFDgDkAUcLaljKJExeCiQKdM1cU2mzlPX6FoUjTuNDEV7UmoQXVENEJK0w2Q3IwvK5wRkBMDxsOPnOlc950_hMRq0S-v-RJG0MuOQAGs2zjOTLgeBfFDBRRwNbeweBAmgGeL1tYDdcezukDZQNF3BG1Ahg-ZFgEjLjQWVhBuQQpwnrlbr8GHOqq_k7a137oHtniQirQvS8WO0CjWPaOMgXoAXsvzZoBFIRGwGrQF6ZDxIf3EAsWC-wn6FIBNhzhohvBj0X2fhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی هوش‌مصنوعی از گروه‌بندی جام‌ملت‌های آسیا ۲۰۲۷
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/89818" target="_blank">📅 13:27 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89817">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سال 2019 درچنین‌روزی؛ لیورپول در آنفیلد کار بزرگ مقابل یاران‌مسی انجام‌داد و درحالیکه در بازی رفت 3 بر 0 بازی دو واگذار کرده‌ بودن در بازی رفت بارسا رو چهار بر صفر بردند و راهی مرحله بعدی شدند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/89817" target="_blank">📅 12:11 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89816">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI2KErk6_BPN7xa5-tDZ31VIQcLXIRGw2dPdD2rdchFRy88KaW81eb2Y0iRiSG0b_dtndF7bhxeerHZ0DxvoQ0pXQFSbseXjgGRzKDghfN-weDPjzo1F5Dt2MXQg4mMGHHobsYRxRhZ8sa60XSjld1puH-Za16f4slsasvupKhfJo8PPkNHi14104D9UPv6wr1RbgGcR3S2ZNJaybPS2tc25_Y4ctZiZ_TZagAQBZFXzILLEAAEy6qBsgFFXtBrcyWu8sL0ly_8cXxXhzsr2RiMgOEzkYiVYDt0Tovj7x3KsahpCxikoHvFVL9iQen3_SDq99xQba6IHKs6H8_Zw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❌
با پاکسازی پیج رونالدو از اکانت‌های فیک، ستاره پرتغالی ۱۸ میلیون فالوور خود را از دست داد. لیونل‌مسی نیز ۸ میلیون فالوور خود را که فیک بودند، از دست داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/89816" target="_blank">📅 11:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89815">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuwijD7dRzc9POIixjelVF0ttN7HVdBuW8Ko0NSWibuDeEU4sR21ktsZHH1QhG7TGbiM2MH7DD7CcmPS-bn4TrlJWfFxZKeTp_tFzaTHrMEZlcy7tNldJyNF-IAPPJ-GNO7kheWiZFkP2rIFUvIadg2ZjRik-hsGF6bIWYHpwVF2NUr6eUQurekRnt6_23oyAZYbNESm4g6itYQP7Y3dgsQ6iFQCGNWYl04x-pfMRO58BTojw-_nyumu8ZYQ6AgJKB4I4ekHD3uJdxle9EXaP7aKUG_IUm722z2x2egM_H480esrOTx2S320GmYc7PHAMEV2qKPcM8lmTgaYpgsmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
فینال لیگ‌قهرمانان اروپا
🇫🇷
پاری‌سن‌ژرمن
🆚
آرسنال
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
شنبه ۳۰ می ساعت ۲۲:۳۰
🏟
استادیوم شهر بوداپست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/89815" target="_blank">📅 00:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89814">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee63d2d75.mp4?token=Gu4Krp8apOQ8VX218_k_k701G3CJsJ0sk722wy0C0f_OZfVSk92rBD4mn2zXk8hhK_ELCikCA-BFmiuhUqEQoBgF05Bcb4gDdAu_PHO9aj38KbmF2kho6lebrWLzViss0v5Qkzx_CwQviRdwY5gEe5Wvk8aomR2Sk4zHPBEj5H-kzXrg6tHexczasWvFmpKbdpM9GQxD6Ix8OCB7JbdKvBAyodNoD5GNzUNOaDoiXJHlbpCdvrnNfkoCMMozv_UEMJlqt5BOrBMtSWvYMcSsFb4jIdF9tlPYHP6ET4OhscR886uJ0Ie1OaAjIGbevNdsCT8CQ_5OhEwAvAGuP-_4B0na1IEKiAs6G_6DaT8NuqhXmtJ7103oGmeitylUoeJ2SJFf1lEeK3lAWKzYeWjNxCnd3eHTCwB9WYJheqlKW1diL_1QyYR3ghL67Q3vv3PC21IsIgxIQOz2EscwI8YqO8gPIwd2vs8riEGPqjiv2KPZvrTZDA9Mte_VvAsIi-5Fm_EwV-pNJBeRo02KVDJP2pWAgexi6Rf0mdyWkggh1j6C6EedyzJ_uy8B40CZ9QdsvgKMn24jPF3JrGr5Ts3YfrBErqKoopiBT1K7tTC-EAtFfmEYVoYw8aVFwpXwpczmgAPBaLqVuqZ6q8Vh7TeFvoOqlqRo4ApSvmb_qFSjXPk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee63d2d75.mp4?token=Gu4Krp8apOQ8VX218_k_k701G3CJsJ0sk722wy0C0f_OZfVSk92rBD4mn2zXk8hhK_ELCikCA-BFmiuhUqEQoBgF05Bcb4gDdAu_PHO9aj38KbmF2kho6lebrWLzViss0v5Qkzx_CwQviRdwY5gEe5Wvk8aomR2Sk4zHPBEj5H-kzXrg6tHexczasWvFmpKbdpM9GQxD6Ix8OCB7JbdKvBAyodNoD5GNzUNOaDoiXJHlbpCdvrnNfkoCMMozv_UEMJlqt5BOrBMtSWvYMcSsFb4jIdF9tlPYHP6ET4OhscR886uJ0Ie1OaAjIGbevNdsCT8CQ_5OhEwAvAGuP-_4B0na1IEKiAs6G_6DaT8NuqhXmtJ7103oGmeitylUoeJ2SJFf1lEeK3lAWKzYeWjNxCnd3eHTCwB9WYJheqlKW1diL_1QyYR3ghL67Q3vv3PC21IsIgxIQOz2EscwI8YqO8gPIwd2vs8riEGPqjiv2KPZvrTZDA9Mte_VvAsIi-5Fm_EwV-pNJBeRo02KVDJP2pWAgexi6Rf0mdyWkggh1j6C6EedyzJ_uy8B40CZ9QdsvgKMn24jPF3JrGr5Ts3YfrBErqKoopiBT1K7tTC-EAtFfmEYVoYw8aVFwpXwpczmgAPBaLqVuqZ6q8Vh7TeFvoOqlqRo4ApSvmb_qFSjXPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بایرن‌مونیخ توسط هری‌کین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/89814" target="_blank">📅 00:28 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89813">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbd45ba6c2.mp4?token=FL6MNiNdp8W28z4MMPWR_VWZMMGjem95gUJ8n2irh3nu0JWsuGwHCACMYaCATcwEELDUZ-qnUJXAeoOZCCpR5YEeQ10tgHwZSTzHw8vmlDgtXzzjKtqPXShaNAK9dpp5bUIIgUMkMS46AsHTmQziB_oLMIfDBh-aWVc7Um0uMXgKqKS_HKT9wP9BH3wtPXSksJKZfUMUlG-6-d2D93Hg5psay1Le4MCKy4B_nVBOb9ZIMxUlI59ee9e4ALUL7EQdiH_javgDKY8h0Ktndczt3ObSb7q4tgSU4RbSF5YJTI07UkSuFJ1ZQ1OookOHrhdyrOWoHlGdhQKc60qJBQju0jDJXj9Cmbx1tfeNLDRlMn-vcDa1v5XlEhWCzRC55SW2n4SDs3HyXEEecqOIYdjj5S3BK3K9b3k3yqfer8k29WmdomtDPt-INkdQNcvPBbKRcVLBIwHAzbo5iZ9e_yurs91BiB10t-l75PbpqxjvmxnY5TEgfh6iWARhOOCrvLVQTGZamHacULNLAS4ERpPrSpuSPCl4KvyTAaIncMyHB1xqodROye7UBaWSPaX_Vj2hDB3f-r2bsAYL2h_iwhUZKMniqW5RANE3TW3cy35TSnxaJI_-rdSCSoTXAQJS9JzlsIt7pIBNnPB309AJTOEplqeVahz4ffZheCSfCk3yrMY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbd45ba6c2.mp4?token=FL6MNiNdp8W28z4MMPWR_VWZMMGjem95gUJ8n2irh3nu0JWsuGwHCACMYaCATcwEELDUZ-qnUJXAeoOZCCpR5YEeQ10tgHwZSTzHw8vmlDgtXzzjKtqPXShaNAK9dpp5bUIIgUMkMS46AsHTmQziB_oLMIfDBh-aWVc7Um0uMXgKqKS_HKT9wP9BH3wtPXSksJKZfUMUlG-6-d2D93Hg5psay1Le4MCKy4B_nVBOb9ZIMxUlI59ee9e4ALUL7EQdiH_javgDKY8h0Ktndczt3ObSb7q4tgSU4RbSF5YJTI07UkSuFJ1ZQ1OookOHrhdyrOWoHlGdhQKc60qJBQju0jDJXj9Cmbx1tfeNLDRlMn-vcDa1v5XlEhWCzRC55SW2n4SDs3HyXEEecqOIYdjj5S3BK3K9b3k3yqfer8k29WmdomtDPt-INkdQNcvPBbKRcVLBIwHAzbo5iZ9e_yurs91BiB10t-l75PbpqxjvmxnY5TEgfh6iWARhOOCrvLVQTGZamHacULNLAS4ERpPrSpuSPCl4KvyTAaIncMyHB1xqodROye7UBaWSPaX_Vj2hDB3f-r2bsAYL2h_iwhUZKMniqW5RANE3TW3cy35TSnxaJI_-rdSCSoTXAQJS9JzlsIt7pIBNnPB309AJTOEplqeVahz4ffZheCSfCk3yrMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
گل‌اول پاری‌سن‌ژرمن به بایرن توسط دمبله
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/89813" target="_blank">📅 22:38 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89812">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0adbc6a7.mp4?token=Zhyi1qzsEHahfNqCB3Ci8wVgEfif2vS_48WpSa9_QxcXRYRFrifgoZv1LA1D6-1kgbfNUpUMb8x_Eujw4uifgf84TDP4YDzaQVIYoOFSoQqnrvNQLBUF3D8M47rYWDij704Wh6yc4xaaQtH1LvkEAXcCHUDc-val4qfgsiXUkos4ngKQo0tDkDX3bER4L9BuBDIpDv8x7ObC3WDc3VKE8gT0SdB-b4CqWmX3M_uQsFCIEGhT3egXfetNWtwRYZb3M7Gdqc2en9gsHSqcPwkC5goDGEVNdv5xbqZyx2dL2t49NzTe5p-UKFDlFSNeHk260Z6RZzzFN9RmudZAsfS8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0adbc6a7.mp4?token=Zhyi1qzsEHahfNqCB3Ci8wVgEfif2vS_48WpSa9_QxcXRYRFrifgoZv1LA1D6-1kgbfNUpUMb8x_Eujw4uifgf84TDP4YDzaQVIYoOFSoQqnrvNQLBUF3D8M47rYWDij704Wh6yc4xaaQtH1LvkEAXcCHUDc-val4qfgsiXUkos4ngKQo0tDkDX3bER4L9BuBDIpDv8x7ObC3WDc3VKE8gT0SdB-b4CqWmX3M_uQsFCIEGhT3egXfetNWtwRYZb3M7Gdqc2en9gsHSqcPwkC5goDGEVNdv5xbqZyx2dL2t49NzTe5p-UKFDlFSNeHk260Z6RZzzFN9RmudZAsfS8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادعای ترامپ به فاکس نیوز: زمان توافق با ایران یک هفته است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/89812" target="_blank">📅 22:09 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89811">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز از توافق قریب‌الوقوع آمریکا و ایران برای پایان جنگ را خبر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/89811" target="_blank">📅 17:02 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA4zoCZGrjljxb79PFz_iniwzs0NX60G99sfiXVz_dQOYcqfwizRowlde4RvaEMHB85XDDSf81bHetdzuToiTfmToKZBX7HO02MvvGB9s8pyqVNiETe_NIEUfi8cMHf4R30V8Ec4umzHbMHGu8Bvzbaqy6JZ1JCiXn7pxhMBPeZ6BlKT4NIzW-BaLk71jLK6HIIpcSbrpzzPT3SGRKdHaq0Pdk8GF2VI0vq91QhMpKo9IJAX5_1fvQejN_ozLZ6_2Osc6tK0XKY2WvVnM0IZfY05vcnpsrwiWSdduioGT2HiW2IfQsfK519pppvGeJ7oXX750KreRtJlmVemcManxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
♨️
ترامپ: با فرض اینکه ایران موافقت کند آنچه را که بر سر آن توافق شده واگذار کند، که شاید فرض بزرگی باشد، عملیات افسانه‌ای «خشم حماسی» به پایان خواهد رسید و محاصره بسیار موثر اجازه خواهد داد که تنگه هرمز برای همه از جمله ایران باز باشد. اگر آنها موافقت نکنند، بمباران شروع می‌شود و متاسفانه در سطح و شدتی بسیار بالاتر از قبل خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/89810" target="_blank">📅 15:17 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز از توافق قریب‌الوقوع آمریکا و ایران برای پایان جنگ را خبر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/89809" target="_blank">📅 14:15 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLFxRSiyey79DycRiNmmXskKcS-4Sp98_hR8At7bEITTmAmkci0_XRaEO7MsitzcanYaw214OJOyiubbLZX__u5Fe6kp0l9sg5goHYajz4svIAsW-yI-22ydiFr7ctOFpoW3LkpkNvewxAonRs9Wz9eo7Ohdutj5AC4Cp3zJ3VEy6BMAR7NvTkg2826qgxE1SOhvKaFCNNYF0V6kBLYeKIdbmE1iSz5TKBAxjZjFjD7qIOGwtOJH88eu0urEXNn7_zcE2ATjlGR8yWUMYJixXmMLFwSxNZDF6NgbK8cShG8cNfkpUfWA6RSQ6zDAkZVzyU6aDqwEoaDIQWd0fscgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت ۱۰ سال اخیر اتلتیکومادرید با میلیون‌ها هزینه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/89808" target="_blank">📅 14:03 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز از توافق قریب‌الوقوع آمریکا و ایران برای پایان جنگ را خبر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89807" target="_blank">📅 13:38 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89806">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaKCVoPR0y1KEU_fSE1jXBnHqz1soJO-D0Gtz2JdGgLaRueWTcFmCWLCCO-A6jSt2xp3E4609-KkExjVEHL1EyQwgkBobSssVI_PVK4aFuhnokXHY7-4WBcmJ8iJuwXwv7X3VH0ajYdctvTrXGL11aAaih-SS5PNpNMxinPkdFLxWRH40Gura_xFaPbgOHenDg06M7pr9Pt7ATQIJ31knhCxMOc80OnwCzicpFB7N3VbUgwuLEMcNV3nnc2T99A3KaLLoKacv6B_uTy1osnWJWVpoLIiHYzDbyupnDdPPuI6gOGfVteiXUgYvkJxHj3bTUIyWa1KzkolzeBI3CuIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز از توافق قریب‌الوقوع آمریکا و ایران برای پایان جنگ را خبر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89806" target="_blank">📅 13:28 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89805">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiUMGeE6a4-CpUk75s3dK9ZcERwHI8v3PSWexKJ3M9Nkqz2nCEFzu_dPluyw6Mt9snrBykBtxnswyC410YnCRwkQy1_zx_REvMqhX86DKCb9JjotSDhP59CZ1_TRrQmkBSSnau-i1K_ddxd0wBXaxmlE66tRE6PhSxq4PohQkZhVMGrUAbdWG-N7sGM5lUuW_rHH5ThdwrhP2H9EqXQDdQs0DIf1GTJEkE3QcWL3gTFGoqs9n17L9jC4fDhPuFavCcnwJ3CG2QWOVeEykyx2I1bRLjk7CR-SYSVoZ-G1mLJX967LDNdgNTPgFKLVQ-Xbrao3VXZo-2oCFo0hUpG8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالک ناتینگهام‌فارست وسط بازی با چلسی :))
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/89805" target="_blank">📅 13:02 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89804">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cd17339c.mp4?token=Upnc0JBCofcPSt2Y24UI500pbvI9Y64rLofy_5DO6wMFiATO8rF5AcxzoH1PW73gLfeoD_E6VnJRw_B-Z5DymK8DyeFZU9NXt6eWNODP0R4q_ljEZxTrJhZXt1TmarPK8r8SgHJLQljePXRPLMhsLhjuzmu8mKqp0erQ96eB7pAaesnH5rGZky8Qg-XF_WgARCnEaBEaxcT8DRNzzKkFmbPhddFH7a7-Wi7E31YgXWn65w7nC-aIosjyYjeC1Ea6W4oTPmoci1U4Ov-T_cqbv0VjuDRFg_TXxBoIFt8qk10hMe8RZwYAKEptTVu0sjebXiKqJRR4DSxEh54rHJmasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cd17339c.mp4?token=Upnc0JBCofcPSt2Y24UI500pbvI9Y64rLofy_5DO6wMFiATO8rF5AcxzoH1PW73gLfeoD_E6VnJRw_B-Z5DymK8DyeFZU9NXt6eWNODP0R4q_ljEZxTrJhZXt1TmarPK8r8SgHJLQljePXRPLMhsLhjuzmu8mKqp0erQ96eB7pAaesnH5rGZky8Qg-XF_WgARCnEaBEaxcT8DRNzzKkFmbPhddFH7a7-Wi7E31YgXWn65w7nC-aIosjyYjeC1Ea6W4oTPmoci1U4Ov-T_cqbv0VjuDRFg_TXxBoIFt8qk10hMe8RZwYAKEptTVu0sjebXiKqJRR4DSxEh54rHJmasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
جورجینا در مراسم‌ مت‌گالا ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/89804" target="_blank">📅 12:00 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89803">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
معاون وزارت علوم اعلام کرد که تا اطلاع ثانوی امتحانات پایان‌ترم دانشجویان مجازی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89803" target="_blank">📅 11:56 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
