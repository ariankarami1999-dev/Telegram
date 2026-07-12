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
<img src="https://cdn4.telesco.pe/file/KvRRoHMgctw-ifpnNZYr_KLKb5rpm2pTmX66vDC0J0qK6iRlWdtDeLzwgBjF7fiNfyheALMoGH4YtyQXF0INRppfl3cAeXBiPIXTy-FeZuT4Akf4XCwi2YUJQF-pQtCzVxZNGVR9T_dWhwSSvP8CB786wbwM7mBBucSE5XA6MFBke3Ekr66wq03nsshsVhLnipybK9hnp8hncrGUxx7734BkrK2rUS8O9206PDLlkPdVmSiO6YkdPfgJAB556-yHtqmrDGbPJJ6tZMUPAH47ExE8hTTxCEYjqd9PllPaJibXTf4L_AoxyTBhuMgo0d52vZCspEL0wxbEeGucv1_0cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 373K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">متیو ویتاکر، سفیر آمریکا در ناتو: معتقدم در صورت برآورده شدن شرایط قانونی، توافق جنگنده‌های اف-۳۵ با ترکیه نهایی خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/17651" target="_blank">📅 21:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/17650" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگه بیرون میرین پاور بانک امشب فول شارژ همراهتون باشه
😁
کلا کاراتونو انجام بدید</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/17649" target="_blank">📅 20:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه های داخلی : گزارشات از اصابت دو پرتابه به جزیره بوموسی
@withyashar</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/17648" target="_blank">📅 20:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو همکنون در حال حاضر در یک جلسه امنیتی با مقامات ارشد دستگاه‌های امنیتی است.
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/17647" target="_blank">📅 20:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2uwo_K8Q2_GpmEeE-CDRymeYpRJxasZg6iKP1OxjWyqY49qSY2ljWrfQBmy3eSWwJnGO_BksqAA_2k-I4M3KctHu5usgB-EJbCgxwAmu2tzORJ7xWSVOJwiegE5cpE4YryTXrIcEWEgXN7IY_EKrgWSOdBGzTGheHtexXKAnktZK44KvqHMUEgEgoGlfthL_Db2E9HEVVV1jhi7ZQsO3vgzy3mPe-BH0M1ZE1O3PK_k6HZcL6HLG5qNrj0XAttfXwWmZqIa1tpzYDthsIXNk6QVBu2wO2XJIG7fUbscmq-pvHCUPh2uWlprsDHKXtAWmKChZ_u_Ow6K-znqixGAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ دستور داد تمام پرچم‌های ایالات متحده در ایالات متحده به مدت شش روز آینده به نشانه احترام به لیندزی گراهام به صورت نیمه برافراشته اهتزاز کنند:
به افتخار زندگی و دستاوردهای قابل توجه سناتور لیندزی گراهام، دوست عزیز من، و مردی واقعاً بزرگ که برای کشورمان و ایالت محبوبش کارولینای جنوبی دستاوردهای زیادی کسب کرد، دستور می‌دهم تمام پرچم‌های آمریکایی در سراسر ایالات متحده تا عصر جمعه ساعت ۶ بعد از ظهر پایین آورده شوند. خدای متعال تو را برکت دهد لیندزی.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/17646" target="_blank">📅 20:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مسئول آمریکایی : حملات آمریکایی که حدود یک ساعت پیش علیه ایران انجام شد، با هدف تضعیف توانایی تهران در حمله به کشتی‌های تجاری صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/17645" target="_blank">📅 20:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/17644" target="_blank">📅 20:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل مزاکره با ایران را بررسی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/17643" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ولی خوب مشخصه دیگه امشب میترکونن
🫱🏼‍🫲🏽
😂</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/17642" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وقتی چیزی ننوشتم یعنی ترامپ چیزی‌ نگفته فیکه ! برو همونا رو دنبال کن  دایرکت منو سوراخ نکن  اه</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/17641" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اف بی آی به کمک پلیس محلی در پرونده مرگ لینزی گراهام ملحق شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/17640" target="_blank">📅 20:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اعزام سه اسکادران جنگنده از انگلستان به منطقه خاورمیانه
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17639" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا یک ساعت پیش به سامانه‌ های موشکی، پدافند هوایی و قایق‌های کوچک سپاه پاسداران در دو موقعیت در حوالی تنگه هرمز حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/17638" target="_blank">📅 20:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منبع آمریکایی: حادثه امنیتی بسیار جدی در پایگاه آمریکایی در کویت پس از حمله ایران
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/17637" target="_blank">📅 20:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjJCW1-jI2iUafHqCe0IGZHFmOmgzPqNfmMwykASasDGoszwKq8gDnFjluQAhzrgv7gkEH0Nfg14L5-A6k4ZDHvaIvq8DKp58HzGyO2DGNmTE14aA1p-W6AtAyn3VVbpqbfvhWxh4EWfSFNYnSvvAegDvYjexvojVkh2EwmCVud4FDI9KJ-01Qem2c49lJ9Wj1mYQQL1JDEzgRmbIdKmuyd0WHhCxA_tZqLRbsQoP0EqQ78ErUdUbb_1KiYly_wL1YuRwQXylJof6I0TCTeVBZwhpbmhbOmlPqaAQNDM2LX1S-crXKNGV6kMimqt87ij2Cne7wA3b-dM4qiAM78fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس‌ها نشان می‌دهند که سناتور لیندزی گراهام در حالی که از محل سکونت خود بیرون برده می‌شد، که پرسنل اورژانس به او کمک‌های اولیه می رساندند.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/17636" target="_blank">📅 20:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/17635" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGIe1W2rruVr4HTPb8odgEsDg6f9Vumo3jPVZyo7tFmHMmAzET92Nt1LUEno7rEWTz7jVu4snTLpM93X1YQ-KB3cNaipwqRA0kB8EO3F3J55KqanSzqVjRzwcgDZBrTqF4FSj4Pl9EgdW5xBqXQnw90kFSmKgxaLBG8xLeshDPRmmeNFAS6ExyWTA4XvyhCt1UBWXizQPD0wiauJ__--xAQwPIEoWRvfRg3yzBZcIzjyXEKLkg8r-fKnvYk-e4HFhyavq93mXkZ1LfuQVOmpo43Xe07Iouc2aqvp1tlrvKSi0JqvhlSMHxnDlL5lpAY_Z-n69kN5fa4lCQnWRbipUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون قشم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17633" target="_blank">📅 19:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmczWbiiFOTj2uqfclHWXaJr7gzNREGn-cwkeRX8N2YSqrwDSkaBCGzuaXa5wiWG_YKGt9IPXMgzp5zh64IfKh2G2dLtyMuvENQt0AW_yCfV6JdHalwnB5LtLZ8aLtvszxe0wM4uwOig9wMBb2574-zAt0yYfG_8cEjYM9na92cAldNdT0yIhq5924HmHexYEfC57NyGm9Y97TCtD9NbWrckTLc6Fv1QHevEBsF-HUrg5BMrSMsB0mcifnpqLZdb-B4hP3cSjUxGoPY8jT-tTtLaEC4xlPkbcemAWVA-cKHqDffbTkK16yZCSJYiYIE7NaapZCfgrprjE2RD49PoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون چند انفجار جدید مِسِن در قشم ( مناره مسجدش تابلوعه تو ویدو هم دیده میشد )
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17632" target="_blank">📅 19:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رویترز:
12 مجروح آمریکایی که حال 2 تن از آنها بسیار وخیم است به پایگاه رامشتاین در آلمان منتقل شدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17631" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش چند انفجار قشمممم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17630" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هم اکنون شهر مِسِن هرمزگان @withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17629" target="_blank">📅 19:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a1593a64.mp4?token=e1tWsr3gXkHNuj4kCs73sv2bnIU8Allp16CsUrc6t53s1B8wkKGbfH7OpssbNPLkXQqVQoumsDbbDyZVWdvaf3LPXcus2kE073zeRC7lcferEz7v2NuJ-8q9R27AotoRtag8v9JUWG6SEkyXAm-7eiBE-lDRL-gYFKbdC6q9jI8r-rWjAxx1hM5M6vk0HXKYPV3JRAi3SNQgEMvKtvehxGqUoOP72wNk-a8gXda3F5IBz0PYe1yNSvEfT5ysZm4QLmHP3jI7HMA4QY_4wBd1fnmd4KPFkYOkycMV3D9uy2NCeIsiOHM3QzXXQuNqEmZYa9xqvezUa4Z9ZLJkOJBbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a1593a64.mp4?token=e1tWsr3gXkHNuj4kCs73sv2bnIU8Allp16CsUrc6t53s1B8wkKGbfH7OpssbNPLkXQqVQoumsDbbDyZVWdvaf3LPXcus2kE073zeRC7lcferEz7v2NuJ-8q9R27AotoRtag8v9JUWG6SEkyXAm-7eiBE-lDRL-gYFKbdC6q9jI8r-rWjAxx1hM5M6vk0HXKYPV3JRAi3SNQgEMvKtvehxGqUoOP72wNk-a8gXda3F5IBz0PYe1yNSvEfT5ysZm4QLmHP3jI7HMA4QY_4wBd1fnmd4KPFkYOkycMV3D9uy2NCeIsiOHM3QzXXQuNqEmZYa9xqvezUa4Z9ZLJkOJBbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شهر مِسِن هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17628" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنگه بد دعوا شده…
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17627" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیده شدن دود در آسمان قشم و بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17626" target="_blank">📅 19:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر دفاع اسرائیل: به ارتش دستور آماده‌سازی برای عملیات مستقل علیه رژیم ایران داده شد.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17625" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17623">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسانه های
عربی از کشته شدن سه سرباز آمریکایی و جراحت شدید تعدادی دیگر از سربازان خبر می دهند
.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17623" target="_blank">📅 19:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17622">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عراقچی در دیدار با نماینده ویژه سازمان ملل در امور لبنان، بر ادامه حمایت از لبنان و تمامیت ارضی آن تاکید کرد.
@withyashar
🤡</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17622" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17621">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امشب
🫱🏼‍🫲🏽
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17621" target="_blank">📅 19:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17620">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری کویت :
رژیم ایران در یک حمله غافلگیرانه پایگاه آمریکایی رو مورد هدف قرار داد
بدلیل غافلگیری ۳ موشک پرتاب شده اصابت کردن
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17620" target="_blank">📅 19:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17619">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش شلیک موشک از یزد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17619" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17618">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش شلیک جدید از قشمممم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17618" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17617">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رسانه های رژیم : ۵ لانچر از نوع هیمارس که درحال آماده سازی جهت حمله به خاک مقدس جمهوری اسلامی ایران بودند طی یک حمله پیش دستانه و غافلگیرانه توسط یگان موشکی هوافضای سپاه مورد اصابت ۴ فروند موشک فاتح ۱۱۰ قرار گرفتند.
همچنین در این حملات یگان پهپادی ارتش جمهوری اسلامی ایران با استفاده از پهپاد های آرش ۲ مسیر امداد رسانی و دستگاه های ارتباطی این پایگاه تازه تاسیس را مورد اصابت قرار داد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17617" target="_blank">📅 19:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17616">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هم اکنون انفجار و ستون دود قشم ! @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17616" target="_blank">📅 19:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17615">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۶ موشک یا پهپاد شلیک از قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17615" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17614">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مهر : شنیده‌ها از حمله موشکی جمهوری اسلامی به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17614" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17613">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU2jZl-MCUHtfaAEz_25pAEXpuMxzrZFsP0D7EsPbn6x_o5cFbVTg-bN0DcBXKVjPArVkqcjHx01o4kalmOJNTZ2GQA1Klt4WMZ8E7ZUih0bdB0qYYk5rLtpEgAKmQrSIPhqn5X60DVdrn5MdCjSDbLckMRwT7XKRwlzY8Tblga4TGyJAvYy_rtmZ_QJUY3vfj9utcCRC8X05Ado6t6TBKFWuAaW-xkyxpCRmmIZfPw_AnbRFuteSzeLtjo0Y8lHu6GBuN50sGhfDtxShtQ6DGNv2shrcWaUR2fkVstiYOk0A56jkYJw8Sk3OItYQ4nXTn5ZI4BryZkAWHpclnCHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون انفجار و ستون دود قشم !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17613" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17612">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">۶ موشک یا پهپاد شلیک از قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17612" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سه انفجار یا شلیک پایگاه امام حسین بندرلنگه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17611" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17610" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارسالی : قشم درگهان یه دود غلیظ از وسط دریا مشخصه اطراف تنگه
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17609" target="_blank">📅 18:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5ushjrdrC37vCkKWjvKMHxOgkjpmLuOprGCMeYOOp2T69qGwHeEsFcR700AdlPn0Pxxuuw3Kp5hcMHnFEu-9mIqWED5hl10GRNWFJH5sxlX_kH5NKpusd420BWA2M-D6doW3CEZQWE_G8MMVzuzvyorPw1TG4lI7ER2IPzKoQ6S3LDA4OMGD3CJMgecr46Ip1PJL_XJJ9Ic0dQdftoKn65HuW_MT-Jd9oiztgbvLlCJDYNRC3S8XSseJwYtCyBbRVxQoG7tP2uekRutWXqrE1czubBt4U5eXiDTrlxLSwSNMZ_vNydkGGZh3ISyBrUkHQFKI1tGoWfkGYrtkPC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه راکت بالستیک در حال حاضر برخورد کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17608" target="_blank">📅 18:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هدف قرار گرفتن محل‌های پرتاب موشک‌های ATCAMآمریکا
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17607" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارهایی در کویت رخ داد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17606" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17605">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d44ac8d93.mp4?token=Id3sgJZaeTTv-ZWMIqoQjTjqFIurQvTRUCp3wcW1x20ZRG3PpCFR9b8-Q0aNmKNIUzofngPZtzapI4iMYXbWV8iXOg_Lbj58gtGkourJXMg4twWg_PCUH4rVer7kwNVNJRgYs4i5BgoKrn0tj9QCdQdYKylRFlm2Wxde7lshpX-YPvkY1jaKHnfR44sKIVo1U56V8O6qaPsXKBpRd9vCByxkiwxPWYtpOgd_s_hwOg6aX7pKOmbI9DyOE8642t9zTe660c4-ZXki4_UchAiqCt8rdZrVIWaynjoqaquYj8TqqErITTw9B9PMyiuDaAqgcxaXsNoUdk24fT5SAHT3GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d44ac8d93.mp4?token=Id3sgJZaeTTv-ZWMIqoQjTjqFIurQvTRUCp3wcW1x20ZRG3PpCFR9b8-Q0aNmKNIUzofngPZtzapI4iMYXbWV8iXOg_Lbj58gtGkourJXMg4twWg_PCUH4rVer7kwNVNJRgYs4i5BgoKrn0tj9QCdQdYKylRFlm2Wxde7lshpX-YPvkY1jaKHnfR44sKIVo1U56V8O6qaPsXKBpRd9vCByxkiwxPWYtpOgd_s_hwOg6aX7pKOmbI9DyOE8642t9zTe660c4-ZXki4_UchAiqCt8rdZrVIWaynjoqaquYj8TqqErITTw9B9PMyiuDaAqgcxaXsNoUdk24fT5SAHT3GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های مانوک خدابخشیان درباره‌ی سناتور لیندزی گراهام.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17605" target="_blank">📅 18:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17604">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facaf1d397.mp4?token=bE_axnCezWoyFulKdntgV8GhS3s_wNKybRknxj9i23mJ3Zk79pEIEA9k7Va0C5Zg0tkpaDiXMob6lLvg_cam_9gHUMqWcw516s8ceRwKWWbSQLZwSVAK6SJk335w_yRS7gzhl25UzbKeYU9UaNjLhIQAPzWBT-Iz3TigAfEg8ndj01Yy3cz57udyQ61LlJsUnXHKrhi9YYnIO-mg9-LYzUiURgOCV48acXcJJ01W3wn3MYZ-C7Tynyokk-1QD0sWXoz3fmQg-6-rGFbLgCS-l4Q1xjWt7r2vHlxSuMvgwJimbPx0vxyBeeVGg_Di4hKCcgMDaA6OlmzNByZOtRUoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facaf1d397.mp4?token=bE_axnCezWoyFulKdntgV8GhS3s_wNKybRknxj9i23mJ3Zk79pEIEA9k7Va0C5Zg0tkpaDiXMob6lLvg_cam_9gHUMqWcw516s8ceRwKWWbSQLZwSVAK6SJk335w_yRS7gzhl25UzbKeYU9UaNjLhIQAPzWBT-Iz3TigAfEg8ndj01Yy3cz57udyQ61LlJsUnXHKrhi9YYnIO-mg9-LYzUiURgOCV48acXcJJ01W3wn3MYZ-C7Tynyokk-1QD0sWXoz3fmQg-6-rGFbLgCS-l4Q1xjWt7r2vHlxSuMvgwJimbPx0vxyBeeVGg_Di4hKCcgMDaA6OlmzNByZOtRUoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره لیندسی گراهام:
شما کمیک‌های سوپرمن را به خاطر دارید: «حقیقت، عدالت و روش آمریکایی».
این لیندسی گراهام بود.
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17604" target="_blank">📅 18:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0736854521.mp4?token=Ag6Cx1xx8ZMD8P2AK1tylphMks7wkqGkw38LSHBxeVOZKlbsZotNZMSutZrM-0bwf7B7hW3vVyPkjEgMEhmCZsU0lZy5gEr8s_4iJlG7kx4f6NWyclY6aF6_YdNp_WaomS790Teb7qqP6PGIW94aVqH00LEnj3d-D1nvPxJDz6gUeDdWyh7kXj4eWWW0tsgXcjpGV547ptZeOorF4BweDK_CvmRckAc7PBw9Jvz_jJB5ba3eSmX5mjrab8hL8vo8bMkeQrU6iomM4_Z4rqwHBtzyLNci2Q3KrUPi69QnVe5_Umnr0MI1avoCVOJBrHykXqxJM_wn9p5hwB1eNNRrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0736854521.mp4?token=Ag6Cx1xx8ZMD8P2AK1tylphMks7wkqGkw38LSHBxeVOZKlbsZotNZMSutZrM-0bwf7B7hW3vVyPkjEgMEhmCZsU0lZy5gEr8s_4iJlG7kx4f6NWyclY6aF6_YdNp_WaomS790Teb7qqP6PGIW94aVqH00LEnj3d-D1nvPxJDz6gUeDdWyh7kXj4eWWW0tsgXcjpGV547ptZeOorF4BweDK_CvmRckAc7PBw9Jvz_jJB5ba3eSmX5mjrab8hL8vo8bMkeQrU6iomM4_Z4rqwHBtzyLNci2Q3KrUPi69QnVe5_Umnr0MI1avoCVOJBrHykXqxJM_wn9p5hwB1eNNRrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره سناتور لیندسی گراهام:
«او سیاستمدار بزرگی بود. مردم نمی‌دانند که او چه سیاستمدار خوبی بود... احتمالاً هرگز نشنیده‌اید که من این را درباره کسی بگویم. تعدادشان خیلی زیاد نیست... این مرد سیاستمدار بزرگی بود. واقعاً حرفش را می‌فهمید.»
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17603" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ به NBC : گردانندگان ایران مردمی مریض و شیطانی هستند. ما دیشب ترکوندیمشون. امروز نمیخوام در مورد مسئله دیگه به جز لندزی گراهام صحبت کنم.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17602" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ درباره جانشینش به NBC: یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17601" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درباره جانشینش به NBC:
یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17600" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به سی‌ان‌ان گفت: "دیروز ما با ایرانی‌ها به توافقی رسیدیم و آن‌ها از همه خواسته‌هایشان دست کشیدند. اما ناگهان، بعد از دو ساعت، یک پهپاد به یک کشتی حمله کرد."
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17599" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دونالد ترامپ به اتاق جنگ با یاشار:
بنده این توفیق را داشتم که پیکر شهید گراهام را بعد از شهادت زیارت کنم. آنچه دیدم کوهی از صلابت بود؛ و انگشت دست ایشان به حالت فاک درآمده بود.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17598" target="_blank">📅 17:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f6b3525c.mp4?token=ObGlEiWeeY-aUM9LBhB0OjGnkRY1NUf9NUBhiPP3a4B0nFYXczyLwJCyMDGj3UOBoEgaYftpOWZUkuhl9H-rW-8SH3ogL5RGKDmGhPKMq76ZuBXTuNbccMJnrm5NQifKdppQyEpZ7UQGgzBIPcVT77iIbopoBezofjfBomh5h6PzuG4zw5arFu5MW_EWv9Z4J62yPvdYXYHhGxZXzVfXOvYriG4keSKNu6o3O5SkLB4LZOWnY7lTakMW83Q3uhtNhqDOjwzX_EpDF9RJtuV7SO4DONuM8wNhkzVKqEeL_1WlgHDOOdSiLqgq3irrK98vQYUCVvxSpFgBJ67pL4CBcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f6b3525c.mp4?token=ObGlEiWeeY-aUM9LBhB0OjGnkRY1NUf9NUBhiPP3a4B0nFYXczyLwJCyMDGj3UOBoEgaYftpOWZUkuhl9H-rW-8SH3ogL5RGKDmGhPKMq76ZuBXTuNbccMJnrm5NQifKdppQyEpZ7UQGgzBIPcVT77iIbopoBezofjfBomh5h6PzuG4zw5arFu5MW_EWv9Z4J62yPvdYXYHhGxZXzVfXOvYriG4keSKNu6o3O5SkLB4LZOWnY7lTakMW83Q3uhtNhqDOjwzX_EpDF9RJtuV7SO4DONuM8wNhkzVKqEeL_1WlgHDOOdSiLqgq3irrK98vQYUCVvxSpFgBJ67pL4CBcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید ، به دستور ترامپ پس از اعلام خبر درگذشت سناتور لیندسی گراهام، پرچم خود را به حالت نیمه‌افراشته درآورد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17597" target="_blank">📅 16:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ: تنگه هرمز باز است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17596" target="_blank">📅 16:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام : ایران کنترل این تنگه را در اختیار ندارد.  تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17595" target="_blank">📅 16:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">😞</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17594" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام : ایران کنترل این تنگه را در اختیار ندارد.
تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است.
نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ می‌شود، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران.
ایران کنترل این تنگه را در اختیار ندارد.
ترددها به روال خود ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17593" target="_blank">📅 15:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">@withyashar
⚔️
شمشیر زن</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17592" target="_blank">📅 15:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سر صف
😁</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17591" target="_blank">📅 15:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17590">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheFarhām</strong></div>
<div class="tg-text">اقا توکلی یه انرژی بده تروقران</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17590" target="_blank">📅 15:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSepehr</strong></div>
<div class="tg-text">هییییچیییی داداش
😂
😂</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17589" target="_blank">📅 15:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">طبق گزارشات بسیار زیاد شما تو دایرکت، به تعدادی از مراکز نظامی شهر های بزرگ حکم تخلیه داده شده.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17588" target="_blank">📅 15:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چراغ سبز آمریکا</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17587" target="_blank">📅 15:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لارا لومر،خبرنگار آمریکایی نزدیک به ترامپ :سناتور گراهام یا توسط روسیه یا توسط سپاه حذف شده و مسمومش کردن
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17586" target="_blank">📅 15:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سیاست</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17585" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">من اگر تو (تیم خیلی نایس) شاهزاده بودم الان یه نطق مینوشتم با توجه به تهدیدات اخیر جمهوری اسلامی و انتشار لیستهای ترور و مدارکی که موساد به دست آورده و مرگ ناگهنی لینزی گراهام آتیش به پا میکردم. افسوس…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17584" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17583" target="_blank">📅 15:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17582" target="_blank">📅 15:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">باید تا میتونیم مرگ لیندسی گراهام رو در رسانه ها به جمهوری اسلامی مربوط کنیم منظورم جهانیه نه تو ایران(توییتر به انگلیسی) ! همین کار رو تندرو ها با تختی کردن که خودکشی‌ کرده بود و سینما رکس که خودشون آتیش زدن و گفتن ساواک کرده و از دلایل های بزرگ انقلاب ۵۷ بودن ! چرا ما نکنیم !؟ این فرست ها کم پیش میاد.. بزن بریم ! تازه این بار بعید نیست که واقعا روسیه و جمهوری اسلامی باهم کرده باشن !</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17581" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18fcd6ecd.mp4?token=G3hwoKfs1FeEPcAVJj3OWVJpXWgdRVf-3WUf4AC61KN16xq0_WHhvahLY9sdWJT7oBpO-DegYkS6IfCBWUSpBJUx8Bpo-i6bdv7JlON9BJjFeVWafN0WKqSV7dJsIXO2-Tf-Uqrw1U-J1b86Z-zmpiGH4uBObXtkdO7hdyLt2j9trjsqMO1yBfN9HSR8C7mk_P3k4NFaw6tfhgAJTQfiDKK2snHRx4VRswvxNM9zGNJB8jFXGs04LRQF0aN75LooVg62CoWuRSSf-BLokr7mpKoymjWUjw5_mnDPtMTZqOULHdV9taCQ1wYBFL48BYDHf4jBP9EQAToWbq5lvEIGwmyONyP8ufQJwNpHHdJ8c8jNQhyzuav2h9glXvsbEACmQ_SVX8W-_naSMCzdcwdK3BtJF68BCS_2xAchdkIpkrmohp9N8OzHNklpbhc1KvvChIoRKZBYGdm_7BAgF48EgqPsO_91pUybmkexVcSCZq3VjddfBGSEI92Y8rFXxW_R0nHJPz83scyVHsW9sCAeBn-c4TRvsi53ZxRkIFxKANUVmxfEdpoJZlr4BSpbkLtx0PH2LOiXGCrd-DLl7m8ZsJAbL9bkFkzjADQWF_F9yjT0a0OdamWYOlluXY1HAaiHpoDV5YZrlBWMEjKRbIwHj3_Gy12K7nSM1-3tCYSZfGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18fcd6ecd.mp4?token=G3hwoKfs1FeEPcAVJj3OWVJpXWgdRVf-3WUf4AC61KN16xq0_WHhvahLY9sdWJT7oBpO-DegYkS6IfCBWUSpBJUx8Bpo-i6bdv7JlON9BJjFeVWafN0WKqSV7dJsIXO2-Tf-Uqrw1U-J1b86Z-zmpiGH4uBObXtkdO7hdyLt2j9trjsqMO1yBfN9HSR8C7mk_P3k4NFaw6tfhgAJTQfiDKK2snHRx4VRswvxNM9zGNJB8jFXGs04LRQF0aN75LooVg62CoWuRSSf-BLokr7mpKoymjWUjw5_mnDPtMTZqOULHdV9taCQ1wYBFL48BYDHf4jBP9EQAToWbq5lvEIGwmyONyP8ufQJwNpHHdJ8c8jNQhyzuav2h9glXvsbEACmQ_SVX8W-_naSMCzdcwdK3BtJF68BCS_2xAchdkIpkrmohp9N8OzHNklpbhc1KvvChIoRKZBYGdm_7BAgF48EgqPsO_91pUybmkexVcSCZq3VjddfBGSEI92Y8rFXxW_R0nHJPz83scyVHsW9sCAeBn-c4TRvsi53ZxRkIFxKANUVmxfEdpoJZlr4BSpbkLtx0PH2LOiXGCrd-DLl7m8ZsJAbL9bkFkzjADQWF_F9yjT0a0OdamWYOlluXY1HAaiHpoDV5YZrlBWMEjKRbIwHj3_Gy12K7nSM1-3tCYSZfGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر مارک سیگل: پدر او هم وقتی خیلی‌جوان بود بر اثر حمله قلب فوت کرد احتمالا پرواز های زیاد و پرواز
اخیر
‌به اکراین باعث مرگ ناگهانی است
از سوی دیگر، همیشه این احتمال هم وجود دارد که یک عفونت ناگهانی رخ داده و به‌سرعت شدت گرفته باشد.
همچنین، همان‌طور که اشاره کردم، پرواز طولانی از اوکراین می‌تواند خطر تشکیل لخته خون را افزایش دهد؛ لخته‌ای که ممکن است در پا ایجاد شود و سپس به ریه منتقل شود و باعث آمبولی ریه گردد؛ عارضه‌ای که می‌تواند به مرگ ناگهانی منجر شود."
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17580" target="_blank">📅 14:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">علت مرگ لیندسی گراهام ایست قلبی اعلام شده
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17579" target="_blank">📅 14:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17578" target="_blank">📅 14:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تسنیم: جمهوری اسلامی پایگاه‌های آمریکا در ۵ کشور رو هدف قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17577" target="_blank">📅 14:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تسنیم: سامانه‌های دفاعی سپاه پاسداران انقلاب اسلامی، یک موشک کروز متعلق به دشمن را در نزدیکی شهر خرم‌آباد در استان لرستان، غرب ایران، منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17576" target="_blank">📅 14:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرنگار هرمزگان :
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات آمریکا در استان هرمزگان شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17575" target="_blank">📅 14:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مرکز امنیت دریایی عمان اعلام کرد که
به درخواست کمک یک کشتی تجاری با پرچم قبرس که در پی وقوع حادثه‌ای در نزدیکی سواحل مسندم قرار داشت، پاسخ داده است
.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17574" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : سناتور میچ مک‌کانل (۸۴ ساله) هفته‌هاست از ۱۴ ژوئن به دنبال یک فوریت پزشکی نامشخص در منطقه واشنگتن بستری شده است. دفتر او تشخیص یا دلیل خاص بستری شدن در بیمارستان را فاش نکرده است، اگرچه گزارش‌ها حاکی از آن است که اولین امدادگران برای نجات یک فرد بیهوش به خانه او اعزام شده و احیای قلبی ریوی (CPR) را انجام داده‌اند خبر مبنی بر چند ساعت پیش فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17573" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرضا میرعلمی</strong></div>
<div class="tg-text">عمو یاشار
انتقاد دارم
شما هنر ظریفِ به تخم گرفتن رو نادیده میگیری.
بیشتر روش کار کن لطفا.
این عرزشیا میان دایرکت ی چیزی میگن پای ما ننویس. فقط دایورتشون کن.
عشقی
❤️</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17572" target="_blank">📅 13:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شبکه 14 اسرائیل : ایران با کارتل مکزیک رفیق شده و بزودی خیلیا قراره ترور بشن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17571" target="_blank">📅 13:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkmMOsl9vW1Wl8W_sE0EyKeHViQW2a-aMGBc4uUX06I3kYqBWbIY1NSkuYA0iuCTcoMxP0vZfyyvXKgMSfUC4AO3qzpJJVqnJeVo6ph8Xdfp7gJpDx0GuyTmK5T18kbkJYHYM9HwVzsnmj0xgDw1Xd0NFT86-ZVRycRr8I-S1khSOAW5-hADodrtPQOAn1cvHe5FyvJFgajP-1pCGUD2qDKJ8HwxOTv0yipxhsc4lknVS7iML8POfdRENjEiXQ5l_CiHJriekwNlOYFQGfU9jOkQm4cU59aaDvGINLoaS7YczmuMxXkK7HwpaTqII-e6cCZ1QiIn2150xphWl4DDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoZKoZKo7HnjE-XFi_jt4x_pU3eLtxscqnLFLmhcQSGuKJ6n69DFdTLjEmONW7WmLE0k62f3VgKy-821COxoxXttht04P-pha9XQVxmnjA0zcfJQSMRBYUGH5N0nb2DEyx7lksSPdchp1AjxZiX0TkBX8SZ7zoL5w1zojK3ioRU5EzBn_9EB3uQXZtcyTCgRHGkNp82uxsZF7_T-qcj-BjVvDMbVtALFJh6akENB2-H62DXtqk46Pb7FPn2UGrrLq-odxp7TwHHREs3lBzbTUnSs_mOROIZ0VmS3HGa4ZgcDJZGR6jnIr1KN6kak44lCxqDLrvCZFuwQDwHo6f858A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPJGA6325aUiMJutYRlG4ojlL4A57MZPpDIWQu2-RUhqovOdUPw1OSE7Z3tPqcZEKoROX-8RPl4R-0_mvaBm2YYaxTpqlX-VukQ6rm6kGd7nRfyWKnlLBwPfa0XaYh9mLz7uZoIM3dWtIGu0bRTaTP2-TKb8rRXUGbfyNnwgz-IOQUmf9CeavoWCy18x1ulmK1Jn_obR9I7pkPO7wJLXKaahLKBSxitik97TyWZrIhGebUulOCbgOY0Xot386LzM3CmthYzAbVs-hcuIjS6c72GZ9fFxtIr5O2A3O08NytHdzJ3JpZhJ3nl59ahxORHqVB-0e8LifAWeh4iqKYPc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmTFukxFaOQup1VvLXA669FLxpNCKOY1sTA4o4t2WBcXZo6fCzPULfRmXLbqLuuoyvkomWx8hev8BJ2X1ovBrl_JDT6yTqZ_mTN66dJgwPqg9dwOLOwMdqi33Wdyt5kRgVuxD1ZR_3wPtNjoqNP-BtI7-kvLz7of5MjRnYGgUuk2ncAwUpvojeyNWw5lMvkEFG22WY2ZFJPP4fEP_8Y-ycBZxb7lAD6JGT1pQENrDFGLQFXO-7Ia1NlcuyXHAKmot1lStPncX5FAhUUR8kTubV2fuelz6za-fukZ6Yfm3v7eO3904ii-WVuG4dh5cysKvXUgvOwadmj6nW6rJ2cALg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یه موشک بالستیک سپاه در لرستان سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17567" target="_blank">📅 13:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عمو یاشار گل ما اصالتا ترک هستیم و اسم شما عمو «یاشار» اصالتا ترکی هستش
😂
❤️
و برازندته خیلی زیباس و اسم یاشا هم هست و جمله هست که میگه: یاشیاسان یعنی زنده باشی یا زنده باد سربلند و پیروز همیشه موفق هستش</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17566" target="_blank">📅 13:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA®∆§|•^H</strong></div>
<div class="tg-text">عمو یاشار گل ما اصالتا ترک هستیم و اسم شما عمو «یاشار» اصالتا ترکی هستش
😂
❤️
و برازندته خیلی زیباس و اسم یاشا هم هست و جمله هست که میگه: یاشیاسان یعنی زنده باشی یا زنده باد سربلند و پیروز همیشه موفق هستش</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17565" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">همین الان پارچین پاکدشت ۴ بار صدا انفجار اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17564" target="_blank">📅 13:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4352950692.mp4?token=oTwXNEIWSKB5gWoWMwHSRbiJBgRPAsoDAz9tGZNydWliVyRP-WLszszpadArPrQLw8UBf4iybb1YJ0wXuLdJovZXF-LE9ROjtOdTRdTZlbgh1wkLXz_gpVp_1K5N-_KP1Ng4evEOMmozFyOzJc80khtVoYjJNa1ztDGmTdrFYIYtYXX_pcYjhsyq5O8o6d41AXC19sQUD09eyECSjk7DaZo6JjAeIrCM57tWDaqMQd5XMNz28RinTOuvw6GavlXUg5Iff0aqGrCrGDnSlR8CVf350hsXiBUjmF25JghXhLmynLb_VHcIWYerRdBWPM9JzGctTgEDHYjjMJsIPecqKnmNhXI7YhsB1N2tbhIChMHBXiS03ksRQHeZnpE-R3UNV9P4gzcaM-Y2UBsym-WDDGB62M-3ItxyPNCWPsu8WGEDsV8XJohAJ4IZGfJhiaa1VtlJsuPAldwec244pgcoJN-5hNa5I1OiWuJtm8XKXj1wVocQtek7pKouOsLxlw4E-XJbsK212WwyQq_X_Xy_fCkgOKA3IWGSV21_3lede5n-9ptpM-KBjzy-4nSiz3CbyRuCXdfjW0c84R9-mXw1i6BYjHLB1T0oLEPc80To4kpcK2jOFQdn09YBwqT0xMRrbPS9rLxsOvXsSnjsE1ejjWWKbFwslchKeF4svjGjbBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4352950692.mp4?token=oTwXNEIWSKB5gWoWMwHSRbiJBgRPAsoDAz9tGZNydWliVyRP-WLszszpadArPrQLw8UBf4iybb1YJ0wXuLdJovZXF-LE9ROjtOdTRdTZlbgh1wkLXz_gpVp_1K5N-_KP1Ng4evEOMmozFyOzJc80khtVoYjJNa1ztDGmTdrFYIYtYXX_pcYjhsyq5O8o6d41AXC19sQUD09eyECSjk7DaZo6JjAeIrCM57tWDaqMQd5XMNz28RinTOuvw6GavlXUg5Iff0aqGrCrGDnSlR8CVf350hsXiBUjmF25JghXhLmynLb_VHcIWYerRdBWPM9JzGctTgEDHYjjMJsIPecqKnmNhXI7YhsB1N2tbhIChMHBXiS03ksRQHeZnpE-R3UNV9P4gzcaM-Y2UBsym-WDDGB62M-3ItxyPNCWPsu8WGEDsV8XJohAJ4IZGfJhiaa1VtlJsuPAldwec244pgcoJN-5hNa5I1OiWuJtm8XKXj1wVocQtek7pKouOsLxlw4E-XJbsK212WwyQq_X_Xy_fCkgOKA3IWGSV21_3lede5n-9ptpM-KBjzy-4nSiz3CbyRuCXdfjW0c84R9-mXw1i6BYjHLB1T0oLEPc80To4kpcK2jOFQdn09YBwqT0xMRrbPS9rLxsOvXsSnjsE1ejjWWKbFwslchKeF4svjGjbBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17563" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمیدرضا دهقان، افسر پدافند دریایی ارتش ایران، در حملات آمریکا در منطقه جاسک در جنوب شرقی ایران کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17562" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17561" target="_blank">📅 12:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">معاون امنیتی استاندار خوزستان: سه شهر در استان، بامداد امروز مورد حمله آمریکا قرار گرفتند و در حال ارزیابی خسارات هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17560" target="_blank">📅 12:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری مهر :  شبکه ارتباطی تو کرمان بر اثر حمله آمریکا دچار اختلال شد
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17559" target="_blank">📅 12:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیوان امیر قطر: پیکر حمد بن خلیفه آل ثانی پس از اقامه نماز در گورستان لوسیل به خاک سپرده می‌شود.
از امروز چهار روز عزای عمومی در سراسر قطر اعلام می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17558" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_BM2T24uwUS0zaWtQXc0f31FXC4FdtIGNTlLZr8vwtKQP2gJSm5KHSyd0C6YL6ESGGgQCVEw5rU-RsoyH9xn4uxlAXNumaIc7rlr1kZeJJh38Ib_9SbkEkoprU7ggmlOvL1ahS24YMSqtIANS4fbNwPEDFwi01NzONfLPV4zU6U9NmWHuSzF2gAm63ZKYiWY7EHU8pDRWsTFOiWF1M15cK86-NrpYjgGSeyFppeVJAsUUqToTZCPjH8K6fDnwFNJ_6dORIhqQqpF3xOW9kWrwTUJ3VY8pThnD8dPi7myYPCMbhI0KI0XR9utjA6YeJ_bBleCnbiqpyCWjOWTPqm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب
🫱🏼‍🫲🏽
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17557" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هنوز تو شک ام
🤦🏻‍♂️</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17556" target="_blank">📅 11:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سرویس جدید رو فعال کردم اگه بخوام یک استوری حالا ۲ روز میمونه
😂
🙌🏾</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17555" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شاهزاده رضا پهلوی : از درگذشت ناگهانی سناتور لیندزی گراهام عمیقا غمگینم. او دوست استوار مردم ایران و مدافع سرسخت آزادی بود.
در لحظاتی که نیاز به شفافیت اخلاقی بود، سناتور گراهام همیشه در سمت درست ایستاد. وقتی دوستان کمیاب بودند، او در کنار مردم ایران در مبارزه‌شان با استبداد قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17554" target="_blank">📅 11:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">استانداری کهگیلویه و بویراحمد:
اصابت پرتابه پهپاد آمریکایی به اطراف شهر یاسوج در ساعات اولیه بامداد روز یکشنبه
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17553" target="_blank">📅 11:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: اسرائیل و آمریکا دوستی بزرگتر از گراهام نداشتند
نتانیاهو با ابراز اندوه عمیق، سناتور لیندزی گراهام را دوستی عزیز برای خود و اسرائیل خواند و گفت در آخرین دیدارشان به او گفته است: «ما دوستی بهتر از لیندزی نداریم.» او گراهام را کسی دانست که امنیت اسرائیل و آمریکا را جدایی‌ناپذیر می‌دانست و تأکید کرد اسرائیل یکی از بزرگترین دوستانش، آمریکا یک میهن‌پرست بزرگ، و خودش یک دوست عزیز را از دست داده است.
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17552" target="_blank">📅 11:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgVYyRU87iCaFwwsHigVsaHQiOn4e3SXcTx4xkdxQKmK29-9BY97rvjCjh7X17TyCLC3rY_QiqHmHG5awugV7jH4D6UM_ONnchJ_uBe3eFsGlklB5V5oQJOQTmtZ2uhDs47LFrRIenoTynJTNUpHqCaetdIAxOMgD3eVqT2kMUynPp8uo_ZM66DSpK74b_k6a8WB_eUuDAyoHDH2dYu33OOQB-RYCRthmTNyhW26XuqbsI2ZEB9l3mel0-b_4AGwz-2bbf3lFO99t88lzby-DO7tB9NZ29jaPGyyuzHaHjMkh91BVXjyLz-2zMGlSt1_rqjo_PPXBAx6gvTcOQYOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17551" target="_blank">📅 11:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش وال‌استریت‌جورنال :  لیندسی گراهام نقش اساسی در متقاعد کردن ترامپ در حمله به ایران داشته!  گراهام مکررا به ترامپ تماس میگرفته و پیگیری میکرده و حتی به کلاب‌های ترامپ در فوریدا سر میزده  گراهام چندین‌بار هم با مقامات اسرائیل دیدار داشت و حتی تا تل‌آویو…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17550" target="_blank">📅 11:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران رو دوست داشت و یک آمریکایی وطن پرست واقعی بود
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17549" target="_blank">📅 11:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyI7U6qohOFRv0l5fabrAXEgfe1rDQTC9EsZeGrr0RzwQu0C3VYGqXncF28EsTfslgoFEAtu-hlKUsdM7dLa0Fe3P3G2IWSntLVY8Y-no-Qj45oTGQME1_uUX73YNLY9jz9TzSDCeBS01iIJmMYTiT0WUiElTqhs5TTo8nPyGiNTsYj-cQmJdloP8-i5eZG7_UAk4oFs9m6jvlg4YDLbJooo9PInBN7tivLopOnqxr8VzIaw425o2EfIRXrVUThZE6CfrbxM4qTmI2QBOMYrxK_YGuVymzzAdaS1JfTzU7wanB6lM9jmJZeSSIWCQOrn5l0g7uhmoARKRmjD0TdDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود.
جای خالی لیندسی بسیار احساس خواهد شد!!! جزئیات و ترتیبات بعدی. خیلی غم‌انگیز است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17548" target="_blank">📅 10:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سناتور لیندسی گراهام در حالی ساعاتی قبل از دنیا رفت که دو روز قبل در اوکراین با زلنسکی، رئیس جمهور اوکراین دیدار کرده بود. او همچنین قرار بود تحریم‌های جدیدی را علیه روسیه به تصویب برساند!
دیروز هم از کارخانه تجهیزات جدید و پیشرفته بازدید کرده بود !
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17547" target="_blank">📅 10:52 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
