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
<img src="https://cdn4.telesco.pe/file/rbPGknbRdlXdLSZ2BQX0xP_IHZ1WdynCiMUtgv0oVGdE2m3g2iuQ0oEaqfjWm1NzJErwKEsrX3b3itLmkHU3Eri96G4ZhDU06X4GpAXirPI0G2dHD0-mspK1VXCjvwOAZCpy_goSUyXNNWizai1-f1pdpsFTVPlfNbpDNH7wK9_h7cgxQIE-DTA4v0DVAtoP6lxBOa6kWYZoBRZnMEyCwb3_pY2y1umWpbiW_oGBC-S3M-9awsalzi5dCSFDaHJCOF7M3_XnyiZ2Xvjq7FQXND8WCnLBEo6aeMjLR0GgNlaYD-OcJM1BvpHiCpAsrb9ED-g8mg_8XpEiHHe41JPTsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-690866">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromزی‌ ویژن | zeevision</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfEbYWFP4jB8ORHMAra1EXkYloZrzMt4XRfF6KcVbrtEXi5S6ulhudC2XFSBx7SGZmaH4DyMwdFLKmdz1Zx-JBJePeMo1LXyZHnE-PSKtz-jESE81D7ApDsl3g0xNENK0UuJfa4lRhRnjcbSIKp-SKyMB9ocN-G7XI3TchfsG8_KaRC9uYQxUTAvdfHdljXi1jZXosTL4nr8sWtcJVO_FRmVB9DskUm0L970szZwSuvFklkEbOnOeBDXcMPymUedTkqttXoQRm_BFIp-F-mFVxzbRLPsodO9eY10L-os_r5xkfuEkTLZzttYxQ_Q_FSqxqk5T8siLxllsePmHRjG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه بار دیگه ببینم بشنوم دور و بر اون میچرخی…»
هم اکنون تماشای قسمت سوم سریال «نیم رخ» در پلتفرم
#زی_ویژن
تهیه‌کننده: علی طلوعی
کارگردان: رضا شریفی
نویسنده:مهرداد نیکنام
محصولی از
#نبراس_پیکچرز
تماشای قسمت سوم از زی ویژن
📣
@zeevision
🌐
www.zeevision.ir</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/690866" target="_blank">📅 16:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690865">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه آمریکا به الجزیره: هیئت ایران طبق تعهدات کشور میزبان در مجمع عمومی سازمان ملل حضور خواهد یافت
🔹
هیئت ایرانی نسبت به سال‌های گذشته کوچک‌تر خواهد بود و محدودیت‌هایی برای آنها در نظر گرفته شده.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/690865" target="_blank">📅 15:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690864">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6039264e.mp4?token=RZsf9PT4IrKF3j4JkTe_nmLtkkST6O0oe6-kYteZ7Apvg80CzyvzxfpqotAqY9X3UCOHchzEG9TUBj4p8kCdYsuFW2-5dfnTiqSQ5gzcITUZ0gDPPljZcIgUCPTR-xZEriRQYvoz73FxSDSrtKY5PxHqZU49uO-QjVVdn2hv4bgaoPPeg02sMJR2gFT3IQ_Y7d_5AxyzsLqcx6eW-Koiv2M9NTjuxW-wUhvgWAVSZnyEA-U9-7ghKahnodIYJU7sh5bjqEZ_8URgcKCVMLOtedpmffp0jV0OGaqX0PzQQcbU50rKqelWPQnxGqSQy8VgvYng5u4MrsMWusx7W5QiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6039264e.mp4?token=RZsf9PT4IrKF3j4JkTe_nmLtkkST6O0oe6-kYteZ7Apvg80CzyvzxfpqotAqY9X3UCOHchzEG9TUBj4p8kCdYsuFW2-5dfnTiqSQ5gzcITUZ0gDPPljZcIgUCPTR-xZEriRQYvoz73FxSDSrtKY5PxHqZU49uO-QjVVdn2hv4bgaoPPeg02sMJR2gFT3IQ_Y7d_5AxyzsLqcx6eW-Koiv2M9NTjuxW-wUhvgWAVSZnyEA-U9-7ghKahnodIYJU7sh5bjqEZ_8URgcKCVMLOtedpmffp0jV0OGaqX0PzQQcbU50rKqelWPQnxGqSQy8VgvYng5u4MrsMWusx7W5QiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروط جالب عمو فروتن(فیتیله‌ها)برای فرزندانش وقتی می‌خواهند خانه مستقل داشته باشند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/690864" target="_blank">📅 15:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690863">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
عربستان صادرات نفت به اروپا را قطع می‌کند
بلومبرگ:
🔹
آرامکوی عربستان به دست‌کم دو پالایشگاه اروپایی اعلام کرده ماه آینده نفت خام دریافت نخواهند کرد؛ این تصمیم پس از حمله به خط لوله اصلی عربستان به سمت دریای سرخ اتخاذ شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/690863" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnGzw0Tsgx_qvNEwwadguvkJbq--1vD5Xe3Xas6WxHFuldvoxOo6Ueimhtc1SepLVklP9Tj-nMDALm-git9U7pXFNcCr6kKOffsZNA3ZK0AKmBc1MjrVZI0NigYzYRpRL9zgQTfVl2m2I3VNa-J3T_REpnoXlZ5YfCU-LG8aQgXVYzu1pra7pbGF8QO9ukY3HZiZWhTEM-8enx95TycMGesTq7hC-tMeAFYEawMEmHQEu9xMnPqnFX5Wp5dSeBVyUpIJDp1TBOOroEvIzYWmdQXB_gfdqhPj3ZmdQ4_dELCaaF100l0Bgq6WVGAWF8XA2f1ov9Kwu4oEw5711c8Plg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOAKLykrlRQW0mxcH5F7uf7KoY-3PS4gqnIOCwavXp51TSXSVk4mF7kGplPLWhvB3yf1ZZN2DoXslrMdCY8RsSnVo4fUywPpMrQ0gecllBU0ShGN3jM-LIUDyKOiRMh5JocP9hz2nSaFpMLG2arWrvGfVd--qZv1Rm4oXghw2Gja2KwithfOLmvCSWNOK4FAKLuodGSyoEl2KNrzxpNsBDwGSWzQXthOg5fU6JzmrjZjFm6vL49ubs27pXl4fNM8UDeicr381sd_sCYgmA2qwjx4Fe9ScXMms0htPk3c1DNm0ZiO4G3X8oSA7JznsUM1cA30bgPT3aZQQffpw7C9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRQnH42iyIKMhXIBjlM89wikNpkwF_I6badVzlrj20jf6tXOkJcJeiabKdxsmAazj3Sdwk44WLlr5A6LIbQX8xUSUvJEs9ZwVT4pYbS3-vrVL0_EL014OUB3tNKaL-p8UCmVPxIeEJuEiB2CtQk3rokxAM_cz4B3flEA3neeAGlGQ959J375DrCzyX8ETKWYveugYfrIWMo8cZjHGAvsWwU96YjBkcQVUvmmr6hDAJX4BIFO2mDRqBNFB9E2YpJBhsN8Nzd-lHg6yw4E_yOsv0O0FVVTTnWk_fghTEpYCI-DkgKorOElj_WNK_1-2EMm0sQHJoYsIqTQCHUD9gKGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcCw18TdAb9d12EexMbLIHEmwNwKgQrafmy2bWu93JdtdLhntHl2KN2vTGBLPNSlGOIF5Tn-MricqFnxz9vn2fgPqjMBO-3QXgGH4gkaaion4Qn4gC85khKE0czmGer7yGujzJIWoerSWDb5VwJTxs6Lhqmg-rV2CwJsjFkXgWUADJ7jz7QLN3jVG9EPMicOryNRcPlizEmUTC8As733Hg5O_Hov_RKI71FAgrlU4-8gPpq4261yuLT39I_ct3qAaRFH_CcB4hYBoa8Uu4aCnL15K5r2noCjQ8pK4uuNdvbPzqxC4iDKa7eXmmQPCNCqvMbK_wy6Rfkafoacg8_DoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور زنان جامعه مهندسین کشور در رزمایش مقتدرانه جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/690859" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پز دادن با برندهای غربی؛ خیانتِ نادیدنی به سفره کارگران ایرانی | لوازم خانگی ایرانی چگونه ورق را برگرداند؟
🔹
در دنیای مدرن امروز، هیچ کشوری پایداری و رشد اقتصادی خود را بر پایه واردات بی‌رویه و وابستگی مطلق به برندهای خارجی بنا نکرده است. نگاهی به استراتژی‌های کلان اقتصادی از شرق آسیا تا قلب اروپا و آمریکا نشان می‌دهد که دفاع از «تولید داخل» و تقویت زیرساخت‌های صنعتی، خط قرمز و شریان حیاتی توسعه اقتصادی در تمامی دولتمردی‌های هوشمندانه است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245912</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/690858" target="_blank">📅 15:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSuma0DW4kL1WCX0UgawX7ISIP0UuNBHR79mCDktjjRqnvlsuAOagUN6uvfv_6jCxBEDSWS8SDzuhgAHpG42mIlnjAFch82ma0bc2qxVPQ1qDRJoGVb_Pvtoxu0AE4TaAFjN4nDE-1dJxh5quHcalbgY22YEg3W7rp6j-EdcYVaL78BxyHAbRSvhrsHsxh-TrQtZI_vzhQ-LCVrqXYap8BweurXPsVKaDYRlTK5GNzUYxbddvZqSTE8YvGdFRhak7ldF0xMtb7i2hpXUdHCrpW2utzyR2Q8AAEJ4s_8kyvcMWxo2MVUewL_W7immM94Q6BT-sW8PjRmlYbmuNYnIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازنشستگی رونالدو کنسل شد؟!
🔹
نام کریستیانو رونالدو در فهرست جدید پرتغال برای بازی‌های پیش‌رو قرار گرفت؛ این در حالی است که شایعاتی درباره خداحافظی او از تیم ملی مطرح شده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/690857" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
انصارالله: همه حق عبور از باب‌المندب را دارند جز عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/690856" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a150198.mp4?token=vfcLPZ4n5FYWj_vZkW9AI2oMxCfybSQ-QZ7sysBsp7NPFp7cMXwjM3RPIRr3F2LThYq9yUgwTGHb_Se4CyB9eef6GJAXRLKv8FjCK13mDLLtXJ2CVl1y3lSvB7x-No2uylaRIb89lqQQvXZ9a2aarhE4cHxz7VbQpscCb2zxUSyaASJ5zJEEz-l_8SlZHVU-PQF4Q626k7ZFlXZpH6y9xpCRhnPYMio9wtFCAUN_U8OcYeyamDobW4ZFuHG0z4_T0htevNRzUwVdKt-HOHP3wW5SiNTUHiNVP6-lnJF_3MbtpJ5_qVEko1Khcwj_56XV4ekghSReqhgoKuZqP2GpcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a150198.mp4?token=vfcLPZ4n5FYWj_vZkW9AI2oMxCfybSQ-QZ7sysBsp7NPFp7cMXwjM3RPIRr3F2LThYq9yUgwTGHb_Se4CyB9eef6GJAXRLKv8FjCK13mDLLtXJ2CVl1y3lSvB7x-No2uylaRIb89lqQQvXZ9a2aarhE4cHxz7VbQpscCb2zxUSyaASJ5zJEEz-l_8SlZHVU-PQF4Q626k7ZFlXZpH6y9xpCRhnPYMio9wtFCAUN_U8OcYeyamDobW4ZFuHG0z4_T0htevNRzUwVdKt-HOHP3wW5SiNTUHiNVP6-lnJF_3MbtpJ5_qVEko1Khcwj_56XV4ekghSReqhgoKuZqP2GpcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر مشهور عرب: جنگ ایران و کشورهای منطقه، معادلات امنیتی خلیج فارس را تغییر داده است و آسیب‌پذیری کشورهای منطقه را آشکار کرد
دکتر خالد بیدون، تحلیلگر مشهور عرب و استاد حقوق دانشگاه ایالتی آریزونا در
#گفتگو
با خبرفوری:
🔹
ایران مزیت جغرافیایی دارد، اما کشورهای منطقه به پیشرفته‌ترین تسلیحات نظامی دسترسی دارند.
🔹
به گفته بیدون، کشورهای منطقه در حال بازنگری در میزان اتکای خود به اتحاد با آمریکا هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/690855" target="_blank">📅 15:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690853">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2vu_2TUEiMyTndsviCnZGyR3CQ77_bIFii1kxVzZcPJBUGjPlncebsZLCdpeakEY2rBRAIK4BLII4DbqwiIIzMxM9ykmdlFm0-RQ7WNUOZOYiXOciBQd6Lex9j4c30V9RyznRk1ndtv4PgmrKdBcVlsMSVRmubOuwPJ5X7bzWglpn9obaTubfOqeNXqltAmEKx1V4sn8HA4wZPKtWYsuJKs7ctRSA44FJsAWJ0YSD34Bg5vS1RRC_3RyCsMNdIrdWdZzHtD99L1ZjUwJOyhSje9g6Bx4u36zULojwg3a87KpvORLhBf7-GWqcIZp_5g51Zi9FHSFP8xyKitXu2Nwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tm4c4qQ1Wd-Ge3EEl-nrEOpYuBm9Nuce0QGtCF1M2s4D2xw_tIRetqcuI1Hwi5ZiNn4AFgrfb0bdgzY4jvNXfHIGVLXw1k7tJCj5NwuEL0qKvkDKqaajyMDFUY7a2BFHHJ5TCAwDipuZAXwZTQsNWvmBueJduJRhZRZb9YCDUvHFzw-1GqEj4Yej6-a-manfv-yPFCNUPrWZ8sb4cPiiadqZt9BK0o7K4QwqQlZnhJiyYP9WKicJt7X3aQ7awWeeY9EFSjBAPLVh6w-wclKGtM3X5bsGkAKp1UOV1Vbnjhm0woI9IBYudplhbr7egDuSf-K62ZIb_FuuFDPcL9rVsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور دانشجویان علوم پزشکی تهران و مدافعان سلامت در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/690853" target="_blank">📅 15:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690852">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krUcdVB3Hhhfg1w7owXad4XIyiDVuvPFoxUQiTOx4HOV3AW4RJFc5WIFmwzmlZpzxZ6dd-vmgxj4GuONw3fcTS8TYP6M3kuNF7nrOhRovDQXamabPkKV5AAfZSHcpBihn1co6CM4FREpLdF28fhaWKS4UnBbGWXVmsvIzhOAIhxZ87GNBUA8nb9XnuoduMAwjmtbH_egnDEzSlOmOsg9bcjrD-chNGiyUoAwPDiBwjA-AYO2d146XEuJI6NkjSVujkkd9HaaXqnpIwxmzoklO7I9coQFaol0Ptqx7vrTJtz9k855qPCGKtBnUKkneLOmr89fLoqG43kcHwkn_5LN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690852" target="_blank">📅 15:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690851">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ade4a47c6.mp4?token=IyMIf0CqoBwVEosymX4SfdolxqmM2OmyfjmGthXKLO3qHr_kSdZkUkWfB9Io4n6hMtVDWPGOlX-qtVkfHfjbJX8lUvcHi1ZVmZIkNpaYpzloMVqT8IP8x_woHp8R48Q042_CV4p_DnkDO6Hxz7qJ1LDYMwEAPz2zBk7N210USK1TYcjwAnz6amG2QVBSeaiWxPTCuqDAGcwaGdrBI4QQroVJSiiSpTinPsGbWggwj5Eab3YUPro7OfgT1nKx0JdeIqWfVfNXf3CH2EyHYoIe7NjLGytVlUAG19_3nAoByc9OBOS0FDoqBMzz63q0szoe0jXI7pRuAOaR9uZO5m9sMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ade4a47c6.mp4?token=IyMIf0CqoBwVEosymX4SfdolxqmM2OmyfjmGthXKLO3qHr_kSdZkUkWfB9Io4n6hMtVDWPGOlX-qtVkfHfjbJX8lUvcHi1ZVmZIkNpaYpzloMVqT8IP8x_woHp8R48Q042_CV4p_DnkDO6Hxz7qJ1LDYMwEAPz2zBk7N210USK1TYcjwAnz6amG2QVBSeaiWxPTCuqDAGcwaGdrBI4QQroVJSiiSpTinPsGbWggwj5Eab3YUPro7OfgT1nKx0JdeIqWfVfNXf3CH2EyHYoIe7NjLGytVlUAG19_3nAoByc9OBOS0FDoqBMzz63q0szoe0jXI7pRuAOaR9uZO5m9sMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی که در ایران نجات داده شد: چتر نجاتم در حمله اولیه آسیب دید و به طور کامل باز نشد
🔹
با سرعت ۱۶۰ کیلومتر در ساعت به زمین برخورد کردم و در این حادثه، ستون فقرات، بازو و شانه‌ام شکست. با وجود این جراحات، از دره‌ای که فرود آمده بودم، یک مسیر کوهستانی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/690851" target="_blank">📅 15:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690850">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3617254b.mp4?token=lGsGaar0IKf8ZHyvJR_WYIui5mn5wVt5B5rr3_VIpE4KQOAGygkbv74jFfsSUOEObJbnmKOzyreivwpZ_GkJvoH1e4K8r8a62A8tAPmAHQK6sfb2FN9tZafCfmzYhPn2tN_ySIezZdd3qoTsaMDYVoE5WaGvSCAXNMtxiI7Rg2Y64pHGBaz2G_EQ5yohnHFDqLYxgGnV4T3JI4rQqi194rnvwP8TkVv6ahhtP5Kx5o7gobOVxs5CjVx6o-3k_fkgTU5cnswSWbUwmGLQMYH5_4exp3O9zsbSaLrOX9gtZWhuR3fNItF7g9E5sngfNPSKAxw6TjaHnV5eh_vFDiqVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3617254b.mp4?token=lGsGaar0IKf8ZHyvJR_WYIui5mn5wVt5B5rr3_VIpE4KQOAGygkbv74jFfsSUOEObJbnmKOzyreivwpZ_GkJvoH1e4K8r8a62A8tAPmAHQK6sfb2FN9tZafCfmzYhPn2tN_ySIezZdd3qoTsaMDYVoE5WaGvSCAXNMtxiI7Rg2Y64pHGBaz2G_EQ5yohnHFDqLYxgGnV4T3JI4rQqi194rnvwP8TkVv6ahhtP5Kx5o7gobOVxs5CjVx6o-3k_fkgTU5cnswSWbUwmGLQMYH5_4exp3O9zsbSaLrOX9gtZWhuR3fNItF7g9E5sngfNPSKAxw6TjaHnV5eh_vFDiqVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش پهپادهای سپاه پاسداران انقلاب اسلامی در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690850" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690849">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1dd8dd6f.mp4?token=dKnmLTqcLn-IuVrBb9F44O9j07Je3guvO5Cgc-pOT1UUkR7iX9hJS4HEMkoyLmrHsrIV8EDEo2ZTpICxcqmKu7xXpzRVkP8zLmyQw3u6daiRZSoFgVjqlCOSdFmRuXrhKDstA5I3WT5k_NRMzfB3u5AzgCUegCb_vNSvZ9F2mmViHtrRkN-KnwpVGrTsjG2yKl-4rene7wdoeReLRYKMkA8ujtiFH4-un9cQo4tv3Gt0lEAcn25QxIbW3-QtgwLnmJlFcidsLQp2Kr6RrnjYXljR2sZpLw7hd-LQWNFkNF9Rb4Z7DCoYu1GSXELEIMrWskRnH5A48dGj5rvacYDIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1dd8dd6f.mp4?token=dKnmLTqcLn-IuVrBb9F44O9j07Je3guvO5Cgc-pOT1UUkR7iX9hJS4HEMkoyLmrHsrIV8EDEo2ZTpICxcqmKu7xXpzRVkP8zLmyQw3u6daiRZSoFgVjqlCOSdFmRuXrhKDstA5I3WT5k_NRMzfB3u5AzgCUegCb_vNSvZ9F2mmViHtrRkN-KnwpVGrTsjG2yKl-4rene7wdoeReLRYKMkA8ujtiFH4-un9cQo4tv3Gt0lEAcn25QxIbW3-QtgwLnmJlFcidsLQp2Kr6RrnjYXljR2sZpLw7hd-LQWNFkNF9Rb4Z7DCoYu1GSXELEIMrWskRnH5A48dGj5rvacYDIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند سرزمین عجایب
؛
پنچری چرخ کامیون با یک اسکیت‌برد جبران شد!
🛹
🚛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690849" target="_blank">📅 15:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690848">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmA563LoXfLc6tddlNWDFqt_MSaIBu1L4zTVLr5aL9j-ODiLd0si6eUPW5tDq7S6MiLxol7tYim3LQFb2X-_NL_yb_T_Bo9qGGXO96xGmqD_8LFXhXXUNk5gtFnyvbi0eNaxxD-987p1dOuu18mUds5ShdXGx8J8UYFWjvJ86wgC8gusL6OkrpBI-LsrusbWdRoI9GZRgLiSJ0PZLaBoTL_GafbeD3AwiWzosLZuD487Sq1ShSF63jI0MiaQ1a9ySb9TD2iR8JT5N9B5iad6YEbe_9Zob0QSjgo1PZEmyB9HAIQjMd8waYaUgP_zhNSzCtRmXNbkSuzjWTo7-zEoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زخم‌کاری چین به آمریکا در میانۀ جنگ با ایران
فایننشال‌تایمز:
🔹
چین دارایی‌هایش در اوراق قرضه آمریکا را به پایین‌ترین سطح از سال ۲۰۰۸ رساند.
🔹
پکن با کاهش ذخایر دلاری خود به‌دنبال کاهش ریسک‌های ژئوپلیتیکی و تحریم‌های احتمالی است؛ اقدامی که می‌تواند فشار اقتصادی بر واشنگتن را افزایش دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/690848" target="_blank">📅 14:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690847">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMtKzpF4VbJU4mGf-yVXDOMjLSf8sohrKDzcWLMKxyz2i9upuJMn8b_p0_Cm2TT_CcyqEjvweoOE_fzC173IxYkZw7AQ9AQrYRWVWzJO58V23zigdZja_TemAesmjw7EimRzA4S9dcaHdnc-1z7R4DY8QWNCGZevDiaWjFj8xv2BJTv-Ub3gvKaV5TPH2AvTxRMLz4d2iZ3XXx7uPmT4L1ZRTnYOXDoDmAkU-4f02yoekrpXYz18fV4I57ckpexPYmvMA6vxRufG9tKQVK2oaNBIkxJ9690MA5FzQksK8exBzFAd9jiFXhtvpCpcIJf2FUuztfgGNOD-YTfwe_21-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از رهبر انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای در جریان عیادت سال گذشته فرزندان رهبر شهید انقلاب اسلامی از جانبازان پیجری حزب‌الله لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/690847" target="_blank">📅 14:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690843">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d34c6fa0.mp4?token=qvQROGwFKUxPMlk-meJdtR5F6JhjslmRB76ZysbEpYypQqfflyV05OEbMEh1wjegj1j1bLaWuImSRPP45Smpud51eO3a0pLNbZTjv9aYS9oiMOpPksetC0tw1lS5k0PRrAYHWt4Cew_-kAgPlpJGXjep8rlFa_JtqO48aBWU4x8cw-nt8NpetKfS6oa4ztvWuWc_h5wndDpmemps05ihDOxvLAPyx1MnhMpmmakxLDBfrC4V7UQggUBAkU2wd8JwsBrNhHSTza1RcKBrjmI_ITvu6jxvuoXjZBIbcLlZ9xEwtmEBkKcpVK7yswy8AFft6yKz_mn7ldA1kIZGNrJbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d34c6fa0.mp4?token=qvQROGwFKUxPMlk-meJdtR5F6JhjslmRB76ZysbEpYypQqfflyV05OEbMEh1wjegj1j1bLaWuImSRPP45Smpud51eO3a0pLNbZTjv9aYS9oiMOpPksetC0tw1lS5k0PRrAYHWt4Cew_-kAgPlpJGXjep8rlFa_JtqO48aBWU4x8cw-nt8NpetKfS6oa4ztvWuWc_h5wndDpmemps05ihDOxvLAPyx1MnhMpmmakxLDBfrC4V7UQggUBAkU2wd8JwsBrNhHSTza1RcKBrjmI_ITvu6jxvuoXjZBIbcLlZ9xEwtmEBkKcpVK7yswy8AFft6yKz_mn7ldA1kIZGNrJbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور ویژه زنان و دختران جانفدای ایران در رزمایش مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/690843" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690842">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246c8f53f5.mp4?token=nfghIHuluZwsaOcWr5F7nfuS9RMVTJUGec9fz3zVHX0xSVlqLJnW8pOheN4qfZ3P5n9BF3rSbrXduiWg1ALU3aNuQCY0nA8KWMdUVfk44iAoQzsHUka0upbIMVL8rEhEsujzM7mniTGEyVZAYHvXwr4z_T0dsiiSFT7DEm23eziXrT-fXEY1IzaICmjSEgCllMHvkhDgepELN0LeQLajiEFE_xFaXruH8vyAFiK0aq6lIoH3UD-UfeePzfBEskMHabSsYue_UJOdB9Or-k3nxP6RRBkAHwUMYqgE1aqKz82GRLv9dpQK66U5V7N7viCVfRaGvqlLizjF5w9j_gKwvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246c8f53f5.mp4?token=nfghIHuluZwsaOcWr5F7nfuS9RMVTJUGec9fz3zVHX0xSVlqLJnW8pOheN4qfZ3P5n9BF3rSbrXduiWg1ALU3aNuQCY0nA8KWMdUVfk44iAoQzsHUka0upbIMVL8rEhEsujzM7mniTGEyVZAYHvXwr4z_T0dsiiSFT7DEm23eziXrT-fXEY1IzaICmjSEgCllMHvkhDgepELN0LeQLajiEFE_xFaXruH8vyAFiK0aq6lIoH3UD-UfeePzfBEskMHabSsYue_UJOdB9Or-k3nxP6RRBkAHwUMYqgE1aqKz82GRLv9dpQK66U5V7N7viCVfRaGvqlLizjF5w9j_gKwvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نماینده کنگره آمریکا: عربستان از ترامپ خواسته جنگ علیه ایران را طولانی‌تر کند!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/690842" target="_blank">📅 14:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690841">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
انجمن خودروی آمریکا: میانگین قیمت هر گالن گازوئیل در آمریکا به رکورد جدیدی دست یافت و به ۶.۳۹ دلار رسید
🔹
قیمت هر گالن در ایالت کالیفرنیا برای نخستین بار در تاریخ، به ۹ دلار رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/690841" target="_blank">📅 14:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690840">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6781ae07.mp4?token=lRAVP8Mj8o8xwWfBs_qXd8YmYLdqsWEP_Ja_la3tlVQCkolHn5wz72cfUOT7Jdu-MJY-eInzSyUiraiBlQuUD7b_wJ7n7t100US4W9V08b1cSib5TCCahSUvCfjoiNmBme6LhmYbwhU1TO5Aa8FbrV0VhxS1krhRFgRmLzXMBgSp9zhMHi9NyIDpGoHUkWkwDDHLoUeXFnJMQQPnJ0KqhaSlBLtlc2_nwfueqX0UbDzwtHRKoMyZTMncnd3FmQbTiJb5w2P5wo8d-rjW3DNkymVkO78W0yAKcuBQQwdjLJ_dkt2nKelH2QYXjwI6YP0ZdI-TwBxYaZEn7jZgglU4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6781ae07.mp4?token=lRAVP8Mj8o8xwWfBs_qXd8YmYLdqsWEP_Ja_la3tlVQCkolHn5wz72cfUOT7Jdu-MJY-eInzSyUiraiBlQuUD7b_wJ7n7t100US4W9V08b1cSib5TCCahSUvCfjoiNmBme6LhmYbwhU1TO5Aa8FbrV0VhxS1krhRFgRmLzXMBgSp9zhMHi9NyIDpGoHUkWkwDDHLoUeXFnJMQQPnJ0KqhaSlBLtlc2_nwfueqX0UbDzwtHRKoMyZTMncnd3FmQbTiJb5w2P5wo8d-rjW3DNkymVkO78W0yAKcuBQQwdjLJ_dkt2nKelH2QYXjwI6YP0ZdI-TwBxYaZEn7jZgglU4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیمار فلج توانست با تراشه مغزی نورالینک پس از مدت‌ها صحبت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690840" target="_blank">📅 14:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690839">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3335bbf6c.mp4?token=EcvVsMu_o3nDm-j7DyduZoIgRl9GY4TuiIGTH2IkUwf2J2G5lWOe7mdqlA8Uz2kaML703KUhgFgQ5bgbVDXnDAKAd0hc9nBHGLuGMKKMGyZVO-gUA5Mh8IkgZ735_zdU_AtrfO1lkUzGeWZ5iTt-UZpxyefOnB1PaS808cdx8IKTKm70BuvX9zwWS_dOVeEbtBIkM3fe52nZWZzWxG9mj72kh7GfPfEvL-_eAKzSroHe11mcVjgI5D5qnMmkoghZKBEa5mxupRvC3W0CfipiP4IgEWIr7IuBGs3OK5pkn_RXM3iY35HM9d3CEBBP3sDBcaAsorqx7l5wxrzqd0f1Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3335bbf6c.mp4?token=EcvVsMu_o3nDm-j7DyduZoIgRl9GY4TuiIGTH2IkUwf2J2G5lWOe7mdqlA8Uz2kaML703KUhgFgQ5bgbVDXnDAKAd0hc9nBHGLuGMKKMGyZVO-gUA5Mh8IkgZ735_zdU_AtrfO1lkUzGeWZ5iTt-UZpxyefOnB1PaS808cdx8IKTKm70BuvX9zwWS_dOVeEbtBIkM3fe52nZWZzWxG9mj72kh7GfPfEvL-_eAKzSroHe11mcVjgI5D5qnMmkoghZKBEa5mxupRvC3W0CfipiP4IgEWIr7IuBGs3OK5pkn_RXM3iY35HM9d3CEBBP3sDBcaAsorqx7l5wxrzqd0f1Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور اقوام و اقشار مختلف مردم در رژه با شکوه جانفدای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690839" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690838">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690838" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690837">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2pnl5G47jxJOtCz0rDAbLMGLPcnqObu8svdh0_cmK2SzSXd1_hUsj3IGBYeQdn7pvqoslCaTFOm9Zcg6NCMhMu0n1V_OPCkKCFu5XdClfFbSrrFPWa6xtM9IXF4hYKA4ws_JzPTfgfWD8YZmQUe2VEsmkrme7i_dO0SIa1eyM8TkJwEY2ybCC5KOLg1IkUfVGBJzKHWYgzY2ma6rQO5y3ZI75rM1k8PZsdy74rPtTygBulsW58YxICGem4SzO5AIiRUfq9JZXHLObQzW8oAh6RV37qavnT2Sdu_xuAfpYwZNhBu8YbkO9UAhK5QNRpDoXjnW_ODBLepcnIe7hKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ریسک تنگه هرمز بر نرخ تورم آمریکا اثرگذار است   قالیباف با اشاره به تصمیم فدرال رزرو:
🔹
افزایش یا کاهش نرخ بهره به‌تنهایی نمی‌تواند تورم آمریکا را مهار کند؛ زیرا انتظارات تورمی تحت تأثیر بسته بودن گلوگاه‌های انرژی، به‌ویژه تنگه هرمز و باب‌المندب،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/690837" target="_blank">📅 13:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690836">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان یک روز پس از ادعای عربستان درباره حمله پهپادی به مکه: زمان اجرای پیمان دفاعی اسلام‌آباد با عربستان سعودی و ترکیه فرا رسیده است/ ما وظیفه خود را انجام خواهیم داد/ پاکستان کاملاً آماده است تا به تعهدات خود عمل کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/690836" target="_blank">📅 13:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690832">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyFZiOgAXBIXZughgAt3_LjMDhtLK099LL1WMPOx9nUXb-o2MyV4uUQN2gzvg9nkL5FW9fdzm509VPiFzKmVMcQHZaWzGiuZpc0fBBk8VZVGRCnCgNnbjYrOYEN9oVALGhwKj_ippXqAQSN3tUq8sYCFPH96NvOqDq7YAFDsF76YsuCQM8wNSTJy1yq6W7JKDLYH9A47ZgbJ_iNNJ37nByQB9nAI9AOaU-EKzncIlEW-o78fcG0wDMDHe4hFRP7v1AZaFjTgdQ-owj74YW_5WDjzFHfTZDRXw5RUu0Jsmsm-6khXxOUE6Q2PSD9GZvncJm3zvfYXUkhhnHZg3bEzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6VAmPJgeE__DqjeHAZ0jTEOnCFrf4EVWWCYB2FCV4Kgeb-1NnxTT7t5aTDq23zcG2DI4hFynhCHVUOP7fmS89xRsMcv-hCVG4y8VdiM9Qfde1UGOGj1uia7AI0iXApcITBw8ERN5JCWO7LhrJp-a2QF1uAut5xnHg3c_ccT96il1Cp4QUTlgJM3W9Qr_AcRfGd1wQIwwMPALC8Qq5FUAkd4T9bGkaKAmCjKd1EH782u762HE8BeW4iOdS6ytebVTEIKc8619O2hY1ltQIYxXLUfRWTEbV-wRF8DEirUmNMDZFsJ9gSdZhwN9XTbeeM6pqluaQYP0Wbb027SHKsW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiHrjlA2DjxSCb3fUSyWCI-YV3i66mtVmOlL_vXcGqATu04nHTH_q36pCjB4CKaYdkrNiUc5XqfUdhLRQGtI27S_v46HHKLoQmAvPD7tYWgHY14fgtsvpwf11oyuL3JrY7xtRjvlOfXqc2biSrlkx_ynslxPWaTDosl2dnVFqdA8DvPo0XxlxcYV_nsOFtHWLfuySOy4mfhhWugq1sBaBPEcIIUPnBKvahrw1ML100O3MSJ9N4pSKgzYflK6K9gBb0mkHM0NM-KQ_2XLHQ0U0Lsn7YHHNXZn2OLZFDG4hqReM30hBkioWiGyxxSpiXnuZJLF41v5OJBva-1XleY9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1cuNKUoCDw3yyi5qXT_ArM1Kx0sZonvv8j41KrTer0j07q140vbhrRXXwRt4pVnBNvxkUiRXC8vwCzeEZ1iXHzmzoRA777Z7iwVtkyDaH5EHMZZhIfxjhbRNs0udDHZ18q17ddYCXUavaci7YSvgZ3cz8gdwQkwjVggeXs_UT-PhSmIiaFpWVoH6OMLeOL8NWDWq8ZXMkTQoiQT5xL8yibvx_xIvAsPz9eX9OPTtyaPZAEW5y8uCxvgPDQrW1dlkcpV3ocPZAbZ5yNk_V2rZ6jN9WqVYMul8ahFc56G9kMHd2egkuNpDenSmyE8T5-ZK-9q2fTDEDu_9naAPNcvvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور جامعه بسیج ورزشکاران و جوانان ورزشکار در رزمایش مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/690832" target="_blank">📅 13:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6cb7a77d.mp4?token=Otl04xR4r3x5sMgBolj99kGkijuXYFqVnEblO5AFUYNryiQOsSc-RVyFxqEYTYMKmELl8ts6YRKt-6Ko48pqbwQUveorZbRdt1DX3OtjmawVRpOH6PPhjBgJzs1mIWCVR8-LmyGGPz2keghV6kq3VIiTrTAMuZ0Y8CZCDBafUsdQeLgz_NfS0gwl5pOVjRTi68Av69nedVL0JCba-tcICWQZzFiF1riKcv4TG6XHdvzFY6xXg_cDB-Ri0TX0PtK5ItyZN8DFHFJDO9WCt8-XbEmpcneRyZEp8cVDxQVKD66kn09qPknvxrP9LoTTItQMPbC1obwGFg6XNewOvb9mUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6cb7a77d.mp4?token=Otl04xR4r3x5sMgBolj99kGkijuXYFqVnEblO5AFUYNryiQOsSc-RVyFxqEYTYMKmELl8ts6YRKt-6Ko48pqbwQUveorZbRdt1DX3OtjmawVRpOH6PPhjBgJzs1mIWCVR8-LmyGGPz2keghV6kq3VIiTrTAMuZ0Y8CZCDBafUsdQeLgz_NfS0gwl5pOVjRTi68Av69nedVL0JCba-tcICWQZzFiF1riKcv4TG6XHdvzFY6xXg_cDB-Ri0TX0PtK5ItyZN8DFHFJDO9WCt8-XbEmpcneRyZEp8cVDxQVKD66kn09qPknvxrP9LoTTItQMPbC1obwGFg6XNewOvb9mUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری عجیب از ایستادن بتمن بر فراز نماد شهر سیدنی استرالیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/690831" target="_blank">📅 13:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI4mNHmZesYWveScLMMIhjBHsMpUJuhXxbWpiQIGdjpkbkCnAiOY8lWjepUJSpkaS_K0SfqWs0Y6MfNy1SAKqTosawTqpkIlRTouQfiuHnsO548EDoexhqWQZuc5TuXpHYfLGt7la0FQ_uYD0_Oah11UhUwbQKob8LSxd8fcgiIzW-dv2QxqTI_MGBGHEG-5DMv-ciJW_BTFb3zRO1tdlczQ87ilv0HW2v6QjCztYZRhWZ5qfdTwYkkR4emgPYVHAN64ha8-T_cUbDfhFDJdcXDpQu6VdIZyyeeW8KvqTFQ8mr5qDOtPk496LXZghUEkat1PVss8_DC67x9iMRIBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر سومین شهید درگیری با تروریست‌ها در سراوان
🔹
مسلم فاضلی سومین شهید درگیری امروز برای پاکسازی خانۀ تیمی یک گروهک تروریستی در سراوان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/690830" target="_blank">📅 13:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690829">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اولین تماس ماهواره‌ای استارلینک با یک گوشی معمولی برقرار شد
🔹
فناوری Direct to Cell استارلینک در کوه‌های ایتالیا، بدون نیاز به تجهیزات ویژه، با یک گوشی هوشمند معمولی تماس ماهواره‌ای برقرار کرد.
🔹
این فناوری امکان ارتباط و استفاده از پیام‌رسان‌هایی مانند واتساپ را در مناطق فاقد پوشش زمینی فراهم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/690829" target="_blank">📅 13:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690828">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
فایننشال تایمز: ونزوئلا ۴ میلیارد دلار ذخایر طلای خود را به آمریکا منتقل می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690828" target="_blank">📅 13:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690827">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc351cd5a.mp4?token=Kd_rrhoii8QkELzAukBC85KySMG46iyyK_01IV9sTE2oJiHeds_9Hz4jenTrJDhF99NIBqxkCJPFIO_X3pRDQnxOkqMlLUE8VKXAE60kHJ3047r3DfThF0sc1pRF1dtqU_w5vrPWyYyH36UHDsebpRPN-zVvIpDUdVJoYxPAPh0PSw_S-0QBOnRe-7nk2h2KQiKTZt10YhawiqwZeCkGMPpMrt3BFsSKmUiQffu-9eetI49WLhko3ENFB5HpR2tK55fWxvj__E9z4x8AdBAzLqF-MFfZ5C_SVnsWZzjPKZro-rLUiIH5PjaPgIq0kLzoFbJupRpHf32VwnxJe-MzUpYgVvT8PLjPe2lA1W-RSuHaddc-n6ocjp_veZm1ZFJMswECWHN1DrDBkOWjvFPXlypeN2eFY94Xg8tS_Th6jGy5zyJJ9KiGHGY2w2GIMrDZSxbg9i1g4V3cwmJS0XOBDNpjhDJjc1Yy5WJcYIRZ5Z83DZDlu4DmrxaM6YqpOkCcj-_FjkChc3KeBBOMdyg3TM5YXJGvOzGsYgB8Pz6auCnkxMGGoWwjfdlMjyagt7osstJ8gNJudilmCg068kZ9B_Irlo7QTsDmzKJcQAepCVxImlO1eiJCJNXxy0o6oZi8_ovuA_cSRNGddHoRduYqaBPhJNHx3Q4hnew9gr4cOM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc351cd5a.mp4?token=Kd_rrhoii8QkELzAukBC85KySMG46iyyK_01IV9sTE2oJiHeds_9Hz4jenTrJDhF99NIBqxkCJPFIO_X3pRDQnxOkqMlLUE8VKXAE60kHJ3047r3DfThF0sc1pRF1dtqU_w5vrPWyYyH36UHDsebpRPN-zVvIpDUdVJoYxPAPh0PSw_S-0QBOnRe-7nk2h2KQiKTZt10YhawiqwZeCkGMPpMrt3BFsSKmUiQffu-9eetI49WLhko3ENFB5HpR2tK55fWxvj__E9z4x8AdBAzLqF-MFfZ5C_SVnsWZzjPKZro-rLUiIH5PjaPgIq0kLzoFbJupRpHf32VwnxJe-MzUpYgVvT8PLjPe2lA1W-RSuHaddc-n6ocjp_veZm1ZFJMswECWHN1DrDBkOWjvFPXlypeN2eFY94Xg8tS_Th6jGy5zyJJ9KiGHGY2w2GIMrDZSxbg9i1g4V3cwmJS0XOBDNpjhDJjc1Yy5WJcYIRZ5Z83DZDlu4DmrxaM6YqpOkCcj-_FjkChc3KeBBOMdyg3TM5YXJGvOzGsYgB8Pz6auCnkxMGGoWwjfdlMjyagt7osstJ8gNJudilmCg068kZ9B_Irlo7QTsDmzKJcQAepCVxImlO1eiJCJNXxy0o6oZi8_ovuA_cSRNGddHoRduYqaBPhJNHx3Q4hnew9gr4cOM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باب‌المندب؛ چرا یمن به یکی از مهم‌ترین میدان‌های رقابت منطقه‌ای تبدیل شده است؟
دکتر خالد بیدون، تحلیلگر مشهور عرب و استاد حقوق دانشگاه ایالتی آریزونا در
#گفتگو
با خبرفوری:
🔹
یمن به دلیل موقعیت جغرافیایی و اهمیت مسیرهای تجاری، به نقطه‌ای کلیدی در معادلات منطقه تبدیل شده است.
🔹
منافع متفاوت عربستان، امارات، ایران و آمریکا باعث شده جبهه یمن به یکی از محورهای مهم تنش‌های منطقه‌ای تبدیل شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/690827" target="_blank">📅 13:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6DMeHsFmCtsLznxE48u0GZzpjbYAAhBtIUuaR9vUXQo4WHRE6FSCjKs_-gfbPnLhQQPeW8C97un0rfglnVFL2NTEGFQyNUcOqrJmE5Ez9tHd007Xo68OTOGkeJS9Z7ixMbuRc0p8rEy5I2s9CIJbW42WdyqVGlOyocfp25FiW3y9TeFf74eHSOgN9A8g6w2YQiDcmVFt-myFdhRyhAB2q4fb732rnpOqNgX-R4dCM0i47R0MyQ_ZhuHmQMFpV67A40PLzSfhDolXhEiXMVq29QkKetDiDwjn_M4nc4gPsbcRYplKnN3t3K-DFK7RTKfdFUhn4bEnCju7mgdGpPSBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmux-8MwFQHplNydF2Apze_F9XoLbiXjE-dlogT6R2XXTCEdo8kCJv-qjJ_6Z9IftX80bfzvJZ1OdoqVGq3iCrjEr9eWusVQF8TACM9pW3cDMIHyJ48VvFyMQ_RM1JhVb4NRffUJ78sMVO7k0CiPnL6HNV3dV69a1Hp-0aeo7QwbTnxxSQJfisXHTLMbcN6AeV26pznMN7S-A-m8oefCAdMZG_YmvsF39eqMOycAFLDBl4Tm2Sr2BQXIsQrNR4ZzinqICdiIf76KiKCOrDFe10QqGIwXDej0zCzXc3yAhPImbJPgD7B0hKFbODhl0mRS5NFIiJ6tabFu7NpUzaZVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adQAchj5oi-s9pfHORQDt0gVFHyW7pOUy_IgyYSspefqgxmgFo_kzXFvEeGXveS7yHDO4Dua3YChmarcyV1YgOw-KwaBO2rcgNb3CP3ghZhssodfaELjK2gw3melGfxYB40H0Hp02bRIGWl06_5FdvlZmwNqp9XjrwyKXm0_hMmZOLa2Lo2pfAILr3pMFoScTomdHzg-nrV8Ir8X1V9qRUVSG8kE-geoRnM4pVrh9584j8-AiIJbpcJSVHQnH70xKt65K-45M1TWvlNm66lWvfYuBSAxtgrURlJSkDfKTOChSfjirH8ER7BYldG6hCpea041wRHe7Bn0zalj_D5jyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/divlhqYQyfgXGrcDXlX71b5JSGd0Z-gfqdeQnOXMvJVOOxLvKW9d9LsNYUfjbfj0YJOISPUN2XGS6fPFIhnNwlE_3_4xHayBLIR_ZBxx5TbbJZwHcHWTLdhhC-508gjiF29bOAHYXcsq5PvHi-l9pdGkG7v7vjlKwmmo3DoyqfBSwJz95FFy0feefjQc5tQzuovoZjy14v7Z_MnaWmuspt1AHBL4AGI5shynwqbnMqa--USPq9NNeGQ510Hu9iiEgxFSKsKkVhLI5aHdfhFQJdAKU9S0YBmt1JG861Tg1bbqPv-5pWET0uMrWX3TH61ICzqsi8Qp1KC3lcvfrCZIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlc5iQq12U14EVmkQD8V74xI35oOLciLeoJfRZWtVvIoYjYPqMrqc8fl6U6741vEW-fZfEg9xfCTeA2eCVja8CWBTpGA3BmK0m4kjH3dzJHVTLbxi1fo3JoAQR0j-1gnTsjYDZo8UXyXPL-jcVbQKpC61qqYpSgmBhcbuhcM1Uj_UqtD5oRUIaTz2yM7etSUA__hmA63--O7Zr6uc_dnhDlFNQqdrWctbVppLJHUInIl3WhM1xgN_3rUBxAdlCUNSYf7e0w3F6qqA0U3u7Xmg-fScJQfLWfsQN-Nvae5M74P6nddv4heTSbImaMUGkVqisAMk0D1cCnJMFk3J4tltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMyj2OoubZjYdakVt4tYqHQdXRcA0kX-gfXXJRypfxNQweDRIq_GWgL3QsAD2XJTEPY1rsSHZOLqzTV1y9KlHvwgbCEJCQ4nUQf7xr3I_805HBt-ySo5pQCQAR3FEgM5dWnyga_a9cpMUXhpgl7YP4PFmSJfnpdRsmSPrFt0PY7KdiQBITvVpEaS-x5xwCNAlbLqT-nUHgYJWzoHHlx-M2SEwzlXx9NBkgg1hgB1zu5KELXcsZHFITghMiXIETyBIgGeVWPPQMN2KMrJiisLlyQYOdjVaYqMUZxLpiaRpSiEuZ8OF9QImtfb81UvQzFxHXlFGST1jLh0UmwdByrq5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر متفاوت از آغازین ساعات حضور مردم در رژه ۳۱۳ هزارنفری جانفدا در خیابان‌های تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/690821" target="_blank">📅 13:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154ac35b65.mp4?token=O0ZhjHk1dsrdgggibdoosckXM5ZamYZs9HrdhpRflOFaKwi-LlAIo6bXDZbJFYSWxN6WxeMNKR7AXkwdQBZrb4dJdhMwgu1lqz-MSBurq3Sjty1mDR8BvjsXuW0D7PxVCd0wf7r53e5C6vxkPvvxBBW333AEVyp-KAmACVPJQpNkpsFAhVZwfQscSGqyAZb2W5aj0p1C3lSKIfn8JRjJ9l-bmwB4V1f1vqcs4eN4Y_QXHW_l90s5Vmpl6CMqJxqj1FJbFs2u37risN0iBQO2ZPbEZhW9wm_P8-bGQI-O-sJO3FNOACKCHyXl4W9kNLs3YIUSvbKOzSjT3ImiaQAtcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154ac35b65.mp4?token=O0ZhjHk1dsrdgggibdoosckXM5ZamYZs9HrdhpRflOFaKwi-LlAIo6bXDZbJFYSWxN6WxeMNKR7AXkwdQBZrb4dJdhMwgu1lqz-MSBurq3Sjty1mDR8BvjsXuW0D7PxVCd0wf7r53e5C6vxkPvvxBBW333AEVyp-KAmACVPJQpNkpsFAhVZwfQscSGqyAZb2W5aj0p1C3lSKIfn8JRjJ9l-bmwB4V1f1vqcs4eN4Y_QXHW_l90s5Vmpl6CMqJxqj1FJbFs2u37risN0iBQO2ZPbEZhW9wm_P8-bGQI-O-sJO3FNOACKCHyXl4W9kNLs3YIUSvbKOzSjT3ImiaQAtcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه
آیفون ۱۸ پرو مکس و آیفون دوئو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690820" target="_blank">📅 13:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXhuesOX1qjpoUYFmYvhEhXONjltObqa1BD26e-1Ouonat4ONqekm0Kqgc9reNvojP2LIoWfsHapn1-swiK4ezdr07OYBX6c33nqNLLpJRU4WI-ZcL_Di8li-bqOZAfpXvTPubdtAlUhzlBj8XrY042eGU-GuVJEVsKvuku-xpBVEcG9lAqO5j8fR2Qfs-JW9_e4Xal4abWXDN5P92mnsyDaiLNXlzodm97GqzNYh3gi8QCsWn-wxqTlQfXl1YLNbVKLZCaGG9ZuVIn-eGm-Gu0ydSH9mfxwCVey_pz0r2WBHb0LwRu5qylzSBL-8r4z6kCAwX2DZnBJs7rFYhBBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش غریب‌آبادی در پی خروج امریکا از شورای حقوق بشر:  آمریکا نمی‌تواند با خروج از شورای حقوق بشر از زیر بار مسئولیت خود شانه خالی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/690819" target="_blank">📅 12:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933d29d4c7.mp4?token=MYpdK8pacWV3SwOwe0RSqWPCQoUgvbKQm-zbPG_rlzQe4pHkd2qF7aLfF93jkLL3FcilMOu17kVdtldE_VZN6FeRLqJE9MhSc-1QKyLsWszrGJbePrg-Ewc5tTY6rDsKBG_yfBwMslk7eBZXDdnnOMvut592SF15l-3JwLTKWUPykIxTEL1YWNk4Oon5tcMalQ6_sxlBFfi5HPqXHXvj_g3RsUUewQrKo0fWK52KNLbOogUSA59OL2pd_6jYtViCMnvL6H9MrYZfaM4l_qgKAq69sFDdc_1giYvvXc0QofWcIYSSqlQ3ukpjj9GlrZSjjrgD7H3EfRlQgQ9Lw52pwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933d29d4c7.mp4?token=MYpdK8pacWV3SwOwe0RSqWPCQoUgvbKQm-zbPG_rlzQe4pHkd2qF7aLfF93jkLL3FcilMOu17kVdtldE_VZN6FeRLqJE9MhSc-1QKyLsWszrGJbePrg-Ewc5tTY6rDsKBG_yfBwMslk7eBZXDdnnOMvut592SF15l-3JwLTKWUPykIxTEL1YWNk4Oon5tcMalQ6_sxlBFfi5HPqXHXvj_g3RsUUewQrKo0fWK52KNLbOogUSA59OL2pd_6jYtViCMnvL6H9MrYZfaM4l_qgKAq69sFDdc_1giYvvXc0QofWcIYSSqlQ3ukpjj9GlrZSjjrgD7H3EfRlQgQ9Lw52pwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع
انفجار مرگبار در یک مسجد در پاکستان
وزارت کشور پاکستان:
🔹
در انفجاری در مسجدی در مقر پلیس در کوهات، ایالت خیبر پختونخوا، ۱۷ نفر کشته و ده‌ها نفر زخمی شدند./ الجزیره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/690817" target="_blank">📅 12:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832a1e0b98.mp4?token=dZauj5Ue6bVkBN5Q47I94at-6N1zgP-yBSsoWDPZE0CKPwUx4OZNQ2NbtvkWXprHYnsSXyT6KR9Gpz2jswbB7eyGuwhjaqddsV28fX_5WfiNFA86ojkYIGKl8fzSnovwUHRWpOfQCXkP9W0OJPunnyOsmNb2Yrf8sqwmu84eypVyyEGm3gJe8keYuo_e2z9BpZUFOfHa7AkMhMYX46GCqEtRRgOL_U8FSBx9KrItAok7cYsv2BoUARniEYNzg_2J-O6p2iZp0F2d4DV5Ug9B616EXfvD9eRXQXHKWMgT6gysgn--MtEJaLIQCpLx34v8pKRDbOupVKbdwM3BsGBJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832a1e0b98.mp4?token=dZauj5Ue6bVkBN5Q47I94at-6N1zgP-yBSsoWDPZE0CKPwUx4OZNQ2NbtvkWXprHYnsSXyT6KR9Gpz2jswbB7eyGuwhjaqddsV28fX_5WfiNFA86ojkYIGKl8fzSnovwUHRWpOfQCXkP9W0OJPunnyOsmNb2Yrf8sqwmu84eypVyyEGm3gJe8keYuo_e2z9BpZUFOfHa7AkMhMYX46GCqEtRRgOL_U8FSBx9KrItAok7cYsv2BoUARniEYNzg_2J-O6p2iZp0F2d4DV5Ug9B616EXfvD9eRXQXHKWMgT6gysgn--MtEJaLIQCpLx34v8pKRDbOupVKbdwM3BsGBJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا متحدان آمریکا در خلیج فارس به دنبال گزینه‌های جدید هستند؟/ آیا چین در حال پر کردن خلأ قدرت آمریکا است؟
دکتر خالد بیدون، تحلیلگر مشهور عرب و استاد حقوق دانشگاه ایالتی آریزونا در
#گفتگو
با خبرفوری:
🔹
کاهش نفوذ آمریکا در خاورمیانه پیش از نقش‌آفرینی چین آغاز شده و کشورهای منطقه در حال بازنگری در میزان اتکای خود به حمایت امنیتی واشنگتن هستند.
🔹
جنگ اخیر می‌تواند روند افزایش نفوذ چین را سرعت ببخشد، اما تغییر معادلات منطقه‌ای تنها به حضور پکن محدود نمی‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/690816" target="_blank">📅 12:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
بیانیه مشترک ۱۵ کشور درباره ممنوعیت حمله به تأسیسات هسته‌ای
🔹
بلاروس، برزیل، چین، ایران، روسیه و ۱۰ کشور دیگر در نشست عمومی آژانس تأکید کردند حمله یا تهدید به حمله به تأسیسات هسته‌ای تحت پادمان، نقض منشور سازمان ملل، حقوق بین‌الملل و اساسنامه آژانس است.
🔹
این کشورها با یادآوری قطعنامه ۴۸۷ شورای امنیت، حمله نظامی به تأسیسات هسته‌ای را محکوم کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/690815" target="_blank">📅 12:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بسکتبال بازی‌های آسیایی ناگویا/ آسمان‌خراش‌ها با اشتباهات فراوان از راه‌یابی به فینال بازماندند
🔹
ایران ۵۱ - ۷۷ کره‌جنوبی
🇮🇷
۸ | ۱۶ | ۱۳ | ۱۴
🇰🇷
۱۲ | ۲۴ | ۲۵ | ۱۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690814" target="_blank">📅 12:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
هفته پایانی
جشنواره پایان فصل چرم مَـنطِـ
‼️
𝟲𝟬% و %𝟳𝟬 تخفیف «تمامی محصولات»
⚡️
➕
تخفیف 𝟮 میلیون تومانی اسنپ‌پی
خرید حضوری و آنلاین
با کد: PAYCWGZ5
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690813" target="_blank">📅 12:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f98bdd053.mp4?token=vXTW3TX1O75r-SeEbQbTXc2yoBELlMXqwLTI4_73OqUoT_CFQVHzme3WRqdyD0Aeej-pGvZ0-1nGRmeTfWV_nV4-UbVH_SWWijxvl5us0HX5jJ_zrLu8uWyEALMZS-cjC5yeFXPkqQTRXlj7YZjVzLdZZ3_VHHbp7J3iTH6HXHee8zU-FRiJYOVmYti0yjF8oEuSfWohFgOWtPJLAs70Ye-1V39y2QgKUeQj_1YhUxnkCIm_86kZp-DChI-Ot45NpQ6I3icMyDNz5nA_LyXfPd-1iR7UmCd2VdWcIMPL5e3TkZ-IXLKoc4-9lcV0sFW_g5s6g3zG1cEMQw4Kt7jl7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f98bdd053.mp4?token=vXTW3TX1O75r-SeEbQbTXc2yoBELlMXqwLTI4_73OqUoT_CFQVHzme3WRqdyD0Aeej-pGvZ0-1nGRmeTfWV_nV4-UbVH_SWWijxvl5us0HX5jJ_zrLu8uWyEALMZS-cjC5yeFXPkqQTRXlj7YZjVzLdZZ3_VHHbp7J3iTH6HXHee8zU-FRiJYOVmYti0yjF8oEuSfWohFgOWtPJLAs70Ye-1V39y2QgKUeQj_1YhUxnkCIm_86kZp-DChI-Ot45NpQ6I3icMyDNz5nA_LyXfPd-1iR7UmCd2VdWcIMPL5e3TkZ-IXLKoc4-9lcV0sFW_g5s6g3zG1cEMQw4Kt7jl7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروش جالب خودرو در نمایندگی شیائومی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690812" target="_blank">📅 12:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وزارت امور خارجه آمریکا: مجوز فروش جنگنده‌ اف-۳۵ به عربستان سعودی صادر شد!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690811" target="_blank">📅 12:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eULh-8FrwwhplOAJCAII9D3gKURZZylVXlryM8AMZZ3EG3rdLU7crfiyiLOTpY7AW5W48lALXwyPF-UqO--zP8jOw19hE_9jP-Dz1b6Hbe6nDlMkr01daxJGch75VGIC2MHf2asvZjrbir4RWA6HmolRlkCXrW2rin0Y1hhtJkIFBdCHNeTh76pYz6nUQ5BqUy4zW8svt9_FsegRJhkfvVtPNRbCVq9Iq-D3LeBNjpAxjVYgAwEbeNik2X4gtqplZ8RbfrW47NpxKud8YJaP5qdr2l7eoTAtWnzoJ3zeI7ttzWnRCN1vsB1kMxzEy8PP8jr36F-pzdlywuYbnsZjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار امریکایی: در شمال تگزاس دیزل تمام شده
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/690810" target="_blank">📅 12:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e003e68b95.mp4?token=EboieM2IfK1PB1WFkeKoXr2da26k9Mo6pViG370AuKwbqJp97qeQ6PtnRlMfmSmzPftt8OFn759OAlILLgMPhCxtvsIoUKNbYS85LfsNhRr9FloR7_qA_1yx-5YkHIs3bRef1-oZEKwOsyIffE8lmT5Lg8-tRQGzaCIJsKAsA2tDG2xX7fzBxkcr8mZo0PFbOHbqNHoU6p6rBM_ydw0K0oHuRnExr0Oabs6c4B1X11_ngHRogn0hBFKj9qXNdLM6YABVvG1XhNwBj7XyAHcCBqKCmiSe4AoJzbVpaTMEp6IgK5jEwxkYz7gKhK1wwGGMWz4E2uWwl4C-agJau_130w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e003e68b95.mp4?token=EboieM2IfK1PB1WFkeKoXr2da26k9Mo6pViG370AuKwbqJp97qeQ6PtnRlMfmSmzPftt8OFn759OAlILLgMPhCxtvsIoUKNbYS85LfsNhRr9FloR7_qA_1yx-5YkHIs3bRef1-oZEKwOsyIffE8lmT5Lg8-tRQGzaCIJsKAsA2tDG2xX7fzBxkcr8mZo0PFbOHbqNHoU6p6rBM_ydw0K0oHuRnExr0Oabs6c4B1X11_ngHRogn0hBFKj9qXNdLM6YABVvG1XhNwBj7XyAHcCBqKCmiSe4AoJzbVpaTMEp6IgK5jEwxkYz7gKhK1wwGGMWz4E2uWwl4C-agJau_130w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اضطراب چه زمانی می‌تونه مشکل‌ساز بشه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/690809" target="_blank">📅 12:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اصابت پرتابه به یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس امروز به نقل از مقامات محلی گزارش داد که یک نفتکش در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690808" target="_blank">📅 11:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
فدراسیون جهانی بدنسازی و پرورش اندام شب گذشته در تصمیمی عجیب فدراسیون بدنسازی ایران را تا اطلاع ثانوی تعلیق کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690807" target="_blank">📅 11:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
درمان سرطان از مهرماه رایگان می‌شود
معاون درمان وزارت بهداشت:
🔹
برنامه جامع سرطان کشور از مهرماه آغاز خواهد شد و همه کارهای مربوط به درمان سرطان از جمله بیمه، پزشک، بیمار و خیران در سامانه ثبت می شوند و شناسنامه‌دار خواهند شد. بر اساس این برنامه تمام بیماران سرطانی خدمات رایگان دریافت می‌کنند/ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/690806" target="_blank">📅 11:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2tLsDscanv_GJbzauboOCS2LsNaJygijPleZt_wHVnWdsDcaWAxyp5ZG8IwUBTB8wznQGZmw9ddTCOPJXaK9ObcjSkXF8FbxeQHfaQ0JKY7QR8dtDiLp5ZzKrrOyoeLOKutZ9idLjZneA6RHKa_BAGxB66lKZNDLSN3hpZrVTHRIxqh_lq5FmS2koovgGWba4PRE1beu4vtVEFuP187udWiglRtO2xPitVZ5GZOvWPhDJpsBAoshIhsVC5LU3v-i4EdHE94HzoBLVlclX51aysjSIGwPOJn1kXs9-USNCXKnOdgqOn3TX2bWkJrvDZ576-HxF-7rTSnVnFZyxrPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ جنایتکار افشاگران جنگ علیه ایران را  «سگ‌های کثیف» خطاب کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/690805" target="_blank">📅 11:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1AaKX_EZPd3i9jQz-PwEfRMp4_BwX4e-gT7vv8_qx4Pk66dZKWS4Gb0hjfvAAMdOmWfU6S0d5DwWTPc2uFZO4KRrZkrw7s55WHcZr63XMktVxIlwqzvGXjJG0339jdOvsbLFquhpMFOWFGVKHPsBzfmQGFO8hdf-MU6Wawng19-F0Wtw9Quhd2MoPog1VPEI0_6AMZPt4zPcW2v8y3l9cS9FGj-6LCr9lHSuAiCoXzTTsggt9a8d0jw1Jw-XIEYyYfuNX8ZnIgq1ooiJN-Ggjfq-a4MR6PL9TpWSzBAo8Rc_GtqpOaWPfe97zPDBAHU1NXg3pF_YpQefq9LQCvAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ غذای دانشجویی سال تحصیلی جدید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/690804" target="_blank">📅 11:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aca0e19c9.mp4?token=pntRbqVPufbCZpUyTyZJM2trTTqzl3w4kdUhtG-NSuLVmSyPsWmn9aOLvPodK_oL2o7P1i_l1fV8-Wc9d0_bJc163obYEKnj4aPLZz9cn5RLmgWtz5JlvKTM0QWC7X1Le2DOF1aDirmXXmk24VMPu7JIRO7RotAVQ4IiU1-_IEpHenc6vPfTgHiat4PgMfqDm8u-PP6oZKpBpwJWFRHxUc36jtTZ5ZlK0HsniIP7tEnNJLFOusCs1Tib35txWG6jd7Wa-94va-sLnqW1LlLe5pui0fq3sG6KuJbiWiMynyUR-UEion3SDMClrnb6KYn48RsVSvcWsiq578W2fVthrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aca0e19c9.mp4?token=pntRbqVPufbCZpUyTyZJM2trTTqzl3w4kdUhtG-NSuLVmSyPsWmn9aOLvPodK_oL2o7P1i_l1fV8-Wc9d0_bJc163obYEKnj4aPLZz9cn5RLmgWtz5JlvKTM0QWC7X1Le2DOF1aDirmXXmk24VMPu7JIRO7RotAVQ4IiU1-_IEpHenc6vPfTgHiat4PgMfqDm8u-PP6oZKpBpwJWFRHxUc36jtTZ5ZlK0HsniIP7tEnNJLFOusCs1Tib35txWG6jd7Wa-94va-sLnqW1LlLe5pui0fq3sG6KuJbiWiMynyUR-UEion3SDMClrnb6KYn48RsVSvcWsiq578W2fVthrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر هر روز غر بزنید، چه اتفاقی برای مغزتون می‌افتد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/690803" target="_blank">📅 11:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUbibm1tb0vHJk0tojYEG8TNGovaIonlN-X0A30-sAS4Lvy1Gkt08FzQshHpmDxsAR1xyzo-Hl86pIcQkj_5NJWQlV2va6Uron3i1T2uy_nzJ9rJFOG1wN4t5pB2fMrAucv-L4yptXM3GqTvKdL_TheKFPG5O39n69vdcvAw--5osE9bn7RLH6fzzdyQHTdl_y5qe5RMd_wGvW4WcegWiBa5qqHSj7EY1B4bldYj140kv4CpWvT_xOYP148euHWlFE3KApUa7-1vCK0Z7e13NqtKv5MFUilZgDqXlDZBnHdr-DRpTbr_iq7NmRna1rWGyR3vxI9VmEUaXmOLbq6iWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پرتابه به یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس امروز به نقل از مقامات محلی گزارش داد که یک نفتکش در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/690801" target="_blank">📅 10:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZiUggXmgl3_PYq_NmT7yKpToVdhlrigFSkbtb_KZwxiTYNVmO2rjH9DmC7CHzYGgGelTbFv-i9hHcAIf8iVKCRlx-88bjR_k5j7-YlrDgaZFuCRHIEF_zfwLPlCTuj6BlOuYl3eEMkgmTuIKxJIlKB1FiJPg6t_L8tMsB7Ya_cq5Cuyopr3d-J2Coi4EBVZ3I5QE7YIv33MZOD1dqvqx1M0fzdQO6jDsJHiV1VnmU0yUnPEQ_yGWZuB-JMfcZn7QSkrBB12bfazZR1EVrU_m18pD7zI-4_BAROXYJppDMVSZ3HzWZKRJHgntCrVWyYjLv3ue7MjaFtaaeEBWDTI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ریسک تنگه هرمز بر نرخ تورم آمریکا اثرگذار است   قالیباف با اشاره به تصمیم فدرال رزرو:
🔹
افزایش یا کاهش نرخ بهره به‌تنهایی نمی‌تواند تورم آمریکا را مهار کند؛ زیرا انتظارات تورمی تحت تأثیر بسته بودن گلوگاه‌های انرژی، به‌ویژه تنگه هرمز و باب‌المندب،…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/690800" target="_blank">📅 10:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرفوری
pinned «
♦️
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد
🔹
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
🔹
این تصمیم آمریکا یک…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/690799" target="_blank">📅 10:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ایتالیا ناو جنگی به باب‌المندب اعزام می‌کند
🔹
وزیر دفاع ایتالیا اعلام کرد رم برای تأمین امنیت عبور کشتی‌های تجاری خود، بدون انتظار برای تصمیم اتحادیه اروپا، ناو جنگی به باب‌المندب اعزام خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/690798" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwwj7BPtNaoI-OPffBhqJ7H6qv8EEhdUPl1EQJjsp2mKTaU3awUY13oGS9OBBCss6RqV4bGLPmdO6N0KWVnPRiewzU2AOm-O_2MnjUyTIxc55R7CJBqPZN9CuerULWDad-kVnPGWt31YEJIuH_RHXOtSJt4tdE9rXdgZyUl73v1OyzNTy-kq1Lcto9g4Hf-MqaTTsM6KEKfdZBGxIc8-EsbciqDc5XDYB3HoSflKrbQJvZnHH4AVM2z9vUT9-MICuVwmnvGVJ_R-JkvlPx1_bt6kNdIhsGmhLWbmNjIvInwDZVSNsWDF4_E_BA66wMN9GHc4bKsmrI8l56N4JDBVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت ۲ تروریست مسلح گروهک جیش‌ ظلم در زاهدان
🔹
بامداد امروز در جریان درگیری مسلحانه بین سرنشینان خودروی سواری و نیرو‌های سپاه، دو نفر از تروریست‌ها کشته شدند و یک نفر نیز دستگیر شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/690797" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مقام سازمان ملل: جنگ آمریکا و ایران در ماه اول، ۱۵۰ میلیارد دلار به اقتصادهای عربی خسارت زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/690796" target="_blank">📅 10:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwM0RDIelN1eqY9A4dgSPxgSpsn1mywHmpzZ0cuGQa1KUgvMzZMb4jsw4GnguHJLuNOObHhXQWyZR-ohj_FFjKCSc2RXrQLeYHMnBiLxBj8FtmwXjkyrRLyDtHTadtopaeBgOWzLiOJeVRYxI4Wq92R5acB6f551vwe38i4WPtl_Dw6xgc2noE0k6YxnZLPnh7COALKkNv1gNXnQF9WgQEuGq4LgyQl9GMGg-VZZns9pqDhZQ1P_6hWnZJitxYhu_BEAyQYY2O9kfhGAd8kofSuqiRJpeL2cuqpNP0HkOuu7sxFahlKrk0fwDrIYFVQbTuHBlaDN5S8iASRoKDP0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیمانه‌ها چند گرم‌اند؟
راهنمای سریع تبدیل پیمانه به گرم
📊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/690795" target="_blank">📅 10:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5sZMnRTmKb-OxssuhfLPUQtpG4UiJDxhShntfL_EwGACyqKIb4IKIuMvGTKgmRvUOe-eZh64aAyH1YXaPR_qy9i7KWg04YI0LKBzovXrmZRnrsbgcsnZTu074tiOOjDyZRU_foyR2SPF3_Bi0BjHSLQPgOHk8TqioxFJ09VLJR5FmAgh7tcNUxHn8XLH9XU1yCGgBDtyL7TLr2F8vP2nFA3mti9Gu39n_nMjidSWsVWHpZPGBbBRciXTTx4bbowq0YyKKXWblZ-2_3gXRhLTc6WyVp9Lp6iL5H8TQqttodI8HEqRi2Ggu6oFtYua1PEoQdkxcb5iN3GpKMs4gsTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی صنعت برق استان تهران خبر داد:
تحقق ظرفیت ۴۰۰ مگاواتی انرژی خورشیدی و ثبت رکورد مدیریت هوشمند شبکه در پایتخت
✅
کامبیز ناظریان، سخنگوی صنعت برق در استان تهران، در نشست مدیران دستگاه‌های اجرایی استان، با تبیین موفقیت‌های این شرکت در مدیریت هوشمند مصرف و تاب‌آوری شبکه، از استمرار روند نزولی مصرف برای دومین سال پیاپی و دستیابی به ظرفیت ۴۰۰ مگاواتی تولید انرژی خورشیدی خبر داد.
🌐
مشروح خبر
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/690794" target="_blank">📅 10:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690793">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حمایت ۳۰ میلیارد ریالی بنیاد ملی نخبگان از طرح‌های حل مسائل استان‌ها
🔹
در راستای تأکید رهبر انقلاب بر نقش‌آفرینی نخبگان جوان در پیشرفت و جهش کشور، بنیاد ملی نخبگان طرح «شتاب اولویت‌محور استانی» را اجرا می‌کند.
🔹
بر اساس این طرح، تا سقف ۳ میلیارد تومان از هر طرح نخبگانی برای حل یک مسئله اساسی و اولویت‌دار استان برای حل مشکلات دستگاه های های اجرایی از طریق راه حلهای هوشمند حمایت می‌شود.
🔹
در این طرح، نخبگان، سرآمدان، اعضای هیئت‌علمی و متخصصان با همکاری استانداری و دستگاه‌های اجرایی، از مرحله شناسایی مسئله تا ارائه راهکار و کمک به اجرای آن درگیر خواهند بود.
🔹
طرح‌ها بر اساس اهمیت مسئله، کیفیت راهکار، بهره‌گیری از ظرفیت نخبگان و قابلیت اجرا ارزیابی می‌شوند.
🔹
مهلت ارسال طرح‌های پیشنهادی استان‌ها به بنیاد ملی نخبگان تا پایان آذرماه اعلام شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690793" target="_blank">📅 10:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690792">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد
🔹
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
🔹
این تصمیم آمریکا یک روز پس از انتشار گزارش هیأت حقیقت‌یاب مستقل سازمان ملل درباره ایران اعلام شد؛ هیأتی که گفت «دلایل معقولی» وجود دارد که نیروهای آمریکایی مسئول دو حمله در ایران، از جمله حمله به مدرسه شجره طیبه در میناب و یک مجموعه ورزشی در لامرد، بوده‌اند و این حملات می‌تواند مصداق جنایت جنگی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/690792" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اتحادیه اروپا برای اوکراین ۳.۳ میلیارد یورو موشک و پهپاد خریداری می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/690790" target="_blank">📅 09:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b2b8f30f.mp4?token=qgkbmWfYPVjNPIXBKLfnYykcFdsga8DlAZyzNW59U4pDDeEtMYy2PWP6OLOCEb_jTmhRLcyvunjTZGNQjARcx6YGJaCoz8VfEzikEpWx0OOZMQ70cLWeB3HCBKSdJjD6AKcImbUyj0nvYTjYi5JX12mQQvMn3ZoKnqWYlws218V1PQlTWvxF1u0532L7c7LX6uQJmrpl-FjC_r2sWYXBALF-vFmEeZLKYgjdiJ4JlJ207PAkl58UASVKdaWWy6ZFBa0BGKlv1rDyjRnwPglpfmWC59frRXGBrmaNz4DaLW_fuV-S2KkwR8usMR4Mox2AngNFp4uOXEdA0-j-HP21g7D2mCWaq84c6KibUWN5qw_IkhSf6HYZRHQi-UyaPbTcHP1Fzp64wXhS1nD3UkX27xGgkIsgD-UNePhsH4Hc4V9MecplX348-1_ugi8ZICvurxKK3T1t_B39bqb9GoLDSuETL4PDG0VOCyHsfFPP7bFIWLpf6w8Ud41QF7C-eQy66ODwk5qUmXds-_wf6WN_C0MqZ2HvRNye90iFzdwZZqCt_FQBIPn2GaI6KZuP7_7cCca0Bm6HHfewTsExJPpF3lvz9jpV9i1yGAFZNLD2qxj1QJA34crcS46vbDQr93tQhEElv_n4hioP79-jmHFgWmAfn7CzyO_Dv9j7k-gZTE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b2b8f30f.mp4?token=qgkbmWfYPVjNPIXBKLfnYykcFdsga8DlAZyzNW59U4pDDeEtMYy2PWP6OLOCEb_jTmhRLcyvunjTZGNQjARcx6YGJaCoz8VfEzikEpWx0OOZMQ70cLWeB3HCBKSdJjD6AKcImbUyj0nvYTjYi5JX12mQQvMn3ZoKnqWYlws218V1PQlTWvxF1u0532L7c7LX6uQJmrpl-FjC_r2sWYXBALF-vFmEeZLKYgjdiJ4JlJ207PAkl58UASVKdaWWy6ZFBa0BGKlv1rDyjRnwPglpfmWC59frRXGBrmaNz4DaLW_fuV-S2KkwR8usMR4Mox2AngNFp4uOXEdA0-j-HP21g7D2mCWaq84c6KibUWN5qw_IkhSf6HYZRHQi-UyaPbTcHP1Fzp64wXhS1nD3UkX27xGgkIsgD-UNePhsH4Hc4V9MecplX348-1_ugi8ZICvurxKK3T1t_B39bqb9GoLDSuETL4PDG0VOCyHsfFPP7bFIWLpf6w8Ud41QF7C-eQy66ODwk5qUmXds-_wf6WN_C0MqZ2HvRNye90iFzdwZZqCt_FQBIPn2GaI6KZuP7_7cCca0Bm6HHfewTsExJPpF3lvz9jpV9i1yGAFZNLD2qxj1QJA34crcS46vbDQr93tQhEElv_n4hioP79-jmHFgWmAfn7CzyO_Dv9j7k-gZTE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برش حرفه‌ای آناناس در بازار میوه مالزی؛ مهارتی که تماشایی است
🍍
✨
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/690789" target="_blank">📅 09:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
نشریه لو پاریزین: میانگین قیمت گازوییل در فرانسه به بالاترین حد تاریخی خود رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/690788" target="_blank">📅 09:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اعتراف شبکه سی‌بی‌اس نیوز: ایران در روزهای اخیر دو فروند پهپاد آمریکایی MQ-۱ را سرنگون کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/690787" target="_blank">📅 09:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOzGbqG6oZ7zBV0U6Q_bUGdHGaLdphqkcH-L9OwWNqbeeiqjQgets5B2rtzuR5mAORabfPahFh5ExmTxpqhb6Ao2xys2wLcUBg65igrJGxhWkNo_SbLph4mFnBmDZWnl-lJpZ6DhR0Fd5Wx3tbR5Nb4L-zdU3d9G9DoW1eSBIcgvWNpfSXmsJ5P1JpMQ7c3DnTuPF3Qn8-yeU5PekFamv4zltfAs4hZlNnA1cfCqlwHcKV5KJnj07l8nsa8gjTHazvvyLg3axSmFjp_PBZwsYEvyOFey0VxUpzNDTLsjrThNCNe0PKcNhyJmUi_Cycn6ixneCVknEW3xrv3y_ZDB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم دلار آمریکا از ذخایر ارزی جهان به پایین‌ترین سطح خود در قرن جاری رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/690786" target="_blank">📅 09:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVJ7ChLe_16fvvq9I2K269l5nzvOt_VNg-3W6AxP2DWusJcl26pl2FTg3yicbGy4Twu9DcjmA9ozQAdaCz9RgqpNik72TULQ1Ox_j5-5PWXFjlas1NGBGd-o4FkxePEbbS9Cnw6Ql_uS_ldsLiD7JH-FO_X-3e4NtK4s2ZvRG9BHIiH8r2uawgQh0HKn00DyFRLeaV5YvTUP8HeXmDEEYnrvZUU0EQJs1AFxia62nSLpPcUJzSgSTT4j6N1vZfE3o7cDaiaIw22sDqOUuty4sCEEJ4LXvb99D4KjJgdD6jTiGdZiivMHfgFzx2lbyT7AFNep_eAoDe9Cc5H5tudslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*وام های فوری، کدام یک بانک به صرفه تر است؟*
#پاسخ_سوال
در کانال
https://t.me/daaarmaaa
کانال تخصصی و تحلیلی دارما، دستیار شما برای محاسبات اقتصادی
https://t.me/daaarmaaa</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/690785" target="_blank">📅 09:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آناتولی: تردد دریایی در تنگه باب‌المندب متوقف شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/690784" target="_blank">📅 08:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd4256c44.mp4?token=rwaKGcp-0IikVoKPHOs7LJYaRuGDMiGZ0Ps8YDGClPPAeCtYPmxVghLErKz1BzCIh_fyjPSxE45y-zY6J285ME0ymDbbH4VYwV1R411W5Z7bR0aEeYPLAgojdDhUSpS-shOKhzy5IWIpdGS7sSXLfCHv_sdfP9Nu1XZ5gYsQt7IKa3Ac74lrS3PHm1WFgSatg0iwzROIFS-DCWsLvgp7xWWDqOptTZcrCH8pzk5l98UgviOUYa_Z-aVKERght4vIzi7LSX6dCbWEeqszYmmU_twRH2Om8fk-Bvx53yUlfELrmso84RLbvukzTRlq7Pzkv7iP_qtM-43FCRxZ1bOBzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd4256c44.mp4?token=rwaKGcp-0IikVoKPHOs7LJYaRuGDMiGZ0Ps8YDGClPPAeCtYPmxVghLErKz1BzCIh_fyjPSxE45y-zY6J285ME0ymDbbH4VYwV1R411W5Z7bR0aEeYPLAgojdDhUSpS-shOKhzy5IWIpdGS7sSXLfCHv_sdfP9Nu1XZ5gYsQt7IKa3Ac74lrS3PHm1WFgSatg0iwzROIFS-DCWsLvgp7xWWDqOptTZcrCH8pzk5l98UgviOUYa_Z-aVKERght4vIzi7LSX6dCbWEeqszYmmU_twRH2Om8fk-Bvx53yUlfELrmso84RLbvukzTRlq7Pzkv7iP_qtM-43FCRxZ1bOBzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوتمیل صبحانه مقوی و سریع؛ در کمتر از ۱۰ دقیقه آماده میشه
😋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/690783" target="_blank">📅 08:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690780">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_yoWfGUuZYLaJYs6L8DrFAXRjrbu9oOlc-ly2zqmnhLsaPYiNwravRbGNCj2G3HuVXjuK_EVGf1-rXb_BGGkaY2RW7s2cfQk6fXnNg-8x6h2g68LxzWiZbFEqalfYhlhWBxlYjsIere3wyN6zNAqIfXNJIrjWXyn-SQVw3Gre9qDLImYLlj6UVJLEPzg2uQfs6T3osgptJcmAV9LuP_aStAAp9uslabW-Hf2c8TeU4NcIG_pK0n6dWfuwgdCGBOjGmhgg8O7bAQ8ABWx628qmIRv1nf6LN5pfKo8vVuAYbx3483EEc-X5yzXqWzVV9Ownn2Qn_7xyJzcie3wteeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llBXIyn3SLA02J4g8NUoPDJcufM6q8h2BACh_vJ8CrnuOXzv0WzkzP2aEiDZcNbTrF2R_qv8rimd0nKKVZune_g0TQwMsSvTpExGS5P-1No1weIyYBNQGB0rim5XIRawozCqj4d5Aa7oW2ZDUklmuNmdSg7uang4c7ylJSTzmYA8qQ1znevC-5FMmGjOZVd43k3j1Bdik68bvvDpTOOuGUNSrwuSgwvcEBeP2a1bMkUzLzaaM5rCoLXnDe4BNgFhIvKKWpixCkC7RM4vaUrAXnZYp_u6nh7Pne0m3fzeUskOHjH4k9LvTSZoqfJ_PrjwZ3GhrrZIJk75rnQ8E85w-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjjSaFN3wWEINPDnF6UwDJX6lCNWsMkaxkhdfFqw9cJzSri-ei82JcB9_d5e8XL-fSUalBGr04Re6RKcxwS9SAQdxwEtOLqYf8JN7iuXENIQV36gNjs1BCMFFrE-EeU-NA_KWXOxSA0lBDywk-Xcbd6PBayjJw2peegppM6hTerz8KGOG2zgRNpngYFNR-_avLX1rPo86Cwr0ln7ZYV791IvScb7TAgT_HVGGnTZ88NF3ldNhvKmtxnG9JFIqegXLhOe99N8sHjZI0grwKBwiVLJegpdQCTi7torA7wOkFpjB0_TAyT__cUS0R5bWz-NmdqZGUbaEFs_ysBhyHstlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بامزه‌ترین عکس‌های بچه شیرها
🦁
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/690780" target="_blank">📅 08:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690779">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromطَـریقُ السُّـلُوکْ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbn3_UVNa7Lk-0P3CxCxydgqbP6750k_uXvCZ65T3MkmMRiuxaD635KQUHPuBTyS8vytnE-DtByPRFqR7wzSQq5XG_1bEYhBOxdd-SiqvXqm0ufyXPPGQddSwRdzUIykDw9K3G56Kih9Q7GzL5pDQVZCWnmr27-TZTIYpCLp6pvE11PYiYSzyBj7Fj2k0cQG8tAhIpNI5QsC4wT7oUdp0-ijmbG_Xo-Z14jf2mM_rW1Bpx3PuHgTkXGwgDMaIqYSsaCW6nGACeJ-BZ1F3MtjRmkuRsYPfBQyH4ijlAewMtMhbAAsgyxGWjB2WPYsQ0XZOmSajHZeIBW0mq3qw1Sk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شرطی که شهید آیت‌الله خامنه‌ای برای دیدار با شهریار گذاشتند
🔻
محسن عسکری، از شعرا و مداحان نامی آذربایجان: در سفری که شهید آیت‌الله خامنه‌ای زمان ریاست‌جمهوری‌شان به تبریز داشتند، شب شعری برای شعرا و مداحان ترتیب دادند.
🔸️
آقا شرط کرده بودند حتماً استاد شهریار هم باشد و ورود من به جلسه قبل از شهریار باشد.
🔹
آن‌شب، دقایقی بعد از تشریف‌فرمایی حضرت آقا، ورود استاد شهریار را اعلام کردند. زمانی که حضرت آقا متوجه شدند استاد شهریار به جلسه آمده‌اند با نهایت بزرگواری بلند شدند و به سمت در رفتند و از شهریار استقبال کردند.
🍃
آن موقع متوجه شدیم که چرا حضرت آقا چنین شرطی کرده بودند؛ اینکه شهریار به پای ایشان بلند نشود، بلکه ایشان به استقبال شهریار برود.
🔸️
عین جمله‌ای هم که در اولین برخورد، بعد از سلام و روبوسی با استاد داشتند، این بود که فرمودند از آرزوهای زندگی‌ام زیارت حضرتعالی بود که امشب الحمدلله موفق شدم.
🔹
بعد با نهایت احترام، استاد شهریار را بغل دست خودشان نشاندند و شعرخوانی آغاز شد.
🗓
۲۷ شهریور، روز شعر و ادب فارسی، روز بزرگداشت استاد شهریار
#رهبر_شهید
#تقویم_مناسبتی
#شعر
🔺
کانال طَریقُ السُّلُوک
@solook110</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/690779" target="_blank">📅 08:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690778">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPA8s3LrYrXGMLEk0MSJ4TN3CMu6Wo3CARfRAOCDW39A86MwNgA5qUdImTlSFjBzkE2ZX9dgn1UbrsCxdPc3rX03gHnTboaKK9-BcWb_bd8VgMRCErB02JiEKLX0nPCviw0qkfFEtmIDei2pn-wM2l5l9WMlQpQQCSh09mE8w2veDWubjIegdeIul7zJgr4AXEI6wA_vQze4DElk0VS_6qGmH17XcerB6BRf2yYtw_eJJmQaMZ7Kh4SJm8VFdYTjJaqGaAx4IbmgcZd9R13viIbYA3HQCz_pOD4dELUTH3FaJMxEi9Qnt28vlB_ocFYoaE1rmYjKiBDUgZmVMLY3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنیان‌گذار تیک‌تاک ثروتمندترین فرد آسیا شد
🔹
«بایت‌دنس» (ByteDance)، با پیشی گرفتن از «گوتام آدانی»، غول تجاری هندی، به ثروتمندترین فرد آسیا تبدیل شده است و ثروت خالص او اکنون به ۱۰۴.۸ میلیارد دلار می‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/690778" target="_blank">📅 08:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690777">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
نفتکش متخلف با پرچم کشور توگو مورد اصابت قرار گرفت
نیروی دریایی سپاه:
🔹
شب گذشته نفتکش متخلف ترند با پرچم کشور توگو، با تحریک و فریب ارتش کودک‌کش آمریکا قصد عبور غیرقانونی از تنگه هرمز را داشت که مورد اصابت قرار گرفت و پس از بروز حریق در آن متوقف شد. عبور غیرقانونی از تنگه هرمز جز نابودی شناور متخلف نتیجه‌ای نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/690777" target="_blank">📅 08:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690776">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رئیس‌جمهور کره جنوبی: هیچ‌گونه نیروی نظامی به خاورمیانه اعزام نخواهیم کرد که موجب کشیده شدن کشورمان به درگیری‌های مرتبط با جنگ علیه ایران شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/690776" target="_blank">📅 08:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690775">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
«شهریه» مدارس غیردولتی اعلام شد
رییس سازمان مدارس غیردولتی:
🔹
سقف شهریه در مدارس دوره ابتدایی به همراه فوق برنامه ۱۷۲ میلیون، متوسطه اول ۲۰۰ و این رقم در مقطع متوسطه دوم به همراه فوق برنامه ۲۲۰ میلیون تومان است که مدارس خاص هم مشمول این رقم شهریه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/690775" target="_blank">📅 08:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690772">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0DLAXvDAYMvmkCoKIsYiENdLO-PDYgbgrm2uuNy-WlUUMYLGJIeoatImVR6iZ-EBMzbbud0Rhvwbc252lnjFbWP_Qw3KipidxWj-fz4mMww4pGeD1jKXcf4s2ROQgtSzJgdCAGVYaQuSIZ3h9N98gYK-bc0LSq6BWpdPwkGQ2eXqw2Kp2NVlL_CLogKqCwU4kA6vg_4qZMqyrZ8qN8Y9qXYR25mzPVE4FN0CknICu_MDg_fA9eHLzg6GmMOQzTV1p1iG-ik9rv189ixJVivS1OVmQ0r5Gs0z2HGIEFtrxLSvCqKOTbcqRwJ9_mUEamcomoZn9L8PEducoDakZw76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD2qUVaWH3e9eez65ijOMMnmcFty78eNW5siRgBRKYSHSaOGMp1kuplUUXULrVC6W2ttfdDnGaFNc53dlHo0GErD3mu4jSFnd76u6-8hzvxNqLbWFEGxvM3D5PVf297JFvv_ZL3WVlPbYOQIU_PCbnYZD5sr9HiJ8MahlHvePc31RyYVaNXAH3KE8s0q-W7MNE-wulXPlm0m01cODEMpkVz0QQ6OGnN7vOFAMkRYw9No4XtL4JG3-dfQLQB00iy7TvGV1KAXJvOot_Ff4KQNpQR5R4d-4RXJ455JIGgrSxwsYQM6pGvBgyq_4q9iFj4iA9NI28c1sqINWRrC115cHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ywe_khIrCGC6Y5xtzvz0me8Dn-wAL9tfIi1TR0lH_n9pBSaoARBan_lXBORJt0cUttcfU5AsU5-XkoE-DxbHq_lzA9XHYVCy6Uo9NhWJcyM2lAuMDoLe_xNQIVOUt2W7gWWDrBRQtay9JGApyfed8dHSDwydIIHzbhnNTbitK-UVfywhL8gPzuRM4qXE0G8SZE57HGM0cEE-9I4V3NtkY2WUfsCAz7Gx5lb5yD3gKy9kf98KMzMfhW8YcLiiSbfG0dj7gE8wgBhlpQskMniAKOE8fWXrUkUy6oWruD2b2GEJxA_xFtvPV_eQiCSiVwBgyu39DoE-gZ623qA4EbtDmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتقال تجهیزات نظامی آمریکایی از عراق به اردن
🔹
کاربران عراقی تصاویری از کاروان نظامی ارتش آمریکا ثبت کرده‌اند که در حال حرکت به سمت اردن مشاهده شده است. این کاروان نظامی از کردستان عراق به راه افتاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/690772" target="_blank">📅 08:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690771">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvxSTwz8WGgmXGyxcsFzlUh_vilTtl2KttoEg7J-rSMLri2GupJDeLjNOAt4r5pB7kv4_YFK-UfHshSTrl4PKfl-fh-7ZQtD-li-Bg3b-nliQwIWogl_2DQgj5CJVSllm5Y3lS-_tsJikOxbGYwUIn3HH2Szzo05N2YiyQ_Lm-yIK5QLcEONuyIQnkDC69ZjP9fftjArPPeBkGn2TCu72ttY_uL1F241mfFLghPhcGL5kzkghGniIw67wWjZaMYuXu927dEOuKKGWMKwqPsFiG2sL_earDr2qzBTZKAmo6UgV_aQnOqByXlu5p1VAM8t8H7rAM3_wgWvpShjEtoXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۷ شهریور ماه
۶ ربیع‌الثانی ۱۴۴۸
۱۸ سپتامبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/690771" target="_blank">📅 08:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690770">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfaMM2mOE7mvEvBUpuUNsktmIhQeMjMqAiDtC9BJkSF4MKu9ftVUAfMppI_IUYilchOrSRuS8YV0mh1C8NVtwo1_OH2xRNbKjan1o46yLPIfxfeI-nwx7y49GsffiYyW9RNGDVoZI9naBjUgRSZB3dRNApdyXI5Bd5InFmuJrF-_52-kWHcwMy8EbahuiKrw-M1ty7Xu87SZDLKMnZ7mzpVLy5FkVvWr1oAQAyr2jLhPx-2xSHnjH2HEd26losqT-0HUH4EQmg7ikGN_pvjSdJVM7XHRVgvM8M5l_xXMHkjYfg-GUhi4NfpnDQRpMdA0Nw9MpqeXI2Nu4qIl4i9cCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه دنبال انگشتر  معمولی هستی، این کانال به کارت نمیاد!
اما اگه
کار خاص و فاخر
می‌خوای، حتماً یه سر بزن
👀
💍
انگشتر نقره دستساز
✨
حکاکی اساتید برتر ایران | عقیق‌های یمنی و غیر یمنی
📍
تهران | خرید حضوری و آنلاین
🔥
موجودی‌های خاص و کارهای جدید رو اول اینجا ببین!
👇
گالری حنان
https://t.me/+af-LaOPsPHZkMTM0</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/690770" target="_blank">📅 00:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690769">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUfRtq_EWRJ_weQk2MbC7FkM2-KrhJwYR0IENENwpKZh4CBU61VrGhwHt45nwZk8T2OSWFHweqzcUKBm6w_0O9Ah7QoSsVhM9k2u83Nmw419Sw9lH7y3Ue-pX8s8Wn8Zb_VBUNQR14aWAq_ZVFyNRpmQWCv4cQ8lNrNJ8HKDKwNZN0Cf1AyJ_CUvkZq3M_wZYeeunCPDAkCaOwbn8ebq3e07RPB4B0qosSsC8rc5huFJFAgEDJtcLkKpApVaFuq3GcsXgIHY2BBoTqGMC8jZqPjMowKMGtXrnWiBteu7K4jKSzJNZTfYxh0QDamM_xZC4D8vP3-bxIWeLDT8F5iH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پاوربانک بخر، ایرپاد هدیه بگیر!
🔋
پاوربانک ۲۳,۰۰۰ میلی‌آمپر Xiaomi M10
🔥
فقط
1,899 تومان
💳
پرداخت درب منزل
لینک خرید اینجاست
👇
https://memarket24.ir/product/brief/63565/180124/</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/690769" target="_blank">📅 00:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690768">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حملات شدید اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات هوایی و توپخانه‌ای ارتش اسرائیل به چند منطقه در جنوب لبنان از جمله السلوقی، القنطره، بنی‌حیان، طلوسه و النبطیه الفوقا خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/690768" target="_blank">📅 00:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGh86Q3XjF5FgiEUiFabQ7eAiYJqJBQpGIO5kpSHCB8HNO5vfe-m5Kp7dkyE4yWBAY79dt0anUvCZn3oKRSF0_9mTtdxZEgiZoCvio8wTi4Nh6OngJwLuB8jj5RRIMXuUU412iIF0BX9pSFvrIL0UkPTZD1gvyv5d0j5MDYLGacs1wbRor_LQgG_NitYW9aeExo-nzCnuV_9VvTdLbg6hI3OOS40WjB48m8SBzKZMdgRqkRMdmYuUBm3orbopZz8oAHIdP01RwyQ0gREohi0R_5zFi9NunDavvilyCx5qBoVT5cwnpC3JIeYlSbvxak407O6_mxRkMNRx_TNsIIwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ah4PAHEG1-6TegtcbCPorANCNOGnmHY9doh0usfDXXcceJooU8wJKuvjHsywqXvUPSmf-2-BvS7UW3J-RGwjoQJTs-r61ck0nJJPaxZJ6EIh_HOXmDAwlafZadzGstjkNopU9cG0gknn3vUCSQ8NU4injyHjhmy--8n0XkNhZg5q8Sq8TrX1BlnQpJ5bqErd5tvw00fCZ_VW8XnJ43RGlnruczGDkPDOOtmtnFcagC7b1OBnxGGf2dGIK6bAacbZTzuPPo9mLwRmoFDUKV1W974xZc-yR63kS3OTL4E_Rfku64X24Gd7qyoTRpgXBhykVIwQ-T9yOF_5RV4W05SzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeChvRjPbOq7H2AfyI-TbB_9obJNfO9wI_jqCwiaNdsWTUq8jg31uWx3jIXnHk56LqY1tfdyhdwWCY1eATfoP_ULlSNzldBOB3k9i6cFGpzaPJPHcJNErtvolLpafyHqzcRkEKFpwS10nORJ_ff4CNSYLljOJk7jdTkfNKrYMhTdB1H2rMOLkOWNKH_Udo2HyFpS5bMATFE8in7UecgZWvegqKou9piKVnjSXJORBApV6-FHvPRrRsJluiNlPeAAaHwUYgJZlnqqN7275iNXBcZorQPiD4cBHB1Ea-BxciukTdSypTqXDDnmsLzoIVdn-eMDkamw0MNBzaj8FXeJxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف گونه جدید گربه در بولیوی
🔹
دانشمندان در جنگل‌های یونگاس بولیوی گونه جدیدی از گربه‌سانان با نام Leopardus tilcayo کشف کردند؛ نخستین گونه گربه‌سان کشف‌شده در بیش از ۱۰۰ سال گذشته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/690765" target="_blank">📅 00:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690763">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e289db30a8.mp4?token=FnAmn8CES1tAZTCwRBTY8BIOvMSBkzHU1hDr6Qrg3BHbApqfoijin9aW2DnGELkFe-9FJRLZC2-3haKRZux0guwBH5-fb9MGgkHY1M4gNAFr15SmHVzsqQdIOPg3mSow5IYgTb84osTsI71tpf5L31cHSTdBW3N5y5bUJo2YueIUo76Cm2ZampQgTkAeQN9vlxfIr6jh3hk-UZfu4ggxP19eU7mnsqbqEybimDv_sKSVS4jSLiJ633DIdlL3Ho1oq2jmhtECet9CRs6bY92_uc0F-v3Ut3gqiuMl9HvqpzmVal-MotIV9EK3OWeRhmrIL0LWgMO_aTHmN2sa5028EWYx8hGpisYpJYSotRPnTQtaiIC49TZfUNOaPne2sslym31NqGHy9YDyt69RC6U26jeqrRIlljcq_nEP-F9pFMC4OVF7giR-heLdYtBWCubef7ogNx9ed8YLyg73Hki0ZFfIAYUU6G7qnmhP1oVp0kbNZ_t_5fDM1n68nJQrXN1T2YXQmm3YDVcbInp4lGZuMIG5NtEmJaYpjY5YMnjHzTgbUEUWlQu1gcBTQsjaYqVrCNiFsaF5lNQxHfNXYykDr9sNjYJAdKTnQnmuS3c7n25KzVQs7icHKVOhX3_IxSY6hCE1kU8xO0nUn_6hxBN6cgNuCj_eerR0jtOsOGzZ4mE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e289db30a8.mp4?token=FnAmn8CES1tAZTCwRBTY8BIOvMSBkzHU1hDr6Qrg3BHbApqfoijin9aW2DnGELkFe-9FJRLZC2-3haKRZux0guwBH5-fb9MGgkHY1M4gNAFr15SmHVzsqQdIOPg3mSow5IYgTb84osTsI71tpf5L31cHSTdBW3N5y5bUJo2YueIUo76Cm2ZampQgTkAeQN9vlxfIr6jh3hk-UZfu4ggxP19eU7mnsqbqEybimDv_sKSVS4jSLiJ633DIdlL3Ho1oq2jmhtECet9CRs6bY92_uc0F-v3Ut3gqiuMl9HvqpzmVal-MotIV9EK3OWeRhmrIL0LWgMO_aTHmN2sa5028EWYx8hGpisYpJYSotRPnTQtaiIC49TZfUNOaPne2sslym31NqGHy9YDyt69RC6U26jeqrRIlljcq_nEP-F9pFMC4OVF7giR-heLdYtBWCubef7ogNx9ed8YLyg73Hki0ZFfIAYUU6G7qnmhP1oVp0kbNZ_t_5fDM1n68nJQrXN1T2YXQmm3YDVcbInp4lGZuMIG5NtEmJaYpjY5YMnjHzTgbUEUWlQu1gcBTQsjaYqVrCNiFsaF5lNQxHfNXYykDr9sNjYJAdKTnQnmuS3c7n25KzVQs7icHKVOhX3_IxSY6hCE1kU8xO0nUn_6hxBN6cgNuCj_eerR0jtOsOGzZ4mE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه امروز با آن روبه‌رو هستیم، جنگ برای بقا است
احمد دستمالچیان، سفیر سابق ایران در لبنان و اردن در
#گفتگو
با خبرفوری:
🔹
ما در دوران ”دموکراسی نابالغ“ به سر می‌بریم و در این مرحله، نقش رسانه‌ها حیاتی است؛ رسانه‌ها باید بر ارتقای سطح آگاهی عمومی تمرکز کنند.
🔹
هرچه آگاهی مردم بیشتر شود، جامعه استوارتر و مطالبه‌گرتر خواهد بود و همین امر، مسئولان را به اصلاح مسیر و تصحیح عملکرد خود وادار می‌کند.
🔹
نباید فراموش کرد که آنچه امروز با آن روبه‌رو هستیم، یک”جنگ بقا“ است؛ نبرد موجودیتی میان جبهه حق و جبهه باطل که فراتر از مسائل گذرا است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/690763" target="_blank">📅 00:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRLvTNif0ymFgXnxcwMeIi5GZMKs41WkZRgEmRxeel3KaARIAwCMiH-dtxoSlZVEaOpyBeSeqMmpBFXK9xJTMopl3VZ1QYWgbRQnAo_OaAFndpF6zFcjWAqhMl6kGg4t8g7uh9YqVLeqG_39GGO3VO9Y3CgfmQk-XmHXt8GgsNq775R-ASQvxalvwxPE5FBN2IiKIl6XUHR6lhpSyOO1KYOblHVI0hu3IKNj0Q8urJsW5aNZ5Q83gQWQ4HeL6SvXbMYqsAdRyqherzdnUqMjCR1b3QLLmk99sFGEAKFP008IeRnk93NDvYWe7e4dQU8dtCBBKtg1Yt1juMet5AwDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/690762" target="_blank">📅 00:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای‌ترامپ: اگر‌ کانادا بخواهد به اروپا نزدیک شود و اروپا به او کمک کند، اروپا هم تحریم خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/690761" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690760">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترامپ در حال برنامه‌ریزی برای جنگ تازه‌ای علیه ایران است؟
👇
khabarfoori.com/fa/tiny/news-3245846
🔹
در سفر عراقچی به چین چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3245951
🔹
جزئیات کامل قتل‌عام خانوادگی در تهران + ویدئو
👇
khabarfoori.com/fa/tiny/news-3245893
🔹
ماجرای عکس‌های یواشکی از علی ضیا در فلورانس با زن ناشناس
👇
khabarfoori.com/fa/tiny/news-3245801
🔹
قتل یا خودکشی؟ | مرگ مشکوک زن جوان فیلم‌های منشوری
👇
khabarfoori.com/fa/tiny/news-3245705
🔹
صفحه ویژه خبرهای پربازدید خبرفوری را اینجا بخوانید و ببینید و نظر بدهید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/690760" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690759">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqLqLeW3KOCNCYvDP6dyhxMal3BXAXYVdJOsnMRrKcQIz_K87Yj-HwvkcI8XHpuaKW_Gevq8s2OTTxo4UCe2Y0o1jzes02fYpWbohWYSiQ54cMnF-v2UkXbgGwoN-jy83C0ph7oAtCD88yqRa94Bx8PJcAaeXqTElXHbpQ4b1EfWjZ6afmMkcR78FzNLurqfO3DopUwy099r9g7UUGd8xd0tRIWDJYL4-oO4YT6GA0968bJ-nCff284vhy-sLCT2-7CwHNP41KrCPAwMlRO9bEf-uulwdl-k1loraENxLd2CdVlOsc3QR3s1Zp3QEyzSDIr68xe_Wji1PErsRPfBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انجمن خودروی آمریکا: میانگین قیمت هر گالن گازوئیل در آمریکا به رکورد جدیدی دست یافت و به ۶.۳۹ دلار رسید
🔹
قیمت هر گالن در ایالت کالیفرنیا برای نخستین بار در تاریخ، به ۹ دلار رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/690759" target="_blank">📅 23:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8bf2c053.mp4?token=gowpPi0aiXyZys6EqbrAO9bnXREDMXqc0Fn41EOLYO6KEa48Ga7EBf7vcNT4XsHRfmuGCZVh31TlLeAvgAXZjSLfwxn7gihmFDklHC9FIk2JiNxRPi7ufErCLA6vDgnAMxkqSDu3ZTh9gZ-8HrBDec_wRy2txfD6wVB2HXJxUi6lxAXF-5SZZBvtAoTOurGuqgeIfIZn-sABLLqSm5fgJUaXSa0k6fnyz9QKK5jpRcHfVqOXZgvvyoNcngNOULjoa5vGVs2RlIDXDinvHheDxUX0EZnaDfoNuWejMZkZcdBryo-y0zJ0QNRWC2kI__IiPgvQU2jQkCIvVINaZF6KcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8bf2c053.mp4?token=gowpPi0aiXyZys6EqbrAO9bnXREDMXqc0Fn41EOLYO6KEa48Ga7EBf7vcNT4XsHRfmuGCZVh31TlLeAvgAXZjSLfwxn7gihmFDklHC9FIk2JiNxRPi7ufErCLA6vDgnAMxkqSDu3ZTh9gZ-8HrBDec_wRy2txfD6wVB2HXJxUi6lxAXF-5SZZBvtAoTOurGuqgeIfIZn-sABLLqSm5fgJUaXSa0k6fnyz9QKK5jpRcHfVqOXZgvvyoNcngNOULjoa5vGVs2RlIDXDinvHheDxUX0EZnaDfoNuWejMZkZcdBryo-y0zJ0QNRWC2kI__IiPgvQU2jQkCIvVINaZF6KcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای اندازه‌گیری مواد غذایی
🔹
این پست برای خانم‌هایی است که در تعیین مقدار مواد غذایی و اندازه مواد اولیه مشکل دارند و نمی‌دانند چه میزان استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/690758" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15736a757.mp4?token=QZkC7IXu1QZTaONIqfna-j4bCc0W_FUjI5dohsLVMbqSbOdGwnjXlRMSmmRWEtKinf4-o7-MaCGyFFiPEGQcsa5Tr2a71xo0kw-BBkWj1pMdj7ccLracosvfPYW_aZG_mehi2NKpXFzJ5ZxgdZq2xBr-qDncfOit9gHoHtd2dPcZ9pYkeuvG8LIsBln5ZldsDE6c_L4QBG7d-LJZjrtVi96f3xdzy5IRGoLvk13fatkfmh-yGsJ9cc1AfcpJBOQ8UxxXHOjOdVmpjN1LQcXygRHy1YdwetPpG-aJv1j8m_aAyLPnlDQVIRNzEpb5JMu1-BYa_JZvgvnRsjeybkNdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15736a757.mp4?token=QZkC7IXu1QZTaONIqfna-j4bCc0W_FUjI5dohsLVMbqSbOdGwnjXlRMSmmRWEtKinf4-o7-MaCGyFFiPEGQcsa5Tr2a71xo0kw-BBkWj1pMdj7ccLracosvfPYW_aZG_mehi2NKpXFzJ5ZxgdZq2xBr-qDncfOit9gHoHtd2dPcZ9pYkeuvG8LIsBln5ZldsDE6c_L4QBG7d-LJZjrtVi96f3xdzy5IRGoLvk13fatkfmh-yGsJ9cc1AfcpJBOQ8UxxXHOjOdVmpjN1LQcXygRHy1YdwetPpG-aJv1j8m_aAyLPnlDQVIRNzEpb5JMu1-BYa_JZvgvnRsjeybkNdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایین کشیدن پرچم حکومت جولانی در منطقه الحسکه در شمال شرق سوریه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/690757" target="_blank">📅 23:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690756">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سالیوان، مشاور امنیت ملی پیشین کاخ سفید:تقریباً نیمی از نیروی دریایی آمریکا و بخش عمده نیروهای ویژه ما درگیر تلاش برای باز کردن بخشی از تنگه هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/690756" target="_blank">📅 23:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
تکذیب خبر وقوع انفجار در اطراف جزیره خارگ
🔹
خبر منتشرشده مبنی بر وقوع انفجار در ساعت ۲۲:۴۰ در اطراف جزیره خارگ، تکذیب می‌شود.
🔹
براساس بررسی‌ها، گزارشی از وقوع انفجار در محدوده اطراف جزیره خارگ در زمان مذکور تأیید نشده است./ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/690755" target="_blank">📅 23:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">نام امیرالمؤمنین روزی ما را میرساند</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/690754" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690753">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پروفسور رابرت پیپ: من سال‌ها جنگ ایران را شبیه‌سازی کرده‌ام؛ ایران پایان این جنگ هژمون منطقه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/690753" target="_blank">📅 23:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mohSdyjo-46SbUO4Imllqcm_3AuSAy1Lc6t5CwvRoE2ln--fjnZMWFXecl8XCwixzzjAZbkXkHdWsuZu9vuLc2XxMjueG7ZavNBTDbeWkVqbIBRmya_BlSi8OsD53vxEhDDWB8xJIvCFb_WYaVA52eoDo0JBdCYaNJVTBXPk4nuqKnqg0c3JCAJDnozKbc1NLzepaGK6VtjRlLQBJIAEH8X05eTZ1vCLxf9YFsxr8Aiq8Fw7F4Z2uAGon0d-ZTZy7szzbcIyzYIqWTWg8m03_9hh1EblXYv9VoESUGIPVlbzUcCQIiXAv9RtSNGciLyHuLYjiJhZbWmU4-xnKbvhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این موشک ها سلاح اصلی ایران در جنگ جدید با آمریکا است
🔹
بسیاری معتقدند در صورت شروع مجدد جنگ، ایران این بار به پایگاه دیه‌گو گارسیا در اقیانوس هند یا پایگاه‌های آمریکا در اروپا حمله خواهد کرد. اما ابزار ایران برای این حمله چیست؟ اگر تهران بخواهد دیه‌گو گارسیا یا پایگاه‌های آمریکا در اروپا و اقیانوس هند را هدف بگیرد، از چه سلاح‌هایی استفاده خواهد کرد؟
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245961</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/690752" target="_blank">📅 23:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
آسوشیتدپرس: واشنگتن با صدور روادید برای مقامات ارشد ایرانی جهت شرکت در مجمع عمومی سازمان ملل موافقت کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/690751" target="_blank">📅 23:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f6e8a00c.mp4?token=aj8-e3KKiuKzc2gQswPrpDQnbP9l3_8EP34qcQaDuwXXndL8Jpl87qkKuAb27ASq7I0QW_V0a-y565HEvgroXx7FNzFWT7Z5DD2TnqSz21FLcCnyS7DTyKgYIiVodgoQjETihykJe6Ajv9A7XUcU28v_oF9ZbEvyBMsakPNl74ncDyq5nmfWRCugt7Bb6_teIgK2ITNkne1EMrbA095R2uu6asRu4BBMi69QBOtHgT9yUuXzO-WG6eW8rVVsFIwrFAtkQNF1VTKENyjGYqpm2Ukz--zd31W0VQZxkeyB0_fXl3BmOTHqxGYpV2TcNrBhxdZT_ICDfYxbLYAAaP0DWx2WQODAYXbCv6phZaZ7p9EDoG8RDJi1dixAUcSSPxymo2MOa_r4-mkYqvUm8VKGhf_UGoc7lwEtgIlEKZrwqzE0ytFK1mAdTcAUCbOoXonVGl9MLIU5nT4X4H7O6dx23CCcpxcihm2tdhAY-Y65M3R98vhEj6-IiZjfkKgc1v4992w-ML6ZINhJhazFRb0S30Fk69DrbH9hWH3Ww4aMoIe-h3xKpkpKH7vX6vV1diUofMYuA6aTPj08thgl4MO4mYpNPamGmkgTwROIo7xgGWcZDBUSrgI2F81ZTx91aj524Tnqw781TGQzBoJFsaehAU7AnSjLYmsuA31V18Rhywc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f6e8a00c.mp4?token=aj8-e3KKiuKzc2gQswPrpDQnbP9l3_8EP34qcQaDuwXXndL8Jpl87qkKuAb27ASq7I0QW_V0a-y565HEvgroXx7FNzFWT7Z5DD2TnqSz21FLcCnyS7DTyKgYIiVodgoQjETihykJe6Ajv9A7XUcU28v_oF9ZbEvyBMsakPNl74ncDyq5nmfWRCugt7Bb6_teIgK2ITNkne1EMrbA095R2uu6asRu4BBMi69QBOtHgT9yUuXzO-WG6eW8rVVsFIwrFAtkQNF1VTKENyjGYqpm2Ukz--zd31W0VQZxkeyB0_fXl3BmOTHqxGYpV2TcNrBhxdZT_ICDfYxbLYAAaP0DWx2WQODAYXbCv6phZaZ7p9EDoG8RDJi1dixAUcSSPxymo2MOa_r4-mkYqvUm8VKGhf_UGoc7lwEtgIlEKZrwqzE0ytFK1mAdTcAUCbOoXonVGl9MLIU5nT4X4H7O6dx23CCcpxcihm2tdhAY-Y65M3R98vhEj6-IiZjfkKgc1v4992w-ML6ZINhJhazFRb0S30Fk69DrbH9hWH3Ww4aMoIe-h3xKpkpKH7vX6vV1diUofMYuA6aTPj08thgl4MO4mYpNPamGmkgTwROIo7xgGWcZDBUSrgI2F81ZTx91aj524Tnqw781TGQzBoJFsaehAU7AnSjLYmsuA31V18Rhywc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد
علی فروتن:
🔹
چند نماینده مجلس برنامه را تعطیل کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/690750" target="_blank">📅 23:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FySzsbRMshvujTU3GJSTvG6Fo1ZMtKkOBVj7ZPIp-nIxRvh4Q7anMIli2gvQkWqyN3BV8NCJE63ri9vFaRyabqx48IEviFa_ctq5OMQEoqzeYZPfCoyoIqqktfYUuYDp25Ke7HoBW9C7Mm9KLFQCx25kAHHUifbTDeF1sNqef-GWd3Q8gUD91wLPQeTumBq1-NccTd87hmYjknyK7DRR9DtCZ1Zt_2FkrfKJirbcjNj9RG5NwoyLkXzx-7Rt___jb9cFDs36x9yas0r5djSFGyx0zKiQ77AItnyPyxTaYO9KNk4feHy2-soksnPhDEClbAuzZGKi3bvC6zGbyMfwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان جذب نیرو
🔹
«فرصت همکاری برای حراست، انتظامات و مهماندار خانم و اقا در گروه ایران نوین در اتوپلازا تهران(واقع در کیلومتر ۱۱ جاده مخصوص تهران) ایجاد شده است.
🔹
اگر به رفتار حرفه‌ای، ارتباط مؤثر و محیط کاری معتبر علاقه‌مندید، رزومه‌تان یا درخواست همکاری را ارسال کنید و جزییات بیشتر متعاقبا اعلام می گردد.
واتساپ: 09309000316
#فرصت_شغلی
#مهماندار
#استخدام
»</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/690749" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=FJqD6dWZdUpZnTA8Vm9Gi2UHylFb3oOkjdD4tfItql6xG9bmsB8VKxwIdPx1JFJZhn9bRjNK_BjEQ0IYcpP8siytBxKo1A55I5lxZWyTYVtScxA_IzDoRd-CzPh95TBz883-_P8JKrT0rlN78e_HoYvzBpSCXn-opkr6d_s51quDjtf4idEoarsnKaygAc6zqoswtfSl-mKIoRdzhyeCwLnxNV5ZxE2LgyvthVxOnjUhaIyoKUWMtqTHVQz9dbt2IEZBkvXofuFo8VDFH_QRyTK7zRq1ZsNXfJizltta6ewUvUcw7YU-gvlX9Nb4Pai66U9hZPgBb-QC7ZWoxVDA-pprj6lNG5B8--jfQF0dnixOH9NAnKquv80MbABfgPCPWZkadCWyPh_5LLNORVFQlnaHfhf30SnElWChhJ94V3gbXTTIaZhdcWwouUDeC8yf2vo4XxAdKJ-mr_qYmhI11aE9GzdbD-aVUXJfOwemLGodQCi3RSoEDez9Nsp8tbRqSSVgrz1m-HDcPlHTcGeCd8lGZZyGTCb0buuYfWgJrRvcp3PfrPdcgCFoCxoHPMhLvrShUAGPxL9ujd4dPC-PQ744o9rWnuJvllEoELsw7dqpO0eD-OO_SzN2Msndqgz1-YpBQb3FEHqBKxPEEodIRFvwNkbhF_ggoef-dFEMTjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=FJqD6dWZdUpZnTA8Vm9Gi2UHylFb3oOkjdD4tfItql6xG9bmsB8VKxwIdPx1JFJZhn9bRjNK_BjEQ0IYcpP8siytBxKo1A55I5lxZWyTYVtScxA_IzDoRd-CzPh95TBz883-_P8JKrT0rlN78e_HoYvzBpSCXn-opkr6d_s51quDjtf4idEoarsnKaygAc6zqoswtfSl-mKIoRdzhyeCwLnxNV5ZxE2LgyvthVxOnjUhaIyoKUWMtqTHVQz9dbt2IEZBkvXofuFo8VDFH_QRyTK7zRq1ZsNXfJizltta6ewUvUcw7YU-gvlX9Nb4Pai66U9hZPgBb-QC7ZWoxVDA-pprj6lNG5B8--jfQF0dnixOH9NAnKquv80MbABfgPCPWZkadCWyPh_5LLNORVFQlnaHfhf30SnElWChhJ94V3gbXTTIaZhdcWwouUDeC8yf2vo4XxAdKJ-mr_qYmhI11aE9GzdbD-aVUXJfOwemLGodQCi3RSoEDez9Nsp8tbRqSSVgrz1m-HDcPlHTcGeCd8lGZZyGTCb0buuYfWgJrRvcp3PfrPdcgCFoCxoHPMhLvrShUAGPxL9ujd4dPC-PQ744o9rWnuJvllEoELsw7dqpO0eD-OO_SzN2Msndqgz1-YpBQb3FEHqBKxPEEodIRFvwNkbhF_ggoef-dFEMTjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
این
طاق،
جاودان
است
مرمت
میراث
فرهنگی
، ادامه‌دادن مسیری است برای حفظ بنایی که سال‌ها بخشی از هویت این سرزمین بوده است.
پروژه
مسئولیت
اجتماعی
بیمه‌بازار برای مرمت
مسجد جامع عباسی اصفهان
، حالا وارد مراحل بعدی شده و عملیات بازسازی در بخش‌های مختلف بنا ادامه دارد. کاشی‌های آسیب‌دیده، سنگ‌ها و بخش‌هایی که بیشتر در معرض آسیب بوده‌اند، به‌تدریج در حال مرمت و استحکام‌بخشی هستند.
بیمه‌بازار
؛ در ادامه پروژه مسئولیت اجتماعی
«
طاق
جاودان
»
، همچنان همراه این مسیر است تا سهمی در حفظ و ماندگاری یکی از ارزشمندترین آثار تاریخی ایران داشته باشد
#مسئولیت_اجتماعی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/690748" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (اوفک) با انتشار بیانیه‌ای اعلام کرد که ۳ فرد و ۲ نهاد ایرانی را به فهرست تحریمی خود افزوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/690747" target="_blank">📅 23:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
حادثه امنیتی در تنگه هرمز
🔹
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرق خصب عمان، خبر داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/690746" target="_blank">📅 23:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkZhJWdluCj6AT3o5jTseJYnDY9IaIlL152W_Jaw2hgrzJH0ZpTikZebyFDyDb6aOkerbpxzoOnqAlAr9Xe0HSNTy9VuCbPUlgvh5tqqIVHDbsuw1gs0CKWapH7q5-ky8_xGJCdQEJAdVTBVgCh-zM0oQH2OTAr5Obz0srKkigwvQKz9gX1i_xNJkSwVhW9CJAhbfh7fk0ZeVT0NgkCmvF8QEGzfBvnvEFOzufR60DMO4vo5uugKsKQNCkBV8ffZIu3_P-1JGyeHAcBd5BiivCG3mVFfhMo0Bar5yqfyfl87cpvaqMD7zkDX45apE-2so8j3VNUN2R2F2p2Ut-sMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/690745" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: آمریکا در دوران حکومت ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/690744" target="_blank">📅 22:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmfRIiGoBEN9hWK58uzOwJlh407_qjSJcfwb0tClD6oty5GWcpJF9H5Ab5uhnMDh7hHRrMAKpfW3RXCHjqlOLew3n2oWutjSiGZOgI8Pv0PcploGYc0g0FV2fhbMCzO1f0o3GPs8D2mnrCwoVRA_m8XMYtfYnMnMjUfRwHjlyH82M3lbQfefqQgh3OW02IWwxHeTsOIEsJExuuDLcIxSu8KsMCl2nftZA2UfDEcT1tdmJeKkqW7iUHikVs2kNzqQlJlXCtnANWTBOXC_MdRugAglaSJEgfw-K6kRKywLlCvqtMWR3aD2y5TM8DJFs8foZP2loPozt2TTou5RrQHabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار آمریکایی: آمریکا در دوران حکومت ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/690743" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
رسانه‌های عربی از وقوع انفجار در شهر ابها عربستان خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/690742" target="_blank">📅 22:47 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
