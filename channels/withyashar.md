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
<img src="https://cdn4.telesco.pe/file/JvI_Ll3TxU1S4dgjv-yKfbhgKeQ1kW4EJzo2BpOnaXOitQ22tF2S1qugbGUdO54sjjPIQ7qhph8JSPjGR0fL7Pzhd8RIRxhL_OEk6JixUToEWC0M-t8tHMOfM45Z-6kz0wcPApewsMJ8iOA7HB_cObaAOY_qe1Kycq_c6HbZEh861dncB0PWSuHULIDMw2mSQx7xOUiGQSuSJtahCwux5G5yS0_T4zM4PJr2sXnLFzyRyz_Rh1E1pXT0RUUzShMhgIACkWyBP2TLbrTlB1rp9QvYZFfSo245Qj9sIbBcqysWs5-H3P_I5IZwsfAa4CzFMCq3YlpavAxidq7zuq63sw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 00:18:48</div>
<hr>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2OCsQN2M9E5ezr6kDTA7wRtX7vGWc_N0fT7k4M_LL1ZRYR9KvjuEYDIxk4Imjb1jaGONKYaPYW-uBd_5hQQU4iKidesKJyHCxmtiW5t4m6kJDatVRt_K3s0wtNRJ2OejnDDVI7gbw9o9zp8-8J8Y8TBpF1KsDVDF2a6FbxuXejQq-e42ED-Nf-s7oEBNQjjIzYxBhqjUUumTxbUM_HQOwCiHCihl1-bpF_nq_LkHDhZqLqxnYAsVyK33CN2Z8_CIgquhDuuknCYXf5WnSZuxCY4sw_T0UdnTpWQwaC40__PPqc8wvxOuGBw_xpvs-VNlOi4y8c0AqATvlr98ID0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1oLohXX_-5t2dNP-FZMmRAlUJEPecKxTjt7UeLFLUPRbqWy3gZbIVIJicS8md2BKbKaPN4yhEPH_e4JuCT8rgBhZBqQ5F8prkscoHoPfyo1KAkm4BCdqzl_zc27AwR4cqmxyJW3aokHL1JDeDOSqVW-YcFg-gJNn0TB_BptPx70F8pSsPBq4lnHWISptPe14Zm-QbwkGcNqSQFZARmTBgXyGxxvuh38JSBl5tvf9gTRXwhW4pFmjyKiadtcCf2K--odj3AGJOehVMTnSb_Va3e5biBbYBE3gQmz-xIBD9yF29exrLz-T4sFxaHIqCxRrrt0gCAq6R2cF32Ev1m6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxqplsLSn2vPzP4WsU_J4DaXS_NL9zHYVVe2QLsXmvXlBcLUCv1K_tNUI_0hS_-TA4NSuwW0r6VsMu9pVbPSlw2jEXzKyBTECt6AlrZzCpGUFznVVBDuw1mnAz7jXk7hP4pxtirsE0vgvKMK05M_gamvXAwdFN068Dx4i1YkGZWAFzcssWEoK0A0b_M_ZvDc6uZ5LHvvndiq4XCy3m3NP1z0iO-J-OBy4Ccb2ApuVLWW635isXAsxMqljSZWjNvJxpuLXTaBIDdABvXDn4hqQKFnZHl57Ygo3T6J7jMb9jPr8ZUg6XPYW7hPMyRRwPC93diSHB0jz1nU9uRtE8BAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc574weysxnze-y3BGwSFJrxbg8fVJzMBfooWJWjO4IUc_2-cpq4exCUCZFWE8adHI-qHzjnTj7kicvnLG9aozbON68X7Yx9Ch68zBOAv8bV8fdvoi-2pVTBi8WZnOIwvoSHbB1jJdnDAimWKJM1R7lYce5C5b6FA7-9ys-Tx2WJK6oPMDoyCXEbugiGDGVCxbb0ZxMVSP2TvbJBtUpADbDJgAkCsO-Yu-BtVFeG0gN9belrdmKoVHtXiMoGRBuHKW8Kf60h49T6rd9IpBMTiTBeEbmRxl4OXJzSbvSzUv5n55uY7PXGeC--yVOyIDGvBPjOH3OE__I6SDfkEtOjRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=HIML66NCe6Ra2-kNgOgWTA3_cpMnAdQyLzmL-VXBcmLmvpwfFCYf_utVaXrXkwBXBUTfQh_5AIrygiZLbPHl-qto2VDa9CXrEPW1W0En2Eaes0ytVtX1_IFUfqTiSslz_mvqEcTl0Dp9qoybaKQSiZYHXSZ-jWlm0V2ftZc7ZBA5AOcjczdkIRNcpX2fHfWD3C9Vof274mVYr3mjxYQ-Ng0Ho7klb8gEx1p8BiG0hqfCK6AV8oZR6pougXTeUCVZirhRc2zaob97Sw8liN75kuycHo_Aov-IFVVrcG2z10ZN9nMYd4ee7QMWCMOD0GYryk2AT8EvLTetc2djKqX02wUZiFLKJlB-8caq607saIRG3cG0V4zBhdmbb2eLV_RnPrd05ZYT0CVudYujfEoAboVzHE1e4OdscKEasXxfqk_8QL6WOOd9i_Qb2WUXYkmr7dg4JPd_DumrzlgftSeq14VTk-Z_lv5OHfbiH9KjHpHd2keSAQfh6Dhxf0gNEa_KR4jPrsS12ajof-X7zJsuxSghcq0SkkEi8xpgEcBhSGxT6NeGqmcx_JCfX-r78dXooLfmncAM4P3nCKj0N87_FEREqQv7sUwJIsdKmQrfMlepTbg0bNe7JqDQmJXUjrEC6nacDFESrasMQ9wL0b0AHI-bXFxi0fN9Xbxnc_caegM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=HIML66NCe6Ra2-kNgOgWTA3_cpMnAdQyLzmL-VXBcmLmvpwfFCYf_utVaXrXkwBXBUTfQh_5AIrygiZLbPHl-qto2VDa9CXrEPW1W0En2Eaes0ytVtX1_IFUfqTiSslz_mvqEcTl0Dp9qoybaKQSiZYHXSZ-jWlm0V2ftZc7ZBA5AOcjczdkIRNcpX2fHfWD3C9Vof274mVYr3mjxYQ-Ng0Ho7klb8gEx1p8BiG0hqfCK6AV8oZR6pougXTeUCVZirhRc2zaob97Sw8liN75kuycHo_Aov-IFVVrcG2z10ZN9nMYd4ee7QMWCMOD0GYryk2AT8EvLTetc2djKqX02wUZiFLKJlB-8caq607saIRG3cG0V4zBhdmbb2eLV_RnPrd05ZYT0CVudYujfEoAboVzHE1e4OdscKEasXxfqk_8QL6WOOd9i_Qb2WUXYkmr7dg4JPd_DumrzlgftSeq14VTk-Z_lv5OHfbiH9KjHpHd2keSAQfh6Dhxf0gNEa_KR4jPrsS12ajof-X7zJsuxSghcq0SkkEi8xpgEcBhSGxT6NeGqmcx_JCfX-r78dXooLfmncAM4P3nCKj0N87_FEREqQv7sUwJIsdKmQrfMlepTbg0bNe7JqDQmJXUjrEC6nacDFESrasMQ9wL0b0AHI-bXFxi0fN9Xbxnc_caegM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD5KWA-5e7tJlxWw1DKA2uiJoHqkJzEvbeYUAn9ebT71X4I1IxsPUBz4HuYwLRQ9zUy6q8y6wR0acPQNlmKizHapRy64461T5_QR8UnVXVQfNbFg2uI9iI6v38p0136D3soZ8uwUA4sIQSSyTTTz5Wrn6zkGkwzQs7s_V_8KZ1MvsiC3FZ67TsRRz2aMeC9AtMrp_JVsk5aWlUtgzPD5lvGcwXvi-shCqA6aOeVAXXndJL8eam2bvSkF8dAcKSFaHWjcHH00Sv-RgKiseTDYR9OHsil6VXAo41ezrYl2XHEPdSjDLIB7IXS0OleEiMRgqWDxWY7truq2JuSvzxTwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU_O07BJO-bYjDWU8f8YN86Q_jkVIkDcpmOSCWhbBXN4agpsHUa_WBVDJDI-5jCXvG020eXsPp68XDZ4c2YzbQMF-p8jIyGmCTQi0YSKxhcm9WE4dhN2qGjanAVl2zefE8H73eU1pUn9o6Kl3OFjcIYWm0rMFD2UPEtoDUpv4yxvlcZ_idxXXzvY5zqozGZH5gyYq92mzcUW-g3AfymR021JYFbD1h0PH1-RL5UncItIdOaqDZjD9ML_Wow0G2nGQdghiVRm6Al4zWtcV0Pu-i_UuL0YmjyAR0GmIsF8qT7iIfuc0RiuRQcYxBMGyEtuG296wg8HuNFbqVyFx9kXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNYiQ4uWa7fRvOnzsjm1I389CCaLqCtHY_HavjBrEJGemlObVlY7Tlino-Q_XzIyVCvOcBtWKL1rAVQh7pxwsYMnlJmc39KJnHccAd0cTLTfs7MOKlk0e4YW5vqIXvao7YBh4mDGBaVdV6B2ndShaKg71I8-CrZMN7Sk5d3YddhdYx-osWoH13NEPuortkfvpzlg5smPAb72jjg1beqWoGafNUf72N1gVspQKZQXKG6NeQzlvWuxIh0Eft3i0qI6Oic_2jEDYI7k5rULtolC5fcoNBJAvwG9pA5q7w-_6rVZmfrNYdAoi0mJHX0OUEg8J5qCDq5nj_xKLY5NMX6QRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9KjyHolQhzmq9OPAP1DQEaPys-cIOWoCKpAsrGnylYqhf2e_cnbKs07036zD0lpE1tyZDAGThFIyCrCH3xP-g5vrlYDJ50Cav649sw-WK2nejX_KZPRML6YjsLnO5qy8nZbObrULNf2z1cruLGQdE0e_ZUqmwSuVe83UKpLsdQyE7Hj-TRG2qUIOUnvOSsGQfJbqUU_w6zrpW-xpuLytwvpxZzIijZ7SLNInVGu6ix4Z22Xz-pT0iW7Jy-98SGQi2XLTrIunmmRx6l2fqrtSTyoQCNcjTV4anAKsaCjX2HKky4LbU_NXUNZfRmGeKrkinkZAMpQ7e5vcxhR7F18Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBweKIFCYiASCuGW1ko7UCwXYLrL9TkUYZBChmM8sAbSq9UsrLNXlHnQ_OfnRR4h99nA0-5v7qLLywFQ7_rNOCgfLZHdDrQwOy_wPC0Myk9sXhCXRdU0jcqL2QUaT0HSVytER0OZ_Y0jCsu8Q5DFlIMgwyog4rKgRyoaKfwCf7k2za368jiIaxTy3UJ7IOPhE-9N2G4MDNfssP9PTJwTr2JrAUmyRNo-wj-VmVD9lUNifESxISkQP1MiglDrIET9s-dx-uLSAG95nQphMpB5ZQBdW6ZAE7mD21U5dV65K1JZtAURRilsSm31umDA84GGr9ftaJA3okyd2rSXJ3VTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1ppDMl_dMqlVqPUl4SkjvFCErHoBsLgo0zy1zwFT_bdyjYqvUAmRHNH1bYFVtcLsSKVya6cxOX3YwMwzOBVkHYQjeqRpdBWR9q-qJmIFgmfCEeBOaC1cDheZVc2ZqebGczkla5fQmrlp_cSOpjsxTr0g1XC6Eu8ElaiyCkueM2NC7Sd4ptvcsrQy0RF90EewRSCHv0VW5V6BtsTOyfph57W4Mi7LD8iRSiVz9b3HJN0ycZagadsUFc3CXhh_uTYAENEbmITb7AVC2tIZdw9Pj35RgFR9hj036oNfj1HxNbjyERHg5PGcNIfUKVWXTeoqxiNXnbNkOQvGYQJL3mQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=GIvMlHHhxo_KX3REMI-bvvldIDG2D3zoEB1-qUJ4KzLwCmcmpHvGrWG2q3TugddcmwAeeOrnmJKrqz8UOEYol4LR2uu2lhuquODpyuAYLHsFba2lm_byZMrvUyQxWGR5WPHEz5Cb6kqGBdfOlvpCDXhgCzSBEuJb6wR1ldayqvJF5L1-wAo9-Xyt6I2poZeJkQC62e4SC9UFhJY0Nu4_dWjnhcIuqQ-lh8TkgQFLmwWWponRPHFID2LTXW42m-58ZR4_IVYSzsWqxCTXHwHnWPbRAkiy-IC4bifiSSkDF8bz7_bWkNDtu5mobiiGNDetRWk8ZDm4wed0bfiiEIf1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=GIvMlHHhxo_KX3REMI-bvvldIDG2D3zoEB1-qUJ4KzLwCmcmpHvGrWG2q3TugddcmwAeeOrnmJKrqz8UOEYol4LR2uu2lhuquODpyuAYLHsFba2lm_byZMrvUyQxWGR5WPHEz5Cb6kqGBdfOlvpCDXhgCzSBEuJb6wR1ldayqvJF5L1-wAo9-Xyt6I2poZeJkQC62e4SC9UFhJY0Nu4_dWjnhcIuqQ-lh8TkgQFLmwWWponRPHFID2LTXW42m-58ZR4_IVYSzsWqxCTXHwHnWPbRAkiy-IC4bifiSSkDF8bz7_bWkNDtu5mobiiGNDetRWk8ZDm4wed0bfiiEIf1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=Ynk55h9yMrgweVROen7IorKN92PKpWa_FEbHI1-X7l66gaIb-nRYwqANcxzFcAZ4RE6w1bnIv1SGPwNm0kk71_jDeSzJOs5uoODX93RdF0bPgK5I4RDqmlstYJPWSzYsXsFu5ss_W01fG3KoNaeLpZxu7SV6xx6XtlRrOr66XWVETjmcPlO0kbtleN-XYpG9jirUP9nf9Dn4-HABi-Q0wvqcA69T99eEYLubbeWqQaAjBaDTf2uBCG8o_lh9XlAQnIpDbuojsHOeNhP9WyuXc8Zl-2RBQo0Yfl1fmQT5_B1GcSnVLA-8e384EZwH6Wcp1SYFRNSXalbhvEhlEG8H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=Ynk55h9yMrgweVROen7IorKN92PKpWa_FEbHI1-X7l66gaIb-nRYwqANcxzFcAZ4RE6w1bnIv1SGPwNm0kk71_jDeSzJOs5uoODX93RdF0bPgK5I4RDqmlstYJPWSzYsXsFu5ss_W01fG3KoNaeLpZxu7SV6xx6XtlRrOr66XWVETjmcPlO0kbtleN-XYpG9jirUP9nf9Dn4-HABi-Q0wvqcA69T99eEYLubbeWqQaAjBaDTf2uBCG8o_lh9XlAQnIpDbuojsHOeNhP9WyuXc8Zl-2RBQo0Yfl1fmQT5_B1GcSnVLA-8e384EZwH6Wcp1SYFRNSXalbhvEhlEG8H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8aguaphDqMWAA_gX9J6h6sKTpfWLMAkfECLbp9sKi7JW_ZTb-fkF-q3Ekq_K6Kdqb4DJAl-3IBmbqwe0px_M2bqLhfnNIZaCN8yuyv10XEu1FZdS6YfmG-x-9auq6-_5xH847R1vHXSciDmhMbcZLGcAWOVHrptwyJs3Al3O7iPqV5_c0C8tNbdGsSnuJmEVHWgqJ_SCe9GKlTf61ZFpMf2Yjmst3bPIcqIlOarG2G1rxGwCVrCuVE9ASYsKrM4DqU-UdhJAWhcinauHZgG81HWB0vUoL7B4myU4mzx_vFBAGSTT96fVPL8kHGFPfpjrqG0QUxsU-DC5xG4ttZsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLIHAL-YcUl73ze_2u-5-gnWg9dyx9WjRSpS4_HpwS_fPwH0Ea5izFOnE7rx0-Qt2O8XcDtJDV-JBRw39pAB4UBZ5tf4vjx1QPuDcRTZZqylICOJJRB6n-f1vUb7yXwef0aR1-PME9GbGD-JI975A-tLUtouZhlA9Sdgbpnmz3gZTHR7jDCBk6fo509Qk56yq-qonP5obO799Nr7hRk4_72XrMp8HvwmoXeD0E345mjC3DTWdFd61F2cEdjQ5bw1BJOZQ01OnjrL47Adntdcqg-gUYW4RhDd81Sd8Shl0VGvwpbNRdPUbfZf_N10o97v_D2WNaUJl5aH-y7vC3E_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=K-0Kh5gJztqZUAFRPOSCMl6IM3VQSp1CC1zMWVWCwpoXd9GuYP7wNhaZL3WMDAmc5FX0Nh7nPyVkVdZbvCSBMMaaM3Udlybc9OkQg_zh3F9AETZiaFIUSegBrqDlKCCx_vaIM1xj9i5ylKtdxOYDwwl2JK_KSzO1sgqBXTzmi7JaA2HP3R1z-QsryX64fjPueJL-zvdPgF2bzWdWs2MKFpC1I5HazPS6wjUkkU2KjRna8pDOMunXBfEpGeJAPgKWAvzvQyrMZ2PJ-KqiL_AiEF3KQh7nTCvr3ShNJ5hH6jgWxwottDGAH7DTeLc7klhV6D764BXO0kvZ3VerEdqfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=K-0Kh5gJztqZUAFRPOSCMl6IM3VQSp1CC1zMWVWCwpoXd9GuYP7wNhaZL3WMDAmc5FX0Nh7nPyVkVdZbvCSBMMaaM3Udlybc9OkQg_zh3F9AETZiaFIUSegBrqDlKCCx_vaIM1xj9i5ylKtdxOYDwwl2JK_KSzO1sgqBXTzmi7JaA2HP3R1z-QsryX64fjPueJL-zvdPgF2bzWdWs2MKFpC1I5HazPS6wjUkkU2KjRna8pDOMunXBfEpGeJAPgKWAvzvQyrMZ2PJ-KqiL_AiEF3KQh7nTCvr3ShNJ5hH6jgWxwottDGAH7DTeLc7klhV6D764BXO0kvZ3VerEdqfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfAxLBiaunYON1GRCxUjfOzT_dlyt0ybfFyJ44pRfT7fWhCte3lkjoQe_MMLx1u3812tlLs82TrdTDtY654dKeMMGOoSGoB9EEFun7F1O6JDblZn7RFw78gOR-syX5aFkL5rikTsh5KdmTccTI6w-I2eMy61xFmsb6gNoti3tHVzbOdHyTmfysV39FbJ_8oJxDb7LsjmOarxFnNyu1gV0BYzvPIlfJyY4X7lMcZCXVmdnMrhEB4ZKXPfzr855hw1G6tHvpmlFfiv7l-eh5tBaZY1GD3FnKT0jaAJ2R4tiUoCLxzfrPoON6CAzjbJA7YentwAjrK17bPw7_NDjDV3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhmRwlNYakw7M-uGEdbeRYibXVW5FcLIDezdtnqcXAphcmkJSR9k6bj1GGIMfUCo4AvBtnUW4OKBzRt5jIRKlwERFN0JXHjUXtbskEue5kF3Ekm_tcIP2UC1KhFW6agkCkp5qJheUGGJaWG90n9e4enMbAcxAhrJ9J7b0B-NgCBtM3qEn_T7glUNB8IUuSeQfES0QWjH74GxUSlFBYLkgqswirG8fC7EqBVskhkO0OAWeqzdoHMAvhaRV7UjInhOnUv6TKVcwlpslsvpplPBFsff87MP7hZ3y8FeAWbFkHMWBybKx1qHK8ElWx8U1eBZMRzMOF5VBfhb7qvexrK-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDr-P78wAZW82BXtSJyv225xcET8Lmbgt1hrmDN2DRYMdQcBD1Mf6FPVKND8utxKJpDa2yVWl9VMRagxDSldEDol5XKojug6rWZ5h47JLpOLtK0V98KBRV7pVggyz_csHDPLuvRLwbua72e9RvyfbZCt3vFlfevLfjBgz3L1wFap7-vYqT2UPvu62NR38emzMasyit_Hh8ddm4g41xt2Ge0n4AhYTpbPWst5NAz-z9XzuPxncGhABHBTUr2rR4xIay7Fk-9Vm9F55LObbBc4v8xzZavByBrtpYf5AVevMlVgf6tPLxct0beQyEviD9-EgLpzJJANJC0rYrkqVrCe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPSrarjD2p4dvifJk0lot3C8F4k01iQsxlssaQZA2ehp5n8UO4PRGILS3H7HqlSz3cET2isAVF3teIJHCMh5Cx0hBLQHcv7QHqaf5tYj9apP4qiInIWQs-W5pEcCaxt5hfAjP1avqO8Obhz7YN8u4bAQHZQdLZl9Kcv-AdUpamRG4RgY3hVcOe69u-zOmI3XyguN4-YAK-mEMZmeW6hEubQqwdz0fqL3CRxGoeSp_QOTzDRx_VJYJpBiz9ojrufWG0CFYisAWTSAt23GczXWp00JgqKne-g8RB1c4zV-I84iWJJ9pkfUfwB7gnAD4ONXueZptum_B8iwUSlDdnoF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=F_wVTjZpTqGe89kaEacuuRlH8GcTcQa0vY2Ptf-YXLwE52ORvWN34lQw8zq9bUfT355h2kPnB7swQu_P_jWyx9uOkH1Qdu1_dUt4ugc9LTfeMNetc9dJh8Y6jj4Yn33IZPH_T5WkY8JydWvY-5pE9jN-1F7NDfDQ47eCSZN6OlO0VUNJOfcfUHhXw8TYyzpc_MYO2IIx6Up-95-JSwtI248bkdMJm1gI_OpiwXbxofT8mh__n7BYGisHsRT5g0vWHVDt3aemU8wd6FlQ4NvvM7KSyN6dmPmzk9USxAC89Xls0COX5zzFNmhzSarvepIZFae2eqIp_nQKYqv0ZL5V4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=F_wVTjZpTqGe89kaEacuuRlH8GcTcQa0vY2Ptf-YXLwE52ORvWN34lQw8zq9bUfT355h2kPnB7swQu_P_jWyx9uOkH1Qdu1_dUt4ugc9LTfeMNetc9dJh8Y6jj4Yn33IZPH_T5WkY8JydWvY-5pE9jN-1F7NDfDQ47eCSZN6OlO0VUNJOfcfUHhXw8TYyzpc_MYO2IIx6Up-95-JSwtI248bkdMJm1gI_OpiwXbxofT8mh__n7BYGisHsRT5g0vWHVDt3aemU8wd6FlQ4NvvM7KSyN6dmPmzk9USxAC89Xls0COX5zzFNmhzSarvepIZFae2eqIp_nQKYqv0ZL5V4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=M_0SJPwy1u1zxZpTpWyYGfU0Xk8TChvdesCmvz6xxOc2FsGgSjCf4iMCadJW_ZEhrr0yAX2F97GHzbOuma1JwpKUzHCXn4ZXyJr-XMVYnBIZ9h8nmvWxPybtZ2Du1oIwMk-6PuPi-UAn5Qz8zRcf7nIELcj6Gjg1pcWshtfpGL2bThC2mKBjqgCsf42ojdiw7uAeFlgkk1KlQ-6uxl8a3mUgRpTyRkAThPH_Teq-gt380mhQt4zb21txkOWGvkIglLcTuteY8y1s7LnjZfrjCijkOkKLMVTxum3RGkc5CXlfbbY0bwraryv4zKKOsJdS5BDE9P8iW8CLxgu_G57mAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=M_0SJPwy1u1zxZpTpWyYGfU0Xk8TChvdesCmvz6xxOc2FsGgSjCf4iMCadJW_ZEhrr0yAX2F97GHzbOuma1JwpKUzHCXn4ZXyJr-XMVYnBIZ9h8nmvWxPybtZ2Du1oIwMk-6PuPi-UAn5Qz8zRcf7nIELcj6Gjg1pcWshtfpGL2bThC2mKBjqgCsf42ojdiw7uAeFlgkk1KlQ-6uxl8a3mUgRpTyRkAThPH_Teq-gt380mhQt4zb21txkOWGvkIglLcTuteY8y1s7LnjZfrjCijkOkKLMVTxum3RGkc5CXlfbbY0bwraryv4zKKOsJdS5BDE9P8iW8CLxgu_G57mAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohynUa39-wzLPRUC2EF6wuSuR7DX5qx1USB7el5osZyFLmngSRAFETsOq63TNwuztHcfuW_8C7gl34yT5M86Y4Q55VoH4sSESx14deGT8QIOhCg7Cg__9_cNrbg_akLVZsQj8aPLqLRhcnGKES33TllLMxe2Xs5R4gNU0o0GR0HRSYSoDcFCr4Ov8Y6pg89cJpNdRQaBxCifumlcWr2g2_rKn-2NGheM_dRDUYnnfzd_EX9R8qbRn3iiDpslyPgeHyP9M9snZMbD9W2ZPH9fzfosKd7gluG4easO_kk1YQDh7egIr_6_e0PaIKZtzfD-v9GomZnc54LzJC-wQpDGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1kbcdKvI5M11buVLvB0VokwnUrhIeORWWWjSbH38mDhjJ9dQXTGN2HWi9iEpwJWmBn0tDW1snmMlcYy1y502721pA3HJ6ggURGveoZN6i9G82nzmehEtLjCAT5WngtvnOrELnFVgeOCbdi6j9DAhIhKhAqpBaM3XFZfgBcC1hEaVGcup9QOrGmB8V7IVECH2zxxdsBl_MY-stke-ir8wOECms456peWQEmSKdSjSZwRN3sXdfMJAfUkr0DfSV7N9Zf8tZPOmaBwXP89j0YTdL0XMMKTdC-cJgBOYqYPWdBd3wpNbjjq1Y4oNml4-MoAD7ixrWUCYZ74MB7b-9nTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi3lRTkKxkatF12fCnakiRJRvgFeOBkdrxNsVOHezbTjsi6A5dQ-FLKB8izg75GKqOTziDVaTCVqL77RylazGI8fHqU2J1Jsre9J3JjmVVEDl2tqPDAqvcZ6y_qdcT4HMQd0o58jkBoWTLldqnoJvMaaaIEoEZm3tz5Q-dAp3twZTbi4_bC0uMsNUjkdY_P8YR8owWeaA24vSBbFqaQH0pl4jdh9XfMIGk_OgJRzt5PPiYi_o7UfnvldvDvsHIOhar0-seU7mBLngyT7jbjd3bSumsFxRy97Aa6OKlbpIaOMenj43S-l0P_wIRgPGVxaOoGlonqq9uxO7PNiYkLCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=vuqeoPHjwE0D_nNZLrZAZd3g8m3J-FPIxzfnAa5m4Id5E5brtTqUucsjz7yFBZ7gaKc8K2BaTt2RrQz_s46xygRp7aG4l4r0FGUcrpWc8hhcQ-6L0b2CDL5RfTy0mrmiINqvxPvUcrMGFh7s8j-SR3gMnaicI4OGUT7Boj_kqb_ldhKLsBwKqViKdkCcDEC1Yf60641C3N6Dw5RBSatP8Xns2e7X3wbyddKbcsAwNhYBZRqDvMy4vjbQfPMD3pQq42NRktstFqTLdZeUAB3nSNr0iBRr7XW0ys8hL9xs0FhFF6EpyJm6Uxo7ZAO4R_kX13y57qoG9uDalaNWDXxkAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=vuqeoPHjwE0D_nNZLrZAZd3g8m3J-FPIxzfnAa5m4Id5E5brtTqUucsjz7yFBZ7gaKc8K2BaTt2RrQz_s46xygRp7aG4l4r0FGUcrpWc8hhcQ-6L0b2CDL5RfTy0mrmiINqvxPvUcrMGFh7s8j-SR3gMnaicI4OGUT7Boj_kqb_ldhKLsBwKqViKdkCcDEC1Yf60641C3N6Dw5RBSatP8Xns2e7X3wbyddKbcsAwNhYBZRqDvMy4vjbQfPMD3pQq42NRktstFqTLdZeUAB3nSNr0iBRr7XW0ys8hL9xs0FhFF6EpyJm6Uxo7ZAO4R_kX13y57qoG9uDalaNWDXxkAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=UwNaC_aqobePutFteFuEtiRLgfDC8vUacNg-XzPnjqTeibJRXuIwJco0ohYA1yOVKZ3P8XibYM6jbVdgUXjnAdro99nkJF4Ix6XobJWm12RuD775ZmIRK70tUIdLmLvytW6Pwft8qNVJVIMBEY43mjonwLkxc-7MSpSZIrLVjY_pbOiTpeKP-jsNtdhGhl_hM7Em2tjx9ag7Joia-MZMhYj7Qwyq0yDhgkaCb81hQDmqTzDJIF-tW66oxg6egGn17tFYvvXsuP3xqtCZ3jwEYf22zYiqm9zUWPQ8NCgGL-GLE4rFqOAPslTERPT88pYWs9vVv9VtdDUwC5bTU_1kJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=UwNaC_aqobePutFteFuEtiRLgfDC8vUacNg-XzPnjqTeibJRXuIwJco0ohYA1yOVKZ3P8XibYM6jbVdgUXjnAdro99nkJF4Ix6XobJWm12RuD775ZmIRK70tUIdLmLvytW6Pwft8qNVJVIMBEY43mjonwLkxc-7MSpSZIrLVjY_pbOiTpeKP-jsNtdhGhl_hM7Em2tjx9ag7Joia-MZMhYj7Qwyq0yDhgkaCb81hQDmqTzDJIF-tW66oxg6egGn17tFYvvXsuP3xqtCZ3jwEYf22zYiqm9zUWPQ8NCgGL-GLE4rFqOAPslTERPT88pYWs9vVv9VtdDUwC5bTU_1kJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین.
مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است!
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZnaDMeLV1Mc46M9RgMzxb4xdp0mgpW3VRJ6LCeI6e0qe1W83jjgg8_eEmVehwX7cyY9IxtzWb1zZegmNyY0FhmgaaCbsquea8LsTSc17-2Ui7qO5fToKa25fr8dPuAxi4Z0LltApoH86RdRovmhRqowau0FADxLDWou25_NiRro945ycWqafL7WYOuMM-80BzqK0mY-qJcWI5Buaor_EmsJF1eFyKbRTrt4pyqqOY5yaATM5vhukJoBq-WktMREugVLHnOhiLcv0v1Im2aUoDOcIrD7eS6Hvie5zbknMDk9lllYfCscT9qWBy7H_pobCI-BYaNEUzkZaz_kFqlKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOh9iolbGrhwnfK78n4-Z_mzDFZVbXWdZoGmRZco_692x99-1cbBfAL26r8HWfy18sdDStSnrfb4oNbvaG2r549H_5wyCVzxxSi6jb3InxLFcUlf48zzLUOdjldbW6EPtvPl_Sln0HJV87yKrXqDOKrzaBiQy9xG9F8npviN8cNHrGOV04oPiQpeLRxMYsuytXY3ASL0S9n7dUMIBE29M1th9XtAFa5iQzBej_OD0uSTIfMqj_O6_IwnZPzDIDMisJkc1118o_9Im0BGn_Lp8eCi5xGwPwsMYOO5RUFHD5aZ3k6O8t1fcYXF-_2gG0psz0s1OpkBr2zpb3ckj1diZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQkrGN9e6T_KQhFXf_YFWLSx9oW8TclfB7mLAoKhz1pCZTTewx8hJU5TB3Ca-9r8ODdsDGD-cFOyHIHVHlo16YC0PVH6q08UDH1yrvyc-ycQleI0ZEx-K-W-Fm1z2rq7yK56XCBVM8nnOmSeDg4jHBY-OdqpPQzvOEbrdJxn0qKHwayqxZKB0DpYcvkIFP5DuVH0PCPgity05Mv57dVKIMTRGsM95npZPuZpo2BsRxdbYzTjDYK0WHkKv1TDXKHwitkSsCVAqzQbO_a2M9kj2UhK9q71OoW7ukEyNUTPl9mLnbgKzRzD4F3l_k6P7RJkJxgvyIUm1lla-_7YvVw3-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLNLJ1jy5HweK-myNk5GoutUaZsUlf4dFjLvdRvXaAr5YbEl3sMWSQqWTfVC0l9ZYzH7SF-MJYXxxU-7AuB7kvR9cp7YnPDdzKY279ciy7P_m4gmzLl_8OwOIcwLiHn8Vhv8JzXNfk54X-J4jLkmqLRnNZbbq-7cbtov39Vmxa22jaSwz9YEJHlxTGtqGn35hIU8lw785r7zLTlGqPtL5_1vHbbhZRhJ5myrui5eGSeeLmGIB4O1bAlc8E5y71d98xlKPVxFyKajbSDu3RBAgC1VHpY78eZPEB-7ihlQdTgrmlF4zib0TE_7Vewc6g4FKDgXsKs26arTLZ_CCYGIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq-2az3IP0AO76YYPe7o_9uQ9DWdPZ6reNY5uZWoYLzUBRQGsigKcA9o5Oev-H6UtuGPur9TN1mvdbrw-tOkbt1nysHrFqbzYIEtvSQaFYAqZGDPjRPInEvTeaDR-w6PXHtyF04wSq4MxwsZeN18p1a9VLB57cxFb5r4MpZfCa87yXwp1mvQ4XPfcYRLlkoC4eKS0AcM4NNXCCGfUWayaFkSGQDKlAmLnTjH-CTHu-sOr6bjSfSmWP3nHojFOu65O1UJtiX5jZIRWskQwlStKqAH45eh3pXI9g1OixgN5JDnR3hpnuiPqCNBxxaT4KH81K3Lw4NMTvqAaeDBzB-OOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chN20XwjkLhnTCrMAiF3v5u8jCuee1Jj13X46YO5Ef2YgaqBU4rCfbwTBfRtIuJ359KwxLvdBpFy3h5AknsLA1ZJliICyizWWs9GDNfSS1Y8oWLQOiBPoPeEz8ydmQXpK4GmYUnnmfOnZkKmkYh5dt1tFcGdeWtyRsOuzKH058by_9Y53InhGdmeCZyjhoi0hEd5pWrug0dHNttpZFS12W_rONZ73uZX_urO7ZVwABO3FCuUpxh1-HFQzO4bSJV35T1wFEjXk_pcH4Rv6oI5ZvLBjQ5O-Y8l5IXhhhiUDgbz4xMqxkNDNmTC2tcHsi9vGxTEnpxeNyB-UGiaiG2_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16443" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیویورک‌تایمز به نقل از منابعی در سپاه:
مجتبی خامنه‌ای خواهان حضور در مراسم خاکسپاری پدرش در مشهد و اقامه نماز میته، اما مقام‌های امنیتی تاکنون با این درخواست مخالفت کردن.
به گفته این منابع، نگرانی از احتمال سوءاستفاده اسرائیل برای ترور یا شناسایی محل اختفای اون، دلیل این مخالفته.
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/16442" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj_O75wAdNk8Jh2InBYo6xryxQ3z5VK2OjJeZtcUdFGF6EQLeKLETg-fI4hr2AZ-7-sVy3rdA_3SXKBnMpDMo1qRFmDajd4Z_e1NYVYpkOOnSOdK8a83wV83bSghhWbs0hrMLs6BYhRec4Ek-U7r2mW8eGtr8QPM2X0t8znMZCVN_JnSUpi20beI0HW-TiiOq6N0ob4cFTqKSnggN0KIjZwcn6LEphLwQe8GNpyb-jA9IJStvgzZao0i6SswKHjbdrgem1KfAFuPswIPguNSETDmVQ8prwWtNcb1n8L3w4cRYCy0ISmOOfK3Kzs2XEgPl35NNwy4uF6q5qGTLH6uzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار علی عظمایی امروز به عنوان فرمانده جدید نیروی دریایی سپاه معرفی شد.
فرمانده قبلی سردار تنگسیری بود که توی جنگ کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16441" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkChMOBE31Opyw3i3g_An-7VOMS72iz4p2WVInuS0iyhGWExhOEuS_TOuSXMzviiehD-ywTsQyMvBPl0Xgpg9dNS5VR0-d-c9Q5CxbzLMUNUtVu0-SofoD56AJhxwpwwpJb4an1gJupS88UsjtDIm1H-6atBm3c2xJ-wOGnHm8Zt3fZWeDu8vCcALWWmf8_VtzJb_oOshPZ6irw5HDsm8nXJKJMeN5RXGWc7USBAmy71g6Dnuy8fAn0kHxLAnc5p6DyN8r9UJk-6u18p5YJ5qT0NOY82v-PU_CYabuYckKY3RR5XwDgdppn8pWAizWjAA88LKdMuCoeyIY2r1pdjujcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkChMOBE31Opyw3i3g_An-7VOMS72iz4p2WVInuS0iyhGWExhOEuS_TOuSXMzviiehD-ywTsQyMvBPl0Xgpg9dNS5VR0-d-c9Q5CxbzLMUNUtVu0-SofoD56AJhxwpwwpJb4an1gJupS88UsjtDIm1H-6atBm3c2xJ-wOGnHm8Zt3fZWeDu8vCcALWWmf8_VtzJb_oOshPZ6irw5HDsm8nXJKJMeN5RXGWc7USBAmy71g6Dnuy8fAn0kHxLAnc5p6DyN8r9UJk-6u18p5YJ5qT0NOY82v-PU_CYabuYckKY3RR5XwDgdppn8pWAizWjAA88LKdMuCoeyIY2r1pdjujcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzigYb4fwI0yF_2aqbOqqEFscjWXTvtlKGSl73jOQfkDt5ae5HM9TDFcip9OfebrHSLqe0tRqCYw5-b9eg9nncA2N6cdnoFzPobY3VWbVWhY1SICi7sQpv8BhyAXfv7eqdCUeLXGB8ixBpbTOHpjHed9JK1IZ76X-lq6UwckLhIQPaq9isnATUkBYeYkFAvfdayNdRNu_9jKCmfmqGoRE5Zrt7N2J5vkdopCKWQKO9EucCzdvx5OofBMU9eL_wLMh7d_Ga_sS2OFZY02_2-1E_b806ZmTJ87bM7ym-U--lLDaYsJJYVxVYFs9ZoK-k5W6UACy1IuzXHdZ5QVKydldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le4qw97Sqk10ZGcjeCzEpgTXhmO06DfS8DhyICnjuvrzDU6ZRvudh7hh0uY3Xy6UfHZ0yQ1Fkh57VGFC1hCYQ-ZA9EZQ9l1w1eMCZOEH-4pa85bMRmK7rFUNFmAj6gdQSuYaDxA4H6W92wtKFaZ-53YLAfHdv26qCSI0NxnCtY_oGbv7wH3HH2tdEgclDaJfU0JNbVq5QrjnqdE0OG4xd0km2O2YFggZ-I7yowtoMnaCuJW2fiZoe2SNyN88CRsCR6E9Wz-MMGKGTTvn-HsHFwOnazzQZZqWRnJ3wlO_yQ3IjVpVpErxfM6UvxJOGoMEm6ozxdT3Iuyeks3oGAlWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSR13pbqcEz1oe0FrecWEZ_-_EMT-58BLHpJb-HvYmQ2_uBmD1A29dXeTl7SKVk449zv460MNFmFvgZHRCoqqxU-spek2bMAljhXxBkxDmH6tLfb8FhLejxPJj8awrNMk9mDVOAxUz37dJdGGXQLnounFkvtSckPXwcb-kqQq5BZL-eUjJi0ALLYocPLFkUwvjv3L2CYUoo0WNh5jLoHY8XFd8P4GdY3fcGKnlBjCkOGaYj0fz_gxChfHQXOqTJpEJUrZGaUtVTWm3e6Norw3e6ny0HPNeFChD032BgAlg_i8q54TTXoipdggsCv76LnLPihkqX2YMH9Okkcyw4ihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPoM2pyP0B-tVLYFcm0lzSgBl5aqRzP2y03kXurY1tWQ1HwwJNmYRzGN7_aybWtgX2gODB1zHwXLB7pZOJooW4sDYD2HKo03nnFdpBrTnjsOvo_tNc0_kMfcv1VRcz_ZrfxVNlnSuuOMfV2v98CcFVUUq4EIvwBa8lPMOC3vtPni_voZP-9eypWnGiqDAThpx9euDvLN8RkP-7_NE0a039bZ5wZAyQui1IPZBSQj8cb5bjG_G3gw_WqbrJkHaPeOTCQmJ-lo-PrvBky_2fmvpEovErkCNGAR4lxQ9RACDXqzQPpCv6mV2HyNzYfG7jxWtIybRgjFA-oiuH8lDsmXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
