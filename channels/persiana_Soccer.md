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
<img src="https://cdn4.telesco.pe/file/IFGohYSVqMW-9wqVmU-P_GkRKqeLmVWqn0wQS7Q8P9GTrN2zPGfJlpcNI0KY9ZJ-1WG3napKAPuqzzwD9PyD3vHUwzdPbVe4O2lhSJE2bPxaHY3jwHb16-WnaJkH6meWnJsGFqdtFS4k9b0Xf1HW2qSn0HMGw0Y-Uu16eU8n-V0-SnbAocpkPngNzZmmUJfIDdkSIg5rQNAh0qzHvE2pRbFEKekK_35dyh6t8E6IDZJW8DdX2PM9_l_lBoXQQNs7pmAdIbczQdLN9Q5BYHo0lpILm7frXrD-xNJ6RCSBJbDgiTQkkGEb2r1Bsacci1LNqAzphnAlIze2kH9eTO3DSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 432K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq9PWfRS50GEK4h3d0Ln_7VnNItWDLP_BxjUkpfNvHmCW2ZsX0OX78_ubxHWNWDWyFYVc4Kt-40pttigIXleusrGyDZv6b04jF11_ZomESmRsJKkbvZnf08zrif2GBvg8TeLw8UjuxvlJ1VjmZE-KpV_P20vjm9O_L59s7xMSu6PUKb_52t1qB77esewhI4j5UClJKg5tV5Su138syTE2KDUfhnC-T3quHLZs66s6xaEA8NiDGHewgakcjgd63FIyiT7klxQE5tMLkx0V15bqBSM0aVbyyW0s0aRHU1pTfn5g_wawj9Prg0CpmxQeDZjHB9GVOIMDWXJ22AT4sTLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ1H6Bn5fxcFS6DR_pH6ioPO6ICbonASsMgDUYx3qFPAl45Ba7isOK0GdhQk_6qPsb8nq7dEB3Rz_oubeGswnH7jD6hq61US65LQc5UR2JmaX_ToFAofhV3wXREzv069pDDnEobM8_f1xBaXB0uEK8oN6X9vOITPbDk-4H970K9zyDRm2wVBxh8Yi7eMuBg19hXi2xzJSTY8Y2rFhxyVdZrRwO7BzEeh6FWAaE9NgbkNmlz3qQQTryT6vsI3GEJxpDHxuZGukaA_jQ9EWU7EqmA43Rj--fbU_l_lUIcjBvLTxdNmF9ZsPwX7sFYdeBXY_Qzd9BXW7lWDgVtdxS_-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/30764" target="_blank">📅 23:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
#تکمیلی؛ یکی از شروطی که فرهاد مجیدی سرمربی سابق استقلال پیش پای فدراسیون فوتبال گذاشته در جام ملت‌های آسیا روی نیمکت تیم ملی بشینه اینه که مشکل سیاسی اللهیار برطرف بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30763" target="_blank">📅 23:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNJ_kXPAKrYz7CpNaf3Kalyun9kQFQXipQ1xxjFPDajMnUsMpYaag6erBCE46qgsOvZXvVqtcDAhe6CdgYP_eM0y580jbRdyotU2R-gyOztpDR1MtcWVR3imPgS8GL2OE_lIvHeI2l9oIeqjC5aHctqGZ9zAHQO8dXB0bVCuRWF7AxREeUQSgE04lmiS0Q1ZA480fMccVFDSud_eDogyYgtDA7ritnUe5jzANUO83X71dO1e3_BNcW2dnDF1OLlvsfkapGmIAHbk2-A6TshjsGfRxK3maFGmktnWC2oX1HkNwpmaoGjIzbFkXL8-QjNvIvI18NxR1DfIVvR2dCy3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
نگاهی به عملکرد و افتخارات کریس رونالدو در تیم ملی پرتغال؛ بزرگ مردی که یک اسم میوه رو تبدیل به یکی از پر افتخار ترین تیم‌های اروپا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30762" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arBaHdAhsXRypl5Nh1NGzyyCv26TrohO53kEWat7gdljHi643jJ4b3xIxcVjAwIY8L9XFH9hGsktVVh3wDz4qEbrrOS2MdSxixKFYEvPzAvZIna69FNH70JXJNKiLvGtacjORMXrd3IGYI1dFlf1RIlT6LzCab_rlJ7Ydgq6f_Hz57p9iXNNZ8TalKQWY8AHSoDFLc2ag860G2cikYeM5TxZRZQeBFFqI3LTBd7bKAh23mFSIx7HmM1yZNF_hme2dFUitiJnZvZiwXTy4-_SFMM7V5Z9Q-hBGWkYPWh7MCbRwkWWxccp8elIn2Jfb0zLpYf2Pje-r6LZKWty9FDFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعدِ پیگیری‌های‌میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد. خدمت تسویه و تحویل که بعلت‌مسدودی‌دارایی‌های میلی دربانک کارگشایی مختل شده‌بود فردا عصر پس‌از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت. همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/30761" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkoi-jrwSsykb1hC376AK1N1FMT1Le4M_tDEjUovKLDt1REgPcQC_2qMk1nTShxSq7rzYVSfUEE9WCUN6poNsB91NgPfUuOHLMdNkJ8R34vmBOrX3w7ZQON0sTWXyt2sNyZ--hL2dyo2XZ9XJmg-jkdWB6HRpHsT7zuGdXCoRW0QmWXhI7f3dOTciQIK7XkeV67L1kPvPFMIqiteVX7vqQBdddZ0KSfYxpYioh-fde2Q4PG1XFKaAmy1TZeRRMjON2tin-Yx2iThB10JU-06VFnveKg4QEmrcUBtGCrf_GCPH2cJQZWDEcauA0rnBXzw4ncAnJ8-R2HJrm_8MQET6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30760" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGAaRo8ZgtJN_AT190xwsZnkAUFhYYUOH-zxkcz4OAjTPJTgjfh7yuqT8Fbbeeuwv3XAksFVnDqF3kcmILzj6AIa-N9zOH3XVmcNHgtzYMMCPWk3-Yxt-XV7Vki9xqK0ikQ1VgDjkngrQBqI2lbYOaAZXSAgLdrMml81bJiGqfy_xh0BnyeYTxyTzZFegrJSCFvo82dXDe53XsUnvt_BvAqkkkBp7kLrRhBew752eI0pXlq6bIk_mqQRISQs_ndljKos5KG2J52X-awQ4K8ySTSTsocFXfa4Gbq6gaSuUTn45zBcRO0RUqsIsM-jW_xaYqYxcnIb6VTIuALyZ3kL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یورگن‌کلوپ‌سرمربی‌آلمان:
توپ طلا؟ اگه تعصبو بذارین کنار و آمار امسال رونگاه کنین متوجه میشین که‌توپ طلا باید به مسی برسه. اون تو 39 سالگی یه تیم رو تا فینال برد و نیازی به حرف زدن نداره دیگه. چون با بازی کردنش همه چیز رو بیان میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/30759" target="_blank">📅 22:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUfD-2wT7PcLrq9i6mLGN_jxufYPWsLgw41Q_bxN7RHLDok5Ed4S_mpb-X9weCKS4UxLq373t8YaAsTdkEalsvwawrRRtvRZdulARpMMkiBhJDL3Q4a2dec0aXPWLtKeWx1OqcGlr-nspDizxEnsK6MH1KKZbArWJ0yn9sJo6nRv4MnQEwjWpLUnhZ_eYnt-McvoVGwuZyeMjqRTjQBmrb3r5-rxXiJmMaHYTfHMX1D6Xk8jYon5IF0JNB4tRnDTDuDipnixHslOFjYynzeHbLAIrhtfxM6DNb1LZMttaKLkULuPCg9zOoz8fi_oBUhilYi0yiXLmeRK9g64TdffVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کریس رونالدو: اگه کادرفنی‌پرتغال نیازی به من نداره خیلی راحت این قضیه رو بیان کنند هیچ گونه مشکلی بااین‌قضیه‌ندارم و خیلی راحت کنار میکشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/30758" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH259du6z3Fsj7cLyxwF2LswoFt536wqeKc1Na5OqFMJ53GgqcJBMIagq2zZcudUdyh7oixM2D1-uLHeGHMIIljwCGnT9TMutIpQm5FIQGP5ETWZxdW6sd_TMDHoMkSAqu2m9a6_arlaqD4aUp__fHHPWmrl_k_OZvgkfdyJqB_1WzRdK9ah-gA1Ne-tmFTQ9KQJsGi5y3tniYShk7J3pgt6ZqW8UDVtkwHSET1ZNxrO9Ere7DpnR-BKlulFuFUUo-APmeFxsJAvdrw_dNnqsk9tKNgq1dF8-9yVo6GiIkODW8LAL5qUTDN4ZhgphrGPrQY-G03w951-NR84xXS-c4es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH259du6z3Fsj7cLyxwF2LswoFt536wqeKc1Na5OqFMJ53GgqcJBMIagq2zZcudUdyh7oixM2D1-uLHeGHMIIljwCGnT9TMutIpQm5FIQGP5ETWZxdW6sd_TMDHoMkSAqu2m9a6_arlaqD4aUp__fHHPWmrl_k_OZvgkfdyJqB_1WzRdK9ah-gA1Ne-tmFTQ9KQJsGi5y3tniYShk7J3pgt6ZqW8UDVtkwHSET1ZNxrO9Ere7DpnR-BKlulFuFUUo-APmeFxsJAvdrw_dNnqsk9tKNgq1dF8-9yVo6GiIkODW8LAL5qUTDN4ZhgphrGPrQY-G03w951-NR84xXS-c4es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وکلفت ابوطالب حسینی به رقم قرارداد امیر قلعه نویی در تیم ملی فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30757" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N963pTbc80NeYoyJqYidjHxf2k2VkKLdX3CQK0HIFai3Dxl4c5h8oH8jA8AmGWjG2zxBelg9ikf4TcfKBbvTLVpkA6W1m9kZVPecDLeYQTpLtBHZBl2L9vt2dMZiaGoiR_CTC1GhH4wPk-atHH3SCOPsXTGcMY1omJWbqylmD6fptGK3TgzetMYC2d0Me-f-p2Q394V7HVwNz81ooSf_A4W_aDxdPf65ushGy7F6iVLABDPy8cWawQf0Vv4--_bafM1h0A-pHjCnXw2xiuCQtJdMnr5bl7CWn5zMX0440EPXKs2xMW_iHuI8XSUifldX7IetfEL4bbB9EB6zWfDCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/30756" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzwzeTbqODUp8UGosLSUsAoNAet6RiNSgWWNS1vdpNGXWaGzECXrk4LWKP7xJhW8mhPi3v9eQBHy-GOSk29Exw3b2eEcFu9YNNDQX9qP9aLQH2v-rDbpa_qffBOPcaYqjcSCu3MU1n-xBtu2CUa0lgoXuoy1u4VPiQDSbCEfD2jREgOCUTje65ZDIpdHg4V_mlCCeBRip8EOnoSxqDKpVkKv0UGHvjh3gdIxjbNTPBYJojwh6TzoU76GgQgeW9peZfIB9Blt3cGF7qFFkNxvzuIlvuZxOzdE_GP0WxPZII4PIkL1YXaK0I5Mzsg6B0abl1xk86rwNrHmvv3wGafSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30755" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwkaFtrCLm5szlSomR-Q29RQc6oJJlr51OT7mtnY1xcTm_eX1GwmzYWu-qtV3LUL5XvES1tnBoUIvAgxS_3MMsKIYqkPJdwoE3wYjM51XkYR3HIcN0k07VzQ_bval8nKxR9bC8FFXhWCtq-MuUokUY-OR4KJNh4aURdCEMqe8bcJyt142g2d5aDCQ3DGU-EX3o9JrT5zHwYmTgfAc2P_MAGMOWeHFL7cycRSMqPXsRH6a7WjM8UNcDYoTyacUSFQGZ0Vee-_ReEtzpOEOfs9bEfplrusCaTsSm21oQW25v1DtrLyy5ITz57OYqv_VPBI4RW0oOXBgR2S6l4EvpYORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تالار افتخارات ۴ تیم مدعی لیگ برتر؛
استقلال و پرسپولیس با ۳۹ جام رسمی بر بام فوتبال ایران؛ سپاهان با ۳۰ قهرمانی نزدیکترین تعقیب کننده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30754" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=IB5jGEQdYCgCVPRCz5rvcN7Mo0AhmKx6iwp2-yxOH-B6hMuqtPax5V_yLYx-STh5h2dXc9KZ3s0q066g_lGAga_C8D_zAUILNUmvLNTvMeaT0OjQRIZZs7YypjwJhvlZiZn7wVpo-DxexNlQ6m-kP7GY8Hfqtb_Cb4nSAGdmpNIAXGjdwnYonIslMIhoLra_h0fJeD2RNKFGzxiWmazjhDZSsX4zF7BzA3U9iEdCCOednpI_JIiY6U-36tH8B5Sk2Lk82xPVwqyZ1w-4QXB7CbI0uIfSQpW_3WQitFb2bDy5iQ4efz7HU5j2E9eT-CzFgooazI758kbNaat7vuGrZbM39DXJa9S8F3T4VpLyli9EuISQ722TEDfDggSEbhfzbnOG0BeTBbuFRkrcXq-lTNpiehqtic_iz4GDEoBrnZit1J3zOvr9VHS6CZTnf4lgEl1V_PFOwjANFJk4dChN3k5xLpYBmGxrKzqFYloNqY6ehv4GH4prWYCvTLohXmPIJuclSyg7l_ILh8ZjjYvqT2z5qvUj85CLAbc0Mp6CKvSliR4R8k12UJPr9rT8JrGFNERtM4E5RBbysCbCiSwCqVssrrMNnCKlAkDs3bVM_Sj-m-w9TtNWJ3bxBJe3ROweq8xdRCfc_mhtCl26M4WRo5KDoV6ba3W4suvG01UEFE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=IB5jGEQdYCgCVPRCz5rvcN7Mo0AhmKx6iwp2-yxOH-B6hMuqtPax5V_yLYx-STh5h2dXc9KZ3s0q066g_lGAga_C8D_zAUILNUmvLNTvMeaT0OjQRIZZs7YypjwJhvlZiZn7wVpo-DxexNlQ6m-kP7GY8Hfqtb_Cb4nSAGdmpNIAXGjdwnYonIslMIhoLra_h0fJeD2RNKFGzxiWmazjhDZSsX4zF7BzA3U9iEdCCOednpI_JIiY6U-36tH8B5Sk2Lk82xPVwqyZ1w-4QXB7CbI0uIfSQpW_3WQitFb2bDy5iQ4efz7HU5j2E9eT-CzFgooazI758kbNaat7vuGrZbM39DXJa9S8F3T4VpLyli9EuISQ722TEDfDggSEbhfzbnOG0BeTBbuFRkrcXq-lTNpiehqtic_iz4GDEoBrnZit1J3zOvr9VHS6CZTnf4lgEl1V_PFOwjANFJk4dChN3k5xLpYBmGxrKzqFYloNqY6ehv4GH4prWYCvTLohXmPIJuclSyg7l_ILh8ZjjYvqT2z5qvUj85CLAbc0Mp6CKvSliR4R8k12UJPr9rT8JrGFNERtM4E5RBbysCbCiSwCqVssrrMNnCKlAkDs3bVM_Sj-m-w9TtNWJ3bxBJe3ROweq8xdRCfc_mhtCl26M4WRo5KDoV6ba3W4suvG01UEFE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30753" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyAilKfZr-Cr3nswfg11guhdY7X5-qX_uABwepiPPtk1exRY-ryk8c1zt9Sne9Yfs1E5PWLuuQFF6Z5s-6SydJ0kWYil6UbgeMUcS8WG3jPc5i38GaZcGYZUhvO2BNEJHou4XGD784UfPApoDSjQgMF9r_2Y1dR9fzeXn3Dn-n_es2Q0s9qHKt4Ov8HcNqLsBLnshZMBh66i93N8Uah0OrFSvBhRdj157EYxXauDSlZnsx0eay9ovMFeMoL3t0Gbb58MB5J_V3tq2xoI8zCs-AFPgiwTPxWJzJmLgdZGKx9lEkCN34QXoHoT-WRnUaQSJG55UoxgcUggOsPL6MmW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30752" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=jf7fxEU0SRI0Rk3BeJsidT45SNVa97yG0bkIA5fPlvb0uMom8CENmF34UwdauMwjJLf8nwLbiVDxwH0xpE7ldL615Oh9RJ_Opow3Rco375gry-Ggbzb9ISYyRchlycO0MgZYsyWbpnAOGAULmx9lYqyt4Ii6Du6c0boszy81XdB0Gi6K1g-VNu7SQonjhFnS_VBsQLQthY3pNspxo09TjYWSd_5GFnv6GMEpf9bba9IYtEGjksgw1ZuBzytfK9Rb7w5txW_pDxHqznaYY4OszYOvdk_LeHtZauQmTKqlav0Q1MuV_SjAY8VctlEfE3VsNkyQpt6_J1mupUC7o4yHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=jf7fxEU0SRI0Rk3BeJsidT45SNVa97yG0bkIA5fPlvb0uMom8CENmF34UwdauMwjJLf8nwLbiVDxwH0xpE7ldL615Oh9RJ_Opow3Rco375gry-Ggbzb9ISYyRchlycO0MgZYsyWbpnAOGAULmx9lYqyt4Ii6Du6c0boszy81XdB0Gi6K1g-VNu7SQonjhFnS_VBsQLQthY3pNspxo09TjYWSd_5GFnv6GMEpf9bba9IYtEGjksgw1ZuBzytfK9Rb7w5txW_pDxHqznaYY4OszYOvdk_LeHtZauQmTKqlav0Q1MuV_SjAY8VctlEfE3VsNkyQpt6_J1mupUC7o4yHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm9UzV8aX34N1ILOj7y8PZTPq1gBmd-S81XYyRZii0BSi3zlmk0hGPjP4MiAcLfQ6ynVmuCcM914_fu0BPK-TUXwzVkdaKev2hP5fw26lytdUtJbNtkyKj2-lDbRy3mTlijCjwQ6N5jBpZH04plsw3SI1G4cuYP5WdBNpbIjsxsk-JVP_xf75zbrtfsZgVORZYPrHbsueSbDV_C8VnZsyNN6hWs8JhIclZ4pEOXJZVx8w8ZXyYDSYfl4Zzc16KBvRobjOGsdRote0oOpU6wDxdZh1hcztFAw9JIWGRTwOGrL5HmsxGENbIzzlhcKqZ60vqkKB1HPTUFNh8_DNe8sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=UoZsuJn9rSNwa_1V96QrVaeNoyFvI4Eu7V60v-04guKE0cgRHoyCO4hfRAsCbf20TDDeH862yQz7vs5y33LNcU-jxUqsJ5yefBosiVAB-hgFccClMgn2H2HY0mvpKRs6XRBWVvpQzv4GL_kwAaxtJ9HKW7C0zvbfyEZKxgGFH0su-NU5r2joAVDnMOPrdBC1SGROYKElIlDE7AQ5-SZ7xxWZbtDaoqLxSnttU2sgUDTmreLe8qKPGxFPUZOPVmshJjwpvKHQ47gY1JaGvUsxWW4G5lwUG1wm0Z7ajRB4Hm35at5gQsyf4HmPMpDqcTd5xGUEunmS81wWmPYXdPIV2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=UoZsuJn9rSNwa_1V96QrVaeNoyFvI4Eu7V60v-04guKE0cgRHoyCO4hfRAsCbf20TDDeH862yQz7vs5y33LNcU-jxUqsJ5yefBosiVAB-hgFccClMgn2H2HY0mvpKRs6XRBWVvpQzv4GL_kwAaxtJ9HKW7C0zvbfyEZKxgGFH0su-NU5r2joAVDnMOPrdBC1SGROYKElIlDE7AQ5-SZ7xxWZbtDaoqLxSnttU2sgUDTmreLe8qKPGxFPUZOPVmshJjwpvKHQ47gY1JaGvUsxWW4G5lwUG1wm0Z7ajRB4Hm35at5gQsyf4HmPMpDqcTd5xGUEunmS81wWmPYXdPIV2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwjTi6Oys0Jq_LYg21aU1lMpxSyWr765utLYM66masNeJk8YU_gStxApK3WvuNk1Gv-vY7LY2ldwX5SeyoBg1SyGGVqzTYbPDkDzxqRbSGNxS_qcAr33uRU3PPqKUb7mot-SPyIYwduZHDCjiJxCldSByBuhe1E-qdZF8ozfxkXE2Yz83L33J3GCiM3MN8RF3G2USYvt0jOKKwYb9WSm30CyXcyjh0YsUOFV7MZOVX2VqUXAyBo4cfjxxvJEodLBkmG43LQUYq-h8jnkkBeKBi5N-Nnn9oOQKbHQXnyNVTs3hQAUIUjBT4PRRYHwB5O29qbACIgTxrkluPbVkIIjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/30748" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz3xoEsEipoPRkDcjIqPl094cyB0Hs4xS_8u0krimTCsgXZqo2mtGr34TQx0PjDj0gTTRA70SdvYU60HxIi944UMy4PBX6_L-e_yae1OHyWzNRn2NKFm6kPS6bIt7p-3KjFk8PNh9IwIUoA4R-gh3WJkR-UPyL49hBP5JlHCwaT7IrGHQf6DasIhoG-PTyWCyX_rumZpn70o0eWe0cTKdYmsgFLxRap67gIqOgaMUoMTvjgJiwAdslYPedoJLlKXFKk7naH9yXfw_P_ArB4liOm4bG8GjTlPCSNdsSbRNrB27-2I0u6HVyj_7FMqe1fXaDU_2eQ2XJ4sJ2ExvjwbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQbdrtn1g1RGLC4P_9Jm0uJgTGj0AadMTEOc8kFgWvHD03Mg0QR1tKm46vMuMpZhjt1lFrAcWINRusQ35hTgglUM-mxBv-izOUHYpkXDILij_K6YX5Dt_bcOxJuNp7g2PtTQ2W12U-Naub4xhmZrC8ZIYgJC8ZFdpUiUXBCzf965LmlVTULd8v3h1sXA8EHJ-6e-EzbVlhJiHDXQBTVYCV0p08pYfalKEJbclQiz4bP1OdG0eizSonvEa_Ivg8ZZnIbyJzthVTZy1z_hf2w3_ztixoXxDk62_xal3psLOFaO-A8nM15wNj5JSyvdk3I8ipQFYVO4vTKorKH5-XMg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛ ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30746" target="_blank">📅 18:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU2qM_vBjHwItLFBiQjGvV-qHEIuUuQPkoSGv2dcrApacL22FJ-1qn5q98ak4VhFQXx01IXvx2m7JN5_3l78S4gAl0cKjBgOK5kFhC4ywqR38gkISw1Y0D_BKPeVs7E5Yq7JsPAO66QFN0VLWEkpNG8mh57LGXefDZNlTtLmi6W727OXCjO32zU-YNaieSnP_Or1o3BVIiPHyQPOsEtUMQXPygpT0uvwlHslWRoYK03PxCIEFBKSqjX7Gw4MiCRjIsZ55ohivtwvECZgEaxRq2mn5zegoWX_w7VoSllhv7liOcFk5vO-w1okoxyosB9AbYpvcQW0cwAlzB_1-CBufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛
ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30745" target="_blank">📅 18:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQYI3LH1oOvkNU2BYD7GyBYbSBbdSFoBALNRQ7djaFc-XBP63925eRMd6wk7UKxgCoem70nRl3-49znXAmKXfAf9o2mb0T3YO7BvEjg8jHOCG3wvuGtc3xZVvphpd5040RH5byK_WRBO9zmG5j6rIjLTs80xbXxFZV6hd7EYXaQbeFQiuxDqpswzYTrYmTzzJoreANZ684n64k5KE-xPXGrdex0ZL6V8urFON_NRlc4AqaQnH_-CmGWlsJNiQbTw7DTYn5eVGMpofhI7sB_j-VsT-DA0dcH2EbSHazwVntQv27SEkkBVmqtfIHi1mMeeLV5WYhYiaQY0wBlzalXCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتقاد دوباره پیروزقربانی از کادرفنی تیم ملی: من با تیم آلومینیوم تیم ملی ازبکستان رو میبردم. با احترام به کادر فنی اگه سرمربی تیم عوض نشود در جام‌ملت‌هانهایتا ازمرحله گروهی صعود خواهند کرد و دراولین‌مسابقه مرحله‌حذفی حذف خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30744" target="_blank">📅 17:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4OJ69h5U5YD6VjC2sK2XvP8ohB0LE7RxkASFlrVsskXQPIgHLzG4UZxzHoYD65L4ePtiC5S424_NRMD81UBVkaq-WIiBuScUSxCFkEK3N2fdEsIeaiXATSnFF9dT0WHDxc9Vh3t1vQG4mOoztTgPYCgU8J-hVJ0fWB2M8bvKAMqpy5fBypgErFTglkrdN_C6b560I0HHe_XEhUNv0_I9ClHEwjNb-TWRV9sIEpUAGGurQGdKQs-TAEaGGzLH1fVteAAEcjCtAcf2e8V4pu7YOQPJlwTeg1mgxzAshIvVPVyahA6Q7Dw_EbXJM4qPC16yChw5FwmaHxeAaEFgF3LSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داوید نرس ستاره ناپولی:
وقتی خیلی جوون بودم تو زادگاهم 2 تا دختر بودن مسخره‌ام میکردن. پنج سال بعدش وقتی به چیزی که الان هستم تبدیل شدم برگشتم زادگاهم و هردوتاشون‌روبردم‌یه‌اتاق تو هتل 5 ستاره. بهشون گفتم باید برم دستشویی، بعد کلید ماشینمو برداشتم و بدون اینکه پول اتاق‌ها رو بدم سریعات برگشتم خونه تا کونشون پاره شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30743" target="_blank">📅 17:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZr7jp2KM4dQuzT9c7NRN2SYmQvKKevGf3tENlKJvRwphT71xZ8oG97XGNmojW-S_7cS92NKMVmkTCF6IOXqJAL1K03r7kuzdRjfLDCK_yp0l9KUSL-fZxSdC-Njfgk7uhwPe-4U6_L_9krZrfaiP8jo7swIepst9CRGlgE-X4yb0pER1FRJWprV1wcstjEbG2Gz49beF5maxxUQkQKkrBB1MlFM94B0yxX2pjlxsoaNRT97Z2TjYWjtZniIWuemhREuTZydlVXbY1INbqaXaHGGtwD-ifhsN2uI_Q3LqjOX1LOvG4-mC5c9Qndvc98AknyUK0xSpHv14E3jLkpIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علاوه بر مهدی‌ترابی؛
مهدی هاشم نژاد ستاره جوان تراکتور نیز به‌دلیل‌مصدومیت دیدار هفته آینده با استقلال در هفته هشتم لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30742" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGpjxCwhxoaDCx056qs3B5Rs5ZwHxw0pPONunYvm3KA1IXPyd0LHK4kXnt9Rn---bVi6i4uC12bU3TiKUEDFhuJiHXRmrINxiFv4t6bhG7g3le-D-hLCUtLqE9k5LthDxD4976lGRRCtR3FIzdUpuX6THJOkqo9ERJNK0_irvQVHxwuFEBcKcwyC0PE4yJOzQp3ghv5LwN3SqeUBYnpigw_mU2h5KJgjUde65wL-Q6AUh03Q1jaWkdtE1yVfIAxbueIYxbnl_ZooXtOeKJbIcmJP12Ffgbh6cqzOUuNYoU_JsRFSmtJVSAJVTuN_mIGcLu9-hFiZ_qhEUVhR5bMz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
لیگ‌جزیره هم ازباشگاه‌منچسترسیتی بابت تخلفاتی‌که انجام داده شکایت کرده و احتمال گرفتن جام‌ها از باشگاه منچستر سیتی و سقوط این تیم به دسته‌های پایین تر بشدت قوت گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30741" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30739">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjGuXAlHvdDHgBONr2NmkdHoAzVqgB8D6p7SJCzWWFeZnSmkNBH2hmXkO-0SOhOjfCAXWoKWsOrYHEPdhM3oqGq8mHvPDZKI89DnqNuLmh10JEoPPTkUqy5rbL8TPmmzEKWw4LIldITCsEgYwNb61pddPjL8FaHnQCCpYSltdzCgvLFRfGr55DB1ShtVUuYKpdMyS3XXLCqDsLtTnylkfrU3WpGGQv5-ifztc-XhkVnaWC-1BaH4xGy9ptLQn4MgeVQn92SeZBb7UzVC-6so6xoMZuYVIGeSqlQrdCZ3TAyjDvIrel8IZkmWf7VhyNeKTOPrndBAAIxwm-6t6aj_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30739" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30738">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
#تکمیلی؛ طعنه عادل فردوسی پور به بالا رفتن عجیب و غریب قیمت دلار به عدد 245 هزار تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30738" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30737">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb8jkgRHn3qJIgmJW8ldXCSsTjnSLhFdQBLg8L2plJ_aKzK_pwjoufqXMCBCmB3NsELLy6KkIf9MzJOPvnHA9S1wO3RaNBiLm3vXGieEQ-k8485azYzDDiMrWJ1h3Ru8wI_HSjH0wn7xWPOXsjSrMHJ1XYFVzn9EWFjlLp3FVR20JL_uWaV08tVWSzvonN_yR0zjRahq9OIqzK18MPd6KL6L_kVdeX4VBUS5CZvFgYmTk5oh2RCvbN1hs3MNWB8l1dNFEqqFY0ctnm5GxxPCNLUF3kgY3-k-du6JVxnAxYBv4mFetgjuMfl76zGEvbtwMU4IFnIVgT-XW9aSvv8sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
نشریه‌مارکا:رائول‌آسنسیو مدافع رئال مادرید ساق پای راست مصدوم خود را به تیغ جراحان سپرد و حدود سه ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30737" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30736">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
کی فکرش رو میکرد که نکات فنی مهدی طارمی دررختکن تیم‌ملی یه‌روز به مدال قایقرانی ختم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30736" target="_blank">📅 15:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30734">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsEv9A-OjNiXxgsRDX--KDK8alwFWn7Pq0HZWJoAjgmjh15P36jJOAHS3cy14CyRgf47EmARJNpfYcLtYRJqtQOG3ns1pyib41AyjdNjEmNuHghP5Z0EcGtsllkW4otu9_RkHf1ywLBGCVh4kzuuxKUi9X3orsrImIzHtnDG0HpMAtDaGbhjsUrLrXCEYnPWj5W7K4DN0F-32HlqGIuYBR0g6DkDhZrVn1zHSvIVwq4OD6dcbpS-45AXq60qknBwBeNytd_oVmnKFjfUzK8YC2OOn8KHvFsT_VJ07ErsZ9CES2LrltEUJ8QSkDr--GZG5r4_cpB-AQnxLqQU6VF7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxpPKrm7XMbx03LIoApLg2C4Zw8FQBE3fEwNABbWBlS-rR6y6vxgG83CrmAtwhSr3-ukvCfMfND8xg7mh7nodgyZx9r9HXXSfouB6OZmQwMBWAn5Feh87E-tO1qUnt8SAZDSSc-Lg0KiQTvZNfrawAvlyQsko5fI4az0GAdIUzszpWZLgARbrK_0B1NUx9g3ZvVgQFjAHt4ZcYUboa9kzpJD05GLMGvn227LaQnxrb9B_1Dt19rFk5KPNeMp9tszZvSNFFi7bV8oHMqVatZDcS1WvaVg-FPjbStCLR-Ew6BkwztUv2Fzdiq5Qud4664AsZsAab1ACuOso4FKJP1ggw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز ستاره تیم ملی برزیل برای درمان مصدومیت‌اش اردوی تیم‌ملی برزیل رو ترک کرد و به بارسلون برگشت. مصدومیت رافینیا حاد نیست و بعد از فیفادی به تمرینات بارسلونا بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30734" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVyn62i5eAaa-VeopKnDdq8fZsVO-VeFvuyqTauhylPY36Fug6-DKO1gy-16ejVF9DD30G_5FzM3BTyNqgLdE8Pi0sSXG10WdZFYnslV5oY1fvI4ZoUDZyGkYpwMMSZsM6aw9nNDEN8U8tY8XC0-0C2Q4ctkwDuU0k5vf-jdHNh1rHxA5Fsn4z2oaw6Bcvg8uR6_9ajObTvuva8s17-18gpapKOopuEYg9yn1gFe61HWIE01cvcQKi4ki3iDqX7qfa7fFlCso3FjGhVisIHYkAr7FM_bXS9j0L1yaCD3kY69SxzFz-qRNlcS1_D-9uQ2jcH1Ez9p3jgYIVR4MavmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30733" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTn6RtCGGyNtsvWK6Xn0tRrV9qfQUH3vLmCzGMoHvZ9xSigdsRk_jvb8zBUbvAw4pybKeVZ01gTk7VEaXZR-EQ_Hin75JdAKGOo2BHMqmSNYb-10rqHuAD33DECCzO_sXnIEdxYeR1K9MvUL2Mec4E3misCx0HTMCPVVOmK6mD1aNZNzAXuSfxiSdEMm_n1eomceMIa1HBKnsCwQfqhEMH0nynmEW5zYi85aOZ2kbHJb2B7T-xfADMOSkgKieIqw2fxcYqwQrZFZjFgl_RC8y8Qn1g40yOb6VjVXZfuilkgmiS_4HIviHFpdPObiHwlK0aFHawdA5x0KLJEYBFSBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30732" target="_blank">📅 14:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV44Iz-YVSQ_DXW_i3_WV7vU_jW9LRR2JPIId5FKSHV06smFNFT_l166GBvBRISgGoVupvfu-wG1HrLFHrBrbrmf8CKKeQmLjVBu1urBv3HvDSlbG_q-xoKQzSK3cx5dTsC1eMWZf59Ck7bWO3qzQVZeF2OnY6v4FggoK_uMscqH6hWWooxtoK2pAfFIsk9IDSEaAV9c5yBm5Y9CaEGAVKIGfx8wE1-Vb0vClM11dObjMkc8XCl5V-CTitqurZiy7DgAo2lxQL3L2tk830IBuzuy6lJ97DoAsfvl_4ZafdKTGn9rN-bMCEtiAolsQkQAn_i-NvVBD9DkN68lb127Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
کول پالمر ستاره اسپانیایی و انگلیسی بارسا و چلسی در کریرشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30731" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdtr_NiNt4jPn2ScMEIE4248sOGnFgFO-s5m7WS-zkAk8bctZ4-TfXtLQ_u7BOnboQWo4evoIWApmIvXzJ_vf0D3nkhCD09HHql8ZS4AErN3M-MdSitaDhUys4nFUZlKPuB6Fnt5gvDHVgJZXu4eU74inq8nWyPnrwD5VXdbwzBwj-OLdMuDJYuW0H7zkeE28Vagcq3tFnFFEWfcY-MYkYNjz8d1twSw7d9WAznJuG9Qyh4AQfpvR9sbVVBwN4RbjgLqDeZuAp_KM5vbF33QSWoTm7b2FZ8kvQMiGDndrYSBh8o9JZ3oVP6LmysO_QxGrrdVnuhJQeMV4hRfrdUh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون: در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30730" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peZJuThxtLMheQ7OtHW6vlIuQPp-yYKdyNyRp0NbP2caah0Tf6kniPGm9U3banHmduWNzJGdjZrmhVDfzYqhQB6BcGwcBCMOuNj8KmD6LeVBOSQ63vfWAtDMOdWFcxmj2jSyIOweQEJjMX5CB8-EJOV5sEt4xIuh-dAhvJ52lADD7RF4f8RBhXYs76HJN7qzmAQbMtiqVSev1iD5IvlMe5nl1NDr_FudxXw3glWOkMhHbJZhrON_TKCla-Gp7gipxLovFgGc6jJu6dI-PbnucEWbuQEDsSmJ5gnEwlNqB6gFxL5IBbzqQ0lo32bfx6fMbQ0CvmR46YlATcjnPstwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون:
در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30729" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Jen_QnsF_faD4_B0C9o2PG1HdVRcJW2s1gB7xKetKPbz-3y-o5Y0zq_RSFIaYbhD_WTjrX6FCHFULkTwvD7W_FH-0Nxj5lJK4Ak62AgBkgREwuUylmqGnxTbLIUp-ShcIZqbWScHVkABKvIj_RKGLXgOBoi9QVL12LHX0OotvD51YnJaYgTApwCiFVE_IFfrZiodDyOpAyzflc8Id2UaNfb2OSTvVz4ZFPQj28J2JwhPbqzkUWxXSgjyMVLLWaxx4OU0rBvsav23D6eHwjSd2DEXqJPrgOfZeZSETyiAlq7fMEMQnN0fY86O-QQCHGA4uUmvyjt5T4YVODwVYFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ2rHPfzD0rr_qiuoPlVfb-N2BPACjhanJAhzb3dNJh8AQ3zEOWj11lTwTUKFtCYoAS82oIAmhtz2cRQrsDrS9QF7lC_djmlpNph6Q0Fa2g-Fd_TwJVMxNUvNBwUAJOsBi8q_wspyJCsEU-tfaSIG7dNZVRLylV-rNKFQ-kHdYIYyrArM4xACe_gMTEMXLI7yoY_CQw3CTbowtyixBvdOWTyFGb43INCQdGJK5eNMMi5i4KUrpoRukqAdYZonRT9mmRxIc-cQ3_QV8dtbgDUrOSdxpximAd_IKsOmJrXR4n-pN7uP4anqGfyPYdZeG04Evr0IaJ3sjn9rItTvZsJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCzneA69Xz6480lRq5cd4pKB_TyvpUu3e0aeFuGJIV2znw7xL7W7ZgXJG-70Upn7Svf1DLMGLAaJvvI4vjDqsIBDZGW9fGcZJxISEdrYuc9xsA5wXmbKA_ZrvmTWj5_ALHmOztHHeJDxB9YQE1RyHhCWp8ahE3rbAse-hHMH7ijX_JfksU6jVwXdqiAJ7kYaW9IImjY9A6dnilRm6qYU5RXSVW179nTiXRBN5fzAKAlAbgE_WA74mUn3sJRMMXJaprcFdUkR10wfokyRx8LwcYQSNjYVzpmwefhBTXIFryGT5YXMlk1yoM4mViQPzdQ2zL0Zo2Yhn8A8hPJUOXvs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30726" target="_blank">📅 12:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=ngfIp0rBtq0a1MzReZ6cU8GW0yceSbIzopgnPn2u0rTBwbPGc7eg_1Sl53ELDA57yWZiaG-xB7MsYXgwCurTlYvE4lCSPgLKlSZCr4k28phNHT1RaOojHqCV-BaLpHRkrZ32k0q5EAYNiuUU2bynV-BTSnY1l0QVmc-Yl0b06VA_icTbp0MYNetyvE1GYn8JmZV_afOjSW30-IcTlBYXNfp1r5Ad3BxhvPU2ZTz7jqx8wVcKaG2RMBdYxfk4AQwTg-dnu1nG4LQSPAldfGUBwNt1Qukn7XSCbAaOrdu2pd5mqOATerLAPMaNpawjcOHTJKUfkrrVFSwng9UmZL2kQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=ngfIp0rBtq0a1MzReZ6cU8GW0yceSbIzopgnPn2u0rTBwbPGc7eg_1Sl53ELDA57yWZiaG-xB7MsYXgwCurTlYvE4lCSPgLKlSZCr4k28phNHT1RaOojHqCV-BaLpHRkrZ32k0q5EAYNiuUU2bynV-BTSnY1l0QVmc-Yl0b06VA_icTbp0MYNetyvE1GYn8JmZV_afOjSW30-IcTlBYXNfp1r5Ad3BxhvPU2ZTz7jqx8wVcKaG2RMBdYxfk4AQwTg-dnu1nG4LQSPAldfGUBwNt1Qukn7XSCbAaOrdu2pd5mqOATerLAPMaNpawjcOHTJKUfkrrVFSwng9UmZL2kQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیرتولید محتوای شبکه تماشا: درپایان سریال امپراطور دریا؛ باتوجه به‌درخواست‌های مخاطبان بار دیگر سریال پرطرفدار جومونگ پخش خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30725" target="_blank">📅 12:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQd_igHBeYN2fx5sMWAhWaIGWVGnS72tLKFLG5bzvqoPplhRSZdil1_px47eSxlsyTM-FtrKgNbxxOOBfmYDWaoWiPTMUJZpasS7Lpk4EQdXU6CzB4TxDZ5fEpNiOzerGhw0JZ_rSMYI1uGYxVU_KHh5cTiQeNn2iV6ca-yYdtY0ph02coAHC6I4zIAq5IbWk8zxzf3RtmK7x-IA8HBw8AjCICdCyo5IJ7v50mBC5zbZCp80Wxn_PgeIJbp__-PimnAXNtBZSPIZLA9ieuGzTutxKQgpducDkT9yIN9EAA9TQTMhXCqU_FSJWpd5K8KyarxsR_GK19WYZSD9SZ7r9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛
محمد حسین کنعانی زادگان کاپیتان 32 ساله پرسپولیس از طریق ایجنتش آمادگی خود را برای تمدید قراردادش باتیم پرسپولیس درنیم فصل به مدت دو فصل اعلام کرده. قرارداد کنعانی در پایان فصل به پایان میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30724" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=TgM6ejXwQ5B9Y2M2duLnBslSYPWRVlVSqrco_wVi1PGKm93xwphSLjv-3rjupEAGFENDCtVjijr_nF3xRQE7u-uxGCvWm58bOys_RU7QVIDSSeCErICwwhe2dtyRLq-BaMlTY3rO1UfJ217Yi9Ypj0-7bTY-Sb56N08pdP-3qSjg83LbpaCPi1QtUz3e3BWyyaP_drOvPLYKE_dfOGtEKkTp-3YqOTrXq-I7Y4PP7LdLxNZo_u1bkebSK7yXnuP5_-UzQe8YbKhU4Tau-7Nky2QQFOtC2sTI_LBGG6WtcKyn5YamTTGFHCD0fKLhWRaKLY_giUkdJqtSrmjcGg_pQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=TgM6ejXwQ5B9Y2M2duLnBslSYPWRVlVSqrco_wVi1PGKm93xwphSLjv-3rjupEAGFENDCtVjijr_nF3xRQE7u-uxGCvWm58bOys_RU7QVIDSSeCErICwwhe2dtyRLq-BaMlTY3rO1UfJ217Yi9Ypj0-7bTY-Sb56N08pdP-3qSjg83LbpaCPi1QtUz3e3BWyyaP_drOvPLYKE_dfOGtEKkTp-3YqOTrXq-I7Y4PP7LdLxNZo_u1bkebSK7yXnuP5_-UzQe8YbKhU4Tau-7Nky2QQFOtC2sTI_LBGG6WtcKyn5YamTTGFHCD0fKLhWRaKLY_giUkdJqtSrmjcGg_pQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30722" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWcaN1cmlOEKkL8zTGnk1no3N0W0AlIkLjPPX0-HcUtL5Vbfz7981b0MRnFDSHM8bWAc1ahXOd2s-UzXSEWKQHNxfozJ3h9oc6DDkqjrYBnascddjQrlJmjz3IeTkI3icXxYRAki54bP0En4DcO8TvLiyMUNVNA3B3vkkUeOMnfdHrTVXff4_IWHEb4yQPc-1tpPdnWlOhNP1XIUf3yQlwthrfs4NC5mRayBnTL2ITXZiTlMZ_OhsVuISh5d0t3He1UupjAIv7FHZIh1DrNB_z_ArJt7KB3D2R5nWIllNkedPuIgVOaRmjbk1SW7Ta2CHaJcA8wDvc5NF14NJqbkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30721" target="_blank">📅 11:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOZI4sYRUOkquk236OQsCEINvZ9VOW5arKu0J3D7kBmwQF4JZ4evzupD-uy_4pq1BEO0BTBlrVM4JvPqtc_7Hjgn_bLkXGt4H7moIhslNHFzxvFzkJo63D2oSWohEKarezxJGtx3aUs96LcgrORRKRy12udH5pugb0kzDFUkZ5uCPUouKfDCTaw_hYGbvsWt_CP5WU9a_onlZLHP6q8FvkDp1Sk1WlyUGWBsK3yhY4YCuVxyppOpuFxeVvyrBqIo4MTuWvPAzRAp0MmJ29CeYgqlf6OSjd2lo2XczfhkoemfIVKhDFVhn1zYAvaCb_PUVElniLk-H4Hl8i6OHWMKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
تیم‌ملی‌برزیل امروز ظهر در دیداری دوستانه بمصاف تیم ملی استرالیا رفت که در پایان به تساوی یک‌بریک رسید. رافینیا در واپسین دقایق بازی با یک پاس‌گل دیدنی مانع شکست سلسائو دراین‌بازی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30720" target="_blank">📅 11:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG0LbcGhY90KVbdkABWQq-e7qjYAesBUqP-rTnAbV9g4U6eD5BvGqs716wHzEbKx_q6bLy5SJWDAwwDkz-aWeA4g19FO6nC75agApc8cAcDU4w5sZ_Bt_jFhdk3mGr4uLxYZWYNLslK0LI7I3M1xCt7hNHahQJ0YCTAOhAxPCdEB9RA-M8rNMT_WJgHqE1IFlYyA_ImyP1uuW_-Sa2dzgoFWpGx0KpJAgmyE_JP14AponTyTi9KK-MdMXqxKVYP28hCKJdNsasTc_JKV48O9z1xAvsvY9mOfjej_SIZXVNwrnpv8fto7objIc-KsvOpXR7yGFm3q3NV6PiY86Zm8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با حکم فیفا؛ باشگاه استقلال محکوم به پرداخت مبلغ 30هزاردلار به مسعود جوما مهاجم کنیایی سابق خود شد. آبی‌ها 40 روز فرصت دارند تا این رقم رو پرداخت کنند و پرونده او در فیفا بسته شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30719" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uILeYnRW-IpVoybr2gCu17QvyOTwzZuwD9W5-dMNrG0Qnl-Zq3ehMu3hbt5LRZB5_Wc24GRrlhyclsoq73TSmzl-4qtlfSG67GXltjiQTvECmsUTNLPeg8ujJWqs_H7H6NCYvVmt_mrMF4N6NDiucNKhI8cbsfl7o2T5Ci4B3AN5rEdbI8Eqr5KMnlxYVs2_5vatFH5YNs1cXfJ78bD_YA1GTO0s3ov0S8kIp44iaS8ATuWPeEo_TP5JacIHuT_042-6HCFQRw2LbeXt1YqoJKLitKdrAH1PcIPBSHkMw9h4GFPkKZlzI9CSJLGayfyiE-IxVrBzW2ZlwqDdHl05Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد اسفناک تیم قلعه‌نویی مقابل 50 تیم برتر رنکینگ بندی فیفا؛ هفت مسابقه و تنها یک پیروزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30718" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#آپدیت
اپلیکیشن بدون فیلتر(WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
✅
سالها فعالیت در رده بین‌المللی
✨
ویپاری
🎁
نسل مدرن شرطبندی
😮‍💨
پاداش‌
100درصدی
اولین واریز</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30717" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm8dIDzJfRIZbggKzAy8Lh0bGbTSu3Yv-3nXLU3zlFBayix5cHWWDoRq1cJUhX76bUUoVuSC7BrkEYuZLL7dtdXIkUifcqEp4GYLJW1uuW5vJCSlfb2-fhmCxLT0lYwrSUamVzu1YSQcaT8BOU1D9naDW7MiKAtIVPe5qvG9cP89-VT9aj3e4nUvr238UO7eXaz58NYGWVwkkyTQQfAzLlrlbKj9s1LtJzvuX6hMY6GOTYjmr4t1KicYw8SyumXURBy23cpeBvK0TBdIgMjeOtdhUJ1JVseEfNCkLvfNkxZkF4TDFsMTyCyFR3AJQVtJM44IR3opfF4as7dGStYNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
میدونی چرا حرفه‌ای ها سایت ویپاری رو برای پیش بینی انتخاب میکنن؟!
🎁
┅━━━━━━━━━━━
✅
4بونس روی چهار واریز اولت(به ترتیب ۱۰۰٪ ۱۰۰٪ ۷۵٪ و ۵۰٪) هیچ سایتی همچین بونسی بهتون نمیده
🍷
برداشت زیر 2 دقیقه بدون احراز هویت
😃
درگاه شارژ ریالی پیک پی
⚡
تا 25% کش بک هفتگی
⚡
هر شنبه 100% پاداش واریز
⚡
هر دوشنبه 50% بونس واریز
⚡
باز پرداخت 100% شرط های اکسپرس
✔️
بونس 1500یورو + 150 اسپین رایگان کازینو
🔵
لینک ورود به سایت(با وی-پی-ان)
🔽
🌐
www.wepari.com
🌐
www.wepari.com</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30716" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmO2gfxFktnFzUEwwvZfEpB347iyo4iTTQnvTHfg4I0oGhbnsP7aElTN5gRuLU54hvVDFyuAfmN2TuW5j3VB4I_ryWE8l6YAMYq-lmasgdiN3a_GVBNIvdzaZstQ7BlplfJcGgAhqdSwcLdQnI4jijMWT_E0wjFjYtydublDPRDKTNJcAJF8-wSS_ppvF4BO9kTc4JRiwtZcIrdfxZRF7okEJdiu455ngZvOLgQ6qXsYvA4rK8PWqI4VfrrjXY4ARneMhAJ6wivYtmMnLw8XwojRoTwvYYHio1_CLe-Zhy-ug65JqBkxApzUOC9AWH2ih95yyUVSOmb99smCG1USaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30715" target="_blank">📅 10:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6-1LbbM4LDMu0YhzH9q_6jzHar6-bNa0ohbALyBQCFA-sqmZjw7Gdfs17jFYUR7WXqyv8c2Fh7X6zm8cJ2LXmJa6WIdfldI2qv40T-Zj4UF5a0HC4YXltEJfv8a14Ce8Io3ixLUzQCbhjjBeVdWIeiP91ubBVJfgjkDQsyNqgwuVHNg1Ru-UvGf0-dtXsW3SEeAMGx2Rkvh9QQPLJqGa8GGxgSQQg8BP-hekIV9D-vQs7AZ-6xhD0lEAyS45K4IDqvCsQgMQoZkaVfuN6p8g3lSiupoLy28Z6H9fvaGdBMxHlEmhRRihPUpKJ8YrUsyKTfUlMozLx8lJulFYHFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30714" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=vQTlp2BlI83Otd2Rmvhrvwrtonj-6toNnqZt_MQ0YhHdNBWj-BOsY0ZtkSDD_wC5XlwV3mxft_XmZ21dCwOSikViQMFpZzp2wGoLZ6-PUIzopA0bmMCjfpBD5OyESjCyOjhSAMM5XxzgrBm-cASwGMiezCOmPfr1sbEe1FoANTUtv7Ia7ibtcpvGylE9OSttanFcXFesNXN4GwxoosBGrxRFQLECsIb_nS0hmSlzyAzLySwR0Q8UDupYCfJ00vhvFiHGmr15SBUatbG8EWCFt-qu-9C9VpmzAf80CVmk3Hk4KtxBgluld0neSvAolAr-qGzyXKK7Cr2wOAuOmL-xWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=vQTlp2BlI83Otd2Rmvhrvwrtonj-6toNnqZt_MQ0YhHdNBWj-BOsY0ZtkSDD_wC5XlwV3mxft_XmZ21dCwOSikViQMFpZzp2wGoLZ6-PUIzopA0bmMCjfpBD5OyESjCyOjhSAMM5XxzgrBm-cASwGMiezCOmPfr1sbEe1FoANTUtv7Ia7ibtcpvGylE9OSttanFcXFesNXN4GwxoosBGrxRFQLECsIb_nS0hmSlzyAzLySwR0Q8UDupYCfJ00vhvFiHGmr15SBUatbG8EWCFt-qu-9C9VpmzAf80CVmk3Hk4KtxBgluld0neSvAolAr-qGzyXKK7Cr2wOAuOmL-xWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟! دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30713" target="_blank">📅 09:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=B_nTl5JbUdD84BIgUtZDg3SK0mSk6jqshFq53I90lV_mlWA-vpUaeKpdd25-X5UHK0GUqnNftBySPApXEWWgHTL24laEqwCCgcccRjBvY9zGC8br1SKkRA9E5TSWyiXImsq5lEkqppoImpXaEV4s9ousfuYNbiKkMJVfO-5D7BnzTC5XDgeIdnYtSe6b8FBekNABEQxSYlmEFo3AYwNKXhmDli1TaFGLpMn5rOTcK7cor8sPwnzinH--2lSDAFSibvNrNNq4fQqHJB1OMAUAE2bMfxTYJrZoxixsL16o9ygia7WRuLwaNBBwXvRtcPlAPFG4KjKGpxNp1E2auf3TLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=B_nTl5JbUdD84BIgUtZDg3SK0mSk6jqshFq53I90lV_mlWA-vpUaeKpdd25-X5UHK0GUqnNftBySPApXEWWgHTL24laEqwCCgcccRjBvY9zGC8br1SKkRA9E5TSWyiXImsq5lEkqppoImpXaEV4s9ousfuYNbiKkMJVfO-5D7BnzTC5XDgeIdnYtSe6b8FBekNABEQxSYlmEFo3AYwNKXhmDli1TaFGLpMn5rOTcK7cor8sPwnzinH--2lSDAFSibvNrNNq4fQqHJB1OMAUAE2bMfxTYJrZoxixsL16o9ygia7WRuLwaNBBwXvRtcPlAPFG4KjKGpxNp1E2auf3TLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟!
دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30712" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lglgnfo8_-hTHwSyCQDKHkB9evZ0j619-pRXetTyGE7EwGpxuFU8X4xtB9KDmHBUA1Hw-CqM20gSIp-1fuMv-5qNoEtaN70G09IO6xo5ozyvJi4sX7MB8L8GqpHQBRT9f0fYdXtQvXBvcmrDzUxatmpjjDAKiyyFxhLGy7QDShsJPuTbNZiaMC3qd2G4jol-yv0WEsMWbhrH1-UMw0V8srqsoLpkz4R-nxRXmELB-CQq7202jJT5LexLiZWvVszkWgjbBQEqX9DHpY_6rWTD3IVjFTz6T5Uo2q3-98MDNUGYyfEcquTf0lMEhV3H1Pc5ayUJrDKpZ0k0VfuWS7TNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKGn3i9f_KFRjmXF61vnaTErYGW3LuhGXiZ16EDxqpxlAH7_9o6p176s2DNxL-GmWd2fQs9c2YYgo29OW9tMzFut_yEWS7rJxDv_NvZd8UrF8GHKP3BZETcCbirs1PH1sA0YiinxxjQbhIvwcS1K4B-PSw_eCvcsIjomONOZVxpGB8Kh3qtcpzYsF2m9XNHUWuKOSETDBa0J73pIYXyakCeiYr3p0QomlwbI5MwM4sBswEDg8UU3lullXqzyGFVSwMt0wdVnOu6mS98OFDyVgd4VpllxBm3LlZsfIVxrRGrqBaLVEPJ-Xymak_O-0r4eHFiM73KJRKetjdccezutGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQWbVcw409vi13kcGwujr1B0AClYrElikQ0UtmaSzvUNkML2L1CZp9q18jsxOdq4g3p9xwD0ZQq2idXHKlpV-iefVop8lBLULeD50lhswu4y-ziRGx_NgB3xNovoa5xVWISlU27_NHlXbBnYtU11SHZ8lLDCEQHrfYNOn3zV1DJZaG7HpnjZ9HrLcd3VKFlIuDMfjx0dUK1DzRjLz2h9mGDSWbsPhbfX-IJETDNrdA6cU1J41_bDwFDU_UHCOqVpHBcpCIbNFWr_Ctdpd7f6H1wih68efzruLhMSBd3QqaFOO3KeubXW0oLKpP5mhtQyeV65zXR4n2tNUUH6mzuXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppI6OlcmKNYfvm5w4Qfn4Plg23MTDRNmUkXz2Afp7beDOKDQ6GK7SqZQO3-kFBMTqPigsC66c0ECcZWaFKPTRZO_Vp7Ug9r6BNxphT_4CelU5zNFxy-qCDbKpW7Ye-fPKeozBozht7TRgeczM7omclZvthoMQQ8x8qFXGx8udSRnm16OfLELbphMGA8tAVPE7iLIDJlpkyFIdrpLrSOTke_c-5vDCZlADQebILbDUcLVih7Io_0Fwypftupt0hD78AhAulxlSjwl5eYPqNbCB4wdt1CeOAIoLW4lqzcy50PpTcUSfrYHGVsZEB8pwNUKv-GpMllP63rOrjwi6g3SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxfjbH88JbhM7A_lArnxwM0dlkmGfZq-DdaDdxRYQKEMrtP6X13QFAfT_LhFrYaq48a88hRFlGOm7Z7z88cBEziMeJVa9nu1md_yd5BV3t2j5syDXyOL_fUD8pdAb0qD7LSwZgzANl8VBuz5IaFtVJ1Az3Z_g5jyji7JGzEZn3ndmILsf9nWLGq9D3V2PLbJv4-irZghVKZEihngEtWhJLO5BoVuvskCWNZfB7c_0JXhenDy8kpqQLBDYF2XG4lGttkfecOz5x56GkxApo0YnluF05mP3cnhjl8JNHrsU8UFjirrdvk_x1MCicuky3ZdQxXZOnq-PPgL-SO7NDLpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30704">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxZn4bM1Hwc3klhj4m-fSaFh2zUcI3mL8msS_wS4KGCv0D0zJ-yWarnxbacM_HmypnhA_rqRA5h-wYGib6e8NgPqny31l5s90Qj1KyM5-jTY_J6OmSRXW4eQ41jRVNHI-p9gp9GuKML0-ShwVB4jfdB1y1a8CeVw3bB_wEUl7BTpa_2OHJc9sZfg5WwCcIPhznB0OWpNwIkve6W6xvRE2n4kRY5XI_vq1WtUYojvYnEqBwFAYBjT1LFReprlmQGUUJ5_csGZbrKpiGMvMtNzyvZ8b69CNC7bn4PwVauer3I-6ibtAbGLyMK0BxGrDWl94RKHK9kgjHmFfRfkGEeS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ طبق شنیده‌ها؛ فرهاد مجیدی اگه اوکی رو به فدراسیون بده حتی ممکنه در جام ملت های آسیا رو نیمکت تیم ملی باشه چون تاج بشدت دنبال اینه اون رو بیاره سرمربی تیم ملی بکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30704" target="_blank">📅 00:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های اروپا؛ پیروزی ارزشمند سه شیرها مقابل جمهوری چک و آتش بازی تماشایی شاگردان دلافوئینته مقابل یاران لوکا مودریچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30703" target="_blank">📅 00:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30702">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reMhfRjhqSMrxyVkIKuzNiD2WBKCs7Z37s2co0NDtx0yfAgqD41krEMcnt2R88TwZ6_AI7iQxxyB2oqT60xvV-OD9Pm9eGH9t5Ic39hoMilIk02aPwipZWtF4r0RUJuH5I7RY9EBol4tLiSkHJPyTi0rRdGCk6HrIlMaUX6-0xAk65-4uiO7dhcyD3knoQNenPucA3jKbb1uJyFKXKwmE5X12Z4gadn3fYUXaOYzi4Eq-ZfyaKVbObfG792wievC5tjoEWHvs2D9FkdhfIkqAY93Zf3Ma9z2o8KfbxLauiu7-YemayRBuUnyfQwAKlZ_EgYZX_GPSqEOzVOtQC-GnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30702" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30701">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c014a889.mp4?token=M5mkx-C_8LkOW2WCMsc8ykJh9tFn7OBPK1Hqd6LWpMBfr93q_7dJxXtShaYRPOhSaRfInBGpzghC6VvDc_5ZRrNnjHGdRU_RCQW6STdDoKNYtVKutR6_5eBqNBy0ItbaY2Z2XaDftcyp34ruYeAP_evoW3PgH8D12FYIkF5H5PeSMFJtsvBhNL3za00a1oKWBdUAtmKu3hCmCKzKY0udH87uLzyqlPO19g55NV0u6APuuzgeV39IzTYRoY_tciIlnFSArUPS3GijYIj3zWExOjl7Fzbo6i-TdTNivweV3OfE-7FJMRD9F-sI7ihWPZLCa5pWrew7Ozc4TZ-7NY81JCc6WdqY0SU1AEjR3gAAr5WrRViEGYQ4Na9wyhUbODSeOucWEpNI0V_GPdcdZu15QeaXtKV4iWytQYyv3aqYs8TW8T3S8JiiTQagcIFPLP42-cixPbH1Obvq-AwWnP6Rs017g-bGt5qSGgP7VMCGPAVaHMLXQ3UKvCWxFGm-AKmKEm0zCcTdeXEyZmVIz-uxc9p1DOzuAulEV86TJQKjByk4LezCNHKpU_CVbX4wZXQJyHgvNT4t1_uH30AJCLKB5m2msJ7Qtm7zhFl490jUUmVsdkdBZbW5tS7GgMTTHtOArjuNRYeCHu5VCPv1ASoRxBv40St2g_oqI76DnqOw7MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c014a889.mp4?token=M5mkx-C_8LkOW2WCMsc8ykJh9tFn7OBPK1Hqd6LWpMBfr93q_7dJxXtShaYRPOhSaRfInBGpzghC6VvDc_5ZRrNnjHGdRU_RCQW6STdDoKNYtVKutR6_5eBqNBy0ItbaY2Z2XaDftcyp34ruYeAP_evoW3PgH8D12FYIkF5H5PeSMFJtsvBhNL3za00a1oKWBdUAtmKu3hCmCKzKY0udH87uLzyqlPO19g55NV0u6APuuzgeV39IzTYRoY_tciIlnFSArUPS3GijYIj3zWExOjl7Fzbo6i-TdTNivweV3OfE-7FJMRD9F-sI7ihWPZLCa5pWrew7Ozc4TZ-7NY81JCc6WdqY0SU1AEjR3gAAr5WrRViEGYQ4Na9wyhUbODSeOucWEpNI0V_GPdcdZu15QeaXtKV4iWytQYyv3aqYs8TW8T3S8JiiTQagcIFPLP42-cixPbH1Obvq-AwWnP6Rs017g-bGt5qSGgP7VMCGPAVaHMLXQ3UKvCWxFGm-AKmKEm0zCcTdeXEyZmVIz-uxc9p1DOzuAulEV86TJQKjByk4LezCNHKpU_CVbX4wZXQJyHgvNT4t1_uH30AJCLKB5m2msJ7Qtm7zhFl490jUUmVsdkdBZbW5tS7GgMTTHtOArjuNRYeCHu5VCPv1ASoRxBv40St2g_oqI76DnqOw7MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد سه دروازه‌بان تیم ملی ایران در فیفادی مهر ماه؛ دو بازی، پنج گل خورده، صفر کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30701" target="_blank">📅 00:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30700">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icX6P6QngZM5_rr6IIeO2i10uTnUKBGGNJ8ikHfSUVacEnfq8ArAkM-RRZrP2eubIecKG_UACjSMa_8TcUIbXFMbueWTjCz379vDz5yN7UJObjSdJsRFYFW9CER-nsF4nfaG8Davo8XT4GuuzvXJK5pSaEC7joog-Qv7CBsY4Asywy9viNuNvxwmj2d6lrv3Njx-1jVyJvthvni10S1WSSyfwK1PIfLPiH8TMVxPu_UoW-rSU97v3s1-lE6jsAr2hJByPHtE0eDUSAAOyPksiPwHFSDcohy8EH80xfS2hWeA4f3Xa33iJiyS3VBF2JmP4f6sYgDfSrXba9oOhhvHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30700" target="_blank">📅 23:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO6gtMoNtVqcX1uy9QA9xupYJvi0i9SxFz8BrXY4HPBw3txdAfzqPosERpbQewmA9O7OxeqYLa6MeH_T70gXwJW430MEQ96UKqed7hXwdtWxsyTYYQSrxbCDQmDy4I5xmk16AFH28VVbDHLDQOnaBAH4WWsE8JoxZg5bMCWYMAfq6L_VUK5HbcpLbOYuSA4NcOOrvJOd6EyYxfwa9IXAC8e85wWh7bQtDARE7l4KjuW4MhZvh18Caxa6iPDa3ynMjs5n9pN6qEjetFbtBavaWXMuyqNak8S63-ESbhursqEFv-CVi_oR9O8aXNmYJHvtslmFce5AT76iHaF1B_JcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=omhRF7IRKKlUssG4hO_84NKJkEzXhPg-4HTYzDFrZDkHOtlNA2GqapYZOBqofuGvh2WHytAblU8zZstj3veQLJ21UUanlmzqZJShuFgWJ-YQJCWPeq8IMGc8nUUfPNeiyegDuRJsho6Pd04ZaSBA5CgsOOLGCD5DFYZClKPLqAt2eKSyqUSU0XPajVyOnT0WOwRCu2xnyAKV31nGHTDtMddkbO10bvX8qKZ_H0r65Ea7pMU5ly7YCZe-x_YGK7homlNw_ANyZwXackUC8j4e2pvhd8pLUlXSRficqJlW9dzYr64Hxw452O2W1uV9McvFmsOYmUKk5ZwYIlwLwI07ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=omhRF7IRKKlUssG4hO_84NKJkEzXhPg-4HTYzDFrZDkHOtlNA2GqapYZOBqofuGvh2WHytAblU8zZstj3veQLJ21UUanlmzqZJShuFgWJ-YQJCWPeq8IMGc8nUUfPNeiyegDuRJsho6Pd04ZaSBA5CgsOOLGCD5DFYZClKPLqAt2eKSyqUSU0XPajVyOnT0WOwRCu2xnyAKV31nGHTDtMddkbO10bvX8qKZ_H0r65Ea7pMU5ly7YCZe-x_YGK7homlNw_ANyZwXackUC8j4e2pvhd8pLUlXSRficqJlW9dzYr64Hxw452O2W1uV9McvFmsOYmUKk5ZwYIlwLwI07ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkaw6qoxMxmM-NPlhqEjwhH7CQoZs_XvMGbHgHCQejdMNF3fbbDaAU93_LT7ha0KLVIQnlfO0VAisgLobzbQdP8ac91vVPuX_i4JWdIkdnjMb-lUMjUPzNhkV_xShImbpD-Nk4gs0Q9tLJ2Z4atGgSFnd83gRbOUEiDkh7yXCXxFRbI3PKdD3b6pEOiT3p3tjs0udo5I_Fq8pG9nfAYDX3JNnGVNtVc5PCYxCBZxG-ndk9MM1rKPNIt3LDlP88EvPdlZMqs0y4N_Ty9R76Jl04GkXK032rnb8w4SnmJSdOzSaaxADvPVXoTyhwQWm-jUYj0mco6D_5ngwCI5z8rn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1wOHWvonxVeoXAYK5xNMTbJi6SszCvj4HnCoF9rJcFPgcc13-BZ0zahobeQrJ6Anc4Ed-YoBB81U6RLJ37FUJNq41HQaFN7j0SZiI5fE-jaV3kE3704BaWLkmmGCOKi875gc4RFFH_qHGtVbqTsMFkuVhFZ_s_GhZ-EzCrehg9h-urLG-FQSsYksAs_gA9JP9UQHwyTJZ-Tp36oaP7TP4VO042wUOZZwk7OEyt_92hVaJxN8Uiocg2Bb0iZak1w_HWxXqaBkysDrq8qo1B7DnVjsU_L34kJCubTRoYSiS7rCgbHHCl76AyOAD2NpF23g9KZ9Ow-78DHI9j8iRwujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1qxIaW7RaCaxJpSIgwVqVYd9b1xzD76y2P4quHmSnOg6VNl0dKHgJOg6DbAzmF8JDyoZ0XUwOpW84LTnOUC41AaiAbK_-BDZ73cwmU5SUBIpf4SA7cgdtW3kwdgbj0xiwbSMGkl1IwTXrs8tBTyzAr0CrKU-0HN8xfplRIU2T4C-0NM0gJHOd8LdvsIXJPOwk_DU810mgFAkGGV4ERdbfSItvSj_Ry7BzIJdO6MfuG1YPq_AMwQu-hwGsC2iyZGO6enOJ30G7tXSrbgOlbxWToiYEJPusnfrNSHkfmAiq2zxCY1RPY3wrLTT18wLhB9zuev3InEEnOKKkaP-w-GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=C01c74nHpmmcAFP2ncsnp2OW7_ukeZfBg5kNeNfPvUgYImFe4x0wl5jyCnCuHA-DhJJL4R_JdYDzlwI3Dcmigo99N1ZRLhSusZgqOp1yaCH1eL8gz9yxWTl3uS8wnEXzwBJ05PldsSkkCSMNyowKiUSsKlcvtPhjuZ0qh5BzATGfEMo5kph-eO10T5SDN4TlD2oaSp-2zEU_pIUbdE7aJuw-3BoRTNXRMrxbx-aHwW8vXJq8YL7_TpayvbRAFWfs4Ir-urLo8Pi71vqMKY-r4h6zLLq7uS0x7Ybzsf7Bd5Xctj_qpgDRtvJ2-W7W2PthOoPrR-PiCgoVQkq6sxCntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=C01c74nHpmmcAFP2ncsnp2OW7_ukeZfBg5kNeNfPvUgYImFe4x0wl5jyCnCuHA-DhJJL4R_JdYDzlwI3Dcmigo99N1ZRLhSusZgqOp1yaCH1eL8gz9yxWTl3uS8wnEXzwBJ05PldsSkkCSMNyowKiUSsKlcvtPhjuZ0qh5BzATGfEMo5kph-eO10T5SDN4TlD2oaSp-2zEU_pIUbdE7aJuw-3BoRTNXRMrxbx-aHwW8vXJq8YL7_TpayvbRAFWfs4Ir-urLo8Pi71vqMKY-r4h6zLLq7uS0x7Ybzsf7Bd5Xctj_qpgDRtvJ2-W7W2PthOoPrR-PiCgoVQkq6sxCntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maXWAWkbbskJOiDqWRjFlFe2z8Vs4Q-VRzQlzn2blD7_ja1DhgPij2S2Hn5N_elY9VlzxNl4WyyfB6kiAIZuZmHyJcEEAf-hhAYUySIg-IiQ-7Y6UH41LHxV9w-YVx6ggCK7T4Zywmq3HGNTx0UaTf4wES7cm2-vBdqcQw2bZRsx5rEX7gn5gUYGi6nmcddcGGiKavbKz1BmdsWI5mkTd-0DlWiZbvKwGynT_7eCGmsHAZppjl3b7SCt6DrKxR6uh5O4dF_aGfeAfbyro2ggsE0iMQhoPa_UBz1D9ugEESw9qigQqtcczOvul66xDX2bT0MWf4hqGnuD25e8hlMnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovfxlrduqseaCe_P2qPO3YZdsCJH0kH-pzDwhrgTVF9Z0bDF5cl5CvzcxIq2SXXzK7LGFHCGyh7rAmadnN80zruqFROF6ONoSVd4g0BkkoekFxwa60u7aGQ7_CYCaxHQnMtG6Mc5XHDSmimmlZRiabjufFDwv_D-vQyylPPZgEbTqrHFM5z5IFD1Kewdf9lh5CTtVSYmZU84PL9F5ej7oVk10yq-QRT48uJ_4-AyFygmLoyXqRYFpROp_L6v0GEpwuuMO8MqVMS9KqTe9DzBRzoqYbBr9WLFNuMmVqcemejT1Egc2yR62NgXdhDRX2NYzIx-jJRyoL3HbB8aurOwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=rwUWUVNcC-Sxj-8LzuWhAv-AH7FpRlKYktpiY1wffmy4_UqZzAuwSYknhg5CLyGar7mbZtZ1PKxFZO6prg6dxjKTpz3olaUfppNjSV25HfCTRfjxLtBu-JG-WxhvTa1xL7pL7bOz_a66YkafgjKKhz2Grt9ri85M0ADjCD0X_uc43vIWprUDNPIZnz9gJKS0kyEwPa43Rk3p2YE6Vqwl8unzoP-dNPDzryOageGl4RvPWbwFDe3RY1VpjEPQnBVuHIWBNNKmIxqwbWaNOuSEViDo2vr5O2eloBoh86vq7TMcqPt8PwzCvTgJhzPnBb5-CavaALoFI-8WwUxBpYO15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=rwUWUVNcC-Sxj-8LzuWhAv-AH7FpRlKYktpiY1wffmy4_UqZzAuwSYknhg5CLyGar7mbZtZ1PKxFZO6prg6dxjKTpz3olaUfppNjSV25HfCTRfjxLtBu-JG-WxhvTa1xL7pL7bOz_a66YkafgjKKhz2Grt9ri85M0ADjCD0X_uc43vIWprUDNPIZnz9gJKS0kyEwPa43Rk3p2YE6Vqwl8unzoP-dNPDzryOageGl4RvPWbwFDe3RY1VpjEPQnBVuHIWBNNKmIxqwbWaNOuSEViDo2vr5O2eloBoh86vq7TMcqPt8PwzCvTgJhzPnBb5-CavaALoFI-8WwUxBpYO15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMIkU1nK0NTA3fl6IquGetJBmx2JNnWEywuw3sstg07JVYAIKdjr_QR0FdjkZcQgl7r_TYvJZezPVG4BG8ijZuXevkkHVs3CXUwgZPPL_f6Gz-18A_DmX6-rAFlx2nW44PlaVmvcmsOKNlpbWEJ05SnvTY_h7Gdq8xrpgjpomyqjmTmeYq47GwhNDGWHlH3PpGR7X2mqoA4jB_-cE6P6sJrwDHkn-iuXnxrvyIGkItB62HLt6Si4Gh12CE5osWTFG93LPtkwN5TU0_QEi6sZWyujTN7aDDz6gSq66ibz961pVc9bIqfwZHMAiD3RGNDHUrDCVofiEqHjFVkJF8et1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUbPXsgYW-UFidT4O_E59vlGtn_r-UVGrz_h6l3Lz3UGUhHC92W5JhAwnogHQhxwKiSYUjWfk0NYvvaoSjk2rF8SkiF8gdwNcSsS1v_Dc5R6ftfPvIrVhOeFb2dN8q8aJ3-AMx51GBiF4JgMN0Z6_sUxjmIgbd7HADrSjMGPgGZQ17yg3U-GNSlXVE8d_-Qdp7q6xfmnk0Ww7LIgBqCxmHouVYRfz9e0pR2ygxXHO3-SZXAZX8qbYpgf1uzWf7LQrOqgL6UTCrV6Ifkxj4y2I4xxu10GJqV8LygzUyAq3R9XJLtejvi79UKqcjDTFWLyU1kXNMWgzIqnl3F4FeOLRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=qznNiatVvBS02sgJRNyD9RxYUIlkmdB86s3HifVAP29bwjEnk-R0BSzgcTCTweEGOp7Sf28vAgOIp6Ipuj89a7OS2PgpQc8Dzj7gmvQ_syzf5Jt3JWoW8514wAUD79XttlLtzoxrt1WrLdB9cVZV4sZ7Y3C90wwFflVzplyaUC6-t5J0bpcjGNmVa1mKSm_CpIBmd0Gn10iKBWOf068b-hxq2IeBkWzY5bMjYCvrdtRO46Pc12XPsT4j0351WOHjY5ht2kN-7hhscZfth9GLUTkP8ZShfIzkJW7Bd3Qk9AGAd1odFe1_SJatUQwhKsYrNt71qDwpYbqfeUT5d7qxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=qznNiatVvBS02sgJRNyD9RxYUIlkmdB86s3HifVAP29bwjEnk-R0BSzgcTCTweEGOp7Sf28vAgOIp6Ipuj89a7OS2PgpQc8Dzj7gmvQ_syzf5Jt3JWoW8514wAUD79XttlLtzoxrt1WrLdB9cVZV4sZ7Y3C90wwFflVzplyaUC6-t5J0bpcjGNmVa1mKSm_CpIBmd0Gn10iKBWOf068b-hxq2IeBkWzY5bMjYCvrdtRO46Pc12XPsT4j0351WOHjY5ht2kN-7hhscZfth9GLUTkP8ZShfIzkJW7Bd3Qk9AGAd1odFe1_SJatUQwhKsYrNt71qDwpYbqfeUT5d7qxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=O1D7PJZbw8WJPEYXLeoTFvQS4jFJ68uU_YVcYRNQCh5BEo6h5NSLx0bcSynYrdXzskw0EuJk-CoWMsoEsElumss3xz4APOimO8YZiSys5iCEkxsl6IlzXh0hYZO49ivqlUcj4AVBx6xc_6rd2v4Z_WS6vlK9MvVDaX0AQVrchQ-rmc5O1J6bwNR4IZmRl0TyjmlTKHoGG_MZ2II-6EI8ZXp0CJ6xJHpaaqnDHOC9E3o4FBzhQX5Mw5l-FZ4PZmaf8l9tM53c2xJPYeZFkJXlsCKaOUZLaqSNDZAXq485GENWoSutfKF9LpaLRQfRa8Rm9BaJOcvmwFLuID0sdzCBAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=O1D7PJZbw8WJPEYXLeoTFvQS4jFJ68uU_YVcYRNQCh5BEo6h5NSLx0bcSynYrdXzskw0EuJk-CoWMsoEsElumss3xz4APOimO8YZiSys5iCEkxsl6IlzXh0hYZO49ivqlUcj4AVBx6xc_6rd2v4Z_WS6vlK9MvVDaX0AQVrchQ-rmc5O1J6bwNR4IZmRl0TyjmlTKHoGG_MZ2II-6EI8ZXp0CJ6xJHpaaqnDHOC9E3o4FBzhQX5Mw5l-FZ4PZmaf8l9tM53c2xJPYeZFkJXlsCKaOUZLaqSNDZAXq485GENWoSutfKF9LpaLRQfRa8Rm9BaJOcvmwFLuID0sdzCBAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZzfbiLJ3a0tTdAkyAapm6-vQ1erVtnspaOM736ICDeOQ1yY3OlD_rmohPX2yOyvVjN-WrRV1UuLpMu9goUJLlaUW6vnshZZYh-rgLnrILu0WdXA_503gCgQnM_gb6rE34yKR5TaveQV5-eUCzTw8SK1BxAc7E39J1IegHav04om6PQtavv_b_u0zRhmRoLGodruRdey5AtIxMACSG7w4kVZCB0no3Ffe1jAtwMoXR6R1lPxU37CpP5Sg0TmOnJQ1KUdE8En9A-E53bnZfNZLZsx4drenkHyBRkjPkAKjihwxFCI9NA8dCM3xV5B9KOwGeQOWRTzrwv-O-cjzZWwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30685" target="_blank">📅 19:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAgrXR9dJjWOSonDea9Qhs8xE54Vhf_MkHxuNV9-F79UGtzYqo1KChtjRMgHHirEDLiTtEtH8FYdjP-WClSms5Lrwh3TUBAZ-pUhQxO2vEcN7jJVX0yLQaSxqpLwcu43QtGB8b_pc56jaQsNpk0kd71T8sa1tnzJt27VmkR0t1-0Al_blCJSSOEe0jg_-54B6MQ-4IOxr_usBrL08sdGLpoqxNWps_X1-8x1pYTc_P3zUlRTboSraIz8s9tjK7A8i3G0dGm-LgT1IS19PoHhbkd20QEHIZ1Hqtir-tOBtfj2YO8GNp-55lroqG1M4TcL_OFjXOWrT4PIoKW4fVZPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30684" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLQq3KaSlKPB8A_G0SuIR0FQPUEw4c3oqWe7IcSum8518EdHmNpZ44xcigVxknyBN8FAqhoyP9YTNshc6NT9p_XkN0omDGwj5xcuDlicSvAGDKdHsJI-Yy5JHTNy0agmmUiXeuq8mIvdFPKa7EBnqLB8VkY8gmmzFY2Z_JCHtY6zP27Z5bE9ljNFBcq8Xm1RYtXJb8KJRf2SjLlMkCe3YS8YEiNjdZ_WRy75_0geoZEZJ_LS30z3rIWb9fzpOs58kr8UBZR8adjkMq40ucBxrjn-wNrjVg-KZIh7PnKZNjNqqdirgSBJYJ3VAdRNw_-DgywekWk6beEVaHdKCABxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30683" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY-RjNOrOtxBYsrgShKAj4Y_15elcm62ykqbgMGTAME0msAhjNMN88IALqRt7yXTkYkDkUjIUkgISSo13Zl2NJFejOHAxqXnBiFjDIqy-shXxwQYz5G3TvN5IN9cxrDlGhzsIVhNUlqQiW4N9WTSaWd6dgtWEPxyODb-SVC9zrZeTrtR9Hg-YTC_f1djV1xJ37VOPxukObbQZAOYkjiEyQWMomcuXC_hoonQwqYDy-vkgxCeZx5wvCBh8eZVqgZUzZh7sPvoE8ciip-IJOy0Fs9gP5FB6Xhr6is1mdFyiJ8vnCtK1ADbOfUFtuYbawr7dD_FQ5NOOhJnGeKeGob32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30682" target="_blank">📅 18:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlhAQiBvR_MObU64WpYLZxnnmwKvnnkdzyAmCccuZYqEp3Ddh79iRcLRwOfcxCn5kNkEk41ewh13-hdcgIKdO81Mm-OHMyEMkQR5wJbqoLDuHe4lYQo1b733jlxDn7u26t39H-opI20t549KoRsttAS82rO4Zn4zep0IONyIdmk2Tr9f6j_-VI8Bfq4I2anNPzBAUSW3ZkMQuIKuPHVK7w2L9Klx5KfrwiypF9b4kNosXm_D2bhxdta1eDdzR81JBSJdGAipNyQ2L_R43iqG0dvbW35nKDXBtrccR160NH1Q0Q91MKZ0GEmy1dNNM9KvEN4ET8BDkr_MiHKzqjHoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9rW7kf2acTP-4k3bRt6pP9nrk_URu-BoqmIafgKfPRAJkuXzcCEF4Wlc_Dh9XMm6ZPxqis8JZEz_N4QOFlHHk80jri80D6V6QZkZva6eCl6FkBXewnoqLd92FsJqXTI0jhwAY_3YRO6ScrCO-FLwL84v0vnI2UyTyyp6i46wanM9NqNh5xWIgClANTDhcuwleu9ojgpRbPBfhspy9BlwIRYAokiNQlzbadnTQPlXdRElMTFirhNn6IfzRBPrgHqMoOF2-CoaQF9KvrEPt5GqrHAP0BHhySLo9K4qKpAIL1nQ8uiFR6ufrSqYdn3gXkmfzwy6xRzk53ZNqTyq7W6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kr1XdanILhmaO5fHElfiScQr4BIW7nAgw3j_ygQDx5wAWZbiQTzDqPpQZ5PD_nPL24x4c60w2cpcDQ5-7047fM6OfSX_HKTlcXLWgsK-ZFrNCtJM0o3qMVdcDmw1BlCw8pXh7HfX3lRB9qJ1JZzc9qsEab11kFqLfMSmq5V8liLmWED2u6e4v8xSyYSvrR4BC9Qhd7g2Eg8dLXJnQd3on7ro3tH3PnvyfiB3kek5DhyUDeJzRknyl6b7LD2fY1zmu_W0ofgUJV5JmXsJSozYx8XpQry0JYE13Dqk4iuRAmeSSHq5i7Dl6eImiVZFcYebpbIVkMS-wXXKrTSVFjd6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXmJXjOs95krTmNH-MleexqkD4vYfVCR4sGoaicfHQjFHwrpB_zC9d4gSWN6ZvvXVC4qQ_N2_sW9cVlj_MCPYWO8GkOSV8Qt8nouqfk4FRvow7wB-Pq9Du6Oxl5j_Y1Bm0f-Pjw77Te2HrTMoJv9jgh-fYzcAtfLQ02Tqfo8YO93QodZRV4J__mP_ic6HkkValP2prO8_T4mP-UZ2ZamqKCdiFY32N6f1nLxZ4BWVEJRpn6sWmTQUxoqEC95gcR0ps0ob6q92bI2EHHzeqK9m7uHieEyj2F06Xc-H_ByrS_ZCAwShT2H5-IImvYxwcFSOv-J-WYSdo99Kn814irH8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=rJRpg4uQBe5dwecR22ie0_f1w4cHp83yRcBFF8BZOOYr9Eny2ngx4OfTjZw7DZbyIlUbx4zLpwnBmfneKiwWYpim65ctme6VKUUn4tx1dPwG37RylqiHwMMjU7HXlTA3KZmtU5L6IB3cLQYRfgp72TdnbLIKICaX7hyzOk5OLS101zz0C1wML0Q0EqGf1xXXKo_vwCsNG1J0SHXhH0lutaN1TYOUpGOEwdGiyGP4E4oHQ7lEoPmF41GcEj2y9AbcIeSfDVv4yFWD_ept_VBnEVTn1bvqvuZteSB0NWzHeYlYEoS5_Rc7d4wPd3f0FVPQ0bnSryKCA-3ZCz6iUASVbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=rJRpg4uQBe5dwecR22ie0_f1w4cHp83yRcBFF8BZOOYr9Eny2ngx4OfTjZw7DZbyIlUbx4zLpwnBmfneKiwWYpim65ctme6VKUUn4tx1dPwG37RylqiHwMMjU7HXlTA3KZmtU5L6IB3cLQYRfgp72TdnbLIKICaX7hyzOk5OLS101zz0C1wML0Q0EqGf1xXXKo_vwCsNG1J0SHXhH0lutaN1TYOUpGOEwdGiyGP4E4oHQ7lEoPmF41GcEj2y9AbcIeSfDVv4yFWD_ept_VBnEVTn1bvqvuZteSB0NWzHeYlYEoS5_Rc7d4wPd3f0FVPQ0bnSryKCA-3ZCz6iUASVbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابوطالب‌حسینی یه‌تیکه خیلی سنگین به ماجرای حضور خداداد تو مدارس مشهد انداخته و لحظات با مزه‌ای از وقتی که دانش‌آموز کلاس اول اون مدرسه به‌دنیا اومده رو نشون میده! عالی بود از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-WlJgZCkzWFS9Op6zXEEmzZMck5tNpVWc9LOC_ZQr54yz4EXfvVGf3rHc0JrjBwefqTusA1lj7OEOAFyyuboEZtkqDyps2NlU6HmA_tYYceZaxf4VLHMBXgwEKGlkAg8pyTQll5hpAI9PaCQGLkKSV0YBO_bSg9CL00dzgpEk_pi6-ikbmtxaUr9CsWHUnLis0H9jovAkf4EVwCe2vSHdE58fK_zTmBY_mDbF9QZBDDMp_3MhgUvti3wUV-cMxv0eM7Y2ggQm5UrXLEL4eDNlpt0ersNMwLkIshv7bYwl1eurg0e-CdE-i54cGfk9pS8_JUclvQPr-VWid-YrUcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3T21pnEZNCXKxn8RQ7m5POs74eEHaWxOYVlb39dZqRgtjykvEbK2NY0pshiFGosBqkhd0dhX53XyM2qYikHFJAvtHLd8YLwfz8T_yP7IAF38kKg3hm9BeyG45AJKdAhrau_ZlmIp4v4HgrAco5QLX1Kwo227fVRt1qU4OL-JjZYeVsHSEkvsjhs7-p1CB5M6IYfNzZ7goGBwYD3dOH3NgghutKYj-AQPXXB3_SV5bOV1RrTdbpmc6HKqLgjgE_Sg0C_3qhZrxv4ociF_csj6ja1tyJTgGHaiRS2mHY1VJmTN0XtSDWg_d9q_p2An4uFNHEJnzcv0sR6R0Z-f4qjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGIU-SZzJpBALwB37YMd-Qsb5xAaUbsRPsldexFH1zS5lELfXgD8U7Tp5UzBWKmlHeg49-CltXMo7WXZQa-cTzejuNHM451GTLH7PiUiWCSLUoRz0kFz9Gg5oPSQ7rQmDp37eAdGpI4Kt1a0QhEJK_0SsA4-SwkN2jZUGGz8ftijLJzjLDgNuIziO45BueNn3uQiXZmZCV6cNF8YXM3ZvTGEYVdNLwHz_ogBbTI9lmnE-vmexQ5NmgqLb9covfFRYRo5zlqZXvYpIezT4l-X_PIEU_TAjtsWY4rGG1dT935t1vqnlz5kP3Wpi0pujc3XmgjTEynVLIxkVW5baSBw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TErQJw22b1ygSHFbsA6028iVh3g-SKjqWu9oyfx1ymOlr78mLPuA2IMgOeycHoue0Y7MUiDHA0b_-jUkJsszOuyeG1wuKN6DqVLle7NHfFIfxRQQKbX4yEfw4VtLGmPXhseqMIRtdH75N3pQMYird1IHnRwokhw12mAkv-_blCnerj7J_Xg7FYpjyxE495WdD0qpSTOBzKATRIX45y0dB49j9eFa8KaLi2ai2RdiwdHBVlvOLSizfpRENoDJZuzSqVPmzLsMZlJamlFVmYRCGcl9uKu24Fl6T9HUIqZh1O2A1jBbWsvXipkGLD2lQkx3npu0584-FkallV3TRh3sAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXq1n1au3zXYcFa2FK5tlbBjCgx_TIF_pGpjUktG6L8TbZWswVbQn2WcqIWpiX9yx43nP_Jwz-k3Hs3BCAyzuDAxNll1TKfV5F9zh6H-fqVLRhKvjz1KoQ1cnk_ck3zvpv0d5gjBPM1Mf-5DMQ2QWrt2dEmAlRlJE0ma05HIG6ucPnKjVwkm5ifM0WwwpslVWPCH2PdgVsM7QyrcLTQjdJ5nR52xSt_N5roD1OvphpxInbYtueUv1fwCzH9Wqtm6f6LVFRCI226AfIVJk_bfftuM4cdiwUWWlkttt_33VLqy4OW2qero44AfRapvsAeYzJYavNtwch3cHhA-z2QMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30669">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhiQKfMjAmhuyyzffLCHKzCFVGxtiyGRZd2YERnHG78lSe3ag-dNc3jJHxf3h9frybNjfFbTi-7mOyKL8DudbdE5PzSmOKkHjGZYtJQFoltwNz43GkpdjBEfJZFc_JZqjUhDkX31DrRc8JhZY4XxdgU7STKpWLM0gTXsKU3MFbJZARV4REQy-UAU86_QWJWzI9JJU0OVICGoFbCiDqQrTZXrOrcPqVJQTKbAXxTnxXXjo67m5IUNQiYgVE6M2AeWQXsfVH9jEkLXIrFLn8TWulm7tKJYWcKGYveb0BIQ_Oe5jeTs2FkKUFV3ue63xLs8qQqgLRZBNAN21UmWlYq5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
تیم ملی امروز در هفته دوم فیفادی برای دومین مرتبه پیاپی امروز ساعت 13:30 به مصاف تیم ملی استرالیامیره. بازی‌اول بزور مقابل کانگوروها مساوی گرفتند. امروز بااین ترکیب به مصاف استرالیا میرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30669" target="_blank">📅 15:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30668">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DENvUqBgyrs-eMQjGH3lRiaqgN8wZQbagb2oApzS2Url-genNhduoyD12Vq3FePDkDVe_vi5M5J4vS_CrBNHgR6NXGN7ZEyPgEkR462sglZU2tyO1iUyt_arYIT2VIYr0TxRlIu5z63cQZ-TCE-CzU1Ouxa-IVfkOENKOnAmJaZqxvmFjeSwUwIXxgOqTww4b-oJ9_DVDNDZwzuQCSWTnLzxRZ7zZr6DxBtuRCIAbQuLn7RNW4xoWyOkDh60JC5VgOPVkvMAYgI6zRJN9ksgO6BEJlM5QFB3M16IakZ72LiUT6OTm5RsXmESSlIsqQT0I4P30g6EfgQT2JPpy9R0rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30668" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30667">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXsrhErmKwX-IM-sbpkmX2WOMwgUdDn60TmuIfXOXlqUdP9bBwYYeh1Jb1PdUuYDfSQJ0JoYgVyY0tm1HrYZD7WLap6PmiB4KkisRTp8J1kqsvB-xRB-wN4fdOOtsKA-lBn89gwLZ0sGvRqb140JaR7I7XjkJEVsX639jOUD-y7IobPV38bjsG41RQwhnI1nOYyihXMi-1knukCPQc1FScuODPzGfrerEoiAokhpK1cT5qKuwgVLZneK6GZoMr4K7xz2cLRs_EiHS_E8ZNMU9hG_birUXUSUeTrIDlVuzjRe3qmHPhRBIX8RfGe_udSlH08cRYQGuYPJ8b--BqBbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سه خوشحالی‌تاریخی و به یاد ماندنی زین الدین زیدان سرمربی تیم‌ملی فرانسه و سابق رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30667" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30666">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
ویدیوکامل‌ویژه برنامه شب‌گذشته عادل و برسی اتفاقا اخیر فوتبال ایران با حضور یاسر آسانی ستاره استقلال و دانیال اسماعیلی فر و شهریار مغانلو دو ستاره باشگاه تراکتور؛ اینم یجایی سیوش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30666" target="_blank">📅 14:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
ویدیوکامل قسمت‌دوم برنامه فان و بسیار جذاب ابوطالب حسینی؛ عالیه حتما ببینید فقط رفقا یجایی سیوش کنید بعد از 24 ساعت این پست پاک میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30665" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXurEFae7ICpieZQg2rt80ijBuJq0TGM64h3_Htdki9Ooc0LmtQZJxHliiJNg0quv8wQkXQET6-yQy6T-iDYya_b1E-BehXexDctrWqrodQ4Ob9BZcUY2TAjedr8aPkBltJshxQQGCV8wJPDx4xKFIDU0Aj-nUtUEamt8kAjYe2y1n-cpga8Cukuha7l5IPp21gBnW_FclkaH_hH27l2MgZ5mIzJP2xExhU9Z0S2FBZFKiHscDktqg9edFkRN76NzVHH9TFfe6MxGfxy3Seka4wDSTiRj7YyGFo6U-lxZiwLB1or5NdDoJZgqlf-UOFCqDMnfTvDcSsyoSgGCroWzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30664" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=iWK9wRWmw8vTvpP1SKmaggCS0s0Z-14gLeyruBOk3DPlnA-fi96sjmHW3NuSSUmDRxVMGBSUhLoW0qKAuw5dWMzltA191YshljqqmjK-6lOqiZ68ILgztKk4e5RU5iMZlvignRuCqkgTjllKbwp_LMvELhcTW-7umAG4HmrA3JDXEaPXa85hakqckmQZ2A0gBl3c495hM-BEDMNZ8VY6_2j1o2YNoFuEbOPG9lukhoFN8fhg0ZQKXSd0vRVsxJGgdIE5poduNC2DFT6WckVFkmnPZk13gfEsPTwFZW7ZKv1JR4y_oCujU8Vu8SsgMeguJkQ-7p9yRActC3rKzL6H_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=iWK9wRWmw8vTvpP1SKmaggCS0s0Z-14gLeyruBOk3DPlnA-fi96sjmHW3NuSSUmDRxVMGBSUhLoW0qKAuw5dWMzltA191YshljqqmjK-6lOqiZ68ILgztKk4e5RU5iMZlvignRuCqkgTjllKbwp_LMvELhcTW-7umAG4HmrA3JDXEaPXa85hakqckmQZ2A0gBl3c495hM-BEDMNZ8VY6_2j1o2YNoFuEbOPG9lukhoFN8fhg0ZQKXSd0vRVsxJGgdIE5poduNC2DFT6WckVFkmnPZk13gfEsPTwFZW7ZKv1JR4y_oCujU8Vu8SsgMeguJkQ-7p9yRActC3rKzL6H_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30663" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQGZYbrtPSjP7Ln8AZ_CEIS6P3BMHgsMXgO-LNFc-zZLX3CmmUjgaijXSZbsT6R5SmRhSAho_8hXNlwhlC8X-d9c8ZgM1063Q6MxBB9cfijWODlxb1yUQUpheKHB78n76_AqkhVsWE7dc4g42KSXK9dyn-iQTtVW6kboNTZ8DzuGcBEI4v4w1NGyHn6To8SqpJCyOiKUswvKBSUVmLGEXaXu98EpyjrpSPNBB7_uoqGALEJwdkPuWQ97PMowF5bKRJgxXltjO6-iNy6e6IBkfv2G3tFwsKMwMlKmeJD9ecMGsoWmLQsrqJRkRBwX8J0ItpUmw_jR9kGPKHODGensUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30662" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=oeBpaMAk3gaEovftT0nUrDfnIbqlrswJxCjpbF_wnPVAvbMDF1ht79qMxW7ZvnJeHCWUHd-d1qeqASy5ilXooz6z509wMuG8Ju55moT_pv1s5amlTz8yZY0d5criWc8DoLjFFt-SzFPY25ippDi98f9U1m4kl_1VHlN6bRwSmyYKEd9xfC6wbqRIXit0psf6rh7u6rDIkaZZQ-hxZ4nhckKtPGy-MxDhJ0jlNXPXofnFLQ4RsI5OrMHo3RZz_GxfCs3ykQS3rYBuWaarYi97f4Ezo2fE-476RM0Va48Y384aZv5iFdwJzbvInvXZuQLQwFbbRljH_NwBVUrlm6Te3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=oeBpaMAk3gaEovftT0nUrDfnIbqlrswJxCjpbF_wnPVAvbMDF1ht79qMxW7ZvnJeHCWUHd-d1qeqASy5ilXooz6z509wMuG8Ju55moT_pv1s5amlTz8yZY0d5criWc8DoLjFFt-SzFPY25ippDi98f9U1m4kl_1VHlN6bRwSmyYKEd9xfC6wbqRIXit0psf6rh7u6rDIkaZZQ-hxZ4nhckKtPGy-MxDhJ0jlNXPXofnFLQ4RsI5OrMHo3RZz_GxfCs3ykQS3rYBuWaarYi97f4Ezo2fE-476RM0Va48Y384aZv5iFdwJzbvInvXZuQLQwFbbRljH_NwBVUrlm6Te3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارتاکاشته‌از لئو مسی فوق ستاره آرژانتینی اینترمیامی از یک نقطه در کل دوران حرفه ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30661" target="_blank">📅 12:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNNrhfDvnS4xokwqW67q7fjh7K0LlZvSgzCrW4xy4tbWYoe_9JOJzAT8aCXUXrt2SIzm077Iyzw7DWYlsKpe9IkpVJ14p2hE2SEwobKNjWnR8DtKPh2rXhds6C-QmBPdKXxHa0CAo9lgKtCEAOMCZgTMhVlyqpUD5uo2n3_c10tHWRTqUEU8g0wMEv_aVS46msQpNPwObIWDitilQjGet7M4JZWJgHtfbmothlz-HxyCbiu1knlK6zx4HOyxxIdh4eikg-sjWhmOfu5Q-AZ71kWyKw2KoujSE3qyPeJp7rbFszqVbzDWhSLvDwl_pT2BA8S5F-74UHVbCNkqovF6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ8nIamQH-OSFQOxM6slI7p2QvMzZMBps97LL9YWF8toRFSGpS0nxJpS9vYDREu8aSxSxla5SuSWY9Xw6VD8ztkTivaKwXLPBrafNvmwxL5uFOENS--5m6I6dp-lDHub8hZBzfGpOvJ-kkOZjWSl6Hb8vS41cF97TxcEhrYm3lXAmjUchz0SAMZOMv7cCrOWgLeyamRTua_RXC6VpK67C0Xe-I-ig-8O1NAYzFMhZGJrl1TT7c6lK9p4a46fLBsyTCWTsx7-6KnuxkTlB6jQA3yad2RbGCOU3DVGH72x29H_lxA0LcMH8BPWuLZ2ZlJo2OX46jOdRjXYBZg4BohnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
