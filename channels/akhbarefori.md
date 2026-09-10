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
<img src="https://cdn4.telesco.pe/file/rJD7z0XlXXPABfUIVAiVPexi7Z--2yuzZYrKNh38r-mG_YcikvbgKYYS8hS3ESp0CM5Q3ZVLRmV3iWCKI1lxt1NhKUx_cGQq8QuGOJhmk78eh8QAblExvpFPI2OTBQEmFrpr4dpLrNjbd9w3wbdLfFNTQMcudRPwyZaCH9MyzEdHxNeBVst6cYNbaK27U53zEqy2wI41YWsc4zvhMT-eaXvNUlaPJqCIUNNZ1kwG2U8vtteuyzflKyRoiQ6DUOEnv_apjThdvm-orvoCQgVMn9JxS2P3L-DY5gWJS6yuZ8j0ULyQjBZk3MYrkRuJWvsC9KjAdX1-XnjEArMvjfxsTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-688727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd29b2165.mp4?token=SeS96P-VQcorTkacrWKTlzsGRXbGmFEJWGtXKIjP34DrJ9i2ZnYc3I49Gz1RIi0alMTLqQ0LRajEYP80A36AdzJbjVpy4M_Ti-KUWPO1U53N-sjDcL8cYjq4mxF2wIQOCyQUFT2smRM9ZPBoA35iR3H-ew8EIM7qbjFDYcpk7JhZhuTkgBUWQlyN-Csd_Y_9ef9gUjB7z5z49DN_K8lTK_KFuhri5AiS99-j1h4TYMtKOSK8oJK3srDplMD1_5TQE50NTC1WC4LlGCYFoRB08Fqo78SKOrTK3YbBiAabPXGjvkKoMpJCqPmNB_c-V5bOqRUWb6DeC97H60iOvXoRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd29b2165.mp4?token=SeS96P-VQcorTkacrWKTlzsGRXbGmFEJWGtXKIjP34DrJ9i2ZnYc3I49Gz1RIi0alMTLqQ0LRajEYP80A36AdzJbjVpy4M_Ti-KUWPO1U53N-sjDcL8cYjq4mxF2wIQOCyQUFT2smRM9ZPBoA35iR3H-ew8EIM7qbjFDYcpk7JhZhuTkgBUWQlyN-Csd_Y_9ef9gUjB7z5z49DN_K8lTK_KFuhri5AiS99-j1h4TYMtKOSK8oJK3srDplMD1_5TQE50NTC1WC4LlGCYFoRB08Fqo78SKOrTK3YbBiAabPXGjvkKoMpJCqPmNB_c-V5bOqRUWb6DeC97H60iOvXoRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مطمئنم نمی‌دونستی هر رنگ درب بطری آب، معنی متفاوتی داره  #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/688727" target="_blank">📅 15:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e0d0778d.mp4?token=SjZhhVU4PXgqRtn49BUCeDaq0tO61MCGLVNTVLP46MvIdoW2he1Zxe61d93LtO2r2BC4Eb1F5Jc1c_Py44LAKRRTEcoGPlac8MwHp9_oh9EnRezdwrbWLa6E-EMhKEmEyqylgdUsg5KDvklap7ZvQj4PJnK7GpGiMNSbGTz2v1tNVv0tUHee1IRm_LB3kRYRr9eJsU3ptnLqWb4nr4GjOvf9Drg7HXT82b_hcAqDkshHFeNZbb79vV8nsA2L2-9w54O35TBSZG6pcQKfeDZzNI09_ydQRAOm8k_LGknaqgHW-n6f_P4HgidIS1mdKiDIqxzu65WdB-OjMIZzR7365g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e0d0778d.mp4?token=SjZhhVU4PXgqRtn49BUCeDaq0tO61MCGLVNTVLP46MvIdoW2he1Zxe61d93LtO2r2BC4Eb1F5Jc1c_Py44LAKRRTEcoGPlac8MwHp9_oh9EnRezdwrbWLa6E-EMhKEmEyqylgdUsg5KDvklap7ZvQj4PJnK7GpGiMNSbGTz2v1tNVv0tUHee1IRm_LB3kRYRr9eJsU3ptnLqWb4nr4GjOvf9Drg7HXT82b_hcAqDkshHFeNZbb79vV8nsA2L2-9w54O35TBSZG6pcQKfeDZzNI09_ydQRAOm8k_LGknaqgHW-n6f_P4HgidIS1mdKiDIqxzu65WdB-OjMIZzR7365g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای لغو عملیات ویژۀ آمریکا، در نتیجۀ حملات ایران به پایگاه مهمش در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/688726" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7EyKpn1VV3YHyHbP2bNH04_-Y3RpPIs-Xm3D1f6lBD8zU3CUirCo3-5TGtLuwNSwNmWmKj4huftWHZ66DL-DycGLj7ULO3mg9kdA6bIxC4ZSyW2MeuCgUBVP0nZ6UYK0DYLUWIrQHURdW7i6xPvRmqyROSUq_B8qPOl3vwU_PAmo4HjViefVCM9Dm7aZ-u6JcwDclTT_QE2OVoAik-aim_3lUNH00mYlqWX_NOxRQM4nG6u3MabZdZFXMO_pNJ5Ez7rJ2o7CYobhUoX1Z2Pq_kxbE_p0xy6eOCmRgIrCgCZxKLCJkBsEWpyK3Rg5R0UbXOJH4PuBCP1MF1-Ahz6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/688725" target="_blank">📅 14:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
جزیره زقر بدست انصارالله یمن فتح شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/688724" target="_blank">📅 14:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=HTI2Y-2qsSUPXjIk3EuGxfIU9lDhXlmH5ABuipIoDwMXNgxinaAXAG1Sn4q39ay_hU57UeNptM7_KhbbIAwCnD83UXV18B-GchwF5j5lxlLcVPixXnNq3TJExdBejLiq3LSpTJrCW4n24Qi52ar1dq8IEdEuUpGOL0SE1scUiZ5tn6uKliEgsfwt3CEinIhbE3kfHMqzo5LHcDxbtAiVw1rdB5DXpmA3JPtBZt2j_VyKOsgWgVtVBixR03MP8w0XN_bFhuc8ZlTbu_RanYmb7xwbHuObwA8-HzT7PZiJou_iWgHC3HNPlnz3puOjek2mR9k3ZJwXVTFh8vGr8ERTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=HTI2Y-2qsSUPXjIk3EuGxfIU9lDhXlmH5ABuipIoDwMXNgxinaAXAG1Sn4q39ay_hU57UeNptM7_KhbbIAwCnD83UXV18B-GchwF5j5lxlLcVPixXnNq3TJExdBejLiq3LSpTJrCW4n24Qi52ar1dq8IEdEuUpGOL0SE1scUiZ5tn6uKliEgsfwt3CEinIhbE3kfHMqzo5LHcDxbtAiVw1rdB5DXpmA3JPtBZt2j_VyKOsgWgVtVBixR03MP8w0XN_bFhuc8ZlTbu_RanYmb7xwbHuObwA8-HzT7PZiJou_iWgHC3HNPlnz3puOjek2mR9k3ZJwXVTFh8vGr8ERTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثۀ مرگبار برای کشتی خارجی در چین
خبرگزاری شینهوا:
🔹
یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/688723" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
جزییات تازه از موشک جدید ایران که برای حمله به ناوهای جنگی آمریکا مورد استفاده قرار گرفت
نیویورک‌پست به‌نقل از روزنامه تلگراف:
🔹
ایران برای نخستین‌بار در حمله به ناوهای آمریکا از موشک‌های مجهز به جست‌وجوگر الکترواپتیکی استفاده کرده است؛ موشک‌هایی که با دوربین و حسگر نوری هدف را ردیابی می‌کنند. سنتکام حملات را تأیید، اما اصابت به ناوهای آمریکایی را رد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/688722" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
الجزایر روابط با امارات را قطع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/688721" target="_blank">📅 14:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsSJgtZsH2aygpdswbUWtuITIz_8PKKC9-1HFr6zB3we6kVYdYFt99vR3wl8E_-4lRzSH64qEYY5DC5MlFJPVFgrqBcFwc3ANIyg24aZ1ULTnmJdmpvpxYRe-t881Q_vT0mPabSoaIB7C7iJreIpOw4yUnZoVriYLFVoktY4DEI-IDkBYL9btt8pElNLHmQAfHNRiCU1XS70grfTxHU8Up1hJevZLN8AS8sMb7B9CsU2VQOQz3rb1PmgXxWpmYqMZ6cyJnC8yZ9VdxmYZc-ZNJPtV3jzXox0BOldOTNDl4Csta0oiOKsrfYpc24n2393nHUkptV96LgjGrEfgVypIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال، بلوف ترامپ را رسوا کرد: «کاخ سفید نگران مقاومت ایران و طولانی شدن جنگ است»
ترامپ روان‌پریش، ساعاتی پیش گفته‌بود:
🔹
«فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688720" target="_blank">📅 14:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45cc121a87.mp4?token=rIpZVNsGP9Cc-t0rXSa8vrNeouVuQ3HyvHcqsLZnx3N4hzA0cdjpofezky74PTqxj7gQTrGYWOe1M-pf9p8PwcaBEpk7WwY-XNYeVu9Z1K1PvR8ba0ixtqJb01zpZy-7giB4iYIPhL-n_3oxZ0dYmiduChwI_8yhJD5v7lh3e_65wswbHJodZ-WqR2vAXiqabWit5ltdbX4G9nw8gndfG9Wvylwvjvyek9b3fo7Qjy4UwMLibfOSpe_qg_R_7QOhvyly4NyfU3CZGsBDr7iOATCKDHGl18Ai4lMeqeJopXuTMKVyqvGnl0j9QZeIgLaseqKpXvvb1dAhW-27_k4hTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45cc121a87.mp4?token=rIpZVNsGP9Cc-t0rXSa8vrNeouVuQ3HyvHcqsLZnx3N4hzA0cdjpofezky74PTqxj7gQTrGYWOe1M-pf9p8PwcaBEpk7WwY-XNYeVu9Z1K1PvR8ba0ixtqJb01zpZy-7giB4iYIPhL-n_3oxZ0dYmiduChwI_8yhJD5v7lh3e_65wswbHJodZ-WqR2vAXiqabWit5ltdbX4G9nw8gndfG9Wvylwvjvyek9b3fo7Qjy4UwMLibfOSpe_qg_R_7QOhvyly4NyfU3CZGsBDr7iOATCKDHGl18Ai4lMeqeJopXuTMKVyqvGnl0j9QZeIgLaseqKpXvvb1dAhW-27_k4hTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر انسان‌ها به‌جای زمین، روی سیاره‌ای دیگر زندگی می‌کردند، بدنشان چه شکلی می‌شد؟
🪐
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/688719" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فرمانده‌‌ای که با فراموشی جنگید...
🔹
همزمان با نزدیک شدن به آغاز اکران فیلم سینمایی جانشین آنونس رسمی این اثر به کارگردانی مهدی شامحمدی و تهیه‌کنندگی روح‌الله سهرابی منتشر شد.
🔹
آرمان درویش، شکیب شجره، پیام احمدی نیا، هاشمی، سارا توکلی، هادی شیخ الاسلامی، پیمان نوری ، میلاد رفاقتی ، حسین اثباتی، محمد صدیقی مهر، حسین اسماعیلی، عرفان آصفی ، رضا نوری و با حضور امیر آقایی از بازیگران این اثر هستند.
🔹
«جانشین» محصول بنیاد فرهنگی روایت فتح و تهیه‌شده در انجمن سینمای انقلاب و دفاع مقدس است و با پخش بهمن سبز روی پرده می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/688718" target="_blank">📅 14:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dATsLi6FJY7R0_8g5RHaQn8CWZdkUPk8J9Q1870Rq4TFmuMP14ax6qyrclyZ4pEnzhCXYhime2Tqr4flCejKPf5NDENxPKeI8T-JJMuLiLJ7RYr99Qrd_8NVGKcFYrF3UvH5YGuUDQqhAOCBmraRaWjDfzENmZnJPN30z_9tAnuKFcK0gb-RRouPG3UHG7Tj3QcvsV0EDNLk6giamwykBo46UHsU9zYq0RSGD7CBty02jo5FlbCevuwR6TuNfJDsgNnV2Zv4FcUX9iiXG9MCLZA7DvI_T0z1Ef1h8uCb0MOh_r2geqOEgVmSMv7QSLTeAESpYMn2MkDDABXxw0QYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688717" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68e197b46.mp4?token=g64OW-IsLL5rg88r_z0Ks_ec0uhbqWoKX7-pjSz9YXN3pkA5lwD8dj2pvUNU0_h_OC1-vWNtVVX_THlrTHXH8giufGE5HS0bLqi7c3gm_M0cAgLfAfx3LxU4hz-M8mYXVXp6wpTh3tClLe4HO6A-7DIefysFAOkfqeDBOOpvV3xraAjwcs8TePDCJOl0i9B-3U8sVcxHcwy4wFIGlsUdidiGstl0E1RMa-Ia3dP190QW36SDDYCqhjJmQgUifIZmvlbUdWu3mZmpvht1ahgQMUOF5t-i7CnNd68nHfJ6NWkW6x3S6lVRyVxoBDJ5lO89U4C6GUFonWPbstgTR9Kddw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68e197b46.mp4?token=g64OW-IsLL5rg88r_z0Ks_ec0uhbqWoKX7-pjSz9YXN3pkA5lwD8dj2pvUNU0_h_OC1-vWNtVVX_THlrTHXH8giufGE5HS0bLqi7c3gm_M0cAgLfAfx3LxU4hz-M8mYXVXp6wpTh3tClLe4HO6A-7DIefysFAOkfqeDBOOpvV3xraAjwcs8TePDCJOl0i9B-3U8sVcxHcwy4wFIGlsUdidiGstl0E1RMa-Ia3dP190QW36SDDYCqhjJmQgUifIZmvlbUdWu3mZmpvht1ahgQMUOF5t-i7CnNd68nHfJ6NWkW6x3S6lVRyVxoBDJ5lO89U4C6GUFonWPbstgTR9Kddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشرشده از ورود نیروهای انصار الله یمن به بندر راهبردی المخا، در استان تعز و مشرف به تنگه باب المندب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/688715" target="_blank">📅 14:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688712">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vg8Vbo2RRrYlTEyNEWJYvzer2yUh28nQlKwT8Wq77Wg77w3R7JX1AnfbhP4arrQ082Uq7avgC_rkyacp-7ZZCp2RDD_T6yV0GH5jGIkgBNJNi8Al-QEtpMTrkzpFm7CfBX9_sKQn1Y7bFq-TgfEjBWWF_DBQsm_UtkCbEWUfo3tnKVxeOlvRvptd-dZCgotSowIL8b6L_jn5682MA4z3LetUPcEoDZNtA9Y9jPZQqpIEBl9TSa1DpWwcW9Yc3HRTzWqR70Dzi8ZwiNZt8AzpZsCDoP8S12slbvM4FeI4f9gTQXDD_2z7wZ_vSZi9J9vqppCyZa_accLMQyUHMrrQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyaOyLkdy6xoJif-XQkzw39Iz8dO0DmvvHBdu2-LrmhekkrQ7h9MvTOUfxlzWfX58sGyFCsANVPnWrdWB9P82dhvYth-42y0A-hkLPbVZha2eDWOY04kA0kzjh54o8Kco2m4qrICnLE2AhqNbPPx9RpwfDMLQqdfRvTfxhTsMZVeH-ZqgSDxJSpNmkWyZWOouG_Z-NHQhv3-7bnFzGAEUULT7AgKj0m4NzRphdowHXmzMmdlShuHIvxepF35IA3ySLF5kqcYT1xnRmkFd5wFmd_7mKVZH_aPzEl6ZGvzYyBdHWXwkCq7g_H8gRg2PF1xYOjjyFinGvJeD268qXTW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDX3ROJERHxeRTUahkhd7WKow8eG-J5lhCFmg4bhO86Mch9Se23-_uRPZU-UUTeCDcpB_hcqiu9d75aCMtUd0ropf2PneN8LmpvmTwwnZ9CoS8PADYH6P2MQVx6kJCLNuYP0kHQdTAv7_SEpgMS_52IQS6hlIHexKyWlE6_E8_irAjto4gaqrUmfNmSfteIdEai_7ztkMCc41m46itdeln_YKn5Z3LL5b_jHPN_c3kNd3rNSBhPKFjlQ74OQRQ1NC9_rYDts2cm1xSf5yOHCXXnWpDR7FFG98OoDw156o_OYOBE3IYtSfy8Bdid4gLfpsMXK6I6DuZclOO1fyUTQeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هزینه های میلیاردی آبدارخانه شرکت های بورس
🔹
در حالی که چند روز پیش هزینه ۱۱.۵ میلیارد تومانی آبدارخانه بورس انرژی خبرساز شد، بررسی ها نشان می دهد شرکت بورس کالا با هزینه ۹۸ میلیارد تومان رکورددار هزینه آبدارخانه برای یک سال است.
🔹
بورس تهران با هزینه ۷۸ میلیاردی و فرابورس با ۱۷ میلیارد تومان در رتبه های بعدی هستند./ تیترتجات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688712" target="_blank">📅 14:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688711">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پزشکیان: ممکن است در برخی جا‌ها با کاهش سوخت‌رسانی مواجه شویم، لذا باید سوخت و تجهیزات گرمایشی جایگزین به آن مناطق برسند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/688711" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688710">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c562b5ca.mp4?token=bEvsrBk-CaLeDqGabCCM4o36bJz39cKw0DBBaam1NEUfL3_xBwdpsMo6GYtlxK-W2SnfpGAI6F6VVtYuou3Fa8FcPhT7VulvPoq2fxIOMvK6k5qCQ25bimSth8f9n5fXuPpPF1GPagnhi_VemxZzQ1vEJoLHrUC82w2z7r1cHdmgvKAk-UAAx5foS6_5acB_kGpSiU-7tXDb8AOyBDZd8PzNKmxD-LR9oqw8DGloVmhU9shUzx2dpRFAwwRHsU4_vxC70cS1jtR_nEBT5T4r6TFDTOTDlv2WhpQDc-ap8Bfo80luqxZC0BbJfgOtGNLZxOdymbN7wYB3D-hXqHDGGq-XMBcPHVqJrf4yFWFEjhk8LwM1c-ANlspja8TWha9TOtokcwNsQMEOnmvt4lfCCfL-m2-Lei-nW_aKe3ec2kHPC7Er4uyZmBh34AnZ9Q1uSFcJcTmNBH_kOYYiHi4SG-K7ZYGZnFqIueNP-Yiyse4n15XI7NATXqDL8nOK7YUns1GdHIoRmtCqpVtM62tCh8EsarLvupz7z1o6QW5d6UGkVxGyGki5dbwReYNtDn82tkoEXYrCRRAfIpboALu_wn9ALFWdLaB8WtZHp1BOhW5SMD5NzY7ncoAORtoScQbM4o7aol9AxdHtQQgREr4ovMb8i1Rbn7g5lSPnptAa_QU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c562b5ca.mp4?token=bEvsrBk-CaLeDqGabCCM4o36bJz39cKw0DBBaam1NEUfL3_xBwdpsMo6GYtlxK-W2SnfpGAI6F6VVtYuou3Fa8FcPhT7VulvPoq2fxIOMvK6k5qCQ25bimSth8f9n5fXuPpPF1GPagnhi_VemxZzQ1vEJoLHrUC82w2z7r1cHdmgvKAk-UAAx5foS6_5acB_kGpSiU-7tXDb8AOyBDZd8PzNKmxD-LR9oqw8DGloVmhU9shUzx2dpRFAwwRHsU4_vxC70cS1jtR_nEBT5T4r6TFDTOTDlv2WhpQDc-ap8Bfo80luqxZC0BbJfgOtGNLZxOdymbN7wYB3D-hXqHDGGq-XMBcPHVqJrf4yFWFEjhk8LwM1c-ANlspja8TWha9TOtokcwNsQMEOnmvt4lfCCfL-m2-Lei-nW_aKe3ec2kHPC7Er4uyZmBh34AnZ9Q1uSFcJcTmNBH_kOYYiHi4SG-K7ZYGZnFqIueNP-Yiyse4n15XI7NATXqDL8nOK7YUns1GdHIoRmtCqpVtM62tCh8EsarLvupz7z1o6QW5d6UGkVxGyGki5dbwReYNtDn82tkoEXYrCRRAfIpboALu_wn9ALFWdLaB8WtZHp1BOhW5SMD5NzY7ncoAORtoScQbM4o7aol9AxdHtQQgREr4ovMb8i1Rbn7g5lSPnptAa_QU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با گلدوزی می‌تونی خیلی راحت لباسای لکه‌دارت رو کاور کنی
🪷
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688710" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvZXf7HxPNKjV_1tSt37ESEZJE6pMhUJmVhSFH59riGjahwkQ-L2gs6x7q2d4xtzfxRWxHp2e91jJKtYkZOTiiz5RjU3ybNmOd5HFq5ZG9rRlnRwyWt7sUljfacv9BFw0MbqQbo0msF2dB4dQH1zLJ5GK7iOgYda9BqmqFeUiieGlEf_GUNHtn3tz5xp8pXuCmOtSKtK4Bisd5hR4wr-SJxjVc940cFNAkjH9gMu0li9pCdMx62ss3QmViQ_Io5T2n8PWm1eV6LfvSkVzYiGi-gimdyQ7-xJR_x_CwhB7Hl1pcpoYU0OBuRqaY88mB2tpVM2B2Sp4rCNlN8EAPPRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/688709" target="_blank">📅 14:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db4c9cdf7.mp4?token=lwIO8N7waEfOP0rveSvzUlChQXOzziftSjCd68BXyimRIEYE2myymZ1_xYda98SfkfCsGlDSSBqMBh7oYXkPYkIGt-BdbkkToeVsdF70JGwuC96Xh-aqhAgnIcH5ZXlRWNMs7gTc1Ip2gUvLkL0eIn7VxOdLVhJnqwzR231nQRjEZWsYZbExY50p771dkyy4o0Ci4The2D0vwsxvZBcPQ8IdrApNW0XM4evMDefLkLOBtefr4leXckR8tdjk1tQj8bgIFcJ6JnpbupkwHI2rpoozqwUeOcmxkgrFq5ZLJg4MOv94zqnZzNPk6hF_o8tfi1rqRux90Fpj2aKJ5LeePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db4c9cdf7.mp4?token=lwIO8N7waEfOP0rveSvzUlChQXOzziftSjCd68BXyimRIEYE2myymZ1_xYda98SfkfCsGlDSSBqMBh7oYXkPYkIGt-BdbkkToeVsdF70JGwuC96Xh-aqhAgnIcH5ZXlRWNMs7gTc1Ip2gUvLkL0eIn7VxOdLVhJnqwzR231nQRjEZWsYZbExY50p771dkyy4o0Ci4The2D0vwsxvZBcPQ8IdrApNW0XM4evMDefLkLOBtefr4leXckR8tdjk1tQj8bgIFcJ6JnpbupkwHI2rpoozqwUeOcmxkgrFq5ZLJg4MOv94zqnZzNPk6hF_o8tfi1rqRux90Fpj2aKJ5LeePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خرید رادار پدافندی انگلیسی توسط حسن روحانی
علیزاده طباطبایی، عضو شورای‌مرکزی حزب کارگزاران:
🔹
این قرارداد را میرحسین موسوی لغو کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/688708" target="_blank">📅 13:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وزارت‌دفاع روسیه از تصرف شهرک زاروبینکا در منطقه خارکف خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/688707" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترس اسرائیل از پاسخ ایران؛ کاتز دوباره تهدید کرد
یسرائیل کاتز:
🔹
هرگونه حمله علیه اسرائیل، صرف‌نظر از دلیل و محل آن، با یک واکنش قوی مواجه خواهد شد که خسارات جدی به ایران وارد خواهد کرد، خساراتی که ایران تا به حال آن را تجربه نکرده است، از جمله حملات به تاسیسات انرژی حیاتی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/688706" target="_blank">📅 13:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yrp9uyydgAxqXlSKaeBlhNXpOl6AZde8RDCVkiBVC9SO3ovDGJRNTw-bHOXAzmC2MVZd8GcV7rldLQEafeFqy-I__kUM4pYVkx_nm0B4kBPYyTUcDUqjtC5FtinAEp7f2uyZx38u-lXv29GfX402pl5VctXNSg8OUnNDC5IRdfJ1E--KOjcwwKbYaMpkdkDl_i563pQXWp7vy92UL88HLGsVH1w11iGsdFX7VMEOL7_Vz-rV9De7chpfgiKbxtXuu7pZRnsSsCbvLkValAa3YDO4C9FYZxVp-t-ofN2uPOs8IEIr83vJt4oaH79QAjVEVT6ju3UcYn7xt2zZnOMIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزیره زقر بدست انصارالله یمن فتح شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/688705" target="_blank">📅 13:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7ff24cc3.mp4?token=ZfM1RYDLMPu3db1k_MbGZg5EHfrccQs8NhRT82Q7tLqzTSNsDZ6uBoNPAAGDGzBoUjLrh20G_0g7JS0wOfq_vPbJepNCNUuXMG011XshcqUPpsdmqxHxVnpYr7Ai2M8utOFw4Mx7cYfxXJ1pWiVyLXVcBiMAmmjxuwkpomanfPktgH5WSUm705PRDcT4BcWUdgBp8L-symBF9KPI3Mr3RloPEvl-kf-85tAmIXLT8TlziK9RwogUGa2p_O0s2Iq3I3VV5d2Zppsoop3yY2yukAZm0ktCfphlLkwDc1-cHm3MdZTOD5VGxKw35oY54kQcDC1HGMR_nEQ_P91YZuspcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7ff24cc3.mp4?token=ZfM1RYDLMPu3db1k_MbGZg5EHfrccQs8NhRT82Q7tLqzTSNsDZ6uBoNPAAGDGzBoUjLrh20G_0g7JS0wOfq_vPbJepNCNUuXMG011XshcqUPpsdmqxHxVnpYr7Ai2M8utOFw4Mx7cYfxXJ1pWiVyLXVcBiMAmmjxuwkpomanfPktgH5WSUm705PRDcT4BcWUdgBp8L-symBF9KPI3Mr3RloPEvl-kf-85tAmIXLT8TlziK9RwogUGa2p_O0s2Iq3I3VV5d2Zppsoop3yY2yukAZm0ktCfphlLkwDc1-cHm3MdZTOD5VGxKw35oY54kQcDC1HGMR_nEQ_P91YZuspcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریما رامین‌فر و پسرش روی فرش قرمز جشنواره فیلم ونیز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/688704" target="_blank">📅 13:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGgYxjTDqLsxQn9nyl_Js_5vJzCorjBFVSWFC3_CQA_oHwAc3qY-3aEOxsAJqVo9pd9pvuJjIKGSBmXfIJHduB0N7mf6flLEgunuUgSDymwSp-5BXw3er3RKk6y67AMwP-XICFameurvgLEGZPBqeInndzrZy-g-EXuSfvY11_Pdhq71-tOWK1rkVY8Z0gB1tQ5lySd1IGuOtmbaKW1bt0IfKqCYESV5HRN0V_r-EO07MDLV5-vweualOWpNunekk8McynQW0-479dZCjbMoowAp60vMsl0vLlEIt7RHIMmX98KrGB9C46pOahLHlq6QtjHJfLex6YnFx5Uk9pynFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۱۰۲ دلار برای هر بشکه افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/688703" target="_blank">📅 13:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ارتش لبنان: نیروهای اشغالگر اسرائیلی به توافق چارچوب پایبند نبوده‌اند و از زمان امضای آن تقریبا ۷۷۰۰ بار این توافق را نقض کرده‌اند و همزمان حملات، تخریب‌ها و بمب‌گذاری‌ها ادامه داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/688702" target="_blank">📅 13:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkpQ1qtW_BnyBLiOU9jdtJoPxtcPfOywjfvCh1lbsXsvsf00s_QfCzhIDaeLSNnIL01oWmykzebLeUOHmoKe6hX687mCryXkofdEB3f5pZAlhb-OyDVZhSqdKAlZUG74-dd6h6sF77MgH2tbHGv4igHztbaRhn-nXqKkQX9Batc-YX1KhyrxLo2a7MuzV5w-eFYLcROrxNrpW4mhWFMgRRJ3qlsr1oFMKko1lhsHyiGqMvgJIF6c1MbDnq4XrorqhBMIK10mI4AyFJ68aVAaj5BhKCFrtXcxXfnG7eARk2bQEoWIM0MK9u2uHPdWdI-GvXqv8KdAvsrZD5boUybi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان سابق‌فدرال در واکنش به خسارات وارد شده به پایگاه‌های آمریکا در منطقه:
ترامپ و هگست شش‌ماه است به ما می‌گویند که ارتش ایران کاملاً نابود شده و همه نیروهایش در غارها پنهان شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/688701" target="_blank">📅 13:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
به گزارش رسانه‌‌های نروژ، نخست‌ وزیر نروژ فاش کرد که هواپیمای حامل زلنسکی، رئیس‌‌جمهور اوکراین، هنگام خروج از مولداوی به مقصد اسلو، پایتخت نروژ، تقریباً مورد اصابت یک موشک قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/688700" target="_blank">📅 13:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688699">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d845f0b3.mp4?token=pVrNQm1XTX8CyWqfeo5KbFyPH61mlI9Ouq5UlyB16TpsfDY8e48Iedb3OMfn5nRZIbyyZZLqasnIjHwazdVXsMB5vYv94WpQSWroHplyismkLn_ACB3G3TFYQTIYht-EFLYeO6k9SIC4SRiCF473bX8yoTpAOCALnOl98Gzw__GJMhpPWFlN3cbvkjyYRKoNKpNSgP7H8HsvYPOwl8xXUQIWOv2k2lT4_s7QMBPowDc_FaqLLzCUELGyVAY_ci3cFerTf6QXcMmHDNAfitVspBWFrKx_vPrUlLYtter4BzBp77YX6PH9_4h_jRtwKOV1FhmRrRfQPCPULkyhCCYc3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d845f0b3.mp4?token=pVrNQm1XTX8CyWqfeo5KbFyPH61mlI9Ouq5UlyB16TpsfDY8e48Iedb3OMfn5nRZIbyyZZLqasnIjHwazdVXsMB5vYv94WpQSWroHplyismkLn_ACB3G3TFYQTIYht-EFLYeO6k9SIC4SRiCF473bX8yoTpAOCALnOl98Gzw__GJMhpPWFlN3cbvkjyYRKoNKpNSgP7H8HsvYPOwl8xXUQIWOv2k2lT4_s7QMBPowDc_FaqLLzCUELGyVAY_ci3cFerTf6QXcMmHDNAfitVspBWFrKx_vPrUlLYtter4BzBp77YX6PH9_4h_jRtwKOV1FhmRrRfQPCPULkyhCCYc3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی نیروهای انصارالله پس از پیروزی در شهر حیس در جبهه الحدیده
🔹
نیروهای مسلح یمن در ادامه پیشروی‌های خود در جبهه ساحل غربی، موفق شدند کنترل کامل سواحل شهر راهبردی «المخا» را به دست بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/688699" target="_blank">📅 13:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUr7BmjCSJKgQhM_lIN7XxTK3fPxI37WzI0VWlcnfHU5xfuW30uzuwpAgio_EtGZUcogerhW_Mar5EwMif-a9m8tI3JtGEojtPO4CgM8evbOxxJlI3kYK_y8FVdxWUR0tdVpBTSgAR-VGNyKYhpMUTPInCHpKgVqgMSqvu5F1cKxX8E_wzzOkz0cDT1j139IiVMZqz0y7YygUP3gYE0JMS4ZLj3wfmRU6WfooKioPGSCoC15i6C1uoNrTt0iiXGCoyk_hgW4-grt5SJkbR3sDyo0Q7o_KXZD3deHqzcYmeLgDGY-4DqdNMXv-fILD6sHcrhSqQH9KmqPt8L0IVXZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۹ شهریور ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
بازار طلا و سکه امروز پنجشنبه ۱۹ شهریور در مدار صعودی قرار گرفت.
🔹
تشدید تنش‌های سیاسی و پیشروی نرخ دلار نیروی محرکه اصلی بازار داخلی بودند، اما افت بهای اونس جهانی مانع از جهش شدید شد و شیب رشد قیمت‌ها را کند کرد.
🔹
این واگرایی میان دلار و اونس، طلا و سکه را وادار کرد تا با احتیاط بیشتری به روند افزایشی خود ادامه دهند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/688697" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اعتراف رسانه نظامی آمریکا: ایران به هواپیماهای آمریکایی A-۱۰ و F-۱۵ در اردن آسیب رساند
/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/688696" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b0fcb209.mp4?token=bu6T0LLD4COmxK5rcNE9cW9SfDeiinIw1uUTshUY7SzteOtO-Jk_wlrqimHEa7SCVn7kqdDa7BOXM4nwH0poyYTPytwWcMnEQ6xbWzxAKkrSF9-gtqLtM3UmFmAoVaoHl0RO1y7X7McBHmfDYYfPynu3MmkdC2U914z8uLWE6hTaRAmLS4ZqWOP6QDZ7SDQXLAF6Vp66HAcxPSGJRrI5idRJM1mcQGma3LKfmkN-7jPQy5-ZTwqtMNCNorTmWzlgbEk83PgCIuFNALR6GcPFBmD_XkqqSsCibOBGNiW_-2iABG5NyFTpETUOa_90gSJQiFxAsC-dL6ZdAV7jyTNQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b0fcb209.mp4?token=bu6T0LLD4COmxK5rcNE9cW9SfDeiinIw1uUTshUY7SzteOtO-Jk_wlrqimHEa7SCVn7kqdDa7BOXM4nwH0poyYTPytwWcMnEQ6xbWzxAKkrSF9-gtqLtM3UmFmAoVaoHl0RO1y7X7McBHmfDYYfPynu3MmkdC2U914z8uLWE6hTaRAmLS4ZqWOP6QDZ7SDQXLAF6Vp66HAcxPSGJRrI5idRJM1mcQGma3LKfmkN-7jPQy5-ZTwqtMNCNorTmWzlgbEk83PgCIuFNALR6GcPFBmD_XkqqSsCibOBGNiW_-2iABG5NyFTpETUOa_90gSJQiFxAsC-dL6ZdAV7jyTNQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مامان‌ باباها درک همین چهارنکته باعث میشه فرزندانتون ازدواج‌های سالم‌تری داشته باشن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688695" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688692">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjgDo_TZzfxtXn47gMatO3nnpDteB2PD-4SJsEBOW0GdbsYsEh1dmNu5UhjbppY2PVwZsa97hcziHxgSbLynNiKiTNB3xLupPDUI6AJp-qyckdXz2el6sq4SP0e5_RiQH0_tQBhLuDWeyvzg534V_duO54rg9aPu3woHZofSNYq3p_CHIPoIFrn5DmVIdYw1kJVEJM6VwB1gAG4M29lZ8folDTnheER38RctwGtypOvNj_lQuU9IrHHbUL7GOQ5J8YOa9ho8bC3AY9kPvJDv1scYb0FiMo9r-Cr7AdaPQvY20a4njIz1KxDU-tMqUHvDqF-jJ8xsrf1kXFJu9DN2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQKqG9ESbakBSwFciUktfawZ2RwDGCIlf7qYSAvRWNezwl6LwZx2nZc2Ew_FULAluyNid45uhgIfsQ0aZqr880yuU-FwbTbqIIKgyeq4CBZwJXIF2xSd29crMTaa7SXstTnKNWRSY0kRzHfwLJWdqbXAUsjAzV3hiGcslY6vk66rCy17IJXP193qk82unsh-c9JvMt2dM49btPi36DavqEUhMnk7RWZOrEfwopXfEBVMPvf_smzUvSwbgGZ-b7ZQFfhXzATDTJqJMf5AVj3LIDH0hEHlK2yCc8RDPCtAnrFOJwG8gy244Mr849qlVxq0NoTfgbv49PTmfbaftVs2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4NB-q6-CNCsYqAJebsssEZoFneLjR9Dm_jybK6Y1NslMiuWcHqj7G5J6WV6H31RDJCF0occzB4aS_lQNFBp1F4OtM7QJ53XriW8His5E-dzFIuUMMrnRQT7WdD-2tIKvv3qK2mzwEhuot84Gu0N5kVfq4U-thxJSWAU9UaV4ZOgIMXUW7_xj_Y1qYewJ_7DANMTTrZaA-_WWZ6ZxPmwsM2g8JSe2bBiBSpCpVBxm-rVR0HIr6noDHPamWdXCnA3A5m0B1mSOeJr83T2asRSSOQlhRuErPDMIdgBJ7V7r6j9IPlW6rertIY2bFpVIf-1qP1ESeRwa5z0iKHKP0J6dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالیچه‌های زیبای ایرانی زینت‌بخش خانه‌ها حتی خانه‌های دوره ویکتوریای انگلستان؛ خانه موزه سامبورن، لندن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/688692" target="_blank">📅 13:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/688691" target="_blank">📅 13:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cep6vS0nwghiF3mLdrYwM-41da1I0SJJDVLkNOxQnqmvD17GARc8t_urjcaAvjBTxVIfgmOLLiHPr8PqCuBMeM0mJNKVl3QtZkq5h4Ru9sZl_woD3SXx6ohf8dpQgn2Ec8KCR29lYuQVR3xt833rF402UMR_mpOzn9Rbl16oSUsnx9olq6PuFRB861RHqJFaynea7BcWMZvPfYAUA8M0cX8mQwuALfN2in67kZFLxgcU8FmzV0m1TB_7SFlc2IICRaKAST-8jWRYURx7ffj4e46bocsERE_PlHjKrVAZBKi_hU0db9Hfhc-zwYlVs6-QDirVhwGrc5OUPiZO_t3e2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
قاب ماندگار ۷ دهه اعتماد مشتریان/ رونمایی از تمبر یادبود ۷۵ سالگی بانک صادرات ایران
🔵
بانک صادرات ایران به پاس ۷۵ سال حضور متمادی در عرصه‌های اقتصادی و روایت نمادین اعتماد تاریخی و ماندگار اقشار مختلف جامعه، از تمبر آغاز ۷۵ اُمین سال فعالیت خود رونمایی کرد
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/688690" target="_blank">📅 13:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688689">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هشدار تب کریمه کنگو/ رئیس مرکز بهداشت یزد : با شناسایی ۷ مورد قطعی ابتلا به تب کریمه کنگو و فوت یک بیمار بر اثر این بیماری، شهروندان گوشت مورد نیاز خود را از مراکز مجاز تهیه کنند و از کشتار خارج از کشتارگاه خودداری کنند.
🇮🇷
✊
@
AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/688689" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بلومبرگ به‌نقل از منبع ایرانی: ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/688688" target="_blank">📅 12:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc7TzW0yitL34XI9WR3HKgWzit1JGY5yB1N7njdPtJL0FavGUAjQLeb4Gwgz_rtAv9UDOM5qh9bNu8LStHVNAX8Tpjkc_-If2jOsFeU7wgeQ1o6emcCLBWLJxNqiTIcEmU8kGJtYmDc887Vibn4N2mfrgZhwqT-n1HOQfZTedb2u2vw5TbheWlQOBtnDescfApfLds_DaQx_-FE5sKtgmorxunO3Oo9LeH2CfsymWlSrY0PGzHs-k1z_kaZoDbyBM1JlazoRsuBlmkDnrYMBAjdQE534oPcfSOlDJ8pRxbA-mqp5sKw-kWFqAxjuDE_oj6T66nQoT9YNVlSY1CH3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDeovFYpjnwTFearAWUz5de8a3JgqU6UNZ8_U8YQEX92bKk93qjdtv2Dsxtg_jttJV0WS708fnkOyLS9ngqGYG8MBtJLAYhsuROLDbiROGpWeeQXHDdc9SKGNX4w6kuC2xEIWmjdIiEPl6vAJDX6U5zo_CnBSIKmPb5Zme5CFHF9rGlGvBI69xkTvHI-Khm20eJs5UsPwIG-W6Neq7E2cVggyglXTqOTLes-4WIErfoSj8F66FJuCi8hfcLLCZDoCIKU_IgDE5rvAHuLMqeiH3Ed6BBZ6bI_fKUJSKoup-WGfDRG-g5G68XS8BqvC-nO0yNEXmM69oQpcsxYSXDKwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ادامه اعلام قطره‌چکانی تلفات آمریکا
🔹
آمار رسمی پنتاگون شمار نظامیان مجروح آمریکایی در جنگ با ایران را از ۷۵۸ به ۸۲۱ نفر افزایش داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/688686" target="_blank">📅 12:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
افزایش هزینه وام مسکن همزمان با رشد بورس
🔹
قیمت اوراق «تسه ۱۴۰۵» ۱۲٪ رشد کرد و هزینه دریافت وام ۲.۴ میلیاردی به حدود ۴۷۰ میلیون تومان رسید.
🔹
«تسه» مخفف اوراق تسهیلات مسکن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/688685" target="_blank">📅 12:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cygX1DAQ56bhWvX0DmHgFW2Pq9CFUAwITWfWm6u59nkIdzyXP5ecwqBRcx5zQeUXDOOj9Nl_DwFnnGM4aalKIruKno6AkLTNLVlL3rj7GhqKUTrS1_GsC7GAY-bkZeB5QxoQ7eD1jlVntRsu1QIiyMZYo6lgDXFvAOxS-SqD11wDjVrJeAYw_HUrSCiMOa666tFpQ3Gi-AXoKy8HQ6FIX84DekJaHso-fQaMuB8YDB-HADXE1QE6inNfG4jpbDnN2rT5_UhWYSwPl4mAF_n0J1Es55U1pEUjYuHFtyhvvj2qVTWm3G5Pc-s5i9o9B70UfxAHRuCkxHMkd-9nSo8Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر شایان: بنگاه‌سازی رویکرد اصلی بانک صنعت و معدن در حمایت از تولید است
دکتر محمود شایان، مدیرعامل بانک صنعت و معدن:
🔹
مأموریت بانک صرفاً تأمین مالی نیست و بنگاه‌سازی رویکرد اصلی بانک در حمایت از تولید است.
🔹
از سال ۱۳۹۱ تا پایان ۱۴۰۴، یک‌هزار و ۶۶۶ طرح تأمین مالی‌شده توسط بانک صنعت و معدن به بهره‌برداری رسیده است.
🔹
برای اجرای این طرح‌ها ۸ هزار و ۵۳۸ میلیون یورو منابع ارزی و ۱۶۲ هزار و ۷۴۵ میلیارد ریال منابع ریالی پرداخت شده است.
🔹
این طرح‌ها با ایجاد ۸۲ هزار و ۳۵۳ فرصت شغلی، به شکل‌گیری ظرفیت‌های جدید تولیدی، توسعه خطوط تولید و ایجاد فعالیت‌های اقتصادی جدید منجر شده‌اند.
🔹
همچنین تا پایان اسفند ۱۴۰۴، ۱۶۷ طرح با مشارکت و تأمین مالی بانک در حال احداث بوده که ظرفیت ایجاد ۱۸ هزار و ۸۰۱ فرصت شغلی را دارند.
🔹
در مجموع، یک‌هزار و ۸۳۳ طرح بهره‌برداری‌شده و در حال احداث با تأمین مالی بیش از ۱۳.۲ میلیارد یورو منابع ارزی و ۲۹۴ هزار و ۹۱۸ میلیارد ریال منابع ریالی، ظرفیت ایجاد بیش از ۱۰۱ هزار فرصت شغلی را فراهم کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/688684" target="_blank">📅 12:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688682">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار کرمان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c0c8a3ff.mp4?token=aZVeCPZdAliGg9UieftgRCULfn10TT2LvObyz1DSAqvJ01db72r-OwvqIg6TLoJG74NQ745Z9doVEmoEgZ4-IHmCkGQIZZ6-4Q-lh6P62WHfpN6-BUrCpvfGOfo2Xmpx37gjBh7D28bgWzXOrrm8H0-eKBZyPC2uLrlAcc7dxOh49TgRxboOaLBmei0EUwgOFDGXLmmWvsB7pf8cZagjS7w1Y2sCBVzXRUJ3u2Klm06wjvg8XXZK-hEUbSZFxvAHMKXLLXJZDRVHyhaie76prggihdexjbacBTLplNd9eLNX-N-Cd8eijxaXyZ3EuVFJ95h7vZUh1fHeh28PZaUTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c0c8a3ff.mp4?token=aZVeCPZdAliGg9UieftgRCULfn10TT2LvObyz1DSAqvJ01db72r-OwvqIg6TLoJG74NQ745Z9doVEmoEgZ4-IHmCkGQIZZ6-4Q-lh6P62WHfpN6-BUrCpvfGOfo2Xmpx37gjBh7D28bgWzXOrrm8H0-eKBZyPC2uLrlAcc7dxOh49TgRxboOaLBmei0EUwgOFDGXLmmWvsB7pf8cZagjS7w1Y2sCBVzXRUJ3u2Klm06wjvg8XXZK-hEUbSZFxvAHMKXLLXJZDRVHyhaie76prggihdexjbacBTLplNd9eLNX-N-Cd8eijxaXyZ3EuVFJ95h7vZUh1fHeh28PZaUTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«از عجایب کرمون؛ ممکنه وسط تابستون شاهد بارش برف و تگرگ باشی!
❄️
🌨️
»
🔹
بارش تگرگ جیرفت سربیژن
@kerman_news</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/688682" target="_blank">📅 12:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688681">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f166173e8c.mp4?token=muyAvbv7tZsc6q9EQHXXJNrQdD-6Gi56igoIPOa7gGn9XvVv3QxARgDnF7xKevfD29sWJl3aQCTz3lm71NamkY8e53HATnKAgF6829jzfsUsuHEsgrMFtvR0LdnuYfR0mCtAC0wgFPcjE0NyxPDinJ0MpB_V35r7Z2TCFj87xA5vdu6cQvH0gqY0bOe6W3EAEn6Ne9_hrWOHbeTMpYf-D5vJKFK8tB4WS_KxGsNAOekhObtXx7qJ_liOQC-y0bnKvDUzfHUfvssbID-YaOPohGMz1j1xvecVvpFszQKoVPmmn04Sziopq95ji21G_PgA5NUo0EEJBx10asrKtQe3yqXlDgHrSJBTJHcB9ns4o78l1dbUkA5td-1cl6XUIu_3XXEwtK8ElN-_PgKDm8n9bLdYr8oJpxf4WnhryMge9g53YCjVu2rgLXNoKdA8LmkEobKJYNOjbP5jIGXff5wKGX1C74_sEsa7ngI6VOzQicxlY3sUNRY3a_M8RLWGCF9JUuB7Rw55CZEwSZAXD39oDLRElMXwEhD0b6aIvtD6a2wEqghC42pbRa4XwtPRc60moynrzEk0o_QqjEhneUT8Rufb-PavUQueO-KLVhJZn5d0OqZ9WKpkkShtvenD1uv4hAmEmank187D8wcHXq2ITvoUgxZjKEIcnKtKExTmy8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f166173e8c.mp4?token=muyAvbv7tZsc6q9EQHXXJNrQdD-6Gi56igoIPOa7gGn9XvVv3QxARgDnF7xKevfD29sWJl3aQCTz3lm71NamkY8e53HATnKAgF6829jzfsUsuHEsgrMFtvR0LdnuYfR0mCtAC0wgFPcjE0NyxPDinJ0MpB_V35r7Z2TCFj87xA5vdu6cQvH0gqY0bOe6W3EAEn6Ne9_hrWOHbeTMpYf-D5vJKFK8tB4WS_KxGsNAOekhObtXx7qJ_liOQC-y0bnKvDUzfHUfvssbID-YaOPohGMz1j1xvecVvpFszQKoVPmmn04Sziopq95ji21G_PgA5NUo0EEJBx10asrKtQe3yqXlDgHrSJBTJHcB9ns4o78l1dbUkA5td-1cl6XUIu_3XXEwtK8ElN-_PgKDm8n9bLdYr8oJpxf4WnhryMge9g53YCjVu2rgLXNoKdA8LmkEobKJYNOjbP5jIGXff5wKGX1C74_sEsa7ngI6VOzQicxlY3sUNRY3a_M8RLWGCF9JUuB7Rw55CZEwSZAXD39oDLRElMXwEhD0b6aIvtD6a2wEqghC42pbRa4XwtPRc60moynrzEk0o_QqjEhneUT8Rufb-PavUQueO-KLVhJZn5d0OqZ9WKpkkShtvenD1uv4hAmEmank187D8wcHXq2ITvoUgxZjKEIcnKtKExTmy8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از امتحان کردن این ذرت مکزیکی دیگه از بیرون نمی‌خری
🌽
مواد لازم:
🔹
بلال
🔹
کره ۵۰ گرم
🔹
پنیر گودا ۳ ورق
🔹
پنیر پارمسان
🔹
نمک، فلفل، آویشن
🔹
شیر یک استکان
🔹
سیر ۳ حبه #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/688681" target="_blank">📅 12:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688680">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره VPN ها؛ اطلاعات کاربران در معرض دسترسی است
معاون فرهنگی و اجتماعی پلیس‌فتا فراجا:
🔹
نمی‌توان هیچ فیلترشکنی را به‌طور مطلق امن دانست و اطلاعات و داده‌های کاربران در زمان استفاده از این ابزارها می‌تواند در معرض دسترسی قرار گیرد؛ از این رو کاربران باید از VPNهای ناشناخته و غیرضروری پرهیز کنند./ سیتنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/688680" target="_blank">📅 12:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688679">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رئیس قوه قضائیه: دو وزیر محکوم در دولت سیزدهم ترک فعل نکرده بودند، بلکه مرتکب جرم شده بودند/ وزیر کشاورزی دولت مذکور در دو پرونده متفاوت، مجرم شناخته شده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688679" target="_blank">📅 12:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688678">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqs8QNYf06bCYaTCVojzllia16Weg223EFv4gFVbwXu_7Bb_NBvAE9-QIzczDhINNlhbGZN6HAw0nrgRGQijFycRu4rGAy7WL6UDtBnz7u0tnK6FNBQk4ElFylVzt4Wz3KU2L0UPnVlzjhH8jfCnOIfTK4uK3ERaZxCnrKaPe0ww3bRlIvuG4Mweder-h1ao0XOHlInviBXum8jK5Shj4jQnW8Q4-MYAhTHYPqibY3RWiYzf3yxr0EHf7S62kx92e0NRkBkj7Jwy4rfE5sfv30Zw168soa-W_SgOQwrqUNC2dvPE3Dy8muEPxiXooj-98Pz5SmXTdpODCzPAOPlUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصلاح تعرفه‌های ارتباطی شرکت مخابرات ایران از ۲۰ شهریور
🔹
شرکت مخابرات ایران در اطلاعیه‌ای در سامانه کدال از افزایش ۴۵ درصدی تعرفه برخی خدمات ارتباطی از ۲۰ شهریور ۱۴۰۵ خبر داد.
🔹
بر اساس ابلاغ وزارت صنعت، معدن و تجارت، تعرفه مکالمه تلفن ثابت با تلفن همراه، تماس‌های همراه با همراه و پیامک تلفن همراه تعدیل می‌شود. در همین راستا، سقف تعرفه تماس تلفن ثابت با اپراتورهای همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش خواهد یافت.
🔹
مخابرات اعلام کرده آثار مالی و درآمدی این افزایش تعرفه هنوز مشخص نیست و متناسب با میزان تحقق، در گزارش‌های مالی دوره‌ای شرکت منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688678" target="_blank">📅 12:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688677">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6de943b0e.mp4?token=h7iRKB62_ZonXTxGCQ6nj30gbFjeLUjM7Zw6B7CFnBwaR5YLzumuhUP52vuKIu9qiN-rtcC4RiC2HfxFKLMZb63NDA4v1w5jm7iV9q3DZuUyg1H_900t6_sbPVDAIZrKqrCuFG1woHhsbvlF6s4kz12KvPqO_WN4ah903hCEIXOM19fjumoLhAIXj-byej07fEwdJLBFqFftIhpnD3cn6tVNW5w4nWAe03j2AanSvecXeivNnBWawOIKUWOF3XhHyA6TAzyfFp0woJV0v90jAD6hYuQFw6swONWFfdzIxd6bMvK5AyRtR1_YBGd_idGnpQUBIeJtrRlDgebXXFhLHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6de943b0e.mp4?token=h7iRKB62_ZonXTxGCQ6nj30gbFjeLUjM7Zw6B7CFnBwaR5YLzumuhUP52vuKIu9qiN-rtcC4RiC2HfxFKLMZb63NDA4v1w5jm7iV9q3DZuUyg1H_900t6_sbPVDAIZrKqrCuFG1woHhsbvlF6s4kz12KvPqO_WN4ah903hCEIXOM19fjumoLhAIXj-byej07fEwdJLBFqFftIhpnD3cn6tVNW5w4nWAe03j2AanSvecXeivNnBWawOIKUWOF3XhHyA6TAzyfFp0woJV0v90jAD6hYuQFw6swONWFfdzIxd6bMvK5AyRtR1_YBGd_idGnpQUBIeJtrRlDgebXXFhLHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول ۲۵ متری خیابان‌های زوریخ؛ نسل تازه اتوبوس‌های برقی در راه است
5️⃣
4️⃣
3️⃣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688677" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688676">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزیر دفاع یمن ترور شد
🔹
منابع یمنی می‌گویند محمد العاطفی، وزیر دفاع دولت نجات ملی، همراه با شماری از فرماندهان انصارالله در حمله هوایی به غرب تعز ترور شد.
🔹
انصارالله هنوز این خبر را تأیید یا تکذیب نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688676" target="_blank">📅 12:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688675">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3nw-BlOoeAn27U24kN1qCNELAMQNxPPk2Q4LuilCWHrGLzxg37ZRazA9MWgTOoXBxjoa8v40eJL-rgeeQuBI9bT2SpSxMwK2NUAnFOraO4X7bzr5iVg5BpSnnKRB8UlkthV14DwA__l6DlfcqYexmvAYpS_zBc1Kir2vj1b6rDLLcd0BAbqhzFowf1gC12qokbJTx-g9dVuuQl5yKqxaV5Jw-3fWOfyK307DXEhcOxllcNqvTd-2ri1I_dbcqPanHWuJpCuowacNa_daCf6e0Oz6_bIow35j1FeFLCqlY6qDqOEyvTHo1xR5HM71rR3-9iKAwo2_ZGLTiTGzeT09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همیـن الان یه قدم به سمت رویاهات بردار
🏡
ویلا |
🌳
زمین |
🏠
ملک
📍
چمستان | آمل | نور | نوشهر
فایل‌های منتخب برای خرید، سکونت و سرمایه‌گذاری در مازندران
👌
اگر دنبال یک ملک مناسب در این مناطق هستی، حتماً کانال رو ببین
👇
🔔
https://t.me/parsia_villa
⛪
کارشناس فروش المیـرامرادی
09196674154
09196674154</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688675" target="_blank">📅 12:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نگو که نمیدونستی
😮
😮
جشنواره پایان فصل امرداد از این هفته شروع میشه
😍
💫
۲ هفته کلاس زبان آنلاین رایگان از هر کجا که هستی
😇
امتحانش که ضرر نداره؛ کیفیت کلاس رو ببین و بعد تصمیم بگیر
🎯
🫵
ظرفیت فقط ۱۰۰ نفر
🌸
برای رزو این دو هفته کلیک کن
👇
👇
https://amordadflc.com/home/sitepage/4860
☎️
02128429272
🌐
amordadflc.com
🆔
@amordadflc_admin</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688674" target="_blank">📅 12:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
آیا پاییز و زمستان قطعی برق خواهیم داشت؟  وزیر نیرو:
🔹
از الان نمی‌شود پیش‌بینی کرد اما تلاش ما این است که پاییز و زمستان آسان‌تری داشته باشیم./ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/688673" target="_blank">📅 11:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688672">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgZnWfO0G8kzdea_jBI3xNAhnjUHC5NzcMXUWW_vcMW27oQLo4bj2QPtrp6fJhZrlKJhhk73i0m3bU0TQXt2uwqyzHLgMh8LWO9c6oSZLscxiCpLsQw9139G-ioJWs5rxk1pX7L9BQvIhROZd7usDyeaaW9tzzm93YPiy-nRVdDN5bEg150-bngKfiY1rhe7MIhH7mVnSYBuPMbGh0yJivScgh00uEWjFzejL8VwLSgqtk8U4xcU_cgzWH_YlQL5n9ZZXym854ejWmO7862x9OqgAWGWY7Gz8FeeV4pNdRVNPVmJZy5VJbqWiYM-Snqlt5IZeaCRjqKClF8eWxKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز به نقل از منابع مدعی شد: ایران از یک سازوکار شبیه به تهاتر برای فروش نفت خود به چین استفاده کرده است
🔹
پکن پول نفت تهران را به صورت اعتبار، جهت خرید کالا‌های چینی مانند دارو، خودرو و تجهیزات نظامی پرداخت می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/688672" target="_blank">📅 11:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688671">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52d9a4bf3.mp4?token=ZC_PvyiXO0LwJn0EHQaqRCdcoyfC7KjYgM0LDMykWWLIbsnWs2ilzyP0_zGkc4aaZz_Hf5OgDOST_K-NYvjqwHhn6rqzZcYfwM4Ip19vemxYBha2ssOfHyrRJou6IvK0cbS3v-iLt-xxe-cXX2Whd07_byv04MxlILEQkxyMCUB77uZ31kqCJnDDd9v8MSqXKeh5fgg7IOadCTF0quU9urD3dtaVlv5WQX84U7cV3cJNdSKEZcxRv3b9cPTcgSxrDG9tPfBe-fRLPMfLuHiPbIQuYg5gDmPFHHFocN6IElKupqVrzukErdoNNj1Bos83WOI4cOm1FXiRYFQI88lzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52d9a4bf3.mp4?token=ZC_PvyiXO0LwJn0EHQaqRCdcoyfC7KjYgM0LDMykWWLIbsnWs2ilzyP0_zGkc4aaZz_Hf5OgDOST_K-NYvjqwHhn6rqzZcYfwM4Ip19vemxYBha2ssOfHyrRJou6IvK0cbS3v-iLt-xxe-cXX2Whd07_byv04MxlILEQkxyMCUB77uZ31kqCJnDDd9v8MSqXKeh5fgg7IOadCTF0quU9urD3dtaVlv5WQX84U7cV3cJNdSKEZcxRv3b9cPTcgSxrDG9tPfBe-fRLPMfLuHiPbIQuYg5gDmPFHHFocN6IElKupqVrzukErdoNNj1Bos83WOI4cOm1FXiRYFQI88lzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژل دانه‌ کتان، ارزان‌ترین کلاژن دنیاست
🔹
دانه‌ها را بجوشانید، لعاب طبیعی‌ آنها آزاد شده و ژل غلیظ به دست می‌آید که پوست را سفت کرده و موهای آسیب‌دیده را ترمیم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/688671" target="_blank">📅 11:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXy4nVds-kdq6VnU7NKeT5sfIDKbtz6JXKdninstEyCqcAC329nn2TtE-7Wg-2tE7BkGGr6zxFbOrZ0x75B0tL6K-nAP5Gk6NKvBGuXUH_bDNhk3HuEPUAZOBLK9WESiVLBb5cpC8QExEHMfH_wc4wzN4WzCny7jSSPbHYHb08q1htYj3Ea4w7Vy-gN9F9-F73iyFpmzzDSTg7GA-3G_C31CuaQkmwxJ3jRGzCErPzWIzw-jGxVSjtmjZO8jJ5DEiS8g0-uecpDJGkXW0IQ-p5ZHQsvDmnhD1-cjlydigqNGXTh21tvsiMXcoVX-JeyfbYhCHgButAmbCrs3w2rEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرعه‌کشی جام ملت‌های آسیا ۲۰۲۶؛ تیم ملی فوتبال ساحلی ایران پس از انجام قرعه‌کشی مسابقات جام ملت‌های آسیا با لبنان، ویتنام و افغانستان هم‌گروه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/688670" target="_blank">📅 11:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
آیا پاییز و زمستان قطعی برق خواهیم داشت؟
وزیر نیرو:
🔹
از الان نمی‌شود پیش‌بینی کرد اما تلاش ما این است که پاییز و زمستان آسان‌تری داشته باشیم./ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688669" target="_blank">📅 11:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
میانگین قیمت خودروهای وارداتی چه قدر است؟
🔹
میانگین قیمت خودروهای وارداتی در سال ۱۴۰۴ حدود ۲۳ هزار دلار است که نسبت به سال‌های قبل افزایش یافته. در سال ۱۴۰۲ این رقم ۱۹ هزار دلار بود، چون بیشتر خودروهای اقتصادی وارد می‌شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/688668" target="_blank">📅 11:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc4549ab4.mp4?token=HVunTeB8vLPT7pkMY51kmEagnyUqF1x-NpgM5Hw1a_3hpp0MXwnAqnX8bMkqHtvLU4h7GS1ldNK4wPhv5MDC-gd-pfBQwSDIU2UIlf-QsC55qE0xfi-rx1x1r0XKHTSezCeCNNqHSf36UIlYfxWeHreEkVXQESob5j7_u-Vc65NvTSN9XyH9OP5A858L6vmxLNWwkGdE86f9vHxUiNZspNsRb_NZlL74B2pQ_WcwOz48FiZ2mu1FmIJqt_Z-1hTpgQOsFzTxQCnH2Un9X2YqAgCm-XJ_bNzwA_zImR7mH5SrF-FfDaBem9qlZDsOUeisEJMqJBgsUrfYpWL7HJDv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc4549ab4.mp4?token=HVunTeB8vLPT7pkMY51kmEagnyUqF1x-NpgM5Hw1a_3hpp0MXwnAqnX8bMkqHtvLU4h7GS1ldNK4wPhv5MDC-gd-pfBQwSDIU2UIlf-QsC55qE0xfi-rx1x1r0XKHTSezCeCNNqHSf36UIlYfxWeHreEkVXQESob5j7_u-Vc65NvTSN9XyH9OP5A858L6vmxLNWwkGdE86f9vHxUiNZspNsRb_NZlL74B2pQ_WcwOz48FiZ2mu1FmIJqt_Z-1hTpgQOsFzTxQCnH2Un9X2YqAgCm-XJ_bNzwA_zImR7mH5SrF-FfDaBem9qlZDsOUeisEJMqJBgsUrfYpWL7HJDv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ متوهم: ما دقیقا می‌دانیم در «کوه کلنگ» چه می‌گذرد و فعالیت‌هایی را در این سایت رصد کرده‌ایم/ ممکن است ناچار به هدف قرار دادن این مکان شویم ‎
🔹
ایران در حال فروپاشی است و برای دهه‌ها قلدر خاورمیانه بود اما اکنون دیگر این‌طور نیست. #Devil…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/688667" target="_blank">📅 11:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688666">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803268b4e6.mp4?token=UiJjQD-58wNWG6hHuE3ibECzX8ntSA_ksozRsWpHOGcYXA6wI4zXKh09MqG4wKD-1dNHP21Z_dL0MeUfsFRUi2xisS6JGUbi8XVVNXFqAzTiCc3VdzO9FYyXegI1jAVI7WW6O_ds2QO8pHJG0E-sIKNsVhNd0QLWmWhASdH0rHVbJvfsvtZSYMpcLpN5AKHHIpoiCp3AOs3Ulx53goyjY68_0Tfzw8HeveDKMt8aQtygJtsvywU3yhz6KaKTP0HSWWjQukkTHiPestXlIIFw4tXkuSpQ3oefddoAuotgYO3ysSFhLruRyKfDXIchJwOLK4Ubo_3r_hby51ZOQSOTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803268b4e6.mp4?token=UiJjQD-58wNWG6hHuE3ibECzX8ntSA_ksozRsWpHOGcYXA6wI4zXKh09MqG4wKD-1dNHP21Z_dL0MeUfsFRUi2xisS6JGUbi8XVVNXFqAzTiCc3VdzO9FYyXegI1jAVI7WW6O_ds2QO8pHJG0E-sIKNsVhNd0QLWmWhASdH0rHVbJvfsvtZSYMpcLpN5AKHHIpoiCp3AOs3Ulx53goyjY68_0Tfzw8HeveDKMt8aQtygJtsvywU3yhz6KaKTP0HSWWjQukkTHiPestXlIIFw4tXkuSpQ3oefddoAuotgYO3ysSFhLruRyKfDXIchJwOLK4Ubo_3r_hby51ZOQSOTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
رئیس میراث فرهنگی سبزوار:
🔹
کاروان‌سرای تاریخی «روس‌ها» در سبزوار تخریب شده است. این بنا در دوران پهلوی ژاندارمری بود، سردر باشکوهی داشت و برای ثبت ملی اقدام شده بود. تخریب توسط شهرداری تأیید شده و مجوز آن احتمالاً با جمع‌آوری استشهاد محلی صادر شده است.
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/688666" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPFS79oUC6svuvOWP0qgFJINgv5l8bCge_pIQ9Y_U0QhBbFmVS6XdwuoMk8dLICUBlz9XyAG25VejtdauImqsF_0zpn-tdslZvlvmEt9ovvnuYoNnLIr3JLJpN3JT3gS7Ol1_1AbCMETQ488mJaQS089qxgBUgKABIQJrmPTRxsfKq6tkmz1WOmZ36IcI9o9yrTGe3xOZxlhUFhlVD0eIrDHZoOiw39CNQj5ZeqKqxEoBEGvjALUuuOZVjQALlw4H0_ywH94i8cn3BIFSztLVcrPSe1mg8jyfViG1fbTgdlhuv-OuQn1i2OPpWmAah9BP4YjRdbolyW4Swbaoz67jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: پنجشنبه ۱۹ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688665" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ed56d9b64.mp4?token=kNAcISSJkDIHsA3-Jrn4sNJp1-vjlRYf0WSLspqQ4-CQce8v71YE3vcwPUki8gprsmqjL82RhXHKzj4f1e7atL4HgBVRjv4DA1uMUEfGE8TDR0CnjvXf-MZwHMfBE8DeWcQgn55zLRG4EAOLs6_089Mm2csIywjpHXh77mZ2J0HFTEhDFxzacr14bbtnSs2RR48LCz31J57HjOdd6nYgh6xfHwtNv4xgWlhJzOIIMW84QPe2SIJdt2V2US7bZ7H64yScm7ZgRkGEU3xXKQT_8uR-YV0NS3-8eRa33JvUlduD1baDjhpPyeRbr1ZN_1aV0z9mC4HEe0okLexPsxPvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ed56d9b64.mp4?token=kNAcISSJkDIHsA3-Jrn4sNJp1-vjlRYf0WSLspqQ4-CQce8v71YE3vcwPUki8gprsmqjL82RhXHKzj4f1e7atL4HgBVRjv4DA1uMUEfGE8TDR0CnjvXf-MZwHMfBE8DeWcQgn55zLRG4EAOLs6_089Mm2csIywjpHXh77mZ2J0HFTEhDFxzacr14bbtnSs2RR48LCz31J57HjOdd6nYgh6xfHwtNv4xgWlhJzOIIMW84QPe2SIJdt2V2US7bZ7H64yScm7ZgRkGEU3xXKQT_8uR-YV0NS3-8eRa33JvUlduD1baDjhpPyeRbr1ZN_1aV0z9mC4HEe0okLexPsxPvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از اولین بنز میباخ ۲۰۲۶ دنیا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688664" target="_blank">📅 10:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397d00b91d.mp4?token=vagz7dSs1W9ruc3q2Ilcj7-7LczooaDs38sa3vd7V51MAyCrZxd0p4EikNmIO88biOskaCLHnjAVZWc7V-JymTMXjGighNLTjW5ejUGLitQQ_8MSI4C1JYj6wj_GtwByvyvjYyn4o8Oxboxz5gIkfn1QluzxoniRSbKcINoelkjxNC4oHBCexwNO3-hbsb4NCMft-7xhPoyNPr1DljZjjj64UKjtzruZ5HdEVBWEmJCtPOM0y9DewXWA4F7fPAZlD29bhXWhUCC6NkirFwQ-8EPDtIXeVqCsTL0WAGkHb8emVyfxHsi2ysDfYGptvqhKoiRAgGVUBqzYkKsfRGgPpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397d00b91d.mp4?token=vagz7dSs1W9ruc3q2Ilcj7-7LczooaDs38sa3vd7V51MAyCrZxd0p4EikNmIO88biOskaCLHnjAVZWc7V-JymTMXjGighNLTjW5ejUGLitQQ_8MSI4C1JYj6wj_GtwByvyvjYyn4o8Oxboxz5gIkfn1QluzxoniRSbKcINoelkjxNC4oHBCexwNO3-hbsb4NCMft-7xhPoyNPr1DljZjjj64UKjtzruZ5HdEVBWEmJCtPOM0y9DewXWA4F7fPAZlD29bhXWhUCC6NkirFwQ-8EPDtIXeVqCsTL0WAGkHb8emVyfxHsi2ysDfYGptvqhKoiRAgGVUBqzYkKsfRGgPpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر روزتان را با ۱۹ بسم‌الله شروع کنید
روایت داماد شهید رهبر شهید انقلاب:
🔹
رهبر شهید، هر روز یک کاری را به نیت حضرت امام زمان(عج) انجام میدادند و ثواب آن را تقدیم ایشان می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/688663" target="_blank">📅 10:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd13c4a34e.mp4?token=NGRp3UW2AnXz8lertEoKRM4ryU0Gk8BWly1rKm5BArcTKHz1TlRnqzZNDgAexK3eaI7ge_Mkgrtzi8nkZwCvmESYk8irkF4RxyfoYBFTKp94bfXhp1eU-oLNOANRLK_N20LMr2qsiOxUdfx03JUvtSELMLzgl1jhUW4hmysCjPPYcBpL9hvpQAUOjoMVlLqyIKn38AoXzXHV4-ZQn3L5Yyj_KqphWCRVr7Ep7-55A6NTrbRCcRBJuKF_YiUFHYXsFOjEOqjHshQNy15JbAk5f-qIK48TNxEOSxHMQuZtXa5oFl6SHQGSndRL0PMI3YWjoCzPHZHOM8m7fZW6ATVI86EtVWZc1J_pKNKxVdkxWhd1N4-Y1ShTawI_70qTrakZ7HYr3jAea5dNyWsh9OY-TSWz_dXPwMaAWPXRU-4UcICHWNt2tJZYC2t5KBZ8fXSSqs0F4noSEV2GTb-By8rlnu-X_fvJn90kNkhhKH3S3Fewey6cDQUr-kF2P94q3u9OqnMQNoJ6vWbegEWUVpWja9wZCnaHmj0Wh5KcTecMCkyFjF7JFIBBsirAhZNUpTeTiVPo0WcdpLsKiiy9WEsvhK8S9G9nXznoWBgw8h9Kk7EkjkQNUeAVql1UyGUOE3Pp7GOIbCn9R3uBfyrEAIuXZBF_V45f8S5ED20QfnmrLkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd13c4a34e.mp4?token=NGRp3UW2AnXz8lertEoKRM4ryU0Gk8BWly1rKm5BArcTKHz1TlRnqzZNDgAexK3eaI7ge_Mkgrtzi8nkZwCvmESYk8irkF4RxyfoYBFTKp94bfXhp1eU-oLNOANRLK_N20LMr2qsiOxUdfx03JUvtSELMLzgl1jhUW4hmysCjPPYcBpL9hvpQAUOjoMVlLqyIKn38AoXzXHV4-ZQn3L5Yyj_KqphWCRVr7Ep7-55A6NTrbRCcRBJuKF_YiUFHYXsFOjEOqjHshQNy15JbAk5f-qIK48TNxEOSxHMQuZtXa5oFl6SHQGSndRL0PMI3YWjoCzPHZHOM8m7fZW6ATVI86EtVWZc1J_pKNKxVdkxWhd1N4-Y1ShTawI_70qTrakZ7HYr3jAea5dNyWsh9OY-TSWz_dXPwMaAWPXRU-4UcICHWNt2tJZYC2t5KBZ8fXSSqs0F4noSEV2GTb-By8rlnu-X_fvJn90kNkhhKH3S3Fewey6cDQUr-kF2P94q3u9OqnMQNoJ6vWbegEWUVpWja9wZCnaHmj0Wh5KcTecMCkyFjF7JFIBBsirAhZNUpTeTiVPo0WcdpLsKiiy9WEsvhK8S9G9nXznoWBgw8h9Kk7EkjkQNUeAVql1UyGUOE3Pp7GOIbCn9R3uBfyrEAIuXZBF_V45f8S5ED20QfnmrLkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی اپل از آیفون‌های جدید تا اپل واچ و ایرپادز
🔹
اپل شب گذشته از آیفون دوئو، آیفون ۱۸ پرو و پرو مکس، اپل واچ سری ۱۲ و اولترا ۴ و ایرپادز ۵ رونمایی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688662" target="_blank">📅 10:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTltY_VEGzrZtoNbZcKcF3pkw2oOBonN9yC2Be3GoV1hTauvtlUN8IaD84CcaXtpo-KgU56ehXA_B3-tdQHC9ZHG_0iszn0KUNRgdvCbgwqaRHop8M0Y1AdEUtjP_FIa5OrRMWwnqqW9FXU9tJfdEh14Al2E6Qb6avxo1ONlinviY_z4aaUCivhDXaEDk6kFw3nM070NYJGHNvgaeiB99O9VgtLrZ3Vj55oadyZmLujfdTXtW6V2V_qmavZ4ReGUL_PvOFBXWGoK704umxR-8gWtfifS0Bss3mhO9NKA1UD6R6_KcUqCi4ybRVwedEWlJqdc1Lzn_8sZkTZnFCqm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس گنبد و بارگاه امام رضا (ع) با نگین و متبرک
جلوه‌ای باشکوه از عشق و ارادت به امام مهربانی‌ها که حال‌وهوای حرم را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۰.۵ × ۱۴.۲ سانتی‌متر
▫️
ویژگی: مزین به نگین و متبرک
▫️
طرح: گنبد و بارگاه امام رضا (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه معنوی و یادگاری ارزشمند
💰
قیمت: قیمت اصلی ۵ میلیون و ۲۵۰
🔥
با تخفیف ویژه : ۴ میلیون و ۳۹۷ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/688661" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f5be1143.mp4?token=PLmN6GjWYPpl9i01mdlz2i3a0VUJd9NtpICGYc5wGDdqOQ2XJ3L7t6Ibbrta5mr9NVm5ZWipNedy8USu7imKmXZ51ClPHzDTdIwnRnMR7Q-psmyuLtIu0IqzE7IWAOUxaDO0jE8fwBo3ZhoPD71H0tfZn-EQP7zfSg01OW9NEY7-PfosyEqWFgFAySdI2Xszw--F1UUwB-JAvgYChvbH5EPgJ9Vl_MWz-1676vkdfQ-FpjXEeFt-8IQ_tRdy2fzKz_AoD_XLysLOgY5-uqXj51xcejh0j6l3UOX9ysWkutUQ6MVvfKZZqXrAtYXEuSNPMsFbgA0HRJmphDg1412M-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f5be1143.mp4?token=PLmN6GjWYPpl9i01mdlz2i3a0VUJd9NtpICGYc5wGDdqOQ2XJ3L7t6Ibbrta5mr9NVm5ZWipNedy8USu7imKmXZ51ClPHzDTdIwnRnMR7Q-psmyuLtIu0IqzE7IWAOUxaDO0jE8fwBo3ZhoPD71H0tfZn-EQP7zfSg01OW9NEY7-PfosyEqWFgFAySdI2Xszw--F1UUwB-JAvgYChvbH5EPgJ9Vl_MWz-1676vkdfQ-FpjXEeFt-8IQ_tRdy2fzKz_AoD_XLysLOgY5-uqXj51xcejh0j6l3UOX9ysWkutUQ6MVvfKZZqXrAtYXEuSNPMsFbgA0HRJmphDg1412M-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری و کمدین آمریکایی: چطور می‌خواهیم در جنگ با ایران پیروز شویم وقتی از پس جلبک‌ها برنمی‌آییم؟
🔹
ترامپ ادعای بزرگ کردن آمریکا را دارد اما با صرف ۲۰ میلیون دلار نتوانسته یک حوض را از جلبک تمیز کند؛ پس چطور می‌خواهیم در جنگ با ایران پیروز شویم وقتی از پس جلبک‌ها برنمی‌آییم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/688660" target="_blank">📅 10:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9jF1NEdTR4vIRGyc2CuNth1sNtgc1az86_vCgzb6gptowZ4vYzW4CY7AiC2axGGOqv004bZJO2o-4bxjfZIuUyNYOmQ92jRL0UKpBntONe_zEaGRck0E4w_gK3wzH8JU8aQ9VWGrsjXB0bX3i2KEBPpIs350rArbqKnWtJ1WBJGeV5_kEdCNNS8w5G1gBonWCFY3eSKmFSOuFigdbsFMcnDx69wrftyig28LFVCveVSsgNg95IlrmBu49wGZlXNmnYwKGUdxY7V0Yj5APc14NCkzQALvo4WyX4SFGxwX4qT6aIg98QmjQyrlFYYxYmLx8vyoJFXfVWaUeRnmJEsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: اشتهای ایران برای هدف قرار دادن نیروهای آمریکا بیشتر شد
وال‌استریت‌ژورنال مدعی شد:
🔹
ایران برای شکستن بن‌بست تنگه هرمز، درگیری با آمریکا را تشدید کرده و در هفته گذشته حداقل سه بار به کشتی‌های جنگی آمریکایی از جمله یک ناو هواپیمابر موشک شلیک کرده است؛ اقدامی که از آغاز جنگ بی‌سابقه بوده و نشان‌دهنده اشتیاق جدید ایران برای حمله است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/688659" target="_blank">📅 10:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2A2yzrq7FiVcOGpPOOfj1xXq2DgpNaCkfjXGBNHd59YAEhT1k-1c6yNJ3tVt5as88WCm_RtKtyk_Cw46HV0FhURvFI2V0ktFryqPcadtLF0Blh6lslLBwhVkul_bIIyeqKZmOkjwyCAaTNcjNXoKad8N4ugTmQIuUKCMZmdDqhrdORlyA0WryeC9vCOt8668zKwhE2sOY-i9CPbLB2lG3sqHJkjozm1SR0Gj3Z45qPTtOGtBm-svWRKErVLgusN2LIo1fldDSWaOgvG7lfoQplRrbb1wcCjNcr8SujHKOUBfbOEAy0XGyx83EHOpSuQPQ72DA228bJwgA8PNr1aJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
تا 70% تخفیف در جشنواره mono!
👠
کفش، کیف، البسه، اکسسوری زنانه و مردانه
‼️
امکان استفاده از تخفیف بیشتردر شهریور ماه:
💰
1,000,000 تومان تخفیف بیشتر با اسنپ پی در خرید آنلاین:  PAY2SCF
🆔
@monofashion_co
‌
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/688658" target="_blank">📅 10:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c9330f9f5.mp4?token=Q-nwCsGL7GheULC9_Ek5FHuLMNcNRo3oergUApgX2iWaK_UIdHd4805s7CE3NnKmim4YFjZvbhsUJKneFt4GqWtK9SEREzj0RW8zPicRZU8ZqKKPdt32pS5E7jWIffjNaQKCbX60gyAcJYooPX6GbRhV2tjOy9blhpNTZhAOLF_HUpfQ__lUjlL6ynGVmtKVVyXihigCzhHUCOEoz8VG1mm7J_hVlVRE9RLB2VKmlFcMNZodehTLY01PgaRgxSw9XCy3-wkDLDLCSvYu2NQzz0deKSLGat0ays9JohFNrUpRSNmyKYGrOHS8tlGcD1BZ2tzAUt9olmQu6GuVVXbADA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c9330f9f5.mp4?token=Q-nwCsGL7GheULC9_Ek5FHuLMNcNRo3oergUApgX2iWaK_UIdHd4805s7CE3NnKmim4YFjZvbhsUJKneFt4GqWtK9SEREzj0RW8zPicRZU8ZqKKPdt32pS5E7jWIffjNaQKCbX60gyAcJYooPX6GbRhV2tjOy9blhpNTZhAOLF_HUpfQ__lUjlL6ynGVmtKVVyXihigCzhHUCOEoz8VG1mm7J_hVlVRE9RLB2VKmlFcMNZodehTLY01PgaRgxSw9XCy3-wkDLDLCSvYu2NQzz0deKSLGat0ays9JohFNrUpRSNmyKYGrOHS8tlGcD1BZ2tzAUt9olmQu6GuVVXbADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به ساحل خزر
🔹
پهپادهای اوکراینی به بندر ماخاچ‌قلعه یورش بردند و برخی رسانه‌ها از احتمال حمله به میدان‌های نفتی روسیه در دریای خزر خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688656" target="_blank">📅 10:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af970436d6.mp4?token=TNswVDcOBsz3cbVKSAhc1MBFpg5obD72XdGg0IIi9Y5lPxEV6x3z-9wXYgkCgkrN2SSXEVWKut1VlXrOxWXE6T8EtxVlqY285aBOmhzr-5p-Ob84hoU2BECfwV8t9yNsZNPRMuz-TlUHoNCNY91pjrI25EZ614SAA47FkosO6LyomGkJ_jhnvSSoxoTDMInQErc0rG8vaZyZVMjlukIiaFFtZCGYrZxvOvED5eP4wjvuj4S8zJvMxpgAwOjNvEbydvbTCZQylDi5Sdl35SqcLgcWTWGcW0RkWRZmxqZarqxFX9MT0qKeJ11W72qiW7SHomHeJNriliYTcvTegrEllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af970436d6.mp4?token=TNswVDcOBsz3cbVKSAhc1MBFpg5obD72XdGg0IIi9Y5lPxEV6x3z-9wXYgkCgkrN2SSXEVWKut1VlXrOxWXE6T8EtxVlqY285aBOmhzr-5p-Ob84hoU2BECfwV8t9yNsZNPRMuz-TlUHoNCNY91pjrI25EZ614SAA47FkosO6LyomGkJ_jhnvSSoxoTDMInQErc0rG8vaZyZVMjlukIiaFFtZCGYrZxvOvED5eP4wjvuj4S8zJvMxpgAwOjNvEbydvbTCZQylDi5Sdl35SqcLgcWTWGcW0RkWRZmxqZarqxFX9MT0qKeJ11W72qiW7SHomHeJNriliYTcvTegrEllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور ترامپ میخواهد شهروندان را در این ثروت عظیم ناشی از تعرفه ها سهیم کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/688655" target="_blank">📅 10:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYq-S1KDUUagLSX5KwLEPT2D-Wd8iBs_-5Z7u3fI0mE7PkUaOR554Awk1nNhjJa2pbQRx-rKtygj9NIIdhZcAJg8GGjlJi9Di35V4_4H2-JaEhFIt6-4ctN7yxgv-OxObHMQE1T1UXH_HX-YjqUAf3NTcxpJRqJwBxzreEQuwh7sqGYZTKft5Fjr9-br3OqCVjvu47oXw6cDG3C4j9_2DLv7x4xlG8k1spQPnl4dSOKUt9cSrsTry0Gli3--8fz4uKJxf8PbwkUzm64sAeljXrXhWyA0ZwGRc2GIAc8lVJkCKQ_wNgdalN0c5TuRWH1sFFUW4X_1ivvkgwK2izKaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره یک غنیمت جنگی بسیار بزرگ در جنگ ایران
🔹
جزیره پریم در تنگه باب المندب، بعد از بسته شدن تنگه هرمز و تغییر مسیر صادرات نفت عربستان از طریق دریای سرخ اهمیت زیادی پیدا کرده است.
🔹
منابع منطقه‌ای به سی‌ان‌ان گفتند که حوثی‌ها در حال انجام حملات بزرگی برای تصرف شهر موخا و رسیدن به پریم هستند.
جزیره پریم یک نقطه حساس ژئوپلیتیکی که از زمان جنگ آمریکا با ایران اهمیت فوق‌العاده‌ای پیدا کرده و در حال حاضر از آن به عنوان یک غنیمت یاد می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688654" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04b4e8f9c.mp4?token=D2osNiGASs1rsrAqy6KawijTKyUjjZJY-DtMi4jfHZLCwOe1zzR0Hm6E4hOK5Ntd-Q5a7bgeQY7YkqwV21Hg5HCCgZ790ka3taUl_8Qb8MYq1hxOrs3ZPhdKLfrY_hQHVYPvRmGfmuJcDnZl85TL0r5FQ6bZ01DBr_zHNhZup8NUjXFq5yAhH5BiTc5QlPjhF_7LAYraR7tftD9mNnp36jg4TXikoB7r-7WRtaB06QrBl3oTV6UqI1CfgTfCN3KNOCLaMueyyhQtLvR5HWj-pN_ev33BtoNKEjtpqEIUdGkrI3iDO9WifxNoHCCwaK61pBNxtpiSShGgbfRv2w0drw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04b4e8f9c.mp4?token=D2osNiGASs1rsrAqy6KawijTKyUjjZJY-DtMi4jfHZLCwOe1zzR0Hm6E4hOK5Ntd-Q5a7bgeQY7YkqwV21Hg5HCCgZ790ka3taUl_8Qb8MYq1hxOrs3ZPhdKLfrY_hQHVYPvRmGfmuJcDnZl85TL0r5FQ6bZ01DBr_zHNhZup8NUjXFq5yAhH5BiTc5QlPjhF_7LAYraR7tftD9mNnp36jg4TXikoB7r-7WRtaB06QrBl3oTV6UqI1CfgTfCN3KNOCLaMueyyhQtLvR5HWj-pN_ev33BtoNKEjtpqEIUdGkrI3iDO9WifxNoHCCwaK61pBNxtpiSShGgbfRv2w0drw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی ساخته‌شده با هوش مصنوعی؛ هشدار درباره یک اشتباه کوچک اما مرگبار در اتاق MRI
🔹
رعایت قوانین اتاق MRI حیاتی است؛ کشش مغناطیسی بسیار خطرناک است و یک اشتباه کوچک می‌تواند پشیمانی دائمی به بار آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688653" target="_blank">📅 09:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b44744a09.mp4?token=OKPUqMUDBlIz1z_hLXyXp16kei46O-chp7DrIXqLmNrpEI0H7KNwOGZsy8Lnq-LYgKLCSmNEdEXlRikwBGMfnrenjKnfTtSqr_Y3gji9EeHzDNSUV4wiiQnv70PV0j3dBERZXohFiL6v6Nphnlij4mDXmPgBL1rSYiblC2VwXsYODvMIm_rCqHTXjQD9cvHCXnGqqc136K_qOxNjDyc3aqc8bS8uoT4rUIprIUXS1Qjplx97M3n-8fK4qKlhRWskPUQkqX6DN_Alo-PozO98D7Lu_QJKuUSsOcmS8BjB-AhrxNI6rXE9qzr3rk2RqXBseshWzOQzv8fsI0nCwyL8bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b44744a09.mp4?token=OKPUqMUDBlIz1z_hLXyXp16kei46O-chp7DrIXqLmNrpEI0H7KNwOGZsy8Lnq-LYgKLCSmNEdEXlRikwBGMfnrenjKnfTtSqr_Y3gji9EeHzDNSUV4wiiQnv70PV0j3dBERZXohFiL6v6Nphnlij4mDXmPgBL1rSYiblC2VwXsYODvMIm_rCqHTXjQD9cvHCXnGqqc136K_qOxNjDyc3aqc8bS8uoT4rUIprIUXS1Qjplx97M3n-8fK4qKlhRWskPUQkqX6DN_Alo-PozO98D7Lu_QJKuUSsOcmS8BjB-AhrxNI6rXE9qzr3rk2RqXBseshWzOQzv8fsI0nCwyL8bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشم بی‌سابقه رابرت دنیرو بازیگر مطرح هالیوودی علیه ترامپ: ترامپ یه آدم بی‌عرضه، پست و حقیره، اون نباید به چنین جایگاهی می‌رسید؛ این دلقک مایه شرمساری آمریکاست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/688652" target="_blank">📅 09:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpyeeCKIj_91MlnYPbw8aEuyiWB887Ll4peT9IPkHjy9r6b7UBnDki2XbwYap8kpfc40OlyRCMhDrhbIzeT4A7RFF705ZMdhxoXlKc-VampOrsP_yBRCbFdwTpy3Z9Xy4-MYszu-efFgvt1ggXPMOcdCCMIgf1L8TLJKey0v966aUvZqwtHNc3JSjflRjD53S2IyUjA_2lYU2X08pHEA2GhRT35xPaqXTXyAyHoqqcniV90vXP8lzPTHrtMQDoYUCtBnuIyT9A6XEnHWqyvf74p3Mr7LM4l-i37XU0tihuaTxfsgxfSLLvav30eN6eeF0D6zYx4QLjE5xAJdA11exA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین زمان برای جذب هر ویتامین چه زمانی‌ست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688651" target="_blank">📅 09:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مشاوران ترامپ هشدار داده‌اند جنگ با ایران ممکن است تا پس از ژانویه ۲۰۲۹ ادامه یابد
🔹
ترامپ در محافل خصوصی خواستار پایان سریع جنگ است.
🔹
مقام‌های آمریکایی نگران بازسازی ذخایر نظامی ایران هستند، ونس و روبیو درباره ادامه مقاومت ایران در برابر فشار اقتصادی بحث کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/688650" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPkCThE2liePz3CWIvxd1wJo8mGkxjMp4bQev5avQl8SAQVjgyBYcyJo69l6ZmGTO0nvA9_OSPyfbDBYmD1x1Kn2hrrQZv1rq0Fluvhi5N6Du8DiebSAeeXnQ-WP1rs5Nux-RMuaMWJp2XNIwrRRxZeoQy_zXiWuF8CipxU8t4aY5yuGDdfmwbpJYMJMahpbW2dUYQqpCdhh82tLLwmxwCOUCMUDLb_mXqAmmYYLfWZ4GI2g6bzWEpLUP2cu3nQX39226Z9zkqKHIjQb74b5Og55DEVxJSqfBvHsYQlLAKt_QQMxLtQDmnohu9RKIO9YZZloiixy-J4qhsr65guCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/688649" target="_blank">📅 09:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اگر ترامپ و نتانیاهو پیروز شوند چه می‌شود؟
توماس فریدمن، تحلیلگر نیویورک‌تایمز:
🔹
پیروزی نتانیاهو: تضعیف دموکراسی اسرائیل، الحاق کرانه باختری و غزه، پاکسازی قومی فلسطینیان و انزوای اسرائیل.
🔹
پیروزی آیزنکوت: اجرای طرح صلح ترامپ در غزه؛ حمایت ترامپ از نتانیاهو احمقانه است.
🔹
پیروزی جمهوری‌خواهان در میان‌دوره‌ای: ترامپ قدرتمندتر و جسورتر می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/688648" target="_blank">📅 09:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUiaboTN1KnfSD-ejZdwPlw4BGTVtEveTPzR7y11rjhr9JNVat5n9GCclk3ZGNANlKz1x_OvufKrjP_XCyQ0D5cXMDjjajJaRwoTeUP2LrGxX9ZsB-orncb4JJPjhsMtlRC595Nh99Z8TARbSHfrtFTvQnqEEBAJJEovRhZ23Tl_7V6hHehS7z-zM9wPMfF-PMD6b-S7uAkbf2g0QIwpWdg9s9eh5bqvwVqdeV3IuSKL8b6XDORpSI-JP7IoCa9bbJIhB3eaJHVhJDQrHJQBaBwLz4j5Kwl8Xd4UuYGwvoWdHronqMJmy5CTuSEEJESjuY7X6dK6BD_mgYTtvEoCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtQkoMY3okcHHOLIF3iXVh7GQj9DUtgRmqVC5MEWsoRnMxlSX8ykm2xmORIKYiA83K0Pu4p8lzzKyZZotf_y97ZFkW4DsgWyS7vG5snFbH84hmfW1sCNbwmkTHsCjH4i3CzxxhuKKIwhB0znZFxq3GiWzp0VUguSWbwBVqQHZvVwYhROG9ns0gKHLsHfVhsfkz_bbtxxbfTtwt1cHRVHQkn4YXyJwE0z8J66BzCi4_afWG6KmKdxgqrKjeO7PFyL9OGGNOf81B2S-89uEcVSzp7fV76xCuTnqSzzVwXpMaX_0Zi1yaQ1nb_zMDqducYAsLN7HgXUDfleH17dO46yxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کاربران اینترنت اپل را متهم کردند که در تبلیغات آیفون Duo انگشتانی «به‌طرز عجیبی بلند» فتوشاپ کرده تا این گوشی تاشوی بزرگ را راحت‌تر برای نگه‌داشتن با یک دست نشان دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/688646" target="_blank">📅 08:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d8915dfe.mp4?token=oqzy59820G-8q9MsjS5ds2sMPsat2QPXY46A67WyY5SFC-vzMGjDkfrNUQeYfGH_Et-4DfftaaatHCCz77zKGl6NhrC-OeddNoCFvp7t39YENyiD32bzPZ4wiVbYNkbRyxdstQ1iukHrgmpogpyjSTmQXxpt_NprEBbpFPjnWUnhpaXljdPFeFZUSdnPCYfZlBH5licrZR1oC7GfiIBYPPwNYUv_g7mAEr7DxygsnHgwJa_WtpcETfY4bvPSWbB4Eo9R_wAocCTafxLYUG_HmxJrSPD-76CdidVQPOgW5B7hYMW2ek5YDwCgUHk_KfmV-U9SYPzxw6uN8pSFvdpSJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d8915dfe.mp4?token=oqzy59820G-8q9MsjS5ds2sMPsat2QPXY46A67WyY5SFC-vzMGjDkfrNUQeYfGH_Et-4DfftaaatHCCz77zKGl6NhrC-OeddNoCFvp7t39YENyiD32bzPZ4wiVbYNkbRyxdstQ1iukHrgmpogpyjSTmQXxpt_NprEBbpFPjnWUnhpaXljdPFeFZUSdnPCYfZlBH5licrZR1oC7GfiIBYPPwNYUv_g7mAEr7DxygsnHgwJa_WtpcETfY4bvPSWbB4Eo9R_wAocCTafxLYUG_HmxJrSPD-76CdidVQPOgW5B7hYMW2ek5YDwCgUHk_KfmV-U9SYPzxw6uN8pSFvdpSJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ۳ حرکت ساده فیزیوتراپی، عضلات ران‌ها و اطراف زانوها تقویت میشن و درد زانوها کمتر میشه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/688645" target="_blank">📅 08:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBuExWP4gh74q9xJPQ2vqe5tdyjMNgodT85eCOfFe7HrlJE_VeCiNi3zMTFLizidf-P6FecVd8e2JfBTeuEo1kL5m-7yUTEcIRI1LLYHf5reSXRVSNIJrpuEzFSTAh9pY6XpgnA2uJKZdzM8z5EyKtYujb7wElEMUgvSI3ozkcuu7Ue4Zz_n4hJZGk8mDtby_htB6eiRCV_WsntXnhFh6ywUtb37xefoLvNnr8RyRRK8-MPdNCIDcfUNMwtzZzM3F5sajFhmmkL37S8c5qbhGEl7B5AUqXQzyV-tc3U5db1RIA8TjMVL4wpqLp6MIx3f9X-G3vOitDz6MLXAo4_hgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دنی هایفونگ، خبرنگار آمریکایی و تحلیلگر حوزه ژئوپلیتیک: ایران تسلیم نمی‌شود و می‌تواند آمریکا را فرسوده کند؛ پس واشنگتن نمی‌تواند با چین هم بجنگد، مگر با توسل به سلاح هسته‌ای که آن هم نجاتش نمی‌دهد. ایران آمریکا را کیش‌ومات کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/688644" target="_blank">📅 08:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اعتراف وال استریت ژورنال: تلاش‌های اخیر ایران برای هدف قرار دادن ناوهای آمریکایی به موفقیت نزدیک‌تر شده است
بلومبرگ به نقل از روزنامه وال استریت ژورنال نوشت
🔹
ایران در این حملات از کلاهک‌های انفجاری هدایت‌پذیر استفاده کرده که امکان هدایت دقیق‌تر به سمت شناورهای هدف را فراهم می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/688643" target="_blank">📅 08:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای مضحک معاون رئیس‌جمهور آمریکا: ایران دیگر هیچ درآمدی از بخش انرژی ندارد
!
🔹
این در حالی است که تنها در ۱۱ روز نخست شهریور، بیش از یک میلیارد دلار ارز نفتی وارد ذخایر کشور شده و ایران با استفاده از ذخایر شناور و مسیرهای جایگزین، تحویل نفت به مشتریان را ادامه داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/688642" target="_blank">📅 08:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdaYkbmoPc-eHlp1ERygHFnxC9NVAN-6iWjpqFJmGqK2E6KcG63iNo2by9fnJLGVi5yom788zi4BnnNLy5vBz0a8by59u5-Zgjsw4LjFlUCuK5hkYVNRxFGpmgsLiIopKRFcl83itjVZOyVxdfVUp2cEMkt8OaaKKug0I55NTKosQDm-tFRuZX6CYiKcAozNryutn8GN2ynnTf_U5aVeFSFeEpEwR95fqMW_XMTF7eS_IsPUME-dlvp99MKn0wR8UvB7tqTbqoKSB8tAtUMrYzrjS5EJy8ESjGJ56HC7WCDhQpOkdmzEzWKW10IiSjt8aaUNyUIz6mCJGxtuaLwCJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3fcbcc589.mp4?token=pLHQoxby7M8MJWCpKOC2i3aMKgioN5XS9KV4TeegENQ5uYM9xSE46JAxA9YQIZmzNl-ixEwyRYiGAPDFnLjvZ9NV5qnwIxwbL6nrdjj7sC0UWihA_HTBf6JSidMorUfqcBfcSw0IM9qRuzwfk-9iPXuuVdXvKud7A86pqRv-V0n6CGXdaTE5JgvvxSmltzwyER1lbapquaYUsoM1JnIxAG9dMVDrAJg-gfAFb_ZZgg2k25KVDBRHOvInA0LsNeRLUmREaUSdTTDw78F7-3a3exNk3TnoyAwBBqm_dTtNXmmfmbkF-pLoEu5NLiCwkirjmccb-T4UC2gR22hDB01Wkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3fcbcc589.mp4?token=pLHQoxby7M8MJWCpKOC2i3aMKgioN5XS9KV4TeegENQ5uYM9xSE46JAxA9YQIZmzNl-ixEwyRYiGAPDFnLjvZ9NV5qnwIxwbL6nrdjj7sC0UWihA_HTBf6JSidMorUfqcBfcSw0IM9qRuzwfk-9iPXuuVdXvKud7A86pqRv-V0n6CGXdaTE5JgvvxSmltzwyER1lbapquaYUsoM1JnIxAG9dMVDrAJg-gfAFb_ZZgg2k25KVDBRHOvInA0LsNeRLUmREaUSdTTDw78F7-3a3exNk3TnoyAwBBqm_dTtNXmmfmbkF-pLoEu5NLiCwkirjmccb-T4UC2gR22hDB01Wkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی نیروهای انصارالله پس از پیروزی در شهر حیس در جبهه الحدیده
🔹
نیروهای مسلح یمن در ادامه پیشروی‌های خود در جبهه ساحل غربی، موفق شدند کنترل کامل سواحل شهر راهبردی «المخا» را به دست بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/688640" target="_blank">📅 08:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فیلم لحظه اصابت موشک ایرانی به داخل پایگاه آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/688639" target="_blank">📅 08:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69e3d01dd.mp4?token=pIzpU_kmZrNcW3ZBoyP-rKVCENAKizkTVcPbiq1yVSHKtMuJ4KtthumSBFU8J7Wzaxy7SQngKnhgH4SmBoLgVolBM16oyfgUxAgHQrHVVw_kDkH9HreIG-AUoOiKXbzA91w7TWdxZzJZxRo10py7kZE7QZESSFoPFHq3E0zHj70spe2tbOui3PaHtFjUFaZ6bMggjfnLXeNzvkNLlIl8xmpRP6SnINaee3RuXn4hyUQX-tyAYcjsiaZqZiOUQ27Au-KguxW5BnoHIe6plVxIJRNZp0u5DqFx5z28cthjadU-nQ4Q8WqoIOfKYPKwy-4QSoE2g15-6kOHBP-VpkqQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69e3d01dd.mp4?token=pIzpU_kmZrNcW3ZBoyP-rKVCENAKizkTVcPbiq1yVSHKtMuJ4KtthumSBFU8J7Wzaxy7SQngKnhgH4SmBoLgVolBM16oyfgUxAgHQrHVVw_kDkH9HreIG-AUoOiKXbzA91w7TWdxZzJZxRo10py7kZE7QZESSFoPFHq3E0zHj70spe2tbOui3PaHtFjUFaZ6bMggjfnLXeNzvkNLlIl8xmpRP6SnINaee3RuXn4hyUQX-tyAYcjsiaZqZiOUQ27Au-KguxW5BnoHIe6plVxIJRNZp0u5DqFx5z28cthjadU-nQ4Q8WqoIOfKYPKwy-4QSoE2g15-6kOHBP-VpkqQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همدلی مردم در تهیه موتور برای پیک آسیب‌دیده
🔹
در پی آتش گرفتن موتور یک پیک، مردم ضمن حضور در محل در حال جمع آوری کمک برای خرید موتور برای فرد آسیب دیده هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/688638" target="_blank">📅 08:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ متوهم: ما دقیقا می‌دانیم در «کوه کلنگ» چه می‌گذرد و فعالیت‌هایی را در این سایت رصد کرده‌ایم/ ممکن است ناچار به هدف قرار دادن این مکان شویم
‎
🔹
ایران در حال فروپاشی است و برای دهه‌ها قلدر خاورمیانه بود اما اکنون دیگر این‌طور نیست.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/688637" target="_blank">📅 08:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1pvjQGlBtPt9Ck4QvPY0MdunP4u4G-xFGuRJusqm9KFh-cNfZDeVGkcW3G5lHtc2Lab2Sfx0dv7zjJ_S_AbNn5gS1dDQZfaA3c8nPu6FB2XDdNDn116aBUe3yNwsh0efa0GF-M9ARZboR4Lbz1oiGEcy42hm3kQwMlum6aY0FIexnbXodHHzDdgC7i_gGoMvEzliq5i8X8O6c-kgAJ6yUeCBcSJ1BoIICbqK3bjb0Z4BB82bVYclx5UyUzPXqe4_Kx5T2t4AUBDOpLxBg6EfArVg-I9O4B20-uSOP1qq8TbMzwFbaGKaBxxieScoJJDQFgNl8QygIWUZ4uohZllcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۹ شهریور ماه
۲۸ ربیع‌الأول ۱۴۴۸
۱۰ سپتامبر ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/688636" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688635">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PndlNtsusGrdxEoQPDSzA44BNMaNz0DibPoCe4FxmgazNftHegrhkVcQn22VgTuu1xxu5H-_RoQF1LQZNh-mup25FDxB66x9hkTePQM54PcsgCTkhKHhW-UeIa_NZNzqjb5Us3O3K4X5ZAZdOlzrbY1oR6M9fI-WwGTfiS9YXNvRdnqOp3opcPPgwby4nQhYdWlWZFyoCg1N5HRNueABv5UJOI-cve1T5bhWy7q4_mglVuQ1UyDoyDNql77PpfzpUuxht_7I6sN4yZKL6sJuVHq_Jd-agQBcQs5Z6dbMxs6s4tcotthYCLougDqTXKW58huwdZmTofu0BVLI1px7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
اگه می خواید زود تر از همه از اخبار خودرو خبردار بشین حتما کانال تلگرام آخرین خودرو دنبال کنید
🔹
قیمت روز خودرو
🔹
شرایط فروش خودرو
🔹
مقالات فنی و آموزشی
🔹
اخبار خودروهای وارداتی
🔹
تست و بررسی خودرو
🔹
تست و بررسی موتورسیکلت
🔴
کانال تلگرام آخرین خودرو را دنبال کنید
👇
👇
@akharin_khodro
@akharin_khodro
@akharin_khodro</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/688635" target="_blank">📅 02:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688634">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DijCN1OBtXZdW_ctw5sVuuqB8RPo8AbvYoOeSeUe8ZZcERKsuyEQ5VUiVy3zHtV117fg6ayFbWOEJX6Gsu_I7bzDmo9MW8XyamFEHJ55hwCkx3q0y54m10b2Ag01IcMYODQA7pEFjAwbS7wwy8DWOR1cGqhuz6aCaIEoHvaYkyiDThCdmnWPNl--yIHthZg-eYiNxmaJLkHhawAp0r2H2mEJhUGAhUzdTT52zPoxyxPBYmsjxtXcPJTkFxu89k2VaLqgEb3880Jl3c2M11DLChGZFfRhmIKlbTMjhJJ3xY2mqbyU-3kS3FX9PDg-GU2o8kPD8-dQVo8L7VYDzDf3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله الرحمن الرحیم قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخْزِهِمْ وَ يَنصُرْكُمْ…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/688634" target="_blank">📅 02:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688633">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
برخی منابع عربی از وقوع دو انفجار در شهر طائف، عربستان سعودی خبردادند
🔹
برخی منابع عربی مدعی شدند، چندین انفجار پایگاه هوایی ملک‌فهد در عربستان سعودی را لرزاند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/688633" target="_blank">📅 01:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688632">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6ayMNmOIrS64N9jEiQO2qpJz6OeYBN8BJxgWE-dIvCgMt4TiyAJvPbNgQqRVtuIbwKPxUkttfOqCLtv7NkWge-XdtokqEFKnXD3p6sw-GCFw_eu4CWXp6JK7wBppz6w3pJVPz-T_dkWjxcGZ9WO2ItLN7PmlQEDl79lGySX74o0r9M1bK63Iiu1FWS2_fa7TFBL7O8uWzeHzfir6a_biiqp2dLBiAlCto2bpQwroMIKSPlIwCJwOr1L-nFc-D-SZRO1h9tpcb5N4ideasE6IPGXfQ1ME8s7PP9_Q_YzobY-ztbbqlU8jytQ-awsz10OmKg3TQj8GVNb1XEqOssOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: دروغ‌های وزیر خارجۀ آمریکا در رابطه با مداخلۀ ایران در موضوع یمن-عربستان، نمی‌تواند جای واقعیت‌ها را بگیرد
🔹
ادعای مداخله ایران در یمن دروغ است؛ انصارالله مستقل است، آمریکا با مداخلاتش منشأ ناامنی منطقه است؛ صلح‌خواهی یعنی پایان این مداخلات.
🔹
صلح یمن فقط با مذاکره ممکن است، نه با بمب و فشار.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/akhbarefori/688632" target="_blank">📅 01:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688630">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرنگار صدا و سیما:  شنیده‌شدن صدای انفجار در قشم  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/688630" target="_blank">📅 00:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688629">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
خبرنگار صدا و سیما:
شنیده‌شدن صدای انفجار در قشم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/akhbarefori/688629" target="_blank">📅 00:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688628">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5RU9CL4Hi1lGO8sCyA1jqAgEZ2H0BAcHfnK25kfVDjqAXw7eP2jQr5fV1kDz6hMNHP1IQi8DUDskye8xO73RiAThwdA0xyLLzv1sPGt46T0we7Jsd_mAKP6wO28SC6tF0qvFD4AcB4WtOGtb0KjHtIs0cdt-n5_lr-irxEROmS1Gs6KZ0d8xduqND7yTh2-6uG8QohMcIKwPK1xSrI0jQrTMjUgh4h3Xt2NqzJc4K6oqvA2YE9z-VB81spy9c8oQlhdEuoxN1UGTCLc7J3eXu4-boeIGYASGfOGMT9XHd1rEWJAH6LCJZ7uqLsnCp-JSUAFCgng5OQqlri1NUZY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
اگه می خواید زود تر از همه از اخبار خودرو خبردار بشین حتما کانال تلگرام آخرین خودرو دنبال کنید
🔹
قیمت روز خودرو
🔹
شرایط فروش خودرو
🔹
مقالات فنی و آموزشی
🔹
اخبار خودروهای وارداتی
🔹
تست و بررسی خودرو
🔹
تست و بررسی موتورسیکلت
🔴
کانال تلگرام آخرین خودرو را دنبال کنید
👇
👇
@akharin_khodro
@akharin_khodro
@akharin_khodro</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/688628" target="_blank">📅 00:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688627">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f24ae6b8.mp4?token=AlqCU0DrURoxpHV-ilfxlkQYWvNbFnyGLP6Q34f63StQt0XIDvjgbyRPGRvkGA6kb_UMMWcUA2VHsqsMfZteEyQ_b-HSIOtY4aRnAktfCgJ7j8Guv3MsSUJAiIv_VBlPI1ee32F3aesBvr8RXEEhDjY9eiWw05pnJBVHsmrJkl_5VKMdBB43U6AnNAZH7RLo6j95SlJZZg-dK9YtEiIwP9R45ILg0jlacUuUrVW3ZNvnG4Ur2xbsmsaMJw-qmGwcoEvVRTdjXu09QV8S9dZT4EqhTbvFmQtVm9rSzpgvmifQqKnaTnOjuUzuaK_ezk08hlsMR596SZAlvxYqcKHeDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f24ae6b8.mp4?token=AlqCU0DrURoxpHV-ilfxlkQYWvNbFnyGLP6Q34f63StQt0XIDvjgbyRPGRvkGA6kb_UMMWcUA2VHsqsMfZteEyQ_b-HSIOtY4aRnAktfCgJ7j8Guv3MsSUJAiIv_VBlPI1ee32F3aesBvr8RXEEhDjY9eiWw05pnJBVHsmrJkl_5VKMdBB43U6AnNAZH7RLo6j95SlJZZg-dK9YtEiIwP9R45ILg0jlacUuUrVW3ZNvnG4Ur2xbsmsaMJw-qmGwcoEvVRTdjXu09QV8S9dZT4EqhTbvFmQtVm9rSzpgvmifQqKnaTnOjuUzuaK_ezk08hlsMR596SZAlvxYqcKHeDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
☀️
چراغ شارژی خورشیدی تاشو
✅
شارژ با خورشید و USB
✅
نوردهی قوی | کم‌جا و کاربردی
🏠
مناسب خانه، خودرو، سفر و مواقع اضطراری
🔥
قیمت ویژه: 1,098,000 تومان
⏳
تخفیف محدود
🛒
خرید
👇
https://memarket24.ir/product/brief/47540/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/akhbarefori/688627" target="_blank">📅 00:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688626">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vogoRf2tpQKL_ADVuCSfFdok0remTtb14TDSQ3V5ZuFVE9ep-2mFQbGECE0vgPDe3lCkiobGnsDjQtpQHw2eydRIladvAkLHvLVt05lBHTCsGxermmrh4xlSCzMk-V7krD59jBa8bXJSjlO3hKU_exY59c5WFiXNZp4qfUcxLRivpOBgdomQtmwNmjZH_LE1ImnFMLB7AT2IOhidR298mb5vDTfBacRXZ-1lKbP3tJaIifoh_TvFcDtwR98d0rVH2WF-ml8hGnqjSHlyte-5HqG_BH_p7R9ki6rJT6lU90N3r4qh_Nre2VhyqvPHyJ_KDUg7bF3SEtBrtTUgeEm9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه جهان زیر ذره‌بین؛ اندازه واقعی کشورها چه تفاوتی دارد؟
🔹
سازمان‌ ملل دیروز با ۱۶۴ رأی موافق در برابر ۱ رأی مخالف تصویب کرد که نقشه مرکاتور کنار گذاشته شود و از نقشه "Equal Earth" استفاده شود که سایز واقعی کشورها را نشان می‌دهد. سال‌ها آمریکا، کانادا، روسیه و گرینلند بزرگ‌تر از اندازه واقعی نشان داده می‌شدند
🔹
آبی تیره: اندازه واقعی کشورها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/688626" target="_blank">📅 00:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688625">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNcwx9TaEXSxmP0Ej4shG05OYbYOwJjnLfw0cfi9m-kKaPGjhkV6nxOHVBi4lLcVoGyUovJevWZO0QFqPpFgcE0t6FykqYtKfJ9LqU1R1qXPL9Oiyv4BbLsBl7NPbQ6ECn78BHTg-i5e7MMO6i3BDEIYfsxUNPcVBHEtGY_ZXTOGB4YVhqDUxJmdKQu6jbtU2tzpacpDRVb0tVY9Xh6Xq5OtR5mJn9mZlUkIjMCY8Ls7YEl4Nog0GvejPejBWER-Zc4XazkiXBXhqX2RpYIoovkATFF8m4TpE4-KLYk1swpxvCOxIjVD28XMkTDuy7sWqW1sP2HuRyCHBAJQOIinkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارزار محاکمه حسن روحانی به ۳۵۰ هزار امضا رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/688625" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688620">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0fknHfJwp_etZjqTZwjcBlvs1Ee0WWGQa_z8WYfWuYmHphQywYSiKfafuWCxOp7UcmM3P_MjhpX9p1pTIVKxW1jEQEA4mppZUWTo69HkvR7YARFS6DaqHmXFsW0Q0dA6XLxdl2Sd7JMgbwfPHKvz-STtqkWFN58FPsbp3S_jCbtTrg4fYyp5QDWfRW1TGHif-e2AyJWZ6umuuNgDlbrSz8D1Sse3d8kuOTDj9NXbbJhE49Avw_VbuZsDpY3y1SsuXj-xLRfv56l3bUAJ1sRjtbWqRZyHIbKxDecfmG87Ws4DhZ-9QFXPCtrD4Y20Q8kqWqUOvORzj7rdeYDjIoPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmsyttRc3GvYbiw_mtj_A6y2qzlMTb5MsRTwsg3rNy8V8TLWGmQL620ZrxxG-QYwo-4Py8aPx2gtmGE8XHYrJiJYFcpmvkAzyH2wz7Yjbb9nqEMUG19GMXllkZHyuRxcs714V-g91lR4QhBX5W36MaUt520ZbMcGJ_pLS7GdJ4yNpqn5waz8f1m7CI-9lYGqbq6-sRFOVM0JCi5K8USD4leveeOvF5ID_1qD9CpOvUmikO7SgNpxIBkErj61S8oeBhKBfzqxNvhluXj1ha-Snl0cwhhyfDklWy2rzcrW1Gu43Av8J4iBxPTJfVi7KSs1z4dCxnSeazIhp3pgJ-Yvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbz98HbDrcxlOvIiGuY3N6A2s13A5jziS9_ZsNlriTaHj_h5E3NHaYH1C3AL-lnALsWDtPd8m5eUVyuNZ0TwtIYiKyi2lCKkfKRXxj3xgG_Zg38wtoWDeWUzulrcPiodZdYlnKcYblmS2tnk7D0v-hXVseFmMD7M8KLOIMiexkhnj0XRt1oh_KAsyzMW40nX8J_yA3qNy2K-itxbtqOfhRHtlh4-qUo1ks_Wcvp00DsQ0GLG5773VkqKiK40RB8SRy7AaDNTqnlFf-LaSMCvCLEZnnInQ-tdktNoUlmMOeL7hOKPjKfoiuOBZeRuawJe74DYarF9y2uvxa7mij0JdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886e88ad32.mp4?token=eoWElysTO4uRIn_GZRiOttQLdLgeE-Jhvoj4ceDYXunTNolScQBbQzWfwX50w9knpA_vafZOL81AUCSjb3kVzTbmGbcSmVROUyfcbH0SHULuUWCD8lSYFaDrYYvjPnLgO6yHmzZwdDfwLZxuVROFh9rVW9qGIR6b0YJT4z0ZT0dxNuYUHyz20jMqb_rD0V6fE1ClXg6a-AokYbhjQ-TBgyBH_AvimHsKSOvIdVZidQDWNgVqdlbvV6_BATffZan9hkSqHPZp2qIT6jCjjf6fj9wHp8j5V28jfvme81XfER8hV2IQIkdRz3Na7UQBjJznmJIFbIntZc2HwCXGyN1PlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886e88ad32.mp4?token=eoWElysTO4uRIn_GZRiOttQLdLgeE-Jhvoj4ceDYXunTNolScQBbQzWfwX50w9knpA_vafZOL81AUCSjb3kVzTbmGbcSmVROUyfcbH0SHULuUWCD8lSYFaDrYYvjPnLgO6yHmzZwdDfwLZxuVROFh9rVW9qGIR6b0YJT4z0ZT0dxNuYUHyz20jMqb_rD0V6fE1ClXg6a-AokYbhjQ-TBgyBH_AvimHsKSOvIdVZidQDWNgVqdlbvV6_BATffZan9hkSqHPZp2qIT6jCjjf6fj9wHp8j5V28jfvme81XfER8hV2IQIkdRz3Na7UQBjJznmJIFbIntZc2HwCXGyN1PlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از آتش‌سوزی‌های گسترده در تأسیسات آرامکو در حمله اخیر ارتش یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/688620" target="_blank">📅 00:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688619">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJBfYE1vI4_0say3tYnXY5l6l-ZAYWdjPfbl68QURYGF0eDsNUm0aqGEEYUxBj9t774p3MFCEsTzUgyT547WBZIDBZhOOy4z4hMeim9ohTvsQ6XgoaAPIfQ_CheigMCiY9SoZkblqu3Iki5ZDIxxpoJx-M2GjhxgZ2nKoRDAYd5r8IMwsYVXklTX6RC6KSXDPCYE9YFzBqY681Bbob5k6LbqETAPrqMfCFx24nj8p-Y4yZb9cEG_f5vuFfejkROKkTcEeOCScyOLHD5tdaeKXIsmPJThfheabsy62iFTp7kAInIvUpzxiPNNbfqzAhOByFYJNnQqD-jxCaifowh21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688619" target="_blank">📅 00:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688618">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dV6vjvnIkqORTLpBlEoNXrJ94xU4R15va7LbFUdH7KK0e0iVQ9xBPoFFVUETsFiEpii-GtP9IyFeeYImx77o3p91Eys_HOBICYx2pdbOWrGaukJy0Ym82IX7a8qyY2eVR-Rh5YUR4XQi-0PdNfT7Mkj7VyIDTDhuZFt_DGJKaJcfLL2RFiXMQ2RbS4lnLhdycLe63aX_MtAqBvCWFpnZxA9RMGvNuxSglHCVccgg2elgTsRpbHxAiSxKCc6qrsL_6_T2roLSti2-DZOpsSgWa-IVrQaS_xL2B39htGEexbP5pwoE1wdoY9gQZ-Oo4ZZX2onmljrQbJCTXptUagiSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: ادعاهای مطرح‌ شده در بیانیه اتحادیه عرب، مغایر با واقعیت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/688618" target="_blank">📅 23:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311a64f078.mp4?token=dD3KDqogtb0nHg6aKnEW2oMDolGC2qVCDcNNAu5tL9XnuBAM_4KmQKYsdca0hgfTnlyMuq3MQZ9yiMrXvh5NrDLI_SoFN9YFcxo654wwe0vtiA7VS0Dr4G1n0O-H4kTYWcixOgmItMPgkPNsFxwfDkzWQF8Pz7dm5KuwCuGxndN1tQ5bf1uUO3lj-0xfTWlhrS39kKkwTSffdyuiK9VUbp9iRmV5BRDeeAE1wKTu1vSnJn-Ai3LqFo0HONYJ9ezTIAH8kzIbcj7S4fjdXQS9sW7FqHg96TfBxiZtXkZeEdbdnstqKE6C06rMKndTMERpZS7ITuDMeHKanWAWSJuAjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311a64f078.mp4?token=dD3KDqogtb0nHg6aKnEW2oMDolGC2qVCDcNNAu5tL9XnuBAM_4KmQKYsdca0hgfTnlyMuq3MQZ9yiMrXvh5NrDLI_SoFN9YFcxo654wwe0vtiA7VS0Dr4G1n0O-H4kTYWcixOgmItMPgkPNsFxwfDkzWQF8Pz7dm5KuwCuGxndN1tQ5bf1uUO3lj-0xfTWlhrS39kKkwTSffdyuiK9VUbp9iRmV5BRDeeAE1wKTu1vSnJn-Ai3LqFo0HONYJ9ezTIAH8kzIbcj7S4fjdXQS9sW7FqHg96TfBxiZtXkZeEdbdnstqKE6C06rMKndTMERpZS7ITuDMeHKanWAWSJuAjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عواملی که باعث میشه پوکی استخوان بگیریم
🦴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/688617" target="_blank">📅 23:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
به گزارش رسانه‌‌های نروژ، نخست‌ وزیر نروژ فاش کرد که هواپیمای حامل زلنسکی، رئیس‌‌جمهور اوکراین، هنگام خروج از مولداوی به مقصد اسلو، پایتخت نروژ، تقریباً مورد اصابت یک موشک قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/688616" target="_blank">📅 23:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed923131c.mp4?token=jljcEMO7WeJ4Kr7KzfCvUs7Sqio10sAS8OE-58yJuw1aGE_LVx_zv4IOo-FpfvKHZJbKI_x9UuLMo90erfHe--4P1LU4CR1lDCbpfMNvC0zUKNiiqBitUiPEkMHK3DeZFcp-7c6qGXanKW_5b8u0NKWZ7W1XVtOUyCVJYWZxYCk8tvEZq5fB5kfUhYLChn0fPrybL7-fbSa7GJKHX7WxiILvN40ydImHy_xQqlsbdVEI1a7KUeOsO-6oBCGC_Ux8o0lQEhhRpe7ium2MByevAN1JVUHRZlmYmRQfySpxJyu6ogv5r478nb_lAh-GAYT7PWX58gab3X3fbSYP0lIPLrVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed923131c.mp4?token=jljcEMO7WeJ4Kr7KzfCvUs7Sqio10sAS8OE-58yJuw1aGE_LVx_zv4IOo-FpfvKHZJbKI_x9UuLMo90erfHe--4P1LU4CR1lDCbpfMNvC0zUKNiiqBitUiPEkMHK3DeZFcp-7c6qGXanKW_5b8u0NKWZ7W1XVtOUyCVJYWZxYCk8tvEZq5fB5kfUhYLChn0fPrybL7-fbSa7GJKHX7WxiILvN40ydImHy_xQqlsbdVEI1a7KUeOsO-6oBCGC_Ux8o0lQEhhRpe7ium2MByevAN1JVUHRZlmYmRQfySpxJyu6ogv5r478nb_lAh-GAYT7PWX58gab3X3fbSYP0lIPLrVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کارشناس سیاسی: ایران می‌تواند ۲۴ ساعته به سلاح تاکتیکی هسته‌ای دست یابد!
حسین کنعانی‌مقدم:
🔹
چنانچه فتوای فرمانده معظم کل قوا درباره دست‌یابی به سلاح تاکتیکی هسته‌ای صادر شود، قول می‌دهم صرف ۲۴ ساعت به این سلاح دست پیدا کنیم.
🔹
باید آماده حملات هسته‌ای علیه کشور باشیم و سطح بازدارندگی هسته‌ای را ارتقا دهیم./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/688615" target="_blank">📅 23:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6755e56c8c.mp4?token=mo8As7Au08yQ-cbbaH9Wn3u2D817VzQBOg8OtIeB_5eabnHe9_pV5Nl-oL0yicT4wKxj6jDJhqj1I0I6_HqJ5sWgYCKjf2f5Gux7phlDsICbn1LVNymoThBGrO3APhj8n8QBI8C2ZaAeZTEW2hjxYylcvJzzEdx3wr3ely6EUqG8fiQdJwDjCDuU1pAb-nTY85QLy0gUrdkpQY7vr-Aucez_yfOUO8ATPXcEbOHCyozOjJMrc3gh73Aopb325lVuXkcxSW6Q7_M4AQb7-maAxF2aDWPJlUDuV72CwPJusFppZoCSTHAIz0ck_2Qc38lbVVwq8ngSWr6TUFRErCbAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6755e56c8c.mp4?token=mo8As7Au08yQ-cbbaH9Wn3u2D817VzQBOg8OtIeB_5eabnHe9_pV5Nl-oL0yicT4wKxj6jDJhqj1I0I6_HqJ5sWgYCKjf2f5Gux7phlDsICbn1LVNymoThBGrO3APhj8n8QBI8C2ZaAeZTEW2hjxYylcvJzzEdx3wr3ely6EUqG8fiQdJwDjCDuU1pAb-nTY85QLy0gUrdkpQY7vr-Aucez_yfOUO8ATPXcEbOHCyozOjJMrc3gh73Aopb325lVuXkcxSW6Q7_M4AQb7-maAxF2aDWPJlUDuV72CwPJusFppZoCSTHAIz0ck_2Qc38lbVVwq8ngSWr6TUFRErCbAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: شما گفتید که قیمت‌های نفت و گاز قرار است کاهش پیدا کند. نفت حالا دوباره بالای ۱۰۰ دلار است. این را چگونه برای آمریکایی‌ها توضیح می‌دهید؟
ترامپ:
🔹
توضیح دادنش به آمریکایی‌ها خیلی ساده است؛ فقط کافی است بگویید، آیا اجازه می‌دهید ایران به سلاح هسته‌ای دست پیدا کند؟ پاسخ خیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/688614" target="_blank">📅 23:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مدیرعامل انجمن عفاف و حجاب: گرانی چادر به دلیل گرانی دلار است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/688613" target="_blank">📅 23:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ1JkfLGpegWdeYYXlf5PlK7KlfyUPxNkNwvtWw7QsQHKoh0ERtf4PdSlVIpm_nL-hM6HZck68lO0X4XSpeEFWdk_WIbhswZ2336hNjcNhEPIyoRCAE2sQ70kPD8deFDAbChmr0Gg8lDYWXFXUxn8Hh4geBE0UHRdM6wmRkGWxM58p2Q9SgXYHOg3wOuj_x8XJ8aX3hNhge7DdSiQ6XHwfPEPab-1DU1dWD4wlbS3oSNo9b5yJV6u4ehwuwouvoehbGoTUAu8Qk3WkGrUJ2ra8nBbXoToNMBgY1kIbCuW6ynGHaSKkLLpUUPDzV8N6MRfaiOy8I7JOvp_J9VFVvtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cd23e0f9a.mp4?token=FdgPmDsparbYEAKdezJ_0DavoX9W1UoUkwVkc0D6QnwLfrYFuyzEDyAD97SzO72QNXTUqeULe_bzmySE3nUiPO8ibOyM-vWtBEq-B7WOA1AcgmmBzgB_n2UP8WefQDpxu34ZGZoZZoMq_QVmYWGmIIslAn3rtC44I_3LZuk0Ky48MoouPHrvPi6itrksLN3dO6dLiA_ApyFVaDyul8mS47avv1rvEmkzhUfXWY_UfWyET-uSKedsi22z1fo5Jgdi4XTiZVgS5P4ExItwUIyWmJEhBJqy9_3dqeCB68JF7CgfPabgBTYNFqL57egu99v7j2jzmhsidzmxuMLugkYwvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cd23e0f9a.mp4?token=FdgPmDsparbYEAKdezJ_0DavoX9W1UoUkwVkc0D6QnwLfrYFuyzEDyAD97SzO72QNXTUqeULe_bzmySE3nUiPO8ibOyM-vWtBEq-B7WOA1AcgmmBzgB_n2UP8WefQDpxu34ZGZoZZoMq_QVmYWGmIIslAn3rtC44I_3LZuk0Ky48MoouPHrvPi6itrksLN3dO6dLiA_ApyFVaDyul8mS47avv1rvEmkzhUfXWY_UfWyET-uSKedsi22z1fo5Jgdi4XTiZVgS5P4ExItwUIyWmJEhBJqy9_3dqeCB68JF7CgfPabgBTYNFqL57egu99v7j2jzmhsidzmxuMLugkYwvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار مزدوران سعودی از دو جبهه حیس و الخوخه در نزدیکی باب المندب پس از پیشروی‌های انصارالله/ فتح کامل باب المندب تا یک هفته دیگر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/688611" target="_blank">📅 23:14 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
