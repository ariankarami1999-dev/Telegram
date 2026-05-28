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
<img src="https://cdn4.telesco.pe/file/un6TNAbWI5MzWD1nf511yrkNGLxTULc1XXLbtUhaeLl5eDD5wxYwEz64CBcO9hR1AusC-niWIYeESjMc9FZw_NsNPmLKxfNDt0TAsBhOuF3F_TSfJE_phpDneo6EFr_6y_Nznnh_Awu4SsEWiTgEySbEmmDk6T1AAv6dVQlUW4XfhH6lOnyD-pzcCAuk91QezI3oA_3xmoi6inOBQpc3mOoDK4KxNZRfDOXtKOCEC8ozjVfuiYimOp5BnNsPikB73_-xkvXC1YMb-R-HT7Q68OIvEDHrrTjTrhSNR4up1GlkXP694QKdx74IAVBcwEu2m4IEocjwAde9ymetcMHOgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 278K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-12784">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNp-Q1AfnVJnFLp8-j1kl8VBie82pEF5lM0-WOLSUZkO9DfR_JGkj5xbfid7-0sKcr9KxAMoVv315RNcBvTccWD5-fwxONUgS84cb2stUOGHcAf6uUlczoCf3kLD0S9HizW7m4cYBO-0G1cNJ0skTAx4oPJAEgKULQeo0EfIlTQuDsXvorjBmpR3dTFUF2E0cgb5v66TjSjoaZqyKx0pZLrQxBquVN079E58zNgJ84cIj6yNdQ1PqLbXin1sXdMsfcc0QQYWUUEKO2JqvwaWIeO37oyDpd5jNa2M2OrW1rpz0syYSG7BxWepdlnLYjS0DVCy6Snw_kJ0zU7uxSs4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک Ai موشتبی رو تمدید کردن و موفق شد یه متن طولانی برای سالگرد مجلس بده ، از خالیباف تشکر کرده و به امریکام گفته شیطان بزرگ همین یه امضا بچه ۴ ساله هم با پاورپینت انداختن اون زیر
🤣
@withyashar</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/withyashar/12784" target="_blank">📅 14:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12783">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUWsY0oLw9jRxcZm5BURYjaDxEKNWb3p1TcX2rWi3bS7Bb-G8oSEFLzRZtBMlH-thxCxqqSJsnK4ixo3UZHsdyNhYSw570dUvUHAZoTXNlTIREFqgLRlGiQfYBKJxnPDJSULsmxrFc_KnqjEiGe8CsH_zieU8alsvC3Ckt7rckYuy9xgV5iWFeP_L1LJCtwyyfcIFVUf3Xrk74ctWuUrXpqHS7Y0UY05NiE_TF-q9u7RiMGi4OpCpxcDfsaN3DEwLiBdVChM75nSOguK9GIsA1TVn62K48kQDgfh1rYhsmFbaAKyN350LV3aIjSMkznjfd1eqMmLWWYj0pjQdot-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«روزنامه وال‌استریت ژورنال دیروز گزارش داد که ایران برای دور زدن تحریم‌ها و محاصره آمریکا، از سازوکاری موسوم به انتقال کشتی‌به‌کشتی(Ship-to-Ship) استفاده می‌کند؛ به این صورت که کشتی‌های تحریم‌شده حامل نفت ایران، پیش از ارسال محموله به چین، بار خود را در دریا به کشتی دیگری منتقل می‌کنند.»
@withyashar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/12783" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12782">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSUVulSD1N_KXHMmbnY7cf5hvDZKEr71ZNo8HrG6fJY_Xgxga0rZ3_vdoECbgYJyY4Zg8Do0uXgHOj1SQFU06cZMmckWrNHQl3zoryGirszxuEAbScXotm1tFOq9uJxPzqRbiPJ6qxWupQwIl7K8eTdNH26CTr9iov2gTEaxS3qmhBtHQF_hYBZSUc_J2W_Xm9va2ocYwZEF4nZR6nWJB0yV5SN1PsV2H8tTiAAVY4wgr6gacX0FHd8opf0b3ZA6j_QJoCUmAFDglFXPH1hl1sLVsQcJtsPlQ4c150boSIWoLdTyLq03XhUKLPz1AoYnrPVQYX7wqIH_F-bLMbNWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دقایقی پیش مجدداً دستور تخلیه فوری کل جنوب لبنان را صادر کرد!
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/12782" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12781">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مقام‌های آمریکایی گفتند جمهوری اسلامی چهار پهپاد انتحاری را به سمت کشتی‌های آمریکایی و تجاری شلیک کرد، اما جنگنده‌های آمریکا آن‌ها را سرنگون کردند. به گفته این مقام‌ها، جنگنده‌های اف-۱۸ آمریکا همچنین پیش از پرواز پنجمین پهپاد، واحد کنترل زمینی جمهوری اسلامی را در بندرعباس منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/12781" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12780">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/12780" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12779">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPRRZKjZKCUFT13NEpn3Mdc5Ld3fuFZfw2DSaPij3mqIRMrovefuNn7eL34E8s-9q49uSyzTokALdzR6Y2r0myXNiobaHWUT7gypElBdAxnQSOG5KbODXyaVvq4jkHSJxBFJJRTl5cjLjoJteJqRdjLvW72px2yO4CBdjWV302yH_qNXNIExMndq9DVvA-NAqxtbopIePaJ-RZH9llJS8obBksAd7mxd6Y2S0W0UV-LpSeq8pqUjk5UIetRoZZ4UMNMgrr6qbrU6rawG-EA6uncYBlVZu6gLPWVE-TiZ3AP2Oe11rCTLr52QOuHdxZV8PfHR812DqKKY4FqBwrvMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم ترافیک اینترنت بین‌الملل، تا ساعت ۷ و نیم صبح امروز به ۵۳ درصد حجم پیش از دی‌ماه ۱۴۰۴ رسیده است
@withyashar
حرفم که گفتم اینترنت فقط با رفتن اینا به حالت قبل بر‌میگرده هنوز پا برجاست !</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/12779" target="_blank">📅 11:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12778">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12778" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12777">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBHz0XHQLdEmnsmJVFNWZ4dOF4TC3nSTzJm_94tERffksZjoe45NfKCJBc6gnZnjEjiyxRXg6d76KqTRdrJBmhzKrKm3XlSRXHSQEjBLI_-kQA9dTHD0BJFphpNhHAeVPsVNMQDs3LQp8ckYhZECwn3zZA6GELcJGAFog1iB6iXjzQbkbhRnpCF4lbRAVdg_3FDq6fidahdeKGozoKpiZ9bIkraGTHAanlMPA3Wqq_MAEBQyX3fzW1vQb_TPJH3zsjMVmHvNtkhSY3UAGjJD36LaEqHLLQJGhXAhF-0PXcBPO_BBaP-2WOohNxClwsf9kOZ3Qm7q_xsr7gnz9yDeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
👏
👏</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/12777" target="_blank">📅 11:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12776">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBeobkUdXKBRghSgsKo84ucGhC9ulTOveRu_fQxFLmtWm0FYkhEicy3V5tfWdGkeotYWmGq6jnvkVUnk7vxHicvKr8EMVykCvpcJw7Tu8buHFhJFVwt5eClDwAfmJwHAnlA-UhS6T4L5XraWvN2RYkxPLenfJ9_B7NO0MD11B2diLChcYjCTssXxPmqB5CgirRNIgtdeqy8r6SykDpl4jyKABSemcBX4zkcsQeOV8yjNtBjtM8JUWTXfYoAuJA-TIDVniHqbYzva_7UFUJ77ukNfS_z5jY_4FliZIjrcNZ2bKGKZWmxyNprQtjbAlJf0pr19wEgUBP1K0GgiJlgOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/12776" target="_blank">📅 10:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12775">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3p4RtDPzqLje_q8QO-Qzhdy31DXgvex7crDVkuMxXYaTpNJQh2-u2J7le4-D13sS33-Hlrp5ezGvE_yxxY4MpBjhEPXLpwaCXDBCOFRLaCBNbiKzN4Ynvrhz46ujWQ5TsHQY6aDp76af44HPEuMSKKTPiEG93Jmc7OiYa6EaMfYRPS55AUkeyMhLjp_kMRd9pz4xv3t7t2F2-K4Dvw7nl9BidEl4_XfZXG2aB3zAv_S0HpiVkLXK4fergcuQ6orxaP34DUH0O-VKXgvXOIpIp1VzpnsoLgOF1oI0mPpkcQAsMaj6D5-PryNV5TOYx1C6gWlmC-CSpk4r4s5qDp3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل، عزالدین البیک، فرمانده تیپ شمال غزه را به هااکت رساند
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/12775" target="_blank">📅 10:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12774">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRqevLCi-seJAXXdBDl4zE0YrPPvKa8UNiPXmo_SCaJQ3uCIPxLg9y9s7acVbNvSobK8EHo-aVLSNRoEQoCzCPtRYi051dFdj2WRIT2lelMO_O6UIEOB4eGvszTpiCHWDyKpPJ3D5qdNVRjcqlpsK85IGLxeqy4Z2mOIvTMe0S54CKbLkR8bHCfVipbSuLh-qHMKauPEHD35xLMXhlZkQ9VWgRG9Q7rV4IlLgK-Y5G2IBTUm-2R3kj5A9VRPVDCPiFm3LYenff1upe2sXNsuLDrrYwfADFON7z3eqnWsR1RvN-5cRQmNI3hCO0dfHoz7MUrHoax08qMIuhOwERC_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
یک گاومیش آلبینو نادر در بنگلادش که به خاطر دسته موی بلوندش «دونالد ترامپ» لقب گرفته بود، پس از اینکه در فضای مجازی دیده شد، از قربانی شدن در عید قربان نجات یافت.
این گاومیش ۷۰۰ کیلوگرمی قبلاً فروخته شده بود، اما دولت به دلیل نگرانی‌های امنیتی و تجمع جمعیت برای دیدن آن، وارد عمل شد.
مقامات پول خریدار را بازگرداندند و حیوان را به باغ‌وحش داکا منتقل کردند.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/12774" target="_blank">📅 10:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12773">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس»  را به فهرست تحریم‌های خود اضافه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/12773" target="_blank">📅 10:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12772">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=VENfzIgsMpAYfE11TfW5AfgRFyLGGuSySzvE_0ENpvXd_rAyCeOhgEZXTZF1MxD2lz53SXM_o7jKQWy44tpbTc5d6H4z7hrbjTxFzrUuFTZ-V3j0DTwH0cdggYXqMWBbzXdgnUaw_LxkB7bLXdq2onlhLatVEJroixnO23bXwB4aqyYrIw2OgQvZKmBX2Ql6bjb8A7v3zC0q8k5l2YhgKSaTSdnEFBHsQbExAPfgJOHkxNm1Y54ykA0EoQ0DOyizSrscQ5AqPmSvluBfTznqySttKFmyLvz5VXsdkC18D07aM9kX-NypdbjUx7NTKnRZ3yDDMy-tLVhycG3OAEH-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=VENfzIgsMpAYfE11TfW5AfgRFyLGGuSySzvE_0ENpvXd_rAyCeOhgEZXTZF1MxD2lz53SXM_o7jKQWy44tpbTc5d6H4z7hrbjTxFzrUuFTZ-V3j0DTwH0cdggYXqMWBbzXdgnUaw_LxkB7bLXdq2onlhLatVEJroixnO23bXwB4aqyYrIw2OgQvZKmBX2Ql6bjb8A7v3zC0q8k5l2YhgKSaTSdnEFBHsQbExAPfgJOHkxNm1Y54ykA0EoQ0DOyizSrscQ5AqPmSvluBfTznqySttKFmyLvz5VXsdkC18D07aM9kX-NypdbjUx7NTKnRZ3yDDMy-tLVhycG3OAEH-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
رد موشک های ۳پا در امیدیه خوزستان که به سمت کویت میرفت
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12772" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12771">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اکسیوس: ایران چهارتا پهپاد انتحاری  به سمت یک ناو نیروی دریایی آمریکا و یک کشتی تجاری پرتاب کرد  نیروهای آمریکایی پهپادها رو رهگیری کردن و همچنین یک واحد پرتاب پهپاد ایرانی دیگه رو روی زمین قبل از اینکه بتوانه شلیک کنه، هدف قرار دادن
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/12771" target="_blank">📅 09:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12770">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فاکس نیوز: آمریکا یه ایستگاه کنترل زمینی ایران رو تو بندرعباس زده؛ همون جایی که قرار بوده یه پهپاد تهاجمی ازش بلند شه.
به گفتهٔ مقام‌های آمریکایی، چهار تا پهپاد انتحاری دیگه هم که تو تنگه هرمز تهدید محسوب می‌شدن، زده شدن.
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/12770" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۳پا یک پایگاه هوایی آمریکایی را هدف قرار داد
روابط عمومی ۳پا طی اطلاعیه‌ای اعلام کرد:
به دنبال تعرض سحرگاه امروز آمریکا به نقطه‌ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/12769" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مقام آمریکایی به شبکه CBS نیوز گفت : آتش‌بس با ایران پس از حملات امشب همچنان در حال اجرا در نظر گرفته می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/12768" target="_blank">📅 03:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:   ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد @withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/12767" target="_blank">📅 03:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12766" target="_blank">📅 03:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/12765" target="_blank">📅 03:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12764">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه. @withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/12764" target="_blank">📅 03:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/12763" target="_blank">📅 03:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12762">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12762" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12761">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8116492af1.mp4?token=nsT8ZUP7c-sO-Yi6ztsSWN4wMQvpDYoyv3Qb76GXvJDDghxff1QybMkSHJlBVaEoPrKIZzEsw7cbUM0ivHkf7s8sXaR1hUpI-KozZCc61ra5rP7Y3gY6YCoe3xalBobbYIG-NZQNjhKa4vP76SIfcvA-SCDA6x2Ptx01orj0P00xB_G77IoPa9NfzMCdp4DyfuwmYcAmpCK-ujTXsP8ivT192EbIIIr6DT3spr9tJUpz1YL3RAQ4uwjSWWUk6UkXJRY38XbZ4XsAFDTWvKTHvsxut3u-D9cvGczqJGRm3N8Tg_ErRqXtrD9wJ4t5I071yeJ2F3hOd-RWZgQO-QNXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8116492af1.mp4?token=nsT8ZUP7c-sO-Yi6ztsSWN4wMQvpDYoyv3Qb76GXvJDDghxff1QybMkSHJlBVaEoPrKIZzEsw7cbUM0ivHkf7s8sXaR1hUpI-KozZCc61ra5rP7Y3gY6YCoe3xalBobbYIG-NZQNjhKa4vP76SIfcvA-SCDA6x2Ptx01orj0P00xB_G77IoPa9NfzMCdp4DyfuwmYcAmpCK-ujTXsP8ivT192EbIIIr6DT3spr9tJUpz1YL3RAQ4uwjSWWUk6UkXJRY38XbZ4XsAFDTWvKTHvsxut3u-D9cvGczqJGRm3N8Tg_ErRqXtrD9wJ4t5I071yeJ2F3hOd-RWZgQO-QNXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی همکنون در آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12761" target="_blank">📅 02:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12760">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwN5XeWz8r6163r-efyu60d2v8lJweiQmLMkH3D_txD8Mo3zDcAA-44lF0atyB_TUBomlJXu2sQP-sCGwszZqDnenz2WInXoAjoZx9Sb8nlnWSq4_YUfxfUeCPfiMCwNLmWhYyXb8cGu44I_tDDInonWReUREyLcxZlGtdGMpyE6C15ZR5Fi5pcnWnFYR2cmT0wTSRodE8LBebIf9o9KV4dlnbagYi4fYPMjUExYnig31OpWe5T8H94bE4R6MjxSxFnYn4BW_Us82mc9tr49LzzM84YGXJFBdK7SqhvOR1c70lLGin35kpmTVKzRs6cNf4LIp42UfasgLiUicao13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12760" target="_blank">📅 02:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12759">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/12759" target="_blank">📅 02:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/12758" target="_blank">📅 02:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/12757" target="_blank">📅 02:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12756">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12756" target="_blank">📅 02:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12755">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یا موسی</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/12755" target="_blank">📅 02:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12754">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پدافند اصفهان فعال شد !
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/12754" target="_blank">📅 02:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فارس : شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقه هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/12753" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبر گزاری فارس‌ انفجار رو تایید کرد !!!
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/12752" target="_blank">📅 02:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12751">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تایید نشده ۳ نفر‌گفتن ماشین این کاربر‌ با آدرس گفته :
بولوار‌خلیج فارس یه ماشین رو با پهپاد زدنن رفت رو هوا و بعد پدافند با تاخییر شروع کرد فعالیت
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/12751" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12750">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">داداش من بندرم ۳ تا انفجار ۳۰ مین پیش بود و تا ۱۰ مین پیشم صدای پدافند می اومد میگن گویا یه ماشینو زدن و ترور بوده
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/12750" target="_blank">📅 02:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12749">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/12749" target="_blank">📅 01:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12748">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چیزی ‌نیست بی بی اومده یه قلیه ماهی ‌بزنه بره
🐟
شلوغش نکنید</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/12748" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12747">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام همین الان پدافند بندر عباس درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/12747" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12746">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارشها شما اکثرن به پایگاه هوایی/فرودگاه اشاره میکنه</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/12746" target="_blank">📅 01:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12745">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صدای سه انفجار در بندرعباس دوباره
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/12745" target="_blank">📅 01:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12744">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارشهای ززززیاد از انفجار در بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12744" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کره شمالی تشکیل ائتلاف چهارگانه شامل آمریکا، استرالیا، هند و ژاپن را محکوم کرد. پیونگ یانگ همچنین تاکید کرد که هرگز از برنامه هسته‌ای خود چشم‌پوشی نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/12743" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12742">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=DouNo95Cg_wJESW8TAq4sUrYQKyiMqQVYpr0_FMGp-oDkN4TqenfEBVEM9rvJRC7kLQO8G43Y44aE6OmJUTXxjgA8u7zYWkSW_kyu9EJaCQ2CW2rJ6QSZXIODbO7H0vR8Am-Ro3sVx6mrtgNKWC2bHkdFUudyhSd3yerN-cO_my2nDIhLMMYEzsPLPoP1IRv8CQkShWEoYXR1oJZp-vy3U-_aCxG0Iwe0zAW_Zqn01mfEDI7g8_WbFAXyRlq8eyM0uqUyC3pCAgSGgAG79nkT80EpB1RJ4xX0Ai-gmqFyFoMgKtBSawR5QPMaSxj9vYYatRY89RUBwk5C_qSyCzp1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=DouNo95Cg_wJESW8TAq4sUrYQKyiMqQVYpr0_FMGp-oDkN4TqenfEBVEM9rvJRC7kLQO8G43Y44aE6OmJUTXxjgA8u7zYWkSW_kyu9EJaCQ2CW2rJ6QSZXIODbO7H0vR8Am-Ro3sVx6mrtgNKWC2bHkdFUudyhSd3yerN-cO_my2nDIhLMMYEzsPLPoP1IRv8CQkShWEoYXR1oJZp-vy3U-_aCxG0Iwe0zAW_Zqn01mfEDI7g8_WbFAXyRlq8eyM0uqUyC3pCAgSGgAG79nkT80EpB1RJ4xX0Ai-gmqFyFoMgKtBSawR5QPMaSxj9vYYatRY89RUBwk5C_qSyCzp1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حتما با پوشک بسته نگاه کنید
⚠️
میگن سیلوستر استالونه بعد از دیدن این ویدیو فروش آنلاین تمام فیلمهای رامبو رو متوقف کرد.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/12742" target="_blank">📅 00:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12741">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علیرضا فیروزجا با پرچم فرانسه نفر اول شطرنج جهانو شکست داد
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/12741" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/12740" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12739">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عضو تیم رسانه‌ای هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود!
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12739" target="_blank">📅 23:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12738">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یاشار جان  احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/12738" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12737">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromE R F A N</strong></div>
<div class="tg-text">یاشار جان
احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/12737" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم! و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/12736" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKnow</strong></div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم!
و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/12735" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شاهزاده رضا پهلوی جمعه پیش در نشستی با شماری از فعالان رسانه ای  که ویدیو آن الان پخش شده گفت :  تیشرت های سیاه یا ساواک به خصوص و هر چیزی غیر از تم اصلی شیر و خورشید نپوشید این جریان در کمترین حالت ایجاد جنجال میکند و انحرافی است  من واقعاً درک نمی‌کنم این موضوع از کجا آب میخورد و این مسئله نگران‌کننده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/12734" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/12733" target="_blank">📅 23:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/12732" target="_blank">📅 23:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2ksulAz5C5DgXKE4YxLdhK5BaA0LtmqA_aA4b5L6dtAK9yQNks11zZvYFU9baBzSuPbSZr4kWMxsT6UC87VyglrYa5H5l2USl45bYelhhd0SbtflxseqYXdg2HAo72GWJDEq0eiyO0hgtDmAIWyKy65Tn6L5aH9QfZgLBaM-8qTpa2mROiQYEtMNs8B0vkjLCyAsJOoH2dFfLxy8kLPAQHvKMFmUZ5q1ej3Var_S4sBDTyIqgE1Hip8yP3cPUl2HYfcLFZccWz6cM-iQgNnSja181kwYl-diNf8cwh0eg_eBy56ukga3mX2MAzYRmO2OmbPArxEcg18b7jcRB4Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : داداش این ایده ایی که دادی رو یه مقدارخلاقیت دادم بهش که بفهمن دقیقا چطورمیشه رفت بدون پرچم
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/12731" target="_blank">📅 23:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/12730" target="_blank">📅 23:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هم اکنون گزارش ها از دو ترور بزرگ در شمال غزه.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/12729" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : کاری‌ نداره اگه همه با هم متحد باشن میتونن ، فقط با پوشیدن لباس های سبز سفید ، قرمز و زرد یه ابر پرچم قول آسای انسانی‌ پیکسلی درست کنند
🧠
😍
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/12728" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/12727" target="_blank">📅 22:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12726" target="_blank">📅 22:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58450dfb0.mp4?token=mJElCDyEkU953tqp7U1jMzw5YEum-q37qDSxDbtfu-q0DVLTgpIes41Csf8TIJSbx04NSotShiPejoWA1gUdriye5NJ14c6P7YAWhzQLfUn8dktPTxKbPBoC6hByfm0_vyCGZM2XbwZtMhc_nKWvBUMB8F9oWEtzDC-d3YS5E1EGw9sKOx_Ik4G93gptAhSFY7NidLIcrNhxuPSc65duBwx79MAVC1TXML68jtlQCBEUM8STkXuuvss3CywCQJ4Co610P2Ccx_Dc2tacpLU_GEsC67pRkwMjwojhN17MzO7z02JjgaJu_jRiDoV8tgUcfb_oVmpKs7zoiKIkaZosaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58450dfb0.mp4?token=mJElCDyEkU953tqp7U1jMzw5YEum-q37qDSxDbtfu-q0DVLTgpIes41Csf8TIJSbx04NSotShiPejoWA1gUdriye5NJ14c6P7YAWhzQLfUn8dktPTxKbPBoC6hByfm0_vyCGZM2XbwZtMhc_nKWvBUMB8F9oWEtzDC-d3YS5E1EGw9sKOx_Ik4G93gptAhSFY7NidLIcrNhxuPSc65duBwx79MAVC1TXML68jtlQCBEUM8STkXuuvss3CywCQJ4Co610P2Ccx_Dc2tacpLU_GEsC67pRkwMjwojhN17MzO7z02JjgaJu_jRiDoV8tgUcfb_oVmpKs7zoiKIkaZosaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما شرط جدید ایران برای توافق با آمریکا را اعلام کرد: پرداخت غرامت ۳۰۰ میلیارد دلاری از آمریکا به ایران
!
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/12725" target="_blank">📅 22:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در اسرائیل پرونده‌ای جنجالی به نام «پرونده بیلد» فاش شده است. طبق این گزارش‌ها، یک سند محرمانه منتسب به حماس عمداً به رسانه‌ها درز داده شد تا خشم افکار عمومی از دولت بنیامین ناتانیاهو کمتر شود.
گفته می‌شود «آری روزنفلد» و پدرزنش یک مسیر غیرقانونی برای انتقال اسناد محرمانه از سازمان اطلاعات نظامی اسرائیل به دفتر نتانیاهو ایجاد کرده بودند. سپس تلاش کردند پیام‌ها و روایت‌های سیاسی خاصی را وارد سخنرانی‌های نخست‌وزیر ناتانیاهو کنند تا بر افکار عمومی از او تأثیر مثبت بگذارند.
این پرونده «بیلد» نام گرفته چون بخشی از اسناد ابتدا به روزنامه آلمانی
Bild
رسیده بود. مخالفان دولت می‌گویند از اطلاعات امنیتی برای اهداف سیاسی استفاده شده، اما حامیان نتانیاهو این اتهامات را اغراق‌آمیز و سیاسی می‌دانند.
@withyashar
اسرائیلی ها هم دنیایی دارن خوب‌ مردی بی بی برا خودتون اسن کارو کرده ! ولی مخالفاش داستان کردن !</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/12724" target="_blank">📅 21:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12723" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سلام یاشار جان خسته نباشی، ممنونم بابت زحمات
میگم یه سوال تو خبر دارین که میگن جلسه کابینه کمپ دیوید یه تله بوده که کی اطلاعات رو لو می‌داده و فهمیدن که جی دی ونس بوده؟!</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/12722" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش اتاق جنگ اعلام حضور کنید. مانور امشب شروع شد. این کامنت زیر پست بی بی را لایک کنید، ریپلای کنید و اگر میتوانید اد تو استوری هم بکنید و به دوستان خود هم بگویید این کار را انجام دهند. آماده میشیم برای مانور نهایی در دوشنبه. توجه کنید فقط همین کامنت را لایک کنید، حتی پست را هم لایک نکنید که کاملا دیده بشه
❤️‍🩹
🙌🏾
https://www.instagram.com/p/DY2dIhsM-VK/?igsh=MXFhaGU4NzliZzVmaw==
ترجمه:
تبریک می‌گویم بی بی جون، فرزند راستین کوروش کبیر.
دیگر زمان آن رسیده که مقدمات حمله به ایران آغاز شود.
مردم ایران در نهایت ناامیدی فرو رفته‌اند.
لطفاً این لحظهٔ تاریخ‌ساز را هرچه زودتر رقم بزنید.
هر روز در ایران، روح جوانان ما را از جسمشان جدا می‌کنند.
تمام چشم امید ما به شما دوخته شده</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/12721" target="_blank">📅 21:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/12720" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12719">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/12719" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSG</strong></div>
<div class="tg-text">ماجرا ری اکشن پر قرمز چیه دیگه ؟؟همه دارن میزنن
😂</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/12718" target="_blank">📅 21:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be7-rB2GtKrSYedIwa5M6fqJ0GuqxfpexJwIssKGWxm5RGIt5xLILp3hSNCBOVm83mGPmPcZFbj8VEt1D105UpJ6sIs5apvOSWSTDPin0lY6K5hiKB2LoMXuLFYeR3pPS7Yi4UUOqi10PDFXcol9-tIObwDREhZPjVi-ur5mDUzFaQDwCCsv79mzO58uSHqELycBef9jFR4_5IVR0K2FqHbROUoTvKbRzkz4sRHU1zLEqyLMcRAA_pY28FDaTygQO1nXp0nv1Wbdbvpj-qQhc-BoOrKFOiU_YKZqHdGXdHocxlst3W5FxYKOqS04Z-fcEFtwAL1-e1FcEnmn8euvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی رد لغو تحریم‌های ایران از سوی دونالد ترامپ، بازار سهام ایالات متحده در عرض تنها ۲۰ دقیقه، ۲۳۰ میلیارد دلار از ارزش خود را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/12717" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12716">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/12716" target="_blank">📅 21:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12715">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اتاق جنگ با یاشار : هیچوقت انقدر مشتاق نبودم حجاج هر چه سریعتر سلامت برگردن خونه هاشون
😅</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12715" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12714">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12714" target="_blank">📅 20:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12713">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/12713" target="_blank">📅 20:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12712">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: دارن کم‌کم شروع می‌کنن چیزهایی رو که باید بهمون بدن، تحویل بدن. اگه این کار رو بکنن، خیلی خوبه.
اگه نکنن، هگست کارشون رو تموم می‌کنه.
ما درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول صحبت نمی‌کنیم.
وقتی اونا درست رفتار کنن و کار درستو بکنن بهشون جازه می‌دیم به پولشون برسن
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12712" target="_blank">📅 20:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12711">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرنگار: آیا با این موضوع راحت خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ: نه(زیر دلم درد میگیره)
@withyashar
🤣</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12711" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12710">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ :
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/12710" target="_blank">📅 20:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12709">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/12709" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12708">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhesam | امیرحسام</strong></div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/12708" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیت هگست درباره ایران:
آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند.
آنها آمدند و التماس کردند تا صحبت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/12707" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMXtl4mfC06pC2KaKvuMEY0aI_fH8E7pJTh4FjnWlonJqtlAdBAW6ROPi-UrR-I6o1mjrqcah-Ct4BpAsk7gIKju9plSaP-J9UpWKfHbz74eLRwC3yyViw7OZ_IrGCce-YQ5mGOL_3_ptDvB3FKdysdr-lP8n54reH9VWvD-pVQyfY0DEK7TwcqmMmmESZbhunCGpJrIWXrh_GNnlXAOIu-QLbwh9YUot-Du0MdcU6TohnzlRjzysFHxp7tT_tiAAbq2U6c-6rrVMMaquMLX09P_E_cvjRAUkv2ZfnjH9wnk4KV44tz0Z971ZF5aW-G8vrBwas4wdfvTLO3bxbcdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️رئیس روس اتم می‌گوید روسیه تصمیم  گرفته است بازگشت کارکنان خود به نیروگاه هسته‌ای بوشهر در ایران را به تعویق بیندازد!
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/12706" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12705">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مارکو روبیو :اگر ایران توافق قابل قبولی مارو امضا نکند جنگ را شروع خواهیم کرد این‌خواسته ترامپ است
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/12705" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من به خاطر جهان جلوی آن را می‌گیرم.
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12704" target="_blank">📅 20:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12703">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره مذاکرات ایران:
آقای رئیس‌جمهور، اگر این کار جواب نداد، گزینه‌های دیگری در اختیار دارید.
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/12703" target="_blank">📅 20:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12702">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">روبیو : ما با جمهوری اسلامی پیشرفت‌هایی داشتیم اما در روزهای آینده میزان اون رو خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12702" target="_blank">📅 20:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12701">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/12701" target="_blank">📅 19:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12700">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=KopHD7BllfkwznjZLEvWHmalKqfMiOwyacSNG-PwfMvvthN2zu9P3G5qEGl3CTqgHnuqFyxtAqKnM3mcMqTwFobRC-UTcMT3mTwXq07nSjF7Zrkhzt_wnq_5PjmZxvpXof5wwPt-gKIdL_oKeOpoRILYOb6aIYx-TlzxqBirQJZ5-FGoiqOyfK9u-G423JXkJDl1Hbo2KeAaugGTASbLManCciTnwS34DWlCR5hlToZSse1gNvpcxDUuiAtAt7EOwkpGWB2Yt6pxZtb54I5bAAUjptwMQTRgSa3ceD5y2Mu3j4IAalDlwpdyb6NbnA41chxDJ-ZTEeE-eZ94DNtRXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=KopHD7BllfkwznjZLEvWHmalKqfMiOwyacSNG-PwfMvvthN2zu9P3G5qEGl3CTqgHnuqFyxtAqKnM3mcMqTwFobRC-UTcMT3mTwXq07nSjF7Zrkhzt_wnq_5PjmZxvpXof5wwPt-gKIdL_oKeOpoRILYOb6aIYx-TlzxqBirQJZ5-FGoiqOyfK9u-G423JXkJDl1Hbo2KeAaugGTASbLManCciTnwS34DWlCR5hlToZSse1gNvpcxDUuiAtAt7EOwkpGWB2Yt6pxZtb54I5bAAUjptwMQTRgSa3ceD5y2Mu3j4IAalDlwpdyb6NbnA41chxDJ-ZTEeE-eZ94DNtRXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران :
ایران خیلی دنبال توافقه. هنوز به نتیجه نرسیدیم و راضی نیستیم، ولی یا توافق میشه یا مجبور میشیم کار رو تموم کنیم.
اونا دارن از روی استیصال مذاکره می‌کنن.
اونا دیگه نیروی دریایی و هوایی ندارن و رهبرانشونم هم رفتن.
ایران فکر می‌کرد میتونه صبر کنه تا منو خسته کنه
به انتخابات میان دوره اهمیتی نمیدهم اونا گزینه دیگه ایی جز توافق ندارن
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/12700" target="_blank">📅 19:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینترنشنال باز خل شده ؟ چرا ترامپ رو انقدر میکوبه ؟!</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/12699" target="_blank">📅 19:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم @withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/12698" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGQ3_mL-EvbxBVFVcaPewRmQazQb-ds8a0jYtnEqd2R5fvGPh2Nj5gVJ7ulBJFrt0JoPstc1itcEXdq-L7YmOt-h9RxMS4uk2d6YKDEJjFh_3KyB3yigWGTwy7fZYzZO74FnUHIuHn5k79VHsOtB344LAHi1knn7GJZBnJPhPAVZQdyv-2N5FCF92kPjK6BkE-AnssE1FTDnLW6p1Z73vhQEBl_UxTuE_QPg7FuvodfiWCpPcJ9zRZE6RdTEgWC2C3HLE45C6Jr9Gy4W-j6K-AjAD1ySljR-cUzlqOOPUC934NMgmbdYOQVqU210gu1ptGNjkk-pSSleTnHfkI1rOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12697" target="_blank">📅 19:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3xw_2dcwouRrrRVMEcNrNuLisZ4p3S2FdxhMP6O3S5_xKxsSPuRuK50JCdeKeNRN_xJ1Og-_az2aAoU2CGWqtZNcA2bLsoqE1CSuaF6hSxRA6Q_rU2dCAvmmw04cCz4w00wDOZBs-Ok0oM2uxzawisPiSiIW4NdxpBWSnjOFR92DLppZbgS9a6FmYveIsMKEuUYZm23bslsPQ1wx-PnDhQZtNKU3q8WpCa0HolLa2VW7e7yqoIgxNHSRnB4C4femEeLyDEOmpkWcg3yuzbmexsNHghZkfu3cssPjGkEYkCtpx_1ARAhVAmTgPIEpwDnlt2u3V8pTnOsXm7QYbKq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها می‌باشد.
میزان اختلالات در شبکه از دیروز بسیار بیشتر شده است، بسیاری از سرویس‌های گوگل و کلودفلر بسته شده اند و حتی قابلیت استفاده از گوگل پلی و اپ استور نیز وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12696" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">یاشار جان من دندونپزشکم، دو سال سرباز بودم، صبح‌ها تو کلینیک ارتش یه شهرستان دورافتاده کار می‌کردم، بعدظهر هم تا شب تو کلینیک خیریه کار می‌کردم، از نظر مالی هیچ سودی برام نداشت فقط دلم می‌خواست دوران سربازی یه کار مفیدی هم برا اقشار ضعیف انجام بدم واقعاً از دلو جون مایه میذاشتم
اما اون دو سال، از آدمای قدرنشناس  و پر توقع رفتارای زیادی دیدم که باعث شد بفهمم خیلی از هم‌وطنا وقتی برا خدمتت هزینه‌ای پرداخت نمی‌کنن قدر خودت و کارتو نمی‌دونن انگار وظیفت بوده بشون خدمت کنی
همین تجربه‌ باعث شد دیگه سمت خیریه نرم
خیلی از مردم ما واقعا قدرنشناسن
وقت و انرژیتو بدون سود و فقط از روی عشق به کشورت صرف کاری می‌کنی بعد یه عده‌ پیدا میشن که  برن رو مخت و پشیمونت کنن</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/12695" target="_blank">📅 19:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwNXpzUxsOFgVmYEuqYB5qZiDJ1pL1jd4t0JZpZGr-Ki5HpwLzMTAf8ZpgDbjz0ErG4QUv9YIEuGq2hkaAfnJSvHcHRFSLUMk-I39Q5kI08f2dOjP7a3pDUhvVDIVctiNkF00Rw0wkzp1sou-8fpb70k0bk-_mZE6cBrvQkTNAfweDNJSQ42I7Pzos1zDIUa6dejFmTHujJMoNlUGztQAmVnlj0P-LBXf4MnoiHQzOCSZh6pVEvqRNaCLSotE8lyjt45cRz1hCnaZpzXBNdefHGh8FmYF3H2sfooT2ok21Z4uEgff5UDC_fbLMJ6Rr0ZW27ESv-V8KUntl4YnXO5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به PBS گفت که ایران در ازای کنار گذاشتن اورانیوم بسیار غنی‌ شده خود، از تحریم‌ها معاف نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/12694" target="_blank">📅 19:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUx8Yi_gzrXQAYeThya9jGNMLbJn4PZg809360V1ciaQxhHY9MtPk2su_uuJgxtt3MV5IU3XnXJhY-JUQHwA7kEmoc8SGMwP4K9f4IXHwsmu1EE7Mil4L3ng1M1z9OeLBuWdlXOaAGnBYl7JJE4vdPOflWUmqmlKmgiQLDONOlg5c9ep3CbJPQ4a-ir8bbYeXiN79DIPcf42dv6vVGVpZFJDVwUoukWl2auScXSSE8dqw7FdSauH91FLOb9ofd9yd7f3uP2BtRtoETuEVz979T_KfCcEMxVU1ssF-q-JudumxoJ70yEmkxKs9wcqZZ7RY4INAdTlzeOtljFZYX0ZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار برج چیتگر پامچال چهار از طبقه ۸ به بالا آتیش گرفته
این دقیقاً روبروی همون برجیه که تو جنگ دوازده روزه طبقه ۱۵ رو زدن بعد گفتن نشت گاز
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/12693" target="_blank">📅 19:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری فارس: به عقیده ما احتمال دارد ترامپ در ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است
@withyashar
یاشار : عقایدتون رو …
🤣</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/12692" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_Dpgfa9zpbSpoaj_ebGxVGA3zSZPJpo7lI9nQJp5MVtWj3eHcsov5iHQxXFjZkdNpXTEOKEvzj_ZlvHBui15OQVkZMIQ0aH_OlbszAfoYf0s-uIA4qnAuGDc5b9OpiGnNPm4FG4ODNSQZIiCPpw9mPbAHB9b_qhpK8jOLRylT9n7uAiHUjjqhmQH5VLBzWSJjjAMLhS58m1JmPrBSdL8ybHAWyP-v8yStZnjYauHycfodipjUTAhYBM8MPKnDjO9Drg-DI0U5WfRx7j6gFeQVIAGep6nZil-nsPgGgrak0ulzhS7eFfgU2Ar45bFNcFCkRbQtdVFeZbQsWpUMEjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
عوامل موساد باعث بازگشایی اینترنت شدن.
@withyashar
یاشار : شاید باورتون نشه ولی درست میگه اینبار
🤣</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/12691" target="_blank">📅 18:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntKwaXPStrMp-l6WrvDxSbv_RFKbmr1vGpGCfHt0Aa964eXpaGapQd1igPgoaBtnqeBvWsbR2sDhoBSapjqHaDnPKOX4siMxE1PVvvm0OeHhlbGeI7zyPT9C4UDP1JVCTRwab926VCa9NXsgeZ4ry6X_vaNnPFhuo5n3IU-Cbau0QAw907CQbYkjv8rZhvU93rtKx2yYaAB1gJSJhq_DSb8t8G_ULjBiJ1pwwduEkQeY3PXy26a9Lc-e8vokn69H6cOPowyKt1SllwS6bnBQp9eeNfsTsD9uOSyasL1TRyYEtLMfx2jwcqhr8xZW-5SsIRwciCFz3eCna_mOkRqywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از پایگاه هوایی رامشتاین در آلمان، ده‌ها فروند هواپیمای ترابری C-17A و C-5M نیروی هوایی ایالات متحده، چندین فروند هواپیمای ترابری C-130 و حداقل 10 فروند تانکر KC-135R را نشان می‌دهد که در آنجا مستقر شده‌اند.
در اتاق جنگ گفتم که رامشتاین مهم‌ترین پایگاه ایالات متحده در اروپا برای جنگ ایران است و به عنوان یک قطب لجستیکی کلیدی عمل می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/12690" target="_blank">📅 18:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/12689" target="_blank">📅 18:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کاخ سفید گزارش‌های مربوط به تفاهم‌نامه ایران را کاملاً ساختگی خواند.
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/12688" target="_blank">📅 18:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پست جدید
یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12687" target="_blank">📅 18:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارتش اسرائیل در اقدامی فوری دستور تخلیه کامل شهر بندری صور، بزرگ ترین شهر جنوب لبنان به همراه تمام روستاهای اطراففش رو صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/12686" target="_blank">📅 17:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زلنسکی در پیامی به ترامپ:
اوکراین برای رهگیری موشک‌های بالستیک روسیه تقریباً به طور انحصاری به ایالات متحده متکی است.
سرعت فعلی تحویل موشک‌ها به اوکراین دیگر با تحولات هماهنگ نیست.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/12685" target="_blank">📅 17:51 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
