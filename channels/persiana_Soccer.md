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
<img src="https://cdn4.telesco.pe/file/S7F72QmCcMignJQwYJ957PtKh_B6xkSLNPTi-Xtw1sxwipbJDiawWGBOtKlnalxhjy-WbOgjouz1wX326XOknVklEk58MQA0CmmYz7XVfM0Hs3OSV3gk458Bh5olzdiwb3p71Hp61iwJxufpbM_gJ6e33-Bvh37hOawS4kcFRmajkPWRKjsRqDcZn7MmBE8dAIr-XyKm5YvKIjJUilx4UWrk3uYVPGFr546HVnd7n_yfuXi3VVxckwL-a53UqftUG_so_VqP0ZQN5EtLjLDMkLfjFPqT0t9K2dtrZknaC9qqlEBVSOyWvj4SJ_0pL2ic7bj0_VgFSKSB8Jz48wskqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 196K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-tc1fid7QZA7WNLJ0R3_MBBbaezM0ztCbAb10Nau7z5MVEFIKMftHOQHFkWGn6M89mMxvNspecMdBK6q_VFH4PYQoSY_UvKYwDyummRpcvlzAqYYVgT5W7vJ2-x_M8B4I0teWl4gvVMhxZZ7rHEuQzLMxJ3OL_2b3SPyO30yaiT8Z3_l3vEUS3Kiq9Ax21S6uUcRZ4xj7Pjl8j9s_4SopgRIU1_AaI8m8Mwsrb6lC7WLQqtIAFsklSUIB-tgg-dufWFICAZsu6MvJj6jbjpZhaSTved0NWVpH_c-BFPWGNxUpnxc5vt5pJs1Ap_jfwnSxX8VZHShTHv21qhhylAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOkixufHAi4gRsE9yokVrcxsDU_IM1V_gteRx8EZJxAL0S24z1u-DtW0WGxM8eJb9d4SzYk9q3aRQYJLoAIhyPCacpfSm2g1ryvZZWCS9uVK753LUHDuXCPvnh0CZlqJaPop3_nS0oo-Sz2quAD0I6JfhBQSYjQ2gfKK7zcIG7LAd4_dI28-mb_DskJ9hEEnLEzHBdXBe8P4Y7MouKuBrrBDhrP5RZwZ_fgwhDohAXVYRnfX3QH8MxTXNRwCelfYQbsrOVgvrOy4rik3FLOxPWyiB_hFFFWBxXbrDIlTmO4k-Hh9JUgBCWZ9_YvsBKkxzILHxk-JISNI1UX3tPGn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeqkWxonFAn5eypWDczGj3rcuElDpiV-3N56UIVKEppgWUGfHzlKDn-D1Ahqh7XdzPyJoUG_c_5j_-wpX5LVDDOoib7gxbjJ_BOk2gUGBkJiPVH3yVBYdFyipGfinVs7ZYif1OTkll5oCpQPWO8gXCchE5YLvVI10VmFn4gME6JXJjMiNPrBcWUCBK6V5MjvKneZGvNQANjHJsAueriYkqmrT5ym1_IZDlD29uUfpIVz4ktn_xDXRmMQn9vlCzBicyfgZMXmPTD-7aWRLWcTggXNTQEoB-hEzUM1suRRmfZ2jijQNK-LTqPzhYOSL5grdf20UGbH0pDzawHKQUIyIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPvx_nKbp2P9Q9MGsJPV8hvjkvJ4Be-uiwSyApgpT4kI_EOlwKgwBPHgaAAQmkVqLYaoNGo6B_WNhV1VpWrtHdMhCSG51bIi0zHvXg2yDdCyHBNVGTMLDCMqMzvkMhWuP_hVSMo2RolvNCbEMN9qzNFm1FzTt9MO5DPcf1p1mV2a2xKaeYsG16xkCotvE9eooPH47NdPqRkTofOUb4tbYUK-YGtYHDHJ6ISL-7vbTY_xUCLhIHWHbcD14s1H0azs2qi4YvDWFKFByRjjXRL6XRLqiBIcc7VBYFG2qtnsSPeaqGG0xo5TgOwDknHprv3FtFdplkNtJi-aSU5MULA-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnZE6Qec2JeTp6BFB2Sh7vts2ctiTzuofh-K1Kkpb6rlBxoumPFdv5Tqb7SSFFurt_-wJBHar11k5bgSuG5XvrpJ4kyFOO2Kzo-RHImh6ZGTsD458uAceak3Xn72z57m2ZHKR3lJWWWZRtUdXqjfFUiWy-kt-BC4n1jYnxEFsb0pL95uR8WZJeNbua-4Q9HugdR1Opa7t9qZ6nBYS_v7aD9oikWWmRfVhLH_UnMNAkgfNYOgHWhGIZN4S0lvhz21DE2pf8aerzc59nf0WWs_tTYMa1IXnFYC-QkGu48E7r4esCmNvwzRtlwkMewMmn6NlFCM2obKunbyUf6Mf-hxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgEhGh4r8EQF82njjeWc_dTYSEBpr7QxfgpbI6vG6jiWCUkZ3SY2IkYvQobdoH0bSdNHF8ZSHYtV2XBX246HJfLGQgbS4TWopZVDIXlbkovSrjeZ5eq5SmALQbpX42EzNCXzDi68bLyAI-EduvDPgf7S5FzmTF5mhzSI3FJLfrfrBjGQOsv1cMeM5dnRlK1wibMaqMIjW4ES5M1tpQ_yjK3NngDqbuczDMX82iL9DoS176ovWZVSIb9FqT1nXdcdON1Qvg3cLLI9QvjA5BLQoqOq5fQCR0YvSpOHA6Of9DAYJflzDo6InX93v3sAXc5fCIYHuSNt2LLgw4anAzjc_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfN6yTPE5MWEgaj6Golc42wcTUk6w5Bcu759QnG8wdSwG0iQXUpGfgTU6bJmoR8YrVg2U-TxcP3W8nrwMAYEfAWBV0ugK7VZ6IflKvPn4odgkiAvvIq4eK0RVm-UuA9jdtZmoBugGJb00Hdu8_TTGcNMQn7JqpsAEIJu5GxCw4eDWlG68gKB-hcbplVgPvL5evbLBLN9_LSCSA1WJJ48D6TiersKrKqhXHaR9lMEpS_qu6Q8Leyrff8X8sjeTQqbZtNbvxYajFGYn2SvcpV0TmFjndJvWszUeo-WRjOeSV3_Gf17CSkLOyP9u_WAGH_vpDL0D8FSGEm5u1QZE4ikpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0uWg-WR75CbOEjoLnxSyj2oXkRoyyAk8f-xyYf4A24e9RTJ_W6GeQO-12UuK8HyRkypYVKUvyt49fEb3Hx5FxiO6gEd04xUDEd8hVHsgMfNmhy7p3RBARpVUoIGro-0z0NLLlZuvaHo2FOBjMrllcEETcY_pC8OQUtcl-jSMINcYU959nPHxXWxoOZ7q__BrrC4G8snAoZTLIWglKXcwLU2cYhkUnuscUOAMYmKnoRs1wPIqdvkPsYZdaYw9D-Omh74In0Zi_F_i3miynfFInmLWJxMF7fP4qXpwObXmeommqB2mwzvQfXXnsxVzzloKEfPzgKNyqHay-8vHgT_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubt7G-e2Y55BOsNYiTq8AHGD7fa2eXzcqxieyAZ-fh7BYsJbdankqHOSeiKQ_x0WM79QtkdfnxMDjbq9X9X_QWJOpiETU3hDd-UsbLQEL7sZcfryLmMK1WH8xbCbEQaAF9lpLx7qdtpxOBnYUIu5gGi-QY3BcH0M8n5zHFNQbCwU_LULUrXPDGpuZA9db4UHzUcaw6OMg6lfKVt1ng7LbgcFk6YxTd_t7cHuMO97MpyOY9bFkJO9T3MS_A1fwXG1dgI9KPhsqZFGlnDSN_F2QddpmsQI-dYHroG6AJvxFCqWhnnuXS6Erirp1z8aXyh0E0lnkmHaZFeqglx-Xp8DwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3QXDSMthlDE2zKBDr1OEb3lSr5s6XNI2iCHdXv2Lqxu19Q_q1zZOLTOpz2En6AS9zAYTpJKd7MsOWjDv6KVHoXD6ekJG9KevBkJEhqogOQYG039oFskmkkM9iQ7E77QAzdWqYgubNhNce3VzL4yhyqHWwEgzVXsZcU6q4R4G74Nb-n4Cqpq2AfK3MraXPGIaGOTOeS4wUBlqlA0ZpAj8fc5l8zIeR0MSzsBmxmaWqmI5UT0c2S78BLfp35V9EzdTPPifJ6Ye-Su-ndZUIdh1O1O2i0MRTcPtAgnYMaLw1KqgvIVCk6pAfh8aLf79kJj3ba0NcrnR-46Q7pnLZX_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4HyyG3mghZSaFcp7GeRB_4Dum4_Jir2AXdbChNnOiujTMmabl5jUOJacmAicUch2-nej-hxqXuficrqiTfcNdsKTj7-K3AaA6Azhf6siXfuVY9Z7Prhi2AwOUgRsWjCombRaBj9Z1cP_pFdP9a2jsDb9Xx2VkKaBEgt3mrchVY2lwRwHZT6_Kkhue4LCe8wS8AJQsM7yyCBIy_COEychUKIxmYehu-87GwAZQuelvoOeUO2KJGKQm43_lQrtVTo_4EtrpQGbjIBM6MdRJPpWvb-PFJpTL-wXzM4mF4-qU-dPCRhtw_shtHnD1dw12Kud5YFS4cRd0rmap6-LS0Gsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn-AThZy_ITnM7ywhTQ06AXefEu2BYKM5-_Ixs-3FlECkxkCZOp9MHnv6MUHqrDfcJ9q7msv3eP5ueFeyoxSS307H-lxucjr2ZAt0WfqPQAG8bLRf5bfmDZU2j1aIemCvX7w2Uc8y0cVyhJDIEzElK_CK1LX66FNK_Su5iMjUpuGkpZze7IKA5Ks1i8Bit8-zIUPFnweQkd5WB1qgtsGisR9ku1bzc0nDAdXt20M3jh1n6DXbA4gpkmjpZmO4tdU3a0gtBA0cdsKoe9HA4Ud7v9RZKNy47jjDI1HFdyVLVE10q1i2FxPmaLRlo8Wfsdmi9Ezkcc6NM_jSBEPBwXSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=FWvQPRbaGrRwrlH5hy2vPMtC0dOA0i4QB0gIcnDQjNXDISspbnJYGEnZ-TSo32kvvPNQkvhu7VKlUz0q-L2Z3vWRDb5GzgqDRy7_hVoVthR3AGaUuFVYRizPtUKNUCZvXfRzcqUB6QiyLWSs0itw7UwZ_GpUjaG_VMaSYUU6_u9t3W4qrOxWnxQl7ANNfarEgaqWlSsX5az9__wKjNHdGHSYfVmTurEOKWrmjXNeWM2u7KKhFAXy8bczG1KWq7X9Pw5_XklVBIiynyhUg-jFK6D2gN7p87j3Zt6ppgcIQju99eWwvJwYH7SR_-SxPsOCxp4v8o64S-89wJ5AOMvC14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=FWvQPRbaGrRwrlH5hy2vPMtC0dOA0i4QB0gIcnDQjNXDISspbnJYGEnZ-TSo32kvvPNQkvhu7VKlUz0q-L2Z3vWRDb5GzgqDRy7_hVoVthR3AGaUuFVYRizPtUKNUCZvXfRzcqUB6QiyLWSs0itw7UwZ_GpUjaG_VMaSYUU6_u9t3W4qrOxWnxQl7ANNfarEgaqWlSsX5az9__wKjNHdGHSYfVmTurEOKWrmjXNeWM2u7KKhFAXy8bczG1KWq7X9Pw5_XklVBIiynyhUg-jFK6D2gN7p87j3Zt6ppgcIQju99eWwvJwYH7SR_-SxPsOCxp4v8o64S-89wJ5AOMvC14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWqIaJoibJZpydx-wY4dnG6DOxJDY3Kh8OTsCgDodyPFDmIK4Fmz_ipcrWnAper9HXd_3taphRIGO922E35odezWxAZcfELV8VXL1pHkvGQD7q4Jw2G_OWYxtEyb2nPRcGqfgixr-i4HsTcEHEybWgCzhR4NJsB4QS9_GxfDSLPs0qdsVGhIjAWnaumZBce_iw_SaRBnhgKCijXMoElm1QtiE5btg3tU7n6KRfdh1-cjjqa-1ruIzDBk_Ko3kwD_sS4gweX1nlkW6QyogZgliA0uY19uQDqZk2Y6B8Cb8sU2I9cIY1JXKnX2KSyTl3OeUaUQrTfpXuu_jaISh48tuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVNmRPlt_bPTFQT8D5uurEueZs--AILFuA5qA3p3aSC-9FoMFvn5oWYWvX5wLlZ3oF6fRN9dOUlnHjsHwZvcoRK_xau8QS4JTTSvZ4wcVTcEib0MN5GajQopmcFKBbOzEfKWmYP0GHNhRiiVSuvbelWouqgd0VGuHZwnQt1Ojbj3AoiYjTv1-ad11gQGr6Bms1SkZ8If_dE9U5n6vdB4aI7GhsEKamNF15h4l75NEVfrP_FyptenKYZyT5WDtkfHg1JrkdmKG946lM6eRlCZhglyWty171HP-34t8qXpp1GXKE7xPKTsL1-qb89_kQhuOYeUEOFbK6qvfp01sz-RDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=DdjEM1MNbsu_i0jgQ8f-9MYnQcB9DqM-b8QSH0E2Rlf0qah4uylPh3HEP2DqNoUBfDbx2oTf9foRxV39O077kMAlBv8V4UkEKsJKeyvgcfrI_NmbxjQxduIJ6idl9Dj1obS4-PL7T9uzJcDYvjZJ1cj7NxTqDuR2YG9dZfnlO8fowVpHJYLDxNR6uR7phaO0-PJwnjyiOs7npCJzG6OqXLpx6gPOTgE-AaNZDAlSzVXxLMyeK5HTbcOwoAHkiYxYDVWic2D_LESFNMiKbI_H_bZyXcGbN4Yzgrf_ahnotOuKFYvkgf1Ukw8LJChyQOA-epKDp3CdDuObyWo_ir0r5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=DdjEM1MNbsu_i0jgQ8f-9MYnQcB9DqM-b8QSH0E2Rlf0qah4uylPh3HEP2DqNoUBfDbx2oTf9foRxV39O077kMAlBv8V4UkEKsJKeyvgcfrI_NmbxjQxduIJ6idl9Dj1obS4-PL7T9uzJcDYvjZJ1cj7NxTqDuR2YG9dZfnlO8fowVpHJYLDxNR6uR7phaO0-PJwnjyiOs7npCJzG6OqXLpx6gPOTgE-AaNZDAlSzVXxLMyeK5HTbcOwoAHkiYxYDVWic2D_LESFNMiKbI_H_bZyXcGbN4Yzgrf_ahnotOuKFYvkgf1Ukw8LJChyQOA-epKDp3CdDuObyWo_ir0r5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwY37agm-nxNNHque8yc5Gs4MEQC68Ozo7dQLa1pZZqErHc70iwFQ7FuhffCtavCoeXxUItsGPHOQ7LJnR8pyQ-ozSQUW_z7JsPR_tGlD_OLUTU0cP70KAQuX3L0Zl75dwhiBL1LUfkbdKkDOHkdVYoKZf8s8vQW9A_mIGOAGP1vKn9KB7zlJHzZ68GSc2hxn8l-I_Wwqr9yx7bkZjtBV6kgO0-Q4E3gW9_7rZblO02NyjoYzRzBpeOv8h4QoLSmw74sCfCU0A0U7ToEm77TuvbC7KjpABsGUUM04svlmp2FRV7QRsYv9VTXwq5zCgbkcTrSFeLpv7W1esGEUCjBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMgoqCFQmv_z1wKMw2NLYNHiNEgg-xRQVVKP6gB3vv_qmiiLwg25PgX9JT4lEE--dqLToDtk1Q_cDtownqvIUmUWpr5gxDMahwET3VtRN4bC7yXvgJCHcI7lYvQxpy6rEqWZcVE6aT17c0ooaKYRWRytsya9RXhLirz-hL3QCYG5HfWYtvc5VtWjE5-SSv9WsaIztfEPtQsOcK8lQDkiVO2AAeZVk_FGaWvG2vC8Y_hgvOsj5RW3TckU7WEJEcizdX7LBW4ov0ynRBa82Aeo9-hLesGxgJcjwV991kfpVxxiLxZcGpBgRHP45vYaRkX-LamAFSzMIWKN2l36F3vFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23108" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuFUJZXqyes2hn_XQbatDwqpfFGI3w4b4yWR0DB_gs3KbAnRSFymmUOH4wpzRtTNf6qLG_W6l71f8sl1TlzMgOJPlgFx6RReEKZDMp10o6kZAaM9EYGuCy5TsgQVAW8M0tfkONVRScuSdkzhUPpd0Xe2NRzVOi9JIx7b07fSzion_ohsEFzXO4VOWvwuMF4DvXLsdfwkNvgrkGG-LtiFDTHjUE7YE1zH2lCcNIzgh4SGat33Ow_-q1cL0mD228mnotLG3GYnLy9eDZbRY8lIGDaQiOImNpPaWvXcq_dvpWMAXEp6-jdWruPWwtth_S-b21G1GDhqPkPpcOjnK39Fog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1m7Su288cjAzILDNHR-W_3GfGdkx20aRBWCvdcnN7agFUcl7e4PQ6ZF7GlPJZgXRHTMF0dmPyE6HUjjbHW4T6kk_eIy2YzgJP6gXaGNSlt3yGPL8P0tWtGu4rT-6M7JU1YN3e7BxFOyIVatiTXYTqQZDx8ZsP8nQV3-iiOv_foXQa6R4uOWybAk9yPLY_7yoM6AbyHe8J9NJ7xdgHHuqacLpKaXJl3t2PDFK_zJxZwQOT1qNOAQIn4rDW0YIprPXsjiDbQ7kliSXL-Hzn_DwvEvzc1p7ippkgq6Them866gojAkR-4hYohJwtytzYukWlgFgUeoJ4rutiXUGVxHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gi0swB3TUr3riUyQjNNisMUTnHMC-58DZ65_C31RXAQhu81yyYuP7BUzgP_OwFoEKUXaji-tgyK8SaNtbE6lB6qzCwGt-kS3G7UXLnhcipToh87AL1VShu5wD280iHkILHYYXgMYZ-N2S9VCDnPcEJuNaoBMW_cGpavJ_RUocyobpzdcJIPw04f4iaUbfnM20hGiwOqr8sT1xdfLTZG5okQ2aK-m8iyT-2jIP9B6FxsNad4fzFoaYcMLQtzVE-sE61xg9GsFonWUpPAXVX4Hj0NtzRgkhdYdA8msKbh0ebX-l4DeULoPbP5iAWwUEYtfYJSrTsWbQRo96JbvWp3Wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RB3G3JlJRYOQk0GzGY_F4Xj407jbXkDZ0Ki1OpkqjvEbtkl0irvl07-aIc5osakDJGG0_yCu65Voa3qByt8ks3qmyc19cfAuR1yhxyeQcgxDeD6IxFpclP-6cG8eMAvX7OtzzBzstXG6yK8l6lfKFQpJZBt1J4XDLLjl1MZoT7p8b2kF2Z4P3OK53sSADuMTeTxCs-ON13LbhfofiwBb42k6DpNDfagG_Ff6iJnJicPVgmsAn5Hfy8jJC3RANFot3Ztpl2DNzB8Ev_AxKQbx1Z8rHhQKNLKDFE_AxV0BYfpoUTHaIBlQ8JFnRo7L01I0SdFWDQgyyp-XJ8Z48XI9rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgm6S3dwVrxq0Iv_gJmV-6bpUMoD37ee8S_bLcf6Pr66GxK6Xe4sam-LuKr5nEjaq2Wbz0q1LQnwHNJ2JbCgP0ZQll7Ouoqle9mvouJcJ1K89XEuAUuYwIwqSqWxudLe1SY3nS8A0K8Y1kL9nvSuQwJIKJtAYyVfidmW5jr4xz-yh_dFTRWZnPB_mQDvNQdaCOzInwUsP5f8jbQrSgWtPvA-Qwdb7I1GvsIx4Z24wRPzwZ1FrN3zdlA9CTYY0NhPhsWQYUZ4ZAHZfhpQeGGu_B7AW6Plb_B2s2j2ph6wNX8-Gt2CQg1sMOVMmaHgPH9wCLgI9O1qXMaFQ5hsj62ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHrqAePgVYUIwz4sN0O6r908xzPNpcRGE4mNUcfNqO97WuNKPY1kRINNJuja8K8moyWVLaOTCxtD_ABTMehnG05SARHNF7lLRBLK8cRk1khskTzUFpvXtUPTGscpCf8o8byjPPpS_t-QMnaVqV6mEZmhH3uloPZoC19ZfqQurgeasLmQUCarDnAwQeHkTP4-xQwZ7hmtt8y0seIOt8RSXuN33vvK14CMHbB5hW49xyyVUz6IM-1Kx4KXU4KTcbKIRPFer0N4qWBbKBVN8tG8W8Vo2de8GEWYns_DylxkUZSrWvEdEpmhyRS5naPDhR7Wha2oVDns9rPDZSI-IqWJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=bYRaBCr6-i7PoEepHAp95bdi_-rWC4xe6gBobb65RJhrjHW1v_cz_P_uxNa4SQOnfbHI8KFA1HXmW01XZauBaCSEDsvpdfiVTYtRaKWeCjHzcCv26C8kl_wAnLsIvT3w2pvCcSgV--M2B4nzfORpuUxO4kv7pWe9oNsQG2c0cXpdUGBFaAborq_JrrAgDH5lW0Ego20XK7Luh6GK0Cc3rC31-A70rW8QRMm2ACU8YiKdeb8odTszOsECh58s5fkJL8aV_YoQQWH59QfuXG3feEqGstLO3dwu_A8Dwu2zWOVHT544_aMwsu1yXqpM5sBjyhCAHbMgawidJywLyy_JSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=bYRaBCr6-i7PoEepHAp95bdi_-rWC4xe6gBobb65RJhrjHW1v_cz_P_uxNa4SQOnfbHI8KFA1HXmW01XZauBaCSEDsvpdfiVTYtRaKWeCjHzcCv26C8kl_wAnLsIvT3w2pvCcSgV--M2B4nzfORpuUxO4kv7pWe9oNsQG2c0cXpdUGBFaAborq_JrrAgDH5lW0Ego20XK7Luh6GK0Cc3rC31-A70rW8QRMm2ACU8YiKdeb8odTszOsECh58s5fkJL8aV_YoQQWH59QfuXG3feEqGstLO3dwu_A8Dwu2zWOVHT544_aMwsu1yXqpM5sBjyhCAHbMgawidJywLyy_JSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeHZZsyPEmUtUTfFjAoJp5VBeOVbfotiLxbDsCW0OvHPHMBFqISgY1Z_aqmvsYR9Xr8Bveq7GqfwLP-fQJxgY9jdj3E4QM8RpeHpEtFrlJB8QGef4vZUlBhUTZDc-i7M8VVpF1stdCkb0poYoYZAn5v1StIPM-zUjrM_nI0skchJDoP3wBC9p08aBjASGOco8m01CrDwGtaER3irj97pSuEAiWOW4uv_KAcCLHpO6Rt_rKVlVEQ0uGNMnEYIDgI_ObTDPDtHuvRnt6U-5tQ2fNYzvXGQjpc0eoWbGACDp8wxXie4sviYwTF2JaVmDXAUB06vYJXnB49J_kAemntS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kaja2h9isXmDyyu5UtbBbRKXhEJAjCzPUAMDFy6nbAe8Y2rbfIbEwyKxkM9TTLwv9H206MHXkctcaXff325ByE2r6GANLmhynEhSUgxxNY6_zHjV3YMlNEsVQb6ZKVlVfPUSJ9uM4qkHDv2Ml5JE2VaYh3v0oJ4mWBTka3qhcH9RUO6d9Zyr4blriFi-lxHNv8Yg7Y0Dv2UOMguHmbA84ylYCWBcAyN3Gs9aOJO1sWQ3C9azFSitsUu0GsRLPRUPRUA7DOLpcqA-LKHn0W6EaTUkvYIYZfmBZ1oCTb1CDkeHTn9pMNFF8Jlz1NZwQULzG2gTifvGO2HneqAZiEnBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JE7pqzMyZy-6tZZoRCSGi5UMENG_1sePkofZ1Za0GMz0cPvK4mMWcEDOqjYf3jvd27rJJvLQ_COqt6kPjq8kwHzT21gLk4wgFMh73PgKnWVcNIsmj_lfJkMermiOIDGdqKn3BVpCQM_1exYFOWS6fN3gLyxkQ5fN_3uedn-n881ZtngdjqK7Usx-UMplxRjFiHlhILFcE-wr-n5tHcSepK-cJhf3ItDSucOSUzSxVlJovHllg_zNfV-pK_AfbNfDJQlYX0XWW85ahOHDlcUpzh-yR-8JytN384IW6WhdtWbjxoRtaXSNecCnaiulRwBY4uF2cW2kYyFyDmfKL7d2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JE7pqzMyZy-6tZZoRCSGi5UMENG_1sePkofZ1Za0GMz0cPvK4mMWcEDOqjYf3jvd27rJJvLQ_COqt6kPjq8kwHzT21gLk4wgFMh73PgKnWVcNIsmj_lfJkMermiOIDGdqKn3BVpCQM_1exYFOWS6fN3gLyxkQ5fN_3uedn-n881ZtngdjqK7Usx-UMplxRjFiHlhILFcE-wr-n5tHcSepK-cJhf3ItDSucOSUzSxVlJovHllg_zNfV-pK_AfbNfDJQlYX0XWW85ahOHDlcUpzh-yR-8JytN384IW6WhdtWbjxoRtaXSNecCnaiulRwBY4uF2cW2kYyFyDmfKL7d2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANE26Jvjlji47TEnt24oP7NKGc4OJpokUeBujT-_NtmB37TsLA4xki6XNgOB_4FO6PU6C4l3SPbxXlUUdOHUejN_cXN3JEOp9Yc8GQWcm6fw8SgCLhKgrDO-Ey2KkZPbovuWJ6veguacRrvjnCNljSWEsKZ6KP7cEaRAP4BeRJqiw7SEzshcqhXwMUHAV4Y3Y4Q9zxLndxoG4cR8w-W2y2WkABC1RkZqeXCsbmfTonnCMVOTiLYzgNEOtHZtDvvLono2pL0daM-WDNseQuRmirwWX8WJoL-qG2nFt2kUE5mHEZhNzZbmJIAPMygkRqeKSkyeuoKOEjxtQe70teRTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doe6HpzWEAmBSP9CwHU5QfPf6ThasTg597v4qfLe1S6TTzTqtxravLTib2eTO9czTm2Ah1UvFnPOy0mpiK-AUf05suGVrmKgm0DdSLxdcbD08YpFl2I7AxV5PrRShH7IdshaEONBsN2UPhPMr2ipUbP-9FZ62T2STibAwVFLsVf6rEaFRjwwtRYizxzw2gPg29tIu65fwunauEEr-RoaMfTNMLBJc0wDalZmx8fiHoKcct8xitwZsya_BmV5ZJUMmuBu2gDy40-L9jdB_uA9dLBUGbIy76tqVu-C5TCiIN6n2UoZgHeJRkd7fcLUhxHAgCnSYlCu3d2-QLWIkTfKXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcUtERQv1AgZCIzvtSRW2ZINcSj2t_Z_gK9XVuiPf-OvQ_fPehHUcOkAgo0CFTVP-MJt3uymcTJZiZQqf9-x6Ro1hijnvbIfJjRDyqUMD9S4kY9aWbZWxz_yOZaIZWz-XYs22R1Pv6CX_L443FWL84FCGSFXTBAPyX29EaVw4PncBvrzvED7SzIhjnTD5-WdykvYQdV4IW1_cEf2bW-1u4w-SZbtKQfh3VBaKZlsu7Q-Whux8QOeSIMa4OOslJeVu2OmK_ZAD0Qyf4_LydKec_dPenNuin_ZnvI1p6Fh0QRCHStuRIvMKO3arFA9UgaobWOuJ5F9FwwFqjAf2f4tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bz4a1_mlJug_vAXN64iUKagOWQDlox8OgPY37iTjBLGm75T9WWabPC594McxfjtVriZYy0rzLOER8_VAUQeMaGRsLUzSGWt4qASPe1-dggs0cPF_UcGfpp936FVh6jtJP6lbsU1OicTaOQDWrCeItb0s0eVdY5oRQeGG0XW7ygGGYUMZeCO8uK_00l0hXs3kSyltx_OBjgbm2ZDpYc2x7nVVKSOQmc4twtcrN-QMjN4akG6WwTUhOV1FaQ34C5VLHALau4e6WcpcoI0Y4MiByV_NvQd1eBZM7Q8xxAWp08ICett3eHZlY4vilNggMLzG87oeup5NmZQ3_ltm4Vjytw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfeD03qy1tcb-6wbXOcoz_OBjZmtacSKMqVRxY8QDwNIZpNFMpyRAKWWAQQ6eG3khOREu0301xJUSMo00ZVYSd-zAh3l4JDEl8Dbwu6lPsgOeoRLWAGJK61KTbmTVUbUNiT5t3Dh3-kb8iiSidlpQSYhfkVTqZMJSO17Ez8s3xu5PsOH5ZuT-cxHnIPPPqAYkE_oplROqjZd20FGecKFGmtRf8-G6TV_v9p1tkrm7q4-_Pc6hjcldlXEBXVmJDQ7DvsbT7wfUsIQzwbBydy6Nu7_gF9z66W1oPD0ffKteTg5bzF_n9ymcby_YvvP4BzZ0xjoh2mvLxo2e1o4aQacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CmPKkCYd1EIodInutxIk7_QSzFT_GjyZRWFluSl4Bqc_lXaAq8Zk1w-ENeYirS8g8piNQ5pktsLqmIKUcF510RzwY0pN7GtntIonCagxAeO09G3wHbT2xMNQ2iTpQyVVljuRFuqb_IsMvd3GHCF2G6pm2kxNdZdNGwQFTF_YzBSVanB78C6Zew1fWQV14w0JWBi8GEJxVx-YeOHGLJmMNUqSoZdXNuRGn3bwWtP-ykjsz1zLJDNKfcrspNTwT_2aCf_FLydFvmeQVjcztEyAhaWrFao1Ta7cgj0_KPXC93TO1uu0Yx0djSz_Y8-S9GEt5RUTTMkeM5NwGQ5xpLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m84KOmFAZll9W9oPfFSok7x24ob16TLN10dakY8CyH2KQKKQPVt4nf1RTa1TBLd2uJjeRbbS0z9gZbfEHOJ_7KIiJAAY_c3er1qmt5DrZD__2M8XF0jNC7fnd8M0lNh7Z3-2oQA9Sxf08krPiIMUUG4y2xo12oDWxv4bHw1OBtRqN8jp9kN6KlrOpeGWns4o6lswjH32MiXfCUwQGwE24OJSUJlOMinnWz17x5VKZ_835VhLP4F-kqPtJ_vebZEzfbnW_tXsIxsL6HtzADy0_iEI2JS9AJfnY5dvRd_s9tBt8FgChQYkWKkpXMARhaNjaEPWrQFrucAsa5ZxNzvUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NnlobTVtP38jBfCiSwojBEw-tg1KADprRcAnZB_MpR7uReafHbHjOU4-c_-kICrGdsaX9BxjbBeigLPvwXFAcQe4W9POOMjiqfz9jca7tIPsxNEARntfmzmrcnvA-RT4qAkxVSpd_xauUmGHZY1ykUWFnT1g-ZQ7JFiENr39LAXY6QSMfA7mhi46uzM5FxowoQ_stF_gvHUm4qWd6bjfxl8ulbSAmZIv1NX5D5Pwt37xqlFnzaCe6qZCxAcUB-ZVADx_9hTDddtrP1cHek7tOPatS4_2Mm1MSP0buo-T3m62MQln76exJPZRD8IYuKD7Wih5zFMRl2RNx1JsoDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAh6RKnCrrvLOXBQtQCnK3XQGOUrrUB-J87LqMU5nFW75xi01zPojgY2bIp1I0h2aoVwRcLiGtbxq7z22Jj3CRvN94jJGudylfwAY2fx0GSHFddiLSBMskCM26RBp6hCTn1yNnZE_nbEn9kBeYstZuI89VjZG42sX8uFmfEYM10EmG5PZluaKXY6CnF2aWOvFRMz0zZjdmo-uHuqS-0M4eo8RDvROq8Amr-8Lf-_kMbNn9LF-HS7Hn0TWW8e1Rwh71H2eB5QdTEa7syRi5DO_MZNQf4Mg356d2JpPoUlGXNaM2eOPODDD-pZityUhRl8j06BQ0ylBAP2vJGAKeEjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye3atitMNV0WY-XZq5shaSOjS8QA5HoLqWlKs7gOOI91xY-ULMo-Wuiydu0v_3oasepdc-vm1o1Ttj-Gprw9MtfpRFzYlWEmrjh3OfAVL1KR0CeqCwGRyQIrcCeA-XJ8IYD7gVn9GWqeRKd8OVaVJIYCuSIHezrO2yDS3ThGO_vXg7ZFVKOF6auuz-YLK8eRvcYqi4qkjsm9VmXBV-8V6sagoim3JFmI5BxCMmAWwccJYMM7zzIumi27o2L4nkxZH0PNbw2iiLxtLAL7SWNq-7NoWOdqmZvkn2Rqv5whDHPbfUedNN4n0kbeFG9C8u3G6g2xeR3rThFnbI8iow0o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plqo5dYzzZn7C0XERP1tJjpRAE7fNuxvzIrzLkeqba4ol3peoN5tshFzSu65oL_qATS6q0ki2Ftjp727Geelz7XaqpIsGk6ML4K-Ux4mmikM-gI4T9eZkpUPiY8ebcumEJKTwraT5wP1kh9Tb5qRYjUp1cYYTWYx1AMIR4qxI3y-F8EMcDQBQQ23oImcDsIEF0TDFZttlcHcssZ-1R5SlU4rL7ZnN5oRwvY-NSXKaNgSYJ_oXnKLzr_MnQo-y7oeZhH-wd0VrmGOl-O3ZJf9hQJXAPrIecKJn66s18YlywcyddLFwBgdOPg5QoPse2gYjkpzii1REqGnqvC2_dtMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLjS6iW5XOmFxeKOiR4Qr_MJ3N7LeMaeOwzTDWBhIcJ2SaEgPEWCFDvKgjJ2g2nu2sVnhMTEk3UGFDHlc-9no-y2zfAV9SfIkJXNCl8B57GIO8kT-jkXHNm-tWjcq0Yw0zSDTIlSV_ZOlf0giTgtKSW6IXmPCJOo9TP2rX_H3dUOzlFA7aGW8R0kLIjwupvDZJ7Hibaaz-nFqrruIFUvHeBdBA8PVf-9deBdkb2KejT_iAseyo0kV8CyAAZnazpOxYin8FSWRTSXCQcLVDIE8l3VqfgErbKmZxiJ-7e_IkaBSXkY9OjjTOLcLEtoM135itOWypxSGO-CN3sUl6eF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUXHXJennlwGp3PUUgx0uPtspOTR0zFxEoAoO1SyzDGDjS-7so32S50sYr_gr_Ct3wtIbEG5_1fHtrjYqn6qefPn9aQnxzasVsqGHqiw9ym2hyPAycB8ur25QfY9IaQgIJtFIGpe6R-t2NFr-gvkRvl6w_ZH4oHYEKuijfvgjl0r6XuMQdNlGZJ007XAbASiHr2EzF07x1AslMoT00UeFRLiBnKoWU_wRcHHCSRcephSHAH10rFrQgYb1nTsXijJO-8BedlqLLoAMI0a5rYjGjRZzavUfJbzeiS0ZW6qMYIp-q_JQwZ_B9t1J7Wbt0zKFJRTof5LMffTGfXdFrkuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbtQpMFb69pQY29TrKXa38ea68p0KD_Aq0eKWTwUetTrvZOIsyLYcvNVHOV_hPUqQiVnIt_CsG2qYZC9AntLbg6I7QI1qKjU-amS7jO9olLmhUwLQvQMqGgOqoU3wMGJIheqw6BQToMO10l4CzszTxnDuNTWlgK3Zl5oXZ946WWqNDiLyjad77-EX6rTyCrJRyEQRUPBqS2ycbYHZPJDBmeO37oaxF8krvnc8jeEMaXzcO4IuElJscABbFj0lOLiA4xLGmsKA9-02cZO3wemZS5i5f6HXSDjOo7kNR7x5TxqDHuhFQyWqT4DUqu9z-qo5XxY9POsldj3XuBsRaLpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZejtzpaI82aaI1L3M4xYLVuLelSrmSjbIFqzyo7kmr5SMXITBCuamZccrapxWXeAxVjB1HtMgkbjm0K83xHaenG8jaDRZsOc-WHd-NA_8ITGUrJtx4yIuOUq_DmvoFj1fgl3Zxvtm9iAkgVg8STLvERcqY2wAbgXwJOax1EVdhROOlwkOHZMVinLdD8BfL-7HxShlxZkxsrLJRA2FWT2QiolbcFg7NHy5VEVPu02gHIwSiV9KYymPsejDrhqiGUjPvFWY8IVeBfg3uFF4q6RfOzK4HjdQqaP25I26QhNQu9_pBBiHfGnwFmRa7xJ_EWIPifnrpB-I1hgQFAwDZUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyF-7Z2LvhwUKK-Nny-1LCkegydzNKrJDJcUjpclvw4FTdsm94KkIyiizIrN-L462RBPeScC-pOmk2eQS3_gMsaZe15Xw_Foi8NVrUyi5xsa_Qj4PRLqmNKi-qkIng8icRbuQDqEtRo6kQCoctPzfG_4h8O0khe1pfxQN55mXxRtszOP_b-e86naHZsSafGBz4KyF3yGjOoZ9RZjukVvO40sbGg25BYbpTJMwIX7jaZMvij-1VTxCzz_dYmOrnLElhrKlFVymSYS4xv4lH7Yxis9wqGk_9X8w3b2dAB7LmrXXyDESnGFhnDZ_M9HODRzUgtCsPisD7m94_DDFGzTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp74hPxsVbXsmDwIUx9pm7UbUrNYaROSdmDMIHFFqqL3jREpwkoVF5mfi61Mh9GKR_uMiLsK7-Jww4lWToJBDdtCzsfAajt1d6VtMdj9HAXZMSi_rOvvBIaic3H7AOAkVgiDHuFcwiH9BR18LiDjDdTqhjupVLRNRciavus97q35CQ0Vyu2q54uJFIbXa3pgEFRWz_BmT5ms_7DoHBDkgpDvyaB8p-uwa5evW9KN8XvnQVqdBEUQrY8PKYomv0JhuJDI2C34iTjqKww8sSYsYluepBpkD8WxclWsI0nVhNu_LOjhGPTK3KxDm_8H3CCS-0MbPsLqluO_JUqAkA8BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTWHWs0hptYdxNwH2yF3Sgn_PdYQObFWrw4Km_815OnKCUMOWqyPbBG3OsGb8Clx69_SK_D2cGjYQonKW46BExemizFDwj732piKn8a_p-KNQPH94V1TDIaN8V-0hBiLrKHgauRMJyLZn9z85bD3oYSx6rnJL18aQq1loE9XOhE6nnBx86AUmSk_dz3LVQz9Qvt9L6MSSzWkm5UXGAFO8uWGNrVlAGi5RJskndudBW_wXVeZCe3OpP0_KFD-Sv8x8ZuyjpfgImndsFgT27j0HuZqlhmOa7xPVwriDFOVg5RZUX5IkMNzifnoyORCuX1IKr0NzFXs2UEuRd0ma5SYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_I2VuhL83ZJB5LciwOxv6VmMyto7F1p7Wln8dZX0b1o8hnwYW50ZVOe5vxOtfacUKO2UodwlWobPOkntdfgNlG9P5HB2dIJEG0j3RXFw4fPygVwKGoV16NSApiAkKO2YLGD7saHic_2bYOo8zMoQbUAf8_u3SjD1j_UMpHBJe-lIZ5O6DmiRwp5lk9OqG7F9tw8sJ9Z2XhlT9BW7znfhalcRcjysMKOBTyK4NWP7cDzRrfyeym-U4Wm73W23hgn0b7OT9WfLlB-85k6tSNjPigXBsSxOV9MXLHFnZgwCWlBWJ_Mv9snXMciHYZEOVgJvRcVLJnNlv9_isDmSK_WLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-rCjhbE14Wf-3MftN0inCCbV8JdsfMnx0RlUjwOnY0yBdlIUcJoc77besrwEqQzmaBoqk0Z51UJ5gLZsYpvTQSmKLZzsDB4tHJDnx5P7ZcZRNKb6Eu2BPGpUz3e223PY1YP1lSoX-dLy_dd7XROEJ7UdLH02ysDAqAL6YnfsQn-steD3Rkq-GrJPTeO6OF1drX_tzLSbRxxFJuB2oD7XXtF7lDmkhPsfldBZAMmQ3syEEYDaSo10a6bWHc2j4kagtOyldpXT3-2wjN0GMwDAZadp3X_ETeuT3zUQJo7MIPg1BgNw7qISQBNA_lebBbMv_jKmCHzxB2Yhy674bSt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYuriZaOrGO81Us0O3t3A3L8-wAr3V0MNhZ4VFh7kp5UP4KmkoaSpzDkE5fpelga41IiN7ZmoKIZYDaQYaBJCDpenOIZyY4RGTBT3y8ZWefQ1D3KNHwf2pl9CWs0MyQvVHL-b7qwp144xweLuhDSPRsjBqQ_Oprr7a9mYbrTllI7-AK8MIRqRdfbDzXQCdnheKP7W9MhuAwiWi9dG8NodR1nZNFoubU3UJ84n-FjfEO9HlHwJqbhsg7WZqyi2G50y8Ce5PiEhar0K-glNFRuwsttmuoNb43FQn7olxtFwprV14cbTobAH5eUTwlkWIztoey_YA7aYh3Z1D9OLPPDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYrajnCPnIm4W9BaYf_j75yD1Y7x7uVfljqWS80B9xKi1XTmebUPRQgxGK8q2xSB5fhc5HcgK3bL6VbxZE9F06eya0oEWQRj56WkEhuZALsA2NptWj0oZYJBUTTHsFnc0a_clMincfe_i4cl9pOgeDi4IxRMnMPLsKnOfZsIBA5TybDwOlv_upqs_YXBl5Zoeis2jOlgUfAVJ3TZucGQ5KMr6DxdOrltg7fRx1csoPucqCif32ALLlPR2Qvpa35Q16rNqgl3vcJNmNZLt4GkLDmvO4C0vfYw3YVrdVNS1aew7G9qaXJk_I4tLUlQWSqy_DF8Scv05YFGINMXRvkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfX5k7Tsp4xBZIz2INsLx29y4hXhMn3_lf9KWOvdP7zJrZt7W214odARW1yyq5AviRH7FZIXRdptgF0H8pCpZUPG6BijxBGpmpbxthT1kmhDZywnFa4vQnG9jYZ4CzJZNwx1yuhpzONQzrBQW9b4j2YjpnduX0lfWeEkDeqeXDIDICN7VjdV_G8ZSSm1s7IEHuSBkGeRrwNZFKNOFpToV3eSN-Xmc7-E4PpZOMrNRMp4YIr17Z48bg9_3LU2LoZUJjojL8rlYosbkwg4SVxka6S1yeNKz7SOi3z9fC37ArguPQJ0DtdK3YOzoiMVsPpJuLdw9zIG2_bvBDnRWk67Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsLIXqWHsDjJbUd3SEwbacf2EPCkn8kaIDtEAmcZzmLIfMZ1chuxkZgzseAAa-qktGaVCuHONZHHwkRf71E6jOLYqRDcEwq6dqt3Q4OYoVeU4D4XCOQ5LcRaeRGVSrk5HJFHs3VJD6jPXBregDD0W9mWYGjD_caLaXQmwOkDv3iID3n80WPIhf1Zch8QtgL4q4RUeCoKDakayfubO4zrVCmhEEuUSJkf8RLYrFVgjyAui9yYWV2Z7zK1vqO-c881_qqHvbaLLVoGs6KjyosDbr_ZrIs4qQFouYW57OqQUEIittKxoLPL__pG5zuYXhnCDRlm_DHlQE4kHr-_qPixmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7CJeeHc0lEVMvr-WPco-O1Ex0_BHO7EmFRwOcFybaQHiwHY00u9nslDH41dI8t3oeiTUcEcdbAokNsPk8OlAmf_c914dtxKD_D_AQ3Y8lvkmQZnTCG8XxlbiThRMRE7vYvDZ7xlIyk2jN-rVsGQ0HgJYmryAYMTamiy-ddLtTpsUrfIHWmkX-Thr8Wwj3l6TX1_ERS5NZwoSDwwvwQussm42LhEbUj9SKDD-Tk3Xsu0AB41YIqnNhH_gmKHrI7EQaSTK0m2kcxFZ_XS8X8Pa2CBK0m6ShTAPeqGbzaPeI6u3nKC_dNMW7sf2JHQKghZ1lK3K6nEhbHPTwf7dPGQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=cn715yZh1XUiifYr-7pSHEpN264dI2TuHJcCG1n3Ujx4o4dIS9RWgnAgIJ8dm3yKE5ILyU2d3EnLQcglJzXNKB-VvaOqe07GYuz4t_WyDiuougwCbnQjZjqizQysiQpxLSAzJKXskiK_AbDlEtDSObXi8jt_Oi7w6ugLHILdNneW3LtRMAYHXkIENX_4gi_iTxiehDbOvCy6btRqu2mIQYBwTgFMjEy5FEyH9KuMiqxWKMfk5oFcg5pgjH3AaSG-Kv6fr_YF--QIN3R7ozg7jlJeDBB4jRomp1ftcmyCDjEnduKnfs9qSbKjYM_fKrL5EKFloWmaTbd_CtBfEyEoCL48QY1xfrVGrMCrH46Vmx9889a6yrO7ST4Ra4FwsoIDh1GBseTNdAWI-2B9odIyD47kMLCFwe71mgHsy_DeOay5JvETnS9-PlBfEWsoq3zdFofKvjVv1rbM14DKHUH4-bJYhM8fFtTUhfcPOki_Rs86tEJXHMVmb_tVP61gXf9feTT4atQrMu4HGMvy-z0fNeKh35QgvsxokNbr6yTbNs1UlQ_6e7Z62p9dQ-JXIAr_EcA1EEYbM03AQtebb6E8wSqypZP7VjQqMtgoeXO1oC71fprml-TV_Jy6TDuWBzyWbaSFMbh158Gk5DXL8jRlgP76mBrzWOWcJIO4TfgbPVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=cn715yZh1XUiifYr-7pSHEpN264dI2TuHJcCG1n3Ujx4o4dIS9RWgnAgIJ8dm3yKE5ILyU2d3EnLQcglJzXNKB-VvaOqe07GYuz4t_WyDiuougwCbnQjZjqizQysiQpxLSAzJKXskiK_AbDlEtDSObXi8jt_Oi7w6ugLHILdNneW3LtRMAYHXkIENX_4gi_iTxiehDbOvCy6btRqu2mIQYBwTgFMjEy5FEyH9KuMiqxWKMfk5oFcg5pgjH3AaSG-Kv6fr_YF--QIN3R7ozg7jlJeDBB4jRomp1ftcmyCDjEnduKnfs9qSbKjYM_fKrL5EKFloWmaTbd_CtBfEyEoCL48QY1xfrVGrMCrH46Vmx9889a6yrO7ST4Ra4FwsoIDh1GBseTNdAWI-2B9odIyD47kMLCFwe71mgHsy_DeOay5JvETnS9-PlBfEWsoq3zdFofKvjVv1rbM14DKHUH4-bJYhM8fFtTUhfcPOki_Rs86tEJXHMVmb_tVP61gXf9feTT4atQrMu4HGMvy-z0fNeKh35QgvsxokNbr6yTbNs1UlQ_6e7Z62p9dQ-JXIAr_EcA1EEYbM03AQtebb6E8wSqypZP7VjQqMtgoeXO1oC71fprml-TV_Jy6TDuWBzyWbaSFMbh158Gk5DXL8jRlgP76mBrzWOWcJIO4TfgbPVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGp8nDRS_s5VcyTnnauI1Ww5jEtW6gcwTB4neLqgndMR-rIXS52yeEdTKWbAX-ruqB_hZPWqiYsWdJxSsbnBMuXvvS5rj2JG0jZrbVfBdeo44RTxH0KtcqSslcG0XNm9b72awpoJ2CJNZtaNDshpYWrUyaxBcr3v9MDuKfbbcAOcxmPMa2D1skxOVBHglh9O9c70ChSUvoVlSLpYZd0a35h8uO1-BSMGK-VWMhV0Xx-fgCEBpOIuEiyp81kZuth74P6oZ_znZu8SNvSzICAnpV1dhvlFysDOFwNql6eRk7_-Sqa7-QwA5GK5bGimhoHyIpyqq0fkCk1tqt7EQ2s7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=mUR08S7zEOvlpG50Xh014g9aSi0HNRo18mJotlYtrUAJ1qgOeOmlObKbUQkjUX6nkN8vblU9brMvrx91fayp2UsYJgFngzPVKAklBxaI7SYi3SV8UmvuILNXhx2oukK4JC2d-3NrROVJmILNRpe-Pf4TtBUvjVQEiITgR2qUhSTMHrKHx_-462OsCBYu2QwZfgzT4uxCjlprM0lurTKyqpvQpXG9EtbNxf_Vvi9ryNC3NQaIZUmGtmwU-e6FX8FZwD5dQDbK8eDiVf7JGbJ41qFiz3oby-R78J7Dr-dDVMfgKetW47dxLtN27BoX0qDu02xOZnxtNUE0jYRy6WiZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=mUR08S7zEOvlpG50Xh014g9aSi0HNRo18mJotlYtrUAJ1qgOeOmlObKbUQkjUX6nkN8vblU9brMvrx91fayp2UsYJgFngzPVKAklBxaI7SYi3SV8UmvuILNXhx2oukK4JC2d-3NrROVJmILNRpe-Pf4TtBUvjVQEiITgR2qUhSTMHrKHx_-462OsCBYu2QwZfgzT4uxCjlprM0lurTKyqpvQpXG9EtbNxf_Vvi9ryNC3NQaIZUmGtmwU-e6FX8FZwD5dQDbK8eDiVf7JGbJ41qFiz3oby-R78J7Dr-dDVMfgKetW47dxLtN27BoX0qDu02xOZnxtNUE0jYRy6WiZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF_VqJ-fm0DZpR5CBN1erBMWBrCfRF0hbNuNZ52-cG79z_lU2w67uUWaeJLC3MtpvtzbFnAv9rOEyceId9fPOMhmbgEiB_8I8QiQe-WOoh9YvQSsea-g-4Eic9jLc4JYkZLbAYWwt4aIRCJO_IFspS1FJDgZ7_hYVH0N6sAMNhhUJnQMpNj4zur2xTIes-jynRgVpFetTgjfhwa0vfuoGe4Z73GLaOW0j5L6BgfJrH5DWDIGQ0n8zIAUxt5nDGkR8PbRXEZnAS3U1-C2W2lzW3fFvlBHGsbWwvqnHZZ9fobgiAWNttOpa-TT-zFWfn56fjFKCca5fuh73Q_h81mx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHKJUng447O9iDnjhCghIowTpIYK5-aScXEEBqBgSwrTEk7Y3Jk6gSATE1B6yoK7QlXa1AtiyRAqy578AFNt3jAjH-Um926jFsEpaoC2ozC-HR-qwB1WqEe1CIah_XnKtCDeYa7l854fDfPMYi0xW9XZMPfixzjCD01d8IwMCnE7U_dIRIAZnadRVUnGy-8gXs6hYOz8WL44jmjBLlCLv63D0xqi7y8jcqewAUMlEMfPbJo_lwKocVCBlUeyoASNArJ7wymyYaZFtSorvjz5x0sJWwqe-qAeoloUioaAR8tG6Hjj6XToDgCJz_88URcAKxxN6sViVE5e5aDtquj0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEbA_jXnDbM0q-2V78TnQB8SZffl2llb0pAh7uqh1DQRgmnxkRqApNaQoWlwKO7Letqn-hykFR7FaMKS5-wb6ZQa7K21rowoM3cXYGI8JEkGnsOIkhXEPjbSiEs8OAx1L-G8TEA1S4wra-GUYeXdnR8dYBMkYJ90xd8-pgS4vBs-6v0r-80tMJKUC-4RHbqwqTghfhZXQY8kOGylnde6TErmtod3-OWoP3gnnGNNmbuANWPKr-v_YA7XlDnOQNyKVkwdVBQ3cWy2b6RcIX7fDK4gKPy5_LZIOxh9PhfgbkV7mpJESgUbjOZe7yZZzsRNZnz0TklD7TLkl85HNR2E7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q58DPiDFd9Rvmzb4cF_8phGz7aE5NwqLzsvf7v92p9gOZv5AlNOdyrHltssxlisHIV3WrUE3bzeXanJieC0_7t5dgupWDItJXm86ktFC9qG3cbhPa_c-0SvNx9yqXi9WMQuwh8x57cJDL1TY1nZP1FAPoymNL-72SxR4nATlibsMqRCcBzvM4TAnCgi3GL42yx3yRgODMTsKjfydeekQBUeQIhORkw9O1a9wTfraJXgsfnrnRSm0JQn8FpM81clzjjZI6uLkNYX7nZ-7CELLczlRq9tw4J_rPbSEH8RIigEUUd7Lj0XlJEAP-PiTLCFvpADVzWhMWUZzgGfdh69cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=oFWm42-2C9vKCWNXnctsbwzy-gJSGFj0C4FeP_HXb2Z87Ln0-xerlBMpV8LrjN2AQ87tMLzIF04QSWszJwH6E1GDqcMLvCUqK0Ybr9EUqnmbBbGqocrtpS1sYL-sX5OaYRNdTVbBh_K1ZPuZrVdi2GUONpC_6HXMe6zMfBdLqdPMUDoisWCXlulswNHuYPvnUMHGOgI7crhVpu1RWo5UjPUwtwlFP9k_SsQ9XXMe-uKAxcjGJ3MSkDoxUh61BPqkkmGvhPHhF0W4dz9gRxpTCthgiaPtXuD6wnRIJafL9kYecyK1Rt-oX1-lT6S52SAyExx-jetPToxHbeORtLhJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=oFWm42-2C9vKCWNXnctsbwzy-gJSGFj0C4FeP_HXb2Z87Ln0-xerlBMpV8LrjN2AQ87tMLzIF04QSWszJwH6E1GDqcMLvCUqK0Ybr9EUqnmbBbGqocrtpS1sYL-sX5OaYRNdTVbBh_K1ZPuZrVdi2GUONpC_6HXMe6zMfBdLqdPMUDoisWCXlulswNHuYPvnUMHGOgI7crhVpu1RWo5UjPUwtwlFP9k_SsQ9XXMe-uKAxcjGJ3MSkDoxUh61BPqkkmGvhPHhF0W4dz9gRxpTCthgiaPtXuD6wnRIJafL9kYecyK1Rt-oX1-lT6S52SAyExx-jetPToxHbeORtLhJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukqNttWxvmLZMsnN1dOfkmb1TbjZvtNkfH0CyZeeZF65lZ7GcoCakaBPPWQjOinQVnyzfErwTZk4jlxaAqL2Qa-bJkIWokxU1OodmHSb5ztx__l2vuMHRcxCCHcF69YPEqJm8z4lPRj-ImwBzT4kx-zKJ97Zn_dDJDjN4VQ66zU_1AX4fIzaQ8nWIY4RDTmvZrRX19y9zoCnk2tP9b-m2SbCxpLlBpKAhcH826IDeAj_9KoyrOUue4O5wBWNfbbuSPJ9xgTWcXQKMWFrsDcIDVU3AT7v0MU70l2AgibB9TB44wfSXXPZYj6CfiHnAuS5JZoaetE1GdSJsFhABhlz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ySjU6U0ATxwl4wCFxrck2wreEfgcZAQrCc8qQGyJ1joO5wehURfcyJ9Vwhr2g5VdesweX8BfClC6DDLnMNP2QAw2ktPVGnSFnF_6Y2l73AvbtnDHVvy6LzefuNdQ9U250rgnwUG43Pkj3F3RcEXSpg8Izvf2cgOlsaglg4zOVU_7tgMswRw2OJ42hoNWm5i3rpDXwaDaho-xROhE8RNorpfZLLf1HJSj0oBLe9fEmLyNKkfBd_z_550qgkUlxjZmJhNO2NUePBQM7dHfoOyGKgHk_MAoLzbI-tGu5_bS981Ks-GUg58KpNzhDHebxD4LaIVkTlnKHp-9GMk4yd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_oZw4U4jmdTzp72A_a-PrEesCc7PJxmrB8E3K9BlvTfi7_naa26PVyzDjRvA2qRCcDmYIeNb5uO4CdemzqLPqaDJza_EKvmZq-IFx45OAJy6ZyWVPYSMfq9pzikwVIZ_ntrisTncSUjYdlApSJgd6azwGzaP1C5xxM-YiU1fUXuB4_9YgcLcy0Rb-1RWYSqoZAaxsWLdHzObXRv3Z8KeFnxg_0TThh6vkmqlX-spwODVgpJIq8aDbQhLV2IIsixQL7wB_dARbzfgBOmr1dYI6RaJAfjn5feK-Mq2tb1jP8XW519eiW5Jucl9EGAq0Oka9RewrRVKCfhZFMd8N-7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nmk0kkQGoWQ1uIU9idqqN1KVwmK8aeHu_9fTvU7iDe-gfSwn51G3xCQfOV5KxuUclt08V9bwkRO6O3xI6n21zp6Dgbh7KuTnwyr_BxqrNDpLC4qoe-RT1bYoaFnozj6YYxv57BEOyoGq0dfgRHiHVDn2z2-qU0cDtsX9ZQ0D2dSKqy75y6h8lIwYhFtTEpz4uwxVfV6bV59mJg9l_SZNlETwE39Oqhpr3OxUit3DAaeq-RRKufRgXPefe6Fv2bNnGA-SO-gQ78rb1PFGRd5I8x1ZmG6qIFqHC7vlzYfa4bybFWDCb_inNsvbqQ6tieOsZhwYbdjIyOKkENzLLQjPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7Sjbt4Mr3NBu6zHeDVWfIgbDcTiWPQYqfpdzq8Jb53ONrXuwiQFCNnR0ePC9zS43kTCuYIAISG-AKeg08R8soTkBK6U8g7kZsxtpm7paglVmdOGulL4XdOFPJASm1Od1tajxvF4vsX8yEb2wRoTSxVu3GTNJrk98X9oMCZlRD-pYthXWeYJ3LT2q4zzfCdKAoSsgDkv0inNXglkkZLlX_dobbLlequoOB6ETIX3PwM9m6qA-HUTU4PYQpYv4eVAqNvtswAg7UJeYJ8esa266ZW33LMMJp1RUT20jzGmEnptNGbInFB8oQhqlfNUJ2TqkjfmiXRMHKP0RdjEQdd6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=PUdi0ef-4JuYn2xpgsx2tCWNlhZJgSY1Le3TNVgpzCkC6hNky-tnSmj5OkNeO8fun8OcpyPotuo9OLIh0kT3lCeAPm2ZqulBi3U9gxz2-TQ9LOz5UDylnSISUryJLl17wZwxRVuoLbaY78CJdNLzTbcyUVlzjgLshWRwuES8V2ehJlvb7X8UJi1aWNkAfTG0Ln5YQtH32GXMTcB_EZtHJ7Yy27_Vp6olEMryar0SrnzKdUeGvWpe9R7h-U9QMxL3WWFGVKk2HcaRFFj84safwhfc-k-5m8GB7TqQrlotliWuiV2MA3DDRfLpOzcJDJCaIR_lUlaXJRe8wIiQeUfofA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=PUdi0ef-4JuYn2xpgsx2tCWNlhZJgSY1Le3TNVgpzCkC6hNky-tnSmj5OkNeO8fun8OcpyPotuo9OLIh0kT3lCeAPm2ZqulBi3U9gxz2-TQ9LOz5UDylnSISUryJLl17wZwxRVuoLbaY78CJdNLzTbcyUVlzjgLshWRwuES8V2ehJlvb7X8UJi1aWNkAfTG0Ln5YQtH32GXMTcB_EZtHJ7Yy27_Vp6olEMryar0SrnzKdUeGvWpe9R7h-U9QMxL3WWFGVKk2HcaRFFj84safwhfc-k-5m8GB7TqQrlotliWuiV2MA3DDRfLpOzcJDJCaIR_lUlaXJRe8wIiQeUfofA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfwQnk2RC0GaggRlCct8FrYuqjLEbCBRFckfaCraKnifgDSxWg2qLD-aAt-9SW7cQMpBC5ADgK9TQnWSqpB8ZnbBhtbgjg3qkst0URnIuClyxREowOaupU9UhcrXKmvFM6AmClQDSPq76heowKnrlyQIeCRSDJJntVGzGjZotGD1Vb0YKnvdLnsXEDT4lJXfBiqSSllrbV4n0Pvv4qrh_SEAfvulP2arDtjMtsx4dtZBFfreH7cpI8F_WUO3p2A-IUr_5XQ-Rh4D08Css_x4gT0KQ5vaN2BngRL9KBZLxqwYnyQvD6HHCJwZjs0XJJnLemf_kRVAmY1DJ_VoijAkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQQv38rUa0Y9-TYz5YQSqlRpOU0jGIYmlNlPP2w1a1X01BkOpWnhOVBpYSZhEKuZpsdIt1xKVUUFIKmpU-Unk6SgiJ0wD4IDIdg5MgBypbXgk_NTIX_J9Bn4xuwoViSKqLkleP2y-BtnS8UVHNGKPtPk5FmX2Mr6v23ji1psrTpD7HtQzgEYDYMavNfNGsdhxjZ2BAHQjqmMLyicAL_V_mVVBX-JBJj1PVN8tOFQwRH3xmUb36EkWPMpZaG8P-7FUgb-rIQ8_NMR-klL-9xSnjEIVK78RrLcpqiD4B-uJ8r3A2jcBe9gbMQpc2MF6xsgQVUUHinpqSd1Duovu3JhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxNvTBOUxANR5vlWdzUj09NRJQ89VNpcdaykoCO1WzNief4izWogjnCRlIec8EhSN329UR5DjZA9oXVFexQxHqD4zY-wPKIou7yA6UbUI4L34CxZX6OyaytNByS_SRFCA1L5af7mA_1-lutz3H12dE5nySsrf0EkLDZBstPdcaYMtXko9tR_GSXgQ9Vdy6-P81hewbWy2GHlu8EHvyxEE8rKSsdy2Av-JM1aOdlMwvGWEAOXEOmOCipMlSRX9bGzGyZWODpraJcmpjviPLFZXn938IbH1wUFS-GlYKbUVR8H-3gMmAjsPNDak_nbF11AZ_CTNHD7tG89yswvIYTp5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLq09jnU_7Zq9qH5FFpjpaTBJURjULBpePu7ZjboxO_237fqAdmvDIXK-aaOvEnQ46oNd6Juw4PRoOG3wZtoV5LLdvqO4U9o85ZRw7BsfkHqQ7WI7U4VugHMxeAol4s9OmRbodhdsurs93KdjEHEbY5PncLCaoO_XakXVII05J69cCI05J2rkrgJJE8WkZcvPo1Qn8Vxvgj9ANhn-QbsenrrqPymIMDo3JmSlGUnninrdBgdsCHXfmXnfEZJVQKV0QsbSTGxCRawXMkowT2wjwJ6g613bi8LxwHZV1F1_nJjTAzqTeKtm97gM3vDZeJJKcXklHCVMv_IXGgyo3P39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsGbf0Hdng3RxFLqkx0NJwPswdOufn1gsjNSNdETB-grTNyVcDYl_FvYdT8wqQOfbGlI0vvOjeG_mT8RH3PuhcbxMV1_0xKC6N7kplBpzFtXcdFnmAhnrSNzGanDeWCNtIwbckh95Ol_aznhXPwaDGLELshHqiGQnfqNv-cFDoR1RNfBG2xbFvMyZ5Rvf2H8AyRON5jpxUJV9b0WG1AzScPtsYnHEyq3vusBbrtOMS11FtMO_nMN15nma_QfTux2yqa-uyA1fLj5xaTgNJ2WeEyu1EyNfno5UTiRBV8f6l7BVaWrlTkcMX7-Nweu9GLj4myfIwgeWmZJCqyEF4sS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8eeY7l_7vpc6he4Hy--Lw3qmZQdEaoYyI8JDumuRYPQH3KQrGibzaqH8VO3Aa5i0wsIl134MotX2eE9gwLS6e_RBF8a2xS_VjZdumBAmVsKcYd6XiYIbtHtPiknLpyWD05ewy-yHnCRJeSWIxu7mrKLyoouWkoxEJHbR8jDHVodUwg9wXmdsnQpy3pdbAX60xf-iL1ALYUDhrmldXj69H-K41YdSI1IAWVgJy3AtFx9KvzjqUZiMf9uSX_jJav7sRE-mTjUITRmq9ms4A_jv8rIQJSrWgGoAATYODw1F8eqcqznmXzA4Eo6NnSkuYpyWtRzulS4qJY0yf0lNCjpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5orMiIwP8Piqkh63WnrT4B8RY1ti_Zv52O0W3KQAw4ATirjTBDHpyQ3UhAn523ObZRVTeVLspFk7QYFpq3LHDEigGmcyGTGwWP26c5bodNGIcQv8ozBB_uQ-K5QDbFEYbNNwymru6KR_bVrUuu3q2usgRzhk2YiePFgKjKCQnLHuo3RK1qmknnRmex4wpt5Jh9MDOePFwZy7Zrh32FaXm-Gsm9sXL98OZJzT27nqng_2ZbHhdjM-4IwhmKp430RLDuCdwxg3rhDR2VuisFqZ5WECLiWsYozMuZBMP4iug3uqh95-u2bbQELM6m1YE2LyupBoBO7sPrWBHn5l0EMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFH0pewiSJiFtE9Qzr5D0drAw1nnu2K1ImGScHjkjyMJ78mVa27spMBiptZH_irEo3YKN9geYcl3bKqTgJAET5yJGDjVQ4aAgazZirqq6q2_f353MCovQX24ivM2W3_IBEeD0CWtj4cOwe1Z6AqJRuhhurQrcM69_12c-ab_pl_F3gg5BR8LJr8Wk5llrpMOs7THw3laoubuyleGQBKoTn5L066pGUdYiYy2FbkSYIQtOzLB1GIy5uuZ6wR9qbyxq_GynRlkF6g5pGakcmdd8n9dudg4bzIEhWLNLXHOeHAWOv6ZKv-UH9m_PXRXfRJK8_sgvXsPkDQI9vsBv1p3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=VmoOln8qwoeeGrtGtPbnpJu1mhSCSm90OmiOqmt-9YxsKa5qqc3oFawj5XLnLC7kFhmvYk-Wbvd4Neyiu9o-m6hrZstA9CKfyOn6mae8ZUjxFKYAv7ShFFoSNeoWi5gX0V-1n7RxzxiGZaGkpdY56QjsEAu1D0lJvfdTvQrKGABGjoT9U2K_vLGusvpm0wpR2c8kAhd_c8GvWKPkCAu1QzZKQAbm_6vOoFtYdlwB8MOa0jeu5Q5NVU9ugBGBG1_laPG65ZkFKseTsLalSI-B6bi0JXyXWARb0UKajQP3hEP6NLz9o7VA8df2Uc5enzCOGCYmbozaFNTGWIzzDmfKcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=VmoOln8qwoeeGrtGtPbnpJu1mhSCSm90OmiOqmt-9YxsKa5qqc3oFawj5XLnLC7kFhmvYk-Wbvd4Neyiu9o-m6hrZstA9CKfyOn6mae8ZUjxFKYAv7ShFFoSNeoWi5gX0V-1n7RxzxiGZaGkpdY56QjsEAu1D0lJvfdTvQrKGABGjoT9U2K_vLGusvpm0wpR2c8kAhd_c8GvWKPkCAu1QzZKQAbm_6vOoFtYdlwB8MOa0jeu5Q5NVU9ugBGBG1_laPG65ZkFKseTsLalSI-B6bi0JXyXWARb0UKajQP3hEP6NLz9o7VA8df2Uc5enzCOGCYmbozaFNTGWIzzDmfKcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuLY-5rmE589mUAYV5HnYjgYEzhS0OZIYRluv48Gdl16r_K3oIUNNskfJR1uP4r2YwEB0Pko7k2tkCtImwhYmQz-qTctFfalpsxyrUDyNgRt_U0vRPZEajr5RApZRniUGLLtmVFFMmpKm-lYkF4P_ilve-t_AtIM4cklm4Lmlw8iDCm9fre3xu0tsCicG3xBQb1DXvP8CIDFo4uFLrANED1HnuSKOLLnXAeGFcKJb_nQeeoNO-gZZXOs5bCP3uxG3ANdfdfmwgsqvVzRY5TuqeVuhWUZ4yLSMfH-10-4lsVMWnwB8BJL_IoAtIVWm7bwdVgL7VcqYKX3oUr27F-zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=kjgliGV_vz_oXm2lFP-Dr9Vophbx7sXBHXqzEZ-T1mTWlLJ0Fqa79FarVI58gwSxOZv-TJWPQoag71MRgYC1C9HiQGSkFQAq-8QD3Hd8Vn6LX0jJY_H5jsLtuAuetHroKlUCLG5y2RMvrs7YrHV5HeUdmG17nxipHHUXJCyESlQ2-cvfiVE31px-DuxwTSvCIfUjRa_RDICZPJM7LgM7f9Og0hBiFlwARG7m4zSF-unB91jLrh9NqftkazePvv2E8YqUuS_M4cqQ9HL6pFzo4eQLPejTTQG2PiZyH7SaZMrXsRJJnRUUi5h414WI-K_wb3J-4AvEOFsEYfa2Lfmz5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=kjgliGV_vz_oXm2lFP-Dr9Vophbx7sXBHXqzEZ-T1mTWlLJ0Fqa79FarVI58gwSxOZv-TJWPQoag71MRgYC1C9HiQGSkFQAq-8QD3Hd8Vn6LX0jJY_H5jsLtuAuetHroKlUCLG5y2RMvrs7YrHV5HeUdmG17nxipHHUXJCyESlQ2-cvfiVE31px-DuxwTSvCIfUjRa_RDICZPJM7LgM7f9Og0hBiFlwARG7m4zSF-unB91jLrh9NqftkazePvv2E8YqUuS_M4cqQ9HL6pFzo4eQLPejTTQG2PiZyH7SaZMrXsRJJnRUUi5h414WI-K_wb3J-4AvEOFsEYfa2Lfmz5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=bwhw55NGRHVMOKlPQv4ctQ_zBK4b7RdHPBHk5x2adK0yZCric--b_CbRsUV1Ia0beYyASn6zTrgCDfgjzPQYY_KTnstV8aWiuzMS13fv3c-aEC0siS3j5cUYJ4R7jCaIVtEjVI2GiHdCMce3yN-dvKCs0gIVon0J5s5-FTdFbeLKqWOq0wJzgLpYuATxYYW0pf8VTFjOZpcOeoxBs1mMykgMGwpnA0pZXJGP-lwfJURnUX0ONcr2ttYkq_xC_GBJ1_6J2Nj4mhWU8hj_gKILWemog0_yM0zq9Mn2u6YIydUXm9XPm1X53RWGJCArRGZlKkEhHl9MUi2hqSYEXz8M2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=bwhw55NGRHVMOKlPQv4ctQ_zBK4b7RdHPBHk5x2adK0yZCric--b_CbRsUV1Ia0beYyASn6zTrgCDfgjzPQYY_KTnstV8aWiuzMS13fv3c-aEC0siS3j5cUYJ4R7jCaIVtEjVI2GiHdCMce3yN-dvKCs0gIVon0J5s5-FTdFbeLKqWOq0wJzgLpYuATxYYW0pf8VTFjOZpcOeoxBs1mMykgMGwpnA0pZXJGP-lwfJURnUX0ONcr2ttYkq_xC_GBJ1_6J2Nj4mhWU8hj_gKILWemog0_yM0zq9Mn2u6YIydUXm9XPm1X53RWGJCArRGZlKkEhHl9MUi2hqSYEXz8M2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FjZkMeS7XR4hFGmTNIRGT_nSNsx8-TQwJ37vJK1lBob8Zj6txbZkZdY_ejDoJ8dGPBy4Kbuk8dcqMPxD-WhMWkTr3ha4uNhdeDOEbLA_2qZTPnmXYUbHIlYWQN7QrKc5zrYZfFEPNtUutfEs358MYhtaUFNkjLZEN4z5fzxVhk0UJlOrR5T2ZePWzx6TIYGJY8RhBQ4ybwIS-H-_nrAnu_hAhBGgmFw1m8j-5wvV7FyW_9o7Ep4Ogu-0YVYTyuC8vWwjfVTEN-tqhbHaanwuITpIk78DQDhDbnJgRDtNt5AlpvBlBUL-W4zCoLIrcgjZLX9cCksYDHkYh_oEGpV7UVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FjZkMeS7XR4hFGmTNIRGT_nSNsx8-TQwJ37vJK1lBob8Zj6txbZkZdY_ejDoJ8dGPBy4Kbuk8dcqMPxD-WhMWkTr3ha4uNhdeDOEbLA_2qZTPnmXYUbHIlYWQN7QrKc5zrYZfFEPNtUutfEs358MYhtaUFNkjLZEN4z5fzxVhk0UJlOrR5T2ZePWzx6TIYGJY8RhBQ4ybwIS-H-_nrAnu_hAhBGgmFw1m8j-5wvV7FyW_9o7Ep4Ogu-0YVYTyuC8vWwjfVTEN-tqhbHaanwuITpIk78DQDhDbnJgRDtNt5AlpvBlBUL-W4zCoLIrcgjZLX9cCksYDHkYh_oEGpV7UVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5iaQftOM0jiI11oM1z1V7xL4eBayIrI98fxkh8kwPWGsyojYdWGfznK5nf0WYGDNSuhSrvSz7x-lJ1o1XCqwYfxKGF0sKv2mu_Sxmk0gMiVI4zRu0QHMNJL9JHvsMhtgIpW6_jwWpB7H3Ymr-Q-dyN7jI8MNGZtG8CYIlymcv-9_VySpZ7QQEiw8U9fgaoz0YnM-r9-P2NKD4b-OvCj5zKR1oRb4odn4qeI5oMRVzTxpLUMRBBn19l3azL7QTbX6TK3DnrpWUYg6kI2u8YE9Z_l5XrABgqGAYS47hj9gCypVieAjiKwSWhuj7vid0ZQwLpbFhXDVhw8vRXLwcMJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJyg1HlbK7b38m5Rnecah9bWAc1agOWhW4jCQePD_ZqrXei6CZ5IRChxVMclZMmR_p5aMXdvgYPkfivLbNLfFA_f9-BN9RjvKfU_NFH1TJfP5zg6p19fwVA2Ts4xyd_CeIdPPcO00SiRziUoL65Vr0I3vVDhj5gJoFMOIH_YhUx5CVj5yL7QUU5WjwFFd_wxj4UqZetpBO6Kayqc_CV20ulxOWOC-oG5sLRiyzERRpAgBvLdMDwvTR3XxHOeUqYw5PYa5ldNfFYdoUReI5nxf1svn7k8VVYK3wZXZnJIn20ZN-FU9fTN3k7JPHK3kS92k98SJCp-Vh_7hZyzy0U30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp0UGp599OMHossqT0Kkk4gAPGefhbSxSmK7yBxUEyYVwLiDcrDWSTARxvY73YaPf6LEpE0GKP_473QHlV9pe8U3HMmFz3TgnMpnQBE0ouKwu7eJ1seTSG_PJ5LZSYjXy9bs2ETyjA9T8JWcrxoxejyBo05nhZpJJGm_8o-r-wOBA2sSg7OzGScs5gWR5E91ruU3QMRvB_tIPQVRrp-P-PlFRQrYXvbAMPI-lKrCPvvvoIVx1nyQUZr4tvSP-4AI0gr-Z9B6FoiIcnK3ReUDYM0IJV9gnttrnJ-kV_qblDevcnkOG_Ieh4eOPl7qj1b5YLUB4fEsanG-_MCzGWi6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=GsioPDJebig-NokVjHjbiSLwXX2VLc3vDZ4rYQAjz4flxPz5fRc5xT9nz9SF5qPoZ2CF80xV9nNhhZNWW5s92WZ2dbMT20cgUhG3VTtVWF53_40UgKByNWOebo8vlwJa8OhaQWBOpINLwgN4Z4EmDVXroufLctRgX0Z7pnLLMC7xPvrwAq5vjxlWt6Ik12C355Amkt40-FZ2hbS1FNOThdEUouiYEV7yKNOrG8iBzEvj4y-K7DTtf7LxugW5lPqqwAUKX6W01mFNnZvF4M4CUVb1ZTBFkHVog52XahAM1fSjUjq3ZsXSTx7pdRbLZjf-IVO56vyYtH-yUrytas7cbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=GsioPDJebig-NokVjHjbiSLwXX2VLc3vDZ4rYQAjz4flxPz5fRc5xT9nz9SF5qPoZ2CF80xV9nNhhZNWW5s92WZ2dbMT20cgUhG3VTtVWF53_40UgKByNWOebo8vlwJa8OhaQWBOpINLwgN4Z4EmDVXroufLctRgX0Z7pnLLMC7xPvrwAq5vjxlWt6Ik12C355Amkt40-FZ2hbS1FNOThdEUouiYEV7yKNOrG8iBzEvj4y-K7DTtf7LxugW5lPqqwAUKX6W01mFNnZvF4M4CUVb1ZTBFkHVog52XahAM1fSjUjq3ZsXSTx7pdRbLZjf-IVO56vyYtH-yUrytas7cbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKIXkiVwENSNkFazKOvVMFMhQGD3Af6jGhLvF_ql_tjgw2pxdeU_JVmO7uWGdrTXfvPsRlVN-v-8IGjLFwUaGcrkxsWuczaIQ25UjS-SVZWmbwxdpXk6Jvk6u4WewIWfLJBjBSemtwv0KFmBI97v6425rvCIKcQdE6A2SjdPHDsvE6a6KQyIhh-CXeYTaZah6LkOxLNZNp17flCk1TUpyjoa2v_yKXYwpphz_t2zl-2_Zh4DMsO2a1kILAs01PhN69nttqP5rFxzYfYdJKYdvC-Go9bLgq7kjTdCstO5CC1v4LB9irvYbwyKIgnoqlAh839H4oNjWOA3HChW-KRyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emn7hfzFQn25R3F7XvGjUBRYxCkz7MmAMW6AH4veCtp-VrYsqi1EvLuOafqEz8bDIbqLNEqIuFSpZv_q2T9Tty83and1zDQ8Hjn65w6J40TLNU3CGLEoqCdutT5_-fz0p-cbRJPSWwNR1zZkIID2vrBDRnqLvTgdNaYkyn4pNN2a9YPTqL60sPgBhPM_fEklwfwK2iZQVhkH1c6M_184KoWN_hyKfb45I8kysJrRvA1YaIvVu__OAgkiwhCPSmFribJ0ZVZL5HdhTf6-u9xncoahyPH6D2nw3Ij0YswB7S6tEJWBTZ-h8NMj-FfE_l9u07zsk_MByPS0AlsJbu_6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOCEK6va4PIemKaVKGDboa0psBSQkvy_KwDAmcAiBT6hh8t2KR629FR7GVmWES9m24oAmWEiq8C-pAVIBvy_m0stcm6OhXfTCqT0CqvEvz3tbuDb9TS8TwMSxDTDIwmqYMUDVSlwXsetzQdMPD37IFAroljLLdUE-H8EZAwclFjiD9jXeWDMiQYIA28DB9zMOQycUxyeIPLBmQOgdOaXQIQvSNKVjBC4o7k-aYv0KUuU2d8n0KDgYGec-fgf1hem-8oBOsUSSvT5t8LPBEm_OK5plwOjFfqRtg8bubyUGTdrlqhHeer89CyhqamfUOrzBQJvDpgmrQ75umf0sgN4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPSSKhOFYITAi43VD_hsSak4U5SEcobLlViC_UPG3GCX6HuJ-rdKGbE6y-ZbbxqLxXJSEZHXxwmRz4D5FR0mMVXF1QWIlSMJ1jt7lkhOuyEfz3WKbamxM2LNLoDOhizVP4VWCjO6oHc8SShb473H72pD9PWFMcnG_yAyRX3GvHdlsfKXM8kQlBQPjBCLQHX0V1BihusHRNxnqhUToiU7rZqXOBbZcBM6MGeEEmr16E7umknqGAE3nYt9VVXZKIM21d0I--n46GTVamIbPFel925SsSGHufsMs0RIz5oaaFQ28pqt2fDTe0cvG1LcZYKxUCQt2arsKTJXqDy5rWarfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwGfnEAVS2MgNXUYM2voXFLZYH2aPWzjXimMdmzuJ7tyO937gBYaEb_BJSxsB7qHXuNTWvfT28ScD3rCG-H4u1PwHHauxfnzOOZDKj_o54PHv0KFat3zc5-EEJTw4dJ8LoXvtP5L0Lo2xfP1FSsPriq73UiHFh5p17w1qq7aOkT_iBRb0o6ZQHy4oKE6XFfn6AjeP6OC6Mo-Ud88xC_cXYzMI_eyXBl7Fs4RU7b-mJzh43ERbtSY0DRl-vxqXzHa7EYeVpXUhwvkFPr9hDhI-6DaQayCtU6txy9PrEHZklQ7oPDyyISsueoxXOxnViFpQa1jpEFQpQIUz_f34aPmvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=dQ_c6SBA5-MhwHuWjQhE_oxLFiVYElr6r8Yy1GI_3zFyIrhOsk0i7TJvMXBjvMIguVmqGE4wztpuDI8ThlgxIZ18QKR5YP88dGWG2v_J-9SKnfdaHLD_TTcbW_MeRLLfwC0HAWvVCJ-IyggQmw8PmYgkphkhoILkV9JB1rf1CgPhW3NJBMdwY98_in9ygJzP-j1PRaaKDbglKMeRIZ9P3sxeQ3LSbWHDuWGSgO6QcCgJxkuQ19rMUNtLmRfpgJ9nB4ATI-vWedMBYZLwvsNxxN2_OtN3aNo80vg_wqUDwqEIOvSGv8pxE0Oq2ciqbO2GOr0dqN2SedKoIoQY67vWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=dQ_c6SBA5-MhwHuWjQhE_oxLFiVYElr6r8Yy1GI_3zFyIrhOsk0i7TJvMXBjvMIguVmqGE4wztpuDI8ThlgxIZ18QKR5YP88dGWG2v_J-9SKnfdaHLD_TTcbW_MeRLLfwC0HAWvVCJ-IyggQmw8PmYgkphkhoILkV9JB1rf1CgPhW3NJBMdwY98_in9ygJzP-j1PRaaKDbglKMeRIZ9P3sxeQ3LSbWHDuWGSgO6QcCgJxkuQ19rMUNtLmRfpgJ9nB4ATI-vWedMBYZLwvsNxxN2_OtN3aNo80vg_wqUDwqEIOvSGv8pxE0Oq2ciqbO2GOr0dqN2SedKoIoQY67vWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJdU8krD4moVP1xrrzJpGFsEn_dJxscaCrNsTKeQuLpSkt0KLBDSfkQUXHTShN9fDSl3nNoPJraHaFbHogBhn3pYP4Y-IqOCZ1CNrscNKiBZQ2_uTG-Kblfso8g39uz1xEjbseQ1b6iDniGT5IwVlwzurjMzWWeAgW3M3AS2-1SAKT4tvyyGQy9TDHDtikkKTwCSu5fgGCSaFiYfXCXojN0JOqojvHcVEdc-fmgukmLFtkdj-Jlf0XUrqZuopVECK2J6HM1P7vjcjDcMv4DcCU06PsOjzXcRmS_tZ-7rOamaGO4b0vttHpfao2fzuHS7rq5pcpwq3z8vgGK55WTSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G25AmzBotfAODafdVlqu1DnFd9hv8R9Ns32SrhNgvq1GMimIeZrn96CViGAKEZ_3XguwP5IGyG9_TKU2zBpy6xRGXDhihhmSpCUdtaha3gh4dJhMe7IAdz7aqVj8m6wnPdkBGLHYJ-jiEnl8fejNDcKPbLyeSXuwIrjaIswL_iXhCzJCajLpPqgbb1RoXoPeCnshX0xBjvHVTgDKhux9C7v-yukQlISH7yoLf44qccW6-BZLM42SJP6t6frfKyB-QMgx8g2ailZVCQClNV601vTrabVlkzT9MJTC1qNOKUZLAJQDTlyTf5-MQKeYfeylWnAtRDQfapHy_552DX8zEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
