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
<img src="https://cdn4.telesco.pe/file/oS3HjtFqTy3dSLsVhC3-wZ0nyoCK7nzk6d5KvLIaAUzgFTRETWuetsMVllhAGVkhPZ4Xmqsf_aKtDA26CpxsEVbm0m4ImNgnqlDdGOSubgyY_jtQlLU0PSoVEINeB-ss6-5lNGNcHcqe0SqGpMgKFwb9l4wvjrlqq0Po-ayclVoe2Kjnj0BVumncU1zR7VLwWe2c3QInj8IEQehpl0AmLOpD0ass51qLrQ9TG7c6ggp1fwqq_2f0tGU0o4J5A2K6jNvI7fBLj8ndpHzSH7lk_0yJg3he8VyU7jQlsTmZFhpwnA5mqvyg96hsLfTV_G00mXzgod2vfbP2CNm1g0HSQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 02:17:25</div>
<hr>

<div class="tg-post" id="msg-669351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
روضه خدام حرم امام رضا علیه السلام بعد از تشییع پیکر امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/669351" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2757dbcfa9.mp4?token=VbGWI7lY9gRvrXwqm82u5D-pkfwYIgEiKjcMaAN_khW9BANpLmB6-ZLFZksjq2e9an4ImEqFc95WZ-AglE_-9YXJh4RFTHoR__3NCQzFP3MDFBW4d8nXBMp7kujn8rRMwkoO549o3uNlVS8vVEAuxWB6uCcMuEEJy5uvKw4LvktjQruTSG4NwtRmUN65526YQSGDZ-jVcBL6pLPTYqE-SCHw1-38QXzo6eojOpLtC12RCyRPE7Hvcu-kxDhqjCIvF-5LFkK1RV63yVaxfJcmAE1TnX4pZgy61CMugHm7OQqLeqCgpk0nA1Ay7AOGHmsYaTXNa3IYNg4smWTHyBLhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2757dbcfa9.mp4?token=VbGWI7lY9gRvrXwqm82u5D-pkfwYIgEiKjcMaAN_khW9BANpLmB6-ZLFZksjq2e9an4ImEqFc95WZ-AglE_-9YXJh4RFTHoR__3NCQzFP3MDFBW4d8nXBMp7kujn8rRMwkoO549o3uNlVS8vVEAuxWB6uCcMuEEJy5uvKw4LvktjQruTSG4NwtRmUN65526YQSGDZ-jVcBL6pLPTYqE-SCHw1-38QXzo6eojOpLtC12RCyRPE7Hvcu-kxDhqjCIvF-5LFkK1RV63yVaxfJcmAE1TnX4pZgy61CMugHm7OQqLeqCgpk0nA1Ay7AOGHmsYaTXNa3IYNg4smWTHyBLhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به امید دیداری دیگر...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/669350" target="_blank">📅 02:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b553e0cb.mp4?token=ToAnon5rhp_8UTHERJjG7Lvu-HtEj1Id2vKyJSglvPL8n9nhlYXBOkRvtvwrdic_AMbXS14us-6zhfQB1vusrY1AJnExXq_X9-WaCosWWreMEZt83LNyzJFP7ASEa6v_6Yai_IbQYvQkKojOxJQThScAMKqtHbN1S5RswN9QMEINZrcUJCTPvN3DExbYzdTpK5nwrOyAT29rCv8-C_atsCAOT5bKu_RxPzn2-60KfRVsvpJ2rPPogw_mPtR0gpLQH4f_uv5C7A-B8RuC7jeieAKEfKEukybK2wapKnb4g96_05zXLjYe3yfQzkrZYAC0D_1I306mwVwWR0UnQhc62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b553e0cb.mp4?token=ToAnon5rhp_8UTHERJjG7Lvu-HtEj1Id2vKyJSglvPL8n9nhlYXBOkRvtvwrdic_AMbXS14us-6zhfQB1vusrY1AJnExXq_X9-WaCosWWreMEZt83LNyzJFP7ASEa6v_6Yai_IbQYvQkKojOxJQThScAMKqtHbN1S5RswN9QMEINZrcUJCTPvN3DExbYzdTpK5nwrOyAT29rCv8-C_atsCAOT5bKu_RxPzn2-60KfRVsvpJ2rPPogw_mPtR0gpLQH4f_uv5C7A-B8RuC7jeieAKEfKEukybK2wapKnb4g96_05zXLjYe3yfQzkrZYAC0D_1I306mwVwWR0UnQhc62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار ما به قیامت آقای آسمانی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669349" target="_blank">📅 01:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2RA-lIcp0e3_WiziDkqsMC0JT_EWDBcdUjn8IwdlSWhOnmahY0qTqphvCJsO_H9gIfp6cGy_6xMY16iHJ-6XmeskdK5pygzenzRFpVuoJ2vb3K9SiF-2r3VeNmcMpvJub54L0kjvRPo0ttvZ2GR1s4FCrERMPpJTLGzcNF-fHwZkTn0ez3II9OViPbyVz-6CZoc-6D9ZdyML12-tdiTs2OE9TFk5tOfJvyf3EsmMbXLG87Wrp1SBDGDGMLvFSYsoLbwTG1EoG4Iq6jbgqpIEYwmveY5JlUGJ2lj0kCO_9mR93Uf4oUNkk127ZFpJc7Sle72mdJzU8K6bu9UwcgQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۱:۲۰</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/669348" target="_blank">📅 01:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb2e3a97f.mp4?token=ka0-Ir55R2YmY1uOiM02Vi_wk3Jo8-llZhVeB7HwBGI4dWfLiCpFjXnRwUz3NKk0H2e93-M4YW-WyWNxsRGMQgq7Hx2b_Y1Ka8S9M_lz0K2YozMcRdFql4tfF6IOCZKi8tLssubFs3QvFJDWMhwgKhN1uHc8LmTaoUOKftmFaa08ByADkihZnj8t3AYe3sAooG6Wz5IiQ6fopux3pF4D_FMzWv0H37KB-I0TScRkFvvJBBS8_H6qZq6UYvYOAcF5xW5CgpuGJq-BE4Sbcapnva3S7NbZOOj12RyPddg3cxhpw0eD7CrTiI60UCjiPndUKnMxxUHsmGRQuqjvGWh6OFkI-6Wc734zqW42jY1t2QsNaNzdsZviafqK_FknadJtKYZhZGWL8DvGSGx06rkGXgMZxlhtBgFl2-463wUVByO_MD13O7m2OosjNuat1qTaGd1rkcN_4Gw03fcNsCyNaLRrhyKriqqaXMcKAiyu__zC0GpTMTunGjFxOKL8Gm9m906JeC8UOkn5A979j93NZhZK_wI3vi4THii5AQFrbocOcKjztePHkxz8ARgPkJg-heSJpOORj4BXdzVPFVDrgLJQBpgnaoho7qattbEobS7bUD8oVCtskNPHJju8ZHnXhgMSbv6D54JPsHjMwdtsVIUd2FY6YQ5EPnNMmEx6kKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb2e3a97f.mp4?token=ka0-Ir55R2YmY1uOiM02Vi_wk3Jo8-llZhVeB7HwBGI4dWfLiCpFjXnRwUz3NKk0H2e93-M4YW-WyWNxsRGMQgq7Hx2b_Y1Ka8S9M_lz0K2YozMcRdFql4tfF6IOCZKi8tLssubFs3QvFJDWMhwgKhN1uHc8LmTaoUOKftmFaa08ByADkihZnj8t3AYe3sAooG6Wz5IiQ6fopux3pF4D_FMzWv0H37KB-I0TScRkFvvJBBS8_H6qZq6UYvYOAcF5xW5CgpuGJq-BE4Sbcapnva3S7NbZOOj12RyPddg3cxhpw0eD7CrTiI60UCjiPndUKnMxxUHsmGRQuqjvGWh6OFkI-6Wc734zqW42jY1t2QsNaNzdsZviafqK_FknadJtKYZhZGWL8DvGSGx06rkGXgMZxlhtBgFl2-463wUVByO_MD13O7m2OosjNuat1qTaGd1rkcN_4Gw03fcNsCyNaLRrhyKriqqaXMcKAiyu__zC0GpTMTunGjFxOKL8Gm9m906JeC8UOkn5A979j93NZhZK_wI3vi4THii5AQFrbocOcKjztePHkxz8ARgPkJg-heSJpOORj4BXdzVPFVDrgLJQBpgnaoho7qattbEobS7bUD8oVCtskNPHJju8ZHnXhgMSbv6D54JPsHjMwdtsVIUd2FY6YQ5EPnNMmEx6kKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بله، وقت تمام شد...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669347" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYigegoSYjOUo2SoHi0tS7eYHtkj3_F5uynqtVaSr3ikIhE0FRH0HxLuLoH6P5QMR1SL2Xu8-KxTKE9W54OGy79cVuoDqiEZ75iBeCuireRuHoGJV4QrVD7X-GSNgjcCU5bi7V729KUX5p9gNbtWa_PLJDh9S97KzKMBxGS7BxG514WdfIFdk_IVsKJ7gIUKskwpR1L003WugbTzaEeauk4ZV4P-H8FocWWAHCUB7plNPxs4R2A16W4kR-FTdaqNF8S-dzRfBDBu11BHWzy5kGgMvbjkUicAVh4XzpfeewkcdGjA4KF-g0MUF3bs6tPOLUTfZIT_gc398TTUUuABnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینک شما و وحشت دنیای بی علی...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669346" target="_blank">📅 01:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=EdODjygXCrcfLlhHmpdLkGsgMPUeUIUviuPMaa5tBvNUd2YToNdicx3OvnpR1D1-p253nM54yu1brpNrP3t5VOQBqirsEDj_b8hZyKIIKwJYAzyfMYt1nw55P0yXIcU6Q1amvjPPSM7glZle5WA-lsKhB-zf1j6NJtY8l4QY7L7seqhPczeaFWKGwmTWwmltUmSoc3gHZ9lLV3SEPEMFBaZenWNKTh6JqyeylZ4WgCl5wP57HEdncftzwyh7mqeJABLKo77TIyBIcbSNtd7rWtTa9IwexR2dspmM75kyftHKvEQz__S3aJVrGC7AVNYPyhM29zrRPA_-LSv5Hw6_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=EdODjygXCrcfLlhHmpdLkGsgMPUeUIUviuPMaa5tBvNUd2YToNdicx3OvnpR1D1-p253nM54yu1brpNrP3t5VOQBqirsEDj_b8hZyKIIKwJYAzyfMYt1nw55P0yXIcU6Q1amvjPPSM7glZle5WA-lsKhB-zf1j6NJtY8l4QY7L7seqhPczeaFWKGwmTWwmltUmSoc3gHZ9lLV3SEPEMFBaZenWNKTh6JqyeylZ4WgCl5wP57HEdncftzwyh7mqeJABLKo77TIyBIcbSNtd7rWtTa9IwexR2dspmM75kyftHKvEQz__S3aJVrGC7AVNYPyhM29zrRPA_-LSv5Hw6_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جمع خادمانت، شوری به‌پا بود امشب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669345" target="_blank">📅 01:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1iBaFDorWX67BgDbCChPAmqz8VAwU4Sn021_kyrPrsf13FD_Kaw8X2PFST3KkQwI1skkpcRv4AqGfaeuNvQ64jAG4syV7l46f34W94Td1vAymrtyWi53_sDwlxIZd88NTL-4Wp0HU-iiakfjWD-WQlACxgnseqW5RuG0-mhE_xrtNiLbU8MfAOWa3ejEJCV5VfABAnZRBNDT3QvYVsyE1lJlFHbTGropgX9V3kj_ewdndtEEgV1XrVnY73LXZcmf1q3CFm7V7EG0z3Sv3GCEaAbmYoKCMzDYC95Lg-QpFu8_WVmcGwsAxxL8KQEudWd_ySqG1LWcJQ8DwqXZz5-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروس‌ها نخستین تیم صعودکننده به نیمه‌نهایی جام جهانی
🔹
تیم ملی فوتبال فرانسه با ۲ گل کیلین امباپه و عثمان دمبله با برد مقابل مراکش، برای سومین دوره پیاپی راهی نیمه‌نهایی شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669344" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">نقطه‌ای که ادمینِ کانال اخبار رهبر شهید انقلاب بعد از طواف و خاکسپاری پیکر آقا گذاشت کار صدتا روضه رو انجام داد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669343" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H88ZtVQtw-lHh5lNn4LeKb4huDttl1X4Xtr-lqDlCRhPy1vNMEJrpm-JjCOaoLag5XcBW6_mADEEApFTJgrkUGa7OWpaBF5rWALYUwc7yb-4yJLp27qTwc_HC2kCcWIW5r8cmdoMyOobN7Qju1mnqAeCvwgl-JPE9wwalMnVcinEWS3hJqcrNWQsMUQY19z4g7WeZtrUgmK5Ts1J1BjJT1T1tICqlY5h7n8HFlYcmx58PkbnwAHbiGRWSSuIjE4117urjqe9sVdW6oZwmd9rlhn81ESFeN8nZ2WZ4T3fwGITK6VyuoeOzeCEEP7L4nrQ_skDtsWjORtFBOWAOJjnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقطه‌ای که ادمینِ کانال اخبار رهبر شهید انقلاب بعد از طواف و خاکسپاری پیکر آقا گذاشت کار صدتا روضه رو انجام داد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669342" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8a1ef2d7.mp4?token=TVR8P1Y5X3MGGsE_u-HEFvAJrmc_5NcBpMO03XqNdCV4lQIn6A3Cc6ni_-7C40cQQwBC5-DHZTHP_l3WShzFNqawtlMMg9B0rjs3SadcN9BaT67JkJmZ-hmYjEGbjUv_DFVdx9QYr4o6fDgLYlIaiyVmIV1Jeg7_wbEyO7cdzdyXrn69DhdTErD1OfblRB4qrFv01UkEVMHoO6wg6zuFJ0JcAbcRt8c-R6ESFG35bX_qY2KeNpNsTWxxTZpEp_fmqHCLw9X090quxR1NnyvmAxFOI3wLF065M3gjzwmBuUAh3UCzs1is04NHWYCZIKh1PIPl2A2P4b5_Zd316iNEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8a1ef2d7.mp4?token=TVR8P1Y5X3MGGsE_u-HEFvAJrmc_5NcBpMO03XqNdCV4lQIn6A3Cc6ni_-7C40cQQwBC5-DHZTHP_l3WShzFNqawtlMMg9B0rjs3SadcN9BaT67JkJmZ-hmYjEGbjUv_DFVdx9QYr4o6fDgLYlIaiyVmIV1Jeg7_wbEyO7cdzdyXrn69DhdTErD1OfblRB4qrFv01UkEVMHoO6wg6zuFJ0JcAbcRt8c-R6ESFG35bX_qY2KeNpNsTWxxTZpEp_fmqHCLw9X090quxR1NnyvmAxFOI3wLF065M3gjzwmBuUAh3UCzs1is04NHWYCZIKh1PIPl2A2P4b5_Zd316iNEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکرهای خانواده رهبر شهید برگرد ضریح مطهر حضرت رضا (ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669338" target="_blank">📅 01:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669337">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وقوع تیراندازی در مشهد تائید شد/ دو نفر کشته شدند
🔹
معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان مشهد و کشته شدن ۲ نفر را تایید کرد و از ارائه جزییات بیشتر در این باره خودداری و تاکید کرد: «هنوز علت حادثه و هویت کشته شدگان مشخص…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/669337" target="_blank">📅 01:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669336">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: اسرائیل به آمریکا اطلاعاتی داده که نشان از طرح ایران برای ترور ترامپ دارد
🔹
اسرائیل اخیراً اطلاعات جدیدی را با آمریکا به اشتراک گذاشته که به گفته آن، نشان می‌دهد ایران طرح جدیدی برای ترور ترامپ، دارد.
🔹
خوک نجس روز چهارشنبه در جریان نشست سران ناتو در آنکارا، ترکیه، به تهدیدهای ایران علیه جان خود اشاره کرد و گفت: «آن‌ها می‌خواهند رهبر آمریکا — یعنی من — را از بین ببرند... من در همه فهرست‌ها هستم. امروز صبح دیدم که در تک‌تک فهرست‌های آن‌ها قرار دارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/669336" target="_blank">📅 01:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669335">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPbAnmg8fyOCb30ywolAn3_WmJzAE6psa6OE0giYdlNUJXQ-vMGBsmNwlE2x_wUQ5FoOwDa83CYMRjZNCWQA62z7c1jgBDf_GM7Cgm6RYbTixUytb9s157up54pE7Va-TTEwdFqr93wnTKv4G_My3NbIZFwYGPiXWf8vzgElrDvPjlZ88PwmXTJzrIlQTydyFdTrTCg9P7d7oBHw8EEQZao7hi1NVL7HpdxhjgmyDPLkK5h7EYFJKyfz78FQqpIWJupYrbFUM_xm7IpPcSuDV6-eYOS4bvew9HDHv44XPm0sliPMY4RG1plwnJaE3t3fcvB39-1Hn4zoWHE8u5utQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دشمن، از درک معمای حضور میلیونی مردم ایران در صحنه عاجز است؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/669335" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669334">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55abc22245.mp4?token=hutxpcvyNDTewHIHrAqhHD92r7Vziq6JavdiEzHmvoB7qXq8pmRtIGYBxHPS7jmPN1bVzysT5NcDJ33klYKaBGb0NRsQ5eR8IW8JcbYosSdaEwcXMOsUsdPVo-P9C8J00YHeC2M62BixtVpKFCxxgnc3vQNVYfZ7C7e71mrtbY2A3GLrJPqO5xhrsu84b2OnJbK4o86a9h_iFnZeYM4JV45FrPxppARQr1MZ3RddG2zA3y1OC9CO6eF-aXLsb4bfym2CZbDvIkMS4jeb1Vqdo6fkQ4x_1GGuE42ZTrZgs-rhZU7SoRwuMgor_onebGYtNzHDKWFQL3NfuHIRUzaqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55abc22245.mp4?token=hutxpcvyNDTewHIHrAqhHD92r7Vziq6JavdiEzHmvoB7qXq8pmRtIGYBxHPS7jmPN1bVzysT5NcDJ33klYKaBGb0NRsQ5eR8IW8JcbYosSdaEwcXMOsUsdPVo-P9C8J00YHeC2M62BixtVpKFCxxgnc3vQNVYfZ7C7e71mrtbY2A3GLrJPqO5xhrsu84b2OnJbK4o86a9h_iFnZeYM4JV45FrPxppARQr1MZ3RddG2zA3y1OC9CO6eF-aXLsb4bfym2CZbDvIkMS4jeb1Vqdo6fkQ4x_1GGuE42ZTrZgs-rhZU7SoRwuMgor_onebGYtNzHDKWFQL3NfuHIRUzaqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حلالیت‌طلبی یوسف سلامی، خبرنگار صدا‌وسیما از رهبر شهید انقلاب به‌نیابت از همه کسانی‌که طلب حلالیت داشتند
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/669334" target="_blank">📅 01:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669333">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هم‌اکنون سوزاندن نمادین طرح لگویی ترامپ در مشهد
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669333" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669332">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
معاون امنیتی استانداری خوزستان: هیچ حادثه امنیتی در استان رخ نداده است
🔹
معاون امنیتی و انتظامی‌ استانداری خوزستان اعلام کرد که برخلاف شایعات و ادعای دروغین رسانه‌های صهیونیستی، هیچ‌گونه حادثه امنیتی یا حمله‌ای از سوی دشمنان در سطح استان صورت نگرفته است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/669332" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669331">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d589bff.mp4?token=G6xYPIITmsk7mkSVBDFc8Zg7nW_0X8iyh0OWlPM14h6uZeec1LNFXVOuAf47zK14BR1lFS0yTU41gjAYPZFVtP3NvnK_5ONSX63wtieCrlhVNAXUjHZAmlO5j2rnyhxBaH_qfEv99LVLDLh_YvGmzaYYq7hAtb-UG6CUlTfDh3JykMMBF3eYToYxbO8gF5ZVBpqR0UW85dCO0GHHmv1ZhVyZLEPPbQovjlCWpeJGRmSCFF3tnrx_Yvmdn47ZnO-PHN7Ib97ACLwP-VsJkdTCa6964FBrXwXAeUfPhU85-A5b6or8akqXlHvz84OEHpDQ6ZA-n_2AX8GrXtr5QdHqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d589bff.mp4?token=G6xYPIITmsk7mkSVBDFc8Zg7nW_0X8iyh0OWlPM14h6uZeec1LNFXVOuAf47zK14BR1lFS0yTU41gjAYPZFVtP3NvnK_5ONSX63wtieCrlhVNAXUjHZAmlO5j2rnyhxBaH_qfEv99LVLDLh_YvGmzaYYq7hAtb-UG6CUlTfDh3JykMMBF3eYToYxbO8gF5ZVBpqR0UW85dCO0GHHmv1ZhVyZLEPPbQovjlCWpeJGRmSCFF3tnrx_Yvmdn47ZnO-PHN7Ib97ACLwP-VsJkdTCa6964FBrXwXAeUfPhU85-A5b6or8akqXlHvz84OEHpDQ6ZA-n_2AX8GrXtr5QdHqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم فرانسه به مراکش توسط دمبله
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/669331" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وقوع تیراندازی در مشهد تائید شد/ دو نفر کشته شدند
🔹
معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان مشهد و کشته شدن ۲ نفر را تایید کرد و از ارائه جزییات بیشتر در این باره خودداری و تاکید کرد: «هنوز علت حادثه و هویت کشته شدگان مشخص نیست.»/ ایرنا
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/669329" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669328">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344822aa12.mp4?token=OXga43IVlOzSZ5mfj2SXKRqA-3mDlm_zcMr3egv1Tuogh62-zF-1h9NtQfkeCdI4tl1RtlaoMeEfo4PoS46ub5RPW-CSfgugB5xetm4Xc07yTexJl62LU4Fu26ANqHgnX2k-XsZy_SKJhKD-zddadscp07ogv4Qz5Ubk8CpDdZfZ68qrjjxtcxO2tWTJ2b2tAv8GBmEvZDz5FeXqnQVGeM1y99IPUzUlwaUiJ9kAoRpygLwJZaWBfl5KgYMmTF6f3UHLTWoKCZsauRebe0e_vudJuZC8-o2Y_VLMWJaZofv1OzslFTl0jwNMxAlUFhHE55R6cwh8uPzYC09KUEM7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344822aa12.mp4?token=OXga43IVlOzSZ5mfj2SXKRqA-3mDlm_zcMr3egv1Tuogh62-zF-1h9NtQfkeCdI4tl1RtlaoMeEfo4PoS46ub5RPW-CSfgugB5xetm4Xc07yTexJl62LU4Fu26ANqHgnX2k-XsZy_SKJhKD-zddadscp07ogv4Qz5Ubk8CpDdZfZ68qrjjxtcxO2tWTJ2b2tAv8GBmEvZDz5FeXqnQVGeM1y99IPUzUlwaUiJ9kAoRpygLwJZaWBfl5KgYMmTF6f3UHLTWoKCZsauRebe0e_vudJuZC8-o2Y_VLMWJaZofv1OzslFTl0jwNMxAlUFhHE55R6cwh8uPzYC09KUEM7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به مراکش توسط امباپه در دقیقه ۶
۰
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/669328" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای جدید سنتکام درباره تنگه هرمز
سازمان تروریستی سنتکام:
🔹
ادعاهای رسانه‌های ایرانی مبنی بر اینکه عبور از تنگه هرمز فقط از طریق مسیرهای تعیین‌ شده توسط تهران مجاز است، نادرست است. آمریکا در هفته‌های گذشته مسیر جدیدی برای عبور کشتی‌ها از تنگه هرمز پیشنهاد داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669326" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669325">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
علت عدم حضور آیت‌الله نوری همدانی برای اقامه نماز امام شهید
اطلاعیه دفتر معظم له:
🔹
با وجود آنکه مقدمات حضور معظم‌له در این مراسم مورد بررسی قرار گرفته بود، اما با توجه به ملاحظات جسمانی معظم‌له، بُعد مسافت و فراهم نشدن شرایط لازم برای انجام سفر، حضور ایشان میسر نگردید.
🔹
همچنین چند روز پیش از برگزاری مراسم، عدم امکان حضور معظم‌له اطلاع داده شده بود. با این حال، متأسفانه علی‌رغم اطلاع‌رسانی قبلی، خبر حضور معظم‌له تا ساعات پایانی مراسم در برخی رسانه‌ها منتشر شد و موجب بروز برخی ابهامات گردید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669325" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=MtMXPSDP4tatyVWgIDTH7yuFQM_L9DjE6cNqKG7Or88ivMTHvkNaLFRq-qRiTkuGPwgbR8d-ny790kaTu4n7UrgzJ9f3FWlZUcjsxSuLWbzoOP72fhSwNe-9A7pgJmjrbE7MQ5cxuHOg3wmdIRh8Uxyd0E0sBgjD_3qHjCLNJjtuKZgbqTzHclcEtIW80WTnO9S1xCRgzHTmF0YQtFdMDGpmT8SmMLCwMEvzwgzJ-VPxVrfFRqt_dlaEI4jtsUz1jKy9VzWUUvXV-h_xkLjKsMzfoHEPZV9hsFkS4QLv6OIloNYMRsFuh7fayhPs_plAHUhfog69ioJNdDplqzK5oE94asqa9b1cX0AXU96FaU_-cvhlrYSnR0WDNSn4tGrsq-N_lcZFr10jrqEaqYeeYWeL_p0eZGl-xEQopIKBOUPkgiNCLpTWMl_eKpWH1MkK5fzSpGa8GbdF94obuywWXRLCu9oIn-4Vod9yhn_81-iUtKx03DhLNILggME-451U8a10uRr4V9wThuzGxOBHnynY7_TGgDTHESNoNerXNECRQXub7oCyNRNpHX4NbpKnTLf46X5MWt7OFuDkY8hrsqDJskFtiKPuj9MeBztw6UPiWvg2qwcIXi-OHo0yF_jHDxYlzE3jY0bch9vIFvx-cQKad9XPT4n5iLfdOCmf5eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=MtMXPSDP4tatyVWgIDTH7yuFQM_L9DjE6cNqKG7Or88ivMTHvkNaLFRq-qRiTkuGPwgbR8d-ny790kaTu4n7UrgzJ9f3FWlZUcjsxSuLWbzoOP72fhSwNe-9A7pgJmjrbE7MQ5cxuHOg3wmdIRh8Uxyd0E0sBgjD_3qHjCLNJjtuKZgbqTzHclcEtIW80WTnO9S1xCRgzHTmF0YQtFdMDGpmT8SmMLCwMEvzwgzJ-VPxVrfFRqt_dlaEI4jtsUz1jKy9VzWUUvXV-h_xkLjKsMzfoHEPZV9hsFkS4QLv6OIloNYMRsFuh7fayhPs_plAHUhfog69ioJNdDplqzK5oE94asqa9b1cX0AXU96FaU_-cvhlrYSnR0WDNSn4tGrsq-N_lcZFr10jrqEaqYeeYWeL_p0eZGl-xEQopIKBOUPkgiNCLpTWMl_eKpWH1MkK5fzSpGa8GbdF94obuywWXRLCu9oIn-4Vod9yhn_81-iUtKx03DhLNILggME-451U8a10uRr4V9wThuzGxOBHnynY7_TGgDTHESNoNerXNECRQXub7oCyNRNpHX4NbpKnTLf46X5MWt7OFuDkY8hrsqDJskFtiKPuj9MeBztw6UPiWvg2qwcIXi-OHo0yF_jHDxYlzE3jY0bch9vIFvx-cQKad9XPT4n5iLfdOCmf5eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکرهای اعضای شهید خانوادۀ ابرمرد شهید تاریخ به دور ضریح امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669324" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=RVMV_1SauXiDsVz_Vcmu1YwfAibHWUvfMMiSIx9DGCVKnGKmER9ByvFgg4iyMM2w65bzUB-SoOpMoDD_pvqq_NA8_1jQ2rm-jznNu3m-rE7lLyUSew80TyFFuNE6EvbBKY3hUTtiseYvUNVmjURE85Fp7ascNtj5hsHzOC0zKAyV9gp1T60KFcYAScdrlH9_KqoESFfNosz4Ae0iCTV-2NVDAmw5cjpwIAPYe2vZThSEQYVyPHyht1RRDeipbfwNdJt3Exal1SAgdHA1uK2cVeeJRMgECdpIdnt4MuSVcSonrNPaNGcQ5yl1iyhohclTwmYbW3cILIwZYHOLAQa3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=RVMV_1SauXiDsVz_Vcmu1YwfAibHWUvfMMiSIx9DGCVKnGKmER9ByvFgg4iyMM2w65bzUB-SoOpMoDD_pvqq_NA8_1jQ2rm-jznNu3m-rE7lLyUSew80TyFFuNE6EvbBKY3hUTtiseYvUNVmjURE85Fp7ascNtj5hsHzOC0zKAyV9gp1T60KFcYAScdrlH9_KqoESFfNosz4Ae0iCTV-2NVDAmw5cjpwIAPYe2vZThSEQYVyPHyht1RRDeipbfwNdJt3Exal1SAgdHA1uK2cVeeJRMgECdpIdnt4MuSVcSonrNPaNGcQ5yl1iyhohclTwmYbW3cILIwZYHOLAQa3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوهٔ ۱۴ ماههٔ رهبر شهید به آغوش امام رضا رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/669323" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab92d02555.mp4?token=neP6w4lkr7vF3DRu8PNax76QdgErfhMudyGdFmuw3ImrDJ1KfkDoOihkeleFB88Ld011r0Ll9EizdQlHQOijqI8eQuPg_gzZfpXldWeMgQkx0gDTlbFCuQIqEOO8JM6EGlPVQ-hrhfnulCL0KfhU7vu-_58dqy4h4IO1u5SKTVBaflCfK-Tq0YYegVJ3NTue908W8uzPOiL6TfXX_qLNhAc4fxQwQWo1yadUypMPR_EN1TuJyDDT9rmJ9C06-QuNtHXT6d4NW_dBEd0waFOjzTS6PJ3eYff8JxJ3W47UgkZahr_XG6FJ9dXtPbUBoZIXabj9fwipp-_QIB069K_b8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab92d02555.mp4?token=neP6w4lkr7vF3DRu8PNax76QdgErfhMudyGdFmuw3ImrDJ1KfkDoOihkeleFB88Ld011r0Ll9EizdQlHQOijqI8eQuPg_gzZfpXldWeMgQkx0gDTlbFCuQIqEOO8JM6EGlPVQ-hrhfnulCL0KfhU7vu-_58dqy4h4IO1u5SKTVBaflCfK-Tq0YYegVJ3NTue908W8uzPOiL6TfXX_qLNhAc4fxQwQWo1yadUypMPR_EN1TuJyDDT9rmJ9C06-QuNtHXT6d4NW_dBEd0waFOjzTS6PJ3eYff8JxJ3W47UgkZahr_XG6FJ9dXtPbUBoZIXabj9fwipp-_QIB069K_b8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه محمود کریمی در فراق رهبر شهید و گریه بی‌امان خدام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669322" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyCKgxIjJGT4h0fvvONkSx2RD5iyUzqBz4VQmVJILRshsHg4lRY-XOvOUpdrSoBwXaV4b-MHVoiwgkTIYFNVt3fY1TO4iG_yDe_1p8vt0m-v0TWj_foGxXtTlzGzoZPsaLNKqd2l_zsDtkjJq9Q_Jb4VGuhOSabpoo2ylXrxVYXbbPW1dNlAJ2xP1sN-0OQprn64KVAgLozbIAyyUNevbeOsJu3op3e86Xk0E4298M874ZLDCtTy7QE9AMg6uLOBOAB5gsilHQ4Zzxhgmb2j-KonXt4IxLjC206ryrUBYJg1BFWDkSNPhYPl_vZtXbxHIEqdhpV2qEoQLqoDQFxcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669321" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqIUe8_POMDzUQJo6SitEMP2wvylI4VTHKOw5LLXAcytBFDElELapbMrcDrmQOe_NLqgTxqpyrcuTwrxBfiXI0chjN1lhs1DqCkkHAnyUZci8XK57X2iGOy4Nv7aLZpthbwnrFd124gv7wULV6fOBv7-P_7UOs1hdZ7Ula1f_V95WTfiNhzeW-u1hJEZ7eITGkfi2guEGFy0D5ySeCDPLkxDwcxVhhEj6wnfw9df4x-CH7IdWSSlG82Bgq5CyULpCgbc2fCR7LMCTtE9FkwfRhb9EfWbRM4l9k5CO444HQ4EptJZVSkA7-vlSEW0phctVGLRBpBDvWXXj8mrUp0KeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید در آغوش امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669320" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9Dicrh-fcTGoUukM4HTrqogaMWj3RRiJOJ84oeBVtqt6pGj6o51cfx47oNm457rzjTw1TT0kIfh5h_BXW6KJW_KDn6tiE5C0Ku7W7C-Tk06Ss8S-5lb_uEMuCJKkhPFbiDxv06YpPc9g0XW6ipishwffmu66Bx8AF4AQkGmUFY1adXnInPQjvmZUPooaw6jxLyOI7rCPr2kvvHgHWAgy_-8SitTxpczg6RIyKXx-Yk6BQKnalcsaweEBJAatqR7635YhV62Zq_G6gw9evmFfyKpOd6yW3ij3r0UCi5AI7pFq-_RgS_HVebRKBpVr0a7JrhfXVr74VMUW44AT8A4ip4IOx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9Dicrh-fcTGoUukM4HTrqogaMWj3RRiJOJ84oeBVtqt6pGj6o51cfx47oNm457rzjTw1TT0kIfh5h_BXW6KJW_KDn6tiE5C0Ku7W7C-Tk06Ss8S-5lb_uEMuCJKkhPFbiDxv06YpPc9g0XW6ipishwffmu66Bx8AF4AQkGmUFY1adXnInPQjvmZUPooaw6jxLyOI7rCPr2kvvHgHWAgy_-8SitTxpczg6RIyKXx-Yk6BQKnalcsaweEBJAatqR7635YhV62Zq_G6gw9evmFfyKpOd6yW3ij3r0UCi5AI7pFq-_RgS_HVebRKBpVr0a7JrhfXVr74VMUW44AT8A4ip4IOx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر رهبر شهید روی دستان خادمان حرم امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669319" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fc6307b0.mp4?token=szEj-iINWz6R4XAu6GnzdYR6nmoNE9PscxIiZatYzlBrR334BVS7rvA8p4kiy8Bz4ZEyv4qbk-CY0mlslcJ60JGANUIzzkOZXm6FWtJOoRmy7dA5SC8LKzdZOQlvqAqGwnEuGlpVvOTNIuNyA6wsfwBO93gaxhekbGnOsjjhWQ_qpoePsR9ZREIJ3HQaNMJUkBe92cunmaNqnBIkmfXKKBD6k8z9AKqtopvLG193NujJ70C77ObTddTxfyekvLYdI_HAZ1M-dar2eA42AnefjoFk8JuTCqdZdfknnvxk5G3JswCwEs-ePzNlvzd4B03TUxRJ79G_mcsLmQUtoniTYgbXncuntwrADWUHxjlwtGmag1Ukha6nfJPTLXk8qHWSC7QpQQA_jGN86Cb47VuPhK4Z0TO91vf82kv7AXN8UTbP_EiH9wj38Y-jVf1l7R8ygOYXWQNcy7yeKuLfCjbOkeJSgFk_93ixuQhqlkWuI7wHSaGmfqu3JEkyvBjjpn72bT4wXaufBDzhSTKY6y5T50rNMHjjkDz63o1Z9KnqzHXsKWHssJCH0h2fIjrybsD3nDVtJMhClw25QOaBSwWZXP-HrOJ3_S2ugFxHSOgt7dm2kgSeoaojPe-97LDpuoz3qEbfKWB4sP9vkFHZLl6_YfFZnhTWUWQmksFBfON_Z3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fc6307b0.mp4?token=szEj-iINWz6R4XAu6GnzdYR6nmoNE9PscxIiZatYzlBrR334BVS7rvA8p4kiy8Bz4ZEyv4qbk-CY0mlslcJ60JGANUIzzkOZXm6FWtJOoRmy7dA5SC8LKzdZOQlvqAqGwnEuGlpVvOTNIuNyA6wsfwBO93gaxhekbGnOsjjhWQ_qpoePsR9ZREIJ3HQaNMJUkBe92cunmaNqnBIkmfXKKBD6k8z9AKqtopvLG193NujJ70C77ObTddTxfyekvLYdI_HAZ1M-dar2eA42AnefjoFk8JuTCqdZdfknnvxk5G3JswCwEs-ePzNlvzd4B03TUxRJ79G_mcsLmQUtoniTYgbXncuntwrADWUHxjlwtGmag1Ukha6nfJPTLXk8qHWSC7QpQQA_jGN86Cb47VuPhK4Z0TO91vf82kv7AXN8UTbP_EiH9wj38Y-jVf1l7R8ygOYXWQNcy7yeKuLfCjbOkeJSgFk_93ixuQhqlkWuI7wHSaGmfqu3JEkyvBjjpn72bT4wXaufBDzhSTKY6y5T50rNMHjjkDz63o1Z9KnqzHXsKWHssJCH0h2fIjrybsD3nDVtJMhClw25QOaBSwWZXP-HrOJ3_S2ugFxHSOgt7dm2kgSeoaojPe-97LDpuoz3qEbfKWB4sP9vkFHZLl6_YfFZnhTWUWQmksFBfON_Z3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از روضه حاج میثم مطیعی قبل از تدفین پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669318" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669317">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaLr7ayjD-ztWWXYWNJeCuv5y5ctiBMGptnoEgOw4KN5mCmB1t3fd44aUiiQe-CJGGuqOASv2yxv_DNx4eOFITE8IkpgyuDPaMdpv7G8f8qK25szDkl0tI8GaCgBP_XcenBbX7nFwe5QZozM9Yh8eY1MIUrM7W75FzUEr2WcYuLUwUCT8B5G5yPOGIwEkdn53vdfO8Yr35O0XAPayzn4t91c6pd3RSwEJeD6H3OZri-VGyDrAss2mFxQIDdmnjegP-QlawSzALZZjzZnoznRwlzlk5jodfTHbU3qpc18GJNT5mqaRGU23MJNovWCwmudBraOcSpFLTl839NL2P5Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رئیس خدام آستان قدس رضوی، امشب مهمان خاص امام رضاست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669317" target="_blank">📅 00:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669316">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYgqYE1_oGYwDSHoYDvVlBzbdPAggJS-t6E7NYRDCcs6aRoC0OnI_MfUpX39NYXy6w3jb_AJzFhq009_hwavOBKxNqkjKdQNoEOuWqZhec7aXSv7a_vJOvNYZtHX-6ilX8DD0a7gCBXELa6gL1J2Pb5EYuaQR0r1Cxfip0PPkzwDNN35ZmCx3lf8_c9WzAPI688VM5CDbsloRG9gb3hVf3WifNBTsUWgqtqw5U00szsUqGJR90HN0tObdKsHYtthUtq3rbaz52pVClqMLDgLUdjCjhmHqTbPhHj5POsINwCI_kGWxbfSXJ-E4Dvp41pd9uvmQiGCvzIvE5EHwAKSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور علی اصغر حجازی، قائم مقام دفتر رهبر شهید در مراسم تشییع و تدفین رهبر مسلمانان جهان در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669316" target="_blank">📅 00:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669315">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f920723e4a.mp4?token=Pnr8BpE3N-i6dnjSbeVljOaozw_MUQclkKuUyUxHVdoj0_VyBcTZcI8cVKzs4oLPDA2uygqDJQNjr7_XzYhxfLBlThdbxHKqkTQa4de4xrIJ_QhJ9csyIoaGXCRwSGX_IoB_xzbxmF0ePj85XwI9w4mmPaIFG730OAFprrKxNWVtrEnI_EfEFyK8niKmL5of_3mmwKclE4S2g6fDXKEsh4Irz5ILOqX45mP70m3jeCIkW7D-FqGEp_Gi0bVeXF-WNIcu9e-BmPIzJ0LOSog9NH3VJO7wPMGxglWFsquO7tNkc1GWog0olVf2Abotv47Qqpaxm0TDIWEXgIdYMJ1GBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f920723e4a.mp4?token=Pnr8BpE3N-i6dnjSbeVljOaozw_MUQclkKuUyUxHVdoj0_VyBcTZcI8cVKzs4oLPDA2uygqDJQNjr7_XzYhxfLBlThdbxHKqkTQa4de4xrIJ_QhJ9csyIoaGXCRwSGX_IoB_xzbxmF0ePj85XwI9w4mmPaIFG730OAFprrKxNWVtrEnI_EfEFyK8niKmL5of_3mmwKclE4S2g6fDXKEsh4Irz5ILOqX45mP70m3jeCIkW7D-FqGEp_Gi0bVeXF-WNIcu9e-BmPIzJ0LOSog9NH3VJO7wPMGxglWFsquO7tNkc1GWog0olVf2Abotv47Qqpaxm0TDIWEXgIdYMJ1GBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مهار پنالتی امباپه توسط یاسین بونو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/669315" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669314">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3FXIYE2aLtwZvP8ndygRl1OEpDqq4WrCh5HwEJiigg2Nk-7bX0BprBv1XpCmmADQkd26ZA0tOMHyKmQ6xy57LQgtVTuzeLmXQVB2EZpb-6eedhDFm1QGcY6rqfNKn8hMuOJWWjXjd84qc-JGpijOdhE4Y7d3AdSGiCtEsy1rXSr1sb4eNYeS2NzOr0QcU1zQ-EM-438jN7AsmWwIFobm-SYW9oY9NVY3cGjI4J1UmApi7ovsvEIdHYJz48HoEhSsg6ts804Lf8Zb58rBiW-GcE_d2gXI_Yb0cMkcJl0NmQkCp-Oynt5KKvYiKvO8UzQBJo0KjTjLblb4jk6VFvoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار | شروع مجدد جنگ و نوسان شدید طلا
⚠️
در جنگ دوازده روزه و هم در جنگ چهل روزه طلا ریزش بسیار شدیدی را تجربه کرد
❗️
این دفعه مجدد جنگ شروع بشود آیا قیمت طلا به گرمی
1
4
میلیون می‌رسد و دوباره قمیت
ملک
شدیداً رشد می‌کند؟
تحلیل تخصصی منتشر شد!! روی لینک زیر کلیک کن و تحلیل رو ببین تا دوباره ضرر نکنی.
⬇️
⬇️
⬇️
دریافت رایگان تحلیل طلا و ملک</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/669314" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669313">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3SvtjCnCo5R8iZPTiNusxgpOZj-pz6tRtH5voJTYJgA_IdmF7elDIGJujcDv9hP3Nbzhs24Kyoe25weTsrl76cXCwRC_DW_O6uB1ViAfhwyh-LVfk9fMPj0eUkFUMLU4sB-g5jaTzUbESGzixcp3hSgPGq3M87yMl66stgBDzs_7sKXU5qLBv0lyIwiRQD53NLbKASEII_XEoJ6NxYeqXl9sqX5j1gUUXa-yiSmiQoN07x58-kBWzufqLCZTsFlIen0aP9Z_HA7BH4NAj9B_bPKjxzCbVhsNUAtyU9krGLcZzwu2dJCAiM6tqqa-VUDm1Ff_InY56x3dv2iMXjaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669313" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669312">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-text">📢
به اطلاع ملت بزرگ ایران و امّت اسلامی میرساند:
▪️
پس از مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی اعلی‌الله‌مقامه‌الشریف در مشهد مقدس و اقامه‌ی نماز بر پیکر ایشان در صحن پیامبر اعظم صلوات‌الله‌علیه‌وآله،
هم‌اکنون برنامه‌ی وداع خانواده مکرم رهبر شهید انقلاب با پیکر مطهر ایشان در حال برگزاری است و هنوز تدفین پیکر مطهر هنوز انجام نشده است.
👈
پس از انجام تدفین پیکر مطهر، اطلاع‌رسانی لازم برای انجام اعمال و نماز لیلةالدفن از رسانه‌ی
KHAMENEI.IR
انجام خواهد شد.
🏴
#باید_برخاست
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669312" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669311">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
فرماندار کنارک: منطقه نظامی نیروی دریایی در دو مرحله هدف حمله دشمن قرار
گرفته است
فرماندار
کنارک
:
🔹
منطقه نظامی نیروی دریایی شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.
🔹
دستگاه‌های مسئول، نیروهای امدادی و نیروهای امنیتی بلافاصله در محل حادثه حاضر شدند و بررسی ابعاد و جزئیات این حمله در دستور کار قرار دارد./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669311" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669310">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
عربستان به‌دنبال حذف اسرائیل از کریدور آیمک
شبکه عبری‌زبان «آی۲۴»:
🔹
عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند-خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/669310" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669309">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
فارس: اولین برآوردها از میزان شرکت‌کنندگان در تشییع رهبر شهید انقلاب ۴۱ تا ۴۳ میلیون نفر است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669309" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669308">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09749751ad.mp4?token=YDIoXYkMUoSQZqBFXMqp288OegGWS2njIsiWXuSTy2l-hUCMe_Pu4PmiIg711-axm0VLH7wd9POrkEoh7jw3yi3X1FALZnz9DEujuHG9sAcxmo2sCzoilPxSwfWiaAs2t7rRFGekHNtZeVPxEqE6Ge0rI6ST9vt0a3gR_ZIDWniNA1DG48GBvNWRGI5BXtdhi04CUGpJvJl4mKYCLqMmpV8fbxQEluOPkzwT6mjItpDMfOkWgp-LEukmEd8iWpuo2ypQpOYHguG377VfIgQ0R_QEkQez1DkcV5et49dB1LZgutvt4Of_Quv-YeljE1KhG__rhUrZHqXytveiKWGbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09749751ad.mp4?token=YDIoXYkMUoSQZqBFXMqp288OegGWS2njIsiWXuSTy2l-hUCMe_Pu4PmiIg711-axm0VLH7wd9POrkEoh7jw3yi3X1FALZnz9DEujuHG9sAcxmo2sCzoilPxSwfWiaAs2t7rRFGekHNtZeVPxEqE6Ge0rI6ST9vt0a3gR_ZIDWniNA1DG48GBvNWRGI5BXtdhi04CUGpJvJl4mKYCLqMmpV8fbxQEluOPkzwT6mjItpDMfOkWgp-LEukmEd8iWpuo2ypQpOYHguG377VfIgQ0R_QEkQez1DkcV5et49dB1LZgutvt4Of_Quv-YeljE1KhG__rhUrZHqXytveiKWGbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا دقایقی دیگر خانواده با رهبر شهید وداع می‌کنند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669308" target="_blank">📅 23:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669307">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa04b01c83.mp4?token=n1LE8ox3occzNcfS-Nk5T6NeA1JETjo2ljv9bLi_M8dDpzbDUs-GNS4IUWfAlCF9VzG6ni11KGArd1hO288w-_gb_nGQF3PAiV6IkVUSJ0cAZ5CDtj_ZkaFAUblSa-v6s92Truk7DCvzlcbPIRqABhDXNcnNXODpD6xSi2mm6DHYn1AmZJm9kIHnaAklRC4AuizvyyefX0_UscZi2yf58vd_LGeywf14-9Ck6F_WDofMi7UoIxZR3LaykH2LYIdY45mdM-pWMkOFhCnyNerPuiQrOMcDPzpyG3Bfz3ts04Y8NkKxUAssWM3IiMO4Gl4-450pvbln7Ha0kgVQrPcIJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa04b01c83.mp4?token=n1LE8ox3occzNcfS-Nk5T6NeA1JETjo2ljv9bLi_M8dDpzbDUs-GNS4IUWfAlCF9VzG6ni11KGArd1hO288w-_gb_nGQF3PAiV6IkVUSJ0cAZ5CDtj_ZkaFAUblSa-v6s92Truk7DCvzlcbPIRqABhDXNcnNXODpD6xSi2mm6DHYn1AmZJm9kIHnaAklRC4AuizvyyefX0_UscZi2yf58vd_LGeywf14-9Ck6F_WDofMi7UoIxZR3LaykH2LYIdY45mdM-pWMkOFhCnyNerPuiQrOMcDPzpyG3Bfz3ts04Y8NkKxUAssWM3IiMO4Gl4-450pvbln7Ha0kgVQrPcIJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#باید_برخاست
♦️
در مسیر وداع با رهبر شهید ایران، آتش‌نشانان مشهد با دل‌هایی داغدار و دستانی خدمتگزار، گرمای راه را از زائران گرفتند تا سهمشان از این بدرقه باشکوه، خدمت بی‌منت باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669307" target="_blank">📅 23:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669306">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4ee86ff9.mp4?token=FSk7y8LIB95sMOERsaCeGpkxzGsMbv8vPDJXtdwQkcIhNjeO_vONi5QJfsdrAjiEv1D08UpZjkP-U8of-ovAKPnQcCx_8qkKHeRAst2eueNoLODZ5CRrkRBBIJI47M49bWGK7Hs6FiPZRtgLXtq_8v7sEWHQvTTn9n3VFMK-vPyzKmZBhulUjgzJDuxGcgf-8M23bBTjPGEs2sUrt65nCJaoLmo-KDfFjw8z26CsMGugBlxS-NI0bDR4_sp4eZFzsH52JUs9HGfAIyvCoXVL1X3JpFN6mcszmyzfwmUW6XnUk5cU1urG28sWN_y-BDaaa-r3eZKh91o4Mkzwq3YZZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4ee86ff9.mp4?token=FSk7y8LIB95sMOERsaCeGpkxzGsMbv8vPDJXtdwQkcIhNjeO_vONi5QJfsdrAjiEv1D08UpZjkP-U8of-ovAKPnQcCx_8qkKHeRAst2eueNoLODZ5CRrkRBBIJI47M49bWGK7Hs6FiPZRtgLXtq_8v7sEWHQvTTn9n3VFMK-vPyzKmZBhulUjgzJDuxGcgf-8M23bBTjPGEs2sUrt65nCJaoLmo-KDfFjw8z26CsMGugBlxS-NI0bDR4_sp4eZFzsH52JUs9HGfAIyvCoXVL1X3JpFN6mcszmyzfwmUW6XnUk5cU1urG28sWN_y-BDaaa-r3eZKh91o4Mkzwq3YZZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار کشتن ترامپ هم‌اکنون در اجتماع شام غریبان رهبر شهید انقلاب در میدان احمدآباد مشهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669306" target="_blank">📅 23:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669305">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
نماز بر پیکر آقای شهید ایران به امامت فرزند ایشان
👇
khabarfoori.com/fa/tiny/news-3228909
🔹
صدای انفجار در چند شهر جنوبی ایران؛ آمریکا: ما نبودیم
👇
khabarfoori.com/fa/tiny/news-3229100
🔹
تصاویر از داخل خانه رهبر شهید
👇
khabarfoori.com/fa/tiny/news-3229045
🔹
وفاداری هالند به نامزدش، زبان‌زد دنیا شد/ عکس
👇
khabarfoori.com/fa/tiny/news-3229043
🔹
توهین‌های ترامپ دوباره احمدی‌نژاد را وایرال کرد
👇
khabarfoori.com/fa/tiny/news-3229101
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669305" target="_blank">📅 23:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669304">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نتانیاهو: جنگ هنوز به‌طور کامل تمام نشده و اسرائیل برای هر سناریویی آمادگی کامل دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669304" target="_blank">📅 23:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
نتانیاهو با خوک زرد تماس گرفت
دفتر نتانیاهو:
🔹
نخست‌وزیر و رئیس‌جمهور آمریکا در یک تماس تلفنی، در چارچوب ارتباطات مستمر، با یکدیگر گفتگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669303" target="_blank">📅 23:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سناتور دموکرات: تصرف خارگ خطر از دست رفتن صدها سرباز آمریکایی را همراه دارد
کریس کونز:
🔹
تصرف جزیرهٔ خارک برای ایالات متحده بسیار دشوار خواهد بود، زیرا خطر از دست دادن صدها سرباز وجود دارد، چرا که این جزیره در گوشهٔ شمال‌غربی خلیج‌فارس، نزدیک به ایران قرار دارد، و ما باید درگیری سنگینی را انجام دهیم و جان بسیاری را به خطر بیندازیم تا بتوانیم جزیرهٔ خارگ را تصرف کنیم. /سی‌ان‌ان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/669302" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2b858c81.mp4?token=ioplanmGPR-1rQMuJnp6N_hlSYrlNQgbh2Yc_6CK0ybjsAw9D861bmyHb1kUh3ZTkbeYj6rvf6-2tGzmn_8uUe2uJf05GE1gjleO4_iAeM7Nox9N3Wc8gVFBDl5ReE6PH0XhTn6iamt3_zFXbL90DlE-2QAYLE3eppC3Dx279aSNc1zdoEizdKASqovnHTylFYaowk6IvEeTT9nEij2uSawdBEAW7id_XySu7Hys3U97oWVMCnkhAivfdrSo2wgVkeM6J9nczH26zePnAGA5pGKDBBVa5UTuUo5xORFw1GEoN4QTUvrGxVu9J47ZM7w8K9VB2SuGYwAg7rqQ-UxNCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2b858c81.mp4?token=ioplanmGPR-1rQMuJnp6N_hlSYrlNQgbh2Yc_6CK0ybjsAw9D861bmyHb1kUh3ZTkbeYj6rvf6-2tGzmn_8uUe2uJf05GE1gjleO4_iAeM7Nox9N3Wc8gVFBDl5ReE6PH0XhTn6iamt3_zFXbL90DlE-2QAYLE3eppC3Dx279aSNc1zdoEizdKASqovnHTylFYaowk6IvEeTT9nEij2uSawdBEAW7id_XySu7Hys3U97oWVMCnkhAivfdrSo2wgVkeM6J9nczH26zePnAGA5pGKDBBVa5UTuUo5xORFw1GEoN4QTUvrGxVu9J47ZM7w8K9VB2SuGYwAg7rqQ-UxNCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون رونمایی از لگوی غول‌آسای ترامپ در مراسم شام غریبان قائد امت در میدان احمدآباد مشهد @AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/669301" target="_blank">📅 23:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
صداوسیما: اقامۀ نماز لیلةالدفن پس از خاکسپاری پیکر شهدا انجام خواهد شد
🔹
به محض خاکسپاری پیکر مطهر رهبر شهید ایران و شهدای خانواده ایشان، اطلاع رسانی می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669300" target="_blank">📅 23:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvFwVBc71ynneEj3lWl8Rjw0zKF3fuqo06G3SMVCQ2j0AT5WskmEs12HyR1cAUDT7nfUaOyiIM-ZY2Nm7tcce9uMtMYYg7EbxEm_j0moZDG9RsVRzZfQ9I0fIpC3OaYpa4ahr0cWFwtet7EFLhqgEXzz08qnTlAvtlWK_bFPauokbQhkwW77-Iq_3uezOv48x51Ej05SEo_GoE1TmEccfmsABuzPuSaKK4YIG08lMU4C2vCMazDB3pR0eWfLhtGlOjSJr8VVP75awIot4nkly048IEkdt-c0EYfKFTRoEZ39b9Zhntd_k77FVMQhoq6qHxueKQqG9V3Q1hXOXiXgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/669299" target="_blank">📅 23:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/votheEcISiXDMpSMOGw74WQ1IBmB5G9cXdN194b7noIEQK0GzdDPSL30Cr01wIpMyunYNFYpsumEzXJiLEgnjWFQ5_qub6FxADyvixqdjvCtX8wmU8tEZ_wXMuXZiyY6fXUJTTXhWGdsaH88hEdLrt5jmHYrXKgnymkJzG4YKw3pdBho5YtdTXav9Ma-5MEw7vWQKJ0w5oRuEsbbq2A-g9PWMQV3EhOrT2zwuKyoGuNpVE3QLvGBCTlkEo487Y-bCSn_tcvk_Ob9mvJJoYJQW4Mn2u5GbflUFaXVULfvoTj5Y2iB7UGOX1xeBpKgNMuFhLHbBPN4dJUHUra7rieaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب جهانی تشییع ابرمرد شهید تاریخ
خبرگزاری پرس تراست هند:
🔹
ایرانیان با چشمانی اشکبار در مشهد برای آخرین بار با آیت‌الله علی خامنه‌ای، رهبر شهید، وداع کردند
.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/669298" target="_blank">📅 23:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669294">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d4f26adf.mp4?token=WeEFHeVwuEPhebrmX-ejU4aFGFLCq3q-4ZAc_xXH_u2wE_xcZnc1mCscwUrb7_DYrIMXoVD49_vzjYtWaKi1qYftfCMgHO6MCtKps8ssrIo0dq5Lw0d8boywPdEC-HE8JGnbVmKAB9ygK3daR5smbgV3A0PUadbttzs67EWArFYsDCLu6rhnDXXgzUumVGauG1SMWJbXyQCnDk1JV_o85ZIUxOhjfffgGUqSxqPWMmVV7SZZjqxWwRSJSVzh-hsxP40XFUK6m6bkI03bwwuFqZXa0d7GXaQIbOXUttDqIffdUMdefOUaRmr1lP1K7NwLmeQu7dwr9-adMDodMtoEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d4f26adf.mp4?token=WeEFHeVwuEPhebrmX-ejU4aFGFLCq3q-4ZAc_xXH_u2wE_xcZnc1mCscwUrb7_DYrIMXoVD49_vzjYtWaKi1qYftfCMgHO6MCtKps8ssrIo0dq5Lw0d8boywPdEC-HE8JGnbVmKAB9ygK3daR5smbgV3A0PUadbttzs67EWArFYsDCLu6rhnDXXgzUumVGauG1SMWJbXyQCnDk1JV_o85ZIUxOhjfffgGUqSxqPWMmVV7SZZjqxWwRSJSVzh-hsxP40XFUK6m6bkI03bwwuFqZXa0d7GXaQIbOXUttDqIffdUMdefOUaRmr1lP1K7NwLmeQu7dwr9-adMDodMtoEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مراسم شام غریبان امام شهید با حضور پرشور مردم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669294" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669293">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7XgBfjo2DhUYLCy6vH6EmuiXyIKVopXr2CJa5M-Cg1AQiP3dlGWw2px-v1iAWzlZAueY042npEwUn62RatFP_i4yQiteDf0tfDnKcsTpfsDaBMFFtGSDE_vEIFUKrCLOPt_fnTV4UDUbzq83rG_U5lwqRrpAPLlOjA0oDpGwIjEvT7RhEMiV64q-euYY9TbBscFmd4lkQFL_ba3te5XNXAGM5R53RGN-LAQYFRzmOQM1fACyjscqYxwc7pgc-ZZ6fsLOP4ph-E_nkGWAUziUpaxxdV8k4QEIdmxBPwBhWT4eQZJx654_hW6SQzB4AYRas55mGLmCDpTjLHf11JS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آستانه برگزاری آیین باشکوه تشییع پیکر مطهر رهبر شهید انقلاب صورت گرفت
🔹
فعالیت فروشگاه‌های «شهرما» برای تأمین اقلام اساسی و معیشتی زائران و مجاوران در مشهد مقدس
🔹
هم‌زمان با آماده‌سازی پایتخت معنوی ایران برای وداع تاریخی با پیکر مطهر رهبر شهید انقلاب و تشرف خیل عظیم دلدادگان به مشهدالرضا (ع)، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد ظرفیت زنجیره فروشگاهی «شهرما» را برای عرضه گسترده و تسهیل در تأمین مایحتاج ضروری زائران و مجاوران فعال کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد: «با توجه به حضور پرشور و گسترده عزاداران در پهنه کلان‌شهر مشهد، ۱۴ فروشگاه “شهرما” در سطح شهر با هدف عرضه کالاهای اساسی و تأمین ارزاق عمومی زائران و مجاوران، تمهیدات ویژه‌ای را در دستور کار قرار داده‌اند. در همین راستا، به‌منظور رفاه حال بیشتر زائران و مجاوران گرامی، ساعت کاری این فروشگاه‌ها برای خدمت‌رسانی بهتر، از ساعت ۸ صبح الی ۲۲ (۱۰ شب) تنظیم شده است.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/669293" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669292">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منشا صدای انفجار در بوشهر در دست بررسی است
🔹
فرماندار بوشهر ضمن تایید شنیده شدن صدا در بوشهر و چغادک گفت: اینکه صدای شنیده شده از منشا پدافند نیروهای مسلح، اصابت پرتابه دشمن به مناطق یا هدف قرارگرفتن پهپاد دشمن بوده همچنان در دست بررسی است و علت قطعی آن…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669292" target="_blank">📅 22:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMPOWIbFBvFE-tBjS6B3E44ozvF91b30HZoZ5hRbYkz70KLsXA23Bv8mVlKMHiZsGqX9IOXnwnl4FiD2q6lTONy3kXfA2LG8dWuUkABmjHX8nuNLNlg8Mg6jDFxZxbCHGVbuApVHX4zW_pMIJ8QH9QUSKgC-kvGL-5u3dmu9w_9YvRWE_x1cSJPU9d_LMsBu0dK3RweYJpQ4Uc73xwYY2F6peA3fehtKvYcVJpV_qSjTs2L9LY8UHBVLtCONibRGrrvHIr8dWH_Rs-0DBeTmfgeDkjt2rriOA5lnWG_7ibnZt-BonbIA7D6-6Zi3f9ytkgiVzgZ387HvxK9sYkMtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnFX768vRTj1WlQgSNI28EQF_yBITJph8-O3J94wAzpptvcSJl3fnnRMwflnbFphVBVbKynZXcOjU9QJ11SOluMC4fwwUVHCFRFM2tZYUsdvM3ZULDiRTLxzxrn5y2HP8pL08USlEqjtbTLnR-HyFchnvTF4t8C7hQ8iP3VMcO_HIQt36tji954YsBlv_n-ZF_vyqwgJV7-kBP1qqipTh7SRGOYu2iTHk_9F7i7CzgKJIVDUAP3CT30taUUrzYh8aF6dOH0St1DAs5DD4c6F4Q9vgD4_OLIm9SZmG57eifrT8e6Xo1K7bP4txTRY9xEFXkttIY50Pi-hRayEMiH5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkwfe_ox0wecmR-oPLKHLn6B22bTrsMqs-xXoFSxNnhyAPuAe3mwFR65QdZyr1JueI77LGTHl_Jlo-McSk6eEs23niOfNhUFOhzpqQyb7y_Qnd2-70HKa06jGjs3tWI6makdOY2cDXtrCKWo2HPxvN4ZyMX_4khSBdphTOSOLf8BTfDBBIFgguEgXt7hlLrJntSjK_qvCXRqlLXuLP_f0mjQd_JLCdozQeDhaVrJF_rfzv6NT7VpAHVal0v5jg10bNc-eG3p-_hRHKEj1jzl3zZ2u8EMotRgxJ65hYWJoGMScjLrG0CWM8pTbiLsFBhuPeIN6R2Ko9ulHYlRgwmM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dp-GIDMUtapJCZ_KJmaH_4_uiVx-UVw2tp1DD9TEVHDfNhCkrXdxG5BEwa1HgaQcsd0ItmGg-C9Bt3j5L5kOLVLXGBqyY3JcKn7kxDb8KkX_qrhoqbiZCYIMTb4y2WqOmsEHuLAptmM_Wz4fJWILyMFdxUnT_HytQsQUtn-BlsEGlDVzHZyNnlLIMN2oumz89A_C2qWaCbtGAzOPzT3Q8p0SAVNfqQC4sDt4QzzfjHeGBPDYMJRHLtV1Oo4ZePKA3YGwG6W2MiWVApDhAcsLG_17SaT7sWrtg4wSuSBpL_FhXdU83vQVGXeTfxUGZiEU33TrUzAsTg5lcxuiIq-xSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGZTeY1JBdjZZI_LFOKfmHSi1LIj13D_IgRiSYyOWM1TivJh9VU1RsVpW62bvvwYOUvjiwknWJKJEq68PD7Hra9nm0eL-ZAE_rKJ4jnHtMDmxf4RhX7J8N9qWLCQUatZmCgiH_ryQEkvS8-iS5jq2pBfZeyLw7qx8c5eX47j7W5MRG-7MU_P451b_3Cw7w3tVnps-pACr-qasXnH973By9avn-l2EXLQ0saq40OD4jc8nWKuDOEfr7IBkCZv0FmOMsiAbUPmr0kq-l2oNlp3KpxMlyVU0R6zCtMyXiAqcJq_AUzDTK2sJ3w7hFl2J24tAL-JSx3-OzdIsK_4Xy6SEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_0eUo6xLyvwels_Kq91oEL8d9nSbFJrr002YXRG_T_xzksSjCVpeQazW_ev_-Ao8b7YHGfkAn34Nk64010VBmHa4CVbLUu_s7dKkFz8RNtSqSCDuZaNKbG4CPqlYEje0ZBgZcZL7o63T5SiN-kb7dLmzUnDBW37A6_TBWNhIbtJKm6uAtKHsZK8m8hSY97b9USV5miER8YDlRTKh5QWmXrqnoB623YDqZMC2VaaEGWDvAZ0tnoEfk87Pm3d4mj8pwBpKw4pS59pyp3RL_99Qvj3erga5jXXyYtegvSDD0MZ7G-_1yNsI3AAqUsHmmn-WKn1IG4YfSQSnLdPwdRKnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هوایی «سی‌ان‌ان‌تُرک» از وداع باشکوه مردم ایران با رهبر آزادگان جهان در مشهد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/669286" target="_blank">📅 22:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE6D4HjkClPtJApYgthjtKOb--WyEQiOc2r0kg5YtxsDgvWE3yWiIbilB6lCrfjgr0avsM235qYsyIWMCMkpcTlyLFdZ9NndhXt8YauYFF4ewMJ3qyOqAPTxDUOGCllvE0qPNpLWxJyccg0f1GHmG5FCsQQ4zRi2xWnm0iMyDRNNA7ShPwvyu-yQkzIPZlnbQGo1JsdenGMUyD9Ez-z0A7ss7dq2T0Ties1Q99LawN0OXARiq-Rrs_gG6ecbmA-XPWBNdEOa0qmgUxOyAAJQBdQy7fZtJoITWZeIuM7tLFAtp-b__dQGHevZHEJJf55JaX8Rxmmupchg4AwrLXB5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ ایران به بیانیه ناتو: اتهامات درباره برنامه هسته‌ای و تنگه هرمز مردود است
🔹
در این بیانیه تأکید شده است که برنامه هسته‌ای ایران کاملاً صلح‌آمیز بوده و ایران به‌عنوان عضو معاهده منع گسترش سلاح‌های هسته‌ای (NPT)، بارها اعلام کرده سلاح هسته‌ای هیچ جایگاهی در دکترین دفاعی کشور ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/669285" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d897623a.mp4?token=DytYjxDcxQzWq6HLzw0vUbOotWfNcpnBi-zn5DHKd-WOUrjJ9_LZ-lvrOnoPJ5evM5wmeiIQKj3a3qUO-Pn3NM4fT0WkLb2xHoQzF62rHwjKYCpMXPlaW-CGMFa0ObCVo9RnKb4fVIk3cynu2AC7rpmD7FHwWdXeBryKa5ilwn3vpVcYP604PK2rBascKQvjvohniiP4lGQDpW-8kDbvLoMytb6kZ9YXR0IFZPJgNUJKgl6SH_E2rQ44u5A8ygrZKKC9Z5nXQRWc8B2czdGzt3nWSBxrMVplvo2OSqeW5z7eTIk4AIliEof8AEgzLRA6Y2tUIDGYySsNBHLHdj3Yag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d897623a.mp4?token=DytYjxDcxQzWq6HLzw0vUbOotWfNcpnBi-zn5DHKd-WOUrjJ9_LZ-lvrOnoPJ5evM5wmeiIQKj3a3qUO-Pn3NM4fT0WkLb2xHoQzF62rHwjKYCpMXPlaW-CGMFa0ObCVo9RnKb4fVIk3cynu2AC7rpmD7FHwWdXeBryKa5ilwn3vpVcYP604PK2rBascKQvjvohniiP4lGQDpW-8kDbvLoMytb6kZ9YXR0IFZPJgNUJKgl6SH_E2rQ44u5A8ygrZKKC9Z5nXQRWc8B2czdGzt3nWSBxrMVplvo2OSqeW5z7eTIk4AIliEof8AEgzLRA6Y2tUIDGYySsNBHLHdj3Yag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شام غریبان رهبر شهید در خیابان‌های مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669284" target="_blank">📅 22:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH3fRyXUdKlFoJdXeKGQdZZqOmFJkDhNwR-LJz3mxdYzUPMXHFMEgCyUzMkkCF2C-M2BH4Y0aNcfURX7owmQU8XBl3Bo8soPXRc5q2ge1M-a7CBJ3CKbBQ58EbFflNGvuGjSSOyFKJaziT9tErwz9nGuli9h9B9MA5fQLYzuAvbMaHW_RcdQQh6lCBugfSj6LYhBctttlr4n67UUfaPhGSSFuhTTcOBfwB1kS-PblUFrZtvMcnOMljJpEkCuW5kSwrlXfCCqei6mx6f_LE9Oq6fa0SmEbX_3VfisJ8UItu2nq7K7ZIBcFz0yUu0q-MkYVXSTAv-hDy_AN2rbMPA0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاودانه شد
🔹
تشییع باشکوه پیکر رهبر شهید انقلاب در میان خیل عظیم زائران و مجاوران حرم مطهر امام رضا(ع) در مشهد، صحنه‌ای ماندگار و تاریخی را رقم زد؛ آیینی که در حافظه ملت ایران جاودانه خواهد ماند. این مراسم در شرایطی برگزار شد که هم‌زمان، آمریکا بار دیگر حملات جنایتکارانه خود را از سر گرفته بود، اما این اقدامات نتوانست از شکوه بدرقه مردمی بکاهد. اکنون با آرام گرفتن پیکر رهبر شهید در جوار حضرت علی‌بن موسی‌الرضا(ع)، نام و راه ایشان نیز در کنار این بارگاه نورانی، به نمادی از ایثار، مقاومت و ماندگاری در تاریخ انقلاب اسلامی تبدیل شده و جاودانه شد.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/669283" target="_blank">📅 22:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
صداوسیما: برخلاف برخی خبرهای منتشر شده در  فضای مجازی
،
تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/669282" target="_blank">📅 22:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
♦️
گزارش‌های تایید نشده از وقوع انفجار در اهواز و بوشهر/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/669281" target="_blank">📅 22:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رسانه عربی نایا: احتمالا حملات امشب کار کویت و بحرین است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/669280" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619ccc9a61.mp4?token=J9aUR2gw0HULGPqPIoy1Rc0dsdqTtD8iXgMdPpR1qtJlTGVy42ioCbslcCYNqHMQajBx3OdTzUH4lcd1wgIygaFuQMjOzKREVGloqyI-AElck-I-h1o1tyP6qwMUJPyc6I6BruwRAy06QkQRpIgMoAzCXJeCAOzcb_PZladjG8K8QSbrq9MQLfQrGwCkXkenuxyWenR1osTamCnxg64QD6V-tK8udAeQeJi4aBLhh6a_8fFOsZzxTM2uQY75CrOXiWepouyKm5phrnpqgexvGVvVYtLFvOTW-N6bRYR_QwQxgpnOSXHrNRBBYeJ-BbwtfIKJZV5wJ5agGWcVP9al1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619ccc9a61.mp4?token=J9aUR2gw0HULGPqPIoy1Rc0dsdqTtD8iXgMdPpR1qtJlTGVy42ioCbslcCYNqHMQajBx3OdTzUH4lcd1wgIygaFuQMjOzKREVGloqyI-AElck-I-h1o1tyP6qwMUJPyc6I6BruwRAy06QkQRpIgMoAzCXJeCAOzcb_PZladjG8K8QSbrq9MQLfQrGwCkXkenuxyWenR1osTamCnxg64QD6V-tK8udAeQeJi4aBLhh6a_8fFOsZzxTM2uQY75CrOXiWepouyKm5phrnpqgexvGVvVYtLFvOTW-N6bRYR_QwQxgpnOSXHrNRBBYeJ-BbwtfIKJZV5wJ5agGWcVP9al1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم رضوی در ماتم
🔹
حضور مردم عزادار در حرم رضوی پس از اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/669279" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0fb62bec.mp4?token=khWpIoQXRJBbpxqYHY7ku6tq_EoA-YpqN4u0ChGh7OdPoRS7qKBkMk6a-pyRhn19fI3LnYUUin3wJvaRvFjPM79Pt8tEmdZ7oDcPeJwH9l5cv76hiB21hw3mIr6bmv4DXNZyh3gDaQZW2IfbOUrOdCcBac9Fa9_4-Sq_nj2E06LqVsAt2wW08YbqattrDtc8kx8r-sTms9FlhVz0nMUu6ZwiwM_2pp-Nwq9JSJcAExcc2PDhXVHjyc_5BnYZvMjUsqUFFm2RJtn5H_RFL2Czgtqj0ipO0zr5wFVQ4OnRd7ncMNQq6lUHAq_Cc8CYuetw_1MyZpI_N8H2_ot-9daQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0fb62bec.mp4?token=khWpIoQXRJBbpxqYHY7ku6tq_EoA-YpqN4u0ChGh7OdPoRS7qKBkMk6a-pyRhn19fI3LnYUUin3wJvaRvFjPM79Pt8tEmdZ7oDcPeJwH9l5cv76hiB21hw3mIr6bmv4DXNZyh3gDaQZW2IfbOUrOdCcBac9Fa9_4-Sq_nj2E06LqVsAt2wW08YbqattrDtc8kx8r-sTms9FlhVz0nMUu6ZwiwM_2pp-Nwq9JSJcAExcc2PDhXVHjyc_5BnYZvMjUsqUFFm2RJtn5H_RFL2Czgtqj0ipO0zr5wFVQ4OnRd7ncMNQq6lUHAq_Cc8CYuetw_1MyZpI_N8H2_ot-9daQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون رونمایی از لگوی غول‌آسای ترامپ در مراسم شام غریبان قائد امت در میدان احمدآباد مشهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/669278" target="_blank">📅 22:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
یک مقام آمریکایی به CNN گفته است که ارتش ایالات متحده در حال حاضر مشغول انجام حملات نظامی نیست./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/669277" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/669276" target="_blank">📅 22:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تاکنون دو انفجار در بوشهر و سه انفجار در چابهار شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/669275" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlK04prMMYbXZHFcThXBR3Zio8PUG3E89F1lcG5-C0mY8uj7ym-bE-dGqidrsR_jPUVSufy0c5D_PJmCKlEvM6RsPXR2x6b_JWmoINxsX3uwHEjbuJBUFWwwvja1GWEmd3GDG95Vjc4PU0AkEcrUE7i_yfNOwjViBViyuwlxylNZX1UsulaBKYD-MWQyboN5ZMQbZ1vHfsfVSSWIZxaB-TiUjdkADLSCE37Ov1jAUpdtBlRld61ySj6lS8obQ_Yb5OFg40uvazAgGl7r-6XaZFokcKMfQmysJx1--wLPLKr2Z5mmm8j4tq0gBrCUhSH2TvznvcirRbfo4bcP-rt4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
نماز لیلةالدفن آقای شهیدمان
...
⚫️
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
💬
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
👈
(به جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
📝
اسامی شهدا به همراه نام پدر:
👇
🖤
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
▪️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
▪️
شهید زهرا حداد عادل، نام پدر: غلامعلی
▪️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
▪️
شهید زهرا محمدی گلپایگانی، نام پدر: محمد جواد
🏴
#باید_برخاست
|
نسخه قابل چاپ
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/669274" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-BKpZGVCsFRNwGrRsDs3qzoyOnHDzLGavZWnnKNP3af9zD52hya2fj-0GxRb6rnItx8Qi8l3TWaAeoC220_xWXWVIHkkNk5P9Z_G3Jeb2GKvLvuuG_PoMFFyFiSluxGtajYdi5s1Tx6GzZxeGpAb4AaHMZKSYrftsvkXHZ5-TsJn9UbVU3dsmseOxJW38UEMRlQUBzv_A4i7E5xCc0Q8XCr6vlaD8VlMRI0w2fVgkEhmgGEto7ba5CvaZtYf_zZbFqFsmNucH_66tNwhkRtrzSMbA9jj3AIjwzXmhAigu0sZ8Ko2mrywJYN5mkMvF-BXWk7haynUZN6bIBs7SFD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین پنالتی کسب‌شده در ۲ دوره اخیر جام جهانی
🔹
در ۲ دوره اخیر جام جهانی، ۸ پنالتی به سود آرژانتین اعلام شده و پس از آلبی‌سلسته، انگلیس با ۴ مورد در رده دوم قرار گرفته است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669273" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر «رهبر مسلمانان جهان» حضرت آیت‌الله العظمی سیّدعلی حسینی خامنه‌ای
اعلی‌الله‌مقامه توسط آیت‌الله حاج سیّدمصطفی حسینی خامنه‌ای فرزند ارشد رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669271" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf3479c1a.mp4?token=lw5SAqro2l1G6WQXvyfdBQrfag_QvbncSXM_awP3fkWLgeDB3aOfDW7bc2rHoRY1jeI8bTzhbbVjwXoXLjPQMnooKOMrwAcpYxVyKX_HT-UVmM6D24LbpeLm1QAmL9SLUMQwAxET932vWVbmmb7A1D4-FV1dIqp7dlAFybyVeBdOemxGnMHwrV7yPORBoo7vQGBdMtSYkD_VqlEo46hUK13OSuWTY4j2zEbDRhnRmJX9EFnLqU9FuUgywnXZScCrXPmR1MjEFRz2a5W8jcnotvUj9mCLBTlfd4469RXt-8GbYrYK-V2rIf6GEdzzrnhGHtDre38_MigMNCYrKSq1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf3479c1a.mp4?token=lw5SAqro2l1G6WQXvyfdBQrfag_QvbncSXM_awP3fkWLgeDB3aOfDW7bc2rHoRY1jeI8bTzhbbVjwXoXLjPQMnooKOMrwAcpYxVyKX_HT-UVmM6D24LbpeLm1QAmL9SLUMQwAxET932vWVbmmb7A1D4-FV1dIqp7dlAFybyVeBdOemxGnMHwrV7yPORBoo7vQGBdMtSYkD_VqlEo46hUK13OSuWTY4j2zEbDRhnRmJX9EFnLqU9FuUgywnXZScCrXPmR1MjEFRz2a5W8jcnotvUj9mCLBTlfd4469RXt-8GbYrYK-V2rIf6GEdzzrnhGHtDre38_MigMNCYrKSq1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکر امام شهید بر دستان عزاداران پس از اقامه نماز بر پیکر ایشان در حرم مطهر امام رضا
(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669270" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uisf6GmOfYodrSjX4iF3FF-NkbIyAwuxpuTZ4Ejf3q1S5yFBwqcc6eFlVEVnY7-WP0nrUU-1iYZ0WsF1n1q3kw_PDwFuqOcCBIKNbXeJ4JoLM68CcP5cQL-gsr9wJ55bG4ykDpEpg6iPl0rNHpPSPbhOghxRF38YDW3-F9y2KOXQHJeMQzpzV8QGEdmvV-xVMaEyrm-a35hR3WgLsEjzYtgNB3tKQjK0isjnQnOguFNgZOUWJTCJkQoBFC2u3PxyfTnpdsLq9CDDIQevha23ZEfneNw52DYw1Oqr1wk8AiN3dKAzKd8g5T9nDxUkZYiH4s7bEhAq-QpnzMteswE06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هدف تنظیم بازار و سهولت دسترسی زائران و مجاوران انجام شد؛ آغاز عرضه مستقیم محصولات در ۱۲ جایگاه ویژه میوه و تره‌بار سطح شهر مشهد
🔹
هم‌زمان با ایام حضور گسترده عزاداران در پایتخت معنوی ایران، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد با هدف کنترل قیمت‌ها و حذف واسطه‌ها، طرح عرضه مستقیم میوه و تره‌بار را در ۱۲ جایگاه منتخب سطح شهر آغاز کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، با اشاره به نقش این جایگاه‌ها در تعادل‌بخشی به بازار اظهار داشت: «به‌منظور حمایت از سبد مصرفی خانوار و رفاه حال زائران عزیز در ایام تشییع پیکر مطهر رهبر شهید انقلاب، ۱۲ جایگاه عرضه مستقیم میوه و تره‌بار در نقاط پرتردد و کلیدی شهر مستقر شده‌اند. در این مراکز، محصولات به‌صورت مستقیم و با حذف واسطه‌های غیرضروری عرضه می‌شوند تا ضمن تضمین کیفیت، قیمت نهایی برای مصرف‌کنندگان به‌طور محسوسی کاهش یابد.»
🔹
وی در ادامه با تأکید بر نظارت مستمر بر این ایستگاه‌ها افزود: «این طرح با هدف تنظیم بازار و تسهیل در دسترسی شهروندان به اقلام ضروری طراحی شده است. کارشناسان نظارتی سازمان به‌صورت تمام‌وقت بر روند قیمت‌گذاری و کیفیت محصولات عرضه شده در این جایگاه‌ها نظارت دارند تا اقلام با بهترین شرایط در اختیار عموم قرار گیرد.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669269" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa20e8a52.mp4?token=i2HCsrwjTWIteDsPWj66n2QbhcyaoqjS8KODBu7ud4zu4HaG_CjL9xsVWx2DAdgbmTz4z-7Pt4HG0-dYoatqpK6BmfN3VQ2j_NODHVInJYeNhf-hEYmCOOcsU5u5qHKJ2GDXv4YJn1GBJobh89ROhJEeEVjM9AD_cGyDEQ6O2Zh2HL3l9iFOjtPcVWK0wAh3oavd5GhIddlT-OWlTmF8GrBnnclsv7YkfOhR_7FpbLLwLO4rIpRbmpacU6ZcW4lyi1_s1TOcE4cP64PMjQ-hvK1xtW9s-q_dZvVNAdCERvyrDVQr0MgtrZtHjeGR69lf2pQf8zcbBq-i74ZLwrBkiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa20e8a52.mp4?token=i2HCsrwjTWIteDsPWj66n2QbhcyaoqjS8KODBu7ud4zu4HaG_CjL9xsVWx2DAdgbmTz4z-7Pt4HG0-dYoatqpK6BmfN3VQ2j_NODHVInJYeNhf-hEYmCOOcsU5u5qHKJ2GDXv4YJn1GBJobh89ROhJEeEVjM9AD_cGyDEQ6O2Zh2HL3l9iFOjtPcVWK0wAh3oavd5GhIddlT-OWlTmF8GrBnnclsv7YkfOhR_7FpbLLwLO4rIpRbmpacU6ZcW4lyi1_s1TOcE4cP64PMjQ-hvK1xtW9s-q_dZvVNAdCERvyrDVQr0MgtrZtHjeGR69lf2pQf8zcbBq-i74ZLwrBkiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ آغاز اقامه نماز بر پیکر «آقای شهید ایران» و مرجع عالیقدر شیعیان جهان حضرت آیت‌الله العظمی سیّدعلی حسینی خامنه‌ای توسط آیت‌الله حاج سیدمصطفی حسینی خامنه‌ای در حرم مطهر امام رضا علیه‌السلام #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669267" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjVAP2j9_tRr8wgjSaWJMWVBCNdGtxSwzS0ms3T8QVQRyJF6VUxZtCPX9n-GhMNH9LLqbio64LZwpRzmTxNA7blbAaW-D_E2A0YEDpfD_EESx0klZ2Oe-6lq7fcZHSUxnhgK4FE-OC4_Ttt_Ls8IbFC5jkKTMxJsfRZFOHAYT0ot6aQdiGLM2Hw2QsxoKJSDbQoPvZXYSd35WK218szzw7y7WkqKUbuxb2oGsdLCHmMN9tWQd3PuL3lglt0Dq8tIm0HXyvnl3Wtu0Xb00Hzg0gk_Kju6Hd_JlODxscbIIklB8VyIQcNYVTg62s5-_IcE1_ysXSyaSKE4WeK_fzgvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاده‌ها سالانه جان چند نفر را می‌گیرند؟
🔸
طبق آمار سال ۲۰۲۳، سالانه حدود ۱.۳ میلیون نفر در جهان بر اثر تصادفات جاده‌ای جان می‌بازند؛ رقمی که بیش از ۲ درصد از کل مرگ‌ومیرها را شامل می‌شود.
🔸
در حال حاضر بیشترین سهم قربانیان مربوط به سرنشینان و رانندگان خودروها است.
🔸
در طول سال‌های گذشته، سهم موتورسواران و سرنشینان وسایل نقلیه افزایش یافته، در حالی که سهم عابران پیاده کاهش پیدا کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/669266" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تاکنون انفجاری در خارگ رخ نداده است
🔹
خبرهای منتشر شده در مورد صدای انفجار در خارگ صحت ندارد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/669265" target="_blank">📅 21:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6QA0UCf6RwQnLNkeAhv8fQvLxs5DMp33oeNhdbz6stGqjUOLrUVjCbfrkkJVvWzgl9HVA-Kl2QSCyHAAHvihbWyPINo80RN43DECu3hL9UzTa3tfm5Y08mVWjR0POlU_023CzbgOjKgv2kwo6Nya3AUPtb_Z80sBjZZQ_YVlytmrkchLSXHrcn-dqhVkc50ZZYpIXyUt9NYc2JedNryOyogJcHTHJFdBFh9oJbPV7yuS9I6n3fdEVwH7sfI2Axe_ggr3tSPFNnSFLbelNTEbhZ2RQGG6Ac7UQ4ev_jvurYCvnSFxGY1P4j2syZerUDqKO_gfWXnX0pQC5g4cZv8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعالیت هواگردهای امریکا در جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669264" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
♦️
گزارش‌های تایید نشده از وقوع انفجار در اهواز و بوشهر/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/669263" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a88205b172.mp4?token=P1MT3QshH-hBqJFeRDe6Ug61L4-Oi-0tSeBQRseepfPTlyRUrM8oZ5VpFSbTMv-iBApMSDVMtSLi2owiX9bZ0LXaVssIrLFFvIVkl4R37Gr-EbbGiGzfjqzevr71UkV61NAcAostHQ9mPnb_Zqj9LsB3MwcfvoQasGzjB48kVVE4WL4HF4-nEVOpQnUlUgTyLzgGDU2K30ju85deGEqtNkJeBeM54SACJp6ABLcAwox2J7-kF5BT_5vwOrCoyNTcU7BZkWhjgIHM-JJ1DuEy4FYJiDxvZf54mvLGCdEzk65tjL7fXBuxgzgPjh60qfc6AJ1BHkwKJfS_HsAVWXlxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a88205b172.mp4?token=P1MT3QshH-hBqJFeRDe6Ug61L4-Oi-0tSeBQRseepfPTlyRUrM8oZ5VpFSbTMv-iBApMSDVMtSLi2owiX9bZ0LXaVssIrLFFvIVkl4R37Gr-EbbGiGzfjqzevr71UkV61NAcAostHQ9mPnb_Zqj9LsB3MwcfvoQasGzjB48kVVE4WL4HF4-nEVOpQnUlUgTyLzgGDU2K30ju85deGEqtNkJeBeM54SACJp6ABLcAwox2J7-kF5BT_5vwOrCoyNTcU7BZkWhjgIHM-JJ1DuEy4FYJiDxvZf54mvLGCdEzk65tjL7fXBuxgzgPjh60qfc6AJ1BHkwKJfS_HsAVWXlxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ آغاز اقامه نماز بر پیکر «آقای شهید ایران» و مرجع عالیقدر شیعیان جهان حضرت آیت‌الله العظمی سیّدعلی حسینی خامنه‌ای توسط آیت‌الله حاج سیدمصطفی حسینی خامنه‌ای در حرم مطهر امام رضا علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669262" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFBiyPHHszBmn0yZ3FK9cLhgsWmrjbIbtagqdzBS-Smctm97mSKgQH1vsRFTjY81rmTwRlyjHZN6pn8rIyNsLGVZsHkd5dMJtGzOQ3Gpgb_-jdcZoHnI6uMVFkx4NrFoiegoPmBaaeEfLDRVsnXEYuXhZI3n77M11ErGgoakaNuzVnFD-nsY0xjQbqvOapH57tnLET1yZIDEhwsM5H_VQibwGEyY81g1RrQnWQP-4QHP6uqYKMQKVDemSap1vf3HR7II06bpzuauZjtBcLH1WRGk02MD5MU5vcN3QAcfKh1Y25bYtK3ytnlr5nuoD4nu9v_aZFMLMToVcPUA57JqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از فرزند ارشد رهبر شهید انقلاب در حرم رضوی #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669261" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
شنیده شدن سه انفجار در کنارک
🔹
دقایق قبل سه انفجار  در کنارک شنیده شد.
🔹
از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست. /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669259" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
♦️
گزارش‌های تایید نشده از وقوع انفجار در اهواز و بوشهر
/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/669258" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naSYNeKYn8jis0zDjCHdP563Vgh23PuNb8SucKbd-LXtN0eHb2k8TnhdcINvp2mwCU5Z1RmQLTcpEdwyVRxJ608t6vmEQ3vylNPVZhFGCl8lt8bySXsL-L43P-tfZVKDjWPut3RZvfpuSa1rcNtTxBLOeYJGpN5kSMwXpTpbLM1QhufOZRQ1lJO-9UBYtW7OTy8xJ8bmo_dBom8I2BJetWbp0o6HsAV7F2Hm8ormvk5c2kRjBBqyepT0zevNuUuSj9a7yY5eubztp128X0Mg9-rSksvsVYqF59RtWz6Q6jZjBoNQPweO-yJllRZ-lQC45I2k-3AOPXuhk-nvR3o9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری مصطفی راغب خواننده درباره تشییع امروز رهبر آزادگان جهان در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/669257" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4473819833.mp4?token=CpiV-zzfTt-yEsl9uON-VKAxGGEJhnK3zCOYge4-eX92L_oXPSr5rfCQ2GlI2s826umArJFdhmAitZjWlSlGZRFSv-jnrvrqgCYbyfymJ8KWaCT9RnkkbGSffplVjYNaLxwvqfs98g5SKYICCk8fMpfyh0pSrslgA2h7RiBaqQjWyye2b_a2GgBk54uBWYMVvC4ttv8FtAGlXKuToJ0gjdvh0YnjH2uaTEQNuJzXa9CzaiNsrnJIk-DG6BC5cQaX0DKCpd_dsM1VLWuG_KQI5WtP5GKFR9Co8IrxwmkB_w5oZPdBI9GSrc299fNNBML5wwgiFiYKheIIOLmODpefoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4473819833.mp4?token=CpiV-zzfTt-yEsl9uON-VKAxGGEJhnK3zCOYge4-eX92L_oXPSr5rfCQ2GlI2s826umArJFdhmAitZjWlSlGZRFSv-jnrvrqgCYbyfymJ8KWaCT9RnkkbGSffplVjYNaLxwvqfs98g5SKYICCk8fMpfyh0pSrslgA2h7RiBaqQjWyye2b_a2GgBk54uBWYMVvC4ttv8FtAGlXKuToJ0gjdvh0YnjH2uaTEQNuJzXa9CzaiNsrnJIk-DG6BC5cQaX0DKCpd_dsM1VLWuG_KQI5WtP5GKFR9Co8IrxwmkB_w5oZPdBI9GSrc299fNNBML5wwgiFiYKheIIOLmODpefoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از فرزند ارشد رهبر شهید انقلاب در حرم رضوی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669256" target="_blank">📅 21:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669255">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پیکر‌ امام شهید تا لحظاتی دیگر وارد صحن پیامبر اعظم میشود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669255" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669254">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fd2cb492.mp4?token=bkwhh9Ly8N1qUiQf0HYg1ByB6SewB1SQkCU445ihXSK_QdPzFNdIeNwceBflVZ-Ag7a1mCipUFLaqGjg9xQuzq31Pd1pEQG2vaJFzeoDqW5CpLbnvveOxvWRMqHssmspbgxOG98boIBvNvO0hwpBeoOhgIiqHiDMr-NoZxk3v0CgwP5xtiQ-kFWf25x6JuNsmkpD3qQYWqcuu_J0iPJ64F9ptT3xOakzQbsx1_rZ-xJIailhOeV7aXlN3YvP3xlbFPn5GR_KY_5P9AwQZ9n_7oBgjr0c3VljDbsvXERatuI4_U97f52v5zQi9jTjKdlQWe08QGXM6d0BFOu6MNpe5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fd2cb492.mp4?token=bkwhh9Ly8N1qUiQf0HYg1ByB6SewB1SQkCU445ihXSK_QdPzFNdIeNwceBflVZ-Ag7a1mCipUFLaqGjg9xQuzq31Pd1pEQG2vaJFzeoDqW5CpLbnvveOxvWRMqHssmspbgxOG98boIBvNvO0hwpBeoOhgIiqHiDMr-NoZxk3v0CgwP5xtiQ-kFWf25x6JuNsmkpD3qQYWqcuu_J0iPJ64F9ptT3xOakzQbsx1_rZ-xJIailhOeV7aXlN3YvP3xlbFPn5GR_KY_5P9AwQZ9n_7oBgjr0c3VljDbsvXERatuI4_U97f52v5zQi9jTjKdlQWe08QGXM6d0BFOu6MNpe5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من بهت قول ميدم دخترت به‌زودی بیوه بشه!
قسمت چهاردهم سریال
#بدنام
“آغاز جدال” فردا ساعت ۸ صبح، به‌صورت اختصاصی در فیلیمو
بدنام، جمعه‌ها به‌صورت اختصاصی در
#فیلیمو
کارگردان: احسان سجادی حسینی
@filimo</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/669254" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669253">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFphaU1YUtBGcI4rpOTLoSNfJSmW_SaRnNaWHog4GnSU8mmNw0Hd30ONYuh_Bsx-euqPNUJr-2rBrNygYdsJGYhoWWtroDEGfTUi0x0Lw_aiR5tnahX_OVyXV68JK4Khfp8oXpLxg49w2CPHHGCInDkvF1ODlfd6pxQ5tbbYnHBmhND9nLHvkBt_Y5les1NFXa0-MDvPmysuKWElmZBfqvVErrafblO5myGpZs8C24v4UHFR_e7v_tmTmsZI_DxdITRQ0nG7mBEQuMZqXDojkpQit7X_0z_nEtRjYOFMUiDey1IdanhcXQ9vePC1RyaSPD2OyS2nm0goJZQ2ZaKM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر عراقی: صدام کجاست؟ شاه کجاست؟ رهبران پیشین آمریکا کجا هستند؟
🔹
آنهایی که تلاش کردند میان ایران و عراق بذر تفرقه و دشمنی بکارند، اکنون کجا هستند؟
🔹
این مراسم تشییع سیدعلی حسینی خامنه‌ای در عراق، که پاسخ همه این پرسش‌هاست.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669253" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669252">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b969b303cf.mp4?token=Sl0Lt_Ibt0efkKFqHii-K2bdU5jxFeR8Z8SRUJkT2I_K17HqqSmltGyK_NNYZAqDautny9aRURHsEpLIRiIEcltGatYgtWfEu3orMgKqabC8JDP7hjzLIMe6WlVTOa_mlIXitxoFdKukm2OnS9nFPnic5Yv-N7NRk8j3JiUX9-rJYNKqJU-NfKPDZtmGel1y5pmPeNecldB1qJjJiCjaU70f3ZiBkMVshSzHmtAR-P896gefScTG7VH7HBVfNphdgkDbnR02uBJITEAuc7nP3fN-3UQCfl8PHaYKLMSyFhs4PK3Hdbg49-_gtO9vbxVc53X7rLPzd94-dtNCDje3t7MOF_-fzQWQke2JmMXiGsGn80N_pxCsYbtkwE7cqvBQ1kQ2tx7qiICEIR4vnx2Sya6KIscRYfkyQYPPxCkV982y6WignYJgtVXb-ou58uyZlumHbmafnTWmxVRMgZUv_7I6s5EpUF2NST_uy88LTpoI88iKVlFKDXq5F8NzKN1DHQXDF7iHlEecNRS_7ez68gC04V65s92bUqd835d8ps5SySYRUyQXuB3Pd5C7XRSbjz8GKb65XpGvODSlHkjdnTvt0GkJCOluepBYzvoFQeMk0up2j83cq2aebYaIimPkYU4xXcgIzIaQ69Lo5UdFSZSIAGnJKtfk7JHcf4dYV0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b969b303cf.mp4?token=Sl0Lt_Ibt0efkKFqHii-K2bdU5jxFeR8Z8SRUJkT2I_K17HqqSmltGyK_NNYZAqDautny9aRURHsEpLIRiIEcltGatYgtWfEu3orMgKqabC8JDP7hjzLIMe6WlVTOa_mlIXitxoFdKukm2OnS9nFPnic5Yv-N7NRk8j3JiUX9-rJYNKqJU-NfKPDZtmGel1y5pmPeNecldB1qJjJiCjaU70f3ZiBkMVshSzHmtAR-P896gefScTG7VH7HBVfNphdgkDbnR02uBJITEAuc7nP3fN-3UQCfl8PHaYKLMSyFhs4PK3Hdbg49-_gtO9vbxVc53X7rLPzd94-dtNCDje3t7MOF_-fzQWQke2JmMXiGsGn80N_pxCsYbtkwE7cqvBQ1kQ2tx7qiICEIR4vnx2Sya6KIscRYfkyQYPPxCkV982y6WignYJgtVXb-ou58uyZlumHbmafnTWmxVRMgZUv_7I6s5EpUF2NST_uy88LTpoI88iKVlFKDXq5F8NzKN1DHQXDF7iHlEecNRS_7ez68gC04V65s92bUqd835d8ps5SySYRUyQXuB3Pd5C7XRSbjz8GKb65XpGvODSlHkjdnTvt0GkJCOluepBYzvoFQeMk0up2j83cq2aebYaIimPkYU4xXcgIzIaQ69Lo5UdFSZSIAGnJKtfk7JHcf4dYV0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب تشییع تاریخی پیکر ابر مرد شهید تاریخ در قاب رسانه‌های جهان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669252" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669251">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b52e080a43.mp4?token=KYlFwnHEPbFzH_BRbd8d6m-bdHWlghj2p67NJj0WW_L3yhHcZrhOfbw6dnKkVm_ujoXf7gl54nHqUzZVsd9iS27Tv5GMKw-igsb3248LbRjxmyQC7hnXR-7c03gB9hMdP65LHK2A78I0Q8KOVgzA5YTgT1rKVEXSrMWd-7ZDanJ7beUL-9kDBVWZeXMRz_9aqszHH6ds7ZvMqQWFlI5XeLZX_zs17kqCWYPEOkmx-PnMyfutLzhtrIW6MjET_NFeIbmVcBSQBxtB7uSZw-3rJztA0jXdUpJzBWAlRv9RpQEqZQfnCmf4fZj00huGpEmgbkC1YqOecBRajXgscGqDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b52e080a43.mp4?token=KYlFwnHEPbFzH_BRbd8d6m-bdHWlghj2p67NJj0WW_L3yhHcZrhOfbw6dnKkVm_ujoXf7gl54nHqUzZVsd9iS27Tv5GMKw-igsb3248LbRjxmyQC7hnXR-7c03gB9hMdP65LHK2A78I0Q8KOVgzA5YTgT1rKVEXSrMWd-7ZDanJ7beUL-9kDBVWZeXMRz_9aqszHH6ds7ZvMqQWFlI5XeLZX_zs17kqCWYPEOkmx-PnMyfutLzhtrIW6MjET_NFeIbmVcBSQBxtB7uSZw-3rJztA0jXdUpJzBWAlRv9RpQEqZQfnCmf4fZj00huGpEmgbkC1YqOecBRajXgscGqDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از
غزه، مهد رنج‌ها، درود بر شما، درود بر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/669251" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669250">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر امور خارجه ترکیه: آتش‌بس میان ایران و آمریکا پایان نیافته است
🔹
نخست‌وزیر بلژیک: جنگ علیه ایران باید متوقف شود.
🔹
یک مقام آمریکایی: طرح ایجاد مناطق آزمایشی در جنوب لبنان ظرف چند روز آینده اجرایی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/669250" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669249">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkGpNRfiK2wK9y2L0V9qq5Rkk8w02zovJaLI6j2MSH55q-rdw4BpydEbmuzzjvAJ790sa38Xqg998W9iTXB_WFZRC8VvE2bK60M1AGM8FXLQiv2hcyYrpC1wGxf4mR1Z27uOx21H8aDhayTvwYV-O6rrop6vWESPDZJKkR-rl9AQnbEIs0NmQ1si7Z4cqYjvlZS2gl_3oRcwxhuy_NsyvITU1wmDNY7c3mjZfsv_sQWLI7_PujycC3UU9RohDx7_9LBVFbhY0tlMYYLFdYW8EhaQUbuiOlkusU-Q9IZxxVCL29FY3wiaVR4H6Sq7yfKtwsiABIJQrqsQsQzJv-rgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهر، سیاهپوش هم‌گام با حماسه؛
نمایشگرهای شهری مشهد، تریبون زنده مراسم «رهبر شهید»
🔹
هم‌زمان با اعلام برنامه‌های ستاد تشییع و وداع با قائد امت اسلامی، رهبر شهید، آیت‌الله‌العظمی سید علی الحسینی خامنه‌ای، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد در اقدامی هماهنگ، بخشی از فضای تبلیغات شهری این کلان‌شهر را به پوشش تصویری این رویداد تاریخی اختصاص داد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآرورده‌های کشاورزی: «با توجه به برگزاری مراسم‌های برنامه‌ریزی‌شده در بازه زمانی ۱۳ تا ۱۸ تیرماه در سراسر کشور، مدیریت شهری مشهد برای همراهی با آحاد ملت و بازتاب باشکوه این رویداد، پوشش زنده شبکه خبر و پخش تیزرهای هویت بصری را در دستور کار خود قرار داده است.»
🔹
اخذ مجوزهای لازم برای این اکران گسترده از طریق مدیریت محترم افتاء خراسان رضوی در حال انجام است؛ «هدف ما این است که شهروندان در نقاط مختلف شهر، پیوند معنوی خود را با این حماسه حفظ کنند. به همین منظور هشت نقطه استراتژیک در سطح شهر برای استقرار نمایشگرها انتخاب شده است که در این مکان‌ها شاهد اکران پخش زنده شبکه خبر و تیزرهای هویت بصری خواهیم بود: میدان شریعتی (نمایشگر منصوب بر بدنه سینما آفریقا)، بولوار وکیل‌آباد (نمایشگر مستقر در حاشیه بولوار، داخل پارکینگ آزادی)، پارک ملت (نمایشگر مستقر در تقاطع امامت)، بولوار هاشمیه (نمایشگر مستقر در تقاطع صارمی)، منطقه طبرسی (نمایشگر مستقر در چهارراه شهید گمنام)، میدان فلسطین (نمایشگر مستقر در ابتدای احمدآباد)، بولوار سجاد (نمایشگرهای مستقر بر بدنه ملک خصوصی در تقاطع‌های بهار ضلع شمال‌غربی و بزرگمهر ضلع جنوب‌غربی).»
🔹
تمامی زیرساخت‌های لازم برای پوشش منسجم و باکیفیت این رویداد در نقاط مذکور فراهم شده است، این اقدام بتواند فضای شهری مشهد را بیش از پیش با حال‌وهوای این رویداد عظیم ملی هم‌سو کرده و امکان مشارکت بصری شهروندان را در مراسم‌های سراسر کشور فراهم آورد. شایان ذکر است این پوشش تصویری تا پایان برنامه‌های اعلامی ستاد تشییع و وداع ادامه خواهد داشت.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/669249" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669248">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4047b339da.mp4?token=aNZKGrQfpz2IXh63mG0JiL-mrgAxBxMI-u5fyxNMgVPJpxUSljMqUVWdOF1PpU9cY27CHJ8g8g7QcZxQwA5zP3TMTaUa6OD3iNf5EU9FuHsgVW77unB-CSZ4icsnUsVIxc_AVnaOYXjIaqiqJJ8ev46CbBYvwTnwYdy4gxnCYLdKlDLlH6XsPV0qBl_XZNQaWuo_BIbXEyFNO-WKeP15jzm9z_gwY9wAwPM6iduiLP2zec6xwOjuFfR-MVFGkfK18i4UFTcTySuOxwHYffOfbYv1nF5DbmJ_w_4r4IjK4xHU8a_LHRMdalctCbblR6W4-v-o1THHVy6cAGfV0ZFvUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4047b339da.mp4?token=aNZKGrQfpz2IXh63mG0JiL-mrgAxBxMI-u5fyxNMgVPJpxUSljMqUVWdOF1PpU9cY27CHJ8g8g7QcZxQwA5zP3TMTaUa6OD3iNf5EU9FuHsgVW77unB-CSZ4icsnUsVIxc_AVnaOYXjIaqiqJJ8ev46CbBYvwTnwYdy4gxnCYLdKlDLlH6XsPV0qBl_XZNQaWuo_BIbXEyFNO-WKeP15jzm9z_gwY9wAwPM6iduiLP2zec6xwOjuFfR-MVFGkfK18i4UFTcTySuOxwHYffOfbYv1nF5DbmJ_w_4r4IjK4xHU8a_LHRMdalctCbblR6W4-v-o1THHVy6cAGfV0ZFvUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور قالیباف، سیدحسن خمینی و اژه‌ای در حرم مطهر رضوی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669248" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669247">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7qN-yuvSbMJWWjt2Msya9YfrL6qN_ErEt1cQ5eTSNyW7WEdvG2ntkHXimZf4CiWZiAChpvNe-kCBCo5lUV5W242ZoLCMveYXLJreCpFUNSLGevnOUsY7833zrXCHvXH9u9flMZcW5lw23_p7pqGrUaaswyokC9G5PvDMjpg6C4KiVp2oOajxqVtWUkaGp1ZknogvojOFxaGU-tSOMdH7NUNXUSSno1KEdrly42QkDsSJ2z06OZRK0JVlIWY4W_zY3eVU6MVNiW_BsnimawYybDHWU5RhWffs4m-O0YIIURD3t72eSPVPTYz-yGrQ9_5VKE7MZtp1WfGuTBp5saRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیت رهبری
💔</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669247" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669246">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515aa7f7b7.mp4?token=Ix2bIdQKpIUZcnUdCaYfRgnDwlmqP_eP2VlJGLpSwuzOSwTa87Ebae1HK8HH5V5dDcnEYgHghbGMVGYWd_8Fqn7NmNiHeiOOGU5vJMY-CAgk18_C6Zx9DVoYEbbTQypK7VhQu7Y7aHyVePs3TfuUipFMzO9fP9kWydgDGxFhRx-vaKWlwU8UDMxsMj5vQ-mVoudn-FSqiI3Q2oavekdT8rWFCfooD7z9ZKHQZcr93_WEIHbCEPKIJLZZmfMeQpKlOK1Qh7ME7lWwKGIuv6ucOOJuwLYtnbQdqfo4Rjq0x0LPPIfCXNE0w7U_Dd09CqN1l1ZtUT49FdKIP7L9kGkAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515aa7f7b7.mp4?token=Ix2bIdQKpIUZcnUdCaYfRgnDwlmqP_eP2VlJGLpSwuzOSwTa87Ebae1HK8HH5V5dDcnEYgHghbGMVGYWd_8Fqn7NmNiHeiOOGU5vJMY-CAgk18_C6Zx9DVoYEbbTQypK7VhQu7Y7aHyVePs3TfuUipFMzO9fP9kWydgDGxFhRx-vaKWlwU8UDMxsMj5vQ-mVoudn-FSqiI3Q2oavekdT8rWFCfooD7z9ZKHQZcr93_WEIHbCEPKIJLZZmfMeQpKlOK1Qh7ME7lWwKGIuv6ucOOJuwLYtnbQdqfo4Rjq0x0LPPIfCXNE0w7U_Dd09CqN1l1ZtUT49FdKIP7L9kGkAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف ما یک کلام، انتقام انتقام
🔹
هم‌اکنون؛ صحن پیامبر اعظم، حرم مطهر رضوی
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669246" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65aff7c68.mp4?token=rPd1AGc1nkv4duYWOOLLh2JZpJGX1G-BiKJrW40avMiENHiPuZkN9fMhTiOyE4S1dH0QhvOg2Wx78xY3Lkk-GG1UBdLGyWWYoBjLcAoitxQdnP25g-SOVcMao2vB6PDNwm9qNKqc_7jfVkXjoyUtVdZhYPnbDgCfXhJN_y2clRIxqy1MyJfmCbGHkH3-cNrvjHWUfjHrlltKAYWCZbZChuZBEudgEa1IorWJVzTFbN-dQ_LG8iR-5hPUCADpsDJ8T6RqoHJfBzz3L9SSputWJIC2AsPkxwpnTcT-aO7Onz4IvsxyZvTNrIgDTUKVD1OKQKvar-kTs1QfHE173RQhnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65aff7c68.mp4?token=rPd1AGc1nkv4duYWOOLLh2JZpJGX1G-BiKJrW40avMiENHiPuZkN9fMhTiOyE4S1dH0QhvOg2Wx78xY3Lkk-GG1UBdLGyWWYoBjLcAoitxQdnP25g-SOVcMao2vB6PDNwm9qNKqc_7jfVkXjoyUtVdZhYPnbDgCfXhJN_y2clRIxqy1MyJfmCbGHkH3-cNrvjHWUfjHrlltKAYWCZbZChuZBEudgEa1IorWJVzTFbN-dQ_LG8iR-5hPUCADpsDJ8T6RqoHJfBzz3L9SSputWJIC2AsPkxwpnTcT-aO7Onz4IvsxyZvTNrIgDTUKVD1OKQKvar-kTs1QfHE173RQhnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود پیکر رهبر شهید انقلاب به همراه خانواده ایشان به حرم مطهر رضوی
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669244" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejzy3IcZ9-VhFYhzo6_1HmVHpy36tqfT2NsDt09B_O6rx3M34QEivCBUB4VUVs2aS7zu72GvIorgGj8SM9bxwb3POnX5YlHT_19ql9gWDS9mPOKjDDN245ME7l-2iB7DNu6fGkl_0b5_it1C2e5cUg48ECwrC7YKUlT30zcXb4yXtDv-XBYpEVw0f91oH4CH_ZozBaULUrcMOZJC9lAFRJ4s22D1LqnV_FHrOj2GKxz6Ak39XMI0hbGCnR6eyFK0Z1NZlONLzzDtYNkKAiB9uzs1E65O4CN1mw5I1hn7XZr2EgSTpPfXaUbMktqivxM2te8FtDBmht9tqgu0IaszQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قـاتلان رهبرم امنیت را نخواهند دید.
(در حاشیه تشییع رهبر شهید در مشهد مقدس)
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/669243" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=gWuCkt5vk0vQzndeuhY7xmXDCYHrs9XaSv7NqXqjDSwRilsjvd9p5dJChYpmDq3O2jrC50OaVbBkTLGDbintFOtkFWkCIhuwuzJu3mXZf5ER6ifVVy2fIMDgWWwI_CP2u6GWKh1jeizwMWIOTJdZMgDf8_mhrqkgYrj5TiTAmLhTCDaFdOt6AU5OntynWTNnnnDAGtUARaETi-ieysdLkVLtt46_upDchGwkD9Ei_tXkl2ejlRyPp4DxsfYNsChx-dZFGrU1ll4eTjH3y_EoRk-lJT7UZfPkX6a3AQMGE5T2UdWHrPzHvw0VE4eGQAlDTbA9FkaKyU9GaoJbW2pQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=gWuCkt5vk0vQzndeuhY7xmXDCYHrs9XaSv7NqXqjDSwRilsjvd9p5dJChYpmDq3O2jrC50OaVbBkTLGDbintFOtkFWkCIhuwuzJu3mXZf5ER6ifVVy2fIMDgWWwI_CP2u6GWKh1jeizwMWIOTJdZMgDf8_mhrqkgYrj5TiTAmLhTCDaFdOt6AU5OntynWTNnnnDAGtUARaETi-ieysdLkVLtt46_upDchGwkD9Ei_tXkl2ejlRyPp4DxsfYNsChx-dZFGrU1ll4eTjH3y_EoRk-lJT7UZfPkX6a3AQMGE5T2UdWHrPzHvw0VE4eGQAlDTbA9FkaKyU9GaoJbW2pQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی بهم بگه دروغه...
🔹
نوحه‌خوانی مهدی رسولی در حرم امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669242" target="_blank">📅 21:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=I1oe2CyJaedKFEIMJSbtH6fR_QNMt3YA9qFTXJvzvq7bFfIkoQFbK8d49rGey3b9jfSXB8-g_Cu6sRV68p5ee3ewm4qbheY3vHCjj8Pp_uOf8eS0iMLUeMvzXDWxTR1VHDEUbY3yNjLkQE_KEO1k60Drj9EHlDw0o8I3NxFwkB7lody7M33wd1yf1iOEOhqxg4eNeNyosmngn8YoeL6MOf8gG7DrsJosculiiP3_jVdk2wntLANCwf2ANlYYHAnONemctCoA59r-HgnT0rzMflCG71aI7vipBZPnYAQZuMo5jr_6f8Rat7li6JxLa9_A4M55dXjc_XjYsbJNhkmntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=I1oe2CyJaedKFEIMJSbtH6fR_QNMt3YA9qFTXJvzvq7bFfIkoQFbK8d49rGey3b9jfSXB8-g_Cu6sRV68p5ee3ewm4qbheY3vHCjj8Pp_uOf8eS0iMLUeMvzXDWxTR1VHDEUbY3yNjLkQE_KEO1k60Drj9EHlDw0o8I3NxFwkB7lody7M33wd1yf1iOEOhqxg4eNeNyosmngn8YoeL6MOf8gG7DrsJosculiiP3_jVdk2wntLANCwf2ANlYYHAnONemctCoA59r-HgnT0rzMflCG71aI7vipBZPnYAQZuMo5jr_6f8Rat7li6JxLa9_A4M55dXjc_XjYsbJNhkmntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی محل تدفین پیکر آقای شهیدمان در حرم مطهر رضوی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/669241" target="_blank">📅 21:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e45dd1ffb5.mp4?token=r6ql3weWUr0tAD8bxvKcPP4QkSb_CSFUwrRBa_eMg5MLXtVAdL-zqTyA9mY2gCvH6HfJOaND1xE_7DAjvxFIkGEY5ZT-s8zk440U1oc9fpiMYDy_ephlgan08NBRfkcb6KHdBqH6L3vQxvTSt25YsvLmWccjwidRq30tEEiAmNZiwxiutqCK53inL5UmJ6WajwkMMkUZCTDALnKKc7UnuD8dtREtviPCqNuE0YgeJu6hq4umYT65yrOSQZWWZEOH8o1QAeed57PLdI9-pBbBIYpmJouq4PjvelTGh0SD93bUd2h3L0VSmytLAMC2mOSKI62eGqk-7yf6mH6eVpcP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e45dd1ffb5.mp4?token=r6ql3weWUr0tAD8bxvKcPP4QkSb_CSFUwrRBa_eMg5MLXtVAdL-zqTyA9mY2gCvH6HfJOaND1xE_7DAjvxFIkGEY5ZT-s8zk440U1oc9fpiMYDy_ephlgan08NBRfkcb6KHdBqH6L3vQxvTSt25YsvLmWccjwidRq30tEEiAmNZiwxiutqCK53inL5UmJ6WajwkMMkUZCTDALnKKc7UnuD8dtREtviPCqNuE0YgeJu6hq4umYT65yrOSQZWWZEOH8o1QAeed57PLdI9-pBbBIYpmJouq4PjvelTGh0SD93bUd2h3L0VSmytLAMC2mOSKI62eGqk-7yf6mH6eVpcP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حتما الان به امام رضا(ع) رسیدی...
🔹
مداحی حاج سیدرضا نریمانی در حرم مطهر رضوی ساعتی مانده به اقامه نماز بر پیکر امام مجاهد شهید حضرت آیت‌الله العظمی سیدعلی خامنه‌ای.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669240" target="_blank">📅 21:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQIFSsNaPMDvu63jodC9LnUMJK3-VLhfSf90tV3HvCdZjCJf14lX1qtZ5F55pn87qEAP-4Rj5HEOW8TNkbAy_mwYbEWw41ZRcmswEbzyZkuzOGEyKxAAz9U8FhrQhySJStD7l4zimkyS9rEb-19IHreZjC9jIYw9UfkMQp9xj0Ve25SSfftJMvJmOXpQXWJC60Ob_NOzc26FZXfpMBGHRuANt3_CAOsiuvcNRYpdIG-Iipjjf4DJDLdxXRdG_sHx_vg9PtLspdb_feZB_K6PDQqzifDplt08-JUQz7dA3CSuu-IhPIaIeNVvek9_VM9wGTzw0YDmvsscnmMbI_9PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از جمعیت بی‌نظیر مردم در صحن‌های حرم رضوی
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669239" target="_blank">📅 21:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#باید_برخاست
♦️
آتش‌نشانان مشهد در روز وداع، در کنار مردم ایستادند
🔹
آتش‌پاد امیر حسامی، رئیس کمیته ایمنی ستاد تشییع شهرداری مشهد، از اجرای موفق طرح تأمین ایمنی مراسم تشییع خبر داد و گفت: آتش‌نشانان با استقرار کامل در مسیرها، مسئولیت تأمین ایمنی و خدمت‌رسانی به عزاداران را بر عهده داشتند.
🔹
وی افزود: تمام ظرفیت‌های عملیاتی در آماده‌باش کامل بود و مه‌پاش‌ها با خنک‌سازی مسیر، گرمای هوا را برای عزاداران کاهش دادند.
🔹
حسامی تصریح کرد: نیروها تا پایان مراسم در کنار مردم ماندند و ضمن پایش مسیر، آمادگی کامل برای عملیات امداد و اطفای حریق را حفظ کردند.
🔹
مدیرعامل سازمان آتش‌نشانی مشهد خاطرنشان کرد: خدمت‌رسانی در چنین روزی، فراتر از یک مأموریت، افتخاری بود برای همراهی با مردم در وداع با رهبر شهید و همدلی مردم و تلاش شبانه‌روزی نیروهای خدمت‌رسان، برگزاری منظم و ایمن این مراسم را ممکن ساخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/669238" target="_blank">📅 21:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de0dee9cb6.mp4?token=FSqTZUotuZ1u2HpeyeYlddAPTQZJ6FYGixIuSU8oci--rX5NVnGNyBPV6LbM87Uo-F7XWrXcnFSUGOAIgLz5BqLLLndX8vAozWUAOD6VRzIl1Op7rJTmkthGhQVVHfM2wvxjMn4NBAIKKwYx6u7uVB8vUbDTsWpotCSM9mGsWdl_ToFIn1BOrO_1VMlanG78E-7yMLtunsi9Hg4sALX6HmqvE509C8M3Dg37cRf4KBcLRcQSqgOdCdkGcRNnMiU78iYugUqzBYDlt_ce_zngmZMSQT1F4TbyPo1FrxNEFpBQSWPTqVOm7j85hTzfTLKEOkHHxd1ayoZd8SaI0t88dIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de0dee9cb6.mp4?token=FSqTZUotuZ1u2HpeyeYlddAPTQZJ6FYGixIuSU8oci--rX5NVnGNyBPV6LbM87Uo-F7XWrXcnFSUGOAIgLz5BqLLLndX8vAozWUAOD6VRzIl1Op7rJTmkthGhQVVHfM2wvxjMn4NBAIKKwYx6u7uVB8vUbDTsWpotCSM9mGsWdl_ToFIn1BOrO_1VMlanG78E-7yMLtunsi9Hg4sALX6HmqvE509C8M3Dg37cRf4KBcLRcQSqgOdCdkGcRNnMiU78iYugUqzBYDlt_ce_zngmZMSQT1F4TbyPo1FrxNEFpBQSWPTqVOm7j85hTzfTLKEOkHHxd1ayoZd8SaI0t88dIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما رهرو امامیم، دنبال انتقامیم...
🔹
هم اکنون، شعار مردم در حرم مطهر امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669237" target="_blank">📅 21:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تلگراف: مشهد به دریای سیاه و سرخ تبدیل شد
روزنامه انگلیسی:
🔹
جمعیت در مشهد به‌قدری مسیرها را مملو از جمعیت کرده بود، خودروی حامل رهبر شهید انقلاب اسلامی ایران به سختی می‌توانست حرکت کند.
🔹
خیابان‌های مشهد به دریایی از رنگ‌های سیاه و سرخ تبدیل شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669236" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8791f99083.mp4?token=SXm8rlBBtjZJd4eKCie7XYk_enD73v73MDkOfGpzTvPAqNH7kQEvqfTNoIQV4bMkZKqqqTeaib03NPQkBCDy8zn9NJR1NbymHe_DDdFcFG9TKgmthBn54O21XRimN1JvxflrlRIHqlloBb4NhUm_KLRa0favW2-efX9Iwn7Seg9nI6pHXUuqfe2oipLl3Qtkg42I0BHcPAfl6tTxlJw_diw9I1CJv--_Nt-TCXsNF6FHxoZ1ZCHiK636gw5fYntsTUGYhInJ_7VkuDKccFVwtWX1Yy80iUOSfK4PoQG6Yvs8V2yDo4tsMRaWPr1mHLXN9crifjArCCMrucfKjq9_6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8791f99083.mp4?token=SXm8rlBBtjZJd4eKCie7XYk_enD73v73MDkOfGpzTvPAqNH7kQEvqfTNoIQV4bMkZKqqqTeaib03NPQkBCDy8zn9NJR1NbymHe_DDdFcFG9TKgmthBn54O21XRimN1JvxflrlRIHqlloBb4NhUm_KLRa0favW2-efX9Iwn7Seg9nI6pHXUuqfe2oipLl3Qtkg42I0BHcPAfl6tTxlJw_diw9I1CJv--_Nt-TCXsNF6FHxoZ1ZCHiK636gw5fYntsTUGYhInJ_7VkuDKccFVwtWX1Yy80iUOSfK4PoQG6Yvs8V2yDo4tsMRaWPr1mHLXN9crifjArCCMrucfKjq9_6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌صدای مردم در حرم رضوی: حرف ما یک کلام، انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669235" target="_blank">📅 20:53 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
