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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 392K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 19:13:36</div>
<hr>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7yzuM_Vq_11Gi2HwTup0obqume3FrTnnRo2oZNFk3o4oaI88-xF6xGAiNafQFsr43wsbQlaZubkyz1buQ22q1E3ycbJMzP58WVvE-kNmB1osKiZbKqN7Rmh06DKQSLYSozvBqGbg4MLNdR7eDztQa1WIpjq1nmhzWftDRzLnI1iCvzayMZMxykQhgzx7mcqbtwcdsRoVvsyEqBBzevgo1twpN5YNyZf6iY8TyoOocsVGIOWsJhQN7EQUOAoccX9YzIFGRNJCdLePsHX8xc6Jkc439YJon_uO_O7lwJ08w6e3gOs6_79r6kco5FJVFdEEkEAdd4nr03Dq1AgHky-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRizUKVIekKdzQ5XNQdGnahA2_5udmQ4AT8JPuzHWKtUQl4FcDQw_4DnKfutsXiwwyCBWCrftOYcpVlTSw0q9m0DhZEN4ZCwjbKBBky2WAzjUF_NT6kSuERWwIseyJTZReTTKntgiesZLjBR812uKm3V49_wenCzlWszyGewPixGVsQtkoOhySCwkv1OV8tZ32R4aDW15SWNJ-FMG9qjvZByQq1saLw8HaW2mRn9mGYvPNzLh8BnUD1qhPUeg2f9ZmCJ9sXsz0pWHojjpufI0BKIKOdoR2oQlgKAdL50wrr-MDwljfmf88-GKZuOPrnCJNY97ZELFyS6ImvGP3Qstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUzfQZVh9DeHt4Zqq41m21n9XKP4o27yXG2jqw6H5li6UNkkWODjxUg-qEGM4gFxKKoHHhEER5N_XrtnpiKtlaZkM_1HNyZcEIJ8HyQd5VlnUwq7XGGjO44XoTB2F_-6BxPoDgKrFc4tuAtHD0D955D7BeMV5lWL38P3a_ZRGJj-buD99eYLYEXbcsZqZOUt7Yw6QpZ2AgTMHJ391bQdPBefaC78te0cX_13SCP7sXW1C0y1-Q-93pPeCceFUiEgx2aMJks6ivSHTvzu8Qtxs4rIVJc8RVdMO78-kSRAYzKpoBKikjl0_or4s00PxEVC0g_UHQjGICR09wKN1P0D-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQEaVbdm8aShl7X1P06dXha9WUZ1p_pDhFu5HZwVMWmvgPJim4jT2CqMVrpM5svmLacD7v3FthiotDs2sYjhVeYAzJHelBRNTyDdCs4tB9DzuD4iOYOj5HwfxS3tUSNzAyGJREwsaoQdgsin-AzS_5Ay3MopQ4chXTqLtOxf9A75zToaoaOCpjsqWZIalNOQq33G1-7dstPalBa8swS8G62fFma_t2MGESxqDzQp9NGnv4GeF2x23fgF38M4mJKp2xtCR4Efvnhy3s99KovjapCcDUj61R-FI-c0tu6WHvKL2l_FZ1EVdD0D0wMyTAEgT0WsoK1aTgqQDERVE3agkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZezubLZX1YI8vZR1YoCpCdrG0S6XCF85YnQUpM7dGvyFdbBZRwjViR5f6JIDaYN-jqqy64cMY-KBGYLl76nOC4olzxW2YvS-Q5XaYzvrG1aopqdgnMdt4T6vaCQ4nrmqF-ytFTWdGclde7uyKY6ODIvtLf2S0I2Go7KTow5BaENfV8SzizTupyNMmK9iC-9lk4tj9_voL-T_RTYiX2txxp1fPryD77NzOBBdLcvQnsV0mBXA0whSXHsf66nsMgWHDqf9_SVjwVSvCHyWgi3ebjuPolWXNqZtrvBVSNRJgR-9fWDB_xvvj7eYBkp5_jkKq6paLS6IxwOKuGt5qfz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_EqWEh_JmLDbzE64tkTOXEKXnUnkrw0xD6dPvOXxLtQ5OiYnMiEuwAGoN9_09G5ASyXZx5PCuPXLZJdoFImvwYnY7WA1WVi1nib0WAujBXmKpwRRtxasdAcSj-v4gt1SNmjHzDF57bFgW5UZzr9VwoiIvYnbC0ivxog53MRjwV2WRAeSI5qaD2MTcUUSijn3iQL87-sX-3jcYISQXagVMMv3Fphjsm8vYV5_dX2DTSAvOD25ErYwbmROdIBwTVm8rsPlXT-JZAqX93QaXT5dZZUcTkTC0DFcw5AzGOz-HtKwxW7onFOCEY6izxFDT_-GwDq60WPqHVl7OAvwZBFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=kujPf6jTiDH7rz2ddLxAWzj9QnP_PYW5WvaMZspq23VQw8ps5eUqhA2huZ9qD_bzzPc48GUALZ3X0ZAFp08yoZEYNhggXl4JMcP4IYUUcTxsxRmbkcxe3WhBF3GW5OlUjwWo8ET19AdEmVSXfhxoyrQQr9qxHCb1Zc6xvCxlexFi6ZwM5gK6sTMdOTcaINfmTsMt-kNa0FWyBxUvjxtL1wS_WNmbOVFXP7_hZKq0vjiJ4VngmLsE8-Ul_mJa9U1NqIhEwXPGotJiYs739KcsTLGsOr0BIvHGD1VU_thoft2twPhlxY71AW36fzMK_1ryvqJLK5RHeeWueNrTdrDppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=kujPf6jTiDH7rz2ddLxAWzj9QnP_PYW5WvaMZspq23VQw8ps5eUqhA2huZ9qD_bzzPc48GUALZ3X0ZAFp08yoZEYNhggXl4JMcP4IYUUcTxsxRmbkcxe3WhBF3GW5OlUjwWo8ET19AdEmVSXfhxoyrQQr9qxHCb1Zc6xvCxlexFi6ZwM5gK6sTMdOTcaINfmTsMt-kNa0FWyBxUvjxtL1wS_WNmbOVFXP7_hZKq0vjiJ4VngmLsE8-Ul_mJa9U1NqIhEwXPGotJiYs739KcsTLGsOr0BIvHGD1VU_thoft2twPhlxY71AW36fzMK_1ryvqJLK5RHeeWueNrTdrDppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8JtSqga4xT20xMPv3iCFAoXnTN8tW_8gbfr3T6udbWssmHMUws4z2GlFZs6fCEuKYuwrYEC3LESZW1bWdxF7mAGxi8_CJeuazpwQNCaJ1TMtxI3r05tcNvhHH9prEdB8YzzSc2insFM-5AV-XeAs-4_rcmaqx_ugrqwOJg0VUdFydog5hZCdkKzmYHEz6e3Bkuhvi7ae89ZMeD_ty23z-ljmuN-RM-cpmuxf6x8Gawnb8wqMpi_p6A6VcO1b59xGCzL5qJJ-jD5a1sPyxg0csJrzbLzoZgiM6ET-FLzOVlpLBXrOIJ-iz65GI22ybZI8BoaG8pSqYnlAl7zIh6V5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=kGFdw6fDmZXAcGCHqbAY6zPs_NcyziwwsxYX0YOD8DRTgPB0Ze-SNPucfGL4QTV1j_JKOSGOXuj4PxUvS1pjn9sKm5fUEf3NfZqW4fu29IrWqwkPFEptW_VzWRk19ORr2r_4LyRaHdI22AXqscVlnWJSDlo7Yjpg08jNdjaLKsyCF8YLaSFrFk7fEVgZECYIGEZ_ImL41kc8P2yRt7MO5kj-qaU11n1xN4fpx_YmAQ13CZ4RiLwDPB_30qZrAD8VZ9BNVTvqht6_QcBqz-wSWcfPKrJRFjsCcnokzbesWPXEf1JOjX91jJ2FMz90EDFEAaS0wHmqKGvG_-DQM8zOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=kGFdw6fDmZXAcGCHqbAY6zPs_NcyziwwsxYX0YOD8DRTgPB0Ze-SNPucfGL4QTV1j_JKOSGOXuj4PxUvS1pjn9sKm5fUEf3NfZqW4fu29IrWqwkPFEptW_VzWRk19ORr2r_4LyRaHdI22AXqscVlnWJSDlo7Yjpg08jNdjaLKsyCF8YLaSFrFk7fEVgZECYIGEZ_ImL41kc8P2yRt7MO5kj-qaU11n1xN4fpx_YmAQ13CZ4RiLwDPB_30qZrAD8VZ9BNVTvqht6_QcBqz-wSWcfPKrJRFjsCcnokzbesWPXEf1JOjX91jJ2FMz90EDFEAaS0wHmqKGvG_-DQM8zOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KswPZoadMJUOI7vjpvSJ7s-pklcV2ckr6CiHbYWkUJbyu3rhrzT15T03NjM_f_whAjBq7HARHSC2GPqcH3d9L1c5ULo0sxRc2lu0ZAWUnEHAjpoVK9uGBG96V11qt40ndWTtQYh-7KA0XSvexYrUANUgszlB-nvpdHBU5b797yAmnD44G6mQFmtRd2hwhDJRDcOuiF-uOh5MwzDZAHCr0wKGQ1CJpUSHR-Uu-248z2BjSvp-yqwvPyC1KB-yHc5fBKrSx7vmwoiwQSMAj7COFN42ZdWw2qriwknpNtrKkqvmFKQdsCpMNY_j0ehJ2-U27T5B5xxa28HvFbDSsStYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8CBiNpCKfiRwcFWsbl1npo1sqLMSIArPSm7VO0XCv-4CDPfx6AKXJqiljVDLjlVTIlhc819yWLsqSj6hclR3RuN8J85T9RzQg2VUXtOR15NrlwrJsFRmmJ6H5te-BKPfH7b3pAYKn8pp8c_RhoV8-bCFo-I4UgFw8obeO14DOczcm-EIL1vENm_Iy-RGc-0rulsViora2gRLbLDiPwAKLgxcYL9vyLlw1eUYAuf4Dy0tTTlGq9LJx3v6fLQbiK4bxXwrNyve-PQyAlIBZFG8W-E4uVVzNe8p0IJ5b53frCQSl-ySyUeAz8t3bnFXmdqCIJ4QSc1SEfEHVT01L-jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=MTNLyuLn5z79axGpwTySNPoOczCnsHPddoxDFsJFl4jqP606OTtnwQZjJNmvEQRM53MHrW6189lMUgjdexwLl3tn1PBENZMHaX8mjDGik9q0Bxeoy81VaGw687mw0VvIJ0Mkyq4BWVBzy20Edgz1HBMUqorsVf4QD64Mde2942U1iA0K1bIQsIIL_UHYeSH7ur6SAwasnSZ98sEkGugE7nL7ECBXtRoPlFizpk2Dp_YC5aJP3d5Wc5lhvQsK67ZjgLxZVLwzIOq0FHdjo0ymzVU26oXpbxqMMgNQwEMtJSdjVOSxCherBHrOu3x92nT5lLuUa_77bQGmG6y_1pSwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=MTNLyuLn5z79axGpwTySNPoOczCnsHPddoxDFsJFl4jqP606OTtnwQZjJNmvEQRM53MHrW6189lMUgjdexwLl3tn1PBENZMHaX8mjDGik9q0Bxeoy81VaGw687mw0VvIJ0Mkyq4BWVBzy20Edgz1HBMUqorsVf4QD64Mde2942U1iA0K1bIQsIIL_UHYeSH7ur6SAwasnSZ98sEkGugE7nL7ECBXtRoPlFizpk2Dp_YC5aJP3d5Wc5lhvQsK67ZjgLxZVLwzIOq0FHdjo0ymzVU26oXpbxqMMgNQwEMtJSdjVOSxCherBHrOu3x92nT5lLuUa_77bQGmG6y_1pSwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Ne1b6qeSd8FZ4XbVimCDZDV_JuvDrsoq8P36OOiby84apJcLQLzcfxQkzqTKBOqsl6gGEOxbvO2Y-jWTxquDOLF3hu_DJBb123XnP9ynCMOsRzRqWId_uDoj18uXlzL1iBqDVEVDFl4kte51cLUrFw8N5B7RfGnkKOiyJaM8Iwx7xSSKrDVfx-TqC7qnQiTMxIM4Fm5lzZGUXOuc7sRY6NydH3UI7EYU317tnSsnXmZXpQ5h45gGSdPjD-q87FVjEqApHpz5FoAPgUucF1vxcT81rX30objscuJcHSKdkIZ-sFBbI5ZjTcn88yWzdx6aYzRvteLNGP8IAK3i0ckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUgXgPSSLAdj9Qthp75kLfe406gd8zm8lUD0qFCLDq9NzDbihVbancAqlGceKV1QbjAWCSPLm-pWSCB982AWcj4ZtvJ5fKv2cFbj5JITXQY8hLAJIvT-tCH-sfq_iqYktgUZ_lAWkihGwzGpjwFxCDIxNxVPzpFus089sota3Vn9_tMiLNcEdZ4nMkOcKpHfxMjT9TatH5uIXKS4Sjkr1UasdfSHOAAPnnLlBLl9InmCeyQGEEWDO10K92aky9vn59Se-QsTNqe50BI13BikV1W4rtKCjeatSEnR0a1BlEMvBOvJGvrEb3rnAAS8UIzmb8myT2_R4SFDv52O5vqoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfSCZucNivh8XtU3oNP7ZtcgVm4LNBwIzBfgFTSyRIYoiYVoT3orOVTm0YLieSpW7CvcMS2rxEuNszuUFsEXH9B2_s7yoHclhPGtoT9ACLb-2o52qvwmp4oxgRUeH2LlZaVgMquQS-pvDlcjekOwHKnCzGmTHWf3emgONq0wgtBbD1Y8M3FkyeaqNYoZFDKq398ULsPiwUQHpAHX83Iw1PpWcfJp4JBYCiaZ89b1Z_LomInJnJytysvOE9T-wQ5AHFl8IVNBVDxGZhJF9jVgKDac_x1wWBBsbGqOCG-qrPEPgJ2K9Vsah-q4bxNhdGFe0Dt9MLILIYTyEE_ENMzBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrfBVJFM1OWcumRFVkccCILv3UviL1-KgiXGBzdukLM0uyjkUXiiMk8nf7bwe_vidwCPYku47JqT-OyGkARENbd1lkJvKnduEcTAoLa9aDIUQ4CF_chSCdYkcNxSs4cfy7AfjKgEY971Dgiq7CZ2aae8Y1FalFVjdXBiAzh8zp01GL4BO_tBLiDjPpNT5E7ue1KFhF1NzXaBsgk593UIqe1uAop64yZg_SBuSVKG47FmreampD1VbDlgG995no_n0xuURHMDz7VERKkKuQXCpa2in4A9RMzHlEbKYT1DKbeeggGxLU-X4-gXsIknKLJip-kz5X-j9zGXm7Rmpl_Gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsssX5qLjuVizx9YsZcjYQEtPMU-axmk7XBofX3ergAeEei0M_Mx2uVPjwUXkyLbevNjq70GyVYqakFsnTFICnvlzDa8GbZVkKMRhf-UPWQeDpQ31ABdE84B61g0swb_5dSQjtsLWx7woYve4xN4kcveNx8a4_F2RsEaVzLShUUhXXP_qso1xOs0tYRsV42aH7u-dbXuKS-imenNtJxTMxd_Nru8XyiqyHYCxUnFeaCQB7xth2ZKcSdv8fE7recNic2NoqEde4OU-gGQboIYeVmyrnuYnVgmV8zQGW2Lqqo0yR7hIy3lSnZm7mOz_EnZcmzs1wENqXFfeyB2tl9TgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkmzarUcy37GRuW-IryboSepL9zD-1MPJHcHl0cP7FYhiRRVey8Y-5VON5_pIZAU3NYETt_2gchJNLT0wpNCvvlG8RvJzFbgohCMaJnLJCEfs8CZTpiZk5Q8lSrH3PftBcZvDWCuALqtY2JacqR3EhpjZrRgOWr5obqNJTssPR2tJUGfHubMU3zKrM_E_IVpyZxbIjJIQNUGR5b4mzouTpbA_YzRFc2usbpKf2mi72rVRcKgUdAIz8fPahgjOQz6lxacRj6mJObrWL_Xifye5a8rkN8KZJPna_UnDjgx8HxEWLZQ_gRuljAoF4bmEYCUIqEbfcl98X52tPLJrkItew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS5k0IlrS_P1Tvrb7a_x8eyoAWKnoMbHBKcnu9CxTUafTOMhhm45LXH_7Fo1AiYE6dtg38lLyVM4M22WGzyc57nVliOQddpEVbqU9jMIv8u-GqL_DOltJFGt8JUMzGWJmXphOsBj1Jn1yioxwgX5kkrOl3Jh9HlGYLV0WkPKzQC4g53i0qCzcf7VRM8WXSBl2qNvMobTCgJAIyIp87LedEd-Hj4V5DsYNN6_loFWIVTkjVabojGk4OoRDLhxNYVb8pJSrOsZ8SVw-tf2LzTZiJyJHYP7lmhU0czwoLGpygIiinMnpkYqXP1QU4PFzGKtcF_gkKs-hliZq-h8OCJyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-ebxrj-W_JazLpoueCxwAony-_RPTIqCCXH2f0kvA2VLMmvK3BNU84ndKJ8XY0RWa36Hozk0jyFXtWNHe8UeJAMo0iyjXL_Ue577Fs61ilHmBlwIHN8xHbt7W-MxfIZrgMYbf47I8v7We_hWVpc5HudI8froNL7gb2c7nZvARdtBFa_Hcc5PwfVeh_FQGWrbkTEyDAkME4-ymANd8Qj9kFiSgiFZ9idIgbhWp_KMJ9l71Vm9zwlFtZbvwOFw1HMdW8BvwX7OeTTiQNYATegIPUhEzAS1IgjI_4WVHfAII9JSh5jJ9FmxYx_RC8Z0lcHR2ophGaaYWefIp1fSE48AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWTa4pK7g26Pk4KEnAX1vv4eb8CtM_MGVOYyf6e5xWc3RRH17Qzxebp1PgV-ZDUDaqAijY5hId4h0nSkYVXh5ygsHOp8BkqmkAiVIYFUe-1GOsJc_sjyC3eAK2c-pUoLvITrkSOM1DKm8B_swWQHi9vn7fXjE1Xin83kWb1IbuTQ2ESuof4ifKgnPDnc4tjhEdKOhhQBfLkbqAH0P1t-5zcP0zNfuXEkQ25973-6uiEYmIkewrXWd4pjn-a02hoXWdvx1pHH4psLKzOmDaM5KKg0JOfUFdWgBJtxarOjCpXauYF72Num9__9enaFQ2eYv1_TBOllVbVgOoTv5PytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pboEtNtmdQ4dEgkdkSKREXestPB5RFwpRKgygzfe3v_S_rqVvAv9Ph5CG-rebqqX-hUyFOxihM6A8_qlsNcWwvRYroNpjFhQygxHLiBSi_XKSd-D_H54Ji-x82x1k_ws9gPkMfFZGU7KjslV8TI6Yk4v0ttoicJH4F8UtYfKZhCX9ONd8Co9s9BIBMtw4rmFBTmvoNX8utacstyxIw92cr8hG7Zc2NJ_fbSOGixBQhrgxWelG3vuDdhpOSGL5kbM1TbyfPHXramak0T-6FNRA2ijK53KpMoOrsJ6Je1rYviIZ9shpmuuBkUZAGxkyKUAn5LPhIHoDDwdHxy47vK28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxdOSjnZzBuAYWqP5C1ZgidK_xVWwc68wgts-7zBfaUi1QpKWm9qTZ9I1my0lTo2Lvf1MMtKDLfvlaW_mgMCbAGOxPXJ6bGfrxpSRQmnFu4eIBtuk4otCS-Ci9VkUnpYTgnM8PdlAISGk8PGQ6bD7RQpu4xqfztDprrtWn9srk4cmBa7GPSKa8gwK87PCy0yU4nvn3YJA3bFScjiweRDV_xvOAW2w7EesRX49qrMGPFv46gVTYpZK1L0BGYDlc7V8jdGE5F8QmC-43WL_eoEKZWrshwrRuNGyd6OVj6c-akalLOTFds1eKvbsVneYZHaziP17-gfXuG2JdGmX1EVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEnTNAzMVpp_7k2aTTcQFk7oeiu1f9ygvctyBUqyJ6PnYIqjH8WSDNpu3QGHOY0Yuvu2E5MS__D7ZmKIzyE0c_mvqAJ9264Xxl_0LAjU-IFOpwLEc_lIOZzLb5ejBzru84OUMCOW9UZmYWDLoCLIleuaWIad7F8YyyT5ipKLllCnjum5TxrNHfCnR3WOsgioQrFbWVzBpGD3xMKAEoXNK7_YNNLVZss_i5UYPELOywmKuAJvWeMiIgMQ1itp9CCxz3il8jRxdWLEVKGSKIH-0929O893X5tFWE9rdILxPV3AiEyihLn_1k6RjlnbMx00Sks5WVkO4Ixof7Znp72LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVAa5BXRTBYjlsT9RKn43o5zQaZJ4N8Pnk4noVOoLBhUgL_HN7gs8GjSPDG5-uyXyltqb2J2NuWvhdPMRsJFtxEiiFUA7zhZy4aVB7GQKv3-JA6ncigxNW52k0_iSoNyy6V_3Z2f3uItpqvUiiaHatzAVaoaygwAQXO4pXOHE-wwsW3Tt2UQQ6ato-2raxjo1a3FRKvZ61YuTlZdWJVt9KNoid02263mJDSKT8sNAg5kk6ZKTED4uBK_guUIRDo8G_n7KuCF5oJp79WOCV4d52gGlKeCXxbQxm4DFF8fwPVHywpJy5WpcYtPkJYtK65m-ZlgYQTpwwiqsWx25rSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scH8ShAdeCD9RiC5lzvoDSHawCU5g55Swj7lC94vRh-uiiXcLKsom6gztmlRkB0O_0LksrWfu-QnTJnmj6AZht8Q5Ctdfy_tdjKVIIRAf0ob-m2oMh478FEdSVul4RSZ4pzpuN1d7HS1D9FcQxXgF6jXk-ZkbVr4bLOB8furlBNq-77lPQPdiechIcoFlzMQtTKEeZidJTfuWtPqEbNNC6T5N3nhNTvxz8EzJluMpCpyCK-c4aNzu-8HKv06m5jlWHTHjJj8rMvTkxYb5vK5heYICHH_JtD9XJVxrqgx1aopmcfIpIX3H078pQ7_erS2hy8boBZLfeqgo3wQ-dj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll9EkuL7IdocoWceTlaodEcn9fK6wHuH88evM051Tiuyj-PzlmEODelRs5ZqG9rQJKT_zqUre9lfWPSjMPJ7Kr2FxTT1jz_q15-zBQS34SroEBXemslozZP6X8kJirpm4tEHKCUBHRRj5RZwIwvb0WfKUgkHfaSe2ALurcp4NKdjSgnZcyJgUr_S--byCZPtfLNzK0gyWPCtchOmQi8EqWX5mjzwyMkrisArzFWNOHneg6dZToCJJQLMoxiFbENCXU7V5QZNzXB9rn4TXXeoD7Elh-SBBoXtUbOdA-heC7MtEhWBP09-k48uHsO_sahm89Ud3l6x2jlFz62VBpOxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXhm6rqbVOMki8trwzCMxJ0g9RXbn5fteE_dod8aFlfGWc_z8CiQLusoTTiOKn77Tw8EhICTwjjRQjJOHltPkfqU7-gp0PpenYN_zSo4JQWkx4sux8dqrfGHQISWO_3JW2vca9T9_ytpMOEiTtFlsrM4LHyPKhgBF4pjQRQ-9pgeNy4-mqT9Jq_MATOtlGXgJL3evvfhZ09Tks0hZu1Kodz5vNCWDx68Z0FCnSjxKnYH56qJ6Dwr5XAB_cvu6D8yaw0A73DsRu72eDQU296Xoe8w-oCglJMOtUrDLpZbksYnx2fZemSw5hfgERq-A-3kbEJgTmMiQInfrWunU-1vNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Pp1Z33V7uo_TxAEWETGNG8jluLvVNMvQgZ-XXiqa79PONKJRP7bbOL6eHIc8JQdH8Kqe4buLdAX4K0EpqgmqPvp8Dq3uhHXbY3G2yOTm80AgluMKCZM5FWzQzclobFcr_lPlwrxwI9HZ6141bEU1WlEaCrXzwgxz-4KrXAwmxpFjBq9fDta3OU79bTyeY1bqYLIYJWXJM0lryHvevymniwEuLHbwxPsI53gU007lxOM-LZMNz2F0VcHWc1df5IluP6kLh-naG7NRAHXiF70_wB4GYEoZkWSQZIhXWdoIaYmpIOQw3Kb5wnXXPJrg-aGmmuxC3fNxIGgmwPNGwKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcR_MFCiFCQh1m-jFR8XqTfFkcbzlXVTXYBGDH_WoJDyc-0J3LaAmyvHzG-3BGKM2OvRnUGQrprwcxBMfv8-63YEMxuWv4oVWZ8oVDiEBehsjcF5_9xaAPBgCuwKtevBhKM3YU-1HKg9HbKxsbyotmQ92u256O26hK19m5aplcuGqkqk4v2vtjuBCzeNPRRZ8MiQ6jFF2UV5KO_GLEJ3TnYcw5RsETmMefdelGRjoRpELAUFNZto3uAPvhDmAC-L6cRY451YZdjuXSoFHdHX4rfZ1JCLjeZY6DcgvJFPXQw62hpmVSGp_rFJMKtQrqzITnijdd2aYMF0LDYeyfAuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edUEARLR7BC2eSBZVcfEIvxmO0anx_gfo1yyO2CwbMDokkFVMheygb31bLxBCmI98sk-AShozVvwNq8XxjFA_kscThSVdOJSJ_5cydHr_ZuhNUXOVtucbZ7leMO9pggr3VBUkd7e2fhGboD0iDkeRfsRDPZEO2UTIK4-sW5iwkVtqLiQ38uncsxFWRIYUAazQ14GXV7FsJhM0HGplzN8by-hjgF7QJ2UTi11o_D-Opsv7bUlwwoWuQ6Xfd_6w49ECH744c0XyCcV-Hutv-yOZ6kbf52WPlFJicEXrrx4UrOAV7PHJJMrfo54tGQYeKXIRpIU0UsT7V5EBYp1peMTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIbfXvFJgpYY12qXE6WE5kRB2xjTYC6DiluQQjjSS1X5BwU1k5FvfDtvH0_CMKklwITuasZaqJ675jUZaU1SVNwxO9sOw3LJlrVKNb2aVrWtI6s0hs2AQj9zf97_IFzh1YEBCkDMaSPkGdVLnLTx-m2M7UrECNHcULEUwraR7NHYg-b0GPD-WmUsL-SvFZCkiHURutqU5_siRZisNSR0mezLLOU9nQlk1c48I1gr0CbpxrDXJ5pnv9uPvpLFnuzjCfqaoEMWc2Z-xymtZ4jd4lS6KdO3WF5sdDqXsMYfBh0PDrmK8DSTKTlqmCnHGR3OopShGGYsNJwgP2lgEjkobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf2TiU32ON4O31nFULaSM71_4qUlgR36sG6Q-IFpwIdrvDcIwjs3ds_PEaMQgxhzeOCfFEj4mKaSTP66MfAQOuIg6nvYl_gkrZBBuSS24HbBtJ4Y2mPtTm_lRugRbFQC_KYnytVi-g3k7-DHeW1qTfARrNiYgN380A_RmzBHpfke7B6P2txV3g7NJABMEAdYVJbMyCOd-p5pKOmuOLPcAuuBC2Br2ngLuT0Y-tXXHJeyRnaGpvOOXonE2i0qlp_-pg0ArTr29WaP32Ik4MVT2XSCjyrNJnvYU5BvUmCSJDieZyMxTuQGm0IPbx5Tb307-o76zrddTLq--DPXz7pH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=Zy12JN20RExeBrl4G7pixa2x6ciuCcORIGACUSug_m9Ce9_fLI_XgwY4iuMJceKPu-iWVXMitKIJQdX-ZsGwawGm89Mi9wrCyRs0IzKk_J4MkW9IEa2PzM53bRriPHiqYiBHjzbkXnx37f1C0XtBjhSgm9uJKoBZ54sESpmjiBIS-QMY1YzycTKCjXyEUumdpO6u5hWogrej0ScLVd7lgMWY4XH8zW01q1gPJ44rGYPsdfo8ILYAzE2I6Vd_IXqZZELuJ11gvSo2htXoJwXalE22LBwGVD7A34-jHshqjFKXRXSLae6B498PBOCtwrtyCYgB4-gevibDENM8AqlWdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=Zy12JN20RExeBrl4G7pixa2x6ciuCcORIGACUSug_m9Ce9_fLI_XgwY4iuMJceKPu-iWVXMitKIJQdX-ZsGwawGm89Mi9wrCyRs0IzKk_J4MkW9IEa2PzM53bRriPHiqYiBHjzbkXnx37f1C0XtBjhSgm9uJKoBZ54sESpmjiBIS-QMY1YzycTKCjXyEUumdpO6u5hWogrej0ScLVd7lgMWY4XH8zW01q1gPJ44rGYPsdfo8ILYAzE2I6Vd_IXqZZELuJ11gvSo2htXoJwXalE22LBwGVD7A34-jHshqjFKXRXSLae6B498PBOCtwrtyCYgB4-gevibDENM8AqlWdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk4GIb-Ou4pq1lqmb3ZCi4Qk3bC2R34q9-v7hgimuQDg7GWLBahUUDHcUKh8FKBiZWO3U59_6t5IfHKu0iElI89yMqL3XhQr9yHcYlKkkT9d9LPqeAUxplXR_RE5Ixn-WNGyxFXjWvDE441CUjHg-bFGQMFICAymCchu02bAASVYCDjBaZHDP2bxdD31ZzEybQsw9vePI6WHQ5xm2PHl3bqXgpMCd1dcaiZUvmUkqDe1PQmYNTd-wzi5QEkCkECY5FnSw7X7xLaVf2Uo6ovVMdmo0J7lpXxr-Fd7CZgPaSSjGsZyDGnu7IsJ7Xl6Fo-dFvgOOLaP_Vgvp4Me0uF8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=uA1U9JxMyra-PqwAy-0RnFJb94JPZKsxCIchG7Q5jzSP9SJPkiCHTw8NjafyZqp2yvKZrKZVEn2D6VgDuVcw9HnDalHzMTbmsXGlEwVR9sHut7m94iedzXc3f0kjeVarO_7uQdi7QUh0_QEDyCWximJNIBHM806VE6YOBOgQarGP66GJhsBTpXiA3vnEomEF3hiP2b4I8RWW-mVEMkKGbgDlZBKjZME1XFGXwEPXL1xF-62aJti3sCyDM86x9vhPcO4Cdbuk_ru7AnYmBPnIoBqa9DkgesiklT73LSyxMF7aDp_SLimRaX0B3dD0ejiGf32bbPkZC9wKeHFBi8hidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=uA1U9JxMyra-PqwAy-0RnFJb94JPZKsxCIchG7Q5jzSP9SJPkiCHTw8NjafyZqp2yvKZrKZVEn2D6VgDuVcw9HnDalHzMTbmsXGlEwVR9sHut7m94iedzXc3f0kjeVarO_7uQdi7QUh0_QEDyCWximJNIBHM806VE6YOBOgQarGP66GJhsBTpXiA3vnEomEF3hiP2b4I8RWW-mVEMkKGbgDlZBKjZME1XFGXwEPXL1xF-62aJti3sCyDM86x9vhPcO4Cdbuk_ru7AnYmBPnIoBqa9DkgesiklT73LSyxMF7aDp_SLimRaX0B3dD0ejiGf32bbPkZC9wKeHFBi8hidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGjnCWR3rfnUG_JiCQ-aidiGanFru9_G1KEKn-TtHr8BpCiApyMiKOB7o70Wqf_w8K5eYcItI7LlwspSdl2Nb-DLuobTgGkKW4AH3jSgU-o8pWZAS8Az1lJtzT9C4LbP_8_g6DDQ90U8ou8csG3aemnFjwP-XoBOejP_FayV87LAzBMQ_OoNa677xGuBJNc-ydx1BO9GtVEEFz5zUGHtFlXjPVG_IZNIhAdx9jMjoI7Qx4aGqCnEmGSUwuI0K_bazmhqcS9Mwfz4TJy6XlmOkv5MMLOZPrmSQd87xAGTWwDkpyIAcYJL_7Heu2pPy0dOhYRaZwkKMImT9x-hyLYSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=OA1M68WH1XSLJJqu1GRH-0N_swwos95lzWfMX1dr4ixqogAb4gwI8ufVlkofwXzXB5UuPyyhcKH31WR1YZxO6ULAyA2bnwP0suRjQbwiGC5VRnKMW5Cvr3eIfEolUAR_E6Z_IEexo93-hK17pp2Mu6l1sp3FvciNjqy8mrKx4stV5A2dhgoEg7DvLgmXgpFcuE0vRjrB3wghnjJXX__NgY8vc0d-K7pZPJ7TKhRwWea_eFysL0VY74J6o6KGQV0gdU6Kvm0OhZEDg_xzmbHqJ9OOzWf8bKs-K082D-JU1xhiFHXIFychREPYpbHUxoWiZghbdbd0wjriZ4NyyGi3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=OA1M68WH1XSLJJqu1GRH-0N_swwos95lzWfMX1dr4ixqogAb4gwI8ufVlkofwXzXB5UuPyyhcKH31WR1YZxO6ULAyA2bnwP0suRjQbwiGC5VRnKMW5Cvr3eIfEolUAR_E6Z_IEexo93-hK17pp2Mu6l1sp3FvciNjqy8mrKx4stV5A2dhgoEg7DvLgmXgpFcuE0vRjrB3wghnjJXX__NgY8vc0d-K7pZPJ7TKhRwWea_eFysL0VY74J6o6KGQV0gdU6Kvm0OhZEDg_xzmbHqJ9OOzWf8bKs-K082D-JU1xhiFHXIFychREPYpbHUxoWiZghbdbd0wjriZ4NyyGi3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0TlX8cXMo3ohx7qepbnrEFfL8fbrNhr6jTZNSW75bJNxbL-eZPHEsOjqtl3bqbez9_HNbrMGhXsywNcNizHjkaf1ctEXrY3-TzI6144fytYacy6uSOin4P5w6IXLJCabL3D26-e0YHeTqM18nIE3hbMzabHriqgy5Dzw_GgV32Z-Ab932hPE02MFXWixnUaU_t2T6yBJR24J7-Vvb2Ny7RwR3jTs9depe72OB9SLDTN-cT_eQERoIWufKUDnKkff9ACeUMtixTSzl7ZouDvykiQ7YRD-SOijcblggZYL_2VJxn-u-xGJyXiy-P6j9NYNqiIwGenQHDakqW___EmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHZc7EcSIWLjvNuLXIV00JE47b25_ueQdzn9AJLHO05XjmoFbjqwE2FnkFEopmVRPzwbLvMe2sIp6fCZ8lZDw6eUFDXot7GEAKGZsGm8njdqku8ahtIUcaySHd7cxweFft8yucm1So-RA7glD_WP_COE2MRpOksadvQOujC2PkEDeoLdyib9JuHiTelRrQEXmeX3jJbyGpS7f44hYT2fp41THUGZn585BPdo4Y2IsCkgBydy0FIz_j13Gt9AS-eRiNcCUsOhbv3PnhpGqfZ83Zv70wGjuDhJoeRC61Z2l9tLA3k4SLzm2PjS-dMVmVaMERaQWMsP3VGHzHgzN0JJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrcSZJ1FA6lUk9QQpYtOR9O160qVEzzmxZ8nDxS6-WrJ27b1MluDvIxD8YeeBwJHGR1S0fqPhCgnpmcpHrvldLteBrdiBGq08lJ0dLUfGH055WcX_9Q4V4izic19taq1lZGeTHl2-VfzOX-7GydTQyNMEiTQAbFB0E9xd9AnXlyMQV-oz2BpqU48LMY0duWru3t5YfnrY07dQ0i8k-MRvf4wg_jOR7qY3g1-AuBFRPWegIaTb4czTpAYxMs_tsS8Zm7on8tYmMP5MEx2KFrOIHFx819sOylwl2Sv44iTm7P5rrbvssCYTPaW--QRomkgTR-wU3R7uukbdIGiw5E74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJn1coegbb7kMP1JIYkWi_V3esUVH6olavh8ovboIFZ-MSfwgJF3hE4TooDaUZd_qvFYrQpk6aaFdCIT7IisHJ4V3t5vdB6VMYAI3_SlAdasJ_Tzt7T0mJcfIcQB8sm2vFRty0TkBmE2x_zIDqBT11T-GpN6g6qlygA3Sb89pxrJbM2t4rkXP6okNh1FQXtFSuq5j486B6SOVQXPVIPtQS3PpSseGMeRFO3bluibF82YT9NqhDe-FDEC_TwenheNfjfRpOdiVevSrIhJ9PVylfHE7rjsMJ_U1uahLzhu9i_868H29VU-lk0ryiBPV-sqYkUOF65Q719u7BvC_VKlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmXH6mDeHCg3SgWYdOk1382ozQBfhSzMirV4MILhHXIgsQGFSQS9MPj5oPmsd-Ee3Puqpz2oYUZX6eo1a4T4P9CnYkFVBIxsyQ5U_9mOjFdPvud4ctsIOXg0d7PPv6QtG0aRbfLJMWZmuJwwBSF6bG7VOCfWjH9PWePCp15SqoAYjCxgq5h8LrAuU_8oMyQvuwB7SfvE4z7Z1yz77ksOKQYOrcTsCmemkpLMBYkXiRrJFQiijUIFP_303PnWtPPwMqVC92o0maTA_3ZpqHxK5BybvdENO0rbxMqe7Em9Rb_K0E9MwMiPJNVeHl9HDqacg1cZYp_o5L8PbYvYXgxZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU8tu9SIauhvpnXQ0yhtRf2RqVQ4zxfn3MaL35appbki3PcyqZ9rUjqCnl23CI0Ygbb29fsnmS2SZVjDC66ZgmYVUsRPhoR8vpQ2ctxJ5nvH_4ctegRI3_bRdNCIrjJoZyIHH7vUlXTO9V8_IPEucvw8no54PIGQG-BgKt6jLt8oHUtzUQQoXblY2vuUYUe93CCoEYWxSh6j-N5xxT1hr6jnoT0eHiV1WEPpqyHpPjGTcZcUqBfah9y-qQ8wHpm_Yjx5X1rIX5NetLJTD9dulx3Lx2dvoZxHAgQ-caDgzBU9PCUL_jv18EP9eovVrHWkk5LyCG3h6v0cUigaA2q2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNClYKS6hSf8T7U6UTwHSqt4QF8VLeQ2yqQywjrj63EkgsevaRtcXBZsLGdpXvmjzsmkpAwSCR5nv16gjcPPXNIwOjk7z24pzogIsvFnU9lEaycE2PuTR3Ich9c6_8c-B5E_q9kaYYcZwWSremcxmzIUj2YV_7T8-HBtbZiH0rPchG_e98jySbUcC7Rl2jlx0uBqs1npKD9THlW4exMFdEl4a0Od-2qPDquaa1Ite04faA52eNgIR21l7uL-hxAvYpdhfCGWLQxzRhK6cEFV37-WD1Ed86PmDdyafZvmaWbKfK1dbz7K7cpMznBeVlbeHfmEM6HoL5hW5w0s1CrJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db2Fz2qfxpGtFlucqe0j-12C-gWf1F0VVWUvtxafBKOsxjUYIZH5t8lpxrVHmU3g0bR2i1OTNdbW9mEsIjBW955j6TZlpLkA_O_uwOKVPFSHU8FUuqbnGB0FeWXhY4am99qrn63DPNi6GlOmN2gI30s0EOSz0lqNkmuW6y6NktWjZjNZp4rJRlxeyrXB-SvsOw7oPm892fxgJjdXVYCdzsEld6RKTWMf7PwKUc8yK6p2ATgFmJuPbsFGguQzeOowXtE0ANKd76JmXqsLsishCn5vXYhSAwtKVTy-K25AlljCz_l22lWTKsW0OHhw5_vH1HQQqrl2AMqRSDkRLZi56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwpfG4_M2OD-MMtEAlkkriT9e4PZ1931xHtn1Jkd9wZEMo36nA0xgg6nr7hTQ8QAJ_r1ujtELp1iSohgXSvk366tAKnk1X3_oexIqrZR7WpvITHERi6--V6JGxc71NnyNI19Gy1Q3N5JtQkeE5fQvQv7dzR9A9nY07kFXyiFVFzTwtbWz4DnalrZ-9oqU6jqzgVFD6cS49hwEHGsMr8g2M-mw3hQvU6qtEUvM5hatp1386Wg5p80be4gxODyHHhoJw37KbPNAvSBhYHAYphFmQ6QP5mh-U1v49C7Elo9IbBHreYGYbCckdwk7Thsh_h2iNfxjzvkCGrin5CtnkQu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-UH0zsoe3DF50az8iBqvmaDd0WBKYb2-nUGET1vpynbcKC9aoPRrlGATP9h6hEHYS2bnotR41NOrs41pUFHGzNUi27gVa4ylQPhKmTcpNQLikAsLUllxh2MrvXZcePsr66VgC19OFqy7u0zNnyhSBzkLbCJe-MQiWPd7-mqTUbxWneJ6Q4HXLwEzaiv6T9ettBU-keFfSe_effCdPb0MlvyTCUkNaqfCThMNG37WPXEx-_2H7bc9RhPgoF78R8X2JjkrSlTLBvZbzp5cmIHUPT-tuin_D-5T7UbIGAocvIP3sK3yUJElawps0T2rPqQvi85McgOWgD81yyLcT2RFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvYYjYcPYg0IpARo4L_U5IX48jHILBJYBxGd_hGbx-Az3VVKacWAI3cAH5SRFllowbYv-j_qV4dSdoQWBtlE9IJyxFGROqB3wl69E_QooGYauRXDg3F-LNIwUNMeHYXAre_TRhiujfxFLIwvzHWlwJY_pzKu2GSeiTSMVQNCdMVSs3dTBoZoMdfL3l2nBVf_HjmNvexB9EEOXtUdP1SS4LU4NnEPjiF5IbRMszSH4DZXpQz7tk3NBEVhx_7ljN7s_faVH9cvpyfTkLmxRXRLv7-AeawNfI5wYy1oMm5UgVkgY2dNhwBaNDAIYY3LdNGTvXBQ8Rn-uD3ouC7ZH05DcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQZ9AHUrGqt-PNgt2AgG7xSyEsND5H1yWqp1gtWxLi3zDwlrq8EVfkjvLrEWnUfayEHIxujwqMTxeF9Y-Bcowwst1I81-w7LlxdjiP92ey5dpAgA5Z0Z9KX5xljz7hnlryl_eRvGXyR-N14dRIM6ga-bHa_M50QSlGFZZBg_W3qFkI-x2AGPclHTsoAkyXtMNmQSlj6-zrF7NtJ4lj03xRHKio0TJc3UGamzMCUydJL_VwBMBDxZNLZiYDK9mJ4eFeKtruF5LDZmdbGXPKW9WTB0f13RjId9U4HnqEmE06sz6xD5Ovdjg5KOq16D7Zj_zFTmSFiemJ1f_3mEHYhd_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHVcDmEVdodJkGD01W0ZcwXtAzIpbeFz8HRuRGbjNCVNRTPtM4b9pgjudEzBMFt4O55cg9v4ISxe1E8nUq_m_STzZPYE2brl0nOXLOilU5qg6z7iy8yCdNMqBX1Mf2mHpIbsR3uhL-sXM-aPKLF3EoC8rAL3Br3TeyQzd4HGJ1rof4A4wit7tmvYSGtggW3HFsdr5SH4UlcOacEMX9nFxhFeXBpSxxU-QjDe2fb_194B6LErc_bppD0jH4yafykK1meSxnf3G2yiVQSprQQVoa2LrxIB1d6LCVy9JeOBUyeUK9vyA4wMJOjSKhDsycE4sWOU83KeTnFkO7sCLlq0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tweUFtATdX-UQDReafjY8BjviaaRGklVf-Ne8b11pE7N-xVvC7ip-UUvguWLMZ7JSMyFZ3TNhDB0bNyN7CueVkzwmiJM3j0EWVK95NWi0QNNtODC7RRPu2d7wzUwlhPc1vWacZCARO_4C8AJw2c7gnULXxsBw79j01Afs46CrtUJyhIbJnPfk0kV2yyqzd_8UofuAM_rPKXdltl2tAt4zcr_NCokZ-KIufcNO1DAl9Yui6FdH5AfdCUjwM38sj47e6YvKr4lb8BU1GCmKjW2_xO-omi-lHlXGBrAuSAPiWFr4Hv444MUsGFyO37lVYPfbAF716lH7CMpRc5oGfvrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD3ur-I2dwjDejVfXkQsDS67wAfNhT6rztNv0-eKl-LwUDT0YOGEQ-voOYZfyfUHWyNX6flisNpD9s9nGuYFX59b6549kzojMuv_GyOgw29g5MGjXPe4NbTKvBRrcAkysT4Liks2fDwvCZkz16TL06kRVWNlf1hJm8FkJIHM3xXLN76C-p27LedSn9RB1qy48SXwEObT3QP2Bexb1xFvwhMUqtb_XqBFcZ5ZwvcbXck_pZ5IGKPIE-mlxxCfih4NxqaEf2mUznN5pXsni0GIuWJUxVBc8zqVjA9T3RP58738Xg51h0EcJMuZs8bXnIoMtzG1MtKd9tqc09LCedHzGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_HiJGdZbG6_EMnRrs_HK5GmdEO-PBC2vIrQTpf6ClvxzwZdLxXun_hLVE7siKuhQidV7VrsVSG0bUIYd126kJpsHksG1HsPGKrsyzM8vQr7Mfem-GQoQVHAq9g_8NZdVWTULqDrOLuaW0bDyE_pzUBQz5ewyaP02ZtZRjq54cEO25ByuU6As9d6E4FkzVj6Sewx5lUk6Ln9gRvKjSZxZb5J6IABxbYMha_jW_KPq-fnzCNLTN7RamosBZMhqtgZkjyU-rmhlO_QdvbcUu53hmaOYKl4dO6yT3TbMYTLvOJw93JimCmpbdemb3yo9e5Qtql0XIHR2nw6560WVoda0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_mXgC4r7ErgrsNUiK1nT0xxmvi0aHmtiY7qkAX70TavRbO9WLiujI3ClvwSLDlY29Tk1zFIWzO3-LD42RxlwF7sC4bLfltq6yj1SPypNVrzAthITuY0Kzsa3t8BaNTiuVOZtbEPtWRUjaCLQad_PdXXcuUfcEnmAf9m9yT6sGFjcWq4kWOpjyqdRfagCP2V9z9hHY5gL-v_uMMwgLKeh6A2alGwFGbN9UTf2F5snTM5ydQPmdiF-EzwpYftrcDLqCnPBYV-wbcCXQVLWDxNhgS_veUfOwcPNB1Fq8_nrkVmF_P5bdTLFPnlZBl2SERdjavF-OSDoos2UR9_ReDbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faf-XYhvrpdNzOAekNFq0VowiKbYhFM9nwHLAqqAXxkIyjS3QTgaKbAYS4c8CriNSHYLK5Pa3JM21TDR3UrbeMdTD96RH0-RcPWs3zS7r7s1qcbUMh_JgJKxEBIBwik3gNsSZ1u5C4ePotl3lXE8OzcL3lxmP7f4dwtb98Uvizn8v0HpSNWumqfT1pSfGRasOc3Yo9EjP_Gp4kr45eYs5hYsvy9TNVuq_WHDChsWYt3oQhYFsZQrjEroZ6sREfOb2SkFBmlhQLQBOcRZxYKfCnFO0dn6PxgQcDjnOuewF1ufhmc9PWgT1hQr4WprfjNXLESNPcYpwoyCdHZ3fIshyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfY5Sd4m8j-mUFDJJSDQRL-VmIpqIq4OL4CTjZ3uI5wpJvYLf66WjMhFXqW7AwnzSMuGuLpEs-gav_BknnrZp3sO7wDJZ-dfxfnes6TXoqGK12aSqxKleSHAGrgnmrZwtvTTFClK3TnRr5RsjZphleidnu1UOBlg2dIR2U0Qi05gzX8qneRkgvMe_W4dm8jw8M6WuBQOdOMlsPnlSh9dH_EFvZeM6R_0CUBo-qO9Wj2M4SZVQYSwLieWNvJ1guxRDxuO2DGh84t8LroECLdqsqR-ubuKguS_eiG5P09jINDt0xL1KZkqUO5dLO0q3uOI69SNx24XpiynF7KIG_t8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lit1nPi5Y-0aSBYUbbVWzhHGaMUbsVeGxcJ72LTIDulMoSiQRxMi7IUj4lm_ajaUSyXeh6-tOUG7W0WK-QVruq8IRj3R99t70AJA29U-iJb1eMZhJjTJ3Eg2kpAWrsFLSJ74Rx0KfZGiBHyFvyw8OJMn3aucIDi7a4UZQyzXoBeTO67vBUABaw1FwxD0JqXcTvOmOlpJFt94qxd6gMEYiPs_IDfhwQv1TH0R0rp45UgPnrG93XEOwiGfUzWBl_6vj6tXnJSNKozQPdajuYpxhMEqEH4hExqMrWDHmTZQdNc5nCaO5g_epreQtQ9Vc94_G9e-APLa5rWCHOckd2ByFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXRIMR0etHGuB5WabmObT2LdGkJ6sjOt_i3sEu1i6z-vTNjU0zxYahD4OSfi4Qf70mZD-ODCt1G0ecM7YK7wlM4pWKu5gLcKQULX0LMX_AwEk0L6acUK1drEyEkMCC4nYukzUkFPRlLVSVMzucuQJCMS3d-LmZXZ36-Qucy-fpuu2naYv9Yew5QAmFuJnu66pI-j50tew5GBycODUHNNhySDBCYowVh3haTa9hjcFeAXb0fW3R7vS_XnlC_tPjPyXIc0t1IBzGRRXx6STf3P_-lbhyFrJ5HS9k2LU8wKcbNAH4e8064w4h8JW-qbJr0rN4BejHn6MimG0d6WGfsJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_a4uE0nEb4ATRhkAur8ryZZ6PA_ljitb61DbAwzavlgU4SYzWg48N40alJsX-oOD5ePnKccIPBFbfV9S5AQktJwM8HIbYzj70wU5UycOJGgNY-vrZWUIsNVAt0hAbjqGlguzDvkSqTR-5zkwrf_3bLUSg8tWD37qISVrctDqnA3nt3dcK7GBRoe_EGXkBDPZKbNqGu0mLyrk6wj5bpAxl8LNJz1Qvqk_ann6469rZfmYWnjTbrFg4qdNbnekULPJCbFSaG28MN6QPWvw7JHjIS-WDPF8g23gibzUTL4fhtGc3R-hZAtq1MoF1XUxVgv1R1CtBLh741suEojp9WSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qim2mONi8XGiV6Cd6KQdMIW5Vy8Z5Rb_KPp5WLpHBEina98jYdTtIBqwkDqEgoYiXPaOboz49vKuGGneIs97__T2KhwR0ogmS3N22XV9OHlLrNDHm4lyaVcl4DcHuDZvEQDw_qZvtx5RR124_n08TW4UglwkpEI6BdV_qdxW2DfhXo77Uk5dI3KnSmwd9rhFmEF5G_ojCf8NtI32JVf9C7KRB-w_HlpjORfT6QcGufsllezI1trTZgckQlf0K7QCCEw8w8amNovwgU9Cm4H-ecg0qI226ucHuO2o4h3RdNsEl7umoaKmlCKwipCM34gO4xy_pMblvkLLbFsgvJ7t8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ysg_WY3Yc7NbjanLLgcXe_TDewMgVrbkRwKCCG_ptkZNfqnawHEPba8l2KqlSuzzQUQfEf6rrlpnCtsnrmsgDrSxKQRtfdAGPOHzTrPRQGNml7Nf-7XBCiTNb2PwE2cQ2OfCZdZG6fA7ayktWH1gPIWdRs9uBC67Ve-mTpf0IOrWABKNZcmf4_CiESCd8-TTmrrNcatMtQ4vQGqCUhQLihqugEpxuQXwFlJtP8bD8sfdq9kNNUMBct27dMdFpJhgundvdLUKQ6QUtJ6Y7EonsheUFPkUZRxkWnZUFnSlaOkwuwBi-ekiQdFzI37u2KA250LkOMXuqFP9eGhj2UCg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hfa4BEelRwvMaqcmNy8JWHU5-rW8ZjvIEkd_pNwHqhVg5vCOE4kaJHzSd-JoVxkjpJyVJcsR6NxOJZkI0G-MB2kmMcVrUxX4ZBEUumsIvvC8bm6XNDgKucIXAbMHZEGXXy-wzWSb_YcrV9ZXcJYQkRJF6jXWu8ASiUhDpgWCHrM7N3uGnFRN56BX1kAULLgemwcHTpx4XTVSUnnLyI7AdxsFYqDhIo-IhoXBKDAwu-UJ_2RAqY6BwN2jMqeFaXflgNLZpVnb-wWQL68Aid0wjN5qpO5AtdW5LhBMILgMNzG5M_CTOrkt4MA3h-k5rPeM5rF8lME3AInHOnBA4iTC4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXmgIYsHmLvTG5utgPy8F95xZRTzSthwB8f_J6_AfFfFvdh6xrn_bdxDvT9C7FbF_DlUOa3bRD8Nbl-69d5d2ASltoj9wZmX5KmTJjFWHFYGUaWXrT63wRaJoA3BU2ZNDmq5IZkwunTliwwY1RewWa3vBeXvsJ1iMLfigbIgNedQfldx4elgPTIIxl3t5k59Nl4kUJDlF5e7-KdpJBXdjN98eTMT22O-ITUvIfCX2uUCo1itxryEVnR4pxKDsoCC2etTplOUh21IH4Eo2SViDeFPts7Y6gLJ3hVulbhKrxvPzPlyLi73Isd7wXY7zvPwUzB2dVRRNQmqwBk7sCWnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxghJIjJWoADL8efDhKQNc-BsSzdrUtHL9T3FtQ8biW_rHHBHm5F7yAAFUCQiYNWujlIdGjmBH5gOj221_rsCoWurqyv8Us78x498dJXlQz7lqYJt6N9guibmgZQMuIkLQGQjg26cCjATX9KaDmC3qkRlmI7OrbOuQpmU_rZU6sYpspJO-Q0TyzCE1x6ig9fLxqoRzjz4Vovgn7iYMxVfGQ3drhifpGJDjj0EimXTwTRBs29tEDi_csFRlb2jwqLAaqwGeDPq7LgyzMJDuT0wxaLxmxJKdpTot0OVRYXgBI6k-U3Lb6zJ9fZ3sdOb1MYGmuk8aBZgyPD4w3FC0dmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWG7qZqz4se9iu0XqcFgcbYEwtflGm5_nqonm9mProWkvWeXdcZUitKcciDVHewTmv1-LUKh9c9CnBfYuvhcZqhVXJbfKCmFoDuEBzIuiQk0B_7uulyiMwEWqGQDuH8fHxhXskRVIRYCwImaTZ-XcvWCEN4O4w14_KSaz-9wF-5lfqGsO_sv8dXVYzttrEoeAGH_0DRRXAOzGF4yPjgatEeQlaMr1od9w5rd8HEKC4DfGejnXQDwWkns-U9dqcjk9xYZ5VcbbvFb74rSZLww0J0Cyjlty0m9xxuFqVKNeUJjS6t7UKtaUIAJcZ3G9DnV5Iv_EHRJLcaIHKDQ7kb3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBFTRPikpVzUz3kEzComjWSntwJEp4eGQaWqav4SwdSwPzUCRykhWJW6UILBkEFC5VoFXs0UpTS3fjtHX2oAjsAZe1Eq6mC0HNPI-fit2VcGH6Y0Z7aLQZrEzz4SE1DrwB4yJ9sAffI62ijJaApj5t0fx4iEO8QNe504z_Nbq589rQ5t3Vva0nKV2i299hGVW3XFdOXISXgFprRE2aSNVPxpBjbCk9iQHpx7qR9QlT9617Xl37EBOzZ_3LdFHS0ILaL3ZCKKHfM7VI22oX8lcDjWbsrY0s36pkNq_-8ilsQz7gfqFq7eAp5YhxwOiByE7A54z48jZJhE8xxp6HEOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4EaXLuiKVadhOSs3kB3JfOMXIsx7mxXVaF1GzDlqq6Cc8c_9gUkdMbUmfynIQzF_VytZutLGAFPTKtvZdOghWKmdPWkWuT5-pnVJhOaCJsz4mVinSRtR2ciSmrAvGrDjDCsSw9oc1CoLKEJxvsMtyKHqNQPckrPdxp1F5Dcp70bu2C6bJtqCqlnHEw0lDwh-mhAx37GtiRprkHiQCCHQ0E6Tx3Fx4pt9lyZ1fjMZZ9WO0xdcHZEqoCyT_k5QFqz5DLx11C6yOdHD70bWR_eoN9SsEASXq4kn2KdcPfCPpr8W4BZJhlorSrb7ImxABU5rcOzJP0E2M0e-OoplyiqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEQi_4-D3KlB9Ac7SUgYXHfmHZMSArb9xjHZD7JHEZ0EgarQVcQOatta7XYx3ZWZuLeK-XwVHgSsFhMQLU8VPCsSicVghphXnmCHuK-LcMC1D6lFdcH6z9E8oxln9BZ5CI8Jx80ZHJ4rhhJj7vs_zcnWqpvi22hFBwpVQWymdXKS7JmkdEHbiwo_CcgdWALh8w2k1XioOP0jJS9Tp_B1iUNe_O9gAUWtWfS8YPth3DjgcknmBrKeX2U-uW4VOrSJNkng05Ht17U9lFMQvhyC1bVOaTBI3a3jWdxTM4cI6f8L1z9sclayXfklQ-slmH2leotcBogA5skBed5AE66KSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNgTodHtmlysSEO17N1wIA_eqLF6VlkQfHHel5nzYpZ7r7PUb7xGaSiVqrFNYZ9nzjZzbLeCxuIMIprkyYfoBNc1sHhzZNYNECtpCBVCWXgMuKbcEGEp2VM4YIeufdXE43hFMlSk26XWlwjoEvHZC2BNrMk0q7YZqwGIqR4KlBK1qlhQe3vBsjf2QdWPL6-KG9x2IVfHcHZRBJIBN4Mg8MJLfw9_BMzo479S2Ken2Y6p1RrShZhK9JEOG0J-jl4mWrhciFLaUxhBCTcXUVAtYEFg_I4ypMdG4Q_ymxZ4i6nKbS8udaOIRWo4FR7AmZROJD9YFbY-LhPqEfiMW3a-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PAypfqw6x3JPFxRtqlzF7lF6l8y3W5j8w7j-9paX0FHqMa_NQSMTKJ1JSxs7a3HexjmyIy_NogCHdr2VxQ2SCANpPoH4gZnwix1mM6bywLaM9aBYUOuFpYHs4vmj4gqyiZGQV98kKLDgzkFIN_EGc2cW6t4KlhkgbW-o1iB_mNz3Psp3R5kcG_I4HjlAtMxa9x0hvXeJPblBpqH713k6jTGs4vvR01tecXUTAVnbMaLWspWuSnM_ULlU0k00PtZ6b3KK4K_8WZ2fAB-nniRWY75QLUDc-rBeHZZcu4BhJ6ncveAB5IUz3gP5c5ICA2IVzv-fQBZn8QaPgbZtyYlykQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=HooE3k0IaYrtR8ikjoBZ8eKBNcJPQpnrBBY2KuwwvU2bjzHSSpsr4fH7O251flQjfSW07rWCIG-9FsomkXnuwWoYPNbXACBkVxlU1kzw1w_GEj8IeapoD2iUYhI0AgEi9Ja8j3R1x_YPabLsy6QJROrMQvSK89WrVBmrYEvWMzpEE6zE1baTAIbrPUoIqOx2FRJ0WTabJFVR4Y6bsgtJzRQ6-XUmmkzOXYBom1zvlyGBLE8qEC8ZeK_1m-7Xc0fEzvLWLZ8dI5-AVH98MdutOVkvxgIDPj2wfRDctJdckoABglgawbNFGqm1l5msTQ9R-yDFi5LMTju4SbUmo048qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=HooE3k0IaYrtR8ikjoBZ8eKBNcJPQpnrBBY2KuwwvU2bjzHSSpsr4fH7O251flQjfSW07rWCIG-9FsomkXnuwWoYPNbXACBkVxlU1kzw1w_GEj8IeapoD2iUYhI0AgEi9Ja8j3R1x_YPabLsy6QJROrMQvSK89WrVBmrYEvWMzpEE6zE1baTAIbrPUoIqOx2FRJ0WTabJFVR4Y6bsgtJzRQ6-XUmmkzOXYBom1zvlyGBLE8qEC8ZeK_1m-7Xc0fEzvLWLZ8dI5-AVH98MdutOVkvxgIDPj2wfRDctJdckoABglgawbNFGqm1l5msTQ9R-yDFi5LMTju4SbUmo048qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEPSuWKIqTYfgTMoTF8vvwM4Ihd51ld_mffZ27gzsXHS9kxCUFtJsa3ySJSjJMCsBaFebdKwY9ZL2x6RsLql_Psn_ZorJRIS809sJT_KqYyHkh7VB7pTuLCy7w32b4v04xPVlHMCzw62frZYgSTEMgxnIGok0ahv4mMmxzuleiiFE9_0VRovNvmgAkhsqsEq_aJ_nWTohukmbhOXiFMTz9C9qQJlrcqOVa-84JdpwfXJNdhEuRNyzvY4UFiO-sKX9uC0jvVbs6zZctjABkeH71Ylpoei8cbkRI-7UaTjZaokxaS-usNGE6EQavu9Zvo89vVzPqEns81WLodM7QMidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXjij2KrmVPDSFNsnajFAvgfvNbXJGl8hf_ZqKjk5a7CHaGHd-7Kaf3M88NinPyOH_pbqSqwmCc80GWSfA8NQIRbP-fgxOhBmmw85b-EUW8N9NUFXaHCfLWwBv8K2Ct_pHJeUFW_tb9XEch4wPrIl7Px9FZi3_Fg1otHzzlc0zcji4u1hey2Et3KWjwpHqHer3nrcqwt2pgyfQ5jpxNM7zDFqsI7K17jdl-f3ukY4_eQrW3brnRAWIdcGOhr4oSrDRQa8ryd1nS85-PwV8i7weYqTd-slMBNJPPV_DXWPNEJwW6VzJnFa-GVGyPNkZflOlWu7DAjc8r-EQawKnDm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwZnvV-1usQODpXRXdxP3VioxQW-xUOPCcQnP8XNTQj80v-h-IoigBb2kISZPlvuqlZDG1KdaSUc9vc1UO25OYMc5NAGE8PwHZvGKt1L50NimFF24wKM9vB-ta2gx-lDqSexQcJ00js8sog2Bb3xUhlD4a8KIAUHHv0BWPdIQfWmmsNcCpvY9jzmkYVI9KNEPmM96aKjDjdcHPXZzL9edpeY_DpTD3S_sAVBbJm4zxfKsxl_-5SqsFToex9ikcdnlPH9L0TWQdSZ3M50NnIPRncLvL2zJ_8G6uyDz5D24gnq4hrSXjF6LwXXV97KCYv7S3V8R0C4Y7epKPvgo-Bo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2jlkRsmr-54lq7SmeFR1WWTLLoGfJs9bwr2sitkIDa2ZK_tPTy9dV0fGJtP6ZamhX6UmK2_FKpvBulX7RGsR7tLfiKE2AokIYpY9ReugEgHZqi4eaia6E8Kz0pFkqcuRtmT9sVyfvUaigTP3SVEnAuLpDf2orn2UPrnVwnWYkR3Z91ODsalCjEYSBi8hu_5SE4TsJYIJ4xJsJfeu-Wm4HLRIDmGc4uXqj0GKXz7L19V4dvomiADJtFvj-1y5z_MxZWVssDSgoLCTs9dZ2acemtpoEGwwUnX-X2E7pBoE89_QxwlaoUP-MGE0m9ROigPJFZWfyd6YrHM9RhuMxvtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEAduT2ZAMUl-XVGSDumnirpXZdPk-5VQ-PHUTm87eFreDMfQsbEbaRi0-6wV4ZGzJnxI4IE9lYAv3MlRTD4Schlb9dWtNhVNw_4FuYf2HxOIIY3-da9-7VGNoTa_NMQwQ5CoQUnIE915GcDL3Q6X8WM-gD7uyyrndAbZpd0NeB-q42euJP8eK5REoA0QEwc82-cPceqiomTruo1wuDqWYMOWaOpoJF5f6dxO4Vm2rZcJiVbXBSjdz0k0bt1_BGH-HX5MwGO7Xr76ycHyOz_b5diK1MESCzStE9S4o7fge3x1BQ_S0Bj1O9Q2QCNhLXblcIvlGx5tzfEPTQ0AobBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=p38SvJ4EffRG70PT8kJyWu1X94y0Ppp7LZ9rqEJcVoxs_NUD93hURZWavPWvRaPRUOWFerqDMCckerSWppOWFLJ0coL_2KF8F2FUqDzY0CM0zAd5Bigq8b4eikHtz2Kp-ypx20ffTVU-u7WoB_fL-7haPjAryV4llC3w6sxOMbXr311U0LcD9KCTDUvaVpW1Wwp1xtYb-YZiYJ7lvzSHUn5MYCUo_84cewJKwO3wOEisCSnhTnrqu-3hFhCd7wL17xH_H9I7-k1TMCbiaYG_6MDAqGjbzSqkKxe-cgxIDUXKWJl1fF7TkUrxN7w7yp6ZW2Y45UYuUvfiuWowY3B26g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=p38SvJ4EffRG70PT8kJyWu1X94y0Ppp7LZ9rqEJcVoxs_NUD93hURZWavPWvRaPRUOWFerqDMCckerSWppOWFLJ0coL_2KF8F2FUqDzY0CM0zAd5Bigq8b4eikHtz2Kp-ypx20ffTVU-u7WoB_fL-7haPjAryV4llC3w6sxOMbXr311U0LcD9KCTDUvaVpW1Wwp1xtYb-YZiYJ7lvzSHUn5MYCUo_84cewJKwO3wOEisCSnhTnrqu-3hFhCd7wL17xH_H9I7-k1TMCbiaYG_6MDAqGjbzSqkKxe-cgxIDUXKWJl1fF7TkUrxN7w7yp6ZW2Y45UYuUvfiuWowY3B26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=oYaJxf5bUUM9xXJKmBwQSK_PKdcof3pZuDOAGs_GLAJQAuTO0pvoAnQTDNq9LLNSsZrSnxcMOsTTeECL06z7Hr0yrAdANIuAG-Mpetvk0P9XOrqV8chzfDM2cdQ8QjntJvLf7AvHqOFg1v7gITSPb-Y_zyI74WFXebK5IgM8l8o_amMex7qfxddp8p7FIGjyvGFn0idyrbjGhHh8q-Z0oP56csT3b7Fk5Yac-dg6MKDtlgtYsT1HA2YM7yXIYneuVbhpUuy7TAZTrtU_X6nibj416Q7oi9RTDe6MLDvDbGLqEyYqhPrePiOde404_Qun8SCvgP5i3i-KEL8sRp2vGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=oYaJxf5bUUM9xXJKmBwQSK_PKdcof3pZuDOAGs_GLAJQAuTO0pvoAnQTDNq9LLNSsZrSnxcMOsTTeECL06z7Hr0yrAdANIuAG-Mpetvk0P9XOrqV8chzfDM2cdQ8QjntJvLf7AvHqOFg1v7gITSPb-Y_zyI74WFXebK5IgM8l8o_amMex7qfxddp8p7FIGjyvGFn0idyrbjGhHh8q-Z0oP56csT3b7Fk5Yac-dg6MKDtlgtYsT1HA2YM7yXIYneuVbhpUuy7TAZTrtU_X6nibj416Q7oi9RTDe6MLDvDbGLqEyYqhPrePiOde404_Qun8SCvgP5i3i-KEL8sRp2vGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BApngux3C1zccVx014HgCCdxYweLnmdppMPSH80cnSK5JclGZcCT2o8S_jqTsK5Jcz5BsWB7URbtyV09txR73jc6rTsocxNO0s26Y8CGojVZyZvS6224Q-3uNUSOybdGKwZy0Wshw6UKkE6WYkOEha7J3qoBJ2T5V0c0wqQxLHdlh8omel99EnAL_Gb8Ku1uZBc5KO-6cLBcEntzk1IWTZtijmmf-3PayLCT2v6eusKiZKo1yPvM-JRj3szzm7-MzzPCewCPQOMwViFO5lSXNBxknvksVrx4i2RNB7LHgw8tS6hgxhj9MT1M4hoQwg9A2_F1ktirc0U8I58_ZWzCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQsTlhSHH7IIS-S7jTgY8CUMG0JtaScrGX1esShOcZTMBkHGuinlpMEb-kS0Uc7R3zEQ8w7G7u2yXOTmrIHsHkCky11BwGpIIvdPYiott792nBu8xOVQu3Zf7uJl1vaRYHwGWTSB4qqpfEhumcnkDx77vfhZmpNwQyudcWPYn-Cx0wMOf7xGCx1y7xQXTU33OCZfJUhdlZL3bcSkxXZf7RgXmkbf0smDF4oHQx4mNPollizE5qyaKBuXPZgdRW1M_qWiG3Mnjqz7LHtX8rV-iLqVFdxUyRPH952JEV1u7eyVoNel_swJ-YkMEjTTVx42QOZgQJjnA92cferw8heeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSWdjBYA0yWxXK31c_69zaqossq1BG4VBMZdVzFWF8j_Vf3Cxf6iu7i9ExJS3B3TNBXKCMpq8ycSPl1yNiPFgXaxpJWxDnPnBuGIdHpJi6tB7tFzMTZO_MvS5x6_CZM6r8Hai_Lmye_4HAXGqfnIR-HGlVwF3SbsA-jcowDlQa338LraRaAQpzXKu3BRdf_iF5G6z29W4Sgv6frGrOAoUYjWUGo-3IVnuNbo8qn-BQ6OncCcMPwwWcaJcccT6VT6C5qDVHRNUzoa5VvGX45TxGOw5-pak5xb3xEC183mbWv1DhYUw-8caN3NKyRCcvr1ptBz7QK3muX4_s8RU8tBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCjhNNj3BxTQAMQIU9ynUkJqCkbwYg_lbpqOA6VphpJtqmmDmlMMqQaqPMh_MOCn93uS1znWUzyruI98rdhLBZtCBYI_hW0mPgVHY9UOwN2tqzmHbNJJeguy8MNJONvrtsJocx0XtgenGlnEwclnyeEX85FtQPD4gnIwkkJ0ul_0wjjeV0jJmEUvScVD2U7qtX0ikr8YmmhVyw7c4tmfJD9cUSY1f1aNEH3z_3o-U_PFw0536gAexwMwcaYW5-GXnKuqAgizbhzTf8GTZUc0cP6RgAjors2Bd2ag-0HAqQmuTsFc_vbS1ciFVpPPOsWHcjwNt8Lf8SojGzCgXSTMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpzsRbM5x1egVBFAiiJ0G2NlnzFmcBC6ijwCOCw-UbQ9Y-KSI8nyyCO79RwbYA7V33C_pvPDUUcL-g7QKkMBBhVNhhYEz0KXsn7TFZ5KYzdivIrC5lJc1VlECVgDDyvo0r4WuwDzQ-4vOPzEKWGV5kDGn7ri2jA-zsXG_x5F-Lqc60tBzjEfKUzpRIAXZodaZsO_auAEiFOsO7md2h9K8mz_KvvyYuLNfsUzbV4J42cLzVyTHz4MYKwzcYOMHUTEu0kaHL4pKnm1Oe0upUvO0qW6UKXf6PKBynRCxuTiEd730_ydmTBCTLzgCeTvqJukWmS_-0Uf7X9dzVoG2yA4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esiavJLwrf5rwF1R20OGZ-lbtkHKYFEPKXgBdHbuRqGn-Ruo2S9Wps978-JhEvSgumi74tnPltiel_GGzfmacEcZVOw9GlrD4eWlEjDL5EYAo9SHeGC94SLgudXQ741rnRsztajv08VJYboaZXalfIBa4bnPbg8T43jVyeLCxI045xd3eof5Wtaub45L5_mRilABArh2BfKOvTlkFERHuX4BYKyNJnKRPgoESm3v40i1JDCOGHC01KNS2HRnrDKxnPXje8s7G45NMF7MjakyME6HUtgK9E6l3bvGpt9yiW54VNTtZOlpeaUuF3MahQJKCdEy5zQct2q5TXT3fzCNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAfvHVF7PzUh1xtQwLcxopy9yuHN9T8pi3honsmDHu1WUSPm2fYsF7zcgrALUBB08vwT_BMf0gy-aB1Y53PN-aQGgjmasKPtHXnvE7B23KKh_lQ-VFoeQ0ORQhn4wTE4YnkfUzRlpaAxH7uIebYmdeeg9h_T9jNsaLeB6I5lSL4xRQM5xZ6vBBGxo3mBWQoRczOYFaM0VKSxGlSJTF2yAHGNb66WCMjxVhC7FWpYWmeM3xZqLxQqw2AR4i031zbR5kz69JWSqU-KDSjEeeN3NdTrdGlFrjBhgxGcikZMMWILJSiAEjICLM6NZP1X3t6Sg8RSUVz0uWx_1Ndz5o-3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=O5yMxVCIk-9vlP8xeUdFIO9QGynpAeizkbUMgnvFarmr70JSufv_ZvlwxY1qomw00IFB4WZ2Z2XhDlVrcz73cboL0CyUKB1txZ9XZyoOn0qTFW90bICu8yOZj1VFv7alhJklUqEnr1fEfWN4l9sojSpSzCoYyl3SzmQkmQIuYqqSmN2323wBiufhlqgR8w1uOKYZR6ODTJZzylChd0ugv-d8BAg_45xsbwxqEc-k6kJsQ5EIox96CwE8QcOrtLxBIAIx9izrOxF1RM-5Q45bLNJdWe1AjfRvJzbhCUpSvup1otiZk7pG_rRaGQxAK4RSdV9dH0kTK8BAhvEvWvKxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=O5yMxVCIk-9vlP8xeUdFIO9QGynpAeizkbUMgnvFarmr70JSufv_ZvlwxY1qomw00IFB4WZ2Z2XhDlVrcz73cboL0CyUKB1txZ9XZyoOn0qTFW90bICu8yOZj1VFv7alhJklUqEnr1fEfWN4l9sojSpSzCoYyl3SzmQkmQIuYqqSmN2323wBiufhlqgR8w1uOKYZR6ODTJZzylChd0ugv-d8BAg_45xsbwxqEc-k6kJsQ5EIox96CwE8QcOrtLxBIAIx9izrOxF1RM-5Q45bLNJdWe1AjfRvJzbhCUpSvup1otiZk7pG_rRaGQxAK4RSdV9dH0kTK8BAhvEvWvKxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9m83qXg1V6BW3sxi_FxGVkZwaoLbVu6AJDe9J63LvZOG2AXnUzq1tKuNxDKgdcvZHKvHQPlEQy2F3zATzfKduJkjZvBluvTnpcFd1xTq9ciQBlAC8cGCY2dzbpSR0zll6HA23bY4gvK8HNOXZMrvYoyB3B3-XtgdWP2HOldB_eVMYgL_ZxlMn3VH2yYKgQk0DS5gnryTvHuZq_wenfqd-XJulYBDMbhQwA5Az-HuGlcWzsYvzSh9uIy1w-Kkqfu7tucSB9bZng6BLHEmmuEI35JG8Yb_TvI6cRvhuYTL7fTyg7Tmb4NjqwlsdRLkZF2cdq5NUM7tlpT_LlkjV_enA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcnqD1KZ7Lhc_awjVxsYirC8vpvyNletN_jR6m0HOR1BJoxSaIsW_f3Sd4mBHen2pcenuz1Dh5T1mky2O1sUk482wOtZvx6XiRPNPtMc2SaToPm5-UAnDaXDMV3IvWbWJcgvCGw4Ivmv4RgIRyg-5ouZtkC33cWRL4W1RZN9oke12QTePFfFWpgwUX0slNFHhLso5CX50nOB77ZYrjwdRywtte11XOmYfeA4A6Bs-s0uvjaSHkByJVMPZ1z3P0v479cS30W998DxjUqUEk10D85fMhfMu49yrlFrc7LqhpGzN448W41GazmkjHdtXUwd0YWOv0Q_pSBmXigUAmJElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=vccz91T49tjhDwWrdbODpsG_JdOoX5mi1h-0YCMiaCybY28ZuCF0EpQX4RanoVFrzQ9huERWGx4uZ-EiNcSce_3dv6Oez1D1UGTkreoUTE7jhAT63vEfIkxqpg4CL9xBkholmuptLJSXOYyrVOw-vvSgcmlWh_odqJN4u_4ed9PDRtJY29UlGv2c48DgkGxtXRqYBRKOSMKH6uvUtDeED6lFGKTEvY3Q-0549EMtvvxVtbfAIpxOMmY3K1Sq_-gmRifN9b2Ll4qwNboNC7I3jd83c7TVqMtSvDFufMgpa4e9k82XmDNsCDHAkZBl9lVLBXcsnDTL-W2rK4CDl6maqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=vccz91T49tjhDwWrdbODpsG_JdOoX5mi1h-0YCMiaCybY28ZuCF0EpQX4RanoVFrzQ9huERWGx4uZ-EiNcSce_3dv6Oez1D1UGTkreoUTE7jhAT63vEfIkxqpg4CL9xBkholmuptLJSXOYyrVOw-vvSgcmlWh_odqJN4u_4ed9PDRtJY29UlGv2c48DgkGxtXRqYBRKOSMKH6uvUtDeED6lFGKTEvY3Q-0549EMtvvxVtbfAIpxOMmY3K1Sq_-gmRifN9b2Ll4qwNboNC7I3jd83c7TVqMtSvDFufMgpa4e9k82XmDNsCDHAkZBl9lVLBXcsnDTL-W2rK4CDl6maqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=gvgyOO8QDcsh26-ru0pN-7xcAvKKnh6UjPxCXIK8hwK0zSJOdj30dV5tv1V4tBbTdkl7C1sMoX0CU72KMlHylwe0CLbP09CzRqlLvWQYi2fIrLnTTaqBF81XRIcpuMSs88iNibgKIpNYQ56XUzN7F5IdHNj6_M_2TlC8MQv0Ymu-0bMDD7DSk4C-ENf-ik2vPWOtC5PrDTLw6d1_Uw3j2IEyFRcUJEJBYc3DYithrm4Bj1gLPNxZJCmcSUkZoTtKWdXyWDwuRwpYM155GAPJYVaA-pJtTp6aRmCgoVz-VCc_d2irgaXN_JQXu5PgEDOsvPz9COUcumDD3jnOgOOWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=gvgyOO8QDcsh26-ru0pN-7xcAvKKnh6UjPxCXIK8hwK0zSJOdj30dV5tv1V4tBbTdkl7C1sMoX0CU72KMlHylwe0CLbP09CzRqlLvWQYi2fIrLnTTaqBF81XRIcpuMSs88iNibgKIpNYQ56XUzN7F5IdHNj6_M_2TlC8MQv0Ymu-0bMDD7DSk4C-ENf-ik2vPWOtC5PrDTLw6d1_Uw3j2IEyFRcUJEJBYc3DYithrm4Bj1gLPNxZJCmcSUkZoTtKWdXyWDwuRwpYM155GAPJYVaA-pJtTp6aRmCgoVz-VCc_d2irgaXN_JQXu5PgEDOsvPz9COUcumDD3jnOgOOWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIuuQN_xnkYb3AAsk0pmleqsQQ-Y2SFK3Dc4U_F8iR9z84_VMZLO7SzpYYQ3sZLWliz5B_4i1MhqBiqsptbHEt4JzrlijxOngZxj3U8llSgyWkDAT-gnj2FFHZKMy10RQzCG0q0xZnUIAd_fME0kX6biJF5aB4CIA2EZ6Fa0yIGvTO4EBUdXeIpyqfOJNJFLIrh9o5sgSg5AwmBtWrDCk-pwnOktCGwRcPU7DJKEwhC8GEQSAGaJznBPVriZsroMhniCihiV4da-5UKd84aHzARraU2o4q_dxOTitQP6tqLe-9tkqLbtJ3y-wHab6w9P6qybD56pdNOAoInUMcnofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e94c-8mt4QxuWUYkZQPLaILlAAuHw3Q6GcUsI_-iWO0Qm5fCI4IQetRl0ir1_jfFhJsyW15FB04r7AF-HwtnFDZnLDSj51Uvvyc1QxqAXNyoDi8zsqCPSsKJjEBuKNIfUR0XguFNy3sucFcfwNCulHj7YzTdpI87-9rArzyLN4S-THSrF50d78YKgzsJb5VV8ru-pwRgd54Nc1Wlc7EuT0HK7UxdqEoi8tjaE9Ph5YGGvX9uTBT0XoivNaOiFBIcWiE74qFY8rfm3aBx5Os3PSFpD1Sj9xGO_EAXkQFRl6ExyaVP271eeQ0onUY81qzBr4PuBPkWlD1uJTnz2rRKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbrEry1kGj-16FyfygIdw033o3sj5gK2svdoVdoKF5EXohv4wAz5dycGfjOaFt-cgF6l7jvYzUWiAtY-cQe6qZHgEyqvIwxxXP5MLF0bM3dmeGPFWtkJdpg-9XRGtnV9WtTIc6hI_D1YutZZ0dSqqveOC4t1F_7DONx7S7JwsnWf-6vpiDeKIqFk8WldoUYyEAZ_4yC_RZ-AwVkGqYWkoB4G-Pqv3_ZSyEd8P5okywcLkFFlU_fU1vq7csQWZpTIgkPrWIGuHpjKDr4gkzMU45wjewBGCcyuXaUZVTsWFDEcKoQwxBFp3T30AVOUUU2P3BNEL5JgOgVMPdZRtAGCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZGf7bGIHAZmFgmvkCgggEfnoWrtaikx3d6ggPM1dYoIHzqmMQFztAt71EijuBpZL3ow3WUtA2KHJixoXpj-rLcelvWkP2hV2kbSci0ADGBO3etyRCEubJlZo_E0185ap6Q8iMq4wq9613nxY-wMx4ZUMiv54Sfuj1idPGtARxONwbI7efuRDi8N9dNZ-Spf8nBV7qP3hSSSUckS3vC39w59TRziaDtWT_g4N67ph3Jj4zKOoWJ_nOEJthNseK-4n0rh9WygC8j6U_pbIbfZKs40rGLFu3ectKkwP8yrAHtH0U5jZcSdrATPRmW-kn8IXJafiQ6Z1_vD3PPgEq-h8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdldW3UnTQPUQ2o2gEQN7sU2IMY3L4RPAta3b4SuocOCrckxM1SMNwsvFyOkg8UYmz3hXL2IhdaaXzh8ZcJ4cPct4iDrI4WGrGv5lxeXJntFjGArYka3ZSmviue5KtTPaSjBFkjWeU02sEzrjaXeIgY_kqTWdLV5QW9aSZnfJQ14TSAgeedqeDXoVmwFbz7MEYH9tBo0L1BIrgTAvZwPRMizNDh9iqDmufDl20Ut3lAv6dafA94Oj8WNiuT_zOw5-REogzB-ViRENl5Dww64f9j5SMC-k40bA8789i8cRTkXrAgP89xuh2nw3RokZUyVN1k5b0SMJICrB9WgIho4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=qmrIvc4TYuVyoZvJnVTjqTqIaU6CNXOapPs_eBvG4tt3TfWltLNpM67kMrd5e0Kl-53Hjn17V5IPAsDQYGuYZrxBE6lhmFQ_t5VDK5RIsroWkKdY-i88bBKeZyE6H9B72hPuekFKTq8tBXWM9XvLJ-sGo4WdaF9wt8WGSShxJcIrImBQIM1DKMSQ3iMEe6PL1EREa0LiS8iBVJcPW8_sRZN2cTQ2XXqwlV9JmU9sNKYO3u4-CmOnJjMdQpnqScd4P2ZkrS9eyUx7xNN6AGPxFsdTeEcBhwYkJWB2fGuFxpMph53FAJV4XK5czzlSl5ul8C5QEKHDEEPzzHYZ7rbz8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=qmrIvc4TYuVyoZvJnVTjqTqIaU6CNXOapPs_eBvG4tt3TfWltLNpM67kMrd5e0Kl-53Hjn17V5IPAsDQYGuYZrxBE6lhmFQ_t5VDK5RIsroWkKdY-i88bBKeZyE6H9B72hPuekFKTq8tBXWM9XvLJ-sGo4WdaF9wt8WGSShxJcIrImBQIM1DKMSQ3iMEe6PL1EREa0LiS8iBVJcPW8_sRZN2cTQ2XXqwlV9JmU9sNKYO3u4-CmOnJjMdQpnqScd4P2ZkrS9eyUx7xNN6AGPxFsdTeEcBhwYkJWB2fGuFxpMph53FAJV4XK5czzlSl5ul8C5QEKHDEEPzzHYZ7rbz8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUX-wnT_vYmLkq9X9QQrFHjKv-fCyemQn7rHq9xxGM7pChPHcbBdWrFzCaugxDl2MM69RG8AG6LKcVgp645wdyuQI048r4IL7RRyQpzZ6ZQ-Zdd32BAAqGvzQSUQYl4DgPdZDbAyS9W0ihgsqLds5m_SPoWrHCuMMqR_d72DR1Ae2TNwUpzmqzwSTghqwwDh8bRKZX09SbPX98FggZxhd14jq8p1t5IoNi5hPFAJXeqEJlY3Tecw9ezpZseVfgt7tAcNZW8WYRIYW2iObqrEMLr86-PB-d1BViBmYQi0FDKuThpcpHpZ8ggtijSijtpgya22zJsghuHV-PljfKk8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfqrhAi3jARBnSQ4XVAUAxP4mOPqv3QLi9jFDLuLXIOlm_oLkre78--Pgu2-j7ZbKNVkzjpGVue460Wg8j_0waDDvIfq3p2IMoYDfXK1EZ8ALpAPh2YFoMbYfJphbD7atsNlA3vQBwKnIuKlA8L7-mY4Pk9PY3Kl3JxSbWraKIt3XnyuBI8461UKDdUtvs8G2TdLnl_gC94Hj_eIghfYCq7o1ifhpfTEHTIvjNvstf48u-lUxqeMmbBjXQsiazqjCgyp8U428DxMGfU1IKQCnEC9UNeG574mlOnK36XE3JzBrCcT7yDdgFa3RayscekYpEYczmpbsY4_ZKCwbewVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
