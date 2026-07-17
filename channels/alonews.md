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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-135166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/alonews/135166" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/135165" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روسیه: تفاهمنامه میان آمریکا و ایران در آستانه فروپاشی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/135164" target="_blank">📅 23:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_lc5NXVHOEUI7SqehWFOpvScaKc4CX7KwZHnogdjxD_in2LEyR1hJm3Sp_ny3fz99wlIvskolDaME6Yvbpl8qrM4Orx_AL0GONQeeCUdwmyZvLW_nX54VTunolesQxoYELJ-bOixZibsIMA6sQMU08TE3wkUJZoqzjLGfXvPhTr7x-aSRmagnBeX1QbdmS38auLegweAtv0tUgvTOwbk_ZnYGzxG9kqwGsaQWYkPzozEXORpLVAoz1LVQOKyQuz_0dvP9oW_Nr6Yrob_FJloh8Ai95kL85F7myK-oEMd10bLixGWGB4OzfP74qPFuTdL4Yvz_vA2nBXF0LwOSP-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ سنت‌کام:
دور جدید حملات از الان شروع شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/135163" target="_blank">📅 23:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTiVlK4mgdheuGdouo9FcWm_7yz5Gn1gK3exknLVu6ORtM-TmxxAkJ9W6QFjf6Ohpp4sVxE5nNAMZYbU1AhFrOTXiyr9F8AQPmjUb_xcVezs-bxqkjC6djA4JLKwmg1CGe91aRoBNYliJqUExmxNalKD0N8rvbmxfuoOv3x00qeBi-KCAWfLa0iq2trhazznqXP2Tr8-coCJ3eacLPD3zA3BD6yyAut25kfRtNRpFHNjWaTRsTdPwFLgEcP6nKWqBsACj0OpOelsXYb618Fq1wfprA5k6nDLVC_Sw-8He3c7IJgmFuIN8dNu6B7NcazPE2yyBTrY2_ikd5xoJS2Lqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: باعث افتخارم بود که امروز دارلین گراهام نوردون، سناتور کنونی و خواهر سناتور فقید و بزرگ، لیندسی گراهام، از ایالت فوق‌العاده کارولینای جنوبی را در دفتر بیضی (کاخ سفید) میزبانی کنم.
ما سال‌هاست یکدیگر را می‌شناسیم. او فردی فوق‌العاده و یک میهن‌پرست واقعی آمریکاست.
🔴
لیندسی یکی از بزرگ‌ترین انسان‌ها و سناتورهایی بود که تاکنون شناخته‌ام و خواهرش نیز همان عشق عمیق او به کشورمان و ایالت کارولینای جنوبی را در دل دارد.
🔴
در جریان دیدارمان، از دارلین خواستم که برای منافع کشور، در انتخابات مقدماتی ویژه حزب جمهوری‌خواه برای کرسی سنای آمریکا که سه‌شنبه ۱۱ اوت ۲۰۲۶ برگزار می‌شود، نامزد شود.
🔴
امیدوارم این کار را انجام دهد، زیرا هیچ‌کس بهتر از او نمی‌تواند میراث برادر عزیزش، لیندسی، را زنده نگه دارد.
🔴
دارلین که از خانواده‌ای فوق‌العاده می‌آید، در تمام زندگی خود یک برنده بوده است.
اگر نامزدی را بپذیرد، از حمایت کامل و قاطع من در انتخابات ویژه سنای آمریکا در کارولینای جنوبی برخوردار خواهد بود.
دارلین، نامزد شو! بدو، دارلین، بدو!
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/135162" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYydIOTKEYe_Doclmljf_KTgub_HQXFCJmV462emAIdcvBcjPXqlvjNPPH0s0WpWU1M2P5QV4lzOqwK78iDLwqqA_WYaG3qnGq-l5TR0RjoVQPGzrjSVMDhOoU2Jll7tsoP7uknWS7UeNV-eEQt1cVwdhFbSZRero6V5AYCUjPC7JUSoLfFMqlHkoo7SLY0mQlb19YTus2IywY1Wo_qGtdiO9ok-BHTwhYyg_GfdIPfXfnOH_hY0f5TJTJx8CwiOfk0h1HI-LzsbdyB6JfR1bQCQGUkfO7oEuBPYEjljlNtYN24mxbAmTw4fS9ToWqu7gb91M8zJHlG91AqEK3u1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: یکی بره ترامپ رو بکشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/135161" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
وجود شما حرام زاده های طرفدار حکومت تو خاک ایران از ورود سربازهای آمریکایی متجاوزگرانه تره!
🤔
کی داشت با وینچستر تو سر هم وطن های من شلیک میکرد؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/135160" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135159">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPsMqkmSV49tikJstyFX7nS_gNFS24Fcxz0w5EqlSWwBCqxmMFTy4CCAFBJW3HxlPRTP5wGhggT06h4RTUhwrN4VD1a9knd5UPAh7GyvpQi7_w6A1Mai1V0YvCL7qWkCtkxFTL3_b5gIveIoF0KYvYOp5pBcBLjPlJUGYOE04_sUxoeTXUY-ro5G9m75oGAlOqsydeR6eH1JWDE7mUaA3f0sIThRDAhT9KgMO4NAPA9jl2tDmZhfiiHjxSlmqqNJ27mMWXnwfl0YpW5UKyBRwmdM8YgWAmMtJCi3HAJ8kiGk21Z4rwbVXJDPPPcIqHH8olfhbT5OEm0_3zHTKAK1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی دبیر:
علی دایی برای مردم ایران عددی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135159" target="_blank">📅 23:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9cwvAu-qpMGGZZPM5dY0PvUXNPgdUQ1z17U6Qhdfq4Aog19KEVMhmYoX7xZoFS9za1wyQrd0rbA5gh3VUc_JiYml8ECg3Z43eKKY7DNGGc-mnPpDl2NpaIcDuDn5Vwi-J9I2ZqdqpW7MNOq4LiPPbn0sa39_NDbHWFhepz-NUFICpWAbHo6XYdqvF0Uz4oCJPdvGu8Dnth78xhBHA9leDvTKhrzRJKf3mVvPm47wv8U8M5g-31RcxyF88viYjMNiWjdAaQmLmnicYZ5-nszgypsfj6gtxrmRkaVr__nV2NTAV7bbezDSrGy3qVzMW7UFHKLW8hkvuw0AUFSm0yvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیشرت ایمان صفا تو ختم مادر عمو پورنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135158" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=lkNzNRb-TD_7KIqPLmFVtF1tNCvCPO9nl08fj159QjQFa_KXmBvJvzKsOSaoCc2y3h3QWejgOddeBErMaWpSHnFVIvQqSvsJFMxt1ukahxdJLDlkCFbd_szKQKc_7BBN26HZZrJP23V4QgdL5ro62FIRSBY5l9mU2JqEzsQZqEPYYv1j98SAokdU5zGXQrjMdiDXLf79geU9QTRkYm4c_kTK_QqOiiB7-3DASy8uLiTQEjN6i0zm68UrRL4CYE-4F2_7PBHR9ETk0XJ72FIRIilyZIkh7qjo_rszchJvm85A64AHiQlN3Sc7GdRWu3IdDosf1RsxawM_zk-0-XoEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=lkNzNRb-TD_7KIqPLmFVtF1tNCvCPO9nl08fj159QjQFa_KXmBvJvzKsOSaoCc2y3h3QWejgOddeBErMaWpSHnFVIvQqSvsJFMxt1ukahxdJLDlkCFbd_szKQKc_7BBN26HZZrJP23V4QgdL5ro62FIRSBY5l9mU2JqEzsQZqEPYYv1j98SAokdU5zGXQrjMdiDXLf79geU9QTRkYm4c_kTK_QqOiiB7-3DASy8uLiTQEjN6i0zm68UrRL4CYE-4F2_7PBHR9ETk0XJ72FIRIilyZIkh7qjo_rszchJvm85A64AHiQlN3Sc7GdRWu3IdDosf1RsxawM_zk-0-XoEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روابط عمومی ارتش:
ساعاتی پیش و در مرحله سیزدهم عملیات صاعقه،
سامانه موشکی  نیروی دریایی ارتش، با موشک کروز ساحل به دریا، شناور متخاصم دشمن متجاوز را در شمال اقیانوس هند، هدف قرار داد.
🔴
شلیک موشک کروز توسط نیروی دریایی ارتش موجب ایجاد رعب و وحشت دشمن و دور شدن شناور متخاصم از تیررس رزمندگان دلیر این نیرو شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135157" target="_blank">📅 23:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99HLxpH5AgDMNgNtu9lLcgYxQkYy9LoKDbqJ2WVaNErkBaWlAtcExDBiAT5Pdmy_OjdXZLdZoT4wCdpbbd_djLdVi19uwToL0yIsl22kKqcB2_2bqnGrv-YGhEmsDBlkRMUJa0K1ojZV7D5lSLVNjjXwuNDeTcAWiAtsB1v_8hZL0t7i80xVeb4kvbPIe0oKICLrZcp-eX5-ZBmbTpjlKZRU_cG24WMh_i7FS33TLqrFn7ZbmjhlVzjnriBlvv0ALqy2VvCuibibcGQDP5E7R90IVq1M9kHP02d9cHIieXYPQ5VReNfh5K4WNGAGQ0iBzY83D8fgvGpE0piKAlC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دومین استوری بیرانوند علیه علی دایی !
علی دایی که با ترفند نخ نما شده‌ی سکوت، مدعی مردمی بودنه ولی چنان تیم ملی رو به باد انتقاد می‌گیره که انگار چه سوابق درخشانی تو مربیگری تیم ملی داره.
اون روش مذموم که علی دایی با لابی سیاسی مربی تیم ملی شد، هنوز از یاد کسی نرفته. ولی تنها مربی‌ای که به عربستان تو آزادی باخته، روی فراموش‌کاری ما حساب باز کرده.
این روزها که کشور مورد تجاوز آمریکا و اسراییل قرار گرفته، جایی واسه ادامه این بحث نیست، ولی دوست ندارم باور کنم تو میانه ی جنگ وجودی و میهنی علیه ایران، اسطوره مردمی (!) فقط نو نوروز نور رو بر تاریکی پیروز بدونه تا با این واژه‌ها، هم‌سُفره کسانی بشه که آرزوی بمباران ایران رو داشتن.
باور نمی کنم و حتما اینطور نیست، چون با ادعای مردم دوستی نمیشه در مقابل جنایت میناب و دنا و بمپور و کشته های جنگ تحمیلی سکوت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/135156" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpiPbXb3KehxTLCFWfSnE1Ys_jToinImHPLbjZvlXuUNzOJx4UomcbgkJVR7kdpvxDb_AW_J6bWN7cDAl61dEIipm0rPv7obewIFqPw7j1fO87X1saB_1cEBcQlaGTeAl87d3a7_dmxm0NCrAeytKkHkdcRR15-hH0IIqPr6eixH6vt_KCv1LTfHAMpmLxAeScC5NAO4BJdDlHIScPJSnmooV0WA7yVLAWCz9K34naUGS82IcwjY7uQIPo9pNg3gM6U65ZZKuzfIkDzEJ2rJ4-R9IzA8V533YjHLZMrPsZNCmCGcxkcNhGKGRsodUAVFgxLU-WUn1Y-Su8NE6we2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری علیرضا بیرانوند درمورد حرف‌های علی دایی!
علی دایی که دوست داشتم همیشه بزرگوارانه حرف بزنه و با احترام ازش یاد کنم، تو مصاحبه با برنامه ای که عواملش واسه باخت تیم ملی در جام جهانی دست به دعا برداشته بودن، من رو مسخره و تحقیر کردن.
اینکه من به عنوان بازیکن بگم مجسمه مربی‌ام که واسه اولین بار تو جام جهانی نباخته رو بسازن، نشونه احترام و قدرشناسیه.
من که نه تبلیغات سیاسی کردم نه از رانتی استفاده کردم بلکه به عنوان پسر کارگری زحمت کش، بدون هیچ رانت و با تجربه‌هایی سخت نزدیک به 100 بازی ملی تو 3 جام جهانی و جام ملت‌ها به تیم ملی کشورم خدمت کردم. شایسته احترام هستم یا تحقیر؟
رانت‌خواری و فرصت طلبی رو همه زشت می‌دونیم ولی کاش تو خلوت هم اون کار دیگه رو نکنیم، کاش چهره ما واقعی باشه.. زشت یا زیبا اما واقعی...
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/135155" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/135154" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
وجود شما حرام زاده های طرفدار حکومت تو خاک ایران از ورود سربازهای آمریکایی متجاوزگرانه تره!
🤔
کی داشت با وینچستر تو سر هم وطن های من شلیک میکرد؟</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/135153" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
دشمنی "آیت الله BBC" از آغاز تاسیس تاکنون‌ با ایران و ایرانی</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135152" target="_blank">📅 23:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
قیمت هر لیتر بنزین در پاکستان به ۲۹۵ هزار تومان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/135151" target="_blank">📅 22:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14874af67.mp4?token=Fv-XzN_CBfTPUSv3wjsd-Sx9tBdJuIvV1Ji78IkBEcNxBYVaDEY4YmbVnncOBjKZJT4BSEnGOWbh85dcWhQMA0g18tUaVmAfCETkGBcTHiCKloo6jVFYSmfnqex2JCdOSKBo93Ak8D4TukL9tJhl6T0EbhzElSOCCGbPQP3uYo9Su1ewIj1N_BuZQdaoDXJ6VFhPwEd9cQckJ0GsQW9OMI7RPOjtcRGIDP7kgnKRF7YM8AAamZApznIPzetdIksr7xOmLwa45L4WhoMFz82w77AM2-VHRaWFlpscvS8PGq9M_16lIlToB-YpWpUJI1KbyNPx0fEteNO06cVVppNRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14874af67.mp4?token=Fv-XzN_CBfTPUSv3wjsd-Sx9tBdJuIvV1Ji78IkBEcNxBYVaDEY4YmbVnncOBjKZJT4BSEnGOWbh85dcWhQMA0g18tUaVmAfCETkGBcTHiCKloo6jVFYSmfnqex2JCdOSKBo93Ak8D4TukL9tJhl6T0EbhzElSOCCGbPQP3uYo9Su1ewIj1N_BuZQdaoDXJ6VFhPwEd9cQckJ0GsQW9OMI7RPOjtcRGIDP7kgnKRF7YM8AAamZApznIPzetdIksr7xOmLwa45L4WhoMFz82w77AM2-VHRaWFlpscvS8PGq9M_16lIlToB-YpWpUJI1KbyNPx0fEteNO06cVVppNRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع عراقی از حملات پهپادی در اربیل و فعال شدن سامانه پاتریوت مستقر در پایگاه آمریکا خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/135150" target="_blank">📅 22:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
معاون استاندار هرمزگان از فعالیت دستگاه‌های اجرایی این استان طی روز شنبه ۲۷ تیر ماه با ۵۰ درصد کارکنان خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/135149" target="_blank">📅 22:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وای نت: تاکنون بیش از ۶۰ هواپیمای سوخت‌رسان آمریکایی وارد اسرائیل شده‌اند که ۳۳ فروند از آنها در فرودگاه بن گوریون مستقر شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/135148" target="_blank">📅 22:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aea9b3cad.mp4?token=uuf8wdxsLXBdZtzqWrjL9Jq7TyFlWRM4NqBo50zDaEINHCxRuQWoklGJk0d3AzMparPeFK6svjMer45vEgRPhnurWsRqaJbnsXimS-mX5cci4l3m5D59DncvjOnNNvcCo-cVNcOTPrdGQ6fYgqa4S66dko__3tCxBuPAjsNLXMCg1M107Gwn9TT1IsT6d-M1IT4declZjPCaWOgARr4Phcqln3JBsNHI2uzjEZSJKjDo47XyHasYy0YgM-QekV2qZ3hKpSibPWcqeiiERgMi1FHsK3zOzDk4vz-SDGMrztKPUtQEXrBAr66chl0K9qwPiWj2RoUtiGhkNSkVbCr7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aea9b3cad.mp4?token=uuf8wdxsLXBdZtzqWrjL9Jq7TyFlWRM4NqBo50zDaEINHCxRuQWoklGJk0d3AzMparPeFK6svjMer45vEgRPhnurWsRqaJbnsXimS-mX5cci4l3m5D59DncvjOnNNvcCo-cVNcOTPrdGQ6fYgqa4S66dko__3tCxBuPAjsNLXMCg1M107Gwn9TT1IsT6d-M1IT4declZjPCaWOgARr4Phcqln3JBsNHI2uzjEZSJKjDo47XyHasYy0YgM-QekV2qZ3hKpSibPWcqeiiERgMi1FHsK3zOzDk4vz-SDGMrztKPUtQEXrBAr66chl0K9qwPiWj2RoUtiGhkNSkVbCr7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: اگر فرضا دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135147" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فاکس نیوز: یک گزارش محرمانه که برای ریاست‌جمهوری ایران تهیه شده، نشان می‌دهد تنها ۹ درصد ایرانیان از حفظ وضع موجود حمایت می‌کنند؛ در حالی که نزدیک به سه‌چهارم مردم خواهان اصلاحات عمیق ساختاری یا تغییر کامل نظام سیاسی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/135146" target="_blank">📅 22:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
🔴
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/135145" target="_blank">📅 22:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا مفاد تفاهمنامه را زیر پا گذاشت و از تفاهمنامه فقط یک اسم باقی مانده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/135144" target="_blank">📅 22:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZExUAXlb8ZxcDQsiolSczwbZFvFITHsPJNlm09EEFgwKXAAyKEqaLoml08oagwcuEzAQNSxKiYlOKJc2E48qoBd5jorIXji7KGpR-h5rDnNW28pcfBCsKC6urBcRii3qhTkjDOpX0pqbsjDB5V4Ec9hijVknpRWE-cFPbKdS_BEEbgoQNaGQ7JbnRDj6O7ni27DbGcq1vlcO8sGeAmy4s7Ech6UqUGYaz2ilggUG1gdziAlM1ZI7CP0FK5fgmd2sU3DHMEYWmFXvRDAjWF_M6H194bSDrvnRk1oM91RpMB3iI2R5OUbpNP1-N_XwCa9JevtUiXYJ7nj-b5Q0AAMOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ب
لند شدن پنج سوخت رسان از تل آویر به سمت خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/135143" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا مفاد تفاهمنامه را زیر پا گذاشت و از تفاهمنامه فقط یک اسم باقی مانده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/135142" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بیژن زنگنه در پرونده کرسنت از سوی قوه قضائیه تبرئه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/135141" target="_blank">📅 22:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پرس تی‌وی: هیچ پرتاپه‌ای به محوطه نیروگاه هسته‌ای بوشهر برخورد نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135140" target="_blank">📅 22:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPi7miaG7yoTcMKmBlnkRbsDsekY7mK2Udp88jUcdErExVdit87eH1_GweYxOpMR868aUQqi3WAIhOjZXA3Xa_hFMZc-JN-gYBP5j03DFlXUB7XYZpSctVBGVAHyBKeKlSo3TLBef-HrdIyiwKpwV7ROaW0riDz9S33rnk81-tfi2zt0h4fyS_-8IGIv3QgS0tSOf-4ZUouPv--DhSkjrRm3Io7bNYRJsRFlmxz_Z2pugQZ_vky5CKODFT8sp5T-y-dcQkoZZzt7KLljsHE2gf5ndGVwC0ETw9gsZghtEALUlvj28B805oNzWWhmKDuhGomAhHtP5MnvW4HE-1KFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: سه نفر از روستاییان هنگام عبور از پل بندر خمیر شهید شدن،اونا بیگناه بودن و ما هرگز اجازه نمیدیم خونشون هدر بره،ایران از جنوب تا شمال و از شرق تا غرب میهن ماست و ما تا آخرین نفس از هر وجب از خاک خود دفاع میکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135139" target="_blank">📅 22:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAllw1zzlmePKKHyS-Cibl1_isC1ShR90QioSrmrbygXsSEfKEZU3VAO4fdbpKI-eV88QdncZXVLyjPja1inEqgJB0KyF5-JS9iQAeCDMTaybFt032Riecb4UcxcQZ449c2lA-TAVgSd1xnLOk_PE18Awi_SKjjcn4CJaaRh4XA7CNMK5fSCJ5SWv2ltC-84zqBfuZd-rmThhaTPc4tpTebt41N5-R0wjCKEBzn5TMGLPTwE6NhuZ5W8v61c68KtLQVsHGyJGJuk_nvoi0F5mjBWVpP53_rSbjupYCV22qNAz_3jdTITqCvlCKuWeMt4mAETcWcxeOxDEEZ5t6U0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا در ۱۵ روز گذشته در بحبوحه حملات مجدد به ایران بیش از ۲۰ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135138" target="_blank">📅 22:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سازمان آتش‌نشانی کویت از وقوع دو آتش‌سوزی در دو مکان در جنوب این کشور پس از حمله ایران خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135137" target="_blank">📅 21:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CayAZZyQi0zjl2Fkj1NitGQw3x4Az8Nyag_I1PPEXe3nb3Ij-gllk8VfNaS6v7aaxYjlPvMRbXaUkj86beKNYfTkoqBTSMW774POwrGQoF3_RLSSXB2q8rTggbEKREYlG0YqjlF60jwXUq0Z7GCnt-iXuAiblqkG1D1MzAxpRkUk_MJn2ONh0RoyieDf1GIWPdrqX32YgbfMlbd77uVA1WaJ4fAWTJ90OlwzzD8MCLY8sNMGD7hnw2cVzzSVgXFzZCPwvOPXzkf9RhhcDcirPhrr2JPnoWANZEhJXTxfQ-eEjM58ULiWpFB3NtATIVUNebObReRpCjiQ32dimsD9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت ۸۸ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135136" target="_blank">📅 21:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هواشناسی: خودتون رو برای موج جدید گرما آماده کنید که نزدیکه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135135" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxzH28XvkrL-DQF0aM9yLIEcytutv9Xfb6YCFuvCBKDLYC8hA20_OthI0qsZRBRz-Zi58HMsRANq0iF7agg1Rdir4UOyYhpc43fnD5iBzQLyOZyUEMpvHm4EHNYdRmQtCbwU8Y033nNT8z1RZqjn1r5EuiVF0Wk2iDXXbG6orxIPEBTL8oYgvc_EMF_v1hodWceqOifm5AwSOVqQOd7tMh9UcxV1kyk6-WOLdf3EE4mlKAvafBlGp-vEh3cVz5ytD6IRn7SNZR_kE8NlORx_SxWLgzSYOOYPWC7BriMpay4Hwzp3vn6mi7fiXyvjIxCiBOPXXKkP35a-YfJKRbT9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین بورس آمریکا
🔴
با احتمال حمله سنگین آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135134" target="_blank">📅 21:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c089a5228.mp4?token=iZ0Zy3DoNacWMnD4Gqkr0q8KCgnRERNl8dkh88nJNu5ZfJe7gu_KXNrQ8SeEG0xinfco3G5FMMwVukgOTN_3vzXWqEwjjD6Ozaog2miVNin9HWEtTivD3972an3ggoZMa-z0RR4Z0vyEcj5dfoBr5B_QGup3OQspFyA8tLBxMgRizy7ChfBT9SO1zFVi8D2KECkVZ0p8HEnI0jsoOoBuE9agjdAZ3AMLf8lbKqfkC2NcI7Y8ZvDp4wXE_fX2Wwya0aVb6cRRkbZiRdO79zLCqSHQ6jFrOSm_OYZddi68Eqw33AdGoeX7dCg7KDLli9wxlRnbxbW4yJZTHksZnsWoRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c089a5228.mp4?token=iZ0Zy3DoNacWMnD4Gqkr0q8KCgnRERNl8dkh88nJNu5ZfJe7gu_KXNrQ8SeEG0xinfco3G5FMMwVukgOTN_3vzXWqEwjjD6Ozaog2miVNin9HWEtTivD3972an3ggoZMa-z0RR4Z0vyEcj5dfoBr5B_QGup3OQspFyA8tLBxMgRizy7ChfBT9SO1zFVi8D2KECkVZ0p8HEnI0jsoOoBuE9agjdAZ3AMLf8lbKqfkC2NcI7Y8ZvDp4wXE_fX2Wwya0aVb6cRRkbZiRdO79zLCqSHQ6jFrOSm_OYZddi68Eqw33AdGoeX7dCg7KDLli9wxlRnbxbW4yJZTHksZnsWoRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از حملات ایران، یک کوه به طور کامل در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135133" target="_blank">📅 21:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/621b16c793.mp4?token=Dn_GgJmbzLhbQUKuUKcYnpNraYMAFRwRDb5fTdL9vK1oxUguZOi9bQ4JU0v1-TQqMez15uwVn3KdMgBTTGr2HGHGnMaXbU8rUnoa3hBdRnLaXUyxcEvHTJZbGqKzWiVAxrrGdmlhdF-4c4j3K27RaE95ZAhhvbURIjaRdU2uO-VSG8LGZYspI4lzVoghU49Zb-MkzV29_xR2PMSu5uw3t82_etSi53c3m1jyhEUFBK17KQhxZZaxozw7cteq4NNrXF5nLEEKVO6uXtET-GfF0DTAFfD8J9AwhsVCv8OYH5nJVzzJsXYjyz8YcBc_HKD-YF4yS-2Qq34HPG8u9oqooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/621b16c793.mp4?token=Dn_GgJmbzLhbQUKuUKcYnpNraYMAFRwRDb5fTdL9vK1oxUguZOi9bQ4JU0v1-TQqMez15uwVn3KdMgBTTGr2HGHGnMaXbU8rUnoa3hBdRnLaXUyxcEvHTJZbGqKzWiVAxrrGdmlhdF-4c4j3K27RaE95ZAhhvbURIjaRdU2uO-VSG8LGZYspI4lzVoghU49Zb-MkzV29_xR2PMSu5uw3t82_etSi53c3m1jyhEUFBK17KQhxZZaxozw7cteq4NNrXF5nLEEKVO6uXtET-GfF0DTAFfD8J9AwhsVCv8OYH5nJVzzJsXYjyz8YcBc_HKD-YF4yS-2Qq34HPG8u9oqooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای ثانویه در استان سلیمانیه، کردستان عراق، به دنبال حملات پهپادهای ایرانی به انبارهای مهمات نیروهای مخالف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135132" target="_blank">📅 21:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135130">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bbc955ed29.mp4?token=sQZGssgirVaIiKuAxbCv1K7RlrOmfRQcj7JcXECNZb7LXPf8_Mm49WvUSOAWUEkvs6HH9w1-89G9_sPbweUs40PmSQobJYOJVC7u2WjK9BqFzoYNi6dSsoKM4GQeisaRC3IDjZaIbsGPnenhFRsHo5DRBIADftxFSsFRrRQZHpfRQu_23puf2bvHHyknTaP4tpdLM5UcTopzgxo0tyPD5LRYIl0oxYE-VfHjNFIWmBSUhrwsBiC9qTr_wiCPy6HRYmT7Ae-7Yv0kCyx_OdEr_L_Lb9if-Mque2vxGvRaz_8W4C2VtihKheegPIgNPihzlVtyFtIXvJzQ-3HHTWZ7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bbc955ed29.mp4?token=sQZGssgirVaIiKuAxbCv1K7RlrOmfRQcj7JcXECNZb7LXPf8_Mm49WvUSOAWUEkvs6HH9w1-89G9_sPbweUs40PmSQobJYOJVC7u2WjK9BqFzoYNi6dSsoKM4GQeisaRC3IDjZaIbsGPnenhFRsHo5DRBIADftxFSsFRrRQZHpfRQu_23puf2bvHHyknTaP4tpdLM5UcTopzgxo0tyPD5LRYIl0oxYE-VfHjNFIWmBSUhrwsBiC9qTr_wiCPy6HRYmT7Ae-7Yv0kCyx_OdEr_L_Lb9if-Mque2vxGvRaz_8W4C2VtihKheegPIgNPihzlVtyFtIXvJzQ-3HHTWZ7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به سلیمانیه، عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135130" target="_blank">📅 21:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135129">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجار مهیب در هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135129" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135128">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تسنیم نوشت: امروز یک کشتی در تنگه هرمز مورد هدف قرار گرفت.
🔴
این کشتی با پرچم کشور تایلند بدون توجه به هشدارها و بدون اخذ مجوز از نیروی دریایی سپاه قصد داشت از تنگه هرمز عبور کند که با ممانعت نیروی دریایی سپاه مواجه شد و مورد هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135128" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135127">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135127" target="_blank">📅 21:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135126">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
صدای انفجارهایی در اربیل عراق شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/135126" target="_blank">📅 20:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135125" target="_blank">📅 20:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا جنگنده‌های خود را از اروپا به خاورمیانه بازمی‌گرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135124" target="_blank">📅 20:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135123">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: ایالات متحده هیچ برنامه‌ای را برای اعزام هواپیماهای تانکر سوخت‌رسان بیشتر به اسرائیل اعلام نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/135123" target="_blank">📅 20:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135122">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apgXyJ3nvXyYD1p_5lGykjeBgywaSLRSXFE_JFUlt9egkocGPFbIY_8IV5IWlDjUnqNVu3XXkSS1DAccRCqvXupP2a2i0yVWb-W9MnMmqOY9A-0brn36m3zSRaxN4QQHq3HFAJH1w7TSW3oBOVWey5j9CxjS-plgBA86-ATXEc1-s7ag3-d4cvMtzhYzHuUGQo24E1YgH3cNhMYGgsxm9hfeLWIw6XXS1XAVkMbp-xURXQe1SPyKviDgXUizdf4uemBoVLUklqxv_Tm8XiBzS9X1syg4psPNZ6XjgvQwFQsOIsRvac2jppQ6LQCkcQ-C1u3fmNi6ovNCUYdixq_2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای  ایران اینتل‌واچ : سناتور لیندزی گراهام توسط سم نوویچوک کشته شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/135122" target="_blank">📅 20:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135121">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e68436f0.mp4?token=czxg-ozhAkDIHzyZfq_wlNt8kKB_W4wEM89gD5E2BSiuJLvNJAJjgtUZtHmaoPjM8Ns-XZQHiATdf9Oc4EbN4yOyUjskR0NYgiM-VShHFptCrUGtEv-yTEXyIZPT-LKoIBaxZq9XEcfa-Up6NBjjLprqDR25jzSoFeCvtz0kjjan4vtKBhtrg0t19-N3mR7XKuBCLZj9840MmaETb7OlZchnxMle4NqCpM1BIFH9-Xo5orE46155Ifwx8wL9MTxbm60wjZ5XmODJ6kayHKgpmxr2AD9JZB_3CxUiKz1atIRSvLufcg7sF8rB3zDn3B0nU2LPjnM9SKfXmhihMzjwPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e68436f0.mp4?token=czxg-ozhAkDIHzyZfq_wlNt8kKB_W4wEM89gD5E2BSiuJLvNJAJjgtUZtHmaoPjM8Ns-XZQHiATdf9Oc4EbN4yOyUjskR0NYgiM-VShHFptCrUGtEv-yTEXyIZPT-LKoIBaxZq9XEcfa-Up6NBjjLprqDR25jzSoFeCvtz0kjjan4vtKBhtrg0t19-N3mR7XKuBCLZj9840MmaETb7OlZchnxMle4NqCpM1BIFH9-Xo5orE46155Ifwx8wL9MTxbm60wjZ5XmODJ6kayHKgpmxr2AD9JZB_3CxUiKz1atIRSvLufcg7sF8rB3zDn3B0nU2LPjnM9SKfXmhihMzjwPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش صدا سیما  از آخرین وضعیت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135121" target="_blank">📅 20:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135120">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
موگرینی: ترامپ باید در مذاکرات با ایران رویکردی منطقی اتخاذ کند
🔴
مسئول سیاست خارجی پیشین اروپا:
ترامپ باید در مذاکرات با ایران منطقی‌تر و منسجم‌تر پیش گیرد و یاید اظهارات عمومی متناقض را کنار بگذارد.
🔴
دیپلمات‌های ایرانی برابر فشار ها خونسردی خود را حفظ می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135120" target="_blank">📅 20:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcH8d03-FwGETzeED3Mokp_9VEp8c2ujIM8CX62b9171uAeMSUIGMSXUbUVsNESnf-dUrrBSLtopXyfpSl3vLWxj3-MvEWqnSvwVmRJuF1KwADq8C3AjAVokWnz6dsWYsQ9ulXCqQASt8oBBknb4lwQ64PVOpxjRAJ9RC4wTeYMNd5zXi9qb6XN6iIX_fxhvPaxE3KozCFGOo2_WzkSC6hXs21mXimot05QKYp0PC4lIo5MuIwXfw6tqrOQIhKTcUwMciVDzaBssoVO7m1TY7WISRzW06HHziyZhiehh3n2Gin1uVg9uFo_2C11YPrp08TfNHnIB4qL9JSQCWbi0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موقعیت سه پل از پل‌های هدف قرار گرفته :
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135119" target="_blank">📅 20:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGe1W5C6baOLD8-t929Yk7Go_9LLvlUNwsYbHV0ZYyIM7VUD_ScfjPBgOtLnNrJ80o7fG75KZC4zwLR57kWe4pP1GFTwpvz5yPMu9ZOp8LKVsj1JgWKu-vPsTvUmNU6X3ZHnqL7HVVmMpPYQWH9KipVrEkxlhbFy0UyyvXHzJg7cBAv9kQITPfORFneWoXgksfLZm3COygw8D8F5GdVCvqigQcb2tKO6A0XfL4rrgBly9gHSmJ2LWYEv1fv8dgjv6LNzNidYAUI1gaz5Xw6j9KHXFCSmmjJYDQycZWC41ZCNFwBIaLslSWZ8MiNsFAYbaXgxQ5rDOFFc1W16nOxNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت تروث مدیا به مشتریان خود اعلام کرده است که می‌توانند با پرداخت ۱۰۰ هزار دلار ماهیانه، توئیت ها و حرف های ترامپ را قبل از انتشار چند ثانیه زودتر دریافت کنند
#املاکی_دیوث
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135118" target="_blank">📅 20:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFTjtuyHhARe1xj0-JG7bR_pJ27nra7a9C3zsa8HOUX5khRl6hT1DXysRITcaXKrCEdLASHOoZoXmvkpzPq746q6zjfeV6qBP9diMgLRuqUIpSyOBiBJkq2US9mSKTfvqDx9KKRI0xyVgFVRWaWSBnnPTtbsG8pFDInzb1folmsnD9tdKBrrdYTEpkRaLjRdTQ5qjy6W8nJIBWHo4naV4iG6bbsnADSvFSud36oMPCXiddCLDQQzSNSUwhSLqdDx4RrQ_ZyVFyiNWMM26h6j1VCTqq2-u5M7rOzvP5Sc5dEZ5-VavsgCanjOwQZ3c4clwCDMxNSKda6VTjCo3cymdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترافیک سنگین هواپیمای C-۱۷ ایالات متحده از پایگاه های مختلف آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135117" target="_blank">📅 20:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ8mLJYsO_vuxJgQ-a69Wq_JSVa_4Zh_zrmA-5PxoQokwjWz06mamjl5B-1n1gh9N8HyZV-jIRQbATzNwNFtwN1MmwU9vKJKq-0GeyfLaHWap6rX2Lq5gO0jNMaQSHxICyTyepatkVb899ozswUR17fxOD71zVQD0YSJZ5FkaYJvGxH8bGbjKRchgW39pnqqUaIsYG1-KmYnfteCJoI8tYqVyJ6mflZaXP4YzjDj0DVgChlnVC_b_3XWx5l7l-OIcs-og_A06sEPslBj6PnQQ6tz_eF3Od8jrXuI2StOqdJy6bh_BMUI3Ze9VNDd3q5QXxvhSbGOArJtHhZRKE5lSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اردبیل
: ما تنگه هرمز رو به برمودا و باب‌المندب رو به دیوار ذوالقرنین تبدیل میکنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135116" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
باراک راوید: واشنگتن در راستای پیش‌بینی گسترش احتمالی عملیات علیه ایران، به اسرائیل از استقرار هواپیماهای سوخت‌رسانی اضافی اطلاع داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135115" target="_blank">📅 20:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGh5ybDeNCIBxtkd4k9moumd97GoF6QO1vPg2XLS22NZGVPmdmvlWJPCImn1pAtX2e6kYVQSo22F2rMj3MGc-ypqLIqRGtdMKQ3NeFxACasNWA812ulMvYoZKDsVj0GjGOaBNOBmvyMXCx7nsEJnOduMr1Ep_02HB4iIup8n5IuVIQnRgOldt0yeOde41lvFf565V_cZTQTzbm7ZxtyHXmaCZz_HIGqoHgHne_ZoQt1h7LNPdqeHtz1HLNcRXwu4UEj-8oNhXjaitnygqEC_7VQYgZOVvdnjB3Bz5yKjrnZUt9Lkku7UX3n_KROUnhrpiHoa-wOXdOLIeNnuBYXqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست فرماندهی نیروی دریایی سپاه:به ساعت صفر عملیات علیه یگان های دریایی ارتش ترویستی آمریکا نزدیک می شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135114" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1065e7e088.mp4?token=EpHapM7MVbG42ebRAR-yxmWalztEu_pnwt3OALTXaI0KEuGc9RLg-J78V5pftN4YILgVIMF6LoxtjSKWNVp3iZTUxIlfktgfF8ygtHAFE8pkrUT60M3LJd-B5A9U_t_Mb8ERlUAl4dFf1yQUNtzf8THcfVtCN8wKo786tse4jKKIzV8D00E67C2eICleYs5oAFC7FSqWZ1c7it7BRoY3l4Uur9tIN-44Rl9eiG2xfnBtq2qCNnxBYiRTkc9-I-Sl9jgsrRswU89LkcFI-irf9T3UsPmu2Nbp6aHCg1mZawZ881yT2_6qFeZcR1muh7wEBi9AWa-dLpc-yNe_uaL6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1065e7e088.mp4?token=EpHapM7MVbG42ebRAR-yxmWalztEu_pnwt3OALTXaI0KEuGc9RLg-J78V5pftN4YILgVIMF6LoxtjSKWNVp3iZTUxIlfktgfF8ygtHAFE8pkrUT60M3LJd-B5A9U_t_Mb8ERlUAl4dFf1yQUNtzf8THcfVtCN8wKo786tse4jKKIzV8D00E67C2eICleYs5oAFC7FSqWZ1c7it7BRoY3l4Uur9tIN-44Rl9eiG2xfnBtq2qCNnxBYiRTkc9-I-Sl9jgsrRswU89LkcFI-irf9T3UsPmu2Nbp6aHCg1mZawZ881yT2_6qFeZcR1muh7wEBi9AWa-dLpc-yNe_uaL6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زیر ساخت ها فرزندان ایران هستند که هیچ آینده ای تو خاک مادریشون ندارن.
🔴
زیرساخت ها جانفداهای 18، 19 دی هستن که توسط عرزشی های حرام زاده به قتل رسیدن و مجهول الهویه دفن شدند.
🔴
چه انسان های شریفی که در طی 47 سال حکومت ملاها، شکنجه شدن، اعدام شدن.
🤔
مردم از این حکومت گذر کردن، با اپوزیسیون و بی اپوزیسیون تصمیم گرفته شده</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135113" target="_blank">📅 20:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سفارت ایران در بغداد: دوران حمله به ایران بدون پرداخت هزینه، به پایان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135112" target="_blank">📅 20:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
آکسیوس: ارتش ایالات متحده دست کم به هفت پل در اطراف شهر بندرعباس بمباران کرد؛ شهری که ایالات متحده آن را به عنوان مرکزی برای عملیات سپاه پاسداران در تنگه هرمز می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135111" target="_blank">📅 20:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmqjRm21-jU4MZLSokEW1MpEzPGpA5OY6jQN2Gnv61GCPkshzd19VCUaXn-1bp1oIbnCz1B31bcl_HJtcHjDL1LFD_54Q9SYEeqfsIghu0gMTr6VqmJD5nDvUDZjDBOZFLKMBVE9GXIMr-WVm_xqY6bo76SXKktgA-IBxY4b-Bh_Zvl43f9LX9iHt-EcfCt2RbTTUiYEprMmpNUZrHWtD12jKZEoWMhmJ3XmrsfewOYI_Faj2cCLEy4D9D_dcA2tQ8ZCR_cR7DUepftOi8DNnYDdC2fmVqpa7Or9-Jt0DnK5r5hj9YAawo-WRMmDkzYWIBBlvvfy524hF758RkgsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه : یک فروند پهپاد آئروویرنمنت آرکیو-۱۱ در رامشیر منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135110" target="_blank">📅 19:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/آکسیوس به نقل از مقامات ارشد آمریکایی: ترامپ هم اکنون در حال تصمیم گیری در مورد گزینه‌هایی برای یک عملیات نظامی بسیار گسترده‌تر علیه ایران است.
🔴
گزینه‌های مورد بحث شامل حملاتی به نیروگاه‌های ایران، حملات بیشتر به تاسیسات هسته‌ای و بمباران سایت کوه پیک اکس است که گفته می‌شود زیرساخت‌های مرتبط با انرژی هسته‌ای در آن قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135109" target="_blank">📅 19:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رضا پهلوی در مصاحبه با شبکه i24 فرانسه:رژیم ایران همچنان سفت‌وسخت به ایدئولوژی خودش چسبیده؛ چون رفاه و آینده مردم براش مهم نیست و فقط می‌خواد سرِ قدرت بمونه و به بقای خودش ادامه بده.
🔴
سیاستشون هم اینه که همین طرز فکر رو با کمک حماس، حزب‌الله، حوثی‌ها و بقیه نیروهای نیابتی‌شون به کل خاورمیانه و حتی کشورهای غربی گسترش بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135108" target="_blank">📅 19:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
معاون استاندار بوشهر اعلام کرد: نفتکش «بلما-ان-آی- ۲۲ » دوباره مورد اصابت ۲ فروند موشک آمریکایی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135107" target="_blank">📅 19:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روسیه: پنج کشتی مرتبط با نیروهای مسلح اوکراین هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135106" target="_blank">📅 19:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بیانیه ارتش : نیروهای ویژه تیپ ۶۵ نوهد با انجام ۱۱ عملیات و ورود به خاک کردستان عراق ۸ نفر از فرماندهان ارشد گروهک های تجزیه طلب رو با موفقیت ترور کردن و ۳ مقر مهم نیروهای تجزیه طلب رو بصورت کامل تخریب کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/135105" target="_blank">📅 19:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
تردد در آب های خلیج فارس و تنگه هرمز به پایین ترین سطح در 3 ماه گذشته رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135104" target="_blank">📅 19:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کلیپ وایرال شده از تور نقاشی! در جنگل‌های رزکه آمل...
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135103" target="_blank">📅 19:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Si_3vottYeh8EJy7bpgP5lTbTl2PafUvJAVKEL76fnO5vpY7oXaSd2IQObmPW_knhzoNr1n3nrp0CtAtmIdQxesCkJDsb0aEC6Kc1FDf-_qu9j8nm0kTHCf7KCCvFt_7xTY5z82nLE0_VbL1N43reGyKl9ZjIgnDN7XaE1vTitReJ7RGOqVOqW2C-6PJbvFhNse6d4R9DowiMKOQaKrdkYfTKYQrIaS-ZqAbhTfs6hZvTUCYJ7YOYR7NvlB3AREZcEHT1mDkagnbtO06G2DRru40l4HCid_HOtTFj2pS1HHvfYaIZfbgm8OduZVzWymGVVcUW3J06r-BzPg_rTSg2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطوط ارتباط راه آهن که شب گذشته در هرمزگان هدف قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135102" target="_blank">📅 19:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4Ky18UvNvtSpTfixxJ55Le-j3xKBZ1Z3EcSrCeXEd6T4SoS40sfhSihH0_oQsibnpHZEj487IXY3QERPX339QCpUuzDK8bX6ddCipjRh8rg4UdSI9u7bczIiQ3g6RrP1KzLuzP2WiM2UjDO58wFpXqx3RTsZqPwgfSt-f5EgYV1bKmC_jHO69riCiv076S4EIuJjYRsdOXDiV2KD9u-x-UpovKIcWai-yK13-1dXqhuuomKTbj2qPlEAsAnRqWI0FSj3oc5sAwmWWDXJFcko_l7MswwYCSiJHcpfygbd9UI0hBPHtH4zzgF6iJlDrF6NZ4aqpwTsR4okfYon9pv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز یک پهپاد شاهد  انبار لجستیک شرکت خدمات میدان نفتی آمریکایی هالیبرتون را در منطقه صنعتی مینا عبدالله کویت به طور دقیق منفجر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135101" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQnl6pXqdRlNINWOmuqaIxIZuRqWXmuhQ-B5tgd2STS_Sm9Nt_mLM20h7Lt2398Apj9iBp5bOApr1H725ydnJxdPAAZagkqvkXoPHfZx_mW2Rxat6Ed1CvVFIihvYoicsod_vKsuO6CdQ1ycsXVCUK3PDO26hKpGwsIrWwrOSHDT22TEtkpPDqjZFB7II9m7Z9la3EOFpXDwM-91QOqcBlSoryFLn2tFeMPXs7X80oJcbvVqNUZgbM25iUWCv7ZUlDvdvaHtDt_pQNeIZ0DyOzoRqPb8oxa2c-CelbvcfGkK8uFLOawSYEPWQs_6d1bb1WrAlUph3qcHr8ymnoLd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش سرویس زمین‌شناسی آمریکا (USGS)، زلزله‌ای به بزرگی ۷.۴ ریشتر در سواحل جنوب غربی مکزیک، در فاصله حدود ۷۱ کیلومتری جنوب غربی پورتو مادرو و در عمق ۱۰ کیلومتری رخ داد.
🔴
هشدار سونامی صادر شده است و ساکنان نزدیک به سواحل به عنوان اقدام احتیاطی به سمت مناطق مرتفع‌تر هدایت شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135100" target="_blank">📅 19:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135099">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd46584c7.mp4?token=IBSTdFiorXRiBUq3jK9om0Mhz75yTUfppZhjhtdf6VYcWHgK6GQOMMnEE2b7RGpAVSYOY0EK5FzeqxgFMHD6P2w7UQ_RKTfztpmQsdju422QS0d25JeOxAAdQ1icnYeMZ9DNutg8kJdkjB3YMbrwBvqrlI48mxR45SLsqLQAh3BOvts9Z_J0fEdEEFx2EKxYCu0aLVl1YlX99KIBR9923L-77qG6_VCscBygridh4pUF_NFHJo_ag_YFFDxcX82DqYkS9TfCJ6-BXnrkXpBdh69XGUY8uOhhBsanIc6SuJbJ2y9UNqhnox7je92KesNVk2jZvFK-2Yq2eQXz4WM94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd46584c7.mp4?token=IBSTdFiorXRiBUq3jK9om0Mhz75yTUfppZhjhtdf6VYcWHgK6GQOMMnEE2b7RGpAVSYOY0EK5FzeqxgFMHD6P2w7UQ_RKTfztpmQsdju422QS0d25JeOxAAdQ1icnYeMZ9DNutg8kJdkjB3YMbrwBvqrlI48mxR45SLsqLQAh3BOvts9Z_J0fEdEEFx2EKxYCu0aLVl1YlX99KIBR9923L-77qG6_VCscBygridh4pUF_NFHJo_ag_YFFDxcX82DqYkS9TfCJ6-BXnrkXpBdh69XGUY8uOhhBsanIc6SuJbJ2y9UNqhnox7je92KesNVk2jZvFK-2Yq2eQXz4WM94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع ایتایی: جان فداها به جنوب اعزام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135099" target="_blank">📅 19:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135098">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0e44244f.mp4?token=r2D7zU7uLyMMed2NoVyuVdxUGnBO8Bk5z7Z0KxgQPaKhZaBnU0NaUQE_huhhwaNqVZFO-haSn6jdnwcRHW-Q7giGQMNIVYBrhf1YfUs3D6NfTkbmKdaLbLeUiqnzQ0MboE9zPedNpZrIP8QmlBhwiZral393HSO1PSYNdD7tYBEDOYOrNPwkgyqnhtiwzZokXpxOOh7FzRa7kKYHAZ8nTzpK7z078QRc6x-kOCVZggdxroLyJS13ZzIErC1oiEGpsG9tIvvpbMYNdB8QEFWDeNgaiVP0ZkGoCAbc7wRRKQBdsghSSR1M9mScbJ1wa88fPDkyPHPNqMycUmtAcoBjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0e44244f.mp4?token=r2D7zU7uLyMMed2NoVyuVdxUGnBO8Bk5z7Z0KxgQPaKhZaBnU0NaUQE_huhhwaNqVZFO-haSn6jdnwcRHW-Q7giGQMNIVYBrhf1YfUs3D6NfTkbmKdaLbLeUiqnzQ0MboE9zPedNpZrIP8QmlBhwiZral393HSO1PSYNdD7tYBEDOYOrNPwkgyqnhtiwzZokXpxOOh7FzRa7kKYHAZ8nTzpK7z078QRc6x-kOCVZggdxroLyJS13ZzIErC1oiEGpsG9tIvvpbMYNdB8QEFWDeNgaiVP0ZkGoCAbc7wRRKQBdsghSSR1M9mScbJ1wa88fPDkyPHPNqMycUmtAcoBjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارین ترافیک:
تردد در تنگه هرمز در ۱۶ ژوئیه به کمترین میزان خود در سه هفته اخیر کاهش یافت و تنها هشت عبور تأییدشده به ثبت رسید.
🔴
بیشتر شناورها از مسیر ایرانی عبور کردند، در حالی که
هیچ‌یک از مسیر عمانی استفاده نکردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135098" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6725a38702.mp4?token=OFJZEjrkobPq_EuKx1rrbcOIttqEzgHbMyTU3B8ioMto0wMk_WzSN4vLdR_1z42Eb5xJBlcunuBG-O8ExYJpvDkuowYw75zxu6vDnHSWI74GdVnT5oLsXHaon-tW-zUg-mXygHH7i40b1wBW257Mo-ZB9WMBe7DlZlovTzSqFsBixSUQecviL534dz14P6DhHoVIzFekHzG-GJ3DGs5E0wT-hDX8HzhJgHPrm73ix0IP89iJGZiitaugRdT5xomvPAFwN9N69YYZF2WDFErN0o9CgYAAAE5OI3BBHtIyofjF1szj2oZ4OWiIFLICBNRrAUvFQOFq3J6c2nJznrC3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6725a38702.mp4?token=OFJZEjrkobPq_EuKx1rrbcOIttqEzgHbMyTU3B8ioMto0wMk_WzSN4vLdR_1z42Eb5xJBlcunuBG-O8ExYJpvDkuowYw75zxu6vDnHSWI74GdVnT5oLsXHaon-tW-zUg-mXygHH7i40b1wBW257Mo-ZB9WMBe7DlZlovTzSqFsBixSUQecviL534dz14P6DhHoVIzFekHzG-GJ3DGs5E0wT-hDX8HzhJgHPrm73ix0IP89iJGZiitaugRdT5xomvPAFwN9N69YYZF2WDFErN0o9CgYAAAE5OI3BBHtIyofjF1szj2oZ4OWiIFLICBNRrAUvFQOFq3J6c2nJznrC3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی تاج: قلعه‌نویی در جام ملت‌ها هم سرمربی تیم ملی است
🔴
رئیس فدراسیون فوتبال: AFC به علت شرایط به وجود آمده میزبانی آسیایی را از تیم های ما گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135096" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf3d1e739.mp4?token=LGsqPyA1hnzKQKdm9K6nWrdrK6vT21vLmz_3BeBpxrvHlgilNVbKCW5YsghSpDY-ld35zda0Wxjt-bKqziAcqBC9HyjPrTG2kIm7rmoKqUKJfJ-cwUnMRghlNB2DefmQHMQW40LL8pmgNj5rlzXFij-Df_wKpZWO2RGR-BWSkwVNP4P7Bnku12gMVbX8at4r7FalsmY0HJPn8SJE2r_0ZFoDlh7E1LdG4tS7vD40H6DjxaNJwh6QO2wk-ozAYsHX_-zmDifq-uvUIo0B6ck5hS-euvyjCPu8qBzDEZ3OdErfQRwhoAQACDzOgP4CfunP-3jUH4tWcpCwJ4dVzGFiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf3d1e739.mp4?token=LGsqPyA1hnzKQKdm9K6nWrdrK6vT21vLmz_3BeBpxrvHlgilNVbKCW5YsghSpDY-ld35zda0Wxjt-bKqziAcqBC9HyjPrTG2kIm7rmoKqUKJfJ-cwUnMRghlNB2DefmQHMQW40LL8pmgNj5rlzXFij-Df_wKpZWO2RGR-BWSkwVNP4P7Bnku12gMVbX8at4r7FalsmY0HJPn8SJE2r_0ZFoDlh7E1LdG4tS7vD40H6DjxaNJwh6QO2wk-ozAYsHX_-zmDifq-uvUIo0B6ck5hS-euvyjCPu8qBzDEZ3OdErfQRwhoAQACDzOgP4CfunP-3jUH4tWcpCwJ4dVzGFiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یکی نیست بزنه در گوش این بگه کمتر هذیان بگو!
🔴
صحبت از کدوم اقتدار میکنن؟ فکر میکنین اینا اگه میتونستن ناو بزنن تا الان این کارو نمیکردن؟
🔴
میزان مگه رای مردم نیست؟ صندوق بزارین اگه جرعتش رو دارین بعد ببینین ملت اصلا شما رو قبول دارن یا نه. برادر من خواهر من بفهم اینو، مردم از جمهوری اسلامی عبور کردن.
🤔
خوبه کاپتاگون کف خیابون نیست وگرنه میزان توهم اینا رو نمیشد توضیح داد.</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135095" target="_blank">📅 18:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135093">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
آکسیوس: موج بعدی حملات آمریکا به ایران، شدیدتر خواهد بود و ممکن است تهران و شهرهای دیگر را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135093" target="_blank">📅 18:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135092">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFST2ZJ_zVTaB13nvRdbnpaROjhjhfey_OVexw0tgYU_b2nICGTMSJ2ZP-5G0HBbz01sZ7ZiydIAn93Zouo7-AebFGeLvjhpvCXRe-WpNVnBz2uDuFTEZYjutgcXPYDVnXAFCmJdzR4dW2KqgOE3TQWeKiEXs1qiFyJeyOvcktqPkAA7R2_4hxgOiJAQm-MyMyWi4j03F72ttR6aBcDRMpk0s6Y5HBjnnGwuX_OLt3Bh_3gQZIgkx7H6VKllEB5pe5GSVDNUAjWCEeXNAi1n_YLM3GPM5eWN2KtPs7gsVF1lYFrxusDvspD3s6ZW6UkjmBntnbDE83udaE8EF9WXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۲۴ فرانسه: ایران از حزب‌الله و بقیه نیروهای هم‌پیمانش در منطقه خواسته است تا برای هرگونه تشدید قریب‌الوقوع درگیری‌ها آماده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135092" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135091">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ارتش کویت: چندین نفر از پرسنل نظامی ما در حملات اخیر که «چندین تأسیسات و اردوگاه وابسته به ارتش کویت» را هدف قرار داد، زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135091" target="_blank">📅 18:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135090">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
معاون استاندار بوشهر: یک نفتکش مورد اصابت موشک آمریکایی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135090" target="_blank">📅 18:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135089">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQG8CPX5o5QuPo1cCNpdkbui3bqr0Dz0T63WBDVBKWAHcWF1BUJ7EoXperZjLOyVl9EqN0I3VleVOtWrf_K-wJpMC4bSbbgOLCmbKrNL9lFOL8JBsqtZxLCYhTtayEr4T7A1RfdzpPdfZ9xsZRaJHEl-t0fMrqiZSqt6B-5iVxgM-BpkJF1uGIyV54wVpCNl-EsPQLmmmomJEEIMG3Ai_JC9oJNOmSfmE8Cf_D3XhmRG_IjrJkxlhi1ir4AIqRQaJZN9LH6WY9kIfxymYQAXS17wwsUYsEt52BvGrR8u3h_MQF-ut4FrZJQ7QDoCZ9JjTcLJoVJA5TSy7Ldxi_3PIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هجوم بی سابقه جنگنده ها به منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135089" target="_blank">📅 18:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135088">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قیمت نفت در سایه تشدید درگیری ها در خاورمیانه، به ۸۶.۵۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135088" target="_blank">📅 18:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee03079d69.mp4?token=NDyAFAs9nCNQvnMqt4RiNwJa1M_Q8O8bsgXbu6UWWKZyY_MrcAYbh3ygOKURsstd3wL75BfyEv-MUPYLbk5UciElsfefJPLwqozHeBFudz7TF1bX-kXbAkpDXAYlb4UXU1znt7TpU2hVRa5mZUTEjnbtiKWA2lpXT5lxXr567KPCh-qMKUgw1cYiSSPwsOWJZ9wMbpGL--g0meqJL_AsDzBiPfkoEde_8E25G2V9f0kFNew6LW3S9zJCQvSkhNQ1N97z_0RvGYeeKL_7MiRi41QnDmQM5xfs54rTmSi-WkBVo7v7rKYxAvFia0F7-3fTWw73goWDcJdezSuHc0mhvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee03079d69.mp4?token=NDyAFAs9nCNQvnMqt4RiNwJa1M_Q8O8bsgXbu6UWWKZyY_MrcAYbh3ygOKURsstd3wL75BfyEv-MUPYLbk5UciElsfefJPLwqozHeBFudz7TF1bX-kXbAkpDXAYlb4UXU1znt7TpU2hVRa5mZUTEjnbtiKWA2lpXT5lxXr567KPCh-qMKUgw1cYiSSPwsOWJZ9wMbpGL--g0meqJL_AsDzBiPfkoEde_8E25G2V9f0kFNew6LW3S9zJCQvSkhNQ1N97z_0RvGYeeKL_7MiRi41QnDmQM5xfs54rTmSi-WkBVo7v7rKYxAvFia0F7-3fTWw73goWDcJdezSuHc0mhvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدیو حمله به برج مراقبت دریایی در چابهار رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135087" target="_blank">📅 18:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
در صورت حمله زمینی آمریکا به ایران،
احتمال حمله زمینی ایران به کویت و بحرین نیز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135086" target="_blank">📅 18:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135085">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxwjn2cXJcc8Sj5vqJkwxqh_rpDuTIJkHMmTVUYdxwYr3MLUoWWxZ6x9pPbwWonTEVOQrsyM8Csy8rtrNeSd8gfTs6l8KbgjlBklvcyIC17nI4XGpCrO0VhlF8oQ34jC19PSuPKeKxKZ_jjCJDwsTLS04fiFg6ToihxQ748JrKgw47_wjB6dF0r1oUkliTFMMUQ6YEzwItmmSCnnregTIJTl-Rgyywr-XJtkE09EQ4JjPzz1wbbf2lOsgT7vxDICjS4_qPhZ2VVXcu_FefmmEmhoVnyBs8X78hiREubxln6CYZPFcQCO3FbdJEw3HTjoGjE7YlzUjnzVv1PSqc3Eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی از پاره تنت فقط لباس سربازیش برمی‌گرده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135085" target="_blank">📅 18:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135084">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2b-0YsxWlNV7wAJy2CGeWGH3SS6SVPD4R6-26tNPaLJ3lrgYl6Zobshj_pBy-jITgOLQyzVAPXQMZ0PArO1EpSjc5uLZ2D3p1sF1auXYxF-mCBQtoE65juGT7a_Lp4_UAOal_TVOBZjqx-nAv44us_P-OX9tPP76Ou20nj4nUrvA4tiXYTJVXCnYPu3Idxmqx-OB9JKoEgm8Y9JSenD7Pe2C0ZfkOvRw3HhK54yX9mlvgMP1NzhIIlgWB8vvuhEzOH5_73YaUh-odyfPpcFA2MnQvqUlCfAyGqEptA2c_Y4Q535V-W9gjiKUu8KcMkbd5-GdkAYrct6D9jLhdILXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام یکی از بومی های بندرعباس:
تا الان شش تا پل رو زدن. اگه اون یکی تونل ورودی رو هم بزنن؛ همه حبس میشن و دیگه هیچ راه فرار زمینی وجود نداره.
اگه آمریکا تمام راه های زمینی رو مسدود کنه و منطقه رو هم پرواز ممنوع اعلام کنه حتی به صورت هوایی هم دیگه کسی نمیتونه وارد یا خارج شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135084" target="_blank">📅 18:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135083">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
در پی انتشار اخباری در فضای مجازی مبنی بر ابلاغ دستور به دیتاسنترهای کشور برای آمادگی جهت قطع احتمالی اینترنت، پیگیری‌های سیتنا از چندین مرکز داده نشان می‌دهد که این ادعا صحت ندارد و تاکنون هیچ‌گونه دستور یا ابلاغیه‌ای در این خصوص به این مراکز ارسال نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135083" target="_blank">📅 18:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135082">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ثابتی :حملات شب گذشته امریکا به احتمال زیاد مقدمه حمله زمینی به کشور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135082" target="_blank">📅 18:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135081">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzMUg9nk5cAIBq1p7NnPBOj9GSb0grFuB5eRSe8wE3zV46buNRGbAIKjqzElT5RmOibY-3BQ8KYAsTqrvuFseSnW73soPiEN9BX6Oq0v_GAZ6rCIfh2euyMU6AOpt060AUCJMOk5JL4R_IlMG6ZtSj_22ZbzRym7VmSh4VVCLB8c7O7rfNr3RZ-Bb1geNJwu4NKmRdFGeqOtVRqP7ddaN5-iCQPAefGwabuSj0I7XvcEGlgKjMKtjHXC3KBqu4mkMZWQYL1bDhbLAoLcpI0TytgGrAADylEZ9xNfdzaYe4kevSKr6YGSwt4cxjPOcX2H4BbF_zRQ4-Tx9x2UaLpKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی نیروی دریایی سپاه :آمریکایی‌ها هر لحظه خود را به ساعت صفر عملیات علیه یگان‌های دریایی سنتکام در آب‌های منطقه، نزدیک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135081" target="_blank">📅 18:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135078">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PVIOhvMWoAu4pg-Xja7f46rE7I2Es7omuF2TgigyLrYUvTMkxrnmMBj-fE9dndI7f7KF71aEDZ5DTpJIhjb70FisTjPJ2P8WMmhYRE_sncOeXouTVVbPRB7JUSGDYqe7PRZ1TT84QRT0ZEvGqk-E2oSYfP8BgoTofepQKsLRJu4rIHGT5lbFmlm-SO7_nJqZ8bIdWtVUiLamXQCETFJhgxHnvghQVDViPM5pGRHull0ZUsAlAw5PO3z6zzxdVvvlT95OttgabhhDLNEsL6ImLZaF3WJVVqz_UMnlXx3AY9zfi-iuv4TGxsdLCLRy_e3vzOiO3r0DFfXJNHgl6DPGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mfX79lEtdXyPx5TYJc4U8k6HUm_pZMolXRj9PngyD61fXZCEUpwE-uBiedanC6C7_P7ShHAO25DMlJ_0pkKQLX0lQC9v_ujFLRDQr_5LftotiRmlE0t8V081b1lnbtFabrpxKdwG6lhogLY1esVMh63W-MPJPdvJwRTby50Wwl59jlAlrM4tzKkxkqdMy2MJ9tgmsr1dE2wmsahbPyPy0dVLSmCi0_I715bwAgABxs96KbtQJ4xTEuvD6KKOPXrNVKXivMGopDFHYwzr_ayyfAvQc6P9e3ZlJ8gLRjHw327wb9LMm4PF28R1jdKS50JByVsdUChgR5a25kyY8u82Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dn_FdyVaDgmUM8dWavKotacVAgoM25-G1KN9A7g5d-Y_Ce-77-JrsujzYXVBXRyYk4bxVngv7MFnWNnJ5b6klL2aqwBRiu5jkLR2K36siAd8LMU9KI2g1cMLLcd_7DeH7kWssDsPva459mOyENvxy1bjh40CCnD34C_4DN6nK6skUqkJVQhJ8ylrqUXRdCxxuYV2qoSTnF9iQx4I2_GWF3P5mbIs5XpqdNVulWl_fJw3_MWJ7i3rvS_premax691y7xWBiHQQmpJB3y0B29qsu7fOQO6ylyWzPoCoeN-Y4honp0JRSLKSIA0cHLvUyoheOIwyy1gYaGTW2TdmAtY_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر هوایی از حمله آمریکا به پل‌های بندرخمیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135078" target="_blank">📅 18:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135077">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ارتش: زمان حمله به ناوهای سنتکام آمریکا تو آب‌های منطقه نزدیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135077" target="_blank">📅 18:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135076">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5927edea37.mp4?token=Cn-rtCQ6I5MbpQEUxpZexzr1lwygdigkiD43XTssT-3yG6RUfiv9vPL76W2f3MtNe8Av0f8zUkaFVpv_V_5H8ygstiqnyX7iFu7XIPdaqFhBkzwOnVjxYhHedtktOxFD8zsNlUKszARW1teAUmGqg25IuJP2VW7-xfECI2btaEDwDNn619HkyiTWTqKVqe86V7JZa1jn-KosxN1DhBc3I-ccpaUOM2z0KC7ByY-MZetPJSy6vmEo85cHRREVscGcBx5qlzKxtZ2rKRgf8hK-y7pIe4bUpkoqI_5XmCzZw4VTaOpzugUQQEXVcK7Om25OqGSsHn9pq19JP3ce1AL2Lxp6PqJ9XDVHXKPr1Qi76Axk2TLGOWrVcZJH9qvYeqzc6wz-elfvqGY8U8mPYC-jzo6W0mPnEXfimB0fhRhtZOitsljBOyH3cUsbNrJJ-WSIsAos4sBwxJUsjEkShYeud2wadkw159JUNqvcU4UbHxb952O8TA4Q4EUCtsXt48g1v4LaPJ5dlCSUo1moWekBvcxmwPmGxHmkUFAGzk0YPxJxaNnFj2EH44xYdkpKC5HpDfqZYc89Xif_JB7q9K-fP8WG1ngYVIiTmGHBlFG28s6uc8zBUqqPFFTL-WQOGncDbSgDvZTI1tqfFsFwBbfnlPt0W-4jXkhUxU2q95sQDs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5927edea37.mp4?token=Cn-rtCQ6I5MbpQEUxpZexzr1lwygdigkiD43XTssT-3yG6RUfiv9vPL76W2f3MtNe8Av0f8zUkaFVpv_V_5H8ygstiqnyX7iFu7XIPdaqFhBkzwOnVjxYhHedtktOxFD8zsNlUKszARW1teAUmGqg25IuJP2VW7-xfECI2btaEDwDNn619HkyiTWTqKVqe86V7JZa1jn-KosxN1DhBc3I-ccpaUOM2z0KC7ByY-MZetPJSy6vmEo85cHRREVscGcBx5qlzKxtZ2rKRgf8hK-y7pIe4bUpkoqI_5XmCzZw4VTaOpzugUQQEXVcK7Om25OqGSsHn9pq19JP3ce1AL2Lxp6PqJ9XDVHXKPr1Qi76Axk2TLGOWrVcZJH9qvYeqzc6wz-elfvqGY8U8mPYC-jzo6W0mPnEXfimB0fhRhtZOitsljBOyH3cUsbNrJJ-WSIsAos4sBwxJUsjEkShYeud2wadkw159JUNqvcU4UbHxb952O8TA4Q4EUCtsXt48g1v4LaPJ5dlCSUo1moWekBvcxmwPmGxHmkUFAGzk0YPxJxaNnFj2EH44xYdkpKC5HpDfqZYc89Xif_JB7q9K-fP8WG1ngYVIiTmGHBlFG28s6uc8zBUqqPFFTL-WQOGncDbSgDvZTI1tqfFsFwBbfnlPt0W-4jXkhUxU2q95sQDs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
چیزی که امروز بد داره مخالفین خاندان پهلوی رو میسوزونه همین اقتداریه که حتی توی توهمات خودشون هم ندیدن چه برسه به اینکه بخوان توی تاریخ دنبالش بگردن.
🤔
ننگ بر فتنه 57 که آینده یک ملت رو به تباهی کشوند.</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135076" target="_blank">📅 18:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135075">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a42lAIFRSNVuNuzzJen2bFb9BQ0pe1x4tlavtXLRl-F0SbHl3LJpiwhjQXXUGJy1OhX4yaZaS1_8WEPpYP3zAEmbMpOU51fCp2PYAQ4pbm_giFofHtl5PNDDecIWXSdYJfT4GJ_TiCPZ8ONdl5q40pAMBX4PObslkEw8JiUbN0pfhC1fKvjC9wfIstknvea9EEHsqiNyE9pNWolQrb14f2ZKDQJY_4FqVQaZesR1vGiOSXV9NzRCVtYeY82_A047cNN7mYXlOat7rZPZZ2sUtzsSh4R8czMGdmdcz8nRtgzndrPSWIZVbh2lgqUkw3NpDj1dXbfnnzSbhqjokEqN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: یا با ترامپ و نتانیاهو هستید یا علیه آن‌ها؛ سکوت یعنی همدستی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135075" target="_blank">📅 17:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135074">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سنتکام: اخیراً هیچ‌یک از نیروهای آمریکایی در منطقه کشته یا اسیر نشده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135074" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135073">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/ رویترز: پس از آنکه جنبش حوثی، که با ایران همسو است، دوشنبه یک حمله به عربستان سعودی انجام داد، پاکستان، به ایران هشدار داد که هرگونه حمله به این کشور را به عنوان حمله به خود تلقی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135073" target="_blank">📅 17:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135072">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز: پاکستان در حال مذاکره با کویت برای یک توافق دفاعی گسترده در ازای همکاری در زمینه انرژی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135072" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135071">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
صدر اعظم آلمان : خواستار آتش بس فوری و آغاز مذاکرات در خاورمیانه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135071" target="_blank">📅 17:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه: مسکو با همه طرف‌های درگیر در بحران در خلیج فارس در ارتباط است و از آنها می‌خواهد در سریع‌ترین زمان ممکن آتش‌بس کنند. امنیت وضعیت در غرب آسیا همچنان شکننده است، زیرا تفاهمنامه میان آمریکا و ایران در آستانه فروپاشی قرار دارد.
🔴
رهبران اسرائیل علناً اعلام کرده‌اند که به مفاد این تفاهمنامه پایبند نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135070" target="_blank">📅 17:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135069">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شش فروند اف‌۳۵ از گوام اومدن خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135069" target="_blank">📅 17:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135068">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5b7c49ce.mp4?token=UPzQQ_HVSRi85EmAt8PrsFWrtUPsW2GKCYLNofXRMUDCdS7KkGtiAJ6KnArWbIeMusy7sfG3-iiHUnGi-_AsSAE-hfamhe1cYbXHjy4aw2MvgDqieRTviEfKM14ARx1nTFAY6gKN-FVdm-b94buvJ_EjQBxfvuHZJzwrkV--y9_HxApsuo0rmNLFxn_EQYcjxF6fDgfFMIUh_Rnz1bYffpjeLAzLGSOtN7jQ8X3KExI8qrxylp8h9G86JyFxnAfydcZemzZ7J1xHQC_iw-KNV_KMbhogFAE4VtS7JMnucewetTiVbQpp11T2EVudeKC43UzXmpxEbq7_uD5iTkOreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5b7c49ce.mp4?token=UPzQQ_HVSRi85EmAt8PrsFWrtUPsW2GKCYLNofXRMUDCdS7KkGtiAJ6KnArWbIeMusy7sfG3-iiHUnGi-_AsSAE-hfamhe1cYbXHjy4aw2MvgDqieRTviEfKM14ARx1nTFAY6gKN-FVdm-b94buvJ_EjQBxfvuHZJzwrkV--y9_HxApsuo0rmNLFxn_EQYcjxF6fDgfFMIUh_Rnz1bYffpjeLAzLGSOtN7jQ8X3KExI8qrxylp8h9G86JyFxnAfydcZemzZ7J1xHQC_iw-KNV_KMbhogFAE4VtS7JMnucewetTiVbQpp11T2EVudeKC43UzXmpxEbq7_uD5iTkOreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله اسراییل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135068" target="_blank">📅 17:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135067">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بخشایش اردستانی، عضو کمیسیون امنیت ملی: در صورت حمله زمینی آمریکا، احتمال حمله زمینی ایران به کویت و بحرین نیز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135067" target="_blank">📅 17:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135066">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6c614a1.mp4?token=iLWKvK7JEdu3Tia3-2koxgKp10Yj3Howo0iWHZ6pwN8AmCZO3QnPNOrhWtNSxHYyCItNQ44T7j-H_XALVRQgigxc29hZAIhxoB-H3IUP7eREg-co_Tv8rPkPEiT_BAd2qDlXLB9uM5NoyivycLXQvvP7R4ifMOu-w50TMVYDE57eEk3VasX_UjpMoROnBXuLDobQ4w8eWwSZVF4S18pgbie1AeqcaG-7AsX79YUrzg9msePOg8lNq3qyOyF_lg-LgVgUqiHItEXrDFWnp6X8A4o7pVnbJu-qxw-u5wPhnpvmeYoJvRnb0x1ozot4UjCvMu1VItjwW6ScQcZYy3DKfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6c614a1.mp4?token=iLWKvK7JEdu3Tia3-2koxgKp10Yj3Howo0iWHZ6pwN8AmCZO3QnPNOrhWtNSxHYyCItNQ44T7j-H_XALVRQgigxc29hZAIhxoB-H3IUP7eREg-co_Tv8rPkPEiT_BAd2qDlXLB9uM5NoyivycLXQvvP7R4ifMOu-w50TMVYDE57eEk3VasX_UjpMoROnBXuLDobQ4w8eWwSZVF4S18pgbie1AeqcaG-7AsX79YUrzg9msePOg8lNq3qyOyF_lg-LgVgUqiHItEXrDFWnp6X8A4o7pVnbJu-qxw-u5wPhnpvmeYoJvRnb0x1ozot4UjCvMu1VItjwW6ScQcZYy3DKfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد آمریکایی از نوع لوکاس روی آب‌های ایران شناور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135066" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135065">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5F76Weuzve6q0VnpeaiqaaqMaOhi9-uxNuXfua_E9Qy1yHm2iCEJnUYZVnvrlj52bIBpBLgDi3WW2j8wYdT5Yu_KKHSP8bhLQuEb0g6Y1pVXkMGM4xjJ3aH7sD960jyY4gXqXFew8jjW5xWZ7ta6KMJszqp-w2I1WnfxNbFS8A3IKzQeEHt-_tdp8F3TTxRvXcszEppVvRmlSjCQWce56xaabTZV4MYhiQe7pul8K_Eh3QaybZq_MLKmYhlHM0H7d7btMKLMBSm4w6EhlQVtAOydO3AE0csc4hBYmwAvUWnk4N-QksDe1fOL3kE6tTbiFbsKqgU3wbw8FvpJdkhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
نماینده‌های مجلس فقط لب و دهن هستن و الا میرفتن تو جنوب جلسه میزاشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135065" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mrfkm9Alo3FQDsP0uEH8EUV79hLXFNfpTifa8Rfvsu-TU0H5hOQ2JaWtwkE8AUPkth0lvDYBF1SF1VJmQW5DYjr0tIn8SqGP6CSgSXSz1kPxHrKDCWOP0pPfEuEeIHM9jpG5Wo06D4oVNUkziLCiDbhd54fupkXB2HTGMqUFx3qaEK-o43UCwDlmIFDM8S2DixEUugWIPDHO9gEESczqQZYgNKoXubtn9UjABCUSwrk0hcGkGYOTAM6yEvxeMZ0W_x1USubEd3bx6Ees0azTzYpDIB4WuS-8fs42qeBb-qzjRElnYlAa7nr7nOCjpbNJRooP7Wk09TrjfheDuHP0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788a242c29.mp4?token=FOXGp00LMVGVpwT67yn9kh-bUr_rklN8ZYis3oqT9kZeLdjyf8LLSVwo2BsGsmZ5m14jXPDBe5o35pAcaU15ro7SP4qJ82nM_EZiOpy9zoPgxd3OaDp9AgqTjG9js_-dfMrAhut31SMfOrMGX1EtCxMyjk1mpooI4W92HyKehgyHI789FzLHY6GUGat7pWD6apYgP19PgUKu2mtdms_encRzGNK4ob_nvQSrccptd8uw0cCJetXeAVl4CvDN4XYZSeLDNxKyt45zh7t1uw5V8L6k9j0hIkP_7yzS5Q000bTPgvrHuj2r5RfzPcolHbkUEFFow0MWz4JxMDCEoKMi5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788a242c29.mp4?token=FOXGp00LMVGVpwT67yn9kh-bUr_rklN8ZYis3oqT9kZeLdjyf8LLSVwo2BsGsmZ5m14jXPDBe5o35pAcaU15ro7SP4qJ82nM_EZiOpy9zoPgxd3OaDp9AgqTjG9js_-dfMrAhut31SMfOrMGX1EtCxMyjk1mpooI4W92HyKehgyHI789FzLHY6GUGat7pWD6apYgP19PgUKu2mtdms_encRzGNK4ob_nvQSrccptd8uw0cCJetXeAVl4CvDN4XYZSeLDNxKyt45zh7t1uw5V8L6k9j0hIkP_7yzS5Q000bTPgvrHuj2r5RfzPcolHbkUEFFow0MWz4JxMDCEoKMi5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که یک انبار لجستیک متعلق به شرکت خدمات نفتی آمریکایی هالیبرتون در منطقه صنعتی مینا عبدالله کویت، پس از حمله پهپادهای ایرانی در اوایل امروز، به طور کامل تخریب و آتش گرفته است
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/135063" target="_blank">📅 16:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFU0cfPdBOR9cilt_hywlCgMj2IDfT30igHiHoEj-4fQOj8zOzrT4PZwlRCPfXcKeIPxD63uk7LWS3o1rgBUzAmL1c4zVCE9yTIH5TdtE4AebJtbRSih8Cn8sRsxE09Qc1gpERTtby0YxqM4mfCEPoLsstXGZ8CE_n9TjPs1n7BigsGF1_VJwHJRfExLwRBuf_OV3h4asntsqFqaJ07NdGAzZKENLCKc3QkI0hYq6gvn-AKJuMpFUkz_bmFJgY-3KHCvwB3LfY-3r6heYFeeDygCPDeuM3BlBVcJSu7Zq0RPjf_SF4e3pHCWEl4Ei0NHw1KpY7XS75NQjfnLvXE6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا الان سه مربی تو این دوره از جام جهانی نباختن:
@AloSport</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135062" target="_blank">📅 16:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmS6f63oP4IlbMB1NXiC23YnXt55chwMtkKal_k63nHAeu4ZhSdecejfbsBAEsuXH7upMFeqWL_pKE6f5DRenMWWR535nraQ0JbfHY9rtbMgt-1b1Sjfrlc1_0s6tnaW1JaA7fyMcUlk3QnxxB6waSEmiS5kq3wkHaRxR3KctVVKPdH2eqEE7uVPscOfu-lUUkhrSG2LwX2hBVR1vMEWxBbuQx6SmzJerY_h0UOpUgn-p1VDCmqtDhLhqPMvRim829vXKFh_xO0De6av447-fF1wRamvoWpHEnAHoxaxaxProI5AycnwmzRK36q2qhUGIAit4BtDmbE80TTTrh99yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق اعلام برخی منابع پاکستانی، فیلد مارشال عاصم منیر قصد دارد به تهران و واشنگتن سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/135061" target="_blank">📅 16:27 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
