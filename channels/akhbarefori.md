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
<img src="https://cdn4.telesco.pe/file/t_r6O36fvFxyDz1cSWQQxM_R963RZymQu0Y3nFYBC1MGGWfwTroQzz9pkWk54W8-us6MEe7uNk_jdvNKj9sbMlswZYFQk6McxvosjumEPRuXpL2y7_awoYQGVfzkGxolqzCqHwPcLFMhsZGtH8Erh8jW0Ji3wx2bCFlk8_BhEnaondz4Aqfa3tsZlkhwslWzCq-HUX0RjTjV0wOidraFWH1DvfzsInd9KBvxK9P9DUJFG908oSlXjTL7phDeJ4uJT0TjRDnIn12qWX-ZG09JA95LwQRjC9gtlxfcNxp_6Shm2RyLh3zCIA_JIV-k_RNk3B9C3s6zHY7pfFe0l3clnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-664127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXeSVXVscUnQJAhmNU2pAIKoay5EtTYhRq4Fjv2efYePMnpSbubpCXKcWRkNCS9DSHGHEteuUz5PI3AIBBH8mbzdRdOfkpVJ9KBizXnvfGM8kcVEapqIL4PHhra3SwREA1CBkuVz04_I1KLwy6RSpqCPScIcmkagA5_W97ePxZWuMb7s587JtkBVuaEs21iBR8d2xmsfSfxDdjVUv7K252PuOqjCrEQjQVBwic3ZfrAX2xDehZrt0NQ5by7jI8x3cwwYceVqsD2DkhIFaElpPNcnTwjqALZ096cprQ7GAM2d7S9pDwg1EVpQ9NaVKj4KVi0yFSoTpV_4vYEVPwqmMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ جام جهانی، خداحافظ آقای قلعه‌نویی...
@AkhbareFori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/664127" target="_blank">📅 07:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dVjuL_ulndgoTpu5F5FNvizqWj242qc5Kh-oufI6lMMT4sHRwyWiU9822eYPusjAv4_1uuHYF-wlwemood5Brr397T8HxRmKm959Gp1X-Fk1qhTZz-_VgLnXRIVtzSidN3-kYD6l5cCJjyh8gtHCpLER3Y_cRd41uneEdIV9n1Gk-_CuEO-cojdsEUw8-8V4_BA0SStkSrITihkbD1C1UzQQMhojSxN0ksXkltOG3YAAPkFcLrlRke3KNQ4sWuvAad5gUB9Rsc2mAG_cbdrG5KG5Fa2jqUWZyrFUV2H_p0VJI3EhyCHyrCZXN5ptYrOD2lPd8onx5EzmEk4X-1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۷ تیر ماه
۱۳ محرم ۱۴۴۸
۲۸ ژوئن ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/664126" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران در عین بدشانسی حذف شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/664125" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در دقیقه ۹۰+۴ الجزایر گل سوم خود را زد و ایران تیم سی و دوم بود که در دقیقه ۹۰+۶ اتریش گل‌ تساوی را زد و مجددا ایران از دور مسابقات حذف شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/664124" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گل سوم اتریش در دقیقه ۵+۹۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/akhbarefori/664123" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتریش گل زد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/akhbarefori/664122" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">داور سوت رو بزن</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/akhbarefori/664121" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الجزایر گل زد
گل سوم الجزایر در دقیقه ۳+۹۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/664118" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گل گل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/664117" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ثبت‌نام کتاب‌های پایه‌های ورودی اول، هفتم و دهم آغاز شد و تا ۱۰ شهریور ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/664116" target="_blank">📅 07:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجارهای جدید در بحرین و فعال شدن صدای آژير در این کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/664115" target="_blank">📅 07:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664114">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجارهای جدید در بحرین و فعال شدن صدای آژير در این کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/664114" target="_blank">📅 07:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجارهای جدید در بحرین و فعال شدن صدای آژير در این کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/664113" target="_blank">📅 07:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
گل دوم اتریش توسط سابیتزر در دقیقه ۵۵
🔹
الجزایر ۱ - اتریش ۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/664112" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گل اول الجزایر؛ دقیقه ۴۴
🔹
اتریش ۱ - ۱ الجزایر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/664111" target="_blank">📅 06:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
اتریش ۱  الجزایر ۰  تا دقیقه ۲۹ نیمه اول @AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/664110" target="_blank">📅 06:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ترامپ: هواپیماهای آمریکایی انبارهای موشک و پهپاد و ایستگاه های رادار ساحلی ایران را بمباران کردند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664109" target="_blank">📅 06:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اتریش ۱  الجزایر ۰
تا دقیقه ۲۹ نیمه اول
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/664108" target="_blank">📅 06:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گل برای اتریش @AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664107" target="_blank">📅 06:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گل برای اتریش
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664106" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید: روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است، روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است و ۱۷ تیر برنامه تشییع در عتبات است و ۱۸ تیر ماه نیز در مشهد مقدس مراسم تشییع برگزار می‌شود…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/664105" target="_blank">📅 05:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPqeHkng956hDymDXWfRERztLvB3YO5n9Usxd8-9mhs9ufcWtCxBSZ9jugQg46IEcwIJfuFsezUGFNAQS-UNy-B2yUo5XDwYosFLDS-5CNiE33WIWvssOpDjtX5YzxHE8ov0zzHGLTQ5gEqxn8_F1Xnr7hzNsNXTlPYINPAIKK2UhnN6i8SoF2nFMhMqR16TyBd4Uuag8XR2BmrX2LaXQw1ZEC8TseKRn8WsAVLa6Qi4AQHoUYJitpigAq0ceI-soewmH1uIJRpa_hFLu2uAqGhSFTYOAZQ_eJsxWZz2rlvNEHvsPuEl9awSktLfRrhR3fmzA_mn1YJMahG0e8VGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کی‌روش برای صعود ایران کاری نکرد؛ پیروزی کرواسی برابر غنا #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/664104" target="_blank">📅 05:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
منطقۀ سبز بغداد بسته شد
🔹
برخی گزارش‌های تأییدنشده حاکی است منطقۀ سبز بغداد که میزبان مراکز دولتی و ادارات مهم عراق مانند کاخ ریاست‌جمهوری و کاخ نخست‌وزیری، و سفارتخانه‌های آمریکا و انگلیس است کاملاً بسته شده است.
🔹
میدل‌ایست اسپکتیتور با گمانه‌زنی‌هایی…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/664103" target="_blank">📅 04:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBZkUorKNrnix7ET6gVzb8ePq14LdVLoTKy8MBta-sWTmmJQUGx0RvDLI2BmW3VPg-iWfJmVjbaPq9NOvCIy9YI79pkJ_zaLHeEovMfrMSErS2iuXTkyXz6BnPpO5lN_Lj6vtHE1Ui62exBC1aH_PxlHiAVyf6WiygIutODBk34DMPZDli3THW4L2Tk4faH2wSnKzyf99ekrNvv4nsLUfkI2I2MEdncAksljWCDDbcs_vLFe1fGA1rFabFjJw6DDcMI5P3KvkaxfcgXl7QkCoksaKXY33HCAiDqx00nk8xw7OapvcZOZiXc5iH6hGP6liXkpxGzxHYKFX8-9hh1mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/664102" target="_blank">📅 04:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c935e2c032.mp4?token=oCUCmEc2gvqqPT7AaZJuxnOGBCk21CH2YJ97qZ7gOESuMpjPdUI6kuwZTBqfMNzRbGO3H2F4WFP7Yxq_S5NEP1hkzn7u3Y4ydaRq1TKLv3RINUBL8dG5TeSOlflXdw7sMntveUhiSkDjT1qQX7eKldrPjjDU6a-jWq1b4rFLaGBt6gQB8o27ZJo8gwwZfdcy9muo3HvZwxcKu4DXSJzyL3l9l_DMvSU7C6oxAZ4aEyYYAC3NW6fAwKTcbCVLftou8GQNdEJ2nTIstkeCD7HEzCvKEeAr7wOTUVKmLtlOppR1Slpgz0aza9ZFmmjhgGD0k2J_lmLxyF34MVr_VxFflQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c935e2c032.mp4?token=oCUCmEc2gvqqPT7AaZJuxnOGBCk21CH2YJ97qZ7gOESuMpjPdUI6kuwZTBqfMNzRbGO3H2F4WFP7Yxq_S5NEP1hkzn7u3Y4ydaRq1TKLv3RINUBL8dG5TeSOlflXdw7sMntveUhiSkDjT1qQX7eKldrPjjDU6a-jWq1b4rFLaGBt6gQB8o27ZJo8gwwZfdcy9muo3HvZwxcKu4DXSJzyL3l9l_DMvSU7C6oxAZ4aEyYYAC3NW6fAwKTcbCVLftou8GQNdEJ2nTIstkeCD7HEzCvKEeAr7wOTUVKmLtlOppR1Slpgz0aza9ZFmmjhgGD0k2J_lmLxyF34MVr_VxFflQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منطقۀ سبز بغداد بسته شد
🔹
برخی گزارش‌های تأییدنشده حاکی است منطقۀ سبز بغداد که میزبان مراکز دولتی و ادارات مهم عراق مانند کاخ ریاست‌جمهوری و کاخ نخست‌وزیری، و سفارتخانه‌های آمریکا و انگلیس است کاملاً بسته شده است.
🔹
میدل‌ایست اسپکتیتور با گمانه‌زنی‌هایی دربارۀ دلیل بسته شدن منطقۀ سبز بغداد نوشته مقامات عراقی، مثنی السامرائی، رهبر ائتلاف سیاسی «عزم» را به اتهام فساد مالی بازداشت کرده‌اند.
🔹
او یکی از برجسته‌ترین سیاستمداران اهل‌سنت در عراق به شمار می‌رود و در پی این بازداشت منطقۀ سبز بغداد (الخضراء) بسته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664101" target="_blank">📅 04:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا
سپاه پاسداران:
🔹
مردم عزیز و شرافتمند ایران اسلامی؛ فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیرماه، با پرتاب موشک‌های بالستیک و پهپاد به‌سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی‌السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آن‌ها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانۀ مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
🔹
براساس تفاهم‌نامۀ اسلام آباد ترتیبات کنترل عبورومرور در تنگۀ هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
🔹
دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم‌نامۀ اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/664100" target="_blank">📅 04:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ7cHD3sa0S7DnvorEgTzj4K_b-15x2W2aaJj66iymQi-6iD081uCWfkwKd_DzgF-TIWSkC57yHoJdRSm_5SRcBZqGW_4y-ZcTLraFxjpUIdzXDSbu1bB4L-HMeIP8Bmzd7miv5mOvU2B0WMH0-k8AT_dmxUdtfiSwOHPSXFQnzbyWR32-lepLrslVEDSQUF5rpyKSky93WlCYdOROHcrO3UaAI8jDIkNyvf2Q4XvUpCMyf6Hc1ceF2vTZ_jqwfjCcGLUCeVfzJMglHPWU1QSWM9_Vp2GPCEX-ccCQ4p_FRHRKkReLkhIZAsaqNS9D5B3KijtZJDgYmKJxnJeZEiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
🔹
گزارش‌های تأییدنشده می‌گویند صدای انفجار در کویت نیز شنیده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/664099" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین گزارش می دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664098" target="_blank">📅 03:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqHD0OIKcSDEEs0Vb9pu8YxaL7J8-b06NVXMFA3R1pI8cnl_v34y8I7uyO224USoD8VUNmDRIMbPz2TIXmzA4YGWgo3bgzMe2Z7ahpB4DyFoQfrzCuQeqyhl3rVzn6EsYNrZGmj2ILA3qwga7tYmdGxzmtw0RIl2nEzd7u0nax3ozyRn-WpRkrxAZnpGTCN80JRl2C3rIUG7YOI7OmGma-I6EsMb_L1JgkT50BH_VzkGWnOS5822GUdGkb3uR8RvDH1St-ozNyrNRvwBd-tfVczuzkFYl25rY2T7KXqnLyD4x6-hW-MElHIR-LbuSYIEsTs9DqrQDhXkd_utKrKlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: هواپیماهای آمریکایی انبارهای موشک و پهپاد و ایستگاه های رادار ساحلی ایران را بمباران کردند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664097" target="_blank">📅 03:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ: هواپیماهای آمریکایی انبارهای موشک و پهپاد و ایستگاه های رادار ساحلی ایران را بمباران کردند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/664096" target="_blank">📅 02:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maLg3KfRN2mxvoNoWDfx809XPHb1EA0S0UR1U3R2FTAV2uWmI3LIbKp7QLFm9xftz2nRaeSf-o_YnCGNdTgKR88o3Y07MRGXgJ_CLS6EPmzalbOWZjeEcuTTrz3cFe7Z-ontoooMCbPmigu0oib1ibtXd115Gs0TOchU-26Apxl4_k9NvDVnli6FV8ZrRuOnM1p_Xu3XezW1I1kT30Cc19RAE7YbIZlvQOMSDVQZOJ2Ay23Iu0NwpRME2dRuoe_YQAuZySh3lb4JHtNwTkAjh1zRLWwpLvdlnVdJEnGTgAUaYM4BKZyV77tK-MAVTveAnYSn6HghLbvONcRGa3A4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/664095" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرلنگه و بندر کنگ
🔹
گزارشات مردمی از شهرستان بندرلنگه حاکی از آن است که صدای چندین انفجار در شهرهای بندرلنگه و بندرکنگ شنیده شده است/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/664094" target="_blank">📅 02:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe4ff472e.mp4?token=c4MvCl3lt7bCS4juBVE1rWriQappZ9tWH6RvhLE5k7xQRJDXHyhYD-cOieFLqVAlxLdJyY4NdHRglhZtSyeRo0VpazxXQD14lSWr5id-01oh7ExnBI1FjyJwB_PpUdcRoIk6apPeoRno4snyjEWq3R94lu1M-zpWbSi_ro9LhGjDQu543yNZQksPQA9qPGt09Rb0UNrYMXqQ_fsLXy5Nuxlla_3kaR7zo4lY-3UJb_rpJuGWUXtxOZSl98xQgQHBOvvXXZm7CthQTR0aB0MlCpYpCOfZ5NxfY54te-s5-2433pQ01mTFKv-D0Vzo9JD4AkwXC5Yplh3hcEkrGmlexafAtijSJxOF-kcVwoOLJcyHSoyrhhOQ3eYhOE9_iSDNmV6fg7evz-OFmh1-9CF1p7SXuSW-W9nOwrUb73RlV5qKkEFj1cePy_E6ggylhtlUC3QQEmGWa15Lem9Kt-9hhcbVH-HSD34wYHEWy3wZA-sGFkL_Wl9idUd2KcPDbn1y9c88P0jbj-I-BbD_CrtNOwAzvJ8VeNDETWS3tfALRR23_EG1CC0xa6Fx6N45pb8lcilfQP7ysy2ZF9Gprrafmtr2aAqkDvPDlctW3ilWrMMsX1RTRBFAUUZbcTYZ39lJr35GWtAj5IsSrr1wltVJWuGU4m2Svy0ns_u5SyEjac4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe4ff472e.mp4?token=c4MvCl3lt7bCS4juBVE1rWriQappZ9tWH6RvhLE5k7xQRJDXHyhYD-cOieFLqVAlxLdJyY4NdHRglhZtSyeRo0VpazxXQD14lSWr5id-01oh7ExnBI1FjyJwB_PpUdcRoIk6apPeoRno4snyjEWq3R94lu1M-zpWbSi_ro9LhGjDQu543yNZQksPQA9qPGt09Rb0UNrYMXqQ_fsLXy5Nuxlla_3kaR7zo4lY-3UJb_rpJuGWUXtxOZSl98xQgQHBOvvXXZm7CthQTR0aB0MlCpYpCOfZ5NxfY54te-s5-2433pQ01mTFKv-D0Vzo9JD4AkwXC5Yplh3hcEkrGmlexafAtijSJxOF-kcVwoOLJcyHSoyrhhOQ3eYhOE9_iSDNmV6fg7evz-OFmh1-9CF1p7SXuSW-W9nOwrUb73RlV5qKkEFj1cePy_E6ggylhtlUC3QQEmGWa15Lem9Kt-9hhcbVH-HSD34wYHEWy3wZA-sGFkL_Wl9idUd2KcPDbn1y9c88P0jbj-I-BbD_CrtNOwAzvJ8VeNDETWS3tfALRR23_EG1CC0xa6Fx6N45pb8lcilfQP7ysy2ZF9Gprrafmtr2aAqkDvPDlctW3ilWrMMsX1RTRBFAUUZbcTYZ39lJr35GWtAj5IsSrr1wltVJWuGU4m2Svy0ns_u5SyEjac4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: جزئیات عملیات امشب رزمندگان نیروی دریایی سپاه علیه متجاوزان آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
🔹
شناورهایی قصد داشتن از مسیرهای غیرقانونی و ناایمن جنوب تنگه هرمز عبور کنند که نیروی دریایی سپاه پاسداران با آنها برخورد کرده بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/664093" target="_blank">📅 01:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فاکس نیوز به نقل از یک مقام آمریکایی مدعی شد: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/664092" target="_blank">📅 01:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صداوسیما: شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/664091" target="_blank">📅 01:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk0MuynZa4kfDYc0xd0gAnXD1jE82JW9BBfaVdUXPtJ2-p9AyODjeLnkwzEssFy1TUc_yJG5qmkGnBE5MxIGOhP8KlE7hF3MgjFzbdYb23MTUlSRGPHsSwIk_Gcld5r9hYqUK6dMGskeKQUAd1FkHKUZNzp2rvJJGeAFTYN_ebM-PAOIxKW6TiWIkHCDTNELiCb2Dxv1rqH2xiVFbxHXFIXokMDD1EfeUZ0I37oVFyyex96I-Yad0X3uMHUWLYmOte_ezY0cppTd7U9ZD9afhlDmkiSRKT9pPwVdYwT8jub5BTLgCHkNXvD4zMo9guTooK_Encr8Uo-dSejhIIcAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام حمله تجاوزکارانه به اهدافی در ایران را تائید کرد
🔹
سازمان تروریستی سنتکام رسما حمله تجاوزکارانه جدید به اهدافی در خاک ایران را تائید کرد.
🔹
طبق ادعای این سازمان تروریستی این اقدام در پاسخ به هدف قرار گرفتن یک نفت‌کش تجاری صورت گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/664090" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
صداوسیما نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/664089" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای خبرنگار آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا در پاسخ به حمله شنبه ایران به یک نفتکش تجاری، حملاتی را علیه اهداف ایرانی انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/664088" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujzmHV_obSAcGg0sxK2Vran_-dUJMwGKzeGV5_5w_qpHNgTGhq4sz1F-UE3Fc4wcYyUEn9fsgqdj_UtLtozZdbeYJs6zOWQ3g_kU6oe8K-XfDWWcos_EWXJK8x_S24r72Oc-IPLZzpNKQSwxW_B8zT2ZTorFf30_y-09s2MuViJpVrVwabQaASsfIlRtrHZkg_TUvXwUw857PhIOC6jyiXIXT6QA_obzi_wqmphk3HyDePj9u4grTiHpY27s2K1NVQVIEuEHKJzPdohGXlxQ4YRKPR3UkNdQYB2JtomoIeL8KAL9KNC36lUDZWS6aLCnqGO4ixCeD3YlK-aYCWVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صداوسیما به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/664087" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664086">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در سیریک
🔹
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در  سیریک شنیده شده است.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است.
🔹
برخی منابع مدعی شده‌اند که صدای انفجار در بندر…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/664086" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664085">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در سیریک
🔹
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در  سیریک شنیده شده است.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است.
🔹
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔹
شب گذشته نیز شهرستان سیریک شاهد حملات نیروهای تروریستی سنتکام بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/664085" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664084">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ترامپ امضای توافق با اسرائیل را به رئیس‌جمهور لبنان تبریک گفت
🔹
پایگاه آکسیوس، نزدیک به منابع اطلاعاتی رژیم صهیونیستی گزارش داد دونالد ترامپ با رئیس‌جمهور لبنان «جوزف عون» تماس گرفته است.
🔹
طبق ادعای این رسانه ترامپ در این تماس تلفنی امضای چارچوب توافق با…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/664084" target="_blank">📅 00:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664083">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ترامپ امضای توافق با اسرائیل را به رئیس‌جمهور لبنان تبریک گفت
🔹
پایگاه آکسیوس، نزدیک به منابع اطلاعاتی رژیم صهیونیستی گزارش داد دونالد ترامپ با رئیس‌جمهور لبنان «جوزف عون» تماس گرفته است.
🔹
طبق ادعای این رسانه ترامپ در این تماس تلفنی امضای چارچوب توافق با اسرائیل را به طرف لبنانی تبریک گفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/664083" target="_blank">📅 00:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664082">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANhM94UKdTff-6YvXiMbQ_VxS_uODCmuN0hoF9OI1kEpmLq6eI5tT_bTHg6yP4Dxkb8S-tSFGasaml6EJr3zGNNDUGc-Dmim16SqgVNBBBLqfZmcYjLFCCt9PTDysI8YFIc22nPuVp5xRCJof_jW9tAjph67uoiUmjCV4_QUU2mKV6uNsJMtM9TZJ6nNHxpIVsY6m4Rt9eUJv_9waQXwO-g2CVsvFTMmBiViawBuvqiIwy21j1PSokLYt6mEDYrVnYJUElp-UmsZfowRFnMdCtOSM5p7ZtTJgdPj0tgZXXU_AfGaXb_tyDnaozXUqnfTOeKibIuKH-DW6eG_8SFPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در هر کشور چند روز باید کار کنی تا بتونی بازی GTA 6 رو بخری؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/664082" target="_blank">📅 00:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAyVxIIMy9Wf2lqHpFoCHG0Xcz7TEh9N8l7WJNKw0qisq3C88dghXdFYinOM_VW-qOPGn5gS4qDNcTPpYTVqVuczINCa_kIDmCgqV_3Bn3CimPo_7jZBgb38KvAjicWWr_CQF2XkkkCOqAgbbq_l9vllX6gqxA23fPHuskIkOMWNwcU15dY9l41WvjNiSetDj4_C6-tw_H-CnuMWGg-tjFPdeaSnphKLuhNVnWgYMxQI70wVdKht1l7wdFEwy5v_rWVplBqKceQqabIM6C8ZbBVJM3E9L-In3XXAMqV0IsAZd3zNY4qg7XESH6_KBTNKTg4HWxeKAQOBD0Ho40tgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانشین ولادیمیر پوتین درگذشت! | سرگئی ایوانوف که بود؟
🔹
سرگئی ایوانوف، وزیر دفاع اسبق روسیه، معاون نخست‌وزیر و نماینده ویژه رئیس‌جمهور این کشور، در سن ۷۳ سالگی درگذشت.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3226136</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/664081" target="_blank">📅 00:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به النصیرات در مرکز غزه
🔹
منابع خبری از حمله هوایی رژیم صهیونیستی به النصیرات در مرکز نوار غزه خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/664080" target="_blank">📅 00:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بقائی: این یک تناقض آشکار و استدلالی مغالطه‌آمیز است که با هدف فرار از مسئولیت بابت همدستی در یک عمل شدیداً متخلفانه بین‌المللی مطرح می‌شود
🔹
از یک سو به‌صورت علنی هرگونه کمک یا حمایت از متجاوزان را انکار می‌کنند، اما از سوی دیگر آشکارا به ارائه «حمایت‌های…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/664079" target="_blank">📅 00:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5xnCP46eiLHd1NeXGykqP2sdJ07FQukSh-ytPuEl1qwl8aAEGUMCIjkIijVKhMa3KuJ4-a6Gkxy-Oxiwv8XlETiVcSRy3UYQzADlCOBBTWx4VzY8Nhfe3BizovbBLbqshuZFoCS7kue95DL-TysvrLDyNAi4JJpgCfEApEoDcjyUCS7_BUKzdKYUyixDZnxRaI6YhcBJM8YMtwLrSw5KiA2rQc3X8ClRuFq0nYjO4jRUhiQovcfg-Bnxp8-aSN46a6WuG7RPHCaBSplMH8pZjfuKoYdSSOP5TOTgIAhM32LBI6tM7vQL_6xFlSZKa2fGIb1jiFVYzFc0gys_EHbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664078" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
رسانه‌های فرانسه گزارش دادند که در ۲۴ ساعت گذشته ۱۰۹ مورد مرگ مرتبط با موج گرمای شدید ثبت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/664077" target="_blank">📅 23:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda6118ec8.mp4?token=AtcJ53MV0Xorl93wnFsh2DqVAMDb1NDWKZ0MzHim2KjR3xJTDPDYYOjGONX-0Iu5BIF7wAcQgTqwc48PoHx0oaPeQ_dz1e4b5ue3Mf8rUPJ09P_82q0LKH1H9NjrWNHaAhFmmvML6TD9cf4Pi7qNBx62jsed1VICSyIOJrtHO_PIU-AJH3CKfeEP7dpxoxXABPqicbjWhqJwdaqZCIclrTaT3tvGbp9vDWrUqwWM-Asdx0npYAGLjb8b934C_14DW3CxN2xtoxMPEIxXBEoc1olc82QNlui0VovXeJQg0Y_D7ZaxG3wBGhS0kUYP6l4Vs8_1fYei-svdZ7ELDKVmDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda6118ec8.mp4?token=AtcJ53MV0Xorl93wnFsh2DqVAMDb1NDWKZ0MzHim2KjR3xJTDPDYYOjGONX-0Iu5BIF7wAcQgTqwc48PoHx0oaPeQ_dz1e4b5ue3Mf8rUPJ09P_82q0LKH1H9NjrWNHaAhFmmvML6TD9cf4Pi7qNBx62jsed1VICSyIOJrtHO_PIU-AJH3CKfeEP7dpxoxXABPqicbjWhqJwdaqZCIclrTaT3tvGbp9vDWrUqwWM-Asdx0npYAGLjb8b934C_14DW3CxN2xtoxMPEIxXBEoc1olc82QNlui0VovXeJQg0Y_D7ZaxG3wBGhS0kUYP6l4Vs8_1fYei-svdZ7ELDKVmDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ری اکشن جالب قلعه نویی از لحظه گل تا مردود شدنش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/664076" target="_blank">📅 23:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac9cc1551.mp4?token=IOG-yKxyGoRfRV77gMK2BYF7gWmCY2lzBDPCeHj8V5VIaAsoNZbOU-q7iGHRubQh2oxNgQ3NWmDdPILc_iHi-5tt1gMJ-F1rwox9KZFq2VWNFfYktjPJU3Hp7YEBZgUvcYle3M9k1H836mctzbd53pF66X5OqqFPX05hMgjTMCbfqH-CDVluywA2VaKbunEtcjtmLQvhRB3OGJwx73LnwxBoW_OV4ngNXftKzosULI68lLzA6vTd9NsPCMDe0NudTN8jQQSDXmVn_Pmfz3sdaIHs7iJ2vZ-dXUsXYjDE9fmvxudX_-BQxeFXlgG9knXHxgeUBj6iCqGA__gfr6oNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac9cc1551.mp4?token=IOG-yKxyGoRfRV77gMK2BYF7gWmCY2lzBDPCeHj8V5VIaAsoNZbOU-q7iGHRubQh2oxNgQ3NWmDdPILc_iHi-5tt1gMJ-F1rwox9KZFq2VWNFfYktjPJU3Hp7YEBZgUvcYle3M9k1H836mctzbd53pF66X5OqqFPX05hMgjTMCbfqH-CDVluywA2VaKbunEtcjtmLQvhRB3OGJwx73LnwxBoW_OV4ngNXftKzosULI68lLzA6vTd9NsPCMDe0NudTN8jQQSDXmVn_Pmfz3sdaIHs7iJ2vZ-dXUsXYjDE9fmvxudX_-BQxeFXlgG9knXHxgeUBj6iCqGA__gfr6oNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کواکبیان، نماینده سابق مجلس: مسئولی گفت کاری می‌کنیم اسرائیل دوباره حمله کند تا مردم بیایند پشت نظام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/664075" target="_blank">📅 23:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664067">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7l0LPKGZ53ikVUb0QRpgw3D3MylGookjqNxUkW-I4A28qq6lI94VNVln7od6N4CcE0GNvns6pYs6aCmhyZrWmHmVyfgcocOo5PBZ5SIvaqttvOgm8DM8nXJwlLNVsn0aVIPj6aYaRQM_f3QnTR5H8CVSKiwdZvetSVpmLXaH1-VxWQXvk_t1-PWCE7WawHVVqI1N8eatiVtL9GgNdTVR1lHSfIs8WvchS_8Cvdp1OaXowj3JErd7EzXn4Oy8AtMG-T_RDdiGpyiPp28ldQVOpp_9z5dciYwQ7Igja5LPckzyEp0Wr1Ao3ZY5t6ByfqkJEt1hoh88DK5ZnTd4L7Q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qytph3g6_0C4FZ1LWipQ31-qCgQIur6VpB4EPkzRkXZsMPx695JdfSumHBj4gKbBFvQig4pRl8K87XMonxXxg4Gtfdb-aJ-BkypkssRBwTIoUJTcUx2iJG6tp7UyJ_99mI6AZwoUnQBB5wRtoyGZXfEikX41yN9lBrajsb5ct-ME3WgXF0hD-Ut4OPcIXumNoFbcNACfNSxu-qOcZBoqPvenJKCR8O6K231dsatJsCFmkxNhQNwB-eDTat-GGs6qOTxMYLanw8N5q1s67jlH48l4oplmgFnsAV0gJ-za4LJsmuvPXsEhUFC8H_pWXpmHL7s6EycTDtgkkdMIu8voRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IU1asXyCcFrWn6BorQKc4kmxIAdeYwvD89-pRQobxqW_r5wJppX3BybcwgN-64kMj-y3KC8SogkOUE6I_d7GgcAnIxMbaWGkKJ5w52yeIaZmh020njkrt_hLZmx_3KubFFj7lGpS0H2Zmw7lJWCJi-LpwUcYDGvWJxMMB19KZMBO4XRCT8wp-DeQZM8w-kOxDYfuwF99J7WQJ847rkUHM8_9PWQLdidMDkxrr73C7Ib8wQOHrDJL_Q0PS6d-ABJit8zcVB-_l9PUFIxU7p7QoJ--6IhjSJiOIOjqekSVPo3P13G6Ms1vKHAjxUOa5nn2XY4G-FCh3Lv_sF5HIucCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkqcmloH4PrCTx1mvgK9TkZ2UWhcQ51tVwv_oTPtZp-0jmvCj6rbjqjAGtr-7PCtnuSlfhQhSTgFQXYOkXbfiMVJnc3fPIuxGwun6d79vPbAvyQzIRa-z76BmM-PZ53OJbItSWbkJOhQTOP4gM26rIknDo7WNCqcjmTk-tkWoVmroK3pvc8Q9E_PbRmhNGBiXQY1RmLpy4znKno6kao3xK6mlEDbHxcO_jslUmSApolhsM-1RxuhIahPqr_I61qC27W4xVNi6pnlxPTMe2M1Oo8r_kvCNvzYwPxlF-2W7K4wkt86F5aTQFYx3kTFGM8mPVZ2rJit56Po9yCovPP4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7scZLbBky1dvLiwCD7yq89Fsxr1ssrzlr9-q-R7bHXjw1EfxqL5_oVFStnFZpDrfzDLwiTZu8VpIjpDuVzxmzNVh1MMeTw41Heck26TicXtxBE_Mumq_i32vJlC7a3zY1NentSNNEz0yqUorvR7HXm-XIVjpRHAhoBwo4KUrQFdjcAegqdF_O30VhwrW8ImEx_mNIGn4sNtJk7e28koGuomD7-z_Fqs-ioIZRPQZi9guySKyelyiTGv1aIh4-d08cEQeKUA1oVIZmdea96FjXX02cxHlTv6zHvMorR6hX58_lp1YJlF_UkdsQWWWXlmAWzXDZkKkh8HeS5lGYZKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUCot9WQJH1ocAY5Zd_OdCtbRIhkllUXIJRv5cnZi2iiV7NsEJajBxRVCMsLg6JNy-DZHtaVUllrEp7i0L9leJlmppPu7vcAdjcKY9MN357TmX9dY1u1nBpbuAA0ZFSvsV0okeakD0Z0seKIcDTSZcnrpuMc8dq4lCuzM0sJEmZAjP-1NQkC8Bavqm68Umry7l4sjdZxmA8cyIeFdp-4gKqYXDaHwMMbgQCTFYeFxtPqTzxpA4H9N7t20uxchTFOXuFrnKYIRBagEBL9Qf4lx0uMN8Xif17iJ_ido5QqCcDHb92AmC8oXCMIJJgOBZasVsyv8P7YJsn2Q9PijzkIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRI-PBdUuwExBfz7dIZ8WHcu8f14Yrjh9ccDaQqNvnumNtTiybXLoaxCKPcnpMxYYaUp0j6L5u3XKdQon2O2q0BZRry7icX8EJ9sro8CgCTyWq6jNVhm6lNe1sGI97cTg8sfV0Oy6zXtbHzlPgbnPVCsTTCCkd-dnQGmsUKR08TBbLpvrwQ7aBqihE05j18-JgvZIWR8z7NBXBoHVev75bAUhyEIhq62A7PAtk64E-IA95_cwB6a4egJDaV9asPlHruLpkZ_JElrR_OW_QHL8O-CF1jJSL-K0YsxHDjBkKy2AQe7STLcU_sLPkXUj6irIk_Cdrf9JNstcfMxGQxEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTyLjCP7Olc_97QljSLPasiozfLNPHUN8XyGGlmFnt61N7U4YEcx9evgKhowz1w_ytzqOTv_kIexQgUClkZcuvGM8LDlJav2NBG50_8HWZ1Wpum__G6rZ0EfTn7ZPKvMo3SCjsx1Ak5A1u4RQ64YjuasgvnDupmN6yzA4qY-6XCZwAVwnOZ37hFkw3CsZ5EW2A59eJJ0IuDI_-FmSj8jVhmUAAN7o74gd7YtUq8vLq_8eIiMdnSuz3ZY4SXVCNq1gXQGftZ2dyGKG6XJdTDHnpuggVy1jAyo1DHJYnig7-DZsc6D4sDs3K7cLZ98WEDP3iMkF1bCHn8s1z5g36zBpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
اینجا عطر نذری، با عطر اخلاص درآمیخته است...
▫️
دست‌هایی که بی‌نام و نشان، اما با دلی سرشار از ارادت، برای پخت نذری روز عاشورا کنار هم جمع شدند؛ تا سهمی هرچند کوچک در خدمت به عزاداران امام حسین(ع) داشته باشند.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664067" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664066">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اختلالات گسترده برق هم‌زمان در چندین شهر رژیم صهیونیستی
🔹
ده‌ها هزار نفر از ساکنین سرزمین‌های اشغالی در اوج گرما بدون برق ماندند
🔹
رسانه‌های عبری زبان در گزارشی از انفجار، آتش‌سوزی و قطع برق گسترده در چندین شهر فلسطین اشغالی ازجمله شهرهای حیفا، ایلات و کفریونا خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/664066" target="_blank">📅 23:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664065">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
اندیشکده واشنگتن: تعیین قوانین تردد در تنگه هرمز در دست ایران است
اندیشکده واشنگتن:
🔹
نظم سنتی دریانوردی در تنگه هرمز عملاً فروپاشیده و ایران با تحمیل مسیرهای جایگزین، کنترل جدیدی بر تردد کشتی‌ها اعمال کرده است.
🔹
ایران بازگشت به وضعیت پیشین را برای ماه‌ها غیرممکن ساخته و کشتی‌ها را ناگزیر به استفاده از مسیرهای تحت نظارت  خود کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/664065" target="_blank">📅 23:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664055">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OouKMF9joPGDjQq2UpWWP8uOg2dGRLn1Lm3X43MFadLOOsFyt-WnVcv-0vDLy6QoisNHX8YLyrFP_-_1ZjyZStx07oM20o1rrj5We0a1L-X2NujFfJ7V98xkyoxVxHHbU4wBNyCX29vx3Bg3tcIwV6x9bkg5keBe4udY3SaXhmEAmP7Ku5kiQ8aF8S6BxXzYo3Giqafgrsg8kEYcUIy4bd0YUW1x_MC9anjGueq9uaIGoclj5KT4PXR8VacOHhe_naz68mdWL05X9Y-N6BlFqNiVlzMP57zx1j_pPi1-dV0yIRiScnDx-ebhcKplNjtJKFdyxjto5gwVbJVEjnegWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0fkYA8ysijxi-mIEiBzyQKWlSfT2YKuMUL5lnqBJxHcmWUB6ng32R5qGmwWPkymYCtqhntiGLz0Ku3sKis1qcoCJVHuSDia93mZRk8ZXz_wuxETtgcR_V0aMY2nhXkEjwTiMxb82AwCZ-88iEpbRetS0AGWbVSchi2tgTAvOQ5I_Pxw51phqjsRieEdAO4Kydvx906U-DX2iVT67I3IrPAtu_iMFQz7mnoWbAGmPiJrrEhdaX76q-Np4yYjBqxO93rQ3pYzlbIJvcaPPsFAhDzZp0u9YLcbvR9_qKSzzHiymC66JGs4B_2k4OkODy4mMtAraSocmq6d9omBeBITuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXb90NFstZN0RS8WIXAfrJPydHVxL_FyloRZK-FVRAzK9pPEXsJhixX2_0ABmLNOde0Lgd1D3tTLXKi7ajIS_gwrl-OE8OKGMvg4Upt5lGVoZEZfYe-3vwz_de3jd3JEg8mG4CSkSPlqLUfVQO5x6eQ4xZDgnj7TYoN-DWnVIaOdCz8pv4watlvlE57tpgHHWZFF4xFMLB7oJhqmEQXalae-Pv0qWomI-Qbd8vHK1-Z5UxSjf-op5N8KafXZ39ze6-2cupvUoOLJiwJ0d0vBI04Fl7pzv5FfD7UkbC6H6CttgbI7MRaypzJs9LdBZvOxWk7_PeSVrmJ_nU05Yc31TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzMCPQ5RzgMQQiUdfbq35P_WUx8xMJTeAmYgJdEagy28aCRC6P8tNrwL_vYR66D_PUD64Wjk2iuCd9UbQFvCCtSqtqbEw1mvcpkFiApaOM-xQiqHd1m0lSue0enSWd6QjN53d4nO-EepI48TqU-Gdbcwhr-yjTiTroWqok_J9xfAjMrkNWukkqAHfVGfLukqL5akLHRwLK-Qoj_aJBdYYZkPBu6mhHa8SnhUZaM6jGAcUu66zwdz0Ne6QHJjwtGnc6kudb0oHz21xtspjotgC53ydnINowvHJARAZyYSaVLyaKfkpNiAzmAbSgBMDZ2PoZRUuROmmKIPwtlSmokUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLP6QN6uUZUZs8zWI6ulL-za0DAHfNVy0UW9GWGf_XZvVYQeQctpFA8xvh_gHB8tjha-rnz7M8C84H09dAeeqXMAzX9wq4GrOc8i5w9mgmniJ3LBPLK9NLIahZaUmdhimEqr6jjt-gfaGOkmRL898c6VhQPsKb-W4WmNtC_GUKUFmIMchCkHxrbr3QFfOsZkEZUOXqDkzcNFMXOXzGin3Ci52QXiDtSwVVn58DKJzfIVKbGAQToa-2c2c-EHFkwBmZMOMKP3DGdljXnx2VKrwFhVMOWxwFLzTQqn_A68skmT6JU0BnZeHg9itmm0tplOrzrPPbi_c9wxaeRr3c5RTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XemLGu08MCGp0Au774rMRIg6tHEoozq5ROZfawTF7_9GS-Z0_VbNAwfgboN5rXDUrsRBxtwKY3l4vzkDhbYDmaY3zs_qxFwtXsnCHXlPQ2bYD9boFlcG8uqqXOSfF6d1UUDMFESIQR5KWFgbFUNMZvf3rWh-RZEvekFxYE77Bys5U2893SAic15FKmwSV3kNOai14hoOlP-bIES8QNfO4Sya2Sse9JlAQ6hBbOxYWJI-2pmfiwjpU-MuS1TVc39X77nwHjyRMSxny9hD9X5CUYxQ1GeX9o24pgtP5XrGjvhy-175IgG9RpuvEMk_QqgfFIt3SSOxklMl5WQLIND2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4ldHBaHh1AL3AnH-2PGnTk6BrpLFHYAsX2XNxoQ8HO_Px1KY3K10umsRlNSc9A8Fh8GOgWHBagn6S4Gp_nbOua3TQ_Df7k2iCCF9kdMUTupkWUGpHREvQezmjQHN2-4GZf_G6bugS-Z_KI_MifMJbLKPx8c_z0PHfnf6l0IK2_fDZxoxRQGZBitpejQzcvtK-eh5CBx49QgEutn65TCQD8TqVTCMdIhgkNhTeULbReRFFPq9Dk8jdQixWVJvEbItUL6Td3xEEvzd50awW9a_rQ7cUZElXQk_-RPg3KPxfwAMh86kMCmRaQsy5M7Jl3s7PMk0KjxB-Lua9AGRnO_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7fq0x3oqR9FwUdAcXOPBTGzFr5xtqg8iIdEsDYrSTDRRc_CGHzxPBtv_mVT19X0RnD4iBT3cBiWW1dzGRCzRMMyijKnlsCZ7Q1iLXTZ8j2pCaZvI2ClpNr3B7TtbOu1E4Q3k7BvG16JsdiPdjzh8t7GLyn5HgV6qx690K9p9vK5VK72L0bOzog_er4D_BHJIH4_n1T1bdHGBOVvgHSVvtreR4IAVjuZQxXqF3hWk_-LE0wnEMRCtMmzDSSdBVBouYysbcHkZz-IY7rMWsXp-kBtAk1W8Q8QvWsM7A9owre8RSo2BJxGhNXt-eGtfThObIXUa3X1naaDN1jPKQpJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1XUtQqZy_NmHQRTYGAsLSN2HhntgQ3nO5u7HdYR0aGbx3ilhGEJ1N29AseG0BEQCQpHjJ_ObOzJt3u7jaAdq5c-HnQwNd3jaX5eP0H-n9iBGR28u8_ZyygIhvoRprNwlSabYWXSFXUtZwtu-0H5d7ezrveCk-Uf4XB7DpIEtw35uVX00h3ZpB05Bfk3cF95ZKVHMw6C7qgj1_BbWwXwOZZ-PpY9l3BKdg4B121WlsEGOlvctI_lDt3iIiqXQ8GTXwZV539Kg8OO7wRvD3hlD4IL4BEABF1wTfVy6_Ud29kMO410RbuRdLR6NTDa-PXgh56zcYzOPhdEQjEyUf9fAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdHzyrcsKzCFL7YwclBaIfKaUUwGq72bG_2n4_a9HCUq5C98c5bPmTZ42K5HQA-ml3FR9zVR0Rm4hXjstGjz4Urh9QXU9ku0-5S3utPbjJiPzYpoa0m5VaWrxnmrJcwyF8lonAZgYr55MEyViXyMGP7M4ZRPyje4Z7ydB_KzVGYmd1MWuiXLdrVvypuzgeoSyvLiFSjs0Vv5FhFCkvWz8cAo_bYNkDAAnKGYRBxX2AATyBplVGApUx-NfR8ECL8nZGtX6173tv32_sZ64EIliuLZeLqyMWBInUSNbR_pHiOiNk2qNmQBhrp6zQBOwldavNRsWkIi44inkmZ_XtM83g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از حادثه ترور نافرجام رهبر شهید انقلاب در مسجد ابوذر در ششم تیرماه سال ۱۳۶۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/664055" target="_blank">📅 23:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
پشت‌پرده درگیری های شبانه ایران و آمریکا/ یک اشتباه باعث «جنگ بزرگ» می شود
👇
khabarfoori.com/fa/tiny/news-3226117
🔹
ادعاهای تازه درباره نحوه ترور شهید کمال خرازی
👇
khabarfoori.com/fa/tiny/news-3225979
🔹
نانسی عجرم: امیدوارم تیم ملی ایران ببازد!
👇
khabarfoori.com/fa/tiny/news-3226080
🔹
جانشین ولادیمیر پوتین درگذشت! | سرگئی ایوانوف که بود؟
👇
khabarfoori.com/fa/tiny/news-3226136
🔹
کلید صعود ایران در دستان این مرد است
👇
khabarfoori.com/fa/tiny/news-3225973
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/664054" target="_blank">📅 23:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce687d0de.mp4?token=G0WXZP3FceAkpo0CdFhCfnUAIqh-cpPNNw9TTYKAkXjS-vRUtnqTJxYD713Pfe5XnAVHPtBK8fBf4v4x9O3ytvfmN1E1kZh1i5eZXJBNbvkZ5o4S7Tr0ncul2dzrB7moXK7iX9PaJCA03zwz437g0BiVG-Rq5sBM-6njn4VFhANHMfSGXR67qNEf2z6wu43LIPO8f5Csvf07cyyIkkg_BcYLn4P2pGdpskpXMUsudix1Q4VbehadhPxtQ3WEH2ULpGnAbd7s1Yi0S63iBQrfYa70y528f2TkJc3oGY1-rGsyien7xcOsEWDTS1R95Ds5KhX8tN61ceaaeceSt-x_WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce687d0de.mp4?token=G0WXZP3FceAkpo0CdFhCfnUAIqh-cpPNNw9TTYKAkXjS-vRUtnqTJxYD713Pfe5XnAVHPtBK8fBf4v4x9O3ytvfmN1E1kZh1i5eZXJBNbvkZ5o4S7Tr0ncul2dzrB7moXK7iX9PaJCA03zwz437g0BiVG-Rq5sBM-6njn4VFhANHMfSGXR67qNEf2z6wu43LIPO8f5Csvf07cyyIkkg_BcYLn4P2pGdpskpXMUsudix1Q4VbehadhPxtQ3WEH2ULpGnAbd7s1Yi0S63iBQrfYa70y528f2TkJc3oGY1-rGsyien7xcOsEWDTS1R95Ds5KhX8tN61ceaaeceSt-x_WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: نماز در صبح روز دوم مراسم وداع، بر پیکر رهبر شهید انقلاب اقامه خواهد شد؛ یعنی صبح ۱۴ تیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/664053" target="_blank">📅 23:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664052">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بیانیه جمعی از اعضای مجلس خبرگان رهبری پیرو پیام راهگشای رهبر انقلاب
🔹
جمعی از اعضای مجلس خبرگان رهبری در پیرو پیام راهگشای رهبر حکیم انقلاب اسلامی (مدظله‌العالی) و حوادث اخیر، بیانیه ۱۰ ماده‌ای خطاب به مردم بصیر و انقلابی ایران اسلامی صادر کرد.
🔹
در بخشی از این بیانیه آمده: از ملت عزیز تقاضا داریم که کماکان حضور آگاهانه و با صلابت خویش را در میدان ادامه دهند و ضمن حفظ اتحاد مقدس و پرهیز از هر اقدام مخل این اتحاد، به سخنان تفرقه‌افکنانۀ برخی ناآگاهان که به دنبال محدودسازی این بعثت‌الهی هستند اعتنایی نداشته باشند. حضور مردم تازمانی که رهبری معظم (مدظله‌العالی) مصلحت بدانند ضروری و تعیین کننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/664052" target="_blank">📅 23:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664051">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سردار حسن‌زاده: مسیر اصلی مراسم تشییع رهبر شهید در تهران
🔹
خیابان دماوند-خیابان انقلاب-خیابان آزادی-اتوبان شهید لشگری-اتوبان آزادگان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/664051" target="_blank">📅 23:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664050">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKWt9KIxxzaZU95SPnyf2D5-riKycVUKRCraV2MJK_twlFh5og-c8qARnks9bfUO8mARmAfXPbNUkzwEy1GgE3eO_HcsV3cW_x1BNFGleQ6Zax9aaRj7NREOR9LLoqyuSNvq9GTBwmlSBEbr2IuNPdHn5rjOtdGEMzu9NMZvFmz2oM3gBqNfJrrtyUKU4prncyuc5N19NeP7QxuV2lRfWFmX7Ll6uwxpbidsWdW1w7luAia4MPYk5RsxcS9xV5AF2VPAqbyJyOZgJbe6Uc8p-ynm15mmKQNYqu0cG6zAfcjbkoSDtosxqlDlYIl-3j7mSDl0aMRzesuHf-ESd0Y_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره دست به دامن ai شد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/664050" target="_blank">📅 23:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664049">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24769656e6.mp4?token=m_RIwizhbSdUPkdNlhPeIOGT0XMf5wkhRNS3wGUzIF1qvxOVVt7TEfeLEV1WfvwiooxGUz7eXf_MWE9wR5q5doUiCODSJTK6YW-y-8Gg9jYBXeUuUlvR_SiiVZkUVIJG3og-uc9fqpZCmVQv_qo67ef3z2lQpxX9utd9vxCvJfBgDCpO8lXe4qa4rgtw2TBI5frKezyJRkXOwNlgz_xC7hE_117XTlvYOaA67RYFzPf6E3bm8HUFYCR7X7JTXJmMX5QB5hxn4bcwriN9AFSsu0OlWcBATzU-h7CIFsIQM8fziNisWziVv8wKs_T8naVJiyp3teFpDVR2GOg4ps489w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24769656e6.mp4?token=m_RIwizhbSdUPkdNlhPeIOGT0XMf5wkhRNS3wGUzIF1qvxOVVt7TEfeLEV1WfvwiooxGUz7eXf_MWE9wR5q5doUiCODSJTK6YW-y-8Gg9jYBXeUuUlvR_SiiVZkUVIJG3og-uc9fqpZCmVQv_qo67ef3z2lQpxX9utd9vxCvJfBgDCpO8lXe4qa4rgtw2TBI5frKezyJRkXOwNlgz_xC7hE_117XTlvYOaA67RYFzPf6E3bm8HUFYCR7X7JTXJmMX5QB5hxn4bcwriN9AFSsu0OlWcBATzU-h7CIFsIQM8fziNisWziVv8wKs_T8naVJiyp3teFpDVR2GOg4ps489w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت مخفی و مرموز از آفساید شدن گل بازی ایران و مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/664049" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664048">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سردار حسن‌زاده: ما نمی‌توانیم در مراسم وداع با رهبر شهید توقف جمعیت داشته باشیم
🔹
برنامه‌ریزی این‌گونه است که مردم از یک نقطه وارد مصلی شوند و پیکر مطهر را ببیند و ظرف ۱۵ دقیقه از آن بخش خارج شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664048" target="_blank">📅 23:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664047">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcsGj78JfDMWCetoeh8GR6yXBuZgH-SUjwz5lO08PljHvRP52-0LqGXltE6DYRB010SlhCGtDBDSkUU_7ZgNAVmc2SkZbEcHmBiuzrhzZvzx4oMN37eV3ujcWuQp8FMjWaxjmpjaTe_n7vQOQyTYHNzNmKNfW01dpsH0kj-glTf7OhXMIF6TEQJuJFvr8XMhBbMyHaX2qiX6pp9Tke6dk_m6xPt_xJOjDGhtsuZzZs-Q_myCReJxqJrs2bGeWVat-rFy1lnPu8cdutbVYe6K-3l-W-Gej143yc4gMXPvUDnUaQEuaRqe9t2lifF7IYcyEdK9gwDM0rzC5aIWm0zyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: این یک تناقض آشکار و استدلالی مغالطه‌آمیز است که با هدف فرار از مسئولیت بابت همدستی در یک عمل شدیداً متخلفانه بین‌المللی مطرح می‌شود
🔹
از یک سو به‌صورت علنی هرگونه کمک یا حمایت از متجاوزان را انکار می‌کنند، اما از سوی دیگر آشکارا به ارائه «حمایت‌های فنی و لجستیکی» اذعان دارند؛ حمایت‌هایی که جنگ غیرقانونی آمریکا و اسرائیل علیه ایران را ممکن، تسهیل و پشتیبانی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/664047" target="_blank">📅 23:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664046">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
رکود در مسکن ادامه‌دار است
سعید لطفی، دبیر اتحادیه مشاوران املاک تهران:
🔹
دولت باید با در نظر گرفتن وام‌های کم بهره، از خریداران واقعی مسکن و خانه اولی‌ها حمایت کند تا بازار مسکن رونق گیرد.
🔹
وقتی تولید مسکن نداریم، نمی‌توانیم انتظار کاهش قیمت اجاره‌بها را داشته باشیم.
🔹
تا زمانی که دولت از خریداران واقعی حمایت نکند، رکود در مسکن ادامه‌دار است./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/664046" target="_blank">📅 23:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb08ab33f.mp4?token=IVC3Q8ol3AVjUcZ8yPeImvKqM-RF5SQAl9OBznQZiXbrSOrHvJYChbh-mUVmCBR26QSADSyqtvBzfMQurgL89Oito_U6nOCw_pem0BmmsHliF9KtAYYObIRDCcspSfe52d7xbgmWx_dJ7OfeYpbJYWDU9TebrY2TbSPteZfvYOcxfgkMKIORJ6GSKWCtMQu3yZnNgJgBnSuHUf0Ny1Xc02DNtLU86EICwVNMRUqdERaGWDTfukHMqY6N0ntXy6ur5-cFlMKJs2vC3jGJmusMD28Eqm4T9qNCI4fp-QYU9ONRDbNC0hcz8iu_IBSXrMd56QqC_P_xRwESAHizlGnA6XizemnqPDHA130gn-qzmZpNFi3PYccIGhnrBs8krsAo7Zw4EgLkrMPEaaPyiDuQoYej8IZUs6uaE0DvbkKoBlQL1USXn97EWYP4DSMGGH-TTc4pbe93C-t1B258BTpIa5UR3ZVfBJn4py_qV_VMJDHMY8kQg1sgwmoKA1DHqZ3qcdF6OSC9XqhNG6MoaCJ_5KxtcqyzWxAAWHsmxTOR11XijDYp2ZWOsafsMuWonFMc_VpWpKAI0FXHzMaj6P9rzZEuwoZYIb5EMBWjql9hPW6uktTOKnzcMo2odnqqYe6HX8akx6TJuPvhGGMCEba7uR3A0zAzXPQrTSrN3lcHogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb08ab33f.mp4?token=IVC3Q8ol3AVjUcZ8yPeImvKqM-RF5SQAl9OBznQZiXbrSOrHvJYChbh-mUVmCBR26QSADSyqtvBzfMQurgL89Oito_U6nOCw_pem0BmmsHliF9KtAYYObIRDCcspSfe52d7xbgmWx_dJ7OfeYpbJYWDU9TebrY2TbSPteZfvYOcxfgkMKIORJ6GSKWCtMQu3yZnNgJgBnSuHUf0Ny1Xc02DNtLU86EICwVNMRUqdERaGWDTfukHMqY6N0ntXy6ur5-cFlMKJs2vC3jGJmusMD28Eqm4T9qNCI4fp-QYU9ONRDbNC0hcz8iu_IBSXrMd56QqC_P_xRwESAHizlGnA6XizemnqPDHA130gn-qzmZpNFi3PYccIGhnrBs8krsAo7Zw4EgLkrMPEaaPyiDuQoYej8IZUs6uaE0DvbkKoBlQL1USXn97EWYP4DSMGGH-TTc4pbe93C-t1B258BTpIa5UR3ZVfBJn4py_qV_VMJDHMY8kQg1sgwmoKA1DHqZ3qcdF6OSC9XqhNG6MoaCJ_5KxtcqyzWxAAWHsmxTOR11XijDYp2ZWOsafsMuWonFMc_VpWpKAI0FXHzMaj6P9rzZEuwoZYIb5EMBWjql9hPW6uktTOKnzcMo2odnqqYe6HX8akx6TJuPvhGGMCEba7uR3A0zAzXPQrTSrN3lcHogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت رسیدگی به هوا و خنکی برای گاوها در خارج اروپا خیلی بهتر از مردم داخل اروپاست
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/664045" target="_blank">📅 23:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b1b81c91.mp4?token=otE9rxorrPhGfxcK1pj4Rl5XgSuzXJm_I58KKR5FfUh-I0742BvdKP5QbbQx2B7PZ_546Q5k-6a8NriH2uDcx3oFcLxjbrIP6hPv06bIht3-7260CQxD7fiucoWz1rUzCh8ea96vRaCIKP10zmUc0TI8LO24_FncY08F8epGAt2y6a8uerkb3VZg3Meg4dV35WlbeSZ9O7XEhnecTCCR8qo6BAXAfi3V6G2antJnkZQEitYCjUlJYSQ560X8Ba1tT6yB4QmB2r8oJRsaGaP07aYHq4fRJmbChgaP8YaY3bceohQrdOcdZFKe8N5QUyxdHuiahJ86zxnlxbX1B4RgMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b1b81c91.mp4?token=otE9rxorrPhGfxcK1pj4Rl5XgSuzXJm_I58KKR5FfUh-I0742BvdKP5QbbQx2B7PZ_546Q5k-6a8NriH2uDcx3oFcLxjbrIP6hPv06bIht3-7260CQxD7fiucoWz1rUzCh8ea96vRaCIKP10zmUc0TI8LO24_FncY08F8epGAt2y6a8uerkb3VZg3Meg4dV35WlbeSZ9O7XEhnecTCCR8qo6BAXAfi3V6G2antJnkZQEitYCjUlJYSQ560X8Ba1tT6yB4QmB2r8oJRsaGaP07aYHq4fRJmbChgaP8YaY3bceohQrdOcdZFKe8N5QUyxdHuiahJ86zxnlxbX1B4RgMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/664044" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای وزیر جنگ رژیم اسرائیل: اگر ایران علیه اجرای توافق لبنان اقدام کند، پاسخ می‌دهیم
یسرائیل کاتز، وزیر جنگ اسرائیل:
🔹
به ارتش دستور داده ام برای حضور طولانی مدت در «منطقه امنیتی» در جنوب لبنان آماده باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/664043" target="_blank">📅 22:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju1gfignLK30NQ3Y05xzwSHg88ZYaI2ApLV_H6onv78dX9ph_PY8gOdpPIUfjcThswPKSYs2fGnR0Ua8B41P45IwXBLXeRL1OhMAQ3680DhvDyn2TdsQ5Mde8pwSFnlGjOwg1R1RtEjS4XzW3RV1bTAd_ijFzdOqJP_K0px_5aLQ6eWllTjs-kmlNjsKdxHGmRHabUKPZuqvcbQES-pHm19LazEfja6Eh1SqizVbZxNEgS3-tUuj2ld8_fTwj-NFjlr2qfHWYztXlqzrK9-vCteNIeLGOndO0C1zs6EUpZ_srrvG9c4lBi293_12cB78ZwgQty-S2-SEe5XLi_NEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه مدت‌زمان انتظار برای دیدن پزشک متخصص
در کانادا و در بریتانیا بیش از نیمی از بیماران باید بیشتر از ۴ هفته برای ویزیت پزشک متخصص در صف انتظار بمانند.
ایران با ثبت آمار تنها ۲ درصد انتظار بالای ۴ هفته، یکی از در دسترس‌ترین سیستم‌های ویزیت متخصص را دارد.
میانگین زمان انتظار بیماران در ایران برای ویزیت پزشک متخصص فقط ۴.۳ روز و برای پزشک فوق‌تخصص ۷.۶ روز است.
@amarfact</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/664042" target="_blank">📅 22:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
۴ فرد مسلح به یک مقر نیروهای شبه‌نظامی در شهر کراچی نفوذ کرده‌اند
🔹
در حمله به کراچی، کشته‌ها و زخمی‌هایی وجود دارد و در حال حاضر امکان تعیین دقیق شمار تلفات وجود ندارد/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/664041" target="_blank">📅 22:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=k_CudD69BJ4X15TLr-sID4fshGX8rBHkXzKDrQv4KDnkUYNSpvDTsm8mp8x4a0R1jQAuIWXY_1iPxUwxcd4mvTkkvlspl-kDuzZYnh8cboYpxD17ZWNgSb8TdKRHmg1FARfMffIOBeFmpPblP7dxBqfNT3XIUi2Ld60Z4lYQlTB2rUHprrsoGd_cW7b3Ioz1QDKzC4pLjGJG90Yg3tlhNWqiqTmHVKErnrO_kroEbtH9Qs3f68kONCHN3XQV_c4TJCEDe1li_KGffXC-gcjyuvf2R_VHcbauPWsDjIJatXqcTW_Sazj8HtDP_XzPqVtMTWGo_8YloPGH9rfwnaQ7eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=k_CudD69BJ4X15TLr-sID4fshGX8rBHkXzKDrQv4KDnkUYNSpvDTsm8mp8x4a0R1jQAuIWXY_1iPxUwxcd4mvTkkvlspl-kDuzZYnh8cboYpxD17ZWNgSb8TdKRHmg1FARfMffIOBeFmpPblP7dxBqfNT3XIUi2Ld60Z4lYQlTB2rUHprrsoGd_cW7b3Ioz1QDKzC4pLjGJG90Yg3tlhNWqiqTmHVKErnrO_kroEbtH9Qs3f68kONCHN3XQV_c4TJCEDe1li_KGffXC-gcjyuvf2R_VHcbauPWsDjIJatXqcTW_Sazj8HtDP_XzPqVtMTWGo_8YloPGH9rfwnaQ7eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/664040" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
دومین تیم صعود کننده به لیگ برتر فوتبال ایران مشخص شد
🔹
تیم فوتبال مس شهر بابک پس از کسب پیروزی در هفته ۳۱ لیگ آزادگان، مجوز حضور در رقابت‌های لیگ برتر را کسب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/664039" target="_blank">📅 22:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-hv0Bxf-swBtAr6KPvmVGgHpP9nwtry4FJJltb8a8AHNToh0kPgNP9y_BWjGwhwbuhGdAjNREZCABGdLXYo1xUcLVhzdgyIa698czNg5OAnFBkQmBDwm1SJZTWRQZUnEiO4rIkCyAgFahOTHC2cv6j4XEZE-ju_HoCJDSU6iWs3YKlRfT1iWwphYNfN7zRlByTzAgAjChGuDSP4N00Xv52CtP4j_C_6fVAytnWQ-N4Obrizj1PlPeuydEePyVWCf6rAsqtbNAGH5le_bkARtvPWeYcVgmegPKmPL9XGJNMUvoR05J9NKnMuevAKCPDy1X1pC_L0711HqHbxPRPrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده درگیری های شبانه ایران و آمریکا/ یک اشتباه باعث «جنگ بزرگ» می شود
🔹
رابطه ایران و آمریکا همواره در خطر بوده و این دو در «لبه تیغ» حرکت می‌ کنند و ممکن است هر لحظه وارد جنگ بزرگ شوند‌.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3226117</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/664038" target="_blank">📅 22:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R59carns7NS7yrQKvLAvgIGwN6lv5VgIKocO_tuVjdtg4KjdfU9N74AWDSFlGH-ziz4uIbAo_ISzCa45KXXsv0a3EM7k_RF797Ie0XqyjgdP4kTBT4tqbAn4kq_RjTwiq-JQWXBHEDE8SWFMU0zwp1MbMRv4KpZhRgCOIehHwx45hM3LJW24BY4UJuDtQzrvFdrK9Kp0yjM8ZEeaXjBXpc_4HM3FNwZpnQfo9uMIbzDz1Q-pRj2w64a2Y6PNKKZYKnZl4YNcgxcRdaBu9QsUReFkcoBTiPVIKGTGE5I21oes8rkOHqEInsazIjbCxXlSYfjhiktTNdmMp6exfz8KBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: شمار قربانیان زلزله‌های مرگبار ونزوئلا به بیش از ۱,۴۳۰ نفر رسید
🔹
مقام‌های ونزوئلا اعلام کردند شمار قربانیان زلزله‌های این هفته به دست‌کم ۱,۴۳۰ نفر رسیده است.
🔹
پس‌لرزه‌های متعدد عملیات امدادرسانی را دشوار کرده و نگرانی‌ها از افزایش بیشتر تلفات را افزایش داده است. هزاران نفر نیز در این حادثه زخمی یا بی‌خانمان شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/664037" target="_blank">📅 22:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd486c8659.mp4?token=vMLL0CvUfQrp5fqWuTBQu3MpmUef9xI1SdR1y0tuv_sVeCTMxXI8LWoRfoKxrLAX1ecEh7NI9p64MrPQGyF7tI7BKsFMhc8h9np1E6NCyGnOHXmzKk4GJvU22I0VXJuC6T_4lK__WRsJLimjCNRRNNmy7TB6gwVM43Rd7mx8_E6iHiVrb__2QuYOSWWOVPGt03NWfbD2amd3Y24s4gNd9At6zhxz27mRgcF5p7hrvoeYLlkyBz6rSX8hsZcPWaUbhJFqe3CRoEvKH3SGy808BCmv3H8ZXNAuWXBCAlNOUYJnxkczTPnR8mB6gIYTGd83adGUHAkJN9MREx6xpR-utZnLOyhZ9uA_Ni__wVzDcCEgbMsZ2E0L-KmYzZysh34ylfrR6jCHZdhbuUolYjG1lIIeecoJJjPxunCzde43iXd-WnLS8DUej879Vpf0BkEzUxjmyZTXyuB2zXoph8LQuA1n7B_vcjw8sKghxjwdjkbkVHmcbkuFZzPUqjiyI3nvORie7xzEE_2y1W4yDwZSgUedq8AUVw9yW1aKxJP0gQ-xUIJLMparAPZRp4vyd9fNXIPvGPvM-iewTzeJceE0nuIO-0OYghXjx7J-qGOm79RDL28kcfMJH5UbjqIjjq5xh2LxW17uSqRiUqBebNHCBVpX0Z8XXoMPSaVZ331Qh0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd486c8659.mp4?token=vMLL0CvUfQrp5fqWuTBQu3MpmUef9xI1SdR1y0tuv_sVeCTMxXI8LWoRfoKxrLAX1ecEh7NI9p64MrPQGyF7tI7BKsFMhc8h9np1E6NCyGnOHXmzKk4GJvU22I0VXJuC6T_4lK__WRsJLimjCNRRNNmy7TB6gwVM43Rd7mx8_E6iHiVrb__2QuYOSWWOVPGt03NWfbD2amd3Y24s4gNd9At6zhxz27mRgcF5p7hrvoeYLlkyBz6rSX8hsZcPWaUbhJFqe3CRoEvKH3SGy808BCmv3H8ZXNAuWXBCAlNOUYJnxkczTPnR8mB6gIYTGd83adGUHAkJN9MREx6xpR-utZnLOyhZ9uA_Ni__wVzDcCEgbMsZ2E0L-KmYzZysh34ylfrR6jCHZdhbuUolYjG1lIIeecoJJjPxunCzde43iXd-WnLS8DUej879Vpf0BkEzUxjmyZTXyuB2zXoph8LQuA1n7B_vcjw8sKghxjwdjkbkVHmcbkuFZzPUqjiyI3nvORie7xzEE_2y1W4yDwZSgUedq8AUVw9yW1aKxJP0gQ-xUIJLMparAPZRp4vyd9fNXIPvGPvM-iewTzeJceE0nuIO-0OYghXjx7J-qGOm79RDL28kcfMJH5UbjqIjjq5xh2LxW17uSqRiUqBebNHCBVpX0Z8XXoMPSaVZ331Qh0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور هیچ وقت سرطان نگیریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/664036" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/664035" target="_blank">📅 22:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بقایی: ظرف ۳٠ روز از توافق نهایی نیروهای آمریکایی باید از منطقه پیرامونی ایران خارج شوند
🔹
جزئیات این گزاره باید در حین مذاکرات مورد بحث قرار گیرد.
🔹
یک تعهد دیگر این است که آمریکا در حین مذاکرات به نیروهای خود در منطقه اضافه نکند
🔹
ما این موضوع را به طور…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/664034" target="_blank">📅 22:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef2292562.mp4?token=qVT3-ooJmC19h_bkA7qQU5HjghyJqe56P24Ig-AZXLK6LAWah7kktTUx_WBeqHD_MftyFXZEEeJ0bgahexxHq0krsCn0Jf8mDqQ58-Dqmqsq-T8wBQ8HQ77PBTXi0aO5km-uDvp9h4eh96qomSCtbxSmBZ4ruqv9E8WeiBvLwtpA85SqlXAIjvZ8Kbpy_4hNZ5NkXbdRqiXMbTKHlil4ZawNQxERWLHv6f7UYGRhU3v4wvQyZnQkOyO1U2V1mQXvwfo38YjVmIxAmKMv_05HTn-M_cst6piDkB27EciB0V16l8SQI3LGl5ybzuws6Yayle4TP2EJ-tGJxLkq30UHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef2292562.mp4?token=qVT3-ooJmC19h_bkA7qQU5HjghyJqe56P24Ig-AZXLK6LAWah7kktTUx_WBeqHD_MftyFXZEEeJ0bgahexxHq0krsCn0Jf8mDqQ58-Dqmqsq-T8wBQ8HQ77PBTXi0aO5km-uDvp9h4eh96qomSCtbxSmBZ4ruqv9E8WeiBvLwtpA85SqlXAIjvZ8Kbpy_4hNZ5NkXbdRqiXMbTKHlil4ZawNQxERWLHv6f7UYGRhU3v4wvQyZnQkOyO1U2V1mQXvwfo38YjVmIxAmKMv_05HTn-M_cst6piDkB27EciB0V16l8SQI3LGl5ybzuws6Yayle4TP2EJ-tGJxLkq30UHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راه حسینی
🔹
همراهان عزیز خبرفوری ؛ محبت به امام حسین(ع) در صدای شما جاری شد. روایت‌هایی کوتاه از کارهایی که به عشق سیدالشهدا(ع) انجام می‌دهید.
🔹
این ویدئو، روایت شنیدنی از صدای دل‌های شماست.
🔸
الوفوری را دنبال کنید
👇
#ایران_حسینی
@Alo_fori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664033" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کیفرخواست پروندهٔ رضا پهلوی و عوامل اینترنشنال و من‌وتو صادر شد
دادستان تهران:
🔹
کیفرخواست رضا پهلوی و تعدادی از عوامل شبکه‌های اینترنشنال و من‌وتو به اتهام زمینه‌سازی برای اغتشاشات روزهای ۱۸ و ۱۹ دی‌ماه سال ۱۴۰۴ صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/664032" target="_blank">📅 22:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b451747df6.mp4?token=IzPGNIurJ_WG3Nf8rXgkAiUoXmPTwpp5fIsHmP3tK0X6ak99ZKlNDCNFhwlC_uT1k6UjmG0KGGZYQ2jiKbHNA2Sw4ugrdUFXLtYT0OKfJH9C5DInVUfDj2Ad9y-E-sXH9fhIGxPYdYmt4qQ9fkAN-Jdl4k5ae9CXFPxkpsMhk6o8Ie1Brm9LNPI8jdVwBq3rcVvWLG70pbxqRMGms1Al2uJXhK7qNteQjUUFxgPo0HRK9NONZmDx8DmuAmPPhc5NozXXd_eghwEuaTFTLPrvcymsc3PDkJhUNbZX6eeCkUyzAXyXEsUEDgQx2ln29O0Ghh2NeNdEcJkNNyKD-4jx2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b451747df6.mp4?token=IzPGNIurJ_WG3Nf8rXgkAiUoXmPTwpp5fIsHmP3tK0X6ak99ZKlNDCNFhwlC_uT1k6UjmG0KGGZYQ2jiKbHNA2Sw4ugrdUFXLtYT0OKfJH9C5DInVUfDj2Ad9y-E-sXH9fhIGxPYdYmt4qQ9fkAN-Jdl4k5ae9CXFPxkpsMhk6o8Ie1Brm9LNPI8jdVwBq3rcVvWLG70pbxqRMGms1Al2uJXhK7qNteQjUUFxgPo0HRK9NONZmDx8DmuAmPPhc5NozXXd_eghwEuaTFTLPrvcymsc3PDkJhUNbZX6eeCkUyzAXyXEsUEDgQx2ln29O0Ghh2NeNdEcJkNNyKD-4jx2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهوی خبیث، دقایقی پیش، از عون و سلام، چاکران درگاه ترامپ در بیروت، اینطور تشکر کرد: از دولت لبنان بابت شجاعتی که نشان داد، تشکر می‌کنم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/664031" target="_blank">📅 22:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a7cfe3b9.mp4?token=HvpTWJ3twkkG5ES1CalLIA9L7PW_2GSKjK6UeTWmaKr_nY-OjN1fp8bvNOro33CEd3KlPWJswA_PgvAJQFZDfkmpAgeH826F7w0LuQtgsgZpjtFnntePA5Q3w8RdykZjiUq8vng6TyJitMSqMOkUgeLn-s4byoL0G1Zk-KJRrIXnutjZgOr4EkD1E4brvFUnGmEWSLB-lp0LZVaeUbiBfJJqoktYMaEyoed6K2-OqT9K5FTtx1-T8hGJOFtoaewXJwpGE8C7pGXCmygEhpF2ns-O3PS3DG_aKlJlwGXkpKGtw4VBPzQ-vRfB4rSyaJs9iS70u-MphQKozrtIZr36Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a7cfe3b9.mp4?token=HvpTWJ3twkkG5ES1CalLIA9L7PW_2GSKjK6UeTWmaKr_nY-OjN1fp8bvNOro33CEd3KlPWJswA_PgvAJQFZDfkmpAgeH826F7w0LuQtgsgZpjtFnntePA5Q3w8RdykZjiUq8vng6TyJitMSqMOkUgeLn-s4byoL0G1Zk-KJRrIXnutjZgOr4EkD1E4brvFUnGmEWSLB-lp0LZVaeUbiBfJJqoktYMaEyoed6K2-OqT9K5FTtx1-T8hGJOFtoaewXJwpGE8C7pGXCmygEhpF2ns-O3PS3DG_aKlJlwGXkpKGtw4VBPzQ-vRfB4rSyaJs9iS70u-MphQKozrtIZr36Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
بیمه؛ طاقی استوار
…
بعضی چیزها برای ماندن ساخته می‌شوند
مثل اطمینانی که دوام روزهای سخت است…
✅
بیمه‌بازار؛ همراهی برای آسودگی
#بیمه_بازار
⁩
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664030" target="_blank">📅 22:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عراقچی به عراق می‌رود
‌
🔹
وزیر امور خارجه جمهوری اسلامی ایران، فردا یکشنبه در راس یک هیئت دیپلماتیک به عراق سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/664029" target="_blank">📅 22:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
نتانیاهو: هیئتی را به واشنگتن خواهم فرستاد تا منافع امنیتی اسرائیل را در رابطه با پرونده هسته‌ای ایران تبیین کند #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/664028" target="_blank">📅 22:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اندیشکده آمریکایی: ایران از اهرم تنگه هرمز به طور قابل توجه استفاده می‌کند
اندیشکده جنگ:
🔹
ایران بر الزام خود برای تأیید عبور کشتی‌ها از تنگه  هرمز پافشاری می‌کند.
🔹
این امر اهرم قابل توجهی به ایران می‌دهد که می‌تواند به دلخواه از آن استفاده کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/664026" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw9tFmuaOmIQev3bN9qAq1ZhiAsZcpQPfO76JXcQZNKC9WqmfqB1bx2dapTo2ntEWgrSb12Gr2PectjhK1gEQf2UqW-uUsWORjetitRJQKEzMRQ51smvWDcyaxai4Mr8-Eb3pAuJ4qbzXwe-HkOOmtmw_OSvEj8qi7CAG27QkqU0no7cmBgUZZNFTJe9u833DpPaCC0bBu_YEwmnM-RxPofWSzYcknwpZqAwMUcR5WTnAWByZtDxeGVLE-s_TyrXaqDrRDXsirIDRL8gt-SvlbRylIHcqKwCiIHgkGkqVoxjJ76kcZ4rbpt4zpVD1hMsisXPHwFaNjp8TY6bmvJn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه قلب دیگران را تسخیر کنیم؟
🔹
امام علی می‌فرماید: هرکس حق کسی را ادا کند که حق او را ادا نمی‌کند، دل او را تسخیر می‌کند؛ زیرا احسان دشمنی را به دوستی بدل می‌سازد. قرآن نیز به دفع بدی با نیکی فرمان می‌دهد. در حقیقت، انسان‌ها بندۀ احسان‌اند و با نیکی…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/664025" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
استاندار خراسان‌رضوی: محل خاکسپاری رهبر شهید در حرم رضوی هنوز نهایی نشده است ‌
🔹
به تأکید رهبر شهید انقلاب محل تدفین باید به‌گونه‌ای انتخاب شود که زیارت حرم امام رضا(ع) تحت تأثیر قرار نگیرد. محل تدفین هنوز به‌طور قطعی تعیین نشده و چند گزینه در دست بررسی است./فارس…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/664024" target="_blank">📅 22:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
نتانیاهو: به ارتش اسرائیل بر داشتن آزادی عمل کامل برای دفع هرگونه تهدید در لبنان تاکید کرده‌ام
🔹
ما به اقدامات خود در لبنان علیه هرگونه تهدید فوری ادامه می‌دهیم؛ روز گذشته ۷ تن از نیروهای حزب‌الله را که در خانه‌ای دور از نیروهای ما بودند، هدف قرار دادیم.…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/664023" target="_blank">📅 21:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نتانیاهو: آمریکا و دولت لبنان با ماندن ما در منطقهٔ امنیتی جنوب لبنان موافقت کرده‌اند
🔹
اسرائیل و لبنان بر سر دو منطقه امنیتی برای راستی‌آزمایی و خلع سلاح حزب الله توافق کردند.
🔹
توافق با لبنان را به لطف ضربات مهلکی که به حزب‌الله وارد کردیم، به سرانجام رساندیم.…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/664022" target="_blank">📅 21:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
نتانیاهو: ما طرف قرارداد ایران و آمریکا نیستیم  نتانیاهو مدعی شد:
🔹
دولت لبنان برای اولین بار می‌گوید که خواهان صلح با اسرائیل است و این یک تغییر اساسی است. #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/664021" target="_blank">📅 21:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نتانیاهو: هر زمان که لازم باشد وارد خاک لبنان خواهیم شد و در آنجا با قدرت تمام عملیات انجام می‌دهیم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/664020" target="_blank">📅 21:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نتانیاهو: هر زمان که لازم باشد وارد خاک لبنان خواهیم شد و در آنجا با قدرت تمام عملیات انجام می‌دهیم
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/664019" target="_blank">📅 21:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/664018" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/664018" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/664017" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/664017" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b29a5b4f0.mp4?token=cF7_dREhepUueVsFHmyDdLp5vg9vxWVtSdawimkVSKJxBGjcQDUNh34qdkN8JZQ-VPdz6xz9pJQq4gM9KbpYbGSAE_SzXOJ3XEtsrgxDYtXoYQM7ITSGjNTuTZeGw29sambx8tLXgP_QUb2pcjO_UvqlfvRL8HnB0hZ2d_Dio8-mlzuf_NHAaGv1l7hAsAblIEwn23DIKym9ZpoP0NhV5M2UkDfPSt8FbbVekZZgDmYkFzlerkoJx_Cpd_ykzem0RmZjyuYSBSZ7jYrs-xr7hIhf4YcF42b9ZBRgo62qn4HgBRQHXhhKXcWvPX6Gqqk6LAmcu31iv3E4-b79EB_Maw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b29a5b4f0.mp4?token=cF7_dREhepUueVsFHmyDdLp5vg9vxWVtSdawimkVSKJxBGjcQDUNh34qdkN8JZQ-VPdz6xz9pJQq4gM9KbpYbGSAE_SzXOJ3XEtsrgxDYtXoYQM7ITSGjNTuTZeGw29sambx8tLXgP_QUb2pcjO_UvqlfvRL8HnB0hZ2d_Dio8-mlzuf_NHAaGv1l7hAsAblIEwn23DIKym9ZpoP0NhV5M2UkDfPSt8FbbVekZZgDmYkFzlerkoJx_Cpd_ykzem0RmZjyuYSBSZ7jYrs-xr7hIhf4YcF42b9ZBRgo62qn4HgBRQHXhhKXcWvPX6Gqqk6LAmcu31iv3E4-b79EB_Maw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند مهم و مفید برای سلامتی بدن
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/664016" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXymGruTvu9XBv0tw3SnjJLBiEmRKeaSu8xh9gtLi1Qd6X_X_yLKTFpYNX_8r7O2-26KaPtZJOKZYFeoDAq9BTWCpKo0Nq5Vu6miwKGeI7UqA67n_RCFxMYTRUlskihvtgIfyNhtBjMG_LnYJRngZBgz7jUPsRmkE43GYa6-7kgquO1mNligNMYoPfx9wRMpjtz7H3xyMp8Bs8f-PWRa2hpeS788KfuAlKLvFJvhcsUQ-Xwrw4ymzcCw3P2QMGTAk-3oS5Ni7sJ45bbPFhZk77y9u9J4oJwhS4wxm4Mrd3sbBWeF4Pr_6c4SQ7jF5GtqitENwS85xbANjZYT3Kltqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو در سایه سکوت خفت بار مقامات لبنانی، رسماً اشغال خاک لبنان را کلید زد
🔹
نخست‌وزیر رژیم صهیونیستی در یک کنفرانس خبری با نمایش نقشه‌ای از مناطق جنوب لبنان، مدعی شد با مقامات دولت لبنان درباره حضور و اشغال بخش‌هایی از خاک این کشور به توافق رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/664015" target="_blank">📅 21:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ونس مدعی شد: مذاکرات با ایران موفقیت‌آمیز بوده است
ادعای معاون رئیس‌جمهور آمریکا:
🔹
اگر با ایران به توافق نهایی برسیم، عالی می‌شود.
🔹
افزایش جریان نفت از طریق تنگه هرمز نشانه‌ای از وقوع یک اتفاق واقعی است، اما توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/664014" target="_blank">📅 21:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc606f8ae6.mp4?token=HeS1oXgg6dlZwDy8OZ-KHdcaDWc5tSMpHvsk0_N1OVqBYeh67QBPTOrioeqXQOR5AD5iLr3amFwge7CROIqCrTqF1DCFDhHYIRIKmoRPw0ecCpP-zMqjpPqhswf2xfNkU3HzEDmFr-NtWqhw7bUs1YuHdr9AzXARSvRyK5ZrlPH17M8zcQt87nRhMf-qmCKGvfY_qWlzWO8WH613uDLPzyiSvS9kKWGd9OmoE9Fxg0d0ol-scZCC8nb_0RivwBMJfYM3jI7wDVK9VnPijLvyUoMuV9FmVuSxDavpGegLY136dMLWyMAMy4jC3FRCttgNNjp0Ya9TzgaX25vGjHmin79VvmJ3gkmi0t87hMc57EYlKQb6QX8SHz6cZvA5Z90GyOSW4iJwL70c0WUZtYH7mKevgafFLnyVS3WRwROh5nRxDuXpfvqcITVyC-dANFLsK4Zm-uxmyA846atsRpBDv7puPvXc0eN0jUJCVURmQ9bFRLgaLylM7YGjbdyETs-LOnDJV0Ok4FcnW5FZ3cZuVNQqwRY7HE5Wam-JYk8Ae3-5CTqKvvZ4zokaYu9LzEdF_XCRp68HkjkttQjGgCqoDTPSG4vkns7MsODhdqccJjrBMArbo-KOB6Y0N4H_Tj8BR32MhLqHewtTxlrZL-VU4eIOvezEP2DV8e4M3v3FlcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc606f8ae6.mp4?token=HeS1oXgg6dlZwDy8OZ-KHdcaDWc5tSMpHvsk0_N1OVqBYeh67QBPTOrioeqXQOR5AD5iLr3amFwge7CROIqCrTqF1DCFDhHYIRIKmoRPw0ecCpP-zMqjpPqhswf2xfNkU3HzEDmFr-NtWqhw7bUs1YuHdr9AzXARSvRyK5ZrlPH17M8zcQt87nRhMf-qmCKGvfY_qWlzWO8WH613uDLPzyiSvS9kKWGd9OmoE9Fxg0d0ol-scZCC8nb_0RivwBMJfYM3jI7wDVK9VnPijLvyUoMuV9FmVuSxDavpGegLY136dMLWyMAMy4jC3FRCttgNNjp0Ya9TzgaX25vGjHmin79VvmJ3gkmi0t87hMc57EYlKQb6QX8SHz6cZvA5Z90GyOSW4iJwL70c0WUZtYH7mKevgafFLnyVS3WRwROh5nRxDuXpfvqcITVyC-dANFLsK4Zm-uxmyA846atsRpBDv7puPvXc0eN0jUJCVURmQ9bFRLgaLylM7YGjbdyETs-LOnDJV0Ok4FcnW5FZ3cZuVNQqwRY7HE5Wam-JYk8Ae3-5CTqKvvZ4zokaYu9LzEdF_XCRp68HkjkttQjGgCqoDTPSG4vkns7MsODhdqccJjrBMArbo-KOB6Y0N4H_Tj8BR32MhLqHewtTxlrZL-VU4eIOvezEP2DV8e4M3v3FlcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حفظ یکساله و دوساله قرآن کریم به صورت رایگان
✅
ویژه دختران و پسران۱۴ تا ۲۲
🔹
اعتکاف با قرآن در جوار حرم مطهر امام رضا علیه السلام
🔹
اطلاعات بیشتر در
👇
http://Samenoon.com
https://eitaa.com/samenalhojajj</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/664012" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ایرنا بررسی کرد؛ عدم پرداخت حق عائله‌مندی به همسران بازمانده تک‌نفره، ناشی از قانون است
🔹
عدم پرداخت حق عائله‌مندی به برخی همسران بازمانده تک‌نفره مستمری‌بگیر، این روزها به یکی از مطالبات مطرح‌شده از سوی این گروه تبدیل شده است.
بر اساس گزارش ایرنا، عدم پرداخت حق عائله‌مندی به همسران بازمانده تک‌نفره ناشی از چارچوب قانونی موجود است.
🔹
طبق اعلام سازمان تأمین اجتماعی، این سازمان صرفاً مجری قوانین است و تنها می‌تواند مزایایی را پرداخت کند که در قانون برای آن پیش‌بینی شده باشد. در قوانین فعلی، برای همسران بازمانده تک‌نفره تنها مستمری بازماندگان در نظر گرفته شده و کمک‌هزینه عائله‌مندی جزو این مزایا نیست.
🔹
بنابراین، در صورت طرح و تصویب اصلاحات قانونی، امکان بازنگری در این موضوع وجود خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/664010" target="_blank">📅 21:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtJp1jnohHmIswdUJ9N6PEOkKMmzUbeJb--d5yMNSX6GI7OVb7858DwaJ1tZnvmQ5pvSqyuB4xkjTuk5VshjdNIf-jyc_mZaRj8kWjpCaNKMphHT32XfXeZywgzVYZL1MNbNwkaMHTtc3WlQNa7-7tRwtxXMjuXy3Hfy-2MGPJmpOEoKMp6xGq5b3UU0jtKQxzjlRf89uve-RGt5th2FQ5xMZp22W3zxZJ4-P5citlR6yI0Qks18Jy2CZBEJsTQiqeScTyu2IUaPdbcxZZLCIAtPKQb_ziJoJq3vBv1L8kqqpbIcqgWm70gm3jJYOe3tXCHyMrctes39bllHFqC-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیز مرد شیعه برای شکست ترامپ و دار و دسته اش/ ممدانی، آماده جنگ با مرد مو زرد
🔹
جرات و شجاعت جمهوری خواهان در انتخابات 2016 سبب شد که ترامپ به قدرت برسد و حزب جمهوری خواه یک پوست اندازی مناسب کند. دموکرات ها از این پوست اندازی ترسیدند و به همین دلیل، انتخابات 2024 را هم علی رغم تمایل کمرنگ هریس به سوسیالیسم، باختند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226025</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/664008" target="_blank">📅 21:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c05CjH-u72dD8XGPrlfYrOfsP_mLyA9_eGk9NqKSUUYtUnyWQcQcEljOY18-wSNzuo7nt_Y0unx5K2IdGxV7x6B67ibU5HR6PI5FBXqIScwWXIN9gcI3hNd-OzivNUN_SPta-MuomyYeP50N2hJ2uVC8QXhKxQxOhWgYBd5ddqvJQG01f4ULLxDwzRXxJ5bf2XkU7YWAzZTOfJWUdrVPbX5rSrb-7-XDn7L2w4i3zcy3vWBTLCxO9lDeo1b81PSvVHFDFeISXsb-68-BWXgfV1ZTzUYzgG3x1AcrSzHxwdMYeJNJjLoMcwuQsLIaB43e9-v4L8c-GEZJnRv1GkT0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از استوک‌های جدید نایکی کریستیانو رونالدو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/664007" target="_blank">📅 21:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
۱۰۰۰ مدرسه تهران آماده اسکان زائران رهبر شهید  وزارت آموزش‌وپرورش:
🔹
بیش از هزار مدرسه در تهران برای اسکان زائران آماده شده است.
🔹
زائران بر اساس تقسیم‌بندی ستاد برگزاری مراسم به مراکز اسکان هدایت می‌شوند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/664006" target="_blank">📅 21:07 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
