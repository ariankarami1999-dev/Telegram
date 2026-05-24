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
<img src="https://cdn4.telesco.pe/file/aQK5tnMMF8zRpzGEvUDSLaf9u8hlIPjuDaulWfYFM9a4bDy2kbxBlGTSCiEzGLMQuMJOBHjaFCYCScQ8Reb48XS9iEcGKUILJdx-gJYkKZqwKTkYgr-sc-wr5cS3GeB0VDWRUaFJBHLvqacvK6XE1TbAO_SFhJpHtNQJMUyczdp5JIa8C6YHNmcUDzsBItkIg52RvAnya1dM4GZzr3nH5JE0LI80OVQuDU3RO7rT-3365Bfo64gbMJcMHLEtdaOP2RsvMKYfiJH0ngE4ubUtHg2Q0eI1lkWgWnDk3A7ApgjbW18Ge_7544UXsU9aNCS6k0iq9ThMyeMzQXOSc0fxZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.91M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 09:05:40</div>
<hr>

<div class="tg-post" id="msg-653785">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN7fcv7HgsREfSrqv2jm-XbgicjnhYZAoAG0VkD0JbE5UsJ2TG8fqwiOPmR6lQF5nA5B_RM5HL_ZbrGosm2m_70nzae19V4YIBfwCs5GJfhnpVUYywTDKTD8Kr-LxarGSWb6wdUJHuZwTnDdVyaYYj1rMfnvSvCXl_yZ6KlxumE3qCM46EaYmhSqSKHkkXy9iMQhPKWzORoWlj8qW9hTnPBoHD5cEWNTHfKWhAStaCr3DHBpXodJmzAKq6uNiWTDxMIW2pfR_0ztI4-fSQHwGgBxn8Jfu4end5LC5nsb3aKGEzXmr0Xzo1OGYPMjF2Bdca9-mv4m_CRzOpxAqbO8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توافق خیلی دور، خیلی نزدیک/ تب‌وتاب دیپلماسی برای مهار بحران منطقه
🔹
در حالی که خاورمیانه یکی از حساس‌ترین مقاطع ژئوپلیتیک سال‌های اخیر را پشت سر می‌گذارد، همزمانی تحرکات فشرده دیپلماتیک با آرایش کم‌سابقه نظامی در منطقه، نشان می‌دهد پرونده تنش میان ایران و آمریکا وارد مرحله‌ای تعیین‌کننده شده است؛ مرحله‌ای که در آن، «توافق» و «تقابل» تنها به اندازه یک خطای محاسباتی از یکدیگر فاصله دارند.
🔹
واقعیت آن است که تحولات جاری را دیگر نمی‌توان صرفاً در قالب «مذاکرات هسته‌ای» یا «تنش نظامی» تحلیل کرد. آنچه امروز در جریان است، یک معادله چندلایه امنیتی، سیاسی و اجتماعی است که سه ضلع اصلی آن را «میدان»، «دیپلماسی» و «افکار عمومی» تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24 · <a href="https://t.me/akhbarefori/653785" target="_blank">📅 09:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWN08UMx3pNG3noDryPk7AD8ykvvfmE52zy1pUtOF6rmq77YTcfQkR-TaLD8F275hZ_5NV1vGn_0PIT6U57SWcoZYEvGxx9lscffMxVUHMZk2oAXfF70tYNkspaYn_EjPVxUjOBFiOveQ2ZVuarX0afuuAzy-CVrZ82DSCttg792GPwbGnJbJJs8FJOIJD1L1G5O2AFYQAXgmZi9GZIG3b_tG0Q_Cx4UxJeR3lXz_MqJOrsMO55JdLG82oo7SAuCJ8TD1L1WXz2JglzZkf5IsahjrREFE9OktijO4a4Jnqv7j16OPOSunEqc9WvWtsx5ciPB_70gDUGVwzbSx4M-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مشاور رهبر انقلاب به‌مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 340 · <a href="https://t.me/akhbarefori/653784" target="_blank">📅 09:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7ytKMJb3eSO0NdaW-t8dCTvG8rnCZdIaPZ-HXu4gVo9r-VY8NVpaiBgXrsi5xecUyxgEnaEWnKHwX62ILBCpMXnBeD2qhsAgYeYYb7B65GMXgrTF3sJO_LHosYC8ll4urU3WDAa3LDPSi6yXfE7q5JfmT_dkxKcjQDz2jwEjss8ohM1Y73G82P_8ox0zcQmqPGORtNSs85o-iOaUXnEfTYnkM3QMzfyQ7Zli2edrPHPRy6nDaCXOoxajBBawuoHj3L_s6haqPG1P9P-rg8F9pt_hms_zdyjwE-LA3OdT7eGBQQjdUJgeonrwp7N7uu9uO67pb6lXdaTPUs4N3Lyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pO-XKrKUe3uDpQZRUiDL8SbjL6XBBQhkLG6MC5EMyds4TR-7Es80sYHrULHycOE66aZMy0q2aokPA0xBJF6Nq3aXhJIwje8kcStxX6v1rMl2WfEc90JqeeBS1P9Mjl9MeR3__3Gzu4I11WELEYomeH_FYMe6tXJ4rYpETp9lYGmOpMfOSCUmHdlCKHMVZ-N0CJhdPcqgzEbGLXG8JyqfB3fC6VT77Mw2TFzMegiIKIUUpzYNaJXhy6UVp13dWx8vI3kgSx2PiOwJPZJWPdwdKnOeotY1LN1p06crTTJc_ehCom9HzpDCxp5b233POGvNf48ee3m2A7Zhcw2eKwhlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQE8yBXqsY2zUc9reqaO3lnFt6WYbLBwpzmkmWpcj8mKqNoLraxdbuCuoXdaDGHDwZX1gcSuLoBystXsn_8y94IxoZlqtZPBFZLPbhpTVSzXKl_Lm9vdW26DbHcMlx6hoCCvfstpbYKOK_rJdJ5QBOlIvWMp-7gOzl0n28u7BsTf1hZK6NMo8k9MISuM_mulkFytddvd49wqOi5iMkx7bRzBBS4hZQa61OTsSVh3LWuTlqcdHGSLlafCsNuQEjv1pUy26EM66N5KMphqoGx8PQEjYZ_MSKNp02DD__R6roRgoWiIDHuSsUD6ReL4Q4nteY8VmXO5dpsXqH3AFkUDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1HdOCgl6HjQiUwbrKJbH8Zmf7YLUT6sEr8pIB1i8Sv_fLhKatDwKXOaThW9EPATzsrEyi-1wtxBOFZZFWvbtEZbI554dwYvTCoUidReKCKf-ikbftRjLGOkPnoHV42l4suxTcQuPSDsNmzSw65UgHoaVwjNAu9S6_M7OnIC-Z8Nc1k6nclJWaWTldZLrp2ceJ1d_g-RQC9CVkCKsSYdGgFlaKZUkU6rOPvxrK2oiT8NTUold8t0WOI-rJLJAlNP-iRTzlCIbPND_byyWQ2Gbxs501KgompuBYSo8qzUKFMiACOTdZbOXkhoQU-4nsxBo1cYkM59RjWZWhdAhEnTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoTbEbIrt47QXz3fiZmVPIRrXAJlX5ik3StbIM8Pes9xEjGIjJSN6D3HRuOfWSQ_idYUuHez0t6n6D4VutBcdfnKOgcQ5sTdgf8t8tm4mtPkvFUR1N1Yr_dBdY0UAgFourv0VXVrfeis0qAF9Y7PEHwLB_wfOMgf1z5P9kHIvU7_Xpzh0zcUitu8WT5e9ujZ8Xo6YTS8wNd5qiYuCDGN0tftrXbu5toZdeaP0-SvLNGmt-m2oV1scimpJCAXIsson1eB7X_Qzx8rBehr7iaAtpxjyok9oeuYpaBui_MCWF6BxRRrbfS2auW33XiyUCXRk8K7IaGkcOuMPckq2TNhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD-IwrVZkpIcnxDJYDYCbHpI9to5C2XBP7lC4hrLyE0_6Q16qfy6Mm_jezAk9_OYMFxIl_XgYZMaZ6jlsf00LYnAXc5cG27afs9ceijNfrmw1hWQZGaufq5NA-ylJHswyEGQ3mluJXj39JPHgnT_7oTSwlQU2IOTcLdnThS14hADeQ5hMUZoS49Mcs4sR9ffzGZ9u8FzmZT6QxeFv_ntvCJZ_RZhNhr2az60rGnrCZ19bC9DopKlbTvFzhykEAnTRd_Qx_m-iMOMG0O0JX0FdZnYBcpwNlAmRqkMQwPKJBKZXnZbTRlEJFtlVSvKYhGXLFzLKJdrStKjLBZv9pRqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBmAco8K7548rf2bTq7e3SZZwAXAVfaLmA-Gn-_uNgFcX4vMh_Op3hG1IeT4A1FU_z3ob8-hLvUI8vHl-GFFvsdJgAgAwvgyZCf3SQA9oxXsKSizKlg8mJ38pVMiJsNUHg7x9iQOkCl4J3IoNzjO5XyEEKPuCZC0GrENzQ4PkMWC9Fjpu0w5z5WskoD2clsHAE_EA2-IEAeCtPSUu-rJbhKv-m0iFC0apDLSLdLA0--Q4hFTxZbsPuEHvQpYWyv4IKlBqcUdwpAoAD7qUGqyjG6PTdvhoj0a963ojLXv5hRcqGq0zDZgvRH2pyH4n2KJV9cbNiEUehHXiQITHi1zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAg943c5wnLQ5mPOhA27OiLa_pU6HXyjxH_zT-XlSDJvAu1H-O2N5yIQki4JUV5kH-pWiKuTZcpReEsnYPw5iUvCbGFt8SccJFfpcyBW6CDX5LXkddGjEvfufI14pl38125lazx7LNqJZekSMP6S3W3PXKVxDL8N6NuzlKQNaRV4-q9ayA4YZWjiBTYwXZHM-wLvxyr4aRGrk1rURuxi7i_kp8nUzIk8tunGXVVJu2mlW14pPpAdXTGpNKFDSWU_kiqSW50zIzmjSz3wJP3eGCDJaWWudr_-eR93AF2VewbNlS9S8EHwKce44M3VuW_zqhv8fEw320-lBL2OY6xsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YY20fxHyfVxQZ0sa-DLnegiIgxCMpb9HAcQtoKtCjAAXOIwoB13KiCcEPOzPOrjcNO2O2vsnnkRTkD-nUpN4OUQ1qDSG0mw28WK6B74v60PirHxs44-J4ysiROmxGcmrAHAnDCtl3IHXDfq6xy6OovpChyU2HKLqnzs-vmUDqsL2YaUcYQ8rxhAycHdp5_KYGM_Em3Dcd5fxN-Xep7tZTRBV2VaEXPfR0RVD3FCgXKE9oUAEpHJxgwyC8LVinklO0jW6_u1LwtiQnoyCCAdjuqexGIPBEUIPiZ0aKFfoXtBviOf6zfqcpS6Iw6R9-lbMQXcV4Cobw4dRj4tSDsFmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzfPdWV4azRHajQCLenaSl3PwOwjvRX77E85_hpyi_oqkXqeTRJ7ILczScGfCKifkSJBKdm2l9wVa2LfZ-GQk_xFmkmHNXiWDyrcMJKa2dSShwOhZi3WaMlbBuFIAK2_z92mzc52SZYAbWFssgb5hluCZdRU9AhyDEdMm51ao6zdANX9ubfyRp_D7q_SL51fNEOY8UYwoB5LVYhTGeC1NM6K-LKQ90Bf7jkbRmDcK4X7id6Uq5LUKM0XylpAW9lPDj7jvgWmztZZpH7MZyQ-MMg_Z6b3X2gqbfJ2McI1RBGr63EJaDLc3q8CrgRfhrsc5SbDyMUph2Xsomo9OyDHTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از عملیات آزادسازی خرمشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/653774" target="_blank">📅 08:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQTNfNLFZ5QmeAndWYfsEh-HOXxy-XEkmFCA5SR4fFACB1mkBlIhmrnH1CY2B--ogTNp_VuCxUITxxFLz0RbRUkSTicq1YvmAJ02T-GYR_0MUb5lLrps9GKEUV8Rsvdg_TXZZCjDX8xawt6QBzkOxbW-bpyKaXfUtv5HXr-Z4CyG1CuyCCXysPkDZNFARGriSFckftXgGpulHRW7EScYoib_r3qzSV4Pe9NZgmIPQ5EE3Hq2GalXP5vBIfcIdrg-O5TC7e6180Hzq2JmnJ9oV51RKQR6ImT_-lFiWjkyvCUFZ4dbXoKqcupiZOOY77BDvAe7MgZ6HZ1wTRpXmkf-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مشاور و دستیار مقام معظم رهبری به مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
🔹
دکتر محمد مخبر در صفحه شخصی خود در فضای مجازی نوشت: صدام و ترامپ هر دو یک خطای راهبردی مرتکب شدند: "نشناختن قدرت ملت ایران". اولی در خاکریزهای خرمشهر مدفون شد و دومی در باتلاق ساخته رژیم صهیونی به بحران سیاسی دچار شده است.
🔹
سوم خرداد به نظام سلطه یادآوری می‌کند که سرنوشت قمار تقابل با جمهوری اسلامی، شکست همه جانبه و تمدنی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/akhbarefori/653773" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOXLxtH0uf8VUyp8jWtFdV6N3IVVp5dpu4fSYdCjKvCq7IpThCoYYZ5AYS679dPz4lZGcrZLb4lAXm-be515NYQlgoT_AcCRWvncFETY7Kx3nUdliPamST5tImZabk74stG5X3uedeoDG3mxnULNhjC4kheBnrL_5p7alY24AI6jQez5nfiZAxbGqzNI27HpDNHVZaFtby6t8IUfiM9xmCZS8T74vHrZTU5LE0dJ3vEWSuu2cN5eYl8n6xPrAspmNxxLnBtB3caAd1jfMqXGLsyzoWBGBSdUqszTSiDpGbdQU6O2krxBCgdpaVoN6CPa4IHP94zoTa93b8vpu6WkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ ایران، کاتالیزوری که بحران پنهان واشنگتن را لو داد
🔹
استعفای مدیر اطلاعات ملی، برکناری رئیس ستاد ارتش و دو دستگی روزافزون در حزب جمهوری‌خواه آمریکا، همگی نشانه‌ای از یک واقعیت تلخ برای کاخ سفید است: جنگ با ایران به کاتالیزوری تبدیل شده که لایه‌های پنهان بحران نظام سیاسی آمریکا را برملا کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/akhbarefori/653772" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شبکه تروریستی در فارس متلاشی شد
🔹
روابط عمومی اداره کل اطلاعات فارس: یک شبکه آموزش دیده متشکل از عناصر آشوبگر و تروریستی در این استان شناسایی و متلاشی شد.
🔹
در این عملیات ۱۵ نفر از اعضای این شبکه آموزش دیده که در اغتشاشات گذشته نیز فعال بودند بازداشت شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/akhbarefori/653771" target="_blank">📅 08:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO7UUCy7Fu66gBmppUnNNtUoIOVrLAStEor42F5ZTNouRkKKIDfgdCshDpE6c527ZhRuhsKM9g5YDoqshYqb4Qa1vgeE0GoGG_3SJRt5ugN1QdmCpOgb5Xhg17iEP1Pvu0e5EDuiIFHgbpuWYgFjtjR5U03XL2ewXNB_AEum5R18xwKwkNsWTMScixFHXB1peoJ_vXJy6sLlJeclRK6rWK5QviI7zyJ_wygdi7pJHor-Oha08s55Qtimnjw1ShklEFatIdHwrePievnaYGb1mYAg6nAfIVv29vQh9YEyeXwK9mrXdChuRxqdS9hGCCwZ4Wz468BZr2n7Yf7r1dgD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو نظامی دیگر اسرائیل در لبنان زخمی شدند
🔹
با گذشت ساعاتی پس از اذعان ارتش اسرائیل به هلاکت یک نظامی خود در لبنان، حالا امروز این رژیم از زخمی شدن دو نظامی دیگر خود خبر داد.
🔹
ارتش رژیم صهیونیستی صبح امروز یکشنبه اعلام کرد که دو نظامی این رژیم در جنوب لبنان پس از انفجار یک پهپاد در نزدیکی محل استقرارشان زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/akhbarefori/653770" target="_blank">📅 08:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRHQ4C2_tvYSQN9e3h9ybiOJGkTM-sC81l3Na9ORXwp9ohjq8dkyKjsP0KgDGsaEt8F_mu_i2RUyOgCMsfVmv5Q1MGSaOwxJx9nfxVR84fBnvGMlckqdjJrGjiVKFqAwDROWSAUxp1FkAIPev9Hhw__0CkVcWifFqSzuUGwUljoBiQnnUSjetGhncp2uuUmRKFLr68qJ8q_RePgg751K_EgaW966ywBNbBMMECrkfEslbQzRbgo9eM0jApBx1HA0UwEqFRbSY_DKUZnJqLa8lFvftavBLqPSGEK2yob2RGuwtrBHI3Lriy0TnX2fgJLlj9r-cNF-iZhVflpIiCRnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر ۱۷۰ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/653769" target="_blank">📅 07:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5XRI5xIAqAFaTn_PMII8uXOXoGGQ467ivL4X0Pvh2qkCPXuItmzRF-1nF3qjs64GbyTyyMhyVSDk4d25abFlW98msj1v5UJO1YOb4jtRxobOZHGPIVIX2HPbC_8ZsTSHu_7Z3AQOK7NMlSKTpUz2Zc5UQLFdFw4102yEakC3THnw5oerKkQIv-DTZl41l_RMFqvRgcbPWMAPLqE2ppXwSjgzJ5TMDz6EzaNd6qBqSI6kM8zqI75aRliTPth4Dm4UNP-n7BDRTnFIhsFJHHQfb6YvEBLG2bzFm85wVhOYPrPv6LsHsKZfSKyaroc7Q7xg1fgP35OlktqZPu4JoE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: با همان ایستادگی حماسۀ خرمشهر، دربرابر دشمنان پیروز می‌شویم
🔹
معاون اول رئیس‌جمهور: حماسۀ آزادی خرمشهر آموخت با مقاومت و اتکا به توان داخلی می‌توان از بحران‌ها عبور کرد.
🔹
امروز نیز در میدان دیپلماسی، دفاع و سازندگی، با همان ایستادگی مقتدرانه و تبعیت از فرامین رهبری دشمنان را به تسلیم در برابر ارادۀ ملت وادار کرده، تحریم‌ها را شکسته و بر دشمنان وحشی خود پیروز می‌شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/akhbarefori/653768" target="_blank">📅 07:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9HzqV7rdmXx3zmr0AdvTV04Mg-vHnKKd4aR5de8a6HJzKLBc4NvavOj2cW6LcdLw711lyVHJ9tYu2yVh7ZS72e31Ad1YWjDNWmE4dxu1h6HHUv99aW0Ia5q6_PqVXGH8rl3_-1wrk7ERacEZQO6HbGwludBN1XR24j2JvwWswDDZ0gFCufIzh8MtCCJeJ_dwAEfQpSuZ6qIH_r25wGYqOv3m9nku8oFHwjazSP-5eyHou-3YnW0GUCe0z101HIxX2412s1g3O-gFvJ4DFZwYseElJlauBwHy7ti65iuVYgUjKSSfwbQPq85ZP_6huOtn6Fg8N762Y6Cqi3g2_1WtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن آمریکایی ـ صهیونی در جنگ رمضان به دار مجازات آویخته شد
🔹
مجتبی کیان، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز، بامداد امروز پس از تأیید حکم از سوی دیوان عالی کشور و طی روال قانونی، به دار مجازات آویخته شد.
🔹
طبق تحقیقات انجام‌شده، نامبرده در طول جنگ رمضان پیام‌های متعددی را به شبکه‌های معاند وابسته به دشمن صهیونیستی ـ آمریکایی ارسال می‌کرد که از جمله آن‌ها، مختصات و اطلاعات محل واحدهای تولید قطعات مرتبط با صنایع دفاعی کشور بود.
🔹
محکوم‌علیه در شرایط جنگی، در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/akhbarefori/653767" target="_blank">📅 07:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌چهارم - پادکست کافئین</div>
  <div class="tg-doc-extra">بی بی مریم بختیاری</div>
</div>
<a href="https://t.me/akhbarefori/653766" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#پادکست_کافئین
🎧
▶️
بی‌بی مریم بختیاری
🗓
وقتی شرایط ایده‌آل نیست و قدرتی نداریم، چطور تله‌ی فلج‌کننده‌ی «انتظار برای حُکم و سِمت» را بشکنیم و در لحظه‌ی بحران، بدون کسب اجازه، رهبریِ میدان را به دست بگیریم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/akhbarefori/653766" target="_blank">📅 07:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8964485f3d.mp4?token=ao5abePbh0qZkBOd8onXI1UVhZxz8ytGu_BH1pJNgScYUmWtXo9r68ZyIOMOznx1WyE84PaOgszREANONhCkj-QzQ4gG84Ox76VnATs0AAAjzAw0x9pcdMi9NonSUlSe-iPvTDbDfq1SQj9Y_oBjzEbLfrFbeE1PzO7GCXCBh53uPhw9YlkcbdACtWGsw4moovLAKlgIDdlVRnsS6uPpXqq3u-7rz66e0glws4pBTOsS9zFzBIFZqyz76m8E-kvmAw-HZmH-5h4PQoeg3o8o_5Es_oHnZT05N4W1k51rHkPdvImzCWtdIJtaMel9yVIDrKJqNFLy9k84BxYzE2BErK4RXKs6CiGUddaKU1WnjjM5MQv--S4S7V4p_TjHCPCmnc-aQO4CZOZm6_ybWvuRgBTW5PP4-cpz5AE6xk2E1ukyuoaxH52Nmgo9gIKL9TaIH5rGTGpt8yBa0bdj5rvasEo7UnHJajLC2bvlruc1ggBIIM9_yXcod896nyCmb4a0OFbbCw4wS5arq_i5WQqoSFkA7fB7la9D7F5qo78YvK7b3I8ng7ayoVAHTTepjpNJ_chWtRs_P3Kd_5AF4xHfiaKsYb6qxNXTtVvd1mMbcCmmXYk2yJj42vAQwtj5Y4FTmvFvAKtPk4LHpl6YjZMN_gk78YgzaN35ULI0zHwqiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8964485f3d.mp4?token=ao5abePbh0qZkBOd8onXI1UVhZxz8ytGu_BH1pJNgScYUmWtXo9r68ZyIOMOznx1WyE84PaOgszREANONhCkj-QzQ4gG84Ox76VnATs0AAAjzAw0x9pcdMi9NonSUlSe-iPvTDbDfq1SQj9Y_oBjzEbLfrFbeE1PzO7GCXCBh53uPhw9YlkcbdACtWGsw4moovLAKlgIDdlVRnsS6uPpXqq3u-7rz66e0glws4pBTOsS9zFzBIFZqyz76m8E-kvmAw-HZmH-5h4PQoeg3o8o_5Es_oHnZT05N4W1k51rHkPdvImzCWtdIJtaMel9yVIDrKJqNFLy9k84BxYzE2BErK4RXKs6CiGUddaKU1WnjjM5MQv--S4S7V4p_TjHCPCmnc-aQO4CZOZm6_ybWvuRgBTW5PP4-cpz5AE6xk2E1ukyuoaxH52Nmgo9gIKL9TaIH5rGTGpt8yBa0bdj5rvasEo7UnHJajLC2bvlruc1ggBIIM9_yXcod896nyCmb4a0OFbbCw4wS5arq_i5WQqoSFkA7fB7la9D7F5qo78YvK7b3I8ng7ayoVAHTTepjpNJ_chWtRs_P3Kd_5AF4xHfiaKsYb6qxNXTtVvd1mMbcCmmXYk2yJj42vAQwtj5Y4FTmvFvAKtPk4LHpl6YjZMN_gk78YgzaN35ULI0zHwqiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی مریم بختیاری، سردارِ خط‌شکنِ مشروطه
​
#پادکست_کافئین
| قسمت بیست‌و‌چهارم
☕️
​در این اپیزود به سراغِ زنی رفتیم که در اوج خفقانِ استبداد صغیر و جامعه‌ای مردسالار، منتظرِ هیچ حُکم و اجازه‌ای نماند. بی‌بی مریم مخفیانه وارد تهران شد، رهبریِ یک جنگِ چریکی و شهری را به دست گرفت و شیرازه‌ی ارتش استبداد را یک‌تنه از هم پاشید.
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
​از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=pSS41rtTzorAVCrI
​
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/653765" target="_blank">📅 07:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQMxNYrRXNGim73sfJoeNHu6M6fjcmgQ4rb-9DpSr0Ydu5ZmBgQulelLcOQ9IxsfS_kTE_uPXqG5abP6rdKQng5RI2sJNcgVVEMCiJgBjj29ScAib2CBvxNUiyhbbCVfYQ-VnFKzEhtQR8wRo0boi4avzggkJNJsK40rnjLPNUSwA3orFPha2WBcGc4lo0ZcXb15NwwjltbtsW7MxJvOFORE-8xmsUynwpK8uuCBPvi73TeHfmr1l-76OkBEe9mLyaeEoG8q_NjbX_VCI6VRd0kcb-mobQX_3dkQat4DDT08xk9PJOLsaaCCbgVZf79nXUdQx0ocnfaiEMw39FjyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔹
این اقدام ایران را دور زدن مشکلات عدم صدور آمریکا توصیف کرد و نوشت: ایران با انتقال کمپ خود به مکزیک مشکلات عدم صدور ویزا و تعلل دولت آمریکا ٢٠ روز به آغاز جام‌جهانی را خنثی کرد تا راهی مکزیک شود و تنها در بازی‌ها در آمریکا باشد.
🔹
نوشت: ایران با موافقت فیفا کمپ خود را از آمریکا به مکزیک منتقل کرد تا با کمترین مشکل تمریناتش را انجام دهند و در آخرین روزها با دریافت ویزا در جام جهانی شرکت کند.
🔹
این اقدام فدراسیون ایران را نوعی ترفند برای به حداقل رساندن کارشکنی آمریکا در زمینۀ عدم صدور ویزا توصیف کرد و نوشت: ایران با انتقال کمپ خود با مکزیک مشکلات عدم صدور ویزا و بلاتکلیفی را حل کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/akhbarefori/653764" target="_blank">📅 07:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
روایت جالب توجه یک پزشک عرب از علت بمباران شرکت‌های داروسازی ایران در جنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/akhbarefori/653763" target="_blank">📅 07:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpOeP8lHDi3iCDzSlLwm-5z3nSh_IWKNoRjQHqUT6j5MJ29AVVzV-tGsd-UEF6bmHINJWkxRKshsAw-ewRXotvHcRmZGQhtIu3QeUbQCDQHpwk-DldTbIwcvdaFht9aX1ua_p4eNg0p6ZlnFIuvHWCBoq3apIuxQ57ahe03--otKpyqLi71oEDiixd7W6XsdHFICUnWADGw7kQrS1eoy-wI9AndSDzG486JT7mjppw73QFX_tVzzogWA6ulDafDAx6PF8lnBcdYus13XRulC_XMjC0BM-la-rVnnlp7CYTOT4n9stEpwShXdKbSMlY7on2JcdD4VRx-OWM_mCd2-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۳ خرداد ماه
۷ ذی‌الحجه ۱۴۴۷
۲۴ می ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/akhbarefori/653762" target="_blank">📅 07:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO5LOrpMbpCskL1o1BT4Ps9YZBUIo9kqi8mLKoE-aKNdO5tF_xeURzGLgEXUGxNelep-ToS9sZw1HTF3Fy96jKcYzBXbs7uZXNTYTwXMYseFVMWZM_Gu3hj64JgLy21Zq9p5gTLth-J9TwB5tIbFsZxjZfVBLY4XDPBDb08D6-7TPsG-FODl9VG-FA7-agQbZKh2tLy6z5on5o0UeJ6yOa9Yg6GkK6oEPRbTWgESBkGCMYAlVoVfZ4Fgzj06n6Xaczh8Sevy2M2pBtejKscD-K4G6IyUdBGasm4o-KKVIrUeNo5vr3FsK2U9uyQE9Rv_EWs_GEXhJgh-j0WySNkxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروژه تازه واشنگتن برای خلع سلاح لایه به لایه لبنان
🔹
لبنان این روزها در کانون یک بازی پیچیده قدرت قرار دارد؛ بازی که آمریکا با سلاح تحریم آن را بازطراحی می‌کند. از افسران ارتش تا معاونان ارشد نبیه بری، همه در تیررس واشنگتن هستند. اما هدف نهایی از این پروژه امنیتی-سیاسی تازه واشنگتن چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/akhbarefori/653761" target="_blank">📅 06:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xje4of36H26mnXzGSJKP9MrW1ge0_fD1D4Yg0cZBF39rRZ7xtvGsevWGrwFTWfdupdT9QmMQOA7QnnsL2SDZz2n4N7s_KEFssI0zumZtq_ofRX0mpFhoh8qWSaTTc4-8cL69rfs52coIqQTgvRuNCga_4Uz9826GvUa82GjADQNyjiWDH9RkIEINF93ALmxqOhIdIf7XTN9YzaXUpzx7KlPWqCA4nKFe6XT8QrywKDpLb3tINmIg_ybjjI01kdmSy9OSrPOZqdXlnGKjbY_6WT78yG3f9f4kPePdp2Tn-2jSpeUMrNqiqGYvjoaaFxYn2PLD1XeBclG7TppG_hkbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر خارجه: ایران منطق صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از استقلال و حقوق مردم را دنبال می‌کند
🔹
غریب‌آبادی: ‏۳ خرداد، سالروز آزادسازی خرمشهر، یادآور حقیقتی ماندگار در تاریخ ایران است؛ حقیقتی که با اصول بنیادین منشور ملل متحد نیز پیوند دارد: ملتی که قربانی تجاوز و اشغال شود، از حق ذاتی دفاع مشروع برای صیانت از سرزمین، استقلال و کرامت خود برخوردار است.
🔹
خرمشهر نماد پیروزی اراده ملی بر تجاوزی بود که با محاسبات قدرت‌های حامی متجاوز آغاز شد، اما در برابر ایمان، ایستادگی و خوداتکایی ملت بزرگ ایران شکست خورد.
🔹
امروز نیز ایران همان منطق را دنبال می‌کند: صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از تمامیت ارضی، استقلال و حقوق مردم و کشور عزیزمان ایران.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/akhbarefori/653760" target="_blank">📅 06:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0sTnDhGANzAFFXBUU_pFEIUMwPEQEUulbTo2ywpAerXpJgDE-SDxqahIG93VJ9Nc54VYBu92P58fhOKZLlqqqc5jJiZTOm2V4Qot-vx39zW_Yh7gbDOiBiYwiyphzq_o3R3ZopjCSkG8Duh4rCbwYO_2yQeYcL8mcqACYqLxX5_tff914N9ISG2FadUwBnvjV3VtjwxmJWdLS7asqALpwrXmg1jCVnQUD4f8npp2L4YWGHhttCVr9spRvBIgaDHzOJJeMbC3eng9l_fvaWbpQ9730TVoo1Yh-eAMj-S-90jUOKMM4jYKPxrkEizCenw_Pt5Oaq4eEsgWibcMfV4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم بیمۀ کارفرمایان، و محل حقوق بازنشستگان تغییر می‌کند؟
🔹
وزارت اقتصاد و وزارت کار به دنبال تصویب لایحه‌ای در دولت با عنوان «لایحۀ ایجاد نظام جدید تامین‌اجتماعی» هستند که بر اساس آن حق بیمۀ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد.
🔹
طبق این لایحه سهم حق بیمۀ‌پرداختی کارفرما و بیمه شده برابر و در مجموع ۱۴ درصد خواهد بود و ۱۶ درصد مابقی از محل درآمدهای مالیاتی تامین خواهد شد.
🔹
همچنین کلیۀ منابع حاصل در خزانه‌داری کل کشور جمع شده و حقوق بازنشستگان از خزانه‌داری پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/akhbarefori/653759" target="_blank">📅 06:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از سرویس مخفی کاخ سفید: مظنون حمله مسلحانه در نزدیکی کاخ سفید بر اثر جراحات وارده کشته شد
🔹
یک مقام مسئول آمریکایی مدعی شد: فرد مظنون از اختلالات روانی رنج می‌برد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/653754" target="_blank">📅 03:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sklOISk34FRkvHux_fOBFbLLiUxelS28xCj3rii1Zvf-nDyfVNwgnZBCHl9BZvPEAy86OcjkY6L43Hfr2XpJpAsR7QMPmTAYHCdTOXKveYYxSdlqjXes3yjpaorKfjQ74ydBBjwyxl0Zu4KegtYWMByEwfYC4RowkI5fYwVD6yALo7ur8qTo7ioh_mQtgAtZYIfI5odSNYG2QxxZRxOVhiUlYgTPyNWW1TskuhVZbMfFgoQYwz8PVf1nw-A3tNxf_gUWcIX3PKr3DZ2XXgEjOmg3fim_e9Pnya77SopP9bXwlkwUsJpjtYAyye1yeK-PAfW8pshu79tlOlC6adh1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک پمپئو، وزیر خارجه ترامپ در دوره اول ریاست‌جمهوری و رئیس پیشین سازمان جاسوسی CIA در توییتی که واکنش به خبرهای مرتبط با توافق احتمالی برای پایان جنگ محسوب می‌شود، با ادبیات و ادعاهایی که شایسته شخصیت سطح پایین خودش است، نوشته: «این توافقی که درباره ایران روی میز گذاشته‌اند، انگار مستقیم از دفترچه راهنمای وندی شرمن، رابرت مالی و بن رودز بیرون آمده: به سپاه پول بده تا تسلیحات بسازد. این حتی ذره‌ای هم «اول آمریکا» نیست.»
🔹
پمپئو در پایان پستش، آرزو کرده که ترامپ دوباره به حمله نظامی متوسل شود و ناامیدانه و همراه با فحاشی، با اشاره به تنگه هرمز نوشته: موضوع خیلی ساده است: آن تنگه لعنتیِ را باز کنید. دست ایران را از پول کوتاه کنید. آن‌قدر از توانمندی‌های ایران را از بین ببرید که دیگر نتواند متحدان ما در منطقه را تهدید کند. خیلی دیر شده. [برای حمله دوباره به ایران] بزن بریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/653753" target="_blank">📅 03:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
به گزارش فاکس نیوز یک رهگذر بی‌گناه در جریان تبادل آتش بین یک مرد مسلح و نیروهای امنیتی در نزدیکی کاخ سفید مورد اصابت گلوله قرار گرفته؛ وضعیت او نامشخص است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/653751" target="_blank">📅 02:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6JufmQLlPMYh7yMeT-g06uSlE2YpxCQkLGi26yh7paXn9Yp2IQDaLjoS8kT0UaOWFQBZsTpKAIj2Z4BIDZ4P5GsaaYGEvTXEwyg11tr02gL5rQPGRpEyE8_MSjbTWdOHOdM4GlM2jmNJ4-XTgx29mnIIRxdAg5PGJuWgdRj4ACBTsdpSpNjjhqVLl4LUffreyXy6MHNlMbZqqy8oTcjr5DqsyDMKwBAxPJp_WFIC0bcs5Mqu-_4e_ReUvkar_L_HaGrdvXSSYjQ6U7isOjNrds02nkvISTv57AkOPE0Sm7S2dsOUkyAqUuxluT2W0ONmmqcFiRstaFAga1K71bfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ یک از اهداف جنگ محقق نشد
🔹
رژیم سقوط نکرد.
🔹
رژیم انعطاف‌پذیری خود را ثابت کرد و می‌تواند به اعمال قدرت نظامی فراتر از مرزهای خود و در تمام کشورهای شورای همکاری خلیج فارس ادامه دهد.
🔹
برنامه هسته‌ای حذف نشد.
🔹
اورانیوم غنی‌شده در خاک ایران باقی مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/653750" target="_blank">📅 02:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfbEj-MKxqK2BuaTxjdTgsCwNL2JVEpR9kc2aiDJ63ETQ-NTHuDh9ZlHar7XAez-8OywgYmo2hVXzA5othSBM_h8g72Awgfu64Iz4Kwe02duzg1aDa2VMFQm-DgvCGWt7wJ6ZXqSRRkZgxzSRRG4v5TvWG2Y8Ua87ir50jW9AQ6GGyWZikzFr6_Y_-NLIU3n4ezhve5MIxN62r9MdMaxEpgTywdafA8j1YxfrArA-j9GTq07fAPQ-SffjmvwbrG98HnjjgbUEuYxkp1M0TkO5l1kesQJZMxpzmU9l7wyLQvtubKoZQuPVPFscrm6ET65w72GIDQhixPmqXiFCh0v6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر جزئیات گزارش‌شده از توافق ایران دقیق باشد، نشان‌دهنده یک شکست استراتژیک کامل است
🔹
کاملاً خیره‌کننده است که چقدر این موضوع ضعیف مدیریت شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/653749" target="_blank">📅 02:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b19166e8a.mp4?token=R8alKSb4fZ0Mmcud-QPpr95lKt6vUYsCsT2FP0y2tkF1sDai8bP6ZElDWX06n5sYBd_W3CLHNQPB_XsHnnv__Lpwyocgon2nfjFqLiHvR81TXXE71h6KVvNq5eOghdp1TO8WvYg_HVm4YVHU6rqGmarqVs80v4KGh8TqdMiEhgVf7G4Yy9DKIrXUKhYRmIerwYbOm1kVaRrfxphpORGTbnpxtiaAxmlM-IkKjCOI4rd_FZXLwJUQ19FPBEWErTqes1OvbWHUbnIHN0C-sFaUy0_6kd17A2Rl-2Q5dOwcOKg6Ip76qQBP9lkWuyzhWlSqE70rDID3AigZ1f5zpQ9cdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b19166e8a.mp4?token=R8alKSb4fZ0Mmcud-QPpr95lKt6vUYsCsT2FP0y2tkF1sDai8bP6ZElDWX06n5sYBd_W3CLHNQPB_XsHnnv__Lpwyocgon2nfjFqLiHvR81TXXE71h6KVvNq5eOghdp1TO8WvYg_HVm4YVHU6rqGmarqVs80v4KGh8TqdMiEhgVf7G4Yy9DKIrXUKhYRmIerwYbOm1kVaRrfxphpORGTbnpxtiaAxmlM-IkKjCOI4rd_FZXLwJUQ19FPBEWErTqes1OvbWHUbnIHN0C-sFaUy0_6kd17A2Rl-2Q5dOwcOKg6Ip76qQBP9lkWuyzhWlSqE70rDID3AigZ1f5zpQ9cdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاکس نیوز: نیروهای امنیتی فرد تیرانداز را زمین‌گیر کرده‌اند
🔹
شبکه فاکس نیوز گزارش داد نیروهای امنیتی فرد تیرانداز در اطراف کاخ سفید را از زمین‌گیر و اوضاع را تحت کنترل درآورده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/653748" target="_blank">📅 02:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To7kBAEGSXW3p9KMIB2TlHA7JygOUQHmEuBaxfPS7xZJPGpRGtHzDgJbQQdEaG1SIlgcCA5DEc4G7nmYrX8tqBEb8C4QKs7kan9dzFeB0dAOWunoTiwxM6hV8be7MtfM5LqBF3YfnbhuFstRkgkAXFOs9RBECCHBwSNPd-wNGAzoye9-YvdHNBvL1_rCfLsnhQfxn763kf_4n_3dZ-zg4y69QJ4ZZwZXZ9CRZ_srew88KUxKA7dW7gATKBsdYTv8JI_80O4-JRb6GAIIph376mtxHjyzhsmYRXc9x3U1RsKZuZK36lV656BxJjkD_7Z57cDaZ66d-SG9wCrF-CS9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر گزارش‌ها درست باشند، این یک شکست استراتژیک فاجعه‌بار برای رئیس‌جمهور ترامپ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653747" target="_blank">📅 02:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaHOmcL8Vws5zC3a0hFZz5bmalYKHidUQ6KjEpyVzqgIZdu2ovImlXFvuKxrAxvHQhSiA36BKIkvURX0ltKr8qd1XSlGkRvdJ6OWJqql3z5MgdLBcF7qo8niV9CkmKn_tAKews-9iyOxob9sXWzfr2gVefK1ZngxTa8hqiLDWuoNNYOsUX94lR1NJKG6ycaA2vvGXgoAns0_EwSaAYDpwgIu5PfOPxRpnPfRYz3uSUIGYdmjn78D-l-MFZQ33vCUdSP2P201QuxXPeN7nCL2WIqVJs1OxIlNRf8Q1Dwj0LhWciIwCCYqcgN95fI0yV33LB9_qBgDraCy_WPI4Lbp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با فرض اینکه به سمت توافقی که گزارش شده است پیش می‌رویم، باید بگویم که جنگ نسنجیده و احمقانه ترامپ که به اجرا درآمد، به نظر می‌رسد با شکستی ننگین و تمام‌عیار پایان می‌یابد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/653746" target="_blank">📅 02:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLG5W5b6P9mr2py79hBRaZzykoEQ6tqjFyh3-VA5R0mMdEmBsoxxOH0jc3tKi4z1L_eveExfMSyMF8uhtsM_tQwofoZXGNI-eZ0HWFuJXpQBuwG1r0xKh4XOrgpvb67dW18OSR9_bPNK5JndV7JUQh4bYJDyOHBu4I0EvVPQP8_oajZHpqBTKB0M59uiKsjszelSJ3nIApcS4S1ubk6TLzILwkMwmaPWmcw65z_2wFot4LZhO2EGc2RBQ_9B6QhwaHeoRB1VgA9bnMo9imKlJE3umm1TEWFmeQqQ3vET6XaqTadqHQMY3tf1afjkdCz5nJPGyJetRikXiD69pvMXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش بن رودز به لیندسی گراهام سناتور جنگ‌طلب ضدایرانی: این مرد به ایجاد یک فاجعه جهانی کمک می‌کند و سپس متوجه می‌شود که سیاست احمقانه‌اش ایران را قوی‌تر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/653745" target="_blank">📅 02:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXi3dI8EGFgKux-Vm9FBQn_pkLty5oJBqnKcZULKKiXJuxjTQHgWWjDEa1QJ2DadDGRrQLzmsr-BvCCeL9wn2WeVjeUVYNEhL_LSMextArmMLmOXkkMPw4vv7yQDI0BkjbJ1paRYDRCxcr24i0ydTDP6ykuRw_G41c_HZ9Wn3bHmX6l2UKta7Thh8N2WocJN9JoUhA0KT_QIRn9uFJ--kiaLvm8z9HUNXTwp7-adi1xdC_eco5b75ZE0_dRiqHmvz7M6lJiSw9kYHX9gPJ4U8zgefZJAvwjJEPPY9EJQNVhuy4EIOhV0iCMMBhlfLfH5NexhIp8hG5yNc93OPm3x8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با توانایی نگه‌داشتن کشتی‌های فعلی در تنگه هرمز، اهرم فشار قابل توجهی دارد
🔹
علاوه بر این، هر بشکه‌ای که به بازار جهانی می‌رسد، اهرم فشار ایران را کاهش می‌دهد.
🔹
در نتیجه، احتمالاً ایران حدود ۲۵ میلیارد دلار دارایی مسدود شده برای شروع حمل و نقل از طریق تنگه هرمز دریافت خواهد کرد.
🔹
علاوه بر این، به نظر می‌رسد که محاصره ایالات متحده برداشته خواهد شد و نفت ایران معافیت‌های موقت از تحریم‌ها را دریافت خواهد کرد.
🔹
این امر هرگونه تأثیر اقتصادی عملیات خشم اقتصادی را به طور کامل از بین می‌برد و هیچ اهرم فشاری برای ما باقی نمی‌گذارد تا بر اساس شرایط خود برای یک توافق هسته‌ای مذاکره کنیم‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653744" target="_blank">📅 02:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr7uPMrOGPe0jepodmW_trKGbmV4WZdsvgtbbxS21XeO-7l575D4BP-JbgTCr7jiP0TR-swg2Hvergs_xblQ98lyYfvZi8ls84OLDKlhLVbGR81Ocb_sBtRnseI2PHgtDYiSdvAgslN7dtLwqN5o9zCMDrqK3cad15Y8Kf1s5wo_h9KdsnoFC43c5lNO_wn1G_QJoUGyHdZwu1ytgzk18ZwTY7iznQ9MOR3djkDIut6ODpjCv8cZKjwhVSBVI9tqlTuh24ao53NPl22jErUvuOTW8RVVmVf00I8Jg-l-MCTogZ84aI3RGuk7r2qa8XagfiiXL-mAHN1wisNm-Ni6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن رودز: عملیات خشم حماسی هیچ دستاوردی نداشت جز اینکه سپاه پاسداران انقلاب اسلامی را مسئول تنگه هرمز کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/akhbarefori/653743" target="_blank">📅 02:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4e071b4a.mp4?token=tnwM0dbKAM9fyfjGEUGlZwzNqnHDNyYE_Klmbgx0D7eY_xo0H4H9cPTbSQHt6hy74nsVrZSiOdCfvL4ipOTbwZRkN4U0FTKme2GtgW2V4a20hRUJj7c5pB7OmioA13VzcYd9N1VZYdRD2PXreFY6I_HlmnGSmJnXDGqn_IblSrsnFE_m0K2lg3zNtt1d4Y9f32eApF6Ek4mcR98HBYWNW3KPStkeXmmAvfjRm8Y9bZYp-Gd0ZgSw0PdHD4P9vMoTSH7Gl-tY27MCxI45nXp8lu7wLoaelvHaNkFzFHbU9nr5e7Oc0WiiGOfVOs2sBnUooR0zq29IXa-gKOpAF9mlsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4e071b4a.mp4?token=tnwM0dbKAM9fyfjGEUGlZwzNqnHDNyYE_Klmbgx0D7eY_xo0H4H9cPTbSQHt6hy74nsVrZSiOdCfvL4ipOTbwZRkN4U0FTKme2GtgW2V4a20hRUJj7c5pB7OmioA13VzcYd9N1VZYdRD2PXreFY6I_HlmnGSmJnXDGqn_IblSrsnFE_m0K2lg3zNtt1d4Y9f32eApF6Ek4mcR98HBYWNW3KPStkeXmmAvfjRm8Y9bZYp-Gd0ZgSw0PdHD4P9vMoTSH7Gl-tY27MCxI45nXp8lu7wLoaelvHaNkFzFHbU9nr5e7Oc0WiiGOfVOs2sBnUooR0zq29IXa-gKOpAF9mlsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقرار نیروهای امنیتی نزدیک کاخ سفید
🔹
تا این لحظه هیچ گزارش رسمی از تلفات جانی یا زخمی شدن افراد منتشر نشده است. هویت فرد یا افراد شلیک‌کننده و انگیزه این اقدام همچنان نامشخص است و تحقیقات ادامه دارد.
🔹
به گفته سی ان ان محل تیراندازی درست در یکی از ورودی های کاخ سفید بوده است و هم‌چنین خبرنگاران از وجود دو مجروح خبر می‌دهند.
🔹
دونالد ترامپ در زمان وقوع این حادثه در کاخ سفید حضور نداشته و هیچ ارتباط مستقیمی با وی گزارش نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/653742" target="_blank">📅 02:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf42b701db.mp4?token=nJTsxeGGLljZP-boztEkgtYGUlzjNrrLnbqi2Wlph-ObqWXeKErJ3LnK6Uje-3DE6SVmVt6VKEfm4vBYMIJyaGW6evh1KVBY6aDYrY3GQhICvI6bOAteaZo8SC629OfL6zlsVBzPauMPeEc6kogROwqr2l85dFdomcjKYjnnCFCpqkbmPnOS8fo184eWTUpFAiVzwQtV7P_ejDyInTAeIN3VZCh4Si51-5S3bcAIS2RRMXvFlLGewFfQIoxvATvtjlL-dCezYubitsiM5FNehkfEMKfvaYMNnx7RXd3I5XuN5oKPZCHbHSn820_5h3YUt4bSAUkskjK3FIAM2BuUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf42b701db.mp4?token=nJTsxeGGLljZP-boztEkgtYGUlzjNrrLnbqi2Wlph-ObqWXeKErJ3LnK6Uje-3DE6SVmVt6VKEfm4vBYMIJyaGW6evh1KVBY6aDYrY3GQhICvI6bOAteaZo8SC629OfL6zlsVBzPauMPeEc6kogROwqr2l85dFdomcjKYjnnCFCpqkbmPnOS8fo184eWTUpFAiVzwQtV7P_ejDyInTAeIN3VZCh4Si51-5S3bcAIS2RRMXvFlLGewFfQIoxvATvtjlL-dCezYubitsiM5FNehkfEMKfvaYMNnx7RXd3I5XuN5oKPZCHbHSn820_5h3YUt4bSAUkskjK3FIAM2BuUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم لحظه شلیک گلوله‌ها در خارج از کاخ سفید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/653741" target="_blank">📅 01:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ان‌بی‌سی: تیراندازی در بیرون کاخ سفید رخ داده و تقریباً ۲۰ تا ۳۰ گلوله شلیک شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/653740" target="_blank">📅 01:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اکسیوس: پیام تمام رهبرانی که در تماس تلفنی با ترامپ شرکت داشتند، این بود که توقف جنگ به نفع و مصلحت منطقه است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653739" target="_blank">📅 01:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxkMEdl1c7jEB8O0xg-Q3SlHXxsomxPxgJNj42A9VKCXRvgjwSbRIX8ttQ7CBzbd_CTzTc6PBH6i39mZ9RxL2crngtrM35qWn8wNA8ipDMVdWm9kLoORQzgPjHDwkUMEu_5Z9-564THHMst3sZtVT6GXgtE1bT_JzF_Q64qyR0v5tA2JZEt_AKQ-dZTYh64cxeiACsGAHEwoKv3LTDW9k-aO-gJblQdGBGTuHb9QJffhg-8i2k2_hrEWbTtUpZ2YGdqwXD5nYUmtCxwc1TiXw640GqXHmatlm2divFKxVLQv09lRQ5tBZMNIHy1VFS_mbtjEeXPXfUwcqNL2GdYRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ذخایر موشکی آمریکا به دلیل جنگ با ایران
🔹
فایننشال تایمز نوشت: آمریکا به ژاپن هشدار داد که تحویل ۴۰۰ فروند موشک تاماهاوک ممکن است تا دو سال به تعویق بیفتد. این تأخیر به دلیل کاهش ذخایر آمریکا در جریان جنگ با ایران است.
🔹
پنتاگون در حال حاضر بازسازی انبارهای موشکی خود را بر تحقق برخی سفارش‌های خارجی اولویت داده است.
🔹
ژاپن انتظار داشت این موشک‌ها را تا سال ۲۰۲۸ برای تقویت بازدارندگی در برابر چین دریافت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/653738" target="_blank">📅 01:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVAFwcCydz1DkQUV_qbxZpk5xNa8M1bF7bD2VO98iiUWavipWzbozaiSCjb6Z-N-QK7id7U6F5tCasNcn9ADp1YnNHmbYrNkUvqCLStpm9Z4ZYs5cd71ZkF8WaIegFrDf1_a0sbu4VZjSQrJG6KyFVamuMSEyjM3tbUfFTXZa_yR7mVNiD2BxyOWE9frIqc8n23IKRWeDc9KwEeZDIgFGrWyUk61ZaZPo8vR6LEz0s-cLYMfOc39Ot1WU0Jx-CFcp9ja4NN6K86ko2emoH0JOA-zvjJ0cCHBJUwsbRudjBvBkBAy8WjU8orfp-DmjcOqWWu3UzU9Err87n9P_OyQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزییات نهایی توافق ایران و آمریکا به زودی اعلام خواهد شد
🔹
دونالد ترامپ: من در دفتر بیضی در کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، ارتشبد سید عاصم منیر احمد شاه از پاکستان، رجب طیب اردوغان رئیس‌جمهور ترکیه، عبدالفتاح السیسی رئیس‌جمهور مصر، ملک عبدالله دوم از اردن و ملک حمد بن عیسی آل خلیفه از بحرین داشتم.
🔹
این گفت‌وگوها درباره جمهوری اسلامی ایران و تمامی موارد مرتبط با یک یادداشت تفاهم در خصوص صلح بود. توافقی تا حد زیادی مذاکره شده است که منوط به نهایی شدن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و سایر کشورهای ذکر شده است.
🔹
به طور جداگانه، تماسی با نخست‌وزیر اسرائیل داشتم که آن هم بسیار خوب پیش رفت. جنبه‌ها و جزئیات نهایی این توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد. علاوه بر بسیاری از عناصر دیگر این توافق، تنگه هرمز باز خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/653737" target="_blank">📅 00:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
برخی منابع از اصابت راکت به منطقه الطارمیه در شمال بغداد خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/653736" target="_blank">📅 00:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
🔹
🔹
این سلاح مرموز ایرانی بدجور آمریکا را ترسانده است
👇
khabarfoori.com/fa/tiny/news-3217248
🔹
گزارش لحظه به لحظه از آخرین اخبار گفتگوهای ایران و آمریکا و احتمال جنگ در منطقه
👇
khabarfoori.com/fa/tiny/news-3217074
🔹
شرط عجیب ازدواج بازیگر مطرح ایرانی با دختری در آمریکا
👇
khabarfoori.com/fa/tiny/news-3217295
🔹
توافق ایران و پاکستان بر سر یادداشت تفاهم و انتظار برای جواب آمریکا
👇
khabarfoori.com/fa/tiny/news-3217312
🔹
عکسی از جورجینا که رونالدو هرگز نباید آن را ببیند
👇
khabarfoori.com/fa/tiny/news-3217077
🔹
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/653735" target="_blank">📅 23:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DapslzdlgkHGnOPp7pAJ6xNZLgcuJJgYhWkF3rwrbQlRLLtauaKZi4VP4Xiv4Rnlejc4yHp5HhEl2yUgV1tKysn3M0W_3k_KG9JY2yupIxBoVrla4eyTml8rtC4-ejpHl9_84w4mIaawOjv8anlykPMMKA5nZijT9zl0WdwZGEWH6cJYJL80NFvEWa45pg7IpT1l--slNOgXtFixDQInkxBj2L642x49xAxBuPxWA0rAuag_M9vqVflNj7FamNgT5A8Ek_GxZTxLDmqqgBuQ2QLfU80dBvn8zDY-IgMNXUvfKlPbQvCHtHDPSIafTjOQylp1uGAUQuDOp7LwEJVtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ns54L2VrOMrJp6HXPP829zoI67ALTBi0iBUggWS8YtDSZpHgoEAnYTkEhOt97Jk1HYHKlVim6T9SusWADekzpm9gKkdGVHeEXLqZish5KpezpHALmvxlhY4u7Ho6WTS5N7AKDmx5vigs_LP0E-06n81T3d_pebHfQrZLpZ9Xe7LJHuJAgsphuC9amrLeIrZML38BRXLNDKDnaIaPDl7F5XDJHhapF4S-EDiW9uoUrF5abDkgtS4HAnnXPWopiet1BSh7S7XnEMWl4p7HUf1RRNZ0zpXP5VUP3CIabT1SICU3HpTrFZY7917d4GxWcK15bGbtg1Hrqg9jHMknfB9mNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHGDqT1BDjki9VxgYnZYy55jGlX48rVeygOhWtgZoM2-fejnyjmK8QHowq3gBnRiJMkpZ9dh1RxnF0EeuZrpygyceNoIzRqorynvd0VLhMlyVHi5jdzfvV4oFs8YAdg3WSA2wyG9mY8aF-jf3fiM6WK0mz9C7heUzzZK6YoPWn4RU0ziAVxorga8jyhULGKVTx7uztqFk9iFw91YGcFsnGJ0keyGoN6MB7BLc39xw_xHqfTEATb3OyBhSL-Nc-qo6Kq43KYnZG04m05qw2T8NHF_6p3B0vpoE1kAu17pPURkwlck8ZZjQYn_GFZj0veBAmAbO2TdEW-3IzExGHRA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1_e_eHTdsy6hIFLIaJrUCcOIUjlFhMHeYTwJyU18ToQ_dLw0r8jXb0pzsWNJnSvHBYuIUAmHvv2Y3GqRcCPoj0zt1lOTkuxh5SLpGYWQv7UPJ6aIaudzr25lDOK7QK0Kqjw34QSFHthKPQdPUmQxG8yrOxwgWYnDUzhWrkJiqHFQzaJFsYPq6xx_WIMY1oWkb5zLHQl9Da0GTokRV6AtXAR-ACztmcCf6VpRVCN_0DEp6H8DSo1L4ouB32uaRN424mMehUAlqWVk330Tvz5050DZHpBCfwwrKBRcM3W2Rfxf1niNxPu4yC89c89kVAxpmtrtf3RinEPCCNc5qMI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0vjjH1SGHrM7XAmjoudfM84_IX_OTWKmEH_ltSLKAdPt10oUT_h_pLOYOunYMGOlgMwcYSkDJcYqvRblddMVMlvqQf4BFMOQlqONgc2pibwVpITIWgHZN3u7sE8obHFe8MEpW5gyj32ZS_Z2IfSTnB1SWNUEFoBcT_P8Rsfxels2QoqYpIQcqvntxGDjLBij137EV88zTYWLh2A2PbywB5pUvGLKHFNp9DvwV0U0gN0afPFAfqOa8ZMjwr2iugrGOLZ7hRZcbOOFZJrAc8vIuOTDC8YqF0hsacBosfMwBNRwKjksK-g-BZTa8MDgoEGgc1XLuYaXfYGI_2HgDSWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLslVpi2y6_mtNJZQwI1_hoHWUHI0EZjyHd38UnYAQVtp033QjifyEAdsOVst6oeEd_BMKk7obZ0BqRQRiXo_Gx2du0aYt_hINvpIoMzidaD_HCRpeVkwbl3ZIhNddLME06i_0EiP1oT85WRadUZBW2wUWfVXLT4F4YxsymOa_90_Kgo8_g-Wcf5sBoGcTebiKwh0BMzQCh8JGWbSaEH0HcH30ATtWOSXhaNaO3Xw9400YYQhMm1VtBIeuYFSJbxD-zX1EWRfdHruxFLRSPTOwmCmpB9bSPQoyqVTjD9xv6_yRYosEuu4AEn2LTFcZPcNHqyXH_ZAoZ1WHVi2Lkwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQJ_gDhq9FPHIYesbh2B_raxRuhfaRArhEE5bUI35u2GWqHZxTFJBSoTJNOIRRluzmEtV1QdVoslg8YJ77hwWMJeDawElRK2fRyXnwmGYwcHFTwjTWy6RIiro4SOsGIEqqltj0YnSjkYSURjbIKBNc8CSHmPCqDraC24Ay_FpupYQlhyXj6OC3x1wtHZVZLtvCkya6FMIJQZpbQGVOljvH0g3cw71SXq_spchjEhRKHwErDCoeN6waECQfqzXowQ_j-j7K3nnJ2tCQFF5gW53TfXkLjNOhdP5hSnyymL_khOtCs6xEkdo22PzjBZ48SjLWYO_k9VwRnNqdWzdJXG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoESOmKmyM_CQ8X1vE5mjqNG-mlnRTsJG2wNpGy6PX7Ijrthn1uz5B6b4DOmfturUjjj610AoJ4JbRNYae2vGc_CdgJ_RNG5HT4xw42pTDHmiixbgDE7AZUj1y9-kvrV58UMKd340yvC3xK0P3j3CxGOX5jbDinG7mMXmC8S67qROxcolORpgyLhcPWof-tpAc9IiKgPszhu_VOkj8Psm3fAYGuMt4zOuKxnqIsXVWliFkDVpoIwIb7w0Jc5MVB8xe2L5iDzKRRnwIPE6UicevuxdQVKCsPM901N3KmTzM59NwLh0sG3sGSXgvwdUQuga9Htsqy8pLbcfaJ-IKQG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMuNrOOlXa1a1tNTtL52zu1AgdQ6CrIV0hzUfbxQY5i6CPAc5B5x5rI0AbBJ1NoRj8TJP1501XT_iUTpM322-iqffAXtS__YDhxYhPrcK7JH1q_1eRQBvt_2FJaVGrwe1BtXzmiFcHMvcwq2Dc0FGW17pmXJL8b0bEoOQto-3_sJvGV2K-iysjrZ1WOCyzas6iO8r97_Kn2MiTMxn4u7zNEZiW-6hPG5-WJ8KwajlWDFio1boIquIMRN5r_GAMCkMG9GkmWkoOzvnP5SdgEee3PSfMcGYmr_8WxQ78aWmjHUyH33mPixEabFndt3Mq09v2sjDQkdtXHON1pGSwcw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس مهر | اجتماع حمایت از رزمندگان در مقابله با دشمن آمریکایی - صهیونی
🔹
اقشار مختلف مردم برای خنثی کردن توطئه احتمالی دشمن صهیونی، همدل و هم‌صدا در خیابان کشوردوست حاضر شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653726" target="_blank">📅 23:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653725">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de8cb2c99.mp4?token=sQRhJAzaMSJRExczRZMkWH6A3ma3XSrRYWWxOAdT52fl8qwVxbn654ShGhFStao8UxvBmksiz-rSWD0blNPpUM8mJ8Yo_Qnl8bAtzND-pc58rh2XikZ1lsMcYoc5gbC2Y2f5Hi3cyLLLVwzPBsGgTZEITQOpry_SiqxtbANd09yuEXwfSf_Yc_-DicO5uBgojoKOHQ0nLJpzs1bPaJtbeBl3b_Od12E645WQHKtOQGFRhtg3Ha8KtYcWjeMtdtiq6Q8xa4ERZs31MTNGvBpH8TywBKQLo6H52FH-mofA4Sa5FG5FcJY7UYU6exDYjS4aabs2Q4rXZ15O-tH4pwcUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de8cb2c99.mp4?token=sQRhJAzaMSJRExczRZMkWH6A3ma3XSrRYWWxOAdT52fl8qwVxbn654ShGhFStao8UxvBmksiz-rSWD0blNPpUM8mJ8Yo_Qnl8bAtzND-pc58rh2XikZ1lsMcYoc5gbC2Y2f5Hi3cyLLLVwzPBsGgTZEITQOpry_SiqxtbANd09yuEXwfSf_Yc_-DicO5uBgojoKOHQ0nLJpzs1bPaJtbeBl3b_Od12E645WQHKtOQGFRhtg3Ha8KtYcWjeMtdtiq6Q8xa4ERZs31MTNGvBpH8TywBKQLo6H52FH-mofA4Sa5FG5FcJY7UYU6exDYjS4aabs2Q4rXZ15O-tH4pwcUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه سونامی در اقتصاد جهانی بعد از ۸۰ روز
🔹
اعلام بانک جهانی: از زمان آغاز جنگ ایران ۲۷ کشور خواستار استفاده از «امکانات زمان بحران» شده‌اند.
🔹
روزنامه آمریکایی هیل هم گزارش کرده در صورت عدم توافق با ایران برای بازگشایی تنگه هرمز، قیمت نفت احتمالاً هفته آینده جهش خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/653725" target="_blank">📅 23:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653724">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiyWHSktmqKRja90ymbClxV3KnygA_Va94tkhsYTgmjhZtnGgqU7opRk6bPfCdzP7iePUoEYMQnal0qVLOcaqA8bOn2l5GD_CleBQB-8o4fvnMmc9hojW4M_FHr4FSI7r0fuZtP59WJ8Xxum138WEoLMZU159wIK40pgELuL3TlCGD_b4i8i6XS-ShxTxTssTbLRh6Zseb2x7B5q2oUn0gXflYhCuHHwq96yL6bKoaAzbHayvuASVa63ljqjRQG9_BlpAnJ2mdWstWReZtazJgyb9RTZ3l2-4C6Tp85A0MLZqKyCYmG4fdEo0_g3J1Pz64qtHTFlT_S3yO2znfSN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و تحریم‌هایی که به آخر خط رسیده‌اند
🔹
رئیس‌جمهور آمریکا دونالد ترامپ و دولتش همچنان از فشار حداکثری علیه اقتصاد ایران سخن می‌گویند، اما به گفته بلومبرگ، ظرفیت سیاست تحریمی به پایان رسیده و تحریم‌های جدید دیگر فشار بیشتری به ایران وارد نمی‌کند.
🔹
تحریم‌های جدید آمریکا همه چیز را از شرکت‌های نفتی و کشتیرانی گرفته تا صرافی‌ها و واسطه‌ها در سراسر چین و خاورمیانه هدف قرار داده است.
🔹
اما به نوشته بلومبرگ همه این اقدامات، حتی همراه با یک کارزار گسترده تجاوز نظامی با همراهی اسرائیل و همچنین محاصره دریایی تنگه هرمز توسط آمریکا، فقط توانایی ایران را در تحمل فشار آمریکا برجسته ساخته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/akhbarefori/653724" target="_blank">📅 23:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653723">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd2741f18.mp4?token=mkDlpDeX3HQrHO4Vzymqf84uvxKW8iuBAyyAy4Mi2ZmbgITcvJTSeyoJ-EAQT4MLez69U-g0ndww9pRU-uEEaaLh5kMVpbYqs_yyNfMPNV1iHLJHqY5iQ2M0mD3iLEsp-4RmynfmIwL0uRRXzJSiLUrGjvd18A2WYQDt4T5NP2KfIRKYT6_G56QIZ9FK5dwv_3nvtxlalp5Y-HhjOXE3XMLUpeulVCYUfws1PZDrDcLfqqMTXSRTmSJq2muGHhkAQkwdQjKYP4VnsavS5UI_WsUB3JHHa2GX9TZnI8iv1liXzQfyBQX87yNYLJInBtCIaxKO4nfTB7_0QVjA07cIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd2741f18.mp4?token=mkDlpDeX3HQrHO4Vzymqf84uvxKW8iuBAyyAy4Mi2ZmbgITcvJTSeyoJ-EAQT4MLez69U-g0ndww9pRU-uEEaaLh5kMVpbYqs_yyNfMPNV1iHLJHqY5iQ2M0mD3iLEsp-4RmynfmIwL0uRRXzJSiLUrGjvd18A2WYQDt4T5NP2KfIRKYT6_G56QIZ9FK5dwv_3nvtxlalp5Y-HhjOXE3XMLUpeulVCYUfws1PZDrDcLfqqMTXSRTmSJq2muGHhkAQkwdQjKYP4VnsavS5UI_WsUB3JHHa2GX9TZnI8iv1liXzQfyBQX87yNYLJInBtCIaxKO4nfTB7_0QVjA07cIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از حضور مردم در شب هشتادوچهارم
🔹
«وای اگر خامنه‌ای حکم جهادم دهد، ارتش دنیا نتواند که جوابم دهد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/653723" target="_blank">📅 23:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d3fbbe05.mp4?token=D3t6oc1t6HusNgX1aVLMQMEnz-ZqG4dGQWUHy6kVcUL5PF7PuTgRJbttON1PLNgcb1wv8W6DWRglhEyK2zmJFjgYDtEXVfMq14CMgA_V2T_m__6q4cnRwKEUaEqhRBdUlB9AcOdYI4zmDIXDnqRBMpoPpKonNfOSmj0YG2zBQ-2j8UuH8ekYqxCmIOU6wvfWeo9zbDLiM_ZtqC_W-jpAOAQI8873_PZQZYMKXEeD2lahY8RFW6n1ukY47sXfR4PqeaKCkwZBD1oLPoSpNU9RDN1yVKMgZTeZCCtEDsRKdnNHR4SuZw_3y88Y1i0BusOvrqLJVpmdcBj5AGsN1NYz6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d3fbbe05.mp4?token=D3t6oc1t6HusNgX1aVLMQMEnz-ZqG4dGQWUHy6kVcUL5PF7PuTgRJbttON1PLNgcb1wv8W6DWRglhEyK2zmJFjgYDtEXVfMq14CMgA_V2T_m__6q4cnRwKEUaEqhRBdUlB9AcOdYI4zmDIXDnqRBMpoPpKonNfOSmj0YG2zBQ-2j8UuH8ekYqxCmIOU6wvfWeo9zbDLiM_ZtqC_W-jpAOAQI8873_PZQZYMKXEeD2lahY8RFW6n1ukY47sXfR4PqeaKCkwZBD1oLPoSpNU9RDN1yVKMgZTeZCCtEDsRKdnNHR4SuZw_3y88Y1i0BusOvrqLJVpmdcBj5AGsN1NYz6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«انّ معی ربّی» فرمایش امام است
🔹
در دست تک‌تک ما شمشیر انتقام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/653722" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZYDxB2rZNiRNkOHZfustcp-WYUs4ago0fdTtTvASToJfDPWP30qgRkoeijI6Kcp49dcs4041tvsZrQE12iH-CJRGXNNroxmzODauCZEGcd5KL3VJw5UFpLFbgGauGND7DfrTALnqfCMU_EA7rpplnKuAFuWTFJWu8flNUNU3pwRaFPxenWHvywor1zmxoBd2B8oE0Lnn1Xvr6NItT6-q-PNwF4eD-6bkvOkqB4ts4SLeMdo_1qfGzxKRVIh60Z6B01CQxPinlbZLLtSBAEEcZO9hQkIowTSgVfQgcIFoSS6aaGhCI4zjxoE90_ThiL0XBjtJJvcMa_aghpqy_W2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرمت قوه قضاییه را احکام کارشناسی حفظ می‌کند
احسان تقدسی، روزنامه‌نگار:
در بیانیه انجمن تجارت الکترونیک علیه رأی ۳۶۰۰میلیارد تومانی آپارات نکات روشنی بیان شده و عجیب این که قاضی محترم به هیچ کدام از این قوانین ازجمله ماده ۲۳ قانون جرایم رایانه‌ای و مصوبات شورایعالی فضای مجازی درباره شبکه‌های اجتماعی توجه نکرده.
حرمت قوه قضاییه رو احکام کارشناسی حفظ می کنه.
@Akhbarefori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/653721" target="_blank">📅 23:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTb5RSsmfZH_EQ8hrwPLZxu1eTsx1NNe0M07p5iYl6D8M7NIoepuesbHzV5u2fjXtbgqeRkvfoRVcuDH3djeALZkIoBkFq-HLEwqFqU7CBqozd9xDpHILI5yKM8E46ciS6CKWjQs-SaFNU6_inLFpStIGVd25kSxdGKb3cw7i2cegUseuS_cVzZvCgJSa4noZf_5gkPW1gtr3dwnWAD63qQCuKzvcbv6BHiXLbzXyU9UAxvGBldAtVci5XT7g5133W5oHkEKab9J_XaYBFHEF905KlMCX8tYgUg6dF4HzWUiYHOtzeYd67_jliViUiD3U0X36JMt31Rau5fnGBusWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشینگتن پست: استعفای معاون اداره اطلاعات ملی آمریکا به خاطر مخالفت او با مداخله نظامی ترامپ در ایران بوده است
🔹
یک منبع آگاه گفته استعفای «اماریلیس فاکس کندی» (از مقامات ارشد اطلاعاتی دولت ترامپ و معاون تولسی گابارد) دست‌کم تا حدودی، به خاطر مخالفت او با مداخله نظامی ترامپ در ایران بوده است.
🔹
کندی نیز مانند گابارد [که او هم استعفا داده]، پیش از ورود به دولت، مخالفت خود را با مداخلات نظامی فرامرزی آمریکا ابراز کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/653720" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 55</div>
</div>
<a href="https://t.me/akhbarefori/653719" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وپنجم
رائفی‌پور:
🔹
0:07:40 صحابه پیامبر از نظر اهل سنت
🔹
0:15:20 سنگینی کشته شدن عمرو بن عبدود توسط حضرت علی (ع) برای برخی از مسلمانان
🔹
0:29:00 حدیث منزلت در ۵ هزار سند روایت شده است
🔹
0:34:00 اعتراف و حسادت دشمنان حضرت علی (ع) به سه فضیلت ایشان
🔹
0:55:00 علت شباهت قوم بنی اسرائیل با مسلمانان
🔹
1:07:30 تفسیر یکی از فتنه‌های زمان ظهور امام زمان(عج)
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/653719" target="_blank">📅 23:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ac296132.mp4?token=rSDCl3UI8o509KgYaW3BkCgTNTCozawwhhH0AovUI8zx6pFl8E5IB_JlIQwVe0QVVa2qLvTidUiaRHujrXhfpVxn3zL_PJdlTzMxx_2sshoeWcnFXJshC_cRCNpK6diF0-Nl0MkpRYVLnfm6mY5pdyiygdmNSw1o7vkm1FOabU4hA0uhlK6mWsZCmH548hhrMKgi0dBi2Z5hrFIOdDDdpS9tVI-Sj8ioreKYguxCle3GK2YudnZDZ73fgQ9ilPnKf2bQPgLVDsFkJ0aBWVvQ3xqg1Y866DmE9lcMkw91gcevuPSt5L5GY07Hqw1usJWky2N0mYj1vN8bb6RQgWPQNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ac296132.mp4?token=rSDCl3UI8o509KgYaW3BkCgTNTCozawwhhH0AovUI8zx6pFl8E5IB_JlIQwVe0QVVa2qLvTidUiaRHujrXhfpVxn3zL_PJdlTzMxx_2sshoeWcnFXJshC_cRCNpK6diF0-Nl0MkpRYVLnfm6mY5pdyiygdmNSw1o7vkm1FOabU4hA0uhlK6mWsZCmH548hhrMKgi0dBi2Z5hrFIOdDDdpS9tVI-Sj8ioreKYguxCle3GK2YudnZDZ73fgQ9ilPnKf2bQPgLVDsFkJ0aBWVvQ3xqg1Y866DmE9lcMkw91gcevuPSt5L5GY07Hqw1usJWky2N0mYj1vN8bb6RQgWPQNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به مقر گروه‌های ضدایرانی در اربیل
🔹
رسانه‌های عراقی گزارش دادند یکی از مقرهای گروهک تروریستی حزب آزادی کردستان (پاک) در شهر خلیفان در استان اربیل هدف حمله موشکی و پهپادی قرار گرفته است.
🔹
شبکه عربستانی الحدث هم خبر داد که مقر گروه‌های کُرد معارض در منطقه «وادی آلانه» در اربیل با ۴ فروند پهپاد مورد اصابت قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/653718" target="_blank">📅 23:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0eacf8e9e.mp4?token=YFYwldJfCd7IpD_b5zejfoCl1eRq43UpYpYS60EnraJPnUZXuVSTa-awSHnZ7Aq7Tp5GZU6C6546CVxbQl6hrTTY8ofaE0s79u5hMc4BD5a7FNFUX7ZsmF3j2K9dOs8kTe5t82e-4wnD-vWu4yBrHX1kLsf15R5VuaveEBJfRIdPFKTbSB5DJRQE1ofD_WB3kf4XDUgrt3rC36J2sPfh1Ci5W6WzFnrXnyh0C7e8J4bQYYKe6i5xCoUf0HYoYUcOKqijfcq0iQOV3NgwrUkTJpaHJIb73TGrdwwVdC2HIvw73ls13DrPvIIWh7sy7tGOtdWii_27VePhiCa4PYqrqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0eacf8e9e.mp4?token=YFYwldJfCd7IpD_b5zejfoCl1eRq43UpYpYS60EnraJPnUZXuVSTa-awSHnZ7Aq7Tp5GZU6C6546CVxbQl6hrTTY8ofaE0s79u5hMc4BD5a7FNFUX7ZsmF3j2K9dOs8kTe5t82e-4wnD-vWu4yBrHX1kLsf15R5VuaveEBJfRIdPFKTbSB5DJRQE1ofD_WB3kf4XDUgrt3rC36J2sPfh1Ci5W6WzFnrXnyh0C7e8J4bQYYKe6i5xCoUf0HYoYUcOKqijfcq0iQOV3NgwrUkTJpaHJIb73TGrdwwVdC2HIvw73ls13DrPvIIWh7sy7tGOtdWii_27VePhiCa4PYqrqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سامانه ثبت ادعای مالکیت املاک راه‌اندازی شد
🔹
تمام افرادی که ملک و زمین‌شان قول‌نامه‌ای است، ۲ سال فرصت دارند مدارک خود را برای دریافت سند رسمی بارگذاری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/653717" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfa22ac8.mp4?token=TAh2kXcHCLRxGIsrFDMPdp8-Ab18y_p-iL0SIs3LB7R58jZUKQsMuexlejlsm3IJgg_26_zRLSJW9fwGwcr-z3KiA51aatEUtBT0SdXZekPflgWPCuP7TE9Y4dF3Ija3uLikzZAsGehle_I7hKQHSSAS34LYQPpTrXqxntoA8JTI1IXawH4FdCVURqyukO-GvoKnpT4gf38YHzsNHwkkz1rhk53_FPr-3XiiCukuSSa2QOAcLPXnPSZV7nkNJU1pzhcb_W1K0XpFezHGirvCBGQXj3QCFDffzkKDLgued5pXLF1-evaik7nEIHvWXy998UUhc9m1qayWo2PYzCiFCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfa22ac8.mp4?token=TAh2kXcHCLRxGIsrFDMPdp8-Ab18y_p-iL0SIs3LB7R58jZUKQsMuexlejlsm3IJgg_26_zRLSJW9fwGwcr-z3KiA51aatEUtBT0SdXZekPflgWPCuP7TE9Y4dF3Ija3uLikzZAsGehle_I7hKQHSSAS34LYQPpTrXqxntoA8JTI1IXawH4FdCVURqyukO-GvoKnpT4gf38YHzsNHwkkz1rhk53_FPr-3XiiCukuSSa2QOAcLPXnPSZV7nkNJU1pzhcb_W1K0XpFezHGirvCBGQXj3QCFDffzkKDLgued5pXLF1-evaik7nEIHvWXy998UUhc9m1qayWo2PYzCiFCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در این شب‌ و روزها، سیاه‌ترین سرنوشت‌ها، -با اختلاف نسبت به سایر رقبا- از آنِ گروهک‌ها و فرقه‌هایی است که روزی حماقت کردند، به سمت ایران سنگ‌ریزه‌ای انداختند و توهم داشتند که بازی کردن با دم شیر برایشان بی‌هزینه خواهد بود
🔹
حالا در آستانهٔ سومین ماهی هستیم که ایرانی‌ها اجازه نداده‌اند آب خوش از گلوی تروریست‌های تجزیه‌طلب پایین برود. شعله‌ها را ببینید. این شعله‌ها در رؤیای آنان و اربابانشان قرار بود در میادین اصلیِ شهرهای ایرانمان دیده شود اما همه چیز برعکسِ آن چیزی پیش رفت که رئیس پدوفیلشان تخیّل می‌کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/653716" target="_blank">📅 23:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a04caf63c.mp4?token=qSjf9AFHgRPyXYcINDbCa72aOryINitzqUlAOmJ98u_NjD0lS6t5KsTVAkfuXFVgcWVlnBAgaLxjEinrJyhKlbpOrjFmKq8r8k0D0cJs8dA5NE7vDVMnNh6MrTNP-FdmnKcKnhbcFMR8JCuJnKhzTQ4R0kgD_IHpDgwN9NNtcy2PT8wMqEgQF3GlD8ujG4z6MlKHeM6peMtRQT1ouKm2l0G9H97u1_dkUObTv1d_Inx-RzOGIgfbpJ76UKamlKbGM8a2VTYv6rQkDtdijP_Xb8X6VaH_4KGal2XA7EpKgubisIb1esmv4JkG640bdxS2MfxmMHYgzhy2mBKqiGJu4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a04caf63c.mp4?token=qSjf9AFHgRPyXYcINDbCa72aOryINitzqUlAOmJ98u_NjD0lS6t5KsTVAkfuXFVgcWVlnBAgaLxjEinrJyhKlbpOrjFmKq8r8k0D0cJs8dA5NE7vDVMnNh6MrTNP-FdmnKcKnhbcFMR8JCuJnKhzTQ4R0kgD_IHpDgwN9NNtcy2PT8wMqEgQF3GlD8ujG4z6MlKHeM6peMtRQT1ouKm2l0G9H97u1_dkUObTv1d_Inx-RzOGIgfbpJ76UKamlKbGM8a2VTYv6rQkDtdijP_Xb8X6VaH_4KGal2XA7EpKgubisIb1esmv4JkG640bdxS2MfxmMHYgzhy2mBKqiGJu4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/akhbarefori/653715" target="_blank">📅 23:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای رویترز درباره چارچوب سه مرحله‌ای برای مذاکرات آمریکا و ایران
🔹
یک چارچوب سه مرحله‌ای برای مذاکرات آمریکا و ایران پیشنهاد شده است: پایان رسمی جنگ، حل و فصل بن‌بست تنگه هرمز و باز کردن پنجره مذاکره ۳۰ روزه برای توافقی گسترده‌تر. امکان تمدید نیز وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653713" target="_blank">📅 22:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4943cd2a90.mp4?token=PWr_BoxfMlmM6ypMNIaiDsnGH0dWWsXpikt_CmOSYQ5cx1YgVoxA8IsBZEBzC9v8-jav7QHMMbz_MXDhuJBE8c4Tsqv04A5HkzQIE5LFsnxQWaJfh82Sf5mx16ECFmI7QB9wEOL-ACaux0i_1T9WpnB8rF03YXYhgaW9e9uyEXgIV3LwpoVPgztmIWnlzU6i3dy0LUG2vTg-6u7bVLKDhl7Xmf6iUx8X1Ssm8OueRkhA1yjOEGUKS26pa1-29Z6oowQOEXkp88NJ5tjY4xZFs27zbu-f4aqz5T_dpdTXj2RtNqHfxq77O3bg1pIAG4czAUWYth03oAvCsWozZF86rWDRd3uPL8QSKqcKPZaV_OKASB7Y-JcVouzG49Y7RFI2Ah6Wvay7USWbS3ooFsBHJA6dlaicmY9UoYq8WI7LHTpUI3CqPlqmakQLV2IUMmeVAv-AzoRIe5f3y-I3RTki2rm3Jd9KuhD690z5gTFTglUQO_ON5uwKBNFzKCQ64YCpBqpqeqYJC7yAgX1JUl6S3uFpAxT02BXjo9-re2KXQfZARk4eYO5OVYtsh1sfWTNwxP9dFzDLUrZ2VKqUUr7J6CI1GSgkiG79d2919h0t_huhJiLm_jlOrJEuVFUCT5l9YOvJzOA1eZ9KnTE-QYgkjtkrIrnAsovb3_pSbSifnrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4943cd2a90.mp4?token=PWr_BoxfMlmM6ypMNIaiDsnGH0dWWsXpikt_CmOSYQ5cx1YgVoxA8IsBZEBzC9v8-jav7QHMMbz_MXDhuJBE8c4Tsqv04A5HkzQIE5LFsnxQWaJfh82Sf5mx16ECFmI7QB9wEOL-ACaux0i_1T9WpnB8rF03YXYhgaW9e9uyEXgIV3LwpoVPgztmIWnlzU6i3dy0LUG2vTg-6u7bVLKDhl7Xmf6iUx8X1Ssm8OueRkhA1yjOEGUKS26pa1-29Z6oowQOEXkp88NJ5tjY4xZFs27zbu-f4aqz5T_dpdTXj2RtNqHfxq77O3bg1pIAG4czAUWYth03oAvCsWozZF86rWDRd3uPL8QSKqcKPZaV_OKASB7Y-JcVouzG49Y7RFI2Ah6Wvay7USWbS3ooFsBHJA6dlaicmY9UoYq8WI7LHTpUI3CqPlqmakQLV2IUMmeVAv-AzoRIe5f3y-I3RTki2rm3Jd9KuhD690z5gTFTglUQO_ON5uwKBNFzKCQ64YCpBqpqeqYJC7yAgX1JUl6S3uFpAxT02BXjo9-re2KXQfZARk4eYO5OVYtsh1sfWTNwxP9dFzDLUrZ2VKqUUr7J6CI1GSgkiG79d2919h0t_huhJiLm_jlOrJEuVFUCT5l9YOvJzOA1eZ9KnTE-QYgkjtkrIrnAsovb3_pSbSifnrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: در هر توافقی ایران حتما باید غرامت جنگ را دریافت کند/ مطالبه ملت ایران است که از مدیریت تنگه هرمز عقب‌نشینی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653712" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رایزنی مکرون با ترامپ و سران کشورهای حوزه خلیج فارس برای توافق با ایران
🔹
رئیس‌جمهور فرانسه در گفت‌وگوهای جداگانه با ترامپ و رهبران کشورهای حوزه خلیج فارس، خواستار دستیابی به یک راهکار دیپلماتیک و توافق با ایران شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653711" target="_blank">📅 22:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Whk-Afht1F3UlIumBJG9h6b7omiW24l9m3rLAus_hIeB4Wr_c4DacwlbnOOl8UZNIqOAxGp-8XobXHqzE0F12uiBI4ECtzTx2vf6okBc0OdyuAIUs7o8A0ZAd3wbAq1vpNq4Tmd-DHK-vMKJ9W13NN-1qQfnmg26qNPLlQpQk3R0FnF7PEiWdgLzbpc6s3gC7kd3FAf0sORFcozQaCFPzfjpOqiXam9v07byWAZ2s74m1iLscZ557SjGp0xKdY1jD9h35mq3M0Bh15lNWisvLuog1xTT1jXgG2DNdw3g81BJrlHhQQPZ8yWchMnTmZgbeFyXpROEAMgUACBO1bDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت طلا و سکه
🔹
طلای ۱۸‌عیار به ۱۸ میلیون و ۴۵۶ هزار و ۶۰۰ تومان رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653710" target="_blank">📅 22:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RStr0PF_C9GBWP_mNjGTPf8OQHkYrWbbU9FzfnFFvLxddzHibCKebu7xEfBj9_G7-BIIZDZL59-or2k4Rr5TBy8Fo7zROu5yvxCw200uIFJtBht9tbTEVEqlBBDda89_ujK8yeDu0iK17d7S0-Pm-EVua0nW4IFEnnSgq-8giX6NWpJ-rPKxjNLRC30xtYxNoSFqfI8CmYVSMwmOZv8eXSjRDF_JtFTslSqNRBN3_CaJuMFaUqM7jC-jt4lxojERKEJrtNYdwu3NwaPv1GEA3CP1rWEeV-oKFgge04B8oz5d9qjUELZqOixWuUfwCZJQ7mSJC-LbX0PA6L2EdEh9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوری| تتر ارزان شد!
🔹
در واکنش به اخبار توافق ایران و آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653709" target="_blank">📅 22:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تجربه اصناف از اینترنت پایدار در روزهای بحران
🔹
قطع اینترنت بین‌الملل، ارتباط بسیاری از اتحادیه‌های صنفی با اعضایشان را مختل کرد؛ ارتباطی که پیش از این عمدتاً از طریق پیام‌رسان‌ها و کانال‌های تلگرامی انجام می‌شد. در این شرایط، اینترنت پرو به ابزاری برای حفظ ارتباط پایدار میان اتحادیه‌ها، اصناف و اعضا تبدیل شد.
🔹
اینترنت پایدار، علاوه بر تسهیل ارسال اطلاعیه‌ها و دستورالعمل‌ها، امکان برگزاری جلسات آنلاین، آموزش‌های تخصصی و دریافت سریع بازخورد اعضا را فراهم کرد. فعالان صنفی می‌گویند تجربه هفته‌های اخیر نشان داده دسترسی به اینترنت باکیفیت، دیگر فقط یک نیاز فنی نیست؛ بلکه بخشی از زیرساخت ارتباطی و عملیاتی اتحادیه‌ها و کسب‌وکارها محسوب می‌شود./تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653708" target="_blank">📅 22:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک منبع:
🔹
جی دی ونس، معاون رئیس‌جمهور از اوهایو و پیت هگزث، وزیر جنگ از نیویورک برای برگزاری جلسه‌ای درباره ایران به کاخ سفید فراخوانده شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653707" target="_blank">📅 22:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مقام اسرائیلی: انتظار می‌رود ترامپ امروز با نتانیاهو درباره ایران گفت‌وگو کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653706" target="_blank">📅 22:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66fae7a7ed.mp4?token=t4-VW7sb45XSfTXiV3oFkH0DoCUM51FzYfxxiEFJ_TeIjtGZHB-gWpgmy5yoMcNToXKYE30o1BLpBhwq8Za411iMVmMgL1tSbgQOSzgnOjdFGvAF9uxsI9HX_wgBtvJZ0IrX3xysc94pV1QDV75MVTq6WKk6ZKEedkEFrhEohEKgkSFVa6oXwrBWUaGHTfW3ys6uhZa45LlYbvTwnUqUEl3L_HOxxcQjIwlrBpTGWOCFuUhj00qlF57RUS6WHimN-L5VmP02Dx4aoaTB7nfqq7jRnoiJqhdR8pKnu_gHdjiCai1eYHKzWt8ewbb2CMRdXRLd3ys19uC4P73b2lxfVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66fae7a7ed.mp4?token=t4-VW7sb45XSfTXiV3oFkH0DoCUM51FzYfxxiEFJ_TeIjtGZHB-gWpgmy5yoMcNToXKYE30o1BLpBhwq8Za411iMVmMgL1tSbgQOSzgnOjdFGvAF9uxsI9HX_wgBtvJZ0IrX3xysc94pV1QDV75MVTq6WKk6ZKEedkEFrhEohEKgkSFVa6oXwrBWUaGHTfW3ys6uhZa45LlYbvTwnUqUEl3L_HOxxcQjIwlrBpTGWOCFuUhj00qlF57RUS6WHimN-L5VmP02Dx4aoaTB7nfqq7jRnoiJqhdR8pKnu_gHdjiCai1eYHKzWt8ewbb2CMRdXRLd3ys19uC4P73b2lxfVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: هرگونه تجاوز دشمن با ضربات جبران‌ناپذیر مواجه می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/653705" target="_blank">📅 21:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRbiWVJhjuKq7zH396nUtt5ZBWHuZnh5_RCyRjtsDuQ5vlSFRBlbTGdfI9RezhusvXE40X1q-JKDnxF1XgK0h7IlXxQfLBeC5nhSCdKdQd-CrIt9Er7RTt5Or8rGTg92DiY5JNqP6d4OzeHiWe3yQ8VjHZSSLw0Mj8DPVijUjA5j1kE1qgs3IKgDGvr1-KhJCPGqqoZ6ZCb135gZPTOro3tPpbxNfmKYnci3wYVMSCy6o2LqGgYW9Kaqy1rVBI-fx_I95IfHzdjbvXaJl6gGbnq2P1ivi8uF9I_e-3x6_aGEgVq7wDl3O2-Z3RZwRL4g2g3RlewN-mWcthdXriqH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برات اصلاحش کردیم!
🔹
با تابوت اشغالگران، «خاورمیانه جدید» می‌سازیم.
🔹
در واکنش به عکسی که ترامپِ متوهم، با هوش مصنوعی درست کرده بود‌.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653704" target="_blank">📅 21:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg4olbxBMfXq1XAOpffyTok7whFMHoAbHcj6M6dtL3OXvnS1me8e89dtqW1Ju-beUfAjMVByvPDX-rCfD_1ppeDbrJStSo7HY6MID7oiVYFHw7bjrujOxFXSUUz-YMMTw5eqtRgwNwHrE_Mv6cba6pgSIxnvvvJOOUeECLMFAYzlPbmSMzZWay0WyQOQNGBD9Krv6NO9S356G4BnP7jZHteHRpLILV-F9ZBNTQtTxQN7b3ctVGLF4dZRnmu02RLr2v-x5YgXG5zmXcCuXNBw4KP3gmq0VJrxTXRKqbG4jmjmCHcnEq-EnRrC9Cawjf2bqKHETMFiT40W2kPjpNUOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت یک گروهبان صهیونیست در عملیات موفق حزب‌الله لبنان
🔹
ارتش رژیم صهیونیستی اعلام کرد یکی از گروهبان‌های این رژیم در حملات موفق پهپادی حزب‌الله در شمال اراضی اشغالی به هلاکت رسیده است.
🔹
یک سرباز دیگر در همان حادثه به شدت زخمی شده و یک افسر نیز به طور سطحی زخمی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/653703" target="_blank">📅 21:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653694">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0buzNF89tJMRm4snr0S7UiYCcieQBaiEr4FAZ0RfKaHBgyw2NGS_2LGD2-bqDq-LKfeuCgG3VT3PeQorZLBdQzhK5gv4FHbGwd9a2moz-5PngeaehE9_zlZ0CFolzo_JWX3gR8UI3rtGvDvfnwGUCHUcsF-bWS15N0BC47E5Sm4SMrmhuOM40SH5q51ChpNL7AMRr30gtoNpuqv1KsfOJrhFrEbxLtnAg7M1Q-74ZuB3z7HktQ76qrZvNCKC739SCyvfR16Y_LJMdV8WN8mWizt2dgDu7bbCvA_xJIpaDMU6EETJz_aRhjKMEMCdpiqJ7Q41EznddI4TwK78_JvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiaGImtXHK6mS5XKgE5hoyLMYhLbQAI84PltvIVdrH674o8qup_MJirVSves9wYG3XEoM-nAImmLCi9BA8UjPTvzJlvHzEQ2DbPZ4_I8G4M69cX-InSSwLgrJErIsbiBBJmaWs_u9rZQ5Q7SIKecALlbCgJvde5OCqLq3EYHN6AXFkkSxE7cSvuKnI3wtyfRONUWU8xDLtLptaorb51--jBWvKepTGX6VbZezQyDfhu4NaCJIKEjRy4tmSZgBloTrHnDCJqydE2-PnkypWv-rcLH9ENPZkez5uB_evsMN68DLOXVaRgSsxbE2ORdeL1_z_x8w26b3jEp0-vEM2C5pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7UEba6j2P2bN2aOguJ78DboPLk1_cE3j9NcahPy8YOiITRyNGCWNnXWj-Clbh9RAsLyp6syL262MGqDO1X_t-qI9paG3T3_IzrvgwnOADtH39OhHs_Ee7YaVeLEa_Hrrx-bXbWIMiOJTTxA3wLhIgzpTpV3WUiCA_zokWgdcE7VA-NksWHTpD-INDJWFSHtWKSF9yYW2UrG1ZeVQgOfw341Uw6cVvWcML8umRdnuQGswSVC-vc-F7CC2xScs5HeHYQcVOpje1ADOEM3eSKE5phcJLv7ZnYo_J7fdwY2QX3AYuVkvpwW7sjwvPouDg3Xscgy9ZPFhtc7WfrwWGk6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHjWfjKgcb0PRixafYS7fTaHDbYVHQ1Xsc500-v369qZpvxlZUY72LvnWjzBmPWE_4Inpf5UPPU56dHVx9ThBsKFnWNXihsnyiXePxScCpR3jsZQ-dhkZRh3w0_6vA0zjMYqm5MFmcDpkaCa3Y5KE5LB5tpGqGFxlhlgoVmeUsFiJwycZAbYQ_pKa0dR5_CJUvBeyHQMmtk1EhtfWWh9UTH_yD4mRzPd_5LiNTlMuXvRCLQ_NL_Vzy_lidMdrwirde-k_yo8oNgTjNhoptDI10lDjYZuG6qvX2dN5ypnM_5G6Pxdqhkr-yxhsUNoEWukf7cV_er1VAS4z-hMA5ILAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaB1H_j0RZYWu25m2XV8yyomwuBk5k5UaSPYS0-fZtCjZ-AYbVG-ORigvK8kyPpPg6lW4EOehdfys-cahX5ELFq02iYANgYGBwl4BaGAfHUywQnhed2MSZnHRRtQuhpA2qXlTAt2T9tBkMy1yyYLp55ccvn5VujdwqvH-ktmurn0Vnp8VS0Erij246NQQWI5eZSc-9QeSFOOLW6QgzLwcNu8HZE6Vdi9471CNmbcAb9dNNxuIXkFS1PucAHWHTcUmMAKTKUrgml7qF3yO2ZiueD6erxAj53vraxr0aTOeHOwRggg3VoxvIJJvugkaRuIT1S3e1gj3jrJYXyAQ07gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFZeR3TxAH0xXLmq8uEIvwTV4o9QAk8hmmEmP0OU0gjKFhn_zIFb3mW-q0LVz2sPoZeF370Z2c1mYKSt9LVDDfW6RkyYmZzBVBq9Zni0vz-B21TawLWSOz4JIhHXPxWNXi-Cus-RaQT3CwSpfeKSI4nPndYBlOkNHsCsHbhzqX3vcLQkf4AIqGdO021q_X03eKr3fZQcyMkPQcQ6HLGYJPpawOuT27000LMksAne21o7TUfrrNhbdVXjHqxSw2TvQmF5DEpB5-F1rt_5wedf5a7nxGwLGuG953KvFxblb8JMGVTPU64YBdvfud8zOSUFDu7QKLi8xH6rx0vixnCDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0NsZhfGjCdkj4Ji0pHRsviq9MUU_owm0IezPv7yvm8JO4IZXWrSInxF4P-NdyCGIDZcwmM-eZFca6ScHEu1BgmzWMn_VmIRm2ZVXesBtDAY8Z8mjvVOgeWuH0prV5ygKdd3ciIrFXWI11ZbQrg7tiz0tD9IJBqSxtwHBrNrm8l-Hd9WBYner9K43UHgyrO0TZMlFyYNWj3-pAzl3raO-l--5cX9XUkpHVShF3VCBTC-an7RTwD970yqqirv9ijP0lrMLKlfcYPiggk9W_vLUOxIaG6N5HI50fdLAZNvDsObFrdLnacEMSFD9EhwzrHgZfXaTImbx4tjI2F9YaS-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clXlWWhDVSHvSRBU-vXXLyRyQqk65rXKbjO5eWuCpoq6PA6VfFr0q2yS8jh_-Gk9Ui5zBohL2vQc1HFgI5MwvU_88bxVLhEYaD8ztIorJDB-oyT4qVSox7TGSarbfmwtl8h7rx2caH98z-TVuDsO53CbBC5C-dbWgt3LVJvUjcJkVfHgBKhEabNMZfocpn-YTOX7qk5lahZfGsMapoUY8Deu-2eWZSn7UVjiLi_yuxZls8RMGmIN_bs9ZTpTKjnGcNSDkQg3S63CZ2QyaEaNmw_QtJkJZiJrTEuh2eQovJdlioLlqYV0kq-S_64TVnaSCEs_CEC5_GE-SCOF-808Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d978LKRJSEf6Ly69D2_Mhue2PmOLKhKFgdZjuZSD8qJI2mV7BrIUXjhgAZYP5QkJJXoRyYt4l1x0w5ig-N5kqy7-rct0Ot2ItdqWVvmBEk2Tt9jRJpWZtPQV9qhAKsiLGWTmiVUEFn809eKj5xvaarTI5_fXjTzYth5ofGuAsXN73fnGlxcfS1c9fZUQbxsZLGBm0T6Ww3Qrs-60t2IGQ0OhphIG31aYCThZio2qQI1tQwKlvoWl5tYEStVXVAWgZ5BpX__yFX1SlDY5y-n6wyJXpoWG_6UN6MnTZeaGSkV6T0XAs7mCJtHUba6ZnlkoyWmmycEodICF5pHJgqzOQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ همدلی
💫
هر روز، به پشتوانه
#همدلی
و همراهی شما مردم عزیز،
#هیات_قرار
با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، گامی در مسیر حمایت از خانواده‌های ایرانی برمی‌دارد.
ادامه این مسیر خیر، حاصل اعتماد و حضور ارزشمند شماست
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/akhbarefori/653694" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653693">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhv3NZJhk_FjLOlzoZtxgF89scpGoCbC17_Rfe73QVwEwPcg_2G1BxZ7r0N__3Iy0GMlOWO9xVUFrjpzMO5nr5_32l5a_tsowZtjCsrRDrUEUwmQvF3Fql-QZq2ejTulvJVVIf6zIKfLH9a816uYwJIAIC1EhXz-UmoYNfbaGo-rBXudmgbTJp5r5tV7dK5M5yxMFwSp0bAU6LX8OKWI3Qn_LZzsOoNud4nWdiSL08H-VLdWveioqc1jFX4OPfYxotVFIbucwXMw4qig5r_tK1Ioe__GHpy8Sgb5ssiRrPQx1et0jaCpM7vw1siMBlWMNxOJ_A-Ij5zaOrCzitXzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژنرال صهیونیست: ایران در جنگ پیروز شد
🔹
گیورا ایلاند، رئیس سابق شورای امنیت داخلی اسرائیل: سناریوی بهتر برای آمریکا، بازگشت به روال پیش از جنگ در تنگه هرمز با رفع محاصره علیه ایران است.
🔹
ایران در این جنگ پیروز شد، شاید پیروزی با چند امتیاز بیشتر اما این یک پیروزی آشکار است؛ آن‌ها می‌توانند از نتیجه جنگ رضات بیشتری داشته باشند.
🔹
آمریکا در تنگنای آشکاری گیر افتاده و در نتیجه این امر، اسرائیل نیز در مخصمه بزرگتری قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/653693" target="_blank">📅 21:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653692">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آمریکا زیر بار هزینه‌های جنگ؛ ضررها ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/653692" target="_blank">📅 21:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653691">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OugDj07juW8tVA12qh5jyVWBInYIZ72LKW6u8FWZlBgM7HZfazbSzu2rMHTZR1HCiEvKVVJeb0KE5EB_sU8d9CuJtE_em34fDdBawwJmznXPn1kGM3SKca3rzgpOyavI0OmOFYWr2PvD9US8SD3t0_WyBYg17D8_mz4oZJYImClCAdsX5Xm85XUq0_UQdvBMBo5b8XxpjaDlC5VgfNtASG1ldveaIqfkbs7xTjifrM-gh0YADa3t_S_3gK1JTbe2UTUWgELOpoeVuHpqdnviHrHzG8SMNubeWMcOtz0lufHCtddxhYGMVx8sumD2Dxv6zlhBo5uPjlSIXLQus3hnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ در مصاحبه با کانال ۱۲ اسرائیل: اگر توافقی برای اسرائیل خوب نباشد، آن را امضا نخواهم کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/653691" target="_blank">📅 21:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh9pQklr7cBKvs10gTuL2xGIXYuD_MlNbI5cFgNPK6I1djmZZcUNA4f8CnI1z-9wBAJ2nVHz6RgwUTorfyN60lWLpyRZEyvE0SV0Np8l314T-QEzknxip-prpqLEjNXn5I1oVh5ygM7k5FhWYHA6FFx7V9vBo54_H6A3XntFNNruT6R0pkPA5uACbjxOuouZEUuPLfEVmh14UwlD7OA6REHV4kejtdQgE92--lBaUTGBv-sc0bL-jrwIq3R3InAGmqpx7WVtg_A743ImMGLSZTixe-gY1EoTuPVArDuU_Aq1Ay1t77gC_WndGasrGC7-Pp3swVaum5xxWbLhHzv9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رخ دیوانه
🔹
رفت و برگشت‌های دیپلماتیک با حضور عاصم منیر در تهران برای پایان دادن به تنش‌های ایران و آمریکا به ایستگاه پایانی رسیده؛ نفس‌ها در ساعات آخر این بازی پرفشار، حبس شده است. در همین لحظه حساس، ترامپ مانند یک بازیکن شطرنج از تاکتیک «رخ دیوانه» استفاده می‌کند؛ وقتی موقعیت کاملاً بازنده است، بازیکن ضعیف‌تر رخ خود را مکرراً قربانی می‌کند تا حریف مجبور شود آن را بزند. اگر حریف بزند و مهاجم هیچ مهره دیگری برای حرکت نداشته باشد، بازی به حالت «پات» مساوی می‌رسد و شکست قطعی تبدیل به تساوی می‌شود. ترامپ دقیقاً همین شگرد را در پیش گرفته، او در جنگ ایران به اهداف نرسید و حالا در مخمصه تنگه هرمز نیز گرفتار شده است.
🔹
هفتصدوپنجاه‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/653690" target="_blank">📅 21:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653689">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039d5d0ee5.mp4?token=tyYPN3v27Ev4uhP0IeCD7kHE78UsGfvDvOOcvNshCSnSBYoPS6E5T3X_S-UnFEPfIbOK0KDrbArHaq86Jh5RnsgvcU4qKs86xCvtOOI8T3Jj29sghGJh5W8tEiFGTuYNp60p45WquRR-EA9gxz1BjfNj8urc14elju7GKRtFJ2waP1WX8GQBmdDprz6bvaZf8ZsKRSlJQsXV9FhRWa73wSTECsIWFv2fxtyW8y8q0zJg1gj5NHQ-lsSiizaLo1XaThTAkLyVx-LMlUMfFvDzjjOawgrDqot4wZcQE7q6IDXIkdrp0I8DLP_XLMfcA1uHjzr3io3o8AlcB-Ipr7bF3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039d5d0ee5.mp4?token=tyYPN3v27Ev4uhP0IeCD7kHE78UsGfvDvOOcvNshCSnSBYoPS6E5T3X_S-UnFEPfIbOK0KDrbArHaq86Jh5RnsgvcU4qKs86xCvtOOI8T3Jj29sghGJh5W8tEiFGTuYNp60p45WquRR-EA9gxz1BjfNj8urc14elju7GKRtFJ2waP1WX8GQBmdDprz6bvaZf8ZsKRSlJQsXV9FhRWa73wSTECsIWFv2fxtyW8y8q0zJg1gj5NHQ-lsSiizaLo1XaThTAkLyVx-LMlUMfFvDzjjOawgrDqot4wZcQE7q6IDXIkdrp0I8DLP_XLMfcA1uHjzr3io3o8AlcB-Ipr7bF3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای تلاش کشتی اماراتی که با رنگ آمیزی و تغییر نام به ایران کرمان، قصد داشت از تنگه هرمز عبور کند اما توسط نیروی دریایی ایران اعمال قانون شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/653689" target="_blank">📅 21:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653688">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97u57AiHlNkEcOnWOnIOinkBBK3ScMmASGnDopWnx6O92x-_mk9QNnNLwCl9PxtQVhM5KR8DgVXb85Tznj-p7oU431xGxjFZVJ4jXselSYO3OqwmEwZEdMrurNgEXWBB7q4RCEbP_n-tT7k5Sb_hWloTkuQs4JXdi6e9CMdVXsgESm3_-7ad_3enxHu0ww2XjgXRrbIqv3_ig8tWSoYZGdSGoc0F_B7DhJn9lqw0mdrOwabcMXOoN6MRkEi9ujgGWlvC0sCqSWhuhWka26mxLQJ1BIhUswPPLc0sTmNcnxw_LHP9lgLt5wdurppTZMYjBjQSkb0QmpLcCtrgcfi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانك ملت در عرصه تامین مالی با عرضه محصول جدید «تیما»/ ۵ خط كسب و كاری مهم كشور تامین مالی می شوند
🔹
بانک ملت با عرضه محصول جدید خود با عنوان «تیما»(تامین یکپارچه مالی ملت ایران)، گام بلندی را در عرصه تامین مالی زنجیره تأمین برداشت.
🔹
تأمین یکپارچه مالی (تیما) به عنوان یک زیرساخت جامع برای ارائه خدمات دیجیتالی اعتباری مکمل فعالیت های گذشته طراحی و عملیاتی شده است
🔹
تیما پنج خط کسب و کاری را شامل تأمین مالی مصرف کنندگان در عمق زنجیره تامین(تیما لایت)، تأمین مالی غیرمستقیم پروژه ها (تیما پرو)، تأمین مالی از طریق لندتک ها (تیما لند)، تأمین مالی در عمق زنجیره تأمین برای صنایع سنگین (تیما پلاس) و تأمین مالی شرکت های توزیع کننده و پخش (تیما پخش) پیگیری می کند.
🔹
تیما با تمرکز بر نیازهای مختلف زنجیره تأمین و با هدف حل مسائل مرتبط با زنجیره های تأمین عادی و پروژه محور به بهره برداری رسیده است و افزایش قدرت خرید مصرف کنندگان، کاهش تأخیر در پرداخت ها و کاهش ریسک نقدینگی در عمق زنجیره تأمین را به همراه خواهد داشت.</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/653688" target="_blank">📅 21:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653687">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbbd6b768.mp4?token=Fz6bJiICjIZ73a_zmzITu6llzERZf9z0rEiZt2aC_0VlBwWTw8NQpeyUbuQvFlvtXWrvMaPpu8HsCJFVjANGLmTHN1iQj4T8YB4ovH1j9QTSFy9Dj3Z2XL6vbYUiylDWS-MBi0_gZxc36f42hbyluppAoYT3CAkiXo88yCDkOeFyVQREnxIx9kJUtUVU8bhpmg4Wew8Q0FRsrBC3NQP_PrXZfj5SZh-IokREzIpNygg4bKAIGdQRw-zxaqCVDkeqVUHxQaRT3AKcXTE6uYPaVHKp5v963EDtyy-kO7ULRREBt6Dczh0NG7FyvmSFpEtbxFBD90YQqY1NzUUuuNi2QIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbbd6b768.mp4?token=Fz6bJiICjIZ73a_zmzITu6llzERZf9z0rEiZt2aC_0VlBwWTw8NQpeyUbuQvFlvtXWrvMaPpu8HsCJFVjANGLmTHN1iQj4T8YB4ovH1j9QTSFy9Dj3Z2XL6vbYUiylDWS-MBi0_gZxc36f42hbyluppAoYT3CAkiXo88yCDkOeFyVQREnxIx9kJUtUVU8bhpmg4Wew8Q0FRsrBC3NQP_PrXZfj5SZh-IokREzIpNygg4bKAIGdQRw-zxaqCVDkeqVUHxQaRT3AKcXTE6uYPaVHKp5v963EDtyy-kO7ULRREBt6Dczh0NG7FyvmSFpEtbxFBD90YQqY1NzUUuuNi2QIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرکبیر چه رنجی از جهل و نادانی کشید ...
تراژدی آبله کوبی و رمال های دربار
👇
https://youtube.com/@caffeinepodcast2025?si=abexgNBj3wu5Tfk7
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/653687" target="_blank">📅 21:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
غریب‌آبادی: غرب تلاش کرد به‌جای محکومیت حمله به تأسیسات هسته‌ای ایران، جای متجاوز و قربانی را عوض کند
🔹
معاون حقوقی و بین‌الملل وزارت امور خارجه: با وجود اینکه در یک سال گذشته تأسیسات هسته‌ای صلح‌آمیز ایران (تحت پادمان) دو بار از سوی آمریکا و اسرائیل هدف حمله قرار گرفته، برخی دولت‌های غربی و آمریکا تلاش کردند به جای تمرکز بر این موضوع، جای متجاوز و قربانی را عوض کنند.
🔹
این کشورها به جای محکومیت حملات، تلاش کردند در سند پایانی اجلاس به بهانه عدم پایبندی ایران به تعهدات پادمانی و قطعنامه‌های شورای امنیت، ایران را محکوم کنند.
🔹
ایران اجازه نداد این هدف سیاسی محقق شود و در نهایت کنفرانس به دلیل زیاده‌خواهی کشورهای غربی بدون تصویب سند نهایی با شکست مواجه شد.
🔹
ایران با سوءاستفاده ابزاری از مجامع و اسناد بین‌المللی مقابله می‌کند.
🔹
اگر نظام عدم اشاعه قرار است بقا داشته باشد، باید بر پایه امنیت برابر، حاکمیت برابر و پاسخگویی برابر بنا شود؛ نه استثناگرایی هسته‌ای.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/653686" target="_blank">📅 21:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
فوری: انتظار می‌رود ایالات متحده و ایران تا بعدازظهر یکشنبه توافقنامه صلحی را با هدف پایان دادن به درگیری‌ها در همه جبهه‌ها اعلام کنند
🔹
پیش‌نویس این توافق در بامداد روز شنبه نهایی و برای تأیید نهایی به رهبری هر دو کشور ارسال شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/akhbarefori/653684" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653683">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سناتور لیندسی گراهام می‌گوید که برخی از رهبران منطقه‌ای، ترامپ را تشویق می‌کنند تا به ایران حمله کند تا رژیم را تضعیف کند و «از موضع قدرت» مذاکره نماید
🔹
به گفته او، برخی دیگر نیز ترامپ را تحت فشار می‌گذارند تا توافق فعلی که روی میز است را بپذیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/653683" target="_blank">📅 20:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653682">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9dd3401e.mp4?token=fTKQWaHLV1omW4vyCBGBL41o4usfwAkRkppxovU09dqkO2ApO8rcm7DVB-kaSglYMpL1bqOwQOkyMUADnt66ZqCo0LL99U7GLmSl-QlkgJBAF5LWd7Ht2jLrDtt5ZKKXXvF19jQfJun8iJyAWLbk465ix7LZZIdOid49_9z_-ytQp1wd6FV_qCShV5TjZid4UO-DFj4WEOMHiBcJQERZil38H7BTgidLj-mMhbJ0S5--aLjpa-jNKuRDhgYdCrnbYBFugj6qBdwYlLBcpkgTJNMx2dlfNIMt99XG_LcFJcnF7EL8D8g9O5hXdbGYXZYESdFqAWA-e3NrvSG_sVYXvIZwVAPsYSvx_Vp0Jt36HhLddKl3ovB8rWzh-5thoFM_WWkU5OYT95o5xTMywFvffkB56c4AuxwEjc1Qquk8ikjha0dmpb1A3DRzNHQlwOnMJHDjt2PtSLd7LcHsIqvzlh4YDKjrEyi_oTv1cFHL-0dsKOkzewFsptRJeIZTv9I-fA-vOousIeVSxYmvxEc_n6MCEHKvfoRx2BGI6_APMAm5wvGU_BgZIA5-n4MPYx_ZO9qeTQ1FzxrGbn-97NovEYK5ASkJo4Dzw8NR9_SnskvqOlmXzUEvGRMi65oR3Een5TOixo1pQiwGxwopafi_pSuiJpWGB8RhnoMeglBiUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9dd3401e.mp4?token=fTKQWaHLV1omW4vyCBGBL41o4usfwAkRkppxovU09dqkO2ApO8rcm7DVB-kaSglYMpL1bqOwQOkyMUADnt66ZqCo0LL99U7GLmSl-QlkgJBAF5LWd7Ht2jLrDtt5ZKKXXvF19jQfJun8iJyAWLbk465ix7LZZIdOid49_9z_-ytQp1wd6FV_qCShV5TjZid4UO-DFj4WEOMHiBcJQERZil38H7BTgidLj-mMhbJ0S5--aLjpa-jNKuRDhgYdCrnbYBFugj6qBdwYlLBcpkgTJNMx2dlfNIMt99XG_LcFJcnF7EL8D8g9O5hXdbGYXZYESdFqAWA-e3NrvSG_sVYXvIZwVAPsYSvx_Vp0Jt36HhLddKl3ovB8rWzh-5thoFM_WWkU5OYT95o5xTMywFvffkB56c4AuxwEjc1Qquk8ikjha0dmpb1A3DRzNHQlwOnMJHDjt2PtSLd7LcHsIqvzlh4YDKjrEyi_oTv1cFHL-0dsKOkzewFsptRJeIZTv9I-fA-vOousIeVSxYmvxEc_n6MCEHKvfoRx2BGI6_APMAm5wvGU_BgZIA5-n4MPYx_ZO9qeTQ1FzxrGbn-97NovEYK5ASkJo4Dzw8NR9_SnskvqOlmXzUEvGRMi65oR3Een5TOixo1pQiwGxwopafi_pSuiJpWGB8RhnoMeglBiUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی دی ونس به کاخ سفید فراخوانده شد
🔹
گزارش‌ها حاکی از بازگشت اضطراری «جی‌دی ونس» معاون اول رئیس‌جمهور آمریکا به کاخ سفید و برگزاری نشست امنیتی ترامپ درباره ایران است.
🔹
«جی‌دی ونس» معاون اول رئیس‌جمهور آمریکا سفرهای خود را نیمه‌تمام گذاشته و به طور اضطراری به کاخ سفید بازگشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/akhbarefori/653682" target="_blank">📅 20:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653681">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
صدای انفجاری در استان سلیمانیه، شمال عراق، شنیده و پس از آن ستون‌های دود در این منطقه دیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/653681" target="_blank">📅 20:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653680">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی به نقل رویترز: ترامپ گفت‌وگوی گروهی با سران عربستان سعودی، قطر، امارات، مصر، ترکیه و پاکستان درباره توافق با ایران برگزار خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/653680" target="_blank">📅 20:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653679">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اکسیوس به نقل از مقامات اسرائیلی: نتانیاهو نسبت به توافقی که در حال مذاکره است، به شدت نگران است و ترامپ را به انجام یک دور جدید از حملات تشویق کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653679" target="_blank">📅 20:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653678">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06609fc3d1.mp4?token=sexhduwTkHgZ9Xi3kWLX8LOskNgzCRR-_xeu1qViX3xW0o20FWkz28qXmSrXoUw1-4uvyn_j6MWsorx9AtZc-938tLKvDYmE9YoEjW8t3xbbyRL6t5m01NuH79qZ7Mp_Voo6KSOundv0LRro8FA3-y2EtL7tsYjNLDe4wyG00cVmPuLVpdvQmW78NOQqt7ih8uFfys7wu3ZgKw6O17loBLw3QXd01JfxmeYvza7eywVrMSfz3ioZTyCRyhOqHVyDtI-kUGzIp0E9coRxCsKqDffK_PyePS5HVPY4cR6VD7xEvb3m1Cgky9lVKlP9uKCzG-NC2advSKRFoxm7Kq5pug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06609fc3d1.mp4?token=sexhduwTkHgZ9Xi3kWLX8LOskNgzCRR-_xeu1qViX3xW0o20FWkz28qXmSrXoUw1-4uvyn_j6MWsorx9AtZc-938tLKvDYmE9YoEjW8t3xbbyRL6t5m01NuH79qZ7Mp_Voo6KSOundv0LRro8FA3-y2EtL7tsYjNLDe4wyG00cVmPuLVpdvQmW78NOQqt7ih8uFfys7wu3ZgKw6O17loBLw3QXd01JfxmeYvza7eywVrMSfz3ioZTyCRyhOqHVyDtI-kUGzIp0E9coRxCsKqDffK_PyePS5HVPY4cR6VD7xEvb3m1Cgky9lVKlP9uKCzG-NC2advSKRFoxm7Kq5pug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا:
🔹
ما از نیروهای هوابرد و واکنش سریع خود خواسته‌ایم که در هر لحظه برای اعزام به خاورمیانه آماده باشند.
🔹
این نیروها به‌عنوان یک سپر آهنی در برابر عوامل نیابتی ایران، از پایگاه‌های آمریکایی و جان شهروندان آمریکایی محافظت می‌کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/akhbarefori/653678" target="_blank">📅 20:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653677">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCBd7LhiENDRpBdqUa96X2QiKmpNS0YbMqbgdQlL3t7TahoVAHWEtAbmF6hsMfMi3tp376fG93Gb5zg1inTvtfKkiUgNGhq-8HyuHBfTA_WsbrpcD-NgiAHxfs44uSfdk0WVxo3dhj-lAShO9NHhiIjvzfVUUr8qOqPwmICtve6O4IURWCj6ZU7rc8yVNcRRuMNX2h-yQFsY7QLB1E0Rkq743DgFe9LQbuVjZYnwGzBFSdZjYGtwZS-cSbfwrB_VnzFgQKmDFrMSkD1Fc6ajxSSsyW1JVDIfgIBBXVh9yNX2DEZ_ZTd9gQjw7S7r6l0Dj896K48FFmVP3zD9ywVLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محکومیت شدید جنایات رژیم صهیونیستی علیه لبنان
🔹
سخنگوی وزارت امور خارجه، ادامه حملات وحشیانه رژیم صهیونیستی علیه لبنان طی چند روز اخیر، که منجر به شهید و مجروح‌شدن ده‌ها نفر از جمله چند امدادگر و یک خبرنگار و عکاس لبنانی -احمد حریری- و تخریب گسترده زیرساخت‌های این کشور شده است، را به شدت محکوم کرد.
🔹
سخنگوی وزارت امور خارجه با اشاره به نقض‌ مستمر حاکمیت ملی و تمامیت سرزمینی لبنان و شهادت بیش از سه هزار نفر و مجروح شدن بیش از ۹ هزار نفر در حملات تروریستی رژیم اشغالگر علیه لبنان طی ۳ ماه اخیر، بی‌تفاوتی و بی‌عملی شورای امنیت سازمان ملل متحد در قبال این جنایات را شرم‌آور دانست و بر ضرورت اقدام عاجل جهان اسلام، خصوصا از طریق سازمان همکاری اسلامی، برای توقف اشغالگری و جنایات رژیم صهیونیستی تأکید کرد.
🔹
سخنگوی وزارت امور خارجه با تمجید از صبر و مقاومت مردم لبنان در برابر تجاوز و اشغالگری رژیم صهیونیستی، به خانواده‌های شهدا و مردم و دولت لبنان تسلیت گفت و بر همبستگی کامل جمهوری اسلامی ایران با لبنان در مسیر دفاع از حاکمیت و استقلال لبنان تاکید نمود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/653677" target="_blank">📅 20:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653676">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad6a5fa78.mp4?token=HOUTUSVs9cf71lSr-vmZDRvnM2F9m69e6FXd6ZET4MSXwjObUx3IVaRWmEGGoRfizJNR005XPZldHpAwAgpCGUhB_-B3X5UNyO-MS3ZTBL98NjfdLrIRFyOoIyMEl1lSTARcSJ5SiNGRWM7235zwezkeOnH2K2kuEbGXHhLdFLwxBcFlYOFZGe5cAdXf14iVXxe4KG8JJ1X0dPCZd4bREvD8jZI-Y5_v72OzjGUOQ5tyA5zwgHphE-CP4tfbJsKqlirkOrSKfdK20nV2pljtZ8IbMMS1Ouk5qwiWI66MZffIBn-UwNMOcqBKa31R9EpFCdrZo1SbPqbZDkvNqLttxp_WMl16SXTFpW3u44cfBaMpfYnDH8EnrpIU-GJv2ImIXBJi9p_LGHG6Q5T5x1oGnA3x2CaRamnB-MqPSIcXKabD2jlDEj06QA5UN229QKYQZnmDR6rrfklTIh9f4US8MTXVXQs-NPRVdFiJm85_oNqvu7MFac9ielpzIxwwPZaiEh7xVb5MKAIfqs-_f1bg2slO3Lv-mDlhun-xK114XfHQyo2Zl-rggoV8d0LnEZterPLzner50DK2sjrke_c97QF1ImSIX4aqYEMHrwl8uYP8fTQ38KTKvYAAA_fBvyDPg7NsDEiYHPGRG6bJt_h9hFzoxpbQgvSGTdndqzrln4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad6a5fa78.mp4?token=HOUTUSVs9cf71lSr-vmZDRvnM2F9m69e6FXd6ZET4MSXwjObUx3IVaRWmEGGoRfizJNR005XPZldHpAwAgpCGUhB_-B3X5UNyO-MS3ZTBL98NjfdLrIRFyOoIyMEl1lSTARcSJ5SiNGRWM7235zwezkeOnH2K2kuEbGXHhLdFLwxBcFlYOFZGe5cAdXf14iVXxe4KG8JJ1X0dPCZd4bREvD8jZI-Y5_v72OzjGUOQ5tyA5zwgHphE-CP4tfbJsKqlirkOrSKfdK20nV2pljtZ8IbMMS1Ouk5qwiWI66MZffIBn-UwNMOcqBKa31R9EpFCdrZo1SbPqbZDkvNqLttxp_WMl16SXTFpW3u44cfBaMpfYnDH8EnrpIU-GJv2ImIXBJi9p_LGHG6Q5T5x1oGnA3x2CaRamnB-MqPSIcXKabD2jlDEj06QA5UN229QKYQZnmDR6rrfklTIh9f4US8MTXVXQs-NPRVdFiJm85_oNqvu7MFac9ielpzIxwwPZaiEh7xVb5MKAIfqs-_f1bg2slO3Lv-mDlhun-xK114XfHQyo2Zl-rggoV8d0LnEZterPLzner50DK2sjrke_c97QF1ImSIX4aqYEMHrwl8uYP8fTQ38KTKvYAAA_fBvyDPg7NsDEiYHPGRG6bJt_h9hFzoxpbQgvSGTdndqzrln4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف‌قراردادن خودروی فرماندهٔ تیپ ۳۰۰ ارتش رژیم‌صهیونیستی توسط حزب‌الله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/653676" target="_blank">📅 20:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653675">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان به نقل از منبع مطلع: بن‌بست در مذاکرات میان ایران و آمریکا پایان یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/653675" target="_blank">📅 20:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653674">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apGMN_zAoY0_XCMl_QryNmzS-ROk0ruQpq59JTlRSvnvxghB7K-N7T7oCNyGDxJb6o7xUzYa5XWPvvmT4ykvur4g8b5l6hI1G1hqOOm2Ak9qLGL0NJag5XSK3JmAx4bu6HzzLEI56kNbfNUIUJdgQ5yzKP3TZ4llsDl_qxGPrdeNl9umbOi4gZZ31dMH34iotl8_7pmRM01ucwr1qGQXRVs8hyLMbAUDJq-aCfGAd_g-9sp4Gu42xwodIliS_4IDE-k4m9M7uI1e5eEFNuWgJ-TusaNVCQgHoEBSMuYGRlRilxLK7RLHhZA4MC25rRU6U-Jr5uud7JiHYsvZImxA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتورسیکلت بنلی TNT15
✅
در کلاس شهری
✅
انجین بازطراحی‌شده برای یک سواری راحت
⭕
5 درصد تخفیف
⭕
اقساط 24 ماهه
جهت مشاهده قیمت نقد و اقساط روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/ei1
🏍️</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/653674" target="_blank">📅 20:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653673">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
هنوز بر سر موضوع هسته‌ای، پول‌های بلوکه و کنترل ایران بر تنگه هرمز اختلافات جدی پابرجاست که اگر حل نشود مذاکره انجام نمی‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/653673" target="_blank">📅 20:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653672">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تناقض‌های آمریکایی به روایت سی‌بی‌اس: دولت ترامپ علی‌رغم تلاش‌های دیپلماتیک مداوم، در حال آماده شدن برای حملات نظامی جدید علیه ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/653672" target="_blank">📅 19:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653671">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ترامپ به سی‌بی‌اس گفت «پیش‌نویسی» از یک توافق با ایران وجود دارد که قبلاً آن را بررسی کرده، اما از گفتن این که آیا آن را تأیید کرده یا نه خودداری کرد و گفت: «نمی‌توانم قبل از این که به آنها بگویم، به شما (رسانه‌ها) بگویم» و اضافه کرد که مذاکرات «بسیار نزدیک‌تر» می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/653671" target="_blank">📅 19:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
جلسه وبیناری مجلس با حضور وزیر بهداشت برای بررسی مشکلات درمان و دارو برگزار می‌شود
🔹
گودرزی سخنگوی هیأت رئیسه مجلس: نشست وبیناری مجلس برای بررسی مسائل حوزه درمان و دارو فردا (یکشنبه ۳ خرداد) با حضور وزیر بهداشت برگزار می‌شود.
🔹
گرانی‌های اخیر در حوزه دارو و مشکلات درمانی مردم، محور اصلی این نشست خواهد بود و نمایندگان مجلس به همراه وزیر بهداشت به بررسی راهکارهای رفع این چالش‌ها می‌پردازند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/653670" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653669">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCU1HsIkojEtyrs4fOweeIiY7Qx2-gjgxKIJSukedcXs7-3pg2B5PfmQEDjDvnGSL1N4kZYYkB5Fymg7Kw8LmwyqkCbN-h-L-WkfRtbjyUlVPNsVvsaKC7iLi5rvMq9vNkQD2hNZhZEDzIMM63b8ve0w3_ZWlZtSmKxhoONTlOWtnD3Pqd_XdNqd2T7PC7uHxswZGkHQxzdwTRxUnWPFzpgDI3239Kge6YL-uooN1zGbunwm3m5F8-PK5IRNzraFDI-Xgmsq6UMEOYjYwAweYIs2QaD8XcHEawB_30kptAJ_ZmmLlqbvtnLx81uv7QYbdWGsrihWUr8lu8Hb3HFGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلند شدن ستون دود در پایگاه نظامی صهیونیست‌ها
🔹
رسانه‌های صهیونیستی از وقوع آتش‌سوزی در یکی از پایگاه‌های نظامی ارتش این رژیم در منطقه الجلیل غربی خبر دادند.
🔹
بر اساس گزارش‌ها، دود غلیظی از داخل این پایگاه نظامی به دلیل اصابت پهپاد حزب‌الله مشاهده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/653669" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653668">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ترامپ: تنها توافقی را قبول خواهم کرد که سرنوشت اورانیوم غنی شده در ایران را مشخص کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/653668" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653667">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9a4dd220.mp4?token=D9C4GW3vanaP5opkuEwWVZ_nFr2SMg19xtl5hBFYAdeGfI8e41g0ukff6fl1OEmeC-HNAYPGJPQ5P2z0MiGquqX9-8JEqXEZdPSpzIJ-ryK8KIL-Zck-OJli--V7Wmxx6f6clpoXuZOynQtRmxrPh1R6QpPlIl7zPEg3DFqSERiykxDR7mpMosjkmB0M2tkC9C46fQ0QzHTqBXM2slbZSNCYHAdszoj_0v-hYgxNt1Hieu9w5OUzeKKR2grAARyqbek3_g81Mj-xkVCGmyPl0jYffoPy0qB686wJs_srUXxK--1Qhj2abRfRb7BijADxEYSNUHqKmjcHG8wP5TlV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9a4dd220.mp4?token=D9C4GW3vanaP5opkuEwWVZ_nFr2SMg19xtl5hBFYAdeGfI8e41g0ukff6fl1OEmeC-HNAYPGJPQ5P2z0MiGquqX9-8JEqXEZdPSpzIJ-ryK8KIL-Zck-OJli--V7Wmxx6f6clpoXuZOynQtRmxrPh1R6QpPlIl7zPEg3DFqSERiykxDR7mpMosjkmB0M2tkC9C46fQ0QzHTqBXM2slbZSNCYHAdszoj_0v-hYgxNt1Hieu9w5OUzeKKR2grAARyqbek3_g81Mj-xkVCGmyPl0jYffoPy0qB686wJs_srUXxK--1Qhj2abRfRb7BijADxEYSNUHqKmjcHG8wP5TlV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقی‌پور، نماینده مجلس: شبکۀ حیاتی کابل‌های فیبر نوری جهان از تنگۀ هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/653667" target="_blank">📅 19:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653666">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
فوری| ترامپ به اَکسیوس گفت که شانس «۵۰-۵۰» برای این موضوع وجود دارد که یا با ایران به توافق برسد یا جنگ را از سر بگیرد
🔹
او گفت: «یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم.»
🔹
ترامپ روز شنبه با استیو ویتکاف و جرد کوشنر دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند و انتظار می‌رود تا یکشنبه تصمیم‌گیری شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/653666" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILzQKENc4VxuQ8RrDDE790LptgoehVbFqXC3ldOwu9f_t1GkUnyFnVzX1bAEfuSHOMd-0gmOJDFvFyy-iQONra8aycmi1mhQKxqscLtC-qct_HME2wZpUxKXkjI9ydaGOJz5wzCxL8n5i9QOsO2GylSpoCnab2-wWQRhy4R89JOuJnS1SefUL5g-994KOUwLdOvJLUU5-vQzBGJrQz9HuKaN9moYrs3EdvaYTcoXlc2LmIu8adkpuDX9itD7vee4OQM4oroB_d2QjoO2I5HPTk-tibuSK3ErcUU99zMa_7DdTeYOexqQouaLlIXI3iB3x0ApfIWAHEFSw7i86_j5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوهای تلفنی وزیر امور خارجه جمهوری اسلامی ایران با همتایان قطری و مصری
🔹
سید عباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران عصر امروز شنبه در تماس‌های تلفنی جداگانه با شیخ محمد بن عبدالرحمن آل ثانی وزیر امور خارجه قطر و بدر عبدالعاطی وزیر امور خارجه مصر، درباره موضوعات روند آخرین تلاش ها و ابتکارات دیپلماتیک برای جلوگیری از تشدید تنش و خاتمه دائمی جنگ تحمیلی امریکا و رژیم صهیونیستی علی ایران گفتگو و تبادل نظر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/653665" target="_blank">📅 19:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFYImi93wRYahFi-u3xodruTgXJfSbR2FDeRwL4moOO7SU2mqH8fZ3rMOy0UT-NYIvbyytedzuKQgNITKslOeObLUypZBdBiRBhS-Eu5RQNfF-AmEA4L-G-nRhdu4hDbQYWC_v4G1TnfZlz35clTcsQ6kdzPTi4sD7-uXkamv53D2SgDhZvQcG9aFwdQBb3cUNrrNpgA-U7JdYEHjkD2-vLQsQucADqRZtdxF9Py2br5utluz2mqJ97eSGpz_a9Uw79JsttCpZUJbQkDPL1OsarUgmSZN925D1OpKWpyDIN6n8srDuIPDgVYqRDE191g9zWvNaLmWnKSN-hqvazY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: تکبر اسرائیل در حال تبدیل شدن به مدرکی علیه خودش است
🔹
ویدئوی بن‌گویر (وزیر امنیت اسرائیل) از آزار و اذیت فعالان کشتی‌های امدادی [کاروان صمود]، نشان‌دهنده حکومتی است که آن‌قدر به مصونیت از مجازات عادت کرده که حتی ظلمش علیه غربی‌ها را هم مستند می‌کند.
🔹
در این تصاویر، بن‌گویر در حال تمسخر فعالان حامی فلسطین است که به اجبار با دست‌های بسته روی زمین زانو زده اند و پیشانی خود را به کف اتاق چسبانده‌اند؛ رویکردی که پیش از این نیز در گزارش‌های متعدد درباره شکنجه و آزار جنسی فلسطینیان مستند شده بود.
🔹
انتشار عامدانه این تصاویر نشان‌دهنده اطمینان کامل مقامات اسرائیل از عدم مواجهه با هرگونه مجازات یا پیگرد قانونی است.
🔹
با این حال پس از انتشار این ویدئو، موجی از محکومیت‌های بین‌المللی علیه این اقدام شکل گرفت که نشان می‌دهد افکار عمومی جهان به‌شدت علیه تل‌آویو تغییر کرده و حمایت بی‌قیدوشرط از آن به یک بارِ سیاسی سنگین در غرب تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/653664" target="_blank">📅 19:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653660">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اسلام‌آباد تلاش دارد دور دوم مذاکرات مستقیم بین تهران و واشنگتن را محقق کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/653660" target="_blank">📅 18:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فعال اصلاح‌طلب: اعتراف می‌کنم در نقد به دکترین دفاعی رهبر شهید اشتباه کردیم
🔹
علی باقری، دبیرکل حزب عهد ایران در گفت‌وگو با: رهبر شهید، معمار بازسازی قدرت ایران در جهان بود.
🔹
عملکرد ایران در جنگ‌های اخیر و مقابله با قدرت‌های بزرگ نظامی، نتیجه دکترین دفاعی‌ای بود که رهبر شهید طی سه دهه طراحی و تثبیت کردند؛ دکترینی که امروز قدرت نظامی ایران را به واقعیتی غیرقابل انکار تبدیل کرده است.
🔹
مهم‌ترین میراث ۳۷ سال رهبری ایشان، ساختن «ایران قدرتمند» است؛ کشوری که توان ایستادگی و مقابله با دشمنان خود را دارد.
🔹
این دکترین سال‌ها از داخل و خارج مورد نقد بود و ما در جریان اصلاحات هم به آن انتقاد داشتیم؛ اما جنگ ۴۰ روزه و پیش از آن جنگ ۱۲ روزه نشان داد این طراحی دقیق، هدفمند و کاملاً درست بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/akhbarefori/653659" target="_blank">📅 18:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfmn1VvKIUnpd8MCuS3tjuZ7NN4OMrwpW-9n95zR1WTPkpTmunYE6NSvzMAn88HqKHwp559cwjqGBgvownkEFppg6DN91eCJFTUTAofkP-DvZZ2N1BHsn4rIhG9uGm4Z1iCkwYaWEIAlD1Eo5I_mHcVPqvZcR8SrwNP1qaaZ2rqwWk-0EOnvzDynbkYwoMZaZUymmoYcrgodpwlz-PEGk2VJnv3fYKvTPq_uy1yANcTSHNXi_aVSIt4QOkW9WfnCehogSGkItwTa8iLBIEYxXrvp4IupT79204BRKgOMfU8G66W37WIaQO4LPkVROYeC0o7E4POtVdMPoYshY4rx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حیرت کاخ سفید از «اشیاء مرموز» در تنگه هرمز / این سلاح مرموز ایرانی بدجور آمریکا را ترسانده است
🔹
بررسی تصاویر ویدئویی منتشره از سوی کاخ سفید نشان می دهد که اشیاء ناشناس همان «قایق های تندرو ایران» هستند که در آب های خلیج فارس در حرکتند. این قایق ها با تغییر کاربری و موتور، دارای سرعتی بالا (حتی تا 200 کیلومتر در ساعت) شده اند و به همین دلیل، تصاویر ماهواره ای آمریکا نتوانسته پی به حقیقت آنها ببرد و گمان برده آنها اشیاء پرنده ناشناس یا حتی یوفو هستند.
دراین‌باره بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3217248</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653658" target="_blank">📅 18:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854eb6914b.mp4?token=EDv3cnJnPFAgDeXQfUDl-1ZVqj1f3slsyq8UBr8-RutuoAMrzUGgwuAOUXBOcZ2BUATIOax6fMJuub8FkCwwCNMQPwcBCiQow7vULs2NX7P5f0bu06YGdIfsSj3JDhy_lgbxz3GU8OL5UmEyMDWGPpQ7z342B1C_eEpg3yXzr_AywTNcr5nYLG1koIaMU5RPlu1Exbu6ttcM5obZmb8B4--7Sf4IxRBUp3gzrpwqd21LtiZEzCuyzyUfr_473vRGgwGAo_rprTKXzdQHnGriaLgAH6vJ_Nw0zd_dkZzaGxe2xz4lma_AX3D_m0bKkwIpKXDCWhqayVxlPUf6lr2EL7apPNcE029pWHXI-cKurn07UrA4m0HG2KGIuFNr9pkIXLkLC5Yg9KzQokXPUZv1RJNolpPT3SLtD76t8wVrXMIB_LfVWsI0IFIQ_Taq9IMw-NI2qWl4iEIbt5husxqVxQ-Yw2Y3IoG2oKiiJbqypjK80bteKyCR1Eegs4ue92WnfngVB3IYdfp5IGLpResWOE8ZbC7fZfekwTxz_dRzDOSrnaOanAoAb6XdDccpaiFtYiliwIfVCeFlWuHHGKcrz4cqQXtGsVTzn1uSAcmMbHZGB45bQxRMqAL_lYY_FZJtFWqiubFPBls3p_IsQ67wmB1JGT8GcchJEKzAtgKFVc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854eb6914b.mp4?token=EDv3cnJnPFAgDeXQfUDl-1ZVqj1f3slsyq8UBr8-RutuoAMrzUGgwuAOUXBOcZ2BUATIOax6fMJuub8FkCwwCNMQPwcBCiQow7vULs2NX7P5f0bu06YGdIfsSj3JDhy_lgbxz3GU8OL5UmEyMDWGPpQ7z342B1C_eEpg3yXzr_AywTNcr5nYLG1koIaMU5RPlu1Exbu6ttcM5obZmb8B4--7Sf4IxRBUp3gzrpwqd21LtiZEzCuyzyUfr_473vRGgwGAo_rprTKXzdQHnGriaLgAH6vJ_Nw0zd_dkZzaGxe2xz4lma_AX3D_m0bKkwIpKXDCWhqayVxlPUf6lr2EL7apPNcE029pWHXI-cKurn07UrA4m0HG2KGIuFNr9pkIXLkLC5Yg9KzQokXPUZv1RJNolpPT3SLtD76t8wVrXMIB_LfVWsI0IFIQ_Taq9IMw-NI2qWl4iEIbt5husxqVxQ-Yw2Y3IoG2oKiiJbqypjK80bteKyCR1Eegs4ue92WnfngVB3IYdfp5IGLpResWOE8ZbC7fZfekwTxz_dRzDOSrnaOanAoAb6XdDccpaiFtYiliwIfVCeFlWuHHGKcrz4cqQXtGsVTzn1uSAcmMbHZGB45bQxRMqAL_lYY_FZJtFWqiubFPBls3p_IsQ67wmB1JGT8GcchJEKzAtgKFVc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر شبکه افق: برای اولین بار اعلام می‌کنم که حضرت آقا تجمعات را از تلویزیون دنبال می‌کنند و از جمعیت زیاد تجمعات خوشحال هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653657" target="_blank">📅 18:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88702db038.mp4?token=h7JO0UveaQt4zGpL61GVsPLWZQvKPiuJOGESfvibbNUv952Kljn22Lqe83m8f7rk4CewFuDIm8ECwzTq9baiFkhx5jN7GxTDZFb0EDPF4_JjbPXYKbzY95fjyUBwtENsR4vQyyCff59Ir2GycEscQUwoLZhZr_ptrUbBwkD74lfmZ19yfIKGYuO8m4QI26V-YgdZcOZ-Lhy9lFHg8VvLe1DfK5DQzuaTKN3ca6iFFxK_0Z697Dw2glhOY2_1GH7KX0ZUqRXnW_SLvw_eSoRthjU2xuAFVn5tYl3F-p_jldhe7mQMFNkatql4MdCU258pesE4Y8gSjZbbdoKzR2ZdCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88702db038.mp4?token=h7JO0UveaQt4zGpL61GVsPLWZQvKPiuJOGESfvibbNUv952Kljn22Lqe83m8f7rk4CewFuDIm8ECwzTq9baiFkhx5jN7GxTDZFb0EDPF4_JjbPXYKbzY95fjyUBwtENsR4vQyyCff59Ir2GycEscQUwoLZhZr_ptrUbBwkD74lfmZ19yfIKGYuO8m4QI26V-YgdZcOZ-Lhy9lFHg8VvLe1DfK5DQzuaTKN3ca6iFFxK_0Z697Dw2glhOY2_1GH7KX0ZUqRXnW_SLvw_eSoRthjU2xuAFVn5tYl3F-p_jldhe7mQMFNkatql4MdCU258pesE4Y8gSjZbbdoKzR2ZdCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا پایان شهریور واردات کالاهای اساسی توسط همه اشخاص کاملاً آزاد است
🔹
وزیر کشاورزی در نشست دکتر پزشکیان با استانداران: حداقل تا پایان شهریور ماه به دلیل شرایطی که در آن قرار داریم، واردات کالاهای اساسی توسط همه اشخاص حقیقی و حقوقی و بدون هیچ محدودیتی از همه مبادی کشور کاملاً آزاد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/653656" target="_blank">📅 18:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOFDBD8LgJ-CxVJy9e3EIEZ6h_GTIUivfIK-NHLM3xrvrsAj37r5x3qhRcbTDIYEjeKuVpkpUAN-8MR6hCPuIQ-p7-q9AhPxRwcd9K1QeXwyAR4jp68QENKqsO7dBublJuF78MTbY7w4i8LJXblAfA9N7kBV8h4ip8vAHgh42rzdUX-gGeXjfqjak4oBNieGRKhgXds62j8ZmdLt0oXFrAg2XI7L8esb8YcDCXi2526Cgpk7sQLFbaxBqaI2tHf4zjOotjKPQeduubIGBvDMSNz2b9U0NYzcRw0OfM9EmHDbix44KW8XnkUJeXI1VVLQhRV4VkSI1uSQc35QhtwpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فائو: تنگهٔ هرمز بسته بماند، جهان با یک بحران غذایی مواجه خواهد شد
🔹
سازمان کشاورزی ملل متحد: ادامه بسته‌ماندن تنگهٔ هرمز آغاز یک شوک ساختاری در نظام غذایی جهان است و آثار این شوک طی بازهٔ زمانی ۶ تا ۱۲ ماه آینده ظاهر خواهد شد، به‌طوری‌که یک خانواده ۴ نفره در اروپا برای خرید یک قرص نان باید پول یک وعدهٔ غذا را بدهد.
🔹
افزایش قیمت انرژی، قیمت گندم و برنج را نیز بالا برده است.
🔹
کارشناسان پیش‌بینی می‌کنند در ۱۲ ماه آینده قیمت نان در جهان ۳۵ تا ۴۵ درصد افزایش یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653655" target="_blank">📅 18:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای العربیه: تهران در ازای پرداخت غرامت از سوی آمریکا به ایران، پیشنهاد بازگشایی تنگه هرمز را ارائه کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/akhbarefori/653654" target="_blank">📅 17:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653652">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در شمال اراضی اشغالی
🔹
ارتش رژیم صهیونیستی اعلام کرد که در پی نفوذ پهپادی متخاصم، آژیرهای هشدار در شهرک شلومی واقع در شمال اراضی اشغالی به صدا درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/653652" target="_blank">📅 17:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653651">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مصوبه جدید دولت برای حمایت از آسیب‌دیدگان بندر شهید رجایی/ رشد ۷۵ درصدی اعطای وام ازدواج
🔹
سخنگوی دولت: موضوعی که در دولت به تصویب رسید؛ تضمین‌های مالی تودیع‌شده برای فعالان اقتصادی آسیب‌دیده از حادثه بندر شهید رجایی بود که تا پایان مرداد ۱۴۰۵ با آن موافقت شد.
🔹
سال گذشته میزان اعطای تسهیلات قرض‌الحسنه ازدواج ۲۰۰ هزار میلیارد تومان بود که امسال با رشد ۷۵ درصدی به ۳۵۰ هزار میلیارد تومان رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/653651" target="_blank">📅 17:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای روبیو: پیشرفت‌هایی در قبال پرونده ایران حاصل شده است
🔹
مارکو روبیو، وزیر خارجه آمریکا:
🔹
تنگه هرمز باید باز شود؛ ایران نباید سلاح هسته ای داشته باشد؛
🔹
ایران باید ذخایر اورانیوم غنی شده خود را تحویل دهد؛ معضل غنی‌سازی ایران باید در مذاکرات در نظر گرفته شود؛
🔹
خواسته‌های رئیس جمهور به هر شکلی باید محقق شود؛ اولویت ما مسیر دیپلماتیک است؛ امیدواریم که از طریق دیپلماسی حل شود؛
🔹
احتمال دارد که امروز، فردا یا طی چند روز آینده مطالب قابل‌توجهی برای گفتن داشته باشیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/akhbarefori/653650" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
