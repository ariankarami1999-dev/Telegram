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
<img src="https://cdn4.telesco.pe/file/T_xbVFVR1nUNZe9oyTW-5pZtPp8-v_ZiKwjUzozhL6fNw9ftd7Ozm21sHXWvy7N-xM-vAizbZDov1XHuoZPadEbTY_foYwBScPksSCZZ6n5T05_YD6qLTeFsXvuadOQbnAQXrrXxAD0WRN1FdXrB4kwN2p0Zxl_51QY9_9A1yFhMZKSf7FCYfAsDeb_PA7SFgfKqoqcD18GgqY8gZRPsjH_7q_pOp7-fmNEKqaG8KRXzRv4up27rcRjbmgqdOg1ycilmoEK1bk9KgCScIpTyRwtGITUz_YzFDZytkW_g15xUXStVEqGnbAMLElj-1S4bV_Z2ntn7XyuzZhiFq9Lw0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 137K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 21:28:40</div>
<hr>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHuu1WckMXtszxJRs8Euz1MVpw8d3zx7oAJNlUgl-aLikZPB6XwlN6Xn9ArqIbq2TpwYpiHpsSc9kFCt4tS7Hy9G__dPyNHFnreDiaPb7cCRZ9YOld--yzNpqO57WnAu7wrJ-RbY7l-jhQz9hPRP8PjWTf32THNJHDBtXLVnsZbp9PPV1LqV06cIhJVJlm2OG6gSPCjHaRekko8DmMfvr57K_wica1RGgTdQdhh2hx_lrHtB2dFAzS3HEWEJWiQx3-mkRyMdE-OWhjREgMQTieOVtt3vhJJGnMAY_h83MEjuXYZZfiY3Jm6cwtRpUbuF49TirHFrPVcw-XcE1s4MtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsjRl0idaYc8HH_haOnKZMptzWtAewcu-MzUtBmXYf4IS4lUv7fGS1iwhJ1_3slLkuFc8XylBFeP_CVNHrwOw1URckqe4VVDx1qHWIpLOB9X3GlLU_vVBt-Dsc8-oQNndvm76oRnrObfFGqabuL-3PnY5XfZlIUQfSZzvEaSwsUcItwlKlXR-CKi8kRCt1aSGLNhOQJsI0AnPUscuLk8eA3KE4IeA7aBErKRsJDSY7bUr69Ir_Abh_Y8IIu6Fvf82ap8Q-wEebOcKbS7JKwk-IJvKOyOrNdLiEQ-7WLogaF9fwtzLHOD8HdpnuAPVXvmoi-vHFFZyo3EqqQQz0vh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVHAx-WURhZ2PXGipozixvhKzrLFH7Xsa8TEmj2XXuSDmao7IgiFlGAUfsB_Xs5FsPQ6uUvSDsVopbs-5XDVrlHcgqoIYU_43tsV-oy7fjzpTzKAwhjvUKjgM4yehPjbBVatcOxQfa2HUy5PDFfeSnbvKLqOME2Sh3dG_JJwobfSCJ7feeg8tj01CGTmhWoj5gaqE2mXtvCHOV8gzZ7ld921nYdP8tq85XZgBoNHgcmaCfStyrVp3UA0dU_I4ikllFXF8IQiat3SvhCcxOqEvflp60a30-lX3lIaAxK98AVpqv5yM9UPsDkStklfu1KqudJL5ym5oEuFmWzdv7K4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WON2YUveRHMBvBKeAg43Pv2ztIpMpctyRbj9XXgT8RD2d1GEWR9TmD73q-MHZ-uaedo0C7PUMQdSXiWIlqNBJSOVlLCL1jP3xZ2c4LA_XQc3a0azJACZ3LAfbN59MRacKMIhb2bX3Ggp3FgJYfzX70Jh6gxO33M5rQChViCMSnmSHcW-L78coRDLQQ-j0ZPoZ7CamI0AHJlG_TJGed41mmMKYm7NK3cZV_m7v1M3sIh-hjPdQQ6-I9CQih11jFphyP5lwuFARrhxe_SaXeByoEEuBeREpw6qKyTtwFRxkpVt_b3-nTFByXLSlwPfHlkysa9_UtJaO2Gd9cDY4rxzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amZ-Z_qPa5APz5eCp3Qp3uzIEuKTpu-pHs3rIWckk-SnYhIgAk5Sb-RcJoKz4FDiJh2DKQe6esn3Hm7D6KvDMzTQchI8w1zQ-UAAE0LFrKOC1VoQzh73n7F4b1Ro9aBgSrhND9Xm4LcDq_aDsP_LfyxSzmbaID3Lldxy6gmB-S-8zrcfNBUp82cLCrvVwHxNJpuLalhH8L1n2uzhQv50PZHtXaDyMBi0vkej8LAGzyIrRB73EmP0hNVIg1zvO2x_bTLDXg5AvZDPCK7D9b-HhGKhR8LMJLnT406aAgWhBUYDkxdBtmj_ggDycj9BAO4qtmb3bfxHz_GnrdnFvcNFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89899">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/Futball180TV/89899" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89898">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/Futball180TV/89898" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZOKYdrCQLGiD1tMR7u-37p1IIJPt1Et4os02yi1UEb7WoVSYCxw34VUKgw7jK1FtvYQrkbEI7JoiUcW695RCYe-VaRkuz26EXMJvN9KBocSQKqyZyDnTQT9DKG9UGYiuc0GDrdrHcdsTwc0YWnIuxz2AcajS4gIqIOznX5Ec9w-nk6Ao5YuGrTuwnPUQd0xIIPXeAbKeM-9cdAoFVvswTaRID559f54TNKGV-PDsYhpHmVZ8t2kvwndCXxb7BSt7n6qUyvVabcTKpXv23vzYs5I9N-F3tt9Ml9ci9_3EzxIoYx_h4WAMoBm5koI-KGSNOYRLv0iSxwa8G3ACS_y8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKk1ZSqCkdQ7gC5zLnwrRR40jXs38KmR3XB7dIbCLUlo7bvG2C9N95TWtcKRMY_ozGPoWF8-SUXPBKFWG0S8KO6oLr-l54pceB4UbKxrywHFGaKl2dmDiHb9jgqUBCELxpRkVy1UQhYzG93tuEPOVDXKnNBn8ptGP00DRKyCJTnX5FYB0qQvkwY59V8w4ZE293El316zK-mHVh1PKd_1iEhW3d4EVI0Cr-7QZGS9wovG4VPFDfKuRyqEb5mgS9Q92H7PQ_Kqn-5QXDloT8X94oaEI7jZgGiEQVsw5GCTQUBBVy4V4Pawqc46jLlpWMSZk8uiLNzwdA4v7IHyFU4LEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89893">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/Futball180TV/89893" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/89892" target="_blank">📅 00:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89891">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/89891" target="_blank">📅 00:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89888">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/Futball180TV/89888" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksH0XXlzCXloAG-MP7saRpKzGIYTxhP7RSy5rBfrPHHLJdsQEQVPrnnJ5dXOddz5dQ3M7sUWl7vq0wO84IWILswPs-yIAyhN99x6hyVu5SITMqkHSKGjgGgAsJZAaNQ__20LxL8rHTMqACYOx87GUhJay2lgm2ZNd0-8xgqMCxaBOOKt90vYImdNVXjW1etE9gq9ZFo8DFqYAJt1uvBiNiLIC84qlDqgbbGaGeZXww4qAHjqc43wX0OuP4QyELr0dvTYS3RGys-bxYksr3C8wcqfHmx0CpZDFYhgCHm_Rh-NSUio2xGnfaB_9tVVvQFP-cJitBWiVrzuXpRSLx_wAhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksH0XXlzCXloAG-MP7saRpKzGIYTxhP7RSy5rBfrPHHLJdsQEQVPrnnJ5dXOddz5dQ3M7sUWl7vq0wO84IWILswPs-yIAyhN99x6hyVu5SITMqkHSKGjgGgAsJZAaNQ__20LxL8rHTMqACYOx87GUhJay2lgm2ZNd0-8xgqMCxaBOOKt90vYImdNVXjW1etE9gq9ZFo8DFqYAJt1uvBiNiLIC84qlDqgbbGaGeZXww4qAHjqc43wX0OuP4QyELr0dvTYS3RGys-bxYksr3C8wcqfHmx0CpZDFYhgCHm_Rh-NSUio2xGnfaB_9tVVvQFP-cJitBWiVrzuXpRSLx_wAhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=iEa-hE0P6GhB7muyjd8Lrf2YsRzkf9DaAFaoct6nkgEJYzSsdPmMQVQgRsSsywSNL_yOKvuPDTpTxzIFYRLjKMNbmWIipMAB8TT3_Qb94ywGp1kUO9qv9GGeB0WijX1swCczfr0Du_6LG7pJoKZ3kXb3a8CzuqpaT8F4KdS4mTQzmlkK-JKaYTCLIvciO00VLV6HIqfhi30OwE83EhSRY1vTWhMZaTUbr9xRovl64Gg4lAvKKl-shOgdG2H5mG4MMEs_rhyYG8RkRMP11cIBAJ4l74sHsr1cXNm-Gdn-X87fFk7VuGrJRGd69fkd_QDzZK7ldGBSZLmHpSjM482OWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=iEa-hE0P6GhB7muyjd8Lrf2YsRzkf9DaAFaoct6nkgEJYzSsdPmMQVQgRsSsywSNL_yOKvuPDTpTxzIFYRLjKMNbmWIipMAB8TT3_Qb94ywGp1kUO9qv9GGeB0WijX1swCczfr0Du_6LG7pJoKZ3kXb3a8CzuqpaT8F4KdS4mTQzmlkK-JKaYTCLIvciO00VLV6HIqfhi30OwE83EhSRY1vTWhMZaTUbr9xRovl64Gg4lAvKKl-shOgdG2H5mG4MMEs_rhyYG8RkRMP11cIBAJ4l74sHsr1cXNm-Gdn-X87fFk7VuGrJRGd69fkd_QDzZK7ldGBSZLmHpSjM482OWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idVmucEXXhDF-mT6Ffg1vjVZczrG8aUqrj4JO_g7HFoUA2Zy90OCnR2dzvoUoU1-6z49Sg5GETU4WE5Cgrs61PR1eNo6wUhy5nnkq_M6SfIUwW2UAkc4PEQIIxhcn-rj_LmM8XKq0dJkdQI9B-ilMDfr1oYxV3nNQpm8EOLxrx-CCFcPZplIUKg-ZzoSmyhM7xeg-pmhBFr2Q2z1R0O0nKd59yz6GuhchmEE-g-YY2OYWsG_gvPzI5QOtZjbP3CG5X468UTcHTWJmOoremoGrRYp5njq6xebR_RargD0aWJ5DH5sin3_LIJZ9EfMI1xaL0KvFV3bXYF607YWSgNV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNTw3ufZMoVUPfQb7EVVKsbaL4_52wD5wF3XgJBHsYl-QBVc1RzVZue67H7Md2G6AgVZuvNRw4NWYEmr0A06wG_3xAwAiQaoIIub-waJHGBu7x23SoeiZcBWU7ciEsP0vXFQtiiVomK2dX0JqQVD1zJfm0dkYaRcOj968eiTxJxwSQ7jgikCEZbNpcP3zqvaMYqeUlQVpQbJt81NPfmpCl-DaiXVppKaa2S-ohSqYw3eO4BzJIPygxa2XLSRiRb4oBWWBDt4ltZSVcTlVyUf-rBfSafseoyRidoK2rNzXXz23ipjvftUaEKg7YuSKPMNVaUEQf_EYp_Xg7AjFGyNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixxF6ej956BoAV0j313iOamr_-qzEYYFKQzdTeEt46xK7_DFVFWN4mb2VjGu7smsLd0SrCkWk6as_pA-dfZfqJgp5YU5sOEL2_fTMWlIotzdxV_eLt0fZ4vEibmN_1zzo2pP49Xxfey7vGbft83dmL8UX8AeQHV8fT-W1PVkWk2h4yZQY5310vdxXX2DmK1TnYx8jXCMNULnTDkhPatfbWkX2-NxuVvZHembuz1E0461QfTebsDRe7AWiMTUMvW16_rhVqIOVz7yazNazbkyZne7Xe3Il1e8YpWrJO25KelvkDTykHJ88dnu-El9FaDX2hc7V_q9CI8Odn1bUsr9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKb2cghJSnIS8LIlMRJOwvZC9vX6xnSgAU6XEOH9GBjACTGCSRIfx40X68lGAVnHLFsCs7_K4VDHUVLXbgW9xBN1X1xfctKTlg7IMjq935E1bcEQHYR-82YcGaH7DQA8bYVt5mo3tEZm7GxuKv6EzONGXwjFWGPfDHiK4CLRYAKOfKml5KX-ZnnN5v7clMgHjRQPsYR3Wmr1WW3DAU1p30rWkQqOa9h1pHHkos1Ocis_cFf8aEQQWyxfpT5mAE8ZX8QpobpgO_JSXlPPo1nJ5npmdS6VZ4rVB1i_fGgqmfNc3T1iBDdAHWiarTpISCsv1hUTZilcI2P__4O7vMLSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0vdVev7lQ1ocqZHIV6OazDMJwiOTkLhAm-02kMKGwQ-EDoooqOaTbh7cdCacPytUVeom9VAR3qS1yu6jBA5vQgd1gYbY8JBHPgsH5W0_bzZHZJPrUl5CDcfyGbcredI4S5Dh5HYz-c9IatdIZ62vupJmwOk2PvJzKh6lvB8Avej3fzUZFtFOSb4hKv0R_b1aLmN7nUTO0NKT6vmVcQa9FF4ewYJ36ueR5yV0C1qhC64ZapqKl3V1VN4GN5w9FlQhI2Fz5Kf5pnJxDYTTrQGQNiGfhhibrJxiJXfbROHeCNHUs5PHdqHr_xVtf0IQua3yxHkIAihihTNbawVV2N7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYoKa9eHryt528z1iEySVh5YYkNC4T7NFz8GL_Yz5oLFe5OtFdb8Gm8E5zG6QduS0UKReGu4c-XMw8bjkkLQ33rG2jJXqG2WdzsdUCkRiywDtRrIc920RIbZGqT9GeESIMYqkjC13Tn_R9OJ4896OFtwZSdnU1AxiXPN4E0DAw4Vrqvp_2qPuUoDHFv2hzpt8li0iEhbM66Mf2CoRYmscuZI0cJ3fnpwo-Ys4TKkt7wWjtgelOCAjHIEqbaEwLwJtVN2N6gCaBn9IpSZ2d2EZ1kO0Ap9fR5P0OtydInzL7Vo2gCUHJimSwxHacFF_xCsGhtAsOg4airJAqUrNgeqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nasND3f_xZEJJh1IvFJHDxuaZ4XhPoYb2vM1blDcimDKRiL66ser63vRDj8HqUWerQaqyCcRqupJ5FYfUqnjqm9MCI2RKaEGcYtenxDqqgJvNUlcqgqNYbRRv7QpyNI6936YdNMN7kN-2yJq54shcI-Jj5NeQqfBvXpvEv7obvq_xWRXwjh5sQc6qtR7N5wT1Uq6EmZiESlsI1Xl7ZxlWh-9G39VHkGJmGfdjo0PxyDt38WZneUoE2AJRC7PVOelz5zeYdCMHO2zXrvi5oti7xBpmaCgqK2k7vuURfP_14j-a3Hvfa_lP3ItFuYlph_XuAVz01s93mZkXkMuEdMNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZSau9GKI_YO7S0haJbyfBf0dIiFNKpDMkGich8ptE7CTLWkHdOur0jjRkmaPD5_TN8eH0FnqPAE2T8YTf11D5ybjXofwOs-u5gXObzOvQcVtuKYy4n2my1XL2tvoadvma0_t9dGQd1wDAHkks7QhmaxzehB3Y7AbtKT2WgAe6LkKrY0UsWUgxCeQm3HHylObcIU91fghjP5H6-AasaFlGJK7BN5E-nmYvmaN7pgaB8VRIaYP02pmbmiY1lon8RJf3CFaNwrghmW-ysCvfCpFhsVO58WSCkmf1-ejexXGqoUTwLc6rBge8H-1MQWEiXl2zASiCw25GU66DHqNIR6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBtFQ7dv4FD3RkhH-hrtOv1gsBFLtd1ZJREtB9oQn1nt4Ob2kW8mVqOY4MWf6wj_Ek2P6L01qygCzHy_YHFrOfAAvdfUE6L6XgzDpfv0To3d-w4Z6UmBGEYVzo1_jcxylIom4aKCUxAvcPBVxtqkvnl9S96lsRY1LCNRXnn5XvckPdESIbmX_om2I0arU2IeNLE7SNf22uX4nt1kBBrwvGwzZXeyPeTVNcaeCdlTo10vWpvSWjZEnZjLdVedTGxoY2PpAyZIDknb2iu8moKhIS2U9DBDaGpMu2YmxDHKludDvwPc5wBYU8Fl_O9ReXxiooXT9S1koEIbk_nrwVBnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89873">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/89873" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBuAXRH9MP3Fc3Yw5RJGUZ-KANW5Rymr-UTupgwfyZHZ2mTWlSJW-kOzNcFbCLAEEj0QAifLTVDXyDi2TmD2nmI6OPO_VoatDGGu28Tw68ZJy5p9-rn2Ccd-gR3M6IHeu_UaerM8XKGm1A4H4C7PrsHAuhA_5R_cttIKe2_vlODQgYq5x13NNK7tSGsq-PH7pPELR10JlqJj7KbZBEc6iDZcEe9knMY-X6dZW5cWRaN9Lsk3tLmsvMxt6MXp4dxJqWyzuYaFQr_t4kL9633c0hO0Gfu2BTZNEsvoOzeU_0IqDswjAKtSRNaB4BNa5Wbl6vrap-pPK39NeSxG6rS0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrMdEAf7q9G-PMla4rceWUsNP5sGQYPYxZ051YQUq2WnPBHAoByVGpQcnIXzgVFiZM6U3t2V4FF3CwNmIxNmxWT3fwT6gAV0yt4H_IsIEdXwET8ZyNsyW5vckTO427rJ6k4n0pwPTaGNgMIIkzDWXpImlF-ELhFLQEBESpafOK4rtTzoN1bJbGppnp02Zim8aOBZ8kj_LpnvwcXmrCtU9_sG-HLmeH5BE6LnW5R5VV36uYUm18mxskzOI0V1fT_w97CgZFr0dEAvQ-P2CTDbcqOK3Yykqe9J-fiQfV-cZYnBjvxtAsZxLkNLf0f5aBEFLpUQLSivP64QvyGK_F62QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le60t1S9_53l_hGpNonEB14ph6CqOQNKJfMZD79p3WmsuL75qwFDo97DvmEPajp0wkR9fREN-ocbvvHqIQj-3p74XI3_wVoeFmM_QkE7H1kCQiq7preKpgf1JMGaCxJgXotvZwXfMu_A4wvphKO0Z9pJE-6JevbU8TAVz_9JOTWFMRWP5WOa_ef0q8vtgd7RRqEWOGIYws3-ouUhZe4XxnOW9d-F_sqsVFgfBPnYyamVA5MLsWpcRh3FLpR1mqeXkEEUgfEgZ4ofvb9c1dLXwY-RJ66yvXlLAi7Hw48UFMnJiOKL8cnF_FMiVKdXx0kUYnDBt_a5j98_vJbcXRVAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCgi_IKNRCu8N4q7miD0sS7a6qCdbbnzj_xucIdshGXBqGnxWApdMWwsnHoMf6nLQdDEjPDHQemZ0HVySZ6068HJV5im2cSYxPUi5hKKzdO0vVAyftnAivYxO6vFCvSBFjo6Ds-y4qvt1stNE4AgKdwdYipVZxM80cYAyV906A4nNGc-s9yCBs407LE_iw6Mbf9GcDUWzjrjMpB4D08c6B0lLvnwcoK30WiYWlVKnXPm2gqJEVxKSXGyHT_PkA94xQXKF1ZQREhokMV6LwVgTvWdiSZNpE7PnH_ih1zHb-esdJm-oP8sIJCn-AcMVv813rGLRMisUrBg25v0VufvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afGZslFm256TkmZdzQr7n_0Uc5Oqipvu0BSjslMhNvIxbqQty5IGylwSwCepLVAk9HDszWPG6ouAW654r7WTxfxTepJ9vb0MQVxoLASlJi6GDyAnSfHk5anSFq_3lg6CnDYkf3eABZ7hjBmhN3y3Y27gu1JO6OvRJDHbCgP0uBtRvKEmy0n77_ME8WsiMRPvKm8DX8E8FDkAsN-r5_9UtGRe-9yCI8OfzZ0FgCY24WLI1r50DF1DWVd8vLlm2C1zJVePm89PYVBQnQpwBVqLb5PCWE3R_1_SXJT4T4eGDn1OBQCNoVqCFdH5OLFgXMqpK2cO-yfxcGcG81Qx0mR5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY9IVQn_biQH9B5RkYyDWeaUbEoCG_9ODeX03fNFaXmdbNGL1Fri1aSIOZ-Pl1voHC0MDcW3cwFl0rfSasW9cv9fxWWDPKRosrEwPyCsvpkQi-zlBTMXu6FCUlHwL6vsyECeRDT0xR_hhXQroDh9Y8Bnq9FYHM_X8tg9cAp0L5zA4A7LkU-FPqSO6p5PX3eJMQIGHaWjHwmtDjiwC1QLwlPOjEgtlxL4vmC3f4RW5b7d7kCv97yfj9uDzq1dP_KQhrVT_JED2NRhdsh5tSZNU3sNqnKSS8-Ejyj-K0VdxQI0A_dPX0qyWWob2AgJJaQlU3qFOsjPWpCilpWzcozAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvhQLdrVuq1BNWMiLUWE7TWA8YAP7UhRYdBQkKjSMFMi6PUwVDNUX1Mjay2LKWqiWVUem1axwk4EBA1AYWHg5c8cFXGLeO8VeNF8AvnwTN_HaVxCWrI3kq9YX2TpChGu94Hdz_w50BUV2HnKDExjT9H1r2nDRGXYKwAUB_CDozqGgdJ4pH9rbEwOG-c4lD5EQd3A0cC51NVtGWkz9VvDRTBES3nXEWeC9wxrz2PwzQFj_ZUgsjtJKeQiORNoXCuDXxWWRDdilWZpIdMtKNG5hiahZRY6-W3c4v9ENxmiS0DNO4l1bcYpaxFNEpQu-ly5crdM36W7mKxktY-SJcbshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thryXvQLYDq6afy7BuLyeyUQMEbx74GIThLGm6hgDgTQbm0V362JYs1rYhGzdnMeRXU3sfT-V0exaCvXC2C2hzNpw__qK3mLN2dkuKcWEGFy8Dp-gZ2ob3dJo8RJ2hqs36BVBfUc5ATTd3bzZa8buVT0H-nh1b19yHD3CSFbbdd01fHJYMzk3Df13ZhMXf8QkaCoNGWn0haFR2sLaOIoaR_V7YZ_Lf5WqUQKYkbAtHt5Bm7adSrTe0y89RzSRB7gYJ0N1OD47gGUkeKN_q_isWNOOGa0guHP-1v-HZiU-2YUTR7H_kZO7h98oKgp5VakSCDjP05Rt0Y_1ziY-_8JxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTavk76mGDQ5ybLjXPBKCF-ck9WdHf68LJq7Zywxd-UYHI66tH-gWs4wgn94A7N7LUV-shTtIbg01p7-iaGx5zzhmAf4n7LarHi-F17oNwjcdghgZUdLFDqJhel83fOM6aZKXj19n2QNsS_yoshskLH-KsN37sXKNYAcjHzCcsgUrBkhfxj-PuoiaiBASSFHqjmZ-dNJ5dZfBfxFabRoq-hUXp0ZnuG2UVZyhALofPrc42zrauuScfLIEVgskfe_xKdkjDhD_eRmd17KZLu--L6cm2RQR3Yi6YSwIr-yNygERoVgy9OuJBVL3DGcPJnwphuF-S2laYGbQZyQAfXbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ ترامپ: از پاسخ ایران راضی نیستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/89860" target="_blank">📅 23:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKpBMYIGiQIV_Zfue22ZxpMbv9LkvBfC0FpulLZAdE-6IPiw81JwiMSwVvxCbSdAzgvtIOTEjzDN0afEmrzsoZ7ZfYZmXDI53qEOxgI4HoX7vDZmdsaQQoUNXWW7h-_4N6YSNQH2eIRUPxblkwBa-ZN6rooDPaOS2A3WpaizdQGZ5MhkDH2fnpHEBR8fQwA3sheuZMFXab5XgsxG_mOUSrNh7OMURm0LL6ka2Hg58V7ntQrjf6hgBeKH0RZATSUqjScZDBcctadbCgq_vJllQDFDUvTjrjsIa8sfEFCsi0TN8-SPg8CixJHCJjr_EA79wAsyZdlpI4o9RsAu8cGIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری امباپه وسط بازی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/89859" target="_blank">📅 23:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/89858" target="_blank">📅 22:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
فرررررراااااان</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/89857" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بارساااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89856" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گگگگگگگگگگلگلگگلگل</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89855" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89854" target="_blank">📅 22:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89853">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFY0RcrzUoJN3dTkzYr77vy4_RBWWGaLBmsBpAv386gwHpboZp-6KglZgQoqKkR4-40uV1SYKZLdsWzs9-BuJXe01pBszTORXpmBmhkG5AmrkUFiTh-ku7IjsVPl9DVctk2az_KbA91CmyjjvzGI2RUy0cujPAf5nKqCUNz6xJ-AvU5NwGvkUjAB16nWGnMyNSbOC6sn1tBmxILvGBR0XWg2_UcaiEjb4ydVbyBWB6ARhun8bo8KRCn_lQ_H44bcWGtyKatHWAKYTz6bwS2Uu7LdMtxBQShjCdfU6fPTXm9-mK-HD88axVxmilhbDLJEhxdG2XJRPyuI-SvycudSuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89853" target="_blank">📅 21:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89852">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGm3-GumgddWAK9cDMTvOSnJ58WqPd_dEdRKgiOTyxqAuGg29f2aO73e5XXutWERSAh-NVXKPPBRzHjQNN1vYk6fJWonMrmAAOY2-9DM1c8JdlLO_lbDmE7goOlsoYlk6p1Ckctg_nwfq7tdApsT-An07UE-i7KjRMznPpna0f_ZlRF7flyYiZwY0dI4bxuvIHjaKfjRFmmDM401FVOkCelaa5kIIyspXGtR9l8OBUEq_Vdvqd5M3NNF5kc-iIKu4takcvGUr9etOjkAUdllpsRgJ_nSlHpzmFydSsLcKvgKa54jj7spDZuc-FQ34a2LIj-vJM1jrSMxsFcg8g1t1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/89852" target="_blank">📅 21:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89851">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnPfDJjlyDdbZTvwFsS9mZzBpNtykcXqfm80hSWaLOMXjbtCgP-tw-NmT5HBzvdh7O-iIAIjlB14YWR_OzgYYO8fuz1BtNla5JyvHrYL0LNFiLxZulUQ3vOUXC-TZ0oWjSmThB0o49BHBJ815WzO60bl4S7_uL_u-TtlCvQzWvHjJSWjdJ_vBJJ-VSVuvwRkFmGNuAP8RBAVZt46bvUlyH4RJ6u8rsYesHy3NoWHr-2VzTClFbKS6Zw5kPrFhPwyPbQ-i9hXR0RJs3eqn7dHGMN61eziVy90SzysCk5QW3d1EH_OfppvzYNuDUvxrMOwLklruGQEGdu1vrupPjJqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/89851" target="_blank">📅 21:06 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89850">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
آرسنال با برتری مقابل وستهم صدر جدول رو حفظ کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/89850" target="_blank">📅 21:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89849">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=A2WUkxSAkeDhFgBCwBQQ5ZXIFi-neaFo4W9xnls6hQMmsX4H_I6D_n9I0Oh4wSyHPXccizX1n2Qm2ljJPSH0a_xXGaBoNMV--UmCjgCRggEQ9phiFUmsjqwrfsqF2q_4buj-QrKxBjkdbs-ArGSjqD2RjmYjGazugOMlM7KOP7rB7GxJdjYIX84YFFF7rJfHk5L00iHpM3XN2LDbiMsN28pq3bAL5Ol3mD5s9Nb88wkGBPu9R5SzdspsS8EaY7Z13ICXln6-rzCg_ey4NJXBpoUXoi_Dkd9kV7vYchCwP9HOFECUjojmvqj-EY1g3wRBC4RrQ-cvtaLZdSA2pzVWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=A2WUkxSAkeDhFgBCwBQQ5ZXIFi-neaFo4W9xnls6hQMmsX4H_I6D_n9I0Oh4wSyHPXccizX1n2Qm2ljJPSH0a_xXGaBoNMV--UmCjgCRggEQ9phiFUmsjqwrfsqF2q_4buj-QrKxBjkdbs-ArGSjqD2RjmYjGazugOMlM7KOP7rB7GxJdjYIX84YFFF7rJfHk5L00iHpM3XN2LDbiMsN28pq3bAL5Ol3mD5s9Nb88wkGBPu9R5SzdspsS8EaY7Z13ICXln6-rzCg_ey4NJXBpoUXoi_Dkd9kV7vYchCwP9HOFECUjojmvqj-EY1g3wRBC4RrQ-cvtaLZdSA2pzVWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
هوادار گالاتاسرای در بازی دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89849" target="_blank">📅 20:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89848">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/89848" target="_blank">📅 20:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89847">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/89847" target="_blank">📅 17:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89846">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89846" target="_blank">📅 17:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89845">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt6GfTtSOnc0FgMrX8h-Um-t_GdwfLDjChbndxs28XHEbYljr5AGCvPkG34ccQHO6MWUMN6MF6G70JyFZt_s1O0xJlEKgXR4zwmAeB2jZ4o3JrOOOxyWQQ52uizTcuDmXZly97JCEQ1sJ8N2Id3K-dg3YgfEWLGdd3l0bC1onhmekRrIQIdnwr1a1tcrnu30UHfxYCPqW2OOooAqZiIh1PSXeCklONHzn9o8cBiMZKDdQMWHiTn-QQ9o3OOhRS8SaiWhIkMVASqsVLNCAhoaaZcZWprjJL4fjGC9eeUaCiy_5jjzwg6fZJ_2k9BOrtamTskshMvEvRYkjVIOc6a1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
منتخب این‌فصل رئال‌مادرید و بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89845" target="_blank">📅 16:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89844">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grxWJ8JIeFWImE5X53ETlKxMXCJkkMgLPHqYSUtkBr0BcbHx5XLdJ0MxR8Rc1uFEpNsm3SrsA7HgxPWXgdqYvG7gcpYH0s5jI2n0iwQqpt8U-dsLsOFgtgxRrBMKOkwpSEzFjmDv_6KZfJ2ro76tsqTXhOwI3upLSSgXf1C9yg71zFL7E2uBRc6mu_4kwWA8T53fep-PzjGQkqTFuoWgklW5IytObJAdmEGmNy4b0nKW994wR03snrm4NXM5_6Zn_JxuKCacyio3t_ftMBZAiQuaZ6XzR9q8A06U2lqokdESx7n1l9TYRtf1Q_hKUyqyNULvj0RPZW74mW9T0jHaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
هانسی فلیک در الکلاسیکو:
‏۶ بازی‌ها، ۵ پیروزی‌، ۱ شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/89844" target="_blank">📅 15:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQG3tjyR-ybr7XiV8VyccfNqEDhP4RiYKIwaGww-iVRDYymYppZoGejhSFljkmckvIMhGAWDv08G2PPoTmJx8R07sxJa3yQqDHhTFFx6NTBTGz7GQEgoc77Nu6IiW5XijyaBXUVvp9c6PFUoRKLpIQ-v8EmAObM7CXYbUJBVqoM3TO5wFlXEtvDCbOFBdRGhHjkmt7IDuXT0ljYMLCzeKlQZf8OmPJ31Wq0jOPAIRewpZzLvM4Gx9YTcBV59WYmWe69L-3d6XFVZpE2jqdVLkMlFlNAThqSGEgpRTNwXuVn0Ld96nBiKDO5_81MsX45DXwJTotZrUsXSDD_56xbclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89843" target="_blank">📅 14:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
امارات اعلام کرد که با دو پهپاد مورد حمله قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89842" target="_blank">📅 14:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T43hNgEikcxUoqQXrAAA5DDwyl64FpdC9OY4SZWUdz-3dP_4bwluAUrRy1l_hfyuYBs8YNBVhJPJKEDys_bZk0OCdbJ1VIs4rdVDvGb4go8RobRMQRbXfAeEe4pjBPrKncteBX_EQg13_kwcI39XIlI_FI7TgQKqIQ0btowPCnhXse1wVbU_wt1VdQnpfxwHbRX3obQWka4KA_mPEM8Q6wPI3yISYO8NB6pgdVjDptJNWqvrwyVEm0vGfclvjCBRXEnJwfZx_h6U2NiDehs7qwdaJlGXhP200iYquLQ91e0iDmPK_J_tpKJk6nDhYBJifqiU_OCLZpwcmphd7reu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پرگل‌ترین‌پیروزی تاریخ رئال‌مادرید در الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89841" target="_blank">📅 14:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89840">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/89840" target="_blank">📅 13:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISHMgTCcdNIgJbD3-ANlFsMWMsXDmgiPsWUVk9OGSImQ_Ixfm39fDGyx9TVDVcPTO5BxgeoYNDq30ItFMgLh8mjAAWLrxwuz2ncWWOXytolLeQ-XalyL4ZkjXRfImyo4B674-1dqkffbUhdRq_6HbpQFfVrefwdz2Vs-yNacfm9AR6e6Ade36W4-7XVPiLrybeRbNSuh1W-FyiorWlX_gRiE53BhjBUzjg5DadBOcHfoy4vRX6DAwlSkNcUjuX-MqFPA0bNQrM13nZiRnvL6D1OlzmyBrrgyQP6xa-QyPG-nznxzVYgjXS5CS5oAC_VvHfoxqwPoaOwd03-xHd6MVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/89839" target="_blank">📅 13:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89838">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89838" target="_blank">📅 12:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=uRzXC_fRRirRfm6qA91-dEFWLsOYstVSwv3r61PlWpoN_Yuqt_Xetyi1xkdbTjTt4dRPbJXSxyAqQb6Emz3iqXZB_LU1AD7DoWbZ3p_sZ-jpuCrPSQRdfxfvyNiRmqyqyosmqmyi_NtKiRTmai8GbS5vBNZI84puGDpO9tk70of0feWbALXN2cQgvwlAISD_M-MWpOK9SGckk_wjmSYquJ0vCLkOWPBAynBBDi1rSnuyJQDcTnGstdu6NYJdng0hlOw6qZP8R7L9qNJkW7lsL93us8B-gTGMWWuth5GgAUcvX9_-Z-zxuUQ-0UpNV95oY9LNfVN4SgNoWjbNE2qN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=uRzXC_fRRirRfm6qA91-dEFWLsOYstVSwv3r61PlWpoN_Yuqt_Xetyi1xkdbTjTt4dRPbJXSxyAqQb6Emz3iqXZB_LU1AD7DoWbZ3p_sZ-jpuCrPSQRdfxfvyNiRmqyqyosmqmyi_NtKiRTmai8GbS5vBNZI84puGDpO9tk70of0feWbALXN2cQgvwlAISD_M-MWpOK9SGckk_wjmSYquJ0vCLkOWPBAynBBDi1rSnuyJQDcTnGstdu6NYJdng0hlOw6qZP8R7L9qNJkW7lsL93us8B-gTGMWWuth5GgAUcvX9_-Z-zxuUQ-0UpNV95oY9LNfVN4SgNoWjbNE2qN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آخرین تمرینات بارسا و رئال پیش از الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89837" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiiYDWTcl9kyQ8OkgbUJ-MaJNf6ijxlcVRz8VAgvrZ45yyfaynYA_gJaBeqduDVr8CmMS_Nt4K0i7voWcfL82P2DsS9g7Y3-CDvk-aWByV0GQrzT_sBASCIOwFuuwQi3fjl3zzutHygz82zs9niv3Qc170gBReGQ4Mw-KsV9XfibCGZhf2X9SBAZ4eZmdYgqRQMAfSUWWXLmPge2TmZcs7xY9qICfytxkotQgz1zEfrw3D2CERk7W6J4elPVwl_OJAyMMzLKQ7WidOY6323O9lZzbtFu2XkTztGFJAfFppfMiBGuL1ORUvACXC-u--csw7REdp8ivEoPr5jZS66GRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رسانه‌های فرانسوی: اکسپوزیتو از کیلیان امباپه حامله شده و دلیل ارتباطات زیاد اخیر این دو نفر همین موضوعه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89836" target="_blank">📅 10:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgKgpZSl6Nb1EhXsOceWPRdyW6zFtD4cqQboagt_YyBBJW7X75D_MNYEGtrdatfqw5RyBVJkzkD-uOukkzadRif712v_kCKmfpJ_HMypIqPUaXrjSR2L3FgaNLHV2BAGLKFgOcLVeT5trl8nX61BFSOpPGbXu2iZbiCY3FgJemEjJ2CSjyJHnvEzm__05wyaQGA-_t-fv4CVkDulK-XM0bYv5VWDB-U4ZoO2ljqyVE7NmZ-73Ek7xESbk5LZYKZqNHmGVOx0lQ39CTk7FOPBjxlIVxCyHfXxupxjgNbNbdhed8cX4lM-LCn9RWr9SEKg07njfSt_m1sYO4DNVhTARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوتین: پیشنهاد روسیه برای خارج کردن اورانیوم غنی‌شده ایران روی میز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89835" target="_blank">📅 10:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89834">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89834" target="_blank">📅 00:27 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: ارتش اسرائیل طرحی به ترامپ داده که ظرف ۲۴ ساعت تمام زیرساخت حیاتی انرژی در ایران رو نابود میکنه و جمهوری اسلامی از پا در میاد و وارد مذاکرات میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/89833" target="_blank">📅 00:20 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUcP2gl219nD_BpVvfkf43EPK7v-uKnTV-FiF-ANhgCpAaQWOzrpMmWYKfBF5H3rWnbuQ_sufFldx0cv-aKSSm_4Kuqql3GK5KL281yQkMy7_yMdoTFaTa225c9NYaTKoSSFFvVfVv59I6zAbH40THmlOlhrK5Ntkjas_P-8oEFqluXT7PdnZATAp9SXiQHVxiKxu9IOXc_WheamtoKS9or_y0LQKnifboKmDoVjt1CxZTiixHQhyV2fiYq037LkIpM3jEcp7zWO2_NscW4j3tAIlhFN8cGViZ77VtciY9MEi-QqibFaZN29Gb8oRXn5M18SEnIJPtkL_uaguuS8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آخرین رده‌بندی توپ‌طلا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/89832" target="_blank">📅 22:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89831">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/89831" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89830">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/89830" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89829">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تبادل آتش میان آمریکا و جمهوری اسلامی</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/89829" target="_blank">📅 23:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89828">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/89828" target="_blank">📅 23:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89827">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
اخبار منتشر شده از حمله امارات به ایران</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/89827" target="_blank">📅 23:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رئال‌مادرید به مدت نامشخص والورده و شوامنی را از تیمش کنار گذاشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/89826" target="_blank">📅 19:43 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🇪🇸
شوامنی و والورده از لیست رئال برای الکلاسیکو خط خوردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/89825" target="_blank">📅 18:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رئال‌مادرید قصد داره بدلیل اتفاقات اخیر، شوامنی رو در صورت رسیدن یه پیشنهاد خوب(احتمالا از لیورپول) به فروش برسونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/89824" target="_blank">📅 17:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
جزئیات درگیری در رختکن رئال:  منابعی از داخل رختکن گفتند که والورده از دست دادن با شوامنی در صبح خودداری کرد، و پس از آن جو بسیار خصمانه‌ای شکل گرفت که به درگیری شدیدی در داخل رختکن انجامید.  در جریان درگیری بین این دو، و بدون قصد و بدون هیچ تحریک از سوی…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/89823" target="_blank">📅 16:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKO3AE-noRw20q1BBc4yFxRIKtRo1ujFa61meO6BcMn6BGtleU3k07zi5uVfsoH9do7nC5ev4EEP9i8zdGtg5h3XffprbO6Dd6vppsKpVgtkpBIcU0gj47z-DbAp2IuJuCWXnHyszjHE88PnfJZG_OoOX4dUa0syHK0QwuR06345tg72W6GGcThVL0HcAr10CZF9Bumx9bXVwkqrS4XCsVRhSbzAHM_zr2OICpfE3lBFHVeT7BVxq7kK-oOi-yBd1mbFH7oj7283A2ZF_hdHz8JonRNX4VqOWSpeUy7rfQeRVyXggz18sw-zvO7faaKDfQOxOcMWru0KAa1cfPS1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فرلان‌مندی مدافع چپ رئال‌مادرید به دلیل وخامت در مصدومیت تاندون خود، حداقل یکسال غایب خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/Futball180TV/89822" target="_blank">📅 16:48 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89821">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووری از مارکا :  در آستانه ال‌کلاسیکو اورلیَن شوامنی و فده والورده امروز دوباره با هم درگیر شدن و دیروز هم دعوا کرده بودن، ولی امروز بدتر بود. فده بعد از درگیری راهی بیمارستان شد. رئال هم جلسه اضطراری برگزار کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/89821" target="_blank">📅 16:45 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d80YQgTpjDpgfh4dskTwAmnc0R5W1Zmv20nTjI2d8vCZ2iJaMae2RlO3kVriXOJvcqUu02hljY6lY-9gMVDaWWuHwicyFzf56X2qy0yx2u5OZiT2o5lYyotiMe_ZjbwUh63NrxJUq-5Gw7ohxi7HsW9_Kcra8ZW7stdEJ-6iQK_4Ypn_T-iHRmeZkxp0GL-qjzjDzCzZ1DQhEYDCR_xkMhUZnmEJ_J7MnaW8PJHfUUhWhhhFWbUocPWV-1dV8vc6pho_-qL5lp0vkzvmiIseX34ZTlnU6_2QMd2fM4pHX5lwcMe3hshCZDHrlSTbAhD5i9RLZUi3b8uT5lF41FJVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت خونین رختکن رئال‌مادرید :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/89820" target="_blank">📅 16:39 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89819">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqXxeR4N7ekwVWFxWEjFIVVowm1zQ6i5Jk1_aNHWfM2ve2rRveMpzvwjrBI8g7RDTOeGOMNpQcdJIDkqC5f2WaPABldNw9-w2zIgYBia22NwBDCqlYTqDxOZa0yjUdkcIAU3CCypHkoUqf8roh-Ok3FKbiShSpIXMoDqQxkNiY7UyiMEfyWrsDqJxZMZrVNlLmbqCScsDo81yLRHEgm2OqnwyBinimAJ2GCTcvz5xLQi6mkCqCWsSho52i53cJXdn79priPTc3Yw2bDMIo-6uTyEhZNzzdpBFy9GiZ8MuucSAK_gTa6X8L37noQEvwuC3A_uZVguB6vpgSonaL7XPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی هوش‌مصنوعی از گروه‌بندی جام‌ملت‌های آسیا ۲۰۲۷
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/89818" target="_blank">📅 13:27 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سال 2019 درچنین‌روزی؛ لیورپول در آنفیلد کار بزرگ مقابل یاران‌مسی انجام‌داد و درحالیکه در بازی رفت 3 بر 0 بازی دو واگذار کرده‌ بودن در بازی رفت بارسا رو چهار بر صفر بردند و راهی مرحله بعدی شدند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/89817" target="_blank">📅 12:11 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1A3g6x6TIs6SUpR4kz5-v0HfLZ_lZbNdZcwtTZWFxL68vTok-e_lTDp1N7hgKiv4XDGGDzhYcnJTegMLF79nj0iaxda9RNtRgBKjy1fsy-aJMmfGVbs8JfYBGJvWJXfqi3DOr-dv1wrGFfQ3iXU1-OhSysiBB1tYSoSM25S6xFx7p7fqcIe7ckocCWAUEWdjgkEkoZnNWwCTOWE9WXf2N9086k6N8QqAiPqJaKnQ0fXfssgSLO_bmTWdktOQc5SbbFSVWkJ4qUL4nLJGtJN1LkPzKI8XFg89AJso01uvu0OxLJmVD-ehHyW7vyRgOIQXdpnbDxO64Qg1bg24L1ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❌
با پاکسازی پیج رونالدو از اکانت‌های فیک، ستاره پرتغالی ۱۸ میلیون فالوور خود را از دست داد. لیونل‌مسی نیز ۸ میلیون فالوور خود را که فیک بودند، از دست داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/89816" target="_blank">📅 11:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjbDyQ4KbCu0Hfeo7NLQAGIudOS2ojJrvc1KVosg3oFECHpB88ddVQOhoK9_UQxUsjVOBlMeVdsohQNlizouytRtLHwVRTy3v7sK-02tGb7qD3Q_r0FEbwmaskcVrd_aNgvfXnLJK0n2VHsmDd9uP5hN5T_nCJ6_JOq3dGYxYC-hMG_KrwDF0OD-SlNDjXan2OeED6zfoIIiElu5OS_hd46qwbT3qvTUvbjIYVZY0LE2s3BT43RVtJa8-1mzCXYAlWsd1ZUM1_Wu3ov0tORY_5vvWbYSTalwMkwOCr2wqm0WO5on8Oi5-Dmc9Di3lzRu_uvkUS7b_2ftEIpad35v1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/89815" target="_blank">📅 00:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89814">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/89814" target="_blank">📅 00:28 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89813">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/89813" target="_blank">📅 22:38 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
