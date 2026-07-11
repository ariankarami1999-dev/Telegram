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
<img src="https://cdn4.telesco.pe/file/BMk7N1ABk-CzoSYM4MbFOzKenT2N0yERUrIH2i_7dLx1u8n2Ea_jJHFdvucO20CHTSHNhSiFvc9B5zbKsjsLbDQGDkNlGJX3EW1WsmrVl6kAcXMpyV6czJHpnkNZMFd5VMHxVSGUQFULo7vDpuAjFrksxunVSIvls8oybdifxUdBQi2ECtxDIEC1OX0omOEr9NcoBNPbDwJnWqHnVgwKl3B0OwQZ8ugGaZNMQWDmJovqLy_hF04R6tTZV7KnKbfA15mIPFRWXbsqhQHxJpDOhm7kqDolUAAf-fjrMkmO8m0v-1vEFtp6TwKquZsGqAnXjiUw80Una05zKNzyVWBp3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 23:09:05</div>
<hr>

<div class="tg-post" id="msg-80044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تا الان کی زده
دکی
🐳
ویناک
🦄
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/80044" target="_blank">📅 23:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فکر کنم محمود داره یه 20 دقیقه ای میبنده</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/funhiphop/80043" target="_blank">📅 22:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بنظر شما کدوم میوه مادرجنده اس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/80042" target="_blank">📅 22:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بنظر شما کدوم میوه مادرجنده اس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/80041" target="_blank">📅 22:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۱.۵ نمره خودتون تو امتحان دینی مهمون فان هیپ هاپ باشید  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/80040" target="_blank">📅 21:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/80039" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80038">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7QkoeNCrqxfGBY_CDftWOplnBwYaKJ9kFAfvfNs6RploltaTLLnS9faYcBd4XV26i-ylEoCjsRCgTlPppeblf3-HwfrqdVlSbloR8J4zUfgevg8mMDjZBukHe0-qBPnSaIVpsr6dcpLhsUaHLQS6-g3gR1jwyIornq-4KLfx8cRg6BVH5e3R9G9OyXWghmG6rvYJLxYGWm7ZOpQsWiLErnfVHEHm7syMfm5EBYDeQJKrkbHRVin1h6j2TCOv4zLge5H_Zc3D6yz03nrQ_a4Kp7shERFW7gnylL1FI9HJHggpWYAyX8yR03GPlPbvVEivJzIuNsuqcyn6PDr9q5uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا هرچه زودتر اقدام کنید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/80038" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80037">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ولی خدایی ویناک چی فکر کرده خواسته با این فیلمه پولشو پس بگیره، پیج صدفو باز میکرد عکسای بدتری توش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/80037" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80036">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">استانداری مشهد میگه ۸ میلیون نفر اومدن تشییع جنازه خامنه ای
یه حساب کتاب سرانگشتی کنیم: با تراکم معمولی (۲ نفر در متر مربع)، این همه آدم ۴ میلیون متر مربع فضا می‌خوان. توی خیابونی با عرض ۴۰ متر، طول صف باید ۱۰۰ کیلومتر بشه! یعنی تهِ صف تو نیشابور بوده، سرِ صف تو حرم! دمتون گرم، حداقل جوری آمار بدین که با خط‌کش جور دربیاد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80036" target="_blank">📅 20:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcZfz0O1cbmCthCclaYVvkqBBsv1vHreJ7c2tAqccvFDam6HazrN3xvLpOOmJeQ-Z_VQicyA4ujyeHScYTizzULCHy8CsnTRfGKEW2xPrafDrIUaclNbhjTH8OlSkT07IU1FfxVQ_QHnb_BH7kmk4IBrs4C5xKhPJJOYaCdHRriDgx26g7FtpHcozizHmQJ-h5vO9mCodr017z8cfk2sUjYskOAJEZ4KwLRkbq7T3ZrTUtjoj7qm7ORrvTJGaibkzPo-kEmsuEVxlx1dL-4FZGJQ37DoqibVSwW1lAp3wsPY5YQxDq-brh6Z7DzRVyKPMitQa7nW5Z8M9sagSZhQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوربورد یه ورزشگاه تو کرج :  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/80035" target="_blank">📅 20:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/80033" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویس جدید کاگان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/80032" target="_blank">📅 20:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714a553f9d.mp4?token=YxuoDE1iI9l_Egcu_GCObtAyLrlmFyFEybXiwaGu0Bn5SCJ5N_VI7F96gccUFHHr7glqfKRUMWif51GrmQ4KSNAsG6Ecr4sdwMivvR90ObotR1kFxPnz88ZTq05YE-N2wGPsyjsj9XBK_-yWUjW9avAPwm7_qbntJNVznf2PXCNfiMh_XhfVRUc4EWBBIXDSrzaIjin635sThorvdmuOVmhX2aLTpD3feRUzKvG-FXfFM3VFqmZoI9xjbTtR83ulu1u4pHWSGQXjmBTzUWlUMPS3RxbnAWDzLagg26Et5-cxZxr9cIgLESBqCVh90xRAmXwrPRcbOSE6rD3--n3kt1YhedcFxJ1Eg8BLaGiTaTJCtep-fIwdTzpPbZAd8zW6FqHFzTZkjW3dbCavN0TYHvk3B-719ca-kPf4zhdaq3JHPmxt9uSfA0Vi4fH_E0LcMeVwrCWQ3nWQMMttha5H4G3lbAMj_z0OQCY7vqXTiPhrpKszC-bCjiNcL25swt0toDsX1Dx8CSxaZbr4ra5Xr9s6zb1rAYtSNzgpVJQYSLTS3AHJ76Q-HbbsX1im8L14z5gOK4G7PoCCx2Wg0LfHsYvS2ukrnm9gzsQQZqjXyRwzmNCiXy0xTh7eynr8ed5L73GJx1wBBB3D733G3MTyS4PN4ny0XiAG-ZazPBahHZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714a553f9d.mp4?token=YxuoDE1iI9l_Egcu_GCObtAyLrlmFyFEybXiwaGu0Bn5SCJ5N_VI7F96gccUFHHr7glqfKRUMWif51GrmQ4KSNAsG6Ecr4sdwMivvR90ObotR1kFxPnz88ZTq05YE-N2wGPsyjsj9XBK_-yWUjW9avAPwm7_qbntJNVznf2PXCNfiMh_XhfVRUc4EWBBIXDSrzaIjin635sThorvdmuOVmhX2aLTpD3feRUzKvG-FXfFM3VFqmZoI9xjbTtR83ulu1u4pHWSGQXjmBTzUWlUMPS3RxbnAWDzLagg26Et5-cxZxr9cIgLESBqCVh90xRAmXwrPRcbOSE6rD3--n3kt1YhedcFxJ1Eg8BLaGiTaTJCtep-fIwdTzpPbZAd8zW6FqHFzTZkjW3dbCavN0TYHvk3B-719ca-kPf4zhdaq3JHPmxt9uSfA0Vi4fH_E0LcMeVwrCWQ3nWQMMttha5H4G3lbAMj_z0OQCY7vqXTiPhrpKszC-bCjiNcL25swt0toDsX1Dx8CSxaZbr4ra5Xr9s6zb1rAYtSNzgpVJQYSLTS3AHJ76Q-HbbsX1im8L14z5gOK4G7PoCCx2Wg0LfHsYvS2ukrnm9gzsQQZqjXyRwzmNCiXy0xTh7eynr8ed5L73GJx1wBBB3D733G3MTyS4PN4ny0XiAG-ZazPBahHZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏یک پسر هیجده ساله خرم آبادی یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
‏ رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80031" target="_blank">📅 20:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdVdk7x_xu8pBMRjw6eN3vwJjEkILwMwbl-7hus9hZh6da1hHiZ72OYjHaQiD9clZvKmEYJ7FCaW7V51Hrwd3WySLzcsHkDwQS586QVMVzXhFC7-a8R_F7v2PxPpGVnVWtvJBwO_FnyhkTz1WInk1nGnfbxWjV3FrpKrDdIN9eCmgiVHjy1HX675o8qYIHkNrjEivPw2yaY6gYanxXqAO3kZrCp3rXlBMsvL_vTrZuTBJKDaqsnC3CBSh2kp90dR6srInS8f67R7z9u_EOfWF9SNu0OYDuXywR489n7mIqvbknNaOGmp_fy_lcGQ9NJWsHR1auomjVALMdCLdzWgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوربورد یه ورزشگاه تو کرج :
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80030" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شاپور بیا رپو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/80029" target="_blank">📅 19:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شاپور بیا رپو نجات بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80028" target="_blank">📅 19:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محمود فکر کنم دکی هنوز نمیدونه منیجرت میخواد هرکی زمان جنگ به تلگرام وصل بوده رو بعد از انقلاب اعدام کنه وگرنه پانچای بیشتری میخوردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80027" target="_blank">📅 19:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وسط تابستون برفو میارم بزات</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80026" target="_blank">📅 19:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خلاصه دیس راجب اینه که ویناک داخل ایران مخبری کرده سروش اینارو فروخته، خایه مالی کرده، ولی کیر شده
و میخواسته با فیلم رقصیدن صدف قبل از پخشش از دکی اخاذی کنه پولشو پس بگیره ولی کیر شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80025" target="_blank">📅 19:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80024" target="_blank">📅 19:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80023" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80022" target="_blank">📅 19:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80021" target="_blank">📅 19:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/80020" target="_blank">📅 19:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQuzsjDF0FfTXDOEUt6LsqfY_6kzJMY0WhIQnAwJQwTG1mZ1bDCQWAEKNouwXTkR3DCrrJJaUluXmqODQfzabKyW467YlTsWIwQkM-6PmAbQG05BZzj_LhGCb09c9m-C0FrzyoPmxzJHt3_TlOW5H87zBn3Spp_oy9g5NJwJri0z_l5l1ED91imiUXTrsXhrLzxGAAbfEC4_pP2E6RRdNpXAhoQCs85IkMJBmGRqTtzBciF_sLN_faB_Cz4wQ4pxFBUlH2cSwBzH103W5bwq6cXGeQyWjVQb0qgfIlTr_xwnChOsRU27M5sEC5rbt5rH0J1goZEKE7gqCLu6sV-Apw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80019" target="_blank">📅 19:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بیگ شگی معذرت</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80018" target="_blank">📅 19:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دکی بک داد دوباره</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80017" target="_blank">📅 19:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0ANjnXRnTwUFS_6lrDjW9xW-NQBAQ7ilgichIIrPf4h5VTyVMZUF2wuw9aktDG6AXcQgZoEAavOQTadpygVnaSzpXtihq_a2JalnYljjhnCCGgF_nZcKgwvi58ClZgrpzjd6KJtLm3nGhrgxILi0JHuGirY0V2UBKCudNDCHS3OC3FiQEbukHp4JUp7JVjypDzDYDAc6V0qmpJ79gP9N8lB_cQh1CAWTSFhgoEhdeNgJFF_OxK-1CbZ9DU6ADpW38WehpQuT2YJttMmKr8hdGapOW57LmKtGTpPK6ydDX7dJjgKWLJRm4KFHyDY2aAU3KI-5LN6jaV7cDTgAx1ybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی داشته از هالند مثلا عکس افشا گری میگرفته، هالند زودتر دیدتش عکس گرفته استوری کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80016" target="_blank">📅 17:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80014">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTuv0a93Ruq7XY46EnIT8vg9JNI0e_ddBVMrfSqIM_8yO6r2hcwztWphJwI2vQOAvXjP5sU7brLCy0ckcCh631mvtrsqiRn-UaUniF9m_Zw5fV4rNovzj0uHXqZVsxGGWe9RXaPtd267be5MsMliv448gjUnqKoVUuWlTeNi2QfZiEyc6FRqCth2BngxLqucgauNJMG1xMRsTiUm30ibIlWbSHgXKevFTtJ86-a6D0BduXj74MHl4CktHJ4b2ZvtItimPm6BJdkTfJN-oSGVvH3kZqpZnU3dpFmVACwbU80fTXQeXmXln-k-_BN5stuuMEYQjC8FTl8utEZ0ODcBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک طرفدار فلسطین با این مرد فلسطینی که تو ایرلند پناهنده بوده رفته بود تو رابطه که هفتهٔ پیش مَرده انقدر کتکش زده که زنه فوت کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80014" target="_blank">📅 17:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80013">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epeozryt6IYzVbaGZ5o1E8SZPK0z9fDENC5Jn1K-VcWImnJfy9X1ccBgXY8s2XuqaykLzwAxF957lknfBhUpAHOvI9VXc532cBk6q_1YDaXN_VR8DIf-7Lp9LhDP-V7R-0q7HUsfwD1a_5Pth0BvXnBdsyHdfKqWkz7GUO44GNGy5hfygUUp1e3aAQsEZZM1kZDOzyQwJwsNFPqMsX5ZoPBIdNiCSsKqFJgxriLcMUKb5XfW-OBAzqTy6Xuin1d2Qu87TOsL9B7xOyCRK4gt8OTEEnOHD_VF2fApMUVlXzQiEyVmPbs5CgkGlrgAiyewoPl3ZyiIczUVVaLyyRD_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نروژ
🇳🇴
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- نروژ در دور قبل با خلق یک شگفتی، برزیل را با نتیجه دو بر یک شکست داد.
- انگلیس در مرحله قبل در دیداری جذاب و پراتفاق، مکزیک میزبان را با نتیجه سه بر دو شکست داد.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی آرژانتین و سوئیس برود.
- با توجه به قدرت هجومی بالای دو تیم، گزینه‌های گلزنی هر دو تیم و بیش از ۲.۵ گل، انتخاب‌های مناسبی برای پیش‌بینی هستند.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g20
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80013" target="_blank">📅 17:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80012">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیگ شگی خلسه و لیتو و پوتکو چون فعالیت سیاسی داشتن از آلبومش حذف کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80012" target="_blank">📅 17:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80011">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آلبوم جدید بیگ شگی به نام اکتیویتی منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80011" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80010">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiYF22In16Ls_vWrc7q1m7evk_SiY9QNUHMbeYyJzu17cqJRV_AIW4nydoYtyZG3OuuzNFMupN3rgTjmJgl_ohni1g3yeVL2yYvNkcwgq_5H9bqljZQFxiR3GCvEraA1XpWmM5m6ENhjQrCdqwTx-P_USBjv3pYBI5Ia2uDjytBfJCU_Y434MjHpkUGTh1m3SE-n2tRfhRXzpubysL_c4SiomcNIQzOWe65fpwtdWNCL4HDYUyoKmPceBiN_9gU4xVrHxAhjtyt14RVL2RJ90TRF4jwFE0JAzmpCAZB9_vNwM0hfOquz04ADnZxS2b1SBSLBq_krP90mnNA12LNWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بیگ شگی به نام اکتیویتی منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80010" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80009">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کریم آدیمی: یک فینال سی ال
کل اسکواد بارسا: صفر فینال سی ال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80009" target="_blank">📅 17:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80008">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah1_3Eo5VGvRjwOHei4TV_PqJCn99CTcOyapcQsesdBDphsQgZuuAvbAb5j_HfNFLYHW-p0smY70GZ3_ozAA2f6oz7VjNNFRLaATlQorOC0mf4CF1XD5WXkgpJO0aPYThpD2QnqRXkZwJeRxmcfGSN31pq52GpRT22s5KBycUNUy_SKKQGTJcFaONAZhSKuEPRblZz0ZzueIFWdsc5Dm6jepjdntb0pjr4WUNRo8YIQfTwcQSYNH6OFjlJlRpnrUVZBPq_Ykcf0R_05CPCNwR1-H2tGbkS5UgLNGjIyUR0bN1MbNI5V2_FxGdY1UD_kUadNWCcP4ssVPZh7RpE5e5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گچ کار آورده برا دیوارای حسینیه سفید و بعد از قبل و بعد کاراش عکس گذاشته و ازش کلی تعریف کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80008" target="_blank">📅 16:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80007">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مکزیک عزیز لطفا امشب فوتبال رو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80007" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9ef78584.mp4?token=CveP5g0gRa-M3YK6XV_CBmo_U0fshsOWPkqGoeYI7p776gttOR_YFeaI8g0I23twlZ5LK7_yCKOXnCwiw4MMlrTbWbkjhbvJgHONDOGPoXJBuNdbHeh2LrEpMeMPcrvvJ991PsuAFGmRvR7sDW5zTYycy08S6z4ubeDV_siY3YcNPyO0DH3WzfRDRSZ26Ssodzvjyz23E5Vrc8gIwTdALsrgYwf9w5v_ouZPPnnBYdlvsjIqy2-cHDKHH8uNr7btepQytdTtno2wh-q11gLHm1nsmsnDGhzzZ6w2bfFcQ0W7aUnUWegYz7LCdmpLPCzjIZmOzu-2om-OARGJIMauwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9ef78584.mp4?token=CveP5g0gRa-M3YK6XV_CBmo_U0fshsOWPkqGoeYI7p776gttOR_YFeaI8g0I23twlZ5LK7_yCKOXnCwiw4MMlrTbWbkjhbvJgHONDOGPoXJBuNdbHeh2LrEpMeMPcrvvJ991PsuAFGmRvR7sDW5zTYycy08S6z4ubeDV_siY3YcNPyO0DH3WzfRDRSZ26Ssodzvjyz23E5Vrc8gIwTdALsrgYwf9w5v_ouZPPnnBYdlvsjIqy2-cHDKHH8uNr7btepQytdTtno2wh-q11gLHm1nsmsnDGhzzZ6w2bfFcQ0W7aUnUWegYz7LCdmpLPCzjIZmOzu-2om-OARGJIMauwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیس آف نهایی کانر و مکس هم تموم شد
فردا ساعت 4:30 صبح مین ایونت UFC 329 شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80006" target="_blank">📅 15:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80005">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دنیا یه بازی جام جهانی هالند امباپه بهمون بدهکاره، ایشالا رده‌بندی میبینمش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80005" target="_blank">📅 15:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80004">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTvbvnwzC7Jn7UoJPvk88Huvxnn62kM8DXemxIRyk89u0IX0ezpa1gGWrTQn94NS62gjQFBE4mOQT33VNJta75zT1rkbO58uj-pYfV3vLKsSj01KpldnmRHX2bLrfU-hyL_g2Y4HtLgLExCaMaVAb4fyQOOl2mzLQQyOLPrtU2R72LV-wiakaR10fhkJ4-kXwyri83iqEjFrp5mrBgbf_Xvxz6PAenR9vEZ1JWb777vRoA6uZlX47h3cjm94hXuFOqlMxDaSblL2fYQsCwOqB2ZO9zxztZs-RsslJXZ_aoJhmbNk23xYEHrGkF_7CiNE_eydGODHpveiXmbJi4bFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۲  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80004" target="_blank">📅 15:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80002">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ny0H8pt05R4sNj0M41FhaOAKa8LrdIseRoAc481MPwHEy98lAQoS9K7KSFs3k8tvj1LajkSgS7udwONLYMzbOa_Cbr96mD6VKtV3wO8Pn0AOve5of-2z-QGu1SlSDwhOMCJjR5g5DzNskfdBU9iC_Fd1RSdsTq0HhQd7OL_nHkGjJ_7lDUJDe8GlrQDDyKr7-ZH3g4Hniux1vPLIX9RZcKbJSFk4hjZCyunfPN97e3TYzHOEOJlSCVKjDkX5CIr8-BbbUmGfF_G_Rm14TMspXAnVDYlVo06XIJxs9WFoajDjMbNx5YLsTxaeQpNZZ9drL8bQsIV272bvAxoSb0ZVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvFzpdaagS7CBMNRx6ygnbB1IyKk9IaDtUvCT6ysoY-b3_EGF65zoXbK3bG54hGh0FnszJleDGk2FANwZkvX8C68uwl390GsHBexp_MPxN7oqsfyBLHGqyx1-CtPM0jU3-8l--SmAjgFdgkQ3NPWYh69Kb0DEyXMuCAhvmd2uBQNkVEZJAkdY42y-6wzSirdbtnbwHxevRlSryoGnTJcKSYzjvLmc7R2YXqUUc5545zyu19acixfl4N9CggbY-RMfXbAM2wcObRqN-sQdO7-WKcrjEWGF3lxlUf3n1uofKaZ5WJ9RS6VivBjOKHeYli2YGi74gTPbEEIDcgauBda_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وفا جان بچه ها تو کامنتا جوابتو میدن من حوصله شو ندارم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80002" target="_blank">📅 14:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مناجات پادشاه سامتینگ با حضرت آقا در متن این pdf: عهد می‌بندیم که مکتب شما را پاس بداریم و آن طریق مستقیمی که شما ترسیم کردید را با استقامت بپیماییم و در این راه از سختیها نهراسیم، و همچون شما به بِشارات و وعده‌های الهی دل ببندیم.  عهد می‌بندیم که انتقام خون…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80001" target="_blank">📅 14:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80000" target="_blank">📅 14:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
  <div class="tg-doc-extra">150.4 KB</div>
</div>
<a href="https://t.me/funhiphop/79999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بالاخرههههههههههه
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79999" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79997">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">باز هم خبر بد برای دانش آموزا، انگار قرار نیست امتحانا عقب بیوفته و از فردا برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79997" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79996">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NukUWWOgwJoaQoOpSbUhofmKwVqmvrEAEcozbyZW7ooMyRG0H0uxgGDDOIe_3RFfnHLbm1qn-fzBNrJ7_qTUmNZBPWAFGi-iM6pqqoWbhhHipWMlI-mXQJBbOls680INxBSj7BoSHqmyCUI48DaevzAql1IABAf0xAkwYc-8h_VZbLWW8EipByKlWZw76W5fP9VTxJg3uTEZiSRxY6l1llEn2XKp55oL-RkO_lbVqUytlw9wXFD1O26ClGuYF1n0ftBMD2e6f8k8IZlgvt0ehWokE0rw4MgNC3858nTi_hZde2MiUHDvJkOY1ArQCrwfHuXe3oUxMdepJK2Ytj1dZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل آزمون امن یکی از دانش آموزا کنار سایت هسته ای فردو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79996" target="_blank">📅 12:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79995">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پلنتون برای بعد نهاییا چیه، دانشگاه چه رشته ای میخواید برید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79995" target="_blank">📅 12:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYjhWLA1m1tO_Qgsl_3GrVd5kqng1DtI0MHIa2FMSrZcSsOidUooQhin4wwidy4RnD1MoF0TSC3fV43pYfvpzTQKIe_UIkKIWbq6PP9E2JYNHJ4XJDacHOnsHDSsaydayzcEv6trWMjuwLeMzbPsMfJixI8Zy5RyYLAJlrGnqsmS1mUDIvMJxo-wcH-TiKUZqeIgbBKqLkOkCo0XPRdXBnrKKFuEPNLpyjkdY2Cn5MEbisl6NNAuk4DFJQJcwHd_aowZchiXySX59EAemB3PeztNuckqkAQdiXxPrNOSmgAOScgKXxLMjs0yt6SvK4ddwngZFGZv9SSXTGkE8I07JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا اینطورین که این سیا سوخته لباس آبی رو به لباس سفیده ترجیح میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79993" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSnuL7k5kgGem_bnmNHfCKshLJVFVTTLDRjZHoF0Gcrl0h-PbOYly93S0vcO1uH7E20cFHXJHo5wabAcb5wgsaA8WZyBUw3etzFKhDsTZDHdxorIVTWVngQJhLOoMrQQlV5oXjxGPEglM-imC6AeVGX-0a2QpKjWEwVPq30q7HXVfQnrlNHBL9JeCVrcEmB6-Mq4R9xPi-c8lbnXuZL9QHG2ONvt7FKZeMmnYAv4Ud4g38O8rgElh5hXZTeyjC3_SzyWh8FuGPUIiB5O_ndDgKg8QM6p2gTXC7K0UeAFZyB-xLf3evZrtdaIZu8Gk_aD6IZHaAc5lhm1XFdOwOlX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: بالاخره دارم ریش در میارم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79992" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b894cbd87.mp4?token=fcLx7W1oiw7k-llHUUR2zoOECJ7ZpbqJCEmnVOpj3q-wNHdjqqNYHNNUNDA2UoL8OzxaxOAfvecdU5ti_k7RKIXiJzi2WI0J2GipgLhJsXIrpXlZ52YBLxeGnXMEJ0LBKig5RKkxG9X0tBCxzgl3q160UzF8DtknjELqVC71lZ8PUo9QA7pWK6Z-ej0YT64TDuyRtlrRlK5mFA1NrAg69vVE-agpbAJyyBjVIYAIXNjXaBKWXfX6P1_Ln5uu5faT4U6P-M6prTbrqNdthJm2baT9fIY2_IiDhyMIH8Xhtm33Lk5F_RAhWgEJ_zPsiPtubQMBXB5XCk9rxqCBxv8F5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b894cbd87.mp4?token=fcLx7W1oiw7k-llHUUR2zoOECJ7ZpbqJCEmnVOpj3q-wNHdjqqNYHNNUNDA2UoL8OzxaxOAfvecdU5ti_k7RKIXiJzi2WI0J2GipgLhJsXIrpXlZ52YBLxeGnXMEJ0LBKig5RKkxG9X0tBCxzgl3q160UzF8DtknjELqVC71lZ8PUo9QA7pWK6Z-ej0YT64TDuyRtlrRlK5mFA1NrAg69vVE-agpbAJyyBjVIYAIXNjXaBKWXfX6P1_Ln5uu5faT4U6P-M6prTbrqNdthJm2baT9fIY2_IiDhyMIH8Xhtm33Lk5F_RAhWgEJ_zPsiPtubQMBXB5XCk9rxqCBxv8F5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری به دکی ندارم ولی این صدف بدبخت حداقل یه لیوان آب که داده دستت، چقد باید بیناموس باشی فیلمای شخصی کسی که بهت اعتماد کرده جلوت راحت بوده رو پخش کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79991" target="_blank">📅 10:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BddS92BU1VooCKOPhpKuQakvC6cEFf14hvGSlv3jMWSdeRCpv0aNXnjzI8lykVQaDqxCqw-FNQ_3JXlogW-ne-kA1xrVrT8YrJT_lFKspktDmpPOgAkNeNfWknQ-m8bUd_VCTh6ct5x1eRcEmBsTfIBOPTB93J8nSw3CSlupi0BK6gCqexmbrFSSZgmIuA_j5W-W0ZoKCsvYXxpjgHBsgXoKWZw44XxwOmWZpGct0R03_ddXEZgTdwg1gilzc-9VYmVkAJZIMUqxG2-umXPueV8sK6tAwCs7iXD4Fvc0ISXgRa_5B4YMI2RzF_ebrDLxRvKLRul_wmi1vPVcrnk36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نروژ
🇳🇴
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- نروژ در دور قبل با خلق یک شگفتی، برزیل را با نتیجه دو بر یک شکست داد.
- انگلیس در مرحله قبل در دیداری جذاب و پراتفاق، مکزیک میزبان را با نتیجه سه بر دو شکست داد.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی آرژانتین و سوئیس برود.
- با توجه به قدرت هجومی بالای دو تیم، گزینه‌های گلزنی هر دو تیم و بیش از ۲.۵ گل، انتخاب‌های مناسبی برای پیش‌بینی هستند.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r20
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79990" target="_blank">📅 10:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیدید دکی رو زود قضاوت کردید، ترک مامانش بیشتر ترک سیاسی بود و دیس به بابای صدف بود چون سپاهیه، دکی داشت انتقام مارو میگرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79989" target="_blank">📅 10:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیشب خبر اومد که سایت پارچین دوباره شروع به کار کرده، صبح نشده زدنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79988" target="_blank">📅 09:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زدن آقا زدن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79987" target="_blank">📅 09:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWXEfVhZr5M_gj00YejKUzUJTJHHEXbJMqNYkKApTcgn6Ha2DtV6LNpYyrreLKhKBVdppWC_ld0vk-wF6-1sr83Od5uZPK28ihyC8HPleWbngPIVpYpIKaKiUii5FZS8aj1ER5CKx3nmlrstPtdcnGTJwQ201nb5kzLMTAPRsUaqgt-4bNxSOL12-x6cNAyorgd8On0_gjolAD2cvxLrgeDBxckuSih9Qn4wy4rahRRdK4JK-BDSFPteMRw1N1k2abOnoqc0SeBCnWX7rxiBApxwuW-yvLT0Eb6QPFV8h8L9HsR1U-ZiYRdQ32bbRj1lx-o_Q8R1N-amWrY2sp40Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
اگه ترور شم یکسال تمام مناطق ایران بمبارون می‌شه:
1000 موشک آماده و مسلح شده‌اند و به سمت جمهوری اسلامی ایران نشانه رفته‌اند، و هزاران موشک دیگر نیز در صورت اقدام دولت ایران به تهدیداتی که در بسیاری از نقاط جهان مطرح کرده است، یعنی ترور یا تلاش برای ترور، بلافاصله به آنها اضافه خواهند شد.
دستورات از قبل صادر شده‌اند و ارتش آمریکا آماده، مایل و قادر است، به مدت یک سال (با امکان تمدید)، تمام مناطق ایران را به طور کامل نابود کند.
الحمدلله!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79986" target="_blank">📅 07:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیس ترک جدید محمود ویناک خطاب به هیپ‌هاپولوژیست به نام توماجی ریلیز شد.  YouTube  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79985" target="_blank">📅 07:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیس ترک جدید محمود ویناک خطاب به هیپ‌هاپولوژیست به نام توماجی ریلیز شد.  YouTube  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79984" target="_blank">📅 07:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دیس ترک جدید محمود ویناک خطاب به هیپ‌هاپولوژیست به نام توماجی ریلیز شد.  YouTube  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79983" target="_blank">📅 07:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دیس ترک جدید محمود ویناک خطاب به هیپ‌هاپولوژیست به نام توماجی ریلیز شد.  YouTube  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79982" target="_blank">📅 07:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZaCWJMFcL2FXeAZPvLC5AlQnqsUoCAt1iICfuSN6crm5tlu_9DKiCQ4EkMJkBOQbKxeizoXuDGCK2gC3-0pM3zFKzcPl1lfxlN2VQtOMqg88QS7_1tLfDNEfzzLAEngKVKBby_FC1QSRjoEKvfzbvCDTO4uJcRerXRXH_0DIwsohgXMfc5DURDAinY9Wu7hHRobINYl-Z0Cwe1SW4ztBKh6dauZFdIJwYa0c0f_fJ7iyhhrUcZFyDG12cpA29IuDoq3HddIm8JtGtrCCGJS2MbYLJAzInw7CThLlEBDvVL4Zd0nHOtCAgtjvFIrnZhr_9e7QgEjMO6UL4ey6kGiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید محمود ویناک خطاب به هیپ‌هاپولوژیست به نام توماجی ریلیز شد.
YouTube
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79981" target="_blank">📅 07:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxrI3jIPGOx3KSjmWf0G5Wffksip6GQvHfN_shOxYQkPAotOH4itqN6CoVbH5h6hjTEfwSuAv2mKYNfU7aUu5PA5auB4Of_dT9R-J7_7YYPjw4s2-FjeNJnTfuT_aC-Nn71f8qMX140hOMTkaCBozQj58P95bc05m2fIVZeFZNP6u-Lt2XtHk2hZlLvFL9YMEy6fi_3LGt6asewMJyAo2cbSSFedqJcjk-q683sf1o6cT4zPK1SHYEN3k68bha8K45fbfqpzq9QEgibv-Zgs9SHkywtYyTVKzRycmT25s_KBSJxO75Ze_843CpOnB-POZZ4tfleeJzOl9Bax45fXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش پروفسور عراقچی به اقدامات و تحریم‌های جدید آمریکایی‌ها:
ما تا حالا آتش‌بس و تفاهم‌نامه رو نقض نکردیم، پس شما هم لطفاً دست از نقض کردنش بردارید ممنون.
🌹
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79980" target="_blank">📅 06:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba76537605.mp4?token=cfUczBWLv39oO-36uM2ppoV0zOZCTtHmWvU85XVdeRJwHBRTJA0U9CBGpsAI75C4rqxFfR1vmr7-0AsCUU74EE4tybl0EMkSrugmk_UgbY7cGMEgg4eZhbbVCx9scruvkL7T6oHqDIB8qahqltdaCGMOs6YAIez1DkQwZrvFmNGXWK-OFoXq5khIJIi0VTRFo4H2RSd8pgrOPtNG82BdtNMHbtXCNBLuMJp83Tx_Usz0_AiptqKyxl_Vcwa5zu7iALj1Bbgvo_4VxkqtdhQLKsvk4XW4kQnamdAL1g9yZyls-5m5kK0M-CNd4MLsqkrsw332P3iWcOLbToOjCvv5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba76537605.mp4?token=cfUczBWLv39oO-36uM2ppoV0zOZCTtHmWvU85XVdeRJwHBRTJA0U9CBGpsAI75C4rqxFfR1vmr7-0AsCUU74EE4tybl0EMkSrugmk_UgbY7cGMEgg4eZhbbVCx9scruvkL7T6oHqDIB8qahqltdaCGMOs6YAIez1DkQwZrvFmNGXWK-OFoXq5khIJIi0VTRFo4H2RSd8pgrOPtNG82BdtNMHbtXCNBLuMJp83Tx_Usz0_AiptqKyxl_Vcwa5zu7iALj1Bbgvo_4VxkqtdhQLKsvk4XW4kQnamdAL1g9yZyls-5m5kK0M-CNd4MLsqkrsw332P3iWcOLbToOjCvv5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 6
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79979" target="_blank">📅 06:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5412d07f14.mp4?token=TBtWfzg5QB0GvufWpThsLDteLHzdv4jgpeRMXWcJupMdBVw7fSOX4qHrYihyjufdVmkQZ9gzrCcer4V016ElrC5rvwAIVVHtjcxu6-k_ZfkxtnPwt_NzpGx-F9QnuP0v0ILWOs82j_WQ46nIU16f1El4PbisrKOQXiNHKcImYSTZZFqGNrDL0xofis83CQNZlTjMICgcYtz8dFAYxLzefXaF7Ga9upr82s3vvmHvxxPo8It6v4TXcI8_ENaWJpYSbwPKRgxBDO6Q84g9D7FR-mvBKC6fhDlW1WZzqvxzSz1AnLO96Bb5H8OPVxkkIWO3qG4f9OcILmuzxthHIBdYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5412d07f14.mp4?token=TBtWfzg5QB0GvufWpThsLDteLHzdv4jgpeRMXWcJupMdBVw7fSOX4qHrYihyjufdVmkQZ9gzrCcer4V016ElrC5rvwAIVVHtjcxu6-k_ZfkxtnPwt_NzpGx-F9QnuP0v0ILWOs82j_WQ46nIU16f1El4PbisrKOQXiNHKcImYSTZZFqGNrDL0xofis83CQNZlTjMICgcYtz8dFAYxLzefXaF7Ga9upr82s3vvmHvxxPo8It6v4TXcI8_ENaWJpYSbwPKRgxBDO6Q84g9D7FR-mvBKC6fhDlW1WZzqvxzSz1AnLO96Bb5H8OPVxkkIWO3qG4f9OcILmuzxthHIBdYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکی با این فیلمی که ویناک ازت پخش کرد رفتی تو قلبم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79977" target="_blank">📅 03:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzfnl3Wtz9XVc4DV0sPde_FOSs4OgWhZ6NVQsHMhB3gcnXT2M9QghexrMGyoWPuFKFhJL73shj6yPCa_7kQrNzyhoe8nwgBHsQQqrzzuQx0m5_feQhA5STQ-JGu3v9fWOqdQIx_nZAGVSxSaRvkUYwTunEFGGmLlUXbPSBa-BB08jy-il4q6R_JqIXn6j7gu5cex9bBkwv_oExPk4kBXAJz_nE3BTaW2e-HNkKK53PKfA3qKH4miRqLT6QVrHDlDy-Goh-iSlnBYxP2mXp-_tn8CAW90kdHElthSTA2NKuH4yWXaLCpVGFuqiWKwAq4ybhHgIs5ZUhjvgCHUtfPmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصشرای اینم بخونید تا ویناک کصشرشو دراپ کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79976" target="_blank">📅 03:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رژیم ورودی های سایت طالقان و پارچینو باز کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79974" target="_blank">📅 02:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrogxpVbzxRXtzXbO9Yb3t3ksWa9W5mBR4U2nnA4re64fNTFsBzLPy2lKkM5e61drUp2f5L2ts9yfk5iJ5dSEmounr3_6uIvMyrkMVYh9su0nsu7sPcpyZMPa8yOi1WMMjVjqQyYYDOYhB2FYXAQMd2ThUM-TL30nECQXrdZYnKUjWmBuoDKFwCsFog7jkh9O4k4QqWr36NW4HsAbQCKzkOIFRhz25qVIlbb0AOLlNazmmea8-jz8_NIYys8yF0wUPUk7pyUwOjVzh_miyAxc7MR2l-IXu5NhHQNRegIr8_JSN661_81krez078jHap4HJje-Hm7-892MKEXhumMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FuunHipHop | Constantine</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79973" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79972">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یادش بخیر ی زمانی دنبال کننده های رپفارسی فکر میکردن ویناک همون آرتاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79972" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانر میزنه یا مکس</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79971" target="_blank">📅 01:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79969">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGYufaFmf8ei37Pm5QCqsNeSLYF-MNWAg9lclLxXN0x7Xtvh8WQVtMeWzigFtsbevdEPdIucUlgx5S_oQQHJEY0692y-DigO5hTeoRTxuDTIlyGL1H_hpljnMxp2k1NmGmotFCKligXATyHMCvalUsjSziAyS2ECJrL3ij9f7AG45OyUbwgMMNZwMAe-vRkZPCJDReYHf0mdWRG0CVyUydLenn7a6uyrzIykpsPUS20KVUrUYEP7_LtfUN8JLeha59iSRLoGIUNWBgHswLUtCippzFHAVESSMOJK5Osq9m2m2-H25_kxJvV-NSRNQs9IIUXc8wPCfDdKoztGsf2MpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlAda7j-uTt1nf_gqdRF1F_hX8Pun7aW_qmUzPRSaDaVZk1VbnqedGdsogXPSgCggTALRReMrrdTxGOJoSbeGjzVo5nwuFDVIpCES36iw7Sp3KL9MRkNgkCgPSKrDo0TuMvv_GHnAeQI1VnnaNrkOXw7cGBiqCHM70wNClWmzoGD0evoSEq5b3xGnT-9vYT_T9GkeSvSfpoPyzo_yJvNi_w3k4XhmB2cPjsZenmNT5o0le9JOhVlnMoO5K8hvRZ__vMRc-FzryeCVn1yCng8Fy9GgaJ_UTQFByQAldtxQYQ_dnbfEsuyqdQvp7HDN6IM6wr8ngw8MxpzRa4G_ATO4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داداش یامال خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79969" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79966" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79965" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">توضیحات کاگان راجب بیف دکی و ویناک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79964" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAshkan Kagan</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4c7da62a.mp4?token=v7toSf-mljfeonMn6NuyZI4-84YW43qRdw-pIw8roYb2QtaDikrPvOAT-wk0WvyORrajVkYGDdlQqitL8Wf48VvvKbnCEeNnWWX8Hevq0e7FbIwwFr__ofaNVFHEHKrRG4VOxpx7X03YV7tjDxYbmg_wekOc-HgrK_yUlpgDF1PChoR8cNfHhr1Npgf9VjGFc6-ITENc5ktk4rUspQQ3bkJQF1xBElEvxg26VAuV49GxIpV3Pty0PmW8ppbTjoR0NF5PxIf58sTbNb4XeMy1CBfNoVpf1nicc8dlkTLQOtHWGPl4tCmmTFD3T8pDFdEhgUJzKU7VS6teF4sOhtHnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4c7da62a.mp4?token=v7toSf-mljfeonMn6NuyZI4-84YW43qRdw-pIw8roYb2QtaDikrPvOAT-wk0WvyORrajVkYGDdlQqitL8Wf48VvvKbnCEeNnWWX8Hevq0e7FbIwwFr__ofaNVFHEHKrRG4VOxpx7X03YV7tjDxYbmg_wekOc-HgrK_yUlpgDF1PChoR8cNfHhr1Npgf9VjGFc6-ITENc5ktk4rUspQQ3bkJQF1xBElEvxg26VAuV49GxIpV3Pty0PmW8ppbTjoR0NF5PxIf58sTbNb4XeMy1CBfNoVpf1nicc8dlkTLQOtHWGPl4tCmmTFD3T8pDFdEhgUJzKU7VS6teF4sOhtHnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79963" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دخترارو چمن و مهدی بردن، فمبویای گوگولی مگولی من بیاید چنلم.
https://t.me/+cPimg8CRJ19iOGE8</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79962" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مرینو عجب کصکشیه
😂
😂</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79961" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این بازی اسپانیا خیلی دراماتیک صعود میکنه مطمئن باشید  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79960" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79957" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این بازی اسپانیا خیلی دراماتیک صعود میکنه مطمئن باشید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79956" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بلژیک به پرتغال زدددد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79955" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">داور به حدی به ضرر اسپانیاست که خیلی واضح به اولمو تنه میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79954" target="_blank">📅 23:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلیل اصلی بازی ندادن پدری اینه که دلافوئنته احتمال میده که بازی میره وقت اضافه و از اونجا که پدری قدرت بدنی کمی داره و بازیکن ۹۰ دقیقه نیست نبودش در وقت های اضافه ضربه جدی به اسپانیا میزنه
برا همین ترجیح داده تعویضی بیارتش به بازی که ضربه نهایی رو تو وقت های اضافه به بلژیک بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79953" target="_blank">📅 22:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دکی بیا پیوی چارتا ویس بگیرم به ویناک فحش بدم فور بده چنلت فک کنن کاگانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79952" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79950">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کاگان اون ۳۳۰ تومنو بگیر بده تتو رو سینتو لیزر کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79950" target="_blank">📅 21:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79949">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این وسط که اینا دارن به هم میپرن من فقط به این فکر میکنم که اینا اون تتوی کیری رو میخوان چیکار کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79949" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79948">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سکوت تونی وان کید این وسط خیلی عجیبه، کصکش بیا دخالت کن دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79948" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79947">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کاگان: لطفا نگو من اینارو بهت گفتم
ویناک: حله خیالت راحت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79947" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79946">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بقیه ویسایی که کاگان به ویناک داده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79946" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79945">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79945" target="_blank">📅 21:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79944">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79944" target="_blank">📅 21:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79943">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قطعه گم شده پازل کاگانه، شاهد هردوشون برا پانچایی که میزنن کاگانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79943" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79942">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قشنگ معلومه چند وقته آماده بوده، موزیک ویدیو اینا داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79942" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79941">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این بک دکی منو یاد دوتا بک کصشری انداخت که اول داد به پوری و بعدش بادپولی رو داد  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79941" target="_blank">📅 21:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79940">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بابای صدف سپاهیه انگار، فک کنم دکی چون رو زنش کراش زده از ایران فرار کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79940" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79939">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79939" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79938">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79938" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79937">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خلاصه اش اینه که دکی میگه ویناک کاگان و دکی رو فروخته بعدش فرار کرده ترکیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79937" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79936">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دکی راجب بدهیش: چاقال تر از اونی بکنی اخاذی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79936" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79935">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه نشونه هایی از دکی قدیم رو دیدم تو این ترکش</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79935" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79934">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79934" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79933">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79933" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79932" target="_blank">📅 21:24 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
