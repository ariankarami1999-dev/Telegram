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
<img src="https://cdn4.telesco.pe/file/GIS2peHtcf3msVut9FVfG1zY-UA2LjTa6JUZ1qV5tpXrEH5oqAFPEr-WMc5a7fBKGnYcwq2Y7Js2XcycUHWxmJ2pqg_qb7rwD2xjiiv3DDN-t4qMNYxcg172yxPQNYvQaAW62DtrFFuE7agDaFIkVr89Y5gXHD7I5almKt0FibHz_mB0wt0NVYt3ejNVDeHtOvKN376o9KEVmreOMjcJ_OnbZphqYtI3bfNIIEENlngi_LljvhMxhZoKMMXsEc7FMgDZilzsYt-AluJtyh0Gtsp-wqSF6DF9DsYKFNWIYG3vzqy1dXqluakcQ6yvHzqgWQwVJm9y_21S28uKfSohWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 208K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUYk1-iA6PgIu7NL-lweGzs274WOU_B7hKO7KWOgO2-VJAqXJUmhn7LJqm8bWwgwq1Wv_zz-4-EcuSsNKx0PdCPvEfssYzCStvhdZJFkX4L4w-uWIPN5dXOBlIhLKj2jONpGy6FqUZ1JZkt8CcRdYRKzZyYgj__1dGSQ4ObB4sYjD5soPvo-fQ3kzsQwqwL1Bx65ns4trDus81AsYZT7d_bfw5_arf53SyhQGR1eEoRBfAEjYeooIUNdRN7BCr5WVr9Sc6clnV1wP7FYD18K0cg8KSmsqKFE0mt4WfIRDqN2797AQNt1erTHEd-dM-ymYgyopiWN6_h2Nr-kROwEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBHHDdN_5VwmAbAr_DY64TYPzwjFRg9UhDCcdyzeDijdmNY3vfONSl70Mbv5eGfh6QP_r2loLV562riroKNBhlB2ljWrwnVhVncNAv6CK7CF7-LTL3c1HUy7_-i5yC6RDuCjN_nh_N3zeY3unfZaNgJZ8UahkzYo3Oiaw0OLGy4EQSjhyoCXcbsCh2KJ5CkCQaE1S245cRBMAd6oucav3Hzb_SGV5Xu1Aliaj7k8gLMMF1SZrmmMQkLnONhkSQmjXqCJgIyvFSJsLpTGw5_T5ShldKMeXgwiKogUFesGN2R3NvbVaCvr107IaY0NdCm4eUw9ufjUHywwFs30670Y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obiQj-2lqrXnzIxcFkvCJTg-1fxrrMZiCPQDbspxgRoSA8pLd7uSUqQClHLzT_Sjj8oBJ94qeQ0Lo_8iJUPJb0SKXIq6wTRdlJbbB-_92wcoq9yDVr563PcK5Z_5liLA2iCNrdLQiw2dbbl-sBOWVMAFCLE02FjK9zX6KiAEk-W-A_t0kMG8RehKchIg-VyUKi2fJFgQeMiMOKc8UQuARcU1KvD606qmJGoWLLwj8an2omUOIgTqv9aqvSt0a-ZzjWSIMAr-NKsw_Ff_V0g9PqIphCXXKpR-DuAeegbHuU13zasB9kEw8CWrOoRgNnuCfpOeWQLaS7e_Ox-YOTMJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udni4PlaImHCDL9IFGwv7_1YYiJ3QzB4dhWo8S88XdWIQeWILXJbxdjXCWUYJap81u5imDtbIuWiOw-N7zW4fR2dh1y9bCXBKeEBWr37fy58PfhMmymMaiC4EVSqUu7_2pLDxWq8hj4ueJaTMq0-ppeUE873qSzsjtg1ZO4Mgj60ZeuR3rOGYmIlpXeRIuV5S-yimIUrrGXc0A1P2N644yBiDa4EpFqccgCW8gRGbGgF8LFv1sHtQ074G8iPJnbOwOiKXQrGMMoeaHM04A-ifPOalzrAiaU7WqTXGVWuZEKauRBT7EPj9cGYiVb-xvfZOuikwFXMTIhEq1pDKthpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9ZdsZtCq4m3xmvrQuxsp9EuFtlKA6C4_ARCT0Nl-S7UPneNTOym86v3QHz7qz9k0ZmgxIxcxlcFlR91fjOMosDVmxmFRmX5Ssja39cs9yRadpEXxZcYiCBxcWJOLGh1hhAD-g9O5aKZDwQcVZHc7QEmbhXHSUXvV7IBJXnl2s5WLs1RfYgCBSct55EPzaK0pYcdbnDYuRmhaTzWZgm6EUYxJDdwIvhM3I-M9e1f1WwNtr7iMTaXpNANv5FLVgJGr_PimhYNaX-MI8vctA8f4xnf0EQExMlnoG1o2XghQMHXbItX48NTqjXL20RBhWcWGDoSoInV38EeRJxObNWgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciS4YdJXbGuWDzD5ZyL0-q01v2wdIDGMCfYFNxw1rFJFecEZzNBQHoYiiPBmgEqRI7_cdhGMwiyaNQRyRhp3fG6KMJhmPgSM7_cneEANL60z1IcfuA98D9LpljOib_70V9-ZQl_Es9N4ZkqUq1NY8Mm9KOtdowZ7fCddvoZ1PL6aJ5ApPGlDMW9JamyLiNeHldW32ncfiZ6jCLcdgxW6Cn5KaGHZxD4YXLxXqTKmXDQ7FeIfWTmQGuAz50Xc42Or0By1P1ZracRqXx42bOoe1MxTkOumZutMjlewBpT61DPB0LFIRxv5TtDg65LhXDdf2V8o1cyP7vOi0EsJnCZZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWl2ydOqvsGxPofN9Kmm-qbsHdoIkJTIcbXbOoqWne2TB09WQ5AwaIQZhC0W4172-pbcsVRNdtZW5sNt1qEKQQuhCNFYZzQcBNBEtKGdDOIR8LbqFbICXKEgJMogDdZwg9MhjFL7q7ac149PUQGjSeH5SWPdoj92oNW8gTyBRZxEcGXqKFpU6A7oLIKeHsL04T7x6PohWEzr-UMM-PhvCc0afpZNDLsZRuUg6Oq4td97tuQi1tB-0I4gaCAzESfeJntvlCQ3GgUC_Z8N7h-bXLKPHfBzAY_53jyDJAHPkAHZ-VArg4a6g_HtpRC6kiJJG5xs9PDnuZmDjekV0dIHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKVmcMAopjdnljZhl4s2F2zr13mEoV9HZvT_SWqi50v-biLT4om8_9jL3MmoTBm2SEPUGjwDPkYfInYBaKJglC-iXApQzlfN3GiRX_RQ1_c-0l-zKRwanASRk0WduLdKbGe4f1z4kWcrxBVDypdgjuqvJ9MZUe4T3aQl-C8ZvaFknqsjjOurOzlntyTfeNH8JdW34izHIfhkW6F2t6Ma3zUYbD3r8TxTR7joFJzwGlX4Df3ruWCtAsH84c-WbfPYyQpbKfCCbTfjSTQ2oyaeBNeIorYnHFe7Jv_0XGJ5z4rdpAZn5opD6VU0o-NOzJwQO29h90dbSntL_JP74nv8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7zRwTARC8J1ygNIdAG-bF4J5wJeMdlD2jFlxzFy7e6aYAH3DJUFCOjgWkOQSV9mdVUNikMYJZgHvtjvSTlGJF8H-iDgC9hPdqd9gmB9bYlgKsSjKCxPd0s1Fm6Aw47JltGAeeZMWAZ3lHwJj3W02yDPuE2ZdM0-aabSIXPFo2z5AYrRBSSdywa_M0kwtAt7UYjo6T9IzeQshT0WG7BTGzai8pGJl5IF0HB95keVeTNTierRH9AH-rZOYpZnRZDW4VLwpNDMU8KHxtyaI0-LYitOtBXTqdJTKEOt125Yty9oQ9hEXM3zSAOAsHMecQ0xNg29_CtFappj1QzC-dhGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dylM9x1moJakiwRpoVgQallw9R6bUIA5lFrgA4Q57pDHn3UWD8jcF6ZrbX2tMWlB1OlJi7yAfvtJRTiwQNlz5SM9tHXQP0KmqQLIqq_lmOHtABgd_CSYZolZPUec9_ZXPwsJnsGafqBg5xQqZasGZc9HTPvTUnOCJp7RxOBD3mAx-tZsxLMoS9HlOffdtPeb_VsBDr03nOiLys1C_jz1SNh50ujctVGcr04iWbtq8x6qsFO90g88VvC6rHE__Opmjoy7Ot4durQrtEcFOPcGQ6r3XGj-4uTGq1Y3-r8LT3Qq9wHtsqcoJB2x0S9P0aMxwTmfDHIr1vwwOBAluftDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okUspBLii1RcUEDHGWVQwz9VQa4TuG7UVeMvKY5NwoDw9mGwQl7IDd-ZHsei0s2mWlwtve92UbLVcysHy5I5aiH5TQkWlChMEGt4ZCJo3UAKORoOOxbrUJ3CxHuKDnct61U8cC6SCCftR67rKYrzrUnaFjaZmvnwT2t7rh4bKzkwS01GPz-CaPZy6q9xqLvzHMJGKcxfJlFWSS4TtZ26ueEIzbFXAd2XujEwL3nj0qYxPOeNIIIyCaYL0noxWXun3StlOWb56MEVd16HZIijbD1vtAY3zWZDPFpo2CqINy9_Ojw5sBbtkAUkKkL33W0FNqU-In8Dobjh4t3FhUkrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTEgOz6k7hkDaIC5UjvMowDjZl_jjH_2SqC30RnwgSkowoJ1cXy5_YW22MjqbL1X3JasZVEC_ngQK3-xvEem9ATei9l6Xb2egFIjYC-DLXnMlXNNM5KD4KnBsdboUs_v1gm6vRyUbcg97F_rnFu9paaN267L4hrBRghdEFW-CdyUhRZnwV1LxJQrcpDd2ldgzHNi73h4Rqh5oT9MZTPgtVZToBKqHnpYYHkQdamagIAqk7yqJkbfUuK7AtOwMD1fk666JfX9vKv_1gKgm3otkx_N07iFAgnDSEd8k78Ve1Kz5pbuzzrbYUHM07oC-IdMhOKabLEPqjRKn_FeY4afnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULSaJz_di_4on6BMnvE3fMfAohPqeDAKUbM6zCNVaOnQbLE6Vazl3shD74EP3vXHmm4s1NA1cXlZa4jvJZOMNb980cL3LC_FN5RcoJOKIaMQoMmTxx2xwVMiE4IkHgPvPkTPEAI7sL-cO9dx_aMERXBdFKjSehKVrd5zNabPZ0Ow9gl9KQUNKJxFPeTTYsm495yd2VZWnsbqu0Tu2Ec4eqsZ_1AgKcNTRzMNv0WYzhuAro0C2ABe1yo8vlNIuAOPjWUt3pq2Ihh3nwUZXAlMsLjjwQiRZ4f3gLmFUXrPK3y_Qal8fWADh5b-RGHMeog9SNidM7n1FRdBjSbCGb02Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=cOmy6tsbPAx8Sm2hbdPhbUr_WMUaPAH5RK_CP44Ia9f7kD-j_GyBQUBmFQpdssbMoMvOkhD6lW6YJrgziM-W-VQRmJQrC0mkSwufsBOndOhN-bM8TkmVMbGg6VtSkTVGY9_c49t-mWLsM4rhP0NW1T_9lsU5JvtocwPlJ2uRTwOHLqZIsD_1fTo7UOLzkIjyKZ5ST8g4p9-4U8E5_IFWhHOt2STfOltl7meROfhz_aYpHUB_bvQ8Cw5dhTZMwykfrjjPRaFRgw9ID6nkjKVlle4hsrtTNFQ14Hfrh3r8Jzcrt09zFOM_cdFIEmdJa3Nva9sCTRRCV-oxqJ6mJPGIew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=cOmy6tsbPAx8Sm2hbdPhbUr_WMUaPAH5RK_CP44Ia9f7kD-j_GyBQUBmFQpdssbMoMvOkhD6lW6YJrgziM-W-VQRmJQrC0mkSwufsBOndOhN-bM8TkmVMbGg6VtSkTVGY9_c49t-mWLsM4rhP0NW1T_9lsU5JvtocwPlJ2uRTwOHLqZIsD_1fTo7UOLzkIjyKZ5ST8g4p9-4U8E5_IFWhHOt2STfOltl7meROfhz_aYpHUB_bvQ8Cw5dhTZMwykfrjjPRaFRgw9ID6nkjKVlle4hsrtTNFQ14Hfrh3r8Jzcrt09zFOM_cdFIEmdJa3Nva9sCTRRCV-oxqJ6mJPGIew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUntBcC4ptxkuVkYG9AwWHDdpHV05cglzJAVa3lednL3VKfwhYgSU2ESUlFr09YWgmOMWSpfJ7_a30PmSVIHZV1mEQj6aVFi-urSiGX0JFfB33Y5RJ6nbdRk8X7of_DhTsi40egJ8DWsLEbPzUUgz0BGk1zKUV0JqApFT2n1LaQv5eUeYn5l1qM2wA0J3JSQs79_74JSmNSM1OYJVaa3WjoV8R9_Rf66bRvN4_uDhR_39zkqj6rxxXrAi1FXL0hDJnNvC9tKgwwczQ4xHwmv5W_6o8X6-XR3iKEbAzX4b0khnQtDKXOjC6femXnM9QyiiayVX4vTyJUR1ht-KcGHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUXPVenySKtuG0LqfEcgzP9cmzQ9cHEbJZo93u2SsBgkAH9NRWnOw9O8FxU1AYwFoWIsRUdfdyHqS1X-i45ZkSUEphb_7QXculQbG5_T8ZCL9PmrWrE8CIC5pJosVhBCJmn4JTlvUOaL9jPt7nrLWD7mhow6KosdcWSJQg7HGaPD2JTBzE-eALpdSAvFVo5rV68Pu95BywYuoG26B2UVsAXoVzfOTpLVDQ4LT6UdqXsxURKWi1gJz3kQR2M-Wm_EwVXln7b0FpV2FW2rCXCnEBn2ip-kRlKzt5dQ8ORVdqSPa2wLpRwYgr-7aLwip7ioP2W6uEFZ9SEe-e0BjXkeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYdGBYPq4wiQHKJ7uXofmow7zmebMMnraIUSBzLBehz542BIIw-B5vxunZCE-ku_BBnB2rNbaV0o1ZfVksaGZKq_irItcYlylqqo36DmaqzGWMx9spLKuxjNfcQTw3HpDCNbGsgukAzLG_B-4aX4AuLikc2n-bXYpOGcqmXBX1W9Q2MERPWzWt2Uh55IBG_0DXsYFzEY-cSkXq5fcWbLoVRjxiSTm4nAchr_zR04K5P9gofn6s-PU-z8ps4mHOYAjsu07KpPu9Qzd4UIuBxb9ASsDuyW-f-D3fdBGCNAxGcelK1ybJukrrEhuV5Jed5lNswd5Ylsx30NabF0i5nEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnjKQIL8Rj8DU6d888C70BXgOsx4HW07svWUgVdmVtn-TI9RCZZdoi0AoCJL-7qsG_2wZrLH_XcUTasYj363JuqELQbCkOKdk5sdYcdrof6shkpHADoYOup_wvhYOZdOVf9wUPfKRmPfDu_UQ1_f0Nes3SSy3Qhx0ueFWlAXqoRW-owMTPwBQH2NBRqfd3kYmESOzzpj84zAu2byINVFL3G3Wih_axBH1NMAW4ZBLlp6vl8R2EyX_Cww2mYJKZJq2qBxTe1V4s1UYSF7tOT27gNPEHD-E-ZhqxJ0b51LZOD_7xMV6-letnIJ-VUw81LC95JB_MRiS5TPEaO7k9ua1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ipx-rIWjX_9xngFFF1Cj26x4o3XGbCpZ2hrXUq8Er8zb4K_45u7ytlD6ywtLSYbAB6fUQBF5nR_0lXjIit7iI3stHLHkJUd57CLvHdk3PFJZYizulvvqaV-SJDpuQ8koqSBEBLxAJRLhaRaO7W2lpq55pLwQix5cfYH0ShFRFW4QT407tgNAGYi4DJ9yVTKyTU4hLaCEqeF80PfEuRnTFwd5Qc_c4wTcV60as49QUV7rAww6lizbuqQRYP6wnbzQ1HEERxekQg534ft8ehI8B6dkdCz9M8AKKUo4YxSZdxAemjMB6s8iAAngP1bjruKWTtMQ1f3FX0nDdK3ZfNL5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY2dL6RACe02Qn2Q-Oa1Vi0_vaNxpJDXakKo2BJDt2Y_Zr72h0iyRU8YFleJO3xW298k0foHryr0E2mVIvyFqJvoyh8gNb4UeX2dB7abQ9ZQ8mSZ1x3trgq8Pi0AQ_hWczrI4l56eBW8DoBBm5OxRQae53kYf4XTn43uQu-VzMMU8Xpy_MxcS_hw2STbwdwlP5G8rdxk3nM8S0UR4BBh-rIxC6UExKLRsWfFkrW1oh3gplrpkbe1YIEAa1tJzFAIzW7XN_2TabQfCIcYk2AyKg3Teho01GYnzG7KO4rhrvK3qRojUKVg3I9zkcaXS-yg6I9u00FKDf0V-E-jp7QhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGoDx1hL51hwwfIajUZmAmssv-CLt9RbJSAa8BcfGoL2ch_ZrnPGHHw9v27UIYmxwIDIn_4yMb2FxCbmlb_O8eKb1yBcgnLpzLPPUj3x45kgwdsJ67OwN7o1jptnUHdobEF8CBnJvhIF2TLGlykUAC0uEyJ42zAMrxZ6bAzrkJg4k4CFWejfX7zjJR3YHbDAd2dsw3o6W5ILA3QBFpolGPVj_N7kbcm-r-xSNoUkPRdQ0V_ekWA1hoYec7T_EiWclJhvjN5G3p1KYZxVR_a7wUbFx4OfInHNBOAQgFcC5WGlu3QVbeH853tE_hY-NQy24TMepTtoXXe0VNoigrzXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAenl1m2UzXESip2I-8eANd7BzQ4uwVK9XVad5NhYZud04B-5uaTuQmBlElLPbbDn3-12bQz07V3PztrXsmyICpVhmwt8YUciScQNiPrE0i2dTLbo8p5M32kJ70fOhTBnMuKDQNYociYxHn9Afb10AwitSayQOcE-LYFJRZse5wtvvFL6KX2804ujLTAFwDgqC5ko9fdypOfWdwjej7gjBKoSqqAbzT4chhBcWA3-8VEl-qxB0oIUhee1G728UOU6arxEgFOFVzlXYCl4hJlveBEOwsKazb_u_ntxLu9fByWeCO865YMo3yff-KafxA0gv9WKqbeH2VxlxJHRSWImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2wjf37l_VvngsD3MJppwUs4mOQwqblmElXL6XCZRMUjgXxYwdDT02Rzu2gx6YALmJ4XxNTNBHAYIsjXBbcqbGQDUUkly9I9HhkcyXjLOXFtowqC250g7WHS-ZE9sfju72v51-Hkv6ZqofVEjGouIdnpI_aIeNKUIUcG2ZnSi6p1W0oU4jc2BcrJ5hXTo_ycX7ZeZIEGL2dcE872QHL26tF497Yc2yskpSCC0d-q4n934hC2ipB7Zh2xTj_6HNB8GFnvqGS6q-hy6DLodE-lGJp3OVxoGKe4zVvtL4ujzSpynj17FCEZZNMY4Kcldj1PLh4iViDRRHhtP9sZL5qZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMJu3ibkTReY4OUC6dyyAXmx6BlVB0SYMX_5Jac-8J5RMGJQqwE6v7t7H2TfHN1LEsmq8qGc7GKWLYEvbUcyjB3jsAJAkUh4unqPmSBVfqDLL6KGkoecdNxoGiM_ubqvHAMpNV30gUvKjEzD3eqdUog0vt6QnusNsnCO5uVOGd_2pZXuoIxNW8LlVmHzfdiOwqjO9l6Le5ot6JnR7n450yeNGG_1Nz-xptOcAydD7cLKQNs4g2cGLlsGNrAbqmrEhb-SkLjFZm8hCLNPTNcznmm4phOToLk7frRzVKxrxkjd7L39TObw4_Eeb0wnS76PeAIrO0HnDgUVhrtrqx4ovQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE_nDhLVrS5m7BAVB0Xgqs3_uwj_6MjDTktGhCfLhnyazmTI8G_xkYM0LLynQYFEPLc5iki7kC_3zYEO9yU-oU26nK_HOrZqnnab5kqtdyQuQDgbQh0qAi3sg3b1sBhnqKu652Hg6SSjckqkrff2GOeFK7f70WD_S4ZD8UOArGfM674Ix_0QVf1nuIe1EPh6h1EOJEz0AJ6JJxSgCIMO1HLWeipxx7nLWciGR-v3na3OA1px0dSyFiZ1zwlJoXY5oTULM7mIGCUauZLe0mMbCBHPUUGtmGH1AlLsEEC01F4ob3qDNkB8DiZfvW0tLHikGzNYdKdg_XTGEtL-73gExw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUQojo29Qjyh7goRX43QFrtYe-BhWdCEMI70WeFHYS8yV0E0eo9R17zdzKsMQtP9AnonZmriybdcQIYM7qeXeL4Br57tXMHiXVAsvWY_N4WWRCl6qcLHREWosviBlt_XFJ0O53DDLFI8i14qds5Na-kKWR7btG7P90aMBwaE9fOIMVTBEhDhjE4rgQOv6xCX5k4MpTYy72e0KuCNLPTpPrmxqQSMfywCSbXRn23ZWillfNdrceNHOu-raXqVkE1Zt7mMdova2AoZzg1SdJhR2z1bzW9PCWlX_nSuWGfx9VDckdoKRZVr8T3WmcHhL0Aq-9-VKaOkn111HItnB9MqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbu8dE87Ipdv32jfnosFDPPlrQooLJOvm510fyLNqJw_kNf-4fCWiL2dfyYbzxlJRfpmd5qFEeOz6XQEH5NBffZKFZC6cprLPEV1UPdRMt1Yf7pniY3BGDWSQhGdw34Ib9egaPHJBmdQ9kEqlrtZ4jPuKt8gkeAxdk697nEiJA7efPC5TOMpfGZk3LfZ7N6qDnMfRL8nxsYDfyyIMU3sP-neswJdl6BeYLYTtyl0ghtMi6v4X8rI-Grrftb_IZv_-h8DA8_YHO-UYfUSXLI3ldcf_P1ToL7rDPypwvtU8NllGPdH349R5a5iTh3H7xwR1Qz--RRkBeGZNXZ7IPfw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7n9IWQHVqb-fZcykEW1RLfZdaGflsUh2IpNM_12OG9IU1v-aMdzsL30XWsfdNNvq4WffiMewIsbpL9eemnAuWMEWQJdEvZMR7gAxqtMpc3KKMJ-CX_kPaFziyoqwbG626fW-4GapEOcTw3NxvcEbDssuKN0KO8q8e9oEwXX3g2ou8BrxK2r8VR3rBQ7l15Acg-aBG5vRQVHm9qHnNcS8YenEtbXbWH3lkva4scisE0nOVV6tAEzVtYTY7HqeIhT6jaYsW8adlH2VkasCQKpT8Dt8hTuJshSRMKDx5mwyq-AIj_JZHcwQSr0nAAyTgOtTWd2YPMFHSoI7r8xCOlJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_waajeWBDrfwoMY4RJwKwkNq_L8nkg77ChGsr737KnZ6nY_S0rQEBYhznP4jpmHoyu9N9svA83RPxgi4wEKwWSVcozG5N2jgllVbGU82ZfeDMBHbtBafRczEYHJpuS62iC-9JkVQjYYbJ8mN2WjOTYmQMOqG_DpQV9_heeVyo6ZuLRENBQ53XDUDN4YPxnBvXMp5hzNC6Mk9U_vn1fMJ-Pb1Wjt9lMAMN8LkjJ5_ceBssApHXlanrzKfcqzXsMw1620WWOn7k0vYwhyqFlBfesnLNtVUybs3K5LYgl7bSoW91jql4bDBZIVaf46i6o-pbVwavDLlFc_bH1r9VTLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2QC8QiqhMt5BGZea8ctUZovLDUSywbAtJxxji0WtGfpkv4B3xNvMGcfBkA2KzpcolXNm4AdHZ_xsPpTcFHJZKrwZBhSS4PFoMTjqiUmI3NkOHfsAh5RaBgMTB_6eoT64-7rEF3ff_q-NZV5gZT9mkjcvwRW3JaR7xuxGUpQ0lgF79PBamkpTZ_bXZ4TljYDJips9LqqtYMRStdO_ft_JZWUIJMurT4lvVGjfeUuST_RG08iRPZD_2OZTtxPGwnN73R91HDUQheecIKt-HXKsCzbbrN6mUi3wM62tm8pC_sS8pwgnu7dIQWpsHHNwUPu2Om58dJJsi1OTAivOxzYOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXIkhCgJcl8XbKMhv29XpFWzfYSIJCTcnlpISdFx4J7EVXfAJhvxNafIqHwH9YbeyONO-mrurAOKBR_2rPAd9uX4ANoL5UOG6CY1o9TLVqRrXMfBF1Agz6rqAhLBueB54yLyiUR0x56XNKZzNhEZ8Ltmvm0pwh0l6T3k67eLvX9cb48oZ46MGky9yfrlhRh4UJ3cFn_O90aJzrCU1iWkEhDr241aUh2GMOs13j9qsbPsS4oX2E_1-82MAmyf0syMyU2k1t0WfU1FI4plZzE1YXZ_Kua5ChUrJN0jvUWIpyUSqTkXMma_p6K1xididXgOqw2wDWtUuxFWp0DjbCbMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNsvshsvTWYtM18kizVP3k8d10qplJCFCXN1y1YkpRFvGX2ctbgGF6tP3-h90mFksxDTAY6hEjw3nR1Q5b-6ujBO8VjE6uUQ2tvO5ozxOQLQVKg-oFKNvEUIb9ac9LmI-MLsezPdiK5VHJwfN0eSjZVRTvWM92iNLNRydIOPBsXYc8oxhBozC0IKlZIPmBUj-Zbn6w4rxSeJIkcJGj4ALDW3OxHErN-jgMOXOeJRjan9ssyByVS3LWgjJxCfTGKHwXesFJec-q2IiVisRh6Z613gjUIrIDL0p3QX-VBOtporeo4pcQ38TEAaST_laU61Zw7q4PKmmI0ea9TJXjepTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBPfPKgiScgG9ex0HimG76inNqhC-gPbfhl9HVV2CtW0oEosanPe-l4OuYEUzyVZ2wsTpVxtqtqdclrMfmhtdEdBPtTI26n7K1se5e-NI_oZZ718qUavZbtIigwTJ2aNdU7H0FBkGjSjHlXQMFMBT-no8Wvx6HFx6T5Vxc0HPk0JegofzKfU7VHSOCjWV_n6FiKJwnrOTYXdEIzY8ydExGUbSnsqxeG_AQKKe5yZpCpzM2HKwGuJbmQaebABfeo2qHTriUNnvZrwkfpcqVkSWojrWD_LY2wKl1zh65y78zUuDPJbsT2DlMai2oQvHc9JB4xfvVPg6ox-JBgqScGGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrP2M9o60aT6TxS1xrsPYQ4UyP2SP6GCiRvmytPwoGXW0wnEBS9u7ZufFEjYaZRn3q5faarohYVrvn8-ljS3WBhMuUBzw4gB2ldCFQJDqClamZJHLZGRHUkic2Vq8csxEShsZYjd-MVSmEfoXadVlZMJDeHrm8ZV-hMDzSzixmFGgKG5DE7xcD5KMG6KjWsCkohHsG_su5S8HuyGuMe2RfaoQN5FBGUf5baokJjVKMKUNkDcJspQOV_IO1tisegIc6XHuPZpaaDgpif8NYhVe4C7RkgG3yPQoyLAUMaEYs-Eylo4dlgreBpULa9igSlrMTIvCG1LBAU0_p4TNihBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vgs4n7lMNX-eBlh48Um964zy_gCJfWNU7cmPqnf_fKtkUsdexdHzNdZ3zTfKMNzFE56Sl2CcVMndsPx37gVhMqM3U_pWQQIGnZNHpYRgpRjXZHMOujReQoiOKjMP0o7Tq-kGPlX5EaAlwdec93AoSYPJAcJ1r5kWwBTWkTKApP47kR7pwYrV5I3iv54GlDsK9q11Uq-VISNiZktl8QxDF26ay4U2u1x4ptjcrnktCIOKM8bfD-XjGoBWK11pGeMcnWxCYzhLCpd8rt9_mb76_na-reo9_QgsXdQHdrPsoeoz-vFTugYn72EpA3zVL_2GY5HfjQngej3wAVSPq8GINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT8V9RTnDHeiWISH_hUajQFpq5B29lH4Te-P6THY-B_33v4RL_36mKIZKJK9ra-Vr2qm2viMxoqVA_j6P2ywVUAEokAY-VCLsjtkkBDDirK-Wgve3JxeA23hotPiFDwVqk1jBTOS-1apx8mbGFQHtxKc3zywv45tOGz2EiH7JGtoU7L1ClUQPaA_fSqTEODkNdCVg7h6Zc3RaqRIdn2GC3LzU6gN1uPv6xujcc_ORoMCd9vbv_nHoXtdpSBsiwR8rDk1_dQveXIQ1BIj-Thp0E2mw1Ek7XRDiEndtOYzfYEa5mrQYduCkHoINFhiKQxctsYoBpz-TzWfuyhBuL50tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbzZDpGQqntSa1HDH2tsSXwVWVTOsJ33wpFbWjPMWXOSB0P3XbQBrDetBVpoGnQc7TgTdLXgJKH_QZcIaeJzZrQV_p_7_iKKHFmaH4Yr0jKTQlpzzIDzQ6seN01SVWL7qgPbk7GpP_hsavx85FU3PnvJ_wMKuKSXJdYQpKv3xvLd2Rtrm2DHuR94rrc8_0TZpLor4oAUX2aAn1APu28w3GyFK9LbJjoShgUwHBgmXpmGKiuWcjd9a8TiEtA4e3u1PmrPNyQkzEtkZXdmTcGnUn5E7Y8dD0joK9msWds89kfBL_Xtt2izAT2CbVeWLq_JZs-ekHq-txrVjcu_HzMvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai178guzjeoVk0nd73JUTHipkka6etLSH6yvGejyxX7j2q96T7Aj6g0raGP2PQxhRRJmf2YCuWBQa6obxNlhKpT-hwOyt9SF5f7LYJZNiBS8nv2s72hh2JJIPWSHl6QwSNwyAnqPtL5kuOQbpS6Yen24uSjsv5FQ4dnoB4hpAGlxTUB0acJVouE8z0pvPNhPxE6dLiIoR6OBJRGgOPTQnQPdaXVBF8nNuqj4QpjgnFmlMaN9UieFiUj5xQ5jj4bwlQRTVFt3qH44VYz6gGB1cErGL1F-y52p46QGILstOAFOVcNKzMnwSMSBi-pdVTy5lturU02eFUKp473KkEeqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukLDROIkoXGWNSIxJtLXQmPvoTub9kKitfeFtTv3glTRxyGib2xQkuEieVVRSa_w-noaK2NfxPl1fR363r7fMFrawY4hQF-n12iJ77WUBZcrpMVFZPvgCwTxxb38Pq-N-IoWa7POnZJHpz66K2bvQv_AxfpzyAmsGMuB5rTQ20qw55NDT6gTUsVPls1p3qovYYKHkUHGGhKf0X93LfshMge0fl0riNoI4sv51I3p4oAvmyBgwGuNdQdT0mTsvQGRRie91CqTiXKqgOPItWyctNa2UvbrY3KhlcaOacLRdjjROHqg9t8x0DtqW57kfjc9Vs_gTMvF7vwWsmfdxFmWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSoRI1v4f4GePaS8-2Zir8cKz4TJdD_k7qcQdl5ZpOTiFqyKUtdTI9aw5_Kp8XxBEUu07ymrOth-yjGvgzPTfwlw6OoEFweMCHXJjoa2FAHMqNE_zPIbGJvdWMAM5339A3LMppJaVc8xkaqa4gt4DVQlqH32-4xERmR-0gMTQC_-gZUnYRbxhbNeAGH9YolXxgqYx-DY3eU4FHMMGtyKSH4CuhIYc8_qTxwQuRwTN0lFZ4ao1sptdyPsopdd7r5byfvr0YyF_iOFnWdJMy-xwFRDlf322S2ueQli8a6JCInFsy80ccVG02aBlLln4NyXehsYl7qYp_kQpji429TkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqS_C7vbxfF-fVRDQqMjMx_m0V1D9YUML8Ilj5CHJz4G-6W46vvZYGgRdDQ26kZ7a7l4asVf-GIy_xG2ptxOVfgGG_MtFsYlNXofEXa7MyniP7F1H8S5vnw7IvdUA1FdxCCSQQymzYtkInHY76eSINX6xHZ9bTp1K_RykwCqcScFhehQ5b_P2bNIdX5mPY5V5B_cmXN83J_xsldMaSayFYQuYJ3kQHB_59EafW7SiLZCSm17-FP4wguexP_qyiuu8WE0CN9HGUoPJaDLthRFd4IOUSRLSQYhsWsYyzYMLCz55uLS5EMQPwqu6jQpAEfFHGkPU_XKNYe2Sj2AJUHUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyqOeyMUOEOwa-r__hQyAh-KAhEFOSpIh67kNZ23Ip9-0z8-Nz66yNSLDE52Qh6OKBpDWOnXmGLURZSuTsqwEC3n-rzA3D3EIKY87DcTWQIuRhNJmbFPCnXyhoPu9EIyzKHpCqz0l1DWyS-hfdngMlMdngd0KDQlrcuhgoDrPBMS-FoaFRCsCq7rSYtK5Tzn73ZmNzPvrwx1TD4SoOzMJPphuJaGrFo_82Br4nRRfLgyN_4v26q59_tM3copiLBv2N6aWlkZa0plwyzU3hUwY5GPBnB57glB2VejuTkGoM7CDcG6RIejSEtCLPqEnHv0FVh-HmwMbqjPgFQBg4nwrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M82qaD0UDpOegz6oCcUm5aeAbOFrE6lkFBZiHq2xnUKbSHmdku8cgOVWhYAhRFUaW-9DrSY08ptRE8Tp8StGwavitWO3dA-aXNdMwXg2ZivRLx-KY9VJVXD2NZRAarslPwKzG8pEKjvHqamcD1c-rokn0plpFFKWiscIx3G7Dwpxq2Z81x2DX3AcWn1NpJx9u61RL2MgWFTNx9vaRo_KzzINs1_T2nyYa1ec0A9V793Di8kNJHe_tVwEDTtYjtSFDnT6lOcWY5FGwBDuLbyX6y5JwAz23PawhLTHOV5jl1RV3MkicCkSw2Jic60mlv7PDMfALWx_wXR2lumwNdlFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwoUZWSEMBquBfGOaTLIT5M5JxOBOQvbo8HdqLrMGLMEarikc7SJymIiwR80VGuO27_0HubBTguBiGcYUJ69lnDJlFtkg2mXGD-OglN1BUiAKrmkfxm-GO1VlGnGMGaXnorjjR7buxpVIEr5BAY9T81xxBrojRXzgthQkxh57GsN8sqXx9bT-uff-b_Q8nJnfNNLDXnARE6JAyfDEbEHa8Qvo1qSpjByN3Q3h6xTZYvJLBg-uNJKslqPHCbOeh1oci4DBrbqfM88vfBNdM_D3KVC2XA1dvXvH54iAiTf0CKRYPHHw2RmjnsgKa_Dkdu58E96FOsJYZqHUcNUTlSswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2FWxChC-apXsrVeweXEAbmz2Lrg6XAtwZxhXk2YN_pTXBMovTTiHeqDvW5wF_xTlFpR7AUzfyfabPzoZQNvpSO_-B2GyV4HImCgOgPa2Z-XbhIpmHsvbseigORrDgZA0QneQVGulPX80fwo0aQ_v_LGepqEJUSrN9DHV-ZSbFk0VnZp8Ziif-OA7cQ-lzEAntWRogXXMQnAyPJ8HEU-s_1JdIlJfyEIGRTHQs6lm-2XLgZxIjkLOs1ZWaaqjjwmu5vUgGHbWVUKFlfVmh21irbWWkxMNaeQFo7-ZW69yZHgMpcmdf8G8Cyk31YAVtaLle7oZwoooImRzQ1TmWYrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw5tR3baxK8KdiCWnoMERJy6WK0EQn4iIoIt4xvwNWNgS-t4WrBFbA8Y2bYdgQI7PMlpXn4eajR5CCDWaNtgsV_S4jbPde4sB0_HfAJAmHj_rT97baGt23cX6gTpiaCkEA-_7bY4iG9BbtO-y16XoNlo70AZ0Bzcd8SWVUL3UGnOrpC7yxLEGx39swGcwv3Lr3X02cq8Vrq_fGpQIXyCXZtYn_1im4fOpTBbteqjDHfot1yyOh573E2rp3au4jHWI5ou5_RsZQHIpWEsPrLKIQmP3OESYPHmC02FFgnZ61waPz4foXR0p-trEBvFfncy_N3sJJ2z26VpNeQAla-Rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwCxlq2KSr4ft2vlwg2tuN9HANf2Xh41hf3-sFCkVLUPAfwtBJhXDCBjy5rqdquQcBNGSfzajp50OCR-mKdonbiwS_Jql4gGvpIvjWOwjDomr0ZYDdYiiMCEAewapsvVu3NdrYFdGYmGkXEYJ8tfizB_B1sZ0fbsHp-ATPDVfkLNMAbojI9HgVWnXDWRXv0FHJR0DgB0lk8ZCR56M6j_zrFiryiosM-HSWTZDzr8aXKGqly0Cb4IxIolE2fpNaiRe9gSZvCDy18wxx_xtqPjLmJi4_6AsJRrjC3I9OQE8KzdkW03WTBRLHGIkdaZLz8pmAR7VFM9HCD_vLoCu2Jh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Rahwdcxdtz8EgZCRQkVLKhKwAbp5E6ln57eKJM0bNGRnEnAJOZJVhK2h4x8McoDTi614vSrvNC_2ixGRgV2YKIcqfe0asf0N9Dkl4F5UA2tqOEmUDTlV_EVIKE9LBBdv9bb7zvhT3OuIJXV2LEnfujc6rFqpLjtZE6h03MQTr-4iGxXz5jyASzobjEaAYsUaqvD8jGTjcI9M4If_efunfiK79ipE4zG4gWalSUlyS9Lcyo1P6EH0h-GJl4b25Em_fUeiCyaX5ybD1BWiW1AyLLB6D0x7sdjuB2avj1bOQPNKKhByHnJn3NO7tYs0Z5IkVYWeCv_oLNM50RelYZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwt-4JKFy49ZH-2zaJnioDuDhS8fevVuHDoIRxRFmXx_y2X_BsK8Vp3J4TPITJ9oAVTWptQuuGsmcY1gKqwoQaJM6wiadRTFvXmligqKXWFQrctRwJl5945q3BbkqsthulLSiLrd0-amjzBCbss9ejmK4y6mHgT2dVmnzD8pKQ5t_mJBoR4ZyECNILx1D4-87pGprk7ki2qmiYiCw13O_77vpTRKdrloK8aj-zM3-_aMxL8C42h3CZ26aRAykwo8nh7a1MUF7KkmSj5kK20iU-fyB1A57wAHcAiav-mfM9tgedMRYX-tkmfOPnHswxwCFFFc7BUr3FulHpt7YE2kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وی‌پی‌ان پرسرعت و پایدار با قیمت اقتصادی!
فقط با گیگی 4/800 با بهترین کیفیت ممکن به اینترنت بین الملل متصل شو
😍
🔹
تست رایگان 12 ساعته
🆓
🔹
ویندوز، مک، اندروید، IOS، لینوکس
👁
🔹
دانلود و آپلود نامحدود
⚡️
🔹
مناسب وب‌گردی، گیم و استریم
🎮
🔱
20%
تخفیف ویژه
برای مخاطب های عزیز کانال فان هیپ هاپ
🎁
کد تخفیف
: funhiphop
🤖
برای دریافت اکانت تست یا خرید، از طریق ربات زیر اقدام کنید:
https://t.me/ToPoLvpnbot?start=start</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8bshrmmnEDHjZFBl8C3fImwCD-Q74C8gf_V2EsR_mXYj7CXkuMM5p453ukyk4ShinjMv4wX8qGXiPbGqnr4irmUAd3o7XJczH-ZfOv14p-Wdyc8wDs2k6Ch05EFbb13xuLPbi7k1JIenHQzP5mqQwA1eXST7eCjr4JfoK1l27pU0ptnUayTydmKHFh5WjHmHNa1nIhOVMr_HAZi8j2OoFP0SNIhwJj8nwRMYWdP60E3CRwEa4LMbFgTjoPHjK6E-na_XRAi7kTprB-wOjkYSu3KV2DZ8hPE0ycrXOlSQAS50XarxAJgLlXQy-AickHvFbIFltATr32ez2ANk3DtSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FS61OTjM9kprF3XOv6p3nT1W7gHvZ-M4lK_bCfK1arjEmrPxTyTuJA_VTrxGMQoKuVBtNONQ0IV8Cc5xr6QuWa62DfJFD2dM6O6bYUXq2c7SuPetk97dls0cffhQV89dUZeajKcLCP0oO-JX4ofXneZq8yrlEK7K1XRV12-Jv7NzCiCBPsRWX-kE6OtL5qInUH8caY-xqA27N1I5uqGlt3vTB1ubETdXaOmOcospA-DK_UdY4B4H4dAEGe3egcL0mL7bGC_0ESAlk3s7WojGja4P-r3Z6yuA7T8OyVoHIZXhHL5KxXT7tLgq96hPmTYms1028arfIu8wmdCu9lfYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTanAQhHWaEj6w3sRiYUBJOqFjVg6_DfeUlEXlIAsVrwLA03G2xtqEL9qVoKGuShKGkKrgVFhHW2KFrwlxXmi-rECrQ072elq0y3sf42vIvHYJHr93ExYzt9jFiy_EQ-LJd55-ILVTOGT5gIoHGSJNK-O5CQ1mBb0bMl0SaH7V32r1UDNA2c_aSKfvzrZPhSqaN7OFQT-3_ML2wWlh0rPw8CklrTGwaR7ai50jldfZ50xjort8KFAKxu8qVYKEOTAyeOfkaro_q6ts1hrPWk2VVU6ieb0H8WX7XvMsQlJrWsaedfp6BD0C0W3OR2RyrUpUPHYvVb-41tNO2GR9umig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxfq-izA5Cp3yUTa_gPaWNqya7jAbreuh3tJL70D8WFd4rGOBfgsq_BJ2FG3GY9tbHYx7X-8LY2TWLtlaFTJa1uML_o_DrS3HCd8OfB1hKWtJ173IFFlYFU5svz6S0DxYwlGbgpp8APnV3oU2nFGVakRsftF2f3h4OT_3JoSo-G3iPKd0td7q1L0K6RQQD44KS_L11BkUcdNP3pU4VQinng8KsTNLJ76tG8UZpLaGA1vP9tk6PxS6gIWWqjwUfLEKL8gXmQ-2cWqUpNtznonT_PxEYUdAaODIAEkfmKHjjnc0OeXu0cXQZwwemBFSfx8CGiYmv5Mm76XHVR7mziYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItTW7NzF5NkZGknGfbmm7xsbqv9S3v8UrPbNwxOFs-61MjTSYZYk15zINFL3Xg2rA2ukVkQn_mcd8bkfWBNJkZLPVRawyJMMHM-67SQSaUWefcsDMQGzAy454N8fzKo6UGslOArQQA-Qna3MFlF4ZH_K_p1HJsKyMUscm1r3aj6DbAdzW3yZEZJSVTQzOboYrMNTyoeOM0Zmh67kc-kaEXrHPsK529cXl0tNIJzcMhEnsJpai7pQ0LpemeRlWHfUBvpWnAq1x0hPjyCrKJXjOx5dU7uuomjK-8jl-eWKCZ2T_deK2HgaNzndcoSiM5hOw1ujzsDvk_9Cop-3m8AROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81297" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=kTS4Nt12juFwuR2oE3wllOvFYpVm99GxthnJ1lm1BUhNzv2UDKRtK4gjE28Th5_d7t_HLIKj-YHOlsgmXGN2w5_y_z89zfqeMuU_uRBW4CtVN9_1zIHwYbii56-S3qXekM4edndpwJnOV6eaHc047WUWHeuBjjP1Ajhi38ETAW1PXebmvQhZ9nwwWbb-tcOYqtfR6HnXnGA9duFf0O6R6l1Msr0IcNpBPUxPAJG1ePaVHzVyNP-5Ttp7EroBmfS7uUaZhAjDupsFX19F0tCOJNviUqv0_E9hyfgj2myWCk5eXOKIRX3riBgFXiCXzoBcKjVBym6BZGOokMAxHD0ccQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=kTS4Nt12juFwuR2oE3wllOvFYpVm99GxthnJ1lm1BUhNzv2UDKRtK4gjE28Th5_d7t_HLIKj-YHOlsgmXGN2w5_y_z89zfqeMuU_uRBW4CtVN9_1zIHwYbii56-S3qXekM4edndpwJnOV6eaHc047WUWHeuBjjP1Ajhi38ETAW1PXebmvQhZ9nwwWbb-tcOYqtfR6HnXnGA9duFf0O6R6l1Msr0IcNpBPUxPAJG1ePaVHzVyNP-5Ttp7EroBmfS7uUaZhAjDupsFX19F0tCOJNviUqv0_E9hyfgj2myWCk5eXOKIRX3riBgFXiCXzoBcKjVBym6BZGOokMAxHD0ccQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=I9-fZVYflwYBPl4NsLcBaU6PwgSVXfxeg6Oa-_vJZGlX89jRMROnl1QJySOUB3ducR4Ubv8YHhxkzxWselBVjGyvu_rPL9jTKRYwxeLjyLlrNvWwfvf0Wwu7hu6k1Fx2w77Nm1Ad79LwjRF5bbny7202E5SrS0iUBzDxeHOoWuYghkYSbUBKgdTOXScVdOO3YiCzZPCDLjF4RQaWUq_dTVtWsusoXadM9HCXVaoP6CyIUHTYWNZAoY86TF0NL-mpYifzzd5Ip1bll-jgYtRa2zAqZ_JIouYvhY_HVS0dNxomc05oRdKFH_Tf5LA5uY8AUqiQkGrrFFvQnAWmTdxfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=I9-fZVYflwYBPl4NsLcBaU6PwgSVXfxeg6Oa-_vJZGlX89jRMROnl1QJySOUB3ducR4Ubv8YHhxkzxWselBVjGyvu_rPL9jTKRYwxeLjyLlrNvWwfvf0Wwu7hu6k1Fx2w77Nm1Ad79LwjRF5bbny7202E5SrS0iUBzDxeHOoWuYghkYSbUBKgdTOXScVdOO3YiCzZPCDLjF4RQaWUq_dTVtWsusoXadM9HCXVaoP6CyIUHTYWNZAoY86TF0NL-mpYifzzd5Ip1bll-jgYtRa2zAqZ_JIouYvhY_HVS0dNxomc05oRdKFH_Tf5LA5uY8AUqiQkGrrFFvQnAWmTdxfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN5Ovx6b9JWDhbf26U7LYJk5_ScIMzn9juxnMJWK2JjdZ4s8uGcBM3NGX9Cn_IbMYphLYUvyCfrtPi4sV3Hj-VuBLuJO28cem_SL3LYKNZf5QLRNnrSPYarbuY61hxoOKCxYxhTGGkgOSvmQvtfe3LBHa4hXYFgcPt-WTNG6wo_PA2WTqOuZBX_0LOijmnfUBMJcUaMX6dyfhaV87leA4OnlkftbN4zuFX628SzrdVF4u1kv80fNLirF1zHyGIJod5iFd81TE33wryGhAYw_pISrXqBbFSQZSuboWan2pKCimHnHPerLjcDMo5wUMtp5m56jXg8BsyBMwR6krcIqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=RvhZIUQpJ5QXnIe9W7woBxFFGRx2_PtnLZWvo1uLFhAPswy55M2F7ESSf_UT4juRlBYkmp-qOrzcFkPFT99T6hcq-P8Kk0kiNcvp7E4YSPUWgSWI2YgxjXf2z8-1o4G-prITyPbWcNqKX_wHR9cq_O_aorUwFiaT0HDI2RR4IiAy5XStQD9_D5q_ewHj0R-7qRekVvJZiDh1rlllpka1wYOaHovvpOcuLnXgqPtJgtav8LSgfLqEXMAI49EmX5F8Mjwflh8It1zX8_qa-4twY4aWw6P8Yypl0eQiHMtQtnzuHd5q8fVTosagqP0l-_za4yFd-3rfjs9hblB4Nm2xBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=RvhZIUQpJ5QXnIe9W7woBxFFGRx2_PtnLZWvo1uLFhAPswy55M2F7ESSf_UT4juRlBYkmp-qOrzcFkPFT99T6hcq-P8Kk0kiNcvp7E4YSPUWgSWI2YgxjXf2z8-1o4G-prITyPbWcNqKX_wHR9cq_O_aorUwFiaT0HDI2RR4IiAy5XStQD9_D5q_ewHj0R-7qRekVvJZiDh1rlllpka1wYOaHovvpOcuLnXgqPtJgtav8LSgfLqEXMAI49EmX5F8Mjwflh8It1zX8_qa-4twY4aWw6P8Yypl0eQiHMtQtnzuHd5q8fVTosagqP0l-_za4yFd-3rfjs9hblB4Nm2xBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxLr44Z9DEpsyKN0k-QNilcuEnpDWcsHyNriVnjBNoaanEkHOiBVladlMuT4KpYSVrqwsrdyxucre5pycAsYb_2yCKMYgN-0GZEyGil6D6Hjt83J-C5bU382wNjFPztYmpFQ7RuN44ZMrKrjKTVvt-BtXCF14lv93mq08Jepbebfoq57i31Fpq_UbzQwG6i_sMt8_3ARcBPlvXMNgD_RY-RUJ-sGup431iLBIEB0ZtJUNtBv9WwmCt-odC9n9FKR6TBJuieiEN22C5sTWSfYPJxgTE7hBCFlOP9F7GtAK93C2sq6YoACpRCE3f0gM8c3Lkc65hobQMQrTpPrF-xJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzSzy5Uq5l5V43iN11rB2HmuCAthoiRewf7eA9dB87vK0uel-8C8sGu6vAcee29JJ1NhqAmAnhPu12RDtJPGVaf9zLusUDviPSUdK7hnBXkeWwlC_Z1YScYBbK8q7iG9Kng1SixIT8NK11JRl-cCXchKw6WuF0Vsktd3DkjQYDYCwg37MtXcVuwvHRiW2yjowthFDO4RUhSIw6TuQGBd0xhFJ35vse-rLRSOh-Mxwa576waQCpLMzhZNv3w8G2DOASPHfD_MGdNTlzgb9WKc7BcC4Haih6Lc9PW68ZhGqKQEbizgGlR_FCV1UjNepu5125dpe1dRk-r6bgsYsEI8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bttp49qgTtL_F3umtKBUQczUya3bpZTwm6Ue1yDbZHYcRFiVcTxiiCsfERo801zk9s1aaCGb00YRUUwJdEcjxMT-i9S2VbxNJbcaoDyU71l8fKUqF6_YW8S5wq1L4qCLvWxF0DuIh6xK44YHDAYZWv9VtRz1DXIDKvzxVYrM4-frWA0l96Gm0hQKeCvAmr9PsoghnHyGAcxl2n0rv6uReqLmknzxrSI2Gyc9oOLZrdOI2sEkGaX-2BlmEka6AwHLIZc8-6ki8u41K0Twn6eGVg85kntSTo1WCpZ2gHQockjLDyQmbSk_cklDvSOwEabEkf7d5AxC9yHVQ8Zx2OGAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید صدف زن هیپهاپولوژیست :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81285" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsctHmISZfr53epgaihxprsdrXcCwFnr0Qz38EJEGOO1Tz25atugHqLT0IkEyyJMqSbgegi08jIpV-FZTzQpMUVqwnwIwbbvzS26ts3lOFAW-Posq-hQ0PD--xIKasNNBJ5buHpq7cxpD4yLCsca6BzRtBqqj64L4R5eIeq_NFTWZw3sOHpCneZ_y4VET7bARctUNsdyuAFoyzytcDnHlyukF55YwEcXztVcBt6lnTHipyXJU9IdEVP6fX9LVfjvnV31aC4hulnVHQIIbozu6V92Lu53qSE73TmRTQENYGjkzR2Ktgd8aHDSHFKf6QWfLeLcXUF0eSrtsYSV0gqvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81284" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShrdiR6LBLPU43ZnrbjY_VfDEKLVJfcPgkg872kwtuLNhcmrwNpjOPyxh0GYPbHlyZWUtCavX5hLt41t-6w9lXFlK6Z80irWajzLi7DK9ncudX_X0V5bMVK5xhwJwYCPzkuYhOmRDR2dJApRXhc1MEov9mk9J6jVkle1rpaY8xfkw_0zoffD1VkDiYDyT1MvgLIEVfQTb3wvnrIoSnnENUmxubwxm_Hnm1C9GsntfMCSXGAeaai0XTFtrPnWej_mi0Qnxc7v1qcKZKJr5XAAg-Wvq65t0pUJmuQgCUdclAMNZF3fuExMPEYHH8To5u7oM5t6dzoXuocIM70C1IwAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تجهیزات آمریکا که تو دو هفته‌ی اخیر زدیم نابود کردیم ۲۰۶ تا ۱۰۰ میلیون دلار قیمتشه.
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81283" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خداوندگاران هفت آسمان را سپاس که امروز من را لایق زنده ماندن و توانا در شنیدن این معجزه‌ی جدید تمدن بشری دانستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81282" target="_blank">📅 10:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یادش بخیر امتحان نهایی فیزیکو فرمولاشو نوشتم تو کاغذ بردم سر جلسه، بعد نمیدونستم کدوم فرمول برا کدوم سواله، افتادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81281" target="_blank">📅 10:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnpnBSrePErISvLXC2PXUMMKdmDLx5QgTow2zJn-mMooA3vBtIyXPMyu13hrPrfxu5w31FJ_J3z9c5tXSC-UZGdoJ5kDxo9Lmtlqqm2NiYP-rXSikfxMDMfOZKQQmgXfGZ-5J5o18Q6cb2JCxH5clX3SAPrDtqikbXagAERjbtpLgOIj1i7nm1wTNZtmWk-eXjdjY_dadpnZ8NyDEFSxljtj-k2_AtUbzw-TEgVSzzGUprAAfenjtmkdMXBKhPWm20HecxuQlNaKGlzxUBjrOgvfj6qo6cO7rBc3M3eVJuJsKCKnPvlnCjiNNneRileuFspEDZEibt-Avbqp_fYvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاسی بسه، بریم دعوا جنسیتی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81280" target="_blank">📅 10:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آلوارز کلا سه تا مشتری داره پاریس، آرسنال و بارسا، آرسنال چون داره وینی رو میخره کنار کشیده، پاریسم چون فران رو داره میخره کشیده کنار، فقط بارسا مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81279" target="_blank">📅 09:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امیدوارم زودتر بمیری مهدی اونوقت حافظه تاریخی داستان پسرعمو و F35 زدن رو به همه میگه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81278" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81277" target="_blank">📅 09:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81276" target="_blank">📅 09:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یارو پیرمرد افتاده مرده ملت ریختن سر جنازش میگن ۳۰ سال پیش خایمالی میکرده، خب کیر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81275" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلبریتی تو ایران همین که خایمالی نکنه کارشو انجام داده بیشتر از اون بکنه یا فراریش میدن یا یه بلایی سرش میارن دیگه اون آدم سابق نشه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81274" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ4COYaBMjQk60KiUjJyz_ERzwHGw_A6g9rYMdtRkmFERPrLJ7bJhx_trTV-U_SwDE8UTehYvpuG8ggihsZqAoWjvk17zUYgMtVcyYvoS7-ENCYDQraB-PXW2rBTnSjmJi_qAYB1RsC77QNaBVvk3pDYUy3r0bx44EgUKb0iEoHDIH1W12qCz73EYnkgkB_f3CdGYAZKb5d1P1U1DvQ95PL37iMAF0TWztXcq2UoezUyiofn8YvAyC1oQwQb7_mbML-rDSWSeEJdBNT0y-ZHhs1fFoT8C6pjvzsSYeW-w1ki7H2BpyFprZjCXSb0oGb8r2ynYHj_NotayKZSKSarmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشید مظاهری اومد مستقیم گفت، چیکار براش کردید که از بقیه هم انتظار دارید بگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81273" target="_blank">📅 09:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwGG69O5KqOw-Tc38cZJtTEd2PmYfdVy0mS20TTqzGGs0WGOMG3pScka5ewnnD65nio3SczXoebVCPSFy2-MXEKsPUvBB7sC68EEUB59S2hgyTIGXILGGc2bPJUjHPMupdqtGKttv19TkEgzK-TT5LrqQYpZv5J1XZQ1dKuBUyK0olbDKi_EWy4oooEIUEfsEihpCAsQ4ezcnRk6q2gpHvo3PjiUaCaTF2QIat3MsxvngOOsi-X343FousL7ClH2RsNIuSd2YsHG7gyN9c-hrdsH13iBifSbwkYgp-g-S-3buBPF5ako_1rk-IHqEHwScgCf5JPOi_tX06Nr0KSQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81272" target="_blank">📅 09:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فیتای ویناک و هیپهاپولوژیست از سپاتیفای پاک شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81271" target="_blank">📅 07:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt3SHkrU-cm5rHUa8GgMGt-PiGUkpAJ_KB_h4EBIY_P-8G2RGqKJXZV6VcKT4i1WB0EzPgOjGHarMs1Bb3ANkic2RH6zRRClwIktrhQZp13wXrj4Hde_En49dle5o0ASiNRtfs4r8lwt4NxeWnFnLa8aIdOcA5bNeoaWUJGBjIds9JbZszI-V02MUMvcV-VHPvh_paQtq0l6X9XlpToD6V52TH7WcGCYuvghBT25WPf4hO-hh1FYQ4ekCI2zn1pVy5M-bxfd7x78LGvgtADGNLlYdPYSI1Kt252TkXnAaYEgf_5rh5PEG8iH93cm9bIlYdpcZ3iAQiyHWbKgkXzBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود هم پاخور بوده پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81270" target="_blank">📅 02:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81268">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایمان کیرم دهنت چرا کسی جز تو صدا نشنیده</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81268" target="_blank">📅 01:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81267">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81267" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_dkTTtwflXOc4wwlcbwTlyeH7kbHDx11Fe-I8xyKtcrNr_TtB7ylHatZABkZi3b3U1wjmQyrwwxgNZi2tfGTXkORazX35tAE0s4OewoUHCKSkT6ZM47Yojz8V8-RH84HVTRVhZyb8yu__dgqAy-SkxFFN-PpS7fzL8ep1X76ch2SK8VsJ190ZSBmPXWpLjBhk6JRbIiCILvXQTx4wAPkY8NGufi5k0JoSfWHnTcDk8HIXdfPK4PDclmtbYpFnlpH5KDwrkTNafu6fvv3OvmyoDAuQ9u_jTn_Ud2MT66cEX0Y5H2XM20qkhw2Jo4uS8vCFEJUC5hv5VVe8vljP413w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی رپفارسی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81266" target="_blank">📅 01:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81265" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw4xRG04dP25Xj4SliGjJn7Ol3Lofrcr2hZQD2QrTLBu8qqEkO3BXSwYL6AlDk5d8LiJ3Oa5j4WAY11XUxq0djDFhbxuoBYRsJUb0agWbPrRljAtflZCsNQbqUA1zMU4jziHs0zHOASkZUIEx6Yuzci_B7V0_3Yqzra6c1MtCYsMNGlZ9RS7AVRrSDfLx6LmOxdpa_h5Zg0qG4I1Q8g6-U3w6lhaQWCpngORRN4YO6UnbMx5-R3hQhVNX7e1ZdzruYruImdS4sU_Q-Tnz1v666ogeQcVS31OfWIBWdhfHNspZUW-c_kyDJYgh327ReKW3qAGKq1ODHczDVQwfyx2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81264" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">طبق جنگ ۴۰ روزه امشب شدید میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81263" target="_blank">📅 23:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تموم شد، دیگه هیچوقت، هیچوقت نمیزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81262" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ در گفتگو با شبکه LCI فرانسه، درباره ایران:
به مامان توماج صالحی قسم این دفعه
این‌دفعه به شرافتم قسم بار آخره که به دیپلماسی فرصت می‌دم و اگه برا بار ۸۲۸۲۸۳۹۸ام، ۱۰۰ درصد از ۱۲ درصدِ نصف خواسته‌هام برآورده نشه یه جوری حمله می‌کنم که اصلا خیلی شدید و دروازه های جهنم و این داستانا قول می‌دم قول
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81261" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هوف
کانال ۱۴ اسرائیل: ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81260" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81259">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585792e34.mp4?token=A0c3JJdM3LqAJmci3qfdo-QC28h0jOmOIMiQ1JWwNK4ro_KePnMgT3jfk8fGx1UbCUU_uPOEW8qU47kZBzJG3mpuLd4HhoXkrV-Gz0BcOy7bI0Slc3FrpBmc3K4Wuj_fKG0GDS4n2S-ByT36vCrYe8ZRFLqaY4rn-HcEpx8ojKuSpaJDHmRsdPlv_qF1Ru5BD1fB_d_4KgRoPngFLIkYnhdn3Y6OBcce3H4SF9ui8ljMnKKcITulhDuqC3sDABFkx3kDC-Z23_OVh4iAlqCxWYABgK_64KCeW-Sc_o8nYheZEtSj7ONI6SdSv90fvdB6C3rYzGzSkYiB0Elz74zfJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585792e34.mp4?token=A0c3JJdM3LqAJmci3qfdo-QC28h0jOmOIMiQ1JWwNK4ro_KePnMgT3jfk8fGx1UbCUU_uPOEW8qU47kZBzJG3mpuLd4HhoXkrV-Gz0BcOy7bI0Slc3FrpBmc3K4Wuj_fKG0GDS4n2S-ByT36vCrYe8ZRFLqaY4rn-HcEpx8ojKuSpaJDHmRsdPlv_qF1Ru5BD1fB_d_4KgRoPngFLIkYnhdn3Y6OBcce3H4SF9ui8ljMnKKcITulhDuqC3sDABFkx3kDC-Z23_OVh4iAlqCxWYABgK_64KCeW-Sc_o8nYheZEtSj7ONI6SdSv90fvdB6C3rYzGzSkYiB0Elz74zfJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از مادر رپفارسی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81259" target="_blank">📅 22:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=gHsgxkVWUtdINdkBCMRnL3uVyjN8aFJEaL51ckMRpjkkO60IwNjyh-83bl0-h9Sh8vXqqRfpDTQJGr9fscEzBhaqXkPo6x1G4g2ltcpQA4Nb9ia7qtEM8-xaM7hxaFw22lyoX316LZn-473PUbT_UcA1X9z58EW2TwiutAoLZ3PkF8GunA-X44wRyzHpsAHfTkWeLtcbBejiV4p5rzVtXxIfeVoGoorzXpygmt5Gg1jlReKnOg-3qwX7oCpELbr-02vUnKLjCTEtENV6htYfBCHgCBfkt7LyHADEBLGxm-GIxOeBvmjeyF7Rctw4v13ooRNJlXbiI0Fy_eOQHgYFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=gHsgxkVWUtdINdkBCMRnL3uVyjN8aFJEaL51ckMRpjkkO60IwNjyh-83bl0-h9Sh8vXqqRfpDTQJGr9fscEzBhaqXkPo6x1G4g2ltcpQA4Nb9ia7qtEM8-xaM7hxaFw22lyoX316LZn-473PUbT_UcA1X9z58EW2TwiutAoLZ3PkF8GunA-X44wRyzHpsAHfTkWeLtcbBejiV4p5rzVtXxIfeVoGoorzXpygmt5Gg1jlReKnOg-3qwX7oCpELbr-02vUnKLjCTEtENV6htYfBCHgCBfkt7LyHADEBLGxm-GIxOeBvmjeyF7Rctw4v13ooRNJlXbiI0Fy_eOQHgYFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس داوینچی درحال لذت بردن از مذاکره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81258" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFiNVeX1nyVaZTSIIwvQcimpUmoTbKCE0So3bX2AHdUhBJKEIobVUnnE6Ww0dttxqL55AJ6ZpdyKX6wYrKfwA3J2BBvaA7O-Gj1AQFNwOOiamGI94dfPBSmlaQUNi3ByPTBUpPBHsyXcMKv_wjTKoDwTmnrfRFH9bSE5UCfBjWSjdPYGQEVKWkoSntvMqzGJWHE6uExy3HtsSXnJOszNlHyKvLBOMNu03o_MM805AZ0JYiMPTUi23086B3HsZszgbJzsVKqXn90korZVs5UFrAzGqQHIIlGA2VrtA4S28YPKWH7jt1BahGNsdsrew0HuA9WnYLC4REUvrIP0yTBeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81257" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
