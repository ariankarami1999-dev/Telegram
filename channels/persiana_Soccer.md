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
<img src="https://cdn4.telesco.pe/file/poSPcI5yPdJdgU3hrGWzQ8eNlNE3zapgCh-p1KY9EzWFshZrrmk6g8xv_jMz-lhmpSyZdgVhD96EHbQiIylh6-Bwd9mBM_kB3yOweKYxrHTPobLrvL_8U-ytcw3NjalGhISMqmKXBIqv1jTAiCzuTQkO_J1nsIYUqcpCwS_yLrudASTBEtKh1kC7fW68qXIpZshIMQLuPVh-glr5Bru6M-W0_R3wK2bckl5dJVscMkdk_HhOKeFxve6XW0VkbzPAViy-a_52UxoQOBpAMwnSqqC-b79L0UOn2o6CdmcpLuPMI9F5ffHC1egyLumEt46PMdoKSbNdP-qD50Dyt8KtQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 555K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxmBggWwQznbBepo12YLLjelbnCb8_hPGWlLv4mxlCm8eyxPWE-Fup52Dh7xwlt_2MNU09MgD9f9ag8CuR3DekXx0WQaHDy6x-nxj5E4VAx5PS5DrvFJWSUhCc6QUNWSnyIxPiIyY2i5GkLRdARYzndOUGrO07ZjEKEmCFyDs3_aceDPOqioncQOGSUvOx8KL9eS9qIWlXM5AWiaasqgwzqfjGZ5vviXWBB9hkHv6Zp2S6V200GLKu2bzdiO-POPzOoLZ4klWFd6_jcfBmWqHwo8Vz0p7jo8nV84m6PY1E4TDDQ4o2piifuFtMnXGws8vhEEwijGGkbMwrij_lHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLBqqvUJjGyCsQ7DUEFv-GqaJfJ6I6nw8qeTC90swm369o2W0cKZ1M2WyHQ4ub1B_oiI_xpktW-Ic2FLkgGHBUA5m_vjfTCPgp23CjEhbn0jgbCO2-KTXKk71z-LClUaLu5lKuV6Cojj7-z7JnzKwQByr7BbfPDqF1Xw8qw5B_3G10y8a-qvSV6xFzaB-M69ZbNVwTv_smEkgsIpXZGziTLXtkBK1Hvp46zNB7zmBMzIwzaElKv3VJ01WJpOZ-dn4wauJxu_A3IiSujljQLjwYygQpEqLRUUT_eBZsZmsYMWamrG314q77KLJ5aQiBiTbl6MYTw5ruQICwQYTSAy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgHSp4FQPT5edCGRTVBS4QeTExlLZg2kkiMvoQDm2_uQyxSODprtlQzd-pCi6KasAlo2-Sjn9XQBV7v_9JOuN41texcBtD0mxF_3NPzGZlgJlf9ewYGTkwyUlewLYA0NcSRCiBzKeQZEY3foULEt2hOzOu4rYOQ-3eiA_qQg2YraEXsmBFY9r5VKweY4xzv6Ecgewu8ELjD4PLf9XSMs7cYpjOyjjmGpPWYI4f4khLuzR8pRp5hz3ibNsetVT1slA2rPIPOYMKKiP9x1OhEbkfRdhhybMmvNDTLHmiDaHJd7wHeaMc9ZTVfjJyNzNI5yxza-O6XjFafkSXQNit4u4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voXfS-YhRjK86VpLbhCrWjLv0xUto9kt6PSW4f0w1YFa8cqfnJVC2FWSw9iSCD5K5gX8EDSz1VDmUcpSZYckxN9sTggw66OAo7EKuKUTzoQLw1yCaxGGHjI72SVtnBNyrZ-NtqcjDCG54ocXjsm2MgoM3e8FNMYJp8CsAsETzp4LN6AHB_jgapucI3iFqwigWBJId57BWwPRq8EJv35KbsM6SEgsab6KYdqhEBLraKYksZGVd5noXwQnPOZH_8si0dvIN4rOyrC3gDQgWs7fGrbiT-hxZqs_XN062NlQzuL8p30MthVhFoprZn-FC3-Rs3lC4cAB4KOnkH862ZgM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwT0W9ddS1AN_HfBzYjYAFcGZnwtA2Gg41d4Y0aOW1vICpgsIv-7kiBpJtPxsRit4xuPDMcf4D_WAXYv2eFEaZDSqcSGjFg8nrZX6rSAQ8U9tBlOMit0ZlrTjUOMLTEFD3P8g_QG0u0dgBvlwEKnxLIRWwMTeCovGSYyIW9uW-72nDZ5CIC44JQVaJ_-d6SsptDPPNH96Uc5q_D54tjHdpkQPfdqQnoEgBdOwUGT8yBGKM4h49Fcy61oHaZMFBKn_4wnJIyA-7gRoXEDFIIcurjmTw-wEz6RvcfS33Cn5Glb2IZ8L5-K2zviyFuIDgNlPs-7Y-URnb1q2XMR6bv3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJJbFZb63tFVSKU_S6oS4yPXsafURms0CrcF_5A8rEIQjXhxLhbGAj-ucIk6QW111CmWXlcj5Q-6d1fSJ8Snp76mNC4VkF2QmU-2wbOvtWUMhvl190cKgVFgVewBG-V0qlJuUQjdrv6S8DYiEWIrX3R2aJ9VfO4Z34790s6TYx921XVIrNYyjyPfVPTjFwwS_fEadmNymgpAkVKhjM7Ey8qxg35Pudj20J5zecjfaK9ZwR8X-67pnRBjF0UiUznhsko6lzVIGxW_eEnJ9Kak9qiMxpGcg40hHlr6q_RtmzMt2Gc91g7ntsSxvgXx957GMjkT2aFIUzWPhYcCcATpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIT1fTrPzu4C_PhQM5ozlU9oNZHkzbbUsD178TQLukRksm9ARnJ6Wngptn2IpJOOs4Rsm8gfwbzI0QCWIF5PG3H3a2dzxXNrKnIHFTsTc_oiXZVL43EwQDFySGul8__TwPgxqBhbo2ksc8XlSkTc6MNbLJAhW4HP6rgSf-o8LYqeK-1CJfmFlufxDsgXpbJxL_91c0LaTpdTBVUqwUldOCSetjP3TFNQSCj2RnbOE2CLpWa_5eW_32h0_-kqzcOF35BYKd3j7tfaM1nHElxeAh4VG17QFVw7Bey9o6HYF43jV95P5-XsQ0vdNKjkAQDp_BoYFV4WfqhUBiUzWq8htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhL-7w1TUQ_33jcbFyVaTyHSpO43OwVbkXaT16pg-m9LWn6KBKmgE_PVFlXTiawy8RZetw8W5DwysSWNdhuWzGvThaM8oyUm7Cbff4aDwOMm7jWqnNpkByOu6HDOWJBdaYvaMrpbvfCiVuPg2botEwBI_vUM3NX2DVgz_-U2LNXrGsRfyCAx4k1np8ai2ZCBjm1rQjYRVwEAirhEonOJ4xcQJorBqYrVSVm3gNDREFIgw6mRB_cS5N1Cn-qWsLkyyXxgMLgNlk6hXDTGsd99-jEI-Sx6DijnxulP0G-G_96RJXPQfPh03snrd0LY3W7KxZdH9vtrPj2TYOYgzb-euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3uSNg7L8uWofXmLPQTIWhn7Hl5KVvVUv6BjrrP4vdv74YopVYBmE7_OVjp67gpiyn9Feims7H2-oKIcAPLZNxpXoZVC5sPPo68XyKMVIf8vHtRSFnDqg_x2k64ylRVmd-pWiF6lQG9sUBhhdbOhV_imejhnvqmVu9zcHPqxdsRe8-RBvIRuNbw_OlNi3d0S9__Xp-K68bvB6gTdKgFPICZo-HZOJBBP3Gn0UnYCv7xozKizOJcOCx2DzzRtUfy4-j5ArhMxu0rjUxLqZRK4uxUlfSWqEPja7JaOcdQW359vykt-G6OuD8ZhRB4ALcRzcK2GYjc_k34uXVJDli4nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIHrhGH1pginezTNwD6O6DitAxlxUpWXaKBuAWsCNxgPPGeno17E4AdUFatZxq1gSEwhbQc79l6DX2PxccafKddqN2j4gW27vwzqJN54gPqthDp4j5A9fVdBMuXrPmZC0tDrFZbrqoQtULt1bf_0juWz7EvsVM_8aTcnijaT05yqO8dBYFLHCBnoua3nM6IKnTWNIA3-tLyPg8rgM_43vvLkeJDmfuPaaXnYuHymfh1FuuONm5lQutLEQCpXl9zyn16Kg_Qlh08b67ulxzvff5h2hWMnNwKVJrgMEhSL98FeJT9HZcPfV1TTZC_-0gIT5Mn81jS1P6WUVWVvKbCyug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSuZ_MLKdZldb2qdw5pDQ6OZD0aoTz3aRfbRIUyUIZf5RJaUoAo27EmixI--QBSMWj7BkIHlvSiFyZaGQ_uzZVMVup0WSwqx8_b50a7YF4vFx13EHApTMRMSiD1wDd_PECKICvJD7Z9UX2EfIH2B9GNST2Ycdw270osXYEquwg-GQvnnSPoJXJ3rVOFXJgyYnnWZfKmpSF5qABMpTS0YA1XP3tE8dvZLVf2UgxqN-yZK3-abMT00iQfoEb_m4PV8ELn3B69PBfC0N34JLYd368zhQqe4y95ygzmg3WeeAlm9UbMYLvs1s6jUJ_AdRZpcFP72Su3UbQeltprzKxnZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZkCYgIYV8y3JYVt-Yuj0XQyWszcVRJcyigYZSf7mORjoP7GIgqMWkzAhcIkCdCJGZIvvBXpC5qh554APCVwserbybHv4l2DhQnroKl8m48BVQ9Hy7rLL01Lnm6gMvpgbnmGHQoAl9W_aNiZyrWmdP2ct8Y20C-LuHldYCRREBh9I6PMxmh6M6EU4fpJPk4ie66Yg6IexPQjBtq72rg6HPS_R6Fc5mByWoKv8ZvTHNMMKwH706YM-XoubZCR1zCvaKWETzUCq4Nb5JHlVy2oh_qzO6CO-d5rL2t3can1Ye43a6DKEdf7RWP5imHvbou9M_PEgp_cWaulIqDNR9grGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TudvMNuO2Ukk6PkXPQBUZno566PU96Cfb-SKAuWGQR2oo2vSsjXtVGYWXSxraDNJNdxwE2zBVm51RUYMETBccjSjJVMjyNRYZmqRzOlUbflg0p5gdADwJeKI7TEF6wQUOWGdxbGKfkNfc4QZgBl4UXLKR-I3vk8ZeL-CYLsu5BKPU5WDRei8vFaA3tmTYAveCGCf1wasr7ETIKKvCTuZtmkXkbqE4ImoIN_y4HOspjih7XF9f5cn5RnNg5vZ12cOQFyXBsOGe7DVvLz9qKhvh3F-0ZWw1NJhMIqSB3AE1HOHStSNSKnJD0FxYtIq6BsNYIKCvxbZ3zkspXjnNaECgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔊
با چرخ بخت وینرو ، برنده ی ایفون 17 پرومکس شو
🔊
💰
هر هفته شانس این رو داری که با چرخ بخت وینرو حتما برنده باشی جوایزی مثل گوشی آیفون 17 پرومکس ، جوایز نقدی و فری اسپین
✅
حداقل مبلغ شارژ برای دریافت شانس 10 میلیون تومان در هفته می باشد
🚨
ورود به چرخ بخت وینرو
🎲
با وینرو فرصت برنده بودن را تجربه کنید
💎
🎲
ثبت نام آسان و سریع کلیک کنید
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
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr1
📩
@winro_io</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=GTG-m6WSFYF1ZkHvElVHwI1U_BCr_ij8uX6Y55cf7CRVpAow-h_HAAvPxQvl33g9t8444jpMImZ_jo_GTLBO87OTHy9O8Rlp8u1GmimMBFDwQ9X3m9BAHKuXj2W4tBtX3XRJIaNdiOJfSdFIL-6gp94geM5r0APfD_D7XCKdJYvoX9xrKjY-tVQNhR1W906EhvUdZg4Nw4Q5pB5WWHNZN1QiIrDtv7WS8Nk5I0kSW1mSOvb-XSVHM0odJ8_cDIpgsKiaAvtS0C2xONok8cvBlYU_QjV8YCVRh9tSVHirguGho67j0PLj2WVt6MRJ2ks_PL0aoa9zJMT3dyzlrP0SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=GTG-m6WSFYF1ZkHvElVHwI1U_BCr_ij8uX6Y55cf7CRVpAow-h_HAAvPxQvl33g9t8444jpMImZ_jo_GTLBO87OTHy9O8Rlp8u1GmimMBFDwQ9X3m9BAHKuXj2W4tBtX3XRJIaNdiOJfSdFIL-6gp94geM5r0APfD_D7XCKdJYvoX9xrKjY-tVQNhR1W906EhvUdZg4Nw4Q5pB5WWHNZN1QiIrDtv7WS8Nk5I0kSW1mSOvb-XSVHM0odJ8_cDIpgsKiaAvtS0C2xONok8cvBlYU_QjV8YCVRh9tSVHirguGho67j0PLj2WVt6MRJ2ks_PL0aoa9zJMT3dyzlrP0SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=hQCysF42MzC40VVV7iq9jHZlq2vzyW3ovgVqxXOXL56pGc7ZkHPiyRGhbx8dgMM4oNGi0QrR0tfhdZjfVmnNgZtK1OJBCupXYcL9Kf5TAkFLeABObwjMzq8esemUj-HJdNjI_x9XqUnCTtcwtSzWB-okkWUtfrt5lXvKtohDlwbKRD5CQkshP-ubIZVqBA0mfTqWOHv1UkUo-zR9CY9pMO3eIg0AXb-WqohpD1-xdKFDe4muM1UvoOpucKOjQRCr8GevZcCzF1lDozR2BIskbovHq7ZgXQTLc_ES-o-Qtu2Evua1dOCMHJZbX63SzEg2Wc_PUR3pXZlshnwlNWkVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=hQCysF42MzC40VVV7iq9jHZlq2vzyW3ovgVqxXOXL56pGc7ZkHPiyRGhbx8dgMM4oNGi0QrR0tfhdZjfVmnNgZtK1OJBCupXYcL9Kf5TAkFLeABObwjMzq8esemUj-HJdNjI_x9XqUnCTtcwtSzWB-okkWUtfrt5lXvKtohDlwbKRD5CQkshP-ubIZVqBA0mfTqWOHv1UkUo-zR9CY9pMO3eIg0AXb-WqohpD1-xdKFDe4muM1UvoOpucKOjQRCr8GevZcCzF1lDozR2BIskbovHq7ZgXQTLc_ES-o-Qtu2Evua1dOCMHJZbX63SzEg2Wc_PUR3pXZlshnwlNWkVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=an4E9pvysm53cr3UcYNkE_3NGZX_2QG8j4q5pRFtRdNQEsMg_AizomxPPK7XoucEM9msA6P1TvjUrfqRV-F1Cp810FLbH6Pq5nQ_8cwufwafiBApwG_FKq7RRrHm8nYRwJrs0-g3Q5oR1idp0UUybXQzWQpg3eK9vcdUIpZWIPwacsGm2uDGud9IPjiTaMWU4xbWX8bcd4xxnBfCqSIxnF1ZrCLm_8k3KRP2S_MGZU-i14Q2gftWZyso7VDWGS51HykVpg3J3Zo2TCZ9GtGdTvg2cacVdMT2b6_aDay_OeX7frt_WB8H8Y_ndqLMm0hZudXMn9DXcPuT-SQzYn3-ym8vZvh6SYiRcNrUEuVy4CQ15HHE9-_nTMFI4uuzH8feCzPUrRhSHnmyoSHv7bnBHOSpzyA1MOJVtzHG4w-JTo45Z3VHjGZ4wEt16Y-TsMluj6TKUiC9jHZxS92cUk4yKnZcWYq4TYf4gnjzmoYW8GfODAmu33R3UlZerJ0Gawesan9sUj8dpAdrKPPQ1rALWm3UFj31sazcOmpK19oL-FTp-fRnKU3xhLoBUcnZ9hAFbHviAD7vLeH4RwjwvYN4OPblWBCw2S2FXdXUUGFuSsSu7j78LPgB2Azl8joL0FJsAF5485duVCvg60U0bBrk6POqJPeZFHaOeO9qPEjqx8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=an4E9pvysm53cr3UcYNkE_3NGZX_2QG8j4q5pRFtRdNQEsMg_AizomxPPK7XoucEM9msA6P1TvjUrfqRV-F1Cp810FLbH6Pq5nQ_8cwufwafiBApwG_FKq7RRrHm8nYRwJrs0-g3Q5oR1idp0UUybXQzWQpg3eK9vcdUIpZWIPwacsGm2uDGud9IPjiTaMWU4xbWX8bcd4xxnBfCqSIxnF1ZrCLm_8k3KRP2S_MGZU-i14Q2gftWZyso7VDWGS51HykVpg3J3Zo2TCZ9GtGdTvg2cacVdMT2b6_aDay_OeX7frt_WB8H8Y_ndqLMm0hZudXMn9DXcPuT-SQzYn3-ym8vZvh6SYiRcNrUEuVy4CQ15HHE9-_nTMFI4uuzH8feCzPUrRhSHnmyoSHv7bnBHOSpzyA1MOJVtzHG4w-JTo45Z3VHjGZ4wEt16Y-TsMluj6TKUiC9jHZxS92cUk4yKnZcWYq4TYf4gnjzmoYW8GfODAmu33R3UlZerJ0Gawesan9sUj8dpAdrKPPQ1rALWm3UFj31sazcOmpK19oL-FTp-fRnKU3xhLoBUcnZ9hAFbHviAD7vLeH4RwjwvYN4OPblWBCw2S2FXdXUUGFuSsSu7j78LPgB2Azl8joL0FJsAF5485duVCvg60U0bBrk6POqJPeZFHaOeO9qPEjqx8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=aSa1732_AQvJYhO3-RxfXYLOwpCr8qFGrXs_xaLuieYVf0FJi5EpE2yyi5bm_y87hvY7UXBBf7B1J4ImdyNzAWhIFkF-E7FcKH9r80sW5LgYqS4QtXeSVynVYxMe5O4xuMYBxTwsqslEOdZBJjlRmuNAm0Z3ejS_yOMpI33dazvTYILVDt0Wn3j32xDoACtkB72fTyXrEIS0sJnF4_LnHTrc_Kmr5mQ6X4UvsQKyOYYJ6TKnBbGxsirbso3jLxu2KK6CO484n1WG6gsRpLIlUOEQWVdWt85klSjChkaVy-DHxprcYHAfZEiHV-1N4NwdoI7YomRQgcVWqxLfVubmfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=aSa1732_AQvJYhO3-RxfXYLOwpCr8qFGrXs_xaLuieYVf0FJi5EpE2yyi5bm_y87hvY7UXBBf7B1J4ImdyNzAWhIFkF-E7FcKH9r80sW5LgYqS4QtXeSVynVYxMe5O4xuMYBxTwsqslEOdZBJjlRmuNAm0Z3ejS_yOMpI33dazvTYILVDt0Wn3j32xDoACtkB72fTyXrEIS0sJnF4_LnHTrc_Kmr5mQ6X4UvsQKyOYYJ6TKnBbGxsirbso3jLxu2KK6CO484n1WG6gsRpLIlUOEQWVdWt85klSjChkaVy-DHxprcYHAfZEiHV-1N4NwdoI7YomRQgcVWqxLfVubmfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9CZk-_2g9k1HULkdLxkHBEe6EM9yD1-OmnPVNbDg0N8y-N3KnEnjZNLgExkHyhD5ERTIYiTuPiodDd6pPugo6aNFdL8rWQqJ1n-kTxvJxn3Cd6zbi4fvNdUXzeFNJO97OKuOuQQBpqUxKA1eZ7gGaSNAW7C00m5LX14P9rLvl5n13HO64dehpAbKJCJsQf2C3dqqkYjsqIKxTeec3rw-UizKmgKNtX4lDzjZe93MOhGgbHjShlkVc8_t_4FZu1Peyee-Ky77f_9y4-hJ1bCBJ1sBJgxplqB28l5Kgd0u1SIWS56EnriB75v38o0nReVNVPKqpdAcejRooLuLo4TEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=LrPLbyCWSo_WG1g0Wc7oorwCKMzCq7_yfOm06v9tzZV3nXzEktgjuiCbaSTriFx7w2VctDPCHX96VFgknJN4y2C__WUZqzOhC0C_7AX9Vmf_tnIVu9a4lk8aC_VyaFwDgEqHo5cwMWwSQAX06nXBcBgUUiTEnUCBn47B7qXAH9H9-0dIz-KOXy6n8-_gXmRQiKkLfOVq5Y38pooualKRzG63zm4nQeFNuzDF4EVpViSpQdExeS0l_ncvV89mwJcDmt-niE89YXM7viDbkk4yjIwGrjlOmSoqu-4poZwR0kyTx4jTaKnc9oyTfYso0k_Xt8nUmoxHfPFkjDNUq6zjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=LrPLbyCWSo_WG1g0Wc7oorwCKMzCq7_yfOm06v9tzZV3nXzEktgjuiCbaSTriFx7w2VctDPCHX96VFgknJN4y2C__WUZqzOhC0C_7AX9Vmf_tnIVu9a4lk8aC_VyaFwDgEqHo5cwMWwSQAX06nXBcBgUUiTEnUCBn47B7qXAH9H9-0dIz-KOXy6n8-_gXmRQiKkLfOVq5Y38pooualKRzG63zm4nQeFNuzDF4EVpViSpQdExeS0l_ncvV89mwJcDmt-niE89YXM7viDbkk4yjIwGrjlOmSoqu-4poZwR0kyTx4jTaKnc9oyTfYso0k_Xt8nUmoxHfPFkjDNUq6zjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vQ78mkpf6SXeHu6_SlWsP1nJtArE5gy1dCHJyhnY9qp1vbVW6WBc-BL2QSyR9avmiN13gm3D2KNUgBDTYE0Tsfw8ByQKTOMkoRd5AWHLo1mUoA-itilZj6nRrrqXNzPzBrmGRS488HqD0-sAWI1B642yrZ0ENb9cXLpKsWWAGovC7n8YHIl2UOxgfDSa-oBq7EZ_uqQIoAQDYZYILYvkU0xaKzX47V-Tfib3RD2eJ-Jd49P_662uO_04jeKshdRNDa1XCfULaA_jmLmJ1a6JMTBMU3hJqBKuQHSxkOb20HuCM56sVLiftacgJFjQHrNe4MDYJESPnDZNp8i7ixEKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vQ78mkpf6SXeHu6_SlWsP1nJtArE5gy1dCHJyhnY9qp1vbVW6WBc-BL2QSyR9avmiN13gm3D2KNUgBDTYE0Tsfw8ByQKTOMkoRd5AWHLo1mUoA-itilZj6nRrrqXNzPzBrmGRS488HqD0-sAWI1B642yrZ0ENb9cXLpKsWWAGovC7n8YHIl2UOxgfDSa-oBq7EZ_uqQIoAQDYZYILYvkU0xaKzX47V-Tfib3RD2eJ-Jd49P_662uO_04jeKshdRNDa1XCfULaA_jmLmJ1a6JMTBMU3hJqBKuQHSxkOb20HuCM56sVLiftacgJFjQHrNe4MDYJESPnDZNp8i7ixEKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbw6LmhwvinfFz9F7Rj4UrmTlnrl4cxC6mXftodVyqQj-472n4on8AndCtR2R_qyE4EdXaXm9YFefLYycr9s3zJz_OKXeGeohQZFiKFE6jVmnymosP4nocJ0C2gMa7Iwg27Zgi9tTYOCfhwlos37dPQDPOeiZ1nBK091r17qA-4u9iEuFkkvAsP914V3-sNgIi-zOc4ctoI2wN7szWnVgX26CEo7SXg7Ebcy3iVP78pOLz47UBoYH0EdJcRV1CE4A_kArGR2Wo4msuU6Xyl5SaSOGuxCc1B887ZZv95EabxHMC_yZlp2KwT02fRGp8JR7DS2LmQPYN7xYelLuLtM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=Kt5h7H0rhHsjjUvpB8mbx5-65iqce9A80pPi5_LfA4TlI33tBzE2AgNVV6YZpuZ2bpZFGjPQ2w1bzOiWAmuPY-SUzISTXSYT1-bxeJlJpDOfHQDcMRUy4-5yNmjcvx5N8LD1ekRwdCL4PWYLMrDFWu3Sb9eLGSknxcrtEHLPmVeGeVrdMIzIyY7SlImUK9rAb-fMqHR15M465gJw59kKfOcM1dVzkX-QeBwYnGtooHGfhyQ4FZiQQbJKCafgquUo_ydJTL7DLlFoQ42gTK4T2kGXmcQjjnASeNduoFcIxBeaKsrpf3k0s3gU-bZIQNXuulCa5CTM5aFaIol84zAOhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=Kt5h7H0rhHsjjUvpB8mbx5-65iqce9A80pPi5_LfA4TlI33tBzE2AgNVV6YZpuZ2bpZFGjPQ2w1bzOiWAmuPY-SUzISTXSYT1-bxeJlJpDOfHQDcMRUy4-5yNmjcvx5N8LD1ekRwdCL4PWYLMrDFWu3Sb9eLGSknxcrtEHLPmVeGeVrdMIzIyY7SlImUK9rAb-fMqHR15M465gJw59kKfOcM1dVzkX-QeBwYnGtooHGfhyQ4FZiQQbJKCafgquUo_ydJTL7DLlFoQ42gTK4T2kGXmcQjjnASeNduoFcIxBeaKsrpf3k0s3gU-bZIQNXuulCa5CTM5aFaIol84zAOhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjcVcbk9TVlwEVqfjLjNgMy2HGqfweLnqQozzktDBQbNeoCWZiZgj6XuKJHpvIkwW7xcz__WuNwx_x6V-hCZDHBiFlLBUJqwlWoEB8Rb9jK_d5n7UefHg0EzOAtJoz5UEt5w0hfNFdhtc5GbEEilsZVgsnqSQHtbZtNw6nJZVIfLQd9uZyF5Ch95_H28Nekv2Hm_NOwAZLuJxWnyzo0BprJCD6sclzCIIdO5IW6p3kaHiiIL6Uul-PtVIR9pgP8LPFAZ9RF07uFVWVpmENVnmD_JjEf0rM4KwjjgaLeN-FO534IayNX-Z60JrVcxcIcVpE2qsq2f0C663oCd4oWoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppXxZDmooERAqE3DXQjSUvjID9GpvFcT70GH6PrYA9TdBSQnGwDwF8hjYmkujCddX3Y5jEYELr8Ky7uqYhL69U2J_wSsoIlNlLQ2yRWCKsD1M36xwT4YD7jzrDxHfaHtKIk3Vn6g2c0q7ue5CW-zI33nE21xjNm0FGf4jXd2SwymQ-T0FtKN_Isp3GXjbCSdv6Lhn9KaRrIWIUP35OB-o620Cq_pbiQnDERmjDNCm9Vx-PWv-ndvFDmcD27We3qE5jZYiOtpfZ6siG_7IJrO1LW7uneu5wo2Vb8DSHp9bfl3CquEwHkZUJCJ4CTzfYSdaWupjwjIenQVYuMJHQl2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1d-nyeyCAV_GvMSsJ_v6hkPUQzz2MSSigz-UxZ1ukiPM2FXbioQt7z0W8hyN2XxSxjzHo5omlUJY68z7jbdMpWlOiTWTMXyv9AtmGzcAGBq9HOAl1aGxvxcnsezPLT2m5R9UPIs3zPsaURkSxh5NHcyj3zkxZoHWauBOypJbOAI8XP0dT1KLmb_hiwKgLkBQocO8BoJ-XtlBRJAUWEf_WEKA9bkfBcsVXnAN-kIIQTEeTA_AvvoBLi22UI3LYMD-RO7otQ9tiHiMjBmvxMVPJm6GQvAc2r5v2t1YrQaHvDXfVKrzVfz5syBFytAQ0n4JFfpeOxJozveucuNHplT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTjB9LyyQhAq48GaDQMK--IPH473HiqhivK_3PJkKv4QzA6BZgexaYKFUR7E5e2b2t-heeRl8ynmzACCCsdqFfaTPcOwQxqpOFJ44I3MXRvEphFYOJvKEK4lTdHyFhLf20XveWqBpRwewz2GsVppHJIlxEj_GfO9UobwxDu9LJ8jNlffckUKTxv3ekgn5JmNGxK7tI2fjquwH79TdfvDQMUkFMPwcYbdbTgBduhugcatN15E8K3jt6DeO7j1W5trSmVpNBoDfvpQDqefDTilxXQBQrZ8AFRyHmDd3DYnseyPlkpRCCXpraKO5Tiq9BeBE-1Rzpf4VDA6AnD4WJxq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKFJrsfZkgHX3j3tbr9XjxPydacowMpmzTb7uvT5ecGfnIgPKPFmSMv3Pnhox7xh_Y3UaiDgYc7QKY1MOrakrOAoVA5V5pB3lUF5OPRvQ8UWdh7peepPxw1QkwoyTwbbQSqWwB1KoS04IOrvBZWlfT-ZfELynxvo1Nb9l6DUMEy_LSOvLkvhxAHJS7HQAOqLxSBvGNh5m_gjFw9eixHtEHNi0f6IhnL7qau4oNKWzDZnRqpJPDKuoBFXIUPdN3m9sIJSI35wrNEp8eQB1AsJhp7hd8qnxa43yNwtdD9yA0Eub80HWoJdOj3gu-U_ybogfXkzY3tiQODiJBAFxQGHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuSdRpzNR9FsWtWO_uFWH71-oENHXV1h8nrp2XvVWSt3ik2N0kBUJ28CPOglFSXYGh6ZIQ9p_8Gg3cWJtv_HEVbuN9jHjzHLFIp7XPfuzVFGsBs18yawgD5kKJ1_8T583aIgH0cWfZ2ddKK4O6CW-diSPgBgHewSFoIZ_uR4Zw08rv1V_NX8rZUDtA-B5yEnBsQ_hsyKzPL0x3r-BbEhfLTdEx8xUyRTT75tGnVMknm1GzPQYMfOEICnIoES0pprw1k1xySEBis920455bgSxmhS66D-5z25JiGiF6rx_0wiGeojj_oCg74X5lcntxMaLG--pRVqs7O2DedXfWrqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA_V0u-skeycuHWTwHi6gJvfbgZ-8bGXIIf-_h6vBBAbgm8gZ8tFjjWrDzG_ZjU38muHFngDyN5XqLAmUSMwTdUUBA70xxyL5G05CHWKJWpUlNrhq8v25CYySGoGSAhpLO4-qmWKysqCvsijgXUEZbssLkVcJ2x6yRmMDl5aaeXjHWX8uwmtmi35ZV6dA5IX38MBYaYXsMht2SFrxENJviv78oWW8DgZxhRR77syy3x4SUvt_PCMs4yUby8XgGRIJvdyJ2nlClZ2WZOKVz2iYaJHcNRSigaI5rRSBbAJoxR5OQLe13WBk_rwEFXChE5s4KIK0sRa1x3ZBObAe0QmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-CLyqyaw807jG3gpyiFtog9Lm6oHjOgsWma_rlNCxQaKwW0Gff-2k5U1r7wzBsoTC2Q5_IxQZpiYaa6gU2Kr28qkulvJK-8DA8clUNZoeyK62xghdvWWez7gOXgqQ2whTilinCvNYjbD3JOFB59LV9H8SrXmP3mnEypUk8i_Bq3QaiX1b96eLRm74r8nB1J0uMORyrt9r76cFitvtCpeAX_1Mt89iAvWkG4ghNrqbq6WmLB_0uD1w_IPGRJdlNBvog0m64RfzhD7iVhoeCEERgmFX3-A-_gr_2fuJouNZr5gBpGLi9I9nFmhDi8xFWYez6RrZVaMom8uG2fC2numg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEvdgYx2AN2psBI7oZQ4ZD4-UeeeN7tBKjCfe70rMPnr2Sgl56b7DIenkFx9EvsOFcTyJfwghwJKBQkrWh4iHrVxuggYOb_3w_280v0bTH_MY5-Hv3sFbS3mbRSnvXatEPqRb_eBq952UU-oc51fWtLiIkjx0cccmD5y0ffVb2jyzv5RFBEgBOHjXPWsz-69LSPdSd7G8QRNsQVbHWTJpE2HjLJj9jwb0YpQ37YjvHrE9uxzlEJnEtT5OQE64UadVNREfD0RzBGqy5QjWCIcc26aVvxKZE4CzQvCn6GkwCZf7lr7eOwx-qUef_MYKFWYdiaI4_z9Yu4lrHO4Bl_Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9OdiniUwOu2SVP0Zk7bOkuJLiWrMENucIbhaIDySNb4GUAYXlSJ4jO0Th2QHwU2oSuPT99jOwPoNeUvgvJNsMebKXOLaSyoIdfQT7EfLEYCiF_CEHkcKGbGNOd3DtxuTpRGoQSottGhPSXWzCg8kvSxkKyJk5ht1-6NNTi-r-OWK24JWXv6wzDkUj8V40pABePefG5d5f-AW5zaPWC-WAxlO1MHyvQoLmcBYVPMgpAOxvsg-W6BVRnHD4tFWK6Cobl6eCEWYMXxI2S4Sg8dsGAHdBPhVZRNSK0ZF-ZutXpmA5ss0FP3nzTIAEhN5XooSA7NFsyudT8Z1RmHPSOAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTfd3ja1aU22udiOPJpeqiHpfHYCFpjFmTGBvcPEGpoFyqq8p9_l8bPCF038p_KlLYCVq2lmYIK_1_WlD7LiR5XQb-V8xyWoY1bN6ZbQ0xXBShD2eXlVxaOlZIZXanqg7IBnudqNOElDpbqr4eVeHlhU0T89i1pprpVBmjWvE0mzPZS17sGnv-DjeRfoQj0ufdUbp17JId20UPZ01rAnzm7qL_xY4MBclzEXURx1axy28iaxKPCKYJmx16CAaUOzeO76cs9NbKFv7p37noZpXedC0VtbrkVsFlAc5SUvktgE0pyB5xMtalMdavspkr58F73Aduf7Zt5WJR2qCMImpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abKBTEMCSzRIEi2fpeXXipDCQwaPsvWcvAYwRgrDu6gUZFF7phS6mtWWT5JrXR4WtbquNSaw2zhTMJzrV66UW_kwkDWl4Pie8jfWr83toIaHjDpHHgXUIx6yU_HbjHFXqTK_yaYtOBwPMi8uZnkjdHLq6Jq04rGmacf11cXVigbBFoFLR9YVMKlo3EG1-ek2U1jFxWvi6P9hHiXJ91mXkSSqKZZ9lFdCUiSbAB6Q59mA0RjDeT-Hc6t1XnvLybrHcLCFX8xlF0aPnepX26LNMMzArvcUucY9xqdHD-fM3RzWDt8dSxSqNdk7nHQElEnTBWOY_4Tqme4zzZBdcwQzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=cHuoYqXN9kytq7vtGTamdh3sz6kuF09fMDforpURhKxMPvc-F_Jy_wS4n0YEdER3nZunioDdcr0RDAJS8AOm16nOGYdISY6gFHErdvQmSfgsDqB9YGtUvK4wGIcqybtZwIguKgujN6hregeayygOdEu5lmEymTNXuQviArDa_4o_dNIaVZ05SDQnClbOfwmQ-Q9w8xmIyBzYlAWDiPN2049TPPiWqpydvtdm-pA8J3q6HuQAwQfFCfTjVX9T0CvcHJY7ZCx0Y5JY-lhk0sHfRqWzSQfTmewJXLdTWd3DRtkFdKFheai3Ku7qPbylcuqDIUNQY_yalT1NSZcKqd07Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=cHuoYqXN9kytq7vtGTamdh3sz6kuF09fMDforpURhKxMPvc-F_Jy_wS4n0YEdER3nZunioDdcr0RDAJS8AOm16nOGYdISY6gFHErdvQmSfgsDqB9YGtUvK4wGIcqybtZwIguKgujN6hregeayygOdEu5lmEymTNXuQviArDa_4o_dNIaVZ05SDQnClbOfwmQ-Q9w8xmIyBzYlAWDiPN2049TPPiWqpydvtdm-pA8J3q6HuQAwQfFCfTjVX9T0CvcHJY7ZCx0Y5JY-lhk0sHfRqWzSQfTmewJXLdTWd3DRtkFdKFheai3Ku7qPbylcuqDIUNQY_yalT1NSZcKqd07Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=EEAt8yla_R3aYN89EmrogmB1Y2qJ4pZnmJ72BTwVuc6bjPJ3GO2EfawxOWQKBPQBJnx4EnUkDQpIi4hwxMltDBFtg4gqgx6MTtZf-kU9PL4CAaFMDSqqrayHr85fLzkJhAg-qyv5bAmS5tDmu3UAvEdOLkCMgk9NGSKdf84H5ltNc540LaCaKj9-XKwvE4PFf2wInFnwajQ3mUEuDWvJChoK8tMWST32AA3AOeIfWQVMj5UweFMWjYf0qmCpTChsnMb1fjmiYMPsf9nCsA7cCfIENDr31w1FIbe94s1wy221dNpuVM8Uy2KYZqigeSeKMxQcW-aW6yhxUNCA65ySJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=EEAt8yla_R3aYN89EmrogmB1Y2qJ4pZnmJ72BTwVuc6bjPJ3GO2EfawxOWQKBPQBJnx4EnUkDQpIi4hwxMltDBFtg4gqgx6MTtZf-kU9PL4CAaFMDSqqrayHr85fLzkJhAg-qyv5bAmS5tDmu3UAvEdOLkCMgk9NGSKdf84H5ltNc540LaCaKj9-XKwvE4PFf2wInFnwajQ3mUEuDWvJChoK8tMWST32AA3AOeIfWQVMj5UweFMWjYf0qmCpTChsnMb1fjmiYMPsf9nCsA7cCfIENDr31w1FIbe94s1wy221dNpuVM8Uy2KYZqigeSeKMxQcW-aW6yhxUNCA65ySJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3f49A3vZBiSEq3HEcsKqhSEzPEgkwkXgUumKOJ9bgD1sf0BZ3eieePSdltBLUJQ56dsRuduLuLL8UfuU-AxY2bT1cw_dr4V41DJoET_338dZ5R9ic43UgJ9IVsEwHbPKKHfiK6h-yfuqTQJbSOfuJzzE3lFjfrrXBdsnea1IFfDVFAbtn8Xzi2G370FKo79ADdRablbS94SGuEaoctBpoxif06WDzEIc3dUHLP7S89a_Ze1LnxPXcHIVNnPGwsY1hboA7AtVGrKba0wG-m4bXmbS8rKLy-eHTr2oVudXbwR1IljAy__R-96y_1cfdqZuG7QEoGSlAVcUA-lmo30xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHwhTrXZJHx1j1W-2eqSlRhw4t8ZqdZ55eubGX4whUCypjL5_xse2zkOs9IJG-LISxFOPLcyzBmw4HxsiJZvYKlMERKL5NEhATQep-YAB6MQPxFq9TDk-834904aKMvOahB2BxdHIgKtJMvcPnJpm8skXaeizuplF9-mei6Vr8EfrOdyMs3hnMzVUjMFHclEGXmCmx4Iz50r7eCWUZrVdGZdqgUYbHrbEtFUu5CjIao8V1EhgdgwASAFZ86RqaKqcNcgqMJfaBOx9v9yHYCAO_BPcmNFlGblGGAGwaPTQwF6q-8Ey3QEW9IXX_AMnyhzzJyGVoqj__fFl0otfUgVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhx_S9xbTjLcV_WJ8bA2-vNCshVZw38Bc7CffxYYfEYE8Tl4AAiiv_TN9qDQwRhd0HhxF7f0Cah-6hV74haknTfwQl7ABv6k1H6T4SIz1MK0Yv0Y9EuJi3CGmjNKgdRJrMZtafwyNt8M9atxLO8zORiDqcVn2PB51ZM6dOOkCs_qiY1BrZd0GtVp8XZwbeKVjLkFAn75r16in5Mb7jV3QXNg2d20qC94FQ5SdcP4MOd25r-DnDidvYBkyflBICplK4B-WPPdD5Gzd5L1hMBBRxQVfweylCmuwCfSt05j-K2OcKhb3aTYLSKLoQZTWEA8p9-e-DR131wzTX8V71YT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYV5PB2H4mCamkey0Kvo7jJ7YIlwL3k0jwkl2bpN5GMPQuEMtaw-Xb5ykneEuCHnhWsSLZEbQwnbnG2298no7pUMd4aH1DZ6Kn5XJgNB_v5s8zZuxlKzqqCUropahqXoFE-iySCViXVg-fH_0prpdmITgaFeaskCegUlW4X5TBGbEIMCIz1UjGk7SuuuO_uZCF_QXSobIE2eIHnz9PlXm66xZF6NMRgacYErh2AEYCgiTZ8NqQe8tMd9zWtNySp1sM4SwRDYfDrkt1lc6jd2W-Fi_3LqddZ5Yt0rAv6x9sgH2qsqXWzejQmhJj-Oyzs_DjDznoDtbKaJJT5zS6d-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP2jSztx7lzWHIJW9sEJkjra5xEoj-VzXlIvyuLA0lPGsN2QxDUrkb2gH2wISI-qzGzX2Bi1K1b2OtW81l514Nxud6dcWdDUb4dFqiWEeyXDFHz1i6BZRk1iAuQR4NzOQuKEcc-xlWWG4oJWz6nIpmxIiDHvNeUEp8GkkOTmO0PTRI--tyPoeOZ4lECnqog9IMz3qMLxDvV8Mr0FVm3iu62T3Avfdv-tkFS7z5EpV4a7d6U0RnJq71rWxt6aRr_ma5_JUGGaD6pHS_31YUdUde88MAv5aGlPwf9J-Zv30YMIvwAjT1VJTDQVO19LFtty2oIgmZ4U8OcYB9jTanqRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0-mzPLVr5IcU6r1iy4MVoQSijm9nT6C5hhbTRfH-kxR4Fq2oXsI5qD8MjcsAXwSLjVxoBdk1esKLwp9xYnKcZqUC1J7cy4bI226G5Wr89EH7M0kLsTOhPkg8QJrLpqUJXjyj5TUUhWW_9S-nzBv-SxMCIo9i0-dCg4YUQfq4-erGiU-qpf5LAEDZ280z3ZLqCj26yKkn7FK9RhPB-8QO7r07mv-yB3A4lDBIryv9p02YoNBoXiHAHPWDMPDshXBl3X4HDYaKEe00-UKlXDAZTWVSgOFTbyi2eRNhXryDGkKK_6B960e-Jdi_8I3nDBiWnGWZXOpmAQVkXIVc2d0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3SOHd8hSkIn2oFugKQis9HBZq5PsBXxAfxRlN06rd4C9vTDEiZyyrPwuZDLAhWElkq69Ecm37wwArVny6VQGuGXRqUrpybdm-wWQ4puoJQmoo_ci0G-TiM1kDZKt_CA0oyjtS-eZIYjn6YejGzMVGAwpoBS0hvg0Qt1yx3QMGMoTaESKQW9ZOyvsLrBIeweMYBmD1r0MNCbHCKfuDttFBiXqCdJdQ7mEPT81U5t4xUOZ0dGqckE-j1i_g-fYB3r89TrVNE6DxJxUc8mCwJa1P4RIbfj9VdGJLjUQLLNmZ8wZXn5nJhId6wogr_p_3EJhkLXTV__flKTdeb8nDyftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBbi5R31GlFh0xJjphimNVeUxji3pdw_3m_9fnsRwGsL3ERWjr2SNLX6CzWvO1FIC_z1O8TKh7ejTHNPIU5L13IZulV0kt6SN9JFkityTneA6vWYlbkDityFz2owo9HxRsHPMdeaRI4z3dAhfdVdv5jyTaD0BFkCEF3iJqrko-qBd2rtzLZCopTVrTN4OIu_2nRzAx6pgbVZPLFYMiElEE0LXd2rXoM0ymVjH20v2OOXbaSBjnA9QOWXCqQfyl-q4WD2p_47KO_Nn_Qhws1kH7UOV3WJx828dss69Lco9ggQpWZcI0sP7EgudhsjSmzjTM7G_6e8qg0vhyygQkGBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcMIxMX6DWllxhGemAP2JeLvfTpdkPwXIhg-7eP1x1loJCPwLyBVwTP2qKsQeXKHBR6ycqMjn5yT90cSEd2fmNoGur9yuul5L4Mc48_fbssgRGxPIRNwd0V6V0JM3o6oMCQq991KGALdxG2Vdr9bvWvM5gCi4D72mnk6vWqrPagA8kNJPr-URvM8NPq-OsB3Pa1tgQ-wLKp3KL5v7umeveHKtlO8SvQkIhb-iHnVp6QK-FHd275QAitKsm9qhaL92kF5vVqjFnI3aIbcftJ-s0hRZVhKk24e9Pm07nK0mpQZUh_P5SlohMD3SOUc8TR-5GkNBh9IFUNs5NKb44p2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m22IrG3uECZ_Q2vSKs7GdpheZIuHJooojDmNU4uGtce0L3cZZcLYP3fyOTDXbOB43V6PbcwDEYHZAgBAaCTx2w8_eZfJukYxlrZd9IGxyQjN44upTGTdhl-yrDkPdANTh21SGLb5VxXskd0BTh80qN8BqNqMAlOgD0XcXhByY6P7RZMhoQfNK_rBg45ZRsHiengcztx2cd9_TNAbbY-sdN4mYrfgnJ9A3LMuboUg_sRi_RapwzwJ2dZzOy169fdx0rlXmNAZR_rKj-xpGw1fYFAZnyjDbwhWAeI44qNlFjjyBfCZ_8kLBvhZVyxIoibpVfA1sK_v7qUfoOtSsPKoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0ngsffTe4Q8FHVlQW1bwT49_GXB3S3x3J5ghuNZL2V8td4IwXsd0JVv2JDkj-uNToDqUMotQcdnOBu9C9E_h3Mmqyg8zpm3OIwIR6xtWsGGuAPSsGhyBQOghi2ZWuqifugZ7hDR8RcIt-_Szfa-9ZY7RPmyxP3_vG5G8fecUrWviRWdZ8xrIibbn-7BVuimzwqW9rIR1JrLqUshPLV9MTfZAR9CKHIGZt8XCUnxAJUdO-PbgG4cqQYo_nkX842xN4I1QQdpvnfWCQW5zEGnO9qFatutun4dqEMU03UUknDKO_WHpZ0hVkpN116JPjHTn3ZBYGDqg2pYC6OZbPBt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3e4M5c5T9pHx0jAVAdvhZ4W9BuO1GAQwrHCAsvws4pLCEu9d4VpAF_hV6c66NVZg3bej3mR6jIUpMGAn0RNxjLt4nAi7gPxS4NNbZEnhh8RaNZ-J7RObsPyQTucgjHbrU_Ne89v-xh5wnfBxCQ5_NGJuyYhOTpgvfZByPikNlE5lspoun-1o5xP302gBczbKZuChotSvq8xnj4qsOFAZ9Lf0YsaGqIkyzMMnQBmpmT1bERIEIL8nuHdPv-Ybsd6QWEt2gbvpn-CZbm3NBwePLl4U0q4daB8hYC50kwd0AO5WuAaERBh3TmP3R-GiBKwChV3Z8R4EaOTJTdIgZU-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTcbveVMN-IeVBhxvfXQh612ohET8pn_29YwP6uIaj03Xq2kUdNj9J-7skdTdPsUJyO6aBpie0dbUb0mfuJlqGHueQg9Eg7S_BrXfHjV26WPxNJHnz0i3NJooFls2Cf6LZK2c_mAxzLtHCGDF-1yr8L3OVX163zBHQ6Rh93symHQS3YPsdeMgPjj4XsWdcWrMyoQbftmEHNK5owxdw30gj3gats9OvXrV7knwvm560SaApSoJKlWsnVKT7XVGZhtaD8j6dKTc15_9S_bZY_hbDImYJkQWGerPl34U9kTPAIWTnkt8tj2LkVUKAcQaUpfJpD0EtB1NqGPbfxki4KGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ_Q66DxMYxFfSRakpbp4WJwVh4arFVS4hc0bjCfhKL_jR9EMT_zKH83PooHCifRVPrNdfx13MhXLyjZO0F-xkqQ_4z5CSivsnpehDvq9QQY70fasDiCWiXkbqUiaL9iUox9Ji62AaHI-OBCv2YM2cUmjMKiYt7V5J5gnX92dyVavJQse-uC2m1nj_hSqD5eBKkpDwGv0vVbOZ8xB-pLn6V3LfVLlO06xcCZG5Bg3idT13wYE1tapYnitupYnMdYxsFFzawBdbt2F9XTKQLwBpnxoluuMHp8YR7n__onhzCvl_u8gP5TlUw1wHL-QsHzxZ9tGscCusP-tEM8owgXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7EB0XUfEcd9x_Xp5Fy5yAipHBBI9sfOz0VlGYVZZtZh4w0VDpKyLu0ONi441A85vP9oSo_w7_Klswv4osIsK0jY-BryoSVlSXdZt6cokgoa571vhY3F5jf8BX7FYlqCJQNsds2OJGeYVoGzZBXQ-C8fLnmr5a0pkns79y3jVGFm6wlmf2tgroCJGpgvKCshRlC6aMGPPgpfGCYh4qXUyuVXp9zbkosjZ6V-dhbnQf13tZoC1ItSMdDTLh5C8W-9z28dyeHHBmeL_NowffSzcslD-OgaCeVd6cvG0kaSS96kkZQWYW2CwyfY_cc_CfGiryaOqeGk08ZJMzbVZ9V23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1I0Jypg-o8bcpmHF0EHKua2xrdJREzjCtF_-uVjJ2hr6ymO37ov0O4RaNi59S13nYITW0vMDq3-n47QjWcHEJf2HtlL7hAxjaiK2XXqexVRwiOWpL_lL3rVfeWQ6K4QuC_2geh5-9cGS5Wsv6xGTGcciFAxnphiJzS2yNdnnofsGKrWmZEjmZuG-B96Sez8zCMZ1f51sVxKFgpQRuxN7wmIuuupm6VPkmLf36eyb0KQl8-MJ8e3F-8iDqWtYLdNfg5awPnJ-S_GNhGCfg_EInB30SnU8G0yddhzSg_eal-RK4DSxYWJD8nxXumhdRy3WpF0Hfx2U95G685iQE1WRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4sJ0CtzLor86AH-Vp-PLQdpsOoxYoGG-VJ1ymLaeaMDMIl2OzKEzF9Lr69Lg2n1Bkg_3hRA8Xyq06IZ42nzS1WtYhNtIza02Zmrv-skmcbDRzaMzAf-pCCv1fwrWczpQ1Txj78cGx2OvPQt5M0H290Zc4bjKDgWMWtT4dAVVCwK8nMgMjdm6svoA5Zf7Sh-A_-uFo6-1oWHfQfDfBrN3ghUFu-Bzo9uTQVCSZqXcR_AHowySGlHkCaoqdtRDWc3j8fxlFXC-qsgEiSBK3Vy_NSHVpNhxo6am59ffiUzP99u_t_-NOb7OSVbM7Nd52N0-vrFhChc43jigQSjqhqkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXB8SypnwLLQcVs_iyPMVpFiXv_8aNihrf-8cuEI3kPZHiuDp9NHh8-aAfcPIuRX21JTo-BeZ3NRjhBLeyG-eWzoqUAoIavNyB05tm5mxm-o2L99FREuxU9GKVKXfQUk5ub2XNFUNeA3nplGnu_F2SOixRCPglh7ioiRHH52JvG6gqti2anr4jy6weq6ov2hGzQKkAgR6_M8sYBq2WNvjTE8jPF96PNYFlDeSIPKBUQZmYRjZsbpB-Gj7khLBFxRBKCV9iVPnwV43tX99Y-cfg8CAdyfZe0iwdzbi0eVvt52PHPY9548IFgYRpLPk6w9Xcx8ewCYu3I7gkBywSRoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWnmTVTdr8lPIU9ftGADey0WzklnEgEqtuVpFCY23ZhHR4UTTIkXCPaTcfd2kST1PltxnmL8LOcjlTciFS6VPkJ2WYazhyhHtMYug_BTVlMutSBW2pOWDhGPZUD76m3huvkL7sEUpUNemSfQB8JArWIntmoBRhX1pgkPB1rK_sp2bLOj79RdaapzfppBQVe1MyPga7-tpesjjGyk67CENRezBS5wzHZ1dSQH2H0x6qLnrrthrPRC50Qi587Dv_vxdzRLI_wRNTx8sZ5avE8ua95q9yfNiQz0WiglnkYMUbpRkvNcbq9soIyr5qq-pSuw-E7B3y5caW5ySeHC1MOpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE6futvxFFi2ToEBU3VEPMJvgBWZstl15e9EBYSfsy8YEJYuSY3NKKxWS92eLIMUvAHOgC7397aV1O7EoDdVU6tTBQSlqVAnMZseKjc6JVMI6pp3VuNtMeYgZjCcNG5fEqw3xvspP_yP4Qj8daHbiSY72lnTWHXOngiRKRiJA82MTiQln822o1eA4rSsh10AZqhfEkYID6S9tAcZbXFzQeStX8PSZ-jqCTO5b4iGepDkTGEIwkJImUgpTLhk_jxOjQTAmqwfFGnvxynAZfXy5vurQ1v8qIE0WHmvthWFbvOaJy1tyWO0fSbqZgAN7xlH8Y6UYYUhRPoL3epXOIBmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee69JQ6SsZyAHyEDjkNpZO4cghjeb7S1MAHS4Q9Ke4OWHHybo_41v259dp9wQ7cvSpPx3ZPfYEpDH5I3ntmr4-doH0efb88Xy9Ok2srpXcfVu9d11qdzLvilYZv5R8wUC6TkpX8De7JBMyeaXtH8W2nwf2mgCCJREKmtpEpmVO67S4vpwBPVgpQFzUCIJi7aNdefPnUAzbPH9iwGtzEBvgDWGBm5mLVhgionCvDsilPCQFGLOYcUINICSYcErVCbmFyTPFDXvef8zxrTFj5dhSVKbpbmP_c8pTjsqPyOhwor--X5kFddMlhSN_Pm2NnBngsw3wvhrxu3hU4jgLn07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcqlmwuBuJEC7RzJZxJ8tlqFTkQucZS4E2rKQATls0UygrzsmR5znU29I4evbFidnII6g2HdEH_KFVocqYspkxX13ne2B98el-EsClALfZlxWf5YokZ70GHAc_PtRzpc1iopPFgKbeshIYA28njvQBAi1xScTwdtAvGyDHqUg2yl23TM5V1uvPin9zrn3ATs5Wfhsz8Xo2eJumzTT0hVLGD4KXpsgukJK3Ol8rhsGsJb4QkUJCBs7Khhlm9E8OfnEQ92hNT_cgxR_moLCUYomEaiZjZKDfEjUxtFPpmegoERaD2VrnGCchDv-2OWoZkzuJsHDQtrN9sM2u_FlaLQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e93eDCpATonXiR9jRexQ_QIICTh5vtVyPppo0nHvNOzE4auFfaCQYgyFavM9UKIuxquMpXlMihkcZoZ-O8w279gXqy--pfJCWoISzLGfKiCUF3hmLj-dZ592SrZ5TVR9mg-vC5qoDyGcC2TQqDqIcjGw5uLCU04LYdLFoVEo-EkopLkhUJO_aO1AzTPo1OmZsSbn2qoE-U0gDNH0P6lbf0ZWLj0o0bhEs_4GVm9Ihq1qEEA8qVaM7g_GjJtZvEV70tZ_YB5s0Bh4rivVPA_3K405ubr6P7oULg8FKZLGDQfQ6RK80FZX4lJfINVE46sZLnDpVla2B87VHEUSHI-8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKH0m_p0ovlgNHxoZODUVg8NyTGq0R3EUZABS16A0hvhdrdOh-bp-fYZZ1GMhNUVEgMrlR6nH_HIN5A9Ci7MaHEgbHHRqDHmtVvAgBWItIqw5WjWR0vCtnRHfX60tIvKXEBy8BH_41pLo_-iugyfEURAvApiaPzsM3xr3zTh-ZuE1TaxfAoUBe10vpbLtwxjVVmP0N9hOaS1CxWNNlGD_gm0zzDbQokuGme0uhy2TByOdvyoM39kcTCpRboVCppAS_vdvDuwhFHf3GBgxRnjiVOeUrJqu1wIyIi09x4aWXt83XdpAN1xV8EBHls5LAmjcun9epL8tJrQ8vDMXGV3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIgdKtI_AhIZAV6rtIqf4CpZVWAEvP0exfciJb0vptdZrFJtBGkgSfuLrGUbXr2hcDIdQEd2IxlvM1ToMAjt5TCiLjlJOaaqlD_oTIfZ3FuvGPHMc3E6OSwDQ5OSMxqMKpJ9n0DO4fWBi1YLUckVM5PlaiAtjNozsrpsEOe0386M39Hqvf621V8nKKWl9koloYqfS26S_BT4T5G152skbIxw2S8uGBAd1ffnMmT_-vrh1GZjD2NwRs_dd-8jBZ5SV4j40kmpW26jIF04gtc71d-v5GIa2PVwQg5D3m0OHTdf8UUtloyXYOfVw6RmpxfoUYGk7-OQEBzfasy2uIwlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6L3O_yM5DbcAK0vCRwii2N9p-pt7fO0kebds1UHO18NzL1X8hjFBo_jfUy4paZdrPgnmn-jVq1MRHrTZeaZzZ43x4Ahy9m6Z5IAxrvb1WEdJ8dLEayXa6cpoLyD5HBbu9YmuE8SiYl-acnN5eJx2Lf2i2DghbSQFdRTZHVgih3fI8QBwTfKGczRxtSonreAYL56qUNgDGF65s6PhfCxzKcmjgLon9tQqDYqZfnk1lxD12J_kFSZ9gRvnmxtg7SKdcVMfX4VSYQ50MrJ5bsBOpRq7Y392vrgHgsxQlgCifW67VwQLjMGF0XTlGRfslTWKPIB3elgWdydb630C38DCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImZPeGZL4VOlLspZT-YV4b7gTQm2gH1zl_m8U1e1fwEW91tT0uifkTtv1ZuZdfl8zTYnwzhdG4naKTTikA_uKEEsgdCeyD4j_c5eQx8sBj0CsGyV4yJFwHG2Mo-O26yBVrbZEw3M59WKaac7dCSoIHNta7w2eqPRrZLZ7FNUapFnuonuqI_g8ZmInR7vK4Xx_ARAKjfm28AUkziL5wznQ05FOEDVbBO1TEmMGih0ZpflUcA4T7swAlTM18p8bSicgm8iBNOhVbO4zeldIsJO0-mis7hmNw8xjFwS0Tky6PIN6EsPmyjnH3YFQ3W0u54vef__XqAJaWV8JbxdoT75Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1h537iJjkAwZkAKrYJ6T_UFrwNbkIuGZMFRWnW9kgAS0Tkg70eC-PONunHU8qtWT3BX_ADzvcvFVE83AZPylxfH3E41CjEcXNTaXuOQNCNiztospSawNoog6FBJ7Jy1yFaG09OZNz26zboG0PZAm3YtRePnC4QeQvqgcWqFRNFPjhGzNmOgJjCMq3W3tbeksMaoZQiXD8aGchIS6hh-TTabKOfJiLXSuEWXpFFyuXArIjqA6zFiArDJ9YJkk-hBiintLQY45B-wJUD36l9mQG8TLyqAs_fAqqe12RRsoT1yOMe22dE6b5MX3UyNYXlIAH6hUqrQoy-WsnM7kIYWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raxStEhMYYQXqP14GA9i-HpAPYK-WheIpb0UDlQJNZ4LFskyGlxO46myXLs77p3_IMiacZQv8qS2ZZwpxnUrOBZfmQHUdiX7VrzpR3GDccYnTNNe5rm4avTXOjqxsD0tRew492l4vMDQjBaeWz9kaOw-HQCAt2YB-9I7RADsva7_XsjQSFGtTkKehLoXZCbW1ThlrEQ1pBPACkmuTmsAuhmSxnHAjNoNLcSGoOVOEpWaEzvcjAIT-2YsHBtjn0wD9xQpwgOzVhpxWgaPX-BOmTqU05cmcy5f3euXU_Tf89jAuBpSkqwmyLtI5egi-AMvhoHPI3pMU27Y9GmVZpUJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le5ZFRpNIqBdBjyHLDXYaMsrjEMq1qEXk6gQ8ikmBD227nU0zATrIcwUDH-b-uMhuNDB5v8m1NjCriXgogL5Q-zk_JkzgPwYRvJEbqkXESSNMP78mVNOL-Yfv9LV4wUNGkwMl4wwiJGXM3vxuib4TvWiY8SFZKw4iHGof5eqiUL2cyOADZOF9XODv69qMzTagISU6CRN-yLtM64yfVVSY3BtugCoJaS2vC174Ug6HluJdNwsCWEoNKgyhn3Q8w0gu4cPErM2svFCEgAHO9iHIy9KngbMbEiNBrmXMW51rmi4KRAvYQhqFbaqbFobPb_EOfjd4TRB2hKfcMcRNfd10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2_shPZ37yRdx6VjTmZjGTZconSVjAuBW8OItk-WVGsXPWrEM4Fnu7CNJ_SRzrm4owQPsRLk6VE09qbCNcf1mDZ4C9k0uwLL-9gdCiAJwt6Mq8Lv47uEtT-jurDLWYedL9LntX5bvItPHksoQ0q_svn1S3pG9Wt1XQO1jsYJR-yX1Y3EJ1mN6Dza7ArkKgVJSHv1gL0sB2xo63wLLav4en2XMvf7-eZDnHSZRAmEgYYtXcRoZyjDJ6u-CxUejhVZJxcDjmah6nbm7LpbJPK_cxPYz_b6vxrzWMJdFgbYFX-fguhKztY7Z6miqdk555anOVcGx4cldDHubRI5Xwbk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi0toEWnmxIijgQPW5zahTlzqrrB9rA9K186Ox6ZfYNnvJhOJ-I6MFb7C822KkZ6De86XwrInxp4jQmK4xxqKkdAcX5dVqGo2kKVmgKG3q-PC_SAXsoM7GFEWbqu34tfZmP-ThEK-g5ViJWQnUALY4W0NbMGXa1cWLzPr8P8ulrFSEnbYwlVa3hpTiLLI4cuhNPH3TD9u5DZt72KYjn26warOKwEuzfjzvGjwETfTes86O5p4gRy7ts4UwpbgZ_kcE52ZmyB5kEB10sZ6pUc5aEEd-VH54cu918i-bVjRv2a9TRrwdI20oBjTnL7NAvGrCObm0F5DNmZHcABk3J8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=Ob3F_nt4jFA6RYTPWQaeWqIjUFjkox-HXhJkhroYwSz21qrUBexejenArUHEq2cfUYJ4_7mntnW6h8tqTJkFzMvrW7FTS-maLzjbqq20Eh_4zqc2pV0fRY7dslxO-xULFsStJ_nMpkwiTiZzSfxmuA5kjdQvcwjzR1GGsj_2PDdzEKcFXKM3x9dQg_cRWKBS-fgSxgsOTbOWfipQoFlI5McMirjk4_y3ZibIwRX0xqH4KV2yecW8aeG7rWnVVlFTtC7VM-ftFtSunRB7jEfr9Rs5uC3DSXGUyoDjBsx49yq7KSTVOZHr7RuRQHemrMT1fyAj_s7P1aD9O-kjWkjLX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=Ob3F_nt4jFA6RYTPWQaeWqIjUFjkox-HXhJkhroYwSz21qrUBexejenArUHEq2cfUYJ4_7mntnW6h8tqTJkFzMvrW7FTS-maLzjbqq20Eh_4zqc2pV0fRY7dslxO-xULFsStJ_nMpkwiTiZzSfxmuA5kjdQvcwjzR1GGsj_2PDdzEKcFXKM3x9dQg_cRWKBS-fgSxgsOTbOWfipQoFlI5McMirjk4_y3ZibIwRX0xqH4KV2yecW8aeG7rWnVVlFTtC7VM-ftFtSunRB7jEfr9Rs5uC3DSXGUyoDjBsx49yq7KSTVOZHr7RuRQHemrMT1fyAj_s7P1aD9O-kjWkjLX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg-6V67ylP0dfQKXjUP_3OmVAAmtU5UwUNCcaMWYZLAF-ADrNG9s0GN-2me32QD8aCysh7OlGes6BPjzovmCJpgRGlNL71wpQvxB1pBhagU7bHbpkM8ae1aOe7D4ihRsbGC-bYSoDbEdMP88Z1papF3gw_uLTDX7l_JLrS_jz3g_0XVvBvYtKjFWv-OQ8uqLMy9mQp1LGbn6U40Why716CSbuxF-JG2UhODBWnQuPX7WMT_3PUXZmYQergTf09TK0uGzY9jb2rWOSQ6sXzIPIKSmvleDMSsSKs2NnjCZN4dIdKjAgQQjlfEwYEROZ-xWJjvOe-JbIcn7J2X3E1iO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=XRAo3EjHT6xAu_bSlof0mXELSQ_tCyqM2NyakfO-rYol3JNXjkx1shbHFcPnGECPPwilS97t5QCIQhwSdPgn95-zlA35x-1VRjcRncpQpWr4PQS7Dx30_KH4GTCIzZ4y6S8O5f3VaE9-fm-a9n9hFkHmWNiGy_XEwpec4_Cn0lsb7pq2-0SroH7aocwSTXooXlSaVc_em8i65lo2QgtPioSxngwAu87Su5zxjhwhQRukyXiNtOtTF2Nwem15rznovvkjEHn0cEY7cFWRP9T5TV_t-Omr3CrqQZnE_a56TlSqfCwyGtKx9TWCLzVYQ2pLZxlCvEXuktmW8VYONp6FAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=XRAo3EjHT6xAu_bSlof0mXELSQ_tCyqM2NyakfO-rYol3JNXjkx1shbHFcPnGECPPwilS97t5QCIQhwSdPgn95-zlA35x-1VRjcRncpQpWr4PQS7Dx30_KH4GTCIzZ4y6S8O5f3VaE9-fm-a9n9hFkHmWNiGy_XEwpec4_Cn0lsb7pq2-0SroH7aocwSTXooXlSaVc_em8i65lo2QgtPioSxngwAu87Su5zxjhwhQRukyXiNtOtTF2Nwem15rznovvkjEHn0cEY7cFWRP9T5TV_t-Omr3CrqQZnE_a56TlSqfCwyGtKx9TWCLzVYQ2pLZxlCvEXuktmW8VYONp6FAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk02nmxRV3J4U9iDn2UBzQICsKqIjolunvZTqaPEfm1BZoa04WJHqFG-kY263UKO7_rDNnRvw3iZuKWwtCDtdfbelLCD0waLtVAeD_84CtvQMwNUHMf573fffXP8eyahenmRnY3xiXjoOE2FBPoUJPfPpbF_z5qzh0DEfjv6dO6qQKbmxf47BP4UK0AnEDJ0RsAzhfQSBQpy-VpXsrZchdics5_rOztRYZW38j48fcRNxxmR251nk6wt6Kd9rpfzVOyyM0hpIZL1LmgislfdKbOvz4Phx8zaJ3Xq8ebDQEjmdgE-MlCvXrBXn2lRIxwzqOjMA7PmW1kisp9YMw_nFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdglf_b_oMtC3eMvEXj27UqEE8Xf22AtgFirUkL-611zxEbLqTr0FZcOlE5GaqIDosAwYdfSCr4lDNAT5hAwtQkZ1GWkSjG0aNI1w-gmCU_d7inl1dhGQXMTBMkJqiYvUsdNmVleZeuCAx60bRBi4R1ipqEMe4h6zj1euqnvHBYs4zJmb1_aAVCWinjndUSB7OMWVi4xqF1ZgAcY2HwSaYKLtZxw7PTepDovToikWggGKk6-UPUqKjLNm-VotDAGJLDNpJCmDsbXKZNWbmyEe2PnsucLnStPHUCHKxzIv9rIVXY80jEF2cnliWPHjb2jLs3Lr9V0OijCIVUufQThlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ACmCfEBXEL7rFtV9dWuUtXorKrjdQsYwndcmHBN1uiLNnTilyaoeHvu_3wHRfP9TkMYWvT_ZjHjQQnmVZPDBy-QDHanXLn2SmZhTxk3sYogk2_1xB9xhaPEt4mMMN3MTolxJXo_eLVJLHeltlg3cLt_VuiLurTL6NOuaVthGffUrqArsD03gvgyRekjf6bwFVSP7uo-BRn991sGK6i5KeWtHLvIqokciaCmWTyuFZz95N-bN16rKZ-_OUNwVHZ_R3J8dcdwsPDIsetba8YEuBuJ97l-tIbl6lCDeL7Wb4xUP2IxbU8Tw6KGeIZdMttRNrAm7Fs66jrF7b1b-4XMpGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ACmCfEBXEL7rFtV9dWuUtXorKrjdQsYwndcmHBN1uiLNnTilyaoeHvu_3wHRfP9TkMYWvT_ZjHjQQnmVZPDBy-QDHanXLn2SmZhTxk3sYogk2_1xB9xhaPEt4mMMN3MTolxJXo_eLVJLHeltlg3cLt_VuiLurTL6NOuaVthGffUrqArsD03gvgyRekjf6bwFVSP7uo-BRn991sGK6i5KeWtHLvIqokciaCmWTyuFZz95N-bN16rKZ-_OUNwVHZ_R3J8dcdwsPDIsetba8YEuBuJ97l-tIbl6lCDeL7Wb4xUP2IxbU8Tw6KGeIZdMttRNrAm7Fs66jrF7b1b-4XMpGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXwDtJlOlwBzNAMDycydlzOkLSazYHxyoz89i0PgSnFhf8LfIE0KsJJtaf-JnDVWDHfqQIKFXGM1_jMSarzsSs3WpbryhEqN5fyKu0vZeldNUPh7NfK9doPCaffArtzo4CcgHo4kRU9afbZUi0dJjsl14VxkQBALw2zpo-CnCNtc2KEeqYjjLnAImz6GEur0aAYUPstTHftxsLCZFcL2G2JCvWi-y2OVt1zdLDfJR_FadSzLC4oqsP7GTVfkd0rqAdo3--jgCGi0n6Mxd-Y5Jz9NOagqgKEgRFLSuCLtnhb2Ro4wml3439c3BOtjTdbxGxn_nUH-b8XnWQ3WEYDevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ca_k96ZOWFHnOijsXGDS-YO3k2nLzVQ7RQF7KvqdN5vuKUL7xiWMjPX4yH8DJGuMTR_tlnNZwhNzxEd7dggPZfzUIUJSTOxa5XEhmeIV82Lq_BDH_nQLCF3hqifzXFF2U-t_GAN20eAelI8F65IqsXmeqL4Qq3x70Jqz1jEkTtmWStPl-XaSsOWvprNhZtry6uXwC4Kz9dGbA3neAj6pRx5EYxQ8ceSr8pbtl3kOtpcmr3Qqlzlqf0pmMmiT96Gvdj7Muk4oXtuHtJQsjWwlo9HOMcK32kVdOoD2ra9bjiOCr6mFs5NW0LI-SheH_iWpv5FGzJ0zLRel0wnEeQw9wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsbYmAt3LVB1jN2S5hOM9ZAUdzY3I0YBfx9kHRNDOlPJiWnzBJVacn_KAWhL9LCWKnvCJZceDM0fC0vU9HYBAU5sWVb5-KZezn6znRGF-4jhu9CSa0NKaBSLUlxsAU9JzfixOMPp4xgtBIFxIc6TtOaFjwgWW6rKHYsh1Ml34WIhGm-nKsdnSkxck63pFYpCVLEGqfjeTSpem-LQMoDdrReaS8Jn1h0bHS8_QNJBBvYhGAHnGe9jG2-4ElVfqItzG1_SYDctTIi9t8VNHPQN8vwn3rOTls8dtTBwWgZBtiDoThOko-yR9rrrIUyOMx_PbPbfxOU68TqPxdzadflWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=fOoA-pXvPvTB7_zV4lwN97GovrfBxJlbkjG9B8-87jDsxIDF7SnKovBY-Xl9lpVaWQ6HKOJWhNWlO-tSm-AuYpjvp7y2XwIBGvjxxbfQ3OzJUYkiTRIVVbPZu3cGk7YLCwb7f2Gw3cYrxQYE2xt3mSGMXPY1lwu2msafQHNBVSzWzcp4h0kCwtTXqvOeyKxc4MrFmauRT0VvtbyErOIq-LYD_kuA2s6JCUTWRDYneoC1VszqmNLBYMQ9Mi3OCmoSLpsAjZ2OPE4tCEPAU5ltoIj7r-aGigQNLEwc-rkOmf-IFO5DL-s8_lA_EqcHTAKaHvqfXWiOLDwmEfLSHdg4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=fOoA-pXvPvTB7_zV4lwN97GovrfBxJlbkjG9B8-87jDsxIDF7SnKovBY-Xl9lpVaWQ6HKOJWhNWlO-tSm-AuYpjvp7y2XwIBGvjxxbfQ3OzJUYkiTRIVVbPZu3cGk7YLCwb7f2Gw3cYrxQYE2xt3mSGMXPY1lwu2msafQHNBVSzWzcp4h0kCwtTXqvOeyKxc4MrFmauRT0VvtbyErOIq-LYD_kuA2s6JCUTWRDYneoC1VszqmNLBYMQ9Mi3OCmoSLpsAjZ2OPE4tCEPAU5ltoIj7r-aGigQNLEwc-rkOmf-IFO5DL-s8_lA_EqcHTAKaHvqfXWiOLDwmEfLSHdg4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=E2N69_CiIWbh3luzXPQvXBgnvM4A1vTxh40VvYXJsaws5NUif4-DqYRiMMIU0rUCMAa-IRMTHy0hsVTEau96kwhiB0f6G3IDrHuM4b9vczhrNHtDKuIwiZ-FhkOJ8oBRjWN6osqfOWqekwjDM6Xq8yaYa-ihkUPfrwUahw9a452xAWV4OxoTqgCekBPUnTzkCXKPppLEdv0jg-_wcw8c4pV3eAvFjpSy3X64z7hVznhEWmUf8ldYnHXOFMdb63ElksfET7iGgC4s2xkHuzOHkKU53_P5v_gLepjdrAc_lx3uQnM2jPNaCyvUJU6FcUQyGwg3Kn27WEEnYUWloIZctA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=E2N69_CiIWbh3luzXPQvXBgnvM4A1vTxh40VvYXJsaws5NUif4-DqYRiMMIU0rUCMAa-IRMTHy0hsVTEau96kwhiB0f6G3IDrHuM4b9vczhrNHtDKuIwiZ-FhkOJ8oBRjWN6osqfOWqekwjDM6Xq8yaYa-ihkUPfrwUahw9a452xAWV4OxoTqgCekBPUnTzkCXKPppLEdv0jg-_wcw8c4pV3eAvFjpSy3X64z7hVznhEWmUf8ldYnHXOFMdb63ElksfET7iGgC4s2xkHuzOHkKU53_P5v_gLepjdrAc_lx3uQnM2jPNaCyvUJU6FcUQyGwg3Kn27WEEnYUWloIZctA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3R3pENelq0ud7hSIbn3fCe_jL2zl3QHVcmRmqBU5N279bHALh5cWRRSBCiX-37oUlq7Upb5p8whcTIJywALUCeb53oCE_iXd-OmNWVHbVWQrtUdWIjz3lPj6kgqCkFn_2P1rgOHCeuBNq9e24tm2wJPKDO4sCdFgr02foFCXFrPRary4LKk7SkaM-lKCfK-JTZ5aou1nP0cucophplDeO2F5CRYEyGFUSDrNWn5V1XdUGnt85y7-2qMXX_l-ZU5V0UsfaVYx-jlyw1w-UgH81Wanzurdp9HuIB37bmFVbyTDH3vLi1n9Yt1oj1y-7Z6ESzn6Evm8Oio7ClWLPF8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=YUuWLdnLI7IKRchbNSZKOfplfCflV_w_zfe7tYOnTFbwAlfG36ONchTQY1_hYKE12KtwQSO4DPrqqIYoBCSWkLeUyEHNA0tai89Wqq3w_ic0C_tDtxWMBABCRE7vc8RpF6dwqruP_-Y-JTtWEbrQN_kBDkkX1alUNSsJWcQtbNbhrgNbJsY-OMw9sN-FaIEch5Is77s0HZVbLdtNvvWo0CzqLZqi_XOe3maLcZlWVNDbzqzHbAWUnD0fBzJMQqT6Kutet4rI2QPqB_QbdGC9UJlxYFMVvMEUj4kLEQWMBtS3sG0Iqq5useN2dGQ_HmRB5Lz1X4srv82LvoMRimb9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=YUuWLdnLI7IKRchbNSZKOfplfCflV_w_zfe7tYOnTFbwAlfG36ONchTQY1_hYKE12KtwQSO4DPrqqIYoBCSWkLeUyEHNA0tai89Wqq3w_ic0C_tDtxWMBABCRE7vc8RpF6dwqruP_-Y-JTtWEbrQN_kBDkkX1alUNSsJWcQtbNbhrgNbJsY-OMw9sN-FaIEch5Is77s0HZVbLdtNvvWo0CzqLZqi_XOe3maLcZlWVNDbzqzHbAWUnD0fBzJMQqT6Kutet4rI2QPqB_QbdGC9UJlxYFMVvMEUj4kLEQWMBtS3sG0Iqq5useN2dGQ_HmRB5Lz1X4srv82LvoMRimb9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2OJxRz7s-M8UWz43CInLRHUSCrA-fm1F2ildqMZDqvVoLvLjd0epLhttnt0VJ0ao6CXDLrfCRmgMoIv1UBih37A-LAmpuukrcdl4eEXNluoTv7ikeH_qwasOlo6Xma9R-rutqYzFjsofd_ZGczQLSdVh5Ff4I1GQ4xdsPxDQ_S8eAVS4iY0J4QlEJI29zk-NVB-5-Y8ga6bDVfW51HIRZyJ0Ka9148DUSujuxPwiVfSmaRf31Ugt--Wchhc5_j3ny8VgVj89kTQ4HyBHK-vsWYl3Bc7Z2XGOGa0RhnD4tF8_9Fuw90Lu5ZRHohff2DB0RMia0Y5Asx7TXfevSy3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxuJZC3W3dztK4gvT7Qb8cUkZUbchrcgEDkykS6O3W38VxPoEELa9Ob4EjV0c53VfmYndo3Rc_8qpLD5bi3zflob0DSY-xAHNDOj3N00NJWKjyU8KNXu0UjuoHafoxlt2mdv8sEhwW9Vnujh5O7tn6wb-3HMYNFV0f4RwhFw2A6LKTeUmBpYoUS4MzxEtK4kvWAKAdq2B-y3MHpwrX6eHcNhXkGMwgf-EcPOBWgEK36Qty-eq4s9e16pBjsAM2j9oOGfuBMOIPKY0dzYg9KjdVwNqQKlVlQX-2DwHDcmtwlE-69L-90Yzu3onDx3kjF7ITsTbXJ2mywgPv5mLM0wng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrl6_aLmHecEp36YUlMHJngbunuPj5fH4pbTpusXY7oKDYFi37mhmD1bNDGCSlnzjYvZYwRIjl2i6KOLo7FyH2KoD-fahm79WnEdLjKs2p505QvgdZFOgs_xRIVkP9iQRpQvMvbPD8oFaMJ8tbsQhk-3QAWyonWoD6HMhMcZrYvjjJ07TGqym5O_ENQKHvfiACDZbOR4ZfcBhjcxRIpMG3A9m0d1wL5tgrqqVsMU9SKlNl6jXJutunZEEdehZfK69YdUL8wHNfkz_kU3UCGj9m8IkQvSTqS4Jd0wYddlrxB6oSU5ebOaqQC8blc4egUz1QNvLyTRohJjKHmmd75y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHkKWoIxCS2PmylF_Nwd4odGfEHhNF3y66T3_qpXJzH2zEw3iE2XpFXy0E0fmmuhlPqGWXTeZwx2TxpNt_tX-KUMhvL3L5sFyuKngbRzyUUVteh92cEeA-e_b569eafKPfHPLMCWusDCGXvAqiMoo2l9B_fgZFwBBg4yGBsygtuK4aYPsgv4442bwOWtDh-mKqm10DBhOPMrcTo-eeoefSo2v0ijnpwpcxwyRFK77a-hLJYEmGP0S7w2uPsl_Ro8zeiHlp32A33_D0m9OcVbUhIcPsWQZWz7S0DVQVY_0zlHhTgmvYITYDtcsNb0gIBOvBA1NUS2s9qADOA_wOhDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irXaqkelXDK9JCmIaPBwslv89LmqsZgWoSUfw5_TbxLOxXy-gvTybYm5sDorL-NLOeXnBlkYNDlepiGQI5iqPos9Th-BGRoB93-SrzZXzSHMbMgWCOJqERwdLGaUKJO4mVVe--Tda6hdMYi_Fqf9Ceezkzj48CNjU7SZgVUXGAbhCbEbkN0uM3vRdVQYNDS2CvKehCKYJ96YTYiQGiZljG6kphkFyp8frQQPwyhEYn03hiD15KOThTKieXO-L2e3KE6tcxMdA5IvOlPXSFwaXoHsxNcYQWNmnBrKzLPPVh7lb9XSyw9fPQ5jt53FSIKjh-q0rLnjggnK0OQ9RccLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=WlxangUDmA8x6urC-6mAzfF4IpiZIbSsSfS5O93aDD4AcKYnNeSe3iOVVXhSNzoS6Ct1M1IR57sxvXBgH9VVwQ8YQbmGzq_b9txJ55XlhNbR6-KiiL4WHRPdkofhZBx6NvnBZ_XypM6JxiOXTJoedC-W-bIvzPR8Z5bzhh8ngY9Z7NFOd1p2_pL5TIpSstK6ISa8Fjks-jY48cpMBTXjiBMBUFGdBt-UMWDcfQu3H3XgygWolHqjJMANjE2hG7EsAnWU4hAdDNLZ-vkuTQ7y4vvKm6CKkpVsNWeDlRoOUEcuSFfy5bnNp70NQiajGb1A_RnPMm9x3gRUJaLFtkFKcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=WlxangUDmA8x6urC-6mAzfF4IpiZIbSsSfS5O93aDD4AcKYnNeSe3iOVVXhSNzoS6Ct1M1IR57sxvXBgH9VVwQ8YQbmGzq_b9txJ55XlhNbR6-KiiL4WHRPdkofhZBx6NvnBZ_XypM6JxiOXTJoedC-W-bIvzPR8Z5bzhh8ngY9Z7NFOd1p2_pL5TIpSstK6ISa8Fjks-jY48cpMBTXjiBMBUFGdBt-UMWDcfQu3H3XgygWolHqjJMANjE2hG7EsAnWU4hAdDNLZ-vkuTQ7y4vvKm6CKkpVsNWeDlRoOUEcuSFfy5bnNp70NQiajGb1A_RnPMm9x3gRUJaLFtkFKcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=nsI719ssPorKIbnnkp4DFEzDD5NTkFpT2WETizcRMXxhVUzQcv6Mku5qEkL0gVbubuV7IcWblTb2Smng2_b1nb9PxG6eW9jhqLNKU0e6O1xJA-QbrKeS-GtMe6jiDP6ywuQp-iPdKIi1icScOD9MDQW0BQB90H9Gy_7P1TYmIM4xUMYmsJu5ifPwTrRRJOG84MTqrHglced_8HR9pkgHGtHkhqwajCMF8ZPMPDL9m2KOtIs0xw70qy8YNR5nSsVKekk4JFHBDahGWSfaK5zKXztIG_k6FSgJwFdhSgWaWQHiD1KEKEQo6ASVU-b_A-YgqTRihtEguq1s63uwS7jwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=nsI719ssPorKIbnnkp4DFEzDD5NTkFpT2WETizcRMXxhVUzQcv6Mku5qEkL0gVbubuV7IcWblTb2Smng2_b1nb9PxG6eW9jhqLNKU0e6O1xJA-QbrKeS-GtMe6jiDP6ywuQp-iPdKIi1icScOD9MDQW0BQB90H9Gy_7P1TYmIM4xUMYmsJu5ifPwTrRRJOG84MTqrHglced_8HR9pkgHGtHkhqwajCMF8ZPMPDL9m2KOtIs0xw70qy8YNR5nSsVKekk4JFHBDahGWSfaK5zKXztIG_k6FSgJwFdhSgWaWQHiD1KEKEQo6ASVU-b_A-YgqTRihtEguq1s63uwS7jwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6H5SINOeqhe7kMaPZLEmLbGtlc3IHhSw9J8N8Bq1lOW47-LspUK-7MZltnc-tX4_ci-CfnYOvYBGLh4ZaKoT76f_FQRTkrSy4w3mVrQcaxi5j1uv-t6J9b0ZUUmLReDjuq-z7Dje2vm-BybNPHPqw7zE1HbrF8DSwlbcOc6WpbMBsKLhkXdi2nd5e7ZIx4YGJYvzJw_Y-hLGw-ZPwZB4RALTESIO2lGu7Y9pWCEGmuKG0sqPo4x-QjlKmF1alVzZRDvCpWYjiHgzRwy6xCr_M5WeodCtPTFggO_dSsNx9uLGdZsW79N5ablzD3a7-a5PscddWJMpIfqiMzePzl0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=OyL-FRLS-w2bN-XK8kzmq9ThdFOpnLxpi1kksg2uBFy4qD952sJbVNQDLI4gw7xtQzAO0aDc02GLTY8aoyhlf4neGh3n-OgIm850s5CPJ_JQa_ESDVplxhZIxXW31D1fIKKfAh5t1mefXrhIr7fVvKSKQP2ZqQvL1nm2vkFc-4WH1KH6vyK-XGR-QCtFnjf0q0FfNtwNT9QWHvnpAY4EetUSMAwRBw9W9t6WYDey1-dUoRQovdPJ6UbKvoWOR3l4xmpOx6kcu2CBvfqNIGdGSs2wOC-GLH3sb5DoNFF5kNCyBCi0GVDI4-SLlkuzWSEy5q_q-jkI6MuzYG8LYljpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=OyL-FRLS-w2bN-XK8kzmq9ThdFOpnLxpi1kksg2uBFy4qD952sJbVNQDLI4gw7xtQzAO0aDc02GLTY8aoyhlf4neGh3n-OgIm850s5CPJ_JQa_ESDVplxhZIxXW31D1fIKKfAh5t1mefXrhIr7fVvKSKQP2ZqQvL1nm2vkFc-4WH1KH6vyK-XGR-QCtFnjf0q0FfNtwNT9QWHvnpAY4EetUSMAwRBw9W9t6WYDey1-dUoRQovdPJ6UbKvoWOR3l4xmpOx6kcu2CBvfqNIGdGSs2wOC-GLH3sb5DoNFF5kNCyBCi0GVDI4-SLlkuzWSEy5q_q-jkI6MuzYG8LYljpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=iLpZwm3bnYRO-kCQgie4qBzsSMveKxh_F5W98o3behfvC3AX9HIZxDhUjjdNWRjs76__XuAlsl2-IK7_j66eFfm0ZQVgvZFKmuKhmb_9FVfx4BigaRCX8Vfhn4w_N3Bzot5uleOBpbHODejSgUeeYODhAgdTL291cWhmz0CM3dPN04Yaune9f2VE_7jABCpwKiZxcnHSNAZVFKtkYVqmNJyypJXg6PWmB1wylCAUy5B5bMt__Dq7P-CuYbTbROpeVyFLxCQg3sKBoHdNO3hRxWWsnY7yV8PJf0HSMWqpoipR-Ml5JNZN7FjXzPiX-hov3QcOPZqz6LSrtf2czoCWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=iLpZwm3bnYRO-kCQgie4qBzsSMveKxh_F5W98o3behfvC3AX9HIZxDhUjjdNWRjs76__XuAlsl2-IK7_j66eFfm0ZQVgvZFKmuKhmb_9FVfx4BigaRCX8Vfhn4w_N3Bzot5uleOBpbHODejSgUeeYODhAgdTL291cWhmz0CM3dPN04Yaune9f2VE_7jABCpwKiZxcnHSNAZVFKtkYVqmNJyypJXg6PWmB1wylCAUy5B5bMt__Dq7P-CuYbTbROpeVyFLxCQg3sKBoHdNO3hRxWWsnY7yV8PJf0HSMWqpoipR-Ml5JNZN7FjXzPiX-hov3QcOPZqz6LSrtf2czoCWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
