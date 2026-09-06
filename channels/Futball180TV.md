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
<img src="https://cdn5.telesco.pe/file/Yk_aN2BNTEALTKKu37m1Dux5Gr5Ra3gqdJEQykIzYOz144QoJ2mgzOpSz_fAWDYG83CgDl2FX4JoMlG04Em4uWZGS_Up70pBlqmgTDZzROhnSmqjQ4wRdxjA0C916tKckkdQNes02XAoDy_WmQ0PgDYX0DpoBsSxNc5TZZXdc1Cc4XEGNXZ6F2NpZ5W2BejUkGf1NRG1siFnrkq74Ecz7GYCtldYMqnWEcHC3ZsGLkomT234wkjo7OOarFvMVxb5R-yPoLtx4JNwHlOsUYhYJEj9pPq5Bo2c7R27up7sTzPVVpI2tQoAVm7lorlbGPe3qsHexM1QGe866DPeliOUJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 425K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-105730">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XbtOlb_ggSYFaQr3adnqLS5theSn9rAEuX4L1JCRofACVPskM6WkdYXR8_1U7Q65Rf4Xgz8QFkNp2H0qXUADemyAs3obTkXphngSLRH3T7dVdEqT22EU-gFiwoxd04fBlfv5X1MJcS6OCf-XIC5YlC9nxG7KkyYLWRA8i3Lufpy3AfvF4UjzmaaRv0j6DjNvj7hcj4UCSp_ovD6C3durMCKMt7xCt8TPNL1HbaIEavoscqANs6pHj8pPAZgLvWQkui1ZwpsKklJY41L9PkjgsfBN2FIfwmE6wkiyki-ENtKyTAI9RLK62SGfx17FXWXRfLTwRZ8015tOcu7yDdtun-o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XbtOlb_ggSYFaQr3adnqLS5theSn9rAEuX4L1JCRofACVPskM6WkdYXR8_1U7Q65Rf4Xgz8QFkNp2H0qXUADemyAs3obTkXphngSLRH3T7dVdEqT22EU-gFiwoxd04fBlfv5X1MJcS6OCf-XIC5YlC9nxG7KkyYLWRA8i3Lufpy3AfvF4UjzmaaRv0j6DjNvj7hcj4UCSp_ovD6C3durMCKMt7xCt8TPNL1HbaIEavoscqANs6pHj8pPAZgLvWQkui1ZwpsKklJY41L9PkjgsfBN2FIfwmE6wkiyki-ENtKyTAI9RLK62SGfx17FXWXRfLTwRZ8015tOcu7yDdtun-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی آرسنال به چلسی توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/Futball180TV/105730" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105729">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گل چهارم بارسلونا توسط پدری</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/Futball180TV/105729" target="_blank">📅 19:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105728">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هاورتز زددددد</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/Futball180TV/105728" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105727">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آرسنال مساویووووو زدددددد</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/Futball180TV/105727" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105726">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/581a696d28.mp4?token=mLWt08NV_92veKaVmnTd_AlcMnlkP5BZMtY_rzdCKNu4UW-dGVqeSbLIVDEMEuKKOxqFFILJ_XtjHCeljaghGo_7Ywi4UYYistuLaQe93QJUPGd2CpMz9p7WJVG8agMsEChTpnxHJBiWv5jJZ1EsesItVnNXz6oVBC9-qMRkAAmt1R0WbDHzmZRspwcPn3Fw0DiipBGmhx0A7yam0BPvxUAaiuBgRsevJo5yAJZs4g1XpI9FhLsjbHPTite87dJEh6pzGHHRr5_lOwXFWdMhOkk1OxCqy1oyoyKSqgz-U6jcp3U73ExkKv0iAma78RFKtaXXvKO-M0qN7ye3mjO2F4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/581a696d28.mp4?token=mLWt08NV_92veKaVmnTd_AlcMnlkP5BZMtY_rzdCKNu4UW-dGVqeSbLIVDEMEuKKOxqFFILJ_XtjHCeljaghGo_7Ywi4UYYistuLaQe93QJUPGd2CpMz9p7WJVG8agMsEChTpnxHJBiWv5jJZ1EsesItVnNXz6oVBC9-qMRkAAmt1R0WbDHzmZRspwcPn3Fw0DiipBGmhx0A7yam0BPvxUAaiuBgRsevJo5yAJZs4g1XpI9FhLsjbHPTite87dJEh6pzGHHRr5_lOwXFWdMhOkk1OxCqy1oyoyKSqgz-U6jcp3U73ExkKv0iAma78RFKtaXXvKO-M0qN7ye3mjO2F4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به آرسنال توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/Futball180TV/105726" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105725">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=vWF4OcVE--X_uHiyZQ2Kr22UMXQymqa-KGEE4a8F3_H_oVEA2ABgg4gAIEb6ucLUAsTj3sL-D-2sPjEFG8ddmoF-hWx2pn2YgDf67RPf235P5QtrG91Ql2sX9mEC_I6JRkIwPutOkVJXNpZwNUTVYT2QmaBfuLz_-tMRhz6NANP8IWZ361g8Z7L-A078xJs7Lclo6Hcq-87WZqWwWmJ_Hw9il49f_iKlqChYgXeJT0nK3MRY8CA2MDsLdizkCc8KloUtqcHzBj9BjIFgloKtYC_JC2kQAc1BohvqF13NYHnfS4QINJHFG3rqAsHfwbM8QursJFESDyOlmw3CjMnSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=vWF4OcVE--X_uHiyZQ2Kr22UMXQymqa-KGEE4a8F3_H_oVEA2ABgg4gAIEb6ucLUAsTj3sL-D-2sPjEFG8ddmoF-hWx2pn2YgDf67RPf235P5QtrG91Ql2sX9mEC_I6JRkIwPutOkVJXNpZwNUTVYT2QmaBfuLz_-tMRhz6NANP8IWZ361g8Z7L-A078xJs7Lclo6Hcq-87WZqWwWmJ_Hw9il49f_iKlqChYgXeJT0nK3MRY8CA2MDsLdizkCc8KloUtqcHzBj9BjIFgloKtYC_JC2kQAc1BohvqF13NYHnfS4QINJHFG3rqAsHfwbM8QursJFESDyOlmw3CjMnSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به والنسیا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/105725" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بارسا هم سومیو زد رافینیا</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/105724" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چلسییییی یکی به آرسنال زدددددد</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/Futball180TV/105723" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105722">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeGRXkP_lNESEfRiGC4n0Bpe4ggjQEnQN0fpXQssCI8Z7rgX3eqUGJUGRAeDPMxZ9BV1RRX1gowhMMWteCzJZnXsWY5P_qr0cLYLN-NjdBW4b5ymuUMNrhxhQh-60ggbgeRmh028FyZFUMczuuxd4GMay6Vyd8GQJnIwBvosqfOLh4rDsehXqnoXp2_-yr9CjP8acZrGocZBR7yn6dD5YfmTOaniDD9hoTBvHge7YDmQO1jfNPib3eKGJDbDTUnHAiGwIiEsd2ZwCPSDaG7SCYI6KZ9jNS9VdnvvyGpTAMakUhTivuYd-fk73srZ38lZ9AO-HifKs-U04gvFZjyh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رد ناخن حسین کنعانی‌زادگان روی گردن و گلوی عارف‌آقاسی؛ لامصب چه جوری چنگ انداخته
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/105722" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaR-6giyeSEixw78Q2WmenfqReFppO0HQqert961P3Pg_HmPa7oPuX_05qvCO5XKBA7_J523sLOi1OvpEHuB68F3I6N_f55VNC4NtB0OywC5oFfB3izJG_7scnldU1MW5KEkw8GE8EMY0O-Rv7HBqDYDpFfHux78AOu8m5brDWhofk6HPvOmz-xJ0qeY3KgmRVPUN8MO4CuywsS1O7SFQCJzJCHkeYuC-kqgdvsfH0s6CMkgLyMCqXQxwkJIiBaoZfSZoCl52MlWi8hUsUFTYc5nM-GrwIyKVFDNvZ95b4hs4I5LlT_Y1J2pLzzdRm-IcJzo4vgin5XG_rybQw_gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اریک‌گارسیا در بازی امروز بارسا بدلیل سر به سر شدن با رودری دچار شکستگی بینی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/105721" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV-uAxUd2uXsrr5Tznu9QjD0UeD6bMkRTTpsEmL-TZxoeeTTCEg2rdnePNGOL2qHWuPQ6zwR8avbHDFJUhCdsuN_8_w2sHg_jKepk_9RHx1XAf7NiuPOVRhdSC8yOp_K571kedhYir8LxJsHbfxzE-sTens3SWWxijdgXQofxL9-YrOufRUMHXI2w76DdoNoKJKbH4tNlUD8UYfVLtkKoFIzTq8Jcd8Ox72SUIP5FQC1DYZ1FKlWVn5ZAcXwWVetwMnJ9LTzfVvvwS7Ua8UCyd-lmsjhbcDXY3BeOeNllj0-YPNqWzVVhHoXYfgBow2GB855W499-ZCSomoDSZNe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/105720" target="_blank">📅 18:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fe998947.mp4?token=sbAJ-Dskx7XDXbF-lqBjb6pTPg1zLA119osyGJCD4vHJYky2hFfSuswwZgUaJKmgq4MZ141R6ySjdJCcFS9XBvLpYz7bDc_z0tKJgF2EGPHeUMWLJOOUYqzdpvtInEQ99UuYGDTHxP7sWDSUA6HKuQzt-Mbkwe_M5hCuJ4YFEDId82CZ6_CjBANIoow6mUi41eiuDz58LNV_yvDx1rz6xYmoFnUuuVdTNhCecGPAWIt2LeS4d-1cpIvxnl80TTvtc9eHDdMtoAiV5F99nCf4I2AuF03bhSqvKupC0tA74oeiMmRwRGuj23OtVRiCKQglqgwhQCDPZI_z8lO6rEgnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fe998947.mp4?token=sbAJ-Dskx7XDXbF-lqBjb6pTPg1zLA119osyGJCD4vHJYky2hFfSuswwZgUaJKmgq4MZ141R6ySjdJCcFS9XBvLpYz7bDc_z0tKJgF2EGPHeUMWLJOOUYqzdpvtInEQ99UuYGDTHxP7sWDSUA6HKuQzt-Mbkwe_M5hCuJ4YFEDId82CZ6_CjBANIoow6mUi41eiuDz58LNV_yvDx1rz6xYmoFnUuuVdTNhCecGPAWIt2LeS4d-1cpIvxnl80TTvtc9eHDdMtoAiV5F99nCf4I2AuF03bhSqvKupC0tA74oeiMmRwRGuj23OtVRiCKQglqgwhQCDPZI_z8lO6rEgnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
سوپرگل دیدنی در ثانیه های پایانی؛ گل دوم اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/105719" target="_blank">📅 18:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e19464327.mp4?token=LCYc_igokmkW57aLHwwPFdrmbMFz7bb6M798s5qPaNmZ2ZiHARuj8UzJdRghJFuHnBuf480tjfqlpUaaH2X11v5-YunM3o_j7aJ4aE2qJXXMpFw0e5j4lfjrrsPoSiOM19570DQADxTgIcD8rnr1Y5m2cOVsJ-Z5ZqY9l-Cdr0aIZI5p6zIqL7AimmGh6P2BdYoVuuiQAVcWDjlwCrxuTCGu-luEih8G2d4PAcEHL6amCPJDCLhvP32-bMRMJVf1_b-6YRNkZqKinitYEdn0avgRojxU9PEjMHjszEm5TtMxNTKq5NF_WPIgYXg6J49YKII-d54OkRf54r702vE2Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e19464327.mp4?token=LCYc_igokmkW57aLHwwPFdrmbMFz7bb6M798s5qPaNmZ2ZiHARuj8UzJdRghJFuHnBuf480tjfqlpUaaH2X11v5-YunM3o_j7aJ4aE2qJXXMpFw0e5j4lfjrrsPoSiOM19570DQADxTgIcD8rnr1Y5m2cOVsJ-Z5ZqY9l-Cdr0aIZI5p6zIqL7AimmGh6P2BdYoVuuiQAVcWDjlwCrxuTCGu-luEih8G2d4PAcEHL6amCPJDCLhvP32-bMRMJVf1_b-6YRNkZqKinitYEdn0avgRojxU9PEjMHjszEm5TtMxNTKq5NF_WPIgYXg6J49YKII-d54OkRf54r702vE2Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم منچستر یونایتد به اورتون توسط بنجامین ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/105718" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گل دوم هم یونایتد زدددد</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/105717" target="_blank">📅 18:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4032557f9.mp4?token=PMzAKg0yFlGF2KAl_bCDepZIL2mIUeyaw7suXAAfL3zWrryOeZpURzxCo31VlNGAu-le8oNaidqMa438QwsGKgEtD0-cCSmSv2KPkJGg0nGWGWo2dtBAl1uYNe0Jt2JUyuSGmWW-wjTda7KgRAB9CGGXriSIEaAsUrptKotWBGK2GOY1naJQ0EK8qQZOGr92ac5BCTW3Uopf_JgAm1F_Cb3wmVPiVK6F4rb61Q0LOj9SNCcKxxXOelXyq_KkJ87OYh4orOcr0hZP1nkI8PCPUV8-fV4NgNif75ck6XWnVEIPXtevG4VvF4pdOaBSSRqEFp2PJ0-CBvFu2rgweu1HTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4032557f9.mp4?token=PMzAKg0yFlGF2KAl_bCDepZIL2mIUeyaw7suXAAfL3zWrryOeZpURzxCo31VlNGAu-le8oNaidqMa438QwsGKgEtD0-cCSmSv2KPkJGg0nGWGWo2dtBAl1uYNe0Jt2JUyuSGmWW-wjTda7KgRAB9CGGXriSIEaAsUrptKotWBGK2GOY1naJQ0EK8qQZOGr92ac5BCTW3Uopf_JgAm1F_Cb3wmVPiVK6F4rb61Q0LOj9SNCcKxxXOelXyq_KkJ87OYh4orOcr0hZP1nkI8PCPUV8-fV4NgNif75ck6XWnVEIPXtevG4VvF4pdOaBSSRqEFp2PJ0-CBvFu2rgweu1HTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک به زاویه موافق لامنس؛
گل اول اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/105716" target="_blank">📅 18:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/105715" target="_blank">📅 18:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105714">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/105714" target="_blank">📅 18:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105713">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پاس گل از آنتونی گوردون
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/105713" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105712">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بارسااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/105712" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105711">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چه گلییییییی زددددددددددد</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/105711" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105710">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرمینننننننن لوپززززززززز</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/105710" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/105709" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAV-kjiui53B6cJt3ys8nBCNfoC4rR3M5z-fy93RF7yLXakH842D3vrOv7uBrulAxafqLbAWgUcczYHLkvOqqOaOZziRH9in6hvtAG3JRd4IeNSBbdaBIqruJDNYzpc6LRy01MEc1TzU7Sl2xw_MODAAHggwGEJqRqt7cikb63LGgfB0rJD3NNyEwX_WV3r4U6atPFiXTPQitMkoqBMhfw3zOdD_OsKotyBwCWMRRTsOufj9IrNnw6SHJFOh2jiXS3hTTDsExbOWaR4MIF-RhRasZ_BYyEI7qeEIx6ZcNfNejeTBKiNIrz7QXqZbkUSPkxYNfw7oUoR47IuCWf2p_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گلگلگلگگللگ یامال آفساید شددددد</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/105708" target="_blank">📅 18:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTEJ601g5m_o0gBmL-JDR81wEH0mVQZVl7aBEP1enhRxI51m3QymasWdi919AqSBclUGri4Qpctfippq0Ee5hVc-2gyaXYP1xhjaNFTPWNHd3H0xtcVbzAWatCZWM7sD8QFPwnQqjDQ9RyoXItPlhxTkvRMWNe9B9p8-c0d4RMiGVlc5rtRClEk1YdzHVpNLCIJ0bRonGC2AMu3BgQ4PpFJrqYpNV4ONdNCC9knBTwi2yPXIOW0AmgICbKUpY9uokVTGVPULVoH0mJYHP54tBbCyxBsFz3Se_KtO6LurmBoQZHBuJwQJ2ndULL_egc5azW3YAMew_udogUq7bL69gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب سپاهان مقابل استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/105707" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10c1daa423.mp4?token=pERjC6XoulOR76_HEvv4xLLQDjahINjvqgD4oD7uAeQXR7vnlwrou1qFNzT5UFvdoA0bm6duES3ciR2u82Q5upepxLhVTfCu-J1l9WHLx0AnaE8I51g7zzv15gOO3vcTU9kmdIMm4nIEQx0hY1-uvTV_RuX318O2j2LlKMSPNXsejZyg3PjSG6UiubObsz7RVi4FDRe7iGFgkdJVEhta5q_akTYzyD3H-h6ZQQ2oErRMgsvtSKz6cFCiLFi8ZlkuL1YKpATchPQnFABB3-nWAkaNaMG9SHxLoeYQs-0WcdCv7Ghz-xQARn7E9h3YeTXA6NWtI0gQcNDXa8mfwktxik3wd9Xn6-fi4FCGy7EcJf0yLc7ajCU7rf2ZRcRtAtBqXwh-YBfDqg2ayZ9Nyy445QMQUNPC8uXRq63rVe-5aOnTrxgbHIFxkNxvHZrgmluMFXhI6-UqBTGVqMimUtcXtzpu37Ezmd0-n7wpYwHBqUN08kCGZnB6Ov7Q-b9Jr1vDgSxqAjotfg35Fj445a51StBt_BddS0-gLZNrg-TQL0UjEf2AeoLGKPtoX-DmYt-CYjhluE5UJGuFBU2ksJo96VKdrOFHAx0XDmMF-BrZlAN7tunSEwYPcIi3c2UBe3X_leGNT-qe1iDx5gofrhtmSuyzU7Lg6fxmLEBgL4ih6QY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10c1daa423.mp4?token=pERjC6XoulOR76_HEvv4xLLQDjahINjvqgD4oD7uAeQXR7vnlwrou1qFNzT5UFvdoA0bm6duES3ciR2u82Q5upepxLhVTfCu-J1l9WHLx0AnaE8I51g7zzv15gOO3vcTU9kmdIMm4nIEQx0hY1-uvTV_RuX318O2j2LlKMSPNXsejZyg3PjSG6UiubObsz7RVi4FDRe7iGFgkdJVEhta5q_akTYzyD3H-h6ZQQ2oErRMgsvtSKz6cFCiLFi8ZlkuL1YKpATchPQnFABB3-nWAkaNaMG9SHxLoeYQs-0WcdCv7Ghz-xQARn7E9h3YeTXA6NWtI0gQcNDXa8mfwktxik3wd9Xn6-fi4FCGy7EcJf0yLc7ajCU7rf2ZRcRtAtBqXwh-YBfDqg2ayZ9Nyy445QMQUNPC8uXRq63rVe-5aOnTrxgbHIFxkNxvHZrgmluMFXhI6-UqBTGVqMimUtcXtzpu37Ezmd0-n7wpYwHBqUN08kCGZnB6Ov7Q-b9Jr1vDgSxqAjotfg35Fj445a51StBt_BddS0-gLZNrg-TQL0UjEf2AeoLGKPtoX-DmYt-CYjhluE5UJGuFBU2ksJo96VKdrOFHAx0XDmMF-BrZlAN7tunSEwYPcIi3c2UBe3X_leGNT-qe1iDx5gofrhtmSuyzU7Lg6fxmLEBgL4ih6QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/Futball180TV/105706" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiwU2q1eHD9XGTFNh8ncSRoNuntsEhPbJnhswKPRRkYvtyNUqdsmJkHmujMZLc8JZpDn7i6MhaZgm1QCHz3voOvbmhCVWIy4FETsYl9pmIfareKsaRVjTfng8apAj7OMWCH2H2N1hbdDtij8q1Hg4IEStsyabE4ltx_kv423SCsbyzyPCypI1y7Zkfj-2MmnTuYYmMCqvHQGCq4GZL8uW7HE9ptmJ37IZ80serqJ-YecVl9jsd5iYu2JlQvMWPEzTZH74fv7sMSvczAHLDCEsy5HmDEvADvVEQVH_0Z1kuOfpQr8jvPJC2QAkFSdoipVbCGFtvXrbpkhZbwyHWUdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اووووووف بارسا چه سوپریههههه
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/105705" target="_blank">📅 17:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-Mpm_Np9VLxKyPhaRAg9DQzCOhrfwot8ZPrcG-mEEGJ6YQQD2cpzLE1I5tFM9612lxoj0jZgzb5XdAtx0IFORX5ZhqKtMgDZTrd-4lbIcikrSM7S6gNF-kQVj4W4ns3JGeuzo1Ne4nsvqC6TDB0fyvMeJsDImmcloYUC2bV6EF9UE2MnA-rk2fUpfszEv-4x4TplXTOQVG7NvN_67nQqJa-gT8IJJEmYzP27jALwnCWL12IeIIhebnVMu-DBWf8SSAthVUoBHS3m5M7hmDVLmF54ZEeqc3mlAiQhZwAoB2Hjb-v6lIOglMt5ILiVU6MnoxEKWG1SSUK340ej0YRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMLpJwxQSiSwbFiPp7fYQG3_TvxYwhSzaiUe-SqIri_r80oTbkw3mq4C54EH31lHsDixemssQh_XAR_IgTUYOq6AagiYSIdcV7lsLKrLwSMLLpvrYf3AAiq0ucFvCfCzPqA_DlqMShIjQ9Q660P9EavWvpEXB4yTlb1JKgSFOe7m3kk5l_QXgIYXK0NnDF0m5AScx4Y_a-54bR_t3-2J4AnPUNDzDeHIMf5Ijlj90qDieiU6S9HJn1GJ_D16bGWhiQk6vxpz_7YfHvhSt7fuOFfbFH5Q1Tsc2uP3XGxAqA8VmdU66nuTLd-r3PDmh04gSKSaXJdHQKqTOjuFsAje9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکییب دو تیم آرسنال x چلسی
ساعت 19:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/105703" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اووووووف بارسا چه سوپریههههه
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/105702" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دبلللللللل لامین یاماااااااال
😂
😂
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/105701" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105700">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگلگگلگلگلگگل</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/105700" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چه گلی زد ناموسا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/105699" target="_blank">📅 17:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بارساااااااااا دقیقه ۶ اولیوووووو زدددددددد</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/105698" target="_blank">📅 17:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">لامین یاماااااااااللللللللل</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/105697" target="_blank">📅 17:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/105696" target="_blank">📅 17:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3e81743b.mp4?token=llMeFOSHN_lp5GBdP3eOy3s5W6z1om1eisRtgLmPcv2yX7JlH8SvwbPMZ5mwRzOT3xHoFCAULWdi0lsfV3yLFWWYNQ7eHyhAuZ8cjujWCzwiZ2c9_2aQYZv4DhOQoZBry5oYuFjTH2_lHzNvo8qlm3acdMsm2e5SleVXhMhASo1IX-W-EJFtiYQR3T30OgMm0MNEkSblUw4TGGHotquVuBc7XwKcEjzki-PXxDMMGe-bLump05lzSMeqdwk4_o5r1f7RmbGpX9GgWCJcgYpZ3waeXHFs3YqvCJS-DhJYLx2UEhIdLYdQWz7d7WHPcHwaBCH8ru4J10tcyP5wj9ojDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3e81743b.mp4?token=llMeFOSHN_lp5GBdP3eOy3s5W6z1om1eisRtgLmPcv2yX7JlH8SvwbPMZ5mwRzOT3xHoFCAULWdi0lsfV3yLFWWYNQ7eHyhAuZ8cjujWCzwiZ2c9_2aQYZv4DhOQoZBry5oYuFjTH2_lHzNvo8qlm3acdMsm2e5SleVXhMhASo1IX-W-EJFtiYQR3T30OgMm0MNEkSblUw4TGGHotquVuBc7XwKcEjzki-PXxDMMGe-bLump05lzSMeqdwk4_o5r1f7RmbGpX9GgWCJcgYpZ3waeXHFs3YqvCJS-DhJYLx2UEhIdLYdQWz7d7WHPcHwaBCH8ru4J10tcyP5wj9ojDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول منچستر یونایتد به اورتون توسط برایان امبومو با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/105695" target="_blank">📅 17:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdfVyqOw98p_19U2uOM8OGj_NIdUt0BMxAycMFmypMCizjh7nSpR2fyyjm8TiHdkLr3Q-iYIsFg0jST3ZEiV_SNKM061EdBYUAc0aersMIhMK2ggJnUR-lV7bFq9C09bUySd_OsLjiuNBqELrT_IjDkgT6luo9TwGE1-RllEGTN-WSPQWSwSVYOLrBHgZRrZcdD19jV6Ovdy6XU-3Ak1GEpTkHm8pGETPIkNolFk3qyCid9kna21SY3ZjnnjtkH2K3hDYw0-SkVRYhF3ZjIqqIL56JSorr9bYrInKAB0YyR-9ajIDLDKB4U7FfcQ5MVT8UZCCgxqylYjYOD0VXG6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ترکیب استقلال مقابل آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/105694" target="_blank">📅 17:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105693">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صداوسیما راحت با ۳ دقیقه تاخیر داره بازیو پخش میکنه
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/105693" target="_blank">📅 17:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105692">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امبومبووووووووو</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/105692" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">منچستریونایتد یکی به اورتون زدددددد</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105691" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105690" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105689">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdDTfjTPT5P22FYCtXX6shpbwGakEnPGf_phFaGY-33eGSab5nAQLWerEZro9hvMEvLnk3xH5h92jAzvtyntjclkcyR-NicJkrhAOSdDgCYhDzcFkN9IWo4DiTlBuDoY1PLvUEOecJlIKAwU3ZcPjTo4XHBmhbS0OrQMRxrN6airGQhtw1UKfePULgWI9vTvc9vLEKlYIEYiB1TBZI8jCHSgXIX2l2_y1o_njDby8nPbyaEkSFwjlHBdO-6vYpIrLNPEEMUmUqMesWCWAHOUe5mx-r0SsxY8V0_XUeJAmyUS6LBog54YYsrTlZi7CgyRaJ8k5Co0DYV_bZVrgyxg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
ترکیب آلومینیوم برابر استقلال
محمد خلیفه، امیرمحمد هوشمند، امیر نوری، ابوالفضل قنبری، شروین بزرگ، سیدمهدی مهدوی، سیدمهران موسوی، سعید صادقی، ساسان جعفری‌کیا، عباس کهریزی و امیرحسین امانی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105689" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aab68480.mp4?token=MmGdH28GlUli3JgpSQa6tEF4xwoKeSzi1zKnRb60jOdSyFs_f4xtAEiI9Eh8GlOl5z8243oRGBINSQQBKNZORTVtFpRTOn07olSwhEqDXoVBvT6aBifYXvSZNEdPXndTFTZBaPCwxRB-IfCDtIEzl3N_SoI_SFbi64Zz40SPK_BXIi6zy5Rw2DLadg6cTrhgYlgedWuVZN_XFhOkxqNNqpIM2EM7slZA4oi3wGdn8BpIetzt30HQPFB5MeNTKvzYRk85p71KvPoW3QT3f4wflye18b6nGr03U03-ZTQ9QBmCf7BH5LMyJ-pZ5_enSW8xvApQa--FxZAcoqN5y1lz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aab68480.mp4?token=MmGdH28GlUli3JgpSQa6tEF4xwoKeSzi1zKnRb60jOdSyFs_f4xtAEiI9Eh8GlOl5z8243oRGBINSQQBKNZORTVtFpRTOn07olSwhEqDXoVBvT6aBifYXvSZNEdPXndTFTZBaPCwxRB-IfCDtIEzl3N_SoI_SFbi64Zz40SPK_BXIi6zy5Rw2DLadg6cTrhgYlgedWuVZN_XFhOkxqNNqpIM2EM7slZA4oi3wGdn8BpIetzt30HQPFB5MeNTKvzYRk85p71KvPoW3QT3f4wflye18b6nGr03U03-ZTQ9QBmCf7BH5LMyJ-pZ5_enSW8xvApQa--FxZAcoqN5y1lz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
صحبت‌های هوادار استقلال
:
🔵
سهراب بختیاری‌زاده مثل مدیر مدرسه رفتار می‌کند! کاش صالح حردانی در مسابقه امروز بازی می‌کرد. نظم خوب است اما امروز باید صالح بازی می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/105688" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4C75l9JpCC-_zsEQ7JOgXInh3xnhuaoMz2rJko_mCyefz9Ti-lgLDDAANGmgt3GZNntYKRB8SVyOS-rO2UP21PyPb6hgOvZ6oOX9E2AywfJiisvEuw5A91GQHkNTkuqbgNhAaIlbTZUbUeMw8hOrtBzVX8hr9qDqi4hbPIODYK2JYrlD7DmtDIe-Kx0AUNv6rCDPIUtVU4V_JzbqvQb6xSdl7bGNsni_ues745fJo42OjZQiRPwDA8JhaiorH4StOBigJP2LoETd6uq7bK0bQmXVI9c1-kCLeekEgoZUCwxmXSYGLZDFG--RW7RzpKHRkJZvCms1qSKlBoDVFBdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شماتیک ترکیب بارسلونا مقابل والنسیا؛ ساعت ۱۷:۴۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105687" target="_blank">📅 16:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105686" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/105686" target="_blank">📅 16:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV9pgqmo3MQBX7pftymnIVFL7ymJsIvxu72DbWiUrewPVVWxqTi7TkfFJ63fEWTvgATDhLNxuFt6jy51nIOxxR9yJnGBe7fDxFoXga9JoP_w_mJKUZX5VE8Q_RJwLFd5hg0_pElapuyqWMCfM4XDRNC3dBpageMTVyXOt90AWz_vfZ0z6ZwEt2QpqCsRHQYPgQPu0Nq6ALdM8HuUnxonprSi67spfwYHjhUOiexpXjYr_EkEooVCiDh_a4pzIhVo7ewtYYjOIyE6sLyPsHQXdqYyYDj1DXb71P-WCI8CQken7jCm2_QVb32yH0KDW3F5DfwkMvkRnJfBUb-xYyGlnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105685" target="_blank">📅 16:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2bdbbb8d.mp4?token=UviRSFVHG8wAVYFx3ag1_wA1k2lDJC3ckoovIfWLnAglvTC18C3F0F1ftxlaYrdsypdARQD9gD3Oi2txH7KM1jFzIee3jOPk1xLcyZ0IiytT_G2Y48cS96bsDE_1IV67y7XOS57AwkEUCFGTV_28v6wHQ59CIV6RsbHUT1BhZq6N4tj94r-95waJGJss-91Yg5O3lE_tsMdebqlQENV4xlxbOTHYvvJ5aPV6oQhY4a8jU7XfiWb5b2pjxoISPct9dLVDEul0dW0oTTVCowLmSMRzY77Q1LrxsGHDdb1arrSu3iM07AkdtnQuiKrmUFsphtmy_8b37uuTB9G0VgexUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2bdbbb8d.mp4?token=UviRSFVHG8wAVYFx3ag1_wA1k2lDJC3ckoovIfWLnAglvTC18C3F0F1ftxlaYrdsypdARQD9gD3Oi2txH7KM1jFzIee3jOPk1xLcyZ0IiytT_G2Y48cS96bsDE_1IV67y7XOS57AwkEUCFGTV_28v6wHQ59CIV6RsbHUT1BhZq6N4tj94r-95waJGJss-91Yg5O3lE_tsMdebqlQENV4xlxbOTHYvvJ5aPV6oQhY4a8jU7XfiWb5b2pjxoISPct9dLVDEul0dW0oTTVCowLmSMRzY77Q1LrxsGHDdb1arrSu3iM07AkdtnQuiKrmUFsphtmy_8b37uuTB9G0VgexUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
وضعیت دیشب امید عالیشاه هنگام ترک استادیوم یادگار امام تبریز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105684" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd27d50a5b.mp4?token=vJxMY_u3Vs5hWKxow-VALG3RzALQk1oMIVjE_e7DigHQ1kgnM6rUFy0GleoqHJl47lmyhKH-t-Z0BtgnNuliD-fIT_NSHFM2I6yFeIF5JkTTZBRMvlEpMf2uG-7OobQsoPNgTyQwPwAW8VQB4vZVCOAV3SHkhgQQGgPEchiktSCJ1ta6BeHJ8pw7lioM-946f-i3pNnF9S4iup6R7-EXMCyxiDaFp160QBaHjxUb-Ydw_z0HWEuOb90YWXCSg82C_LZoY2_AZE-2whQVQTNpOlwFQt5Y3I4tdl9Iq3iiRfBRKK3Lxv8MQb8qiQxSV5ry7a8gOnLnM8huY_vOryBnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd27d50a5b.mp4?token=vJxMY_u3Vs5hWKxow-VALG3RzALQk1oMIVjE_e7DigHQ1kgnM6rUFy0GleoqHJl47lmyhKH-t-Z0BtgnNuliD-fIT_NSHFM2I6yFeIF5JkTTZBRMvlEpMf2uG-7OobQsoPNgTyQwPwAW8VQB4vZVCOAV3SHkhgQQGgPEchiktSCJ1ta6BeHJ8pw7lioM-946f-i3pNnF9S4iup6R7-EXMCyxiDaFp160QBaHjxUb-Ydw_z0HWEuOb90YWXCSg82C_LZoY2_AZE-2whQVQTNpOlwFQt5Y3I4tdl9Iq3iiRfBRKK3Lxv8MQb8qiQxSV5ry7a8gOnLnM8huY_vOryBnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇮🇹
شادی فوق‌العاده شب‌گذشته لائوتارو‌با هواداران تیم فوتبال‌اینتر از این زاویه خاص
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105683" target="_blank">📅 16:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس: اینکه پنجره نقل‌وانتقالات تیم استقلال بسته شده به من ربطی نداره و مشکل از مدیریت خودشونه. اگه استقلال بازیکنانش رو به تیم‌ملی امید داد ماهم میدیم. اگر اونا ندادن ما هم نمیدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105682" target="_blank">📅 15:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df0581598.mp4?token=t_mONKRyFT157Vl1MUGve7GV3n_OFX8Q7UrokthzVlbQmmhZ5uOGqitC0C_l_7nrbn0S3gEbsrI_GZD2fY2JTxQsrrVO1CsYjuSm-vWIDo23kA2KOqLQj7uB4ghQ76MHF5ihf4Bz7hXDuS8Rs4aVM1zzdl3Ln2lWGQwXBZNeS6SQ6WSNmNNOPOj-zpkSKQdjXc2u-8vbEsALBHht40PGXdMr1PISDNRQJ-2PPom7f6QLpmaGjmwJ4B5Se6tZNUS7qahSpHELrn1pehC_9BULQpDbaaLb-m9VHx67BleziJYNihLZmw7QrRtipVeIBR2-N1jg2grZ3HM3pkELmbOCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df0581598.mp4?token=t_mONKRyFT157Vl1MUGve7GV3n_OFX8Q7UrokthzVlbQmmhZ5uOGqitC0C_l_7nrbn0S3gEbsrI_GZD2fY2JTxQsrrVO1CsYjuSm-vWIDo23kA2KOqLQj7uB4ghQ76MHF5ihf4Bz7hXDuS8Rs4aVM1zzdl3Ln2lWGQwXBZNeS6SQ6WSNmNNOPOj-zpkSKQdjXc2u-8vbEsALBHht40PGXdMr1PISDNRQJ-2PPom7f6QLpmaGjmwJ4B5Se6tZNUS7qahSpHELrn1pehC_9BULQpDbaaLb-m9VHx67BleziJYNihLZmw7QrRtipVeIBR2-N1jg2grZ3HM3pkELmbOCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی تارتار، سرمربی پرسپولیس:
از فیروز کریمی(پدر زنم)من خیلی چیزها یاد گرفتم‌. الان چون ایشان استقلالی است زیاد نمی توانم مشورت بگیرم اما از او چیزهای زیادی یاد گرفته ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105681" target="_blank">📅 15:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105680" target="_blank">📅 15:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105679">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
واکنش تارتار به گل پیروزی‌بخش تراکتور مقابل گل‌گهر: نتیجه باید در زمین مشخص شود/ مطمئنم که مسئولین بررسی‌های لازم را انجام خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105679" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=FAChvuDse1ZPhpX4xy_ZxRR014G0MsJYifTkMLt1dCGmfpkMg-IpOa_rQlQXf_pkXYYUt-w5b5O033BsUhnUE-b4hf6EzqNxEnGMan5gXHXhVFj6GYWzwUZHGpOhKzjtqaLQ6QirPAIUpQqU2dsJaop9Fud3eg6SUtENyPSAiYUoXCdJExNG7DCe4baayHaEBCK0iQnKpyxt6bCTisAzOW4ncUQoSyqBLuQuMmAChfpvkSRWvvlYY6iYCfsK0uLocUb2B_K08keGAot_rrD2sgvEK7zb5IkNEKrGySz82k8lkUlVQl1JuG1k_gzLUdRb7x483ZuWdD0fekwS-lecsIBHI3mhJRcECdHcmj9p334qcZV2a0Ds9jiaZgY9_yK6DfzLhjw3fG566mG-RKJPuOgAp9GlNaqKdXP-Is8zEhpgxY5fS5AN6rT3n_6Qpg94WBrHke0htT4ZajwT_q3rfVltldNmY1e-h8J-LgqCgO71nFqi_qef8QExslWWo4HMIl6yNKOKvOF9KHZjTYVzDwPM1vRGF1bhJqx_3TrQJO8qQjdTinj2-_CBLph5pkdOPhLm6vfIlvY9Ar0gHGiDgh6UEkV-waK9xUOJOjtyvKc4xdOGqWZ_30JopqNnBpO1yDyr4Iu700uUefbUycNCKhMbWCGA2NqXL7MbomohOX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=FAChvuDse1ZPhpX4xy_ZxRR014G0MsJYifTkMLt1dCGmfpkMg-IpOa_rQlQXf_pkXYYUt-w5b5O033BsUhnUE-b4hf6EzqNxEnGMan5gXHXhVFj6GYWzwUZHGpOhKzjtqaLQ6QirPAIUpQqU2dsJaop9Fud3eg6SUtENyPSAiYUoXCdJExNG7DCe4baayHaEBCK0iQnKpyxt6bCTisAzOW4ncUQoSyqBLuQuMmAChfpvkSRWvvlYY6iYCfsK0uLocUb2B_K08keGAot_rrD2sgvEK7zb5IkNEKrGySz82k8lkUlVQl1JuG1k_gzLUdRb7x483ZuWdD0fekwS-lecsIBHI3mhJRcECdHcmj9p334qcZV2a0Ds9jiaZgY9_yK6DfzLhjw3fG566mG-RKJPuOgAp9GlNaqKdXP-Is8zEhpgxY5fS5AN6rT3n_6Qpg94WBrHke0htT4ZajwT_q3rfVltldNmY1e-h8J-LgqCgO71nFqi_qef8QExslWWo4HMIl6yNKOKvOF9KHZjTYVzDwPM1vRGF1bhJqx_3TrQJO8qQjdTinj2-_CBLph5pkdOPhLm6vfIlvY9Ar0gHGiDgh6UEkV-waK9xUOJOjtyvKc4xdOGqWZ_30JopqNnBpO1yDyr4Iu700uUefbUycNCKhMbWCGA2NqXL7MbomohOX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105678" target="_blank">📅 15:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1304ef0ba1.mp4?token=jaXD9lbumtcLfolrmZ-WKXQAA48AjMVOafZg2oR1EKfP5AD7MLfryLAZ5a1QLZ4fBNamYq39bUAaxj4X_ZFvXZVgPZYjeJt-3L5Z6SeUQYEQ8I_msjPJk4uqi7TY2NZLzNVYgOnVpT_NWS9VV0j7zn50eDm5N18p7a2Dj330tfR7pstT1vB3ip7xFdxyURo_Fixw8_GU3krn5mcYZLxUhLARrJaQwO6hXtKR3Gxoi8qoEer1XnHWtRpTEcZYTqFgSpSl_JlFRjVRDKQ7plC5AhdtX52yv11vvZAqaYD3IBQnWh7wVL1v54xHnSXxvfQJP3DVPbw32nSLefIo5rAI0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1304ef0ba1.mp4?token=jaXD9lbumtcLfolrmZ-WKXQAA48AjMVOafZg2oR1EKfP5AD7MLfryLAZ5a1QLZ4fBNamYq39bUAaxj4X_ZFvXZVgPZYjeJt-3L5Z6SeUQYEQ8I_msjPJk4uqi7TY2NZLzNVYgOnVpT_NWS9VV0j7zn50eDm5N18p7a2Dj330tfR7pstT1vB3ip7xFdxyURo_Fixw8_GU3krn5mcYZLxUhLARrJaQwO6hXtKR3Gxoi8qoEer1XnHWtRpTEcZYTqFgSpSl_JlFRjVRDKQ7plC5AhdtX52yv11vvZAqaYD3IBQnWh7wVL1v54xHnSXxvfQJP3DVPbw32nSLefIo5rAI0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاطینِ پنالتی این فصل در رئال مادرید دور هم جمع شدن.
🤝
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105677" target="_blank">📅 15:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae12814c.mp4?token=FGk12Xm6vmDLl2jKnWMS0lEHXqlLD2j3sR_vhaH7BTp44cYcmWleBcTb9PvYSjPvIzpTd4wcbatTdKJIMkhBRkk4EfnlH_Dt-zPoFVJi1RZIGAUJ1ov4SceAgXMKKmfiLhA956cy_kPMGSu6SIR2JmcwECK7q3VTsLTFGYWfQL1vFE6nLRo8aMVvz2MjlAVZi7rt8NJh5qPI1cCxi7p87knyj6QQj3aJd0sSLoOFNgh7YAHDwAB8mvUzhhLpL3RLe4xHjv6SbwGcn9psgeJIdi3g3W8ruEL31UstG_ezzIz0pvZYBZu3FM8uVvh0NNLPpYstHHapasL5fLwMog80MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae12814c.mp4?token=FGk12Xm6vmDLl2jKnWMS0lEHXqlLD2j3sR_vhaH7BTp44cYcmWleBcTb9PvYSjPvIzpTd4wcbatTdKJIMkhBRkk4EfnlH_Dt-zPoFVJi1RZIGAUJ1ov4SceAgXMKKmfiLhA956cy_kPMGSu6SIR2JmcwECK7q3VTsLTFGYWfQL1vFE6nLRo8aMVvz2MjlAVZi7rt8NJh5qPI1cCxi7p87knyj6QQj3aJd0sSLoOFNgh7YAHDwAB8mvUzhhLpL3RLe4xHjv6SbwGcn9psgeJIdi3g3W8ruEL31UstG_ezzIz0pvZYBZu3FM8uVvh0NNLPpYstHHapasL5fLwMog80MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎾
👀
واکنش خانم‌ها به تعویض لباس آلکاراز!
کارلوس آلکاراز پس از پیروزی مقابل وو یی‌بینگ در دور سوم US Open، مقابل جایگاه تماشاگران لباسش را عوض کرد؛ صحنه‌ای که با واکنش‌های جالب هواداران، به‌خصوص خانم‌های حاضر در ردیف‌های نزدیک، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105676" target="_blank">📅 14:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105675">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e7b0fcfb.mp4?token=Pljd0I-KKo4k4abXVspcj2w4cltEVyoulLKILLzJ8QneZOvvDCXt8_dH5MgPEIMbLWhiWpDwv-nAt2zHDc_Bbq7BaM1MCIFde8pTfaym5J3R_yvEIm8Bl0VJDvhcrx9OHiSm9qsPRuplTq-jjIopZQydMWr9124SaVs2jJOmoDv1oN-cqGOhx-Mnqy2yS-_0TxmBlcyhu7faRK6tVFnMuqHCZ6UpTQcZrYsX5CJn2_t5ufiN0zdeu_9hhyhzfXxhYV5WdsRQyBTKALDguSSrsc0gwBk8eH2fRq5bYU84x_xRqD7wprseZa4RqNtYDNgqFbM9Os2N0L5wuoz8tg4qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e7b0fcfb.mp4?token=Pljd0I-KKo4k4abXVspcj2w4cltEVyoulLKILLzJ8QneZOvvDCXt8_dH5MgPEIMbLWhiWpDwv-nAt2zHDc_Bbq7BaM1MCIFde8pTfaym5J3R_yvEIm8Bl0VJDvhcrx9OHiSm9qsPRuplTq-jjIopZQydMWr9124SaVs2jJOmoDv1oN-cqGOhx-Mnqy2yS-_0TxmBlcyhu7faRK6tVFnMuqHCZ6UpTQcZrYsX5CJn2_t5ufiN0zdeu_9hhyhzfXxhYV5WdsRQyBTKALDguSSrsc0gwBk8eH2fRq5bYU84x_xRqD7wprseZa4RqNtYDNgqFbM9Os2N0L5wuoz8tg4qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بهی جدیدی، بازیگر نقش مهرو سبابه‌چی، نامزد مسعود شصت‌چی در سریال «مرد سه‌هزار چهره» به کارگردانی مهران مدیری است. وی سابقه فعالیت‌در تئاتر را در کارنامه‌اش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105675" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105674">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sH2_v-QtadBIN3Bk5wK_JZNH7qmfi__w9ePOvx-_j9aEhSE5_qvTAgKIj4lUVa6bUiyBGXc6QrDxAGP34OfUQcwIBzvZCvBRC7a7KxFlcXqGbAD0ydZrjIaYbl7XqTHljKmM1JTJMsufXp00K860Ss2Eetc3O2eu_y_YSS3g2PdqBFViDASUM8WJjl9Jtbg_ArRhf6KpeAnLJ-boi3jcLTYc4x7JdX2IRiaU2rGURenPSpMtWB4hZSLGsY8tdzm5S6HPTmhpEcvpbUXapr7z3QcIGyhLbcd58gsICzf18GDmhcamzrUIX_BYRQASj_Q7TFeTqL0_y1vtGUKxUllQink" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sH2_v-QtadBIN3Bk5wK_JZNH7qmfi__w9ePOvx-_j9aEhSE5_qvTAgKIj4lUVa6bUiyBGXc6QrDxAGP34OfUQcwIBzvZCvBRC7a7KxFlcXqGbAD0ydZrjIaYbl7XqTHljKmM1JTJMsufXp00K860Ss2Eetc3O2eu_y_YSS3g2PdqBFViDASUM8WJjl9Jtbg_ArRhf6KpeAnLJ-boi3jcLTYc4x7JdX2IRiaU2rGURenPSpMtWB4hZSLGsY8tdzm5S6HPTmhpEcvpbUXapr7z3QcIGyhLbcd58gsICzf18GDmhcamzrUIX_BYRQASj_Q7TFeTqL0_y1vtGUKxUllQink" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری وزیر کار دولت رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105674" target="_blank">📅 14:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d1369def.mp4?token=DaHCsjTANwZPd8zZzasqv16SJZa5pu5tdV5zT1-NNaxh5A4xVeKSc4sCzb-dYzRefJnptPgEImuqDoQdRehi6MhcUdYZFZg1tKqLXrp8DL_SuUAVsn8jsSf6B60hZopMKQGDVOwh5e_LEYNz2ylrGCdpntxdkk7qdaO0hDRhDzgiPR6NjFipPMIeU6RTGC1gl2POu-lUmgSyMCeviZ_IuuVHu2X79ifBm9w34AR93dLiapzAJT6_dhKwtCDjJmwaiLHxRCBWtp1yxmzf-VwFmpDkAZGNq7oQXqOb5Y0jUTTtzwKb4SrerdPmdr0RbHBRm-1_ji-ndCxhN98bW57AZ4nRITDv3fptHGA_1kGvL777l3m8_JD1fnbPS3mvW6NRz5noBv1VckJRo3ccdkMGSaI8EzFX_Qh_u-ACbj2dZ_7k56C2S96HLbH5fm62Z99tgIJvEIaSAtasO6G5a-VTVevdItWJ6q-1vAYEblxxg4D8d-23IyZfCP_q1KHMdgUeKC651CaKY2S_jWEN46nHsG_0H3F7MrrJXaMXqUyRIE_aJbIlPLGQQUuFvyos-tCyBaOONq6J3zumpUvzxVO1u2t2NgZ5VTQoS_iGlzjksoLCqoolUWB4TC2PnquXXfnX9RGtqC1pqZ3Srsg8T81CWl0HLXNFuI4JoPMADMBcrzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d1369def.mp4?token=DaHCsjTANwZPd8zZzasqv16SJZa5pu5tdV5zT1-NNaxh5A4xVeKSc4sCzb-dYzRefJnptPgEImuqDoQdRehi6MhcUdYZFZg1tKqLXrp8DL_SuUAVsn8jsSf6B60hZopMKQGDVOwh5e_LEYNz2ylrGCdpntxdkk7qdaO0hDRhDzgiPR6NjFipPMIeU6RTGC1gl2POu-lUmgSyMCeviZ_IuuVHu2X79ifBm9w34AR93dLiapzAJT6_dhKwtCDjJmwaiLHxRCBWtp1yxmzf-VwFmpDkAZGNq7oQXqOb5Y0jUTTtzwKb4SrerdPmdr0RbHBRm-1_ji-ndCxhN98bW57AZ4nRITDv3fptHGA_1kGvL777l3m8_JD1fnbPS3mvW6NRz5noBv1VckJRo3ccdkMGSaI8EzFX_Qh_u-ACbj2dZ_7k56C2S96HLbH5fm62Z99tgIJvEIaSAtasO6G5a-VTVevdItWJ6q-1vAYEblxxg4D8d-23IyZfCP_q1KHMdgUeKC651CaKY2S_jWEN46nHsG_0H3F7MrrJXaMXqUyRIE_aJbIlPLGQQUuFvyos-tCyBaOONq6J3zumpUvzxVO1u2t2NgZ5VTQoS_iGlzjksoLCqoolUWB4TC2PnquXXfnX9RGtqC1pqZ3Srsg8T81CWl0HLXNFuI4JoPMADMBcrzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
جمله کنایه‌آمیز نکونام: چون یکسری قانون خوب داریم، تا نیم‌فصل نمی‌توانیم بازیکن بزرگسال بجای مهدی‌ترابی جذب کنیم. خودمان برای حضور در آسیا دست و پای خودمان را می‌بندیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105673" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105672">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105672" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105672" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeZTR4HSxy5Vg1P186ADbc7xAoizTpqahUX7OGNeEXEDz4LqcX72NnBbnDiXWdz2g25L2z2ZhPYSuz6ATPmMVntJMz3kvIqyFqQLHXU9z6ssbcmD-l0x0VZXiWpiKaLc8D-RDVifnuOud5m2_saCEyJKCUsEqpm-k_jDIvM1ODc3zFwDtXGS0QC3C0sYmWWYaBu7c5AJJq-ESRsd7zaLhE3Ly8oK5PtHliknghyGDiHTly9mK4dglvtty7IgiM7Ie4pdO46M4ipHrIwFo6fiNbPnPk4Wq0p0NTGOiiOXWA_7-Mh0UaBclv3TYydGMZX7KLldVahYaBethjzCLsuNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105671" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AltGx_nBK4ouUEM972RpCXZKOoZX2MFkubhjS2hs0LnQtLo6TD1PSg3bEhBHF9f7-PvbRBwk948_7Yuhi2MMxyQfwB6r6LhbWSnIs-Tbjw2I3MAxlwwO2mODpOHEHy1s4k3WPuhG033EuKLZARusWZdzXups8ncZhw8DlLe6N2bOjB62Ihw6Y02evSQlYWYP3PkQakeaeihYd8v9L0k6-DX45cOyY_JBqNKUljN_rKLqCpdAVFczOnC8r9UEhdG47WHYnbiyD1yFJMAaVBA93rOgpK2A_IkrseAounwiEIBPbbJWiE6IkovmuwiumYbAJaqNxxc6rXh-4pdvpbri_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🤩
🇮🇹
🇪🇸
مایکل‌اولیور انگلیسی داور بازی روز سه‌شنبه رئال‌مادرید و‌ اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105670" target="_blank">📅 13:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105669">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7107d982.mp4?token=MXKiklKrFSlrR5P28FWD6N3S3x9-qKsPqqrS566EFnHBM8NTUEJX8yCzbIUimF8_B45dwWkkVNHtmGa1vlRMK1HCEL-vDoYNWz30Bnd6oUnvI3Nybeun5j15KHeQAmVT9mgxmM-a9GAI5q3kxvi-ZBN4tY6AASAo9wD-gJ9ju5daYbtBY4CH9H32bZgVJ-keeMoVIfuItrqu7pZQzek8RojhxVu_rIv1MZMt6KcxVw6ixKFfpre6XGW4nOsa0S_DnTiokiqPrRSz8AwKsdsrGbxoitov6Jxk9ExZ0cNId1AU2yd0ITgWHyrUSpoa-T1RFMBfqK6MCIvanPvK_5pG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7107d982.mp4?token=MXKiklKrFSlrR5P28FWD6N3S3x9-qKsPqqrS566EFnHBM8NTUEJX8yCzbIUimF8_B45dwWkkVNHtmGa1vlRMK1HCEL-vDoYNWz30Bnd6oUnvI3Nybeun5j15KHeQAmVT9mgxmM-a9GAI5q3kxvi-ZBN4tY6AASAo9wD-gJ9ju5daYbtBY4CH9H32bZgVJ-keeMoVIfuItrqu7pZQzek8RojhxVu_rIv1MZMt6KcxVw6ixKFfpre6XGW4nOsa0S_DnTiokiqPrRSz8AwKsdsrGbxoitov6Jxk9ExZ0cNId1AU2yd0ITgWHyrUSpoa-T1RFMBfqK6MCIvanPvK_5pG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مارسکا در مراسم معارفه ایوب بوعدی به بازیکنان سیتی: فقط خودت باش، ما میدونیم تو چقدر خوبی، اینجا لازم نیست چیزی رو به کسی اثبات کنی. کار کن، یاد بگیر، لذت ببر و خودت باش.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105669" target="_blank">📅 13:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b1b9b41e.mp4?token=torDMykcFBIMAOcbU2NW02ucmSYozrRtPAC-yj14pRpmclxDUWK0ic6GrAuIqN7j0dwVXA2jeDMLpPSyHZlwPPE8-Ojr9lr7KzDvwDMEUY_qhRSb58U-tBHhmMGsBrdAgcYY7HZ3HN8CuvIGBk3DdPmCDLKLoZvun3z2gUAjODxLcb8H5hN5KoCZEJZd0Zz4-Lxex8mOuUc6ufIl5iIol8rP4cZiCYMYM4v_IbwgrOBiNyw5D5vX3DLY9uABuYLxRFy8h0afPOGaVCpE6TA3--PHjvADWlY7LoncK95TvvBJb5ZUN1kKHe0xpjjBTSO3fioNkfPJqnKEoUSCxs79vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b1b9b41e.mp4?token=torDMykcFBIMAOcbU2NW02ucmSYozrRtPAC-yj14pRpmclxDUWK0ic6GrAuIqN7j0dwVXA2jeDMLpPSyHZlwPPE8-Ojr9lr7KzDvwDMEUY_qhRSb58U-tBHhmMGsBrdAgcYY7HZ3HN8CuvIGBk3DdPmCDLKLoZvun3z2gUAjODxLcb8H5hN5KoCZEJZd0Zz4-Lxex8mOuUc6ufIl5iIol8rP4cZiCYMYM4v_IbwgrOBiNyw5D5vX3DLY9uABuYLxRFy8h0afPOGaVCpE6TA3--PHjvADWlY7LoncK95TvvBJb5ZUN1kKHe0xpjjBTSO3fioNkfPJqnKEoUSCxs79vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
روایت تاریخی رویانیان از هزینه مراسم وداع با اسطوره مهدی مهدوی‌کیا در‌ پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105668" target="_blank">📅 12:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82f6d2ba8.mp4?token=GiCZQJ4R5ATForN0WqzDGl7BsIvR6uL3wayDQPIR7_QbvkI8mQt9xJ1oiwCpTZme69gwGEtkMEFYETmLVYZLfmTqLNNHoIJ66hUiYsvK5tZ_YM2TTkTZ3Rxa4JpKk-8ewr0ANYoiSiZevXRB1_I37e306YjvckBCOX4Vn4CG_BOAkl1Gz3mgWTtdu8gN0Z9O-W-2gzKpYacbf7V1tHvPIgM7S7TlGm3oibF_NL3h5Qf1ecjlGFIPWGmxABl5Fs6bW6ePt1obCikq77q5RTtRamD47I8T9IV7H93WmastRs7x3xivJhjnduJfSo_UBaWQEsNsovPKd-hJqq88pQQzNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82f6d2ba8.mp4?token=GiCZQJ4R5ATForN0WqzDGl7BsIvR6uL3wayDQPIR7_QbvkI8mQt9xJ1oiwCpTZme69gwGEtkMEFYETmLVYZLfmTqLNNHoIJ66hUiYsvK5tZ_YM2TTkTZ3Rxa4JpKk-8ewr0ANYoiSiZevXRB1_I37e306YjvckBCOX4Vn4CG_BOAkl1Gz3mgWTtdu8gN0Z9O-W-2gzKpYacbf7V1tHvPIgM7S7TlGm3oibF_NL3h5Qf1ecjlGFIPWGmxABl5Fs6bW6ePt1obCikq77q5RTtRamD47I8T9IV7H93WmastRs7x3xivJhjnduJfSo_UBaWQEsNsovPKd-hJqq88pQQzNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇶🇦
شادی‌گل فوق‌العاده سمی اکرم‌عفیف در بازی دیشب السد در لیگ‌قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105667" target="_blank">📅 12:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdb42b18f.mp4?token=IYyEs_0DefON2BYtGvmbDU69lm2S7p_4r7qvymhDgpMB_f2H5wtiySnX4xQBIA28DFaN5GeAkhrcVZ1ICDmx3jrbVsofbU5DSba-s7IeYHLE9t5YwCTf_79n8iQzDTgotNeUDGqMSARU1hVIPsdDSd6XvFITQ_vN_MGH6cutb2n0QFlpxKKF1EEEu2__CI3yY0SmHkO3SExdz-8-vGL0OSjEQhuaLxh09z3MOF4FjWAlFS7UsUFj7-G-wRnyWjRnieHb4CPg80HxWVVjUcodm4fiw5dMlD0D53eaMKytPA3FwY8J5kFKfcB5gubhlsej-7-dAOdb4LdwUFMYLezW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdb42b18f.mp4?token=IYyEs_0DefON2BYtGvmbDU69lm2S7p_4r7qvymhDgpMB_f2H5wtiySnX4xQBIA28DFaN5GeAkhrcVZ1ICDmx3jrbVsofbU5DSba-s7IeYHLE9t5YwCTf_79n8iQzDTgotNeUDGqMSARU1hVIPsdDSd6XvFITQ_vN_MGH6cutb2n0QFlpxKKF1EEEu2__CI3yY0SmHkO3SExdz-8-vGL0OSjEQhuaLxh09z3MOF4FjWAlFS7UsUFj7-G-wRnyWjRnieHb4CPg80HxWVVjUcodm4fiw5dMlD0D53eaMKytPA3FwY8J5kFKfcB5gubhlsej-7-dAOdb4LdwUFMYLezW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل لیونل‌مسی برای کاسمیرو در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105666" target="_blank">📅 11:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105665">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a3702d1a.mp4?token=iUGOjCp5FpT3abBIH7iS2PwS91kFoGe-dJkegn_YVoSI6JKGHyk42s-YIXG7qUGyM3bRRiJM5xzJpgkMDFjgGpNqpH1dU9Q642su-osHEcLyJ5c8xI288ZxXXN_VZuWt0HrI6kkcHqp0LCnL7bmp6tX8vBmOM56qNxdHHjUf6p_l2bSWvsKKLsUJNOV6k-Y6Q10ruyyL8JArz2HheySBF5eoRqH-rc8WGyY8_-u4RIFCkwWNJR5m_UqfEuLWPxZxGV_ECAMr8i-I9x6ZP6nUodyOePzJWAcftx9wgjqPPHhEVwsO7jxPTXHCuEBR3_9uRfHnWHBviIkEdqpqVvjm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a3702d1a.mp4?token=iUGOjCp5FpT3abBIH7iS2PwS91kFoGe-dJkegn_YVoSI6JKGHyk42s-YIXG7qUGyM3bRRiJM5xzJpgkMDFjgGpNqpH1dU9Q642su-osHEcLyJ5c8xI288ZxXXN_VZuWt0HrI6kkcHqp0LCnL7bmp6tX8vBmOM56qNxdHHjUf6p_l2bSWvsKKLsUJNOV6k-Y6Q10ruyyL8JArz2HheySBF5eoRqH-rc8WGyY8_-u4RIFCkwWNJR5m_UqfEuLWPxZxGV_ECAMr8i-I9x6ZP6nUodyOePzJWAcftx9wgjqPPHhEVwsO7jxPTXHCuEBR3_9uRfHnWHBviIkEdqpqVvjm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😁
🇮🇷
🇮🇷
ویدیو سمی آلومینیوم اراک برای بازی امشب با استقلال در هفته‌ششم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105665" target="_blank">📅 11:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105664">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA1Y6xbvWl05rbWjcResxzpO3sbgy9odCIDzeLq-K8JUTixFvMbbRq02bmY8lN_i5yhoN621xqQpyFJXqbJI-bchvipCJ6W9gi091x0YCwEGlSSxtgwTVBO9cLYIO8FqS5AGGQcZDrXG8PvZDws4_XnKObxnkgnXkQoNLQvUC4xvOwhUF5SnIJMnRckSEOUi6ly-ELjfW8YYYf-UVOcfQKnrqoE5gAGQOMQzePP7us7hZK3TasmJjiMgWLvtyAS1qVnH2bjgRZsKI40Urh3mTeCyG8PzuJeESTdR-w2bIHeanD6h7jNmvVSBLI3M5zck-rxC3dEOzvoICVd_2B9Y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
بیانیه جنجالی باشگاه تراکتور در مورد امید عالیشاه
‼️
رفتارهای عالیشاه دیگر حاشیه نیست؛ یک رویه تکراری است
🔴
این بازیکن دقیقاً چه مصونیتی دارد؟
🔴
چند بار توهین و خطای خشن دیگر لازم است تا قانون اجرا شود؟
🔴
چرا داور مقابل چشمش توهین‌های عالیشاه را می‌دید اما جسارت اخراج او را نداشت؟
🔴
عالیشاه پس از سوت پایان هم به مدیر تراکتور هم توهین کرد
🔴
سال‌هاست در تبریز از خطوط قرمز عبور می‌کند؛ اما خبری از برخورد جدی نیست
🔴
اگر اهانت به داور مستحق اخراج نیست، پس کارت قرمز برای چه زمانی است؟
🔴
این‌بار نگاه رنگی نداشته باشید؛ قانون را اجرا کنید
🔴
اگر برخی بازیکنان فراتر از قانون باشند، دیگر حرفی از عدالت باقی نمی‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105664" target="_blank">📅 11:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105663">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d77d3348d.mp4?token=P-K9BK5RVIkWrlbwvk_NxRrU60Znj6dtSKa6-V6Yw3Kjg_Na3DMAnK2MvxwFaFI0vTtImcj2hYMBYotb3sb7dtpDf1vdoGc_kLJVmYEsv7QJwsWorKC7loIBdt5CUC4AqexUSpHjbl4lCpY3BInEE_R7EHqhqC5isOYU3X9JnG80d6l1VLm1rcG7HDakUDhPHQMbCQlRweR77ce_ph3bEOZVaFYl_u6Tr08V7L2Eh3O_jfNG0MgI8Jf6V3MheVUe8cCxUt2jzdcI69MdMK_ForsdsQ9rwop1sqDn0rJC0aEvmhhmGV-eoAcj5hnjge8WDsgjQOJf7odhOYbYxOmCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d77d3348d.mp4?token=P-K9BK5RVIkWrlbwvk_NxRrU60Znj6dtSKa6-V6Yw3Kjg_Na3DMAnK2MvxwFaFI0vTtImcj2hYMBYotb3sb7dtpDf1vdoGc_kLJVmYEsv7QJwsWorKC7loIBdt5CUC4AqexUSpHjbl4lCpY3BInEE_R7EHqhqC5isOYU3X9JnG80d6l1VLm1rcG7HDakUDhPHQMbCQlRweR77ce_ph3bEOZVaFYl_u6Tr08V7L2Eh3O_jfNG0MgI8Jf6V3MheVUe8cCxUt2jzdcI69MdMK_ForsdsQ9rwop1sqDn0rJC0aEvmhhmGV-eoAcj5hnjge8WDsgjQOJf7odhOYbYxOmCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
گل‌بخودی فوق‌العاده سمی و البته زیبا آداما ترائوره بازیکن دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105663" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105662">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goYShbd0i63-boUiLoRnZ8pZWYpYcHDr73p4VIx5gjvebq3PJoRmne7pjyRqhBuSql3FGsdDWJ4f5sfCiDg4TseVBXsf6CjiTj-MsSAdNSqWtVvGlpRhpKNj8xelriRUaf-GGyT0iqZ5jx-bF7dK8rIkb_edcaB1dy2NaUT7Fh9th0Oi7jZ96bC-N_xaslfb1zpNxv6osey-gkpgq1FCJTfu80feiWEUlaUZc_wf0Ve8O0xuXf76uBB-50Z_aqKci6kagUDjFkLtvmWyOmOgx3tqlIh7t3a3ZlWdH9Muy0EOnC1a1IW8icCR_6iVUAuQ-iVgcYzrx6eRQyc4gmE6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
فرشته کریمی، ستاره سابق تیم فوتسال ایران، به تیم فوتبال زنان پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105662" target="_blank">📅 10:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105661">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff10f908a.mp4?token=n-WLCp6RtchKvLGfwSDKMaJ60dSZVnGxBCZFxSjee2H8oRlrd3kjaAre36jPRDeJpN9kSh8uc8z-4szFLvvERh4KChAM_a5B-k4cw1P2NA_wcH_2gfedsZHZJjHWVSI6LDKg8sISFf91WnwiTD1DN_QPzUiScLYw6leY_lCF2gvrIhLjCqwnsOTl4mCoFN05v79ixWrqynU7Dnwo2YDTSJLNwKi4qwQ6cgpZyTDOQjExuXriNWJMs27JZmnKHDDlp2EDONTkStelR1VeFMaXlpqqO36rMIGzPGy1pzNjNlPGEKYhN68SIBMrQw1ozQH8X09ljm4a8cFg2mi8WhFbHYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff10f908a.mp4?token=n-WLCp6RtchKvLGfwSDKMaJ60dSZVnGxBCZFxSjee2H8oRlrd3kjaAre36jPRDeJpN9kSh8uc8z-4szFLvvERh4KChAM_a5B-k4cw1P2NA_wcH_2gfedsZHZJjHWVSI6LDKg8sISFf91WnwiTD1DN_QPzUiScLYw6leY_lCF2gvrIhLjCqwnsOTl4mCoFN05v79ixWrqynU7Dnwo2YDTSJLNwKi4qwQ6cgpZyTDOQjExuXriNWJMs27JZmnKHDDlp2EDONTkStelR1VeFMaXlpqqO36rMIGzPGy1pzNjNlPGEKYhN68SIBMrQw1ozQH8X09ljm4a8cFg2mi8WhFbHYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی گلر‌ها وسط بازی حواس‌پرت میشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105661" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105660">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cec5d5803.mp4?token=FeZzGvU8i47siTJhkvTRRgroyNwNU5Kb3n9sbSai_Zs9MiPYQH1LgmiLjO3hUKtBMGVsrD-XetEYNQ65kFCyrs-RtNkh6Zyhzozf7WjfSwrE8puP4S2COptvSOewGzhtCGzWP7RSF5ZysRcPQwmDQ4CqETo71qXtXtJsRVVhLvGWWcG-s5XY7pNA2t1znkAvN3S3lmO7H05xpg2sgHhh4atfv7zPvq6gx04Q33T4Kd-usp8e6Z4d2FH5DP54L-JXYKjVEJSDEz9lxvvmf7WX8H-kEiziYb6MseRzTNyNBU_UbSV7Z0yIhOrJ7rqbB7AZbOBRYURV8nBmzE07FA9hhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cec5d5803.mp4?token=FeZzGvU8i47siTJhkvTRRgroyNwNU5Kb3n9sbSai_Zs9MiPYQH1LgmiLjO3hUKtBMGVsrD-XetEYNQ65kFCyrs-RtNkh6Zyhzozf7WjfSwrE8puP4S2COptvSOewGzhtCGzWP7RSF5ZysRcPQwmDQ4CqETo71qXtXtJsRVVhLvGWWcG-s5XY7pNA2t1znkAvN3S3lmO7H05xpg2sgHhh4atfv7zPvq6gx04Q33T4Kd-usp8e6Z4d2FH5DP54L-JXYKjVEJSDEz9lxvvmf7WX8H-kEiziYb6MseRzTNyNBU_UbSV7Z0yIhOrJ7rqbB7AZbOBRYURV8nBmzE07FA9hhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رفقای باسکی، رقبای لندنی⁣؛ دیدار غیردوستانه‌ی آرسنال - چلسی، امشب ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105660" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105659">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjgriy3Pc_lpynklE6uTbCEca6UuDs4sFk6V873WeqT7sDQEjM3ue3ftbH_3bo6Es_jhw269nFHXvrVY1Po2bqUgJ_-EeE06ZHTEXdW2JyYv8a1ncV-6FFLkEFkGSAHovOZF2x-yccEdIa9hA-t0teQ_iMHKkCAQQ6K1CLrZU8ah0j0vqTAYiqCueZVN74hqsaOfYwZwcu1gyUy62oGrCyue6cQdMRKldE89tsZQr5ly77wb-fi0hu5qdEmiv3iNqNcQAhI69DlVBDt1JfcAkUbiBg5NaxfyjVMDUgxRZ-yYzxzSRMf2bEDPp_RVoAMZbFVcwTXG3f1bbChxEbX8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚑
تصویر دلخراش؛ مصدومیت فوق‌العاده شدید ایوب‌الکعبی بازیکن المپیاکوس یونان در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105659" target="_blank">📅 09:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105658">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3abb5b4d2.mp4?token=r7SMBz7XtvmRMG--2xgqXXPWJsJ0Bj1dXOQJ3DSNFVKrEOlGP9WUQzJHBBZD2vRXQGJilqcVB014fesaAUoCeutNIbRtfMWHjiXL0Rf5PkcF2Xd9I6isJ6BWPYFUD3YfVzPAlstRAfZwdeXDmF6-iySV9uyVwjLAmIMq_GKDUN89RtN1mJQWBhwiqrrw1IBef-aI5ffBch7xEzuKQTz4KJOcoYhrd7Zhafk-_xf-m6e8f8QI6YvruFHAG4OJBfMhYsDjnfCTA4bvMsIB2ysF1r_PINkNVBu7JZhFqbpCfRgZuG7xePLi-2CwlA64E8mU1KVWh9pH58Gs1-cKVJwNDyQP8SK4zc-KgwkzBUVQZzV_1id3sgWZQ3vda3hsOigQVTrE6ESObQPOzBcR2Mn-gWBCmbN6Cj3X9Sojc9B5gDCPj1_tvGRnVfMG3fu3jt-FQiTcKdUv8M21aBfU2twSfc4xJ95XaclzAuP3ddObWvQuwPrAFDpBV1ELjWuTiVl0yMEnD1W_rM6QBDlYF8pBA916ay7hGe0LrD_cGWlyrLJP8OJPMKgdFGJ9OCz4KLQIS2_04WFOlRBNQwFnEbVd2mwTNB4f_gOoyt3iGxDbiQpwdQN-1CmaD7MH_hWaG00i4176auui7So0nUJrGd9aGfgjcxmQOgjbnI9GKtS7q9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3abb5b4d2.mp4?token=r7SMBz7XtvmRMG--2xgqXXPWJsJ0Bj1dXOQJ3DSNFVKrEOlGP9WUQzJHBBZD2vRXQGJilqcVB014fesaAUoCeutNIbRtfMWHjiXL0Rf5PkcF2Xd9I6isJ6BWPYFUD3YfVzPAlstRAfZwdeXDmF6-iySV9uyVwjLAmIMq_GKDUN89RtN1mJQWBhwiqrrw1IBef-aI5ffBch7xEzuKQTz4KJOcoYhrd7Zhafk-_xf-m6e8f8QI6YvruFHAG4OJBfMhYsDjnfCTA4bvMsIB2ysF1r_PINkNVBu7JZhFqbpCfRgZuG7xePLi-2CwlA64E8mU1KVWh9pH58Gs1-cKVJwNDyQP8SK4zc-KgwkzBUVQZzV_1id3sgWZQ3vda3hsOigQVTrE6ESObQPOzBcR2Mn-gWBCmbN6Cj3X9Sojc9B5gDCPj1_tvGRnVfMG3fu3jt-FQiTcKdUv8M21aBfU2twSfc4xJ95XaclzAuP3ddObWvQuwPrAFDpBV1ELjWuTiVl0yMEnD1W_rM6QBDlYF8pBA916ay7hGe0LrD_cGWlyrLJP8OJPMKgdFGJ9OCz4KLQIS2_04WFOlRBNQwFnEbVd2mwTNB4f_gOoyt3iGxDbiQpwdQN-1CmaD7MH_hWaG00i4176auui7So0nUJrGd9aGfgjcxmQOgjbnI9GKtS7q9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
مهدی رحمتی پس از سومین شکست
:
🔴
برای گرفتن سه امتیاز تنها تیم بستن، بازیکن داشتن و تمرین کردن کافی نیست و باید کارهای دیگری هم انجام بدهید که از توان و اختیار من خارج است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105658" target="_blank">📅 09:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105657">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/Futball180TV/105657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🚫
خداداد عزیزی:
اره عالیشاه بهم فحش داد منم جوابش با فحش دادم
با شجاعت میگم بله من فحش دادم و کار خوبی کردم
قبل بازی رفتم لیدر هارو جمع کردم به بازیکن های حریف فحش ندن اما کار اشتباهی کردم
باید میگفتم به بازیکنا هرچی دلشون میخواد بگن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105657" target="_blank">📅 08:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105656">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41325b7826.mp4?token=urArk6yVAqzUbw9TanR-fUjQQcUs_NejU2G2TwTL4I0kazmituAYMovUu6UNr6yv-iFb98L8wU6aRL_nScWa6fJjxDsTCLIkbwLcPgAs8TOL3vvq30nbsDwbfqX9khTtsKVHI72psVrLqlzzS8oyBZJt6jWbhCBHTMpDG2rPagU8FlhKvaa_BoKuqDTCEjEUxwwfwBTMPXl06OBNAh-ssfrCBLvn7v2UpPxu9YFDZBkaTqJzM8SeiwovI7A3jY9glO8hJWIFPppfa9cW1aa72x5gh71SbrP6HmU0X7wtpr0Tsw-asyf-H9QiQhjbEcWpzyJDp7BHkZcg0fCC10bt5wajHqYWs-azONy2o3Epuf1IL-qbSYEC990ugTIUSRI11yoyz0vejj0zdpRET7QON_1nMBjdFxmrP1FNObGqVY6c3OOimDDRUN5DahOmBlGFBxpMkAf75vFoX7VaUtK6Zx2-jzZvtjDKxBwSYcV5RbJcGGz9k8owBcfeBFNG9bG29Mc634yLCCrMpisu6fYHyWfJSZLto3h-j6ElkLjMOig961GoJWw2Fohmco1IjM_uFQL_8KBvPgSCG-KOACJPeEfaLudfxgSu5STKNcwT6EhA8Fw2xdO9UAwHwzgfJSCv3fUD8aHfI2kW--t18oYH30AjMTNd84GPKh0GQfmi8ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41325b7826.mp4?token=urArk6yVAqzUbw9TanR-fUjQQcUs_NejU2G2TwTL4I0kazmituAYMovUu6UNr6yv-iFb98L8wU6aRL_nScWa6fJjxDsTCLIkbwLcPgAs8TOL3vvq30nbsDwbfqX9khTtsKVHI72psVrLqlzzS8oyBZJt6jWbhCBHTMpDG2rPagU8FlhKvaa_BoKuqDTCEjEUxwwfwBTMPXl06OBNAh-ssfrCBLvn7v2UpPxu9YFDZBkaTqJzM8SeiwovI7A3jY9glO8hJWIFPppfa9cW1aa72x5gh71SbrP6HmU0X7wtpr0Tsw-asyf-H9QiQhjbEcWpzyJDp7BHkZcg0fCC10bt5wajHqYWs-azONy2o3Epuf1IL-qbSYEC990ugTIUSRI11yoyz0vejj0zdpRET7QON_1nMBjdFxmrP1FNObGqVY6c3OOimDDRUN5DahOmBlGFBxpMkAf75vFoX7VaUtK6Zx2-jzZvtjDKxBwSYcV5RbJcGGz9k8owBcfeBFNG9bG29Mc634yLCCrMpisu6fYHyWfJSZLto3h-j6ElkLjMOig961GoJWw2Fohmco1IjM_uFQL_8KBvPgSCG-KOACJPeEfaLudfxgSu5STKNcwT6EhA8Fw2xdO9UAwHwzgfJSCv3fUD8aHfI2kW--t18oYH30AjMTNd84GPKh0GQfmi8ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⛔️
‼️
خداداد-عالیشاه؛ جدیدترین دیس‌ و دیس‌بک ایران؛ رجزخوانی بر سر کارنامه و سابقه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105656" target="_blank">📅 08:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105653">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105653" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dff4d583.mp4?token=NgJrn0cPcwkVU0GkzDG4IctAEu83OYlR3ECqC2Kd5GCAqHYGMgrBE760qLokqpcCauwZcG1DOsUEyte5fewEM-xi8xJbMhocuWNOPaKgdBPrkvTxPeMG8_GsYGMgNiZ9_0c-2valf_QZKB4GsJkleHnbTsC4GlaKvbKWwxohSeAbAzx7mmtLsRnyD2muTCfHoXYvg0Sw-6cYj-9ewh-RAESe2xS35xK-ogrw5sZZRMJmE0BqvgcdHue3_7sMpOelf1slDYb7t5rgd_Mnr02UQHOkZ9SfSmcJsGyG7EOgGuAO9PvD-IJO_wLRoaYVTBiPemDjhbBJw3UkdqUDvYnUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dff4d583.mp4?token=NgJrn0cPcwkVU0GkzDG4IctAEu83OYlR3ECqC2Kd5GCAqHYGMgrBE760qLokqpcCauwZcG1DOsUEyte5fewEM-xi8xJbMhocuWNOPaKgdBPrkvTxPeMG8_GsYGMgNiZ9_0c-2valf_QZKB4GsJkleHnbTsC4GlaKvbKWwxohSeAbAzx7mmtLsRnyD2muTCfHoXYvg0Sw-6cYj-9ewh-RAESe2xS35xK-ogrw5sZZRMJmE0BqvgcdHue3_7sMpOelf1slDYb7t5rgd_Mnr02UQHOkZ9SfSmcJsGyG7EOgGuAO9PvD-IJO_wLRoaYVTBiPemDjhbBJw3UkdqUDvYnUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚫
اوه‌اوه لحظه‌ای که خداداد عزیزی به داور بازی میگه کصکش
😕
😕
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105652" target="_blank">📅 01:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b7a4758e.mp4?token=sEqYq9QvYEUN1j0QP12BMRGv9XObYgHEVLvwP23ZCX0b1tyEoPlRNtCBk4IEhjZLsizaWIknPZgYDuNK4yYX3PV2CfcmFCUAwRcpgXCr3LVYFrwzsnyOce88G7JrvDD1KRV0OizwTJkEa0HnOhcyvgoLYL28c3anFYKHvb6OCQ7dYeuGODmTRvb7MpztM1alxpcCpFuh3P9mnhz9S4aU9V5hv0v76Cu7ORZyxdOSFAeZFB-_cINLMylo6wcGnlIjo8zok8-BHtl0hGvNtPxVrWJH-JE50SHCWfzmQeSndlrPy4fb3G6sE9vzhx8V_yG3xO9DeADX03xdoLPW1TkkgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b7a4758e.mp4?token=sEqYq9QvYEUN1j0QP12BMRGv9XObYgHEVLvwP23ZCX0b1tyEoPlRNtCBk4IEhjZLsizaWIknPZgYDuNK4yYX3PV2CfcmFCUAwRcpgXCr3LVYFrwzsnyOce88G7JrvDD1KRV0OizwTJkEa0HnOhcyvgoLYL28c3anFYKHvb6OCQ7dYeuGODmTRvb7MpztM1alxpcCpFuh3P9mnhz9S4aU9V5hv0v76Cu7ORZyxdOSFAeZFB-_cINLMylo6wcGnlIjo8zok8-BHtl0hGvNtPxVrWJH-JE50SHCWfzmQeSndlrPy4fb3G6sE9vzhx8V_yG3xO9DeADX03xdoLPW1TkkgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
🇮🇷
واکنش محمدرضا تقیون، مدیر روابط‌عمومی هیأت فوتبال تبریز، به ادعای گل‌گهری‌ها: فحاشی صورت نگرفت، مدرک دارید رو کنید
!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105651" target="_blank">📅 00:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=tdNFjb31zLaB01VrOuxuXkbcmYK4BhxCo8iJHEUzguLpSp_81HqExWm9mXTA3nXVONvJLUSg8ErHMiagqBe-VTNSPrPAqL6TQdvasnmVQro5-1cpl4hKrvBIEifDlxKgAj5r9sAgq7S0Bs87lq8gaxEDP3_Cg47JKCHUuSBcxlhmpZjMjaCrtfktTL8YVdX-WBzIGxWGR3cNz6iOtEcxf84DhOKCouKqkOPshlXdrdiSzlvwEPzRRXiezxavaOz32aJjBIhQ8YtkBnHRUzIrehb1jfZfoVQPpT6FlQ9S0QhEl0Ee8T6f6rqwsjIUf-lpfPJvmszZGXpTzSKJnMt9KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=tdNFjb31zLaB01VrOuxuXkbcmYK4BhxCo8iJHEUzguLpSp_81HqExWm9mXTA3nXVONvJLUSg8ErHMiagqBe-VTNSPrPAqL6TQdvasnmVQro5-1cpl4hKrvBIEifDlxKgAj5r9sAgq7S0Bs87lq8gaxEDP3_Cg47JKCHUuSBcxlhmpZjMjaCrtfktTL8YVdX-WBzIGxWGR3cNz6iOtEcxf84DhOKCouKqkOPshlXdrdiSzlvwEPzRRXiezxavaOz32aJjBIhQ8YtkBnHRUzIrehb1jfZfoVQPpT6FlQ9S0QhEl0Ee8T6f6rqwsjIUf-lpfPJvmszZGXpTzSKJnMt9KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/105649" target="_blank">📅 00:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArWr--WdKHkE2sD2RVrrWjDYgR-FTt_YQRVRno6wMDDEJuzHuuT3uOUAJFkuu5L4PX0DOo1FBYQDCBq99urZPD3cODju5hkA2EVXXJfQMNj-UVhPu2RAu3TOfrDHI7ttLPS4zSZEx5zU5gSm8CtbeRTKu4GCU__Y5WaN74YEsicHkzphYcqVL_0m-0g0tE2zo-xTOO04mbgclrMX_byKXzXIONcdrooB3H_rDWB82FmUBB8EY6iRcw5WtQX-izATPMCBAE7Y53EWZnrUoViTk21gsGitv4wQOlP9BP_Fi3PXNhF54cRmTf0KopYSkHEXdr669Yq__Z5o1dofU-9GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
💥
اوبامیانگ در این فصل از لالیگا:
📊
👀
4 بازی
؛
4 گل و 2 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105648" target="_blank">📅 00:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105646">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو از پشت چسبیده به دفاع حریف تا تاکتیکی که مربیشون داده رو ببینه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105646" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105645">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه گل گهر با انتشار‌ این ویدیو نوشت: دو صحنه مشابه با دو برخورد متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/105645" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105644">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با انتشار این ویدیو نوشت:
خطای شدید امید عالیشاه روی پای امیرحسین حسین‌زاده در شرایطی رخ داد که بازیکن گل‌گهر پیش از این یک کارت زرد دریافت کرده بود و با توجه به شدت خطا، می‌بایست با دریافت کارت زرد دوم از زمین مسابقه اخراج می‌شد؛ اما متأسفانه داور از این صحنه نیز به‌سادگی عبور کرد.
در ادامه، خداداد عزیزی، مدیر تیم تراکتور، که نسبت به این تصمیم داوری معترض بود، با تصمیم داور از کنار زمین اخراج شد؛ اتفاقی که در نوع خود قابل تأمل است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105644" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105643">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
مهار شوت سنگین رونالدو توسط رایکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/105643" target="_blank">📅 22:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105642">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🐐
به پرواز درآمدن کریستیانو رونالدو برای انجام حرکت آکروباتیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105642" target="_blank">📅 22:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105641">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حمله شدید امید عالیشاه به خداداد عزیزی: خدا را شکر سابقه ملی ندارم. من نون بازومو می‌خورم
🔵
بزرگتر از شما هم نمی‌تونه اونجوری صحبت کنه. داور سر تیم را برید، گل تراکتور قطعا خطا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/105641" target="_blank">📅 22:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fes7krtB-XoqFR7HVJaeSGqYmgqumnHDDLqfrsGDcBFVXApxOQlxtmqjk9Emg09VyJCrfr-aly4_tqvm7ntpLA0wQ9P787grF3OhFTRt0a9qKpuEwyGB6zyvyufmA6WnVpLfCXL_jsEkcByjCiB-xPS60pJRWEzgQNFBq09_6hGqmrjlX5TE16TTKtLN4KvUinjr_yPY5-pxtjwxltVzAkLUUsa1yh8eBwh9BA4-tARr846TKFxlkgmTEmPC0gn3C-C0T_4Nk8ZUbO5G89IjpJ0GlNyQIHm8aTGw9A3V6M7aBMeASEriCmgXPYk2BmnUCDuR3Tl3ifDsUJxDY5T6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
محمد عمری بازیکن پرسپولیس بدلیل کشیدگی رباط زانو حداقل یکماه غایب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/105640" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=MnKuR7KdJMGcjbOw0ru69h5SMFCGup6O0nOuGH0406DiS3u4NgXHWtR2Y5R6YaOiNhmTv6v0Al_O4siN1WJBTfdJs3Ql5u-ffl4VBk1Lo7n0EwdF6zU2CF-uLfildOBA9eSZ-v_SUB_btmoELBFcMul2TsXYmDsQ6s-oQ8VX6HvBNoClgLkX4xc8wENPkCl2uIxyhuIeSL-hqephZ9Kwb68VUHTPLEgUC0hPCpAJtqScybjw-G2-yx6aQEh0p2tRUBrE2kbobMqTGTKp4_DPXCnQynEUeNwf0CJQzO8qvcdMBeCZy_y70OzqgTkJDcgY5KMCafXqYxH5TqDmOakuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=MnKuR7KdJMGcjbOw0ru69h5SMFCGup6O0nOuGH0406DiS3u4NgXHWtR2Y5R6YaOiNhmTv6v0Al_O4siN1WJBTfdJs3Ql5u-ffl4VBk1Lo7n0EwdF6zU2CF-uLfildOBA9eSZ-v_SUB_btmoELBFcMul2TsXYmDsQ6s-oQ8VX6HvBNoClgLkX4xc8wENPkCl2uIxyhuIeSL-hqephZ9Kwb68VUHTPLEgUC0hPCpAJtqScybjw-G2-yx6aQEh0p2tRUBrE2kbobMqTGTKp4_DPXCnQynEUeNwf0CJQzO8qvcdMBeCZy_y70OzqgTkJDcgY5KMCafXqYxH5TqDmOakuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت‌کریمی، مدیر عامل تراکتور: از آقای تاج درخواست داریم ستادی که علیه داوری بازی‌های تراکتور تشکیل شده است را پیگیری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105639" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105638">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWFOPnxA2EC4r2PupsxxqySXxLLJsWYC-2kY0YEKxzih3c4yeAocwKsOFCAbmSjd04vGLZBA_MXRx-EN5Lz_zUVLae3NpNo5DXWKaURIz27mTeBBHqitfWzUIsGiCVPCDdL-Y38vnE_nD2zt98v8VF8fkXnbIwil7Dpm8YOY-b16AU8-osoGfYgeToyav82f8IE1OzYBtg9QIkuPjaOs0rWVd90AUDVGNsyg1ZJnKLM3udcCc75ZDoyYBtjm3JjrByuQ_u_yJ95NWswZQMBAEhgZ-OCyx5fSX0ZMlSVyT_trqmtSWK9LhIFvk3l00uRK5r2iWTLU942zUMHsmMyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئالیا خایه کنید که سه‌شنبه قراره با اینتر بازی کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105638" target="_blank">📅 21:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ffHm8eDwE6KH3blBsKX6sXDpea1fdp3EaTVLyxvXWso2n3O26mZC6LzpxwJRuxhsiYAfPC_fpOYC4rgL_pfa8QPz6RNu4D3oUQeB8XfrEm7aqhUDnGJy5DoJNaKXtJES2BVu89nK6oEFusCOKTCB9kJA8yOzgmh1AHqOy6ahUn5mSZubyywKJaXLfT3tp2ryFqrYOkgtJkh8MYi7m_WEfuj5dgNHe3AiR30BwvWxLshg8qljsG4gCybD0s2km1LgIKqpJyJOKIomYz_O9rJ6ToTaEOmQwmlfNyCF4deewDv7rtVvE1Nnqx5fNCkRaf8PkYVe9_OZdjlicGn_vSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105636" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105634" target="_blank">📅 21:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=lkklSnV0gPG_cx4R_CkqEQmVQ0TMWIowrNcwrxiwIplBlmdDOzop2eaUI0iTbv3o_5T1mJME9FBK-xpV6ipR2_9XO53NfGBsp2F04rssuHTl6owhf8ELfdxHqjNJ7X7oSZlphh2P6Smk409BN1QXTV5AA6IaRuc8J_69bPhL7X-LI7eBLkyRlvnNdrV9jZQZn5LGlXbeHZRO9DpYmVq--iZpmw2VvhzKIMHYdHAQGJ3dMlzjtAjtjWyAmnPgo_PLIwdo8onrkunKJlUZwnN5EVx7AIVTTjRAG_o0VsK1i4e1NSkknsOQ-jp-rp_6hvGUrx-zyItHA10lgL__6428jUmrPWKzTbLJuX7IyhSa7ACLDTV9Q-vA26egNju9DOB6bxoumQ_gPWAC3o7pK8YVaEftB3bOUBiOYeYz21e9AzGvRC6WTNnfRcLbFYtdAhbicBZqxAq8HxYmBZ51kRd6XbfWUvhXC5GL4fel0ckY69705ZKEU5PZOnaN2tWgPzWpdrdsYfejX_SD8D3H6KcVTRG5W3Ps9G6Z_94TWrYRfsi2_NpxrKeapy2TLjo8QNTuUzz5jYIgyxXPodubPsCwrRkvHgMFoUpZIVxPNohnVcVQhvB089yU-xRqPjldQy1mZHc2Z40hhzk54w62RByBent_VvRlr6RCr7qnaFcXBgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=lkklSnV0gPG_cx4R_CkqEQmVQ0TMWIowrNcwrxiwIplBlmdDOzop2eaUI0iTbv3o_5T1mJME9FBK-xpV6ipR2_9XO53NfGBsp2F04rssuHTl6owhf8ELfdxHqjNJ7X7oSZlphh2P6Smk409BN1QXTV5AA6IaRuc8J_69bPhL7X-LI7eBLkyRlvnNdrV9jZQZn5LGlXbeHZRO9DpYmVq--iZpmw2VvhzKIMHYdHAQGJ3dMlzjtAjtjWyAmnPgo_PLIwdo8onrkunKJlUZwnN5EVx7AIVTTjRAG_o0VsK1i4e1NSkknsOQ-jp-rp_6hvGUrx-zyItHA10lgL__6428jUmrPWKzTbLJuX7IyhSa7ACLDTV9Q-vA26egNju9DOB6bxoumQ_gPWAC3o7pK8YVaEftB3bOUBiOYeYz21e9AzGvRC6WTNnfRcLbFYtdAhbicBZqxAq8HxYmBZ51kRd6XbfWUvhXC5GL4fel0ckY69705ZKEU5PZOnaN2tWgPzWpdrdsYfejX_SD8D3H6KcVTRG5W3Ps9G6Z_94TWrYRfsi2_NpxrKeapy2TLjo8QNTuUzz5jYIgyxXPodubPsCwrRkvHgMFoUpZIVxPNohnVcVQhvB089yU-xRqPjldQy1mZHc2Z40hhzk54w62RByBent_VvRlr6RCr7qnaFcXBgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
صحبت‌های جنجالی علیه عالیشاه؛
خداداد عزیزی: او اصلا در حد من نیست
🔴
بیاید بگوید کجا بازی کرده است؟!
🔴
اگر یک بازی ملی داشت بیاد صحبت کنیم
🔴
این همه مربی آمدند رفتند هیچکس تو را نخواست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105633" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105629">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAbTPwfEKNO_qi93wP2eauTwKOh3VzI3XH8vvN-k5WAfSvtqAHV8eTTMczMHsmSn-spJ6El8IA9o7bIMLHxn03g5dSNmKpA3oCextlD2xYevRwDzGr3P47K_kU6H1Rpe9jwurY0hyv_jURW5lyG-Yu6vATpunul3tY5F8_E458sJJ7YJL1XlesvSavpofgIilzYfE67SlI5OZN-Z_KyNsfOqVwlMm3bGkY-eKx8FzXIX_LrW4uyg89geiYAhzOuyjIUDKesTn78P4Rm1UvHQrh8D27EhryoRAbdYSZkPveOazgiWUwhmksGNWAaCGJj5ZKaopLBA5NLxkiQnIhIQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105629" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=O_k5Veo7VuxrWE7DwrN3pxHzJzSihKbysLik4zOfxaeIu2Qw5YrtwX5hnmYFxibx3daJy41EH97VIwN138ZT_WN1hSDpfJEwMgOMFwDgmuRQT-1Tzx5jk9NUNPaP_t559EXIcowRiSvaS90Cvt0fhX4b1BlOe4WQscCFY0ttYG8GXTqKeYNxRQ1uSsEheAPmWDgXYxufSpQ-j6iTSuc-Ap2YzrpaLN23DpqsrHiQVRnVJNHwJUt-pnb1ccq1_ItW0jfxi3yU3hxcH-ni-rzhUVXh6Osx_jA6JRjZHO7S6C3NFemqWVHE25GcEqARgRT9PxdfhH3x8Mkz6J5u72OI6HZIkLJJfYCBZXuLb16nzqAuNl7LjR5-POFDNmxUOBfjSpwaDfRGNg7tIyd7X3x_U6h6bfZJ3p1v8AseINdywzMIqOVXlKIagIbZ6mhYQ4meryLxPo94kzomqhr0PnFS8jYdb-2WrCOcJc7F1NMQ5R6hJThyuOiCBLPUilo1pDmhfM7QzGOnZRutfU_t6xa4rhtXOMxzqL5D4DixxT91J1rWja3T2E8n1CTWIxfk9moNh-1uenKWEWo2GKKksP7G0WsB3H_LISPTBAnOcgLdw2Sz2EGMnqJDuixIYPd_d-1PHdfjwbAPblKNNAT4aqzqoDv8lERmi60o7A2RMVEmts0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=O_k5Veo7VuxrWE7DwrN3pxHzJzSihKbysLik4zOfxaeIu2Qw5YrtwX5hnmYFxibx3daJy41EH97VIwN138ZT_WN1hSDpfJEwMgOMFwDgmuRQT-1Tzx5jk9NUNPaP_t559EXIcowRiSvaS90Cvt0fhX4b1BlOe4WQscCFY0ttYG8GXTqKeYNxRQ1uSsEheAPmWDgXYxufSpQ-j6iTSuc-Ap2YzrpaLN23DpqsrHiQVRnVJNHwJUt-pnb1ccq1_ItW0jfxi3yU3hxcH-ni-rzhUVXh6Osx_jA6JRjZHO7S6C3NFemqWVHE25GcEqARgRT9PxdfhH3x8Mkz6J5u72OI6HZIkLJJfYCBZXuLb16nzqAuNl7LjR5-POFDNmxUOBfjSpwaDfRGNg7tIyd7X3x_U6h6bfZJ3p1v8AseINdywzMIqOVXlKIagIbZ6mhYQ4meryLxPo94kzomqhr0PnFS8jYdb-2WrCOcJc7F1NMQ5R6hJThyuOiCBLPUilo1pDmhfM7QzGOnZRutfU_t6xa4rhtXOMxzqL5D4DixxT91J1rWja3T2E8n1CTWIxfk9moNh-1uenKWEWo2GKKksP7G0WsB3H_LISPTBAnOcgLdw2Sz2EGMnqJDuixIYPd_d-1PHdfjwbAPblKNNAT4aqzqoDv8lERmi60o7A2RMVEmts0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
🇮🇷
سهراب
بختیاری‌زاده با کنایه به صالح حردانی: کاپیتان دوم ما باید یادش باشد که زمانی ناصر حجازی، پورحیدری، شاهین بیانی و زرینچه کاپیتان استقلال بوده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105628" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105627" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105626" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClI9UNaWWcspWqfDFaAwCBaFAueP-LniRka81FqNFKkTfS-qiU8DoWospncfO1W32rygDx-sqjDLpIIu2dVvQJOg2ZwhP5Zty_yF6erxqKYJ18mNVZ9Qp3uHO8wUSNVNLq9OYmEKYED9KzLLdGzvlKUtVFN1BcO7SSQLLzLBb7jeTqSHBcZX9ysj8tJx1B36EV0NM0e25Uprufi66enhjHW8T4dN5qad0W7852zAjZ2VMLOwWwOXin3r4lC5yfE0ELAY5xTSdgucriVhxwRGtDKskQ-DvtdQcw3VehYbXZJnpzAdETUzcMnFxeId7NnA4TS2bL31k0XVjVGlyn2Lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
ترکیب النصر مقابل الاتحاد با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105625" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq64SABdwH432jSMNf8EPOS-GOcbnlW8xouMg6c-AA2k6m63tUvjy7Rdll8pRhWXoGw7snxR2z00hv1z3P3DwmTy7WLYDmHPEC9ejnDBaloclkw-CNobAPaiqDZcBnnxXtd5mYuloQg7Y3ZmWgVNrekIchZK4qvQoYFVQEdr8PHpQHNl0-g0z44MSNArDJBXQ_xJX_7ZbrhwJHLvwKuri54LGuZMHuMH4RgaHb6iF6a2wqvKIX3_jzkBqjuuPthDXq9vG11hqbhTotFZJZZg9f5dmhhQoBVuYPS9n3Yzpor_6Pd40y5V0OSkw3Azk8Zq-3U3OXJKRRpkxCKY2iwVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم لیگ‌برتر؛ پنجمین برد نکونام اینبار مقابل همبازی سابقش رحمتی؛ تراکتور با تک‌گل جنجالی امیرحسین حسین‌زاده در اوج باقی‌ماند!
🇮🇷
تراکتور
😃
-
😏
گل‌گهر سیرجان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105624" target="_blank">📅 20:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2yWil7qi-zkcx5OOJk1pXCCVoIuRQlTwdKg98KIFh27nfsV2nHDLKM-GNc479606yO0BEZB4nyoj4PegFLwP1dDbYVK12ROFhU6IaQxPDX1m819szLogRhMI-psKbOL47KrI4IMNuNEBFJErIASeZtWeGQ6zHxDTxA06oZZtoHSNYNfAPOAEp8kgWIDCZorp7XOoLPEby9MsIWO_PsWa-e4fLLfjiKCnmCAPj97kyQfjb8oA1QZDZQ-CufDqqYqgEYToiotm72M6oApMXibtIQ37_4zxsp9cxyae6d-JPT8bJ5D_X2iiLd8ApkIFwrNE2xz_taMHvFlfdCGAWJfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105623" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU-rovc1Pf3Hu6VL4iUIIJCKrevuSPMxCICQQA4vwdC7eDhNUv64q4G0FXz3md6k6whRiBRygYcWEl50nOexXPwB-XapL16C_ZcTZOTfs0diwuMVjs7eQunQ35zDp9qhlXsYkgXciU_M7FEbj6J1XlhdrPdWKD9S3e-xOHj-4BNPmux1aNZ_4Db4LXcVkc095kilByrNtK1hUdwgEBC6cDnS2MMoSXB4mzelOUJJekNOK3ErnVgGQS7BsX5c_nXKMqrzVpsoWK-44d5Yas1cnkqiNOMqhHH21U2zZ-crfChmU6axQw8zmF0xVlhVxF1kBH4AOxK5WnrQ-MDf-c8ZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پایان بازی؛
🇪🇸
بیلبائو
😆
-
😏
اتلتیکو مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105622" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMCrXNjfsQBZxr_uD5QUEuR8_3r4H5LFVb-yVoKdsb7uK9RH_NgEpiVUbtzLfZLwUbaO7_qCakdfPRxsjfaxRu0uK5obpyk6BaXHTtQbYOfW1uzoqhGwwt6x8Du9ifNBNMs97RuBBuowxaIQeax2GW225jNzDBKz--OJcym8OHehNDxMQLtFZ_8TH79EGmrT3R0QD1gw1Jq23OJX7-dwMS6YAVl1Pgr0ymr050Aaolb4gn_ddYErdKpcp_cwuDm0noTDVX-7NfDhqWYDVC6fEYbR_X9I2ug_Jr9mRWlrRe7oEkTacUHRnMkDy3SyzRJEcVdiDGCer4Zo3Pe-PuO_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105621" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
