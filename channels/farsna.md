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
<img src="https://cdn4.telesco.pe/file/m-LA2pxGF-tJhsVWVm5_LwrkgQsLYWftVLy5LYNM7nMwdAMrfP-eWuBa5VUID-F-cNR-wo7yOz1Q_yzcCy2wcp34GL859vS23__Q1gEVdSF8Wkc22GirpHyfuN0cp8Qufp1xrJSvhZkdE_4eANcNKI_FgaB-lCdtXDng8kMNeSH4NK7mxm8ATl8IOjqW3FmXOEKS-g9jl0dxb8iDUilAX-IdjcVVtAudMUSnHaLN0y5MAMwM0aXNGpZui6wOT1A_tLVVHDPzw1u0E7VhJGgOZRtK96Yq6sNZ9wu-G5Im7Df1-XqCx5KGl6fTc3sZ2m-fMnXowRGV4ynoZ98U9tNNgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 13:56:18</div>
<hr>

<div class="tg-post" id="msg-457197">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341e45a744.mp4?token=EdsaX_i-XJClq9FL6zUcp4oePtfMWAnn24wcYH5QkEOwy3LescyGNJfy1aDYCSIgN6KFr7uFRQwrbtKQe-1gswtNixa8ck2sONZyuZTjxEcEzOqxuHJnSRK5AoI-ValMxoYT1cltExM4Z8KPAybxypbEO5JGUSnJx8np4vj4pYaagbcND6Q6h2yqE7iZm4FVJxwDHYqnqjiSN07sbnw1tjg1A0gSZ0JrBMKSXvctkhBJB3XF4_0y01jSj8udfa8LS0gKpPYFc63n4_DeGgUmfA2YW-cRYNOfmo44DtCRlpfQrTPgt_7RrlIb5NOKtw1VJwEgDymSGhYby2zHqrqLdCzITCfLPGsJXMCTGUk6DJQqYG1icr37TTpDWry_496fr57uw0dyeS7bhyjPNSkO81TvWqN0zGcIvTiALG_cK44_q16lxgWWtbFr3kfS45Gnn2O7A9Cmgel4XwFtk1lPd2-eqkqLNu9OxJ8QKzENNIKxssYoz9XeiePAbe-PFjsIRgVq_auffHI37OCeeIe1ZjMWWS4rfyQGLW1Vukir7IH4B0KUt1MEj2TLWHoNuSfwyjTuxNyvXORBbSgfbZmZYmJ3udhEj0XYhCN4XMB3y8bGPpfhx3IzkJkejLie2ux2vOckwDfXsG1Vb5yl556ZdC7cW9uvXNdjmKWz3NaJlFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341e45a744.mp4?token=EdsaX_i-XJClq9FL6zUcp4oePtfMWAnn24wcYH5QkEOwy3LescyGNJfy1aDYCSIgN6KFr7uFRQwrbtKQe-1gswtNixa8ck2sONZyuZTjxEcEzOqxuHJnSRK5AoI-ValMxoYT1cltExM4Z8KPAybxypbEO5JGUSnJx8np4vj4pYaagbcND6Q6h2yqE7iZm4FVJxwDHYqnqjiSN07sbnw1tjg1A0gSZ0JrBMKSXvctkhBJB3XF4_0y01jSj8udfa8LS0gKpPYFc63n4_DeGgUmfA2YW-cRYNOfmo44DtCRlpfQrTPgt_7RrlIb5NOKtw1VJwEgDymSGhYby2zHqrqLdCzITCfLPGsJXMCTGUk6DJQqYG1icr37TTpDWry_496fr57uw0dyeS7bhyjPNSkO81TvWqN0zGcIvTiALG_cK44_q16lxgWWtbFr3kfS45Gnn2O7A9Cmgel4XwFtk1lPd2-eqkqLNu9OxJ8QKzENNIKxssYoz9XeiePAbe-PFjsIRgVq_auffHI37OCeeIe1ZjMWWS4rfyQGLW1Vukir7IH4B0KUt1MEj2TLWHoNuSfwyjTuxNyvXORBbSgfbZmZYmJ3udhEj0XYhCN4XMB3y8bGPpfhx3IzkJkejLie2ux2vOckwDfXsG1Vb5yl556ZdC7cW9uvXNdjmKWz3NaJlFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای یک خواب عجیب بعد از شهادت آقا
🔹
در هرجایی به آقا توهین میکردم، اما ایشان به خوابم آمدند و...
@Fars_plus</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/457197" target="_blank">📅 13:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457196">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiFyr9838XiovIzFpy1WjlaVdC4okY6yRB7W_0ehHhfPyRgSBFOwiXywazOkUk4uk3EcptsjAGG5zmLDKXvOPD3UsWBPaiOTIFdOLdt0sGcm8S7ecgppm4GfirpXEfVCAy_yflBVp1x9flXmT_yOe9s8TwKOg0GxFcjkmgcX2M9zLlG5JkMZtRlsuVcmXCFUMxklEWw2C-2rUwKBiDbm12H1p1y6Dp8IwUQ0bXVN0_fGcAve9jI747yYUc8M_q2AswD6mwkA5upESKdwCGAID4ey10wQ3NoLLyE9TV7Qp4PuBn_sStwq1pe7IHHzcHRQXMvToNz09uVEPxyLV5QxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت به بالای ۹۳ دلار رسید
🔹
قیمت نفت خام برنت در معاملات امروز با عبور از مرز ۹۳ دلار در هر بشکه، به بالاترین سطح خود از ماه جولای (تیرماه) سال جاری دست یافت.
🔹
این افزایش قیمت درحالی رخ داده که نگرانی‌ها دربارۀ اختلال در عرضۀ انرژی با بسته ماندن تنگه هرمز و بن‌بست در مذاکرات، بار دیگر بازارهای جهانی را تحت تأثیر قرار داده است.
🔹
به نوشتۀ الجزیره افزایش ریسک‌های مرتبط با ترانزیت نفت از تنگۀ هرمز، مهم‌ترین عامل جهش قیمت محسوب می‌شود‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/farsna/457196" target="_blank">📅 13:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457195">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVGqF7VrXF2kS_yv23voidq7Zxi2ckIg96QQtcT9npJ3kPA4dKGrwduRNKRY5jP_0PW3IN25a6y0nb0QOCd9ErrZW7SBLP5KrMVuhJj4NQIsOjL1bSk4v0Dmdl4g1XBwV2Rj2C4XNzlHOT1aQEE6yZnYrFhzuMHJrfTOt080lOcC3KgZwtghPzedAdymz6DKq2dTmCfKRG5vvLKghkZpVtJneZTDeMSSNJe7wf1u-eotZXLwRyw6RqUDlX3jq3vLV5hoOkjZAnexpv2FxUa56jKyWVgw2vRbFo0284P-o5ne2pLcRbn3JqDTLS0pDIafu_ByzdI_k4OdZmxTcZ9c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثۀ دریایی برای یک نفتکش در خلیج عدن
🔹
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد گزارشی دربارۀ وقوع یک حادثه در ۱۳۶ مایل دریایی شرق مُکَلّا در یمن دریافت کرده.
🔹
براساس این گزارش، یک نفتکش که به‌سمت غرب در خلیج عدن در حرکت بود، اعلام کرد که یک شناور غیرمجاز به آن نزدیک شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/farsna/457195" target="_blank">📅 13:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBtrogEf6mZsVSCk2bicyhYqKHMh-xEiEfFSIkal_4BsVRmtZJdb4jsMvAZIthrhP21Yjc7hwkKiluciLefq9scUhpMhB8kzys45z-AXqGGDKkJNh1OqDBgG4FaSL1U64balxJHeK663cMnWk_SxXpfkaAN9qOqbNFi_SELp7cQxY8XVHfkVnKMBWnFqDP8chNdGhotXwKllOYofJ1apZBpNbs_KC1xQxGNb1GYhFU6u8XwjBI168MJxO6DU3zkCTTmaoDqJYu-hPN5Ci370L6ZZ0xmXpDs2fAtiAbrE-ZpJlsJtHNS9z3s7vb3Hzq8l3-1BjuiwkEen6FbMRV1KYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCFIdRav0jP9R6YWxoulq-EZ7KNZNTqOyO7Uwi-aTmwoO9ex_ntK-zpPJrpVNyPelnLQ-7lhMHdxDOSsQOSLhcf7RBkDKIJCnKJXsKl4JR-4T-u88A1oJARt0kF0A7dN6mVG-lQNHv_Xz2UsXn-F6Sm1ephEe3fY9E2M2YsiGXd3vS9pEmQoYBk2vOLTMf4zXbn0aRh81OD16MNTrsaaEX6PmUWqUi_HG9LXD898IX4UZKEFF9K-T5RMO7Ub3QK7zZikFTtJ35w5n3vA8vNazjITLpTtaTezAeet5MpZb7-vzpxAwvWplRGLvuzC4utkHN73pBa-1FoKHLwKLlkYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hENDmd4aEqnjgx15deDNE9hlB9EPd6t5NBfpultlfEfSXRJEHqV1rvF0AAPX28_JaTrJ3FFyfD3t0oVAezK7O1STU628-fk7nArZsq8VoBgSI7EQSjHXGi5yQFO_VQL3IplqEIdGt6taON2OGMRrbBnFhN03-5hlUg0YCZoI1uxOBQrECwyFwE7iRrzqGgWkqU8eBXLRwIqo_fECGZGAlSVTGtXaxjGGfUtXpaL3KOQJhWe2IrxGsOM4vFAoF1UySdtGvsmBr4fyMzoGmOWJqRihrmGlb0K6ibrRKTl5wa6BZP6W6oesHl5zFsYpTcoaAdhYM7dOIwNw5ArrmSBSQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d097d3b42.mp4?token=J0SUGa_lMREK1G0DDXWAZhWTVtz2yIO7rNFlYg1TZrRTncsKChCPnqSLHoEbFSv10_U3PSK3m1Sucy2Dsj7LqhXtYu4bYJ8vMBRFLVLpi7E_YhEkjSUbqRamDvutgbWgXvlzCKSa36yWGD-idt1w-AdouOwpniv60Pu3hHiSbb7jxUT8Tv979tg38jfwXrkb9MVB_v19OQFrA0NPnirDsQhRufK7B6E8tGGi67z4XqPMSmJzCYcOrTpTPx3K5JAZT6NafPEZlW4Nl4BuQddF6NH3wLAN9a_UhlfB5Tvc5aq3WBvNwWYiYbJYYIfrPU3C-QtgOUPfmb3kZptFJF8h2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d097d3b42.mp4?token=J0SUGa_lMREK1G0DDXWAZhWTVtz2yIO7rNFlYg1TZrRTncsKChCPnqSLHoEbFSv10_U3PSK3m1Sucy2Dsj7LqhXtYu4bYJ8vMBRFLVLpi7E_YhEkjSUbqRamDvutgbWgXvlzCKSa36yWGD-idt1w-AdouOwpniv60Pu3hHiSbb7jxUT8Tv979tg38jfwXrkb9MVB_v19OQFrA0NPnirDsQhRufK7B6E8tGGi67z4XqPMSmJzCYcOrTpTPx3K5JAZT6NafPEZlW4Nl4BuQddF6NH3wLAN9a_UhlfB5Tvc5aq3WBvNwWYiYbJYYIfrPU3C-QtgOUPfmb3kZptFJF8h2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب برج ۱۰ طبقۀ ۲ هزار میلیاردی در اراضی ملی میگون
🔹
عملیات اجرای حکم قطعی دادگاه برای قلع‌وقمع و اعاده به وضع سابق یک ساختمان ۱۰ طبقه و ۳۰ واحدی غیرمجاز در زمینی به مساحت ۳۶۵۰ متر مربع در پلاک ۲۰ منطقۀ میگون شمیرانات آغاز شد.
🔹
ارزش این بنا بیش از ۲ هزار میلیارد تومان برآورد می‌شود. عرصۀ محل احداث بنا، جزو اراضی ملی بوده که پس از تصرف، ساخت‌وساز غیرمجاز در آن صورت گرفته.
@Farsna</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/farsna/457191" target="_blank">📅 13:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a88da1c3.mp4?token=TqXJPCSFDJcfdZqrYc0fVY9HhLHEKZARJm5iHHuIYAdIz1StsOLEjsJg_KQsRmBvRAOIpfFY6SxdipMNs1p1V-Tbd5b1bcC4Vvk-RnS8P1kpOvRc52sfGwOcpEVFvKJRchvoNBk9V6aeZQvK0T6bM4btUHJFfNTnkS2ThnOt4nPsQYH9piE7RePTKCGEQ29LEwVlc4FPml3OT2zk3AXlDLnR4Hesg9ve5TOOwAl-1XiElIDc1o6cMPEupLDfE3mf8AN6yXf_mYdJGEbTpyFWgl5sxKFR-_tC3EyqY_ApSnL2Vcw947EcAVYSH74Y8IpZvHtXgnDlBytRxwA_I7kswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a88da1c3.mp4?token=TqXJPCSFDJcfdZqrYc0fVY9HhLHEKZARJm5iHHuIYAdIz1StsOLEjsJg_KQsRmBvRAOIpfFY6SxdipMNs1p1V-Tbd5b1bcC4Vvk-RnS8P1kpOvRc52sfGwOcpEVFvKJRchvoNBk9V6aeZQvK0T6bM4btUHJFfNTnkS2ThnOt4nPsQYH9piE7RePTKCGEQ29LEwVlc4FPml3OT2zk3AXlDLnR4Hesg9ve5TOOwAl-1XiElIDc1o6cMPEupLDfE3mf8AN6yXf_mYdJGEbTpyFWgl5sxKFR-_tC3EyqY_ApSnL2Vcw947EcAVYSH74Y8IpZvHtXgnDlBytRxwA_I7kswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین عکس برای کارنامه
🔹
براساس یک داستان واقعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farsna/457190" target="_blank">📅 13:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خوزستان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7OrDE5zKu8Or2rNYDjbh-O1PysaTcCPqps1MvKo1d3u8c5BW1mJpZj8oOo5-jHefw0ipmm2aP4OHoCII-5tba6muBoPj87J1Sq6y85oxA6jn0igeo4yoBjhxi76f7vE5phGByDFzT86FYCbyo9Rq5VHp0X-lDvDYg30eVSaW13PMoqqAuoD25QUUf_M0b0gQpw8SsCtzjNGdsUsfSg1O7yiubW9TY01mB6pdEEPkVrGLaVhLTYuI7-BQKeWuw2aLDstR84EGLszPFGhRB1c0S4dmNgDdFeP39zC8Wrm7eCxIe8vCaksTj6L_K4OghLfk04Owlo77Itn--6J1a1gTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنکوری‌های اهواز در تاریکی و گرمای ۵۰ درجه!
🔹
تاریکی و گرمای ۵۰ درجه‌ای به‌علت قطعی برق در حوزۀ دانشکده فنی دانشگاه شهید چمران اهواز باعث اختلال در نظم جلسه و ضایع شدن حق کنکوری‌ها شد.
🔹
به گفتۀ دانش‌آموزان کنکوری، قطعی برق موجب تاریکی و گرمای سالن شد که این امر به سروصدا و به‌هم‌ریختگی نظم سالن جلسه انجامید.
🔹
سوء‌مدیریت و عدم برنامه‌ریزی ادارۀ توزیع برق و دانشگاه شهید چمران اهواز منجر به ضایع شدن حق کنکوری‌ها شد؛ دانش‌آموزانی که پیش از این هم به‌علت غیرحضوری شدن اکثر روزهای سال تحصیلی اخیر در رقابت با سایر استان‌ها با چالش جدی مواجه بودند.
@KhuzestanFars
-
Link</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/457189" target="_blank">📅 13:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb2b16fd3.mp4?token=DY9NAZ_GHP-De6Sj0KH34YRbsSB8HIKjQ7N7qBn1jnKQTmhJNtBvQhYABUWknPwzxAt_X429C8PDmpXllXpomZWq5Yxfr1zj5Iwo7MHUn-buSn6VbpjEEeHamGziCQehQBZePLRWiBcJTKnkg7XVldWEI6UGp7qRLBZf12jdlnNNzkebh6sjijRfE1GoPF5NtqR0IvDIEGnHzODzkiT9vDuVnRwQ6B5TOhZzob6qH2vMS8DDcEGwdYzRl5RAgK1q9_2bDCmxzhZ0OJ9tizlM-JtG9JU360khmK7PeCQVd3GuIgDii9CYKvMNxos0txPqZfAiNxlBQIUEH7-8UKeXcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb2b16fd3.mp4?token=DY9NAZ_GHP-De6Sj0KH34YRbsSB8HIKjQ7N7qBn1jnKQTmhJNtBvQhYABUWknPwzxAt_X429C8PDmpXllXpomZWq5Yxfr1zj5Iwo7MHUn-buSn6VbpjEEeHamGziCQehQBZePLRWiBcJTKnkg7XVldWEI6UGp7qRLBZf12jdlnNNzkebh6sjijRfE1GoPF5NtqR0IvDIEGnHzODzkiT9vDuVnRwQ6B5TOhZzob6qH2vMS8DDcEGwdYzRl5RAgK1q9_2bDCmxzhZ0OJ9tizlM-JtG9JU360khmK7PeCQVd3GuIgDii9CYKvMNxos0txPqZfAiNxlBQIUEH7-8UKeXcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یابن الحسن آجرک الله
من واسۀ اشکات بمیرم
◾️
سیاه‌پوشی حرم رضوی در سوگ شهادت امام حسن عسکری (ع)
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/457188" target="_blank">📅 13:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457187">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpxnptoLqDDDfznJ5QROzEhFe-Gm_0oY9GVSfK2pexbdml-VzOp0oMZovhYv6UGCNn6zb7071J3DCeIS5BpBL4djRWbDVdAqtuEiWcnpoCPUo1MsV7Ui-KlCGRTzb-z4gAatDrT2vXlNdGj2fndbT0zEH-8xQqAy34Jq2XEo0rDITKaHQkg4k5lipLr-fHOTS-hTAQwWcX05sT9UKeUoYl_HkuaGp6YJPGcTYHQn-238xDA52A3FwIQawQ1V3XcPeikZ-9BN1uKFtb9r71HJnT5GMwqpu9bT-2U_N0Bc4sthhmquC5ULQ6LK5OZUHeTGToIXWRynmFz0dMoy_awzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/457187" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG-j8ox84LIkQstS5gNIfYJimlJ1xBDS1a087rNY6JOKVWT_2BNNZA9_Bu4JkraHPBAaJUZrpxb2xiD4yBidRxAmd9z4V30w-y2k5bz4oBHMiWaJAilGSwJRmxdhSQsPsu0YaoEQMPp34H0ah4Dqo11oVr54h3LLPtSvwYshsa5qzlVT-F0s2e2y9llVmAKODs2KtR1WPrrk4AVmGEMInppsok7ASCuDGVmWV8CFoL5J-i1OXO6sEO0nnZKRze9q1R5ak6RHBI8AhMvyjnIc6jf2DExhKZ8wId-Mutyu_W3Z2_RhRj3BsvSwhgcjrT4ccYYcuzVf6IIiJ2zQAYs1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_ZiOzmkXMy3gg6_kaEzwJTuIyLnjayzxi-_L6f3TXhpDeQE8YEIfxstQJY49mc1VTA9yDAeT8PAN2nVPITYZJOESurqWrLYU-bOAscamA71HqXBrDG1wytuD4nyGvMI7SccQK2BBgJVkJp9RSqMiomulo_RM-K_-8J7NDXpBwOXl68HS8jjwse_alij3N-ztPsK34NQb8fXnlcwGUVHI-min65Mw1qxQqsmnXLU99mP8iQcoD2ZGunFcjRmC8Br7ThD7CeOsYuYqRCrEMWNmtb_WYBKickQtslUYcFdTHm3nW0BAGKCDb9KCoNAfNpWRJCWQKVx3b2j7he7Vjaqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn3PCuBoWmGK1fXv3Buc71EHqf2ZRVIOrSd0iCWo0sqh35Uf8hU1PlqcQKnpcjLcqYRFdNE-Wd_49nErA1W0sLpxLurH7qKIVWxh4ei6Mii4chFq3o_MAZSiFvboTTYcwR48asYprXbThMaZqde7a36oDE4oDmA-nOIiBcGUjdz7VGn6Ahq_k83r282eUz1-t8H08jiS7gI_fnySMdBPJIwBRXdfABbdnTH489mviOEejOPi981WKVBLLCC29Bz_xOOAJ4rimeV0MSFmnHjKgAgHGHQFf9gO1KJKilwigFTk2hdQhJOwM7IsQuBGnKWY69QGpJ0UKuDcMGUWRaH_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0bkjyzq-KJxW_1E-emNILkefnvdfGeoghxI1YCFMMpxW-KvH91Yp9_-KlSVYxB0CYbzIfRLBffvIgv0Ht5dLXSEIFKQzShPIvod0Fp8AvBiu2MpP-NpqRR57Oq-KDrMYnBw2ujI9svyKDnFofwazWXfNcyLEcL-r8yPaDKXIWSWjiEFYVcV0mJaDf6C3tp9hYu9_dUeJ_s4-_qqrG2nTlY73m3faRR-zSxiUH3hhOYtK2ShuNpBGcN-g2HuawuzojBr-KKuzFo5iyplwTNAE77PlU0Cj3LNcCUJ2dUM5ulKyelAZsqJLxLy4NP1m4pYXuMQ-onE77406C7WOXtoQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: ایران و عراق دشمنان مشترکی دارند
🔹
رئیس مجلس در دیدار با نخست‌وزیر عراق: ملت ایران و عراق هم دارای اشتراکات جغرافیایی، تاریخی، دینی و مذهبی هستند و هم به عنوان دوستان و دشمنان مشترکی دارند.
🔹
ایران و عراق با نقش‌آفرینی منطقه‌ای در بین کشورهای اسلامی…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/457183" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=RrAD8-JPBVun9TOPHYcAvmIw7hWwiN5xWGrnyIjueyW4VGjMFzValjCd0OACzzxJBA5AzTLTPkOAeZ_7W3EsCi4Twn_K6viLRbQqBiHhueygFS-wP4-tngkzyIdsG5vv85o6rBTEM_ALMGk8sBtcuB9e3sR2xCw7HJIPQwN9v6e_nP22vHCvz8Yrw8XTqD1R_L6hNgeyD-iuh_S-asFJl5DY9mfYThVMJYWkgo9j4YPpi6PCd885qFW02G8_7TQQ3Sm2O93z973434D9EymMos7cvxABaLHJnHB5jyTVn6hOFTHuvh_tz2km5_H2JcSOY9FV-YmrxhFfgoR0LtKUDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=RrAD8-JPBVun9TOPHYcAvmIw7hWwiN5xWGrnyIjueyW4VGjMFzValjCd0OACzzxJBA5AzTLTPkOAeZ_7W3EsCi4Twn_K6viLRbQqBiHhueygFS-wP4-tngkzyIdsG5vv85o6rBTEM_ALMGk8sBtcuB9e3sR2xCw7HJIPQwN9v6e_nP22vHCvz8Yrw8XTqD1R_L6hNgeyD-iuh_S-asFJl5DY9mfYThVMJYWkgo9j4YPpi6PCd885qFW02G8_7TQQ3Sm2O93z973434D9EymMos7cvxABaLHJnHB5jyTVn6hOFTHuvh_tz2km5_H2JcSOY9FV-YmrxhFfgoR0LtKUDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردبیر پیشین نشریۀ خلیج‌تایمز: کشورهای منطقۀ خلیج فارس از ترس موشک‌ها و پهپادها، به تعامل با ایران روی آورده‌اند!
@Farsna</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/457182" target="_blank">📅 12:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JupuXNwozvWA-U_DrkQ4ByvfXspJbeYmH1RqPDM2JBcGTZvJOPXDtJKXA58Wa90sXp9fCQP956OlZrgaU2NMY6IVNOsiSm6F8cnHIzcsNPQoIexDXh7KZ7ijfTTEOwcS5-nWt0U4mlbRlouYZRPYAYqqqQbxW0oMVNaQrZAWrKtr5Yq9q2kxgc0_Sj_s7TQ0w-AonffJy0IeZBjTzvhSwpNuG_8UfTxWZDCc-tH4w8XggcIVbFpMGufx3eX92d2VKZPP8CfnAFlU8HkAK-vAQnYy4PA5mRwYJOE1fKvty3_wTPauSJZ6nQvzw3vKKW2KsH_xQGjAFvcWZGoegw0ZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در راستای اجرای سیاست‌های کلان شستا و تاپیکو؛
💥
پنجمین محموله متانول فن‌آوران در رینگ بین‌الملل بورس انرژی فروخته شد
🔶
در راستای اجرای سیاست‌های کلان شستا و تاپیکو، پنجمین محموله متانول شرکت پتروشیمی فن‌آوران در رینگ بین‌الملل بورس انرژی با رقابت به فروش رسید.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/457181" target="_blank">📅 12:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨
✨
شهرآسا؛ جایی که هر تراکنش، یک فرصت تازه می‌سازه…
اگر صاحب کسب‌وکار هستید، وقتش رسیده از تراکنش‌های روزانه‌تون بیشتر از همیشه بهره ببرید.
✨
با استفاده از خدمات آسان پرداخت و اتصال پایانه های فروشگاهی و یا درگاه های پرداخت اینترنتی به حساب بانک شهر، وارد دنیایی از مزایای ویژه «شهرآسا» شوید:
💳
تسهیلات ویژه با نرخ‌های متنوع و اقساط بلند مدت
🎁
جوایز نقدی، هدایای ارزشمند و تجهیزات جانبی ویژه اصناف
📈
امکان بهره‌مندی از تسهیلات برای پذیرندگان آسان‌پرداخت با میانگین یک‌ماهه و سایر پذیرندگان با میانگین سه‌ماهه تا ۷ برابر میانگین حساب و سقف ۱۰۰ میلیارد ریال تسهیلات
🏆
تقدیر از پذیرندگان برتر
✨
و هیجان‌انگیزتر از همه…
هر ماه با هر ۱۰ میلیون ریال تراکنش، یک امتیاز دریافت کنید و شانس خود را برای برنده شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
💫
شهرآسا؛ فرصتی برای رشد کسب‌وکار، دریافت تسهیلات و کسب امتیاز، با هر تراکنش.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/457180" target="_blank">📅 12:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/457179" target="_blank">📅 12:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krkFfkuLDpM2vfZtVuNBXPn2d-pm8Y-teJ-okxs23KKQI0mNrsDzq2mZzW9S1LIW7fiTnnonxlp6Ig1JTMVvFf-hBEg9j7qI7ljENncZRctkMxv_Xr0xfaCtr62qK9TJ0k9BEvj6fcXp2z_dEkdyYt4TBJVOITY6kZmSzlvvQlfxhR6SrKf4UoYOXtHQmE3DV8x-NJr-A4k_kErZUgpcU4ZmAWudyZKoi_NhBL2XPZGbR0J0-aUh4McZc_rs9o9CtpU5lJTZPZ30IEwcSBCyWFS_ht81t0yHqk2piWZqEY9d948kP5Xfp3ZPTGPLbkq_jis_XMvG8rlFvexlLd2hjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اهدای دست‌نوشتۀ سردار موسوی به خانواده‌ای با ۱۱ شهید
🔹
دست‌نوشتۀ فرمانده نیروی هوافضای سپاه، به خانوادۀ اسدزاده بخشایش که ۱۱ نفر از اعضای آن در جنگ تحمیلی رمضان(۴۰ روزه) به شهادت رسیده‌اند، اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/457178" target="_blank">📅 11:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgASHl-1huyjSODFd1ix1DQ971VPnIFIqGmaj2nDGjMLkyeRESGxHXxIn88scHnorMpWTDpGL9Xwt82OtY_92TompQEpsQS0EmJuEwq46ChonoyTHmNQfP0X171jD5GwFxBhSltipMey94FURQBkJ-GA4WfSa8VbmCGq58SzKtvF5ZtVFLUHFIg6rE2wIz7AXzmaOL-7w8EedKhrq7xoL3E3d3a-K1DoLzYXz7pw3jrADTTlyBdh6K1h0gcjQw5dSvVBrk8vcJCjwi9MpUrtmdb4QxuI-7ZBQbq2mVlPu8-xBFScBnprnxAdoobJek11JbwjzOHYmODF4JxyqW5uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXuFsxJkG0fXbZGg2I0vIq95lRDvjjtsK5PN6rLZf3ywKxSzaz2sbg7pLTFWDjkIMBXvlaIsW81C3AqPWMDKjff8Fh4_7uXuDKdkNz58kCBPwNGPd44B3G4911eSxVUduxblclv0YjDHuX_rqhXrFJ7I0bI5YMEdbAunuwCEu1ZDEt9ajm-hJfcKP50VqS3L6mwAjRzITTGMcBpEA6nDjR9ozQ7OJ6I1RmWJCSsoGpDgS0rWgC6ptrtfRprGm70HjYDQGSctKByW45APX5p12lembLjp1t9kFG4C1bKmN5CrWywBFnpwz5MOQSKjUpkcitmZFxhUmmKn0yqsIJ7D8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M38bEtqoxDGmOI9nqJt7p50QbETcX-vY_ZSbkXpWD6iPIdisRhemFPNz4QbjxyVYMAZjo6cubhGxFQ6dV9HF4p_WpNA4qQm8088aoPeJ9QYCl7HBv2fQkcNcyB1bvD9yPBOgptnZdO2axlHT1n2pWtpZjQiBh-zBSAM6jIApqsK11zr7SUPQqof8HsOUpC0MbcM7Q5mZq41b2h84ngpqX1HaLeKpKKSbT3H-aMl-YQERu--4ejn1PcHaJsGpR0N6HBT4GQnB2LcvRkLfCsQukZfdICmrA2s21lr21Pr2-2sdugPwDOgDzMQIeWRCLvgrX-0R0aqud-BBpAKRjiPgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0qo29VqEz1poGbg8_bxuI7mnVn0PZ7uHUpuy4h-vPiMlOp4-xwTbtSKNusLKqw9ptvGgPTO5u-TyzLT4qPuNK_o-thnEENN46h2pRJPkjlmIAaLbC6aOY4FrEtpGAVqYyj9VKjjsrpT-ItZDHyLM1wX0Yy3NVdh7J2w2zRMb1XbTOjlhsIVBvsWKxFP4_QDkf85xv-MsHsYvZXzX34tRVuv21-A_WJEEYoArYUQDWpxuAmLHQgM2ZecmyRbC4fIklzR0iogdK7OCp0cfADINMWIM_UV8J2J_uyBOImGqQ6lHnRcspLWVpmFYMBYbYydLiTWbAbPT47gP0A68YCvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHDeMe4mHv6rL2hCiHAr28O3NUkx_2Fo6jAWXw4XNCFRkjxdCDoDOHTH4GmS5ICb-9sJ53u4CnbGTVpj5wnh002PgCQ_sejr1MGuGPNREfCX2stWg-sPHR-870_CdsHE6zTHi06Hpuba8c2xpoh4hNriZZBAyjE4RTH-IXGerZBG36g-jYs-DkHuAz8VttOI_81a4DJfo2E3YloZYRSK1zWdKGgZhhGVHl3kYAqDVtHRDCrKZQB9NiuS_X1LBX9jM86F3Zad0PGMTkSxjUS5yn4rvSuFa_arm78gJcWZhl-UdVMJNyLcO0q8N-UbVXLrSFuMD_AvG3JS3PI4g7bfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCZteIDMj4w-w5IRdCdI-wPzvnr1pOG1bSQhAEtneSw2sQgRD-ckSBoHXgsiaxSYZNHhndhcWq2OvnTga3KFnXW_errUxl1MSA1aRKUxwcI6lyOtvXaCJZjbr6bCWBau4C9jc9XTG2eSfH5vD8LBJwH1FMbaXOf-ioXmiS6fxf_VmmNoJJCb3fXbZ2MZuXK1-01V9EaSf8FwEWJGcM7VU5g-ViovEX_9rKBT-x2BYFa0xISo7Q1MxCIAm8nfha8w1bgSuhTBwt6SuWePeCY0yQjhCKzOcvWWjX-4l28SoEV24PHY24pJJwb6x-I6vMfzU0nk5bNKT2Dr60JjRmHmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfROrwGW3cLZjdYYkshjKdWhoP1f9QfBOrTrWOjtW5JVXM8MDSk4c3F4CJXcSTLht5fCwTeXeKCUWlnFzW6g30ICBp1l2MpDL3aq46wQ33DUTtmMHG8z0OVHFIE6lnK0XygNBuJncbCpRLW1jIxN6ll3TjmIoeALxgueYyiWZQnP3ujLSoWP3Qs_ICrmZMEVg5omF61qpEuHgm95mwe8fXTQ4rUPR3cRNDb6aEtddjuqg3d591D45o85h4lD63URsUiXLGGHmAo_Rbm5rQrnwYSg0RzNRIgrzhaz0fXLcQG8WvElmhvQB3dTbMiTGz1ueCinS5STdQJGu5Bj0eLPOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وزیر علوم: بزرگ‌سال‌ترین داوطلب کنکور ۸۵ سال و جوان‌ترین‌ ۱۲ سال سن دارند.  @Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/457171" target="_blank">📅 11:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f312278eb.mp4?token=ON77ZD9kevPwl7Ie3TktU2X79kAVKHSiuLwJLHkuRYbKltETIW88u2fj0o47QU79BKYWf5AxyopKbojsw9QuEVuKKOGUKsIvMFBMYxH3Y5L__vq7ifTfLEmQbjUsLjslgwtXnT0yiho3SWMlCfufyPlKHa99-b8Q_QW4QHAHTca0-Tsw5cE7Q2ZAfZCQ8XcSi95iPkhpqq6777vROwhaMcQkJHonhZGFQMgRwvOjfW8fRA-4mfuNOpZLVLMbC4Cb0BKU5fWQamhMNcDkQGh9o1tYZYtxdmlws_u3PblSPwgh6OVYYlRRgKL74N6kFQLdFOERBq9BJR3YILHtGQhbqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f312278eb.mp4?token=ON77ZD9kevPwl7Ie3TktU2X79kAVKHSiuLwJLHkuRYbKltETIW88u2fj0o47QU79BKYWf5AxyopKbojsw9QuEVuKKOGUKsIvMFBMYxH3Y5L__vq7ifTfLEmQbjUsLjslgwtXnT0yiho3SWMlCfufyPlKHa99-b8Q_QW4QHAHTca0-Tsw5cE7Q2ZAfZCQ8XcSi95iPkhpqq6777vROwhaMcQkJHonhZGFQMgRwvOjfW8fRA-4mfuNOpZLVLMbC4Cb0BKU5fWQamhMNcDkQGh9o1tYZYtxdmlws_u3PblSPwgh6OVYYlRRgKL74N6kFQLdFOERBq9BJR3YILHtGQhbqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دود حوالی پالایشگاه تهران چه بود؟
🔹
روابط عمومی پالایشگاه نفت تهران: دو تانکر حمل و بارگیری فرآورده‌های نفتی صبح امروز در محوطه بارگیری پالایشگاه نفت تهران دچار حریق شدند که با حضور نیروهای آتش‌نشانی، آتش‌سوزی به‌طور کامل مهار شد.
🔹
تانکرهای حادثه‌دیده مربوط به حمل نفت سفید بودند و حریق در محل بارگیری رخ داده است. نیروهای آتش‌نشانی در محل حضور یافته و عملیات اطفای حریق را به‌طور کامل انجام دادند.
🔹
در این حادثه، واحدهای عملیاتی پالایشگاه نفت تهران آسیبی ندیده‌اند و فعالیت این واحدها بدون مشکل ادامه دارد. همچنین این حریق خللی در روند تولید پالایشگاه ایجاد نکرده است.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/457170" target="_blank">📅 11:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbmlP3pU_GDTs8Al-Ak7H1oT24IcnHgNoOdh1Q6xClIqCoowVnair4fJPpAgMHcLlhYVtx8DsBoRrjtn71UQL64FVivcL0gFJS4fFhku7xmWyJ8bfVIbWhXgHAgb_OxqPvfAl_vBRLanq8OP5bpbmlNc66G4gMlK-14e7KNImSrNSCBvOE5YOZZJB4mR9D7S7XRdJ3m1PrynrgqB5AQu6SXISSZgA9jopXR8CJ85VvBauLvK3eos4U8OW_1TZfZ3GfObyXGl00el0NNf5o1tJp0et4uSqeYgagB0Dr-YogrSG0eU5FBDsQc2A_o0sjpJ6HQgZO0CYeyYShWpKTg4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به مقامات آمریکایی: اصرار بر ادامهٔ سیاست‌های شکست‌خورده، تنها شکست‌های بیشتری به بار خواهد آورد
🔹
تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی آمریکا از بحران‌های مالی داخلی است: یعنی بدهی‌های بی‌سابقه و افزایش…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/457169" target="_blank">📅 11:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsM-QQeHDMFbHWFhIGdQnb6FBKp2rbNbaWoaLdn1aspwRydDbgzFRCt984B1OlCAQwuJ9u1SDNcTSAqQ5C-UZcLC90Qz-yDEIC-O8R5BSU8ch-_TNbt62Y2CKYHY7HjlpAUE8q6SSnYr-Mds88_VLkN1Yat02AAH4viRAxG5hjdbOLZokOHhnk9Gyel8hLCVbD1tD_G7m3GAT4IAbs8BJ0Y9PKzLEEb-f_uNji2BdvHDF2B1gnnEe496x6c_OGtmdm7jdr-ptL7zV4gk1JnHEmjckZSEVsP0upx2p_EbCByUd4k2XcxDLUOiei9NU4HjsGW7lDYyUEVPAdyiMToBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترس از ایران، بازی اسرائیل در عربستان را لغو
کرد
🔹
«جام ملت‌های ورزش‌های الکترونیکی به‌دلیل ناامنی در منطقه به‌تعویق افتاد»؛ این بیانیۀ سازمان Esports Foundation از لغو مسابقات به میزبانی عربستان است.
🔹
اسرائیل در این مسابقات برای اولین‌بار در تاریخ می‌خواست یک تیم ورزشی را به ریاض عازم کند.
🔹
سایت Al-Monitor صراحتاً جنگ ایران را عامل ضربه به پروژۀ بازی‌های الکترونیکی عربستان دانست و تعویق ENC را در همین چارچوب تحلیل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/457168" target="_blank">📅 11:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=SKMLxpgIEWD_JcUBqPHfWrT8tNRlN8VgWqfzed3M85CbyZ8wiV_sflq4A9yP-k8MAP_PEVtBfgruHGMqj14Qqekpy9TRu7EQqdv2XVk4mQA51B4qwu6pEBv2AtmZp3_eMjRGCtXBxHsFDO-EAqu-zi7O8D_ErmOwJ27018tGWoFf_7Zn2V7yahAxRoyAlJxkCoM71UoUiRkwynh6wej8nBd0cgs5S_FclghVKLktg83h9NeouHBttNlAJXj_NpCz3D85J1_TNKILoYneVTcxjnYeOfNMrAxOLJJdWGsq3pQTe2Iko_LkDTDvvrk_xDQKwaazD5_BGg85aIoYU_hi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=SKMLxpgIEWD_JcUBqPHfWrT8tNRlN8VgWqfzed3M85CbyZ8wiV_sflq4A9yP-k8MAP_PEVtBfgruHGMqj14Qqekpy9TRu7EQqdv2XVk4mQA51B4qwu6pEBv2AtmZp3_eMjRGCtXBxHsFDO-EAqu-zi7O8D_ErmOwJ27018tGWoFf_7Zn2V7yahAxRoyAlJxkCoM71UoUiRkwynh6wej8nBd0cgs5S_FclghVKLktg83h9NeouHBttNlAJXj_NpCz3D85J1_TNKILoYneVTcxjnYeOfNMrAxOLJJdWGsq3pQTe2Iko_LkDTDvvrk_xDQKwaazD5_BGg85aIoYU_hi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزهٔ مقاومت: اهمیت اصلی علی‌الطاهر لبنان، علاوه‌بر موقعیت جغرافیایی، به تأسیسات استراتژیک آن برمی‌گردد
🔹
در میدان نظامی درگیری‌ها لحظه‌ای ادامه دارد و حزب‌الله همچنان با تمام توان درحال مقابله با دشمن صهیونیستی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/457167" target="_blank">📅 10:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گلستان - خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o26xtEgv8007l0llC8LIAsHQxUfqCnM4ZLzMS5ug9G2VMVgmNAeOz17WXhD7YxriVSd6-IaoNgqBB6KV3Uh8akM_H0orllxt4hBK8iTk37a8E75m-TPg5AbLUqlqMLAM1R6G-OD4em4W5w-re1K-BkAo-Z_EInb1bVBupRIvICVO3clUuMMes-vQtvnXNiTgUM0UB6MUXfW0TwjJ7mdzjz8pGw8YZGEUJ6VUoq9A76o-hcFBDamMS3Mv7RNevmT6Uv4pSCjY03cMAgNKo5_1VucU7E-I9GicFmZuhRU5S1XTEZMu8U38cHVIyWx30APJGtrjYSsAgsN2mrHBdtoNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رمضان مشت آمریکا را در حوزه نظامی باز کرد
🔹
سردار حسینی، فرمانده سپاه نینوا استان گلستان: آنچه این جنگ آشکار کرد، این بود که ادعاهای آمریکا درباره قدرت نظامی خود دیگر مانند گذشته نیست و آنچه باید از قدرت نظامی این کشور می‌دیدیم، در منطقه عیان شد.
🔹
آمریکایی‌ها در برابر مقاومت ملت‌ها و گروه‌های مقاومت نتوانستند به اهداف خود دست پیدا کنند و امروز تلاش می‌کنند از باتلاقی که خود ساخته‌اند خارج شوند.
🔹
آمریکایی‌ها همواره می‌گفتند گزینه‌های مختلف روی میز است و یکی از این گزینه‌ها نیز گزینه نظامی بود، اما امروز دیگر مشت آمریکا در حوزه نظامی باز شده و قدرت واقعی آن برای جهانیان عیان شده است.
🔹
این قدرت نظامی در برابر گروه‌های مقاومت نیز نتوانست دوام بیاورد و ادعاهای مطرح‌شده درباره توانمندی آمریکا با واقعیت میدان فاصله دارد.
@Golestan_Fars</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/457166" target="_blank">📅 10:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g62eOgKOa5B2yYaocBLWBUb7ntzvu2mxeAEyYXiKYUw7qBDEdDO89GjnS9vtHgZAOBbEDpp4cu42AuZZQhenkVw_h8BpoA6DJzumiHxloiTM0FCI1qvgtAl6RxYYW1yIAf65lAm3MQt8JqfhWw_0OIeSKYrLtgTxgN4ZaOwHA3VXvmpBXyhmv0VMvLlCfn6CeDO7LF7GoNKuVnYjQd0q1xCqsr-7Mg2hV0uSM1RBL4KVspo3cpsTTwlbRvWsfcQ84khg0fhtM0Ed2zz4o1XL1p3h0r6RYClYwZ0Ou6SKHQMGHz1eSUoOarD_x-1C5UXi0FOMpjgoVT1VwENoALiiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: با وقوع جنگ جدید، تسلیحات مخرب‌تری به‌کار می‌گیریم
🔹
سردار محبی: قدرت تخریب سر‌های جنگی به‌کاررفته در موشک‌های سپاه بسیار فراتر از نمونه‌های استفاده‌شده در جنگ‌های پیشین است و اگر جنگی آغاز شود، تسلیحات ما در تمامی ابعاد با گذشته کاملاً متفاوت خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/457165" target="_blank">📅 10:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee294b7936.mp4?token=moTlOlcJ0r9FQhtf8pWH-h31wWNI1AY1ANgc9sB1_rJXDuwVx9-h3f2BT-Dvvyf1LxLhWtwK5PXMW6P_m5wb_m5VzwGF1c_aXMlQC4X-8Smqle1v2oeB8Xc1YvkyBV9k-Vyo5L1RinTNpHCJW8h3AD2Z2UjBz4niI2SURMfUJezHAgerUma1lFboPkhT8jjuFHfmpNyx0D3qkt1y_6eMo0uLLp49mY3-Vuy-JB60yS2W5MuEco0xJjHFHjM19XUYsaGsXzU_gACSbNWRim28Vopp5SJp4NQMVNH4xnSS_Tou7ZprV1tys175EFXzwQImfCAPTq_MrvvyKEU-eMPWGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee294b7936.mp4?token=moTlOlcJ0r9FQhtf8pWH-h31wWNI1AY1ANgc9sB1_rJXDuwVx9-h3f2BT-Dvvyf1LxLhWtwK5PXMW6P_m5wb_m5VzwGF1c_aXMlQC4X-8Smqle1v2oeB8Xc1YvkyBV9k-Vyo5L1RinTNpHCJW8h3AD2Z2UjBz4niI2SURMfUJezHAgerUma1lFboPkhT8jjuFHfmpNyx0D3qkt1y_6eMo0uLLp49mY3-Vuy-JB60yS2W5MuEco0xJjHFHjM19XUYsaGsXzU_gACSbNWRim28Vopp5SJp4NQMVNH4xnSS_Tou7ZprV1tys175EFXzwQImfCAPTq_MrvvyKEU-eMPWGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت با آرمان‌های رهبر شهید و طنین صدای مرگ بر آمریکای زائران در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/457164" target="_blank">📅 10:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwu3rUhepzaqSVmr6XmyIhiJMn8ir5ujarTn4XglMO12kI68SduAqdX7J9r-8H6uVjp5_7AEcP5cGbtIjY7x3_JzPw5zRxW7O5rhZ13Pk77CUfsJxQOJNL6rJ54QSOvamlqced4XYK9wXG8XlGqpffRCjF685OfRS36zAJbvUnciuKVflPjjxrbA9QQVynDHqLFkAWq6DCSPwin5q_jsNKKaUeotZV5afqM9y6B7vHwklmGFa3nudrTU6RodXSXrLPcWc6Nwl7BMmKD-V1uI-TKimxt5vhhOQALjYr3ej1ICfKJcKV-GqAY8-75lRBVoHtdJ-xxx4QvjEgjgU275wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/457163" target="_blank">📅 10:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134c5c9f7f.mp4?token=u6tmaQmKMIrZJtMiDoTsKmCR6BTXpOrwb8eW523qTyFzAsIjConakTlGHB_tXc7acSaeeBX563C2P_cjboBFBdd7DUPBtNF3KDAmDhn3dsIQA8Dqhgdacw6FaBKFvz3X7FHJ1U_rt97YOQf1rdshWDicnvYfUPtNQp-H0dYSTwfdTfQ8dSaoZ_I7Mz5U_wT1fSmiuPXXuC6laywfXIY031d1rkh3VF7Asoa_E0QUZYB_uf5d1Hvr5w-NTzptti-WXq9epeVn2vgqtkTFjHYFc5s37o4DsThN-_TJE_5qZy9kat83RFsrYwL8ODt7aYh4cUpZZWfApybEbd-LwOja_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134c5c9f7f.mp4?token=u6tmaQmKMIrZJtMiDoTsKmCR6BTXpOrwb8eW523qTyFzAsIjConakTlGHB_tXc7acSaeeBX563C2P_cjboBFBdd7DUPBtNF3KDAmDhn3dsIQA8Dqhgdacw6FaBKFvz3X7FHJ1U_rt97YOQf1rdshWDicnvYfUPtNQp-H0dYSTwfdTfQ8dSaoZ_I7Mz5U_wT1fSmiuPXXuC6laywfXIY031d1rkh3VF7Asoa_E0QUZYB_uf5d1Hvr5w-NTzptti-WXq9epeVn2vgqtkTFjHYFc5s37o4DsThN-_TJE_5qZy9kat83RFsrYwL8ODt7aYh4cUpZZWfApybEbd-LwOja_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو اتاق مشترک بازرگانی ایران و روسیه: توسعۀ همکاری با روس‌اتم، می‌تواند ایران را از خریدار فناوری به سازندۀ نیروگاه هسته‌ای تبدیل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/457162" target="_blank">📅 10:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457161">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان یزد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860a438708.mp4?token=L7T3s-0NGoRXtIPxpXCptjnLG40NnyhXH7uQOFiWpcsWWdTVdVfDaCioap1VfrikjcI52_Egj-oaAWvsjIICt-SBBBVRqQAyMuhzuTM8YwztPbVFhhHVs3fYPiGLyHeTQsKigx583dTnW2ObF-pnyjkFeMj6ZmO1B7DjL7VQrgCWhdO3q8SxSLPWXwei-tG6Tb4UKHwKKE9-JqiDNO-UVX8w77tMfr-z8yHitVTNd9-XxTyDj81CyIBHODVuZzwXxRVphwMbEJH9RQfZhJFCga3o_9xJThKTVeFoBQW1yiT2l3MYER3irI9PFBJXypK88jNxLzNacCx6HKaHeAetqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860a438708.mp4?token=L7T3s-0NGoRXtIPxpXCptjnLG40NnyhXH7uQOFiWpcsWWdTVdVfDaCioap1VfrikjcI52_Egj-oaAWvsjIICt-SBBBVRqQAyMuhzuTM8YwztPbVFhhHVs3fYPiGLyHeTQsKigx583dTnW2ObF-pnyjkFeMj6ZmO1B7DjL7VQrgCWhdO3q8SxSLPWXwei-tG6Tb4UKHwKKE9-JqiDNO-UVX8w77tMfr-z8yHitVTNd9-XxTyDj81CyIBHODVuZzwXxRVphwMbEJH9RQfZhJFCga3o_9xJThKTVeFoBQW1yiT2l3MYER3irI9PFBJXypK88jNxLzNacCx6HKaHeAetqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرغ آتش میهمان یزدی‌ها شد
🔹
فلامینگو [مرغ آتش] یکی از پرندگان شاخص تالابی و جلوه‌ای زیبا از تنوع زیستی ایران است که حضور آن در زیستگاه‌های آبی یزد، اهمیت این مناطق را برای حفاظت از پرندگان مهاجر نشان می‌دهد.
@YazdFars
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/457161" target="_blank">📅 09:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457160">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCjz96y3gjtwB7b4_2FE9nxE27msZwqRFTO3npeFAERFFoVNUeOWBA59E3XC8vFvWjsazwJ_uNrRhbwNj6FqfLiIVkWOsRjHyDyWsnpb8V8f3L-f75KhSzzJOrlBDz9wOx4zYKIEumen5QIZqRwiZ-vRaouhInpl5O3ckFWLd-QulW4kzULep3L-ChbtY2P3vBy1ML45JNJ98H-fWaVQjco8AYs3ScyJ8pBy7H9cEUzD56_V8NZ9ns7KgZgv_zYA7weSiXyObLS1S9OaH9qWsPo0kugO_XfequfOk7QlPsYOjXehNSLb5emC3Nm8AQOxZ9RA6nr2j6webbF7q4yHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/457160" target="_blank">📅 09:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457159">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnp1byYvlvDuVhu6SHUCPhmWcukUxlOc6e0ZRclCniwpm5KuAKjldr6BrBCiGX-Q8GiWm5qVJ7WbNLoEqqi5Ok-Ac47lLaYB7BooM3aCT-IeOWBDZppWzwkwnfai6j6kO0ZA1U99nhb8ani6-OrXmdp-_b3BMsFGV44ziFQhtoGb0BFpx03rQranoKXPxUbp54OPKabvs1QrXMbaFATvTIlVB1nb4Nvb5dJaZHMDKPepswlmLqK4SHKDMmIOF7k1SPOadmYEVWwOGmNirdggtnNLg4U97NRdUTQGYuAbnu7sOQs_-tHbt_3c7HltYZrmA429P77aNONUcnCj0yW-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اعدامیان میدان علیخانی اصفهان از جنایت‌هایشان گفتند  @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/457159" target="_blank">📅 09:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457158">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da020506f1.mp4?token=PPQbvLcFuJq_icTRpV-sS17unPNtIuP1ykkhBFhs2sPp-J--FtKu-Y5BUn3FeshqbQrYFGMwMUhs37LwdtlYcG5WzFPqIeXZpcSKqSFb3h-2Fs-3mGx3GVyQ_bK2onsFLlBM7pZ09zie64hzK3EVX66w7FBm7srhMI_T1r3R_evT1j_ev1oBd2Se6j3jMP3xu2wrUcqcv5CE1CoI7RRQbktJu_qxq3scE4-LT4eQfXOpYAp0E0IhgAf6MCeuHvMetVLk1qF6_XC2Yv0wsDJqT0UgaBvXrWJPNiIusQQNXlCem34EfAvoQR4ZQtQ4OrvVrIvf43hPljMyZB-QcH4_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da020506f1.mp4?token=PPQbvLcFuJq_icTRpV-sS17unPNtIuP1ykkhBFhs2sPp-J--FtKu-Y5BUn3FeshqbQrYFGMwMUhs37LwdtlYcG5WzFPqIeXZpcSKqSFb3h-2Fs-3mGx3GVyQ_bK2onsFLlBM7pZ09zie64hzK3EVX66w7FBm7srhMI_T1r3R_evT1j_ev1oBd2Se6j3jMP3xu2wrUcqcv5CE1CoI7RRQbktJu_qxq3scE4-LT4eQfXOpYAp0E0IhgAf6MCeuHvMetVLk1qF6_XC2Yv0wsDJqT0UgaBvXrWJPNiIusQQNXlCem34EfAvoQR4ZQtQ4OrvVrIvf43hPljMyZB-QcH4_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/457158" target="_blank">📅 09:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457157">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc67442d1e.mp4?token=MBcpxnJvVGHCQsgLeLmLCpSgaAknsmKmgkBekCVNp4KC2CvD5a8hNBH_cZ94u3ZABvN-HvYy8Xh7m6fi32TRpvDLnzMmWlXeVABbhlgZV8z5rTRGDWhaniUcSb6hZplUk6UxWLa-PBDWnpfqI-6Abr5Dw03g50sHUQHOJH9oNBtr2xVrRmpcvU-E-lO62vn8QqEfzzYgDLqMsQljlQFyHr5_E1fLZXvAOxlDhLqqy06fNHjAcpYz4FZflLqV-Zr--ECgsncylD1mHUqNW7PzShxoqYQXVGmuxDdymnQXy9q3-qFQNh-XVB15YEN_vnDm6XKOIVwfXsv0H8AMVSEvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc67442d1e.mp4?token=MBcpxnJvVGHCQsgLeLmLCpSgaAknsmKmgkBekCVNp4KC2CvD5a8hNBH_cZ94u3ZABvN-HvYy8Xh7m6fi32TRpvDLnzMmWlXeVABbhlgZV8z5rTRGDWhaniUcSb6hZplUk6UxWLa-PBDWnpfqI-6Abr5Dw03g50sHUQHOJH9oNBtr2xVrRmpcvU-E-lO62vn8QqEfzzYgDLqMsQljlQFyHr5_E1fLZXvAOxlDhLqqy06fNHjAcpYz4FZflLqV-Zr--ECgsncylD1mHUqNW7PzShxoqYQXVGmuxDdymnQXy9q3-qFQNh-XVB15YEN_vnDm6XKOIVwfXsv0H8AMVSEvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران در شمال کشور
🔹
هواشناسی: در ۳ روز آینده دما در شمال و شرق کشور ۵ درجه کاهش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/457157" target="_blank">📅 08:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457156">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqLtkRJrOOg-nIB5Kp4X5sCYQXkS2mCvZOQXJD11vZr85UULCc1y36wl33BNz3R9Tyr7w8II12pO1Riy8p3ULrEBK1fSRzTbqO2FbDolU7p6X_DU2cZlKwvV9BUX7nCBoU4hYe-MIBU7cVZJ-FtElzQ9mwJlDyyVHufEzLJsnJ41YgdOCG01Mn6UD8_LBGmskPgXAUuD_ZY6sYNuBrMqZia_WQjhcrAQx6natSVoHZX4vEtLld38YWXbxlck6VmeAG2LzQmzAsKX3dBdP2Om4JG4kxt9KGK4MGL9ex9C8fQWP1W94w3uSLqmDzNSYS5TXHVo8wKNj2EikWTpPyBMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/457156" target="_blank">📅 08:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66cdb8a28.mp4?token=KCmQgvpTVVTjzLjqWL7wBDtZy1Rm-p9lRgziOWmMrnidNgBQS61GyGDb0WiPMORaGA1IwXkA7pkE_ZJawQAM2BNAVrbIHeM82U2Btd390OaQf3td_o-rwNGdQA-Vkq0n6uyE-LKz_XLZIc1uShZ5Jg--4MK52o5YYX158iEFJw44plTeRVuHdwdCS9Z2vVADoBjmMN7Da3xKM3EjgW72aoT5KyjzONdpLKmZzU2GoLA20NOahiBpJpv5OKUc9wbwTZkY7WS6jvTMRgykcwwuefSgzwh61h0e7j_mr0B7OfykkVQAiRODOj0XgxOhjYJgcofBRGydLflmZ0F75R1v9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66cdb8a28.mp4?token=KCmQgvpTVVTjzLjqWL7wBDtZy1Rm-p9lRgziOWmMrnidNgBQS61GyGDb0WiPMORaGA1IwXkA7pkE_ZJawQAM2BNAVrbIHeM82U2Btd390OaQf3td_o-rwNGdQA-Vkq0n6uyE-LKz_XLZIc1uShZ5Jg--4MK52o5YYX158iEFJw44plTeRVuHdwdCS9Z2vVADoBjmMN7Da3xKM3EjgW72aoT5KyjzONdpLKmZzU2GoLA20NOahiBpJpv5OKUc9wbwTZkY7WS6jvTMRgykcwwuefSgzwh61h0e7j_mr0B7OfykkVQAiRODOj0XgxOhjYJgcofBRGydLflmZ0F75R1v9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آغاز کنکور ۱۴۰۵
🔹
آزمون تجربی صبح امروز، هنر و زبان‌های خارجی بعدازظهر امروز و ریاضی، فنی و انسانی صبح فردا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/457155" target="_blank">📅 08:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
رئیس سنجش: نتایج اولیۀ کنکور شهریور و نهایی نیمۀ دوم آبان اعلام می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/457154" target="_blank">📅 07:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دریای مازندران تا شنبه تعطیل شد
🔹
مدیریت بحران استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، شنا و تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را از عصر پنج‌شنبه امروز تا صبح شنبه ۳۱ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/457153" target="_blank">📅 07:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457147">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWe5RPVQdL9Gsek9mC7Er8_xS0NKiPPifXQahsfcJ4pXyUqniJNsyc8bVGJ_8pq89jHNZaIJEft929SeLUf_epn6Mp2l6CoCOBVf3qENYKlmVKxbJi_Zel8UE_9ZU0UMHaarf2tKAF4Kn7gMB5wV8yaF5xMCMXtIOr4-IAXZBBHpFH1e3pKC58eowCn90WpeT43RbebQzMgJ1u3o5tnxJCLuxGwpQ0jLxx8jeTzIgGww9DmWa3hwR-7bRsjsoyfO1jeZQgAGiMOync1Yn--7lI4YgozqiyI8grsKH1awFCcSDt-INFKzoGzr6v4quThAXJDruz-fedPrL9a8DhIulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZRjGHliU3NFuhJdS5-fEfLezMqGbv-7R32a8mulBRbpfsZwmc-oR612Rf2j1d9KvALvZs9lqWLsi_bqQPHd643RrFO6EWLCsIRedvWa6YT_k7m1my2jDb8uxvdvyOrloT6yl21e4Lhga8Cve9_Xw2oymyK0HlE9OlH3CVEAWpklSRvMk-X7SLouBwdZwUPYQPWPYzdTK1G82qCA1mWUjvEOGDBoqOm48dIL7ko9HlWSspGrUHpSjIFJhbTJxmM9k2SHCMFLZ-cRjOMLyOfIL4pzTbc4HuzrFXECy8ciy1HePu-6Hyz_0qpqyGGJg4SZ-S7Bg9QODKoqmlzrXns47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_gpDsLEhwAl6-vyrCOjYWg7boZkTLqpfbGa5ZpcQ3xheeySc5G37NBrQyYjcRoVeu9vVALYwkjwfruBPfl5Is_sUxgcsnEGRrohPKIg-bbhwVXgfFBVgmM8SRHZ2bUeCuTdK56o1QWxmKvsGfBOjKbPCidCGIiZbb4z0Ny5fwfixI9o2ulJghfE8BvNaDbvGIh-1gXSlGbdWB7yFswemkbOv4CWt7pwJFoW67i4Ski_6yLiE4W-f3zuDoPaK50572jrsMW9uYGF8YtJvSLvM-i2_22nYThkjFzwIlkdnbFNUO2TP9i1M7VmdXWeY8wWuWhGcLg4OokFK_nQrlFxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2-x5_kUWqqlV631sruH_KxIdcdNwqZP18ZBUKWZMUUjktkbxk27FRdPOTOj8lvHbqkV4houUG5QvaCkzeRtACMZMg5GTOjzaIZtIHCf-Sp8s-SYSmKNehN1hozNXHhaNaYrWggt2tnEU7EWhHGshjMflr-mMDqw2tf8XwTp07_GTwW4BkmRX0Xywc_PY8tVNzBXN025Nlfz4jNO-D5u-HLPJrhshmJJMUMt95uljQn9OXSURFp-ANj2fxo1FLj4FMQkPNEjQgXAoeD8y0iuwX9iml3TjMm1OQz5Y5YDyQbedFB906YPCBPKBUz6fxN2nBDrEM3Vk1KqPn7jO5BWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3SxvzhTGJZ_dlO8J3ZOVro0J8-IPpT7E5ED1BgFKw7PMQmJKu6ff2_O153AFd9EGQSat57gHr8G2rO9ZfqsVY7b8fc7n3MTJPt0t9mZqNDfAk--qLhiCg7N36DjfMxSv6PA4KUhqyz3TsaoxSEGizyt4kikyeXHtpbBU_U8UkCcqV5QvXRPkW_S0fhqyr43i3eEsdft_ZpfaoDUWB5KEN8WiO6xIsk-yTl6fBX99lvbK_Y6Mi81X121xwGdWcVYSUGv3xUQCiCwD8zsm6Y9rRCG_0ppzKe_ASZzpeKDHxJ19pCWwbiD5ZM4m6ZJTZKcpg_KQ1cgT_bzIdtMbkyAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbXnH0Oc0WYrMpun-OfGC413ga6LeXIvMTqHadWWFRwtPk0M7nq3o4YDsVQW4gOLGuQNPC9vMwefGJo1imWPhR18HNDtrlU8QYVpcNWxDTcQcQOV48LILxuoLO45uv_rzNUhbrAjNvohNOr08UUEwLtvWxSsWiBGojkrYNM9_iygxiXxq2G2_u-2nGeq7GnRDUdY_9Z6QiD0PZfutYuPaX6TnOpxsGolTpeq0GWouvqH1zsY1A1eOoy_g2nhM5aEuElM7L8fmATlGB0UYIUE8jaH_CSy0sAifAuD9XKG8VQnko5OfCRtyBcH-ycYNzEMUnDdzzgKLG7b9cPdAsXXsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بازار سنتی تجریش
عکاس:
فاطمه جاوید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457147" target="_blank">📅 05:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457146">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035dc36b79.mp4?token=Ctkq3TYukVMpgJjdv1ozOynrH51RwN9bgz8PC_0HllnM3XGE212v3whw-dIQknzYtV1AxiDl9ASihKLHfBmBS-VIyS7C9EhQl2D1HB-cmB38EY-GGDI3mOT-wLbkd_66xKDa8ghiluTEXBADccQRSaEga9qqtxo6hRko4UlcqixBNLLikHrp6OcQZjI_X5KjnDk_bvukSlWMi5k197MqbxrPqN05Ps7GZUQwOqWVs4bIeMEkkyI3HV0_nBiGcKsc2_biXa8SIrrV15R6a3UNnQj4TtCDZgWtQWZHf7jMHq8BfNPJ1MdophpZCyJP04GybXcTvtZLYP7n7zKGMr4lQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035dc36b79.mp4?token=Ctkq3TYukVMpgJjdv1ozOynrH51RwN9bgz8PC_0HllnM3XGE212v3whw-dIQknzYtV1AxiDl9ASihKLHfBmBS-VIyS7C9EhQl2D1HB-cmB38EY-GGDI3mOT-wLbkd_66xKDa8ghiluTEXBADccQRSaEga9qqtxo6hRko4UlcqixBNLLikHrp6OcQZjI_X5KjnDk_bvukSlWMi5k197MqbxrPqN05Ps7GZUQwOqWVs4bIeMEkkyI3HV0_nBiGcKsc2_biXa8SIrrV15R6a3UNnQj4TtCDZgWtQWZHf7jMHq8BfNPJ1MdophpZCyJP04GybXcTvtZLYP7n7zKGMr4lQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): روزی شما ضمانت شده و شما مأمور عمل به احکام هستید
🔹
مبادا خواستن چیزی که ضمانت شده برایتان برتر از عملی باشد که انجام آن بر شما واجب است!
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/457146" target="_blank">📅 05:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=gYao5GPbDaUuqDdFvSztG51DObcZessBZBk6PxsmeZ5I9TsxF1dEbFd_aGSKDPCfguiYPgDAwTh7x0C_kR3CZoT1h2k58b0q0U_03Za-nPh8aZkksXHXW4s-pxBpaKhOun4fimgqFVxSmaS2AWvXweTNXH29_ila_Jhhvi5YQheTPnaMLSYJkkt4Bu-SKw_aPZ2GqWTygfXNn1HXKkQ_0A7mTyBdG_mRWCoqiUJdDG9VM7eU1_yDP5WB7fR3t2YlyzAay2XotIy3JSq-Nv9thswSudspBt3hYun46huFRvJmu3XEru-AGET6nyeEjkc2BmRcJx11LoX21cjaP-Gs7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=gYao5GPbDaUuqDdFvSztG51DObcZessBZBk6PxsmeZ5I9TsxF1dEbFd_aGSKDPCfguiYPgDAwTh7x0C_kR3CZoT1h2k58b0q0U_03Za-nPh8aZkksXHXW4s-pxBpaKhOun4fimgqFVxSmaS2AWvXweTNXH29_ila_Jhhvi5YQheTPnaMLSYJkkt4Bu-SKw_aPZ2GqWTygfXNn1HXKkQ_0A7mTyBdG_mRWCoqiUJdDG9VM7eU1_yDP5WB7fR3t2YlyzAay2XotIy3JSq-Nv9thswSudspBt3hYun46huFRvJmu3XEru-AGET6nyeEjkc2BmRcJx11LoX21cjaP-Gs7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشک چینی بعد از پرتاب دوباره روی زمین نشست
🔹
چین با موفقیت مرحلۀ اول موشک قابل‌استفاده مجدد «ژوچو-۳» را پس از پرتاب روی زمین فرود آورد؛ دستاوردی که می‌تواند رقابت این کشور با فناوری موشک‌های قابل‌بازیابی و کاهش هزینه‌های پرتاب‌های فضایی را وارد مرحله تازه‌ای کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/457144" target="_blank">📅 04:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSTQt232J1zHGuOh6bQaJiel1RU6j8CP36fHG9_exulHFI6d1T9dk0cF5Dks9TN5HJfRgXeQg0pJD7xIlOj4Uh6IRyhTexuWTifHQ12YxBjo6Yqis6c7B7vQ-6hscdbbCaJnXHuDYWlHxqk6R9-USzQ4Zts-t_z555IFMOE_LlFFF8rp_6MBq2tzWyEA3NDNR3ihQJgji-1_m10ac09jX-PDKmjg-IImQd-ey_eyHFAwCwoyf-lzyaEFRZOWe0yH2sHv9nswlULTewK0LP-7fA-OTlvnyNURJOMvPBGywDTO2IlWKrqcyoaJI3vrblfTZFeTYIVNAvapVw_2rt4Psw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراض نمایشی انگلیس به شروع پروژۀ جدید شهرک‌سازی صهیونیست‌ها
🔹
وزارت خارجۀ انگلیس از احضار کاردار سفارت رژیم صهیونیستی در لندن خبر داد.
🔹
این وزارتخانه در بیانیه‌ای مدعی شد ما کاردار سفارت اسرائیل را برای اعتراض به مناقصۀ پروژۀ شهرک‌سازی ای۱ در کرانۀ باختری احضار کردیم و از او خواستیم که اصرار کند کابینۀ نتانیاهو فوراً پروژۀ شهرک‌سازی ای۱ را لغو کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/457143" target="_blank">📅 04:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062190fde9.mp4?token=vN4TIFr1W1hSfw5ZIHau7z0IpgaIsZn-IaCkqX58uqarttgxT5gv8v1jOAvXDOjGlj2sE1HuAY7vLnFIoghl42dlazRG1x91erziNo4oE89e_LAX87NBo2HcFHK01Pi3HgtkuSgeApic2PhR11goDBoR-WXgC_htvRJUiSWFsczlpJmJja1EwHVsozqEGA1eYWbYN7ILL6P7kQw2AHjs3CV406PA8qVeTyjM6_CeLq9LNy_ki5S5Z5SAsmLtM56RwcO5JI04pPTOI9z3v9vO4LRlRWLOIrqcXV9asfWdbU3xYmX8fXDeWBpww0P2CYMfQVLfMlOCUP4_1EM5WBgmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062190fde9.mp4?token=vN4TIFr1W1hSfw5ZIHau7z0IpgaIsZn-IaCkqX58uqarttgxT5gv8v1jOAvXDOjGlj2sE1HuAY7vLnFIoghl42dlazRG1x91erziNo4oE89e_LAX87NBo2HcFHK01Pi3HgtkuSgeApic2PhR11goDBoR-WXgC_htvRJUiSWFsczlpJmJja1EwHVsozqEGA1eYWbYN7ILL6P7kQw2AHjs3CV406PA8qVeTyjM6_CeLq9LNy_ki5S5Z5SAsmLtM56RwcO5JI04pPTOI9z3v9vO4LRlRWLOIrqcXV9asfWdbU3xYmX8fXDeWBpww0P2CYMfQVLfMlOCUP4_1EM5WBgmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجاوزات متعدد صهیونیست‌ها به جنوب لبنان
🔹
شبکۀ «المیادین» بامداد پنجشنبه گزارش داد که جنگنده‌ها و توپخانۀ رژیم صهیونیستی مناطق «کفررمان»، «تلة الدبشة» و ارتفاعات «علی الطاهر» را هدف قرار دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/457140" target="_blank">📅 03:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534dbabd1d.mp4?token=GGQpxo2bko2uyjc63O7ukMM595ELud0bfUFkhlisfsItYBGSrkzEkkUXIosoYts42lxxGIRhGL3etRiWp3BDKa-OhVjseyvHfaRC5mlJi7GfGd8DzyfaLpQa6DbhE3IKnV7ilTNZFSHnO6vBxnhS1hcZjv98C6P7LgTqi6wL5qEGv8Uy7IRbyPPU-f1LxBSY3s4npaB-8K5jnZ2mEAVT30Djti6IejTqPxBuHqIFO3tyVs3N0e7CVt65RuABpLv7VPODS_BF9PQErmHwotmDKtC0dc0-QWG9LvQoAJ5lrdRyEHP1dVONjgBF8w-ehqaiQFj04cCdij53AG-wbHGyv2VOd_wkf0cViCzTQsVtC8W3K_BzRvfw-VT0IKCLY0wSQDF4gTjKEFQw2fslguhmHqtmGM3BDQr80maHsgMRLSPmhyD-LHCMcbDxMtPxKqK9Qf-119vR1m1pSt9qHn6wQwRsiGX_XXTK1-IAt505tq5x_IV1M9OcSpDeMtdhes8wue0PQtBvqHDH9gnknU0xHL6_dzOtdvoYRebFSjTbd6e2JGZ8Gd4qrAmV-dcl2gSQ97WAtvJ4KgQV6uFbtt-ZtfW7Hg5C-aEN1pIuHE24BzM-XImWZcmqUZToHrYrfnmQs-TahUGI2uwMr2sBuX8QffCTNPS6Yhst7M7J7mX9iGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534dbabd1d.mp4?token=GGQpxo2bko2uyjc63O7ukMM595ELud0bfUFkhlisfsItYBGSrkzEkkUXIosoYts42lxxGIRhGL3etRiWp3BDKa-OhVjseyvHfaRC5mlJi7GfGd8DzyfaLpQa6DbhE3IKnV7ilTNZFSHnO6vBxnhS1hcZjv98C6P7LgTqi6wL5qEGv8Uy7IRbyPPU-f1LxBSY3s4npaB-8K5jnZ2mEAVT30Djti6IejTqPxBuHqIFO3tyVs3N0e7CVt65RuABpLv7VPODS_BF9PQErmHwotmDKtC0dc0-QWG9LvQoAJ5lrdRyEHP1dVONjgBF8w-ehqaiQFj04cCdij53AG-wbHGyv2VOd_wkf0cViCzTQsVtC8W3K_BzRvfw-VT0IKCLY0wSQDF4gTjKEFQw2fslguhmHqtmGM3BDQr80maHsgMRLSPmhyD-LHCMcbDxMtPxKqK9Qf-119vR1m1pSt9qHn6wQwRsiGX_XXTK1-IAt505tq5x_IV1M9OcSpDeMtdhes8wue0PQtBvqHDH9gnknU0xHL6_dzOtdvoYRebFSjTbd6e2JGZ8Gd4qrAmV-dcl2gSQ97WAtvJ4KgQV6uFbtt-ZtfW7Hg5C-aEN1pIuHE24BzM-XImWZcmqUZToHrYrfnmQs-TahUGI2uwMr2sBuX8QffCTNPS6Yhst7M7J7mX9iGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الیوم یوم الانتقام
◾️
مداحی محمدرضا بذری در مراسم چهلم تدفین آقای شهید ایران در حرم حضرت معصومه(س)</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/457139" target="_blank">📅 03:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU32m3JlPq64oNiHd5j0IvNg0n1cjrk1xyDpbC8n9u--RnvzwfsFUD9_yhN3xSQ60o4fIyP4UziymUe82Yq278kQan5xPP9BokQ0HYKerWu_Swa8QUE9Nm8WtAyjIgg9OKyCGmGULX4TlvLuwjJdZ9zKokGEzxxCqLp3gzCN4nUg4Qsfy1Cf2onLHV50pl3iHTuS-4S1EgY2f0Sc0KreBnzknXc9AXJ8mkpCcrz-h6qCOGeYD8bEOeMF7v5nWdlnT4vEssK7qSS7QvLfCYmwEPO3yynBVnPFYpzCUA9SxQ12BtXnXu7Ixyuf6miGAJbrjVIFT016fSva3Wb5TaXL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران «نابود شده»، صنایع نظامی به «ویرانه» تبدیل شده و کشور در آستانۀ فروپاشی قرار دارد.
🔸
این ادعاها درحالی مطرح می‌شود که ترامپ پیش‌تر نیز بارها از «فروپاشی قریب‌الوقوع» ایران و وارد کردن «ضربه‌های تاریخی» سخن گفته بود؛ ادعاهایی که تکرار مداوم آنها، بیش از آنکه نشانۀ یک دستاورد جدید باشد، به تکرار همان جنگ روانی و تبلیغاتی علیه ایران شباهت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457138" target="_blank">📅 02:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfpkAq3LPaqtpeLExMGpNPWqqCmWb6yxyCQhY_Nd-hnWvXPd-uK9mdy3mI0V-wQqbWQc5CJZOfWpzAk8Q0NikYotW3Ydr-WSS00esCtKdAyosw2uqLt6rAWZjghoQbhWOX48qmmXka1Dhe1Jytho6JZAAjNLVacEXEPR2ObD14a8XIKHpyRxJihl_07z1KQJ0zVJeK0DLfm9hgIVzRANP7lO698uYuN23ZtK_4DKIE1btekHnFH5q6LG-RkiV9Q1TulaHNpm55KLZR9NQEsLDc3gh2kjrQY1DI4LPLDlZMLmwUMilnh_33uvKgFZbeWlunpDsui4R9sQtpwgc-HymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک فالکون ۹ اسپیس‌ایکس پس از ماه‌ها سرگردانی در فضا، امروز به سطح ماه برخورد می‌کند.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457137" target="_blank">📅 02:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457136">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQeZD2cg73u6e1ZT0NBGwIubP4w2MyZ4OXY-Nw9hs3NLSVyMj3KP6Aka8NEqS_oYHinukYss37XhkcHaEyXtm6xvimYLtU1t7sy5-rtpL0Z7JQnitWRgFRtJ9JtrotxTF4vzEFKTp28W54Po8m_GCSNicDvN9HZK_DnJhDcJ3koHwLgoBLn3SAV9Uq9rak7hCQMSxBIEpiV0wkKfpZG6OR8kKD9y6XjfmvpfZADLlTnSvtWt4XzX_g-5q1P-pQaRjUIppg59hHwLcarbagzaq7NNdF8SBDkogV-_89odwcaQZS0qixbodyW6qFNQ-Gd_6LXwo-FgDCZLdyUtHsaTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه غول زیرآبی حمل‌کنندۀ سلاح‌ هسته‌ای آزمایش می‌کند
🔹
روسیه آزمایش‌های دریایی نخستین زیردریایی هسته‌ای «خاباروفسک» را آغاز کرده است. اما اهمیت اصلی خاباروفسک به محموله‌ای برمی‌گردد که برای حمل آن طراحی شده است: شش سامانۀ پوزیدون.
🔹
پوزیدون یک وسیلۀ نقلیۀ زیرآبی بدون‌سرنشین و مجهز به پیشران هسته‌ای است که روسیه آن را برای حمل کلاهک هسته‌ای در بردهای بسیار طولانی توسعه داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/457136" target="_blank">📅 01:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cefc2913b.mp4?token=Qdd03q9AiRJwh72hNPFVvfrUW3rdUntpMks2pfACUxrSbcero9sOCKLiL1C4eH-IlLHHkGtuH6AiwmAwAHe4J0V7oElv6EI44NdB1gFh0xXgISQJTOAsDFNVrz8iJLzXpf3bQNd5fgglqWGwswfI3ofe9L8JLNjti_uKlhf_IhCOCgYshFlc592vDxHcNzmpGq81KILhWgciSaxDSZVdP_ZaWnhaIhy_K6tsbHBn_me4KXpqpzbzMsV4X5SJtv06EjP-SMAzNoCF2A1cnWAcUhU2xiQfDQHMLd22Dd1TdQPeI1XEVz34LBgglvKVpmb3PM0ZO7cExIKzNkTXZxt6CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cefc2913b.mp4?token=Qdd03q9AiRJwh72hNPFVvfrUW3rdUntpMks2pfACUxrSbcero9sOCKLiL1C4eH-IlLHHkGtuH6AiwmAwAHe4J0V7oElv6EI44NdB1gFh0xXgISQJTOAsDFNVrz8iJLzXpf3bQNd5fgglqWGwswfI3ofe9L8JLNjti_uKlhf_IhCOCgYshFlc592vDxHcNzmpGq81KILhWgciSaxDSZVdP_ZaWnhaIhy_K6tsbHBn_me4KXpqpzbzMsV4X5SJtv06EjP-SMAzNoCF2A1cnWAcUhU2xiQfDQHMLd22Dd1TdQPeI1XEVz34LBgglvKVpmb3PM0ZO7cExIKzNkTXZxt6CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر تازه منتشرشده از توله‌های «هلیا» یوزپلنگ آسیایی، که آن‌ها را در سلامت و آرامش نشان می‌دهد   @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457135" target="_blank">📅 01:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRqahySUDoZngEwrCOMoyjyQqb4f8XfCH-JBD1XQErDR2g1DSz10kQluHzK0nlgJYmooPhIBkbv-Xsv9bmqHE2iAE89YHwWK6t-lBgx-lTcK56xlEXQXZBCqAgzpUulm0eeVfKHuxJOMb8aCOF-Mt0kQvD7jMKNRJw9wTVMLy9ScPtNmvJAlK4ImqmlHvMQTOw6QjzdELtXqS7lC6Y6b8TqaT9_PjxB7wPvjRSVx3fS3k229KIhY5ThgCEwJ-gvl5wIUbKoIpLcLZHt582NoiES9rg1U0_jT3_7dHeZEzbsnBT9cvZIcMj4jqDdiDKhy0jlEcLJrPX2wjjBDk_noxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: هنوز می‌توانیم ایران را تحریم کنیم
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم.
🔹
وی با تکرار توهمات مضحک خود ادعا کرد هم‌اکنون تنگۀ هرمز باز است و قایق‌های زیادی از آن عبور می‌کنند. البته ممکن است این ترددها در مقطعی آهسته شود.
🔹
رئیس‌جمهور کودک‌کش آمریکا همچنین دربارۀ افزایش بهای جهانی نفت و قیمت سوخت در ایالات متحده ادعا کرد: خطوط لولۀ زیادی برای انتقال نفت و گاز در حال ساخت است. من فکر می‌کنم تنگۀ هرمز به اندازۀ گذشته مهم نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/457134" target="_blank">📅 01:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حملات موشکی روسیه به پایتخت اوکراین
🔹
رسانه‌های اوکراینی از وقوع چندین انفجار مهیب در پایتخت این کشور گزارش دادند.
🔹
شهردار کی‌یف با تایید این خبر اعلام کرد که پایتخت اوکراین هدف حملۀ موشکی بالستیک روسیه قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457133" target="_blank">📅 00:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMe2CGZ6I6LVsJg9BtnnFavNDNLMcPpQBS7YrGPrhWJ-T13dFx2ktn-ZuYlrnZZdJHVhq6vNprZ0kQabG-PPgWSEO1XnF86DjElrAikqMfHjTXq4tf-ChMb2wuwXmFTI-6-VMUa1vnk-Wp8tqumrgdiwsyId5aemmwFmI988U9HIGLV_0Li5F8HTakxpvldZTIV_SwhrWGdX__avmesY9j7nG7zvI7bY7tpIo4WdO-UQeMb2fGFC66SvvxWXXn-PU34aSRK3dWip2wqDnsiPBsNV8Mh-oLuSywFZ4hbTu1xXgJlo6wJbHGRQ1eOOPrj21DMvQPgKCHrkABdASNP5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8NayPsirXxwag6PJbuusmRZuW7VMxMDqmxGEizHDsdBSf3vND8-dBdEwtIOdDD98iEbTCOKoX7Cs_22Vg3Txn-cc1vpSWnN-GNoRzPZ2By29N9VCOu6KH3bFzzV899OyYEZWG8IbycfcWi-1loR0x_PZWxTVZcJT_LaHn_1jui2ph4Pab2JPnnplKW6BwoMOv3Fbc_zOarlxsDQ1qbvfc_SwxL2VsM7c09zKZNF6RrL6PNosNwwWdCxDQe_2HMyHzXEdBL4E5jj9YOFDQ8h73Ria2m_BWJyefS4Xxn7FHcIw6ws6LVRFPvr3XyMTnDty5-Ff_XCpBxjaXWh0nN5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btlYpJM3_QY3kDjSV_yaWBGXHgjcVNBOhn2sQrI3zhJpm5Kw7fzcygFJNmC2_m2bD9NSjBFbABKl0zGbsLs2LSq6yYcfJ_7MSSyk_I1E0I1JjuLzicazjQVoCZtWB2uVJ0ZoDWpYPh16vlsxyj8aUrgKeP2PtLmdrCCzmH-2i7dUClGBrAJmsIgfR9WN7GMufmKP7d_YbPSojg4bA3zxm0xNFpeG6lMyPxHCmhhl8qr9_n3uu1eAJDKr9Bb0i4ky6KthhydPU4Z_BX-nDLHhKtBogXocX4qsLuySTVv9HAjLtYWhAoMIYpxqIZfpdhrhuFUem1rWp0IRDHQgoxt7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZcmJkhZ3p7S6OVZWJN3kIZpGI6vOFzMY595jUjIW9y5SQGClm45PzZIQwgqgK-foipSU69P0m5Y2s3dkqvuhB2c0BkBHh-i99GePomWf66qSZgDq_a-AB2TNpxTkdQOKzZB3HsgV2YlKrSuAWnaQw_aqsCAEgzfs1-syUY6jE-upHx2VcoG7-7iOs7oJq-jXWhPHXBQ1MverG4udK8S3sgacqD6t24IxBiI9HdvzD-DdatGnZcX2dsBQRoghrok4k1OfESEFq8uKfC9XwIMaLZAVvAQsMtWLvyEt9dGOSVNjIJxl_jt6hByhnEWNyNr7HidPxogwDTCSHK8hjiMnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۹ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457129" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsy2M61tAK2kTtkd1kVEmwyIihG_6rwcMbLu-VfmSGFEgXCrX_nk5qT28GQKOq3Yvzk915mGT0IOTOSmrlsZL3iG2APtmryEAS3o0-536LpSp5h64LZ1EXDZEnNd3EbHPDpjjPwnXnFRN7Ii2VJUTypPriLoff3JHmg15GOvuxgGUQyajiQyTZCDVpD5OOXoBDN-aIojCRfC8XNZ25_mVK0RJPCrtLEkNsHmUxOYcPik9pB40ABWsUicHzKz1fOdf3jZvfSef1vGNPkSVR59WggLns-T3erWpVElq6YXSyog-YXeZbj3Z4yJGkXPBRsTmViQgMTjbKzu5kWMq5Wg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZzpKgiiYmTUQ5NcZrh0ydpB0nwTBODX2eJ0oBHt0ISnmHl7TXbCtP1q9GTdSy4iyyoEgpcSAtFBDqGuMu3WI89SoanweCeqSaKRm-aB2oiQ3wKiblmkilO6wVAgY7T30yHku9fGtLJutAGC9UyjVEh3pkIlWjnZs5s79TclSXOJ-C8CNPRleOAgdoGn9Z-zMBgX_SbvKE3TXgsbOeKpuAGvZ2pOLqG4nzd5LsBcG6HMv8URZDd4X5LX_M6A1Pi_33YDgenqf0rY1H0C7eIjXFvHSwJGM84yo9wx-P60VCjAbbeTz2TYOt6xopVodIqBdslj_YaWrGNxdVX_E3jdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvOrsCvxBQf6-w7wXFKjhthPSHtijHRLjpsIkPo-jAlrJQR6XOB022Txaqoi3k7-k65chUOMZcA99BzQdDcbHBXSEju78jpqTSfS594A61bNlZBXmzDMm_uQ5RcStSqSsUeOdYOLhWZrx4q9QHMfG_H5Bpl5k43Cq8cXjxxdfeEiHumbwNHYr-5Nmvmx0azVQA-DqmJLaYCfsPqE_Ihr2jm8YfdK5TK408efxyBtLruP3r-JiJDT2e4hDZo0nmHfnjksSw9JDPMpPFW3c6GHlBkrZpGKQYLNYY1tsTzK9STW0UUXf1-CkIIQjblSBVA_ovfBZoJTWzoc3Tkh7oqc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR3ZdrODYlvE5zzb8X7W-srRN_dySAcrFf-ENP3xbAgBuIONQk1hL9w1NC460kgyUvkHTDUaUthYoPExAcxFEQqis7vxtLiPqU6mYaQgsxFVxca0BTPLRccSbKIAIbwB-KNRCqn0x9kIKdIBfrzNoHpCqL_ef-o4YqwHqh0f9CRjSU_jK4b6Bad6RjXdDa6H03Lw7oGEh5njSAjp69QcFv930YiUbbHqC3h4Hiy2eab564Zj-8a5sAuyWeCa8NdCOfY5pkVcwAB5Ffsr5ivSZiqIogt34UoVvWzX8Y5glM8jS0uuuNpY5e1EPf567WKd01IJFy2ETezS8Qmz9LPT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCprFdTq20ZnCwSQVmlRDNXuhs2V9yBW_cLj3JLCF_FLdA0SpcCke7x_ljvhDPJRSVeohrxuYVstAJ4Dzn4_0tvdlJtj4DzTBc0NO2mvktYAC3bE2_kvT4ech77qrWup6OLNbizGBJpOXm5oWNPJNn6J7NbT-uUW-oO3a5T5wzYfiEGqyWshnY6poZDi1tuxzhyaodiJkHPVfoJWDrEoHjihTzMVogTd4GKIKOWq-Z1rQWCNh__N2Kw9iTtk8mgIJJNfAs_b2KAqYX9dpozKEaNjgbW-O0ZFwYa-_OetIW7KvvdK4wHQKqRCpVyouiFANa7WGsdSNdiDjzgeriO5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLGc4w_3mk9iPrR1WQN9OpKP775dMmPzd-wQb2Nz2NScDzSW3YkxFef8XF2rwUu9ul4aMaaFSuKtBrXUzdUS72NN_BpN85EOEeASYKAefGAlUlkh5WnxUTxkfha2LjBOt_l5YTKOTsizCA8gsuIl6kVkMPePgZp2oyI7Bi5KvBa5PokUWE1mb-ax6FiIzg_bMDQq9ykBTfsw6oE3kIS95HdUakmw-bkVj8k464ak6tqQSqBhlsTsJFWXf47xGI-m3pb6ODqrqn3mK3K9SXYiCDWHyP_ArfxusBnYw0RMGbW5GTPTDxKLEOtc9zuePvt5lTwS_pDwoqmBzR8kzfD_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKlHGvl_iZCTZjjmL6iHrEMINEy-4DzmPc2ELG0G4juX0oCiD1EwQ_3Gd9II09M-X2Mlg8Ce3qYGuMKO3RXE5vXJOEIy4oM3S24ngpdK0WtTbOurczlohabOIY9m-f8QciPhe11NCa5FjuoWHxGXuvO-XZOPUc7f-ACG-vPOtqMCnGN5Jpq5S1FiwBdnPXyTLqdZ_-mSnjGtPlEitvdSK03FhRmpqyCaDJxfSZjbHunt43_vPxilRASLG37CI8YE39J8U8e5IZFZ1vVEyeh0Ic5O-rupWF7fyqyX2-bId16lTHWSiiaNNkAUNO7pAAd4MjRoOMYV89mnkuRRKSFoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5Lwupi7bqtSdr-NNNcw1Qqgv9FIDJsoSnyFG1kG5BcbVCOEtOPtmVj1voTbhMGbZnvtVgqqngM4KPiQ-Q1Ak8gP1sCrtnqyiGleQ-BMXK4MwuiTBy9DKBLS6Dz1PCOp86taaOR-p3CeRepyAZ5FyJ6HHhIkv1BTMXA_aTiZgU1Jh53YmFWc_GKA57ksiD4U1uLvZb07XdJKp9rqxG8Jlud66qO_b0FS1Kc8czVYqJdIvSHToO23Okw31TT2vUCyBqPn2IQq1G5GrCWVfvhioLg7484rNGAer_CMueWctaz91Zicf86MDL6s7mLIlSWyPfzt5SNH_g5phJPwKA1wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMRWJ15QdYr1-abl0fBL9Bo_3xl4lU92xfmK-FQSIl4DOh9mYQlYc9bw96Hq13XMuIY-k6TWuwo03jRc8rT9-9UQ_zCrP7BUZLFlktAB71OSh6YdW6W1B2Pr43KbmxbjWf597gHEL-ETQF5N7V4zj_PBHL67h_uJHlRFuAT0e1Wo5CcMkJCWWcKLIhzXyhQ9FpVwI-qxDBAc87sslutihzwKmKBIr056dfZtQK1YQGQmapbN2f9999frj5kTlNdaljuemWJO7G5gZ62toyoLsrt-D4D1xLgio2qkiNT4AD8Wo7Cm5HZccL31c160mqeuTWfWUYZki1-JvY0HcILR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdxgpJVkNEPjgOK3FgfjQQlTojHlv68ehMpxdZ9NJG3mrBN636zt1OqoRtEcIW4tSDGPZnFQ1O3uqn3d_Bn6Dx0GS-DbTBOqyfvlsgWDW831zpGTLLUWzadkLzHYMaUD_1koYwwmix4hJOYWkQ1IBrl4wzaCv8AW8gMBY9yAZv6JL1UUwxZTZmekznkWwSnYWrS8sHtpzGKh6Dd8h7qdeemwq2_Y2Zs24oyUDRK4w6sWcyDsA6leldr3dPxBYrx0JzRXb18XZAlKVl7aAFIcmRVyeL9ZLT2kvmzb9uKqP5x6aVXwynfVIyvQVP_ynnM3Z3A_mBpciWv2SlcxMqN3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457119" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPJQtmuHyEWdrqzeC-PaPcTNZ7F6sV46vaK1IT60_nV_gcvLvQBq28UwJDCJN-RC6aGbGpXSSWUa_qkFR7ho4uXhEw0__FZL_iZJv-P5shOiTeT8zeuoL4V88x0anYMRizlFpgfdgLV0CD0ubqzvzwyPLIPtTOCskMVExD-OvAtGaw-SG86ftXKvQ-irXz0z2_sbZTTMawDP3nwf5WZvKxlQ3uxgvcQJsb7rK8ACOuj9pZtCUtUKhHa8cx-X-DESyHFPz6LJJ2SzT-qDH2g-uBDZH85tGPKl1-wIm6MI4YS56rSFq-ANOG1IXYo0RATVkRXdG3GX5DTXHt6Y0R854w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام اینفلوئنسر اجیر می‌کند!
🔹
مرکز پژوهشTTP در گزارش جدید خود نوشت: متا صاحب اینستاگرام، برای مقابله با موج ممنوعیت شبکه‌های اجتماعی برای افراد زیر ۱۶ سال، به اینفلوئنسرها پول می‌دهد تا از حضور نوجوانان در پلتفرم‌هایش و ابزارهای ایمنی حساب‌های نوجوانان دفاع کنند.
🔹
این مرکز در مطلبی عنوان کرد که متا در کشورها، از آسیا و خاورمیانه گرفته تا اروپا، به بازیگران، روان‌شناسان و اینفلوئنسرهای حوزۀ فرزندپروری پول پرداخته تا در برابر ممنوعیت‌های فراگیر حساب کاربری نوجوانان موضع بگیرند.
🔸
این کارزار از زمانی شتاب گرفت که استرالیا نخستین قانون ممنوعیت شبکه‌های اجتماعی برای زیر ۱۶ سال را در جهان تصویب کرد؛ اقدامی که دسترسی متا به یکی از سودآورترین گروه‌های سنی کاربران را تهدید می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/457118" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457111">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjeFr5wjdMpqcsR6RHmyJ6JV109Y--C9jqngJCnqefH5vkbkR_-h9GuEA9brWSOsNf58s2TsaO0rgsuYWWL4xVRhUOpdc8qaFIRAEabIvsemuX2ztRfdPYOxbKAgnpLwG8Ygig7l7w8qAZG1VV5BLxiaLSuH1YdeUFDKfI0mqiMe-AFjO2FDeN5ZDclfBaeBDQD6u2_P006662uiY7nI1Tau2O1MiCTDOQOrKCbO2mLFTf_BjkZldueptu9OiysDcwSGhTujMpNOfeBARSomFd9L98TOMLzMDCiJ5FwdYHHvEdypSC0uDHELj424FkUNsAiiqAwmRoCRLTnxgBEygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnwGsDmdm-0yeIEnRHQE_fDdBzfrl3FcHtqFiWGZbxIupSE471CPaQwKRFX15HxN3bwCnenq7MCah_tLWKw6FXJUiA1BAnhpoy69DPmctFQk5MOOaPE1A-MK5XyFCqv5Wy1skd5lVYvhbJEeUbkqd9C8BGyN7A2njrjGIiU1KZIlYQ8JHl6xxb0ShdrtH_esjR0HWlhsERrTPxr5IzIY0y6ulCVejTq8oAHVrQHDcN-_WW13wCHnz7lP3uqcHEMiIy0uYEHLtNbMRkMQCqSNirZnS7ObvxYamhs11oDi4nRXqdPy65c9fiylelTaib3ICMEmD1xu1NrDPXrtYrQaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtiQVgs-rYBYFsphOEnahwjeAt2i1dV7riygBUGYOIzeFZOFfDmydErNidWRCB6KG0TsM5__SDr2scw2rAX8t-naximOufZ7LYmilYlnUx-xtGGNw8vuTLXSTJ2fQmvSHqziiVtn3GKDnH3y1oeeIgtNTtGU_OuykbrgF1FeAPyghzzuPOnNcu0uUXL-wemVnGSDN-ayLnYmN17j_vz1Ng7bR9-fyvfcAwlTHGvEsy6QmYaDi0QmHzu5mJOqXhp2GirLaXwfLFKTaCs7LkO7UXTkL2i6G4cQkx-zN6UFOqSszlHS_wqzGD5EQg2zn55cVFNlwECag1xZcebu9FAs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoXxpIPrZq6mmT7SiVEu0WzO3HN_SVEHOu4xWBD7WwusLJqa0K_BN2tZUOCq9CQtl7sjgupjSvAOx0roVqJMF-rERw8S1_4hoI7yd5_iJ3RrqQSkKP-ytqY5gclAP4BdAX5KOyuOMDlzybtlngFDhlvBWZezIOdX0F5V-UdCF5tv-EcZxA3SI1CaDcI0d-DFxeX40Gw6X6IO_hlleFfRHUG4YlBxhuWj3vZUVqVp7mlYfOMM6Gehu4mHZcJhWwyCs6pKsC8niKKwneE7-BHTI17YfSDdDcYE8j7JBrAOPkAGOL7KGroHpo_7erWK1I8N8RVHZK19O1rDxEGQxFWlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HblBN2A9DOVJA8IGh-rEle1f4ZeSjK9RIS1VK3jcP9PZvqx9R1YrSr2ZerP9OrK2d5enXwB4oyp72UXqrh68qebwp2bgCqdFmYQf1dYQ-Rade-KvxbXzOhhyYLD0NSX80VONoHhAThAUPglRZW9qWGRMk78lhJrB9zDEwQGf8Gg3jGb3tSUt1DO_Mofi_VEYAor3t4TO-6POCV8vlqvEneMEFCprICIAPyDxN3RUsGu_RNwRA1jJ6BmsjSqQhOxGzRlPKCqCzRxHUugHKM59tJPxIEyQTxPfIT-Aj0kE7-PEO4bLdKFeMCFTu0YoSnr3w45y4NT2OYS2YbZNCx4KyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jv04V6QltzCtcxr2tdbe0pGWCqgitrOzWUF2-1p3fZ3epK2TiwLOmaTsaS9UxqzS94eCUF5tIZ8qCepPeQ9ehCUsVv_CWhfaYchHnpwke9KBU1J3vqRMdGUfpqOU4IGRasl9Q4NKTVSU8X2j2TWwq_G2Nh-3F8lpKNnoaxGkITznlfsJuX0pyAE-ke8CBOXbG9NsmitCkNOAEUxl3A_lj094MOSgXhf4XBWZ_JIi789bLJ5F7tTsLdshX5DXb1jXjY-htVcskLuifPe2yOUeZAhyG-jpzOVjcBhv6txLH8MtBdVYkcrmMBHl2A6SgZBKErDW6dXKK5aZeyxIBejhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV1x5zDEkEtwbuv1LaqWqgI4xM9iIWCk7j7f47hstb4k9-xsHZ0izWzfMRAjzezJpSvz65cnVBBGi8vK8BPSCkyB6aVchrvNaBRw54BewN3rRQEFxzYlEnqX_14fbuo7mW7fMvyseyjhG7Sxo-xwGDKHoeTlW4wdGLMY3a1Dl3hJBclxLStSF7f0_WwA9Zi0vl90k2kKFhICqiqW0aR6pYx7NXA-6FNXtoFGZiv2V2bxxJQ1eRCEyj_lSTn8LZpWhfossoQXXr6cSYirTcs5-4qEafXsxGcZjbCfbbSUG_qpUQjJcPJT5fqp6f8Qfgza0oPYahgmQid6j3kufV2ihw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین خاک‌سپاری رهبر شهید انقلاب در اراک
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457111" target="_blank">📅 23:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457110">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc99cb7a6.mp4?token=Ff97HdwAEv9om62trISBsVO372rohkU7pCv1DgFbcfPRaorAseWoFGFuGQzzmyABkCaJRWF6DB65OpUTXwummPYHiJmyIgherYLb3ug1zGPApJ59SxeIjUjwGkzcIs2Y137iTG9ejhugY23vfFPNVzkXI4xOFy8XDMoFxj_FV7Rm559MN6gHbOgeyAAQDdRNeqcWTN3s7BQ3pkqMArdGAtfNhxQJdXZ0s7GQYEcqejKGi3waKzqVaUm_DAgR_gVo5LPLwxtUpMj3dAF71WtkvNjIdPMtw-P2qRxBSvPEFogSIY1T4tuzYxrvawKzfYD5wdbajG_GplWYNBgiubYkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc99cb7a6.mp4?token=Ff97HdwAEv9om62trISBsVO372rohkU7pCv1DgFbcfPRaorAseWoFGFuGQzzmyABkCaJRWF6DB65OpUTXwummPYHiJmyIgherYLb3ug1zGPApJ59SxeIjUjwGkzcIs2Y137iTG9ejhugY23vfFPNVzkXI4xOFy8XDMoFxj_FV7Rm559MN6gHbOgeyAAQDdRNeqcWTN3s7BQ3pkqMArdGAtfNhxQJdXZ0s7GQYEcqejKGi3waKzqVaUm_DAgR_gVo5LPLwxtUpMj3dAF71WtkvNjIdPMtw-P2qRxBSvPEFogSIY1T4tuzYxrvawKzfYD5wdbajG_GplWYNBgiubYkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر شهید پاکپور: بعد از جنگ ۱۲ روزه فقط ۳ بار فرزندم را دیدم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457110" target="_blank">📅 23:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457109">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تکمیلی/
مرگ رئیس دستگاه اطلاعاتی اکوادور و پنج آمریکایی در سقوط بالگرد
🔹
در حالی‌که رسانه‌ها اعلام کرده بودند که در پی سقوط بالگرد در کنیا شش گردشگر کشته شده‌اند، گزارش‌ها از مرگ رئیس کل مرکز ملی اطلاعات اکوادور به همراه پنج تبعه آمریکا در این حادثه خبر می‌دهند.
🔹
به گزارش دویچه وله، میشل سنسی-کونتوجی در این حادثه جان خود را از دست داد. وی در ژانویهٔ ۲۰۲۴ به سمت ریاست اطلاعات اکوادور منصوب شد و همچنین، مدتی وزیر کشور اکوادور بود.
🔹
علاوه بر این، ان‌بی‌سی یونیورسال اعلام کرده است که خوزه آلبرتو سوارس، رئیس و مدیرکل در شبکه‌های مختلف تلموندو، از جمله کشته‌شدگان این سانحه است.
🔸
تلموندو یک شبکه تلویزیونی آمریکایی است که برنامه‌هایی به زبان اسپانیایی تولید می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457109" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در لردگان
🔹
سپاه ناحیۀ لردگان: فردا از ساعت ۸ صبح تا ۱۲ ظهر احتمال شنیده‌شدن صدای انفجار کنترل‌شده در شهرستان لردگان و حومۀ آن وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457108" target="_blank">📅 23:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=cbnH80xASgsqxYjNk05q1F9PdwjhNLR2GjUBywgYu6OuOBaFtWIAhGW4-eEeiyE4GmJ0O85EzYOw3J4Nm0C5-BRuskySaOuFZQuDBkqOFNjfsSgT8ShsjKpmbMyh6aQGWDyWDdW-oa8GEGkqj_wwk5g2OXbfEtP97wPF6xMQGhfcJac4KpWTv9QhrJnwE7jevzjEf3nN0Wb6egLPeQ4c3bkctP2qIfmEi069BpyziNkHmoKC5OAfduUMP-Y34ejgABRaZhG7ke562oHshPY6USpwqbr08hhCJ_2c2EL4Gb_6tO2jGzOGC5e4pxu3TtZsw1dVrsQGTPgdmW8mVB_Zog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=cbnH80xASgsqxYjNk05q1F9PdwjhNLR2GjUBywgYu6OuOBaFtWIAhGW4-eEeiyE4GmJ0O85EzYOw3J4Nm0C5-BRuskySaOuFZQuDBkqOFNjfsSgT8ShsjKpmbMyh6aQGWDyWDdW-oa8GEGkqj_wwk5g2OXbfEtP97wPF6xMQGhfcJac4KpWTv9QhrJnwE7jevzjEf3nN0Wb6egLPeQ4c3bkctP2qIfmEi069BpyziNkHmoKC5OAfduUMP-Y34ejgABRaZhG7ke562oHshPY6USpwqbr08hhCJ_2c2EL4Gb_6tO2jGzOGC5e4pxu3TtZsw1dVrsQGTPgdmW8mVB_Zog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: ۷۵ همت از اموال بانک ایران‌زمین به نفع بانک مرکزی مصادره شد
🔹
این بانک ۱۱۴ همت اضافه‌برداشت داشت که با کمک قوه‌قضائیه با آن برخورد شد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/457107" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e19cea5db.mp4?token=mfHBxqSgjD1d0C0q4Daw0Vo3WIbUFmlbk3r9nuwDrBCuKPSISqKoy1J4ZChkQqeE48NJVJQKy332XWClI4BZ55H1YX3UWAnbnGSNvjYG8hauy7PsQ7y7AXH7igRtG4hDGOX0gyMMDWmmdULczQrLqAF_8B9JFcBnVhBvEHhT_lKlVtAHXBTXG8zPwSrk7bMaWFyNEvwQNpY1gR08tb7tAOcKSn-ij65WTZbeVNqdB5ZeA-zJtsulE1-UMewA6sxwveJq_4Oeo1rBnWLZXuKSDQcSym2T9Tmp-mxwWz-AzafQfMK3XKCO8KKjH-QTQ8Xweh-hpC-uzoYCZqAYeqeiwGZzvlSid0u6qEMP-ChRvykBIF7eg0Z0EIvVO3yuld_UqhAS5ox3trx30S2-OlXF8Oleenji_QCG1Qk8DnJWVxGTeFp1jsB5oOE2crlb91gqHfm2BZ7hffm6r5z_OzSwkBChonrkW4ceYt1YzAlqHrtfnSmnfhAa-_GxFhC8n55F3bi1tXzdLL9W5Cl-RCChBmw0ZrHHrd15mPQSaWz40KSppOHXjuLTcgMUyqSW47w-drjXdlMbZ9UaGcEwe77mjyzuvQNSc-ZMDUu_ZLkDILDFLWRqg-HrEkfmaVQu_20MJEsQIEwCPK7LiJxUGGW401FQWRcjPLW24_17mL4XU4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e19cea5db.mp4?token=mfHBxqSgjD1d0C0q4Daw0Vo3WIbUFmlbk3r9nuwDrBCuKPSISqKoy1J4ZChkQqeE48NJVJQKy332XWClI4BZ55H1YX3UWAnbnGSNvjYG8hauy7PsQ7y7AXH7igRtG4hDGOX0gyMMDWmmdULczQrLqAF_8B9JFcBnVhBvEHhT_lKlVtAHXBTXG8zPwSrk7bMaWFyNEvwQNpY1gR08tb7tAOcKSn-ij65WTZbeVNqdB5ZeA-zJtsulE1-UMewA6sxwveJq_4Oeo1rBnWLZXuKSDQcSym2T9Tmp-mxwWz-AzafQfMK3XKCO8KKjH-QTQ8Xweh-hpC-uzoYCZqAYeqeiwGZzvlSid0u6qEMP-ChRvykBIF7eg0Z0EIvVO3yuld_UqhAS5ox3trx30S2-OlXF8Oleenji_QCG1Qk8DnJWVxGTeFp1jsB5oOE2crlb91gqHfm2BZ7hffm6r5z_OzSwkBChonrkW4ceYt1YzAlqHrtfnSmnfhAa-_GxFhC8n55F3bi1tXzdLL9W5Cl-RCChBmw0ZrHHrd15mPQSaWz40KSppOHXjuLTcgMUyqSW47w-drjXdlMbZ9UaGcEwe77mjyzuvQNSc-ZMDUu_ZLkDILDFLWRqg-HrEkfmaVQu_20MJEsQIEwCPK7LiJxUGGW401FQWRcjPLW24_17mL4XU4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریادهای مردم کرمان در شب ۱۷۲ خون‌خواهی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457106" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a78829c1f.mp4?token=Ch-RNzzBStYu3End7F2fUxdI1bV8WlVwYIxBx-CGE-Oe7mcog0HFMhCnDjLwVOGnmy6dA4rBTGQj4S0pEbwSVh7THxnuWASzTiriJZl1rXSB06akvgOXCRJ65lD8FTr-7I0czxy2ms4LUN3080W59hTS1iXegnO1_u2JJp7nlTwBQhKwcCgy9SRbunoEhuQ78bmElAs2FEpdeUwYfGujeJmKYwxSg7qDfTNX5L2F5yo8BIrQABHnb3EodXrTDsCke_V0j4A2SMbsz1mugle2tKybOx7i0CP0ttu5qyS8zSEWpG4v4_Qsp5AwVGgWWbX7Yycjl_tZPriCTq6C6eo_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a78829c1f.mp4?token=Ch-RNzzBStYu3End7F2fUxdI1bV8WlVwYIxBx-CGE-Oe7mcog0HFMhCnDjLwVOGnmy6dA4rBTGQj4S0pEbwSVh7THxnuWASzTiriJZl1rXSB06akvgOXCRJ65lD8FTr-7I0czxy2ms4LUN3080W59hTS1iXegnO1_u2JJp7nlTwBQhKwcCgy9SRbunoEhuQ78bmElAs2FEpdeUwYfGujeJmKYwxSg7qDfTNX5L2F5yo8BIrQABHnb3EodXrTDsCke_V0j4A2SMbsz1mugle2tKybOx7i0CP0ttu5qyS8zSEWpG4v4_Qsp5AwVGgWWbX7Yycjl_tZPriCTq6C6eo_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: باتوجه به رشد نرخ ارز، رشد ۲۳ درصدی برای کالابرگ منطقی است  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457105" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e7b14962.mp4?token=lMrG8EpsZQmPTUpgZ4wzsfRQJqdufhpUJTBUfTAEID6sm30KMKE1mAKvdgH-cxmmI3wB0fjODOCKTvWTtjK85E4sQFPDBCV05L4PtSCl5iIIsjuQu9nV7h5rrKE94-3gnbX_sDkblOWbroyVSDMT3Ng4mXh9XziLNfhpgvQrbWMJaXY_GwMrhULRN7bbcyp4ck5N1hrC3Q0kK4JCGobVKegSkd02zhOBQaUFFKnQ0o46eBohlh8VV-MoSZAOcB84mgPHVGQlLpdGK20JbilekvaHWlNP9y9wuwiCurDC9TcQGr247yqHrz5tONXldGOSElI2lG9RhvlUJXfVioJ8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e7b14962.mp4?token=lMrG8EpsZQmPTUpgZ4wzsfRQJqdufhpUJTBUfTAEID6sm30KMKE1mAKvdgH-cxmmI3wB0fjODOCKTvWTtjK85E4sQFPDBCV05L4PtSCl5iIIsjuQu9nV7h5rrKE94-3gnbX_sDkblOWbroyVSDMT3Ng4mXh9XziLNfhpgvQrbWMJaXY_GwMrhULRN7bbcyp4ck5N1hrC3Q0kK4JCGobVKegSkd02zhOBQaUFFKnQ0o46eBohlh8VV-MoSZAOcB84mgPHVGQlLpdGK20JbilekvaHWlNP9y9wuwiCurDC9TcQGr247yqHrz5tONXldGOSElI2lG9RhvlUJXfVioJ8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتح عظیم در راه است
🔸
سخنرانی حسین یکتا در موکب امام شهید ایران شهر لامِرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457104" target="_blank">📅 22:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noAcn8SjWpeJIaFOWM0ArjOqZZWvEsHHgGw14Z9vuXTbKk912QchXBvjiANKYOV9WS7zkzTEwKivJ-y8tbqiTa7PquWsklkXX6c1WmsDCnjRFPoEJxPWZ3pxOIgEllOs_ho6EF-EpVH5y6bI1roaw3Zs0WAdZ9i1q_ki3IT8l3EfZJz5hI8jK3blX-F1bbqQHyN1I8yO8YqrxIcYjKUxDFGDW4r2a0AKehDLZTxA_cDMiztWvnvjCPmJHmK18glxZRm5jfrSX3Qpek7Myku0QORLhGKdzM9wQUJkRboRXPz7mycngA6CWSDaQ5w6T-jQkYwVioxuxmDJg75iqdaw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگردان تارتار گام دوم را هم محکم برداشتند
⚽️
پرسپولیس ۴ - ۱ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/457103" target="_blank">📅 22:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4808bb6f76.mp4?token=kN_WiElumAE3MSglhAcoC641TjvBnCa5vVth30Jq-k_DlRbWMTw2CBmUXYFXE52BzUhwqkoGsAvMXZgZwK6LUw6XqSSDbAmvK7tlW490VC6WtR1PvcPQRJv7dR9ABnLuiS03yKtdfeG0Ks4-46vMGwj1Uv4ljqP-tV3H0Q-LYXxnHmHf2pDpdYCxsXhzHbx2R0yTtwe9fYazKCjef0gscGEo5CHWDve3YYQolObJ9HUZbRgK7zXaWW8nhUAkqXpgIPVX_wtpyb0F2P_bCtEpcFW_-zVB1y5h7qkSs7NxJjVInTWbyuVoS3yHFhdLyqRG1KLNY2knVPBPoFFSJtQcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4808bb6f76.mp4?token=kN_WiElumAE3MSglhAcoC641TjvBnCa5vVth30Jq-k_DlRbWMTw2CBmUXYFXE52BzUhwqkoGsAvMXZgZwK6LUw6XqSSDbAmvK7tlW490VC6WtR1PvcPQRJv7dR9ABnLuiS03yKtdfeG0Ks4-46vMGwj1Uv4ljqP-tV3H0Q-LYXxnHmHf2pDpdYCxsXhzHbx2R0yTtwe9fYazKCjef0gscGEo5CHWDve3YYQolObJ9HUZbRgK7zXaWW8nhUAkqXpgIPVX_wtpyb0F2P_bCtEpcFW_-zVB1y5h7qkSs7NxJjVInTWbyuVoS3yHFhdLyqRG1KLNY2knVPBPoFFSJtQcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمزمهٔ دعای توسل در جوار مزار نورانی رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/457102" target="_blank">📅 22:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457101">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b984e842d.mp4?token=anJTfaWrK2y5wkzWNhkh-SdSGbtnkx-a-oV7A1fcEkllmgwLmm5FywrqDjPacnJ_ejBOw7v1EgQgk-xScx3384aAUi5pGnMdEc0lHcKPz8npiX5hZDL6XefjMDE3iGaUjpZOpBSo1DZG5zQsicV-vM9p2_g8k5Zdo-RrkjlH2OFqJ84MN51JnA-x0PSzXS_Csqqb4Q0Bd9bTl6nr-G0HwiqezqNICDEXyMVRzJKUYgBJ8M_I--uCubPBWfVgshQQ1UwSHbl6KgDxhR4nLhQ0uDeoRqaozxAZhkEhFvYboR04kAPuYcyW30Xtc2EEfUsRgWmHIYWYLA3wT_j5-Pcjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b984e842d.mp4?token=anJTfaWrK2y5wkzWNhkh-SdSGbtnkx-a-oV7A1fcEkllmgwLmm5FywrqDjPacnJ_ejBOw7v1EgQgk-xScx3384aAUi5pGnMdEc0lHcKPz8npiX5hZDL6XefjMDE3iGaUjpZOpBSo1DZG5zQsicV-vM9p2_g8k5Zdo-RrkjlH2OFqJ84MN51JnA-x0PSzXS_Csqqb4Q0Bd9bTl6nr-G0HwiqezqNICDEXyMVRzJKUYgBJ8M_I--uCubPBWfVgshQQ1UwSHbl6KgDxhR4nLhQ0uDeoRqaozxAZhkEhFvYboR04kAPuYcyW30Xtc2EEfUsRgWmHIYWYLA3wT_j5-Pcjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: ان‌شاءالله مبلغ کالابرگ را افزایش می‌دهیم
🔹
نظر مجلس این است که کالابرگ برای دهک‌های پایین افزایش پیدا کند و دراین‌باره درحال تصمیم‌گیری هستیم. @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/457101" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457100">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a70545bc.mp4?token=bmZxs0FqCRdL4xOMUpEHaUEhCTdAEtOhPAsGI2XKBpISGKbWhg4LgnVLdOzDbnxZASJDE-HbnnvKZb3rJecyIFD-b-MJVU3jGWsfrXEbQ6qAZT6pah-0KOxolhJId7vz19AW6xWkMpAsqUTLPeLYFOsa2C2BDCXwJRutgGRyDPjg1h4UndfEu36_R2G1jWjIAt4KVrATEvSjwis-lsqtqwFx-JogBLM88KjwOttw5amhmcLoKf4n0PRCvu_AyzOh8ePEFH6P7VpC1YbIX2MyQszhjzRvg2it8uwchKaTBAEspfZsi4gDrGSvkjhluOnQmCqPoS2kJ21B0v3jIKdmPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a70545bc.mp4?token=bmZxs0FqCRdL4xOMUpEHaUEhCTdAEtOhPAsGI2XKBpISGKbWhg4LgnVLdOzDbnxZASJDE-HbnnvKZb3rJecyIFD-b-MJVU3jGWsfrXEbQ6qAZT6pah-0KOxolhJId7vz19AW6xWkMpAsqUTLPeLYFOsa2C2BDCXwJRutgGRyDPjg1h4UndfEu36_R2G1jWjIAt4KVrATEvSjwis-lsqtqwFx-JogBLM88KjwOttw5amhmcLoKf4n0PRCvu_AyzOh8ePEFH6P7VpC1YbIX2MyQszhjzRvg2it8uwchKaTBAEspfZsi4gDrGSvkjhluOnQmCqPoS2kJ21B0v3jIKdmPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: ماه گذشته شتاب تورم را نصف کردیم
🔹
البته این به معنای کاهش تورم نیست بلکه شتاب رشد تورم گرفته شده است؛ یعنی احتمال می‌دهیم تورم این ماه با ماه گذشته خیلی تفاوت نکند.
🔹
تورم در کالاهای اساسی هم مربوط به حذف ارز ترجیحی بود و طبیعی بود. @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/457100" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBoPNUUwkMFmUZhczZYK_FR_eXDSqT7NJSLv796DPBYOeQh3BZ3F28zBSpWBg-TDnQYCPGYrdCGcMi-fgAhLjeCcIYyTFieu1JLnSh41MlbCJWy0sp7dMdxLcjJaH8dcoTcBgmQH3jHW9sfI02ZanbDv6pXpyT5TGTsjx2iQtlnQlYXL2POwy9Wk8SDhhIIOVBhaC8ISGT1sj1eOlfRMjPXS6HBCCNFcnBkyzCVPFQY_Rrar3LtTSccgjJK1Y5e9DWXwrukfh5ijTekpvc8HJC3Mo1keCGCsv6v9hmUQlx-cDFTWd2IeNG5VZHx8iQhXkpSOaINcqvtnGatLipkwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RD73j2cpEpCNtIw5KylRlnikMqxAtrAnXwJ4zf5ETAvbgJ67P8Fbh9hDwScp3SdpRBA9h6jHucaTvyT8pH2Cxsa7YQvHyFDE1BgK1tUWntLuk-k9n1eXq4PkAOA18FhKwz56Ql1pxthmuwMNbGJ0EMM6Y66onOF1QZ5ecHKVFE794JATspYS-ncSqaL9t1jXoWkfuJgPG1a87r1dATMcf7sDvLYjVSJ2WTevq_sOajchliz8mGg0TzqXukQs_ltBLGmqUFPZDgMmnLutKVLoQ2Yj8kJa1mY2ho7cNPv8DlgtXAWgjyxUV7XrfbQgNubrE76lMl7jcxgJXrV4DeMD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiGe2IrbwDyTSyHWG3ab9LzJPoPivlG3C1pYW4uPJ8WzoHWz4CKQOmAdXQ9yEZQ6g_rNbeHdII27NNkHkVNIZltTjxHVQo8UOMw30xGmsVG22MJTxA80HbddVHv0t9zgMyTPIyJxRWW7BvF2MIBikf5AWnRyW3pRBAKgwk5qiY8O_AG0G2_NGUM3MKunwwoyrd_4cMrXhH6IG0jJgq_yLKz-wnH-X7YRXChf1LGLk6vUk9IufT_CI67zmMJpjMMz9CTs1UmSUSw30D2uR1xkVibvSnzgS4l_GhZtUDpOSVze-nPtqe_3GaxqTrk3DfaYoey0BYKkuuTniY4mcyc8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fca1k4X088f2OpkxjrP19g84lEqiYfXPcQOb5HhFiXK65iZBCCPba3h-FecevF4ftVhJf4FNj2gOpZPG2rbFAwEkNNWHeVigXLka51iCpEKdbkexe1tVnD7ct4knmQG951CSINOQPqK-EK4avU8D_wBDpeUlWY7ZZkU08GhP8d-dw_YIERjy7IC65F9JuaEmWoDpfa4oPXSg-Rl5TT84NS73x0no3v_U0jO-z0cQqGrD9sZtXOO9klwSwzCBcJ1P1ttS_O8QkWPHAK30q1Hq36V5-BB9NH80LZSfVt30o78ZM_GXsuCmBt3cGDTG0fPskWrW8I8esUsF3w96EkHrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdR68_bubjHUR-SkyiWhxdbLws7kQ2T6wkNZU1e5MX4dt4zkx5mVrBWYCCpYxHC2eQBO6UvI51tzPWZJajwjra20750_iP5K4sQAkizlQkSp07R0eRNCRAlIcMcDBmKEvwazLMhs9SgJb4eJo9bJ_ecW2q-QW5ojJ-z_iWhNVIE7mXdmb3VVSFZDdssxJ9RhbO9dX1YlNS6-foDZIs26gR47HBNyl_OI9XfbV6dWF4Bln2iYaxZlZzSGdFKNSNp26vHjczcZBGg0EzxtACoNjnH7JMNuFW2QGGrJ8EBp-eDawnnSRZw3HIIEZFMYU7IrqCdyBZOraAdg_kLyWWD3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF9m6-PRgO2opEt8eoLMEwvfQJ1sysTFDtcmSGxBEyolezhOGzJsg1mDxU9wEUwvv5_EnmmJRui7DwxLSDNzpsTNTHT-mOq_whc5Pct8YOTs2QtJUPyEmM4A1UiXzY-D2ETaFXwkUGyxRIioZ_OVWQioX9BdtgHhblw5HLcA7eWTvDcfQUhWoPYk36HtCRRsvlQTwTXJ4LngmjmSuHT87A9oHG7lXewSUZ-h9WGekKMWG5_t8Gh8D0AIqcCGgEav5K-C7zBub-UUMVZqIvyIadEvKQL60PYiVid24hosJ-DWyyD-F0ISPm7QjmDvQUDDFxNG6xa5cTUui9H_87fetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PK3FZkBDC2XKI__TvL0QtstIsV1uAzniPjnay3ur8MO9Oi2_pXbr9FBalHAeM4pMjYsVZxgAZoeyXtJwFS5bE_HusXCFSamrA299bFEyhlzTketwre5NwGI9LyUx45yzJbJj_diMq5az9ONlPun_mZ5BIlE84LaQonw5jbjoFRc23nJVmNwMyUlp9jWwxUS59p1DUMVFDf8jkevK9o1JKlferVRMdLwOxb0pMpKy892v9ftMksQXfd1exyuQNk9CvXN3GJJwA_dM42znpb53h2YM2igyfML9G7ZGL7nVUOQJ9HQeZ4-WsQaV-XhLS3NiHRFxmB0bRXuZePJZJADBLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت چهلم رهبر شهید در قم
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/457093" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf0c47651.mp4?token=ZT0wKivQvoIwVE7Kl4u6PqrX1mdTZjhW9ssC5gJF3rwq2MX5xGS048BwYSXU1jaiMs5iRY9IakxbIE04ZJ2PIbpiNddFAxt0lrB3Aww4SggJu3bU3k-_z1EfqEVOdmlwLc6SITsW8muT2s3IDZKqXgWfXVhu3YJgWQDpLVz1uwMG-hM37pz6tg7i4IdkInJtTCklRJfz-yfI9KrS-7mFCarHcP-5he9sfUrq0FtLWj4rhLF55CjBFiCnc_os9yY4NXMJBSrpvlpjpoD2AS6lIYlt4cldjhCCEEXOenvfO9oK72tJLJ9yo92AWRu1ERvwu11qXf2Qi7ujVkr_vnh4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf0c47651.mp4?token=ZT0wKivQvoIwVE7Kl4u6PqrX1mdTZjhW9ssC5gJF3rwq2MX5xGS048BwYSXU1jaiMs5iRY9IakxbIE04ZJ2PIbpiNddFAxt0lrB3Aww4SggJu3bU3k-_z1EfqEVOdmlwLc6SITsW8muT2s3IDZKqXgWfXVhu3YJgWQDpLVz1uwMG-hM37pz6tg7i4IdkInJtTCklRJfz-yfI9KrS-7mFCarHcP-5he9sfUrq0FtLWj4rhLF55CjBFiCnc_os9yY4NXMJBSrpvlpjpoD2AS6lIYlt4cldjhCCEEXOenvfO9oK72tJLJ9yo92AWRu1ERvwu11qXf2Qi7ujVkr_vnh4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/457092" target="_blank">📅 22:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eab130c1.mp4?token=tnFY_fT0jNkjfJkjY_Bj5YNP40um6qKSv4CQwYGvng-SVY8jt2uhBMtDEeMLE1Y27kfnNu8_-onnhHYaPXirNsfo_AnSjyGG7HWNLZKFs619nHTJOC6pTcO-dm7C7PlcyXYZNQ3foZkZl9kBCHx66uRfd6eUO44jQ8XG4F_91DaFNl3h1FX2T_vMKLbrK7lQjpevPPrccQSjlfvpTrs15KvbjTl1gnREN0WU-OS2lSgES-HmftPj2P9n2U8x1SUhisrdS7vTA6ZEajO2iW22a8jYBAgLRRVFvSvCBkIR9vzZz9c-BtgWNop2FI0M4gVlMDIn5l9KOokIfxdm2iyZNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eab130c1.mp4?token=tnFY_fT0jNkjfJkjY_Bj5YNP40um6qKSv4CQwYGvng-SVY8jt2uhBMtDEeMLE1Y27kfnNu8_-onnhHYaPXirNsfo_AnSjyGG7HWNLZKFs619nHTJOC6pTcO-dm7C7PlcyXYZNQ3foZkZl9kBCHx66uRfd6eUO44jQ8XG4F_91DaFNl3h1FX2T_vMKLbrK7lQjpevPPrccQSjlfvpTrs15KvbjTl1gnREN0WU-OS2lSgES-HmftPj2P9n2U8x1SUhisrdS7vTA6ZEajO2iW22a8jYBAgLRRVFvSvCBkIR9vzZz9c-BtgWNop2FI0M4gVlMDIn5l9KOokIfxdm2iyZNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/457091" target="_blank">📅 22:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e60144ae.mp4?token=KyuODHTtjcWrq-5iTyxXkntEti9J8A20zb35iAkLlPpadTRbmQ63qkJVUkzNBv49WG-HVlc-BS96JSWX4UaIrFGFny-RlJt5EL_-rtRZmSV4l-FDgxGOpT285pDU-BJEVvbCjw61L8DJHW8HCVaIXLX0NfmrGN8hZT5a3GKcQo3htcPOvCShBlB5vykty_K3NeHoloCT3O4rIsVyxPpubESGJApilwI4yQAmL_1JtVPmUnRnGnEHMX_P31kVSv0H4ayBdD3rtuC-nRrgGIh4hHp2jKDLtr520hvR_y_RE45KQXNhRMJ5fbYh6lwFd8Vnlh259E7YTzMx1dqfOLug3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e60144ae.mp4?token=KyuODHTtjcWrq-5iTyxXkntEti9J8A20zb35iAkLlPpadTRbmQ63qkJVUkzNBv49WG-HVlc-BS96JSWX4UaIrFGFny-RlJt5EL_-rtRZmSV4l-FDgxGOpT285pDU-BJEVvbCjw61L8DJHW8HCVaIXLX0NfmrGN8hZT5a3GKcQo3htcPOvCShBlB5vykty_K3NeHoloCT3O4rIsVyxPpubESGJApilwI4yQAmL_1JtVPmUnRnGnEHMX_P31kVSv0H4ayBdD3rtuC-nRrgGIh4hHp2jKDLtr520hvR_y_RE45KQXNhRMJ5fbYh6lwFd8Vnlh259E7YTzMx1dqfOLug3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ولایتمدار شهرستان زرند در خون‌خواهی رهبر شهید به پا خاستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/457090" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1bJBBFPktehP1hMTQ7GiW62vw25Y5fREQShTYEuzn9081EUZrLG5Xw-fMUOvDH264W5iMi3GgfNLz9MpizV7G8eDQ1API4Y-dx7ZN84kizBiAoIVuhCo-DoglCose1qehKwk1-IcsGAyXtwiRqdUY3qS_w9yevkqI2nN3MRXA6oUdNxkq0wZ649q5SBBWTaauvHd9aLgBPUyYNsKBpSTjC3N8Hcr557VcGvHkyAMc99NbvsnHAH2L6uN6i8LyQ_95hcW6HCKGn1J_i8rsTYeimNH-K6d2cqu77br9bwbRsEIf_fYA4-qrZee74bA5x6kj6kNO7XCD7hrl78svnC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4XEmdW3MY5S5VZGdSYqSRDQB4_hx0EVbraXZ1aCSgWGQ5DaYwpwxc1yJDcY5LIWKQoPf2ByS39D5Qf2Ostiz7N8bTJS3TU8ZHKpGjUL03x5bBozlKYBL17R1TfAdT_sxeBS5LpPy26_LmkEqJpZV8KDbGd9kZ86UZKssuQ5BDg0nQrcfFxShcJUwnZ5iLxKou7RrsSGiInomCMMibFPV5iNC0HUCbBw4aLfVptZrH16kERF-_40BraymoF2HLBNMOWm4fkddd-zOkemnu0DBZlj2F9Q10WnyZ7sl1gO-nEPssXkKEyQgupRJ9_2-DXEswy9jLxTrHnmQEpnYmaoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXALpNDvb4lktJWnOkPoYqN1Aetb6WpKnq1BEZPwljFIs1RqaWOZ0H_Gll6uPsDWw3kzH7U3dE6LjXJFAsG17InhRGV54KA11RpPgKzg7vNe-wsidzBej1BIabDKiDG14tyNipQAmwrl3SVh1fcKbCar4zVTd-1O_Of95TEDutItejBdb99pYg4POPJKzgxGD7tuOnG-dhezE-5ZFoGYtD7SB19NTO3tybYXgX9gKZgvC4wyVkdSBiMExAtHF2No1yqWytp69_2s63r4ADeVnlCNbgN_zuEP2tXHcU_6mOodrBoSKgf_TpF-4Z5KjSJerShyWVr7q0jYkSJ2pwy8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfhFC9r8RvNnMV-gaofYpji5ewNqhK600NJ_3x4Ngrw6a522fXVrvJkd83Sbn2l0bMo5rjVKqqiHTgpXow7dVpzWxzIu_qaFeG46iqEb1WHGR1kIoq3qsGhO8rgQwptyxlVrSnmbsLC5ZcbLthpJyjYZhEA88H2eaGr5mAW_J6R_AaISs1If4mOFFAdH8Xvo7LgNfyIn9Dzxogeuojma9rktrxVagxPCbmn_K1Ut7gdsj6ItYLnbwnWfUvBeJ_8qE7ElzgqHeFvt1mZovWVQ0JqwtBCGlCX3CpbO7rjiMHAt8FgIMwJjdCUDqYUYP5ONcE5860Wg_tc7C6SFayM9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRvZuxs55Fn1bPgg03hpb56VibpWomM_jbncpIYZPSVOwDaMmx77cut72tSnSpiEWkTTn3mOr0tfeWhgDptlag8LPyBnlpBsZxSirhzQ3OCFhKkmBiZM_9Xul4oGuDVGKBZIbrtMhztJajA0nYKGHuB__I45Mau-UNuXK2Jfid0gw9TImja9CKHQwwbztW6_EGidDJEMEgklBTCbRcHZXxNGJkXCFu8-ZGLEvYTP9mXIMIVRwYaLFX7T8zMPlcu4x6k8-8dYKAFiuLVRipHGc_6YyS8I04JsXgINlClV1t-D1L5Gz1tkUzfCmFUi-7NR9v4OUdka2Ll-_N8IWAf35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kehagCyE11LK_7VucJEjRbITC_Hcuof-9oOXOu8IBsNVCXCbjXshRqC0yi8UDxacolYl8HAoNI2yrxpPGq0q8vAXvLItYzacVDVJz45HmISY1UyRB4ypNhrV0lIwddLhaHQshkBn6G9idHRMfBjPwRsxv2LyO7DdpJzcL2i-M_JOWBg4mKh_kgQfEB0Wle3eWKkCkjx0myAwumT-0kyhqoqEG0eRciVAVFrb_VUZlH4nh8RiJ32Jv38MUt2zRxITZ8uRh5lfM8_H2CQ1D9Qep9C_Y0EHjy376s5yy7qEVDiLap_zbN4pwAT5pRPp-0XVj66BzEBEz86FdNBBN5l52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Apb7zXl3Yh8-275ORAaWLthyGGu523PHbNoMfkEhSJ09aPncSafA5m8-YoGlNVaxpHoLXXbHNMIw3lS-UMhT5DoMj2qad5dK9R3WmYN8G9oLz_1VLVfKBLC8fRXda0vSLoW_wpsN9K3mc64aT5TdRfy3rAqdBs1N8h5eZ5ghIBK2GJzoKKC5W7nnJR-bppVu3wBzegsjW0kQEsU84L-Epv5glTkv1Jjisk13nqDCGOSDxiRR6qnjnigovt4B4iVku0fSY1bEfqpKcLpo5L9tb7o9LRlWWRGPUiZg-6o4Eh3oOjAjE3fEWvIAIjHER2RDdfz_fbG_aVZjltXSDddy0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنواره «ائل سَسی، کتاب نغمه‌سی» در ییلاقات اهر
عکس:
مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/457083" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457082">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80b6cefd1.mp4?token=YLtp_xh8YiRfdvdMGSyehRwjlg253uUZhgHBnvk63hwl_X8xkRNyNLZshNrpC3-tv3TWT_AM0SL5LVsTts41kzMAht5tBvXcAF6UbFlTpUpkDuCGUjfFa9_Kzjliy7fIecuoZvFXQarOuFkFMatBGw3WKUMqeAoj1t0piIcSJMmzjamRhjS3BtDX0oFaOcSg2SBNybZ3mkvZNhN4Or5fq1cMaMzAtpDuzUB9uwr7KUQHVjcfEM97IL5FVC78gDftNMHd4JqMNsLZF9sbE0c1-CRaWCBvr_xuedj1XHXatyGxrGbu9qd0FsA_eQXeasCcGMZ80dO4-KI-UbL-PUrIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80b6cefd1.mp4?token=YLtp_xh8YiRfdvdMGSyehRwjlg253uUZhgHBnvk63hwl_X8xkRNyNLZshNrpC3-tv3TWT_AM0SL5LVsTts41kzMAht5tBvXcAF6UbFlTpUpkDuCGUjfFa9_Kzjliy7fIecuoZvFXQarOuFkFMatBGw3WKUMqeAoj1t0piIcSJMmzjamRhjS3BtDX0oFaOcSg2SBNybZ3mkvZNhN4Or5fq1cMaMzAtpDuzUB9uwr7KUQHVjcfEM97IL5FVC78gDftNMHd4JqMNsLZF9sbE0c1-CRaWCBvr_xuedj1XHXatyGxrGbu9qd0FsA_eQXeasCcGMZ80dO4-KI-UbL-PUrIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است  @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/457082" target="_blank">📅 22:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">پاکستان کاردار آمریکا در اسلام‌آباد را احضار کرد
🔹
وزارت امور خارجه پاکستان روز چهارشنبه کاردار آمریکا در اسلام‌آباد را احضار نموده و به دلیل «اظهارات نادرست» سفیر آمریکا در هند درباره وضعیت جامو و کشمیر، «اعتراض رسمی شدید» خود را ابلاغ نمود.
🔸
طبق بیانیه وزارت خارجه پاکستان، اسلام‌آباد توصیف جامو و کشمیر به عنوان «بخشی از هند» را به شدت محکوم و قاطعانه رد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/457080" target="_blank">📅 22:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a5db559.mp4?token=JvTQ8RWZ_RvmBoKKEXvNHObC9llB86K6LvpvRDVqGXFDjMdG9WBf-8smWh_5hg7knVv6FCeuWT127-kY4vcZl5Do8J1OQehSOdNz_-UFDiQbs1Q1dv6vrhXATsKJ5rcZtA6FaCZDNHTbKzrBSjuy5YT9eNshyecuJFA4zcp_GiAwI-iqZEH_dpszXdMLHKYlbxxLqjNi4lfHEr0M0KSf91F74heC8p_uu2VZqJW4gRk8r6GbdiiIpyqiPKsph_A6j7MMQjFIbAqHiiGPvtemIpyusitA1epqTkd7htlA-GpeWU5oKFcTVr7gQ6isco9kQNmPPnEcyw9xPQ8IUurVbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a5db559.mp4?token=JvTQ8RWZ_RvmBoKKEXvNHObC9llB86K6LvpvRDVqGXFDjMdG9WBf-8smWh_5hg7knVv6FCeuWT127-kY4vcZl5Do8J1OQehSOdNz_-UFDiQbs1Q1dv6vrhXATsKJ5rcZtA6FaCZDNHTbKzrBSjuy5YT9eNshyecuJFA4zcp_GiAwI-iqZEH_dpszXdMLHKYlbxxLqjNi4lfHEr0M0KSf91F74heC8p_uu2VZqJW4gRk8r6GbdiiIpyqiPKsph_A6j7MMQjFIbAqHiiGPvtemIpyusitA1epqTkd7htlA-GpeWU5oKFcTVr7gQ6isco9kQNmPPnEcyw9xPQ8IUurVbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/457079" target="_blank">📅 22:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXBUZASa1NV556BtfKJ5d5o-7bZ_-A64oBAkRSC__g4EOVJwThgtzUH7knxILGmjOyhna-FDYa_py3F9uY_8fA69t3zRZRXl3BMTK59DuwQ1KHU-2ZBJzSCTZ0BJ_aH2dv2Focyf-meEEBs0q9c8Ou38Wh_1t8bFKfArJrlLa-LTR7xlqI8Y1ewDMgZMFI-_FLNjYGgPdvCMgDh40qzEGA8_fNpK8kFJwb3-bOs8Cmg3juv21rBAUptf69r8uGfbhgQKqBvIYgLs3-xKTX7r0JjENtuq98KsHtJlP_GLBuVDiEW5C6KiiWfxVvp_HKrEXzEHobmhCUa4DWF14vQpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با عاصم منیر
🔹
وزیر خارجۀ ایران و فرماندۀ ارتش پاکستان در تماسی تلفنی، دربارۀ آخرین تحولات منطقه و روندهای دیپلماتیک تبادل‌نظر کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457078" target="_blank">📅 22:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjM3Xkce5qhp9-6yfCjEFrmTRgUGfEs-3fkR20-lRKUEWsKiEAdkOHDhehln2MHsvGXsSwj8T9gRM8lPpfI695xg_qq66MVZXkWFrPmionl34_ePlsZJNxrsEos9mVLcSzEOjujfHSPDwlijAsxY0GV9VQ2fs6BMD-XPfZZqQCdJQZLpbPYiLjTdFkeCyWQ-7pcy_cEzfD_49Tte1CseAXbyzi_jjxSqmN_aZKUFlFEeb-aSBvn8135vTcQp5aJjrw4tRslQhbZaZMHKzRtfmEhfWxFVirIUtw1zAU8gVYWwT0yWI5ffRXs6rpbWAIUj6408d5haAO_uU1usSJug-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ایران و عراق دشمنان مشترکی دارند
🔹
رئیس مجلس در دیدار با نخست‌وزیر عراق: ملت ایران و عراق هم دارای اشتراکات جغرافیایی، تاریخی، دینی و مذهبی هستند و هم به عنوان دوستان و دشمنان مشترکی دارند.
🔹
ایران و عراق با نقش‌آفرینی منطقه‌ای در بین کشورهای اسلامی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457077" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvmWdO2fOay2TOn6zVG5Xvv_U-ztHsPbTaZUnd-vtK1ZLOlOQCLOSIbXP8y1QWSTd9hqxDHEkiK-wRV7Ap3fOf9fjHh2ctu7qYHhstd8ZKqGbI9K-ZQybkkQovDqk04yw_sAJs9S5dGEK3vF8kcCcnAW5HcrOupEjeQ7UnO5KLARqJ-ao6w1sqR-pso6lbcdl9r2MublcDQo1HGhApUmBwsG8PqTfOJZ2tRCMz_16bwuIXB-2ZcequeweM4mlxrGN04qTsfXHgQiCI7H8LjzGwSjv2jdvPrsyPu_aU2cywuaMtu2Zmyp2Zr_QTnzHV-HnOvE4K2UH6PFViMCu7xqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرخ‌ها با پیروزی استارت زدند
⚽️
شمس‌آذر ۰ - ۲ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/457076" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495a4bf5de.mp4?token=i_YxV5q_M3zqfdhU72B-Ioozgs1TGHAjJByLHkDPbEYNfkP5szb63DeFyx4MxhMLgwZM6oCmwCvdrINHcpeDqvBemGrOpuB6z463u2wm8vA2B-NOxPsXsrrR-Nsl31OIrH7gFdozQsl5L2UfSYCoSgKGJJm8xm3965aLp1vtBH2f6cKQasFkDEH0Lq9WkR42yRrOFSJEIVbUlWQjDQT1Pi4g7ohK8Yv81VGvBfXF36P6fm2umB18P6I8SEBTs6xIz41OXmbUNhcbC_0SF3clKadpQuKAY9bR9b9yylXUHnGd7WC-_thTgpqeHFt4X4tJzP0Yj6mhS9Gj6v_V8QX7wbjtgZO2ktO66q5caBia5SqLPf5qaqJmq-24ka9odl1_G6cZ9VueehShUCVkFAerlX7L2PuqPY3FW-t_Grf1O7v3Jmh5ABC78-RzL5HDfR8opBUx0LJO8klI_cb98KNuUryqSrzNgBNGU7j3serMWzkxtkFA4iSQLfu7e8AmRqYCvtWODlgJ9pWWBa2HSln_EraouoQkuf8k9cMVIa1oaxBTHlqAxRe_jTNhwwbRfFy94tdXWgKMJLVxxOgAD1o1nk0tBLbQNF2f9Pu_8IiLltdQO64_HR7qblAsg97Jugmzt56EtwDUnkW561guHA7Xr31dbcGfXO9wyomxzNnp1Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495a4bf5de.mp4?token=i_YxV5q_M3zqfdhU72B-Ioozgs1TGHAjJByLHkDPbEYNfkP5szb63DeFyx4MxhMLgwZM6oCmwCvdrINHcpeDqvBemGrOpuB6z463u2wm8vA2B-NOxPsXsrrR-Nsl31OIrH7gFdozQsl5L2UfSYCoSgKGJJm8xm3965aLp1vtBH2f6cKQasFkDEH0Lq9WkR42yRrOFSJEIVbUlWQjDQT1Pi4g7ohK8Yv81VGvBfXF36P6fm2umB18P6I8SEBTs6xIz41OXmbUNhcbC_0SF3clKadpQuKAY9bR9b9yylXUHnGd7WC-_thTgpqeHFt4X4tJzP0Yj6mhS9Gj6v_V8QX7wbjtgZO2ktO66q5caBia5SqLPf5qaqJmq-24ka9odl1_G6cZ9VueehShUCVkFAerlX7L2PuqPY3FW-t_Grf1O7v3Jmh5ABC78-RzL5HDfR8opBUx0LJO8klI_cb98KNuUryqSrzNgBNGU7j3serMWzkxtkFA4iSQLfu7e8AmRqYCvtWODlgJ9pWWBa2HSln_EraouoQkuf8k9cMVIa1oaxBTHlqAxRe_jTNhwwbRfFy94tdXWgKMJLVxxOgAD1o1nk0tBLbQNF2f9Pu_8IiLltdQO64_HR7qblAsg97Jugmzt56EtwDUnkW561guHA7Xr31dbcGfXO9wyomxzNnp1Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این هم جواب مردم به گزافه‌گویی ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/457075" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrigciQk8VZCQQ6RIKSFFLyofJyDNbrtGqhg3avSxRW_XNoMrHOma-epTRnAPi2uQpMPKiDtld8jvV5_fuBqPleeBs2ELag6dcSd0DjSENPic-o3kLiLDT2JBgapyi5Tcyh6anROnWewaIsu4swvJPzT8CnrkGThY8rz2OE40YHIOpyZQ-bUW1eQOUKRIJnctY3aTqveqXS8U8bdB0uQyFfXFar9ikzi1R_aGXwp9nSyzgSLWCksS2xqPUUUiCLMeAq8jgaKX4MgpdMVTiKGuVzpBAzxiaylrkAn-R4eNcMQ4mE1mQkhrimGNdN163jT8eC9R9Cs2YQhhTOAU9DBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمای ویژه از مزار نورانی «آقای شهید ایران» در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/457074" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زمین لرزه‌ای ۴.۲ ریشتری حوالی گیلان‌غرب را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۴.۲ ریشتر، شامگاه امروز حوالی شهرستان گیلان‌غرب در مرز استان‌های کرمانشاه و ایلام را لرزاند.
🔸
تاکنون گزارشی از خسارت‌های احتمالی این زمین‌لرزه اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/457073" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od5NGV7XBoN9Bp5y54yJuWW7vZM7KWz91n_OooyNNS5ze6hmkS784VBWk1I3U0cb2Llw4zKfW08YlAWr5-ZpGN2tEICMrxI8ZxrZ4WqnP6rJmqNHcU4dUi9cRK9BF7swTj7vsLy9ruZPnyJT1beY0MjRdo2cRMD_fnvF3FguIrkvVH-aK34HFmtkHk5SUj5Mvb0bEtpWLqMtmmq7GQ95VU0Np7f0_2jhmN68_XO1sz_8TcUfRdSrMZjgXi1987Te9os5o3WCsDjCMt7CjDopZuDAcKu95lB8VTvMo172mwA5IUmtfProQy987CrFQgG_DNMofiqd8GCsm27va8Ling.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قالیباف با نخست‌وزیر عراق هم دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/457072" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d316473ded.mp4?token=f7ydUtKiGm81diCNDdYxh0pfA9zSJawH8oWuQKXIcneoHaTCnz3F4srrGYQmITpfofsd3cKmbRq08-aM4VuXwzh84o_2LnfUqzkmJ7gTtKKCPc5w5PZGTC-R6U55oPYp7kFiQjT5Mde7C4QWr6e8kDafYEAkY5FefE0zJrOerJT38iDArVmgrZTG3X9K6t5QXa2N9ahN1cBmLrjQb9DWoG00w2C2nSEMA7wgVtMgwFZ33Re1lEIVy2a_xlWxgf1ggwYGWtZxA22YwskyuaWuU7Xk1LcgdHYiSiewY3X0iKMLHVGS_xT8slUqTj2xUbOstEK4lM-4pP5S1oBVq06t-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d316473ded.mp4?token=f7ydUtKiGm81diCNDdYxh0pfA9zSJawH8oWuQKXIcneoHaTCnz3F4srrGYQmITpfofsd3cKmbRq08-aM4VuXwzh84o_2LnfUqzkmJ7gTtKKCPc5w5PZGTC-R6U55oPYp7kFiQjT5Mde7C4QWr6e8kDafYEAkY5FefE0zJrOerJT38iDArVmgrZTG3X9K6t5QXa2N9ahN1cBmLrjQb9DWoG00w2C2nSEMA7wgVtMgwFZ33Re1lEIVy2a_xlWxgf1ggwYGWtZxA22YwskyuaWuU7Xk1LcgdHYiSiewY3X0iKMLHVGS_xT8slUqTj2xUbOstEK4lM-4pP5S1oBVq06t-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال خوزستان به پرسپولیس در دقیقۀ ۶۴
⚽️
پرسپولیس ۳ - ۱ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/457071" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeadc87d4.mp4?token=UB-l1XzmMmVCirEEfFtamvhE2k9LmYImsXceljUSPgdKxje4-UM5hWxzB9vjOiyTYPBnkRcKAPjrLSMUBP3gnrz1WOy8zyLn-BOyZNp2LPT-r-ruF1rUzJsvu1cRVviqIJbOmBJ0z8HCGxRBhQzTkgE1cE3lKmTVkZrKvh9OHFz2ZRv6-tw4sdwuZLufsdWS2GQGS_MtJPvVzixWDVuYHCfOcxtxjCMmzc8etbr1t03Lcq8JOVa09io4CxwEWL7bSgzJcLPwPA8YoBxkiQIJ3mLT3_WKdK9nYzJ37EdvUKh_FejqeW6morjrw8FOcA1-s0tUS7ooPMDUGl7LQcdzIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeadc87d4.mp4?token=UB-l1XzmMmVCirEEfFtamvhE2k9LmYImsXceljUSPgdKxje4-UM5hWxzB9vjOiyTYPBnkRcKAPjrLSMUBP3gnrz1WOy8zyLn-BOyZNp2LPT-r-ruF1rUzJsvu1cRVviqIJbOmBJ0z8HCGxRBhQzTkgE1cE3lKmTVkZrKvh9OHFz2ZRv6-tw4sdwuZLufsdWS2GQGS_MtJPvVzixWDVuYHCfOcxtxjCMmzc8etbr1t03Lcq8JOVa09io4CxwEWL7bSgzJcLPwPA8YoBxkiQIJ3mLT3_WKdK9nYzJ37EdvUKh_FejqeW6morjrw8FOcA1-s0tUS7ooPMDUGl7LQcdzIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)  @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/457070" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acaf501b28.mp4?token=tpuw9Q2I572IOsiqBkc64KKhamXddg84Cv_Cctt6fYCF4tQqWNLKgqn10KqL8joyQTrdDi9Qhi6eSoEhkkwlCxnCmf5mOUXYjxKhyglexqvB4-4aM6g6GpnBnAkTecKXRBryGAzl9cL_PDPtSNZQY82nt1f7TUofY27-jFp9OuDrtq3zLaHXnXhUqnxdXt9p-0EVIkbAuK2MjoF601BHZaQBv8-O5GBZsHl8bu6hukoL99y2to2xKb-f032fgWSC4KR6ICrmTtP8yKEjgyHSZPan_D5S8m5ex83OhBDbRG7mW6EtqZd4UirRDIAiqFREfcgqqOGefh2G_xr5AjlOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acaf501b28.mp4?token=tpuw9Q2I572IOsiqBkc64KKhamXddg84Cv_Cctt6fYCF4tQqWNLKgqn10KqL8joyQTrdDi9Qhi6eSoEhkkwlCxnCmf5mOUXYjxKhyglexqvB4-4aM6g6GpnBnAkTecKXRBryGAzl9cL_PDPtSNZQY82nt1f7TUofY27-jFp9OuDrtq3zLaHXnXhUqnxdXt9p-0EVIkbAuK2MjoF601BHZaQBv8-O5GBZsHl8bu6hukoL99y2to2xKb-f032fgWSC4KR6ICrmTtP8yKEjgyHSZPan_D5S8m5ex83OhBDbRG7mW6EtqZd4UirRDIAiqFREfcgqqOGefh2G_xr5AjlOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله اعرافی: با رهبر معظم انقلاب پیمان می‌بندیم بر سر راه امام راحل و امام شهید و آرمانهای انقلاب اسلامی تا پای جان خواهیم ایستاد  @Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/457069" target="_blank">📅 21:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c017da3af3.mp4?token=J5F372fLo5a4lq85FmgeusXqnkJbirzzVLtnefnfeIRqMMuHtjqo8VgeZsd36EBPkVN5dBzT0Yi5TRMCKUU9SDW2qaU2cem-sq4aeECHvFZ4hwpiyf9RIs1mZx_yYvECEQFQdl0x-vbcoNui7CN_Ku6W2UiNutfQaGDJIJ5mQEWl8n_eX2vMMv-DObCafaR1mb1QT44tyncR924PQOOQA9MfVkb1YT_u26ilnIRDy8Z99VMqjS58567Nl_O8pW5fL1DtG_dG3pGUZzJjMiko6qIXlUy9abeA4O9qGIcT_kIjge7l4sIHfu2c4-wDK6viz_Kjs85Ibyz-RmzfA_vXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c017da3af3.mp4?token=J5F372fLo5a4lq85FmgeusXqnkJbirzzVLtnefnfeIRqMMuHtjqo8VgeZsd36EBPkVN5dBzT0Yi5TRMCKUU9SDW2qaU2cem-sq4aeECHvFZ4hwpiyf9RIs1mZx_yYvECEQFQdl0x-vbcoNui7CN_Ku6W2UiNutfQaGDJIJ5mQEWl8n_eX2vMMv-DObCafaR1mb1QT44tyncR924PQOOQA9MfVkb1YT_u26ilnIRDy8Z99VMqjS58567Nl_O8pW5fL1DtG_dG3pGUZzJjMiko6qIXlUy9abeA4O9qGIcT_kIjge7l4sIHfu2c4-wDK6viz_Kjs85Ibyz-RmzfA_vXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیسیون عمران مجلس: بانک‌ها تمایلی به پرداخت تسهیلات مسکن ندارند
🔹
آن‌ها ترجیح می‌دهند منابع خود را در جای دیگری هزینه کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/457068" target="_blank">📅 21:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFDlbfKoNoNzejgLHSP5Ew8bJG7pNWK4I3Dm0DNcvr46G_UnpsmjS66WUvnbXTU97zPgdSEeF937J9w0w6DxuWbq6bPmHwQ9CTy-D0MFw137xBHXXYueJjy9dBfwi8SQXu57vd2z8kxsgSTMuH51hXNC4NHdTiiF-Pv7NBaaow0bKz_ozsinbOvFvsGuZIWB-Y1_IBRo26WDuv-i-eBoCK8oiMM4giIfz6l2bRebg15e7lmG-AH2iix_BTjl0nKJMDhOcxa926aoDqa0hreXkUdaeG3QyOEWasWdiB8IzneZZvGxZcVZUlHGWxVsFAlJi-J_VukFp6Xq5MQ-az3m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس معناداری که قاليباف منتشر کرد
🔹
رئیس مجلس با انتشار تصویری در اکانت خود به زیاده‌خواهی آمریکایی‌ها در خلیج فارس واکنش نشان داد.
🔸
این تصویر که قابی از نقشه خلیج‌فارس و تنگه هرمز را نشان می‌دهد، به‌نوعی بیانگر تسلط ایرانی‌ها بر تنگۀ هرمز و خلیج‌فارس است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457067" target="_blank">📅 21:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4612523b.mp4?token=r_uomK86Zi0deK7VBWdKlQVLM8Gu3j-Ys-JfkJg9uKBKYUKjzfY4N9LT-4CWhwzphJzpQNSlxk3xnZmVrMJRFldVo5xP_-1-meNykRdLQiajMyFBeijDTuL9Z1dm-vA-thByY6Yav3NjKb_-oDFSM4pG5f2IO6UtCiaCGD_WXHiJECJNxktJj6GnZ-H6fc-aqR-sqKEJMpiy12TOEm-iYUALSTlSqfDg8sod_cOp6vZOpJfe96r3WZiVtbf6fmWATUcKVeOffzE8015AdfSFHRSKgKvL4OL7igPdaVGSIFYvZVQ32zhniKBhiRNAHXK82E9Ui7a7hK51z9hQjQiC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4612523b.mp4?token=r_uomK86Zi0deK7VBWdKlQVLM8Gu3j-Ys-JfkJg9uKBKYUKjzfY4N9LT-4CWhwzphJzpQNSlxk3xnZmVrMJRFldVo5xP_-1-meNykRdLQiajMyFBeijDTuL9Z1dm-vA-thByY6Yav3NjKb_-oDFSM4pG5f2IO6UtCiaCGD_WXHiJECJNxktJj6GnZ-H6fc-aqR-sqKEJMpiy12TOEm-iYUALSTlSqfDg8sod_cOp6vZOpJfe96r3WZiVtbf6fmWATUcKVeOffzE8015AdfSFHRSKgKvL4OL7igPdaVGSIFYvZVQ32zhniKBhiRNAHXK82E9Ui7a7hK51z9hQjQiC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله اعرافی: ملت ما پای انتقام خون امام شهید ایستاده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/457066" target="_blank">📅 21:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb83c53a3.mp4?token=HJOLfYcSOfMDsuAx7Na_2yDqPbFUoPpdlUzTtImqdb4SyfDjGX97ugPRuCE60DGNIszD2F_qJLJnSrnWSdd1eVDJAlohaDyAbxs9oe9A5qE9H8Io2HhcVq3MUA4izI-TZp34L5RPPQTyTF9DeMwLl2Q04_xtcOe6uWQN4GqZtKyeZNKJduunQUSvju556keB0j1rHkH50N22IuBejZlNYcPOTnLtAsXvfDaFdQE0MOVi7aXD1TCmnk3RKUKpcuVa9dyAbQXINq3F1MV9bLV8HkhBHfLHEWRRMgPpmWFDYDboPqZJejTuUJoBo5q-wLePVBBVOO3DWrJ8geTDj6cXGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb83c53a3.mp4?token=HJOLfYcSOfMDsuAx7Na_2yDqPbFUoPpdlUzTtImqdb4SyfDjGX97ugPRuCE60DGNIszD2F_qJLJnSrnWSdd1eVDJAlohaDyAbxs9oe9A5qE9H8Io2HhcVq3MUA4izI-TZp34L5RPPQTyTF9DeMwLl2Q04_xtcOe6uWQN4GqZtKyeZNKJduunQUSvju556keB0j1rHkH50N22IuBejZlNYcPOTnLtAsXvfDaFdQE0MOVi7aXD1TCmnk3RKUKpcuVa9dyAbQXINq3F1MV9bLV8HkhBHfLHEWRRMgPpmWFDYDboPqZJejTuUJoBo5q-wLePVBBVOO3DWrJ8geTDj6cXGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم پرسپولیس به استقلال خوزستان توسط سرگیف در دقیقۀ ۴۸
⚽️
پرسپولیس ۳ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/457065" target="_blank">📅 21:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780459cb40.mp4?token=qOPAuv0XyUZyWY4_WH22gKngAAHC5XRf7_ZTQM1OkIKc18oYsczqWY-FMLWgBytDyeH1rLJINgYk_zC8QYKvXTSO3voVQDXixQ1D-bzJTTZ49y1CK8G8auMmXhhQC_ivNU0iWRonfFE0j8HDrZYydWK9qVyBHEqO9W4IlxP-uIDKwzGDacdCtrBZSo4fib1HKNbr0rYpAm-Xk-rBD9IwARCIIAPeanByOD-VUeqRw5zFO6mNt66P2iD1cPMpXDYPC4RqXgjt9wXURhmj9qfj73jJh9Bt7BFdP3wOcoxJwV--jBVHx08QAsDnpKTA-LfetsMaunjouZvEwYLiS8yJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780459cb40.mp4?token=qOPAuv0XyUZyWY4_WH22gKngAAHC5XRf7_ZTQM1OkIKc18oYsczqWY-FMLWgBytDyeH1rLJINgYk_zC8QYKvXTSO3voVQDXixQ1D-bzJTTZ49y1CK8G8auMmXhhQC_ivNU0iWRonfFE0j8HDrZYydWK9qVyBHEqO9W4IlxP-uIDKwzGDacdCtrBZSo4fib1HKNbr0rYpAm-Xk-rBD9IwARCIIAPeanByOD-VUeqRw5zFO6mNt66P2iD1cPMpXDYPC4RqXgjt9wXURhmj9qfj73jJh9Bt7BFdP3wOcoxJwV--jBVHx08QAsDnpKTA-LfetsMaunjouZvEwYLiS8yJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در نشست پزشکیان با زنان فعال و صاحب‌نظر چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/457064" target="_blank">📅 20:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9565c277.mp4?token=XC5BUpfS2f0PI7x3i1Vqg0jXQ8mB0vRt9IiX3-nwBv94CmXqlsWC_2y9E2j-xClCBVGaMP7GxnhlpoDWI9uaY60Ys7YwJ3o54nUOSD_hb1N0x61neCFFKbEC2z3RENYdBVN82NbooR8ckEQS52r9GVrzWf9Ji-dztw95c6-t4ewcmZLMUhtg7npatpFkF3OkUEZRmMcb3C1PaoEk6xisx5ivbo26TT4Uj0CosTl7dNp1-ZxgoOkjviiXcFZLhTkFvMkLEWRNCPM_aU40Qt4_ViZtPjcnd0MtNlT6WW7H1qGrOK3FdJm3Nw-EG1Mzc0reyC4BLHBfwi3IXbV7R3nG5r4um9oOfocWfUuEqoUuHB20oeMjz08yxIw9YaqMnFnWdHyO_4e8NXaj6dN5jJWjc6x66DHhBUg9FDIcwm7MuK4oVDm88D33CPdExwcQPLWK4gE9IaycRnsJGdoC0jY_v-Fx--kS2bq8O771MxXdUFqlXPkrZv6lbz0eXxTrd6W5xWS0EeBrpGhlyL2FMEaORwEKUi4t6nPwBrtwvfEMUi9P5cycWPaMGLY5Dej72mWCJWOVmV9dbWiYaJUqig1GhX0ggkL63yhhXS8UGFzNLxZWoiFeOwRXUI_CYSR8rJOaK9YnIbhH04ENgGcboW_VhhLw_2ZRCm-GjGfZJZKXmKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9565c277.mp4?token=XC5BUpfS2f0PI7x3i1Vqg0jXQ8mB0vRt9IiX3-nwBv94CmXqlsWC_2y9E2j-xClCBVGaMP7GxnhlpoDWI9uaY60Ys7YwJ3o54nUOSD_hb1N0x61neCFFKbEC2z3RENYdBVN82NbooR8ckEQS52r9GVrzWf9Ji-dztw95c6-t4ewcmZLMUhtg7npatpFkF3OkUEZRmMcb3C1PaoEk6xisx5ivbo26TT4Uj0CosTl7dNp1-ZxgoOkjviiXcFZLhTkFvMkLEWRNCPM_aU40Qt4_ViZtPjcnd0MtNlT6WW7H1qGrOK3FdJm3Nw-EG1Mzc0reyC4BLHBfwi3IXbV7R3nG5r4um9oOfocWfUuEqoUuHB20oeMjz08yxIw9YaqMnFnWdHyO_4e8NXaj6dN5jJWjc6x66DHhBUg9FDIcwm7MuK4oVDm88D33CPdExwcQPLWK4gE9IaycRnsJGdoC0jY_v-Fx--kS2bq8O771MxXdUFqlXPkrZv6lbz0eXxTrd6W5xWS0EeBrpGhlyL2FMEaORwEKUi4t6nPwBrtwvfEMUi9P5cycWPaMGLY5Dej72mWCJWOVmV9dbWiYaJUqig1GhX0ggkL63yhhXS8UGFzNLxZWoiFeOwRXUI_CYSR8rJOaK9YnIbhH04ENgGcboW_VhhLw_2ZRCm-GjGfZJZKXmKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ کودتا با یک الگوی آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/457063" target="_blank">📅 20:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJkjaTCIU_G8q8J4zWFzfsZblCcCdsIRGv8HXfxr06XxEpOv2k2CCb8ws9LyB9zhsEp8ecaWcPBhknwrF3qGjZpiMvv97RAZFYuElu9Rpa1iMzDjWLQK5CGeIAjADJGeXIKFRS9b1rvFZ1qWO58mbRWjb-lCJMpKzpsuJDMkuaTI8MbGQbNsmJ7kbvNKau_hRNE6LfRAPaBybsuu6VKxFOdy3YHAtObQ_MPLwxT83fFVLf7jRUXxGwh3Q8aOrT2FY0pP4SaVOXsteHtt375z03bm8xuudWamtMRtjaxD5LEve9Q4igov0_xsmamS0wxs3XQvvfhQBWVMNMrdiBPgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
🔹
وزارت امورخارجه: با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/457062" target="_blank">📅 20:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f9c60ed1.mp4?token=ScsJGXbru1oFBTHZVvmCUaPyBSeXRx4iTZAQ3CoKwmkfNlVlBxXKJTLMKj2MITLzZLI2lsrae1YvIqToW5Vwof8GT_a0u8c0PGmXB24u4KZFWqepUErbhEGnXy92hiysjJKHKX8B0zdJWVAvZpkkcQNpLi996KBe1t8fFAmpmW7fO7aNGzHDdIB-WVQ9rZbgvB5RIBdyWwVgsnPXRpKWLjYoftSAOoxaFG_KctweKO_2lCH1-OygbKFxwXmxHTXb4G_zDuR8euEBdcFkKK30GE0OnZ5xdBUwOA0BV3bkhGptgYg_m_A2DRHHBZQ0odSc_0cBizjhxbwGBKMkwA6LnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f9c60ed1.mp4?token=ScsJGXbru1oFBTHZVvmCUaPyBSeXRx4iTZAQ3CoKwmkfNlVlBxXKJTLMKj2MITLzZLI2lsrae1YvIqToW5Vwof8GT_a0u8c0PGmXB24u4KZFWqepUErbhEGnXy92hiysjJKHKX8B0zdJWVAvZpkkcQNpLi996KBe1t8fFAmpmW7fO7aNGzHDdIB-WVQ9rZbgvB5RIBdyWwVgsnPXRpKWLjYoftSAOoxaFG_KctweKO_2lCH1-OygbKFxwXmxHTXb4G_zDuR8euEBdcFkKK30GE0OnZ5xdBUwOA0BV3bkhGptgYg_m_A2DRHHBZQ0odSc_0cBizjhxbwGBKMkwA6LnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این بازی‌ها یعنی کودک‌تان اضطراب دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/457061" target="_blank">📅 20:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57af079833.mp4?token=B5Re-esZuMdYcZy6p6PEA4nUSouRLjdjUCivtfnnaIBDM_4fH08ygSVv14Mf6j7JJZ0w1Sk4n5-rwvCxlnLtt82n1-0xovKYBgkopdUe6e5GIJq36K9Gxii-WSchjI4Ndviqr5mSZcqyNymRdxmi3lm9ITgrwlsfPKd65nyCXSi8x58GTYCRJfk8ZS3YzBzupItGh89uU_kfJ8yhd1b4alKbMpOMqQ1AASxZWnNOhKx8RNk25PPXCpIYFYzXkQIx8jVzc_9KagFpRCgMdW8AyPyN8Cmw7sDJz3UQtsAUPl5AkzT6btXRnd4ORJKik_haYz19UeN0MG8yr7VyjPUcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57af079833.mp4?token=B5Re-esZuMdYcZy6p6PEA4nUSouRLjdjUCivtfnnaIBDM_4fH08ygSVv14Mf6j7JJZ0w1Sk4n5-rwvCxlnLtt82n1-0xovKYBgkopdUe6e5GIJq36K9Gxii-WSchjI4Ndviqr5mSZcqyNymRdxmi3lm9ITgrwlsfPKd65nyCXSi8x58GTYCRJfk8ZS3YzBzupItGh89uU_kfJ8yhd1b4alKbMpOMqQ1AASxZWnNOhKx8RNk25PPXCpIYFYzXkQIx8jVzc_9KagFpRCgMdW8AyPyN8Cmw7sDJz3UQtsAUPl5AkzT6btXRnd4ORJKik_haYz19UeN0MG8yr7VyjPUcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم پرسپولیس به استقلال خوزستان توسط علیپور در دقیقۀ ۲۰
⚽️
پرسپولیس ۲ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/457060" target="_blank">📅 20:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c87ecb9d.mp4?token=gkjguMHsoqc-D9brl7pcc2eCwKo_NSI4c_1uq2BN0MpcbAKqqer0C7XBDYFTZTBe6B0wnH5q1LbOQi8ah8n4qewxbk9tKCd1xTZCik-VFlVqJ1rYJgKgdPe68RMzoM17n5YSTMILPuN7efDqRWJtXPOTEcopVIzq2oz930sX1bDETNFoDiuEQKmRULUir6a_QYXAJfNBwAmIuRycAKNxfG0TobIPbsR6cdaXBikkemRC0-jp7VXrBBzAHp22rARJXCw5bj8HAjhSMIV9rXdMkm4-Ux2GgBwAuzMgQgzJSi_gfiSr8r-HZOMtrYpH3e9h6HN9NLlmkRHXt5-SX7rwnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c87ecb9d.mp4?token=gkjguMHsoqc-D9brl7pcc2eCwKo_NSI4c_1uq2BN0MpcbAKqqer0C7XBDYFTZTBe6B0wnH5q1LbOQi8ah8n4qewxbk9tKCd1xTZCik-VFlVqJ1rYJgKgdPe68RMzoM17n5YSTMILPuN7efDqRWJtXPOTEcopVIzq2oz930sX1bDETNFoDiuEQKmRULUir6a_QYXAJfNBwAmIuRycAKNxfG0TobIPbsR6cdaXBikkemRC0-jp7VXrBBzAHp22rARJXCw5bj8HAjhSMIV9rXdMkm4-Ux2GgBwAuzMgQgzJSi_gfiSr8r-HZOMtrYpH3e9h6HN9NLlmkRHXt5-SX7rwnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت‌هایی شنیدنی از زمان‌هایی که دعا به استجابت می‌رسد
برشی از سخنان حجت‌الاسلام میرهاشم حسینی در برنامۀ سمت خدا
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/457059" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyzgooHbNgOpPCXqQTTtYcH6om2tUDJE90Z-htzY8zTCVtHYxEE3IKeGkasBk0p3T-cqL5kTiQruldBRYO0KkBLfptpgcrr3tXztvX7ds3t2ui3vcIMiZN22vKskChmxSBRKhu04oNzLfBaT6qBKLrOGJzG6Dux8AUQEAe_C_WdfN7fI1XutrlQUbuQCyQdINTjvqiJcR9a9ZX_k9KO6JEVjBaitrp6vVlNBBQ9q2Y0-rJMBtePze_XNTHa-5kA9n5E8K9rgLrFVAI_AeyOjld3CBWP90W6M2KDAQHPYUiOKO974D2Zq9Bo5If7y4lXKIUyimE4oBE13G_-ziPMeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد قیمت سوخت پیشران اقتصاد آمریکا شکست
🔹
فایننشال تایمز: قیمت گازوئیل که مانند خون در رگ‌های اقتصاد آمریکاست در جایگاه‌های سوخت این کشور رکورد شکسته و به ۵.۴۷ دلار به ازای هر گالن رسیده است.
🔹
آمارهای جدید نشان می‌دهد که «کرک اسپرد» یعنی فاصله قیمتی گازوئیل و نفت خام در آمریکا هم برای اولین‌بار در تاریخ به ۱۰۲.۲۰ دلار رسیده است.
🔹
افزایش قیمت گازوئیل در آمریکا پس از جنگ علیه ایران شروع شد و ادامه دارد؛ متوسط قیمت این سوخت موتور محرک اقتصاد آمریکا در سال گذشته ۳.۶۹ دلار در هر گالن بوده و حالا ۴۹ درصد گران‌تر شده است.
🔹
۸ ایالت آمریکا بزرگ آمریکا که قطب کشاورزی و صنعت هستند وابستگی شدیدی به حمل‌ونقل دارند؛ این جهش قیمت، هزینه‌های کامیون‌داران و کشاورزان را بالا می‌برد و دوباره تورم را شعله‌ور می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/457058" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40204522b.mp4?token=dgGOEB5rsRvAM2lYBKlKbhhdeBOiEd0RTXPMuAlQ9ovSkaI-ul2cFEwoAdj_ivZSjpidPkBdf1APJybvO_xhRKAHE2B2IryJSky7CEIXexlSRrJiSEeVBKk1jjsqPPPG8wATQqXY4c8ivXzhaS3iDl9Lszd2PoWUxlo_xtsDWY0dv0by1Z2qUmbwPM_L124RDCD8I_cbKYLqL-92mcP9m1T5Z_insnDpSsm_Qm6OSi84sqCkRLGDmC6gQyyaVcRqMlrO_4Exdt9yPCzcku2w4RFEmyd76TpMpWDnMI6Z6D7ijQlcfi83i7T7qmW1s8eSm9FtIPyYw89UQ3LsND1JpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40204522b.mp4?token=dgGOEB5rsRvAM2lYBKlKbhhdeBOiEd0RTXPMuAlQ9ovSkaI-ul2cFEwoAdj_ivZSjpidPkBdf1APJybvO_xhRKAHE2B2IryJSky7CEIXexlSRrJiSEeVBKk1jjsqPPPG8wATQqXY4c8ivXzhaS3iDl9Lszd2PoWUxlo_xtsDWY0dv0by1Z2qUmbwPM_L124RDCD8I_cbKYLqL-92mcP9m1T5Z_insnDpSsm_Qm6OSi84sqCkRLGDmC6gQyyaVcRqMlrO_4Exdt9yPCzcku2w4RFEmyd76TpMpWDnMI6Z6D7ijQlcfi83i7T7qmW1s8eSm9FtIPyYw89UQ3LsND1JpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سیدهاشم حیدری دبیرکل جنبش عهدالله عراق در مراسم چهلمین روز تشییع رهبر شهید در حرم حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/457057" target="_blank">📅 20:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=OJ5cYBGHGv7ndA792njjcOEuTsSgXtWSVk8G7Qu95Zi9HfKyHKLeM-zqWEYdtxZm7QenI0aQTPWmXi4o-IJWdCBqVbfrLJG2Yu1aWMuEUrJP1b70tuoBK-Ka7kiYXLVqZXF4C_Y2uYDj2wI7mx5J5TeDG5RsA5OPhba9421KSov9YNem3ETXFsE84I4UJWZ_kBI82xtfwgGqRNa-opyKNKa3AF_E8TQxXn1b5pLfyQAeeyNZ1F12rVqa4-nLGqjtVUapHKOO_Bq06Dg9J-_EN_EYyw5szNF6OF6hb37jhWo3C_qVnngluHaQF16UVvv_BssD8Tmdl6t5JDC39g5NGiWSTDgkd_0wqEy_DxQbWnxMSGrgRQFKRrSIjKmeVPLThSDVvE1psiWB3MxbXXkULuu52Yao0fEx6MO5qB-rTvw-Xs9Ck5wGW8ePIV-fv20ZamX7u1SOhhMraC5z8-8oPBsEUNsSTcP0GoUrPasMrMV-OEIuvNTQWHYR1cGBUAJ2EbX7JM5DEDzDAAMEf5KKSenBGaGJDor6peR30h5iyra7KA0pVvgLX1L4QAWoR-Z8_DELfcQP-7GKsvl4fY8b89eQNJSxrewPQq-bB09zSYVZD2RGtQ3wamPdxumt901_go2NW8npdaAwBTEfjm61tPcrtIg5gTg9HJsJ6s0A5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=OJ5cYBGHGv7ndA792njjcOEuTsSgXtWSVk8G7Qu95Zi9HfKyHKLeM-zqWEYdtxZm7QenI0aQTPWmXi4o-IJWdCBqVbfrLJG2Yu1aWMuEUrJP1b70tuoBK-Ka7kiYXLVqZXF4C_Y2uYDj2wI7mx5J5TeDG5RsA5OPhba9421KSov9YNem3ETXFsE84I4UJWZ_kBI82xtfwgGqRNa-opyKNKa3AF_E8TQxXn1b5pLfyQAeeyNZ1F12rVqa4-nLGqjtVUapHKOO_Bq06Dg9J-_EN_EYyw5szNF6OF6hb37jhWo3C_qVnngluHaQF16UVvv_BssD8Tmdl6t5JDC39g5NGiWSTDgkd_0wqEy_DxQbWnxMSGrgRQFKRrSIjKmeVPLThSDVvE1psiWB3MxbXXkULuu52Yao0fEx6MO5qB-rTvw-Xs9Ck5wGW8ePIV-fv20ZamX7u1SOhhMraC5z8-8oPBsEUNsSTcP0GoUrPasMrMV-OEIuvNTQWHYR1cGBUAJ2EbX7JM5DEDzDAAMEf5KKSenBGaGJDor6peR30h5iyra7KA0pVvgLX1L4QAWoR-Z8_DELfcQP-7GKsvl4fY8b89eQNJSxrewPQq-bB09zSYVZD2RGtQ3wamPdxumt901_go2NW8npdaAwBTEfjm61tPcrtIg5gTg9HJsJ6s0A5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)  @Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/457056" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4502fdbd.mp4?token=C9womxQCnemCrR6q3SklvUiWnlaJhh4XQMwoDA1La-YPyAlD0cSl1P5w20mZPVoVCwab7PB28ojXx2BLIlJkkM58esyvMT1tEeL05eyI21bcnS3Klf5y0fYyRwmNTpqpolKvSXivHb7wSYVsKB4khjHeqIgWLzQQ4xG6QL4dBhMILtf3dWtxsE8nArPmbBFxHlAhBxCvpwjPc605xD42Sa12pqnvlQ9_VRFUnj_fh9E40w4lDvJM9hIRQ_TYEzsBy6a5_cejnuGJKnnmbsnb6wySf_Y2kHSFGBnzTB7GJensTJcgj9MXbX6O50HWYoi5D5CpVXFH9X3tM9oSuHVtOYz0SpYDnP9OGa3Qs_0hUC_JDe-3wBwc9EDPaPWIXzNzOIORm8L6Aa6-R1PAbpMqgLB_cI4sKdVD2rHzphxAY7pysVpkhImBYefC9MtCQTZ2m0Hy9R81W354wErHoUG5a7Yk_MFWfF2wpqPgMdYy0hDtECyj_sBzZqFDYd9MyKI2szdCaOXecJB291kEzgAOHpXE8D53cBFttgZhFpfP7CeMjEqyI-3XN09-tgIhouPVBoqqpFdfPeZ9hbm7Cy5PWJFFNNHA76LG30Xrn3GBiBebVGQUyrgqgWAoGldezKsHBCniAw7eyJuqEKi9mBCEXa4x2g8tjt10BVOT_b9fizM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4502fdbd.mp4?token=C9womxQCnemCrR6q3SklvUiWnlaJhh4XQMwoDA1La-YPyAlD0cSl1P5w20mZPVoVCwab7PB28ojXx2BLIlJkkM58esyvMT1tEeL05eyI21bcnS3Klf5y0fYyRwmNTpqpolKvSXivHb7wSYVsKB4khjHeqIgWLzQQ4xG6QL4dBhMILtf3dWtxsE8nArPmbBFxHlAhBxCvpwjPc605xD42Sa12pqnvlQ9_VRFUnj_fh9E40w4lDvJM9hIRQ_TYEzsBy6a5_cejnuGJKnnmbsnb6wySf_Y2kHSFGBnzTB7GJensTJcgj9MXbX6O50HWYoi5D5CpVXFH9X3tM9oSuHVtOYz0SpYDnP9OGa3Qs_0hUC_JDe-3wBwc9EDPaPWIXzNzOIORm8L6Aa6-R1PAbpMqgLB_cI4sKdVD2rHzphxAY7pysVpkhImBYefC9MtCQTZ2m0Hy9R81W354wErHoUG5a7Yk_MFWfF2wpqPgMdYy0hDtECyj_sBzZqFDYd9MyKI2szdCaOXecJB291kEzgAOHpXE8D53cBFttgZhFpfP7CeMjEqyI-3XN09-tgIhouPVBoqqpFdfPeZ9hbm7Cy5PWJFFNNHA76LG30Xrn3GBiBebVGQUyrgqgWAoGldezKsHBCniAw7eyJuqEKi9mBCEXa4x2g8tjt10BVOT_b9fizM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گردن‌کشی یک مونتاژکار مقابل دستور قضایی
🔹
پس از انجام برخی اقدامات و تغییر کاربری غیرمجاز از سوی گروه صنعتی بهمن در یک محدوده ۱۲۰ هکتاری کشاورزی در منطقه روستای دانش شهرستان قدس و حریم منطقه ۱۸ شهرداری تهران، با دستور دادستان شهرستان قدس عوامل جهاد کشاورزی…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/457055" target="_blank">📅 20:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df437fbc7.mp4?token=rZWM7JRtlGJnxwIs14a1ejugOM_3iG6GQprWebyfcfDXunZpbHcN28IsHcOjtmpOZuJfkS3v7esV0IrfI9e4S8EqjRcM-3lzJ52eY3i0AdfYC3w_58rrddCI_udbu3niDIQMEmKnEXMivpj0mNobKpbMmIG9-Zc47gE1mBnV7NKleZdnU9nJROQ5i2wAeh_jRIeueuwuo5J8gqOyjdSA648n8Tda0PPb37IHeiy2joJwmgHAAa_pL1P3QBCONFQxm-i1_qKyyFZyfgNh-gGTGReLwGc8rd-goUjwG9f1QYnqfV5v1Qicl3QMEoSNp42fLR4HSw3x8GuIHEren_GvBD2ytKIb29St0NPVEqPrcenZyEYYmIWv2UQBKlbFjHHRd2JzxrjNU08LwMjZLGd8CnPSFOXTucwk8wDZ8d2Ix8pknkKFiqMVocOdVtlnFjCr_nxyZFgGW7EuC1c6NHF9g5Hx0SBWqBNBQ9ui298rPLr4WduH2Pvc8lWjYZCNDABNwL2bu9xFXm6j8rQ8zPqfY0wJxfTZS7d9ZQ71EeFUppfm-skoeoxp_fbgjhXlEesS6ynb_WJkZQHBb69AjX_ZjboDj9KA0XL4yF0IJWihrQACFXr5MZeGeH5j-2pSw7znH-lDXbTu5nVt_cS0n8qug_ELlta2AaPvKoeenGux1xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df437fbc7.mp4?token=rZWM7JRtlGJnxwIs14a1ejugOM_3iG6GQprWebyfcfDXunZpbHcN28IsHcOjtmpOZuJfkS3v7esV0IrfI9e4S8EqjRcM-3lzJ52eY3i0AdfYC3w_58rrddCI_udbu3niDIQMEmKnEXMivpj0mNobKpbMmIG9-Zc47gE1mBnV7NKleZdnU9nJROQ5i2wAeh_jRIeueuwuo5J8gqOyjdSA648n8Tda0PPb37IHeiy2joJwmgHAAa_pL1P3QBCONFQxm-i1_qKyyFZyfgNh-gGTGReLwGc8rd-goUjwG9f1QYnqfV5v1Qicl3QMEoSNp42fLR4HSw3x8GuIHEren_GvBD2ytKIb29St0NPVEqPrcenZyEYYmIWv2UQBKlbFjHHRd2JzxrjNU08LwMjZLGd8CnPSFOXTucwk8wDZ8d2Ix8pknkKFiqMVocOdVtlnFjCr_nxyZFgGW7EuC1c6NHF9g5Hx0SBWqBNBQ9ui298rPLr4WduH2Pvc8lWjYZCNDABNwL2bu9xFXm6j8rQ8zPqfY0wJxfTZS7d9ZQ71EeFUppfm-skoeoxp_fbgjhXlEesS6ynb_WJkZQHBb69AjX_ZjboDj9KA0XL4yF0IJWihrQACFXr5MZeGeH5j-2pSw7znH-lDXbTu5nVt_cS0n8qug_ELlta2AaPvKoeenGux1xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/457054" target="_blank">📅 20:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43389d44f7.mp4?token=eL4Q5-LDWhri3GpONdrVpnAZJfM6gt33cIz61By5cycSonAh0In7N3tsNF6dUUwA0Ku91b8Q7T8p5uC1hXu88MSI0lXVlF5Qy0_lioi6HxDLNE_dwlozKgq3r8M-ThrhrM6H5K6rddDsDOhH9QPtuevHEM_U1yrbEY3nGjJK0bhowp0ouROy9DvSdVf2pKjJxC9eE7jSTIhF_DOxmaJvjhU6x4VZnUqTE6JDYDFQSk2lfBEs-OeK-cymN9EqL-uCcwcr5wz7PrnbqDpVvmDW2gnPkoD9HYrg43PvN7jO8oN7_Hz92mHKBODJWcpVvUzUcfb9hICZTp7DgTzHKc6BxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43389d44f7.mp4?token=eL4Q5-LDWhri3GpONdrVpnAZJfM6gt33cIz61By5cycSonAh0In7N3tsNF6dUUwA0Ku91b8Q7T8p5uC1hXu88MSI0lXVlF5Qy0_lioi6HxDLNE_dwlozKgq3r8M-ThrhrM6H5K6rddDsDOhH9QPtuevHEM_U1yrbEY3nGjJK0bhowp0ouROy9DvSdVf2pKjJxC9eE7jSTIhF_DOxmaJvjhU6x4VZnUqTE6JDYDFQSk2lfBEs-OeK-cymN9EqL-uCcwcr5wz7PrnbqDpVvmDW2gnPkoD9HYrg43PvN7jO8oN7_Hz92mHKBODJWcpVvUzUcfb9hICZTp7DgTzHKc6BxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود  @Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/457053" target="_blank">📅 20:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfffd7c1ce.mp4?token=aPkvSR1LRrs9Q2Sk-T5rroUbs-NE03t-AImvVDWI7izOnQQNLLuCIlJVQOjrK2Clug6YA6eAkzdvDMW1yas503oFdE53EiNqPHFvdRCe7ffs0UNG6x6sf0dGLpPkJO6zkn3XQt2Nwj3InMC84uXswcsufSM7m3_3P_J-w9nrtM7lMwFZRhHVFgTfW77VUr_ypkDxyDH_RPzBrVdo_YE0qkYSya__IIbhY0DSMPvlUjSTV-kYu7SStE22TQLkeue0ZRUjWzmT4rR-r3D0U4lTjOVAzIFAv3-IYmZE--6zJXZNYk_E2f5-YhN0H2_1bz58lj-DMJ4UNRQSIlEqnHPJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfffd7c1ce.mp4?token=aPkvSR1LRrs9Q2Sk-T5rroUbs-NE03t-AImvVDWI7izOnQQNLLuCIlJVQOjrK2Clug6YA6eAkzdvDMW1yas503oFdE53EiNqPHFvdRCe7ffs0UNG6x6sf0dGLpPkJO6zkn3XQt2Nwj3InMC84uXswcsufSM7m3_3P_J-w9nrtM7lMwFZRhHVFgTfW77VUr_ypkDxyDH_RPzBrVdo_YE0qkYSya__IIbhY0DSMPvlUjSTV-kYu7SStE22TQLkeue0ZRUjWzmT4rR-r3D0U4lTjOVAzIFAv3-IYmZE--6zJXZNYk_E2f5-YhN0H2_1bz58lj-DMJ4UNRQSIlEqnHPJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به استقلال خوزستان توسط خدابنده‌لو در دقیقۀ ۶
⚽️
پرسپولیس ۱ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/457052" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4f517fbb.mp4?token=vNP1RAZX1x0lNd-6HcYKJXSauRXaJ0K_kJg7twTDDS2pR17rMwYDbLRdz1rYmfKxsiGRhZ2n5WiLc1a2dtkoxQ7HDwicAikkSk3cMjb3cKGP69JKvXOe7cMBDgoA259oACYog0EV2d3LM-3TGoaoaPNYzuLWHX1rXw_uCqohMdLz6_ebyyNPlNdHJ13RqKiBVTQS5FQw_qVyghHbVUVORSI4TjJcSdTdKt6vvj3jX8KXlzD3yVFgyzBHXsLjceW4QkGJRCA-qbtAPAjj9-a3ys0xA0f2LY6Cg91Kq5XXLvHsOY2UlBxIjO7kMOpTUMl9ia90EiwKcKcLyU5iUjop2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4f517fbb.mp4?token=vNP1RAZX1x0lNd-6HcYKJXSauRXaJ0K_kJg7twTDDS2pR17rMwYDbLRdz1rYmfKxsiGRhZ2n5WiLc1a2dtkoxQ7HDwicAikkSk3cMjb3cKGP69JKvXOe7cMBDgoA259oACYog0EV2d3LM-3TGoaoaPNYzuLWHX1rXw_uCqohMdLz6_ebyyNPlNdHJ13RqKiBVTQS5FQw_qVyghHbVUVORSI4TjJcSdTdKt6vvj3jX8KXlzD3yVFgyzBHXsLjceW4QkGJRCA-qbtAPAjj9-a3ys0xA0f2LY6Cg91Kq5XXLvHsOY2UlBxIjO7kMOpTUMl9ia90EiwKcKcLyU5iUjop2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: سند آیین‌نامهٔ ساماندهی خودرو در دولت چهاردهم تصویب شد  @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/457051" target="_blank">📅 19:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457049">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ebe804d25.mp4?token=tmAUme6FpFETl5ZeJr3wopMT8CV_aH0-DwWubounSfYYXb4zgW5bMKI7cxpng02wKD1RqGqZjO6tnhvTvNSOL5Mz6UX8Dp6aAHYD3tMIBMKDl5FErqtGUr7heKf1m-6Y818uStNIkja5hx_xFSqUBrLjBWjNu9in5T1AeRpEnjli6t722JyRr2duEp1Ib5YBLtDhkOy0nvl8v_HB5zwLVu6bEKGhOhnTAbjzTS-jc-HQZc1juKC6D8IMhHN_uzU3iqZv3sYYjb3zKkpxCaY-OFN6gXraR4Cg0z2fSOL_4W5UfkiOMCCGx8Dj-cr_m1HmQMXxGpmI-HidpoH47ZcDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ebe804d25.mp4?token=tmAUme6FpFETl5ZeJr3wopMT8CV_aH0-DwWubounSfYYXb4zgW5bMKI7cxpng02wKD1RqGqZjO6tnhvTvNSOL5Mz6UX8Dp6aAHYD3tMIBMKDl5FErqtGUr7heKf1m-6Y818uStNIkja5hx_xFSqUBrLjBWjNu9in5T1AeRpEnjli6t722JyRr2duEp1Ib5YBLtDhkOy0nvl8v_HB5zwLVu6bEKGhOhnTAbjzTS-jc-HQZc1juKC6D8IMhHN_uzU3iqZv3sYYjb3zKkpxCaY-OFN6gXraR4Cg0z2fSOL_4W5UfkiOMCCGx8Dj-cr_m1HmQMXxGpmI-HidpoH47ZcDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به استقلال خوزستان توسط خدابنده‌لو در دقیقۀ ۶
⚽️
پرسپولیس ۱ - ۰ استقلال خوزستان
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/457049" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457042">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrrFouGc0tTRgGGqKSXD-4GdALtrjS9xLE1NHCk9sPCP5XM2essUdGUgpI-22rb-lQIx2IFZx_dxOz_TiyZ6KRcMetTp68LZX_9DZGl0rnLGnuZYWMOQDQDZ6pIbrn3mLP581yPGycqXOELsPyyvA6TdmRnwfDcI3isC63-TKYe9e0Crv_bzQsqR4gfBX9pvw6uALrWo8BQU4oK60z6ISWQkZrsXuvYnKC7k4MLJeGLeTpzRC9M0Qq4-QpfHbC_QTZ6YIGFJQ67dOPiM-FL2AC8-WYOT-OrFz9R30DOpM8tRSuHo6E3FtY35jQdD4C7Z2FDISVefC6kOhoNQeHzjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geX15_yNpVgt7TfY0BeJxg5-bLB3ckeIsFdCd7QtVTRZjA9D7ktLF6ZDi_zfekO-Gd65l9kF_XYo7TUbZOWFLkoAJdfIJs9cGzMYPeS_9ihlODt-C278f7sWpmJQI7fZLmxvkQJBpDN0um6AG_Fegeh84Iob3SNNXCoF-RgUP-TEhGkZg5oSSnM4SWwzFdnZFsjAaXG4I--5PZhlKCLVS29q85NwjqG_XSPSuS4gbKuF4cdamDvAJByOBqsSHwnfqZSRRXCzvfSkGCWNMUn-1LfYAsac3nEpYVUOTcIwlFMd6hbwaAWAshFM8z-iosxr0lF3JJWllTu1YeZ6ISseQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1zasdxm7JEKUAIGdwEnMvu7cFYsD6OS5gviDjQgGWVzpBw416JVm7XO8qSsghYkg0f7RkZfaGl30xxc7krRUnM1u-5bAjCxgsNHKNJkzptXvp8SAE5ZtZM3nktaz-LZF2cHm-esxj1Xn7PiCHh9fLyVG1xeRazWdAbZu-qWdCeN1i-Mq7VcpOhTPMDBTMYB1GxNGRgZfqLgy-Okud34Dm77g3nkXuj94aTyvF3fSFBXfi0pIgN9uGeIkVyE8VfMGM3qq_hnbb_UJLm3uu0thIWgOeb0HxAc05Y2jgZ2EXCZOOlzUyZhG3BgQiLmgFVyYEbVWvGwOHtSNQLidwZ9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVnugvAfH_B2fi_3nyxI0CjJ423uiOUaLGEdG8_gJHQYXLl9G34voxvMtIc7dekRSEtrmmO675RnBH8QV-NnpmwXjgTGmx-s_RCsvnuc5SDZcLAXXD65c-bhwUxdJTwIN9E0MLYiVrM0szrDBif8-pIMh5XpS2MvZ7EEaE4XuRZaDHZUUpfKAmtZvkk9qHCdFpKqrru7dq2R3B1A1GAbJvaRbzFp0dnhcSQcui_2bw5Yb9SKqzjqCE9qaCuR-HnCddR3l7SIXrWhfHiY-bRBN6a6W9q7nXwmqD91rh-m1jLBzkMCvQIU0Qk98VC3k6tvWfhXiTp-zOd1jhGUpXIp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfFEAQIeiEeAC1x4HYDxn8kS2JREbq26tQwjlnGMDETBI6E-AMXivLGp5ugUFhUdffet0sRMAHaOysu-rQmTnNDtEtEdhMJw8hT302Ws5D3J3CPqC0vwL3ZodaiEjFNAJ-bKon_wn6n_aryyjWFDhzwavbv3PHGKeurf4tZ_aaWH4XeJ11AmRqQGhLjkPtRXrmFTsXCX4C0Ea5Ts46MsMfu-qupbLHDgS380eeOk0sQn6iMcFx_6juXVSx56vl7YnwkzLcAJVzQZBZLHKncAFMhfUXI48sxJifRdJQ7XJS88xZRaSdiL4xsfqH-tzw06EXkvHOj8RNSwWQCR858zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjVryOV9qqKbJ8bCqGkvy_jzKsKHr0jERvBZOq622yQSlfKvhpu7Yma60L0pbMYdGXBH0YHEbURxLXJJBMrss8PILl6WUKP20tZ3OjZsiu3NedTAe_3fuhoPOgddhHvSb-XEBdkDs-hLSLTEWL-1SvaBi-A5sCdjL-x6UHfSL-seC4SXLngS2BXv2edslhsYKQazDpGReVLQdJ3oG-pQEVF5FuQ10WkDXVDoK_c25nuEITebKdtXms8O0zbsxtu7uui39bYDmPxSo3jOwjfNmPMcoh71Ztkv2oJeFfZYQZiY_wBi57QCXH6txQwGYGGp2tfE41Oj54y98zgE3FPIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTm7lpmqfCBbtsU1eglrSvxOVHeeE0aJF-KANwSGwPpfbfeJ342DnvsK3_0_ocLXcinwcn8cS-HfUJdMXp_2Zj2Y4Ycb83pjLNl8OwLvxcHpiZZXwpXDk_HLly7X8WtTchxvujL3TolHDnD_hxRppG7uZpZaqbochA5EhcbPen6cGd0O4ZyAWG6ErfALKN7j64_TPqVCckg3fxjSxU_-xQ3nBmaezbnNt9QEAKoV198EOSp-fGoZaHGlfP7gr8imZP7H_qVhge381gNfHtSgLoANFK4K3q5agAhM223VeSouthq2-GjRoAmYGr7Xw2p9OF_FNFbo6I95iIzNjOLQ8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنان امدادگر در میدان تمرین
🔹
۱۲۰ امدادگر زن از سراسر کشور در یک تمرین عملیاتی در فارسانِ چهارمحال‌وبختیاری، مهارت‌های خود را برای روزهای بحرانی محک زدند.
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/457042" target="_blank">📅 19:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d110f4cc.mp4?token=VxgmP784NrRMN66E6WI0K7sAZzOOYF1MqW7NPycHgR55Trj_wd7X2Z43rLr3NGsD8pn69p3zl2lEx59-EKpkZznHXl-Itoi3cPQqEXrnflCsoW5bW1_QMkGRuym-5t28TJXQ09wQnhTbhVY3HNE7elA9XKpwbOpTXuvze6v5OxRadv5EqDooTd9H34_qOk_dXNCEqUXpwRaW8mE2USUm6mX7HDTuuk6c0jQpe3r3xZjOogdEl0-PkDzxqrwmo10x9dZYsBIQ64Z680tI41pD5oeAEqIFu6tPuzOa8oynYXMMMbwijaJ01HotSzj9yYRFqauJ4V3DNLx-J28FeWa85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d110f4cc.mp4?token=VxgmP784NrRMN66E6WI0K7sAZzOOYF1MqW7NPycHgR55Trj_wd7X2Z43rLr3NGsD8pn69p3zl2lEx59-EKpkZznHXl-Itoi3cPQqEXrnflCsoW5bW1_QMkGRuym-5t28TJXQ09wQnhTbhVY3HNE7elA9XKpwbOpTXuvze6v5OxRadv5EqDooTd9H34_qOk_dXNCEqUXpwRaW8mE2USUm6mX7HDTuuk6c0jQpe3r3xZjOogdEl0-PkDzxqrwmo10x9dZYsBIQ64Z680tI41pD5oeAEqIFu6tPuzOa8oynYXMMMbwijaJ01HotSzj9yYRFqauJ4V3DNLx-J28FeWa85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: سند آیین‌نامهٔ ساماندهی خودرو در دولت چهاردهم تصویب شد
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/457041" target="_blank">📅 19:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
روایتی از ساعت اول جنگ رمضان
🔹
گفت‌وگو با یکی از همسایگان بیت رهبری و روایت او از ساعت‌های اولیه حمله آمریکا به تهران را در مستند «همسایۀ رهبر» ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/457040" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
