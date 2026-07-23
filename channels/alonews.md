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
<img src="https://cdn4.telesco.pe/file/Hy-43fF5_pucDh4i9ICWmaPkamxKDXaXLw93TRIUgNvvnJGOa12lfVMVRB9YnbNgvvtgVkKJJnc0ps-5s5590XN2PH1ZKKwAPG0MjUgncrs4MQpI28n8kkienMK66CGqKCJgiLPZXRXwBPSJDCwoVA_eOc4kO7Uw4foU8Pc7e-GVWEpSSOTv_SOhM_31KoxC7jpNuL90JENOCYlaaGZVTbcGZGrMurl44m1coZj-sFPJb5D62WaWBc54fp7GxUWhjsUvOwt71Rkv1VW8g1nbSv9pMdX5pgj-TY8HYMXCV4uHBc854Dxv1_-zAqyX75m317e1FSEgF4hE_tjk-cXhqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-136974">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اونایی که کنجکاون چه ویدیوهایی بوده، براتون چندتا رو گذاشتیم موقت
😂
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/136974" target="_blank">📅 18:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136973">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رویترز به نقل از منابع: ایران این ماه برای حوثی‌ها تعدادی از فرماندهان سپاه و تجهیزات مرتبط با موشک را فرستاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/136973" target="_blank">📅 18:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5233e33b.mp4?token=SYUVndX8_S9gpVA2p8fKi4sXM5j2QcIQeubb9LO-3gzr8gRG5Vaq8jt7Y3zPpFETLy0RlUc7NaDGFU7w8HsP5RquCaVJDZL1AEvkvVeL5dvqvKsRiiWKhi49nf8aRJstCqWnIWT67H17VMZcJWTFL2zcMkI2vbXoeSWHMGdZuqy831EpP18RgDvkf-FMNkc5yX4CppZlZg591PeXnERbSsqri2s3v3okV_26x6w6RWOTsu8649-AgRYFLF0TseZQk-eRdK_LmpbarOwWYvSX66-h1TIgTWZZQiwtAMIhzq1YJGqloPthjtyO-q1pIHiNX3IaIjA-TPTIrJUjUKJ8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5233e33b.mp4?token=SYUVndX8_S9gpVA2p8fKi4sXM5j2QcIQeubb9LO-3gzr8gRG5Vaq8jt7Y3zPpFETLy0RlUc7NaDGFU7w8HsP5RquCaVJDZL1AEvkvVeL5dvqvKsRiiWKhi49nf8aRJstCqWnIWT67H17VMZcJWTFL2zcMkI2vbXoeSWHMGdZuqy831EpP18RgDvkf-FMNkc5yX4CppZlZg591PeXnERbSsqri2s3v3okV_26x6w6RWOTsu8649-AgRYFLF0TseZQk-eRdK_LmpbarOwWYvSX66-h1TIgTWZZQiwtAMIhzq1YJGqloPthjtyO-q1pIHiNX3IaIjA-TPTIrJUjUKJ8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی چند لحظه پیش عملیات تخریب گسترده‌ای را در منطقه کفار تبنیت، در جنوب لبنان، انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/alonews/136972" target="_blank">📅 18:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136970">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EYpGwv0eESWdKqePcp6XUdoGKFUptuH7k3HV0ceiHJ_fxr41pahajORZ8_--Zj8L6jJt0kEkIUVya6dYFz0v1lhTKuuAKcpqAXrTQ9Pe5aGzuHhoG88R2bz2zhwaCBbUFwUUPN76tXKOdlg59yE-Teb9tnZ5IblQ0fdxnqOLDxuHNG-abqxZ4vStVU11orMK8Fee76HN8SsN5H6h9OFmN_8yjfeyF4GRQ83mGqZ8qjI5u1aZ4jC6d6vIkOY3Wmc_OeEzPbSIZRJcFI_Kvs9zgWW4EX7uBMYG3mLt8eu2tIneh9B7cC8BzoPNHq-PZU53cvJHe9E2byEEvNQfRm2GeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ta_bxUiCuGLleL3ZZGOGfKQcPORpgpyyB3A5FqisPxy1qSYtmy7ia6T_arAhMq2hgsE773pV-rOV_qrP28ZevT-L4bEJBxNBUhxr_sdPdzd8h94k-3yJExaPTnfXzOGH4XljeDQm2fXJORAkiKtiewLhn3Xnaci1cW5d19UcPW2vLR_R4tvdjw10E9LCOuf7FjYpoVS-7p3Mhu3fnaF13kA3xsGoUOfoDtcf5nV_PNACjqsdvsSQMkpEIbgl_w8qIw2_8V2Tk2ppp21frjV3T3bybjcwG-_ZPx1-NFz_wbSat7ovNPOHy1Lio80mSKfzRrBMVNufnGpvdgX9p2i7Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پلیس فتای استان خراسان رضوی، از دستگیری زوجی که فیلم سکسی ارباب و برده ضبط می‌کردند و سپس آنها را در تلگرام با قیمت های نجومی می‌فروختند، خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/136970" target="_blank">📅 18:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تایمز اسرائیل: بانک اهداف کاملا بروز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136969" target="_blank">📅 17:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136968">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عراقچی هم به قرقیزستان رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/136968" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136967">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhy6O6n5wg3s2PtWw9IsQBnR3U40-CgR22lH6UA42KYZnEZyKg2KZsWIS6Jjcf9Qt2Z4AIyw7NxDIeF63-QJedsRRyg6UAlnpumQWVbx4UP3dcA9FdMLA_me_9NL0fxpYgccilOQI4L41wP1nc5PqcVjhvIMp6XE-gfRNmtv3PcwspI4PlTGEgvg6Ad-hD9PHk_K_M5zKi-pfAUwPffO9SiWaFeEZ3HbI99ERFnJIjt3quD3Hqb2FcSfQeqipt1_WZZwSO0LeDWoTesm-jISZ8G_NiMscWKbEqzPAqnNoQH8bQnElhLFraIsQA6vkXJE-ol4teTs7MUeCFb45PTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکندر وارد دهلی نو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/136967" target="_blank">📅 17:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136966">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سپاه پاسداران: پایگاه فیرفورد در انگلیس هدف مشروع ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/136966" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136965">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHXQaUyurWJZbzGHliyIqAY0csDpxIHCubwXxd4K5hYY_Eir4TsDrxFBz1JHFUi4bvValYT9Ew4O9vI2_qRQLNIyD0O3TuA_v04HBhF8y1yOz5ish0Lbz-dm974c0fFuBXiaubonxKDULKZ8Z2k2Gnxq9GcfhBrY6KuII8XRSKpY7sAU9e_F9fHp_ilIwDto4lmdIX7qgAIX0i6c5yYtr92CtmpDFh0pKKi80J7_9WJZnpRNd0ymm16upZKel1lIR-7CPXCju2qqcWDPaT9Oo_l01cBEx8lcznDr__GXyoGBsXAbCaywJ9iOrKBFQyk6PQ5AZbpPwA6BNCoY3k36sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت برای اولین بار از ماه مه به بالای ۱۰۰ دلار در هر بشکه رسید که عمدتاً به دلیل حملات یمنی‌های حوثی (انصارالله) دیروز به دو نفتکش سعودی و تنش‌ها در تنگه هرمز بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/136965" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136964">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPx7SlV9sCX07mgL5r7nmlv4_htSpIXpvlJW8uxhuO7rKTjTdVxlqANu3FBHbNJb74_wOG_EgXEJ69Osr7NdrBvnupPd9qqZzMWhdy4SVGedFAVXJGCWSUnYOHRinjOVEaEQkS22U3A98UBZRySSewf5iPE_lTYAt_YaKmFPmZkL4mjlPJ82gEL3T_GmOwmfgpTe3T5iKoqj8oAWJpN-CBCYcR4w7wxN3Q-pM3plZEzqj_AdjPx2n8DxuFnmaohBokn-0sr7whHDH5mZYVTLrpReR3ujlnJSRrDAjUEzEBaAcTyl4DTy71u-rRnr7WptUnhB3LRgO305GgkVCCPLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز
: مقامات آمریکا معتقدند مذاکره با دولت ایران به جایی نمی رسد و برنامه تغییر رژیم را دوباره در دستور کار قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136964" target="_blank">📅 17:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136963">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03794fcb99.mp4?token=C6YkqPB4p0-KKTdVHxcwJi7be5ZYW00jlpNUxs40FJSraItKtyHGmA_dVpQLy9lKGXRnYwvbmWsyxpNJC2d840MD3dFfxupbmMxWfdIo4DCcge9ziRGvJVLcx7vgrUhuXEobTJRD9uYyD-EdqivKMJqBG-Cqz6Q8CXQTcULaC1-FC-U0Kq5Iy2z_O2MWHCTs2NbFHdHZiVM3Y5hu65lspVHsbyMeGURFbAufcIFNcCom1pKeMDcgzxp7229L4fAnmuR2qIoneHQUiCFxnEd_MNxRZ3mfeSSZ5JNGOrOiNA5tN32dGwOIqMPDolw4vcJOyc3tReK1w3UrgYzuXQv0Cp8ShT9kPgNZLAVKIVh9GZsMXmZQDwkPOwxJI8X3vRjwprNRG_Shv6_e6VZsqW-3yR16pNKPhehsDISH5S9eXi8YihFeTBzYGSJJms2dtebvccCUji4ghcYS2MkBq7dImn189izPwZzVo-fsSuzLmKEW1DD7AvTC-cAECMq0cYFW0Mj86pdph_2lDzU5F2yohDsKN4n_XVE2AHcckUBzgE5SZWLBkyScqLfXMm0zVL39Lr89h8JIOt5WhI0sJL3ge6k9xLR6xRXdoSrcA3CiY7CMZ4qr9JgwLpHR0c634HzIbMrpuZRUgOB_HBUfybDL11YC2B73sBJYHH6XW2rR5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03794fcb99.mp4?token=C6YkqPB4p0-KKTdVHxcwJi7be5ZYW00jlpNUxs40FJSraItKtyHGmA_dVpQLy9lKGXRnYwvbmWsyxpNJC2d840MD3dFfxupbmMxWfdIo4DCcge9ziRGvJVLcx7vgrUhuXEobTJRD9uYyD-EdqivKMJqBG-Cqz6Q8CXQTcULaC1-FC-U0Kq5Iy2z_O2MWHCTs2NbFHdHZiVM3Y5hu65lspVHsbyMeGURFbAufcIFNcCom1pKeMDcgzxp7229L4fAnmuR2qIoneHQUiCFxnEd_MNxRZ3mfeSSZ5JNGOrOiNA5tN32dGwOIqMPDolw4vcJOyc3tReK1w3UrgYzuXQv0Cp8ShT9kPgNZLAVKIVh9GZsMXmZQDwkPOwxJI8X3vRjwprNRG_Shv6_e6VZsqW-3yR16pNKPhehsDISH5S9eXi8YihFeTBzYGSJJms2dtebvccCUji4ghcYS2MkBq7dImn189izPwZzVo-fsSuzLmKEW1DD7AvTC-cAECMq0cYFW0Mj86pdph_2lDzU5F2yohDsKN4n_XVE2AHcckUBzgE5SZWLBkyScqLfXMm0zVL39Lr89h8JIOt5WhI0sJL3ge6k9xLR6xRXdoSrcA3CiY7CMZ4qr9JgwLpHR0c634HzIbMrpuZRUgOB_HBUfybDL11YC2B73sBJYHH6XW2rR5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما: وقتشه عرب‌های خلیج فارس به دوره شترسواری برگردن
🔴
پ.ن: یکی نیست به این مجری احمق و معتاد بگه اونوقت چه بلایی سر ایران میاد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136963" target="_blank">📅 16:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136962">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=U6CM3AyEvJCmKyAbD3_bHTtMbtiMUhltMBGwm7MRYWRxO7ySMFBxv_SGUi75ZbYxF6XqKDCcz23GeQZnha7J6N14T0q7lwVyb7ZolmXvEjhETklzpdywVeqO9NqdsO280mQqbC7j6BdIUIu2GRUdcnFrMzW8Oyq_-ZenYqFUWEaWtcU-JsmTs2w7S2QC4Lq6kU9fp-EL31BayN0bNTc8gKPJqGCqM39M8WnUA_MVcL6PzoWe8HPvn0nuhyvSJsEmFyQ6xUWdF-_S1A-JLMKYi-UCy7AHMuE_QLr_xePhYISY78nXjXExuQ39qfMFvilf-9VSM4tKNeJB5TkLb3WENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=U6CM3AyEvJCmKyAbD3_bHTtMbtiMUhltMBGwm7MRYWRxO7ySMFBxv_SGUi75ZbYxF6XqKDCcz23GeQZnha7J6N14T0q7lwVyb7ZolmXvEjhETklzpdywVeqO9NqdsO280mQqbC7j6BdIUIu2GRUdcnFrMzW8Oyq_-ZenYqFUWEaWtcU-JsmTs2w7S2QC4Lq6kU9fp-EL31BayN0bNTc8gKPJqGCqM39M8WnUA_MVcL6PzoWe8HPvn0nuhyvSJsEmFyQ6xUWdF-_S1A-JLMKYi-UCy7AHMuE_QLr_xePhYISY78nXjXExuQ39qfMFvilf-9VSM4tKNeJB5TkLb3WENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
باز نشر
🔴
شهریاری نماینده بجنورد به ثابتی: تنگه هرمز مال ننت بوده؟ مال عمه‌ات بوده؟ ارث باباته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136962" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136961">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOAwT58po8BBfQID8kz6rWKew9X2efRDycZqTpjbwf5XwlN_Qiu8DXqK_9HpMue1nnDFXMmKkSL7i4xxilKu0KY0bidgvfCnppoHMZRQTOSOQ_SnWFMJMZh93rxTQGgGqhAYSodQGZPA7AOP9JdAMnSe0WYj4EmXECGcqD_hWuxtauEmA4RqDn1eLB8hPvIfpYjYoqP_wO6EoSEV7mrgsnxqIHCrsSIpMVhtYWGoNJh-D2f25SPZUccGWjE9iVWLapUsjQ5XVrv-fEN8ddmjONzDQbMn79SDNkqNFHelyzZW-p_cvoCmvtsqQI9scURx9dfIJI7VhjiYTjIMGi4YhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موج خروج اسرائیلی‌ها از کشور
🔴
هم اکنون فرودگاه بن گوریون
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136961" target="_blank">📅 16:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136960">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQA--exuyRcDZunrS5Z5hHEyF2j7327qttHQ_lX9_Wt3l8rxIqVWJWhtp7e_iTK4XScZr0VXh3TPbF51b-vQ6UgTrjw2bwPwKY8vyiHmYuBs2ftIEL3xxnPmGrmcIYe3TOdmO7ZHz6iA5RhmQnAIEGjLU2ZjURgBCEbNyUeH3fd7I4HqwBMB3Nx_qSeUScHA6ytBpZlsTeWtY731ys3OLRxDASVZll-H8IfdKH05Uh3CQAnlJh0d6z7JWvf566q_s5_GmjmWaKttUcsmCDdvhEJzZgf-dTwLxOardBe-oGBp72rrEUbf3G-dj2VAI87lQNjCkZIB7-4Sp3U1irZ5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آخرین پژوهش ها، مردم یونان با 164 بار سکس در سال، بیشترین تعداد سکس رو دارن.
مردم ایران هم به طور متوسط، 50 بار در سال
[ هفته ای یکبار] سکس دارن.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136960" target="_blank">📅 16:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136959">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نفت: ۹۹.۲۴ دلار!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136959" target="_blank">📅 16:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L44Fp92yQMa0q4hD7iYBRUwLuBGw2EGtQeAPIALxCLqY9V6GPOB6rQW-0bSnK2R9BDosigqXdQ_hgdCZV0bGrZaQHGXgRsdGwAlTqlDssi5bJZLbZN8Vqsy7V9qmUyQbiASPc_K-zVfSP6SC0evOqwqt2Lr7Ynvs6EN1q1Y-Aoc3eeIgk9578tAyIYTamRWx12thvH4xME7bnFrllVpTdby2idltpxyMDag1Tq_j-Z5P-R4ayo0QqX15OkFbxs2lHfFBEwtmN28zb6r_kazjwnleWH9YU9MgqfmBslV2KjRGaaodinmzw200b4e2otxXCVYkfeNh0NVoUx3UPWHbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه صدور مجوز استفادۀ آمریکا از پایگاه‌های انگلیس علیه ایران را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136958" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnAyu-Fsd9VYAn0Od_lDIaCTpJR8ran6IDdqQnDVlTs-agjGcJNEgILYdjF5ZhHZahYTes71xF5GiS8OrjjEFUxr6rhrlqZnERM2s55gurP1yigQZHBM1lZazBtPp8viHz81MMixKlsah3jRBsiX5v_Hnw9cloL4abIngAynn0R8cr82pfftxKAy-1pCOtaKZ-dKBmyFyp63QLEgjip87r1cfKOGL3CQFjs1qqogWGTXNfNHhhErmpqemnkstQgD1XOBmAC4q4W0F_wyT_8l1U4Wnmp-NLqzMs3rzJtQmjO-Zc-NDY0p3If7qTG5JzuqWmLMyLvCtkOZKgfJvLumjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: یک سال پیش، ایالات متحده آمریکا به طور جدی به حوثی‌ها به دلیل دخالت آن‌ها در تجارت و بازرگانی، با شلیک به کشتی‌ها، حمله کرد.
🔴
از آن زمان و در طول درگیری ما با ایران، آن‌ها به طور مسئولانه عمل کرده‌اند. متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته به دو کشتی سعودی شلیک کردند.
🔴
لطفاً این مطلب را به عنوان این درک تلقی کنید که اگر آن‌ها دوباره این کار را انجام دهند، ایالات متحده ایران را مسئول خواهد دانست، زیرا حوثی‌ها یک ابزار و/یا نماینده ایران هستند، و مجازات‌های نظامی جدی بر ایران و البته خود حوثی‌ها تحمیل خواهد شد. من از عملکرد آن‌ها بسیار ناامید هستم، زیرا آن‌ها تا به حال به طور حرفه‌ای و هوشمندانه عمل کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136957" target="_blank">📅 15:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9K7IJUxj1z7PLC6INmkgGmm04RjFvrxpRr5wcC_ABgXQWt49kDq3g4wH5klaSZ_XQrQ7zaUWZACxeQBeInGRs05jJvUQBDxflEq7cXD0a8aYJPJk6eW9ZG0GljKDaFRF75k-7Ao_ZC14XfrueqYdWU9Eba01hS0lKUQw2SQzdov2ukZ-wBrU7RBTzyovwWudQ5BjhgFILEvoBVAxAyM0akHUdGNKdf2Iwf7e2GUtiGcQ3tAvsOi8zgTaY160SGJiBpq0kmcalJnZr-wpU1SQJQLXR9ecb9V4OtcG-mKU0mIDeCvsVQ2It9rAh8ihV5r-pEKolOiqqAtCDknX2uGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش نشریه فایننشال تایمز، لورا لوومر، فعال رسانه‌ای حامی ترامپ، با رئیس جمهور زلنسکی در کی‌یف دیدار و گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136956" target="_blank">📅 15:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e803bd871.mp4?token=da_eD8pCOzvp2IPjQuRt8TEjHFZlg9FyzP9_c8pmYWITsXGhTZoRk5a707AXHV0jdmBqO3Ic0YvYVfRDJIr7BFYls8STH12--c6GL2aFHAaPwAvhWKtXk6_iFDzMYJwJrWR2DHOSzTgHEHWcAVgZ8mmFefO6XYtDPXDP9QXHC1vgItAb0jdLAE6s70pG94BWC-RxRkOW4WvM0Pn3rtZKk60emKED0dk-USwby3lvNbchZkbLpKlyRRCrkdp6Z51SfNPGs21DDOR98lbvn8XJlwSY3RkuUetLjPZ98Qmze4_e6-mfRi0AwCPplPIFojb-41PpAPL_f0VmjtL2e3dEtly_Ua3PZoCf_FAYADsf6Yq7IP_VOXn-hWkAYwyS8Lru40rlxrGlWAkZp7ur4rgHQfXhhCiMI1u2V542XEaCbaqiYS_tgcVOV9vfs6KqJBTmfWMkmcgb-psDZa4wvItYrJ1xFfVIZtrU6yKgRsJroqfrIN6-7lUC2ZWmpJnI5LbZwl5L-FCpRGH3pKJIO4Jb1ihwo2WnTdoARxeiDtJhhOpS7vkNuMfGZAyGCNydRaQChLfI8HNSVePqCn-9r_rnoaFpEkN-lQiBkoWVaQi16BbcFwkjLyxQN_pQc8bNGS0VjB5Sth1dI5MW_-0VPMSsCj6YnAgeLiXigfYIiVkJz2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e803bd871.mp4?token=da_eD8pCOzvp2IPjQuRt8TEjHFZlg9FyzP9_c8pmYWITsXGhTZoRk5a707AXHV0jdmBqO3Ic0YvYVfRDJIr7BFYls8STH12--c6GL2aFHAaPwAvhWKtXk6_iFDzMYJwJrWR2DHOSzTgHEHWcAVgZ8mmFefO6XYtDPXDP9QXHC1vgItAb0jdLAE6s70pG94BWC-RxRkOW4WvM0Pn3rtZKk60emKED0dk-USwby3lvNbchZkbLpKlyRRCrkdp6Z51SfNPGs21DDOR98lbvn8XJlwSY3RkuUetLjPZ98Qmze4_e6-mfRi0AwCPplPIFojb-41PpAPL_f0VmjtL2e3dEtly_Ua3PZoCf_FAYADsf6Yq7IP_VOXn-hWkAYwyS8Lru40rlxrGlWAkZp7ur4rgHQfXhhCiMI1u2V542XEaCbaqiYS_tgcVOV9vfs6KqJBTmfWMkmcgb-psDZa4wvItYrJ1xFfVIZtrU6yKgRsJroqfrIN6-7lUC2ZWmpJnI5LbZwl5L-FCpRGH3pKJIO4Jb1ihwo2WnTdoARxeiDtJhhOpS7vkNuMfGZAyGCNydRaQChLfI8HNSVePqCn-9r_rnoaFpEkN-lQiBkoWVaQi16BbcFwkjLyxQN_pQc8bNGS0VjB5Sth1dI5MW_-0VPMSsCj6YnAgeLiXigfYIiVkJz2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری خطاب به ثابتی: در مذاکرات اینبار  هم شما با همین اراجیف تون نذاشتید پولای بلوکه شده آزاد بشه!!آمریکا میخواست پول های ما رو آزاد کنه و تحریم ها رو لغو کنه ولی حرفای منتقدین مانع اینکار شد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136955" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136954" target="_blank">📅 15:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش کویت: گذرگاه العبدلی با عراق هدف حمله پهپادها قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136953" target="_blank">📅 15:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ در مورد توافق غنی سازی هسته ای عربستان گفت: این توافق کاملاً مشروط به پیوستن ریاض به توافق‌های ابراهیم است. وی همچنین افزود که این تاسیسات کاملا غیر نظامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136952" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ در مورد توافق غنی سازی هسته ای عربستان گفت: این توافق کاملاً مشروط به پیوستن ریاض به توافق‌های ابراهیم است. وی همچنین افزود که این تاسیسات کاملا غیر نظامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136951" target="_blank">📅 15:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136950">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رسانه های اسرائیلی: شنبه و یکشنبه سرنوشت ساز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136950" target="_blank">📅 15:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136949">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مرزهای عراق و کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136949" target="_blank">📅 15:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136948">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی کرملین: ایران و عربستان حق برخورداری از انرژی هسته‌ای صلح‌آمیز را دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136948" target="_blank">📅 15:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136947">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ارم‌نیوز امارات: آمریکا عملیات زمینی محدود برای کنترل مناطق ساحلی و جزایر ایران را بررسی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136947" target="_blank">📅 15:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJIWiX4yJzdwC9vczlSACiuC3HAjalsOGyApOqZ5IKI_ECCD4vlgCCkZyjpaEb9IsarnJ5Yo-Eey78H0m6_wFPBLxS1M08r-DI0OUPGhpuO0H9DlRFlFhMhtOZr_BAbkhzRQXiNBwUYMsKq8fllVLdDCADqrq4GDmmbu8Hyuzt-9i9b_sxak5fTm4CFAkjkQi6OT5qqhvxoOJCDOkOsqY8-fQ8Ukxjb9pr4Vc9y0lw_gljfpDgZi_X4gEeVx3p-ssj3rcEP1XTfM9T-GFGL0eViuyQZJHCF6cU5ZMyb6o7g1BSAvmYDm_fsoKreiFomt7oagGKUe8XOKznexrkOGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار صداوسیما در جنوب کشور با سلاح گزارش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136946" target="_blank">📅 15:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136945">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35bb3d092.mp4?token=aQkEA-99QS5-kAsiXqYlxX5DdguTb2kxMTzyIzf4OxHz17QlxxcH3lzc7p_vgtl1YsmZB7seSSD_wSkGtkWSAWYD4oOrH2Rd3hgXEvjldHMPOgzfN_MwVvnoburkB_P12KUDc_vwgVhvmUJm7_zEhgdf0JWQyAWetSQojOCyCNb--2jjcWeGfo4JSmy2fIRG-b53KsHYEvEaX7kVWas_IXJf6HhfGm1j-4xto93wYQVwhNAclroW4inoRQOgyfL0D4REEfnNjC4z5dN9WG7GVUwaEP9SKW1vDwrrnFNimmCfgFAedodK4K3LeWNsOV4bJn91O-ZOpWo8GtiqP0kEqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35bb3d092.mp4?token=aQkEA-99QS5-kAsiXqYlxX5DdguTb2kxMTzyIzf4OxHz17QlxxcH3lzc7p_vgtl1YsmZB7seSSD_wSkGtkWSAWYD4oOrH2Rd3hgXEvjldHMPOgzfN_MwVvnoburkB_P12KUDc_vwgVhvmUJm7_zEhgdf0JWQyAWetSQojOCyCNb--2jjcWeGfo4JSmy2fIRG-b53KsHYEvEaX7kVWas_IXJf6HhfGm1j-4xto93wYQVwhNAclroW4inoRQOgyfL0D4REEfnNjC4z5dN9WG7GVUwaEP9SKW1vDwrrnFNimmCfgFAedodK4K3LeWNsOV4bJn91O-ZOpWo8GtiqP0kEqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: نخست وزیر عراق یک سفر واشنگتن داشتند و طبیعی است که دیدگاه‌ها و برداشت‌های خودشان را به ما منتقل کنند
🔴
با آمریکا در حال حاضر مشکل میانجی نداریم؛ مشکل تبادل پیام نیست، مشکل نوع رویکرد آن‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136945" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOnBjuhcCthOWK_pZtsL8FvZlSawGJr1k6ZFbgBNrZ0z45BVZIvgUiOZd9mLspmbiPg-_Av1x8g4dfLabhivAtnmBRl1O0EUuRmee3YYZ3Yo3R2DaG-vGIPIvKxQsjuNttnlVvVGnW_wlgWZ4NfqzuIA3KicFdDTBndfALRbEBMy8kuDGuMEmOGDcttfBpXG9wQonaGQk9w7iTglpiwHcxtDkXTmoTh0y6LDAWs-BEuINbafrQ2dbpibQt8t2cMm7crxf8znmF7a_XkIBuuhfaOw-ZW0eA5IRkECtnHbeEJvQrkitlqrLK-xaznBnWqHeGedUO6NvVmJ-jCPrIUwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت برنت در بازارهای جهانی، ۹۸.۲۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136944" target="_blank">📅 14:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
طبق گزارش شبکه ۱۲ اسرائیل، اسرائیل خود را برای احتمال تشدید بیشتر اوضاع آماده می‌کند و در روزهای اخیر، پناهگاه‌های عمومی در چندین شهر باز شده‌اند.
🔴
با این حال، فرماندهی جبهه داخلی اعلام کرده است که تغییری در دستورالعمل‌های ایمنی عمومی ایجاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136943" target="_blank">📅 14:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رسانه های عبری : پناهگاه‌ها تو منطقه (کرمیل) اسرائیل باز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136942" target="_blank">📅 14:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnePlUxOGUSGJfiacP9WyHLOcFriYDpD19RTjHb0NzoKNolMlJzHJ7-JtoJlU-oEzcAz_q_AJ9GFnlY5QdbyKox911cnsLSrhTfhQ9uMoy-i27P5BzwZ7YRWwpo2XTRgCJBdcCCTL8xR3Q7PbBfVi2zulncU7KNp1xiGHL9oSMtAqXa12XHyPwDcbEJRTugYMrfwePeBa8ec-4ZjummLOhHCjeXZLjtDFBfc-bXwCnt14yOPbSbuGaAe41kdoLcGWpKqISItJ5n6g5EA90dvpallSLweToAxt9076-BBfYl44-ayQ6OT6xx0lZ7MqpFNh2YP35B_-6gX9FepqF6_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید وزارت جنگ آمریکا از نیروی زمینی: منو بفرس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136941" target="_blank">📅 14:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIvTbouHu1f_CKBQzqZB9ucFsHYhXuqLqqY9euDweGPY6q0qIRoMwBi9CmdFhcxi_9nekZUCZZZwGCcIr-rH7JbwBzNjubB5pIRIWQJdBqoFh3ySWfgI2ZWUnuaYXu0Bm6PmYVlNkuIgqGjCrbr1zIEaXeqMxBEyOr6VuF5c4mQ1zCUJ3i-4J35UEpTq-QHGDxgfYUk4MalR0X1xRKq1hJb3x3eToJKeFnlUn38XVgggrRgRUdGpm6uFJruwHuQFJFGXFHRlz2_yLkZiGiLRmp2wZAqCUMVTvxGNaqHjZgn6BegfEIwhe4pvKm5vB8WTBevZ1uFiLWABtiT8ebmPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیرحسین ثابتی و امیر قلعه‌نویی در جلسه بررسی عملکرد تیم ملی فوتبال در جام‌جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136940" target="_blank">📅 14:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WA33QcsoHEa1sbABelEmUYV3frt-RqItmQjwcwqqoyOhbr0mg3gisgtdYC30D0OT-a9UWInrGtWtkTIaYXzL-2ZQrgGnGVfatLp14E6jUEbTYcXKfpQPyTBqzx5R8nvddijOxVCGNKxz6t34g7-brRn442zKD3-S7swKfTjfEp7Or8ZxbWnzeim6pDmpSmMTX-STGprvV52e_XLPOSq8M_H26k-FTAsJgHIM1QFlO53XTsWTuf-t8xGzDeAVJAAd2NOw5tJ2NFoI0f_DbYDKTvbxt5qLSi0_rw6j-TgYgpHFe6-fxqDmTvRI70zPExJRQyDlcPt9-WtvD1zxjYvv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو نفتکش بزرگ چینی حامل نفت عربستان بعد از هماهنگی با حوثی‌ها، از تنگه باب‌المندب عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136939" target="_blank">📅 14:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx-b4ZEkZZggRMQtE3r_Jh_c2ZXBJ2Z4sbIyak9DQwvZMHROOF79PCx5e5fKx8Su7qzZGk_WZr2Jy-fYvxxKx2xxNwcc1IlhN6QIv-yjRDoCaRV0b42Ae8rnT1m0IlvpWslEz4qN5vIpxl_wYTeas-iL438aJ8VOJd1q8v-x8LDa4kKr1KTuhbsYmiWNNh_Sgrpt7sDW-j-Cu6I5LvcV1mIh7qhXsmK70bJOZhNqvFc53r3vZfQ8xAoybQN577r7FPjY46lhkKf5KskLXehZAbo_cWrF5GjFeywrXBBGi4WhiimPLGDrWv-7-2G8PSpHcuS_ANJlsUQrkW5cbq4Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرزهای عراق و کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136938" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAV1eUmHy5lBYx-O2hZL6vrkxNiNc596of9pONpfTXKueCVfWBFBgDIDTYSRkaYR0JLzaK5zxsh4FqKbP4ZDMNaEnSTN5QJR_r_KYIF_4crNbQV1PQvigtDF-hzPHXOxFLeMqmIARvpT8P7tLmrDLdiKCIYxSsdwsK-bVGKuUJ5A5Qe0v4V1HHADzQM6U8yf97nEwU41SODaINMOhgtGXD85NX7ECK4tQfRzGMK8TbH8aBem3owPRn_hABCDdHFEcM-g0bHZHZSSsXnYzhXqoE8PMfjQuj4180BEEzIAUrCgSAchg7FfC6mDNMFkEoi3vL4xIUHYRrR11qlbDitBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOJyl4YCwXUmSA7a7WtxPmymJMplaOAoPFnXHtehh6tx03K1DNWrQZ94Mdnbwyyh_STK_xLv10X6VOiYnTKYDFESIrhiSbvfKzIVJ-EWxgY1qHZm5746qTOwS_tRy9KUQQdVbaUs-V0K7YOryNvZzgyTl4m_e7emoesyyrUwG1QyXnN4Gdgf-hxInZJKXMtw2pmWk0R6L7pp3ACunEJrFhysuVvLdsGFgr-8Gz5CWvXkSYWJA5N98tlpdqufXwjBppEV6WzTRWPbu4ncLHJHNpT7PtiizvhyJZfYKf773Ih-fr5OXHxNqHeGL1Um5fq54zH9G2A4MAVXKGAAL4ntqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8WOU7ADnJNjVCwG5GBSgVr9D7N0nRF6pGRlPhNEsBg_U_43v3LTe9RwqWul84yf5vpn1o77dtsnN0knqXIzJhOSHARFuxOJ7QFyM5_TBfh7vlYajYksMtt0cF0ydVrpTPaR2O26iL-UlZXPd5HpfRvqVzcWg-hrBJUBDbxbA5dcHZazLsTFMjafApHKWEZDMIzEm3C6cRFCrZaPGDlHeZEJJ8BEG0aSB_FjakabPOOl5BhV3G5NqY4osfFgBRXfEmlQWRPmM4q8Y4uMXv7kw-ISIxlxWb7LWqL5v_RGTnS1WdfwTk6Og-zqK2SJd5SnolpaQ-NXB4TrGCICTmtJ3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یه فروند جنگنده سوخو Su-57 روسیه
امروز تو نزدیکی مسکو سقوط کرد، خلبان با موفقیت اجکتِ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136935" target="_blank">📅 14:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b9f3edd5.mp4?token=d7JbqQNA9sUGkM09msFsowJ7GJtGg84vcsOb58Y60JrK6OgUiYU_7fosDaENGMm2nA4vyhc-KiS1cCcaXtHfPnO2Ba-QvcjIXAp2WirW-tWGH9JebxeN9OsxRZB_P4eVSfmxDbExvNT337z9EBWESnqe5nGE09OA_TtYBS-ZvFkBzMl07wM8eZ381aOToArf-8CX7Wu3JgU1Q4AGm26ec1nPn9x2uT_4R1aIycwGQTvhLhYr-2Ku3lwFDrs9cAB7gSoSpDbzSNSFlBBLk8pFrRYlwJK1ro3MP6Tzx5tZbZWzMzL3PoPhZmmvUJiNw14nB3qUF0w5RyvxJp0SjQncTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b9f3edd5.mp4?token=d7JbqQNA9sUGkM09msFsowJ7GJtGg84vcsOb58Y60JrK6OgUiYU_7fosDaENGMm2nA4vyhc-KiS1cCcaXtHfPnO2Ba-QvcjIXAp2WirW-tWGH9JebxeN9OsxRZB_P4eVSfmxDbExvNT337z9EBWESnqe5nGE09OA_TtYBS-ZvFkBzMl07wM8eZ381aOToArf-8CX7Wu3JgU1Q4AGm26ec1nPn9x2uT_4R1aIycwGQTvhLhYr-2Ku3lwFDrs9cAB7gSoSpDbzSNSFlBBLk8pFrRYlwJK1ro3MP6Tzx5tZbZWzMzL3PoPhZmmvUJiNw14nB3qUF0w5RyvxJp0SjQncTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع چندین انفجار در گذرگاه العبدلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136934" target="_blank">📅 14:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
الجزیره: سفر نخست‌وزیر عراق به تهران ابعادی فراتر از آنچه رسماً اعلام شده، دارد
🔴
الزیدی حامل پیامی از سوی واشنگتن درباره این است که «دولت آمریکا به دنبال سرنگونی حکومت ایران نیست و اظهارات تند مقامات آمریکایی در چارچوب فشار‌های سیاسی و رسانه‌ای صورت می‌گیرد».پیام شفاهی نخست‌وزیر عراق، ممکن است که بغداد را به چهارمین پایتخت برای میزبانی گفت‌و‌گو‌های بین دو طرف تبدیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136933" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa16f50d1.mp4?token=rzDHmUX095dplgsNH3HiGW9qWVq0uhtnMRFULJFG3vUSOjOM3lm2Q08GiBsGlHCe7KLaVGVDOsaUAiGmpSr7MEIE0nuOr1lTfV1g5N7TzQLn5_F4RRr8qm5jh1e0mZibXhD9QkizYABDZCfJtbb57_LO9oMCF9K1wunyROlQbbv1gniSwf_wsl1rXZqw7auIQl6q0qx9IEDPz0FTWqNni1xcID-TD8iNlPjEzahehTypPyrBeRYQobKEcuIiKvKUpm05Jbq_dC5eUMSYXm3n5RBkxSoq-YcSSfYs3ZV1jHNIvetnhNiK2tUH3wKc0kQp2zWk-05P2KbOEg-ppTHxnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa16f50d1.mp4?token=rzDHmUX095dplgsNH3HiGW9qWVq0uhtnMRFULJFG3vUSOjOM3lm2Q08GiBsGlHCe7KLaVGVDOsaUAiGmpSr7MEIE0nuOr1lTfV1g5N7TzQLn5_F4RRr8qm5jh1e0mZibXhD9QkizYABDZCfJtbb57_LO9oMCF9K1wunyROlQbbv1gniSwf_wsl1rXZqw7auIQl6q0qx9IEDPz0FTWqNni1xcID-TD8iNlPjEzahehTypPyrBeRYQobKEcuIiKvKUpm05Jbq_dC5eUMSYXm3n5RBkxSoq-YcSSfYs3ZV1jHNIvetnhNiK2tUH3wKc0kQp2zWk-05P2KbOEg-ppTHxnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظهٔ اصابت موشک به پایگاه هوایی ملک فیصل در الجفر اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136932" target="_blank">📅 13:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
هاآرتص: در اسرائیل خود را برای احتمال شلیک از سوی ایران در شنبه و یکشنبه آماده می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136931" target="_blank">📅 13:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
صدا و سیما : دو موشک به شهر کنارک در استان سیستان و بلوچستان اصابت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136930" target="_blank">📅 13:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مظفری،نماینده ولی‌فقیه : قرارگاه مشترک عفاف و حجاب تو استان قزوین تشکیل می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136929" target="_blank">📅 13:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhHy2FKclov-tmdnp64M0I2nUX03B738x5jOd9FxfT83Oj3cacBnr85TWQze1woCZ6zs7AOZujSUvD0wgF3umnCFOTROf5HCmvZ52EUEbvHWnxE2c3Kipg3CaTR0YA5la38piv_HqdFHNI1ZVjxNYuhq-yCGLeriPBC0khzF8JFUGRmcI4cGCMt89SCUjQTgFecFsKORTRNYDJQfNTjQyGLR9ZNIxEzJSqoh52oM1oaRS4j5q2hqfvxYIUfmsc9K1iW3LctYHUv63s_KK5JDGVPfz9ndOMtELL5n_-DuQwFDJCwDotbX8QxlXYDDJFnq4XSZiNTCr3__CBGq5xaYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت پس از حمله حوثی های یمن به دو تانکر نفتی عربستان سعودی، از 98 دلار به ازای هر بشکه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136928" target="_blank">📅 13:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b94d872.mp4?token=dgJdCr9r6lJlGbOQZEaCGcT11lTuxyVWoAe2zuP0Lqv4QHouDee1tjOAbXv6K3mr7IghLg8gXfR-GSmu9SRGmR3K7VhvN4Ux9jHppI3IK5MYFfd4tlePR7KnjgsR7evbgHpU0e9YwHV7VANl0nT22shM1jHzH7wRjuEq-BiX-gbxiy_FeyKEcTNSiNeeOnKZfaV4WuzGYeKEs-SRvJ1xucuzV5qA0ikJKZB71l5kNiro51DXsVIxGBIEtv8qa7-XlIG5qa07wNPe9IgUS3nSoN3KVV9Tai-nB03V1f6AG2GFc-avpR6d6_Rr4UQiBtj1zqPCCTvcrhe9hlBHpd8k3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b94d872.mp4?token=dgJdCr9r6lJlGbOQZEaCGcT11lTuxyVWoAe2zuP0Lqv4QHouDee1tjOAbXv6K3mr7IghLg8gXfR-GSmu9SRGmR3K7VhvN4Ux9jHppI3IK5MYFfd4tlePR7KnjgsR7evbgHpU0e9YwHV7VANl0nT22shM1jHzH7wRjuEq-BiX-gbxiy_FeyKEcTNSiNeeOnKZfaV4WuzGYeKEs-SRvJ1xucuzV5qA0ikJKZB71l5kNiro51DXsVIxGBIEtv8qa7-XlIG5qa07wNPe9IgUS3nSoN3KVV9Tai-nB03V1f6AG2GFc-avpR6d6_Rr4UQiBtj1zqPCCTvcrhe9hlBHpd8k3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال پزشکیان از نخست‌وزیر عراق در کاخ سعدآباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136927" target="_blank">📅 13:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=P3LLR3c91LZ4tFjcqaINEfD-qhJMyubk3QhyxWOHWM6IKgOoI7ZKHYxZS-5uXjCPvK7tzgvHgErFWVCdElWFoavSn2TJhaNHPxcvi1OD9RdzTBxk8NDZRnfYHuSc4_OJnwaarm7Df7hVp05kobSxweszxcNNB0nB7ZAjB52S9xeT5Dc7E6bEhTBvP2F7f8bEKIwvIY49dyEFhR_5majASGcuYbPwtPHe2xxi4VPfhUaK6JYXUDK3g_2RtpIVtTjcSswFecKfebQEsE8P8OAs8G66ClvndVFWdlhZkTGwSPSRmJZarArRwsGPLH5aEb0VH4yKMI2ozyEikqkNlA8JeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=P3LLR3c91LZ4tFjcqaINEfD-qhJMyubk3QhyxWOHWM6IKgOoI7ZKHYxZS-5uXjCPvK7tzgvHgErFWVCdElWFoavSn2TJhaNHPxcvi1OD9RdzTBxk8NDZRnfYHuSc4_OJnwaarm7Df7hVp05kobSxweszxcNNB0nB7ZAjB52S9xeT5Dc7E6bEhTBvP2F7f8bEKIwvIY49dyEFhR_5majASGcuYbPwtPHe2xxi4VPfhUaK6JYXUDK3g_2RtpIVtTjcSswFecKfebQEsE8P8OAs8G66ClvndVFWdlhZkTGwSPSRmJZarArRwsGPLH5aEb0VH4yKMI2ozyEikqkNlA8JeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبوسی
ِ
پزشکیان با نخست‌وزیر عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136926" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: در گفت‌وگوی تلفنی با بن سلمان، توافق کردیم که به همکاری برای حفظ تجارت دریایی از طریق دریای سرخ و تنگه هرمز ادامه دهیم
🔴
حملات یمن به تانکرهای نفتی سعودی در دریای سرخ را محکوم کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136925" target="_blank">📅 13:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb7b3edf8.mp4?token=RY5h2fWVZ-qFkDlNp2cTdxqx0CB4ijt_ixq5kwgIhU5hYvTSBzNMOPguTYpirmALWbLdQGDo1EE_TdPWMi-EmvbNEo8l174l9bUpT1GVee_HHMEfsukocx4Huw8Y3gwiXZIDNzUjIAjwo5pidIcMgC6Atw_9-wsvOtZWpPgUEVelxY2tfuvyiyi7LVVCAztzvAvgHWVycqKu9Dtvs9EVKDxHFsh1wUzH96a3qYhduyKVm0elv9pUFQwkAG-BtepuSaJ6Asa2ocjTUiYkWhlk61hnSm0BQVfpX1K1j_ArjgZDtG291CCcy5SPhNAuNxGc94OMrpnFkeeC3S2eP6ekSEDZSfztfmWs3e_SDO5elYyN2ajiYVv0MMetXjJG6C8ZZptqkQI0NY43P7DQwmEpfBun9khIBkt7uuKJTrOCiBOmh_E1v-DTzPPXcTmRvQ9pcSF_dkFhhUMQP-xLxYXOnp2Iivvx3TLnwOvpnEMxD1wyKXWJ73_puJ1N25hGWPcP11AJEdb4xRMO2gd4IxWgCch169N0VSc7MmrO0c1NSSlbfLzyLJ685l4usj91yZ-QME3_Zi9Ev1MN7lG1t7OjTNMT0VWLj647tPdXPsrQSm9Twc2cV13rAYCOt0lVLqq2GwOWEAaoaJ6GVDCeCtRFY0xg46ipOQJ38A5OSUVZq9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb7b3edf8.mp4?token=RY5h2fWVZ-qFkDlNp2cTdxqx0CB4ijt_ixq5kwgIhU5hYvTSBzNMOPguTYpirmALWbLdQGDo1EE_TdPWMi-EmvbNEo8l174l9bUpT1GVee_HHMEfsukocx4Huw8Y3gwiXZIDNzUjIAjwo5pidIcMgC6Atw_9-wsvOtZWpPgUEVelxY2tfuvyiyi7LVVCAztzvAvgHWVycqKu9Dtvs9EVKDxHFsh1wUzH96a3qYhduyKVm0elv9pUFQwkAG-BtepuSaJ6Asa2ocjTUiYkWhlk61hnSm0BQVfpX1K1j_ArjgZDtG291CCcy5SPhNAuNxGc94OMrpnFkeeC3S2eP6ekSEDZSfztfmWs3e_SDO5elYyN2ajiYVv0MMetXjJG6C8ZZptqkQI0NY43P7DQwmEpfBun9khIBkt7uuKJTrOCiBOmh_E1v-DTzPPXcTmRvQ9pcSF_dkFhhUMQP-xLxYXOnp2Iivvx3TLnwOvpnEMxD1wyKXWJ73_puJ1N25hGWPcP11AJEdb4xRMO2gd4IxWgCch169N0VSc7MmrO0c1NSSlbfLzyLJ685l4usj91yZ-QME3_Zi9Ev1MN7lG1t7OjTNMT0VWLj647tPdXPsrQSm9Twc2cV13rAYCOt0lVLqq2GwOWEAaoaJ6GVDCeCtRFY0xg46ipOQJ38A5OSUVZq9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد مطهرنیا:من قبلا پیش بینیمو در مورد سال ۱۴۰۵ گفتم.
بهار پر رعدوبرق داریم(حملات نظامی).
تابستان بسیار گرم داریم(کمبود انرژی در اثر حمله به زیرساخت ها).
پاییز بسیار برگ ریزان از داخل(تـرور رهبران افراد بلندپایه حکومت و فروپاشی).
زمستانی که بذر سال های ۱۴۰۶ و ۱۴۰۷ رو روش میکارن(ورود افراد جدید و مد نظر خود آمریکا به سیستم حکومت).
این جنگ از ۱۴۰۰ تا ۱۴۰۴ مقدماتش فراهم‌ شد؛ از ۱۴۰۴ تا ۱۴۰۷ وارد پیک میشیم و از ۱۴۰۷ تا ۱۴۱۰ پیامدهاش نشون داده میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/136924" target="_blank">📅 13:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ارتش اردن : در ۲۴ ساعت گذشته، چهار موشک و شش پهپاد ایرانی را رهگیری کردیم
🔴
هیچ تلفات انسانی یا خسارت مادی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136923" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9xK55s9Wnu-42R5j8WerSWWyHwUelUbH0YFNr-7XQUZDLLOqKAEY0G3K-98b4hB-nL40g9SNALye03iyj-cpSrKJY3MglA7ZX3jM0Rt7RLME8z_VBVJbkdbo_WZfp8VnNP2UQh5Sx6l-HotDvosmAR_tDVmy8E8s199Y0ZexW3TUv80VTI2BDI9tvtsvzEdcfARasJVTx2yaqWyFFBUGlYoPIqJ7sP-zhBW99FTxCp2Ne3lwSGbfrdC1vMpY6QDE8UiKh2FUW11wS51mV-jaUvLao6M_B3YkSAFdWOxI7QzGKOyyqH6hqKAuSmM1h6bbNUyW0yPtoQCFwbgVpXNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوه قضاییه: احضاریه پرونده قصاص ترامپ برای کاخ سفید ارسال شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136922" target="_blank">📅 13:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f08eb177.mp4?token=eG3roGpI5PmipIGl867FTkE_l54kAiAu-zRsFvyyclPWXcbOr-jfrGDMbW1Se53QY91j6lH-oH50UmGMGW-vWS-v6VMrVE2RGiHKJOTECzynL-i1xYDT4r3_l34uBUqCU_v9JIFmaTlUeAK4_zi_uTyvNjT1wJgaSv_pi5zPGZVNTcbS747ISmHPaJSC564WDvpkrAtj8PfSWe7AkQwQVYA7EyqHi2HKE-vs-dApWkabA40NRRy07zec0jQ7eh5I0s3F8meNrLRYR69ks7WbIAz7C2nY9zQJlf20lwcV32usW7VRhpq0BVASPKIRIfimt5PFFaaBDY7HNQOV4RXdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f08eb177.mp4?token=eG3roGpI5PmipIGl867FTkE_l54kAiAu-zRsFvyyclPWXcbOr-jfrGDMbW1Se53QY91j6lH-oH50UmGMGW-vWS-v6VMrVE2RGiHKJOTECzynL-i1xYDT4r3_l34uBUqCU_v9JIFmaTlUeAK4_zi_uTyvNjT1wJgaSv_pi5zPGZVNTcbS747ISmHPaJSC564WDvpkrAtj8PfSWe7AkQwQVYA7EyqHi2HKE-vs-dApWkabA40NRRy07zec0jQ7eh5I0s3F8meNrLRYR69ks7WbIAz7C2nY9zQJlf20lwcV32usW7VRhpq0BVASPKIRIfimt5PFFaaBDY7HNQOV4RXdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری نشان می‌دهد که یک موشک بالستیک ایرانی صبح دیروز به پایگاه هوایی فیصل در اردن اصابت کرد.
🔴
پس از این اصابت، انفجارهای ثانویه نیز مشاهده می‌شود. همچنین، مسیرهای چندین موشک رهگیر قابل مشاهده است، که نشان می‌دهد همگی آن‌ها ناکام بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136921" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f640ff2a.mp4?token=R63xWG5BUG9rCu0el8j-ZEnL4tQ6mQNhyj_WiH-FTAzI-Gvc0T8tdXYel6bBPd04vF_-C61KrnQnLlc0XK7CM0SEQjXrEGP7ptk5_Rl1Ovx6NOcmNLQ0PPz7WadQRRyfqdcrDNnc7KR3EbOXstDM3PocINmuclI5almwZjwmkNVIBqY3q6-kEf_by5V1JqY5E-LxthuE2APUHxcBa7igleqZVoG0ApAIFWMZxT7qpBaoYQFLo841lM2eJPEW862Uw62hXZy2k1ARdvtGXQexyWUeeXSYh0xjYgotv4K16oMzaR1w0yHCiIfa3d9B7hdGgv6zslPgDo4uktOk3fab6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f640ff2a.mp4?token=R63xWG5BUG9rCu0el8j-ZEnL4tQ6mQNhyj_WiH-FTAzI-Gvc0T8tdXYel6bBPd04vF_-C61KrnQnLlc0XK7CM0SEQjXrEGP7ptk5_Rl1Ovx6NOcmNLQ0PPz7WadQRRyfqdcrDNnc7KR3EbOXstDM3PocINmuclI5almwZjwmkNVIBqY3q6-kEf_by5V1JqY5E-LxthuE2APUHxcBa7igleqZVoG0ApAIFWMZxT7qpBaoYQFLo841lM2eJPEW862Uw62hXZy2k1ARdvtGXQexyWUeeXSYh0xjYgotv4K16oMzaR1w0yHCiIfa3d9B7hdGgv6zslPgDo4uktOk3fab6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گوینده جمله تنگه مامان ثابتی: اگه جرات دارید رفراندوم برگزار کنید، هیچکس دیگه با ایران دوست نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136920" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه عمان و پاکستان پیرامون تحولات اخیر در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136919" target="_blank">📅 12:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9b370e41.mp4?token=breyaiWFqaEGd0TC6j_Xf0EfE-TvP1rFef0Qccuc5gzcxrZEbCry3Rtp4OmFxNmOpmRpDpGqa-mUWxHXopX36HrBlD6r5MI_rI_hT1pmPtCycyQEBtnmmss22EDNE7LcaCYiHfA3tXX-zuJVBF7ZNOWi_zAXYFmMreaqlvESBt4ORG4zE9QTlllgyypU278r5OTcCms4GPUmq3pr45iqGuh1wVCOf9X2sxd39X6tyCavXAAr31wa8b8rU7aww9Dec4nQrVj5mBQM-DkEjCt4RZ6UIwsaH-8yFUZDUeauSvFQMhmp3rXoBoM7pb8xfDRx0cHyYk0e04Iw4ekfJvBKWZpxwPSWbFftc83VC1pAz-zXd6CeEbTu9uFN5nf5QoJetiAQ5ZwugUGE9zcjC4S3xVvOUKfjavw_3GwZ24pUNJRJCB87XvJ5Gc_zs5VVkR5EmaH0PwhlSITLU3HURrNMd57YQ3OGFWVrOM7bIGQt8BsOLjAd0tCKJSFo2VhE9DU4efQku8Ve_exQOfcVT57nxldxipRA--eJtJ735vb3Nu-W2wJC4xJCRhepdWVJzb2zXna0CAv3eugqIG4nS7d_vrqkEnVFqZUw_EpiXtthdyp6H9P5zh2JoZfCs7isdm_9d4V2d8urnyI3rALrqwpP5B4BET6axhXEk_ccKDAzRmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9b370e41.mp4?token=breyaiWFqaEGd0TC6j_Xf0EfE-TvP1rFef0Qccuc5gzcxrZEbCry3Rtp4OmFxNmOpmRpDpGqa-mUWxHXopX36HrBlD6r5MI_rI_hT1pmPtCycyQEBtnmmss22EDNE7LcaCYiHfA3tXX-zuJVBF7ZNOWi_zAXYFmMreaqlvESBt4ORG4zE9QTlllgyypU278r5OTcCms4GPUmq3pr45iqGuh1wVCOf9X2sxd39X6tyCavXAAr31wa8b8rU7aww9Dec4nQrVj5mBQM-DkEjCt4RZ6UIwsaH-8yFUZDUeauSvFQMhmp3rXoBoM7pb8xfDRx0cHyYk0e04Iw4ekfJvBKWZpxwPSWbFftc83VC1pAz-zXd6CeEbTu9uFN5nf5QoJetiAQ5ZwugUGE9zcjC4S3xVvOUKfjavw_3GwZ24pUNJRJCB87XvJ5Gc_zs5VVkR5EmaH0PwhlSITLU3HURrNMd57YQ3OGFWVrOM7bIGQt8BsOLjAd0tCKJSFo2VhE9DU4efQku8Ve_exQOfcVT57nxldxipRA--eJtJ735vb3Nu-W2wJC4xJCRhepdWVJzb2zXna0CAv3eugqIG4nS7d_vrqkEnVFqZUw_EpiXtthdyp6H9P5zh2JoZfCs7isdm_9d4V2d8urnyI3rALrqwpP5B4BET6axhXEk_ccKDAzRmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخوندی که گفته بود شاشیدم وسط اتحادی که قالیباف درست کرده، خلع لباس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136918" target="_blank">📅 12:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
برخی منابع غیررسمی عربی مدعی شده اند که نیروهای آمریکایی و شخصیت‌های مهم دیپلماتیک، ساعتی پیش بدون ارائه هیچ توضیحی، بغداد را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136917" target="_blank">📅 12:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
صدای آژیر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136916" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09a5113ef.mp4?token=cxKyrgqZEBtURJdSQtY-xkhOaTwZTKYbN6oFLCvpYClPf3JiaRwbRpOlRDjHCGVLUKXBo6H3EOD_gr45mt795P1-R570uBIFkUKsVF1suSDV924tTh-7RRkjqAGdhagHJ3g_ydIb-Gr7zYMVF-kqxgAUTdhrU2306bu7LFB7JeMOcfRjIgYvTFhnOeMkY1ykX7M-pQza2w0xGtDIxSRkLDmCbpaCBRP06dRXVSMDXkw5GoZ5IYcXmY28aNSvhusbjwUn96ppbjmeeWV9-PhioTm_lDMrpEJLtczvxd8Bxc4lXhigpAeHqKJn8l5UA2XjojP6bHHdGDRS8Shh9a7ozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09a5113ef.mp4?token=cxKyrgqZEBtURJdSQtY-xkhOaTwZTKYbN6oFLCvpYClPf3JiaRwbRpOlRDjHCGVLUKXBo6H3EOD_gr45mt795P1-R570uBIFkUKsVF1suSDV924tTh-7RRkjqAGdhagHJ3g_ydIb-Gr7zYMVF-kqxgAUTdhrU2306bu7LFB7JeMOcfRjIgYvTFhnOeMkY1ykX7M-pQza2w0xGtDIxSRkLDmCbpaCBRP06dRXVSMDXkw5GoZ5IYcXmY28aNSvhusbjwUn96ppbjmeeWV9-PhioTm_lDMrpEJLtczvxd8Bxc4lXhigpAeHqKJn8l5UA2XjojP6bHHdGDRS8Shh9a7ozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا ایالات متحده به دنبال تغییر حکومت در ایران است؟
🔴
روبیو: ما به دنبال خلع سلاح هسته‌ای ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136915" target="_blank">📅 12:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وضعیت کانالای ایتا وقتی آژیر کویت و بحرین فعال میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136914" target="_blank">📅 12:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
صدای آژیر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136913" target="_blank">📅 12:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
شهر رامات گان در اسرائیل، که در حومه تل‌آویو واقع شده و دارای جمعیتی حدود ۱۷۲ هزار نفر است، دستور بازگشایی تمام پناهگاه‌های ضد بمب را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136912" target="_blank">📅 12:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03ba6f662.mp4?token=skQsf7qp1I8Jn2YDVG_0SHJVLScD-MoS3vgPYbaslK74YENfmiC2TLyQ87zKDZvjGZR4Mrf90LI7tMaI5tXGkttQ_YwLByExniC7RH4UVrqvIyuIp9YiDTgRqGgmbobfnYy-f4t3NM2o-fyve64Ufd4dvCTzwmbX2s0y07oYLTeUYUnCfgTTvzKZ_YN_jktX0qTysdsHDV3DAwMPTA3Zx4bKWbtOw4Pfw32YPVrF3mLvrYSKr4TgapTo3W65L1VhgwXYknKFA5fQ_NXDMfnZHou4BiD1c4f31HAM3IyQJLr0D86WuN1-TAqc6VZWIwfu0-xxcg1DVBmwvBp3_H9rvSVBZSyscKpnWfcjjGQR2aXGLcjGGdVTyrXEM-03UV0oMiNhnmV8lqSBHY0Dd_iXYYuXenP5bPzVVzNXO5rW6MQ7KMmmoS_CMgAxV16fASo50jGONNC3_sPeX0ZZyN4Vw2PoTxLbZAZ0VZIjIO8PnqjCbCtBHTPMV_HGHACl-h6dScMbyuPVjf6AomlNayxC032jfT6DVfNPUSYap-mUmN_KMLLOVjHYI94ULhji-kP-3j217eA9T95mOO-T60Fbs0YgvFaLIh7evrAbBd7QICJH7a6Qh9HJCBIzKi29x0DtIBtd86tO8RwpfH-DfPORLxJVjHnh8gFrnEdd9HJkydc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03ba6f662.mp4?token=skQsf7qp1I8Jn2YDVG_0SHJVLScD-MoS3vgPYbaslK74YENfmiC2TLyQ87zKDZvjGZR4Mrf90LI7tMaI5tXGkttQ_YwLByExniC7RH4UVrqvIyuIp9YiDTgRqGgmbobfnYy-f4t3NM2o-fyve64Ufd4dvCTzwmbX2s0y07oYLTeUYUnCfgTTvzKZ_YN_jktX0qTysdsHDV3DAwMPTA3Zx4bKWbtOw4Pfw32YPVrF3mLvrYSKr4TgapTo3W65L1VhgwXYknKFA5fQ_NXDMfnZHou4BiD1c4f31HAM3IyQJLr0D86WuN1-TAqc6VZWIwfu0-xxcg1DVBmwvBp3_H9rvSVBZSyscKpnWfcjjGQR2aXGLcjGGdVTyrXEM-03UV0oMiNhnmV8lqSBHY0Dd_iXYYuXenP5bPzVVzNXO5rW6MQ7KMmmoS_CMgAxV16fASo50jGONNC3_sPeX0ZZyN4Vw2PoTxLbZAZ0VZIjIO8PnqjCbCtBHTPMV_HGHACl-h6dScMbyuPVjf6AomlNayxC032jfT6DVfNPUSYap-mUmN_KMLLOVjHYI94ULhji-kP-3j217eA9T95mOO-T60Fbs0YgvFaLIh7evrAbBd7QICJH7a6Qh9HJCBIzKi29x0DtIBtd86tO8RwpfH-DfPORLxJVjHnh8gFrnEdd9HJkydc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا با وزیر امور خارجه روسیه در مورد این موضوع صحبت کردید که روسیه اطلاعاتی را با ایران به اشتراک می‌گذارد که هدف آن سربازان آمریکایی است؟
🔴
روبیو: چه کسی گفته که اینطور است؟
🔴
خبرنگار: آیا اینطور نیست؟
🔴
روبیو: چه کسی گفته که اینطور است؟
🔴
خبرنگار: گزارش‌هایی در این زمینه منتشر شده است...
🔴
روبیو: گزارش‌هایی در رسانه‌ها؟ اوه، پس حتماً درست است. این در رسانه‌ها است. این یک منبع اطلاعاتی است. من نمی‌خواهم... اجازه بدهید بگویم، بیایید فرض کنیم که این درست باشد. من قطعاً در مطبوعات در مورد آن صحبت نمی‌کنم.
🔴
هیچ کاری که کسی برای کمک به ایران انجام می‌دهد، به هیچ وجه توانایی آن‌ها را برای هدف قرار دادن آمریکایی‌ها افزایش نمی‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136911" target="_blank">📅 12:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران:
آنها هر روز با ما تماس می‌گیرند و از ما تقاضای توافق می‌کنند اما به نظرم برای آن اماده نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136910" target="_blank">📅 12:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت خارجه آمریکا برای سومین بار پیام هشدار صادر کرد: تنش در خاورمیانه بالا است، خطر تشدید ناگهانی وجود دارد.شهروندان آمریکایی احتیاط بیشتری داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136909" target="_blank">📅 12:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دقایقی پیش نخست وزیر عراق به تهران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136908" target="_blank">📅 12:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قیمت نفت برنت ساعت به ساعت افزایش می یابد و به 98.5 دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136907" target="_blank">📅 12:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: ترامپ مسئول مذاکرات با ایران است
🔴
تمام تیم‌های مذاکره‌کننده بر اساس دستورات ترامپ عمل می‌کنند.
🔴
مذاکره‌کنندگان آمریکایی با ایران دستورات ترامپ را اجرا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/136906" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دقایقی پیش صدای چند انفجار در کنارک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136905" target="_blank">📅 11:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزیر خارجه آمریکا:به نظر می‌رسد ایران برای انعقاد توافق آماده نیست
🔴
واضح است که ایران برای انعقاد توافق آماده نیست، یا حداقل برای انعقاد توافقی که آماده پایبندی به آن باشد، آماده نیست.
🔴
امیدوارم حوثی‌ها حملات خود را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136904" target="_blank">📅 11:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
انفجار در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136903" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
روبیو: اگر وضعیت همین گونه ادامه یابد ایران بهای سنگینی خواهد پرداخت، هر شب سنگین‌تر
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136902" target="_blank">📅 11:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیروی قدس سپاه اعلام کرد که به چندین هدف نظامی آمریکایی در اردن حمله کرده است، از جمله یک رادار THAAD، یک سیستم پاتریوت، یک رادار C-RAM، انبارهای ذخیره سوخت و مراکز تعمیر و نگهداری هلیکوپتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136901" target="_blank">📅 11:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: بهایی که ایران خواهد پرداخت هر شب افزایش خواهد یافت تا زمانی که به خود بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136900" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اکسیوس: به گفته منابع آگاه، میانجی‌های قطری همچنان با مقام‌های آمریکا، ایران و عمان در حال رایزنی هستند تا به توافقی جدید برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136899" target="_blank">📅 11:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / ایران پیشنهاد آتش‌بس میانجی‌ هارو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136898" target="_blank">📅 11:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر نیرو:  نیروگاه زمین‌گرمایی مشگین‌شهر اردبیل به ظرفیت پنج مگاوات و با حجم سرمایه‌گذاری ۱۰ میلیون یورو به شبکه برق کشور متصل و وارد چرخه تولید انرژی الکتریکی شد.
🔴
این طرح به عنوان یک پایلوت بر روی مخزنی از انرژی زمین‌گرمایی با ظرفیت تولید حدود ۲۵۰ مگاوات درحال تکمیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136897" target="_blank">📅 11:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTvnISWmcf70spY100EtoGyvOjdk7FfS2OuF2lLktA8ep8kMtfF3bSyM3hZXPdLgGJRwFiJgdKSQMbC3-Cux3Yxcc6jKzBOdUNJp6HSnyi03sM0vFInE6GCI4id_z5XcS4PLertw-ShDk7UYnLx6mrK6icZrOIciosurwSqwOqx8RFoOS7l7Si8Tg2mIBkONqZtqq-t_uWVpTiVBvNXynzEDkQO8vfMlr_i9qYUrm2hSJVLXlNf6DADnckmX8ZyAxwV-ggM-RFilqx1XR1RrcXEMhpQ8Dr2ce_GLFigOY0PxiL2ujSvd09NZGBTp-Vo2kUlWmQGXW-R3G0q2vFNMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۷.۶۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136896" target="_blank">📅 11:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
صدای انفجار از قطر و اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136895" target="_blank">📅 11:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd04aa4c7.mp4?token=rEWZvy-ZgDNCeBuWpOxQx6hDO948fm9SDUiwpCxlzOVUFsSstUMwZG0XOW-0j_fevVtIQIKILeY9e4xQfCILeT_vyljd4TBT8iobulH5Ro669Jtl91KXW1dYqQylagXSXWzmkEBwIBYpr5ijADfAmZ2j2PgPM2JoanL_RnzwN_AgVsrVYmSxTmzvEdqjyIVnPGWfyHh4fn7IIxP_GjSBmEzC7UMuAhFJX3rJdtdkJtsKqqtZ8SN_oUohDQQcUV4dElP9p0Li9og61AvODDc5VVKw0ArpKkH6j0oplV4NV8bf8NV3FXpFyfa0YY5ihXScSSNz9sCtmxRbd0ZfISGmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd04aa4c7.mp4?token=rEWZvy-ZgDNCeBuWpOxQx6hDO948fm9SDUiwpCxlzOVUFsSstUMwZG0XOW-0j_fevVtIQIKILeY9e4xQfCILeT_vyljd4TBT8iobulH5Ro669Jtl91KXW1dYqQylagXSXWzmkEBwIBYpr5ijADfAmZ2j2PgPM2JoanL_RnzwN_AgVsrVYmSxTmzvEdqjyIVnPGWfyHh4fn7IIxP_GjSBmEzC7UMuAhFJX3rJdtdkJtsKqqtZ8SN_oUohDQQcUV4dElP9p0Li9og61AvODDc5VVKw0ArpKkH6j0oplV4NV8bf8NV3FXpFyfa0YY5ihXScSSNz9sCtmxRbd0ZfISGmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری های نیروهای حوثی و نیروهای یمنی تحت حمایت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136894" target="_blank">📅 11:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اتحادیه اروپا با صدور یک معافیت یک‌ساله و قابل تمدید، انتقال گاز طبیعی مایع (LNG) روسیه به کشورهای ثالث را مجاز اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136893" target="_blank">📅 11:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ1FdY-TNAEb1UnGDDXmFKDeMJwbF7C-gclGDiC50GkdJVEZKqnWeYNPGp_yYQSvLy4kpJKCzFz__adc-SrV3TAxyp5aTTUDELp2sF08tuL_bLI8orppgQzxM2RubXHmM3UIR7g1vFmZ4-4PMhfvtnz4cnCo2l6hMci5zInf9f8iEfsHc31TWEdIVGpT2jS0dquViG2fyV5_fOhZGGX-Rw_aDxXC5281iyffa1cFP--doZcJMlnByzS3WTqufsf88Zt7iz3D9vPWQ4AsfWHR_Tr5PEZnPpqZbY0kNutC-sDdTM-vnGQ40BaOWcGqkgl6yqrwl6z0k5qoXTDLri1qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر عراق عازم تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136892" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7bWGTAp73_v0T_vAswypfaDVYo1upVjK28lnroE0oWhw-_RLKvJcU4uNLKLpW5HBdHj9dbwSX2BD7749nrwtf2GeKZ0UibkzA7HDcVXRbr3FcUMQ4tjjTqVuaY05_gzk101JIJz0o_4eVF9FQCDKPNP8IOAFtJHV53i5rYIv7C_u6y4XDTrfS_2xk3JFbFRstjabM2CgqQkEkzpcRcGmyXOwG5fInI1spwzfCoUGzf5dKr2oIkOSx8t5jecZekyG4vJuMaklOr5rojspq3BWXgbWIzxIG_uqEsv_yTjP4n8AdOwL24psvsF3mYpad040B52j_SRdKD0zOFqfB9bIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
دو شلیک موشک از آسمان خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136891" target="_blank">📅 11:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
تهدید هر کشتی که پرچم پاکستان را حمل کند، تهدیدی برای امنیت ملی ماست و حق پاسخگویی (واکنش) را برای خود محفوظ می‌داریم.
🔴
ما بر ضرورت کاهش تنش و پایبندی به مفاد تفاهم‌نامهٔ اسلام‌آباد تأکید می‌کنیم.
🔴
پاکستان از تلاش‌ها برای کشاندن عربستان سعودی به درگیری در خاورمیانه ابراز نگرانی می‌کند.
🔴
ما بر حمایت خود از امنیت، حاکمیت و تمامیت ارضی عربستان سعودی تأکید می‌ورزیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136890" target="_blank">📅 10:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شمار قربانیان زلزله‌های ویرانگر در ونزوئلا به ۵۳۹۸ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136889" target="_blank">📅 10:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌گید تنگه رو باز کنیم، مفت بدیم بره.
🔴
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
🔴
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/136888" target="_blank">📅 10:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLGi39UoKBlHGLmc9Q5rXC96Sx7BAi1QEFqj9FhI4WsCnfdYYENUs2hg8hh4FlILK31hK4UKIP9dGtgJgJcsyV-3vwKhJ5Br-xrO8yWPUE7tLd55BJKRvZx5iNWYTIL5YDY1_5O9nmSIvQ6V4KA2w3tqCImQNgW2QjornMwlvXSW1lJC1fy_LOjBuo47hig59dey1Voob_WYKDwdwWmzh6vU5TIk344lS-V4StLnoUme-p6xRXNKfgFCcVKqvWPem_DvFv5u-GuOxwbXDgq_PyvX4KjV4_Pki-yQk6dcndVAOLQvOK_4fibrB8zcLqz_gF4-mLbVvIE8lbkCACQtbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش از حمله موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/136887" target="_blank">📅 10:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApAIbvCFCXkNp8ZSwCT62Z8AwYHShRuAl-_8PWdEh-xAkgS1zdBkl7s0Ur_bAqkN-u0TvYgmM4e8Z_hf0hiFz0YDZGacOjF0WDrgAbUJbeIB0KgXFQpFpjgCI-UbpG9FhyhsSEFg3rTbyj45ejWSF1u4GXa-_rjAdxo4VfCKSm5HcnDfQ2avMpT1YYsCJ68R8Miv1X0esxqiEbwWJJgP4v59Fx6_j7UFKK3ErqdmXOaBYghzUlUFQcgXPTVXAEVei56J_aMvoXYjYHQoJuenuMDRkGP_7o8Ny5_vbBh3g-MgZdvGGQqwv5Ud1-AHE4oOzwyu0RVba5fwIxRU3e0wXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متأسفانه امروز صبح خواهران دوقلو
رومینا رحیمی و  ترانه رحیمی از معترضان دی ماه اعدام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/136886" target="_blank">📅 10:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسانه رسمی عربستان تأیید کرد که یک نفتکش این کشور در دریای سرخ هدف حمله قرار گرفته و دچار آتش سوزی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136885" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af710f15dc.mp4?token=pwu7v43xB98QtF0PSaeEjXW734JBXBlE8xumaw8kDaqLErS4sqkd8SigGKWsUGq_vGeATcaF5nJR6BhOA3l0klnSX2R3ccc_bCF2bOBHhiDiIF9RKRHmnVI4oR4uP1HbnVHM02HhHNst85vdWbMMgo2bxFSG6iCBFKtYm3Pcvkr7AIqqmoq_Cs4JRxByixJ7_K02X1pTXF2OKm9mCggyKFuVRpg4xtdsID5JECkiquXwPmqMvfuvxgsU8fOOWcBjRd9V9iCX3X3JlJbRyfiDeu8DMNmVROBPQ6LYufPNOJvzYzceoUWvFTMvolj2PraeY7W0TEa_7ENAPIvjckDxxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af710f15dc.mp4?token=pwu7v43xB98QtF0PSaeEjXW734JBXBlE8xumaw8kDaqLErS4sqkd8SigGKWsUGq_vGeATcaF5nJR6BhOA3l0klnSX2R3ccc_bCF2bOBHhiDiIF9RKRHmnVI4oR4uP1HbnVHM02HhHNst85vdWbMMgo2bxFSG6iCBFKtYm3Pcvkr7AIqqmoq_Cs4JRxByixJ7_K02X1pTXF2OKm9mCggyKFuVRpg4xtdsID5JECkiquXwPmqMvfuvxgsU8fOOWcBjRd9V9iCX3X3JlJbRyfiDeu8DMNmVROBPQ6LYufPNOJvzYzceoUWvFTMvolj2PraeY7W0TEa_7ENAPIvjckDxxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز هوای شمال غرب و جنوب شرق کشور با رگبار رعد و برق همراه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136884" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
براساس حکم قاضی آمریکایی محاکمه نیکلاس مادورو، رئیس‌جمهور ونزوئلا، و همسرش سیلیا فلورس از اول ژوئن ۲۰۲۷ آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136883" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8a27cdc2.mp4?token=Hm58fgxVamwvqltjp07b5UiimuganGj2I0C18zo7zaPCZtYxoOzBhxUvV4Nja05SaGShVjxCQoZaKaH5MpExomj2Fm-z0ybQ202Tz6k5IJmBwgkKudVt_jm468Gf04BFBw83vTcEDLkvGrttP6LPuZFhu2OMrTdePNUmBicprKm6B1XKgYDqUzEw7ME2aJLDfHnu-vrtP0qy2_BxwqXEPriIaHdOwc9vMSjlXqdoJ-zfNyxGWGdPxFLdUhabbuCLWeG43b2GzuvcsMnlpHg0twFqZ3Fr3Wg14AjTdsQASQaPl0lO6LBn78ODw2QOnkZ88hcd9EOHRyNJtUI6ZJyJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8a27cdc2.mp4?token=Hm58fgxVamwvqltjp07b5UiimuganGj2I0C18zo7zaPCZtYxoOzBhxUvV4Nja05SaGShVjxCQoZaKaH5MpExomj2Fm-z0ybQ202Tz6k5IJmBwgkKudVt_jm468Gf04BFBw83vTcEDLkvGrttP6LPuZFhu2OMrTdePNUmBicprKm6B1XKgYDqUzEw7ME2aJLDfHnu-vrtP0qy2_BxwqXEPriIaHdOwc9vMSjlXqdoJ-zfNyxGWGdPxFLdUhabbuCLWeG43b2GzuvcsMnlpHg0twFqZ3Fr3Wg14AjTdsQASQaPl0lO6LBn78ODw2QOnkZ88hcd9EOHRyNJtUI6ZJyJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک‌ مرد که پشت سر ترامپ بود، در یک گردهمایی در جورجیا خود را به جای رئیس جمهور آمریکا جا زد و توجه همه را به خود جلب کرد
🔴
او به طور کامل حرکات، سر و صورت رئیس جمهور فعلی کاخ سفید را تقلید کرد و عبارات او را تکرار کرد.
🔴
این ویدئو به سرعت در رسانه‌های اجتماعی و رسانه‌ها پخش شد. برخی این تقلید مسخره‌آمیز را سرگرم‌کننده دانستند، برخی دیگر آن را تمسخر دانستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/136882" target="_blank">📅 10:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e26a43d45.mp4?token=v5V0K8mLGBVpO7vqY833wQes_kxrqwmPUOWHD2jsnqIIG61bZ2yN5xizRYrekVUb6h1ctDmGO3MuPv3N3vT2Ir-lzsM3K3azG4cHxOViikR6-ioGvIHyS-8I715_Sct5YvyXxEbkpaxxoiMG4efCBzgUkAwVkJ4vuT2j8rwg1sbHAU8_PN1ZlO5f9IVSVkUuFAaUvWhbUDWifI5YYb-8lfRDdNtyrhm-OXqe0kwlNs9qDfPOWUqeDOLkqjxPvzdoRdlDySWyzPsstJWBf0XaKxvCyfeERfJ2P3vKKfXDO3MQbAysTl6mF4WQgll9ly0LXahCGKBj5d1RMe9pn2kvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e26a43d45.mp4?token=v5V0K8mLGBVpO7vqY833wQes_kxrqwmPUOWHD2jsnqIIG61bZ2yN5xizRYrekVUb6h1ctDmGO3MuPv3N3vT2Ir-lzsM3K3azG4cHxOViikR6-ioGvIHyS-8I715_Sct5YvyXxEbkpaxxoiMG4efCBzgUkAwVkJ4vuT2j8rwg1sbHAU8_PN1ZlO5f9IVSVkUuFAaUvWhbUDWifI5YYb-8lfRDdNtyrhm-OXqe0kwlNs9qDfPOWUqeDOLkqjxPvzdoRdlDySWyzPsstJWBf0XaKxvCyfeERfJ2P3vKKfXDO3MQbAysTl6mF4WQgll9ly0LXahCGKBj5d1RMe9pn2kvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی همچنان در پایگاه علی‌السالم در کویت ادامه دارد، پس از حمله ایران. می‌توان دود ناشی از این آتش‌سوزی را از فاصله دور مشاهده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136881" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8ZnrXTaYwMTudEK2BMufh-iC8nvyV3F2CgMZcgf4iQcfqfm5VWtxuv-04T_HoPOfQNx7G-hVFKQi3JxMAe7ZCT3Vjatg4J53MBbB145nA9672A_Ed-C1HWq0cZ4sAOS-cPG2Y2YamduBSiNzI6-Cv2PxCUyuuodhEB1AK8oolg-Znf0-swVcJXLwe67RQND5IKWnkN5veuN_ad-8vqredJUVU6o47Q5Sxn0LNIXYm8gyPfWI2cpBEBEsodbpzz2tUyB-4a-XmuaaX_6GDI9gjAuMXgZg1EwQe2Yy7oGc71VtnhgAEW1Z61uN3TV00gWrIKh5S_tLFWN08iog3yyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری رسول خادم برای عادل فردوسی‌پور
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136880" target="_blank">📅 09:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شبکه آی۲۴نیوز: نتانیاهو همچنان منتظر تأیید کاخ سفید برای دیدار با ترامپ است؛ سفر او به واشنگتن در صورت تشدید تنش با ایران ممکن است لغو شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136879" target="_blank">📅 09:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f280731e5e.mp4?token=GDYsS42qKhue6FjydyvpRkUQxsAE0RudUe40S9mWor86n3TmH3H0sir79nRwfxBZHMYfoblG8bTSJ0T8iKS5UY_gyxe7vInODI8JGkLkdziTx0vMWLNF_yc_WBV05ApYFAFbggymLEvglGCZYiuwrupmL35On2b9stGY3IOoJqdD-7_pg3w66G2w8tk77oyyv2IEYx4T0Bj9eZVbDJKeFS21wLCH_Af0js00IwQPISX8EEZXOWlL5uBJx207f6PGKOAfNPnV2N6Mf10Z8dCgvR0STtvvCGGVU96baN5i6ipLpaERxUtnJCfrNcP0_Bw1xrOUcEIy_3wlQNGIoSjd7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f280731e5e.mp4?token=GDYsS42qKhue6FjydyvpRkUQxsAE0RudUe40S9mWor86n3TmH3H0sir79nRwfxBZHMYfoblG8bTSJ0T8iKS5UY_gyxe7vInODI8JGkLkdziTx0vMWLNF_yc_WBV05ApYFAFbggymLEvglGCZYiuwrupmL35On2b9stGY3IOoJqdD-7_pg3w66G2w8tk77oyyv2IEYx4T0Bj9eZVbDJKeFS21wLCH_Af0js00IwQPISX8EEZXOWlL5uBJx207f6PGKOAfNPnV2N6Mf10Z8dCgvR0STtvvCGGVU96baN5i6ipLpaERxUtnJCfrNcP0_Bw1xrOUcEIy_3wlQNGIoSjd7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اخراج خبرنگاران از اتاق دیدار روبیو و لاوروف وقتی سوالات حساسی می‌پرسند
🔴
خبرنگاری از مارکو روبیو می‌پرسد که آیا از وزیر امور خارجه لاوروف در مورد کمک روسیه به ایران برای هدف قرار دادن نیروهای آمریکایی سوال خواهد کرد یا خیر.
🔴
خبرنگار دیگری از لاوروف می‌پرسد که روسیه چه زمانی حمله به اوکراین را متوقف خواهد کرد. سپس یکی از کارکنان، خبرنگاران را از اتاق خارج می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/136878" target="_blank">📅 09:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d28883e8.mp4?token=dWFCKPNDVUL9ydLodZH7LbpuKbeik8Foc-Nj4RqYjzVgdmh7ZLWteBlZWJ6yXhS0vmd_sYCCzdWahrPxrO4jA1ifOVw8LsQ9VOE6HFC-3Fy-1wObdAq_m12ltEnHYw141H9JA9I8kyTv4CEik80Ld89sgM-pDqiKfjmMdOY6IpwJbu1AFrvkYUaA1PUiijaazQCP1ncii22NqdsFw2gOk0sguwHiBw8Ub3DMX6jdja9cV56veqCnTwChPFpisP8VaiLQoaoYXQwbQZYrgzw_HyPdb2tgb1iBfXKlL5i0urwZrVmuNfMh_O9d4erF23ML7o_FPvifUnnz5pj4_-nAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d28883e8.mp4?token=dWFCKPNDVUL9ydLodZH7LbpuKbeik8Foc-Nj4RqYjzVgdmh7ZLWteBlZWJ6yXhS0vmd_sYCCzdWahrPxrO4jA1ifOVw8LsQ9VOE6HFC-3Fy-1wObdAq_m12ltEnHYw141H9JA9I8kyTv4CEik80Ld89sgM-pDqiKfjmMdOY6IpwJbu1AFrvkYUaA1PUiijaazQCP1ncii22NqdsFw2gOk0sguwHiBw8Ub3DMX6jdja9cV56veqCnTwChPFpisP8VaiLQoaoYXQwbQZYrgzw_HyPdb2tgb1iBfXKlL5i0urwZrVmuNfMh_O9d4erF23ML7o_FPvifUnnz5pj4_-nAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلمچه دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136877" target="_blank">📅 09:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
عربستان سعودی در پیامی به یمن اعلام کرده است که انهدام یک کشتی را بدون پاسخ نخواهد گذاشت. این هشدار در شرایطی مطرح می‌شود که تنش‌ها در دریای سرخ و آب‌های منطقه همچنان رو به افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136876" target="_blank">📅 09:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=MGKHkcV3LI9pBFj_-OkzU0k4vBNZvF5so1TP83HAwaiTepIRrdTmPYJBpB2qFz_PWnKHIMTyJECCuF6pIKDyAhJO2xWUpDnwu-tjdKCw1bM6tA_bCW03pbfQAS6BolPPYnbxp7zqBGQRLJqfK-4CsR3ZnPV5pagDJA6EDxuYTH5b5xTcGhXUC67FVarXD7QVoqh_SC9UzftUBkVTFTSEJ36UyWfQFRBRBxtiou-zXnRvt7lyrMFtMIH97kg7c1qlpaKfoC8YoBYr-4stAm_u6fEdVLstsUJFBG0VeKo82J2h4TbV3B0_DzAxIByEA2F-BjEkLEgEW7eM5NrDoCUupw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=MGKHkcV3LI9pBFj_-OkzU0k4vBNZvF5so1TP83HAwaiTepIRrdTmPYJBpB2qFz_PWnKHIMTyJECCuF6pIKDyAhJO2xWUpDnwu-tjdKCw1bM6tA_bCW03pbfQAS6BolPPYnbxp7zqBGQRLJqfK-4CsR3ZnPV5pagDJA6EDxuYTH5b5xTcGhXUC67FVarXD7QVoqh_SC9UzftUBkVTFTSEJ36UyWfQFRBRBxtiou-zXnRvt7lyrMFtMIH97kg7c1qlpaKfoC8YoBYr-4stAm_u6fEdVLstsUJFBG0VeKo82J2h4TbV3B0_DzAxIByEA2F-BjEkLEgEW7eM5NrDoCUupw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری نماینده بجنورد به ثابتی: تنگه هرمز مال ننت بوده؟ مال عمه‌ات بوده؟ ارث باباته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/136875" target="_blank">📅 09:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
به گزارش وال استریت ژورنال:
اعزام گسترده تجهیزات و نیرو: آمریکا در حال ارسال نیروهای ویژه، کادر درمانی، تسلیحات و هواپیماهای سوخت‌رسان به خاورمیانه است تا گزینه‌های نظامی بیشتری علیه ایران در اختیار ترامپ بگذارد.
🔴
آماده‌باش نیروهای ویژه: پروازهای باری از پایگاه‌های عملیات ویژه انجام شده و این نیروها آماده اجرای مأموریت‌های مختلف از جمله رزمی، جست‌وجو و نجات هستند.
🔴
آماده‌سازی بمب‌افکن‌ها و جنگنده‌ها: بمب‌افکن‌های دوربرد B-1 مستقر در بریتانیا برای عملیات‌های بزرگ آماده می‌شوند و جنگنده‌های F-16 و F-35 نیز به منطقه اعزام شده‌اند.
🔴
میزبانان احتمالی: کشورهای اردن و اسرائیل به عنوان پایگاه‌های احتمالی استقرار این جنگنده‌ها و تجهیزات جدید در نظر گرفته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136874" target="_blank">📅 09:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
معاون استاندار خوزستان: در حمله آمریکا به گذرگاه مرزی شلمچه در استان خوزستان، ۲ نفر کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136873" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bda1db65.mp4?token=JiHJva0adxFRs2amJg76wXZcGMyKzT0ydyHFhmyY0SjwfgvtRnWEttuuRsSx2XWrEy97N0imVlV8Hch2Zcgbbp2lKOxxKP5TitWHfPv02VjJyum78Hl_5bpPg9PNA9U1l5cB8sqsc48zCGOztAQMrNUYSRWZkkg54f9C2UpKmVJOmmDkTQA3kEYEiFRdkMHHvHfjC2jV0naHVo3v1Fh_PiPYhomL151wAsmUcwntS5Ph8EOXY7I83LQuxtTQ_-Q3Ia5COt7GrS0V6o5iNrt0prC20CyezAppPBI4cfEnxR_Y6TUl5h36qqrmUk3xhpkFNHrwVgk5c1HPmj4SjcxyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bda1db65.mp4?token=JiHJva0adxFRs2amJg76wXZcGMyKzT0ydyHFhmyY0SjwfgvtRnWEttuuRsSx2XWrEy97N0imVlV8Hch2Zcgbbp2lKOxxKP5TitWHfPv02VjJyum78Hl_5bpPg9PNA9U1l5cB8sqsc48zCGOztAQMrNUYSRWZkkg54f9C2UpKmVJOmmDkTQA3kEYEiFRdkMHHvHfjC2jV0naHVo3v1Fh_PiPYhomL151wAsmUcwntS5Ph8EOXY7I83LQuxtTQ_-Q3Ia5COt7GrS0V6o5iNrt0prC20CyezAppPBI4cfEnxR_Y6TUl5h36qqrmUk3xhpkFNHrwVgk5c1HPmj4SjcxyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: چابهار و کنارک شب آرامی را پشت گذاشتند و زندگی همچنان در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/136872" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
