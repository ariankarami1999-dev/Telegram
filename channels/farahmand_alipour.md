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
<img src="https://cdn4.telesco.pe/file/odMzl87i0JB-7YA73nt40ciO9Ig1DWW51iGAkIV43D_yAOf5r4bNUu2FjGKox8OCbmHHoqiZFqRoAjYCieXhE9zkgveTET9MlrUJLI8siylCmQkQkOkRRE_Q_E4jwgv4cDm9Na-fiXBootKlb7XuL8y-v9wnOevkTSFi_xLMDeV_0Y5AC0ueTDaWZptx8TWjEH01C9wI_jexQ7XwK2Mr7Oh6k2xZceEc7IUKU1SFahxfF_oRtGR5BJpZKRaBvAzSLnxcuVVvQWxtITho8bqVJZnWZLd5IMa9M8Gf5bOBpXKm9hF7lONBrS9NEh_bUmkuCK1AJGHkTyjpItX4Z3_9RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQwgQB6MUx0AvbGDorc-79rjQrwJHYO5L2YVPTKQKvKGyayw4wlBIXlIanEw3WGHi4ZwVhE_thfstHPg6Olx5bICucdDUgxEhseKg06V3FnYtYj1O5l-GftaXl3CD2-UyG76i9XKt8Qmq0iazv0sGeE5WQelcbMM3GTDvry7BEwQFA5Yt_mS2LPyKezM0N4YZIAa_8SAjzIbLBl2EbaVHHt2srOuNsKyLF2tuHjFnJCh9zRNv4l8M-_MySV4DoRyqqMQVFlDFHtJf-BSsO2VfcJno2TeEEnJYYa5Qu2irTFqsuMtu2adqi7x1TTB-O1BROejfh6Frmgt-hISHXJ1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTTn2Jj5KHYC8RLPb7aSDcF7aqG47R2kW2DF3V7v-9m7DaBht_hyBNl9WPUBJf7YyerXh4p2OOb1cN0EVIUoaET879xoy__e6LPKXUA0E25e0ANmOe9TnrDyvpIl9D3AhS2_VtxMmWf7sDb_M5sLOK0jw7NOB9WDd0RRSl9ODLNiFhREAf_CPypjoaPObs7MeN_btAZGc9KO3gn3GQgxNZhHTKVDObS4q9XAAnHMnzyhUdcVVfphlFPuWB8HAYrsZrsCNeGm52Ie-0keLZTspsXtnXK3KUAmMT3zuufxAk7xyrhsfCLd16_6id4FbnjqujrlyWD8wDL6S8lmA0nnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G70VWaEQBxEcwvi6rMCkkJkWeBJEL-Sea-H_bxf_OaL6VbGpp4fQro_LKrkZa8YgoVrRFkGvP-8yOUQXNV16KJHxP_vt9lexm_oXzl7bHCqq8yBcpUP2DzgTKbSPYHXy0frysoE7i8ZD28QGx2r9uTM_Btq_YpsJjYxxxrq3POQIzPv_g3tBkg9TYFJy_QKztMLTE4ss50teG6qCRolBe8v3-qYpeHE5YU-oTwniFUdTpyzxpAIo5ISJjdoCo0wfXlFkfLtZ12EfFtk5aRrMV_1eDhJtctJEkE1SjQbtvJp3mIfD3WXV1txD-W82lHgK-qRzI1XYcDY9HIX4C1Uzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsto6SnBp_pi60gd21bENs2IPfIOgAbWrPCJxtlRTSApICc1zggjF2Y7MByxAXnkx-u3Ys4YWQDZJEii0f_W4GiD1gIShvgzQqrWwBi_ppkRxeXGbGQQP-jXFv5gWZHppGrmiYpimg2XruhykZrDYNvPAzZVBxd2W0z3nvJ0a-8jnGD8QabSlnP-HtHnCAO_pT6EvWbCFCvh-3NqcoPUSOa7jIXbGe1oKXInunZLwy8XLj4giZKn8hlNaYB19MARHMygRn0Dwwxf8xXBucL7kyGhFuNHgRvp4ATh-7zPqXJJAuRhPhWIT3UiKMHVTkzY3h6ZSh-4AO2LFZl74ZP4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0h3gujJfP6Y1yvTQ9jplx8LCvqNyLo3cMaIzKL2accxpgIlYI2LgbwoBiq15taX-0w1jDeiRE50CSTvwyyI_7yv7CXL8HEDwQ37lBa4dwSWgmNHPyEtoz-U7OBQIbrrkYvZdmOG2reLJ2oLeGnQFoAclY7F6mFey79KrGpSVfCYqooILX3U45Tck6E-zDo3siaG7epYa6sG3hiJkpB3bA5-mcpniDWh5kFPeC6JX8RS3bLgJFTfgiGu2N5MDscx__ILu9NNezDt4qxALNuGedsw6idyvBBHUghi5PhUV3qiQGXoqKXBXGaSQlTaZFHNW3ml7G4IFWbN-ZFbxHQc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMIuzHJp8QYZ-tuQQyQLvdF4D6ZcQYZGKh5kUgNhm9XFYRA_mO6GU3df1qCyR8_kyZcbW0anC3Np_BSsRTxzMJlpES5wzqoHVy4RNJvHjJ4MEANUi0HocILgwr7f68jcEY3J06I8CRL_uaBVf8FeZhHDyDIeY0kwk6hhpeTdOKiLUeU4nf5kEiBRlbMFy5TS4KcE5_eDrjemdVi6gsoZTY0imyx2_4S6ZhnXngeGD07vH1h0U0aeeX_x76krlv6eAGg4j6Gt9f4ZIKFuG3Zs8EiPV0JuxmwTZeoIZx_-jPXA_-DRrKCEG3sQQTBBAbtKY2wBeLGuLWJ_QXyJKP30WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOXmMBzj1gtPL767RKTF92jto7e8cWxFLMPYeONe6lI3a-pCrmTnKv6xwd3pEhevMC2JuihD-WohScw13uRH7dUeNmWaNumzWTX7txVzRQwJEz2zpltW60D0soqLEdyGDXWhy1-ablGG6_-NBf3-SGSvf99KbId2ger4exy46K9K0S9lVfvyEwHVGRbenqpCEIchMhCMym4nfJZH488RaZJ7uzZ3YngmCs-laco3dyrDgC-W9zL1qjzA-x3h5jxzYVrkMry6XdUwmjVao5DlYuxLL3hZuU3BT0fb3U9IVsnp9fbbIUtZtxTCrEfX5eKvH3WYgvDpu53SN--vMjt9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdEsWjej7mEmokP6asnb70Lt2eFWtjPo6x3B0RDpKE3K8BG-b0l2gxTPg_69UilzAOcSJnlIdLe-RpPpiXx1FZ6vPYXpvD_9t85qIwAPJH-mkzZLrCkAUK50ab6J_XFDFb1ZA4yvGGwvUAP-OkjjMeVo_Qsjb3iaoOGyWpDpoGZFmJnZ9ZlH_yGs9wW-cZAckxJ4ZfkysTXzMXn3XVoD3DJmnguDyJLR-CJLwlY25ZcLQvePNkRkmie3-5va7GKsDCKlMmfe3l__k0wYkDLPvmdPVe4VusOdf6i3hdRs7wnq0jImOcY4jb-1jo-7YRSt3zED3k1pYz8lFrS59GFKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nW4uDwOybgmv7CGxBKQqpLCroTddtpw9ofUDU3OIIqexjMWTH38Lou50yPLMTY-AbGpoVj2Lv96ZmVE5gabnRpL5MFe6jOrhvuV6U9HkNYTfu7Ug5WxdSBs5m2MLhUA51Y9Pv4WT99hVJ2TJejAiE7aRKfyCiDWuusRaV-symHoaX6UG-prgERh-Wqkmvr-6AQy2KA-YRDDkXUTWMcHdYo9yiiXjdmRdpTJ6A_sB-lRTuMz9Ze5EucSNx7estd3ZeOUr_l5WHzcSqLnXmJXsNY73AoQJZN39sU0voCzaWDk76dH46e7tXIbesUzyNQl2QNiu9qjCocB-HvKk6oiPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVrth0LlkZyb1w3aJ56lbzqapAjdLBA85r80v6EUhFDMPuWHgXR3EwC20JdE6T1ZaaogkkyuN-673_fKsXkS6BTWN-teIeTI2C8HSSXNbAnBP_xXQ9XfEtmDOdMYc0inbys4SCLT5o4shAduGCsJgpFvzxX18U9i8vNF6ZjcPA0hk0kFyhlv4V2pFD7P--BNFh0Gg1P7bTVukuOHfs1ClIky79c41SkiD9a7KSO-IZJtqpiUYSGN_fAN6xhwnbkFOJO0qkylsHS2Ck_c5Q_J6ahwhksSQ9YCK6awiGPuLWMbFjDE7BQ_nBhQ9WS_-JGD0g16XJBsLjphiXKqnpaWQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbTrJ1cxkKVtaWF1vAleUk00ZtLvk0Z9lLdesjnDJNCaO8OEkLzA2ZWybbgjgwQk02CFHooTqVVWsNewvci4b6GP0GfnFI8hYU6j_R9auI8oORe7-RZHcgGdaQcUhnEk-jHoH7w71CVjkCNOFQEWUmek5mnqykoiqD96Sl-JQ4UglR1p8CbX9CvhqY2_uOWrSiPCiV6g31M_-iOCwnWghCVFIbYDBYC9y3DIxDDwiXZE5oh1C1pDUspLmZCQiEFSSmiDRDOAWT-po5fcuqFGJn3sTqhZq7f-TZethkPVi7BoRS_zmpFeSetnHN5kla9o3OGQaWtTy0JqHuKUue6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpzh9esTkGHv68HYC5gZUFe8jyz2GrK6i_mpnghtLo95PvPWbwSpHCNAv_Q7HSOOUGVlXDasHQQOcmnJQIk00KDlpFVTsD-_aG97ogxM7voUn6WK95K-1JXcI3OyzsAnO7KXQWowVPaMt3ko_tw5Q9FTs223K0rbAqE2rXcC7QQFgE0IHeY9BJ6B1cfrQAjUDoNogUuf4OBsiSLt3FNOPfQ_y86ufubrEnvYvTK77iScsyPCf5NhH5GLFocNZUto6gG5RfKW2qPNwvb7-5x1G0HPAkka3zksSTXzDmBmdVz3qUok8J6KdHsfCBcuNxkPQsI-wXmbhAbOysZEDm74IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=pNcpqoVkp7ghz-cVcKzw6kxa_iyiIcQ27jmAUVdggoZapTNvR1Inr-UfNMx_oDhs3QR-6WlLp4uikB7qbW2Pls2wkU1qzXLWIjIvGRaK4lyVRcnXO9XCfWiUgnCn4Q-8mF44SZQzv-CvZGAlUryzg94zQBWCGG0GFtBhO214UzrYN1ICTJTYGxMTEpc1HwmFNNBhrto3n_qagAhb5HLrefG9af-F2niHi-xSaEtOhiIFcj5fYjbrE-ymhpgvKP2KUl6dgU9dHM7OJ4g96W4-C6KL8xivl8Rd-RxrAEzFcN3tusJG9S8gvhHRwHJQhzLXfjonpppGqQTLl0u1n0deQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=pNcpqoVkp7ghz-cVcKzw6kxa_iyiIcQ27jmAUVdggoZapTNvR1Inr-UfNMx_oDhs3QR-6WlLp4uikB7qbW2Pls2wkU1qzXLWIjIvGRaK4lyVRcnXO9XCfWiUgnCn4Q-8mF44SZQzv-CvZGAlUryzg94zQBWCGG0GFtBhO214UzrYN1ICTJTYGxMTEpc1HwmFNNBhrto3n_qagAhb5HLrefG9af-F2niHi-xSaEtOhiIFcj5fYjbrE-ymhpgvKP2KUl6dgU9dHM7OJ4g96W4-C6KL8xivl8Rd-RxrAEzFcN3tusJG9S8gvhHRwHJQhzLXfjonpppGqQTLl0u1n0deQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ligfWXEpDrfPaUkowHNluxliarN17LBj7zMVglMBvkIfLujKU9g-7D1Nilvah3J63UIcQN-Z4w1A4mwSDu5GCB_i82qS7kXqZx_lNjnTj3B6y0TwLiUDsh2fCHWB-hv6KrNiMYGWG_8OBMFJDiUlvrWIvrN0lETARNzkZGA-54EZRRGDb26F2f5ufkedezv2gCmnPXaB05qX8kYpxt8KoegFhvOApu7Br1OlBNmUrnmtJiVepvVGeES8LMFLVmfqYI9_e50CUpNsmoEXB-UE_Bo2u0OIo5FB0h3wi8biU4ZkwgW5HdA-Gfr_cAxcndHbgUAbIC9PbNNo9d2W49pFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ligfWXEpDrfPaUkowHNluxliarN17LBj7zMVglMBvkIfLujKU9g-7D1Nilvah3J63UIcQN-Z4w1A4mwSDu5GCB_i82qS7kXqZx_lNjnTj3B6y0TwLiUDsh2fCHWB-hv6KrNiMYGWG_8OBMFJDiUlvrWIvrN0lETARNzkZGA-54EZRRGDb26F2f5ufkedezv2gCmnPXaB05qX8kYpxt8KoegFhvOApu7Br1OlBNmUrnmtJiVepvVGeES8LMFLVmfqYI9_e50CUpNsmoEXB-UE_Bo2u0OIo5FB0h3wi8biU4ZkwgW5HdA-Gfr_cAxcndHbgUAbIC9PbNNo9d2W49pFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUAImYVBAaKOUFfO3Wo_slhAFkXNtHt22y6rDkr2IbZamVgnhbjT13duTSze1X8gIATtWIb4UNN8sINirg0ClMkf6Bmp5emao3s0804wSsefabR5kBWeE0poq0bEsnYAglQO3-SbAlvL6CScpWuwZYjhZtEI6Yblt5Cmitjb-vs_Ov_2GxK8gvYHzgDPQmnnvxxpEHPw7bpEyFob1w294kR8CdoteQRfiHOxksw075tzkKEPa_hpvwLGDbOrCOkojmUHC89QLJNv4I4biT3RFye2IIsmWdf2mmRUUTkcfeaE-cw6nGrYaCyGTvC_X3Pux6xsN4Cd_-fg9p8yJOr_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHm4CvaoENjVNGT68RyfK0VBQNL2uTyRPhH48Xt_YnEtG_qjLFkjbt5LDOvlLZD11f-5hRnS04g9kvUYZDWDEQ90Wg-5me8GPDTzMOlwM6wIeLp3sWCajLXi7WGKiQUSEgTzR_B6E_nzPANNzeFs1kvuIyD7mlc5nMgXwlgMH58Znpcuj6sqMex-3Gy7Nnodx9cMb-ZJ2ELvWVAtagJImvl1PNv-xVxS8-5Ue7PYNER7wXwZy5JI-PsOWbJfzByInNKUrQz7_8pT0SsTkYOoKM7mfbyt9rSFWIPEMw2V_mD1f6LRQezs_tpw1FPIml5Ew1nLV4yGgbcOFnDoR0El_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSuUaD1Ztgx6SBeD5lVLFZJT_Azw-NpVTCcZ-CP4Y8gwOiT_fG4lVePs0nyHAN-AhbUBvYTTxQckGD56pNmjOpA0Vr8LozyqYUUL6Qx-SuN_KMvvWv25zu8bHyQfaGAtBBo_6yIQQlX2uTDD2OTwQj6ITuuLesmRNV2Q3oMi1nFxy5sIPd7VLLIjbJMpKYMRzubqWIGyI97hlWixmFKkbxo-nvs1Xmb-MVAj1EooPxsgAaU0rTVzJPhO7IWBxMuBnv1ns0Ae59CvwHrbd-b0ZIwkC8nM6khTs8jXjRLdfT-OSULhTJCofwD8muNCOWGRj-EmpZWdKeSxShUvKg4gIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiXliKdKsBIVemrEB8aNMEOzz4MkrmrLmYFQZe5mcRUkQGtzU-PDz_xvaYrK2nHsUx2E-uSbDWVRy6XQhnP3VkuP3gP6KfwV0EkXz1Wp_c99CimIwJYZHW9LvuIemJST6lQV5rj9196GiVUtO4mdoLk1ZcZ7kJ2aVdACCiJpifBgyIHf-fZpRnqrRAFZNdG2pW7QuPMXf__oDY9odYMImxV9piQjKC-RcDo4TxWPn-Qj2KZToB3R4NG5tWgUAM-R_-zD3WbzzC_PR_xyQ0rIomt7JFCvmqO4UZG--v9VbkeiBOaXxvKm7Hra-SAqiGHx59cOoniXj_fZjvbhhTQkgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZIjOOdN0gf6j8yRQQdOSZ1Hy94PYJy9ti_6KicJ2g5-hPlFfPuTnvBIngOBfaBAKSt1Jce4-h2AGESdcVoS5R3Ay2ajmHthKK03i-0mOfmPIHVAIYux3Ogmd3dj1u6KD3dSwa7jQUUQgu4-Y02FHz50c5MO0EahkvD9oRs2gm-dc8G5783MabRpn4zM0U5_2hvWpDLygAzYtTkIT8bl_T8vRNonJWHTsso23Gydca9jPCnljPF-YTffGjO0rWbJ6x5-FrPWi-BjNKXE4W8NP6vKYoHYDgoqUUTsJ3a7r8ambO2RjoT3_43JhTxJMqD1hv5Zz4uQ6iakr2UYnquwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcqiCGXwbnwr8AmT9z-hN8xJ5fsmw86lXQB0oRvF4AnsNJYYSCqiSbQDTn4hFZNi2afEPdgZuoQ7ToJo1AT4KPImLdlCy7DpRa6-Jg41iGQhcBUq64HJl5IsBwXKUp4PAX5H0jHbxGj7xG0XBQNqoUmuArG0EqRWEDb8d5262LoC0SzHnp-AYWn9n_piCP0UdSqTCRdNca8HzhvaKe2I0ZeaExSvhM5wQwivPuWVN-r0y-689JfW-EDkbUXz-kHXVPu9_wQu6YRGJtXExlJpaJK2rDKIUQEg0c_3g48m6Wj42APL7Hhl8Kf8N26U3F6ha6EuazJ7iHv6_8JusC7ERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ttlq6DjvFiW7qyPPF1XUELbdURL9BGYDOjl1dZD_Uud_FbF1LbXFz2M6B_wpfeBzEwNzOnN3ABKrQ-jysTqGPogVgIAF_2D-L-SfuDoOmiK2z45n8SEFdwQTsQCPt5iBPh2WXfTkQg-1NUFQzOYRgZfzQcAaeHvVow-F-M00oDxX6Y34xfu8rU6n6cR2jCFW_0H7HdIrt0Rwc0sBkMhaVcPEkMHlHMR_2n-swOZ-HYJ_hiwBygPqxEWmMhmvRW18hIoXf0Xh3TehmHD8MgEtTTmG2F0GAbJHW29bMsk7I96h28sVwWat4wiOI5d4qrYvIG6-QQi5SvFrBjBA-t7nAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqNFAOcBKNvPsZnguALbYZsav0Jz5KhE3I4_b8dh_h1NGuM9C5aPTjZjWD_QBMiY_VJOECEEY_KtvgpOf58swbCLyY8Gt0_bi7i7bWsNEaay6BX1m4G5VgGOpKPYDrf4GenaEsqZ3lToVFHDC7D1CERGH_mNIluY3UkBEV_LnAH6oq2a6ZXZkKJ4I3u4nt1GImG_ar0x3MJqRttAQ5fU3GsLA7f8f2wwET7CoYteCgJybvYQhG-yWq1arvCVyhBh7dbHup4zcyMZQSrLaD4De_5iUMPoa2TJ1_gugUGGYTvymzufgum1s9CNtphDXBHzOmv_o5wP5vq8QFyhbD5qVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=W-6BdBrm268kwu9eIii6S3Ir_zz7jQpFmjbbTOYQykiA_GWlNi1Qgha5X0B4hSy0WisecuAPiRONtaHooyQgo7nAxrumuwgD2WxqVOITnRo57s9oRUBtKV4d4rsMlFXwgngrVgsQ7p1kCxqaV5uGi_3LRG3FwRcYrFQq1MPNnuZqFtqwSucMqolw0AkfRojwuRDKlqgNnkjEoZsiIiW_9MsMAveuKxhzhk9Nl8S7F8w3cQkIAKGcMtOs4IURT6Y1xrrpnrWcheIWsfwVlc3L9CIApXTY9JARi_StlFs6B0xPRZWXHb3iJx2j9R75-7JAJuaImnn_rdTlhUaM-mJY4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=W-6BdBrm268kwu9eIii6S3Ir_zz7jQpFmjbbTOYQykiA_GWlNi1Qgha5X0B4hSy0WisecuAPiRONtaHooyQgo7nAxrumuwgD2WxqVOITnRo57s9oRUBtKV4d4rsMlFXwgngrVgsQ7p1kCxqaV5uGi_3LRG3FwRcYrFQq1MPNnuZqFtqwSucMqolw0AkfRojwuRDKlqgNnkjEoZsiIiW_9MsMAveuKxhzhk9Nl8S7F8w3cQkIAKGcMtOs4IURT6Y1xrrpnrWcheIWsfwVlc3L9CIApXTY9JARi_StlFs6B0xPRZWXHb3iJx2j9R75-7JAJuaImnn_rdTlhUaM-mJY4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGf428suz2AJxBovKclW-7HrYPrNoy0CFypPeeeeG7zP9eRdF9ha_JzqzxJ4NWeLVSDdB7DPa6SeOjJzjKyk6ssQ6OWuW2D22MJAPlAs3cLO8aX14nsyr9jzBck3clS4iirYviS__po7rHUD72_7SxTOzfNxZJHnT2EhQNpfC4XGfYZPn7-FpE4AJrOYsPVOXjhrgoqdHFtFz1C4ciE_z6smQBIzRaCx-KZqO0iCn9bIeVR_SfjX07SQsauZN1pe1d19N_rjqod53qnTaGFuzyn_IjIGnSqNIym0vEpsFcCNxz5wyW3AGC0hdCwjgPh5Oyy7VrwavdxPmhXqmF8v-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=cfbWFj1bD1JS_y8gFrA8GMLE1PH6fgdnjHgAFa_wwUIVOvAcgZ6l9aXa5J7fOZhKn7co0pRqr8lYncFR_NlBeB5-jBtoWqTE8feOC9Fvz3YnmCGtQxVAtYIC491Zl4-6GSma7gWU94MtV2orxefTxHbIpJsIvFS3HPACaMJkg_cYV1RdWI2iDDrQqukHTOanp9VdNVwVg9tozA4vVdZsW48DnzmY6U_NabnzTsM17R_PUb4eZ9qwxjfXwufi2cBmq96eL9rXAx8ZghSFraSo8vqDMflNzcNak5d3GgWM7kkZBM2sfee7s9cEtpQJTZFfce4ImVbhnWyMrAw6m6AofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=cfbWFj1bD1JS_y8gFrA8GMLE1PH6fgdnjHgAFa_wwUIVOvAcgZ6l9aXa5J7fOZhKn7co0pRqr8lYncFR_NlBeB5-jBtoWqTE8feOC9Fvz3YnmCGtQxVAtYIC491Zl4-6GSma7gWU94MtV2orxefTxHbIpJsIvFS3HPACaMJkg_cYV1RdWI2iDDrQqukHTOanp9VdNVwVg9tozA4vVdZsW48DnzmY6U_NabnzTsM17R_PUb4eZ9qwxjfXwufi2cBmq96eL9rXAx8ZghSFraSo8vqDMflNzcNak5d3GgWM7kkZBM2sfee7s9cEtpQJTZFfce4ImVbhnWyMrAw6m6AofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=lz8EMTNRuAOPB344H5ueZYvD8hFCQXjOdT-8io56N6q06lJIQGoZwXAd3wdL2v3jFudGtOeKZpF2OlaN3Dsd8Ul6J4QbBiN4HwxJJReMycTQjoJASHIDOURJgwtz8GUtUX2mfsSDQsRwlpRalyTUzhGTV0rAY9OF7ep-cvuuBrSYVxq_ZnNFCzCbZXk5yMWJEucKhtlh_g631mSQ80IgAiv7t7dPu7jSAL_MLj4RbUBLkenGGiE3boBCIRuO69S3LR4gREN6-DCHXS6HsB-xHrgPQq1XDeXP-3zkAqR9SBAWncWlaWcrBjxqyAswyQm8kiIU08mUNHSMKrM301CltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=lz8EMTNRuAOPB344H5ueZYvD8hFCQXjOdT-8io56N6q06lJIQGoZwXAd3wdL2v3jFudGtOeKZpF2OlaN3Dsd8Ul6J4QbBiN4HwxJJReMycTQjoJASHIDOURJgwtz8GUtUX2mfsSDQsRwlpRalyTUzhGTV0rAY9OF7ep-cvuuBrSYVxq_ZnNFCzCbZXk5yMWJEucKhtlh_g631mSQ80IgAiv7t7dPu7jSAL_MLj4RbUBLkenGGiE3boBCIRuO69S3LR4gREN6-DCHXS6HsB-xHrgPQq1XDeXP-3zkAqR9SBAWncWlaWcrBjxqyAswyQm8kiIU08mUNHSMKrM301CltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhraPtzzTuzYcW1-0sLcuqem7Mzr_0sU2eUYT6ix0iemI4x8AX3Lp3WmdKGkpxOOtHZN5wLfVzHQhSm7fYEtdEBmmTw84xejC1V4xjQyfbDAMfWqZV5bxbxCtrmat8E6VLuNS4z4iJHTGq1z1fUJqB2TFw2MMAXJn3zVWN-Ao-ZL2S3lu6zP5A4W_Dl37WVTEQpfgMxC5e0arQ-fXhhGFA0fUUP1dao2iQcXX6lKkLmdtJrZRblE2IWC01lS6c63gmpmsjXevcw-sKEjKFKXsoCbxEZRepUbUhbvKDUu4EjhGwL4X_1xQ1T0TyVjd3M1FbU9AQXzJwhrFyjHKvyuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5pjlbr_0D6b4audrqnJXHv85ranBMTVEXxzauILOXQUm67yJu2R-WrbFqHOu9W2DZn0w07eKm9V2ehvROgZ_w0kteQ0pZHYGFsbXsxwnxGPFB6vKcofx2iNcmafsMRGlgc0sfG05k5psluPmEjaX0bh5pNnrvi29jN853LVxYJM-007yl_kdm8F7RPhMe46ybc7Z_YU1b7c1dusEu-jqkPSjKkv-7V7rp91nB_H1wqvnX_loq8yC0joNNKeBbf1kuKJHER2xLuaFZrRT3X0d-VLDv7afAGGm_vo50VqYofNcdyiDqCcy5HHZEdRHP-dkKWIFUippfCu8QWgKoPRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pvyqfctCeIHYq015O5LFSnM-6sXvxFbZm0Zm3yU2XjXpRJwx8d3U9AxcGtQbmtG854h-cri15tWXmOWTwzSMMxo3kAccidnOrvviLPfNgBB_ndznEdlTtkB4HVXoFJgf3dFS450bGznrMbkhskqlL5Xg17_1ikHwt07LfMS-XYHZwWAIiQmnhChe40V-Xt00b-QdnTk6GwjUswlFt7KqX8o-2OOJgJAuV0gVM8zEVULeMjcRPyjtflY5NffNhMnKGcmGCLCllqsn5szGYac5f_IMUPptCpsoN1tm_IYXYpzgHEl5GCgAwi2JkBiLw93v5eYkuXWjoQlyacA1yQPIs1lTfacvHE448WdHQndlNcCZllyQ9HtdrRH0Q_B1sii8f0-z9Lsf_O2u7G6Yq2fi-oibPkCU7X2-RUFYP2bORMtToR3E5hM53jvm6PZc-u4bQkKrR9iPdmIVX_tlf7394svAa4zIp26PDTEVgh5QdFeYuE1ck1OZnZuOTj_xlfNp1N2Sq8xI7VZP5yCCruWWddlJOM6IS7iRVbkuBHvU_EZrCtaWOZrUs17IJ2iXNB74t5oHzTQ8vTF6EeKjc4vl887fJH_VkoUVZ9kj8We5yg5RYEvhSe0sPDfsaTeMcH0kuuF6-24Mk0xkQp5ISdBsLNSKyDySmZNI1NOrvANv1R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pvyqfctCeIHYq015O5LFSnM-6sXvxFbZm0Zm3yU2XjXpRJwx8d3U9AxcGtQbmtG854h-cri15tWXmOWTwzSMMxo3kAccidnOrvviLPfNgBB_ndznEdlTtkB4HVXoFJgf3dFS450bGznrMbkhskqlL5Xg17_1ikHwt07LfMS-XYHZwWAIiQmnhChe40V-Xt00b-QdnTk6GwjUswlFt7KqX8o-2OOJgJAuV0gVM8zEVULeMjcRPyjtflY5NffNhMnKGcmGCLCllqsn5szGYac5f_IMUPptCpsoN1tm_IYXYpzgHEl5GCgAwi2JkBiLw93v5eYkuXWjoQlyacA1yQPIs1lTfacvHE448WdHQndlNcCZllyQ9HtdrRH0Q_B1sii8f0-z9Lsf_O2u7G6Yq2fi-oibPkCU7X2-RUFYP2bORMtToR3E5hM53jvm6PZc-u4bQkKrR9iPdmIVX_tlf7394svAa4zIp26PDTEVgh5QdFeYuE1ck1OZnZuOTj_xlfNp1N2Sq8xI7VZP5yCCruWWddlJOM6IS7iRVbkuBHvU_EZrCtaWOZrUs17IJ2iXNB74t5oHzTQ8vTF6EeKjc4vl887fJH_VkoUVZ9kj8We5yg5RYEvhSe0sPDfsaTeMcH0kuuF6-24Mk0xkQp5ISdBsLNSKyDySmZNI1NOrvANv1R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0veWetztE_O89K768Qv11zqais9-It3sBroPAQUQXcda4pGrl2rtM47QinTSN0J5Zzhq6WPFzO3uszGhCT0wKFnQYesvEcfexm8PtC7lcCmYZ_RcuYD-lpw5U52BaCRP_kBhfAw8nTvdEzKMyKLKzcMOmmKAVdf8gKC78uOyoBbZRWyskzsEe5nW45rQQ88y71q6UTiuTS_G1vh4tUmItzNbYK8y3uXl63FwS7U72ZG14YoYLh6zLXHQiMOWTWU9JLBl_VWByP17iUi0YzMZIUW_tJg5VhgRs-fVTlS9brxtNNUTLHRYs96xbfGfXvFEyfaZgbJhF-W-c72xyJcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=gZJd3xdtB8Rrk4wkYt_GIxE_K8VaxO7a75vmGVFTDutgOXXH3AKArflZ8Gt2cRpsxp0mkP-esEPDXh-LESSV-C-u12z0HYLkveoVz4CN-kwA2sDTKfnvgaAVZJr2LI6GtumR2FCyPKJ31sZ-dVriEi9P91I0g1XFKj76LUXzHEfb0rZUrdbTgcXYkbD24pqVT3Co-Pbuqk8CRzn6m6kdSf-KnJ5oGjR9OnN-8ebQ-074jg56kSgPYGYRg5tC5g3UdyX4Qs-_gfqky3-tQTF-VPWQGpAoeMOOfbREzUS5dArUPzUethbHcMvpqm1QgQPdrzC9Js4cr5y6e6vPzFCc4TKE9wyM0Fz7_UobjNn4wbrVDNvWBCWXwaOJAvNv_jC7hM8mGUr3YTfSvQn6k_vnukp1ydyZggij616IYDc3q8DCzuCw8hhbzdjEtZA2hn9RDI4NDXh10x9Hi0L49ZTBc8DGftp9De3Lo6ieDsbp3kqtcTb0YyDzKFCKSSjrJz5RROaknjIFCTJPZSx1Mb1DkfjIGXjyC-QdEjhS20tLvXBD6ZpQ2fQDXxHMDYPLGzbjodfeGCoW93fGh12MsfhtvhdaXUwgi1hYRx5myW4u9AyjSNZGLsektZpbGx8pd1zlCS05zrMoon_15wEsLOZAo2fqCjH1VBhTZuWGo8AZu0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=gZJd3xdtB8Rrk4wkYt_GIxE_K8VaxO7a75vmGVFTDutgOXXH3AKArflZ8Gt2cRpsxp0mkP-esEPDXh-LESSV-C-u12z0HYLkveoVz4CN-kwA2sDTKfnvgaAVZJr2LI6GtumR2FCyPKJ31sZ-dVriEi9P91I0g1XFKj76LUXzHEfb0rZUrdbTgcXYkbD24pqVT3Co-Pbuqk8CRzn6m6kdSf-KnJ5oGjR9OnN-8ebQ-074jg56kSgPYGYRg5tC5g3UdyX4Qs-_gfqky3-tQTF-VPWQGpAoeMOOfbREzUS5dArUPzUethbHcMvpqm1QgQPdrzC9Js4cr5y6e6vPzFCc4TKE9wyM0Fz7_UobjNn4wbrVDNvWBCWXwaOJAvNv_jC7hM8mGUr3YTfSvQn6k_vnukp1ydyZggij616IYDc3q8DCzuCw8hhbzdjEtZA2hn9RDI4NDXh10x9Hi0L49ZTBc8DGftp9De3Lo6ieDsbp3kqtcTb0YyDzKFCKSSjrJz5RROaknjIFCTJPZSx1Mb1DkfjIGXjyC-QdEjhS20tLvXBD6ZpQ2fQDXxHMDYPLGzbjodfeGCoW93fGh12MsfhtvhdaXUwgi1hYRx5myW4u9AyjSNZGLsektZpbGx8pd1zlCS05zrMoon_15wEsLOZAo2fqCjH1VBhTZuWGo8AZu0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTxvtOUK0G2lhrWt9jT-zE-s43mJ05VnVUapTi4Ma5xtdanV6LeP1PwMcQ0ESuwfbrN-pgUVCiBpv-Hqp7cTtv49TfbTLDRcG1TgfdH0-_TbzC6FwMWGU62RPqN2joZ0PJGkIL-tvF5Y2-fhwPeSuwtgqTAWP1IiR3HQEhBkrR-Xi-uJrXhCN-AzYRrwzDArjK3Ty8nzo30AE03LhWbauAdWEIjquzoe_dKDKwEl0WYSq1jPC1Ts2cX10vCQNZiULUq94Fse6xenWv_sT0RP92EhrtPTspLyKcUQmOMjupOtGuM6snTboSTAjgEIrBNFev0qnbR4qlJcUUwyot4DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbu8bi9N9r-TIWvlnCJ5SnvJZ42dH6NTEjstjqAyjR_dc7NvfDIjb0ZDg31YHxW7LQ5nPg0ry1F4gF7HbFVprbJJ4tndcFZUO7bfyuphrLTRiFwoBue75AYDpDr_OlqC4vM8ytjng3zLtrJ-fySMQ7nqYpGBCSU-9UUYmsxai3Zp6gDn959uM8yUKDhKafSuIht3yOGgiCzAtbc1112wnejT-oGEADDt2PvuPnmpLzMW2xy0rBIpE3YWKMgcCP1FcKCyA6N9v6qIuMtRt8VVzOxZxsqD4Tc-sWPSi9PSy-j6jjMwT1CI090Gp6oaKkQFx2Q40U3IR8HogbVSogOx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoDIBPXr4NHpRxLPh2l3-OdZ-YQUxqMnxx8XmGXRCY8syoJjv1bOgara1hDdzZQ_psbwekXKHeaL_ssP0plcrYLjOyT_87UL8qOP66LRIAa9gEpSFI_zegE4eu1buryQym4NYjSfuTwXtuBInt-5xfHzYPtvNpp9WUoEdP-HkXdI2FCSZdTc5wINzj9qG9z7SJ4VKkPlu3r-V5SSa_gSM3k0qjhm4VaiJkw9bQgyCHLdZE2qsTFFe554HQtPrCWBF4bdOdzrK50g4LXW3TrUn8xAmsYhNb26MsOjokmFL3iPqUJ2ZLHsHQ6QGITf5-vocPlE7dOFfDspyb2HukTV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzdt0AaSfS0mUrvo6qe8p9U3e_4tG0o2MjmKj_YK61ac8Yq0mzE4zarsXfvf54Y8Rj99tNALTyL_3SZOYZQnQuISDlddWhln3LLSIPH6YatPt-eiM-5AbRC_4W8JEMhsV6MM1t7k_q_OIgQXW42U4OuR7f1U_4zlvhP5VxPjTr3mdyof-4yRWx5MExpyt3fDaZlC6uuFm0Qqur5EppzBWqUA3V4oC_r_rExH5xAR7dsxBK9cQl7maxdOgaoA3cftmB2KGOMFU1se615FoScBUlv0-zXtMM6rEPZAvhsz2qkN4fP-Gif6sw93aTPj6w93O07OpnEysEWmwzFiuon8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHAiVMaLvdWTOKIOMuauvLEQ64UunEw_CmHeoly8nPY1ocYchzrIdvA5EeqLinCy2RAI4Trwx5uN0IIRbD789kJIcQtQXhJWAdbVkPvBtZ-a2AiRekyTDShlHZFJM-N27jqpTItEWMTBUnhlARL96Wt5ZGE60LW24OkE9Rq6HioFu1SrXa8kyn1DEaOk16iqpUD24L1zPA7RVLaaq0iM8Iazq_YdjRpBVyDOLiJhzE6mOgEBAMaeWjLdVogsiml4H28i3UUnTGPa2siK91514RDwbgmkFwLvkaFiJ_5CxZwBnH1QKdIxGTrMOpv-fHPIxtY1Mh1_A7Bv0bGbqlxW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBi6Y0NpndMWJSg1XuCANJLNEw8spEzzjBOmdUxycu-tv5koHo_jmbDujUxFI6fCwE7pq5qTjEIkWx_dpxn2BGQrfcR_JwF3BA_et_urZN-P3pn7ZxTHpoF5Vbwg-uvezhgye8hfx48y3ESGT6reaaVvybgVVadBM0FNlcMHjuydMdYJQa3ZKKaBHadl5ZCAdA8GUgxQsT_yAjquVaqgfQd63wqtAHD_34aa9Y_L6ie-7DINWupt3OBu01_LgpprZzZkQONx01jMuVyMGzxXAJx_-ZHw_jijw3XmWOrSNWVoLT3d8J4yi41GXItq3XyuGomFgbzb6-OZIz0jjzIsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCVzTnkcrD6Rj90NVXpWrLlP6XpOguznxOe46wX9OkPQLr5-x3MYHImjdBYcrUMe63M2QYMAWlufY-TanvPIMwLLuDj1k09XEqPnxM0HE_S4aciE4p8FoyyEOqegoYnU6hqlOp-D30KMP4fWj18YU5ryfqtkEFSVh9PVUdLroz229lJNit89P_Mhf4akVbEPKGNoQ-bBDFNKOL4MQ87rh4uOu0ThIo72h60AOCQArD2y7VAsFtMKJMUQ1_RyawcfznCx6by_8CWBwBicjGR7hKyb1pF65Pn-L0X5dQYQQofZB0rQMdb0Xj7lxEvicQPc0OHaD5Locy2378GCX7RFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jye2_G7r6zkqwu5wogSTPc5kk5mkcqB2btGyWbh-b-DoZRCmezRhO_fAXY3G-1wk1dvYj6Lw3nR0Qm8bTsOu0jDz__Ov9G1OCVCDjUrJvt3f6KRhJPou2QL3FHaLNil043HfODHM_3wQJhAFqXPoL5nVpRTtCkYtoONcYmjPHfoU4v21UgksKt-RwdQnZajipTsKD-Hzcg_5BKcnNuSbj90P48nquZxfQJgNwpF5QJir-nmRN1VJrlz9Bkn5kPAnybBweniBK_nfT-O5Yrui43YqJl-n6VlzLF6yPrXn9CJgWaBHXpFuYMK6CDRuWP0RoVgVYjXETSQ7tJrEu4lTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpcp7PljQ6tD8bZkQG03fL_zrSQD6dT8chMeQ8dqqEx8gerJtgzq-BXZuSG17A7OvlC68f7DBFGpBII2eyDv7kJGWwgERZq-AFrhmEzS_4Y-n9uI8j9tpY_dF9rHRsIcdMRo6gkzTLOG91eexaP6lKLvoKRQW1xkY9L6FnGArwdVqRwkFILgwfg8qdcLiS5YcOid-76WJBcBoIrDmtyQTeX5R38bNUoylixFhWqiYokbiKpXrPqeoJ4CwQf98wjz-KxuUHlbuf8r43emZQX8EYqtj7YdUycEYwL6X4cnaTNJnWoSCbHf8ri27LfCf3On55sDOsyoYcVeM_qt65aSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKas3B6m1yubOCq3raNCUmeEa0eo6AQj1jrD8VhkShGOoZcu8l03glN-masScjAwK0FTiiGMGViMDKvg_6u8-pHqn-RYnaIIg9YydI_WLfRi_Dt_Jk7NooZkOEhCticcvT8RnsshUpxwmKGc7kUpRfxxUA0yZYUf6vrDfE4M3IXZkxWHvJxQ10yez4pi8vZWdMYHfFRaACRhLPqzbZtenbtYbWpHpnKGOc_ruhcP4Q4UX6i11AEDgip8c4M82L0bXoT3-qTRGQahFm-m9snF9lHQVfnahEmUjdvFZ-EbMagfBGYC9P8M0AOU22pGq_HNhlN0vA94r6HomtW_ezWNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZiugIGsw1HNKxfHzVydIqUk5FMneSvzw0VjG2QjLMR2GXgxXbi36Lzrv23Ha-SITkLnuLXaiP1bLujsBBrXHHgl7kHozn3jheR67EI78KMEwq8FDIGq2Y_zGC7aOo2Q0_Rm6mRfPJ0uQ0nZfGhkv_lqbJKtePZUs5b77zpfQmP7QESeqy-IPRuI319GiqarNZwoToEujFHPghb147TENJZJPzYF5TKg84H1pKcNGmscMd8WwfbycR_i3lpaE2Cl1e3-TaHCVofCE0VqQhDEkhuU5qKtmE9DsyqLQLBUkGUMmDkkIAoa5x6mUQqq_beotrGqGOYBPJ9LV6eIU3HJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ68R986g0kUCZvCAwegVXggMUIJAN1yKuLHSoeCcSjV7Uytudb1T8peqDX307iqMLxhXWgFO4ebaFXIgHYBvpA3MjPqHEHPkRRG5AXlFuHrEneTFL1XCAgNmy-P-TESIdHOujjeqr_nCDuDPcz9lVJZdFD4_5Viekq7LYUFvhSc4CZ7BdeVQ5l6F1J_UjYQXyZDGOjac2zlucThp345_qgFAw5lwrwnO_4GvxD52T6cxWhqOroSahBfZXd5ciQs9wIMM9lN0Gff_n2RI6L3DQAq30SWZB6sKcku_pjxp82N2d6z7XMRvD0cg-OghRueUh57OKpJhqPfiFDcQJ5-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2-IqbtDjnzgjZksrSk30XhPL6W064n4NKWfgKb9EwSGW48f04mz7DW11rArYRoZXbKQ0QR9E37-QwfdxznGwqnVEwF6UE4fkWYuesTwgIQtLaAej0WsUDw03ZVSjpZZtdVtYVMZRggrcbuyBCjiLdvBJh63YenfEfNH9bmxs72JNrf92Mw2k9MiRjzg2F6iUEk4W3eztDepC6OQtHlY5-rup2MRxUb0EdCUenoDe0Zt4vw8BAzELIZxQbkiOxARtKF3jbAsc7COGsDtPMWkWCQnwIQdR9N3tLR8SH3weR3CbCBfZ3UAe6mGJSDMkS9c1hjudxdP2V9BZOsA4cHY0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC63aY7wc95S6xFA0IiZ8WxPYnrfrzXTeZXR_nOp9P-IQibEVzHNlN90TYR898jBEmnkmZs3pi4cbzcbOu5NvqvsPZcH4a7PZU2DuH3vVbGQKtUDJCZbyu6eAbE_oovFJwC81tezOpzdtFoIU0xPFjjhIp3zjxNEFRgwYFLRT9la4wB2ar_v_ROA3GKN6DDEu8j9J1HHzG0fFYeZDzGw5vFgqffXgLpoz9dj-soNWmMA_jwPtvjOiGCjnpRPIspZwG_n5EGZ_qhZ4a-EZgFKTH-la91F9XGqgUvi_uBm1OnzMp5yq2Y4AbQl8wFB9ACr-nNwuZTLrXOHY65TvNrWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlNsMTIPyVxQoe-bYJeaIY26IigODDp98vQaN17Si15ZbYN7AjDVnRwf2nRNY2KQtozuwSd4AiGDhlCAdIuwlgOkkMW7eC_Dhap4m1ogxkoF9UEFOs7xbDD1nqvmb-qb5i8kQUkhrwSwgJO2IxfEcTApwUxhsm81qpt0bQZ7NZccDacXJNlelW0LaDOWJlVmgI-J3ZAzZQAvZ3DiTNwBr_lQ5S4ovaug2YnnC_bJXUYVl1dpMZvVyXCfcq1DYWLi4AIDvS2wwY60x-aGMRsrcMSHe91gME7utOQdA95z7PiFZEdv-Yz4N87w0kZ-xwB3PRT1bFts9f7EKei5-L46hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgxMwEQ5m-I1dIZw6ywXODN0sBRRAe0jhiX4SKx_euydhrVFPCi3FOCLpws2V8X_fbdwhdahM1ghwVhUNAogsD1huSXyimZSLSjtVjNxfczVPKLLfj-YAOpAy67fnxPJgoZHCC5uvL4Xi6owbqRbg99thkKefeo4HhfQo3ezJZN8B8tmEflF0m7jb5GcBi35nfdpp27cgfFyDIgxTTTPnqXIsa-tGQHfffn9_-lMRETGRH3t0-mo84aZkkjlU7fF71-IxBiQXiK4yrexV1-xnzYeWqdBMK1PWpxOtlj5AaY2Rz7BcHoSVvdIfeU0FnLRVXg8RXpE5QU_E9HetzZ0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcsq_gfeHHCRHIabHGJ7D9hszeowH-fHpSsjOMRTaIE3cNxIWLsbQOaqBDGGGHFYZH6G6uXq7FDXh4qyNp10x1PPFxgcHs-Tz_uy0JKvXpS5n-7TBMzGl1m6OXQbW81qzF2jrkFMGPNXR99z3rIX3yN8dOtQ5aqrk5vWro0HKkVMrmJaN4fetlk8RABYFzA-e64HmuI5QXWfS3altIZoldhleWuE7tnXtxoyGYfgwXicr3lcqt8lukYuw4R5eTc6wOdu1H2TOFqVMDTquFNfyzL5NyVMd8L1n7T40UgGud4HYQdRUAkctuTIidnZ4wwTRLCmO-WyQFpBL7rcq_L_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8Owujal-EB5YsPNx94Q4ROht9wH_BMM2sy3WcMO5XFD1vcG6-7h2JGipV2si-BJRBi9IeuUnQQxQE4FN7tZ0hlLURTBALSMEUACYYAp6MQ-uApacbpXkX7QEE-XYbzd9Wu0_yfG2-Cbe78BcfOdRU6fkdCkgsuKVSSZL2uQm68_CX8pIUNHLe3BMpJ5aQ1Sip0Zqh6aVIHQiHukXNxm8GF_TDqchfVQ6OVTqpRP-bvNKpSxodE4uTiVgn0vkVa0ANOks7k6mfPYyqnNI90r4UrDj1OgAt5HAbR0fQG8BAIJkpRckIYjt4_tJElF56svMr01G6peIWJb3AWe7vKYvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeFdTAKhBThhKwL-yj-bhNQFq26vsidftKnStdxNCc8apq-P83qdcZ1ASHii0gW-9BDFrPuu5_sUd0_MeW-E_EttyjzbIXUp6x0_HX0A87u5oIF8f6IPizHkLPP0WpAXuPJSrumRiXxLvPpEwpUXDpJBUwh9eMkH6rSWMdh7iDFVCIdI4jbJAVTblZ7zcAlQ1ggupEPibB6piR37k5Ag6bI5jfgFq4ijvbmDJYEJUHQyygOYNju9nDyil79g9Ifg_Byg4zpJs1yTmB16O6yO-4xbjqoKYzVlpyG6OHR4pVoWThXNWrf6X9nddZ20VEd5mkFhYIbNuLTo6OA1rbu5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/manc_9oL5ds6cI6j_zn22QtWyR0WvrLNs9vQrbS_buP-FMRWVHgCN_2p9aXue7Tv0fgMW_i0wNLXvJmxrktQhBdf3BBlsBuxzze08kjdEwkUuNgr_Rok3zBzgK-MPnJGVx1tQpKLvsWqzNO9sW65WEdhk6OjerbOtziWcK5GVQlt0C8Twajzb9_k2QBeJsQ1CqVL5YD70kcdLFjUG5NHmNjQovHgjdiNOFIA9WQhRp4YmUz3FrYLPZL51-ymZNue4i9vmcSLmNyd9-z94QcS4FokxLKBTL5Bv0YGUTPEnS3hr17Wkx2hGwE1OCcElhaNzcKhxsBSkzjMkGTg9JWJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H04aDlK131_ruPwNjSz52sfX2BWZQuFLsIVhYWAElnl-6IOT7muw_KMS5mteo1Z62-8E8V9kzTac-9B0pLgumQQks0fOmvVtHOO4flIMjI0a2URtX1wf8ftvS6OqxE2qdPqmfQ7xJmWgXscdhisnAsfOhmtiblPgY6OK8CT6YEiNRD4L-KlhT7ngQpljUAY5HLwSKFVOnckNqZ1Rr2oTw5lyfOD-1wAo965CGYNKd_a5Ckm6V6UZEVeYjAdqNbIXF-shdWtSWjiKWjLFkMyi53qZ7rA4wH5wj0ctDcBVgoW4QvK7R5wvFTFTlblf50sCEI7umDm-7p18RhH8kgq3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUOXYmA_RhnbGf5IXpC7gphJMZKPUxRjbm9_Fd1BAedSRYt1YIxm646SoGURr3U8LkRyeMWzD5YW5PaCSy3PVWjF02w7_5B8xwINF62uNA4V1Cgzlnxlvg2Jv1LyUXfksAdheDC4kPpgDoLPvPdq-N3XdB4yErJC5PW9-wNAkkFpHUCZsslnJOsKpDPzYPo23SYnJ3vkEEnFrsFt1aPokflbJxoP3EcTuq2eJSTa77JP11ofNtTaO4v-9Y70IEMQbP-5jZDXKvhnHUhEoEdXm3aCCHVb1jqUaqU4a0Qy0drvyFB9KGvYrpWzWB1RBYMBZEd_XqaC_FUAPy88oHjYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS7mm5ErrvQzdCT8g8NLhNInv4qXFRLqWd3Y_j74GvHYvCogx39HWQdoyUf8kw3z6CtDPmq107E7AlxE85zlHzzVQrDzzj4FMdBeDDONBRqTG-cQ7UTRmk6IDIIEv4iF0Mtq_oIEYI-eiWDXzXyAEWS1x5dj32llOi-dl4PrqVThIcW1ObWbwsTiDFibarDpA-_XKf14SxMAvsvPKbHqlafXcXodqNGPfiIvMAOp_hdcm8X9VqaWr7TfMxlG6z48U_Y9BP-mIUcEDoVqFzrsYCnv0AwTW-vug8mTjkAITM_k4tOCAsUEsOlGeES3AJcb-zxhcmuU-uGDr_s9r5WjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTfKcfg9L5VV5Y_tsEtpJqpvq2ak3cAASG_ohJi5aKuhqezB03L5ILOy9KVA9YUvdK5O6GPJtLt7-s9Xy8fBZXArm8MicM5yoedlGWG3fFNLmYoxKR2g8x6gaptTvEyvlAme9enQL3XLVPuAEdf94NvPBMZy2ahA8BqNHBgT_BV0EcJJ9EFHLms1GSneKPjzjc_ZpHsWPEIHqlQ5KoQiYwV-QZfc_DIfpjKK_pQ0mDxs4eW6yBpOi3u1K-S--YQaFC0c_dvQ8SRxsnMYxE3GkfWJyqdn-I8Q-NSQnMqhooYuk0uZEfHWlZLcH17tIotI3wQCs2LF8js2vFHgDSToGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqfkWyxjLANIfjldIcbSkvPDsBcLIMc_UtHV6E3hjw10r-mEbzwo8vVqliGppqhJIFpNLt9OkRHrOhyX20oU8boVBSh5RxdHKUvT0wVtiDt8IY4kJCt1e9Lvy0Qma34bqz-LZdVZBLlAXOjIOU_bEgZmXVle2j94yhMhi7qLiHuoRJY9yGdUUK0um_IPnK1DJzAaVrOqOAS56CGnnbX5zQm_Y9nh8SltbQT9_0bkcVzeRwagGnikfp0AnsjZjcVEXR7ql56j1_ltH9ynzfyRFb7w4Bi8NlQoKThjNFf8nJTzBilN1Uh-UeATP1TIWOa7NhUot7-XRLFalJNnWKBH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTRrJfPl3xf9i9PuptIGAI1aN15JsUXvDzmbyM4gdrbsmPq3xXg5iRA676hBSCr7jm40ahYljGmysQ_-as7J260DmaFGAyvdMr0i531ln2dBwX-Ya2NDGZIi3t4EgJLr2jt72XwChKvBhbDgK51R9weIPtnfB5RJBr600b9n0UAZxXMsmSomZ3EJEHdAym2toqm-CyIE_6o0RzumSOWI2FU0-TNbjsqabJ41n0gaDd3trMqxS-EqrCDaUcNIySWNH8-khhFNdqHfKXfLQOLAyIZn4vTR3aDPhnefqv4PqBcZvR4S_TyHeEySjDUuLOh4ULfI8A2VSubfDoR_UNxgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzongUI-ox5I_44FmwijQ-rB7aikbh1dRL9sk7iWkS54tpbvY9xPq9DBhGIJ_EzIRM1y2WB2LJ64gbRo3lPkjvW7WF78MO1p_Lvut4XTisyXju8mJfKd64AQkzQjudpf2ibSYPRbrOHs5dAl58tnZ_ScKv0GAHfWazP_HnGJ7YXw0PQ8cV83dJ0x9si6ZRxe_Jk1xUAY8gH4d0ZwCLfq9bHnhekXUEvHHkl7iHUBsN9XyLnAjdKy1R2AmqM2nMHQI9LmPHVPJXrbalTo8WC5Ux09Lg8Y5dGMKrDQrnnB0TpmhUxzM-VjQcKMxtImEk24GvQ3BFYNJQHfB-bTLQ8f9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er9wvN1RtGX-4-Ukgin3bRIaRx4LOrBho7YViMfkndMzsPx8jR34htlR-YiEGPGpaE0Q6AyUm46bIR9N0Gme6y1TUDmxvogWzzrEhIs6_2KIP5tbdzJAyMyB9lm1oCJ3CiHtOOlWQ6sUxXdYP5GI10ezEZE2cmwrHDNrt76l7QnUE_GNraZb74KyO5Jzq05Mj4tC_nRFfYKviHTGGExhk_jAvYfPX_1jHajrZWLKVQ4LRfTBZIto9FrGrEVFqt9iOuDcfeTnubKdDe-oPmcobJAk3g0wgmWN0koMiwdmmyQW8__z1dPEXna6rqFkOzMLJXJ-TIoCyQH0KCS-SU_ANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPDpgImlH3SgOA2Tqo5dXrPW79qGQVG6BwIXmGVtAfus0MFdnmKDKiY5zeBAJy808w9M5MleyrCx9GxQ2b1B_8hsCnWQs4S9agqE7HHd3CIIzPnrNiVH8R6_BWummnKADllIvnmPvrp1-4XOIkEwkPKcfQmzKDrZsdIJjU7-eDCxVM1PT9cjHPqZQlzw9uy7RAQQu1D-meqj_Wms7HO3r8yPPWWf2MFbyMahFtKmwN_eAaBL6tom9JcGmDFWCdENxRiu_c4zfOI_kN3rcf5viPK1jKHmN0MQVA2iBaeYWhX9_aIuulc4vR5biQptnrdTREtTaPdlkyOK7gIeLKpUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6BEja1ajnuRX4mbyiiCtFw6K4r1-pVhMbRkUgMLvKNk4_v1rBZeD2JxqkGRB2r4yX90XpGW_yEHrFFrk-OU_NHZAwOsX_bp7QoAzQWDx2EiRYdHPGObIQFl7hyKuukY4Muzue3QMxlyAAzoTv48HHNzWHVX-aUSnBiBoUpJeyhBRyhS-H9Mdtwa3YndDebLiMqF_2LXgPHHreikyGs7Mx6n_CFIH5UZNYzr0T7Z3gnlfVW-V3r1-8nBoseKr1bNTjwb7pVktzpaPt3Dc2KkClCvjqf6qjmOI9WK_bz-tL4rQ98mZ8FpWdt5BY9UixXyAOsHgeM72cAUZrYQVRUF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is29B4RjcMnKRCUmepyFH73MCi8DnIRwrsKrThteVF26NZD9-CuVnbkFJyXlvKDwbhGfgSeFRfpOcf2bbxNShoxwsPVZHYnLg-QpeJ8Y6PL4bnmXDU9EJoXTtF-fD4PUICc3yDOwqcnqULcYq-j2EMA9duO_bPxdXxbvDupFkSjbyqB4t-VQJ2qz5Ztp_kYHe-9U9b2BcvXIHeVd_AzqtjGhbDnoLp6mx33H0y8rEqQtf-nVXKDfcjy4N6FqNQrXGw1bbvpVVl7kqwhIIdKCBy4TEJ28nx8k-LfPNlNQr79Oq40vQVDBXLVyg9rrQpo-nhfKoVM8PnboICH4ZS0ecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvZv4mRpiEGgfody4B6QS8UKzG0TT9XeGiKCb3LUgPAztKoHfcbzlXJuF283bTgKeI6KhG2mEn3D5OsZOPgSWq0WXcudXqOBz1gPC0zg90m0MeGLbakkHFFl9OZqsxJeOOYjp-qWqtko9OXeFOCseBkmQmR-MeVmNsMbzgnhHaNeNiMHv45yWJcTLLdPTt4WUV3GnuxYntXeyYZiXD-TKnlc0v5KWkmq996bw-uRNSzIOOI2-eC4UC_kuQ_3AWCSnpX5tjebLHpc2-k7E7EJb4eYMabO_6NYAIBgLiFwh9ZIKgi0sM_k6caz2aK0ufRFY1bHAsBFN8qI8WVVwd7Lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcM9Yn4hoK4NNqsyPYiJTw-rUKsNpqytQWIenmahJcDzgkQoIeaGKueIH9BFGP4lNCDFKSNrbLgTDdbpqeBOLkUgj5gvvTvEmRUNGtRcnYE50uYKOUI70TXAol1wqge0uQ5GcFGSlmJjD8qoA1QjZaU0YPktnLoNvCO5yVIlal9GyWfNZz-lCU7N6U32UYfbBWyth0lIsV-TuNkjUOO7hUiq7baKrE-xBpqyITsaOF0ybq4b8E8srThT2TcReMOUWqPZpGrekM_iFm5TxMK1-p8kLUle-aReQ058mxAPhK6sDD_3BAPErfMnvEwOFS_V-8_572IaHmq1tzGumscKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOt6dlT7L2RDX4MJMlpunwOZXbpst-7aKDEqY-bL_ZWIodxN1DcjZU2H3ljU7J-1VP-CYA5YeodHL0VtLjCr9NoIYyJ6bTvsM9xfCMBTUdCPvbF1vbV5wCf-sYePFRxRU7n2m4p5J0so83z7m9kDaCHsV8_N7tGwoD_VbHc3icb4-j2BMl2xIx7fzGGdMoAHgLbNGl0o-Kr4iBP6PHKjAANVY6tN0_rFd3X17BELht8ESdSvkhvCQttsL-InM3_3b8Lx6ygp277OSuOBeyUKBw6bxg4XApKqjEy3BMw9SFkdCmXZTW1gVqGYHLSmY9R_d-YL6MI1lDIUmX1C7iLRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=i_h4BUExGQC3p0hUYIKFg95Um9VARMbWAOwOmoRMDykcuWCKEH1rMLoG5UlWDn7FHy_UGAn3nMP0XXYjgmlv9in4Ts5kqs-J7irx3ZWblTYyIuao8vUriOcwo0Nbf7Rzsdu_uoKpBsAGCohkjmAO3YP9hvw1NRj6jCIA0STNF5T6YMgPekDAC6svmHxR0mGjRaA-2P1k436P_myOqB0iCw13QK8TRdxJCV1c6RdCmv9oqQOQv5wBpsYt3TIcqfCK09TDFFjgEaQ9zEiJHNUgBK7VeoUdDffcaeG6GgIf6FlnMyzc-CcyALNuHExzn4KVE8bSUU8r4ZR4ZDLD9rC-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=i_h4BUExGQC3p0hUYIKFg95Um9VARMbWAOwOmoRMDykcuWCKEH1rMLoG5UlWDn7FHy_UGAn3nMP0XXYjgmlv9in4Ts5kqs-J7irx3ZWblTYyIuao8vUriOcwo0Nbf7Rzsdu_uoKpBsAGCohkjmAO3YP9hvw1NRj6jCIA0STNF5T6YMgPekDAC6svmHxR0mGjRaA-2P1k436P_myOqB0iCw13QK8TRdxJCV1c6RdCmv9oqQOQv5wBpsYt3TIcqfCK09TDFFjgEaQ9zEiJHNUgBK7VeoUdDffcaeG6GgIf6FlnMyzc-CcyALNuHExzn4KVE8bSUU8r4ZR4ZDLD9rC-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYynwQOBCyPvPVvAzKibPz8NWbmJrR9xYAN63m4-qOoKspR5n7Bt06GkShaMBoOUoIxCbO0mpQJ6BpJHmsdMrldkPnmGztlyCtvEuwT6lbRd2ogLhi_cfV4PGwDW6pz8A3d5CJ0_TqgUXJf1LFWWaAPE_HKx7WSzf9xZ1q4iDqKvjcvpWW0bI2rqq0udYXq-JDz_xS2QOc0d67t3D97_DF-Hqksgz4D7XbVX4MI9bmT27u5nZ75e-P8-9EcsEXoKBn19PUXBmgyfJAUY3f8qiTnys_2-Jnnf2ymLesz3QS4Bp8ozh-gXxYkJaTIucNQlx1h2000iZl6P3h2gnoTT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=swMf-8QiaHOYn9vbPSFm3C-uQN78m2DYtQc2GCxFn3werTpDI4CEod0Iobjua5Szn8eb-VSPlGBuULO3A8JPEqfnRiW62pnR9qXOGjfchniavCr-n_Ff6Qi4NpQeOcyjmljIrkiE_HjvGp0CYk9d0cKCIs6h94nwAATYQY5-_ORGqaeEG6NmsDY0tCDOtz0stXXyslckg9iGl7IfmJfazf4dB-wI_yTNUsZSAeqlInbvIDDS6_SaTuh_Lfh05j3G7bIW78T9BOb-A2nuR7cRE8m1gDfH_DV6SSI6TSCa_uriYaWMrex0wdnloJ8Y9zCgOvHj92RTFIKQr5SyAz6Fnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=swMf-8QiaHOYn9vbPSFm3C-uQN78m2DYtQc2GCxFn3werTpDI4CEod0Iobjua5Szn8eb-VSPlGBuULO3A8JPEqfnRiW62pnR9qXOGjfchniavCr-n_Ff6Qi4NpQeOcyjmljIrkiE_HjvGp0CYk9d0cKCIs6h94nwAATYQY5-_ORGqaeEG6NmsDY0tCDOtz0stXXyslckg9iGl7IfmJfazf4dB-wI_yTNUsZSAeqlInbvIDDS6_SaTuh_Lfh05j3G7bIW78T9BOb-A2nuR7cRE8m1gDfH_DV6SSI6TSCa_uriYaWMrex0wdnloJ8Y9zCgOvHj92RTFIKQr5SyAz6Fnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0BRuaHSxE20PAE0cxM-YVCyiUDPmOaUbYNLPFEqcS9cHlqR1pIt5UUmtjw4Puaksd0DE78TChBvFTvFPk1Fv4v935-r_T6MvOfnBgaOQ38zsKO8XYkOHKfRzfZAjF_dDrLV-cnKgvpAW2uVbLYLRiaZsPZ9Ombfez7FDFkLFQyzZmlpUyNms5WcdmwrN4jB1ti6tS0D9zptxjFXx_I4dmJNCKuUqGRe_WOqUuqF0KKNuTDf2D3DA5inR9mZzohhdpqOwbh3ue7dzV1mbLR7AdYdZXN7JWyESf6NP_p3Y4-cX4K3Xz1jxsJ4LtgyZ_eOHPJrXBEJ7-WoI504DI4dUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW0TNiwojvLlTRJ3RAaK3BiA8rcqbFRfkWR5daZ-plDWGq8el1SPuWt1pO98JEUJx4L8Xhx7e1GvJ-TMP1T4HtgklQNTkpqOvLtraQ0TqwTv1t8sVJXi3YaJUUgdNWyNlRDXxx8IRfTiPzOjP2FUReX4wYz74fkFYfuurEvscfQeMl36pmw-GPlzH9XDsmyq2Mpwl2C5j52Uvq210TngEJAUb4TBLwXl77ibWgtktgd30CTnPFcYmi4e6MrPqB9zpvoLp6zwCrXT0L3FOBJ6cff9fnmzrlZfOv2EaMcpV7mst_uhr5NYucOVyfpm4V9IoZgEJuOW5sN6bQ8-aPJc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=pMg_u7_iprAVKhKI-usWfdjl9igHUdsRY_-66JOzbp7e1o-VgQdASHqmBiEofT23q4UCTcDBFNSHTWeSfq5DhB0OXdO23hCu5D4lRat3yC49X4dz0S4SDLd7qAtBtCeGLRcYCu0Hnr5g40zZle7dhnkz5_Akimva3qZ8QSuyqopvTDENxxlMupb4mghloB6mwgdwf5R3kvjdCeAsq05shvCgCfPqD7Kl0CCkHawJm3wLt6fatJD9vU69peOc4TKL0PADFooB4bjFZ0qLk9soiX47SYggB3TF-iOn2ZsmKKgiYf8975NCiFbTO8yZ59_P8brSNcN4-3Es_o6aKmPZuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=pMg_u7_iprAVKhKI-usWfdjl9igHUdsRY_-66JOzbp7e1o-VgQdASHqmBiEofT23q4UCTcDBFNSHTWeSfq5DhB0OXdO23hCu5D4lRat3yC49X4dz0S4SDLd7qAtBtCeGLRcYCu0Hnr5g40zZle7dhnkz5_Akimva3qZ8QSuyqopvTDENxxlMupb4mghloB6mwgdwf5R3kvjdCeAsq05shvCgCfPqD7Kl0CCkHawJm3wLt6fatJD9vU69peOc4TKL0PADFooB4bjFZ0qLk9soiX47SYggB3TF-iOn2ZsmKKgiYf8975NCiFbTO8yZ59_P8brSNcN4-3Es_o6aKmPZuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW9LCV3lOSkOJlgAkYblLV1u0QbmsCZ32GJ3sl7T8YUNyW3YPd7AIRxvNg5t2qCEH-bgmzPDEFA3QGgSVN0ms-G7zChcbK5zeSpwjeOPVzJUaymVPcO6hFz9452ksB8S-3h8LmNEH2AkszKXhWC-krLxZT-V4TyXsEtW6WJfBAkfMDR-tAYCO3zqopHFQoeNYHpGvfM_8ZlVA9_IxW2qalE7bsHqZHzcmAporPr2qEYyF1IDJ0dKayOq1CY4C4C4KGUXk4AZPPedys1ONCyBrV-Q8aVNnmUJd1OAVwLGKWiEOWd428KmO4GdUwVr6XyoDzIVPHXJwazFR80N7SsXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
