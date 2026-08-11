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
<img src="https://cdn4.telesco.pe/file/apMP7fjkM_CuorJgCv1ch-wBuW5a80e2vvuDiAHd0LGeNtufnig-6MEA98loFBzwSAp-EJQlR9CxW6Hbu_-giza2vTtw8eCB3WZp34NwYB7lD5Mz1gHfZBX1SeLbBZQ9GWnm_cL2f034wYMQTRem08-EDimiZnc5wlRKAgLZHbplCufXwCKxho9TdBuiUeefQPNMOdKczRJWuHuodF08sP23jtgtjCbjBb1uF9GHnSaSJbWHGaQMdnwqGt76jCrQyHi20BubJRnaVgDwccaFOmizE0w8oseBvfN2Qj12ag1b2lJg3xihup35ANGOCwTRP8o4s2uIQxn1VIX0Bfl7CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 628K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 05:08:25</div>
<hr>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=LsZyxqBGdj7FZHLGoxyus9AzPLjRXi8kvJkABE1cbToYhKwIE9gvZvB3zSSYNKoF0VSuQCfL1_aesLJK9cqEF3SqLN71S9GbDIhhQ0hZ3vSBucpyqoFhzu6-UBJgoifQKhqgS1Aezf8luXHedNjRDjXgRVuTpp9bMrVMSG9m3tkpRPh7AWj781Y8dxeRCH8faeFb5jS92KmM-ekChu00gtWzyK3WJDtNU5vImGzZWmLj0ZZtERPWbw5kW5WDMJzHHZdrFyQVvSrqWmGbBud0PV0QStS4aZIKTbAehzsspxaMaoRMCJT_KvdS94dMATS7DGT6g53c6zRof1eYFUEpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=LsZyxqBGdj7FZHLGoxyus9AzPLjRXi8kvJkABE1cbToYhKwIE9gvZvB3zSSYNKoF0VSuQCfL1_aesLJK9cqEF3SqLN71S9GbDIhhQ0hZ3vSBucpyqoFhzu6-UBJgoifQKhqgS1Aezf8luXHedNjRDjXgRVuTpp9bMrVMSG9m3tkpRPh7AWj781Y8dxeRCH8faeFb5jS92KmM-ekChu00gtWzyK3WJDtNU5vImGzZWmLj0ZZtERPWbw5kW5WDMJzHHZdrFyQVvSrqWmGbBud0PV0QStS4aZIKTbAehzsspxaMaoRMCJT_KvdS94dMATS7DGT6g53c6zRof1eYFUEpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unTtPf5-6rWSMXOudx5_KwDcXlsCi8Q1t_p6V5MbCBkriFip0lV65H-YCflpMH3jqOHn5OERbvN3NH_jzqmCxTUYcRI-CiPp3HgTpP6rGDTM0FMq2QDCQS8ksFEGvvOsHofCwWdz9YqXS4zhPnzUhEhhKGGh0bVBAy3b2LcC-3DO8jhDJJf9pIk43CEyWm7WfmYI9zL7YR3KK0s9jgtjfEqLrns1s3B104xXhVYVrzW_S4pFKdEQp-WoK1YhF2uJCqEcNrRp1wGOi9ZkY4oAMRiMYSZyB88X3lV6RMxsQI5prHqhbUZePNlMjsK2ZtS0XdFecu8wB9aYpWqd0kHAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=btQffqrMknvxQDvHWhYecBtT39tOGrftNX7i9aXSycuGHd7m-ZwHt3My9jvvPajk5znqCUna5XCxVcJBQsApB_Lj69WTKCCVE3E8YWe0g4AMiGvfKdA5gexIanMFSPy-NKDnjLsjqdKyHVHRqQMqfK4nzUsh1rDwCKOBsBLHr8MEauBdNJlHyfG-a5ovoK-yRAEy6gfB_W9cVDqlDd6eCuUnCPA8q_uNltz6JKSDLBaq5p6oC72JDPKRspzSSnEU_NTyC51_TIDQBOAurtwpF3wrXqALfbMOqQyfIAPId20SUvxU5Pzld3ndhBX8RlmUbW2FmGkKU7gn_mrvEnUECQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=btQffqrMknvxQDvHWhYecBtT39tOGrftNX7i9aXSycuGHd7m-ZwHt3My9jvvPajk5znqCUna5XCxVcJBQsApB_Lj69WTKCCVE3E8YWe0g4AMiGvfKdA5gexIanMFSPy-NKDnjLsjqdKyHVHRqQMqfK4nzUsh1rDwCKOBsBLHr8MEauBdNJlHyfG-a5ovoK-yRAEy6gfB_W9cVDqlDd6eCuUnCPA8q_uNltz6JKSDLBaq5p6oC72JDPKRspzSSnEU_NTyC51_TIDQBOAurtwpF3wrXqALfbMOqQyfIAPId20SUvxU5Pzld3ndhBX8RlmUbW2FmGkKU7gn_mrvEnUECQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMmq2Hx2jWUh0-gYnM3W49LUwYZVy655GLj4XM-aQYdRA99xmR4XP4tA-jl4lu60S_b7QEu84t16N2Q95_1_4dIcv00QerN875sHTa-AwfAKEsV0IWkHTeDVGAnrAs9B0DVrzDSVNqL7m-1fIBbyBh9c5B4UoDB1fzrUv_zr511UzPIABVf8labIT_6poLehNytBw84i37UCNcvfBD9beDwpS4B6up5F20VhDcQHpEgJ2p-U551bxIlkc56fv4LEhbjv-9hfl_SQWoOI7Q0nnWYFzmeUlUiUiuAGOPQYKTwnQVTI_pSZt-6E9ZqTTz1HD8jkgQQPGUZCXBg66o2LjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwp3K1l_oHlfoJEPbCfkKW1SBXewk9CpCDbnK2KZD7u_iau8haH-4vec4uuB35VoLbYySKwl5XqqWMKeEDUXNNPHIruXiQ0RdowGpai6cdzDWpIsj6n2Vn5WSy4Cy9bC07BqKF9_20wU2JiXRhdbpatwPz4cdGzZnspc6Usz_ImdxFfC-0mXj4mt7T4uYhJ0eTYrQsTCWsoh03a305BN_-boypY5Zc5o1oRv6X_hILtoUakTeDZwoFgcaLsGLFG163jFMWU91oAIP2v4XabwjQ5Irx_h3mB3csYy-smoqaypS5KtHOwuGrnGamsloiob_EmwZO6iExKJIvPBTOT5kSEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwp3K1l_oHlfoJEPbCfkKW1SBXewk9CpCDbnK2KZD7u_iau8haH-4vec4uuB35VoLbYySKwl5XqqWMKeEDUXNNPHIruXiQ0RdowGpai6cdzDWpIsj6n2Vn5WSy4Cy9bC07BqKF9_20wU2JiXRhdbpatwPz4cdGzZnspc6Usz_ImdxFfC-0mXj4mt7T4uYhJ0eTYrQsTCWsoh03a305BN_-boypY5Zc5o1oRv6X_hILtoUakTeDZwoFgcaLsGLFG163jFMWU91oAIP2v4XabwjQ5Irx_h3mB3csYy-smoqaypS5KtHOwuGrnGamsloiob_EmwZO6iExKJIvPBTOT5kSEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=l5CU8nnFWSCsmrJbs7CLkiXAiIcX8DFzlWjjFvFzf0a0RKYRoMdtFPn-wkaTzTvQclUqtiNsZdoE3LKsEtzCz9LFKaPtywIOtUkBOY81jo4n-UybT6fBfU0qt6k1ElPF9kAAY2w9O0NVTtqKKW79_071jrXCAlMh0RG8RbppjM44AoemA7jp4hOaxyV7qdsuNgeSRgVaVJCSRvv4vJk8Xb0Yl_Jqxye2HPjE9m3geJLwQA--wjQyytlQVUvo1vg54EE0nUT1uWiXJqWgfGCH1KZcr_YloyATIfIctlca3HEzgdYBS3X-IStqS1dXkRonxFfAtjYw9S0itXzK1ugBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=l5CU8nnFWSCsmrJbs7CLkiXAiIcX8DFzlWjjFvFzf0a0RKYRoMdtFPn-wkaTzTvQclUqtiNsZdoE3LKsEtzCz9LFKaPtywIOtUkBOY81jo4n-UybT6fBfU0qt6k1ElPF9kAAY2w9O0NVTtqKKW79_071jrXCAlMh0RG8RbppjM44AoemA7jp4hOaxyV7qdsuNgeSRgVaVJCSRvv4vJk8Xb0Yl_Jqxye2HPjE9m3geJLwQA--wjQyytlQVUvo1vg54EE0nUT1uWiXJqWgfGCH1KZcr_YloyATIfIctlca3HEzgdYBS3X-IStqS1dXkRonxFfAtjYw9S0itXzK1ugBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxjU52wYYXvr4a5WRgyjX-r8RbjByyQEICGuWzJLfvoAN7eBuxDztP_1w6Erjyqca8oNffX6sf79GCqIdprviXYXq-cyXXZTDjgsIW0ZKeJ3Im1t5NeuSL2EOSGWtCKwUUgs3c7IVp4eeSOsf6FXUWJ8QBLQy5Spo61mrnA78T1ZHpK8TutZRXxx6FzR06biMWeV9y5HUE0R0UaUFXUVuNrEBlRRS9N_rPIrwKHBc5eYv-0zbhWG_YJ1ch8GbljwfiTJvTLXNh9byve6rC89G7Z-lmDIvwHMjKOLjBcU8O8sdamXKo4c9842kZ-m-3-D93anxRybr7idedO-dOnSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrJ9VfNXfmIn_I_ujOmtDsOR4Bc51zOjRFkGaCOtBOv4Aer4mj4W8fYE1dVwN0tS9MtNSti8lRDf6doeLlk18OJc6O7mTT7Kx_EnAEGhtj_UxPHurXqk-zXSIhhshxluPOqYxAmXqRMOttTiEOzbDelsG8vBhLrZ_-iKDyxbRkXIBX9K7vrrAeEwjDRyPc1mDjkXUl4tKUKxspLLEUlKicw0yXygbQhzIMaW6WkTlp4y9W9zjtJXFn8yXrD9ZtOtf9nNK8a4avK1yr5gCuNMxRIn8v4G-wJaUf5Hta9LihQt5yJFqqFwG3Af1lZrn8HIpp9QX-BgTfolFUgJKNsQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑
️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر دروینروشارژشو
🎁
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
‌
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa19
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/27496" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=hobq3bXs0j9sz-5EWwedOISfvYqrC1sK_XdYP0dB4kFOQ1tcwn384HJeMC1dBWPLrZFwcWU6JFtVgkASjNCv1m_F14A9mhmi4NWukzcNNvwIIuJeGg6ZwVEURGQoh5tNa-S8AI8AQ9DrgwljyDbsJdUrqMVIYQdgnx_EFTGBOwHlNiE_GAjrGPamULaoSouYtfSyLfPKnHllo6ewvsypXG6P0X4mP-6UzPGpzrtSf4SRGOX3qh5EocNBgaZvF2Qbbk4MNcOVewpxXQ-GHL-alPoEj0dNv1vhlFPMuVQaBtfcj5GUtM64lt73B3UW4K7qILC7zm0HMu5bMNSJDdNXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=hobq3bXs0j9sz-5EWwedOISfvYqrC1sK_XdYP0dB4kFOQ1tcwn384HJeMC1dBWPLrZFwcWU6JFtVgkASjNCv1m_F14A9mhmi4NWukzcNNvwIIuJeGg6ZwVEURGQoh5tNa-S8AI8AQ9DrgwljyDbsJdUrqMVIYQdgnx_EFTGBOwHlNiE_GAjrGPamULaoSouYtfSyLfPKnHllo6ewvsypXG6P0X4mP-6UzPGpzrtSf4SRGOX3qh5EocNBgaZvF2Qbbk4MNcOVewpxXQ-GHL-alPoEj0dNv1vhlFPMuVQaBtfcj5GUtM64lt73B3UW4K7qILC7zm0HMu5bMNSJDdNXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XctliC6CNRbY6Hkmw-NpbZRB5SsEsyDtpghy_Sq0Dim1FYesN4sr-6c1vS3BDWvT8n1fIHofVjGooFjEpfkSC_85wNhGgJj861wIc5MiUwVV9yBNC9w1D8LNSTMZ2tovpFwTFy6jMJY8hujH2qDX8hhpa86haU53v_MGSAsLWtDZtSffvIUwlVeb0mpXJZt80x-nq7M4PzFTUTOIC7Rr9yqGc4TDStByBAvd10i8FHqeLleGWx_hjP3JZ28IyVCXKt8VlzVuIa2gnaMY8qqTaxz3FxmraV_B8R-vNs_-VkBEGSRnc9GT3n68zpj7ectNS2Z9vdelXlmcJQjiCLQhXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb8tXM-TQZLqIuC_kGrQVgtx-B63jA5t5j6REUsvGb6vwEW9Vw2sE-cnGAYRx1s9MwGMkDnDUsp3b4UruD7cUtu-V5KHmvl0rusf4yfP0BN8TvcyVN91UaoclDXeZt5OWXEPAqoDXvcmB2SPRNOpCOinvQe7Seu8MhsJPaBgU3dITYFXV0gLmG4Pq4KF34m1GeOEElMmalBHUui78FpiTCb9Gy6z8m9xqwx-055RgHeJiGjnizeKT-NMJ0aObEo36EFfZbGKH-M3UpbmzOCktDmuSDoknlaMIbRBIoABwopDxeQlWpdGrQcYke55vmVN02O2Jgf0qT0wRus3P_Hy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4ApDb2srHiHMur9xMCtiWjC6Au1QYNJ3g0iJ_sMhv9abYrrb8MaZyAo8SWandaBc9HDmwa08PHl1V2mvirfbn-z70NUs1diWAzNcwdp5L1FSsZ_k_UKVIucFVCA_Ed79fGT4T0r2MgNncp7ihL9Ov6BHTorJaKJk97cLjvM5fddkBCVFwtgm2M85V6BRHvioVYQhamx2j6oEqMZZLzS093kww8g8oIPobwfHHNP4v8Blvf6zikkKWEECezGGOe3lscbqpwz5CrtCa4jFZLw5pVSozEIySXuhUS7Ym_YcDYvplKoBL8ulMdwP2yP5uicXrXvi7KJBDGw9OySQK4zWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK4iUMxZs4wwxkJEeN4zOwnTutDb64qKodC4kY8ADkZEVc1Q8w1ixiRDSfKV1N3_aYFw0lwpKAdZuhQf6h-j4EsfpLxaCPAJVBvlKrBqG4AE2mZDs-vFZBJkfF1tItWbG11zYSzJpAmPo3MJpuKVVsFKMSIZg_1xxSFD_X71NSzf1mfcTWEKJ5sF5JXIn8xpz0K5Lh_mcMpSzCB2IzzNjPLvS28EKaGrfIDK5yu_qG1xgNcAx14GjhDENqnZb6Iz2nxZu9bbnJKhIey9HQDsbPfj0X_-66Ycb5Qaa9gjwqNU0xpqSvxRy8HeMXNncuR09RSP119IapeNFFMhbgFlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifk9nA9rC8Fk9nkVUKRb1f2I1MuITo4UTluJMsyAns8mCaxSYrEFQHNUnFB3P-NIQ6RCiYmKQGfLzrOaa4NCoHFWaUOokWaj5xq2S2QJNjITe3353Xrnd1fR3ohLgV1tJ8dlDUGcbW5PYrmBy1D_SytIYLKXNfSfYpUkaSA3aY2hCRokX-t51480uP_pIoWJMx8xX47CJRZG2qQBwIYEPQxH2egddCJ2Q9vz4fDHF8upqniE1t0GjwZLZB4vo4uY18isbBZKYYYhB9PtYeDYmeUwKJ1zKdhUssnpdoR9XUFOLnXgWaRT7lrjdXOj8qr0U2zuEQMu_e6Ululxts2CvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8nd4Cn8bdBrRqsfNS3YKflqU5R9c6-SclyMs8lgLDOrqgcaZvJw_634GEWaFucew1Dj0bOy67S7K9fLiONO8BrIovpq-lOxiZj3jC3WWhg5dB2pqf-T81fMUqXFTCViw7IX46hVBqaR4wyoNS2hthOvhppTWI8L1PvkFqolo4EEN0mV2Xh9wzGISUXqZyEmBZQj9D7IG852KDe1yo1e88puHiyV-4Ht4sNGDkRzUqlSY-m3fq-5mGg_uq5BCgdhEYqSRhMrZtqVQnGTFrf1P67UM9iI-VJf7xRjyQ2nMp-PQd6Yf97IWS6M3iorH6-iK6nX3UnkKrr1A0AyqxuAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG-35uxst_CuC9wxcF6pndTz9LCRx59SCimUwxCP19rrVyMlUxA8pHXuwZVd6SgI-IPD7qUu-2puY9kEK02IPhV22fBsJr91OyrrgRitW7Z4l7hKlgCUlqhb3Tat2NeK352hqMO0mglbUyFD9IIfpGJjn9EBzWAmBolLxFyDar-_E_tSiWYe81VvFncyR7pvJv0MZ5KbW6jiJwj4VIqSQHjcak8-nySJEnBpFjyC0UqhwFw_JyiodSN3Kw6-NJ3IwCdpd55pC195Qfg0gu6EimIvF26WA0I2Pu0gbraxmt1YeDkbl7TXBOBukU8-rcj15ZXMi5Lkb8iRQLzFURcRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czLDJU4I1eCZeTunqw9GGMWbAMTa6_wdwJ6W-P55FC-dQTzppNyUgk4brRFZJWvTdoGn4k5fcwuPVt48lhwkSWMsRcJy6CS5eFMQG3mWAmOs_Q4M7Oqm55U7PGq5DZiQ-ZKfhTYnJI-5w-Xh6fM0377atHryA034fEcC4EL4kuWOt9AvAxPqMKS592j2PdsgLIGbY9hBjLlwD-W-tp9jeUhC-799FjnvEcgrnp6kdWkJc9TrcF86B2X436HI6F5jtXFboYEaP6V3CTaKxQ7u0itKuLvdshZYuZAJEpaa2kALBx3S-XTKWLaqfviVOEj7wQkFJ8F0Ym7OTSzybF2J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZGn-YOBbGfkn97fRMjAPCEcyJllqzjXAjaNS2z6kgMonEjNpq7isC0-gQuIW9oRCH74UUcQ85RuM6C7BjQfttU_3AeRcCKQeNYNTQEeiaAICo19tPBFonmcPRweV-uz2V_mWKT8QV-OrmXBR29vQtib2Mhk3ttSTCsjgdSAUM-WhkSGjP9PGlsHa0ExVZCYB0TFPcUaXexD4Yjuzwx50Q20_Oq6gTEbY9f0oSLqx_bNu06m3kwxgni09REmFwNC3YZZbmJJZbyjUCtrMCJyETD3jgLITdo24eaVIkGTHA0y-5dPJIMc51aQDAIs4vpLlmbqbH9Dta_V7207j37KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6mlw7U1jnJN9gGakrwhp9OVJD1dz07ei2ymqiWjjMbgMiuWMZp5VHM28FotiGK4-TC_ZekFCS2F3D_ssiMDXnrA_SVNeS_jArNm3BPd_O_T3kfiYAz3TfGbb3zTcnPrmXpGnpYYc37XnBlg5zFM4DqdKvRw1sBwOwY0PYyilTrAzRDn-xagiNID1f8FICB6bEkOslng-ZEM02u2B5tRwPzxqViHbiI5PmhPGm_heIj7U-ELqN1cdNnfmjJwydfG8WuV-VZF8qZQbkTfviCPSvrZM4HcR3jwG2CuGcpHWgPhLx430H4B4YsEbAxWKRM7S9uUazl_P8zzmJ-sE4hYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dn7skqo7h4qhkaWIVkt7ASxkPsxeAbK91U1EXoWsJogXImERuktDym28gRTh9ECXz6BuL1YT599dWNwcgWSSctIUd7BlMGX0ixY21Hw6uUJ_lJOi2_cm8AUD04z5R9E3zqLDMdgw4gamvBD1oMuJ8pv9YE9OAjZ-8CVBA7bW-VQGCRERpq8xjmv3pLVS5qw4504DW-oOedEt4uutRp_2QDix9FwUPZk84PJt7tAqIl6XzMyPYCWTQKeRQ1d7XtIhTG3xBdTMkqncut9UnLZKPbx-eWMjR1yxWQQjvP31w3l75gSz_psVOSncJC1aaw95Zir2jAoPzzCmaoqdBz8Ocg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvl-TCB4KedPl5r97Tgi8t3ciJ_iMkPsYBGMZb6zyH3yubPam8GZJae6f3ZZyd0KtG7R2LwPfJGr3gbp2TbR43OJaAxFOEvoH_i9MWBTYzR2a-puqJaKFldhXgJFzMBkZvJr62rV8vHm385D6A6XM_CI8luoVnuSWri57Q6Sj_3JNzgDmHTjtxpgSjoZ9YxgSQsZoEl1NJs4WVD3hzU2wgWieC8W6qCpfBH_RSCZroVUbmPGZxyBHwSMAefFmdCgE6r-AIATmEcC_T-l4DDopJMxX5UABgew1eN5Nh3VOwI0uy-QGvNqYOY8mSjrLDZ6tsaKyNTAzjsxuBM5MQnOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSqXaMB9y2Mf_WDnpD-lxie0HfV_Jw9RSKL1vtC6XGB2qrCuMHdTBfVlgdgvCXEQpx2v40Lfp2PBO9oUZFpwgOtLGSvFQCZ0sOLXcY4tuHwQ_IKqrJbkUnhC_QKInYTI198sto0kE9kY5S9txxdXJQRXtHIJ4jVSVXSOLJ9SO7yMQnaKzGriGsI_GmL59TE4zeuTBHK6Mb7ebwiXovNHhtNGQjPJ0wea_5VcUGlqzCDOx6yhRsP6MXhRyBkF7Ca8wWdnwkwpiHGD8oSMKrnzGskXddlJaIzAqicD2OgyxXIwBE8i5dFendy_Hwq3JdrSprkbOJzqD40Xp64SWqD5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bceG_3mH-yMDMbou2JHqxo9bxhwkwwn-jywVdAj8h7VtYlkbtK8FyRJlhS5x5FyXwDHKuw2fC-iiMfT5IaN3KWQpmdH7Fd7A3RuW4d6Pym9Ygx8-YsHILu2aDXLgsGghjbvDyLLGM-ZBxx-pzbaK-sF7T5mR-AGn-ix-DcJ1RDAXUKNO6d0XnTX_1BLqPaqYFk0L_tshRAG_xCcBO21QWi8ubVuM_IgBFBwOQHhYF335HTd2thFECOqv5Q8znDPWXkLCy8j-WFBPPsPjTaisWlIF0J_6_pp97-D4Nzmh3kORheGzkR4Ll_oZ0lhRT5hnZmnfT7eQ88q-QUpew1XxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnVWeiSnCUNyGUBy9SI7-uOO_BM5I-IXUtP-bnNMP4sS9oItoI6BV9CMFrLgn_rsrB_yN9eA4Mj4dQSb9XUVuIDFQy52_okjD1Cjc02eukjuREQhFWO0lAhAYccktlPrJ_sTHK3-PUY11KZ9bLG49wEQe5flD3zERQnjhDpEWeaLqjOi76MpKx6LiZFRoGEsI9sz1lZBH7Lv69tfOAT0bsg_Co5jK-QmI-9sj9Q20rjAE_jSfDC8lGr2aNHSn7InJWJr-13CXJPRYxwgnrZVOyqU-zZf8kSDTOEkbYfV0o30mCMKuqcxEwz45B6ONl7ChTqBDfomMxh_IKRnPTlyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-v4oFprzbl5azjRfonA4AWxaf78QFo89-8BAU8S2ZeX1hIfF9NM8gAA19JSa-I8I7TGqs40360y-qd0k8vASXE9mX96bVq9jJwGC7jp-8q-2_vxLFtt3_5rZMI4IPjSrI4BsX3OXUeqRLroDSqTM2e3WYgEKqvgmixOI8b0g69GBYcOfWCv7Gdp_XBo6J8W3-7-RJL7bJ9g391q8-aB7MD3UEu9iHrDERZe4Efmxq78DWpI1iP6EV8EL1zqYvLGhq7DyrDhihFh3534NNzfvI6GiT7E4_ORIAeNV0Zc5wjNYLheCuPeq3dTIHxvmi8WtYP6jOhzP14vOx3eX9T0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریپتوواریزکن
0️⃣
1️⃣
درصد شارژ بیشتر بگیر
🎰
بونوس ویژه‌ی
🎲
در
اپلیکیشن وینرو
🎲
‌
✅
بدون محدودیت، روی تمامی واریزهای ارز
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🤩
🤩
🤩
کش بک هفتگی
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sg19
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27477" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXU-SKfD_Gx1aEmZFxnwSxF_E8E3IyNSDClWswLfhc6AeYEU-rrBRUb-A3TahuwNXEJIm9PUGU7Nz9koiCAKcYk_b6GNJAnGk7N6a34naBd5_siubTe0QN2MOiC3Mjnp0nxFaS21eQuZWcg63_sotbs7Oi0rJ2KBcodBfUXLtKmHcypLvP9zqbL8DelH3sLuNfW2sCAj0WXKptJKJxNJu0MK_NcdIq0GDOF_sO-k_hrwJehQwGhrzhRsGGcXj9XrSkUKL-GV9O38eUjFNFLAkUqcFhKeoduCQ-e6LdGnFNvf7utm_ou4QlZDW_j6dyNP1-yQFKTqZLG3mwOopbh4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2r6Ga-FORNtrJvAquuWNo15kBLV8nSMMcowUGpzVQ2i9v7pSVJosxmIOuZb5GOkL3EgdMQ55nFo06c193j6Gyf7uooQ4j8tui0bZrRUDGr1hREcIO4zyqGdcjjePO9WG4buvp7_6iW4mzX-Dk6mgGtpHkpmILLyTszRncx47qaSJ350IwMJBc2GlP-KqgnMxyggiPiZnKovWBhWulqJ-AVJQiPw61MPVDGQXgD1sBZnALh9w5pCnVOi0ubQXLlaczPdU41eYOawQ9e1CtPUNocX3UE9sl0fr2SIfEz-tiDDXrsWme5ggJxC-wXDCW8y9JLpLvL-YAxSndw5DlMSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8ooBAJd1hUM611B5gzzzpo8EsR8sPvGcStzS8bb6E5D6CpaNCT1zv-dyNEtAMgekQS4utT2zi3oFg9TdeSZs-FLQ1wyPiMHD0KfQOrQf9jy2au-05yErw9TTty00CQVeGwwnwhUXg0vCPAi4nTujOPnQbXoOKT_TCuiQWde6IjWO1CDgBXyEs3LhEdd5nSX_epqGo-7hHh4OB1CACaMii8DuoiZJrkuj0fRZ66RvuzQzYJC1TULakkSh16dwE58lVbDvue89shwBCJraiUS38UWTtk_hXpPdadDZO94bWnqb1iLUSSjLrqsGBEhIPbhttla06CAdQmwXuiVif4WBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUR3CpGDFKFgrXCrTo_QPKwIdQ2J0c5kEvBllCXhPA8si8c8gp91Vy3O9PrqKxHP0axlOUAz-U9rKgpP3EXYFfbVmOYX1q1A0lHF-96XDMi-MifijJITc6GznTbc_CEbIy9ImLSXBCk9dbd6eWNNT9GVEwNBpq2tdEF3aDMYcqXm_7G0ihKNx3SwO3SAX8GS1_JhELbQKV0HRrSDJwawBWzCfomD_U0v2H1VDeU4qACRwrz3nGre4AwsyMItgGV_Qh2LD7en9di1UI9AOEE6vQajdcbfOq_kgy0OViXc78EFGnmmalDX9vZwJwlPFwAzMZsJnOxagiTh19Y10qPaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAgauRWje4uQlmnv3Iqc6NkxJEgOl8iO2fW7olrs4-FQUHHG5UNZUmmyTlI5s7n212JKa7mxH9GvXzMMLQba5Hn1gtJ3afs4jUebe1_BxY66j5-oEhgYBvo9z7RKwHXDiSI1f_2t5SW6oYmemqQvgAzk1efnE6Fua99YIpupqdc_fvGOlwZGjm_rYgLNMsuUVVlhcfDOe-qdmsNdq4BzlZxeKztt541ZrA8tNZCmfV6S3ayCLgfCyzrrN0q5hB-jJLAHC1H7s-GUdFlzbrOlFGPqf8y4fodRqnLePjyYe15xFMZ_FVuBUo8wFaUYK_utNwOQqefAL7PPTqS7Y1anyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=IAqOJYz75tgzcpiUtXcbDEQsXjR0dysy0ZQXg-qZPd_JCs3aikNwol3WlvHvDAJnXS-qdFGs7cycCl1uXPvMY_sZOo9F_7ly257sqrx56myEYrpIP67XZOthCJUgQM09llc1zJj-pXrCRFL2FVGTEucREC7X-jsQLAJTBhdJZ0kGHuWHAZ4_u082E0oe-inSL-WPZBbS_yhQJSc1ahPZx4opS_yc0vkjnamVUB2G6_7W6ogHfCnEkmvOkrZKj5UdKSCpeSVxlBxyZiXdJ-U_cKW17oksQrTyxhL414fsSdZ2v4m-CXq_NZOIn83-o9sNMsYWL-pamTaBQUnHy-OmUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=IAqOJYz75tgzcpiUtXcbDEQsXjR0dysy0ZQXg-qZPd_JCs3aikNwol3WlvHvDAJnXS-qdFGs7cycCl1uXPvMY_sZOo9F_7ly257sqrx56myEYrpIP67XZOthCJUgQM09llc1zJj-pXrCRFL2FVGTEucREC7X-jsQLAJTBhdJZ0kGHuWHAZ4_u082E0oe-inSL-WPZBbS_yhQJSc1ahPZx4opS_yc0vkjnamVUB2G6_7W6ogHfCnEkmvOkrZKj5UdKSCpeSVxlBxyZiXdJ-U_cKW17oksQrTyxhL414fsSdZ2v4m-CXq_NZOIn83-o9sNMsYWL-pamTaBQUnHy-OmUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=NvdIDf937yprvWxanWEOxc4Rukfb3ewcIvoc7-nvPOp6l0AnM6ySvOUgQiVOc77QKF6uClRw5pCHKysJKbY28G0YKedjB5GnfNkJzworUaxzqssoEZHr6PFAqL0TD46RTt68F06yDtL8Q_-F4vIxvhxmxxZByWgcXd6u3eLUAs78SjE-GV3BetIIwr61vt9lY_JFkOW1KYZW-2juZZSxY9o4iaOnpVkdsZQa6VlikaxtNQPJDkWDkMw6YIkodIIT_iQiuUzxJCk3u7rNVRsFwZDd_XKlzy4iM-ss2_0DQFwpvSR-XqN2aChyC9um44NGtkP7hdt2L2medUTr7CAF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=NvdIDf937yprvWxanWEOxc4Rukfb3ewcIvoc7-nvPOp6l0AnM6ySvOUgQiVOc77QKF6uClRw5pCHKysJKbY28G0YKedjB5GnfNkJzworUaxzqssoEZHr6PFAqL0TD46RTt68F06yDtL8Q_-F4vIxvhxmxxZByWgcXd6u3eLUAs78SjE-GV3BetIIwr61vt9lY_JFkOW1KYZW-2juZZSxY9o4iaOnpVkdsZQa6VlikaxtNQPJDkWDkMw6YIkodIIT_iQiuUzxJCk3u7rNVRsFwZDd_XKlzy4iM-ss2_0DQFwpvSR-XqN2aChyC9um44NGtkP7hdt2L2medUTr7CAF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcv35kzdGoC0Yo3tZH-WNeoOXAzMnfZRtQ9udfjJpJoLWyZTUqGAgBJgONX5whMykX5USRT-URpoUtIBjjSxdsoMLog_l6p_qGPSToTa9cP9lBlx-xC1542ie7SRu_Yl2EETkEtcSVISaOqliN7buHHIKadmhHMpFzm_zTf2ocYRYHhV9E4VnceER2OPyE3Df3PHeXfS_XdTcIcswnreIM4gXyLGejYHK8cU7JrP1juN0w-M1ubyraTBAb7PEdjecC0Ulx4WGFbq18Sd4KvhBPfOHNIzzv0XaOLzm1o5iAQuvy8VkxXm11JVK4iCQpql_WtYFts8ng1XHxb7CD0npA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجتبی‌جباری اخیرا باقراردادی یکساله سرمربی تیم لیگ یکی شناور سازی قشم شده؛ و بعدش سریع مرتضی‌تبریزی، امین‌قاسمی‌نژاد و داریوش شجاعیان رو با خودش به این‌تیم برده؛ جالبه هر ۳ خرید روزی به عنوان بمب نقل و انتقالاتی به استقلال آمدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27469" target="_blank">📅 18:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq392ZiySFIGgPzU91K1lvdZuUS1E9BR2gZ_lUcNazGb8wtt2A_Hslrgj_SoEn414dCgiqpLbwTM0LQxNZOUuqlZsKid5m4BJ1tgfQw-ALL2XVuyYa3C3rNVNZsRAZBnfX61SX854fX3cvavMGt_7y2Grj-dGItjzofyAH1L2jchdtMUvhpGBjZ72lE60C96tuxn-YUZRqj3pY4WWG7LZtIxakE9D8YkH07CEhjZDFN0kMm2QVV-sbt_TAXOKZ3bn0Bz8uVviX861bRBFuvCSQ63yxJ39r8_fakd8zes5mJQ44wwz-06JlZCgxUaIdoY1jJzaKRHbfEcJu--8Mgm8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🤩
برترین عناوین تاریخ‌فوتبال‌جهان در تصاحب کریس رونالدو و لیونل مسی دو اسطوره تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/27468" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az1aHsLwF8T13YKKXs1vjKJpvMibUz_bVsorM91QlefTlfLeBQI_7wEfLxnsHkuZ3UwEjQ9WgdbiHCfRlnhLAif1pMSQepZUuzSTa6sWJ8OjMoWp22ry5-aQeitSZ3F-uRo305TiyHxAmgDRso4HDminmRd1ZO0o9MF6MhYddE3StWbNGefyW_Agk8LZZjnZ3eJZA6bWk1jTiqX5-ErxuE3AVPR1tMYtJWQkv_gpSMryNC5FGH-EKWfJLqWmitcME4J-OzQ6bpP5g-p_kMHmrhXZ4SGLo228u6DJFl2psRXvWVjtO6Fs7QmYHDc4SFGFTiGi2WOPKBGfV1Kft99p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoL7HBkK3H4ApKyfy3Y1_1Dp7OLaKd0WVRScSvFPrDEEW7_dwXzuMnKVh5WTu4zG12cTgmM7MgN1r_0D0VXYcpc2yQqZIxJsTFkpEVA0cSkQihMnI3Vht9b3sKwNMdXUHZm10dFw_yXZhWPuR-DeSFX3LIhcXRSHo8lMP7mbvlQ5uXImFZmDELDW-LG0kQn12E3xg9xyTnM0bX3fO9cny_wfOKUetbZLUP0Wjq5pL4xQvhOePEew2J-rovihSWY4ahi0p-cA_0sxgXVmXRw0tfYHbiKIc6r-p9aFHxPhRcV2aaa5bcDLa5wbbqiTeuEHXWo-8I_PfRVWRY5C1sejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ObXm_BNL25YPWwiSEg4hLYmpN4BpT3oib6veFiYaypQ8qTshW_FySJY9l2vG61VQdj-PoN-yHjYenm0m81Yc2FpIA-4zGS6-NnvMclU54hZXE1ivowcPX_aJ67ZQHEpbH3GRuSvoRAQStKoZilMFgIWtVrnvuifhmy4JSLMNNrdSdkhzCuM0Xh6xCHD7DXjCwAom1KLcUcFDMJpV--MWRiguaLyJDiwQJ7aA_FJ85fHkBrxqJEWH3UF8KRj4GSpbWcNeHP3YU7k6aiewtHqcnoS_FZDgubfDB0ao5Xrjp3qOUk-YENMafI7dfk_uPw2Q4iSgq6E9G2pXJblWwiUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27465" target="_blank">📅 17:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=nlBF8xyEYw6tGXyKwfPHM0r9iRq2FRlJamK5-HYurchSHJF4xf8GBEBFLjUg-7P9ZpZ5hHHLyund2OjXvMSpyAn6kCP5Yh7evOkCfv2UQOciyCZa76liEnkLQhxDQAPJ5VANoapmGnmg14UMWImKr9hy6xvn0v_ER854xnEXicnsrDcXSD7pRiIQ-eci4dquXgVD_pVpZPyo0q6me76WTV67aPrf7cIEHyo5Hx8VXB93pUNTKp4Y7TTULsv7CJe5trEIboJf4aUPbej2LcUUsBfJLDSEGtdYotBbDVpZE3M2nHdXFYNlWrDRMgDtONCDLn9wnU7STbFQS6IxCd62ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=nlBF8xyEYw6tGXyKwfPHM0r9iRq2FRlJamK5-HYurchSHJF4xf8GBEBFLjUg-7P9ZpZ5hHHLyund2OjXvMSpyAn6kCP5Yh7evOkCfv2UQOciyCZa76liEnkLQhxDQAPJ5VANoapmGnmg14UMWImKr9hy6xvn0v_ER854xnEXicnsrDcXSD7pRiIQ-eci4dquXgVD_pVpZPyo0q6me76WTV67aPrf7cIEHyo5Hx8VXB93pUNTKp4Y7TTULsv7CJe5trEIboJf4aUPbej2LcUUsBfJLDSEGtdYotBbDVpZE3M2nHdXFYNlWrDRMgDtONCDLn9wnU7STbFQS6IxCd62ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توضیحاتی درباره کودتا شبانه بزرگان تراکتور که منجر به برکناری محمد ربیعی و آوردن نکونام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27464" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyJvf0jsbhMiskk-ZsVc7Jzuml-X1wONcS-_6rCm_IwSAgL-M_TTXO1CHGX3JoLtbSmEM3ZskmP4tJkugAgqyoSp2DtYRuzsBuPNQu0nPzda8Dg3VEFZ-MWy9Z5qbmZqswDK2HqUnoz92mw83ENIPKV2ihMB_iMauJm_s-PH4OtGYhpit69GPKhmC5yuvaaaaOTChkKHxJvuZJLz6qBvJg8j6pe1mKAQNBVICNnuHQkSd6FfwgrwqxXsKUtZ2ksdIDiixTlGsp6w6DBuzp7L738IAzcpyNLkL4_g5Kw3LaETfL6PvWE3P5YOJi8fphpg2ol3piYIfr6dZY5gG0T49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پاسخ علیرضا جهانبخش به سوال قیاسی به اینکه در آینده به کدوم تیم استقلال یا پرسپولیس میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27463" target="_blank">📅 16:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV0eFiJ2bxBi-ntJD168JpscDvxebI4lIPcPnHwhF4QW_VCybyfDXzF8idRjTJQmViR_GWLySHyyIK75rCHY4TfdOwtn2OOA1hFOAWpRe4Dzw9luXl181sXwugE7EvcElLTDgiePtPrm4de6-zeA_wOnhiQb_XAfRpYqzffINibqv0JS5xkfp1wHA2Wc8W90eu0-gWIM2gmYOh4t74Q3Qc-C_ICvbdlbXyiDXm8i-HmynO4j3waQlTyCFlGs2ouukYwYK8LW-lVKLQnuNS3lmPrkpu-Wloc4PFGYh2ln56ZJxTtRmC3M1f3pUTyz1Rjo-_z7SKNd3UmtwuxnPdyegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب احتمالی بارسلونا برای فصل جدید رقابت ها در صورت جذب قطعی رودری و خولیان آلوارز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27462" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0q_lRkXAUmIOlq2aXon-r-TbSZWOiTOtY6AA0q7c5MARqWPmIZpJ96MlC7kjkQxaUzzEgTFvJZwDiNrI-kSdixunxWNGR_unyHgvjkjjQci3c81biDFkIF5RnRraSR5yIdehGpj5fewZbM9tx6Xbr_fFFBXSZEEinQm3ClybSHBnil5enBaM7dVHJSjnrwsQ5XdC_DGgJroP6cdSFR3IiSvBdLzXn2ON-IkIMWBkX0G4M2n5hB9voxdJzy438UQLSCiMMvwcZPDhsFX3FFJLav2TAJVo6ytx0n-ITD67iE0dSO4y_papMZG0c-UAX2TwcerUia4iLrqzpu9BAIopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باتاییدیه مایکل کریک؛ مارکوس رشفورد در تیم منچستریونایتد ماندنی‌شد و شماره 14 شیاطین سرخ درفصل آینده رقایت‌ها نیز برتن خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27461" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA5UWy5DQokMQUhLpkRvIIIO1EnR4eW-N2EhK7NktqjPCjgeDHLaBjPQ7dTCVS3KLdzUh0C4HJI7HVz2mPwuzg1llrA07vhbo9-rbGW0iKdYRqTk_qoUJYuoiWQHfNWD_S7u26yuB_KjR3WSRjxF9J3ky-jrRGqLQBVBwpNLHJGFfaki9gzD4bb8RVXO4EtIJBAHurj_YGPCz7G3HGO3PXVgE2TGvdbKSY-mI2rBiHt-freys-7ZP6sG38E1TBNR9rjv-Qu5Nm_kPqboZn70XCaZ4KcnNIi0M6N00M2Jk4L71HoufcVf5_ffizsLfGNGDEUwIWEo2zU5ia5dGmBufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27460" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOaq6jnTJD8syukBk0vCLddJYYqIcOf6HpSr7_BYvf13NPmTpkmFG9epiEtMz3ftrvGqmbP5kkKFmIhJKTv3MSISTcoR5v3NHzPIKeyuYQcZHB9K9IP-bWcxfKi5d4vae_DGCX6-OLQUSFRfaVUqqYy0QRpATnejEAQHmmHRu4y9JR6Wl1Aahz6hb9_sRWuMG_AxaWnNng4nHDWLqbpeIe_iZ9NerhrK5S0ow5s2uGYYNSTorp1P4z3M_0mSVWtmieaG69qZL9e8qTyWVyRQ3BY9KRzhgezjVvfzPmBkIxMQQMHMuNIWVvoUscZx9WDwxH6IM5sxHhkAHC2hUCw-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27459" target="_blank">📅 15:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643163ded4.mp4?token=QZFDzwDWaVqVXkO9wfAgdgxm75YY5WD1Yz6kgxr0yTNNElZE5Ci7pf-bq7ZHBDX0prsgWwNtJxwxZqehMcqdXcUxWyDQYtI5R4N0RqkvqzNx8crhjX6xy7d3OIuGoOx0IGFdJLv4K5Xr8sSDy2HQG4QZq114hq4ea4rOL0jDGvyLwK-94FsZmB8wcGfyzXIXCSisO8NKBPKjA7B2Nzn5aZBcOBtgeGABjcD4d8GUpBmAuzqwhEEkYakhHx5iUVUA5KUMfJ5eInlYHKgfTlaIdVtynHm0X7taPC3ugd3KExBWlPV0Xt520AOAqGE0tBbHj-KVXRUXxmXpsh6-Thl2Zxa9gjjqrvfTHsFh60UfbhL2GHZKmV7j1ghXkVYkUT1II_-dr6jQc9POMndNzHp6ntMz1rEu6C1gyhUqpaFlyTGIwHyEzaKHlC9RtxFx8VZbCaKmwNN_BGmbShAWucwpM6UG-1mOQE_UP3Ml-2Q7cyY3MPwSVNFZwRXXr-cPAfhd_PkJ19N53LBvFqDgr0jaIBiVWWUa7KVtUKRihjyoMp00n_vJstILHrIZkDqx3A9XA-tDDnVi93OMa3zW-JXoe7H3NKfWQcCl4enjA5ZEBL4hFkDBdltKwzAT2ZLKkqt5caqMzyPhLj9hWgtOGYam8zqaNrEpqPe-SzV-rEISIWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643163ded4.mp4?token=QZFDzwDWaVqVXkO9wfAgdgxm75YY5WD1Yz6kgxr0yTNNElZE5Ci7pf-bq7ZHBDX0prsgWwNtJxwxZqehMcqdXcUxWyDQYtI5R4N0RqkvqzNx8crhjX6xy7d3OIuGoOx0IGFdJLv4K5Xr8sSDy2HQG4QZq114hq4ea4rOL0jDGvyLwK-94FsZmB8wcGfyzXIXCSisO8NKBPKjA7B2Nzn5aZBcOBtgeGABjcD4d8GUpBmAuzqwhEEkYakhHx5iUVUA5KUMfJ5eInlYHKgfTlaIdVtynHm0X7taPC3ugd3KExBWlPV0Xt520AOAqGE0tBbHj-KVXRUXxmXpsh6-Thl2Zxa9gjjqrvfTHsFh60UfbhL2GHZKmV7j1ghXkVYkUT1II_-dr6jQc9POMndNzHp6ntMz1rEu6C1gyhUqpaFlyTGIwHyEzaKHlC9RtxFx8VZbCaKmwNN_BGmbShAWucwpM6UG-1mOQE_UP3Ml-2Q7cyY3MPwSVNFZwRXXr-cPAfhd_PkJ19N53LBvFqDgr0jaIBiVWWUa7KVtUKRihjyoMp00n_vJstILHrIZkDqx3A9XA-tDDnVi93OMa3zW-JXoe7H3NKfWQcCl4enjA5ZEBL4hFkDBdltKwzAT2ZLKkqt5caqMzyPhLj9hWgtOGYam8zqaNrEpqPe-SzV-rEISIWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک در یک برنامه دوست‌یابی با حضور ۲۰ دختر شرکت کرد؛ اون در نهایت از بین این ۲۰ نفر، یک‌دخترروانتخاب‌کرد و حسابی ازش خوشش اومد و حتی براش واق واق کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27458" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=e2N6DF_z25esoIM4r-h5DiWwdEtdw4GvsUrQFrj6goI9KrTeREWBgEv-lzpUUtaOTFFAGP2F9l8tvfLjMLFT9eKj7J3yaMqiyOI02RMu4pbiJnMhQN2szk8nsZyBF93rSfOQLyDhrofhUm83orMTPo71NdWRZzDi5vYh4ON4CVd0eM12Qq-940DyIThVTEXYK3J2fOrdWSwyLZeUY8FczUNMcmXAZxr_54w92wZSxH58b4GOdneIJmUm3UaIJexCMkfXSybsdUwhNBwu0jJMct2HFIUviJu1rE4GClY9Tdw0Q_U3SemQoIHYZcS3-tfiQf0suAJsdSYk6BbShS4vdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=e2N6DF_z25esoIM4r-h5DiWwdEtdw4GvsUrQFrj6goI9KrTeREWBgEv-lzpUUtaOTFFAGP2F9l8tvfLjMLFT9eKj7J3yaMqiyOI02RMu4pbiJnMhQN2szk8nsZyBF93rSfOQLyDhrofhUm83orMTPo71NdWRZzDi5vYh4ON4CVd0eM12Qq-940DyIThVTEXYK3J2fOrdWSwyLZeUY8FczUNMcmXAZxr_54w92wZSxH58b4GOdneIJmUm3UaIJexCMkfXSybsdUwhNBwu0jJMct2HFIUviJu1rE4GClY9Tdw0Q_U3SemQoIHYZcS3-tfiQf0suAJsdSYk6BbShS4vdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
«رودریگو دی‌پائول»ستاره‌آرژانتینی در بازی بامداد امروز اینترمیامی‌روی‌یک‌شوت تماشایی موفق به باز کردن دروازه حریف‌شد و به این شکل گلش رو به لیونل مسی و پدر از دست رفته او تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27457" target="_blank">📅 14:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az_fLstgPO2TkkkgkWHY-t5QCudt83dLioKPhgzX-kY7J-9iHAX845AT2JQDwiltmIFdaBfmlw7_ncqgoKMoaX9hMw6jL3i_-Yq1dK1Fut0PP74SZlayCNVAX0nwaMREDSubN1sq5oraVfiT2Nuu4e4Ipd1bfZLawFPe_YQK0Mes0Mk2GBJJMxREFllkO2neeUm2VELYu5oyrN60cse2o64PnCGRO487DF1z0REfq0ejQFoujzqRFYokEtHxyz2eXy2jDxTX1XPUZ_wCRqHL4gJVywmZM9u_Vk_zep1CFU0LVNlQCMYsjlsEbEBsUGmk5E1vGw0vgRbHZVeIoX0W8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
کار انتقال فران تورس به باشگاه پاری سن ژرمن نهایی شده و این باشگاه بزودی با فعال کردن بندفسخ قراردادش از او رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27456" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC15hdUvlbD3iRvfoh_goMFaIYmfdP2s4X6NQ5dg4R2ly0hA6Uydu15jgGfaSceIcY4S18ltMuCKHQCbtk4e6hj5pJEC9SMH7w6X2GstnNLZq6zGZD6R8XkvQl1g0HMASYVBJsf_5EHfqk0MG4dBqv3h_2dLPnpovtwR2tdbAlMXpaI7_zlTq809V2dOeXrl_3xG7g-4PI_LLU2DB2zUvzZt6CFblVq3csvrYC3_pybL03cYKUkpOjk3h715jcNzyJ9WRBGs2Z5MlA9UDdRRNqznJjIikyKY36KwslKGUv2BAe-hgHJPB1HwtIl4PjDBsKFLdIVs3WIZ22QuKH12Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🟡
#تکمیلی #اختصاصی_پرشیانا؛ فردا جلسه‌ای مهم بین مدیران دوباشگاه تراکتور و سپاهان بر سر انتقال آرش رضاوند به‌جمع پرشورها و پیوستن تومیسلاو اشتراکال به سپاهان برگزارخواهدشد. طبق شنیده های پرشیانا این انتقال فردا نهایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27455" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e058bdf5.mp4?token=XPjg2XprJaMARnEAiloYelj531_PNJd8LjNFM6PvkExls7W9VYIjepXqeIZwkvnQZdjX4Qhfoa9drCV5N0qYU4Mp1-iwb7ZSIMHlKojhMnilaMSMek1oO0SIMa0FEBLD1BHgUPIBHl3NAW1mFEpA-zRSFybxqxquwhviXZga6vqSgC_XOF_kKIrrl1k4D9UjYEV6CFl-Br1ULvVA_ceIQQpmebul6dOnhDkjJFgqTg0INmx5-jQbf8_iIxto4LN4gtHZWqkf7MN7zTdEOf9EWwXG5Ms-DPPbJkGo_GQ5A8dshGRT7k7X1oQzfhQM6L1jPMfsPWRMJ7JOt82NlmSN7aQl-8F8Qo_hMb1MRA8P-58c60v07kktpBCytJq8-N_9zpl45_ODHV3cHOrX4JFoQaglZrABoVB7d8V5V4MnO6L4tOqJzO1NTdlElEpiArV74dJAyMQrWg38CWYTAtsxS_su0HrzYN7CfjZQ1PpozpQ2fSMrB2T4bcpx6xhKrth2wFt1zRWnI_zUZ2FbV7eCJfaeBxBEm8_MZ9cF7HhoTiY3axMSVuom4xjkjlUyBZxGTYyNxD56zleKXFCVna1z99fmHGyB-mXosrJlNyNFOPFSbPvnWytdorPMbw-GLce_2DN6dOaTPGcKkLSB4rrDLHIcxGPyDGfF8_Gknkdyl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e058bdf5.mp4?token=XPjg2XprJaMARnEAiloYelj531_PNJd8LjNFM6PvkExls7W9VYIjepXqeIZwkvnQZdjX4Qhfoa9drCV5N0qYU4Mp1-iwb7ZSIMHlKojhMnilaMSMek1oO0SIMa0FEBLD1BHgUPIBHl3NAW1mFEpA-zRSFybxqxquwhviXZga6vqSgC_XOF_kKIrrl1k4D9UjYEV6CFl-Br1ULvVA_ceIQQpmebul6dOnhDkjJFgqTg0INmx5-jQbf8_iIxto4LN4gtHZWqkf7MN7zTdEOf9EWwXG5Ms-DPPbJkGo_GQ5A8dshGRT7k7X1oQzfhQM6L1jPMfsPWRMJ7JOt82NlmSN7aQl-8F8Qo_hMb1MRA8P-58c60v07kktpBCytJq8-N_9zpl45_ODHV3cHOrX4JFoQaglZrABoVB7d8V5V4MnO6L4tOqJzO1NTdlElEpiArV74dJAyMQrWg38CWYTAtsxS_su0HrzYN7CfjZQ1PpozpQ2fSMrB2T4bcpx6xhKrth2wFt1zRWnI_zUZ2FbV7eCJfaeBxBEm8_MZ9cF7HhoTiY3axMSVuom4xjkjlUyBZxGTYyNxD56zleKXFCVna1z99fmHGyB-mXosrJlNyNFOPFSbPvnWytdorPMbw-GLce_2DN6dOaTPGcKkLSB4rrDLHIcxGPyDGfF8_Gknkdyl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27454" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454a762bef.mp4?token=e459AldqJpAKmgEYYh9lVf488sfOnjlkULhvmkbbWjlGakK2i7QFYDY5nDWsb0rtDIraEUrWUJpOPrB872B8_E0O-hGhs7ly4mEpAaKpbNh151AVlsnNmCueLShygu9koBOn0nbEn_7rj1dteoDi0cN3KY0xzm9JwLUfJFLBc1E76EjGfHSG1wW2GvqiogVYGdMjRgXlSW9bkkycZGM16KnbXmHSmSuw57edjdf1AgFtAmiTezo2jrMaaKkcD2_GpmyVOeiswBNch78j0TqiW5GXkH3o8780qqIOVJXm-zsLlRs2BIL7GAwPVSN3oG_0vsuYo95KjKOy4BpGF0BmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454a762bef.mp4?token=e459AldqJpAKmgEYYh9lVf488sfOnjlkULhvmkbbWjlGakK2i7QFYDY5nDWsb0rtDIraEUrWUJpOPrB872B8_E0O-hGhs7ly4mEpAaKpbNh151AVlsnNmCueLShygu9koBOn0nbEn_7rj1dteoDi0cN3KY0xzm9JwLUfJFLBc1E76EjGfHSG1wW2GvqiogVYGdMjRgXlSW9bkkycZGM16KnbXmHSmSuw57edjdf1AgFtAmiTezo2jrMaaKkcD2_GpmyVOeiswBNch78j0TqiW5GXkH3o8780qqIOVJXm-zsLlRs2BIL7GAwPVSN3oG_0vsuYo95KjKOy4BpGF0BmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27453" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERHCM33Oi5l8tR5IiKXFOY_9eE0SQU3QV4wcNQeuk7ZwbRR2453bNA9n-Nn5RRGRYgEtNqFG1e5xSZMc9JflFhQM_uwlEddvD2ZZOO3TwtGITOp1pvT0UQWZh7Ku8OeRaIMfKK2BSCACwIdFY7T7Ch14xRY5YFAIgoiGyVLgp51gnoFgXYZlYWlwEPhS0vpNbQcrwGtrGo2daweHQvPPApPE1xqD6yjgNYWPQ_G2FrfbJPXaf4FhAf8LbcBuj1mo1EZXvTtoB3CS1naiWNlA5Gt0GSp4cE98mumicf1j04ahEv_XlVqS6IM60_Lwwu0lfhN_e-P9KTAsW56xqboww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27452" target="_blank">📅 14:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I17-XYkUn7DdML-EYt9GHvtdzPWtztLV6qX5K-sfLI5tVbFzwnvXxpcWIdamJ5ONDKjoZ54mTld4Jd1d17Kw-Dp_2XPX6NnfeoBiVTskYvFUNVwVlVanTggT1_DcVvUVhCkM4rS2idflA2IKKl8mTzpwwDIxbBvMpXQn9n18AQSTpTfk0oDBq736yMjFhhdpsx9bS4765AdNmVMnsSkw7yaGwPrh-LcQXQCqxc7uyRzMsmNhiKiay_FwG9YGKItA13r2L_pm49PAn_bYRWrJkEb8E8P6ItERA5u6Dc9HaTMWatGwWDyUM4wlL7lxXvDuwC_18PhZKuHqgp8T75veiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ تنهامانع بازگشت مونیر الحدادی به تیم استقلال مخالفت همسرش‌بابت‌جنگ اخیر هست. منیر الحدادی تا حالا سه پیشنهاد رو بدلیل پایین بودن رقم قرارداد رد کرده. در حال حاضر دو پیشنهاد داره یکی از تیم‌های ترکیه‌ای یکی هم بازگشت به استقلال.
🔵
طبق‌صحبتی‌که باایجنت…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27451" target="_blank">📅 13:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSdxeWhB56o5nOp6ytxO3gi-RMQ3HuAJc74crR-pbC9cSdmZ5VEkUuObf8hcBrYWkKhjPOZkyrRmEe5768OKyLzuQtWhjN1jbMACW4jo7UCw5zHBTD2833jXpyeR_qq1CbUBvw1R_Xo_Ftp-5LIcavoI-rpnhGEO9Oeyq23AvaW6sSLwMKEURr1sVfqvW7ht713awR-LuGvXX5tmTZnBBkGXeaM1-tnn4V_ElddD5f1vehJmoDa2pwwYIrnoL2Xo_AY7XlsPcmXG_XmIJXSVuELd2MXQ7i5BgwqOhXWWYKObuR033Lh2Tq04XQr_mtFfY-3zGZLFaOqCBYXL9eZmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها دو روز تا فینال سوپرجام اروپا بین دو تیم پاری سن ژرمن قهرمان لیگ‌قهرمانان‌اروپا
🆚
آستون ویلا قهرمان لیگ اروپا؛ چهارشنبه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27450" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxilFinKChk0ea6j81iVqImI-NI3ZQEVPxA0OIrP8hNIn9AqShPfQTt4n265kut4I3_eDs8JTNhihRGSjbI1IHzVLLtAX0M75mIIm-HYWByO8A5DVhVXLNmikxi8-xPfTQRJf3F-fuNK9gAHVA_TbNsqhubbaYkAOVZYsFTfjts2YvcfOK3_CRz49TaQfSeny_YOufEbxXoN77hK5RTAyH_bFQNB6bvMOCJn_VsswPzy2Z2Fp0cfUrnwqfGLPOLYje9N8JgCYZ24VuELqcpN4KZ7ePowu9QyYvc0GY-2oZwWFESgHbrv_5frlmIW0Jw4dkc9LFO4q3DQwsTkr-jNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
عکس های جدید از مراسم ازدواج مرتضی پورعلی‌گنجی؛ مدافع باتجربه سابق پرسپولیس وارد فصل جدیدی از زندگی‌ اش شد و با برگزاری مراسم ازدواج، «بله» را به‌عشق گفت. همسر پورعلی گنجی اصالتا کرمانشاهی است و گویا پزشک هم هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27449" target="_blank">📅 12:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN22ZNVFqwoaJ8yyQWkDLazCumaZADBPn0623Pgt1hKcWYez-mzQrEuEktJljRb_uZ2ubhUy44UBxrZMtgnvKU8R9y8pb3itTtzTbEy7XS_q4WMg-B8imfWPASKnP8RXm7hra1bFGdHkyY8lulLL-TM3NH7SDGglRHazweCbioihkKcXq4SEHi2b9li8RkbzrJ2is4mfAVVyGC2JPO5cnMB6DpyfSI_b5f5hnr4l5326sQzlSxixG_JI5elx0tPehblEk-UfVgn0YUluW9TMWyJSCq5DKMUX40hIbEFJJJyPAkB4pSyaVG0JL3qV92ciY0ucZM7dNHeyIWGg7fP4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2FlCSsJHNlK3RMqM4RW5GjXAz8Ju4IK65fXflpzmq1IKgzFLxrufvQOtw-CQfO2d2BMjotq5CTfCYxRACzx85KcHFs34n08Ds8wmKZ-3OAIj0dT_IIjtNrdMbdpwgcJ3JAVAaRR8-U3VuTN8HXyBhbys-F5ErY-Op13xl0vZBWPJnad2WQvZoLA1NB3mIGndgGm0hYdlcI1TXEJFX806dP9CAsFC897VKfC2A8guGO9dm_uFK6_oEh0VJy4kUfjeOPOCGzUNYIWV6PYJ6f1f_aHpxE0XyHnAY_qdX8bKq_XVnW1jg2BlvHlDbtxkpsp9XJH_N5H407rzyKyM59lQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لوئیس همیلتون در کنار دوس دخترش؛ حالا مشخص‌شدکه همیلتون چجوری به اوج برگشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27447" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27446">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzcTxbUJlWgboq3rNUhhTOx16EW_m7u5wNSzIsIrsQRClte3n8K2IP2fAHx371oqqiDyan9tP9z__9PetxZwJjswiPcYD6WUOaE5QlePmtxuUiF6zc-E-nn13_wMDwF-t4g9dkqFDO9oRpZJ2AtO5YtVFxPtN8aVDj0J-0UO1piQd-E7j0lj4jqMovYgKtmZTJiJsOLPJ_KH8ujuVGTZMoHU7FezZIJiu1gy4L5gIM5OZ7lr1BvAg81CGHbtLpD1DrBmucgQ4t9KMt3JKb77ayni2jfedgn15M3qSfoDa9L4pn7fxuH8nbojBZQSQMo9EcD2e19evFG3XhY620TkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛جرارد رومرو خبرنگارنزدیک بارسا و از مامورهای FBI: الان ده‌ها دوربین در سطح شهر مادرید رو زیرنظرگرفتم تا بفهمم خولیان آلوارز دقیقا کجاست. یکی از اعضای تیمم هم با استفاده از هوش مصنوعی درحال‌بررسی پلاک‌خودرو جولیان آلوارزه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27446" target="_blank">📅 11:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27445">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrbWNQwbDtsDSfTdyqvrNt3zGhWUq2bNlprpy_eHr5zrQfQuEbgvUVs6VVQ7Dl5FJ3yCOmNywT5DX3UIlacUtjHJeIYg0WpjpEQqqsPlPmAEL02BKI0BHkGmIouFGanhBMVB6U6HbOB3-01ALyK6RYSDJ3FZ4jWAMQu6bqVBE1IcIZkff4pe9z8xCdKc7qKRyGqz19REN2jdmzHEyb65x1dZnnNfAWPcfZ1xJXtX6ILXwIa7Mdhaj4bT1jxOawLJkDRPTIuMQfxhhtG5cmvY8H7vhnrBkI6ZV82ozmp2nwapHJ-pqwtydeG2i9YrQ80h_lg79EIPbttz5kjdiqPpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دوباشگاه‌پرسپولیس‌وتراکتور توافق کردند که محمدقربانی راهی تراکتور شود و محمد مهدی محبی نیزپرسپولیسی‌شود. حالا باشگاه تراکتور هم بزودی از محمد قربانی خرید جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27445" target="_blank">📅 11:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27444">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG4eo_bKfYvaHKjEM0UkTcSfEQ3OBc7jorwjBE9LAXsAJZCU--uGMkWowFNFu61WjOtm1FCYrp9aAHH5U08sCFnrCORKzpHrqpk-xnDK0lmhAgwUdLijMJpW0w7ZP7kdgEOTmdguPXRcrXonlVUkftYeRd2FpU-5RBXmyFmCs2IqMZSCoBaVGBuwdZevynlz6oDgo5LgTPSqPYp6VdmrXjMWkRqOG279XBN1vXX7RC1oO_KMW_N6345fh2LJF-rEeOC6xgj_0ZZJsqKeAionw6wcAeiUaR23CGuW3Vg1YySFyKZ4cB6PCmncVf-ZhwnyEp4hZlnKTBchLGFO8tScog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27444" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27443">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_hiJywWzp3dnTIh4wQLJVVRP8ThMrBGKGAmV1--M_Vn5k41VyxW34AxftBxMIeWfezmwT1iyzFMYpHGBy4KDmQGJpbD0UVKkzdbm1L0Cm21ADktom5EvLNBYGb44PF_ufbRz219aHkvV7Bz5KfzAqhLGbs6zAI56Xg44N1Y62dnGn7cKzHk-pmvRRiDc1q1P-Z3DUGYstqQOclCqIZgIBRtj5S4edY-ZxZ9xKPnqM6ikbqx-uAPU-mIPKxSCLgfH9LQB0ugYJgvJcbJogRtgIm7fU0M3HpMUYE8MAkUZJo3lNMChg75JjZsIeXl4Xvl8JZuJCnPz_3fcAyKbMFSbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27443" target="_blank">📅 10:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27442">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuiW5i_tJ7L98z0kYKidNY9XbtansARQBIhznCxHuW2geo_PM1-NRiM54dv3qS06k44xm9GWw9XtkB13P30lW9RJZ632_83q0tSaKtcuPd2GYidM00gQWSzUIqUZ-EyL65FeVOZWLvlbXTwDIccPBTuBDmV2DRNuezuVQqpzA7csfO3YePsiH-gTMBfFZxvmVd1AB6QtymtThgnHjCnPBcwU6MX_WwppYRICoWfD56libmRk5EU9QISv_8FuqJX5nt4LAXfsvh5hxheg7s7ibsQM2w9th31B1WYxmDXqvGAgwy31XNnm8TQtx3kDxWH3A8C9NaFIw_ac4jipvVTO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست بازیکنان المپیاکوس برای دیدار با نایمخن هلند درپلی‌آف UCL؛ مهدی طارمی بازم خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27442" target="_blank">📅 10:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27441">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=ULrlPOvgN2kjT3HsK-xMdED9U18yyMTaPRcgJn-xBTrBGtYYVbAhWSHFAz6G9M-rVuXX3T3qYH7k0O45FVkYnkqsrtjuZnd9tPluG8w7KIb8JWn8F4KGKttui64lVugULT9o8xTgsm_SmTC1cDRKaZX8KZa_4jncs5rQw3kcNG8zJZDAMUucAM8GzjRghwLjRkCiY5kOLbhZAq0Ak_HiPTrc6xn16DlN2N0zZvtZ8gyBFDov9BwhRrAEfU63qs8cqxFNpFLUI8O6QzAlJH1pdtXn5QkY7Bd6QJwaqSm0G_3GqIh2_eHVetb8FY3i5uWSfSJJeR7712d4JW0p6kAk6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83727b1e8.mp4?token=ULrlPOvgN2kjT3HsK-xMdED9U18yyMTaPRcgJn-xBTrBGtYYVbAhWSHFAz6G9M-rVuXX3T3qYH7k0O45FVkYnkqsrtjuZnd9tPluG8w7KIb8JWn8F4KGKttui64lVugULT9o8xTgsm_SmTC1cDRKaZX8KZa_4jncs5rQw3kcNG8zJZDAMUucAM8GzjRghwLjRkCiY5kOLbhZAq0Ak_HiPTrc6xn16DlN2N0zZvtZ8gyBFDov9BwhRrAEfU63qs8cqxFNpFLUI8O6QzAlJH1pdtXn5QkY7Bd6QJwaqSm0G_3GqIh2_eHVetb8FY3i5uWSfSJJeR7712d4JW0p6kAk6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ علت اینکه یه عده میان فحش میدن و گارد میگیرن نمیدونم‌واقعا. تو خبر گفتیم بانک شهر و باشگاه‌پرسپولیس گفته ماحاضریم این دومیلیون دلار رو بدیم. همین. هرباشگاهی‌حق داره به هربازیکنی که دوست داره آفربده. دیگه‌بایدمنتظر پاسخ حسین نژاد باشیم ولی میدونیم…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27441" target="_blank">📅 10:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27440">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=rF_BarisIulqOA139rBHsm1Md8izNl5FFPpykiNIMF-Oi59lbPf__7eJhl2B4BE5Od7lPaBnj-GXSD2XbZKmfTwI0SSlb48lHMyehRY4FenUA64VrtqWqSYPnYjh8GpRuIknhsNvuFnFxf4L0ltgLTDKzvhvcWgJIXS4SJ0Up0gvDQAkwjfuyD95mr5_vSuH21XFJoPT_uCnivcQB443YbJVKGRxBM4eYspePSLj_0u72chtBtAEB_I99jrAY3so4LxuBd77IIOvAkfe9YFgOSrlvgManofTNBqWU5gv3hANh7QitXQtELgrrLQ457U9zfw7oyBTf01UWGW7djUGVLEl9yIYL2wEMFFzbMwczXMqt1eIKs6tiF-Jp0W0ILEMnw6QAJan5K7ZCGNTTpSdyzyv4CzKL4WQL3C95ZRDTsz7w42XDwXczYAx4QLpk-lorf9OdxAKGqDr28wOO_PN3mliSqQnXVyjRxViC2z-Y8wDXK5D7VOKGv9BqTACWFvftX5Lj_5GgENKyeOzWLhJtrSOgRnLrL-47Z5c1hz2TXja9wTNJ3cT7aAiZacU-6S8O7Riqk262j8WeK4Sd11vxEw2FlvryroIXE3dhUuwM-oPAdHCSMmzkQXd21A31pfpkdcfh-Llb6Yw3Zgeo8TMolb6-AsANlZSxjo63Nm6too" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65599dd5ce.mp4?token=rF_BarisIulqOA139rBHsm1Md8izNl5FFPpykiNIMF-Oi59lbPf__7eJhl2B4BE5Od7lPaBnj-GXSD2XbZKmfTwI0SSlb48lHMyehRY4FenUA64VrtqWqSYPnYjh8GpRuIknhsNvuFnFxf4L0ltgLTDKzvhvcWgJIXS4SJ0Up0gvDQAkwjfuyD95mr5_vSuH21XFJoPT_uCnivcQB443YbJVKGRxBM4eYspePSLj_0u72chtBtAEB_I99jrAY3so4LxuBd77IIOvAkfe9YFgOSrlvgManofTNBqWU5gv3hANh7QitXQtELgrrLQ457U9zfw7oyBTf01UWGW7djUGVLEl9yIYL2wEMFFzbMwczXMqt1eIKs6tiF-Jp0W0ILEMnw6QAJan5K7ZCGNTTpSdyzyv4CzKL4WQL3C95ZRDTsz7w42XDwXczYAx4QLpk-lorf9OdxAKGqDr28wOO_PN3mliSqQnXVyjRxViC2z-Y8wDXK5D7VOKGv9BqTACWFvftX5Lj_5GgENKyeOzWLhJtrSOgRnLrL-47Z5c1hz2TXja9wTNJ3cT7aAiZacU-6S8O7Riqk262j8WeK4Sd11vxEw2FlvryroIXE3dhUuwM-oPAdHCSMmzkQXd21A31pfpkdcfh-Llb6Yw3Zgeo8TMolb6-AsANlZSxjo63Nm6too" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27440" target="_blank">📅 09:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27439">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs5WM1pQ6W64M-D-YL26kazG0ilYfeb73TyMPTfpWRSeozVUKN4p5HXv_ffGJM0KeaYcjeJCJyair1uAD1bvSsGdVWZhtAwLrcQxvNh_RFsnmfHI6Q5V7jW0EgC896xwNcPosx3FKhbviSTSzHvGWeAMUh1kOkPE80kCHGrcs1KFjdfFRR9UGbTGR9YTcBzG8SnrKw6vpq2aYeJKFpiY0vbY_cFF8B33CSsgimm_Q3UYMeQYuqUepmCLE2OeHbuDOQzi91uyQ8wapfaZD0Hj7MtMW83VlxhnYe65ymfnBnB1U8q7X2YQBSd2WN49IbzZuYU1Lzc735zFPElZ2ksN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شنیده‌ میشه باشگاه سپاهان در روزهای اخیر مذاکراتی‌ باخوزه‌مورایس‌ سرمربی‌پرتغالی سابق خود داشته که بامخالفت‌همسر ایرانی‌‌اش برای بازگشت به اصفهان این مذاکرات بی نتیجه ماند. مورایس بعد از جدایی‌سپاهان نتایج‌خیره‌کننده‌ای با الوحده درلیگ و آسیا داشت که با…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27439" target="_blank">📅 09:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27438">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxyyX2hWQvuhw5GX0KSz_CweQpSRuOlrlujHEiYnNVme8WA0xWaDR5qIJRKBokpfXZ2I36Pw40Cy08ch807kHOiHvEev53c-r5XWciR8oJLizK8Z56UPLVU-LiHHjf7iwv8QJZ8kYDH4Gh1jTs4VNCHDUFsMUmDnVfWaQDh_kMRQNz9V5gyIkK35T-4tmLOhJZY_0zgTjoTSnuNaFe6nUmjiiov4gcMFyIkLlJOAQU4LHbsfaTKlSFr-FjlV9rjp5WXHmM4LQK2o_z7ceZj92IxPxcbxuOF5N2DvZI9tGWjsQp-I_Jl-SscEbCR-7prBzSYpmEcxrUGxxs07zI3UrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل
دی‌ماریا:
اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27438" target="_blank">📅 09:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27437">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu0kC24pZ_xmpy9-_W14G5mBV4Z4iDcL57t4TSqgFxeZoYCn-COzdt6Bat2tiwPfTnljZM-QxUO3oZ_DhcQ4Vkt7dhceSXRx0N-1B4s5xu9IYw6ZlvG4iRrMI0kHH0FFdrkIIx7pB8ky6xVYQMuoXtl2yFheKtQquTToWZst5ikTUKTHEoYM2XgtSTRvyBuDGi6cQtTUFJrnzh1Zkt0DvI8zp0fP7xxrigwLQauTDgX5fE2jC92hxdP0Fxu_v7AFLEJZXMcbEBAJAf1HB9qMex_h1cT6T6oi26uw-GobR1jFq0lvk1vudop6ZvOOOHHdHllBDnvofcYNGzrkP5nACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فنرباغچه به درخواست اسماعیل کارتال سریعا میسون گرینوود وینگر سابق‌ باشگاه منچستریونایتد رو به خدمت گرفت. از فرشاد احمد زاده به میسون گرینوود رسیدن اگه پیشرفت نیست پس چیه؟!:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27437" target="_blank">📅 01:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27436">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7E1BkaPuxdNVO6J2Zu6nbpYGyKE8sQqaYt_J7_rR72oBuA0p1wPxl5thPsbjhl-OLsj7smBbogYyPQKhsPxYA5LuWI02LwoLfey7YN1Zh1UFqgqgq14uaQgHXUA2ueKnQn1GFeZviY6Oa-KcHbnd9-lnc6JouPnRNF_y2qJSHtA2COE7gSuyJZ6Rbjdx3huxYh0m_fzVC6x75BHwDShUMvHZSEUthqXYkPvKPM5pgbe2eYcjzZMwnh2C6jqnnzkAIJhv6jfS4UZOP8jXHsX2yh8iid9RRL4pJHnSE2HjZgxb2m0E9d3VrFnp8nw1RZTkjFTTPFahPcwyjbnbyrI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر ایرانی خوزه‌مورایس‌پرتغالی اعلام کرد که بزودی‌ موزیک‌ جدید او منتشر خواهد شد. یه‌ بخشی ازویدیوش رو درکانال دوم گذاشتیم! دوست داشتین اونجا هم‌داشته‌باشید محتوای جذابی توش میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27436" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27435">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=E4lNEbA4zgIaf516RErtRVQwbMxdq7lKqJ9ukgTzodYINmp-j70mtpNFtu9_UyYBc3cN3eGnfk6ZGVljbaBLMdZMQ4TrJe2PtZBgt30cgnQE3M3vzIqko8L_V1uVs8TGh7fpsFwwYapJikYqwY4uh6ALVBHMGR2x3Zi47rSzvbcqKxZb7BzTSghDV_nxriCxqIUgxlYEipVXz_uNs5WYLB5XhZlIt73vC6ukT8PzjTlF_8uCbLX2BvXjBf3bSn78lKH-L1FuA7nwnfyW-JkPAnKhPldmovQF5gU98iAjHnCHNnpryXT5WRLGyyf341h0oEcwycP7kDgQDVJckXa3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da4d4aa52.mp4?token=E4lNEbA4zgIaf516RErtRVQwbMxdq7lKqJ9ukgTzodYINmp-j70mtpNFtu9_UyYBc3cN3eGnfk6ZGVljbaBLMdZMQ4TrJe2PtZBgt30cgnQE3M3vzIqko8L_V1uVs8TGh7fpsFwwYapJikYqwY4uh6ALVBHMGR2x3Zi47rSzvbcqKxZb7BzTSghDV_nxriCxqIUgxlYEipVXz_uNs5WYLB5XhZlIt73vC6ukT8PzjTlF_8uCbLX2BvXjBf3bSn78lKH-L1FuA7nwnfyW-JkPAnKhPldmovQF5gU98iAjHnCHNnpryXT5WRLGyyf341h0oEcwycP7kDgQDVJckXa3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی که اخیرا به لیگ دو روسیه رفت تو بازی این هفته‌تیمش به این شکل با پرتاب دست توپ رو گذاشت رو سر هم‌تیمی‌اش تا دروازه رو باز کنه‌. خنده های گزارشگر رو ببینید که برگاش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27435" target="_blank">📅 00:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bftECZx9XCroodJmiWIiEeQ9TmmMZB7yKy1Pk9oYulyRcquWPsJ_quw4uqWLeOYDLhYrJZ27XwHZ84bJumh9l_94gQcmS5JE8zYRCtY7tWD3FdWzKwqf1Js-5r5fxR-c_dkU0UYG-tO0H0O_dpa_BytMCV8_4Qok7WTlNjr9T_hNrgy1EhYafMKmDTy9PqRA0OvsQ6vLbzsHo9jMv2vchJe9qZHvImnspeyf8-2ZKPo_onxkybcgQhNfcxM70Y5X6rSHkE9ntfXBKln7DNBBRn8x3WxnRQxrW1Rle3DMaRVEQZlX0pzgp37MJl4nyv487qbXOux_DeA1a_YRaf3jiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌از باخت عجیب آرسنالی‌ها در امارات‌ کاپ تا گلزنی اللهیار بعنوان یار تعویضی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27434" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKK6OgRf69_jSbkS8_qjGzlN45Me8fezDBdQBEPBb_Yza5RXhsc-EVdPMWFxfMMF4U_OqNH0qq3ScJlbjgJbuvGZY5Be0CJZAgj7ikgPUWRx7sDHNVRV0N2Nm5bLwA6j_REX-I3ODDMWSB5Qlrtg5r6z8nh_wWAV4t5kVPkzh2jY598Mdc-q_i1O_MeJsg_wcAfZgs_UXZBCwKSmjhq89Jros6VaMXmb5_khLwP9V9-nGZK9Lv1WoUqCbguBx1F9II0d6YTTXP-yX_wxoNtBZYZIJdAvgWhlZNUU7nq-z1MCfVdcNz-TYBQLTxmROs4uiW7mWWVN7NLug8VAQ9PRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وینی‌به‌رکوردرونالدو رسید؛وینیسیوس جونیور درفصل‌جدید نهمین سال‌حضورش در رئال مادرید را آغاز خواهدکرد و از این نظر با رونالدو برابری میکند. رونالدو ازسال ۲۰۰۹ تا ۲۰۱۸، ۹ فصل برای رئال مادرید بازی کرد. وینیسیوس که‌ازسال ۲۰۱۸ به رئال پیوست، حالا وارد نهمین‌فصل‌حضورش‌دراین…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27433" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27431">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saZTI8ZhrjYWnr04tmJqr8lMC0XGJBBhcZzlZWogwgzAxfvKtly3vcX1uEYB-RqO6E_DbWG5bLQHfacHPAqFrZxX_lmv96ruk9w0loc9MfO92rbTSa9SZNd5hPBZWJyLM1R5XMsOqoS50GdECUPyZJTJVez883nOQgLWdjQR0p-26eN3M3X33rq7jPhj4mHneFYV_EkpwGejuZOK5F8u4TqGJVbonyU8CDmenbQ6Dd5zJLhX9zab27Kq-akV1Q02OwWUERGWaIYXGYFiPZMBlOYXoSwl6N9koGKH-bdwW5qldAQC5HkBOXYNOGY-C2U23BpsEy0SFJeeJNdAlVP5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
گاستون آیدول منبع معتبر: بارسا میخواد آفرش برای آلوارز به‌120میلیون‌یورو برساند. بازیکن هیچ علاقه‌ای برای بازی دوباره در تیم اتلتیکومادرید ندارد.  هنوزشانس‌خوبی برای این انتقال وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27431" target="_blank">📅 00:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27430">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6LRNAuesC80n55NA_T8Rirl-0uEY_1nLv-1zsbt1G1orbqKRFf71RgIelgwLoKtP82v69OcKPQyd0PmVnLuxdoRtunllVhIjqbEXhOIPOjAY09PcRhWxjHRXgx4nF3YQJW5AeK_y5bQeU5AwaZE1xJeYE0FrZnS_X2w_uXGRW6Mw-krKTAyfPuhxZILKfzXP5jEqeto1ULtOC64PeyMEugBb9nBDn8KtXnhIcl2U2zp5zMezLVqi5N5FwdDPJFwnUM-6-U4zc8KgO0dD-SPAOatKyYfAsHFf8i-4dYzDIOZzvtCih3c1jxfLhZ31C045H4zKP00QKKi68uyQB1k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید: حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27430" target="_blank">📅 00:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVu3dLJSmGMKEDrl5ATwccy9z1i7xDfPrpjaomMcPtZWROVcgynL4unyKkSzmKoELdHdlUIyzX4jLIH4H6bUugkhdnR_PaegjIBIYjobM_sgXdaHUK_5ykDvgC3q0dKv6qedEpnp_4Z7f8zBmRgPHHDNOpJAIBgGHq7aBbpQtQ0qqPjcGGsr3xk571NX8MRMFP6KjKsJ5LGKzjb71CCvDKENrAVtHDomepLi1xtZ25UiWUGttErMQOMdD08cIU16TGPW0nwyUodurvPJTpbsXD4Fjehdf3AFhMyPsbK9L5sB9BP3kBJJcQ1drRF39HY7fm57pOc4ySvtTzDgHDG5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آاس:
براساس‌اسناد داخلی‌پلیس، لیونل مسی در جریان جام‌جهانی ۲۰۲۶ باچند تهدید جدی مواجه شد؛ دریکی‌از خطرناک‌ترین موارد، فردی تهدید کرده بود با مواد منفجره وارد ورزشگاه‌شود و به مسی حمله کند. این تهدید به حدی جدی گرفته شد که نیروهای خنثی‌ سازی بمب و سگ‌ های پلیس برای بازرسی ورزشگاه اعزام شدند که خوشبختانه اتفاقی بدی هم نیفتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27429" target="_blank">📅 23:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27428">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhotYkKrOGD5wz_1J_IxofZLYG4OvEgX7NKHnfWl5N4sIIzf_NU_Ij5gmwMJlUEqKDnRDDBg0-sBqk9l0HzkaxDXtE9gsW_pITheZPEIoyRh284oSDGOKe0JXxzLCNsYj9Ymx7GuaW0VN75VoHQ4tNHDSQCZF4I5kgF5Bmkv_53WRgoJg6qawyzr3h9lIe_1A9jxJgygAH-ytygh7jK1F5En8zQX_InmaPHQBL2A2T-ZeZlQEJaitSh9M2JhikhViQ-ZkxiXA9lhRXudyWStWz59ex9_J6JD7gsf5JX3vHkW0QGBK4CyIfeCzrx2xWnQT3B2dLXGyrWVYwr7sYsqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ باشگاه سپاهان ظرف روزهای آینده از بین‌ حسین‌ابرقویی و یاسین جرجانی دومدافع میانی فصل گذشته پرسپولیس و آلومینیوم یکی رو جذب خواهد کرد. یک مهاجم هدف نیز جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27428" target="_blank">📅 23:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27427">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19eee8d27.mp4?token=DdMPLi2_2VxgXOJVnDGUmLuk0UYih5f4i2_wqbZlAZNbRtEzINBt94ujmX9kyAlbull7D7kDoZL_4B8wxwTIp3ot3i7n2UGqeHylH83kUaeOH2Z3GeQPM-nlqXYJbOd8c0A59YKkBGFD1Rb9XNSDqzCmMOt4nauxkQPp0kR8tp_dRcjeu9cA1Cza2uDrRJsug6-nejdBs0iTwhB-XlHgAWm_5T14TCg-hRENV8DbgUPYnEZPgZbSNqfN1u5pZqHuPetorIgYUji-qHUn3efnmbkZZt7xflfufB9m1x7hl3yljSevrK9xWla9779psK4FWMqIc7jN4CRZuOgR29M5kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19eee8d27.mp4?token=DdMPLi2_2VxgXOJVnDGUmLuk0UYih5f4i2_wqbZlAZNbRtEzINBt94ujmX9kyAlbull7D7kDoZL_4B8wxwTIp3ot3i7n2UGqeHylH83kUaeOH2Z3GeQPM-nlqXYJbOd8c0A59YKkBGFD1Rb9XNSDqzCmMOt4nauxkQPp0kR8tp_dRcjeu9cA1Cza2uDrRJsug6-nejdBs0iTwhB-XlHgAWm_5T14TCg-hRENV8DbgUPYnEZPgZbSNqfN1u5pZqHuPetorIgYUji-qHUn3efnmbkZZt7xflfufB9m1x7hl3yljSevrK9xWla9779psK4FWMqIc7jN4CRZuOgR29M5kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شایعه‌امروزازدواج‌رونالدو و جورجینا باعث شد هزاران نفر مقابل یک مراسم‌عروسی در پرتغال جمع شوند، اماباورود عروس و داماد مشخص‌شد مراسم برای یک‌زوج‌معمولی است! کریستیانو رونالدو هم با انتشار استیکر خنده به این ماجرا واکنش نشان داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27427" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4UzXK7PyCUSVDtKBvJBeG5Gl2B8N5XU3fFWlD2gw1Md-0hYwtS_pieNXRKT9ULKXtePg44bx_nTMR9pUyy9012bG7EQ1-I1W-aTJ2nkAkUywPjotKXxTALmXrrmbtrcTEf59y2YnHch7d7iX4nM_AQaoGBy7J_VkjoUY0-YcbBs0PbXJo5GxU2vVqymPm5VnYp_PnEnYBZqM90n1htuyZ-6cOFc7G1RGcCoogcIesri_1btUx-QOTmEbSBuFvZwgand3sIJ0pJr4p1bN-Z_mIrKKRK_Wj9W4fXEnxLmOkM5ykd0e8qjrdhMq53xOrK7Q1Xn_49vZ0ekmsW1if4Xwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27426" target="_blank">📅 23:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2YvPhTo8afRpE8npfhBPHfalKX1luBzybckVxW15lfwNzbtw5uc5ZvWcpYFJPFZR4Uc_Ii_YzuxiXtGTxRDI731marMEWBHBjbJhK2-G_QFvz9UjqwpIQojbgJSeoDRFheULQ0xqoiOIqwrsGD5wUnVlF3rV8rI8R0uNDOvwJN-btcDBeGPVoA7EmDTWsnQkzDbQLIzQtP1BVNhCSQJdKe4tgWJcZO5V1uHvkVeXIEFrGLzOkYHg9E3JD5n8_w0FQTZgM9gfcJmSxf9oAOA2kyoxCOBzVN_U4pxJdZhpdW7JV4FnzJAdIstMliBNkrNNqWKJyhVr0KVJeNXY0-Z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27425" target="_blank">📅 23:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlqkySzd_sPdFgXqUe_CA7oObIl-NFXM9tbgYmWNZdHB3DcJghlypAGGyAFGS_ZEXh-d0RMd7TY2T0_zBWM7AvG-XzPqkvOfFZPtpjuWe_QA8YP8Lw8U2U-1h5gEeip_mFrfa1MqBrqQtugEI9I196aD17xoqWxFtgmt6IWWBMEKVl7H9ahXJiOQRcT03f4kE_8NwYyS7nhPOOhyA5Flvg6NOnstC7oWhofsWi7Oa43DKnO9kogbXx86rgi05UlFylyo-K072ng4Q1TA7WYce2j7emvpwCwxZ8AfmySj_QEJpDk1bKMw6XJo8RdocH4VRiES3QhoKLGmvivotOxAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری از موندو: سران دو باشگاه منچستر سیتی و بارسلونا بر سر انتقال رودری به نیوکمپ به توافق رسیده اند و این انتقال بزودی نهایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27424" target="_blank">📅 22:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKqzY25r5v4y8eBycda6TjdWcmqCClhE8_aeXI-2NA4504eh3mtGuMOCvSDtlp734Kp-oshpL9jiTwaVBSekDUTIGq4jHUzdXVAINoPQWyETGZC-_PMZ8NtuU8snniIoh0NGeRX7qy3EVLnQebyv5jq8sDHYI67840gOdEOUh-Ds30bz0sop6Y17svdYmgpZ-X4xGfHwY-JmkyzqJ0n3jShja2ffzKCdHzYDSq-HBOBW2APfEPz4GExubUODhW27WenKxKDZT6EEFD2zbKUcClQl6EHHMWN0OjkbT7F-2fPQDVWqZWcBXrkn54JrGiJw3AqChSuQfVN0W3RRfp_Kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
اسکای اسپورت: باشگاه بارسلونا بزودی 55 میلیون‌یورو به‌باشگاه‌منچسترسیتی پرداخت‌میکنه و انتقال رودری به‌جمع‌شاگردان فلیک رو نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27423" target="_blank">📅 22:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27421">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=FIf0sB_RQLxQdj9a9Gj_C1nyjMqPyitGkv--nWvJ9FG7KjKLA6eHMn8ZmQ1yAnK6cbWUjElcH1dqSIhuQz8rR_IuwrsNPLBjeAjlL7bfG50CymvIuq77JGYWJYsMkO-ZDJZQ_aKnTej__q8DUrML175U4SCjALweZFGnzRe2jlNfFXmx2PQ3qg2QVr4JWY4uYsJbPCk28EetyL3dDfpJ6OIUGnHVLp5YdwIoJHxIhQsmiKaQyeUZ_7VFYDu1Ln6Pxh5Y-ek5N4p2j3GY3f4lw8ybVSrY131-pZuLO91NBKY997KvQ6Fpe-AztB7hJBryOTjVbGzskHhEHOiq1LE93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=FIf0sB_RQLxQdj9a9Gj_C1nyjMqPyitGkv--nWvJ9FG7KjKLA6eHMn8ZmQ1yAnK6cbWUjElcH1dqSIhuQz8rR_IuwrsNPLBjeAjlL7bfG50CymvIuq77JGYWJYsMkO-ZDJZQ_aKnTej__q8DUrML175U4SCjALweZFGnzRe2jlNfFXmx2PQ3qg2QVr4JWY4uYsJbPCk28EetyL3dDfpJ6OIUGnHVLp5YdwIoJHxIhQsmiKaQyeUZ_7VFYDu1Ln6Pxh5Y-ek5N4p2j3GY3f4lw8ybVSrY131-pZuLO91NBKY997KvQ6Fpe-AztB7hJBryOTjVbGzskHhEHOiq1LE93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امشب دربرنامه تلویزیونی خود از کوروش اژدها کش و امیرحسین طاهری دو خرید جدید سرخپوشان رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27421" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27420">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=JtWRSi9Z2vUj_UMCu89Nf8cjrDxW0QJzRBK-sMqHmqiLwWtKVknFzlBdVo7YHM94uoZYbS2YJUUxqZsN386_Pkqu2nLD1uXi1Wp_iVI2KmMci1OjCtZb7LjQ-VXPra1JNyAbZP0Szsw_6WA5-8KbSxavmjcb6YvO696FL4EG2BOsniWgstxvQzecG1DycT9YJglKFFbNpZfLyCSJ0SnQn3q4HcaFPE4eM0E01MGGVDGkAvuPwBy1XrYH3XOgIAO3XqjUSxP3jhcgJWcrHDaXSDyXTZenIRXZChLWvlM9qYjb7_OdM3CRQB41M6Zh0VjISjejhGjqHiSCcieGeZKSJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=JtWRSi9Z2vUj_UMCu89Nf8cjrDxW0QJzRBK-sMqHmqiLwWtKVknFzlBdVo7YHM94uoZYbS2YJUUxqZsN386_Pkqu2nLD1uXi1Wp_iVI2KmMci1OjCtZb7LjQ-VXPra1JNyAbZP0Szsw_6WA5-8KbSxavmjcb6YvO696FL4EG2BOsniWgstxvQzecG1DycT9YJglKFFbNpZfLyCSJ0SnQn3q4HcaFPE4eM0E01MGGVDGkAvuPwBy1XrYH3XOgIAO3XqjUSxP3jhcgJWcrHDaXSDyXTZenIRXZChLWvlM9qYjb7_OdM3CRQB41M6Zh0VjISjejhGjqHiSCcieGeZKSJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مرتضی پورعلی گنجی مدافع سابق پرسپولیس هم به این شکل مراسم عروسی‌اش رو برگزار کرد. همسر مرتضی کرمانشاهی و پزشک هست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27420" target="_blank">📅 21:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27419">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=jQ2ZRvl3hORi9aC2vIPo2O_h5xEVrKmKOfVDpymerlvtYDFqdemkHAOoS2KHLOgvl59oaaqikVtwwhLuTo728Ccmu_U6qFEFSypyaiMWAG5dOlHgEH7B5WJCGD-8jPtbOH429caERozdwoNLwaIiFV53bQ6-2OR1mi5ZeyAnzdUV3Xzbr8GjfiITFB4s9fMD5SclVQYJDyjlAXHeNsHCd9uEWak6I-Np1ov1c1ikF9BhDCWpQr3b6PNX-iY_KvVXRqwMt8UVY7sVKs522wmHLk8FBGhHcESQjrhJsnf6TrW5xo6DhR-pcdkOKbFNkj03v5QehnisSB1b6W8lgNi0-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=jQ2ZRvl3hORi9aC2vIPo2O_h5xEVrKmKOfVDpymerlvtYDFqdemkHAOoS2KHLOgvl59oaaqikVtwwhLuTo728Ccmu_U6qFEFSypyaiMWAG5dOlHgEH7B5WJCGD-8jPtbOH429caERozdwoNLwaIiFV53bQ6-2OR1mi5ZeyAnzdUV3Xzbr8GjfiITFB4s9fMD5SclVQYJDyjlAXHeNsHCd9uEWak6I-Np1ov1c1ikF9BhDCWpQr3b6PNX-iY_KvVXRqwMt8UVY7sVKs522wmHLk8FBGhHcESQjrhJsnf6TrW5xo6DhR-pcdkOKbFNkj03v5QehnisSB1b6W8lgNi0-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27419" target="_blank">📅 21:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27418">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8_Kz5uCH-el3SMI-b-XitcmZdW6V_TgAwnMmqQiBiT9S0lws4om_A3A7_Insb1CHH-j3pMG1CFiKFsuQmjTblDNGla0t0oOxqQNyUtEf3QYqjYC-6W2pyTJumUQAsi6LMTN2uPVaR8XtTAvgRdhVbm5JkU-TD8kSroVdmmrK9Soo5mo3dzvGT1MKr_aiB-37_yX8SLSrtT2AazIKzhZ_9em7C7IZE3yIX5VkpyDCVAN2HrrzDVeS6JejLCb1e6-srUPv8bUJ5seHyQu1hbZW1Q5XYmnxhPFB-hR4PIxmUp0PVihsq5l5_j3msqtInxw1XYp35R9lW_joxsvxOJbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27418" target="_blank">📅 21:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0g4GqLwKAiLCXL7mwbLfCvDnD57p43NlVRmo1UM14A0d6I-uPRBoXcZBNQp1qFR3LhdC3T-wjjMlfBl5aAA_m_fGdu13UGBTp1tcQcNOj_zcLfyyCCzc0MC_ekTFB8LhgYe-xoDtMCuxIoweUEGx1_i5SyYBq_YIEM5SvkR-K1wkfZXc_ROeyEPhiHvxoRUmy2jGkMpdsnZanXMaW4EjZyZP6PhxNep7iFvVk96kEQd1XX7q7gJ3nXrh3Pef7C6YQy9_34TzfrYxgh-S_evlSPHjJFJP7SdpNFLNGsa-GiUnL5SLX4nl5lON7amllbK8GmyeMjDy3QajYo2wAPqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0gT3uutUJP_NhsBoafCJC2KTkcFlO-He4w9SbmFSUBTX3oKoNbvSf692mr53JZpwEqkgt5bBDZUoQ5wIF-y9bsMTsfjJT6ZtA0zjPotegxUgLIlD0kDDMTmXNDdH523CVYiInrwWUoj38JR9ewe21XYO4V5vqJUBLq8ccdDHbPBg6qjtgYIwxhM_Le_6JCHu5YSxsST9bctckj2Km2nvz18c3dCJPj7Ht4WFrt4o6wxW5FubgN9l8AJUBHOF4IiaCz5ztcK2bPcHidYIMVo8Di7CLNhcGPqNqpZOBJvHHIk3sbEbY8sbI00-8YLmC3OJD-94WErBQrj8CN0xImOVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برترین‌گلزنان ۲۴ فصل‌گذشته لیگ برتر؛
در ۱٠ فصل اخیر، سجادشهباززاده با ۲۰ گل، بهترین آمار گلزنی یک آقای گل را به ثبت رسانده است. اما رکورد تاریخ لیگ برترمون همچنان در اختیار رضا نوروزی از فولاد است؛ ۲۴ گل در یک فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27416" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYkU5XZjGqInY8uwPGqI93javJ-l7SoOjU1uL2af70FTWxDxQ6vTjvzerGzbd35_WfmX8tZhO6luP4aPrxevUI0CYa1HysHGGO6BicOhWTENykUs7q7wT07u33NZfBkfK_80foNTTieNGDASs-MQrMJpJFmePhpbJJQGCh9HkD9qCxHIBuEBWeO9CuN7uZUOnCy7pxQveWDKB-PHQusKQnkXKUiMkFmRvcivLjO451GxVD8qcbn4Fi9tRsrVI4qXsAw_o64Sg9_yO6Z7lWEnfGYRgpfsaz4LQHeu5GT7DVpYKUWsaCnu6tt2jByqWBrMUwU-Gb_DmivPAE1QBaBrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ جواد نکونام سرمربی تراکتور خواستارجذب آرش رضاوند هافبک تهاجمی باشگاه سپاهان اصفهان شد. احتمال اینکه با اشتراکال مهاجم تراکتور معاوضه شود وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27415" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=fS-wqjqjGIJnhSFjuRMlGGiyjX7bNRJkaVZU9xy5-e67bAvPjVxGqSpTzKQAQmLazrjIYCqzi1w0rqs24erPLmr9QLe4zlVi1OqQeonssRaxdzvBtoJPY3KzfMQ1psb8lIhJYEzYShJ3vDwMQOsR2y-Gxg_nxeXGizkL7yRSxls0pgTnE723nhYH-mEtcAu73gnUsDP6lQR67ZpyQ5FIxTktZO_w7IQ85w0hgCOFxY4E8tNK8mQkJG6e9wJjfLo211p-1LhXr7TQoUQlmL1A0g_O7tohgJA6hwoF3PyvInrlAEFNDOD9hnoaBQiLTWYp4lIjXIHXhxT7mT0_gXbF5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=fS-wqjqjGIJnhSFjuRMlGGiyjX7bNRJkaVZU9xy5-e67bAvPjVxGqSpTzKQAQmLazrjIYCqzi1w0rqs24erPLmr9QLe4zlVi1OqQeonssRaxdzvBtoJPY3KzfMQ1psb8lIhJYEzYShJ3vDwMQOsR2y-Gxg_nxeXGizkL7yRSxls0pgTnE723nhYH-mEtcAu73gnUsDP6lQR67ZpyQ5FIxTktZO_w7IQ85w0hgCOFxY4E8tNK8mQkJG6e9wJjfLo211p-1LhXr7TQoUQlmL1A0g_O7tohgJA6hwoF3PyvInrlAEFNDOD9hnoaBQiLTWYp4lIjXIHXhxT7mT0_gXbF5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
رودریگو دی پائول: یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27414" target="_blank">📅 20:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=K-pBtss5qZe1RK-7IGRLNKNZDjgtdPR8YEsXxWwLPEM5vvASUT6NC-GEBj2TuG5yPsIh0xLcK-54CD3JCyDEqy9F9X_7L6ermzRs4dxjZvWj-EUNkTcefO6SpUTEf1TYHKVORQr30kP0a-_Ar4hkYL1XCq6PFDcJggQh1QVQPQNePn-EhcIp1FOW6r4xYC6FmyoHcZTR4T_Uf-UwOICAKn-8tVAuV7soFtu3bgJJOM8YNkRE5T2aNNN8wMWHq0a4KFZAi3LuqjZli8RqP-VOLBC47ir5fSHoFDXQ78kGRWnZrw61Tys8a0jJLOPVhKZt7G41cKGwKRDM7JcnEkmK4ons9-KoX7UpOT5yYHUONj5ks79-OM_hA-aYelscG7qEA1GPsMeMgwrgJDfkQlGr9R060bhIZ95tCToKglzsGkRdbBY0M2obafj0Ie0mH2-3s376RtxSvr1zUj9eGdKn1Xy59xVJnt5zeYKK-3A7yuh-9ZSQivrWfmTK9ngEJDSq4qm6rdAsSBW2A8pLLKVJtsf12oDvqRnTMczzl_zHmjQdb4gcmZ-fJcIQa91I5fWieQptN41OqfpDrm5JpJPoJi6YIN2aPjYd7rkkZ4jpgTR8U3Rgw_fLwMqdmWrbN6Nl5C3RoSLUoXQIB68bS0QM1NfpsCihpo6rMwYjSxl0zIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=K-pBtss5qZe1RK-7IGRLNKNZDjgtdPR8YEsXxWwLPEM5vvASUT6NC-GEBj2TuG5yPsIh0xLcK-54CD3JCyDEqy9F9X_7L6ermzRs4dxjZvWj-EUNkTcefO6SpUTEf1TYHKVORQr30kP0a-_Ar4hkYL1XCq6PFDcJggQh1QVQPQNePn-EhcIp1FOW6r4xYC6FmyoHcZTR4T_Uf-UwOICAKn-8tVAuV7soFtu3bgJJOM8YNkRE5T2aNNN8wMWHq0a4KFZAi3LuqjZli8RqP-VOLBC47ir5fSHoFDXQ78kGRWnZrw61Tys8a0jJLOPVhKZt7G41cKGwKRDM7JcnEkmK4ons9-KoX7UpOT5yYHUONj5ks79-OM_hA-aYelscG7qEA1GPsMeMgwrgJDfkQlGr9R060bhIZ95tCToKglzsGkRdbBY0M2obafj0Ie0mH2-3s376RtxSvr1zUj9eGdKn1Xy59xVJnt5zeYKK-3A7yuh-9ZSQivrWfmTK9ngEJDSq4qm6rdAsSBW2A8pLLKVJtsf12oDvqRnTMczzl_zHmjQdb4gcmZ-fJcIQa91I5fWieQptN41OqfpDrm5JpJPoJi6YIN2aPjYd7rkkZ4jpgTR8U3Rgw_fLwMqdmWrbN6Nl5C3RoSLUoXQIB68bS0QM1NfpsCihpo6rMwYjSxl0zIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27413" target="_blank">📅 20:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpEP_KiuxMYuRELf0lbKX0t_n4_SZXZmgd5-khbGMTkKkJJrgCbOUvxdJkvBdxmBfzRnEu55r-3aFIplm7jWBjUS6P6Es605G836TA3z1sobfuqlqAZxxXKq2CVRBgjMuMDa5vMhwCYqLpW0G1v9b1LglA_5fdguBjYvV7djs7lphxVAaasWT3lf4X7Z-ynmAMDsEI_yAsvb2IoiYQ5nogXQE2m4aRx8Xwy5JDaQuTRIxAJftseq9V4BhR7dMkXOLATuXfqZ2uy51TFQHSnTHpFV3I_ZKYwEZO6xLcfn9RleG88j3l2-jYPZd4uGw-THflKtneFBNW5SZuxUaJQuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27412" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKx7MXezjaDcnhKFlb9fAMvFSad-xLsbSam3z-xZIpfae_QxxHoSqJ2M9EE_zZn-0cDnxOJKsFWUGllUZIh2s6vEbSzI7QIYatubM8uSyxgp6a6usVWhD4_ydZkHSzk6UankIjdbWo0mgQYfkqSI8HI_t_17ZKN_AD_ME-l_dteHpk3OZFFZJDyt8UpJaNjfZRwCYwgm39fDvATsN1NysZv9dHOpd6cJd9Kf2eGya4RUh0BdacTOqSxrTm35GhghG9cGDct1pRx1DS1YKn4wUI4eMSOlcTo3amnyPWaUmAIf0AyGITlnhtcfNtWlLYqOTxLcv0MOXZ7y_cK0YjNEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت دستمزد ماهانه موسی جنپو در استقلال و تیم جدیدش؛ درپانتولیکوس ماهانه 20 هزار یورو میگیره در استقلال ماهانه 140 هزار یورو میگرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27411" target="_blank">📅 19:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W25wYhxUfa7Z_6bVA4ERuyxpMilWQMzCWbJZMsbGHf9MFIH6eJEZ9CmLcsqXLqZPTAts8yJY3sNJzLAM46eQdUUi65PMGBZ876GlVB0GepErgbGOvog7OE7_K5zjEoxy4MLKHrtz6OhGNnTAdssbjuegwxKi-3_TcCNuDwlHsMH18WMqbCqUPU_2DeBfYlfa68zojalC5KhgLQTZ8F4p_1x3tJCKsFMff2DKGccduQHwMOu__ALrwf2G97vNHKQetm8NTRTPBiD6WH8JJ8JDTNsyh1M4JyBmzKd1ZJM9qZEf_SAO6LdpqxafnbHxQdJepFv5c41wEieXyKHE6-4fWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27410" target="_blank">📅 19:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4oa_-_8LR_ENsjPAmhM5MdwS6xJbL3NZlSmHwJxlFkJB8RRoYREHxImGqDNsQVVbWlHsCpNqKPUm5YFHR7sIpX1UImlG51819D6YLSL5oLDqiE0IzEGv9hSJEa6TyFcckGbTkK7zttABIMJjealrjky6l0qHBOygdIuvRk2q9-9ZfFmhKJZO5DmMQsqQ3JKM8KlKHqUJIhoC_l9hYKUOWDR7DbHzNVk-hn5VQ_3MuQQO0wv3Ph3wdspImMNuwzCoUROF1Ecy-ctmoirxM9w_mp_WsfE594Fcqq0rHTK7I9wjdNNKT4dbiWN-ddKsr65tk03Z1nN0TFOjZIo-qcRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27409" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3m8t7yDXyE2zUj3fNWIcqrb9H6gHIBGocB9yD1ACRY_kNspiNxm6wsWLvHd_L-Zo_p6RvWcj71-ZLGOtiEjlfJIaX8Ot5_ujXXwIahETL9qzRlCRY9QbHFICd5gKRLlbRqvw9c92ZFHjq4D6-xbCpyRy9Eejlelw9Wro8MjI3Acchh1h1droxl2vFZKn9pvE2VVaBePpCB-bQv6lu_mvJ-CeLf8HFCmD0330Zx7jTtVcErUfwq_cHIyomRZxbPhFgCkiCfs8hFUiEqLp9-junLgmyH4PqEd7h_g5v2jfKmbz98GnFySByd5LTYv3Ds-tBrBNc79rwyGG9q4tnTyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27408" target="_blank">📅 18:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI9D2bjF9Sq2bfFrrX-2RnZxuyEKTnTZQpmrQNwuAchndkBMKNVALsDvSuFm1PWPee8rHDc1eUmmWqkqRbVgBcFt1pPmXac9AEaTEFFQzkKP7T7c9EMyOMtfvVZPLy3pd3djnKrPA8VOkPSQDWKdwJwZmPCfYZpFNAEJyJLchUnyiBjXqMEkCXMoqyiMmUB4_6lXzvE6PnQsFUuGQONJMmAeB3FnjKhXD7qbJcdrpCLO6HzMyvkRL6vGMuREepXgYrVoX-eQuPEdl4GlbWA_CY6Atqya83w0hdTyNVxsgEoyS5_wB6BVy0W0Nge1nZctkiW-vRmKu24JIWz1lB9WPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فصلی فاجعه در انتظار روسونری؛ آث میلان در اولین بازیش تحت‌نظر آقای روبن‌آموریم این فاجعه رو بار آورد. حدود یک ماه که با تیم تمرین میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27407" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=mmKs9h5IogVfMW4pyN3qEvCoYR-Pl6a9vElCyqPtaLVpWL8XQBRXOEKB1nK-y4eo0hZTaaqf4myHbkiY830Lma2MqUoA8XM92QN2yst4OXk7ob9eslmquoJzbmtwfV_L1sLayTeW2IdiSIAOPqFpN2s143FT_xHXmViwsgBdlthexjhfrGegHkJYruB98W7Q7lvyKmTSlVc0YNirlUpjYFAsDoOGUOdFMZeHq4gr0PjowFUVJZ_UwdrhLAh5dhvC0GnqdjfPF2w3yG5Q-Nn3AWAcdIB-3nlvgHeEvQKcnnFJ1cEB2m9CXoZ4qA6g8sTuRTl_4oE5rBBOieUgtYzUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=mmKs9h5IogVfMW4pyN3qEvCoYR-Pl6a9vElCyqPtaLVpWL8XQBRXOEKB1nK-y4eo0hZTaaqf4myHbkiY830Lma2MqUoA8XM92QN2yst4OXk7ob9eslmquoJzbmtwfV_L1sLayTeW2IdiSIAOPqFpN2s143FT_xHXmViwsgBdlthexjhfrGegHkJYruB98W7Q7lvyKmTSlVc0YNirlUpjYFAsDoOGUOdFMZeHq4gr0PjowFUVJZ_UwdrhLAh5dhvC0GnqdjfPF2w3yG5Q-Nn3AWAcdIB-3nlvgHeEvQKcnnFJ1cEB2m9CXoZ4qA6g8sTuRTl_4oE5rBBOieUgtYzUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب شهاب زاهدی در موقعیت تک‌به‌تک با گلر چلسی؛ تو یه لحظه هم رگ غیرتش باد کرد یهویی با پنج شش بازیکن چلسی درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27406" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF1fMYq2R9rBQqzR4-rG5u3rWmk8cQzcnGoFWVoj9zKUJy9NoTDuFXzuLQabXI0pNnNdaUw-Blxq7TcLolsm21i2fyY066f6kN8MZ-xGEmMf7yLhrhRaEEZMms-iicqVo-o8821IktgHwPDge2WAs5dxACPt49K2rW4D9_fmAf7eS46OYY-KPS7jcWr6rlb3we3nSmItgb6ZZrw-bl2HdCZ77WEEMCN5FZXKe64PqTNM545XuNKTZApCFGYXumU7NH86XQoc46hKbon3RKcn0hgpFjVnpgKRJneUWYprK-OudkG4olABIKSrAg--54E5YRAn4di3m3kNn4s3-SntIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبرریپلای شده؛ ماخاچ‌قلعه‌روسیه‌امروز تو لیگشون‌بازی‌ داره و حسین نژاد طبق معمول بازی‌های قبل روی نیمکته چون کادر فنی جدید این تیم تمایلی بهش نداره و به باشگاه گفته این بازیکن رو بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27405" target="_blank">📅 17:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVMfvmqdxcVMxr4gI5djIQSoWKLp3nkQzTb7aqmhZYrkytVnUgwxz9mjVnY9XdcY3b-c9G9I3F727DRqxmPvs4tgVsvF-3lm_kP0Cld0xSJjUOiPZSs2TedJbrVBHVD4KJNeQLh-y893p98pYLVIWnLZTAERrI3iitZOy9YYpidIuDeV5ijHZUqhY8JTUTWdpoT3z_tR_oyNGQsw14NQWskmKMyRHY1jnGkDUfaM947MxGX2YPUll8kY5UyQ9fsoHoLJGq4Qu3TP0yJGmZehgKuWLWjbiKXTQa9WVk5STI84dMD33e8fu_P5rxegbwgqMZUVBxrFTJZwqn33AYr1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27404" target="_blank">📅 17:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=p1W38oYYCpoHeGpTAZ_a5uYIw3CGqcKpjUHlVPqOFhKWQwursOt1DXJTQ0INJMePejJazZMyoZRSrO2B4IJneQXrMnYPZ_Fi1i5EqCAvU-yTOZqinb2Pc617QclFwd7NJlRdUJvO6YM0gACTWBBWX018kz-V6HSsk-cFcNLpMGJ-dvDgbuqBOJtwV34WywcM8p3WXvBGUz33eNbDy056wMiJHIwXd-2M0byKCC3xOA1D0M6zu1KNip_pP47uc34oLaGRWBOEfW3tsTvd7Vwu6buwSwhYm1DquskMwd6qm5RFPSDS9hcz1fzlLADLemfEZTgA5Yr5onm4X9ZvowzLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=p1W38oYYCpoHeGpTAZ_a5uYIw3CGqcKpjUHlVPqOFhKWQwursOt1DXJTQ0INJMePejJazZMyoZRSrO2B4IJneQXrMnYPZ_Fi1i5EqCAvU-yTOZqinb2Pc617QclFwd7NJlRdUJvO6YM0gACTWBBWX018kz-V6HSsk-cFcNLpMGJ-dvDgbuqBOJtwV34WywcM8p3WXvBGUz33eNbDy056wMiJHIwXd-2M0byKCC3xOA1D0M6zu1KNip_pP47uc34oLaGRWBOEfW3tsTvd7Vwu6buwSwhYm1DquskMwd6qm5RFPSDS9hcz1fzlLADLemfEZTgA5Yr5onm4X9ZvowzLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیانا؛ درصورت موافقت مهدی هاشمی نسب، مربی سابق استقلال به کادر فنی جواد نکونام درتراکتور اضافه خواهد شد تا مثلث خطرناک‌ جواد نکونام، خداداد و هاشمی‌نسب تشکیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27403" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAnpjVY-fDWUUHDr5DqoSw6Q6l0tp30qGZbAxRi-HvE-ICEDgKdgSqDojOcWsJhiY4s6ODjD8woDSHNbKTGjYYM3aOM1nVEsZrkAfLvTmQvUKhF-0fYT-u9jJAlvArOKMJhuhULvE3OiCM1jU-rjlXfDpj480fptLLFj-sOb972N9EnEBXF3rfWtYV6xHxGBSJK9j4qx4clrANNHBf__fUDVDkJtxxOIpxJtwk-X-ZEyw34XZkUKHHmvFtfjC9H5NiAoqytvn3TvTdwFCIrCVwmWdPufIaFcVCNA7HNyf2GVAtoeiSAAeFBREbFKIqC3kkp1B1olhpBOtEeluJlJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27402" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0ppDbTDO8sFcojQIr_N0MTh64c-KZGpN6Fz3wY1DAtUAq79iDbR-lMNk5HzypHC7ocQnIL2DYCoFH5PhAsrcU_dNkO59GSXX0aPU8XL3xqRRqEXGegXrPQRIMp_seG6Sg8QBtbeCzCyny-Rx_tFlwN3cTf-27mb0zRIsDSingyXw5CziVjk9iZuP8HhFLpT30aHu3Lk6qRgxN9QKnTjjDZMv-sZRqVE9yfQTLXfvc6IMHKlAOUGEAr3uCGT9Cq6kZfKFmN4YL0myrIdpmq0QuW5FAKcrCSPRWic7Y1lWzvYXFjZ1hkNv2fvq4UfYtNYoDGEaXVGSINjnVMORIr6R3suA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0ppDbTDO8sFcojQIr_N0MTh64c-KZGpN6Fz3wY1DAtUAq79iDbR-lMNk5HzypHC7ocQnIL2DYCoFH5PhAsrcU_dNkO59GSXX0aPU8XL3xqRRqEXGegXrPQRIMp_seG6Sg8QBtbeCzCyny-Rx_tFlwN3cTf-27mb0zRIsDSingyXw5CziVjk9iZuP8HhFLpT30aHu3Lk6qRgxN9QKnTjjDZMv-sZRqVE9yfQTLXfvc6IMHKlAOUGEAr3uCGT9Cq6kZfKFmN4YL0myrIdpmq0QuW5FAKcrCSPRWic7Y1lWzvYXFjZ1hkNv2fvq4UfYtNYoDGEaXVGSINjnVMORIr6R3suA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی عارف آیمن ستاره 25 ساله مالزیایی جور دارالتعظیم در بازی دوستانه امروز مقابل چلسی بعد از دوری شش ماه او از میادین به دلیل پارگی رباط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27400" target="_blank">📅 16:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA71MM5R-rsoZ3DBpm-QUf8Y_iFku3sNPxee4b_4yNGqLfnv8h0atbimCJOqsq8oDr29lN6a97LUVVze2A_ZFPwkyE7qSYsp_0urxS0ALFTAP7U09QLxMJa0vbOSoyG_Bh_Z5UwBbCEfXMDvHgkApq8_3TUMZN1syVkHsFDC_6YWIV5jBLFfrwFZWrguESP_B3ik-KaMOwGoA_2fVdhYEGjVSkbvRdbMdbhdxZ8_yczZOuIVPsoaxTk5cBz5tr79BzNhMDFOQTQ8pASzT774UcsdNodtubyWDEEQixXT7oXrpoFlY15OPOahUB3W0-qV8XsiIvdLCXOGDllnXf5yRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27399" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIMWlELnx-JODK0hgk8BWov2Sp6f5qC73KKokpRLQAsJcgZ7VnB-HcMyJuTr8SMOCXKNZaI86i0oI-_fDXr2UfUh7LYy4Fi_p2cTnnu0cnLisJIkmVbm-uwVFFzbh60D5YcH6Awwd1YetxfAjRL4LauLpu33wSdaWBQbXDLIE2J1fhx76DiIPm0B26B2B65merParLYuVmqkpC9RKiPG42unPXvlKiQMtFBC6tVUiGOorGxiUgFH2Q8Ji9drMjxaYYKb2TiWO9socWllgp-kS3zyjqpVNO-FuJqjL_l0XGQpq0CW-5GZzKeTcMiEMRjm1c59aeDqqJwKiUQdkE4KlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27398" target="_blank">📅 16:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=BvKbQyNmP_tt0yKatlAzupSfAoRD5ijkRONGUNJW6LVtrSQGAgqZ2756TQbZ_XxK8c-QcnpoUdmFJW-HIfeFWnSYnVsWhVUdQFo6RjrHzGLNnQ21LWYq21rwe0yTQAZJIpteMWdJYsrE_vYifp0pKq4GoUglfRyIgDm61xeeoj2XIMEIyaOKJRcTN_G7Qmrk7JveiG3CTMhFgG2VdzI-9f_oVZcFlIfUP2_horufq9rCUcvPuI00D0BKQ1yGD0U34QvEMzN_Z7gV9UVVsve7wMgrylOfWk0tlE-OPMz_EGLVoHDp15MRStv4RpSraniaHFfptMLeUlVMDwoc7hXCRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=BvKbQyNmP_tt0yKatlAzupSfAoRD5ijkRONGUNJW6LVtrSQGAgqZ2756TQbZ_XxK8c-QcnpoUdmFJW-HIfeFWnSYnVsWhVUdQFo6RjrHzGLNnQ21LWYq21rwe0yTQAZJIpteMWdJYsrE_vYifp0pKq4GoUglfRyIgDm61xeeoj2XIMEIyaOKJRcTN_G7Qmrk7JveiG3CTMhFgG2VdzI-9f_oVZcFlIfUP2_horufq9rCUcvPuI00D0BKQ1yGD0U34QvEMzN_Z7gV9UVVsve7wMgrylOfWk0tlE-OPMz_EGLVoHDp15MRStv4RpSraniaHFfptMLeUlVMDwoc7hXCRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛
یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27397" target="_blank">📅 15:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=hEP5T49n4wL3GDi02yKm9cPjFvwweoJ-1-JuVL2JAfjdtrSXaoaVXC_HjaAbyH4rPcJpbPmZVboLT6lPAHYV41LM7AO6W7DU9C_po4ax_WgSKm4vWy8b_b34Jkq4H2ispOhqgCYqtECk-tRhTUhXw2csMIbZnP_zKJtDR5zFTaaRW4XEDaOB8z9AaLWiAExZtZpQYkNJHu4NGi4UOL1BxeGNWGppKRnePpn6I9WG-QSDiMRQbt-p8NakxQQ02EOt_1Rn0UL6RoDwBMOoE5eJa_Zjj4iPOc3cexy5od4Ki2RNsPwp3b14Z1hWta8l-78bZgsN1eEWBx6PVHJP63Gbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=hEP5T49n4wL3GDi02yKm9cPjFvwweoJ-1-JuVL2JAfjdtrSXaoaVXC_HjaAbyH4rPcJpbPmZVboLT6lPAHYV41LM7AO6W7DU9C_po4ax_WgSKm4vWy8b_b34Jkq4H2ispOhqgCYqtECk-tRhTUhXw2csMIbZnP_zKJtDR5zFTaaRW4XEDaOB8z9AaLWiAExZtZpQYkNJHu4NGi4UOL1BxeGNWGppKRnePpn6I9WG-QSDiMRQbt-p8NakxQQ02EOt_1Rn0UL6RoDwBMOoE5eJa_Zjj4iPOc3cexy5od4Ki2RNsPwp3b14Z1hWta8l-78bZgsN1eEWBx6PVHJP63Gbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27396" target="_blank">📅 15:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0574804636.mp4?token=wAdoSkeSMEXK_qkSM-K08PNiq25C4YDpucNf5BVLoEMVmR-BwuzHpqiItOvu520H40cUHHhyZv8NOEACeEC-kipE7NgUdl4kLJjCfysMMLQpPlLUpfr6j6ZBNoJnw8g-lmMNnaxcrjhp1RkBShfEFwaJiG-GK9VJbHLn7e9DhooGB7d9pKCy1IpNAUKSJJcKmRXa9-gUAVvFIeS9DIE2qF17vPplOBKi9u6JbhMZk2KW4SYFtv4CpI3npcteqRr2FSTc8R3CHGn8iMLW-Bg3bl4kjNtgkk31TSV4WPg1mJbKOU18c1mIQ-7zzVv7rkuoTjBFdzonwmcHl_6aAHyDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0574804636.mp4?token=wAdoSkeSMEXK_qkSM-K08PNiq25C4YDpucNf5BVLoEMVmR-BwuzHpqiItOvu520H40cUHHhyZv8NOEACeEC-kipE7NgUdl4kLJjCfysMMLQpPlLUpfr6j6ZBNoJnw8g-lmMNnaxcrjhp1RkBShfEFwaJiG-GK9VJbHLn7e9DhooGB7d9pKCy1IpNAUKSJJcKmRXa9-gUAVvFIeS9DIE2qF17vPplOBKi9u6JbhMZk2KW4SYFtv4CpI3npcteqRr2FSTc8R3CHGn8iMLW-Bg3bl4kjNtgkk31TSV4WPg1mJbKOU18c1mIQ-7zzVv7rkuoTjBFdzonwmcHl_6aAHyDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دی‌جونای‌کارینگتون فوق‌‌ستاره سیاه پوست لیگ‌ زنان NAB پس‌از اخراج‌بدلیل خطای شدیدی که روی سوفی کانینگهام انجام داد، در توییتی این اخراج رو‌ «امتیاز ویژه برای سفیدپوستان» دانست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27395" target="_blank">📅 15:36 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
