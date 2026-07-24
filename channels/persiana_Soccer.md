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
<p>@persiana_Soccer • 👥 568K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 22:23:15</div>
<hr>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsk0LAIjUp4S51ichYWY4t30zvTj_cBdW5TyMHYdGUGVLdP-sqXLp-uScTMTKzQsvBJEsSpqpZCQnVdi7wQrElvKlnU66u26GBaIETQVnbFlsQr1luW73hhECLWVdzqbeWES-nEw91SqT69W6nPFOHoaIn0BryZDqpJnmSB_ucRQp9XYj4kis_87cuIjbdsuTIlGuNBOLXvvt9ciW1eMmW1urJbg6GJNBmss9zvEg179vtAcJetdN_xAejY302btV_2AXLyhE72ioZYlpExGtu0U0fLksOwFPrOhP-9uIwkv_vCIRiUUG5U0Ry5lkOYhjjx8-KItWUkuaxwvMIts_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmGVRUUU9nm9bQO1b19kdPaxBJphKpPn5sc1pYe9GDxvxfWu6hhIUgMTZuuOGuDz3H7i2UQSZsP2a_4VaIBd0URdA9rr-UdmeyaGUeE19YC1bZ8eTQYN5JcBXGZXrWh4FTK5Fs2hzUSsmFY64to9yFxDJlrHH-HrfczQzSqQnsu7CAw7xEFsVs8Be5oh6EvhDnrMsgHBt7QSDgiVJrkFcPQ6LB0FjXNpAPtNIZwJk2bRMVM53qPr-CZQaRf0WYleuiEs50IlYwDuO4dUbCXGASHKO0U3tUb3Ov8D_9k6FAkcr0YfymGNEpmAKwKZumuaUY91lVjVdjXagS_U5uzG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIQvtyPga3SAWJjoE2TC1AQKAlvGc-cQ2z5iSh-CsZ-UgA7g8J7dCS2FcpRT48egzDeb9p6y5mHMvHwgUXJpJGMHGsDWWojJMPVnjzmGvq2yr_DGP97lhEnVnT1hIyMVKS6gJi2ZxAwdjHXngPLBp10g1lUeAFhcUpsrElrooAU9bilM3zGPJoxmMjLzxHhFEie_H9KVed38OjuAMj9_5MLzUFKoyhOgSAuJrnsWGjI5vv2IITuI1ONjwiod1mSnhpWGZSRH7kT8cRAl92ak9OLDvZlbHpSbC3MyDgKqL9qX0sVwR3fwQgn1m81CDmvnX4HmPeuMB1mKrF8pt3YEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtrhUHxPNACw-rlGtC7_14IPVA5auppECpLbKAnLy57fPxQJS-VjmbUATNiBztkGt2VNHfd-XbCgTnZk8im6lsF61q80B60A-ibTRNW06UBaFmRWCQgnkWKGTj6Hruj2szE876pQQXhkOS-mR-6L8_lHLwqJtXzJJ5GS8pB_POS50VmhPbqi_m6koWG7L1t2Dtee7vEoh-Ity5vYjcZekDXh-prO8NWhvn5DSXoSIHmTvVoCRIis7i8mTAzkaW3Yz44uqJNNuC0qtpIXewcwCcdl1l4bT-ClgTORF6L9taSxdxENE_DIb0a3ISyy_uMDlfaolPbjkttkUgSsx0Zn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGEWMtgZ8054rHgHUqOghxdNx_kKvGhXweayA720cMJc_6h8U-uHx3UbzIPs9UsF8bnGJoDi20Oxpfr1rS4gh-LavA6GKAWbECqpwTWoD7rQDOIiu7pxePAJoX4NoD4zIKdH7d6xJtDhvdvPnU8BaF7sNFec4WZch8xKp4juzVMPaY2qHKQ4U89bf3JkV59WM0InW5ic_IBX-Z2IYbrE5KEcavmDGawVMcB86SCO2Cva_W4X7hPztUSjv0pd_7o6voPpXXbdymrJQUlQYT5TVMVzqYd16ICO8M-zYcm765tOuW_cciERBqjihzLoXkXjt5roEkSrIXrbpdTeL8nQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmUPXx0iKhgvNP-a4sBVFhrAvSw7cgl2833NIUIXaNAuWTZIOwtWg5Z5d9Pk_I8N8dAI7xgrsLmiEeRv6HOWaF9IeLZD1HO6qh1eGpuDGjHXraIQv_8LAozaiLzGe7ZYAi8EWb0P_9_j8pfE-PFfYHW8PaI2-rOOmmZUx1w_kQBYoYM-5A8aelvxSXV74uvGSvflDgbjKfoF18J6w-dQWbe5LbGwQiLCMLUVEzgYxneXsMbDnwZLIwGeYUIia-OM4YDj_YxYlSdopEb9fc5g3J70lQUx6FC7_0RxQlkUVb5izBC2giUdLuR_GIO2wYYKk6oGJZ-yQO_oS6AGixnESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D356DfrBjxu-fe15RdbSrf5sk4JrQWdfnktUbcM7kXkkgZbAWb5dAGQuqbkw3VTbYMbKJdafDXZkWnZwptR2EZSGlvoMxFJue46ZJCeyC9yoNOQ3zcUnVxc6JlcEYXh8bQohQ9s8GDJ-ULlinZDXDitFDCOba2sVG3frMmK1Zsxu4vNkvSSZtjGZpWLADk8ol6QY871BMkt9L6BwQsCxKzd7iUmdchRezrGFbMuCR65cc0S92A7xhO2ND1ZlTU-HbTjqv5MAN6IyMFMw1GGn5gbLaCw_hbvRx7lKQd-vBAL3IMpLZI11AMlkr8Bfvi019TTwUY3lOMp9xg7-WLfF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adiHrjmxbOVcdl-NSwNOCoR32RjDiMs-jBNcIXlc9D7vvABBx0UYwa5LYugQTp82HMZedE7Pe0GSbQnqvAtOvQ_DtDvsmP28yqS0S0RpoQSYLLSEi-mH_yeX0Lm4pyNq7GLfqnjpIXlTePM9BM_iNpSY3pkoV8lpjj3p3VaEV_gEXxMsSCjz0rhfl8Ctf_8bJ44y4UerEZXjykiuwR5zfW7F7D3DwaBvTQ6QCT8eLmSAmy0IjxOicbK2HrSKWxFpyuq_W_Qa11-hJfzYxlBit8BKbBEv9F4rcJ4_DEkfPgHpo_7eySD5JFGkPHfkfheXwAhnk1wkuu9_D8GmSFjrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTBKtUloKdBtxGWKn_cM5J-qOXB1Vs8fsvo5IESAqdVhpMQY_f9TjOiKu45dRcZaoiRubumcqrFoUsQnIVASKdFbRcuu3Wtrny8fdCq-zfWMT3y3gp4BckTopbFsmc4ajnVMsXeTvPora5a5uEqcU6it-YFrr1KKK11be59XjOFJxY923tnXcB9QnXwcZ5alTfnaoRcXFRynm2RbAGS7yhGvdeWL_TTenJ5QioBBezUd6xizTkH8sdZYesBX1S0o_Yv99wPlms7xHFr-SxdlfkWm-P09vSbZnLdoVjUD7SV8prz2-uo0oS-mhMGJCaGpCIypqm4ld6puiBfBfnBSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0_kpAyX-0VlFZH9G8_xTXVyxCAeMiUPslhAUQxYog_pWoRmil0B8SkvHdTw-Pw91wMSJ1KyJDPaNWkex09vrY1FCHF5XYG3_lDWwuvlKH-mDmCGFPPJahxayBsNyGHf_eB7Zb6IWFBW2E11H5gRDvqGE3z6WExhPISvWnDAimbATnTlBEbkbJcvBsYkr_79itUuYB3QRLsZXaRh_WFBHb3MQx2jDZ8sa_fT3HwjO_wQ6HY3Ohj-sOAT9r5HB4lWW3L0Tp3JKdVFcBFoRY9_-KbmQPKv0DKeEu9OzBF60dDCou6Qn2B1cr0MdTrig5li-cOAflXBhiLLLAtvHRVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF6gJKPQ5le6S9AYAvX4Jd8A6mVkZXDFVE3yAbXgzjTf-rrrWcS9kbGqOU4t2427IMGmXJyPXQ69WwVlcJVvT33YJobPKa38JRSDHjGQVvx3qdpG1HQkKdUWs1RUovdkvbY6X9i7ZHq9vFTGo-qGDoQXZnx88-JW2BtrZMkQRlaFarepnhE15PoDHSSgTg0lOkrgraSlukcAeE6puzKeID_E_GPcd-tUt8akZUNJD0di2UfUMxWZFBrLthZziYRoj6JI4LO-q_-IooYlIDXLWwEXAgL_moHn6Hby86WElFXHR8FvgN646U11xKlv4d5z4QyZ5u4p6g8MpO3axY9ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8JmbuyclesmmTDJd0i7Th6GBbGY0F13a9iTa8kgSAgRTcq2jYJop8yqlMrS2Wty_qQq6XCqpeCaacak9ZigzoYkG0c1d-rugkTEMvBM6m805YCpZRMNKH-V6YEvBi1D_QGRjDb8mBIbdpwh4yUj0kIu6FAZ8xllxxI7w013RJvNcDhL90WL6Nyr-H_7h3dEneypRPRNhEy_20e2RK3gFr2IN7XsyGt7dnB0aIU2r4Ss4gxapFm6uCr0Y6HTVrLvQ7sLxim4giLrMyff9XCrJ6KRslQXaBaDv3Xgza-qxnk6W_5JfDDVlgFat9nV0dwdzlDH5M75BI4EqEqdGLtfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP7An1s7NRi6vVvgAdCO_3Se0UDgzNKbpquHfAc-DWRLfReIorNcf1VyHly4Ug3LuxUU1HK5lyQz1tM6PxEtOp7GqvhiL8d0fl_j3BEtQIKzcLmbIYWV-rFCF6-VPKe95t3kjUYSzr49IuNXL_QUcvzjVvWGer7JGFnCPWsUc7ip4d1a0QKbAHWm6uJODMbNrsmFyomr9TQdcL9tg3Zh6V3F_I4M3aijJpNH52GSaYn9Bm0eGALP2WfrAbVh0mkksrkHnJzn780Fq880dj4Zcab9Br7iV5A1vm6WkvTEHd4prSTUnj2nMoIAxShl7XdHnbch3NXevZhKRkJGPDic3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
g2
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26422" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5l9OvpWtZTh5vIqAYvAUXepGvQfY3kiFQEs2MW8QnQ0Dx8Q7FXp7N2t8RMgjDemtNYmJQYGHEfNvzCSUV-VidOSEKGYQNDorb6DxBXD_fS_uJp-ZbZrDCN0AX5r32RgA7IEO5AzNZVcvicokmMnbcZtCLh1osvw27C30dg-FaweBG0nC0oZx5qUGFfhUZhYMTycCvkQI7TxpwMQ7hgKE_MmnJQ2BiYMZhV4c3lMjWacwiq-Zy1iLlU_sOByON8vqxcphcAjU-HIwrphefKU4FDIP8jeTGRssB16lV0Q1XjXJ4Eu-vIj2l63sKnola7BaUfdW-80u6sHiN3dR6REMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5r3JqBx383ilFjfwiGncwOijIDK_AFvfowYOQJ8FxADRT1e9pKejaStSRXfaCAQO_2cTye8Y4Eo2YKDFmDZEjtZnp_PkjtU3cEwewDdB9GCW7EjWgCXqs8zLTAIbd8Pfhc0Q5G0pkk-4A_xwSX32mG5JAwaO8p48rtK7MKmnpPmQktjBFdczBpeHhO5QJPBjnGruySQQDokTjGr4t7ehSa0vHZ2Fb85RbWl9qs5-4Rmb1H0Y9V_9bnUBmF9aQ1kYMQOYXlFAYU7-lu_XhA4HIOWlJwm6V5gWvtuuIt_p19chExnwT6JttmQqHzdMVNCL_1J1BN2WacUmfuxdrtBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbyhI9-Tn7p-IlxbP4DcL3z-j_1up07y3z_rrxDlCXi7G-tdFW938dfI9uLSavCE_iNzMDN1_iGOnObcxWIppOAzSucPvvluNK81U2ca73YZkEnZA8kk7gPS12gx94kRfh8d6kpWKaNwZ71hAdpr-865TWQT-DryvQeHLNW71HxsQJc_78cRrfdBgdz0cAPx93Pu9nPSZiVQ-mtzl5RWwtyD0oSULH1sbrYW3Q0m4uiA3FyxJptu_HHzpBoLVe15z5suVRlCTF3uIwLZsycHuCRMCbgOl4bbSsopWlGc0dVfEFc5LM0Tk_ajjalJwO22ZlWxJT3ti5Q4hhK7WZnP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkOSqd5HRi8I80ClCUcKDJ39m-49i4T6CS4UfEp5b9dfzntMD5AXyjie5RsKV8LVSoamsf8Rllhi7vpKQeFUmBgWoXSa-lsi6079m6Mgpx5L5btl93_uF4OE3xX0TAMXpurvmFCXsn8duQxQ3lOPa7TgLScAzqLJDkmwcujvxv0C_LkVUkDe8DvFVbRlIqIWrbfq10GhuFT3AaYpoJ46gWLuF8PgkaT7pAgTZVpBpRguEl8jPNaGH4Om3KjPgmWUyn3QwZeePvqP1-WnownRUzEDAFHzH-GWeUix2X4IZW9CgK1jt2c_2tRzbaOH0LSskzbhY5yEo6BpmOlaW0Hmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOb9gS_DojrErMGlHwiSzi7WN9zs31oQyWVbhN5NmOBt3wk-kQCjeodQf5XHE0r3b4nnC3VhGWyB9U4yxYpJcKDBXwdyvNCXIA1f1Mi9rEuVSJdBSefV5lKpXATo9AAEv54iynJ5Y3j3j0vi5Yjzwfmj2Zq-cVOolMde3zOfr2cvt1mV5Nw75ujrwTE1TXtGvHBgpq6Da2Jp0F3wE_rkt_NBjynDZ8thN4FGiAryYeD07arRU62OABvFLZlaIvfWd_iz15TGdo1OirjCGEWj1p0027B-nNmPeRdUcQfucqT1uWKtGDad5vtc7jIXwLMr50gCVwDZi2FlE4Y6PtDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXDbJl3q8vE5-AuA1PeDBlzYFt-VB52nXiPa5uPZsiRKYwO5a2EtE5m6W41KzgKLPoh4fP9DfYk0rUDtH2dsRGBpKo7rCiB7-FBtEelajYFL4teBuSGBAomBB8Koni8xAEB3rUDF3dpnP1LdqZfiqpZTmndqP1ovcWpSILF0pR19ihrEiSK0rteQQ90k4mi_ZmB_5keHMMEBXUdVwbgSzjmhlWHCJgBkV7P9JQjw1k-zTiMx1yKlyEEH08i5VhZ9xO9U9_5ox3OpdEBTPve4O6ayMj3KAjHbgF17QKFX0kuTgfYTcZcTGSDdRAHZhJzMgmC3I6E_CH3v15iQ7OvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TxkDVpG3YWzT1YD-YL4gt9tBMCTTb5a-HYPkrQX00WZpsHUUiPOx5sNCVhH-W0caMLQ6BmV_ITQhZ9KR5CZCGSDjKzvrPKbH1AMEuWyFmug525KNULYVrbiGq-QYv06ZezA1fj4YNU4ZZqILB3f39jCO2TVtd_3ib171nLQlvAuAAJcBIbgphPwgUjIgVicD2VmChq2SkKyyY1fo-IUJxyj-MIPHwxCx__HTp9Wo8G19YOXM3DtvrxxdznIBzoQ3-wUGyGQeZopfuANabsrVBUG8eyrZJy6PqnZFtOdw1pWlbK8dBH_YTLEk9sAJ1iMrAeZ_nlEnWkxCFschmPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEeHMwItu2SfLOdZFenNQ0sOxxc1VJVne_ejn9B9GMKbndXfncTGrjwYCIJrRqroI07tByjSUcZClmH0mjmxTURbbySL-e0xa9Hi4fxC_ikJAosdWDgcFrov61u6GOi7F38DRM6DXnyXOzjEd7xOAw7HWq34c-sdjss99ScHz3rGmenf-iR-ySzvm-mUvn00SvBCPXWLDBbsDJKEhZDNgY2VQtcjgmK8n1jvsUp4MUkZbnq9hy39S24jNoIAQVZm5MdKnmtlVg_h0vfkz93Cln0q8KlB5nQkLkeE_ELD8vwLhgIYwGZf6jY8W-KHqIG3j6rHjLFZLyJJPqMMZze6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txUhSa2dPIAziZgGGkv9Z-r_LrB7iJ68LFG-g4Fi-vNPaMO72O64lfRwC6j508sbEzF9nnGG8ISZl6lt6k1iKZ8eBJXAURUvriO9TGl3hqJQxF33mZ6Ffu9eSsQjkuvU73sX2CmIYR3rwygF60thQjDb8p6PqJvv_ntvTuhgIbDel5fA6XcpGrn01F_CNWzWEpThUpOSkZMqIPY2WuRgRt0F0e-1o-WGogKVliyyRCfdXeWO49iaVN461Brj2RiKJP-HLS1hoGZt8QECclyvMLdIpOJuZ5NrbWuO0QVf4gJu10eSWrpCLTgwzHPD4WMt_eiziFGzgJWoInSReNBejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEV5nc1fv7n6Bf-D1u207CKe9GCYxV9Zo3O1XR6nJelEnBaCWrXqpKHH7HsukiUrerSxftAHm21CL1OHmVZwfhG8dhaXC0285cBKCU0NVzhKDqWs9VkeXB9aQDHFUtKzXulMQz-Li68JoVPlMfI4LqttiXJxkiU9F8BSieZfFBH_ufx3fugJk3x-ciu6ZqahrCbKPIhaJgfEPXjwKdqOeol-LBzZ7ulRwTHKl_G4DjrpaXTpBiRa2OMOfQCGkS3y7mJJ06JkTQw-DQl_RSDPuTSK45c-1JW4IYfm4EvQBgHnNQTS7EFia4OORifDo9o_qgrs7Yz4S4OsJUSYkrH9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVCQ_Pq0znRmnslyZpF7EJvI3Ob0z-BmNjAJdYt6vQxse98y0kX1t37WyTCCwcDgLmnbsFXxtNgaRw0tWwoG0RvYWWn6dXT2Cky6NgoNkjR0XhkDWD4EORO0xAhOeYlbvZ62uE5Ssblz2xNmTRnMcDtr4RGyLFLKegsykxYO23zyacVfq7r3YdcshbVX2TGWP8g4FdXhlvSb4P6qx859vn38UNYfjZ2NDO_VTkVH5YPZY5Z5C0WiD2ArW8KOpYb6JbV1BS1Ga5kCyX508mva9jpNnSVDjnwfhpYZvuxnLRqoLL1YjfU-RkXiWU3obFGFLtfTFJBYAOADgfXRK4LWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E40g4655fHjjugWCuwTiZWy5sIALMM8XYZEdQg7TsrI6q3Jc5JTSNEIwtbrVWgGmtKJ0cHQDHjLOVz-oLZ6APY6x20ZT9vKgMvvQC7sQG_ISYf9a5dvj1-2-IttQTACWmD_3fCAP8PMkKeWd9ZEa_w-JoGWHWEEwnIvJHeQew9HjX1_erznxNPvZp1OwHTTNgLGHtM-sfP6AXwK7yneklMH7MDOWtciwJXCtzllJJ8ptr4mk7_twW9RpEKjI_HjkbDT-66kYbktQLchbEI2uPlzB6GDmGKa8CFJ6voF6B8e9dizV3R72Cp5H6vVBFtnWtwMjcLM435G4me4h23SiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT8U6zN-_4munaN1uAl1VCAy51AJP_3-USsnwo1TlbtPtHsD9fKxt0r0d4A-qTBTP0kdiZFAUIR1pWInja5muDS3LqI1YaQKbmrf_nIzcxgX70wA7GGC93MK04E99HPw6aMJdS2LYoJWvyHtbS9mfFO3KRd1nRGms3kWXZJnpMJK3gFWgXYFkCdqMi1qZniBHbhEcJIkyUIXiDrtlTvRxAt-W9aep6aaPwO4v65tiQHYL3vP60LcnFDcd22ia5MWvLHhjdTIGDJTHkMr7NBGWMHE4oApIKkWr0OjbjcCg-IokrchezjQQNV195Sp4W6WUbNDELkVJa0_dMmf8acbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=nuH9RnLZMtbKFJTij3cj_vtvELAywThoaqI05uqZLO4gTQh_PyXW1s_4l7DVmzXf0EvjqdeD6o6L5qSwgp5ueJIRT9DIE27qgXdGkWbT3PuLD9YT3kg9upWAngUGDSjOhQPLu46eEJ5Q4t9OhrXKCdFw38n2M_cBCfh_-PKTySQNO0n-eGch0R9JeIx140w73gb4adfG2HC_qGn38UCxkATUjMM3XX3OfcCspIFeSrjdfEIAD50GZZs18J-dYZ1y4YawzpkhGULBOLsvvSQ5xy2_44aU-FqcnwRd9W8vDkxHHIxZ8oej2QSD3sj_TMOx5nahnGaHJVPcGTKLdowhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=nuH9RnLZMtbKFJTij3cj_vtvELAywThoaqI05uqZLO4gTQh_PyXW1s_4l7DVmzXf0EvjqdeD6o6L5qSwgp5ueJIRT9DIE27qgXdGkWbT3PuLD9YT3kg9upWAngUGDSjOhQPLu46eEJ5Q4t9OhrXKCdFw38n2M_cBCfh_-PKTySQNO0n-eGch0R9JeIx140w73gb4adfG2HC_qGn38UCxkATUjMM3XX3OfcCspIFeSrjdfEIAD50GZZs18J-dYZ1y4YawzpkhGULBOLsvvSQ5xy2_44aU-FqcnwRd9W8vDkxHHIxZ8oej2QSD3sj_TMOx5nahnGaHJVPcGTKLdowhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxwy1IMLhHIx7E0rQc81k7irJ76bM7mJTHZXD7X3esXqX1dM4k8tsjgCoMbJQw926EAzi5nYOvKyR5_61I8bdGvPHl89oQdCGRG7uE-R8zeTvxhO0JQ3fyKtx4u9uespKd70ERuG0j_qAKPJWc_zquuaUjTSl4VbEQmB9YfL4GuxEUQEXxFz_R-q6ZLlkX-oKuB9xJO9aj5h0ifMarrPNQv5B-w8dqgaf756lI0MGOh_KMeI65tS8fxp7kHWwKEL56eWKzS756PhHrkrxLm6Jb1UlkN5fNCVbyG5Nw9EQY8Yk-76_v1DMQTBI23DKUjY76sAWZ-5arze8TUg8BqEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0EiJM1k-CIqscv2DYGAUuCp1L_y_c1uXY3iePRCCTUuoDsZsBg_OrTVUpLSGT920NNFNed0QR_86HEZVWpnIHKMwjJW3NdKquzri3N1fP-9VS10VRjFuswyY3dH_rbfYigSH8P7hPVB49gZM1rWzszeodj0HnwtsA-3dcsY0ORTlp0NtGFEut4Hrca8_hnOu1Be1_fQiNyEPRd7RRt2mxuAfkGl-6sPNb0szivME8IXWq56sGA7BrpumshqVkSfG9bRTtxV4nb0vb8v83KRQxvPx2IRXaJKvAXkiD731VE_f7I71NodOkPNsqOTpW73rP3nYcKmuLPFXUimw0VAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyb_1Qh2ipAj0FkxQQmKW7luM8_HGBEa_jHKOoSYXpgMbcY6vh0RPSj7B06Zhp6njJ3YsTh9cYA9xA-YND2WxV00KcICEiO_fuKTQ2joxHRI1v9P3A6tyHIsTZvNh0kxnD-23Ja1Kqf-uV9fTM2khm1U8s88Dqe6JlCtrCNSG7TWUPHHWlnqW4MFzUcnHKSAcAFWrSOGAZtZ7rVcrwOXS_-Ekj05puFYhAw-lN53FmZ4aCGdxVt9EIVe0Jx5vc8I5PgAVDdbKy35qh8I7Hg_NDPJ6nsnY7NevqkxtkFfI4kfVpiVbLY2q_Xy54A-QqVijbHjOu-tevEUokNCjTBuBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=M_Eb-QW-bSAdunTGBVqEQTzVru1zFjep140DbyZYaHZ-R86BHoZbv4hlfcnRL7dWgMpcZ6VNB1PNmbPdIMFaXhwLJLlJ6umzYELhYgbQqPDeNw-YsEZQP3hB8ne2A9O9k57JzBvrQsvKfPagH2PYM9EnFzFIHcCwS_rswioAcsJsrNke2M4SPxbYQNI6-a8MRFtyWw1A9h8Xt3lgCe6hG9Rb82vOFKPOUlpxv1ixrvMru9pYSR8pKYC7SpbnTytBeBDZdijppCxFzxCBFk5stRHrI8GfPg1itD5O7OYzba301znnVC3F9GkrhSNh9vVzDWY_4Yo5gXXWU_Z6Cg_rJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=M_Eb-QW-bSAdunTGBVqEQTzVru1zFjep140DbyZYaHZ-R86BHoZbv4hlfcnRL7dWgMpcZ6VNB1PNmbPdIMFaXhwLJLlJ6umzYELhYgbQqPDeNw-YsEZQP3hB8ne2A9O9k57JzBvrQsvKfPagH2PYM9EnFzFIHcCwS_rswioAcsJsrNke2M4SPxbYQNI6-a8MRFtyWw1A9h8Xt3lgCe6hG9Rb82vOFKPOUlpxv1ixrvMru9pYSR8pKYC7SpbnTytBeBDZdijppCxFzxCBFk5stRHrI8GfPg1itD5O7OYzba301znnVC3F9GkrhSNh9vVzDWY_4Yo5gXXWU_Z6Cg_rJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBStgtj5p5GILaMZb82i0AZ3vaShYDomKZ6Y5kCp1IzNwzzB6cnFoZMXOTbvtyU6oE3fZHLdR3DHcb9g___60C7UTGdv3AV5UjmSxxvULFLV5lxy7SO6rzaUVqA1qndo8n7UvfNgWH3jt25Sbb89OWxgr73x7Xcx50Uizw5Kns39TdyRLrY43Ax-XUsnPa6Sqn6rysjx5L6XMtCAJ_m5TZEHs8gp8NQ1zA2AfNdqqM3faGrUb1FYexEIeQ7aNSHrXWDB3fW4y2i0K78lf5pLHQnWY3KibF0_K45l-syP83_VILm579UtfpgFmwrDIxSov1iBzjDtplV3pA6E_koBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=YKjC1arikKHA1dIqxPBJ6TnZJ8gfXFVbM8ue4UYBFrJPtqrNz8PEh0lCAC_N11NBu_w38OmY7_lJ8ep-qUxCp6jEdgr2TOC0wKLvzE_iMkCsvDw5u6Lexx76L4O-uJooKwhkQSE5lYfArQhr3kB8dm7UwcIZusuqeKvTNyjLelQZbVrWxopaMHoqHqAw32aULirthUhoPOB8VFhPgdhYZlEV0JLHlW-a4sdI4hWCamNvEofBiUKDuEhWTJ0yfEvlmA0QweaWeW6omV8ZJxjvddCRtkn8NCAvSn2GOaRB8VNJOiu4eTfH0gPZMWFmdSNT4xIihx3ntXgppPFZA0lQ7Xhu_8Yp87LBDXe2I4z-uHLGiOJrmXabgHooD0C8HtR1YtXCKwr7veLEcsX6SfdQnM6Pwf6Dq6MGTRIaOJSgMREb2Azq4ZoLnA6vKxJ1Us1HSdG7VIEIepbrwgpFnEp4BPj6s2odbIIYjljCkGu6hF-ZeMxbEb3HuJS2fKPk_-6AhjN5tyl1aba7pUsAzvJMidI9kiNy0zdY6uzifV1o_3OSIkM8Qu2-_hxPcrqkomfgr631_jKKnKqlsHtap-1HoEjdVUgtPFxRJx9BGPD5sCVhNPJ3w_LMQCJX5GVEI6LiZT-ZJ1y7fmw8PaW6QUYUMM0zLweaCKpitmDvfS-kKI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=YKjC1arikKHA1dIqxPBJ6TnZJ8gfXFVbM8ue4UYBFrJPtqrNz8PEh0lCAC_N11NBu_w38OmY7_lJ8ep-qUxCp6jEdgr2TOC0wKLvzE_iMkCsvDw5u6Lexx76L4O-uJooKwhkQSE5lYfArQhr3kB8dm7UwcIZusuqeKvTNyjLelQZbVrWxopaMHoqHqAw32aULirthUhoPOB8VFhPgdhYZlEV0JLHlW-a4sdI4hWCamNvEofBiUKDuEhWTJ0yfEvlmA0QweaWeW6omV8ZJxjvddCRtkn8NCAvSn2GOaRB8VNJOiu4eTfH0gPZMWFmdSNT4xIihx3ntXgppPFZA0lQ7Xhu_8Yp87LBDXe2I4z-uHLGiOJrmXabgHooD0C8HtR1YtXCKwr7veLEcsX6SfdQnM6Pwf6Dq6MGTRIaOJSgMREb2Azq4ZoLnA6vKxJ1Us1HSdG7VIEIepbrwgpFnEp4BPj6s2odbIIYjljCkGu6hF-ZeMxbEb3HuJS2fKPk_-6AhjN5tyl1aba7pUsAzvJMidI9kiNy0zdY6uzifV1o_3OSIkM8Qu2-_hxPcrqkomfgr631_jKKnKqlsHtap-1HoEjdVUgtPFxRJx9BGPD5sCVhNPJ3w_LMQCJX5GVEI6LiZT-ZJ1y7fmw8PaW6QUYUMM0zLweaCKpitmDvfS-kKI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd7ER00m4UlLq9ttiRW0dZRiNgBaek0agEAyxEiqd_PHgVOBrWDxFZxAOFENwNunY2lhGCWTUXYObqP99AxDEqTpdBrd20NpDDOPP3PftMAZaoUAxHf4PW78aaZsmNkCyTkYODKsVogTUuzT1lujF8G_eVCNxE0kqRfuMjbJ9zteb1Tt3Jgm1M-fYhYF2IBYU5bfZuZppLqrUffC4t9WuXP2kRsVimK-6HosMIFcu1Kelyi40nF3K4CCA6XLgPZzYPZ28rLOa9JVYY9NKyZfXp_6OSiBYXjDAQXeLj2MOdaqFff7CExcUWTEofJeK0YCQ48nGCeNlL297KyC_r7f6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja0dwxunfFBaHccp5bIAdHSJSHsuWqyKS_v-U-drEzxOajrc56wHJAFzt9Yww48jxh9ObIdY7V-oVdl4oc4LXTAh5GYoZ7w5nclSbZsenN_yTVULEhorum87WfTRekiPthKc8VCDFwVQLOzkXgeUzWxX2I_Q_5OSoo4QRwkeQLvTDZUtWT-UQnDwg6xXqd017Lf1nuic3TcTHb2X9doLtmKNNaQs3kM2hOgYz1NNvl8bVl2Kqc6-r88vx3kd8-FUSBMYwxlHN0dd41sQestjo_WhuGoTXuogZeEGz_CuhHkgXQ80w5hZD2RRYZzSe6c5wW425Kjgbc2oX5UQlwcUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t32oM1m8k6o8TlavrfrB1X1tTukTCUFgrjFJWMaVts8OTV5LLBkWf1B_b_yDziyGSuTKpFD7gwhY6LliuvnflXEjL6eQWQb-gsTSUBVIRBRsq5oud3mphV0eyLaQmbMAF9gez_oulquU6zE3tW3LoV2nHmgs-MAbY1zvZhfhm6OWwRThQHYFgAytYOtHwVo5fk9mkXCkjFi-JD90NVFqrcW_gOHKh88JRZ-EDp_n-_K2FJQ0ARbE4_vlGeSax8qqAPpVgPjvPXS1mNxpLy9ZJt_eYwPVtB5g9D9X7oGghWr8skZR9D-ChhSGTYKbUYLDot-I6gl_AlwtXonL6T-jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moxRk9kD9pbF7cDURf3ALzw5hX8xPw9KL99RMXKZqI3czFoERaXmd1riUxuuCxQI_uz6ipncFxY3Cb-Y2q4yVDrMQsviDaqdj3hkjb97wIsomGUQzTX_8hvGLGGwzHOek6c3A0uISwZ8UfIqRBNWzlSse5JduD0H_RQPcz4cVwflkKpAv0mS6dspB5-uguxxZLvtEHDxKXzhf473FNxPRfIzi18lvA6WjISL9IpTEAYjZroFp7wn-fhlZKBfhFvzLDz_hRJVOEvQMu8X7iteN7tuK2_47n2Zo2rZfyJDPRA1-inN2cYr6BAmf6t41nWLMWH0I617703mAwgOqVK-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع‌ترین بونوس‌های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
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
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r2
📩
@winro_io</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26395" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF1jUvTaxxwvXJ9Hje3sGSuBn9z9b1VjFRksKkR4JEKdY5WTQ52od4CyA1fTxY005u6BlVDFh_64IhTBwUAAgm_jpF8s-ZB8tuLxqK7civMvdFLrmaEOXbZH2b1yZkEe5jcjWr9veEud5VC7OCfaye17QocvjXbKOu0tOzuon2xcwte2ykDKeMwda_ba3AFx90jNX4ZXiOPkhfqssWH_kblijoy-KdcFM9vI4PkLRZP0tWcVT0MsVE41DYHo1DP2xEmGFgc88LWGZyOrKd28ao2M_81yzkeLi1LkVkyZ1mjNj6gzVIFMRakgwV6PMa8vzGhxHkAuOX-N3XwrvC-EMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW5uWcBkywdiJKrmK5uOKj2M06IGFRCREfvvGjmcGkyoV47qBgDAziUx1jRbQOaqtaeDKdOvnTGHjoqDmHS6GdOJ_OiwDL-q8_pLhzMKOVY6uNrrNP-Le1pwhIHQQiU27p1V750q1nbuPPt4IS6-wQ9NK_v961m-F0Rac9H1_zMtLvw5hNrSI0GPoOU_Pv3mnIJsT1a-RC3Vklp6R_l-o88LgVvTqIGIcpleHrxbPE9r3eTkXBt9-MIHAwqhNcPJu84UUovaBkDNRVnB9jLtRZ0z1pSoOFtwidZnuC2u9VGxRy5P8I0vDzNkDcf5Yy4hMrbcpQ5FdP65kTGphcsMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttRNB6MYO0aiTJfGlJ3taFokxqM_n6oNbgnpv06NPNu0EfIC4Qo6gVQjK2SFun75ht4qGs_2IKQDgKq4JD47trQeh6nwuoVr0gsiT4uP4pc8_z84zf_ZBs90HrK_NDriwHGdkV3v4SQvf23fcmGwymE4XbxsDJ52CJ_yk6FahLA-_VtTWdOz-mxwamcTlJwHN3j7YZIHU9BN3mEcM8nMOAkn8uxOEUEcl89-sCM9lVbrcUQnNzL1z7q6TtL51ygQ25kEt60AuYPe7-BEge9-Y4x8WsuGOmN2IWVo_YfEf45DSs0S0DLqzlYT8C-gPLeoo5JRtXGJfQ4QlFKGVUTGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpE_7zrhWSvugikDdJgiuobLu-k1QjYGBIWkeXSLQj7TS_-9znr7RKi0aJKcWJ78xkTJHqT46G6qr68rf14TCyNdyHrTxFOIW-jUC5gyVPQAjpHG3AmVci7usdnxcDDCWwDrNeFFUH1QFxtSLPBZiu4-PudprbvyEaOPtEHy4QvfK7Sfmdmskkrbj46gqVh6TziBrywq-5e9ih62JDphPrKwNytvgDZQ51DtV3asGmTYLtqq1cRTHcot8L7i0H55c2fu3yhUznz0XHWXA4dxY-jhYXwmGdsWHJgsvdeksQEtH9UeNGnWtZwQlS7XSICmb9_-o3pFi4ZJXqn6uUQb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHj08V9zgl8FmeI3ovPkGGq0gAZozpkEIRFJR0XcV7z0jsiTxn_P_xjBrUZ55GD3CS39Kc7PdJuPZFAvpIh62qWEk0fam7-o8r2JR0N-gbp_0ymAufajvhVAA-GDWCQ8-_mc4FNLggZZyvfyX6afwPJxh_C9mlTKaObcfRRFz3JVHRSfE_MsbxbBy-GPzzLK0R7JzSO5gOvWv3VQNRv7mRGcB6egZlG_SlRnODtT4e19ozT886KafSR4hDxgfp_nV9MXy8lUk-mD6wkQjYkv5oJOOCOXuwmgVxeNZO8ADE57OsoswQ3Co3f8Y6f9r2wvjlAUeV3brNf6vK4jvjnChg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjEyvAMMfjdUMhggsRtHINTAV74G3acNhMfQuO_gFBWGmeYKdCMdZaOjkKrOhDXyykLOJkIj1IfpJDZ5EMMygsQEqQAAD1j7xIkEitqzo0L83IsSU8gWUF4HN1ITydKHC5GPuVdCBtigk4NWgtY-kMg33_prM-yOjs6oYXLHO5CN1Qhnx3VN-BuPveG7FD7BRFzuQNzffxM4X6C8t42KCQ9ZWVrQlRZpiaVrZLfvQsWya_RZ6Ov6NhSrlijUJKLRzNdNC_CStLG6-Xe9CM_7n2BUms8AB6YbokvRTBrM8th51S-L0rgodzbH4wxj8TZi2ZYYSFG52Q5IFepMaGAmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYzY1WE9ukaZq_B339ytaaRTFHitVUrLy4KOLKgSao56oC4wdXpNQxEsBSm2axjZquCMgipPVUeXKf12qRuQyXqGhrjj0P8i8EwiTsuMTAhh8MqVOyOdwGdc1v5Vud1bdEhBGYh9tOIHbnzzAT1zWAcr9T7e4rGmFHXgkvZCCIuSAAYDNUiEzWnyfsPM4lyRUVS-ULUQcwJPGEJO3hUDLVGsFzG3Te7SpEXhzGL1thpdHXItmq-ZDSVat5Ws1VGmSylZe_F-3Qg_IVEEfIOZQWnigyyd-fep4adjunX7pzoupWhvgdO9-ibeArEhetLm55mNLV179R753hOgjy93gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chaf5RXVmnQXvOmjg0Q7614I4SXW9GCPIvLqG5BZLKp0JfVGDX5w8-Ut7P-85QijbydhuaUH7go2yKESuljQ25abOXYoXzV_3BsTfx0JS-DIqhncs37k4GZuB_fBhfwqexf04NwvxaCX6AzpNVH_GOxjU7_et0EHCF9xL_-X43ll61Q1472kthfid0UyuSTBBtonj8jKEt3dKRs8ARfK2Km6RlmHWXGPotNVjNgd-i0cyQsv_tTFHnxRtC7hrzikrJo0eM6kfKXRP4yJVO9tmDf1GDACyhenqJ3k2OX2UMPYEuEtdK0FZpWTgEyrW-FI2EPXwa-Z0xcuRBp8CMlGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggoXP_Uju0zmQGbng2ZYcg1uaXFWhr6YSWnRRXxLxVfVYuFYEAxpEEu9dEuBiJE7aG6a-fxDlBeHs_eGLtZuiPilTDRLCcAKx4luOV_YPOXWD7rHeaExUk78CW63CDfghaydfC64r1KdC71zaor-vWO-73rAjBqcFJkuXHdP_yY4TbGTljngHV65VC8VYj7jaV2DBN6D-A_CoPpIXKMOkwB2okdcoZg6ZfMzBAetSZX1tkxD6yRJAjKF23fVsJIsBzVfrWNlsEeNnsnbyJHbEjpyF8a8WQ1veBE0LK_jOwrZdb-DkTByySE1-DUWBFI6h-PUQyYUb28b2HjuWNBS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwhfpr4wxgSPjYv1uVjk2WXeyc-XKGXlMAUR6BPSCAWb6Xq-i9_1L7b8lh7wDwdZWSFBwuH0C53KoxU-487Q_7dBIneOD8ZpmJWerQJ8bSSDuLKZeSXd4VLOwuGi9zJgfchsFS_TbN5loi13KBdb-pi8J45Jv-1XaVY6seLOxOz6TWcqf-gONK7fCGwTAlWM3fE92XJaBuYG9X0ftOGGt3X2TVS31OMZVRoDnL5GGy7UYPSQnemlZhDEx0ipH3HyFvTrySaKyc-vMumSCq7IO33lV5cfw-GspEu6TBdzlH05SmmPwIIn2IYe3gYQg5xTKy-cmnSwHaq4rUCk88G2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDibfD8srUeoGum33qyoSAz2FZyaoiZSAXpwX5MtH_TRD5UN-KF0ULeBNCbQjmnsRRIOqOgYMMe0ZrwsA6i1sINKR6ygRSCTUS3XgpOnuUfZsJeXWeoihl3efGpw0sWO-9ozW67ss5rfd4Xe5pBV8a8aBtyqvRrxADInRarNSFlnhEDsBvzO0y1yMGt_uaa-D27SZtZqXdeav0p30OGoLx8SAylgtTXlceiMrYfSU3HIyEeT1LX1ZG5s60gr7geGJR5Uxrspl6ffRgzM059aMH2Ypa_o6ntoJDAu9ViT0My_d3Sa_UjOdqxQyRd0CMAEzK6G_CrVZpcgmWmtd76uLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=s0l0X-acfyeXTCcsHqzd2KyvKN8sJnEPnZpKQ6-B09_OyAFDyquPte06xhmoyRMUivR-Jv-MvkZnNub23CbhT-l7ERJAcunODSfRw5M2Kjc2J_aEaNhD9CM65u4psEG0mOPwCq7YFOHkGV8ww_xFJ-j7pEtQ0A6db8I9lr61pRf9mLT700eqr2Jdwx2SOYikvnkUhoGSitISnGmSzUcbzNhjrJ3AMNtl05ziIrTZ0LmodKFhWMtdZGnDORWcDycVv5immmU5RZxRbjyOvR5Cx0UAJ1m_TPg25E97r_9ju_WmyD5Kk0oUQWOjX4_8h0y0QDfLH-9AaugLAlSUZ0ddBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=s0l0X-acfyeXTCcsHqzd2KyvKN8sJnEPnZpKQ6-B09_OyAFDyquPte06xhmoyRMUivR-Jv-MvkZnNub23CbhT-l7ERJAcunODSfRw5M2Kjc2J_aEaNhD9CM65u4psEG0mOPwCq7YFOHkGV8ww_xFJ-j7pEtQ0A6db8I9lr61pRf9mLT700eqr2Jdwx2SOYikvnkUhoGSitISnGmSzUcbzNhjrJ3AMNtl05ziIrTZ0LmodKFhWMtdZGnDORWcDycVv5immmU5RZxRbjyOvR5Cx0UAJ1m_TPg25E97r_9ju_WmyD5Kk0oUQWOjX4_8h0y0QDfLH-9AaugLAlSUZ0ddBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkAd4kjhPuGIxtHC0zK9xZH4AgyMKxKzBb4gtIGqAbp2eImsIw_p7AxMW_2ucJMltVyQ0pZhcXeLcqXR1xs4tOgiGA07RDYDLj7HnQBvIkAvpez7cVDJw4GDvM9fkztVBu2R8x8JzXzib69CQEiGyXfHfLhBPaaBi0C90_L_KxiCOZaPWhYFicit8rVOH6E4je4rtpdOPPpLk4d9n5MfZg-Vc1yLVtdkG4DOA9yImYZjG6x7GK74x39SY3KVqxvGGFBpUbyh8TbQuvSk9vz2IlmeFDtXnz_qC3KQEP5Qtwa7bGvM6wl6mCCHxn2JA0BzWI4gozZkLm5I2jR4IKMM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL--P4f0rHkeokKzzQkpQsMywMEj8d1tMNTTj-uk_hHne97XedE85Sz5LuuuhV1Yu_B2UH6oQWtZj_F3cjGPeVn4VoFJtMI1u8pWBYPCnmb8eG8yxJooySitqVhnXllye_VDIe4z6HGE2_RKpmdN1eYhhG2onKjmRaYkhpjBRhpves5k3bgWuvVcOsvxkOkWVjKKYS_zWICBj9ixPWJbUfYlS4HZNb2gTLMEYD9yKMpdJW2zh8pKXYXZfYWSzgp8cZZMjCMWBvysJ77VjxpJLb4bXjJNLF_GVkUVxUbc01_tfSVzByVXQ0YSGHE9tQOlbRvtnDY2-ZyUKVKTqJHyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtrTwVD5oNAMiZM6zYOdeNIy9jnhalUdN2w7j1gPFMVdNi7b2urF9ckRraM2f-svLKVbm-jIXpjVavFwfi52zm5HbTSVSaaU5aiZ4CpkgGeriveBgUq3efirT9sMilo8QDbS3lWxgzZOgr0_qgsnDVlrCLVY8_QBATd6Cb8PwcRfanwZsYcj8NPm2TiSjCAY3A2Lk9CRDbFkcuq-P6RH3qAm0sxTZi8HPxmZJpQsHvACv_v39UiJBwW41ETAhrduHZhD2Wdpt7fUeN4uDJ7nHjNRf4seD8a3n_UOm1E9z6sgeRpuzkRlPvm6lRYEI3n_cgKwjeUIVMfdcdIjNIEIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLUwdNAlwmWbZsFaGzvTGyd8QfyStpfgAy2FwNYsPgeoqL3s-ysulx21XUu8qEbnZSF1APrEMT_K-W1DqF4ghqrtbe7JmRlw1kv6DBKI0AJ8KhXsgsQgKs4gO9rDqjf2SvFRwlzrbPfhnX8TcKz6i-v7idVf5AC2VDQZTJacC60L9mqFghzSxkEqfVKa9ug9RYkvwIdWZqC5_WSVWJSLMgfwj_VK_OAo_ucfe1bruvnrm3G9wAIOk3iMJq_pmIFDeDDtyu-oC6IWUlrBgt_aZG3cG_ImMsffMT3-gjwGVNzIqxwwvUjeniVhLjxboRcN8alDnoZX2Vi7e73FYPaJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=p3SYDJJhr7440E98-PcuQOdSpH0_MF6ryhcULtvDpqzLR-IrqU1PigDdTJnHB9fIhCtc94efjM1l92HpAU6MzVr4NtE_JrHIW8DvRkMQEWbTIMKgaVH8-JJ6Jk4-Vymv4h39tmLv6SKAAAH6cHeWlRurPAY9LZ3KYW0jWa68l6BR6xTIy2nE6-e7PKczulJpEvlFZrBqZTxUw5e_FQR9HIxSps92tcsAiqziCC4X48xt0BwAiO7sBYWU1S9vwkgmltldJ73gL8c5DMhiFXteeUdx1rfmV07l4VkJjRpqE8YmqWAbIrCS846IbXrrO1ouvJ7aplyOLXuO8YHyORwLDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=p3SYDJJhr7440E98-PcuQOdSpH0_MF6ryhcULtvDpqzLR-IrqU1PigDdTJnHB9fIhCtc94efjM1l92HpAU6MzVr4NtE_JrHIW8DvRkMQEWbTIMKgaVH8-JJ6Jk4-Vymv4h39tmLv6SKAAAH6cHeWlRurPAY9LZ3KYW0jWa68l6BR6xTIy2nE6-e7PKczulJpEvlFZrBqZTxUw5e_FQR9HIxSps92tcsAiqziCC4X48xt0BwAiO7sBYWU1S9vwkgmltldJ73gL8c5DMhiFXteeUdx1rfmV07l4VkJjRpqE8YmqWAbIrCS846IbXrrO1ouvJ7aplyOLXuO8YHyORwLDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=ha06E3cqbcTgIFWekfzeQ5HeiLqcO-1fXume6wOjPQCfAfFAayASc-wnEvA1zFQ4wxCjyuYcWPUgCmhlnmBe1RexCWyxbiy66nS_B9hFDAFAeBSfGMgbUh5W5sYrnn2oTi5oYpLXSZtY_E_9E_0vIj3IPrPl9qOKVPJbIYY0wo9csuzcm2wbxfl62-eeLbA8k7Gjp4Yjep08JAs1yiteevJtWs-8qV4TGDxOIM-ejzyiKDOyQBstayJyabbr2y_y_xGr2zcIbLOvUWLztwmTM9S2Fw3ACRReK38rYLTU6V1Tra4RpBHP5SXIBnwV3RZjPBuu9wD9GMWs_vq7eBlDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=ha06E3cqbcTgIFWekfzeQ5HeiLqcO-1fXume6wOjPQCfAfFAayASc-wnEvA1zFQ4wxCjyuYcWPUgCmhlnmBe1RexCWyxbiy66nS_B9hFDAFAeBSfGMgbUh5W5sYrnn2oTi5oYpLXSZtY_E_9E_0vIj3IPrPl9qOKVPJbIYY0wo9csuzcm2wbxfl62-eeLbA8k7Gjp4Yjep08JAs1yiteevJtWs-8qV4TGDxOIM-ejzyiKDOyQBstayJyabbr2y_y_xGr2zcIbLOvUWLztwmTM9S2Fw3ACRReK38rYLTU6V1Tra4RpBHP5SXIBnwV3RZjPBuu9wD9GMWs_vq7eBlDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksz-x-4j3SujsiusKraK6pnzgh2tffANo5OyMPQrbuDwu760rl9hKJ3BBStpM8aiGJrIGnopAIDk_TP8eoP8V04kqIKDudKzxGOK9wzIyY5wBqRq-VKSgltmUGgLxP_vADrxYwtMwL_kjQLkt2ohno6LxJW_6N0JA70TUgqY5MgXHRME0WSapVSX7gh6Xeb-3h4Rdo75yIBdUqm3qGuN4S6kn9pmODfCbPHI_wPlNiak3Hcz39bmZBUkJXqycCnwGeGszZU3UhddhFJcRsdY4NpzZRP-A786LVDEVUsR-MJGTw5cP_puiU9uk2y4CKrp8Lkzj-LUo8kmSel3DOkTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAHZDFOObbPWP2Ekfu_16DCR8XGc40siuKtWcIRZK_h3Y02DSEvm2JmLhktjDwUQQEsNuTHgQOUX6t2YoHQ9SPjiC1y_vGYvLArXuKsHf9JxDdsSgWzB8thYiahwcAfZV92zVJqeuD9vKMIC2CbY1Fhe9NBIEHrfyfQlmj9fftOi2bXck9-lJuFzUdqmRStoIb-RGTqAQtRhtoyT424-Ez5dkcMmgqWz5KgRdpJwjC3J_dx7QzWtISjT3bXAYPo04eInbURyWRLRd91GKH0khGwzcgZG_jVK1QAUFSgm6IRhEvCIMBUg2pEn8knJKnVSKfq0P9VYRACtBIA37uk9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6imGViCvvnlLMhpdEta-g5jFtJ-ZvATyKEMvy1nqUUu1wr4NWMa0su7OLNXO7V_SfCl2LU_Gn-5zaGhsa5zymVU156M_AIVkO4O1Ean3rmkXtyHoamvJ8WzWKcAZ6EAM-yW6QTePY7nY9QuQrtT5iDwNNFZoAspAb6T2pGvxE1l2oJT3OOnYQihTkN-ieklB-FhEPFTroK3sTzAd5NdfEE9l95xXvqag3IfmYFzS1-4WZv0E6AGZY65DEAm5dPEczJr8hwKRtmVGMDsDUcClIy0et90j4piZhOazeSz6ACoolz0IYqsRgh21Z6Pjdd4zHqP4dIAaiujtU2fb2hhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfvYv-aH5vM-IQNqPG1u0tGNydBcwATEZu1-gaBKUdE5osIdaCbB0aA9jWvO8g0_KwWU0oVZHXj6n9e63gI6SFsMIfKc9u2TbJQCIxU1Lch5dkx6cSha1Cik7vvBB_j9U7OPxN20nzJML1mWyR-qbddHKDzUA3IVXJxECj7dKDZb4fMl8kiYUBPTyfuwibcCXeoMccUGSkdfZ2_kUMdtdfoHYmUSBrNM9I7WgpyCN297ymi3ps348s-Qre8ltk91opSmBm4v_9208sL4OdsIpRgFbfOCnToAS0xIFRJ1O-jVz_G052Ce6jH3V0UWvjqkUONHJEyBT5XocwQQH6kWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhuPx8jUKDJ2q2qQCmQMuDzJLVCCD7uL5PBiuUzX2MfTbM2d4H_D04QYyMKcGLUinJCwZ-J6fxVQv0PI4MDs7bMWl8ncfcZkvXSdLAa9XjFqxn516nN79CL5MjUpcX42dV39eb1YHERhnozkFsvUPpt07EMWmZgNJ5WdR4RPjeSHdLVzLQZzU18Y6mRI5sXH-D6R9ns7WUnjzrtHWVgp6MZ6q3OHvh_Noj--z4wql0Ci7H9YuYGB2TzXCuu3csBjyJBbxWWRN40bs0exRGhEsixBjCCc_S79dCFvKsYOHAjTUqvThYiNe4hbBWSy2-15vymFHmHz4KdddMuTf17Zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWXxU_jZSLCQK3cpn4e05uc5l1A2EkK6OVWnQ117ePRWvy_aedoNrtd7rfrpQyu0ZoDuJ6P66JXeISDLX7oZ-jjJCzck6mjwTaHY9u7NgQbTnPTXaYmjpDVcTLzoOUDwmGH3lPz0NxOlizUO4KMlz14trkux3m6-6lFxp8kaZt7-hnuNcs6jejWLhUWdLQfXUAdDPxl8iaJ1tAFA948Lk5mKyEXEljwwwJD6UlFHhst8Lx5L9ua7P8-K93STa_Ht7BRei2yZ7WXq2_MGMIG2MP3FMx26L5xQwkk7frxGlDzftMNDdSXFio5Vft7RK7FPhm_u4DRoervu2xu9afEFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Sq_HNr7wcP2QP361EMX-HZO8tCZNtHGOCRnCvCw_JV5LJe51kJyQ5kSEWUyGA8fYUzAGVF60GUOztnyhY4Ha9H5VDdYfAJS60-ltVpVv3PUqLUJvgXjVto41Icj0QoiYFpAHParJ47x7sXPGgpLGC5CJ-zfYtdm1-VbRGn-EyWQIZ4RRfv1mvoysqw2zHwNS-E8oVvuS_XtcvKh8Ix3H9oH3nTtyUq2w3Gp7owLkVGKttNYYuLOpTx28C0FmnmaJTDnxTYJxQRNuAo3vDDCz2_siD0WHn91kjMvNj5FrO8DvQddMDEv1kGJ3IEJvoldIVDFqZ7djVOqUDv8cQTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp8lepz6sAPh7Jy6VmvjMD18TrOAkN0LfWIluOsMejhwh_Oy9VGvjjpxaB0c9SQgp2dkmwZG_D5imweamcvuZAWzNnRQQ0iEb5fPE7X7QrMdjjeLu2ujvIZy5SQY0wFJlRG8R4lC7OEA37Nz54QfMSPDGob5fFXcesI3KemoZClXvvje6uT14lrNsFvHi20QLz3UaqCR8dsqvQiJO5wNChhRjyjYmn4WrCcxNypdpYfze-IHZQxf4exFNCgBPBCGKt4PNGm15DH-bLRFNJNZcXI17Oc8sv6UOyesDski02UJKGLQyEqsfTrvMWvvAx-U4x0kZIuezvZGhi6RWYK_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=M-61_S4dsf9n1vIQpNgMuwQn1v9BriNCDtO9NXtRA7JTwmObECW1foCAI6xVSdGvrzh3kbRviK8keXxjasoeofwY6J0JvqaDlX-xT8_g_B2Ob5Y00R_MLOJDoWxSrGkci6cOHrheoMk03AUYklpUCLSMA8PT5uxAKXX5NEZioFyBb0gYW-NsUrOu0QaiHyyB_BtoRlf6tQoZt2w_WVByz-7ldQ45XRV13UWiv-oBKfr1YU6tq0TB6wgObt3Sn7RBCnuanAJV-09p1PN4WaRud2WO7THcUxNf9XDEDKV8nMAL2AeqMe7q1leIRUhvQhJCB2dKRlIIdQpgEDkjbkYTOYIPKH7KFwm9qSJMevJtU6GBMxLuQMOZNBtRtZD8sjlgLLyc9Ub1kJvogSH2R0eVE1GirtfPOLLJHUh7LYKdN7WG-FGAlpyAe8IAmZVHLaHvhAolk4neKFIqDukF9lWbYTBmfXr0Jj_k6QAIxfAbOleAW0mWNnj-VXsOWBlof_M-3DZsizorvZynyRvxfEDGkN23zFOVCvE4zFdPgVa5ZiU_nqRrKr93KKRCaHkhWID14AbNwrY0_55eGviSAK7bUaL0Jsj-kQMrIvPpWPSVthkYkm3WbJxFmUggB3-uYi1Qu6RYDMCs06aFXkLW_CnqMnEdG16e9OK92n13IariT8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=M-61_S4dsf9n1vIQpNgMuwQn1v9BriNCDtO9NXtRA7JTwmObECW1foCAI6xVSdGvrzh3kbRviK8keXxjasoeofwY6J0JvqaDlX-xT8_g_B2Ob5Y00R_MLOJDoWxSrGkci6cOHrheoMk03AUYklpUCLSMA8PT5uxAKXX5NEZioFyBb0gYW-NsUrOu0QaiHyyB_BtoRlf6tQoZt2w_WVByz-7ldQ45XRV13UWiv-oBKfr1YU6tq0TB6wgObt3Sn7RBCnuanAJV-09p1PN4WaRud2WO7THcUxNf9XDEDKV8nMAL2AeqMe7q1leIRUhvQhJCB2dKRlIIdQpgEDkjbkYTOYIPKH7KFwm9qSJMevJtU6GBMxLuQMOZNBtRtZD8sjlgLLyc9Ub1kJvogSH2R0eVE1GirtfPOLLJHUh7LYKdN7WG-FGAlpyAe8IAmZVHLaHvhAolk4neKFIqDukF9lWbYTBmfXr0Jj_k6QAIxfAbOleAW0mWNnj-VXsOWBlof_M-3DZsizorvZynyRvxfEDGkN23zFOVCvE4zFdPgVa5ZiU_nqRrKr93KKRCaHkhWID14AbNwrY0_55eGviSAK7bUaL0Jsj-kQMrIvPpWPSVthkYkm3WbJxFmUggB3-uYi1Qu6RYDMCs06aFXkLW_CnqMnEdG16e9OK92n13IariT8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHlXSeHsPnIL2_aMlUmOhCgntVQOcGlWQZLQ1V8PzETL5O4BIkXjKjxWuBIY_CPZJLtio5sUFuJRluvKd1xhDX7hllDoW1xN165M5SRh6tvbFHxJe6iVOfO21j_yjqjm2RS4Kl7UmasIXK9aZqUF16QShud_IiAG7zSfPCRiZzM5MTqb8w9ANaVNVm5uV7zRSR57Gmf1AsDRNFa1u4DbxhNGbyK7MpCutldWRLrJfO912eB4eLL3U9dWGwxfttCl3Py57HJvFXeyLmmDaUeY3uWPYRc2NNx0Wnc4etVhRHJBRu5vt49ywjm3h7j03HgqVAjnKCInR36o1ijmeGB_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiD59ry2ll9k-umdaeq81RVo_lUgc8koVsf8ePq_ZNFsrIgDl5xXF3slByA24C2rDtpuyWeshIh1sSLbEoe2TN3xtW2Z7YuQJlwmJ0dKvBnkN0fztgGrGiepvdO7G5J3y3MRwC_0a8CCz4d9B9qbuSWPeUQPav0boD8gb7qDY--AtoY24LMG-f5WzW5T6fO9_4pzbSIE7VeDStcefcvmsrx3Nau82al8RD3Kut3zAcez-0hbY3ByzNySnHq4sS9O3UtvlWd4foSP4IG8tEpXwAw1kkG61CH3ETbzr_fB8AepwxjjJvwQc9BnBhZ8hI-MmjW76O58khjvoCaTmqZNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ_rj310al3V9S9pFCqiH1H9qcNJoV-ArJ-xL4EFxgGFoQwxCdsqFW8BpLe2t3lZRYFr_4iLNzaeeptvfDGctERcKFYdOXzci8j6ZEArpSTNuFu5fQLyNyE_2lW4WaQ0JHmKa3ajE9TvanVlu2KT-GFK7aF_0kQxN8nZ3jsncFo7i7gjuo7jMNeYuaT-J31OtK95Z1dGQzxDKKSIgdjkydwajD0RfI5-WI4YyoQ5WJMTcPv5PsOSvHUFWza6WnzB_0qBxfBaNAW8kYlB2R4Aw4uZZXS5YgkJ74B681pbjJxIymEh5J7Md_08_dNFcWJmX1Tn3y778XYv6DS9fB-OgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LluJS8gvEVmbrLV2svJ5-ZXHFopurpP0UmHLootJslszBziwYeP64i6b83-5WTA0ZZ-ye5q8pfsuU-eZ6_gnh1tD9eALxVu-KmjQTAsIwkQPrb2xm5ocTZtzlPkinPpXTSJODZphbrxTPmq_VD_-CVhEfgxBpSil0nirMNuZWGd7rtwyRbKNZuox5c8OwZReZC0LUE9BpnYjcfBTcjIATLYVmeK6jLOeeZp7FP3FRuTnUMABiCZiHdGifCAhSENyL0ghE9innuI7V5HlLXqiuUgkGVv3farV5hCTBmTcEpcNpdYl_HLz-esozH9pbcdpZHeKVc7SaiXvhLaVbhmtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjL8GwOdzURh1Ze8Pa_UHCKK0q8hubrqDUAxuZNyvsWOc3qfNirCwZOmSQ6QFkUiXxYA9B9Oj-SlYAnOUtaWGTcC-bLvub4re80DVn7IWOWs64FyeLr6zgNSfiiHjTBNAdcDkP1sl9QQy1WuqIBxdOsAB3ln4bn063ztiooR6A1t2eVE9BgfBivzn5NCGF4-gwIvHq2jbGBMc4_5XCKj_zI9psrwdbJWLt9J2e9i9dyAUvh9rNu1e-MVSiaUdaTrnr4meNXONkoWEDoCnU9pxR82tHuffiXH-iAkkR4Btm2dFBH4L1ZXV4C6Z-Wrejw80OB9ZrsVlue77CNt9mGQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdrHACcd1qY1rn4G84eRPMMnP_Gxy-IhABjVWMGTD835x23oPg7XIjmGAUfh-U9h19xIsxSbfMQQlr_vXP5B_b9O0zFgwA8pH8M2hMX_t5MNd82E1kEauTXU2BNKJdMoJsmdHIVBH42WZucT3Hc110Gw9lzwsw_TGnaU-4LemiecQHe_7bMRl1VD-Y05Ir2wbGpWbI1oDoH5EUemO5EemEF-0-mF8dTtRTGHG7YppNz2G-BVKZ3dWgIim6hw6nGk5xKIpOqMbLF2Rl0QgE55qjhw3DPjS2wG1HAyKMO-seSHzZFzby813oVgeZZTRjgV_iJiDNjiH8Maeng-koOiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHftAvwJkTLi1E9CGu5hSZcYiSnC1cq6kZ0LxtB0kALqxnNmmrDS0o9p8tJ2cu0XvHeEZS30IioQ3ABUJCvWGt6n2nQ87UUlOwnT3LjpHvCS0n6msoS5fRCIl1A4Yj87aU8ItlU-mpQ_mObjKvht5o9GuoQFNtBHulKw-Ti5dd7A8FCcyuGWgsUbpMtG4rTMfVTIxbbEw1CvBpJ53iXG2OpRPiL-aa1QDmFEo0zb3VrhGmgsYc3QNPmbgbXopQlx-wExOsVgmze7Q4En5aS8rZwcGLGikF1zcLZm2g_Jkx3xmPZqO24HVmRvXkOzRRbYLvem7FdmytJzkQlX4TmlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=mmuU2_XSVzDzghSw8gLLjF_8PhjrzI41OAduTa6O0VDSigIjYtQNXhnSSRBjy5lQAA1g00494xHQBtKs6bI-fqhmM6B0j4WsCjXtXEOUg0vHRfTDicxoGMWeWubpzF4pC57obvj56z_WSHYpZlEdvvcNNye8_jWnHFRpOzQ04UbSGavu9NKGxmdZhpgtCvnwkw3E0No2k3f69EYwtb3BmRHluneEwQq0DYg6gbd-y9HOoxagwNp9c-0yM3GghgFDgOoN3RcxlRdgHrJMfysUhm3ZSfMhmEmQ2Zohg9M06MVy7v3VBDfcvi3YnLFDzLQ7kUuUyeY5WuYQlmvuNPED2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=mmuU2_XSVzDzghSw8gLLjF_8PhjrzI41OAduTa6O0VDSigIjYtQNXhnSSRBjy5lQAA1g00494xHQBtKs6bI-fqhmM6B0j4WsCjXtXEOUg0vHRfTDicxoGMWeWubpzF4pC57obvj56z_WSHYpZlEdvvcNNye8_jWnHFRpOzQ04UbSGavu9NKGxmdZhpgtCvnwkw3E0No2k3f69EYwtb3BmRHluneEwQq0DYg6gbd-y9HOoxagwNp9c-0yM3GghgFDgOoN3RcxlRdgHrJMfysUhm3ZSfMhmEmQ2Zohg9M06MVy7v3VBDfcvi3YnLFDzLQ7kUuUyeY5WuYQlmvuNPED2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Dm5pRWZKsNjt9geDwDk4srIlO9UrH4p-E_8L4y2SgVuT3beeKj-zi4wKS5zUKmw5Dq330UzOwkf0n2TRVHjsF5FhcuiKR0qSEn2eDfyjfZIm09j48XwvYhnSwR24ghLKHvGS2VKXnioEEga7o9UL8TFEYG5FnFvW4eckGbEkRQOXJbSGBwXEs5j0ffuLrJGGQ9SERRIzrsUOyT156lj0pcpbMxFBarfxXPNh8PqZf6OgKirxGE2CXmr1ExNYHqiaBNWmpkLUC9gpw-rhBVLgkayl7uRhwee0ycppxgLYzl0h38SKf2tyqUx2Ab_KTnc8Z1FQowYjWCANs9K9lBj0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Dm5pRWZKsNjt9geDwDk4srIlO9UrH4p-E_8L4y2SgVuT3beeKj-zi4wKS5zUKmw5Dq330UzOwkf0n2TRVHjsF5FhcuiKR0qSEn2eDfyjfZIm09j48XwvYhnSwR24ghLKHvGS2VKXnioEEga7o9UL8TFEYG5FnFvW4eckGbEkRQOXJbSGBwXEs5j0ffuLrJGGQ9SERRIzrsUOyT156lj0pcpbMxFBarfxXPNh8PqZf6OgKirxGE2CXmr1ExNYHqiaBNWmpkLUC9gpw-rhBVLgkayl7uRhwee0ycppxgLYzl0h38SKf2tyqUx2Ab_KTnc8Z1FQowYjWCANs9K9lBj0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqaCFT6BTjgeAgtGTA_JgYbh8gwbjZRBTbAwUf9KxUwlpHVz9sv-2hgBZEreVJBZmymJqIyBPMANRIduJ4WqSAgeNuVH3Z8YOdSg4-DWUent_qMGg1m3vH5Pm3eweAaZg528HeTKS4Vli0UCKWk8s_Yg-2WYghUWsN6JteFTnPR4p9EWbb5pHjKBUqz4pZUmfI8cH86czSwpTQBSKZqLrA5c4QRt12Pjl5G-rH7Mv993uYYL1bl74NBDAODl0AMQVtf_bx0qtRob5l0G1FINVWkCUtqq7EACp8ELyWAZmeiKt4Lz-fTZNf-0x3IYnnYHZbXPdKyH8UCuKHk6TwYAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQaxCNwLtOkHL_yjcF16fki8N45QVcKa_ReD_MhmMwucY7QoHAqD0wM0fZM0aatyCEmNygpJ5bzKtgECCtW9jz2Aklh8UiCbYUzwZ8Rr7YqvLuPl5lp0oUtX2vXu4XZjCUlKG07x2eoMbTsgvUrlOUMGVi05bbmMDK8IFkQd_VuBEcXp8E5RFF3nwSRGWSbh5lHt-fjFmDe60ECBK0YYUcETZAaC5LmzDFZP0vAnHsaWPAkxa9-q2t5AlHUTEzKwSVSPGm7fG4oy250QLKjxYaIq2ryT9XP3guKpjkquZwWygOKbH5wMLs4mKxBBOIXR1k4bruMD4hiMHzETySrqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iim-vTJbyHORVMDOBOTc2mwppBSM7ZIjHypxRwmmCPoDAptlIVzlyEvdlXzCJlg0kptoSj56zRHvB-UNufTBaQrVUmKzj91yAp08hFuLe7XGL5GtQnWIoK_9jCxnNmNQNYULONmk-GWFo5_s4N9mcGZU7DCVU4JoZ2FhTgWt1W4rIp8u7Z8qxBHRCngDIRvTnl-ha8yB_9DJCDgvsIXBnWLN75zC09j1TEfJAtPWdOVBAPpYCd4kxjxqIezcoh5i8G4P08-XI0rDR6OS0DkSsfWWGvOOkpdSyzzCrk26WgLb87iF0hhMpW_cj4ER1arplsA3cH4hZtv178dKmiJcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAtcdTlt18oD7kYoD40f0HhzhhcpJEczG2RE16V_te7JifKOLY79_oXf6o5zo6cBz-YDa3marZw8C82CDisX4RGKa7OIKZUPkmy_Rp81E7L5A2CmPG0GLTzzbVPUKduDRBIkgtIFhMtCyOefOSZzFGQQNBtjlWnwrJm1HzZdgqH_QusTrkTjwRLWztzRd3rpbe3LXEgofkHNvH2GOfI8wLUsVDG8V1BU3wmNRkdizu6gNHrth0GbpVg3C2UXkkxP6Rk9Q1POiLFEDbGfZirLB74omvgbooh3ycf8awXIl3u2vNo8bkN8QFxCsNmMPiS431KycrMapFRhE5os7pPd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWiubMvsiWdh8PLA5J4oKAXYBNQI5q66RtcroblS9TAtSu1Y4quEJZ_h-L1FubuhyHZQGy4C7i3qmS_XK2Cw4WuqX7MDW_wOog6ImhuZ3cH1C__tVpA59DXbsspX80TYVCG6wqg38Rv8LBG2M6DlVLMJKzHVsrbfzT3wKGvuRKFHXbr1etSP2I7L_vPKPw-YSehH-33YBBl8nqmdaCMRS5raGsZCRtZEl_X9OjVgJUFjiQiq3-FR2tDCXiaoNS8ahH4-vASH81JcsItLOL0QbQ9f3nrIY6-fytajKCobjbzjAm1jtKuYbdjzteLGdTcfw_d3SLEpTLOWixYyo-CLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkcSXDLYpkq57gW-vsHQ54NmyROC0A5bFSiShbChJ0jcSGaXd05hhCXaEmyHTFdwtME2le7H7CypFayoeBP230XpfEQgZGZSK43MtzClZpT2pAc7XyP7jiHSokis8TenMm9hr6e6AwM2bXUri7Rg1tZ7y8nZfc_zZEved9v2WKLSVvtDlHxDKN86tg9ACzcpsry-P3mnNujHjJELj9x04H0ryeytRhN4yHMZyDwFpjpp5G_yQmnXZ_VJONrhtW8EoPmJlM4ApBtXQzPl6LdUww-cCoq3ej4QiHRODkN4Q1dsrn5wpwkM9su8IP3mPpWgS6g3mbWM0pGVHUB0GSwJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXPmtK5TT7wTr6TlcQuj26QLzXc1z0sh6_A35sebKtP01hnU_oymaxedS-j3fTrPRWDnRqeUGpNV6QMFEi8pkcUkgU896RvB-L78U-bObOdazrCqqdEIbgMqY0WHocDAdmc355TrJ2qsptkMbwnE-_r3gbv3iW-0IdFFraPp0uJLJW11tuVf16EIY0qx2GtDjO9P7ZeaRJWYyisKsrVlMSC4WDHDweXOLL-6NzdKjiPjpz1-VEUuBf2-GuXrKhAirKKpVeWEGY-rn0HVNWUI-JIC38ixdaC2SVIIkYAuTWg0hLGS-bV8rJdmEtKVnHQM8lFmBIrrsS5Jf_0ktF9m9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=I_R5hyX6s3_YVEcA7__1qTwZsjjbAgfnQG8wmSvLXOobIiwLGAw89T4GHodXjvrVyJntmtO3M-6J6Mrq-3YgspCO8V_QUK4QgRh5rg6KFtyokapEZpKbknF-Mq3R5aP5jslf2rHF75-S3fmgVevFDyfD26-wPUYFM-w6P0sQ-TPo5oHZKsnVHKA665j88GfM2DH1wVjFbNbFh6v8-krjmB1eelF7wJ65bp8VTIVE4uHha-Hjg7Zz-GW95BXGskz4Kb4H9mxC_fhe3lFlgzwu_TgV_SLCV-r5cQk4yEaYtupgig41mb3onvyaBtVq81cdIkyfTBNFF4D9VZHoC4qgPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=I_R5hyX6s3_YVEcA7__1qTwZsjjbAgfnQG8wmSvLXOobIiwLGAw89T4GHodXjvrVyJntmtO3M-6J6Mrq-3YgspCO8V_QUK4QgRh5rg6KFtyokapEZpKbknF-Mq3R5aP5jslf2rHF75-S3fmgVevFDyfD26-wPUYFM-w6P0sQ-TPo5oHZKsnVHKA665j88GfM2DH1wVjFbNbFh6v8-krjmB1eelF7wJ65bp8VTIVE4uHha-Hjg7Zz-GW95BXGskz4Kb4H9mxC_fhe3lFlgzwu_TgV_SLCV-r5cQk4yEaYtupgig41mb3onvyaBtVq81cdIkyfTBNFF4D9VZHoC4qgPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzq3pHPLG0BG2a8F4i-9uz11gJOv92D9QvTQ__PX0iLuj5AUp3BWrTdH1GQbLz_HkwF99cgEunDlBX-EvR12FKRPy3w-LkbUUPK3lkiGELgkMW7aBccgIjh9BXLkufXSIHEp3ZgSY_iMd1N4nJff3U2eWVrPpXJPCQrfwcSWK6sDyC9Rxxj9SKGvYIH65tXGbSqlXvlGEunueybuD1cD9IxmeKHBy3Z2YodEhQIDx33xELcfq8TdTbQ58k1B7vBtwSCXZBEtjm2dfVy4goyAaR2oOX2G8G6ikawDIgu031OFzv9elJLs2D2yQQiDpqZcBnt0Lj9hitpBPhv7JGiOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=QQsjUammSs47HfwcxjiG27g2ps8wwolw96aq7Wkzx4zs8Wht0FexokCjvz0-FMkn7pJ5iDxaMYtli9f9ilE_wBlcdEeSIAxRLH4ulu-vU9w5mQQs44LoRFYjcKLcTs70vPuVhNoXz9bM_wijVRk8RwX3O6xcGgfPCYHbk1frYFJFVLj0raHWqSyrlJoP7BCyW8wEgUQ2SmeJn-taCzEoUE-ulndDKvx69Xbv4eY9Len9ggVfm_fWRG99vmikjBUVcjn2jzrKFUuzDhy0GppL-EmDOkyfF2Ry-MPkK230NQR4fNpKpZ2JDwmhHz_-Nab0zrhX8BRHCKKu8u9EaHroqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=QQsjUammSs47HfwcxjiG27g2ps8wwolw96aq7Wkzx4zs8Wht0FexokCjvz0-FMkn7pJ5iDxaMYtli9f9ilE_wBlcdEeSIAxRLH4ulu-vU9w5mQQs44LoRFYjcKLcTs70vPuVhNoXz9bM_wijVRk8RwX3O6xcGgfPCYHbk1frYFJFVLj0raHWqSyrlJoP7BCyW8wEgUQ2SmeJn-taCzEoUE-ulndDKvx69Xbv4eY9Len9ggVfm_fWRG99vmikjBUVcjn2jzrKFUuzDhy0GppL-EmDOkyfF2Ry-MPkK230NQR4fNpKpZ2JDwmhHz_-Nab0zrhX8BRHCKKu8u9EaHroqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXEmG4Kos8sxk01u13UVaReazVoYRU5I2wqoiPII6Qi5AlTcb7-H4Js8MblN_qFN8PlSfz2zzmyUMC3HJjsu4HE69SyiWsPjdmHijy7gURz7JWTPGxI72bVbD_2OPNYqm5xMJla1j0G1BdaM4tGMjkAGzZgB5AzxE8w1iESNuOrGZRrbeCm1zayqzZ_UaIvz084nPeuDl3xs9Rt6VeSU9uyMFDcZQz576mfxvnNqqKb2eJxUDnm1Hd6ItLAnk2N99etDzTlz0Y0FlQH0lR34Xf3FPQqaBfcXhOxLV4KAqa4ohLHDsxX6aeeXIWq9BnocXeY4RgYQi1uDTBRDDPoCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=C4PxVJdw1BB613KqI43acUUiRn0qavg9n6JDBjFUvQqE5hvwZ5ft9akPQs0Rx0v7SWUQGw4ipigvVzQZ4wnHnXOf3i62p9XPCJjm7_Hy0LMC3TGD4JiMV2ytFUpuY27WbK-L3449M_fLi9FNbW_hOouz4aT7ruJl7kFRVOqb8VLSI3q4BuBn55PfV0k3UN6iUEEI2DlmELyqrDSrGSX1MpJUlHdVPGkKld9BRGD_YVFQLSKlN_9rh05rEMWa5nW7Tu6w8NI_vLcPZbUniPgBmDaib5bgwlAwHDhykNobIWCDg1Rx0UJhD4UyTwEHuhrxh2teSlBQOJNdT01vxkFK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=C4PxVJdw1BB613KqI43acUUiRn0qavg9n6JDBjFUvQqE5hvwZ5ft9akPQs0Rx0v7SWUQGw4ipigvVzQZ4wnHnXOf3i62p9XPCJjm7_Hy0LMC3TGD4JiMV2ytFUpuY27WbK-L3449M_fLi9FNbW_hOouz4aT7ruJl7kFRVOqb8VLSI3q4BuBn55PfV0k3UN6iUEEI2DlmELyqrDSrGSX1MpJUlHdVPGkKld9BRGD_YVFQLSKlN_9rh05rEMWa5nW7Tu6w8NI_vLcPZbUniPgBmDaib5bgwlAwHDhykNobIWCDg1Rx0UJhD4UyTwEHuhrxh2teSlBQOJNdT01vxkFK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqLTXX3sv0q0sCRG1yKAxduJW5CstHvIpRITXXsdwhWzrChG0c-kngGNOCb_b8Tef_4tXIXEFAfGK7WdNQCyjNO_qpcvYbMZF7TlYGDcz-H7lfDpfgLbAytRX4UO4CkJOTVO2yPDrX9Uvdr7sYxkIqoD_6JhokO7boSjHmGECE66ZHiApBhA5JjV4WWhr0xRlOHuIxkSFtEqltSKnGbtBp_-aKvabvJ5nbcVxSoCVHYVSGW0Hqna6iyT5wjSyC79JcfVSnNqltLi5_IfmsH6HIFmWF-Ik_JAAgQ900MFRhbRfi7s6fwngSPILO6PC0Z8xMnHPXpnFiYk1vOAB6ZbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwzaUKHzAOtij596gmItb8Ywf6IRifUvFcA1ViXlDd47VE3RnWOG-J3F20h8LslF0Uv0uBGzHkFpHySlrZboR74Z3v96hbu2QsISFVL-HWhUgva8cqXLwTiDphO9ND9P6mNfMsLLnEWtSWSIis52D1Fg2fKHsIyylvNTNRFxqKSG9R7bK44qYstkCX4pSELC-5xquL0Gcj3nHqyBAnqJmP_IGwHF0zjnr-Yl5DWVIRUsL2RGzh5gMZtufvXRdkPGEgVWD37AiKYMVj3am6pOGEs5Aw6avcnwS-CWzWNTnT7Fn9pQ0NPMU5DgCLwlqRvXmDsugaSH0_cyXALy4usCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArbBqIxSNHbP0deSyzIcYQqHsb20kzLNvpaDAqjsYTR2VI9QeB4vxRzJmq1Gr_Gwjduh73G53jXYuDEawayFZ_XUvJuP0iD33xn1uEVXv9bS7C9qRP7k9V69xNf84wNSo8-ZIRJ4ktw8VLEGvKNsGReKnb_5U8wA8qFqLCnLJ0O4H9YU5c4jNhOA9QuvwrrkO9qCdf6koGY7lHtO100ZTvSeNBuCHfLDLVkIjLOASSwvosIogZ6GJ-GYc1Qi0S_vQ5w6PJ0iXJzNPm66niSS-eS1olgnfamrtaMmb-cVd1KVu_QeiBbvmaNj0aVZ0neMw5ftlBcwsrVrEShwQZ0AgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiKnmwEmEQt2mLeAu0Yss_6gHOSMQupQnhOXdA2BtAtk_LiJb8ENsmeiHc0lXQ45XiBsNy0x1beyz9Rs-E8rqsFwTtI7caHaSjre1yrGhwwLQ7LeQrYRq25jwIBbq8N4WlKwXhu6IJ2S-vAk-GnqKhQPOmc_RMnqATUBJFLLjvuZID1NtaHWTKAUE5LzfF9rjFZF4S2m8l_yCHmXxyxkXFXiGjdv5gHa9GLPwwn0NHcMsOq4I_sB2BHZs5vRsircNTBNj_fO9HKhO9s363RDe2f8WOPZQEpzKaFr3P_O_K1Vvx_J9a1Zb-akVMsOgpzPE17wRxx5M9CEmbNeigXRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh2_M0gcFwSbtM3szgDq77ONkCk_vIkURDAW7eF3JvNECOWIOcb_AM9Atrl-3zQiOc1w6QStMsBFVVf0gw6YuSOCCnOIrDPfdT_udJA3tiikJpibBmEKwYCgMbFYUUfuOT6pn3vV85om8Np2YvcfkaCTP7C7SbYI7syC7vg5LmW3FILLMIZdxDvHiRcTuFfdTcV0-NN1HSbgCgsIu5neVCTcVSkKzOUSaBZr0Tvh4q_mzfTei6yg5sT7XABPDIFVVc5RPdWMkCqCN-NVvtjf4Ozssw80vqI2NdGCDA69lp-Yjr8q3ozKObiE4Yoym6OCI3DBxAgzG-Co1PllTOKTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1zVMjyY7_3G4zc-vLFbza3fXY-W-xjLqu2FX5XRV-Ro78BZYX-31wx6PFsOD_6C299-65ooju-hIOvHkkt6jsMY04NJb0zAI5CRvSScseeX1jdFXA5EF3HsXlC2dcnkduafjFZft5sRYmQU63j_BNxzKmzKzYLGGlOlld6P3R87D6o3Y2wXbjrrQ4nAY0vvXD0X9y9iReuq-wdT5NGqV9-Y5kg5x1tfk0u_Ox_j8br5Xg-bBNdfeWSwQCd2lyFg984VP7vNvQ0hQxSUjvA0eXErUOr6IJVWXdEJM_ZGLTQ6c4hMqlP0a_o0Zowp4_-w4OLUmYiAl94ywMPIG1Opzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=WVQwBpfOSaHP1TtLD81K8qdcoWykzCllnN4X5dwy_xLtGZfo2q-8WAogvPcAVjLB0ahMzJrAa7Qbe6OWC7R5pL7CEJ4yUE3ElMfMZFP49Y0_44Blzq2b_hS1F9XPKkuw6S_DcNuHN6G89xqG1SdivB0_5lNagakoqwC154kWosFXIPuK_4IpdMg7sCCzN8EO6gRz74vC4WnFDPcb4CeAU4N3-8piQFkIIcW7dfHp2ZwhgxDuQuvySYsek07eii5ASvjKJFV4vFAQt9CIo3ObUNPNS9G3PxZZHnb5WSf3YZtJRzp424bP9TEz_F1u96qFXg0GUZy1q-DjWLlCd7-Bow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=WVQwBpfOSaHP1TtLD81K8qdcoWykzCllnN4X5dwy_xLtGZfo2q-8WAogvPcAVjLB0ahMzJrAa7Qbe6OWC7R5pL7CEJ4yUE3ElMfMZFP49Y0_44Blzq2b_hS1F9XPKkuw6S_DcNuHN6G89xqG1SdivB0_5lNagakoqwC154kWosFXIPuK_4IpdMg7sCCzN8EO6gRz74vC4WnFDPcb4CeAU4N3-8piQFkIIcW7dfHp2ZwhgxDuQuvySYsek07eii5ASvjKJFV4vFAQt9CIo3ObUNPNS9G3PxZZHnb5WSf3YZtJRzp424bP9TEz_F1u96qFXg0GUZy1q-DjWLlCd7-Bow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLT7PgUvKOqPTwfdWF-lvlsscGutgou3pykpGlFQSZ47RFm9fGmwZ8mgF-C4euBHqchQD3GSGDoyxqvBaNrwSK7TKGxCmw-Ls0cRMqzJj9AU1UR4M80wOY_qH7zHJlVgHmKIz7cY_PUOhklkAGymuCgGnpKjFpUnxtRrXjVnqdP8wmOLkSEKr_Uh2v0Q8AKhvJbcdomKJlJHdENgj8bKbA5Vl6hg0lOwB560A78TnPC4KhP33__CZ7fhDdJ2A8neHF31kuC4aa52xwxNMstn4iStXzWFVrDhQbEfinURx5zQtlAzT3iOhsrrUDMgRH6Pn25wJg-0kL09xn8KcPGumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBYn6mXeU2SPCn5pEgdZIbiAUW4xSJ76-jx5K7ccMa9zJ3IxwzmzNqngZ4gp6O7pkwUX46FoaJHkjmPusgcq8pOB9TjdrR5U03vIh-x9pxpChHtaZO_5Aya6USjnclyuWs5wm7-7VZYkhTMD9bpYJDzR01BlGuMxAYj4--zOBGvFx8uAF47frKYv7tV4Pox6X7Vd7OGht37v8Ynx8XDjFV2txRk0QkVjhFXPZB-DUVhP4RHi_Mq0I3T-6AphC4L5GTScvvK-BwZyhaBpa6MgFI5T8-cpwdRAQe0WactqfT6feLcdVbdE4qK0hk5GSWDZevrDc40bCRAs6st1_SxwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
