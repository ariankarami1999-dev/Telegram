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
<img src="https://cdn4.telesco.pe/file/lcAJsVvK0ve1DjFRXkHjd9_8632bfWUPzUoVH4ttCYMyIg_a-A9i3ZbxDspY_c2funG1JSKLDwoVkk9SYrPF8Q9-uC208rENsU_RPHNZ3ji0d5bILwFWL4tEV9iOJk5Af520b-zfqihprlo8U5i5_u--KpY0AOIa4ydj4Q2rrIQtH9XHxFSsOhy_zLNKkGt0E8iKhTSAzicUat6e2kpAIYvKbLnFHQVAtCP789yHr9_apANp_Q9Zd5rp9F9lSZxwXv4pw30ZeqsWO_wDNy1JjH20Yq3coz-I2zVZk6qQFygGjtjv_sIa4xezTfIhDlAblCRJMKq-Tz92RV52sXXMJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjieEiAjGYQWiSrW_5QermMUVTcElQhZbpBSd8abhSA9Lw4rP5DxvFy1tEyZJKR15NNHv6pVAd7HDgx6AyiU3-NelEIEFtTeOCl_8M0EgY5CfASWWNhN6HmxoBPq2nelavRL3xP6DTQ5mjMulTTNfNV0E8YOc9rloiflcJcMN61Q7USnm4Qqy9yVIZEflyWcHKLTvyJx-LchBABCXfZSNE18vEgJ3d9RT8Q-CBOofQ0ZwoZZFM6N4j7zJvcKrh6cOtj_J_AKBoDbXG5Ad8cjqtAy8YbfG5Zwd5bZ_5eu4sO7EpvClwt4ffMPDl3SakIj7zs9LvKNWHNbxXTtb_LUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saHKT9WHfAweYBYPZBkG2Srr6_j2XWItyGYb2ENaKaK5pOFr519WDyEUSN3JXK1ZNr1tNuRY7WAEupy5ZYbnXnMSJe7S-9uu_NQzXpc-tJhv5Zi4ZQzmIUgdhEaTdAQid5FK7HYi59qzAW5EAae2uYlvfJjau02IZWEiL4Az3p70U3xO01uDsXaCIMbX-rqN1MyR8nU6QZCaWW83cnsgNwrqe79i-DNVMnPF3AISQ0vbZ3czN5Leh6G_tpNoUJncfhpwhpasQyzgqGfp2PPV1VytUC15WuIDNyQuLuIP1aIou6pColSjEngsDXlQzJGa0zD5_vf-trnjv89fcMovzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=XPEexr7JweO4PzlMvUsAvS74MBIXlukUwvzZLD28ryUiA1HEKxQJiH312uCXmBfs08zxLtFJYqKdOR9gkXkaDLETHs55IAcrh-iGzOoP4qCbAxzsKTCrEpyuTZ4rj1r1F8WqUBuJ23NUMXLzhcWHce6o5Fn6cVqeIRRhV_DnmdYGRQAyUzWLu_Bqpcu4o1aWCzvjosrA-PpWaN9lUFyYkOPUwWSBky8YWQiCa9vgzd6nzVfrChln6y3HMKINlSsaqUAk5zVEZBZVUYmPb7wE3bTnbtrutLnNDY3lo0-DIRiGvS7L-RDv4gRyoZTGMECpHAMPqkREWdVRwm2iqv4K6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=XPEexr7JweO4PzlMvUsAvS74MBIXlukUwvzZLD28ryUiA1HEKxQJiH312uCXmBfs08zxLtFJYqKdOR9gkXkaDLETHs55IAcrh-iGzOoP4qCbAxzsKTCrEpyuTZ4rj1r1F8WqUBuJ23NUMXLzhcWHce6o5Fn6cVqeIRRhV_DnmdYGRQAyUzWLu_Bqpcu4o1aWCzvjosrA-PpWaN9lUFyYkOPUwWSBky8YWQiCa9vgzd6nzVfrChln6y3HMKINlSsaqUAk5zVEZBZVUYmPb7wE3bTnbtrutLnNDY3lo0-DIRiGvS7L-RDv4gRyoZTGMECpHAMPqkREWdVRwm2iqv4K6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=VRTy3IJb2l84UCt8ydl1KtHU2QVvHkyzRSPqKjcJzgWTXJCW_kJSJjJJyXgPGUQwQdqiDONXoIanQKlaRNXNxeU6v1yynknpZfozBWb5b0xJxO6XIhNyuDetY35yObGugsVGVKV5FoACd_b_c_M5WNeJQdB7Ew69roAKjL9Xpy37husieWfq7xqQ6SMR8qbLxp6L2LSkeP728TalBLic9Z0_Y_oplUx1Y47P1yA_2CZI6nuA9Co-RcEGY2qalgHHZMy6_jZM7ewaXBMHX2JvGv_IfAWEn54InHnQyH7AJuvg-SqVn3z7pg1O1dN2kt0UbWtwUW0DQj98qJGPLFAQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=VRTy3IJb2l84UCt8ydl1KtHU2QVvHkyzRSPqKjcJzgWTXJCW_kJSJjJJyXgPGUQwQdqiDONXoIanQKlaRNXNxeU6v1yynknpZfozBWb5b0xJxO6XIhNyuDetY35yObGugsVGVKV5FoACd_b_c_M5WNeJQdB7Ew69roAKjL9Xpy37husieWfq7xqQ6SMR8qbLxp6L2LSkeP728TalBLic9Z0_Y_oplUx1Y47P1yA_2CZI6nuA9Co-RcEGY2qalgHHZMy6_jZM7ewaXBMHX2JvGv_IfAWEn54InHnQyH7AJuvg-SqVn3z7pg1O1dN2kt0UbWtwUW0DQj98qJGPLFAQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUO-pUzMaQhyGvsVujnLlAHmpDkhsvFrTaqCh9DkmnmCsAbGyGLq9DL595ItFJIDJw1pR4MvB4KjA3Zt7HQkRySbIPNN-aeZeQOORmOxAS9jkXu93J1insljMEZEattNJ4q3QZ8rrEUb2mIyz0giVklh5mSr9cKaDRhPpLnA3n0PrVZn4e432GNZdNFWesui_QI1ZCtWRTqMI8S7UOIZostbjSesRTEyEDW9EMBQzbZOvhQ8r1STTy_WuNWQh3bHZFPXJxr8djWMMYz4jjXOLal6rZXOr-E6SsM-RtlDxx0JsMMV-UHz3qOParzNOvAx8gaqz0MRrgCUERr3qj870A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNTLYX37coBYYr2-M65ZDfLxZMTDds7YqjIRIMnD37nxU1k_bVtYIZRPd_upxubbKUmjHHR2-AbO9j8-WOUZgfN4yPxGPxGdBxHyfvl5gqMME6ERhkMvbjpKQfAZxbmZ0AC3-IR-HjjiMrz64GT9vuMGg5wIS1Peq3PNtC9KP7ailPhIU7PYIWr_rgtesZMNCcA4CWPYImQES4I_ncFXyP7olUCF1eKNTQigWC-nvLlX8voRVs0mT3dtcXignk670z6i0eactzcXLCFHKkVUzkClLUvyfi1bNaUUhRXvKCBMtYkF58VCvxpisrjp2bkxe9GuzkCGcQMn0v92S2N3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=mxgo_UurUnLh_ovBYkNn3e_ISd_qYUsoi1ppQab0c7DpTX1kTqrEOCu1IOZdz4hwv4-zIpim7Jcz4i_Nwy6MQ3r_J73yj6GRAoKZzGjM1QkcrndKrnTRgs2IHIS11FLBor7OIOwTORr0TZ1Rt7WJbnt_zNZhmd0uyCH62jr3JHepDxFEOq9_663fjtkeOUlFn7YPWiXqR0DCUh6SQHwqAo1LE-v4Vdqtkqrlbiw66SZDV1cRdfiCzUNhR_JQvK0c6i5v9JkZ4ZXsAVt_fd-r9pyECtLepOcXYkeSbb6E31pVxDPQtl_i_0_LhJDYwxbhZPOY6bJNgw5AkGUjA8Mzd4xsK0gxloix0fkloXxBu7vYcEawd94FOnAzXX-3XXVWkZKB46iwxRdrhJ6b7RwsxlCF3KBQSzIbNomH29F2Q3tx0_EsWXg1f-_W0YXeS-8k-Na-Y2VHVS60kHLwykbs80vLRZiLZkYdZRFwEkwNtGMk5rVKNmREsqN8laG0n0f90AxgCvH6SUMcllGLYk-0aH8LeHgU3tXU7bLe_BFuH3CMWUfzkEoW9o6ZfYJFzgMFL-DXoa9Vq-Bsz9ac6QyAAUCF2ngl6a2RemZqgp0CCGQJ6r7BYZPClcvkf_v2QHXYq6zJ95zWf6lnrW-CI9PrMOpvT7EbalYRw_6NUgYHpMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=mxgo_UurUnLh_ovBYkNn3e_ISd_qYUsoi1ppQab0c7DpTX1kTqrEOCu1IOZdz4hwv4-zIpim7Jcz4i_Nwy6MQ3r_J73yj6GRAoKZzGjM1QkcrndKrnTRgs2IHIS11FLBor7OIOwTORr0TZ1Rt7WJbnt_zNZhmd0uyCH62jr3JHepDxFEOq9_663fjtkeOUlFn7YPWiXqR0DCUh6SQHwqAo1LE-v4Vdqtkqrlbiw66SZDV1cRdfiCzUNhR_JQvK0c6i5v9JkZ4ZXsAVt_fd-r9pyECtLepOcXYkeSbb6E31pVxDPQtl_i_0_LhJDYwxbhZPOY6bJNgw5AkGUjA8Mzd4xsK0gxloix0fkloXxBu7vYcEawd94FOnAzXX-3XXVWkZKB46iwxRdrhJ6b7RwsxlCF3KBQSzIbNomH29F2Q3tx0_EsWXg1f-_W0YXeS-8k-Na-Y2VHVS60kHLwykbs80vLRZiLZkYdZRFwEkwNtGMk5rVKNmREsqN8laG0n0f90AxgCvH6SUMcllGLYk-0aH8LeHgU3tXU7bLe_BFuH3CMWUfzkEoW9o6ZfYJFzgMFL-DXoa9Vq-Bsz9ac6QyAAUCF2ngl6a2RemZqgp0CCGQJ6r7BYZPClcvkf_v2QHXYq6zJ95zWf6lnrW-CI9PrMOpvT7EbalYRw_6NUgYHpMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvG_MmqYw18OWuvXMyX_-x2nIY5NjEMYWomy-V2iZcD82mDSzopcBzVAbgCELFy5ho3rYbP6wrPha-EASXRMA3i55snhpwTJ6Ym4xD3HkFTr7EcmnbB9uAnotYlPaqjaDI1Rulor5ZdVMZddbr-kPixR-5wFmoFgSsx59vCJMRTIPmRViqmUtNjEzz_hCGvjqRiScfNWQ7x6S_MhLaydzojTC48aDId7kXApdN7m8ME43Vgxdrb-q7ob4JD_PBVz0oeIIVqEofbvgh-Q3sCVM20IYxc2DlTf5slJljB9ZL-A_m_csuzTE3QSGBq7gXDQcP2qgVFY5PxTugyGAUJKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYJdRgFd8d3DmYRnLZS78hdAnxtdbKskJQ0n7MsffybgVJOVmZKcyfYaaIRddo7eG6VSE9fRdlhR27zzIuFRxHnmJlT7LJ7E6BI2rlJ5SGpRABaJc1dtlc97Lhd3XIyDhtqSEtjGE8rEALd6rJPj5of16cVYrr7NZ3HvVtozwJEYY5VUlQWojf-0HOpCMnap2Nzm_cX3u7PZs3Oeb6kLcSaLTx47MCPn5DPsMgFFhkl1LhEEcBWG2OmfaCIyvUZVLnQOeZOHNgnFD23dn_MC7DVuGB1YDKrmU1_kZy5Jnkyyxc-pRqifAfXAY0EJQs-4asNnFnoNtbv9L_wX7tWHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpi8Ii19b2z4GHOqwMJNsowIBmCl88CLlO2yK9NhciP7xETvZHtiFrNjw6IuLRNT-85HCNtPsGSw3onGrECWmq8Hgv_qujAnaObhs5gleTrTWtKEiP5R9CVu0wy-2ft3P-zvUnd8Nt23OOUcfQ6kWbUT9UXjEjX3-I20rD_vy3iBAMw1-q4SwcYMFwrzEIW7DngLVDWCRmsV-PgWXAhlaMIsm9Q-qL2_7e0heF4T6qQ_MRQJ1cCziFfyY_JY98IOv4EQjXkBC0sLwIi--E69xu63XxhnxW1CyT4WzzkjVFfMqsTIgcZwWiiGuAwegNQQaA2fyYtmoA1shOVaGl-qmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmsK3NyospuBQmC5SqfjxLw9CfmC0ZtibWzd3eGaQNTjqWkrdyrrL2AtYwXYEcihB91JLEezLkvanPRriLXy3N-bh96itCrVJsFJWON9y7CqZUdE88FV97Do0uHZ_qx7XJK9cJK3i8WTgbIgq5SGO5vomOR6axdsolt81sapjyObHgyM4Jm_865qesPYv8sA_bl9yjvAXCObyTEm2ZJsutenmnjx6wE_eMLU8VWXNJB-38w4n5f2l5GZiC9sAJHwkezxpRbuj48txVA3adVprbqHdU0dgpZI8WgtaP8jJF8fsfs_WDXtqYwyKzKgusg7ddC1rB71Y1qBOd6BdCgwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP0XwqSNe-6jxezYNZp3bZViPTDO8meQFTFReYMjsNQbZpmVge6zvAXT3ilXKONTmOTG9xykMGKCYSkdk2rCPV4ey-LsseLnnnL1RTBgHX3XPP8L4WciPpGUfRTD6yOiiaA-wLIyRlPXvlN30WCDF_wH8S6Pwp17GkAKb2FVE3OsOkxTsxhfFRLz8372O0HB6xMV7e8oFNb7on_Mf2Hn96CDbvdPOtLDMixDLaM9tmIw7ynqZgdno1nZck1QOpVlhCuDLIEiEz1eROpy4UYq3VLFhTnAgyMKzDJ7pYuBZo3i6ENu2WJ1e0kl7-1GTzx5hOAJRLvr7lWIpiuRu8ovjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE0BHgCokzwIFDw3PkcMV2W3WX0aFvupMSMJTl2GtipoJSwrDb8s_YH01qNiNLAPmWutQGur89EEtzYxQzUMZ53HUzPAGeIHrzleKitlSHozBQK2iHInquCAtgPDfLDY-wOUGxOWZzwWP20xMX4MQ_LfmnkSX5qjMDtF6HEWsawyfkcl5a4CZw58OYJH_WDftvv28-DlG3xNNwEXV42I-TmZv1e3b6filXKSHZS772kgd37pSqDVuSHUBaxsTC9oqj_Wy61E5fXLZdhkQnkqjKhIojtuaW6AukXC9aUXUUnNHROY3Z0bxlyneU1X_I_xbs0CdqSlDWhVHowiePApDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=VUBrZX_EItIcUZ6CBxBrIRLGiluzpcere1-JLUhEyRjOR4ADaRf_TT4t1di9wjVQJ_WKsGND3C-lxyauezJT2KCRZPKzo7ajcnrQgD5ztNKHBFosF1u3ecpwq5XCzPO3847EdUTPOFcvHNZD5WW7MDsGfJBQd_ADnxPGR2dWrOYKlfSKUO7Td4M7nDRbZwxrQNsX7DMGF1BzIdjFJuFCXV7Azu4FIcpIWV63b24sApTQ4kU6y-mjXfcNDFNyHYpzzFNC2TTDKuMHoDY56ubJxh5uEY5WXASKPtT5IAQ8e8HuCI5IK4l4CrToORQlrpzf4DeVOGuGJ7PslFzfh2_opQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=VUBrZX_EItIcUZ6CBxBrIRLGiluzpcere1-JLUhEyRjOR4ADaRf_TT4t1di9wjVQJ_WKsGND3C-lxyauezJT2KCRZPKzo7ajcnrQgD5ztNKHBFosF1u3ecpwq5XCzPO3847EdUTPOFcvHNZD5WW7MDsGfJBQd_ADnxPGR2dWrOYKlfSKUO7Td4M7nDRbZwxrQNsX7DMGF1BzIdjFJuFCXV7Azu4FIcpIWV63b24sApTQ4kU6y-mjXfcNDFNyHYpzzFNC2TTDKuMHoDY56ubJxh5uEY5WXASKPtT5IAQ8e8HuCI5IK4l4CrToORQlrpzf4DeVOGuGJ7PslFzfh2_opQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=i4wwvBu6pkcTAvpvrlcAYafh3AtcNh_7AvGYqCUXcxY7X6f9ezktexVCsmFbuM5fGyp0a-3qF8PcDsoG9b1OakysYP3RAtwV2XXHYCdukFISNfhAMEfW9NiVSbQqQwe900SBIrHKJMR5YWHlnhFDdp2zflfCwy5IbuQczgJJKwwrhO1_nyb4HcZVVamrsxVEyF6wlRYKyuTe2U8Pqn1ud9VHTVMHHB-wh6ZOMaEef9ksOy73vFD-vj714qvYlxfyHY1ZimpgrzpgpKCrq_wYDqx72jCz-5LWrZQuHEvFo5L4j7DUaKqonPYi9fU9-0hoNYXjzH5a8FZRqiU0zklBEnPN5e2mh4zq0jrc9dCS8q7yEpyKuYdHlw88Qqfbc1PF7tYmsdd7g1oYkWPn_priby_pEEEM8b-gOW55QxGc9MqcVckB8-UR5nhhUmjm7OO6qdhZmxdp9VZEGjizdzFCIZn0q1UDhI2lGAevBzIB0tMlNm8Iv-1loHa8gz_Xn8M3-hRJHdtL-h7x1OBLcgJT0ziDVeqT2nmt3AFArtt4C9Gql8BwUf0t3WCNTB4T5o2c8JATveEfdHk0Y_xTUj3h1_TC_OaoNqDx0KXirWTHiuuL-W0BTkYGaWGIZ5dJCjX-BhETxuefTQ_3fd54_soPz8q8RbrwZQAbRAZbN2ChoKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=i4wwvBu6pkcTAvpvrlcAYafh3AtcNh_7AvGYqCUXcxY7X6f9ezktexVCsmFbuM5fGyp0a-3qF8PcDsoG9b1OakysYP3RAtwV2XXHYCdukFISNfhAMEfW9NiVSbQqQwe900SBIrHKJMR5YWHlnhFDdp2zflfCwy5IbuQczgJJKwwrhO1_nyb4HcZVVamrsxVEyF6wlRYKyuTe2U8Pqn1ud9VHTVMHHB-wh6ZOMaEef9ksOy73vFD-vj714qvYlxfyHY1ZimpgrzpgpKCrq_wYDqx72jCz-5LWrZQuHEvFo5L4j7DUaKqonPYi9fU9-0hoNYXjzH5a8FZRqiU0zklBEnPN5e2mh4zq0jrc9dCS8q7yEpyKuYdHlw88Qqfbc1PF7tYmsdd7g1oYkWPn_priby_pEEEM8b-gOW55QxGc9MqcVckB8-UR5nhhUmjm7OO6qdhZmxdp9VZEGjizdzFCIZn0q1UDhI2lGAevBzIB0tMlNm8Iv-1loHa8gz_Xn8M3-hRJHdtL-h7x1OBLcgJT0ziDVeqT2nmt3AFArtt4C9Gql8BwUf0t3WCNTB4T5o2c8JATveEfdHk0Y_xTUj3h1_TC_OaoNqDx0KXirWTHiuuL-W0BTkYGaWGIZ5dJCjX-BhETxuefTQ_3fd54_soPz8q8RbrwZQAbRAZbN2ChoKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-cdfmRJjG72cEXh_QLvJ3imcvBSFWSzawvLm3AXbYpG3tdkqVMpxEreX8KvDR4hZeFH427UnYEAMNkD5f3BIO_LKbFTHFq9kVfn575h5qUli_wQNpJs2-DDYmvNEdyZIvNMbxrb7N6BmFGkthulRe4g7ypTJqjyAwaADwB7ccv9oGLmUlRhGINfOfF8H9JsMDTe5F0BOGwzz6yanFQOlv-GGni6thZ8nc3ahyharllh-SG8yD6_D2KCkrn-vcpXNy0pC1nicDrOZ2Z3w6S3UJovibUVt1pVbmyHa6GscKlN-kmqSuhfFZi0B123OicuvS3xmbb3Ie9Rb1dXbK8bNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DR9e1eUORDsR9RKs3FHVTDgP-HIozKG0sdF1imYoy-DPXkUq9Ksapl23KUV3dX_0iBRN_4CpGsRJOWGFZAX6nTtzruyenF90STkrxjKCNshCGZLFDQ9T_1fK2h7UjsME5ARAfXJxgw3nf5HtW4BtKjBnofa7psZ0DtO-D9Nf1qehzvullFbgcyW8H2H3A90UXFV2P8n90XWl_odFnpOXQHFFiG4pHuOq8X82ouytvugyT-Dl0uC3uMWztvFN9GQo6v-GDzqlIV4sygXA_G4y4nGLIjFw6FnG35D3KwnFvofhYiqKdb4SOzSzS4pCr3LW5ZjumjiC9o958FiUljXo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJJcK06FwH-7jf7SIgewcjzmfx4w-14NaA8NFZld3jFOtErMfFFfkRhZSiyLUOlU6tqMSh0ttl7PDxHErPMn1WUNmgsD1j_ybr_Wj6qtyckT_4doubDM5mh325GxFHfe7NowJcAXHwH-goqVvQSCYE2lkbmvWg20nLFHZLQA_HEtpvmaeJ1DTUpGmOiOBt6spZuxwxA_P3jr4W5aJ_X4j7I9sMz6-WzYIJLpzdnKJ3b7AbTLDml-lI7sSQt_62S3katKEmvH6i2Ld9KZUwa0jQoVvp_cSfriHwsuwJNhV0vDmfSEFPi8urwCNZbrtXAXn7Lg1xmGOU2_OYjmB8J4XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=beT5II77ApnQ9zoq3HC80Ew49m2EgVSIwm8cdZU31BbXczGa3f5nEMUa9kSBrABFnuy4crQFgDAJs2mTlX5QWPBH5GHZICSUvnQGEmEd1GKI6uo-N1MtZA2CBfLfdGb_d4vvvCT8ZyCBQKzQ1ZOM0PC3IXkn07KgxApm8vikyIYnzwsNk6rRESro0nF0BGpuctXmPTcrlC92noUQzBBwjyQa4kvBURcUSAzcSnamBznVcvv0yRy7GDa_fpPA927WaUNTpvjaRmvHmXGu_-k_BS30lWOqVs362G7rIaG8n46F4hicZ0yv6p3LDCwObiCzweNME5muK7jwanUnyhIXog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=beT5II77ApnQ9zoq3HC80Ew49m2EgVSIwm8cdZU31BbXczGa3f5nEMUa9kSBrABFnuy4crQFgDAJs2mTlX5QWPBH5GHZICSUvnQGEmEd1GKI6uo-N1MtZA2CBfLfdGb_d4vvvCT8ZyCBQKzQ1ZOM0PC3IXkn07KgxApm8vikyIYnzwsNk6rRESro0nF0BGpuctXmPTcrlC92noUQzBBwjyQa4kvBURcUSAzcSnamBznVcvv0yRy7GDa_fpPA927WaUNTpvjaRmvHmXGu_-k_BS30lWOqVs362G7rIaG8n46F4hicZ0yv6p3LDCwObiCzweNME5muK7jwanUnyhIXog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=QY_Z7jI5V0o8f3bUn9XF0yQxovSN3qg4HyBWj_psEBwJu5ZU7X60FvxeNEvF1Aab0gDIJnZiwhv0m9w1KgqUiOaXg6rc3EcZU_aeXaYHx3p1GoWcmG-JxrsfLqwymDeGksjbvrREEzjfcbg-IzIlN07cYyva3Zor8lTkDkBGQYV_7GFYQz5VAPu9NEumh6nFhzv-uSVY3Ye8hRfJL1mvCE1PhiV-uRPK5hduJsZNq05BeATyvYHGGX11HaZLuK8FucwmrDgKfqdxIQNzF7x3zd8Q1mSzEUYSdCSLLcbRkwJYa3hypmzVou5a24mCaPb8VV5Uxi6M__89eTy7M6IifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=QY_Z7jI5V0o8f3bUn9XF0yQxovSN3qg4HyBWj_psEBwJu5ZU7X60FvxeNEvF1Aab0gDIJnZiwhv0m9w1KgqUiOaXg6rc3EcZU_aeXaYHx3p1GoWcmG-JxrsfLqwymDeGksjbvrREEzjfcbg-IzIlN07cYyva3Zor8lTkDkBGQYV_7GFYQz5VAPu9NEumh6nFhzv-uSVY3Ye8hRfJL1mvCE1PhiV-uRPK5hduJsZNq05BeATyvYHGGX11HaZLuK8FucwmrDgKfqdxIQNzF7x3zd8Q1mSzEUYSdCSLLcbRkwJYa3hypmzVou5a24mCaPb8VV5Uxi6M__89eTy7M6IifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkQv5m-mDu-8xKBvq2VC1L3PexOfg7m7AHnvsRW-tv7vGOS2nGfvvvTDFKJNVv4COM4dVZUXlE-RT873KXpmsP08Ap28lRCPYSb4KkwBx0gE033id6bjPTc_25-2Tz2loLO13PJk0sivVKXlX1s87mRLDUWLQTMpVQm84Z8POR4qFFATyalN0cllQOKwZJAkMMQugjRVF0_7xeIZIMS0593PXiLiM06jEgdYoPZqi5Zs2Q5Kz_ainRbuHnlTJsbai35MXB3uuXPA_SC2HiyHKrzCuu-J8W787zSpJQRKfUnW11_WQvXW0gtw71_q1ru2sCJMf70-_ExCPNm0ITv7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=hnGHXSJTwx54WOa7XA7THDDLAe8kWZHKth1VulztXO8Kc1BzKLvZllEO5C4GiTtBnakx7I9P99zMG_4wBQK5ptYT_b9ofVyfroT1YuSeer_1ddmW4zcHtG7WFBV7uND6-QD4F4jhv0UZ5Kr4pmGEK22xel0522_UQGTLmn7DbxClkWg-i3Mgax3LeBJxTOAXIsg2eJ4sm6xTXoSUMmzPTpNj-RhbtBD1S4UGJXunReOx8oRg0zoZbXVEJf1qaBaytL3vFXahMipvppyQp3nzLkC2mpxZFGKaVKBQSopdrcLjqRFrNeQalf-J645Rpt6bPboXeVQmiWkijdXtTs7T6nq9MfAuKdrca1jc2DDOLuLlzZqVC_uB1DPtLyKJMum01aDONCl2hwOdo2A55ig-uEWfB8MR0MahyIvKErxCVE2gPV3R86j-bmT4o_3ia-hXTGivhBgRNdMIdwyma2Mblf3EhOozuhu6CeE7fT-ANhAik1IS1c8udKV5hjTRSBma-iytcs4rFLIlFFa6T1eBS79eQsIbK6ihlfxzMez3wVwyK-7sP4W69p83hrOqDRs5FGZQwuLz1RrPkf6ursVq8_oL6saw56xHiQ9FQywBpZLbbPGPeZIPlcDikGbWvmhKzzKKo4R7nKy8a3qNX41aUhv-Rp2pIGjJI1ZQsdvtjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=hnGHXSJTwx54WOa7XA7THDDLAe8kWZHKth1VulztXO8Kc1BzKLvZllEO5C4GiTtBnakx7I9P99zMG_4wBQK5ptYT_b9ofVyfroT1YuSeer_1ddmW4zcHtG7WFBV7uND6-QD4F4jhv0UZ5Kr4pmGEK22xel0522_UQGTLmn7DbxClkWg-i3Mgax3LeBJxTOAXIsg2eJ4sm6xTXoSUMmzPTpNj-RhbtBD1S4UGJXunReOx8oRg0zoZbXVEJf1qaBaytL3vFXahMipvppyQp3nzLkC2mpxZFGKaVKBQSopdrcLjqRFrNeQalf-J645Rpt6bPboXeVQmiWkijdXtTs7T6nq9MfAuKdrca1jc2DDOLuLlzZqVC_uB1DPtLyKJMum01aDONCl2hwOdo2A55ig-uEWfB8MR0MahyIvKErxCVE2gPV3R86j-bmT4o_3ia-hXTGivhBgRNdMIdwyma2Mblf3EhOozuhu6CeE7fT-ANhAik1IS1c8udKV5hjTRSBma-iytcs4rFLIlFFa6T1eBS79eQsIbK6ihlfxzMez3wVwyK-7sP4W69p83hrOqDRs5FGZQwuLz1RrPkf6ursVq8_oL6saw56xHiQ9FQywBpZLbbPGPeZIPlcDikGbWvmhKzzKKo4R7nKy8a3qNX41aUhv-Rp2pIGjJI1ZQsdvtjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Q-it6U2iDklKXX2ebS2NPJmBXezBYwItVxX3AHFtz3kvP5y_Ag9JCIrkA72yoWsVFlAE58llXgnMwtQNfTxnWtT9PXdRAR2ytPbldQ5KQGwA2NB5KMdpz5phBhu_DmWiAaZeh2Ig0ZKYF13859RGEjcVMGvabMD8xTfZtXvug8S6ecGq-U5bA7CbMkYGMyujoAE50hfp6hrm9MTVGIewRRZPxdIEbqeQUidrMKDFybLnAM3ZQ-aK183OAZ-EXb6yVY5wIl6p6K3FBpmO0mNG4h3n4I5xr6wB9Dtn7qs-cNxiOJj2oO2QzmMINCp6pcKfWQkO_FOUyq49BYDyKZoTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Q-it6U2iDklKXX2ebS2NPJmBXezBYwItVxX3AHFtz3kvP5y_Ag9JCIrkA72yoWsVFlAE58llXgnMwtQNfTxnWtT9PXdRAR2ytPbldQ5KQGwA2NB5KMdpz5phBhu_DmWiAaZeh2Ig0ZKYF13859RGEjcVMGvabMD8xTfZtXvug8S6ecGq-U5bA7CbMkYGMyujoAE50hfp6hrm9MTVGIewRRZPxdIEbqeQUidrMKDFybLnAM3ZQ-aK183OAZ-EXb6yVY5wIl6p6K3FBpmO0mNG4h3n4I5xr6wB9Dtn7qs-cNxiOJj2oO2QzmMINCp6pcKfWQkO_FOUyq49BYDyKZoTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3U8CwNKt0cQZMZh3tvQvNRk8In21YntsUHakUgyVDRslxs0dWl98eRQXEjBnRlI6JL8-4gHrKn4aVg4aR_savGs1pudrZ1KwA-FRMMsMrAG4bzbUabkmgHbVzC0WxTSpLqm9D_emLpr9ThmTQabdpwYhY8BSNXZBKbRFREKLLt1JYxphLUUnF5wI-d24rBiCsY7jAMXaTjfwJ0hohZOjDA5KlKlXdCdpF-oACCWnTA8vIYPF02QJVUpkBpH47RGmd3T7vwkTtXLyVqyHqgzFrYVwg59WGQWTcvkIkVr5y3EFWtbm9cOCXL0SIp8zpiE0dxO7QT6ZDsCPfTjdpAf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=mlcznoRn_v2s80YETClPYDdVm9Mxyf-sxaWZHG25-ZC3TB37qNMBfGwixDCtGkNTFfygUJYeTU8dP6qi36qgqBe8v03Seq7yQ3Jvm-9LY26LWyNf5EzjE2eP_3j1JfMzF5fdyE_0bY1tIbpj0hiwHCDgDgDOMdgAlcuNgzPQU8CwKdS_Io-FsV3qK6SO68B8Ri2bnmPE7cvEfcVIirzNkF-9N0MEdRg2aRpN5-VL27LkN5x9cbnA3aivsCzssktcVP389eqOTdwRjSe1DvsK4FhVmtvo_zuE0dXB3mzr-306R5BeAEIz6rCZDB6XKzS1ijOIAYKP1KCDdWJU2_LFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=mlcznoRn_v2s80YETClPYDdVm9Mxyf-sxaWZHG25-ZC3TB37qNMBfGwixDCtGkNTFfygUJYeTU8dP6qi36qgqBe8v03Seq7yQ3Jvm-9LY26LWyNf5EzjE2eP_3j1JfMzF5fdyE_0bY1tIbpj0hiwHCDgDgDOMdgAlcuNgzPQU8CwKdS_Io-FsV3qK6SO68B8Ri2bnmPE7cvEfcVIirzNkF-9N0MEdRg2aRpN5-VL27LkN5x9cbnA3aivsCzssktcVP389eqOTdwRjSe1DvsK4FhVmtvo_zuE0dXB3mzr-306R5BeAEIz6rCZDB6XKzS1ijOIAYKP1KCDdWJU2_LFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM1xjHKYlipx0EGmvVALQom7dRKG--8MZj-fnft0j1W1RDsptPufUYuAH52PaTy1u_FtGlcw7sJsuflnwvVh2xqgfMQBEBQdmg2lWd1LqSdCwcj9NyGeNSzYlgaSbvEfJa52520Zk6pkGftre-ajwknE8co7JAtNfkqCi2-UGhJ0fgRu71xPkaDZM8MUH2y6-ecZXuZFuX84oCw34aWoGjrGvqJZA2RAIE1ddVcbmdMtEMuhF5SkFqj2KUuLpVy3wt2qaVKB9yyC6UwXEjGlt_3g3k_uryIkxIZQIcLGF33BSwnodPIPYp0XKjDCFgl5sVQfo_ioFkr8_Phrhee8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDCyb5fchsK7Yah7J8WAQCl3mx7wUxXhO2qo4v7VQQH85hKyIJZvS2YvOEOGLqy-47bfvtfjE9MGaf2VJV53iIbmvGF5qLkC36gNuZoRxXGlsYWKlG275TXFBLpW5_oMyarcUmVEBZRcl0zSGJKC85JTBqiTOhMCwW7y9OKSVSlPoi8ew2GQDiF3KusQtLL7I-mfDtMpC0HZgQ3nIuoI8FCj86doFTu01DPmKQZ7BrcYTRM1j4sW0GDpfJwrWwdt7OHMSHvuOvK_pc9kl4bhk7w_jv_5nC9-wAjXABIHWw67nHsdq4s2DUZni00qtWo9U_h8ENyS9gQb_m-WYtoSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=XQpKTx9KHuTYu3qh1kfZ4hSwvU21d3uOEPoa0XkOtkAN6ZqvH-O_1yY8fCy5rO4KPeJQIOYZWsTTpIvtWIIvEolcrds0Bs4p1XgvJ4IYZsDF8RhrOi8jSgN-Wbd9MsSE4SWxthFwBTQzvfYh0NI__ZZRZDhQQTkM16NEdJ5VH827JOSbuZO2pV7aR-Y6XfhxDf0x3JbhGsrFQkloDLqaLr_hg36IR8C11QvBcnfORI6y3uE0B7uWmO2OwePNgJCuPI9PLEiJPd9itxo-2XrvA78sccB45m5yXfb3b-OBfmR7fJ6RSG-PQjkCIhZ_p-NTcy3T_17dFyDo8uZO_Yj4cWVAYKR9qGUXaNbHgtIpiV7iEaPgjGRjXARPqelWJwYwR-UR_Vpwio_olSzIAb2YUjLwxInEhvuNeVNYXTVqDuxuOSnE4KOSXMu58p3adXY6VzKEOhg7LgpohRXZpRSgsnAn-IfkwDZQGdoOgswzTa5HCEnm8KQT0pQpSllAHDaO72ppU84jU_FfjU2atx6gHoN8o8Nz44YASlxKPYtR4Ya6MElFnHAbrc1zRv_NqFw5xBrPTkRxnyi8WC5C6630uC-GMmi303ycDlD7pZoTjfDvgRFaLV8QaLA-gQ0DGSedGZevfnWWev-t3jVOniaI2X94QanPlQ0NkAa_sfuv07w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=XQpKTx9KHuTYu3qh1kfZ4hSwvU21d3uOEPoa0XkOtkAN6ZqvH-O_1yY8fCy5rO4KPeJQIOYZWsTTpIvtWIIvEolcrds0Bs4p1XgvJ4IYZsDF8RhrOi8jSgN-Wbd9MsSE4SWxthFwBTQzvfYh0NI__ZZRZDhQQTkM16NEdJ5VH827JOSbuZO2pV7aR-Y6XfhxDf0x3JbhGsrFQkloDLqaLr_hg36IR8C11QvBcnfORI6y3uE0B7uWmO2OwePNgJCuPI9PLEiJPd9itxo-2XrvA78sccB45m5yXfb3b-OBfmR7fJ6RSG-PQjkCIhZ_p-NTcy3T_17dFyDo8uZO_Yj4cWVAYKR9qGUXaNbHgtIpiV7iEaPgjGRjXARPqelWJwYwR-UR_Vpwio_olSzIAb2YUjLwxInEhvuNeVNYXTVqDuxuOSnE4KOSXMu58p3adXY6VzKEOhg7LgpohRXZpRSgsnAn-IfkwDZQGdoOgswzTa5HCEnm8KQT0pQpSllAHDaO72ppU84jU_FfjU2atx6gHoN8o8Nz44YASlxKPYtR4Ya6MElFnHAbrc1zRv_NqFw5xBrPTkRxnyi8WC5C6630uC-GMmi303ycDlD7pZoTjfDvgRFaLV8QaLA-gQ0DGSedGZevfnWWev-t3jVOniaI2X94QanPlQ0NkAa_sfuv07w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP6RN5sz85r28z7QaUVrF6Q_mAeTHD4B3cVIMGFmoSBX1xUtwF5NZLHC-u8ew5CT177srkisJSRVD5y3xGuGSZVhzw89GJPajVaNFt5n0z69eDDoIvgJ06y57H-RKhoRZiSmv9sZdLAUnBtN1IGcK1C3-4Afxw9Vd4Mr57GMCHVOv05AhHXfQoOEl180eUrDW6yCpFqrDcMi0eLyqv2mRnBJLM4o60RLSHyRmMoXylp05ymwj1Tp79L45MVPfNjwUFM44uS8AyEnGaCBMyGXY69T7uH92RVcFITf4KaBrNLqnDOg8OyvyzVjOVtV6QyhKtjB6HHPmYp9S2bW7lWLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0ez6cr7xIy12Sa0VMEWHE89vWyq8ABYed_vBqEArrt1LwxmyUbJpzKN5X6zXPkO0RdYeAK5FK1Pkz3Te3aLSIcz232s4djsucV9MAVEuBKE2dG-HjxgOXk9Sbt9BjcGHdCR35H9AUbxbBQ8n5MNbRu18h9IlARFcz5nOop0crAJ1HhPkUwpYbUlCE7o_4Z3mMV2e0gpjAfL4I2-5O-nLMTBzom6KNujLlAzbn1rkkXzPOEWS_YRnyDqnNFCNsdt571aJnO2121W3Y3jRovXmLUIJj3rnmfgNQxkEaLZu34-QDqf7_quJEF1K12aZaUZhHG5l4RbPZbEaTKteWS74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=tEwugzAn86VgEKwyUYOd3uHPvbLUbNLFyQIDx_OcrFgC8QNqdz7VS2myGxbzjLpn9x3P8zAK9f-6uF8kG9k4hgjkxKbE89nZZRru8_8UrofR12PxmUMZ9yc6RgXQsI5qmigSOQZfMKDsmH2pL5LONi7bwsYm4BApaXx3AXoCdXXZrifbKNBB8g8SBJ6UmPk5YoHmleRxcdUnuFDP5VAKpwCc5n2MLOHYRJtDXRix3EzMCqyVzKGnFLByESlVNuh8FaKtJNWp0m_rt6R_XQtNO-YBP0VQeD21fGUUj8ivA4svzgfonV4YRP33JFBloKkSEw0TMPbCXuTggcF-Pw8Wkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=tEwugzAn86VgEKwyUYOd3uHPvbLUbNLFyQIDx_OcrFgC8QNqdz7VS2myGxbzjLpn9x3P8zAK9f-6uF8kG9k4hgjkxKbE89nZZRru8_8UrofR12PxmUMZ9yc6RgXQsI5qmigSOQZfMKDsmH2pL5LONi7bwsYm4BApaXx3AXoCdXXZrifbKNBB8g8SBJ6UmPk5YoHmleRxcdUnuFDP5VAKpwCc5n2MLOHYRJtDXRix3EzMCqyVzKGnFLByESlVNuh8FaKtJNWp0m_rt6R_XQtNO-YBP0VQeD21fGUUj8ivA4svzgfonV4YRP33JFBloKkSEw0TMPbCXuTggcF-Pw8Wkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=vVgrH7p3Wz9v0o3HFvSOFvgTPnktVRbcxzc7lBktVdq8qAc5jAmwRU_onOGbMVAR-4e-P916l7nKUJRitaQLm5S7Nt-Mms2ckNyetd416iBbUfcg_Aird0yVlyRt6ERP4Vkb5JXR8UKR8AmVFyC5fcKjk3i2xhOJP_2bCaXR9z-xz_IllZ-KWa2QdO_urd0iHwy6sHbixdaxWfCAcD2fFDKf1ea10XBJQ5-aSDgBN1JVz4tdowj7cuxgBvtuNDaSE-BwzyLchsJMxL-4Vnvdy3tH6nAB6bCLPw5xCuoVbxCrpEmWQTZ8jRBohu_ljTTOAn3nrAgh_NfntTucufYQ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=vVgrH7p3Wz9v0o3HFvSOFvgTPnktVRbcxzc7lBktVdq8qAc5jAmwRU_onOGbMVAR-4e-P916l7nKUJRitaQLm5S7Nt-Mms2ckNyetd416iBbUfcg_Aird0yVlyRt6ERP4Vkb5JXR8UKR8AmVFyC5fcKjk3i2xhOJP_2bCaXR9z-xz_IllZ-KWa2QdO_urd0iHwy6sHbixdaxWfCAcD2fFDKf1ea10XBJQ5-aSDgBN1JVz4tdowj7cuxgBvtuNDaSE-BwzyLchsJMxL-4Vnvdy3tH6nAB6bCLPw5xCuoVbxCrpEmWQTZ8jRBohu_ljTTOAn3nrAgh_NfntTucufYQ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=vzmRHdeKra5ohW-e3SSh7VQ3C9oSlj6UusruDioNfQ4TJPlYuuFqP_XUTaWs1tO-8m243ItYbIiNr1gDK2CaEmV8xFeNqA_kntsmPFewxsFje6yR_Kt8q_abvmDsQK2RlZuMy0-4HAzMlnQ94IueK1X7g4PTwTgzeaQP9OPsRX2aW1L4k3CnlY7CHCW8FJzG4SLXju5IkWevBbcyYW4Ml4Y-UD5U1ILyQMe-aDDmm335uRTJUcslQyaNjhJ_6HF2e2H2h3-KYj_tDtZicO7ENINTaF-7k2fu0mMHqNi6nE5ejBl5pDPVrkz86ZhNmgk-hRep1OvuqQrWmxQDdksO-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=vzmRHdeKra5ohW-e3SSh7VQ3C9oSlj6UusruDioNfQ4TJPlYuuFqP_XUTaWs1tO-8m243ItYbIiNr1gDK2CaEmV8xFeNqA_kntsmPFewxsFje6yR_Kt8q_abvmDsQK2RlZuMy0-4HAzMlnQ94IueK1X7g4PTwTgzeaQP9OPsRX2aW1L4k3CnlY7CHCW8FJzG4SLXju5IkWevBbcyYW4Ml4Y-UD5U1ILyQMe-aDDmm335uRTJUcslQyaNjhJ_6HF2e2H2h3-KYj_tDtZicO7ENINTaF-7k2fu0mMHqNi6nE5ejBl5pDPVrkz86ZhNmgk-hRep1OvuqQrWmxQDdksO-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKBg5WW_nF3nWZaRXRx4-2BDUvSchBpgoMd2OIcL1m4fMjqSsPW2hcZ3ueEKT8jZPr0dAUVwbLP22t91qPZqjG322-HdegA-Mh-aqlrLJ6qQYF7xRtY-I8dQ-QeLd59grG-pklUBRl3yCCwe5y52ITSgdUhv3sBPE8PvAM5x2Nt9PEuNeVLUtV9fcoMVJVIX-gjT4KvWUYEZoKoeuRpsIYoEJ6ys-xDWwkVAGoDTw_d4QCb8Wm4HHZ-rkNTwQBppG-xkjVVA2NtoMv2xFRtTu40i1OKVnutc-ixncoM9SzjUkzTpbgARDEWNDy-aKIH89sNUZdvfxiHmnEtDBV1-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8F3DraGYwUhar27hC14r4Mz5Pc5hBKC8HPS7a9uqFrajt_9von6bz-hMH6Orug1nn8IsHWs1RRILJEmjR_eKc7N2aVorD2EPPFUrFEhKHT7u-SyY_oHTlI3qetScVVVwIMevyQVLkV_tw6Hca-CUH3svxEeTyG9rcYIVDKA_x9fqDbTT8zo1q7tzuFJjoupwOTMqQhQ056lLzp2EoNzJQPDL_c3bmx9xI5bgLXSJntDuoWBzSJO8ueGh7AeNQUX7LZIYywby_t-HkXFzyxgBysMfGeM022E9vbx2zFny6lLpvAP40MsqlmM6QA4IjnJa6J0XsuYJBkG-LIq2zj88qIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8F3DraGYwUhar27hC14r4Mz5Pc5hBKC8HPS7a9uqFrajt_9von6bz-hMH6Orug1nn8IsHWs1RRILJEmjR_eKc7N2aVorD2EPPFUrFEhKHT7u-SyY_oHTlI3qetScVVVwIMevyQVLkV_tw6Hca-CUH3svxEeTyG9rcYIVDKA_x9fqDbTT8zo1q7tzuFJjoupwOTMqQhQ056lLzp2EoNzJQPDL_c3bmx9xI5bgLXSJntDuoWBzSJO8ueGh7AeNQUX7LZIYywby_t-HkXFzyxgBysMfGeM022E9vbx2zFny6lLpvAP40MsqlmM6QA4IjnJa6J0XsuYJBkG-LIq2zj88qIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=AYy5qp-7kHqF61aPT7jiYvur5ZIXts-E3g28G4urUXhqbe2gE_hAmNf6krKPci5KTx1c5VdUhQ4Wqqt2V8u5z5GEqeTzGBoHfIiUTGJEOFFq0uwHC7JwRhB5u7FMf7PHqslWD3JPQ92SUEAmSYq_zY8s1cClAkN_tqJWefIqTfYt3RTonISA0GewKEnV4d87o00e3AJw4tOGN9vMCNuCGrQ1NOR3c4P-u56yUjQipfqyb1z4ouc1OPGlLibZqWLpOnup18Q5s3AYPpxYQrcNF2TMrVid579ZIRGKru8ybT-SuFHZYpTr6iIGi9cRkAeCZnokEkMslXp_kZy6O2PU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=AYy5qp-7kHqF61aPT7jiYvur5ZIXts-E3g28G4urUXhqbe2gE_hAmNf6krKPci5KTx1c5VdUhQ4Wqqt2V8u5z5GEqeTzGBoHfIiUTGJEOFFq0uwHC7JwRhB5u7FMf7PHqslWD3JPQ92SUEAmSYq_zY8s1cClAkN_tqJWefIqTfYt3RTonISA0GewKEnV4d87o00e3AJw4tOGN9vMCNuCGrQ1NOR3c4P-u56yUjQipfqyb1z4ouc1OPGlLibZqWLpOnup18Q5s3AYPpxYQrcNF2TMrVid579ZIRGKru8ybT-SuFHZYpTr6iIGi9cRkAeCZnokEkMslXp_kZy6O2PU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilKQ_e5b_tFIxj0ij06GM9VvhGiLFEUfhWKR1sIAJUfOu2Oc_2Dcps6PtrIOPS9Go8bq11PF__wYNalg6Ta8j7iJZWSUx8EWiRCj5jID0-TsP2GEMM_ixINpRu1-jcil0sfue2SqvlO8UAGxIhaqy9g0tjEFPgMd0RG--zJx_6qJew-Wr2ZBe6AgdLJNGbZtuoGOUKnYbLsPQ1JjtDuQT6juaApIYuqDGSsY1-SWgtRPcGKbh0Rv5Ai3xzFo3kMIcEgREIivqE9Ma-7d8Z_cD7A4vxHRKILqvjX8DQLONKq3a9W4mNVxXGO1PpCmZizh0isEqke5AZMASVaknqysYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ukpsBISoyowQ2WN4zJxHBT6nbQme1OH4_BbzvXpx8UbpkWY0v_2AU3wVVvZDMyRYsW6DIFj0EdeOGpJgVlQ0inJAtxiFL7PIj7-7WbsU5zRqOuTxAvDDIMPZ40Q1uxfH8inn69W3zQg2tGrEopDQxLNihlpqUjzAgWXGSBWw9tbbW2ao3eCm9ffnd-ThGsT0BB0YFhAfYqpvDczULyyvojGp9JRYCuX26JKHYjiMCJjTCpck8XREKLsA8qIG9K8iJJQGxu5bBukNBzEF0nH_KOu4-7IPzfZTJzFV9wdiKqRPbd-8fLc1axH_QYBp6iSnLdUkgh5dLvlvNymxhytTml1JVxBRUs2d7DneUS8T7ssVQ2IO7P1tzSRY092b8lU0iSUQUvLc4NqxJ87RaLOEo9-JJNNki3hW_Zlzb-adGBy37iJzy6rPjB3h-VQYUriBNLepqGCa6VE1JZcClciUv6QMGxAPCf_zs35tZHxX1TIwdWaFq1BeOAS-Y6heyxJU_i1W7U04B8uPaGv-UJ54tilE5ZVn8WeX_4oDVf7XuhMM2yoKMyQOB5yg-XDopvUEaS7zh0XfrDeGkYV0RR_K5CcMNEanqF3JJ5FFizOruVEO5R2ryQ82_yVB9ezDzwKdK1NPvPolsx577cv6x8NtKOk4KiMDm_eQZ0q78a1N5sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ukpsBISoyowQ2WN4zJxHBT6nbQme1OH4_BbzvXpx8UbpkWY0v_2AU3wVVvZDMyRYsW6DIFj0EdeOGpJgVlQ0inJAtxiFL7PIj7-7WbsU5zRqOuTxAvDDIMPZ40Q1uxfH8inn69W3zQg2tGrEopDQxLNihlpqUjzAgWXGSBWw9tbbW2ao3eCm9ffnd-ThGsT0BB0YFhAfYqpvDczULyyvojGp9JRYCuX26JKHYjiMCJjTCpck8XREKLsA8qIG9K8iJJQGxu5bBukNBzEF0nH_KOu4-7IPzfZTJzFV9wdiKqRPbd-8fLc1axH_QYBp6iSnLdUkgh5dLvlvNymxhytTml1JVxBRUs2d7DneUS8T7ssVQ2IO7P1tzSRY092b8lU0iSUQUvLc4NqxJ87RaLOEo9-JJNNki3hW_Zlzb-adGBy37iJzy6rPjB3h-VQYUriBNLepqGCa6VE1JZcClciUv6QMGxAPCf_zs35tZHxX1TIwdWaFq1BeOAS-Y6heyxJU_i1W7U04B8uPaGv-UJ54tilE5ZVn8WeX_4oDVf7XuhMM2yoKMyQOB5yg-XDopvUEaS7zh0XfrDeGkYV0RR_K5CcMNEanqF3JJ5FFizOruVEO5R2ryQ82_yVB9ezDzwKdK1NPvPolsx577cv6x8NtKOk4KiMDm_eQZ0q78a1N5sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD61I9239Fd5BLkT2RsJ4Nbtlsv5C0u_x12ndxHaepvuw-mkFs-f_ioZXSW3T8j_k9eNwkHQfX0ifALPS_HUveQat73x24w8bBlz6NcCu-HpcvQIAwWb7KEG0ql4-ADs6w0yyzvI6Ldch8p3rgp89T8JvNY6tvYWMiybvgWDWyYl8AZ2BH0Agoz8O4XBuQuZZL6AMWP1TPCpvD48gRuee3xRHeGAcKGgqDtTx9g3awY6_bc4KK7DVATxFt5oDzTS8320tWSOaHsifRJhIGafV4wXt1As4AcyO2E529yOphZQkk1ERA2CIrZkUlfCyb-joWm0rzwgniLEOWUh-kdrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=j9BJhTzgC14mTRPkTnVaeRveByMLn2dy85-rnqSwATfOSed-3RfCayOEMA0Ge2jWRf1rCqS-QvOhV2vEV7lDm4DQysrAYQAZF9HNN_AOqMsEMSp81uh9DyV4BFCzzzYNxXFKDxVi1-lWvcKdI-QYgTTRwsrPuTw2kEnyEXuqJcR9IcePQWJkCQHoW1_w_xOkxYLTiuQ5YcfnuKVt7PpBbdVg4oHBKbbY0i0g-lPg6W_ctepxr4tQVB6SBiG7LJeLw-5jZ5KeQMRDyQNIbC8Qt_v4lH3Bfc9J2G3oIGL0ZyC6l9Um_g-gqX95eaE20M1OG8JVZlKwuEJUQCzj5CbM8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=j9BJhTzgC14mTRPkTnVaeRveByMLn2dy85-rnqSwATfOSed-3RfCayOEMA0Ge2jWRf1rCqS-QvOhV2vEV7lDm4DQysrAYQAZF9HNN_AOqMsEMSp81uh9DyV4BFCzzzYNxXFKDxVi1-lWvcKdI-QYgTTRwsrPuTw2kEnyEXuqJcR9IcePQWJkCQHoW1_w_xOkxYLTiuQ5YcfnuKVt7PpBbdVg4oHBKbbY0i0g-lPg6W_ctepxr4tQVB6SBiG7LJeLw-5jZ5KeQMRDyQNIbC8Qt_v4lH3Bfc9J2G3oIGL0ZyC6l9Um_g-gqX95eaE20M1OG8JVZlKwuEJUQCzj5CbM8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Nj3QmR1oifzUF9rfU-h--EZODzLP7ni4f1DHsdvhZujo2SQPvUlSpd_bjPdKZCpawr3RwxVvJq4A61Xh9cc4WJljE7CkHYqAmyEUheXUfKeC6Q6IE71c9gd0N2EKjTM4LMf_8uSbn5G_xPV6Ru89rLt1tyD1tEg9LR05f3ssamOHN7Ns3r23LM8-PXLXvhbVg9uS0Ixc1g6fEyGZ7rrBnR6grD37rmCvJv7ZDzQPZfpP_0yvoVd994dK9jDIrN0SODyFNmG_p7vyu6BnpsPoSFB2hsP4KN1ZrzAORlifXKnkKH9upKMePiPfkISaHCSPf4yl2S-VF8e4bVRco52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB2_8j4zSA-xOwn4HAbbzd4ZyEWeHR5cQyc6znzTzYUIEvzWJQRjBnoCfEIt5OJSpFZYYZP6Pmc4xOlfVHJMTLTK2y5OCN_aFcW2uLWI7c8dmH6jvkizPIYshIVUPz1lVqnHi3fqEwMxfLUOu4CgTYPlTi8NouReWBMwzOC8Th4E2HdQL6uWa-BDPbSvtZKQ3x0dbx0n_D5SAh6fNy6z673OJkwLgEkoP84wro9QgosmAgyzynvwq805jAYo7RN3V7ta-KugF9obUyvjg3pc2ay1OS41snFY9U_flVKmW_x4w13UrUvjz6YyyBB0yIVuBZVe-r4U-BQei9RZxcCLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_TmCHZTjAG-ZIeCAoIXdxJIOVwXOCRWCaU1vbnzsKx9bew0Bq61gH91smb3E4bgUyqlM5o3eeqahvCD15GIzrvVKHvNh-t3Jv5_SbsxLyfe2tS3lMwsz2z0Ev627OL_Ol_gj6v7RdB29IR-MO2wo_NiLtsW0ZViCti5l7bztdtgUDecWMBNH7WRhQA5fbv9lOKzL8B4ZSAHCSJBPYUg8knveq3aq6mKjDZR8eEUItoRd9K7gNOzMSvCGQ7kiX2oK5HA84g8Fx7XCI5eq_nhABiZlzgUI8ylbliWQnbdFP4l45iP8aJtDhQNye3vmI8Tltar4bglTMMgP9zUIFdGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Oti9o669S4lmtJgWWYUiDtyAwGZJQVVTJIjjgBBN5Q9nV1YmEScVeXsWcPhtCnJ98IVs0Cx1_A3CQUbFeCkREs-CGKFoFsLJ5PJ9cT_uKls7ZP0wZMIWDiCBFUdnS9HsDP6nO1JVgvYi2AJ0mwVX9N0bX0lxwGLYHzp0RObEAdOE6K2cbsWYjoRDCEklck__UEgC0BpTU6YO9pwNbdGk5nYLIs_-XVuEBJtGzW_8T72T65WGv0nwekxexOI-oGWTZujJwbQY5PDhdPEZ8Ib1_wFgdhZNqlJoVwI2pWa-FQ15TNKyzPdeqTxX2Du3ZxN5h5eM-VP-wqhPG0n2a8mjEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Oti9o669S4lmtJgWWYUiDtyAwGZJQVVTJIjjgBBN5Q9nV1YmEScVeXsWcPhtCnJ98IVs0Cx1_A3CQUbFeCkREs-CGKFoFsLJ5PJ9cT_uKls7ZP0wZMIWDiCBFUdnS9HsDP6nO1JVgvYi2AJ0mwVX9N0bX0lxwGLYHzp0RObEAdOE6K2cbsWYjoRDCEklck__UEgC0BpTU6YO9pwNbdGk5nYLIs_-XVuEBJtGzW_8T72T65WGv0nwekxexOI-oGWTZujJwbQY5PDhdPEZ8Ib1_wFgdhZNqlJoVwI2pWa-FQ15TNKyzPdeqTxX2Du3ZxN5h5eM-VP-wqhPG0n2a8mjEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSq2rPyC_z2qoZgKw_TLOeILPzIu2N8kA9uE64mvCUOEeiAQKUv7trQtiP_ulMwIJW0YDufXAmf8Ok68aT_yXzL2oU2VY_tSXc-ajnMOTU3zdclBBMeE4emDoZ-8ajPcSEKHvVIlyckZiPfcGy7He3qLMBvJ3pVoTWbqmKCGdnNH313bL5vT34Boh_Apv__gWkZAe0X3PUmy_hQpKsv4ygDXLetyIDCu6gn6lItI_ehAOutbl9VM1KoJ11u3E8QESUrBxcmZ-aCnZg7ZyBUAmQehQMH78modR6MHZSmfusux72W1fsDr7ky5KjT_jxKtCHIywYSiiPDSVEjaxHCOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0b7RhN20Ou1p5C8JgUuJZxC4bM4fXnVKWsSkeF6dIOcV3B2EQYWPaHVl0dnhJNURMac2uqFftLbcxqfm66vC5ol-Ry1T5UdeVVG2k9fN0FP6XKJzKB9swxe4dIgwAWXpNudJDNSZGS4FdSxMTNXMngMkut0tEug5xqbpGKppPu7xm3hSLGQ39ATEBYMYHqXv8Pv4M9bRvVL_BPXL1UJan5n1twOSETjnXhCJl6vY10USDLh4xhmw9UitAP4wDYA_fx6JhIg8Yeib17X8plKA4NaY2-KVjF-pfJDeoQpYDUeSk3U0NmcDeG9L_veke7wn16na9mayovDIvgA94-aqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0b7RhN20Ou1p5C8JgUuJZxC4bM4fXnVKWsSkeF6dIOcV3B2EQYWPaHVl0dnhJNURMac2uqFftLbcxqfm66vC5ol-Ry1T5UdeVVG2k9fN0FP6XKJzKB9swxe4dIgwAWXpNudJDNSZGS4FdSxMTNXMngMkut0tEug5xqbpGKppPu7xm3hSLGQ39ATEBYMYHqXv8Pv4M9bRvVL_BPXL1UJan5n1twOSETjnXhCJl6vY10USDLh4xhmw9UitAP4wDYA_fx6JhIg8Yeib17X8plKA4NaY2-KVjF-pfJDeoQpYDUeSk3U0NmcDeG9L_veke7wn16na9mayovDIvgA94-aqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Ujrpwro2m9HXWworQrhgSMKlL_gck2upzCYXwzJmHFjGsUBtZTXDqBCAwJqnU1dXqcjY4yGc4HMkNAoy45LcV2CFR7kN5-3RtsEWtcWYtirFu7n9em_OHvIF2MxKROMTy8vYWV7Qbu6OzVJEMURJAuXi6Lajl3zx7L2c6MSBhKeXyhtfvm1sa15r1Z9W_lhzz9ZHN2JD5bc6u_Yroc-I16mZxxOJXpZBBfEARygs0iGYZgQC1FFVrs-L3wpAGvXdYsFDcnnub39afKLPeI39sSlBf4N4l0VEzNHeC71RgoImMrYkM67V7Q4NurLS4aJPD1dyBF8birfI8gkKjfShNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Ujrpwro2m9HXWworQrhgSMKlL_gck2upzCYXwzJmHFjGsUBtZTXDqBCAwJqnU1dXqcjY4yGc4HMkNAoy45LcV2CFR7kN5-3RtsEWtcWYtirFu7n9em_OHvIF2MxKROMTy8vYWV7Qbu6OzVJEMURJAuXi6Lajl3zx7L2c6MSBhKeXyhtfvm1sa15r1Z9W_lhzz9ZHN2JD5bc6u_Yroc-I16mZxxOJXpZBBfEARygs0iGYZgQC1FFVrs-L3wpAGvXdYsFDcnnub39afKLPeI39sSlBf4N4l0VEzNHeC71RgoImMrYkM67V7Q4NurLS4aJPD1dyBF8birfI8gkKjfShNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Hfv-cvRsfZNS7Ak_LzkMYqTDYZRpLciUSVpa6yECvN-Pjghj22HqrehTaC9jYtplfYpgralkrGBc_OCN5dzSUKFWvUZ27E-S1EJHMOHPL_9X62R0zicHrkpoiz0swCrOtRt9DlwZZ_UpeUEL7JMrcp9VcRtaEKzes-6d9V41GieMLpQwbk_9BdeTFR-26BfGexVOdLSrcDfoxwMEcrG9FRIiF69EsqdX3LWo7slIt1zY2I_uQlhMrjrue9tAjzHBkxLr1mxtbnUKNG1S7GWsO_fUKCyyT-j-9ppMvqL_UCEEDFFFURGsyEdvcZE8BJGZYWLx95ZRgUqz78MMGOUHzUbdg045H1xeuE4TMYtEwpU8f4v8bIOdBjLCdYZ7HaQdaPfM1YAo1j5HCz3zHYeg_H7cICvt40ziTgIfEPrNLGIN3JIbjvzr2Eqa71wZ6mxeSAP13I5-ZqwJkUt30W4k9iLuM0h-8G-Inc1j1vrML0an1-aKtA78jR7p7-tERM71Hxj8nHb1Jg0DCKuWNyXfLmk3aEAJVVna9j6hpW44MtiuzUK7SgZq4-orqJplV-5jDXWe96ZcVqK1UPkRtdNu6HaK2SjuLbbPE6RMn39LDXwQSuoC-YwoY2DX4w3e5f32X-0uDKuwEhXhN2GLMX26np8zTPkfHtsCuauwdBdtcuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Hfv-cvRsfZNS7Ak_LzkMYqTDYZRpLciUSVpa6yECvN-Pjghj22HqrehTaC9jYtplfYpgralkrGBc_OCN5dzSUKFWvUZ27E-S1EJHMOHPL_9X62R0zicHrkpoiz0swCrOtRt9DlwZZ_UpeUEL7JMrcp9VcRtaEKzes-6d9V41GieMLpQwbk_9BdeTFR-26BfGexVOdLSrcDfoxwMEcrG9FRIiF69EsqdX3LWo7slIt1zY2I_uQlhMrjrue9tAjzHBkxLr1mxtbnUKNG1S7GWsO_fUKCyyT-j-9ppMvqL_UCEEDFFFURGsyEdvcZE8BJGZYWLx95ZRgUqz78MMGOUHzUbdg045H1xeuE4TMYtEwpU8f4v8bIOdBjLCdYZ7HaQdaPfM1YAo1j5HCz3zHYeg_H7cICvt40ziTgIfEPrNLGIN3JIbjvzr2Eqa71wZ6mxeSAP13I5-ZqwJkUt30W4k9iLuM0h-8G-Inc1j1vrML0an1-aKtA78jR7p7-tERM71Hxj8nHb1Jg0DCKuWNyXfLmk3aEAJVVna9j6hpW44MtiuzUK7SgZq4-orqJplV-5jDXWe96ZcVqK1UPkRtdNu6HaK2SjuLbbPE6RMn39LDXwQSuoC-YwoY2DX4w3e5f32X-0uDKuwEhXhN2GLMX26np8zTPkfHtsCuauwdBdtcuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=l17CBDcmlh8bG9Y7M5t46hClHAGcBmaFObys8VG0xmoFD6FRFYZR3UByUVGCwJ1AJIFl_P5r3zOTjqov59xt6gJFnwHc9QvGhlyIcqqXxGjmp_fiFklMMlL-AmtcnJy-Sg0eUAhwxfnx1AEMWm6N8zj7gB8rvpFaxJwohy7zCoezwwyA9ZxfCN4OdSmQW78lAkxA-F1_8R4qVBZN5Rqr_qVXR3IOF6h7Ye79b0ecT8r4wNXuaJtcnVgVtdoDKYT9ZGYH-5yrJGQS3xDfxZGqHf5AJTv9pNLAdS6IK_YmVEsyjJHi6vsZoaJObgJQhWnK4gkQmbNCgvOe59TMoHRhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=l17CBDcmlh8bG9Y7M5t46hClHAGcBmaFObys8VG0xmoFD6FRFYZR3UByUVGCwJ1AJIFl_P5r3zOTjqov59xt6gJFnwHc9QvGhlyIcqqXxGjmp_fiFklMMlL-AmtcnJy-Sg0eUAhwxfnx1AEMWm6N8zj7gB8rvpFaxJwohy7zCoezwwyA9ZxfCN4OdSmQW78lAkxA-F1_8R4qVBZN5Rqr_qVXR3IOF6h7Ye79b0ecT8r4wNXuaJtcnVgVtdoDKYT9ZGYH-5yrJGQS3xDfxZGqHf5AJTv9pNLAdS6IK_YmVEsyjJHi6vsZoaJObgJQhWnK4gkQmbNCgvOe59TMoHRhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtqWlG95NfwJt2xBCNCeHlbcqzKifBBaBuIyO9fgWWecZ2Rh91fg5lwlCp5cigNIlewgGeGlwzY5ju1G58xkpnkZFmUOUDSHz12RAHSh7vnmW4wuxR8M71JxqZsBTnV2nn9F_Yg-4bo7WyN6dnp6pc4BdNdFMzIDuVE5e7TzMxM3sFxadMLZx4XWkKRhRu7cbewImvjDJjjYMvI_qR3w92Fj4xmzfqSAoJ3KSb_oGnHASxoBURykXND20kMUW4gG51uDGY6pVjViulaMpHUGLRk5SN53qonTs23MCMXUPXbZScHaVW-iXo_htUzp_qgqtKu2oHQto9ZPsll627r-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=nFrUwlzvVjYWMrWYH_vLjensYqC4QsO2OTZbVJ4dqZQCBlNlSfaJgc2P27YCCE8m5Tqh9k_ggazHzGINupTjbRGoXv2XqbMr3dds4xfB_7z8NluiIoschEPRbSreSkGDmhtiGtz9jIREKYmBcZXTtt7gwBXBoQdHD7n3Ot0eYUtbhoGSfqC_GfRWabN4CGpSIeQB4yOu9ljsFrisqp-F1_otQMI--phqKrv-W7KJUgcbTcH4GZz8mXXjusCny1XlUvjo5-_Gbd3F21Dp3_Nzdtv6erOwJCmHcDe47CND1Yz4eYjW4E5Vyg_VEx0EYO2t-Kyu_i5yBplsX58ZmYRI0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=nFrUwlzvVjYWMrWYH_vLjensYqC4QsO2OTZbVJ4dqZQCBlNlSfaJgc2P27YCCE8m5Tqh9k_ggazHzGINupTjbRGoXv2XqbMr3dds4xfB_7z8NluiIoschEPRbSreSkGDmhtiGtz9jIREKYmBcZXTtt7gwBXBoQdHD7n3Ot0eYUtbhoGSfqC_GfRWabN4CGpSIeQB4yOu9ljsFrisqp-F1_otQMI--phqKrv-W7KJUgcbTcH4GZz8mXXjusCny1XlUvjo5-_Gbd3F21Dp3_Nzdtv6erOwJCmHcDe47CND1Yz4eYjW4E5Vyg_VEx0EYO2t-Kyu_i5yBplsX58ZmYRI0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=o9kZutTCF1r33tibaDAgezzn7IDVhxDDuOONXfgyRn4kdQHEBzLHsds8HKCDLJHAcRSePdwW1rdF04kou9elUfuNbFesAvb5xGBjsVQbbo1E9P8anJPfa4TN_TpJsrrRatFWmyvSqxqE1dbihgZcanvmIE8XGvP21qHtJHnUF2mPib5a7C1n9Gd6E5CqR_-Z1G7RSgYeOKGnejG7nAlRYd2Rh7802ZQDr5-3yh-qbjLoFSHWJsqeKYdzFucGBcdP7CfCUEyBGzxE5_PG3QrKkzZGzFktD4UWJ06-0diTgx4eg57D7MPXHF0dc9l7C-2AKFXLRkElX4Z_34Pwa7JwHp8igfmLP_GLHAXxb-aKsR3i9015bxE6GzrV-RUzaIEQzrAGR1_1YbsFoWTxz_9jpgxc_Bixm9I7CTdXD5Ma_kOBMeyNtfoiKWXLsPy37sOw29YZIxTAk_iKorKv9yNjtKnGITz7RtUqWx1WDk8hwGR-F60k6wQI9CUnnrJ2KSQtatl5sxBkdHxXi7_S4D_ele1QJxqi1WNuOfF-6p7vaYpEjy9SAamBMDBUdww2_EFs9SDlbjex9z5gn1TQ64Zu4f069RP9HLW2BPwBSTW_tuZKuNl6Mtoj7WtpoDIrnOagE_Zbk2yWEGv-C_m9W_Vcyb6q-13_5TCli0o8kNkClP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=o9kZutTCF1r33tibaDAgezzn7IDVhxDDuOONXfgyRn4kdQHEBzLHsds8HKCDLJHAcRSePdwW1rdF04kou9elUfuNbFesAvb5xGBjsVQbbo1E9P8anJPfa4TN_TpJsrrRatFWmyvSqxqE1dbihgZcanvmIE8XGvP21qHtJHnUF2mPib5a7C1n9Gd6E5CqR_-Z1G7RSgYeOKGnejG7nAlRYd2Rh7802ZQDr5-3yh-qbjLoFSHWJsqeKYdzFucGBcdP7CfCUEyBGzxE5_PG3QrKkzZGzFktD4UWJ06-0diTgx4eg57D7MPXHF0dc9l7C-2AKFXLRkElX4Z_34Pwa7JwHp8igfmLP_GLHAXxb-aKsR3i9015bxE6GzrV-RUzaIEQzrAGR1_1YbsFoWTxz_9jpgxc_Bixm9I7CTdXD5Ma_kOBMeyNtfoiKWXLsPy37sOw29YZIxTAk_iKorKv9yNjtKnGITz7RtUqWx1WDk8hwGR-F60k6wQI9CUnnrJ2KSQtatl5sxBkdHxXi7_S4D_ele1QJxqi1WNuOfF-6p7vaYpEjy9SAamBMDBUdww2_EFs9SDlbjex9z5gn1TQ64Zu4f069RP9HLW2BPwBSTW_tuZKuNl6Mtoj7WtpoDIrnOagE_Zbk2yWEGv-C_m9W_Vcyb6q-13_5TCli0o8kNkClP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8hF9wG-_5ceO-uC-AV4D4mzH3Zqedan_wOPmGrHiwa1G6-HVZGYPp6bBgxDHfF--bUEjKVZ5qmQuiugP1uAdOPPinImc3hJAyTESJZBaZdHpueef62E47HegQdIeiE4rnzpYioGIYLLPE_7nXqwMOli2COvozBp4b6VZ_KyXClroQrCSVfqt4uDPXHK8IRls4RD9nQR3vRqnCk9Ww592aWaP4yJ2VrWkTDGj0yUebw6trZURJLE7--Tv3HFf0QVhz2kfA3EW8gItvOJ8ALrwNEsYRGyXCPMs4qEFGbkV1dYDV1H-xx8k6df_2P_y61-Pt5tJxIEF4_DLq5ye8x2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=LtkunN7XnIE7vMZfk5rCz5mMGs7qRdNNGM1MJhJbedFfWxqBrin9xJN8Wuts06iLt6CkZkR7VXZHwBRjStZhQ32cE9Slge_hUhtOy3z8c6nyTG3Rf7Kny7RYvuFO-IwkuoSjaOWVbFlrRnnIkJnZEpDnTakgxdk7QNIJV6N6j1UEwlHndpn8IFA7ccWjOUFSRdItBbvci1dZZsPNUQ3zvRbyzueH_aonWJDDCcqy_28jTV-IG7GxOFzmIJOSRa7Tc0S9iMYIK6KrwSMRuDF6DPEbPkV7Weq9hF_uScBOZvJ5JUtyXgzL3ifPJgP0Pw_DvDXYa_uiDWUXUEqlna1Gr24ZLDO6WGpRQto7Tsv0W8ZfdmWEOy-vzRAhhTep2eenI5wfNerCQKP1iqMGTvQOLHvyqtBen1XVozSrwV8i2iokStQIHmIPR8XnqZvNNCrIV1V7To68VwF3P2KvqqFmAR-BPCkNXkxpoIY4q7OXtTk_66xbwcVareEWz59JgErnGqmf-1WS2LI_DVQktWXv0sM7f1uxjoqvPXulhHvyV8ydvYcNFG5lyY8YlJS32yiK0yb3c13uJ_5kx_vUqpYgXSr2tQudTcRtPC0yokzrkAKA1WtyogiJYgH5mWk7ByrAKyVumts4LFGqM5EqzKlyJtR2vULZgnaDMauXg_Jbuxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=LtkunN7XnIE7vMZfk5rCz5mMGs7qRdNNGM1MJhJbedFfWxqBrin9xJN8Wuts06iLt6CkZkR7VXZHwBRjStZhQ32cE9Slge_hUhtOy3z8c6nyTG3Rf7Kny7RYvuFO-IwkuoSjaOWVbFlrRnnIkJnZEpDnTakgxdk7QNIJV6N6j1UEwlHndpn8IFA7ccWjOUFSRdItBbvci1dZZsPNUQ3zvRbyzueH_aonWJDDCcqy_28jTV-IG7GxOFzmIJOSRa7Tc0S9iMYIK6KrwSMRuDF6DPEbPkV7Weq9hF_uScBOZvJ5JUtyXgzL3ifPJgP0Pw_DvDXYa_uiDWUXUEqlna1Gr24ZLDO6WGpRQto7Tsv0W8ZfdmWEOy-vzRAhhTep2eenI5wfNerCQKP1iqMGTvQOLHvyqtBen1XVozSrwV8i2iokStQIHmIPR8XnqZvNNCrIV1V7To68VwF3P2KvqqFmAR-BPCkNXkxpoIY4q7OXtTk_66xbwcVareEWz59JgErnGqmf-1WS2LI_DVQktWXv0sM7f1uxjoqvPXulhHvyV8ydvYcNFG5lyY8YlJS32yiK0yb3c13uJ_5kx_vUqpYgXSr2tQudTcRtPC0yokzrkAKA1WtyogiJYgH5mWk7ByrAKyVumts4LFGqM5EqzKlyJtR2vULZgnaDMauXg_Jbuxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pkLs6vVr36zH5lnWpKvCT8AEX2cU5D3zylsh1f-0SZVnNsh9BdQT2YDwpmb1C6Zkc15Z2h39B2eD0Ph38dKwDbtkQjZe6yEKydNO7v1eem6h3f8TH14sHYdYZ1-y_Qm_xCGGzmS79OFY5QUe_1PzarUESDME1DGuRQGKG5ljDNUUjnhiVWBcH8DwR1bCE2KohuhJcXcFlv4C-AMpgFUxDvg13ch-UT8mbU7o30XSGA8o_4HgeNsKcXaDcdb4N7A1sTXaF4isfpRLqpkZkSDi47UccjeXwcAykmiX1NHK-DcYqiY7Yw3zUJR-_KX0-QC3zhM7XbQxDgxlrla81wPY6yJH3IEQf1gkYKTkOo0LGStH2CIoCBiZ9EJBn8Q007eT83Ng4Jj3j4w2lCF6X7O_gz4-VHxVwOjjrAMn9AvjExgroFYr7v5Dk8QFj9yBfO_n0R8vzi1OWZg3GjIJTDUtU8QoXqm8XiNVucTPEPfeurC5OhqsflIC8ONJo7__bPL92PHKz0PNgy_AUQ6iWF1uFhRW6pSrhbvfZ88IFFjNew9cIilgMolfHsH3SDnSyOTPZO4K-fGecWhAk5DbZ9KzRG4ZH16owAPRrvVZl9nRdAA4kkJ7Ke3y-2imi8_MQk-SOiSCtCiqtJxluExiIcqatfn8x7wU6IQLc0P0izPf_jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pkLs6vVr36zH5lnWpKvCT8AEX2cU5D3zylsh1f-0SZVnNsh9BdQT2YDwpmb1C6Zkc15Z2h39B2eD0Ph38dKwDbtkQjZe6yEKydNO7v1eem6h3f8TH14sHYdYZ1-y_Qm_xCGGzmS79OFY5QUe_1PzarUESDME1DGuRQGKG5ljDNUUjnhiVWBcH8DwR1bCE2KohuhJcXcFlv4C-AMpgFUxDvg13ch-UT8mbU7o30XSGA8o_4HgeNsKcXaDcdb4N7A1sTXaF4isfpRLqpkZkSDi47UccjeXwcAykmiX1NHK-DcYqiY7Yw3zUJR-_KX0-QC3zhM7XbQxDgxlrla81wPY6yJH3IEQf1gkYKTkOo0LGStH2CIoCBiZ9EJBn8Q007eT83Ng4Jj3j4w2lCF6X7O_gz4-VHxVwOjjrAMn9AvjExgroFYr7v5Dk8QFj9yBfO_n0R8vzi1OWZg3GjIJTDUtU8QoXqm8XiNVucTPEPfeurC5OhqsflIC8ONJo7__bPL92PHKz0PNgy_AUQ6iWF1uFhRW6pSrhbvfZ88IFFjNew9cIilgMolfHsH3SDnSyOTPZO4K-fGecWhAk5DbZ9KzRG4ZH16owAPRrvVZl9nRdAA4kkJ7Ke3y-2imi8_MQk-SOiSCtCiqtJxluExiIcqatfn8x7wU6IQLc0P0izPf_jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=v0EA4gEdtokLmvgXke4YppGVSQw2c_O56HLAORFey5EzYwJ_ge8KEKEpccjjR-Wviy0fhM2ALzuMEyh8pnF8oQ4m4emKwLEprWVKX-NupNh-3UvU7ZBvrOYE7mmC0XTrGtvf-mIHzFMD82JuRSC3EBs0OvWJy4eBJf_O0AewU-s1VPJsC7MJV4jR9zTveOoe1fAGf4zkjqBI8TRsQuKK4xKdflKxFpKlLR411XKFx6aUYhkdI_x-JTpC2XCAWvWUSkiifBeIpd8FcAgMl8NwPM4UVFyEq3P1USPFy1uWxmKi6qUaU-cmcOd6meYAjphucYgeuiADewFjHrKkXt4L5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=v0EA4gEdtokLmvgXke4YppGVSQw2c_O56HLAORFey5EzYwJ_ge8KEKEpccjjR-Wviy0fhM2ALzuMEyh8pnF8oQ4m4emKwLEprWVKX-NupNh-3UvU7ZBvrOYE7mmC0XTrGtvf-mIHzFMD82JuRSC3EBs0OvWJy4eBJf_O0AewU-s1VPJsC7MJV4jR9zTveOoe1fAGf4zkjqBI8TRsQuKK4xKdflKxFpKlLR411XKFx6aUYhkdI_x-JTpC2XCAWvWUSkiifBeIpd8FcAgMl8NwPM4UVFyEq3P1USPFy1uWxmKi6qUaU-cmcOd6meYAjphucYgeuiADewFjHrKkXt4L5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=aJIKpqK_SPUu5qWN4qW-sQGlhnx-_S76qYB1CxfvoxqIP0ALBztc1WQHWtdhVNJoNwppeUADQaPqkLwLYh_xjsjrdkHgnsUZybaFqkrcNo6S0Gx6Qy4WBDoEheZhbwNdI0DANYUBaFG7gaNXhimvKR44fjDweSrPWCcdZEG7NvyRETnxiO4VgoHx1rzQ3PIvmOXo5l_c59bb3EnbT1ehGn7yAyQLJE6VRpIwYAWMW2-cM6_7JfBaj97qbhUH3NcY1UIR-qPr1L3PcRaqcQrxK5b1vs-g-uxEbibld3q1Nx33ubgo-as-MmxJHg374RejcLBs0YLC9GGNaPICyfbR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=aJIKpqK_SPUu5qWN4qW-sQGlhnx-_S76qYB1CxfvoxqIP0ALBztc1WQHWtdhVNJoNwppeUADQaPqkLwLYh_xjsjrdkHgnsUZybaFqkrcNo6S0Gx6Qy4WBDoEheZhbwNdI0DANYUBaFG7gaNXhimvKR44fjDweSrPWCcdZEG7NvyRETnxiO4VgoHx1rzQ3PIvmOXo5l_c59bb3EnbT1ehGn7yAyQLJE6VRpIwYAWMW2-cM6_7JfBaj97qbhUH3NcY1UIR-qPr1L3PcRaqcQrxK5b1vs-g-uxEbibld3q1Nx33ubgo-as-MmxJHg374RejcLBs0YLC9GGNaPICyfbR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=cORoTWu4NXJV1UuxFGm85n-Vw7lo0FcSXEzbi-UDG9OolbJMD0gFl-JO4pOXMnQpzlAGU0ONvhNiqiPWPOV8FWf_zSv5qfrZGVHkpGuEOpw3wyHd1dVqFNAQitGdjs1w0NHSPx_Nfmsa8ljZ78_wYjmCXd8J66x5yFsKytG1qu9A0eEjsMbgy961oKA3Wr0k3b91R97Opql4J97OV_5Funp2CFec6K968dTHI18C4PW_NZqstJ2hxCmg2JRl-3FECsmFN4OnlORjxsFoZNasx8-1WX2qURRzRV5XiGnj2PYslFgPuMhKUPvt-p2VhGjjUtfxo6HRP1G0AINYn3lK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=cORoTWu4NXJV1UuxFGm85n-Vw7lo0FcSXEzbi-UDG9OolbJMD0gFl-JO4pOXMnQpzlAGU0ONvhNiqiPWPOV8FWf_zSv5qfrZGVHkpGuEOpw3wyHd1dVqFNAQitGdjs1w0NHSPx_Nfmsa8ljZ78_wYjmCXd8J66x5yFsKytG1qu9A0eEjsMbgy961oKA3Wr0k3b91R97Opql4J97OV_5Funp2CFec6K968dTHI18C4PW_NZqstJ2hxCmg2JRl-3FECsmFN4OnlORjxsFoZNasx8-1WX2qURRzRV5XiGnj2PYslFgPuMhKUPvt-p2VhGjjUtfxo6HRP1G0AINYn3lK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tD8kOvHsqnIPbomSWHvvszgJBqiQNx60-CNnuC5UX6H3-dcH7g8Ce8M4mtUGLnGaM2unT31U7c0-V5HGgX3iYlgn1kzpCerlhs__FhF3JZ10_0L8ZWsfB3qkzosku7xqIElayahEofDXGk0sUFAWIiL_wroI0leXyHRcaGBHBy2JLwpU7PHaIevWQRMK5Zs9927QHDNhGeyG2TexSjAylIVN2b56pL7DG4zgP32c_NxBV-ZPxCCx8qdR_P326uFD7i3xIbtmFqA4tYkptDkZpiLFsJbFBvj9OtGvEvQS_bnaxALy-LrkieZP4DpK2IWaj2-tSfPc6vNBC1eXy-0UyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tD8kOvHsqnIPbomSWHvvszgJBqiQNx60-CNnuC5UX6H3-dcH7g8Ce8M4mtUGLnGaM2unT31U7c0-V5HGgX3iYlgn1kzpCerlhs__FhF3JZ10_0L8ZWsfB3qkzosku7xqIElayahEofDXGk0sUFAWIiL_wroI0leXyHRcaGBHBy2JLwpU7PHaIevWQRMK5Zs9927QHDNhGeyG2TexSjAylIVN2b56pL7DG4zgP32c_NxBV-ZPxCCx8qdR_P326uFD7i3xIbtmFqA4tYkptDkZpiLFsJbFBvj9OtGvEvQS_bnaxALy-LrkieZP4DpK2IWaj2-tSfPc6vNBC1eXy-0UyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ZmOFoD1R3LDSI8XgN6isMTV8ACKj6YoiC57YyO1pTsV1xKylAkiChbvMSgxKCKfCiPqbjr5HAVoIuSuKUdpZywMcrifCASaSh-ffCxzj9U5YoSWtYF73m7j0PG_5bI1QdR45pi0SpPK5CKet6cDxPwI_Ja7byMJx4l43UCeiOr7klSfECIY-j7u0EvDHZmMjDZqUg2uVznzKALbUpimfYiV53akTsjCTKMQ4vgmxst4xya_D2T6pUm8i9f8sHOg6ybjCEhAtJYtCZBkX4HSEtmPWorMiF1omgPLU_LhxzLjRS49jTn-IyzgUSO4jdpUMPkwlLFL-K5aMciORo_nJiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ZmOFoD1R3LDSI8XgN6isMTV8ACKj6YoiC57YyO1pTsV1xKylAkiChbvMSgxKCKfCiPqbjr5HAVoIuSuKUdpZywMcrifCASaSh-ffCxzj9U5YoSWtYF73m7j0PG_5bI1QdR45pi0SpPK5CKet6cDxPwI_Ja7byMJx4l43UCeiOr7klSfECIY-j7u0EvDHZmMjDZqUg2uVznzKALbUpimfYiV53akTsjCTKMQ4vgmxst4xya_D2T6pUm8i9f8sHOg6ybjCEhAtJYtCZBkX4HSEtmPWorMiF1omgPLU_LhxzLjRS49jTn-IyzgUSO4jdpUMPkwlLFL-K5aMciORo_nJiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=f-OKzE6bvW9EnXhN6oT0Wzf56_GNH6quIADD7GCE_XLEfei7p5NLJzw3wdnJRS0lSD7Ftd4QH6MirTAQ89rg7dzRQziA0q0LynFlACufczypX6MNxH5w01_w9oM9gPFEjU-dmSx9QGGV3kI0bppjNvmLXN1LlUpgkdiayxFU49QapruGX9i03DfmVu6PajZN4bhcSXbUEXZ0WJAxn__Z-ZEXIUHik8eyErjM5_goAf3Ol8nhUJBpPr_VtvD891zKPXaMutxWRKTiYhpLsstQx57uvmlFLYdl_O2z3AJ47f_oV4E8nBmmhQ8goNH0rh7aJu57GqUKxW40o4VjHHOSIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=f-OKzE6bvW9EnXhN6oT0Wzf56_GNH6quIADD7GCE_XLEfei7p5NLJzw3wdnJRS0lSD7Ftd4QH6MirTAQ89rg7dzRQziA0q0LynFlACufczypX6MNxH5w01_w9oM9gPFEjU-dmSx9QGGV3kI0bppjNvmLXN1LlUpgkdiayxFU49QapruGX9i03DfmVu6PajZN4bhcSXbUEXZ0WJAxn__Z-ZEXIUHik8eyErjM5_goAf3Ol8nhUJBpPr_VtvD891zKPXaMutxWRKTiYhpLsstQx57uvmlFLYdl_O2z3AJ47f_oV4E8nBmmhQ8goNH0rh7aJu57GqUKxW40o4VjHHOSIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jNdtpsRUQcbscnAUzz39pBr2Dfhha0PzS0PBW3q4Xeyz3Wlf12OmB9ePrb38iHYdRA0mHOOKHnky9Z3vLBf904_ZT_hrEndla1ThFmk5xLdA7_XpXoB76T5b-21MxQ94M6bsCrRZqgUNJzhCSkCFq79EG77CbHRU3vviMydYdCHBsLH7z1Pcgnu2S66jJtodFyaV71Nl2Nc05b4Q1vVCINWdDf2p4XJSiBJxJruKFCe2vyN6Ue7cHbX9A_CwZ4fizGat-c7CXUAut45zKus0ho-pftk6ZT_Fy4TQ3R9sMyGrm3mmu23SR3vv6Z9C-GMKfZtHWTnLjPcr1QLXPzI0dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jNdtpsRUQcbscnAUzz39pBr2Dfhha0PzS0PBW3q4Xeyz3Wlf12OmB9ePrb38iHYdRA0mHOOKHnky9Z3vLBf904_ZT_hrEndla1ThFmk5xLdA7_XpXoB76T5b-21MxQ94M6bsCrRZqgUNJzhCSkCFq79EG77CbHRU3vviMydYdCHBsLH7z1Pcgnu2S66jJtodFyaV71Nl2Nc05b4Q1vVCINWdDf2p4XJSiBJxJruKFCe2vyN6Ue7cHbX9A_CwZ4fizGat-c7CXUAut45zKus0ho-pftk6ZT_Fy4TQ3R9sMyGrm3mmu23SR3vv6Z9C-GMKfZtHWTnLjPcr1QLXPzI0dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7gbW_62riTV23udVGs2dO1IOKGDvmW6aYUpQo2qB_qYtjA_aFIiF066bW8E13QDPvIeTm9LulyOoJJaTjzrXV-hh457NzNXUmZmmaV5M9gbdpvN7A5Wael_QBwTsCyil9AzM-eW_jkjTQFJhwqMBw5rei4dfL1aq_AVH6KUJJ5-DLVbXjuukR6NNVmSfxPvwLKK_2lD0kMZPEpn_r7c86ocHYDQ0BX3JKqwDUusSxJ8GyX9-RrcCawa_54XrS8Yr9deAy6CvOMS2D7-mkaVkatPr9Z6IiTg9ur1ZP7wH5wmtR_wMtcmANnf9TlDXRzggFISJtgHAvmWjcC30BCQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qCXnxkCHynxlDLv5eW4PgiTrOhfI4K4J7CXREUvPRnITieJmFhdhX9AWabdORpjfJSKunDSICHTFwKN479utZT-aKN_6yKanJ38yufFy1B6_Jto_XTRomQ2dG6-qsn7Z5la_MDwmsAeTlvRPusHXTBa4FXngPX-xja2glvl7CWM5D8jLmNn9UrYIy8E7lmvpioE6yt2qdaRsUmFMR1ZRz-6CbgAZ6cD7c6ibH7wzbxyO0o9Yz3LHMRXYvkn4zRSfESacxQQO0U855pxWTNI70nhsZrZ7m0ykeZP7KaGGYqzn9BDA-Po0k3x8Tj_5qZ-BXxKtuzYBRas0Q76IXZIKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qCXnxkCHynxlDLv5eW4PgiTrOhfI4K4J7CXREUvPRnITieJmFhdhX9AWabdORpjfJSKunDSICHTFwKN479utZT-aKN_6yKanJ38yufFy1B6_Jto_XTRomQ2dG6-qsn7Z5la_MDwmsAeTlvRPusHXTBa4FXngPX-xja2glvl7CWM5D8jLmNn9UrYIy8E7lmvpioE6yt2qdaRsUmFMR1ZRz-6CbgAZ6cD7c6ibH7wzbxyO0o9Yz3LHMRXYvkn4zRSfESacxQQO0U855pxWTNI70nhsZrZ7m0ykeZP7KaGGYqzn9BDA-Po0k3x8Tj_5qZ-BXxKtuzYBRas0Q76IXZIKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=KdP1HLqqvz16LBEmBHlGxDt6LoMS8aWyw3qJkTOqb8EDE9gRqmm_U9lZgYjECNvN6dUoUO57DwEquY0OvIwSbJ368nL0BNVRZvf9n_HVi4sQijcsX1_zhrcDk37JMG3bhsjHRwuP6cd-6IYMgVbEh27C9qP4b-c2-D-8R0TRgC2-ZYbwg220GGP2puH7uhkGJ1aes2bV5fCt8lkk5WIyRU6bjIOcTDhNBr_JNRjs8iTAEkXEQApgepnLi8X_htaG01dlaMtWIWHMRvWWhOMRwng-mFwVf7XiKfMSvjjDjpXOF6Yb6iLSB4CgGlLb-wB7RoFkiVuwmlK4qjwTZXAk0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=KdP1HLqqvz16LBEmBHlGxDt6LoMS8aWyw3qJkTOqb8EDE9gRqmm_U9lZgYjECNvN6dUoUO57DwEquY0OvIwSbJ368nL0BNVRZvf9n_HVi4sQijcsX1_zhrcDk37JMG3bhsjHRwuP6cd-6IYMgVbEh27C9qP4b-c2-D-8R0TRgC2-ZYbwg220GGP2puH7uhkGJ1aes2bV5fCt8lkk5WIyRU6bjIOcTDhNBr_JNRjs8iTAEkXEQApgepnLi8X_htaG01dlaMtWIWHMRvWWhOMRwng-mFwVf7XiKfMSvjjDjpXOF6Yb6iLSB4CgGlLb-wB7RoFkiVuwmlK4qjwTZXAk0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oC6GYcnoIRWKoLSm-Co4CdfrqgUuXaq1wGjnWmq0wlolG6rMhd_eNDL-_ru47hBWarDdxmwD7CqWHZa68ZHD_C5jUuZoPyGDDjDCq6tbDgOgjF__CWajh_ZZBKcZvv06ehMW_18K9xLmA09AEE1p74O5zuk5-h84YE9yvNMSiswV_60BA9EPoLYBT0BPZfV-n4junQRAAX9aW-8JNyk_RLbNnPbXEwVF3vNsajSTayvgcmazvgogw3DO3XgQSkpP_cL8Bi2iuHSzLanwfl5g37vbRwk0qbae0p7HRE4XYjZEX9_5WWYTXezBJuEaK3-vByD26Ev4jDGpTD7uA4A5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oC6GYcnoIRWKoLSm-Co4CdfrqgUuXaq1wGjnWmq0wlolG6rMhd_eNDL-_ru47hBWarDdxmwD7CqWHZa68ZHD_C5jUuZoPyGDDjDCq6tbDgOgjF__CWajh_ZZBKcZvv06ehMW_18K9xLmA09AEE1p74O5zuk5-h84YE9yvNMSiswV_60BA9EPoLYBT0BPZfV-n4junQRAAX9aW-8JNyk_RLbNnPbXEwVF3vNsajSTayvgcmazvgogw3DO3XgQSkpP_cL8Bi2iuHSzLanwfl5g37vbRwk0qbae0p7HRE4XYjZEX9_5WWYTXezBJuEaK3-vByD26Ev4jDGpTD7uA4A5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=iOm0HkR0g3cgYL_PvVjX3oFdyJscb9-dO5_bPP0baa9fcvU5nEO_NcQbo3p2bfmmIN8BifQ5SdFjJTsMGWIaPqd12AYV3uOtDjmGpML4tbu54XD3bsViZtUOkwpWwSkb_r_UyLsMl5cM210yBn8Svr9iQENiSuoaBptFVbww7LFCkLcHXlWSVKhwba7z_8k5iA2jVs9V-q10QlwPi1mrYZk4Y2ZlirKak3aWzx8BPjKYZnq1G7F_KL684aceUgn_WqKvi6Ol_3e-hi60qwU1cxkV4pdfK1Rau-IL1uIWX2dvUHko6s5WlwiJ33Z9vh6j2zcrE98xtx4qN1HVWSnFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=iOm0HkR0g3cgYL_PvVjX3oFdyJscb9-dO5_bPP0baa9fcvU5nEO_NcQbo3p2bfmmIN8BifQ5SdFjJTsMGWIaPqd12AYV3uOtDjmGpML4tbu54XD3bsViZtUOkwpWwSkb_r_UyLsMl5cM210yBn8Svr9iQENiSuoaBptFVbww7LFCkLcHXlWSVKhwba7z_8k5iA2jVs9V-q10QlwPi1mrYZk4Y2ZlirKak3aWzx8BPjKYZnq1G7F_KL684aceUgn_WqKvi6Ol_3e-hi60qwU1cxkV4pdfK1Rau-IL1uIWX2dvUHko6s5WlwiJ33Z9vh6j2zcrE98xtx4qN1HVWSnFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4FEwP3a1-q_CFjNeHIskeSLI6zh69Rzm8x63xYljqhTqkPc52lRaC6ajmGwwC8rlP4AWnQBrI4rcibdJTmvI-mE9cICc-RalhsDbTR9cuaIVCVLhcORIpfHfCq6LHl-Jj7VByGHe180cFklGzYo8Ur-f0Vp2aWv8a6RRrNRWvmQ3oWqwIcaP46t43VYODsofStVOJkQYwtcPLRiKjufG_BdpZCl1zGw8k7hX2zMw4lZhbTRgJgXUE57zrLTcCtEsUp3v9dw5OVffVZTa0HqCK_tDGdPSwVJUd-6ekSfRF_T3IO5Mfa0Qup_mHgYMrdGdzSitPLlbTG7vAxPwKZUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=QA923YOj6OuavA7FuDAWfnkgdRMOkk9tUHM0p2R4hzWu4pQcPEkF94V18tWmMHMhYNszHqjhp0QRe1lwoHCc46A1rvkJoZVCzvAgZRvLZzZdBtyd5k4yjKRFft9P1ybQ8rkMMe8IAaej2xz6QkEyfHEj_fQGg_eWuuBQIiZBlVJTlBIorkRExZwHhyOmtMZwV-4WCcyQrs1i7sl4ekRj9i4sMsA9m6IQRYXGZDd_BTbpn7NY-paRyasCtMWR-P2Cqv3lIFN_rjKcIcasj5kx-hlqed6qfdJOyj6Q3FMCvsNh_iB5KhOVM1F7dmQxBFtVdhgCHjwlB4W0gzKSMmf2zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=QA923YOj6OuavA7FuDAWfnkgdRMOkk9tUHM0p2R4hzWu4pQcPEkF94V18tWmMHMhYNszHqjhp0QRe1lwoHCc46A1rvkJoZVCzvAgZRvLZzZdBtyd5k4yjKRFft9P1ybQ8rkMMe8IAaej2xz6QkEyfHEj_fQGg_eWuuBQIiZBlVJTlBIorkRExZwHhyOmtMZwV-4WCcyQrs1i7sl4ekRj9i4sMsA9m6IQRYXGZDd_BTbpn7NY-paRyasCtMWR-P2Cqv3lIFN_rjKcIcasj5kx-hlqed6qfdJOyj6Q3FMCvsNh_iB5KhOVM1F7dmQxBFtVdhgCHjwlB4W0gzKSMmf2zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hIX4XkPWFB5dJWKDmSZulRtn3h23jQGT7XHetKaLEOIv0mn3MkZs5-8K9qeNmB-pXbjxeaC6cbLJQy05TPQChkUugxMILsxATw7KgRAC0ORh2rKZ2kYNTsE3sfBorjTBpHMe7fOu8LmF8-bH0JYrTukHBr61GJAtqR4F6BQP1xL62oFK5awhj-iPedVeK3_235-ug2ObHLsqiDUONLMMdFjWxx1BY4HcuhwE1vJ2uCAZYSgtFXGOumlyxj0nq-aVzYvM9YWwIgXEYh6gcVR8g6I77SlXey4TJUHhDyrO7qZPnHF3RcWwKZ3MQvIJcVdaPZGR6B0FhBI8pQ98nKk3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hIX4XkPWFB5dJWKDmSZulRtn3h23jQGT7XHetKaLEOIv0mn3MkZs5-8K9qeNmB-pXbjxeaC6cbLJQy05TPQChkUugxMILsxATw7KgRAC0ORh2rKZ2kYNTsE3sfBorjTBpHMe7fOu8LmF8-bH0JYrTukHBr61GJAtqR4F6BQP1xL62oFK5awhj-iPedVeK3_235-ug2ObHLsqiDUONLMMdFjWxx1BY4HcuhwE1vJ2uCAZYSgtFXGOumlyxj0nq-aVzYvM9YWwIgXEYh6gcVR8g6I77SlXey4TJUHhDyrO7qZPnHF3RcWwKZ3MQvIJcVdaPZGR6B0FhBI8pQ98nKk3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gh8Tm6_FuXZJleFFyl0Tmf2Aq5g83Uqjaii8dtwR8MF5fhmYeAPN94aKoHFJwTAiu0g3A-Z6obFz2SlNOKLenGLwptmnQLJ_0O3hSRJst5uVFep4qeMuZWsn7Qd3x7yEQ3YTmGq1IT7cn2gEGMnBlevULfS4R63SJBOqzqy92Z2EI3LyV81jrxfeRu0g3N--9lUwq26vtqY8C_Z2X2EgM2erue5qHZgzI76zzYdRAGD1LZsxqecagHaOdrMo15Nocv9oQ3gCabhP9CXuSY8pcU5iMs2_Kc0Z84Wzlk7Uk4pHg5AKSTjA7U7asc3prWjZrSKqjWskMsDlr0KgeYzWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Smb-eWIVJ19pCHXPrlJKOQfUxQ3KNTl8I7Z0rh1XuIBYsamqLFzTopbslWgGs7FZS-P6GiK4Pl2ASE__kQ-Jzul4fC-rxRx7cnFvY7myOudAjt-AF3Ld2sGXxI6THmf-5C-gUgoGBdU5FZamA95iomzOpZXs8LrFomvK-ge2Sc3DaiqwAPN_RbziMNrykn7xlGnTwGI1IFpGRE9VnDAA3X5908XpZZCoQGCd-fYG9dBmo5fODWZveRm59vxBSL1bWLpKdqcTCORRaBLqf7uq36B50tKfsGDKhR6SUZLUJt_zdk9R12j6ox24YX6I3ccnzzY33GP5JOa3SJgF5MoYQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=eu7BQMFulC1WiNVSNtO3DqOZedp-AcNolGQ1HDZo6F3E5I7yUITgNL4f9BHiOqznM0tt4uLQAuBiTLJK12Rd-muPK4tK1hN6XmVZn10Uz5ekYTb378jDRztOVwF1_oGLwKFI1s2mdo9BMyPBE0zpPTM4REWX1h7Bt1DAmUcncVOpOC4zjBDjOPwAPtpqT7EQwk9NQIuh1FpFd4yBZyx1DWKU4HMF1O38qeGUooR91dyl_mUZjmeZ2By8xR6PcYvqNP-vIGKEs3pvQoy1aywrgXfX9va1iI1hpsx3L2f7vpQeJiCIZeawi8tcjfl79364yxROefD49YTY_rYiOFvXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=eu7BQMFulC1WiNVSNtO3DqOZedp-AcNolGQ1HDZo6F3E5I7yUITgNL4f9BHiOqznM0tt4uLQAuBiTLJK12Rd-muPK4tK1hN6XmVZn10Uz5ekYTb378jDRztOVwF1_oGLwKFI1s2mdo9BMyPBE0zpPTM4REWX1h7Bt1DAmUcncVOpOC4zjBDjOPwAPtpqT7EQwk9NQIuh1FpFd4yBZyx1DWKU4HMF1O38qeGUooR91dyl_mUZjmeZ2By8xR6PcYvqNP-vIGKEs3pvQoy1aywrgXfX9va1iI1hpsx3L2f7vpQeJiCIZeawi8tcjfl79364yxROefD49YTY_rYiOFvXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cncasru1vT9f8OUE4869WBh8Be4Rmkau5hTt_QMPJcB6eCHcrZgECfGVRe0DOvjdulRlpX5d051uKZcxFKFg-fLzI128osLL-tsna2aoGdoW-f9_QmzOUqwCtEPmUFeQI_wI-Xh9YfqPv1eMUZXvkbci9kc8JHHinv4mK1gcRzYyzmxlmnnqj49EONI0yMz9t9Kr9nutg5dts49o8PD59tisboxNZ9vu9gWWwByIDmwfeZSCZ5xsiJcVUd4E3-d2m13lWPpOL8qMWjBB7P9RiHkM-ksBaUpbEXgGumDYyTbDOjMOW1ElQ2J9II2xcALi7OE91fhcleUEC7iP1mLuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
