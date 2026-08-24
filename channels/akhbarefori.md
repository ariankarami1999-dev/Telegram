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
<img src="https://cdn4.telesco.pe/file/XPfkhj0kr-pFMsqxHFhiW86i4nohER_4qs0rNvfIfJ7Y4uODZc0h_JfhFCDWGWliVyohipV4gQT-srIpscBC3juU5lMpEVvgara4x0kxuaYMge6VZQduQ1afOjdL1H3EyoF-K3eqlDjv9QtNmLIQ37t1pl_AAyazE-63qQ-8NKMhpmoCKXKCFRPRI9EFRoF8R9KJb9o8PFTQavLRX9qDns0SP9P-tYA4-12hOo83P5rVQP-1ezg3ewjsKBMUKtpP-m-ATvg1vlRwvQOaNW7C5g7EjYy88upx5hu18ekpPfdE4wfXljXWjW6dFxEnHvrzQW8T3mZ2SS6TAalnmz2bqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 13:58:37</div>
<hr>

<div class="tg-post" id="msg-683923">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
انفجار در شهر تدمر سوریه
🔹
منابع خبری از وقوع انفجار در شهر تدمر سوریه خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/683923" target="_blank">📅 13:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/683922" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23d45155.mp4?token=e1Arp30tMNkZTeleJUWPJNs0OjdR1PnIk_EreGogz6SdZx4BfTfJZVbsW15RTJe4WrswZy_nQAhk0_8ZL0sfDEEfF_N-8d6RlzdtqHpfpQYI2DuTcm_izGLwZ_LZ-h3MqVhTAseL_qLZgu6u3EI8JtxtCOsTacZTQcMXRom4B41zk6AUDBqimCLobxtPCGj-2AIq2HsFUFom8V0ZoSJNZQXai1z6h3TfquorNeN9YVLQEpK_nHHPWeo7km_bkhf3bw1Jv30C2k2mRllvFeFu9N8NfL-maLEPC_RVbNoDmmlHGDxFuu1-SiHqNUFXiBeDFMybvFH7Lmo-3GaFXoKX3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23d45155.mp4?token=e1Arp30tMNkZTeleJUWPJNs0OjdR1PnIk_EreGogz6SdZx4BfTfJZVbsW15RTJe4WrswZy_nQAhk0_8ZL0sfDEEfF_N-8d6RlzdtqHpfpQYI2DuTcm_izGLwZ_LZ-h3MqVhTAseL_qLZgu6u3EI8JtxtCOsTacZTQcMXRom4B41zk6AUDBqimCLobxtPCGj-2AIq2HsFUFom8V0ZoSJNZQXai1z6h3TfquorNeN9YVLQEpK_nHHPWeo7km_bkhf3bw1Jv30C2k2mRllvFeFu9N8NfL-maLEPC_RVbNoDmmlHGDxFuu1-SiHqNUFXiBeDFMybvFH7Lmo-3GaFXoKX3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: تهدید به تحریم می‌کنند؛ مگر تا الان تحریم نکرده بودند؟!
🔹
رژیم و آمریکا دنبال ایجاد شکاف بین مردم هستند، آن‌ها دنبال به میدان کشیدن برخی افراد در جهت خواسته‌های خود هستند اما کور خوانده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/683921" target="_blank">📅 13:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تقسیم اموال و دارایی‌های متوفی میان وراث مشمول مالیات نیست
🔹
بر اساس بخشنامه سازمان امور مالیاتی کشور، هرگونه تقسیم اموال متوفی میان وراث اعم از توافقی یا قضایی مشمول مالیات نیست، اما انتقال اموال و دارایی‌ها از متوفی به وراث و یا اشخاص ثالث مشمول مالیات بر ارث است./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/683920" target="_blank">📅 13:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651a0e2e99.mp4?token=VMaiqlYdBdZlQm-SgwNqnr4jODEMZZpne0gpUosL4ojcZ5xpR6gEEJeulH1imNKhjkvU4O9I2lQwou1t5rni4f4wWVpV5ApXEUs4tk-92eWWUXitupIiXSkry3QrI3eBwTIHhe24I1MR_3SWatX0T5CxQ39xMJkjQpjPJSnUR3MJy_2v9oWZhT6VgJPOPnu53ioF-v0ksov2NIlKf4Iz07vCVXxHyHOwHZKtriH7mWOK6MBSYPH4fJSvqPnSE1_f3_80fIcuoMAEXoCd3DdLtOwS8bpNmNoAJp1_CnYy9rvQVUd1L77TLs6PCEEfipRFTNBqnGo86FdLZR2NwO1FQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651a0e2e99.mp4?token=VMaiqlYdBdZlQm-SgwNqnr4jODEMZZpne0gpUosL4ojcZ5xpR6gEEJeulH1imNKhjkvU4O9I2lQwou1t5rni4f4wWVpV5ApXEUs4tk-92eWWUXitupIiXSkry3QrI3eBwTIHhe24I1MR_3SWatX0T5CxQ39xMJkjQpjPJSnUR3MJy_2v9oWZhT6VgJPOPnu53ioF-v0ksov2NIlKf4Iz07vCVXxHyHOwHZKtriH7mWOK6MBSYPH4fJSvqPnSE1_f3_80fIcuoMAEXoCd3DdLtOwS8bpNmNoAJp1_CnYy9rvQVUd1L77TLs6PCEEfipRFTNBqnGo86FdLZR2NwO1FQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیروزی را تبدیل به شکست نکنیم
🔹
آمریکا که تا دیروز به فکر سرنگونی ایران بود اکنون تمام بحثش تبدیل به باز شدن تنگه هرمز شده است.
🔹
بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/683919" target="_blank">📅 13:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/683918" target="_blank">📅 13:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9a4d424e.mp4?token=In0NN2OYX52Afq0mkalWd2LFYCl7QmcuLo71etVHT1hg6e8LQruxu3wmXgD5G4Hu_bQ7JmGJR9kpp0q3Dzt4_ccW0EeqifNezF8udR30BW_0BWeTkzZNH3LHMpwyIu8lpGEKiI08M9C20yUiS6pOFOKABE7w-aWEUaPLy1KMrlaUzCoPEtgd4Dh3E7uzNcF_ptI-I4nddPaunwVwvTzbw1aQBLKRouWJMPI3mK1EN1_wOC9_eOpeHbysJJYLk7PL564JXY6RuAKtpi34lRIjcxqcRzdWiwxgl4mbj41XYq8wYCk0J2aqWhy_rdUDlZNT4pOcD7VEzP3xYvPQiqaUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9a4d424e.mp4?token=In0NN2OYX52Afq0mkalWd2LFYCl7QmcuLo71etVHT1hg6e8LQruxu3wmXgD5G4Hu_bQ7JmGJR9kpp0q3Dzt4_ccW0EeqifNezF8udR30BW_0BWeTkzZNH3LHMpwyIu8lpGEKiI08M9C20yUiS6pOFOKABE7w-aWEUaPLy1KMrlaUzCoPEtgd4Dh3E7uzNcF_ptI-I4nddPaunwVwvTzbw1aQBLKRouWJMPI3mK1EN1_wOC9_eOpeHbysJJYLk7PL564JXY6RuAKtpi34lRIjcxqcRzdWiwxgl4mbj41XYq8wYCk0J2aqWhy_rdUDlZNT4pOcD7VEzP3xYvPQiqaUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از تخت جمشید از بالا، پایتخت امپراتوری ایران ۲۵۰۰ سال پیش #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/683917" target="_blank">📅 13:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqmxkS7xrYy6qwgpfG19El3-1uctEkoxrG42jwNMDW9PJAxDvejNOateL_FUAMaQ9NxEBB7qRXqJIdPi58fHoA6BaO0g-33BpcMzL5shFKPPEcLpHZ4TIc9KnwbqTjm1imATvo7v4R5mkoCK1GO3555jYmqA2V3Fz_JjaS18R7ppke0ElZuZC0f1ZGC5RSFkRuYVgTZTiNmY6T7HKej4g58tMdseTv5wW90ZmH0OWH2o75OkPw9NWavmWeK6RBN3jkhziwnwX1gwJpAbibnE0yaO2dG4PbtU69tHMwaZZ2U5oEjiWezaeCuJvQ5vNXBxVztqFA0QkD_qyY2o0W08BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFn0aQxmOPOat0xsOfl3F846ckYCObPNwsVs4smsvXcgVPdxYRV7OKxsrvaQPxZnnbztTBpHCsnuhJMlQKqCkDRMcdXMmqF-4QnDCns8I67TYOVZxkMF1kSfuhCY9j-o0MCD51tMmY5m2NxDH8grr6YnBc0313NbeG9oiqnPUJolruh2fuHf7o4DXv65nkEgx1WrKH5mamyJqOqcuuFX-C6NYKD9ff3khQ1TCiiX4KE0fEKKDhFOSEFgojvb5lCYlvqgay089-4b6kaz5gkxcroyQpB6FQVRgm8p-LIJveswP9fQb8WvcXrl5NKkI58Cy53DWpa3Mr2TottmcWrKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzTnUyerxgXrCAW1Gd2YaJ5bROwmHlLqUf455Z26d_tDWa4WuMWwM0Lc-MczW1H-mKaHaRVM5WxUtNNGguUhTDpNQ9VNIOjEbxgDxfJZCDwHABsZnXUxMPPpc8np37Gpe6bDkIF1rbxRZ_zEGWxu7XQrSvnAmIMSDmuNsUn1ZUe6MWgyIguxV7-kjWNMXYkyMx_Z1eBqAFHeeJLVCB2lZAdlBfFuWW8Ps8hboc3xw-7fpWpOlgQCSHCmOFka6VJOzoWv9j1xl2plBjgfDwYs7g4cBsIPCIVrJPt7SzCdRLBvLoLU5WSSuwSkFGwp0PG1cm9EweBFSF6MKhCONAO1pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طراحی منتسب به گلکسی S27 اولترا؛ شباهت به آیفون ۱۷ پرو
🔹
تصاویر فاش‌شده از طراحی اولیه Galaxy S27 Ultra نشان می‌دهد سامسونگ احتمالاً نوار دوربین مستطیلی و حلقه مغناطیسی سازگار با Qi2 را به گوشی اضافه می‌کند.
🔹
این گوشی به دوربین اصلی ۲۰۰ مگاپیکسلی، فوق‌عریض ۵۰ مگاپیکسلی و تله‌فوتوی ۵۰ مگاپیکسلی با زوم اپتیکال ۵ برابری مجهز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/683914" target="_blank">📅 13:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCpJGg2vH-QRZxro-pg6WBJL92bbrLvCiftyDk6HDz1-xGrV3CL3cO5yHMQl6AqimlUvHnQoBpcsEsAwPQt61974lWTLxGuxz8-YbNuLPU-ELpCvHC8RdJqXA_OmSugAxdwYTk1-uk2FXpkptcu6beNjENSeIWtWfWkt-PAptu3nCI6EuEDG8nSOyPvvAMZlgPeHPD5WCk9BuLBw83F7bET7bfO1dK_f7J_qHyy4BZeZdmWUtrt393NWVniuDJPDxbJLmrkJTFzi38KgMSkMG0ECJmpmsybpRfd3JGahjVVgaK6mQSEoqlVvh1fWWCSJYZmvi01x9yyxoh9CF-fAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲ شهریور ۱۴۰۵
🔹
بازار خودرو امروز ۲ شهریور شدیدترین موج افزایشی روزهای اخیر را تجربه کرد.
🔹
برخلاف نوسانات پراکنده روزهای گذشته، امروز رشد قیمت‌ها کاملاً سراسری بود و از محصولات اقتصادی تا مدل‌های مونتاژی و رده‌بالا، همگی یکپارچه گران شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/683912" target="_blank">📅 13:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: کشورهایی که سرنوشت خود را به تهران گره می‌زنند، با مسدود شدن تمامی مسیرهای دستیابی به رفاه پایدار روبرو خواهند شد ‎ ‏
🔹
هر کشوری که به عنوان شریان مالی برای نظامی در آستانه فروپاشی عمل کند، باید انتظار داشته باشد که در انزوای آن نظام…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683911" target="_blank">📅 13:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c7177ed3.mp4?token=FUEnUAzV-QAxNjRGTzAe177O_dVSl0So7VF3RXuI2e1D8PmuGoU8h4zzX1BXHJRavaZkOh9xP147qbIe_3wKylxGyBZH1rpejBEA2-1-fUokLketczdGGky0pcgX14CPL047tIHzfk9bljbtodEJsqq2t8IV5iOQdQmnzrwd1mDKvjWCo_IVO2T1fIpfs3fhOOo9OpM558w-P7mEU55z6cL7K71Lo4n4DHZcM2Oy4w_92QsuH7PpSa9Dk9NLtY9Miw3wX7k4_uPjKhyd036UUmFsa9xfXcr_aZ-74Hn_vVq0P-ax9WuU3kBRIpVXO1sXO5e5Kq7xe-tm5WMFlc9rIV7oYhFurjtHYbSDBHE-jGEE3Ud8lUedJzxtbDbJvD3vrbhz9D7z4PlaQT4psHRrApFiEss9wu0L6UZKgsXRWyc-UXn1cxJk_HpZ324X5Hb7v2YCReO4OxqB6uEf7cIptm1MQkumohUIMG0llqgj-LKorlHBxa0V8JGrDwmOMe9f5TTic_qJwMayPkFKzuf9lR-jMzDoGtZOaB6l9lH6uQ8ZlvMoESJoxnxhggOTq5xGWDWYsclJX6Nbeuwf5wwTtNc4ioh1URI3s6eNfNlQOStUCUrKDBCiVrHb8mkGl6hT_E6xqNyiq0Tb6WQ-rJVTbCnCA6P3RUcEm9EOkngj7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c7177ed3.mp4?token=FUEnUAzV-QAxNjRGTzAe177O_dVSl0So7VF3RXuI2e1D8PmuGoU8h4zzX1BXHJRavaZkOh9xP147qbIe_3wKylxGyBZH1rpejBEA2-1-fUokLketczdGGky0pcgX14CPL047tIHzfk9bljbtodEJsqq2t8IV5iOQdQmnzrwd1mDKvjWCo_IVO2T1fIpfs3fhOOo9OpM558w-P7mEU55z6cL7K71Lo4n4DHZcM2Oy4w_92QsuH7PpSa9Dk9NLtY9Miw3wX7k4_uPjKhyd036UUmFsa9xfXcr_aZ-74Hn_vVq0P-ax9WuU3kBRIpVXO1sXO5e5Kq7xe-tm5WMFlc9rIV7oYhFurjtHYbSDBHE-jGEE3Ud8lUedJzxtbDbJvD3vrbhz9D7z4PlaQT4psHRrApFiEss9wu0L6UZKgsXRWyc-UXn1cxJk_HpZ324X5Hb7v2YCReO4OxqB6uEf7cIptm1MQkumohUIMG0llqgj-LKorlHBxa0V8JGrDwmOMe9f5TTic_qJwMayPkFKzuf9lR-jMzDoGtZOaB6l9lH6uQ8ZlvMoESJoxnxhggOTq5xGWDWYsclJX6Nbeuwf5wwTtNc4ioh1URI3s6eNfNlQOStUCUrKDBCiVrHb8mkGl6hT_E6xqNyiq0Tb6WQ-rJVTbCnCA6P3RUcEm9EOkngj7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مامان اولین سکوی حیات‌روان هر آدمیه، برای همین نقش مادرها در سلامت روان انسان خیلی مهمه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683910" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آموزش ۵۰ دوخت گلدوزی با دست
🔹
آموزش ۵۰ مدل دوخت گلدوزی را اینجا ببینید. با فروش این هنر دستی، کم کم می‌توانید #چرخ_زندگی را بچرخانید
👇
khabarfoori.com/fa/tiny/news-3239788</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/683909" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5pqtqXpf_bynltjQFE9xAiYGFtHpxXVIjebyHahPv_dfeIg8stQCjp6TOX0HBt8sHjsInIAj5YJ31xsBBhLrH7o5Pe81B5cvJXcyDevcsOThN3i_FGm10R9UyF_QfVTjpOL3RySCANr2spj5dvV7O68-l07wwk4F4gP4U4fSBTggove_VZ88PeFk7e4waWi8hWRX5sX0lz9VFIWH_zKJ-NpcgFmrxSD87NBOMbp8nfvh64gFS08lf1wEsTN4tiVijEv524gIviDqw13dws3BcJbo6nnLzQv_fGtNF792rszR_d_xHufZvhdx6iDHYgft-PXwvwpMG7bUSvcyMQwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بخشی تقطیع شده از سخنان قالیباف را با هدف اختلاف افکنی در تروث منتشر کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683908" target="_blank">📅 12:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده کل ارتش: ایرانی تا ۲۰ نسل هم شده می‌جنگد و اجازه خدشه به ایران را نمی‌دهد.
🔹
سخنگوی سپاه: ایران در نبرد با آمریکا پیروز میدان شد.
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی رکورد تاریخی ۶ میلیون و ۱۰۰ هزار واحد را ثبت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683907" target="_blank">📅 12:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEA8nFY2oMsE2Ecexb29TDTCi1jhTkAp82Q1Po_WNXQc44lQ7KnzQtCaJRslUc2klycDh0eBrOz7tBoT_yBUHTyPqmxRMplUgc_bL4omDQNIgfEcLrtv2YueNN2K800cV-w3uuOLqW5WGLDaXvKfJb4IT-RE94lTlhUUb05Dj0YvMrexUfnaHl6oRGLf5hlC6fBcurhQ2ElCbQjo8WBxdXzNM3Un1sFR0Jvv0U0mAloe9PNaaewyn4v8f8Os-O5eXty0R6JlEJfD1T3CrPY-o21j0I_9NlBXoYCb8uHbybvVFnDNZQ73U9FhyXPhsxH1Mqf5FGtRjh5x3nhT5PKtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت بسیجی اهل سنت در زاهدان
🔹
یک بسیجی اهل سنت به نام «نادر سارانی سخی» توسط اشرار مسلح در شهر زاهدان ترور و به شهادت رسید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683906" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سخنگوی سپاه: موشک‌های ما فناورانه شده‌اند
سردار محبی:
🔹
موشک‌های ما نیز فناورانه شده‌اند و دیگر صرفاً به نقطه‌ای که از ابتدا برای آن تعیین شده‌اند شلیک نمی‌شوند، بلکه امکان هدایت و تغییر مسیر آنها در طول پرواز وجود دارد و می‌توانند هدف خود را شناسایی و دنبال کنند.
🔹
وی توقف آمریکا در جنگ را ناشی از قدرت و اراده ملت ایران دانست و گفت ایران در پاسخ به حملات، زیرساخت‌ها و منافع طرف مقابل و رژیم صهیونیستی را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683905" target="_blank">📅 12:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyep0sf4hVSgOxywXcuLMiPgaBNM5XwgAmNG3j2vV56M61HWF6_k8TG7vDC7YEzXzmdjw54Vsk4rxPc1aPnuNIq3k567nIOGaQX0Iq-tdfwQn6rtyCiS053dXCUd2dU_pt16VXTCxPFbUMAVLWW1Om7pvJ2H5KqGBvT70QOKf8OCpW_to3CiJPJ-pIlmXMI03ZTfAdrHa5ffUeb7JdsRYQ7sLHBRgLc7Uhb6EX9jxgHTWGEOQePwGHJdUMo3CbNewQUSyhQ3ck4KcPUcLdPQZ4VYsPJBZzbb7ciX8yb4ln4J1_7G1ZCbYTgonGbVO9SABmVLga8OfEhuSli5zKZQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان سابق فدرال و ایالتی آمریکا: پس حالا دوستان ما کره شمالی و روسیه هستند و دشمنان ما کانادا و دانمارک؛ منطقیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683904" target="_blank">📅 12:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
آغاز ثبت‌نام مسکن استیجاری تهران و مشهد از فردا
وزارت راه و شهرسازی:
🔹
ثبت‌نام مسکن استیجاری زوج‌های جوان در تهران و مشهد از فردا آغاز می‌شود.
🔹
از ساعت ۱۲ روز سه‌شنبه ۳ شهریور تا پایان روز چهارشنبه ۴ شهریور متقاضیان مسکن استیجاری زوج‌های جوان در استان‌های تهران و خراسان رضوی انجام می‌شود.
🔹
در این مرحله ۳ هزار واحد مسکن استیجاری برای اجاره به زوج‌های جوان فاقد مسکن با اجاره‌بهای حمایتی عرضه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/683903" target="_blank">📅 12:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3325bfbe5f.mp4?token=kv-4OdchXN5YRX_tPZhRakCe5rRrKvsxaK33c4pGLURSsn6BDXMg6f5CkmkouVTOG84Hbrb4QB57E6Ze9Jc862czc5nAcZ5Tr5JwJfGnMehs_B6N6p33e_wjIkE2ZD3cVxHISqxCOTkOJAmCgVyAx3_rDP2CKGf0SEhei_2bhd9Rgq-xajhUk8pz67wxJu30RX38CvBK3RDpboNnSB7b6sbUJA8E9fz_ZtRADklNB7qsBNSh-mGLzDz4DKzokYVlIvBOjn30zgH72i872cwHvGBl5QxzLLG6VVVeRFHffVRNO2drnBDgmpT67Y2_j0QY7F4oUQ5pjE_XcjNLaLOIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3325bfbe5f.mp4?token=kv-4OdchXN5YRX_tPZhRakCe5rRrKvsxaK33c4pGLURSsn6BDXMg6f5CkmkouVTOG84Hbrb4QB57E6Ze9Jc862czc5nAcZ5Tr5JwJfGnMehs_B6N6p33e_wjIkE2ZD3cVxHISqxCOTkOJAmCgVyAx3_rDP2CKGf0SEhei_2bhd9Rgq-xajhUk8pz67wxJu30RX38CvBK3RDpboNnSB7b6sbUJA8E9fz_ZtRADklNB7qsBNSh-mGLzDz4DKzokYVlIvBOjn30zgH72i872cwHvGBl5QxzLLG6VVVeRFHffVRNO2drnBDgmpT67Y2_j0QY7F4oUQ5pjE_XcjNLaLOIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خارج کردن کیست هیداتید از مغز
🔹
کیست هیداتید یک بیماری انگلی است که خارج کردن آن از مغز نیازمند جراحی بسیار دقیق برای جلوگیری از نشت مایع و گسترش عفونت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683902" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a28fd090.mp4?token=Zmvct2bmHPkEuRScDQ5MJ4bdahmH8q2weng_h9OHNx1Ur_gCTZCpSTDNxBnnkVKSaoaD-HM6rrQz_620tnt5SAuXPWDpEeUMo5Pl3ZIirYbugI9vQez5yM4SV0iZRX2LS9ZvR-OggBxBXZVKWjfn1-D94NHLGxUmHIcbYJVgIjfkoQs4uYJWC4wDaNjpjnjCR6YE7_9Vwv8ODklAb7GlIaKDtnMgMmCN4irz9JLFe-6spcSAFfXMXK74NGUgPc1-Nn1rOyre2oSQDTnmA60suEFY-IEnUN4u7NTYyID8C-Ebdpjm-aesjFf2bl6jg5edu7TaTuINs4qwy1-VaJ77Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a28fd090.mp4?token=Zmvct2bmHPkEuRScDQ5MJ4bdahmH8q2weng_h9OHNx1Ur_gCTZCpSTDNxBnnkVKSaoaD-HM6rrQz_620tnt5SAuXPWDpEeUMo5Pl3ZIirYbugI9vQez5yM4SV0iZRX2LS9ZvR-OggBxBXZVKWjfn1-D94NHLGxUmHIcbYJVgIjfkoQs4uYJWC4wDaNjpjnjCR6YE7_9Vwv8ODklAb7GlIaKDtnMgMmCN4irz9JLFe-6spcSAFfXMXK74NGUgPc1-Nn1rOyre2oSQDTnmA60suEFY-IEnUN4u7NTYyID8C-Ebdpjm-aesjFf2bl6jg5edu7TaTuINs4qwy1-VaJ77Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: از «تحریم‌های فلج‌کننده» تا «فشار حداکثری» و جنگ اقتصادی، آمریکا به‌دنبال تسلیم‌کردن ملتی است که تصمیم گرفته از حقوقش کوتاه نیاید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683901" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
عاصم منیر راهی ایران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان، برای دیدار با مقام‌های بلندپایه ایران، به همراه وزیر کشور پاکستان، اسلام‌آباد را به مقصد تهران ترک کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683900" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کلید اولیه سؤالات کنکور ۱۴۰۵ در هر پنج گروه آزمایشی منتشر شد.
🔹
رئیس بانک مرکزی: مشکل تامین ارز نداریم.
🔹
فرماندار جاسک: احتمال شنیده شدن صدای انفجار کنترل‌شدهٔ مهمات در جاسک وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/683899" target="_blank">📅 12:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFj6kSLoZtbk8zLET7u_r6Gq2H0JxoiMMKILVPQ_VGtBP4Y8OVspCGedF9bj_t-Oc_VJj5Il1mbhxUdR8SXf23byocrvYNx32MHza2wSv-YFBGZdPc5Vvgh8pPZsgDdxUzfdDupr7a_yJfaoG7GhFec2p-7BgDY2POGEoVQdmyLDHTO0xSuHt6K9WxCD9zQFaBJD9Skw0aoQNhkV--0b5cTcdmF46-h5ShVtMxSbQHvlD4YUB4YCSxtoDJX3AGMH0n_2-elSx7_tsW6kQIsEp8s2gwJdGig7EgryBZDargNR369R1lnvvjyhaB1j7ySPhLy82MvLLhXGxo5fCPWCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683898" target="_blank">📅 12:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران در حوزه حمل‌ونقل و لجستیک بین‌المللی
🔺
اتاق تهران با ارائه مشاوره تخصصی حمل‌ونقل بین‌المللی، فعالان اقتصادی را در انتخاب مسیر و شیوه مناسب حمل، کاهش ریسک‌های تجاری و حل چالش‌های گمرکی، ترانزیتی و بیمه‌ای همراهی کرده و مسیر تجارت خارجی را کم‌هزینه‌تر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/683896" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
عاصم منیر راهی ایران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان، برای دیدار با مقام‌های بلندپایه ایران، به همراه وزیر کشور پاکستان، اسلام‌آباد را به مقصد تهران ترک کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/683895" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Opr-gKStKtyhIQ8LKHC46lDUlmQ-2kSaLZMjUpPWhUpW1eUhyk64ERjwiWhw6KfyaaOgSXRLCf2AkkdL-bTb4WV3pBrhRyLP9PEKEl9ZVLdmt_CExNsAkDvaZZF3K-XovHvi3OYzEaTrAYInCJrozSWvf82LR-Th0JS4S1R7ShRTgSNEFOyunFuqPAIIyqICfDmxPYcsaLXF1AHwLSNXjdpmRW-LDAgJdu1960ZyNhd4X5XuU68kJZ38PYa-GjJZhp4j1AHYRfoA_m8-U9jQKtLij1vbEmKSSJfm8AgathI4L28TkXQy4zfQ09gP1b1ww35U61isD2GtW_DSRxkoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرش پازیریک؛ یکی از قدیمی‌ترین فرش‌های جهان
🔹
فرش پازیریک با حدود ۲۵۰۰ سال قدمت، نشان‌دهنده پیشرفت هنر فرشبافی در ایران باستان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/683894" target="_blank">📅 11:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2803d6a33.mp4?token=NR-Kx4WDGnejljMU7VI54iXdZRlwIyfuv7lnsuGHG7ydCXZv_fDxDKGnQFEMYOcXZVyNwNEHRRnvIWyb0rzWF3PJP-EAysIetZkRbSEQheh88oJAG5TF-SkSRkRCo5t_nfYx1u3I0qofV2d6aZLjItcjtkr-ahUpzEUxaxfHZGoWTAHINw7ALn4CAvBOAQk5FyJKGEW0OVZudoPPjPxMFXVeDzNNa42TTfqKV_pn9y5uKytod2T9KSuyqigbM3UChza4-MyLf_54XuiUJOA41mAQyET4FTSuwqZy-XbJJzwL3sg34auHHD_rjNCMHeMm3H5w36j3SpAt5YilRZS4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2803d6a33.mp4?token=NR-Kx4WDGnejljMU7VI54iXdZRlwIyfuv7lnsuGHG7ydCXZv_fDxDKGnQFEMYOcXZVyNwNEHRRnvIWyb0rzWF3PJP-EAysIetZkRbSEQheh88oJAG5TF-SkSRkRCo5t_nfYx1u3I0qofV2d6aZLjItcjtkr-ahUpzEUxaxfHZGoWTAHINw7ALn4CAvBOAQk5FyJKGEW0OVZudoPPjPxMFXVeDzNNa42TTfqKV_pn9y5uKytod2T9KSuyqigbM3UChza4-MyLf_54XuiUJOA41mAQyET4FTSuwqZy-XbJJzwL3sg34auHHD_rjNCMHeMm3H5w36j3SpAt5YilRZS4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تفاوتی نمی‌کند چه کسی سکاندار سازمان ملل متحد شود؛ عملا کارکرد شورای امنیت و خود سازمان زیر سؤال رفته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683891" target="_blank">📅 11:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee097abcfc.mp4?token=GU4k4B2Qwo1SAXJghmZglFrND7bgUZy2uNO5bXqXgbrdRORNu8ARBX9ve-3kP2nsgh3hzQne2I8wnOQDJ9MdbQQnaZz49DdADRtRmFGZucVyNj7oX_71KT07FDU5oZb5wBous1ewctD8fEjyOriBwbxtUVAKXyZfuy0UynqwZfQCEoaQqAAzWekikqRMfS8S32p6EKQ8fJTfo3kDn4b5RjQL3fMw8mEVRMdO1Phy0GftJOdPtI0OQMtZ7DAD7rnMB_3AsPPT_sxFi7HLBZO4MveFkWRpcR_jOcAZ6PQof_RxiKA71IsFPT-2htOZ0Xnt_327x_w9NpT3UyPpTMr2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee097abcfc.mp4?token=GU4k4B2Qwo1SAXJghmZglFrND7bgUZy2uNO5bXqXgbrdRORNu8ARBX9ve-3kP2nsgh3hzQne2I8wnOQDJ9MdbQQnaZz49DdADRtRmFGZucVyNj7oX_71KT07FDU5oZb5wBous1ewctD8fEjyOriBwbxtUVAKXyZfuy0UynqwZfQCEoaQqAAzWekikqRMfS8S32p6EKQ8fJTfo3kDn4b5RjQL3fMw8mEVRMdO1Phy0GftJOdPtI0OQMtZ7DAD7rnMB_3AsPPT_sxFi7HLBZO4MveFkWRpcR_jOcAZ6PQof_RxiKA71IsFPT-2htOZ0Xnt_327x_w9NpT3UyPpTMr2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: دو هفته قبل سفیر و کارکنان سفارت انگلیس به تهران بازگشتند؛ ظاهرا به تعطیلات رفته بودند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683890" target="_blank">📅 11:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3BHuX-75eTl7Pvytg2iELDNCipXw85DnRWrtxlKXRHOJbOBHiJujZpxdXM-cTy9_wjAw0higoAJvITuWFmV1BQrjwOZ7IxTxmRbX6i9b1sZJqHavQFr-HXOyd3ajEKMnle_zbpryMDkUlUI3K-05Quv16deMdjZAS0r5wKGz6Gb_ag-zCDF20Dgy2Fmn2qE94zi1T-Bemff8bLttP8jL0q5vIPaJyHxwYk564mg9_Z34WBeITMYaCA1vbxdRMtb2sw4XLxWo7nSQxXCI9bEi2Bjvn_aLBK1KOo_OFkpTOgxFa8-K2iJRgKuAD4idU2gfm2GUcaku3DoPyLn69snwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: شناورهایی که با شناورهای متخلف همکاری کنند به فهرست متخلفین اضافه می‌شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683889" target="_blank">📅 11:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5d35361d.mp4?token=N1mPXkuAoQ32UaKupD97xOTXMe9Cvc2B0Pn-4aPOkmpFl4yEAq3aZR4YHuPr0LyR4iUq5HQm88RVsjs-KWitU3WDEXdh0NDJzlteiTZbbPt5zJvwRYJGlHhpJdA7QaEmi2kKb9H1rC9qO1es2FHuIMitMPsM8HbYA00--3u_zbHi2F0Hw7yf7hlP19MV41gvqmCwdWnkYDXZfu5F10XQZTfnp_XunaaZISaRRHWZXlXU_C1vFQByEIMKuIeaZO-7CMAJ1ebqeOJca1HB2myehQU5XxBeRLHJ0TKLeTCOZN688To_gZ52FQMqkukbeH2PwavUkMc0BTNd2I4eiW7H5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5d35361d.mp4?token=N1mPXkuAoQ32UaKupD97xOTXMe9Cvc2B0Pn-4aPOkmpFl4yEAq3aZR4YHuPr0LyR4iUq5HQm88RVsjs-KWitU3WDEXdh0NDJzlteiTZbbPt5zJvwRYJGlHhpJdA7QaEmi2kKb9H1rC9qO1es2FHuIMitMPsM8HbYA00--3u_zbHi2F0Hw7yf7hlP19MV41gvqmCwdWnkYDXZfu5F10XQZTfnp_XunaaZISaRRHWZXlXU_C1vFQByEIMKuIeaZO-7CMAJ1ebqeOJca1HB2myehQU5XxBeRLHJ0TKLeTCOZN688To_gZ52FQMqkukbeH2PwavUkMc0BTNd2I4eiW7H5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی درباره تعطیلی سفارت شیلی در تهران: تصمیم گرفتند به خاطر صرفه جویی مالی سفارت را تعطیل کنند و در برخی کشورها این کار را انجام دادند؛ این به معنای قطع روابط نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/683888" target="_blank">📅 11:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رایزنی‌های آقای قالیباف با مقامات عراقی روند همکاری‌ها را شتاب می‌بخشد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683887" target="_blank">📅 11:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdf70a392.mp4?token=sMLRqRrVdyBgGX4lXZP5NqE-QCZYbKAmxrAwva5467G7oFVwKARJnbz_yCvQKyhZeZ5PzW-kXgPjqB1VJGhEoUPALgxBq_H_pSnlZsTH0Iqy-kGWYGqOM0fRajr1azxeNpOKdk5JhelLq8WzQmgnctvzhSmBKYKVOvmFs8NHnvSGmxaBnutXR6-R6BSEkbavK7ZE4r3URvLoz0HD7grU002mx1DXB3RxN8n7E0CNcm7MKdgBsYv_f6ndOS1xjgkhvbaKpD80Kk-_Mpu4eb-ajB4Rz37-Llzo4RZSPxMMlKq-55AP7J9occpr2wqAJ4way8K3GuLM804VuQ1MtZPnlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdf70a392.mp4?token=sMLRqRrVdyBgGX4lXZP5NqE-QCZYbKAmxrAwva5467G7oFVwKARJnbz_yCvQKyhZeZ5PzW-kXgPjqB1VJGhEoUPALgxBq_H_pSnlZsTH0Iqy-kGWYGqOM0fRajr1azxeNpOKdk5JhelLq8WzQmgnctvzhSmBKYKVOvmFs8NHnvSGmxaBnutXR6-R6BSEkbavK7ZE4r3URvLoz0HD7grU002mx1DXB3RxN8n7E0CNcm7MKdgBsYv_f6ndOS1xjgkhvbaKpD80Kk-_Mpu4eb-ajB4Rz37-Llzo4RZSPxMMlKq-55AP7J9occpr2wqAJ4way8K3GuLM804VuQ1MtZPnlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد بقایی برای جلوگیری از خودکشی سربازان آمریکایی: منطقه را ترک کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683886" target="_blank">📅 11:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e45d3e038.mp4?token=PgIEuu8frflTDNR9b7jkBhtMGaK6PeVKG0iHGXx8FA73_tsW49yxGF5Woi0KXAofESkTiysdSG8apZWoQuIiOEdOs5YHJpORnJr0JcO1eVdJXQXnE6vNRPrb2K6KXa5oLVch8vHy3-Hkiozt5tU15IuVgH4VAu5JIp9EVrvL8kkszBoCuAG7_gBVR82GSNK2bmjI8L9Ol6pDg0Zzx6dTGX9MpuD4ZwsMFGDZEFpu_qKyUfV5RWtP5YU3akVLWI_-s5tBWOtL_EmvLi4XKOITTve3MtuekfRxSl5nV0kewoaomshtDj11ZVW4_I-okvw85Li4lyUl_rxkeYtxZNVv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e45d3e038.mp4?token=PgIEuu8frflTDNR9b7jkBhtMGaK6PeVKG0iHGXx8FA73_tsW49yxGF5Woi0KXAofESkTiysdSG8apZWoQuIiOEdOs5YHJpORnJr0JcO1eVdJXQXnE6vNRPrb2K6KXa5oLVch8vHy3-Hkiozt5tU15IuVgH4VAu5JIp9EVrvL8kkszBoCuAG7_gBVR82GSNK2bmjI8L9Ol6pDg0Zzx6dTGX9MpuD4ZwsMFGDZEFpu_qKyUfV5RWtP5YU3akVLWI_-s5tBWOtL_EmvLi4XKOITTve3MtuekfRxSl5nV0kewoaomshtDj11ZVW4_I-okvw85Li4lyUl_rxkeYtxZNVv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: تکرار تحریم‌های ناکام علیه ایران حاصلی برای آمریکا ندارد؛ جنگ اقتصادی آمریکا نظام تجارت بین‌الملل را تهدید می‌کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683885" target="_blank">📅 11:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0470d0b747.mp4?token=W6yVx49rSZbdZIzK9YRdVniCLDGE3l55ujD8zHPS9BJLzHVa--nqbFOqQYbKRVAhKc6wKVcujFRoxUZ0m0TnC4U9g8lpkFJeEJwYathBXHJ7bBpzwOHzwPOrNazQlmZKVx7UBvO7D54oFvNBMtQrDfttlCF2vhy6FqgWIcff9vBrieMiU2_w1-sZBUjm0d-T6tFud8Gy5GqUb2qwehAlJL_O-JMJIcIzFPD_Tip4Vw8f9x4ASOUyR1V34Qio0BBYaSDytNZOsuMqYsnft1b94MT6myCDt2xHgdSQsA-VrGi9Ai-3dus76d38OleSS-tQZLjiz1_RkHBb1rdGHZEoaCX_OZjjpzbLQ0_JhVUBlWC1pPygNU5sFh-i9_eagLXc0eTWm5PkvX9xZq1vZxakFi4OJKL-Hd_71L09wwDi-Do7zG6JECgQ1pjUpAqJLqmHu0-Wa2E1vo4U4ToAvWYWap2cFYTZPNaDCJai0UGZ5ElDEctWLjf1zbu_0QnAT6sGEuluaH9urT8MHsemDq3_h_F3q5gQreoX6K1DosS06CT5bpuYsTESYTGascJotxgwfv7X83eun736azopmj6tdbtIJ6yXw3zD71vPZKMEApLOLOwJSdj4gV_9NbwsvQ9eg2p9IELyfdSevpzXQrQ8nZNUC1PrGDzp4FdUYBQQT7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0470d0b747.mp4?token=W6yVx49rSZbdZIzK9YRdVniCLDGE3l55ujD8zHPS9BJLzHVa--nqbFOqQYbKRVAhKc6wKVcujFRoxUZ0m0TnC4U9g8lpkFJeEJwYathBXHJ7bBpzwOHzwPOrNazQlmZKVx7UBvO7D54oFvNBMtQrDfttlCF2vhy6FqgWIcff9vBrieMiU2_w1-sZBUjm0d-T6tFud8Gy5GqUb2qwehAlJL_O-JMJIcIzFPD_Tip4Vw8f9x4ASOUyR1V34Qio0BBYaSDytNZOsuMqYsnft1b94MT6myCDt2xHgdSQsA-VrGi9Ai-3dus76d38OleSS-tQZLjiz1_RkHBb1rdGHZEoaCX_OZjjpzbLQ0_JhVUBlWC1pPygNU5sFh-i9_eagLXc0eTWm5PkvX9xZq1vZxakFi4OJKL-Hd_71L09wwDi-Do7zG6JECgQ1pjUpAqJLqmHu0-Wa2E1vo4U4ToAvWYWap2cFYTZPNaDCJai0UGZ5ElDEctWLjf1zbu_0QnAT6sGEuluaH9urT8MHsemDq3_h_F3q5gQreoX6K1DosS06CT5bpuYsTESYTGascJotxgwfv7X83eun736azopmj6tdbtIJ6yXw3zD71vPZKMEApLOLOwJSdj4gV_9NbwsvQ9eg2p9IELyfdSevpzXQrQ8nZNUC1PrGDzp4FdUYBQQT7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا هم دربارهٔ آن‌ها گفتند «امضایشان را با مداد می‌نویسند».
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683884" target="_blank">📅 11:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c317278ea.mp4?token=qTCJzgSAMneMWoELhbaDKWrSPPCI1iwVH3jsb_2RfKD-7E882DcLRHJRO0udigvOlD85I51SqFS4FoRsCTJLG-4w6Gsy7TZB0marqlF_C1qYA4l86TSMC_FOzHPADIEn68xw5IvbF0jwsqza3T33tAXZ_vt6QnLjT-Jwa5MjTqRSg7-ydKgU4Hi-7iIOKhZu7uz_FygJi6-souh3U855jPjmYTUsY7lUiDPQ4Yot-YkLOhKMEjYvX-8nVD4mB7rzKKrCxnz4KTo-9hhVW2w5RSPkMYRtGAdO4jsIB8gPL-6iiTmEVt2wKUMBBDY8xQcsF4rnCpj9bDRYqW99Zd8gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c317278ea.mp4?token=qTCJzgSAMneMWoELhbaDKWrSPPCI1iwVH3jsb_2RfKD-7E882DcLRHJRO0udigvOlD85I51SqFS4FoRsCTJLG-4w6Gsy7TZB0marqlF_C1qYA4l86TSMC_FOzHPADIEn68xw5IvbF0jwsqza3T33tAXZ_vt6QnLjT-Jwa5MjTqRSg7-ydKgU4Hi-7iIOKhZu7uz_FygJi6-souh3U855jPjmYTUsY7lUiDPQ4Yot-YkLOhKMEjYvX-8nVD4mB7rzKKrCxnz4KTo-9hhVW2w5RSPkMYRtGAdO4jsIB8gPL-6iiTmEVt2wKUMBBDY8xQcsF4rnCpj9bDRYqW99Zd8gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران سرنوشت خلبانان ایرانی در قطر را تعیین تکلیف می‌کند؛ آزادی فوری چهار شهروند بازداشت‌شده در کویت در حال پیگیری است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683883" target="_blank">📅 11:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtyxZi9eSWb6nedU3-1LN_elhA9ZIq7nSedeuS3XbIC9aNOxJ-EOV6xqME0x432VgQIcTCUPzeuXwbQIsb5bFvrgkIX7Wr0IIlFEEYjuEoYm3Xg8TfncOdc-eqINI9pMfclTkhjRFMSXLPc-I_rAFN2CqOeoHHrWZkkyD0Mp6xSXVsf9xUIhvbby1yXJJhkPtDS2nFZuhLrsm1Lo72CGnfT3J6FMJksrvYsSziTG6QxryScmXPQihTAJpTB0vHhw53e7x078LMy2tTjb3aivKSuNLZy_cGgKLsE2yejko3BRm0tUSfmeEfVIAP62saWzWRfEGFdEihu8IkKyue9CYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا همچنان قله فتح می‌کند
🔹
قیمت بر اساس سایت رسمی اتحادیه طلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/683882" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bbf1efe70.mp4?token=QhJo7mgywmVrCZtnApTivNojxh1dNmWt5Ua6KC8qQKc_mTIi4lj3ZaZoLzLpIIOMiwArpUN23cx9oNJQkovtt0LZYzo22CcSyFEN4ZPnlqZwvW5orDJqITqFigkUanc1iIq7HKcqUcXlGF8Xh0WwmvPyTiKzEtyjF-cjFyshJW_haHcySGRPMqXbgevkiKe0-QEv1_lszPhwbWNTSpMqViuqvexcnnlzF0ODdQXtdOAOZSdlfNozNgvTDrRaGD0uwbZ8PfOxUwFiNFvPvogAuDYDOCrbBSWDPk09I_lMV9YmxN4DzwVeA40BLG0r4NvKSA07a2yYewYbHktaZCU9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bbf1efe70.mp4?token=QhJo7mgywmVrCZtnApTivNojxh1dNmWt5Ua6KC8qQKc_mTIi4lj3ZaZoLzLpIIOMiwArpUN23cx9oNJQkovtt0LZYzo22CcSyFEN4ZPnlqZwvW5orDJqITqFigkUanc1iIq7HKcqUcXlGF8Xh0WwmvPyTiKzEtyjF-cjFyshJW_haHcySGRPMqXbgevkiKe0-QEv1_lszPhwbWNTSpMqViuqvexcnnlzF0ODdQXtdOAOZSdlfNozNgvTDrRaGD0uwbZ8PfOxUwFiNFvPvogAuDYDOCrbBSWDPk09I_lMV9YmxN4DzwVeA40BLG0r4NvKSA07a2yYewYbHktaZCU9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران از ورود دو دیپلمات متخلف فرانسوی جلوگیری می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683881" target="_blank">📅 11:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573583b848.mp4?token=cYv8w6ssXXRF9sITv8X5SZSo_e_0ZgBTMH6620rc_rYVeQDVo5BuLkETA6lWtHE49dMUUcB0cZiTRecdse5aGPbvOGbat4KZnfqGCZ9qwiBWfCBzFl7o3kdYQOXGF9Nb3yZLHbVcGo1Y4-kx9K2u-9y0VIQ1rn1gojq9ZAD_cxuN2Ll2LcilUerRKc9qOMh03lR2vQvVSgGWu9i21SHAPakuD6QyFU0_-sICaf-5javrxOadAhU96EqDt7fR1SnxHIWK2Nw60_TLVk1koFivlvigEMQxKI-HY8Ki0cqNTqDNTGdz852Dt19XVw_v8iQUJ5CTkKESSVJzOSVI3BaEXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573583b848.mp4?token=cYv8w6ssXXRF9sITv8X5SZSo_e_0ZgBTMH6620rc_rYVeQDVo5BuLkETA6lWtHE49dMUUcB0cZiTRecdse5aGPbvOGbat4KZnfqGCZ9qwiBWfCBzFl7o3kdYQOXGF9Nb3yZLHbVcGo1Y4-kx9K2u-9y0VIQ1rn1gojq9ZAD_cxuN2Ll2LcilUerRKc9qOMh03lR2vQvVSgGWu9i21SHAPakuD6QyFU0_-sICaf-5javrxOadAhU96EqDt7fR1SnxHIWK2Nw60_TLVk1koFivlvigEMQxKI-HY8Ki0cqNTqDNTGdz852Dt19XVw_v8iQUJ5CTkKESSVJzOSVI3BaEXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه از اخراج دو کارمند سفارت ایران در این کشور خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683880" target="_blank">📅 11:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حادثه دریایی در غرب ینبع عربستان
🔹
سازمان عملیات تجارت دریایی انگلیس از وقوع حادثه دریایی در ۶۳ مایلی غرب ینبع عربستان خبر داد.
🔹
یک نفتکش در غرب ینبع بر اثر اصابت یک پرتابه ناشناس آسیب دید که در پی آن آتش‌سوزی رخ داد، اما هیچ‌یک از اعضای خدمه نفتکش زخمی نشدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683879" target="_blank">📅 11:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cdc830a2.mp4?token=IDS0BLP_yecVTd-WWCCY_WyJX8zTIaaEatJW03iYQawymo0zlCmL4GCCZ1U34Hj0Cmi9q3fUv231ND-O4FhYgnej2ksAlHBK24Qpen3P-Ihe35UxGfL-5GLU1r7Nl3sFAZ9y7gttf5faLBt4uiEWxvCJvxArpsRQcKloo_6u1RuoKZK5fos5BlMQ1qWxqe_tzFYiQHjWMhyny6nQPbYkO5ohxzv4Y5fhPyBI-nc-qWBiRd3PwmOrH4teJR3VdCduGdJoUCawBC-Ipd2q0wl4UMXZxpHWhIP1vC4gFlxADIEDrbttQ5AYPhzmCVAiO8_jXvkKZ4xKhIdricl-HvZtwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cdc830a2.mp4?token=IDS0BLP_yecVTd-WWCCY_WyJX8zTIaaEatJW03iYQawymo0zlCmL4GCCZ1U34Hj0Cmi9q3fUv231ND-O4FhYgnej2ksAlHBK24Qpen3P-Ihe35UxGfL-5GLU1r7Nl3sFAZ9y7gttf5faLBt4uiEWxvCJvxArpsRQcKloo_6u1RuoKZK5fos5BlMQ1qWxqe_tzFYiQHjWMhyny6nQPbYkO5ohxzv4Y5fhPyBI-nc-qWBiRd3PwmOrH4teJR3VdCduGdJoUCawBC-Ipd2q0wl4UMXZxpHWhIP1vC4gFlxADIEDrbttQ5AYPhzmCVAiO8_jXvkKZ4xKhIdricl-HvZtwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه در واکنش به خبر عبور روزانه چند میلیون بشکه نفت از تنگهٔ هرمز: این بخشی از جنگ روانی دشمن است و چنین چیزی نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683878" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5421dcc55f.mp4?token=abMinQ4MxMEOgQtMS49G-yejfHT4uoA0fwLnnylrWrUYOGKq3aNlmIRmacfaq4NZvMBmQZjEFn1x4ODYuApi8C04yng70ehtsQ_226oGJ81k0bnfm_UgLZhuJFfvu7qgk7Au-8ESrVpKdX-TelE4FRUGxFhGAVgDFCzM2GMUI18RxQmb_HeNJZWQXTTp7Cd9YI4Si_RVWvEYOOdsgWb4gVb6jfDsKY60KugPfPjWhh4eLOuy78x0ida8HgKPfvU5R732MasDX8H7iRWW9oYGdbxTagK-xIPK7AD91_hpgZffx5f95yeNlV4S7EuuO6Ezkf1zgSKsQk-VLGujr_oNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5421dcc55f.mp4?token=abMinQ4MxMEOgQtMS49G-yejfHT4uoA0fwLnnylrWrUYOGKq3aNlmIRmacfaq4NZvMBmQZjEFn1x4ODYuApi8C04yng70ehtsQ_226oGJ81k0bnfm_UgLZhuJFfvu7qgk7Au-8ESrVpKdX-TelE4FRUGxFhGAVgDFCzM2GMUI18RxQmb_HeNJZWQXTTp7Cd9YI4Si_RVWvEYOOdsgWb4gVb6jfDsKY60KugPfPjWhh4eLOuy78x0ida8HgKPfvU5R732MasDX8H7iRWW9oYGdbxTagK-xIPK7AD91_hpgZffx5f95yeNlV4S7EuuO6Ezkf1zgSKsQk-VLGujr_oNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: سفر وزیر خارجه عمان به تهران هیچ ارتباطی با سفر فرمانده ارتش پاکستان ندارد؛ فقط از لحاظ زمانی تقریبا همزمان شده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/683877" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86534c54a.mp4?token=KXbn7yEi08GcpSwfyYBvpOx7Kxhc4tVHIUFF7QOx4DBwrm01JnFEmg7nehNzXXYCvuVjlq018LXUqBzxRqv-egDXe6D7OvmnTG5I_3rizTS7Txi2Vq6qZIbVUXp8LwtlIMc5aFoQJi-aKnIgwmSGyfS2UUkiDq4cNNzZm3D9vFM5wixXfm3UMOkrZ2rQQUEW3bsjlSjfQYBvlrYpcJqlHGEOC0vXxhRWJtl1LSj37NK0roSKmZX02DtRIo9kFHWarzh2_Cz2ivs54KVjIW4ufAT5Z82MZ5UV-zXQSID8RKqEWFxYkEOOjoE9Mnshu-jyv5b98DP2MMMWAkt4MbZlDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86534c54a.mp4?token=KXbn7yEi08GcpSwfyYBvpOx7Kxhc4tVHIUFF7QOx4DBwrm01JnFEmg7nehNzXXYCvuVjlq018LXUqBzxRqv-egDXe6D7OvmnTG5I_3rizTS7Txi2Vq6qZIbVUXp8LwtlIMc5aFoQJi-aKnIgwmSGyfS2UUkiDq4cNNzZm3D9vFM5wixXfm3UMOkrZ2rQQUEW3bsjlSjfQYBvlrYpcJqlHGEOC0vXxhRWJtl1LSj37NK0roSKmZX02DtRIo9kFHWarzh2_Cz2ivs54KVjIW4ufAT5Z82MZ5UV-zXQSID8RKqEWFxYkEOOjoE9Mnshu-jyv5b98DP2MMMWAkt4MbZlDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: برای عضویت در پیمان مکه دعوتنامه‌ای دریافت نکرده‌ایم اما برای گفت‌وگو با این کشورها دربارهٔ امنیت منطقه پیشنهادهایی مطرح شده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/683876" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e004647.mp4?token=gG34oKx9z8d-YeibADuWrMvVUcW_v-mCb1cY73rQxsgxe1b-aqXivr0AMAfGpkGFdKKAxvxrXF5-P8v-o2NlZEB3DI56HZ6CNI7Mk9bnKtVZoZBJuhyh_IyPMZcl8eLzqiL6qOrZMhxQfk1tH6_G2MgpTQP_s2JCvZvzkoEkKyLpA8dQIEzcdGCJubRKFaeIqL4CpnJN0_Rwq3YuzdJzeMwOWcs--CsPRKrzAnj4uAtfu06s_ArJ49CLlOu1vFr5FffApu4JLw58ntlaV8aY1KiMGassygZd0alzPwxG2gslTpcKfERx-H89tlc8Mka0T7fCmHVI0kz2t7Lat1uvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e004647.mp4?token=gG34oKx9z8d-YeibADuWrMvVUcW_v-mCb1cY73rQxsgxe1b-aqXivr0AMAfGpkGFdKKAxvxrXF5-P8v-o2NlZEB3DI56HZ6CNI7Mk9bnKtVZoZBJuhyh_IyPMZcl8eLzqiL6qOrZMhxQfk1tH6_G2MgpTQP_s2JCvZvzkoEkKyLpA8dQIEzcdGCJubRKFaeIqL4CpnJN0_Rwq3YuzdJzeMwOWcs--CsPRKrzAnj4uAtfu06s_ArJ49CLlOu1vFr5FffApu4JLw58ntlaV8aY1KiMGassygZd0alzPwxG2gslTpcKfERx-H89tlc8Mka0T7fCmHVI0kz2t7Lat1uvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای المیادین به نقل از یک منبع ایرانی: ایران دعوتنامه‌ای برای پیوستن به «توافق مکه» دریافت کرده و این موضوع در حال بررسی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683875" target="_blank">📅 11:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07517ba50b.mp4?token=saMVeGhILMIVI1nwwi7tcYUalRajEdfZW0EgklG0Q3r0dRXfqKKRLoXz3Gj-QdF2N_CSgJYPy2BIi-WsiaiRiv7-BBWXDCDQhZ7DARgvJtDdfwKbZJsMsdvbQDI1K_5zBDORyoxa3xel1963p9SoezoZkxFppX57lbxK1j3CPvGTKthMDhR71-hcHq72BncMz7a0wBLcsJ8A0tAutYE8qEJafW1aE1wus1wqvruwGgo0mRsDnwVfBVqHmbe0INIdgrRhcykHauqFt_3zOGgr4mJayRxsP6WVfTQZThQNZnmy2ssSv9PUB9hrsAlp9Tem_H-HkKLHJtADZ0O67lUVqUtWJbE_5P0Mkv9UZU8x52wdwrCB9IqigiQwDeNTWtABQrIh7i2HLN8VrfNd_Y6Ui20iYHoAP0ttiznsnRwstVYMUhtRUT76aGjoJYE1RWfYsQyGrRhBE_fQlkbP0SRm_AGGMVw8F_s5kgJlAvDi_Vo4uN-QSCMGJHr4u3pNNMu7vnx2oz9LmUqwZPR5Vy9K_JL3oGLDlaBHWvVoH0_wDLilGcwdW6h3RxF-_Sl5IqyFyUr7f28BYs3R3V2er5nVKCXEL6ClMDuYP9sNW8FSqo92Y4YY-v4gtidKfyC6nqlyMUn4f87ZKobg7sfImpE0mBJaRLjFyQaB8H8K6IAnoIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07517ba50b.mp4?token=saMVeGhILMIVI1nwwi7tcYUalRajEdfZW0EgklG0Q3r0dRXfqKKRLoXz3Gj-QdF2N_CSgJYPy2BIi-WsiaiRiv7-BBWXDCDQhZ7DARgvJtDdfwKbZJsMsdvbQDI1K_5zBDORyoxa3xel1963p9SoezoZkxFppX57lbxK1j3CPvGTKthMDhR71-hcHq72BncMz7a0wBLcsJ8A0tAutYE8qEJafW1aE1wus1wqvruwGgo0mRsDnwVfBVqHmbe0INIdgrRhcykHauqFt_3zOGgr4mJayRxsP6WVfTQZThQNZnmy2ssSv9PUB9hrsAlp9Tem_H-HkKLHJtADZ0O67lUVqUtWJbE_5P0Mkv9UZU8x52wdwrCB9IqigiQwDeNTWtABQrIh7i2HLN8VrfNd_Y6Ui20iYHoAP0ttiznsnRwstVYMUhtRUT76aGjoJYE1RWfYsQyGrRhBE_fQlkbP0SRm_AGGMVw8F_s5kgJlAvDi_Vo4uN-QSCMGJHr4u3pNNMu7vnx2oz9LmUqwZPR5Vy9K_JL3oGLDlaBHWvVoH0_wDLilGcwdW6h3RxF-_Sl5IqyFyUr7f28BYs3R3V2er5nVKCXEL6ClMDuYP9sNW8FSqo92Y4YY-v4gtidKfyC6nqlyMUn4f87ZKobg7sfImpE0mBJaRLjFyQaB8H8K6IAnoIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: دلیلی ندارد کشوری از طرف ما نگرانی داشته باشد مگر اینکه پایگاهایشان را در خدمت دشمن قرار داده باشند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/683874" target="_blank">📅 11:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa592d9202.mp4?token=USa1sZvsOP-vkW99gqj8tCPvGP7tRYG88EWyXYmBlVoFwajn0OF47QQhLuGqK8ftNAwFdWoQNCyoLZF-hTGz9zSIqfkZSOm4WUtfUc_jH5CGE0N0h12hSMpNRio5qjEvCDEttantg-PrWZMDRzMjV7vtul34ukl0QCHXk_SZ5xagV2mKKK_DVFoyOnX5Zu_7Ww7RoeUdzq95Q0ygLKDCx7iGWhQfQelMipArUjysvvULYLpsTrIJa1yL4GkrqNZopVwdoArrAQqd8DrHAFw0UkmEk2bfex1RJrmnTb6M4-kOh6IdNf9jLR5zq_F4Xso9vUdB7oW94KOkre21rmb9zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa592d9202.mp4?token=USa1sZvsOP-vkW99gqj8tCPvGP7tRYG88EWyXYmBlVoFwajn0OF47QQhLuGqK8ftNAwFdWoQNCyoLZF-hTGz9zSIqfkZSOm4WUtfUc_jH5CGE0N0h12hSMpNRio5qjEvCDEttantg-PrWZMDRzMjV7vtul34ukl0QCHXk_SZ5xagV2mKKK_DVFoyOnX5Zu_7Ww7RoeUdzq95Q0ygLKDCx7iGWhQfQelMipArUjysvvULYLpsTrIJa1yL4GkrqNZopVwdoArrAQqd8DrHAFw0UkmEk2bfex1RJrmnTb6M4-kOh6IdNf9jLR5zq_F4Xso9vUdB7oW94KOkre21rmb9zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: دلیلی ندارد کشوری از طرف ما نگرانی داشته باشد مگر اینکه پایگاهایشان را در خدمت دشمن قرار داده باشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683873" target="_blank">📅 10:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c354ca7c68.mp4?token=MWgBZniz-YeZ14UJRfEC8N4Qo7eDjcZ4JFoBgAOVzs4ZPDjB1qCTGTvJaYaArDBN6rOX8pAkB0EhRZ8jBh5vllsIrTkyP6f0T8T0hngiljZzO9hLxQFN1QT4OwiROoIhEEskjz2TvyjIvgytY7Nc8LeUrcd0IZOIPoCvNkw0T4dWwbfFS3mE7DJYMMIQvcEM6yi51EbqK_7cvAfMRb9tv8DgC1jQ6kZ0HW0ofCfgjvoxeHGPls_3xPAqflCVLsey5ikBtwN7T7RMesciM0yWVMNMSMee8GwKfdD8qpkDySk8haB0NIbLIPnNWK0pd5k2zTNpAVlOwycHgLhjCr08I6e3TyXCTB9IOYIThsVcRp1jPInpX1x9Y4S_ScOuawng4DRb7w81whKQ8V-AQESMWo8Qsg2CWrLL0S96yB465A14jB9FJ7Y8I0E79DhrB-fKYGS0JTeM7dZ6cQGcuMevSuHXDnXfQ1prg8k5GnUnr0yDX7SZoe2HGxwiYVrxIm74cZxNsxucRkGFgIAyWXT9Ci3xasOoGnAJRFKp5u8TtHxNS27L5Ahe80d0L-OAw8zFjJQhCoYTpdb5J9-k6kIIrBoO3dyLeCXXhrcIORqRLJgcdyYCcN1IJS3FdsdnDfG79wp8HgSbMNiQ6smtzmLkVAaPZhq4Ozj45QOb5KRidQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c354ca7c68.mp4?token=MWgBZniz-YeZ14UJRfEC8N4Qo7eDjcZ4JFoBgAOVzs4ZPDjB1qCTGTvJaYaArDBN6rOX8pAkB0EhRZ8jBh5vllsIrTkyP6f0T8T0hngiljZzO9hLxQFN1QT4OwiROoIhEEskjz2TvyjIvgytY7Nc8LeUrcd0IZOIPoCvNkw0T4dWwbfFS3mE7DJYMMIQvcEM6yi51EbqK_7cvAfMRb9tv8DgC1jQ6kZ0HW0ofCfgjvoxeHGPls_3xPAqflCVLsey5ikBtwN7T7RMesciM0yWVMNMSMee8GwKfdD8qpkDySk8haB0NIbLIPnNWK0pd5k2zTNpAVlOwycHgLhjCr08I6e3TyXCTB9IOYIThsVcRp1jPInpX1x9Y4S_ScOuawng4DRb7w81whKQ8V-AQESMWo8Qsg2CWrLL0S96yB465A14jB9FJ7Y8I0E79DhrB-fKYGS0JTeM7dZ6cQGcuMevSuHXDnXfQ1prg8k5GnUnr0yDX7SZoe2HGxwiYVrxIm74cZxNsxucRkGFgIAyWXT9Ci3xasOoGnAJRFKp5u8TtHxNS27L5Ahe80d0L-OAw8zFjJQhCoYTpdb5J9-k6kIIrBoO3dyLeCXXhrcIORqRLJgcdyYCcN1IJS3FdsdnDfG79wp8HgSbMNiQ6smtzmLkVAaPZhq4Ozj45QOb5KRidQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلسه‌ای که رهبر انقلاب استاد راهنما بودند
🔹
این فیلم مربوط به دوران پیش از زعامت رهبری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/683872" target="_blank">📅 10:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXTECrbQfzbmfDV5Azv7q8PIfiw-064SwR3Bu8Jk-XhlRW2-R76QE99oazjxuA2t14xV4UEe_Eo02XLyaRcdNTyN8IlFjcmkI521uhCTsh78crd6EVvD5hKXGC_OLO9QN-HFiV3oz6F7kEqfGTTqodXGEih4ZMmY5wa8tC0yh9C0pAu6q7zakx1rbq5CvGW-hdhDNXmPTu_K8QcciT6kEUiuJ_kfXLslhCsJ3fB0DjfHF6x7_B980tk28N4mbW8FQAQrUAJJdil7v7olOcCryHHt84zFUlRO-j8brgKEqy1vHKw15hbRZhbmNQsVvM5kr4eAJEOJznJm473bAwlOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683871" target="_blank">📅 10:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
کپلر: در دو روز گذشته تنها ۱۷ کشتی از تنگه هرمز عبور کرده‌اند</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/683870" target="_blank">📅 10:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81555e7b8.mp4?token=s0dDgS6ISfHphHNnyd4BsyVm1SUBLQngWqZvgGuO9ayaD_PlSyO_53R1-qFqwxdLexWdCDIcnK-l-H02jlr5vrUy8l0iZbUOVBgsADYm9x4jF-fjJQPnCGH6Coko0f5uejYRZzIBuG0p-AQG2P1QjV59qCa_7F07ugXBN80m8ZxVOK6UAJtFM23CexcuApd4cauCn1tUBGtn9rfSim2zEpgkREGVIOWRFMyAOPjJ8ktimAAYJuQkA1cTdIAm9MON8DylOAIj8-kkTs6EZKkq5YDI4ZQv9ACU01n65FXRJQnhjZo0qzUg-TGM_R4AQ-fBh0E-30ZhzPZj3C2jCIZxpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81555e7b8.mp4?token=s0dDgS6ISfHphHNnyd4BsyVm1SUBLQngWqZvgGuO9ayaD_PlSyO_53R1-qFqwxdLexWdCDIcnK-l-H02jlr5vrUy8l0iZbUOVBgsADYm9x4jF-fjJQPnCGH6Coko0f5uejYRZzIBuG0p-AQG2P1QjV59qCa_7F07ugXBN80m8ZxVOK6UAJtFM23CexcuApd4cauCn1tUBGtn9rfSim2zEpgkREGVIOWRFMyAOPjJ8ktimAAYJuQkA1cTdIAm9MON8DylOAIj8-kkTs6EZKkq5YDI4ZQv9ACU01n65FXRJQnhjZo0qzUg-TGM_R4AQ-fBh0E-30ZhzPZj3C2jCIZxpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از وضعیت عجیب ترافیک تهران و موتورسوارهایش!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683869" target="_blank">📅 10:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImvIZ0LpeQNG66FrmLEXfHyZeVtuQZlk2c_O5E-f4impzRR__NDvkDvuWpt5qcRcvd25iTekY9Stq0oHMIwICwmxPmvRipfw0tdXxnxL-xjRbSA8zIYKFYmoROcthv4CNXAZ012HASm2sECvadSHldpMEFah_trb6ni0VVNlrq1hPplLrwnv-aaGhhhESUfT05_WzfSVna3vZbgUO5XoRDbdNQ3YDi_kQMDtweoye50ODV2J1Dc4vKdkdBxWI1J3Nd8mzE0LmWI8JvhhyfyTIFg-NX7oRyWX-dxqC3k-feO61ntIqpST2HJFu7IVb2aaffT7NQnZk5DpvZ9qWt2AQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌ روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌ صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683868" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b543d8c4df.mp4?token=Z7dErFR349IruQbjfjnARKLq01xbK9UMSYpr4h5zSAn_25MOhnsq9TAhunwmy9Qbee-p2PwZPFUestRQHKyB3SjIx1w9nTXn5gCxE_CVNQ1UkT_TybSUPpkEcauVw21ldpc2n7XPw7zg3nAsxcOFa9tVGETt_SCBYJl4UV9lrCS9Bd49sp_C_vQZGWDF8Ljc_dOrQAxAsDDhKInAi7RM5u7QMxwsXwBk4NkjqMvIqqXvNCrx5P3Hj1mb0em0xuki3kEqkaj0UOwmgGmQniLYm7eaDJgdwQcPLxfsKhBCCBdmxJVEj1T_7UvtSx1kaKyq92y2zHoWhxeBc2EIrB-zGVZRvfnTFQROuQ3uClf4gVdST8JEvsJAWL2BKaeh_rsc3GAl0XfG1VdWPzQ62G2hQfZ9T0pHBy-AS8t4TER8tuPOI0crl9h3atIlyQCqB7pAxEbWMh9eDEta1qmUloS-fCsEjIKjcH0dRthpVBFU4pCDnL3gd_yk0ST63ZskBYDF3lAwmMUDJGEfxOljclIh44442JcLEietAXweuYpDbZAFoy07d4CSrIj4jDOEFmwo-yyG-xFOApBS-uK41T1V20RbCXeETKWUinqCMMi66wY4atvujLTPuBsnbPC0H9b37mHlBw9JHesVmZvevDI-OEtJSpYYhpcyix5ZpKUstSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b543d8c4df.mp4?token=Z7dErFR349IruQbjfjnARKLq01xbK9UMSYpr4h5zSAn_25MOhnsq9TAhunwmy9Qbee-p2PwZPFUestRQHKyB3SjIx1w9nTXn5gCxE_CVNQ1UkT_TybSUPpkEcauVw21ldpc2n7XPw7zg3nAsxcOFa9tVGETt_SCBYJl4UV9lrCS9Bd49sp_C_vQZGWDF8Ljc_dOrQAxAsDDhKInAi7RM5u7QMxwsXwBk4NkjqMvIqqXvNCrx5P3Hj1mb0em0xuki3kEqkaj0UOwmgGmQniLYm7eaDJgdwQcPLxfsKhBCCBdmxJVEj1T_7UvtSx1kaKyq92y2zHoWhxeBc2EIrB-zGVZRvfnTFQROuQ3uClf4gVdST8JEvsJAWL2BKaeh_rsc3GAl0XfG1VdWPzQ62G2hQfZ9T0pHBy-AS8t4TER8tuPOI0crl9h3atIlyQCqB7pAxEbWMh9eDEta1qmUloS-fCsEjIKjcH0dRthpVBFU4pCDnL3gd_yk0ST63ZskBYDF3lAwmMUDJGEfxOljclIh44442JcLEietAXweuYpDbZAFoy07d4CSrIj4jDOEFmwo-yyG-xFOApBS-uK41T1V20RbCXeETKWUinqCMMi66wY4atvujLTPuBsnbPC0H9b37mHlBw9JHesVmZvevDI-OEtJSpYYhpcyix5ZpKUstSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار پاسگاه نیروهای پاکستانی توسط گروه تجزیه‌طلب بلوچ
🔹
گروه تجزیه‌طلب «ارتش آزادی‌بخش بلوچ» با انتشار ویدئویی از انفجار یک پاسگاه نیروهای مرزی ارتش پاکستان در منطقه قلات در ایالت بلوچستان خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683866" target="_blank">📅 10:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیر عامل توانیر: ۳۰۰ هزار ماینر غیرمجاز شناسایی شد
🔹
رئیس سازمان هواپیمایی کشوری: ایران در تعمیر و نگهداری هواپیما خودکفا شد
🔹
محکومیت بیش از ۳۱ میلیارد ریالی مدیرعامل یک شرکت ارزی در گیلان
🔹
پلیس راهور: بیش از ۵۳ درصد تصادفات در تاریکی هوا اتفاق می‌افتد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/683865" target="_blank">📅 10:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a634c77154.mp4?token=NTBBjhbezU9wS2CuPD9HKcvvSfrdCAFHv8nv03xkZFfwisrQXkZskNczpym0E9YaD0CSdHoUI30P3FF9WtmhRxAEKxaLtFElzfjx3h2SNLy4arGOe5jfEJQdh88URrrvqhvG9uVLG_Eon4Wr9uSuHRH1k_ljHZsOD2FmIgGWdzHYPWaKov6KIdq8XNIwfT7p_bGgAxNBdQTHNu4f01iw6PMotZERnJMkFdUv3ynGP9rhljEhbP3Xmznz3j5urIctiu1Xw97khzdaltJ2-z74ux1z7LxGhyKFvFLEkGKAIJNq4IAYeRVOlgHmyb41UNFMicQTa2Zi2yQwVPxlD0ryhGrrr-Om26HkMUmHUg4anCOXfSmN7UMTdR4eWjb42ebViAiTFWVDiDazKfsn5UusKJEsg4mfAxGAJ9aeT07CQSOGEE4uo2DmuTPZMomYF0XUIXwXPm74Q8Dc0QakNSJajOvdz_ts2G9mfhBVXX5tsm6ufvfgRBJjLlN6KPVNX4cGPNL8WpNlRoiIg5MKy4A7C-2bME4q-CfJMNKFBU8-D-Xgse6K_cyc28mQeZeHT9IbdGnaLC0D-CTLLSurLPKvBW2BMF8iw7GzrWeYxwjQJaQxX7agivS-C2ipNxSR5l8xDmgj5zOoD5kJ_PLPBvGmhCYOy19uIHp2CTGSY2D5jFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a634c77154.mp4?token=NTBBjhbezU9wS2CuPD9HKcvvSfrdCAFHv8nv03xkZFfwisrQXkZskNczpym0E9YaD0CSdHoUI30P3FF9WtmhRxAEKxaLtFElzfjx3h2SNLy4arGOe5jfEJQdh88URrrvqhvG9uVLG_Eon4Wr9uSuHRH1k_ljHZsOD2FmIgGWdzHYPWaKov6KIdq8XNIwfT7p_bGgAxNBdQTHNu4f01iw6PMotZERnJMkFdUv3ynGP9rhljEhbP3Xmznz3j5urIctiu1Xw97khzdaltJ2-z74ux1z7LxGhyKFvFLEkGKAIJNq4IAYeRVOlgHmyb41UNFMicQTa2Zi2yQwVPxlD0ryhGrrr-Om26HkMUmHUg4anCOXfSmN7UMTdR4eWjb42ebViAiTFWVDiDazKfsn5UusKJEsg4mfAxGAJ9aeT07CQSOGEE4uo2DmuTPZMomYF0XUIXwXPm74Q8Dc0QakNSJajOvdz_ts2G9mfhBVXX5tsm6ufvfgRBJjLlN6KPVNX4cGPNL8WpNlRoiIg5MKy4A7C-2bME4q-CfJMNKFBU8-D-Xgse6K_cyc28mQeZeHT9IbdGnaLC0D-CTLLSurLPKvBW2BMF8iw7GzrWeYxwjQJaQxX7agivS-C2ipNxSR5l8xDmgj5zOoD5kJ_PLPBvGmhCYOy19uIHp2CTGSY2D5jFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوکی شکلاتی بروانی رو در  کمترین زمان ممکن درستش کن
🍪
مواد لازم :
🔹
کره ذوب شده ۱۰۰ گرم
🔹
تخم مرغ ۱ عدد
🔹
پودر قند ۲/۳ پیمانه
🔹
وانیل ۱ قاشق چای‌خوری
🔹
آرد ۲ پیمانه
🔹
بکینگ پودر ۱قاشق مربا خوری
🔹
پودر کاکائو ۳ قاشق غذاخوری
🔹
لایه شکلاتی ۵۰ گرم شکلات سکه ای شیری…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/683864" target="_blank">📅 10:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CminvTVBWkWpCv9Eo3_jOw_cp-uNtqIchEVjkLiCpyMD353OYwrn0jlbSm-C22mDcEC1LEnODHlTMA2-3wNe-wUodZoU22FW6v04me3cClUhO2_QXkc96ZYIYBzc1DZeBKmGTTVt2tzbONFt4A28jHG1152VA_-PCBvolpbSHFHaFVy706zf9edmmxhzrM-naD9eeFOgfKIvZWJjWedxYNGUeOWAp2CrKkQfQbzXX9V_-M7tpJFaoeW2iGX6RZZwVNZ9uPe6pZcc2psbMEoA3XVuITnlb7rVxlQjZawyS1RJG6X6wLsI9SqtN9HvXzcIT7XhpJTEgMGeTRBJxCFLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت معاملات آتی طلا برای اولین بار از تاریخ ۱۴ مه، از مرز ۴۷۰۰ دلار به ازای هر اونس عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683863" target="_blank">📅 10:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quosBDr7ZP83oTwVpXX7lL4V36TZjXkp_5yp7ck4QQkD0IZQN4eBgqtLVIuLdY4v4O4mXjwGVQK5BUV_0jz7sOdBLDp_vxokMXpjSKMYA7lCX8nviRnJGfxwlP6MZYdgVSWMyDvG9cioBvUZUstT-5Rap73PywSRXWKvVRVkrmWIHJK6NftYRUVdA7vSN7dz0J4iYut5w9s-ZRa_--cuPdvcLpOccB1a9kxbSmkcTKpxAQGAIByAZe4zlJ5Qj_yee--VFa2bqx0JYnV4indR-ghOTnivGSQMtN3ixCm13y0ehZKqttnkdB6zjA9hoNUsMEnfyF6bevyTesGYt8jVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره‌شکنی کشتی ایرانی در «روز دی»
🔹
طبق گزارش پایگاه سوپربرو، یک کشتی کانتینری منتسب به ایران توانست با عبور از خط محاصرهٔ آمریکا در تنگهٔ هرمز وارد آب‌های ایران شود.
🔹
این درحالی‌ست که ساعاتی پیش وزیر خزانه‌داری آمریکا در یادداشتی از آغاز فشار اقتصادی جدید علیه ایران موسوم به روز دی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683862" target="_blank">📅 10:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سود ۴.۵ میلیارد تومانی وام جدید مسکن/ قسط ماهانه ۵۱.۵ میلیون
🔹
با افزایش سقف جدید وام مسکن، سود این وام به همراه تسهیلات جعاله در تهران حدود ۴.۵ میلیارد تومان است.
🔹
مبلغ قسط وام ۲ میلیارد تومانی در بازپرداخت ۱۲ ساله حدود ۴۰ میلیون و ۲۷۵ هزار تومان است. کل سود این تسهیلات حدود ۳.۸ میلیارد تومان و کل بازپرداخت وام‌گیرنده در ماه ۱۲ سال دوازدهم حدود ۵.۸ میلیارد تومان خواهد بود.
🔹
در بازپرداخت وام تعمیر ۴۰۰ میلیون تومانی قسط ماهانه حدود ۱۱ میلیون و ۱۶۰ هزار تومان و سود آن حدود ۲۷۰ میلیون تومان است. کل بازپرداخت وام تعمیر با احتساب سود آن حدود ۶۷۰ میلیون تومان خواهد بود.
🔹
به این ترتیب سود وام ۲ میلیارد و ۴۰۰ میلیون تومانی خرید یا ساخت مسکن حدود ۴ میلیارد و ۴۷۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683861" target="_blank">📅 10:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ایران حق بیماران پروانه‌ای را از آمریکا گرفت
رئیس شعبهٔ ۵۵ دادگاه حقوقی بین‌الملل تهران از اختصاص بخشی از اموال توقیف‌ شدهٔ آمریکا به بیماران ایرانی خبر داد و گفت:
🔹
براساس حکم صادرشده، ۷۷۱ بیمار که علیه دولت آمریکا دادخواهی کرده‌اند، در اولویت دریافت خسارت قرار دارند.
🔹
در روند اجرای حکم، یک نفتکش آمریکایی در سال ۱۴۰۲ توقیف و محمولهٔ نفت آن براساس تشریفات قانونی به فروش رسیده و وجوه حاصل از فروش نفت هم به حساب قوه‌قضائیه واریز شده و اکنون دستور توزیع آن میان دادخواهان صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683860" target="_blank">📅 09:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2434f23bef.mp4?token=Xs2X4U39pTWE4lZ8C4ld12BxkLFxeSD6pPwVFLrDR5vMevyZyQE7WGFIBeGg3xEiesepdmgnkwl4E1TaZ3nu6wH6zyCPx7yV8Q_Xh9Z68V_FMaqEn2RtwUaWzWx8UXxuh5NgHTkBUG2xqMCJym-4d58OhselbqMV6B-Lolf8LlloMWCk0XRLqJ4QyNCIKGiYw6ItzjmclTYXTI54X2tzkCUjK_vnYOgcsf08wWnveUNYzoDIe_NzzqeZRXMQQhccJWYQYTaCk2ipQeANXMGV9sL5yBLuDUO-YjSy_oG5-ea6rQOJbX3ajLmFY2sdofAGyD3u1QjF6NVdTz0aWMbTdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2434f23bef.mp4?token=Xs2X4U39pTWE4lZ8C4ld12BxkLFxeSD6pPwVFLrDR5vMevyZyQE7WGFIBeGg3xEiesepdmgnkwl4E1TaZ3nu6wH6zyCPx7yV8Q_Xh9Z68V_FMaqEn2RtwUaWzWx8UXxuh5NgHTkBUG2xqMCJym-4d58OhselbqMV6B-Lolf8LlloMWCk0XRLqJ4QyNCIKGiYw6ItzjmclTYXTI54X2tzkCUjK_vnYOgcsf08wWnveUNYzoDIe_NzzqeZRXMQQhccJWYQYTaCk2ipQeANXMGV9sL5yBLuDUO-YjSy_oG5-ea6rQOJbX3ajLmFY2sdofAGyD3u1QjF6NVdTz0aWMbTdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری مطرح آمریکایی: واشنگتن حتی نتوانست از خودش دفاع کند؛ چگونه قرار است از کشورهای خلیج فارس محافظت کند؟!
🔹
به محض آغاز جنگ، ایران همه آن‌ها را در کشورهای مختلف هدف قرار داد. ما به دولت‌های خلیج فارس نشان دادیم که نه قرار است از آن‌ها محافظت کنیم و نه حتی توان چنین کاری را داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683859" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13db53a616.mp4?token=MIKa1OAT3KRhrpZrYVfrn9x7qJkXNbTnLCHK5ur5tq3JIpMYL4ZWYPbSCuCTphTapnsxE6xyzcvw3V6Ws9SGeRJaUzXdegYfqZNZ2b9qjX69VS78U2BwREvWf7rYGI6HlN-GUGMbh3T4PiQCezCoIKqMqcyQctTOolD2Y-n9_EQEkLjwkj1TjHJAo4dTpo_CIEwHy7LBsQyiai3crop2A5hlUwZ9cobvZUYpb4D27KkJaCwZBJYaEJtBwPv5mGU7m1EGYItbdoXhZJ7paUD7X4ngJ_mGuwtjhsbJNHizLsGZxTB8wiNXaQPGZC9B5KoFOm5j71J-jLEqUtE_jG3Fkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13db53a616.mp4?token=MIKa1OAT3KRhrpZrYVfrn9x7qJkXNbTnLCHK5ur5tq3JIpMYL4ZWYPbSCuCTphTapnsxE6xyzcvw3V6Ws9SGeRJaUzXdegYfqZNZ2b9qjX69VS78U2BwREvWf7rYGI6HlN-GUGMbh3T4PiQCezCoIKqMqcyQctTOolD2Y-n9_EQEkLjwkj1TjHJAo4dTpo_CIEwHy7LBsQyiai3crop2A5hlUwZ9cobvZUYpb4D27KkJaCwZBJYaEJtBwPv5mGU7m1EGYItbdoXhZJ7paUD7X4ngJ_mGuwtjhsbJNHizLsGZxTB8wiNXaQPGZC9B5KoFOm5j71J-jLEqUtE_jG3Fkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین در حال آزمایش «ربات‌های پلیس» برای گشت‌زنی و کنترل خیابان‌هاست
🔹
در شنژن و هانگژو، این ربات‌ها با دوربین، رادار و هوش مصنوعی می‌توانند با لباس عملیات ویژه برای شناسایی موارد مشکوک در خیابان ها تردد کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/683858" target="_blank">📅 09:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29000cf9f.mp4?token=hev_VG-cd-eSFaQH3w5uqx5t15gQXjAGt9oNbVvfrFAUsDGyI9zQaZUyL2RuMLFOJq2vuCq5V67n436kX_2HWaQ0ltMhpH27x9jMXGfeaTkwDryoHtINXnT2WyP3TvyAPZoPaT8xiVsX7QS0G4qrKUZy14YscwONaVCTGIDZD-te3nsoGqvPkvyl_a17f6S6hEjuEfzwKKF-kbYsrlHEkRIp4KlDEWTwkzGVE36KJ0KWFfyo2pD8Fu5PQ8NAlUtY6DPVSGjr3_IvM0_bN3GpHnMYgnqnZSNmhY1t2sni4Xg0gnQyocvGi6NCPy34jjURrusgEW4MNZD6yn83nrgMe3bkWcMJRaM4JKkDSlenw9Yad7c-mfIWlxSTBoltguu-QN6qNF0d1dWX5RAeOPrpXvdzsyrv94I4dtJknEPwoE_PxKha6GW45Fz325tkcQoKWhPPePecw5-hbtatWd0qP5mhRlr-kQRTV3Ls4-ErWYDbj7S5R4C3e5cvn7L_Z5Wsr2akYc037CpmdR-cEqCz_SGPFYG7V69k3pkCCAS4av4PnL2pVXqqaDh0PYXNpQuNcZHmGvczwsbWlgDpy8O1jU277ZX3A7DYDQcTa1HSzPUgEwEZFpP7JqBl_Kv4y2YWYG1ClgP_Ug59etMkETpxQAHTNYCh4ilPBWVZx5KSs28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29000cf9f.mp4?token=hev_VG-cd-eSFaQH3w5uqx5t15gQXjAGt9oNbVvfrFAUsDGyI9zQaZUyL2RuMLFOJq2vuCq5V67n436kX_2HWaQ0ltMhpH27x9jMXGfeaTkwDryoHtINXnT2WyP3TvyAPZoPaT8xiVsX7QS0G4qrKUZy14YscwONaVCTGIDZD-te3nsoGqvPkvyl_a17f6S6hEjuEfzwKKF-kbYsrlHEkRIp4KlDEWTwkzGVE36KJ0KWFfyo2pD8Fu5PQ8NAlUtY6DPVSGjr3_IvM0_bN3GpHnMYgnqnZSNmhY1t2sni4Xg0gnQyocvGi6NCPy34jjURrusgEW4MNZD6yn83nrgMe3bkWcMJRaM4JKkDSlenw9Yad7c-mfIWlxSTBoltguu-QN6qNF0d1dWX5RAeOPrpXvdzsyrv94I4dtJknEPwoE_PxKha6GW45Fz325tkcQoKWhPPePecw5-hbtatWd0qP5mhRlr-kQRTV3Ls4-ErWYDbj7S5R4C3e5cvn7L_Z5Wsr2akYc037CpmdR-cEqCz_SGPFYG7V69k3pkCCAS4av4PnL2pVXqqaDh0PYXNpQuNcZHmGvczwsbWlgDpy8O1jU277ZX3A7DYDQcTa1HSzPUgEwEZFpP7JqBl_Kv4y2YWYG1ClgP_Ug59etMkETpxQAHTNYCh4ilPBWVZx5KSs28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: کاهش سهمیه‌های بنزین قطعی است/ کسی بیش از سهمیه بخواهد بنزین خریداری کند قیمت بالاتری خواهد داشت اما هنوز این قیمت تعیین نشده
🔹
تفاوت قیمت بنزین با کشورهای اطراف زیاد شده است. تردیدی نیست که باید در وضعیت بنزین مداخله کنیم.
🔹
وقتی تولید در نتیجه جنگ کاهش پیدا کرده باید مصرف کاهش پیدا کند. در مورد سیاست‌های قیمتی تردیدهایی وجود دارد و هنوز گزینه واحدی را نمی‌توانم اعلام کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683857" target="_blank">📅 09:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
واکنش سخنگوی سپاه به ادعای آمریکا درباره امکان عبور نفتکش‌ها از تنگه هرمز
سردار محبی:
🔹
رصدها از طریق ماهواره‌هایی که آمریکایی‌ها تصور می‌کنند، انجام نمی‌شود؛ روش‌های دیگری وجود دارد که شاید طرف مقابل هنوز قادر به تشخیص آن‌ها باشد
🔹
اگر ایران چشم بینا برای رصد تحرکات دریایی نداشت، چگونه می‌توانست نقاط حساس شناور‌ها را مورد اصابت قرار دهد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683856" target="_blank">📅 09:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر کشور: آماده‌ برگزاری تمام‌الکترونیک انتخابات در موعد مقرر هستیم
🔹
شاخص کل بورس تهران با افت ۲۷ هزار واحدی به سطح ۶ میلیون و ۴۲ هزار واحد کاهش یافت
🔹
گسترش تجاوزات مرزی رژیم صهیونیستی به خاک سوریه با پیاده‌نظام و پهپاد
🔹
حمله توپخانه‌ای رژیم سعودی به روستاهای مرزی در صعده یمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/683855" target="_blank">📅 09:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbZJZ5O1XgCBYxa_ar6AHxqfgNwPyrcOyQ3hJkb3daIgrtv1CcwlPPUehe4Z7F3RZCZlWPeqbMjPkwymGrCSj5bhUm6_YgZQ2TvYsm22xmYgoRYldVLczO7a3zGPBNkM5EpYj_uM1ZQSszGC0w7TBCbNV_pzrnP_MHJcuqVkFFlZFgHg6oQDD-jdaIv6K_9cHDF96KP2dTdQtj0iK8d33yxvreipUXl8Jq7XmQRCUVEpcOrdSOvSXsIcV6q_ONOXEW9laPoWE-XgQGcP5CWl6HtcAiOcd9iNC18hQwqHL6XFTfvd-XO0GayC1DVevCDJQAXk8lsV5yb_nw5fV_JtMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقتصاددان آمریکایی:
تحریم‌های اقتصادی بی‌سابقه ترامپ علیه ایران نه‌تنها نتیجه‌ای نخواهد داشت، بلکه نتیجه معکوس خواهد داد
پیتر شیف، اقتصاددان و مفسر مالی آمریکایی:
🔹
کشورهای دیگر این محدودیت‌ها را نادیده خواهند گرفت و از آن‌ها تبعیت نخواهند کرد. ترامپ هم نخواهد توانست تحریم‌های تلافی‌جویانه‌ای را که تهدید کرده، عملی کند. علاوه‌بر این، ارزش دلار کاهش پیدا خواهد کرد و قیمت مواد غذایی و انرژی افزایش خواهد یافت.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/683854" target="_blank">📅 09:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051fc127c8.mp4?token=AkVzqjXJownO07uD08EPQQhIHAl2atcztnVWrl0vV8jt5dLRyFfyL2xisTAT7SAw9WQsFWaqKYqy4MOu0na9sxjxgwOw_3XTpcj1jwg9jbuTibVDVGRmu51aMrHBTM-1FtF8iI29XxJROTAcB9CKdfhSWwxbnfox5awZm6NeJV63yCaPbqr-EnSf7wyZfGs_JvfBTGlqWh679ANdJbG-KZ_8DlrsfsiSrKE3d4-Wtlsolz7OVNl8fa4IS6KpB03arTw9rFhKjztRFHd_0__7Vvz060G7TSUJ5Tg4cnrPpaQMLAi0lusRrTlG3mVRRgIKzTN8XGgYHWxZ30N0_R1OIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051fc127c8.mp4?token=AkVzqjXJownO07uD08EPQQhIHAl2atcztnVWrl0vV8jt5dLRyFfyL2xisTAT7SAw9WQsFWaqKYqy4MOu0na9sxjxgwOw_3XTpcj1jwg9jbuTibVDVGRmu51aMrHBTM-1FtF8iI29XxJROTAcB9CKdfhSWwxbnfox5awZm6NeJV63yCaPbqr-EnSf7wyZfGs_JvfBTGlqWh679ANdJbG-KZ_8DlrsfsiSrKE3d4-Wtlsolz7OVNl8fa4IS6KpB03arTw9rFhKjztRFHd_0__7Vvz060G7TSUJ5Tg4cnrPpaQMLAi0lusRrTlG3mVRRgIKzTN8XGgYHWxZ30N0_R1OIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزوهای دشمنان به گور خواهد رفت
سیداحمد خمینی:
🔹
ما را با موشک نمی‌توان از بین برد چون ما فرد نیستیم، تفکریم.
🔹
امروز همگی پشت سر رهبر معظم انقلاب حرکت می‌کنیم و آرزوهای دشمنان نیز به گور خواهد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/683853" target="_blank">📅 09:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
عاصم منیر راهی ایران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان، برای دیدار با مقام‌های بلندپایه ایران، به همراه
وزیر کشور پاکستان
، اسلام‌آباد را به مقصد تهران ترک کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683852" target="_blank">📅 09:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRasa_factory</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f718582c3b.mp4?token=E_s8YcTyA-xjUGbMgcebDw1EhaonWB7iwe7U_pEjQZZEmfxSUrB5APYB8Hyk5JQIVAmhCq5SnKiBy3MzpIfI-3kT9qgxrcDvr2OT6pLj9UnjAZnx3n4ujMpst678hSeNZY7D1Yq1RWJfVbU8IrhQb7K40MB9KKtW7agwfptFAXHXZmuOb5pDGrj1J7arctejHrD4nO6xkPGF8hbsDJ9U8PtS-A_UWZGN7lPdO-YgXFtfuOla_H8F2FKcJdlvD9JBqwFtIpi12pvsxIq4h4AZa5uw6YqtL64N6ESVQC_Ur9K5tr49jkhgkNEXcT_krm8tZ2022vZIcMaVaGv0xj8fVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f718582c3b.mp4?token=E_s8YcTyA-xjUGbMgcebDw1EhaonWB7iwe7U_pEjQZZEmfxSUrB5APYB8Hyk5JQIVAmhCq5SnKiBy3MzpIfI-3kT9qgxrcDvr2OT6pLj9UnjAZnx3n4ujMpst678hSeNZY7D1Yq1RWJfVbU8IrhQb7K40MB9KKtW7agwfptFAXHXZmuOb5pDGrj1J7arctejHrD4nO6xkPGF8hbsDJ9U8PtS-A_UWZGN7lPdO-YgXFtfuOla_H8F2FKcJdlvD9JBqwFtIpi12pvsxIq4h4AZa5uw6YqtL64N6ESVQC_Ur9K5tr49jkhgkNEXcT_krm8tZ2022vZIcMaVaGv0xj8fVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فـروش ویـژه درب‌های داخلی
(ضد آب
💧
ضد بخار
🌫️
خود اطفا
🔥
)
💰
فـقط بـا 4 مــیلیون تـومان
💰
راسا‌دُر با ۲۵ سال گارانتی تعویض
✅
منازل،هتل‌ها،سازمان‌ها،بیمارستان‌ها و...
🔻
برای اطلاعات بیشتر تماس بگیرید
05136666789
📞
09153068010
🔻
لینک شبکه‌های اجتماعی راسا دُر:
لینک اینستاگرام
▿ ▾ ▿
لینک تلگرام
راسا‌دُر تنها تولیدکننده درب‌های پلی‌وود
در شرق کشور و مشهد مقدس
@rasa_factory
|
گروه کارخانجات راسا</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/683851" target="_blank">📅 09:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVPe7ALiwCFENh_PhBOMmoSlFth861rMki-gYKsqlMtr56eGpDMFGebioWkT9739eNhtYkrJ-fJDx_ZhWT4PqaAgW-0CLqy2-To6FAhMjtMZgU2UTlu88aDmPkmGVeRay62ZdiCsN67fBsX8dM0DJgyUk-DnEAdaU-_8_JXzMRxoPPbNEJQIUp8A-qGcSN5k3yD3b2JbG_8t2e1VXxKLapbveVifHOQSu4ws_xqUKiraCA1HN1al8LXbOzGQ1waxyY6PZBsYVNzoWpmWDfxnLKHO5AddkSv5yV3PV8MHUMx8lN76kH1vyEMSMQnFLxVxZsnCeGdWYrRqttN-38Mm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت خام آمریکا تنها برای ۴۱ روز دیگر باقی مانده است که پایین‌ترین سطح در نیم قرن اخیر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/683850" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
وزارت دفاع روسیه از حمله به یک کشتی در دریای سیاه خبر داد
🔹
اینترفاکس به نقل از وزارت دفاع روسیه گزارش داد: نیروهای این کشور به یک فروند کشتی باری در دریای سیاه حمله کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683849" target="_blank">📅 08:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تورهای گردشگری لاکچری و گران قیمت در طبیعت، خیانت به محیط زیست است/ مسئله اصلی «لاکچری بودن» تورها نیست
همشهری:
🔹
تصاویر و ویدئوهای منتشرشده در فضای مجازی از برخی تورهای فوق‌ لاکچری طبیعت‌گردی، از انتقال چنین تجهیزاتی به دل طبیعت حکایت دارد؛ تورهایی که گاه با عنوان «اکوتوریسم» یا «گردشگری سبز» تبلیغ می‌شوند اما حضورشان می‌تواند با تخریب پوشش گیاهی و خاک، ایجاد مزاحمت برای حیات‌وحش، افزایش خطر آتش‌سوزی و تولید پسماند همراه باشد.
🔹
رحیم یعقوب‌پور، استاد دانشگاه و کارشناس گردشگری در این رابطه می‌گوید ممکن است تعداد افرادی که توانایی یا تمایل به تجربه این نوع گردشگری را دارند بسیار کم باشد اما آثار مخرب فعالیت یک نفر می‌تواند به اندازه آثار منفی تعداد بسیار بیشتری از گردشگران باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683848" target="_blank">📅 08:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/289ce816c9.mp4?token=r4cPe8rhIotxmfq2hpoF2RN1E6jsN052fT6tW7Aw1HbKnB16OVfqFDI0oK80FGptAdAMizRo0f3I91_WAmSZKe-r-vMGVD-EVhTGJTX8w3YEmq9XZaZmYn290FoWj0Io6xLLV1KF9GwqOmjBcoxrb29TD026StDYx4JrPDLm5VQG0Z6iaz0jbWW512iO0JISj8OHruCU5euUUYjW1zo4f3lX2iD8mtBdZLJ9oCdRrGuGcK6Ebx7L0snjZoINV6iz9LGHacVHA8fPzk9Eatsn1M3By8NaxfGr4Tm1vX8OXJYg4WHwZVyCa_C_S2Tl9esh8rcmJBZ6EqfULp-LLFUxxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/289ce816c9.mp4?token=r4cPe8rhIotxmfq2hpoF2RN1E6jsN052fT6tW7Aw1HbKnB16OVfqFDI0oK80FGptAdAMizRo0f3I91_WAmSZKe-r-vMGVD-EVhTGJTX8w3YEmq9XZaZmYn290FoWj0Io6xLLV1KF9GwqOmjBcoxrb29TD026StDYx4JrPDLm5VQG0Z6iaz0jbWW512iO0JISj8OHruCU5euUUYjW1zo4f3lX2iD8mtBdZLJ9oCdRrGuGcK6Ebx7L0snjZoINV6iz9LGHacVHA8fPzk9Eatsn1M3By8NaxfGr4Tm1vX8OXJYg4WHwZVyCa_C_S2Tl9esh8rcmJBZ6EqfULp-LLFUxxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بگومگو ترامپ و ملانیا در حاشیه مسابقات رالی
🔹
ویدیویی از گفتگوی ترامپ و ملانیا منتشر شده که ابتدا معمولی به نظر می‌رسد، اما رفته‌رفته تبدیل به بگومگو می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/683847" target="_blank">📅 08:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رئیس پلیس امنیت اقتصاد فراجا: مردم برای خرید طلا با سکوهای دارای مجوز رسمی و قانونی معامله کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/683846" target="_blank">📅 08:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مهلت ثبت‌نام آزمون دکتری تخصصی علوم پزشکی ۱۴۰۵،
امروز
به پایان می‌رسد
🔹
هواشناسی: در بیشتر مناطق کشور امروز هوا گرم خواهد بود.
🔹
معاون وزیر خارجه روسیه: مسکو در صورت دریافت درخواست، آماده است برای توقف حملات علیه ایران میانجیگری کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/683845" target="_blank">📅 08:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
گزارش واشنگتن‌پست از افزایش مشکلات سلامتی ترامپ
واشنگتن‌پست:
🔹
علاوه بر کبودی دست‌های رئیس‌جمهور آمریکا، تورم مچ پا و خواب‌آلودگی، مشکل دیگری تحت عنوان «اضافه وزن»، نگرانی‌ها درباره سلامتی او را افزایش داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/683844" target="_blank">📅 08:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd6e28b26.mp4?token=QWd59hh0BCgxjaKk8ODGp8BD1WaKKTx6-MPpLp0DpVHi2kOMu1BjQlhpkrji3KInEKvckwCHNU3JdzcKaecRlQqZJIk_vrvW97KRjHXfhtXgQEm_m7pyrJwGDZd5YNRAkZ4UqWNcoYU0Zc7lSIhnLeDhgjE7B4Q_vYETkhP7m3iXw_OaDLxtVskiZPxIML5THq0LjIZH0-1lZKxmxXySP02GSczQtpOKq0KxmjoEaBRZRA_GDEBVCS8p_9X1btOPr9P9bGdI9yzgMIqx8epTyHrQqSpZUcedIIRGZnkdo7MO12LLITJfLGydYgN05T8EZAXCT5ccnAA3hEueCyERgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd6e28b26.mp4?token=QWd59hh0BCgxjaKk8ODGp8BD1WaKKTx6-MPpLp0DpVHi2kOMu1BjQlhpkrji3KInEKvckwCHNU3JdzcKaecRlQqZJIk_vrvW97KRjHXfhtXgQEm_m7pyrJwGDZd5YNRAkZ4UqWNcoYU0Zc7lSIhnLeDhgjE7B4Q_vYETkhP7m3iXw_OaDLxtVskiZPxIML5THq0LjIZH0-1lZKxmxXySP02GSczQtpOKq0KxmjoEaBRZRA_GDEBVCS8p_9X1btOPr9P9bGdI9yzgMIqx8epTyHrQqSpZUcedIIRGZnkdo7MO12LLITJfLGydYgN05T8EZAXCT5ccnAA3hEueCyERgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه از غزه مانده است...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683843" target="_blank">📅 08:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b43863683.mp4?token=sWKK7_QvK3XJGlhh7tOHwxBXGlUJ-ax2n4EaTB710lokZgcOSbdX39eOWVm1vhvT1ICwc4-JFsTaRsO4ddwzoJeIzZqsNdmTgRw3FgEzwLVGCQ4FkMW_6dm3VugWMEAupEJqTUfdLidp2UvPy3gzLx3hglNRjg-4tZrwnM5nc50HmK38aLj7QfPNG0Ed3K7yVzCe8kQIFee5vNuZjjlJCKsECwv5sOGQuXEgoNQ7pIC_gljAl4JfT6GePWUkmNvsvFCmsyBCR_C0YJ1MEoVstG7S2LA8HKrFzVmnHU5GFyQPumilyLPmTLxvdR_rLEfxjAhcGTSxk8pAyLAPcllFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b43863683.mp4?token=sWKK7_QvK3XJGlhh7tOHwxBXGlUJ-ax2n4EaTB710lokZgcOSbdX39eOWVm1vhvT1ICwc4-JFsTaRsO4ddwzoJeIzZqsNdmTgRw3FgEzwLVGCQ4FkMW_6dm3VugWMEAupEJqTUfdLidp2UvPy3gzLx3hglNRjg-4tZrwnM5nc50HmK38aLj7QfPNG0Ed3K7yVzCe8kQIFee5vNuZjjlJCKsECwv5sOGQuXEgoNQ7pIC_gljAl4JfT6GePWUkmNvsvFCmsyBCR_C0YJ1MEoVstG7S2LA8HKrFzVmnHU5GFyQPumilyLPmTLxvdR_rLEfxjAhcGTSxk8pAyLAPcllFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ نوشیدنی در ۴ زمان طلایی؛ قبل از صبحانه تا قبل از خواب چه بخوریم؟
🥛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/683842" target="_blank">📅 08:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وزیر امور خارجه عمان به تهران سفر می‌کند
🔹
بقائی، از سفر وزیر امور خارجه سلطنت عمان به تهران خبر داد. این سفر در راستای تقویت همکاری‌های دوجانبه ایران-عمان و نیز ادامه مشورت‌های مستمر سیاسی بین دو طرف، به‌عنوان دو کشور ساحلی تنگه هرمز، می‌باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/683841" target="_blank">📅 07:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a195f6ff.mp4?token=mhUt5mve4UTlhO0JDahBb_RdW2OCZVijcyTDL49ooPLAsIPMQOrKB0vREJ5OCESPM3rzFPMhOqIVpQo2vWS5Xal7HKzMOBUB74XD-vzX0vl4Zb8B249qc9GffumyGyMOyx6EgWInYiSfFxEEWRSSbARdID-Pf5bfoLfhS8KYLuCN_5UdjMi0iuuRAE8tjTjxoCVm-SgsLmoFjpTqtOi_G3lW6fwFezhZxZC2iNK7hhFy3X1p1ZKqhzOjXO-UZH-LuRgFirjCaSWaGqKYS2xTn6_qwf6LSV8TkGqerdwVQ_OJvwMJGzxMXrG6NiuKEaCU6-bbiPtFw6xdegMyRasf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a195f6ff.mp4?token=mhUt5mve4UTlhO0JDahBb_RdW2OCZVijcyTDL49ooPLAsIPMQOrKB0vREJ5OCESPM3rzFPMhOqIVpQo2vWS5Xal7HKzMOBUB74XD-vzX0vl4Zb8B249qc9GffumyGyMOyx6EgWInYiSfFxEEWRSSbARdID-Pf5bfoLfhS8KYLuCN_5UdjMi0iuuRAE8tjTjxoCVm-SgsLmoFjpTqtOi_G3lW6fwFezhZxZC2iNK7hhFy3X1p1ZKqhzOjXO-UZH-LuRgFirjCaSWaGqKYS2xTn6_qwf6LSV8TkGqerdwVQ_OJvwMJGzxMXrG6NiuKEaCU6-bbiPtFw6xdegMyRasf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جفری ساکس، مشاور ارشد سازمان ملل: باید ترامپ را قبل از اینکه همه ما را بکشد، از دفتر کار بیرون کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/683840" target="_blank">📅 07:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کویت حق رأی شهروندان دارای تابعیت را لغو کرد
🔹
سئول: کره‌شمالی در حال آماده‌سازی اعزام نیروی جدید به روسیه است
🔹
سازمان ملل خواستار استقرار نیروی بین‌المللی در غزه و کرانه باختری شد
🔹
کپلر: در دو روز گذشته تنها ۱۷ کشتی از تنگه هرمز عبور کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/683839" target="_blank">📅 07:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebc4a3e1e.mp4?token=RaqYc1ioaYndTB1aF3y0BJzcZ5sHKox27-QtfW_H_3Kd7w57iQg9ouvssNA_KY_baxjERJrjVpekksIfYzX9ExfSs3-yrCQZvG2ZyfG67yMS2y9T4eMdDKyTsZyc5kaf4YjScGyqDqm1zweKedZ4p2n6oKIiSGtyhaHIvWUZ9HsrwEcGvaiFLnDSm1rP_xl8VjddMSOSDts19z3YGr82kxMm26qC-3WvH_mQm7AISzf3aqPziUucXuU92230gNhV3448fJeRJaaH1_tu74ayMOHUixlaurtbaBweMGN318YLNlRabc94MnVLUwxpB9n7dcvPyBS5_uke5wx2MS3mxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebc4a3e1e.mp4?token=RaqYc1ioaYndTB1aF3y0BJzcZ5sHKox27-QtfW_H_3Kd7w57iQg9ouvssNA_KY_baxjERJrjVpekksIfYzX9ExfSs3-yrCQZvG2ZyfG67yMS2y9T4eMdDKyTsZyc5kaf4YjScGyqDqm1zweKedZ4p2n6oKIiSGtyhaHIvWUZ9HsrwEcGvaiFLnDSm1rP_xl8VjddMSOSDts19z3YGr82kxMm26qC-3WvH_mQm7AISzf3aqPziUucXuU92230gNhV3448fJeRJaaH1_tu74ayMOHUixlaurtbaBweMGN318YLNlRabc94MnVLUwxpB9n7dcvPyBS5_uke5wx2MS3mxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش کوه زباله در گینه با دست‌کم ۳۰ کشته
🔹
رانش توده عظیم زباله در بزرگ‌ترین محل دفن پسماند کوناکری، پایتخت گینه، دست‌کم ۳۰ کشته و ۲۲ زخمی برجا گذاشت.
🔹
این حادثه  پس از بارندگی شدید رخ داد و خانه‌های اطراف را زیر توده‌های زباله مدفون کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/683838" target="_blank">📅 07:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCuL-nRCTUlIo9vviwlWucSxizQDhZAcfZVYERS2RsQ6d8xzny92TLYepWw0qx1LFt_k8BWSA8J9G4SzCx16afXPru7mnR5-MTCQMxA_FuNlVItEKGy-2CqpgzHPouqotjcODbZOptf0Wd8eIWIS-_iQzdUhVq736X-ajKmb-wnGURROV_RDwfUt6CS-yNCHBnKnKrm9XF5ssMhyKfx80o33SsrvNBRlv4l8r1zd8eTSr92_AGaUD3W_ZMJViUr1RvE2sF0cCHYjrXEc90iKlACf6FRV0f98p9okNof9QcqVSMHU3KvsYlhnompnm3KwENk7UWwEYk0jCEGcm5F4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲ شهریور ماه
۱۱ ربیع‌الأول ‌‌۱۴۴۸
۲۴ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/683837" target="_blank">📅 07:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabea9b992.mp4?token=WkEe6biqVM9NOWQNvj-476HRkq1ZFYO4GN7TZ-5ZgXCxjJvyYl-vvzwU4PvR70JsREyq8L6rpbIw4-z0crzBW04aThF5gItyzz8l-s7Trzr5rgytzEQzZifq3ncRPRmDIRXdvY8WrWVUdOzwEHxjNDfwfNu55fI68i6DROOZvSvCmIY8fLtm4z39n91vTrrUVVYtP1u5U-G8mZ8Wzoi6eB7o2MHOpDzAX10kngszNSv8DO_4Dq-gobQt0I8HMF9raCPoaLbqr2jR_pfyM9AMNZmyTH09EDaVdsIlikb0EpDIJdknpRBhGkv7oFAeRzoVJy_9GcQn832deEk63DNhmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabea9b992.mp4?token=WkEe6biqVM9NOWQNvj-476HRkq1ZFYO4GN7TZ-5ZgXCxjJvyYl-vvzwU4PvR70JsREyq8L6rpbIw4-z0crzBW04aThF5gItyzz8l-s7Trzr5rgytzEQzZifq3ncRPRmDIRXdvY8WrWVUdOzwEHxjNDfwfNu55fI68i6DROOZvSvCmIY8fLtm4z39n91vTrrUVVYtP1u5U-G8mZ8Wzoi6eB7o2MHOpDzAX10kngszNSv8DO_4Dq-gobQt0I8HMF9raCPoaLbqr2jR_pfyM9AMNZmyTH09EDaVdsIlikb0EpDIJdknpRBhGkv7oFAeRzoVJy_9GcQn832deEk63DNhmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماساژور تفنگی 4کاره
خستگی و گرفتگی عضلات رو با ماساژور تفنگی ۴کاره از خودت دور کن
💆‍♂️
✨
۴ سری کاربردی، طراحی سبک و قابل‌حمل؛ مناسب استفاده در خانه، باشگاه و سفر.
🛒
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63579/180124/</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/683836" target="_blank">📅 03:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای جی‌دی‌ونس: ما ابزارهای زیادی برای مقابله با ایران داریم، گاهی قاطع و گاهی اقتصادی
معاون ترامپ:
🔹
هدف اصلی و اساسی حضور ما در خاورمیانه جلوگیری از دستیابی ایران به سلاح هسته ای است.
🔹
یکی از قدرتمندترین ابزارهایی که ما داریم این است که تهران را وادار کنیم تا هزینه تلاش برای خفه کردن تجارت نفت و گاز را بپردازد.
🔹
علیرغم تلاش‌های ایران برای بستن تنگه هرمز، ما موفق به استخراج مقادیری بین ۷ تا ۱۵ میلیون بشکه در روز شده‌ایم.
🔹
ما در تلاشیم تا از بحران انرژی که ایرانی‌ها سعی در ایجاد آن دارند، جلوگیری کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/683835" target="_blank">📅 03:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683829">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/683829" target="_blank">📅 01:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: کشورهایی که سرنوشت خود را به تهران گره می‌زنند، با مسدود شدن تمامی مسیرهای دستیابی به رفاه پایدار روبرو خواهند شد ‎ ‏
🔹
هر کشوری که به عنوان شریان مالی برای نظامی در آستانه فروپاشی عمل کند، باید انتظار داشته باشد که در انزوای آن نظام…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/683828" target="_blank">📅 01:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: کشورهایی که سرنوشت خود را به تهران گره می‌زنند، با مسدود شدن تمامی مسیرهای دستیابی به رفاه پایدار روبرو خواهند شد
‎
‏
🔹
هر کشوری که به عنوان شریان مالی برای نظامی در آستانه فروپاشی عمل کند، باید انتظار داشته باشد که در انزوای آن نظام سهیم شود.
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/683827" target="_blank">📅 01:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwQyqkfwebpVTpzY8j2h5otpSJBLDvvHLd7MU17Tg-jvkXxYYaOuqwG9txyeKeebgbmrDdmc5GCViqX7uf9_wqdAxicP2U5NQgU3mAkuQ2DgvLEJFAXw5RbvxehrsiRJWnAPAbs5gYzMoLG4YsPpXjMQq_z1Ip1XyRhMYLXNDzhHSpks5coX4hND0LE6-GwWc87KeFl6bWFEz_LC8aG1wXlFyF9Mo-uMflvQOCjHb2CawRLKLhGnPzHw-aMaVGb9e6T0_FD2RVS_5rB5LT203ex63PsheZak1JhXqAD4FgXoZVNiiCsyH9JtBXa82F_q24IL1YQgROkuwfCHFKcf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNugthC_v2FxS5LUDCsbSyhmYZCXfjZK1kzCI1e9_OxZOWCYotOfjk-Ppe6RwNxJ1VKD9TyZQ2Ea65g75oltdtoQo0re3T954LzVIcnYbnU2UFfafXn1mPsZqEzsZ4s1FeFCuXlmljvQXUngrwpo-I1BYBZcQe_OSmvbC5XUW1c44RE773sMd4HE9qX6pugKseZqxsKqSr5Ba--66PfOt0iFpIo97h7pKqrw0juUIPHdczjqZUaNQF7xmmLpXHSmefcIqZI0XMAyy9wICiQoXTtT7LWO6TlgRS5gs89hph5RK8HA74BtzQwNYeDtdQwCPdYejIdqgBtlD3tCbDkrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2YzmC58dasbkBvzXvTCP3NbXC_-dH60Lydaj4TBVY6lJWfBBOyOTtXCN8DaiKxTo0QBhcYFj-jqOPBitwLEiRbTyMSBInhMa4bBthauAnPbScj5xVhpuqZmbaHpFwbT91jvbuPdh75M7ag62jkqI64ymvDTcqTLVJRbb-PsBkd8QdwS8ETnuDJH-zImaIEMGjwyh5qJs9cYtUZ9ahFu8TdNalIzKvi2owXZG6DEDpp3JcR9NuIb1TTjcMdF8_dUlQLsnmroYFlerd0DcPG2D5exLXrYsGVSlCgG42vTOehJ9_X408PDDgP-g02dGwMMjlDmpFI8jW_jVkbkfwO9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNXlOc4TFjcvb1f9jpbpRnZcY_k4zsYpVgLJhbhWISQI9dHg2aMMFwFnNMuhO9-Z4qP6555CZWTdd-1vTeDTt7wHibPV3yU1rCWI5_0kQB5zCq0b6UfZf5UE6iVAOTsjPMgZPCsV0RD6_WJSSNLCWm70_kKNjYUvViKBUTV9DXHznSSn1GMCSpqwd7P5vhPoXFuauMH8BvNuRyFwDEg9vTRc3fyoKCAB2erbTuBKqfKkkIJmYZfFWl6weCshVINHW9c4g3syjfNueq5pf45YUJudEfthNi7bHNbwpZNDovGr2nEzdojgC6czhg1EXqz5ccNdikZedhISOF8J-TIWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwqxydyAelkCUQ4W11ykkE8vZDqLKOjzTxjmh2aieV776QyvTowEk4R4atFvZpAlNtvOGpNEJs6NzEdtQ4UudfmWPMACZkGFYsudi8gKglMMxR_wnAc6Rv9oYXTk-Ix6HXYoOzBsM9vNR4-d-MvYhEcVG_uGncu6KVqSoGl7Y2PApE_E4PUZ_dzSjgzszvXR_XjdJFplZcSchGIWeONkA5uy9w6gojrry9BwIteVfrn7mx-AsUZx8H_pjFC824fNADWx1ptI7jh7w2Z4cDqsjQAWgWDYsPWhgNXxQ1wLfX2sNktUmLOoYZHRNlmQNcHjaLmWaCRgW_TqS1TMyl72uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چه کنیم که باتری موبایل‌هایمان خراب نشود؟
🔹
این اسلایدها آخرین توصیه‌های بین‌المللی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/683821" target="_blank">📅 01:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر نگران کننده از دریای خزر
دکتر روح‌الله اسماعیلی، معاون محیط زیست طبیعی اداره کل محیط زیست مازندران، در
#گفتگو
با خبرفوری:
🔹
فوک خزری تنها پستاندار بومی و منحصربه‌فرد دریای خزر است و تلف شدن آن‌ها تنها به ایران محدود نمی‌شود.
🔹
هر پنج کشور حاشیه خزر با این معضل مواجه‌اند؛ برای نمونه، در اردیبهشت‌ماه سفارت ایران در قزاقستان از تلف شدن ۱۰۰ قلاده فوک خبر داد.
🔹
بیماری‌های ویروسی، تغییرات اقلیمی و کاهش منابع غذایی مانند ماهی کیلکا را می‌توان از فرضیه‌های تلفات عنوان کرد.
🔹
گرمای هوا باعث فساد سریع لاشه‌ها شده و در بسیاری موارد امکان نمونه‌برداری و کالبدشکافی وجود ندارد.
🔹
از ابتدای امسال تاکنون نیز ۲۵ قلاده و در سال گذشته ۵۱ قلاده فوک تلف شدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/683817" target="_blank">📅 01:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683815">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8WUbnjg81H5uK2l_RKFbcX2ZJQaZ4QON_-Pm2xipLATvZLlqu5gH4Vo-kPdX_Ea-xMwxZNPKxsw9jwdbHVlNO23dgSOyOn1KSWm43JeyuVPoI60boJjj-lthncPVA9URIm12SP-9dNCAnEkwyTA_oLz7WgKaM22ctX62zgDsI8OVGDjwhdzTdcbDGwSAkMJ4QqKwVs3bg_SDNSSLsYsFpya8DXUPZWGTpak9q-xzPXeEznZ0A_i3E1lG5FM_ePUgn4uIXD2fv8bM9_1ALEJHLfu--M_0kEzwWdTx_uXFdg1PObszp14THFfXgIreoqxiPpsP0LEjl8q35s-9cbIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاهایتان خسته‌اند؟ این روش‌های ساده، یک آرامش دلچسب برایتان می‌سازند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/683815" target="_blank">📅 00:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683814">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه حمل برنج وارداتی ۸ برابر شد
محمد مختاریانی، رئیس انجمن واردکنندگان و صادرکنندگان برنج ایران در
#گفتگو
با خبرفوری:
🔹
هزینه حمل هر کانتینر برنج از هند، قبل از جنگ ۶۵۰ دلار بود که بعد از جنگ به ۵۲۵۰ دلار رسیده و هزینه واردات از پاکستان هم افزایش یافته است.
🔹
با این حال به دلیل پایین بودن تقاضا، این افزایش هزینه هنوز اثر خود را در بازار نشان نداده و برخی کالاها حتی به مرحله ضرر و زیان رسیده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/683814" target="_blank">📅 00:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d8a90682.mp4?token=HjrnMH0hKVsJp-Y_adOWBikQ5yu7stRb2A6PF5-tpkhWgKKMGdL2tqqGue8vu69DSi2VfYSReXGfn5GgFpNKJYAPpKdTTOoXlyRA2TOQonJfLiqpy7Gc6R0ZbN8zw28QYOKhYEjgczuKh2adheHzIM1U5I_UepcHmxlBmOGyu5Un2rMuNZkx7x2qQ2YqvjNsq3wqxLihsZSipTFpk6aol_UtFeyuT_fnsWzOMv593KplU5Zy7hEiJ07Z07pcfukngULBPMmjY_BvyeqVRIRGBxTHmVQ3qedaiXOOEzCmdbeGjsCHQqBplEaM47v3entPaNg4em2mkkL-WiepejB4Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d8a90682.mp4?token=HjrnMH0hKVsJp-Y_adOWBikQ5yu7stRb2A6PF5-tpkhWgKKMGdL2tqqGue8vu69DSi2VfYSReXGfn5GgFpNKJYAPpKdTTOoXlyRA2TOQonJfLiqpy7Gc6R0ZbN8zw28QYOKhYEjgczuKh2adheHzIM1U5I_UepcHmxlBmOGyu5Un2rMuNZkx7x2qQ2YqvjNsq3wqxLihsZSipTFpk6aol_UtFeyuT_fnsWzOMv593KplU5Zy7hEiJ07Z07pcfukngULBPMmjY_BvyeqVRIRGBxTHmVQ3qedaiXOOEzCmdbeGjsCHQqBplEaM47v3entPaNg4em2mkkL-WiepejB4Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۸۴ ساله، اما همچنان در خط مقدم مهندسی هوندا؛ Chief Engineer با ده‌ها پتنت ثبت‌شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/683812" target="_blank">📅 00:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683810">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4afcac9a7.mp4?token=L3OC4DlnNHTT6XZGffpp1ZLjyWPO-z5s-SoQx5X0TkHFWaXN8MpDJvegrsdQV4euq7hqOAOljaIUtjwCXmR0Mgu5PjWFlG_x_JHS5Lb7Tjxg1W5mreORjftjM5sntuM-DHx_c1tf-sH-HYIattjhqGV6yu3OAu23xNVICJteXzVJ4veb0PWNldWtmc0MZaYkWgI-gBUwVqrgybxwYU02UTSafFgo3Mbt6nT7o4tl3PK4ymoNooe7eKludMASqrZti7aTVxM4iPEHnkGbb6h_7sHPsbNg543Ftoy5noEQorsbk6IosiKRIJ_Q77bCatasCPsp7GHAI9JBK3n321mNWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4afcac9a7.mp4?token=L3OC4DlnNHTT6XZGffpp1ZLjyWPO-z5s-SoQx5X0TkHFWaXN8MpDJvegrsdQV4euq7hqOAOljaIUtjwCXmR0Mgu5PjWFlG_x_JHS5Lb7Tjxg1W5mreORjftjM5sntuM-DHx_c1tf-sH-HYIattjhqGV6yu3OAu23xNVICJteXzVJ4veb0PWNldWtmc0MZaYkWgI-gBUwVqrgybxwYU02UTSafFgo3Mbt6nT7o4tl3PK4ymoNooe7eKludMASqrZti7aTVxM4iPEHnkGbb6h_7sHPsbNg543Ftoy5noEQorsbk6IosiKRIJ_Q77bCatasCPsp7GHAI9JBK3n321mNWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سروصدای برخی از هواداران تراکتور مقابل هتل پرسپولیس
🔹
تعدادی از هواداران تراکتور امشب مقابل هتل محل اقامت پرسپولیس در تبریز حاضر شدند و با ایجاد سر و صدا، برای دقایقی آرامش اعضای این تیم را برهم زدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/683810" target="_blank">📅 00:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683807">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس:جبهه اصلی ما، جبهه اقتصادی است/ باید طراحی دفاعی داشته باشیم
شاهرخ رامین، نایب‌رئیس کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
ما در یک جنگ ترکیبی هستیم که جلوه‌های اقتصادی و فرهنگی آن از موضوعات نظامی مهم‌تر شده و جبهه اصلی ما، جبهه اقتصادی است.
🔹
طبیعی است که یک طراح دفاعی حتما به دنبال محورهای اقتصادی بگردد. بنابراین می‌بایست همگان را برای تلاش و تولید بیشتر فرا بخوانیم تا تاب‌آوری مردم و نظام در این فرایند بالاتر رود.
🔹
باید در نظر گرفت همان‌طور که جنگ نظامی نوعی علم است، در نبرد اقتصادی هم باید هزینه‌های مرتبط و سود ناشی از آن با روش‌های منطقی و علمی سنجیده شود و مبادا کسی بی‌محابا وارد هر حوزه اقتصادی شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/683807" target="_blank">📅 00:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683806">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6As-GgLgI_rdM_klh2OSf9P2zQXHIc8hcFSvhhFUQ9WUkvuYCGU0wd3FSnTf9H1qVbdRotWeEYk91TYoqrJBj4-PG71gGQcdtGZZggjDaucoISGJ8qQISyiisrgu14Xoc6yYrP1ysB2arSpyhHqPhMAAVucNmL9-sKUKMT48IjCjuLzN6PU_rx-MmhVRbtHjiWGabDnukxlZmEZ-io5PDe2SC__D1wIzL4TnOuOt5eHp6cusUqkY-6idRUfP-Vh9w_JR-r1EY__Ng3Wh2wDGKUuaSIMkiOVtyRpLEAG5JL0GvSERCqYSSsH5KChRPIbC6a0F20cjxJ6aVhntG5i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پکن بعد از گذر صد سال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/683806" target="_blank">📅 00:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683803">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHmQ9HViv9_2mGDV1h_fzH3E2Pz1DyFeQTCBW2ABDrMqRPIgeQdOOgpZNsNtyZzmizBhX47b8JPkauB7Bib1IuWO2dAFtQx3BNLSWSkjM3D63lRZ5gMpxfXM7LfkTwTu84lYAZAbjrbyPuOUyWCczPz04gDb8IIScieVoU-kpx2TM5bQ_1j3cTI1fVYudtIKWUdRUrmaMJEPuDAumW0XK09-owQhszAueoqGva1SyCsJ87T4Fn9bbIPrJcQznFsMGIjRphHA34MicD4U0KnFtxr-fINTbXZVHJgB--Ub7w0MK-hde2bZTiQRfPGLvt-yYm6Lq5MRnIFD0x0gUNfVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/683803" target="_blank">📅 00:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683802">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حاجی‌میرزایی: با استفاده از کنتورهای هوشمند، به جای قطع برق منطقه، فقط برق مشترکان پرمصرف قطع می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/683802" target="_blank">📅 23:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683801">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
دلار ۲۰۰ هزار تومانی و طلای ۲۲ میلیونی | تبدیل سرمایه مردم به کاه
👇
khabarfoori.com/fa/tiny/news-3239874
🔹
پاهای خسته‌ای که جای چرخ موتور را می گیرند/ «پیک پیاده»؛ فرزند جدید فقر و فشار اقتصادی
👇
khabarfoori.com/fa/tiny/news-3239896
🔹
20 جنگنده سوخو 35 روسیه که ایران سفارش داد، تحویل شد؟
👇
khabarfoori.com/fa/tiny/news-3239775
🔹
روایت فرزندان میرحسین موسوی و زهرا رهنورد از جدیدترین وضعیت حصر و محل نگهداری والدینشان
👇
khabarfoori.com/fa/tiny/news-3239765
🔹
خواننده مشهور زن می‌گوید اجازه نمی‌دهد فرزندانش فیلمش را ببینند!
khabarfoori.com/fa/tiny/news-3239841
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/683801" target="_blank">📅 23:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683800">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5274835f2.mp4?token=PVONc5H40nsXDizG4Y41K0HlzUGR4xa33khipdINDoRe_HVzid0X-oSLVEdmTbJt09A9FJp4DjzFCWVYe_8l98g9jPnaMllVxBqWGzaZe-67RP6QAHcxKoyQDCBI-U0Xa__kqIeYBIOf9vkm1IgLrkXELIHATsaspJdrjdx8xZrRX9yrLgQhFS-TtIBoREZsb3LzQODXJTYgzEmSTLm4-hEX-RJObE7Eg_Pe9uTaxJark8MgXyswekLtFY0QpvgKG5F0UlIuu2xB-pWSnlecMM3e95-HG-6dtlkC1rha2ac88ADH8s9L_cExyZ9umAWEcQ_neNrtJO326e5VCZm80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5274835f2.mp4?token=PVONc5H40nsXDizG4Y41K0HlzUGR4xa33khipdINDoRe_HVzid0X-oSLVEdmTbJt09A9FJp4DjzFCWVYe_8l98g9jPnaMllVxBqWGzaZe-67RP6QAHcxKoyQDCBI-U0Xa__kqIeYBIOf9vkm1IgLrkXELIHATsaspJdrjdx8xZrRX9yrLgQhFS-TtIBoREZsb3LzQODXJTYgzEmSTLm4-hEX-RJObE7Eg_Pe9uTaxJark8MgXyswekLtFY0QpvgKG5F0UlIuu2xB-pWSnlecMM3e95-HG-6dtlkC1rha2ac88ADH8s9L_cExyZ9umAWEcQ_neNrtJO326e5VCZm80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، فقط یک سرزمین نیست؛ خانه‌ای‌ست که ریشه‌های ما در خاکش جا مانده. ما، مردم این آب و خاکیم؛ از جنسِ همین خاک، با نامِ ایران
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/683800" target="_blank">📅 23:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd65fde1b.mp4?token=Yt55OFKwCOYd4PhCYmxOMB2C8eu0O-ZWY3hK11K9dnI4onHXR9k1g5i1Fzxn-juzBbgWcDre-tsjW6EF9Ll0Ez_c7DbiSfQV5FucpcK8apl1poOjeVe1Z0oO2o4Mp7Soz61yFMty9420uhYEO_BAUr47mvjfBCUJwXF7kt0z5GTBufYxQ3p-pq8oblmOK3M74vmSXRYr78LHnM3F6nonID2BYxPXWpk-mhJC6fv99YZzkNb1tvLXxhsRV8VT7ZUFnwxGIs2pdMt3PvxYHhOIPDQfIb8h72Zc6kHMuTDV7GnVp6OxYHjOgC5KU2FoDEQbdu00BK2Qtu_2Z8oPl-cEMybw7ibuiDc5Bu5VJ5CJcAZ4kUydohWh4SJ1D18bFmYoD3eR-Kvjt2PABBp5zNjkIXaOi-oroCf44YvP6qoqaK5Vlcbi63HXJ95GABOaKfqqFxgv68JFgHqmVIjvmtlm99pFLYya9blQ6t_231o6Ad_RskGXGFvqCAt7R7_sk-atm7em8mMOkDz4CK1B__Raym1N3sedBm9XjKbE7a5YPa8Mr1tHRvfyUX5qiwsPlHBY7jDisaZocZ33EJBdg5_KhsGquTVvAt-QQcEoaePYCifuqqRwLncFtm-o_FQ1Z9Kwi8c5l7vAFwYaa6Jol0lwR9RbLjZ5eiYIfZJ_Rtj9Jos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd65fde1b.mp4?token=Yt55OFKwCOYd4PhCYmxOMB2C8eu0O-ZWY3hK11K9dnI4onHXR9k1g5i1Fzxn-juzBbgWcDre-tsjW6EF9Ll0Ez_c7DbiSfQV5FucpcK8apl1poOjeVe1Z0oO2o4Mp7Soz61yFMty9420uhYEO_BAUr47mvjfBCUJwXF7kt0z5GTBufYxQ3p-pq8oblmOK3M74vmSXRYr78LHnM3F6nonID2BYxPXWpk-mhJC6fv99YZzkNb1tvLXxhsRV8VT7ZUFnwxGIs2pdMt3PvxYHhOIPDQfIb8h72Zc6kHMuTDV7GnVp6OxYHjOgC5KU2FoDEQbdu00BK2Qtu_2Z8oPl-cEMybw7ibuiDc5Bu5VJ5CJcAZ4kUydohWh4SJ1D18bFmYoD3eR-Kvjt2PABBp5zNjkIXaOi-oroCf44YvP6qoqaK5Vlcbi63HXJ95GABOaKfqqFxgv68JFgHqmVIjvmtlm99pFLYya9blQ6t_231o6Ad_RskGXGFvqCAt7R7_sk-atm7em8mMOkDz4CK1B__Raym1N3sedBm9XjKbE7a5YPa8Mr1tHRvfyUX5qiwsPlHBY7jDisaZocZ33EJBdg5_KhsGquTVvAt-QQcEoaePYCifuqqRwLncFtm-o_FQ1Z9Kwi8c5l7vAFwYaa6Jol0lwR9RbLjZ5eiYIfZJ_Rtj9Jos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ خطرناکی که دیده نمی‌شود اما هر ثانیه ۳۳۳ هزار دلار خسارت وارد می‌کند!
🔹
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/683799" target="_blank">📅 23:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cee0dbb22.mp4?token=A3_yg-y9IFBcvBR3_TMgoP9ue_XzQu99cc2i7bYL5ufmDrINnBWlXJVCHU6bCu041aywbDA4U-vEe6juSrtGy85QjOdlm_0mYEJNggFgRCHW7zJW-kS3UStpgJrc8HxAAAn-rNI7H01AnzyASJ44rvN8DKXCZcfrdxxrSNwfR0VZPIlIUZBc-zro4pV4GJyv6rh2oCYbvv4TImaKjVken3bp8K-azBa2ymbGWrqJgG1D9Lc9aEURdNU_-ds5j16Gdp8QMtnSdOvdxeAgb60SSKAMZc7vddrYe6Fjo1Xyl95dPcZgzDUOMPlrcq5olEIiyZ8SDDGT9Glxz0iRc7VAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cee0dbb22.mp4?token=A3_yg-y9IFBcvBR3_TMgoP9ue_XzQu99cc2i7bYL5ufmDrINnBWlXJVCHU6bCu041aywbDA4U-vEe6juSrtGy85QjOdlm_0mYEJNggFgRCHW7zJW-kS3UStpgJrc8HxAAAn-rNI7H01AnzyASJ44rvN8DKXCZcfrdxxrSNwfR0VZPIlIUZBc-zro4pV4GJyv6rh2oCYbvv4TImaKjVken3bp8K-azBa2ymbGWrqJgG1D9Lc9aEURdNU_-ds5j16Gdp8QMtnSdOvdxeAgb60SSKAMZc7vddrYe6Fjo1Xyl95dPcZgzDUOMPlrcq5olEIiyZ8SDDGT9Glxz0iRc7VAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توئییت کاربر خارجی: با مناظر سخت جنوب ایران آشنا شوید، جایی که ترامپ و هگست در حال برنامه‌ریزی برای استقرار نیروهای آمریکایی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/683794" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe92a5304.mp4?token=VW9tLS_f1t9ClWbFl7L0uOxi5w1XNmINSJpYL1x4ERZOp6tNtIPiip8L39R517deSpupxx4XEwj635vFM_pOA6MhMWkdqySfuj5cE-2P0pgewtYPM41y9dJccDoIyRBq9yF3x2gJ814OF9VWhUUCdo0Cy-D-7fcsfdSbLBS4eRibqSyJS56dkbXukPuUtxYWHoJVovkKpAVD4L3_3Bisa6K6z_Ped1e-i1Ar4OM9YONpM_paF9RCK4CLslNh1YRJ6rPhbtfeN32FODcdkIdMj0_t2bF-QGjEbykiasLbBmdJoqKQjn5j2ATgo0dZ9ow6IqgR5w_j5MvDFOFazmPZgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe92a5304.mp4?token=VW9tLS_f1t9ClWbFl7L0uOxi5w1XNmINSJpYL1x4ERZOp6tNtIPiip8L39R517deSpupxx4XEwj635vFM_pOA6MhMWkdqySfuj5cE-2P0pgewtYPM41y9dJccDoIyRBq9yF3x2gJ814OF9VWhUUCdo0Cy-D-7fcsfdSbLBS4eRibqSyJS56dkbXukPuUtxYWHoJVovkKpAVD4L3_3Bisa6K6z_Ped1e-i1Ar4OM9YONpM_paF9RCK4CLslNh1YRJ6rPhbtfeN32FODcdkIdMj0_t2bF-QGjEbykiasLbBmdJoqKQjn5j2ATgo0dZ9ow6IqgR5w_j5MvDFOFazmPZgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از شجاعانه‌ترین صحنه‌هایی که در غزه بارها رقم می‌خورد، امدادرسانی در غزه است
🔹
در حالی که بیمارستان در محاصره بود و خطر شلیک تک‌تیراندازها وجود داشت، بدون لحظه‌ای تردید جلو رفت، خودش رو به بیمار رسوند، اون رو از موقعیت خطرناک بیرون کشید و جانش رو نجات داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/683793" target="_blank">📅 23:16 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
