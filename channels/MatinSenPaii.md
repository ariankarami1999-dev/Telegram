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
<img src="https://cdn1.telesco.pe/file/kimjLMwXKMNgKLWaWAKVl6-3a6n64DIJ9PLAu4JyqAAPiNUqB2--G7IkaS2TaLdWdmkBK9dY_EORMfR1H9qExYEcCePWQe7hqt6ool5j7n2dYtXHz9r3fwrOICczvqpg5dE7UictEBle9h5VVEwlqdhLXT6ICE5LDwZvC1sDilt51fg0CsNKacKzdPXJb3_09Sp9PERacvALucasyU7GULcMDnmmv_MghXpOfggJECSjmXk-PCrp67p4g-vlszFmVBeT66u2YYm1MDNgQKyabDnPgxOlFsAxwF_4sq1r1LLI4soYobEuFExuKwjk-V_D9dL02DVbO7gxIKpeNZBhkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 00:18:01</div>
<hr>

<div class="tg-post" id="msg-3712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/MatinSenPaii/3712" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/MatinSenPaii/3711" target="_blank">📅 00:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgMmfAz4Lbhi8SjoUsmvsjD9ugNXsWmIwryf1O1MFh2SLOtDpVkbrTEQbPfmHfDAoBKXhz3Sae9UGR4FZ7TAhYdmoByuccLgFxWYfmm4WXXCreYkTZ0AGYVwo8j52SDZjvy-rqPcwiRsz5kxtF5_-xeHlNvxWuq5QKSZ1r1mMhFR4tu9pgSV1UBPLpqy9_S4yJich9B5sh-fUbpx1Ebt8crXEOmJdfglaP9JWurdopz7d-GSjTM8oCjPNldgmtzVB9rhtiu_psin5S4u9oDwCoFCrQrnV9tdZoN1iX-hsHMVB7Utx2HAPMwGfFpslDyvibT3ZJym8brz0v96foFMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس WhiteDNS-Wizard برای کسایی طراحی شده که سرور و دامنه خریدن، و حالا نمی‌دونن که با اینا چیکار بکنن
👍
این نرم‌افزار مولتی‌کراس پلتفرم تحت CLI اوپن سورس، از شما اطلاعات سرور و دامنه میگیره، به علاوه API-TOKEN کلودفلر، و برای شما صفر تا صد کار نصب پنل، گرفتن سرتیفیکیت و ssl و ... رو انجام میده. و این خروجی‌ها رو میده:
1- کانفیگ VLESS WS شخصی
2- کانفیگ REALITY-XHTTP شخصی
3- کانفیگ Hysteria2 شخصی
4- کانفیگ Shadowsocks شخصی
5- کانفیگ Tor vless ws
6- کانفیگ Tor Hysteria2
7- کانفیگ Tor direct
8- به زودی مستر و ... هم اضافه میشه
آموزشش رو هم داریم با آپدیت بعدی
گیتهاب:
https://github.com/iampedii/WhiteDNS-Wizard
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/3710" target="_blank">📅 22:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3709">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZTe_hunFe5l1F_95qtE8bPvF54Nr_euxbNSXz9NRMF9MzkA2EnspIJ1z_Xo3XLaozNwK_S6yqpb4uJezq6VylolkYkCH9okrW_ILYLze_H57aAQJhYcGDEQrjsU2at39RDfji-DnQw_oWWSCcB0g4tcqtHsAIgk957x09zMesYW3AFtPZrPcMrFio6l6qcFSBZPWdn0HcDOMhaF6tcYnAY4veXxpOj9sr0vst1aXqYQAo_JbAdU2IVnPXpRmk9uoLMUWOsLMzK-Q0__WbKOlLAvdrE7QlS9thm3Q0pekgRiYHbzp3jnlblbv0aCrNaGMLs_LY0AqHcjdV0RFMd-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AzadiTunnel نسخه آیفون شیر و خورشید
👑
یک اپ iOS برای اتصال امن و پایدارتر، با تمرکز روی تجربه ساده، CDN Fronting، DNS هوشمند و تست اتصال.
📱
لینک مستقیم اپ استور:
https://apps.apple.com/ca/app/azaditunnel/id6776486891
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/3709" target="_blank">📅 20:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3708">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3708" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3707">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ElB2-DHGwlBW6iae7xJf1tRAuoL08F7xmOm5GJ2BK7Xk0xtjlVAphKi7c5kkmbB7y2YAuf_h7ppaqC8JsUJtuQZCnlvYvbyl28N23IAnhd71TpgTUcMLcoYSeVt7TeR-35-NWZ-reyA-kf-MgAQs8KzzmpwLXGUahnCBwjciN1dEu_s5mJUEMAKmS_RTCsZ9jmcZOS4o7-7fFpD3fTEUuzRafoEjUHbltgFGRKl80kCubpivOf-AxIZbn-i7dMj87MxBx4phhFJrP29QdQs19oFs47S8-dBbZmOrRUWxAjCynF6XtXy0ftQf_OivzA157RHXzTNQpJFmO6RpURVJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت OpenAI ویژگی Dreaming رو برای حافظه ChatGPT معرفی کرد!
بالاخره بعد از مدت‌ها انتظار، OpenAI ویژگی خیلی مهمی به اسم Dreaming رو برای ChatGPT معرفی کرد. این آپدیت حافظه رو از حالت «یادآوری ساده» به یه سیستم هوشمند و پویا تبدیل کرده.
قبلاً چی بود؟
قبلاً ChatGPT چند تا نکته رو یادش می‌موند، ولی بعد از مدتی قدیمی و بی‌ربط می‌شد. مثلاً اگه بهش گفته بودی رژیم غذایی خاصی داری یا پروژه‌ای داری، بعد از چند هفته دیگه درست به یادش نمی‌اومد.
حالا با Dreaming چی شده؟
با این قابلیت ChatGPT تو پس‌زمینه (حتی وقتی باهاش حرف نمی‌زنی) همه چت‌هات رو بررسی می‌کنه، خلاصه می‌کنه، الگوها رو پیدا می‌کنه و حافظه‌ش رو همیشه تازه و به‌روز نگه می‌داره. انگار داره «رویا می‌بینه» و اطلاعات رو مرتب و هوشمندانه سازماندهی می‌کنه.
فایده‌های واقعی‌ش چیه؟
شخصی‌سازی خیلی بهتر: ترجیحاتت، علایقت، محدودیت‌هات و جزئیات زندگی‌ت رو خیلی دقیق‌تر به خاطر می‌سپاره. مثلاً اگه قبلاً گفتی عاشق عکاسی طبیعت هستی، دیگه پیشنهادهای generic نمی‌ده؛ مستقیم بهت ایده‌های مرتبط با سبک مورد علاقه‌ت می‌ده.
پروژه‌های طولانی: اگه روی یه پروژه چند ماهه کار می‌کنی (مثل نوشتن کتاب، راه‌اندازی بیزینس یا یادگیری زبان)، لازم نیست هر بار از اول توضیح بدی. ChatGPT زمینه کامل رو حفظ می‌کنه.
آپدیت خودکار: مثلاً اگه گفتی قراره به سفر بری، بعد از سفر خودش متوجه می‌شه و اطلاعات قدیمی رو پاک یا آپدیت می‌کنه.
کنترل کامل داری: می‌تونی حافظه رو ببینی، ویرایش کنی، بگی چی رو فراموش کنه یا چی رو حتماً یادش بمونه.
در کل، ChatGPT دیگه مثل یه دوست معمولی عمل می‌کنه که فقط حرفاتو گوش می‌ده (حتی این هم با ما دوست معمولیه!) حالا مثل یه دستیار واقعاً باهوش شده که تو جزئیات زندگی و کارتو درگیره و همیشه به‌روزه.
این ویژگی از امروز برای کاربران Plus و Pro در آمریکا فعال شده و به زودی برای بقیه کشورها و حتی کاربران معمولی هم می‌رسه.
لینک کامل توضیحات OpenAI:
https://openai.com/index/chatgpt-memory-dreaming/
✍️
Diego JR</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3707" target="_blank">📅 15:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3706">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3706" target="_blank">📅 14:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3705">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DvHle1lyyRW9d6ORhDWAsWBOvKo_-TpysTKwGd6-q57_Qa4iQkjIIm2h72dtidLEF0EMiC-0_Iizm3Ct0U2BtrbLNL7aPcz5-71A3DF6Fqc9Z8btD-mnQMOjRQ9Tip_biy8E6aCle8MEBkdB6GeVqYGlJxPyPvgJ-AILCJh-Q6KByZnp8od9HBnoRYuJGwfqAsImchn1J7WRxjK48gUmHUA6tNj7LZGEPpdwFYX9Z3gmDdGdYrzBk2BbH18vEmsi683dnX749SnIqr2yF0uzYtNyIB6KQrfqW5-B8KYzdfQxgBUl8NS3HZRsCQOhT4Iy_PSDJwj1FJTgx_bCEASr3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اگر کانفیگ worker پینگ می‌ده اما درست وصل نمیشه تنظیمات مثل عکس قرار بدید fingerprint روی Firefox و Alpn روی http/1.1
یا اگر توی mahsang هستید Psiphon انتهای اتصال قرار بدید
✍️
🏴
Amin
🏴</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3705" target="_blank">📅 11:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3704">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3704" target="_blank">📅 06:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEJA8m9_ws_NkhWU1mSxi-_sFh3rqdHEJPbprHUaOltb4Won0wJceXqMEeimocP91NRT8g1PTTzHUBEWUi11W2Qdxlr5IEOGagYXfCOFGN_CIdGhbBlbJqO6p38SZlbVypEaGzRzGwK9JNMcp4JAWdQc04oQ1FpXoZZA9DTe903rf6Y36hZlgMAKD-gxedf79sJZZBOPmnUarvmjoQmUoA94M5zGomJQ4cqyjp0SzczkIbCbJFcfZlWlQBv1Dm_J6MpUbe5Em8reEtdzeQVPUsR04jMBWdIcxY24yGiE5aZUxLXoYErz1ymOijMW0M9hSTWB0KPryDGhVHEoi3n-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3703" target="_blank">📅 23:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3702">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lH6YkMiLHGgi5IiC4WaXGdU6MdM8rbtuupyUS0AXwMLsraEnT6UHSJYe01iMZPkPHrqPe6Lp0KhntJUSlhXX0ej4XWsRlGfFBZARHAta8xB_u6DPUVKvS8SPs20qyBaCoo1aYQ6hSbDiBG3LUpoihRzE-JD9PDp5hXvRiYcPtCgh13NMmy7FkiqXzdyhMH5eUWqoYF17VDEc8U5AcbaZNkMqsyMGpqU4fy7UrRnjbqcvdf50T1PRINMtdKFNsarMKmLMlfZ1Bd96hyQAa4mGj7syCvpcTMTAdT8Wn2wLiikVUgHiEndxRJO7aycaE6PxGEA7VhPM47XxlWWwMh4PUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت کلودفلر(روزانه تقریبا ۶ گیگ) روی اکانت کلودفلر شماست. نه خود Worker
پس اگر می‌خواید این محدودیت بشه 12 گیگ، یه اتمیک میل جدید می‌سازید، یه اکانت کلودفلر جدید می‌سازید، و یه بار دیگه مراحل ساخت رو پیش میرید روی اکانت جدید</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3702" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3701" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/3700" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این هم آموزش‌های مربوطه. از لینک ساب گیتهاب استفاده کنید</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3699" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 چرا نتونستید وصل بشید؟</h4>
<ul>
<li>✓ بلد نشدم وارد کنم</li>
<li>✓ لینک ساب رو زدم آپدیت نشد</li>
<li>✓ لینک ساب رو ژدم آپدیت هم شد، وصل نشد</li>
<li>✓ الکی دیسلایک زدم اصلا وارد نکردم</li>
</ul>
</div>
<div class="tg-text">تونستید به ساب جدید WhiteDNS وصل بشید؟</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3698" target="_blank">📅 20:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3696" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">به یاد محمد جواد حضوری.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💔
این کانفیگ رو به یاد محمدجواد حضوری عزیز که هم محلی من بود و دیگه پیش ما نیست میزارم تا یادش تا ابد در ذهن من و شما خواهد ماند...
به یادتیم پسر
💔
💔
💔
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3695" target="_blank">📅 13:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">😭
الان که همه‌چی فیلتر و بسته‌ست و فیلترنت داریم، یه مشکل کلاسیک ویندوز همه‌مونو کلافه کرده!</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3694" target="_blank">📅 12:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WrdjjwfAK04eA8p4Wyqps79aINX_pnum6ssg64Clse6DJd0ucOiH_Wsow6-7JINezppTzMQM40QGMsdK5lHNnCyLh-s18qt3qkVDBewcK3m3wtg9R02LpRUveJRSQhazhj7bvm0wdFj6d3gG7EsNS3pSaNfS5DY-F4dwLRWUWDrhScDZGyHO46edfZ7HuToi5cNVf1WOnqS51RcVamDZTdGwgEvPAzoXy8jvcnb11uQ8UyOqqdAqEG45gGU5hxLTjYRN2pSjF1NFZ9UAvaz-WX4tI4XFqtbQiLB1Xf9YBrR05DKnIcuLqmAfFLz665Dxbl6Dj4ajEaopOoWdbtfF5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چی باعث میشه یه سری دوستان ادب و نزاکت یادشون بره، ولی خب برای بقیه میگم. فکر کنم دو سه باری هم گفتم قبلا که برای مشکل سرعت آپلود متدهای پشت سی دی ان چه شخصی چه BPB و Edge:
1- فعالسازی Fragment (اون F بالای صفحه توی اپ MahsaNG با تنظیمات auto)
2- بردن کانفیگ پشت SNI-SPOOF</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3693" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=anTHOrMmYNcAdmRky9tWbAXhQjbdS5uH-rWWX5UU2-jc-QTT-YY88jHtFEIxdQKUeD5vsXhrqzeBaqeYu6g7sShi7U3Hy-3GnI5fNG5MetkHJFzvWcoIcAw1rwP4PEGllnnzzbQ3F1tDlIhMlxZ1vH41n0E7gWBPu-bMn39bmuiwHoAqhhMa4LkpCcpccVgij8Zephwr8JtDsOOS6SWmafZvahqUpFCwW5VccMP15KlukAXGewKd0Hq6jxKfcZZoUVd_sq1EtwxwOzNe08fJpM8_Gt7htxVDictq4yjaNNsCLAodDo-K9jPNbuMl0_k-iP0ZmtWb1MJBrqIf5q5LkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=anTHOrMmYNcAdmRky9tWbAXhQjbdS5uH-rWWX5UU2-jc-QTT-YY88jHtFEIxdQKUeD5vsXhrqzeBaqeYu6g7sShi7U3Hy-3GnI5fNG5MetkHJFzvWcoIcAw1rwP4PEGllnnzzbQ3F1tDlIhMlxZ1vH41n0E7gWBPu-bMn39bmuiwHoAqhhMa4LkpCcpccVgij8Zephwr8JtDsOOS6SWmafZvahqUpFCwW5VccMP15KlukAXGewKd0Hq6jxKfcZZoUVd_sq1EtwxwOzNe08fJpM8_Gt7htxVDictq4yjaNNsCLAodDo-K9jPNbuMl0_k-iP0ZmtWb1MJBrqIf5q5LkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمتر از یکساعت پیش مدل جدید تصویر ساز Reve 2.0 معرفی شد , این مدل با پیشی گرفتن از نانو بنانای دو، رتبه دوم رو در جدول مدل های تصویر ساز بعد از GPT بدست آورده
از سایت
Reve.com
‎ می‌تونید به صورت محدود و رایگان تستش کنید.
یادداشت تیم: «ما روشی نوین برای تولید و ویرایش هر نوع تصویر با استفاده از چیدمان‌های دقیق ابداع کرده‌ایم. برای نخستین بار، خلق تصاویری که گویی می‌توان آن‌ها را لمس کرد، امکان‌پذیر شده است.»
✍️
سگارو</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3692" target="_blank">📅 05:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واقعا متوجه نمیشدم چرا مردم پول vpn میدن</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3691" target="_blank">📅 05:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">توی 12 دقیقه، با گوشی یا کامپیوترت بدون هیچ دانش فنی‌ای برای خودت سرور VLESS اختصاصی بساز!
🔥
توی این ویدئو، بهتون یاد دادم که چطوری از طریق وبسایت کلودفلر، پروژه BPB و پروژه BPB-ReCoder محدودیت‌های قبلی کلودفلر رو به راحتی دور بزنین و برای خودتون سابسکریپشن…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3690" target="_blank">📅 05:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از کامپیوتر فقط دکمه خاموش روشن کردنش رو بلدی؟ نگران نباش! من بهتون یاد میدم که چطور با دانش فنی بسیار پایین، بتونید برای خودتون و خانوادتون، بدون یک ریال هزینه، VPN بسازید!
🔥
هم برای IOS، هم برای اندروید، و هم برای دسکتاپ و مک  ربع ساعت وقت بذارید این ویدئو…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3689" target="_blank">📅 05:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یکی از دوستان این روش رو رفته بود برای مشکل اسکنر و برطرف شده بود این اشکال واسش:
متین جان برای مشکل
https://t.me/MatinSenPaii/3652
از این کد استفاده کنن دوستان
pkg install wget -y && pkg install unzip -y && wget https://uploadkon.ir/uploads/c86602_26senpaiscanner.zip && unzip c86602_26senpaiscanner.zip && cp senpaiscanner /data/data/com.termux/files/usr/bin/ && chmod +x /data/data/com.termux/files/usr/bin/senpaiscanner
بعد از اتمام کار
کافیه برای اجرا
senpaiscanner
رو بنویسن و اینتر بزنن
(توی نسخه ۵ اسکنرت)</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3688" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3687" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3686" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nfghTEuPDLMpvYuVegSTXe3nW-RPbtTJnrF5FxrhDO-9jKqPJum2-e9dfvo0Q8ytUjoi4BrHh582D9ObXqiUMiwWfjeFfhrLPDVEbYwTL8rPfiwCe8UUyv36H7QiW879q2bl9jzwoSMSXFtpWUroHtzEu30pxVuxXsd9RahNhexCeRJv9w-dEPXLiHylndX7r0n-R479ijBhHehZeLUOqt__InkiLw7g53e6QANmRj8XSAQUlKY6DEPhffOdcgvaBSHTMmgkEqM9z9Ggja7jAYtLzFFg0tj5UK8asGTCtBcwpfGUPQBFu7M4nY55ydLwQXgIwURlMOate9BWoPnyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدده هیچوقت مهم نبوده و نیست. اما مناسبتیه که به خودم یادآوری کنم اهدافم رو. از 2021 که با یه گوشی و ذوق مسیرم رو عوض کردم و اومدم سراغ یوتوب، هدف والا و بلندمدت من، گذاشتن یه تأثیر مثبت روی جوونا و نوجوونای خوب وطنم بوده. کسایی که ارزشش رو دارن، عقاید و شخصیت درستی دارن، انسانیت سرمشق‌ـشونه و شرافتمندانه زندگی می‌کنن.
شاید یه جرقه‌ی امید توی این تاریکی.
شاید جلوگیری از خودکشی چندتا از برادرا و خواهرام.
شاید ایجاد شغل و ایده دادن و کمک بهشون.
توی این خراب شده، ما فقط همدیگه رو داریم.
ممنونم از تینا، پارتنر عزیزم. کسی بود که من رو از تاریکی بیرون کشید، و بهم امید زندگی داد.
پنج سال گذشت، و از مسیری که رفتم پشیمون نیستم.</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3685" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شما یه اپلیکیشن می‌بینید، یه لینک ساب می‌بینید، من ساعت‌ها و روزها زحمت و هزاران دلار هزینه از جیب شخصی بدون چشم‌داشت و تلاش شبانه‌روزی می‌بینم. هم از بچه‌های وایت‌دی‌ان‌اس، هم از بقیه‌ی دوستامون که برای اینترنت آزاد تلاش می‌کنن
✌️</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3684" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3683" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3682" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الان که بهش نگاه می‌کنم، از دی‌ماه تا الان نزدیک ده سال گذشت...</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3681" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K7BrUjlm1-4rfgESxeYE-gDyooqhtRsczXa8C1DSDs_A8Ig9an8oFycqpXA6CuupfZP0LAa-KZMjZUaxwl98B04kwY5WAOa4lGMewpU9hIj4zRGP_gnqApwhiz2svoQKpbnycbnsL20MlDrGBq1Zb_7V9qQCmOzRSJTslb-dvHjQ0ljev6V4TZcdpgpipvop0H7ca0vczBGdVGnAiuA3g6oY3nFBhj58dqHksBY_2cMW69Nlq58uZtKq00wwX2BmuHRLpS0NR-IfFLG-Br0gQnREO3LM8Dn3gHlFuN80F0FiK4W29NeaB1DfdaDZ6H6Xgl2AAK4cTWRhVFNXmM3m7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:
1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی هر نتی(تبدیل سرعت اینترنت داغون به سرعت خدا)
مزایا: سرعت بالا و راه‌اندازی یک باره(هم مستقیم هم تانل)
معایب: نیاز به سرور داره، روش مستقیمش فقط روی سیستم میتونه ران بشه یا گوشی Root شده و تانلش مصرف داده‌اش ۴-۵ برابره
ویدئوی اول آموزش Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w
ویدئوی دوم آموزش Paqet تانل:
https://youtu.be/nwpLOANv7VY
ویدئوی سوم آموزش Paqet با نصب آسان(اسکریپت سم):
https://youtu.be/QkGI8WoOtPc
2- متدهای بر پایه کلودفلر Workers، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی اکثر اینترنتا به علاوه‌ی آیپی تمیز
مزایا: سرعت بالا و راه‌اندازی یک باره، نامحدود بودن(هر اکانت روزانه 6 گیگابایت حدودا(هر شب ریست میشه) و می‌تونید اکانت‌های زیادی بسازید. من خودم نزدیک به ۱۰۰ تا ساختم)
معایب: فقط وب سوکت میشه ساخت و ممکنه برای گیم و... مناسب نباشه اما برای اینستاگرام و یوتوب و اینها خارق‌العادست.
سری اول کلودفلر، پنل BPB:
آموزش اول: ساخت فیلترشکن بر پایه پروژه BPB و اسکن آیپی تمیز با سیستم:
https://youtu.be/_aXy8wwyRG8
آموزش دوم: تنظیمات پنل BPB از سیر تا پیاز:
https://youtu.be/7G9Fjhe_NxM
سری دوم کلودفلر، آموزش پنل Edge:
آموزش اول، ساخت پنل Edge با سیستم به علاوه تمام تنظیماتش و ثابت کردن لوکیشن:
https://youtu.be/svYBcv4bSzo
آموزش دوم، ساخت پنل Edge فقط با یک گوشی موبایل و نصب ترموکس و اسکنر برای پیدا کردن آیپی تمیز:
https://youtu.be/2otJfXgNWCM
3- آموزش کامل خرید سرور و دامنه و نصب کاندوئیت بر روی سرور ویژه ایرانی‌های خارج از کشور که می‌خوان کمک کنن به اتصال از طریق سایفون:
https://youtu.be/DtZyWXWV4BA
4- متد SNI-SPOOFING که در صورتی که یه روزنه‌ی کوچیک باز بمونه، می‌تونید باهاش با نهایت سرعت حتی توی بدترین قطعی‌ها هم وصل بمونید.
مزایا: بدون محدودیت سرعت، می‌تونید کاملا رایگان وصل بشید(با کانفیگ‌های کلودفلر متد شماره 2)
معایب: نیاز به باز بودن اون روزنه داره، و فقط روی سیستم قابل اجراست مثل Paqet. اما قابل اشتراک‌گذاری به دیگر دستگاه‌هاست.
آموزش اول: راه‌اندازی SNI-SPOOFING و استفاده ازش روی ویندوز:
https://youtu.be/dujMBt4sCpw
آموزش دوم: رفع مشکلات و ترکیب لوکیشن متد هر کانفیگی از SNI-SPOOFING روی آمریکا:
https://youtu.be/PuYwXH4D4tU
5- متدهای بر پایه‌ی گوگل. این متدها مادامی که گوگل وصل باشن، کار می‌کنن و طیف وسیعی از متدها رو هم در بر می‌گیرن:
الف- متد MHR و زیرمجموعه‌هاش: این متد محدودیت ۲۰ هزار ریکوئست روزانه روی هر جیمیل داره و سرعت آنچنان بالایی نداره اما با تعداد ایمیل‌های بالا، میشه بهترش کرد.
آموزش اول، متد MHR خام(توصیه میشه بعدیا رو راه بندازید نه این. چون با آیپی خودتون باید برید و هوش مصنوعیا رو نمیاره واستون):
https://youtu.be/jzaqdKl40Ww
آموزش MHR-CFW(ترکیب همین، با کلودفلر برای داشتن آیپی خارج):
https://youtu.be/L3lJZrAqqUQ
آموزش راه‌اندازی MHRv-RUST با گوشی موبایل:
https://youtu.be/7YdJIJloIxY
ب- متد MITM برای دسترسی به سرویس‌های بسته شده‌ی گوگل(چون از روش یک حمله‌ی سایبری استفاده میشه روی تلگرام آپلود شده فقط):
آموزش اول دسترسی به سرویس‌های گوگل و گیتهاب:
https://t.me/MatinSenPaii/3151
آموزش دوم دانلود نامحدود از یوتوب با نت ملی بر پایه‌ی آموزش اول:
https://t.me/MatinSenPaii/3230
ج- متد Skirk بر پایه‌ی گوگل درایو که مزایاش، سرعت دانلود بالا و معایبش، Latency بالا هست؛ از کانال عزیزی:
https://youtu.be/vCr4E6Y1k4c
6- متدهای بر پایه‌ی DNS، که از روز اول جنگ وصل بودن تا آخر قطعی. اما ما اواخر قطعی بود که به بهترین ترکیبش رسیدیم. پروژه‌ی MasterDNS و کلاینت WhiteDNS. مزایا: وصل توی هر شرایطی، قابلیت اجرا روی هر پلتفرم و سیستم عاملی، حتی روی سرور، و اضطراری‌ترین راه چاره‌ی ما
معایب: مصرف حدود دو برابری اینترنت(که به نظر خودم می‌ارزه توی اون شرایط) به علت کوئری‌های DNS فراوان. همینطور نیاز به سرور داره اما از سرورهای رایگان هم می‌تونید استفاده کنید(طبیعتا سرعت خیلی پایینتر)
آموزش کامل راه‌اندازی روی گوشی و سیستم:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3680" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امروز واستون دسته بندی می‌کنم یه کم راهکارهایی که تا الان دادمو</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3679" target="_blank">📅 08:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LNuwt4OzSORCXLrcgp9rRwTyVRYW1Xueo6_bFTgl9iTz3_iFXAbmOeDL4CgGNA9uh4lxciVoi3DsiBmdfPU-zPAtewoyu_vT4gPoY_Soxgqz3UqhparWwmnJwqkywEyKyWYueGtVxf_xEpUdXlo8hbqyW559X5MmH7Zlp_lAXGJQbrwtpkTeui4sPLuIHhdPR6wxbsdc7hBw6pWhJcojAaeysGRt4XFI0gsdHcjkY7gLkI58uMo8S6VEaxM8-cj1Tz9R-63-faiuQoY4s6GA3XqkHPEoJ1YW25MUb5Q4Mree02fA3Nse-VIkVLYcBa_K8f3hWAoMJQMM8HCPdAGWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=BqwgAZZjgD8RCJ1caT00QFOXPQ527fxvQT8t-awGVLYbcTzieeHbX7bidFut9Fm0Rv5gNQr_VqIoOusV0Ir0EL791TxB46ziqCAZjsJbvI28FSxPmt7A2wMJ06RsupEF4jy2QIeXcaGKDpSKVFXL2l1GeSX3FHKg9B9NbUb4GjE346qgRUuYw2smUHAZjGIWoY36P34Co52pwsCBv_BXfZwWJjsHARsi2ya-tvzJC977r1OvnZvIW2kf-_nUF3VmfeUQQslnPXCtXkw7Duj_AnnXkoKoEUoj4IUQ0tcxFW9WkMJQg3jDSj0ZUKPbAoJgc7DzX4hEq_qL2b3E-BUJ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=BqwgAZZjgD8RCJ1caT00QFOXPQ527fxvQT8t-awGVLYbcTzieeHbX7bidFut9Fm0Rv5gNQr_VqIoOusV0Ir0EL791TxB46ziqCAZjsJbvI28FSxPmt7A2wMJ06RsupEF4jy2QIeXcaGKDpSKVFXL2l1GeSX3FHKg9B9NbUb4GjE346qgRUuYw2smUHAZjGIWoY36P34Co52pwsCBv_BXfZwWJjsHARsi2ya-tvzJC977r1OvnZvIW2kf-_nUF3VmfeUQQslnPXCtXkw7Duj_AnnXkoKoEUoj4IUQ0tcxFW9WkMJQg3jDSj0ZUKPbAoJgc7DzX4hEq_qL2b3E-BUJ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 22:22:04  The status of this service has changed to:
❌
DNS google.com via 8.8.8.8 : timeout</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3677" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هیچی.
موشک زده شد؛
اونا هم گفتن دفع کردیم.
ما مردم بدبخت هم چیزای عادی‌تر دیگه‌ای از سبد خریدمون حذف میشه فردا و پس‌فردا و روز بعدش</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3676" target="_blank">📅 03:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBvlsr-EOu7y3U39svHDXIAa2vcly8ew3a-HADIk4FqLvRq643NjcqiMx1HoTFxFVxNEBAg0w0U6b9_WZq8-uCGCkNLQyOHrg8_rKDkUxxjeIgv0pnBbeVIMPj0ulLBtcQW5dG7UYsu5nzyVqQh3XRk0-IRG7ml0w0SAuh8ChyA8-TxR1sBD2psWg1IzUIIy3XAkIFGGHQZDV88CeSYMcb09SGgn4QOmWJfP6lt_Y_zqIhsUV3X8QxOwiO0G7C5oB-qR6y1D6ZejTUqWLOqSjABVHiztOk21B4Dv1xdBX9qk2gzDeZUdCA5nFkyJKCOr9WnfjIw0XbJptexOSDxHwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBvlsr-EOu7y3U39svHDXIAa2vcly8ew3a-HADIk4FqLvRq643NjcqiMx1HoTFxFVxNEBAg0w0U6b9_WZq8-uCGCkNLQyOHrg8_rKDkUxxjeIgv0pnBbeVIMPj0ulLBtcQW5dG7UYsu5nzyVqQh3XRk0-IRG7ml0w0SAuh8ChyA8-TxR1sBD2psWg1IzUIIy3XAkIFGGHQZDV88CeSYMcb09SGgn4QOmWJfP6lt_Y_zqIhsUV3X8QxOwiO0G7C5oB-qR6y1D6ZejTUqWLOqSjABVHiztOk21B4Dv1xdBX9qk2gzDeZUdCA5nFkyJKCOr9WnfjIw0XbJptexOSDxHwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3675" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من الان خودم با WhiteDNS آنلاینم(داشتم تست میکردم دامین اینها نپریده باشه)
خواهش میکنم ستاپ کنید هر چه سریعتر. هرچی نیاز دارید توی ویدیو هست
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3674" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=s2ecwtF7DDybLbZPkFkBudP37iePeXsslKAMJoUMJ4GtbwvYehSZlc5IyvP_qgJFPlzoQFpAFx7dAI5O4HOMxCwZ2RrJIwy3E0gG-usD78fkb7rZ12ZblZnAFNZLds9Zjb6yDzd8LRCiq1_3DFsXG9E_EJEGZ6jJs3IWuPgvq_u7D-EITCg11jcLy5Q-nSJutxDaj_WKnNXiGD0eOLsG2PlcfIEq3UPy5PfZehyQiog0FVlEezpbvPNmT2P-I-abzdAfleiQXzfx5Xm9_J58wvwedzPkx_SCmPu9kXx13Yn3P-P74D_4SPyLAIYI9aGP5D8VAFfaI3zupZ2NTqJhRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=s2ecwtF7DDybLbZPkFkBudP37iePeXsslKAMJoUMJ4GtbwvYehSZlc5IyvP_qgJFPlzoQFpAFx7dAI5O4HOMxCwZ2RrJIwy3E0gG-usD78fkb7rZ12ZblZnAFNZLds9Zjb6yDzd8LRCiq1_3DFsXG9E_EJEGZ6jJs3IWuPgvq_u7D-EITCg11jcLy5Q-nSJutxDaj_WKnNXiGD0eOLsG2PlcfIEq3UPy5PfZehyQiog0FVlEezpbvPNmT2P-I-abzdAfleiQXzfx5Xm9_J58wvwedzPkx_SCmPu9kXx13Yn3P-P74D_4SPyLAIYI9aGP5D8VAFfaI3zupZ2NTqJhRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3673" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">به نظر که جنگه
چون بالستیک زدن
اگه آمریکا نگه اینا نقض آتش‌بس نیست</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3672" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">لطفا WhiteDNS رو ستاپ کنید هر چه سریعتر تا قطع نکردن:
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3671" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استفاده از فرگمنت هم جوابه</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3666" target="_blank">📅 00:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B2oOvhlPcPz_jDhYxIGrwsxUaiJ-Cp7qacj6SJ_Tz847IHzFVxNzeYl_5TlXhRzoNzrb5m9N9tm3itcay5F9SK5Y3LQaRqRw4sn5uVj55D_SAqTeqU_cW_XU_6623YgSxMBSDEgys95LEEcNnleJYxxl0-y0wVCX3CbQ6R9HuQMPSG5_gaGBfR7OlZ3Hsh4fKUzHhKKBh-SuwJ_f61KLlipN2sVWw4f43lYoZHrk8l_ZYFZV-TvKVlJW37iDHemqtWMMZeenWEHSd74PqIFTOZxMYv75ooLJPkvmZHIaDZ9YWQUNps3LvZOMKUUrPuqK-FbyCS1KiENH0B8pOW5A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مشکل آپلود روی کانفیگ مستقیم پشت CDN، تنها راه استفاده از اسپوفه. sni spoof</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3665" target="_blank">📅 00:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیدین گفتم
😂</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3664" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 22:22:04
The status of this service has changed to:
❌
DNS
google.com
via
8.8.8.8
: timeout</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3663" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3662">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 21:01:30  The status of this service has changed to:
✅
DNS google.com via 1.1.1.1 : 142.251.14.138</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3662" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 21:01:30
The status of this service has changed to:
✅
DNS
google.com
via
1.1.1.1
:
142.251.14.138</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3661" target="_blank">📅 21:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3oOfTKZqNPgT-wPGldGwdIMBOwL1tRVavgGwpOBmWQfm2VLlxpiBZde8Dds5cN7pBE9xFtMbkXOWxzCnpq5Zi6tAQ7UyxiXxngoq6O65JuDK24HptCNRG6bGR6aeeyBz1zWPn5TcV0JZSjsMJ_uMJivZeGNusGMDAJKaeBky7a5iPxpRaK290EdpHaivsTMpY1HMrRoxlxY-HpzlLdoZpevKV5s1W5W_6Z3FCOZIcEdWZI3mlszrZgi5LTYE1qOt4nceykewkQNGg0ZenNhRLkgAdeVnvsqM_9BjD3BSU0zqop5Cs5psaIiEtTKGPzbZGPdGN-GA96ftmxTU_RVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند یک سری دیتاسنترهای خاص یه سری تانل‌ها روشون جواب میده به راحتی. از جمله Paqet و بک‌هال و  reverse</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3660" target="_blank">📅 19:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bu8uEgAOPdEQkoXMo4B5ODv5QaJajZjhV2S3REC2eXO7wdTWK-Jvx1nc2FsqFiGFl-PVkGfdk23Uy0IIggWOf4ZWu-lME-FtEc2Yw-FwjcLEMntK5wqC_zB7udYSM6kMThqeH685rYjRKAj7M99KLjbKIkUNvrPGKtsS0f_EOUUyOU2fDWKed98kQ9wSPGePjMI53dIcVDr3lr_E3F2lKL2whaPPYEkyyewogz5VIkEqnpqoLKzRdJ4DqTksNGKbAg5UiWEvixnJfVTjxSyzpAlArXjuNB8faNHANd-J3hayDgbL0_h1-ez8K6bgFNHOK96vdneEw1H9sE28DwSTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت نامحدود تصویر با هوش مصنوعی Nano Banana 2 گوگل + طراحی رابط کاربری(UI) و ساخت ویدئو و موسیقی
⭐️
توی این ویدئو:
1- بهتون نشون میدم که خودم Thumbnailهام رو چطوری میسازم و چه شکلی می‌تونید به صورت نامحدود از Nano Banana 2 و Pro گوگل استفاده کنید
🎤
2- یه UI باحال با هوش مصنوعی به همراه پروتوتایپ طراحی می‌کنیم
❄️
3- و با همدیگه یه موزیک در مورد 90 روز قطعی اینترنت می‌سازیم
🎧
🤎
اسپانسر ویدئو:
کانال تلگرامی ذغال سیستم؛ فروش لپ تاپ و لوازم جانبی استوک وارداتی دبی:
https://t.me/ZoghalSystem
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/MatinSenPaii/3659" target="_blank">📅 17:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ببینید MHR و mhrv-rust و skirk و flow drive و تمامی متدهای بر پایه‌ی گوگل، با اولین بادی که از سمت سرزمین‌های دشمن بِوَزه قطع می‌شن
تنها چیزی که برای ما می‌مونه، DNS هست که همون هم ممکنه سرعتش خیلی خیلی کم باشه و می‌تونید از اینجا
https://youtu.be/6Pm7kNQb3mo
آموزشش رو ببینید.
متدهای بر پایه کلودفلر مثل BPB و Edge و... هم که یه پله بالاتر از MHR و اینها هستن و طبیعتا همیشه بعد از وصل شدن گوگل، وصل می‌شن.
هرچند به WhiteDns هم نمیشه ۱۰۰ اعتماد داشت که برامون بمونه چون توی هر سری فیلترینگ ما غافلگیر شدیم. مثلا ما به هیچ وجه فکر نمی‌کردیم بتونن جلوی Paqet رو بگیرن اما تونستن. هرچند امثال پترنیها هم با SNI Spoof، اونا رو غافلگیر کردن!
برای همین شما ترجیحا متد مستر دی ان اس رو توی Whitedns به عنوان اضطراری‌ترین راه، داشته باشید علی‌الحساب</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3657" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3656" target="_blank">📅 11:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3655" target="_blank">📅 11:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKNTtZJA7-UvARRiyOoLqDP7ctRuD_FMDN6iaNjrodLIcVyG6-qGY--UwOF1qNfedmtJSS6xGrM4jS_CaSxVw1izN5SOBECFGuKFdXpT_ZR3WP2DEdsBfrvkyy3QFuDiWt582qlfNsP0CA4zF6pK3-6NqerlA8AiWXw7zN6hcSUS4KRvwYlknAiXBRzmhh0H6x7t0ILLrUdQlN9CumbKjya4or6pr_ZqhkCYtP4YzT5ds2y_fZoVLML98qnphJIUyvHck3yKAoq9jD-oAJUg3kwsBkYVRz4VJS9bvyswfVRhSrrXTc6SKoN4zHr7DKEssnyRibjVpDx5U2pDlYgwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iWOEjHwOLsx2tTriDcwyql-0pghlTzmHLVdq0FAZ4rL7UWSb6ax79hIkvnobTlSiWAlAzaLidECEhQs-kN65mxXHb-1MgzmYm9IVQwgi7rR_LCeEZkwIpbiceYW6GkT4VMk78DwT9t6HQkAhtT-mdRlKYDAOc5dS356yLF5ppm6Pmi8Ov_PULFI3EtWFS9Gmix-5p3JV82eCAnvKY9oSxi3EacWm7uNN0yh7DB8eWbkHHDi8b5DB5zoBj4CJm50TiVHv3-pdn2aLsImmIX0EyDlJ7nV2n4mnz-jqStOmR7j0-dlrhFz87UbGU1_HQD7mSCJK-2cj1qQGRwl7h2mgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uviaLZbKp3zTE-UwYVogxEHKJuF2PAqvmcq-l3Tg7RpYyFtCJhoOm5YnivoeIQNLoU4TJYGiJQry94IQHKlE4r7AXMXiBwR6qL1a4-0g-lOZAnnl3EZwwSFX8j1AhCavXTT7BKtpYZ1iAmoLttkN_E8j7Fp_H8u9HhJaKaewxn1P3u3Nt_IufAw9oUaNFjj6vv_BkrR10BrtqMjv1IpKUKJsjwBO-jnXHkNVhBYZn1TPwoHORD6vX6zTN65FppRQSz2ODQdHc-OhNUlfjqQPmAFKFF36HZ5NMZm94rKRShvfWgV9FoYRPgRcGwfolPPCJZEXS55x-9cOPMXaIQ7ilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t87UuBS_85SkhPUQjuh4GEX7UrjC-uoCo5YGecewbTIN1z8yrRdS0p6v36VtQTMayVlgfYIjVgQhpJ0kMbGHyfOY65bz1aP751H8748K0iAdNbvXnEQXmyesGNjKptMqBFi63bmYHqC7GqJp7U3qEEaVH_cbJaiHAtJjgug6dQh68Krw9EKkb4joJF_tbCZ93FgTlFK7nmsalAtejO0DbFrEgT8g2gbQgATulRoOtjtbMHzX0o2lP4x64g5gmNnodP0_1WqrUvuQOiepDoBMOEduwh6aDisowrlpqomss6pNueId1Ww8tZ7eaAPK4eHxbUgnopUIPysGan22s0C1NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 33 تایی از کانفیگ‌های Spoof که همه‌شون کار می‌کنن و خودم تستشون کردم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux
دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  Edge برای ساخت کانفیگ رایگان:
https://github.com/cmliu/edgetunnel
فایل دستورات ترموکس:
https://t.me/MatinSenPaii/3643
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
نرم‌افزار RSTA Spoof هم اینجا:
https://t.me/rstasnispoof/2/1076
و
https://t.me/MatinSenPaii/3644
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت کانفیگ Edge(روزانه 6 گیگ رایگان با کلودفلر)
2- نصب و استفاده از Termux برای نصب اسکنر من و پیدا کردن آیپی تمیز
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Edge
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- استفاده از آیپی‌های تمیز توی Json  اسپوف و اتصال پرسرعت به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(با کیفیت بالاتر)
💰
دونیت</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TUOeSretnL5XQj1Ij_khSOZxEi9Jk8h2I_3MO5pYf88_acQZs1ZsV_fsK3eKc2y_yn4PEIBnouoKy6JgdtEU0CO_Pj8NNI_WE5StZPwhn7murLnmzPrAmNPjOKhZ-_Jh9hbr3uepCCKLCWyHIUliprh0o4bsRtFWAtnYwqDVL4gS1qKiQOE0Mz3GgRtQoYi5mv7RmP_DaGDDUzkX5WzYwOdgMHm5o58SHz8UaYjC8tC6mnWejo8-iVfNJXoyOl7tROsfukYqqKaiY_79oYr5ZORH1YO-dLjvRzpTV0e2167I8ukdpVrH-RQVl--L2o2qU6kA-Y_sHbQMx3Tzzm5KYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tCp_RLqHMXsrtFdsqzDM8twXE_1F2gP0NJUmcaZRPMYzgIqSpVi83ljZ1TTgMZm8rqzuGFIo-3hbarvIZVFGOji2GpJrjD5EJo9BLVNjqwocjsHjmQI6dZ_gyzir3E1jMOBwUEE1_xVlUV14Qq5Y_qi34SiAZYh72zJk72TgdRp0Fz3uyf44OSn0tnbKrxS3-JOrvC9yJ1zTY87hoE0Npzq3xu0O2ht5-Cfqeyc3IlFAVvUG8BSiXXZ30S_fY1VZNXQasfw7ubsolI1d4ReB_GoUlYzBvOSEATc64NAHgOpql9kExi_zBdxrdrvtdY81gy1E6l3CJ_TsSuyg9G-mNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rJcODnpO8ToRySHg9x1gpQShLQHrMC6reJ8dwqp_Do7XtocHdbLM5jy1HRaBmC2LooWL-MZ6QEsRVFfXlEwVrZAR9FTUSZmwXZcYDz-GUCwN7E4Tos8qQomO4S_wmNE7M9mr52wCrISzxIywxjn3tSIQXI102J7X3EPBX7oH340ybj9qyxmT9yM-CawFY3xhR2_aCPY-xWDVssWBPCEbbZ83U2efSiyS8d3-p4Ojt9n3D0bsM2V99DnGTewcPDbG_hJ24HeYs_HuzPN8QyEJ3TjZMX4QW2n7vKX9SXK7UX3h5gXvG_eU4FJwxq-Hy8Cs1qwcAjwb5TKYtx0_ca22Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=rNyyz2Dih1iO7OXSPzxeJnnvzg7nlzxDStFJsEV0aJUSFAqOhnn_t3j0_3sjPVnIOscAB4Wwt2REX8SsHFBDVW6GI8mKP8FjUm6ohtjiOyEK1fyFPohpbIMTbf5b46CHKk_zBEwDAimFmCoU3E6S-O7VQI-AbDar-t6dnOwFvB9U8UJ1I_ki4ApTh7OZie5etYaQcUXj28NS0qMTwHaFZjg4rt7ETGbBL-rNpVaw8oJzfUBow0XRdeYSftTp-4d3aUVbE1S5y24uH-MbN8qAVZOzVj64BZeiUENT6Kff8oGRaV-gQXZN-PV3LDtO4SHNjiQZf-3pfIbfPSe4HIwZ0Q1KaGuB9dZDHavnEmEdNMdmBUXZF5UigLcWTNfMeq1BSDI-aCw1XPy6q_zylItA1bZNNQCJvL13w24tUmGuT5RbzyYzaze-HmSwvPhlOuu6p2R_Fd8tb8muL08uZarvYWS2HAftz6JefUHoLFbd5l5kIAuwqzj8RJtVGSCTuKbSp0ayo_Y1-MCSC2IxxmlR-YrxLSbu97WS0XFswtY63Yva6IPLiYjGb4ykBG8hTKjAJesM7hUrDTNqEVa_2v4SenEO8CXzEoxK2HnVygTbnWRQBjOp6nqdX6raqoIMiYtSGi9nOqPJTbNJ02GIOTFz8PEyfwCpbfnRa6xuDx7RnEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=rNyyz2Dih1iO7OXSPzxeJnnvzg7nlzxDStFJsEV0aJUSFAqOhnn_t3j0_3sjPVnIOscAB4Wwt2REX8SsHFBDVW6GI8mKP8FjUm6ohtjiOyEK1fyFPohpbIMTbf5b46CHKk_zBEwDAimFmCoU3E6S-O7VQI-AbDar-t6dnOwFvB9U8UJ1I_ki4ApTh7OZie5etYaQcUXj28NS0qMTwHaFZjg4rt7ETGbBL-rNpVaw8oJzfUBow0XRdeYSftTp-4d3aUVbE1S5y24uH-MbN8qAVZOzVj64BZeiUENT6Kff8oGRaV-gQXZN-PV3LDtO4SHNjiQZf-3pfIbfPSe4HIwZ0Q1KaGuB9dZDHavnEmEdNMdmBUXZF5UigLcWTNfMeq1BSDI-aCw1XPy6q_zylItA1bZNNQCJvL13w24tUmGuT5RbzyYzaze-HmSwvPhlOuu6p2R_Fd8tb8muL08uZarvYWS2HAftz6JefUHoLFbd5l5kIAuwqzj8RJtVGSCTuKbSp0ayo_Y1-MCSC2IxxmlR-YrxLSbu97WS0XFswtY63Yva6IPLiYjGb4ykBG8hTKjAJesM7hUrDTNqEVa_2v4SenEO8CXzEoxK2HnVygTbnWRQBjOp6nqdX6raqoIMiYtSGi9nOqPJTbNJ02GIOTFz8PEyfwCpbfnRa6xuDx7RnEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgB8WyAfhqSuEcVQ8SycRyezwOI60orzs33txcNA-t1g5P8ZC7QanPM2-jpOvVQZCGnDMWtMDbfvIk_5TOjyvHNKMSfiPL7Fjv4CyuwSlWuVlhjMbs8rTkEsSXmVbXO6lzCZBJRjDAQHhPtZXeMuQJNfhtwCOL35WnVvNnHDShxWABgdS2fF-554Q5U-cKq83ZoAz-J20hsYMjXPXydojU94c5mwoA3JtMSz1pLY6fBPiK3QnH2hAi1gGu7AYD7bD4UyJa6srQqNEGWGn5QX5YOWCI0nS1BZPDWZiF2ACbholwX00rAzMOEOhLw4T6zkK12tUVFyv0qYsG5y2sHtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlOGrqdsXssaGf_m_zbvFRQD_BW18qdLlxp12DRmEE4hEqp4EIO3i6vEiWD3wpXMY-o2DR6G15D1_91B69Gqd5oIJBTnmJjPjqaOSqnWIFwKNMJwJw16aQ14aPMCSnAx3iKmjf--vx8Y1OfYVz1sqDVrQFm04A9vslxQiBvNLDVvQnt_w88KaMlcHT6XkvT5aq5Hp9cztitXNVjQAB-RthmUpacuCnK-VKtZIF3ozo5OFjSfgB75k9-DxQWXdLSLmdR8aSV3Dev304NbeeNbJSJ0IxzfZYuKr9QRLZHn0Q-m8p8o4IS9xAIjDxxnnA8-Etu7JtalxhMA7RPl1iXRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
https://sub.whitedns.one/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلود FLClan برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AY3H705HyVy8Z7SNCbKDcX6yD5wU0gzncFdPuq29wsrZMk0XO9BskadzWMkDcO05Wh4yqEacL5HHMv2dKPapZ3EBh_8zuHf9ZiGEDoHyeHBcnYMe7R6VONcxFjP2ii4chb5oi_eaKZv4jz4Rz_YuCemJ3qz_NjpGKSo_R57eBFui8pWIKYCnvs-Yr17sxhjt9PMK7arH0FNltkR1omrqyh3_muYBkRHp89hfsE0k6Ww3nBeDuetKpjxkhqr3XJrDIYkGr9X5fDf9z4UknQ5C9egUDCR66dTqkQIKYXkj4pbaElUKuf7fjkqwu1hAmW66dXdUb9h-fVRIWe2gcBy38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fbVtnoVO4Vk0VPovp4VfOrf-e7iMsLyU3Xv5T2aGIoFEpzB7S-u6bCc9z8v2sm6CtMBJJmqrZ_EJGBkBbloJvswdvTvEEauj6psPAdUChyCS6Lu4W4s5mB6MzZLHnGTd8KqWOh1PPD7F830WJSwzYkaDZ-srT3jBaVFIFmbOx2h2E2_0R8IaGc1Np1olGiWMf1i1ha_XeW3_SA9m9GCCw9-IKEQwJscd75Qn-Fr4U14TXOiGKa398mDFFxh3NX9IHV6xQBEr-_X-gfXk2lLB1-ZNucCcMDQmaQdsFYh5dcpyCdEzmReU0-uFzp8yoqJrpmKZwlNYvhftYrquEBmMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KZcZaMQg6paPdO8y61arc49mPyPY5GH2wDWq5BE5ZlHreyHW5i54rgFv5MumRbyZl8gtGig5ie6G2U_MURLKi_BHx7jM6CqHbfGbx5P-xzkszC3DhWs7y1BV1cBHXg62vXWnyJ0VzakkIb7FCKyyW7wyJEYFaigS3byS3l_RlgfcTmQ9sO_pJX5OEmhKf4-DSuDCAKQODXwITdI9UQX_Pjpf4jkQ66Xxqa1YQQO8g0ElWL9Sef8vo21ORW7GOstimabBJ1-gqns_Lkb5Rw3DkeWiDupqENXYNIqgPrNOUpzim6Vtm9Au69U3fu41WFRS0YkpQ2BvboBD7rEwI1gUAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H3AzYQYXjyQL20_PD-zwyupWIG72Gtr1Zh_9XiOXBRCnIZpszB95kXjhmrrU6XPuZk-V7Guww1u_IBdRVqd2Pkj_t_HaW7H3Ev7QPaIwaH8XLm-RtcEgGqterdXZoocPwJQyg7lAocds3rJMujphKYcYuYXiHxMyXOHeDFoKK_7ZthV_wAndyqkHmx-EW1kEvkEC7HFkGc1p0HMCHLlfXPcchSRln4DXBdJY-xpnF3mn7yURtVsPg8iXNieexCfrawZQK5W1hcMmQTiP3_mUYxOoPfAvaCuSVt-t8mZ32v9A8sXrLnijMbNX3ox18VrBbKAoKVLMsSb1ep93egPlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGjS7F7GRcg5Gj04My3-dpauRjOgYwgyB8tIVz8DnF0NWH9OV45LrteNGOxZF4jx78QVd_3XcLz5deV-02otoWsv-62rn1nJ0DOjIN6ChLO5He9khKZNADapaBFHa_VCLhla79zVclL2fxcWVk7eu9nu1IsjvPc7EFDkahHuLdbs1sntaiWrvi2Ih8JdVkfA7jff2ct0KkcUTjtwooxv7Ue_-9GG_6P-NJbcE4abiIeO3ZxxLJ1_rWrwz6ixuTHj1SqFNPd0Z--hBheRZ1Kemy0UL-uf34MxTJAjHXgFx26GNL--3yBxMX7TxuN8QUKgGN_A6KBOynEg2QvGbnRK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eraJ0ZqNIOyTsjayCUfhtSmoueR8VnNRCyBdqZ2oa6bwjN8ewEnTvbfwvrFSEEL9zptYZ7i3tf3abkEOmSuyrX4i8iFUFRXz7Pk01b_0UpeRDsfG4v3huaAZhkIMI94N3cb4OxaDdHuBmiz78t21dGRFW901Z2mx05IVKD_Kn0pTGkIQt5D1atrdX1-Gmctq2mzKM8wP1VnfBEjdUuNYNAa1z609kfX0vkN_FWm86GP8qM-lQUihyc51FtwloJ0Piz86zkENcn_ajXlyH5IddYpNTKHXsx8N006otJRRJQk7jkT2sBGemTj7YnGa5-NoJXBZVpU43ahJA84Ri3gVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMSpkWx8B3YAwKi2J8cK7y14p6Gkx_uare6-7RUUIu8q3vFtWguF0DdgnapKjDx8YhAhzpNZ8UiIt1WZzhVBHq8HmihM2aHAbfIIU05ol8LzEIeOCHtEvevm8uwrSwHs8WlKitFoy_ZptnpnRf0oSOZn3W590ws3H-4xhBHF4SEZAqJD6dBW9GuJakPPxu9ixkLp6SKdlJZxObGFZ2XpKmuXanHjoreUOMnT7S1OrCuFE9DZ2MS4Lsgl4O6VgGi2fkx4uIRFwz_Jc0R9MOwsw5ssOjyO3-aD5buHNNcPJ2BSYUadb-VoAyLNbCRtVajshJNNN-ggMhAhWAahTntliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAtL23voeGRHluwaRFN6iKS4GSttvHij-TB4FYdmyPlZ25uKW7nuL3CV9AD8Zl_ucY0hJPrZge6LEm5hMDtPZZ2jvb2Q_1g4dVAUH_vl_Dm0cr4hmpMy2llxYPvwuaYZk2J_KJyxAANe6d4Jc4IfhkV1m81F0p7O9VX6hx32hUwuM1glje1cLh9rvZboZZiloFT64VrC4vSEojTLBalsY3KVBt21KvwMhWqvkbC8c3erjyPk26ehHuUNf_d-ieIhdiLxxjjUTNqE4_5jHzBIY7BjFkK51FT_NcUcT_j-MntQCDGhMHxl40hjs-HbKW8rIMvaYSVXE4XW-fwzJaokLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShadowShare
منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...
وبسایت
https://shadowsharing.com
اندروید
https://play.google.com/store/apps/details?id=com.v2cross.shadowshare
ایفون
https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده
(توجه داشته باشید کلاینت یا فیلترشکن نیست)
🌐
@ShadowProxy66</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-5nCNTHjJcG1se5u-SlLarkxaeKwtWwFI7hD76yVil3-vDDetDMDl9hPBrZxovUD0h8DwK4H-WBWhi99Yz9uKBz7ge9vewVCVClpUTUhTVt-u7JI_RVKWZaAlXFIteKOteSKriY7qm1EcfxsBBLOgeKV3U4Pzm7OonXSLkCsu7JufFsUrLLnKR65jihdW8lzhdSQotxfe5oPY8c7pwAxNDxakua1VG7bNclao-4B5He1ErwLS4k3NIC0EqcXV_erFjRpLQW01hi2C_GI8eUXtLFSzoIEppW1_6GfHjZlPIrC0eZtJJFwts85H39fQ1HSjd0brrfy8GRAFLTqEVAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImAmKo6hnZFgeO6kwBJzSZ9MPadBE5VsSAHkEQx2HUf7Lc24OPAKBlMj3ID5ngJ0BlbvMSHfmMcybixk4VulrmI_7UksCZOna5aJ08Q27UIxYz3b6Ugv3OqyRXqGa7xU7w6CEu4K5AstXXo__JjA9c6qZeHplIY2BQAvANA0oBTkmodotAclY_oBWlH0cS8Vy2kzSKWSb9ulW67vshP0xt8N1o3Mkjl4SXumfFnCEGr-t6saRXsvgzepchTskXsH7YeUti0Pw1zB7L-YIhk2fVZI_KDofHxsEgMn-iyeySrXglyepD8SC38dmFab7Rgkk4ZHaTwY3vUMTU1BmNtoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1HKa9VFZH8UDYIeWwlwieNVbG0n4n35zdtOMoSmF9BeREFvumM50ShilfwtRMXPMfrWI35yFRaavjYUUCc_uB5aIVFd_sN-EGSVynEyFKDiuwHD8RPHr0DhmDORtu67svKiLBrlhnXMlYo5s61KI06_QDxzc5b6lZ6vp6A2poIJZa-KqEQSJ2qLm_S1IMXLce_LppF_wygv8RK4E2ARwXpIUh7hNfqr7RyZVdjuW0fvNiL47a5a00TIU7RypBTEkvY65kmcw1tQPpt-We2PK36D6WXGwgmg5dceUuTO5c6UYHoOM24IKJVcst30XnDKYTBicyW_pZdoNM4MYGXNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GTR5lnQnUUlV9Y5LMZljp3AkW7JQvcHczvhmbazaGAavMxsEWjRz8RZJjCHJ2VjeSLSGN9L3LJXgTlxklMiocfG5WfuHmLGWdiottGWAhXqcSLI6C5bXT-O4ClUlPLcG3ZW7qUwck-1ByFsm596mN_7r6q5_2BJIu4o55Y8qzK7W57R3i1F54WUiE3wcTd8C5bqkZuEt5Ux-TyJ9moxshgJofO5k_K0oF3CJjYH-B2UnIuY9GP0I5GM6gWivM_V4-UbUY1t1kPMxmDXA8asdYSNiw-7QwkKv10oLnbMBs0GjSWQdf8C3W61RRhuH0adpVbEyqwNwIourUzcJnPMzNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qRcAcuIE_6D3ivhBcSnIS98gwx7ibGEg846zWqdBJm4l0VmWNK1I7pYOr57SM4mRB7yd1p2LrFq51ARx5gnD5t7pUhV-iFcXFN5zpiMSgwbzfKkURNCv-qDwXZeAr6Rhg8Wo98pk3LLtRnVNPdkTfSacYGdyKhTQjvszDZuHoUowsYcKjKkBqCGNKzDxwhl6gT7-gVNwViNMOjzm2lGDrfI4Qg201C43sQaJS41YOHd4z00MOjFK9uwYPAdfciJBTv461vL5Pe6F1CWAmA9TgIMEdXXgIdUq-SC0OTT0mzMkPdbrra72NsbTOXAdnPL0FBwmfv0D1a3INs0uPgp3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T1ReyQ2Q83cej04-dAhUEc0YH8CnORI-4W8ClDri40krHNh5lpsZ33YobPdKQJBU-yeLJmrAEis_-L_Oaczw-i6w5U5izR4yAJnIutSBSOBUh-OHmqk9Qh9ZhXZTYjpyaByQBIyeoxZrnDfdnOzA8VsJuzWhujOkiBg9w3ojAX12B1ar6dmzgbPxeswZ-5DW0kFnvjs4IDuHvqNdSMtBvGYHIcmiwrcBjxTy8SiD4LEwL9RY5yPBCqFmoEfMr6OscYYI31HQW1TVmmzZvNmcS-G-n4uwVKfOLNijvag2uOCCeAhhkJ9qZa59o0EX9avEXpU5BnI30uGOh7dmuCdDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 0.5.0 اسکنر
راهنمای نسخه ها</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfY5lIS0lZeOaouHYqV_PHnnnSuA89Xo55xrrQOYFVu4px10zpxoAfJa4ItMWwPJQPZQCBYzhXvA148OT4mP65GjDXKL6S2YPo0cO1_R3SU7gnD0uhYaC_xWeLT7v_4KplvoxATnac1L26A3B4KdRhqkkaRS2FBMSPMT-oSLkyG6wB_773TITnC42_Dh8cLkL5lNhOglN2mWCO6bp-jGXT0ZkLaTolWaG2vS9hZgTZbSpOSrib4AG9489yYIjgFnIjeQYvcmreGxQb9ugM13wqlBBiz9RZKqMMF6VEOsbP_s40-qMSzoBIdlq1BtZYKwYaWOYxxiCh9wfZSVYe-TBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
