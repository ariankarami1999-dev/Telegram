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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 577K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 14:22:34</div>
<hr>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUYEmSfCaVfShvj7MY4lzM3MNMlhNawqrHMYq852nAChqa5_AGT-LTin22OXYCA_lczTaruOcZzWIHnIjZpqSuHeRADS85BJJZJYMgNepBRv37GgmM0Cy_J53BcScznmA1yYyxy4WCDG46fJwIhNFwL190NFeEifLDEYwy6aUMr3Lu4pqJiMUa0dRreOQX4-k5F2TrvjZDRFe2i3mNyv2LJZHZ087_9vHVgjiUJ7r-cYwbJQIJhYIPuE2n77ZPj3lwYOX77Xmu1Jyi5O3-mBlvGWnN8ToLfn-YSqvbKwxU4bQsePlcNecyu4JFEAqW20dkgDTc5gGBWieJLMXLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzwrVS5N1D0zkmqsFYaCT1kCdo1-yDMPX9PBpYs2YllicPT4otye9aWm8yComBYLpvscvFhm9Ng3pgjfFVPK3CWTVoEPNdaGN9RrVtteWCZC7sRC_H1Zc4sogyiPBVIhMh_2HTdxKT-FUx8kB-TVqCIL9MPHQ7J-LJ2CeKOlJ8VK1bTzrhar1D5DiPOWqgMu0-m0NbhCYXcWYlu5-RP5xZYZRd0JfdSt2j_m1XYZqhJJXZCU7r--zx4IvTYNWN_jy1Oe6ADMtfQwruZy7w47kp7MYF5qezLXPzIM16hZLON69MuIuCkWUuMv6V9Dbb9W0QnWsWstiwKRqDVuwlUQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIudNl8W9BqEaVz9ho9w62MBe4hIDS4umtz3IvOJ7a9Cwe4d6DCCv5ffiiNPYubJm8l5LSib0cWgl8G-ZfVVweKf85IhrnpX1yw4B9OvwLA5JNQqBC5fhCOfdt4s3mu-HoHeRQva5gv2P3hmOmGd9jB21TQ-pmk6GudXA9NcfIbsnIafmHWAtGC3of6QCBVsI6-CxluT9GXQB9Lz7bTWXAR91-YCo2UZFtU8ho744SE1tgkrAg-kxxf7tuXQB2qreX1ErTvUCewqVDGlXOUZfHPsiUFFF6_2uE86DoGy866Kh4chaNOC3w5uquC_Po0qsM3AwEMciR-4D1jUnF74ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXQ-b2P8x_sm_wp-etQcdMJuPH6o49YVvh2wcQpSTtu7PygTBm3YtZ5fGZNyxMXI23o1Z4nKqsZoyg7lPP33XXr6GuXQ3TJ6JgR-5rARrmxXy6J2AlvDy6o4yAGg_p0s_gT3yOTvk166MmfKtz5n2vWs7sVR9y6YPVBU9RAwJI9Nc4z0WXwUP8aVUv5Zwg7V3K_hNe2UxNRg7dyKVzNzAox_RWuYhLkWVKGMrjhzjyDINg5AdR3s5tAw3y_mJACtBB1WQ88FVEM5Ys2s1W3Twe6aLyjiHKuzKP2ILyBz7Ln6FNo-9BOhI1P_e2aJTu9xyoq_aHmnmKYcb3alQtUaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcnPZsOixQe1vgqMH1-dv2moHeQjDB1Sh1yIoKvf9Z05leal180sVW7D5FQWpJUHkcwfzTWBMnW7o7A2jCVIFtbCFI5yQ-DlwIcMl8wqndkMrnNoLytQQA8EKIqJ1w_wxUBvI7pcWXkjNqF8V2f4hicZAgS8ANkDXSP0MZgqYQq6PDdJgYzBvOkqpBBTrOfT7dzViaK78u466uLIxHfKg80HmPqctiM2bUSLnpIlTHnbo4kR2P5fCCYw0f7hQ_Yo_h4GoMzfIHPUiWc2Qhiz5LhcD64CKxb4eWSoAjrAwdbIenjvXS8klWnpXAjBJkDQgm3-gVznssnrv-AfvNV15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8YNcZOhsfs9aYlvmAzjEvhJX2xLrXmTkfGS35MvJQbetYu9DBFhWBbzVUaMtx6pEJHOoEZ0EHdi5j7ajbe7QTYoC5hhSIyKRv_iY2gUvaPsi_dRemOtPJ4Sg6yVEniMLvVWwcfhDaqNYkHdPon94wLfO-vUnYcvb1_uyJLAPp1JRXujc9duiWao3jVcSIqn9gsfZ3lGwcmVDUqs_kT3STy3hKlie3Fk2CWVlkcaWD5BK5O7_ygaKZCWB93A5quaLUoSBk6CSr6sCuvzsDYCh5q6LdoNhYiNEDv_vs-F2m0WTGHh-wyvn7E1TAy1_Yn-xzOSMcgayQLwywcuGoUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cWZ3aNvKTovdK5wlJEtcUFMnFti411znMhfubyNZ0rmv5KltvMUj7AZ2Pomn8ziYfO47amy664yeClYtRNZ7jVzEu-vPmZ3bhhsD5PcCS5IOSfkjSgA9N8We6nuJ-IuXg1N61bmEZOtdESyh869RQSdi3EIDc_HdYh0Wc6bB2GoKTjt-hihZZxzbvc-gHj3rcn84Kmr1rzcyrnpEEn-dLYXi1m_8WudHYq1qA0uvN-SOSNsbzYYLIbpMcWxFrOeMulfG6LoBhD46iC2KZgSbiZN24UqYvb323f5CFHR3_7cB346wZoCJEJXKqbbA7ECt4g2WAyJXrGBl1g667Wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhu32fQUsqr3aaTbqNhoxlZTBfE1NEh4i23a5uec7YFls1k_rpaSGAhrOsDiMzwkOBUcGS9m-gDG34zKBUE9cFXWRGjqjlExwBH0ChnCtHZDrsq2ljbWWTJQ7Gy7FlzHv7wpG52gbBrbPZEX2bl7UQhKPMeEwO-YvTeIXISORO6nyy8gSW2FOwxBm_1yK5XKAWCCm8N6U8m841h1eTVN3VOlqf-Xvk00DAbStpO5iyaBbip6T5CaVg7LJQUWbjFnX2dP97LW5-34gdm_L0cBo_pNdnpewcj0iqa_l0UWAjc5ypu-lcckdDv64I5wFNFv2MlXuQju4euS5QqhUwrQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwn37v3DdiJDyOkrVEzE7DZE9vGhIUi4kHMUgOIHA11nTAf2VpuBzdvo5T0Mu4Wj2JZwUcl0W4UTSYWqGwhvMRmYhOtLOUUMg81NIXAQwh9BwOpJMxmtZRYAqnaz0NMxNw2v0fzCw_YG4Of83-xCPoGmula7_ZKT50YJxP2R2Qv04E_I54yEuY1FmQFaCvJRBuiB_g1m28Aq2KfnsLlYcOECiGC6YjWJwnh3SZy6AHmXP2Dm9qzmU_VJ94ABAnBRJVRaEv8QjVMEznUNokwq8iDdY3Q3zeAYoecKEDbarQi8o8O4WBPreoi5tWpsb5b8fwRfhgV1hjQb3sDw3nFtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe2lWaQ_JE_LuZKxw3SCFSg6-lNNG72W6Lxx7jF8jsGXA-JkxiLC_vegZaEsn0UfTbQ2AqxKO8VKs0tsy4S91lNcLEppagjEdCDx9gE-eOFVooAijNVDgPtG44u_KAI23ATDzLVAVJTBHVpXWr33h_Ezdrhn2PFRMMXt7vN-5p5VorbpTN7t4glVKKIEzXwOBJWRDzJWxxhjDoCev-Z2nr9IcwqouXCvL_NhQ73S0z_E2aLXWy0qKekuIsbuD3BW5Go8Uiisjn2Mc8a6XyIl_9ypJZozPdsiXWgB49qWtys3JenGlrTPrRBnhjYNrvXdL2uQWQMGA1v7vfFDVeHU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6BRmJzHYlamC7mTb4Jf2wjhavujf0jc6PXyQMvgH74ne2JqKQHCrH-cAcna8nH16BWdz8jPlsveLEKH69vSc6fdqlGGp_EoZMQtnbTwOOrY3myaetXOP5G8LErQ7PoBDfUIky9nfg1sBHOsDw8A4T9YQm1aYHfgSZYCnhRA3775ShiwEEt5_xB0fHQc3M1orK1mnxVgbEs0mQVgL1-EHw-fTjhm70UZX3YMsRuKL3yKHaCsZDZCfXNDdKnVoXGpSDEeDKse9LEfYvF51Pv1vDmV1pHANjHJUR9HjOpTgBndtVBoNyOlMZotmYZp33AO17Yzst6VxqAREamGInG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls3SXx8BBSPcU7ijYCAWZePjtV6vDbm7XKbCqRTXRwAZhDqhnkTWNqMdfpfSuxc0HcWTvajby__I09g81YghWpZcC2G47684je1Lrwxn2kvA4RDiOcbrXQCKuasqO2wMGUIGqqvt1yNmrXKqNhtYQi8t9p4ar5cEhNCXLOG34sND4YuwtljOspMGtXp5O44QulS47cjYsdHxnTGQBS45NNFjYyuFVbdaLc3MjtKsTfr1AgwRf8LjLwttAr1FP4uKFrJe9f36OVsLoyGLixU4H0_N1EdJj4jvVD9qvjBUUmpiPDbP8dC4HFweIpCj4pwJ-FeS0pAZgWYfEtTDhJXzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7k1QKQag2XjTp4ulLno-FuLd6V-b1uUbJNOBKpAsZSwZ1q3TH7rmV_MBnoMIZBgrOtUjJm5WkJ-yj3neK99PN6Z7kwXS_Cutt-Q7aRw797m3V-ijDGwnNFakrWqEpqzPMOKxUd9Sh6tCcCJ2c-NeyShNEQGMKvFuLOha35qJHn6BAJTxcz3TZP4xzMDo2ARC1tiPR7Biw8XPTrzQvkmgqoNjcFlQzpNOSnlsIwL70C7kBwoWW_Q8gONQ1wPz2Va9oIaQJeqBTkf6ZZePqIYMQN6kiLGQE8M1Bnbs8HqvHvOSXWFMlWcDQPOITTec7HbrMuW-eN3bYmTqTK6A4nQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgBRE-0BRoIkjX-llOnkD-WeoHo9lC_nmCHPUi2kM6uSjU9UDkzrgcNR1vKurfokZun9y6wP583WP0qIwEk1UMapusjvn9XixJ8MGHpTQY9MsSa7kiv-ImspkyXvVo_st22-7UUdk53ycFikKV7CQBxCrkaJhRXW9PETvDok3Gb85yKcyP0mvz4LSbpk-is1mV4dItWpQDMUuQFpCD9uMR2T0kym-dTcTNGfh_4wLR8Eb5ViGUwCtIb4B-7ZmeZC9fvrWeQHcmfOSrYFoYGE3aLUL2NJ_sW7xTIE3mNAUI56dPQcTiz7moqgK1TyGlIK5WAXYGitA06sFHhdYRUw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
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
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
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
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2S3GZcxR-w0g-b8osdVFAN4CcEjKaNQ2kal2ShdZQzVa-g0DRxzyAVYfIOPF-O4OMI6l7C5hKGu-Ct7t9mhP0Fduj-7-6PcHcfDAEEniBUIXS2i9s2f6SwOhNdjIK2R5y-UkIGHGgVQ13GaF0ntxDLSYe8GRWfBXgTdWESvnHr0pr1P0cwMU6kO-UWqcJFzITHVXkESbrzF2JNZVz_MYvPWv9zeLSXe-Fb_VY9y3K1Z7OWpGqqKai8e5y_bXBOSo2pDTWuq2m_wXT3dpAynPcpZ0ccQ5vdEBw4XqzEdWMDkU1yUVxhiF4Q9ExDlu6xhpKhfnI0iDsl0ZUxdFyA_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWjq8WKNYY3xXBJek5u6R2iobYnGTKKBpDczD5Sj4zOajZkVcEtI7JZWfKiR5aVAAG0jMibg9tTah51GVSZfBjd1gwtVUpFG-BhkQltV4508uZFUlHsKx4lpGfkRmDhuxKFzpSglWIU0TR57UyF5Wb3VyDPvHy8LPaCSsmnsYOM573SRvGKRhgJX0-v1fFyZR39ySupa7Bbm8hpWBuQOhz9nf7aJk24uIZPF9KWUAvAA1fG1IOTy2XgQHf0aEoQaCiHv9AjBYh03FEAa0lkWUbZGYJEGUuWJWJeLSdL9wxI7qhy8vlYaI1qcL-KPgUnC0qVPcMoodC4GhlpLC7OEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKJWF_HDlWx-SwpskxQPaK4CihyARFex0xfoypA4LDAN1PqTgN291KbU8-kFC8WPhg64beDiySPSVTRN_A2tCo2w2C7kmwyWYPYkJ7U6VFzUYC7FgliJhdSZm_fqQ_mxCc5lnZrpgVhcwOorH3-MgyvJAc4ziWMCn42beFUxoN0LiJqc3nZeUhPQSINmPYPB9giMmXO3DTg2JS-6fc0FtEsLmp9qvtvqn3FiAOQW9Sf2ZHknDsLG2f3qXUi12ygAZxPUhywlIJJcofqzhcQkXnz0Kn2U4hvzIhnWVHmHP40-PPP737DabBhmeDO9BORsaCVXGh86VhCsctf2G-qLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z48Or7rPWjz3pHJbCvL3Ya_bkPv4va-ubuUY46jmgFG05J1YxGE4KC2KxhwI2hrXCau4qtudMxfTMFFu9kX7fK7FZBolr2mnHkY8Gdfdmo9uHBPkrafBrqpjO3qq1sbVx2mm8kZbcfL1U_d5AVTfHKk6MhXm5yTvLUVR-OePS1j0G6Gtj0m9SHEL-kp3eDjePpbQiZ2zS7e1G4LruqeTyd0ybMOBXgOlxUDP177iPbem9zc5nm4BJT6gBoYQQswL_jx0t_axnd6khB7JzAscFTbGunY2cDtIq9jmRAyVTQJzBdNRWAklKQ0_Q5J9nzOqp8VdepweojNhXCXrRbuZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3zpc23F2SgfQY-YsM15kpXP6Jv_vIIffL0n8yxujaHaeJIoYAQC10a-7OQT5sTIujt1XvHyXAtSM-tzpNIjCsHRQ7XMO6ZawQyrDX06KpPotG7X_F-6lW2uHbQwa7YgDRdT61JqUINtIkOmaAwTUS9TvPdakZ2go4XIk1Rnu53bu49MHeLNcYSpw1R3vhjR1AvbOlT6QDSkiCAdaOt0-lu42YiRiK8rn3q6c0B8LmUTlpSu5YIzXxIn1r0bMy9xbgcXW72hCNJTvhtc83ZbkZxfZGhQuaDFGr2B_MWFdrOnbKjbH4aLqH7fhEsK3PtokUfAVorH8SyKrxqMwrAO5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arYwPNq70jOGRjMK2BPfAUO0V8vU75l4A3HFyFW6ltt0HMu8GG57oyNjRmy5-3B9j8IEMlD-mJmn1HcgCMcJZLcnrEqWJuGjjCjZHjYtJfSE6lJJ71gWXVLdJH_dSkA3SrILN-DJNoe_yytBNrZt4cKhdXf0DvIHV7OHt3GLyGRA8rEZLsc9D6RKTGdniAUYwOYi_Pa2A4vyKF4_fEzezYXLseibsYz1E7NAEFa6D9y1G1iP4rQMPuqfR9T8aVCr1F35OkmLfZOtlm1UIHCm6COSD-lO13XHmgCWVO2CfcjEAQRVFmLD7Cyoni8gmQvdCz4T49B8irL1w7t4NgJ3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYOeh3NNTZJWvziDzyMwJ6ZRkrUFigB84Q3T_xo2KUmpxFQCEdkQRGGc8-96DnRS87S0KmruzJpdRiA8iWX8Nv-SxTbcRl5a8ilOBcxP9eVTKjt7QqGzwCUtkGDlnrek_M8FQvostTLV8M716IS6RPmclC9TJ3sqnpG0kiSKOs3kBRLo4BnP-5evivBYfwMVB0T2bipAjIhs05IsnGi-XcMkaGEz4P2LnuD55eLq80Aq1SqLNKJCHyAtx0N8MWLUyqbAWBNQC8r5cWXNGVTI8Fy7B_WtiJR-VjC7o06Uj64nQ4iz9sRyQqbs3h__fL0Xgq6BzYs27zGWzHyysAQCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMufuQDRIdU9WeqSk3z2lIju6QrZdLJ4F1nAAPEW75yA4BD3BRdT3nMMEZ2YwjPsmDYHzuJBPUJBc7fTFNDJANp0rC3ZWt6zznqR1jzVXrq4RtOZQhRL9xmAxflXclS-C4uG8EiXgs6urJTH-FugAG69UAi65Dysf1uAyIDtKnPNdQnRRY4RPdGGD5m74q0WehtQMs-8TzSdbKvm5TvqoK1AsdXnK5hErBprCD-NZhYeZ3Yaba8Sp4lr_Ww2Hy-OSvdcG18uyDiLRsWpXh99Puvf4vfU99ARkHZ4UQ8EOfy74Jtk-p4zjuBo6CC7rnuZbCdUEA9FAkL23N_ijktM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKI-ZP0eJSJfvMbxaouVo9GrWazHdytoiHieIElRJ-plV0SJEPWO8FonzBwqdKr-BBqeyIsZdsp-Ql6SrGVfMewgQnC7sWCSZc_1zMKRc0mdVYIyNqUAN27UPAu3pzxGBYuCTmdgLUEguI8dT8vqzPjAfeU8wJP3PEVAA-qKT-c4p-LUj3Qd7KIgi0XVaxQiAPkRwBWcF8K7z7vrj-QZ-GtUSu6M93z2OMulxM00AY_53A2oY6F6a1cAqZ9dVUZqiR4JhbnUI8ut28VZzsmF56XIXlNRyaFzFLbVhEpwCd7TEwCmtsnbHrhwz8XHANX2kdZyOLabP3g1JDYztLLMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJg-8f4BrCwk43qsOEgMLKMGKmpERGv0r5TGM35Ewja0lUVkFFuIMNziZP46M-3h07G7bR2IeXLmD6FJEfW4DA_CpW0PCyHkSkvb6EeHSNsPgPv_ljx9K4B83N4p4-Kv8TMBVENXKveJlshU0jsBAfokW3NMgXTJzFs558wiSAQ5Jaut4oCZ4D4s3GYrV2JPvNJatMBjOz08fGcsEMKjh8HbTdNMLY4MtZGiLQEgY-3oHEuiwpT9bb_Xxwas3SIDO1slnp4K46rP3vSv9H6TiO927gYtpKyEilc57bjlubU0BtLd74wErDkd56gtSJ2a-0DdzHiMUF6l7SJFQOU7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fen10W2RKem78DCYolKy9_GMEmtXPe7vic36BtpZgEBq2YS6WWLB2VTeqmhOqPiKX3xeF9Dg8okA3n0s89AGmiMr5T85JVaCE_R_Wb5r0lnRxlleecQm0Ret7kQ5cjpaPKVoEXwUlOUikAd4Qa1IsFjejYP3W3hGno4f24wJRcsxFmT74EMh2zaFXIwPJPG5DIT1h1VBNGzqm1QsAvklGLv10yAthZZMSBeWHqHnM47cxBDF5uJrcDztbqqBtPryqPzVFqaPx6VZQD9tBPFKfsfxELqV0cIIbMQ_kPS_huV3TNq-O6XjdhF-GeOu-1X7VVIfj7CF1v9BYok6_K6KQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nov4oz8TyZVqFeaMcWjBI8G_v4gQJcrmuwTCke_Y1exqPvJYjyD0b4MWNvKCuh9Ai92uYwMGXRbSRRig5dlUSrx3zo0KVNmW0E6L1pQudY9o08I-UZ3sfv2WACK76xa3s-mx1JpIWftb6TeHeArMfd-ymlCPptiBeVLM9UdxnqATLNv9uCD3m1eQzw3gn6cJ5Kb-17Cbuf3gzOfr-_c7ACgmV8REUUkN4h4kUXfAMQsN2luyvpc0mmB7qt9yyBA9tlKowWrMSoOQQSW0BRfx_zG7-_7_2QM9dX2SVY5urLsd9372q33ZiopWoyd9hxfCKqh_MK1b3t_u2KoTIl9Dqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR2gTi1RN3B9sNfYq8DVDyqlgjxD42KWcJJ6py4rOfPXH3D0rz9jdTCvild7m9EQQHWdgESQzVMmNZw1zSuZC_weC1KKqBAtmahf6bey38irIrSPYEVUvZY7NpEICwMeqyhD4ryBRlhP6AFSAv2E8iezIK1p3O2pnNI1DHDnYLCeVVygQfIN9NszO4kwFvh3f8I-gJ7II_ew8q__0YVz5Uh_7-g-G8vWr6ca7i8QL_22FpHc34J-ZDZDGeuCpfkPAcL93cU3ArZuhP-R2V_KQ2trh3O6s1lKfvf24gIpOGiRna0QDLoCUSjSv7hmuH1TMlyPhbopQ_FmboVQhh_oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTs5gQzUjGN3_l0o5kjkmcSrkCCk7XOFEfk_yYpCJOGShN2ELbQROfnEfZXDi_n_kuJQI2mVLnslaXrCx9GmS-AOuKWtGZJciV4WeZJwVDmUfqSQr17HDFJMSsr7sKN-Gkp9OzX8kLNAjfNWpfjQFGELSUs5GFpixTfl3FpLyyVTsUGb8Fufw27Wbo4NLU7iYfxXqldgk8xSslZz9hfWTBxbj3zKpKuFzIFd2P0sRou9gBcIu1bJ8z1HLii39USnL8WYPrfzrH4V2g8yIyw3lElhJwSCeIQfmZ_6C2Mr2IQzvaUHyCDFEGS9FvHn1Lt4e8tehDz2SBFjarLzpc3l1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baz6TpqpGM3jO7cDbZfteLMYZaGAkWyZ66lBa0PVRFCqwXEQn_h7tPwT-L9O0JmEEpldo5vbWhOxrh0ytgghC1kGA9bDx8chg08ohZPu-0vKOIzCsm5U0gJvZzK-Vc2xmcQp8hYiJlHvq8mK8QiV8b3DL4f3heb3lZvZG-xlF6ouSNrrK8gOTvtoUAwWRzU850Qjjp9uhQCdDf8WlrKhiK_lKFdN3gFIZ89p2IY8oDYlCBgqz4zVEG6ZHxB7uWf-RDQo8EpLLbZK7lvHGF_4WY7JsfX7xGn4Ize3d8RMyqGCxftoJ7h_J08UXfxKjMdVczC7u-gQN_6wTINWEdkOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=S8AcpVIrVScHJeIiqVq6JCrrVpaOTRQ6nesMMveyw__KDTe2mDopaWzVBF2nIoZ0P5E9CuICizpDBnEvh39kf7PpROwFpf0lglKET2Z79kKfWreWrQfdAXTo0xHfj0GL9VTE5RBo44Y2gD-3-t_FcAxPdBpps6A7-NzEyUuhGJ7KMoN02Rp9ZsA_K027YRyZahvE7Xs6MtQmxlxVkM_uGp2pqyoUdwfzNBUzsAJoKW_LMwLzKZ_B9214Uyc3GSEfbsjm8BqlkD5VO1DBH3h4AuSPjYhVcT00ncHpzjv02C9JK2hNGJPE6nYKlDnlrM5ZL6euluWppirM9tfIT7gN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=S8AcpVIrVScHJeIiqVq6JCrrVpaOTRQ6nesMMveyw__KDTe2mDopaWzVBF2nIoZ0P5E9CuICizpDBnEvh39kf7PpROwFpf0lglKET2Z79kKfWreWrQfdAXTo0xHfj0GL9VTE5RBo44Y2gD-3-t_FcAxPdBpps6A7-NzEyUuhGJ7KMoN02Rp9ZsA_K027YRyZahvE7Xs6MtQmxlxVkM_uGp2pqyoUdwfzNBUzsAJoKW_LMwLzKZ_B9214Uyc3GSEfbsjm8BqlkD5VO1DBH3h4AuSPjYhVcT00ncHpzjv02C9JK2hNGJPE6nYKlDnlrM5ZL6euluWppirM9tfIT7gN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsk0LAIjUp4S51ichYWY4t30zvTj_cBdW5TyMHYdGUGVLdP-sqXLp-uScTMTKzQsvBJEsSpqpZCQnVdi7wQrElvKlnU66u26GBaIETQVnbFlsQr1luW73hhECLWVdzqbeWES-nEw91SqT69W6nPFOHoaIn0BryZDqpJnmSB_ucRQp9XYj4kis_87cuIjbdsuTIlGuNBOLXvvt9ciW1eMmW1urJbg6GJNBmss9zvEg179vtAcJetdN_xAejY302btV_2AXLyhE72ioZYlpExGtu0U0fLksOwFPrOhP-9uIwkv_vCIRiUUG5U0Ry5lkOYhjjx8-KItWUkuaxwvMIts_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmGVRUUU9nm9bQO1b19kdPaxBJphKpPn5sc1pYe9GDxvxfWu6hhIUgMTZuuOGuDz3H7i2UQSZsP2a_4VaIBd0URdA9rr-UdmeyaGUeE19YC1bZ8eTQYN5JcBXGZXrWh4FTK5Fs2hzUSsmFY64to9yFxDJlrHH-HrfczQzSqQnsu7CAw7xEFsVs8Be5oh6EvhDnrMsgHBt7QSDgiVJrkFcPQ6LB0FjXNpAPtNIZwJk2bRMVM53qPr-CZQaRf0WYleuiEs50IlYwDuO4dUbCXGASHKO0U3tUb3Ov8D_9k6FAkcr0YfymGNEpmAKwKZumuaUY91lVjVdjXagS_U5uzG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIQvtyPga3SAWJjoE2TC1AQKAlvGc-cQ2z5iSh-CsZ-UgA7g8J7dCS2FcpRT48egzDeb9p6y5mHMvHwgUXJpJGMHGsDWWojJMPVnjzmGvq2yr_DGP97lhEnVnT1hIyMVKS6gJi2ZxAwdjHXngPLBp10g1lUeAFhcUpsrElrooAU9bilM3zGPJoxmMjLzxHhFEie_H9KVed38OjuAMj9_5MLzUFKoyhOgSAuJrnsWGjI5vv2IITuI1ONjwiod1mSnhpWGZSRH7kT8cRAl92ak9OLDvZlbHpSbC3MyDgKqL9qX0sVwR3fwQgn1m81CDmvnX4HmPeuMB1mKrF8pt3YEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtrhUHxPNACw-rlGtC7_14IPVA5auppECpLbKAnLy57fPxQJS-VjmbUATNiBztkGt2VNHfd-XbCgTnZk8im6lsF61q80B60A-ibTRNW06UBaFmRWCQgnkWKGTj6Hruj2szE876pQQXhkOS-mR-6L8_lHLwqJtXzJJ5GS8pB_POS50VmhPbqi_m6koWG7L1t2Dtee7vEoh-Ity5vYjcZekDXh-prO8NWhvn5DSXoSIHmTvVoCRIis7i8mTAzkaW3Yz44uqJNNuC0qtpIXewcwCcdl1l4bT-ClgTORF6L9taSxdxENE_DIb0a3ISyy_uMDlfaolPbjkttkUgSsx0Zn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=YlbFlja9LXWDaSqEKBsNY38M5xAcjHxgqD_L4Hb_2Q8RhxWoqpivkS-p2AMw8CVa9CxszDRMR4fgVEz1RT2CAXN9o-SGcURNBf142mBjgA73uSNk0IL_ZbGG0rX45SCBdo-FloNNizPwomXqumO4E1YWGPqWdegGFW10I0_iOialcx8LiW9OMuVGU6RSSYaS4ZFzCzipjVOkW9GH6CkzqIz4xGHnF3YS4qxuFimERIoixjdbfiaSor2XDQUfcxQAv63GYU0xOK7xyMCiK639CFqRYxLlGxcbjzwmnA8WipBlTi8HwqgmoaoN795LLliIva9uY41MWsQZubpcbwIRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=YlbFlja9LXWDaSqEKBsNY38M5xAcjHxgqD_L4Hb_2Q8RhxWoqpivkS-p2AMw8CVa9CxszDRMR4fgVEz1RT2CAXN9o-SGcURNBf142mBjgA73uSNk0IL_ZbGG0rX45SCBdo-FloNNizPwomXqumO4E1YWGPqWdegGFW10I0_iOialcx8LiW9OMuVGU6RSSYaS4ZFzCzipjVOkW9GH6CkzqIz4xGHnF3YS4qxuFimERIoixjdbfiaSor2XDQUfcxQAv63GYU0xOK7xyMCiK639CFqRYxLlGxcbjzwmnA8WipBlTi8HwqgmoaoN795LLliIva9uY41MWsQZubpcbwIRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGEWMtgZ8054rHgHUqOghxdNx_kKvGhXweayA720cMJc_6h8U-uHx3UbzIPs9UsF8bnGJoDi20Oxpfr1rS4gh-LavA6GKAWbECqpwTWoD7rQDOIiu7pxePAJoX4NoD4zIKdH7d6xJtDhvdvPnU8BaF7sNFec4WZch8xKp4juzVMPaY2qHKQ4U89bf3JkV59WM0InW5ic_IBX-Z2IYbrE5KEcavmDGawVMcB86SCO2Cva_W4X7hPztUSjv0pd_7o6voPpXXbdymrJQUlQYT5TVMVzqYd16ICO8M-zYcm765tOuW_cciERBqjihzLoXkXjt5roEkSrIXrbpdTeL8nQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmUPXx0iKhgvNP-a4sBVFhrAvSw7cgl2833NIUIXaNAuWTZIOwtWg5Z5d9Pk_I8N8dAI7xgrsLmiEeRv6HOWaF9IeLZD1HO6qh1eGpuDGjHXraIQv_8LAozaiLzGe7ZYAi8EWb0P_9_j8pfE-PFfYHW8PaI2-rOOmmZUx1w_kQBYoYM-5A8aelvxSXV74uvGSvflDgbjKfoF18J6w-dQWbe5LbGwQiLCMLUVEzgYxneXsMbDnwZLIwGeYUIia-OM4YDj_YxYlSdopEb9fc5g3J70lQUx6FC7_0RxQlkUVb5izBC2giUdLuR_GIO2wYYKk6oGJZ-yQO_oS6AGixnESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN-lv4kzHHrct8GXTG5MfK1oU29idLS-eJIVjxv4em8G5goShPbn_0gLwGrv0DIUSvEdtX70ZcfYXj81BL2fff7eGL121B7MFuNSZPuMNNw6WvP3vVg5fbY3I5PqVl_0Nl0mrpe7ryOJ-p0uXMqEMEUfg9dJFRw7OFXvSbrHWpFvITapa40PDyOPSKcdRryyE484lQX7Irhol9pDx4EFFbvu8ShJKTSHcJkRUK1ihpneEOoo23Mo13WtZPCgRHY00s8DU4Uh36AAEvgnZMGcfZYxNsSVgcxS2Hc3TxLGgXjZtrdpyfEXLSpikl9w-ILbH30N4nk_tI4vQEd3AQbiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZjbpk6QpoXC0cCgMFS3jjmtWsanxdV8AVFf_GQ7fFYg9TWIJ89mHXPvp4Kc_kwbEhuwrkrGB5FEoG5OZ3s4bI5ZU05vE8r5IMITErkGtjtdIgRjLq4ZW69sbCsjXKJUTKBLv7df2y1GPl8t1nrpQf3i09frlTaUqJfvEj92-fLpZkLuH-EDtNzheAknzXoneiwhKn92fgXhSPxfQPtO89AYmAjVnsGYbk8c9nJTPfZiQ3JVsHVfm0cmQOR3PDplcTSZd4qHn361MDM3qlkpaGxVhVxck5OfjjyiP15H6I1GFYM1t-YjdgcaMVy2QqUnH1vPsWTgOmSJfxH0pmDInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLGtd9I2fl-IfkEeSg6XZnsz1gxUIzs1sPvMNxqkQgSllSRiyVif-ls_ZW-Qic3wafYzarbFYy3Xj-xhQr5DoQUVGq-Jo2x7eaCCChbylqgwdfXPxdzIaJnrerbfnHyt8tBGO6yXJotbu0NR6cw-7S1CoPiC1YLfBWMY9e3IPgT3VT-ryO22ex38I89wGSDlh0qFV9ksSrIyRofLDmZiXsaBX-7i6OWB_OnmlWoOM0R10OfxtaCAg3orEdMO4t3699tC9ieTGQ-atqjGQFATPv_QP2JFY1xHW9DDpBQBe9ZVyEgdnQYpCJP31fjIAClAdioniIDTatQGiSK6u7YTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0_kpAyX-0VlFZH9G8_xTXVyxCAeMiUPslhAUQxYog_pWoRmil0B8SkvHdTw-Pw91wMSJ1KyJDPaNWkex09vrY1FCHF5XYG3_lDWwuvlKH-mDmCGFPPJahxayBsNyGHf_eB7Zb6IWFBW2E11H5gRDvqGE3z6WExhPISvWnDAimbATnTlBEbkbJcvBsYkr_79itUuYB3QRLsZXaRh_WFBHb3MQx2jDZ8sa_fT3HwjO_wQ6HY3Ohj-sOAT9r5HB4lWW3L0Tp3JKdVFcBFoRY9_-KbmQPKv0DKeEu9OzBF60dDCou6Qn2B1cr0MdTrig5li-cOAflXBhiLLLAtvHRVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF6gJKPQ5le6S9AYAvX4Jd8A6mVkZXDFVE3yAbXgzjTf-rrrWcS9kbGqOU4t2427IMGmXJyPXQ69WwVlcJVvT33YJobPKa38JRSDHjGQVvx3qdpG1HQkKdUWs1RUovdkvbY6X9i7ZHq9vFTGo-qGDoQXZnx88-JW2BtrZMkQRlaFarepnhE15PoDHSSgTg0lOkrgraSlukcAeE6puzKeID_E_GPcd-tUt8akZUNJD0di2UfUMxWZFBrLthZziYRoj6JI4LO-q_-IooYlIDXLWwEXAgL_moHn6Hby86WElFXHR8FvgN646U11xKlv4d5z4QyZ5u4p6g8MpO3axY9ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQbRip4ujFYtEGKd_Z1tRjikYJLamdPX_ziI79xNbdew9CWZUMPjTfxDmMH2egdlaSIvmQ71sLSVBu_fxKqSmBXVUPvhk5QAqEshExmfcMzVnWaYsVWwfs4RhliwOY0VfC3ngDqwTwIhg9eJoMqgTf1R5G_IBvsJe4JwYI5U_5uCPwDYMznuE9QioNqc0TG1cW-6HyMbLR106tkybVOJEzvlT7DkoeTD8Y3__jyGVGtjk8QUN6mOVyFsW44l0QEbPcP0tTZiLlwFGntMK6Wf7Ighdi1jLgXcGXDTEwVC-gVbxp1wpH7lJfWnsUdt3l9xQB4APHIsfJjeksOdn_WtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exTbwPWCUSvpM3JNj6xF0JaGbvkRCe0HKCISNal_AgvrA6-f26U2iTABcdaLUremJ7pOZzNrO4U09ogJx9xAsooCt_cqFPU1UP2Sdu2-nwKPrkIEHImkVlK7d5I017O6JXMxY7GC0-XzmRgg8bAmPfpzv2cA_APQ85dy1FGgCI0H17azFv2JtVgK-NTvQTYNtswYVIbcYcSDRHlPiJFJDfkqjk7Bch4Xop_-6p6SKwY4fZsx7BVpM-uieYDrKss-HSVKtg-9AUW8_e37tCrDN7UZyoNtWmcYVK1akddLp4jULhzx-kdbJTExcbTt-HFO28fCNvv1a130mdoGyKvEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJR3pVhnomNlPbPBQX6oGNjNPtc4F7ckT_1ccONpsG152ImJ6KSsJcTYU1caDXbLbSSMMhRSJxEq1RhZIum1dKEld9fFRg9Nrd13PrMZ7C0PREYJ0So8dFFhZ5nXZOY6IlVwMv1y0YoUcwzir0DW66wxvbLp8NZfSVNUnopgeCNbSMS6ikW4HCG49dK_Ae23TWUgRs1ZIwUAfa7I4wM3pu_nZanyeDgrWAHPJFcZU4jOe-Pn_aVSrAl5AnxOqOyLkbBP6IFRJUQudcTb5b_9yR-XKk1KmpURTOFiJmjb-1ixGd6yRgwNrCSaEmTBkyeh_I-YDaoP14ZRXv6MDZwwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhCAhWDROytiZC_1WIYUzLr_C7cjARO3Ikoz2PPidjWMeKlDCvo8NHS38P-OzHziKSVk970bO1TWLn-GRvTz7CUtCfB_Id037laqAn0AzH8Yvd8rzq9euBgCtV4TZmIXvbYJagPbIYwKmPVmTYS8E9BZXpHKGNk2UZR0P28hr9-h9gGEoNlAkPKqOzUjsEpTTEVinZSWUicaGLxlamXjRzA0GpQmXPwktOy1XQMBVLgZAKqTp6DiT8zxfM5_m1oAAfS0ucjbulW0HmiK6kfMlAXE2dkR3N3mZoIm-LbNZ9IcjR-RgoK-6O3UKl9q0UxK42IYUvVir3UwMC3ld9dUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyCkyQM0cepgmy3VIPauGanVk_rgVaQ0yWYuTsm8jg98vnjlaENX15LHivaoALy9EtOYJDYVMZsIX_sG-qD_1Hbm7yHWKV6rkKJFifa6b8qqWDyWANNh4i8Awyi6A-ZsrAvH-HBKbMJMty-mjwXQuSavm5np-1BtgfxTj_2lqcpu0_Q1e6Opmv3J2Yb6Y-iUGXW58HgQjS4BDem8E-U0jcfL4_iebfAoaem3C-iMVRFfvKfP4yq9TYz_pS37HUZCVXUo3gohXkpDWTSMJcnqUlZkiRYjlHNV5vdB_P6tEqMzbamJnu-UMx0WW2MEraoSDC86xMVsDXqu_nqJ7HKxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD9aRaFjQ-BY3QEOkbzMgl4z1zjCeblKEEgOz2B-ANnL2Xl3pLXAHYkwCOH6qMgutkScMDwlrlKyJE-rui-jmXGw1VIGUPnmiHjI80q5Gvy821mag7DMr7Qq1bMM-1uH5PFjfWz8Cr3FHJI29z7OXbdTfcm1dQxbIpt-k8nYjU7oZEEteIE-JrDrEzXY-Sjjkii7R-JsTiU-ketMAt391kscQ-wdw85LtJT6SiUBfKNSZFbXIRBRkmTQsuYc2mP463weRjNhVpEV_JEgrVXKcwGVu5chFo0ouQqkXKbfZEpCrng9FuSYGEfKRoHZqYRvatFUKKIGu9Kw2ONZoUeo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXZJUKkHZ4f4-0MLEK3dUiQ4u9bJQpNzJmb4jsBDuceHVylOi5vz46C798GHiGyExomT32WEF8xtxha8ZNJT5gawWskKi5XYCWD6NZfyJArQwgH_P3gaWgqcVH8_2Cks1UuSItWfHF2OtCUajTJei4y9tiC43BqO_WhX7Jngp5QegxfoZvhX11OfoP43zI9U6-k_ZyQKyKJwV_SXB32IXau_zpCXSjATCLyG1pVo1gw--Uitp4dntJAVK1LEH1fvTbuw16dRPXHWcBwZWwzlun2OpxXNNClu0G1vpZpLGMj-Hjg-NEkZgDD1ZDqJ5IMJZLA9lIMMefN9Bd1FlzJWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-hTDhFWVtOJas6JaBd2uszrRPNZoEndQDnMvPGzyfEdOqiE_S3UUqM0m2tDyfPw12yxIi6u7_v5jWb6m2l2xp2GdFonEbQwfcB0oPdg3fthDSowNEy-R6X0FSSK8kJ58u6BHx2bHh7faaNK_9ahbWzqQ8F9FesmoDaW1-GIbg2fREOD7kn7sLKjRtGzE1kwrdZTG-YLtVhUN9lruJIFdePl79KJGa5K0CylrHLx1tvdq3ptZecMU39ZJ2O236dIgznbWIgDWFxZQV9rjqHttBZcv_7VleOen6TTPH5EcwJdULQ-hPlM9kyHyDogRAwPX2_d4LI4yXUXwL9-KMcblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5c8RBUaMy_Bf5BVoLwxOnrEpOdplOJz5PTyYhIAfer35HdiC11ICr09OCrgT9dGkE4Vz_d7QsfjfwNpgYRISWRGr5FNV8SRG9yJkuaZ6r4iNjOf2iN5iVLKA79enSgJxN99wqPTdXd85RLER5VUdm5pMMoZlElRnaqlDkl54p0kXwVgqkhKx4PyypWzoODE5452REFrdkAc5xoaEJ3eze1VUmV_PCWJKuk3dk8M_JRl9Y5X6SgO33Ys0FEd1_bO_x9rMK2jIaZ3fST-FG-YLpOLV6sZDP7Kw_0lKASU7LaONHA5dOZF-pn3FKtClctaatPcBLhvV7a0CDdHGrL5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REeB8E5ysy6BWZAkxH1qqvhCbOyk3zs6O8zKyaiovb0fxBUqxZ58flpDHUmW7V-uNYx26ZW8R4nmclb1UVuDqakg350lOhI_wJY_21_rJFbrkXpddVXv_3gLFDEtCyhXjwIEGm00lmNo9Pj2J0jMqC1d42zj0y0I0O4zdTgaQ9U69CYOo63YCFu07Oh2M-Blcw2u1fEcrQXBdharY7l_bDU0v1rh2qxfp5i8Hp91ZVpQJ7DUyIU_f96msnCF9cLl_xCsqU562HxSPBsS4Ql9nEyfmFDyPqtFmHQJvitKHo7RIBQdwct48aGysuH_qKVmsqbiD4VCvS-hggKGSrS-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWa7ubQt40mVvmdpumZ3KieUGwct69duOlFAlsoAYyPrIuVbpbMQ06EVXENYoh7e-OAs6paIZozWWsBip2gBUtDeY5Mqhb2iOl5tIVDIFs56_gqujnjoB2NQs16161qyNyC1Rnc1IDKJyWVvZYBUpeYsoqWwVi_qYPQQlsBn3OUV6q4gAq2c0fUMcVc8ygCaL8zQ7QsLYPC_74vapSCFZ-jcLvkE3-6zLlo39nOeB9I4kle9WZyV5evC7MLX1EfXUn4Sp6fKYXDEzfCsFihKBntDNGGH31G6XuqF_IR2KIHgZO7_SfCCzakuJfeohpnbLR4VBT-pQ3ri5E1YDLMI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8tnOM8YKcfduZ3-6MPnxg419kMPGW-YIMX9VAHaiuEn-sF4BZ7Pb6S_-5KYoo7cIdv1-KVvY9m5eFZuJtRBeY5Dd4XSsaTPCxJCaiDZkJbkmkuJtSzQj1XIPZ7S-BhAXMU94fMJok3iBZMGeS4bnYXBhOFqe5wHULFAUePgpiXuGZR-Yu5d47NY2RXGxqKi45Tq3V317V2mqnLNy1nit07RnstgLf20JL3eZAHkdWexttQIZ_Sh69pI2y0vnwzN3kXqiu_iYnlcbHeiVvohwAdkPB0bCEJB24HMan4D1gtS9k6XPjdd5SwglpoIumvvy1XOjgDd54cvs7ThunXCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSGInRQPCT_66DKhFbXDezYo7UsbRiW_c5Q7RAV1M9ErjL2yFxM_3mW8IEbO24a0IelSiYc47B_dDUQO9IzxCiCPIh_YG-m6X4pizAfcLwM8aN4BYpWeGJQ5TJ_W0QIfo61OqLn230UrEU0aleS5IfQKXLINq6GFzp9Lty8IjbIJ7pbq9w6VycA_BtEr1lcxXek6ihBxaau5pv1AMITOGBU_zdnfhCId36A48UjFwTEbUq4i3HM1dT3BV1qdcnlbFB6Nz8IseJEeRc1N8etQ0mv-zsIHA_y8YxJDrjfMfFcOcNvjw9mrRuY4kcTv1Ev-ipd6o1I5NSnHM-atVwjuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTLJnRdNh7pUL0zWAt-5R-zM2eCCZZ0q5-Umo5bctXpRRYgSPjk4qc14bIFSq5lkPSCylXe8QSizWVPFM-vNVmLfwC6QlbfvPWMq_dcdA9PEb93DSlixojuqaxkTqjGoRA_sQSaqjSgyFOAPLgW1nd4mqrnwfhUtHs4bZDHS-aM34sVXzE-gq6IbCDTqpnKJeRVxt9dfDBcpoH0Etho5jGP8oIDke4UqiU-Vj7uUKytJa_EduXZ2rL0X3LxBdQ6fGL7XxmA0Dxop38sX9bo-OQdnL6_vkQB1pGITrBEXW3ikGdgskxas6tnxAZ5kvMBLNa_3q-xw0NK0WdJ_CZXk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb76LapyINDSxRZSM6-Suze-MW7-x26ZfXyKZhB8V4oazP5BKs0ydOyaJHrDPjNFjYCVj_xtvkyYqYTpp0P6BMTsZcBV7LmXw7NDSD2oF_LFPGEd4pJUhiS3Xxbijs1uf8S_utGhNdwYsKaKUPR-IS1HI-V1-dJbKTZ5shVuIB7GslboAvx9R4lbwX6gEMewgM3kf0E5nI8q_TehIpz9brmwHU4JeITi1blD2dGdfyoa7vM3_zUpC6c43HEydmVd-iCvZ1wpfo_OMfvoEyXKOyuWhUG0wE7WMomWpGnTepJdD0sQQ-x1nB67dKWgqE3Pf5Cuea7lnV94-uULuxNBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWvMK0hJWm8HYq2EMs9wT9DcSyZSB0FnApCSuyCRKFZloM3yC2bNLuwf2SuCALOo2a8uruaRS4hrRgKQuGPNf6n9Jf89mFv08k7m1stiRW5hFgAL4OUbJlSEAJ6k00TiAS8xlYka5HMetkSh4dLZ1fwUKj2IrVgzrPLI3ePQe-AovS8wgXms2HK2qpAA4J7-l9q7GP6G9tL5RKSfDda_XIbndMdKYNIDZimhxAVKo_czoZDhPyLmP1wDIvnr6j-_i_iWY0Vp4bO0EkwQzQ_eqQLAZA7pa5FjtemHSj0ih0Y_jcBGr5lvL7Uoke8qeO0JKTk7US9vGg_TaBGH4iMedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=J0L0fb6zCK3poowUWXE_iCQPL24gnM2e9MKY-TNsrOD04ouv2btc3wcTQMPTU1KgkE9OkeJ5fODzswpi0_I_Kokms54dSKUYe9fxX6kZjfaUm6_O3WOgOP6tBg6NnSrUQ33bX9OV5L-5D8i9MtE0OBOH29ARx__7ueslIEZv2F1aIpWjRCqM1R7Y4V3Nk0vYjAYh18T5MrPU6A-qh49w63ziiiPe-cfZMdHRRFeX7eSirt198A0MamFM_l86EsydH2rdpr42_NxYjQrtEOSjvuBkhuPG2Ob_z51Ua4IZWJTGWG4dQf3EwGEcVhxanEmJ-6wTf-38N7NF5FhxomoImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=J0L0fb6zCK3poowUWXE_iCQPL24gnM2e9MKY-TNsrOD04ouv2btc3wcTQMPTU1KgkE9OkeJ5fODzswpi0_I_Kokms54dSKUYe9fxX6kZjfaUm6_O3WOgOP6tBg6NnSrUQ33bX9OV5L-5D8i9MtE0OBOH29ARx__7ueslIEZv2F1aIpWjRCqM1R7Y4V3Nk0vYjAYh18T5MrPU6A-qh49w63ziiiPe-cfZMdHRRFeX7eSirt198A0MamFM_l86EsydH2rdpr42_NxYjQrtEOSjvuBkhuPG2Ob_z51Ua4IZWJTGWG4dQf3EwGEcVhxanEmJ-6wTf-38N7NF5FhxomoImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBFeWBir3FbxBPkwUiOrD8qygaT0R6xbERzcQq7SEV3vta92GMf1WSbEuWq5_y8HVgnH9ENYK-DE4a1mPAO5xp0-WLvmiDpsVY-orLrthI0458J7IsvxATL8Rh0g9PZyrJU--2h654qUIrkk1Okb05scwTMVZ39NybUFSL-PKDGAdTuxMquwost7CF5dPvbNmQcL2fZcGpl73psfCqxJnQsSUNHzOH6HmLwC-XhbHMJQ1aDt2lGECBsiXamh2a-yb1OQZQXGGgYTGNtFoifsSR4jSOwoRwWNS1QOGtU0ZP5sCRrsR_76xkj1h0zRcVUEzjRnqPwO3R4I3wfqnA16Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaKh_XJkPSzegqenvzCzCBXofg11p9wR8tRqOjKMoHLzVREV9YLeqw60_VLStueqlENkRH2yJiab8rBaoa25cCSC8Mp0071SoqMmClQ3ILY7ysLdKwJR0a5BnYmIq11ySQcQrr9H3cwQHclrso13wj7EpajUrPJaZUxDd9zR2TvEgBX5gTRqXqKMncmR4xGzetjnWpUFMGeJgUMKjwWWcurthORcLrpv-Y4KA8HPTVJ2qAWY18m4QnoY0Am9UpAp5YUc580otva0-otiM_ZRQhEDUZ3neBfcuwR8sFVV5_L_jYwnfvKRM5UsidUxut7yIuiKkeD5aOrfE4rlgsXmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdUn8FLW1D_vtOkmnjxMa7I_FdHfc15RUsdpuUPR9YKciy210F05nnTR9kVFWZ-gYi0rgZDxwtlryLuBEVDO63foVh1hmQIJgpcl5zLFm1-7ZcC0DNrMTBoGqNazYXveB2XuXNUWwkf5J8shI92iRuLRNHdpTiqsNiL9RsrrIIU9e2oUqpN-563ROxBS-eJLxfsV63Px7JN9N2q4egureBuVnj3GsPUMnwNNQ9XljgwItJdc3V4QdeZFzW9blstvpU8fggnHPXBWkKZ40UQwD0xU7tficW90VAk00EfV0-l-st4Wl8UwQOayHNr09fxn0BupYyRYNkaP2AtC-fnxXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=CAWSndWfvPtWqHWlczXLHz_g81x8kETwpR7S-BAQVC4Tn-gwoZxmqGhnSeExk6gWQZLQSAPboS_6YCCzJ3-LV1KTcp_iAaqmZ2ubEkuz9Cdjk-GOVcWZll8VrG036uhxkyDuJPrqk6NTv_cLLhLKl0q_TAdABGyIXlcV3ZQG9ML0OW6yrUMCUgmfqkEjQ2u6XGovAiXKE_tdbL5JikpBugvSHWDCAZTQUHkhKHVyfsCEOcOtQY0-1oS5zhrERaEnLjlluTu5b7OyCETcJSApXqd7Qa6VjUFQCv1cgbv-VZvzg_U5vkD56sAFAgFKcs11zGWHW3NLMOL8fEKvDE24AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=CAWSndWfvPtWqHWlczXLHz_g81x8kETwpR7S-BAQVC4Tn-gwoZxmqGhnSeExk6gWQZLQSAPboS_6YCCzJ3-LV1KTcp_iAaqmZ2ubEkuz9Cdjk-GOVcWZll8VrG036uhxkyDuJPrqk6NTv_cLLhLKl0q_TAdABGyIXlcV3ZQG9ML0OW6yrUMCUgmfqkEjQ2u6XGovAiXKE_tdbL5JikpBugvSHWDCAZTQUHkhKHVyfsCEOcOtQY0-1oS5zhrERaEnLjlluTu5b7OyCETcJSApXqd7Qa6VjUFQCv1cgbv-VZvzg_U5vkD56sAFAgFKcs11zGWHW3NLMOL8fEKvDE24AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqSVrGy1zOjngr8pGXJFtN6Z0N_v27Ab3EX9tOU9M5HaHDj66cQTEioVV4qyjmVhhbuCHzb-hbDXBQ56Gwhq7npzkNu5o1o-uSMWhlOyZRzG-wsAUPOidjM0DdOMJI0f6-7bW_K_hfD0BR7kwCtuIRrc6AYEEP5ggxboIPTNFZ59VhX1el3dDCtuKZamLEnlolg5ciO8iwLvsbxny7Wp2XMudXG7ynU9YDaE_WYP1JWfPgWRblvUSzHsuXBqVdJeoxYBNL4kulCe-BlQouROO96MVcOpnsQ7ndoJQu6s-I1RaWxcWPq7Xp_h8cGzTJ0-27EbUsJvT6fjLCtWNRaseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBpwZrgZM-Rl7WEZa2qd0UVwh9RI6Kh2ORy7NbEwYJ2ibiR9qCgaX7Vpl7bVo0lUAJiYJJqYbQo1z3XbvJ4L_l1nH2ooPvfCkZyaIZi5lr4eoweTwxRRUKL_df1J9YBEJ9fvOQIOYnTgnmDtHCoOyCdC9oPkK42gO5CaVTmNWIB4_rl0ZxFq2NVDapOkCYqyjJY0Zvzc1TrUK7Ta5UvVcvHGDkKKj8ghAMxfQR1hdXxN9OjuAG5n_x4aWVqGtumFrirIbp8d6OVfL_c1siMJLh8ghA-smkZsKWRCJnN-4HX0bFH4bn4FMgqCy7SutSWKs3E5S6adoIWumGA2xNMOtiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBpwZrgZM-Rl7WEZa2qd0UVwh9RI6Kh2ORy7NbEwYJ2ibiR9qCgaX7Vpl7bVo0lUAJiYJJqYbQo1z3XbvJ4L_l1nH2ooPvfCkZyaIZi5lr4eoweTwxRRUKL_df1J9YBEJ9fvOQIOYnTgnmDtHCoOyCdC9oPkK42gO5CaVTmNWIB4_rl0ZxFq2NVDapOkCYqyjJY0Zvzc1TrUK7Ta5UvVcvHGDkKKj8ghAMxfQR1hdXxN9OjuAG5n_x4aWVqGtumFrirIbp8d6OVfL_c1siMJLh8ghA-smkZsKWRCJnN-4HX0bFH4bn4FMgqCy7SutSWKs3E5S6adoIWumGA2xNMOtiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0xy5O3TW0P0Fm7hTM4saP2CjJgMd0dYQ6AhZdprFFJLiJwWvqduH6LfNEZaEaOFmSpNNToFEAXR6Jn8urNw1lDEI0ZTe_t2em2wwRdklIPspxMlMokneZwq2XEZWm21wS03gloxf1QmISS-rZiyna6OlQe2rLgyzCWZoRpFJj7P44EqGq_9r0KnqITxpsvOO9BUXRZ6XXz3NyLS0eUghFF2ETpcTK-iihg3gy46y1JowHAbcjM-1t0KdbdU2rAFoT_VLxVj_XfIPG_sODD26Ew6Z8eU11KcQBaijjWEUyt9KGsa49uLn0ZOf1V9Uy5l7dAVQkHXR1fa5BTu3VvYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAD3Q9emelYKvQBplB55xAAKzcC91BXfb7FaYNFKPHR0Lja-DlivC_hbGWosp6MCo0hdcjuwHbzfc78A0tlF65LIeC6tFYTVkxxX2KkoAo3YBFYD3UPGOk3GtwBhT2ThnBLqVxe3KvjCfDmajtNeyw5D9IchuMtOw0bnsG_4VHXBWECt_RHe-fQSFNySeXk0wmmVnwnFuVBujJJeg9msXoZBdY8Fj_7b_PxNrNM9Tss8ITO_PwzEawOu9V8fHbt4wMXUd6pVVczoZOc2CXduMVyLsm9TJD4vhjs7LmwcSy8eBKMDCj9seqVqNCsG6LRobMO1PCtzaC1sljySs-SALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXYCcZXhUAGDT15dax9xXPevLGv82O9dfTTEP2tvBmSt2g1zTy-KFwepReicuf823TZ5S6uF2XtN-dxZ32ig4xXUp8xwmR00QgVE736djSymTcc_pVO05OjPyEVplG3hlXDITm-eBTeKFymrLgFgTBHRJduCdJZpC6vnvrE6em11otRcb3x7EcD-YGtQxpa9u1KrLci-OKFzwkTqjyvOrUynPo6V9Wbi1uAXttT3noDWseXz5i2bdqPJ3qqdWjnzk1aJMSGVhZqI26JyCJQTWwt9bOWYOinF1MrOcxnZgP-zisjX9sdTzU-wO0LEKOt-wqDiwdyjHHzn2ybTnSZ5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad7MBW4r7CW1HE3CFUiLlVNhQUeAA0vPNazevEP3CQeOJvAol1cZAID7Xy1eP8OsZSawlpRrse3uEJWoA0GTBJ2wvWMV5Vy7TVXY9InhiEgOUuf8KPj1HH1bfnnpNGRmNCF8HB5lXDOHdxh9jeFL8eSHSUMOBVVZk7UWYdXhbcB-zFgBCMT8tcFEhCbVA-t86chaZMwYcmjISHaHds7iOiTDYEZnP8b4mf24TcAhSc3igjMMg6_2Zg2lQbSGla1exuQHC_9BMc_vt5F681hBhFTeAzvoeCAitf-0DtzzyOnFsZJ_1qoTVoHEk8nTr3F4pvcdEK4H49Qs-46VN3CsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riD6uOGt03KqRZGRYZsqH0AL5lxaHdI4CVsYQ_HPSSB4-FJgV1XaSOnhkJ44EXcAjnocrieEMBolNZHxJkykKMg5gmrtbHq1awGTstJVqrsGfFb5tMFKIpBBI2RfpTg2UUb7VKTVMGWFy0zfH1H1E8EsXqPMWNnZ6yn0kolP1lj8VosyEOP8rUnLAl6UO_zR_GWzK_qM0qRPnuZFoS1BJlcPJj4njdvRewlFwJmOPEG351ElijIzu7wk9BUl2q2q5SJBVyB_eJuYWWQZEKOFCOqHej4eIq5dqibkkXEM2K9CJQPmQPu9LAvGzjw6JKD2SFyQ7ZhP7DnAO5SkwSqq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUJM6jQnsxBkFRJZ8e3vtao4yQRGkCsseCOGZn87fie_RBaBgYnjzU2GOcbBVnOIobrhKncCsyhxsnJoMidNvM3TEESI04r-GpqLOmc1xkuW_U6lQ0oW-rBVdtyLaf-P21FcoUYPPB9i3BPBPguWS31mzL4c0h7MoiLo3C72TJd20tC4MPKVIW3izwZN4tjSAeTx3hpWoyAFBuj1rSd3DulK23F_fNYkre5EyRpoGjDxOekjABAXyLxVuBrhZni5CwrFm723xwUTxggprbl9Xm5RcTD99WUTJmrL2o7alFkiwXjvlxHGCAx4jMXe0S6m5x2XeEp4POdhweXBeD73gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0KEJqucCovg9njZ2cV9LxCNL9550ND0cWhd-xAbxkrGYddHPz7GfM_-fpAgUuxTIU6mf5X3wwyfJDqMK_ykqhHB1as4-PiApFMnB_MLRl5HWkBQMYc5iBrM6LEH0AEy3rRjupwN1LPYIUFXCMa6qXow-VDhMXsQnfnAzWXRLEVDR9GSInOdjoNzP79NagPO0k5iBkovbqsUbgnqDQUn-doHmAmXZwLYq23VXY2GFABsYejIhrrbqFa_3TnYBihqUvJFa9zuj1_KTJUsdNPO7jDR975mVdPogktk-daKYUrSy9VAKuH6hfd5esP6KWYCL55HZ2PvUAZUs7QEQpzYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQBy5R97IlRsJeemvxXlRPY9zPkaSnmCE3kjdxUYNgLjWy80E-IvXaxSezRRCMd6JhDEYbNYVwYq5NKjzS27U3uOVlDfkR3_qjQKTEiT4TwloJ2xr4zLgC-AmrYhU4JLig6LlFD0ueDlgJZPRFyB4XkfvHtjP6cOxwKyWwNkpY8kC1RZZTkx0lqfi3gIIrVJgwU0i5yTtGj6L4vX01lXlhDdnv_l0WeNzLyXoxoGmDlbSCgmsuF6BqppI4s5RgNiIuMV0lys_tFxiDJ5CDhw5PAkM0iSBIUeYpi-Y0FjVUwVI1d2vKWB3O-8pTca12iK9DJuq2Da0ZRRtV8Ck0Awfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJI9ax05lceN9hMUq_l7ZAH_L-VY-UB5ZzBGx_3_2Uk-M1WAu1mKZPYu89G4lv1c_TZb8RNtUldT579mEbgj0JImQnEUyr6_i5ORy68Id27Ny7zH5cKE5ABljRsVArNLIS7RLDIRVxM81AtCW_8Y4Ngbbq5GcLYNib7F8jICRrdQVpJU5Nry_1vIrtOI7yQ6PDpeWKEmeOlyOoPXufRDxIBwgp_-62_7jPd0ju94z6cfajYgg8QVigRtSlPIu3JhTRkeUf8TEUVDEXxZx9Csd3iE3y67gzfPzYo7kbRhylTocR19KpCOXwGV8HqEfhkSEMcF_ZZO30S-CuPOigyKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgwjyTXuQp33ymWr6kSV-esjtWjHhatup54tVjSZzRSpaSIGpHL0e5VGr3hl-aDhdJ9hBkQgQC47rPgqFEGfPJmkDVKu72IVQ-NVvI-AJv339ULCQ-00173UfStPkt0xN_sZnDuubKb4mWf5yh7PV4164OIPUCDlBFJIKQvHmDGUJb4O3qcLjX6jWxvO-oxaXl3t7tJDZ1Yd7qSZO5XQ2BdH9w2RVqJPKSW1mVfFMvFWOd111UpCsxXbvFaQG3tqm3BO4Kigg7sOykk4ccguaumT_syb2QYNN5iynYitvulE9sFyOeELZP2iSfulRRpN1VK8bKskYltVDx0QKqd8iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtnY_z-K44yYpgG8JC5YL5Puv-DZLOAUryil2dw9CxQOUSSSgGkcCWTMQ5l3d-_zdQLQtDgZ7Xu-l44WUQtBq2WDyk1SMaFY4k51RoK3ZUjD9fkbaIWlEV5QWJOc0tG3-MjqiZkwvArDw7PxA3cobi46_d2_JtU7Sw4FRfh_D-fgGA0_iCgi1Ra2hV6NN7Qy0wnJ89B9G9qxCtAymJZEjsloRbWLTq-DYYOcZmqxnNgTveb1gcyk9eaVpW29Hgsehq8FddO873XNFizabs5qDBykadQXo7I2jZDYYEaT4ySXSl6qGuvC41dx3xa01bktz1zRIxeE9bpfTboB9Bn-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYUOxL73Kwgca8S32cZpdUDk9Llg79z8dZmCr21KSD7LtLyiFzT76aGOwrFXrPI8ilFtB64PwkKBMwdWrH6BfgjZ2YS2Mq8xRMpTY1bi_U5SFxaeEXmY92FIqkdDqHKEKZrtkqc20yTVTHD_-2hgCuLnF4yZrelvS9oDPI2W7tWKpLwR58dVSPV7W6m00oEzy7tAgPHVfzCHK9jySNXoqtkDUsUYt69MKVd-9jZReI1Z0kaD3UciDb6XbVhxDE4ogsV-pNWkyXpWF4YQ908LK86ng71npZSbedvlSMsOZCKKVrRzCVBqr9N45a96yPVdh2QYcqolPo-DyIZfjRVzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqXdrv52ndHayBraRU8sbwtN3x9VTV-TkhPGxNX99A2eCHRqVTjRLQXVWDmu_zodQKHmbvAcInzpudyE-dZlpMG-iGYPPEZ_NOzA0wNALoSIdtGAjwA3bi3MEfebewaPZ6OPFfCc5floaIiXLCavJ0Y4haX7DqdDwzzblbgaMCi2Az3WDcReE3C30F2XSlJHFuFXHe8zce0fVM6UGCJjjQVueRkn62knVoVWswKS97psmCHZ9rs_IvwDY7VJxaS0molmleEeaRFkt8HhlB_wT0YLO1i6QZXdmwAet1vClAu6vPGKGy93XvpIpg7_2bExHIGwA3HDrLghD0QrL1ERLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkGcNLfExobKEwnz3fF-nEEcFKcBLLXfIfcjRmXBxTQC4gjz2yynubCOUXtXYN8h8eLomKjxGaoqJT67OQ63R2PahM3M6kv8IDZC6zN8_vXO0YUHh7NhpBUWynT2PG26juOu-ETiJiw4KdpeFBRu-kp5mIa5k77wjBTQH7swEOuMzd6AuPg3LJhIj_f5ZEts5vIvzwFubvZOCQZavECcptQvyFfueNnWF1mD_F_8UBY84t2FlPYAdDX40HYCimMmQ-FuxMdIqsGQNrWpXMMgvRTKcHa4_s0wxWnfVHQjXGhGAdDHvM1Bn4ZRqGtPfodSnvyGc-2kYY-3ZzGKu4HbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=pzRku1tGrUq9qahXgvsW10Qb5oCrYih-vdJYkpowY6tI19Q0j4MTHwlcR9Qrf5lQb8CnpKkD0VW7aof5MzNlycW5kJU-WzTYNZGdqVlJv8RTDytmGjAKTvKhe7QBEOcIYQfK98kMy-8fjrUVxVCZTtb_DFPDMQ8RG-rLVbDOfnEB4KeCZNwvgiUCEabmLlzrCrPA3dd7m7tVNqk7EBf5NJ6UVK8Ow5y6D-20lkljZK0lUhDKFNc2xh-kNMmqbDAEAlWtJxD-4erQRvLb0X68lqS_YPfgMBr-ucxlwhvxZX0pLOiJN0h3TeFRxzXDrKwGyXj4KzWw6HWO7wY31PxQeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=pzRku1tGrUq9qahXgvsW10Qb5oCrYih-vdJYkpowY6tI19Q0j4MTHwlcR9Qrf5lQb8CnpKkD0VW7aof5MzNlycW5kJU-WzTYNZGdqVlJv8RTDytmGjAKTvKhe7QBEOcIYQfK98kMy-8fjrUVxVCZTtb_DFPDMQ8RG-rLVbDOfnEB4KeCZNwvgiUCEabmLlzrCrPA3dd7m7tVNqk7EBf5NJ6UVK8Ow5y6D-20lkljZK0lUhDKFNc2xh-kNMmqbDAEAlWtJxD-4erQRvLb0X68lqS_YPfgMBr-ucxlwhvxZX0pLOiJN0h3TeFRxzXDrKwGyXj4KzWw6HWO7wY31PxQeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5xnugE6MsD3kNcXGF8QrOqnfGo4e33F60I7te1sWP1sYYf3tTWdLHCzjEH84ZmrclBvGQkDTT35toPv3nm7QH0ZSbyQqqTZDijQMgS0zm8PHPPKB4x-Zdu2r4Ee7VPdD3uaueeYRGfL1KmwL-YpByFfgTZNu61oTAkLAejnCJ3k4__Thpsf0ICBjTy5yahqeqCN4xbHlDDIO_cH6DasFSYgJ9eAB9n_T0W7oUyWeKZbkQu37OZrXHAKIShgH9PxR39zB6UkD2Rnm-AFaTySgtDz5Scke9YhZHwmQ-nHFVQWHMfDKQXUEu6Cnu6TKA3JYcdpTSFHQMoEmEoLdBTcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvobj12SK7gXKWrg9ZUuR9RE_eTnTvOHS1Kl-_zRM-qiuDRQhOL7ZJvn2XRUiCXy1mJmegOpBvWDnSRzRdlinUXVnrh3Dr9tmnCpffGKh988yZ0IPRUbkzr_SQE3PpRY-oO7oA1Hbr_-KURKLgQMMBxklHX07l_DQP7r8j25rPt4H3BfIvH4GqAOSSrBKf8d1yMDtyVkKGjuwsk7urJ_P70kUiCuHO12hE0CIAFXx9zJB-788r4qMShc3PX-p0D10LDPCZ2XAgp2LDiRPRQLqJ_ifRJM7MTYqG0oambw5UQl1yUEpg-XqQKzeVxuleaGFuRhupv6qEtoTEpVHKtXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKJxT6suJoY196MxERhli3dQ-sE1jDkfzTuYHORrT5NLnMCdze5tMtSFObyJ2Xnduhf8YgEY_FTZB2EtaQoRdrhCoc5yt10-5m0vUb2LZkIJzDU4s-RdUTS8-LTCryWl2EiksWHieGdLgC_rKWmspfo8iZ8djnYuuPhp-2oscx7NrEoAGEi4GHYsRTdV_8P0xIKj74ozg5BfGNMbrMsN-xFwFLKDpoDyD6JKs3JowOkHry0GSOrj8LfHGxS4LHvJft_o22WczjRHI0Q62Lanubj64Av8nv1cI18MCHeBtGLt3f2nS3s_p1T2-tGIcjvPHxOVmDAJcgIVyP9hkhtL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-7MwOh9PeGvGB04xH2sJaxg9Mnd-cUc9uEWBjCJ9TS9XcWmbymbwfcQlElgLvWSfFHbtzLPIhic8lOED-Rxp90dyK5iuP4YqSA3y6V1QiyveB7NhKZxIvemgGHMRKtEXdGgKK2YIkOquMnFJ_pf79QSahG2NZg4tqV6D_dqhuzbeQkF3s5L5_TVLu2gQIiZ92XhVeg8X_GMscVRnC356Xc-2Y-6A7pP-hH1R06sZRp5nX-mfYPOaV4go1maMDRgjQLc4QwoEHOuQNxNkYGe6fJ58maLc2sJeWOh8dDVfV2U985Rtef-44VKTT3zqy2fS5RB3HfxFO3FIPS1hV8jFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=XEs44VWX_JnRJdIlVGJqK4tGvKUS0BERh5xD9h2UtZ7hyXD1F_TTq-Q32tQFDl27UCietuWhQAOCGQCDYNp9WFVhle0TKk3_jOVU5l6a5cPI-AjwfZ898OPrDccXYfRfIEoSIMAiElgH93RR8v3hHQkd0Qz9ChUnkxCSx5ZCj7bdG7OvVttbZSK2N-pgFdvvjYV86CDtDyr2CFxNA7WQh8rN4-nQTerDY5E3fTATT-WnXfBJburUSxKew3afqe3alCGbSlEULStLtQqItCJDutSTsf0wwW4EXamSOu0FqjnCd3DZeF2OwU8wRON5tJaw2fNukBRtqojgroc98BFrZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=XEs44VWX_JnRJdIlVGJqK4tGvKUS0BERh5xD9h2UtZ7hyXD1F_TTq-Q32tQFDl27UCietuWhQAOCGQCDYNp9WFVhle0TKk3_jOVU5l6a5cPI-AjwfZ898OPrDccXYfRfIEoSIMAiElgH93RR8v3hHQkd0Qz9ChUnkxCSx5ZCj7bdG7OvVttbZSK2N-pgFdvvjYV86CDtDyr2CFxNA7WQh8rN4-nQTerDY5E3fTATT-WnXfBJburUSxKew3afqe3alCGbSlEULStLtQqItCJDutSTsf0wwW4EXamSOu0FqjnCd3DZeF2OwU8wRON5tJaw2fNukBRtqojgroc98BFrZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=ACXHL4A85v-h4A_cV8AehFrkVw_-HB4FiA154MsjD_Mpctl0uaUmOTVs64hteQBq-3J3Ob9u-ojedFjdWzmNSP0bSMqXNoxNUchlMILyYUoHYFZpCe4E8K-BOSX655CJ0AuzrpFNygvhX0CPGRvY5eauT7saeWSfLiIJgQNH0jvTh0SNThhy06XYFL0LWLri_I5LJzTqaiVlnVmN0J7A2N4i3H978mtRO6nz-Q5SeOBeKE4-IxW203qIp4YamKwV7NRHhEe2VvLf8XR1AmeCAgk7bd0-_xFAnLN0YwahLFnCwet3gzAR4_CRSpFtdYWne2WGhPGbmjximruJYwt47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=ACXHL4A85v-h4A_cV8AehFrkVw_-HB4FiA154MsjD_Mpctl0uaUmOTVs64hteQBq-3J3Ob9u-ojedFjdWzmNSP0bSMqXNoxNUchlMILyYUoHYFZpCe4E8K-BOSX655CJ0AuzrpFNygvhX0CPGRvY5eauT7saeWSfLiIJgQNH0jvTh0SNThhy06XYFL0LWLri_I5LJzTqaiVlnVmN0J7A2N4i3H978mtRO6nz-Q5SeOBeKE4-IxW203qIp4YamKwV7NRHhEe2VvLf8XR1AmeCAgk7bd0-_xFAnLN0YwahLFnCwet3gzAR4_CRSpFtdYWne2WGhPGbmjximruJYwt47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1iAKTjRLl0z5_t07bsmaJbHiRkBJ0BzLIuVLCUXopaSTMpq4hJFq7C54ur6QNwRRhtwn9Y1lPDh20MWZLagE6kY0RJVYijTn2Z79y-g_hWCxfMqSPeJ-weS8cXNusYONQVN4YMnzIcVLyag5ortTW0U7Vh5FCWNki_63AHyyTm11iSG4hzRosYY-2T0sexZh3TRVu27IR7F1DnKlJBq9UWl0Fk2RZRQ4ZsC8WxizaY6Ot3x7QhdnSAitAQ5WfOWQHD7N_puBLP9_2J5bxkq2wiIUkmeQXAvkWxrV-CtJIDZRXIzPUGqVJFflQbGQn0x6XApKjS4AXgVRlGAFrNe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD_yW4IN8UGYpHVlrq3QUqexwecCR5bUQ_5sgkm8XJ6DN7slOuKYBHEtu4fOIGDjM22AscMdPYxvjTUHuL2grf-1ktfgvpW43l1Q3mlXXG9_QcEoMJLT0IFjgMIjef-a4gLVSAwngkIqCWdTvWh_BwGYe3ZQ7nMxpF6oxwqRchWL4Gv2r4G5S0Avk1uodM3z3MICZBwWfLeMobojJo3ysNDSqdbv72hUWHjaancmVt2YtYUct8uzomoeeKfeJBKCw79Z8Gxv-dggwtqkQDlo9Y6JaGRWh9QgR5_aDs5td_huuFwomBizrB73vEk18VM3krYisbpcW4svMLN2GIXL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6i99kN3-Sk_IA4dqqZAr3_Z-1neCOOM6_thLwbneGLf9RwpVl1-hu31C1KhQvi_j9xla_pg-Hc7N3DpzM13IYCT6lMpSPFRJepu9jZ5Zde2qpSmw55qrD6yIBKHLxlkASk8CT_TBsdYQkCfpBYFDzuctCCuddQjleL6Ak5jsnT6gtaUqAwxxJV8IXZp1K0oAFceZ29JS_DrAGMGyY8DFioaV52Pdfyn3WGXrZomT-QdvHzbwHdf-_1OCB3HcuIqEeqxSj1d4DKd5MYBBo0ybDJbO3iYy_LCux-0RR2RfeYLjwrGqX7U0_YgKpnmYx9l0vOsou12PW_PtifuD9BJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkokEIdeHKUKxo7Ncry6P7vChu6REYdJTbCkwnKR15gvP3HQFJj60TWg5bkF4D_VjA2Sf-wz_EEtXpB0Tg51bkKAiKcYUJ3i9md3DZ7fsoY8gloZ2THEx0EcY8IqDtK2iC7GM93uGazUwXI9JjyVicrhapqUACnmtQVvNA0vDIvSLdd_y813q-qvn9SMWLXL1kQ2A34U_Rg152bCvwIBg4YjLCk60f9NnTlD-FHjKMrNC9LaZ5-kcngevVgawSfYSrYHClS5ixAOC9jmz4jxHfwIqd09wIjfU7M2RLZtEvyjIrIFWCgz6bCH-frYoNPtszbhfjwMXN1_NutjgyAoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jis9ZGiMbnR3tXlupjXCtDFEbe8aNWTPo5ACibo88T7aI7Oo0DLe4zWmr7imwXdwSsh1cJ4k2wiqicTBcQ69HkEAeqjzEdgc9vpKlYgf5uBAefakG9qjx-gdurZRJPpCN1P-QFVvMc-rgLZFhnbBaOmTQJqF9RzUB5tVHBDp-Ad-CSmsVfioUTbah5fpfOAyZW8csogorQAXlcp2rxCP3dkzqN_0fX0te-CPk_m4eXfYCmSjrzMxaarjuJHQPbKoG8AOGn3Fuhr9MF_r6QC-tXwujocYk2BAhmNyMJFT1PvK35sOBwiyswe7vW_03Jf2AFbDELPEs2vGB9Go72lvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGU2nLA6TU-yppGzNgpxtwMdNnphuXPoFvgWW-zCNJ7-8AhobRaQOr_mkXqk2oE5DngV4UD3yFQyeA-vi10rfgZkU1xIEQ7G_351SVYCLnw7sD5f1CebyHkwOi_1bjnKOHhHPy2LdWHmaPSlOzymQYWz31N8Y07gmbPI90TBlKVwdHOwJjXBUhjwTNIrKNay-AdDcUN867vQ72T-3H59iN4l9pjlWjWnl4f83KK8Xmx--ESak69g1shvA0V7kFso8esdZ5JCTC2JqiyM1E7N_HsvkM-PvN7oB889YMUgt5-4ggdEKRHCib0ipIvkTcxVqnXEmtS3QeFw5dGIdAOqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCTVDNljGIFiv81rsSVITGQ1rdPUtJc6FlqvSAoXmyfwd9QmJaN8ijvtg_ahs8ZVAa0l7xjg3htxRakUODqRN7pfE-4585OLy7kbNPoYrBnNOjxea-ZMtwjZgpYDIY-0U299J1qnZ9XVg9rheRbkfleuaGdqWBnJ8pCUF-B9nIm6A_ueWtTbdgi5wNuOXvffLpYeLw59riv4lmtBI_mXYOJwgrDbsZbs7U0jrolIGnNyYP78iS-9JxeUG67zFjoxVPUAhkha8fKB_ElrRW-YMcTP-tlb72cgalUf5UTquhRG4Eq8Hpj0HR5tJp0AXoVpn1xSZJXlLn4JGeU6j-aEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
