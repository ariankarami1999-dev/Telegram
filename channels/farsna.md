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
<img src="https://cdn4.telesco.pe/file/B3xCMfUgM297WjgXcPM9xwlIUwNE29zV6E-1yljg_mk2E0k4Rgm_hx0V0NNPweZS-Q4Wr7l7cHENF74ZZxWtHydIWTBtTeyCYoeat_eRkFJnl29wynAXUIuv5J4wvncj-oi_rTRHVMJpP7jaPoNB1vboItS_FLQJf7yP73OL26OuGG7_WTvpBrq-gh_PwEjf495RaUsU_k8C9MwsJ9ZYBSZ5iQZ2UD37-BwNcowboxButyiv-1GdTI7nP-fDAuPXncY-fgPPX0MUZ8vPvKfNMwMKSsXCS4CyUXtWCA20nkz-DhS0wlnVf3fpHCvqkxRutTAM-JvUL-QKALsUPLAy2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
<hr>

<div class="tg-post" id="msg-464893">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXT9e_tvWQf3wj9iVvplmRiWOIIDGgoVWMmn_OZqcvsycRUfw2079Pm9j4Ri5bhqsujOKHauJS8TS9nBd6ZX-mOHF4Byy1tr8IhFvBEcwkF3wPgMIXatxdKa2kSCcvlVjjmcYutwonwQiWOAS2NwMlzEEDBCkB-xBASD-Ooz5JoP9zQV2SqPrgoKxg-FZjU8YkzA_tJtSwQt7WJN2QpOlD5wGNhjSTrripkBwkrerqQ4-d6_DQZfBnWJ6fO5VX5P7m31EZ1DeYVxPJzfkNwH9pWROEWw3I1IdTH1zQT6qDdnjWHdY7IBYzBqdrtP1xw1lvdc3NevfX94Muu1anasnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farsna/464893" target="_blank">📅 00:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iho83oOXmHIsjGQ4Jagmq8mgMiT3TN6qNSJtLJw0qUhChQPNsl8AjYd36ZPzl79OoMgl3FaJhujYEjkCEXwPIhDEar-eN7NPAKuwnxTMeELG2lB6sz9I85Fa9H61eLSZchG7q4F5_5uSLwjiUFPCxJmOs_RU7X2URQTiTPasvs7g9oKtOgP8jZ38eR4NXx9RpM-9bfsTgeVCPCRmtKm_qY7ekfokW5Nrxbk-71II5qtC0vhiJvM4hTJIaimI8RUhowH5VOc2HBXIpcM3tEhoCW1spSL-Lwu3WY-leSE-9S6TIV-WTPkzuMU9jCc2iKDKXP3U0pwtqV1TSRubZb1r4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVcYOF_cvjAXQY6b23diNYlWoNp463gUiQjv1Ig3Qiit9sUBBXrGiC23hxwkZd-34F7wIXZFq5RxJ26svz8-ZBb7irUaTNC2GsZycniJk9W4AZWAckal5yJtHgiyw9z4LpmRCAY0USxbkqG_8XuNKmJvElNtSePYyh59d289PbhdX4L1WnoG1vnrvuZuEjJkXNttqJe8AuJN-JsNcN-tErIlPoHJM2SSMG1LycdQpNbgcmvo11KN-AcEwnhKQMU0r97-yF1-4-38AcevT65t26XWaC1LyYjS7wkxwqukwSRalhmeX8y5-fTmNlskCtLp6eejZvZ3nf4X_aJgmNoJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR5FHZJFKnalyGXyup2_8YLjs-1ar7U_5I6If7Kepx-qKKOIEvUcL72g0gTJ5Y_mzEpkZ5F7jfcJHCrgAXZAAV-uU2H5ipfXBE53-rG6tHigNfs38cXJOyr1z8-xnhM3fQTpkILii4suJVC3cp8maX-wDAIBcLiSJyoeZGnE2MHUYVeoQ2ElYTSew9REPPUXzBU1e74Nl2C-txdBc9oIkTcH1_FLNe3cmyfQLpx7pfIYqq_tpOFnguo1ztN5N4i037uOD02Rmuh0qoTVP6UivUbuXqyk3G-ch9ce4uX6yeA3NYSOg6_-WvnXafPL8ghxJn-WYDAmMqweEqfzFALtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRr24o0ZaDQjJNPXMQ0N2ec36mA6meJFzqZTDwvnyNChdQ-YxsjkA5YpmF_pP4SaQ-_UWem57rNIMTgRwLFflKW4FFtG7xF3QXsX5LyUYKcHumW0Q4_ELCFtTgH88ijpu6yRCqEWD9tWvoX-4xNlkiS72VFFeh34urY_s8_gWQy_oP1FybMpqmuRLTXcTWsAuThv2I7TzgLHygHZ4GYVbAJK8nbbFKlEFanBEUBqjpbeVmwQmb3dw8FcBJWUz1Q8hQqQqx7FEDndO_xUPRLDLr6Q8-7wvdOUyPv-Ht-OSZjpy0r3tV9B9ZQDbF4u6oUwfRqi78RpslvpRrgPAjICXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyjMzC5PprXgUqi3MlxV3NlIoJM_QEc7f3GUWaG-wadMDpN7xkxcs4wv0k0sNt3YMBEiwRmBb9gsmojELY0KD8COdINrhwlZ6JheiuG-Co0SKYglSEcGvTw9EHR0UpwKPdYKwfLR0gQwUmSeAuD4pqAIaa5HuxrTA3gxDiCSHaNYkN63jCWNQKyBm1dJaVtV8-Z7-qokpTVsQezpXLaa_qfxe66JO9YVpm_NT2ZQmu2JvFGJGhuNitJ3mWzTO9HPpYf-4KRTajuP7q8hOAwhBTOiUfXrY91Nq14NYOLq_Mey2uXUDl9CW13KF1lXdb5I5sdl9GAXf_79uS9bjeWj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTh_PI4AlKh9TQmpcqX0LF6WYq529HxULlVSB7O9SRQ9vUcXBUxB-ZVcRQwC6iT8d-FVYwxWyUCSEt3RSrjcInSv1lpTbzXyJSNIGBvGTAsR44Nu4GTPWKlynoPZVAoApX7wtrZkxagUJWeLK-RoMbPs4LDRnjx6POPQqBrYNIsmECa6uykzS485EkpXVtRCuBUR7WH-pLyP5bCtm_WDM_SIEvabatBbHDtrgvcWPn1WMoKWDyrZFVKBaaDEMZ76tv2hrDxQGNB2B-u_gtLDH93LBT08Y4h_zANd_23j5Ho5xEb69D719ETb9zipNhXfatf5YpWZBLNjKERDohSJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHfZtiAIQzwPBL3bOxERuqqK1e1r2W7KWXOfMTRtLoUUxVs5ye3DE6gLNo_eszKQETnpo8m3_0xKn8wC-KmoKAA7WwDq_lNicqYBNYKqTlPo1_I-WOh6TTuMOZJM0j3glBkrwfuREtpncjqB0afRWQVk6wW_O07kp0ECL7K4BHOzmDt9rKBgTUxNIu4tsy2yTO9djd6pg_9DX5aaJjptel8I4F3jCEHm9tv2ZJn0Pg_UWEI582aLREi4D2-jSli-ogADL7b1RR6fkYddK-QRWL9DgBli2AWXxXKmJJiUv7phfkC4jj2P_DHScdoMMnQ2yzNQWCqhKrVfda6zoKW4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVRRKZZ8VFZF-1OeJpeI_HAYO_GXRxOIuydj5h6LHPORnu1w9lDrOTb8NEr1P_D7KBVksVdjqf0vukDEEf1WGQCmEGYkcKiPvvL-YbBVckG-H-UCouX5IOLHZZ7GdYoPFpujcwKwgZtJ_m-SLzDgXVV9TFemyKZyn8er4b3a-FnelebHxkTvKWRrYd_FbonOMlotMhhrBtZu9lQ2G5SdKMEVGveLLX739Pivncdbyr0yl1JwwcH7Mw95zhIlNqohKAa0B0oBpz5sgCTIJR_mv3NLnkwl4zOIutmGQLoHqx322C0SsZPlC0tXPi3Zqh7yzhF3wayd21rhCWusKm2hQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBQtJ0HgaEuil9ubqs-3rQCDR0oRFtKSE_Kp9DcoOqkXAK7kXY4G7qHUTCy8owc-fHLBvjW2lL4Bk0-iBBGXBAnLJ4i1j4YimmP_9cCQj9HYtGaBnGQF81ZlriQAltd70261ac_8LJg18a4sPvKeej_BW_jANaWtrgIrDhU3fb_EsWz_3iy3Kra1K4rUiYO0H8GMhCWFyHFKj_7YqlH7psbs6ebn_cBSoWzJa44PmMFdEo9aOll6Jq-3RdhilAjYVgdC_Wz_JBAEeyp3XT3QfnASuaJGqQiNFA6p1sHFvZaoP890LQFQ_iGNsj8BdO-tJFkTHLT2vNIOItg9U5WVsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رهبر شهید ایران در قامت پاسداری از وطن
@Farsna</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farsna/464884" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506ad2cc04.mp4?token=dFD-X3majY5cnUc_dixf1tkpslq5v-0gN_Y8ZDsYc28Ezcz6UG4zeYhIErnEHz_1ahN5pinJHWqSjmC59lCK4ZX3L2_Ejm0NomfzpmX8J9i705m7biBoxZCB-FjS6cuwGlD3kRz0Hf4jcUEId7L8GYZPpTIwFyLRg9axeK7d7tsbBgdS3uEJXq2RSeNyAKgsT3TedN_w6bEy8I3I4-JnPsM8WuhtZj0rFAlqfY8Q_FqsxhkuzTuQFupJic4l1IAmXBbsNR2DG_L7b_y_qj6jml7uKXv-CHeTWWnZ-Fr8BARNGhragYq_utMpo87YjHHiFckoK-ORjpPZRHt8HGbp9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506ad2cc04.mp4?token=dFD-X3majY5cnUc_dixf1tkpslq5v-0gN_Y8ZDsYc28Ezcz6UG4zeYhIErnEHz_1ahN5pinJHWqSjmC59lCK4ZX3L2_Ejm0NomfzpmX8J9i705m7biBoxZCB-FjS6cuwGlD3kRz0Hf4jcUEId7L8GYZPpTIwFyLRg9axeK7d7tsbBgdS3uEJXq2RSeNyAKgsT3TedN_w6bEy8I3I4-JnPsM8WuhtZj0rFAlqfY8Q_FqsxhkuzTuQFupJic4l1IAmXBbsNR2DG_L7b_y_qj6jml7uKXv-CHeTWWnZ-Fr8BARNGhragYq_utMpo87YjHHiFckoK-ORjpPZRHt8HGbp9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معنای «لبیک یاحسین(ع)» در نگاه سید مقاومت
@Farsna</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/464883" target="_blank">📅 23:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgrCWH8XDuoJfdAlHqrMmN2DwzWZ4ey8uViIsjeCh-AJLX9KEAZR7_o4Yejfiqn0eU2NbHg8eXlEdNcW_Qj0HZ0ZcDCuU7oRM_qp5G-F0YpObZ1YIiYoRTxPLHOpYc2fXRcVXfKwbYGoLkBzeP5fOrjI3fyPQXB0iXcVDDhzuInFEZBYW5nmLkhhkNtMI64wyJIhk5eKNTGlh_m_9JQYkDU7IPYmyR2tf5U9U8sxxLqpaaBFoZxb7frVT4JAH7dQD4uk7DEiUH01_d-_9Dm7UrLlArIl7wph8yKbVEv_Hvg8GG3a1DYwM71u1lk56OMZZSPJIVFo6vu71FH-yow1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه: تنگه هرمز نه تنها باز نیست، بلکه شکارگاه نیروی دریایی سپاه برای زیرسطحی‌های آمریکایی است
🔹
دومین شکار هم صید شد، این‌بار Mk 18 Mod 2 Kingfish؛ یک AUV پیشرفته، خودمختار، مجهز به سونار و ناوبری دقیق و با ارزش چند میلیون‌ دلاری.
این فقط یک شکار نیست؛ غنیمت اطلاعاتی است.
@Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/464882" target="_blank">📅 23:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464873">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQt6VgUFXKKimnKCQdkIAC_PKnOfdDPd7SXL4N9Faedwp7botIQis4eXlB3U1fNFwBmNJ9ibizLtCuyXcTaLb52xSdCz3EV94UfInNR9bRHerKEYiFb55TLN6VPPzrEjVLyLAwa7exxWw9OjZ5FgnV2wWfk1PBLmFCA5S8OSaGIvgqMqjohH_6lubaKcnkLYtQF_ORhCeNHioNt2DjQR30Ju2mt9bBttZIk0ZrCEqEd-A8uN0ficyaNvdbd_rP091-nVluQe4mfTL5xC8X4zaoQYr6wkwu3PO0Ol63a3lYaFIv8HSNFByGBjOTfrx0gvqY9Uz9Ct7no413DyWcDWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR0lTI5m7AcqyNNFjlixF4Y_8uohWaPjJtTIoCg7ZKFS1xT9aY9ZxsKNGDcRT7nsUka3ID78Txh2M2XdtKLjqtHdfz7bl9ZsH_UesV8d-lu1328PGg4W6EH9zA8NKRWTUQKRiQf4AIiGaXG-WPB8OA9dUvzrFQLVve3ofzGs1dC7hTp2_S6XZ9Wa2sX_LDbH56LieUVVsX24zpDAzdK-PUnzgWqcrM6cHIPdRgAu1zsStd0jYes5t4WKk95H5peBt9RrXKEfPb7meoP-2ZTylw5mx2WOBhZKckT2K1KdbEryR62pp-CQNZjVhw1cqkYwdz0Hls-7C1xwpstKCO1iHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h61yHCTwAmZHTLWO6hbbgNoi2j_lHT1syUZCFlirU__1CFBE4rvxi1_Ncm36LVuV3x_qAfdFtnYWftp2gxJ0J0-05Ud392ZvNa1RrkO8lZf282--puN_lAtT9WEC8oC7utRBC6SfSgGc2SET_kmAgRZpSh_J53uinuNLxy1x0ejn0iw1f_WA0jgyyNCZKtUktXJabB1JfqXKiWS2R2m8T6MMUuSVvHf2BzoTxbXV5-Zr8xSg--i4tertlumJFJ9KCQ3zt5WxM00Rzvk4Vu-w35ExKlKOTumtWWNKzK1_2DAJBNtEtw_DLHOpdPXn0QWUJLFp7WduM4eU4E3ie4_UAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myvO9VgJbplQtEM3Vi_IG9goFwXKaCIVLQewxmC9e69rsLMzcFfkjTVHRUpSymKb52b9B3U3RT_LWOMh0092kXdbR0QvrMPUAHdfpHdJvXjMXowlDB2Yab5ptsUlpxdYgnfppXNXnHjEqY7R1YZk596_G9NvfJyQ9CxtnKOxw6ZhchCZp2Jdfw-wr-egQM9mppDIv1rbVjNyQctbqq1ZfyX9mApQ3fM4mrPFe3AwFWlJumxSNacVYVXXKsG0GbdIDwmPN-LbgEN5Y5VjGVQWTnSDzN-NtfOV602ykBkHqWVTPylaTIF0788EuFFl89Xp_tBpI-qi-vSVH5u4B9Q5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncSWcZXYmZ4vhGR6-X1f5aiIyfzWcT21HTGy45UAwrc7nENJ5CB_6weUFuV0ACGpx2FwBcz25qn4kNkTeF9jT1BRsHxhmvwxP2up_XirmnpQD7GfvUBIS9hEYhzyxMitxrHgGVKnx5B1zYiTvwtNTOZCX2nSSw23TJrohc3hcdoLFOE5IW7R6P9IpHyJlO_UXkfmp7wSnxuBU04GsdfBUzFvMtfq8mZY4D0NRa9rn_P2uBYB2DDgQKFxewA39U4uAqLa_ALANCnmturh8hSUKWQPczxG-40uaJIoM30lLxX3UtNm_4kkTGapZq2JTVJOQvpvPJKUJB1o-SWf_JhxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozWYIAnglRvxZUnlf4eHwFRlYfmqVwo4MPOPPLCrzM3YwZxdj9kE5E5DeD_oPH_K2yqP59n3Gl-qncx8wC-4OiZMdOnjKEuaThxS3L5upppTuUfb8QXkrOHxz27r3sQ2Z5UEMDBx8AktqxLX6LMATUa3vxCQhND_JQOmuv-KvF5e5ijsXEmJuo-raxSsWGg_tUb_WntDgUk9x_NQmwVepKXHnBiU6KQgT9xmsYXVIjbgvJmVdjOfxLlZ_Kso9S3EVcslITn7Xny_TJ-gEXRXceJw2GZ9GGSqVhBl95Sq8g8hvkpYqBNUVvUwql2pQJ4am-GcWNWpG5G83TsvWbK60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peu7vBjI6OeBp7FahI5lmHKfCTRPiuIJfm_8YSaxRGiVvBYuc1r51L2_DSFUdKMYZv597j17vhdH1U3NERoK3XKNB62SmC6ay9Lk8QYscFFDDZ0Pz9VlrFWvKxUjAvYmpVUmblCZmb8W4jBSlcnkSqEYNZ2ix-7eSTLKvM16iW6PD4cAetZXwI8Ral7E3i56An8kvHXcmVhaSh5R3hrUwJ_UH6-ZsFiW_FqDv5M_cYUEGlCEFYjKQivxBDblBE1G605rINDEV8Y5oyFdV7nEjkUW1ubpM2hNQM-OfGpsYHEQAEwk0Sx8gyOlS95_MefDewxvZ63nnp2n0HMPSSTduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6H_GYtpFIpmfXAKe9H8iQJQhY8yMDwK1W3CAL_YB0E3GSpng2GGbuVAfg--1psbKFAmIJNtpmvqlaETq-guiLi5MH48LH1gwlEKUMCtNcjYe6r1WPUxKyCbwW5IehIT9uXZZx07wP9L-GFg6ze9j0_wMCsO_PnGOB69QlvQTSzubO_PZgCezbc7TC2VCq-wkveEqovaRmm3ousvsjtpD17DSIX6rK6WhWZpYK030-DI93xIsZml5Z2gNHdhHLm4TccG75rR7Dwq9YvuJb5w0o_IJCft6QJGGdQpFz1wl_b4bGjowWAUuuFA5ahyiBtJ5CBIk5kZ1erMkzsokdJo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyDiXFHKjUi9wfjksnR9v5Dn7SPPpWj6EJ2G-N42grx01gwtl12a7jR269oIAaGHWpXHrrN3Nb5AXMb7NFL0hpgKvWrsjMiuP_rZ8WGRtska29Pp_ZUwV_D497CGZ7yOjIfml_MOfHisvIaRTCQjaYoKidVZWx9Zy3_1YnnC83a03yyuFiYxM4xjMJFYhE_kZVnO_oSKpKUCGolYhyHWUoBpxCIhXr4MRZT9338kXLWMh4eBrT-4Qi0PUsFY7brHfD1cCKu0Ckc5JpIeua_rIld7vWnsuj_yI98aW9_MvE7B_a8u830QctfPxVKom2UeSsWlPLZyDQ_5IPriYoT1PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از آقای شهید ایران در لباس رزم
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/464873" target="_blank">📅 23:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464872">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f73145a9.mp4?token=fTPoHG0Qcc1r7wVcTmZ96OTc52bAfKMYcokAtL0xQZ21vHwHgDsHlHdNqbfhf7J-qyysIhWplkgDEBnWaD6TJURnWrT8vtTo-7CPwJhJGiLmpW5z42xdKTdx6K4GVZoEdFAXc2uT9fZ0kBle7lxEv269vymB1vLqthgbcZbUCjqktxlsUN5dZMsUgOcRZeX1QSrXZL611jfxhETdF9iOBbq_a2qIC5dsA1FI3BD7pUWvVeKAyCNx4JhJpunFjmv1dy8PTryfBJvWV0fuxoYvbHYzfA1QDlmWM1lHOddVAZP-fFKEIcAjBuQqdOb5FCupYEcRtdyq2HWFASRschLkCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f73145a9.mp4?token=fTPoHG0Qcc1r7wVcTmZ96OTc52bAfKMYcokAtL0xQZ21vHwHgDsHlHdNqbfhf7J-qyysIhWplkgDEBnWaD6TJURnWrT8vtTo-7CPwJhJGiLmpW5z42xdKTdx6K4GVZoEdFAXc2uT9fZ0kBle7lxEv269vymB1vLqthgbcZbUCjqktxlsUN5dZMsUgOcRZeX1QSrXZL611jfxhETdF9iOBbq_a2qIC5dsA1FI3BD7pUWvVeKAyCNx4JhJpunFjmv1dy8PTryfBJvWV0fuxoYvbHYzfA1QDlmWM1lHOddVAZP-fFKEIcAjBuQqdOb5FCupYEcRtdyq2HWFASRschLkCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار مردم فسای فارس در شب ۲۱۱
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/464872" target="_blank">📅 23:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464865">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcRgSAkgG1cDPdqp3E2YuG45hgYYECxQ4Ma0T203A3HmtNdwlBQGxKXuwwRxB5C2iYyMNGfWB7Dg8vMX1La5agLQEWwovPB9IzrggzNioROZ4b3K3bKiCanELnMuL6cANRlUuYNYCtDwgw0IKwXEo23jQvZnhMnBKmcF2O3eiwmMUgB2CXklp_OmBZKorlDl284hLMcyQzyG3KaBz9r3vNFX8xKGws_OANPS_meAIW95BbW5502kLlkttRBpA3uLWO_OqDQDpDDtbML_1tZQxN1rCamWs-uyDCLHCZTACvxNxwJxw8l11OLLj9H-S6Iw6pTMk21W6i-q27EOylNyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjqH3MDIeBwoQDRy9ydsu0mO1l9iEayCPZIYnsuNdOzYT5fMPFJ3YOPipBAx2VjxqO1UeZMzdJeUJLnnO0iyeoZ-hiSvoFlwuSsPPwiXhNUHnm52sZBr5TxjwzUjBN0-RKAyz5m0sc4f7sxFrzx0PU8P21ZuhZvvH5QQfq-4rBk1MN5QVssC1Ivx1jpjt-PofHfKFiEkZSMGp_GOpO2kyCAc8qdU_n01dAjVBQBzIduvfjQg25NFs-mMBMb-LgWsKV-ftK4kK26IWPwHKgpG-Zllfz0HoBbqJpTXzetvvy3dreOLTS_8c3EkJOZFkh7QahjhlkeDAHpG--u10Smd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7-kiIaBGlhbwGVzALUsvjymi3RY6BewI15B2lROOooik9UbyZIqZjgdGKW-_BGJ0xUNiIMJrc84LrtLmfZCfdI5hr5PL_0MVxFsqCtulNrQOu4y5pL8zr7fZlMZZfwBt-ZykbWkk7EJTYm0j-0lNbUWnks4Vgj1kFWcEWSLAO6Acq_IiReGK5bYBh2gJMCxjOpFREBhFt493SuEQEKJgyFE2RwJlk5Wq3hIzCUGXawnGB8D9bjb7tIDd9IO7D6shYQUaI8i3YrLqAGiCUDK7MZRcNzB4CPdUwBgnYy8MrzduqqhWaGO0j4ASJilIBV-5quLYmecsLqu1kVt9mLKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/na5htXu07vD2WuBtum5eyERUgJv22tor3jJyIfhe8YNi93FmqeNpn_jRGovI6zwZsFLAGHak5pt34GDd1QwJ7HMtEI9jMIhi7VPiii09fdLM9IpSuICM3eDGB1EddwB8SZPttfQN7F-oHYMGwt6hUFPr1LodyUwI8HP938-FHJ199QRxoq_x8FcwNF9lCNUg4i8a7Ho0RSWQnQ1f-i08V0Px7VB3ME5KhssUpFG1sBFx7yveX_kn13HbX4iBnWVfwockEhBp5L8sj8zdW3wx3tad2jQUk0YxthYhgiog7-KMmgUvSHUPXP96vGgHyPv46cKEKoTg7QzoRLB-rR9BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhgwdph2XNaCTDuAndOc5O17Kz13RESTYfbUiZSMguIuqW2JnBRcmLwS9wV5UAgJHGjXhIybyvZlnlPhiuxt1yGTRkle76JTZkT2BWU1Wc26LD4WEIBzt9PeSF_viOIEAKW5f9nlk_ufez4qfMmtZR7ricFQMvAGTmdv0uv1zNen7uu01qdDtUh3HEr3eTdzYIvA2hFR4OtEMLHtyecM0joTP0MwvLPhzHzsgyKBecAwuA5TSLSQa-ceuWUwfUeNBZ64Rp7bKsjOeYbHIyIsCopfSXJ8RqoW6CDEPjOm63NKACylpva6xYnf2DCuPtFaMyQaVIgrd30CE1lEbUqBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUEE4k6lcJFK_rD8_LV8QZPCIJGHE86OZzEU473X1lR7xFM_-LsI-8fUdQAkFLIJ5LSBs5EgE343RSExrQbqcCYh4cOjv0ajofg1eIpLPms_vfjX6c_PDNI0ZVKgJxyZACn7eniMbO77P8n3XuLvesWxTKCA_ZVMGH0h5SiygD0cQ05X8vkrOmPDEQc8q7hCC9ddW6FoiSH3KWLB3majRAh9Np1H9hIUlcNReQ1hnT8ShzsbS-eKRyHY1M2vJE9IsXDC_J1FFaHGtKVlz8Syuac_MLkv6M8OIU5Tni6DZO1rh2_s6zu5Fy6fRScLce0SYhgujgqAWI1-IT1qmkbCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k78lQyOd-t_UtxkF-O7jHkLu9pRz-ga6a4lm7QnqPzFEIGe2QncTQmwNtWpWeoT_LwIU3iYnZI57fk7ZPaIT04Woi684_I8FZCEDzb01yyX07dhT_p53wp8r8jlL06O0kEhm_lTgxy98BfKHVDGJRO0G1CRSO_345R3arUqt8ILilYI9V84jtbudVc7DmYgUn23omUsEmv_A59-tEQdP-WF-nQAZWiZA7lyiHSg6Iw1p_bUGLPOgph3TDp9EHCwRJdFS_k2Ol5ZD_ze1R558BD0W14EV9CY-Uu-tsw1RnTMmp5zRnPXhetSYnOzfBNPDg_6UcD5ZtHIQIiBskd0Riw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت هفتمین شب رحلت آیت الله شبیری زنجانی در حرم حضرت معصومه (س)
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/464865" target="_blank">📅 23:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCXPvsrlWDs459yCykvux6hPRRoSQKciag9Xb9MgzkNLUM-UT1Nmtislkv2GTC7-rK_GjxlTxaxDqvzUdB3RMMWzIKpkn03DV64WimoH0YUhIFZbUlDtejGns9k-46tl-yIl5CqQuyT8JdHypdlC9KS_2IP572GvhjNLC0Zo66Fh7J0xtTWt_XUNqwUNq95oMPWrUx9B4-s9LMFbFKk1UASHOUHkGb7NpZFxjqUM9u_flPRw_vHp8ayp9clKtXeeQrQPVWufrvm1I-TaniVWxLM7jFY12r9ofBcW33gm2n8KnMGIazQ1PhwwB3tdNSTO_DLsiXN1q1DX7wE5Cox4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس فروشندگان را پشیمان کرد
🔹
تنها یک روز پس از خروج ۶.۳ همت پول حقیقی و افت ۱۰۴ هزار واحدی شاخص، جهت بازار تغییر کرد؛ شاخص کل ۱۲۱ هزار واحد بالا رفت، ۲.۲ همت نقدینگی حقیقی وارد سهام شد و این بار سهم‌های کوچک‌تر بیش از بزرگان پول جذب کردند.
🔹
شاخص کل با رشد ۱۲۱ هزار و ۴۲ واحدی معادل ۱.۶۹ درصد به ۷ میلیون و ۲۷۴ هزار و ۱۳۲ واحد رسید. شاخص هم‌وزن نیز ۳۱ هزار و ۳۸۸ واحد معادل ۱.۶۳ درصد افزایش یافت.
🔹
امروز ۲ هزار و ۲۴۲ میلیارد تومان پول حقیقی وارد سهام شد؛ یک هزار و ۴۳۷ میلیارد تومان به شرکت‌های کوچک و ۸۰۵ میلیارد تومان به شرکت‌های بزرگ وارد شد.
🔹
ارزش معاملات خرد امروز ۳۲ هزار و ۴۹۳ میلیارد تومان بود که نسبت به معاملات خرد ۴۴.۷ همتی شنبه حدود ۲۷ درصد کاهش یافته است.
🔹
بازار امروز فروشندگان را عقب راند، اما تداوم این برگشت به افزایش مشارکت معامله‌گران و ورود پول در روزهای آینده وابسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/464864" target="_blank">📅 23:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihlPCrOuNzLupueHxI-wOITGqYkI14L094klt-UDBdkh0OnatZVKiQ5Qzzk0Ci6_jvyyeySeotX2DmEASCvwcPznTDrNz6mEXacp8iomP6N25DSM5PfWU7qIzs9VY9tHeNDu2P1V6ewIV2V_2ek4d25hWSSue48sfUlZgjTQOFLLdN82hYingiO6CjaMKy2dYoxErVvODf2vklWcpmX5roG_xjHfsr8AR2IbFdVJHGFv4A16L2UpDHgz6AFxblRYA3WUi5MX6IvRinRZ8j-S-NJEI4SwLKs6ALvlEZEr_6qgGCCmTEOTq6T3fVhKCON1wPrsrLg-O5bi72BXYA68ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربهٔ پليس هرمزگان به شبکهٔ احتکار تجهيزات نيروگاهی
🔹
فرماندهٔ انتظامی هرمزگان: دپوی غیرقانونی و احتکار تجهیزات تولید برق تجدیدپذیر در بندرعباس شناسایی شد؛ مأموران انتظامی ۹۳۲ پالت پنل خورشیدی را که سال گذشته از مبادی رسمی وارد کشور شده بود، کشف کردند و متهمان پس از تشکیل پرونده به مرجع قضایی معرفی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/464863" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1PnhfSy7QIsyyHhwvgQNmq0aV7_HSnIuzF_tPERCIBtFKdHPlqGJDErZV15GmwXtY4xOQC9RA3nBjyAjs2Z9okJxRPOCnzSig8M1344oTQD1aLaRQVjvlGu4MJDgopxvyAAjZXUrqJreabXArO3B1VBywrd8RH4DqOGlXi1ChmGe4b-lIn_L5F8IQR7X3b5pfDh6AG_mxeHg0LwQQYmf0Wu_eLaEHU7x3xO20rv1xG42H4-tQZqzg-S1FcHnKnmTgLWPNROv6w2Pr7XxiNl3I6g_R0i75rk2cuBcuQZ4urToDbdWj1zfvskaujScEs_IO2zOwzaAWwg5dDnEltQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
کانال ۱۴ صهیونیستی به نقل از یک منبع: سربازی که در غرب رام‌الله زیرگرفته شد، پسر سفیر اسرائیل در واشنگتن است. @Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/464862" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL8ObSlCddLgAQA3gomivFnnEcPV66Pfy9vdj2w_ZTLACzkXWyYRozZYbmptwCmgFYYYzQ_X-yRY1OlGpxjpAT0a9zqU2_m1dw2SIFEbv8i8tyX9vlMHIo8Chyw672UJshYMxzYw5TnzUL38JX8QflsMmauRH1a2hvUkeQmX5wN6s79b6KazfFdHIMZbLs2PQZ59LmK2UDIlBs_efhM_yQlYrH-ZMnQuWPMXdKnqkU9ZYsvuJFyxOnjQ7M9IGGfgMCyHu2XizyygE-ag3P4TAaHkhKCBQ87edD-BlhmDseGlN_gQ0DdqcLZKDlgZTU0X-W2pLBYFGnfvkdETethgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: ایران برابر هر تجاوزی خواهد ایستاد و هم‌زمان برای دیپلماسی واقعی هم آماده است
🔹
در گفت‌وگو با رسانۀ آمریکایی گفتم پزشکیان و من برای جنگ به نیویورک نیامده‌ایم؛ آمده‌ایم تا زمینه صلح را فراهم کنیم.
🔹
با این حال، ایران در برابر هرگونه تجاوزی همچنان استوار خواهد ایستاد؛ حتی اگر کار به جنگی آخرالزمانی کشیده شود؛ هم‌زمان، ما برای دیپلماسی واقعی نیز آماده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/464860" target="_blank">📅 23:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJf05Wm8GfUK5nuC8Cxn6fz0K5LfZlhVkSpO6yN2n3vN2a2Ebuy5O0AtAKHagKRZowERUu_uajZ_59b25QcYqa4bp1umseijz4etC7uQKqwdvFOeONYZdqOc6IL7CkeT1KTvcsBSK0NALkf-N4JqOl1Z3dI01ql-TdSqVbQx2gxyzIsFCxaNPM01aypUHjadidcWuDbFgmaIWnovBOTfSnJrqstteDSw-hzKjGhUZ1KnDTURxIsNVnyvJv1PEd6nw5L324LRc3mJF0acUp5d8c8kv2K0DaN_m017YpoUitf16ger42qyx_wOL7f4hHlMfKmoF8BnvsQDfTEIP1h1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردپایی از کشتی‌ها در مسیر هرمز نیست
🔹
تصاویر ماهواره‌ای منتشرشده از تنگه هرمز از نبود کشتی در مسیر عبوری خبر می‌دهد. این درحالی است که ترامپ مدعی شده بود تنگهٔ هرمز باز است.
🔹
در آخر هفتهٔ گذشته تنها ۵ کشتی از تنگهٔ عبور کردند و برای روز یکشنبه هیچ عبوری ثبت نشد. این درحالی است که این رقم در آخر هفته پیش از آن ۳۱ فروند بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/464859" target="_blank">📅 23:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464858">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
قرارهای شبانهٔ کاشمری‌ها خستگی نمی‌شناسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/464858" target="_blank">📅 23:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464857">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
منابع محلی از شلیک کروز دریایی به یک کشتی متخلف در مسیر غیرمجاز تنگۀ هرمز خبر می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464857" target="_blank">📅 23:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fadf46210.mp4?token=YTrxYKiP7DQK7xdj4GcH62kNrjd5F4vBZM6jH3GBobHYMdQtkSo47fXY8UqzQ7RbVr810vHXjxt5DV_hdK6UH3o-mNpB5wYWb7mdcve7ukg0ugLfqJGD0ZqbKheutWnU2D-MUtxHhsvkZyfZQwOAx8jqT8hDVZT_fkxZcy1E9Iw4NohmJXcXlYY_gx6fXnSndNp6IPf0JOgyIdaE28RIfaLDAi3ds6nyJCtOZtX7T4yJlO6xTRtXN6gyB97cz7Gn8yuqL_HRVsz94L1WPQL404ubbGekRjGZIksYG0vmAci9J_lUNK5j6AWwpU6IRFXb0XiFXzfSO4fOBp-839Pm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fadf46210.mp4?token=YTrxYKiP7DQK7xdj4GcH62kNrjd5F4vBZM6jH3GBobHYMdQtkSo47fXY8UqzQ7RbVr810vHXjxt5DV_hdK6UH3o-mNpB5wYWb7mdcve7ukg0ugLfqJGD0ZqbKheutWnU2D-MUtxHhsvkZyfZQwOAx8jqT8hDVZT_fkxZcy1E9Iw4NohmJXcXlYY_gx6fXnSndNp6IPf0JOgyIdaE28RIfaLDAi3ds6nyJCtOZtX7T4yJlO6xTRtXN6gyB97cz7Gn8yuqL_HRVsz94L1WPQL404ubbGekRjGZIksYG0vmAci9J_lUNK5j6AWwpU6IRFXb0XiFXzfSO4fOBp-839Pm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دانشگاه شهید بهشتی: باید گفت‌وگو بین نظرات مختلف در دانشگاه‌ها زنده شود
🔹
متاسفانه دانشجوها حاضر نیستند باهم صحبت کنند زیرا می‌ترسند فضای رادیکال و جنجالی پیش بیاید. @Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/464856" target="_blank">📅 23:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464855">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">منبع آگاه: ادعای آغاز دور جدید مذاکرات غیرمستقیم ایران و آمریکا کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌ کننده ادعای آغاز دور جدید مذاکرات غیرمستقیم ایران و آمریکا را رد کرد.
🔹
آکسیوس به نقل از منابعی ادعا کرده بود دور دیگری از گفت‌وگوهای غیرمستقیم میان آمریکا و ایران احتمالاً از روز دوشنبه آغاز می‌شود.
🔹
کارشناسان رسانه و ارتباطات هدف رسانه‌های آمریکایی و عربی از اخبار غیرمستند مذاکرات را جلوگیری از افزایش قیمت نفت به نفع ترامپ در آستانه انتخابات آمریکا عنوان می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/464855" target="_blank">📅 23:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464854">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486ef75807.mp4?token=Dkeo85-cqbDLh6IBd4hD_CNT9Om7-MhzKvLa1pa5kijp0bXcfDVNxaGli7LxBpfMk2iQh5WcGXY88n07qupSzPjAXXnkNLdAy0Ra0VKMjqAuqxaQhcRdKgk8Pj5BBf3q3sYKUL7t1_3lOyUgrvqSOeCbeo259nk_shY08mnEOammQT1-Na_32vYLEFC-IGBhQwfx2N-PA4-8pVjXJemy5iyzaCbH3pxMi6Jr9vEzYTSZbPbgaRzVKcmxEc-uLjzrLObSh_NORKrenpKjcNDWuiLyBG7BjdutBOKMy606DAAXp2yQYfCfn4eGJInUx6sGR5G3L4Ik5NYeZvMDUZnd-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486ef75807.mp4?token=Dkeo85-cqbDLh6IBd4hD_CNT9Om7-MhzKvLa1pa5kijp0bXcfDVNxaGli7LxBpfMk2iQh5WcGXY88n07qupSzPjAXXnkNLdAy0Ra0VKMjqAuqxaQhcRdKgk8Pj5BBf3q3sYKUL7t1_3lOyUgrvqSOeCbeo259nk_shY08mnEOammQT1-Na_32vYLEFC-IGBhQwfx2N-PA4-8pVjXJemy5iyzaCbH3pxMi6Jr9vEzYTSZbPbgaRzVKcmxEc-uLjzrLObSh_NORKrenpKjcNDWuiLyBG7BjdutBOKMy606DAAXp2yQYfCfn4eGJInUx6sGR5G3L4Ik5NYeZvMDUZnd-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دانشگاه شهید بهشتی: در آموزش مجازی بسیاری از دانشجویان با کمک هوش‌مصنوعی سوالات را پاسخ می‌دهند
🔹
در تلاشیم بستری آماده کنیم تا اگر محدودیت‌ها زیاد شد از آموزش ترکیبی مجازی-حضوری استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/464854" target="_blank">📅 22:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464853">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9080f8cb.mp4?token=biFS18jiZ-nGxZ-Qncx-bESOxaI4bwhXKgdUs-IGQzC8Awn3aB9VqZk8TL-hWzDKNfHe1sp6KFJ-xdNmhq3RHMvP6RNrtfK_ApqFk7DF0cwFSzkH-MTB8e2bRb7lzX1tNj3y6R_SQdJgu-nXSyU_qjLBSCaR_5FmDybMe3tsxLtCFfnV4yYebfmBUstjziNVEXhbuV_cnv36uEAE5Q4-khpKEeBrC3tbqMoRaFrHxhJ_KYWu32Rd0XbZ0DyndXRLIa2MGw7PbSxs1Ru65FQpIfmH3Pp7jp5mc4theH86Dk72MAeRebITjPKmIqyxo53pkKD2d_jc3GdT2r7cNARH0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9080f8cb.mp4?token=biFS18jiZ-nGxZ-Qncx-bESOxaI4bwhXKgdUs-IGQzC8Awn3aB9VqZk8TL-hWzDKNfHe1sp6KFJ-xdNmhq3RHMvP6RNrtfK_ApqFk7DF0cwFSzkH-MTB8e2bRb7lzX1tNj3y6R_SQdJgu-nXSyU_qjLBSCaR_5FmDybMe3tsxLtCFfnV4yYebfmBUstjziNVEXhbuV_cnv36uEAE5Q4-khpKEeBrC3tbqMoRaFrHxhJ_KYWu32Rd0XbZ0DyndXRLIa2MGw7PbSxs1Ru65FQpIfmH3Pp7jp5mc4theH86Dk72MAeRebITjPKmIqyxo53pkKD2d_jc3GdT2r7cNARH0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید سیدحسن نصرالله: وقتی ما را محاصره می‌کنید زمین و باد و کوه‌ها و دریاها با ماست
🔹
کسی که به خدا اعتقاد دارد امکان ندارد احساس محاصره کند، حتی اگر همۀ دنیا بر علیه او شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/464853" target="_blank">📅 22:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464852">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16524661c.mp4?token=KGwgxfwEiYItGVNZiJN4lC3_XD4uuvmN01KY-C9rJQQE_--tb-OnBLMDnKZEgLowpAXA_8qO4hP8yhc-BdOi7COdAAg9ubTQBw3jIlqGjY_I0pw6VTHy_5VL1R1g4T_pBLSUn-v-WF9WByQLVEpckP3LzuM8iuprMaLvGZGyXokrCM3RYhHBFvHP_HGAgbb9CcfvQz8tIt6IJ0x8o6wbfnbX3eP5nzFYL2xJIB1-HD2jxMww9QSrywR8Wl6LtuQ6vUK07XJMuOeTVjqmYyZiqxpTg8U8Wk7yvkXUHCwxBJs6fF7jOp-daf4nx2f8EFXFS1prQQXEC1XcYyP6FNclaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16524661c.mp4?token=KGwgxfwEiYItGVNZiJN4lC3_XD4uuvmN01KY-C9rJQQE_--tb-OnBLMDnKZEgLowpAXA_8qO4hP8yhc-BdOi7COdAAg9ubTQBw3jIlqGjY_I0pw6VTHy_5VL1R1g4T_pBLSUn-v-WF9WByQLVEpckP3LzuM8iuprMaLvGZGyXokrCM3RYhHBFvHP_HGAgbb9CcfvQz8tIt6IJ0x8o6wbfnbX3eP5nzFYL2xJIB1-HD2jxMww9QSrywR8Wl6LtuQ6vUK07XJMuOeTVjqmYyZiqxpTg8U8Wk7yvkXUHCwxBJs6fF7jOp-daf4nx2f8EFXFS1prQQXEC1XcYyP6FNclaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نام نصرالله هنوز در جبههٔ مقاومت طنین‌انداز است  @Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/464852" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464851">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXXRDM9Yf3_m3genTuTqvE8tspxj7mHyAZhz0iG4_daE3QGRI2OwXYXoE1HeuVYQJTSCxbBpper4qLJv7DSOysy03c_QOgij5l_dZ9KaTzzFuRW7uPCUi2G3zr1e3xzBrVdvj5HZRhA2zOPrvkXtNrwfEyl4IKebsQOsmW7999NEzlgeQmsI4ZTTrgOhGVEQWe52huApU9MXtlUTmCPKP5GxvmjBVR3u8-J4B7FNuSRztHtNHP2ywlakE9r_KjrZ5Cj06RZiicebwxhfq3DxVp0luXVVGTPUiPkrqvBP3R_KMtREzdCVAC4FIwtuhrcVPFYwYO6o0eqoCG0eN59Cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در سفر به امارات با بن‌زاید دیدار کرد
🔹
شبکه عبری کان: بنیامین نتانیاهو، نخست‌وزیر اسرائیل امروز در بحبوبۀ پرونده افشای هشدار ابوظبی دربارۀ عملیات طوفان الاقصی، سفری به امارات داشته و با محمد بن‌زاید دیدار کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/464851" target="_blank">📅 22:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464850">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6927a198.mp4?token=uGvm228gEat75IPg-e6peNaE5TWH6fo_q0VjxRb5X0HUN6GAZlbc32EDcBNQSB3Ai7g5Jq6kmDpfORg5V_4muxCz9IP6L62cLk1Lc53i5R41cK3FM9tVactmrsfKDwvMHbEI4HAKuJUNf4SenfK968m7JAWC8zpymupdHq8W4L3Cu3K8xjAWDp6nSqJWNrqi2gFPLdv2ikPlMMoGnPC7fN0kn1RvtK4K6zoWElkF8xn7Ye6XIhB2f02zBtep4RNqPHGgXBEaPxwVu4X7XycaFMDhbVb94Axmuxa4xYsg12JNlOp4cePodVSs95CkODFTPspnK6Y14dqMb9LvRs0hnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6927a198.mp4?token=uGvm228gEat75IPg-e6peNaE5TWH6fo_q0VjxRb5X0HUN6GAZlbc32EDcBNQSB3Ai7g5Jq6kmDpfORg5V_4muxCz9IP6L62cLk1Lc53i5R41cK3FM9tVactmrsfKDwvMHbEI4HAKuJUNf4SenfK968m7JAWC8zpymupdHq8W4L3Cu3K8xjAWDp6nSqJWNrqi2gFPLdv2ikPlMMoGnPC7fN0kn1RvtK4K6zoWElkF8xn7Ye6XIhB2f02zBtep4RNqPHGgXBEaPxwVu4X7XycaFMDhbVb94Axmuxa4xYsg12JNlOp4cePodVSs95CkODFTPspnK6Y14dqMb9LvRs0hnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهلت ۴۸ ساعتۀ عشایر بصره به دولت عراق
🔹
یکی از شیوخ عشایر عراق در بصره: ۴۸ ساعت به دولت عراق مهلت می‌دهیم تا از لغو پروازهای ایران عقب‌نشینی کند.
🔹
شیخ ابوحسام الحربی: اگر دولت از تصمیم خود کوتاه نیاید وارد فرودگاه بصره می‌شویم و از تمامی پروازها جلوگیری…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/464850" target="_blank">📅 22:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464849">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GD9rFJqka5BdAMJCAC67GHtgakPK1b9syXCaF4oUqH5VaF1SbCYwCnUkIkvUHYV5hdGbXDSK2wBppSQpq3BxKjcOUKXJOdw3OOWrcJlrRLbEiF_hh2OkCfzbIAV6l20HxPcEmLh0n-XCvxP2Xg2lQ5meAOQm3UajYfR8I5Hph_jmQEWcdDNKAtwT6gEfSIVTdlSCno0_EtXWXwIN0nQ5i8WphqOJV_Fu_XAtJRMWcnYTFt49eZ4rCrfG6g4bmwL7lmcCNSzUlX4ZWtolvPhGTJAuIJJvzW7qGlqI9fDV2dvr_QND2s435IKux6l3vBiynEsPDO0-m00_FCvzB2QgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ مقصد بین‌المللی در نقشهٔ پروازی ایران فعال است
🔹
مدیرعامل شرکت شهر فرودگاهی امام خمینی (ره): هم‌اکنون بیش از ۳۰ مقصد بین‌المللی در این فرودگاه فعال است و تنها در روز جاری، بیش از ۶۰  پرواز با موفقیت به انجام رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/464849" target="_blank">📅 22:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464848">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_S_zKRAWXOi8oyI-asDN_Mu5Ovx48jn2gdV5sdYg3ZLu-WK7c_AT6nPutC0FEAxA_BHgfYr7rQh3k-uJxgsEMgPfAfguxiF6od4lIGJf8HI8yfB7OdIxhozIRRp_iOKQJPMP7ffzm6kq98QavsdatE--tt6-Y_TDaEUb7sRLnN0JaITPmrkWykcnCx9kvDb1XfAmurciDCKCDVeDWscgVK1JYtHc2xEZyFXcZR1lp0HiIjmry_xkWgb0QmgMhLY9szeDIGLR28mHUY4dTHAh4KT0jpQJMkTU5En4rRHtWE_otz8l-d-2LQNcvAejdd69NxoMmiI9snaPy348-dttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماینرها سالانه ۱.۵ میلیارد دلار سوخت می‌بلعند
🔹
براساس بررسی مرکز پژوهش‌های مجلس، ماینرها بسته به روش محاسبه، بین ۹۳۰ تا ۱۲۰۰ مگاوات از توان شبکه برق را مصرف می‌کنند.
🔹
از سوی دیگر، هزینه سوخت موردنیاز برای تولید برق مصرفی این بخش حدود ۱.۵ میلیارد دلار برآورد شده است.
🔹
این ارقام، در شرایط تداوم ناترازی برق و محدودیت منابع انرژی، اهمیت ساماندهی مصرف برق در بخش استخراج رمزارز را نشان می‌دهد.
🔹
این میزان مصرف در ماه‌های گرم سال سهمی حدود ۶ درصدی از ناترازی برق دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/464848" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464847">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a0a436a3.mp4?token=HM1FquExpFQdmp4cjo8eB-tpVal_YHOp8quWhqTzpcZa7maF6oirdcslSZGZaZtIaTb8Ww1-jv5L3R8gJz7SjAirtO7XLHtnN4-GCMTe604NvQ8EFjtNZU7wDhJfq8soAHZZIMSNImNaWWkcKKa04AjPBxbHHMcJ7asXKheu96ZRZqZ__iM6iIshsPd6WHKKKV2aRBonuL4tMhfauDTy8Ax6gjIOMuRUwz1XX2t7z5S3Y7VrY9PPAG8ZYzZOhPM1osOEvz_KKo0MYBdikFSWDYlMk3W27lLZGdReJn943VrkAQHnUOrAVWKyixfGXBs4QRDCg9WBBi20GbXjrwQGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a0a436a3.mp4?token=HM1FquExpFQdmp4cjo8eB-tpVal_YHOp8quWhqTzpcZa7maF6oirdcslSZGZaZtIaTb8Ww1-jv5L3R8gJz7SjAirtO7XLHtnN4-GCMTe604NvQ8EFjtNZU7wDhJfq8soAHZZIMSNImNaWWkcKKa04AjPBxbHHMcJ7asXKheu96ZRZqZ__iM6iIshsPd6WHKKKV2aRBonuL4tMhfauDTy8Ax6gjIOMuRUwz1XX2t7z5S3Y7VrY9PPAG8ZYzZOhPM1osOEvz_KKo0MYBdikFSWDYlMk3W27lLZGdReJn943VrkAQHnUOrAVWKyixfGXBs4QRDCg9WBBi20GbXjrwQGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر دومین زیردریایی شکارشدهٔ ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
زیردریایی REMUS 600 یک زیرسطحی خودکار پیشرفته و بدون‌سرنشین آمریکایی است که برای مأموریت‌های شناسایی زیرآبی، نقشه‌برداری بستر دریا، کشف و طبقه‌بندی مین، جمع‌آوری داده‌های محیطی و جست‌وجوی…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/464847" target="_blank">📅 22:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464846">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRH7hzJ66xOLuph8SsrhdzawCEukSiUkJ91_eugiOwFkKInUKfLWQvB-uJTqx29_trKY6iV5XNnsLXX57eUfWFZpRFEWBKVfnwl7uMIDLCos8Zi3mhlEUbqcUwpVuarh1guVpX-qHlz6cUAz2kxwpCFmaX8xIopdCg1xBfVVpbOJKMRBqD1pvFTbWixNXeFv1ifw-9uYHtCX_tF9_0NQTo30EtCt3YUy2tIQnYRSxDpE-3eHrAEtDsW7reSHK26TAa_E6ZAiTQoRtb9RP0hdWFYyO9-2ocqPd3TMwP2RaOU66RpBY2C4BZ0MucjqVKYKxqLbbnWHvW4jYkygdpmvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: دولت‌های مستقل روابط با ایران را بر اساس منافع و مصالح خود تعیین می‌کنند؛ نه دستورات خزانه‌داری آمریکا
🔹
بسنت از اعزام تیم به کشورها برای دستور دادن درباره روابط اقتصادی با ایران سخن می‌گوید، گویی جهان را حیاط خلوت خود میپندارند.
🔹
دوران تحمیل اراده با تهدید و تحریم رو به پایان است.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/464846" target="_blank">📅 22:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464845">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0881e6c01.mp4?token=kvoA6Mo4N_oq5AxyElSQMVbgtgRgQvDoh9AVxw6gN4N_djNKhq55jwOW1v9ftg9ix3pC3BbyXhI-EE3lHK9fM9Lp5gn1iOXLKOGgepkZ9CC0421HBqdw63YnO9gX7ukoCyttjQrArakDl2N4m5SkDMiXseESZGsw3Eeu-1W2hvNuFE9bWcHqoS_h5p9LQm7jMrGvpOHubxlI_KbJgf9ZxcPWEcDC6GB7BBzXaDcZxuOFLsLDAKPuhsyhoPxxsmZmN1OLzQQZx6JxcxqRs1Y6wjWB6WQMvq3p4DcfoFwJp2wkur_PN313yr2h7sDBRnnAn0o_qImtbdPqv7iGQzL1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0881e6c01.mp4?token=kvoA6Mo4N_oq5AxyElSQMVbgtgRgQvDoh9AVxw6gN4N_djNKhq55jwOW1v9ftg9ix3pC3BbyXhI-EE3lHK9fM9Lp5gn1iOXLKOGgepkZ9CC0421HBqdw63YnO9gX7ukoCyttjQrArakDl2N4m5SkDMiXseESZGsw3Eeu-1W2hvNuFE9bWcHqoS_h5p9LQm7jMrGvpOHubxlI_KbJgf9ZxcPWEcDC6GB7BBzXaDcZxuOFLsLDAKPuhsyhoPxxsmZmN1OLzQQZx6JxcxqRs1Y6wjWB6WQMvq3p4DcfoFwJp2wkur_PN313yr2h7sDBRnnAn0o_qImtbdPqv7iGQzL1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دانشگاه شهید بهشتی: در آموزش مجازی بسیاری از دانشجویان با کمک هوش‌مصنوعی سوالات را پاسخ می‌دهند
🔹
در تلاشیم بستری آماده کنیم تا اگر محدودیت‌ها زیاد شد از آموزش ترکیبی مجازی-حضوری استفاده کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/464845" target="_blank">📅 22:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464844">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO_-BPOzL6BNjxI-TNVUzf3V5xtLCw-_eFwiw8G06MF8YYN5KzMsFpNjRNhMLHubhOV-rHLSK6G4nrYMa6ScH6H0MY4Lvy8t3QoPyXGttS-7HEU_-b1TtGDIuO3iOH9ph5z69REodihPBrRK9xSitJHr8fn1E4wYFzhWs7OWX9MzRgKI5l6gHH16YqXgJ5fumTC2J6Fbi8Wb0NUa7oKiuxYF0l704Mbbgf7axsqFIvrox_a7NpeKUz9tRpqbUyxjsOh05TKqV-aLKdjbPBtW3d9saGSS8ZemQFcCjfOlIkIZmtBPUIZ8JfCOd-F4_KBCITn1cXDVFydDk-d5MB4dpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت معتمدآریا به ایران؛ درِ خانه باز است، پرونده قانون هم باز می‌ماند؟
🔹
فاطمه معتمدآریا پس از چند سال زندگی در خارج از کشور به ایران بازگشته است؛ بازگشتی که حق طبیعی اوست، اما پرسش درباره سرنوشت پرونده‌های قضایی و مواضع سیاسی گذشته‌اش همچنان باقی است.
🔹
ایران خانه هر ایرانی است و مخالفت سیاسی یا سال‌ها زندگی در خارج، حق بازگشت به کشور را از کسی سلب نمی‌کند.
در جنگ اخیر او چه موضعی داشت؟
🔹
یک تفاوت دیگر نیز پرونده بازگشت معتمدآریا را قابل توجه می‌کند. در جریان جنگ اخیر، حتی شماری از منتقدان جمهوری اسلامی و مخالفان حکومت، حمله نظامی به ایران و کشته‌شدن غیرنظامیان را محکوم کردند؛ اما موضع علنی و قابل استنادی از معتمدآریا در محکومیت حمله به ایران، کشتار غیرنظامیان یا فاجعۀ حملۀ آمریکا به مدرسه شجره طیبه میناب منتشر نشده است.
🔹
این درحالی است که او پیش و پس از خروج از ایران درباره مسائل سیاسی داخلی صریحاً موضع گرفته و حتی در لندن گفته بود تا پایان عمر به مبارزه ادامه خواهد داد.
اما پرونده‌های قضایی چه شد؟
🔹
معتمدآریا پیش‌تر گفته بود پس از اعتراضات ۱۴۰۱ چندین‌بار به دادگاه احضار شده است. اکنون پرسش این است که پرونده‌های اعلام‌شده چه سرنوشتی پیدا کرده‌اند؛ مختومه شده‌اند یا همچنان مفتوح‌اند؟
🔹
او در خارج از کشور نیز مواضع سیاسی خود را ادامه داده بود و در لندن از ادامه «مبارزه» و «آتش زیر خاکستر» سخن گفته بود. علاوه بر موضع‌گیری‌های براندازانه ، مطالب وطن‌فروشانی مثل علی کریمی بارها در صفحۀ او بازنشر شده است.
🔹
برخی منابع مشکلات مالی و دشواری زندگی در خارج را از عوامل بازگشت او عنوان کرده‌اند، اما این ادعا تأیید معتبری ندارد و نمی‌توان آن را قطعی دانست.
🔹
بازگشت به وطن نباید موجب بسته‌شدن در ایران به روی کسی شود؛ اما در کنار آن، قانون نیز باید برای همه یکسان باشد و قوه‌قضائیه باید دربارۀ سرنوشت پرونده‌های اعلام‌شده شفاف‌سازی کند.
🔸
خانه برای همه ایرانیان است؛ قانون هم باید برای همه یکسان باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/464844" target="_blank">📅 22:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464843">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVKPDnyzsQXohq3Ps8CPGwcDhoIEOZB4uCR-jWALUV2fwGun9JSq6tuFZpj1rkyew4NTkAVvXATXgizV37SMD8iFC_I5GR09ge_q5zZSTJNW2NLGaQnkh5yExiOVHXz6inJNb1wh6LZi0WYWsj6hAJz6Tyd6aB5tCvT325GoCmhOBNAZeZbaicz5ebw9cqGQVAfWmsEpOVnpnsTq2qPiXkI-V7hTPm67umGNuSMp1TiYKGGNny64TFWq9h-dSonZuCSuGZoSJTcHTWYmkmd3QXzBlh6Xwo5dn-JXOJK5ldzzpZU0fSUtR7q2eSHBhsARvpOkGNBiKH9laT5j_v35xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنا و صیادی در دریای مازندران ممنوع شد
🔹
مدیرکل هواشناسی مازندران: به‌دلیل وزش باد شدید و مواج‌شدن دریا، فعالیت‌های دریایی از سه‌شنبه تا پنج‌شنبه ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/464843" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464842">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad59e31267.mp4?token=pP4t65dXvjL5Hb1C4F1rfbTv9DJxkrlxuK3xuvQ9uq-U1o0JBjUcmWSKpNisHO-eVUNbRQhgbqWS3kI5pBCQkunwKN5M8Meo1zVbSpM5Dac8pLZQL0R8lCS1kToWDcSZmiT5Y5tLixRxNUP_m1zmYKETSm2ARIqTaCxApihJDlmAXEcE7efPVWStHgOmKlWuGqXUV0eCHwsySyoiLOPI208oZdvTBQslpYTzi5D-diZxTqdLMAhiGUoiN8nsDm5i5W4r1gPmyVBmvx0oZm_tooS0aQZhw45cE949X58pWwgAmBKx43rhWBUqNaBmMdYgS8NO4Ya0qAep6wvn7xHYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad59e31267.mp4?token=pP4t65dXvjL5Hb1C4F1rfbTv9DJxkrlxuK3xuvQ9uq-U1o0JBjUcmWSKpNisHO-eVUNbRQhgbqWS3kI5pBCQkunwKN5M8Meo1zVbSpM5Dac8pLZQL0R8lCS1kToWDcSZmiT5Y5tLixRxNUP_m1zmYKETSm2ARIqTaCxApihJDlmAXEcE7efPVWStHgOmKlWuGqXUV0eCHwsySyoiLOPI208oZdvTBQslpYTzi5D-diZxTqdLMAhiGUoiN8nsDm5i5W4r1gPmyVBmvx0oZm_tooS0aQZhw45cE949X58pWwgAmBKx43rhWBUqNaBmMdYgS8NO4Ya0qAep6wvn7xHYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اقتصادی وزارت تعاون: کالابرگ مرداد و شهریور کسانی که نیازمند احراز محل سکونت بودند فردا واریز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/464842" target="_blank">📅 22:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
در طرح
مسکن ملی
، هیچ شفافیت مشخصی درباره میزان آورده، وام، نحوه تخصیص واحدها و روند پیشرفت پروژه وجود ندارد. با وجود واریز بیش از ۷۰۰ میلیون تومان از سال ۱۴۰۲ تاکنون، هنوز واحد مشخصی برای ما تعیین نشده و هر روز نیز با تهدید حذف از پروژه مواجه هستیم. نه تعاونی پاسخ شفافی درباره مبالغ دریافتی می‌دهد و نه ارگان‌های ناظر پاسخگو هستند. حتی مشخص نیست چه میزان دیگر باید پرداخت کنیم و وام پروژه چه وضعیتی دارد.
وزارتخانه و دستگاه‌های ناظر، روند مالی و نحوه تخصیص واحدهای مسکن ملی را شفاف اعلام کنند
.
🔹
واقعا
هزینه‌های تلفن ثابت و بسته‌های اینترنت مخابرات
برای مردم سنگین شده است. تبلیغ «۵ هزار دقیقه مکالمه رایگان» می‌شود، اما من دو ماه در ایران نبودم و تقریباً از تلفن ثابت استفاده نکردم، با این حال هر ماه حدود ۴۰ هزار تومان و این ماه ۵۶ هزار تومان برایم پیامک هزینه آمده است.
🔹
در بهمن‌ماه ۱۴۰۲، مجلس شورای اسلامی مصوبه‌ای برای
کاهش مدت خدمت سربازی
با احتساب دو ماه آموزشی، به ۱۴ ماه تصویب کرد؛ اما بعد از گذشت حدود دو سال و نیم
هنوز این مصوبه به‌طور کامل اجرایی نشده
است. در حالی که این تغییرات در مناظرات انتخابات ریاست‌جمهوری نیز به‌عنوان بخشی از اقدامات انجام‌شده در حوزه سربازی مطرح شد، همچنان مدت خدمت سربازان تغییری نکرده و بسیاری از
مشمولان در بلاتکلیفی هستند
. ما از شرایط جنگی کشور نیز آگاهیم اما انتظار داریم وضعیت اجرای مصوبه مجلس درباره کاهش مدت سربازی به‌صورت شفاف مشخص شود.
🔹
از زمان شروع جنگ،
وضعیت اینترنت و آنتن‌دهی اپراتورها بسیار ضعیف شده
است و با قطع برق در منطقه یا حتی مناطق اطراف، عملاً اینترنت نیز قطع می‌شود. برای دریافت فیبر نوری هم اعلام کرده‌اند باید هر ۳۰۰ واحد مجتمع درخواست بدهند تا اتصال انجام شود. سؤال ما این است که در این شرایط چه نهادی پاسخگوی کیفیت نامناسب خدمات اینترنت است؟
🔹
چندین سال است
آب شهری گرگان روزانه حدود ۹ تا ۱۱ ساعت قطع می‌شود
و این وضعیت انجام امور روزمره و نیازهای ضروری زندگی مردم را با مشکل جدی مواجه کرده است. با توجه به طولانی شدن این مشکل و بی‌نتیجه ماندن پیگیری‌های محلی، از ریاست محترم جمهور درخواست رسیدگی عاجل داریم.
🔹
من در آذرماه سال گذشته در طرح
پیش‌فروش سایپا
برای خودروی
اطلس ثبت‌نام کردم
و نیمی از مبلغ خودرو را نیز پرداخت کردم. طبق قرارداد، موعد تحویل خودرو پایان اردیبهشت امسال بوده، اما
تاکنون خبری از تحویل خودرو نیست
و مرجع مشخصی برای رسیدگی به شکایت ما پیدا نکرده‌ام. لطفا شما پیگیری کنید شاید مشکلمون حل شد.
🔹
کارکنان شوراهای حل اختلاف
در سراسر کشور بیش از دو دهه هم‌پای کارکنان دادگستری فعالیت کرده‌اند، اما با وجود راه‌اندازی دادگاه‌های صلح و انجام وظایف مشابه،
حقوق و مزایای آنان بسیار کمتر از کارکنان دادگستری است
. طبق قانون قرار بود نیروهای شورا به استخدام قوه قضاییه درآیند، اما در آزمون سال گذشته، تنها حدود ۱۰ درصد از کارکنان شورا پذیرفته شدند و بخش عمده نیروهای پذیرفته‌شده از خارج شورا بودند. از لحاظ حق و حقوق، قانون و شرع اولویت با همین نیروهای خدومی است که سال‌ها جوانی خود را گذاشتند. خواهش می‌کنم این موضوع را پیگیری فرمایید.
🔹
خواهشمندیم موضوع
فروش اجباری در نمایندگی‌های تراکتورسازی تبریز
را بررسی کنید. متاسفانه طبق دستورالعمل این شرکت، متقاضی خرید تراکتور باید یک دستگاه دنباله‌بند تراکتور به ارزش حداقل ۲۵۰ میلیون تومان نیز خریداری کند. آیا این نوع فروش اجباری قانونی است؟ اگر فروش اجباری کالا در کنار محصول اصلی ممنوع است، چرا چنین شرطی برای خرید تراکتور اعمال می‌شود؟
🔹
از شما می‌خواهیم موضوع
تأخیر در پلاک‌گذاری خودروهای سایپا
را پیگیری کنید. شرکت خودرو ثبت‌نامی ما را پس از مدت‌ها تولید کرد، اما اعلام می‌کند به ‌دلیل نبود پلاک، امکان تحویل خودرو وجود ندارد. چگونه خودروی تولیدشده ماه‌ها بدون پلاک می‌ماند؟
🔹
بنده
کشاورز
هستم و بیش از ۲۰ سال است یک حلقه چاه آب حفر کرده‌ام که با موتور گازوئیلی کار می‌کند. قرار بود برای این چاه پروانه و سهمیه گازوئیل اختصاص داده شود و چاه نیز دارای شماره پنج‌رقمی جدید است اما ت
اکنون نه پروانه‌ای صادر شده و نه گازوئیلی در اختیار ما قرار گرفته
است. به‌دلیل گرانی گازوئیل و ناتوانی در خرید آن، بخش زیادی از درختان ما خشک شده‌اند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/464840" target="_blank">📅 22:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2CgAFNaiAqcH33skuPnh5g4PHh-BEf6mnghJrSPy4S-Y1igRZFlQOMDhNZdokcBxkXX6kUkvxXFAEXoJBViYXUzoNicm1eDoXR4IXEPWb_2_jKHUBcp_tEBQ5GqYRyzGhS90youejRPZbRN8TEAZ4SL2-9OuS1hbRWiieu99dRNrYElK8Su0TTL7uiNA8itjpePRqPj-xlaDKN6mHU9QjZ-OWudTyDiaIwoPQ3_-E3RXXUv-Vlsh0MoGmTGdPtGJCg8asumQMM7_CruPOPSir9PzTZJIEOCzzD9XahMMw8f5Dbef7k-kvHnabNTVXpvRtgzm80omU6svWz0pEfbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مانیتور را این‌قدر از خودتان دور کنید
🔹
فاصله مناسب مانیتور از چشم برای همه یکسان نیست، اما یک قانون ساده می‌تواند نقطه شروع خوبی باشد: نمایشگر را تقریباً به اندازه طول دست از خودتان دور کنید.
🔹
برای مانیتورهای معمولی، فاصله حدود ۵۰ تا ۷۰ سانتی‌متر مناسب است و نمایشگرهای بزرگ‌تر به فاصله بیشتری نیاز دارند.
🔹
ارتفاع مانیتور هم مهم است؛ بخش بالایی صفحه بهتر است هم‌سطح چشم یا کمی پایین‌تر باشد تا برای دیدن صفحه مجبور به خم کردن گردن نشوید.
🔹
اگر با لپ‌تاپ ساعت‌های طولانی کار می‌کنید، پایه لپ‌تاپ همراه با ماوس و صفحه‌کلید جداگانه می‌تواند تنظیم ارتفاع و فاصله صفحه را آسان‌تر کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/464839" target="_blank">📅 22:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc27edcda.mp4?token=pUqxtVG4tWcY0Y3neoOPlePaIUzEAZj-Yv1KNAqhPR87AfG_rk5BaISA1TrVY1K0bINuXJM3o_izCUuaW--MkWaMwW3a9YiCPBOqpMjFKWsZ9MaEa39B7zDCEOs7oCEGDtadIZBSHkKjMHUF18jwbaJCVFznzR66ElQISLcYaTD93dp-GZ_w-OmTvKN1z6eSGXhBYLHQmzfg3fXi847Lwc5SAlOiZf7Tel_YVc6SiO_PcA-nucYxjYswzdEmbW0lG2VdG4TT66_7EK3w6U3W8BsYNGUJXsI9W7lK7ry9Hm-XirWoWhCOWYnLGKmowg67iDyT9k744cZS0sAUuRIkHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc27edcda.mp4?token=pUqxtVG4tWcY0Y3neoOPlePaIUzEAZj-Yv1KNAqhPR87AfG_rk5BaISA1TrVY1K0bINuXJM3o_izCUuaW--MkWaMwW3a9YiCPBOqpMjFKWsZ9MaEa39B7zDCEOs7oCEGDtadIZBSHkKjMHUF18jwbaJCVFznzR66ElQISLcYaTD93dp-GZ_w-OmTvKN1z6eSGXhBYLHQmzfg3fXi847Lwc5SAlOiZf7Tel_YVc6SiO_PcA-nucYxjYswzdEmbW0lG2VdG4TT66_7EK3w6U3W8BsYNGUJXsI9W7lK7ry9Hm-XirWoWhCOWYnLGKmowg67iDyT9k744cZS0sAUuRIkHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«انتقام» شعاری که ۲۱۱ شب در کرمان تکرار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/464838" target="_blank">📅 21:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdvax4oJ0kbPR_hXk41b3vD-HFXdzNnjWqZt3ZGAWJRGuZmSXq_5xc7g6NoDEVqV52GCVE-DSPwaqTbkXKIrePkoNkdUWY39HxE6D8JBpRgUTVyNINtY11Eli3LJmwif0d9XLpsSQzNTRl-ZOYL4hd1Ea9y40FyxPfs6bDZwEWaAfUsl2HvfH47-nQzRfwcPRybs2MQGVxks0Be-ne5fStZwndbKs7CKZrSAaIBXAlIUwhvVciX7a1h92fPspbd452e9s27o1VOZZi8lx9T294kj-csVMSzE1lrHBXjIswbz4LxXnvfLj3TJ5WbQTeLguqtANmzkHctp-hr5vCkl_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXBBpslbdnbUEmNVYnGQec2Um6iIKV7tZ7H2PtTkzyBnKiZ_qwmpKiTXeegUa5O0j-37wGJOhos8OebGSf-z4ud4JBJ98dVvOmKFqRjVHW_O97HgwWhC8auOnAqIrppyi5XeulRskpUcVLjllXVIRtVPEdSq4f3J5JkTh1YJwlTJr6OojSvn_BDGzc_hbLwXpCwkUIhnk6uRDCo1aTwR42lt9s9IN3SETQITzF6HnS-nFZRDFulNn6v4RPQZf1JRSCtV4uR90-kqTy3L3XgTJxpo162jFAqxfvR4LKcVrLwl1bleRbXA7Z_NnBQPUexqr74BWXYeVpEE9LwwdGwkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8u7WZqeVEFMfjhK041t-7K2o2467_Ksg_OwUlpZ9YXiACRpTr4Uc4mcpg7IYDmyTCb5JNB-9HHUkzpXnlTzZuhBv1qLTFfNJbiaE-bstBhSA-z6b0jtsxUuHSNRWMXxhR8KD1Hh-6mpfNUxvzITLTUxGM8bpsOymR-1yLu1WeigfqxIflvcMkNG_8h3_B9nMdYLqwoV8c3dHQw8Lh-oXTrTEV0LsZx7OicWX6r-fuqeunaYRftwiHY7gVJkozrNNMa2ehZa9ojAvEAGcoR9BfNpPjBxINXpe_uGaVjWU4-YvBAX5CuE0BpXFpuS1oy_DUfFWjTTTrp3SwN0j6_zQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpcp0rVv6oOP3t8uBz2D93W1rCUauwDg9r3c2piZSJUyH-bIO7gRGgHrS_1r-pBw77DLoYeaNxJ1Q6gaUi1QcTDcVARiziRnfnwZgGnQwkdgu4n497SUsyH4DCoZKLXqMmjD_2ajLVFrz2X__og-z4KQ-7hAaPTJfR7VJ60MZlZYAR38xRhLJe3FLqrbhiBvh5Heq08IcsTuEAHXWlplidc41J81Gdd36LTE83VNu2rM4YeFhSEP4yZDrpSd5cU-jfNqPbTC7GRkvjd6q2SzmaPTFxSC3UqvtPUAyFQtfkhb9zDVfHCSVDpfCCQ7zcWq2D4xXEbPow6hA7Hl4u5ScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOPFmcVHjtLeUv-CwC70i01QqxdSaVxq4AaYGNtbBqzVMBbwsG-zZyKoR5Td4xd2zOIeI_Y_iuR422TOdQWWtHQG7nIqaQktviGo6dRsr23xcMNDS2l0mzt5v2CEYKbulBh1fd9sx4DjHrWzHXOf1F6FyF2CnSArkpVSi2WhMxbQ0w0CTQNAGmqc-Q66_LEX_oBeP4G_F6F90fF_FsTWCRcujyokrm6rOW8YJyH3AJ2cxkEKlJGUd7sCroR_64yy3TjNkPov2ynvjOSKc1EFq1WS6RCZlo94eo4KnhyC462FQEI5JgUfgfD_T0A-kedZg04CXr5-EGZp1zLM4V1xxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsxA9gAC2cUJPuJMatDXvJlbZRytia2DYhss9rfiOwxUH5zCujhRd20kpmz1fzinrFW-lPW7Zq_PBE7Oc0iEo8i-UUNH5DnIJ3_DJucgB4R7V_TG5nOSKHYMmbwjRpRDbLnDGZLmCvpKF0p7zMy3_-h1uZSfy5b8mpEwwwEUClSbxHaJm7q5sW5bZEmHEk7UfH-U4fLpssjbU2f97HyE7X91FGBCiX_AEgyeqDoXnH-04C7_uOfeU-cUP-KxGnSDv9CPkTtLNARL2ruDd7QnEXUD2gLadpFdkW47rpcnpgpR3qNTF-LuRS-zxKXhs3b9kyedgA5naPwOAgiOvYL7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyC4-zbZ5zv3U4fFlUSPwJSHuzEkwlR960E3_Va2yPwcbI-rFbubaHUlJdWObbqaFUQhaPErs0RNC4m1t8rZCn-O-cXalabsFJdlvFyl9YZHc2EvXrNe8aZDi0-dYbPLVdK--PgA5VL75qlY0UAl1MSxW4bRojz90OTU6xd-1TT9gQ0zzhTeXeRLvnz4xbE8wDxq7oace_iFimXDntV1riCAFr3EjXiLn4cu4TngChhIFzFnwBGNyaFrSAULe3yXARvy3OsWqJgcfA0p7M85Yl2aZ5pLGPY1kTv-hIhcEk8uZAvVk3kIvFNXG8tdid_b0O2HVOXXKdV-8pxOXh4UBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیکر شهید ارتشی پس‌از ۴۰ سال تفحص شد
🔹
پیکر شهید علی‌اکبر گندمی پس از ۴۰  سال‌ دوری از وطن، کشف و شناسایی شد.
🔹
شهید گندمی در اسفند سال ۱۳۶۱ و درحالی که ۲۴ سال سن داشت در عملیات کربلای۴  در سومار کرمانشاه به شهادت رسید.
🔹
مراسم وداع با پیکر این شهید فردا…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/464831" target="_blank">📅 21:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-text">🎬
ببینید
🎬
✅
ورود وزیر تعاون کار و رفاه اجتماعی به اهواز
.
🔶
به گزارش مدیریت برند روابط عمومی و مسئولیت اجتماعی
#تاپیکو
، وزیر تعاون، کار و رفاه اجتماعی شامگاه یک‌شنبه پنجم مهرماه وارد اهواز شد تا در جریان این سفر، از بخش‌های مختلف جامعه کار و تولید و وضعیت رفاهی اهواز و ابادان بازدید و با کارگران و فعالان این حوزه گفت‌وگو کند.
@tappico1381</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/464830" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZm1ObiOiKXuVpi61iTgow9m9cEDk2GNJ3LxjHh5lWG_2aoXenrzY99CKFCXugjWBejzVzO81vmSJsS01eEDuu1Zi7_N8-I53KE9N_gCO-zOi-sjlNgkwrgtUxDE_zxvzE_vXs9ZT2nrYaSUcTaGWlfh8FNU9IX9Z_43qaF9w0in3X3f0waJ-BLDPADQZFZw-_KV4kPNaVfSN8fg_R_VgA88at5dTsD3zPkyMDXmofXEL7Aw8NsdZmtQ6irRslBhkxPK2Bb_Pk__5yzWXW4b4lq0Iqql3wVkwkTxdpEl4OaAD9IurW0UJDMF1vaDvO2_D6QsX6O6_5HUJtrwql4DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/464829" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/464828" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU0BHryJvGRcYHQMZYo1oDoBzPFBWtLj07DTJFemwkYtvm43DnNFXVFBxij5xgtvBS7MqkSBzeZqOMVUJ4Foj9Jj_wPUl_Z1rBerzkLxUBHQAnJhNouZp4-VDwxZ8Mz8chDc4tB2Ny-zLKJ9HsXv_zt3vwnO6kacsKALoe20qzRrTllbU0IYDGxsELDxKffH4F1Ph19rLKMLGpihG_fENdPyZIuvtKo_Ii7By58yknoE7VRryiimyw9Q2ycaSqXWuJVLtj1aAUbiWRAgshx0X1M8kkDSUVogYBcPVCuoRm6GdsiWcM8wLCUwC4uMhDrs2I3hCGs4DsozQoE3MV4G1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دعوای سرخابی‌ها بر سر جام لیگ قبلی بالا گرفت
⚽️
مدیر رسانه‌ای پرسپولیس: استقلال برای لیگ ناتمامی که فقط یک هفته صدرنشین آن بوده  گدایی جام می‌کند!
⚽️
مدیر رسانه‌ای استقلال: اگر دنبال ننگ می‌گردید سراغ جام‌های اسنپی بروید! @Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/464827" target="_blank">📅 21:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb620bec.mp4?token=ZiEHmxWrKXGCP78vOe0gCgpp0KTK1GK3NhRxYMyxtUksd18JUwYOHd_tYQPD0UVjM_1lE9foZie68pBGnSd9m-EgWDwWDla3thOZVpHWlZ3buvwOUiCQ709Z8lidMEefZgYa07dFki80VEcGy0y8hK8Wetr8_utITSDALIxHEsS7cbME4XiJ36p8OWHl_nEV_UpI9hhh0EIw11eIjQN-ZV3jjfm4e5dmp39UoRRc1kvTBTa0Yz5v9iq_FhGM4IZuSquiAO_GP2D8Gx2OwS-DXFmdf1c-tVg9t9L_MIri_kWlvdeFbOw3m9Y0rk9dwZ3gNssSwqSXueA-3jozvO3LkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb620bec.mp4?token=ZiEHmxWrKXGCP78vOe0gCgpp0KTK1GK3NhRxYMyxtUksd18JUwYOHd_tYQPD0UVjM_1lE9foZie68pBGnSd9m-EgWDwWDla3thOZVpHWlZ3buvwOUiCQ709Z8lidMEefZgYa07dFki80VEcGy0y8hK8Wetr8_utITSDALIxHEsS7cbME4XiJ36p8OWHl_nEV_UpI9hhh0EIw11eIjQN-ZV3jjfm4e5dmp39UoRRc1kvTBTa0Yz5v9iq_FhGM4IZuSquiAO_GP2D8Gx2OwS-DXFmdf1c-tVg9t9L_MIri_kWlvdeFbOw3m9Y0rk9dwZ3gNssSwqSXueA-3jozvO3LkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یمن بازهم یک پهپاد سعودی را ساقط کرد
🔹
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کارایل متعلق به دشمن سعودی درحین عملیات در آسمان منطقۀ الطینه در استان حجه سرنگون شد. @Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/464826" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8a74474a.mp4?token=s46zjKT7XR3GLYg3L1b7e87OFdMbx5MMDxHeZIOkqlXatcVeM3-YRLel2QcLpe_szEH3lIDtgQmvHE0Pc2kAHHxFzqtqnQFsdJXzc_ttZy59UtmRJAn9-K9CzV0EJc9pkAaU4DfS-GkxmJ-VawOA5EfLcwTuLQ2NLJXU2wDt5c1JvhtLSEo6WqbZIt3QOVBmiHrFKeI24X_D1uXmpGwCT3AmrGxVVAgD2ZK49OpLtNfPa0LTItMan3e6Ed7hEv15MpQQL5RDQOOxnUOE9mG7gTW_8wkPESRlM6T1vyvpXVfi_Zx0fR3YVFOIX2NGb2PFO7X7wguVvrHwaul9004G04i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8a74474a.mp4?token=s46zjKT7XR3GLYg3L1b7e87OFdMbx5MMDxHeZIOkqlXatcVeM3-YRLel2QcLpe_szEH3lIDtgQmvHE0Pc2kAHHxFzqtqnQFsdJXzc_ttZy59UtmRJAn9-K9CzV0EJc9pkAaU4DfS-GkxmJ-VawOA5EfLcwTuLQ2NLJXU2wDt5c1JvhtLSEo6WqbZIt3QOVBmiHrFKeI24X_D1uXmpGwCT3AmrGxVVAgD2ZK49OpLtNfPa0LTItMan3e6Ed7hEv15MpQQL5RDQOOxnUOE9mG7gTW_8wkPESRlM6T1vyvpXVfi_Zx0fR3YVFOIX2NGb2PFO7X7wguVvrHwaul9004G04i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نام نصرالله هنوز در جبههٔ مقاومت طنین‌انداز است
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/464825" target="_blank">📅 21:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464824">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1SHhftkjm195uLiK79drdStVG6f6SibpLr_vGsff8YbRcuQ7b-BdX_hn7-dN9xtC0Vwevs5GSHW_Fh2iJQfb7rt4gFtbS8TT-jfbjGYVhI1AKfDdAl3OwoTH1mqp5L4fmNjSQiHqSwejO0imxo28_QnSTknLsHn0U9lk72LGBQ1qkjQbVrM5Xa7Yb20cs8MCLT1JPaOdHaepl4zQxs5wDvzC-RvmjooM1S4CEWFFDWf7YngkhyZixcQknVi2vuzVJd9m2lSaiJ5Exiw03ERVMbXXryiVy4Do2oGddeBdG1kX0p3a5bJrg-GZ_piR4e5JGkSG2-7rs0Te_jAKAb78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز نفتکش‌های کهنه را گران‌تر از نو کرد
🔹
فایننشال‌تایمز: اختلال در تردد نفت‌کش‌ها از تنگۀ هرمز، کرایۀ حمل نفت را به رکورد بی‌سابقۀ روزانه ۱.۲ میلیون دلار رسانده و قیمت نفت‌کش‌های دست‌دوم را برای نخستین‌بار از کشتی‌های نو بالاتر برده است.
🔹
برخی نفت‌کش‌های ساخته‌شده پیش از سال ۲۰۱۶ هفتۀ گذشته بیش از ۱۵۰ میلیون دلار معامله شدند؛ درحالی‌که میانگین قیمت نفتکش نو حدود ۱۳۵ میلیون دلار است.
اما دلیل گرانی چیست؟
🔸
ساخت نفت‌کش نو چند سال زمان می‌برد.
🔸
خریداران نمی‌خواهند منتظر ساخت نفت‌کش نو بمانند.
🔸
صاحبان نفت‌کش‌ها ترجیح می‌دهند ناوگان‌شان را نگه‌دارند تا کرایۀ بیشتری بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/464824" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464823">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce62a9d434.mp4?token=HXTtj60ar7UgLA7UmF9Uhmzw-CIcMENHQ2IbIR2zxpo4j3NzbkBH0PR8MUcPuEsv7IVzeavFb2UI79qhgCfqEofFhavLTcBbFrJMXWp0D7d_-QXd-oiAyqhA5R6h2s38J5bljxrehTfVSny0gy8wtPkA2Lq3nqiZFrp8udh-7T5nlUpe2rw1tdAoxJ4yVRUx9sAItE9VUwSKeoxzzKw33QsfmsivG-0mM2N1mf95reT_hYJHEwwdvS0Iul0cLulvEEKDsqVR8oJjtAtfsjJYFZuBHQfy-11kmnrE2O-hG9tTeKn3bRkbsvyzRaPzQEvgEMJVuImSNvrSWXs2txFW7JI3ScMGgYIQLHd1hz_qg6tlldLk6BOrg-GUE0IMdeChpveM2U9fy55Y-Eh_0x7Q4Y_n3E6iu_eZ9yCJXpFoVgusxkrHebwiwf81pv0tc4Tp-2I7J6nXhokk5M_xUEUW9yIR54SHXjm9HX7UMGs07M-KHWxtQf3bvKyCU0o9faMWXxSVkWW28_L7_CrJBNgHB2yYuwv4GZEVTHYv-jxvghCqfrdqWKxlDe9jLq2-AEWA3qSub8rF4qTDB8q_DYus7stxlzOZO5_AYTXsHHjWVekSw0GlGhX0RHFFjKPvGbs81HlGAATHcGtcA8yhZKF8mltU--DgI868-HLCfUNIeoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce62a9d434.mp4?token=HXTtj60ar7UgLA7UmF9Uhmzw-CIcMENHQ2IbIR2zxpo4j3NzbkBH0PR8MUcPuEsv7IVzeavFb2UI79qhgCfqEofFhavLTcBbFrJMXWp0D7d_-QXd-oiAyqhA5R6h2s38J5bljxrehTfVSny0gy8wtPkA2Lq3nqiZFrp8udh-7T5nlUpe2rw1tdAoxJ4yVRUx9sAItE9VUwSKeoxzzKw33QsfmsivG-0mM2N1mf95reT_hYJHEwwdvS0Iul0cLulvEEKDsqVR8oJjtAtfsjJYFZuBHQfy-11kmnrE2O-hG9tTeKn3bRkbsvyzRaPzQEvgEMJVuImSNvrSWXs2txFW7JI3ScMGgYIQLHd1hz_qg6tlldLk6BOrg-GUE0IMdeChpveM2U9fy55Y-Eh_0x7Q4Y_n3E6iu_eZ9yCJXpFoVgusxkrHebwiwf81pv0tc4Tp-2I7J6nXhokk5M_xUEUW9yIR54SHXjm9HX7UMGs07M-KHWxtQf3bvKyCU0o9faMWXxSVkWW28_L7_CrJBNgHB2yYuwv4GZEVTHYv-jxvghCqfrdqWKxlDe9jLq2-AEWA3qSub8rF4qTDB8q_DYus7stxlzOZO5_AYTXsHHjWVekSw0GlGhX0RHFFjKPvGbs81HlGAATHcGtcA8yhZKF8mltU--DgI868-HLCfUNIeoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌هایی که چراغ اجتماع را اول روشن می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/464823" target="_blank">📅 21:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWcyNjg2_5FC9NcreWLnSDZCldYIZ8yfixpk0RjxceB8-ING-qRycaQbPNdSH5urOk06MZT8vsZgatZQRx02oiUCRUKKxcFKvtXVNHBkqt8sVyyJvgZe2z3O_z5NtRZLrIYRmMeiwH63psF9Rms4QRY3msJiPbcPfmZygTFrcZichQi4kpxclLAzsDW9iz8Hp1RfkMY7uh-5lNfdna15bBb6feRcJE3tfOdQtmZkGBiPNq-aU3dp9TRRwD2sik81HgqhqCXWnese10eeR3TJVUrOZIA9_sqqkiQ0-4ZYC5TiMtCfQGdT0trESjBpZHHkEm12KMfalrulYp90dIr16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد دیه: زندانی غیرعمد با بدهی کمتر از ۴۰۰ میلیون نداریم
🔹
اکنون کمترین بدهی مالی زندانیان جرایم غیرعمد حدود ۴۰۰ تا ۵۰۰ میلیون تومان است.
🔹
در ۶ ماه نخست امسال ۵۰۵۹ زندانی جرایم غیرعمد با مجموع بدهی ۳۷ همت آزاد شدند.
🔹
همچنین ۲۰ هزار و ۶۴۰ زندانی جرایم غیرعمد در نوبت دریافت حمایت ستاد دیه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/464822" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usUdkpgpkjsiHSKK9dJpoo0S7XP3NmbmtCeIl_TwoP-sIVrgszZW_17QhM3qv0CL4nJpH6C1HaR4mrbezr3Zgacw3PSGeOwaS8C2YPeW5JLZEzghoHHTEgBrjtAUfsDfefEqj1UjV16GnNDN8uw_7HSHbzR6aACF7QEDqRJkHtnRJLDDABol-wQwDcd-SxJRBEuqjtE25JsDTaayRxcZOuvEt8u60Swulq5toPFdu-3xjhLKE3UYmdGKw8wVi5p4DlXcA512mLQLDabCAch4DhcX-eX1v8MZIO3C-c2BZo9p3r73Ba8PMgMBZKrVMQSAtJv5jnDwiytCRuOwrQhYhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حکم ۱۰ ماه حبس برای رسایی چه بود؟
🔹
حمید رسایی، نماینده تهران در مجلس، در پروندۀ شکایت محمدباقر قالیباف، رئیس مجلس، به ۱۰ ماه حبس محکوم شده است.
🔹
موضوع اصلی این محکومیت، مطلب منتشرشده در نشریۀ «۹ دی» در دی‌ماه ۱۴۰۲ با تیتر «دستکاری قالیباف در اسناد مجلس!» است.
🔹
رسایی در دفاع گفته این تیتر مستند به اظهارات یک نماینده مجلس بوده اما دادگاه این دفاع را نپذیرفته و اعلام کرده وقوع دستکاری در اسناد مجلس به اثبات نرسیده است.
🔹
دادگاه در این پرونده علاوه‌بر ۱۰ ماه حبس، رسایی را به انتشار تکذیبیه در صفحۀ اول هفته‌نامه «۹ دی» با همان قلم و اندازه تیتر ملزم کرده است.
🔹
همچنین گفته شده در جریان رسیدگی، از رسایی خواسته شده بود نسبت به مطلب منتشرشده عذرخواهی کند اما او نپذیرفته و گفته «دلیلی برای عذرخواهی نمی‌بیند و از موضع خود دفاع می‌کند».
🔹
رسایی امروز هم در نطق خود در مجلس گفته: «این حکم را غیرحقوقی و سیاسی می‌دانم؛ با این حال چون یک حکم قانونی است، از آن تمکین می‌کنم و حتماً برای اجرای آن مراجعه خواهم کرد».
🔹
رسایی همچنین محکومیت ۱۰ ماهۀ خود را بیش از حد دانسته و گفته طبق قانون در اتهام «نشر اکاذیب» برای فردی بدون سابقه کیفری، باید اقل مجازات یعنی ۹۱ روز صادر می‌شد.
🔹
برخی کاربران باتوجه به این‌که محکومیت رسایی برای قبل از دورۀ نمایندگی اوست این سؤال را مطرح کرده‌اند که چرا حکمی که منشأ آن به پیش از دوره فعلی نمایندگی رسایی بازمی‌گردد، اکنون و در دوره نمایندگی وی به اجرا رسیده است.
🔹
در مقابل، آن‌چه از رأی دادگاه برمی‌آید این است که مبنای محکومیت، صرف «انتقاد از رئیس مجلس» نبوده، بلکه دادگاه ادعای مشخص«دستکاری در اسناد مجلس» را اثبات‌نشده تشخیص داده و انتشار آن را مصداق «نشر اکاذیب» دانسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/464821" target="_blank">📅 20:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy7K9jm5kozhCwseXrR59HVXQh9qwvBgMAW1sKiPnZNDq1DkVLM62mesFvbXfEZdEVZJzoagIS4DdMfjCOvjnTZyxEbhV4FmXCR79gNC5W4tMJU-Ab4pbYf2YqfiX-0-_Z6_tqNZLi4tRdN7LZAbtZAxs7oLXxF2CkZPSSbAPD7bIfAvzOACUyS0UWe9fRo_bYI7EbsEMtcF6nUN9TeplQR9qhdalpAMI3vt0ko_ovQlZSvfUEZX2fR_zgKPDDdv5iiHA9i-dNgLpn6XJbMtCmD2t9QKe7CsmN6L-Nu5dXBi4HnrJ-TSQX-D_AdMw-CqoR22QDS0wSZx4xQ1Ybh-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/464820" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464819">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eaf9933a4.mp4?token=KbG6yIovxIeoMfRlnlABjpLH7S3GJr3D1QGPna_4q7nE3pDsKgwlIowIBeOFPC_shQr61ik9hvTubuuf8VP7fL1WIjeBZx24wJZARtXrgmKkmkiHwL5omigivVorMlrnSSNKmwtnRigzQLabhx01HSKImlM_i-l_TJgAnnbhDZjlYk7DUdjOzwj_UAiNmdEDImlUki8TmBt-rwpmAbR-wCWyXNrlT66MAic7KcSXHksQzZYyjyYlgK4CthRQtEQF35DZ85Er4jvxXnpW1edM5XoAS9Yht7gzKTNY-A6goAbDZrOGTJL7auVzUfJoNXoOW2fToSDOXNV6ayYi2PQlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eaf9933a4.mp4?token=KbG6yIovxIeoMfRlnlABjpLH7S3GJr3D1QGPna_4q7nE3pDsKgwlIowIBeOFPC_shQr61ik9hvTubuuf8VP7fL1WIjeBZx24wJZARtXrgmKkmkiHwL5omigivVorMlrnSSNKmwtnRigzQLabhx01HSKImlM_i-l_TJgAnnbhDZjlYk7DUdjOzwj_UAiNmdEDImlUki8TmBt-rwpmAbR-wCWyXNrlT66MAic7KcSXHksQzZYyjyYlgK4CthRQtEQF35DZ85Er4jvxXnpW1edM5XoAS9Yht7gzKTNY-A6goAbDZrOGTJL7auVzUfJoNXoOW2fToSDOXNV6ayYi2PQlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/464819" target="_blank">📅 20:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464818">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzXNDnE_n3Yx_AvHUygt8Gi-18QnYv8xY4igqbCZPoKDuoxglHm5YuKHr2jsI-JeqfkEs6lpfNPU-EJBr5NNveI9GrfEeu2Pwf7Cf4uIvJfZq9E8tDQH4MHuoq2B0YuvnAHRUK6UMjKGN0HV5hMMkT0K6zO0jSWDQ4KOZ9D40sihiLiAvSvks140665ndyolO7L5dM0lJFoqmPum9jUthbMTX3vcvLeXeOAeNnv_Aocc0hA0PE-MouEDU5QlxsUrOrHHYVpEesEdNygpuGKLX5K2vwpkYLaoRo-3Hbia08SV-KD-yGIx6FMVVWmB1iBu5YBBTsC-fF8JzpjBTv7BhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: یا بازار نفت احمق است یا ترامپ دروغ می‌گوید
رئیس مجلس در واکنش به ادعاهای مقامات آمریکا مبنی بر بازبودن تنگه هرمز نوشت:
🔸
بنگاهِ فریب‌کاریِ آمریکا می‌گوید ایران کنترلی بر تنگۀ هرمز ندارد، اما بازار یک اضافه‌بهای (پرمیوم) سنگین روی نفت کشیده است: ۳۵ دلار بالاتر از قبل از جنگ، و ۵۰ دلار براساس قیمت‌های نفت فیزیکی.
🔸
پس یا بازار احمق است که نفت را با این قیمت‌های بالاتر می‌خرد، یا دستگاه روایت‌شویی آمریکا دارد سیاه‌بازی می‌کند. برای کسانی که حرف آمریکا را باور دارند، یک دستگاه چاپ دلار رایگان در تنگۀ هرمز گذاشته‌اند؛ بفرمایید بروید بردارید!
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/464818" target="_blank">📅 20:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t68kHMN8hhyAFiYbSk-FxiBzklzqPNfDBPx1GtoRYAJyCXv4s9qePAE-Ytnq8rmofCf4VK7y7jFSXyaEkaw9xgPDR-KgW1Z96fg5GpZu30TcH_Lc8pKs_KmFV21SOVJehzkblDkF73i8Y3yGms4dJsn1Pf-WSuMKID84k9mk2Ft78kDOgVGodC7HgfXEQSDITrEDEBhiygg0L4owITA-2uT0YZI1HT7PLVeMdG-TbTZr_HTXhF0-l3KC7Oy0goN8uM1zjcpjsoUxIhPoD7anbMku1yOSvaJrWTrwUSc1m6E4msNwmlDZsPD8sNxii8rJ4q8HfUVnPveLBwtI3gP3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل مدارک ویدیویی جنایات اسرائیل را حذف کرد
🔹
میدل‌ایست اسپکتیتور: طبق اسناد فاش‌شده، گوگل بیش از ۷۰۰ ویدیوی مستند از جنایات جنگی رژیم صهیونیستی در غزه را از یوتیوب حذف کرده است.
🔹
ویدیوهای حذف‌شده شامل تصاویر قتل شیرین ابوعاقله، خبرنگار دارای تابعیت آمریکایی…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/464817" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c478512e.mp4?token=ip0LCFb1hy67ZT1QEicZaXLIlYuXG4Wr3peTxW1XZcXtRLwS-l-RPE4n3_H4KiLywpMCNoy338yQ2Iwa12c92NlpleuswsIhSIZRWEdE6F7Qz0dpp9gZY5KLayIHzxGfc6wxGWbKYYMDVQUJtEmhmlEEf8FJiRSqbYLRX0zjSt5bgXYCoj2wAKS1odkhy4DEadSU91M5SdD9Z6tH0E3bd78gJWZRKA-LbcMXkCAVL9-dRc-EnXSEAjGZuETfbJQ5tisVyzVQseO9yJ4zued5ls80XMphfDdd9AXeHk1ZU5vMW1FBVc74ziaSYRI3cXgHOokQyaQOVHPJcbos5xNFtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c478512e.mp4?token=ip0LCFb1hy67ZT1QEicZaXLIlYuXG4Wr3peTxW1XZcXtRLwS-l-RPE4n3_H4KiLywpMCNoy338yQ2Iwa12c92NlpleuswsIhSIZRWEdE6F7Qz0dpp9gZY5KLayIHzxGfc6wxGWbKYYMDVQUJtEmhmlEEf8FJiRSqbYLRX0zjSt5bgXYCoj2wAKS1odkhy4DEadSU91M5SdD9Z6tH0E3bd78gJWZRKA-LbcMXkCAVL9-dRc-EnXSEAjGZuETfbJQ5tisVyzVQseO9yJ4zued5ls80XMphfDdd9AXeHk1ZU5vMW1FBVc74ziaSYRI3cXgHOokQyaQOVHPJcbos5xNFtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه گمان کردند شهید شده‌ام!
🔹
خاطره‌ای از ایام حضور رهبر معظم انقلاب، آیت‌الله سیدمجتبی خامنه‌ای در جبهه‌های دفاع مقدس ۸ ساله.
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/464816" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuVnR3x8U7eMZMA5zjimmxwfr7JzojrY1J1l5q0oReqDFQaNrzr0qzXwBLF4OKigo3EOKPg9P28LXDsPKGBn5wpEoER7sGTZsQ4jm0XxAtcbSkxdZNddjnzueCtXMvAVRo2jw_-msmPgAPED5o8vwNf0sCluSXh8d6T0TRDMRr8GEvPZrrPLCaBNOyc8ANWveISyOmjTPexzKBeGT_Xr8VIHLhVNJAExPlcKanVR8HMfzHAGZzFCx3110rAEhgzWe8vekc8HW79rG-QXQ8Ba7tJt1LUQo_MOpnAFIuFOevH92anjoFlH0ansCqeDfKFmdjMaG76UB7cW-f7n6TGQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایندگان کشورهای ساحلی دریای کاسپین به‌یاد شهدای میناب ایستادند
🔹
در اجلاس «کاپ ۷» نمایندگان ایران، روسیه، قزاقستان، ترکمنستان و جمهوری آذربایجان، ۵ کشور ساحلی دریای کاسپین، به احترام ۱۶۸ دانش‌آموز شهید میناب و معلمان‌شان از جا برخاستند و یاد آنان را گرامی داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/464815" target="_blank">📅 20:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTBwE-efd3_Z81BJ1LUOoYjxrJNZYK9mCUKbZPwWzT8Pj0FjJTd0u1OeBc-ty6qUZ9aWPOiF7-VpxXqErYYSvn_-7ytiyBDZIuWoT3y3mPjkdfovn9ceuOFZS8ER7hG-HUYUypDm40PTgxvkQ5r6KJoJ1xNHHq5G6S_gpIs-mJI7cFET6NIJ4FEKs8U__1GdNQIQlaqMIYsq47Zgzzbf6hD2ncNtTqg8TqnmhfJKWKDjSm4-yx3VwVcT1iH8DWrZ4gGBmeLHKaQ0_6GAr5Rfbd-svLRrPB0pbydkf6w0lN-3PRmJ8sPTk1VnvH4Bz7DQlPpLqAAUPefEwV3ZrSsMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازهم تیراندازی خونین در آمریکا؛ ۲ نفر کشته شدند
🔹
در پی تیراندازی در یک زمین بازی در منطقۀ بروکلین نیویورک، ۲ مرد ۳۳ و ۳۵ ساله جان باختند و عامل تیراندازی پس از ارتکاب جنایت از محل فرار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/464814" target="_blank">📅 20:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYq9TvM2c241YEgB6HORbpDUVNKY_m6o5qpZOgguvT44umq1DVAv6dq0NjEE68_MZWzS11Y2fMEp9lF5OjalQna9fllJQKp8OjTcJzAyDY0n1etxfb5Kgv6DoHuHMSAOVUM1IB1tqb4M760Z0KieU2-c2V9jfQ3pjnfpyyndsYqIMiO02art8OBKHNKsudlhEcb1Mo3lkPBdqXF3XMvDO2yiYTuzFjed9-sURhWOMcFcTP2Sws64O34XBK6mVpFAC23KiPsHo3f7quc7WtBq9Bxw7wclUVHCQYdD1CvE0YHLqdkKrrYpfEoN3o2N8qPoThdZip673yXYS2kYFPiTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان جنبش نجباء برای تحصن در مقابل فرودگاه نجف
🔹
در ادامه واکنش‌های منفی به تصمیم دولت عراق در توقف پروازها با ایران، رئیس شورای اجرایی جنبش نجباء خواهان برگزاری تحصن گسترده در مقابل فرودگاه بین‌المللی نجف اشرف شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/464813" target="_blank">📅 20:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
تصاویر منتشرنشده از لحظه شهادت سید حسن نصرالله در ضاحیه لبنان
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/464812" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a87c72497f.mp4?token=Nrr3e0i8ye82zPycGXCy7VnbvIr7mcNsZKO5uiEpms78XUMbf5aOW1NN8LtcGY5eADqsRMm8XYlbNHdO8LNhq1HY4R4zgelwAsy84x-nPbCx7f5GAwE1xnW-I9Tgr9YXN5HH_mS2X_v3CdJnh9U6LxlMQqubfG5YTFQ2sY1bQCcGljxy7v4j9DfnVtt-vNHTqWrhz-Flak4x0HU-IaB3ujb0b-6jYN12_DrOg6YE-VaSbBQyh6aT4BpqPpMT5Jv-zDMUhaEPybtwkpBFkocsazOfgJ7eqf6EC7JheIo8_-pkkDWf8vrp4BKjW-_NgJGDvDN0rRmJ1dvs7XevKWpSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a87c72497f.mp4?token=Nrr3e0i8ye82zPycGXCy7VnbvIr7mcNsZKO5uiEpms78XUMbf5aOW1NN8LtcGY5eADqsRMm8XYlbNHdO8LNhq1HY4R4zgelwAsy84x-nPbCx7f5GAwE1xnW-I9Tgr9YXN5HH_mS2X_v3CdJnh9U6LxlMQqubfG5YTFQ2sY1bQCcGljxy7v4j9DfnVtt-vNHTqWrhz-Flak4x0HU-IaB3ujb0b-6jYN12_DrOg6YE-VaSbBQyh6aT4BpqPpMT5Jv-zDMUhaEPybtwkpBFkocsazOfgJ7eqf6EC7JheIo8_-pkkDWf8vrp4BKjW-_NgJGDvDN0rRmJ1dvs7XevKWpSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: غنی‌سازی ۶۰ درصدی مگر غیرقانونی است؟
🔹
ما اورانیوم را تا سطح ۶۰ درصد، با اهداف صلح‌آمیز، غنی کرده‌ایم و این اقدام در چارچوب تعهدات ما در NPT قرار دارد.  @Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/464811" target="_blank">📅 19:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464810">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec0e89a4a.mp4?token=g1QoIr85fJFi3-aReJOuEUc_zY2YwVCViko5lB6FkpLKpEs7QJJNq2nU9n2DsmHhlAQfuAasy_zwgYT-oBO-Kn8JvdJG4VRtpqLbza2DYQrz95KzuUHh1juiucd-ooApYRQkVht9Qp8yp3lHq3m4uCT1530i7Z6ZtA75cPSuD8oGSF_bQ32i6X0J_CGpH3yB-WHVetn1SRo4njPlyvQUqUEGTdHWEpiM22qcgGF2teRzoapLUGgwkeYShYZmsVOblgLh_39z7qyg36JpguFmxmoe5R-oXXmiimj3zxkWFeg11qoOyjShAJkF8RRLMwswlxWFaOP_OZls3YCao60Gw4gAbFNTF0f90EPrtznfj2P1m1ZTDPt6IOWSaPP9K1P3ZA1x1GQyb46AhmDJENm3nrMe3J2ZCSU2dADjAU1toiC7RJhklW0xw64aC5SkSrtTsUIm1yb65JR7ZlcKMweFG844CReUm30e6MqAdciHvOJkbYx0Taj6GuOvCAhkrBY2l43FEcSrv4kSAvylTKuraVJY1HJ-u1fik7tipixwXInALnaSbxxhuefbFgEWC9pvUeiRvahFoaWf4VvmMIFTpkhHKRS3h4zMkQ4-bQ8ep4AybRDdnq1i0MWqYYUYWc6wiJjYswIBXB-Gb03hGp2ydgGpI1DvkcxdHloM4-qowlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec0e89a4a.mp4?token=g1QoIr85fJFi3-aReJOuEUc_zY2YwVCViko5lB6FkpLKpEs7QJJNq2nU9n2DsmHhlAQfuAasy_zwgYT-oBO-Kn8JvdJG4VRtpqLbza2DYQrz95KzuUHh1juiucd-ooApYRQkVht9Qp8yp3lHq3m4uCT1530i7Z6ZtA75cPSuD8oGSF_bQ32i6X0J_CGpH3yB-WHVetn1SRo4njPlyvQUqUEGTdHWEpiM22qcgGF2teRzoapLUGgwkeYShYZmsVOblgLh_39z7qyg36JpguFmxmoe5R-oXXmiimj3zxkWFeg11qoOyjShAJkF8RRLMwswlxWFaOP_OZls3YCao60Gw4gAbFNTF0f90EPrtznfj2P1m1ZTDPt6IOWSaPP9K1P3ZA1x1GQyb46AhmDJENm3nrMe3J2ZCSU2dADjAU1toiC7RJhklW0xw64aC5SkSrtTsUIm1yb65JR7ZlcKMweFG844CReUm30e6MqAdciHvOJkbYx0Taj6GuOvCAhkrBY2l43FEcSrv4kSAvylTKuraVJY1HJ-u1fik7tipixwXInALnaSbxxhuefbFgEWC9pvUeiRvahFoaWf4VvmMIFTpkhHKRS3h4zMkQ4-bQ8ep4AybRDdnq1i0MWqYYUYWc6wiJjYswIBXB-Gb03hGp2ydgGpI1DvkcxdHloM4-qowlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: سیدحسن نصرالله نماد مقاومت برای آزادگان جهان است
🔹
شیخ نعیم قاسم خطاب به شهید نصرالله: شما پرچم آرمان فلسطین را درجهان و در حیات ما برافراشتید؛ فلسطین همواره قطب‌نمای ما خواهد بود؛ آزادی سرزمین ما همواره اولویت ما باقی خواهد ماند.
🔹
شما…</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/464810" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464809">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06d01b5ae4.mp4?token=i3uJihkR443VyUZlzjqeT9axqFKry4y617R0OJ1F5birej30GYXKsuYLUO2k6ED2a-1TFx7gb5id0SFkk3UPoWY1UIwjo-ox2wNnmPgOurMWmGoSiK4Q9x_nO9hil0Gzmp8tIxcnqwvpHlZCZlsc8Z6vh-uYynxpSjUBEnYEXk5Kv3YTxO2ntA1ubuGlZPFR_Hh4CcIhzsTg8xtVF22CZmm27Rd06eOUO63gJ4880VTWY78B9GlYAV6reMOvirV7ZSgfljS3RedZNjd9RPJzuqFgQ_jW68tAm2-uFeFR3Fod9AKsVoIuOj4gzkH3P_rWvumO_FOBUyobvYwc9A5AaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06d01b5ae4.mp4?token=i3uJihkR443VyUZlzjqeT9axqFKry4y617R0OJ1F5birej30GYXKsuYLUO2k6ED2a-1TFx7gb5id0SFkk3UPoWY1UIwjo-ox2wNnmPgOurMWmGoSiK4Q9x_nO9hil0Gzmp8tIxcnqwvpHlZCZlsc8Z6vh-uYynxpSjUBEnYEXk5Kv3YTxO2ntA1ubuGlZPFR_Hh4CcIhzsTg8xtVF22CZmm27Rd06eOUO63gJ4880VTWY78B9GlYAV6reMOvirV7ZSgfljS3RedZNjd9RPJzuqFgQ_jW68tAm2-uFeFR3Fod9AKsVoIuOj4gzkH3P_rWvumO_FOBUyobvYwc9A5AaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ما کاملاً برای احتمال ازسرگیری جنگ آماده‌ایم
🔹
بار دیگر تأکید می‌کنم که در برابر هرگونه تجاوز جدید، قاطعانه ایستادگی خواهیم کرد.
🔹
ترامپ در جنگ قبلی خواستار تسلیم بی‌قیدوشرط ظرف ۲ روز بود، اما اکنون ۸ ماه است که آن‌ها درحال جنگ هستند، بدون اینکه…</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/464809" target="_blank">📅 19:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464808">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2db84a86b.mp4?token=rkDkullrgzR6QuGqn0Iia_DYVjpDkQuwwjANchj7_w_NkZZkHpzICExS7YyGPpRgkGAJC3dvUMNUAuyf9oYTs4bi7Fv9Z7MRT4yQHjecd-JHOZYZZsICV7f1li4Kph73jTePNutXFtdwICKBtwSXcIc8Xhl7NXBuNupGdKD2wR414eK1cO75WAKVbH-rHmI-tGR0GqaOCeoeZ3sbh-W2HBa548IJbJ91_hlcyt4LVpBgrLaw0m_A8h_4jReoGhd-QHxg3j88dN0fQKj7SKwpA5rX0X44o0AMg3PsKJpWLKMvspCKESfMeALAbBUU15-t7_t_02pORT7XYZ1zrRPJpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2db84a86b.mp4?token=rkDkullrgzR6QuGqn0Iia_DYVjpDkQuwwjANchj7_w_NkZZkHpzICExS7YyGPpRgkGAJC3dvUMNUAuyf9oYTs4bi7Fv9Z7MRT4yQHjecd-JHOZYZZsICV7f1li4Kph73jTePNutXFtdwICKBtwSXcIc8Xhl7NXBuNupGdKD2wR414eK1cO75WAKVbH-rHmI-tGR0GqaOCeoeZ3sbh-W2HBa548IJbJ91_hlcyt4LVpBgrLaw0m_A8h_4jReoGhd-QHxg3j88dN0fQKj7SKwpA5rX0X44o0AMg3PsKJpWLKMvspCKESfMeALAbBUU15-t7_t_02pORT7XYZ1zrRPJpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه‌شنبه‌ها روز بدون خودروی کارکنان دولت
🔹
رئیس سازمان اداری و استخدامی: به همۀ دستگاه‌ها ابلاغ کرده‌ایم که تا حد امکان، روزهای سه‌شنبه را تا پایان سال به‌عنوان «روز بدون خودرو» در نظر بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/464808" target="_blank">📅 19:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSFhawOydXIoCSQvGYERSrIEvkf-vi0FLkm4O9Q4hzAdruxTCrRxY-ruRJNrg2Oi5fUcTW7IR6eDAQn7MueNfIuhhO07vRQIS6deLufil37AqFOPNUpNNOKz5GnvD0Hyx0Na2ezTyhvWPPKzwCj_FHvpw1Hd7kDVVYgDnxxzFCKvQAACwXatIl_fzgeJPsKkqO9VnYmuvKB_sfLSa0EDsJJa1rxQ7TH4P-g-lBZCpWXtECy7V0_JIjosOHpeB4tEw7YOlcOyeXBKTEnvursJTX_hAPuAsRj_MVnGh22dM_NC4cW4q0vg_7fRsUSJkBU66hSSw8C4Oru-tASHljPcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NO90ANuqw831kpmdpqZOPk4ri3glu8Ti7AYL4n3EwUiqjQsTn2-bVAuuwECMC6wCEvrY310fEj6GD9cHOWXriQ3oS0I4Vk6sJBZBXn-lwT5_W-XsAAfNX6Rk6cRyKoWSfj-fI-aknSrTloggREa9lTa1ci3mvqayUbrF3ozHME_293ABEeMbXSgUqvGRt13lmxy6iL86g-XkyTu_IRrcxWWigiXJfOCfyaG0xpKdnZtjsN2CMt2V1eaGk6Ol-Nn6lX_AEnowBnzvbs4bwii2OtDzO7OwfDnF0XVYkdXp4EBADs3cy24obGaWj_aybP54YGxCu37hhUmYMUfu4ZllkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEnwcuJBfRtoZNPJ897CeGCQm8OpULagnlKN0SXZJA58cEam7xFQZFNUJnuzzPbF9QlNX_CMU3tGxAL9Q7l-SGJ1RVTYiUjDhOjxTDgnfjGcVLT-IJzUWxnGGTSIB9fXyoDQnr26utApexQtp8q1HKcqtMpmANwdciz4l-h9gnrQkNa4DmrAoDQ7kn1R5-dxtceuTupHiWGO8OPsKXYELb-4UIq2Ydt0HUqJCB2siqhzjpBHpG_C5p73WCnkGtMkwxAcAZwteutpc4t5NFfgpMWo0f5eCybW6NvHtNYw6Ns-hg6Tk7KOQQQYYdm7_BmqFbWJMJ9w62bd3VlPZtcEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaTA7M98pIxAPmjLxkLFWWK4WKTmB9oeJUZKz7Yps1nYNqTYxdU1OsjfhCnIbX2-vdkKa5Xux_HpDcZOYAufDJfePoBmQgEKlO02bu9fG9aDy4H4EAdfDqD0hYzI9L2NDLf7C5Ik_YP5ftFQj9toSK0DkhiTwbfTp2emKiaD-NaM48rriCVbIpq82ATRKDCH_kyXuIiRzmjmXBMWVHFvcnbb89GPyUr7nvGjAp5HJGqia6bSKbx2gw_i4opkjZWa-H4nI2xIGNtqjVueSM8zAAELtBxHEEpsDszoA-GRIWXvK5d-i_WkaBY38_D7vhh7WLc7p6ihZ3Wt8FzAmRMigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0htXfwmSJZVmDt3fnvJQ_v7czqcAIY-65senQIFD6ta95CVPAL-AijvksZsQfXOxfnQi1sKiJ8Pw1wqdy4fl-EnYEEr37uw_VvDoWKpICOXMkejdRUSy0b0Oa9M5C_knphUN1vseheCZqws-W8mvy9Cg4Lv7zJFt9Ek1CCevWJUz3SGUwUCoTDx7n0HrMHz1KdB9ld5mmZt2epzlTQmLt0o22dUHVQvrpIGiApYDV4V3Rh2FA01rWuwwSH7Yr4TWFRrBU8h3i__FulNgYdOwT03Yx63sO79zPkt-ZddbVfQD54k9nO5BqwrybACUP-lMh9DjnCLjp_woZwQXKkTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cr1QeuSTLtfoGNnP3T7JS65dlJ4KzZsb0Y_EgwD3MJ7lCo_RHk5wHdHSY733t01LxteQHUa94EevWu_mXQZzCuhK2gcQTE3QrL5Kbu7A07YxrVmrzVbI2rpmI-1LYINLVgEv_gencIhIPkYZcJlfBm6FNY5ltaNqKFnWP9R2u-suQ4VtK8IJaEGEtyWtw76wxt6xmbD_jikmVERGVffoAaL5Z-T5OR5vn5Q4VOeQPWzgKKvnsmf1Ppf-NQlOu12kEaK3djQyhUv8cly-nol1cMbAUwj9oEE1vvWyqQQRaO2a3F3_Tf90L09ZXNhEviSKHXPfO37mdT8enSNs9plpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T97EjFDVwG5OyuO-ZoP4zGlP3vhUmtPip86uYE5b5azsllDvqTKuqLVgXeyr3GXOZHBN4Bm63LeVJnHdDtNYvpw23DiVHX_h64CHUFkQMiD4wrxQCl0Utod-nkIYkAtoH4Ni4kSwLVHGNFtkPszezb06feauZvRD9wj5kmp76MNcbXBGAH0dW3SXbMGKa6RChZis6bgz-EdjZ0b837zNjJt6VfMOTw3eaxdiDaI51oHlukKSmj2G6HWLT-phjgS8wbnzRpPMWGOZGnLg6hEYiQKfmq5lMjkyVMEk7tGJNJT-BYqHhHt5ecLpRmOT4YirE-iFliVHCzk3L_e3oICEpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه رزمی فرهنگی عملیات رمضان در اردبیل
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/464801" target="_blank">📅 19:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj4Mrm1N1VsTCzGMyYAnoHDoVPu8fcZoROw8PdYge7L7FDUdM9lcgDR7ffou_YI4excj44-vxWg3JyypKMJBs8VY4PBuy_ubVNsKRB0v-9oxbyrFrIiXSfWZVbQ1-w7aDZejgwxykYqyCLcUCvW3uAh4VNdvzpPRxAsg1azuSsf-BJ93MLFI5QjSOoqxQodwehAJqjtilzvwaWKwm9TqutpDSNVKb5bcjvu3AgDgAFyA-2uq0cK4C3z_jkhidtaYVzxs5dUALBeNcWRJabz1QG_Z0DVuesYTiyqglnaTpfpILR7So-Z5mhDT29bUcpaaBiAwo0M39dY70UXaV1yfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج جدید شمش طلا سه‌شنبه برگزار می‌شود
🔹
متقاضیان تا ساعت ۲۴ دوشنبه ۶ مهر برای ثبت‌نام و واریز مبلغ ضمانت فرصت دارند.
🔹
مبلغ ضمانت هر شمش ۵ میلیارد تومان است و هر خریدار در یک هفته حداکثر می‌تواند ۲۵ شمش خریداری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/464800" target="_blank">📅 19:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/877db700d7.mp4?token=EKcsjl8tkXiK9b0kUWc7jOMb-tQN8160zkkC-sLop5lZ8Xyn2D_1XZvRIf_JYSYHZssBkK_q1BQWlaur0pXHmekkQH1etlEu-gVdFaizC2kKva8jyegCQqhiQ5ILwGQGvhdTMAv0TKBwIKthV0Kq6AlNEO5nlbpCk_p2ALGU3E08cXMtT1x2SCYrp42dI9EMWvfWXvHIoWoWLGsLRUETGVd_qZXNMs-UbEAKZMystQrfwRsxBas4iEvo2DPmp_V9OH0ik9lro0P8DpcU2RqiEbU9BvqExAgyxk5sX9x-nAT48ao98CxR9mG6Mv41SInQCpomB9XT0n7wC5XQDxV4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/877db700d7.mp4?token=EKcsjl8tkXiK9b0kUWc7jOMb-tQN8160zkkC-sLop5lZ8Xyn2D_1XZvRIf_JYSYHZssBkK_q1BQWlaur0pXHmekkQH1etlEu-gVdFaizC2kKva8jyegCQqhiQ5ILwGQGvhdTMAv0TKBwIKthV0Kq6AlNEO5nlbpCk_p2ALGU3E08cXMtT1x2SCYrp42dI9EMWvfWXvHIoWoWLGsLRUETGVd_qZXNMs-UbEAKZMystQrfwRsxBas4iEvo2DPmp_V9OH0ik9lro0P8DpcU2RqiEbU9BvqExAgyxk5sX9x-nAT48ao98CxR9mG6Mv41SInQCpomB9XT0n7wC5XQDxV4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: استخار‌ه‌ای که در روز بازگشایی مدارس انجام دادم بد نبود و اتفاقا خیلی خوب بود
.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/464799" target="_blank">📅 19:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af748ff1e1.mp4?token=PRUcxXaYI9yfFtM1eQI_mzKbJT-WwOXLVfoo7PcVFi8wp-dTGqQS-W6_HYcMFvzlmkcTznsWN0QtUsmWChbLFZrK-cv8RlCPnfoW858uFtqThSf02NpMUTaY9Y1z3zMNYUf0gqTyeyihjEilIwpinK0jduh8ifpqGFzOEMLWHjjJsfOFXDiuq5GTe8-I8-E5yzFSCNzEQ8h3hyDrPVkeqf_R5oB036GAXiBLWMSDWE9GcIw50KRDcJosbJiVY9P_Cx8RQ-lNwHoJUwsKLk3zkDx8ub-r0JN9NKUFasSrDmFq-l8js6Gg_wxNabvGSuqpv-8zJudIWkPXlVGGrHQEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af748ff1e1.mp4?token=PRUcxXaYI9yfFtM1eQI_mzKbJT-WwOXLVfoo7PcVFi8wp-dTGqQS-W6_HYcMFvzlmkcTznsWN0QtUsmWChbLFZrK-cv8RlCPnfoW858uFtqThSf02NpMUTaY9Y1z3zMNYUf0gqTyeyihjEilIwpinK0jduh8ifpqGFzOEMLWHjjJsfOFXDiuq5GTe8-I8-E5yzFSCNzEQ8h3hyDrPVkeqf_R5oB036GAXiBLWMSDWE9GcIw50KRDcJosbJiVY9P_Cx8RQ-lNwHoJUwsKLk3zkDx8ub-r0JN9NKUFasSrDmFq-l8js6Gg_wxNabvGSuqpv-8zJudIWkPXlVGGrHQEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق در اعتراض به لغو پروازهای ایران در بغداد و بصره تجمع کردند  @Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464798" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19cb2f3565.mp4?token=gxWS4T8BwljkaZneb3EPQtINxEbKsdqSdlRDW8eDhL3cbST_vHCFgWk2nAgH6V0Jo9Vy06A_yLLAPXDpFwnhOagRZqTWEGxWtKoZgYGbnE33h4ghdps58m8GTz2t5341wAYfXv1i4Wptr8-1t0PM9N-eZyK9WYQPVVPzewxVLteiYO5W80rjFSSSE-UTs3F09qBkBPv2_VzemvbUs0ZP3h6cJ_J7eepnjnlbO_PvD4WdeEYNKPgoECjqyrsEt0nSg3QsJMjp-QmQnjYA7OUmqLKCoqkh_isQLESYDooqZEFco-jHAjV8vbn7S15fYpNSFZRa38iPoaAVFByha8GdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19cb2f3565.mp4?token=gxWS4T8BwljkaZneb3EPQtINxEbKsdqSdlRDW8eDhL3cbST_vHCFgWk2nAgH6V0Jo9Vy06A_yLLAPXDpFwnhOagRZqTWEGxWtKoZgYGbnE33h4ghdps58m8GTz2t5341wAYfXv1i4Wptr8-1t0PM9N-eZyK9WYQPVVPzewxVLteiYO5W80rjFSSSE-UTs3F09qBkBPv2_VzemvbUs0ZP3h6cJ_J7eepnjnlbO_PvD4WdeEYNKPgoECjqyrsEt0nSg3QsJMjp-QmQnjYA7OUmqLKCoqkh_isQLESYDooqZEFco-jHAjV8vbn7S15fYpNSFZRa38iPoaAVFByha8GdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: دلیلی برای بازگشت به مذاکره با آمریکا نداریم؛ برای دفاع آماده‌ایم حتی اگر کار به جنگی آخرالزمانی برسد
🔹
در سال ۲۰۲۵ وارد مذاکرات شدیم، اما در میانۀ مذاکرات به ایران حمله کردند.
🔹
در فوریه ۲۰۲۶ نیز پس از پذیرش پیشنهاد مذاکره، بار دیگر در میانه مذاکرات…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/464797" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJ4LihMVN2b2T7hmtxErW2zXmy8lki8TiMW3ZK8m45H3L8SEbmmuoImb9-OxKTMmh7iI61d-YnTPJidcPpcEIIrx-yKAEk79DE-zaQbGOQZMxsh9JMByPSRBlFSWAYbWOEfcpl8tb4ZT0dy-omYnY6wlh-cuHwvSsW31AuTS0ZkSEWXXvNRe7mj9Ie30p0fi_nTuwsTJvoI_dWFkiFwuzQN685Kxv20pD4YK8KhE2u0TBe6RzNfI1F9ISu0_sEyts-Hi6O-i6k5-FwqIEmwcDV-1D0bPKqOIciJl3qawICDvO6JCynJBdN6PUXBbKE6xdWw-ofClyXHs1S4cJ97HBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1IBhH06_xELd6JB-uuFYkkdu_5ixDlB1XIX0LJspD7kXT8jLaWOT_QFq9FZHgH64SMkswMK77r_KKjtCPMOJptyOmo2Mvi5IFvh5sYcYZo8QcBnZ3KObifDqlMzD-7y8NRwLkP3CP1LWck5GBVVn2dY4vB1qzycIu2MB5nc788Bbc7UoX3OYcuBKMat2w2KMiJAmXIdKUX7CcaUB-1IKjWA-Eoctd14ouuEc6kzucWUQYK3KFppIQ8LIp1fGNGwfpt3HiRe2-CzamvNzQeig2VsjIQm8_MV-eMfd4LIgXlEsh_qX-TRsQkx28HdnhhxYi2NLhsB6SNViZ-Rc2Cnmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رئیس سازمان لیگ: طبق مصوبۀ هیئت‌رئیسۀ فدراسیون، لیگ نیمه‌کاره قهرمان ندارد
🔹
باشگاه استقلال درخواست اهدای جام کرده، اما هیئت‌رئیسه در این زمینه تصمیم می‌گیرد و من و تاج تصمیم‌گیرنده نیستیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/464795" target="_blank">📅 19:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5267bbfaeb.mp4?token=cskT57G8EP2Yb4U5FOIsQqMiFtqINE--MUK6CmpplBerWb3XUvFbbRVG1Nh2RDBiB3g0ZmLfU5ksGfL6Kz0XVcB214_oKU3JeIJ_LMeeMXZa7PA6LwMYwc-dfgyDWU20ngaxouDyRKQxhH7Bs_GFwT6qk3afHBNIGeZXgBM-bF8Jz1H_z1QTv19tcF3ZcNcKqFwSzz9-EMxboyg4nlzae0RyLb8gYJlamyW0b9re7X21s1KXs3nTOXm-lM-hANjDbGf0csvMyFrlLZHpZdMXl7foUSs2vtEiHolvY7AU2oX10lSi1WteaixI90iMHsbXzD3xnc788fDy4_3F_CehFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5267bbfaeb.mp4?token=cskT57G8EP2Yb4U5FOIsQqMiFtqINE--MUK6CmpplBerWb3XUvFbbRVG1Nh2RDBiB3g0ZmLfU5ksGfL6Kz0XVcB214_oKU3JeIJ_LMeeMXZa7PA6LwMYwc-dfgyDWU20ngaxouDyRKQxhH7Bs_GFwT6qk3afHBNIGeZXgBM-bF8Jz1H_z1QTv19tcF3ZcNcKqFwSzz9-EMxboyg4nlzae0RyLb8gYJlamyW0b9re7X21s1KXs3nTOXm-lM-hANjDbGf0csvMyFrlLZHpZdMXl7foUSs2vtEiHolvY7AU2oX10lSi1WteaixI90iMHsbXzD3xnc788fDy4_3F_CehFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب چگونه چرخ صنعت پتروشیمی را می‌چرخاند؟
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/464794" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVeHoVZBfsUxhp5jaUgNRPvTUNXEQrUIuCVSdOTzEaxXA1Cnkio-g70oxuUJWjlG6Me1zloUkCLFu4qaGQVlku3T0NcROBL7BjEukk9QGA76ICYOOhrueO2S6FDwjsO3jYUdFFDSNLKyLXsXt_iRG4_86osOBrHWufKeHL5DQ_nf-dV8cCeggPQ39jc04iW3dTol7RpnciWfJInYRDVZnhlSCArbCjckAXAlY0lFtPoDKclLk1eusv0eEQp91bSyjl4BaNPlgJbdtw-V5CbDGcAu1Nf10p7erWowX6wWFl0TmAxtszm3KoJmSlseqyh8x26csD31Qm4g98N2sAl3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: همان دشمنی که در ۱۸ و ۱۹ دی آدم کشت مدافع حقوق ما شده‌است
🔹
رئیس سازمان بسیج: دشمن در کشور ما اقدام به کودتا می‌کند، سلاح می‌فرستد و مزدور می‌گیرد؛ می‌آید در ۱۸ دی و ۱۹ دی آدم می‌کشد و بعد می‌آید مدافع حقوق ما می‌شود.
🔹
اعتراف کردند که در ایران آموزش دادیم، پول دادیم، سلاح دادیم؛ همه اینها را به جان مردم انداختیم و بی‌ثباتی در آن کشور ایجاد کردیم؛ اما مردم ما آمدند و در عرصه امنیت از کشورشان کردند.
🔹
جنگ زمانش محدود است؛ هشت‌ساله، ۴۰ روزه و ۱۲ روزه. اما روایت جنگ گاهی قرن‌ها ادامه دارد. بنابراین روایت باید به گونه‌ای عمیق باشد تا با گذشت قرن‌ها هم دچار تحریف و دچار انحراف نشود.
🔹
دشمن می‌خواهد با روایت خودش قصه بگوید و مردم جهان را به خواب ببرد؛ ما با روایت‌مان ملت‌ها را بیدار خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/464793" target="_blank">📅 18:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i__Hj1FRQgOnRvHTeK67Md2yQsjLdlcULMveUNg7A6wFddgLnMVEWVPGP46K71cm1wLcb8Yn8-F0DjfzamdzPMR-gMMQcmL_RtbgXVW4x_iF1kSvsdNhul482liC52x27-sndXpF_pVm1clWsy8e4dL4pBoldAnwWe1d2-5q1PZP7wKvW1nJaQDM_V0r3xaWLFrXjKl4nOVxcgSCoFHnlzDVpkg3NBlH3uTpmz64sZ8wXlMkZJFtzaSh5b0b2cz6GLTuNpl_aYcxz6q4iT5qThNdk6hBqj_c9wUVGhAavb43_l3y74bJe33lSRoQD0f3MUAyqfYduA4gzDVkivcWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی دیده‌نشده از دیدار حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای و مرحوم حضرت آیت‌الله العظمی شبیری زنجانی
🔸
رهبر معظم انقلاب، حضرت آیت‌الله سیّدمجتبی خامنه‌ای، نیز در این دیدار حضور داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/464792" target="_blank">📅 18:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551a5a85a5.mp4?token=poO7XPtfLFtDX7zSE3pM_JVdP9i2zXuSGG0kBbm49zABTRik2Wc_5M_N_jPXAgCwdFlEp3XlNBM9WqKkZuW9rvxgJx7-L6hFLOdbStQ_CmZC99VHaseh2KyMOihw5_9xoUH7h_uNOsUhhmywOpuT-72mrYzE4fGc6qVFPiWTGNytB4TJPXp9Kn9YSJ3naezX7W89PA7BIe65lzb6Krd20dH6o9Vh0Aa_Gu2kU6XlJAFUo9DVxZ08j037D1ercpdKnfiKufodeHk7RHpG0vENzMf-rhGZrc84OO2lUH5zcNIi-x61SEAG3jy2maHx1LsEAcAbeEDwIdDG35FCmWEsJaj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551a5a85a5.mp4?token=poO7XPtfLFtDX7zSE3pM_JVdP9i2zXuSGG0kBbm49zABTRik2Wc_5M_N_jPXAgCwdFlEp3XlNBM9WqKkZuW9rvxgJx7-L6hFLOdbStQ_CmZC99VHaseh2KyMOihw5_9xoUH7h_uNOsUhhmywOpuT-72mrYzE4fGc6qVFPiWTGNytB4TJPXp9Kn9YSJ3naezX7W89PA7BIe65lzb6Krd20dH6o9Vh0Aa_Gu2kU6XlJAFUo9DVxZ08j037D1ercpdKnfiKufodeHk7RHpG0vENzMf-rhGZrc84OO2lUH5zcNIi-x61SEAG3jy2maHx1LsEAcAbeEDwIdDG35FCmWEsJaj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این ۳ جملهٔ آمریکایی‌ها را فراموش نکنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/464791" target="_blank">📅 18:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جدال نفتی بغداد و ریاض علنی شد
🔹
بغداد و ریاض بر سر گرانی حمل نفت عراق به جدال لفظی افتادند؛ عراق عربستان را متهم کرد و عربستان با رد قاطع این اتهام، انگشت اتهام را به سوی تنش‌های امنیتی منطقه نشانه رفت.
🔹
ماجرا از آنجا آغاز شد که وزیر نفت عراق، در جلسه‌ای در مجلس نمایندگان این کشور، در حضور رئیس شرکت بازاریابی نفت عراق (سومو)، اعلام کرد که هزینهٔ انتقال نفت خام عراق از حدود ۲۶ دلار به ۳۷ دلار در هر بشکه افزایش یافته است.
🔹
وزیر نفت عراق در توضیح این جهش عجیب، ادعا کرد که خرید ۲۵ فروند نفتکش توسط عربستان سعودی، عامل اصلی این گرانی است.
🔹
ریاض در بیانیه‌ای، نه‌تنها خرید ۲۵ نفتکش را تکذیب کرد، بلکه تأکید کرد که افزایش شدید هزینه‌های حمل، ریشه در تنش‌های نظامی، حملات به کشتی‌ها، اختلال در رفت‌وآمد دریایی در تنگهٔ هرمز و در پی آن، رشد ریسک حمل، افزایش هزینه‌های بیمه و کاهش شمار نفتکش‌های آماده فعالیت در منطقه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/464790" target="_blank">📅 18:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZHZVkavQDTQFSZwjPHCOjhmbv7s1FQRPgL5QZkMePuQWqbFwAMynClRFEMmB4gS9lQPNF2lWc0satgSD48Uhd3F2ZaJ3U5_uM--CQdSmA3sJ0YqVdRcZmlHtmgIG0zmimNxsATyLpXR9PnRfhDV5Py9zJWjdzUhQejNsb-lOO6UtrnoYBNTvpDB6YjgfqhFyHus7JK0WkcjlOegbF9QeIE5-ZEMqcbYvaiMRtYQy8kP2tw98ScjcgIkIAu4NyQiuf4cYWjafKiYVCwelL-se_Fe00gMZM9t4z5uM3PThtRVftv94UI4t1MwdPIN6SobLd7kI_TYO4mr9dPFSeHWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز، باز می‌شد، رد کرده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/464789" target="_blank">📅 18:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621fa550c.mp4?token=GFKcELA9nkT3dfH2bAhVFS674G2jqw3LkHoT8g0ilBUBV564fZ4ncyZgNcQQRZQRR1ONZznfE3alzSPph-7eIRNIsRtyHrpmoZ8SBv5nEyq-4EosZvQIVOdOlOWStIeQrD-fNANLWmX1DAd_J1osOlSvxR-5Z_X-Okh-nZuPpg5WRaXWHW8Z7uFGX9fehN0j2b8WKyW7F0Gp_b5WKlG8LDG6-nnmLkGR2HGjLF4j5HyOcQyCS6Ur0VzIRC8ZX3P66bXo8E1PeGw3-TGeUKXfhe_devFjFWhcCmU39Eldg90rvYm0ICQF7egiYx-sNEMiYcQMxTrt3Hb2iZaOw2HeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621fa550c.mp4?token=GFKcELA9nkT3dfH2bAhVFS674G2jqw3LkHoT8g0ilBUBV564fZ4ncyZgNcQQRZQRR1ONZznfE3alzSPph-7eIRNIsRtyHrpmoZ8SBv5nEyq-4EosZvQIVOdOlOWStIeQrD-fNANLWmX1DAd_J1osOlSvxR-5Z_X-Okh-nZuPpg5WRaXWHW8Z7uFGX9fehN0j2b8WKyW7F0Gp_b5WKlG8LDG6-nnmLkGR2HGjLF4j5HyOcQyCS6Ur0VzIRC8ZX3P66bXo8E1PeGw3-TGeUKXfhe_devFjFWhcCmU39Eldg90rvYm0ICQF7egiYx-sNEMiYcQMxTrt3Hb2iZaOw2HeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۱۱۰ هزار جان‌فدا در بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/464788" target="_blank">📅 18:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYo6ObtZpNprfy9SOIAkHy95svNKRXp1Wb6xSRoDQp5PhG9r-U2hU58iADjIx3TpFzGnWNgVXAgMB9sl-3IOp9xSzTUVn29t4_5SGc5blFK-AiJUwa-LKksWF_IkhOH_Y4tnbHevUdkP4Bq6nh-Y7alE8cAQsaBwsScK3_yn5Wqd9Y46nITXeS7ot6XnNsQyV7jJUaXEnXvilwHliMYn_x1l8H3wxRzclmyh2G7AtIujSK4MrdhGdN0A4SykinH4h4N8Md7CB6EJVxkzcqexe0w7_-YWxZ0Z-Vk-zdeRtaTrxqXT4yGbXVw_8FQ7oCEYAFx2F1E10DXGCluKQo6fLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق محصولی: دوقطبی‌سازی کاذب، مقاومت مردم را جنگ‌طلبی جلوه می‌دهد
🔹
دوقطبی‌هایی مانند «جنگ‌طلب و صلح‌طلب» و «تندرو و میانه‌رو» با خدشه‌دار کردن انسجام ملی، مقاومت مردم در برابر دشمن را هدف می‌گیرد و نباید دفاع از کشور و ایستادگی در برابر متجاوز را جنگ‌طلبی معرفی کرد.
🔹
همه دنیا می‌دانند که ما جنگ‌طلب نیستیم و جنگ را شروع نکرده‌ایم؛ اگر کسی واقعاً در داخل کشور معتقد است که جنگ نباید باشد و طرفدار صلح است، باید خطابش به دشمن باشد؛ چراکه ما جنگ نمی‌کنیم؛ ما از خودمان دفاع می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/464787" target="_blank">📅 18:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70394d0059.mp4?token=pjBwqPsshESxBqnoNSbOcT_nQMifkUuZfRjxAGm0rC9jHjCuLr4awl9zOtvEPjpNssV7QCy2dX9Yft5-se8N3fKaIjtYbA77MczIoi544GAgkXVdqTNxu8wKsvHkFejRm-D2jCutOTeHWo5bZbcJ5ewZCnrJQ4Sn71Nn0BaASBQ32M3hBq2MufYaXkZM6imCG7Pm9hH-tkOKsXeZOrRIPH8vvb0OYMyUHpLCo6WlUMSBBZhzdT-X_xDclsu39oi5J5yW4DlIg4uPX-hJvoGEBCkkDi7NRw5HvI7KT7-VwkbqbmWbq4xGHKtZBfWTTY_0lhV2SI2KFJt7ShLsJ-VmwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70394d0059.mp4?token=pjBwqPsshESxBqnoNSbOcT_nQMifkUuZfRjxAGm0rC9jHjCuLr4awl9zOtvEPjpNssV7QCy2dX9Yft5-se8N3fKaIjtYbA77MczIoi544GAgkXVdqTNxu8wKsvHkFejRm-D2jCutOTeHWo5bZbcJ5ewZCnrJQ4Sn71Nn0BaASBQ32M3hBq2MufYaXkZM6imCG7Pm9hH-tkOKsXeZOrRIPH8vvb0OYMyUHpLCo6WlUMSBBZhzdT-X_xDclsu39oi5J5yW4DlIg4uPX-hJvoGEBCkkDi7NRw5HvI7KT7-VwkbqbmWbq4xGHKtZBfWTTY_0lhV2SI2KFJt7ShLsJ-VmwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: دلیلی برای بازگشت به مذاکره با آمریکا نداریم؛ برای دفاع آماده‌ایم حتی اگر کار به جنگی آخرالزمانی برسد
🔹
در سال ۲۰۲۵ وارد مذاکرات شدیم، اما در میانۀ مذاکرات به ایران حمله کردند.
🔹
در فوریه ۲۰۲۶ نیز پس از پذیرش پیشنهاد مذاکره، بار دیگر در میانه مذاکرات به ایران حمله کردند.
🔹
پس از جنگ هم سه ماه مذاکره کردیم، اما ۲ هفته بعد توافقی را که خودشان امضا کرده بودند، نقض کردند.
🔹
به همان اندازه که برای مذاکره آماده‌ایم، برای مواجهه با هر چالشی نیز آمادگی داریم و در برابر هر تجاوزی می‌ایستیم؛ حتی اگر کار به جنگی آخرالزمانی برسد.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464786" target="_blank">📅 18:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما آمادۀ گفت‌وگو [دربارهٔ انحصار سلاح] هستیم، اما اول دولت جنوب لبنان را آزاد کند و بگذارد مردم به خانه‌هایشان برگردند؛ بعد خودمان باهم کنار می‌آییم. @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/464785" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر امروز یا فردا اسرائیل از منطقه‌ای عقب‌نشینی کند یا طرحی برای عقب‌نشینی ارائه کند، این نتیجهٔ مقاومت است، نه حاصل مذاکره. @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/464784" target="_blank">📅 18:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان به‌جای ایستادگی در برابر پروژه آمریکایی-اسرائیلی، عملاً دارد به آن کمک می‌کند
🔹
دولت لبنان مؤلفه‌های قدرت را یک‌جا واگذار کرد و همه خواسته‌های دشمن را یک‌باره برآورده ساخت.
🔹
دولت به‌دلیل دل‌بستن به آمریکا و اسرائیل، مسئول اصلی…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464783" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌ ‌
🔴
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: ۲ سال تمام جان کندید تا سلاح را بگیرید و نتوانستید؛ حالا چرا این توقع را از ارتش لبنان دارید؟ اصلاً سلاح چه ربطی به شما دارد؟
🔹
در خواب ببینید که ارتش لبنان ابزار دست شما شود. ارتش لبنان، ارتشی ملی است و مردم لبنان…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464782" target="_blank">📅 18:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر بعضی‌ها تسلیم را می‌پذیرند، ما زیر بار آن نمی‌رویم؛ لبنان مال همهٔ ماست و باید با هم به توافق برسیم و از حتی یک وجب از خاک ۱۰ هزار و ۴۵۲ کیلومتر مربعی لبنان کوتاه نیاییم. @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/464781" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: به‌جای اینکه به ما بگویید «چون مقاومت می‌کنید، دشمن به ما حمله‌ می‌کند»، به ما پاسخ دهید «چرا خودتان جلوی دشمن نمی‌ایستید؟ و چرا در مقابل دشمن کوتاه می‌آیید و به او باج می‌دهید؟» @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/464780" target="_blank">📅 18:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: تسلیم در برابر اسرائیل یعنی پایان «همزیستی مسالمت‌آمیز در لبنان» و واگذاری کشور به شهرک‌نشینان صهیونیست
🔸
مقاومت اصولاً در پاسخ به تجاوز شکل گرفت؛ پس ریشه و علت اصلی مشکل، خودِ تجاوزگری دشمن است. @Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/464779" target="_blank">📅 18:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464777">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌ دبیرکل حزب‌الله: ما در بنت جبیل، خیام، عیتا الشعب، ناقوره، بیاضه، علی الطاهر و هر نقطه‌ای از جنوب که مقاومت حضور داشت، ایستادگی کردیم
🔹
پایداری و مقاومت در «علی الطاهر» ۳ ماه طول کشید و در سایر مناطق نیز ماه‌ها ایستادگی صورت گرفت.
🔹
مقاومت بر ۲ اصل استوار…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/464777" target="_blank">📅 18:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464776">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: برخی، به‌ویژه در میان مخالفان ما، می‌پرسند: «مقاومت چه کرده است؟» اما ظاهراً یک پرسش را فراموش کرده‌اند: «دولت لبنان چه کرده است؟»
🔹
مقاومت جلوی طرح و پروژه تجاوز را گرفت؛ کاری که مقاومت کرد این بود و نگذاشت دشمن به اهدافش برسد.
🔹
مقاومت…</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/464776" target="_blank">📅 18:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464775">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: خواهان تداوم مقاومت هستیم و برای استمرار آن در برابر دشمن تلاش خواهیم کرد تا از سرزمین‌مان بیرون برود و به آزادی کامل اراضی اشغالی دست یابیم. @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/464775" target="_blank">📅 18:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان:  یاد سردار شهید عباس نیلفروشان که معاون و مشاور سیدحسن نصرالله و فرماندهی بزرگ بود را گرامی می‌داریم.  @Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/464774" target="_blank">📅 17:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6hFPJlc6l26ONrNgq3anAyo4BS6UBnS0yP1hLGJkHJwyR41yMJ-qDezlbzKmO8Oks6rVVMZcgMKRYTgySQTWxirwOgL-39fMJ72GYM6MNAOgZXjw5jaxHZb032x85yRUSJPEyN-0WP6m6HXmmM3SyFW99SeAU3SN8lkUKYTO23Uwil5j4YscI06Ifk-BeDixuBy2SJyZ6N3XeoMbHLi5zJ0eKU98ORNMyLWyK56vKLqqsMOGaT8orjmXpipNMrChpRtnG0gP_dKMhQSCFPTw1nmYvb1iyO4oKJXyDrlO3EvYk7IPjp3gobddmzp2yqYGzfrdHNpYBdNFnv0DetaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: سیدحسن نصرالله نماد مقاومت برای آزادگان جهان است
🔹
شیخ نعیم قاسم خطاب به شهید نصرالله: شما پرچم آرمان فلسطین را درجهان و در حیات ما برافراشتید؛ فلسطین همواره قطب‌نمای ما خواهد بود؛ آزادی سرزمین ما همواره اولویت ما باقی خواهد ماند.
🔹
شما…</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/464773" target="_blank">📅 17:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084e5cf88c.mp4?token=tEGNT6RUCtA6TFUba6fm_P2sqr39BaEUw2d97AqpLEv_mmBr295xjyKiTrPXCSX6K-kDFs04v9sSeLeFFBfSZE1vPFKbllQk4_65J9oSGbh3mkmksJ0nUQWc6dWX5PukLWQJIbx2mP1WqKNhzlYYwTxml8nsiB3nOvcrfwpZW2OQfZmMO3Nmr86ztamyDhLj-baAgUGIEondbWlWdKu_ekTGnQaiRUIZj3OnIIhhVsPEJPOsxXP5kn-HHKxnpGogs6nfYCHDlqHuISYhba2FlAzvGW8rCm2WDPLj4PCEc7eKzgGDMWEoe2jJroS-liMdTyBx1IznF1ygXPQoKcPxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084e5cf88c.mp4?token=tEGNT6RUCtA6TFUba6fm_P2sqr39BaEUw2d97AqpLEv_mmBr295xjyKiTrPXCSX6K-kDFs04v9sSeLeFFBfSZE1vPFKbllQk4_65J9oSGbh3mkmksJ0nUQWc6dWX5PukLWQJIbx2mP1WqKNhzlYYwTxml8nsiB3nOvcrfwpZW2OQfZmMO3Nmr86ztamyDhLj-baAgUGIEondbWlWdKu_ekTGnQaiRUIZj3OnIIhhVsPEJPOsxXP5kn-HHKxnpGogs6nfYCHDlqHuISYhba2FlAzvGW8rCm2WDPLj4PCEc7eKzgGDMWEoe2jJroS-liMdTyBx1IznF1ygXPQoKcPxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرق میان ایران و اوکراین اینجا مشخص می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/464772" target="_blank">📅 17:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzscuB7-X-iVEsMOsqB6G8O2m4eNKUqlCBAwx6hen0cyix9Qmm0-bCqvUCOWA0pyuO4rZoPtYnJYkv7Nr7KUnq8EmoJnaApk0blV_l7ug0rjcrmwG9S9xqwchqOt5nZsWCvjNyN7Uz5Esk14WdZsoN-hQIxsB5Kfg9mvBahYayvYCqhn2MczcN5yqcBU4ov5nPHak1yalKtNpJ_D7kbcbhzSU-Szs0-50ECvRyXzLMdLQzMpOP2nPdX0QSWi9dN2EEMvdYGHwtxEgXwXD4qaYWTym_Hqtg0ZHWQieKoxiDbeh_hP5I1XTcZDf-KQMlo-ED0fnMzV9WZJH15eVji9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور مردم لبنان در سالگرد شهادت سیدحسن نصرالله در جوار مرقد او در ضاحیۀ بیروت  @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/464771" target="_blank">📅 17:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074489213d.mp4?token=tNWg20CUOlje4QrPF0fWsgeAJFLMVfYh8_HHdk3UBgXeijbSpQOiyUnqKrdm7b_CTLDm1CvPyusX8lBsXIbw1U6wZzn59v00FH7hKpBdOGlMDa5A2WE8pVK40UUW9rNm64d20JUIDTKcgeEmMUjmlXXDtDOYybdoHzw-KpDyqbBG2CO5IR9v6Utxuh4ojhDjXdwYZ8fsiUguU0ihDx4OdLFs3dxvLn15QzZmk80BaAaWzmtUKN8-BnTTZw3-6rBlBBgK_h4dvobxgvac40I_kKzAbEQf0BZvZf7L84AwRJYlskAlzOoLvUIh6-MqXOr5yftdChtUVTXHGktkuWXPLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074489213d.mp4?token=tNWg20CUOlje4QrPF0fWsgeAJFLMVfYh8_HHdk3UBgXeijbSpQOiyUnqKrdm7b_CTLDm1CvPyusX8lBsXIbw1U6wZzn59v00FH7hKpBdOGlMDa5A2WE8pVK40UUW9rNm64d20JUIDTKcgeEmMUjmlXXDtDOYybdoHzw-KpDyqbBG2CO5IR9v6Utxuh4ojhDjXdwYZ8fsiUguU0ihDx4OdLFs3dxvLn15QzZmk80BaAaWzmtUKN8-BnTTZw3-6rBlBBgK_h4dvobxgvac40I_kKzAbEQf0BZvZf7L84AwRJYlskAlzOoLvUIh6-MqXOr5yftdChtUVTXHGktkuWXPLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خبرنگار بی‌بی‌سی از نفرت جهانی از اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/464770" target="_blank">📅 17:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f0ed778a.mp4?token=chzd63WdNCMik3xlAIwLnC0tRzTo1o4GRaLv6uq_vSeIlXpstbzxhtrJzr30ePzLFYUGuN2xEv6q8MKSmtQnH7uipO61qlJtW1j5iGUhCvZOct3NANckkcJGt_eANqbUriWKV-rATNfECi8-TpGy1Iy862wOtOnLhgGLhzytQO3AlCfim8wZuW_NNV7oMIRTK5s72i-RLMMYQTKFSQzZUKL03AqktMSgNG4TrTNbri__B_r4AIHrcR3uIOISNwfS7KTeAzdeztGdwsyqbI0AJEImvNPuqRe5npt59rh1J0-gdh8hbanMMlby3V87sZBJsS1OqyYPBNvWcE1pswTQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f0ed778a.mp4?token=chzd63WdNCMik3xlAIwLnC0tRzTo1o4GRaLv6uq_vSeIlXpstbzxhtrJzr30ePzLFYUGuN2xEv6q8MKSmtQnH7uipO61qlJtW1j5iGUhCvZOct3NANckkcJGt_eANqbUriWKV-rATNfECi8-TpGy1Iy862wOtOnLhgGLhzytQO3AlCfim8wZuW_NNV7oMIRTK5s72i-RLMMYQTKFSQzZUKL03AqktMSgNG4TrTNbri__B_r4AIHrcR3uIOISNwfS7KTeAzdeztGdwsyqbI0AJEImvNPuqRe5npt59rh1J0-gdh8hbanMMlby3V87sZBJsS1OqyYPBNvWcE1pswTQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح یمن: جنایت در تعز عواقب وخیمی برای سعودی دارد
🔹
یحیی سریع: تاکنون ۵۰ نفر در بمباران بازاری در استان تعز، شهید و مجروح شده‌اند؛ این خون‌های به ناحق ریخته‌شده، عواقب وخیمی برای سعودی جنایتکار به‌همراه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/464769" target="_blank">📅 17:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52f42b09b.mp4?token=B3h_vHGhjSGi1gczdbpwO-qU9l2Q4zS3OqbXscBZMzRUL1nIgRVTT29GGphalg-jzkllni7939pczhajwjknMWIz9gzzy05ZR8Cixwh6yf0TdRjaFu7g60wZLqj8JomCPi_DkY4elSWDPz_B-Db85-nqMKbLB3Pu2xgbpZH5F5eSyA7KXFWtNgoe33JJxAT61d9ynkdURPTY0u9-CruZXEUZPSWoWu7FwBRCtaQEEQ7VhHv6rKZbBQ4XCxfPcE2gvvIAwWv1rzPY6wLOKZRDoOylRHz6vtpSjrl1b3BBDX2s0DgpNLfXrgL-2RXO1224qBGS9blKjf0_mZdtmsRSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52f42b09b.mp4?token=B3h_vHGhjSGi1gczdbpwO-qU9l2Q4zS3OqbXscBZMzRUL1nIgRVTT29GGphalg-jzkllni7939pczhajwjknMWIz9gzzy05ZR8Cixwh6yf0TdRjaFu7g60wZLqj8JomCPi_DkY4elSWDPz_B-Db85-nqMKbLB3Pu2xgbpZH5F5eSyA7KXFWtNgoe33JJxAT61d9ynkdURPTY0u9-CruZXEUZPSWoWu7FwBRCtaQEEQ7VhHv6rKZbBQ4XCxfPcE2gvvIAwWv1rzPY6wLOKZRDoOylRHz6vtpSjrl1b3BBDX2s0DgpNLfXrgL-2RXO1224qBGS9blKjf0_mZdtmsRSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات مهم یک تجزیه‌طلب؛ از پروژه براندازی تا هدایت تجمعات زاهدان
🔹
مهیم بلوچ، از سرکردگان گروه‌های تجزیه‌طلب در شرق کشور، به‌تازگی در یک برنامه به اظهاراتی پرداخته که ابعاد مهمی از نقش تجزیه‌طلبان در ناآرامی‌های شرق کشور را آشکار می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/464768" target="_blank">📅 17:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixAJ2o87FP3M5IK7hVvrxw0jnTpwNno5GQyFb_QhncJlIgsWIRpC-mOYXIKe20GWLRILTa3WntYPOo3JY1M7am-yPfcfePD-t86vbobuOvJlr-phxoSeFeYcX2ecmk5yXPfAVLkseEPUm0Xz3DzHZfivbvgIAfG0uTkQYVCE_S0FogLeSaTiC0v0YlNUhtkuSHu_7U_ajkpsOmJ_-1zeKmSMEwqnTC5gDvLPzxqTZgbLYCypq5m7dIDtIm_AdXwkK2rbfqV0h_zyYJ2ZGfsiCCuHiEQ_aSHB7-bYbtdg9FhDBemyZXP70kCuOSlRHvw97hUGsfDJNzyxbQ_tkN1blg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش‌های ایرانی دزدیده شده شناسایی شدند
🔹
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔹
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔹
بر این مبنا نفتکش مجستیک ایکس…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/464767" target="_blank">📅 17:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904ae263e4.mp4?token=GlHdzysIdZJ24XmMYcVrQDbTR9kyAR7VxSs8BqX4U2GqMSmrp1xajanGjnNt39FTXOdnUIeyRbEU39RNdL7UrkfUXgDkwKZ1UzyP4UXRVAwJ_3SINyAA6RgyYjykjQtg5WcdpYQktJlMcjjY7-_Fkf0mlHQlE0LjTNZ7_eMn5VXNni0OVu4n5AOceG2QtXp1HOhzn7fDviOTYkareBFQMXgCH6uPVFGk5nrEpG8xRbgK6onoHBxwAGT6lutJZTS7zqBkUyYFeRMVttVpvCBkspZhoD-4EiSh7jXfs4HwN9wc_Zl618O9fCKal0PzcNjoUJoo7S-g4UshsfGF20Xi5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904ae263e4.mp4?token=GlHdzysIdZJ24XmMYcVrQDbTR9kyAR7VxSs8BqX4U2GqMSmrp1xajanGjnNt39FTXOdnUIeyRbEU39RNdL7UrkfUXgDkwKZ1UzyP4UXRVAwJ_3SINyAA6RgyYjykjQtg5WcdpYQktJlMcjjY7-_Fkf0mlHQlE0LjTNZ7_eMn5VXNni0OVu4n5AOceG2QtXp1HOhzn7fDviOTYkareBFQMXgCH6uPVFGk5nrEpG8xRbgK6onoHBxwAGT6lutJZTS7zqBkUyYFeRMVttVpvCBkspZhoD-4EiSh7jXfs4HwN9wc_Zl618O9fCKal0PzcNjoUJoo7S-g4UshsfGF20Xi5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم لبنان در سالگرد شهادت سیدحسن نصرالله در جوار مرقد او در ضاحیۀ بیروت
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/464766" target="_blank">📅 17:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sALiiOhFNMFTnuo5zjhSYMYFxm1X_cKFHmr5kmIMQ18HH73x1yE-zCq2-pwHe5c4Kdcl0RDQX576tJYTAXKXaETb-hyxSIg6NSmNY8eyFqcxQONzEIzPCqoaAzlBlt_In8atKAdAOeW_o5flL6dMFgG_7ZLRFWnmJAO_hYS9XlaoeFZT_DSdkVp4BL3Ww1ZGHUrH1aprBMKdw_OgMxblP1PfbOUgaT0InSBruPlmrHNHsafwdzgXT86da7Hy2UaMo4Ng8uDziwA-Xt1zT6YfOU9sh28aaKo-rGJ14TEwoKqaOesPajfXGlzM8M-n8AojKvsdC_jfAmaNQXVoa5Cfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCzukMd7h4uxmUbj2AIJ1o6X9JTHbe2Lyc90nkOHTFUTj1Kyv5o8sS4jJsL8CJCsK3wXsUdoAePLLplxhZns5hNYTapPAms2vC_NpmAUT2SNfw3-EvvFPQZVT-3xR64fz-chy36aguVDdaXO7ALKBqASz38w9PbQsbSnuoRNkSLmbQxWAKoMrbat4ZN1EWQdkG5Q3MGaPztStAcmg9VeoAQ9kbNLTpsdyVZ_mIxlBH4aNtUB5T9EEGUiqHBl4N1XNfZfH0-QkrQD-_GlIdUZM3CZcPHg-jm2bHiHbPpSDYyUdgEBM6cPuJRsUg7p5jPEZbDEjBmLigH4u5fSk1FV3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نمی‌توانستم بر خلاف حرف امام عمل کنم
🔹
روایتی از حضور رهبر شهید انقلاب در لشگر محمدرسول‌الله در دوران دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/464764" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884c93a59a.mp4?token=BS4NaGzuyfQHzFenpQDx_0DXh4SlqpupLVVK-rhAZMN92CbT889DW-bwn3HPt4i2C_qKEywDlOmF1J_eEBZLcvJA9eaTXpIL7aVcrw6TLbgmuDmU4Lk3xXg5icU0XrOWtMMcfsfC5QsaJ8r6Yc_z2_hsxF_TfTuTlnD0rQjgQQ5ELfpPpl8XPYfuC8jNNZoH303xG1C_CN8u74itBK7lRnjpHqg9Z6vkeRRnSNxa60ULg-bsZM6sLSMBr38Z0pE21tBgvicX8WkNFar_WH8AdUcmZjuLCZcd9YehtVza40sB9wB5e3peXYquvS3YIMwHtHjmxHSWZnSrr80glA_OpDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884c93a59a.mp4?token=BS4NaGzuyfQHzFenpQDx_0DXh4SlqpupLVVK-rhAZMN92CbT889DW-bwn3HPt4i2C_qKEywDlOmF1J_eEBZLcvJA9eaTXpIL7aVcrw6TLbgmuDmU4Lk3xXg5icU0XrOWtMMcfsfC5QsaJ8r6Yc_z2_hsxF_TfTuTlnD0rQjgQQ5ELfpPpl8XPYfuC8jNNZoH303xG1C_CN8u74itBK7lRnjpHqg9Z6vkeRRnSNxa60ULg-bsZM6sLSMBr38Z0pE21tBgvicX8WkNFar_WH8AdUcmZjuLCZcd9YehtVza40sB9wB5e3peXYquvS3YIMwHtHjmxHSWZnSrr80glA_OpDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از دیدارهای رهبر شهید و شهید نصرالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/464758" target="_blank">📅 17:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33a13a9e9.mp4?token=habWHyfT7UC9bB2VYlaq650POkVRE_aWGWvtTP932PjEFckkGa8Ssdi_FsUBxijGVm86k7ax3UNoCMxZ0qMJAiWGIDAX3avng2jADFhdX8GuKZA6cHOH5B-7rPrAyhXcIdlSIQxEmJ9lj9wgnD1RwUuMp1nmPM7VlSytT66HGwHvHLxUsZ5gLgowR_NB3QpSTTFsYRsQvzDMCRiM3AL8j8XDkdmdO1Nwet7nKffDnLpWh3E-jJCsr3vfRzM4nOalTqxsecyilzCYqXcyyr0HM62EK5-7o4wt4hMh039XcKaaQAAXKNp1ocWvZiquHnc2txP4FgYV2YbYYMzwOp6MmopfbuNadozZ_TW1ZhuYx1txLe2AnSrnP-d2BWHX5DCbFc83HZH0mdlV45skWzntT_NXHKf3A9VhXv_LwuqIG3bI2vYu-gNych-_9NKMrucEHHs2uz0cnx_39WDjt3YlySkfciBVN1KZ79ls7XzmbNYRdpWCwVXpzmVZNPmtVSbzIx_F-n-cca60PuidHO0v13JC6BiLm58lRnN-WEZqRGanlcSMCGLdBQC-fHC7d69cSLqwhCahTkRJbYK2NJi59OdplYgcq0IEriaMYMjFzFTH30XgmCsiOVOIDwyR4-ejU02zpMxiRj4vR5Qfi7HlW6PofHuf-e_ElaMf2JrEsVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33a13a9e9.mp4?token=habWHyfT7UC9bB2VYlaq650POkVRE_aWGWvtTP932PjEFckkGa8Ssdi_FsUBxijGVm86k7ax3UNoCMxZ0qMJAiWGIDAX3avng2jADFhdX8GuKZA6cHOH5B-7rPrAyhXcIdlSIQxEmJ9lj9wgnD1RwUuMp1nmPM7VlSytT66HGwHvHLxUsZ5gLgowR_NB3QpSTTFsYRsQvzDMCRiM3AL8j8XDkdmdO1Nwet7nKffDnLpWh3E-jJCsr3vfRzM4nOalTqxsecyilzCYqXcyyr0HM62EK5-7o4wt4hMh039XcKaaQAAXKNp1ocWvZiquHnc2txP4FgYV2YbYYMzwOp6MmopfbuNadozZ_TW1ZhuYx1txLe2AnSrnP-d2BWHX5DCbFc83HZH0mdlV45skWzntT_NXHKf3A9VhXv_LwuqIG3bI2vYu-gNych-_9NKMrucEHHs2uz0cnx_39WDjt3YlySkfciBVN1KZ79ls7XzmbNYRdpWCwVXpzmVZNPmtVSbzIx_F-n-cca60PuidHO0v13JC6BiLm58lRnN-WEZqRGanlcSMCGLdBQC-fHC7d69cSLqwhCahTkRJbYK2NJi59OdplYgcq0IEriaMYMjFzFTH30XgmCsiOVOIDwyR4-ejU02zpMxiRj4vR5Qfi7HlW6PofHuf-e_ElaMf2JrEsVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض کاربران عراقی به لغو پروازهای ایران
🔹
در ادامه اعتراض مردم عراق به تصمیم دولت الزیدی درباره تعلیق پروازهای ایران، کاربران عراقی با انتشار پیام‌ها و تصاویر و ویدئوهای متعدد در شبکه‌های اجتماعی، تن‌دادن بغداد به دیکته آمریکا را محکوم کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/464757" target="_blank">📅 17:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw7k_V9Ec1bzJ-P6oSOWPjP0_D3e2_-IVS2MVC4FpFbfFozorAi-7YQ8tG4fG-xHU0ze-pWaTmXxSuoXKopMhLEs3zhSg9Otn1VlRg5x0QizKTWlG6cxv_VzGap0JDPwkw1h1gS88blbF9klSPP2UwAbMmNx5VuNsA0WRkjJOxYAB9GCtoaNbNTLOXF4Jny01Q5D-VsSQsbXqCxHv9hru44BgBNLGEz-XFqHvGpVMnXqAqD6nREcX2CD4ZY4Bs8mg3qnglG6G8gLQ73QTKcgD_BoOwHmMWvdA-QueAg7sfAmu1GB3CFLKFhEU_C_7eXWpPZ27aM1Nw8-q5GxmTYzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاخبار: ضریح شهید سید حسن نصرالله عامدانه تکمیل نمی‌شود
🔹
دو سال پس از شهادت سید حسن نصرالله در حمله‌ای که با ۸۱ تن مواد منفجره محل حضور او را هدف قرار داد، سازه‌های اطراف ضریح او همچنان تنها اسکلت‌های فلزی هستند و در این مکان هنوز هیچ دیوار یا ستون بتنی ساخته نشده است.
🔹
فرزند شهید سید حسن نصرالله، در این‌باره می‌گوید «حتی اگر کسی با هزینه شخصی خود ساخت ضریح را بر عهده بگیرد، باز هم بازسازی آن تا زمانی که خانه‌های مردم جنوب، ضاحیه جنوبی و بقاع بازسازی نشود، متوقف خواهد ماند.»
🔹
شبکه الاخبار در گزارشی نوشته: چند ماه پس از تشییع سیدحسن نصرالله، به‌طور جدی فکر کردن درباره تدوین طرح جامع ضریح آغاز شد؛ طرحی که ابعاد مختلف و گسترده شخصیت سید حسن را بازتاب خواهد داد. هدف این است که ضریح فقط محلی برای دیدار مادی با سید نباشد، بلکه فضایی باشد که در آن اندیشه و روح با یکدیگر پیوند بخورند.
🔗
بخشی از این طرح، ایجاد موزه‌ای مرتبط با شهید نصرالله است
جزئیات بیشتر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/464756" target="_blank">📅 16:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e9de6a68.mp4?token=VhHltxE_oZEIKulG7sdQy2Rb2CPy_Y2488Kr0tzDlGM495bLQLIJ-AUUqomDozdcy1j8Uq7_wD_TuTQYr3yY8aFfYXL9BLRmJq-vfWXYTvumz8LqXBjTc3b1oz5tf56oHkOmzvv3IheUM6gNt1a1EKEWhZqnerkpopCU9rcZSreFvQ0NnWhvp35Z4qcI0tkhcA2VGpfU7nNTZBOF4Ta26E2yAiIxD8t1gj80X1T9tywWMRRClTNKMvx8-2OZ21AZmO_u98QjmOenEq3RbgJAV1ipnT7noatbZ_930DBc2wNCdMGmLPLYlSWppL41moVOODR3aO67XTAg-CZrpcngZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e9de6a68.mp4?token=VhHltxE_oZEIKulG7sdQy2Rb2CPy_Y2488Kr0tzDlGM495bLQLIJ-AUUqomDozdcy1j8Uq7_wD_TuTQYr3yY8aFfYXL9BLRmJq-vfWXYTvumz8LqXBjTc3b1oz5tf56oHkOmzvv3IheUM6gNt1a1EKEWhZqnerkpopCU9rcZSreFvQ0NnWhvp35Z4qcI0tkhcA2VGpfU7nNTZBOF4Ta26E2yAiIxD8t1gj80X1T9tywWMRRClTNKMvx8-2OZ21AZmO_u98QjmOenEq3RbgJAV1ipnT7noatbZ_930DBc2wNCdMGmLPLYlSWppL41moVOODR3aO67XTAg-CZrpcngZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلما ۴ قلو زایید
🔹
دبیر انجمن صنفی کارفرمایی حفاظت‌گاه‌های خصوصی حیات وحش: مشاهدهٔ یوزپلنگ مادهٔ «تلما» به‌همراه ۴ توله در حفاظتگاه مشارکتی یوزکنام، تعداد یوزهای شناسایی‌شده در کشور را به ۳۱ قلاده رساند.
🔹
بررسی‌های نشان می‌دهد این توله‌ها متعلق به زادآوری امسال هستند و متخصصان سن آن‌ها را حدود ۳ تا ۴ ماه برآورد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/464755" target="_blank">📅 16:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یمن بازهم یک پهپاد سعودی را ساقط کرد
🔹
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کارایل متعلق به دشمن سعودی درحین عملیات در آسمان منطقۀ الطینه در استان حجه سرنگون شد. @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/464754" target="_blank">📅 16:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eff2052a.mp4?token=tGf2W9RxxELhMU-J0F-v3JbuGipZ0gC2Tw62Zr5w2AnBxf-A5_c9ozR2yW5TDkfV_a2lcpgbgs0Vggyy9gKsbitkarHAFcj40edo-4xfAE02Qb9TWNX2X6q0vC0X6J1VyKVtzHkr4hOuqdE6njSU0G7lLD3KwgSsIsp-CcV4FpzIG5-ZwtEgGrV873cfP5NScfpLcFKKnnuWk3GEuJNoiOAluMQZnU61iryDkYpTdw2xEaUrk9HTg06znR4N8S7v5vHbTuR2csvHrsxn0QCu647OJ8SZ324v9W4cI9aoBrsKcF1uvcE1e3EgvtwrGjE16PtFFmx5vH16aeIJNlNqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eff2052a.mp4?token=tGf2W9RxxELhMU-J0F-v3JbuGipZ0gC2Tw62Zr5w2AnBxf-A5_c9ozR2yW5TDkfV_a2lcpgbgs0Vggyy9gKsbitkarHAFcj40edo-4xfAE02Qb9TWNX2X6q0vC0X6J1VyKVtzHkr4hOuqdE6njSU0G7lLD3KwgSsIsp-CcV4FpzIG5-ZwtEgGrV873cfP5NScfpLcFKKnnuWk3GEuJNoiOAluMQZnU61iryDkYpTdw2xEaUrk9HTg06znR4N8S7v5vHbTuR2csvHrsxn0QCu647OJ8SZ324v9W4cI9aoBrsKcF1uvcE1e3EgvtwrGjE16PtFFmx5vH16aeIJNlNqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به محض اینکه ایران تسلیم و جنگ تمام شود، قیمت نفت سقوط خواهد کرد!
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/464753" target="_blank">📅 16:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌‎  خاموشی‌های شهر پرند با آغاز پاییز هم ادامه دارد
🔹
با وجود آغاز فصل پاییز و تأکید وزیر نیرو بر پایان خاموشی‌های برنامه‌ریزی‌شده، ساکنان شهر جدید پرند در استان تهران همچنان با قطعی مکرر برق، چه در قالب برنامه اعلام‌شده و چه بدون برنامه مواجه‌اند. @Farsna…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/464752" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIcB_ghjnViSRd9pGO5TZzMIUEIrw_vlC-ralMWJGRL2FoEHmi4Kea40ZdX2Lkto9v2tqxB-8V-hmZhlRldZKwE-sZYxVtd6aqS-1vo2cJClJv_FPepLTcSHdueBk8ZyKSUg9nSU9rS318nuC5kmfEg87KHbwHI_bsWLb6cEUk9shD8Oe1nBzhxN8vfl7XibEq_rAePGhsFc09aU2y2zEpBMMfaP_SHt31h8QD6atGv2_gBeLOP9Fp8C22U-xyDs6iui4BzMMys4DejVuBmHPsXHuWY3EHQ12Sl8ORz2zfIyu3h_VP1jm0cg8e9aweERrrQRMFm37_XjHHKAgdtErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس راهور: تردد خودروهای دارای پلاک مناطق آزاد کیش و قشم تا پایان آذر در سراسر کشور مجاز است
🔹
سردار تیمور حسینی: صاحبان خودروهای دارای پلاک سایر مناطق آزاد برای خروج از محدودهٔ مصوب باید با هماهنگی سازمان‌های مرتبط، مرخصی و پلاک گذر موقت دریافت کنند.…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/464751" target="_blank">📅 16:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOIxYKi47J0fIshXGnv_hB0rnE5-9K3rBRsoaI75D3GPgRBsnjHoWqJ3X1RkWvcBGKGxvDL5PQSjhLlD8kou9LIfw7j0rqsWUtn-pZqq-14d_QDBBgZ18T202HQ0Hu-pjNes5yQivhikRCkMEmnnQjzGHZ1D02momnZ0dOZpq6xn0ZQhJQJPHTmTCf259xYHYY1OfQKA0wDYFhko5hzPdRDEzm3sFuk3NJu6qxF6lZ7dteSI1lMD4LqlykgQFFsqSkgxEWG85tWvTH24tYuauAcnEuR3oD1N5HSnjXd2UvY0ffq0pJzNFsTfctG9reNlSjyZ4CovRIaN9FNbUVnS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۳ پهپاد و ده‌ها نیروی مزدوران سعودی را منهدم کردیم
🔹
مقام نظامی یمنی:‌ نیروهای دشمن سعودی که قصد انجام حمله در منطقه الوازعیه را داشتند را دفع کردیم.
🔹
در این عملیات ۳ پهپاد دشمن منهدم شد و ده‌ها کشته و زخمی در میان نیروهای دشمن سعودی به‌جا ماند. @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/464750" target="_blank">📅 16:11 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
