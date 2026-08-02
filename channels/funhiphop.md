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
<img src="https://cdn4.telesco.pe/file/sywsf1y2pw3sni9f5rezvOZVFA3oqMY9tsb0N0OSXMn9S1d2wHvmh60aTZrZWPkFGyr-lNezLnB1XxpSgZmLfRMrjMPLQMw7agLdtIkCOx_5ZgdKBkx9R2D1ofiHrKPlG-cIZorlUeC1baFRpQg2g2pijeY6Ai9Zw501DJRK9DK4xvfrfKHy0mf9yP5mdK3SgYae25Qp79cB09bNeWU_FvAFhGf-3aLgdUs7cPf5K3R1aMJUG-G7hp5Lsfd-jaGOQomTxrtiWgHo-tnLzRQpq7rJY4CDtJ0dM1W9roTisykRuIX1faCjG54hVSWEg8G2xuifR1FFC6-ifbzt_PDJxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 17:53:49</div>
<hr>

<div class="tg-post" id="msg-81694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یکی فصل سه سریال Lioness برام بفرسته لطفاً
@mc_menot</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/funhiphop/81694" target="_blank">📅 17:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الو</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/funhiphop/81693" target="_blank">📅 17:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81691">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قاآنی رئیس ستاد مشترک ارتش اسرائیل و عراقچی رفتن عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/81691" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81690">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/81690" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81689">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJru1ZMk2IStzFh_Jltk-OQweNyYABEcOKggKZo6Olr5TsM_zxDgNsToI87Ip5VK2V0f7W2EQaRcVoBO0poLqGHdB9-Y3Rv-jMz5l-yHxFBAxjqhtgzEU13mpv8DG7bNxhULy4-n3uBDIpJDXx3jKIi_TV5jyyzmbz9fRgqT7FkspJlTYrcfLVzo2EU8c6eoQZJlI2v1oFRkfR3viPJgLf-m264WRS83HzAZ8Kjs-qYY-T4fzlYgL35qjftr-T0wsdbO69N2FUMm1REngV3L9oDmikWu9gi8AtURb84cZ3Kx12ccK7zgDUUwam0dbDFgQQYnc8FEthKtHt1VuzawSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/81689" target="_blank">📅 16:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKU5V2ipCFWfhRc6-FnUnzwstSnu49mf-tVu3Z-KhKLJcv8sey890iCH6lQpa4spq6A7QlqYFSTQxL-50bHpaUdnpQHJTmcLGS0Y65tIxuIfxmTW5rCWx92xAfcniiSpoFz13nNUfzhWJS9-q5RJ6kYMMAMG1TEk8bpyjmArByFkaMQT0G6kZ0M4o9G2kSzcWYq8yqPIyISYze4YLZZHALm5M3a8lLR5H_zMkaQLLbB6u9dtGljX8Kr8kWbNtXhEynNmcmbATqSdITiSGr-7XAo4gr3sQxCXHR3N3sHBGfclX5M3N91hhCnZMUOLxN6Zwgt0FRRiayBKzsJHValxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/81688" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1DAIACPAtHGXvkgD_hiCwP4Hd8Nn5yedxEFGhNMGPPdU4H-MGiAcyLPds9hTatYt1Y3BNrmAgbXOTLe8fvgWp4nFAQTec3wsSTvcDaAANV79pzuiTomsQfNknv2I70gtDZalSSMQFBHyueYLcY67WZ4bJlrXRbC7W7nT_2EOZIKSvOF74oUnvz9-GB1SXscIDXSGdEuk_plAKZ0IzPPayHwSKuB0fBVwFt6PFy01mxEmNw0Goq9pZPSqjzDP_vNc_DsXCOvSgv1XMZl42MgYn4955muOFuveYq7nzYdt2-RKh92R2XTOsZnuPHvPnO9xkFx-Tb6adSoYx6BHBaiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/81687" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
چین میاد بهترشو میسازه
چین به عنوان بزرگترین خریدار نفت آرامکو، قراره سرمایه گذاری های بیشتری در این شرکت انجام بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/81686" target="_blank">📅 15:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWNEK8z5Ceif6hEd3I_Hm4jdYTqJPADoDit10vJ9XGZwpMqWnZZTp-Y-8DeuMfJqpZWgxTw4cVvwZ4WnqId-XVbqpo8JpUHsu19Dgg_3l6hKAtwbYTV6PihnzJ-8gEMiBgU_IhAIBCxqqDpFyKSUQF0ymtxb2KAC8NYHLvV4tDrusCN1AJOB5W52-oui8RFulSuigBYWdUQJEl_0r9cS0TOnKPgPvN4CUzTJwmjCPiVWCaH3FQNqf9l0TitVC3H5LnKknMGY_MP3eP0Sn30SFgJQ_V67KNl97kAGa5kYdYBTwHteJqP4E2xGMeh0ln8l4sk6h1dXnFu4yNboo17rEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگا یکی ترجمه بکنه چی نوشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81685" target="_blank">📅 15:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81684" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81683">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ببین ما داریم چی میکشیم
کان نیوز: نتانیاهو و کابینه اش از تصمیمات لحظه ای ترامپ کلافه شده اند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81683" target="_blank">📅 14:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81682">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5edvptycMr5h3F4Tw_DNxW90l_35uWs8OqPCd0mbYxd4ERJysgxUvqE1QdiPldQuZJBDLRYF0awQhtqm9W63vCFRDNf-G4yBdJlONALinKJEAxlWesdds0m1p7owv_WQnVIrIjTOfS9aPLdJBTf5hi4WgHT10E-drQD-Y-5XbDwfDSbVeAVUOpq_ujbGWT5ygfs7QFVE5VZ2kajsAkKYBLWlxGw6EY5-622Bm-8fXFlfdcMXi3tv26n4EVUxvy3tnurMOaYlvfnhm_3jSj4HHWubMUJDvbPo_RbnCp_0dCpnLMAz1XHnJEG18UADAXgtcMPIJaUkJ9357tUF9mTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم قسم بخورم کسی پیام بده دارم میگه خب تو پولداری ۵۰۰ بزن کارتم رفیق شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81682" target="_blank">📅 14:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81681">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فارس خبر بازگشایی تنگه هرمز رو تکذیب کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81681" target="_blank">📅 13:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خاک فرعی مگه داریم</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81680" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jT2lZOFviMiGZgTvAjcGHrSvTP8KM9O1em40ssGPi_vDszfO7E2iY6iI-cu_twRTrTAoNwf_vwoh51DPRbYIqFIh8ANUJfXw9mLwBW2Br3x-vwW0T5VqoFsaCOUNPtFzGkGk0KoOfViECWbO17PDkThMDbYHZYtAyz9D8h5-XRZ48m38j1h8CFT7LiIyEYfL4ZAVwiSSFFGO5X1-PQUql1BMaZPUVdV3Au0jFkdE4pT0zTsGmGEqo7UrZuZ7PvDMUSCVnVGVod_mFJF4jE8jHkWXF7TNYW7YLm00u1HHSBX0g65LknskHtjoQaI_R0sBPUFy_vifJRI80qSKvrDnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3LogtXL9aeOsRDAWlTxC8QM4qAkhJMJ3Dp0DMG2kYPKIfjWvNP2M8FhBc7xPr1BCuuGy_Xfb6tKucLihOIYa4LCuYcYg04CzHl2yWqT5s1FvOI3utL1n6z29mSPQphQodPYRoAxOToMRmMbZjjUGuyeQ-0JVkZFsfM30QVszXotFtpS0UimBEftZVYe3vhA1Ipdia9QcMm2dDJang7i0NPxTxbZRKI37uEnHUqRQrkuoRsSahErBmRcVCRz5O6B_0CnnGzvXUzaGjVJK9A9CES2-yLUOxS68wDENi8Bj7hqb-2eTBVuj2tBN8XReT9H1p2vCr8x9OKcXL_YVqSXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسریا کسخل شدن فک میکنن مراکشیا به خاک اصلی اسپانیا حمله کردن
شهری که بهش حمله کردن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81678" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIqLrjrAqjewujPZl1wFBUuvENBwKEB5O7JYjbyyVHFGl6GO1RsHGEp_HW-A0NWO3fRLRxuYzrKik2d2XN_VCgIZE71cV6Ut1M0qfv6ACJ0gUuw4IfSFxq5l8l6x5lwaOLoX8hbfy3wx_Th6EFZd8YfS9b17u47k3iy6UOdt2AO9lFZfaB-xfx2NFoTc1h8GzG-Q5D-YQmR1t5kHJ1LJmkBWPctzHOqKD8K6v2mWvoLJ0YmhxEw6TYlb6-4NcvkcbzagPR1PSNksygjMD9ZNnpaTwijtZKAUwJxdxvK9cQIuI9R2j9H0gSq6Q0AQAUf5U5BXqeT_2GM9YiGP9CN_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81677" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyyOcJRNfoYypgil-u7QcjSuodrK80qLQHdkUQeDvT8ISVymhwSg42dBsinY6yyPItoc_86NJtbYkKoP2v2GKGvjzelzZuCn1lwYWr3eVjN5zAGlW9bCPvwagLHl0GUuHhfEywI26fmexzTW_IKiTA6XywzgiPnHnMiKQlDVYe5W-OQu2yDoFfz9Yd-HIreig3gFyb_xLNFTCja6tcFlj9BQ-_OiG5kEajUIYFaT_ica8YdGBZ_mXYNHst5pvNbVsVgVdeMg0UdciHqGWTS5Bj__Gnq1Ptx3RkyH8Bi_8IT4mBYRIIb26tiLw_geo0tXCVJBroz8F0XoDxuDpRjQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های یامال درباره فان هیپ هاپ:
اگه چنلی بامزه تر از اون پیدا کردید، من ابرو هامو میزنم.
#Arash
@FunHipHop</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81676" target="_blank">📅 13:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cybPwaKTrI1tWu7q-hf2gER83fMohN_3a92wUbi_3nPvjScPdlEJiiyFTD5GvIqnQNyJMi4rA7PdXC724L2zAX6A98Itny5EmIftqkvMoaAEfdZbur0RK-1NUlbP92kW2-jrpPP-5WJDRfM6bh__bp_sOlmucFRSV4KI2R585btTldO3yQ-ZmCw7ciMaSmL21CPFaIMB8tUgqsOrITLMQ8PTb4GiZCFMyrWEcYtccJk3hVa0jUJvdKflhgfe3h7Wl1RIr3lVvBA7iiMr2B-Jh3oTKO7iwzL0KOq7Iv-qYIYrE9Ckrbh8RAvsnv9K3RsNvNM0ckQpKfg2nZqFHuCFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ اسفند، چند روز بعد از شروع جنگ، رسانه‌های حکومتی گفتن پدافند ایران یه جنگنده اسرائیلی رو بالای لواسان زده. حتی یه ویدیو هم پخش شد که چند نفر داشتن با خوشحالی «الله‌اکبر» می‌گفتن.
ولی خبرگزاری‌هلی اسرائیلی گفتن ماجرا برعکسه و یه اف-۳۵ اومده یه یاک-۱۳۰ ایرانی رو بالای تهران زده و بعدش هم رسانه‌های داخلی کلاً ساکت شدن و واکنشی نداشتن.
حالا بعداً معلوم شده خلبان یاک-۱۳۰ ایجکت کرده بوده و زنده مونده، یه طبیعت‌گرد به اسم جواد قارایی پیداش کرده و به خاطر همین کارش هم از فرمانده نیروی هوایی لوح تقدیر گرفته.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81675" target="_blank">📅 12:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxa3cP_g-NT3-7gS4XjdaohO0UW2s945yUgzVXFOas7P9PJEvAWrFhXv83uEmSFnb04PpejmVAtSlG_G2KFBEsC9-blG2TwmGBdDXqqOT9hFjUYSXbP6JVKP1pzFHwwucBapHPIDAeuuDW7CxwvwcUD3ooLzwgkQleiHoJYdo3eTXTUM5h2RmgRPp86RzmYLwVnIfK410U4PY9x3gCwt0iJ5Xn7LpDJ3V_20v1-hI-JoG0aGQm0GK9QV8I5626SNnAgchkyGgUc6EcVGoBIOU_phLlmUjJxbWfKoFbq0CJnUEmighZpIQtLoJzw-PJwbVL-gVltlsp1sG53HjnLU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران کیر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81674" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بیشتر از همه دلم برا اونایی که دیشب رفتن بنزین زدن میسوزه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81673" target="_blank">📅 12:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYiDfspamMquTAvyofuTs-zSrlFxqxzgKfOVOBu-IM7smvtDbuCSjz2_OXb_pmcx1rEpJvm0PH2UL-XI_DwqpnsvyreK-XXpcocoipMsuQzlI11CXhlPUP89DcNSlnnp_3LoGOvZcGgzbYAd3iT8hFq8hVjizwUMcO3MKFK3If8gHX14mGkBoqELHBNDbuDqXdrKUHNdFKkIdQJ65YnirimH389XrTdqLT-Avt99ac_LydagAx9HgAO3J_CXkrI2_Lf3eR_YSKKwTKARBl8Hi7qQXcTgNg0A8py4zlsNa3CG6HXYzr71eWHSkLhh_jlYA0cAdXfwBt9IoICymGJZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقبی اردلان این میما واسه سال ۹۷ بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81672" target="_blank">📅 11:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=cXlWJE3S_FGkkzrTEJXTZu5ouUo1UB4uA1pQrjaQBN0ARmJugiscbqsyP0zfAz_VBe6roKlIfa9O7GUNRLTbvMHCBq5OSsd17BqwnV6orvddSURB6m5H2JtPLDKqgk2I8lv8Ze-r5dCq3Y2OID6g2y3yiSh3ntEj4s4MUp1Y169dAmev4UEzriZqi8bKVw1Ces1eTg5oNBCdOnE4Q0n4Ru-gXlNGzY2RuPz6_aP5RMzsYnptVCKh55l4IovEIyFkc3RCjVnCg1BJMFYrNPJj77divwSc7aLcM1MTPxfRdbk8-6Q5ZcseJC4X_nmA5ItGESqh5wNrxaHnVTjTniw9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=cXlWJE3S_FGkkzrTEJXTZu5ouUo1UB4uA1pQrjaQBN0ARmJugiscbqsyP0zfAz_VBe6roKlIfa9O7GUNRLTbvMHCBq5OSsd17BqwnV6orvddSURB6m5H2JtPLDKqgk2I8lv8Ze-r5dCq3Y2OID6g2y3yiSh3ntEj4s4MUp1Y169dAmev4UEzriZqi8bKVw1Ces1eTg5oNBCdOnE4Q0n4Ru-gXlNGzY2RuPz6_aP5RMzsYnptVCKh55l4IovEIyFkc3RCjVnCg1BJMFYrNPJj77divwSc7aLcM1MTPxfRdbk8-6Q5ZcseJC4X_nmA5ItGESqh5wNrxaHnVTjTniw9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صرفا جهت یادآوری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81671" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81670" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewZZ1oWg5uZvVCfH7Dedbow0-UP_cUAMBE4XRJ-M5TmBhbFMkfvg1oPqqyTDm-YV4DjtJdmCdCuiUCn87OkollVsRUZlM-csdeYzIz0FtkqXJrbru7OQZZtxJBnJR5b77cTGfvpiE5QTLh49CfYon8aMzlJsHbScMd0nJqmR1rYY6Qm1ZNP7aJ2ssVtD3EX6OWhNezFPP-kh3Rc5wiQPAsf9-Z-GGZX8sr-Co5yVZ7cfgfC6YOM_oXRqBJQf9FMydWCQDQTS__bxwFGDDkJWG9cjzgh6xij9a3Kwh5Z4OrqXXwVF0MOls_128zoUk9ArYL0sKPshqbrtn5VvFi45Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش یه سینگل میخوای بدی اندازه تریپل آلبوم دریک داری براش مارکتینگ میکنی، بده دیگه گاییدی
پ.ن: کوروش این عکسو با یه تیکه از بیت آهنگ Fiancée پست کرده اینستاش
#اخبار_جنگ_شرمنده_بابت_پست_رپی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81669" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بخدا اگه این مارکو روبیو رئیس جمهور آمریکا بود الان یه جنگ جهانی رو شاخ دنیا بود</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81668" target="_blank">📅 09:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81667" target="_blank">📅 09:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD2yfEYHNxhwwDY6Uo5eLGe04nZIhEUPJTt5Y5_8PRpjYmTxC_YOBFINrkHWLdOIGI84wzwq4xZ8crj_oDTMvmXb8TQ6pSf4U8pE1YU0VOT9NlJiQmeytF0CvU47AMZaVlbXwwco66TliLI1Ubu3ZPSiDzFfE2INHeWiroWw7Dh3FZab1caM3d9STS1H7R0PH1jfznZKvZ-6td9NuTJuZBZgys8OYp9hTVRebbhLH7dDdZqbMdrjgp1LFjEQ6etqpKEYMwedrL9rxKp0gk52k5RU56ivTB39etc6rfJ7MwGSq8hoiaSgivBYzMPq4uEr3xiTrOs10fYUt4IaenMVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#معذرت_بابت_پست_رپی
رک بگو میخوای باهاش فیت بدی دیگه این کارا چیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81666" target="_blank">📅 09:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81665" target="_blank">📅 07:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx9jrXQJEzVB591V1yVooOgBcb0cEBZhu5GuIWIl0a0UjMJbFFPoCQdCyt0uPt_89EwuQ1Q33TM2q_ojZxrdnb5OAmuOWmbSAT3-eiamybI0Jg7zmVU5CkxLO_HCD4lMytyfbH8CdAS-aP4OiCiWlS94Od7IjROQG8ovdhfkdShUlFsX_BZzDw1rZLKKlSccuHKDtnwR1lpx6RejkzxWheINwsGUSMVSGyye2Sqm70eMbIfcSRYRkbeFN9mTDx9tdbq7aalel-vv7HJoaW1LbRtxNqJJQ5CPb9fjZ2mOX139zGCIPTYGjduZtKQa4IFBf9AfB3HmmNquv1Mg3CKJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81664" target="_blank">📅 06:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چتایی که از ملتفت پخش شده همشون فیکه و تو ویس و ویدیو هاشونم که چیز خاصی نبوده جز ی سری حرفای جمع های خودمونی و شخصی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81663" target="_blank">📅 02:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امشب بنزین بزنیم یا زوده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81662" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81660">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=ErOJJna_gkZxR0gp2i_Db0L-CKvUWp9PXrOW3uHWGh3S3FNLKj-1N6zUsb5U9kwAiEFGbFTakTVxnJIzYHD-0GwxNbNMr0Y9eiZ51bMyNGH_1DhAApOnAV8f1DtukLvN0iQyT7oAyIcxgO0Ts-E5rEvrNSadLFiIY2ENX_BTouVG7N9Du8Qq_xwbT2vWrKmlKb7DLpKHdzNeUMB-83TVmApg4yYLAz0pJWEHD0Pk7UqbhcKMJPvt8I6s6xz6fDyJybc0_kwmPjxG5Ub9CRmij8x57OBImnni-qnBTPq3HRRtVfBfafViMoO4xh5q5MsNqANEGbjzS-_kD0MIdA7BHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=ErOJJna_gkZxR0gp2i_Db0L-CKvUWp9PXrOW3uHWGh3S3FNLKj-1N6zUsb5U9kwAiEFGbFTakTVxnJIzYHD-0GwxNbNMr0Y9eiZ51bMyNGH_1DhAApOnAV8f1DtukLvN0iQyT7oAyIcxgO0Ts-E5rEvrNSadLFiIY2ENX_BTouVG7N9Du8Qq_xwbT2vWrKmlKb7DLpKHdzNeUMB-83TVmApg4yYLAz0pJWEHD0Pk7UqbhcKMJPvt8I6s6xz6fDyJybc0_kwmPjxG5Ub9CRmij8x57OBImnni-qnBTPq3HRRtVfBfafViMoO4xh5q5MsNqANEGbjzS-_kD0MIdA7BHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی حتی به لوله آبم رحم نکرد، وصلش کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81660" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dc4y2UgccIHJBDD5cTxaBAdySIcdVfwTwsKnB61x-OYwooigRMDiRdbmILhGRCBH6E8DGwD1b4h-ly3A8Pp6fDkXICa_UlHYtGshdB6zhU-MaaAKwagQpc0Ic6KPXmQ1tIyncyFIX4Ac-BylBNPtKJE59mXQMWHGSNB6LXTuDr8qRJU4VbSbQ6U1iSS6rEQNNYLU0Y9jNWJu5_86Z19tO00zJ2tPwDgd9z8mQDHOAGWjkIYuNVvXtUqZIbIzdc5ZLlmt4B4_UBG84bI_3OcCy8I0V6fsne4LtNHRqLJN0efCWsh643Rk7pxrpXXJyLfybNthNEzvw8el_qj6cHkXCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dc4y2UgccIHJBDD5cTxaBAdySIcdVfwTwsKnB61x-OYwooigRMDiRdbmILhGRCBH6E8DGwD1b4h-ly3A8Pp6fDkXICa_UlHYtGshdB6zhU-MaaAKwagQpc0Ic6KPXmQ1tIyncyFIX4Ac-BylBNPtKJE59mXQMWHGSNB6LXTuDr8qRJU4VbSbQ6U1iSS6rEQNNYLU0Y9jNWJu5_86Z19tO00zJ2tPwDgd9z8mQDHOAGWjkIYuNVvXtUqZIbIzdc5ZLlmt4B4_UBG84bI_3OcCy8I0V6fsne4LtNHRqLJN0efCWsh643Rk7pxrpXXJyLfybNthNEzvw8el_qj6cHkXCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویسای منتسب به اعضای ملتفت(تایید و تکذیب نمیشه)
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81658" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81657" target="_blank">📅 00:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه بیکاری اومده چند تا شات و ویدیو از چت اعضای ملتفت پخش کرده که نمیدونم واقعیه یا نه چند تاشو میزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81656" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLXMqGVvi6yjFHXwmPTe7j3c4NNoJnXLpvzYA-uARqxNS6SJ1K2AFD1RVQz1Lsua_zBlBrnBLU5dmWRpj6esEVnmXu_I_3vcMIH0Ypi5qgmKvddJYz2q4XJB8xvZOGdoSrjpg2UCmZNJw7viUeWEyeQeSKNhHSQgPZskTnczyJ5B9grz0GJgPKoZYdjXykABvtYNTd9KJb1i4gIDCUBlZ5T3xkrY8JvIPXLh2ylPGYeUwKQ07io6D1xcqiPmstzSaAuYz9U8ddRz4Wf_LY_4pv0CatYPm-f8w1GkDS-Un4lkKBj8-rRnOybWq65YMlZbfDdTdrOfzBBZTwvOEXae3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5Sp_YUwDjxUk1ZQ1LSG2WVYTEMv15hUp7nPU2c9tNcKGQGmsmFriXKCKn48_8xa5rJY-4OGqIFmZ7q0riCUR1vSGf4n362ecDkvQuehmoMfN7dTsgs86tsgHQperguhzMFweSbSQkLQxdV4AhJpLQgbryWmKpX1VD5aIkpWaZSCqKDL29UslQN63H4Bvz5rvs3TrB7gus7AKaLgOo3-rXUm950Hc8jq-w-dnwFzZL42Hk10-YdvqBJt1kPXUPU9V9GrZtzcYIJrTV9rfmrOzhFuQM1foNDN1MH2Tdb9R7ENovmo3nZky4ExMVDjCcit3LT5_b_qyRPNAXqdlTizbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81654" target="_blank">📅 00:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81653" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81652" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زدن زیرساخت های نفتی و برقی برای امریکا و اسرائیل کار خاصی نداره
پس چرا عملیات رو شروع نمیکنن؟
چون منتظرن مقاماتی که هدف هستند در دسترس قرار بگیرند
اون موقع عملیات بزرگ شروع میشه
دقیقا عین ۹ اسفند‌ ۱۴۰۴
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81651" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r365DlzbjzLmilpx1DbPfFLB7iFjl1Kai6EsDGiMZpy0T_Oxdswv-8bc1vJKrNKUJ_r2UlX8qGAiA9ZWYdz4h85ZgqOvLVTLNqDNqi0uJKiCKBt8S7I0ULHXrXmtfcczoUpOMVsrExiI9U0exmlesd_KlwN5W6me-b68QSpPfWyC7DY4TL22CC_14ojaJtGTfvobSgPT8cOZHN13wqsO3JRulSn95W7YYxJ7XVYbZMx2302LqMRle6hX_IoBD8WwWped_dXTwW1V78084yadhTZiUG0WaWn6ZD8O-FLqpIgYSRegcbV7PyFvGoJGRwXPZZ86OS2Au54GGTHFG4TLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اکانت رسمی مرتبط با وزارت دفاع آمریکا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81650" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چرا کسی از من درخواست نمیکنه خاورمیانه رو ترک کنم.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81649" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbsEp8v_Q9QdmSV8IoiHJtuoihZsd0vWec6cgtgh7KeG5iCzsWgPwvbW43CzTvEhXPJCkI3NNeCp-lDAf-n63l4kiyBsVjFBksbS2odNFFV6fkpwE_T8nTzZJ51MLd3_cxClJIUOfPcn1TBuiZYOl7765IFdggZET-yqQp9Z9zenaflGEVEVUZ4jR8puuKnDoUCFIi7RaZVbzdnkXJe3h7Z0qPXQUYuJEiiOrfNgiIVp3ta-TlOEOF6v0OfwCo-GOyQhJZ5rT2WrhWx3hv_8GqpY7gta4OvjEtbN4WwcwK9obNUJaQOGxiFVvabC8dyAqJk9Gf53OSXBujdsz0h3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDmtg9MJFdPwtdiJka7kY_VuaoyVcfybWe1aPLT2tnPKQ91hdG7RwTV35JjFT-H2Py7-EdfNOWOoMV0UKbbmMz4oxRr9hlqKebHR8DCffjGQXMx6012uFBhq7fDeP231Frs8RN0s0kMeSMDS3tgvoUfars7XHi4PyfTeUtvvuAA0ubki_R8DWw0mAgVn1EyIrSYqf2wlQN-SZms5mOK7o5EWw4uPKHjH7E4dLPKG7Spimr18fcLZP7_0Neks5FF9dDvGBWWAtRSO_t9jwro-U0FeZ-HRQM8B7Ho14vaJYVa63rWI_9o4LDmvqyrBj2Wv-OW3Ye3xHrkKl9ohz95MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuE4fN4U6HOK6Qq_tReLrutcS5saEIEKr4ltftYGmAECTplq0GRvu90htwp-ch5lT5sTQnIBzsnRP6_ZGE9pbeI4y-P71-d867vmpAqaq6-JvxD0Ga4KQcbsrXZT4vvVcFhIDjEqxkg5AntTK3V4bWYuwE5GeWM-8iCvWYyrLlUi6ZxelMdgk2Trn4EQT1ktL2H6ly-gaNvyCiYE6WZp0TKYg9oEAWbJ2x9om4QIqmkPMifuyHNUgc1i5Ti9y6LgQsKQszPu7_rvop_320MicVDucTu1SeZqGnbCPWIH6Qq6a6r_XZTiZMFTwVnLTRVeSy6-qkH2NqNCO3R18aZVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaJ-Qeylylu_oWXYFeNtyp76-ZZWY3xqNbrJs8e_i7-bTkdZE6XZk4yFU8fLqy2jtr4YuPnMvx8xKuXMxD0P5juXFGPVwv3vr0CWHFrAuK_LuV74mgUIVFtLa8-lR0OXLYNTflLjTgNTWgaEai0fZ9OE6mWzjyVWZTmKhm7FAAZfnG2W2hf-tv3TYO2E1lsIrgzdQOATc1ZiP1lKv-Y1Qliv-4qnnrq_f_7jI_6ELBAai0_V7ofe42F1SdOvUymh1_Gh8LCptJGDwDwwShG8YdOmsAEdVtUchGxYeRHcJzXeAAzp6O3fgcqmDQbgpLG8LcvViFGTJQxAjMde5J6P-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfKp1ltaItHJjktB9TK9KAHbfs7XarMClEcZ8DbGuZJF4ggdZJvzJftabM5DMKjKxURpKMKuJYhztJ8Q9L_nPYavDVPGSeoPQVP8v4aV1WFz5TzR_HyJ5LsgNwuWb6yM2wB8s4H1YxJZyWNRgG2AiTnR8zRxB-DnbDb3c5P1-LkGFiF-SXglYLeL9tPNa9oQTS6St2Rpx3SjZEWuEYFAc75m5dLjzFJmqPIKyXmA7wAwWLRXu8-e8hi5i8SYL2AP1c20erZi9iMm7rUdNilJsqtXzATQpaMcUbhJP4AlKGCEzZ_SaqAu0_LcqUEIbQZUirp3fiZyCgp2tcSniRNKbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنها فرق شوهر عموی من با ترامپ اینه که شوهر عموم، بزرگترین اقتصاد دنیا و جهت حرکت تقریبا کل اتفاقات جهان زیر دستش نیست و بلد هم نیست تو نیم ساعت 37 تا کصشعر ai پست کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81643" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#پست_دارای_محتوای_رپی
سپهر خلسه:
نیلو یعنی عشق؛ شایعه طلاق و خیانت درست نکنید.
✋🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81642" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81641" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81640" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این سری، این سری دیگه قطعا میزنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81639" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
تخمین‌ها حاکی است که آمریکا یک حمله قوی علیه ایران انجام خواهد داد، بدون مشارکت اسرائیل.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81638" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لیست اخباری که رسانه‌های رژیم غاصب صهیونیستی تو یکی دو ساعت اخیر روش مانوور دادن:
کانال 13 اسرائیل:
به گفته مقامات ارشد، انتظار می‌رود ترامپ دستوری برای از سرگیری درگیری‌ها صادر کند، و این، ساعات آینده را "بسیار حساس" می‌کند.
کانال ۱۲ اسرائیل:
یک مسئول اسرائیلی اعلام کرد که ایالات متحده از هر زمان دیگری به آغاز مجدد جنگ با ایران نزدیک‌تر است.
نیروی هوایی، سازمان‌های اطلاعاتی و بخش‌های مربوطه در ارتش اسرائیل در حالت آماده‌باش بسیار بالایی قرار دارند.
انتظار می‌رود که هرگونه حمله جدی به ایران، اسرائیل را وارد این درگیری کند.
مقامات اسرائیلی معتقدند که ایران ممکن است در واکنش به این حملات، موشک‌های بالستیک را به سمت اسرائیل شلیک کند.
یدیعوت آحرونوت:
نیروی هوایی، آمادگی سامانه‌های پدافند هوایی را افزایش می‌دهد؛ سطح آمادگی در نیروی هوایی، بخش اطلاعات نظامی و سایر بخش‌های مرتبط در ارتش اسرائیل به شدت افزایش یافته است.
خبرگزاری والا اسرائیل:
در ساعات اخیر، تمریناتی شبیه‌سازی کننده شرایط اضطراری با حضور یگان‌هایی از آمان (سازمان اطلاعات نظامی اسرائیل) و نیروی هوایی برگزار شد.
کانال 15 اسرائیل:
برآورد فعلی این است که اگر ایالات متحده به ایران حمله کند، "اسرائیل" مورد حمله ایران قرار خواهد گرفت و مجبور خواهد شد وارد جنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81637" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH_viWI_DfNpeHBjq9N4Bguf5Iikdg8kG6lSMTsRzRFfqfP7d6tNo_hi-si-HpVM9nJPoIn_f2PiG4EoIEOk8nBNr0YpazTJSpZdcnm96ca5Ufts-Ax2EfbtNb0EQ-b2d5RiegX_iD1rkDxJ1FhGWO0LoXK5q_UPKW32jX63gXaGX-l8HtFlTRb_i2q-NKchEg_L4N3nWwfRz3VBZlvI7EdbNuPHG3isfHisKvukvYKOKAMuUa6XS4uxvzzzNQgRtA2WcALT2pmd1lf8zTEB7ekgIhNX-cTw_sEVWBR1i4Echs8RRxXyCT65cS6VdkuS_HZhZ2CaCw6O2So4eMhGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81636" target="_blank">📅 20:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpTzmswMTXSXKU0QNWGeuWc9pttPRxhJb_vI8AdcRqxfscCZzh5g9jSyzG10NEhVaBKQSeu_QoYCvH0JazPsq9ptN2s_xDojMWxOYrrjUWu5Y35dSg-uyrra9e5t1YYVtABZtGED8oZ4gMOF43Y_BjYGWoqmc73ZlNgFhWHYkJjAyAnXco5j6w1hn-1RrdFfCH5fUhBcbpZ3JKsi6-bJokn6zv1FAgrv7UsY_6t13Oq6grK2D_lWRjS9lvzMe4PYsIzrLgbF42IsvEnK5hqcMw_-awMeSeURsuTNcQ027sNzLf1PuQ6l13goUqlNv_FExlUuMgfl0LtdvrxJY-oBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که باور کرده ایران ابرقدرته نویسنده های این سریالن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81635" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗽𝗲𝘅 𝗦𝘁𝗼𝗿𝗲</strong></div>
<div class="tg-text">🍃
به فروشگاه ما خوش اومدی
🍃
اینجا هر محصول مجازی‌ای که بخوای پیدا میشه
💰
〰️
محصولات فروشگاه
〰️
⏺
انواع آیتم و ارز بازی‌ها
Ⓜ️
😶
🎮
⏺
هاست, دامنه, سرور
💻
🐧
⏺
استارز و پریمیوم تلگرام
⭐️
✉️
⏺
اشتراک سرویس‌های پریمیوم
📹
🤖
🎵
⏺
فیلترشکن‌های پرسرعت و پایدار
🏳
📱
🏳️
🌳
قیمت مناسب و تخفیف‌های دوره‌ای
🥢
اعتماد شما ارزشمندترین سرمایه ماست و رضایت شما، مهم‌ترین هدف ما.
از همراهی شما سپاسگزاریم.
🌹
Channel
▫️
Apex Store
📣
Bot
▫️
Apex Store Bot
🤖</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81633" target="_blank">📅 20:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUbzGxtUiq9dnPWep0Q596OoQSJn7okzkQQq8rjhO2U8iY9itbCK-KZRlozR8ZKZWFxwbJ7saLg5TpZ20C0Fwa-Hyuf1fVYRZgVZGlzG-gMddm_0kQ7HsO5L-Lp4xx7QC-0t4oBKvLnjF17wzcGUMQb2GdyNdJI0eNou9RyVI7rhANpG6swUn7g5BwrZrzlrJGh-0pfSv9ZhGvwnUGkXxxWEP-QeZJqt4WxqliV8aNEzCm2ZuGiWS8VrpN6pidet7gLmFsMz2rUNePkpHW1x9Fo0Lw8-S3DxlLvLivBN1bDzzKCAOtplxXnnQZFpVPXbFU3zHJFjJoqju0HwVY-Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که این بویان کصکش اومد بالا مسی خودش ۲۲.۳ سالش بود، بعد میگفتن جانشین مسیه، درحالی که کلا ۳.۴ سال فاصله سنی داشتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81632" target="_blank">📅 19:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjbc1r7n4hw_wVCEr-ebN5J0VnOIhdf3brjgRs18AGERD9vl-APt9s9GYCDns4Hbctlp4r5i8pB2Vp6-ktQvXq1BorD6B47vEv_A7wZCEOCrLjLejWAnMOnlgRymBflzuBSfeDpOo6KL3Uopk-1TfZaLBYlzlHvUOwnIMdBlYgpSe3aE7l2VA_FGXvQwwGDR1lncqjnaLXS8eljIJCZqq0RzBon4xweXsUU6o4KpHHk_63nzd8mcfKwbcySK626Tf4aXC8eYT2Z9ozWN2z-9EKPlROaYnxmNbdkmYvXMRTvy7Kz6QD1czosRB3zjWkW12OOnhEyeQ3hTX_WpPK3yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مرده که توی سریال کلید اسرار که قبلا از شبکه سه پخش میشد میومد پند میداد و همه میگفتن چه انسان شریفیه رو یادتونه؟ الان رفته پورن استار شده و بعدشم عضو یه گروه تروریستی به اسم FETO شده و تحت تعقیب پلیس ترکیه هم هست و برای بازداشتش ۵۰۰ هزار دلار جایزه گذاشتن‌.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81631" target="_blank">📅 19:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه های نزدیک به سپاه: اگه زیرساخت های ما رو بزنن؛ کابل های فیبر نوری در تنگه هرمز رو قطع میکنیم تا اینترنت کل جهان قطع شه.
پ‌ن: مشکلشون با اینترنت فقط داخلی نیست انگار، جهانیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81630" target="_blank">📅 17:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81628">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og1s7-F0PTuQ8GmvCFg3lrFXTXj92qr2k2D8yLgAjjZB2ErJ4aycYJ3MK0yWcrH0ViQ-1b3XDUMzjG8Y4W5l_tOexSpmPAQtiehXPgVHpth4SuBIlfWolS02u6eTlCuMYcNBwQt5Cy1H9g50TzsG1CoNVIRcl4CsoYp48h1LUoTS4qNo1h1a2v3RBGNohwqkOHdnyQvzAfOltFfnGw0hiyxF-m-6WvN6SFO4IWS6dPFLSlYu4NApFKcPrT7B8R92zH8d62WoMdqoqnUbPaVDRghIC0ziH7_C645EaqOqyxewhPfnZJh11xmz-vMQ85yt-cjFwvm_pgbCCqM_JET83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=ZO7HPjiJDiPEVD9McVkgLdEHS7jg4rMWw7s60_SV9qR9rtjlKDjTlBFmTNjHlIkJpVQZdHq7YUtNWEJAbVOP0jtsvopPRwNrettDE25f84mSrQcBsLHMilgh3-Q409TJyutO8wo3CBoWDN6GBGwGdlVvZfQJk3bGRomzvaerayPrUQOiLzhgWJmDaAywt7pZG3StBqlwX5ATwvXJjmNWukdg9sMtw_zqqLk0j_X0jgY42yjkcJw1jht8NwhGfLGjUXVTT5SlYN5lk8TTzKV1uT5z74mRhCwzWOa_D2tR69k8kNhDGn3_jtXjBkJnyfNsQCa0GjWYoNracAOwzy0KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=ZO7HPjiJDiPEVD9McVkgLdEHS7jg4rMWw7s60_SV9qR9rtjlKDjTlBFmTNjHlIkJpVQZdHq7YUtNWEJAbVOP0jtsvopPRwNrettDE25f84mSrQcBsLHMilgh3-Q409TJyutO8wo3CBoWDN6GBGwGdlVvZfQJk3bGRomzvaerayPrUQOiLzhgWJmDaAywt7pZG3StBqlwX5ATwvXJjmNWukdg9sMtw_zqqLk0j_X0jgY42yjkcJw1jht8NwhGfLGjUXVTT5SlYN5lk8TTzKV1uT5z74mRhCwzWOa_D2tR69k8kNhDGn3_jtXjBkJnyfNsQCa0GjWYoNracAOwzy0KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید سیدنی سوئینی برای برند لباس زیر خودش
.
پ‌ن: برا آخرین بار ببینید که نت قطع شه دیگه تا چندماه خبری ازش نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81628" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aifxFtx5-1r6kvm0g_KxVxxzrGUANhrcmvPCSILN-Ttba2OmWuoJsb8lHWrJywRWW0TBnNzVOoRujB2ASK2B4QJMnOmJny3IZ8SH0fx-MJcFpapjhqHbdZIMQl9u0iiCftkRx2ttno4dvCL37HCoeT9NcPU62I3swgLy1R9-DKX-jN6Gn9h2NXS-BKoRyM-HdpTPGSKyTwT8mYrHMgG_D4jINJcNtNwqLXcoDGqwuPad9r-rTUzYiGN80C-AfEKQzIpioH8cic_RmXVks2RglklK069tZxPR2n5eWHxrvQUikTbyUZGSouhBDAwePRQOMukBMIM2Hpp_QB25NmY7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81627" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81626">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انتقال لجستیکی آمریکا به خاورمیانه تقریبا تکمیل شده، الان دیگه همچیز به ترامپ بستگی داره که دستور حمله رو بده یا نه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81626" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpnlU24FpEm7neNgOGxpfkk_fOt2TSkjZvxVGUpkPUgqX10XQAtlWjgMpf5T-aLO9namCQ1IpDQfJTL1W1YgNXMtT_SF7eCxf13jfsE-T3ZRz5ECFyt9vRANspHEqLbVG6pVfpaCWWZ7R3DkmPCv98rsGLPJsG20JT7SQNRFyR1uJgcT87ZKqwefQNJ1bHsT8vJ3VVzh6EmzuSlxrJKitnrA_VHSuBlsLLIwDo3p_F_WXJOHp86yN4jieW5uDkCr4FfUbqywWh-W2288ol8gE3c240aGXqZI3wS_S2WUH7V6npPRYq-QJAumDmtcODWYdPpTNweDG2nGfASTz1CFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تانک‌های T-72 لشکر زرهی ۹۲ ارتش جمهوری اسلامی در حال حرکت به سمت آبادان و مرز خوزستان با عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81625" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امروز صبح آروین خیرخواه یک زندانی دیگر اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81624" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81623">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اول جنگ ارتش یه سوخو 24 فرستاد العدید قطر رو بزنه که منهدمش کردن و تازگیا جسد یکی از خلبانا پیدا شد و برگردوندن کشور.
ارتش گفته این ماموریت 4 نفره بوده و همچنان اون 3 خلبان دیگه مفقودن و دنبالشونیم
منبعشم نمیدونم کپی پیست کردم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81623" target="_blank">📅 17:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81622">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpyaCsAjF_8ePhhWK0gsNh_ilk8OSxo2DB_wGthP5wKrQj-rtChn9JHOqBqplwMJiEdzWl8RKgE7uMqg6OeJsOPtxgNBT_CTFpId7nFMouM5b_Kiaqrj_x_GsgG-254zvCldpYE3_Z99FaCkRIcjdsW1rOIe8bW9RWScP0GAFPjHXuYcONj2bh8hoqA3OikI_mCirv9oh0wloVcPfUXnPAryoVXMssaQjIn0cAsb9eINywk-n6sQj0V8p9hTuWbxbo2qhsvE-QLtGk2S9Kgdwm2FQk6Bxe5AU40vc4IKm8yzsLr25tvAfBpFsMNU3eMZ3WhzTj1PFg9Wm_wJiiTzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کمتر پورن نگاه کنید، مغزتون گاییده شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81622" target="_blank">📅 16:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81621">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سی‌بی‌اس :
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81621" target="_blank">📅 16:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81620">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep1xMBQRDOvkX67r__n2-0qS15y3JyRUxC1lU_4pBvKO0SY4qu32wEfkEj1w-sqo72RFZzy5WcswJWtMNjMs8jHIdGaYukegtx5DFJSkJU3rmbEViR_fsYEwkGB-NFAjHvg-MH30U8eJxoU3MMep0vG4zELYKi9iDOC3pt1CKtWVjEIin6V0epW0DNO3kwdFFtuUYIvtXJpWBB5ASCiL8xl4kEKTbacSkMkaSG2fESEEVPiBbOAJzgFYAk6xvgY0xm4VCZcRvAwCi5ic4rsrg25uptHCOGd9bmRhVOT0SIzvCbOeJP743Qoy2oIPMzRMQjgQ1b3bGIts34QMfakMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش چارتا چیز که ندیدیم پیشنهاد بده
اینو بابابزرگ خدابیامرز منم تمومش کرده</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81620" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81619">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wyko0TYfeVOl5ABN8Cwn4fH4y40rRyc0PNArWVIvt4H4LhbPEh1potTATy178TPqouoX0cDc89anJSKQDN28SZYWBEkp18vDertDMQJLQdYrnEnNfit-MidjDgKTcrlmHpawheyvV9eW8tUl8OPbhlA4RCFEkbAQe7ANpEFWC6zTgErvtG1S5Wa46uw9lHmo33l5WlM16KMCVlWRNHmGCw3z3ZGkJb5E21IAZnkPR79y1D-v0Enz5bdZBH7MMXNU96q6KFGrYdF4NKlQSdP6FLaRd3UaToAZq80C1qRgPx_UGtYEY80dlloCuThSs7MthhURLaw7OyZ-Jxf_FKWa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81619" target="_blank">📅 16:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81618">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN4WChilZDYJa8h9SuyB5OVwq94IIPpaZj7OTQZomxAwRvsZIPX2ALAD8CbgWQ6PrRgMfVPUn7Iy8pZSrKhzh4F7oogM_AFzuDH6OJuJwAcYGFqIIeh2srQkKs0xF3d1XhFDLi7fGCwF1085pNuFMGWsJo_Y5pIyBK735QV9ejOG_4EnpadlrchxNerr3GiMMQdhlh6_h0CjYE-mA0YPBTIQgNOk-Sw9SWyZ7Hb3JGpcsGVuS8vsW6Q8v8pLssJMI2jXA-GZGlt0pqi_H3DXOyqcV4rQ4Cvyx7DKt_KYHLtUnjOlFj28CEn9YKMoywCtRXps_rryXLn0t4jo3txd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگار جواهریان جدی معتاد شد فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81618" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81617">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07811532ee.mp4?token=Q3ZQz1k_ZMbTEg_7dDcBe04B_iLwuBBk5IUquUrFOiyINUf_UcujLOYcZ9eVSXyzg21OySeIFcV4AI_DyELxtTeB69gTWtG08RkP4HC-zVujO7plJfPLTp5LkplYsU2_jWU739G6nQ6nrfEbOvdkrxG-pQPIek6k1LtZRX2hZ0ICLIjUsyoi8DomfS5lnrKUC6RjHP6QJqB0LScM4NbkwHB-1D1dJ0spaqegG4XviG2xLsAA-gMAGdwBLk2Dx-5mV59KN3YnrnWAjzYXeiIp9r8bx1ByKswRQwoLZVUyVO7Xx2LnJX9LLlxk0e10UxDOJu9VF6-DZnGSGa1eZ9QpeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07811532ee.mp4?token=Q3ZQz1k_ZMbTEg_7dDcBe04B_iLwuBBk5IUquUrFOiyINUf_UcujLOYcZ9eVSXyzg21OySeIFcV4AI_DyELxtTeB69gTWtG08RkP4HC-zVujO7plJfPLTp5LkplYsU2_jWU739G6nQ6nrfEbOvdkrxG-pQPIek6k1LtZRX2hZ0ICLIjUsyoi8DomfS5lnrKUC6RjHP6QJqB0LScM4NbkwHB-1D1dJ0spaqegG4XviG2xLsAA-gMAGdwBLk2Dx-5mV59KN3YnrnWAjzYXeiIp9r8bx1ByKswRQwoLZVUyVO7Xx2LnJX9LLlxk0e10UxDOJu9VF6-DZnGSGa1eZ9QpeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید به مناسبت ۶۰ میلیونی‌شدن یوتوبش داشت با بادکنک پرواز می‌کرد تا انیمیشن محبوبش یعنی Up 2009 رو بازسازی کنه ولی یهو بادکنکا ترکیدن و با کون سقوط کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81617" target="_blank">📅 14:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81616" target="_blank">📅 14:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81615" target="_blank">📅 13:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=EW6YAMb6b3Ry_rN0UMIcVcqK7azPGrT8uiBy2Cu8aqEpg1PFjXIJr3zzlNy1jB9bU5TnUp9x26AHBEsWuN5UlTFaMXD6WYAGlAaX6_M8Tw1wqZ4OQSQ-0gplW7-qtH4jwElOPBgziQRDSvAnGZE5xXW3cpiaenmKjTD0r0kuKhhHOHjJm-j4opM2gbuVLSOZqqSndtKt0M8qxU4GKl1kM-PrOZrediSdK7nRUJvwa3T3Jd0FOy8sv1MoOKW5O2dmxUzqZ66I_7kWTkcw4cWqXh_3SviTUB1Es0VeHwQdOhV65w3qVSM0Utczek82bIH00zBPM2bTSM03BuYCbT1Qeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=EW6YAMb6b3Ry_rN0UMIcVcqK7azPGrT8uiBy2Cu8aqEpg1PFjXIJr3zzlNy1jB9bU5TnUp9x26AHBEsWuN5UlTFaMXD6WYAGlAaX6_M8Tw1wqZ4OQSQ-0gplW7-qtH4jwElOPBgziQRDSvAnGZE5xXW3cpiaenmKjTD0r0kuKhhHOHjJm-j4opM2gbuVLSOZqqSndtKt0M8qxU4GKl1kM-PrOZrediSdK7nRUJvwa3T3Jd0FOy8sv1MoOKW5O2dmxUzqZ66I_7kWTkcw4cWqXh_3SviTUB1Es0VeHwQdOhV65w3qVSM0Utczek82bIH00zBPM2bTSM03BuYCbT1Qeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با ورس شاهین نجفی دابسمش میرن، پس عرفان بدبخت چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81614" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81613">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ9nqr2XZtny7OyqWdlsdOG_vYAG_whO8O-jbBpfnu7DLTes84PQTEC4u7s5Ry4yU46jKVH97aFgT2K8XeI5wvxKrMFeIGyZO77HI_Y960hAVBPBBVv5nGq1iiRxrejW_0NvvkSkIdE-HGGltoYGxRHhe5FXkAV_20KBcafWiZD2WfD-i9D4fESnHi4HtC0UhbWpAnQE7eDMfsmNDsS0gW4BfghRzlCuiyBLDOJfR4iuVRsPK8Wtq-4OcBFiYanZb9ilb6ghXn4WkJkK-IS-Vz_oNAUag2voR0jMf9V0Wr3Sevk8EBTw0kR08wg5txUzvy7rW_KX19kIY0p5iK1_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81613" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81612">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پدرو سانچز، نخست وزیر اسپانیا رسما به گوه خوردن افتاده و خواستار یک جلسه اضطراری با کشور های اتحادیه اروپا در خصوص بحران به وجود اومده توسط مسلمون های غیر قانونی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81612" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLYz_rAX-DPxqwdHhYpHTjkAKY-Iv31tVXeXdNRvcb-8W6KR0ZLL4XdF4lRU4YDlYWXVMe2CZatSp-NCJaWs3gk0tfx0FYBavC5w7O7MgDMAObhxc9KzKzE84cIgJ5NszsiUuQsN3lLAvyaWXQnSsiyhwgHTAIJGMiM-BHEvWV9dEvoaw0wNy-0B2v-tm-FSSoLnbCCvJXwcT9UmY_iVBgGqj-7VIKCpW3tAxQUOF78ibblNRQL47Dcl2zE9rEMM8beFTLmvUQd1B7bquVJ3E8cwGXY1GDCn7Y0y7LGS8JnWs3zo-MP0V1H411vqTyW_6stBPna4sRGd08s-LRdNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا به این بی ظرفیت چیزی نگید از این به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81611" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امتحاناتون بالاخره تموم شد، چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81610" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مثکه به دیتاسنترا اماده باش دادن وقتی جنگ شروع شد سریع نتو ببندن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/funhiphop/81609" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">راستی وارد شنبه که شدیم بازار های جهانی هم بسته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/81608" target="_blank">📅 01:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=QWOUBrLFlsx4DE6S39AUQk5UIkdBmoBQEHGhLils52G1SkE8lSoFUtePD7quzotlV5u5NC6faJiV7xlCgHKEeTZ9g7luP36I1A27z1oA_qn-4moznLMw0O2pXW500vO5mf2_Z6BVVYI4XfXcIKvoul5Kb6HFoEFcx3f0GZ0UIOFC6k7IJXUn3_cv_RYrPEhUhaGB3RlEhe6FUIZ69IqsZKiuN7uiiCA_jk3CO6MkZh2k3cvKVFVDW9YkZjrn54ZLCoNV60zLbzTufdVDcH0ovm8Rp3YnOnCfq0iwXbhsPr8nnCHzG2MKaqBeKl4rQXvNoI_a3snM1fXQzDA5-EMbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=QWOUBrLFlsx4DE6S39AUQk5UIkdBmoBQEHGhLils52G1SkE8lSoFUtePD7quzotlV5u5NC6faJiV7xlCgHKEeTZ9g7luP36I1A27z1oA_qn-4moznLMw0O2pXW500vO5mf2_Z6BVVYI4XfXcIKvoul5Kb6HFoEFcx3f0GZ0UIOFC6k7IJXUn3_cv_RYrPEhUhaGB3RlEhe6FUIZ69IqsZKiuN7uiiCA_jk3CO6MkZh2k3cvKVFVDW9YkZjrn54ZLCoNV60zLbzTufdVDcH0ovm8Rp3YnOnCfq0iwXbhsPr8nnCHzG2MKaqBeKl4rQXvNoI_a3snM1fXQzDA5-EMbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های اسرائیلی و امریکایی دارن کسچرخ میزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/funhiphop/81607" target="_blank">📅 01:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTQ4jS2BI4JHEpSUYELq86p_JF2sPR_IEK565nNpIzpS5pLVO_g7Qzlgb6JUg49J1KrdMCn6XpwMdWfD39dSSD9neCiZbFdzUkHRrsW2a9yXwM11faO5wn6Gtcn0OjhZ9yO0Cp0RKAWOh-pk7e4VmG9tqh8bu1A4Z-DfvUYEuOENEWGGn50odjm3ZDUOwyYofXoXeNix5U1ev6UZ2YodbgZ7sSUGzFKYIciGJfse7UA0KpNww_cyv-BeK7SHlOvtXCAj2EA0A59yxBfT3t6UZmGy-5oQtkA0_UlNmMlmAdV1e20qaPrKfkOBxpY-bDt8PTqqioQmgP2ydwJ1iK1eJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیما کاتوزیان جزو ۱۰۰ فرد تأثیرگذار دنیا در فهرست TIME100 سال ۲۰۲۶ قرار گرفت.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/funhiphop/81606" target="_blank">📅 00:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɪᴍᴀɴ</strong></div>
<div class="tg-text">گویا دلار تا ۲۰۰ قراره بره بالا
سال دیگه که قراره بره بالای ۲۶۰ اصلا
همین امسال فرار کنیم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81605" target="_blank">📅 00:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwIN1gwjR7i6vVKNVXXeXBApb76JGdyGNXOFn4CjHcsI-fPDtpEtXW-O3tzEperoCr_FVjF5MAe9KlCg2EDIbW18uVJA8D-oPZZ68I_J_1T-H_ikKy_901nh8Y4LB_YyCCHZoNmdPUc0pTlmSFXYxN4h6H64dflFdkaBoFfnk-Vkt_8iaSyYYro_SC-plLrSiwG36XZMn-Md5R9n2ETvBKaMzifguchpnXzeTuUM07X_gpcvyUVb12hq02CkEWmgEF1c6vVXgI9mg-9O33QoDthgi9ew-uEkcjhFev5-XlTzD7GDVlI-Dk1LLHJCS2iczkW6vU-QA1G3DoNfG0mGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81604" target="_blank">📅 00:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=NqBYRyXv-T5tkv0n7PP42XCTFB_CpXWKSmELoBNodHzq8boP0OoPkgfb49w96cz5aFVocpm2cGXISxQ18cZ5WE_BcqNM4-1RZzKpyoeye9QmNRW7zEDhs7aKEZ1pOpheEXTiIaB29fnaIfNli-v3HRr5pIMu-6P8qujN5OhuK8iCLoBwfCuqRY1Fb5WADlxR_ACLXoOHC-vGSdrukcfpW0jcASM0HFgp-Ns2DQycW1NZAzKQU62LZL8Qk1GLDgqlgL_1a9mrmBJss3WaT2uCIVbrfvHSzMHuoPUxyphJyXuN68WYR9BFOGso8w-8Uv_b7zqbqMenZuu79CWqV6l96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=NqBYRyXv-T5tkv0n7PP42XCTFB_CpXWKSmELoBNodHzq8boP0OoPkgfb49w96cz5aFVocpm2cGXISxQ18cZ5WE_BcqNM4-1RZzKpyoeye9QmNRW7zEDhs7aKEZ1pOpheEXTiIaB29fnaIfNli-v3HRr5pIMu-6P8qujN5OhuK8iCLoBwfCuqRY1Fb5WADlxR_ACLXoOHC-vGSdrukcfpW0jcASM0HFgp-Ns2DQycW1NZAzKQU62LZL8Qk1GLDgqlgL_1a9mrmBJss3WaT2uCIVbrfvHSzMHuoPUxyphJyXuN68WYR9BFOGso8w-8Uv_b7zqbqMenZuu79CWqV6l96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترام:
من قبل از شروع جنگ ایران یه نقشه و ایده میلیون دلاری داشتم که خب ما میریم توانایی نظامی و هسته‌ای‌شون رو نابود می‌کنیم بعد سریع خارج میشیم همون‌جوری که به شما گفته بودم؛
ولی اون وسطای جنگ چیزهایی در من جرقه زد که خب عقب مونده، تو هر چی خراب کنی اونا دوباره می‌تونن بسازن که، برا همین الان دارم یه ایده میلیارد دلاری رو می‌برم جلو که بتونم کنترل و نظارت هم داشته باشم رو همه چی، خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81603" target="_blank">📅 23:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیویورک پست:
برد کوپر، فرمانده سنتکام طرحی رو برای یک عملیات بمباران گسترده و طولانی‌مدت (به مدت دو هفته) علیه ایران تدوین کرده که این حملات به صورت نامحدود هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81602" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7mf2kHcCXu1fCcesw2mDnM59jH68ASzIqruT92OR6mU8_iRwG-uYr1IiRxxhBMpXiKZY7_QcFZ3G5dAZ5J_-whTp_MCkek90xOjWTFS5-Chud6vufZ8YQOrdJJCI4iEzBuXRMZp-3vJe4p6gTGQDlQ6yv0DSPt_SCWWAvnUJwbgU2yu8ghnv6JqviD097Ij3bICNhZXL2XCGKdshF_qFRq0Cm8RATrFPaxIPJTgKT58M7SQv5Bz0E0Oa0HiJPeQJSrwm1_sFMrAVDDZtkU-lTn8KmUM9JmaVDP7DjJxfDPVh0DqTuxkPhhwhhmJiSNy00GC-7uNITaf6Rjn-27Gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cwoo1fVrIv92uTFkK94hL8adisxHh91uroe0Q0x2A3LTvSNVaeE47tJivzpSHWAK3pDlaqPojJ3Cd1Cu1k2JPYsh0LIzE8eD29V1irJuBvp6HVTZts7kGixOebEkbIcobYBlq03Gd3CjFdQ867XqKVrMVFG-ekU-ZsiaKvOG7sSQ24nYkKcJmFu98XMJy1MWpHCeK0vDfawwCLYmF_tEKvm-U-pf07QZMRFq6GRLec6XLffezhqM7Q0CEFjD-MKEGb20KH-ARRW0RpahPZxbWpi2IarwLWC64kb4z2Qp2iKsbl1R-ulI7h0885GCJktGuSRBewCUKGKrwdCr02MGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MybAvruhJhDtsU4WcZoHjetT4jwKHHypexAKvH_Cspxjr-1S1Mb5HTWjOk0vcWSC14c1KTvTyDKdblAsRPSzASRmXbWYm15UYv_q_wUyHhlV767wypJ-O0Mkwjim4h2x8gGUtvdbKeDHcPhrx5ZyQx1VgqeZvCb8J2QnM_RjGOsmTLM_IneGqTcV_LIY0RO2GtVBuV6GhP1p4QOQXJtJUj4MCcZ-s7KwT7ozHGOFCR6zrmaxl0cTSEjGaMo9jYBLytIOEH701S9xtUkP08mimw33JZfWr3LEO1xjpjbkbey6Wnw3O9HNS385cR7prhdRYR_rBMcEjAAeeJ4NrZJPzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10712ee047.mp4?token=na8jr_eFhIiEv1tqPHNvwB2BpHaoLQzlPd6egJ4goesm8LGFHQyo-wXhcSJ12ZWFsSD8ej6t8IIiWh_w-2HltYnUoevkr83Kg8nj1toQ9JVZ6jjuMqzKrwqEy6P1KZsOjr_TY7LAY50kthdsSdIx8kYxW3d7obE01CXNriH1QgEpTkY6EiBb9NTWlLpArVYwBrJJDUy9RbDzx4sBQ_AGJ15_jYd9Iakt69aCndNfhfLInagMnCj24bBelTSacGiWmKS1CqRKcKJVQZ6_-MVZpQcB8p9_E6dHL9u48xNRdamLgBD3l2orfu9FzA5XdricXBOz2L-ebsMunldTt8U-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10712ee047.mp4?token=na8jr_eFhIiEv1tqPHNvwB2BpHaoLQzlPd6egJ4goesm8LGFHQyo-wXhcSJ12ZWFsSD8ej6t8IIiWh_w-2HltYnUoevkr83Kg8nj1toQ9JVZ6jjuMqzKrwqEy6P1KZsOjr_TY7LAY50kthdsSdIx8kYxW3d7obE01CXNriH1QgEpTkY6EiBb9NTWlLpArVYwBrJJDUy9RbDzx4sBQ_AGJ15_jYd9Iakt69aCndNfhfLInagMnCj24bBelTSacGiWmKS1CqRKcKJVQZ6_-MVZpQcB8p9_E6dHL9u48xNRdamLgBD3l2orfu9FzA5XdricXBOz2L-ebsMunldTt8U-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و آرتا دارن موزیک میبندن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81598" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔞
فیلم های بیتربیتی با  زیرنویس فارسی
🇮🇷
تاحالا دیدی؟ با ربات زیر میتونی کلی فیلم آموزشی با زیرنویس فارسی دانلود کنی
💀
⚫️
@EzzyPhBot
⚫️
@EzzyPhBot
تازه میتونی از
💎
Porn هم هرچی خواستی دانلود کنی ببینی و برای دوستات بفرستی :)))</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81597" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs4E07B4fp5LGerUPmDYs3gchOe4lCd3gXXj8FInvjOSxexuh9ukjVIZ1j0MTJ5zXdRHq1fcrni8Xc9UozM9yOJJX1kM6djKgioDNHUQTUS8xAVXtyHvHnWbIBCravXTRvuMF1eAXO_GEIrwvhg8O5dTQcE5MEHrjviABQyDFgtclr6xCipjPxw5BH4GUl6MzbRerUcvHNZd2EdJ8zBQZ05BH7hwGVbeht-7VHdaRXfIP6xLY9QONrQGCmBgdvdwFXYRWRiv3LRz9RGnsHICFNUQfNdE33DQHTx8I9qcaNOyo4BHUikRuo0A6jHbtc6pMMBD-Tk7sY4AhlpsdXrp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81596" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81595">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va3ThcdlGJdWWppWXrVh40idLvetbHPaVR051k58Clo5eUzbnqD2MNj7ydV8vDiVg7JN_Q7ttlVZ2gjpRErQ4kfhYbDZZErrq4X3qRSs-NaU6EaOu8CgRX7dsD6RPNcu3ny3n-jRuWPzIv-wqnnBnwyk2fIKEseN2TZbr_wsrEi7_2KZMylJIzHRNoKGWnvdm_r7Lk9nFvbFkjhUTWwjml8aPwjoacKZRWdys3UWia4JBzjT7sgdTD6qr3uKbsLr7peEggjOqcn--DB1QJoTxVK59H5_N6cwTXdip7io5hhBQq1vRrVcOWrzdInRd3pKQVw-u-Fv5uWUmuKQTgiM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای عمو هایی که میگفتن ما عزت و احتراممون رو با برنج و ذرت عوض نمیکنیم او عه او رو بخونید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81595" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FwRwFPCprqsVAVTbDzcKYi2Zmu5i8ivQU-KZM9bgbhKNSxarBHvsO7VJRmMl3Pf5Z1srQWO0v6lNDb8ZjWzlbL05R5fve9pfHiDtySXf5Y4jzDtKKarYwMhiAxOa2I05NaMbkmS_Z9lmoLO8_ruhl5dqo5G7FQMz546Mz7JVElf5ensG2AZYriIrBATgzoLZEXXT3fi0h9BpUgbiOC3cA1D0EPwXgguVtzo_ZrycBKL384gYk4eDVUVaSHKaNoiXcrF86Fs4eoPvzdBRErsfc-lqZBAO8CmlVOTZlvI7o3rapFOUgBIiO53-Qd6ahyqIpVsRIZ_O_AzwIjoRCyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj0kE4b3WN8qeVkDpP7VxUVEA-e65O0lE9g5ymQ5LmfqeV1rDqSQJmCRwN4JMCcoh1d_m59KgS94w3UrPN-CjQty30TjybtdKTHsUjzM6X39tI3I2rhCtLZLOROKVcdSOxvaY7QwZXJnIp7dX38UdmoyKXoHY678MaGYFAODP7-4a_VLeJesm3sMhNX7PsFR2iEdi6idl4l7yWQsO-0w1VNl1N8vowpEBppghkVhcR9ybpKJFxgZm3c7EFMuyHqRtpP-1OU4MyltPh2pNsObiT10FtmzwAr3kqjU3g9gSS1qJqow1WKJSuElBduw-dVUvtfC1TImfvkXWPHgh4kwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81592" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU3QACddeGYwy8YKH8XtO9slbk7cExLcWBgpmLFQQqydhDmYKaYXrtQX0vnvEnWqLfEvbU7Vdvbltws5tkcWaB50w48U8hcxW-2jUJ4XP4vovYbu9Atqn3s2UFZK74B-sn0KMZU49mHfWSK_GQ7QFAE_DKrRO4B3mGmXqvfQR4N3SxnWbj1BXQ81_N-eAiXheSfUYnDdBWNWI8YWICbzDYSBAjiTMtqgaNUCrG8Vi5uRN1YqNoqz37h3MCernJcgb6GVHZacPVPVvP5DtExxrwtit8mcfaQq-wF3-5CsJBs9xZkTPPFFXND6D9qJ32Bg_4dP7uMl132brHA4KYSsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد
آقا تو کربلا رویت شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81590" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMcgjdUh0X35PJAioMIgt3uWD_0s2VcKRyzxsV44aBvmZGd6WYhssE6LLU3zH1yP8xyLtRQJeztaZsaSy2Bk3OZJYsGg38BToeG2-KYrOrgdiP6U79b2ZlgF0tjd3SFp6Bi6o6UxbCO2IKsrsVqICGDiotCQp9qw-vIezUlp043-EYid88RpIgchZm631QzVR0i8jHcg321_MBOsd7_3Jlv7s-kV4MZIBc-qSOGJwtbHRrrkG27uS7msx3X7vSAOuaOJNFBdU5UMqo5KVy8Bo8C0qjVn17PrnOZvEItW7_a1zR29VCgLIZAnZTvuqoZIQpPECbkrER2gWd17eKmWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NopJLpbcEpvin3Fyfv_N5itb-u44usjRcyMJiPpnkuf6pURHp7qclk37_F1kClCZYmPtQl-gnxrPsAT8ocZWfqmDtxTjruF5ZWMpMXK6drUutY-cidYykrsFaBsu_KVEMqbKhmDnl6nQoLnlZ_BDsCKpF8yzhvNOIEcl3yPOaabl4kO1h0r3WeFd3GoCV9NmXI1OjQl6B2uKQFk4FrI9AOxn2F9IdlHMeKSJ9t2ifglMoKLHIlzxdYp5ljPDws6f4BjKLPO9x5P4pD93Sx1gezeJYytAsWm7NM_wN7pJ0h4hx2K2RknsujGRSYdKhbKDL8Dh_OE_Ff_ZXXJTB1wAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=aEa8aRkwak-Knfz1_IkZIOxmHrq10G3mOZ_2LzqsAH2UnYIUWu0MzuxrRHHLuDWiDrKsOCVqZdIuPl-fjH92svTRcKx1BWpFtw__xO3aK-zdM8cUxdUeacIHJPidhUGNwJI7e0OdwW5i45g4Zc288ge2yFENCQbeaiV-QJZ3rhvMawcR0d_k4jua6EA6rvh215tr1ZuCEsOa6Booa_n5bnoXWIUmnChDcm5_lK9lqrtBRPUAwfBHv5eyVA2SWYhD704wX84V9rXGuwnOD2CKxJGCiSlbBNFLYF5El5nPUnmoxHjP7Sb-1rZ_7QYeBm781NMtofSw6IZp11lLWx0s4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=aEa8aRkwak-Knfz1_IkZIOxmHrq10G3mOZ_2LzqsAH2UnYIUWu0MzuxrRHHLuDWiDrKsOCVqZdIuPl-fjH92svTRcKx1BWpFtw__xO3aK-zdM8cUxdUeacIHJPidhUGNwJI7e0OdwW5i45g4Zc288ge2yFENCQbeaiV-QJZ3rhvMawcR0d_k4jua6EA6rvh215tr1ZuCEsOa6Booa_n5bnoXWIUmnChDcm5_lK9lqrtBRPUAwfBHv5eyVA2SWYhD704wX84V9rXGuwnOD2CKxJGCiSlbBNFLYF5El5nPUnmoxHjP7Sb-1rZ_7QYeBm781NMtofSw6IZp11lLWx0s4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=B3xJNlWMQBI5YbTn7dfFjXswIQ5vOLdMnbRA1kNimb1tHgfWWuRi3c88G2jcXWgEBd-r9UFZCsg4hDY_h0TJ1pCQWjymcRggtpuloweIs8hb40MU_coTVHMTUY_J_jJwIV2EPATsmxfvXexAooSfhUxboHp12zVI1x__x2_GOQOpwIpGlkan9OsF_edkaqCsrFkc4A_I4y-kkbSxSik_JzufcZDWRrXfdHqwH_tB6moh6qEnkzbfRaOloZ-todvoCb1EKL8wwKgU0ZrpP9MCCw62uR4_x1Nq0Mhh0O8Ivs0JnpNUjP5e-WfoGEWKQHDJCSRxkWpMc6KSkGHqSStXWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=B3xJNlWMQBI5YbTn7dfFjXswIQ5vOLdMnbRA1kNimb1tHgfWWuRi3c88G2jcXWgEBd-r9UFZCsg4hDY_h0TJ1pCQWjymcRggtpuloweIs8hb40MU_coTVHMTUY_J_jJwIV2EPATsmxfvXexAooSfhUxboHp12zVI1x__x2_GOQOpwIpGlkan9OsF_edkaqCsrFkc4A_I4y-kkbSxSik_JzufcZDWRrXfdHqwH_tB6moh6qEnkzbfRaOloZ-todvoCb1EKL8wwKgU0ZrpP9MCCw62uR4_x1Nq0Mhh0O8Ivs0JnpNUjP5e-WfoGEWKQHDJCSRxkWpMc6KSkGHqSStXWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVwB_Vkc5Vl8echLR4CEk9akA3cvkhtXDce-YkaQJKTwH5JAE7n_25VkUXjxoi-Tx2I9cz5NF8ve0fysB5_rj8XLDgZ8xJanVQpkl7C86kvYaWXU56-UiTGqVvchoQRMgsZWzoo3ZS4N_FeRTQ3vxY1T3BRbwTeY9PIklNjSYbDgzOxEN9WJBSuBN7h1W7SdF1q-FegFu3JnWefEgnPmyWWpj7R5wIEQXeZeP67h6Bpl9X9v9R5FuCTXDZft0PzSRWzviZ9C0EtOswph2Hc4--DjTTaCSv5U17cspctjUjjWM7iNEIY9CTr5eZVvGUFUqVcXXza1xZFjMlZz_tal3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cX88ZnMjOwy-8XbFl2BvVoBRMu4j2t546ET1IAD7PzxnzeY2_-dI8P-K5wSwWw8jw9XsRlaNh0suXa2ObbX5G2OhxrJSpaMDqhThznoDR7MO4HWE9CxRxhg1Pa8cedLIP3rgxei7OyBANGIr0ROSXCsVGMVXyeRu6bMm4X1mPIlFzWT25BHP5WRMcA-Dx7wnyTsU3BWuGh2WWNXoSiPzTL93dHr1Wxyl5WIbQtj51sbDsBs69ExZ1nh7hM0sNQmABECXDvzuCakqgcLCxCqn4ngwAxLuIy5S6VV1tRkCPL7wkh-suRdV9CIXDdVSVIUWbDKRSRSPrxBXSp-tg3KWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3Xy_kcz1GH0cirRb9Wjw2FsdOSvtyxuLAV-FPyEvu_dbCPt8FuIeKUnkMMsIXmJOCEiyFJFYbG2glIc6yAH6D-ROYGJ9N0ddHmNpg9bkrZ1Om8SafoOlXC0zxo8kWB9naAy6LYzyCZRKlYTWiBqjIQsz_MSQUvcJZdA0aAAlE22Xx_miCkoVraGL8gF3NB-XdYsIvXrrW9UF_EWLST8f558yhc4lfKwKZYFumCHu3WkyZ3k56zdv4R49Y1zd_jZlaP8pESk8bqY3J4dPKBq3r4FQ3vfhHXwflrnlpHTJGTV_FRiMXCjvpRj3vi12s1dk-O6d-jO_3NyWEq2yR9EbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEqqTp85taJUHx80wLOu98rww9HYJDkUrT-wg3PbvMDZNHAnyiyRWPGkw7Vofs9p4R4UnL61-2XlnBB23lCGgVgJkm7KeZeYLyVMp_VH65a-k8IisiSVnYbPPtH6PmtETUwXkj1DcY-294RwPeRl3xAO5O-Ynb9bSlVKisZkHE_UevJAhdGCuny0CTPPhTIxuMro7Ea5-KHuCgxlHEVghDOrVinuyC1jr3YVpRAy71CYWazUUqIeHpXWA8O4R0R1Z2qJPytWY91nzts4XU6LwMXUf6LoYvTZrLNtJGtSB8N7c7Z9r1GGEGiNnUXhjBnzljwi8VvXAvz-nMR5ArWdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4fwZOZdvCG6NEuAu0MTtMEA9XgaeLMQFV1mLAFecxM2hSJikNCyn0BK7DjXG-03emdv3BBV-jbj8_sTZ9mvRtFqBoAqXG_opu4dsJzyMFv7dN4p2jewoTJeTHwsoeS-J_F4BtAnJLv0aHL_7-297W7_rhcNFKjVibFhfgP3mH-rwiylxdk7-XHnsxuXH6V32xOYLZmHOGx7CmOgKGlWRhWc19OajTjSy3uDdZJ9AsQRw1HXk9SoqmBZ_aX0mERarT5EQ4TqfooWCS4_88bTEzSWQOBysU5QQjyyljyyw4FaLO_pbE-V0y20tNlG0A1Bqzo6sFVNSCUWLaK2UiYYuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMHplFOQGU6CLKZiYMq8q_kcHUNTxW2iSprmgxKwdDgRXhhEa9PyewBsvEsvnCMA6ZhMH5Cz6jINsJFltzExwIIM43ZQ3peiUYfMDLhZn5ih-CgBRXAfDjvAq4R1jKrjdMJEnzOfO934G62P-9GvZ6hrsSD9cjQtpNEIhVj4lvhR6s_aIBJ6qxBvXLHsjHRF7hNogLLQrgORqdplGOBCHqWEJZFG77-A0q2fk8YsrxrPN0rsVCMF0pA9bn2VPG9eLHW6BR9fLoivab_kPOgx2oo4gX0CxyO59bHPWGKThgwvdnu2wl4h4rNHqSLJCfO2C9i37uWeA9t-KhIDY2KhPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
