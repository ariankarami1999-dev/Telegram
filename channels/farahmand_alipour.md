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
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 03:42:57</div>
<hr>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iKpEveoCZ-2CHdIhIurgC8wRV-jzus4yRW1woM993tQ2t2Iyylxb2S2wAyj3oxFPRsO6cLEPlBrtr3gLUTmNMkW35roWKe3oOT7ZEbqmb8lKKrrY2mgV_lWgMBr1xF4mM2QiE0ZRPzU7bBzI2qcQSVurOJ8XehH_6XXzL5Ks9Qxckbad7Z_YACv2n8uaRf-6JtCvuzxGsHgP5drgjJP6_GW0VYa4XJx362ECGzjGEFkT-jT6Go_CydmYBp0mKzHtdMnQdHueX3g8rtObAObPnU3lDSv-4NkRCDCTCBetuubzZjb-tHZABtbZd-50fodHlK03VrJQWLvpxZC1_2rR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iKpEveoCZ-2CHdIhIurgC8wRV-jzus4yRW1woM993tQ2t2Iyylxb2S2wAyj3oxFPRsO6cLEPlBrtr3gLUTmNMkW35roWKe3oOT7ZEbqmb8lKKrrY2mgV_lWgMBr1xF4mM2QiE0ZRPzU7bBzI2qcQSVurOJ8XehH_6XXzL5Ks9Qxckbad7Z_YACv2n8uaRf-6JtCvuzxGsHgP5drgjJP6_GW0VYa4XJx362ECGzjGEFkT-jT6Go_CydmYBp0mKzHtdMnQdHueX3g8rtObAObPnU3lDSv-4NkRCDCTCBetuubzZjb-tHZABtbZd-50fodHlK03VrJQWLvpxZC1_2rR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQwgQB6MUx0AvbGDorc-79rjQrwJHYO5L2YVPTKQKvKGyayw4wlBIXlIanEw3WGHi4ZwVhE_thfstHPg6Olx5bICucdDUgxEhseKg06V3FnYtYj1O5l-GftaXl3CD2-UyG76i9XKt8Qmq0iazv0sGeE5WQelcbMM3GTDvry7BEwQFA5Yt_mS2LPyKezM0N4YZIAa_8SAjzIbLBl2EbaVHHt2srOuNsKyLF2tuHjFnJCh9zRNv4l8M-_MySV4DoRyqqMQVFlDFHtJf-BSsO2VfcJno2TeEEnJYYa5Qu2irTFqsuMtu2adqi7x1TTB-O1BROejfh6Frmgt-hISHXJ1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTTn2Jj5KHYC8RLPb7aSDcF7aqG47R2kW2DF3V7v-9m7DaBht_hyBNl9WPUBJf7YyerXh4p2OOb1cN0EVIUoaET879xoy__e6LPKXUA0E25e0ANmOe9TnrDyvpIl9D3AhS2_VtxMmWf7sDb_M5sLOK0jw7NOB9WDd0RRSl9ODLNiFhREAf_CPypjoaPObs7MeN_btAZGc9KO3gn3GQgxNZhHTKVDObS4q9XAAnHMnzyhUdcVVfphlFPuWB8HAYrsZrsCNeGm52Ie-0keLZTspsXtnXK3KUAmMT3zuufxAk7xyrhsfCLd16_6id4FbnjqujrlyWD8wDL6S8lmA0nnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G70VWaEQBxEcwvi6rMCkkJkWeBJEL-Sea-H_bxf_OaL6VbGpp4fQro_LKrkZa8YgoVrRFkGvP-8yOUQXNV16KJHxP_vt9lexm_oXzl7bHCqq8yBcpUP2DzgTKbSPYHXy0frysoE7i8ZD28QGx2r9uTM_Btq_YpsJjYxxxrq3POQIzPv_g3tBkg9TYFJy_QKztMLTE4ss50teG6qCRolBe8v3-qYpeHE5YU-oTwniFUdTpyzxpAIo5ISJjdoCo0wfXlFkfLtZ12EfFtk5aRrMV_1eDhJtctJEkE1SjQbtvJp3mIfD3WXV1txD-W82lHgK-qRzI1XYcDY9HIX4C1Uzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5WgF6BaSGs_BCzcut4G7peSBQtKhy2T7mr2EIew1qHcr_ZUW9GxUjb146y2Zyh_6t8V9dBGenU_CePqRNwyZm-rvCaqYlEYHQpW6-pqBHkK5KfV5ETPs2Bjqr1VVsoQE0Bp0eQBL5Oh_zi_w2bUcANp9xAxWz9DzEjLQToJUyepLqKHkq4QnYU2CTUyY41LWJYPzdfsdOntIrJbAq3XO2NPluMfAYbWWaPKwBjlsQeiIksz6uryd6RD97aGU5C0TGxK73Qbw64BH9EYeTYpVtudPf7kiE8f7-lrvzvggaEfApr2_IZvEla2C3GdIeCvylcvzoyrxkr6AjYzDQ3HMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0h3gujJfP6Y1yvTQ9jplx8LCvqNyLo3cMaIzKL2accxpgIlYI2LgbwoBiq15taX-0w1jDeiRE50CSTvwyyI_7yv7CXL8HEDwQ37lBa4dwSWgmNHPyEtoz-U7OBQIbrrkYvZdmOG2reLJ2oLeGnQFoAclY7F6mFey79KrGpSVfCYqooILX3U45Tck6E-zDo3siaG7epYa6sG3hiJkpB3bA5-mcpniDWh5kFPeC6JX8RS3bLgJFTfgiGu2N5MDscx__ILu9NNezDt4qxALNuGedsw6idyvBBHUghi5PhUV3qiQGXoqKXBXGaSQlTaZFHNW3ml7G4IFWbN-ZFbxHQc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMIuzHJp8QYZ-tuQQyQLvdF4D6ZcQYZGKh5kUgNhm9XFYRA_mO6GU3df1qCyR8_kyZcbW0anC3Np_BSsRTxzMJlpES5wzqoHVy4RNJvHjJ4MEANUi0HocILgwr7f68jcEY3J06I8CRL_uaBVf8FeZhHDyDIeY0kwk6hhpeTdOKiLUeU4nf5kEiBRlbMFy5TS4KcE5_eDrjemdVi6gsoZTY0imyx2_4S6ZhnXngeGD07vH1h0U0aeeX_x76krlv6eAGg4j6Gt9f4ZIKFuG3Zs8EiPV0JuxmwTZeoIZx_-jPXA_-DRrKCEG3sQQTBBAbtKY2wBeLGuLWJ_QXyJKP30WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOXmMBzj1gtPL767RKTF92jto7e8cWxFLMPYeONe6lI3a-pCrmTnKv6xwd3pEhevMC2JuihD-WohScw13uRH7dUeNmWaNumzWTX7txVzRQwJEz2zpltW60D0soqLEdyGDXWhy1-ablGG6_-NBf3-SGSvf99KbId2ger4exy46K9K0S9lVfvyEwHVGRbenqpCEIchMhCMym4nfJZH488RaZJ7uzZ3YngmCs-laco3dyrDgC-W9zL1qjzA-x3h5jxzYVrkMry6XdUwmjVao5DlYuxLL3hZuU3BT0fb3U9IVsnp9fbbIUtZtxTCrEfX5eKvH3WYgvDpu53SN--vMjt9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=SR7aVQkijVb-AXTFNs3C-JLtkBI2FMw94xy9TfTjhABs-vnq7SuRFYozpuUta_18k60uKbj-tVEFqksc_b60KC9TFjoPIbqnvzPRgNeqqOGkX8NNTxJOv1-CZD0ABV1bE9Wr800XKUwXejdMq8uKCXiQEbC4JB8CxDPkxUKY4sY84eI4rW1_NURQYkPAIr2oe-nXj8k95E08qOVXpNdQJvODlF89UPSM1UGxjkM1NaeCjQkhsJNXOrsz1jDpa3PSPtDXFJeYaZtabKPnctnkwhvNrlAzJk8qKN-n4SeFR94eCB7o2c_90vLicQc9fPMhh3xi2tb8GQwE36JJ7vCNYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=SR7aVQkijVb-AXTFNs3C-JLtkBI2FMw94xy9TfTjhABs-vnq7SuRFYozpuUta_18k60uKbj-tVEFqksc_b60KC9TFjoPIbqnvzPRgNeqqOGkX8NNTxJOv1-CZD0ABV1bE9Wr800XKUwXejdMq8uKCXiQEbC4JB8CxDPkxUKY4sY84eI4rW1_NURQYkPAIr2oe-nXj8k95E08qOVXpNdQJvODlF89UPSM1UGxjkM1NaeCjQkhsJNXOrsz1jDpa3PSPtDXFJeYaZtabKPnctnkwhvNrlAzJk8qKN-n4SeFR94eCB7o2c_90vLicQc9fPMhh3xi2tb8GQwE36JJ7vCNYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVpabwf9_McNrUp9dJX2c1iB8LclKjsBpKBpv1n2u6BDDbxuaXwYJLHoPmA2o0TqoMfUG2Ogp7jTLV3I569vac6ch05MgBfpJP-UjTfag9j5azddB_9fziFUZhxE_-Vq268cNv8qh86miXHXDMn_B4LI6_Q5dAsKUOM2XytGy5FX7N4pF3kZ6lf4d5HG7decP6xKirylFoFx7jlueOyttAQ0eUr5Z9jXO66u2phywIEgRa353wY6qkZmERWr8RTnyt3qJ-jgU4AfQOXisYmnbzIvWg6nDBDeDFwQCrq8U0yuVK2Sy5vhsvkAR74gId8B4A8xprgs3wOdoI_biDoKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9yMxCpoGQK2p3flBd3aoSRLp0NCKdvT4LtFySuE5smndHl0Dz4JTED_FgCZPdjzma_8l1OeQpLOPqe_A3PZkdguDBK8QL4ddD3EMEOTMioWjWx0jl0iq_ShqSWFk6hJqa-xvjw5yYBd4ZO4teakyiq0GhQ7pe7vVbhSBkP3YYE1Lc3ywGu3Eky6r-Mnfp47oXCBp92bAiR3XQDmabwfOIbsNz3c5XryVID0llwZsMwhxyt9Kodd9MSP0NS0H3yPxAsSNR9iDoykL_TQq8gDptmMfyFkdnInzYVDRo826uto8MZuT7BmBZfHPp3r_q-p2v2DH_EBxaSIssU4xQ1kWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=F9awVBO_MAFsgwhX54sCy9WEukQt-IZy8sv0xJmyRH3r0eLkRnmlaAg3k7FpsHP_dyYF32kKapoVLgkFq4n0b7sRJFC2sTAGaKbWZ2SVC_EqSxENnMCmxSU1vZjst84jKzBXGqZG-QeNW7J8-szzUuoN8Uez7cF8boYsfCixMUTSI9v94ZLHhheHD2LV3-KoRU_oWohUV2OhUnVark6kFIsBJ4VNuAryVdeULdSw6_DBaWrCpN7TTFj8rXHSHBRP2Ts0JBd3LQtfOAXgVK4HOxZMzsbyouYI7rakjwOqxvRD0IGieEECexluTjzBWqJB2ySxTtIxnAswDLNe6BMqYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=F9awVBO_MAFsgwhX54sCy9WEukQt-IZy8sv0xJmyRH3r0eLkRnmlaAg3k7FpsHP_dyYF32kKapoVLgkFq4n0b7sRJFC2sTAGaKbWZ2SVC_EqSxENnMCmxSU1vZjst84jKzBXGqZG-QeNW7J8-szzUuoN8Uez7cF8boYsfCixMUTSI9v94ZLHhheHD2LV3-KoRU_oWohUV2OhUnVark6kFIsBJ4VNuAryVdeULdSw6_DBaWrCpN7TTFj8rXHSHBRP2Ts0JBd3LQtfOAXgVK4HOxZMzsbyouYI7rakjwOqxvRD0IGieEECexluTjzBWqJB2ySxTtIxnAswDLNe6BMqYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=IAFPLjJJ53G0LnCdI_UrWb5VIfbZuA1D6Ckqa0D3R6EvlMckRjFjag85FgH9JsliRdxeRiNfbnCyy4ClskQryGYaVJiwTX3tXAWSIXOCpkQNpn8WfPe4qpafVIs6KnBNZNn7oH9wHPRzg8yfRJwwMZ1Bn48UWRwuyAWfItALvsf6Jfu9PaF2_R69HW7gHfDloGCttuUDKf5mU9Vf2YUxY3tzDhpP2OO_zEpL0BmNYD8Cmspz6NcTqcZnIuEyh4HCkaJA_oHwDL9GOp9rtuemRFnUIckchnqghLKtzvZqRm8ADeDeOmjEolq_49UTw2B3KAtfyv2jY4a0DwrOLyAXpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=IAFPLjJJ53G0LnCdI_UrWb5VIfbZuA1D6Ckqa0D3R6EvlMckRjFjag85FgH9JsliRdxeRiNfbnCyy4ClskQryGYaVJiwTX3tXAWSIXOCpkQNpn8WfPe4qpafVIs6KnBNZNn7oH9wHPRzg8yfRJwwMZ1Bn48UWRwuyAWfItALvsf6Jfu9PaF2_R69HW7gHfDloGCttuUDKf5mU9Vf2YUxY3tzDhpP2OO_zEpL0BmNYD8Cmspz6NcTqcZnIuEyh4HCkaJA_oHwDL9GOp9rtuemRFnUIckchnqghLKtzvZqRm8ADeDeOmjEolq_49UTw2B3KAtfyv2jY4a0DwrOLyAXpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5Co6ffXVxlzzCcx3my6JN6u6iFgET0r6lIfAExaMmApHxMku1IMfVUO3-hx28CJOhb2sYsWn4y20KJ7CpqtjHZAYlUpvoAzjTajpudH0WlE145P-GRcGtHLfYo2k0i6na0JW8v-Saf-CHPIT3rbbIik86LBgke8U5KGrdTL3S3FEGad8wFFtk12ophV43KnsJIjULyVNxYe0etD7eZFF8aCevXE_nUVTq4qcGFKBPeYZ5Y8LPDNS3g3TlsEfba-KV2R-rI6olliSwzYIAxE9vRMCfKFAA_7JV6MtgIo5q7ux_HmkT879LOc-M4lGM52udPe85za7FcYm7IKqbr7Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHm4CvaoENjVNGT68RyfK0VBQNL2uTyRPhH48Xt_YnEtG_qjLFkjbt5LDOvlLZD11f-5hRnS04g9kvUYZDWDEQ90Wg-5me8GPDTzMOlwM6wIeLp3sWCajLXi7WGKiQUSEgTzR_B6E_nzPANNzeFs1kvuIyD7mlc5nMgXwlgMH58Znpcuj6sqMex-3Gy7Nnodx9cMb-ZJ2ELvWVAtagJImvl1PNv-xVxS8-5Ue7PYNER7wXwZy5JI-PsOWbJfzByInNKUrQz7_8pT0SsTkYOoKM7mfbyt9rSFWIPEMw2V_mD1f6LRQezs_tpw1FPIml5Ew1nLV4yGgbcOFnDoR0El_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO-aAQ5YDDjCUagD0Fl9Hi8XFTT-cm4qHfJgCypIkqhnQ8NC0R3YIpfFYwSKbW_9lGUj02oqKFVfkNs4WjjAzeqzyX-lVyDxTXQwWRhEtiSUcA5yA5pBu19dXLJo8Z8u6zJKtGJsCaWaVxm4hCtYs29aft5DvC5CcnHvs6FiFaXM0gXoXvqUhesvAejWdVrdvNZ1V5WxMxb7WkZ-nwBV426ko_NF2pn-3mS1z9um8AI6pgUnC5vjQt4o7aJYu5i063CbCP7VyeYWXnr_lQnjmLQ-SVVjWSokrqCt4VSfB3Whsp3COoGz7A_2i_4OQkra5XMGqO-N6g2q6HHuAt7rgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNFPDHkQ2NLUim9JAiqTM3bwMEWifXaMcg9px_ADvTwbezMdTCvOK_bTIWf7XzEWZ0RYoFWX3QPigK8xfLL33lOQtTSe_8rFgFN2WlGWb7oXFHSmzMcmn9ngykYPWmYIuhx7wEGNbhfis99aVR_cmErN65R1J_a-wJ0tBmZT_aLD44wok5070yRcCiLtlmQwO4g_XQddtK4FKDH6dunZal3pz-Z-ogMjfy77HFnk_oBQhe25tNPRxGgYcS6bvWiEurud4N0V0b9j8U0HVsCeHvAiT9XDD512HfKINs9F1HU72imcEQ0OEDXOZHEpU-QoJw2QpZ5upNU1HLwZ_YCNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMEO_IVxow2e9yTpsOii5GKKF3gXBFpkw1PmmXqdsQ76EwGiWzlRr7ikNSmUP1BXqSVmbYyT7ZuXyFAuN1LYA0a0P670EXTwE-olHzWBXVpomDiPmnZcPshSBqU3Ttsp5Iu6i6kCZczngu1mM2RqhrQjpOapR5ZmFQlScvFCeIapq7426i5uEzVyruUnpxfdKx_NU8ziHRZDvVtmWBYBmtIiVDX8vxn1tEfJRx9BTkFXE_9S52H9EjQO4QfC3wDfEpxxY6C7PcFGu6_tBs73uMU3dM1HKcSEx9j2h6fqk2yNrbt7Ib2hj_9wGUrTDkFgDNetOSrkzS-kdtOWp7uKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbJjmBpRrfT4kU6ph_c_mL_LaTZc58AV3nYwMT7ALY8CE5PaFwuuupIEX3TcpPTUh-eKr2zioaCOSPpHU9o7wUnw6xUGsf4pjhuRofPOfNJ4f7emh2-E2zC0BTpTakY-f1PiCGO5P3A1cHNVHv9NBfVOUxOYMjmVdTRNYbM_ODFvYzQOvdNrhwPMmu66nQM4QQ4yo9yO8ez6SfnA62W0XPYC-9JreBzg8CUi_djd37avCB6OfjOfGXvyEe0JS6TYAh2-e3MtwtV0GiF48z98r4DlSKdKohnJyCsyDQXH9TjcBY_DPzUFqY9JkJdHKg8DNjid6vnwL7Fn23AOBDxKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgYoLP6lleRK0UXoGbVd6BBUA0CJs5D3CEsbQyTfIS5-cjuC_imspMKVo7mcb0VO2vMTORS7siJinT-gFNsw0fnJBBp16vFri3fy9Jz6yZzSjeCnHWtsi_3SJK6SzD_kZdPmTIvecQj8d1ZYdJuLpzDbgbyOX_TbJxl4ZzwyagQ5KN9LbkIkrglbhkbmGZGJUONKoYqGZ0E7K-givRpGyYCGKH1Sy617QULQ6Gc4vqjHMtyggHW_-KuXNUXwqAP0nlEmLrdfwTNqGuAW7hYQHoPbKzmYoFiKaX4L0mEbeClhdn7whHUEnMqgKpLbBT9b4cm74fnUKOp7VfgwlwoLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=W8MrV7_CtuoAWf3jVVhbc_44lm0iSxM6mSZ657Z_9KMWlPfx-I4EKMY4tUXjWhF5UbuJt1X5j5CdoYkUs3cZASG7JWW38gPQn0EVJ6Yd5omV8UTihPvj3HA9W0eXOWdMF1EPBLRTzT1DUWlkeusetWSY8CXcx40gkCy8k_udNHrBuFVHJNcluDksHf4tx84fYsZJSX0UaUtpQv0FCDNZSqsJ9EmQp7L23Pa29XLQ1BbrhhothJC9UtUEOHsHk5BG0XLOI0ZP0mh8kxzY89Uv1XFT-EmSrdYQSC09IxAOtNo6bbt2kxWjiQ6uQKPC93Xhc4H-9NSCcjpHB3HOfB9u-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=W8MrV7_CtuoAWf3jVVhbc_44lm0iSxM6mSZ657Z_9KMWlPfx-I4EKMY4tUXjWhF5UbuJt1X5j5CdoYkUs3cZASG7JWW38gPQn0EVJ6Yd5omV8UTihPvj3HA9W0eXOWdMF1EPBLRTzT1DUWlkeusetWSY8CXcx40gkCy8k_udNHrBuFVHJNcluDksHf4tx84fYsZJSX0UaUtpQv0FCDNZSqsJ9EmQp7L23Pa29XLQ1BbrhhothJC9UtUEOHsHk5BG0XLOI0ZP0mh8kxzY89Uv1XFT-EmSrdYQSC09IxAOtNo6bbt2kxWjiQ6uQKPC93Xhc4H-9NSCcjpHB3HOfB9u-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5mMdvSXImjU0Z_BcI8X0hN5Yw_EBm2cc6kMFOJ-ooXytdhLYtVMUkBmQA4olMTBzLS9QuPB6mnr9kY3B7dOio_MNyzneT3yO1mj8Sf1LLDfCDX1q1cxCS9gFN_GTIXbiwF9IeFtf3c5yl57u3GktG47xKrE_uzVr88qV5wn4MxPB0JrH515R6Xd5HIn619pS_8oNZb5AsQ_wmEt7nSs0G_8xAyAd9XAdFv7c217kYovkpdFOERmD7xV-V0kXCkYQn5NXl7Sb6sGNdbSOlbj9IaZ03oseqAIdz49xZMcmHlAunMQQyGt1if0_EcqHaqLHPKwT95QUjTb6wp64fsSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=SgNXF-jz0JJa-FBImfG_5G201GnLUtawgwh5I0-_J-RYiut7zvtF0C_5vvB_fsDsde8ajjjr9yyMRXLcExxMMF4zbsIsKIR3W6e99ECxi2GQZY33CD4QD-ZExySpBK0Tf0jLo6viPzV74qY2fs_QZ7RSdoCGjgv6uuBi4xw4pyfyqIUc-RRFzHimbWo77SJ9IrPkHsMvKTbb7JLdwMkNge_Ikz3lMvvoR86aZZXW8n19BEjucqUjsth-0_p8cQstqYILFC4FNDVtC1HODC6tYiu1W0Nalr_Lnxeo2p7wghxWA26ouNNPaPfE06gK1pWjHYzbyAuwlCPFkhcMbFosTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=SgNXF-jz0JJa-FBImfG_5G201GnLUtawgwh5I0-_J-RYiut7zvtF0C_5vvB_fsDsde8ajjjr9yyMRXLcExxMMF4zbsIsKIR3W6e99ECxi2GQZY33CD4QD-ZExySpBK0Tf0jLo6viPzV74qY2fs_QZ7RSdoCGjgv6uuBi4xw4pyfyqIUc-RRFzHimbWo77SJ9IrPkHsMvKTbb7JLdwMkNge_Ikz3lMvvoR86aZZXW8n19BEjucqUjsth-0_p8cQstqYILFC4FNDVtC1HODC6tYiu1W0Nalr_Lnxeo2p7wghxWA26ouNNPaPfE06gK1pWjHYzbyAuwlCPFkhcMbFosTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=lZVYJ8i8sGUOW8LTlWyuX0swUyonWIaQbAa2ziYRQ4nlzk0PFN6wu3kLBwqJj4PuRhyDb0iev5c1P1faZ6bIXompa9T4G_7DSUNg81W_i33PeFKwxLWsH_45AJjKZJ3gfLXIjEtv0QC1rh05fiCMjSNowkNSckpUzkkTCza2FlGH2mUJs2L1n0vg2OaPvIA5onJ8-LsF6F6WoURnhEj4KHHkS4TxpvlqBNoOCXNAe3FSECnhvytsHwclz_AYc-5R62I-20O6Q5hG7eVYadE3FX5uUg-_8xnzWJhqUh_6tmzfYdLwSGi64yT0PD5FjXnV7qsLk21lPWBuvokGh6q_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=lZVYJ8i8sGUOW8LTlWyuX0swUyonWIaQbAa2ziYRQ4nlzk0PFN6wu3kLBwqJj4PuRhyDb0iev5c1P1faZ6bIXompa9T4G_7DSUNg81W_i33PeFKwxLWsH_45AJjKZJ3gfLXIjEtv0QC1rh05fiCMjSNowkNSckpUzkkTCza2FlGH2mUJs2L1n0vg2OaPvIA5onJ8-LsF6F6WoURnhEj4KHHkS4TxpvlqBNoOCXNAe3FSECnhvytsHwclz_AYc-5R62I-20O6Q5hG7eVYadE3FX5uUg-_8xnzWJhqUh_6tmzfYdLwSGi64yT0PD5FjXnV7qsLk21lPWBuvokGh6q_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBd2gIxPLZbc87ElmRRlpVhVZic4YUsy9IkhfA2JROKoTSG2mx1k-YlpsBjtO-co22Ms3qif_dRY-ebkeLWCMUHcZDdRVr6gALsL6hQ_Eye9jkRtXBFN-zKeSdPm1RNof8ilxlYDBjHIDsDG7ccPQtoCGWU5gfCNh_QRI8PfviEsqqtQG3_lkAM5RVODHAGOhEEv-9L13je1fOtJd_L7fO9pXKEogVg0OiC_UtymDxPTO9sgBz14QcH8h6lgHJM5uwT4tincK8DdyMhW5ahZ6hVBvJtJ-QTRIbIjNWMCEfgUpu0CLKftJsbKGnVeXkj4GWYnBBQIPJsbNaHPnbM5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5V1FTQy2czGRCY52hRtRUgZgA6AoQkae1G67VHZoXdhFvWQwyOoDOvT5G6h3M-ZEG3PNxIxIjHXHASDKFVCBLdh_xO_VMaOgJtq3-JDQzjyxuHbyVOGxk3DyhBmJ7imHJdmFbSfEY-D0SU1nwDe1bfVtUruODxK5VDTX6czw4afDplLz8uc05kCD2KnT6SEYDF0RLlvyxPFgUlT-tj2dWFmdOkkvmwZKERD1vu1I4r5zxx9pTJMwbSCII8WVm01Vh6bazyhDI6nkvYUnjMO2jfsOrNXj6fOoD7y7mgPgM1r7xeCBXa_av1LhUrbHbp96Qo9UW_xzdsA0y2ePoCMhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=m_0VQhPGfbE_2M7bJBM7R7BWM4J5xpBN9rBLt5vPGG2qkbU8_GE_cZgnCjDYKl3fnxvW4BKQlyGs63tqFqOhbJrW65-MNy89ut-tjdtDCbw6BOVZu_LnB0BD3C4QVTDcRqwGi1oTcn3jASHs7DDzay8uOSDMKPsd6GyhNfvzlbMC1Wmo0-DXZjJBXhfS9xAiJj4A5obw6EqPtrYoBRSJDGL-Kq_xVnhZMJGciY9OVWslZ0Ly5RwlAEMVAA5ap8C5E9FA5WKdA1HgqzhXY-VnFhf-vYQ4bxJAVbUNKDU3LIyg9FaEftNN35L9NUaHjBYwDwtMXKO-By5sIqRRngBfOq3TZ7CEZ6ZM-gJtowIM0VIWoGfQxXWVSkq_FtSRposoAnJFLSNOqxQss4dZP71__31Yw8OOOf8hG8KE4Noq7FwJXDOeB9yxa4hT5UxizDXVSwwJ6vsd9SXdJRFYo05ZO31utyzFViheh0RNLXY7SFTrq1CLiNVi_F9fDcr5drkG6qeykkRLtHOQCmps_z7fnheSdv0nBYtUf0wBlTb_-d4oLcokHKSplx2qzsFYnI-o4IYSxYB5XHKFNvPI9NTWcZ65C_sVR8GVw6qRTfJvKfWjBrn51XvK405v1flf8uqiEyxzIiIaywzqdygD198x1CDqtW7-xVF2ofxQ8iQ2yoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=m_0VQhPGfbE_2M7bJBM7R7BWM4J5xpBN9rBLt5vPGG2qkbU8_GE_cZgnCjDYKl3fnxvW4BKQlyGs63tqFqOhbJrW65-MNy89ut-tjdtDCbw6BOVZu_LnB0BD3C4QVTDcRqwGi1oTcn3jASHs7DDzay8uOSDMKPsd6GyhNfvzlbMC1Wmo0-DXZjJBXhfS9xAiJj4A5obw6EqPtrYoBRSJDGL-Kq_xVnhZMJGciY9OVWslZ0Ly5RwlAEMVAA5ap8C5E9FA5WKdA1HgqzhXY-VnFhf-vYQ4bxJAVbUNKDU3LIyg9FaEftNN35L9NUaHjBYwDwtMXKO-By5sIqRRngBfOq3TZ7CEZ6ZM-gJtowIM0VIWoGfQxXWVSkq_FtSRposoAnJFLSNOqxQss4dZP71__31Yw8OOOf8hG8KE4Noq7FwJXDOeB9yxa4hT5UxizDXVSwwJ6vsd9SXdJRFYo05ZO31utyzFViheh0RNLXY7SFTrq1CLiNVi_F9fDcr5drkG6qeykkRLtHOQCmps_z7fnheSdv0nBYtUf0wBlTb_-d4oLcokHKSplx2qzsFYnI-o4IYSxYB5XHKFNvPI9NTWcZ65C_sVR8GVw6qRTfJvKfWjBrn51XvK405v1flf8uqiEyxzIiIaywzqdygD198x1CDqtW7-xVF2ofxQ8iQ2yoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcNr1Mlg1f_f3KTJPVUHyn3iJ0o_Wkz7K5H46OIFsvOOFu2Aet9AE4LEJqb14kd-3dRkGWwfl3TY315HYG_dbp2_96yKYXjidvUHMDgNWfgtkNt7lo6frfdOv50pX-dw9c_FToqgWBAWfXnidNN7xbJuaiRVxRjvT_OECHxEgH5CzTClCpPEYr-W9RuN_hGrRlSxJvwGLeNqO4ZQJWMkHE32VNOqF74glxtqNtX9IKsv-m5ftPlaHyHQv1NBWQ7TPTZAd11iky2qbzdBTM3gMBjSufSvUesbFTYcWYPz9or-_c4XIYi07F78jMwkoiuzgsXZY4QXnwKUVUkn60YvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=p-TXsRl8RkTmmtGfKjF9rLNSowfNTQL9CE8RyawhdhVLyQPcOUHmMOg1x1BoX1N2AT0YsbVbB30DVKPmKC4w7V4MqfNqq0daH9psea0CUsvrmDPamcOE7_NSA5q4PvKsCnkw3WSZWcHrJHVwVrnN7hHg86XX0AQWXZ5sCtSW93Ce0qUjsF1Ph0YJeTYmigcUcOr-DkGJWRAuq0srKvmND1diZZA6rwFwUfls8UeIhBdArE_lQHn-OcqrtwnkLP6RR0iEqEGVu-0VCuY8LbuSrMWhxDDEFuOCsE-56icmD1Wts0mW3VbLNxvidY9BDe8BBh7zJObDKYlYYO3Q77mbjQxI3fvg-ieg8w62g_dQwbjP4ZP0ztwnz54nHF458YcLPv0TQbERvri1fkYPglighAkz1YhhXJ7uSlI-NlHI-Pdfqz9968d_c0YksY98ylemCxIROKE9OmTP45i0v5LjJS2oGtBIke1zHOEf43eOaMfD_fs0R6EIeUnsxOuJGvUTvuYzn6cCkIN_HBvOOBiPAzeuAo8a6yRRuYjhzuHmCwRx6p7BkUkeTDcQ0bNpeIxhskTKzH4q9ZkuPWrBuiqbxN9-paSLWjo2d2c9xLn43bXTurvOvAm-yptPZkw2pDq6zaon6vJC9Bow_aX2In-vF68-cP4EAT9we2RqE7xo3IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=p-TXsRl8RkTmmtGfKjF9rLNSowfNTQL9CE8RyawhdhVLyQPcOUHmMOg1x1BoX1N2AT0YsbVbB30DVKPmKC4w7V4MqfNqq0daH9psea0CUsvrmDPamcOE7_NSA5q4PvKsCnkw3WSZWcHrJHVwVrnN7hHg86XX0AQWXZ5sCtSW93Ce0qUjsF1Ph0YJeTYmigcUcOr-DkGJWRAuq0srKvmND1diZZA6rwFwUfls8UeIhBdArE_lQHn-OcqrtwnkLP6RR0iEqEGVu-0VCuY8LbuSrMWhxDDEFuOCsE-56icmD1Wts0mW3VbLNxvidY9BDe8BBh7zJObDKYlYYO3Q77mbjQxI3fvg-ieg8w62g_dQwbjP4ZP0ztwnz54nHF458YcLPv0TQbERvri1fkYPglighAkz1YhhXJ7uSlI-NlHI-Pdfqz9968d_c0YksY98ylemCxIROKE9OmTP45i0v5LjJS2oGtBIke1zHOEf43eOaMfD_fs0R6EIeUnsxOuJGvUTvuYzn6cCkIN_HBvOOBiPAzeuAo8a6yRRuYjhzuHmCwRx6p7BkUkeTDcQ0bNpeIxhskTKzH4q9ZkuPWrBuiqbxN9-paSLWjo2d2c9xLn43bXTurvOvAm-yptPZkw2pDq6zaon6vJC9Bow_aX2In-vF68-cP4EAT9we2RqE7xo3IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzsHpFFo_atbFFsojwJFIvAAYTuhSLAmB-A9zlTbEu-GH_JVHqtR_oxBSrSwwybgnzNdHD2M6B-w-nGqNt6Qfdf2nKCB3hJiqaP4H9AHdqa4qE3Pbyj8ype7Qt-5rGGvWjgEuZVsSxFacDuiW47-9Pu5NOS_NzRQRYQTmii4fyTk8GSy7Kys6P_INqGSaoMar6y52zOXV15sFOjm_By7qsNA2Pw8mIVW3lasEOF4nR-Oqzoc4pbnBLd75PsrO6LzJPvdrUIiUDv2HqReAZxae6xzMc_BwO87m60bI4AiHlJAbcCJXPVwgU6Qz5d9pXqJCuOr562gkkjqFy77NnxhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFEclBqyikT8yog1GJsq3slakvoHpkXOSa63wF0FnXlDoBNmg9oMksZrIAOZ9t2OVyq4uxStOLBMJPVGgAoE302N0EZnXVEI8eFdNsX8F0OI8eiFamDWAtvqNDIziVh5WLzfkpAAq4hud_n5NfwaBLt6SIXkeduZDNYkSUrT9H0anrtsI4FCULTllLkTaSZi-OupPsFu9xkjFlBrB7wOS_0D_69WEb4wJb_GD9xQPP_8uARfXRTNcqMeIAWOGMPOBLxyyrIb5t4PQJIsN-MoufofWCaD-jwHyNymh3h5QZ5bfTfLfplnKNvhh0zmAFl6HGOlL0Bw7woh1-heUraTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDFuWQLiriXBuu0t0xKpB9s6gkrULwDtj_jQ8Aan-zBzhMREp7yv0_wMM7nyzNfFWngWneouUB2t4Mk-mO1wOExgWXKBrD_dOcfny_Fe_TjQXmculIMwP9t3WlKl1C4PVFuyqGPuGkMMVwt18YFubzipbzfRRsKUes-7NnP9ZJvuR_Svg50WA6Vti6I3x32nAdmGuzppLyV2-pTy32YSK3Miab036rZHbck-QKKj9oIEfyXE5x0oYdN7HmK0OJBGqNrNZ-KwGHZXCp0NbhBBUlMuP6RAEhC6hEHkWVlqKNSDws8OX6cEW0RduWFRKCwT5Vo3hKUvLUNqxkgTssZ2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwFbO3WNpb4fu_FbKwr1VGMl80IPgsEil5jioqdD9MgWyEXxEzD8iJ02qc9zR7mjrHk4CuhWYgCifv-6Ugw5Ytmz7owpnK2uP7vW4jQiRVwCY60umzonIElzpuwgKhfazsyu6kTNKedNDsx-aOhygI3dtG8TGqJo_e2U0a83ya_6yQeV6nnf25O6BeNp2quFT9jcYbiMHsIOEUC-7hxI5n9NvDcu6Ot-lGsDP6yL0HG1s4mQ6_oHbJedHqot2qAxqFcxCEv45iie-VQOItwuZVr4OiMfaOe_4KOY3nzvvuMP9aqRPSOq637CYIk2WMYFb_Riybc-aeHL2Xnj3niSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IodiTxah9tG0P6QVu8Bq6ojZhdepRKYbmRwoqZOIO-vyarBaqyeqQsZtH6Z1T754F4q1WXpSsvRA-dOnCp7JZR-pq2CduBFucIXEgupCIv0G-loHXGBdR6W3GA0EuYEgGw3AGvMb417K5peHTewM5AKljomT6HoIzioGDuK5DKCqrgDK2QEWGikYVl88TddBIP6CpfmSI8AYRriNN1JJRsY6XpCltjUtQWcZGq4Isj6ZgSlyJQh-uwCXZGGlSfuv8X4YfK7TA6A2OPrjVLXvpAqpLr7r2krSdjIBXDZU-KxdKZcJFLwQPONp1pKDjHC4xWwBzPjqzUPOl-FqzU753g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2Tle8DdWGx1_decASVt_yeqxp0msOkEAV79yGU19jMYfaRQinqUlpCWecWmxJGQDoG--uWJq_R40bw9aIxoadV_-CS_jkb1eFwoEt_UWQSveggajvj3B01pIxEJCQiVsc4D2LncHH1yuisaL8u_8sYDfGDW9m5ay5iClD6b3e6f69TJoewIiH1gwS_E9oPF8fUiSHH8rYRFp7ihVqd043-hLDsqN3Rwt7GWf7DD8IVJSpalYfnb5oDiXl3hs2FdIfHASDZCEPeSCJzd2QlFe2HUPyR2ee1n0f6dJwzPdPGlSy3Lh6-yFCgak-rM_7gZDZPpva-hWplAp4BRYhKQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6Vzpw6v2jq-AmeMQU-_JhhRwbE-FCi7GO4a8o4fG0y-Eu-vtPX-gfWP_KVzWprp4cwpeyEpTVwn9WGvS9dMhZjDQ4u95C6XJBTGHfXDX-W8eENj4Q0ko0T7LF8uKf7GBS4TMDTL__Wf7QMAQVpq6TYvXtJ2vCpwrFPIWrGtQHRNF2-hQ3JdHqW7toBEpSZshesLfveZxLjpGBlYu6yx_qlkEMZlT1xBMlleitXsX4vqnmSOwNfGvTCz9918_ivVc5eIMAa-68Ft6KyRQcexMYEfSYN2iGfb_a1nxx-gUUJ56W8KKNUHIZW-OF86Pfi6NsqhVhAjVVbII_LdMwH0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzeuzzvwh4C2tdkjdRvkQh-_E1af5uGASjjKWTf_NGJdMrLhxoufzORCY7hf8yIMDZecoEuv-bYfBTjsmNR0CcR5C9DeC3lOzf4iSP5qiFrLhJ7Ud31_OCYEGEieKrSud_rAnOGYEG4RHzflwBe9Iowvg8ZBdKzjqZ_xq84jZta6qbfIM78c3qLTXmEdEplW4_Uvk5yqOaQ-_wJDvD5FO1u9jFAql52_aGlNjsWcfsidlXyWuufbbTHaQaGkX4b2yrToy-4wjSYDgiQ8XvrYlN83BC1Nla1xLnkl-sAIP5Ho3GIPKe0Boc-rmr3moDaYhgKROnEyfYWv5j_QnF9tog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLhOLBu1aZZXB_OkzqbYB2hwMA8eP7ndaETMGsqRGpu7USwuvRx3wq0_IOfsAs1pgMdgPU3if0cjeeCIInXxPJJY3ZQ3B1aZ8f2XuUu4n-SArEsHxGAnWkh8hgnPv2iCLiJ2GL6_EZI-w0_rzeveJnv1g08XhRbfMYIVlmE2EPWfxrFZ45btkXcPjj_bGdiFk3-LATY6TIWytS6f3sCyhVW-lMzAA4HMPK5CABAzNToEpg8-_vAL10f9-6wDGyDuOMKe2OtwF7ipeQjh1Edv_-b6Ehsiim_ZQ1rCVAHKLiqiocxQNlPc-I5jAW60ldh9byLti5uyUbSUmrQsYfu_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSuidaS3O1HyowuHk4i070LYM757NEsh8f9y-UxSvm5NtVXuShzhgxMidHY-4ySaxrZrKyqBDatGvyIxQ3JbZASrixTs-b1JQ952sU7N55RoLMJr4oF-myuhcMGUM2fQw4qx52xtVvQe0R_IGy0EWdEucgpu_a3mwtnuH-s07dNftr2-KW-XDPk1kvOGZoDGu_vlEf1gblV-NNumqGx70qQuRKs_x8sDC9p-46DGp1i5hMMENZnoju9peJzzqBIq49xSWjTR55Njlbjca0zySUpSUKJItuvkPS5-7OQfmsSqB1kt57CVAj0VwDIX4_sm9U050LAIWSl2tfCYsFZ2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvw_jplvYgy9jI8F83rQ32bfX2v6MazEj-_sWZWG0WY_9cPyrv6HsC1Y5w_8J8XumVcA3l11vC4QQfsPCLw4auscHasFSyChB75NyY_PWg6z6fona-Kp0W4lazHgbQE7ZjuWCAfycTmK7UqMCp4dYluKwe0kPqeKfu8mpjlg93P5bFlliYsrvhgMgCCecC3xJVlUzoDqNYc1yOCCS1Mw8EyqU28OVI7nUhLVzNhWX_bjIa_sswRmvYcD-lX_e-vFMjOby70nOnLAInSGZE783uloX6a6cepqeUP-9PYtL7AIIWvphv8vZ7Qa7kYMnljifNAP02T6JFw7UVOQ7RasBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3ILHPKp5ER5O6V8pOKfboKC6J4Z15zboiIlIy4P3dUqQQROUFQWAdsJB4BLnjZ9Rcci-kU4r26eCLA8xuvzPzYolWQsq_vM3xnEvu9Z1I34fhI5wQJx-NM_SiSmLOYSgOgubFUFIn5M6QXpjnrc3R_jvFi95J8CtCVlNiU6AcKZQD0RsdOD99-ijZZm5B9hSVefvtgJ7XfvPZfVD80q1mL8ZW7IH3PhPbvhv4ATrozZSH0kBvn_MVU_-e1oh-7NPHsSf-1zlcSjZcegeDD8QGaq_cDe5XpnIYpaRAo_UW_YSeN_fAtm7KgdgmveUFMXxwyFC-SQJE4V3NletBlisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaWkass-umoLdbbizuc17fJRzonswGOIS_8PTvI4-fW0Chd36IRH2T4CX69R1MZsLJSU20S7Uqdru0rd_oR19mZAVZm8cFdNjRC57knyHkbHFZ9Otwjx97QIVNKJJX3toBAtyXqy5YrUt4iyfbTR07Gfno_XBv-c-neRZ8SlrmwpbIk-PMUpDusTXIZJY-AYWNpQoZkUB2I-IWimO_0-dJa5bluGt0-Jpu4u3KCuBHzYeBYVXDLcR0Aq3XBeM_Y84PZVQu2wMF1_izwdBXphiDN1MqK-4Ju2sp4oX0kOgxdQ0aPVzXjpvI_pONCbYt8qs1jSwfXFKjVcEL9j64GS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSpF4bgoE8NXwi93d2Kkz0Nu8Sg0SkvrNEiaa-91ihUNJpovZB4bzjdKj_y0gj-gwQskYH148FUzm224AuZ_F0NHhuiPLvEiSGTEjL3U_OxbNSx4eXHcbzh_k1mJzy4KUM5ZplrN0_GR7HCttQ7UFbIv565fzTHJ1MZ4KCE8WBCuWp-R7rhpeiFEWIEKPGul42hP8tmfOSk7crzLYSsdgdaPe5fkvF7JSlMv3T-gcYLYyBuCtVVcLEFQL62ZqNisszNp5XIbO0jkujdHx6T7gVAe4I6UXEa1GvJRLHXBDshtx-t6Tjm7Rbclku9ZJnQugYtyFH_kvK4cJMZfGY4vFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4ziEp7M1DfyBwmvWPw9LYvM83UN5Yuulsg0zysTih_61zA5GeZ577WVOeEEAhPLDa1FLS1TqiAosCYngiAX2H4Ci3ZXf2f97olpMcckJY8Tw7IUa3IlFYjWNsPvyhcTaYLO2kR2jqqjLvok8Y5nVWmr6ocK3UVGhLrlhfXLMF9KKlVB0Ohd-NXXIUwHNnHkvZSe52cXgsaRMMGvMsZLt3VnbDGqpLPCZoC7jFie9xfdm5zc_H1F3ouR4K1TV2HP2OdMVEv3wJiEVlsxGpOAiLPfJFokpg117EPBY3-xVVnhUqoEltyKf9BUCIx9A3bTNe6WjSjQZ1LZVsYw_-2MAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzQFAx5XA3Q0csIrZpejkQGL975271tGJfVGAcybisBwcZsT9l-ysztmCsMjvTRa5hW6a0iG6FzqyJbQNIYiLrWcHBD88CrRzeMbsp-fu4n7b0NtU05b0LDJCqCG8YVSFB-3SA-1UR7qhHw41oLui-iCmMHOydVbjCgGJ6Yf7ZllHzZIj3pWLgippYEHO6e7r59g1Z9poceVPxjOj2s_UMy0Y12fa7vhRcVIUH9Em84ioyMPZGbetD4WktDB8C21djUfAaeVt3kS9HA9t41PsPMlDP08bkAyX6PqftN_Mlb0q_1VWKUTlfo7q-Ee-L7JvuEwAoSTuJTM38KKXUoORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD6xUh5g7vfNGSlfsitmlU-9TK3JuNHqVQ4u6QyHEYt-u9Sz8hI7Tt3XjbF7F8k9I937UjEP6vBo3L56OFyZLzjT7-oyBiLXwexP4LgsVnv1W4iwFYtjU9vZ9w8XRLKVpU7e6OahtbxI2O79ktRf5uCakpiC2NKwaWvWB1wnHqD_PJ3tYAYiFMYQ8D932GPicwACuiAn-Te8J_y_DVL97IU9JnECeMAOYHM_oMWMZNgMpMxuNa-9quh187f6qDB0B2oVHeUHgshgpUE_H8cmYArgd4h4cOAb0Hzgi3fXi4w9Zskw5juSE3IP5LljiwGFOlX_gYrawALgT7NxnrTGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVrbFxyM-NUB8FOjT6euKDVioWdFsWIOSIGm1yTLBKboYTNapScMLM2r_RVkKb2swW9ZvKpYwgd-eIXQHPqL6uoPcaDzZoe5b7pdCJTP40jxI0KKz6KWJaLCkvQpl6FVSpf6PCu_rbAV_xxU1T9mvDoYYYtsA5tDIwxG8R6o2nmYmFQmXO7OiGdz1u0btcROtxNTTKTTKokStoIS_wKookh9FXIA3xPj5_gZvsjE5vYga7sHN7QD6PgOgQlKvbistzwpSmSaBWDImgjNsj3O4VNDc7QLIuk6GR8G62F-8ZbUmJNBi87_tMULOZGTBRzlt5-R6hASdPgF9fpaxUyqSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxP7sHgMd5cm6kREgceqbNL2ZavVhRc2rdIrUh28gUxhr-a5LsNHB53cXT5iETtURwNxD3YI0NYWUAYlxsjmImu_Jkd7IHDdugVPaBCsQTqf5kINlNj_7XCZFp69cTFIt6ewe1LXJQpZ9AHj21h33nRbgvSfguXPWNFzuJieiZS3vYTe0FlO0CD2hGaMXEyc6a-oZVygea_tsYPVyR-RphUd5__qyC2sEdYfc3u14kHn4P3LCo1ZQ5F8_M0BRBWNg9nTfC2f0HwGt6wxmIr6ty4F_TsNp71UbFjRySSZFtS6Ss_jnrMb6McBoq0tnW0T-mvMYhHlg3_msjr-eYkz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fENpt4NBVd2Fyoa7LGFVlfKen3b2oUkCy1TDKm5alf_pSQpMPutemjbG-fsb7K26y1J4iOrH4HgxbbE59pkHyrs3S7Tk9VP_c62WYKDlnmLUZ0g4n0Ej-_XwwHrPYlCKrrfOkC8EHmHmx9C2vrAPXf3JTLeazYhUU22ip6zpfiwF4_HTCVSINnM7INdhiuveKGHmhSZuxgbXIKWBRtpkUHc9VPJa0QdQMgYy9T8EohPIVTgSJDG-SSfscHDAV9siTMTwbd7D5Lm28dkirstSJ4xUJMpR1ImFie-3baxV86BbKsJpv3Eyd21FGMuQNqs38Lbzk4XVoq6m1fRnaY6OsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8HJxyyFqyua236-G7Ms9IqhR8iJzfpMI0FnlaPgGiYc7r8jc_wTDnxhxqC6BP5hcAkm4f-r8BoTm8ZaGUFq8q-Y5uI7fxBmCXmCj4K2hZ9vrNNxotISQEI1nVGR6jdL5J0K_n7-IE66tkxtbbYS5J856UDJ5hjynhMTBkoef_mbBC_05fz9Pk8vp4JQlWkbqF2zywH_Gq7wekY-ctORoNT5JB4n3gByUqSct0pot6AXIoFwgvpXbdAkSORdlhKoOAfempshKJnttSklM6eM0kQIRlV04dh9XPueHw_Telam39k0rvwwlFy2K0Wo_Yur5rXSoHpBAzcUVOTs4FzY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL_9e2R7RN9VEnII0U91GQ9lp9WEwx_c_HHZe12jvBVBTllpmPjU_7oo9mO0l_A6qfLLZCyW8dBK8Q4qzSmb3gphmK7oIZhycloUMUefRoGTK6BfQs-KcCWW-8ptsZOYVry-w2i8jvwKo5Oem2b1hdixhrtO-E5W-cWaNqQnwa8JbAsOC2OnpsiL6uret2-8DzxIqla-joMX1HsPtvEHyhP3ylUkM6OLW8g9zRswDasSzhlCjxLq7sEvjo5xYEXRObffQ3NcuApWqO69p53QdCVvqHO4ogtN--Y1gNvlXdy2XMmPEosdG9IZr7f75Fd_DD0-bdbiLp5Xn1FejQXKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ7TgBjSk9RMwmyN_1ZphWzar1pQAQ6coUIzzQ60gu1xJ8R8ZPMxVra7LEQSStHSjUX5XCuVSTQ4MZS5rsPcrcsgTaDHcuqf9xe_iETD5yRlbG_rJlrWuWSqmdeGkUq3DCMGNmI0DS4etqrXq2hC9ZaLZgvid8NF6dlFv9XFZ23mGQg8b8Ztru6dR1zd7PPPmC6S2cVfXoqZff6pP7YM06e7OLLw0KfzEnSx3IdloePbfdfs4K0ygHRJeXviamtwD6CauGds4dos4e7GP7U_SDNZHu5713KQnTQciey1TAU-cvOF532n9qjo_Nn-ffWhG96tKb_tnnTQCprF-mQSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zog4BxP7HXS_L0ocy-CA1mc27rB0fi4WKnUvcplWUDXbhbf0xzQ70YolBJ0DdtS9hNZYrI_Vl9i1MecfNfBCSELOPyVDSzm4sopLytD6ehhuaqm0X5flmWW6WVYBtdDN1TFDQHndwhxnI98qGYpgWlWY31F0tUQy2hpaU77l3tyZM0Mu3iT3gRIMUIqNQw7gpEiQLNyZudJczCn3KBvLsC6_pGTmJWQIK4zZohy47GA54uX2O04LAtp4KNA-Qq3QumQdpid_5i67OQgfOFFOTrEigrPrlfQtbg0Aw_iQFyCKclch2lMLee6yL338BLbB-31XDJPfPQAMzRvwfdiEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXWP7MNDwCEqf2Dciu00Ibc055dedAsG0gBNuNhJqJKKsXL5p3IWEevuoldmdmQM7sQIe4W0x5_mg72c6OJNhdGWYW7zA19cGgFAW3IbQ84e2sKTUAOKiyOrZqbnVw5hI5HTUZA_d9ZrhAlI5OVVedql0Yd4HzYp86sDyxCW4g5XJh_aauysP0MD9yIaF02z9n3y1ja5GSzhzFEuYNhcQZ6qmgcRaARZGmPiW8sVFrmQRajwXvht1Hec9NKDezARoi209-WM0LF5pWARyRUZRP5ukSS0zjGdrbAxZ-zYLVJKuBAYVkCzR_P5VzceoEsxdxdTJ9byb77AbVvOmd4e2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH9TJw88AgqIexlQvelFk6hjVU_bKWNgvBii72tC4YN6zmVSMT9dCqYsl0nkz8t6EhSxOuW6qCwVG5k63T1miZ5_Q8SLGGxjhgxBQTFzVs_TauGQaNoNi41-L4ajPBqT2ysJhTFkeVH2qtpDSihVAEJgiKlv8KiohQnkJHwTOm8z5-DLA12m0qRxz9PhhZNTGDguTxvmmNW_CNHMzovQ8dSqMvIwo3N3z4d6w_gewDeWt6RhToOJgY2jdUE5bgKKQRfNf-WJslHDYXDH1JwmPRZTzxqoTxmxRymYa-C9RZGtjPF1h6eFUvP7ooUghzlz2w3ksyhs1OowZOjEQJpjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unW1eo4Ue1jz_DgEyNhA_DvBeo0WmH6WruihyntXvHtVjIf298sZoJcJFCE9O6i-mOq1dalGYn2gCdjhXrx4Sru16qcecwXb3YMz3DXpQO-3LoVxecs3JeWPXueSXVu4Berw8m8cPYuSg8cvc5eQCkwu8Hhtg8eVjYWT9xa-UJ30Jstzj4fmTmlwwdArov2zpY8NB6UwyP1iy2wmddTrHiNJjpEd-O8Ozsa5BQuPvjVexqyQskzPBwEuH0VLlK8r8r0IKfvDkCmounkjso_IpmtYPYJNcK02cAwUWOiRkPQntRa53eKoMEmCahW5BogHTAO7KIfUAm9a26PeBdqhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRnbbJr0P0xWZDxIhpWOCbQg9af6rjfY5UB75IgNsIVLZ-MibUdEMCeSBYW-vkeqeG2Ra3c5mQuOWuYB16EpVo0gVdQ8MCHu275KUCzDED9HeizTNRZvwAW2pY3XMc68Xg91WBjZR_4GNK7rBlVx0OW5hg6_m55yHaSrKeMh1e2KhGnZuWgrgeOy-lr7DD8WrmQP9wspvGbyvZXYsigWE-07T_zg2m6rkfL1EDJQCEXX5RklCqVQwo704buZOVKMdCarenQbIsMtakef20xMRgyt0udWr8jn1Ds4fsNlbi6-glzR0edM3RU-g7O5Y_9kHxUSlntRM-ebhZ5g6BG43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpDqIK_kSYzWniCnOgCsezSMC13vVnUWqYTRGAPhs0M5Ph0bl8jMdDh_5I_M8BaS1NEbtDMZeYfn-nQp-y--dr4eIl0BDnjKAUN5mqIRRZYXoCHg-vvEYDHeE8xh5ES5PYfkkSPk5IOTqTZZ4dIyrVQU8gr82qHfwnRtmtlyThTjUVkS5RTXMj7Fe9lFFm1iS5VJMfQO0EVxKcq_ceDcq_oB7M4tS276fvdeWpVLOb-R77alwTvpVgcQsHYipBStDNsA0jNdxiDxQlQohferwsSiowD1qxt10SJQNUtMk0Z8y2AfIdHfE2IpFwXcniPF90qEyY0ILYhhlREb8p-aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR_VS04gDdbzMTh12FfgXMO6mNrEYdoMwr7ePBpfdekNvVqPfs0ryy2miB5Pco7R2oHlys1j57R_DwZLNRMYFoZySId8vgorr8K0DDMoPbni2QNX0SFebPUv_gduB1Avp14jZHaJHSP6bw3XoNDUjnb2mqPKaOFStN_BA5hOvERmx3FOKW6Yrb7t4h-og4gCEIZpkZViUt-_UsPVgMBWL61xznmqKmIcOVLcRHX03sC_J4C-UIPmNJFvj8jCtcawV1Xzjf7nobVkwPEXbguCbqI9oQw0KON6kDGK8wFEYZGJrVbZtkNdB91N2V2C2k8fBMjtgQciTuQg-fcnLke2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk4FXwgdTIwSCE6howfwBtBHc7dwAdFTDbUA09ptBrT1iTgazvBM7Xp5VY6e5BE7LzofM4oJfts9uHF2Tp020WPETW04tmdluPaG9QDxlGUwY_jhVg8q2eJhd9PbBb6YXbaVfuxIz0i7OSarKPXN-0Y8uG92SI7sRBF7XPN-MV8KUfsMZqkl0-dz0-nw_MOZy76j64t9GeLfRyYtBFGGxmW3FwMuG8tjukEWPfmsJoXfsCEQrfEEd1A-Nez-1yMZ-08Ttn3j0PL6Exgh-xDAx2nbtCatBuOhcJVbdNMq1Ky3yQQJrwKJ-sZ5vwB-tDwBJRKa1B1zPeIaqU4H5R7-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A65kB0qZnDeMS55gH3Yv8VT2PBdGesbKLgrJDG0t_WdKSVwPJHXS6ebNkft0YRIAlm_hJaZJJXaEShnu5H3Fi6dghz3xXyCP8_YogrHD69OnrmC4G_4LI04VKrO4y3S32EVQQirWtjHYZHtp23_RPGIESdOHtKj0ubMpnyUPSu7_VN1XTleoqb3u11FlYMVjAfCihxWYKJF_eaIMWX4Q2KHJtcHmds3Ym0CWc05Rp4MFlyyB6RVyyVB0xbUZ7KGdz7jvhuKF1GwdWtBeknjr-dliN-8B-oH0QkwKHIa7AOkiXCWZN5wjp--B4tGLXZR-qHIGMF5fnPij7PJLOlYFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfvD9nYNvDabJWQVLXbIbzQ7VoWp3HC92Chq7MSiPgkL4rS6ychJhaKqsfGqmTwHZLrUPcuKvDJ_Nq2ld7ioDw61vUq2I_6qPLBjcP0vdsNrhSsu7t-yOL1UkrFrJbdyrXXwBrJlEJnppWeN2naC5eoRb0h7it_jd76Q8Ozd3TdA8IEUuP3qPDzobhSu71YvtiFfkMxXaA0cBGQXqI_GhokKGmOce2eIQzgnHvbF5WWoBzfV9WxSIQp-GD-ObX2-ZwyOJkGoaKcSxhTkBGy4nBGgagDZl3zinDI71yxGCfB3kZqaslzPsftK-3kEWBzN8jdsqEZewmEBmYRKurM00g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SILFmR9nFx_TC5TvlbzZ-3MIjTxAy6gWXcH5CVNKppHgvAol2PuubT_YyVMxRO-GvDdW9z7PbStrdpr0FO5VYlWAU3qBFpkXExHRzANldOaMygE9tH7zmV7ga93JbrGcQWoLC1OYCxZtjIjiBkpBYDmgaU9QPf7AysRWcG6wjrYfastZ57Y8vnfCfUr2q0L12E_FjShv2XtI9nSQwYU0HLJJPvUl3msiMKShLx3yK6n5JIed4GTkWj1y5QrpwO4O310N_xwGWizAOLvxj9BqgqrWD0_Gv4o81b3z5yJM1ou9Rmq310P_vIDJlYudgF3nP3SQaofmwrbJKJ3Fsye6EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=hjID7ezcH0wfMiZcma7-q9X7nIkFJi6dFNWryVUERnUp9AxMY5n-errx0OtoKR9WEFFpCiOUj22BTwemU2BCO6E3ssq_X6p2WY6JFBPGZYWlFH9AY8FkE2fiknKdqE2mJS-1jeOGgFGe0Oo1iCtDs4hm4NZbjJLVekoNrehi4StZQmfkBmM3oFZnd-jwd_eo2cxdcAqqq5bagRJjp0FRAD6WJ5mm_gW7hojOJN7F6E7FNOnwgyYBsIhbrISBWj7AUyd-HC8b8azLFv4X5XU6YZevDp6jONoHlmCj_1akSKr3ENE5e-p8vtlPXBdzDnur8sRAyEAZV2qgA0ORJwQsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=hjID7ezcH0wfMiZcma7-q9X7nIkFJi6dFNWryVUERnUp9AxMY5n-errx0OtoKR9WEFFpCiOUj22BTwemU2BCO6E3ssq_X6p2WY6JFBPGZYWlFH9AY8FkE2fiknKdqE2mJS-1jeOGgFGe0Oo1iCtDs4hm4NZbjJLVekoNrehi4StZQmfkBmM3oFZnd-jwd_eo2cxdcAqqq5bagRJjp0FRAD6WJ5mm_gW7hojOJN7F6E7FNOnwgyYBsIhbrISBWj7AUyd-HC8b8azLFv4X5XU6YZevDp6jONoHlmCj_1akSKr3ENE5e-p8vtlPXBdzDnur8sRAyEAZV2qgA0ORJwQsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAq-vet5SNejAtLqk_Fwyro9s_y_cmkZjvXxwK1fJCyCzoq1QS6zhOcw87S0hXVI5m18VtBZclet_i867Kjq-OdwDTDKTb2q2_azKKe7NUFJ9hJvIq-NdjoD_ci8Jn64Koqbsj_-EtynYu2HI8escgsiyVDkAmN3vp1x37u2bzJFEB3u3N6cTZ2hoCLbs9aT5xdYOxfV9us7WYepc5aNHIUw8N3nARKIVLpBlSt0-fwg9X5E_ulC1SUlWSlHrytLE_TPiv-IjgdzaRRCBy7cUzOP6CFwBqySRPw5qxGcKzqy-gPvpBW_Ctt-Lzo8gWi7HGD4veoYE65m92zKfkTDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4sZciUIWRx9srNd68LmZIOoBY9lv6PfaQjMS5QULRLItG2OZTYqY_aQ5Hvbl-Z2Je83VMlFSzEhbb78CZuBDAZ9llmSXxz0sJr1VXOBQ6oG4zObrhrk1MpNXTXNgMpo7frJGKtmc8T97-3b8rnQqa03ejXMmvcnyVmwz-EZhoT9iZcdXFybkz5hvZQFsQlLdkD6vW_cwEFhvkvWCg5zikGCvEMo0RJ2Dd7vFsLK8wWm4u0QwQS3ej5HCn8RY_-8JoxFZjgMh0k50RlsvI-Q9jHXv5_CjX-sjeOML85YAQGIsEukulwFWfkwE1yeBzIuTtR4uFx_ZkFUebtbe0FaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
