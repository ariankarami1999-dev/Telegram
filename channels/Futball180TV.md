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
<img src="https://cdn5.telesco.pe/file/g7U6J1HxP7dtU5I_fruOC8dRL6CcPjl6zk-sNX2_7oCO78tif3bvlPiL2wvkcDJJmtqwZfbYGrCFoc2uSBsoVPLUwN63cgpYtEvrR8qNVS9brIsIV5qIq_AOSdAxGLi_z0SoyGw9CbDoZwkkssoGxGHEbYA5HT9lHjcHHnW4XGUNZBb5kYnJB2Qbf9iK4ubYhXSllWdsrwPPU2crrUZ6WBYgewllJJWiDqll4EqlUT2uz3lA_06Hky5FEVxx2Od4lesGODVNn9CpXj4fWpiA79tH0ZZy_6Cen8910t2G3EOYKtZgKriZDMAf8f7hNQHhMXmRAUI_QHKh1E1iZ1x0PA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 457K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 07:34:58</div>
<hr>

<div class="tg-post" id="msg-104111">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffae02c927.mp4?token=LncmiRhbq8B17C0VZ_oefA5DXCMW3XO_zRcZW6G6bpP6uo7xZB4Oo44nkeKowiw-nTet4OnmO97CduesQoF1fGIMpF2DkyheWOMxJDbgxlPgldSQeq--pCpJ5YGgKza70Vw7kCakt44nieVcRz5S-JvQ2OFzGmzjS4rjhgsnWShaBEvhPSAC9XufOhwKUoXmwt897--rKmZ0_sbhWb1z75-EDZvScesyEypL4YZTJ-0lxqtsa0WXGaGnr0DpxehIAE6TVc68CQ5myjP_PIdQqi-txd-ZGeg7_GhAvp98EjYJAexUC9Ky2f6LeNe0kG2jD2Dp_UY99dvvePX41eDNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffae02c927.mp4?token=LncmiRhbq8B17C0VZ_oefA5DXCMW3XO_zRcZW6G6bpP6uo7xZB4Oo44nkeKowiw-nTet4OnmO97CduesQoF1fGIMpF2DkyheWOMxJDbgxlPgldSQeq--pCpJ5YGgKza70Vw7kCakt44nieVcRz5S-JvQ2OFzGmzjS4rjhgsnWShaBEvhPSAC9XufOhwKUoXmwt897--rKmZ0_sbhWb1z75-EDZvScesyEypL4YZTJ-0lxqtsa0WXGaGnr0DpxehIAE6TVc68CQ5myjP_PIdQqi-txd-ZGeg7_GhAvp98EjYJAexUC9Ky2f6LeNe0kG2jD2Dp_UY99dvvePX41eDNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حسام‌حسن سرمربی خایه‌مال تیم‌ملی مصر دیشب یه مراسم تولد میگیره برای خودش که زن اول و دومش هم دعوت میشن. این دوتا زن وسط عروسی دعواشون بالا میگیره و حسابی همو کتک میزنن که باعث میشه شوهرشون غش کنه و بفرستنش بیمارستان
😂
😐
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104111" target="_blank">📅 02:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104110">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b18e42b10.mp4?token=tLJf8-eKaY_zDvvOhuEsER9IaxCurGvHdj3PKq-oK1GSLxbzlq4uq0fPnr9st2LLDWZRS2JmDY4Mw49_Ke-38CbjEtiLEVp-87c96mY1BLEZGHmkWsylCgsxp476q7mR9IUtd9lh5f279Bh1MManP9gK6Rs8Op7EeKmNQ-6h_tV_BBYl475l85htChSOWRKLB4PO6c-m1ZoVNES_ZaKn1U5S3t_uSW7xChp4p63J8CgA-NBVur4CQq0xUoNuuOFiC-uRweRvCM2gb6Mw1XRVy_FHG4fg-7VbuDtm7scffQ6FZftNIQFdEPEEoJ2gd8ZMgkJTQq33y3gIcq6I_mTieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b18e42b10.mp4?token=tLJf8-eKaY_zDvvOhuEsER9IaxCurGvHdj3PKq-oK1GSLxbzlq4uq0fPnr9st2LLDWZRS2JmDY4Mw49_Ke-38CbjEtiLEVp-87c96mY1BLEZGHmkWsylCgsxp476q7mR9IUtd9lh5f279Bh1MManP9gK6Rs8Op7EeKmNQ-6h_tV_BBYl475l85htChSOWRKLB4PO6c-m1ZoVNES_ZaKn1U5S3t_uSW7xChp4p63J8CgA-NBVur4CQq0xUoNuuOFiC-uRweRvCM2gb6Mw1XRVy_FHG4fg-7VbuDtm7scffQ6FZftNIQFdEPEEoJ2gd8ZMgkJTQq33y3gIcq6I_mTieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🙂
تو میدون انقلاب تبریز یه پسر برای یه دختر ایجاد مزاحمت میکنه بعداز تذکر کسبه باهاشون دهن به دهن میشه و در نهایت کسبه میگیرن میکننش تو سطل زباله
...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/104110" target="_blank">📅 01:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104109">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
عجیب‌ترین هوادار بازی امروز استقلال و نساجی و مصاحبه سراسر سمی‌ش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104109" target="_blank">📅 01:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104108">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB_fOQmCEl_L_XuiD8ZtX2R-unUDWG-gYqaQOi4G1o4ICCelND3lhqLASHPlv9X11V1Rcq1RGxe_8cx2hc1bqf1piF_mq_LTRc8ZekUMEKrhY13yBKIl1GTSn7vY75yqrL_YUvi0kygeHBpVlOu_ISePpbQMssHBpK09cJR_W9EOCCSYGt4hTqztTS3WWRlz13yFf722hytGUs2LrkvmilQGIGGL6G_vifyxbEaOev7Thqtm_PxyKWYKxPAyTHRrebAo00QbU7_Y6NESYhuG7PEDAXMxARG2m3ICxQakcF-BYZ-KjCWarmBUPOP-iKpgmmROqH4um1EtEHui0RfCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇪🇸
باشگاه بارسلونا در تاریخ خودش سه تا از بهترین هافبک‌دفاعی‌های تاریخ رو در ترکیب داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104108" target="_blank">📅 01:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104107">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKEkAQCFaU4BQ1vqrarBKHtD13NtcWIZn04q23a2GGO0EgN85-SkGTLXDUV4g6tpNFeb-otvwqob9xzSMO03pi0dSVhLOENkyK8_Ycv_HOK6BN2ZYL6jtFLCokSpYCEQ7YZizo4hjnfRWPH3asuJIbYMKODlG8cYXJPXa4dIpsf_-_ubO8LiCE-D92er5K9gtYfegyRhSS1Rhf4ROgzQ-Um-aLtr-ng5slyLPubcWWuF5NwWIPWjmOUlbwjKh65-5Wzoi8hZn5dnpafe69zuOic3cXm0XMtkjZ4Dl_fFPcQzCwdS6AW8DuoUvjnLZnE5qvHwOwz3n6tearZRghopPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: الهلال اولین پیشنهاد خودش برای جذب واتکینز رو به مبلغ ۴۵ میلیون یورو به استون‌ویلا فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104107" target="_blank">📅 01:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104106">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!  پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!  اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/104106" target="_blank">📅 01:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104105">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=HLGM15TJLW9s85IYgoC927o6YOi_8WQIFmGRxoSe2_iT_fVOFy-Oyi5dd2ClrE2yCnG7iBCGKZ1e80sMcX1JsL23CL-gOke23z40E-6OYs87d3T52nNquYRwMK32gNiX7OXqFVvKj4nu5Rp-fC3a0fcU6rELqB_A7MC2va8wEO60Ys9YT1DAbteom-BEEiXfXB2R0wA03vkpZw0fLFxFmcf6NgE9ptF3l20C9QOhoSy6ZnPATn0g70cVMVrm95CL7xJnt-Sx-7OrguUErcSy6MKVLxPQHbdT2_bKg0vafbazUJa2sUxxC7awQH7OqxbYL_NDe52leIvoJvhZfBfYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=HLGM15TJLW9s85IYgoC927o6YOi_8WQIFmGRxoSe2_iT_fVOFy-Oyi5dd2ClrE2yCnG7iBCGKZ1e80sMcX1JsL23CL-gOke23z40E-6OYs87d3T52nNquYRwMK32gNiX7OXqFVvKj4nu5Rp-fC3a0fcU6rELqB_A7MC2va8wEO60Ys9YT1DAbteom-BEEiXfXB2R0wA03vkpZw0fLFxFmcf6NgE9ptF3l20C9QOhoSy6ZnPATn0g70cVMVrm95CL7xJnt-Sx-7OrguUErcSy6MKVLxPQHbdT2_bKg0vafbazUJa2sUxxC7awQH7OqxbYL_NDe52leIvoJvhZfBfYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!
پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!
اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی بازی‌های مهم ایران و اروپا
✅
بررسی ترکیب تیم‌ها قبل از شروع مسابقه
✅
پوشش حواشی داغ و اخبار نقل و انتقالات
✅
پیش‌بینی‌ها و فکت‌های جذاب فوتبالی که هیچ‌جا نخوندی!
دیگه فقط بیننده نباش، فوتبال رو عمیق‌تر بفهم!
👁‍🗨
👇
عضویت در کانال:
https://t.me/+nbm7Tb2pz8VjMDlk
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104105" target="_blank">📅 01:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7I4yRjO5f_W3z5n_fgJmi3pIqpgPIkhKzuVx1SaiicFAJnHoY15EpQFmPk-vg-19MtxG16H9-syox1S6hMJF-Ccxk4FVC2cxb1WGD7VagQM2kMVFH1zurrMwmrF-XxDX3eaDO-KidRp_S1AbDz0TU_arkM6pzmZrOzWYYIwUd0-khuzSfZFP8oAw2zcg2L15miS9S0EfhMn1EjvQTWceOjnzblfPUAOk3BQEqd5bs58Sq1OTif7jHI_h_FYTIylHs_8eHTVBGBQGfdN9erIHwcwkZFMIIeV3laQuGj5B2Oc9qx_vvtB6qtwb0rKZnb4qB6nC3DWWmzO0KjqOVGFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLSTAL7WxYZ4WMRDxWfmFtButWNYruxyyqef1Rnp3mJDVyOmCKYG_xS3WK-O5wYoTTXuJg-crSpaTvQpYhFL9md1Z6odxr-XBaW6I-BI7AX8z0zY9E2c84wBsxg3CvqUZz80JJSzwunH0b7DxAYuJOBmvmcglgJtGVWKIW8hDfeJAEeFUNj5GAra2J1oizRtnYj9jY_hU2_qbmc3zGIaqstKH2oUKLG9DCmwHE5uR2NBd2uPVyGI60NGs-mQLOc32kosIg1XTrFYtsjLErkITKyQI3pnElXQZ0-f3iblM-1UJH0kHyMKCBoHa1EGuzHP9d4yEJrzWWdGAl4UMBmYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDpt2VRbIzbDz6vL9WtyKSWa_uYKt9a-mHi_tYMSweeoX6DzHN4xvKPMpmlDQTRdvZfvHimCr7qe0yD-hoPnTVASft1wXmFe_DNf-ILiIEncaOPR69V56tt5o4Qo3vvbOMklzepghWzs57z4OSzERhOypVrvJyKXLa74eoz_GqV_kxQ8Dw_0UaAq99K1OEFKN_x6l6oWk2EDSUfjRuVfyEK6DGPz3dtzlqkdWXlKCrHMlTxUu81AJtq5NHCWhC7nnZchqkzHt4Ge2L5I3GC-R4FuI39rRgIKpX2GMzJoYWDWShxgI9-y6HzK81rbnGhC7CPvXnPxK0QZOux8pRbvCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روبرتو کارلوس نه تنها مسلمان شد بلکه برای بار هشتم ازدواج کرد؛ بازیکن سابق رئال مادرید پس از هفت ازدواج ناموفق، این بار با زن مسلمانی به نام "سهیلا طاهری" که اهل لبنان هم هستش ازدواج کرد.
این ازدواج طبق آداب اسلامی انجام شد و با خواندنِ شهادت مسلمان شد، عکس عروسی مربوط به ماه ژانویه 2026 است اما امروز لو رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104102" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3OXQCmSy_2m_H6IE49b1W1UQziAQ8PpL_hswMTYSEo2BXnOLsVeX7m0bAiW3pvN2IxiuYWeRz8X0wBi4AidZ-TU-MPJyI-9etCUiAtWPu6CuPyqha-jT2Ggf87L4ocQ2Y2qXOC__-iNDIwNJN7VvFobqhWAtLpvQhW4KY46274SCG0X0gMk1-T8vN_dYeePusdbjTE7KLqJNiuK3ZG6D3EViZAXY_7IlelM9mpPX5XEkKCDA1rriFypPSjbWyy3aqQPhqRLBS7lpW_Tc1avvO50LYRy0WtZy_n-7tZnBmweeJpDsMc0-qGD0Ll7SQmdOCiU5k0tXHTN2dgzOFvixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
رومانو: توافق نهایی بین منچسترسیتی و لیل برای ایوب‌بوعدی بسیار نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104099" target="_blank">📅 00:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104098">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loZQWpBQCRfa45VnyKyDxGTg930wyNwGdpL1wOKlnyyt0yETRkRBud8IPk05lz61RuTT2k8rXA029oigDxz9nmXY_QzMjGds6q4tJjC0wonAquDkBBM4OxsMDbZ-JaojXJcLcCmywZoy6RZz7Yx7jYKWcp0mvH04M2rhWGGjVzjLa4ugpE26DMeweEAMiD8kpkn3frNGiNs5DZ3jJF3bI_3yjTUa1l7F9OZ3uPWT528U8T7GBgRakkoQEMvVU4G5uVRo3TFkT_WhL0QsUCgk6oApyfgIc8mDbOzNX1o1dqQ4Peb1JrVLM_9OTYY9xGPZzc53NRXVf4EFHYeAuuAXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: الهلال اولین پیشنهاد خودش برای جذب واتکینز رو به مبلغ ۴۵ میلیون یورو به استون‌ویلا فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104098" target="_blank">📅 00:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104097">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/160d28a24f.mp4?token=N4uS4dkOga0RAZXrQLAgEYi7olZz_HqEzN7J9kFHUI3NmaQ_uINYMX8OTkDzzYVQzXEq6g89deb2P0wzCo5sbEFEWR72RooHgQv0ZsNCwVbE-NOT9lZUwhXKVvZNwt2SvABsrLzA5667PvC0wkRWM_9AqCLT1DmJxMxrs18t8Ry2MgiNdSdEYVA002mu_2Knq5Vm8eVQHFObRj1VdAle2C4vE7jE25Ziafx55aLlZeilUFNLYsETv9d4g5gGoSw-wBlQW90jx2dkg5oxqgNvIW8Okj4oAAJg2WYpKBaT70NLhDi1i97UV05Zv4VIFSXearD1KOCjIsLMTr450dxf1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/160d28a24f.mp4?token=N4uS4dkOga0RAZXrQLAgEYi7olZz_HqEzN7J9kFHUI3NmaQ_uINYMX8OTkDzzYVQzXEq6g89deb2P0wzCo5sbEFEWR72RooHgQv0ZsNCwVbE-NOT9lZUwhXKVvZNwt2SvABsrLzA5667PvC0wkRWM_9AqCLT1DmJxMxrs18t8Ry2MgiNdSdEYVA002mu_2Knq5Vm8eVQHFObRj1VdAle2C4vE7jE25Ziafx55aLlZeilUFNLYsETv9d4g5gGoSw-wBlQW90jx2dkg5oxqgNvIW8Okj4oAAJg2WYpKBaT70NLhDi1i97UV05Zv4VIFSXearD1KOCjIsLMTr450dxf1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شجاع خلیل‌زاده و بازم حرکت جنجالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104097" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104096">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
🇮🇷
حسینی، دروازه‌بان سپاهان: توپ‌ها جدید است و تازه دیروز رسیده
بازی کاملا یکطرفه بود/ از کادر فنی و هواداران سپاهان عذرخواهی می‌کنم/ اشتباه من، تعیین‌کننده بود و امیدوارم جبران کنم/ توپ تغییر مسیر داد و باعث شد من اشتباه کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104096" target="_blank">📅 23:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104095">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123f073b10.mp4?token=WOnMrIMwlb8cruPoQWiahQtwmGtv2uzFngoR42ZaKdeC1qMi_LIrJbstwY1uittZkVwIgo0IOA1oEfJj9l4fJSURvLemnZxg6kQp9-ZHXCiOfLbMg11U5E1uO854yqv8s0D9fzNLJf7zxZqvRyplzI8VyMFVpJXSD25HPXoixUXGWyt1zycg6P2ARIEIjsQpM_bfgsjcOSZz6pJ8blOpb0Zpu727AIFyh6wvQVLkMNDbzS_3OX7sDTsgO97MlANkKOXV8Zz74K2V3RiMCwfAPQuPZJf-hs3saLkrCdu83Lj0D5VfHgP94NR83lydE_XCWjJLRP0CrZfW5hT-xU6SikUGtIwqs2kq4mVVfm4zQKc2KgzN9FYmKZw4O3RAuqPYr4r6zi242owxq0AtFnFvUljUuF5by_NSvhit-CFTKcU3J0VzlXqukqyNldMhCUfQfwDPQf7RM0eCDM0dLp3oJvMf1YHodg9voQPyZk2ydTfz8o8xHXd5_LPnJa3fWOoW_Yt5PsDYWlYSwbA3YpysQsPqOki19taOksdUozq95I8ISvuMJKn6Qgblo1Pqg_FExGHbUv9lOw5Rf9xG2o8ZvVa498Q22YIkS6oJgU2iDg7VnuTejo9JB5xhI8Ktwt8WvBZuWyYNxoyRu43jmy8oHIwg5DsWZIHDigSGuRTpAXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123f073b10.mp4?token=WOnMrIMwlb8cruPoQWiahQtwmGtv2uzFngoR42ZaKdeC1qMi_LIrJbstwY1uittZkVwIgo0IOA1oEfJj9l4fJSURvLemnZxg6kQp9-ZHXCiOfLbMg11U5E1uO854yqv8s0D9fzNLJf7zxZqvRyplzI8VyMFVpJXSD25HPXoixUXGWyt1zycg6P2ARIEIjsQpM_bfgsjcOSZz6pJ8blOpb0Zpu727AIFyh6wvQVLkMNDbzS_3OX7sDTsgO97MlANkKOXV8Zz74K2V3RiMCwfAPQuPZJf-hs3saLkrCdu83Lj0D5VfHgP94NR83lydE_XCWjJLRP0CrZfW5hT-xU6SikUGtIwqs2kq4mVVfm4zQKc2KgzN9FYmKZw4O3RAuqPYr4r6zi242owxq0AtFnFvUljUuF5by_NSvhit-CFTKcU3J0VzlXqukqyNldMhCUfQfwDPQf7RM0eCDM0dLp3oJvMf1YHodg9voQPyZk2ydTfz8o8xHXd5_LPnJa3fWOoW_Yt5PsDYWlYSwbA3YpysQsPqOki19taOksdUozq95I8ISvuMJKn6Qgblo1Pqg_FExGHbUv9lOw5Rf9xG2o8ZvVa498Q22YIkS6oJgU2iDg7VnuTejo9JB5xhI8Ktwt8WvBZuWyYNxoyRu43jmy8oHIwg5DsWZIHDigSGuRTpAXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇮🇷
🇮🇷
پیش‌بینی کاملا درست نتیجه بازی سپاهان - تراکتور و حتی گلزنان این بازی توسط هوادار تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104095" target="_blank">📅 22:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104094">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9b2a3476b.mp4?token=MtPfr6KFFqBynzQi3NIa5l6m0zprtywd9PqLfh5evTwheIhvjIKoOsgHBgeswgh_pzTbQM6P9O1Fc0Gpqfh_XeeLwphQ20Fx9qLnRC-K3tK0Zxyv7yo4yqHcJByHqowcuRPkiCyibeYdxFvjYhZMQ4FefAQygV7rNDHkdL1vsRXH7c2mXPT4eDMwGrD2nDrS9x5ufHWSSx63oIczuB8lxfGyrhPb_WUZDqYLYZouliVSHX6fjzjWrN2FhF8UzUOcCP9UZbd5ORAUECc-xY6aF4hurdHSjxxhvDVyohdTImJlAr-lZHUOv247hnS4xwH11TGU8Mf6zli5SeCrujocDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9b2a3476b.mp4?token=MtPfr6KFFqBynzQi3NIa5l6m0zprtywd9PqLfh5evTwheIhvjIKoOsgHBgeswgh_pzTbQM6P9O1Fc0Gpqfh_XeeLwphQ20Fx9qLnRC-K3tK0Zxyv7yo4yqHcJByHqowcuRPkiCyibeYdxFvjYhZMQ4FefAQygV7rNDHkdL1vsRXH7c2mXPT4eDMwGrD2nDrS9x5ufHWSSx63oIczuB8lxfGyrhPb_WUZDqYLYZouliVSHX6fjzjWrN2FhF8UzUOcCP9UZbd5ORAUECc-xY6aF4hurdHSjxxhvDVyohdTImJlAr-lZHUOv247hnS4xwH11TGU8Mf6zli5SeCrujocDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جشن ۲نفره جواد و بیرو مقابل اشتباه حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104094" target="_blank">📅 22:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104093">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHr3aJwSxGaM3-bmZ-GXdcQaEWCsthRu25SKN9lciTrPHNOdyTzTkZ9Q8T_hoPjTZu0PbxWC1u4utzy29Vq2tYxHQjSQXXmqFT8zlJmqaHiaEhHzuiqvLx9xHqbdyA_Km29TR5GwciCp4J3f6EVrJye-g5UMsJQ77vNfH3jdQfLqF0S9dCzUArFT_jj4HDG8blIGtE4al5kNZUd0TwPzKQe9XhC8-Wr0zmBa80lcOhq8aamF-b01MqzXH6Yp4Vg29H7tKL6wmGdPJmwj16USWDm34XhPnVfFJA-fVH9_E6fN79IDPunoZi2pr5Zx7cIB0fgF9YJ0CQ7wkCQwRBaUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👀
🙂
روبرتو کارلوس پس از ازدواج با یک زن مراکشی رسما اعلام کرد که مسلمون شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104093" target="_blank">📅 22:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104092">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ8PtqRw4EKFzGj71A5WlZLf5IsUudoOe2NNhexiNCPByY3zx4e5rLyTbIRbQNfebCZOzIuxKC6M10c8YYoLel8I7aN1nRJMNKfDHNRVX98S3U_P1qHgdXpP4C18UEbXRBZv4Goc_fqus7igK68jtNw2XlegV4kZB91Yn-k7b9fcJuoq8Yl4FH0NJ6WGFrdj7tS58BU0U9jdcKTpwanIPo7EXQpwC51Ff1JLcpbyMY5nEqGtYUj-tl8uR3WNVDqutUh6lp83XchZs8lBA7slw5jF26PC1SiFQfwf3i5AmNJZ5j9M9iziYtJnETKdn02uOy_UJbRXmkKR1Q6ujPyUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر؛ نبرد جذاب هفته به سود نکونام؛ حسینی نفس سپاهان را گرفت و تیمش را بازنده کرد!
🇮🇷
سپاهان
😏
-
😀
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104092" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104091">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAc98qVmknT0oniocdmM6ANfI2WWrwzK1lLn6sHuDFJy6Enoebf3g9Me5MR2-eH3htuPnIi1ApxMceXlwwCTo6zDYlpQb5zxfEqzOEUr7huIQvhJjr7fcgUhMRLIpShmpuOZ09SuY5f-aCJ2Hh6WzuD5-bdmKEGnblhScz0Y_ryF8-LUwftkov86ltPYDy_SEN851zF6MK-miXUke6rPVQ6ULLPCCXh01qbShQLB1RhL-8Qa1Ll70LekeAbgir6jH60jPMdgsxMEL4dWcTlsqJMsvj4wIzSsFG8NOoCHYrQmoT_L9ZH89fyUYb0HlgWGh7iDxIIUS1Kk5asGHjCGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر؛ نبرد جذاب هفته به سود نکونام؛ حسینی نفس سپاهان را گرفت و تیمش را بازنده کرد!
🇮🇷
سپاهان
😏
-
😀
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104091" target="_blank">📅 22:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104090">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e5746901.mp4?token=i7t0AQ7qQlfDcn62N4BWYyib1dYz_Itb8GOr78jl-DMX5geSIrez4Cs2GnpIyqjjks0UEQQt09ZW-3t0ignp-nyALPWTgJUuoLNkhenYjk2hh0bs0gqfVd5WxViD0W3dUXQzfmmm-E-CNcNgp3twVgLyd6Ylq8PbVEWPqwzJQoUGYwkFOVGFJu_ast-CgFReBGACSmZnlENHPkFbPpMbWUDVqf_G5goF321RENvTqtCv0odSMDLUx4vcIGBI6vnPQoaK5OcZiKYbvZfHI0ee-H95Bj5_54a2Vr7uDUZH9njamSSaII8VsAH3sRjm8gDIVzsT2aPEEHF2h6HTBT7_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e5746901.mp4?token=i7t0AQ7qQlfDcn62N4BWYyib1dYz_Itb8GOr78jl-DMX5geSIrez4Cs2GnpIyqjjks0UEQQt09ZW-3t0ignp-nyALPWTgJUuoLNkhenYjk2hh0bs0gqfVd5WxViD0W3dUXQzfmmm-E-CNcNgp3twVgLyd6Ylq8PbVEWPqwzJQoUGYwkFOVGFJu_ast-CgFReBGACSmZnlENHPkFbPpMbWUDVqf_G5goF321RENvTqtCv0odSMDLUx4vcIGBI6vnPQoaK5OcZiKYbvZfHI0ee-H95Bj5_54a2Vr7uDUZH9njamSSaII8VsAH3sRjm8gDIVzsT2aPEEHF2h6HTBT7_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل اميرحسين حسین‌زاده مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104090" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104089">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللگلگلگلگلگلگل دوم هم تراکتور زدددددد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104089" target="_blank">📅 21:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104088">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e506a7f6.mp4?token=bU52UDkVIX9Gjwp7ICFr-tf2RrTkv39ebClHyN6ygbA763AB77nBEMP_BlK0vVn-4PgbZxNCRZOym8eR70vdiPcHuy9F1ciqE8VMwJzI4xOOXf2aqc_UJs5-jSrHS_xvVE54BfMVsQIh9lmP6WtQq0hluOi45pGJzSeHsDzjhdJ13Z87-3873SAuZzY0eJe-Z_Ljup-7QxRZuhftbpGwMHJ5IPMYmXEHriD0JIPs2OZ3yleGBnPUyOC5K1pITqmxyVX54HETNk-1D39g7jhTAZL8dIZrZQWRJV5JP9NzGiVpVasTX3fwbqsNe-P_hVu94fc4W4QQYHfO8uIcnQCqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e506a7f6.mp4?token=bU52UDkVIX9Gjwp7ICFr-tf2RrTkv39ebClHyN6ygbA763AB77nBEMP_BlK0vVn-4PgbZxNCRZOym8eR70vdiPcHuy9F1ciqE8VMwJzI4xOOXf2aqc_UJs5-jSrHS_xvVE54BfMVsQIh9lmP6WtQq0hluOi45pGJzSeHsDzjhdJ13Z87-3873SAuZzY0eJe-Z_Ljup-7QxRZuhftbpGwMHJ5IPMYmXEHriD0JIPs2OZ3yleGBnPUyOC5K1pITqmxyVX54HETNk-1D39g7jhTAZL8dIZrZQWRJV5JP9NzGiVpVasTX3fwbqsNe-P_hVu94fc4W4QQYHfO8uIcnQCqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
حسین‌حسینی رسما و شرعا ریدددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104088" target="_blank">📅 21:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104087">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=oac2kjzQ1MFLesecVMG1KfV2v2Mp2hCycBQWtell40Zs6jTudNWAPe88deRzVqaaEJ99Bo44-2uKzXzEoW-_2gQpi7ZkJyGTr7TQMTTJ-YYBBwjAYREK44rKDy9ujFWMZv_gNIKhLGFG5gaX8ZLKGC1WF4DcnEu1Nf2qXcA7iGWP_8BGjg00wtzM6MAfd30k3UG_zH9a2RI_pY8gDCzSVU3VwdZMgQeZnUenKCUUJ_UK5YTVwREP3vhAanPmKRAGJ63ELgVzY3eRE3u5aJF_3N88JDZQKWhn8xWo-D809UhxxoUfZOh6AQf0bdcMNt6TB51tnurb-SSAk9Mxs9sSNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=oac2kjzQ1MFLesecVMG1KfV2v2Mp2hCycBQWtell40Zs6jTudNWAPe88deRzVqaaEJ99Bo44-2uKzXzEoW-_2gQpi7ZkJyGTr7TQMTTJ-YYBBwjAYREK44rKDy9ujFWMZv_gNIKhLGFG5gaX8ZLKGC1WF4DcnEu1Nf2qXcA7iGWP_8BGjg00wtzM6MAfd30k3UG_zH9a2RI_pY8gDCzSVU3VwdZMgQeZnUenKCUUJ_UK5YTVwREP3vhAanPmKRAGJ63ELgVzY3eRE3u5aJF_3N88JDZQKWhn8xWo-D809UhxxoUfZOh6AQf0bdcMNt6TB51tnurb-SSAk9Mxs9sSNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل‌اول تراکتور به سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104087" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تراکتور یه گل به سپاهان زد روی ریدمان حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104086" target="_blank">📅 21:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tttygppcLEPqWepFMuUYEPlSoqwTrPYd6ayXuFE3YsLm9-Szgy6338NXMOVgb0tQhf1r_gC46OK29UoRv5ckshAjZEfaQptjX_E2jPNk6M_w80FuKmwD3AR4iqqrwlvm9jO6xT9J-wwdI5XJkNhTrR4fiMvaAm9w1s3shB9mPN-2uKqdn0UgyCKQDrEQPQTQjJV0Qxr8FvRdAcs0XUL5-_ZEpmS3P7A-bR0DDFQW-yt_FCGRdknsdp25SV6bNFwwSqFHEhsg07biDOvnzEJmrOcWFrOewzcTvghwJXLaxGDyNlaYaDi8iDue4gYhe8Q-sJNV315VWW3DTJ_8eW3T3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇩🇪
گرمازدگی جمال موسیالا در بازی اخیر بایرن که با خوش‌شانسی خطر رفع شد  درحالی‌که دمای هوا آلمان حین بازی ۳۰ درجه بوده! واکنش مردم جنوب با دمای ۶۰ درجه:
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104085" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
به دلیل عدم‌حضور بختیاری زاده در کنفرانس پیش از مسابقه، خبرنگاران مازندرانی کنفرانس مربی استقلال را تحریم کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104084" target="_blank">📅 21:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818201b984.mp4?token=hYrfQ6cJS6QhreEBct4w96vWIW_z3yPTizj60-jVeIM1assjFxw__8VeX6jzzMsh4gAwc2WYYBw4cZZ505x3nmd7ZaQ6BLGqrHskfUvhsvviFIrmJiZhAzl8jf_4PjesxZQfSyVMslepVfaoFrL_KI8iAOLma8XtDYM9FsnQg7iHSOcWMDsH9FQ0ne75qgrqo51UhQPPv-IEbY_fSBu84mIiOPIWESZFrcIZ3eYwHjyjtjFuTlYIe2yXlLlxYjHDI-VwLPEilUH4-A1W66YweYnSqbEE9a6pD_Wjm0CAgS7BC_btniMHGD1rIpoSgeKRPtI9qQBw0LawsDlW8QuHEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818201b984.mp4?token=hYrfQ6cJS6QhreEBct4w96vWIW_z3yPTizj60-jVeIM1assjFxw__8VeX6jzzMsh4gAwc2WYYBw4cZZ505x3nmd7ZaQ6BLGqrHskfUvhsvviFIrmJiZhAzl8jf_4PjesxZQfSyVMslepVfaoFrL_KI8iAOLma8XtDYM9FsnQg7iHSOcWMDsH9FQ0ne75qgrqo51UhQPPv-IEbY_fSBu84mIiOPIWESZFrcIZ3eYwHjyjtjFuTlYIe2yXlLlxYjHDI-VwLPEilUH4-A1W66YweYnSqbEE9a6pD_Wjm0CAgS7BC_btniMHGD1rIpoSgeKRPtI9qQBw0LawsDlW8QuHEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
🚨
🚨
🚨
گریه‌های محمدرضا آزادی پس از گلزنی امشب در بازی مقابل نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104083" target="_blank">📅 21:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWyu4-8eeIzM84IimpApzcBLwXV4MGzaPvSK17ZaD8kOC_GhPwK5Jp7pEzjHCzVuTZXvmvrFH0_WrqL0ZjMhBFukpRqe3CdtpoCJQ96QBnprnQguPLwQDM11XYcsld4pG8MWk4Xh0gsJyjzITxDt8ofZm9_rYELuVux9x7Vrt6O0yyaDLvQqM1fk2unT1nMhQqfqA41o7tx0FcyizmxbEiJfC5ZyNL1Rm858ilaTk4YcuPAI9lLbTmdMQ133n-OjRLg8RmjxgCVDaZYeVSh7ZMl8s-UlR_jQRlOa7PuD3VnrX7qo7PC6Svgtucot8sdyyewugHg_6F5CDMPYGxHkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
پایان‌بازی هفته دوم لیگ‌برتر؛ استقلال به سختی برنده شد؛ فرشته نجات سهراب، محمدرضا آزادی بود! آبی‌ها با برد شیرین به استقبال سپاهان می‌روند
🇮🇷
استقلال
😃
-
😏
نساجی
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104082" target="_blank">📅 21:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e078a045.mp4?token=HoX7CSmxKQQbIAGSOiIBfxjcGvzJHwAnoZjar1JUsO0mqKuV6jNmtyw-FczQ356SeMpAcnwT6hdSIWOv80ACIENVGSre34g5Ke811Q0xEG66IrpggdmwBxlHSvVm2Ox29Y6ieflFLUekTt1qaGQPWSHSAuy8BZu1y-cTlfJh8UI_6avuqljHpr2awQvvfe0zxYhVaPys7Vq9IY-XkiS_yzfqWMzQRda-N0BcU4CRowgtEOzwEQtspJAtT_tsmOUqpivQwHUTvtFubGgZ9dur9U7Yw-8sorYdBCzmIx9aAWYoiwobKV8RWUjc5w0FVn89Qvq9MZPW-dqRcu19pH2VzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e078a045.mp4?token=HoX7CSmxKQQbIAGSOiIBfxjcGvzJHwAnoZjar1JUsO0mqKuV6jNmtyw-FczQ356SeMpAcnwT6hdSIWOv80ACIENVGSre34g5Ke811Q0xEG66IrpggdmwBxlHSvVm2Ox29Y6ieflFLUekTt1qaGQPWSHSAuy8BZu1y-cTlfJh8UI_6avuqljHpr2awQvvfe0zxYhVaPys7Vq9IY-XkiS_yzfqWMzQRda-N0BcU4CRowgtEOzwEQtspJAtT_tsmOUqpivQwHUTvtFubGgZ9dur9U7Yw-8sorYdBCzmIx9aAWYoiwobKV8RWUjc5w0FVn89Qvq9MZPW-dqRcu19pH2VzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل اول استقلال به نساجی توسط محمدرضا آزادی
82
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104081" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محمدرضا آزادی برا استفلال گل زد
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104080" target="_blank">📅 20:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
#فوووووری
از دیوید اورنشتین: باشگاه نیوکاسل درحال مذاکره با سیتیزن‌ها برای جذب نیکو گونزالز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104079" target="_blank">📅 20:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9CdFZREGw5hRjNo0_ifsZl35n6cv2SEBbVaVgRU36XWSEckH76ITzfc0J82Bc1OWCOFoYPwewkK0AF1IPFefaUTuUYcPhYOZ1R55w4ZkPUnptSJ4HpxSPKzIDO7ls_FYtDRjg4UPREFtudrmC913O_OmEVbD1wmAyB2cTPukeP2TxnL6YXBkuC4dLh0GblhZF8WWr8tQd4rhriXSrkgTYA6IHPuC_4LWlbBwNX5KS4VE5mju0ICATA1dzvRY5BeGFPMyAh_R43Wu6_2zDxgKUov5-IpeOh6m8Q_n4zkh0oMpflLcXt_yw7V_ZkRE-XXvr5v5zNIf8UhO1fETzH_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
رودری:
"گزینه‌های دیگری هم داشتم با حقوق بسیار بیشتر، اما بارسلونا انتخاب اول من بود، و این را به وضوح بیان کردم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104078" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzzx_5DYMvZ8CvQ0GO15kWqGCfR3gvqLTqefCrTcgRRkR3mwHmcUwTYs1orC_f2M1M2VTix0_0ojzM5N1bIasG8IHeoj4giQ0Oi0nlSK543QDTPwe4i0Z6IrbhEGQVUrsApVPbMPg86TZKykwisBwAdnNQzDURkQuEhk5CO5fVlkRFesH6Q2Irb_W2T3L-L58ZUAtCHjp5I1_91G4knIDkUMSzEy0gqYlF6VwrH9bnF0C6G5f8DKDT76byX23jJNtvsHBIG04b3lnsgveFKodGz42SglJrfgBmj0MOSJlzEwJgNAZmXOwZSgkaY8F-BJLbDHkxyiQ9Pr2gUR4P9rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
رودری در کنار مدیران بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104077" target="_blank">📅 20:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7wiOWX6ohq56fIWe2ottCQqsOmjtgPh0sJdd1F768zHh-cfbjbzuhEPvmXnQoRFPa-AARgeYBaV_z_o-UspbTWIajn8wS3uz7vnPF7yYCmHAsDdYElRZKnzADtgT6NR8UFi6egonc5hTR4Yr98riNwXaG6zWSiU-MUMWcydSV3rd4q9YrPm0aVW2gvuh1DEc7EQu1xcPWHQ_rGE5zLy5TjtjMN_GhEWB-mMU8SBCvJkt8INF4zWvQWUEHDtBP5zp45xGxp1OWANX9A13vHwqRTSQndZlTfAA0GWj5kDlUTmJmXLfspKZDhCJmaT8XaA2pXfpIDjrX4csl9P1Hd9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر منچسترسیتی و خداحافظی با رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104076" target="_blank">📅 20:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944bb3a08a.mp4?token=ZWMHwDLsNqINdPTs1mg4NwSHvG1pjGIByfVaoZ0cWScP8pZ_p7AI6mjbdsqeDVP2AsZpHA4qu-xRy8VayH02W4GkAsjBxtoiz4Sqo0DCkbpi9uKOsGll62zxkFJ3BdMvSXQ7OrQIiboese8ytU-H4gnhv33SGUNb3Nzw2GTqwxdQFl1CU3g9vOfg8nCcjiD43Fh9752pTP1d1buv-EnA0-x78Rdbmac-PO1Se9tcBykEudSNSF8hIP82RBHNZja283ND6_ykoTWU6GzQ4kzaVZTFBPIJUt5YPrVhbfSn4PW4m-OJh0QLqDHI2MCoZQ5sZtFu0TRwNhaGX6SK0fImZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944bb3a08a.mp4?token=ZWMHwDLsNqINdPTs1mg4NwSHvG1pjGIByfVaoZ0cWScP8pZ_p7AI6mjbdsqeDVP2AsZpHA4qu-xRy8VayH02W4GkAsjBxtoiz4Sqo0DCkbpi9uKOsGll62zxkFJ3BdMvSXQ7OrQIiboese8ytU-H4gnhv33SGUNb3Nzw2GTqwxdQFl1CU3g9vOfg8nCcjiD43Fh9752pTP1d1buv-EnA0-x78Rdbmac-PO1Se9tcBykEudSNSF8hIP82RBHNZja283ND6_ykoTWU6GzQ4kzaVZTFBPIJUt5YPrVhbfSn4PW4m-OJh0QLqDHI2MCoZQ5sZtFu0TRwNhaGX6SK0fImZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🔥
🔥
🔥
🇪🇸
تیزر فوق‌العاده جذاب باشگاه بارسلونا برای معارفه رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104075" target="_blank">📅 20:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szBGq6F9nqTc4z_yNz7EPDcFgWU3O2qDXEr4FuQhmN-KFHhrajICYJVeMjdykrUINPInIGhAssvfsNSoNKu0qvIuwvVcPgv_LLBAlteT4BlOpsonsckUvisAAongBtdE_ws4erRO-BxYf_gOTQ73idd9Cfq7q1p-OpEfQN0QHBWnv06HwOsMcWc4-tvKOKyJ3921tgdiWmDuE5mpkOpqgdpGyIA6wKEdAoUrAF8Hi__ojGkdR09pU7_pOo4nOJHRb1afRT81fskjSp0A1NSBNgeNn1-7zc-LNkh-NznvAJXcVjbJN1oIOm5CuXDINpUqUdibZir5y9lPrvXdX_D-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#رسمیییییی
:
رودری به بارسلونا پیوست.
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104074" target="_blank">📅 20:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🎙
🇮🇷
مهدی تارتار سرمربی پرسپولیس:
🔴
قهر اوستون ارونوف؟ هنوز یکی دو بازیکن دیگر نیاز داریم و تیم کاملی نیستیم. در برخی پست‌ها کمبود بازیکن داریم و نیاز به جذب بازیکن داریم. باید تقویت شویم. حاشیه‌ای احساس نکردم و اورونوف با همراهی کادر پزشکی به رختکن رفت تا برای نیمه دوم آماده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104073" target="_blank">📅 19:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anJdlhitVA0DosNu0A2OoGSL0_u9gJE1eAiyWBiVdqP3yCH-OreDfzkmvyoRkP_Mu_yji0kIprZi3x3oT18Ihc-Kf7U53KrezSN_jgYh089IjLI-FcQXypWFDJRNHZ6gmuceKmYyEYKDt6YoEBCbosoW4bhiALIiJdpPHY23qxxT7iW7FTW_OL70FhnRJagrOmh-V1pfNjWpGht3m-Z60n8okcAO9aCi8-NzYoo1drGG4jObhR7rJsM9WuCrUiW4RTaJ6FoBEmMGyQWYCLQ_1MulexOPwqcLyO-6iVIIAtbI9kPdct5jW2BmxaTW9AEqUhPNHKcFSgHawR_W1zcC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇪🇸
جرارد رومرو: احتمال حضور آلوارز در بارسلونا این تابستان بسیار کمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104072" target="_blank">📅 19:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3hB8gLfTc4_w6Y3WuNv_wdczP3IOMoXbVmRymfNlGHflOAqO3CmSQTfd8xc0bySAufdHlnt8jlGZkF932LLaUe4R6Ogvzp89UWmmSWCdZWp8YSof21FyTCO9eyLySVCbRprF5JFkBnIR6rGvET_vCulACSVTTqcbw86hj4NB3iIbFpw-S_AYsnHznSpQzUECdjjLyHKDEVXAmfav5W3Yfvq-7xMMW-Vw4pCVE7k7K1sYVElCQaGEhAo6nn4R0ZucFJOnhnBLoBW865pQDF6H5uUvIbGHejMV7Fw1z1Px_DwUKJenNEDa-9aF5RhI6y3kF6MR_VltVudfiM702tkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌏
🌏
برنامه کامل مسابقات نمایندگان ایران در لیگ نخبگان و لیگ قهرمانان آسیا ۲
✅
🇮🇷
برنامه مسابقات استقلال در لیگ نخبگان آسیا به شرح زیر است:
🔵
استقلال ایران – السد قطر، دوشنبه ۲۳ شهریور
🔵
الغرافه قطر – استقلال ایران، دوشنبه ۲۰ مهر
🔵
شباب‌الاهلی امارات – استقلال، سه‌شنبه ۵ آبان
🔵
استقلال ایران – الشمال قطر، سه‌شنبه ۱۲ آبان
🔵
العین امارات – استقلال ایران، دوشنبه ۲ آذر
🔵
استقلال ایران – نفتچی ازبکستان، دوشنبه ۱۶ آذر
🔵
پاختاکور ازبکستان – استقلال ایران، دوشنبه ۱۹ بهمن
🔵
استقلال ایران – الوصل امارات، دوشنبه ۲۶ بهمن
✅
🇮🇷
برنامه مسابقات تراکتور در لیگ نخبگان آسیا به شرح زیر است:
🟣
تراکتور ایران – شباب‌الاهلی امارات، دوشنبه ۲۳ شهریور
🟣
تراکتور ایران – الشمال قطر، دوشنبه ۲۰ مهر
🟣
تراکتور ایران – العین امارات، دوشنبه ۴ آبان
🟣
تراکتور ایران – نفتچی ازبکستان، دوشنبه ۱۱ آبان
🟣
تراکتور ایران – الوصل امارات، دوشنبه ۲ آذر
🟣
تراکتور ایران – پاختاکور ازبکستان، دوشنبه ۱۶ آذر
🟣
تراکتور ایران – السد قطر، دوشنبه ۱۹ بهمن
🟣
تراکتور ایران – الغرافه قطر، دوشنبه ۲۶ بهمن
✅
🇮🇷
برنامه مسابقات گل‌گهر در لیگ قهرمانان آسیا ۲ به شرح زیر است:
🔵
گل‌گهر ایران - الجزیره امارات، سه‌شنبه، ۲۴ شهریور
🔵
گل‌گهر ایران - المحرق بحرین، چهارشنبه، ۲۲ مهر
🔵
گل‌گهر ایران - آرکاداغ ترکمنستان، چهارشنبه، ۶ آبان
🔵
گل‌گهر ایران - آرکاداغ ترکمنستان، چهارشنبه، ۱۳ آبان
🔵
گل‌گهر ایران - الجزیره امارات، چهارشنبه، ۴ آذر
🔵
گل‌گهر ایران - المحرق بحرین، چهارشنبه، ۱۸ آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104071" target="_blank">📅 19:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_cG_IRVcTp_pKJ_C4GYx4q3YGmVCDRKmMFFzP3nC_Cr3hJDV_mW3jqP6e04N3utapA9gJVE7iVepe0EdJGNk8eSiMQViIRfshR2F6PxCsu1LwTklgB-6LeHIggmUOnK_odt7KUIc-jKkNqxDlMXAICplxeETAj_-1ev58sSb9qJGmgCW-49V1iejz4DN73_7WLlFhloEiaHjnMpwVTr8L6tiNWRg0S0aOmgqxCtJWo6wAS3jxRpRHgWxS6i7V_27O9QIjEkn52A0KTKX5hxkc1GvDUfM8crye1-QcXU4CZtWgj8yXwEWmf64BCJzv_vN38pl2WMjI8NI4q6DI7jSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
❌
ویکتور ناوارو:
‼️
بارسلونا برای پرونده خولیان آلوارز حداکثر تا پایان این هفته مهلت تعیین کرده. اگر تا قبل از شنبه هیچ پیشرفتی حاصل نشه، پلن جایگزین را فعال خواهند کرد. سوپر دکو همین حالا برای پیگیری پرونده مهاجم راهی سفر شده و در مراسم معارفه رودری حضور نخواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104070" target="_blank">📅 19:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKmPyrClGo59hjKyL0FES3YVvfOHERN7-XPLfnC-SPdFjEeeeTrEXll5UtIuQ8vpkH_V_PcBmKN9Hxslk8Q0MiW11ePdE2coJ_sJd-S7k50wJywWeVvo-qLVj6lGUEDEXB7CrGYpvkn6UUIfu-KfhHSGHC0yPHnlxqwFiCFFbCHEMEDl5ybFY6cFAuiHh7OARgzXl9nZbBxSCJlWJehbYT-4gc8pFzXHsw2sQKLBSau-RchbQtYjNwIqCVhbnLR_89JIvXFdrX_xw1pSkkJgIbgm7L6wo4fc7LKU9FmVEHjH2nM6aV7WqYOIHSWHE0H05Q0JdjD5k_gpPfSfJlEW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJ_8BDJYtSGSeRPLHSpDHFNCFLhyFlKa2GMeZdabLs5JtqB72ClIKHTtAY5guvlCfOWeF5cnylljltked228iHNzNHyJghjUzFuzvhS7be1XZ9RlTHZ49wTd1lL5t2Zcv5ICHQwZ96Ukf9p0vsx00CClJGd2icM8E1Qo2gmFOe5JKOwEtCsetiyNj38CWknPqoSDmV56fxlCnkrwOHDYYQKdoFIcDbL57IjWAmtEdothRAfGPq7f-SZi4MQRUUuhs3phk-A8gm2uS_m0LUxpCcGQOFSIyw5OsDMw6G9hSJ_Z2cJ6rYQIF6JDLQIaau8aKvt7phy7R_2Yjmnh_9jjtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ترکیب سپاهان و تراکتور
ساعت 20:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104068" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104067" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPuzZGEpX--13WxeBiFxeUK4bmEwfJPrz9G0L_PyMDhJK-XpU_6p8NTzCqOpm-TjgTVOPc287_Otkv8X35oJrJg7ufiZ2qCDBBszOIMJ69KBph4umscFVnYvx1TE0kSwmU4ifGi8A-vDkLang41LYZQ9-wY1o-_FsgnNtpZe3KFYYCYrotKUek4PobAQbNrNooHSIEi1lV0cHoAc4M8ubEam9hM8kRtGa2NGshKDkqqlNUPW0cdEA6PJ1R-rVuIwM8CtRWbF6hu3a0F-_uQ5iKmr1F5Hw3WPomushdCfJ0gHFZQhwfnJcu2_79ntzj-VuO6uWBJLK48HhxiJ50DWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g27
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104066" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9118e624d.mp4?token=uqZiF9PQQRUiqHB286Uxcsg5wjdiQ9VUBp8H0MC0maSq3qqYqw1mjz1CqxcejVhi6YP_WXw3zYrHKdHKoAxN_sRkJtK9H94SzQVeJ6gZCdeYL7MkXBVwDH02oLqum8TgWqiiJohzAvXidx0OADj8wg7l6EUyNjYY5QmxKmASpTW3SvcQ0ysIFMXgEtSmojcYS2yth174IZ91ctJMRfdBtt8CDRX_gd7eg1QAiADRPHW3Zo8USjrJ0e8l9YTZRMRTXTNYEpP2QJt_K7YNx6_qX4YYUlFc4mn9U6TKRlW5AReeKW09K62ZEatn9aE6IGhScM8Z87VuWE-mEkxUtkVUMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9118e624d.mp4?token=uqZiF9PQQRUiqHB286Uxcsg5wjdiQ9VUBp8H0MC0maSq3qqYqw1mjz1CqxcejVhi6YP_WXw3zYrHKdHKoAxN_sRkJtK9H94SzQVeJ6gZCdeYL7MkXBVwDH02oLqum8TgWqiiJohzAvXidx0OADj8wg7l6EUyNjYY5QmxKmASpTW3SvcQ0ysIFMXgEtSmojcYS2yth174IZ91ctJMRfdBtt8CDRX_gd7eg1QAiADRPHW3Zo8USjrJ0e8l9YTZRMRTXTNYEpP2QJt_K7YNx6_qX4YYUlFc4mn9U6TKRlW5AReeKW09K62ZEatn9aE6IGhScM8Z87VuWE-mEkxUtkVUMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🇮🇷
لقب جدید هواداران استقلال برای «رزاقی‌نیا»:
سرخیو بوسکتس ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104063" target="_blank">📅 18:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNY2AvSLQKZwYQPBn8X8k0cB-G2IXq3ymMFm7DpSP1S_x73UXZybP4uWDQOF5WSYWGje3-SaLfwehQLEHFQpSlONmBfZ7S79j_5qZ2Y0DPjr_bKHl55kBLHeJbzqrnM0kZdZGSwVjZTwUsoPwPFponpajzAXkJIhYXD5xmJO-QlogVdmpWN50iA70FLtpL0aZI1t7mpb2WHD_s1-cvMBm5WEJf9auDEx9SNcuJPQoEfyjTx6c8f5blmo0tBqF_qx5TAtBQqPJnpZgh27hLd4RzTzyS0flz6CVzXz6p80Xm_Ir3VCpjyrTPYJWu3TQmii2JJ9gs9oiNI5CqbYXIiWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
شماتیک ترکیب استقلال برابر نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104062" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE7n8_wd-fAHFQaCcBPhFZ0TqGh5oHQLq_MfoKs2qrj7sfIq931fOY48EKnWIkHKvf5rYKa1e4nKwlcKPX1kdsPJanE-FKw80gi1grEHKraVXrVViIr67bDMC9TH9ofrEw8Fe8mCDr0ZH5KFo9eufzmfN4J_FOhsGua9oQ-sKbrdBl8LDACSCZoUuetiZdpX1MFsjduHu22EruY3NSQpIQMx3G7YRzMgMErITXvA9UcFTjVKh98JBUdFgkEQLzO3ZBItRCLpxlTWWPMJxqBLKtzul760VGM9um65KnIzlfVA5q2GnbGvbbItb961FlLXV6Hw-6nIB_1evIC4wmtdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیبببب استقلال مقابل نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104061" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104060">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9049374609.mp4?token=tQ2GlijZAeLa5r4afMasridmoFBezpsVUDl1jJ6OUqnJ3MA-OEGnkFLjSbd8Jp6532qY_b-PxS1svK1sEzxg42ngmQHfEAbiFMXxlmWqajf-gMGkvAXJbqOZMUMzmyODfs2tBocrG71yPzqAtcKqZpAlNEZHUdCvYNUVJKBgX8COet05BssWuVAAfxnKET_760RxD7IPFr6EEOkVRnyQn6PyOhoiqeiYDs24mc7dpco3_XGXy3PWbe-hOyP3yo2YKQsFWpPRMx_KTNPW4LHjY979SosDwKTpsWxdOr0ZVV9Tzo5M2eNWaDznQ4pbKASl6LL9oC6rVL8uWlJFFsjo0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9049374609.mp4?token=tQ2GlijZAeLa5r4afMasridmoFBezpsVUDl1jJ6OUqnJ3MA-OEGnkFLjSbd8Jp6532qY_b-PxS1svK1sEzxg42ngmQHfEAbiFMXxlmWqajf-gMGkvAXJbqOZMUMzmyODfs2tBocrG71yPzqAtcKqZpAlNEZHUdCvYNUVJKBgX8COet05BssWuVAAfxnKET_760RxD7IPFr6EEOkVRnyQn6PyOhoiqeiYDs24mc7dpco3_XGXy3PWbe-hOyP3yo2YKQsFWpPRMx_KTNPW4LHjY979SosDwKTpsWxdOr0ZVV9Tzo5M2eNWaDznQ4pbKASl6LL9oC6rVL8uWlJFFsjo0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌های شدید هواداران نساجی به دانیال‌ایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104060" target="_blank">📅 18:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104059">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZQaDt9dZuAtzGmebUf1b4akTg_DXoVgMXrej7WhKITBjV67sRWKxhYCsVGOi1XxomZ9xsI2K3PaWytxMoJlCUnmr5W-oimM90XfzIG0wMqw4mbQWb1UsTZwP_lc4A_5WqezAamU9CktTNC1pKBEhvWD7I0ZDGo5OkdDSfHkW1yhcmeaadkNP8Nwx76u9Cf59729gEgr41c8ig46arvSDuoTl0evFJSlFrSxo4tBD7EVA5JZUii-aUGBBJ9K8Pppp1FUd12jyR2KfFtJk7Dnh_aHfy5Rbcf6tTfaxPTvl3V-iT7ZD-eyUfhelZHOmEEvRTFuCTdYHh_qymXYB0k9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✅
پوستر باشگاه برای بازی فرداشب با تصویری از اوستون اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104059" target="_blank">📅 18:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qojXp4PUvpfFwMkXOMZrdxDGJWavNktQG3tX--kHdhG4NShsSaw254ONeptD1F5CCc80BaUp35XNWd1xwI8h5nwKlDJ5r4vHMp-SoS9Ei6rz1rEtuKyjvR77O4bF9qS2KPXfVBClI6MZqBOVdx3XA5J_apqkWhZMOBx-AP36XKaxI4ZxszVHdASGaCc9KleoL7QZyJH60STkTcVmJy6PoAaHdUZEVaNH9YLhdYsOooxB0QK2e1_1TTTlMkRxGg4S8m6jnrgRd7m8CWcfcdrBVkJu0K7g_j4vZBz-IRUelHG0Qn6Vp-J8a0OuIuAPPpSH5mLxBxsof_oDEKYsYrMz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه HERE WE GO که بارساییا منتظرشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104058" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba95804b8.mp4?token=Zjm6_LiROycYhhoUD2yXN38NHuekPlgvqEiewTd9IWpNHlTm-DJ_t62w9VBb5WPFVfnMKp6KoF8tOYX-G01opFO-Lqfwf0Q9LaXo297iRE-n6FKWFZTQ0G-RRJx6MGcLdkBd9dxEMPeDrewSvrvYcpnOrrVUDflTYZFs1ZjlG7Dn09hQMp_Pg03eh4EVfZshWBwSTMq5EYcEMBrsei74n5m97rwnI7va-6iTo2_liOPMXnBNO_eWJpnDbhNVg0yJLUPOZV6Z1PbtUiNVseNSsN_KVPno09dd3TTuTXtfjVikvq5W9kTzljxw3vmT3_Vnx2rBqjGmG7Xgey4T_X2Q9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba95804b8.mp4?token=Zjm6_LiROycYhhoUD2yXN38NHuekPlgvqEiewTd9IWpNHlTm-DJ_t62w9VBb5WPFVfnMKp6KoF8tOYX-G01opFO-Lqfwf0Q9LaXo297iRE-n6FKWFZTQ0G-RRJx6MGcLdkBd9dxEMPeDrewSvrvYcpnOrrVUDflTYZFs1ZjlG7Dn09hQMp_Pg03eh4EVfZshWBwSTMq5EYcEMBrsei74n5m97rwnI7va-6iTo2_liOPMXnBNO_eWJpnDbhNVg0yJLUPOZV6Z1PbtUiNVseNSsN_KVPno09dd3TTuTXtfjVikvq5W9kTzljxw3vmT3_Vnx2rBqjGmG7Xgey4T_X2Q9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
🇮🇷
هوادار استقلال در اصفهان: فقط امروز طرفدار سپاهان هستم/ تورنمنت سه جانبه؟ قهرمانی حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104057" target="_blank">📅 18:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1f1fb50f.mp4?token=a33pNwjnk3XNcEJ4lx6_piB_AEU_B6sahHU2o6yjfSQKQiV0IIc_mlV-dDOyg9NOl_1AD4zgMJXGkL9iJQx9lrWODy7LcpCUkIwNkiALQHrEsbCl5s6q3VQXwe1QOwKDpJ69AqCFXtOUxw6uKW3xffk5p3UFVsCWailTqX3ezZ3wLi0bV2e0ErEuZzaDpveEqudJjYoe3xIHF4vagPHa_37BXCjTUPEhbvzqcyDhVxngU5D6esOgRBeZX5RrxyV7or9QOqjcyxKLEAUA7cpbbzHiWLqq2BH2NruUsDt4o79cjIGEsGPJru4XZz0qH6Hj0AZO56PpsMwaJky6olG60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1f1fb50f.mp4?token=a33pNwjnk3XNcEJ4lx6_piB_AEU_B6sahHU2o6yjfSQKQiV0IIc_mlV-dDOyg9NOl_1AD4zgMJXGkL9iJQx9lrWODy7LcpCUkIwNkiALQHrEsbCl5s6q3VQXwe1QOwKDpJ69AqCFXtOUxw6uKW3xffk5p3UFVsCWailTqX3ezZ3wLi0bV2e0ErEuZzaDpveEqudJjYoe3xIHF4vagPHa_37BXCjTUPEhbvzqcyDhVxngU5D6esOgRBeZX5RrxyV7or9QOqjcyxKLEAUA7cpbbzHiWLqq2BH2NruUsDt4o79cjIGEsGPJru4XZz0qH6Hj0AZO56PpsMwaJky6olG60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
فروش بلیط جایگاه استقلال در بازار سیاه در مقابل درب ورزشگاه شهید وطنی قائمشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104056" target="_blank">📅 18:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBcV3263nVSE-KU8olvO9X6SzcXg7vtva1EmHz6KKkjQvJBGpJO_3YM7TmPEScEzUpy5OpHB4rt7fBickQRndBPwbrU0sesNxN5gbrJ0qqx8hDux2RbgkSPbRyWdODtWggCDVxYK2nS9wBlWq-ml0siktyzthXUnJPfcKCHwKqricugTgKC5kCUoax4jy3wOBTMHJlA1JrcdM8TjsFXhQzSCloqjl8D68Nc1ZT2R0nUOhNhyhHAJQqHXDEGai172HPvgM87IV1J8RY3uhir4JISSjWczGeLPVW-ZjNvRo4DJTC1Sl6CRret8rDtpbc7ZhqaXXHvTH_BUT85qv1SszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خط هافبک منچستریونایتد تو این فصل پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104055" target="_blank">📅 17:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3846d0c4b.mp4?token=hIQ-cMHrEeWUl0jASesdHuhJYkuAgjrqmRry-_KM3xMKXDFJJc6hAv9afwQVVw84wfT5pPKxV5Ni-SF3Iq02PGaG5-3yhtIxf8Cuqv0YV51reYZRMQbAE8-JYA2nLHKlBqSmpAAno0GtOQ44Ouyqcydk8-Lg_YV16JTZMFq4QL8KPFsqXevAG1Cgfm0BZtgkJR5ECWP6lIdRZCQBBs3RymZj9SRk9p84josi1tOtRuuEGZSSPowOFm6xTvzMc3tB86MR8zNtD3kbvUYQ9wDvsIfMQkV4lOW4dnO-HQa0momiSBsqGDJkKZ96Qf1U0L1-kfMQKTPevx200C3pRokQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3846d0c4b.mp4?token=hIQ-cMHrEeWUl0jASesdHuhJYkuAgjrqmRry-_KM3xMKXDFJJc6hAv9afwQVVw84wfT5pPKxV5Ni-SF3Iq02PGaG5-3yhtIxf8Cuqv0YV51reYZRMQbAE8-JYA2nLHKlBqSmpAAno0GtOQ44Ouyqcydk8-Lg_YV16JTZMFq4QL8KPFsqXevAG1Cgfm0BZtgkJR5ECWP6lIdRZCQBBs3RymZj9SRk9p84josi1tOtRuuEGZSSPowOFm6xTvzMc3tB86MR8zNtD3kbvUYQ9wDvsIfMQkV4lOW4dnO-HQa0momiSBsqGDJkKZ96Qf1U0L1-kfMQKTPevx200C3pRokQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه یارویی علی‌آقا دایی رو گیر آورده شعبده‌بازی انجام بده که اسطوره به تخمشن نیست
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104054" target="_blank">📅 16:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqOvGCoDNXIpii9hAkK06VIfBAn-KDKTP2Jev_JBJmyuthEWzqMFKmnfhcNQ9LT_SRM6Dj_5HqL3rNX10ZF9OJOmYkZH2_ahqOoyNWI_TNAmGKPBQbos5dVPkA3JUkDfg6F2UIHse4knN6O7u_x5W83apHxhp46jk2EK4L-_g1QjQAIiTbh9Mp9OF4dPmA6h0Fxi2svQbvCG8T6qzOb0KP7cm1WUFqDFhKkZlupMCegDR3fcSI5LbKNeAE0PAORGdYDqbUuHKP7ExJ51Yhzeq7BnOHUqO1ntEGz8E-vLB9pd3qzNANfpU4y6hA49M5TXCfoktQWXjdijXxlYR_in2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104053" target="_blank">📅 16:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcgJ4ZMWGtY0ijbGQVWvd4aiD5USLzt-W75oOlPt3W14hKI41QVtd2yq_i-EKGPTkTgT0W-VXZODuO4qjcg2uyBFTvj5Evc0KyUxQF0Cezo0cCi7SGNvPypbmqDed74IHENwHAbbD23hEce3HXfKI86OrGfziAvckOUgFO6AEEVVPw89llb6DEjoUtYeEcVedzUYphxMk5qFJ6KPmNlR9j8CzxopUyKc1jL4oPdHoO0URttfdxLq8CsF047aZl03sfoYP6qmHgLY14XiQL8qoVh3phoAepjLtCFiQiJ6spIBQi-OjGb8Blxjdqy0RpSsa04LGKgu_QtKd95iWftlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ برتر ایران
🔴
نساجی
🆚
استقلال
🔵
🗓
ساعت ۱۹:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104052" target="_blank">📅 16:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426246250e.mp4?token=KayD5JcNXMZmvZnTiS5MSHsl8RtDVN-Nb1nGhXksZp65jfoSWAgO0gGGKd6d6pzxA7SOkSq2YjUTSRbii60YMufHkxRvGKi80WuvQ-LVoSKI0Z0--DdlD-sduDUWzUpNzufn59dRXTMuNDlcgmEUZ4v_5km0v1eEBb0ycYVoLO99E5zVidVDxZF8ggrutoeTO7_b6CNjOnowTJahUaY7BV6PYzAKy-g1k5d-ZnvulA1sUXTd7mrk9T64C6saW3r7UQyFakD2kQlq1DfScH3J4WfnLYT1EpheSgICIREAX4frUF7l-4Vcspm16zz_UztOsaenOg9Niy-xAfWVhZmBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426246250e.mp4?token=KayD5JcNXMZmvZnTiS5MSHsl8RtDVN-Nb1nGhXksZp65jfoSWAgO0gGGKd6d6pzxA7SOkSq2YjUTSRbii60YMufHkxRvGKi80WuvQ-LVoSKI0Z0--DdlD-sduDUWzUpNzufn59dRXTMuNDlcgmEUZ4v_5km0v1eEBb0ycYVoLO99E5zVidVDxZF8ggrutoeTO7_b6CNjOnowTJahUaY7BV6PYzAKy-g1k5d-ZnvulA1sUXTd7mrk9T64C6saW3r7UQyFakD2kQlq1DfScH3J4WfnLYT1EpheSgICIREAX4frUF7l-4Vcspm16zz_UztOsaenOg9Niy-xAfWVhZmBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
😞
استقلالیا وقتی صحبت از نساجی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104051" target="_blank">📅 16:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2dfd54d.mp4?token=oXVS-X-jHjm0lKC8AhjBEfhjZiShAwW-FZ0CGlbC4Z_Zenq2CmygbxUodP9o1FTdOoXpkaLVv_BTwVEr2x0zJOubj_AG_oJch25arWq9EmxaEMgAxBN0tZhkE4dH7qV1WqbUXiWAB2Azym7Sg-kg5xdBzgs-R7m33xae1pWd5JiGnV9atZweoAWKMVIZ9WnBdewSOVdpJawIgK4mBIZkWYb95A4hpDjINyKFHMH5UMcGvQ4Kiz8TZWlI-HOUJUJMQChRoCEs7hQ_vNY-OCpW1V2HsDNdyeGq3HDwTGbvsu8LeJOZEhCTQKWaE1nIHKLV9xu2yhl6uibrfo3CDvEUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2dfd54d.mp4?token=oXVS-X-jHjm0lKC8AhjBEfhjZiShAwW-FZ0CGlbC4Z_Zenq2CmygbxUodP9o1FTdOoXpkaLVv_BTwVEr2x0zJOubj_AG_oJch25arWq9EmxaEMgAxBN0tZhkE4dH7qV1WqbUXiWAB2Azym7Sg-kg5xdBzgs-R7m33xae1pWd5JiGnV9atZweoAWKMVIZ9WnBdewSOVdpJawIgK4mBIZkWYb95A4hpDjINyKFHMH5UMcGvQ4Kiz8TZWlI-HOUJUJMQChRoCEs7hQ_vNY-OCpW1V2HsDNdyeGq3HDwTGbvsu8LeJOZEhCTQKWaE1nIHKLV9xu2yhl6uibrfo3CDvEUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
وقتی میگن رفاقتا بو شاش گرفته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104050" target="_blank">📅 16:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea98bda8c8.mp4?token=G3m1Ato5HsdvZAN4SFe_-AsRmEZTfYL3mLDw8T6tRriARmCKhnN9LswzJ1EYOVMiOuEtJ5lkJut02lFVAlyWW-m8URve-yrF_ihSIDujEDwg_2fb1ixpLiYiUw-ZtkylEV3DO2FboRX4GkTj5UpzajJ378-rn54LsAFcpyBVs2zBqW6WUByvdqF_6iLvk4rkHXd1_NYHnEmjXyFXSabxUhkjvY_HRHMowP4Ea3TCicut9zyzFqOB4H4PSmMGdZRwQZKkHbIfZfQa7xgSgnCTrvZlst7uRDu7UERVBbsiA8HybbctBgjd2-iz9bfCt9PMAGbeFvOryfHWcpJy4LuhqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea98bda8c8.mp4?token=G3m1Ato5HsdvZAN4SFe_-AsRmEZTfYL3mLDw8T6tRriARmCKhnN9LswzJ1EYOVMiOuEtJ5lkJut02lFVAlyWW-m8URve-yrF_ihSIDujEDwg_2fb1ixpLiYiUw-ZtkylEV3DO2FboRX4GkTj5UpzajJ378-rn54LsAFcpyBVs2zBqW6WUByvdqF_6iLvk4rkHXd1_NYHnEmjXyFXSabxUhkjvY_HRHMowP4Ea3TCicut9zyzFqOB4H4PSmMGdZRwQZKkHbIfZfQa7xgSgnCTrvZlst7uRDu7UERVBbsiA8HybbctBgjd2-iz9bfCt9PMAGbeFvOryfHWcpJy4LuhqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وقتی رامین‌رضاییان از اساتید و اساطیر تری‌سام برای مردم مظلوم‌نمایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104049" target="_blank">📅 15:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df89bd7ee.mp4?token=YBWT3K75yo9LTKDg_3mp-NinNszP8gO-X4hvl6IJiTZJaMSv9tGYoIETa8Lff9H4AnfZDI68ze-PAxRe9hxabnWvqp5OGWZwo-eCtGiy654IiX0sy7CikYL_N0cCksmA_hWJQ7WfDoAR9N1bAuGcZlFeJYAJzUz_oxYE0-peflEFVHEmaH0b0c-lJCrvyUnBLfpUr4_3QHXyO_sxfSr0v2Ff9W_rVVBjU6Z3RjIDTwveN4h7HAXBBQ-KpLSDRwFnCvg4NQie1U1I9iWk4oPSFCVXljHo0nj6wCibOtYmf-ciXhFI_FEr7g7-dvrFuuRajp3hp0JFdytYLUsHvJeHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df89bd7ee.mp4?token=YBWT3K75yo9LTKDg_3mp-NinNszP8gO-X4hvl6IJiTZJaMSv9tGYoIETa8Lff9H4AnfZDI68ze-PAxRe9hxabnWvqp5OGWZwo-eCtGiy654IiX0sy7CikYL_N0cCksmA_hWJQ7WfDoAR9N1bAuGcZlFeJYAJzUz_oxYE0-peflEFVHEmaH0b0c-lJCrvyUnBLfpUr4_3QHXyO_sxfSr0v2Ff9W_rVVBjU6Z3RjIDTwveN4h7HAXBBQ-KpLSDRwFnCvg4NQie1U1I9iWk4oPSFCVXljHo0nj6wCibOtYmf-ciXhFI_FEr7g7-dvrFuuRajp3hp0JFdytYLUsHvJeHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
وقتی هومن افاضلی دستیار قلعه‌نویی اندازه گاو نمی‌فهمه و معتقده از روی شخصیت اینفانتینو قبل جام‌جهانی فهمیده که ایران با دست‌ پشت‌پرده از جام‌جهانی حذف میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104048" target="_blank">📅 15:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104047">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785fe1cdc7.mp4?token=masZTDVuxz7fAjkmYY_c-drzkNz6TCQAAbkNQ3_MAoH474-dxQUw2GEzlhOpBjg2mAKNj2pMjGArnmjszzFYBmsPjTF9FhIIBQVQ2ganr3DHS2tfiNaTPGoArVt7-lulzfCoRL8aZpKYlbS1OeohVFsan7jtKD3H7W1DQoXWOISoAdPCGCvyF3x2ka-olnsisCzqZSUh5NzJR326KBWirrtE1AbulkkpHC25mPLuJdR0HmAEkiUl10WW_YZ7FGoUHeK2M0uUkRpNCEOVewdIlQCBYe_EevaS5QcnePdlaLW9e-LGlNUAaPB403bNbjeMGBiLW4wWT5BbZ_NgrHEPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785fe1cdc7.mp4?token=masZTDVuxz7fAjkmYY_c-drzkNz6TCQAAbkNQ3_MAoH474-dxQUw2GEzlhOpBjg2mAKNj2pMjGArnmjszzFYBmsPjTF9FhIIBQVQ2ganr3DHS2tfiNaTPGoArVt7-lulzfCoRL8aZpKYlbS1OeohVFsan7jtKD3H7W1DQoXWOISoAdPCGCvyF3x2ka-olnsisCzqZSUh5NzJR326KBWirrtE1AbulkkpHC25mPLuJdR0HmAEkiUl10WW_YZ7FGoUHeK2M0uUkRpNCEOVewdIlQCBYe_EevaS5QcnePdlaLW9e-LGlNUAaPB403bNbjeMGBiLW4wWT5BbZ_NgrHEPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
⚠️
جنوب ایران فدای جنوب لبنان؛ اینو یادتون باشه بعدا قراره به کارمون بیاد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104047" target="_blank">📅 14:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHahc2KSKEXdd47xLe5Clh5iNe2NN8u6NmAOwMFWJWRim4bhTtP8DJ-vMGkvcxpNfwALS_SPwAWR5FZQsuj0fUQwGeffcgfI0lGyuWS5VM0c8-6je_XOdlW2upAddsZEUk_jvhbsZlanc6J_rqCRThNsX5FKTmSiE9kcdu6enAaJZKIefiJXurmqIWBU59L06jJzLUPf8ImVgVP95LmtQ80RL08fhc0ROoNclikMBAiDISZm6juzeUHJgLmujrg7UNWHEtiCpXm8LkcHmmCBACPFI4dUrWnGaaxwcjDnw5or2kJFFD0n2TuwjUip2JBxVYR61RMnfbMnYZY66-I7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه هزینه سه خرید جدید خط‌حمله تیم فوتبال پاری‌سن‌ژرمن و دیومانده در رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104046" target="_blank">📅 14:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104045">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ac47d0e.mp4?token=X6kWoC2dDD8Bv62b6SpBFOjK9hV53sr2GIblZfh6yYNlSl2ce0ZJIMhL9HtPmkIaM4tFCjYtv_idVUwr9oz0FvCIW-myH2-EfBcuilgFT3wz5vTRjlX2ZscmojF_ouZqnBCt7uhohH_sZIEC5bCNiX0sC-d5I-apEghHAYJIhh4NtfK6gx6R8LNOFC2VVgaOxGD3HZNH9ID43XkciIyjjr-uov3Vi5fDCUtQp46q1BQ2aaFWC-U3LlQEuGFYQXymCTJA_zAwT5SDdPQtccLG7vG0fexeJPRu1I8llN9-rZaxVArcKdxZv0r5tBrHUlmjoyLUHtwt86EQKv-g46E7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ac47d0e.mp4?token=X6kWoC2dDD8Bv62b6SpBFOjK9hV53sr2GIblZfh6yYNlSl2ce0ZJIMhL9HtPmkIaM4tFCjYtv_idVUwr9oz0FvCIW-myH2-EfBcuilgFT3wz5vTRjlX2ZscmojF_ouZqnBCt7uhohH_sZIEC5bCNiX0sC-d5I-apEghHAYJIhh4NtfK6gx6R8LNOFC2VVgaOxGD3HZNH9ID43XkciIyjjr-uov3Vi5fDCUtQp46q1BQ2aaFWC-U3LlQEuGFYQXymCTJA_zAwT5SDdPQtccLG7vG0fexeJPRu1I8llN9-rZaxVArcKdxZv0r5tBrHUlmjoyLUHtwt86EQKv-g46E7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خداداد عزیزی: ما همیشه تو فوتبال ترسوییم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104045" target="_blank">📅 14:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104044">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX4_F7Np8uWF6QvdRyZQr4LOvUosaLakUi0UfjyN5y4caVuQiMo4kSpYcPLPoypelIOz0nWU5D6ZrYr6QtP1X6b2kJ2LvxlcEZXhhPGpe_ANRp-9_UjXeTT_5JFMy_ZmqdeC0AcTqiWfGDxByd92W1rUKI-qd5r_B-zlRTaycc9nkchPoZDDFLKwZBuBOwf2slOikPx9YM8OetABJnLJ9MuxHTvmNP2YAP1_TAcyKY9A2y7Uk6hD_-FoQu94FEtJNkAlnitl_MW7vhRAUxFEPforKF5KtRWRdn0iURdnQJLdBCcHZ6v3sG8mAfju3P38wMCKJxTHtxClAS_P2IHSzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
خولیان آلوارز
🚨
🚨
🚨
🇪🇸
🎙
دیه‌گو سیمئونه:  من می‌خواهم تیمی را دور خولیان بسازم تا بتوانیم از تمام توانایی‌های او به بهترین شکل استفاده کنیم.‌ حرفی بیشتر از این ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104044" target="_blank">📅 13:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104043">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0mXVuwGBrNw3gLywLhWpdXrSfz078bibm1udlAmevXkCck8fS8-CPfNphMAwm5FUXluR7j1d2mgm7VfsvT-yDu_NNhb4tO-7DRF1ah2HSKxJ6o8UKoz47QE_WtWEtKQtNfsNoUtTPf0DzMEhZ5PuiE79UAquhhqMpNN5Ny23j3hy9LMCSy-xY_oNss_f2r9EEL88_VhKQ9vRjPt3INQR_p-gpJF2VLibk4l9vwcy-ejHy51tDk5l42Bcx1gORY6IP3fA0uqnKh4o4bjH5bxP5Y5b-rZk64WSq4PyewC6_suAJpo6lcoJEWk1RCiMzOeWs461wtsQRkIdq5RPvNPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😍
🇮🇷
استوری خداحافظی رامین‌رضاییان خطاب به هواداران باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104043" target="_blank">📅 13:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104042">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⁉️
خولیان آلوارز
🚨
🚨
🚨
🇪🇸
🎙
دیه‌گو سیمئونه:
من می‌خواهم تیمی را دور خولیان بسازم تا بتوانیم از تمام توانایی‌های او به بهترین شکل استفاده کنیم.‌ حرفی بیشتر از این ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104042" target="_blank">📅 13:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buQiZCPdJUT0v8WphYNqVMsSk-ArNqn9wLdsT_29tyuocjq3lYqJLFaE0NgdcLkE7VOleBVuA8YyGAH8FRVGDU8ukEKx6WsVf5cQhyy3vGpE4iT-S7Rb2JQTXuOCKDWdvddcKQe7K2edEFECIL54TfyOikstqrfXvmL2HddSWerAfzKKHLN29wWt-7d8s2aHJ1Y_8ASjn8s_hrYfZHvEUpnPytOGPVTVmMos9x1RAJzdu2cIO8VfeEFiNASU3eEAKVeWYzs4SBVRHp3XAqp9Tp4QEejBZKUt8qVU4eFkyH6qLJwnaVDjLdumXF0sE_vYD6DOFffg9Vi6TOsWag8Fgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
#فوووووری
؛ برونو فرناندز پیشنهاد تمدید قرارداد با منچستریونایتد را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104041" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339d8cb9ce.mp4?token=nKrqdq_mAhLayR4pVR2FIbDZDKUhDS-OQ2YWa69sN7-2dZF6VxKzzX57B6UBeqzg1V-ZNI1d7zYeqL5xzNcPl3X-oo5xISMAJjWwNkK92znHgOr_hBE5tta4OacrUAsoNTN3MieUu7YXSM-JpLbFFI5Lx86eGAgeBzeATWtchK_CG9RNWp43StU2UxJDYiodJXBHlmbRZtc4t9VOpQf4_o9IrkkLtowA8M6RiAffL6SAUlzJ5jq8DLd-VCGvS3VSkzMGNT9pY-6OEWb7tHaHJ5_Qwt7kStxrGZUGLlxgoQcT5ifl2-4r4aGZPujqKhIRWGy4keKdwCegaDmp0Hc9anO-_WvLht-NxqpIxUiiIvv-9YbVtmuDqD4eMaST_HOQTggw3uyVB5cUs3tkUG28IeTeEQNwlHBm6w4qM30Gi4kiMNP_q7VPmca0mNEbcp4zqLkFk7oqAxryqwQsV3Bt8_Dr5UTnA4Hb7NG_Xl1D5wia7qUq5puG9EzJhdHBHotUYa-_Ux-90YrEHKorWYraBOIVrrFzy7SQlM1kWmTkF5OCq-4V6uCpn-99AFxzB1uc3YYof5tcfzFp-TXbZ2fUJByP5CGO0rRltN7gvygp92-MB5G_voWo1h7VTnFNq79N7QM_IRkR00LtD5yjfnA30PyzZA2IJbqeb_AP-ysJbRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339d8cb9ce.mp4?token=nKrqdq_mAhLayR4pVR2FIbDZDKUhDS-OQ2YWa69sN7-2dZF6VxKzzX57B6UBeqzg1V-ZNI1d7zYeqL5xzNcPl3X-oo5xISMAJjWwNkK92znHgOr_hBE5tta4OacrUAsoNTN3MieUu7YXSM-JpLbFFI5Lx86eGAgeBzeATWtchK_CG9RNWp43StU2UxJDYiodJXBHlmbRZtc4t9VOpQf4_o9IrkkLtowA8M6RiAffL6SAUlzJ5jq8DLd-VCGvS3VSkzMGNT9pY-6OEWb7tHaHJ5_Qwt7kStxrGZUGLlxgoQcT5ifl2-4r4aGZPujqKhIRWGy4keKdwCegaDmp0Hc9anO-_WvLht-NxqpIxUiiIvv-9YbVtmuDqD4eMaST_HOQTggw3uyVB5cUs3tkUG28IeTeEQNwlHBm6w4qM30Gi4kiMNP_q7VPmca0mNEbcp4zqLkFk7oqAxryqwQsV3Bt8_Dr5UTnA4Hb7NG_Xl1D5wia7qUq5puG9EzJhdHBHotUYa-_Ux-90YrEHKorWYraBOIVrrFzy7SQlM1kWmTkF5OCq-4V6uCpn-99AFxzB1uc3YYof5tcfzFp-TXbZ2fUJByP5CGO0rRltN7gvygp92-MB5G_voWo1h7VTnFNq79N7QM_IRkR00LtD5yjfnA30PyzZA2IJbqeb_AP-ysJbRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
👍
موزیک و برنامه‌ خاطره‌انگیز گزارش‌ورزشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104040" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpL2KCXZNy_FBKeq1d1kXiyBn-lRqkS5qVjWN9t-udVBFIWlFa3QF3urHYbf2Zg5EM632IGNApIQ9zpI00m0RoxyPEAw8hl2vT50uallKSWkm25tv54DmaknTSTKOzfFnVJgQGwDGI0sxvdOLlgXjNKXVXuFBy8UeU0rdb0bWKKV16INls8kGV_De6WZGpNd-gyEVqy73KwkNUAdNBeGa_yBiA1XufqoocARToRM6I3nPU4eMzGgV0LxtpZq6wZdGBuxvQMRB8276vGjI5ybtWFqjtCDg5x0PBYctJyMe-VMPfQoYq0rNYKyU1ZMudXwt-JB3I7EC444ONhUJxm6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
#رسمیییییی
؛ رامین‌رضاییان با عقد قراردادی یکساله به فولاد خوزستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104039" target="_blank">📅 13:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0tcSa17u4zJ2wytbSaJ1iK-slozNNGrXqhssMyd_RTTWulS3wLs_bQVBIWO31Jx-Pv5RaUIzSdAsC2-GdqvJ-9lQFMQbDB2wyC7-yzcPo1mOTrv4nqXjoI0fyxWf8AjugqL9hpgso8rMp-1IH-cR-xF1BnZGcRMv03StrVhNqwRPeh0px5P0_iykrDYe0WzOWTid3AxLf--RHONVe23Cc2Ic7MyuoP7arIZRh5VvJmbGCNXxMErQkkbOfhinyGhMlXEy-8CqfsY3yBszp4gazvkLrplzI4wQuPWZv4sXwvU7umOexDoWpkuUSmyvnpk8kMlVwv-3GgQB9jZuWAySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSzz4uhOcYAKIU6TtI5Ln7_02Xn6FNUiGDQaXJIu6OsHrYXOKBNugzvghnnLxUataj0mEdhlx34pSOipoW_pU5a_uW0jZrHZnSMaDHi6AWkahNzfPJ8_wiCVLTGBV_1PyHJjyJe3Wyb9QeV2Ie9N-DMZ2NwBHKvekgDPw-ay5ljRn2vwan5py1631zqzSSfF2RPf8Rd_HQq-2n9njF5k7cBeFABA6xKQgnKCmDlzz5NvX9M7LqhV0jw7T_N_E5-X_HHysrN61nmaVgvhw-A6jsrChgSbSB6ua0Cx7sd507Jm4ydv9B79ydWuiw3V9GRKcdEUxQr9DzPrLmw9z0ViFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
برنامه کامل بازی‌های ۳۲ تیم حاضر در مرحله گروهی لیگ‌نخبگان آسیا منطقه غرب و شرق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104037" target="_blank">📅 13:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9ySHt5iQ_4cBfboUhGWFThpdqeGpZNaEVIWiUpi5Dzp-nmUw8gLtVI2tRl5-ND4z1lSkT2njT92mehVMYLPZ1nSa8dbo3cgJLJDZ-qIRFIQABBRj3pMViuXtt2a3dj6TABtNBrpiBd_U1pT5UEY4u6Mq43tJj2Qd6CmhYQ6QQYCamME32DYzOiHYeWtuyzEcqrI-_jU9YJd5yKO2SPJbyVIg-9IpJnGZbZzlgYsPllWD105BdqzqwEuEvZklhg32sS09go5mYN_gzN2DWLAZXGUUtkQHh3jkbCChwEnDuvcpCg0PMCsG3vewSkE5zNHKh6YNhAbEtHiLwW7Q4adtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCKPFv5lC_uBlcfUd-FdiBW2ZJZ21gZnFvawv6WOYc5LlZf0MCorQ_eaJL-z8BOBoLSxLBxa5P_P_mzk_PlKgzgdXWo7cepCFGPyB3gZmxaPU1JN9KLGZlq-2EJtrY6ehs3_O77GWIP6TlbFBAvknUQVon5EYNOE-dy_U8YfDw3j0lDTp-7x4BnNlY1NnyaBv8VyFELI4K9AJtWSWUVklvPJ8DICF0u2NlJJlMFZizXN8A-cUAwasqVzmgbcRMKZPAoBOl2tIYbtgx3vnV4SC3P4gtzog-3s9hVjvk-2FA1KcjsSLnd5waqiGrNC54My6OxDq1-r7OYF7vhIEz_Wfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiZoH6OK6WVGdGjI0NP-d6A0-pV1eInSc9JRuodc0dh-W21fig1OzPxI0ZzpNk_PfSbCuLEmR6Xp_F8kivRhNT6xvt_XpXv3_i1AXd0DMFyKE2jfjmm6Ur_ZO9ZVLqAQLhJ9uY89EXVrza1Jx1d2yg_aMoqKraPcE8T7uTHS7BxCtVBn5d1efuVfq2yYH0m9O1IYKZPUwYkSiUgjtY1g_mNDUk4ogsZuQ6iKxlsqtysZQZTUPV5APMLtndunB0NvvQFHYNFzwWMPNlvBB6YJKfLhg6MElFX5HHa0_fP0_LuVN6unonSa3Jr1DRohkUrI-QoUYpS5SJBYtS0fd5TP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMhzDDZAd5P_QBjsut4WFyuBREEqrDqngcexfMnE7e0VgqrysJCZ099G4nbhK1LWwlxwT7JWXMA4Pfd0o2NfvPgVMVRBbyhJkEgSiSoNTIQX9KT0_bCRyfsHHbuzDAK3Ezy3IpZ8nA_Dnf4_BeGsK3H9n2BcCRgD-N6fvDJzdUTjWIXWP40piRGtygKRVwsVRzxUTBQMrYOaix7kpKZxKVX_6GPLng_hUsfOSXnBBjQjB6ViRfWzZ030uTgNDnsaRIInFUNkxKUVRjuk5K40zbOvL9ak9J149JOyPGBDcpupWAD6gjzs-S2qTlgHujRId-Mwoeuo9NlqYALOQSmtdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
رقبای تیم‌های عربستانی در نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104033" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8832387bf0.mp4?token=GnSJOo_52oPgPZIm3NgSNfrZEGMhRNqBNKZy-xoNWZuDHW3bgGasMI84AVg5X1dMlx0lS8bBYO7N8_8Ko98Oaq8tINtulIz8SFqfFrnfo1vujYtzdIFRtEtgCTE6RSDPo8p7SsPeW24sbkBopluI86lEX-j7oD5k93HCOvL31sOlYF6oRk2Z1vDyz1ttPG3NPxBa1izIHHRCQgleBdkj6pDYNOECCSt4RA2mA-2ciOYXP9lJm4VBsoV5HYRVe4KdB4NgSknuvIvP6oCln2oxwYc-PqXbbXQ5D9c_eWeNiN7L0RNA_Xz_w8izpwfgw0D-VC_VRAdcQR5gg3uPSS74OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8832387bf0.mp4?token=GnSJOo_52oPgPZIm3NgSNfrZEGMhRNqBNKZy-xoNWZuDHW3bgGasMI84AVg5X1dMlx0lS8bBYO7N8_8Ko98Oaq8tINtulIz8SFqfFrnfo1vujYtzdIFRtEtgCTE6RSDPo8p7SsPeW24sbkBopluI86lEX-j7oD5k93HCOvL31sOlYF6oRk2Z1vDyz1ttPG3NPxBa1izIHHRCQgleBdkj6pDYNOECCSt4RA2mA-2ciOYXP9lJm4VBsoV5HYRVe4KdB4NgSknuvIvP6oCln2oxwYc-PqXbbXQ5D9c_eWeNiN7L0RNA_Xz_w8izpwfgw0D-VC_VRAdcQR5gg3uPSS74OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
واکنش تند رضا رشیدپور به صحبت‌های زشت و زننده نماینده‌مجلس درباره مهسا امینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104032" target="_blank">📅 12:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104031">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBImMKjLuPA6IqvZXpJVkZzUscuiIVm2c0_QEJAck-_UKlhK9Vy5Fu4BxRiZxrD4RHn2DHhcgEboLoZeW_ygKZZMT5DB-b_pNA75IVqUDa5TIbBur9xufsWhMSQtespFdvIoRQPvOqtWEULu5JELkhuzBD896o6irGpfWiPFLcuiD-KGc6qbX_G5eONin7YcXkTXkoaVrOUTS9BD6PbStW1_u_uHHhUTNi0jMyNsoSly9slDn89UJflkpec35--eohSjRIwWa9J9d_XVUjE_ZwzmpYTtAu7sECqsJ5dyEovNStWQs0Lau1-r3y_WlkYM6Y3DhYnUf5wbJwOtAAVTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
تاریخ برگزاری مسابقات لیگ‌نخبگان
🟣
هفته اول:  ۲۳ و ۲۴ شهریور ۱۴۰۵
🟣
هفته دوم:  ۱۹ و ۲۰ مهر ۱۴۰۵
🟣
هفته سوم:  ۴ و ۵ آبان ۱۴۰۵
🟣
هفته چهارم:  ۱۱ و ۱۲ آبان ۱۴۰۵
🟣
هفته پنجم:  ۲ و ۳ آذر ۱۴۰۵
🟣
هفته ششم:  ۱۷ و ۱۸ آذر ۱۴۰۵
🟣
هفته هفتم:  ۱۹ و ۲۰ بهمن ۱۴۰۵
🟣
هفته هشتم:  ۲۶ و ۲۷ بهمن ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104031" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ370_OhlmzToN8l3rdYTX7-O9mdM73co7VYBjvVvB7RctoGhNyALp0fsGea25BRoc7J2xBx5bl0NZfvvHVPo75w7dZqb7BdhmQumUChv2b-Fp8SMYGLxgDgqXFMU7DJIJjSof5itukq1Owj7ACBeXuY2AQZ4os2uE03c_prRC2HXCKBjIfv4a9h2zY_Cj4mcXnkuQrofowt_FvfC_ZR54JzpVavWTmIZ-zi9vAZxsRVzNpBN11RbQRwy8WC4MrCfN7LeFOuXQbsVwG3F9XPu9fYekUPU_j-AYc8oVFTifFGQ5GrPDBobcYaJkmnLYr-xpGTuYQG9m2Y7O405-UFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
قرعه کشی لیگ نخبگان آسیا
🏅
حریفان استقلال: العین، السد، شباب‌الاهلی، نفتچی، الغرافه، الوصل، پاختاکور، الشمال
🏅
حریفان تراکتور: السد، العین، نفتچی، شباب‌الاهلی، الغرافه، الوصل، پاختاکور، الشمال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104030" target="_blank">📅 12:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
قرعه کشی لیگ نخبگان آسیا
🏅
حریفان استقلال: العین، السد، شباب‌الاهلی، نفتچی، الغرافه، الوصل، پاختاکور، الشمال
🏅
حریفان تراکتور: السد، العین، نفتچی، شباب‌الاهلی، الغرافه، الوصل، پاختاکور، الشمال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104029" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dru1NstaLBaZs-ER-R_Z5LER_-gPSKOJtyfEf6-IUNtzSgFWDUfIhDI509MqdC-Y0zQCnukY3xZn4cB0ac4wgTHCIfNNUOxmTxXPIVcCzXPRHpk4smSSCz3yQfEeSTbf3MZRQ4EU-86xWjPbVrtsxG1UiYtn48Qodf-nMXwizAy2RKBycKC149U4kNtccrqKvAt7K_TfMf2XHnGenqzliuhOnsmNQ0I2JAGIMvn5CnKZbHgvq5Z758ge6yz7jOrZTZYUEQ9GT-QcqBV48WcJB25qCwvJ46rb0fCV-hBM4pxf6Nwmg84VL0lvMu8wizZS4lR9bD44xCwM-D2wUZGPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
قرعه کشی لیگ نخبگان آسیا
🏅
حریفان استقلال: العین، السد، شباب‌الاهلی، نفتچی، الغرافه، الوصل، پاختاکور، الشمال
🏅
حریفان تراکتور: السد، العین، نفتچی، شباب‌الاهلی، الغرافه، الوصل، پاختاکور، الشمال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104028" target="_blank">📅 11:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔵
▶️
مراسم قرعه‌کشی لیگ‌نخبگان آسیا آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104027" target="_blank">📅 11:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104025">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXZvFwS0ToV-VUMTOSXScBvIJkh4BeDtqTJvW-QTFhoykJYr_4ZuRgQAK17fLWWyWdjjhWutQwiJUG37wAbRrRVHBqt9eRpAaLgsg7lev17RNXkF4ev421PshldW8akaVcNL7uyk2ZT9s94j4YfuHSw2jkE47ca5rY1VustZqvM6kmdqveWgyxrtUcDfvcOYwG02N0Sasi6HqbOUCs-brcc7wjhPeK4O7SrQ-1MJqRinLgoJ6xT3UrSRA7G5Goo3fsTVlDwDKHmJrLp3pNazH69LbJ0s0Q-TfRr6rH_-mEwapHRTNg-HKWxmkCgpHmh7nfkIOiiXmdfZSrhC4UL-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHM__XKVoQ6rCsT0PxK13m5RgXe-mnMoqNqRQ8Fcl_-IU6ueewXyUG_xrzAPifBDpil92hpJS55oFLeeSRm7Gcdls9xg-HOgvnWj-J4YidSHIfJl8YWuDToOPL5Nu-8JaMh3cK45dx7vd_zQBGBqnUOFPNOn9AOr9QVC-a2sNhEIU83stRqZsg3oylc4bH5DVp-Omxm_aU-PzqyF-xJ0ykGEhCRJRgaqSlxStCz7DZ5djjhm8QwbvNWHnPwBV0_WbRf5z1XZ4GydxAK5Of0_SkagLIg5wsu_mi5CK9Y1BrfALy7gVfjEXY9rXXdj082d2eA927gHjDvYSg76uuxYoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور نمایندگان استقلال و تراکتور در محل برگزاری قرعه‌کشی لیگ‌نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104025" target="_blank">📅 11:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104024">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d388dcd36.mp4?token=DjhhdAGii-tHsU5iOQzj-3x_4c9zDZd_VlAZjcmSaevdP08Xz0i_Iq4kJEfkzszU6eDV3mGTryofUknQdNZe9hvuu517Y0HqCur7Mt3lFj4wvbqdlM8N8D5gVCnylHh2v3LTCFuk4po0u2H1pNGK5Pw_2-WlX7J6GCOz7mnR15XzJK5yldRDOjO3J2wXe8GcUAhhkzs6uICxXM5qm0tc8U2FsIu3o8g2wQKZwIj7Jv78WB63Fi6V-R_iCV67yMcRnhNqXZ4Sw2X_NHYRzHRqP5lUUp1zRB05E6_JHC8MUUBR6-s0hSJcwffzryFEMNdK_IPNECQCkEeWN2Vup-nq57SdgUmL0eI2eJYv-K9KSu8nqlvYp9Se72Zwwqzx9yr8Nsw6MiKaIECkfUz4F0rVsqu19In2VeAUdBOT9uld3KpiLLPFFTb8UKji-k3_4CRPvmTvZ5Ud_q9CxENUeK0xWca2X639FooFqPECl9-_tGElCHOL3sLaP31j05ao3-anT2-796oHAT9cELzSTpms3nWmjCUsZtexZDEvmb4-ejMq_xlvcPGeojRINhoRaVTAcfC377VQVJr21HAaxUmYlJ2btqeT1jrb4yF6UKRx1Dd2_MA04-dl1qZ-sSNGXXxrB1bd2HsE82PvK8phsJeyysezaEXbP68M0HqwBvKJ43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d388dcd36.mp4?token=DjhhdAGii-tHsU5iOQzj-3x_4c9zDZd_VlAZjcmSaevdP08Xz0i_Iq4kJEfkzszU6eDV3mGTryofUknQdNZe9hvuu517Y0HqCur7Mt3lFj4wvbqdlM8N8D5gVCnylHh2v3LTCFuk4po0u2H1pNGK5Pw_2-WlX7J6GCOz7mnR15XzJK5yldRDOjO3J2wXe8GcUAhhkzs6uICxXM5qm0tc8U2FsIu3o8g2wQKZwIj7Jv78WB63Fi6V-R_iCV67yMcRnhNqXZ4Sw2X_NHYRzHRqP5lUUp1zRB05E6_JHC8MUUBR6-s0hSJcwffzryFEMNdK_IPNECQCkEeWN2Vup-nq57SdgUmL0eI2eJYv-K9KSu8nqlvYp9Se72Zwwqzx9yr8Nsw6MiKaIECkfUz4F0rVsqu19In2VeAUdBOT9uld3KpiLLPFFTb8UKji-k3_4CRPvmTvZ5Ud_q9CxENUeK0xWca2X639FooFqPECl9-_tGElCHOL3sLaP31j05ao3-anT2-796oHAT9cELzSTpms3nWmjCUsZtexZDEvmb4-ejMq_xlvcPGeojRINhoRaVTAcfC377VQVJr21HAaxUmYlJ2btqeT1jrb4yF6UKRx1Dd2_MA04-dl1qZ-sSNGXXxrB1bd2HsE82PvK8phsJeyysezaEXbP68M0HqwBvKJ43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
حرف‌های عجیب سلطان خر ایران؛ ویدیوی باور نکردنی از نگه داری خر و خوابیدن کنارش در منزل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104024" target="_blank">📅 11:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104023">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ0IqvYfmYgUAAFf9j36b2o_cvfYTlCxBsopAAqR7LjhQqn58Y_kuUK94QVLbH_qKS9-fMHBo1fTlg-_tee9NFDZs_9c0oYx5za65LtSlwmjuuz0ou4ABntew9aNUmeyV5SVhEtNagTr6ELAbbxBzXYL4VXdec1NsdwqPYp2b7kXbwfLCeMWeEh-pFeYGXLKL8tJqA0UyJ9tIbeQHZcr-eOH_qZ1fUIc_0-FZpenJ62Hw32heKtVOGwINpry-ugPeKiUk0W0DaXAjb7pXrWowQSIj-eMGWUE3PdTnGtmKqCsI9HAbvbrECyY2XwKdbxYULTZazlIMVbhv_SWdw1tbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
⚽️
تفاوت آمادگی جسمانی فلوریان ویرتز قبل و‌ بعد‌ حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104023" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104022">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/104022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104022" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104021">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=EaCTHjRkj1_qoc3uxsumit_MTAMaPliw0CYKDsJosHiMbLs0SZIjQvF_4X27sL1O4Ep0ddcIPkFWshNYZ1Yxg-XixmdKbaZJm6Tnacpu-JsnGH_vknfLk0nIqpivRB3SvcPCe1tlSouoPnidFeGpu24U0IPesCD7t6nRzkEkMG452U4mMQL4itEkAV0hEj_bIi31pB0RuSlNnWDThWTBhQJXBMMdposBzb3kjWLoUW6v9N0LTiXO3jrw7TY3pJvTgeGAIh5Qktg7M33im9Dk21zMcRDF-69IfzKx9GgBEU6uBx6y6F3VnCG0eLfuc1XqVuBIB_vBFJ3vR6doG2ckPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=EaCTHjRkj1_qoc3uxsumit_MTAMaPliw0CYKDsJosHiMbLs0SZIjQvF_4X27sL1O4Ep0ddcIPkFWshNYZ1Yxg-XixmdKbaZJm6Tnacpu-JsnGH_vknfLk0nIqpivRB3SvcPCe1tlSouoPnidFeGpu24U0IPesCD7t6nRzkEkMG452U4mMQL4itEkAV0hEj_bIi31pB0RuSlNnWDThWTBhQJXBMMdposBzb3kjWLoUW6v9N0LTiXO3jrw7TY3pJvTgeGAIh5Qktg7M33im9Dk21zMcRDF-69IfzKx9GgBEU6uBx6y6F3VnCG0eLfuc1XqVuBIB_vBFJ3vR6doG2ckPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
😅
😂
😆
:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r27
@betinjabet</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104021" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104020">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7cbf260.mp4?token=Wgs8VQr4GVvG54aK6tHzxjflUEc7MQscAtqnAD3OlCh4hWCG29YdptvDFAPP3hLus-U_gAqyRCdd2-_4AG6IsyJPYmcLZxfjFd9I6prcxvPuc_JgIW_TgjwITp1fEKen3AsQFQ4EuNKquU0MoWrdw6RyTaGBHftF_u1OGeh-3OEBr4fCCSwulD6pyj_fHnDzOfOkumX-C_Go6_x8fqcFNMqf0bvLOngpc9JX_A4NSFMxyhBE3xbcpS1OjZVEMb4ZmechBorYMeIp_5oCO5mR1wjaUwonaFJY9mTneAUUrm1ktmWmGE72rYHvjM1Ixiud3UywxfhP6rTM0SXpY46l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7cbf260.mp4?token=Wgs8VQr4GVvG54aK6tHzxjflUEc7MQscAtqnAD3OlCh4hWCG29YdptvDFAPP3hLus-U_gAqyRCdd2-_4AG6IsyJPYmcLZxfjFd9I6prcxvPuc_JgIW_TgjwITp1fEKen3AsQFQ4EuNKquU0MoWrdw6RyTaGBHftF_u1OGeh-3OEBr4fCCSwulD6pyj_fHnDzOfOkumX-C_Go6_x8fqcFNMqf0bvLOngpc9JX_A4NSFMxyhBE3xbcpS1OjZVEMb4ZmechBorYMeIp_5oCO5mR1wjaUwonaFJY9mTneAUUrm1ktmWmGE72rYHvjM1Ixiud3UywxfhP6rTM0SXpY46l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
وقتی مجتبی‌حسینی سرمربی نساجی به بازیکن تیمش قوانین داوری رو یاد میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104020" target="_blank">📅 11:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104019">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwLHozMHjcB7Zjazmw_cngwrLf23SAG-cjLMNsoPFWRul6wHMzPR_twtu2FSD3fVRXVsxu5zans0pvkLRqDVyXWFuZQTuJiIjd06wuLH8HBtZbaxHXX4FTBdwa6fnn5EEGd6uLFJxwrwNpgeoQJ3lCiVSgMKr4GhMx5thJVk6tNjatRfRxLZuRnmmVLoXVOW0wlWfW0cBi0V7siKDLOmjfZzDWLe7BeHr2vQkyp9RnBXu9inMc0n1gY745uorHmR7nacmx81mBop967pW1PN26Hn_oB50GVP00cGxbv5A17dm_AjnwCc8X8bqpG-FtDZ0UzmttTrAlBJWyR6vX4PaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🚨
🇪🇸
جوتا جوردی :
🔻
آلوارز برای بارسا بازی خواهد کرد!
✅
بارسلونا از جذب خولیان آلوارز دست نمی‌کشه. آنها تا آخرین لحظه بازار نقل‌وانتقالات برای جذب او تلاش خواهند کرد. حتی اگر این انتقال تا آن زمان انجام نشود، ممکنه بارسا در ژانویه دوباره برای جذب او اقدام کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104019" target="_blank">📅 10:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104018">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f82bbb56e.mp4?token=vrHbLVz4EYS8Gzi9QwddyMPuxqG8FrBVRe3S9PVW5tRgCGCsWMuDJVdp6ofpL4Il-9HVswo1B7nbPI7DbYinA4AbWaOGDwxSlaxYO93PLLS-RtrF7vSYcpefvEizG8nxzDLQKG6fDVUr0S-Wb9kLgfIY-BJ28VsP2ElmozBu_xdroeRW8tLc22SltqUVj9g_Hyj1DkV5qDfYksRCvks1mfW-Gz85hpYumGhbK6mYog2ob51GRwLUcuChgyhmWoWbQEQOwwFSUotfIwXgdBtlMk4gRljzJjBNiHu70qu94JiAi4E7ZS0UElF9tMcXdTaOxf7M4GlWLeQcsrQhfM8SKkSspDc3b7J33GGAIRjja71126VVkM5xFpvC-_nZStHDFCn6vCh4x0RkuuhR3WLCl__iwY_xjcrBd0tsVCr3nBwdnfuidA2z99FS2Hkle4Ctxq_cclPgZFSALJRE-WzAPNmTTHiGuKfs-6YTEZzbIOYe9-CZFshK6Gu4w0OPUQK3nTcYPBRp9Sw6eXdXW7qC9F2RamZK9qn5ZazW0IIijfaGfCRN_WarYwZijlORRrioWdGyEXpsLU_fHGTocnMttXvNPMslQFQVETqe9zirITEVY1X4n4aqltk0sciUNm6H27aJU26YJ7MDLiO_DgLH4sc_wKe6ewj6OO7lOr0aEn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f82bbb56e.mp4?token=vrHbLVz4EYS8Gzi9QwddyMPuxqG8FrBVRe3S9PVW5tRgCGCsWMuDJVdp6ofpL4Il-9HVswo1B7nbPI7DbYinA4AbWaOGDwxSlaxYO93PLLS-RtrF7vSYcpefvEizG8nxzDLQKG6fDVUr0S-Wb9kLgfIY-BJ28VsP2ElmozBu_xdroeRW8tLc22SltqUVj9g_Hyj1DkV5qDfYksRCvks1mfW-Gz85hpYumGhbK6mYog2ob51GRwLUcuChgyhmWoWbQEQOwwFSUotfIwXgdBtlMk4gRljzJjBNiHu70qu94JiAi4E7ZS0UElF9tMcXdTaOxf7M4GlWLeQcsrQhfM8SKkSspDc3b7J33GGAIRjja71126VVkM5xFpvC-_nZStHDFCn6vCh4x0RkuuhR3WLCl__iwY_xjcrBd0tsVCr3nBwdnfuidA2z99FS2Hkle4Ctxq_cclPgZFSALJRE-WzAPNmTTHiGuKfs-6YTEZzbIOYe9-CZFshK6Gu4w0OPUQK3nTcYPBRp9Sw6eXdXW7qC9F2RamZK9qn5ZazW0IIijfaGfCRN_WarYwZijlORRrioWdGyEXpsLU_fHGTocnMttXvNPMslQFQVETqe9zirITEVY1X4n4aqltk0sciUNm6H27aJU26YJ7MDLiO_DgLH4sc_wKe6ewj6OO7lOr0aEn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
ویدیویی در شبکه‌های اجتماعی منتشر شده که مرد سالخورده‌ای ایرانی را نشان می‌دهد که سه سال است هدف حملات پیاپی یک کلاغ است. او می‌گوید ماجرا از روزی شروع شد که جوجه‌کلاغی افتاده را نجات داد؛ از آن زمان کلاغ به محض دیدن او به سر و صورتش حمله می‌کند. حتی با پوشاندن صورت، او در امان نیست و کلاغ به افراد شبیه به او نیز حمله می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104018" target="_blank">📅 10:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104017">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STdwBvMdQaZa1jCZBWu8hFHsb5My-l1L9z09oMnCUYSVmlw7pSbULPuNaTvWzXkx1mHQuDrohmpD99edpVEs8yD_3qpMSojUpiJROlxhiaxX-yuEkHJOJKednusIYjbeSzSnEgwFgTrR2D7td-BZDvpi9mnUJdcbN0tOp_EW3PoNCnYMKjjryb0F65qdBFjEkvdY4Bbj-iY6onQqw9SxTGeDvQA0r4BBp02Zq4Evi8MvP1oV_VJaHOxxFGhsRl3Vw0lmvfWtQs8Vqo-J_aQwYDYErzPCrNw0Ppt_rVSqtydP9Ymh9uLrEmS1PemqROF5iAhI1e5OLg4vKBDEm5oq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تکمیل ۴ خرید از ۶ خرید احتمالی بارسلونا در فصل نقل‌وانتقالات؛ رویای کاتالان‌ها تکمیل میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104017" target="_blank">📅 10:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104016">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxDWSTMEiYjPjW8kTHkjWB8KyqOy98D2NGxUIOWoZdXBIlVWIEn9PySNmX86NaYLCzIS0bFo6BJPVkyMtfYPl7qkV3mzQa_QMX-hzICHX-uC73jgMSGbiFP4d-hpjZMo_FsscTpuGUDlUEsuSIuBS6S_b-zUf5u8IAb7uFFY9mgqKPqcvLOu-DTYpgZjuu1_hjwWe__sPx68do_w_pS7oRbj0WpsT7FG9u1o0p6RjSChqt2-Yi-8SYd5m_Ex6Q3q83cKb8AL8aBiXU48zK62bcKzDi51L5xrfq_tmnB--dQ01GNH09ewG0U66IdwyUC9Ovfyt1lH0_ygSfQShfGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
✅
🔵
نتایج قرعه‌کشی دور گروهی لیگ‌قهرمانان آسیا؛ گلگهر در گروه  B قرار گرفت
🔴
گروه A: الوحده امارات، نسف ازبکستان، الکویت کویت و الخادلیه بحرین
🔴
گروه B: الجزیره امارات، گل‌گهر ایران، المحرق بحرین و آرکاداغ ترکمنستان
🔴
گروه C: التعاون عربستان، الریان قطر، الفیصلی اردن و النهضه عمان
🔴
گروه D: الحسین اردن، الشرطه عراق، السیب عمان و بنگال شرقی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104016" target="_blank">📅 10:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104015">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bade9483c.mp4?token=frrqveSIAXo-L8s6sthIdc4mVMhfGabUy9xMB0MAyTutR7FENVipyjHe5ZpgdBo8k-2PNEiKh1u2xXPnLhfMVyGnz3O9xl8Hh69mlgT6cNCD7dMOpKSyoH1K3iaDOMCoI81A_1qMMsdntxYUOa7JoDkzOIOO_DFnIZBvgwdbXiD08J2SqDR9YRe5gM_NTUHf371J65kx-OpUbLOGnr1e1IKQ3B15-OPeJUkvkiNuXc4mHXvXoybf8omkuGrIiL9swnIB-7bU2bi7dNEehxIOWSpm_nDHm89sCTaQP335hre2asUWpItjRpdIJAtBCWx9Eu53fyg7XoUPfELQcspSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bade9483c.mp4?token=frrqveSIAXo-L8s6sthIdc4mVMhfGabUy9xMB0MAyTutR7FENVipyjHe5ZpgdBo8k-2PNEiKh1u2xXPnLhfMVyGnz3O9xl8Hh69mlgT6cNCD7dMOpKSyoH1K3iaDOMCoI81A_1qMMsdntxYUOa7JoDkzOIOO_DFnIZBvgwdbXiD08J2SqDR9YRe5gM_NTUHf371J65kx-OpUbLOGnr1e1IKQ3B15-OPeJUkvkiNuXc4mHXvXoybf8omkuGrIiL9swnIB-7bU2bi7dNEehxIOWSpm_nDHm89sCTaQP335hre2asUWpItjRpdIJAtBCWx9Eu53fyg7XoUPfELQcspSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
نقل‌وانتقالات بارسلونا در یک‌دقیقه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104015" target="_blank">📅 09:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104014">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1d68db4d.mp4?token=q7fiYjDJpgPYBTmwu02L2rG4dA4cMN6sU0nJyN4fuUGfIo9DjNfOdv2BaFyH132kq9Pj-SqROhbLJWBFIJDatAIy_sOb6xqhIphuFjWYhzaVicG7GlphJMeUl8c4rVRyRNWn3iJgSEVwZ7Oni6HLd4rLs-Q8KRp9NrdMaLDJY3hoAbVMQWKvJHmd_M0WDMNyZeQDgXFVp2V_69lGU_3ppnqPg7ODw4N_qaOEkGXh2QTzAaD8gYG9QDKDCZ-0RCvTc-THNH94CNGHd9K3u6JDvIpiU-YVk51BJZtIykWWYi6zOrhBuIqFOT5hB4p9ECFQk7xGrHIGSHuenvS2Tk61PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1d68db4d.mp4?token=q7fiYjDJpgPYBTmwu02L2rG4dA4cMN6sU0nJyN4fuUGfIo9DjNfOdv2BaFyH132kq9Pj-SqROhbLJWBFIJDatAIy_sOb6xqhIphuFjWYhzaVicG7GlphJMeUl8c4rVRyRNWn3iJgSEVwZ7Oni6HLd4rLs-Q8KRp9NrdMaLDJY3hoAbVMQWKvJHmd_M0WDMNyZeQDgXFVp2V_69lGU_3ppnqPg7ODw4N_qaOEkGXh2QTzAaD8gYG9QDKDCZ-0RCvTc-THNH94CNGHd9K3u6JDvIpiU-YVk51BJZtIykWWYi6zOrhBuIqFOT5hB4p9ECFQk7xGrHIGSHuenvS2Tk61PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ شوخی و خنده‌های بامزه مرحوم علی انصاریان وقتی استاد اسدی داشت خاطره میگفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104014" target="_blank">📅 09:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104013">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7d0d9c01.mp4?token=YzWkr20DStJJmN8Pjn1-bP-vR_yGJA_j5DlYtL8frOUKz2eiVD4kQaOB6Evgd3izItHyOw5pfKvw8ETuZvkODygNky1O8XdTkhPX0QXswrKCTMw0EXcAv3omFklkYdQPovmHoPrf4RIsY2QuAiVy_z1eDy3K5hyhZlpOMUrL8FIlhTNcDG5jf7zrJkk3OcmZzgLb7XF6nNZL4v5CvyppNCVXUcPaF1FgJdsFmI7XUJRLiSU2I9lSt75YzpGuHFYt0JboZjevBXGl67D39Ph5-jArL0eIqnqpg0gVQlV_mzk8qZt2Km67XsaoYnBOsT9jrojvFTyibr-zSUmwZ_iIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7d0d9c01.mp4?token=YzWkr20DStJJmN8Pjn1-bP-vR_yGJA_j5DlYtL8frOUKz2eiVD4kQaOB6Evgd3izItHyOw5pfKvw8ETuZvkODygNky1O8XdTkhPX0QXswrKCTMw0EXcAv3omFklkYdQPovmHoPrf4RIsY2QuAiVy_z1eDy3K5hyhZlpOMUrL8FIlhTNcDG5jf7zrJkk3OcmZzgLb7XF6nNZL4v5CvyppNCVXUcPaF1FgJdsFmI7XUJRLiSU2I9lSt75YzpGuHFYt0JboZjevBXGl67D39Ph5-jArL0eIqnqpg0gVQlV_mzk8qZt2Km67XsaoYnBOsT9jrojvFTyibr-zSUmwZ_iIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
افشاگری و ادعای جنجالی امیر حسین اصلانیان بازیکن سابق پرسپولیس
🎙
علی پروین سمت بازیکنان تیم پرسپولیس  پرستو می فرستاد تا از همه شون آتو داشته باشه  واسه روز مبادا
⁉️
مجری : از کیا آتو داشت ؟
➕
اصلانیان: از همه آتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104013" target="_blank">📅 09:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104012">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab9f085ab.mp4?token=CRYzBY_X_3n7-EKZp7YtUwRwta4L87FTsBCsIuZvVSgPCuf_-B7In8ksdez6qx_4jrPzTSuM53SDsVZlHDuBbTYCsIjSVQWEAMcbQTBPL8VDV4K0w3rZA3Pf_kGH0EoTdrv_iROzOppxybPxm1MbokXqYda14N0Qy4FXAJHhSQRZAnsoSh868Qju9xjnVKOQRfBBirfkCRb4_Ct_t1qfHa0GnH1LHZ6rjezJlX_GFkK8PZ0SsaMFtOmd9bL6xwImvOMYFVjt5hbeuoIbT9zbGF2MWKkZ8QPLdF4EsT_Fa5HgCi9eK4clvUbVB4NHFbyFO5KkJG05CdJR-TslJhXPNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab9f085ab.mp4?token=CRYzBY_X_3n7-EKZp7YtUwRwta4L87FTsBCsIuZvVSgPCuf_-B7In8ksdez6qx_4jrPzTSuM53SDsVZlHDuBbTYCsIjSVQWEAMcbQTBPL8VDV4K0w3rZA3Pf_kGH0EoTdrv_iROzOppxybPxm1MbokXqYda14N0Qy4FXAJHhSQRZAnsoSh868Qju9xjnVKOQRfBBirfkCRb4_Ct_t1qfHa0GnH1LHZ6rjezJlX_GFkK8PZ0SsaMFtOmd9bL6xwImvOMYFVjt5hbeuoIbT9zbGF2MWKkZ8QPLdF4EsT_Fa5HgCi9eK4clvUbVB4NHFbyFO5KkJG05CdJR-TslJhXPNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
میرشاد ماجدی رئیس هیات فوتبال استان تهران: این که استقلال به عنوان تیم اول اعلام شده و جام نگرفته است تناقض دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/104012" target="_blank">📅 07:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d4c307b5.mp4?token=pyxyl8eEiFoY29RzWTD1lT4gjD64kqbyOtsRBABYPKF4RMmqgMT5bYe6IHLBx0Q97Xm51dNSEA9MlnfTnPMKjvQxomVCBtohHCXYKpoWE7G_7YzcsWcnFM9mp-PxhBH3izhlE8Rz9dIWKc-35c81fJB1wpOJ74x4on5Q-LxkU6KbBeJOmBobWrS88rfqamFpfdT4ehvIXyX6SNta4KZutxJZOB0E1CZv2qTkjsyQkYpUQ5aI0BQjRuipJLv6fppBhs0j12fm-jzsK5Wznc4mdTHTO9YahDWSP3LUiCtlrH0OB5IrBIzfSgSgj7BgG3ZvzGrwho_vXpsi8hZpjadqHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d4c307b5.mp4?token=pyxyl8eEiFoY29RzWTD1lT4gjD64kqbyOtsRBABYPKF4RMmqgMT5bYe6IHLBx0Q97Xm51dNSEA9MlnfTnPMKjvQxomVCBtohHCXYKpoWE7G_7YzcsWcnFM9mp-PxhBH3izhlE8Rz9dIWKc-35c81fJB1wpOJ74x4on5Q-LxkU6KbBeJOmBobWrS88rfqamFpfdT4ehvIXyX6SNta4KZutxJZOB0E1CZv2qTkjsyQkYpUQ5aI0BQjRuipJLv6fppBhs0j12fm-jzsK5Wznc4mdTHTO9YahDWSP3LUiCtlrH0OB5IrBIzfSgSgj7BgG3ZvzGrwho_vXpsi8hZpjadqHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
🔥
انیمیشن جذاب و دیدنی حمید سحری از شرایط نقل‌وانتقالات این‌فصل بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104011" target="_blank">📅 02:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104010">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f966553cd6.mp4?token=nnhmSLn_6ZEx9Rqge-i25zbPFgaeYLCJk1HjXLBFfVSKyVIQ8pVGOPugqcua36dpUkeV1V3l3_caFT-5EJQt9J9PoUSK9A1rD7rd_qs1AZDB9lsuWHkNH-wYn8wLP0Vc_5mvGs8lC-lfOcUaZQSVZ_qG_UXuE0fVF_rUn3vvZNqRa4h16vZLeTdKcGNJkhPhiEvR9f-k3zn1lMvjzdtFR63tE-aEmu-nY9POEFdbaewWiaoLVb5tIWxCvQZSn2Y4CTSDTu0ov6TIHmYmVSvKPgwgXUoN8PkVNFC6b3p6cHRdYjEpHqhEv3ZFCPHEGjmXh5K79X5nKIqtSUQdOag1cHu3IACCsrs5UItW26Zhs5i1MGqK8oT_CtnV7HiRfjxsGrkxuo-keyhBZYSU1dPFvZ3NhLXcWF99liTEuLS_eyoG9cDOQggxqFdXkgA531TLofOzZURzi0OR0ok-Jed81NvqsxRvkEJW01AEolTS5Tf9vczPXqapUV3zgiJxRBg6aj-JuTpP9wDCHAArjrue35q9ZclBwuygXleEo1Xq8PAlNbRxnBpISYz5z4SAEtIPlVJXmDrHn8IOhxFWAHQBgBPWZjTo2ax0Z31ewznYBnXopgchMMhclqu8Yjf8GdReiq7g7x9lO1adTEQLmjNS_r_bhU2x84hEWNTmAhBlUHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f966553cd6.mp4?token=nnhmSLn_6ZEx9Rqge-i25zbPFgaeYLCJk1HjXLBFfVSKyVIQ8pVGOPugqcua36dpUkeV1V3l3_caFT-5EJQt9J9PoUSK9A1rD7rd_qs1AZDB9lsuWHkNH-wYn8wLP0Vc_5mvGs8lC-lfOcUaZQSVZ_qG_UXuE0fVF_rUn3vvZNqRa4h16vZLeTdKcGNJkhPhiEvR9f-k3zn1lMvjzdtFR63tE-aEmu-nY9POEFdbaewWiaoLVb5tIWxCvQZSn2Y4CTSDTu0ov6TIHmYmVSvKPgwgXUoN8PkVNFC6b3p6cHRdYjEpHqhEv3ZFCPHEGjmXh5K79X5nKIqtSUQdOag1cHu3IACCsrs5UItW26Zhs5i1MGqK8oT_CtnV7HiRfjxsGrkxuo-keyhBZYSU1dPFvZ3NhLXcWF99liTEuLS_eyoG9cDOQggxqFdXkgA531TLofOzZURzi0OR0ok-Jed81NvqsxRvkEJW01AEolTS5Tf9vczPXqapUV3zgiJxRBg6aj-JuTpP9wDCHAArjrue35q9ZclBwuygXleEo1Xq8PAlNbRxnBpISYz5z4SAEtIPlVJXmDrHn8IOhxFWAHQBgBPWZjTo2ax0Z31ewznYBnXopgchMMhclqu8Yjf8GdReiq7g7x9lO1adTEQLmjNS_r_bhU2x84hEWNTmAhBlUHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
🇫🇷
دینو تاپمولر سرمربی لانس بعد قهرمانی دیشب: لانس یعنی همین. ما از هیچکس نمیترسیم و اینجا میتونیم هر تیمی رو ببریم.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104010" target="_blank">📅 01:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vkzl6BptAmpfaBEym51x7yzW0W1zfCaiB1COMEids1BQ357qt7-bao5EeTxecQ0auQFzzv5LVkta5Zz-LnInT35fj8XnsLdUXs0ULIr4AfwtLUZ9hdsuNOCQTIDpi9ZQEwsIxlag7JZwqNZgGRTD0H2-IJNn7XHaNpPwsG-eGuIhJjvnrgjGCG12JHNEacy9dSqpPnRaRGD1guqW9GVdsbGh7WZs2vH3gMzDXox3anyXz4k09DugRaYAvmGDhLHT-z7OGUjUisjudWO_oQYqJ9MMzBfcirxgmM8ODDZIAhgh7PyLJ_AZMBBhNfsqfylsU8VH0zjIN3b5kcUz4yRjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD1mqxGWjrrVUiXEy55rnk_tmFTuAfFvoBJ4R4-L9a43yXOnBRO6tev1tvfcj4NLZDhdlR1lNvtvqFtSEd9VaJOlQsnROhxN-6vXgCvpNvthxkTlIn_cjhACxaIqG6_dPpLroyitKZKCpDbl6bx5Qq8IkFyAAbVzW0gsSwNyRbjdLhULgTGEw-cWhfn-sC7EUHpQgEB1r_ih56nkLCBcE_jM25wkbrR0BOJe7GgDR6VT9YnDtodyBcIiLU_HM5dXQsWbpoerZwH5blfQQPNZVDgIYVEkteAcCpjTZUuNwis-A7i8goj6aLT94jKBgkvh3OopQZaxWTtDCLcJoRgIZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤯
ساعت لاکچری رودری ، مدل
IWC Portugieser Perpetual Calendar
- بدنه از طلای ۱۸ عیار
- صفحه نقره‌ای
- بند چرمی تمساح قهوه‌ای تیره
- قطر ۴۴.۲ میلی‌متر
💵
قیمت:
۵۴٬۸۰۰
دلار ( ۱۰ میلیارد تومن )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104008" target="_blank">📅 01:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104007">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKNX7AU8OeUeJ9D7ihWBZe8hyS1ZxVDuiGuiWGr6niwD9u8ltJL34XXvxXIRBVPgu_ZFgXGz5Z9cpsaDQjnw7QB7XovUiTFk7HOm5wbNMEZjP6AAMMpwLtOyJuyZogqXzKRs4PNzsIHPLSKxAQEC430ofQy4QtZ3tmEdSJEOUwsgewmtgrHnCVzhVrJP5_XAwHXYbcft6bd5M9gEQnfzrN-yXKwycfn1mo-mjQvbcgjGtgLRr2W1-HFJ0rIPgZREGWxXpA28asO6lAG-vkjVU8le88kc5oQGC0u34n-HI0OZ_grWtTcHX9WQhiK_ou2ECYIs-IBDUMXK5ku1F_70aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
🇵🇹
پاولیدیس مهاجم وحشی بنفیکا امشب در برد هفت گله تیمش تونست طی ۷ دقیقه هتریک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104007" target="_blank">📅 01:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104006">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXKlBnVpddKrgGSXKGNPWBrLfe4UpSF3TFbo1Bp7PhjBaF8Jo2Pn_pQh4sfrYXzcngfCtEbRhYVB2XKqoMoiU4QNYooWoXxBeg9WVDRZmJ7yPVFyq-nJ818G-t0yDCY3rwArIr5FpLKsBO_I9wpcPeQbqyes5YnuwAd891F2ATD3Aq63oHtcJexWTUZxm_Cp3Lu65H1qc3gOSV8NEx-lA0gUxURG3YQDG3r-jmdYz4o2G7brqakBYDhQd_aFDA54idvTtt9BO3YzJLMj-QsfuY22hUWu0jfPGapEV3S6zkwNwvJMGUSrqvKkDpSIKZSCDvFn7DgiAJFgJFyJRBPryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
با حکم علیرضا دبیر حجت‌الاسلام والمسلمین عباس فقیه سرپرست هیات کشتی استان بوشهر شد. دبیر درباره این انتصاب گفته که ایشان سوابق درخشانی در روایت پهلوانی‌های اهل‌بیت در منبر های خودش داره و قطعا به کشتی پهلوانی کشور کمک میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/104006" target="_blank">📅 00:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🔵
خبر فوری روی آنتن زنده فوتبال برتر؛ AFC انتخاب استادیوم را از استقلال گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104005" target="_blank">📅 00:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104004">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a00c0468.mp4?token=ISkahdadVd-aHlohzJ5DtZoR7fwaJ_trKjsHYUrTPhtmFTAAFeIQky1iC8bo5ib7LJasQqk7_T-QsGPKIzKygj91HR57i-paA8GSMk_6JelnUHPtGF-uYKqFSNKSdYOa6IHiRG9AWSz1PwbQaCwd88sMazRVuWvz4vVAdzm1xDgG0oRksnlbZxHj8bZTmb0gc24MvvQeDG-iY0OT0PHN0fvGq1F9kJZInxDdGiEjbuNOqcWck-9-NYfc5Plfvs_4LK_sNsFRTPGaVaTnRB-x6tAYzXGsOwTHmR1rmDPyb2Tmo_qafyDM8ph0QLsxw-_r0luoCMnij0Kwh4dfE55msQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a00c0468.mp4?token=ISkahdadVd-aHlohzJ5DtZoR7fwaJ_trKjsHYUrTPhtmFTAAFeIQky1iC8bo5ib7LJasQqk7_T-QsGPKIzKygj91HR57i-paA8GSMk_6JelnUHPtGF-uYKqFSNKSdYOa6IHiRG9AWSz1PwbQaCwd88sMazRVuWvz4vVAdzm1xDgG0oRksnlbZxHj8bZTmb0gc24MvvQeDG-iY0OT0PHN0fvGq1F9kJZInxDdGiEjbuNOqcWck-9-NYfc5Plfvs_4LK_sNsFRTPGaVaTnRB-x6tAYzXGsOwTHmR1rmDPyb2Tmo_qafyDM8ph0QLsxw-_r0luoCMnij0Kwh4dfE55msQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😆
🇮🇷
ریدن رامین رضاییان به خودش از صدای انفجار ترقه هوادار فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104004" target="_blank">📅 00:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104003">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdaa9a811.mp4?token=qKafH60e504cKYjh8A9FD-5xZN-4_t7IHfybZA8j2CLEc2D2YwgM4u2S6MBful2j-Y7bG43N8iYqRGngflJlf1tuF9oiA8XwnWH0pe2vOQonqv7S0sigr3JC3JVWGj2Zwvdj6wrY_3GVGqdF0jkzY4mqfc6_p_5thYULuW_hi5B5K-GiCNk5wxg3-pe6WyJDpTLpcTjAtzv7oDNdzLI3aEDo6a3vW4DyPsIf4m9vIUwnQq1Kv-ZZ-1Vym5OItwFhyyerdQJZrsh2MRw9sbPB5qMv_G78NophJr9jU_hX7Bh2ydRBYx9p46Lx6mbsGKMUb98xcdBp1jXvdK6y6yQPuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdaa9a811.mp4?token=qKafH60e504cKYjh8A9FD-5xZN-4_t7IHfybZA8j2CLEc2D2YwgM4u2S6MBful2j-Y7bG43N8iYqRGngflJlf1tuF9oiA8XwnWH0pe2vOQonqv7S0sigr3JC3JVWGj2Zwvdj6wrY_3GVGqdF0jkzY4mqfc6_p_5thYULuW_hi5B5K-GiCNk5wxg3-pe6WyJDpTLpcTjAtzv7oDNdzLI3aEDo6a3vW4DyPsIf4m9vIUwnQq1Kv-ZZ-1Vym5OItwFhyyerdQJZrsh2MRw9sbPB5qMv_G78NophJr9jU_hX7Bh2ydRBYx9p46Lx6mbsGKMUb98xcdBp1jXvdK6y6yQPuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🔵
خبر فوری روی آنتن زنده فوتبال برتر؛
AFC انتخاب استادیوم را از استقلال گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104003" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104002">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104002" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104001">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TxDCLI9cJGS0JshsYe1Vej8pfLtR0Wnc9bPkEKQMTQlYj2YhRi-LbiGp7iKnEXZl1i04rmxA0qCEw5xXQggQsZyr2Okx8XyfxKXFY9L8Eve6_Pk8DlN3jFXkqF1Pc_sGx1ZTjXg12mxja_hWedWHDYG3YyYQ0F86XJ8p_5InTWsxhLE_p5dl05IhN_gMjbXA-3SQdv6d8o9TTdbNxlNHl_pXzuj0nvW4oFyX4BTpAqIwtDEtZhYj0ChkH4I9AB7xsQVPv3P1uvGZmA4pDr-1jrO678b6Rd4rqntzLKtW6A7tOKxuy6rEE8pyl_uHFg18OPV3dPFXJ4_zwqk8rgqq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=TxDCLI9cJGS0JshsYe1Vej8pfLtR0Wnc9bPkEKQMTQlYj2YhRi-LbiGp7iKnEXZl1i04rmxA0qCEw5xXQggQsZyr2Okx8XyfxKXFY9L8Eve6_Pk8DlN3jFXkqF1Pc_sGx1ZTjXg12mxja_hWedWHDYG3YyYQ0F86XJ8p_5InTWsxhLE_p5dl05IhN_gMjbXA-3SQdv6d8o9TTdbNxlNHl_pXzuj0nvW4oFyX4BTpAqIwtDEtZhYj0ChkH4I9AB7xsQVPv3P1uvGZmA4pDr-1jrO678b6Rd4rqntzLKtW6A7tOKxuy6rEE8pyl_uHFg18OPV3dPFXJ4_zwqk8rgqq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a26
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104001" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b070f200.mp4?token=BOhuAGiolE3vbP9gtzqgRUkg4jZ2Fa6lQoP6Gu9YkjMSZxUWHKyIUI3G0kTxfTjmGQ8oV5dICtLlsKKwQbJGcwC5qreGEnWOWTmC1ithUanzqk-S9hBxTtOgE99WMzz2upJqSmq328cUEIjlJctxIPtdEPL8XVZ9oDU7kvZUlRnO0TnAz-dJ4xZruPXViWqhTwwzfytWeLSoMBEGdXMcfyKWLVO5ZXbY4AEDm4sKw50B0yAMDf_N6RXMQmk_b9dnrdGWfQSUBy1KWdY_FvYGh1tI188LD-gWEkxHzg8G4yPds0M3qHkVubNEZ00ynDRBltOE2G67_CqkguzjAPO1nhR3fbt7MKNyeK5p8-GGK-eM72nRBfrcl3549DjxX_3GRD_k7iz1W-njhTwvpDQiDD5BK2u1RX2mkMsj125naj8kx8SqOmqf7nvN-qx4SdpVHaFc-trnmYIJL3aiuWDAT7PSJ-dSQbSFQc2r6KLOiE6OWdFcutRP4K3sV5TT3_loTkyVYO9YrmYh-sbnhRj-lec7p3JRuXyMjy34_iX71am5u8VTLMGlJarAlguCnHw5CeWsmRSNLo8zOmqF48JDR8v7R3YQhN4nXQy-_jgLhieMrw4vaOzl2kTZbBhv07YHwO80xjjzt7KYOhCo3W5-xJkapJkDSYB9iBs1IGABLIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b070f200.mp4?token=BOhuAGiolE3vbP9gtzqgRUkg4jZ2Fa6lQoP6Gu9YkjMSZxUWHKyIUI3G0kTxfTjmGQ8oV5dICtLlsKKwQbJGcwC5qreGEnWOWTmC1ithUanzqk-S9hBxTtOgE99WMzz2upJqSmq328cUEIjlJctxIPtdEPL8XVZ9oDU7kvZUlRnO0TnAz-dJ4xZruPXViWqhTwwzfytWeLSoMBEGdXMcfyKWLVO5ZXbY4AEDm4sKw50B0yAMDf_N6RXMQmk_b9dnrdGWfQSUBy1KWdY_FvYGh1tI188LD-gWEkxHzg8G4yPds0M3qHkVubNEZ00ynDRBltOE2G67_CqkguzjAPO1nhR3fbt7MKNyeK5p8-GGK-eM72nRBfrcl3549DjxX_3GRD_k7iz1W-njhTwvpDQiDD5BK2u1RX2mkMsj125naj8kx8SqOmqf7nvN-qx4SdpVHaFc-trnmYIJL3aiuWDAT7PSJ-dSQbSFQc2r6KLOiE6OWdFcutRP4K3sV5TT3_loTkyVYO9YrmYh-sbnhRj-lec7p3JRuXyMjy34_iX71am5u8VTLMGlJarAlguCnHw5CeWsmRSNLo8zOmqF48JDR8v7R3YQhN4nXQy-_jgLhieMrw4vaOzl2kTZbBhv07YHwO80xjjzt7KYOhCo3W5-xJkapJkDSYB9iBs1IGABLIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
محمد محبی با انتشار پستی در صفحه شخصی خود از جدایی‌اش از روستوف خبر داد
. مقصد بعدی محبی احتمالا تیمی از کرواسی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/104000" target="_blank">📅 23:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d25894916.mp4?token=XxcmZa4DyshpA9ttVFDht_vCspvWv42egeN7L8iNXajChlFLH4DgL7t1PbgTY4Lv1sjS_QUZ_5yR5H2iz3JZxJtwgWaG65d4LaqU6v6nwornvFJqfD_rW7r1Fj8zp0ApQ4ieoQfTQbp6vRF41W9epkJNDJBgwwLuCOwh4eJLu5tG3Abn82adlMu8Iz4JaZqlej1_E7gcQmGZzwIL0cbIAhU6X6TpnP3V_UOM_6j7mOiu5bFUbw-H5-2fdJNqdyEWB9mwDFQq6hNv_4s0oDrHrQtsxIrjSUVLbHoRP5zciXwsxX-SNWxYq5AdTVGaqdb_UAubZu8XQ6esmRtyUXoWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d25894916.mp4?token=XxcmZa4DyshpA9ttVFDht_vCspvWv42egeN7L8iNXajChlFLH4DgL7t1PbgTY4Lv1sjS_QUZ_5yR5H2iz3JZxJtwgWaG65d4LaqU6v6nwornvFJqfD_rW7r1Fj8zp0ApQ4ieoQfTQbp6vRF41W9epkJNDJBgwwLuCOwh4eJLu5tG3Abn82adlMu8Iz4JaZqlej1_E7gcQmGZzwIL0cbIAhU6X6TpnP3V_UOM_6j7mOiu5bFUbw-H5-2fdJNqdyEWB9mwDFQq6hNv_4s0oDrHrQtsxIrjSUVLbHoRP5zciXwsxX-SNWxYq5AdTVGaqdb_UAubZu8XQ6esmRtyUXoWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
میثاقی: افتضاحی که در تورنمنت 3جانبه به بار آمده تا الان ماست‌مالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103999" target="_blank">📅 23:07 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
