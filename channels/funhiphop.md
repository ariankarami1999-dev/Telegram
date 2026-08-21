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
<img src="https://cdn4.telesco.pe/file/Z0uyRja8Y0VZw1dAYblx0eEt852SvxB4-QfmrTLQ-fmRbeWjUmJHRmLR7GvyjLGVAaQjG5VUBiaHjcdO2dducPD10gmcZ24GbYytcUqdDcrHwKmXL6uGROALhc48Kgevlm_keNvbeAvG_KsSsPUBI5zy_FvwyeMlg9eteRsZj-qPc4wmCOW-ch5CotQcWR1TzC6D1oIY1Qkk9LK51wtl39xu7yqSEpodHkT8qa4J9uSkpwxrRkOOLBwj2nX2vVKrNB8SS_0scbHRX_TO2wnk8jtbDzaWlZx_6Uhrr8GmMmiJMEbNFKL7Qo_gta7yfrNoZyKBdpIr7iwEIUP7QnJvzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 15:19:28</div>
<hr>

<div class="tg-post" id="msg-82424">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پزشکیان : جنگ باید در یه زمانی بلاخره به پایان برسه، بهتره امروز که در قدرت و عزت هستیم و تمام دنیا باور دارن که ما توی این جنگ پیروز شدیم و آمریکا در دنیا منفوره، به جنگ پایان بدیم
پ.ن:
😭
😭
😭
😭
😭
😭
😭
😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/funhiphop/82424" target="_blank">📅 15:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82423">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCKl8TbtNZOgu3EeUkKnEbovSsHnGatC9n3GhaGBnK4_FbdRvd4SYZ1laxhefG0FwIdZ_2G_Yq91iIzEMKn6bEeruKmAQH7n38LVyHA5B9uXwvR1EPqWfTRyjuOLFXLeNgnL1fe5THlAOITV2CKg9jrSej73FIVgQ0Wug_9Tsyd1e6lMj84ewMax2BeDaztpzHCEOKvm9gihEeUlSmSMjjByUgnDa7UtKh7to6RX5U40apu8JbUIvQwM3LqGYeKMs2fLrQiPmZh1RXIm5kXD_DaIpYR94Jq3D93oLhNlfJr_fh4h3pGfaf5YlGZVHTmYb1BW4wo2aRhcNUHolC4XOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/funhiphop/82423" target="_blank">📅 14:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82422">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کنکورو چطور دادید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/82422" target="_blank">📅 14:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82421">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyIfVmU1Up84LmAJLlXeSzxYt-3zBNGEc54NiwPhG9fgCEgY7l21t7BHqfzxwWtBIIan2YNfZjXYsequRgTJ7nww7XcYMwt2iqTd6Wk9ZDFNq5iDifED024CiF9Fcpofvj5tsKgw9AGe6bBYf3ZzPmEYP18mpydWaQIbM_tsKp_VQ4SjOt3oNdU3TJpLuOpSP9u_9c-peiHu7WEyUspIZIFzhirM4MAMubI8VoNzY-9Auw1O5hzTc1Sk3nWzvE3NH-iTqLKvR28_6Hy5xEsWOqCiE0k6nHdhR3nRe3L1f2wxzEFr3w6fCXT8rYxCDQA6btxeyCxLWXPoXBr4685foA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیشرو و سارن به نام Mirrors منتشر شد(لیک)
Download
(حمایت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/82421" target="_blank">📅 13:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82420">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwyxlPPAPNERuBeD_KIbnV2LyO-u_9QLSnBPpRi7w-ONq7cXuSY_ELV0beN01AHzYWvyMEkCH7GKDU_ZkxDzAg2ihDVH5rYhAK0zDZWwjJcthEQ2kyoM7dnI4mal1_4whGNXT7S0N069PcsE9dUTVh3MeWZ8K56EqMX_rVTc1zrvEKtcORhZPQJ76gYc5H3PpN6-bNV71hHzUfRiKMg0c8bcM64CYFnczYbuUtHkM567HjJ7ZVqlip-NFd-t5acH2z_MQC5y1zWCRcC5fnHkvLVWBLw5s1pfjzeRJtlfS9HtUC1lPRFl0ba2FhexlklV8Nrr39XczBokNdOPzfYmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تست کردم مثل یویو کش اومد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/82420" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82419">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا تسنیم اومده نوشته اقدام ضد انسانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/82419" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82418">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=LFD7NUwMjuzuPPY2NU5auaOHIqkLLISn9TUy173XVaY5kr0M95NaT_Ly0O83k-SZ6TNarst3r2TBshfEuxo7sHrL8h4kU-7zMPDMIJj94OC5l1I7un_53xwvyS5kCGpElxiMByOcVbN87ePq72MlIyL_G6Wh1LobyBIaHGZKsqN_3d2tFUzwnezzCOy8ufuX4Ydf8DivBAznUPmijxB-czQigQZCrBsWSiMgK8MRigAjgb9HQoAGg2So7cMavUaQmaUpzqyCX7uShI1HB0NDdGM28M2Xc8FAL-7CoksuDSmjo163kKtrPD7NtOcDcLMPwaxyhfoDO8BXyH3KDHX4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=LFD7NUwMjuzuPPY2NU5auaOHIqkLLISn9TUy173XVaY5kr0M95NaT_Ly0O83k-SZ6TNarst3r2TBshfEuxo7sHrL8h4kU-7zMPDMIJj94OC5l1I7un_53xwvyS5kCGpElxiMByOcVbN87ePq72MlIyL_G6Wh1LobyBIaHGZKsqN_3d2tFUzwnezzCOy8ufuX4Ydf8DivBAznUPmijxB-czQigQZCrBsWSiMgK8MRigAjgb9HQoAGg2So7cMavUaQmaUpzqyCX7uShI1HB0NDdGM28M2Xc8FAL-7CoksuDSmjo163kKtrPD7NtOcDcLMPwaxyhfoDO8BXyH3KDHX4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره با دوست دخترش قهر کرده، دوست دخترش هم برای اینکه از دلش در بیاره براش بنز خریده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/82418" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فنای پیشرو جان جدتون دست از سر این سامان ویلسون بردارید، از وقتی یادم میاد هی داره تو چنلش میگه فنای پیشرو بیکارن علافن بدبختن هی به من زنگ میزنن مزاحم میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/82417" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=jxEOmg6-q0REadiE29oL-NpZEZbYen5EdsC_fMlEBJ_gCAk8ZZyOGVCIT6QG3JueTXNTLQduiwIXWGYSdgoe2-dDJMSL5IAv6o8SscUzemD5LMQgxs5a8RhuVX4DKozfwFQ18K_4JkqZXaVCtmkakz0RCHxYaXgstBclOs1iJG49ypRdX63L58azxHdKhj-UvVLWowVN_pc8wznWX8s7y9WwFkVFn8a_TAvWtIn4DFPa7URm5YQv1Wsw_z0e2i2LmnxwYWSx8rR_fMy8c1zBoT1ejTdwzShHLJAWkjMsZbeFCMpb5CCo0BldzDy_opB0WI6veYI0lZuDqKRQLymPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=jxEOmg6-q0REadiE29oL-NpZEZbYen5EdsC_fMlEBJ_gCAk8ZZyOGVCIT6QG3JueTXNTLQduiwIXWGYSdgoe2-dDJMSL5IAv6o8SscUzemD5LMQgxs5a8RhuVX4DKozfwFQ18K_4JkqZXaVCtmkakz0RCHxYaXgstBclOs1iJG49ypRdX63L58azxHdKhj-UvVLWowVN_pc8wznWX8s7y9WwFkVFn8a_TAvWtIn4DFPa7URm5YQv1Wsw_z0e2i2LmnxwYWSx8rR_fMy8c1zBoT1ejTdwzShHLJAWkjMsZbeFCMpb5CCo0BldzDy_opB0WI6veYI0lZuDqKRQLymPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخت و پز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/82416" target="_blank">📅 10:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfHRjkN-aK5_YrmAazEhBmMoFe6otsh5T_PdZ6cbCaXutrgeqTP3fFlaV0kNI-yW9EE8XHtE-QFr1ozjjnuQQwDQi0kYbrYrIc2FtBZNQlxJWISSBmt35KWXHvO3WnDzzkydxZCPKRN1zbNlpCAy7Nhs72XGvZynFq__IfH3mVz42uMMHBgnthrL3q9xwHOAdEvgj6uTsY7k4JjbSSC6-4iEz_CwreHADdgWs3EU20iF5Ya97Z3BPHsMLkjTtfKb6FfuKiLUPK6Lb5VfUYl3HgeQ1-yTR1yzyHu19VUGe2qkdRdlL-LvvBHOeW8GCIaZcPGXszJcOGvKaZwEXjEpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید آرتا و سمی لو به نام Azizam منتشر شد
🟢
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/82415" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBveRT_9zEO9YMXe3aZNhYsGExqyXBMhtLTJcXA4x_F-g13vX6kQ0Kx7yXmkXORMRSnWtLZUI462EBcsnX3c0rLwY8sD__OnqGACTZlZILgNFNtyFUVV3IKtSWXjK_69ttqFmuohhMNseFZ6JmgwtoSiMPc_-PS1Yib-toGNAUIBh2FrU277QHaTYireFyrjdqQH827OESmjmPMNjskQezMKyKHiZFgTZIJeXUFMDefp0yNAF9djrbXILJIEFzawa4D3HL-loeo5JegqtmY38v9W2D0M7wLNWJ14fi8bw1RvTND8jTBKD8bDQpyo1A9hRctPsF0PI89SNiTDu7IA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لیگ برتر انگلیس
💯
⚽️
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r30
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/82414" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=McSRIdgsTodJYrZpfnxq0zwb_lVx-q8IH3JerA_-nqmdSOCsRg1CO2hzWscYTdBJ-36OhTJ-wwfncyBMEMPNj98Jlq6zi5cew_be1FsuX7wP2WPoV_UjlzSfDiA1nfRC2ZZdfoHi4jGfzfRPRfzI4Yj9VDL32UVhOr6YoUUkfQltYUQSyjcpKNRyjYoctY551yyJdnpPps173uH5EzQND_oih6XWh-s4tonbH-0RH_Of34O_Mg3cOSUXbcYSjwocMX0MvfR_1RR6G8F7wDIhCFqfSHXaHep735QRSoIEXmOEZr0D3-lQcXGfzHFVLBROJCo2M9s4MFLHkOGY5HdUnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=McSRIdgsTodJYrZpfnxq0zwb_lVx-q8IH3JerA_-nqmdSOCsRg1CO2hzWscYTdBJ-36OhTJ-wwfncyBMEMPNj98Jlq6zi5cew_be1FsuX7wP2WPoV_UjlzSfDiA1nfRC2ZZdfoHi4jGfzfRPRfzI4Yj9VDL32UVhOr6YoUUkfQltYUQSyjcpKNRyjYoctY551yyJdnpPps173uH5EzQND_oih6XWh-s4tonbH-0RH_Of34O_Mg3cOSUXbcYSjwocMX0MvfR_1RR6G8F7wDIhCFqfSHXaHep735QRSoIEXmOEZr0D3-lQcXGfzHFVLBROJCo2M9s4MFLHkOGY5HdUnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این لحظه به بعد کیرم تو استقلال، ملوان عشق.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/82413" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB7fjGW-I9jf2kljBOjxhc2mb8Yziw3-tIhExHwAbyBAUcymiZ5is5lEsG82c1Kue5xOBsrFSH29Jm04KBEs-Sc_Bo4XsP_acKib6tw_K56QGYxaSM7wCZv4epT6Tbn8SR0FNpUozyhRKlJ3MW9SkpEPYXYHb9RmoaNoQi8Tykzk-gq1k9v4EkLj7cutYBWtPT4OsEjACUNZ0mwC0WYpLD60GdxtLbIWbM2IONwuqYaoX-muxWfnWTG2iBds48-bqABtQmv1Z2v8YItxO5snuZE88TeBSYm2O8rL5CWsH_xW51lSra5IIdj0396ThbjvBSz_0oAljl4uKD85D7vCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارسا یکم بی ادب بود ولی بیس حرفش درست بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/82412" target="_blank">📅 09:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl0JhkFrmXlb0zrf2KUd-V7vSlxN9jrcoVVvI26tcQuuN5XQLwxU1LazoU5-UII698o5nHaT342O5_uJxroPeNopq_P_C0KXt3Hb5-ZPIlFq8QHjes4IS0UorLguKsp-cHQpoqMFrfffgknQac10iEEvP-kHbrEmrTfnt0Qvk8mlH21lsT425qzghpnuwHZhw15gZCWsqqtr5R3_dkVoNzGKRXIKV1PVp6BqFype4nkzPFxou2BJOp-2XxaL2B0kTWMQe9CB4gYXtiAbRpXkA9xgvhreHiDY0ZXUDUys77K6fEvma_TERmVatFEZGBHz82j-vf4pUtFYL_l9siAEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
💙
با این وضعیت تورم و گرونی دیگه سخت میشه کیت استقلال خرید
ولی این ربات هر هفته کلی کیت استقلال هدیه میده
👇
☑️
@F00TiBot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82411" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6u7T75853prfXIYtO6B-YoVc8mqxnbS7lecZNgZcOr7wdHP_zSOEAwO0bYsU5XeT0X0OBwFg2ew_OveyFAJaUvZeLqK5S4axtzBilLz287XM8BmGyX980Vt2pwqp7VG1oOUx4eHnBdQcRdbz6KtM6w6X18taZTSYmkFhJaXYgpdBBCYWW7dz3A2IUIe89AYeh5DuylERk3VZWtwPgo5p3XgmT7vj_3IBs-09JTw0jFo73u-kdE-NeFwJdVWLg-TB27eVvT3pJXBB6hJWZ4_D6fbd6N05fBC1QYpbG74vwuHjN6wWSsb9_itpjOhib8hHM_IJ7jaCr7oq5hgo7W2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82410" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=WJnhhdmDhCYaf8SlD9EYd015PR0XZbRC1MepCyB6zRnV-C5fUu1PJ8tXsscHha8Sqh-snylPnBdfigo1ZuorxBIkpZzZpUw-5UwE1-auV5iPqFsEFukK4wODmQuA-dnDqLIKQxUZjix63D3u0KS15foR-gEwfo4KdiNDfanv5td-ilcR5-IdRpt9_IkmY5IeuCYNfNPkSPtF7xjqyt6KBjvq8bsiUmHaZnCGCPrVrVGWH6O81_c6YoO2yJJngm8Mt1FlFrmZ65MF9plp-8sTNoQ-l_vEHfAbeVrQBAMhRwiRAL2kvq9S9vhTUwzjaoCa578Ywzm_je7zGBPXpYjn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=WJnhhdmDhCYaf8SlD9EYd015PR0XZbRC1MepCyB6zRnV-C5fUu1PJ8tXsscHha8Sqh-snylPnBdfigo1ZuorxBIkpZzZpUw-5UwE1-auV5iPqFsEFukK4wODmQuA-dnDqLIKQxUZjix63D3u0KS15foR-gEwfo4KdiNDfanv5td-ilcR5-IdRpt9_IkmY5IeuCYNfNPkSPtF7xjqyt6KBjvq8bsiUmHaZnCGCPrVrVGWH6O81_c6YoO2yJJngm8Mt1FlFrmZ65MF9plp-8sTNoQ-l_vEHfAbeVrQBAMhRwiRAL2kvq9S9vhTUwzjaoCa578Ywzm_je7zGBPXpYjn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینو میخواستی بشنوی کصکش؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82409" target="_blank">📅 23:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpBWhMzvCvlY4ncK_wg64DH504qmR789-PCjcN-9er3dffZLC4UZhhbrrDNviR4MqG3Eb40nHktsl_VzFzyUmwuZdkhKjQxa_MbYUMLQt41eKKNWX_X1H0tFY_a2a4z8TRLtiMx7gKGBn69kV6Sx-YfeMdAlzDyHTlNkJVhdbfVamYHNSAd8T85fDCDuFCKx8RKpAwIdfjrxSAO63wFXAE_1bzbVUeOF6vOuwGMy0nSXEf3P722xC5qDFvyh-s0LS6GNBpQRGGNyI7nStKrVHvy2HeS1mBLGLmj7Hy9kl8k_A9qe5YVmxNxWBw24oTMUahO_3Wg8VobxJRiAdYmTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا برای عبدالله دعا کنید  @FuunHipHop | TemSah</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82408" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پسر ایران فوق العادس
غریب آبادی، معاون وزیرخارجه:
آمریکا اسم شکست بعدیش رو «جنگ اقتصادی» گذاشته‌
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82407" target="_blank">📅 22:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=FkNUtCyZ-BHPTcWvKWfWCX-swO2ODiUOPh_4quzEsoYrFauc8TgTxs0-bhl9ylTzFkNufQzvEoMqGGQHrj2h4zzMtPB9bWPNePF0zdTr5Vd1FdwXr9qn4VUK0jniROVV0F2B8SLMAQvZKh_2IHNwlmmUzKUZpZCRRzHZ91sAXDhkhoeXvXArFtVBoWj4JKsGmQUNh-rmgqcKdCXMtXXRsGL_Bns3TsJ-9anIVIf7KCgDPseWfJNgMGIowalYCsnEOvEyaJgLXAc3bUapvOwhGXB8JKXv3-z956D6SBKaiLUAsZQhDZqvRS6maQjhP9MyqRFHEH0mMW_-EDWEOEJY7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=FkNUtCyZ-BHPTcWvKWfWCX-swO2ODiUOPh_4quzEsoYrFauc8TgTxs0-bhl9ylTzFkNufQzvEoMqGGQHrj2h4zzMtPB9bWPNePF0zdTr5Vd1FdwXr9qn4VUK0jniROVV0F2B8SLMAQvZKh_2IHNwlmmUzKUZpZCRRzHZ91sAXDhkhoeXvXArFtVBoWj4JKsGmQUNh-rmgqcKdCXMtXXRsGL_Bns3TsJ-9anIVIf7KCgDPseWfJNgMGIowalYCsnEOvEyaJgLXAc3bUapvOwhGXB8JKXv3-z956D6SBKaiLUAsZQhDZqvRS6maQjhP9MyqRFHEH0mMW_-EDWEOEJY7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید با خودتون بگید این کسشر چیه ولی این اثر هنری با ۲۰۰ دلار بودجه ساخته شده و تو بازار چین ۴ میلیون دلار فروخته
پ.ن: ممبرا نجاتمون دادن محتوا فرستادن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82406" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محتوا با تایتل "عاقبت اعتباد" میخواید برید اجرای جدید علی گرامیو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82405" target="_blank">📅 21:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82404" target="_blank">📅 20:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82403" target="_blank">📅 20:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtCR4bYUGcW4XJTWWWl9-QRAzWotrljse_Ac-84M9jz83SRuwCKMGXpUTlIgx2wsy3sWQk_QNP6eVvvD0iirAQlz6kcc9r8p3Ga4gQYbLaJ_ZvjQ3VaTlP_Z2KXGcSGfCcvld7HVYNEjdoV0HRkw54J1Pyq7cRRsHmt8hMch5QlmZTpH7Xh_FV4bG_2jTF3XLlEbUTHdtVIjEkNYMXJBy9uJxOj_wmlrMH-mjAPVDEGQ1Noe3QRl8veIViUjkrogAOcdBNwCFKk4glxAwWZmdldyHHKu-deSzTJSfXFcUycPh_oKgHAQpassA40kfFtndvIOw22hoO8pOxebXsfyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود ببخشید یادم رفت وجود داری
موزیک جدید ویناک به نام باور کن منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82402" target="_blank">📅 20:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بسنت، وزیر خزانه داری آمریکا:
ما قرار است سخت‌ترین تحریم‌ها را در تاریخ اعمال کنیم، و من به شما می‌گویم، این کارساز خواهد بود.
این روش قبلاً در ونزوئلا زمانی که ما محاصره اقتصادی را اعمال کردیم، موثر بود. در حال حاضر در کوبا نیز در حال کار است، و در ایران نیز موثر خواهد بود، و ما این رژیم را سرنگون خواهیم کرد.
وزارت خارجه ایران:
اعلام تحریم‌های جدید علیه ایران از سوی آمریکا، اقدامی پیشاپیش شکست خورده است که نتیجه‌ای جز تکرار ناکامی‌های گذشته نخواهد داشت.
با در نظر داشتن تجارب ۷ دهه مقاومت همه جانبه، از همه ظرفیت‌ها برای دفع شرارت دشمن بهره می‌گیریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82401" target="_blank">📅 20:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زندگی پر از آزمونای بزرگ تر و مهم تر از کنکوره، فداسرتون که خراب کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82400" target="_blank">📅 18:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYpuBAXh0FL0cwLbLjWNQPIi1rd75nD6KsoNFY2FjsDdUgnx9WRnUy-tKK5-GbwM6JadXVyogtXf8doPPyvlzVUM2jyy2TXsU9mFyyzU-HfWKuk-O81vKUh0-mCRhlqsGx84ZqrWynpEhpon9omyM3lx4OBEXCGUnYgiHMnGaVPOpyEJoZcuNwX8_542SGqPdh4oMJstaqYEe4fAoIgePmLusn7pDBMbv9QUmNLVe3gZzTJm_upzfL-zIL1R69xwcz5Y3IozXOPB-MzwE4kcgAewmpDSiVtBVZiJ_a-jmbH9mVsytr0zUCLfPaOH6zhm7N8zkYRQP6eqn_t0_R35AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابامیخواستیم اقامت و حقوق پایه چند هزار دلاری رو ول کنیم بیایم واس ماهی ۲۰ تومن کار کنیما
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82399" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe9whJnVJBfxkZfZw-5CRhVgjYatSYHIZbiIY8l08Vi5S_nRKEYsmtpZWKGs2JWAz3fF9B0q7Nb6-YNf51ZcjknDMhg47XjTJiSuPbTf8G-_Jc43pD6TrsegWioGu7yrF-FjYLv0lAdtTaBGb3LKwM8-OdOwStUD5ykLfb8On36OeB1mX_H7lslwgB6NDn5avxudOLg-SAvqBTDjSmFGLONUOeVpxvbUkWStPstl3BK1TkKkp9PXvCXReBUqMf4kiopPbXN2k8MHtWhfi8JKXivGUK_4okQsK1I0lW0FGPl8LLBaS-qYK6bMD3W6Ru5drlGdU14e8gNK8vxnJeCu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا شما راحت باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82398" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویلسون چرا مست میکنه فاز رگنار میگیره
😂
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82397" target="_blank">📅 17:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=B7kWNrz8i5xtJiXFrxBZGRGnLhbB1BU9-e8hyVnbZvURICNY5ZxjcqEQksFe8unV6xxKe9UhduXipmLW2ju-iY8nx9zIwier9Gdojys-HN6rjidawcieR1aYD-UOlc3c4ZDy0qKUdY-ep-5pit5KyxZcyqeMlLI3ObwDlwt_qO2l8LRsgXvBZNayItkgsmUyIJtDbMWVzwoK2aC53mKjfju-Lvsg7UjuTVzu_y4R8vtCKPpuZlLppMhnC0eMgocIdfdP6CXbofENxaSA4YE-oocSVDfVzOKp29gO_7IzgGCE53Ics_gY3aaURFRBUV8dQVO7aBXCVc86dHOi-_5d8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=B7kWNrz8i5xtJiXFrxBZGRGnLhbB1BU9-e8hyVnbZvURICNY5ZxjcqEQksFe8unV6xxKe9UhduXipmLW2ju-iY8nx9zIwier9Gdojys-HN6rjidawcieR1aYD-UOlc3c4ZDy0qKUdY-ep-5pit5KyxZcyqeMlLI3ObwDlwt_qO2l8LRsgXvBZNayItkgsmUyIJtDbMWVzwoK2aC53mKjfju-Lvsg7UjuTVzu_y4R8vtCKPpuZlLppMhnC0eMgocIdfdP6CXbofENxaSA4YE-oocSVDfVzOKp29gO_7IzgGCE53Ics_gY3aaURFRBUV8dQVO7aBXCVc86dHOi-_5d8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82395" target="_blank">📅 16:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82394">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7ifMrlBSdkMkEXSpqfGggvOYCLevBxXc77vyoRU2mq__6FKM4gCbLLjD5XWh1YItObJRkQL4oFtp0-hctn2wcXU7BKwdRDXUmMEtqMu3LgxSpVPf3yPmgksT487Hoptu3hKTMCHPt4nl7LObNMD0LlBAyEkGIegMddOwg0gr5AHmXhwg2CSMhuFNCiRn7hDyRcfN2L-997QkoJDKhctXZsyXwuOUQ8um6-4ZN833b83lNOllAQVL6sZ82U9EV2I8IyyHKeZ6un9BxUW31Y6shhezxhN3qgkxeaRSojcKuR_0gRgrfWTzdv5d9YoSw2cAX6z5jxP3V3hE2czhK-iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس پنج + یک بت‌فوروارد
🔥
⏩
از روز دوشنبه تا یکشنبه در طول هفته، رقابت‌های ورزشی مورد علاقه خود را در بت‌فوروارد پیش‌بینی کنید و به ازای هر پنج پیش‌بینی ورزشی حداقل ۳ میلیون ریالی خود، در هر هفته یک اعتبار پیش‌بینی رایگان ۳ میلیون ریالی هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
btwd.link/51
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82394" target="_blank">📅 16:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82393">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دلو دیگه نخون لطفا، برگرد همون دوتا۲ ات رو بازی کن(
منم دارم میرم مچ بعدیو فایند کنم
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82393" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5JZCUgWDOfWaQYFkomE1gJrvdWcQqe-fCRksBJ1sLveUctr6rswGxCzEYszHpIH4JOlnH3_I_hxRlh3bhlGwZYDjm8JpVwOyoB74rp3mIpUCqn1uD5XjlZLDD8R9auqJqTKA_8C46Y-HcyA3IJwIwqKA0A3paUvQvIUMwJOzNxmbPGCDp5IasIMG2RiJqLMMGW_wK8G4OakOf4we-vYicUIbaBu86E6YjI3up5NU9Tf_9Avesz8hi_MWV43cL3xam8BKrqZ5vmADr5Zuk2qn3CAXSWpRf7eLBWowr-Y1lXFh93eUqJuWN2Pace-1RRG3yCYUHS_qLml8a_keksR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دونالد، ترکوندی دونالد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82392" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82391">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82391" target="_blank">📅 15:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر خارجه مصر تاکید کرد که به هیچ کشوری، فارغ از اینکه کدام کشور باشد نمی‌توان اجازه داد مانع دریانوری شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82390" target="_blank">📅 15:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بچه های کنکوری بیاید بگید ببینم تو کدوم پادگان قبول میشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82389" target="_blank">📅 14:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKzVql8MgEL2w8Av_v_Zpu-fADEXrY0Lqwkgnm8wVGGzJF7Pb_YG0kc86t3Ukcc8EmnktvqMJvPGLoeqZhdz5-_gdH_u4mkhl2-wupN8vOE30WgpvYYaHfJJ7oU770jPBgI91ff6vV7CLOAjqZu-YpP6KK7L6MnBXs3lJm0rorMepM_jW2ztALqiHmSbp3YcKLvjv9Kl8Kjt7k0VdTlvuCSBDlg7Znntqwge9yn8959GipYbynXxF4HkYSU7JNBY1YQeTrZx7G_y7IkS9kbEd6GV9VqN-fpEntTf9CFNQNmHggLX_p2PqK4mIb3rQHsYpQgb50g2vQzXBRGtZB1qSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رو به جلو اگه جواب میداد دیگه کسی قد کاگانو مسخره نمیکرد اردلان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82388" target="_blank">📅 14:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=evA3ONY1mO0LgX4-tve6hkUsfJ5BySP6sL2qqNskhrZ3GTT904OpIVBL1fPAC6GyLldqsN4wSaM40MJgZmPj6hDzwt9RkSXMUxZBg5YfimWO_JSGNyusLI3tgvLhpgtGFzI3OqHXEgCXK0ejK1rUebKgBjAoNWqgwWxGY9_GKlKUTGUgVWg-EIyyp7cF9g9R_A-3M0_WXDRBs-jNso4gVsmIpx5to1paU31e2Uo5qYqXoDtxMIsE-cXQtFJb-_J59eDq67hDfRqcaYI69S_4yabC1gq_Ont4jdeFNSgQf7raNeNK5cvJVGWLvVdYC4RA72gtUWrvVigYShivsPvDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=evA3ONY1mO0LgX4-tve6hkUsfJ5BySP6sL2qqNskhrZ3GTT904OpIVBL1fPAC6GyLldqsN4wSaM40MJgZmPj6hDzwt9RkSXMUxZBg5YfimWO_JSGNyusLI3tgvLhpgtGFzI3OqHXEgCXK0ejK1rUebKgBjAoNWqgwWxGY9_GKlKUTGUgVWg-EIyyp7cF9g9R_A-3M0_WXDRBs-jNso4gVsmIpx5to1paU31e2Uo5qYqXoDtxMIsE-cXQtFJb-_J59eDq67hDfRqcaYI69S_4yabC1gq_Ont4jdeFNSgQf7raNeNK5cvJVGWLvVdYC4RA72gtUWrvVigYShivsPvDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه میفهمم احمدشاه اون زمان چرا این حرفو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82387" target="_blank">📅 14:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جواب کنکوراتون کی میاد، کد واسه شارژ ایرانسل لازم دارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82386" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ2GRgG5xPAg0FNaha0N4gM7djMSC_Z8Q_JuN01Mc1cwv5XF8kqz2bPQM3mpvL8T3_Ldot3PP0d5OKoK9eK50zrXdygq_lab1URIZhrEBvT4ukM1AEqq42EO5uOy0gptZObxf18BslBlJr2GQkiCNZfxZkHOQvSNBhpG2zpEvTF93lTPfw6a8kQCo83ZufALDPsoEXco18dvkL7EDrxbvyvAtUhcmDtHvxUuFPLhEYe1AVfKg9SZNjZ3i5gR0d5CmFVpZ67wPGeglWmn84D96hFzOmKH_m0viOl62jC3xZF947Y-oWB-1LTUW8s7yHY_pBfv_sS21hmS4Caz0nIXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی ایرانی هعی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82385" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کره شمالی حدود ۱۰ تا موشک به سمت دریای ژاپن ول داده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82384" target="_blank">📅 13:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به چین بگید یه کپی از اقتصادمون بگیره، آمریکا میخواد اصلشو پاره کنه</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82383" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=fEcF3jC5ifyHOBzuO4P0z5AUiuzEQZ55HhEhUPMKpqhrsBOVa-t42E5ztPS9umV8omkbNIitXC9YtLfWbnFHpRdgp8lP3u0cjuPhGR8mwphoyPQCgwCT0bTDXt4rsYkdA__kDr7gkDWh3oEyH3RQkGOE3E3Ccl8j4RCrpjn9tVpMXNCgnH_iFT5ba0j_asd9dgRaPRfURXen1Lun2aXA9DM29QPB_yVhIe6amuqLXZ7X9foQoVptb2NjnAHn69Fj-a8xUdM-z4yy4Ob1cg7iKtSi6YdrFcNk_Djq03ZkdSyyIa5gPVlWtzfKX3QCWuCXqT5HU1eQ2SftpE9Ld-5ABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=fEcF3jC5ifyHOBzuO4P0z5AUiuzEQZ55HhEhUPMKpqhrsBOVa-t42E5ztPS9umV8omkbNIitXC9YtLfWbnFHpRdgp8lP3u0cjuPhGR8mwphoyPQCgwCT0bTDXt4rsYkdA__kDr7gkDWh3oEyH3RQkGOE3E3Ccl8j4RCrpjn9tVpMXNCgnH_iFT5ba0j_asd9dgRaPRfURXen1Lun2aXA9DM29QPB_yVhIe6amuqLXZ7X9foQoVptb2NjnAHn69Fj-a8xUdM-z4yy4Ob1cg7iKtSi6YdrFcNk_Djq03ZkdSyyIa5gPVlWtzfKX3QCWuCXqT5HU1eQ2SftpE9Ld-5ABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر زن شایع ازش درخواست آهنگ میکنه، شایع هم تصمیم گرفته این صحنه به شدت فان رو فیلم‌برداری کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82382" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4SC6xWsE1s9fsXMjQyJBPQb4sqXn9MpXHkot-rxyfpaN-gFn5ZfTgy0m5Y0hZHOV38aCg0waCxiJluwJ-ZyjCmp7lyYzPp8L0_Nv4M4OPrPz7_RwNxa2cxs9STeirOOoAb43d0T2cZierAb-qOkIO9FkJlBFCksNUATVprp1g5FrkOG1EYs2QYWFeZKAnyBnoDBNWM6XRfADtVqj4EHOGmIm7gRP4IcF_pg-IBwCwBXZKtuX8N4ywceMnryOjQ8LbghW9LvjitOhJG8xnwZRktGlRJQyUcvr0D9VGWKGYkoQTEUGyEPpXMyqRIfBSCzVJfx6jm0I33zHf304uopCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر پر کار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82381" target="_blank">📅 12:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عارف، معاون اول پزشکیان: قیمت بنزین تا محدوده ۸۰ هزار تومان افزایش پیدا می‌کند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82380" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtGmxm9CqHfD5SMxNtWvyWxUc46ZaHUw_WBwZajzNocF9gMDFRsiIENTe4N9JnjRg2uIyAfED5imk17wXkT9FW9U1RDrlwtfmX9OfbKXnYi6fL9A8kCYtP_9gzFmsdHoVAGbj6vPAm6A6AUzOS010qJUMS6GVmAKg7_P6VrXhiYXfU8NheQudhAEad0ijUgIf1O3XNK9nT2EPnWKk-8oeEoEqrsgGfO7_OYDf-gk0UytjpK90KIm-Q6x2RcsdTi-_hP8daVsxjNPW1BUz5QacF_HPzB6IF3uEYSS3nIV9XLLbc6y244qjhy9WAVSf4CCaO0fP9qip0fT9AUcnRvKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رضا علیپور :
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82379" target="_blank">📅 10:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45111cea33.mp4?token=RJnDA6H3FwU3l1_28tYXCoFpBtYN6WyKcKb8NOOiOxQlXu-B_GGNSMzzT4dp2t7-OyILHNPypm69NXP4rMETga1glPYD8fdsvr3tGbBfAsgmyEa-C08Xmgk9kANtQP2NiXU7Ku27u7xg-gVcK9vQW2JhoZFQXyNsWtxDmi2beyrMgaSfG7Z80hg5rnerXEVQ8l5m0Hs-gXtww1vpJegEKWcCEaYCClmSxbaq_vFT8NpS_-QQcQnrFPW7a9TrsAu6YcuuMxRhe4fYF7srlPcZRerqW9WbOrJ3SbtHw4m9DrfUNugBfRz0fovHSgaAOdJvxJubncfZN1NCtFq9rFY5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45111cea33.mp4?token=RJnDA6H3FwU3l1_28tYXCoFpBtYN6WyKcKb8NOOiOxQlXu-B_GGNSMzzT4dp2t7-OyILHNPypm69NXP4rMETga1glPYD8fdsvr3tGbBfAsgmyEa-C08Xmgk9kANtQP2NiXU7Ku27u7xg-gVcK9vQW2JhoZFQXyNsWtxDmi2beyrMgaSfG7Z80hg5rnerXEVQ8l5m0Hs-gXtww1vpJegEKWcCEaYCClmSxbaq_vFT8NpS_-QQcQnrFPW7a9TrsAu6YcuuMxRhe4fYF7srlPcZRerqW9WbOrJ3SbtHw4m9DrfUNugBfRz0fovHSgaAOdJvxJubncfZN1NCtFq9rFY5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشته شدم
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82378" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNz1jl8Mk0JeBwnZjruT-7KEI8XrJuyZyiMmrAriqm82b33LsWa1vgxC0vOl8cuMwFgJonILxCP5LTaNiSQ50368qlhze5DMQcSBwaDTldPXTXkZPbm00Yh52Ox5T_KO4Sf_94iuCviz_F_y3FHBT9HMgAf4AOk3_4qDk_wtKIvRGqFNY0ACceGfyb2zJb0-eFWb1K5FmCsPYh-epO1Vjza1D2GxNLTUzSHDXaZKhjbpyVBnjJacQ5oaHEbXRhYw3vlUG_Uedv5EH6KOWWElUtIB6MovPqtZpbSQDMG-oNIQx36pDyAIg6eV5A_XEVW1wP8znzrVh9HulYZm90hhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس پنج + یک بت‌فوروارد
🔥
⏩
از روز دوشنبه تا یکشنبه در طول هفته، رقابت‌های ورزشی مورد علاقه خود را در بت‌فوروارد پیش‌بینی کنید و به ازای هر پنج پیش‌بینی ورزشی حداقل ۳ میلیون ریالی خود، در هر هفته یک اعتبار پیش‌بینی رایگان ۳ میلیون ریالی هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
btwd.link/51
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82377" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دکی هرسال یه نصیحتی چیزی میکرد برا کنکوریا امسال انگار یادش رفته دکتره
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82376" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anqIBEiIQJ6fGSd4ljHERYmAX2Yvf4Zr0XJvgRAuDydnxFXmnNDL3eO4ujTRCZwkn6WwmZlUxqkT9DdGXkigoWyhvlBl4DoLcekPl0SOD2qwoB3l9Yd0OplxkM6bhJqsd4bthGVpO6kwq5eb-54knlDcSMJGsrVZvIAfUZDO0lnndOdua-sqG9YvUc5NjjSinySlK-zZy9Ks874_5uMgzHt2NKONkBRCLjTRcneTDspfin_QXf1Z7WXuI45THNwfyyMpX_qRBQeu_S7UGkDJjZmo_vw01txRtWiX2Fv8sPyh9_dvAThXR4_IY_MWKaAdAjSw7nCt5QfXcN_IxU2Vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا قبل از فروختن یه آلبومی که هیچوقت قرار نیست منتشر شه(پول ملتم پس داده نمیشه):
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82375" target="_blank">📅 00:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=iQQEUlpRiTz0km7kHSxZe2d16SbZObsFLQ4uLJ17KLzykk0mUQYWCs_J5U56X1npx9m-9RSn4jwzyTVhUrKHCgyUXXLIF_fB1qMs2O2oVHVemrr2Q9qHelVWQUMMhu7-qRGrt6Task4bb7kjmVWIQED86nFqPVDiO7N4tvNaXy-8IDhcH83UY5URKDpKAI9gB4yDPwT03HvgmHB5CJCvsZEGX21sLGHb6RAc9aZtEWJSVenNm7B-RO4tTZzT-4H30v7bg5TwRTo8f-IgGyJZHIXBjvCbe30wWZ6PHEvrDb_GNfwsxF4A1RZWLRfiO5eRBeXjJva0ly9KsyMH0D8e9GBFRWi9bhb3gsaV2tUgxwp-ZG6CL659YctmJUExETS7SbisFhR_nwjsX30ImdrVrHFtlEPpeqSTTlCLql8RJF2NwGJhXVyr2aLr1GHsXft6-K8OtCKap1rjIXsURZEchRQJtc9CF5Iu9wl9mH2hzxNQn46SqNH84_4pv7wrJNVWpPR-Sr08nABDGAdS33n8a8UBnNceB0W5oj0oh7oR_xglGT5dUMjN7tjw4UXZpn69s7RnvydVJKBWpDauu__wfIU7tTWlel9jsl2aVYifIqRaj2kKcspxi1-W11NCyNpXkpQSX4qIzg2D8zeX9B47UXD0fFBruDKQ_63vK_LlAuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=iQQEUlpRiTz0km7kHSxZe2d16SbZObsFLQ4uLJ17KLzykk0mUQYWCs_J5U56X1npx9m-9RSn4jwzyTVhUrKHCgyUXXLIF_fB1qMs2O2oVHVemrr2Q9qHelVWQUMMhu7-qRGrt6Task4bb7kjmVWIQED86nFqPVDiO7N4tvNaXy-8IDhcH83UY5URKDpKAI9gB4yDPwT03HvgmHB5CJCvsZEGX21sLGHb6RAc9aZtEWJSVenNm7B-RO4tTZzT-4H30v7bg5TwRTo8f-IgGyJZHIXBjvCbe30wWZ6PHEvrDb_GNfwsxF4A1RZWLRfiO5eRBeXjJva0ly9KsyMH0D8e9GBFRWi9bhb3gsaV2tUgxwp-ZG6CL659YctmJUExETS7SbisFhR_nwjsX30ImdrVrHFtlEPpeqSTTlCLql8RJF2NwGJhXVyr2aLr1GHsXft6-K8OtCKap1rjIXsURZEchRQJtc9CF5Iu9wl9mH2hzxNQn46SqNH84_4pv7wrJNVWpPR-Sr08nABDGAdS33n8a8UBnNceB0W5oj0oh7oR_xglGT5dUMjN7tjw4UXZpn69s7RnvydVJKBWpDauu__wfIU7tTWlel9jsl2aVYifIqRaj2kKcspxi1-W11NCyNpXkpQSX4qIzg2D8zeX9B47UXD0fFBruDKQ_63vK_LlAuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاش بعد از انحلال گروه تیک تاک منحل میشدی مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82374" target="_blank">📅 00:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82373" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1-URZjSvA-A5x3H5KxIB49chiblZl2vHCU_dsatIVV5cFpL6C5rY-_UWZmoPKQRSS5iG3nARmlcsVp56grP6UgIx_rKwnZ5X9muEY9KFM-W1bwIqpf1HBaQss5Ls3-TO4BDfLQ3YUMg0Dh358vHPjr3RyS6kQPoTk4niGjbFEI6HXnaWo2haRxwK-y3X6q97qFsnGzful5uav59AvqziD3xa76_NSdUP6Q7whxRdTYVYUwUvO7HT9tj56wAdGgUU3B4Mkd3I_gxUzd3DMdCD4w5-kTYtvE0oEF_9yAoubVuJUcjMIjgxNoKinMSsCE-vAAi5pAnVxOJ89n3eVWnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82372" target="_blank">📅 00:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=R5kQHqt28ryQFqg9HRj9xJ647AxfFh2KBKPxnlhxgHSnp0QvizdkL6mmz2qY-8ALwjqzHDIRaweYSPJozDYUXG4Rq8ZIcB2Px-KJDckyj7B__zcP0aMVG6v_kFjmlj49YgWrp_M2G-GBWCLj1xQiVLhqSWEwI22xQM6AB8cOSQsSBTFN33FmGHWs-nWeovoyE9bc368BWPwaGgXwW3-viH1vo7d4rbK9X5P1IeyUd5tjOv53Qu09Msu_BamwyvroKT9-jpjglch9i3JFH8s11Y80kw4-w-9iOC2v7ADaKPXcWiMJ1FSRnKHhecXijJpdcqGTVLk-qLuplg3bVBXQtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=R5kQHqt28ryQFqg9HRj9xJ647AxfFh2KBKPxnlhxgHSnp0QvizdkL6mmz2qY-8ALwjqzHDIRaweYSPJozDYUXG4Rq8ZIcB2Px-KJDckyj7B__zcP0aMVG6v_kFjmlj49YgWrp_M2G-GBWCLj1xQiVLhqSWEwI22xQM6AB8cOSQsSBTFN33FmGHWs-nWeovoyE9bc368BWPwaGgXwW3-viH1vo7d4rbK9X5P1IeyUd5tjOv53Qu09Msu_BamwyvroKT9-jpjglch9i3JFH8s11Y80kw4-w-9iOC2v7ADaKPXcWiMJ1FSRnKHhecXijJpdcqGTVLk-qLuplg3bVBXQtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم تو اینستا تموم تلاششون رو کردن که همه فکر کنن این پسره واسه عربستان سعودیه که آبرومون نره، بعد از این ویدیو فکر میکنن افغانیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82371" target="_blank">📅 23:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSzJqsQzdlmjo68MK_sdcNrFWmPXirCh-tgVoMvxa-G95vMUOX7gD7fsN_hsky3R4-PqBybWj1hZ5grQWHlXzt3r66B4kMiw3fMj8r60G6RRYXvdSKXwIbyb1rkStywdIeyyKnOeuy9JIVBAlr637m7jxHb4h3esIk6qFpq5EjtD38fuqFnIQfkhZ42AW-yc5ptcC7IYVxj-axG6eDKsdFF55ejOoKwbMLctlqQPkyx1KEmuG05xPwH-gOjZzBDpEyLTKMIsqJEnVorw21v_N4Qu-lSBCUnXkWQ582lY0DAOzYkOeKrroNx4go6HSML4XG8USx3dL8spGwWgTnpv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82370" target="_blank">📅 22:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
نه خارکصه خجالت نکش بیا اونم بزن
ترامپ :حمله اتمی به ایران؟ نه ما حمله اتمی انجام نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82368" target="_blank">📅 21:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سینا ساعی هم زندس بچه ها</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82367" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e080993.mp4?token=b0lkjJo8r36ElX8xo9SwMbk32Qt9F4UIIWZZ_PoS_mn-0nExND0FwnjMjR_kjiCjY0vFHJSUS5mfYI_qE0kwWqRB6b7_lAlqimPnDnKvhoP5yfboxEt7f-2W-IMHeT01LIm2R-sQ-4NDcJNSl5JzO2mrEercnbGaJgm3D49A7ORdEWK_OMm3TT1XZYYHGd9ygxUzKhVmKr3meSMljZSox1m4N4voUPrzanQ_nwsnWp5LUro_EMqAzaIBaJYyrf4ZPZq-ZVcYGLxjO5eN50o0NJT2mMkwlhBzg1Eje9GqH5aB3E0_35JqQbtpCXwJ_OGh-BIynXj4sgAhwydPO2MNXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e080993.mp4?token=b0lkjJo8r36ElX8xo9SwMbk32Qt9F4UIIWZZ_PoS_mn-0nExND0FwnjMjR_kjiCjY0vFHJSUS5mfYI_qE0kwWqRB6b7_lAlqimPnDnKvhoP5yfboxEt7f-2W-IMHeT01LIm2R-sQ-4NDcJNSl5JzO2mrEercnbGaJgm3D49A7ORdEWK_OMm3TT1XZYYHGd9ygxUzKhVmKr3meSMljZSox1m4N4voUPrzanQ_nwsnWp5LUro_EMqAzaIBaJYyrf4ZPZq-ZVcYGLxjO5eN50o0NJT2mMkwlhBzg1Eje9GqH5aB3E0_35JqQbtpCXwJ_OGh-BIynXj4sgAhwydPO2MNXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران آپدیت جدید داده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82366" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هیچوقت واکنش بیش از حد ملت به یک سری چیز هارو درک نمیکنم، مثلا وینیسیوس جونیور ریش گذاشته ملت یجور رفتار میکنن انگار فیلم کون دادنش درومده، والا بخدا قیافش بهترم شده دیگه شبیه میمون نیست، چرا نمیکشید بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82365" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پوریا آدرویت از وقتی نصیحت داداشو جدی گرفتی رو آوردی به ساخت کلیپ طنز و از رپ کشیدی بیرون همش تو اکسپلوری، همین فرمونو ادامه بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82364" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1Na_rCvEACByIAAPlVqPZ7_m-sOEDcb19VDuNGA544kLtLYLaj7wFaiLmIc59GAV9gcdjEwsK-nXNm8LqH7ERhOzie9Wrr68cnTtOGbkNFMVjO697QGjQKHq2h1PUQnNId-agJfJz7wlqDB4Om9gvaNc9nCst4nB0LQrrj-L6wImvHijcGISMNJGhrnHJ1ua038rgrXJxI6QwGs17HTANlub-aHSTI78Od60Ghc7sYDtgmU0ZM9G07ZXXAPXGkdYogF0xZS42Ue7X8XpoGKb1-6gpv6eznI7r1fXMq358b8VERv6XHQL871-YRaV-CpDjDvo-vjvctXT4rmlzWN-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82363" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82362" target="_blank">📅 18:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GChVpHLYNZdQHGrnmAjnieue4WwfYG7YdFd9BHeheRROvYZNwiAd4HGPNwOHc-ENL4RoRsUS0pg9CIj7ZTup5zipS8dAxS1OJP98TSWn3lSAUbapVikXA7pAm8hNbfp3J8xp9DsMoaqsx6I8tMniJwpT7LmLhzWJbqZCaeOiNBakPy7t8SGt95k4LdcsW3WXzz48umBvES6uCqpZYgC-JbXGvQ-sKRwjKUXsS6xJ1rOWWFQQIfsmLMMilPJwoseRuch-mrsbsDzlW6I3VzFq1A7-tHsFv7BIKQRXEhHeeAdk2i_K3SXsxuxamY4PDJc80lH2a6Qzvg7ccE14FZRPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات یک سری تحریم های تجاری با ایران وضع کرده و گفته تا اطلاع ثانوی با ایران تجارت نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82361" target="_blank">📅 18:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82360">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قالیباف:
آمریکا به دنبال خروج آبرومندانه از منطقه‌ است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82360" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82359">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=C6AW8xADDG-HKRubcV51uo4NdEOceQqCBP9Z_uF2DcdmTwM-bkFGMMGmK9Ee-4Wjl6YUrTBg-OESqFd6LyB-ZxwG2lJ4xSaM3SDBu3lFpYJUIJwxE7xYKOU9OMTBM2MvxC_4N0Three--tSrRB36D9GzeJuCj8iF_7kNM9s2TKoVtDrVq_A7369aCH3fTNWviAuODijRrpc7SrscKo1XRZJMqn5_kWu2wLVVhN0GDHMuSP0mdHuV1Wy9-_q8x_vtmYTeH8XGo1EygBDaUGJEuxfT3qASKMhHA-wR0nzOs-NU_h3B08GcULbW90yQfshqyDC142jHolwWwS7xV47Aag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=C6AW8xADDG-HKRubcV51uo4NdEOceQqCBP9Z_uF2DcdmTwM-bkFGMMGmK9Ee-4Wjl6YUrTBg-OESqFd6LyB-ZxwG2lJ4xSaM3SDBu3lFpYJUIJwxE7xYKOU9OMTBM2MvxC_4N0Three--tSrRB36D9GzeJuCj8iF_7kNM9s2TKoVtDrVq_A7369aCH3fTNWviAuODijRrpc7SrscKo1XRZJMqn5_kWu2wLVVhN0GDHMuSP0mdHuV1Wy9-_q8x_vtmYTeH8XGo1EygBDaUGJEuxfT3qASKMhHA-wR0nzOs-NU_h3B08GcULbW90yQfshqyDC142jHolwWwS7xV47Aag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82359" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82358">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5uaq_rtn75kEziI51lONnTHCDPGdhJN3YbcRollGu8dZ7qkHVZYBqQfe3LiPvZ8AAZjNo3AE2uEAK316iMWZJoWco7va5pdQ7tgNu-dYjKI98oVnT04ds5-6LAzW_knU0rOs2WXcmFQZ31xlZsu0HHVkIWpXrc5PQMq-Q5HQ2tN_-8iYen8AzOUDUQu8ShgzdG76PGNLL5MoWAd7UElH6I0g1KPlQUP4dm17RGmCoHL8ILLnVlOZX85LAyZ7mi6NII6hODfC7-Q5Al_X38xwWLIQV9LFBmrh7Gwhe071bx3lYxqcfcVtOgy0c-INTipQgTLZPK0jFqlo9jM2uSXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
㼀 ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82358" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82357">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پلیس فتا: یه پلتفرم فروش آنلاین طلا با ۲۰۰ هزار کاربر ورشکسته شد و علتش هم خالی فروشی بود!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82357" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">باختایی که دلار داده بود بودش سنگین ولی حالا برگشته با یه کامبک(دلار برگشت تو کانال ۱۹۰ت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82356" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=eJ_PWgQqIawta0H5KevSFQxtwtlTh9uC4xMEH-Z7uVeOiobex-qq6MfBRHmutfzk30qisc9qFZS68xbgTFaXg-lahHO7zl-0RUTPj-r0Rbgk9cvgqdpTnwzMoNNLgd2Rl3Q6P7saNhl02vufUidJQUeFBN6_4yqSn66iWnjCmmYD-Q3gdzpqzAqM7FWjc78OruD-9SddWhqtmxXiW6E_xPc5l63jShwIzn67097nObs8N9vrC6S0siV3fWD3p1SUHe4rsK-NLzMsOpdh7JjNip4Gj2jc44WPRFYtGrafOd-QJRKQPYL-uoyiHPUhpnQoY9i9y8P2S8Gz-Ar4Y_jpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=eJ_PWgQqIawta0H5KevSFQxtwtlTh9uC4xMEH-Z7uVeOiobex-qq6MfBRHmutfzk30qisc9qFZS68xbgTFaXg-lahHO7zl-0RUTPj-r0Rbgk9cvgqdpTnwzMoNNLgd2Rl3Q6P7saNhl02vufUidJQUeFBN6_4yqSn66iWnjCmmYD-Q3gdzpqzAqM7FWjc78OruD-9SddWhqtmxXiW6E_xPc5l63jShwIzn67097nObs8N9vrC6S0siV3fWD3p1SUHe4rsK-NLzMsOpdh7JjNip4Gj2jc44WPRFYtGrafOd-QJRKQPYL-uoyiHPUhpnQoY9i9y8P2S8Gz-Ar4Y_jpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زید تلخون رو تو یکی از تیمارستان هایی که توش بستری بودم دیدم ولی یادم نمیاد کدومشون بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82355" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82354" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA5YUHw5HYlUPaa6XGf-KrjeTEGbfcNX94lbCpRhSBTPx4ZfMJe0aFlOh_SVO-omKwpmzjSHrgy3p6nYGC3Yhd62ZjHeqMkZE51c2SQ0LsPGq8z8WvXIrg42lvNOwHmQ3ETOvylLbn_03qgCYGDUMyl6fHfo6BAeGh5iq7DRtvjF-UM4PocoqGcENHzOgadberKWUp3X_xUA4Al24cczTwhD-PwtTZUxOQJtpegpBmRU0Ln4t9IDYU8W44KL7FsSZ0GyO30eVFqDIkzPxBTMHdW56fh7M00559u0cInjrwc4qvXZmEKvw3G8pAbzqfaySYo5Vh_XkS7-R4opQW9fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دلی که دریا باشه کشتی میده
❤️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82353" target="_blank">📅 15:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان ویلسون کلی ویس داده ولی از درک منو شما خارجه، اگر معنای فلسفه رو بلدید خودتون برید چنلش گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82352" target="_blank">📅 15:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGwAVd87Py_XCJmSA5Ndrh6HAiCtRk9s8Dt1lAyJPXTDPa6hAxVGmR1_NZKgjNioVTZrA6XoV111ejG8AceKJOrdJq7qNZaAjoO5HLR4PycgRth_xkKk6cJ7aIHSOO8e-YbIqrPA-xTi28PnBlPl1vkRNd2o0Dr6EWaBGQQuAVz0iT1DONiyVmnunhHh3hrTDrmEqU0LCwTGRzhOJ5LM5wKb_qJUWLvsf988SpihA9pkWB8U4on0dAWYvmQ5Z5otbeNWsCFjG42gxcGt7Zftu8hG4IeN_eLI-j4yJm2j783BWlV3FtMDeng3YnJ7r8pE50yZrhWK5g4Ko4DtG9TPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری این زنه که یادم رفت کی بود و حال ندارم برگردم ببینم کی بود ولی به ۱۵۰۰ تصویر مربوطه و داره راجع به مهدیار صحبت میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82351" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب کصخل میتونی آلبومشون کنی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82350" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=n7d9cCaG029LgE72uczNFRT98FBcadQQeRXcEOuCfjigMGz077uNEBUskSwH5d56BmrwLghQnvd3WlAKn3FigyHOifoP2fUJZ4CjlmTJeABH6qesOGorJ9dS45vemidTfK_wQw84N7wkAIx7soqSMspFEEXp9qrxsV68v_8LZNYwVkolJvIunwTkWazNxDKqcp0bhICc0kOU4IdY4T_08tLgAnqD2Lxlj_BQOemuQxz1_rpdbpq6AlM_s8eDaAaujez6NcYhaOQLZu3O9fGQIDTjC_t54GLbgbgpMr2OXsiXMBjDzgUs1_c0bXhDE9ZSRum__eGVl85JTnlebbO5KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=n7d9cCaG029LgE72uczNFRT98FBcadQQeRXcEOuCfjigMGz077uNEBUskSwH5d56BmrwLghQnvd3WlAKn3FigyHOifoP2fUJZ4CjlmTJeABH6qesOGorJ9dS45vemidTfK_wQw84N7wkAIx7soqSMspFEEXp9qrxsV68v_8LZNYwVkolJvIunwTkWazNxDKqcp0bhICc0kOU4IdY4T_08tLgAnqD2Lxlj_BQOemuQxz1_rpdbpq6AlM_s8eDaAaujez6NcYhaOQLZu3O9fGQIDTjC_t54GLbgbgpMr2OXsiXMBjDzgUs1_c0bXhDE9ZSRum__eGVl85JTnlebbO5KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82349" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TULLFQy8AWjYqbBdVQfNQCsWilHnlpstkPnPT0rUbSbkj576TAk0D2Szi_QkKliE7qTV-zr-fpMvHKT9XbifgTw8S5NqFztoSydjAw10E-Iv39u0xWQwy0wmKpcc2whfsZRpimqIskrY6Xl6-w5DKFh6v1WmC0wKcvokDVVclOTYsY16LvnJRvXxEU95CDidmjDIhF_OEFr_Wg7m1vuvV_msWRWPh2ex9ax2IRpwGB95BQhWawm9gshECuqIlQDXYi2vID4mSz-IWI9A0-dFwplUlbYGrwCmbbLng9jh6RSuiszw2YhQZj6lBMVXbrIXB1Rm8tWLSbQUXnGNNBqWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82348" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=CCYOS5exG9YhaUZh1fTgdvB_-Lqp4TCOtfU93YFbfEepL8rVDpVj73-s4mhBLqz89y0FmeYxW78fWAJrw13t5kySpMZqCh4AuZFM0C24408FOLWug0wqsWjcXqM3Vmq7Ftde3MS5zBAa7LmRDVhkn0F9h7WqXQFSFtFtl2EFeBxV2dtKNtuqbsWao5QR9hfQt1UJHfOgCjADOxFlp16mmTNC6Dcg9DWYb-XIuuXlOtnMVUbTN9G_XwxFLRyzM8lBvyyfO-xqhi42kSWOMJONYmgMcu5l8DGrja32yOsCcFW4QxoBHp-ssRLkS1oUHyoRewft4dqG2EukM75fwXJt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=CCYOS5exG9YhaUZh1fTgdvB_-Lqp4TCOtfU93YFbfEepL8rVDpVj73-s4mhBLqz89y0FmeYxW78fWAJrw13t5kySpMZqCh4AuZFM0C24408FOLWug0wqsWjcXqM3Vmq7Ftde3MS5zBAa7LmRDVhkn0F9h7WqXQFSFtFtl2EFeBxV2dtKNtuqbsWao5QR9hfQt1UJHfOgCjADOxFlp16mmTNC6Dcg9DWYb-XIuuXlOtnMVUbTN9G_XwxFLRyzM8lBvyyfO-xqhi42kSWOMJONYmgMcu5l8DGrja32yOsCcFW4QxoBHp-ssRLkS1oUHyoRewft4dqG2EukM75fwXJt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرومزاده رو هم گرفتنش.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82346" target="_blank">📅 13:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH2xEHNTl_IEPEMHFi6vLwkNDzni2xHf8RA47NCCl7_CYCcwHTNt9k_a_dZap8Slx1eMYDBFl_SmPVqTppFbEmPN8vPEucLVWBJCbBIkBzC4FuFSoES4o5kCqq1DkVUAY9mrgaVF-oRvoGdGQolx0TGRPn1GldS5nC6Czhy6WLgXl52Dmup4wuMNFcBAefO8d_vfdJq8hUSN-zmW7eOstJvsI5r1rGaSszeuFqGyVqKuO0I3czCpNOjDx2ezDx3ut5J3YtMUmHop2_nciGS7LY_ybRmF7XQFz3jKwgBqQGqTguGmmHIyWt9UNk8AFOKyMXcnRT-BtlHT5KGZnbC54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نادر دهنتو گاییدم نادر
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82345" target="_blank">📅 11:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=Q64RvhRgb7X4FIZuhtEaPKE0JINFWZArJnnrfVVImsy5cvB3BHJUoQlrVeiAMyEzU1R1RnLIDRBIQF3JsYaUp0PXk7NuT9wP5ChZLCxOVSYKipUG1pCSRb4I3CGtIU-uz4YBNElFgStxx4QLtA9HOnE8aHzzqYYulFa_-WstXW0fkRMlxpPB_xNFo2GiCFDb9MZ3zMz0Yw-Qd493yhl8IepGVQq96tUK466TjwRTJIBR4F29ezI8M1nUHVjd3evoSzCeW1a0RUAZ6_QsX2mR18PBx7s5JgcEBGMkRNuuzvzEb8W57ML7SyBk9ngwhZMv1W1QjGiLleQkNLFtwjZ5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=Q64RvhRgb7X4FIZuhtEaPKE0JINFWZArJnnrfVVImsy5cvB3BHJUoQlrVeiAMyEzU1R1RnLIDRBIQF3JsYaUp0PXk7NuT9wP5ChZLCxOVSYKipUG1pCSRb4I3CGtIU-uz4YBNElFgStxx4QLtA9HOnE8aHzzqYYulFa_-WstXW0fkRMlxpPB_xNFo2GiCFDb9MZ3zMz0Yw-Qd493yhl8IepGVQq96tUK466TjwRTJIBR4F29ezI8M1nUHVjd3evoSzCeW1a0RUAZ6_QsX2mR18PBx7s5JgcEBGMkRNuuzvzEb8W57ML7SyBk9ngwhZMv1W1QjGiLleQkNLFtwjZ5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین دنبال کننده لیگ برتر ایران :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82344" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA0Sm53xzbikwxC5L1BQJQESdsliI7LYThLmMa9BbgzQ3zODY1O19jyAJAUJMKfE7MXNRd_E4tiSMjhwjvebYPiWKukA_4fHMGqObQn6vSQq6xArzvNYVxc9Lb6FiVgpCWHmbSWKOmjedH8Wp99OOEqBzJ_DVyVAWTIsalHX1GMXC-q7XKjv3_4uexKGAzCLOSRRBV7mHEFznWN8BBMI1QUJnvwXljHX91S8mQE-6Mkjz4n-AafT_iEzHteil6BoKBuIEqlmNgJqY3VRNa513W7Kuo_2bdtZflHqnTReePYisiKmBnkDopOKWU9Ojcs10abKk0DqO1u1tY7-P2QDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82343" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ac60101.mp4?token=A-foCcYWXlMIvc_pEsAPMeFq5aC5cbq8P65DGc-FedydssOpWeYNpTbCknzEjTfgSHm7OQ50CxCDGHBSvd2IVyjFTneW-tD-kJNwdVYFQpfWA0lsIsvo_YoJOuQEzsBKQS5CVLJd85uei4JUUZ5mxjYFW6SyEn_hgngsRJqZdTufuckqJ17FX_3pQsrT7HXICMDDdF2gbVPB5v1--lbpOEYfgcJr8I3cTRyt-RNWuVCtPIqaPPyXuaHSlY-Aus01vskKWwuzYDGPywSnvbRhlqP7m0J-WNLGHJux2xskYdrkjHNt81oGErO8Ge7Exus9JiXvNEcdGQLEaX9i5Omg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ac60101.mp4?token=A-foCcYWXlMIvc_pEsAPMeFq5aC5cbq8P65DGc-FedydssOpWeYNpTbCknzEjTfgSHm7OQ50CxCDGHBSvd2IVyjFTneW-tD-kJNwdVYFQpfWA0lsIsvo_YoJOuQEzsBKQS5CVLJd85uei4JUUZ5mxjYFW6SyEn_hgngsRJqZdTufuckqJ17FX_3pQsrT7HXICMDDdF2gbVPB5v1--lbpOEYfgcJr8I3cTRyt-RNWuVCtPIqaPPyXuaHSlY-Aus01vskKWwuzYDGPywSnvbRhlqP7m0J-WNLGHJux2xskYdrkjHNt81oGErO8Ge7Exus9JiXvNEcdGQLEaX9i5Omg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه یه روز تو همین ایران خودمون
رئیس جمهور تو دوربین زل زد گفت:
دختر بچه ای تو خونه شون انرژی هسته رو کشف کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82342" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajVUuyF3Ijw5ahF6zzjnVZpP5OJDaoKjhBcQ4dMQh0RZ33bLuqWlxJeJFbv9ypQyUx_vf7k8gUrCPdzCerlGsyTiAiAPXE1w8VS7dLOmS4afSX10pSm03m4d0vpZwRGxCzrD8XfCyDhmmMPuAFvJLrSjB4qLHgxvQpgP9N8w5JgmFIjL674KvNNouo7AGqm_MxSJMFvLwPNh7aV-fYKCDdIdBk3wK4rGsTtuwccFHsYMf4W-6dCPngTw5IMF9Jpofxe_shEbtqFppWPlzlVgZvNsnqMqGg3TCW6Uu9y4TedfJbBY7h0K0ub2TtYxH9M3jsTObaa6vf8ll6Rb_DRgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراکاریس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82341" target="_blank">📅 01:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt-YeI4rXQH8oms3eQm0mM76RZjgmM4W1QbJTfXG9L7tNXBmSxXzw2rrZ2Er_X_OH7uo1j3dAwDC4Ov1IJrtC4-wz7IvjzPJN7sycQ3omxxddV-Bczd_cQQQ0dtwZIEbGVwyoBbhS9IA6fUlpYX2mwSDCMNLW4oETxI-eeO6JMUElgLMuXJuQseFU-ctFf_aH9_s3TcbVTbVzuqIlh-bn-D9d1aNfC-RSzFr_DVQazN8LOMYKjpNnGUakMf-8_iulWSLLRSK0IVPeZzFXRdaHoxbmWTYZXYr8rMCXgodSA-06rtyQ4akmjVvPF2sV5pCE8efxU44nBzuWyVpakdg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا بخدا همه پایینیو دوس داشتن تو لباس بالایی، آبرو ریزی نکن شیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82340" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=QP1yPtZyAcrqAdDnzYmpO63eMrSx3XDI4i2D9773UW6eXIi_Af2et1fC8Zgh6alPaPK-iWnpxpyhlauquM221hyTCAOv7ObI2eVKIe_S1AEoHAlwlrelGUj2GmxiMsgPbxgpNVvY7hlKW4WRsfTV7q_MnZOZZm6OIigbQEIzBbefv4a8UTkQOF_oo1c_k4Vls9A7U7DhYSoP2mFjIJUu7yiw7xVHDxasigYfySUkHtK_MHwDUdfuDFJKAAlagb2rtxCBd74bAiiWXvUFJwDrme7FrlamxMxHWC3XQglnFhBbOL4dLsdDAQvi5s0vFOBTO0GAyNaM1tx3nZkptbsHsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=QP1yPtZyAcrqAdDnzYmpO63eMrSx3XDI4i2D9773UW6eXIi_Af2et1fC8Zgh6alPaPK-iWnpxpyhlauquM221hyTCAOv7ObI2eVKIe_S1AEoHAlwlrelGUj2GmxiMsgPbxgpNVvY7hlKW4WRsfTV7q_MnZOZZm6OIigbQEIzBbefv4a8UTkQOF_oo1c_k4Vls9A7U7DhYSoP2mFjIJUu7yiw7xVHDxasigYfySUkHtK_MHwDUdfuDFJKAAlagb2rtxCBd74bAiiWXvUFJwDrme7FrlamxMxHWC3XQglnFhBbOL4dLsdDAQvi5s0vFOBTO0GAyNaM1tx3nZkptbsHsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه تو آمریکا جلوی در ورودیش تابلو "ورود سگ و مسلمون ها ممنوع" گذاشته بوده، مایک تایسونم از لج رفته داخل کافه و شروع کرده به نماز خوندن
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82339" target="_blank">📅 22:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چرا این بلاگرا که میرن تو خیابون به ملت میگن "میای بریم کافه؟" به پست ما نمیخورن تا پدر موجودی حسابشونو در بیاریم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82338" target="_blank">📅 22:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این یعنی تعویق
کاخ سفید: مذاکرات با ایران تا اطلاع ثانوی لغو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82337" target="_blank">📅 22:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه 2 تا موشک ول داده تو امارات ولی گردن نمیگیره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82336" target="_blank">📅 22:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3_6wvTAHiTjvNZuaSyNbN9tHgvhiMxBhzI9efnRcNar2tUYMXG0YyKV750W_DKi1l5m8BuBRtVVxbRly_1LQo-5jRC5Brg0YvoJ4PPmJVLubpF14GqFR6nOyRQBas1bvB7PmvQ8biIPtMt5gyzS2YnUfgdGVEvo2K3I4F2YQhB3Oa8CFlxZMNxquFL1zTek5i42u1nHWj110PjzBJnCYxVRvGOPAZiceeiv7efdsvWryEMNzrALkiw_41dGzCt38myQkGTRB8Tn4zAVUzBtdLzBsJyRp1P3nMdBybIUOuengSxo4TgMseozBg_sVoEKXyvjLPAkT3GHJfIunoriKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82335" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knBQx-svFOZiAHwiqxd5oPYaLerx6kLS0Js5ugluiWhiMKXElUkFgTXjfcmsxO38-HtnIVX29WdiT0TOOgRMt5QJEDmzWOwQN9NO-Fe1I9xC8LDxN4XTyiC3XqK4_ncXtIOpfX8v8HVmJizUKwx9nOlMRu39sVYhSlJPZDl5IyrT9_OlMdF1cVGOHaEvGxFedPCm4XqMeAvQOq71-stxpQbv_dnogj2PaNB5SmOHO4vBOMqoEi30VSm287TQXd7e27FuwSxt-7nDnlbwKPs8P5KItdYW5gqQh8pmipgGtHaZuE4DFftIxxS5JOSZjErSHiFXykRfB62edWb5gA4xSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7EDNWB-_8mC5mNoj_NzLYfMuHheqW7epv5ZDkT3ZtbqMqTacDStq8xQKq2vGNgLvn7hnSiKLuCSsopCEOLV1s463a630SyYWBZrza7oi2cG5RsSNfZpq1CzYps1AqI1FVQiPKT1sRUgwTCzQu0pmWATyiZPdTWX3FvGNQPZklxkUTKx88hLEDkYn48njVBc1D7rgQlRg_tmEQTZMNsjTNf3tdUv_-3lyNtpNywgWwsXmx_76i4Y1NYq9-HJP0-p31JxO8_pwpo0hvGVXiIkd7lkcVjNSfA7GndWiuhDGF3Y8RrRT9wJlMlKDRdRXOOpwl41Tt1hmgTmkVna9bE8WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد از ازدواج رونالدو و جورجینا عکس های عاشقانه جورجینا با اکسش که هنوز از پیجش پاک نکرده همه جا وایرال شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82333" target="_blank">📅 21:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK2TN4U5sC0FMmH1UTz9k2SqdZtqH9fXR_27NBZ2UY1KYCUkCVKp3NflAfgv5jt3QyDS2QxCpVIG93RRbXdKAo4XHPgik9Xlk-cLMnvwBxh2WhuBo_AvtF3h-T9Dn0SGxBWYCHztrPFocPKipqIg1Q4Nc45lsYu3lGmlv7tx2byFxWN422dOEvXovvBJ-z2tUj2sWRXWT5xzeQijq19YpRXMIOjGy_Li43hXRpoEPtLWvM6_7ekcx8RD5jSq1G0edc_AkyQHSOG27Wj2MDqjEsLGPc8p5Jbk48lDgraZ8k_NxpFAuuS0mk4RceRR4cToO5C7zEvx5E2DlRDz4Ow8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان وکیل بند شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82332" target="_blank">📅 20:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k92OEQuNW3P_BkDEfCeu7ZK5sFTizIh2uLxvok3mvw728qxpHhDI36Ebop3TuTyAWQkt1cCMODy3kw97Ce-1N8javNwmTltSzA2R7-aL7nuTJwZfKIEbUqFI20qdyFug0t33quwSyRlPDeugxBhdEWadk67wgkF2slAY7RUyWw3PE9KmoUlRuPEvRr5hqGjeyoMz2dBwygX5cHTpIY6rstb7GzlQf_GLNvopgyLwh5itlZ9V3RHNRm5SmSPRsF3CVQRHZ3L-7fl5Sa5CP2NtXXdGWudnBkaMgL1QM2TbUmVTEQf0Gy9GCHu4IJQo7gdT2z0HtifNfibEckCa30cEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبرتو کارلوس به طور رسمی اعلام کرد که به پیروان دین اسلام پیوسته و مسلمون شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82331" target="_blank">📅 20:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ePyT1qq6cSTlVwGD76H44BM_aFivMqEUxs3Dw2HJduXXq4kKs6z0Sg6-s8o7qtHkUz8WZ1af8k75Yhy6ftGFlzv_Sfghum9LKmoLIckU4qjSEZoZQrqFcztKw5NqeiyyA4MK3w-oHHj0XA6NdNcl51QNENWw3vhxurJt0mlzVaKT-44oTQ5gLubQ9EPwSCnPF-QLs-_-JWFq5pcoiSeRFe37IWZc_72SgbQxhEshDFN4Z-IIWP4g9AIdaxHhZ5R9ZAbnL-ZTqBj64Np3N4vblGTRk3D_EAL-deQTmLYxdL0xn3NLLhM9Muf0Y6tkXRP8xM257d3lgDBT_4E7p4sT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم بازا کجان؟! همه این پاسورا فقط 250 تومن
‼️
هرپاسوری که فکرشو بکنید رو ما داریم (بیش از ۲۰۰ مدل)
👀
تکی میخرید اما به قیمت عمده پرداخت میکنید چون مستقیم از وارد کننده میخرید
🛍
•
https://t.me/+5t_pd5JM8E0yZDA0
🔗
💬
مشاوره و ثبت سفارش
@Ad_Parsi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82330" target="_blank">📅 19:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=Bz-a887dFpfxAZQNg_lz-d82nnxFNRFyDy69GFzZIAfdzO5qgWvFhfNc6Y72AitUToivfLiPfseuKUM0GBQqN7LQuhORhCcq_LDNTNRKtHQRLmN6FL0LNTs70ih285QfSZc7H73deHgwHZg1jIiAKd9FEpym_MA4-ibGa2FxBprSrhfqsk_fOK1zGWM-2TJbY24Nbrwyc_TgT0BJLA8107EEmgmmn380HSp2cwrDra62Nkqo9i0HOJ7fk83dcndZm_mghx4uL7gskifTOf8ajYHvVBWJeSzTc03rSvUoOMVcVHKIVCjJTRyIkxiN03llvKfhMbwQlGtn7AhK3HoOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=Bz-a887dFpfxAZQNg_lz-d82nnxFNRFyDy69GFzZIAfdzO5qgWvFhfNc6Y72AitUToivfLiPfseuKUM0GBQqN7LQuhORhCcq_LDNTNRKtHQRLmN6FL0LNTs70ih285QfSZc7H73deHgwHZg1jIiAKd9FEpym_MA4-ibGa2FxBprSrhfqsk_fOK1zGWM-2TJbY24Nbrwyc_TgT0BJLA8107EEmgmmn380HSp2cwrDra62Nkqo9i0HOJ7fk83dcndZm_mghx4uL7gskifTOf8ajYHvVBWJeSzTc03rSvUoOMVcVHKIVCjJTRyIkxiN03llvKfhMbwQlGtn7AhK3HoOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا بابکو که یادتون نرفته؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82328" target="_blank">📅 19:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvoLrThiaZkZwzxc0zQs75luX34jpbw-TLqUNL7U6GGJxiM2GKg6hWX82LiTq47c7221ISQYMTPIOdj_QQ-zk8D95b88ec8JvlC-LfIXfO_Z8SkfUBNjwcwXNUFV6zX9R7wVZYYHbwcMsHxcYhlIyVr1Rjoaxhygr37Tj1X8dSwsEXR0kSCyrhq_WcttNwggc8KH51LkcfTk332s7lRoYHdZyTG1wOuNX0hAMfj8rehTACmkkMdF3Qjpui-nBydySPIVLW-FC2F5_uAkkSLTg_TUN1fmw7aTndrekk-yWHzF_u0M31_d33UpyXr3L2HD3ZtWZ_s-f8OVSHmiEvO1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای خدا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82327" target="_blank">📅 18:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=RaXTiySHAoedMmYBI4D3lO1qiVK79e-1f0dEyb6xTS7L7DrjCclIvbB3MTVRlZBvPEM-hfJWwnBLnAJfWpwEW6GTUdJQEZcchs1Y5kYpjEEtRYWFChJCf5BXSeRw9ATjWd0NyKNTAekFwprZWcpAwhovS1gIcn38pXBTjsbKEe7Ulum5ydb65P_sTNtWSb7n5OgPBsMLGhcccRnwRnHrpYlk-d4KFrEoVNU1tBPXckVlPjEfAnODLSYDvKnrIicys1mkniOqecrcCFLgVYhIH9fhSNEi7oGtEdBQACzRR4RRVJv5n6ZKji_SFX0BnzZ4vHzKnPTixkvSIqAszHtRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=RaXTiySHAoedMmYBI4D3lO1qiVK79e-1f0dEyb6xTS7L7DrjCclIvbB3MTVRlZBvPEM-hfJWwnBLnAJfWpwEW6GTUdJQEZcchs1Y5kYpjEEtRYWFChJCf5BXSeRw9ATjWd0NyKNTAekFwprZWcpAwhovS1gIcn38pXBTjsbKEe7Ulum5ydb65P_sTNtWSb7n5OgPBsMLGhcccRnwRnHrpYlk-d4KFrEoVNU1tBPXckVlPjEfAnODLSYDvKnrIicys1mkniOqecrcCFLgVYhIH9fhSNEi7oGtEdBQACzRR4RRVJv5n6ZKji_SFX0BnzZ4vHzKnPTixkvSIqAszHtRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ معلومه سگه پشماااااش ریخته
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82326" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0wkKAS51Jm65TLp1KODup__Bl1t7PpXQDhUhQQkFNbw5q2XcqFtXRUUaQKeNxwb0m6eRUi3NFAUnbuHNIGm4dU6AHXxvUbkGIbc6twshsO5f_Y0K5OIsqYZTFvGbYs9ixK7YIShuUA6TsAK_wpEu8DSyqRN2hXhHMTVHebG4_QY37oiKThWglxvn080jO2rQbFSqjv-pxBMF_mVSF4yaaIdulYByrEa0_bH1dkebN2F230W3vPtrBDGl6UAMFBJbfoW_kvZsxTCMYJLFKxzkgOrVgiZSntj_1M7RHfMDW1-jUngBIE9ZjQD_6lezSWWec2UqpEVGXafcZFteK2znQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMeHgSI9i3wGzWhWPuLoH8EzvTH5pevXg7TxMY85QmHdxiLuVVRoWP0ChKdhw9LLmv-HWdjNhPv8heucqo1pXhYHq3evcTKLJjVuqINHgDs-y30OcizW1rHul_9J_-rUCoEBUDgCJC6OAmxWdtiKknFOZcoBFsLDaRuJOqMLopXZ6K52i_E4jMMdmE89SNwJhy6NGuT-5mFpGKy6SubQercxj1AqyteamJ4ZWBFC2aYS6m2DSYURUqPb2VHDTHuFB_QNhgEFtjpszbCQUz6ikv5EP6Qe_-CD_oNgLMLF5IbwHAelPJp5Ulja_sRsgMJJX5zMlydlmoZf3pxRvYDRSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جام‌جهانی با ما چه کرد.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82324" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82322">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شورای شهر تهران: به زودی اسم فرودگاه «مهرآباد» تهران رو به فرودگاه «شهید خامنه‌ای» تغییر میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82322" target="_blank">📅 15:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82321">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">طبق تحقیقات جدید محققین، افراد باهوش هرگز ادمین فان هیپ هاپ نمیشوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82321" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82320">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udUd2BXonM61zYSWFfCgsG8e1Qtdi4i8fbTSPrwkQHbtYVSp8KgvELXFkla_NEZXRJzqzFryzln74__w1Aio8NjnUZLYPQnPMmybce4wON5Byiqd8_qiKXWoUwIHy6RNvI1qBFQ-EVJ3ZR7BSU_EinOIeN__GFDeRRi_cWwVkApRshxlt2bz_mCGG0dcFzUyd-Ysfp9V-bAK_YSLwtNmuKf3sI7hyV8gbRk0MZkSbER1lVc3vBPcUrDWakRH21Ny87RSPuaiZbT_cHzsRpXUYxHIrlRjtwHFeM3Ik22czxMGSCf6GinTGjceW1ueu_HnlqxJm_vI4elKMH-YvRVhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی کاپل هاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82320" target="_blank">📅 13:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82319">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbrsJXxHI8F8_cknPAmkXv9enJwNvckA92cylmXkhw_4_EiaqszXnoxORbk969O_63bIQcpnrwnVlQFeR5FfOy3Xe26Vu1wk05NmRWw0zfwDTd389YYpXgk8V2P3Qm4YZNlMIrvuRZgUj5Fj-qDXWnWY2fg6hlD3sZ44HOQPKvlvjVo-ihFK0cf9rMWQ38wem01mA3xSrpSxYBS8pBGdTECQHOfZJvCq89xFqCG6TEc6ufjWliU-mO7uwU-KuwDaW398H7uF04SgOsAr0xTqcNflljvaXNcidfYyFE4CCHPco6MIOV35Rqge3419BquLfUKYkeNpNsG9ACNrCMuASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۸  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82319" target="_blank">📅 13:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombRoKe( Leandro Trossard)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZCw_pnwXzy2h3fF5uQyhm0AQjrk9meEs07wjKIYhoHw1LxZY9gOwudOMFhSxO1ekzbhbHxcGTnwxlMFcAqJ8RzldLVfo6VoH11xPS3OMUusjPhpZspq7XAP3e9v66WcOuYkIjvj8ZAOnun_skmrXEkUWlh6ZWjXNzF6oB51t6p_xHM2vahgSns5IprXdc7kD3pZlEBCBfOuv5YHu6g8_enR5N5gX6df8Vkz7WJeph__te1pmJaiwL5hvTVR7UxjcDX0p9-roRsz5UIiYAxi58h9K3qN1ndTDmPfJ9ofqFpZyLy8CMB6-zcMv4tCmhBjekc9ZeylbLdV_EY8chG2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه (رونالدو) رو هم تایپ کنی نمیتونه بگیرتش
😂</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82318" target="_blank">📅 11:42 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
