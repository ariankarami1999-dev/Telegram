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
<img src="https://cdn4.telesco.pe/file/MbvM7cM1rmECSaBB0EowY7vpY4CuPhuFC-lezoGZxKtirFMQe8qLj1fxQjwHj2677fJjq-x7HTZLnCpm3lx_BK_JgSFkRI1Y_B2tDvhywha_m4wY_TSjZqnAqyOBo3qgehJ8y_M3-zb_8s0kuskBU5hB_lH-LMN3LfgJcMNOCZhNRzv-W49QmpWBt0JkATmI5_ni-s63h7VjT36ryyJqDv3dD8En_jrMXCk9VMCkpuhRwD8qkyeDdkEgpo5DSbfW1SYdgySygg5-UFh0Ovz6UBZmfUgAgkInzi_mCL7OCKXaCdQlg8K8TSCt0Bc_2eU51MsZh7ojeFzCQPI3R1cdXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-674882">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQq_7a7ph_hSTfizJ81i6aetCcT6HLfVr5Tuh_1gg_Jc_s496RRbLIzyZq6VKOKhyyl72hZ4fB3xex3LYHksBOjkB2br4y0Z1sUH9uySjEYof2WYh-olZD8qgeGDctiE3EUT7qk-998d258MZSJAjujs3lDMg9bdd83C4pwsoVnEDYpW4poMwKSB2AV7ccaLZE44fzcisfDdeAsjyRC7YTi1ds4xScMYgSfZBJMjTayypL5dEeyk0Uuuy4R4os1kmJ-gI_E5g4rQXocLIHIWuxBKESKl6voikvS_4TIyiHNSSiAttVm5zbcjuuZPzMH9uqo5XExVMnuoH0KaaMys-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک نجس: رؤسای جمهور چین و روسیه به او اطمینان دادند که تحت هیچ شرایطی به ایران سلاح نخواهند فروخت و این تعهد شامل شرکت های چینی می‌شود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/674882" target="_blank">📅 18:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674877">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhzjiFsGuWkg_lg1HrogtznIgxHfLRSDlR7fmOVLcOOt4wJ5ASOuwUZjs6lR4Q47mU6IuY4DmXwbihc1OzOsqsPTom23tiRhRWQUshxk_56PkiPTazhaCPr9Lj56JWw-foPqVX1CPm-P3z4GKf65KyzgooTqC2f4VCNvnKTRAsHGej-ckbhcz4QHFiEEKspzmvOBQ0TvzVALp42_rQmIdeG0sIyi8eOWSxkATNrNgm1EgCz7uxSDIqUre5LGvMFUsP-zGEd9iG_xX_MHaoja3Nx-bYko0z_Q1GQzSboKiNNjaRtUe3hBNXmxnu-Z1EbBr7oAtbsadMccxvTlBZN8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF5kQDvowoUcH0L7oVwyeXW8OVTce0IYRgs4-aqDVIze-2kyB1BEOLRToiS4M_-HrVT4K9GUOx9g-GiQaJYyzui01GhwjuEU38EDRBxfvsYWuyl4ugk8SBQWo6yLbWqai6Jt7NBdTxoXeFiiask0X0o7UldoN9MqBFmSLi2TN6Yki4Q0va4tssfKbEKC6gFXHsWcMGBwyNzopUEcS207vomLrZgRIim2Fq3nz44N_zG69h9Myu5Ewx34Ii2xoR9ElHCEtMC0buCSrWUfpT-g7qMnD9lgNXoRGLvkL8jk51XXPxgiqf_F5JkFw5xp-YqSxsX_bA6gaMjUuHYBio_1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7clOa-XmLGi876mALnHxdN-U6C0BfysGTUyjM2goahAx6YnZJ5LfPvl3jXMmQlY0Z7AGTqvihY0pXAB0V2lW3Dosnrgsse_D-Dd2utgU6R7tVlQquz4ZfHeEcDlNNhaRO5jVTXiANR7KpiMvBEVOTMUceqOA_UILHwEItA0QZKseOTNdDbndlNsXydPOe_s4tHF55ch0x2oQb7Zhf_WM48SZDjj5KBKTZS7DekD8-JSx-jeUfXIDSHleTxfqDAGUUHV93aVXD0Ehf6-tM77CKEIC5tx5h28ZCsfcVzSxCVVmYVmAae8X_4R_2XBE4AdiLg2ndPhSCdNHv-gvTsHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZg3t8EDKKoUga2HFBDkXG9YEyk7BtgH2n4h0F2RdRk3EXXrlS1g3gBmFNeLiF5WjWBjMGg3ELFK_TiSCApEHoqCJiIwWT46lQjT9BKhTvHDtP9S2JN8-GrmBT8QLe1bx6mGcLGdeFvSZmzEteIFX6tIpKEgkAw7YkbyCsx5CTjYCp-w_9_AMbLN93lLkKc8u9cEOT0cJlMoHfjSYw927Em_uCBXRZLvuqF8vk6VV3VVMmt3-OyPGkU4IchLI3bQvhO-1lU8nsKd3evZYDpmJ1sP5_eWe5JTMQyrO8b1zGAaG3LTeC7UCYwGknE9dvyKJhkFnAF7dzFrjNcydWojuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfQT2Mhv8EEPATSzvBuoMoxB3Tt0ACvJ0hDdtU6gTroYdfEWL4KY6iiOebxNkBVQ-eUeGHLx_DakrZV6BENjcVDFIzWbNAzOVOrsEvlUjDDIV1SWNGzHOMpaGI1MaZrF84kSQJBTg7RqUK7hdQoFv9OnJ0UhKUkjhYZkyz8R8xb6Vd-rgHWPjKf8JvS2_Oh7HYc3izR1084Ifb9oHjx3V8ekwAtj6OPnvsbBASW7VSofUdSiUlttXBnMD6-IxC3J9Hn9wdJ-MUeRQfW-6OaJjGIurrqR5LvbC9qveNMKjeeYl7xyfiGgEPjrt9VwFESJQf2a4-S0OlhAWU3qeG7TOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ ماسک خانگی ساده که پوستت رو شاداب وشفاف میکنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/674877" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674876">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8d223b51.mp4?token=hBOoyudxwZeX23T9CYOqqOT1Nx70jFDCxCsJTjdC6LCN3D9gP79Z2jcsu1cAnM97qvJJBInNsnXD2zC1zohrvbowLDtcAEP47kHFvDsXTy3mL1EJFFDgloiu83fL7WT_MlEs97nLTU8AczrKaSF9vvguZlH9yMbmlQG1pqqDiXPpBKbcULtdAKsdfoFk48zzo5tKSKvZi_comNEH1Nm6fFXqfWMLEUTvqS24GJeVAkNDr414wRfcn7W8sN-6SvVqwtLV8AyEPRpqOuFNyhvK_JakCVjgXZa5P5pRRJzO1kPXop_4GHZgm0qj3jIV5JLyoFpzwjOgGJoGMZx5lkQe2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8d223b51.mp4?token=hBOoyudxwZeX23T9CYOqqOT1Nx70jFDCxCsJTjdC6LCN3D9gP79Z2jcsu1cAnM97qvJJBInNsnXD2zC1zohrvbowLDtcAEP47kHFvDsXTy3mL1EJFFDgloiu83fL7WT_MlEs97nLTU8AczrKaSF9vvguZlH9yMbmlQG1pqqDiXPpBKbcULtdAKsdfoFk48zzo5tKSKvZi_comNEH1Nm6fFXqfWMLEUTvqS24GJeVAkNDr414wRfcn7W8sN-6SvVqwtLV8AyEPRpqOuFNyhvK_JakCVjgXZa5P5pRRJzO1kPXop_4GHZgm0qj3jIV5JLyoFpzwjOgGJoGMZx5lkQe2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ایران زیر بار قُلدری آمریکا نخواهد رفت؛ حفظ حقوق ایران در تنگۀ هرمز جزو اصول ماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/674876" target="_blank">📅 18:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXUWlx3cSzwZWuYHCVrHLkHIHWZNxwu60uZQoKEIhD1Iz8KjRqNX0wxM3Bhk5RXX-H-tup2t5hjXUjw4_ewKXx1kAeIba5JbxrDsLwV2x8h5qzt8lik8-d9v_gByrySMiQd7QsWWEbtUNia-EW7ixbEj9m909cEjQTqlWxOf_sVI_JRjeRucQALLgFvl35eAwQiL2URaoUGsOf-gC9EmYL7Is2nnZmBV-ldph1iGuLSFCP_sfi3UOoeVrnUWQArE2cbHP-YT-_5W-Y-bwIUscPw1M1YbAjCwymDIu21UZOVzjaXLOAKG4OYeBDEys3RabYqrnEusDETCZP9nKTmNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
پس از فراخوان بزرگمهر حسین پور صورت گرفت
استقبال بی‌نظیر از طرح خودکار بیک برای طراحی چهره فرشتگان شهدای میناب در نمایشگاه شهر آفتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/674875" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
یک هیئت دیپلماتیک عمانی برای گفت‌وگو در خصوص ساز و کارهای تنگه هرمز به تهران سفر کرد‌ / ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674874" target="_blank">📅 18:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674873">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سپاه ناحیه بهمئی: صدای انفجارها در ساعات آینده، ناشی از عملیات کنترل‌شده انهدام مهمات عمل‌نکرده به‌جامانده از جنگ است
#اخبارفوری_کهگیلویه‌وبویراحمد
در فضای مجازی
👇
@akhbar_Kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/674873" target="_blank">📅 18:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت بهداشت: از ۶ تیرماه تا کنون ۵۹ نفر شهید و ۶۶۷ نفر مصدوم شدند.
🔹
آسوشیتدپرس: توانایی مسدود کردن تنگه هرمز اهرم فشار فوق‌العاده‌ای برای ایران است.
🔹
پلیس‌راه مازنداران: از ساعت ۱۵ امروز کندوان یک طرفه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/674872" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674871">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9699dec59.mp4?token=Dj3S8kKv_3kyi8shuvtnCPSFw-yGGan5vvD0m6yiti18qfwZld2YKz1y4biNKz4UWt6NURIBtZetJduhuTqpBGrPmszdeVYX7792-mI43-TjeW8GLlLoXDXqzIaHKUY6LSxh8GC1D8qR-CtCVBv2IeJQUo-b3V0RGL99ag9ZeYsmesnxC1EGtwCWFCOMyZUV-Y8SJVZwV2mYA5_DQB3ReOFForrsJG50AwbTy1WI41xlArQC_DIui6K9fp2rXfzUnz-J7H5WboFs6Xf-9p51FB5G5OyzkpUqgOWNT1IhAkZBya5j-JcGoqFj9VfSFInqp0vRmnYc2o_G_P0A5CNsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9699dec59.mp4?token=Dj3S8kKv_3kyi8shuvtnCPSFw-yGGan5vvD0m6yiti18qfwZld2YKz1y4biNKz4UWt6NURIBtZetJduhuTqpBGrPmszdeVYX7792-mI43-TjeW8GLlLoXDXqzIaHKUY6LSxh8GC1D8qR-CtCVBv2IeJQUo-b3V0RGL99ag9ZeYsmesnxC1EGtwCWFCOMyZUV-Y8SJVZwV2mYA5_DQB3ReOFForrsJG50AwbTy1WI41xlArQC_DIui6K9fp2rXfzUnz-J7H5WboFs6Xf-9p51FB5G5OyzkpUqgOWNT1IhAkZBya5j-JcGoqFj9VfSFInqp0vRmnYc2o_G_P0A5CNsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار طراحی خودرو دهه ۶۰؛ نگاهی به کابین افسانه‌ای تورونادو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/674871" target="_blank">📅 18:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سی‌ان‌ان: کمتر از ۲۴ ساعت پس از امضای توافق همکاری هسته‌ای غیرنظامی میان آمریکا و عربستان سعودی، دونالد ترامپ،  عملاً این توافق را با اعلام این شرط به حالت تعلیق درآورد که تنها در صورتی پیش خواهد رفت که عربستان به پیمان ابراهیم بپیوندد و با اسرائیل روابط عادی‌سازی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/674870" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
منابع عربی از فعال شدن آژیرهای خطر در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/674869" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
منابع عربی از فعال شدن آژیرهای خطر در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/674868" target="_blank">📅 17:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
دفتر نتانیاهو: نخست وزیر رژیم صهیونیستی روز دوشنبه به دعوت ترامپ عازم واشنگتن خواهد شد
🔹
او روز سه‌شنبه در کاخ سفید با دونالد ترامپ، رئیس‌جمهور آمریکا دیدار و در مراسم تشییع لیندسی گراهام شرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/674867" target="_blank">📅 17:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674866">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_iHtleuvUSvzEacX994KEhgkAEITHD8B69-WWjclxQrzG_8HSwAFDVm_oCHC5-oz-3WI_LtNSLgC-9D3BBlaW72I8JI3M32h09B8tWUVquPbVxLSdOUJYO0ieIDp6psOPjuODV9975SOpLAbK688Ic3BWjLNfYawcAS_VDu5Fk6difdaam-UCJbFhvveHSLNx3hDHj28T2rIwQIzKHMeR2t9VN1wDI7K8vY72vfXC0iwoihf6OnqP0BBu8RM0Z0Z7B5BISe-pmfpOx4brogq9Bv0YGSnM7amjDVCiaYqlfVpkeZFvu-JRRbYrlh3nhA2LdkzUWKRx9NV8Alm6NSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقلام ضروری در کیف کمک‌های اولیه در پیاده روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/674866" target="_blank">📅 17:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674865">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/674865" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674864">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDyDsnYO0xaNbmRx_2G84zJy664qbOeiK6KLcpaCvClcmzsEYSk3K4wKXSZFdg6XB1jJUMqCxGHL5lDe4_z-3cXwNBll2zIQpXVy5haXrMrL-33WbySf5Z1p-SfmfXHEu24AHRnSSPyKXvT2ZIhGMQvvW40lKx58BYPBO458MaCLkzpNgqwsF3hjc_wo2AIDeYBk0bYp0guoodZ4nBFPp5d6pOtlSLzDo-Z_3qrHlYZ9BztVXVx5ojVlElIvsQF2_6aElZ010soUL6MX3csrzyElwktLUvvyOjg09MW_lk1ztuHtvAedgjhIP_jbmAZrScVGvkZ8M4m3Q7fytlzFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار معشوقه پنهان ترامپ با زلنسکی | از نازی‌های اوکراینی تا توهم ترور پوتین
🔹
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین، در گفت‌وگویی با لورا لومر، فعال رسانه‌ای و چهره نزدیک به جریان راست‌گرای آمریکا که رسانه‌های این کشور از او با عنوان معشوقه پنهان ترامپ یاد می‌کنند، اعلام کرد که روابط او با دونالد ترامپ پس از تنش شدید در کاخ سفید، به شکل چشمگیری بهبود یافته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3232773</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/674864" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee7fb6622.mp4?token=JdQohwzGrefOd3TbtO2JKv5nF9946wE90rlfmuQqMzQRfVY6MlFfJ6wP0pmjrIEjqD_6zKLntDpduo865kXcrWy8oUgVorSMa5mdhIwGnFrVul5km5J6bsRBFqpPH8XVBplBC4sXz8oUcansJt7FAaI5SOdXkAGvPH7h41cQ7_rIzqeEhh_12bC3vrheZyno5FcqYI_EkR90yrhjxjReBnFcz3yNRYWI5KWhYM3DgSVuNAvZb8UZTp7Jo2yr6UJbpgdBUlFMzOMEZaKsFEDvAWqn_i4zDy6fvlefMmnRfjmUpWCOpZhAiGpyF4x7qvFW-LYEL9aBZdjLWYFLq7DxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee7fb6622.mp4?token=JdQohwzGrefOd3TbtO2JKv5nF9946wE90rlfmuQqMzQRfVY6MlFfJ6wP0pmjrIEjqD_6zKLntDpduo865kXcrWy8oUgVorSMa5mdhIwGnFrVul5km5J6bsRBFqpPH8XVBplBC4sXz8oUcansJt7FAaI5SOdXkAGvPH7h41cQ7_rIzqeEhh_12bC3vrheZyno5FcqYI_EkR90yrhjxjReBnFcz3yNRYWI5KWhYM3DgSVuNAvZb8UZTp7Jo2yr6UJbpgdBUlFMzOMEZaKsFEDvAWqn_i4zDy6fvlefMmnRfjmUpWCOpZhAiGpyF4x7qvFW-LYEL9aBZdjLWYFLq7DxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعدالله زارعی، کارشناس مسائل منطقه: مطالبه خوان‌خواهی و انتقام به‌اندازه تسلط ایران بر تنگه هرمز اثرگذار بود و بارها واکنش ترامپ را به‌دنبال داشته‌ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/674863" target="_blank">📅 17:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXjcJd9dUSQcYrc0iOMQwrPPywhTTIZcJboEo12GY7Ip44DsA3u5BHpNHsK2qHQ9JhhXkrwl2BEQFATvokFcYt592TFDukrESIyI7b9mRaoCyErNfanZASd38dRQbsxA6smrKOUjlE3FJvgS3N9pfEXE3k3nuEdIrqzfbLUqrNw2Dhj9JTx7rfCdWwi8Gn_SRcFLKRM23Q_EMwvQnYZdRvgMzzvCMxRHWdK5x-a9WOODiv54uRzRLQVpEdWI5JwiGiOeobI3hhV4UlMJMFTqK8Dh-m9Eir1Qp6CRy2zXW8HJxTq-vhUUUJI9Y-EBbzUm38LoZ6IxGy9PrY7hz1F6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون آمار نظامیان کشته‌شده در حملات ایران را کاهش داد
نیویورک‌تایمز:
🔹
پنتاگون در سایتش آمار نظامیان آمریکایی کشته‌شده در جنگ با ایران را از ۱۸ به ۱۴ نفر کاهش داد.
🔹
۳ مقام آمریکایی گفته‌اند که دلیل این موضوع این بوده که مرگ این ۴ نفر پس از اعلام آتش‌بس توسط ترامپ در ماه آوریل رخ داده است!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/674862" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/045a827bf5.mp4?token=Xvb_98Kfq1-1DGVNVHBR-2-T4LItSNU816mnKWWvJK5DvktBR0ssjXkfZJsOJPgfrt7pl7TllqRSuHM1AKj5plieeP07GOJMbU9wQMIjCMbggQ7UvSeXY5Pk3K8WgmZ9SYT58IB9mf25o1v_SEJG3zI-6URnBnqds1K0DcT5UzR5VfzbcH-Fc89kglQmgjh7q_stFVskh7wGw3uuemkrWd_HVlYMISAsBlk9fSGkAsbuTUw48Umrnu-FboQ6cVKeyoUXxdCYrAmpuF7a_f2EPRod4D4TVdAjq9uCrW6bbwGuPwVCUSyHLUfaJaE3foMbZv-qpgZDkYkeku5rrvw82A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/045a827bf5.mp4?token=Xvb_98Kfq1-1DGVNVHBR-2-T4LItSNU816mnKWWvJK5DvktBR0ssjXkfZJsOJPgfrt7pl7TllqRSuHM1AKj5plieeP07GOJMbU9wQMIjCMbggQ7UvSeXY5Pk3K8WgmZ9SYT58IB9mf25o1v_SEJG3zI-6URnBnqds1K0DcT5UzR5VfzbcH-Fc89kglQmgjh7q_stFVskh7wGw3uuemkrWd_HVlYMISAsBlk9fSGkAsbuTUw48Umrnu-FboQ6cVKeyoUXxdCYrAmpuF7a_f2EPRod4D4TVdAjq9uCrW6bbwGuPwVCUSyHLUfaJaE3foMbZv-qpgZDkYkeku5rrvw82A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظۀ شلیک موشک‌های فاتح ۱۱۰، ذوالفقار، کروز و پاوه در موج ۲۷ عملیات نصر۲ علیه اهداف مختلف در کویت، اردن، بحرین و اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/674861" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-qTq2iryrb0cWmTPeVg-dICIwEfUdjcWxdzU6l2j-rDeNYIpl5LaWE83ToQYeOxGJCBI_e7mH1V4sAPavE9Gu-IlJEF1Lny9gD51zFfSQ-cq3FPAjbehNxrcv9C_TTmUumG0-TjACsGIp5oGhvEgOMeqddKtdowkOR8NN_wUwtcib3pUCB1fgiE4kD-ciZnmZ8KOX3dWA3potMaTelbPATX0DKhm_riLcNcKG_H6je4K0mmMw39nNyP758njJrzpZEBQo6AgHvYFNDbGXuTk1pD6g5xSOTo07IYKB1EnLMRMosUrXIBMmu4X2oo0Mw4mBG-Jeswfz55aIB-9EWrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDSgZBUwC-F0GkeesNeqzn56NEOvCwMfeKK0LPma7KzCtJwI9ivEc5PvxCDCgf6g2aGYutlAERw_fBxQPNvO_HSH36A5NNt43T3j9sDua4NXnCt5ZHEuQR7MebOUum6964t03UB1c4c4a2kIBXyrnhEpyVKNzyCVPHMKQClhfcGPrAvRF99tS-8P65L3O4AQNuPZItv300R3d18fIqUSdk1JF9X93QKtwQUrEoG8oX3iA42ssKLuXSIjeGXsYaKcAl8zCsLCUwguhjJSL6rU8-wqxzVN526nTBCHqqwZ-ag1z0xlGe5rdZuWtDFOICXZCS0n51yBFt04aD0sX5H2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8cFp2oX1H_9s5i0153TGkhz2uuWNu9dfTYI00p8hGle62-mjNQMwU9Fca8PzcuP5MAHbLw0qVuECDge7BG1PHWQcqaO4YFbnq2Xo9Big3uad9X_oP2QniQ6WjvSfCzVcOYc07BgMy8oNDIfDlLFLv6LQEgSUC14e1z4oXl68Ge-KfladbTenuPHHfN03OsYsY9YkTgBAFXDi23k1fHEAEWAqIcS2NT0nSGNn8zZuKDEMKJiBofSXCNLTPZMCWVmossfq2ejx_0YoHkgMT53EDz87rKVRVXQqdMYD8-j8R9k17LaQ62J6XjzFb4bqI7hwMWoaul4AnCQFzkYaeM69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLqr0-4nG1Uy46iK6NE7CM1mcy9hXD2Tn95Na-lzUbumbSoxUjgpgqqcc9v5i2Hl2Jy-l39cvTBrumItR_WiieDE8GZ9RjhJHcXMpuVWpHSyOTRfYKfPlmlbwZ-Vy8AzTmGdJLeSLn6fGrvgOy-liKBAfwsQtQ5qDAp3PAgXwFcIvf7bl4jQJttWsRTHUfsMdNa1lCmtjOUnNfe7ez294vUYevYYjBGqt--QSsuxb9OwDkEl-KOjblbBh3r_kAg25-caXkLyA-cEr1UjDODPTnX45e0Ql5TzXnDCw5IcRAfWb44VsES7aZ5r0e7s2p5sQ5TcF7XOWR2LuHFiKyvRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfFO7qR_5tf2H2W1laq0C00Ieg8U8iNrE9EC5pIeHnAIv7lW2DzzCTKcAIDg8YCJJSKs_mt9eUfhncU05RQ7mDpHGYT9J7Du3ybnqY_hlk2mF74eNXgC9suaSp_kr-LqjxO8rf03GiRwmgbKZjTYd8HuhuYRjtqqF8QU3FKehcRFrC9Bs6hifvbrJvdPGgoMNMeK7rAngyK1tczAeQFc_0wl94y37DcXTy8xZlT6bzzR8H4RpWhqaP9Wy-Y51IeafAfhiH-in9AB73BAq33J7fT8ipeRhVw_d4iAzyedX7lwzlOlEbRU3NGhQ-cd03v3pPKx-REANYCGDsyy2JOs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzISni1cGg58bd5g7qBwzVY7FxChJD8BiZDnMfqv2sk9_whbtdMMzNkLNFXFMVSMY3uCk_yez2Q7P-IalGpdLcVZpkBlQpDG-XzPncFGBL5TVeXw5gsmO4S9NpETn-PDj2QzUHzAVtifCaFepvtKHWJSq5H9fDM9EoXfkhO-FFW6dG1F9-Yi8uH2D_a2bes3drVlRJ4bHG5DxokkQ3dCpRG8Q6B-cgRhf5nR0TJfHXYb-j9V3EQY9D-vJ6dYiVdPI0185HW2pAsR8XLcMoqOzjwrJzWZaQUvSIKDpasfRaxLe0xogSxm6XMf_oDaKofw3lK2hXxfLKywmRSeCnDvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QS6av2DvTwRfa0bF0M87pEYGnFpZsM7vDp2XHvWmK939NBHQlsRDGUH7Wp_1ROrdWSOGuTAP5yU-LvOg19FuDFF632461q72IifS0fL76zNDZ5JR6x2agyfyKneXs9YA4wcFCS4cEU6EFKV2y7da8dmoelfFpx7mFZUF86_mj4o7HIsU8YYlBv1SVGerS9bYzSougjwd79oxTDAtdQ6VqVYykdBsKvMlpGD5j2PQLvDQ9H7rihZj4S0_U3wXq7aSZR7HChpYmjEPYDHatK30XT3dkdOkKzHJ1GGFYNVsVgGT4GL-8YiCy40ggFLDHqhiXkf0FzbHM6c84aeG7YFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHuv5m8AInStrwDGstJANo7vlxbznokzKCvniLs6QXYehNEtQLclhYlZgRd_2-m7QgDIlGDLV2pB5hoKeKAzEIVcdX1DFZcJqoYcKz4N4hQSJDZdmNcovT5iTIOsrmPAT_Z_Nvmx0LVOeq-P1t84paUz3J4FDIhPw-UzSXiYEOeTFJNYpSAXX9dnG9uc65T50cOy-8bhkeZrFRTf_oZO3eGwO6FMY7uKYphpXZXg8W7dBdTcncP60sRgqattI5dcuE0Y4HHKwHvo8xbduPcr9FU0gSF6UOzTwr-36Fm4aUIPljDSO8__IkHTXpXsbt6MjM1im3J33c-XG2G10JL-bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش گسترده کاربران فضای مجازی نسبت به محدودسازی کانال خبرفوری در برخی از پلتفرم‌ها
🔹
تا این لحظه بیش از ۵۰ هزار نفر با ارسال پیام به درگاه‌های ارتباطی خبرفوری، پیگیر آخرین وضعیت دسترسی به کانال خبرفوری بوده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/674853" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0UuYi7XEdLUfYb28SxK7DUtXSe1mDcAElNZKVw0MqjYkiNg8JFw_EpMjGPrVuI9xyGcCO_pODceJ4GucSfz6_f6yEYMdUSZlC2xYfEaDjyhY1Reiv71mOMgNrTkoYaRScPLfi6kSSAu1bJPr4Lh1jPG3xORNjO7f5oWVSD-7Hz43k8_eRd56xdCC_5--oZQMxSb0soAN5_WI8_yDwBP4qihh_vkWpFIvka72AUaSMUq85rdHbotZ_er3dCoX3NHTtpm3CbEG3LYbTUcH7M9NhHTEGNmkZp2Nrbe6DEbJmw6EyYyPYIXCrtc1fczzLbuzjnG0t_gY-9J_JLzQ52jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1UKrct6rGqYFdlX8LD8rYADPLwPqjscUe0OvaVZPMHPKoelqgC6x0cuozqWY3f-vZ6y0tju_7YxDZk9Vxa-2uOIWIrjfY5jypmJTWfTaiAbhg4YRIUTqpVnQ5sGiPcShn5AOFQrGaeGtr7jGalMcQaEjHEH4YIQCsVJEeXejuXkpfAAjcwGoHGyITDqgl7AWnmiNgMkgxKXyrDKFY7B0vY6S250rMYb7tpYvRkbcVaVHcWgdewpQD8dM78rfQeYbPFldMjbG-2HsaGJRAdYT2L1sYnuxE_HD7X22OYejJByIXMbtVkEWWhczeIOCl8rV2DVBHTWWPArGiZZnFVlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSzNmOmicyfHcaAZYuiSG70j6kz6jZDTuvcCq-YjCtyR-41zuBtdXZDEHFgSAHerF8zZK2PbQe6rhl2_Q2Qxa-IFPDz4mx-3XtlVuBQs-ZiisgOzPp38cUwDg0E7kr6PxhnioPSC1Ntu8Ehd1WwzISse12HG1wKAGTZ10DKSXZNF4EqMZAqZcp0vIIYWSVSJ1-Ct3LSrkEry-seQnIhu6MP3Kovvjq0okwwi5pUJr5RL9FUvbIDLgn6TOPWqtxpvJFIhrIfrsI8xQcd6MS_rKU85fYD73AxHHeBI9gDXUFz-xXnCQ4wl5-1YnFgsRzZKFyEp3-mHkNFjFzosHHBhUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۳ نوع سس جادویی برای چربی سوزی در غذا‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/674850" target="_blank">📅 17:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79956eb4be.mp4?token=APrx4eMgRU0ku-Hy9T59EvSF5tMwj1-GMzz2PSb2sEGw8QhS--UGuiBom2cQ-vdhpR4kmUCowNZnC9YcLm031ppHAsbic3tx1UfvSjXpMRay5o4orlaGVoJeP-DGaqx-U6DUbRfSuq7ViTS3PRRFixaUnZ-bM9v_e24GaOqSs4FZ9F2DCt4_rm83IZQ3RB2sXlu2abtHlMhYMfWV3TuCcgMTvI8vP2P1HwUeT94QD-4g5ovTonGfmI7FWrYMHrQ6Pr5qdM9M9p_ISO44fXRLbyNMP-Ia1bITfwpnaa7Ja5-cgg5UxATxAO2-MD6lVKcZyiLucMHa8Wyh6i5MlTngwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79956eb4be.mp4?token=APrx4eMgRU0ku-Hy9T59EvSF5tMwj1-GMzz2PSb2sEGw8QhS--UGuiBom2cQ-vdhpR4kmUCowNZnC9YcLm031ppHAsbic3tx1UfvSjXpMRay5o4orlaGVoJeP-DGaqx-U6DUbRfSuq7ViTS3PRRFixaUnZ-bM9v_e24GaOqSs4FZ9F2DCt4_rm83IZQ3RB2sXlu2abtHlMhYMfWV3TuCcgMTvI8vP2P1HwUeT94QD-4g5ovTonGfmI7FWrYMHrQ6Pr5qdM9M9p_ISO44fXRLbyNMP-Ia1bITfwpnaa7Ja5-cgg5UxATxAO2-MD6lVKcZyiLucMHa8Wyh6i5MlTngwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره جالب مهدی قایدی از خساست بیرانوند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/674849" target="_blank">📅 17:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اتحادیه اروپا ۶ فرد را به فهرست تحریم‌های ایران افزود.
🔹
سی‌بی‌اس: کاهش ذخایر موشک‌های رهگیر و دقیق، دولت ترامپ را نگران کرده است.
🔹
هاآرتص: نتانیاهو در تلاش است اسرائیل را وارد حمله به ایران کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/674848" target="_blank">📅 16:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=ZWOk3cV0xU2H-U21KWHCduZJVyuYssT8efmKFWwND86wKL_myAULhNsuJ9I96AM7PzkqleR60oYdLvoUwm-stg-L7nP_svNQStNXG983dYL3hoeuyIJx8yoFpozXfs4__AeXxE4FlQkXZTMOcmuHQi5RFAu7LkVzOLL4gyUtbQFBecB5e1QLekSnyWVGo1-QhYYmoZK71A7rEM1eJp3E5wwgBHX5oXECoNnvj3wSi-Tm-CLWRrCV_oqoXqlKf7D2h8H8LW56Ro0dVZUI3HtuI8v15M4cqaQaPUiPCb_ozjJbYUYFTYpu-Zno6vPteKv4N-iQFtUnc3QOWx1TeD_rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e3dc7e56.mp4?token=ZWOk3cV0xU2H-U21KWHCduZJVyuYssT8efmKFWwND86wKL_myAULhNsuJ9I96AM7PzkqleR60oYdLvoUwm-stg-L7nP_svNQStNXG983dYL3hoeuyIJx8yoFpozXfs4__AeXxE4FlQkXZTMOcmuHQi5RFAu7LkVzOLL4gyUtbQFBecB5e1QLekSnyWVGo1-QhYYmoZK71A7rEM1eJp3E5wwgBHX5oXECoNnvj3wSi-Tm-CLWRrCV_oqoXqlKf7D2h8H8LW56Ro0dVZUI3HtuI8v15M4cqaQaPUiPCb_ozjJbYUYFTYpu-Zno6vPteKv4N-iQFtUnc3QOWx1TeD_rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعدالله زارعی، کارشناس مسائل منطقه: ایران با حمله به مراکز تمرکز و دپوی دشمن، از یک برگ جدید نظامی رونمایی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/674847" target="_blank">📅 16:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674845">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
انجمن انرژی آمریکا: اگر قیمت نفت روی ۱۰۰ دلار باقی بماند، میانگین هزینهٔ گرمایش هر خانوار آمریکایی می‌تواند در زمستان امسال به ۱,۷۰۰ دلار برسد؛ یعنی حدود ۶۰۰ دلار بیشتر از پارسال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/674845" target="_blank">📅 16:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674840">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oapr1fS1844St_uLoVR7aNqKnJYBQGqgRSEyKN72ncHjapZ0UrZjtrx0ekbK2uOXhV7LBK6his73terLF6b81tAzsgrl71Gcx6D_gXq5VxfWRMwV1z-o5Kc6p1GM4i_U51x3I_5FB29l1x_SrNzMb_jTqZth9lT3VjSwMjriIJ3abkIX8zTc_PrTamYwTGd5jud16D0QprCaUFkQjt2c9XG82Io48CaY7k6UyQ-mOFpzwjoDjLmrWYuBnSzrmL2NmnleTbyXSQKscGFX9GAoPRf_Is3YfhKMvHTMZlLpa8hgeYXh3Fw6HvQ5a6oe1J0iBMNOofT_jngcCMweMzm-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0JuAqMLhGNvVgEOX-Nb7Lm0ZzqsTDVlZr15W8n5QEG_33RpaGdts4c6b_n0PV-Zo48rCdmC-vbeSc41admLBFLStoSiuKJIpl7g-I65bElfh_lYOq-r_giDf4gDWXLN8oJiGOf1omx86mCWXsjinOfsDyevPxCvzsIa7lf4x5rNaZ3cxkF21n5YEiEkuUKBiNwInY3WaR8vTTsnNj_hCCRBzSHxWgOnKNhuqGdHeRkYI-paAuT0CsKXdYa1zT4YpT3bNdR4vwH4EbEqcqgbgDHt4fIDjDOffMltj5syuraUSnzbfpCJN5pnOeo7UfZr_U9lfBzwpLYiHqF2Vc18rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2BQl98PYwTeOl2Js_uaQwkpCMwM1Ztg4rbtpRBOc_BVMA2av0qJema7qlpHzAf3Ps7hc1hzc1ab5HyQPk2kJwHSJcWmag7PIe_yoP9MQQHdKV9Y7uncljTI28AFKfIE3hJwdhQjLK2vbFyymSIJ8X6Rg-o3SN7TBLxLk4sF9ZAIY_kS4XKYevXQSSGF6Kvxof_8HZVLDwDiToNj2ljXik2ASkgh0JsXPL8ajaspWCGRdIVixHkThYnNZcUUgs-iSsabu8pQZam3tahQH1PHgw6O9XV72Az1jBY6j9WvGVInAHvIwugw2orm-IqI1xGFbXUVo7aGxC2e8NmUQ457DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFypLs457c0KHi_X0M6LAu6NwFIW4W5WElAcqa-_yoAZHmUAwQCZaaHzr72wsJERnSsRP9Cty4i4rgcbfIi8NeaHE-Z18zRDeV7Ad6YO82NByESwaSXySRhqxfCYBJYySC6j8J3Wu9tGb7gG0cNB3oY4kctla-1JpJD39JoOFlcStlSfstMiLSaOiqkQ8wacbs4GtIwTrY0F4m-aVVC7yEbzouzaaYhre8w46-baQv2_QqmzfmIwfxSnR9LbTjBatOy3HF6CJrY7TEdTTq5rTxOAfuxLQLxw2ek5CZGCa5LOloVEqAFNloA_jZHHdopVUoWDQGJf_-5n1rnJcc9EJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازار داغ بازی‌های دیجتیال
🔹
گردش مالی مستقیم بازار بازی‌های رایانه‌ای ایران در سال ۱۴۰۴ به حدود ۷۰ هزار میلیارد تومان رسید؛ این رقم بیانگر هزینه‌کرد خانواده‌ها برای بازی‌هاست و هزینه‌های زیرساختی را شامل نمی‌شود.
🔹
بازار جهانی گیم در سال ۲۰۲۵ بیش از 180 میلیارد دلار ارزش داشته است؛ آمریکا و چین با بیشترین درآمد، بزرگ‌ترین بازارهای این صنعت هستند.
🔹
بازی‌های موبایلی با سهم ۵۵ درصدی، بزرگ‌ترین بخش درآمد صنعت گیم جهان را تشکیل می‌دهند؛ پس از آن کنسول و رایانه شخصی قرار دارند.
🔹
۹۴.۵ درصد بازیکنان ایرانی از گوشی هوشمند برای بازی استفاده می‌کنند و بیش از نیمی از بازیکنان، بازی‌های آنلاین انجام می‌دهند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/674840" target="_blank">📅 16:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674839">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3d111df1.mp4?token=SNOFT0xCBvvjA_IVjC1nLYQQYqRaN5RWs8yngQMUCSpCN4i5qos9r_m1UKWSvyfdoeOMOaOQbdYo-6TXhJSpnpMQWIm-MbkdHwvrlKY-5Irkq07NWiqCu62lNBu77tCzY11w9RVXnwDcrgzB_0lmQ2ALTIq2hWRNtUHQ-8D2BR-pqGrRDDCYWySVVdsXU_Mk9GdkJM7U8MTQslcN0i1-JhO4pgBwO1YI-wvALKeuZZadl0PFOX8KuIYpLd_12fY66B71pwdRyEh9LEcrr9KhnLOnJId6l-2ihi5wV3f97Ml5wtJuyPI9EuAf58dMICXtA1Gt_FRzK4ZM_zkI-sSoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3d111df1.mp4?token=SNOFT0xCBvvjA_IVjC1nLYQQYqRaN5RWs8yngQMUCSpCN4i5qos9r_m1UKWSvyfdoeOMOaOQbdYo-6TXhJSpnpMQWIm-MbkdHwvrlKY-5Irkq07NWiqCu62lNBu77tCzY11w9RVXnwDcrgzB_0lmQ2ALTIq2hWRNtUHQ-8D2BR-pqGrRDDCYWySVVdsXU_Mk9GdkJM7U8MTQslcN0i1-JhO4pgBwO1YI-wvALKeuZZadl0PFOX8KuIYpLd_12fY66B71pwdRyEh9LEcrr9KhnLOnJId6l-2ihi5wV3f97Ml5wtJuyPI9EuAf58dMICXtA1Gt_FRzK4ZM_zkI-sSoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواد تاجیک، راوی جنگ در تجمع محرم شهر: فقط در شهر تهران در دو جنگ با دشمن آمریکایی و اسرائیلی، بیش از ۲ هزار نفر به شهادت رسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/674839" target="_blank">📅 16:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674838">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbFM2ctKJ7o8lV0ne7mUxhsJdJLOtt1VYh-MmUo0B3f9de0heSzSuPodRI_5EXjh-zs9DXHVJuimNne5Sv2C_Yt-teVTroSm6x0B7y4QsxLvjV9eK5rh3lg_HZVknXFK6bZj6oKj3o-whEAowe3KniXGV-aGJEznkZcvozQTW1Ma-lWD4IoSHpLVcYLFnNf4NG7RPK0RYud1Nd52o90EJqLce3gf51j2VIjbNur8GUx-ENSBwjXGo57H-FO9F18p_NYSusb8lqnM6cCyaeNXrJ31GqaKJgrGDuXO9ueCQXzxbrs2ZJ94J6VXPhEhGzwk3E3aNZdozWTNkHOcDzVIOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخلیه کامل هواپیماهای نظامی آمریکا از پایگاه العدید قطر
🔹
تصاویر ماهواره‌ای و داده‌های منابع باز نشان می‌دهد آمریکا همه هواپیماهای نظامی خود را از پایگاه العدید خارج کرده؛ اقدامی که برخی آن را ناشی از نگرانی امنیتی و نشانه احتمال تشدید تنش‌ها در منطقه می‌دانند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/674838" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674837">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbd1f46a1.mp4?token=VKnRP4RBv94JhQc5e27MV9P-xTj-eu6ORB4rNZ66QZUXfsejxJiPIlU8URNXy_mj5iObXjjZweIUz_Fx3aZFbN1fPC-pFtBJaEII-a2X95AHcdoh_28xeZelUyxtR8w_0Ofoo2B4n7YFGVgMtNLN1YOGD7jGUUujsJtzb-wrIOmFLhdn5x72VCUhVDt73gauNy6LqFZWiaxFDscLdxhtkFSKgegLLg-hl-G4odTumo6vl68X1WJiVFChCJImmXgZ-0mtd8e9JoQxd-KJV0377bsUbYI55BzaKLv1MIAHNEBa5ImqUBUMXZl7ziQY91vjR2SsZgpod8dWEj3oUFGlNJ2j2fAeKXLI6FBMnj2okH465bSGcEWERJYQtG6AhepNabiqq3jUbm-abwz0IJtN5VuJQuol63z1CSWWgiuyBULuIhX9bMew8Lc5ZwN-vpCSaS65HLC35W4mG1Pq1AoCzFeFDhggUBKQ9o5MlGlBn3InE4R7XBagUaR1JiXW8BMi8gc_EYbjd_MI-dO81veVo7gUoPy3KLPGgZE_Qm93u8_3F4Pec_HgegAJOAUAiMgP_p7XNNSgwUA2eH5oHdIFbRyoBz_oIuvIxp6IZQS9M2FHz6pl0r03Q3PGu3HOD7wKIzj6yqlj_K9M0ir53I3xFhj2oCykkYlWditC9Ha92-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbd1f46a1.mp4?token=VKnRP4RBv94JhQc5e27MV9P-xTj-eu6ORB4rNZ66QZUXfsejxJiPIlU8URNXy_mj5iObXjjZweIUz_Fx3aZFbN1fPC-pFtBJaEII-a2X95AHcdoh_28xeZelUyxtR8w_0Ofoo2B4n7YFGVgMtNLN1YOGD7jGUUujsJtzb-wrIOmFLhdn5x72VCUhVDt73gauNy6LqFZWiaxFDscLdxhtkFSKgegLLg-hl-G4odTumo6vl68X1WJiVFChCJImmXgZ-0mtd8e9JoQxd-KJV0377bsUbYI55BzaKLv1MIAHNEBa5ImqUBUMXZl7ziQY91vjR2SsZgpod8dWEj3oUFGlNJ2j2fAeKXLI6FBMnj2okH465bSGcEWERJYQtG6AhepNabiqq3jUbm-abwz0IJtN5VuJQuol63z1CSWWgiuyBULuIhX9bMew8Lc5ZwN-vpCSaS65HLC35W4mG1Pq1AoCzFeFDhggUBKQ9o5MlGlBn3InE4R7XBagUaR1JiXW8BMi8gc_EYbjd_MI-dO81veVo7gUoPy3KLPGgZE_Qm93u8_3F4Pec_HgegAJOAUAiMgP_p7XNNSgwUA2eH5oHdIFbRyoBz_oIuvIxp6IZQS9M2FHz6pl0r03Q3PGu3HOD7wKIzj6yqlj_K9M0ir53I3xFhj2oCykkYlWditC9Ha92-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از آتش‌سوزی گسترده در اسپانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/674837" target="_blank">📅 16:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674836">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۱: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم عظیم الشان و فداکار ایران اسلامی؛ ایستادگی…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/674836" target="_blank">📅 16:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674835">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
محمد عبدالسلام: باب‌المندب بسته نشده است
🔹
رئیس هیئت مذاکره‌کننده یمن تأکید کرد برخلاف برخی ادعاها، تنگه باب‌المندب به‌طور کامل بسته نشده و اقدام نیروهای یمنی فقط به محاصره دریایی علیه عربستان محدود است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/674835" target="_blank">📅 16:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674834">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6KY7USezIoMqZCSFLHXgwSwdqQ5v18AuAIuraB8XiHMKDx4a-E5EWkuow_WzqvuBgq0e39JqEhIFUbjKwdNRhJNQ_MkVtaTCYoqM2C_N21-qBj3NAPS6ypN0oJXbBowdsIdR6w8Sf8_WFG5rpd2fdwQ_NXvx9MMWXBfQiGWqEyD6jjBolzF2KQJnVSWg97650e_f8LQR35vvEv_6VRAeRsa4TpHv5VFEGgVUbUpKp9fnSMcCdnfF9EKJxJ-1O3jtT026OdDhXHVqCgFDA23LbK77wCKkVBXZaFz-Sb1V3qnjWvb3xZCl3enUiof2OnEwQFiWe8BcDGRm-zf78RzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی عملیات وعده صادق ۳ در جنگ تحمیلی دوم: عملیات اخیر سپاه حذف اهداف راهبردی بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674834" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674833">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbaf83b8e.mp4?token=PxZGKYR8j5_bhEhftGi-CsC7oNyQ5aULCq7wl2WJ5PMxdgv3T8l0ZXIaCP1_nUB615q-s88hkOWbilFxCr2sNoVr_MwpQcRTv8eZfWHN_70jr8OOAmwfpDy7-7bWSTwyhEHzY5zFs0I4l5GEwAdj7lqbJ3J2KX44ZtVatrmVOwETwDgzjkIh1xVsHapbQwiVqA3Mx6sWMW7SpNHHluThnYZG-8OptCOzgwcYlDaZWqOAk1V78-p3yYqukxwOg05_lWa55MU4jxXgwNYUc5Z0-PI2wCCx_zXXzk1cFsFX7_qPhkUAU6oAPhT6_8L4QgkXQdU33T1aHYyoTgVkjcsglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbaf83b8e.mp4?token=PxZGKYR8j5_bhEhftGi-CsC7oNyQ5aULCq7wl2WJ5PMxdgv3T8l0ZXIaCP1_nUB615q-s88hkOWbilFxCr2sNoVr_MwpQcRTv8eZfWHN_70jr8OOAmwfpDy7-7bWSTwyhEHzY5zFs0I4l5GEwAdj7lqbJ3J2KX44ZtVatrmVOwETwDgzjkIh1xVsHapbQwiVqA3Mx6sWMW7SpNHHluThnYZG-8OptCOzgwcYlDaZWqOAk1V78-p3yYqukxwOg05_lWa55MU4jxXgwNYUc5Z0-PI2wCCx_zXXzk1cFsFX7_qPhkUAU6oAPhT6_8L4QgkXQdU33T1aHYyoTgVkjcsglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی تلخ داریوش فرضیایی با پیکر مادرش
💔
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/674833" target="_blank">📅 16:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674832">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
امید ملایی سردبیر ارشد خبرفوری: تضعیف رسانه‌های مؤثر، خواسته دشمنان ایران است. خبرفوری همواره خود را متعهد به قانون دانسته‌، اما انتظار داریم تمرکز اصلی بر مقابله با جریان‌هایی باشد که شبانه‌روز برای ناامید کردن مردم و تضعیف کشور تلاش می‌کنند. در جنگ رسانه‌ای،…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/674832" target="_blank">📅 15:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674831">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صدای انفجار در عربستان به گوش رسید
🔹
رسانه‌های عربی از حمله دو پهپاد به مخازن لجستیکی ارتش تروریستی آمریکا در صحرای عربستان خبر می‌دهند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/674831" target="_blank">📅 15:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674830">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310f040801.mp4?token=RmwVx81qFt2stioIQ-Xk35JBV28v-DlG0tqryvnwi_1vWLGaF-vU2wmGIV-c7xHKpn7gt8ULuhhDnhmvsPoxmq7EqEhN4VWvLyiwTw6-zc7yOsdO6iYRuUaExePhzJhXAPbwXJB2bXgjLpVxOLCVM7fx_SwZHgwyuTyaMiMjfR7zdDhG7JyzTX98LA0b3hrof3T1ZxgXyG_ySrMA5Sk1S0t1WJ4jXA2BkiMtiKv8akopnYQTYbwiEg5_GJDk0QVKsxvXuFO1CZBAKEdBiU-4E3JlsJTGOFTvgTPssrX8LaR5I9H4dB0NqkaHIuDbWIMLiA1Y4sXOg7GkoN0s0A5BoE7_kNtEhFH5WFVRU8evL6Umg2jDIdXPjsbEDJBut6Jl2l59zanp0YsXrvJOV5TAj73tQn9py5dUlLnZ2iAaiuLhj0Yk_YzZfQQnl_x8ABq0T-kDhhIcFY0d6PU-8kxFvems7UD0p_uGkAI8s9xj9XEAw94AmEXH44P6w3EirXjSUwxDXIrfd44pqdRnz-WO4eSaWvIR3-_SFEQqMixSAaEzFvFvo0KVuu7VGrOm_WOVPMffkHBlp0J-PNerINRBYBUck63A1J6tVr0I4wnae5l0_uYWJNzBHzpQL5D8Q9Bx_r9SFo_w77u1d41ho0KmKZem566_i1vp2Mrh6q8jS10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310f040801.mp4?token=RmwVx81qFt2stioIQ-Xk35JBV28v-DlG0tqryvnwi_1vWLGaF-vU2wmGIV-c7xHKpn7gt8ULuhhDnhmvsPoxmq7EqEhN4VWvLyiwTw6-zc7yOsdO6iYRuUaExePhzJhXAPbwXJB2bXgjLpVxOLCVM7fx_SwZHgwyuTyaMiMjfR7zdDhG7JyzTX98LA0b3hrof3T1ZxgXyG_ySrMA5Sk1S0t1WJ4jXA2BkiMtiKv8akopnYQTYbwiEg5_GJDk0QVKsxvXuFO1CZBAKEdBiU-4E3JlsJTGOFTvgTPssrX8LaR5I9H4dB0NqkaHIuDbWIMLiA1Y4sXOg7GkoN0s0A5BoE7_kNtEhFH5WFVRU8evL6Umg2jDIdXPjsbEDJBut6Jl2l59zanp0YsXrvJOV5TAj73tQn9py5dUlLnZ2iAaiuLhj0Yk_YzZfQQnl_x8ABq0T-kDhhIcFY0d6PU-8kxFvems7UD0p_uGkAI8s9xj9XEAw94AmEXH44P6w3EirXjSUwxDXIrfd44pqdRnz-WO4eSaWvIR3-_SFEQqMixSAaEzFvFvo0KVuu7VGrOm_WOVPMffkHBlp0J-PNerINRBYBUck63A1J6tVr0I4wnae5l0_uYWJNzBHzpQL5D8Q9Bx_r9SFo_w77u1d41ho0KmKZem566_i1vp2Mrh6q8jS10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۱: اقامتگاه نظامیان آمریکایی و چند جنگنده در اردن، سامانه پدافند هوایی پاتریوت، یک بالن جاسوسی و اقامتگاه تروریست‌های امریکایی در اربیل منهدم شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم عظیم الشان و فداکار ایران اسلامی؛ ایستادگی مثال‌زدنی شما هر روز حقیقت را در عالم پرفروغ‌تر و ظلم و استکبار را منزوی تر می‌کند. رزمندگان به پیروزی نهایی امیدوارتر و دشمنان بشریت را مایوس‌تر می‌نماید.
🔹
فرزندان غیرتمند شما در نیروی هوافضای سپاه در ادامه عملیات تنبیهی خود، در موج ۲۷ عملیات نصر۲ با رمز مبارک «یا اباصالح المهدی ادرکنی» با یک حمله کوبنده دیگر به پایگاه آمریکا در الازرق اردن، به چند جنگنده خسارات اساسی وارد آوردند و با در هم کوبیدن یک اقامتگاه نظامیان آمریکایی تعدادی از آنها را کشته و مجروح کردند.
🔹
رژیم آمریکای کودک‌کش، به ملت خود و دیگران در مورد تعداد کشته‌ها به وضوح دروغ می‌گوید، مراکز تحقیقاتی و رسانه‌ها را به تحقیق میدانی در این مورد دعوت می‌کنیم.
🔹
در عملیات غافلگیر کننده دیگر، رزمندگان اسلام یک سامانه پدافند هوایی پاتریوت و یک بالن جاسوسی رژیم کودک‌کش آمریکا در اربیل را منهدم و اقامتگاه تروریست‌های امریکایی را مورد هدف قرار دادند.
🔹
رژیم زورگو و غیرقانونی آمریکا در صورت ادامه شرارت با پاسخ های متفاوتی مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/674830" target="_blank">📅 15:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674829">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxG89tApktt5GWVCPsdhZkwMBecUICa3yOJZXccQtkzw_A7KJDUj3-lUzNWs3u_kKqvfCaiDb5m2hH6488IfHfHVBOtI1jSUPqaUQweIn7gFiL749pkKewZsjCGbwqmOGun6PJw0FNTRSzvlTTF-r2vU1WRJpp6X-A6MJ8kM4s9cjtiP05MjqVabD4be-Xv0IMBloMbZ5LD8EFw8pavFgPh87ewfKO9odf7sn3m5KqBX4iQqqm3r9yS1yyjmfKod975D8OM6srZmRKYg9dxEQR_Efb5FPdkhszoVa-XDd5VeOCetv_Nu8x3nU9EfdICowsntLfbneEjRKbW_Yy_mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت عجیب بازار استخدام سرایداران؛ اتباع افغان در اولویت استخدام مالکین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/674829" target="_blank">📅 15:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674828">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fddf870ff2.mp4?token=uF3PSSfQHBGao2pRZSwzbqX1Cd0CDNcE3klXx2tS5yF6mVfDUEWPxVCsSyXUunJXWUWYa-64qQBLs9BgupnbV9re33Rs2JoaH0a78OElrMwO8G0z7PlAOhemEEC4v4pISv8zzlCTDpTZgd2JtiC6N90YJmFDJWq2swKOIj-iy5XoaR_FkVyiRoJRya32eMG88-EXVA-VCrd_P-wCLtho6KXftRawVTuDAdWwNQarYFDYAMvkQXIrDLmhd53jVYW1y4Au9KarBU6Am8x5sT95rrdh-Fsvg5pr_3Ji8znzSc4BWeUJlB2bS3qTKjULFpGqTezmJYdqsNoDIO-CRGPtVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fddf870ff2.mp4?token=uF3PSSfQHBGao2pRZSwzbqX1Cd0CDNcE3klXx2tS5yF6mVfDUEWPxVCsSyXUunJXWUWYa-64qQBLs9BgupnbV9re33Rs2JoaH0a78OElrMwO8G0z7PlAOhemEEC4v4pISv8zzlCTDpTZgd2JtiC6N90YJmFDJWq2swKOIj-iy5XoaR_FkVyiRoJRya32eMG88-EXVA-VCrd_P-wCLtho6KXftRawVTuDAdWwNQarYFDYAMvkQXIrDLmhd53jVYW1y4Au9KarBU6Am8x5sT95rrdh-Fsvg5pr_3Ji8znzSc4BWeUJlB2bS3qTKjULFpGqTezmJYdqsNoDIO-CRGPtVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستگاه میخ کوب دستی مدل (دارای باکس)-BPZ ویژه
با دستگاه میخ‌کوب دستی BPZ، چالش‌های نصب را پشت سر بگذارید!
دیگر نیازی به ابزارهای سنگین و پرهزینه نیست. دستگاه میخ‌کوب دستی BPZ به شما امکان می‌دهد تا میخ‌ها را به سرعت و با دقت روی سخت‌ترین سطوح مانند بتن، سیمان و حتی فولاد بکوبید.
ویژگی‌های کلیدی:
فولاد مقاوم سری و پلاستیک نشکن دسته
عملکرد عالی با میخ‌های تا 5 سانتی‌متر
طراحی ارگونومیک و ضد ضربه
باکس حمل برای نظم و جابجایی آسان
هر بسته شامل 5 تا 10 عدد میخ است.
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/41267/180124/</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/674828" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674827">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تیزر قسمت یازدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید مجید غضنفری که در اثر تصادف شدید، ۲ ماه در کما به سر برده و با جدایی روح از جسم، مواردی از جمله حضور چهارده معصوم، عذاب چوپان دزد و حیله‌گر، فرزندان سقط شده‌اش که در عالم معنا زنده هستند و آبی که با نگاه سیراب می‌کند را در برزخ درک کرده و در نهایت با دستی که حضرت ابالفضل بر سرش نوازش می‌کند به دنیا بازمی‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید مجید غضنفری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/674827" target="_blank">📅 15:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674826">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حادثه دلخراش برای شرکت‌کننده مردان آهنین
🔹
در جریان رقابت‌های برنامه مردان آهنین یکی از شرکت‌کنندگان هنگام تلاش برای رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی که باعث شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/674826" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674825">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
صدای چند انفجار در جاسک حدود ساعت ۱۴:۳۰ شنیده شد/ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/674825" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
لحظهٔ عملیات استشهادی یک فلسطینی علیه صهیونیست‌ها که منجر به هلاکت یک صهیونیست و زخمی‌شدن ۳ صهیونیست شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/674824" target="_blank">📅 15:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ثبت تصویر پرتاب استارشیپ از خاک مکزیک
🔹
پرتاب دوم استارشیپ، بزرگ‌ترین موشک شرکت اسپیس‌ایکس (۱۲۱ متری) متعلق به ایلان ماسک، از زاویه دید ناظران در خاک مکزیک به ثبت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/674823" target="_blank">📅 15:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQE7WSNVu_gG189vF4M7Xz4YggmI7um1y-VrOluVjPC4EXc8R-BFBtz7X20ylCvRCDqHzUSqWxET43zGpQkXnlUNCkIKsXeMeEkoDzlXtz93msGSub_FV-25gFz8l8K4GNadew8tHDEjqZ3EixtscWavXXhkqJBimN_gO-IZ41gflijHnNXqy-VhHpreAxM6E_y7NGXbS7J8WkQtwDzZ6UV8u7ysVdiOHrye389fuS3vACm86BbWQexN-MexvHUfkXnfZYeBCK0xCVXjXC0zPubeDA52dsY5vB6M8W2oDmjhoZNShvaxBoGk4MzQQHKPOWQZ7ymGt48poghCYyjOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرگیجه آمریکا از دقت حملات ایران | ماجرای کمک روسیه به ایران در انهدام پایگاه‌های سیا چیست؟
🔹
به دنبال حملات پهپادی ایران به چند مرکز وابسته به سازمان سیا‌در منطقه، نهادهای اطلاعاتی ایالات متحده در حال بررسی این احتمال هستند که روسیه در این عملیات به تهران کمک کرده باشد؛ چه از طریق ارائه اطلاعات هدف‌گیری و چه با انتقال فناوری پیشرفته پهپادی.
جزئیات بیشتر را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3232561</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674822" target="_blank">📅 15:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIPq4hS7Yj1hKWgZgBCU5HrzwOmekYUboc8mrgyNthF2Tt6K5jMegatb50YGmETa5vZ-WJnmQkoijtxra6gqGE-IbDLL7_UNM7Cx-4ZmxEkQMNXVG3Y1tDICwxnsvKd-iVkHcgEJ8qZQVbtRLAP70P7qO8khIcio5dw3-NNtfr5qn-COtu2dtOIGHL-BvrjD9XKjBKenjJzu5zJ_ysosSA8uuKKB3iqZYuQjb0efx-VXh4dMStSKYhO5igCJp0X6xfE7kcDWhCoRIn38KUrr8bL2VW-dxw1f9Atn6tNpCJ_yGJtEBEqqBOatDjytiglTU0qQgp9snCBnFCGPp5Dz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونگر: مسی بهترین بازیکن تاریخ فوتبال است
🔹
آرسن ونگر، مدیر توسعه فوتبال فیفا، لیونل مسی را بهترین بازیکن تاریخ فوتبال دانست و گفت این موضوع «یک حقیقت» است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674821" target="_blank">📅 15:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7f6657a5.mp4?token=fEIqkbYcMb0g63DJ3AmQt6dtA3jUWhxDr6bBwRkE7AJelGxafWTfLdo9pCxUhNfZJvbHM7L8794GF1zsP6H190hZXCDBQ83jlIy39qfkGQFV-umx6Wb2jq96Rs_XhETLgQxgIlsT7nw8Ma7b3ofIFgvPjuVExSqmu-d0ewuDlXtwL20Jh-DHgRyV9ccVde56K89S31INEOTLcuaqipr5MK_7vC4GIbIuFuvSEJQZK2KIaHM8vmCSVxyRMf8pfh3VTBiUZxqkucCX7WnNL6XH_P_Ct-6ClzKlKp9qrvN6vQwztgM-p8XF0_c7RNB_ETt1DIcXQEmlwUq0c2Q6Z7qyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7f6657a5.mp4?token=fEIqkbYcMb0g63DJ3AmQt6dtA3jUWhxDr6bBwRkE7AJelGxafWTfLdo9pCxUhNfZJvbHM7L8794GF1zsP6H190hZXCDBQ83jlIy39qfkGQFV-umx6Wb2jq96Rs_XhETLgQxgIlsT7nw8Ma7b3ofIFgvPjuVExSqmu-d0ewuDlXtwL20Jh-DHgRyV9ccVde56K89S31INEOTLcuaqipr5MK_7vC4GIbIuFuvSEJQZK2KIaHM8vmCSVxyRMf8pfh3VTBiUZxqkucCX7WnNL6XH_P_Ct-6ClzKlKp9qrvN6vQwztgM-p8XF0_c7RNB_ETt1DIcXQEmlwUq0c2Q6Z7qyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین تصویر از ماکان نصیری و هم‌کلاسی‌هایش در دبستان شجره طیبه میناب
💔
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674820" target="_blank">📅 15:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d007100491.mp4?token=O73s9ZhO5apm4pGFU6tGA84gb1zX_Q0DcanIxuScAB7q_YV8UP-aKp7230ITcfvGpgqKpukmAR8qygPUknAdQ7JiFHA84A0bfNBYHz14JNCsSZm5gsSfIj_sNxDPRM8x0Cph2QVkSEC80t6xhsMnjPdjs7ZEEqNnoeEb8HpIuGA8QLjWM7Cy-wnfsQigZNQIDzFX1Xqukg4czLtYOEjI0Jf3n9YvxUwwle2qbNLvLtgAl_iaewdKzouOglzGm6PTID13uzBqqj_Rm2GAdHDRd-hN5-gMvJmEiZMyssQPnNSYKACx3pXYbVOu6ybGPpDPUly0ARE9_0VOTFL2iGkOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d007100491.mp4?token=O73s9ZhO5apm4pGFU6tGA84gb1zX_Q0DcanIxuScAB7q_YV8UP-aKp7230ITcfvGpgqKpukmAR8qygPUknAdQ7JiFHA84A0bfNBYHz14JNCsSZm5gsSfIj_sNxDPRM8x0Cph2QVkSEC80t6xhsMnjPdjs7ZEEqNnoeEb8HpIuGA8QLjWM7Cy-wnfsQigZNQIDzFX1Xqukg4czLtYOEjI0Jf3n9YvxUwwle2qbNLvLtgAl_iaewdKzouOglzGm6PTID13uzBqqj_Rm2GAdHDRd-hN5-gMvJmEiZMyssQPnNSYKACx3pXYbVOu6ybGPpDPUly0ARE9_0VOTFL2iGkOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تقدیر سهامداران از تایید وصول مطالبات ۵۲ میلیون دلاری شرکت نفت سپاهان»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674819" target="_blank">📅 15:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674818">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۰: سه سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت شجاع و وفادار ایران اسلامی، عظمت شما رعب و وحشت را بر پایگاه دشمنان مستولی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/674818" target="_blank">📅 14:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674817">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3kBw7dhGlHnaCUn040T4rONG9S5zrMtnUzpJOVjYU6CVByxjNTGr63nT1bJYFqhfyNkoLU7ZCgY6S1deJIZQwHKFM-gtN1t3OKx5pq46XDdLexD8LrJidRVwXJBkadFFUR_f_yC1S2bRwB5lEFGgR4u1NPYMcea35M53RmzAv6pZEJOwUWpG9KZ9EnxPojUciHARpBi-P1S6Yr9RwqRk8Wf_nlliTldOuEpgKy0fhm8h_TlNTPgjwcWwDpDTvg3FrKjtpBeFMoDTyrwhwxXk7BFg2_CbPFBb2Emfg_BcK9lMaQbIR_qwKtzQKDI1-GiQggNNEQL77kYbZjMPF9qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار نوسان قیمت نفت برنت در ساعات اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674817" target="_blank">📅 14:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رویترز: داده‌ها نشان می‌دهد که طی سه روز گذشته، تعداد کشتی‌های عبوری از تنگه هرمز به‌طور ثابت روزانه ۳ فروند بوده است
🔹
دفتر نخست‌وزیر عراق گزارش‌های رسانه‌ای درباره میانجی‌گری میان آمریکا و ایران را تکذیب کرد
🔹
تردد خودروهای سنگین در جاده ایلام–مهران از ۱۱ تا ۱۶ مرداد برای مدیریت ترافیک اربعین ممنوع است.
🔹
بیش از ۸٠ هزار نفر در ۲۴ ساعت گذشته از مرز مهران عبور کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674816" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va7EMysbLkQ2kcuRh1WV3oZHrQ3lwwXhtk9UjDbc-eLY3aYtJAC6jQ6wNyyD8rDZFCA-gFP4ynfyx9LWgYUV-zPrZ2W48wKz4CytzuyssUcYqm8PLMq45sqLbeWPJnbUAxUtNlc9xSwZKwViXgJS0iOhtgFPvUq1ZvyzUa8tJ7XBtrO-OUwwsDtQ5SSkrG_nJQD49YSiIaKvqh_2BjSjj8oeBNdeih4Sc5QuvyF-64AjuLScnojxVlXtR3ItTSI_uzco_bbu_EezNCsP9ULd3MA77TMi7Mby-JxE2A09pK-qU1gcAp1xxXeYnLEWqRqwi8LfEuA6s1kbbf-zpa-Vmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه امتحانات نهایی پایه یازدهم برای استانهای جنوبی اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674814" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b9301063.mp4?token=iTnOFIqkjPIvDtEvqTGSSynGqiiutY21mhiHYSG20Bq-V9CZhmw-ogWY-U2wyCX8z58i3-Tr9adQ_TkZOVT5lqAyzhiVymymNPuSlObiOGkoQ7JfRLjP6cXJe2Olpp42jfbVcXyASCIxNj6deZCVZxliy0RMRcm8_Ze_mG7p6sj2PMzd6DZ5Nz1d3evl6Dous7Iq8w5P0aifZveJkPU_v-jenFmjHzA59teCF2uBW62CS-R1bjFvwSLZRCJHZ-zV7rOKfWm813me6hF8qVwDzaismAyt0TKMwmBkLN03_Ya3SEVr9u3dEdR1lH1xXJLLaPm_qzeaNA-JrBG2aQQNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b9301063.mp4?token=iTnOFIqkjPIvDtEvqTGSSynGqiiutY21mhiHYSG20Bq-V9CZhmw-ogWY-U2wyCX8z58i3-Tr9adQ_TkZOVT5lqAyzhiVymymNPuSlObiOGkoQ7JfRLjP6cXJe2Olpp42jfbVcXyASCIxNj6deZCVZxliy0RMRcm8_Ze_mG7p6sj2PMzd6DZ5Nz1d3evl6Dous7Iq8w5P0aifZveJkPU_v-jenFmjHzA59teCF2uBW62CS-R1bjFvwSLZRCJHZ-zV7rOKfWm813me6hF8qVwDzaismAyt0TKMwmBkLN03_Ya3SEVr9u3dEdR1lH1xXJLLaPm_qzeaNA-JrBG2aQQNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی کودک ایرانی برای سگ زرد در مسیر پیاده روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674813" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجواد موگویی|حرف بی‌حساب</strong></div>
<div class="tg-text">ماجرای جنگ۲
به‌روایت جواد موگویی
روایت بیستم:
گفت‌وگو با سیدعباس عراقچی (بخش دوم)
فیلم کامل
🌐
@majaraa_media</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/674812" target="_blank">📅 14:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f39ca15b.mp4?token=i_uSjGSIi6QKWJ0o5skdMjU-JAkt1FBEO51tuXaW_yZLjojMBg7GuLhOzpxHyNcjly8rknhPBYV9OFHHvxPbmftgkTlaFxgwFBfMV69FTo_eKIULOWg-DBUQfhYjhz3IsbVMPvLT2Or8XHpEJrqH0dQuHhX85-AUW_XspRPMfco20OfZkEa_8fVZqgBEfyopfwiB6LjVjdQcrs8n-4kKLZIeAGqw4eBGKalo1q-yjgkdLxpPSRtMXHT6muHHVK6BLm1823WH7vxnxZu876DMQBMkBDpHgCmX3Qb-esfnK14RkRA0-Q-ZyYMqrr7NH3NJKWKMh6bSmFkztJKHXYIaqkosKezwpxyAGQ4eGAwBK-n11ATcZVKw1nt4Qjk0sR2mnbVFVibbjL7LKfimOb4buo4JDNP6Fp8NKtUDC9zO98BKdFSxDbfW-t3Dgffs8B5SpENN0GTQcup6knSfWa3LnfglFQYWSDqFT2_UOPcb2T6GrC7sQwtm4b5hCoNaXrc6nFeNnsGYFDBviPZHsJI3Iy6v5hthm767rH7JPWTQS-LSH1Ix7Z71D9t3YcUGsgA31TI4anYkgpBN0OX6fJaVYvtaVXg62DrINCiONCpkRHNENO6Wj8sVjfaQSJHQrZizC6UC-4as8kImZyc3S1Gsj7x3RsLU9TXn02oIjSFNjN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f39ca15b.mp4?token=i_uSjGSIi6QKWJ0o5skdMjU-JAkt1FBEO51tuXaW_yZLjojMBg7GuLhOzpxHyNcjly8rknhPBYV9OFHHvxPbmftgkTlaFxgwFBfMV69FTo_eKIULOWg-DBUQfhYjhz3IsbVMPvLT2Or8XHpEJrqH0dQuHhX85-AUW_XspRPMfco20OfZkEa_8fVZqgBEfyopfwiB6LjVjdQcrs8n-4kKLZIeAGqw4eBGKalo1q-yjgkdLxpPSRtMXHT6muHHVK6BLm1823WH7vxnxZu876DMQBMkBDpHgCmX3Qb-esfnK14RkRA0-Q-ZyYMqrr7NH3NJKWKMh6bSmFkztJKHXYIaqkosKezwpxyAGQ4eGAwBK-n11ATcZVKw1nt4Qjk0sR2mnbVFVibbjL7LKfimOb4buo4JDNP6Fp8NKtUDC9zO98BKdFSxDbfW-t3Dgffs8B5SpENN0GTQcup6knSfWa3LnfglFQYWSDqFT2_UOPcb2T6GrC7sQwtm4b5hCoNaXrc6nFeNnsGYFDBviPZHsJI3Iy6v5hthm767rH7JPWTQS-LSH1Ix7Z71D9t3YcUGsgA31TI4anYkgpBN0OX6fJaVYvtaVXg62DrINCiONCpkRHNENO6Wj8sVjfaQSJHQrZizC6UC-4as8kImZyc3S1Gsj7x3RsLU9TXn02oIjSFNjN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاور پنتاگون: اگر ایران بر تنگه هرمز مسلط شود به عنوان چهارمین قدرت جهانی ظهور خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/674810" target="_blank">📅 14:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c3869f9.mp4?token=rkC2L32irVW_OE8oeym169Ird8aYj5yK9snOXe4AhCz4RWk2EE4wb4l8U46-nQ7-m71GciHjp-i_WWC3xNsuezEowRC_w31m60JiAzQ9TI9o-Czd86X0k8s1Yv64v6wv3eKlPonklyLB4eQ58Yle7GJYjnV9dRdWJO8vVm-SzTJ00V_fyZaDb9zjFMJDsMKfVZor98bS0u9N2iYreN8euRkSA2rzhrLZR3dXiLY7mNwrPL7a8LoihihDmb2Ha2tdyzEifutsknTjQ2MP8iI0HGN9MgUQEtDwl_nnDivdkyjf2ozvdj0toSrKLdfTmDa08UZ_OaghgME57ZNudVo6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c3869f9.mp4?token=rkC2L32irVW_OE8oeym169Ird8aYj5yK9snOXe4AhCz4RWk2EE4wb4l8U46-nQ7-m71GciHjp-i_WWC3xNsuezEowRC_w31m60JiAzQ9TI9o-Czd86X0k8s1Yv64v6wv3eKlPonklyLB4eQ58Yle7GJYjnV9dRdWJO8vVm-SzTJ00V_fyZaDb9zjFMJDsMKfVZor98bS0u9N2iYreN8euRkSA2rzhrLZR3dXiLY7mNwrPL7a8LoihihDmb2Ha2tdyzEifutsknTjQ2MP8iI0HGN9MgUQEtDwl_nnDivdkyjf2ozvdj0toSrKLdfTmDa08UZ_OaghgME57ZNudVo6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر شهید سلیمانی و شخصیت‌های سیاسی ایران روی دیوار هتلی در تانزانیا</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/674808" target="_blank">📅 14:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58e93fb93.mp4?token=nU9W9q_M7RJN8vo8iHs6yzYHDZJSlpcNW79HfFk2lOqQa0qPRCZN1MgXlvVVOci1UA-oPVOKg9ndIlncpQK0QikO3WFty_oBzeMqGvwwXK784KHvrPg-xTPXywTrl0FxSJXqR42k1A998yRbaxJ9oEbnN6AhZSGvIb8cTchhE-1ZJi52bP2l-n-ucOOGd9jzHa_GMlFY8u1YlBMH0CqxNT1Dg81V0gKQI6-OqJF6xsnyg11AOFQetS9K-UrmwnKEC1KIB3cG-zheuo3IfSHzMsUIR_KKc3oiP1h7u1HIfpYHn0x5XJTQ7crhnjn4FqHY8GkfcuH3KGMR0USTfVkQDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58e93fb93.mp4?token=nU9W9q_M7RJN8vo8iHs6yzYHDZJSlpcNW79HfFk2lOqQa0qPRCZN1MgXlvVVOci1UA-oPVOKg9ndIlncpQK0QikO3WFty_oBzeMqGvwwXK784KHvrPg-xTPXywTrl0FxSJXqR42k1A998yRbaxJ9oEbnN6AhZSGvIb8cTchhE-1ZJi52bP2l-n-ucOOGd9jzHa_GMlFY8u1YlBMH0CqxNT1Dg81V0gKQI6-OqJF6xsnyg11AOFQetS9K-UrmwnKEC1KIB3cG-zheuo3IfSHzMsUIR_KKc3oiP1h7u1HIfpYHn0x5XJTQ7crhnjn4FqHY8GkfcuH3KGMR0USTfVkQDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلینکن، وزیرخارجه سابق آمریکا: ترامپ نمی‌تواند از گرداب ایران خارج شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/674807" target="_blank">📅 14:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8365e938.mp4?token=p1Tgu4eurLv-YMF6pPP10xlcNqUzor7-nIHQd2uLiGfHm-25trXnVdlZxsuXetMyHoxr5JNIk8Kg4ff5b8foiUL5Y5KWovRrHaTT6i6GMYyPHBmq9UHOLhTLgWctvXOFHZVA9H2wl0SoV9_ZtDJjl9m4KhmesAJ6gUqtjO2xmlWCEYTYQo1fzbcRemmUtOlfgdOR_jYLfCFxqmLbEiLvjRJ1pNVw8F8ljZkDOwug2op0Ea7cDsnnT-mQx81rf8gdJxl2GOy5lSahIyXZ07Z28koZDuVEoUW7K0YR8YzA6xYxcf-JJFWPOZnKg5lB9GcEsTjRqaAPDeb7qBT1NjRI8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8365e938.mp4?token=p1Tgu4eurLv-YMF6pPP10xlcNqUzor7-nIHQd2uLiGfHm-25trXnVdlZxsuXetMyHoxr5JNIk8Kg4ff5b8foiUL5Y5KWovRrHaTT6i6GMYyPHBmq9UHOLhTLgWctvXOFHZVA9H2wl0SoV9_ZtDJjl9m4KhmesAJ6gUqtjO2xmlWCEYTYQo1fzbcRemmUtOlfgdOR_jYLfCFxqmLbEiLvjRJ1pNVw8F8ljZkDOwug2op0Ea7cDsnnT-mQx81rf8gdJxl2GOy5lSahIyXZ07Z28koZDuVEoUW7K0YR8YzA6xYxcf-JJFWPOZnKg5lB9GcEsTjRqaAPDeb7qBT1NjRI8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان میدهیم اما سر تسلیم پایین نمی‌آوریم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/674806" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۰: سه سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت شجاع و وفادار ایران اسلامی، عظمت شما رعب و وحشت را بر پایگاه دشمنان مستولی کرده است و اخلاص شما شوق جهاد را در رزمندگان مضاعف نموده و فرزندان شما در سپاه و بسیج ذوالفقار برنده خود را پی در پی بر دشمنان فرود می‌آورند و آنها را در هم می‌کوبند.
🔹
در موج ۲۷ عملیات نصر ۲ با رمز مبارک «یا اباصالح المهدی ادرکنی» رزمندگان با هدف قرار دادن سه سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی واقع در العدیری کویت، این سوله‌ها را به آتش کشیده و از بین بردند.
🔹
رزمندگان همچنین به طور همزمان برج مراقبت ناوگان پنجم دریایی آمریکا را در بحرین هدف قرار داده و خسارات زیادی به آن وارد نمودند.
🔹
عملیات تنبیهی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/674805" target="_blank">📅 13:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQN61hsxA7jopjQuz-O7PePuDu4oaS14OE1BBG9olfy1qF1IkZmwvUp6LKjor4TJwgl39UYC5zwjvUSc78diHWfo1M8C8l4B0W7Aiu-xUzdgq8w7cIOpEdDlOvHyq_mumzIq5L3yNAaTi-NRNVZzZixFpbLMTBVFJm999HCRvaXOVvegEu_Ps7Xayhuw2-J8RzTVEwowjVPz5njrNXIsDk-SBpHPJTnndtLdHVqrxwl9QK1MP4Q-FJpAe7FjJ4WX4TTCNXyglVOGBnaREnmADs-9jMEADcVgnAMgB3Q3TErDQtTTDCIn-7tO9mdDmFB2RzxYK1L1FpaPVuZxfqPrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهران ممدانی شهردار نیویورک: در صورت حضور نتانیاهو در نیویورک، بازداشت خواهد شد
🔹
در صورت حضور نتانیاهو در نیویورک (برای شرکت در نشست سالانه مجمع عمومی ملل متحد) صد در صد او را بازداشت و برای محاکمه تحویل دیوان کیفری بین المللی خواهم داد.
🔹
او به اتهام ارتکاب…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/674804" target="_blank">📅 13:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674802">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمداحی نور</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">{webahang.ir} Emam Reza Jan</div>
  <div class="tg-doc-extra">[WebAhang.ir] Amir Kermanshahi</div>
</div>
<a href="https://t.me/akhbarefori/674802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/674802" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674801">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf03fc9e60.mp4?token=CG3CNiUr69eb_vjWO-KkopztkSHyaCAAlcfAt5FBc7p2bz0mgAH2YxxJNYFU-0mecWA7qAK60SqS6Az3dmUm1jtSHSSyI5irtSv63hPbIUQJmENdXtcVdb9ucht9ATDRMxIpMFLkeN2AHv0m8j1PC79HOM_1Kuofah_xcmSUMYM4kFvIBQn9FiaouXTCZ-nW0-q_u2qY1xdXIagSwPTh2OeuUp_dfGcO_Zb9kbsqQUBTGE1hZXK5Quh0WsI_30LgfaWsku95GUVK4Xjp16RUv6mO3fysx3qMwoNGQMyGhlz8uBuv6l3GsDIi561wSwOByUEAzpeJsK8h52lP3bXQgFb9DSQ_sxgED8bOw4dZyASOkSGSm1H0AcqZDvfZSZvYkzal4-Bpc7E8ws5fF19_Ox0lYamSuU0lJD-2NllBHM-3lT0XvnMwuUjvV-1EcdeLRNQqw4nQ74HopSaj061WDF3tWcysXKSX_0DQeRa6VNTm8CFJ15sJGQ-Lx23FZ_SDSrptTQHTwDW9Ysh9rpkKa5opwm5e-rPF1BVS8jWMJYvLSUJFPSGhBIfgZz606e3Pvt9LiTMlf8c21VKj6WZtWuzr5ps8PJ-zep_P3c4OEMv_70K_FOgaxT0YNqdQ_zb46mVXdwoXJJRr6NeFx_zQ4xmEATnDXFOC3Ln7EM6kkfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf03fc9e60.mp4?token=CG3CNiUr69eb_vjWO-KkopztkSHyaCAAlcfAt5FBc7p2bz0mgAH2YxxJNYFU-0mecWA7qAK60SqS6Az3dmUm1jtSHSSyI5irtSv63hPbIUQJmENdXtcVdb9ucht9ATDRMxIpMFLkeN2AHv0m8j1PC79HOM_1Kuofah_xcmSUMYM4kFvIBQn9FiaouXTCZ-nW0-q_u2qY1xdXIagSwPTh2OeuUp_dfGcO_Zb9kbsqQUBTGE1hZXK5Quh0WsI_30LgfaWsku95GUVK4Xjp16RUv6mO3fysx3qMwoNGQMyGhlz8uBuv6l3GsDIi561wSwOByUEAzpeJsK8h52lP3bXQgFb9DSQ_sxgED8bOw4dZyASOkSGSm1H0AcqZDvfZSZvYkzal4-Bpc7E8ws5fF19_Ox0lYamSuU0lJD-2NllBHM-3lT0XvnMwuUjvV-1EcdeLRNQqw4nQ74HopSaj061WDF3tWcysXKSX_0DQeRa6VNTm8CFJ15sJGQ-Lx23FZ_SDSrptTQHTwDW9Ysh9rpkKa5opwm5e-rPF1BVS8jWMJYvLSUJFPSGhBIfgZz606e3Pvt9LiTMlf8c21VKj6WZtWuzr5ps8PJ-zep_P3c4OEMv_70K_FOgaxT0YNqdQ_zb46mVXdwoXJJRr6NeFx_zQ4xmEATnDXFOC3Ln7EM6kkfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد و قبل؛ تصاویر پربازدید از تغییر عجیب چهره‌هایی که دیگر قابل تشخیص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/674801" target="_blank">📅 13:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFaXK_zIL16XXnjyUQtKOThhklUIbTJQtI3G-krsVnF2hpXTjXwcGZjj-Aj59ovYBdbnJZtUos4-yI4L5kFGjzJ5gJ7J4mTYRiBF01FrDexXOXHdy0F8lbU9IWXZeD6XQ-DpKxPp3MDp8_J9q5W-yUECNnVVu5-AMWe0-W9NP6kwVw9BV7W3qZkM8WQi8HPUZhNLJIEsFDIkeBuQRT43kHK_B0_6AJ3hpKbWT6BhWU3Y7cA86XHXYsDzrff-jVbXDHMfnxNpT2JgDlwvnlE8k9fAasGQIQhAL2mKBQFRiIjAZnQoU2yFTiuVQs1ELz3G8DHLxrG-I3zD4XDeu4Nb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تناقض در گفتار؛ آماری از ادعاهای مکرر سگ‌زرد علیه ایران
ترامپ تاکنون :
۱۰۶ بار: «ما ایران را شکست داده‌ایم.»
۹۵ بار: «ما ایران را نابود کرده‌ایم.»
۸۸ بار: «توافق با ایران قریب‌الوقوع است.»
۷۵ بار: «تنگه هرمز باز است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/674800" target="_blank">📅 13:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674799">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b07f492a7.mp4?token=MmshLRM39QDv99KFkGOWl_IOuPqdCOH6KXwu7A-mk5iBxHivPFcKl-7C-OBO0EWJm5RPzNyjj9W5VK5e6Wjz_nPxaSt0R9ciHlN7_z6lK2ffBPYYgaYeKTCRsG3d0WmP4y0x3jTfNG00g4tze7VMBZ4oUnmTMwcFjKLDK7IA9eWgYG0xwZM3cpyUHNM1OIbOudsBKvCjLeje85qyFmCKoaGtMDxt0NixGMkPnzg-o2DboOIC8TvFu5tbxY0r1CgbTAqIuRLACaIOCISpmmKnOFdLrR4bb7cgpXlCTAZyKB6WhfP50bLa0N-rBwyh5XvAQiipRS6VRJXhuFZ2Hxp6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b07f492a7.mp4?token=MmshLRM39QDv99KFkGOWl_IOuPqdCOH6KXwu7A-mk5iBxHivPFcKl-7C-OBO0EWJm5RPzNyjj9W5VK5e6Wjz_nPxaSt0R9ciHlN7_z6lK2ffBPYYgaYeKTCRsG3d0WmP4y0x3jTfNG00g4tze7VMBZ4oUnmTMwcFjKLDK7IA9eWgYG0xwZM3cpyUHNM1OIbOudsBKvCjLeje85qyFmCKoaGtMDxt0NixGMkPnzg-o2DboOIC8TvFu5tbxY0r1CgbTAqIuRLACaIOCISpmmKnOFdLrR4bb7cgpXlCTAZyKB6WhfP50bLa0N-rBwyh5XvAQiipRS6VRJXhuFZ2Hxp6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ عملیات استشهادی یک فلسطینی علیه صهیونیست‌ها که منجر به هلاکت یک صهیونیست و زخمی‌شدن ۳ صهیونیست شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/674799" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3OOXHTcWUx3zeguQrMtv62VHP8uI2CeJJuAJZHfSa39HH3aT-oMV3ufJOP2QtEBSTeyKyTEfwctB1b2njdFs8uewl9VA9Hc8PHnCXXbsxSwWsG1tqF1txLjnaKjJyOYymU1d8cyem_u5NYZHBxIzb6NUFEZ6WQ41L7aj2gtmm3iHf3oUjpwTJ8JoQKoPZpEHoXuUdOqaorKuzJodtbp7MibTOj9mA2VeXmSj_-AnvUyywMlZU3dg1YOqQg3kETydQfTRzVUVUQfTdPQmLjjtIqmmpryghdO2-VK9oMUWz7iSvB9Lc9x0lA-kcWS3WLqO-rpWOAou1Wf3VpZdGtJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIUhDDYiV1zAMtReniaoobb7eEMt2SjhLy5pOd5HG3hAu5sYDlfG9LDMz4qPw7vq6DFdSQFJTSAqDs_FCwziV_g4iaw2XF2WTGuKAau0dqnvHUEM-nGd0dO5fBnXHdaGK9gM1VoCGQ9IbImIyRP7Z3eSJXSeYEhKjaAqbIzTyWLzha8vmHL78wYqcR7mK5TEsM60pOcinGckhx4iLmkDOT8PjMtDBlvAyN0cenWf1u50vJwVBUlPNOGe09GeZXck6p3X6bAOfuiuS8MWdzhKicHH_b2AbLsDXrdCRWgfXQG58v-ZrzcXQsf-x23JqI-1Xgj11-E-xK4TNvmo9R5TiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استایل جدید صابر ابر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/674797" target="_blank">📅 13:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674796">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEELKZCPdg45mhaBSsIiiCQSJ4kYKp-uK0E3bCkWWNt8Uxczj2-ZtcnsVjOJohfH2VyZpcFlauDJXrV8LNG0pbJm8P7oRBRpbyTbrZgkJMKduJdN34CuVOzCcr9hCFbjD10BLD96xFtxYcSVrFQADT8aRTmvBXyNoX-durX_yMf9OsFNMfQs6hCryP848CTRXJhYsltubc721mV3MyyfH7fY3tuD5x-PvH27rRFVotfl0sSXMvu8ym1QQ__rP9KJpYDzBpU6HtsODr27IqDwOM46U1ny2CHvnp1V7cd2-Bnvh3eoiFPNVIhV88-Qe3mJ4Z0FWJgUbjF-Yfnwp-lBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کاربر عرب زبان: ایرانی‌ها خوب بلدند پیام‌های سیاسی و نمادین را هوشمندانه منتقل کنند
🔹
وقتی ترامپ شهید سلیمانی و شهید ابومهدی را «دو مرد شرور» توصیف کرد و گفت: «من آنها را از بین بردم»، انتظار می‌رفت نخست‌وزیر عراق از حاکمیت کشورش و عزت یکی از رهبران نظامی آن که در خاک عراق ترور شد، دفاع کند. اما پاسخ او این بود: من درگیر سیاست نبودم و از گذشته به اندازه کافی رنج برده‌ایم.
🔹
در مقابل، پیام ایران به شکل دیگری رسید. آنها او را به یادبودی بردند که در آن تصویری از رهبر شهید به نمایش گذاشته شده بود و کنار آن تصویری از شهید سلیمانی در سمت راست و ابومهدی در سمت چپ او قرار داشت؛ صحنه‌ای که به وضوح نمادی از جایگاه این دو مرد در حافظه جمعی ایرانیان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/674796" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674795">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سپاه: با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرید
روابط عمومی سپاه:
🔹
مردم شریف کشورهای محل استقرار پایگاه‌های آمریکایی در منطقه؛ رژیم کودک‌کش آمریکا پنج ماه پیش بدون دلیل منطقی و توجیه قانونی با به شهادت رساندن برجسته‌ترین دانشمند دینی و رهبر سیاسی جهان و همزمان به شهادت رساندن ۱۶۸ کودک دانش آموز معصوم، جنگ تجاوزکارانه‌ای را علیه ما آغاز کرد.
🔹
ایران بعد از ۴۰ روز جنگ پیروزمندانه در حالی که می‌توانست جنگ را با قدرت ادامه دهد، برای بازگشت آرامش به منطقه حاضر شد با نهایت گذشت با چنین جنایتکارانی پشت میز مذاکره بنشیند و تفاهم‌نامه پایان جنگ را امضا کند.
🔹
اما ذات جنایتکار و درنده خویی ایالات متحده موجب شد از همان روزهای اول تفاهم، آمریکا درگیری‌ها را از سر گیرد و تعهدات را زیر پا بگذارد و نهایتاً از ۲۱ تیر ماه رسماً تفاهم را ملغی و جنگ را از سر گیرد.
🔹
با گذشت ۱۳ روز از ازسرگیری جنگ، آثار شکست مجدد آمریکا ظاهر شد و دشمن فهمید با عملیات جنگی نمی‌تواند بر نیروی مسلح ما غلبه کند. اما برای خروج از بن‌بست به جای عقب نشینی به ارتکاب جنایت جنگی متوسل شد و پل‌ها، اسکله‌های صیادی، قایق‌ها و لنج‌های مردم، خودروهای عبوری و راه آهن را هدف قرارداد و غیرنظامیان را به شهادت رساند تا جایی که در روز گذشته با کشته و مجروح کردن زائران اربعین حسینی در مرز عراق جنایت را به اوج رساند و ماهیت یزیدی خود را آشکارتر کرد.
🔹
از آنجا که در صورت استمرار چنین جنایاتی دستور کار ما قصاص جنایتکاران خواهد بود، بسیاری از افسران و نظامیان ارتش متجاوز آمریکا از ترس آتش رزمندگان اسلام پایگاه‌های خود را ترک کرده و ساختمان‌هایی در شهرها را محل هدایت جنایات خود قرار دادند، به عموم مردم کشورهایی که محل استقرار نظامیان آمریکایی هستند، هشدار می‌دهیم با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرند تا در امان باشند.
🔹
مردم همچنین می‌توانند محل‌های جدید جابجایی نظامیان اشغالگر آمریکایی را به حساب رسمی روابط عمومی سپاه پاسداران انقلاب اسلامی در تلگرام به نشانی
@sepahnewsiradmin
و یا بخش "تماس با ما" در پایگاه اطلاع رسانی
sepahnews.ir
اطلاع دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/674795" target="_blank">📅 13:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674788">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJOtOBTP83Jn5Dn-oHfovF4EPmaaJMqmf35HBIMPgVSJPDFKrtWJ_-imF9PHxUEYXIHcB2UsobRt3c3-Y1bUtbQiWv6tHV-xPQLrJu3SM0gjA-UuP6YOUZmRR6h4_9IoYwKYtut70dNp0W6N0AD9YOAb7cdDBYydLsBfhzhD0gysWljTDqNgmmY4gWqXjT02L4VTPNiRtl1TfuufojHima0425NN1F5_KCZl3IyZl7RN6Pi84AM4Wi6jxjRkm8TxnwqoePMoBnp6Y_D-bv3ch39TDipG7aNy2naV4aAtLQBcnPwow7GKYwZ5bvojMJFPT4dDVGDQhZCRg15h-lNGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXp7limxTeX2nKEqv9Wcvj1VaDmIlGaVjVrqktBMbeaLl62f5kJlp75xW6N7W3oPlr5zj5g0U0VJQBZuBSD-Yyu68I95XkoqW5Qx--Kz7_RW3b86Egz53J_mNPhEQFyw1MBCs5pkH4YxoWqoWeRnz1eUj3cW3wUhejejTZ6v5LO8dHA-8nx0fv1WfSuPbjjRBxi1uqu4NC2j2RXmfIVxYEEf9S1hkMZ2rFQnvLmmBuBDRX0m3IfAUplVm03RqMVnfnTgb-bfTnQh5LB-45P1W9tjW-kYtR5RKDvITxIqZZWZMSGKFx51a_8blno7Ic7DC02fFP0e3pwUnpRWy1f7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM0uFYmjoYqwG_5H75uVn-j0kI0wW2TKJ_-wiHmJGWNv8veEcjMSrd0qjCADTkwoZOC2PMzTcsXqmq9NG1AJegPZfBS0JHcpAEIL_7GUApajHBEl0mZepfYZ7SeYQqPY7S7mSnoaO7T-NfWwZkVPWeGw0uD5msSrerL9xyWepX5XhzJykTTOzj-Ctg0vRBtfQGum5hNHTyna9kvQWALzcwBe0-ie10m3ZaWIGkibnkNP6_CEdG9IWgApW5rQ74pEq1e0eF8RFm-tum5yFgrah7PfMeli1deDlswEz6bUvx7pSrIeMl2eSgsSgWM904vCLQYsDARuNJnst7uxcLnttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKm07WcMGgAwX01yGuLu80aKylAgag9Ck5bZhQr2HUMzBrxQM4NLo0r1fMq-0l5h3z4Jc_JdHb71LQbIz0drMpvyPZyNb9jw7ICOkNSdSLVgqQMsL2J5_zvgtfjlDRws3DeG0PR6Rgpuox68LVkE_tUitYaUO9_rc7hwLI_ELz4vjoG4rx9x83w3Gbgtl1VYu9wSrzY_mJhXT8bRsWMKdhEAIhzaJzjEbV_KQzROaemdIo0pnIOP0VU_holWLX77v-1PuY9RUfG8MaFaRniK0j8YoOSvOdkrNMQtnqhuiYeuu7c1FCSpthQe2UnkjmnJ6xxbOrGgQuwhh67B_VqHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh8Ik7N528J1zlEE_c5Rdn_7X4lAWTOd5LOOlr0c8ipilS7ncdqJR1qhLYtmaB9EwVLQntSCs3EUli4oLAIrDGD2Jg_fw99nl0eHJFHaUQOzYddT6h8HejRqcF_YUNxt4hCE8mm2mFo9RhDZeaNfSeDyU_gqPSARN3E3jA6jNwPNBqzlL3gZJg-4TRLq88s3rdVmpNF6WpHuf0aWECQsDxPkn_T7vFMBG8VCB8qeicAHlckRXeuscm4pwuKYZaaTHQgPIVInFEbRhtPD9VWmHdqsvvbGjSthBswCQSKwJVIHRiKAr1_2CQWtbukkfS9zHlUHEfUMEDsne6ayC_N5jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر عاشق کیک خونگی هستی، این ۵ ایده خوشمزه رو از دست نده
🍰
🧁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/674788" target="_blank">📅 13:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674787">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb1e594d7.mp4?token=a6PTzFxwxi6ncxO2jzeL9Z6CZV7bCjfmpXCC_sm-bB2KVOgrqKK0DYRFTitPwrXRTUi5oKo4S3nCzjS9IVBRyp7j84hPiXC40dnR185dW8kEB4k85bxeHNfO-nIyzATAiS2kmYsKHg-wcHl-hmZTtcQGDs-LIUCA6Esah_6MjWnBjuIaWDE-dJyrWlglaJ8_3xM9ej7vsydv2BgGClf4k4J0hfSPS3ydNHVXJdG-HGFfexrhXvlfh5WaUpXPkeGz0-UmV57is-c0HeHOWG1RjwfJxj8ee3619R1TIzBNJOtsw5tiYspS4WtQZqLlCD4b2hwL-WgjxDmHz1lnPtytZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb1e594d7.mp4?token=a6PTzFxwxi6ncxO2jzeL9Z6CZV7bCjfmpXCC_sm-bB2KVOgrqKK0DYRFTitPwrXRTUi5oKo4S3nCzjS9IVBRyp7j84hPiXC40dnR185dW8kEB4k85bxeHNfO-nIyzATAiS2kmYsKHg-wcHl-hmZTtcQGDs-LIUCA6Esah_6MjWnBjuIaWDE-dJyrWlglaJ8_3xM9ej7vsydv2BgGClf4k4J0hfSPS3ydNHVXJdG-HGFfexrhXvlfh5WaUpXPkeGz0-UmV57is-c0HeHOWG1RjwfJxj8ee3619R1TIzBNJOtsw5tiYspS4WtQZqLlCD4b2hwL-WgjxDmHz1lnPtytZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تقدیر سهامداران از تقسیم ۲۰۰ تومان سود نقدی در مجمع شرکت نفت سپاهان »
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/674787" target="_blank">📅 13:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
درآمد دلاری نفت ایران ۱.۵ برابر شد
🔹
اطلاعات رسیده از وزارت نفت مشخص کرد، درآمد نفتی ایران از فروردین تا تیرماه امسال نسبت به مدت مشابه سال قبل ۱.۵ برابر شد؛ این درآمد علی‌رغم شرایط جنگی حاکم بر کشور به دست آمده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/674783" target="_blank">📅 12:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
چین صادرات به ۱۴ شرکت اروپایی را ممنوع کرد
وزارت بازرگانی چین:
🔹
علت اعمال محدودیت بر صادرات کالاهای دو منظوره نظامی و غیرنظامی به ۱۴ شرکت اتحادیه اروپا به دلایل امنیت ملی است. این ممنوعیت از امروز اجرایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/674782" target="_blank">📅 12:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سفر یکسره زائران اربعین تا نجف امکان‌پذیر شد
🔹
برای نخستین‌بار زائران اربعین از تهران، قم و اصفهان می‌توانند با اتوبوس یکسره و بدون تعویض وسیله نقلیه، از مرز خسروی تا نجف اشرف سفر کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/674781" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIHJopQ1kFb39_BdOCHrR0zo-_QCIIwSbaCv_shPnp7d9fsYruwa-ZLiLw-Zmlb_gjdZLhO4SBH364ItlVIUYTjExB9essD16q25h69JY_y2AdmLqrSYprp0dqAxmKdu-CISJYNdg3Q8qlo-ytkltFQLFDr_CaFDW4IFj3bRoEzPZlAN5LTO8oTcCMSNkAsmn5vDgnyVKwl9rrOs2UQmYWGvqwfpm_qmuQZyfMgT-iiGwDMI2cS1ToirgZB0dMpLD19JiyhUEZ0t7xDK3g3DJaTlN8QFSnwhSMWQULttrFWSYrTqsHeBK5KmEbil4TJNtv_k1saSBcMNVHk_p3z2QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/674779" target="_blank">📅 12:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
جزئیات جدید از جلسه شمخانی در بیت رهبری که ۹ اسفند بمباران شد
🔹
در روز جمعه ۸ اسفند ۱۴۰۴، برای شمخانی و شماری از فرماندهان ارشد نظامی تقریباً قطعی شده بود که آمریکا و رژیم صهیونیستی در روزهای آینده به ایران حمله خواهند کرد.
🔹
شمخانی همان شب، حوالی ساعت ۲۱، متنی را برای انتشار در اختیار واحد اطلاع‌رسانی دبیرخانه شورای دفاع قرار داد که در آن به احتمال حمله مشترک آمریکا و اسرائیل و واکنش ایران به این سناریو اشاره شده بود.
صبح روز بعد، کمیته فرعی شورای دفاع با مسئولیت دبیر شورا تشکیل جلسه داد.جلسه دو دستور کار داشت:
🔹
نخست، پیگیری اجرای طرح جامع مدیریت اغتشاشات؛ طرحی که ریشه در دغدغه چندین‌ساله رهبر انقلاب و شمخانی و پس از حوادث دی‌ماه ۱۴۰۴ به یک اولویت فوری تبدیل شده بود.
🔹
دوم، بررسی موضوع قریب‌الوقوع بودن حمله آمریکا و رژیم صهیونیستی به ایران.
🔹
این دو دستور کار، در ظاهر از دو جنس متفاوت بودند؛ اما در واقع به یک واقعیت مشترک مربوط می‌شدند: کشور در برابر تهدیدی چندلایه قرار داشت و باید هم برای جنگ خارجی و هم برای مدیریت بحران‌های امنیتی و اجتماعی آماده می‌ شد جلسه در حال برگزاری بود که حمله آغاز شد.
🔹
در جریان این حمله، دریاسالار شهید علی شمخانی و تعدادی از فرماندهان عالی به شهادت رسیدند.
🔹
به این ترتیب، جلسه‌ای که قرار بود هم اجرای طرح کاهش تلفات در اغتشاشات را پیگیری کند و هم درباره قریب‌الوقوع بودن حمله دشمن تصمیم‌سازی کند، خود به یکی از آخرین جلسات پیش از آغاز جنگ تبدیل شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/674778" target="_blank">📅 12:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa9f28389.mp4?token=GLGj5mKJ-3edJl2ya7evvFYUKL7kpFOJZ2H6LQuc0pnZhjjVoNZl8EKOfrekwJRe6HigO_dqhyXmZeC28hryU-xluociXT8JwEIEKZcpHX-Z8uJIb31IQAyZ78cWpGHEmHQ1Uu-zTaIXq78L6LKQchtmRq9FPd4BlgOmnUtTOC-ew6G1fQ0yOfFVxb5wnnu09xIgQFQmxraG7eIAUEikysiNlZL5hRH8LLxKEPB7olkeGtcLXYYiUmtZKhjjfdCE35jUndOL0kLuS1fewb7GMxT_pLUzNGvI4LCDzx5LxMzUtjEDwi90ifxD_nXO42tniE2uCowEn2UJ_q-qegvLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa9f28389.mp4?token=GLGj5mKJ-3edJl2ya7evvFYUKL7kpFOJZ2H6LQuc0pnZhjjVoNZl8EKOfrekwJRe6HigO_dqhyXmZeC28hryU-xluociXT8JwEIEKZcpHX-Z8uJIb31IQAyZ78cWpGHEmHQ1Uu-zTaIXq78L6LKQchtmRq9FPd4BlgOmnUtTOC-ew6G1fQ0yOfFVxb5wnnu09xIgQFQmxraG7eIAUEikysiNlZL5hRH8LLxKEPB7olkeGtcLXYYiUmtZKhjjfdCE35jUndOL0kLuS1fewb7GMxT_pLUzNGvI4LCDzx5LxMzUtjEDwi90ifxD_nXO42tniE2uCowEn2UJ_q-qegvLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند ساده که لباس‌ها رو تمیزتر و سالم‌تر نگه می‌داره
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/674777" target="_blank">📅 12:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674775">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
چشم دیجیتال سنتکام در بحرین کور شد
🔹
منطقه ابری آمازون در بحرین که با شناسه انحصاری me-south-۱ شناخته می‌شود، نخستین پایگاه متمرکز پردازش داده شرکت آمازون در خاورمیانه است که در سال ۲۰۱۹ راه‌اندازی شد. تاسیسات آمازون در بحرین شریان اصلی و مغز متفکر پردازش…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/674775" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27e007073.mp4?token=mzW0QWbrPcta1ZVX6pWUYGOubZHBdBjZnyhVZ2pqkNtyMI1tmlb18GVzoL4_ncg-s1eFOGLkz_zKd9cErwjup2yAVwsfMGGatR5wmytZn7qz3bTKNbj2oObSl2VaJ_vxI3cRUf9bGmwd-pKbOGk-7ha3PnNl43Tre7Vk2qZx2PRROM1CjEgUV4R0M_Jsbj7UXgdR7hGuPDmjtrHBgwgkH5jahS8-XfEOkB7dGTlZ-5E341Ta93m5dcQHtSbJotqJpzEdt0M3S3-jFeyFD2_fab1uELo6y3JyoeU_13W-lQxTHeU8mfY7MJPfR_ig2U-hkAfnyKgiAvyRAG9Js2rtNTAOWHaDq--LOQu2TbqcvgF-r26JnWOohiRwl5l82jyEvqy69j-iGPmiKE4FqwDrQYxb3UxJnn8GJU8wymxuFGIL5oVhWAyYmadVNKSDedP31rgBOe8TGTHMWf1Ikl6Kk4Ayv_ldcPfKQfj4-ZfW99workMe3qDBDqIO48RRYNpa26NP_O-bIeRm-b7xCEsEG4_S-h3b7k-SbkKks9d02Krp6ky5-n_L8TcIXWBCapQMY9zbMiEYcqT-82ZBi4XUBEbCwiip0QEeFXu_vBHKa3OJsz1PqZRK61G1gCvUQBscEOGIOxBMSe8GCahErzrtv8AnFv-jNxDGESPIWh30aKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27e007073.mp4?token=mzW0QWbrPcta1ZVX6pWUYGOubZHBdBjZnyhVZ2pqkNtyMI1tmlb18GVzoL4_ncg-s1eFOGLkz_zKd9cErwjup2yAVwsfMGGatR5wmytZn7qz3bTKNbj2oObSl2VaJ_vxI3cRUf9bGmwd-pKbOGk-7ha3PnNl43Tre7Vk2qZx2PRROM1CjEgUV4R0M_Jsbj7UXgdR7hGuPDmjtrHBgwgkH5jahS8-XfEOkB7dGTlZ-5E341Ta93m5dcQHtSbJotqJpzEdt0M3S3-jFeyFD2_fab1uELo6y3JyoeU_13W-lQxTHeU8mfY7MJPfR_ig2U-hkAfnyKgiAvyRAG9Js2rtNTAOWHaDq--LOQu2TbqcvgF-r26JnWOohiRwl5l82jyEvqy69j-iGPmiKE4FqwDrQYxb3UxJnn8GJU8wymxuFGIL5oVhWAyYmadVNKSDedP31rgBOe8TGTHMWf1Ikl6Kk4Ayv_ldcPfKQfj4-ZfW99workMe3qDBDqIO48RRYNpa26NP_O-bIeRm-b7xCEsEG4_S-h3b7k-SbkKks9d02Krp6ky5-n_L8TcIXWBCapQMY9zbMiEYcqT-82ZBi4XUBEbCwiip0QEeFXu_vBHKa3OJsz1PqZRK61G1gCvUQBscEOGIOxBMSe8GCahErzrtv8AnFv-jNxDGESPIWh30aKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر شلیک پهپادهای پیشرفته و فوق سنگین در موج ۲۷ عملیات نصر۲ علیه زاغه مهمات و سوله‌های نفرات آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/674771" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۷
یک زاغه مهمات بسیار بزرگ و سوله‌های محل اسکان نفرات در پایگاه علی السالم، به طورکامل متلاشی شدند
روابط عمومی سپاه:
بسم الله قاصم الجبارین
قاتلوهم حتی لاتکون فتنه
🔹
رزمندگان اسلام در ادامه عملیات تنبیهی علیه ارتش کودک‌کش آمریکا و در پاسخ به جنایات شیطان بزرگ، ساعتی پیش در موج ۲۷ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" با پرتاب پهپادهای انهدامی فوق سنگین و پیشرفته، یک زاغه مهمات بسیار بزرگ را در پایگاه آمریکایی علی السالم هدف قرار داده و آن را با انفجارهای پی در پی به طور کامل متلاشی کردند.
🔹
همزمان سوله‌های محل اسکان نفرات این پایگاه مورد حمله قرار گرفت که ۶ سوله بزرگ به طور کامل نابود شد و به سه سوله دیگر خسارات اساسی وارد آمد و تعداد زیادی از عناصر دشمن کشته و زخمی شدند.
🔹
دشمن آمریکایی که در جنگ تحمیلی ۵ ماهه اخیر صدها کشته و بسیار بیشتر از این مجروح داده است و تخلیه روزانه انبوه زخمی‌های آن با هواپیمای آمبولانسی به بیمارستان آمریکایی در آلمان سند روشنی بر این تلفات بالا است، با دروغگویی به مردم خود مدعی است کمتر از ۲۰ کشته داده است.
🔹
این بر عهده رسانه‌های آمریکایی است که در مورد واقعیت‌های این جنگ و تلفات بالای ارتش آمریکا و خسارات سنگین آن و ارقام هزینه‌ها که همه از دید مردم پنهان نگاه داشته می‌شود، تحقیق کنند و آمار واقعی و شیوه‌های سانسور حکمرانان دروغگو را افشا کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/674770" target="_blank">📅 11:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0438202017.mp4?token=YNblR5i-AL31dhaL0hHcZClNaIwEirsT1Vge8kf2-1NlVEHUFCIXaL_G4HhRAXSiLQ4j_jgy6v0QAdxQ5p_0VC7Rnk9eCoSWTNixSqWnQfBfEIvf7ZNYWSYv0WPyvGSicyrGCfeEjKrb-bHGIjf7zYs7MJZROnVoXOjlrkktoHHAj6D8vC1NfKFnsWrT3xYxKteeK1ac1bgvc4kcvZyc0J4dx9YOynzVMQQTzSYihVqv8tu1V0zNGG6kYffubo1NTJJRpECDIIBtBUuknUaNcWnrXSSuWSEadfL8_EaUEEHAHvW4LA1XBXrpxD-pZqPohITLXn3ASzfBaqyxWg-2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0438202017.mp4?token=YNblR5i-AL31dhaL0hHcZClNaIwEirsT1Vge8kf2-1NlVEHUFCIXaL_G4HhRAXSiLQ4j_jgy6v0QAdxQ5p_0VC7Rnk9eCoSWTNixSqWnQfBfEIvf7ZNYWSYv0WPyvGSicyrGCfeEjKrb-bHGIjf7zYs7MJZROnVoXOjlrkktoHHAj6D8vC1NfKFnsWrT3xYxKteeK1ac1bgvc4kcvZyc0J4dx9YOynzVMQQTzSYihVqv8tu1V0zNGG6kYffubo1NTJJRpECDIIBtBUuknUaNcWnrXSSuWSEadfL8_EaUEEHAHvW4LA1XBXrpxD-pZqPohITLXn3ASzfBaqyxWg-2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرار گرفتن انبارهای کنسولگری آمریکا در اربیل
🔹
برخی منابع اعلام کردند هدف از حمله به اربیل، انبارهای کنسولگری ایالات متحده در اربیل واقع در شمال عراق بوده است.
🔹
در عین حال گزارش‌هایی از تعلیق پروازهای فرودگاه بین‌المللی اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/674769" target="_blank">📅 11:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
خشونت پلیس آمریکا و کشتن یک سیاه‌پوست بی‌خانمان
🔹
کوری دورل روئیز، ۳۸ ساله، در یکی از خیابان‌های شهر هدف گلوله پلیس قرار گرفت و جان باخت. لحظات تیراندازی توسط شاهدان عینی فیلم‌برداری و ویدئوهای آن در شبکه‌های اجتماعی منتشر شد. پلیس تاکنون هویت و نژاد مأموری که شلیک کرده را اعلام نکرده است. در سوابق قضایی ایالت ویسکانسین، روئیز به عنوان فردی سیاه‌پوست یا لاتین‌تبار معرفی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/674768" target="_blank">📅 11:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1434f8b7b.mp4?token=YNIO-_lrGejOsCg418e7xnZqvPY1koIBrN8ScFh04rYJEdUszVdanSt2xadMZaaGCPr4wNi_GmVwA7r_u7gd_XMfEBZOmDDpl1l6SJaXZnvr3vbwPSEMMP_q5CokdNhgY87cEpX18MBlRb4izaMgupqWCmPJr8eeZw-i-YIglX08ny202mQTUNHDEsmr83RLQDUxJG57V1yf2XirLuMaOEUNHp4dJP1ipFZa3BHdWPW5SrJvaYu4fT6cOssqi8_fMFSfVa7re8kyfXUPRIZhmFoUXG_F9KOwE2JTkB-P9yojGKR3hTi_vvpAj-ZApPKCWZ1Et49_pW71Tq2mmQHOvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1434f8b7b.mp4?token=YNIO-_lrGejOsCg418e7xnZqvPY1koIBrN8ScFh04rYJEdUszVdanSt2xadMZaaGCPr4wNi_GmVwA7r_u7gd_XMfEBZOmDDpl1l6SJaXZnvr3vbwPSEMMP_q5CokdNhgY87cEpX18MBlRb4izaMgupqWCmPJr8eeZw-i-YIglX08ny202mQTUNHDEsmr83RLQDUxJG57V1yf2XirLuMaOEUNHp4dJP1ipFZa3BHdWPW5SrJvaYu4fT6cOssqi8_fMFSfVa7re8kyfXUPRIZhmFoUXG_F9KOwE2JTkB-P9yojGKR3hTi_vvpAj-ZApPKCWZ1Et49_pW71Tq2mmQHOvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از یک نوزاد تازه‌ متولد شده که به نظر می‌رسد هنگام معاینه، قدرت بدنی قابل‌توجهی از خود نشان می‌دهد، در شبکه‌های اجتماعی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/674767" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674765">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUEtVnebcY0bCtz4dwF_asN2sUFavU9d30Y9G1ww-ESx4ugZRxko_0ZVTsNVuWJ7FXSzcm4ib8sQngZNQ9z93oKHxlh9iDCkQEhT23xbdQgi1UbQkRegdYAD9iO1R8tNItjjH73boUDtx-Qx8nli3XXLh8bArqOQJo4jnF9OglC3mWcvbgokZFK2fOfouyRCPBUvUVgv0EAeXKrwp55AlKQ9mjgemHqXtTvPVtStquNmJTY03BLkvj46Z2mHRH-GCS-Rz4sPfOZAXOUqiAvDKjGZ_chK9Bx1-BC4WbCmIB0P-Nfc2uxzQ9GL64VGUTePpxcAb-xwSxCafM7VK8IFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با پول یک موتور یاماها، سال‌های گذشته چی می‌توان خرید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/674765" target="_blank">📅 11:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=m0RytvI23DwNIeKlMobn1jjEt5cK-BY3RxzcexvvmnKzGkKLNM8g7iOUEtw5bgrNP_gS1Ea907rBfWancwusHb1UjrZ3W852O6t4QjJk6zxJJp1DzGvSSbwjXEoPpEd9jQfMI8C8j7uRK3VWDbhyqNXqUMt5NQsk1tkb7tkunaY5GarzDRl_FAC2j-n5b6Df5kM6KuKW0Hxfuj35Ll_Uxdjs7G_KO6YiqFd_BG0Vx6_FyRZSDXvCCSa-h_i83hMLG3fa-WuFVzFP0QB6EJFUcw2RFKIeHUwpqqUkPFQtwDjZDN_m0tCxHTiHL6rb4f_q0AiYOKnrbufGf34OJJOXog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=m0RytvI23DwNIeKlMobn1jjEt5cK-BY3RxzcexvvmnKzGkKLNM8g7iOUEtw5bgrNP_gS1Ea907rBfWancwusHb1UjrZ3W852O6t4QjJk6zxJJp1DzGvSSbwjXEoPpEd9jQfMI8C8j7uRK3VWDbhyqNXqUMt5NQsk1tkb7tkunaY5GarzDRl_FAC2j-n5b6Df5kM6KuKW0Hxfuj35Ll_Uxdjs7G_KO6YiqFd_BG0Vx6_FyRZSDXvCCSa-h_i83hMLG3fa-WuFVzFP0QB6EJFUcw2RFKIeHUwpqqUkPFQtwDjZDN_m0tCxHTiHL6rb4f_q0AiYOKnrbufGf34OJJOXog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج دیگری از حملات پهپادی ارتش به پایگاه‌های آمریکا در کویت
روابط عمومی ارتش:
🔹
در مرحله بیست و پنجم عملیات صاعقه؛ ارتش جمهوری اسلامی ایران در پاسخ به تجاوزات دشمن سلطه جو، ساعاتی پیش، «انبار‌های تجهیزاتی ارتش تروریست آمریکا در اردوگاه العدیری، و  «محل استقرار نظامیان آمریکایی» در پادگان الدوحه و «محل استقرار نیروهای دشمن مستکبر» در اردوگاه عریفجان کویت را هدف پهپادهای انهدامی آرش قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/674762" target="_blank">📅 11:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df94d94be.mp4?token=VP0zYQtYxDc2rcxXQKz9VPij0l4NVWtvSH8cKF7T-C0new4BJdIWh4oNvakH3DS1peWxbtA7X-LTohd8Ngt4bIzPvgljctw3z8V809T_4klGHabN6kOAvj1oxiQ79kdOIVCh530DZH-7XWf81joDpFnIK0lC6l4DLBvk-fQS0_FbRMBFmxo-H_iVH5n2dpq_K3VM2aQ7WRtlMsoMKfbMt9W7XSFf1PK_tnJUdF_BTEbg0DNqb0S-Jh2nzKQjoAW99m0__YuJemZ51TboiWdKQ2mmWyaGdBUK4frlQHjRaelNv29YIgjfrobgofQxQ9_Iju__JIHgs20DfenHJT6nKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df94d94be.mp4?token=VP0zYQtYxDc2rcxXQKz9VPij0l4NVWtvSH8cKF7T-C0new4BJdIWh4oNvakH3DS1peWxbtA7X-LTohd8Ngt4bIzPvgljctw3z8V809T_4klGHabN6kOAvj1oxiQ79kdOIVCh530DZH-7XWf81joDpFnIK0lC6l4DLBvk-fQS0_FbRMBFmxo-H_iVH5n2dpq_K3VM2aQ7WRtlMsoMKfbMt9W7XSFf1PK_tnJUdF_BTEbg0DNqb0S-Jh2nzKQjoAW99m0__YuJemZ51TboiWdKQ2mmWyaGdBUK4frlQHjRaelNv29YIgjfrobgofQxQ9_Iju__JIHgs20DfenHJT6nKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرار گرفتن انبارهای کنسولگری آمریکا در اربیل
🔹
برخی منابع اعلام کردند هدف از حمله به اربیل، انبارهای کنسولگری ایالات متحده در اربیل واقع در شمال عراق بوده است.
🔹
در عین حال گزارش‌هایی از تعلیق پروازهای فرودگاه بین‌المللی اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/674761" target="_blank">📅 10:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674758">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14b5c80fa.mp4?token=VWlGYsBFD7qD-et6W_jvFWl2ZG3rzGTSpmQDtfVuJN_FS-8UTbnjLGC4LxyH5gsQrmf1RSFeA6WRudT3jDxfOSTtPmIBD6c4yhW-fYybXQzqq-uWDviQR9dNXZgePUa3v_y6KfcCzDRJ0XAA8_eNuDeH_EZFiQOhRrZCRJy-2K9LxhMHXGA04DxDLPZKfhp5_crgXijNjVzEY9HYOYbXCDR99ptTRXr9HP4YyXgsL88iU7BRlcQan_9_1xL8uiGWtv14IsIlwDTCHm_qTyoQigN5iYC_s4RLXpgA_yPuZSUDCCWmwZuncD04o8jC38Lp3O-VQGmYVWFGeeS_BjKaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14b5c80fa.mp4?token=VWlGYsBFD7qD-et6W_jvFWl2ZG3rzGTSpmQDtfVuJN_FS-8UTbnjLGC4LxyH5gsQrmf1RSFeA6WRudT3jDxfOSTtPmIBD6c4yhW-fYybXQzqq-uWDviQR9dNXZgePUa3v_y6KfcCzDRJ0XAA8_eNuDeH_EZFiQOhRrZCRJy-2K9LxhMHXGA04DxDLPZKfhp5_crgXijNjVzEY9HYOYbXCDR99ptTRXr9HP4YyXgsL88iU7BRlcQan_9_1xL8uiGWtv14IsIlwDTCHm_qTyoQigN5iYC_s4RLXpgA_yPuZSUDCCWmwZuncD04o8jC38Lp3O-VQGmYVWFGeeS_BjKaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باستر کیتون؛ نبوغی که قرن‌ها جلوتر بود
🔹
باستر کیتون، خدایگان بدلکاری بود زیرا او این کارها را در بیش از ۱۰۰ سال پیش انجام داده است.
🔹
از اسکار ۲۰۲۷، قرار است شاخه بهترین بدلکاری هم به جوایز اضافه شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/674758" target="_blank">📅 10:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674757">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgZHC-TUIudN-Pb7a6fYsUetre_dD91yEBdOvKkjTYpFmVB-L9y4HQ2_TIyz3BaOaIAYzjbaivkuu0RYyz6H18sviIBtvAcDnR-WA52sGRJCsmToLrIGyt9Zef4ntb3R8W2UCR12OV-qkl8jOH2M3eV1cmzsEX6VzC3KfJ1A_o7q5Z_7RTjgp_j0tw7_SuLvgu3EQmBLXnW-A19j6yDIVtiyTySTQtAxOi7k8FImC-SXbfwguY7Tw_0rwJBJmesNZaIJHaF6rYheSnzcBwL9nIh13Ii58ll5MQlfbCp6jEGyMln1K5KAsvEBpUaV3CGvWyXlU-EhWZX_7ycxqP_fCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
ایران، خانه مشترک همه ماست؛ سرزمینی با فرهنگ‌ها، شهرها و لهجه‌های گوناگون که هرکدام بخشی از هویت آن را شکل داده‌اند. هر اقدام کوچک ما، از حفظ محیط زیست و مصرف بهینه انرژی تا همراهی و همدلی با هموطنان جنوبی‌مان، می‌تواند نشانه‌ای از مسئولیت و عشق به ایران باشد. شما برای ایران چه کاری انجام می‌دهید؟
🔹
همراهان گرامی خبرفوری؛ برای پیوستن به این پویش، یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کنید و با نام و لهجه شهر خودتان بگویید:
«من ... هستم از ... و ایران را دوست دارم، چون ... و به خاطر ایران میخواهم...»
🔸
پیام صوتی خود را با دلیلی که باعث می‌شود ایران را دوست داشته باشید، به آیدی‌های زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/674757" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674755">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf31b84ef9.mp4?token=gb1DXGCPZYnIBDwF99SU_SFS5fTyOnIFermC3o08zzOlb0r8s8wRefLOTa-51B3CllLL7JNNROL_xWdw7_ANID4vQX_SlVkQ2L92Y65en8inujjD8jE_xepY71HglAE6FvNC_llz5VZRIl-G86aaYPpqCGLuER08-8aqGpeGDXFNwAi7zMDoacA1F-oQyi7kTsK13j0nLFSXvMEzOQeC_JXud0nGwE0i-guAdpeWkcsYr0ZgAgEp5u5Z9RMm166d5HKSgOGbmGiObD9WCvg59lLcN2KYOUvSiLV7ux_v7jDEtAzP5pFnI4XTA6BD5a6qnthoVkMuxOu_FKXtuMYjkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf31b84ef9.mp4?token=gb1DXGCPZYnIBDwF99SU_SFS5fTyOnIFermC3o08zzOlb0r8s8wRefLOTa-51B3CllLL7JNNROL_xWdw7_ANID4vQX_SlVkQ2L92Y65en8inujjD8jE_xepY71HglAE6FvNC_llz5VZRIl-G86aaYPpqCGLuER08-8aqGpeGDXFNwAi7zMDoacA1F-oQyi7kTsK13j0nLFSXvMEzOQeC_JXud0nGwE0i-guAdpeWkcsYr0ZgAgEp5u5Z9RMm166d5HKSgOGbmGiObD9WCvg59lLcN2KYOUvSiLV7ux_v7jDEtAzP5pFnI4XTA6BD5a6qnthoVkMuxOu_FKXtuMYjkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلند شدن ستون‌های دود از فرودگاه بین‌المللی اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/674755" target="_blank">📅 10:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674754">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf97b1a3c.mp4?token=OOK7AkF8uEK_3OH0yJatGa9coqX6w1xnZ7xegap_hffd-jyCUEj3NWczaWc5G_RMErltfSjeSekV_dYblchUsF_pxE-2TOJ93bWUxDamB7ADrecv8uddaGlL6bnRyKWhQrcWyk04a45Q_CAemmPjlgaeV41kWgJVa-M5hLseH2hcNa5GXUhBVvFXXSoR0ceOS7IETr2nyYFzpx70oibOIQ4Ke46AUr01Gq-cmwUgHjUif_BrYXlXAYX2mzeoXM0aDk1b2Pv3xBh9ddbq4AFErG2ip23mvEd_q6mPqktaaONO03WNL7lGu0fMycx-BdbeZ_DivGFZfxBx5nAmvXxViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf97b1a3c.mp4?token=OOK7AkF8uEK_3OH0yJatGa9coqX6w1xnZ7xegap_hffd-jyCUEj3NWczaWc5G_RMErltfSjeSekV_dYblchUsF_pxE-2TOJ93bWUxDamB7ADrecv8uddaGlL6bnRyKWhQrcWyk04a45Q_CAemmPjlgaeV41kWgJVa-M5hLseH2hcNa5GXUhBVvFXXSoR0ceOS7IETr2nyYFzpx70oibOIQ4Ke46AUr01Gq-cmwUgHjUif_BrYXlXAYX2mzeoXM0aDk1b2Pv3xBh9ddbq4AFErG2ip23mvEd_q6mPqktaaONO03WNL7lGu0fMycx-BdbeZ_DivGFZfxBx5nAmvXxViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماسال؛ روستایی که همسایه‌ ابرهاست
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/674754" target="_blank">📅 10:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
حمله موشکی دشمن آمریکایی به مقر نیروی دریایی سپاه در زیباکنار
معاون سیاسی استانداری گیلان:
🔹
صبح امروز مقر نیروی دریایی سپاه در زیباکنار، هدف پرتابه های دشمن آمریکایی قرار گرفت که بر اثر آن بخشی از تجهیزات مستقر در این مجموعه آسیب دید.
🔹
تاکنون هیچ‌گونه گزارشی از تلفات انسانی دریافت نشده است
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/674751" target="_blank">📅 09:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f3118cae.mp4?token=p1Ux1bcUZ1JeUjV1lzvh8SZ2-WXT8Z1wccjBeL3ugS2qDp2mSo2sMGAnUCbL24589TNzVMgTWOlDsI-Q5297dpn5POZB0RY_ATfgBTiM41how4pmaJI3MC6aWIW0CY74BRZqGwEI_ZAh5YfFEfBrr3A8P1wAhDlRxCGl7Lq3G4FTHdzynNvwr0AyrZyIDxau-hfGCT190Y8k-OSmovHzmpWvL8DWBWNqCy8OAuxfWk5wn1vM8kNDz4de1WyXKTOXC6mV0bK-fj6_kDwRT4h7cbzhCYfSrKIdkGWvHeuXKDcGiq0UiJULtW7HIGhzTfqjpmK4coRxX29IGBS7B946QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f3118cae.mp4?token=p1Ux1bcUZ1JeUjV1lzvh8SZ2-WXT8Z1wccjBeL3ugS2qDp2mSo2sMGAnUCbL24589TNzVMgTWOlDsI-Q5297dpn5POZB0RY_ATfgBTiM41how4pmaJI3MC6aWIW0CY74BRZqGwEI_ZAh5YfFEfBrr3A8P1wAhDlRxCGl7Lq3G4FTHdzynNvwr0AyrZyIDxau-hfGCT190Y8k-OSmovHzmpWvL8DWBWNqCy8OAuxfWk5wn1vM8kNDz4de1WyXKTOXC6mV0bK-fj6_kDwRT4h7cbzhCYfSrKIdkGWvHeuXKDcGiq0UiJULtW7HIGhzTfqjpmK4coRxX29IGBS7B946QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به انبارهای لجستیک روسیه در سن‌پترزبورگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/674747" target="_blank">📅 09:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674738">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عراقچی: هرگونه مشارکت در تجاوز به ایران مسئولیت بین‌المللی ایجاد می‌کند/ امنیت خلیج فارس با همکاری کشورهای منطقه تأمین می‌شود، نه مداخله خارجی
🔹
آمریکا به تعهدات خود پایبند نیست و موجب اخلال در جریان عادی کشتیرانی تجاری بین‌المللی شد.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/674738" target="_blank">📅 09:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
عراقچی: هرگونه مشارکت در تجاوز به ایران مسئولیت بین‌المللی ایجاد می‌کند/ امنیت خلیج فارس با همکاری کشورهای منطقه تأمین می‌شود، نه مداخله خارجی
🔹
آمریکا به تعهدات خود پایبند نیست و موجب اخلال در جریان عادی کشتیرانی تجاری بین‌المللی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/674736" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674734">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4n-Xn_y3jQIVl3OvxTAw0djCMcx4dDMgfIj-P05FfZd_gcDT4NuwUbV_VcAjpQSgPzaYUnAkjHNSwMdyAVX2COYoRk5H8QYxncD_ZDGZbe7EvR7dHhiG3gJvcYvtZdkoGkP1yhMX8qD8A4rCteSC4po0xXtfFfOGl-imsqSXxxKLUKPqjunoQMvSDzfYu9YoEP8SfjFY2XWQ_ibldRwsQwcniRp58LQ22FEZbVYP1WpHrAauRstJNfEp342fJeC3Br8ZIVKXxCqfBE7pwVsuTjuxM8AWLRvU_XGekua3yO3R1FHsAyJ3Gw0SE64P8IajprRrw0uH2sJ3gc8yyrlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم پنهان مسمومیت با آفتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/674734" target="_blank">📅 08:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967e2e2884.mp4?token=HeM7H3Yq74aV-V2bZCAB5_ENYJZPppa8yM-FoBgg-A8HbHczae6DI4WrgAmaTS1rFkmA8EFxddObN3_oYuak7bPlGyRQf-EbjxL4HgZInvJlI667Hs-bmzfd1HmFnPfLeHKP0OZ3UgcF4fnisvWIgUrgGPfrZcRY8r2PDB49wYqYHpQrBnTISEZ_Xr-6XtjLqkhllhHNzIGjHMKA3Ovz_cQ4_hvGLqHC0d92GyxVZt1n73WaIssSrS8QVTT_-wg5Sbd68Sx2LD63boGN_vHkh_TAuOy4awI6FrjFwe3so7oOtyu6bopJKBJqI4ba6VhmxcTkz_wJyjQJsbwoJ5AdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967e2e2884.mp4?token=HeM7H3Yq74aV-V2bZCAB5_ENYJZPppa8yM-FoBgg-A8HbHczae6DI4WrgAmaTS1rFkmA8EFxddObN3_oYuak7bPlGyRQf-EbjxL4HgZInvJlI667Hs-bmzfd1HmFnPfLeHKP0OZ3UgcF4fnisvWIgUrgGPfrZcRY8r2PDB49wYqYHpQrBnTISEZ_Xr-6XtjLqkhllhHNzIGjHMKA3Ovz_cQ4_hvGLqHC0d92GyxVZt1n73WaIssSrS8QVTT_-wg5Sbd68Sx2LD63boGN_vHkh_TAuOy4awI6FrjFwe3so7oOtyu6bopJKBJqI4ba6VhmxcTkz_wJyjQJsbwoJ5AdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست و چهارم عملیات صاعقه ارتش؛  پایگاه‌های آمریکا در اردن و بحرین هدف حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در ادامه حملات پهپادی ارتش جمهوری اسلامی ایران و در بیست و چهارمین مرحله عملیات صاعقه، بامداد امروز، «مخازن سوخت»، «انبار و سوله‌های بزرگ تجهیزاتی» و «محل اسکان» نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین هدف پهپادهای انهدامی آرش قرار گرفت.
🔹
در ادامه این مرحله از عملیات صاعقه، «آشیانه هواپیماها»، «آشیانه تعمیر و نگهداری هواپیما» و «محل اسکان» مزدوران ارتش متجاوز آمریکا در پایگاه الازرق اردن نیز، هدف حملات پهپادی ارتش  قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/674732" target="_blank">📅 08:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
‌
رسانه‌های عربی: ناوگان پنجم نیروی دریایی آمریکا در بحرین، مورد حملۀ هوایی قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/674728" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOnUuMYoPNFQmmw0C7iMkX4Iet52gxpYeUgWn-AQGvOuOmpCC9zeEShs77MyFrqPOZQJ5euUXbjc7JxUjGWOtoxgku-iXdYMDeAdDaZJ14W-1pwlGxBMKcylVh82jHR9u_mWfwzunQxw8ArBsmuAkSvbqT5JriMreApM76McMaH03ID5fiEmlbtd3pCnDxOn4iMhI1AbZAzHWOM6rR2dOHi2_ZHkvGuhnnJ_DN_bYzs1tPm67dNY48J4rdsQnkr_LGXbR4KYnClvI5A6MPUxdn7w7pDqb4f9YRCWWSn2M1Pv4Rml43ayFlEoY1YPEXpiPTsEwZ8RLyYd_jkW3oTcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۴ اپلیکیشن، عادت‌های دیجیتالت را متحول می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/674723" target="_blank">📅 07:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674721">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfpkt7CTTCxdtY4bOqkP5wEa5TI2UEQkBnGW9FdD_N6YYhtk0XixuYS_PXvfFioxsQEwm5foXtjpPh76i62BX2gEnvfCa_kviETE_ROma-TapNeTUX2LKZni6l1wyOKeMo86J0wyk5flsXglaqMQEbdSSakM8IynK1j2OaV8zG1f1B8JPvH9Taw3WtLtlYEaUwrr1mtYqPZoK2E-lsyovsUqD5xFSicWD5WNnCdqITWEfFhyVdIY43mWubOOdhR-sbG0UgkLoI_2pKT7mc57WmaATLJY4-1O5y7GynQO9zviRBEaWiI94DuC6B6IF_4ZGhKvrxqtDTXzdXbbg9x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس یادگاری وزرای خارجه سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/674721" target="_blank">📅 07:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674720">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njecuXOTENRUqIMaDhenqW20g6aNlclWUzyMVSkDvn5H-x1omf74AcycL83wV8U5VOsMYCM56c6vubGEeAQpMzdV2N-BaI2hgodOuQ_ckk3csh0LXFTkZxfTkEsX-YG1vqFzUH-3Zb7-L8xOg4d7sIL9_CB_akJ45UCzxW3JMxxiKxh8izAfTs45F66rN04Mw-8lRY1wpvEMReQZS4uTn0ybOSukBJL8Fl06vdjgfPwZYhVyAgsUUCyUtoOUq8iEDEt_UdCc3t80nopULxPwqeJ_dNNQqsqCYlDnFTeBRrLLEC7lY1ilIPFUJq_TJowYZrbel_gAVgOeAgGkaAl0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲ مرداد ماه
۹ صفر ۱۴۴۸
۲۴ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/674720" target="_blank">📅 07:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674717">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyAifeHsiUsbM4tVZbSOwAddJi6di0LkLwhi01_bg52NJydmQv4P3k9INq1yqQimfqPEF3qPUW_hawyPRjEAYdGq4BAUJyMFX2EBCSammuxVDDMOhz7xlF2AP-q57KOrJr5oW0wlCFNqWu9Z2ZeUwnDL8HsUjZkqmfBagGxAX6PqWLLEKCFqmAywNBRjkkMNRqmvqaGdUOs0abSwurDlCGmrZmSoFBYtgVwN75EfgOJWV6ebKjDtERyzqQCkbDxGl_G9gCc6C48tjz0lO47I6INXtzMSK5roEsI5kHWKX37mfMXmdwUDSXdLdr4qUM0JNwEpiJPADXKNoXDBJ2fBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ عراقچی به تهدید جدید ترامپ: به محض اینکه دولت‌ها مصادره اموال دیگران را عادی‌سازی کنند، آنگاه دارایی‌های هیچ‌کس در امان نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/674717" target="_blank">📅 06:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60685601.mp4?token=Gq8Km0uudhCnLyXDwcGcfNgqq5nl3gQVHKVjkANAFytTRbFcvj8s5PlO4EY1CT5h1kMQGaD7DJDoEjs2zFlTvINzdowpUY_sIlX-elJJDeHnaFPns6u6QsnLBlxuIXMzHV3yuS56lV06xE-iwQYmXvaUl6p1mbjhoz7pk9FCahFGXxKF27Tdm3pHggjI6srA4QlCsZScM23tl9wHJ2csLDS-LeJemfrCE20fX-3h-qd9Mq-YLpSf05VBmA1YBeSTGZQQ_q2gO1pwTgXqR_5fibJ6Be2N_mW0EB_5mD6rSPuSrNGYorjob_lhfcsr8Iar-S7pZTBQpwKdBPQClQtb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60685601.mp4?token=Gq8Km0uudhCnLyXDwcGcfNgqq5nl3gQVHKVjkANAFytTRbFcvj8s5PlO4EY1CT5h1kMQGaD7DJDoEjs2zFlTvINzdowpUY_sIlX-elJJDeHnaFPns6u6QsnLBlxuIXMzHV3yuS56lV06xE-iwQYmXvaUl6p1mbjhoz7pk9FCahFGXxKF27Tdm3pHggjI6srA4QlCsZScM23tl9wHJ2csLDS-LeJemfrCE20fX-3h-qd9Mq-YLpSf05VBmA1YBeSTGZQQ_q2gO1pwTgXqR_5fibJ6Be2N_mW0EB_5mD6rSPuSrNGYorjob_lhfcsr8Iar-S7pZTBQpwKdBPQClQtb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از آسمان اردن در پی حمله موشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/674715" target="_blank">📅 06:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPvZa66GS8C65smRWFhg-zFzECkBRe89rBQ5ECR7ExEiNah3kB9m89BOZC4EwA18z0GIPFhZ_-7E7ltuDTyNlRj86qyS_R6mVZZ9VeyH48WM3EkW9I9uKbpvnSgT3MWklS5-qeqC1lVBiCRc3j67leO9ypyF57lthY4gGaDHsbY-bxj6VNsvapFSNkDeZDLdYId3rH_gR6MXvEgyrxOlw8ExAce3zpfS2eAA8Qa8mY_gfYTPtM7hm7RaEJ-ScoV9425Z5ttMjcApPISC-5r4PqYKwSjXeHcJJhveora6ywEXfj_wDW9UePGmN1qL_bKX7PMrxlh_gJ6JMfe5yS7UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش صفحه سفارت ایران در کوبا به تهدیدهای ترامپ با انتشار تصویر توئیت‌های او برروی دستمال توالت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/674713" target="_blank">📅 06:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
۴ شهید و ۵ مجروح در حمله موشکی ‌آمریکا به اطراف شهر اهواز
استانداری خوزستان:
🔹
پس از حمله موشکی دشمن تروریستی آمریکا به نقاطی در اطراف شهر اهواز ۴ نفر از هموطنانمان شهید و ۵ نفر دیگر مجروح‌ شدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/674709" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
