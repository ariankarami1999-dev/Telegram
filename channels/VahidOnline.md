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
<img src="https://cdn1.telesco.pe/file/S_0mSu0b7DxR5vJmhVFAp2xFObgKvnt5JL8fSMrk6FYPcOOR5ckzU8kjxxZGLfBKwboy634LE4eCRLLM86ZxccZPkJhog4WH_njWZn00-fwnMz-0YmKbeyhS7l07HMXoaVSJH2ZLNHmq4gLJLv8h1epEYqk0efrxcQDPIcxGT68u8eIAHTEFQweZ4wC9fhXfg51C7m7_47bftml7BZ1fHN4JiFskcgapzCInRo432OHmJFnMsEokw7iz6RiKQ0MFZ0EQMr04zwIZD0bFVV4HAu7H14-Yw_87DkpxeCWciHwH4Rp05gZSAGXaxgSRwxIbP-eOlo7z6CDqKTFox9Uhnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 12:54:01</div>
<hr>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pG1Jz4Mz90q2wxPSSoUZsmcX2zEmWBr6H_W5PwEFPEGW4PDi015lmmHTsElSBYYqjf6yhy0_gVBxx_YbafRMxTOka34j6a8R9wNmpelUaI6eYwzXmTLzs1BflqpP8Nn9HbSIPXLEZlQALtHPxAIVlzQFWlGV3Pj1S0GWkdD8Hz4FgAjyrbF_AbJAN1IvCwkmrSrbI3ViHZksZiimlD9ed7tP1sr2qjbs2c17I_lz_rcZK_3WM8IYJxvbf4bQ7U42z0UhvZqaKsIH7SO-vtPAeNJkVNobCbrmYiFdu8r5VME_97RgvuGglxPFzPzqaOvOrpOrTIeDCCDfze4j66vE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Af8TxWUsIRwj8ArEAtEE9bh5YJhDWAOm3lhXkheHxHJpdggTz7QRIP9osdtHsEmaCXnieU_S06WcB6IBpo0EhKNuTfYTj5mXpk21cdE5emv1ooWgK94p0auefwwJ8rBIus7g6fpMzZddDz0JXDQ4BeC2lTLbsfZKY0kH6fvQDyRy-Mf8X0taN36V7OpGYpBqYNvKItWVuZswXBIViH1lxC5YTNk0bf93czDVJuUcT8SfBH1QFc9XuX6943o7pU2ejbK8-e-xs8d6vaHuAqun_beYJvNTK-rByjYqI8hpVv1Q7Ivx5AalkLTDS5bWrGU7aIWtkM0AdkVhF8V3EUhLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlwoG_Al22gIId6HudCRyDG3uwzQ24i1t_vxuECYOF6BlVjS0B3UWPPFWPHIIN-hq-XRr4j07A5w6TtvgsDzSWLxzUD0Pf-uL_HYDsGyEUSMPPG5mc1bSpTGvFt4ZJngkq14n-q9r2ku41I5WBil_KvwazXTbTKncqq46hYRk4wOgj_OAzfLVyIQdGzECaIvAEqcwwZ_LjZGro9Z3LdfivE3MJQ8vd07Yufbs011Iv9uQvdaLT6cpGfjNXVgXYgiBIVMZ8XmDTntZKBR-3n7QheWjzDrW62UcrFqg0CGXEVjFZSTLV5q7qIDYk2dxPzAoK_Olp9ASYoZRLMdXkV50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YNIC_Lk-FF8uyn0QQlPCOTvrz_GiE54OLbu3IriAs_0JuL6MFqspVly_NTTBz8kIEIknt0Ss7kiR78PRvOQcrgXmUWeBuwmUbaMHKSghkaBF11mEvBj7V5eOVTCNAR-yJ1s3V5P_2dI4IDwFTLFkLEEijewEnvMkrASJpV0Qjx6sRon6362ZUPRqeB5G8-vqUKwm3J7jg63aVlqh0tMSpK1HTJnbVETmpR1_GEoP-4U7Tmdzz1yQ0BA8tjiU9pD2pXNIBpGaee1NH5D-vRgoUXWQU6kx_MxRE5OPx5XVnW5L8VXVsU5i9dRAu6vQcwDOlkprBMozcXsqdTVpy9w-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oDpHsMY9tvrFQ9tLIOfzcZT5ySXYJSSkRXfNR8v5XF2ruZykhDL9MkU1lJxK0rE33tK-DZ_jmkBkZpySas4zfi0ULfq47QPwxm4QoSdkPVjSGJdP-MNGbGPPlhp00Y9uaDjC7mNdDTvsvbqwvaN2yHu_52DfaYJEj2zK72jNO7ZQQ7ifRGf_FYz1ENW4Bq-Q1SSPnqYaikWes4SNUq3dIfAVpi4JoLNGxeR2cJWaOhLXqYGO3f-W1IouiqodqGWM-42ZAAl5z_C5-RZz0DZdn9ZEOLxnUtkM9S4eT_54CUmHFHfKGFjFIU0My--IybvJv3GrAm0vID6Qb-qF5K1RGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/svIrnI7F-4bXMZgMhdcGQsTt2y1PzXrBZw6DQ7Q59ZgtDhx5Em0Vkq73BZY10oXqIdHqWSnfyRPXyZz7Jk31vUdbJTOz0JvyERsNPBOHhw8RIszTDJAU_VCRtmkCVJwbrzuX9gZPUAtGuZ8iczHEtloB8SMH1CjoD6FSzQ5wmDGbuRnpihM1fTcMkzGyVH68LOAHtzf5JvdHuXtoCJPtLe3pHNtpcopkyt4ur37uC2uBwqSyRHlmKrYAFO8w-KVHT_oT8-bkMVkUF58B1RKZTus0ELojhctoVTwCRHnuxDnSnhLPpfpn4WQT9-P6VV7_jQ5i9z5UFwaeFi5Eq-X5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fI46sZIvFsqsOJZVrR5-iUGiN9wg-KXcJ7gg6rRE70564jBPUOwKyX0ItOkbDf-A-0ZkBPQU6xKF7j2PQ6xM0U4WIJjTxRfvgEnF-Jy12Kmj2kw1VUe40MBu_SsM6gGKK4zde3PE0EcI9ekEKt4nlkAY1fkIODA1R_hGWggxup7VmSLy5tDzwF-w2O9yNRpGF_Gjv6WD3USrcYqEZTAcWWvhsdXNuk-7e4uBsFSarLPy2fAUE6_lhMjkriKyV4i02d02ixEg-j3nFGfj5wCqk6pIuSGNfJWK7hwF0A6g6-b8QPXsjn3F3m3ScIuuo4yG4n2b4akmO9sWEwQyn8m6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKB9f3VV1mOFSljOyZN7FuD6Yt3xuApQ1kHFIDszYq71N9NvICZkeOiMks--7qtjgRxtunakTaeIgLTFKAwmhoWb_f0PPPTN1C_Cvc4nno3s03RKQgIKpIN-YqkUHGv35MUX2dyPLhMzelee4SvGaUy2PVGR6omgO1TAbnFz60UssidLI2mX9QU_AweafAhizA6eADNnDHs7LxhrBiwAqJK9451QfnDXBBO_Fg0Qdne9mfr_Mf8UW_Wy9-k9aI4SvZlXVf2GLQUP1Olh6JqbN6XjOvYceDQdFgZfM3baCWVTAVOkj2CkSwT_WS7vC_rDoajrcLWt2Q27LgZ0zn4JCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HAYakbECAlbS4FITYfsK8SWCrFKnH4W7G3Rp7un7-ChwYigfzXbLmC8JRsO9iNBYGG3_01qm7Vnkan9nOm2tDM0z7O7hoW1Z8T7nowslB40JI6sjYEANE4ESkVYxZJ_gvFNnzaTNIiNLOAq3Nvty-fievj-7dQlqRbzkfaIEjQvUabbyllBubR4MTBGKl63Sw1LD1yfG1k7fHUU4Zfnj5_8t8Epbj6-cry4vQZvYFWpBwvQh_CLYrA7JBZyxxFl06aV2SvTOz1WALQ4VGH-fEa8dzR-xhQQZMohX2XzYlyvEy_WMGYEZITozXB3HD9Z5igEpCTLEE6TArqf-geraWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=JQ5sUIPjHdx9syBJqBkRg-9x5IRfAAZ6tiYKpMCzUMgqsvWX836M00Z2dX6YTtYTUAOqZ9nZH5Stp5NPMeOQEUxseiY9i8vycHdx-q_E0p9nuQzGtJwlqnqJ62BM3YAr1ohJ_foqpniQgJxzMan7VCsOFEVJBlo9hLJGzjAPvnQ5Ze92o9Gt0aOajhTLKkhS6NdTVYvPP8AWIhwnjuQ3CY0E-FH9ND0eq50tPmjA8f8ApmCZLD8daWUEw_kFk5O0btvDMY51DyQv9VylGCqV4oHIJ3p5iRH9SF9Zgf7vnm37J1ytGl4VP8m62LvCH_1Y9gJ1clFBx_9Xn3e1J5L2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=JQ5sUIPjHdx9syBJqBkRg-9x5IRfAAZ6tiYKpMCzUMgqsvWX836M00Z2dX6YTtYTUAOqZ9nZH5Stp5NPMeOQEUxseiY9i8vycHdx-q_E0p9nuQzGtJwlqnqJ62BM3YAr1ohJ_foqpniQgJxzMan7VCsOFEVJBlo9hLJGzjAPvnQ5Ze92o9Gt0aOajhTLKkhS6NdTVYvPP8AWIhwnjuQ3CY0E-FH9ND0eq50tPmjA8f8ApmCZLD8daWUEw_kFk5O0btvDMY51DyQv9VylGCqV4oHIJ3p5iRH9SF9Zgf7vnm37J1ytGl4VP8m62LvCH_1Y9gJ1clFBx_9Xn3e1J5L2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7a2Wh5sKKYnfMT0may8kpnweGwoPS4lY62O0mLcuB8m87entLx-_PM5Gf8J_W67AKN4mBixf0RFoJnFKCeGlRFEiYCtVTuYWRPKgEDIuAIgh1319540RBKbEvOF-drPUhFxGYXJbM0WU8kVnPl9KTRIodL8Mr5iQiRwqeN1YW8gZUmSBaVNZNx8I2uAQIPc7VXrgGCM08drx2_IPtL-094QTiuxbAcovcdDr3cG-aRZ02mps_5QEQJ-cWPKjbNNx2RC8u06Gz1I1jNzJvLI0-IRzfTLK8eZ48BzEXL_w7IngUksDrsiXQm8rgSOoZym0yhxorGH4b8uuxJj_9jqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=L591Cilwcko-0Ii3tE1WH6dVr_6m1hFkH8KMlKt4jaTD6uU4i7XsfwbVW12rfrUjcUKTIzATJ5DUpI8OaLqaB-6GcbapFPbZUWRCPh6mRIzQejLtWWGamRSAPmImQ_1HYzJ-1J-cCN9LbhSAFzX8Jy1tGyOgdGLnQda1Ofys8bbY22R55C3j78RyvDtelMs6vNabj9NJqT9FPn0VdMLuIJJ2I6NzuN1VABVWOtiP86_EsbI0fAFACytV-AIBxj3xI7USIfJX3YKaCGyo6mOjNQk5lVA7Seg515X6mXq0wvS8i709Z3i_k9kptXdxbCeAW9l8iA-rq9_JO0EFxAW7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=L591Cilwcko-0Ii3tE1WH6dVr_6m1hFkH8KMlKt4jaTD6uU4i7XsfwbVW12rfrUjcUKTIzATJ5DUpI8OaLqaB-6GcbapFPbZUWRCPh6mRIzQejLtWWGamRSAPmImQ_1HYzJ-1J-cCN9LbhSAFzX8Jy1tGyOgdGLnQda1Ofys8bbY22R55C3j78RyvDtelMs6vNabj9NJqT9FPn0VdMLuIJJ2I6NzuN1VABVWOtiP86_EsbI0fAFACytV-AIBxj3xI7USIfJX3YKaCGyo6mOjNQk5lVA7Seg515X6mXq0wvS8i709Z3i_k9kptXdxbCeAW9l8iA-rq9_JO0EFxAW7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjBpHJJuFihsE81Mt6Mn9gWvzVnH3iyT7NTEFwYw_o6vBb8sXSPOIxe_x4VPFaUnCywHRsGmxegWdSVEOnR2s3Y28ZBAhuqDMXAV0iGqSrDkcvX0g6DFMgsWDnkrxr6yx92rWMtfOzjlL4h2lwbPjF8-DWY8yjsrK5-87HK8q7EcFKw4V4CfNVbhRF8KCK-CaZSniStVRK9921IhCPpQjpm2Y630ornisgo7fhgxLO0lpyMvCPI8YGpDaS3sTblu46SLL38oVRgLxZZD0r7LIP3Cp4uvb-IPY5qGm2uaWZxbM-ILDyulZWpeR1wRav4Qir-2V0fQserxwp9LrJIERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mxHG2ODEW4YkFkRNmnPt4iX2MU--3KAmbU-or9VzSKpD8zX68i4WdonVB0zcCB_nuzp-M7DM14tODBppYZpfJw_AiQ4GhIkbg2nPaWlCEwecSYlKU7qw1xo-457r0HF7LNpU6HbNxzf1oFA02sWEvbI43O3zLAbpCYnKJIPn1onjgDAWILCbf8TcBIk1usZds8UUbH93Ysnv1m9HyKoVVE_FhYURInBo-gZlhKqrq0Sd1EFHiCqVaEcAInAXBL0zLMtlKJfkuN2qzS_MWoBpM2Asxg0ici9i8f7vj7_qQXG8wMSMHjP5EhUyTSPy9qpSWHuzDPHmQ6BD1kKOaxkCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nLkfyCrtcnFFeCMaLqryPl8jSabSg8BpPGpShLg_K1hMh83Jw1CpltLmmaUp6G7wcLq9TrU5USad9w9PMm29ZH1dWeMmiWbruYseQ87vppnebZRSKPPY3-17qaW8FEkcTYymsL5L_us4GJzwwOBIr1eP8V2qn7zWTkU0EEXTmAIJhPiWrIO81HiuR8dBwJG9AhgoaMUPpdIXPgeNBRhQIJav6vuuYA7MtkZut-LtODYGUgBg4nKaLNPiWBxhvF-7DeiSNy6MLMJgTFIIe3oKNHpUupMW1UTdHrARz46PGUwu5FgWRb9dylrpN3cb-74BYmL7AmXnFHHFfcJCZiU7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VOxofoMb-3Usd9T5Ev5vt-mT0Xl7AStSD1cE8VH9TRuFsnJPiHfPTrgHdVznSaTaWL-jCJcbhzn_6f_AZ-eCnrRzJPZdGrCr4ja5HBQbJZY-61HtSHrr_aRuyvRFU36FIVah-cwt9GWXCrLhS-spHBvtu6AK3McpMYWNo3tFmik0m9PiFcx3A2yzCBqGxPzbxJEpZMY7ez84WWoavNMdrrG9D5dTTZ6BUFaGbb7cmoQpSohcHydVunzKcEwQ2RTWZBwMAUC9Pbu_kNkfZ_ybztkG0tz6KP2FgKdGF7KPBe77jExcE95DOOdpk4sKHr-opcCeSsWWExsSU5DeXBAFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=dbaoF3mHTYWN7xMnsfddv9t3b8YFrcejsyv6KqAT6qTkBLt9qDUemv3az5N4t40WoeingqBxjgm2ukywtygzXS5frUzZprBC7e3ZXpzHYoxfCl1Dq9xt2kJ-nMbVNj-2p1uAVowsr2AT0td6nwPC8fDmsNvcAO0YSCUMPILkgd2phiX_aC4PgnePEWY_1oC7hMw6KbBccQbsDg-MdiXQcgLREdMFXeE0MhLHEQZrI8WDoopUoxAQ1FbQyHdwzt43s021z7egBXgytLUpCMiLELAg3N9RLio01u31HoB2GNUDyNIfxFus1f2-7nfEtdHs_3MFWM9faY1J0dmSTsyDUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=dbaoF3mHTYWN7xMnsfddv9t3b8YFrcejsyv6KqAT6qTkBLt9qDUemv3az5N4t40WoeingqBxjgm2ukywtygzXS5frUzZprBC7e3ZXpzHYoxfCl1Dq9xt2kJ-nMbVNj-2p1uAVowsr2AT0td6nwPC8fDmsNvcAO0YSCUMPILkgd2phiX_aC4PgnePEWY_1oC7hMw6KbBccQbsDg-MdiXQcgLREdMFXeE0MhLHEQZrI8WDoopUoxAQ1FbQyHdwzt43s021z7egBXgytLUpCMiLELAg3N9RLio01u31HoB2GNUDyNIfxFus1f2-7nfEtdHs_3MFWM9faY1J0dmSTsyDUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rPqFL38BCnvU_VnP-ldeAWKbneOTjMcLmRz7aMV9LpHk3gUiGnjEDwkIX_4gUp7Z4-eE2irS5I9RwxwjJOANAR2YJpHVlaUE5CItJae6WYCWdcgvDpQqF0swpxlI_GaY2Y4eXoLTzjWL1fAJ-zL5Z9KgBhqDW4BvH2N5cohPVljtnLOVUWJBRTXfGSqTNURQJm4OnU7TVkuSsYTnUtQRb2KJA7lh_qwTE85F21MgleXC09GbfS4uAQ-r0UudbwGYznZJE6vjM8hxsjlt8QlLFTFaIW4J9FIGNFOf1meSjsyDKrN09u4VaX9eSc5lVgo3T5BFD3G0vmPw_sgjXqpd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=pBrJfDtpap3M3qW0iuCDIUppVXc2DadXSrhUwwEG7ikpUp6SBF568hA5ZIE4druudPgIs-wsOh1_jBGuMH3Ism_BZuymmNHGV-WxHJN32GZpB2IgiwKl7-RA1UShG1fSpaLxaFYy5RCH-5JoCVEMM-tBcnB5sGYFDYMrtruVA8bUxRBozi7PQJxY9Yy6nJCxjHoPUMSoMb_dA4NvT3MoXYUwm-obC1bmfS1kSI_HCsSzrJ-Ym4jwFhZTh4f3kF5msrc_oS_YI0ql14Lzt8-4QhtsoDd2z2bIiv847chcrUA4LVWlOdL6UknuN52nDDpbNOwVm832DUV4CrJHksjBVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=pBrJfDtpap3M3qW0iuCDIUppVXc2DadXSrhUwwEG7ikpUp6SBF568hA5ZIE4druudPgIs-wsOh1_jBGuMH3Ism_BZuymmNHGV-WxHJN32GZpB2IgiwKl7-RA1UShG1fSpaLxaFYy5RCH-5JoCVEMM-tBcnB5sGYFDYMrtruVA8bUxRBozi7PQJxY9Yy6nJCxjHoPUMSoMb_dA4NvT3MoXYUwm-obC1bmfS1kSI_HCsSzrJ-Ym4jwFhZTh4f3kF5msrc_oS_YI0ql14Lzt8-4QhtsoDd2z2bIiv847chcrUA4LVWlOdL6UknuN52nDDpbNOwVm832DUV4CrJHksjBVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PtiQOKnZtHKD1eQv40A5EJ1J5SzkqhGG6WPYd_QIrjBl0-bvd2XlZJ7cLcb2uRzRxa0cds1gZeEQpZ95B4r34UaJmqWTlQoV_KFYRqKBimJIpDlEZBhWCGqvpHZRtYMfWYZvbQj9cVvG4Sa4OAnp14dwT55rx3K-chA8VOfl91dNesezDPlxHDj9ueKk8SEHXkEuOL8pNpPHyiiWhU7IaGHjKmrkfAYX9yi7JpKCA23haZLiG8Yru7chYXnR6A90ZN8ntpa3-bay1CdPjkh-tt5JaXBNC6Ufk-RcjqTtldA-G5FTfN9C_Z8U-uTTfTwotoeKE5WSUA-d4suLU94ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=JmyO8Ed6Kwe5KzovltfRxazrRI2v_L3gStsF_33Y-rxR9W4qiUFCT7Oe54ROqAvD02KSZ6VAWAuIcdd2DZbIggHV5pca94gJylgQ4tN2Q88czYJBkC8abxaIsEHfb2q21Np8B67DUa8DIIMLKaej2KbtAYz54TbZZZJESuwJPpnG87mcLnk74CL9Ookec1LOeJOcx8yYrgPofZtor7GU01E0Lrppg5xzaQxvGGr5ZTJOduP119pZguRU6pbOy2eoX8nFM0-zTE2atfn8x5zkVkuizMAPRShmb65bVj2CjKWmzQTECzNZVkY2a7Wg5l0ixQrCSoD1zMCtQAiTFXLWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=JmyO8Ed6Kwe5KzovltfRxazrRI2v_L3gStsF_33Y-rxR9W4qiUFCT7Oe54ROqAvD02KSZ6VAWAuIcdd2DZbIggHV5pca94gJylgQ4tN2Q88czYJBkC8abxaIsEHfb2q21Np8B67DUa8DIIMLKaej2KbtAYz54TbZZZJESuwJPpnG87mcLnk74CL9Ookec1LOeJOcx8yYrgPofZtor7GU01E0Lrppg5xzaQxvGGr5ZTJOduP119pZguRU6pbOy2eoX8nFM0-zTE2atfn8x5zkVkuizMAPRShmb65bVj2CjKWmzQTECzNZVkY2a7Wg5l0ixQrCSoD1zMCtQAiTFXLWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xb4f2_PE7uQ_-gXUMnO4MrIsbBZuJwMUZglGirUvOx0UZ9rl7nCJHiV1QJ_pscPYyVNkXJLA2017u7Y_ohv420JDILMPSoaQ7pkSqFiJBLjzMCxPiwT1_uILVu1EPJDx_ktFp5hAT0VeafZU6s9hIsR18ygr6LFHSjHdO7yz3jYMuGuHDtXCukq3M6xcXz9_aEGpdIAp_2N7DmkJh2li5YeVqCi1g6yBxjlaJsvCZwtJVJqn56LzwldpdTwM4cIyoqfJpTEezPU-PeRmmjJWM2kBfp41TJAxsQAKD998rqGWjNtUymyMJ54I6sooY3g9ATfBNGWpcY21QaBqrGorpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oUWykDWbRON2w8kJkqbDb4m7OQWcVraq4pFvDvQoTdhLc7HS76U35kafimfzJz3_owGcuLcNt-Bf1XkL7xU_LuginsqsQw_00ffnMm06spn2KG-77PvEcp-meYywJ7V3OVFIlDsdVvwvwUIh1WiFm5PShCiovwOK0s1ekgZ-8QJf8kpJqsX-KA9VJd3GqXoDh5Ex42USx64Dd7i94qOK1bCKv2r2Bt14Ki4kB1e2UGwCQudmvv8fF0bbZRHnJ8Dm88mZI3f7Sp6uZeTbclIeoqIuhjhGrgB9DkOs08_VGwWQNuDqB7C5lrD8IBTSAehMPtjP-94rdOO3OlvbgbRstQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vb3ZYf0R8ul3VeURaxThlIFBZbH4iQNvwW8-mi610GqkJQoQRy98-l-5poplAru1f4PKD2czBniVhfnPSFb1jXlxnsVeRuea2esyvI3m0HH2rN5hjLTlN7t8unp9O2dEElUBkTbI0KuhGP0q_TcpYEqgQO8d_WgRvQGD-DoGpDtvESupJ3NSwTiJ0sOYkVJE5pEKLcdyzcjmKeSkwr324471mCDdhX_CrX2S2a-qtZZKDOM_dSIKqY76dnRMwYlC89l6U6cx65REX9pBwg1kM6Cf3XHMl2wVkFpKXnEGetD4QCz1xaKohXOH-fsF8ZXcDw16xQDeKBa37T7M_qHjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=bkEAV9brqQase1cWideD9Zd7DGjTwKGfj_LQIn2gIQNv-QTmwbgWgmCZLbBISWYphqYOuGUCmnoKGC1EW8WpSoEFZjfJUSJUrakXR9g4n0S0jvdP-N6NkcbcNsEaLJZtuW_sbUY3VZYZyQJNvlK9elEn8mV7ocrwUBh-yOep1UUJj-sc3QosnFaTFOSyKRKWuP6n07Iw70LJiPH4mYJPNVXpUpMscLJ0mVA9APs7ZCapa1dLnBPNEp0SKqZ0mPVCKBh-mOVIl-d9OC-AuLNTxgtybiT1TBwUwfFvYyRjnI144PvAaWmMgK-LAfLuZb2K5F8xnHY92over6D9pH_N7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=bkEAV9brqQase1cWideD9Zd7DGjTwKGfj_LQIn2gIQNv-QTmwbgWgmCZLbBISWYphqYOuGUCmnoKGC1EW8WpSoEFZjfJUSJUrakXR9g4n0S0jvdP-N6NkcbcNsEaLJZtuW_sbUY3VZYZyQJNvlK9elEn8mV7ocrwUBh-yOep1UUJj-sc3QosnFaTFOSyKRKWuP6n07Iw70LJiPH4mYJPNVXpUpMscLJ0mVA9APs7ZCapa1dLnBPNEp0SKqZ0mPVCKBh-mOVIl-d9OC-AuLNTxgtybiT1TBwUwfFvYyRjnI144PvAaWmMgK-LAfLuZb2K5F8xnHY92over6D9pH_N7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YksxjM-0uAwb5GsKZ7Z2PYaVVkPVN7uB1lT2hvzoiS0N4rbVhI90YwJSAoM_-Ek7SyWcefXPuNvBlKIuqQqjvmwj-jDNdsMzTsmZchZBs-pLTX1YjrQ7awpl2SEWwvZ3jHpga-Md5nMqsIn4IDxByxjvhkKqGWMhnhwLu-KrIGcG_GQxclKy_WR1UJHB0QAi-9O58CrlIMz4OJoL7bHaeukN21_XKZYstOybrR0cyLS9rinfRNFS63DlcHSYaPvv19LIu-3dhoJ_cKeG9kj-ZA7y2eZg3Py1Q7sA3-KyyOa-0ZALrLXTNEDlZIM51lP29nytehBxM9ER7TGvKXZGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kp0fvUAps-PSjuEKitAusTUFkZA8C-RgtoBpJe3VsCBnkTuOv-aVRg3-2-tT7sPbfd8UFohFUC8i1K73jxk2a6OSOnL1dz6TcTXFWu73eJk_KpJlAC2Bl7tYKyGTDqUpDcIv5LdE9PjtIgRtQnjL46GDdd-X6dsjeUhrqKGj0RBuhpI0Vf0HnstBHvUgoS05bUaRG9iGGjbLJsIeKQChEuygpUgXXE5DFtkCxqroWkO6R-YzNdbPuRpfueOTO83-IvskwpONQQcEEdpQjzpkn4EzsyMiLmqvHG10XplQVxLz75v6Q7SvSQTLIaMgeUJpd-aVENiSFIRx5bPYNG1tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ملیکا همت‌زاده»، دختر ۱۳ ساله اهل روستای دسک شهرستان نیکشهر، پس از عقرب‌گزیدگی و در شرایطی که به گفته پدرش امکانات و داروی مورد نیاز برای درمان او در دسترس نبود، در بیمارستان نیکشهر  استان سیستان و بلوچستان جان باخت.
پدر ملیکا روایت کرده است: «فقط یک خانم دکتر آمد و گفت سرم می‌زنم و پس از تمام شدن سرم، او را به بیمارستان نیکشهر که مجهزتر است ببرید.»
با وجود وضعیت او، مرکز درمانی بنت آمبولانس نداشت و خانواده با خودروی شخصی مسیر ۷۵ کیلومتری تا نیکشهر را طی کردند و ساعت ۳:۳۰ عصر به بیمارستان رسیدند.
سعید همت‌زاده درباره ساعات بعدی گفته است بیمارستان نیکشهر نیز به دخترش سرم وصل کرد، اما پلاکت خون در اختیار نداشت.
بیمارستان چابهار نیز پلاکت نداشت و قرار شد آن را از ایرانشهر تهیه کنند: گفتند یکی دو ساعت طول می‌کشد. یکی دو ساعت شد پنج ساعت اما پلاکت به دست ما نرسید. تا ساعت ۱۰ شب منتظر ماندیم، اما به جز همان سرم، هیچ خدمات درمانی دیگری ارائه نشد.
ملیکا همت‌زاده سرانجام در اواسط شب بر اثر تاثیر سم عقرب دچار تشنج شد و جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=lcM-9_ycNllXwbBrCzSYCsnQkfaXvR1birrlTT1DGmmMYmm92tbvYUWvlsGek52ZXV0TmfnPd4kgsMte4JIPkl_Qlv1TLpZuj8oofAcIs48scUPVvwg2gHfP0nrFRH-e1ybs2023Zp5d4xdlFO6MCPUMXXD09-0xB4QzpFMky22w0HW_uOa7za9DBaS29V9Z9jTnJtBPCOluc_XWzXSJK5RDoVuRrCVk3J9ilcpdig2PhgETFgYZTmfixz73hpuxoBKtbTBxe_FcpINSsjmtTnca5GsbFd_E1p2FRxmIs74Nc_ZytYosf0zg2oPkeMeLAykH9pABqRfGBtAl9ITsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=lcM-9_ycNllXwbBrCzSYCsnQkfaXvR1birrlTT1DGmmMYmm92tbvYUWvlsGek52ZXV0TmfnPd4kgsMte4JIPkl_Qlv1TLpZuj8oofAcIs48scUPVvwg2gHfP0nrFRH-e1ybs2023Zp5d4xdlFO6MCPUMXXD09-0xB4QzpFMky22w0HW_uOa7za9DBaS29V9Z9jTnJtBPCOluc_XWzXSJK5RDoVuRrCVk3J9ilcpdig2PhgETFgYZTmfixz73hpuxoBKtbTBxe_FcpINSsjmtTnca5GsbFd_E1p2FRxmIs74Nc_ZytYosf0zg2oPkeMeLAykH9pABqRfGBtAl9ITsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=s-Ft2rtg7wdWcmf3iL736ew90BYfXnp4CSWdvqSULrCGNhtxoF7Exxs7grHM-JCc7ZJhZwYfT7Go3WZkwp8MJQ7Mhc7BTbW0aTcQ5tvmF0ppNZurPXTSts8QX1c2ToS5qPSuzjgfe4xmYGrRM-22mFRIg-1U5PFbH3up0fLFUKZlZtHo68HWvnT19jmcG9z5fvutJZsEO9XWYy0-fOLBfPeWflZnNrpv-Xo241MoZhOkg9qeEslj2kDm9jWd1UhPEgjSeF0fZygWVgOKKU9G8QqlSJRb77MUV5OebFiTG2vSV-rzm8PIWO37V8etDZN7GogYKfAg7pEEGe_3KIlvJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=s-Ft2rtg7wdWcmf3iL736ew90BYfXnp4CSWdvqSULrCGNhtxoF7Exxs7grHM-JCc7ZJhZwYfT7Go3WZkwp8MJQ7Mhc7BTbW0aTcQ5tvmF0ppNZurPXTSts8QX1c2ToS5qPSuzjgfe4xmYGrRM-22mFRIg-1U5PFbH3up0fLFUKZlZtHo68HWvnT19jmcG9z5fvutJZsEO9XWYy0-fOLBfPeWflZnNrpv-Xo241MoZhOkg9qeEslj2kDm9jWd1UhPEgjSeF0fZygWVgOKKU9G8QqlSJRb77MUV5OebFiTG2vSV-rzm8PIWO37V8etDZN7GogYKfAg7pEEGe_3KIlvJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر قالیباف تفاهم‌نامه میان ایران و آمریکا را «سند افتخار و پیروزی در عرصه دیپلماسی» توصیف کرد و تاکید کرد که ایالات متحده و اسرائیل در جنگ اخیر «به هیچ یک از اهداف خود دست نیافته‌اند» و تهران پیروز شده است.
قالیباف که در جلسه‌ای به مناسبت روز خبرنگار [در تقویم جمهوری اسلامی] صحبت می‌کرد گفت: «با تمام وجود اعلام می‌کنم که ما در این جنگ پیروز شدیم.»
او افزود: «در جنگی ناعادلانه به رهبری ایالات متحده و اسرائیل، ملت ما با قلبی باز و بدون انتظار هیچ چیز در ازای آن، شجاعانه ایستاد و جنگید.»
اظهارات قالیباف در حالی مطرح می‌شود که او جزئیاتی در مورد اهدافی که معتقد است واشنگتن و اورشلیم در دستیابی به آنها شکست خورده‌اند، ارائه نکرد.
@
VahidHeadline
قالیباف: ما نتوانستیم آن‌طور که باید این پیروزی بزرگ را روایت کنیم تا حس افتخار در ذهن و وجود همه مردم، جبهه مقاومت و آزادی‌خواهان دنیا شکل بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=YC6F5RrsFNBjqXgr6RlhKPYHHYRCFFnXenR8vEHfErEG6BQewgvBBXStvVXkdziI0XFUhw51VfdNnemCdI4Ke-ECXLuCYpOQMunOmCCkK6qFlw-WHf0KkvFRh7KpCczWDBEAUyZskWgbHZy8d-qVky51JJkFsNfJ5JUlHqhBDYeB2Eio40ECDChi_Isi9njIEVdAs8wtRPrHkOIDaw-o90_x42UlLopYmWtEw06t0Z-S6qRq9bR7Zcu0U9013nMOdzwdErsOtldPNcJYBiMW4u652ekqvtPwhwUjYTrmbSBYbWwOO5wD2-SmmnmPGhcFueQGJBdk40is90MfVet7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=YC6F5RrsFNBjqXgr6RlhKPYHHYRCFFnXenR8vEHfErEG6BQewgvBBXStvVXkdziI0XFUhw51VfdNnemCdI4Ke-ECXLuCYpOQMunOmCCkK6qFlw-WHf0KkvFRh7KpCczWDBEAUyZskWgbHZy8d-qVky51JJkFsNfJ5JUlHqhBDYeB2Eio40ECDChi_Isi9njIEVdAs8wtRPrHkOIDaw-o90_x42UlLopYmWtEw06t0Z-S6qRq9bR7Zcu0U9013nMOdzwdErsOtldPNcJYBiMW4u652ekqvtPwhwUjYTrmbSBYbWwOO5wD2-SmmnmPGhcFueQGJBdk40is90MfVet7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4nbam6ao29SbViHth-M2cZoj6qgzTArWLc8J4uhE2r-ThVkvkN_z4Nyur9b7D5TaaByv9FduAJSwCqXC3QCOprT1LETRu1oRTKCDVkKC7yn_S6HzEZ9ZpP5L8hvRYtLAMA4DlQZwfwlIPhwY2N9SquCJjbrj4koEx_BtIT7tuAjoRbpT9cYJdE9Hqh7730xjDenC9XijvD4Ofi1uzq8Q575LclaASdVGdK0M5a1UMF95nQbgHCuWKaOsxc_SrVEbF20-xj7ma8aKhgMbFHLZrgtoIurK0aGzHMD5NkkbwNq-EmGqPBqbPNUSlqzexddGWwUbtz2lUr85Sc4eD4nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOLOJ42dusQSio-aVUsEeHCDs9VA36za31gbLwgGhYwJGoqBF06obXHNpjHIYBqmrla8YI1b7pOGF7hvcI-sUfCJCpW3mAvW0JMdMQzB4EZHPPBhl7zIng49KZCy_NhpzHm1ubRqxOj9iSgO07PST4AUIv-89aP9v3MRj8bgfV2QmYKoWmfzzxsuUKwqPIi6Wba5s-6Atxhib-XPmr4sR0sii5YYJK0J87Qp27yztlEKKKi7s68Bl_HsrvKU5Srphwe6tDMdiiaclpJUkAdTAXcPsNTsrHGFoYQuictxL6lNb4OCbaWXtvURZttK64VEECnlGxWmlstGw0zdnr-o1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYJ_jmnAT-pWqeU2lLU4k_YykmiilGWeJN03aVH7q0JnC3nvDbvY6usPZIuVJSpHdi92BxzmSNG_FmkPshaGftvMuhjc8V5EV2D_P5DFp6YFXvPUeveTZFMzx-32VZ8iFD7Lhy1ETg-haLRupb-k6-JCFGgUPjIFaHWAK3hmdKGTGq1TEBeV2WX49fEzOiFN0sLW-6BvsqSb2i3u1aKyYoOMFDeUfQ1NszKg534RniBbUniarUUXttwjq4RWqmXltyNeTuQMBtRbjUQW4eDiiOm1zdVGn7wCNS1wn-np5P99ibYlU-5V2lUY0_c8WIGjRuN54gVdgln5iBKdtK8aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4EtWzAAKu_-30qlwFVMToZHtsGJ8jw9HCR4viI46ev0yrybgkMoypAwwkE-K8BxAG3w7oNyNeHr9H97EPEG0Qc9X3QNGncd8x0pQ_4zsioEHz7zEXZjy1n4W4gtehwyqFKaIj7ApF_XMwvA59wahBeXficzo5BEYOrtvCc_ci7ool4SaAnDbh9ZKTAlcQ7xV18bqu6YSbVhU5pb9idkVRyvXE-YDS29vBdQcnzLGUcttQvxC7ZEqpX5SGC-6Tm_xHjUbnD934AnUrzxZSxGIE4fL8g1uE6qe7t75E9h8U8tZXk_029XYBjOCpk7tPWGjtB4BqB4yutJYf-4lCODZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2ucaHikLOZiQscum6gjjjtMGUQqgTOH4A8BpANXUE_IRuMiBvsYY8du3uE6bpa93wsiY9OOyeHKjm5ZmKVQA4M4VbjvKAz4wVAaxXKg9vMypojFFpX84f74o7944YddNGO25ZlS8YBzTb48qJn-AV5I4nqL2Ag-dfsdqkljf2IEbNnW0IyA0ElI3CLcVMVkWUSlFBKo5RZChIUZGDWcFXnWrNe2DEd0yQdwyW1ev-P1E2xX_C-WpPk90jYWUf48ffvm3Wwjsshh2BL6dyO3XjBmjXlc3AvwMLh3lIkdjrJiCO5GeVA4XwUX_miuGKy8aZJiXkUjg4b40h25RhLkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnlDJYRSk5CgNfa8ciOamnXBEdJ_6dn7rtTKhWOLf3UhXNFPs3yOXx0wLN1KpPWNW1C5sZ9A6n-D2xCoTdowBsaHeUxKxG5XtYFg2ifj6wTgkbl8LNKZ61ZhhoKckJzGZV8oom-Cq7EMa0osGuf0UIkI8BBlwFlvIe3g6CtGeqdyBSHvk705yteWUA9zXCZk1E2bZSaTYYQHemmvj_xOa5BjKW2PK-rh1MPaj79Hcfi-x0neiai1S_IzWxyySdOyvbgyWQWBsYH8xLxZHGOUmo1EGRxu1aI0Ihl-H3tRBfbmhWXQIZKsWZeWWvOJSV0rtE5BD7e0uq3MgaYrOFpNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ayp3V_oyebR-00PD9jtKgFdKDQwRpqabUqwjMK_ah7wr9pH5yVLlWNnrWICJEBR3FgrBIA2e2eYxYR0iZOqpi7_H0ih9OoLf5mqa5sf53viBXhDWTrjTjPoZZx7gSdRfyaA1-43A_OKOXffNaGZ7_Xh0XvIOwVcUOuyubSt4neACW6yHetUBfg6olv5VrSk8uu-mTvNM19v0pCiV4lnba6zW-xYzUK5NXOnuj3YCR36ScPiMnV8XV9en3xxnO_ArIns4L50dzsD6MCSvjXmbeUoLYDTMXJRU7lvl3YXAWDBIOpc-0CIDN7Ku06xx95dzKitrqxfnxCXpkDZD0Tq4pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=bKiqaIWuldEPJk6b6ijaV_msax8PJSdpQtkP8x8qIwvRmpd7qJjZ6W8LdJg7H7lkqYYSuPtGZzBLGVe-O4NYYLwGUbS51xFebVt_Pu6t4nDRGAvWvXhBxvty5IawEIyOo6Deq4L8Nv4RnHxd8yUABwy4dDaY2SRjgudy1dqm8IsNEjfu6WPBr5Emgsm-M4RPHlwtU1GdBMGe8zGF88XcfyFKd3ISzIkygcZs2-AmVabo6U8hG8obzc6N8b72YXzoa3we95qPbjRpf_Z6EveSEdFpA7eviwE03bN7Nft33mDorcWKUIEyUY5UfYQYMpwQzmLMUOzQJCJEOx3m4mne1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=bKiqaIWuldEPJk6b6ijaV_msax8PJSdpQtkP8x8qIwvRmpd7qJjZ6W8LdJg7H7lkqYYSuPtGZzBLGVe-O4NYYLwGUbS51xFebVt_Pu6t4nDRGAvWvXhBxvty5IawEIyOo6Deq4L8Nv4RnHxd8yUABwy4dDaY2SRjgudy1dqm8IsNEjfu6WPBr5Emgsm-M4RPHlwtU1GdBMGe8zGF88XcfyFKd3ISzIkygcZs2-AmVabo6U8hG8obzc6N8b72YXzoa3we95qPbjRpf_Z6EveSEdFpA7eviwE03bN7Nft33mDorcWKUIEyUY5UfYQYMpwQzmLMUOzQJCJEOx3m4mne1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mboj7ENeNzvXJXMugI1NgsB_kvYfWykEhNSKSLAoSzpbePnl3XGVlq4gRJK0gGwLo3n8-eWuMXdVYWAPLFiBQUSNXF1msKQ0Cltsos195Os5mtYuC5eqICVWLQ5-6uRF4jg0Qh0Jy_pN4zl3MgkJHw9U013_TMYyM6I_zE8BYMqQ8IqqTvW6alvYi7SLAOOoQu_1JJoQOdiSesE8eZyAcKW4rxYEKAkP0XdCK-VgdX6d0ZqiYoMjAFENbIQIFAuVg1OhaFTzyWSFQW1_4lKL1oryN_GjRj2qwUOp-prtOCYsHlLVdixrTZNSgx8sTjtExaFAjNT5_Splo__DNwo93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkVl8Yqxjkuu8ZjaqVbg7uhMx2K_DG9xhCM16ihXf0Vsi4JiP249wp5gS1PItAG5-MjDcs740l1GBk-6WNH8cfNBiYLjsb1w9N9F0IOF-XPTcZMx4Xwep5Cx3WFYAfhb7jqCgVxhhDz7PrZ2FFxVKF0oqmb2HRQNuXB6xueOlX3lJfFKvaYQNUUnw8yJ4booGZsxJhvZ5EtkbHz5YHgoGeSZ49cNvL2m6_iL-AscAMRA3Aqy2Bq0C2-OaI_vwoOvYi9J-e23md7hORm1A-alvKRTQrR66ioqpflfr8iY567mqcsmL-5lC8ufYpePAgt9PoSHDguF5QSlS4lO2QvP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcpXjOSn8lUSiFDOFeiFCJAyrhqy1CirF3qqfq5C8WPhJz_84qRLBT-dxXLh5WX16OFRv2GzAVgdeThs9BLGUn3ZCn4plGaYzoa-Fguks2rEzzaoLxZ8GNHMt9Su8aH3HQXk635HtG1RRag50S0nqYomLZBdpKMtx1CIWMri7c_WywrYE-xjI2XQfuZFmoybGtX5DwIObbTmtplDqf2uHJyu_AekK7c7RAD39ktIhYoArWggbkrIhXkB_jcCKoyOlPlEGC1YzYcAPa3selrzeJgFh3_za-xSygzcfDhHFMILfxIKAiC_bDWHKqJe49tIxX3_oLdh4_xOO1-JkcFlcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=dkhDGKubG-TA25YdQwkgp-4beSzvEqePF3ErjjejCzrBJPrstmRCJnoaoF_T7TxSrKtsLtjbZeXmL49X-kg-agx_EjflW0NmW_6HO59VZrNFzbSCD1kdAfyYqqRL7r_Dl2E0MM2CTTF8WEWQM56KyuFbgwxCvhIywADA9ye_Bey_-8wSmZx9LfibQZtJymUJ_bJABlprysMmr_iUwBXyoHAX68d8ZlVLtbbr2xUwmkmx7TahzxRyrIiDtfD-xrQujGMf4ozdf_hjfX47_0KWfc5g-y_FoeSc1v8c1CrZYVEx9XJQFQ19BxbrvcaGzwMIwUhjcWozDSAX3D7UQkKu8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=dkhDGKubG-TA25YdQwkgp-4beSzvEqePF3ErjjejCzrBJPrstmRCJnoaoF_T7TxSrKtsLtjbZeXmL49X-kg-agx_EjflW0NmW_6HO59VZrNFzbSCD1kdAfyYqqRL7r_Dl2E0MM2CTTF8WEWQM56KyuFbgwxCvhIywADA9ye_Bey_-8wSmZx9LfibQZtJymUJ_bJABlprysMmr_iUwBXyoHAX68d8ZlVLtbbr2xUwmkmx7TahzxRyrIiDtfD-xrQujGMf4ozdf_hjfX47_0KWfc5g-y_FoeSc1v8c1CrZYVEx9XJQFQ19BxbrvcaGzwMIwUhjcWozDSAX3D7UQkKu8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qUCBLs-UHX0pJb1-v3VnxS9NXftaLoU1w1fkpFEpgnSUWFSsnvfVNcOrG0ZCrfVSF7-xXo9J_6GA5qtByzZfdkSB7x_ke8AJWaGFRgZw3EJh-QPgdv-Ghq1zktvaoJ9tSM9VHehvLIHWH8ByLPYkFS_Tv196zzXyXl_nruNNigdRTlD5-NFgFjQiP0LB65JPgCMlHtzChHQCNp45x_lVS0NXTf5_6--0J60YK77wsftget3BuKz0W6DtSZvkM5pzOCSv6oRHTFjIigWsxjo0WIqOmCalRrrKPFkIPWKYVlKy62Mu_XCXGw1PSrWygdenNIHxBUwK4zUFfh5EqnJ5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lVK51kC-qxIt9-X0jmgnqqgd776EBNay520axaG59Zwwrm4NLmJu9_0Kj5ZOvD8VBSbIilcLD56h6wJYhQzPMIkpctIWLDCJjskfHBGQUCO065IO-i5_hiy1H9D79cjhAk7dzmoo7kzmnwmEYyxNgV379e_QJgO06hrG870I4GoXptlOrNj3T-ko0dfIdR_28SNPiCSkTO28QGXqbAKmG2Z2PQ-f9BjPY5OfsK12cbjKyouyTtv81c235TNwG-ckmW_XzlJ7rlrW8N4V0cmPF9cjKA_QRI30rK9spgtbz_ZE3OPmnLFToNE3CkKqG3oxJXOriT2m5tk6DGSob7Itcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TKRZH7uK26WEbuxnDXmrJ_lRxYACi18rQmxx4SMnoag6ayqzyxeO5xw6Xwqdx72q31JOqMKqBtUKQPf03zdcDyU0D4Vwc6pMuru78KcIN3SJXhKs_8fyQgC7fWOaSOaK6VRySvRfcd33CjUzSKFEOtXWOiEwBy3ctTp-znaHcDJYTW7thtRXt7FZfnD3qcsZoDhVTEz2p7eMLiuScjxwzGewbnAQuLV5CRAqBODKPW7xQoAPZnACJgCJ2w7vIbKqEpCKHGrHQ3Y9TH_zb7tmNSHFIjljJop-xsTLRU3wI1ZH2KdInZVCKLCxsdUbDdq0faOAkGCR8a6fkqExc5mJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IiCstz9a7IKmapGmHgapEeU6HE2SKUSGXqMQMTRkgsxxEcmBMribNbiSBd8zmXRaSrhkuUIMJu5otxo3NmV_OAxp-GbgvFBBFQmmnqFLJPIE8LvbSOaDnUNsCbyrswdLG_lbftG6WYNuPvkQN-LLJu6G_4fQPTOi24s8gCm4RFFHAdMtaL8bTpoGa7CNK1oaquWo-QXwEZgDiLw1Db1QwHjOyiyXgyaMj_80jeHD--ifAw73GM3BNQvK9gHd8xjwbGwuSUSiTSkZvLp4ngKFkzBLCZqgu7yYwgkTSTAA6NTTZQZouavlRgYcEXI-yLrXv63gKlZt79zrwbjpG0Cssw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=ZmJB8cVY06FddTwBVnjuVL7AcnXXPwrL8zcbhDAPNIkU2ypmsbslk5Aiypg6DZmzSd4cQuTh-NVlchd_FZPTI0NdbCC2vGLatc81oZO0lDSYl7zl82N0moYmR43yGNXg6ZQ64bgeSvNHlcf1GbdlSEewyRVgh7bhUBXErz-dTuljql4lHbOMFkqw0anKccNcDqAChsQhxo_CuDsnXtHEqztTLs0RDJk9kpzUoGF6-9r0S9KInfxpYCM-6cPcZYech8h-RzIbkNkw_Uaqj5_Z_xuGI-bAbJbIZhKPVp1Uv4RdjYQJTZRYaRY78BWf6qzSO5Oc-b3Env62OmXrMFNSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=ZmJB8cVY06FddTwBVnjuVL7AcnXXPwrL8zcbhDAPNIkU2ypmsbslk5Aiypg6DZmzSd4cQuTh-NVlchd_FZPTI0NdbCC2vGLatc81oZO0lDSYl7zl82N0moYmR43yGNXg6ZQ64bgeSvNHlcf1GbdlSEewyRVgh7bhUBXErz-dTuljql4lHbOMFkqw0anKccNcDqAChsQhxo_CuDsnXtHEqztTLs0RDJk9kpzUoGF6-9r0S9KInfxpYCM-6cPcZYech8h-RzIbkNkw_Uaqj5_Z_xuGI-bAbJbIZhKPVp1Uv4RdjYQJTZRYaRY78BWf6qzSO5Oc-b3Env62OmXrMFNSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k7sKTz8TMcGmnX-strphlkSflMh_9VtRgqHBZAQirSDO1T6QAZqsgwVEPRrs8lDGf2EZbYtthEIqxsKz8A19IX19kLiusZpzbXLSGqOTTMGDhfrxAIdNLkbKpBG4jFowP0WIEBJOVka5kY3SQcHy8EfU5Nw5l037cXNBSgI1rSvrwV4wjJFuh1QGnP3QZTgIIgO4G3ffUU97Ng8_jNAyc_CD0W854P2XHXpkd45azAU7MCYrNttXEH0WIr6k3f1uiQdRzS3Rmu785sxO8bS9jL7t13rRTTBJPkzZ7kjDXguHgfyNnVbh4hEQ1FAWjub7_a_omD0uglztJ14H-a0MkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZKDFmJ2u3j53ZUdpAb1Vwo_jNUtmLcGe3_juBAzOVrOoz1sKryfg8kLGceGgGscJluDd_0FXFH5KdMUUs-v7PC1Cyd-cn19wNmmQ0yEx0xUe8wHPlJnVYvPAR7LAcxaGf4VeeaqtvVEiBGgYILKIiCVpINcO3Npdlfp7LLxlvsshpZ5XGw96lJx8KuaLKuvWZQIfwDxvFj_whAcOomO_ezF3-YIkTkpZ4GWpNYWeLio9cAcPMj2m5j08b1rq8LTnpTHhVS4DSL9Glll45fq7zhK6lZ7b-ey-a1VaOUKH4taak-iG_VR2JQ21hPg6AWMNFH146KXAor2x9xn_PGwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tcok5YJdGuQ7eglF0rW2Ey8eA0ab-s0G4qysoxdzQguq1j90cJ_2B_17qLf6yHEaUrb5TgJssTR0YbgtmtnkoPmE3agxcvghGVfUfLHzfTIFJz2RKi_AdCGvPX8E4TxA6iDkq70b6jrn361rktRt-E0L_yq2MVbvpPXaKXxEEAj7M4fO8z-93Rmd0yPG8msvri5q6OZwnpbXuyVwiMm-72pxDtCIyu6KW7X8lEUbC4tfmmokA21dp0A9C364UYS68DqCU5SlgwO1yqbRwyU3r5fio8Lgv9sew0SekrwzpY_9H1U_VM0q5z37WthT04twKb04JN9On6aWvwcSbv1VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dWUh-EePBJ4BBZCgjx92v_YP-MWExJxcJYzur2TkCotpsWeZUfNFK5gXC6CVsyIiXB9n9SU1qklLh2cX09qZi2r2ZHX0U4LjhEnLihNQl69lydzBmSqvZYbWfzzv4493NfeShlzM3IVPDzzEl24WhqGWxDMsYgfQXlmbY2rkXaDW70sFz4h8d0YaqlckrdGTJNq_mVr2hl7qcMs-vY4myJEYqvArpuuVF4qPfFNd6qG-Vm336rzY7VX_KBVE606jeshAC7wpbvucuhtPVt3xLCo-5qK6hvPR_tbrRS3uYsvXDEXQgIe8Qo8ItrwNApr1ssh7jpbyYOyvKmCIans72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WtUAHLCrjSpgiAY6IrRqSJQO749ovgMEp4wUQnr4_w3lQqWkrhUcqG6EyM-rDRNeeTjrYinU9_1LPsnKAJlfHQMNqrcjHv-kI-Q4Tj_XOdhQWXJjzTGIqqJybu8L08Ss6tP87JC1PD8OYuQmyvAFAkQdWW4BGtru2Glgh7_InKMe2iaZzFuipx8di9J1oM_u08o71UAZNMh1TjP0_TgIJxMg3NHeijM_JKxV7Xi7Wi8veC7YGNED05bBSjsCPdCmrDK6EvpWP7tKJ15xDCI4ZjsqR7M3pZCdEiKK4nbnYEC2JBPzYVAxuIETnEEWR8bFj3JPMCbGoi1ek9pjdRagKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u8etWkY-tmLo70UQW3Uqo-w0e-6VvWQv-vh7li6Aaq8GLEXgtc9L8x2CacHMXfqQBMSWvxvTrdw-IIp5PNNszxcFoaItkjs9QGZiKtGt_h0UD7RHlhD3HJQ-Nn6Jo-UihyDBYEghlWp-gRZcI4lhhk7vITmcCc2uzKQS1PeIgTalMXMyn8dcH6mRyLFT53lcDwb5JUzvat5-iaAjjCQreal---5ucynfrDlLb1HbQCsXiR912HtKWsw_JUJOOpDm9S5kv7wiK3I81zdBr3DnZE-rHFlBSKHnbTsVkUNe1_g14qrtdsoigIrwf3vmYDVZRDUy5BvvegAGXpXQKe1hKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VWW6_hQfaif6QBqMC0Fgk8pvYUdLa7buzU-pJSlyqWyV0If-Y5Xv809X2EfojvXzhYdB67qGxOosH_X1f8K_2FZ25LTNZ9H9O9T8woYO9bHmK-fZ7sixt5nPIqllGsI7Yq-WCJBjigB-YfPAyjoebxzW6qNXsqP5Z2H_TuvUx3Yqwr_8uKMFMVCn-tlMOAR4dHO3U9MHsHMw7aVoceEqnMjxJ3FN6F3mgNSbpubN9-_de7jK62uVD5YKtNQc3NrcsnZu5UuO7N_ML14yPyIPyYBVpxDpP4VcFaTLXfKWrmJ1vjBJtSLIDfHTOCIXu8KB-AqVYAXQP4NGl_BJldxP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CW4M1HpB8546ZgAKic0NQuEXSY4bWZ5OiPEJlfhoOZbMmhTAPiIOSw6PLsJGGQPbWxpILmxAComSPK0ePYq9t4agyfgjpBJJWIZ_ypxwhpTelDlHoHlzcz4mCFj_niVeTa7JNlHLm6G4oOPdzz2D-JDhWMvfN_AFSc_GcdAP3S0vHoswgK7uC62aepMO92YIqSCM0BSRsZp3VjXmGidLzPfEy68lxQG7Gqtu8EZu4hyd4oACeq4mTqVSZsmbfS_w8jHLwvSRcUuqRcceZrDsLjZpIFMzE2vjeztkjAF7g6Q7Xc2tN7wB0-OnDPCvWtSRXDmaMqDjJt-F3Z19PjyYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XlZiWCunHhBVrTF8bIO2K0ccOzylTA0PM7uGpUtEdJ2o75N5wZGXbb7vzwR4oZzCHGiMBxJN1SRUL2okUJglXa-st3DKkVtPOI0lJPxQH3OL8It7HK0_iPqsGAHEmL8h1tpeqE-FiHTBFqs5gq-t_1QuCIXmkzZjfvwuPPAzhRsEkwO3pL4geWmVl-w1SPDy4e0iJYb9SwB9s8SVov02P3eYYaoBYwbY283jmGNf_U3K4ADVRn7O4eHBMpAsup1ccXoNUSLPYcj2EIXdO1cc2k8eOSXd6E8KW9Q0808hkDkQ9Kxg-C_UM9s6qodaa1utPmDJSLx5gJNlibH2X_NW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ik_RctZkE4Vp84pbdAC_TI4UwVe4ewDjBYE_LgK9j6ozBU_jV9rNXVg76U3qTPXzG1vG_-twWLowCdU-Ez5OiPxA4sMWqDioC-uiflloOWOOb8GVcE8xQk0F9o-UZ566Z1XIXSMRRrPWprj7IL3Q_HR_M5t_UH2ll-C9PSlQ684aEWzMS784kC-bBGWWUaReZC00OWt1qHOE4_MvcRDAMugPLxHFCZQwbuilAGUfgTfdyFcCpQrIBmovNgrnYzoqIE37-DcdT1f6vOy8jAKNe64fiVDN9k05ZsjcBg4V173FDpTBdFHI2o7V-XbjxxwS8t7htgb26QXM91HoWIbrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZQCFPyG_p_x3q0heh3sASKgES9NdrdnQwdEb7NlqNwIFVwacvOnOehv9UUpQdwPaM8A2uLFoh_dYIiljo2cK4okFuQVrhOM4vr4SwK7nslc_wOgcJtNutDfERAfxcXNbclWSvStzvvV7I13VFUVlolveZ9JxnE08NBwwi7DoEqX9iWbUsQiuATR9Ayfm6pH9dlkDC4FK2YiwFJRrYVQWG_XahZfew-O9nAE4bvsLDaFpx_3G8JoRvKpc1ulV2iTsrd8Mr9hB5w_9seS7EJIGiPtIgJZ-FJYZjwX4pC-1lGycCNiNm2R6KcbMILzkCkrOSjxy73hwVTS2Hbfzf1CXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=cBZgaKdfl9uBP-Xc3S1IevynxsqHIQci0gs-_j8006gQGOm0JPyT-4DABLILuJ8It8Yhkz1GgAFv8JAqB_s1AavYUYhPqlcajgX0IlGIx7wbVstRPZD0o3O30VsfUor27ijViwLYOMysmTpyz_mTkqTTMYtWhR02StSzcNA3m9Zz3u1qXLg7YNHcpz03Y36kxPoM4iv7vijzSq3SS00Ayvb1ComTiwT8wf7_H_DBzy7lnlwRYHjAv2Q8D0ja7XnniqNMdIAL8LGHHN4kgjfcZwAsHnnkeHBMwMY6i-SXYKXziAQGOuzusaf3Xd0SVbsRbVHj6rt5SECXtNvnfAF_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=cBZgaKdfl9uBP-Xc3S1IevynxsqHIQci0gs-_j8006gQGOm0JPyT-4DABLILuJ8It8Yhkz1GgAFv8JAqB_s1AavYUYhPqlcajgX0IlGIx7wbVstRPZD0o3O30VsfUor27ijViwLYOMysmTpyz_mTkqTTMYtWhR02StSzcNA3m9Zz3u1qXLg7YNHcpz03Y36kxPoM4iv7vijzSq3SS00Ayvb1ComTiwT8wf7_H_DBzy7lnlwRYHjAv2Q8D0ja7XnniqNMdIAL8LGHHN4kgjfcZwAsHnnkeHBMwMY6i-SXYKXziAQGOuzusaf3Xd0SVbsRbVHj6rt5SECXtNvnfAF_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drce0VURU6pqJHY5O6elZH_S8bYCR4vOm_91V3JNWFR-77nKvqI30StAUtSZ-W8Gx6Ym595EIiyJbQNBIIZJkCh8awmw-sc3V7pdwWNJtWGiZvKWh8Y2AYvCk2XscjZPNMiUG_OGqzIY3wIPEVXEE_WkAOr2XEJiDBAVajJNIJcj6uPFZsifYOG7BAo9NJFyhBKGZpOpzKcwwYCCeD7KaarJK3wG3ftnyQpF4z4nOE2XD9v2wJSe6BbcTH1gGaiLPeGlS3_btWDpnT-yxCv00bbKAWJo_1Wp-1lkTlevYASRdw85hyI-l5j13j1KDWx-n3O2_MqIq2TiSw8egPtO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDcl-8H8Yt0psrRG-dTN4Z9PW3Ol37Ro9edlg7EG0ZTUnGb1ieLqcoTcutNbFZBUV42UMmjaDbtXmaahn3yRknWLMpzCWgkSlkhtWMl1Cb9eZD4LmBXpI9drCt40KSs8f6si6_mzZvcooZOaJ9Kksfg9Oj_oQk0e0VxQlsUWS8mJZH6dbrgUkeHNcN65IP5EkJUXG9vTprsKVqgov6kFCmJcDBVu51SnRFxtDKsRL6EmPcj1rMI_VB5RyqPhe_io88n0daYbL3AvKktAjsALEgtmbnczAbAakcdIrE_Q0x5yedQR2O9rsIEtOO_MJisIv7XretCur0QpYoycsiD75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yml67rmCzsqkAi1UPC9OHmWy0Ej8tHlpcto4ITdiUONioAu7I81tKCaFEVuv0LDY9G-6k8KttsmsF0Upg7LxfO4cJBUm6AXxtOV1x3AFqjPnSZTFTfVbKMY3b7-hyzKSqZI_oxfG5Fl-D5qCpC9mO2-7oZngFlf2xowIy3hNaVTyEhUeSGc4bijHGeUVS4fwNj-0BNqgkrX5JR8HMkYV_4sakN0LWV6unV6v4wkhUSlq0qL-QEB8_gb76BcfAWJU2tPC3nAeZvCDQ8oZ4Nogw-WxDQkZbQM-2aEKZxnpjcZ-1HZytWASOPGUPqSx9p7IaOroTHzI00zoDI-SkTq8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=LDwJByOrdT47HPXl7AZVrIyxwE1kDQ4e9vpuzk2hrj5p8ZJ5LqKHMmv5CS1JFqIlU9zjfWv55fGw8k6pSlDfPUI7FSpTWWpVStFLL-bxoe-VNRnhDXdOsTp7NSZSy-N6plOv5Cn1KDpBrMH6aUDOVbcd5bqqXNcQ5awA9Koflot4ZfpHwI_Ya5gK82x6jZ2GHI6_BPegLdnHm4yuazJeNhU5TWpo4BOoUcjQvlZyHFFz0itS5ZRwuhgymtcRRk2mzIoK3zNQ3iBtNMFrnoQVo273GPP3qPKKKmKRo1eBzShZUkr5lBrf_DeT0nZhl7tydF1d_c95VlSilhAgBehd4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=LDwJByOrdT47HPXl7AZVrIyxwE1kDQ4e9vpuzk2hrj5p8ZJ5LqKHMmv5CS1JFqIlU9zjfWv55fGw8k6pSlDfPUI7FSpTWWpVStFLL-bxoe-VNRnhDXdOsTp7NSZSy-N6plOv5Cn1KDpBrMH6aUDOVbcd5bqqXNcQ5awA9Koflot4ZfpHwI_Ya5gK82x6jZ2GHI6_BPegLdnHm4yuazJeNhU5TWpo4BOoUcjQvlZyHFFz0itS5ZRwuhgymtcRRk2mzIoK3zNQ3iBtNMFrnoQVo273GPP3qPKKKmKRo1eBzShZUkr5lBrf_DeT0nZhl7tydF1d_c95VlSilhAgBehd4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=E9qKSmkcb5-8UkcsPVk-OBbp5N92HQpnkNmeTkQED4cgwzqw80jhp-dR8xJjQ4slJmTtQzyXusXQlCQ_xnEWb_DzXGvhdR66ksdEyd92XWPSml25coOBaoiauOqRNaWEFWuX_XIke0AdLsdRB-jy0AZkdoEEuTfM6o63RmoRVhdtphnQQQqSEUWtEVHlVUZZZ-mEF3_gtRvxMjZMW-rhS4usNxL2r8vE7-UZIs96HKBucpmVAY31RGMqvWh9xmCjXtxBNVMkxI92ch0YvF-CE9UklzjDB7bzAHRLDrNuHHklxD2rSn3Ltcb0ebzJ8xOi2vm46Tjw4_XelQgsZiohJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=E9qKSmkcb5-8UkcsPVk-OBbp5N92HQpnkNmeTkQED4cgwzqw80jhp-dR8xJjQ4slJmTtQzyXusXQlCQ_xnEWb_DzXGvhdR66ksdEyd92XWPSml25coOBaoiauOqRNaWEFWuX_XIke0AdLsdRB-jy0AZkdoEEuTfM6o63RmoRVhdtphnQQQqSEUWtEVHlVUZZZ-mEF3_gtRvxMjZMW-rhS4usNxL2r8vE7-UZIs96HKBucpmVAY31RGMqvWh9xmCjXtxBNVMkxI92ch0YvF-CE9UklzjDB7bzAHRLDrNuHHklxD2rSn3Ltcb0ebzJ8xOi2vm46Tjw4_XelQgsZiohJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZHqaGZinO6U8lOtrfCK1OCoRvhIJA3XZyCUTXXfAa-YAedwVT4YW0S5quixxh29quivboZDbHr2xuOP63ry8gtXIF-SHRklKt2uVQY-3ROn_s90NW-c5uWxfctbfKZxg4W1ZFbmh3xbcrz5QGOx8wt0ixGDWQY8Up9MLZzwJWzXZxrQPYRbwsXEzjoy_3fj4DMtzXtRGSNOfI4d1lL640aewbH1-0jjdSt7XnwJWfhPspjguQ1ZSzFz6YDHICh6VzeFIyFSCsuqjOiCDUDON9SSA0M4rDslsaU28Kx8Hfe8iBCOHIHqf-IYZn7Q_Zw7jxoz_eWqnh2vL3Qu_p6cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fjZjT7Pnx4vnpfUxitX2t0EFu5ncjabqszkJJ0nJzFl66ES7A5BvBNTGEkzQil04TUGXLGNfbV-aosKB-3e1ywoyu8oD31QP1Ku6I7zGbV1m3UoViLEaA-ksf4aNhE1nhMQfB0W_kvR_roHDqOi-DnnWu6XI144k3TVdULaVRbWom1fG1vHS7kyHjRSO46mAkHSots9hzIQsZ5peFOK65SYEsuWCIvl2XVRAB8-8uE_zudNCDnj3f51M37HpT8CnvwXmDnVW6YcxSavO0iT7aa2_tTwjaAsl4fbxlrAtfbBgCUHD7n7G_vKtom6DqhNRe1Z7HylIALtdExquOGZg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ روز جمعه در نیویورک با اشاره به حملات آمریکا و اسرائیل به ایران گفت: «آن‌ها دیگر رهبری ندارند. رده اول آن‌ها از بین رفته، رده دوم از بین رفته و نیمی از رده سوم هم از بین رفته است.»
او افزود که این وضعیت، مذاکره با جمهوری اسلامی را نیز دشوار کرده است: «یکی از مشکلات من این است که کسی برای مذاکره وجود ندارد.»
ترامپ سپس با لحنی تمسخرآمیز گفت ایران «تنها کشور جهان است که هیچ‌کس نمی‌خواهد رییس‌جمهوری آن باشد.»
رییس‌جمهوری آمریکا همچنین مدعی شد سامانه‌های راداری و تجهیزات پیشرفته اطلاعاتی جمهوری اسلامی از بین رفته و توان تولید موشک ایران ۸۲ درصد کاهش یافته است.
به گفته او، جمهوری اسلامی همچنان تعدادی موشک و پهپاد در اختیار دارد، اما این تجهیزات تنها بخش کوچکی از توان پیشین ایران را تشکیل می‌دهند و ظرفیت تولید آن‌ها نیز به‌شدت آسیب دیده است.
ترامپ در بخش دیگری از سخنانش، گزارش‌های رسانه‌ای درباره وضعیت ایران را هدف حمله قرار داد و با اشاره به تورم و کاهش ارزش ریال گفت ادعای عملکرد موفق جمهوری اسلامی در جنگ با واقعیت‌های اقتصادی این کشور هم‌خوانی ندارد.
وزیر خارجه جمهوری اسلامی روز شنبه ۲۴ مرداد در گفت‌وگو با «شهرآرانیوز» گفت هیچ مذاکره‌ای میان ایران و آمریکا در جریان نیست و تهران هنوز درباره از سرگیری مذاکرات تصمیم نگرفته است.
عباس عراقچی گفت قطر و پاکستان با تهران و واشنگتن در تماس‌اند و میان دو طرف پیام‌هایی ردوبدل می‌کنند، اما این ارتباطات به معنای آغاز مذاکره نیست.
وزیر خارجه جمهوری اسلامی همچنین گزارش‌ها درباره وجود یک «آتش‌بس ۶۰ روزه» را رد کرد.
به گفته او، در تفاهم‌نامه اسلام‌آباد از «پایان جنگ» و تعیین یک مهلت ۶۰ روزه برای گفت‌وگو درباره توافق نهایی سخن گفته شده بود، نه آتش‌بسی که اکنون نیازمند تمدید باشد.
عراقچی مذاکرات تهران و مسقط را نیز «فنی و تخصصی» خواند و گفت ایران و عمان در حال تعیین مسیرهای دریایی تازه‌ای برای عبور کشتی‌ها از تنگه هرمز هستند.
نیروهای مسلح دو کشور نیز در این گفت‌وگوها مشارکت دارند.
به گفته او، ابتدا یک مسیر موقت برای رفت‌وآمد کشتی‌ها تعیین خواهد شد که ممکن است مبنای مسیر نهایی قرار گیرد.
عراقچی در عین حال تأکید کرد تعیین مسیر کشتیرانی و بازگشایی تنگه هرمز دو موضوع جداگانه‌اند.
او بازگشایی این آبراه را به تحقق شروط جمهوری اسلامی از سوی آمریکا مشروط کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=C2rRDQeHWtr9BcoOwWXwrzwsyLZ5jz8h0_qXP7E1j2WQNE5XExCt_2JTo3c54CfxybDaUiRz3d68aEnN4R7Q696z4atyk729tlUKbJ7nqWEMO7CLdHecZn2CnDcjNcRmeczqdRI-_Us9K8K89CJSf6xkVAUox-RgCIdQ_0BgR1n2CDBNf7JOW1fvlZerMKZ2ZWGgRALe2ASmBdhB5llNWx7LyJTQo9wH7DbyPhpmjIIwKVc1-FuFycITPGBDjqJ7DjO3RjPYrTVq0uQUuVJWmhxRTrDMx9fr8uSqQ2JaU5YJ2CSq-C9t8RAfyBTkceuZu6bFYlgdRaEDxJ9G1TiajA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=C2rRDQeHWtr9BcoOwWXwrzwsyLZ5jz8h0_qXP7E1j2WQNE5XExCt_2JTo3c54CfxybDaUiRz3d68aEnN4R7Q696z4atyk729tlUKbJ7nqWEMO7CLdHecZn2CnDcjNcRmeczqdRI-_Us9K8K89CJSf6xkVAUox-RgCIdQ_0BgR1n2CDBNf7JOW1fvlZerMKZ2ZWGgRALe2ASmBdhB5llNWx7LyJTQo9wH7DbyPhpmjIIwKVc1-FuFycITPGBDjqJ7DjO3RjPYrTVq0uQUuVJWmhxRTrDMx9fr8uSqQ2JaU5YJ2CSq-C9t8RAfyBTkceuZu6bFYlgdRaEDxJ9G1TiajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=cpgKuxibbQPcY-uNkE3ayoWXjlcAvApDWSrrAXWnC5CqxV2FosW1RIjAaz-AbI06RkzMYvqzRZcKH6XIHFTp5wmRs-UKigSjrFISff3v3uyKdtbsbCaXhGTjsaIJIlvpAhijXb9-j9X4ddixCk0SzkZye47SOguAyHxdEyqywEzyw8pxMQ7SZ9RmWzpXhPc1NJBLwt_HbB9_ML4RPMYoWc3Chnte-y2H7cjrOZJqmBjVBdvhrlfeANbR5t4B0MHpQ1IuCdKC9yYTdGIjNqqE-jfERlvKKe1LDNK6cb5nlW7zopJW683buzeLZZSWbN45ANNj_yJKTCEbUtCiNbNSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=cpgKuxibbQPcY-uNkE3ayoWXjlcAvApDWSrrAXWnC5CqxV2FosW1RIjAaz-AbI06RkzMYvqzRZcKH6XIHFTp5wmRs-UKigSjrFISff3v3uyKdtbsbCaXhGTjsaIJIlvpAhijXb9-j9X4ddixCk0SzkZye47SOguAyHxdEyqywEzyw8pxMQ7SZ9RmWzpXhPc1NJBLwt_HbB9_ML4RPMYoWc3Chnte-y2H7cjrOZJqmBjVBdvhrlfeANbR5t4B0MHpQ1IuCdKC9yYTdGIjNqqE-jfERlvKKe1LDNK6cb5nlW7zopJW683buzeLZZSWbN45ANNj_yJKTCEbUtCiNbNSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=jQVHoGfLO1I0zFFEtBWaI1gcwdlf1cXN07FbSL1hApWjeZ-m2J5H0Yz9bgmdWPKVI6MwTT8bSPhXivrihxwAQOobj2anyoA-lIeXwY_zzaPWgHMybe-3ffFF5xSUBXTt4xCGEA57sqWGJajrH_Hj631BF5SXrSQ5Dgm2LynXgt85ItAruKnaP69HB_NaVcavi2fDyi-mbzkDEPqCB3m5BixXL0UR3IwY1bM45mGipIXVr2BoyYntXgQeT3TLqEvuG9Wjhk1FfmAKr01SsabMk5lc0Ig-8tUd03l4hKssMk9QfNmDbu378K9r3X4Pw7gHcNHsUAL0aE1svYeMctePx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=jQVHoGfLO1I0zFFEtBWaI1gcwdlf1cXN07FbSL1hApWjeZ-m2J5H0Yz9bgmdWPKVI6MwTT8bSPhXivrihxwAQOobj2anyoA-lIeXwY_zzaPWgHMybe-3ffFF5xSUBXTt4xCGEA57sqWGJajrH_Hj631BF5SXrSQ5Dgm2LynXgt85ItAruKnaP69HB_NaVcavi2fDyi-mbzkDEPqCB3m5BixXL0UR3IwY1bM45mGipIXVr2BoyYntXgQeT3TLqEvuG9Wjhk1FfmAKr01SsabMk5lc0Ig-8tUd03l4hKssMk9QfNmDbu378K9r3X4Pw7gHcNHsUAL0aE1svYeMctePx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hzMe-KEykpeOpcCiyY4il2ifWy1umaS4kINQ37mG7XfngoIB1_TXV7Logp_--rHNFt46RNcwawpgq0hoj6GuVXUIsTI2xzOTT5raFcypnRN6zyep2bQcBvU1DpOwjcrVcuIjjz510MCEmj_HLpqq3HeDn-HowJP3ycDU-EZz5TBlHKjPS69AK94bxynxODa4HHx_0AtJx29Vvqs7ZOB8zGOEetxwzYa0OJa176dnbYE59n1Wyfgzg8Hs3Un1Ygoi_m1zf8C-4yCdXPG-h_V1ZuntIHlObtTwe_tHSTBAch_34DDg2TvQ3JnnGAqo4Wss_50UUOwxhtTR153sbzVIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oWLAdMmJLWkD1HzLIHku0bDZpcSxcz6p2ccMFdS1KaESEV3aTlWk6M0O_lI3a4oZguMKJL_8zMzoOBiHHtB_ewql7aX8LQpDP0e527IcvIAKdwOt26MTrj2Zy3H-WYpq6VWanR0EaBtgZqsJCGy8IEBj0rYhS6G7JbrDoTcXMxbqa3PBcc2StaE9IjdoxCDQvSMmu7mZui7ieqI4Ymz84Z4mLpLXG9ySbBGHwMBCimtuxy3_y-s51MjucyIMPCfAGYSvJ0_GWC43hZ_MvFqXO3n_6vsnWy6VYnSP6hfKFHlkFCJqelOUxiJdMhhvuAZ2lIgzRu768scSxDzyxCdlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=jC3M-bgmkoMZmKiO2vXmJk4egk-R58Ct7L2KbEULPT2OoWD9vW9aeGz2zRZ0kYPzUBaqwqWKlSsR8q30CLCRRsakmnOUzU2fDydl-RypZmFoyQ6rW-pEDzYRHIQxNCSeI3weV2cLFUVJX8hJ7pT6PprleRNuKLDtupDg1UYSQ4JSslnZW8PMA58MeIkv-C0oEi21ECyTb6zhSt00YwTGwYfQsjLUsAQA2rBatYK65GX3KAmXlb2T3d9jIBwvGp8c_u6EvOZe4hSoSyCRLOCGYuJxjDU6LRzc_b11N0JLjoKiTfDREDto34p0Q4sRrWtwS8vqmNaZR-DO2HBv0_9wBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=jC3M-bgmkoMZmKiO2vXmJk4egk-R58Ct7L2KbEULPT2OoWD9vW9aeGz2zRZ0kYPzUBaqwqWKlSsR8q30CLCRRsakmnOUzU2fDydl-RypZmFoyQ6rW-pEDzYRHIQxNCSeI3weV2cLFUVJX8hJ7pT6PprleRNuKLDtupDg1UYSQ4JSslnZW8PMA58MeIkv-C0oEi21ECyTb6zhSt00YwTGwYfQsjLUsAQA2rBatYK65GX3KAmXlb2T3d9jIBwvGp8c_u6EvOZe4hSoSyCRLOCGYuJxjDU6LRzc_b11N0JLjoKiTfDREDto34p0Q4sRrWtwS8vqmNaZR-DO2HBv0_9wBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y6mwzAruFUwf493mIjZoZ5Om9rSvFMKjDhPR7vyPaRsWbXQxLfd3-q6BiVdMW-lSnqbB3TV5OODEZNpKAINFCCYHHp3wYS9fCHE4Nf_Xna2ZnJZAqmehwAS2kaSIofN4fjiftqxafC1QP3GKIDCl3lPzYh6_mE6NhX6RvQLhpC7IFk_wqVJ9kTkQESxUP-f1Iu3Os1z2e5CiPpMUxjyKQRpGkkdHSkMtyzJjIcKANa48yYU7-oy2suTjzbOkAwFDLE9QdDuiRWyM5-B_Mxok-Y7wTyE-YNybdB1nRQW9ZQ5dNaiNkJrp4DE1n0OhOipErXuCVTMNmk2R6ld6-FiFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GoUvk3_RR2gbDeTkLtr7xpXYfzuOJsOCxOdDKhvuXbFAsclO9CxgrC9M6NdCPvOtGlNDoZ24sHAfA2bi2CzTugDsXmfaet7hEMD6YWVXkLqIArCo8J68QbhFAZ772SFvRDVaNM7-PuvKGdP7imYTnA8IAz7EfLIS6kI2y5TApqnU3ZNOIk1AVdqUc1oyoNP8av3iXYhw7REFcjX7ca1L1SqDtGO53qWzqO8crzjIi3BYClqmcL1Fm_k7rmc7xXtKmG8jpX5cdkn6RTAXaljbVKTqVWuFhFsNehY31yOh-GyweZZc3R2JuLC9TAPGzHw2panqNM4DbYsfbPPTh72PXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wAER_zYEq2s7Zavou4H4wJAgWMEJ4FvN50wRuDsibOXqZZQEdWL3RKjWahgzq48FvYg2ywqP_lFGktiAycSmsEzvXZjov2lQOouiwgV-b_4vN2RU2-VE8ii5iX05ggdLTOB-AAsEDHaQjcG24VfSbU56WWly0rueFZWi7DeCejtqEO-xoCjR842hYq7RT-Sz_Tfu5A5Ppt2m5saj7rKim0FT2_WpVMiRWA1pj_HVICmfThE6tJ4A2kG0qfEfBrsbJfZ82-WWKMAfTUwZgVWi-TnXHD4BQ6mCPe2Kb6iBQU5Eq9rO9Ec9KBUSWlJc4q4vyxZb24jpAS77ctNHaRta9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eeHI1yiL4ELs8qq-hZWi_L0YFVpbBOlGak0TgbVMY12ufDdW6r--DIIyC4ZQO_1eKMtUsr_BKOOaEoupnUBOPw7Mm_sb75D_mlINnuXES3ecDcuJDLqad689KQs-mA8OZ-mwrLEP3NS3IIEKVhw5ydH0SKYkO-IDcJjyURSZ82_pyOaynVmm9tkz9355BdQccX2WH06KttypRe8yFyxQNmYD_GL6-At7Q2Q2TvDjvISQQZ9-FvX0xaTN8ZDK6L3giflrVeBwQuQv5iFGAN3pvyyT46p5zfy457OwkTltkCHmqoUUTnf7NHs7ZcShvqkpMhxyx3gcae87pG0KwLgEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Myo_BMGDLF8U3sPZjnh9jDFGbllGj1JVA48aQxyCswkp1K_X0Xt2NTiHBHrsRGHvNlEhnRv62ZGvO-YJu9bg6zdWL0opm1Gq3rGZhWn8SDRxvvYmZaU95Q4ln2i3WAKK8dAg7nbCmvSxJ1MN3-o6cuRexChU49J_2wwwmUBOaa7SlYmPlVwHAdSU2yGtKOOkHit-EjpOJyg_acwmTvy1XpQEXRwIfD9qGRo3_nJsI1Dtgs7MWnTTYOPosDlJ6yP2I7b85REJkjSVxtdvGirk4aHQ3blxLelJrRIP6kDgjI2UnFIPijaPlJFzFtIGT4C7mnuGqNAHjtnvEtWSMoiIuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZh1YX3HD0iiIzpTDlYFBbPsX-zy_cSVILeoFzNrRsOLXcKmfbKQLItb7nOM5cWOej7cnHMf_NdFt7b7TLAzVp558tWHdCEVK-VCJNV8DYk8im2sugZzouWqWjQ3gP-zalq3YTiissU0r3axJ4uqY9MkSPRK2E_5rBQQRHWExTBuJ_Gs5fDS4nMiAbilEpJ6xu28rMQjctkm-rHp4iYgqWSWUY4yTgvbTXYuz0DkP2UnbdQpZwvi1FZNpPiFHBa60n-glJ6VvvmgnZ9CKhMcheA1CZgAIZ_gGnq2usDA6JRFsbsYbqXnayBAsimj3z1CdZhud8KYqSQ5LVpf6YLLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D9sVptLZ1YVR4AAyY0xVNvKzJFktMURLw2X5LXyVnPYFHsv1SraKL06KB46kBEHtiuI-LS0PZRt904ZGZCIE-pWb1zxZVj-ga_3pEbxibF8kLnR2s_g2Jn12mgQGlRLJRsUtXXw_2vQGxHegImD4PGjHyfslL_O54NGXCWBD0fIQoC7UBU6IpNV-B-esSXYht1Lr5Na4v6Y6Ywy8WZrPj56bYRd98gBuJMFXpQ-BL3dNRGFJsJxcHyOgn-9jNMGnm8NGAh6Uia8lPMwd2rlAxwNTv64pJsOeQy-_vA9N6Pun3xm372UwedkNU10JXlzuTBjto7fkSUvhdREOc_mqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n6xX2DblhWY9JI_Qhu0-T7a7X98zgPamQPLHC4VH1rRjo8-YBerZaiixTd-7PAT0rUA1cxUimNyc98c_QmaYBlU-rWDvbklcBz1gmn-M9II2CtPl13ug7ohwZreojz3rfDDed0G3GmNBYlaNGbi1PYJQid6COcEzv2afiN3bvFdwOiLYgeRChQ7q5F4PNWO08QV7Ldi4-hWC6pHSRFJQO2xsEyjX84IH7t4j5NjY8ueI2BJJEcAVjswRCcyeFjP-dUJCOe29cPfCDZiIoaOMMohGWdxdUOZQGctDZzZJBIg-dUrT8SB0ec9z0cOMyTKzmvBWcnnZrkaGa7iETvwkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PM9ddEewbXB9HBNI3oSPkFOH0z7vsFdAqdJv2Y2WxyOLhvgf3PfsQ5qbPd_-HCLmFp1aS9x928TZbynnF-Hd2q6TzPwSuULnsBazNwB3eGzBSQb_W45YzdFmdjXjklh-AXFvTPKXLy6oLBJ9fpPIBzD_SCllo_fELLJMtNE_JL4SRnCDFHkrEpJgCLRh6x9lRONJGYDYwklilHYA_AHo4jBfBqWZ2UV-fKnMtsUFBLXwu-s_FdywcDP8I-Fb2RevmKPogFeNZ432Y07aDcXvbgXlOrGJkjr6rauo702gXPPeYgj136qOfSXPl_1CH_Udss46nLwuKN6wz1x8P2W_Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAZZomJd7JfPIrTXehLTaqLKhn4CMMZA_q2DD5LF6esWXNmaHNGK9DhmC21qI2HMbvx-7noz0Ofeq6Kj5GYmc-stLxoEw8_LuxQFvPoT24h0D2acUasoPmRcAAT565Xhw7SKuFAMetHa9ZgR7gRi45Ee9ftXY_wFEBq9uRyTtpbQpR9-SvExsAtSNMHbfn5UOaVCsu3rQaFgfA60KwmXTtMbeNTURs4Gsdx5hp52ql1epFakySkYo20LLKoTkOqwIGpAV2O3Yi9BXUh5QdTh295MxmyRwcTUizddfgyeYaUaCoPsVCojuqsXFcpNoA47Ccgr8MGdVxp_HyiEOOik-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=oNZ-qoJwt6B4qoMgngupYT2vUQEIWvkkDSx9rgTATw-YxidGmKhfQ6720QPuUsHkE1_8OCv5o23yccTtj-ux4zKCS6HzOTfJqphTnBoZLf8YUGl8IeAk-OCyiqMUW7a2RYIBjNoznWicQscvyWHzzuVtynvL6RnK7lf4XCs8ak84L7WFFhPni6nqh-flcOCSbfCU-APZLvGgurQsPhhoJCBu4MGbgCTghEMl0LDyop-QbnzXTddG9iYOiUUUIasbb-VPKxjCzFFfDHRAayYo1QsN8152lyYWrbE_xbxV4z3cAffvwt6ob49nZy2g7MhgvrkWrahHndmmScWiY1LPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=oNZ-qoJwt6B4qoMgngupYT2vUQEIWvkkDSx9rgTATw-YxidGmKhfQ6720QPuUsHkE1_8OCv5o23yccTtj-ux4zKCS6HzOTfJqphTnBoZLf8YUGl8IeAk-OCyiqMUW7a2RYIBjNoznWicQscvyWHzzuVtynvL6RnK7lf4XCs8ak84L7WFFhPni6nqh-flcOCSbfCU-APZLvGgurQsPhhoJCBu4MGbgCTghEMl0LDyop-QbnzXTddG9iYOiUUUIasbb-VPKxjCzFFfDHRAayYo1QsN8152lyYWrbE_xbxV4z3cAffvwt6ob49nZy2g7MhgvrkWrahHndmmScWiY1LPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzosrMehtAEiKtgZo9JcH9zOIOAFCq-Sozy5C-U22Mm5DJDwD9d81S5A9-WsY6SS9_jXbxiLDBmR1oUjsDqmWURNvJZI-XzhR-6HgO6zmp-yHnTFij9HM0bKLB1crp3MYyUFqAHfQ7SkTSgXn9qUsQUTChydKVXSu1hKDWAjUuAcfwvVGTRENzfrSJQ1nEVN-NW3g1FAnbFfUN7a6d8gsuK4bzLr-qFLM6yzvPT5xdknjsA0-OatUisB2AEhRFSgPbQfWW-qfYnDmdJWbxjl-UebpqimAqcBo06vP96v_kosfO6Uqgz7snq6eum_oOJW0F-HkSeSU_niSRbgKldTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLLT3RsZ5GGYyS2L1LARFJuDK4OO9knZ4iAhZqfrkzh29AUtxBXojuIbu2XsXWZpWR9FDqnhdadobQ4rc-9RXt5veybse9NSArPMOnNGsWPxmIBuAmVxI5FAI2gomTMbvQqFhky3v1dugX62qI0HdYSHjQZvWxSRNXglWfCk0i2fBVVex4KD5uc7_DY8VgxXfEPDbovhYxik2chjsBQGZLo2k0s13YRPn_VNwjowmvzzCVXHw235zI5tBSPYBOlX5nYEC-N68AT9v3Xb0ceGDsB5-uUtpMNwQxEFIXBB-m21fB_JXmaxYHnBOzGKVQ8UvqrGNo4nFXqdP-iVOLxNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsNBsSjLXsx9DKXynQjFK9N8xnWUa6lef7xqxZ110fq0TA_isPGBb84kBmtjUXb3R-2G0aklwxHFAcuoR1jpfs03qq5uVfVdjpMju1VtDfO9vXOBJ087y4dULDHIIyohBpa1HacuQBhVQSP2ZaFYrWMebvrV6i5mrqOngFYWeJgci869p9MsI7Z0ONdF0-z3u-PlC7R-yCGFd882SRGzAJqQ6crwmCaigFeBWbQvNjCaNAqQwubhpXyo7L4xjIFJi0ZCo_codcwT9nPL5A9cNONdECyrzhGKd9gkYX9jwTh9WSUBfF_5MM0uTQCg6r4LGFNL-v6Pp6DzK22UwQC-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kx2qSfeC0b6nBej_A0EnLpwMwBJMZpDQfhuxYyuXE6qWigmTxqxK1TzfYnQSkFVcd7ve_Ws27oZTloWwSmCGbdbQfeGJd0r03MjuL4_X6K_wiW2DfmXFDadWvX0YTO_YR7CTe1yLe3kyShpUSYVO2bt7D0oa7cw3wqAyWCK6SvFNbCja2d5VMEUi5RGyuSGo3z6bP8dNaQj1tTeaXkI7XrD0gtj9wJ1Myb4M2SwiSqN41_TYNqcXFvezq91Pz0gAwjvz7N8u476SXtscN7IKry9bSjyRactbvuEV8tVF6OMaWA8FEeQLiL64HRN40EDOnsrXPCTUGTFJCV9WjyyR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OHg_1yJENX6v52NKKmA3RSpt2zZsfE9050JbfNXSJNhlDS_7XCkMYMS2JH4DDEJcGXhIs_E7BDqzlsbmIaYV4OlX2z_-fGSEaDDpSFgi40kU_2L3ZS_lee47E9B2gtteEwxif7XYLlG-FwKou-VsmcVxLKC47AxdAshg9yn5n4VE_K1sOyKR00u_AxFBuyTx82cjFDNzbtFBuOn_f6XqH4YzhNGwjXEuK1kGrHK7I8QSjEZlONHG4-0saeR1SFHwJYT26DhO8h_A2LKrqxROqSj-MPKsmrMpJz5MPOHy_0KJ157EroO6MnNJZ6K000RppD_6qzyOb6a6wCsdww127A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJLZstETKA1a2w5NbKIMl1wERbO7Rjp6pI4ZWrc40oRbo94jQKPfcArXrNtq2quU6bfj5F88KCzHpse8NKYGj6CiIHo0V0OeMC5K5f8OEfDSGItpP9J3RGJS0P8MT1nbsCi6IHrYtfELYRQ5ei7AGNzbmtnAslIPbCjyCF3mNddzig-NQ0xdf-DvHpkTFC9VwvK72Qrg0J69nqhrT1l6VX1l353z_ZFWXpTbXky3NK9axU1Hony-M7-G05J5MHsn24gYZ6zXc9uPynXlNV6GlLEr1wSiRIHlisWWxAQ9PGCSkxOBNdvI1ucecq3cYitbv_rgaZS1syF38EV1EI2WDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvY4B7XxiKLTWRG7gQpkRkbh_oUkJLaLAJ0kjwO8RriHb1phqBq2peQc_Lw0QiBFauccMXEa6LOOaLhI-qeecCo__51IwmT7aDlKWOzv2Ve-9s2Pc5hdOu5rlZ6LDpVGZIIf1kcWO-BLtbjaT1KJHo0bjsToqjT6J48j3_AxoJ45PrYldCNjxHIsDx6TiA0Pjr0JzuD_CU0TR4XK-7iIQAilMQ58S8r70B3jBCIgTL-Jj0NJn-E2mWbI8QmsqEaVc4SfFQj_sThU1Edm9KXeQkrUswJf8oHbFuFwBS5SUtXrVCTIqCLPUxj_ROaZdf6DpwJ3tXaMR2aGHObhXqWbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orT-no52f1rbEbyeXFiZ0s_d5NT4Ajk51T_QBYIUPQYJUQ2FuDXVLWidzgymvub7tcuB5clLRJaGA9OB-GbD0VnRbnpuMs2tuRMxcWSOIVf5yIbeydnzddpGk4DUlYrE8tacz-WXulnIOY0YmirVTt9PvsFkqw-7ejOrWjxjZgCGqCbLNRtz6Qgk7mu-tAPO9qD9zb0iV5pZ7ReE_YsTpdhS_dKU0LcSweU6pFYZOxutCod2GQUMTpgq1NvwqLuKS2n7H1sZLvTs_CBLZyH_UrPu_0wcxBi_vI0MIDX_UTkX4Usr3SxqdVEryWC6TGrvwk3AFg_fxpwQKYxQaMjLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnTGYsZd14iIJSpnLNcHjCToe-JNtGnpEAembOeueFizb65gDGZI8qohudCvxLjJoseuai637tVADuyGL_24Ebn7Fk5B15Od0SaOOsR0c8cq5ZDhXg85uOiBT7K0mJYNlu4H-a3gxvDnCFYlGYBWXrYWXmG--jKl0LFbKxbDEAfsacAdvwnL8vOdm9VrAAMArfgYCuTD3uYK4XRsu1kZ6rhW98J5lNIceMdC_bslFk7WHJNyUUYlJdoNV7jh9omj9ATu_qGvCOjJL5UUlb566EIgIQg03O7JJyhJ5xYZfBNXTCQlE3gH8gCIzSN8j-GCwNQrFbTjFmDRLcP5NaMblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOtL80iOVClI5643N1hhKqnK5eCp70X2t84Ua3NxX0Hj45bJB-_R3Cs_wMvRmgAs2-WDh21DYBcrIEtNRv1FAzW9NVeeg9oOvBwMndBwHxh00zCExwt1K9VXBEPB_xlX7jMnUmrNk_zBWeK0kaAmpqYRlpSiCP-kxOWBOXbFOHaId3U4TvpxtOENKkwjVaf-jwAbMpKSFcZU21uMQxoz7iCv1hpDVYLAz4A9FJGjpz96qTndYkYMK5eYfN5Hd2D_gFLPxcWNhO9rpSiGi84H_U-KDMtLcxZiA4LzChQFkbIZYm_AXzvag_bjxouYfRhokgwDwQRdY5OSSSe1BirpfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chIQOyBkonbSY-2979mNbnqDKzBDJ_gKq2H8xeL9iDT8TIc3LURRJ1S9mnxMf23YweLf1n7d5UzVsVo8zeWHMLDIx0SvGQEB2j6Kzf3-XZ1sNA9iC2hdDy03FwQWCwQWfsGAirU2Vb5ZI_WLquP1ywFdmQtjbw6bB9G2_mbU8qnUapau_uYcuFFTkSMi4_lueCZfWEK7-o992xple7rEV5Ph7H3xu0KLq2FU0iJFNSs1H13ybkacrd8Hlpi9Xo7rStHSdXk0bUCQhuO5MqhBTrnZXvrTBC1o4Vi7sDe8Ov6A9iwuLXOGevXoIASMtRtbZbFiYcGgA39sayBfygc7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9UXfPC2mtJCsuPHHtJ-RDMqEgwDD4WpT7iFV5T-mjDsvwsoCnrqxmNM7qMXV1DsVFU1ekW2vowOI3aNSVLxCawxKUH0O6504B_EJXj1wu0kaBrwsfe8jOsNuO3J1WZLqVTZxev34UVhR8NF_cDScpn-uviLTZAaIrLCeO5u8SsE7uhJqWALXHLE_XQzQ-oOIn-X8x_bfJtteS8HIXordGtRhtoPfpw5q2Y06QZsBH-NFSfSMNXkK2ifxzbUPg99o5Wyr3qnxlCWSrJFFFN_JFVlQ6W3qGczFCF053L4hJyKX-w8qzqrRYUG0Y2d5f6HUS4dRsjI3Z4rkeVOaGtp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNktMtvmuZrT9JeSSKG7u-aqovMr4JwhNNATdpXAQo-8SluehbiJdleBfSaRyWNOyDKK200P5Fxshr_rz4GF2EdHbXBBNrym0SwBeptNm0zWrQ_gNXqHgiYuwlzx7EVYdcLrnW3YX2qUrlIiOInT71GrSI2UNbGwbo9wroqP7PW5XoF3939_ll0-IlHxuWBlijqYCxD71CrYPReBicJd4RXlBZmOg-DYhnUrAcf2jf255NN1ftFor82SocBXB5nzLpdjKrfQu4HNQ9Kh0IvZ85r5ENDFZqyUFjXfkJBwKCPu9b7hXRbeBN1qI39tjACi5KeyVND0dRliec1jtJiN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASBni4lg7Yl48_NJfXlFY8NyPca9tChLuOFYbmc77nzM8IPDSKidedOpeUy0pN6KbfLxHPdDw0HGAz-VtU-w5eJXPtBVPR9CGxDR8F31XE8BmAI7EFUXD4jnVQe607qtwQY5s3oyUlH5yEMKIh-OhiR2Av4sdgwhbuEjsUeFxtmsWUZU-fMR6SdrHtg7bu1fAr3MTlk7H36BB0kZFLKZL9_UDmFE2MRNmH2IpMb8ru8zuWSHeRcs34az8D9bdcS2t_5ld2EURo0S_lhMQPralnxNq1mTWMhyA_3tDTH814PtsqHgLTJvSlYMQURNhgugr34gaBngCXUn3RHE0atfLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfNKde7p4rGp18_fpEHrH6dNN0Nn0NkYFY5KJJ5R1bZVpLwFBHKFCXboRKEnwxP1Bp42EGNfsPvupGnztlKrCv1ZTp-ZcwThCT-K8kqgI4pYb3W14w7Zg9yGQ6I_Zq1qv6dWR5ilGQx0Iu0ZOZ237WkEsHrsM_UJEWuwjj4Miq0jQxIj4XDeZTE2uPQHZ5b1LvVa0RJHGRiTlGoi2tM1NQy2lkLt3tu9FAvwXGJgj7H9U92EC47TjjzaaD4y-AgDM_uhbyRFWkBunuIfGPZEgeGJWIGk-Nj_k8KSAjGUrDlr6db9G4vGro6J78XdPvQo1LEkbZUoJjrUm2FA81iANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lU2Z1AbPB91zDYJJPeMSDIv047nJE68DCxNO-LBhqGHVlM768tk5u_E79Aj1J4AFU77ki_xV2254kSYtM_JQy6OLrxrEviyr5RZgXTsXTbgPzXK9-JQx7YvSXaYAJ3rw6RlNdBWz4gWGx_aG1ZX6InwBTqhvODzA8w7ph2KfZVlRyrbt6OPOiHoxux7ZMu5GB5z0xFu0fLoRKqNIDo2xhXa8Rp9ZhVImG1nvdHb-lK-auvqXbyfeRgVz2y6aay9qi07dtydriHtrVmtJOaQG3oKjrrJC47aKkv27XMZqmgsXDpehdpeHTb4mntkGENw5uz6wfDpUsied6F1EuWLLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JEhE2EbHw6VFm-hPkm4Q2eqtkkm002e3pLdDwqWZROMSjS6Ox9YrwfypsXZROiQlqJKdG-rKBdSMs8els410ZsHlUt1gm6TfFU3C0rXBv-NnXmU--jQEbh37XogikPHLh1stIO61GJGc_y0oK0R7XiPZ7ylwXHpM3h_CQUGCHY5sWXh8QxJy9ZCmAHpo3h-Zq24Y4Nz42fsuWWm5kZUw1q_pptoEc6yhNvCWDbC-8xijgcHvwNqcYXbw0r6WgtJMF6wnCgtTbKxdhrLQNnAUVzh_72Yl05LaPwnhuQx0g9qZsHkaXOwOKJPzdoxronD1NDMXoK6hSfbOgmFAGr9STA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OI5FSjL4uJER75hXlOGzXcArmlTPVrx_m6oDJ-hTrTVIGpGMteRI1HlIZP_xtWhjS9K8an5ih0lm6F__gxMhm3Ya8oxd4MglBk_Hvg6QzyvQ07lSm-6UIYEV_rgKCSOVpcaUejIgkbmK8Xg57PfIWzBpRXVmKs53StadN0PWrrwfPQQ2RWgCXlFugLo4MxmJsLb_5dwhYh3sKgUVb-0peTD5H4XFGRZfi7LBk7UTd-LLIS7X-2zZkStPxR7GfG3CJD2yHwchHtkqhvyitu8xWttspqryCh_J0_p2leDRbDMUpXs5jFjMyVgoyceYl6acYVx4i6U_AYIH-j5VmYZVmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRFiBFbn_yfBu4eTvSpRUqmDHeACM231ZT65iDraEpS8PPx_UuUwLaa_3VrePxC-gr8Cv5aiK7aXOjo9B-Mk3rF1vdnkbhQK87CyOlJj_FE98sJBuMo7mjhn4Y6WxlBSlkTZEOzJ0XvRjv5W6x7sLXuZJT_vof6GQR-mx85jcNAz57p6M9B5yK4C1HZVhNVmRS8FCIsnPRLsXZpr9bhcAewZqj0pqHoZ39AzUuHOfNSu7lqJTQoS8b0hysKKuIOjuNTG-Juowg73ejbbXxnXymU3UH_ZGR9eAoBN-n5xL1Qia3E3rfrGr-bPg4YL_ubhX-MSgvPrdINHDLeGXDdX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=FrGTolaSJc3M-_ZugZNNCg1_U1TLj2rDfwTGFQVsg5QZ4jdJ1GgD0fhTnM0_-aucrb9Sz-BV68zdDPHeS-JYjKnk9dzu3hEE_2CljqBqEaAW5j1Q0JE9FAEhXRUQEYu2pCu6yQS7hBIec7XkdfOdnjkvQlX-QQ7_b_zi3sKtcbj-4_-OYsMZuoFk0nVJCfVvneZ6ddYY8Trk-4UHq-TE0LX6jH8wbDe56vSuyt4Z5LNuCn6-Ao9ohJ0nUTjSbdZ27SpTt76R92VUN9NG0buCsQjUxb_7UcPFQ2rITu2SmFYncWZd_fE6x9KemH1iU1IIrltC-ekXeO0YybC3eA2P-J_-SUpOGCaq8v_lja-wsCJTtoE1VFikWuN-VieN0aO8xzWp6EjzCvUgtosq8gBbP_EHpupyZjVyZkCqjGptZCqj0u8_3l0aGKV25IWEr60YUfkCGRQUc7KYfzwCCozp7V6t30er-W31sV7rEDobNwiOSNKo2ku87qjGcsiqENHyM95hCcvKsH2s58SCPl47ZP_78_xlZc87YNZiG8EfWn9YZoNNVo-y2dPw2mUARp14axRpLIAZiDa8VXKfiX5nvpgE9242zaLaK1e9t7EhzvbvELHrVni-GwiECn_TwXjboadK7kiRDs9m1kaRPq0ozq35hGxXk3_eTck9C9860eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=FrGTolaSJc3M-_ZugZNNCg1_U1TLj2rDfwTGFQVsg5QZ4jdJ1GgD0fhTnM0_-aucrb9Sz-BV68zdDPHeS-JYjKnk9dzu3hEE_2CljqBqEaAW5j1Q0JE9FAEhXRUQEYu2pCu6yQS7hBIec7XkdfOdnjkvQlX-QQ7_b_zi3sKtcbj-4_-OYsMZuoFk0nVJCfVvneZ6ddYY8Trk-4UHq-TE0LX6jH8wbDe56vSuyt4Z5LNuCn6-Ao9ohJ0nUTjSbdZ27SpTt76R92VUN9NG0buCsQjUxb_7UcPFQ2rITu2SmFYncWZd_fE6x9KemH1iU1IIrltC-ekXeO0YybC3eA2P-J_-SUpOGCaq8v_lja-wsCJTtoE1VFikWuN-VieN0aO8xzWp6EjzCvUgtosq8gBbP_EHpupyZjVyZkCqjGptZCqj0u8_3l0aGKV25IWEr60YUfkCGRQUc7KYfzwCCozp7V6t30er-W31sV7rEDobNwiOSNKo2ku87qjGcsiqENHyM95hCcvKsH2s58SCPl47ZP_78_xlZc87YNZiG8EfWn9YZoNNVo-y2dPw2mUARp14axRpLIAZiDa8VXKfiX5nvpgE9242zaLaK1e9t7EhzvbvELHrVni-GwiECn_TwXjboadK7kiRDs9m1kaRPq0ozq35hGxXk3_eTck9C9860eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9LSHBW96ge82YxxJ-q475vPwJ3xVQqZYb53G8WdmhbOtehlooR-gsZ_jnuEhKf3xlbcM82FNKwse1J_9UVjquLYPdasMMKmqluCdr6IQ-2I5uA0WyrbV7R4tMcLCB4Fz4Y0ctPQmvYaTrlUcB-Ao1CClfWsCJFoN8VvvFEFsz2xyuZ-H6pjIpz7ZweN8rnbzrIobETsGYKwNEQ_1Qe8K94ZH5s7I4TbE3QhkU5iTIQOASvrZpjC5uxzASfTvhyr0WqZi7w2-jH08-iEsz6-dSL20_zY42B4qVBZS3RspGBxLBJ25LkYtVmq45IG9NTkKFHEslQb6_BSZjXbJxRCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jG9f2owkV_J36kjzE-FvHemvI_B8SEf6s0iV7IOfNOmkaqgBx0crp5-1kc1BOe4HqjWxxCuksN_YIFPukdJ5HsPmBTxI2KFxSnX7f6KzHQUlim0LEPTCZDo0Q21hrLH2012VxHex_YgaBTC87io4QRnsW1Ise4wx6xyfkiH91cm2mRgi0cRZnt_u889KKS7U8HZVAoLx2FH0OS2HOlrk3fEwpLs31HxbWFYYUWqZLncRHjbbWLMCO3ozrnlbce3dfcXH0LqRSwIWboIu4eP47brGIeHhjGAgv_xEkR0mxMeQBVnM0qifsaQQ3weHdKfKNto44YTQsmUUjdJzfz3QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYXRNO5ipknxyikUoIzKfh8cWXtFcyAe1XNkEk06NfW43N_mS095i56s_cfdUJUMIdmdw6vUEY0wA4_gIio0GPASrD75iHOZ4-kaWv260L4Ks0SRMsl70rSZI0gny9EN4ohBZ_XYxwhB59Rj0gpx5TCiqBKlV9pUj7pcK-vXgcCtjnKAHd17tYVRWQFIdMooL0aiME4EEj2OFhxXtJ5LPw8SY0JwbZCQaLLOu0_25pYaCUuvm6yCFJdAIYU25jG3cBkgRMTnCdqIoLyKR-IWCesGTnht7LdjDXG28S82PSwp5np4IrqrvdKbnYFvT4eVGUk9SBUVU6PGlm5q7mkF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mTA6PV09X_6fqIERImNB9hW-cCrPnivBeAqCBI4NJI-kSD3yduUJzO10YyV1EI7AKjzJTuejoM8EJJ9oNHCAsHm9NzH6GD-HV3RAwu0Y36rObUO2ZB3rBEM5TwyP37NEh0cbmInm7vvFgklxSywH1uKyLlKm4OEmpUDv1uiD6_LN0g80iMG9PvI3Yt-gxGTBB-8jHWawqMnelyG9Rv9l9_B_DTXTWEC6nbmLeC4_hC0x5pw9lA1o5L3NsLXjEekPUPUGJtwYD2SPtInXs-Hx7I_sEwT7ZQu0dmkOkGxrrIIcTD2WSZrHvdI6ctSBKlr8-XTHm5Lkz8tAZvToB0HxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LFv4ULI9_0arqxIVOOqZQiAp5dXpUgMhVDU1EqwbyfZRFfEpTA9IIC-LSr7PiMjo39PByameKu3fcZRVQlDpY4_cZ62nMt7VyeWBIkhcawUM2bASaWC2f3vxbOUQzeA-57sCABx2j94uDZuOhCq9swj1Zz3-2J93RZMObH_bYR6JhOm-IdbJ6ZqPpcaoNmDb4rxTGpgmUw5mlKXWPOTg6i8TLphTp_jBiNRd9mA4vzkQ6zRn9dAoK-_l9-MTFOVgGYIqpDurNwAH18vQOqyXs6wQpWthEtzxHzpYiU-urpNSztD4MHSEDyk1u2gSlWQm1Y_zMbgUf4elI8gft4Cfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/soo635bl1BRZkpprkmUuOzNxzRxv_xKMelSUkoSTO8y4iwM67ZAdxHzWpG3DfjpgGjnD3hx05Tu-Mn3SSpgjkQyh2bpiCxAK0X16jLts3W71R3fx7cHTyUejhau38ZiuVNrXrOSFVjyfLe2C5PQFfNpbpRt8mtX6qd0y7Tzpx-MWE6RTZsOUSfuqEqIWL4rRcYb5AxKvga4WhM2a4FMO7TepZZ5Bh4gcuoWTNpkv37DWGlTsfw8Y02CpPSDcydnCqJAm14xF-Iy9rJxX_4HE5uRG988Tduncl2vwjgRokG7voD9j4C0LIuTCzOKtQF-LNm-2pghwy4hRJU-aBYSlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XQXg3zcKAt-oPJnCpCEf75WSS0Pe9nhwYphRG_yWoz7yUqegoF8hSgn3BI1hatJuJAYm_iWkoqV3ET58UqVMC9g2u729JJk39Px1wbUiPWtn6dmFmlSmXIxnQ0NpsxI1xaEPAcqLg_I488liqqLCX5bDD-vIHhv47kUU1vFqHyj9amVYWOZtyk3jh76XzLDQ0V71W5mtwabyqzmNMEWQ0wHPURXqW5DFNV3m3HRd2uXXPu1pI_IIz9XmP8FN23PlX0eHSTAL8M6H1tmmTX1uurKgs8lc9omqU2Ub3HMno8JL5rejo4uBCuBoSAQG2d1km9y7wS1zyyzyADpls2y8og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=IVCl89qp1gEdT8Mcv40t17u6heCjQolGxj7Up3GaiUorXSfQPsBI_-mPwHO0J5ubwqHrEoZbYHxEgdd0_6bd1QqETIqoCHGZjISu9lt_ZrTrur8uySwFaf40DwsYZwPWO0TalLmME1MvFTtHpk1biBDhNcIMqVylg5fz7_Q4W6kYc4hjwGQiM8mOH3ausF1nYt9XmlMZdNeq6o4pfq0cG1bXOFvwKhFclVlaX5d1snjHrQiStN4FCZGGAAkDgIrs153oLd6IrEFRcTk1dKyJHFvHszG4se4xql1vrMlt_vbJ04i4W9SEZk5aS3ktCbMQ-01QnobRAeo_KJyI_kKQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=IVCl89qp1gEdT8Mcv40t17u6heCjQolGxj7Up3GaiUorXSfQPsBI_-mPwHO0J5ubwqHrEoZbYHxEgdd0_6bd1QqETIqoCHGZjISu9lt_ZrTrur8uySwFaf40DwsYZwPWO0TalLmME1MvFTtHpk1biBDhNcIMqVylg5fz7_Q4W6kYc4hjwGQiM8mOH3ausF1nYt9XmlMZdNeq6o4pfq0cG1bXOFvwKhFclVlaX5d1snjHrQiStN4FCZGGAAkDgIrs153oLd6IrEFRcTk1dKyJHFvHszG4se4xql1vrMlt_vbJ04i4W9SEZk5aS3ktCbMQ-01QnobRAeo_KJyI_kKQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5_uHTclnp4O09m-D-b-QlN6rFFUwlgH_-77cel1RYvpIM8ILtyt72xBG4mw6XUm5kQVu9_NXhBMhkJj4vu2HkVqFR5pmSfleSSV6mehdmSXnSUcjERxINvcfem7CPxqmr05uJwaDjonJrt6iGZPVfN6o-fkdhUHMys-qV-yaZwjL4iKael-ODwz8tVOEzR5ZYWfaHlEDPsGjPHe_wP7KfMmTccDrQvJdby-UromjGCOQ5o9Sa4aXL4oAHzeOgupR34AUYWpTiNdeEj_p8fwgfj3IdohiUEr7oCOCOUxYdDnIC0WAcM2BN88YciMN29y6Ej9A-lbCRG9ndXdTpShfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nHZbIfVNHrA_p96HIiAcEQZ-q7iN_o1tAjPi_tMUT3w9Xh3KpLu_FdcxOY72pyhytwwhjHs8sdkQ6ViPWUapNXF7XXbNCN6Hd5X2EbFt4KuW7y59WEMMhlu_hIozHUihDwmcwTMU099HEr1R_HvJew3MiL6ovnL8eBWlvfdQetwmhhbUmK1Vjc4j_01ZPcRXRq5a1jBWXgTpYpHCvsJXfSb-MZAijDUvy1z0ar6Gd8tJFyfBY9H0UkcwVQYkah_IW0wbuA8aSYXcUqiAm2XphabWR2omkH--87NiICPyk9xJjduJaVORX2sDWzIPbJhahvKaa2NVEyR0su8Nj6vMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a-8c7SJG1fZabfKjkxyw-RWzoapujpbenBlBjENRtI9W56hmspzu5W33IrTXMElDl8Jht10CN_p0HXW6mDMqVXyfD0cWv0BGOD6ObeQGO0IJgybcEsparCSFIBQybscPH86gcDaLiVX5hFa8n9Jdm8Y8NmmPn5eNvmkuUR6aYEs5hByNrImOmI4juMJkmBulMBzbkqRaEZxNtTFCDj7eYT2h-ChEZ_K8qeoIl8yIJdPI3MAsNIcDvTIlR6K-duRoIjybjYZwpNbVBV1vUOEaddfBE873ml-KcVBBTQxVI3uIFtm_IbzQvkdSFKoCkZaEHDoHsrVJQN_HMw3ZGU6bkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=XsyuJrGlAdx9b0x-Jx4_8f4mTMy3OBd95EIWvxLtI3o6yF__DG-ROftjG2-BbNAxSuD4648z3nnLyiUE_uSupsf1m9hQ4dComp1FjqjRanxU0ps7i29W3CtpR-JOzHLd8yYqYGwxV8rIA6xXcCFIKlPDyuidMAisQ5Vt3_KbkvpHAQEUPZJVpojMxT2bDARRAficaer-t0PrpOstAemplGvPhytty2hSyoKkgVwc6XlNIPkn39ivnlXjnLl9Jmqf5RpU_8VKm0R1hc9vmuENX-xnb7TfoDhCzaJdVq7fknZrOD_IMpFMpx4nR_IFmlV58Dc8A9ogmXSmWFE1pj1FkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=XsyuJrGlAdx9b0x-Jx4_8f4mTMy3OBd95EIWvxLtI3o6yF__DG-ROftjG2-BbNAxSuD4648z3nnLyiUE_uSupsf1m9hQ4dComp1FjqjRanxU0ps7i29W3CtpR-JOzHLd8yYqYGwxV8rIA6xXcCFIKlPDyuidMAisQ5Vt3_KbkvpHAQEUPZJVpojMxT2bDARRAficaer-t0PrpOstAemplGvPhytty2hSyoKkgVwc6XlNIPkn39ivnlXjnLl9Jmqf5RpU_8VKm0R1hc9vmuENX-xnb7TfoDhCzaJdVq7fknZrOD_IMpFMpx4nR_IFmlV58Dc8A9ogmXSmWFE1pj1FkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=tuQn7V2dL3rBmjHWr0b-4zBk8Gb3Eo1eAx2vthFbmw6dQV9No30LPUHYLmvsQe5s7DoWQsVlHg4FhI8BVZfwoJm8JayaE8qCOM2MwNEuME_i2cjpDxXqF_jczuDAxFeJeck1kqOohuT0zsiU5PaqIZxVY6vk9JGv6Xi8UV6lquM7N8swbJDmo9bTgjaBGTrtcnUrs-PQLtEmo-ZTPAI1xwDPQxvuOUD89WnSqPJ0SXqJLNyok3YV-5DCwSEO8fufSDlVCSM2Lb_JXTYqe3B0qQ1thyK7hcDDSV7QhGB1vnRo746Z1zVw2lZN2EytDoFpdnUonYntMz4AN5VpUq9fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=tuQn7V2dL3rBmjHWr0b-4zBk8Gb3Eo1eAx2vthFbmw6dQV9No30LPUHYLmvsQe5s7DoWQsVlHg4FhI8BVZfwoJm8JayaE8qCOM2MwNEuME_i2cjpDxXqF_jczuDAxFeJeck1kqOohuT0zsiU5PaqIZxVY6vk9JGv6Xi8UV6lquM7N8swbJDmo9bTgjaBGTrtcnUrs-PQLtEmo-ZTPAI1xwDPQxvuOUD89WnSqPJ0SXqJLNyok3YV-5DCwSEO8fufSDlVCSM2Lb_JXTYqe3B0qQ1thyK7hcDDSV7QhGB1vnRo746Z1zVw2lZN2EytDoFpdnUonYntMz4AN5VpUq9fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOF0yyLTbnUZ9cbwq3wFTd4WsXbTwtjC2zMfJO9Qq_tZ0mrDdxto2gTm1YsQ-6U7CgCgjjM3lER0xSP6yXqk9jwNLmHBmyElhrhLyHTIN_qFxyqLi24UfZaluX1_ZCdKfh0OKLqOHfHBt2eK0PBktf4W2kU16oQ_jSyAetupd0FQueNsYgUPPQ37gBGbLriOwknkWm8qzUfXrlTClNATOkqI2qtusn8fXEpbzT6gYuaTWp_esJfsRGsqp2gV32c9bf7fS6MT7_pM7VbeveaJc41L4BQR5Kt3ufeQbGaOG1Ggs-l3SVlXuz5jRjEuxIaip6fZAGkaGrO5Oxg-zoDJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r6ofgcwsCEKfLI9-oP02-cVFtBcx_MCP3OaTE8P0bESGDyUzmm-KnUcQCZNMx3Z6XHprCg7pcfznFR2PueLXws-7UeTtGnxR18vTnwpYiz15EsklUZX_gTXvhSRmLftASgFKDLfDKjNfYQL97xaGYQiw2lsuF5ZXALQ8laVYKI-f3hjF9XaDx71osQvPsVQUr2rpXSiZvsqLrR0nOfQTKIRIJ3nnTAjxsslAqrW2zdmcusYTe31c_e1ahO7nrBIIEKs7H31vL-FFVtJIB6B7lHAXIXjUNcwJAf8ZvMjdktlYuKzCDNwVftctHmjjvRN1z4cX3xMT86LfbHdBD19rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upXYh9c4p9KG6cpf2_tApQkYfNJEHjjP3eyg2VufxLgTav7CRD4novIbDJy0Ri1b7eEEtv4_t_cxW1ZttFaww-TyT28c-Q5-ZYo-1fPzhUAf4J0uuCQJ0WGWcX9apKNCcftO3DNvD5F9RiDslD_1gU7KKo_zVwoEpXY8pySPfXBYwRuifmWrPeHgpZWPhanrcM2Cbe7bYRGLRkRUk75CKLhIdrtI8hLtp88hPjlwtO282xcTaFz_9yjZKHGgvirrMtOHXv1wWBA1moq7B1Y8kl7h8twISJPTbO_n1VpIXelIyuTRYB5lRSpsejF8-X7MfgoZhWJzwzKron6sO2cAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ls_AFpXS3i-T65MkIwJJH19Si0wR83HQ_CsmCem2EBXEJ-Plcn2FtyZbbKiioVnnIDV3Ala-hTLWfh2dpScoaT6UqvUwH9tanPcV72b58bEDPeeQF2L2l0UVcMdNc8Z-jNFSGU8k0hECB218Gre4xCK3kbikZTw8WApJ-ZgJi8rcvrspttG9Hnl84fsv0SiieM-BFG2uuksrKdcHIZwY14bBqCPVzd2OX40Lk5SKQNO2Dy0xA9pUi3mbIgtuendwwpIUAThIUMPv7wdpyd3beQ4aSwSPqEZ3GWadGYMs6T13_E4bxkrKWF-2vd3lahd6ldYa349Z2FuzAlVwQn5jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K7d15ju5pqF4NdPTMjgxqiZe_P39nfXGaFn9xjzmpzppVUq1-L91hso6dl_wOgdiFpxZiUfl45AXm3LWrQMSidhO_RBjv3GQfpU8JU-AOMpGqkFHxzE0-y7NxqZXUW_55jzYAA3JwTIfTgzZgqksXT6M5CqFd2KndR_dwuAdCWXPDZuo3PcXTR0tVdX-igfn-dZ9Ujbh8ylp8IZuZTRlScSBU6CYRgE2_2ft5dT0Sc5K25hiZ_gqDOuwWLvA3Rom0vlHTcstFg2fFdT0gMy1Z5XgjXT_64i2YYwnB_kvOmatfbDmfaQgz2rRVN1SXjAiEOYvzh4yaaD0KelVIceIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZIMXRm0c7JoyzVKNOnm6TVuro3H_gGgJJ4sDoA9tpCdGrGms_MZCd5tN1bSvUweDVutGlj88ZhzGDVTSv1CjYx6jfAZUjtM6-1eJ7rcnSJLe4ukE9qgurMBNtfRJk9jBu7Bv4xx13jqOf6u0B5P3R65r0Jo4CMmxUB2sEA0i06MNvWQwSoop9goC_6uk2WCOsNec9QooYfs59y5FKKVo6RdptyLLSPJ-SpI65ZWlx1jq0a5CURJ1wsVgA8ZFu32iXbV9M1ZbxVICh-mJYry17tDxlLVEco1OZuLNVehV4R-sL9ug-csx7uuYkA_QhSa6LJ487akQM-IX2unJQOCorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oaMuvp7JNl4d94X-CYf-T5KmkJ_KO2wDMDPsz-pJTQBxivfhQEQ9ZqQigxSvUdV8-8Ml2KNerMJU_Mg-v4Q-nHtPZp7AFZ_A5JPg0FNraCFHCao3kk9bGgNiGLmDft-c-H5hjULoDZExz10Wnx0R_z6ZZ8oxNTbAFqF6-g83faLQc4XFVCcXTurEyrZHZ9C3JXAQPrCm05Q0Wd3xTw9_qwerRdhXpfB3oUmrOkqk9UNpVuxpiSGQuyIGKrzPsxrRVkw7WQhqfiqQQeNsAqElk0KIBAsNMz7e_jS86E9ImApE9kS50Bm6BHAPpy07Z-x5pqto4XzpNC2duTOt09Gv8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tK6mnRuvVrv-iLO1Q24F2hiPa1m359D6WwbQlevnAOC9qSh2TcZIWCPL4faqac6yBJT76SzJPDobm05TAmVbTI9zBJ_ns0-JQinZb7ZL9BnMV7l3NrXkttJxOInNQ6F1_PMJM0ZFLWBvmqd6ia1yKnQDK-oufvIGj5BazgSfs0YfVZgEu3lXPbeWO9HHYt5oSoONh3MjTGis1Mu9ndjHdnOzmhvitFjkDxPCPKzlQo8hTeUdVd2uhi7vFpyq8D_YVYuO-_CCp32PhJKuQsH_khKuIy2BZIrliaVduuAugzIGpRW-8Wgxe3M_hwBOMu_LOmeoJExNAO2O_qdcb2yrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=U3erltyDwif6CAXOBTfNHsVCgWcuNXO3fKOrlJzgbcDxSZzYQ28v4Mr33zANmSIuJDRn0lqjO_Z6Bdb39icvJCIKIzBXeEHAj2_VCxaGK0d499GzNLTcT5IdTYO04bzGt6ZuU5CJzePZh_4KSisTEJeR5RjuTPd1XEwuueJH58kEeElPh_vtKmtdO-lZTH3xEpHOvb-hiOi9RJgO6A2vEyohECeiHeqVc-OOx_5zkxRc070Yba2M32n89aYS9nysvUUEF5n_nh-ocsrKZqqqxw47M_JBbv2tTxNUQ7y2rZQ71MoKVuT2VQ82W7s5r8JbsfEMrd008hbHJk_11kns1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=U3erltyDwif6CAXOBTfNHsVCgWcuNXO3fKOrlJzgbcDxSZzYQ28v4Mr33zANmSIuJDRn0lqjO_Z6Bdb39icvJCIKIzBXeEHAj2_VCxaGK0d499GzNLTcT5IdTYO04bzGt6ZuU5CJzePZh_4KSisTEJeR5RjuTPd1XEwuueJH58kEeElPh_vtKmtdO-lZTH3xEpHOvb-hiOi9RJgO6A2vEyohECeiHeqVc-OOx_5zkxRc070Yba2M32n89aYS9nysvUUEF5n_nh-ocsrKZqqqxw47M_JBbv2tTxNUQ7y2rZQ71MoKVuT2VQ82W7s5r8JbsfEMrd008hbHJk_11kns1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AyQSTVY6roAM1F8imLdTeOrt4QWbUmt5s1BFdBJxa0TPPvpttw98upTV7oaYzGgqG9DaU4--4i5aQgMSdaRhuxkhFRADvBxsWPoY3o7nyN5RI2vKyMMBiFsJl1odk3snxNimKxEYglIokflEKwOWy8OoBvVDOEgsiLJ7xBd8nFYtQ6cpdw6GPWZXmhddWjsFAki7f3UQ3AE5prfm9ComNI4Yu09QqKcbIE3W_pQ4ECTzp8kpvbAufvmM_2OU3XmZc8nqaKNv2PmU6xMDS9kpaI58Ke_a3Sz29Eyy5p-_wfvpH9s1ZZQN5TGpnkqx9MXR6ZOwp8OGO0UhcpBYbwgnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CNfv83liFkDcpKfsjTkV-7j9XJOplujgpgVOzp_iWZUPzm7OnCL5lWsX3T0f_RTFrJ717DfgXDRlXEArwl2-q8BdoC65B3wV0s1nTLyQUCBLIBJABvPraQKzJkENODnqC39fp06pTQvYH-rcFczJNm1aeFMlM0OyrmAzPZAL4KN6V2-6ODaLaJhFvcHzJCnP31dGqPrPUtswHS6mvjfw1_azDNYa83KObQoeiIgMeaMWbkgBSSTHiIPfWKs4Fx4vrLHhEzk1YF0aCTD-LCCjpPb_hIEjM1CnGCxt-6mzBv1Gvwi9ECA72eYeqGP9d2DRozT6y2DflN4W-qt_U5I0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZJa3DSnPZ1P7bFmgMCEabiBMEIyBohkxzvnYbU7pV2CgnK0Kcz41gTUwNKAFAiGQ5o0mSLlh8wuY54Qeb4vm6_ViOMBpYAu0QE8mFwXpQUI279MsE5lLboJ4QgdSmR4-ZuIUORntCMOKApUfQCZUyomXGI4RlE_bB0zoVpvs2jRe0WiKG0Laa4o-k3eQ3-ajBo66YRk-7SfvsJpMeP_MSwaqLqdlSLbS3s46cmEvFAGiRq7tG7RevoFB1kJ8LZqPQ5DQs9XtPSA8tqV0gt7XaAS_RatDZHZhikxBMbPf6TICh75FnB4B4baWUQGXXTa65SygQwwPAgp2nUJ-jPHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=mANrYuO_wD9bWI1-PtNRqSCxkSZL7kcOToiZ8aiGOvpzN14ajoXD9lYNhCSeKBzMsiuKxVyQQPQJJhxFpoaRyzfBSbEi6y658GoKI0oBzMvjnebspQAwdW92mBl84DQE35jOmUSddHvR6m9EJ3N3oqHJjJ7nG6TW5OP9rDV7vvzZK5FKERjx9JLU7tRaV4EI0i_wXwilH_-SdriwQHooirMqliChjxzFb-X2xmSg6vBICRjrAJVYVkQSGJpEXEYyzor_LeWEUBrAOWe17Ast0ljSwKYq3vzayH-lQLRzEeA724-vA8KgJtKCSbsHQRii6npQn7zNG_BTG03rU8eqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=mANrYuO_wD9bWI1-PtNRqSCxkSZL7kcOToiZ8aiGOvpzN14ajoXD9lYNhCSeKBzMsiuKxVyQQPQJJhxFpoaRyzfBSbEi6y658GoKI0oBzMvjnebspQAwdW92mBl84DQE35jOmUSddHvR6m9EJ3N3oqHJjJ7nG6TW5OP9rDV7vvzZK5FKERjx9JLU7tRaV4EI0i_wXwilH_-SdriwQHooirMqliChjxzFb-X2xmSg6vBICRjrAJVYVkQSGJpEXEYyzor_LeWEUBrAOWe17Ast0ljSwKYq3vzayH-lQLRzEeA724-vA8KgJtKCSbsHQRii6npQn7zNG_BTG03rU8eqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-jSDp6-4_VhNTk5NDwG29SgHm3OvHHgdMNV7RLzEbH4nK8IvCmHPc8V6VEevMv1EqerxPb2hWwlk2yepvEpVH6KK-uVFVk2mk5PWOYNW04AW7YPm4KmpDNlv8NyuKQIsb33Z4M4qiuj3VZIySGmz3Rh8Cwj0lXBaFMYXLL3WeLOws3f6t8KGvVILTuE5SAYxgGhzJkVK1juWtaDzKFypNA7UwIVOTFst7lfx3AsLL4gqFokQj1IOI7jIVcCp7Zixlhew8YrdiUXhfuQMffy-4wkWNIiQOOxYRNEhSmvc3Poaq7WjePzDgq1fRvSFSiqZCNUvlMi2iEyq6bVIMdwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXISaCy3DPfX0qpo-lnW3qYHkxlgBlI97ZTVjqFrTtXGdyDMLUUWp3SBoAWupQ6YlktX8IXfRN8Fs1gQk7QOxnt3cufxACZfvBoAnixo9I_l9GgbdtxJGDzpbOaKuN6VwG584ksDUvl96Eso4JSK7VFmYS3rEtPLK3lnlQ_VZK0WyaKF-pqbHpDxUm9HkruXxbjjig6lZWdwHJVhOI4Pmwd229OoWbK2ynojaqm7_e2tKk8WG4vJU1P5ua7MZEFdGJH3dXinViviEJWxZlkTUCakt-ejun49A7JCnuf3s3qhObE-dCDcA0GfKnCq2GoTxigYWUUEsdz9uq_n1hBW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=cKZswgoHAE2nfNpjod8z-3GOUgEr_ah_FKyECcqPfP9WN8Klm59Ma3pSKdxzOfjcsMKguJm0A9PM_PXy8WE-4kbZduXz1ZGeep_iIiCJZYedPRmk0GSkOPC1GYj3EECIn3PJDsqATagcLciqthzI1vakUlemjGifZoX7FX9essRaRSuVJDUXzfIQ6Ht536TTKMZMgMNyXbKG_IsCUP7uoSOjcj-WAKe1grl5iwIakB03q1yul0wSVXZ1Lf50K46QA7IHX2d1pQ-TIdzEm1WgYWmm3rTveRkYj2NnskxkOcrnvGZNkW5vHOAAsIbDmoh1qqWsan7EJEKTyC87RoD_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=cKZswgoHAE2nfNpjod8z-3GOUgEr_ah_FKyECcqPfP9WN8Klm59Ma3pSKdxzOfjcsMKguJm0A9PM_PXy8WE-4kbZduXz1ZGeep_iIiCJZYedPRmk0GSkOPC1GYj3EECIn3PJDsqATagcLciqthzI1vakUlemjGifZoX7FX9essRaRSuVJDUXzfIQ6Ht536TTKMZMgMNyXbKG_IsCUP7uoSOjcj-WAKe1grl5iwIakB03q1yul0wSVXZ1Lf50K46QA7IHX2d1pQ-TIdzEm1WgYWmm3rTveRkYj2NnskxkOcrnvGZNkW5vHOAAsIbDmoh1qqWsan7EJEKTyC87RoD_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSkEmzAHGc3tYvNlFs7ZS3XpNGYoilF4-WSFkj4nQPeu3PC-8YpAAUPxYwMoYA0fv9yOWcDvK-0M20RL_DKcocp2Vr6BWqTtCTPLA5s1ocDCdqpnC4iucdzjzkw3uYmObJCtpkLZhdA5XiRAoa4NLRLVCBQMg0U04twxo3vs4IlOCB0Q68LLklU01ms9aV4QZ_qbKT-FkaPcSYPJ1Tts8McdW_3D9Inyt8LR5yWv0y-KC_QDBiTEYgz4m3Zb2BVCbtQ7CkewPvbQ3Ivp63IyN-svR-7l6LBMYQsn_z6sTRx2dJkuVezAAebcAoccqInCpBItksvB3xWlSuYX02EQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mpem1R9MT9T1175_UXZAGsU4AmGQ_tzzIVA57d_kSF8kRWAhbMF-20x0yvUZxZUKWl98Ouguut8fDSfyVoaeIcaP9wAUC2LVFTRb36Os6jDY3u5Ky0cT8pv77VZF8Zly7csiIpskcMa7L5H2_zajIwUOiPo1u9_ry5QK1DdqE_Qy_K1LT9SL2NYRZ2ogs_7P98vOb7eyTSuLnIRA3JQ4-Bfb78nVg90EvuXsmZKtrR5XldDTQyyWllTOxNUTee29Y9KYmy_6LuLMdOzxq_X4CNCIS2QAjb6ZMzeszcq0OwIrnPOv-II6yw8EnKtmMQOdreBxQTZRH3WzLiCKZ6t-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-UkQ3nBVLMnH1boDejqf1b7AitrfoKzPhAIXFfN1trKtjQ96GY5NgfIssd4Gq5-J_55RzjW4_3Z7aGGpJWtJN4vXLNT7YVLkWCSRtkv1FxV9au-KmVtQ05-m7hHaZewFmB6dDmLb1vps4S-pTvzz6cWC9OPEyjwsAmdN5UPXpnG0utPJ7WRu7cXiVDnwv3TYvj6H6oN84npe5j5VMUop7XyvdDWJ4OYyq8bD3P8ugBC6AVq89PombySZocuGmQB0JN7XtncdHbCqT4X5cVq8vDQ8QWjwffyeug0YX9jDuel4w4MxtQmIPzwSL1_PavlXvYqp5PTsdtQMDqry5ID-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lmBATrXzMwzVVYTwFPScTPe__dQnw08rz5xlZdixU_BBUjEVNIeskOJIa16RcVncshSTZ5wz7ulxs7L4Bbu6kmwqh9RCGX8QiZEtCajX8FqqUgj_zxMWJkd8v1RBukINfZbaPlZnN0kVahJqX8ZFL_Nxv5HtYdLIRl7YWvsRSV71bODfc9_3KKfqdDgkbxxs2ZTQA5_7TRvqjsFXR7IJH9PTxWB8zR34rD3qYdGHYHI2gWawATQqOrPiSDOCZLno6mRKWjKX1iRXiSiCSmxbfl-cOd-SZ46ktU4DM8k_CTlI0kkQdHSgaMxLfsAoSyjRKhe8azqGTuG6pkZQ5BXpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احکام منسوب به مجتبی خامنه‌ای برای انتصاب شش فرمانده ارشد نظامی؛
بازگشت رسمی حسین طائب به قدرت
دفتر رهبر جمهوری اسلامی روز دوشنبه ۱۹ مرداد خبر داد که مجتبی خامنه‌ای احکام انتصاب شش فرمانده ارشد نیروهای مسلح را صادر کرده و خواستار آمادگی برای «عملیات تهاجمی پرقدرت» علیه آمریکا و اسرائیل شده است.
بر اساس احکام‌ منسوب به مجتبی خامنه‌ای، علی عبداللهی که فرمانده قرارگاه مرکزی خاتم‌الانبیا بود، به عنوان رئیس ستاد کل نیروهای مسلح و کیومرث حیدری به عنوان جانشین رئیس این ستاد معرفی شده است.
رئیس قبلی این ستاد عبدالرحیم موسوی بود که ۹ اسفند سال گذشته در نخستین دقایق حملات آمریکا و اسرائیل کشته شد و ستاد کل نیروهای مسلح ایران در حدود پنج ماه گذشته بدون رئیس به کار خود ادامه می‌داد.
موسوی تابستان سال گذشته جایگزین محمد باقری، رئیس پیشین این ستاد، شده بود؛ باقری خرداد سال گذشته در حملات اسرائیل در ابتدای جنگ ۱۲ روزه همراه با شمار دیگری از فرماندهان ارشد نظامی جمهوری اسلامی کشته شد.
مجتبی خامنه‌ای در حکم صادر شده برای عبداللهی خواستار «تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیا» شده که به گفته او «تدبیر» آن در زمان رهبری پدرش آغاز شده بود.
او همزمان با انتصاب عبداللهی در سمت ستادکل نیروهای مسلح برای فرمانده جدید قرارگاه خاتم‌الانبیا حکمی صادر نکرده است.
احمد وحیدی که از آغاز جنگ و در پی کشته شدن محمد پاکپور، فرمانده‌ کل سپاه پاسداران شده بود، روز دوشنبه بر اساس حکم رهبر جمهوری اسلامی درجهٔ سرلشکری و حکم فرماندهی این نهاد قدرتمند نظامی، امنیتی و اقتصادی را دریافت کرد. او پیش از آغاز جنگ ۴۰ روزه، جانشین فرمانده‌کل سپاه بود.
احمد وحیدی از اعضای ارشد و تندرو سپاه پاسداران سابقه فرماندهی نیروی قدس سپاه پاسداران را دارد و به اتهام دست داشتن در انفجار مرکز یهودیان، آمیا، در آرژانتین از سوی اینترپل تحت تعقیب است.
او به جز مناصب نظامی، در دولت ابراهیم رئیسی، رئیس‌جمهور سابق ایران، به مدت سه سال وزیر کشور بود.
در حکمی که به نام مجتبی خامنه‌ای برای احمد وحیدی صادر شده است، رهبر جمهوری اسلامی خواستار «ارتقاء مستمر و همه‌جانبه‌ توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن» شده است.
بر اساس حکمی جداگانه، مصطفی ایزدی نیز مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفته است.
مجتبی خامنه‌ای در حکم دیگری علی عظمایی را به عنوان فرمانده نیروی دریایی سپاه منصوب کرده و او جانشین علیرضا تنگسیری شده که فروردین ماه در جریان جنگ ۴۰ روزه کشته شد.
مجتبی خامنه‌ای حسین طائب، رئیس پیشین سازمان اطلاعات سپاه، را نیز به عنوان فرمانده سازمان بسیج معرفی کرده است.
از طائب که کار امنیتی را از وزارت اطلاعات آغاز کرد و سپس کنار گذاشته شد و سپس در سپاه پاسداران نهاد اطلاعاتی موازی ایجاد کرد، به عنوان یکی از اعضای حلقهٔ امنیتی و سیاسی قدیمی اطراف مجتبی خامنه‌ای یاد می‌شود؛ حلقه‌ای که سابقهٔ آن به بیش از دو دهه پیش باز می‌گردد.
محمد سرافراز، رئیس اسبق صداوسیما، دربارهٔ نقش پشت‌پردهٔ مجتبی خامنه‌ای در تصمیم‌سازی‌های سیاسیِ مقام‌ها، سخن گفته است. او که خود در مقطعی عضو این حلقه بوده، از ارتباط مستقیم مجتبی خامنه‌ای با حسین طائب یاد کرده و گفته او به گزارش‌های امنیتی طائب علاقه‌مند بود.
او در تیرماه ۱۴۰۱ از سازمان اطلاعات سپاه کنار گذاشته شد، اما بر اساس گزارش‌ها یکی از چهره‌های مهم و نزدیک به مجتبی خامنه‌ای به‌شمار می‌رود.
مجتبی خامنه‌ای در حکم خود برای حسین طائب گفته چند مورد را «مورد انتظار» خود خوانده که یکی از آنها «تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن» شده است.
او همچنین خواستار تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت حامیان جمهوری اسلامی که از ابتدای جنگ ۴۰ روزه در تجمع‌های خیابانی حکومتی شرکت می‌کردند برای «حفاظت از انقلاب اسلامی» شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77802" target="_blank">📅 18:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=s8ifEWUHZaNbUT8WE9D3eX3anDytxAgK_gxLxVRPk4Hl15R0CJs2klDspvCHOc5LVjqcGGtTcUPb8fAoMN3ofRa7jHglZarUCtv3ZRgB2FND55yGTbyVql8jcyXm0cYV7FSyXeag6kUsSY4azm9UvrlJJfgvRIYaIjI7Ic84XyF2LVUP-yM_0Y9PFiFTXlr_iJpHvI7tvZNx0lhokuHIYyR0ZnunekxiyJ86Ah577eu3PpkMbK1Kdt_gc0GZcoKfPpuygi14pdKq5wLAZwiw9s_siH71gn4O8ovBeRVo6rPmyv5p4XKNYznbf_lK3ORRSF0wEZ8z84zclwwou0Sb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=s8ifEWUHZaNbUT8WE9D3eX3anDytxAgK_gxLxVRPk4Hl15R0CJs2klDspvCHOc5LVjqcGGtTcUPb8fAoMN3ofRa7jHglZarUCtv3ZRgB2FND55yGTbyVql8jcyXm0cYV7FSyXeag6kUsSY4azm9UvrlJJfgvRIYaIjI7Ic84XyF2LVUP-yM_0Y9PFiFTXlr_iJpHvI7tvZNx0lhokuHIYyR0ZnunekxiyJ86Ah577eu3PpkMbK1Kdt_gc0GZcoKfPpuygi14pdKq5wLAZwiw9s_siH71gn4O8ovBeRVo6rPmyv5p4XKNYznbf_lK3ORRSF0wEZ8z84zclwwou0Sb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4jI_-JYfTfQxXL_4EfmD2t1jKuz_ri1lFUfVyVvlH9GcK7bSlVHW75weCv7R3Nl6Umo7QgNQ6lU_t5ihec4OAO-ftIEdvU_P-7r0jCA9nR7OpEziqvulLDbhmDZrEBa-azDGuv3d1WhJhGaayodEaUx2WKoo6Nw4ieogFbfzRXI_mZmdRymZhVSnuJIyZ5sounFNQrmj5sgRhe10At2bcOdocVJyvbIw7hVgk9wlMK5RcAHKVDm10t27NdGq1TEL-X3eiyRnFkL6aMvFnwqfxDBGk6h3NdXIP-PjQ6eqJPssite2Ob3nY4FfzEasiRWu3Fce7_yEVqtcuN_IWfwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbAjr9vutgIKgYwyE6ZaHYwNfnurUY0RENfkLbKpDbSJY7Aboiwxm3nmWnfLL0v4kGKs11ZRp3RNvhZhejk571UhByPKKJgGDY2wJf5cRH11lA2ctbmYPbvvTVdEEd7Q8xki9rXyS0rQqcaAKPviYwys1Y1s3cSK8f5WUB-EFBEp5dVhLEGM-qHZ6uOf5jIfShGm0h0XjMLCAvkWh_-WYnuTEdMSsX_Oglg8c4klXpt2WsMaFjl3QEzp-rJ29yq7Ggtz_Sq6Nnw29IMeSKjnXziJxa00VorgNz_dZq7Oi92zutYvYcOI-rLCWYWWR4W1aueKE51YjWzELgan0F7HTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l7z3CPCzmyKZz_Yfds_bThVPFlGY-1bVKloWlCOiSqwqlO0-4NObllt6M4fVMzjCC6gz0i47cPkyrTqGlmRwRGB3Ht_DKixP-H3ZQH4j04FdYzlKrv3Lv6jDe8gV1pUUGGVph_vEFBwjodw9uG2KZZ-wm2lVcaRM83h1pg0VNesL6-YplXe28HNcnyFsW-LgbYGOTqvjX5gXokKjhShZNb1_TkBBGFbGydxCzgPxoX0vXYLGq9Uyt8FtpRQ3JK6O7dz8UHoAODME0fbR0DG2yX16avAefy3mtWLvc4DflZmFvj8g9xyBPCICzpAoDWlQ-ujwFIjze6sc8ek5QjKDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IjQMNu82hiqwjE0mDVEbEhbIJ5jGbY48jzvRspJ2-yygxRD5d7bwQTARV3_6xoxtao20HyTs26I6ZtDcDQTqOXTv1z0xj6OyTVzt8xnoYuLv9cWL9mTdmfpfy4SK8FNglM_Atm_kEbF8cpI6C0DaScyhYjiDs8c97wKaPBaJf9RY_8DBxgI-9SfCwdRfHGoIgYGFwpa7RPGMZnN_hUx8zeZrueUyiSadNJaCypmrN5gP5pJHsVFfe1W6h_-3lzZbmyDpBmtIHy8nRyLHlX5tM5FLeYakN0a0CsI_5cvqpMoMy2Y1jv0Bcu3RRGnxgym2gF023hgxY6qQzfHkk8giOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بحبوحه گمانه‌زنی‌ها درباره استعفای محمدباقر ذوالقدر از دبیری شورای عالی امنیت ملی، روز یکشنبه ۱۸ مرداد ماه، پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در خبرگزاری حکومتی تسنیم منتشر شد که در آن محسن رضایی به عنوان «نماینده رهبر» در «شعام» (شورای عالی امنیت ملی) معرفی شده است.
در ادامه این پیام مکتوب، بدون اشاره به استعفا، از محمدباقر ذوالقدر «تشکر» شد.
این خبر در حالی منتشر می‌شود که از دو روز پیش اخبار غیررسمی درباره استعفای محمدباقر ذوالقدر از مقام دبیری «شعام» و جانشینی محسن رضایی،‌ منتشر شده بود.
خبر انتصاب رضایی در شعام، صبح یکشنبه در خبرگزاری‌های رسمی ایران منتشر و کمی بعد در بسیاری از آنها
حذف شد
.
آخرین گزارش‌ها از فعالیت ذوالقدر به عنوان دبیر شعام، مربوط به پیامی منتشر شده در روز شنبه است که بازگشایی تنگه هرمز را به پذیرش ۶ شرط جمهوری اسلامی از سوی آمریکا منوط کرده بود. پیامی که بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت و تلاش‌ها برای بازگشایی تنگه هرمز را با ابهام‌هایی مواجه کرده بود.
@
VahidOOnLine
🔥
رجا نیوز نوشته:
در اعلام بدون تاریخ این حکم نشانه‌هایی است برای اهل اندیشه...
🔄
آپدیت:
کانال خامنه‌ای نوشته به ذوالقدر پست مشاور سیاسی  رهبر جمهوری اسلامی داده شده:
📝
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
💬
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔻
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
✏️
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
✍️
سیّدمجتبی خامنه‌ای
🔄
و در نهایت حکم دبیری رضایی صادر شد:
معاون ارتباطات ریاست جمهوری:
محسن رضایی دبیر شورای عالی امنیت ملی شد
🔥
اما بخش جذاب ماجرا
محمدباقر خرازی
است.
او پیشاپیش گفته بود ذوالقدر می‌رود و محسن رضایی جایش را می‌گیرد.
درست درآمدن خبری چنین مشخص، همه ادعاهای خرازی را ثابت نمی‌کند؛ اما حالا دیگر دشوارتر می‌توان گفت او از پشت پرده قدرت هیچ خبری ندارد،حتی اگر خودش مدعی باشد کلیپ‌های جنجالی‌اش را هوش مصنوعی ساخته است.
@
pourostadv
🔥
امیرحسین ثابتی (نماینده انتخاب شده برای مردم تهران در مجلس شورای اسلامی) علیه پزشکیان با عنوان «علی الاصول ۲»:
پزشکیان مقابل خواسته مجتبی (رفتن ذوالقدر و آمدن رضایی) ایستاده بود.
علی الاصول ۲؛ انتشار حکم محسن رضایی توسط رهبرانقلاب
با آشکار شدن حکم نمایندگی رهبرانقلاب برای محسن رضایی در شورای عالی امنیت ملی، یک مساله دیگر آشکار شد و آن اینکه مدتها پزشکیان به عنوان رئیس این شورا در مقابل این خواسته رهبر انقلاب (رفتن ذوالقدر و آمدن رضایی) ایستادگی می‌کرده است.
به لطف خدا، تقریبا همه چیز برای مردم آشکار شده و دیگر کسی فریب "همه امور با رهبری هماهنگ است" را نمی‌خورد و اتفاقا مردم فهمیده‌اند کسانی که تحت پروژه وفاق و با چوب وحدت، میخواهند مردم مطالبه‌گر را سرکوب کنند و مقابل دوربین همه چیز را گردن رهبری بیندازند، در عمل خلاف نظر ایشان را عمل می‌کنند.
آقای پزشکیان! حرکت در مسیر رهبری با حرف زدن نیست، دست فرمان‌تان را تغییر دهید تا مردم تغییرتان نداده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f58jRbfFnj6UYFcLLzMjVEZbdzu_-N3-8vwv3DKkz0IOxn5v3YsqFtgvpQxcEq_209WUs3h1lIAgdyNhoZR5mnR69U-aS_yO98mTZoFupHbL73af0PGXev3PRPh4gdCfjLQd1jY1Fx-zEd0EybSO3R3NiCgtlYwLwXJPGvhoR594vWFw3U2s0ThBp0pTyyLcxYJ3kxb3QalClufOqidgm3QKod_TmxK8WEPivfp4BTxoaNpgaDi23gA3Ob2Wk3MZRGKaC4vecrkXyrtt9OuWIz2uMnqz-jkBkJhCpdV1gEchAYalOtsuXHR7KJ_H895jDnoYKWhSOEl49owcsbeyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس: درباره ایران «داریم قضیه را کم‌سروصدا پیش می‌بریم»
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، روز یکشنبه نشان داد که آماده است اجازه دهد فشار اقتصادی بر ایران افزایش یابد — به‌جای آنکه دستور یک حمله نظامی تازه را صادر کند — حتی در حالی که این کشور همچنان در برابر آمریکا سرپیچی می‌کند.
چرا مهم است:
تنها یک هفته پیش، ترامپ در آستانه صدور دستور بازگشت به عملیات رزمی گسترده بود. اما او در گفت‌وگو با اکسیوس هیچ تهدید نظامی تازه‌ای مطرح نکرد.
▪️
ترامپ همچنین از اینکه ایران اعلام توافق با عمان برای بازگشایی تنگه هرمز را به تأخیر انداخته است، هیچ خشم یا نارضایتی‌ای ابراز نکرد. ایران روز شنبه فهرست تازه‌ای از خواسته‌ها را برای اجازه عبور کشتی‌ها از تنگه مطرح کرد.
ترامپ چه می‌گوید:
ترامپ در یک تماس تلفنی کوتاه گفت: «داریم قضیه را کم‌سروصدا پیش می‌بریم.»
▪️
«ما فقط یک‌جورهایی، نیم‌بند با آنها مذاکره می‌کنیم. فقط داریم ایران را تماشا می‌کنیم، با آن تورم عظیمش و این واقعیت که هیچ پولی ندارد.»
▪️
او تأکید کرد که ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت به نیروهایش ندارد. ترامپ گفت محاصره دریایی آمریکا بحران اقتصادی حکومت ایران را تشدید کرده است.
▪️
در عین حال، ترامپ گفت با کاهش قیمت نفت به اندکی بیش از ۷۵ دلار در هر بشکه، مصرف‌کنندگان آمریکایی فشار کمتری از جنگ احساس می‌کنند.
▪️
ترامپ درباره کش‌وقوس با ایران گفت: «درست می‌شود. همیشه درست می‌شود. مثل یک بازی شطرنج است.»
اصل خبر:
توافقی برای تنظیم تردد در تنگه هرمز میان ایران، عمان و آمریکا مذاکره شده و چند روز است که در انتظار نهایی‌شدن قرار دارد.
▪️
بر اساس توافق جدید، ایران کنترل بخشی از تردد در تنگه را به دست می‌آورد — چیزی که پیش از جنگ در اختیار نداشت.
▪️
میانجی‌های قطری و پاکستانی مطمئن بودند که توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان چشم‌انداز آن رو به افول گذاشته است.
▪️
مقام‌های آمریکایی همچنین می‌گویند اختلافات درون حکومت ایران رو به افزایش است. یک جناح به رهبری مسعود پزشکیان، رئیس‌جمهور، به‌شدت نگران فروپاشی اقتصادی است و معتقد است ایران باید با آمریکا به توافق برسد. جناح دیگری به رهبری احمد وحیدی، فرمانده سپاه پاسداران انقلاب اسلامی، هرگونه امتیازدهی را رد می‌کند.
وضعیت فعلی:
محمدباقر ذوالقدر، رئیس شورای عالی امنیت ملی ایران، روز شنبه شروط تازه‌ای را برای بازگشایی تنگه مطرح کرد — افزون بر شروطی که در توافق عمان درباره آنها مذاکره شده بود.
ذوالقدر در بیانیه‌ای گفت
برای بازگشایی تنگه، آمریکا باید:
▪️
«هرگز با هیچ زبانی ایران را تهدید یا به آن توهین نکند.»
▪️
«جنگ علیه ایران و متحدان ایران در لبنان، غزه، یمن و عراق را برای همیشه پایان دهد.»
▪️
محاصره دریایی را لغو کند و نیروهای نظامی را از اطراف ایران خارج کند.
▪️
او همچنین خواستار پرداخت کامل غرامت خسارات جنگ، لغو همه تحریم‌ها و آزادسازی تمام دارایی‌های مسدودشده ایران شد.
▪️
تا چند هفته پیش، این خواسته‌ها پیش‌شرط دستیابی به یک توافق هسته‌ای بودند. اکنون ایران آنها را صرفاً به‌عنوان شروط بازگشایی تنگه مطرح می‌کند.
▪️
یک دیپلمات از یکی از کشورهای میانجی گفت بیانیه ذوالقدر بازتاب‌دهنده کشمکش سیاسی درون حکومت است.
پشت پرده:
مقام‌های آمریکایی گفتند ترامپ یک هفته پیش متمایل به ازسرگیری عملیات رزمی گسترده علیه ایران بود، اما متقاعد شد که فعلاً تنش را کاهش دهد.
▪️
یکی از این مقام‌ها گفت ادامه درگیری به حکومت ایران اجازه می‌داد از مواجهه با پیامدهای جنگ، خسارت‌های واردشده به زیرساخت‌ها و بحران عمیق اقتصادی ایجادشده اجتناب کند.
▪️
این مقام آمریکایی گفت وقتی ایران درگیر جنگ نیست، ناچار می‌شود با واقعیتی تلخ روبه‌رو شود که هیچ راه‌حل واقعی برای آن در دسترس ندارد.
▪️
در عین حال، این مقام آمریکایی گفت هر شب حدود ۸ میلیون بشکه نفت با هماهنگی ارتش آمریکا از مسیر جنوبی تنگه هرمز از خلیج فارس خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
موضوعی که باید زیر نظر داشت:
جی‌دی ونس، معاون رئیس‌جمهور، روز شنبه به فاکس‌نیوز گفت: «این ماجرا تمام نشده است. واضح است که دیگر در ابتدای آن هم نیستیم. ما وسط بازی هستیم و مجموعه کاملی از ابزارها — ابزارهای دیپلماتیک، اقتصادی و نظامی — را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77793" target="_blank">📅 19:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiVUitbKgCAZZdt74pKlHqmYA_RG6ge2GRB2YqhMCesBx0bpUe4f7UaYzxyrxTwACEdhX_uo4SFgCuphRt8kirNYV0kKxk7x4QMibq75hrS3YD6mOIIdXammO0ONqKlcGVCqhU0Ddpp4QNasZini-6xQFPzKQUc8UJGJhPFoBAXIyg2CpA3I5kccCZsSlkn7R5UGxIzwRUc12JXR4XX391VoKaKZTBPNrJOl5QScJgLue59PwqPSLALWBl0GJrrW9I-mWybc8e-FaeSjTKWyE4KPLyuZsLRQZ9jxrE8ljQhV0ZZnIKBdY6w7RmLGASCvEONxr_gwDuvdp4DysPd0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
