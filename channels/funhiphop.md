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
<img src="https://cdn4.telesco.pe/file/v0hZe25SdQvc3ExeX_cQFDLjjvyMlVkRW2xuD-QpV3MtXfPZbZITGBOb2WUTfYSP8hrevWFyn13F174I0xRwqOsx-9nzUCsfuyJoSuW6_RJvzErUdRbSYgRyvTRKqyapulg-f7lskrOZhE1mxcNw3Tuo0qqkDuboQrY2ircj6nfqSI33p91q5JlwuTiDVSjiGUERQHY1JgEJQ9pIhfmNu_3pGRV_vqAsYKem4GUB-SXJdA4LWZL5-JsHgJvEDRr0wwsFk_DJfQO45-kIvT7Ov5kzrLt11figKT9A5tyqCnbEQC39QQ_VarzSL9bQxkvl1Y7RMYlHydyYGkiy9ToOhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 246K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-83683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlTsOaxXvsFF0ENsb5AR4ib53JPTy7LKiuazRFZWc2laakZmUTgWRV20am2RzJmxRFk3n_vNM9slShNDSbjshvbVYAPX9qYab9GrmFTJxRN2vd8wgp7O-fXGosJvn1Wks4AeTTRJs5R8DnvppVrP30fRYFVs7xnr88udevPgt645t1dp0IU8j76zyelFIkfjSHSQTEHT7xlidzR660z_tsveFFFi1xnF4gKAs425XKYqtEglpfZv985pvh4PteN1Qm9M7RsPOib1TCpXstNpxeRcucKX-th6ampmq6XYcj4uxcGeHunm9KbzdNaUvWcUHKOzJfw7BR9dJZwddPuU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Yeat
📋
Title:
COCOON
🛑
Featured: Drake
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/funhiphop/83683" target="_blank">📅 10:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbwp8_yN54rQqaMtVUXPnfMgyy727wK7stxAxY5CcAChsCXHm3G3lp5IgPVmREUZhQ4fFGofpGxdLQuLc5RAPa_87yNCDKDPgkq4XA8E5ZwRwd4lsuD_GEJ0yvk5Z_5v7vGSgs_vb6Tw-yRxFaeuUxd9k5DzxFtpSOuB_l5lUmXTrqYXCx5uA-wTEt-wWkLU9ot_9GcZ5FUnnvjm4zV19bxCnHpZ9U2jqDoq4mxieIUaXnOCQ6g3ASpgf1WaFmqXqkN37HXrpVH73Yt-lkSxkh8a59TCJFnUcH5Bf9TFYiPfGBLMJvcxWoEWJMYBjvSeWD4kaUqiPIU5_noRL1yD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته آینده قراره به هیئت از ایران بره تو سازمان ملل تو یه نشست سالانه کنار هیئت کشورهای دیگه سخنرانی کنه.
آمریکا هم به چند نفر از مقامات بلند پایه که می‌خواستن برن ویزا نداده و الان هم آمریکا گفته که هیچ‌کس از این هیئت حق نداره از هتل خارج شه برا خودش آزادانه تو آمریکا خرید انجام بده!
معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران تحت سرکوب وحشیانه، کمبود آب و برق و افزایش شدید قیمت‌ها رنج می‌برند، مقامات رژیم قصد دارند به خرید و تفریح در نیویورک بپردازند. این اتفاق تحت نظارت ما نخواهد افتاد.
ما اجازه نخواهیم داد که مقامات رژیم ایران از مجمع عمومی سازمان ملل برای انجام خریدهای لوکس با هزینه رنج مردم ایران سوء استفاده کنند، در حالی که این رژیم ثروت ایران را به حمایت از عوامل تروریستی خود اختصاص می‌دهد.
ایالات متحده به ممنوعیت خرید اعضای ارشد مأموریت ایران در سازمان ملل، مقامات بازدیدکننده و خانواده‌هایشان از فروشگاه‌های عمده‌فروشی یا کالاهای لوکس در این کشور ادامه خواهد داد.
به فروشندگان منطقه نیویورک: هوشیار باشید و در این تخلفات سهیم نشوید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/83682" target="_blank">📅 08:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jODj7PPgHzUWxI5_M-q9lnwqxUwp0RolFmbDe2UXYabKxy8XcizxBClMfgRPa-7f8E4An6hfQvM3pbIPCIcbrFniyAY7Lr7234nwNM_5VNIiNSHA_7xg5UBan0Q0zlxNG6hkgzk7s44Il15NulPa_1V7u8oDCkKXsbNtfb69UjQJhjmToZl0J2XyLD7Adrcm8J71YdqaIOLaJCvRP_jIZNV3W0ar_MPze6AGj34hW4amz4fuvUcEKtkX3Ou6zXWTkpPoXhM0I2m3ICJtpVO44Gf2gAji7WgNJBtmfXIrrpniNx-pD7yCrVANHPbawdXxj0WIDleoekPOwqKfLG38_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام عزیزان صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/83681" target="_blank">📅 07:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOIF1T14p3mne8py7Qc7RkCSKecGR0t4ERDzKCX9jwji2GO1GZ7Vqd9Xlsn__hynHzIsBoUKzgMVMWz0gO-j9WYsDRdRRNp0V7G7bndtR_Wz6kCmQxm_D5NLG3_xPgwQMsC0rrwuZNrY7yiRJG7Z7-hMAACghrGub38wc7lz-1YcwTo4KC7PHxxOXckRqGqZDYa3jAvhI8TO6fzm0tHbFse-6q3adEV6QRanHAODbwY4CLXeiuys5YuZHu4FPaEE4O0doZdceR6RUaLkDmVx-vrHIDFwRHTigw9KmY7u6GZeimGZIPWFAnfrHqPQxgZ-h7sfEzX32aHy00cJZxf2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش اینجوریه که بعد از ۵ ساعت بحث می‌گه نه آخه می‌دونی از چی حرصم می‌گیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/83679" target="_blank">📅 05:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us2jyeTellHA6OEFRiIEprGKWgWDG0fx_vyu9YpQRejIIAlIAwb7ryW2sqLEs7GEAo7WT5qFj-UplpYYHm6X8EbyhuBSaqmw3WhmDv-fb-tZ79cIe7OISI4kw2NUJbVlyVHgXqu-qzLGi5GoQiND2jQd964Oyz35dOI2AQZSEhx-g7FZOnZtmjD9s-DYRWUBDEF4CoSMWjCexw572ZyvUlfXB7xdOjYr-fn6y0t8hfw2vhctM1Ntkyf_NkW6gfF2Ra1uoJYF45yVGSWb33dLh2tYwRpHdt0a6LXZki8EL2i1CA9mP0X56s2le3zQwCcETB2h_WXeezhRWspKGCrKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه.
تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان تبریک و تهنیت عرض می‌کند به امید موفقیت‌های بسیار بزرگ و روز افزون در پناه حق استوار و مانا باشید.
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/funhiphop/83678" target="_blank">📅 04:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از اون فاجعه اسکم استارلینکا، فقط چنین معجزه‌ی دور از ذهن و عجیب غریبی از طرف دوتا از بزرگ‌ترین رپرای مارکت (کوروش و آرتا) می‌تونست یکم محبوبیت پوتک خدا زده رو دوباره بالا بیاره که خب نمی‌دونم چرا ولی انجامش دادن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/83677" target="_blank">📅 04:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfRwc9Pkfj23aVyLwPogzX4SN1OjOe6cGVAW8i8QsHCaa7UhfCVLlpTwzQ89CRYItOk-bfMWhMxktAkRcTSVAGcZ_Aq5qE_cIzb3dAa8513SYIYgBi9QQzlmNO1Ayh-q05S284jriUyPNWon9dyWIKmfHmY2lIcJUEEj7TDWdx8ehElR66mRVBGMAv9rvp0Zq3KbL8DMEhmuobGsqmmz-oeIkE1iYJMQFpM6V1dunX1WhtvkPMeCHeC1KUBjM54HhV0oDnvb-viAaE9Lj6WcdgLgLgYA5QLFuWJW5iJLtM2FGgcYul0UUlC3br6sKEL3hCBZ_QqXT6KPBlvs2LwnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک در جواب این همه ویس و ادعاهای مطرح شده، فقط این عکسو از آمار یوتیوبش گذاشت چنلش
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/83676" target="_blank">📅 04:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVQcs-pELhVW9r4GrxrTtV2fzS4Tzm-ymCJ-w-vr6CxYk40FyG57LvAXL4_o0Paa6ax4b7RYPnh32XR4yV7noxA1JLMjOEwkaIBN7afkFylvhsICaLEtTMS-8SDFrB5Iu5WvQXdZ1mDytDTVqZp2TLD52IJsHl4dP5M-vdAzrCc5w4HlqZIxUiNjCqv686_etSb0jsGxunFRFbCKCBp53_qPPh7pIIHfSpKp4n6fktfPJEHnuioufPLOMGy3rkX3SBRSbyBQPdZOLovaym3N36QcweID8KmHjC7UfJSHNrlTV7BHzEREcLjbsaEgLWn6LM3iFPMEuwTYCuCIzuyDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو فکر کنم هر کلمه رو یک پانچ در نظر میگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/83675" target="_blank">📅 04:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">داستان ادعایی کوروش وانتونز از نحوه تولد دختر و پسر پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/83674" target="_blank">📅 04:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=Qr8HoP5Np65AO_njBjXQPeiPAkUlJC-vm2W_YRQdaemiRNXK93RNUo8GOmXlXfHTE5gmNAaUuFNoZfbx1vN91ktOEV3zkb1BXCrv3NPelwuxEriJ9kDX3WeSa1yq-aNfo1kIrJzRkhJEKZmAWTggigJ_EAS9sippI8BOfFZ-J_LIjgYu0kVnawvSpvKpX2eOuMOYVieFlpzdnvFF-XAKyKTepfUJba9svIW5JOVopTkT1AERgyIK85J6LpWpdflMS5K_5IRCVAI00JHxbOf6eCsCzPBtl5XEHi8ppjmS7MOBfSzY192nzN0ALK1BM_Pc-P4akzRe4OvaCSABuSzVqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=Qr8HoP5Np65AO_njBjXQPeiPAkUlJC-vm2W_YRQdaemiRNXK93RNUo8GOmXlXfHTE5gmNAaUuFNoZfbx1vN91ktOEV3zkb1BXCrv3NPelwuxEriJ9kDX3WeSa1yq-aNfo1kIrJzRkhJEKZmAWTggigJ_EAS9sippI8BOfFZ-J_LIjgYu0kVnawvSpvKpX2eOuMOYVieFlpzdnvFF-XAKyKTepfUJba9svIW5JOVopTkT1AERgyIK85J6LpWpdflMS5K_5IRCVAI00JHxbOf6eCsCzPBtl5XEHi8ppjmS7MOBfSzY192nzN0ALK1BM_Pc-P4akzRe4OvaCSABuSzVqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند عدد از افشاگری‌های کوروش درمورد پوریا در این موسیقی: منیجر پوریا وصل است. پوریا با اکس منیجرش لب گرفته است. حق فیت حصین رحمتی ۵۰ هزار دلار است اما پوریا این پول را نداشته است. پوریا موادهای مخدرش را زیر تخت ریچ (پسرش) جاساز کرده است. پوریا به عمد همسر…</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/83673" target="_blank">📅 04:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=HpLfkNN4G3BDqjVC3K7frZ6EzoDtH497yKO0jsy9oTp2taKxrI1dBFR_jor8Z3MGe0An--m2Znpcqgh38B05WKkZBwN457pP_PHjWBxmW3LbDJvVBn7ECH5uhwHDBfv2IsZCc0_L5TY7y2UpTPasamfDxfVIa5TA2Dw4m94qUXK_c2L28XlYQuiT0eFDrkH51t6EQCiwEeUYerbo78s8jT3cFqhSan16pgZikZsTa5V-PC00Q4HJUiEjqSyVDXXEiKdMIaNDYtTQ0HLtjgSE_V9v3_oWe4g3nCtknsmtgU5_t1OhJnMGlPv1Lx6J1GQDSWW25yuHb6lPufq_etq4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=HpLfkNN4G3BDqjVC3K7frZ6EzoDtH497yKO0jsy9oTp2taKxrI1dBFR_jor8Z3MGe0An--m2Znpcqgh38B05WKkZBwN457pP_PHjWBxmW3LbDJvVBn7ECH5uhwHDBfv2IsZCc0_L5TY7y2UpTPasamfDxfVIa5TA2Dw4m94qUXK_c2L28XlYQuiT0eFDrkH51t6EQCiwEeUYerbo78s8jT3cFqhSan16pgZikZsTa5V-PC00Q4HJUiEjqSyVDXXEiKdMIaNDYtTQ0HLtjgSE_V9v3_oWe4g3nCtknsmtgU5_t1OhJnMGlPv1Lx6J1GQDSWW25yuHb6lPufq_etq4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب شب خنده داری شده پسر مدعیان حامی حقوق زنان و زن زندگی آزادی دارن زنو بچه همو تو یه درگیری رپی میگان</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/83672" target="_blank">📅 03:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کوروش چرا به این اشاره نمیکنی که پوتک نسل دویی‌عه و اصلا نسل سه‌ای نیست و چون تو خودش ندید با فدایی و سورنا رقابت کنه خودشو شاهِ نسل سه جا زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/83671" target="_blank">📅 03:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کوروش وانتونز ادعا کرد زن پوریا پوتک سابقا رقصنده میله یا استریپر بوده و در ادامه برای دفاع از اعمال خود این حرف‌ها را زد:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/83670" target="_blank">📅 03:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83669">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrpB-fLQRyqKxZr3RZKngKEevRJ4Pq0C962bYm-h39S3SLdsJkqgNlrKSkjmIDzPBGbYMhIIogwaFLkkUyES6ZhuuTmfn784APh-t_vt6bX_VAJBtXPmGIdLnWD1uRAEb1hZUtbsDotr2602G6DxDG0zekCtjyYW5aRElR-eVshzPDRJQQTDt0Gwh_9niN2VjW81ebUj0tZnb4z0UcnNIR3mvQ-SctNBfp72hJumBYKUxYmNYEg2EhLvFFg4K0uG25trELG1uU83FiTHhSqOp3T4G0bHXep5YSkry83lMtf4Ua4K9LvS4arYymBmuxzju-iIWGE8WHEN1MMHP4cheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا باباش ارتاس جون ناموست برو بخواب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/83669" target="_blank">📅 03:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83668">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/83668" target="_blank">📅 03:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83667">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_5tYFzZxyosTbrIM4LObhY_dtH2OW9UJGU2fCn3LGaZJsiULwoTDDmEOVvpckbr6TDosGmKAmFCZ72N_rQyuL7Zstfi0ZQWtAV29w19-Pko-sAEE79Her-HpH_x2ZyhwjmpU6eQYlkWYUNxmadh5GcQCPTVgQcQ-NuJmPjgjGH-LNZTp6JZrCUOxkDMIW0XrbCxh9wTkdwk4Daf7chXgnJ3Kuj7NUalalHQ6G8Xc8BWndgfsJG6Ex0XVZAQHCR8AU029Ol4DDsiSWAJJ3hD74-3xSa-AMeGdQpf2A7B4OaDbUz0Q36uXNCQKynHJhXBOq6qpr6823lszbniPxqthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/83667" target="_blank">📅 03:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83666">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گنده لات یک مدرسه رو نگاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/83666" target="_blank">📅 03:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1G9MGo-MjS6tmORp9spj8oPMjn-rMJ8bOwXHnVhbbyxg0fGRs4frGctpEY5p1853dct2eL4CS-_-nnKezKGaL-YlUEc5iIviRQHa9JneX-pJKgAuqnQXdGvo7i3CWCfH8Sd7mHATPn91AsVwjN5M5jFRalehviy5sDSt_4zBsAltRtk3htzlyGwalh0AaG4DcDAa6R3wDjoCDQ7IEoYuRZN2_FwARdRniuFfpvUVY70fTfFqDsQ6KfOpkOjfia5yWepPaOAkQ_IykJY0IAA_agzF1g-vEhJ3npQB424N-UHQtyPJAWRlJI2cFme4mgbg-KF9DvGRld8_c6mQbtgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L75R7N7-7WtpzLT-9E8dLFk-ip9ch4ZozwjOW997ky5ozTapL8KLZhoiuQxynAP9sldB6EY7XdpEgKS5lP1b9BP7FuqcXNnWzDlHKthibWFioGRGq4RPmJeAijIFSrEy72GKyawuaYKHbcqFDz67tBhETn_Q1ybCReTqluOZJZBcUKtWZc3rl3BNH2OeJBSEfNwPRm7c9POC_8nxftxyf3AsHkT4-dTwCebWbWiB3Hdqr5fqVbAIWuwreyVEbm_gBI97bNOhXJPYZgqWmI_6wDNHwqg5l9l8Lu67Bk8BlDRIxMsSi76Kb5-BVs5nQAXEcGABfMorEygnbaJRTtCqGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوروش واقعا رد داده
رفته با گوگل ترنسلیت یه طومار فحش به اوکراینی ترجمه کرده به دایرکت پیج دختر پوتک فرستاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/83664" target="_blank">📅 03:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حالا خوبه دیس پوتک ضعیف بود که این دو تا اینجوری ولکن نیستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/83663" target="_blank">📅 03:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awPVIchozHOCDDEvQI4J-UpFajSiEQA8yNUwptX7nB68C7Iq-i1Vae088Xpg-6OCxPnC4r_cR1IFcnKrPtBgDmn186JezhD2iRN3slaJCDpzPNdzqtg6bY2PkOveIw7xspHE76Si1skawqB0IDXfaWHlV27Xsx67KCZ-d3PSP6nF4cOiYW3MGkltu1MHZZ5uGX45OAHtqOPSrdWNwfLEKAmOLacIGC_2JeLuLWRJM3mWQqbpySxM4VC3o866uvBOPFBA7njpFNkJMGhfjxDSDLGBvx8XKfDo76Tsc_B0pl1bUri9a707z_o6ifjwNocMUu3H46T1yf8yoPixgTzzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان من چیزی به ذهنم نرسید راجبش بگم شما خودتون نظر بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/83662" target="_blank">📅 03:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نه دیگه نشد داری زیاده روی می‌کنی.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/83661" target="_blank">📅 03:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جدی یکی از خنده دار ترین بیف ها(بعد از بیف شایان رگ و آدرویت) بیف پوتک و وانتونزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/83660" target="_blank">📅 03:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">میگم چرا همش بگ میپوشه، تو شلوار های عادی جا نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83657" target="_blank">📅 02:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83656">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArta</strong></div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83656" target="_blank">📅 02:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83655">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83655" target="_blank">📅 02:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کوروش: من مثل توی مادرجنده نیستم ناموسی بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83653" target="_blank">📅 01:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تو همون دوران وعده وعید های پوتک، کوروش هم موزیک سیاسی میخوند میفروخت به رادیو جوان
خلاصه کون هردو گوهیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83652" target="_blank">📅 01:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">استارلینکا رفت تو کون کوروش
مگه وظیفه یارو بوده بده</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83651" target="_blank">📅 01:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کوروش: استارلینکا سابات چیشد
پوتک: مادرت جندس دافت جندس به دوس دخترت خیانت کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83650" target="_blank">📅 01:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کوروش جان قصد دخالت ندارما ولی این که اوایل ریلیز ترک لایک رو بیشتر از ویو نشون میده باگ یوتوبه که وقتی اتفاق میفته که حجم زیادی آدم هجوم میارن برا گوش دادن اون موزیک یا دیدن اون ویدیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83649" target="_blank">📅 01:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbRp-I_Qt6pkjC0zQQ3cxG5Na-OX1hiBj1uInIeYTZwYMVMoWpV05aqSfrptg4_D8gkTWGCBKzaU1wDL4NvxiHPTuaH4Y8s8mkPva_b48_aaF2xGkPwtLZQ2SNBoZmoHmfdu7glxAFUmw0rUJafyPxG9Trz_oYZgOYpuxY4Te53n-kP0Ru2T7YTZMHfsMHv2v9IiS4NHZT0Bk1rBHItPOpdD1ScfLsExJVTUj59rlNwpOE-3roE_nD3WPkapMtTo5nhI1CR5JyYB5515RDUBvo8p2GrOrZCoNE7qWJ8--X1Z_kROc09UAbY0HmKbuiEfqMsE2yZwtmCCbhmlRbngOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83648" target="_blank">📅 01:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آقا کوروش یک گنده لاتا مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83647" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83646" target="_blank">📅 01:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب دیگه بسه خیلی حال داد حالا وقتشه طبق عادت بگیم از بیف ملتفت با تعداد کثیری از خواننده ها رسیدیم به بیفِ کیا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83645" target="_blank">📅 00:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNYNblqZEqZPsAl_uOR2h8Zps_qpjcOBzj5izUzhptk94GkGmxdj_hD1aQokpLrsHZirIayOfhlgrK2QOPMZzRytAYVl4O00_SjY6Q8-D-YfderUic8ZzeukZXpZX0UFgo6r8u4og5IknVFMM0M-7YJ5a8Ju98FFW_w9rukI_R_rAGy4_AnHqIvWB3c9rpq6Q4TGTuO8vsEFbPk7KDzy6MI0vQhis34ZAdg6-sVRrruh_IoUhOYkXOot417vjTOLwWbwIrmi-4VrLzRdIeik9Q_IoEvnbp499xw8pUHK0jzoLWGEbDXi294X4ufN0HbJ2fNTG83RxBqByodRYlngMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زودتر از ما گوش داد ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83644" target="_blank">📅 00:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-poll">
<h4>📊 تا اینجا کی</h4>
<ul>
<li>✓ وانتونز با دوستای فرز و شیطونش</li>
<li>✓ پوتک با ریچِ کصکش گو</li>
</ul>
</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83643" target="_blank">📅 00:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عاشق کصکش گفتن ریچ شدم حاجی</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83642" target="_blank">📅 00:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83641" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83640" target="_blank">📅 00:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83639" target="_blank">📅 00:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آقا اینطور که بوش میاد کوروش به هلیا خیانت کرده</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83638" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83637" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83636" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بچه کونی اینهمه مدت بلد بودی همچین چیزی بخونی و ده سال کصشر به خورد گوش ما دادی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83635" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83633" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVC8v9__T4vH-XHsFvr0tRhKRqWYz96MmtCFh83jrSTcCPe4QEVfwYP8UPDolT3-ZKghSOcPHTWQlxg1eJsup9AYa2t0J2Kj5yDzlj4AIF4_Hr5-5Bd1s_NNwErt6lHNnM1fFl12hIa8FoSILpOZTCizi-xtOTfpDfMjW8OcCdAkjVoHEndPjKmBtGPv5WE-wY9eigJX5naqd238kL11zYZ7aV541oe-wOihdX-gMd5_lWDAh-0ykLiTeLBvZLGrZVTE7Yms3loi5ek-0xDTt2CVYKhqs6OFbTGOR1_6S_0nKZ6aqq3Cuj1Pk6ZI4dj0oI4dbggL7fA-NCSM93b0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد
YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83632" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ریدم چرا اسمش هلیاعه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83630" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پوتک دیس داد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83629" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoC0DuzCtLj3qZFp1lm-87-YI9L-9Xvj6At02iTmpAC_baenlM84746A_tzRyXZ8Eo3kmku1IhAJ7jLkVfBfBL8GIy8X4C6-L5rWf3P6fliJ-Kb_jP05cpgfNQhOnjDNgQpCRYfyJksUFvlCBPgmpjrhGe62QAHa2B9Tibl2CIl0VHXa-Ydb36NUjxu8tlsp4otHZr-X34tChmPlsvlfCYvpJubeLPVCLXNkTwcggQrkQ3zmBLvDk3OM8Q-l8A7DTBZuf9g7ue5dYryl0cEKM_AqGhNX53dwAc1O9Qve-VV-RZWbJfJilVb9_rVLUwVKQuH0DmpSETlSlNe240A3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک: داف زدم روی داف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83628" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شب زیباتون بخیر عزیزان
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83624" target="_blank">📅 22:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کیرگوزی سمی لو کم بود فقط.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83623" target="_blank">📅 21:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حالا که جوش خوابیده میخوام با یه حقیقتی روبروتون کنم، بابای من کلا یدونه خواهر داره و اصلا داداشی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83622" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پوتک ترکتو بده بالا میخوام برم بیرون</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83621" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">محمد باقر ذوالقدر، مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83620" target="_blank">📅 20:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینایی که تو اینستا میگن "من از این نسل نیستم" منتظرن جایزه کیر طلایی بدیم بهشون؟ خب بکیرم نیستی کصکش به ما چه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83619" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هیئت حقیقت یاب سازمان ملل:
آمریکا تو حملات به میناب و لامرد، مرتکب "جنایت جنگی" شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83618" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMZ2dQSYTZc4sNSdzKPSz-EukmsD-NinixpCas1yLlT0IcnPiVGFmXnreJRE1bPOnZ0W9jAgHY-jm1i_FfyOygwtborzi_73W9iPQdYfYDUjdb-tk2-4YSkLVwMGR5o5-VXwMWVlC2TD3gh9xVnBhK8wdiXvfi-9SppSXCvwcUgdF14X66-KKxQbQuqtv6y7caJT0gKzepkKuRX9do-HrO_0v5KQK7Fq2OV1mVpaK-kQnxATT2R6Jf3ukWNRXvpygPKebHSoSl24Kd1fYHiGAnxL4hK5eBxzjG8g0XhuH69tIA21DMbWNelUG7q7lbPa6JemPcToCzA3ImfpIf2f6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی والیبال قطر یه دریافت کننده ۱۳ ساله داره که ۲۱۰ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83617" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این نزول خورا چرا ورشکست نمیشن حاجی هرجور حساب میکنم تو ضررن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83616" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">موزیک جدید ویناک بنام تارانتولا ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83615" target="_blank">📅 18:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f2ff6c50.mp4?token=rWiP6fciRUTlsA8EN2CN8QzzxhWzs1HVe9gqlTWvKBCC_C3W07AAuGJFGaPZ_dz_aNjcgsHPrAcwbuZhR9Vodo3EfyGTTko2yNWkuJv24fQKHWbvaEQSBH23OjnQNsJel4kMaddC6ii26rHsokYJbm-c26KALQg8_ub5zI0e1QnOmVAHf0kMPRSxEpZcZOwfgAU4mxPuXQNZU7Lm2I2DkAGAZupXIDi2bda3u48WrjFRg3523gBHpsbe_MDhLWgfXUlx1KXMi323Zl7xYJFrGhbUKBs0oODl0OyVYPsGP3ljIeoP-7Nco9Befjws8i4zzGmnqK-o3GZLOE4hgCWSMR7oNc48Q8Nj_EyS3q7RB_vuMy6zC9yN06C8rK7l4EL-VDVEeVHONtmAXNms__1aV9WY1w5acLJb9m-n4vVbBNSVNHsSpf1zdQ6tRI-lfEKf2NvJAHk1ZkIwTTasAQtaAcK5DpmT_0_75aE-aoUb-91G1W1bCUF5FVTJqJQYe1fzvuny374GJlkBq3RSpinghnqh5bgQgnTM7HfSl_JPCsJb-q4kr6Z6Ah1e8Rp8ncHkZ6XYQmRuwnJQnNdMZmkOByvHepE36Ju5iBcUwhNAstJfLq5nOu9TFFNF3K9b6t4i8lZJJVIsWiYhM88R2vRvk3sF_iC8bvTC6kUBXRKJzt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f2ff6c50.mp4?token=rWiP6fciRUTlsA8EN2CN8QzzxhWzs1HVe9gqlTWvKBCC_C3W07AAuGJFGaPZ_dz_aNjcgsHPrAcwbuZhR9Vodo3EfyGTTko2yNWkuJv24fQKHWbvaEQSBH23OjnQNsJel4kMaddC6ii26rHsokYJbm-c26KALQg8_ub5zI0e1QnOmVAHf0kMPRSxEpZcZOwfgAU4mxPuXQNZU7Lm2I2DkAGAZupXIDi2bda3u48WrjFRg3523gBHpsbe_MDhLWgfXUlx1KXMi323Zl7xYJFrGhbUKBs0oODl0OyVYPsGP3ljIeoP-7Nco9Befjws8i4zzGmnqK-o3GZLOE4hgCWSMR7oNc48Q8Nj_EyS3q7RB_vuMy6zC9yN06C8rK7l4EL-VDVEeVHONtmAXNms__1aV9WY1w5acLJb9m-n4vVbBNSVNHsSpf1zdQ6tRI-lfEKf2NvJAHk1ZkIwTTasAQtaAcK5DpmT_0_75aE-aoUb-91G1W1bCUF5FVTJqJQYe1fzvuny374GJlkBq3RSpinghnqh5bgQgnTM7HfSl_JPCsJb-q4kr6Z6Ah1e8Rp8ncHkZ6XYQmRuwnJQnNdMZmkOByvHepE36Ju5iBcUwhNAstJfLq5nOu9TFFNF3K9b6t4i8lZJJVIsWiYhM88R2vRvk3sF_iC8bvTC6kUBXRKJzt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک جدید ویناک بنام تارانتولا ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83614" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF-pcHQdMrBF5QkSkACbM-ekUSRW6Imhi9UamS5aFg0SMJKejjnbBsiPCrk9V4c-myXdWL4DIQgsXpmKCOKftJP4UTjMIODewy0FusREiTl5ul93Ydf9IKbBjXXAM5M5kqisu9ecuWMdqk9BWW7xV4y_GnaGdE4wMe0SudN3u-Jdcm0vvk_xcmDgmRHmMejIKFn66nV5Nu0vImsqNf2PofAGMjOsOmybRKgzl8Y0gFR16YRi_DmRnhsxdS1SDKEz7v-eGlmBDoxjTjrHy381x5y8wO6ZGzP65eKft3Cf12nxmdUkfGknjBG7X67vG8vFP7SYhtr6T7iUqlESzPSS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
رئال سوسیداد - بورنموث
⏰
ساعت ۲۲:۳۰
🌎
📲
یوونتوس - ان ای سی نایمخن
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R26
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83613" target="_blank">📅 18:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2mPugfMhUeZ_SBlIEQ1MeC-9mi_AijgRFJUqET_g7VVVSWDm0-qp6IIBNKpRdr0q4AbPD1VQie-bl_4e-5_bwnvgzfkujD2l7v0MBhenelN2BSbICwNnn-VMbsYL851L3nAKuw-_2YcvQC4bGFVNJFn-crg6gHVMp3dez8z5v9kKL9IRRXj92FJy-mK-t_EMGlPqpOfarqKyIyWDNDe4TPPVv5XmOjVUQtWdmmJZ-Sm4a7Xbq6JpRrEX_4B87fTeuISWAc9veJVmz96T8J3Fxd7omARDiDnzmJdT_tUSOSgW3mCEqnf1xWNgMwsZqTKSHLlEPD0NUWB7npRvt-ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایع بازا به محسن پیام بدید برا جیبتون پلن داریو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83612" target="_blank">📅 18:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=ocyCjYBHDDKV5I7WUaEFRCTnkHRkVZ_CHUgSPQlYTAWT5I-l_cYMz9GZH6Ys0KiLLmkBtmVT1f8CdhU_OY-O-D3Zu3mrjpeIF3y9WjvzuycmY0R_Pa4d6YVOwcSi43kDWizozL9sxa4_G-Gd4mVM4pSCmFoick3FAttvdaj_8GJw1o7A9u-U2aZqjXV6f6Nrn-Qiaz74NmFdLu3tmdI3hf31b5KeyTCrgb8zEHnrpupEKEgv7wu5a9O_0Zlj2vcZqgF6_CDyQRMUpemLl95Q2XjCS3RMRTOARJ2MTds8PaFo1UF3jGEIK_E5I1xXemcVG_W6Ee5CXJD7rFiDAKNujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=ocyCjYBHDDKV5I7WUaEFRCTnkHRkVZ_CHUgSPQlYTAWT5I-l_cYMz9GZH6Ys0KiLLmkBtmVT1f8CdhU_OY-O-D3Zu3mrjpeIF3y9WjvzuycmY0R_Pa4d6YVOwcSi43kDWizozL9sxa4_G-Gd4mVM4pSCmFoick3FAttvdaj_8GJw1o7A9u-U2aZqjXV6f6Nrn-Qiaz74NmFdLu3tmdI3hf31b5KeyTCrgb8zEHnrpupEKEgv7wu5a9O_0Zlj2vcZqgF6_CDyQRMUpemLl95Q2XjCS3RMRTOARJ2MTds8PaFo1UF3jGEIK_E5I1xXemcVG_W6Ee5CXJD7rFiDAKNujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشکل ژنتیکیه فکر کنم حاجی زود قضاوت کردیم
پ‌ن: داداش علی گرامیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83611" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83610" target="_blank">📅 17:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83608">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83608" target="_blank">📅 17:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83607">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tITBcwkphnLq5lfxbOpt9cs_DEBN1ZLfCfPgGzYv9q2DhdDJIqbPSxJU7oyu4KXoCuXwzYdX9Hf7J9M7yjCmkYHMAXybF2OVPt2f3F32FdEsfaq2a5cM7uocdMNcASyw3BCiOZfxb2v2GqvyrVhxMKy5pwBlEESVLtbg40egTMTgRlBkbqmK_qNnxjNWUPOK_j3W5XLDY4C6ZMxiKbmLsNxu2QksV_WCrzjdmc_vMTCiza5vYhcvNWFOC_PpWDTyycl0yCgDg1Mblg5rimUkBLuu-1Q0-bmIvLBTn9oNV0jBegJsTECUes1gF_tHeq4AAFOu7GS4e41VEGmE0tZi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewReleased
🆕
🗣
Artist: Young Lean & Metro Boomin & Future & Travis Scott & Mogan Wallen &…..
📋
Title: GTA VI
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83607" target="_blank">📅 16:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📶
منبع کانفیگ های رایگان
📶
🎁
هرروز کانفیگ رایگان میزارن
🎁
جوین شو عشق و حال کن
⬇️
⬇️
🕺
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83606" target="_blank">📅 16:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=e-0Bq6sy8AS3VYW6Y3A3EV0Sm3evGyULBRjjYZS1hHux84qJH48I6c4yNuyjorifrP_OLAWHLQ_LMONXJddMByQHkiG_O0ULSj0Ldc59T1quDaO-DNOCSD6q6E_uvn1TkGYsQluBw1yQOURSGP_ictVFKFKh9ny57sPIbie-W0wlGtuAPsVkml32Fk03_hhV3_ZmBU5Q8qS07fWXdMPKgSIBTXInNM_4H2cBncFxFqNFcXe3ZVb6FC7xy1yQfZTlMIig1IetT1398bb-eYVsa23075e3DP0Ah0XrITGyIb0bdE8gz0tQCU-quvUYrbkve5gkUsBMd0Soy2eNzShaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=e-0Bq6sy8AS3VYW6Y3A3EV0Sm3evGyULBRjjYZS1hHux84qJH48I6c4yNuyjorifrP_OLAWHLQ_LMONXJddMByQHkiG_O0ULSj0Ldc59T1quDaO-DNOCSD6q6E_uvn1TkGYsQluBw1yQOURSGP_ictVFKFKh9ny57sPIbie-W0wlGtuAPsVkml32Fk03_hhV3_ZmBU5Q8qS07fWXdMPKgSIBTXInNM_4H2cBncFxFqNFcXe3ZVb6FC7xy1yQfZTlMIig1IetT1398bb-eYVsa23075e3DP0Ah0XrITGyIb0bdE8gz0tQCU-quvUYrbkve5gkUsBMd0Soy2eNzShaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83600" target="_blank">📅 15:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=AQo1FaBnVUdZ2uYU_q3FrDxGXV46N-4T0Ft6yCFCaPY1aTKWol_QgQeJCkXi5YXrwHm2W8yclf9mYxvkD4jtclOq2yqVl7pAm4Z5BdErKvcbwdGA7PJdB42eUagy0hDV4bCk3bsiAuLWDtYcRlVvGEbOg5nMSDFAswzNElz2JNzJAK1CN_4_7FGsb--uE4BFDlLi8pXOqDFkQJ5DaUei_UqcjPf1lfWj83u8XvdGOYgXqvyqWSC2nkRX3CuAxczW1dUFwiAF7sst5nf54EqUDgXcqb7GNIyQSuiuTqm_vD5IrOzINLIJvZOkEKuyJvPYaLn6DwDaxqFv_Wlx_l6ZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=AQo1FaBnVUdZ2uYU_q3FrDxGXV46N-4T0Ft6yCFCaPY1aTKWol_QgQeJCkXi5YXrwHm2W8yclf9mYxvkD4jtclOq2yqVl7pAm4Z5BdErKvcbwdGA7PJdB42eUagy0hDV4bCk3bsiAuLWDtYcRlVvGEbOg5nMSDFAswzNElz2JNzJAK1CN_4_7FGsb--uE4BFDlLi8pXOqDFkQJ5DaUei_UqcjPf1lfWj83u8XvdGOYgXqvyqWSC2nkRX3CuAxczW1dUFwiAF7sst5nf54EqUDgXcqb7GNIyQSuiuTqm_vD5IrOzINLIJvZOkEKuyJvPYaLn6DwDaxqFv_Wlx_l6ZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83599" target="_blank">📅 15:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyIR0SdYgF92ReTZB_VpWBRnM1TDxPxLGqtZgfWmtqrTi3r6abruDJ0DmIPccN_MMKr61YhRavUjdlQKTk2HKjozcUotDxLzFWnQJuRQYeI5mDfH7Jko_CjLA5jH4PAuQUITUBMzqpC__QbMOQC__idehfte_TzihhWxowBrwkU_qhshNTE2bGfLVkimKicuXAye7lS9sot6rEouljkCArtrA7eyECx8iFvVh2Mk6J1BE_W9m6PaTebGiRvan6klI46sRPFZzlgp1Br_Y-Xui-KAfjOO_venWbWzVIiNNdfTiuKQOY2YpvsVIfzd4Ku_8CKUk1psJMkl3SKj_3IE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ts2Qlnl8RD8n_EWMXVkhTg1hTdpywh0LD_2w5Ul2DAOC8T2IJQ7fy5GxnPA_MAJDbIFNrN7A6l2UaNJvxYhsbFxXzK3ik1RPg-b2K-lBo3-tiISz03tPsxc8k4e-LXi7eOD4fKu9XRodqJeHyIjZEV4AmrblxTUWxzGZcUnDVLgmuvFyq57uIpDeGvWCJvfwvJtFV063F4a1MF8ydCTzafHWlCig85PlV6gWF-0OBV-3_0-pnxkAmittZKUMSG0oTBeTQ3XEek1sqw_LqWzNYTfP8b3Qy5Vg7CgtI4Ksn3VhM1-Mhc7Prah1nrX-iZfvqsNGxmNWGq1cvx-Vtdkm_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استر و پارتنرش تو فیلم جدیدش کم مونده دیگه برا مارکتینگ فیلم جدیدشون پورن بدن ییرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83597" target="_blank">📅 12:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqh7XleFP8FZdDRKPFQSw31bb1P-R7yCgBESAgHRp8UBYQqpNtU9CgFT-ucyprUt8k-7fwYI7JqwsecNf-bpV2Wz_39ytdFK6MhVJ6ZjOX2SoehHlGmgc9e0PKKnMHK4QZ7sh4YmJ3bNeB3L_EgAUkpRojJ5c-hUCcqQQpnWHwUDKqyUVOrR2PTztGZYIQS16nFN3HBmJ_kg85EJCFhlCa6X3MAmCDnGMMPLLbUv04aNk0I_ynNxCxCYHMhhf362e_7y670GizUq5XE2CbwJRxkrm13s3e-M4yM_5YVV-tIqxRfYR62lSsXgQVPE8ZB7w7Q_h_BRlaAvQO87KE6QDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی رضا پیشرو از ویناک نپرسیده واقعا صورتی بود یا نه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83596" target="_blank">📅 12:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNEcZmoTaXl8X1IWyty3D9IwbsiJAmQgmfHwrtg6Z0j4L6ITyZXCHqN8xcMP0cSNcB8lmg53PKJ6Jeq8OoRraF5ze54V8qYPQOohqXDuwiOC0Y8BpSdQDs5FNWEQXG8puiRMB8jiKwXc2hwT53tK9pYkvo4bvvEQeAJj5P96E0f59nl1Rr_9RR4TTMgwrQ_WwWx8c_4VR9HamS32JFoKmAt7SPvJ9wiLV6zWhWCizzIQh1ymJ3vZu76XS-2hZYUU3SeFeORvC0b4UZ_2oBHIyheLJBwNtiIjOLfsV2nhoBTvC6sagBRtfmPaMQcb8eF1T-Px4OHnInJyXpQhdY-iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیگر ترک پیشکسوت که قطعا بچگیاتون تو ماهواره دیدینش هم به جمع فوت فتیشا پیوست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83595" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esd5bjyIhLZcZ1J_DJjH8YS2ybQCBWlFfDOKyElBm-CIRIt3rMzH2EMe6eNLC2gticYVZDKumbxRhMv3I9_RSTffHMWh8ue1HvVsqzUdaIneldytDxXcwLNH6hcqB8FHLzJfLmUYBInWjjZIff7te7fQf6nVCXqesx4YVka5-ZRjjrD5vWj3LuGngiSUneLgcmzFH5KE9JDvpKI1OrWKRoCoJooWB9n4VM7Zx8hLKiL8sdGe6bXmTCJG1CkZF6WjjFlthGwt727o_hV407PHsEg6Uqo2L-DkdC5jRH6HglSkljbhMvgWKvL5cyCoFSRtl1QyCB3qpbB6ugcKJ6rtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
رئال سوسیداد - بورنموث
⏰
ساعت ۲۲:۳۰
🌎
📲
یوونتوس - ان ای سی نایمخن
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R26
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83594" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f8e0a26f.mp4?token=vwk_AWLFTJefisB3Rcahzv6HhqhezXCsB-lq1sdhu_9SiMWzBNFKUh4PvWfK4dZ6jsJLdfGO1IcgVUVsyY54z3Khp82eYF5-dOHgHD8lssm01Lj0Ad7qrMTL2N-zFYrUgvdronHdpGFSIrEvhXee2Wuc05JQAQxLeLo7R7gCCh_y8fcJauSaI8lbErvv2IAAId7ja2o07K14BTz0QGJkub9iO3jzPqEtXk6S-psw3g7OTB1fiVe4oCTtjK6tVkBoT7LhBrtYDTYY19bEWE0AYfnhSQXu7ZuQwEIOQ_UsLslvU8D_os7rzFQFl2VXDY_IuNJp-1ygvO6UupvXpUvb1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f8e0a26f.mp4?token=vwk_AWLFTJefisB3Rcahzv6HhqhezXCsB-lq1sdhu_9SiMWzBNFKUh4PvWfK4dZ6jsJLdfGO1IcgVUVsyY54z3Khp82eYF5-dOHgHD8lssm01Lj0Ad7qrMTL2N-zFYrUgvdronHdpGFSIrEvhXee2Wuc05JQAQxLeLo7R7gCCh_y8fcJauSaI8lbErvv2IAAId7ja2o07K14BTz0QGJkub9iO3jzPqEtXk6S-psw3g7OTB1fiVe4oCTtjK6tVkBoT7LhBrtYDTYY19bEWE0AYfnhSQXu7ZuQwEIOQ_UsLslvU8D_os7rzFQFl2VXDY_IuNJp-1ygvO6UupvXpUvb1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید بیگ شگی که رفته کنسرت ابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83593" target="_blank">📅 10:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKx5Pagcivh1DGn96YAlo7yo9Z4IMaFpKqrxJcr1I9GjUa1w48Cr3mmfRqc7HPc7rb0dCqzsYAkLi8hp6kXe7t_LC23YOa63-o762FBN4SGtHmBiZbQOCjuBl3bDD-2Clg6kewfklQF-7pHbI6gbUagICjiVl_k86aRI1H-xe0roLpeG9GgnsZWQsRW4KeykIr1iE6vA3TkHJKgg28K4DqnQBR9ntPGHJWsunNuOSIa7FoAtSuleosge_i4IpHkVdHutmMmDciTCpdvFtMzGkHvNMx5RhSireFcQJwZ6gyn6-XYVPSJK7q_SBsvlt7ccYaBTmJfnDzZHKolC8V8hlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا کریم؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83592" target="_blank">📅 09:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از باگ های تلگرام حامله ام
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83591" target="_blank">📅 08:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صبح دختر خانوم های عزیز بخیر، پسرا ایشالا بلند نمیشن از خواب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83590" target="_blank">📅 08:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83588">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIhYA7RqJqI79iyB3pNdtC2VTTs-JizGZDFGuYQj7hvNwoOC0JLE6-pzt_dOA_TxVU5w8rX6xotffv58gJcfsFSxoOrX7SIYgtZc8M9yhfLxA_UUaYtmIOvDYEnOq5cUetSrgZwBlwNQ-W1e0HYsnrwO3EMQffOQoiioiMVF35HSxTjN4MEQiKBecs91Fq5CNC9Ye1ABSXXIaey7UwYl1x04geYyDP7mynaVr-KzfkaFC4aN9RvNR5nEujpXqxm6PZvMdEmOhiEk02V2nfhamm76JtAl2ldt5Oatv0SI04pyT9aKpoCgLcy2B7VMEIT6Ej8bQKqjFPOese85Ds0vrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzcVIGkJtAR_yTRlrVqgozE8DRbAExOl79m7bXWtdbVA_ViHccb67Us7pwp54fAGmchS_iERnEctFqGP_Z-Oc8CjPnTBQvT2_G6dzgDYtbPpuMldXDSH8GVN0u61Wut6zAK00CI0qh-c5Sw3yh2floo0zXqfJ2RH6_IW84UCiLHX7O_i9j9nIRkLQQ9EtCl5547Pv4cRpyulSOKFQPL_sE-YZeJQKSk0wNANeghJgoPjQtck_YOq2TtnQViGuTLQFCl-A5DeFEoOINxd8hX-qhlBmt8x-kRSwfoRvdIcXRp3_S5gCy6SjqDV-2Ofp4yXaRGDW3DVsKoxhbbgnwqbdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علی ضیا و زیدش تو ایتالیا شکار شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83588" target="_blank">📅 03:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83587">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ببینید دوستان من الان ۵ تومنو کردم ۶۰ تومن، ولی این تا نهایت یه هفته همش بگا میره چون تجربه همینو ثابت کرده، بت رو برا سرگرمی بزنید نه درامد زایی که بگا میرید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83587" target="_blank">📅 01:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83586">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ45bVN_2uIi_ORbGu5_Q2iBJebzP7jCZZuTgA7d7zeahJLq5pGgjZHg28Sv0_ZpzGO-HH6dV7ldPjW7YvkkujHDC-ydYiZ__4pJea8FKT5cUxS-9Q6TMm6cz2EB9gVGHIyohrMUJyVES2rdQLf44eJnpM-DFjgOh3DplpCy0E7p10_XnKR1bYWISIS6zD36Abn8kYt7tNd9OTIyIJzHli_HWpaLd377CmS4rr2QjqWr1nMqx06KLFwTr0CCs8SkAgD0aGIXjDVD81qJ7LxQqcdA2iGHlb0g5FI3rA1SJ-PEgTjpa_NLIQnMclBf-zOHlt5hpoUn0JXHgpk5KmcJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینید دوستان من الان ۵ تومنو کردم ۶۰ تومن، ولی این تا نهایت یه هفته همش بگا میره چون تجربه همینو ثابت کرده، بت رو برا سرگرمی بزنید نه درامد زایی که بگا میرید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83586" target="_blank">📅 01:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f056dbed7e.mp4?token=W0QbB2HUCSQ9ozgmMrLg32WSjxDOL-9JCTu_tI1r_h6hpHzcz8hCShZeeG0UfP7Emij62uh2L9VxYha2-_GxDE6wN49bLQNkBmGQR4SMd6e8bCu0q75uHPNJGVRJeqbX9Tb1AUIhjUYL1lnjpcSpRwY7v7XVHZEgsRG39Kwt81H2d3rBpcWT7VszqjFe9AMgHpkd2TuDYMLGPxHe50SBOJmv_1SX8nNG8NP1tqgcXJy1fmDC17eGdaVcDL5RAzT4JFiC-HAnHfd4TVKAvBS63MYK3nNhapUy6uRcGuW7qvRmuUaKgVPWe27uohQ5v43OZYtXO81aAXfFQPsWDbV0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f056dbed7e.mp4?token=W0QbB2HUCSQ9ozgmMrLg32WSjxDOL-9JCTu_tI1r_h6hpHzcz8hCShZeeG0UfP7Emij62uh2L9VxYha2-_GxDE6wN49bLQNkBmGQR4SMd6e8bCu0q75uHPNJGVRJeqbX9Tb1AUIhjUYL1lnjpcSpRwY7v7XVHZEgsRG39Kwt81H2d3rBpcWT7VszqjFe9AMgHpkd2TuDYMLGPxHe50SBOJmv_1SX8nNG8NP1tqgcXJy1fmDC17eGdaVcDL5RAzT4JFiC-HAnHfd4TVKAvBS63MYK3nNhapUy6uRcGuW7qvRmuUaKgVPWe27uohQ5v43OZYtXO81aAXfFQPsWDbV0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجوری که عملکرد بارسا رو میبینم بهتره باخت فنی بدیم حداقل ۵ تا نمی‌خوریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83585" target="_blank">📅 01:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عاشق منچستر شدم، هربار میزنم رو‌ حریفش نا امیدم نمیکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83584" target="_blank">📅 01:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه تحقیق کنید ببینید ادیمی رو تو بچگی همزمان زلاتان و مسی باهم نمالیدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83583" target="_blank">📅 01:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فلیک کسکش از ۵ بکش بیرون شبا تو خوابم میاد   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83580" target="_blank">📅 00:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فلیک کسکش از ۵ بکش بیرون شبا تو خوابم میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83579" target="_blank">📅 00:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منچستر فنا واقعا بدبختن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83578" target="_blank">📅 23:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83577">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانسلو رو بیارید جا رضایی چه موشکایی ول میده</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/83577" target="_blank">📅 23:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی به فلیک بگه داداش زندگی رو نمیخواد اونقدا هم سخت بگیری یکم شل کن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83576" target="_blank">📅 23:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جا پوتک بودم ربکا رو میاوردم تو موزیک ویدیو دیس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83575" target="_blank">📅 23:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پوتک و آرتا چرا متوقف نمیشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83574" target="_blank">📅 23:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اون موقع هایی که آداما ترائوره به خودش روغن میمالید میومد تو زمین باید دنیا متوقف میشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83573" target="_blank">📅 22:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اقا اول تست کن بعد خرید کن!
گیگی فقط 3 هزار کانفیگ پر سرعت
🫆
شارژ حساب کمتر ۱ دقیقه
✅
@NetingVpnBot
@NetingVpnBot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83572" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه (پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83571" target="_blank">📅 21:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه
(پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83570" target="_blank">📅 21:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینا مگه تا یه ساعت پیش به هم ناموسی نمی‌دادن؟
چرا الان دارن با هم رفیق می‌شن؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83569" target="_blank">📅 21:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پوتک پری روز گفت من جواب دیس آرتا رو نمیدم کوروش دیس بده جواب میدم
واکنش وانتونز چی بود؟ این حرفو قبول کردن و کوروش رو اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83568" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پدر عجب چیزی داده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83567" target="_blank">📅 21:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حاجی تهه ویس ببینید چجوری با خجالت کیرو میگه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83566" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">از بیف تلخون و پارسالیپ رسیدیم به بیف این دو تا یتیمچه
عجب پسرفتی کردیم پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83565" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آرتا درمورد رابطه پوتک و نسل چهار و خلسه:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83564" target="_blank">📅 20:09 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
