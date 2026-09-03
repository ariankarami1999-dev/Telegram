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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iKpEveoCZ-2CHdIhIurgC8wRV-jzus4yRW1woM993tQ2t2Iyylxb2S2wAyj3oxFPRsO6cLEPlBrtr3gLUTmNMkW35roWKe3oOT7ZEbqmb8lKKrrY2mgV_lWgMBr1xF4mM2QiE0ZRPzU7bBzI2qcQSVurOJ8XehH_6XXzL5Ks9Qxckbad7Z_YACv2n8uaRf-6JtCvuzxGsHgP5drgjJP6_GW0VYa4XJx362ECGzjGEFkT-jT6Go_CydmYBp0mKzHtdMnQdHueX3g8rtObAObPnU3lDSv-4NkRCDCTCBetuubzZjb-tHZABtbZd-50fodHlK03VrJQWLvpxZC1_2rR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iKpEveoCZ-2CHdIhIurgC8wRV-jzus4yRW1woM993tQ2t2Iyylxb2S2wAyj3oxFPRsO6cLEPlBrtr3gLUTmNMkW35roWKe3oOT7ZEbqmb8lKKrrY2mgV_lWgMBr1xF4mM2QiE0ZRPzU7bBzI2qcQSVurOJ8XehH_6XXzL5Ks9Qxckbad7Z_YACv2n8uaRf-6JtCvuzxGsHgP5drgjJP6_GW0VYa4XJx362ECGzjGEFkT-jT6Go_CydmYBp0mKzHtdMnQdHueX3g8rtObAObPnU3lDSv-4NkRCDCTCBetuubzZjb-tHZABtbZd-50fodHlK03VrJQWLvpxZC1_2rR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQwgQB6MUx0AvbGDorc-79rjQrwJHYO5L2YVPTKQKvKGyayw4wlBIXlIanEw3WGHi4ZwVhE_thfstHPg6Olx5bICucdDUgxEhseKg06V3FnYtYj1O5l-GftaXl3CD2-UyG76i9XKt8Qmq0iazv0sGeE5WQelcbMM3GTDvry7BEwQFA5Yt_mS2LPyKezM0N4YZIAa_8SAjzIbLBl2EbaVHHt2srOuNsKyLF2tuHjFnJCh9zRNv4l8M-_MySV4DoRyqqMQVFlDFHtJf-BSsO2VfcJno2TeEEnJYYa5Qu2irTFqsuMtu2adqi7x1TTB-O1BROejfh6Frmgt-hISHXJ1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTTn2Jj5KHYC8RLPb7aSDcF7aqG47R2kW2DF3V7v-9m7DaBht_hyBNl9WPUBJf7YyerXh4p2OOb1cN0EVIUoaET879xoy__e6LPKXUA0E25e0ANmOe9TnrDyvpIl9D3AhS2_VtxMmWf7sDb_M5sLOK0jw7NOB9WDd0RRSl9ODLNiFhREAf_CPypjoaPObs7MeN_btAZGc9KO3gn3GQgxNZhHTKVDObS4q9XAAnHMnzyhUdcVVfphlFPuWB8HAYrsZrsCNeGm52Ie-0keLZTspsXtnXK3KUAmMT3zuufxAk7xyrhsfCLd16_6id4FbnjqujrlyWD8wDL6S8lmA0nnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G70VWaEQBxEcwvi6rMCkkJkWeBJEL-Sea-H_bxf_OaL6VbGpp4fQro_LKrkZa8YgoVrRFkGvP-8yOUQXNV16KJHxP_vt9lexm_oXzl7bHCqq8yBcpUP2DzgTKbSPYHXy0frysoE7i8ZD28QGx2r9uTM_Btq_YpsJjYxxxrq3POQIzPv_g3tBkg9TYFJy_QKztMLTE4ss50teG6qCRolBe8v3-qYpeHE5YU-oTwniFUdTpyzxpAIo5ISJjdoCo0wfXlFkfLtZ12EfFtk5aRrMV_1eDhJtctJEkE1SjQbtvJp3mIfD3WXV1txD-W82lHgK-qRzI1XYcDY9HIX4C1Uzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5WgF6BaSGs_BCzcut4G7peSBQtKhy2T7mr2EIew1qHcr_ZUW9GxUjb146y2Zyh_6t8V9dBGenU_CePqRNwyZm-rvCaqYlEYHQpW6-pqBHkK5KfV5ETPs2Bjqr1VVsoQE0Bp0eQBL5Oh_zi_w2bUcANp9xAxWz9DzEjLQToJUyepLqKHkq4QnYU2CTUyY41LWJYPzdfsdOntIrJbAq3XO2NPluMfAYbWWaPKwBjlsQeiIksz6uryd6RD97aGU5C0TGxK73Qbw64BH9EYeTYpVtudPf7kiE8f7-lrvzvggaEfApr2_IZvEla2C3GdIeCvylcvzoyrxkr6AjYzDQ3HMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0h3gujJfP6Y1yvTQ9jplx8LCvqNyLo3cMaIzKL2accxpgIlYI2LgbwoBiq15taX-0w1jDeiRE50CSTvwyyI_7yv7CXL8HEDwQ37lBa4dwSWgmNHPyEtoz-U7OBQIbrrkYvZdmOG2reLJ2oLeGnQFoAclY7F6mFey79KrGpSVfCYqooILX3U45Tck6E-zDo3siaG7epYa6sG3hiJkpB3bA5-mcpniDWh5kFPeC6JX8RS3bLgJFTfgiGu2N5MDscx__ILu9NNezDt4qxALNuGedsw6idyvBBHUghi5PhUV3qiQGXoqKXBXGaSQlTaZFHNW3ml7G4IFWbN-ZFbxHQc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMIuzHJp8QYZ-tuQQyQLvdF4D6ZcQYZGKh5kUgNhm9XFYRA_mO6GU3df1qCyR8_kyZcbW0anC3Np_BSsRTxzMJlpES5wzqoHVy4RNJvHjJ4MEANUi0HocILgwr7f68jcEY3J06I8CRL_uaBVf8FeZhHDyDIeY0kwk6hhpeTdOKiLUeU4nf5kEiBRlbMFy5TS4KcE5_eDrjemdVi6gsoZTY0imyx2_4S6ZhnXngeGD07vH1h0U0aeeX_x76krlv6eAGg4j6Gt9f4ZIKFuG3Zs8EiPV0JuxmwTZeoIZx_-jPXA_-DRrKCEG3sQQTBBAbtKY2wBeLGuLWJ_QXyJKP30WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOXmMBzj1gtPL767RKTF92jto7e8cWxFLMPYeONe6lI3a-pCrmTnKv6xwd3pEhevMC2JuihD-WohScw13uRH7dUeNmWaNumzWTX7txVzRQwJEz2zpltW60D0soqLEdyGDXWhy1-ablGG6_-NBf3-SGSvf99KbId2ger4exy46K9K0S9lVfvyEwHVGRbenqpCEIchMhCMym4nfJZH488RaZJ7uzZ3YngmCs-laco3dyrDgC-W9zL1qjzA-x3h5jxzYVrkMry6XdUwmjVao5DlYuxLL3hZuU3BT0fb3U9IVsnp9fbbIUtZtxTCrEfX5eKvH3WYgvDpu53SN--vMjt9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVpabwf9_McNrUp9dJX2c1iB8LclKjsBpKBpv1n2u6BDDbxuaXwYJLHoPmA2o0TqoMfUG2Ogp7jTLV3I569vac6ch05MgBfpJP-UjTfag9j5azddB_9fziFUZhxE_-Vq268cNv8qh86miXHXDMn_B4LI6_Q5dAsKUOM2XytGy5FX7N4pF3kZ6lf4d5HG7decP6xKirylFoFx7jlueOyttAQ0eUr5Z9jXO66u2phywIEgRa353wY6qkZmERWr8RTnyt3qJ-jgU4AfQOXisYmnbzIvWg6nDBDeDFwQCrq8U0yuVK2Sy5vhsvkAR74gId8B4A8xprgs3wOdoI_biDoKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njIYFFPqYFwsluLSidMsZTZh52kw6SNx-epmtwvAsDIa06t6HC42XhrNq96Q8shLsiVdSbY8fMmI9k2AaE985vhgPfLqpz4tP9yqcmtjfuHuB7pqCv3_ot5E0AG-0ciWQ2Yv5kO-lYiQ-Nrd9VwyODA5Y6Oly61wr50mRKOCJpp-ykREs-JkzGtDL_5p7Wi5cU8u9x7xHdsLGhoeq4zWPozhVBdnISUpGgCVTbWXNacTH5jPsg9OLjRhUpeZPMFbD3OzRgldUcGsQFZanmUmEkWQLQ-fKmYoAKeQRhRcV5qf_E4qi6g-ngzAFgynW8hSMFl33p2UqH58yAnJhqefqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=DueFw4fcu2WRjNbnARc8yk31QWgF1d4Cq0CXVwi9XlTWqMoT8YTmvPnAAne0PKvmt5EY-W4cSN55INf_2Pltt3GXrhtOHyyKhLlplsXdZGB1CM2z2pSDk88ylrAcr9b4m2OH91kZJI3QKmPYGFjg9Qji_7CrGd_eFNKDv7enJbYE5woaFi0pLChj61LHRd-fp3660hQ-vG3RlcAuH_GmrLyWBcDv3bgLmFfbAN-QVC7OIOre6B16LF-PwDSqLwIbHftAAj17bK2YyzofgxM9VxtH2818PEn4vknXv-DkBvUlJtfqRgKncMfSEqOFuALu4LkTLHKAhbMSuH_6b6B6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=DueFw4fcu2WRjNbnARc8yk31QWgF1d4Cq0CXVwi9XlTWqMoT8YTmvPnAAne0PKvmt5EY-W4cSN55INf_2Pltt3GXrhtOHyyKhLlplsXdZGB1CM2z2pSDk88ylrAcr9b4m2OH91kZJI3QKmPYGFjg9Qji_7CrGd_eFNKDv7enJbYE5woaFi0pLChj61LHRd-fp3660hQ-vG3RlcAuH_GmrLyWBcDv3bgLmFfbAN-QVC7OIOre6B16LF-PwDSqLwIbHftAAj17bK2YyzofgxM9VxtH2818PEn4vknXv-DkBvUlJtfqRgKncMfSEqOFuALu4LkTLHKAhbMSuH_6b6B6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=fVPVCOj6o7FvjAXGApEjOuiakDDWbyO3IE9K8a4t4hqvqsJTo_Bif9LwtL6RQ5Bdo9Ff2OPPRQ7ocg7AFH5BrasNX5owerljcqv2p3GN70jn0S4cg77XLtRczTJz5F9sNcxLGqXpCnQoOAzOZ8i7p7yknL7XWLHytbRKLvOhnnANARcX4NxOnuK-h-EOOLeI8Yc3N1q9mk7syLAtoWuq_EU7n6iqOmXXz8NRBwhKWIJz8TONAbjaBfWxGBNVWwhUP9VfvxxhXv9TllFQTyGROk2GZTgjIlH-zxWKR8AWj4TcNCFL4GRr5vQF8vyERhBrpP2qkkfB_eSZkbdTizJJ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=fVPVCOj6o7FvjAXGApEjOuiakDDWbyO3IE9K8a4t4hqvqsJTo_Bif9LwtL6RQ5Bdo9Ff2OPPRQ7ocg7AFH5BrasNX5owerljcqv2p3GN70jn0S4cg77XLtRczTJz5F9sNcxLGqXpCnQoOAzOZ8i7p7yknL7XWLHytbRKLvOhnnANARcX4NxOnuK-h-EOOLeI8Yc3N1q9mk7syLAtoWuq_EU7n6iqOmXXz8NRBwhKWIJz8TONAbjaBfWxGBNVWwhUP9VfvxxhXv9TllFQTyGROk2GZTgjIlH-zxWKR8AWj4TcNCFL4GRr5vQF8vyERhBrpP2qkkfB_eSZkbdTizJJ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv2wrGG9zM6pldEe-FwSR2VbKt2ltmrpOiCw3JI5o41UcvyO6SE6M0IMbFuKerR7yn3sv06I5EyvjkDGr7jlX9E0C3UEAVLeYiWAy80vuUiltTttbcC_GFbmYGLOhCV5dZVrpYpXxZ6D0B3nAzoe74mpTrSeP9ljtLmSbvp_ReDXCFvNDcHYiSNpMT1G1HxM6VPkD1Wy0YFgK7jeE5UoKhKcmFvMXxWmcqaeeRxEDWEcEWQgJpgEdbVwBoInQ0Ihw4AgffI7Ihv0_VPhC9dsSUNVrQh0uo3bpvh5EDGqQtFh8RyKyTfj-JYGu4VUgKZ0nDy2GOIWv8FvrRIvWRDpyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHm4CvaoENjVNGT68RyfK0VBQNL2uTyRPhH48Xt_YnEtG_qjLFkjbt5LDOvlLZD11f-5hRnS04g9kvUYZDWDEQ90Wg-5me8GPDTzMOlwM6wIeLp3sWCajLXi7WGKiQUSEgTzR_B6E_nzPANNzeFs1kvuIyD7mlc5nMgXwlgMH58Znpcuj6sqMex-3Gy7Nnodx9cMb-ZJ2ELvWVAtagJImvl1PNv-xVxS8-5Ue7PYNER7wXwZy5JI-PsOWbJfzByInNKUrQz7_8pT0SsTkYOoKM7mfbyt9rSFWIPEMw2V_mD1f6LRQezs_tpw1FPIml5Ew1nLV4yGgbcOFnDoR0El_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuxdFz1ZJrfnbI32nTmlMpuLNbvdv189iXqI7oMV7h7KmR-5CHY_6zMgcwOKifS-1TsIzEZYlfVjRzAgf1ZYoZQkonlygRm98gCHusAM65du8bQh26kaEjM9h4iNe3UGowvrEAX5zB1Rr77Zc_uKTvJmrm-kILUjAcPfNBo3-b-pZwQCxsh4-JBtujHk8Sve-DGbT5cldrYi9oUq6P6W6vV7i2DSsklUgH7556MqZlHj_tKJbsozfINup_CNQG0pys7EVBWEf6U9BgRijImEaGY8s2f81KGy9KF7TbbIPaVxYf8imj-wE_DtiEEsizJiwXYvPb-83QVdRSyJ1Y83JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2bYkJOGxn7brXO2s4nqHi3K6xCeLbHLmdrVE1OmdKOgOGTPI3242jjXfGrdNELl0FQvWD7NZExfKtKsCV35C6ecGdhQzUq9lMnMDq7e0b2vTDA-wEY3ipZx9L5hdnNPo8xiSti8f1hfCzMQeS3YEIPkam8S6MBh_7mGKsIUYyUhCw-Jm5BNJo-x21bzPe6ZXdvltWhdUtargCP8aQv1S8SjCGEfh3e2P3MayKPcK-Cc9j7vz2CbQBVouSCaImf4A63ryr1UMf2ctpdIYu4gHF67fa3OT8n_XT-4ju0RIrBzc5gfE0xEhcHrDQ6eTGWpcMcM2sXM7aQs4CwBqalwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3VUErpTqi5OXNcgMjMkpqO7fcHGFi3-H6dINS5xejQ6UWqnKJaWmo4GmgVSKh05lzx193q-0ao7Y8Ayr9cI93nnr9n-ASjeQ-chAaZi6SOm51fc-VZrEMpiHufqTI5GicpKhez6z19hvlbt4W0onaUmgR4YLhDD9fyr47-52bu5hNP1ptSy0mdeW8PPPMg5S1kMv6B301QIWWT4ZqFedV9rPh8Gxut90mvDCiUQgLMJlz7cjw7VF33OwWzk0zqNpMqgWREJQfsDJyvSIcxFl3yR4A9kKbpjsspbe1W9zR2VP8C_4jvcTh_NbtlV8W4637iJSiHtbr-wbURrztuC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ7Oiz7qxzyOwoNUvV_DB0xgIEX_VfX9TBbau-j8jqg7vhYGo7VnfnO5HlLrIKJVfsZC2R903f4xN7GQzDupVUOSKAu4GT54K-xhBsVG87Q9p99wz_mA1itl9Ud3e5Z5c-xdTD5xaj1wKEcHHRlvxaVB_yuTky1B7BlJHufOz-EeyZAr0iBtlCtCmba-8HaQ0lFX5i573c_r4r6wW8PULxPrWWKesHP7o_Fgu76MznwvQFfL6WaT5kyuGezvLRMm2CLfqC0CEkMpY-Lt6DwXTB4RWTzJwRqslvHhabAw5dhT4hv-hDKTnH0H2wFCtGBb6B4gKGIM5Gp499l5azQfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCYAkXYdxrrFYKlxXKlOOdGha4DYUR7MCwGL3kZybhFZKapBSFpaF_yhgHsvxRxDdl3plXZV2DB_w8B0L2zIWtfCvtLILjpIrkAhB1t1UUdpw5nzipuKN6OHF8fY63y_wt_9PFcA4TuYqKix6mcwvyd9sKKWnM2xT_l2XDD82cvOwo39URUF5tR4Eam8kkqdvBDhP33Gb8cOvfz3lVBwwXeT6KsgbIHKrDBj_hrQUp_WsWqzkz3P5CwG6lXCS4VyBpEv89lo1oWGzXVGNb9itjnE_ts-rNmuylnJYWbDLAnzKS_PG_GW6NAav7mkKOugmoCapal5Fq20Cz81Oj_mmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7C-oHG5y-3Oll38TuXejUkeruUWjkfIxXuEjwCtx07cpnc2KgsvyxX6U51HiPjmhjXWK3fxKzwtJRsU4EzwlbQopLE53YCY7za68aJNBH7Y0GErBgj4oQ-l0Vn8v8irfvTWbI6SD2d3-ayXgJ6WQyq8l2UiwjjGWIe_Yuz16nsjQqHIC3WCx1FxZI_9XC2aGvpX_V2ZRztL2WAdQBRdheqJCaz0bWQG4euoZoErHi2uZVWeg3qCsi0p0R7KYDzWolSvDbAgMmCm2F2juK81Wkr3CY4Gv1TyAqTJCBhTts6ssmbnHNo9t18eeRe2NOLFLCTMUiynueOhyo9Rrrt7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=BCVDFj31uTxTR-wfNkSBSgN8XBYUX9agmeG1wHYrkaPJgUNqbOSB8R6wB6s7Ql2C-N3B6wk35Zg8Rl8-PCpu46oI0Uq6FVacAP1KmfEkQH2F4E6MJOhcqEJAdhN7s8rmEX3RDimSv4vT6toh5i65mY65NQef-HhRPNqr5zXTltEHENOB1KF5hTJoSC6aWLakz47ofnCXPBMQsXIUkeO6nRZ4qmZjnLhZiuD011OZVmisnKBxlD81Jp8qPkLtNC9E7gmv7wf3ps9p4cT2OuiAJ1v6sxel2f3AVVTn_14EfC36TTUhmfBCVL_fLZ3G3tUZiCQmTPUPzBPbLs6EXbkvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=BCVDFj31uTxTR-wfNkSBSgN8XBYUX9agmeG1wHYrkaPJgUNqbOSB8R6wB6s7Ql2C-N3B6wk35Zg8Rl8-PCpu46oI0Uq6FVacAP1KmfEkQH2F4E6MJOhcqEJAdhN7s8rmEX3RDimSv4vT6toh5i65mY65NQef-HhRPNqr5zXTltEHENOB1KF5hTJoSC6aWLakz47ofnCXPBMQsXIUkeO6nRZ4qmZjnLhZiuD011OZVmisnKBxlD81Jp8qPkLtNC9E7gmv7wf3ps9p4cT2OuiAJ1v6sxel2f3AVVTn_14EfC36TTUhmfBCVL_fLZ3G3tUZiCQmTPUPzBPbLs6EXbkvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fng_w9YPebQq6ndTYkdx1HfTGaleihugxIE9WY22Y2JeUgG_2hoHWyd6LaltoZ6I32YZQYfRgvUy3dvBqAlsiRkNJJOX0ajVbp1Dv9iGWZsSkaJ3tlfxD_o9FlDfiPj0N-b87F2Vxia5cwggG6UzupkpgB1NFT8O6IytHDbNxz0Dg8ANcsT9qwS-8glgUHLWVHFEuznKVjikmBMd-3zlAcgO0klSOMSUW51EQAGA15SEm8y0t6bL7XOY-cU46CnmVssqEShmnn_NOKDX4W8KSD5iEsRjOkTt7xXlrVgmwwjowhBmx-lMqXtTmT7F0VKQoZS37UdOJ3J_OE28OodxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ECih-3ggZAx6yjrvoHANCk5d-_erolDbGoGBVTrO7Vmeoaa32aiu3xx7CAVaM_m91aCHJgsVpWV34A2j1ZcLlYKY8upd-f0qWqeJQnhA5xF4pa4zbF286A8rpprJOanSO8j08GMGeGJi-zkoFzkZZegm8ukxqCzEEHT295g1ZxsmO2UHaHYEuiiA-6RHa07aLwjYlvByWZ5MKGoUkOM_VW-WoYb18AkgmWmdPttS0ZEu8ysoyjXIYZ_LD7ztM6RY4pqWxkeBMtGplJVk0RBXCIPlVcTfDTmwN9lnR-_fIrOrMCtv1ySCaLN87Xn7nUcHdVfh3VXB5V7Nlmsc35uJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ECih-3ggZAx6yjrvoHANCk5d-_erolDbGoGBVTrO7Vmeoaa32aiu3xx7CAVaM_m91aCHJgsVpWV34A2j1ZcLlYKY8upd-f0qWqeJQnhA5xF4pa4zbF286A8rpprJOanSO8j08GMGeGJi-zkoFzkZZegm8ukxqCzEEHT295g1ZxsmO2UHaHYEuiiA-6RHa07aLwjYlvByWZ5MKGoUkOM_VW-WoYb18AkgmWmdPttS0ZEu8ysoyjXIYZ_LD7ztM6RY4pqWxkeBMtGplJVk0RBXCIPlVcTfDTmwN9lnR-_fIrOrMCtv1ySCaLN87Xn7nUcHdVfh3VXB5V7Nlmsc35uJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=dxK_oNCnDRFyb9JmvJK4K1Cphr-duvu_7nAIPFH8IDHlTGXwRRcgQQn85NQgKhP_JUHgnq8u-kDycH_3ohMppcM-i_QsxA1xXrYwRPwrPFFBDKInGn9luAkcAmW1zLCxt7PO97VofLS6A1DMSG_jGAWy05henw-tG4x3vsr6Kdc0BSx0YfI5fWWt_YpmDfpcmkjgQgBms4KQlfuteGgH6OvowsbjK69Td-Oa_SDetz6P59oPIFp0eB8S0wyx5INox75FHZwsE8H8FwVdbhxH6oZHPCvi3e4s0F_3Ej7qLpqMAX9hMPeQ2tPh8_MYPcq1k7e4LZf3UFOFsyxfrbKXpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=dxK_oNCnDRFyb9JmvJK4K1Cphr-duvu_7nAIPFH8IDHlTGXwRRcgQQn85NQgKhP_JUHgnq8u-kDycH_3ohMppcM-i_QsxA1xXrYwRPwrPFFBDKInGn9luAkcAmW1zLCxt7PO97VofLS6A1DMSG_jGAWy05henw-tG4x3vsr6Kdc0BSx0YfI5fWWt_YpmDfpcmkjgQgBms4KQlfuteGgH6OvowsbjK69Td-Oa_SDetz6P59oPIFp0eB8S0wyx5INox75FHZwsE8H8FwVdbhxH6oZHPCvi3e4s0F_3Ej7qLpqMAX9hMPeQ2tPh8_MYPcq1k7e4LZf3UFOFsyxfrbKXpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUT-WStPtptIQ78cWHTVVnOLP_NYNlDFlGE_Nah9SjolM32yMY4ZwtjPq7ZMa9X2mWFQX1HmVROoKkhmPiXArSGLZ27ZePx_zd646ACXLVNOWBzCpnAKrpEqyUKZ7TQ-_QpvwMF2hV9JoYPdVTcrFgOwvuQFUeefc7bCW-gsA8lIrcQGlDiN1gsBbmlolHs1HmiXHmfdeFj_he_UI2AfsKHs_BxCbyuT8pa3CJbl657D1IPiC7t8r0pn-vulXS_MPPsbiacsv1M_f5Q-2trY2y4G6n4GoNnKaRKvoFOGyj0y7zfnd40HZtwqcv8RX13DKZDfavpFgSBk0hXerPTL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx7haafs1j30laKDymJtybjTLtKJLTEcR8KhtjwFsLO3g3Py_S3nwv89cEEZPTmm5_ArrF8X14ACVf-a3hU-DF7AdiCSRZYxbNaluZjI1tSmxbRjT1u_4xnCN2esfbVwHG9s68Pl3lABsG5HCRVCKG3sMoZQWf7Bfk7cwPDQRl5DQDZWje5FLiLmnvJn5q64yEff7j2cU1s4TyPcsPx0uMrFfTWUtWbfNvAPn2o2ajzB8INd8mI-ZKC4i0LfV0fIpAr_5o8Irj6C8HUlW426wmnW9jKXKAGS8NzJ7bYoijS8COTIktn4XK5oLbNqviOu3og7hRKCi3KKqg6MNaMANA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=tXWzbrAUxvI8AnzCDEFccpy_pmBuo91WGoEYYXjfR9BZs6Oi-vYsIiSg2n1i_NUhcGP0sI4AIr_lLtphLk_kk283_QQB7e-sMyLvMArpSIJf1c_MV9B3oFl4Iqh5ZgIMaa9sRHiCN-HEl_pku97NOndt4-VVwc9KJvJZTrj6wlJTjSv83z1E-nwQYD-ZgJ3U9eBDvnhIXTMspk-e4-IKYB9eiIkvceArBM_-8AVu1LaEQGDs_NEu-RigUskjRAjJYdefQ9YJG3c8oZRSWYRWCYHBDfeugv7OqXH-nkjw4NOtaV9aUNZ-8yQoacfS-JfzZIiDCI0ufoWnY-6M7YokPwB22rVSfYnYuyPJcI0O0JrnZcIBo8xmnFrvs61b2gPTyYqgVEp_bImP4YDaH1jrnLrlVdMkz8WxDo_QX5RRZnAbZRt4iaRKaWhdVxH3XzFTTWM0O4SMbi7aZMsk0yGvR9tKx5wJQkBL1m2RStdCyvZgzgcx81VHZB1aL9LhOw4myXyGP25tHwEamOzHc331j7ayLgYI2-S0NNOAWUhWp1NLiuh15K_bl0KyVxibblEW42sNOMwo69qdFpaOqxGr-zsoUMCORhC2xr1WKvBMtlA2e_Ww3aZ-e8zHmHemlqJWGU75f2SFcpvCVe_ky27XsEA6-QDVwoF04N32GoZ3xvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=tXWzbrAUxvI8AnzCDEFccpy_pmBuo91WGoEYYXjfR9BZs6Oi-vYsIiSg2n1i_NUhcGP0sI4AIr_lLtphLk_kk283_QQB7e-sMyLvMArpSIJf1c_MV9B3oFl4Iqh5ZgIMaa9sRHiCN-HEl_pku97NOndt4-VVwc9KJvJZTrj6wlJTjSv83z1E-nwQYD-ZgJ3U9eBDvnhIXTMspk-e4-IKYB9eiIkvceArBM_-8AVu1LaEQGDs_NEu-RigUskjRAjJYdefQ9YJG3c8oZRSWYRWCYHBDfeugv7OqXH-nkjw4NOtaV9aUNZ-8yQoacfS-JfzZIiDCI0ufoWnY-6M7YokPwB22rVSfYnYuyPJcI0O0JrnZcIBo8xmnFrvs61b2gPTyYqgVEp_bImP4YDaH1jrnLrlVdMkz8WxDo_QX5RRZnAbZRt4iaRKaWhdVxH3XzFTTWM0O4SMbi7aZMsk0yGvR9tKx5wJQkBL1m2RStdCyvZgzgcx81VHZB1aL9LhOw4myXyGP25tHwEamOzHc331j7ayLgYI2-S0NNOAWUhWp1NLiuh15K_bl0KyVxibblEW42sNOMwo69qdFpaOqxGr-zsoUMCORhC2xr1WKvBMtlA2e_Ww3aZ-e8zHmHemlqJWGU75f2SFcpvCVe_ky27XsEA6-QDVwoF04N32GoZ3xvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUVaVk47IZfZ8LG_hTHo_E6zNqEEFw7AIKKKXh8Qjs2VN2DDhzzshpT2Gq-KXHt9lB9fNC69ZbbzYHW2Ux2uDbiaeSpLKYA2QJu1bgJCn5yqt1h1BPnS9gVrZCMRRyFC8D81eZph2l7_sGO_324WwetBeAmb5m_61sG92z1nnOyFGeWMUdFxeUg-3_qi1eN8ctpkqqjHXuxzNcUcND9I-unqL1H8HHcvQEGbgsvOHATrz9xzo1Vr3xv4JrEcdmiGNqYbsUWUJffEAhpJY-Qzrbt7C0IpJE5wM0pkM7b1i5RSsTQDIGPh_4kngb7dIhhjZeSRd3Kf8VfMZZcm7AXVEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Ga5BluwkZm5g5YITh_0y2y2si41LqgOTcYMT9J6Ms2JNzSJayky3R-hnrgNHznW7pQEdlvxG7JvUK_1MgysU7CJDYoDHsZQ6GXv0uixkK5vOB8I-tpaXCNjiIEXwH7Emj8WcRgQah9U5I98GQWo0Pq95UomAJ5rd6GEPSP93OBtVYqxeQ5CNT_G3az9bHjPlW5yvHIRZvm8qUHfcI3sdoy4EtZQW9jnYQF66wZzQGkwuw2qpDMljnif-nRsw7FkuvWPA1QJOmCzxTjQmuDqlC_fYLZI6nw71fd5UeWwXVoQiFcY39E5aeAVsSG-vAbzs5ixi7oeERyOKiVQ7QfBxZx_HSeef57amvgt_OB8EYb1zDg5Ob6P4zVSErLqquLtENBfHd3lGsSQ6OXB0W_XRC3LTkRmMKWpPK88h29EHcBvBK_VdWVZU1ZcLL1xJTJkHWU5f6nW6uiJKjAFZhxwp3I9HD071aWstbkVsfcKeki581rt4XwCtfdKw3xWDFApze_ArYKLwBVwhUBUC9fGAIpycDkmuXX_4xsin1C76BkvjoVVc6r8hNzJtejzMPqx6GjfYth4c0fZ5-bj6qo8Sg1PN-2sMdYpzvtMJVLL97JBBNU8do5XDBEWer6ZZYIrKu0KNH8f5Ojo1b1BlZtTHoJLXExfJsV49fJJMGqfry_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Ga5BluwkZm5g5YITh_0y2y2si41LqgOTcYMT9J6Ms2JNzSJayky3R-hnrgNHznW7pQEdlvxG7JvUK_1MgysU7CJDYoDHsZQ6GXv0uixkK5vOB8I-tpaXCNjiIEXwH7Emj8WcRgQah9U5I98GQWo0Pq95UomAJ5rd6GEPSP93OBtVYqxeQ5CNT_G3az9bHjPlW5yvHIRZvm8qUHfcI3sdoy4EtZQW9jnYQF66wZzQGkwuw2qpDMljnif-nRsw7FkuvWPA1QJOmCzxTjQmuDqlC_fYLZI6nw71fd5UeWwXVoQiFcY39E5aeAVsSG-vAbzs5ixi7oeERyOKiVQ7QfBxZx_HSeef57amvgt_OB8EYb1zDg5Ob6P4zVSErLqquLtENBfHd3lGsSQ6OXB0W_XRC3LTkRmMKWpPK88h29EHcBvBK_VdWVZU1ZcLL1xJTJkHWU5f6nW6uiJKjAFZhxwp3I9HD071aWstbkVsfcKeki581rt4XwCtfdKw3xWDFApze_ArYKLwBVwhUBUC9fGAIpycDkmuXX_4xsin1C76BkvjoVVc6r8hNzJtejzMPqx6GjfYth4c0fZ5-bj6qo8Sg1PN-2sMdYpzvtMJVLL97JBBNU8do5XDBEWer6ZZYIrKu0KNH8f5Ojo1b1BlZtTHoJLXExfJsV49fJJMGqfry_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB6wqZSPvqJWYfPOzehs-eXuIyeMTNqSaPoKPQZLXArs-6S3rHOiNU-Svgb_X3J5fXUg-ocNUHN10dfn3P-FaTGEr5FFcNgiIMsUdUj-4mZxg-NwwHBXzqf1yXYdK-a-3-7LvFTP3T12BIKQVwhZxq_PaQKJYxMF-OZXY_p82JgUFmL354qvhgtZ0b2hGwfmUm437b6jfTVUL3VG5BX6qTpT7XrSLJNQFA2Y2BTRIv_n6xMEvjCbyqPGQipmJ5hHEuDxmKHXCwD_CmxIwTzmOpVZPrjNXIL2q25H02yxK22w6uYwqrg5S6KVhhMVp2tzukOI40gsZCpjJfDsmSKpWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5E71ncev_eCIKdRha-OHKBF14VNlKgcETKQSHutiliwe6g3cnBjs87wbwesBca8bkBY98qNtQ81xxauu2t-5sKYPQRgr1fF9Np9l4PRnDfMh6acno-jk7NEO4MVGxap0YmnMScvdQDBX_FAr6CxIwok2uvgwcvAvdU-BQ0gGLgYUkU3OojHHaN4Yjgerzzh_OSPKY8Ap4-iplDqMeAf34caOtMS7x0-9JDuVCP29azVU0enWwvOBs8IaXFTe_Jr1xdLoXZZgpjwBR1CwfnVxnbQONzNc7XYoKfhTNfvGiG2cxTxyQ7DMYqt2ixQv9T19DEgEdugIA0Z25oJ_wcUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFZwIcSPxB5N8xgtC67kwRF_SFs5oSRxxeJedAB6CYkzyEKi6N4l9xmj1DITbAPzklXULvWeGGEEN9ufrZxE09o6JYmGuBnkmOUa5WaRfbltnwxr2lqL4ia45UIaCRWXjsKtB8b9GDJKqIJhIT6CTI-SyFPsubSPzGOpoIf9rpSDf3-tUC_3RsGsbjm49xNYObghkfTmdPvHEvfyBTrkuZu0C57wzgYqaL9F-bKzD22ZytS0EV0epNr3_o2M74qYERFL_Sqels7D-4MZeVAduumrLCtYKXbVeVKyVk97dnMwJw-G5hewhrO9pNeBH8aeO6PjyZgFc9yde1ePpDh36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwFbO3WNpb4fu_FbKwr1VGMl80IPgsEil5jioqdD9MgWyEXxEzD8iJ02qc9zR7mjrHk4CuhWYgCifv-6Ugw5Ytmz7owpnK2uP7vW4jQiRVwCY60umzonIElzpuwgKhfazsyu6kTNKedNDsx-aOhygI3dtG8TGqJo_e2U0a83ya_6yQeV6nnf25O6BeNp2quFT9jcYbiMHsIOEUC-7hxI5n9NvDcu6Ot-lGsDP6yL0HG1s4mQ6_oHbJedHqot2qAxqFcxCEv45iie-VQOItwuZVr4OiMfaOe_4KOY3nzvvuMP9aqRPSOq637CYIk2WMYFb_Riybc-aeHL2Xnj3niSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sau-fEXSo5_iWc0L_7F99lKisEFBQRS3CdXM8-lNkDQaU5aGXLuJG2IJiTdhrJtBxsTHkNUQtlwy-6Y8nNORZjb_BdG3d4EaqrB3rOXI4_S99bwcI8mZRjyL--8ay-UoqZsFmpyTCiNxPi4iij04zcQ-nnRUDTzh59SY8tOSrZAVZZRSeUl3Ztd__OCnhUPIBK3hkjG95Mjdr5UYWAe1atcVz3saQ2KTPrmd9vw_aq1j8c46r9DjOVqnt0YSM5ClAHtnNbxpAlbPfdmotYV1Fe-QCOI7ubj6UsuorYLUcunymalyUuC9GsGF2ITek3VAggEe8qjiYUXWjxa96FhXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce0otw0_wz9xZNGXyu4QOqRIm_YAurSBAU6ETr_PBB58LokdcTHdMsDywfv05iIUpmGePmmr574h3A8PVkqslfblG5rMH3JRN8DjrJhdVBQGvSQCQgFFgA6f_RQlmfdV1ZLFnGNfOL2ulNe_vITNXT3_L3IF0QVNnbduN-jt5mR4ivRsfBd91lzbGpVrdF5P_b3lSaRBHzOmp0t0HJ4h3JZhARTjmJKtCHOnOITwtmxfSwq7YWxW4tqPAZrI6Od90BuDMJ3TafzkYaiQgGa-wMwNPwIPXs3ehv89GKBi5urhuJg2UefalXrvS2IJcd87JCN1nfbXRemIxoCwo8dLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYeJNPfKfaidBQwI1BucIbqYIs5VGS4NVYxKlk5ztF4FYFfUgKyMfEAGwJx0fWESk5dSdNBj6r2gk8RhMwJIpFaF0p1FBgZwps9t92kBm-Eu6XbBu5yg0MFzbBqOdju7u-Z-URNsXH9azoajbJgVzYhBxw8zJCIDTO0NQCPudvaBt2Jp-VoLyWU66mVLInuC7WhXEayPM6Vs6I6oauWYvEFDLCI8IAJjQIyaKVxEJN1Lv4yo5uUPdl3YUy0GrWZmh8gvl6sHcH7rEbcyeIYQphX-HhMPkIf-Ao8qIq8_YLaFpz5dSzd6oUEsdHjQIfYNseJOIXcWB0SIehQ-lxK0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxrc2awxcG7ktzUQukX-KvO8RAsQk65APJ4DgU_DMsuCPXGowlAsDqaJ1XzjNQataTIuADYZE5P6qS3VOAprm0YhO5zKDmAYXm5JEvjs1E9jVL-HqsPVz9No65zmrrRRxWV7YokR01a3uaasItF5dxNPaOnJ42GCn2NnFHhRv8As1dc_93gO4Av41M730cbWRSbOtozuX2p-nk8vmLKWyNcRPfJpY-JPGr1OewLtQk9vBS_5QSy7Wli7JuILeI4-oxZ2zMgjmrOVBRqYWSWjimHG422OQbIvIEVHr_04MZedgH9kSk8pP4-sjsdV7lNrzRbunxZGsPCpi9HIW52uQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrRBmhIgdpGU3tXw3WHp9kynRuqkbRF1HsyVqFEvgQ2ipojg157TuPXjElfDTh0sDr3cSOPIdQx_7T-Jb6glXTXkbxxZISw-dPEOhGgyI5bp1JCK5arEtwCLgkCUmsgUsOgGK8_SYfIz6fobFBQbrW1WByTRswOfkBoTVbiH3vcql0KsWdgxYHsx8fOS8A4pQYQWk8F-eS_B--c_pOxyPK89-Wk78lMwObPuTAN0coszGNxzPaGY761Fk_puq__GilLQofY7rKo7AsMycuH8VnogyHHjOmCc4KoOgJW9GH2w2U4vC2khN8SW2oUZhbZprwp4W26fuvVls6vrukLczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlhBKAtNTSqno46tZpRpIR3nrzljlBSmbm4RU7gC9_piUpX6eLM3e2odNUU7TvejH_S0f47ERGGRRjQaqiV7sGKu2ki2XnbFO1oW8d-j_tl0A5MXCIRIsBGcJG-X7GmuQoxTx0LF8S7Wex7b5uRo3MBaZ0si133pvWtY8iR3Xiwnm2AgsC1pBXWlPvS76AfRaImMqlP3Xn4pQGVixAO9XH046qF3OAqW-82P24QX1m4wi_-XF2SF6UScDIHnmshMKN7dA_gpNTVyXgYtj370QNXcpgY-xXv0a4jhF-w7zHNNXwtHEWwhNZxvN9EYaDXNbuax1S8yaibZ9JEwgzsf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT_Zl0sCs7zA4tQfga1KonP_uyiVpM2spX63naRWJUr9WGHdfWlf5tMNHRUrYXIFzH_lUAA6lRxoVFn0HvpuxK0gjSC9MAJMYFSBjjXJOSnmEO07tFvTAmDPIs1Cif-RDl8fLWnWQeBCMdoPo2lXGAmC08c2ZB9W2SPrIKsSxh6F-q3e-WBeCWnDbbchrBHZLkHvpYwEnKJ1ne2QOItDxciX_7WsLFFW2zpq1KfH8cJ2b42qepMcU73IZW-K8qXWF46D0tMK4Iu-po8yJuuGoLWFJQif5AaRzamgTyQ7oWvBpsNtyGdOFsEOTSMW8lxgHxzJSwFlZnLObV3NlUW5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph58dusmtujoG5gqgFt0sst47M_2fPkW_C3exbJsWi_RVRZSDX4deWxGFA0aONrEFd5uuP99OpJ3FUS6nDPBYmOCJLzc0nsmuK00FzZ4YwVVzy4fXLVpASQCUjE1K49qBJ9zy9u2D8HPiKcLeMO-eRLnbU83-jTtdn2QjHHVf0sYJDnK_-PBF5S3Waf6GpT3FP78XtK3WKnqZyQzwvAjYNtFayi_S64suR4DH95MwiaKkH862_6sOuyDZ42fyqN5RaWrJASaspXzq5UQ2Aru7-6OFCWnQnORWdKxt3epK53af8k7nBwtCqlLDq8ozvIEOfnKWEJajphxuE1IxbLVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdhcovtkfDxETbGF9oFEx0PBBxmGqRq8zkIUzv2Zt9DV9bL_5s8EKXsOg4wS0ALYPioL8IXWpkyoS9cQi-vnAvm0ahsxkADVPHOv-m0uQmEIjwq8UjYrrW69FspZtcELJO0pJmg1RTOrM40K0WlVoZ5rOr42Q_RBQL32P1xZbIfndLqIstC8NWprn1mRpJNJnC9219UodKIkcntAKqWe79wbdoaEBvU50rB4Y1A_B3Uw7hGxGcOFXMUQQImfd6k7siPo79cVyAm79uANwgcvb7DzY1XABD-w0IysjmtFMyyf1WJoMt3uvIASChRHCHfgAv_6YSrTsFBda5IbvCMsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQhbC0WDd-0C6bQfbYiFfUkPT_70nGuus3W0peRQ18gxib5D96cmqiwtsoxO5WjlQLPVRNNG_ofhAAiteDjCHzSI_FgSgluf_jFeKkwVr8KR8MWpZqNaI_eSZqVoEGTe1FjIEqo7Khay2nBNxyMTC_KgNkqhv1pSf3jWUtVS0GsyCfbX3hRnTmOEO9_neyhpta1Zj6fYxNAm6ORfQiSIB2qW_ruptLyNJzalhKEsZIuSU7MDJ3XezCAI3yy8xhuWjKQVzoJwso1TKuVZ9lc120NeFXqieNxZ5296_ASWMmHSTKzaVScgYXJtmYcr-QRzAmuL1XhkhBGbmf3umXsVlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6Y50xe7aTJkfzv97UH8-cZhpH1frPGRYunB-fuDcv2lMshpQ_mVhJgHslQ2ezEBjuT5ffrXoWPLyD-fe3H5Uttw9hyr6i6cVit9lgxXpMZNkZGqOyjcjx0Atwxd0slBf6pakJkzKBCanPmIXBl7shMxsjU8Zl6TcdWCTfQcmSqfjSx_Hsd532UnLrrC8HEBBkAFf9T67xs4v_vlFAhl09h5i3mtS9tlGLiuHxXQXQuqpVCVSVGql4iEQKCbJODQBSkLRpskyF_QKVJfid6ocTYBrOP7N4xKgulycgWFepSccepYVGv6kga7tGtUNDP7mz2wG9IyLBJiejrdk3rLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRkAHCqRXJBMSk6UOO2wqmM5xgnIUKMWydquIGHN2TF2GnrbrrwyB8vzf_8zXQ2uDG_wSHYtBPGFsc4ekeT_k1OPPaSRYw3oqAtRO1LO-gVceUdSdjhETLGWfP0dlOxPCn3SGZYBmzQryI1JyHeai7ScI13e-vHydwhbVLiUKgLNHZ_atzfWneTMeAEjN_NNFkJIPmhGVrwOMrKUo14uPs_3Bk1zdJR4ykOLNc94BqWJnlJmjq9CJyJ2Dw0GCnsLJrLzAt4J7pjN7k-leipJWjENEHaboxSOTvCyuULPk7VwNGocYEnnHJBLsQvKp7xzlnjCRAZgr_VJ9fuQAdni4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEV_rMykZuw8V0VW3KYu9k1WB1mo9pNsXnIpvb5n7I4-R2EPSw6H3zHcvHf2QG0S4EhKN-FcYLlARKOeEszNprFP5RKoHYDDo2oJPokUv21G7om7lUjkL6AXjjstMWq4m2rRjWHk_U_Arigtt042pNPXCrfY6xY3ypnDWqXBbeA1OpUhANaOvaAshSgQO16lDEbL-Tv9RQSAE6qEv3fqDSBuLX0J3LYNZ4wrEqKG_F7q-fJzTytZ0BxJZCdgZVqwXHPSAY0LyscQdTiJaidWrOPxJLi_XhuUzLyc-L8hky-VNLxZClBZxZVcR4c8rzxX5xIB4hxKHyTHc97YgsvhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNKOEphZKAkktD9CxWFOmo82emhJe6MgLognLAUIiM-ZolLqmMmyawd4jEFLbL26Ea8vtoFK4v11NifRGMSiDASzMiQOEX84ImVRhU2RkIJIe_XO_CZY4ZXFZmpBtcOThkRqDjItVAT88hCiNOas7CC7BnPhVCGWpeUVQB-dWCrS8LWeusWHvA5T8UU3nTUarZ8pwGhzn8Zd5Jn0k-YH4yjhs7NkxNlfXgjlIT3M02DDJOKlZh08CHiIYKv0SmxU2TCloIYKlxlpI3qZEPLHWbXAeBGUvqf_6Vi9CcVLsXvQeI3cM6bvpvL25cBX-_DCnq5RknQ-VlTM_fkIOxgADg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwTB7V3G0ZW02Vl71pabaV7I-YxE1Q9jyoboGYClG4OTaXilRLTpZMYNHAJyFBQb7H3_EnOBKBym7wQIxSCgfs1z84bFnkLg_xkKf1w5PceUh-APH5z3_T2mdqeVv_jSCfRU1nzwob3jZVocW0493g53QsXJBjP74wPfk8hnpB4vlMxvL-4QKvTScLKfIuXHx9oSajFsMGLmc4Uei1ONh8v4vQlqjnwsXyCGoSW2QAnz1bf7Wl16UyzfMmhQl9myH0dN134nZzVpUQxCJJJLBGvczH8y0MimISuDIHPUvlXFy34QYhsgx4HzgvScZ5LUdiL1qDw9GO-dsW0fIyCtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkoMVsI89M6lGqTJBTFlb9rQYBb6-8gRELZryO24_vZlJhoCxMvfZW4YFWRg_MpjvvkzRp5sUHJZo6w8mWbdJHtlDXx2-a7wFYaZywdrs6NC5lYFiuWKHn9znEKcCU1op5ZsL66hWOqOYJezIiRXa11IlYEoD2NDMPgofGwczfpwblcPNopWzBDjQ8UmRPDmIhLyjmkjV3Re7zshh1H3FTQNKVW2EXzILogw2vjMKwL419LmGB5MzkMxxmWHIhyimjTiloujtsnNXMUqY7pwhKUUcJ5mTNebYU1uCsJWUm1sp7k-NZZJQOW0vhedsWklvVuRQUDDD-hOUX2iEdfnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8HJxyyFqyua236-G7Ms9IqhR8iJzfpMI0FnlaPgGiYc7r8jc_wTDnxhxqC6BP5hcAkm4f-r8BoTm8ZaGUFq8q-Y5uI7fxBmCXmCj4K2hZ9vrNNxotISQEI1nVGR6jdL5J0K_n7-IE66tkxtbbYS5J856UDJ5hjynhMTBkoef_mbBC_05fz9Pk8vp4JQlWkbqF2zywH_Gq7wekY-ctORoNT5JB4n3gByUqSct0pot6AXIoFwgvpXbdAkSORdlhKoOAfempshKJnttSklM6eM0kQIRlV04dh9XPueHw_Telam39k0rvwwlFy2K0Wo_Yur5rXSoHpBAzcUVOTs4FzY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL_9e2R7RN9VEnII0U91GQ9lp9WEwx_c_HHZe12jvBVBTllpmPjU_7oo9mO0l_A6qfLLZCyW8dBK8Q4qzSmb3gphmK7oIZhycloUMUefRoGTK6BfQs-KcCWW-8ptsZOYVry-w2i8jvwKo5Oem2b1hdixhrtO-E5W-cWaNqQnwa8JbAsOC2OnpsiL6uret2-8DzxIqla-joMX1HsPtvEHyhP3ylUkM6OLW8g9zRswDasSzhlCjxLq7sEvjo5xYEXRObffQ3NcuApWqO69p53QdCVvqHO4ogtN--Y1gNvlXdy2XMmPEosdG9IZr7f75Fd_DD0-bdbiLp5Xn1FejQXKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m24YISLxCjWXyScdHN8uXVYjFC25LiVKCURRUH7BK33a090CQ4AYyhxR7G_uvcN-olqKEx1fi8dujig7w58hx7OceZspC9-4TJcteqJ417l8Vua3cBfsHktsTpe4JnQQyeJ4OHo80rr_ygZhG6bX460bq32KovF9rt3SO89fr663gRlqBb4kbbQ9VQIrEft0E9Ft2ZDFmRmOcfgEyTCxb7FaRAq5ZYADAh4JaV7oJnapqgrmfIwM4ft8uMRt3nVO-MSk0JtZdcQh0h1tOMSrbiZgJP0W3L_pqO6B-tqjhquhsVx9bjcoDUwzjBUXbz63UMsmycVCqm8jkCjg22vOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtBDZEQ9f3VRmungXgtOnUfAm-UnhbmtXvDIHLUvcihwafw8JxXZwZ2ELQaegYEBRZz4VlsfiHeoz2Qby00PvsT8ySN_WARYjSSadqdBcXqtREm3hOlkAzoSVS7jZ5i18BF9-LxJZFRyxqUOqjKB4ms1qpi9BFwznhDJjzrfVs1xcYTDBa761U1Ktvn0O3RO7wZPD8p2Fm77U-5LBnzSUMlNb2vjYwmiE7cKEpu0tprfggoVn7Y-Gz1feV4rooeDi3rkM--sViyo95EVLkocKglCmwwfR06ImUbJvBWfa8sNw1dgdwQ9Oghaf6kRrY_fV0Vmils8460FFGUbJypx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8iCUXaeWOyJf8A6VZA8u1d46seiYIT6ReoB1FN9eO7WeAxbrMfz1mQwPTLcaX-vIHcDEoStv7itnE6a5ox1RtaN3XhbigUF5NQ6VsJPDJLPyjmY6jskO1F2em-Ip8LoMhWkYIjhPI5kJfFDa3yNYdK9cB-n-_gwhYdAzv93B3jkzR8ukWBKaqnKEHrMZnznSYCyXC_puUCFb-XC4RiJp0Guk9ZTeDTYRFU6IFr8jm9oyPv-nd5-jERZAq7NSBftqQR6npWCY_ARYG3xxdtbUKUVQQh7CduKysTaCxf62x8MUsRp-_8tueDrgMueEkxUqs2hN43fVPuEHLFz3pvffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH9TJw88AgqIexlQvelFk6hjVU_bKWNgvBii72tC4YN6zmVSMT9dCqYsl0nkz8t6EhSxOuW6qCwVG5k63T1miZ5_Q8SLGGxjhgxBQTFzVs_TauGQaNoNi41-L4ajPBqT2ysJhTFkeVH2qtpDSihVAEJgiKlv8KiohQnkJHwTOm8z5-DLA12m0qRxz9PhhZNTGDguTxvmmNW_CNHMzovQ8dSqMvIwo3N3z4d6w_gewDeWt6RhToOJgY2jdUE5bgKKQRfNf-WJslHDYXDH1JwmPRZTzxqoTxmxRymYa-C9RZGtjPF1h6eFUvP7ooUghzlz2w3ksyhs1OowZOjEQJpjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMknFuihRt0qHVX_7j9YBs8oPmh2znbie7_hqErDg9LzOX9lOEJYakzRb4_JcLhhYz6pKv-Ijq2RH83xp_8DW9jTixbf6JZ4l9voxijFApFD3Ah8zgC3pl4sRKBJ2lmenQ800GESr6BvUNOLQUKJx5Oiwy-pK3-MK9i-3Iw4U-_QreZ0YoLHQZmCn7iMMETGxkvfJi-lit62hQaTMjiiZyaOS_KYS16WfzF4WhARw9r5zRSQlP-2c_qDN0hHFJ4iUfWxWEdcPnznqTZS9CWEz1nU-7AwKXCcIRVI9S92FEr7lsKXEahb5KaFH3wYB7Pd9Qcnp5S57hEy8DMtE_0kOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pytb0o7Io9a7h93SsmsAGcLji3Kl0LkaYYpwOJTVTGnhXEjrYHFpx4GGqHxn_Dnjn2JtOI7MUBI_R87muCekFCjBB-ZiUZ8CLoT_0kBJ8JrskKQdOStObud6tIg_HbWyQHzR_g_kj6Q1XiDa1L8DOBDlsNHVOs4feOG5RRhz1-qra9IOZVYjoj8Kvl9Bsc8qaGJs-bBolzMjT6vabpvi990PnXkzzfQjDVERndYOKBXDx3tS7BiIwHB4CcB3_NOcC7Rlb7G6gAYKgMre8ImAMKH-qOWs9AAKsxTAaKMWB_ZFFBLofdpsFX0BECmNUQW80Sf4pu8tHjlBJBdTgodiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpDqIK_kSYzWniCnOgCsezSMC13vVnUWqYTRGAPhs0M5Ph0bl8jMdDh_5I_M8BaS1NEbtDMZeYfn-nQp-y--dr4eIl0BDnjKAUN5mqIRRZYXoCHg-vvEYDHeE8xh5ES5PYfkkSPk5IOTqTZZ4dIyrVQU8gr82qHfwnRtmtlyThTjUVkS5RTXMj7Fe9lFFm1iS5VJMfQO0EVxKcq_ceDcq_oB7M4tS276fvdeWpVLOb-R77alwTvpVgcQsHYipBStDNsA0jNdxiDxQlQohferwsSiowD1qxt10SJQNUtMk0Z8y2AfIdHfE2IpFwXcniPF90qEyY0ILYhhlREb8p-aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrGRG71ZnTWYY3k5BmqscN_155fAW_bcjO5wliR6RZKZsY2S0dqA8dA6gdYoO7mjlIlVw-cxxP7MgBXWG2sBnSftotc9PM7oJVo-CzwzkVRfPqs8pZw0u3uRfSgL6mQTg6vkzSyiPjBMH9KbJ0w4HdasfkbeNmyybN2tj1sm_sSxiEB7iSmDXfSN-svX9fywD6IKu5txf-HsG3Fv9R_Y_s40UeFlO9wW_x1JnMZnTP585TBBfgIEAbIVpnTz94hLYDfCFvoDiOokPUTrUuHnM9t0Uhhspfpc12mtffAmk7BAFXHGVvCbnfY-Rp14p7B59YXYA1Mge6hz-yQ1ima4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-sWN40Mb-Dfvpp09Trzut7mlAzGs16NtaNWjyemXoC27_XShtvcavTKTAzMuOu40RAUlJntAmg5LFxDI6w9N2iWLbODVjUqnJ21G_bxutULVVfvu9KUV5cYHIcLrS7Bfp9hjob6jHBXClmrt4oQc_j0H66GmRODp7-yazgUkUUTs3Do3fF8q9YK_SAWdomSmVc-D_tk-qomfYs43LxQyi5TkUO75wu2yr3hTEvZ0gg_h-ovqW5paG-ORvuHLN5e152SD9S6MNXjMogzwZ90PEei9ivdsVjUKB1OqLZ4St00a5qUuHSdITSlsFrtmCa5lWqROAqS9jwH9R6owXrorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIFIITYy1FuT2OOrzjUMcQXP7mDlAlixgwRs3BLTPjtqlnJ01wQvTLPp6I9Q-gv6PjWb3Q5a-8FPQNL7kbI2nO8FLBWQeM0aqrDazfaIjFDbhx1u8mDy8QH64kzbOwRfia-zfVL_TT5gTHsdWoPYoQoaPNDN7hybpfHqRS7sF1ALkENLuODApApOtuoZFYQkXWkPgCE5ZgfPH3JWVJ6XySGrCCl720X6_7Dy-6gW38xLOGG-G4Xl8FhqKGNlNFs63h00Nbh1_J3NwZUom6UpvK7EkQre8WwE7umyguNPzcrl67q9-Chbxo-x4RaPs466_eM-6pdSleyvl8fYN_Pqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKjhetvCOUjNq6EBXOewoBhZcfhpFpT9d-xoNGL4Sdz6HcVPv9bu8HhkQnOFvaNZA-fzXrSsj3T946DveUVgU4D3lh-KK9aUEFVC6RHx-WUU5wC6P9y5E6eK4KspmfbbOJragMEWNaQ8FEW5PdNXLQhpFIfBSc9YVAl3UuA6YW8RjDesiOToj8GcAquD3v6o8hCrpeMAz6Id3YKwveJUSMT3kC-9MUDWbulqOZbSYzaH3RNAZ15SDOMPeBVLqoHyjz5GefEGyJrZsKn8l1EqrgtxKFqieVBxp510fs8jdNp6KyIJUP8ebye3QVNZbuZyOTXRQt5UpSsKUbSJALEuoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0R-lrHtH85CODdoXNkELVfoVQPvKY13qZi3oaxy0IAiHhc5OuY8nJqJQZC1Wgw0UgYnY8uIZTDUIJbbbfEXE8T5pxieAOHZFPMI4xe_h7eCJfzgGhRYkyxLC9MlVqO6DdxjlK6on0R2TdR07SiPLWZRWil39sX4FYsj7C89tjdjPb306C0F386AlkKQkoSA7S1B3l7-KuBqJkfHmbfChnowig14GHEWFNxhAVzUGvIXx53kIbhJ3I3Ag7tJIcBxgKQR7XZOApjFqrPsw-e0iQe12PPfEfAcPS0JRpyZ_OttZhw0Ci4uQxLWp3oQ-JazidqY23eiGMuEe27dZuQXHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PKlI3bw6enzpmnsbrc-euMgklRPZniXOIECc2_X6ukbEojp8_NCkZDM-zQCFe28zOdNRv3juHdJ2ar6wRhm0bEnhtfVVyTh_8vIO8Uoc_fxUli8Ax8C2A-Qg7FpjcRVdu2FJhn0xPAoim6PIr8Ko53L41EIa9d2ltVDvhF15bI-e4Ae06LDNjpdthvBAKqtEUU-Ne-dha3v_4XZ5NfLNw6oEcSut0JuELwqyq42hnFqY-_B6MwCGgzf_c4SpMgp6vTAaf2rfQNw3ZzPM4dSZk7B7U98cuQhBUQBCDNQaJbZ0CARRFvBW3yhUV2T9uWLKv5vmTbt1MQ84PjmG8-uKdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PKlI3bw6enzpmnsbrc-euMgklRPZniXOIECc2_X6ukbEojp8_NCkZDM-zQCFe28zOdNRv3juHdJ2ar6wRhm0bEnhtfVVyTh_8vIO8Uoc_fxUli8Ax8C2A-Qg7FpjcRVdu2FJhn0xPAoim6PIr8Ko53L41EIa9d2ltVDvhF15bI-e4Ae06LDNjpdthvBAKqtEUU-Ne-dha3v_4XZ5NfLNw6oEcSut0JuELwqyq42hnFqY-_B6MwCGgzf_c4SpMgp6vTAaf2rfQNw3ZzPM4dSZk7B7U98cuQhBUQBCDNQaJbZ0CARRFvBW3yhUV2T9uWLKv5vmTbt1MQ84PjmG8-uKdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh0cjJ4gedcTkqwfWKatAYEwC_skFjNBVaqdxGpy5-S8-7oNM8NHUSHiz9uSdt9pVbeZxr8jLI0nxi3Zx1KDmf2ZR4JDM9Mor3MxKhQRwDpFv1cliwygqfEl7pB57QuU46YBDs3DhdHoxwoY6lLR7wKWjVHkhmIKj4UhG5RoOyFjKsG7V7fnl8ZcNu-Ixx54Yjt94PSPY4XovsDKTa_GZNX0HpApYY83EutfTJ6FzXJAwWrex0_55OUDI5BBP2b38pqC0sfI2s1VtUtG5tvT3aaDbwp-zkY39R2LnavClgrOZ5L6M-JUxRUL1niEO3AO_DWjr6aaZ1STbhG0mBJSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=TgSj52vJTLqNnwA1RN2rsfbB9-yP2CACnt08V8i9cE3LLwUfxgbp3hGnuxEvUVAdBbNuZzUCOr4LECzYY4lmHhAVe7xVxeTSxaJMoEC7fpm35PGTy2Jd4v_Q0Utgmgkn8B7SJL50uPXXSNLtmzCwYjjlGkJRuzSxmLqhg_BkXFa8mWp63VzEutVcQKPXBYaseEjjhtWjeIQ_rxzCf40gT4zI8kVZt1_S8yfBe5M_S1Z7PLkKe61vtMG6v17o8C6giH7UU65CombYoZcKvOkvaLT248Ou4Vo8pt1Fha-Zxb7WcQPTRNJ31i4e2E3rTsmJQWSC_LZwJo7QjTCFwy1ctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=TgSj52vJTLqNnwA1RN2rsfbB9-yP2CACnt08V8i9cE3LLwUfxgbp3hGnuxEvUVAdBbNuZzUCOr4LECzYY4lmHhAVe7xVxeTSxaJMoEC7fpm35PGTy2Jd4v_Q0Utgmgkn8B7SJL50uPXXSNLtmzCwYjjlGkJRuzSxmLqhg_BkXFa8mWp63VzEutVcQKPXBYaseEjjhtWjeIQ_rxzCf40gT4zI8kVZt1_S8yfBe5M_S1Z7PLkKe61vtMG6v17o8C6giH7UU65CombYoZcKvOkvaLT248Ou4Vo8pt1Fha-Zxb7WcQPTRNJ31i4e2E3rTsmJQWSC_LZwJo7QjTCFwy1ctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5kPx5bO0giMg3BCkKoUWUMmhKACP4iArr_4_v5Fgpm2Af5vdFdBky1nVU2zY1qxkx1d4ugMzt-S9xxdyWI0k4vp27pGtSDSyqhnhEPRXoCLpmB7KviXxZp8Ben4Fg89Iypih0otSQulnimNI4b0TnaZ7hAnb2AgkBv6at_-f7vA3UPipmvhAsQb9HgM-0uRF2hfQVqvcUMU3YwNE_ruCdMVZdKy5EBYxcxHQ8OrOph6NpYTEQqKhV8lZlyz-zvBzOrUr34a18Sa48Z6z0xM7EFRK8FdtMTD-7AXvbvo4YyAbYJen7jT8LS3vyx8iJwUvQUs93MQcxuc6dU4mkKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7rv5_hn7mpa6Ylfl_zn4tSRgWANTkr3DuaBYPNouYhwf7X1zKFE4L-7DqzqfL_uzrBiIvNFrYD6PBRk2LRIM6fIubOA0_EGZJlCsf2G2Sz6NdzSGw5fJ6Ya-tnWZcFcJ_AmmMZjOxHWaTpjSYO1Y67zCnMu2rrnGZLpYRTR83tiQ9Z1okDXNGxQpj8e1cuumiSDk4SiuVPTIY5OeCYokOTtujgRgAHCKh579pDGaW_0gQuwMbrgr2Pk-2pX906VLFAPa3KHDGynz39ifqUIFcRriqZf3pKVzrxAApaRuxmUwg4Ke4I-pAkVPP2GIu1SW-ljd7JcMh7PdTg0qR0UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=jNjeYhQS_8vqfDw-MC_jCbmZO6GIx4DlzktqV17LfBRbd6LILKjO0TJY2OHS4SD1nCJ6CgdWP5aeifqyPnL-GRK0-HaG6S66nBGg2Mok5Wm7yNX7dY8rXzTCr_Qlj5Syh2-MNVl0Szvtru36F4GBKxtfn7klZNtN_Y7iOxXyka7qF2iWKpuQfveIXzunePbED0cLQQSGQTPT6-AscJfdimZIBZGVrcmjRTYp3EdFN7f8rfV3fUeCw-VDA7MEIf28HcLM4E4jXGLQdyvbpRXXWgnSBSNhc-njNLhdEVJ2W9uf7q6950QmmGDYnMgfYQlwt_uv2ySq6tOmfo0i0AGWEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=jNjeYhQS_8vqfDw-MC_jCbmZO6GIx4DlzktqV17LfBRbd6LILKjO0TJY2OHS4SD1nCJ6CgdWP5aeifqyPnL-GRK0-HaG6S66nBGg2Mok5Wm7yNX7dY8rXzTCr_Qlj5Syh2-MNVl0Szvtru36F4GBKxtfn7klZNtN_Y7iOxXyka7qF2iWKpuQfveIXzunePbED0cLQQSGQTPT6-AscJfdimZIBZGVrcmjRTYp3EdFN7f8rfV3fUeCw-VDA7MEIf28HcLM4E4jXGLQdyvbpRXXWgnSBSNhc-njNLhdEVJ2W9uf7q6950QmmGDYnMgfYQlwt_uv2ySq6tOmfo0i0AGWEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
