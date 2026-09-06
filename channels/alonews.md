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
<img src="https://cdn4.telesco.pe/file/E6cKWQOx-yDAbk-v8gzhJlDanBJCqXifrCkbS27-ovHnwsD0DB_3GjzFkgbGGqAHTErkPoq6Ge-GpiReSDNavJJxu2HS5P64PMp-Y71jlRBWXawHpFzRtVnqYtiwNGEsoJ463ongW-X835ElEprmG2s7n7TT4XODT-ZHu5YONY4lrB_uBRNJOFNp1xzAf8WaBhDWHa3cbe2H1cd9W1JoQ_eRk1smpTsOZOi7SEPahnyFeu-i0gbYeuG09vLsiKQ6sCBiYakcuGEnZaYf8G-cpnbUFbhNpyhsreTwvzXbx1m51DshrhgmdJpJv4sGqMmBbZQufdwas8fEmmy7bHr0Gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 21:56:54</div>
<hr>

<div class="tg-post" id="msg-145970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b309972321.mp4?token=bFpdS643P2tZHmiSrJyXJOpXgEPod1qZGV2WjuMhLVEiQQGScaS-YFXdVJaUSkswWCyWyMrb1lDdeybKp5wm-utwI-ekkkACbGzT2T5M2syN14uJ72GX6HrJMRvXQTiMH_zklagAzZJHcAjLSCfeLqhzZXn5gkgU7d31ZOBK-5dwZ3c0e-l1N2UiCc2k-BsFs-hkm6tbh5nRz0wDEzhXHDiUp28FM7Q2YbEp0VAkqZOUeC61_N__X6qN3DIOwOYI3ffc_-rrsTAUPkXGQukRP7SmCNLE-MHix-LtUvapw3-WMLDZ9V_14lxrAaiknKQqgkvo99DlPRvZY5R9zm-Xhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b309972321.mp4?token=bFpdS643P2tZHmiSrJyXJOpXgEPod1qZGV2WjuMhLVEiQQGScaS-YFXdVJaUSkswWCyWyMrb1lDdeybKp5wm-utwI-ekkkACbGzT2T5M2syN14uJ72GX6HrJMRvXQTiMH_zklagAzZJHcAjLSCfeLqhzZXn5gkgU7d31ZOBK-5dwZ3c0e-l1N2UiCc2k-BsFs-hkm6tbh5nRz0wDEzhXHDiUp28FM7Q2YbEp0VAkqZOUeC61_N__X6qN3DIOwOYI3ffc_-rrsTAUPkXGQukRP7SmCNLE-MHix-LtUvapw3-WMLDZ9V_14lxrAaiknKQqgkvo99DlPRvZY5R9zm-Xhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای هشدار زودهنگام آمریکایی بر فراز پایگاه هوایی موفق السلطي آمریکا در اردن به پرواز درآمد؛ در پی نگرانی از حملات احتمالی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/145970" target="_blank">📅 21:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145969">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
یه سری شایعه شده بنزین ۱۰۰ هزارتومن قراره بشه… ولی تکذیب شد فوری
⛔️
✋
معلومه با این ناترازی شدید انرژی بنزین نرخ بعدیشم بیاد… یک سال اینده بخش انرژی خوب نیست…دلارم میتونه دوباره بده بالا تا اسفند
‼️
@ramezanii_fx</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/alonews/145969" target="_blank">📅 21:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145968">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dlvb8daXPP1CEvRTnuW5TZey6QUAn0Bv7mLjaDHDya7OPs6IOMnRCEbtqyasmh-ZXt4T3SOIWulHLLbhb5ILkM8Fji8Gh0zWzN124MZVuE_FrIrKzBMAV2R9i915RDmps2WfEkUhLkHDT_zqBRZeP_rmsML4-ht08AaRtLrlaeCBt529yMrdtVNWOtMFhmLcfKOpCg84iAegvXNGroDYf4D9AKjGmvaT_GNGUyf1-d1H24qz0q2v2pMDx7lnXnsYbEAYo-DZOVuVwh_ty2wYVWjA1jjnZY_5Js0GoaH5YOjhRGRKPNq0M1TNckzYM36dqbjzRqMfLvVX7J4TpZ_ZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای آمریکایی وارد شهر جدّه در عربستان سعودی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/145968" target="_blank">📅 21:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145967">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvFwdtcOznSZrapX5DUCjQAB-tNFzP236nfRy3IPRryUvGppG45pjbP6b3pMdeMvfoPacBz4DyGe3mGdCopEAxfAtzgOt7TuyUaXeNlR3boNLvOjsm4HvXQ408FaRAGXUWBQ6DA0j_cLbx6cZ73OxPGiPdE-PegxDNAJnChknTOd_wswi4S6q8wPTNzV55noB73W8WPtFNyKxhPkNF_JP7VawZ02q_ureIOMRkJxrV-xDllQFT74S-w6_tjOCht44XxfQ52rpgvgnnhPx7W0pWXbJkO0yfLEN06jnZe9FcGgh6VBetaGxQ5XA6-T_EA7eeDdrKBCwNMC3PMOQZ0gaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: ماه متعلق به ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145967" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145966">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldwMKTtCHWoOrq324mCNjcjPQI2zC9_56IOvdhgRV59plhgO695KNxFxSKhS9QB6MNKNtZD75Ux72t9GPHB9gli6JJ7EWVmphuk2IMRRJNDC1yilekoKpE3u4u_h-ubj557arSWXyOsoqbOE-ZqpYu7vC2bMXcINf6Blw4jeB_pf8QhDuM2YbgthLp9LKLQKLwwpMc2NVVOJf_V0kjZ9_UxDBVLrfoB5-oTIGtNlSIHExTc2jb8mpBr1C3N044AnDT8ahKnXneCpwCFtkg73HtYPQRPzIImiQKOHyNv9T3mwT9uQtZLFp2pmYkUgKPCy6BXbTv0Tpvb9wRtbkXqfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social!
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/145966" target="_blank">📅 21:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145965">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud0Vf4wBP_mmK-OPIuU3TIwRxq3qFleGfxX90ucezvkagPSREFmrmoN-WaQXptvTg23HPSm2bM30hZu15uByKc68HZZiM7CTc6DnfUeN-HatlZp_WdlkicwxREE6Io0VoD-tbD_5v8SRAicQ4io3txwVPyL-Axlq9Vt7fAanTkeq6wUDs4wB7TKZtpanWecUX7L21L8jKlNn1jPZjisusc9oUJmDAkuyIYbdkUxA4b_UtmvnJdsZQLwGo4uC18PMhOVthB3yIfEQa0tVZ4dTPIiPMyXccvjyLUwLuMUA-gsRSNIx_WIsv957-BxikR0M_pQhVMPPp-1XTAzfy4Oa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  نقشه ای را منتشر کرد که در آن ایالت نیومکزیکو با عنوان "آمریکای جدید" مشخص شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145965" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145964">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJvruP8EiAYBr4sAalqAp1DzsoNvNuX77fh0RPW-Sh55LbQ8UJna2R8_JhO2M9222aEirH0pfP9Y8yOZM_Z5XN_zjfugZCRcHceASpwS4JGgXwjPzFlETz8xH4NbGg7kenQJs2HKbZmzXLZ8RHCK9nR9KjqZPVt34PrXT6qRm4wVLia2oikbrE3Fi3qRF4l0j4FTPhgzJy5OaRbiGwApa42lLFk9sQml0k50Yh7x4SGayMKnJ5Yo2GzEDfesGP7AykA36fG90CnzgVIfdtazexiA4A8tTvIviuxRP4EkSZO3jwwseGFPXYNz7YqqJQVBwbY8d9ZIuI_Q5GAHQCdqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، عکسی را که با استفاده از هوش مصنوعی تولید شده بود، منتشر کرد که در آن او و جورج واشنگتن سوار بر اسب دیده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145964" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145963">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN-eecv20fBuCwz5ZKc2-1EbxIgg6WrHpu4zr9g9yBO4MR_bE6kCrTjjJ2zGiifFPqwy38bTn4bFNpoQ9_d9gt4h1SUYqvP1QD4quPjhHVUDzkAyJJnJvIk46sh0yqgzRwKNE-1_4uOHtt8rLac3e-OHqj9Zr6Tz6ecy2yhZGPUfqN5-YwfH5vkUatTYldYhvMVcL-hSAOeyhK9YAMwMal5RdyuDBWVvWrKAGzY69oDViBEj-A42Sk3wiYGBIfqKdS3Lwup2s-c1eybe77qi55HMfk3pOidLslQNH82aOHNiydLfijXy5AvOSKM26klppsYgB6N3FpYePrPqnEke2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: رئیس‌جمهور واشنگتن از رئیس‌جمهور ترامپ دیدار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145963" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145962">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIivn2QldNm4hLwRkl6haoumXfM-fHz0a9ylLQIiuKQFSp9ohqwtBUxj1fZcuxiApggg5Ci6ooewYr7KeKcOeQnm8fpVL462dViyfREWSRIaQBfewZBO2TYTN2HcLPh0YchJlXMXLfj2Vjuft2pIE0k64mvsopDVMRZ5T9CF3ZHewwTGoJt5SJyM2r0ZT5T8nh7YFj1Rb7jejPwdF7RJ3BqDe08fWF-0l6bJT7l4oqnFV0jIrVLfEJazrZFsh2WGopACkDDX5OnGmlBErlfj5jha8QPandigtHNgzB_lTkxoSkm_Q192g6MOrIOVP5ePI6hjUrLnBYbn_T2MEvZ7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت وضعیت ارزش دلار کانادا در برابر دلار آمریکا که به گفته او سال‌ها ادامه داشته، «غیرقابل قبول» است.
🔴
ترامپ افزود: سال‌ها همین‌طور بوده، اما دیگر این‌طور نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145962" target="_blank">📅 21:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145961">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1197cb9.mp4?token=aYrrBJQg8qGrjFNdyk5bxWXDDzQyXMlbgmbPFDgLPxVM0-MgPTYjA-Xx7HtgqnKs_UxAMTNDJayiXk3g3K--1hOH9uJ_lKxdSeyBD_7yEDTOquHg1vzFot5BI1PXi1JMmqCDlu3xJ8WDy53GefF-flswDNf-sCjFTU2yeU_gkF-zcSpHa3NkRAsR9NamqcQCWnlCviFhpFio-nxjjP_4sNLg8zDOEuwm1xoF9G18Mcu6JY1Qpf1jMkakiwid3vD-fFZw-0Oz8mJ-RyjY3vDyGztkxXBc40LMs2BdlBnE8sKeVKRRqUrUb1xaPI0zh5ptrAc9LW80lxIG6oQxh4FM8ZXUgftW-JTvBFYOKZx4T1T5ymFIvmw3rQHF9gX7YsBqF29PQlZcpSaQfrVPTmGI2sevJfoxne2GeAe0qeFS_y_MrNTPkh_UeEZs1kn2HaGdBcByQiRrkydYg2zj6A3VR_v2hPzEDXB1BfpzR2z8dgJsDfxP6C-2-tT169UrqT9vd2ibvEO775kYCnefIoGuSbJ6za6V8qORq6lkwHMNxOSfluTAh2AHAdvTZWjsMqLt9XiBJ5sIEKBNtpj_KdSAIxosnZnBZO-Qb3JvxEqL0ahStWazUZWsRR4K8__T5UGLESMWL4XHfHMnwLG29EMbgjWYYR7G4FZX3-pXABa215g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1197cb9.mp4?token=aYrrBJQg8qGrjFNdyk5bxWXDDzQyXMlbgmbPFDgLPxVM0-MgPTYjA-Xx7HtgqnKs_UxAMTNDJayiXk3g3K--1hOH9uJ_lKxdSeyBD_7yEDTOquHg1vzFot5BI1PXi1JMmqCDlu3xJ8WDy53GefF-flswDNf-sCjFTU2yeU_gkF-zcSpHa3NkRAsR9NamqcQCWnlCviFhpFio-nxjjP_4sNLg8zDOEuwm1xoF9G18Mcu6JY1Qpf1jMkakiwid3vD-fFZw-0Oz8mJ-RyjY3vDyGztkxXBc40LMs2BdlBnE8sKeVKRRqUrUb1xaPI0zh5ptrAc9LW80lxIG6oQxh4FM8ZXUgftW-JTvBFYOKZx4T1T5ymFIvmw3rQHF9gX7YsBqF29PQlZcpSaQfrVPTmGI2sevJfoxne2GeAe0qeFS_y_MrNTPkh_UeEZs1kn2HaGdBcByQiRrkydYg2zj6A3VR_v2hPzEDXB1BfpzR2z8dgJsDfxP6C-2-tT169UrqT9vd2ibvEO775kYCnefIoGuSbJ6za6V8qORq6lkwHMNxOSfluTAh2AHAdvTZWjsMqLt9XiBJ5sIEKBNtpj_KdSAIxosnZnBZO-Qb3JvxEqL0ahStWazUZWsRR4K8__T5UGLESMWL4XHfHMnwLG29EMbgjWYYR7G4FZX3-pXABa215g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری و رسمی/سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145961" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccQxygAv0aPSWLGjbrHXNi3EH_ScheiqqSHCKNzNLF-SAE4tT7Ha_ifGSpADCE-rOmfSIMOxLDh-KDIouBsHMoWP8SHGGzWKqGdJmXX1wy1b97qm5zN5lrb43wn1u_ontVz6hxEPKLzNbFDA0qFu7L37f9ikRm3za1X8_ciPLr65s7oVi450ZWmdZczVrMnj9aCIWSlb_qROdHLckLntSX5WU83CSL9vxGt-N-YTS2jyY2Z8yop-xhev5v2CxAPMp9RpEYtKV2T078cTlCDxCbW_Tn6a1-TPWXttKLvn9fvGy-RpjTe0p-GaFVZ8a5vqB-CXyCJOveY58wgfa5ZPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfrhMyRR2TpoNcFA2pMxTNtZnL0JOVWc1TZ9oZzf6HEHMpytN_wzMsbZe-hKBrO4hHa_OU6bo531SDQ6q5twJVBRWI5jE6yxbHlcpw6tjU1hxmGIkgQ5S5PER_tuXzBVj7HbnId7IJUnVjmJ_en4Qksn-ehTYxhSvQPiHfMQ7A3voCCVY_ZqCBPOP6xtbY2yTnR6uKViPPrb_vrBRzxPcsRdYlRv4sCNUytMguvoN9wXRONyz9SMqg8nofiyLaLxBpNpHqUT4aOE50B0ZbZdityKuAIesu5EN6JQSzkpQCNO2CYJLhRmTOdwtFYmDD-_yqLjcpZq7y6yZgufjIkYbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای P-8A متعلق به ایالات متحده آمریکا و سه فروند هواپیمای KC-135 سوخت‌رسان شناسایی شدند که در نزدیکی خلیج فارس در حال پرواز هستند. این هواپیماها از پایگاه‌های نظامی آمریکا در بحرین، قطر و امارات متحده عربی به پرواز درآمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/145959" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / کان نیوز: ارتش اسرائیل قصد دارد کوه "علی الطاهر" را به کل منفجر کند و منتظر تایید از مقامات سیاسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/145958" target="_blank">📅 21:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر بهداشت: کمبود داروهای ما از قبل جنگ کمتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/145957" target="_blank">📅 21:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de2185aae.mp4?token=HX-I9XdUvVtPDUVjgtNWjV4GFUmWXWjl1k_DLg8g-NuE4P_GuMKzaue8SXCZ_Vjs7_oRx5c8JkCNFcHvJ79GXgfX2WujkSz77I7_xhok-_QYPFJDqeB1Glfso7JgDvYt2WuYXwY5IvLA1aUcvg2fZEUOErVaTqu-Xtzzve2A2FaPdxCAcrg1VZbalrP6Wjd42gFtyhN5WFI73LMq7CHOUgYBy02-omxR_Z9SlhoxQ_ZB7B5e_263XBM5SlxazTPJweIIazKTPLAvnfsxpvJ5kcqXAtSloytWMMYQ62-QwCx8QIhuOkpPTAsWUu0SDfQylX6GVniiueSsCCG5xsY3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de2185aae.mp4?token=HX-I9XdUvVtPDUVjgtNWjV4GFUmWXWjl1k_DLg8g-NuE4P_GuMKzaue8SXCZ_Vjs7_oRx5c8JkCNFcHvJ79GXgfX2WujkSz77I7_xhok-_QYPFJDqeB1Glfso7JgDvYt2WuYXwY5IvLA1aUcvg2fZEUOErVaTqu-Xtzzve2A2FaPdxCAcrg1VZbalrP6Wjd42gFtyhN5WFI73LMq7CHOUgYBy02-omxR_Z9SlhoxQ_ZB7B5e_263XBM5SlxazTPJweIIazKTPLAvnfsxpvJ5kcqXAtSloytWMMYQ62-QwCx8QIhuOkpPTAsWUu0SDfQylX6GVniiueSsCCG5xsY3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جارد کوشنر در کی‌یف: در این دنیا، یا دوستی ابدی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145956" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8283fd5109.mp4?token=US9P4tyj9w3MJjAEsImQC5K-RP9zimAZLPzpNaAs_FR2Lna9FhQ7qB3X3KpgFZ6zPWKkwKamF-EWZaJ6UniHUUrijHghFtU7GtX-KcB9Cjf0JBiJTHvbWuvwbM274HRaegJGl0jbhfcgvwd_fm4XwcjrLn9F4g_XOmyeR5hENZW0-ylcsaO8Q9dBj2SvOcZz-_L7KrMvlfhpVXt80sMb1dqxvjfPyC0rXBSNSz7Ukil3qFHxs9VERbewED8EUlh-TnU6lnEPJvHBLW40SzTWL8ih7_YmKfZN-S--rN7MAFj5h3xn7kXu1PwtOJ5FbnzBl0ur9zEj9pObjhvFkIhliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8283fd5109.mp4?token=US9P4tyj9w3MJjAEsImQC5K-RP9zimAZLPzpNaAs_FR2Lna9FhQ7qB3X3KpgFZ6zPWKkwKamF-EWZaJ6UniHUUrijHghFtU7GtX-KcB9Cjf0JBiJTHvbWuvwbM274HRaegJGl0jbhfcgvwd_fm4XwcjrLn9F4g_XOmyeR5hENZW0-ylcsaO8Q9dBj2SvOcZz-_L7KrMvlfhpVXt80sMb1dqxvjfPyC0rXBSNSz7Ukil3qFHxs9VERbewED8EUlh-TnU6lnEPJvHBLW40SzTWL8ih7_YmKfZN-S--rN7MAFj5h3xn7kXu1PwtOJ5FbnzBl0ur9zEj9pObjhvFkIhliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوشنر: آمریکا و اسرائیل درباره آینده غزه توافق دارند
🔴
جرد کوشنر، داماد و مشاور دونالد ترامپ، گفت: آمریکا و اسرائیل درباره وضعیت نهایی موردنظر برای غزه با یکدیگر توافق دارند.
🔴
او در عین حال با اشاره به شرایط سیاسی داخلی اسرائیل گفت: برگزاری انتخابات در این کشور باعث می‌شود تصمیم‌گیری‌های اسرائیل در برخی موارد «غیرمنطقی» باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145955" target="_blank">📅 20:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802abf04ac.mp4?token=rFsiKwPiq81HxU_4LFyjWMvXIPuXqVXW5cJIF-ipSmrjq5zzv4-h8xVZ0-OdZoUIrpqtkYsSadAOZvSAp0NdHSLy7QKk9wZPe4BhWQeqidlq4ya5HXSpf563idOBWnL6xBgGfa48oFMsgKoWSCDMQL7CEe-vmW82esJdv6ZfgkZ32YZt0jYm-u7YeJEX1daGtDiFyqChyW0DOJJliZKrvc_1tekPYyobiXxWAclO7zDGdHyN06eHKXF-Fpm9KeRR5YcM5K9ML5pBQymzJtiLRNY1bus6SmoIc2SZtUiMKKFs0AwPqnFSqH4dVOfHrdLhpsfvGWBD87P-HUb-Xd6ADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802abf04ac.mp4?token=rFsiKwPiq81HxU_4LFyjWMvXIPuXqVXW5cJIF-ipSmrjq5zzv4-h8xVZ0-OdZoUIrpqtkYsSadAOZvSAp0NdHSLy7QKk9wZPe4BhWQeqidlq4ya5HXSpf563idOBWnL6xBgGfa48oFMsgKoWSCDMQL7CEe-vmW82esJdv6ZfgkZ32YZt0jYm-u7YeJEX1daGtDiFyqChyW0DOJJliZKrvc_1tekPYyobiXxWAclO7zDGdHyN06eHKXF-Fpm9KeRR5YcM5K9ML5pBQymzJtiLRNY1bus6SmoIc2SZtUiMKKFs0AwPqnFSqH4dVOfHrdLhpsfvGWBD87P-HUb-Xd6ADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145953" target="_blank">📅 20:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcCWqwfRsMhPrNpcNa8WiQO_IuIQsAH5SkWA6eIu8qw97hulm9Sc9DpbvBgCwvUf8GAI1WXDCpa-nMGzYoqIIw14h9X3rMxmNelqp5jlTSFHCIhb7mmlZRhJJ2skCPMkSpBakS3Z-0fGowEokN4liPYvWgCQSt9Cg8MqNH0DUenqLgHFV2jQupAvX9_6EBOVCRuB4kNNi6cRJkFwGQ_DY3W5gxrlVdq5S5oRpv2ss82topSLc1gbQHtD6yIlKW0msWhJ7SvcLxlOqGpK_pUO5SRNsx10dt87B719xvW4t--4b06Vz-PqDZAoIthq3GNg9aIamsrMlOjxKlFNb2gXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PE5Ut2V0tVBr21-lvzTd4_D8PtqXaZd56cZ437D7jB1Gp5xq-1nVpUkirH7ZeCiExhJ0L1YnDsYUO6MHqbueLc52NKv5za0EWK1thH_vGIk-frrzTubxVpV1wGmQMEBn8JE-WRfRQi3z7qGmksEnx5ZFB9Ci86KP9BoYrD23Fd96IX78DIv-63dCQQPN4OIbrbn3P6HB36IFL5G7r8CWfLGxAJiluIFWY2f3Iqf0rGLpBa8GrFzCmUR_bHnzizyOedU0kzC1yovoicfDyL3dJKIUIkkmyhCd2loKW99h85kl3x-kL3P79LHjyJ_FWiYd64lehqQmpO0v0wqgf5Lm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWNB6v0R2sQfzUUqy5s_8WTwFdNLZHJAbB7aW_azrNYY2-_hx3y_U7_iqVRmmydTXz7grQyDrZ_kRxXGGX3_ifQvmEFms_DAVA7ENBHsOl1gp-dVraxtKJqIIrgUx5wEpyS4AYykecmW7k4R8izCGg4w9dslOsv5hAoo5tfXA3mDzWf7e2nGUe9Br3fpjmNWpYVlk6PIKaE7Pzm9877NDaK894v65a2kDgd29YZhBqopQSMUzIM0tQwvrIXKtfuskrcxMp6iHO5rWNeMCi-0Rtnc6lAlszXYDV4GtdqkivXk38PPuunq0rG06tsSL9q6p4xNyk7L1X_7ItI6MMUjvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ca623840.mp4?token=eIatAyo7ZDXcGJzO6LwiHwgFd_M0wqupy9csSaMIaVqTwt9dfhrKUPHxfevw9fpluoSIMOrzBcyDwqpgfSrVoNHftBxpc_R8_4NEC-gOW71St0mPMybvLhpBYBYsqQxSlr3_r114GX2EfyuYHx1AhZwc4PpLMZ8CcFCUris5bPumAffp8jjJ4b4mADw-mMROIyReKR39a3uFY9Em3kPndFuBDxq1RYtfAflicv109yJh3Xmr6gJG2ZK9b8P0iPPH26_I0e3K0i16Q-rc6WYE62WtYaqLJmMYnFzKTFviGRTnuPNpSkGx7nvk6bJLA_D1tyHAv6KWh-4UuFYEVPIDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ca623840.mp4?token=eIatAyo7ZDXcGJzO6LwiHwgFd_M0wqupy9csSaMIaVqTwt9dfhrKUPHxfevw9fpluoSIMOrzBcyDwqpgfSrVoNHftBxpc_R8_4NEC-gOW71St0mPMybvLhpBYBYsqQxSlr3_r114GX2EfyuYHx1AhZwc4PpLMZ8CcFCUris5bPumAffp8jjJ4b4mADw-mMROIyReKR39a3uFY9Em3kPndFuBDxq1RYtfAflicv109yJh3Xmr6gJG2ZK9b8P0iPPH26_I0e3K0i16Q-rc6WYE62WtYaqLJmMYnFzKTFviGRTnuPNpSkGx7nvk6bJLA_D1tyHAv6KWh-4UuFYEVPIDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145949" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7befbd48f.mp4?token=J95X4VJCr4quRNr7HN0-_EuD9_44wUY4Zn-3aMDnGNLT0eZErxdPPFhTO53qTSe3E-VC4uz2p-hh9RmFQa-hH2uJ11kEzroN9tIG7gBHzf4CxKOqFxu1i5o3GOfRes9lTPZhqTyP3DPE2nVsG6z3Tk4rlNdPBq4CKfq7A0hJflWEr3ko61mlza8EeoKvPRVOJGogl-u_XMvHBo92uXabkd2iavI9puwvaBHh7xU9uvOWSQGr0M1CqD75GMroIwVqkImub8PBe0seC6PMqe8KdH-v9JUiJoSwr9mvHRavZeiQh4qiJJUoHTJ4gDwTXoTpxbnD4PGTnCmCh8YCI9P4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7befbd48f.mp4?token=J95X4VJCr4quRNr7HN0-_EuD9_44wUY4Zn-3aMDnGNLT0eZErxdPPFhTO53qTSe3E-VC4uz2p-hh9RmFQa-hH2uJ11kEzroN9tIG7gBHzf4CxKOqFxu1i5o3GOfRes9lTPZhqTyP3DPE2nVsG6z3Tk4rlNdPBq4CKfq7A0hJflWEr3ko61mlza8EeoKvPRVOJGogl-u_XMvHBo92uXabkd2iavI9puwvaBHh7xU9uvOWSQGr0M1CqD75GMroIwVqkImub8PBe0seC6PMqe8KdH-v9JUiJoSwr9mvHRavZeiQh4qiJJUoHTJ4gDwTXoTpxbnD4PGTnCmCh8YCI9P4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از وقوع آتش‌سوزی در پالایشگاه ینبع عربستان
🔴
تصاویر ماهواره‌ای «سنتینل-۲ال» یک محدوده سوخته جدید را در اطراف یکی از مخازن ذخیره‌سازی نفت خام در تأسیسات پالایشگاه ینبع متعلق به شرکت آرامکوی عربستان نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145948" target="_blank">📅 20:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: ترامپ ممکن است به توافق هسته‌ای با ایران دست پیدا نکند و در عوض سیاستی را دنبال کند که هدف آن نابود کردن توانایی تهران برای دستیابی به سلاح هسته‌ای در آینده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145947" target="_blank">📅 20:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زلنسکی: جنگ با روسیه احتمالاً تا زمستان آینده ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/145946" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بهنام صمدی خبرنگار بورسی: از امشب نرخ سوم بنزین ۱۰ هزار تومان خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/145945" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کوشنر: رئیس جمهور ترامپ می‌خواهد چارچوبی برای دستیابی به صلحی جامع و پایدار ایجاد کند، نه فقط پایان دادن به جنگ فعلی در اوکراین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145944" target="_blank">📅 20:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ویتکوف: ما برای از سرگیری روند مذاکرات به کیف آمدیم و از دستاوردهایمان احساس خوبی داریم و مشتاقانه منتظر دستاوردهای بیشتر هستیم.
🔴
روسیه و اوکراین باید برای پایان دادن به جنگ امتیازاتی بدهند
🔴
ماموریت من و کوشنر این است که طرف‌های روسی و اوکراینی را گرد هم آوریم و شکاف‌ها را کم کنیم تا به یک تصمیم مشترک برسیم که به جنگ پایان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145943" target="_blank">📅 20:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145942">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0iguN-FFWOjtMxNmK38fb5OW7XJcRKDpBSOTSyPMjgoyiWBphwM-AEFXiHjk1AgghlNsUNY3XFzdP1k8jwzgYR4ZLJliCU67_6YY87_k3OdHCfAWFCaWkW84AVVvvY0ezKq5KghRzLmLRu9PPXg0_PNNSk5xinf_lkbB6NW2MufCYT8hOGB4xyIwtOiYEVDpHf3fwXIgw5WSUTheYgmvW7KTdfOAzY2Jqh6FV_WlLKMtboL4CxPr3H32jfJsSBK6XL-NvuIII8lk9-5b2XCdUuougS342rUq49R9_tVS3dnXOx9g10I9C6IvCt_ItCSBwg9acAFeCAiPLZGxrm5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: افزایش قیمت بنزین اثری بر روی صرفه‌جویی ندارد
🔴
افزایش نرخِ سوم‌ بنزین به «۹۷۵۰ تومان» اگرچه شوکِ ارقامِ دیگر را ندارد ولی چندان هم در کاهش مصرف سوخت اثر خاصی نخواهد گذاشت.
🔴
به دلیل پاره‌ای مسائل در کشور، نیاز به کنترل مصرف سوخت هستیم که این نرخ از پسِ آن بر نخواهد آمد، چون مردم از دیگر مخارج خود خواهند زد و به سبدِ هزینه‌ی بنزین اضافه خواهند کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145942" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145941">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
در جلسه اخیر ستاد ویژه ساماندهی و راهبری فضای مجازی، و به دستور ریس جمهور ضمن لغو ممنوعیت اطلاع رسانی رسمی دستگاه های دولتی در پیام رسان های غیر بومی، رفع فیلتر پلتفرم اینستاگرام به صورت مرحله ای، از تاریخ ۱۶ شهریور، به ازای دسترسی ۶۰ درصد از سیم کارت های موجود شروع و تا پایان شهریور ماه تکمیل خواهد شد.
🔴
عباس پازوکی معاون ارتباطات دفتر معاون اول رئیس جمهور، همچنین از دسترسی آزاد به پیام رسان تلگرام در آینده ای نزدیک خبر داد.
🔴
در همین رابطه، پازوکی عنوان داشته است ریس شورای عالی مجازی و در ادامه سیاست بازگشایی پلتفرم های خارجی، به زودی تغییر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145941" target="_blank">📅 19:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145940">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از افراد مطلع از مذاکرات در کی‌یف: ویتکاف و کوشنر نسخه‌های به‌روزشده‌ای از اسناد قبلی را با خود آورده‌اند؛ اسنادی که با توجه به شرایط تغییرکرده از زمان متوقف شدن مذاکرات صلح با ایران مورد بازنگری قرار گرفته‌اند
🔴
در مذاکرات توافق کلی وجود داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145940" target="_blank">📅 19:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145939">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر امرژی آمریکا، کریس رایت: ما همیشه برای توافق آماده‌ایم. هدف ترامپ همیشه این است که به راه‌حلی مذاکره‌ شده دست یابد و جز در صورت ضرورت مطلق، از راه‌حل نظامی استفاده نکند.
🔴
رایت ادعا کرد که بزرگترین نقش نیروهای نظامی آمریکا متوقف کردن صادرات نفت خام یا محصولات مرتبط با نفت و گاز ی ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/145939" target="_blank">📅 19:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145938">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1a155b4e.mp4?token=v2bFZHlW0VFWyTK2U2fuCvv1czbS5_KmVy2Hh5dSiviEQBQoTu3D0rENt1UAHoKrj4orlhiGCaa33hweU4iYK06wXjJwvKE4RcyO-LHN-OjwesvgAlJ66lLRa_8FMUxvPGIl-L6l37PGCTaVqCbH1F-Dc5cYSBIH9n5wPYbLeBLtSWArJ6k5dg7rgVpSQE4J9bQc8MkKOJVtUD0uX_Br6vwFhalJ7bN3GkGvHT-VWTEV2t_7GuSf2heKLZonlHpJJzGBTagprpPDdJdJozYTCApMiK2eZbusSTQUbRji_Bg5KaWf_YEcA4N-VTjpXErVhVrQ1O1p1M9hEgYQj82-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1a155b4e.mp4?token=v2bFZHlW0VFWyTK2U2fuCvv1czbS5_KmVy2Hh5dSiviEQBQoTu3D0rENt1UAHoKrj4orlhiGCaa33hweU4iYK06wXjJwvKE4RcyO-LHN-OjwesvgAlJ66lLRa_8FMUxvPGIl-L6l37PGCTaVqCbH1F-Dc5cYSBIH9n5wPYbLeBLtSWArJ6k5dg7rgVpSQE4J9bQc8MkKOJVtUD0uX_Br6vwFhalJ7bN3GkGvHT-VWTEV2t_7GuSf2heKLZonlHpJJzGBTagprpPDdJdJozYTCApMiK2eZbusSTQUbRji_Bg5KaWf_YEcA4N-VTjpXErVhVrQ1O1p1M9hEgYQj82-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره ایران: آنها به ما حمله نمی‌کنند.
🔴
ایران از این کار اجتناب می‌کند و می‌داند چرا: زیرا اگر آنها مرتکب این اشتباه شوند و به ما حمله کنند، ضربه‌ای را متحمل خواهند شد که حتی تصورش را هم نمی‌توانند بکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145938" target="_blank">📅 19:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145937">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1caed26faf.mp4?token=ofkQmIcFJQ5XZbu84jogrK7xnH8WErskUIIHCiGScOg9U7eJtaMjRDkKX0PcbWkXA5clpHP6ID8E0EnNTteyJLd0xqg2ebk1hlRHLqrAh2qVCVuySE4MObVNziJYaj-TyA4SASkHiTaKBzlLY4muba-hW-tl9L0pOnGZ9P5OHzVemXY0-TIAd1aRokKMzqYAW2iaK1PQNxwpBnlQMorCcioNNGbosbMq24mlTiuuDSi2x9x7mWpSrAFl8ZnbPIKEoN0SqbL8slA3uvHN5vS9EjfA_gVBqI0u6FvOOZRGJeRttjWB6g-yrGAAn0fCfhbnQcIsQjwIAFP7h_eQel1qLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1caed26faf.mp4?token=ofkQmIcFJQ5XZbu84jogrK7xnH8WErskUIIHCiGScOg9U7eJtaMjRDkKX0PcbWkXA5clpHP6ID8E0EnNTteyJLd0xqg2ebk1hlRHLqrAh2qVCVuySE4MObVNziJYaj-TyA4SASkHiTaKBzlLY4muba-hW-tl9L0pOnGZ9P5OHzVemXY0-TIAd1aRokKMzqYAW2iaK1PQNxwpBnlQMorCcioNNGbosbMq24mlTiuuDSi2x9x7mWpSrAFl8ZnbPIKEoN0SqbL8slA3uvHN5vS9EjfA_gVBqI0u6FvOOZRGJeRttjWB6g-yrGAAn0fCfhbnQcIsQjwIAFP7h_eQel1qLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: هنوز کارهای بیشتری برای انجام دادن باقی مانده است.
🔴
این رژیم در ایران — پایان آن نزدیک است.
🔴
آن ضعیف است، برای بقای خود می‌جنگد، لنگان‌لنگان حرکت می‌کند و هنوز مأموریتی برای تکمیل باقی مانده که ما عزم جزم بر انجام آن داریم.
🔴
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145937" target="_blank">📅 19:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145936">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f79f2049c.mp4?token=qHx9LUnpHBhE1mrVb1Kt00BE3ww3ufZKAkaj_P0LK-_LYl96nALqWSFtSI0i2B1PEmNgkV8haunSFeKYFnDx1A0IeDeAUD1SvDSUW_uFGiVnQ4qxe9eHuWwlv6LmsiFfdXTvQpZgdb6JAalpExk2KVbCf44AMj33cyDN2igtaWgUqz8ySKPXyytOJMUs14R2c7CaiE5y5gTb8YXQzxwPozlvq9VbC2fWZWMho2zjWcU6NlMu-WjtzisAvfFlFWc3JrOAdmWwKkqdnyHlKW4rpSuOZV6yNHM_QQSRymIn7TtagoRtCx_2g8NLLUKCmhTT33MoUmro-s9-1cQ6Kq-Zpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f79f2049c.mp4?token=qHx9LUnpHBhE1mrVb1Kt00BE3ww3ufZKAkaj_P0LK-_LYl96nALqWSFtSI0i2B1PEmNgkV8haunSFeKYFnDx1A0IeDeAUD1SvDSUW_uFGiVnQ4qxe9eHuWwlv6LmsiFfdXTvQpZgdb6JAalpExk2KVbCf44AMj33cyDN2igtaWgUqz8ySKPXyytOJMUs14R2c7CaiE5y5gTb8YXQzxwPozlvq9VbC2fWZWMho2zjWcU6NlMu-WjtzisAvfFlFWc3JrOAdmWwKkqdnyHlKW4rpSuOZV6yNHM_QQSRymIn7TtagoRtCx_2g8NLLUKCmhTT33MoUmro-s9-1cQ6Kq-Zpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: به دشمنانمان می‌گویم: با ما بازی نکنید.
🔴
در حال حاضر، ملت ما قوی‌ترین قدرت در خاورمیانه است و برخی می‌گویند فراتر از آن.
🔴
ما به‌طور مداوم تروریست‌ها را در لبنان، غزه و یهودا و سامریا ( کرانه باختری) از بین می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145936" target="_blank">📅 19:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145935">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b463d6f5.mp4?token=mlp5yK0vt4plzohgPtPbJ_Wp-yW6ttR6M6KatCJADI2utTC0Irw5URQjTPYZhimkbcGpYXhT10q0eLa4z1f2pjJed6LkBSxiqUrTt3FSq-uqysMWyRkCt0aAkscvCMVWF_evVZ1YjXrViBjOK1H4Ky9tJDRAX57u2Ql3RjND8fPxJxailYiaXThTTwigJIKLGDJBzRSoF4LfP2ZwqB9MpwnGclyH04mCzXAOOwV5FEqI3g7aeGiwUE0LJ_AcKgzop4I_SNEM-bKnfkY-4nJeuhGNs_uutRnjSO5zDWpStLymG0WXVqoCjvYGFRF7Afp-p2024-13BIm3UAImJTdR8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b463d6f5.mp4?token=mlp5yK0vt4plzohgPtPbJ_Wp-yW6ttR6M6KatCJADI2utTC0Irw5URQjTPYZhimkbcGpYXhT10q0eLa4z1f2pjJed6LkBSxiqUrTt3FSq-uqysMWyRkCt0aAkscvCMVWF_evVZ1YjXrViBjOK1H4Ky9tJDRAX57u2Ql3RjND8fPxJxailYiaXThTTwigJIKLGDJBzRSoF4LfP2ZwqB9MpwnGclyH04mCzXAOOwV5FEqI3g7aeGiwUE0LJ_AcKgzop4I_SNEM-bKnfkY-4nJeuhGNs_uutRnjSO5zDWpStLymG0WXVqoCjvYGFRF7Afp-p2024-13BIm3UAImJTdR8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو
:
اسرائیل قوی‌تر از همیشه است و دشمنان ما ضعیف‌تر از همیشه هستند.
🔴
همراه با ایالات متحده، دستاوردهای عظیمی در رفع یک تهدید وجودی، از جمله سلاح‌های هسته‌ای و موشک‌های بالستیک، از بالای سرمان به دست آوردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145935" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145934">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
غلامعلی حداد عادل : آقا مجتبی خامنه ای خیلی ساده زیسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145934" target="_blank">📅 19:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145933">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که یک پهپاد شناسایی تسلیح‌شده وینگ لوانگ II نیروی هوایی پادشاهی عربی سعودی را در حالی که مأموریت‌های «تعدی‌کارانه» را در شمال مقبانه در استان تعز انجام می‌داد، امروز صبح با یک «سلاح مناسب» سرنگون کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145933" target="_blank">📅 19:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145932">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
حمله اسرائیل به یک خودرو در جنوب لبنان
🔴
اسرائیل در «النبطیه» یک خودرو را با پهپاد هدف قرار داد که به زخمی شدن چند نفر منجر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145932" target="_blank">📅 19:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145931">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIOkjNmZW5kpShPp_BEJOWYIjXqROdE7GHYPY5FxvXPV-2Yq9ow_rilFsNl9Dwt0_Ss6Qt6UedRQ2efFPLbGmovh5z6UMIkglH4CWsxXu8N-cYXxpZkSNq0GvMwl1LlZ8KThCXxEEAzWsP2HWLrJuOR1PDtjPM9LxYLat9Nvzw4AcqE85qiN1IMuwAU2g4krxoFPmaNWCYBisN-01CgOClHlD7OzAmAjWwnzw4gftiCoGbYJXk3lM1hUli0YTKz4Hts534fxlREQuWHlHWb9KRcPHHpOiggdAHn6XvqNVgXGYsOimc2WCE10wdX3DMCOb5-BgAMnNs27wKWETG3kNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه اقتصادی قالیباف به بسنت: چرخ‌ها را بالا ببرید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145931" target="_blank">📅 19:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145930">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس اعلام کرده ماده ۹ طرح «اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز» در این کمیسیون به تصویب رسیده است.
🔴
بر اساس این ماده، کشورها یا اشخاص حقیقی و حقوقی که علیه ایران تحریم یکجانبه اعمال کنند یا اقدام خصمانه‌ای انجام دهند، مشمول ممنوعیت عبور از تنگه هرمز خواهند شد.
🔴
طبق این مصوبه، عبور شناورها یا محموله‌های مرتبط با این افراد و کشورها از تنگه هرمز ممنوع خواهد بود و دو مرجع برای تشخیص مصادیق این موضوع تعیین شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145930" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روحانی : باید با مردم مشورت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/145929" target="_blank">📅 18:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ویتکاف: از مذاکره با اوکراین راضی هستم
🔴
«استیو ویتکاف» فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145928" target="_blank">📅 18:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ_6japBhm6npy7VBVLLONOnN2iwF8YGRmwXUTuitMV-5Mhcsy_0nqJ7Qo0wmLABJv-nZlg7GkoaRSEtOPbYg5zrKS_HXUnYgTp03rPztENBve88gNmzpuaTSSnvYLC0Jr-vUKw6sW98xlDbxL_jY4kuRiO1b7_pJvw7ssQ9x2jv2osgoDAN6GmS6scFTe0SlzaWTG-Da9z3AfLlt2S8R4XeAs2ibcIeoc23hdZlkoTo1CXC8zMhnClRMO4Qx7Xz88KpWFD5xlXWAXZCYoohrU6B-3SrE_2SqiBhjWN3pHwWlz6YG-jJi2QLfrvPlmABhqGehBBeXwd0aLmjAPhcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انگار ترامپ موهاشو رنگ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145927" target="_blank">📅 18:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=gEA0MMp_oFLlq1OiqPD1LS7ozQH3CgdZLywpsHZ2owxPYdJGq6a8oNU2ZSnNP9d5O7ZsBr-6t1iQCi4dKhs6byFaAMhe7FpXLxEsKY0b5MAbUWgjJgN5ITa5pWusieC0Bw1bGP2gPz4E_M7AX3FfJfGWWumWtbi8cNiGTnTJJlbmKt29XrGBo0SZ2tf4FjQotcKewVb1ZVlcmab_5M6fbptKb9jXMCHbr-BsJR5QdvyyVjsoWEQUP6LxOTbIyBhBxyZ3lBJeZDSh2mz8Do_APawq1bJ3zG1711xR_ddAD4DLhKYQ8_AqOYZeGyJatMRSHOwa4yEoZNvXtRAO1N9Idg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=gEA0MMp_oFLlq1OiqPD1LS7ozQH3CgdZLywpsHZ2owxPYdJGq6a8oNU2ZSnNP9d5O7ZsBr-6t1iQCi4dKhs6byFaAMhe7FpXLxEsKY0b5MAbUWgjJgN5ITa5pWusieC0Bw1bGP2gPz4E_M7AX3FfJfGWWumWtbi8cNiGTnTJJlbmKt29XrGBo0SZ2tf4FjQotcKewVb1ZVlcmab_5M6fbptKb9jXMCHbr-BsJR5QdvyyVjsoWEQUP6LxOTbIyBhBxyZ3lBJeZDSh2mz8Do_APawq1bJ3zG1711xR_ddAD4DLhKYQ8_AqOYZeGyJatMRSHOwa4yEoZNvXtRAO1N9Idg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک سرهنگ ارتش: یه قایق پر بمب با جلیقه انتحاری به من بدید تا خودمو بکوبم به ناو آمریکایی و شکست بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145925" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0406c9675d.mp4?token=QVwHfIBLxelPW7kd_IhL64zxQccfKM5SbgkYLr7upCrvCzeCfQzbGuYhWz9SNNjjzGHWzS6DTOvpJE3eZKhg_HJe9rVK5YiNo2dZDTrOQW0qQdQyDgfpGyoHyDX7ds5mx4_IFzKW7pl3LoUl0zmI1frXS5Mv0cKF1IgCHhd0U6VunEvmMBperWHf9RWTi4IUWwj-YdcIoxPQDit6vyeeJoO-XA4_QaqWIR8Y1F7aFnP7OWEs3Gayi571uLfSHlZc4oI_OclPmEybeKTX4jSVjK-5MeMmv0TreTNkaygtWqEmhgkva2yW2rUScfXsOtwARbv4fINl63rtjnm_2fZNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0406c9675d.mp4?token=QVwHfIBLxelPW7kd_IhL64zxQccfKM5SbgkYLr7upCrvCzeCfQzbGuYhWz9SNNjjzGHWzS6DTOvpJE3eZKhg_HJe9rVK5YiNo2dZDTrOQW0qQdQyDgfpGyoHyDX7ds5mx4_IFzKW7pl3LoUl0zmI1frXS5Mv0cKF1IgCHhd0U6VunEvmMBperWHf9RWTi4IUWwj-YdcIoxPQDit6vyeeJoO-XA4_QaqWIR8Y1F7aFnP7OWEs3Gayi571uLfSHlZc4oI_OclPmEybeKTX4jSVjK-5MeMmv0TreTNkaygtWqEmhgkva2yW2rUScfXsOtwARbv4fINl63rtjnm_2fZNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهران مدیری سال 1401: نمیخوام یک فریم از من پخش بشه
مهران مدیری سال 1405 یه سریال 15قسمتی به صداسیما داد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/145924" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
ترامپ گفته ایران دیگه نفتی برای عرضه نداره… چین هم نهایتا ۳۰ میلیون بشکه دیگه از ایران میخره.. محاصره هم دلارو قفل کرده
🚫
اوضاعی داریم..  @ramezanii_fx</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145923" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nip7Q_mnasYrvJZ3MIH5ZuufcdKMBwYgUJfqJryTaInCBwctdSPuFoGhtgSGsTFNlif2csaD2_r5F1OQB-83y6fwapK2zB4v6gxaJQIf87Kqgc2R8xxRtyHOXRSaUQu8Z8kIyGB6RU0Xt60pUZ8kFCKuXagdvygRfha7Un22LsrxjTsY22LDFXJMNBxnXhOOmF7vlvx6Zw09hA_tZE2DNImmOhzadthjKUktRhVb3XV02YT58-DzKssSqU_oyWW4xHxx1-GoQBn8n91bJIqwAbCDA7op1b_FGGRmcnJaLC-O6H3QEIE7JQOCcP7Vf9RkYlhrQjGNVLyTdyjbp5CNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هیئت قطری به سمت تهران حرکت می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/145922" target="_blank">📅 18:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گزارش ایسنا: ۷۵ درصد کاربران ایرانی از فیلترشکن استفاده می‌کنند
🔴
نتایج یک گزارش از شکل‌گیری بازاری گسترده در پی محدودیت‌های اینترنتی حکایت دارد؛ بازاری که اندازه سالانه آن حدود ۱۰۵ هزار میلیارد تومان برآورد شده است.
🔴
براساس این گزارش، حدود ۷۵ درصد کاربران ایرانی از فیلترشکن استفاده می‌کنند و در دوره‌هایی مانند «اوج خاموشی»، قیمت برخی بسته‌های فیلترشکن تا ۲۳۴ برابر افزایش یافته است.
🔴
این گزارش افزایش هزینه دسترسی به اینترنت آزاد و رشد بازارهای غیررسمی پیرامون محدودیت‌های اینترنتی را از پیامدهای وضعیت موجود عنوان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/145921" target="_blank">📅 18:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr_xx6Eu8GpKxWnsjbVAKVtkmsam-qf_rSfaJ5CHDQENv5msFf5I8DB01FIjzCjbK2QMd-fwSlQSxNbUj75gITRoXRclqbUebWIGgboi7zcup4Ra-FAXujOjeUk9Mwr33PdEjmM9bplIYRsN9F0Ewjevjnr9VfktcDsXtLiAq1yq2Sb-7oWTZSpC4RBggi8V6Jjo99FO-EXzw1ma2X0QG2hucYuWqYUZ3v3u9TCNTACWGP0Dwvbt-0bUoimiUFGSLTDgZhnfxPJCY38L3OHLhjWl378fclRsmaW0AyP_A0X93CgyogmY9cbA4AIJ4i4LAk1rODki1VDDdg-WcY_4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت داماد آیت الله روحانی
: علی‌الاصول، روی اصول خود ایستاده است؛ مردی که ز عصر خود فراتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/145920" target="_blank">📅 18:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اویل پرایس: اختلالات شش‌ماهه در هرمز حدود ۳۳۰ میلیارد دلار به هزینه واردات انرژی جهان افزوده و حالا از عربستان و امارات تا عراق، کویت و قطر، خطوط لوله زمینی و بنادر خارج از هرمز به یکی از مهم‌ترین اولویت‌های امنیت انرژی و سرمایه‌گذاری منطقه تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145919" target="_blank">📅 18:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
جزئیات عملیات مخفیانه مین‌روبی آمریکا در تنگه هرمز
🔴
آمریکا عمدتاً در طول شب، غواصان نیروی دریایی موسوم به Navy SEAL، قایق‌های رباتیک و تجهیزات تخصصی زیرآبی را وارد آب‌های خطرناک تنگه کرده است تا طی یک مأموریت چهارماهه، مین‌های دریایی را پاک‌سازی کند.
🔴
این عملیات دشوار برای خنثی‌سازی مواد منفجره، در زیر آب و در تاریکی انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/145918" target="_blank">📅 18:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روزی که تلگرام رو به بهونه تاثیرگذاری تو گرون شدن دلار و سکه فیلتر کردن، سکه ۱میلیون ۸۴۰ هزار تومن و دلار ۵۸۰۰ تومن بود!
🔴
جالب اینه اون قاضی که حکم فیلتر رو داد بعدا به جرم فساد راهی زندان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145917" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145916">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
حمله توپخانه‌ای عربستان به یمن
🔴
منابع خبری از حملات توپخانه‌ای عربستان سعودی به شهرستان مرزی شدا در استان صعده یمن گزارش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145916" target="_blank">📅 17:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145915">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای قالیباف: بیش از ۵۰ روز است دیگر تفاهمی نداریم و نتوانستیم به حزب‌الله کمک کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145915" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145914">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=oL0iM6OeGeoGCSN6I8wvm23DhzevRhDURHhPkOeOc9f_ATa1dxedbCjIHWzkXhqfsvs2A1eDAYQluWquCSQPlw5_9X6FKY9Mo_lmqEecawiM_5Y34AzI4LsUfMth9GU1RS1Dl-LSSiYhWlMpKOWFqRdxzNjLeTo69citgGGMh9wHybDeOlP3y8UJEP-vZMXB5AbxD-n70y5JTl52gWjY9bMFMVGplkOI6qFZe2vM800dxJ3oRH3kVG3SIWUne2WwcoOZx7bqp3CNBGDT_jttWrLahWP-xuJSTC7sCutEGYbJSCBXlw7DlzItZQaoAZOVLMTjGOKxuqsth3Otmr3o0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=oL0iM6OeGeoGCSN6I8wvm23DhzevRhDURHhPkOeOc9f_ATa1dxedbCjIHWzkXhqfsvs2A1eDAYQluWquCSQPlw5_9X6FKY9Mo_lmqEecawiM_5Y34AzI4LsUfMth9GU1RS1Dl-LSSiYhWlMpKOWFqRdxzNjLeTo69citgGGMh9wHybDeOlP3y8UJEP-vZMXB5AbxD-n70y5JTl52gWjY9bMFMVGplkOI6qFZe2vM800dxJ3oRH3kVG3SIWUne2WwcoOZx7bqp3CNBGDT_jttWrLahWP-xuJSTC7sCutEGYbJSCBXlw7DlzItZQaoAZOVLMTjGOKxuqsth3Otmr3o0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد سامتینگ: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145914" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145913">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRvLjwejvuYLLgir_3PGR_8gxwnAftBGfaDWFfEM9VC_d_qtPOk23kiDEr4RiDhNPIMFYkKPF-T3xxcTlVbhGf06w4FmKZjMSbx3aiHtSL8apED964r0yc-r9WDbLH7sSWrKhznfTcW5a00hoIuRUIj9konBXP037GTMlL40nwAmf12BWxMBOv7oj50n0NmRT26mo_kRZWH1ZAzr-KS9nxPww14rmdbVFLRSbBFTczfZmsdlb_s-b3WPULi_6upMptFLHfIh17bc4Q4suWfWqPK0ToQn163LrEkxWHLGzXvYBGBzPwN7Axabwan2IEz0dMH-b1pJE-wWnw94MPwtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فیاض، استاد دانشگاه‌تهران: تو خیلی چیزا از آلمان و اتریش پیشرفته تریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145913" target="_blank">📅 17:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145912">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
طلای ۱۸ عیار 23,504,800 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145912" target="_blank">📅 17:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145911">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
👈
دبیر انجمن فرآورده های دامی:
به علت گرونی نرخ ارز، قیمت سوسیس و کالباس افزایش پیدا خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145911" target="_blank">📅 17:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145910">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: سطح ترانزیت نفت از طریق تنگه هرمز به طور متوسط ​​روزانه 9 میلیون بشکه نفت است.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145910" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145909">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پژو ۲۰۷ اتومات ناقابل ۳ میلیارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145909" target="_blank">📅 16:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
👈
سی‌ان‌ان گزارش داد:
نیرو های تحت حمایت عربستان در یمن پس از درگیری‌های شدید با نیرو های حوثی،
وارد حومه شمالی شهر حیس در جنوب بندر استراتژیک الحدیده شدند و آن را تصرف کردند.
🔴
نیرو های تحت حمایت عربستان و امارات در حال پیشروی به سمت بندر استراتژیک الحدیده در سواحل دریای سرخ می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145908" target="_blank">📅 16:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145907">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14170fc93.mp4?token=hH5ADymoIF2JedOKO5bJdJokeI80uwXUaHeaqMsoRawp8DzPBSZRGUoUjCmXS_BS-y0O4Mpq40dDKUMw1tzutInlFrl4KfTGmuGu0IBg0rBWYgrDg-reagQSntwLtp2aQzN_cCEg0rtP-KSOuO1WI_fwH6UXwT4nigA8_YtN0kh38-wyXUMP72xukDv46QsCRE_QdpnvqsgFN4pGb_hAW4hnENUTF2zjHthRMMiIrTsUZ6I2BwyJeYzqnNqH8zBIBkBhKRS-ZAHtgr06675mywqXvXJjt1ZfTGxquSq7XmaaUOfUKEaUZ9Gmm99ND_-hnM4jXZJTs9KYE89EtHTQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14170fc93.mp4?token=hH5ADymoIF2JedOKO5bJdJokeI80uwXUaHeaqMsoRawp8DzPBSZRGUoUjCmXS_BS-y0O4Mpq40dDKUMw1tzutInlFrl4KfTGmuGu0IBg0rBWYgrDg-reagQSntwLtp2aQzN_cCEg0rtP-KSOuO1WI_fwH6UXwT4nigA8_YtN0kh38-wyXUMP72xukDv46QsCRE_QdpnvqsgFN4pGb_hAW4hnENUTF2zjHthRMMiIrTsUZ6I2BwyJeYzqnNqH8zBIBkBhKRS-ZAHtgr06675mywqXvXJjt1ZfTGxquSq7XmaaUOfUKEaUZ9Gmm99ND_-hnM4jXZJTs9KYE89EtHTQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی دست هر پسربچه ای یه چاقو هست و هیچ برخوردی هم باهاش نمیشه واضحه که آخرش به اینجا میرسه...
کشته شدن پسربچه ۱۵ ساله توسط یه پسر دیگه با ضربه چاقو به شاهرگ
📵
هشدار محتوای حساس
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145907" target="_blank">📅 16:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145906">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eer0Rk0q7Pk18s1X4SrFlgOsyLhDlnPKSRGuNnNI0a9c1ZMlIeHPjKoWrTBCxQBXRHB2dQalPP_Bfxp7MZ6s2yu4BTFJjxEdAIWdPtMqs4ae0d26jUbY_9WSZvipu6kwdP7QMyxgDjBNYvdo5IYDysNXGPxSWsLcpPacEr6ldoguNKzwDkM8m9l16qHMTh98XWE-00frtXe_SLox7jKtp9Y3HWJ5AY0p-69FP7VAwc8J3A6zoQFoyDrah-ri0Lw2xPIIJB59YMQynB_hvKLPXSd6KI23PrRSwGmWXfG34ulUQZymox3QO49Ti78XgCb4dqmfj79S5WEHzxqweKvdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منچ‌اوسینت: از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در «مسیر عمانی» تنگه هرمز، پس از هشدار نیروی دریایی سپاه درباره بسته بودن این مسیر، تغییر مسیر داده و برگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145906" target="_blank">📅 16:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145905">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">وضعیت جوریه که اگه بگی گرونی شده، به جرم تبلیغ علیه نظام میگیرنت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145905" target="_blank">📅 16:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145904">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d924e78a9.mp4?token=nU_I0cc5zrAe3meViHb3J3ZwMSwm_cqe05F7p5Fm9Jmwy_TBoiz6W6jhqTjGWozxNiXQHn-y2RFL8oAp0UDVYqmeggTbOhKypyNNzc9i7HtR1biReADszfOknUSFrQwRYBDFLn9SFhQddsJHdCe90y7HPKw4JN6LsbNi-fUqLHNnoSHEXuVmZuKochyYC7bFz6WvdMAU08MKtESf7zhCEgedGJQGxI-jK3EXhAihpT5u_edv-BhUjEJoMfnBrkiGxBedNBspPnRnSAY7u93HBDwPPji20HjayOkFPD6pQKAA_QwBA4o4kRYB28bnrfNzlR4eG3nRwFYiCboFNUAN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d924e78a9.mp4?token=nU_I0cc5zrAe3meViHb3J3ZwMSwm_cqe05F7p5Fm9Jmwy_TBoiz6W6jhqTjGWozxNiXQHn-y2RFL8oAp0UDVYqmeggTbOhKypyNNzc9i7HtR1biReADszfOknUSFrQwRYBDFLn9SFhQddsJHdCe90y7HPKw4JN6LsbNi-fUqLHNnoSHEXuVmZuKochyYC7bFz6WvdMAU08MKtESf7zhCEgedGJQGxI-jK3EXhAihpT5u_edv-BhUjEJoMfnBrkiGxBedNBspPnRnSAY7u93HBDwPPji20HjayOkFPD6pQKAA_QwBA4o4kRYB28bnrfNzlR4eG3nRwFYiCboFNUAN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا شخصی که تو یه ویدیو گفته بود دوتا سیب زمینی شده ۱۰۰هزار تومن، دستگیر شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145904" target="_blank">📅 16:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145903">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEqSqaxwpZ0tRT2mHsu3Nns4MoqmtLWXM1fl7_7syDfzlZbt2DbhsQ9ZCwnuIszxzIDhMb9cG4sEkAEajx3PVHhsw36Zi0Iqya6L99g62JiI_A4yODrY7bTO9zeW7oRNWHtM2geCsNCrVtJxAjKZNmSg9ztD0fm7JDFd1_ikH71rpKLABsr1lIt3K8APfK9qXwx6U-BadcmI0Bwdb17Xb5GyM0vCQZQpqrbcLWIZkq9W1uekWjIBpHP-c3KOK4tk0gyEfXcDfCRsY0qKF28FSWRRJutmy07Vc9R9dh1tgx0fHjvVJZrpLEpoH4xAqKlCMKRUdvP1GR7a602be5W8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری نماینده مجلس: اینکه ترامپ گفته بیایید از پول‌های بلوکه شده بهتون دارو و غذا بدیم غلط اضافه هست ما فقط نقد میخوایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145903" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145902">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل: اوضاع از چندین جهت بی‌ثبات است و ما در ایام اعیاد یهودی در آماده‌باش کامل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145902" target="_blank">📅 15:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145901">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjMA1EyT7fcV58286LSwlbM3rfXPrpzFA3vaftalBBIKaZv6U_m9T_nEu4gpNa710EDUyEFoCfIJaPFK6--rKuWOR5r5oV5Yyr4IWrn3JNBcrh5BGSssSwqO-swNyULRAmgAkat8d4Gtkdje3J1EcGgeRdSg8twJTG7rr7SC2ytpHik9FNWbUCpNjO1O6yfKj8Bh0UZ5WmkMn8hS_ym-z-58KmHehugSYQWi7zjVvThie4PQNfQilTyy_7NRG7mxoGYVJS1aPbNEtc9uq8A3cn2yZ0N7tGGmpL_lB7VvVlPG5BIz6fSKXMCtzuNQjobft9OnfyCnSyMOITUFRQLgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت جوری شده که حتی عوستاد هم نمیتونه تحلیلش کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145901" target="_blank">📅 15:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
اردستانی، نماینده مجلس: جنگ طولانی شه ممکنه ترامپ بمب اتم بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145899" target="_blank">📅 15:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145898">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سنتکام: ۹۲ کشتی تجاری را از مسیر ایران منحرف کرده‌ایم
🔴
ستاد فرماندهی مرکزی آمریکا اعلام کرده از زمان ازسرگیری محاصره دریایی ایران، ۹۲ کشتی تجاری را از مسیر خود منحرف کرده است.
🔴
سنتکام همچنین مدعی شده در همین بازه ۳ کشتی را از کار انداخته و ۲ کشتی دیگر را بازرسی کرده است.
🔴
این آمار نشان می‌دهد فشار دریایی آمریکا بر تردد تجاری مرتبط با ایران همچنان در سطح بالایی ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145898" target="_blank">📅 15:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145897" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145896">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvraHzLeRlO3dbV93Z1w5-3p2GKPpMq_SEAKAPYCc5BFRNjwpYFwXWfPHOVqYaYRPnlYP7kxZAUzHINDUBr16capGNvU381beacErPufSSZLflrolCMCvvJEfHQPo4z2Lyea_JP8Umak8ZMmdCwQDQsPZ3xKi-MEqxmvvRjkILljEo6AKGUrvSXy6QP6ufMlsgYZB8qEh9CYjjvH10JyDGzkYVj3wYu9_o9UnCzyJJLMyeJilmRudlbERxvUwqOy8DYQFFhbTctOUkxL62DbMRqp4S0rHBftPyOpPEljhyc7q2tlOCwQeFitE-gU0ksui4b8Nh9WjLhynAHQZDeXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت جوری شده که حتی استاد هم نمیتونه تحلیلش کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145896" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004a973a40.mp4?token=E-UleUUL_5OtUXSGow6UEG5hBdtjVl1ZMK5iIhNTGCBMIVE5od_6K8aPXzWRYAMsfz52gZhW3jwR9ksgR7bVYoAjU7Q2OmOJZgLl_0WrQPPk7j3WTBCbV_TYReq-MyHR4xZFgaafm1ZCGWZsk7sdqO7MfZsVgZ3ZCzgh7nsxsd6GMyWxvRfOwAs8NS_0Yq62L-3e_fN2sklD67o1zmO6QmBPpZ40r8T42nVOj3q9AEd3ViB8W_WJYRsVCU8YQJsu81R7JS_KUNWzgsl6X0qifuOTIZP-Z8-uLOHhtZb8lKDCewe-IGGcsLJE82SQAUvQFE6VBK4E6abNRaOEb7OqlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004a973a40.mp4?token=E-UleUUL_5OtUXSGow6UEG5hBdtjVl1ZMK5iIhNTGCBMIVE5od_6K8aPXzWRYAMsfz52gZhW3jwR9ksgR7bVYoAjU7Q2OmOJZgLl_0WrQPPk7j3WTBCbV_TYReq-MyHR4xZFgaafm1ZCGWZsk7sdqO7MfZsVgZ3ZCzgh7nsxsd6GMyWxvRfOwAs8NS_0Yq62L-3e_fN2sklD67o1zmO6QmBPpZ40r8T42nVOj3q9AEd3ViB8W_WJYRsVCU8YQJsu81R7JS_KUNWzgsl6X0qifuOTIZP-Z8-uLOHhtZb8lKDCewe-IGGcsLJE82SQAUvQFE6VBK4E6abNRaOEb7OqlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145895" target="_blank">📅 15:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قالیباف: حملات ما به پایگاه‌های آمریکا تنها یک آغاز بود، قوانین بازی تغییر کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145894" target="_blank">📅 15:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiW4WRYVnKS6wHnQYKwJJffJt4ekzL2EqIfOTmo4AkpQNmmrku3tzt10U_MEeWmYJ87c_fqLM4fu6jKUFKMOfqPNoiDEEuni866RyR0TAvQYHTwDRenMIPsYIMtKdnJ4w_O553c3QbSiqJ4wNAMhyEC2IufpLbuDbI9EEmUqekSUtqzl9X9WK2qPacfwN7v-tIZPbbBHrbR2_Spqq7y9oXlK-lpe4Bsi93RbBN8FTcz0iqzspPdIeBx-WdnlNqmwYufVdJKGCQM9l3quBtbvbP_iOqc_Fy8XKPx0B-r4lPQlAPxVolhJvj4PKMRDTIn_wllxCxI5yC9TW8PF2lTSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: ایران در حال برنامه‌ریزی برای حمله‌ای جدید و گسترده به اسرائیل، مشابه حمله ۷ اکتبر، با هماهنگی گروه‌های نیابتی خودشه. بر اساس این گزارش، ارزیابی‌های اطلاعاتی اسرائیل مدعی شده جمهوری اسلامی قصد داره حمله‌ای چندجبهه‌ای رو با مشارکت حزب‌الله لبنان، حوثی‌های یمن و شبه‌نظامیان عراقی انجام بده. همچنین ادعا شده سپاه در حال برگزاری نشست‌های برنامه‌ریزی و تمرین‌های مشترک با این گروه‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145893" target="_blank">📅 15:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797b887a7d.mp4?token=W2ioDeq6ActEeo4eZz7q9nFEg25eu_YmTPQ3j6aLxPN6tAAWgmFY1_TsFhPWUZLj9MaQQb1szfI4Cq6oqkZrygSyKwoMU7zVxGGVK7eoPZF5W8q7wbIAgFySeiFHaqmM02gQBVDKMJvZO_0ngtqHLt_qf8dONeoF_fc6fSQVQKT1NMk8HXSrWfZyyxcPezBSgjnuGmgQfMzRI_-tz3XRviSrOMpc65bDxiQqc7VeG-73_EbTI2BNXzslcV6BGJOUGrUQigYQYrp9Ph4J6cEKd8q62x1jxKCOQLvi-qgAG2g4hskt7xLIabcykyHVgl-j7UbxCjfpllz0r9h78PFAbJ9WzeBrq6OB-62Z_Wt2ncLTrqvVBY03ughMYAafghoLtSgHpDsPWeXCYlSMwrrRdXxUQq32reo9yLVcQ78ATVBD-bI9jdibcv4U3JsclxAs0drTRyJfHku7wfCtghJNedkkqfD5QEsRC5iD0yL6b_xF8oGfvJgXXXO1wOnz-nL7P7qwMSfz4K2b556g-TgCHzovg9ojo5X_sroChBz61veV5i2lP3aSjhWjV6VC6y7EAXLRHg39lcQ7zBwYclR0iBGr3A-L8L8KTnBu4IF0o33_i8ytL1Y1mwjrMNzualH6ZOaGO-bVYIA2OxY3pm91t3PGzLZex0xDNoCMYmnEm8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797b887a7d.mp4?token=W2ioDeq6ActEeo4eZz7q9nFEg25eu_YmTPQ3j6aLxPN6tAAWgmFY1_TsFhPWUZLj9MaQQb1szfI4Cq6oqkZrygSyKwoMU7zVxGGVK7eoPZF5W8q7wbIAgFySeiFHaqmM02gQBVDKMJvZO_0ngtqHLt_qf8dONeoF_fc6fSQVQKT1NMk8HXSrWfZyyxcPezBSgjnuGmgQfMzRI_-tz3XRviSrOMpc65bDxiQqc7VeG-73_EbTI2BNXzslcV6BGJOUGrUQigYQYrp9Ph4J6cEKd8q62x1jxKCOQLvi-qgAG2g4hskt7xLIabcykyHVgl-j7UbxCjfpllz0r9h78PFAbJ9WzeBrq6OB-62Z_Wt2ncLTrqvVBY03ughMYAafghoLtSgHpDsPWeXCYlSMwrrRdXxUQq32reo9yLVcQ78ATVBD-bI9jdibcv4U3JsclxAs0drTRyJfHku7wfCtghJNedkkqfD5QEsRC5iD0yL6b_xF8oGfvJgXXXO1wOnz-nL7P7qwMSfz4K2b556g-TgCHzovg9ojo5X_sroChBz61veV5i2lP3aSjhWjV6VC6y7EAXLRHg39lcQ7zBwYclR0iBGr3A-L8L8KTnBu4IF0o33_i8ytL1Y1mwjrMNzualH6ZOaGO-bVYIA2OxY3pm91t3PGzLZex0xDNoCMYmnEm8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موبایل‌قاپ حرفه‌ای در شهرری به دام افتاد؛ اعتراف به ۱۰ فقره سرقت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145892" target="_blank">📅 15:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OapCQI3tUD-2JMjKSEo9HrVvSh27k_Y7qcvJ9MRlXxnP-iRMDpIYdOR32pCD9eBnaGSAg0svFLBgtFx7diewftYB0igg-IdhmwML4a5bHxVFnK_9tyIUg4NwZuOy2ISI23L3bA_kLZCECHEm6dKFnozdUICQuZwYlVtBrTO8kIm8liLdbZ0cvmiEt1e-iti6-vd7TTOd-VFKoMkHno9ZhCQmFRALPQsEAegmRPxuF1HRtUsZZbgis5fBJbys10KI9zCxltJy5Ptc6gZnmK447dtu5tZING1YmNSEWCt97XvmoomfXdT02mr2A4fAUV6zNy7jI42nuGCgx6ApHbAvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد امروز یکشنبه وارد مسکو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145891" target="_blank">📅 14:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
زلنسکی: «مذاکرات آغاز شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145890" target="_blank">📅 14:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f92ebb79ed.mp4?token=hAEwsNzN6e46eyYkg-JZuzVoCIRSVeYcnR9HA24lIzOQZaUSmQZYHUoQ1MajrBHpOyk_HTjT1IfrnM7IaEEArumUL-lP_wgAgtv4Vyw0vNz4yiLDdceagwinOoFnYkVd_lGe16dYP6E4hABbNyr4fWt6fvSCaz8KLmxlIHu7O0MBBL87Nb5jf_WxIRUDA94JjscsSxB8UwY31bF5wE9KDBqHXhbnHnsrMrSENNOsQDw7SOd-Aw4JMM_TVTp5M9piq7HQLac5qk3jszNerbLz-T8VZ7r4yDO2mXFFrJIJAnZwv0IX5T8J9UgMmdn2nVYExpadGBrodFg3BqlUmk2ebzfZHQbVscnJ64AyeA3BTzjRHcxof9qhbRKzYqQpDcGUloXtV3zyO1Mxmz8ylfHe2OSsa585OnjsWrXx0MdpZagf2XPe3Isbhiu1PIXpXalARIpMkRQbnOYl0mTAQEuxjwpLO-cnB2VhXrLT5vVOGq7YWWu61_12E0pM2NlsqfRmBmQXb4Ns8zlaI_fPFjkyRx5Cs6JyvnEvlP8tBljy1cuKPw9t2CzPo09U7FFCdYR2nhNrlkwFV8mSbQtf8Mce95hBDqbVgEcNhI2p4vq3cF6jggVeafQDL67hjwSmdxVcp1YlCyDOTvCUCiv9MffUjUTDah6AdKSBBdEf63yzOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f92ebb79ed.mp4?token=hAEwsNzN6e46eyYkg-JZuzVoCIRSVeYcnR9HA24lIzOQZaUSmQZYHUoQ1MajrBHpOyk_HTjT1IfrnM7IaEEArumUL-lP_wgAgtv4Vyw0vNz4yiLDdceagwinOoFnYkVd_lGe16dYP6E4hABbNyr4fWt6fvSCaz8KLmxlIHu7O0MBBL87Nb5jf_WxIRUDA94JjscsSxB8UwY31bF5wE9KDBqHXhbnHnsrMrSENNOsQDw7SOd-Aw4JMM_TVTp5M9piq7HQLac5qk3jszNerbLz-T8VZ7r4yDO2mXFFrJIJAnZwv0IX5T8J9UgMmdn2nVYExpadGBrodFg3BqlUmk2ebzfZHQbVscnJ64AyeA3BTzjRHcxof9qhbRKzYqQpDcGUloXtV3zyO1Mxmz8ylfHe2OSsa585OnjsWrXx0MdpZagf2XPe3Isbhiu1PIXpXalARIpMkRQbnOYl0mTAQEuxjwpLO-cnB2VhXrLT5vVOGq7YWWu61_12E0pM2NlsqfRmBmQXb4Ns8zlaI_fPFjkyRx5Cs6JyvnEvlP8tBljy1cuKPw9t2CzPo09U7FFCdYR2nhNrlkwFV8mSbQtf8Mce95hBDqbVgEcNhI2p4vq3cF6jggVeafQDL67hjwSmdxVcp1YlCyDOTvCUCiv9MffUjUTDah6AdKSBBdEf63yzOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: من مدافع طرح نفوذ هستم اما نمی‌شود کشور را قفل کنیم و بگوییم همه از ما اجازه بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145889" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68141df3da.mp4?token=dJxBz2-tupj_IXGisT85iNtTSLg6wwFXd-ncsEp2q5UUrvJQwNbDX2pJ90wqOvKWwR8h0rGBcN9fpgXZHQvQxx0qPTpZzTzrA5DY4uL3tB66VBSSU1aOWlP5oAaqsPuJFiDgye3j4c5IxLxcWt2EkiLa2DUSCebYGt5ZE0ocLDvuDUXo0aP-b4rcPkojc7oFRyhv_nLZwBQwMDl0SKJj_sK5vPv6Buz8Bylk6LH3LcFs6m9hZKXi8kI9taf6biQ9oZs6_8JV9uoPX0Ci5wluRcfTtWtEJehASTbyjt33Yirnz6XdF6dGf0fQ9wEoC0qXpYFfJCEkvPa07DZy-wPtRbQY8-0dQ0s2cpMBYrNWq4eCGcA2ZvVAeayrMC8iKJU3BzKuU6hVTl1ktoQytOxT3qdfJZU1dGbTeLToIypOpdgWQRRPyaaJFAnQuR_S42R27OWPgrMd-Kk2WcRWneCGN8O4fBifr1SvQfWHggR38EnVXT_eDE17l1pmTovSVvNn1uWjlwdI3hpV4jjX2LbOkf0efzNaO-5yVH4MVbiZp53vsARHXnC-Js9L6XOZfmoHFKnjas_jLczZvAgEdBDL-wcbuC28TCtUqvxvtgtxL7SO0YNDI975MnanZrnLYPNH2L5NXMm-tjypX3eBg6gg_37epeYLztUD-xVb-5uoLfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68141df3da.mp4?token=dJxBz2-tupj_IXGisT85iNtTSLg6wwFXd-ncsEp2q5UUrvJQwNbDX2pJ90wqOvKWwR8h0rGBcN9fpgXZHQvQxx0qPTpZzTzrA5DY4uL3tB66VBSSU1aOWlP5oAaqsPuJFiDgye3j4c5IxLxcWt2EkiLa2DUSCebYGt5ZE0ocLDvuDUXo0aP-b4rcPkojc7oFRyhv_nLZwBQwMDl0SKJj_sK5vPv6Buz8Bylk6LH3LcFs6m9hZKXi8kI9taf6biQ9oZs6_8JV9uoPX0Ci5wluRcfTtWtEJehASTbyjt33Yirnz6XdF6dGf0fQ9wEoC0qXpYFfJCEkvPa07DZy-wPtRbQY8-0dQ0s2cpMBYrNWq4eCGcA2ZvVAeayrMC8iKJU3BzKuU6hVTl1ktoQytOxT3qdfJZU1dGbTeLToIypOpdgWQRRPyaaJFAnQuR_S42R27OWPgrMd-Kk2WcRWneCGN8O4fBifr1SvQfWHggR38EnVXT_eDE17l1pmTovSVvNn1uWjlwdI3hpV4jjX2LbOkf0efzNaO-5yVH4MVbiZp53vsARHXnC-Js9L6XOZfmoHFKnjas_jLczZvAgEdBDL-wcbuC28TCtUqvxvtgtxL7SO0YNDI975MnanZrnLYPNH2L5NXMm-tjypX3eBg6gg_37epeYLztUD-xVb-5uoLfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اخیراً تماس هایی از مبداء نامشخص با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های آتی هیچگونه حمایتی از سپاه نداشته باشند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145888" target="_blank">📅 14:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ضرغامی: جنتی به دلیل کهولت سن امکان ملاقات و حرف زدن ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145887" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce26d7459.mp4?token=TQAEl2QoFtJBWX40ml9RtQANhIWykyZB5pfUgXoyG7YmcSeWJJem1QYeEsNeI9BypiD5Sjdv33W4EnHnvzq1xo7HgJpTr9PstKWXR83rHWpRmb5Wjalt3p3gNExTVbk5nErlmff_8CykBgnWNvMzwrBYbBb02K3wEIXftH3RKSbySI1GsLx_sGssugM95rYBJ6TV9TiZqquakl3jdeU2Fq8CMUPzi4nw7ZmgJ8Sgm03-JBye4zLBDX1HPsZhFTK-GMnMZcyuv8RbvTbyYUj77GQPON9nPk_LHsSaFWEgkp2IOJA_0G_P00AwdzDLbcimVrBiyze40BU-T1Ln7of6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce26d7459.mp4?token=TQAEl2QoFtJBWX40ml9RtQANhIWykyZB5pfUgXoyG7YmcSeWJJem1QYeEsNeI9BypiD5Sjdv33W4EnHnvzq1xo7HgJpTr9PstKWXR83rHWpRmb5Wjalt3p3gNExTVbk5nErlmff_8CykBgnWNvMzwrBYbBb02K3wEIXftH3RKSbySI1GsLx_sGssugM95rYBJ6TV9TiZqquakl3jdeU2Fq8CMUPzi4nw7ZmgJ8Sgm03-JBye4zLBDX1HPsZhFTK-GMnMZcyuv8RbvTbyYUj77GQPON9nPk_LHsSaFWEgkp2IOJA_0G_P00AwdzDLbcimVrBiyze40BU-T1Ln7of6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود
🔴
ولودیمیر زلنسکی گفت: «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145886" target="_blank">📅 14:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فارس: دلار ریخت و به ۲۲۴ هزارتومن برگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145885" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0192c9a24b.mp4?token=hFH64UWOHvr_a5scfctQjPKImnfHgjBg7_95bhRCtMrcHa9jOR-g-N_d_OzzdbeqSC93VlWwKRxlviwlsxDCqvPFk5mKDGHUM1EHMZU4myId44qTCDt9sEXEuSL17qgNWNziQq99lc6Qvd7WXT-nAQi2B4EGHiS42EJCfI7laMcrcY11ZLQyvDxQpubakcej7CZLtLflyxMJ9_m8FlNNeU37687aQADiA0iVthDqJr8GH9pm596_xvR7O7xn-VFyYfs5IjP_fmKN-26XYKZ7thfCSSlsnVO7BqQj_IffV9atiR4RCPN_2nCYCsGW85sNMextW15Ts_1Zw9PoRkA7Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0192c9a24b.mp4?token=hFH64UWOHvr_a5scfctQjPKImnfHgjBg7_95bhRCtMrcHa9jOR-g-N_d_OzzdbeqSC93VlWwKRxlviwlsxDCqvPFk5mKDGHUM1EHMZU4myId44qTCDt9sEXEuSL17qgNWNziQq99lc6Qvd7WXT-nAQi2B4EGHiS42EJCfI7laMcrcY11ZLQyvDxQpubakcej7CZLtLflyxMJ9_m8FlNNeU37687aQADiA0iVthDqJr8GH9pm596_xvR7O7xn-VFyYfs5IjP_fmKN-26XYKZ7thfCSSlsnVO7BqQj_IffV9atiR4RCPN_2nCYCsGW85sNMextW15Ts_1Zw9PoRkA7Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فریدریش مرتس، صدراعظم آلمان:
«برخی می‌گویند: پس بالاخره حمایت از اوکراین را متوقف کنید تا شاید در برابر تهدیدهایی مانند آنچه در فرودگاه لایپزیگ رخ داد، امنیت بیشتری داشته باشیم.
🔴
چه ساده‌لوحی‌ای! چه ساده‌لوحی‌ای!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145884" target="_blank">📅 14:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d6b0d35c.mp4?token=EdupjRa_bimsUckoLgsH-PZd6F_YHW4FX4NFuUFueaDQrYq8ytuMMV-x6vczb_ZoIIn5j2No96d5WoIP66yUk_sSZUYrB7ugab1pdnRHXi6kUBSqozWfh7t1WGaI7SES0KuQeoLebsSeM5S6Z3h6-xAk7c-wrzwELPtMvEV2AUdt7XuCHVktQmqS0rlhMDg7L4Kp6sXXnhBrxV-jA2zjOUHU-k8_V0sKZRw_aPfitj2CzI0n_nqxr8y-a_-GFixi3qS-_k895kY84wLNz0_8yOBtlPFkTC5uTLH0TL0gNs1FTiqqxIVw8bGhn9O3D-fLyrmcJ7kQZ0mXh8J1zhAyGV9sSyzMS0ElJhVwfPKRxpxeyCCnGvArulhr5Xij4KjPZQwGbRiUQ3YbJGmjwUfcdppJg6R7nIWDgCXOojmM-796qCnXDHitB0X7pDzjHu8i_uKqi2h98opNFe8nrr_k98D0TxLQFdUf4gZguyIHLSqHMUGkAhpsXuHtsu4xHw3SAjUmcDjqVisyHIyUt6ERbAVpiZpZAMB4qIve9dqJDkKL5bBao2HqiazsIyPkm2DjJjKGVGYuh0FzwUc-4Qg4YEdvs0BxAnw5-yd2JFETqYAWPWwQWCRzb6LkZXtZxjB_Es_y1eh2jmZoD1lKG9MtjyGZg0M4b7UKkLhJL3EfUnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d6b0d35c.mp4?token=EdupjRa_bimsUckoLgsH-PZd6F_YHW4FX4NFuUFueaDQrYq8ytuMMV-x6vczb_ZoIIn5j2No96d5WoIP66yUk_sSZUYrB7ugab1pdnRHXi6kUBSqozWfh7t1WGaI7SES0KuQeoLebsSeM5S6Z3h6-xAk7c-wrzwELPtMvEV2AUdt7XuCHVktQmqS0rlhMDg7L4Kp6sXXnhBrxV-jA2zjOUHU-k8_V0sKZRw_aPfitj2CzI0n_nqxr8y-a_-GFixi3qS-_k895kY84wLNz0_8yOBtlPFkTC5uTLH0TL0gNs1FTiqqxIVw8bGhn9O3D-fLyrmcJ7kQZ0mXh8J1zhAyGV9sSyzMS0ElJhVwfPKRxpxeyCCnGvArulhr5Xij4KjPZQwGbRiUQ3YbJGmjwUfcdppJg6R7nIWDgCXOojmM-796qCnXDHitB0X7pDzjHu8i_uKqi2h98opNFe8nrr_k98D0TxLQFdUf4gZguyIHLSqHMUGkAhpsXuHtsu4xHw3SAjUmcDjqVisyHIyUt6ERbAVpiZpZAMB4qIve9dqJDkKL5bBao2HqiazsIyPkm2DjJjKGVGYuh0FzwUc-4Qg4YEdvs0BxAnw5-yd2JFETqYAWPWwQWCRzb6LkZXtZxjB_Es_y1eh2jmZoD1lKG9MtjyGZg0M4b7UKkLhJL3EfUnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ قالیباف به نقدعلی نماینده نزدیک به پایداری: شما نمی‌توانید برای من تصمیم بگیرید و من حتماً مثل شما سخن نمی‌گویم
🔴
ادبیات شما مناسب شرایطی که بر کشور حاکم است و همه حرف از وحدت و همدلی می‌زنیم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145883" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فریدریش مرتس، صدراعظم آلمان:
«در فرودگاه لایپزیگ تا یک قدمی وقوع یک فاجعه پیش رفتیم.
🔴
واقعاً خوش‌شانس بودیم که آن روز این اتفاق رخ نداد. این پهپاد حامل مواد منفجره تنها به‌دلیل یک اتفاق کوچک، در آخرین مرحله نزدیک شدن به فرودگاه منفجر نشد.
🔴
اگر منفجر شده بود، آتش‌سوزی گسترده‌ای در فرودگاه لایپزیگ رخ می‌داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145882" target="_blank">📅 14:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S_XSNLr73RdtjcG_X0qnbUu8QxwLZgdy4KwJ73ooeBA9V0l8Ghf4frXK-VC1M-byzleK8f6DB3jtJRysfbaUkRbkmoO0HJqJUcrL5VsKU-dazJsK3bqQ7x8QPphFH_dRtY774B10ZGLEKiBwG1cLqhHQX3aP2ARR49avSlsxOhgDmGl957yQWMSSUX3ypfJJTfeD5WLY9z1uJ7sQFC0Lm86OjK1rU7w_KB2On-aBzpUvcSzSUr8oeMYgdWgCLCPPgv-DI0IxT566DexTJ84HNkNkOO_RCP_NZ5bNPlPfBJ9YO7mkJsuV3P-oc51q99wfVji7UtPVV2-rRfV_283Ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e_lGOLrlwjmANDECSX5adAecEz8rowWEkl69yVUx1rv1esLyNMq1jSj-RkgsZUCbpG2bfYgRs-GtjgtBNrXyrho-5ZqSvMrs5N2Ak-PKsTNevGaMzt4MbP7FmrqdinzmQkq3BwoOso79SQXBgHZQvVHFJlx_7_45thUQadzNwhqPSMZ4GdpkvKq-p_o5Jt_O2VlQWr8KiOt3yPXr9PjsGBvak7lpRtQQsw72c7vRrVj1RWPQTt5WM95LTL4j2w6y2nL_EYJNSohAmc2aNPOGvhgJ9kP0Xwz-Pnn7Rx4liDdfO20IRVW_2qOx17V0Lzl2mfsEzwxG70Nal2HlLPdqcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی  در شمال اردوگاه آوارگان الشاطی در غرب شهر غزه، حمله هوایی انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145880" target="_blank">📅 14:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145879">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8ed0a2e8.mp4?token=sf93gX7bu3yHy2Tou6Zr3LEoCu0Ve3JYn6yHA87u_xuT2ff8TKsKq7jMzVMkqKEXjx4EKiAlYnClOHT9DOuUAEL8kRKeudYBCo4pFeWyeaWRhvt-6kl5-uIejw0Fu9DoHwNdnRUV6IhK_w8vhrm9VyWy0CEY79LJNESiT9PtL-YL7HqxIUxoPfQ7mismp--ELsmXVRdHMFxnI5mq1QxI5O69wIdL0ouEaTCUHW_6WdWh6SypGec9nrq3w7iHFdxI_9pUQaquhvuejX6QjaWe3XEENOBpEHOUwKC2At55ddPgniNrSxFoNX-C2r7daqryhIXbDUNLzoBKuDdBGHiFmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8ed0a2e8.mp4?token=sf93gX7bu3yHy2Tou6Zr3LEoCu0Ve3JYn6yHA87u_xuT2ff8TKsKq7jMzVMkqKEXjx4EKiAlYnClOHT9DOuUAEL8kRKeudYBCo4pFeWyeaWRhvt-6kl5-uIejw0Fu9DoHwNdnRUV6IhK_w8vhrm9VyWy0CEY79LJNESiT9PtL-YL7HqxIUxoPfQ7mismp--ELsmXVRdHMFxnI5mq1QxI5O69wIdL0ouEaTCUHW_6WdWh6SypGec9nrq3w7iHFdxI_9pUQaquhvuejX6QjaWe3XEENOBpEHOUwKC2At55ddPgniNrSxFoNX-C2r7daqryhIXbDUNLzoBKuDdBGHiFmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو در پاسخ به اینکه چرا خاموشی‌ها ادامه دارد: یک خورده حوصله داشته باشید!
✅
@AloNew</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145879" target="_blank">📅 14:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUiG4HjhtWOSaONOuIzeltU8hb2LIqjv1HNhoCtioD2Ze5pFRXIHr7BBgCumHHTCLhWXGbjW4KtrrrOH4WOEPRc-f6BIWZ-Eg9Kx5-3tiIcbwPPCM4GwAVgL4JBz4vCV_2y15fMOrDWY5jDdEfheFUSc47W1N8rtjlQavtV8LxQbxw-_C2SP-sMJZH40Z9rfRAteT2773r8u-GI9zP49YWmYqhNGQHnJhD35jjm9Wk68M7zaWm3gKEWfVXwtF1_nlQt8FClVOrxbGKScmCJP1mQ6AhyS9Gm4lYMHdjUncRkaeSpJ_ybh-5hiMpPiWND_0hzNgKcvbp2vH-6WTDELQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGnJmATFytT_1SqvkPUwXrjx_pcwRC-2p51eDa6wKm3e0_wpFrJ5UEqneFG1LB-VJKnWMwuapMHI6A_VGABqhIHZl1GgmTzqPYM76NJfwogB-eunRxBo1dukBfH486c-zRNRjeev1NQAtmcDqAylB12boE7MOM5cnO3NIr4HrN2ael5xv1bblWWjE98fqEb6qUd3zpYmiDy47rpxYOGBzY9cOkwXf_4NL4ccju5dKTRxhlXWd6n6LTkjsa3ygf-cz2YZMkcEyebLL6lg2F-Mvdnz_ktCQAwI2MTWv4izuSKiIJkf6KKD1-DO9yiBFFDYSdG2AhrTTxfDn4JWEehWfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زلنسکی در کی‌یف با ویتکاف و کوشنر دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145877" target="_blank">📅 14:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145876">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
معاون اجرایی اندیشکده کوئینسی: شبکه «ایران اینترنشنال» در حال عادی‌سازی ایده حمله هسته‌ای به تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145876" target="_blank">📅 13:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145875">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
هشدار تل آویو به اسرائیلی‌ها: فوراً اردن، مصر و قطر را ترک کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145875" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145874">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از سنتکام : عبور کشتی‌ها از تنگه هرمز علی‌رغم حملات ایران ادامه دارد و شتاب آن رو به افزایش است.
🔴
ارتش آمریکا به عبور ۱۶۰۰ کشتی تجاری و ۸۰۰ میلیون بشکه نفت از تنگه هرمز کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145874" target="_blank">📅 13:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145873">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1b399eca.mp4?token=ldK3NcABxv4exjnZvaj3OeGhjlMIB4ISB3qX2z3YnjtdAXEQPOKEptW0yB3rcFjxZC8CPSo09ky6K2QNG_SmRgl0rV1EuD8TnYDS7lnil6ilb4F6HUFDNgus_eGgNcB4So5-CUMjZAfqAfJQ4_-lWRjab-wiE1ByJ_rUoRlYW9BU3xzwJNl-F5RelNcnhYbbRDb3Q021gC20koQQSE7ZsLzMqTLcNJalV02-En15bDDr2o8TV8t5JnIgfiNVIeSj8VkjvOaqpuVspSHwvHz04xqytJpwkxLbt0E0MqYnOnaiNrGEVaj7UH89idiKcCsnGy4sttVh0sqVjGaWL3TchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1b399eca.mp4?token=ldK3NcABxv4exjnZvaj3OeGhjlMIB4ISB3qX2z3YnjtdAXEQPOKEptW0yB3rcFjxZC8CPSo09ky6K2QNG_SmRgl0rV1EuD8TnYDS7lnil6ilb4F6HUFDNgus_eGgNcB4So5-CUMjZAfqAfJQ4_-lWRjab-wiE1ByJ_rUoRlYW9BU3xzwJNl-F5RelNcnhYbbRDb3Q021gC20koQQSE7ZsLzMqTLcNJalV02-En15bDDr2o8TV8t5JnIgfiNVIeSj8VkjvOaqpuVspSHwvHz04xqytJpwkxLbt0E0MqYnOnaiNrGEVaj7UH89idiKcCsnGy4sttVh0sqVjGaWL3TchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به علت افزایش قیمت موبایل، دزدی خیلی زیاد شده. زیر 5 ثانیه آیفون 13 یه دخترو دزدیدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145873" target="_blank">📅 13:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145872">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d01ae919.mp4?token=DnMCISJ9KzSVf_Miee3uYLJNjFw2tl4iSwO8p_IRRg1os7tM6Ws2Zuh3jkxNTAcmd3_HktSiDvlvu-ge2oOP1yT0jRB3hGI3s9MiUuB0DJfk5Qfu6l5DZVcu9yVOXldA5AONstTjI555NVW6md8MMkoqhj03H9VZjkrWaO0yYW0iX1SYRHWYeEQSJFHLaHDe7FZyHRvEzqKm08F4jYAfvjlOF-wuA4gukiDqnFzbFk8CpmlYBntDn9SgtU4y4nPINugoMzGTkqsKaZiVqyYdv6NYCRfDYkijffss7DaNRFKCnzj2tS68tuu1BTiTZqar3TDfjjuG3r8SYIgpg01gfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d01ae919.mp4?token=DnMCISJ9KzSVf_Miee3uYLJNjFw2tl4iSwO8p_IRRg1os7tM6Ws2Zuh3jkxNTAcmd3_HktSiDvlvu-ge2oOP1yT0jRB3hGI3s9MiUuB0DJfk5Qfu6l5DZVcu9yVOXldA5AONstTjI555NVW6md8MMkoqhj03H9VZjkrWaO0yYW0iX1SYRHWYeEQSJFHLaHDe7FZyHRvEzqKm08F4jYAfvjlOF-wuA4gukiDqnFzbFk8CpmlYBntDn9SgtU4y4nPINugoMzGTkqsKaZiVqyYdv6NYCRfDYkijffss7DaNRFKCnzj2tS68tuu1BTiTZqar3TDfjjuG3r8SYIgpg01gfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی، شهردار نیویورک، با امضای یک فرمان اجرایی، ۱۱ سپتامبر را به‌عنوان «روز رسمی یادبود و خدمت» در سراسر شهر اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145872" target="_blank">📅 13:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145871">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
معاون عمرانی استانداری سیستان‌ و بلوچستان:پروازهای فرودگاه کنارک از سرگرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145871" target="_blank">📅 13:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145870">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTLCqqOyyEujkqc9pRzZbas5P9ttGGq3jryWbdne-zPxLtRCJOVBiexv_C75t3ils0rFHBYm09oHc0ZMn6lttp3ESyL7dSEs_P-pIZMvLnv-zFLPTpC2ilU_fBXqJfL4KtCa-WghflD_4vkRPlj7astyfsaxKIqUtPP4Lyo3CoX8m2677swb4_RAyQQWl7raUKouKCLmysHznVAO7G2V0USKqJeRaV7Snyd5pHBwY1mfrrKanK6MSECJ0I6uUrmmJOr0c3hUBcMYjoXuXdoaeNtLVagzVF-2Xk2VK7xDW_WMnkg75tu1YiHJQJj8Gqb-YtHnJx4sclWZ1OsPyJOvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روغن موتور گران شد؛ افزایش ۳۰ تا ۴۰ درصدی قیمت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145870" target="_blank">📅 13:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145869">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده اعلام کرد که ناو هواپیمابر یو اس اس لینکلن روز یکشنبه پس از یک سفر پنج روزه به بندر، تایلند را ترک کرد و توقف کوتاهی را در جریان یک مأموریت طولانی که شامل عملیات در خاورمیانه نیز می‌شد، به پایان رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145869" target="_blank">📅 13:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145868">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قالیباف: همانطور که در عرصه نظامی و دیپلماتیک پیروز شدیم، در جنگ اقتصادی نیز آمریکا را شکست خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/145868" target="_blank">📅 13:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145867">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
این خانم ادعا می‌کند که در جزیره اپستین بوده
🔴
صحبت‌هایش در صداوسیما هم پخش شده است
🔴
وی ادعا کرده بود به کل جزیره تجاوز کرده اند و شرایط بدی موجود بوده است، البته خداروشکر طبق گفته خودش، ایشان مصون مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145867" target="_blank">📅 12:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145866">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=ogVfYV64e62PgEowM08CBXg-wtOmkVqEaI4vgJJo8zOyCw2jA78UP49j_ZXDAjMC_nqIAyRd1lomYvCSZb4PxD1kav1y1fgXQ60gbUHEKsRhM5ICm0LtbCHWztERGO8vT-UxHPBaKeaG8Qllb2Sod0UuelAkvf6Gpr6hlcrAJKhjTdln4xd1YLSCOsrCsjdw0MfjEzGUi-H5-4XhFoBxyrIun-6fNoeVILG-misAMDcNdPPqrIZ1lB8pgiRIASFmXgGEznbyktmox2DPkdke-BQAZRGa0lBkDUGhHl0vWhuHsUSxxVPAJZBnC2YIZfeqNHRuSjbZrDwNd0Nt4c13-U20hqoT6uFURfCO2uGxo25H8FBQsMbfTcPkiIB_-rqMZnkoOuCun99KRz1ygwsjGDassnMguLo9sulZWNqvYetRRVBATIiTzCPPT8u4m8lDiSsLlONy_R6MZ9CxBkCmcXGj5nJ3dmoVCFPFRwxrzQJNLDWeBzZvfo6OQ4elUSfMTqoDCauzMXXAPl10ivreJExyXsg085Ob_oDaURW7mPpU2ha4vZeWtakc7ncMo1Vgx-wdukF4iGXK0EBnsyD4NWUjekXMFy_Tut1Np1cFNdc77R9twHgbf586R5nmu0OqdCEamElN2SS0tRx0nHxuHzEuI6VuiW5PitjQDLzjklY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=ogVfYV64e62PgEowM08CBXg-wtOmkVqEaI4vgJJo8zOyCw2jA78UP49j_ZXDAjMC_nqIAyRd1lomYvCSZb4PxD1kav1y1fgXQ60gbUHEKsRhM5ICm0LtbCHWztERGO8vT-UxHPBaKeaG8Qllb2Sod0UuelAkvf6Gpr6hlcrAJKhjTdln4xd1YLSCOsrCsjdw0MfjEzGUi-H5-4XhFoBxyrIun-6fNoeVILG-misAMDcNdPPqrIZ1lB8pgiRIASFmXgGEznbyktmox2DPkdke-BQAZRGa0lBkDUGhHl0vWhuHsUSxxVPAJZBnC2YIZfeqNHRuSjbZrDwNd0Nt4c13-U20hqoT6uFURfCO2uGxo25H8FBQsMbfTcPkiIB_-rqMZnkoOuCun99KRz1ygwsjGDassnMguLo9sulZWNqvYetRRVBATIiTzCPPT8u4m8lDiSsLlONy_R6MZ9CxBkCmcXGj5nJ3dmoVCFPFRwxrzQJNLDWeBzZvfo6OQ4elUSfMTqoDCauzMXXAPl10ivreJExyXsg085Ob_oDaURW7mPpU2ha4vZeWtakc7ncMo1Vgx-wdukF4iGXK0EBnsyD4NWUjekXMFy_Tut1Np1cFNdc77R9twHgbf586R5nmu0OqdCEamElN2SS0tRx0nHxuHzEuI6VuiW5PitjQDLzjklY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار محمودی بعد مصرف یک بَست: موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
(چیزی حدود کل شهر کرمانشاه)
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/145866" target="_blank">📅 12:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145865">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd83189492.mp4?token=K_GVfQbbYr4SCqvbUlCcBnXc0BdBvD7dZy7zTUZJXJX25ZeeHtKULNpqMo5eTBCeWTt9czxonY0fJDrW0CeU788MK7BSqfN_wX0oeGKued2IMoZuc8Iy6ErJgccUChSD9dTaJHI_NFiMo8Wc44TzJ0yogAGSuKhFaJV73x7Rf9vSzzPR53lprxJ_7UV6QWO1RePTH-9MBvgAKJ-32sbvC7z6XL2i6V1QKX4sqN7eCRHtN4ZGoPNVWjlpBdjVAr5QWV6WUovj14WwO9nIrZS3nyvot1fweT-vhT72NrvTSc8vqNAEOoLHQnOCnu4cFSOAMbW20-UmZElxOF0iS-7WUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd83189492.mp4?token=K_GVfQbbYr4SCqvbUlCcBnXc0BdBvD7dZy7zTUZJXJX25ZeeHtKULNpqMo5eTBCeWTt9czxonY0fJDrW0CeU788MK7BSqfN_wX0oeGKued2IMoZuc8Iy6ErJgccUChSD9dTaJHI_NFiMo8Wc44TzJ0yogAGSuKhFaJV73x7Rf9vSzzPR53lprxJ_7UV6QWO1RePTH-9MBvgAKJ-32sbvC7z6XL2i6V1QKX4sqN7eCRHtN4ZGoPNVWjlpBdjVAr5QWV6WUovj14WwO9nIrZS3nyvot1fweT-vhT72NrvTSc8vqNAEOoLHQnOCnu4cFSOAMbW20-UmZElxOF0iS-7WUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمید رسایی به پزشکیان: شما کارت دعوت بمباران عروسی سیریک را به آمریکا دادید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145865" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145864">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الجزیره: هدف قرار دادن ناو هواپیمابر و ناوشکن آمریکایی از سوی ایران، «تشدیدی بسیار مهم» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145864" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145863">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قالیباف: نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشتِ مردم فشار جدی وارد کرده و در سالی که توسط رهبر معظم انقلاب با عنوان «اقتصاد مقاومتی  در سایه‌ی  وحدت ملّی و امنیّت ملّی» نام گذاری شده،  باید با تکیه برتولید داخلی و استفاده ازظرفیتهای فناورانه‌ی نخبگان جوان، برای آن‌ها تدبیر  و راه‌حل کوتاه‌مدت و دائمی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/145863" target="_blank">📅 12:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145862">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است/ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145862" target="_blank">📅 12:32 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
