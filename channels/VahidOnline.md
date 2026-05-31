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
<img src="https://cdn1.telesco.pe/file/SAKjmBPWcDMBRJAWrO3InXgFL8-Oaa3haHzAnvkxmFOi5-Bmf5FD_JmQAsG6C4qdUBzytqdMgCBPcdjIt_p0KJZM7T1xD3cL3tQ8K2jAifnu-KMt3MRZFRSoYvK5uwq7Xf6Vm4hkv-8HolVOBRL2t_1TsWXI03bH5S7kxHxDJft758usrHK8M5Ij35uEFv8CPMRfHbfUrZlTn-snljQ6VM3Nn9jxtWciMvfvaGGVEMKuFZLUI_---jD_1v4_-bOHUUr1M-dAT2Pp47tUW0HizE-3boh9ZZxyXLyN-jOr7OUV4OZqg4JzyyKv0q61MGBwC7TH6MnJp_MkJlMHWPSDzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 22:11:35</div>
<hr>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=jjE_JbUbFHSMbc7ZLSfRwmuxOLaToKpQqBGC1_dFOxKeYGz0chLHOhjp9w27EwtuqEWCJ9njBX8R9jkg5LXCjB6BRX06FSpVR-Dwn2KytUjkhNFY8yBh-mZIAzOjZs98a_-R5tmKxq_SM5y1pDkD0KS-y1DWlbP_SgioArrNJYDBY6UnY2WuxdTDYx-Z1QqsaoOIAIN0Ee81OHumXEUfpfFJ5Kq_em2i-6pVcMo4MM_8xec4AxVuM7uoq_DGKGdLzILSDKORomOEytZl2M7IrrQCdB4pe5CkmOzH1LFa0Z-RVq_Xrezhr6_aD9__MwuU6ItVdeoZRr5UU_Rg5oyFsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=jjE_JbUbFHSMbc7ZLSfRwmuxOLaToKpQqBGC1_dFOxKeYGz0chLHOhjp9w27EwtuqEWCJ9njBX8R9jkg5LXCjB6BRX06FSpVR-Dwn2KytUjkhNFY8yBh-mZIAzOjZs98a_-R5tmKxq_SM5y1pDkD0KS-y1DWlbP_SgioArrNJYDBY6UnY2WuxdTDYx-Z1QqsaoOIAIN0Ee81OHumXEUfpfFJ5Kq_em2i-6pVcMo4MM_8xec4AxVuM7uoq_DGKGdLzILSDKORomOEytZl2M7IrrQCdB4pe5CkmOzH1LFa0Z-RVq_Xrezhr6_aD9__MwuU6ItVdeoZRr5UU_Rg5oyFsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی، در واکنش به گزارش شبکه ایران اینترنشنال درباره استعفای مسعود پزشکیان، رییس دولت، این خبر را تکذیب کرد و آن را «شایعه‌سازی» خواند.
شبکه ایران اینترنشنال، ساعاتی پیش در گزارشی اعلام کرد مسعود پزشکیان در نامه‌ای رسمی به دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خواستار کناره‌گیری از سمت خود شده است. این رسانه همچنین نوشت در این نامه به وجود اختلافات ساختاری در اداره کشور و نقش نهادهای نظامی در تصمیم‌گیری‌های کلان اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/VahidOnline/75823" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mWFlQs04vZ9IyS1ElfHGtorzRgw7og9XXEOgQycMHXWw6w942GcFZdIIg_p9Q6KY4yxlIGF1SDZGQvq7whubGnwEbjKpbdwRseRSbuJlDaR-k3ivdKD-6b10yNXeaqveUGLaEZ5pyjaPxvy8zx5lA5wJZral5cVhGBmfRclG5vd3hkQcUbM74AtztyaIKivElInHMGNjiJ3mloeVce2-wRLUrxssa-eP1kSlbR5rO_R2Rk-MwdYpG8aoF50otusLsfwSfA65qM7rDdEdpq064mtmPWrW7fgJPLU75Q7eNQ5940eMXvT1nKNexGztQ4u8_76Lw1MtHQbsdCT8if92Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75822" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9QccuOXyeOdOlzJ-d1UYJ_3l6FvKI5F8M1qtVzig6G36XcQmV3ghxRcp6gEBoqTNZy-0x8y38LNdz80K6yEYVgKfJZG5flPJrWiZTrktQYU1qyfDLInCgeU8txjnQkBuy2W2MnhCV4TMlvfzSuTRg6DDJgPY4Pt7AGvN2mWKm_AipaDTnbK0s0OjY0bOgfIhWKTz8xXWHfADFOSFEO-tht_EOScUDuhjw5D4rbsxg2P6APYpCMaafNPVhDlIbhBt_5S-JZGJLA7mJXsdhSAZqZkuxt8ZaJ8dMqDvuu1FCB9XiJ4qPJVPpNI8VgKGg1lgiv9piFZeyUxbFyvKZyNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پیاهو، مردی که تصویر معترض نشسته مقابل نیروهای پلیس یگان ویژه در مقابل پاساژ علاالدین در آغاز اعتراضات دی ماه سال گذشته را منتشر کرد،
به گفته وکیلش
به ۱۰ سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75821" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6220710705.mp4?token=nES6ZRux82sOIw1Fqqd0KtAmXrFRHm_02otW965giuPL9B7x0QyUHVbyaR1FbU-EGa-hbVSudk8jcOscj26VZGWsPLPmaVcdFOoXAeYZWNuZzbOfy-XKgDkcHvnSVeZ8grf5pVpbU8Sr8w1M3nYkit260YDYvhTDfUo8mCJr-cd_pJpW8e58sPEufQPelwlcb-CfxF_N26GeKXrhMTiTbnvfiBQr4UDUnmBwnarWPUaTGPPrXbx_bwb6skompyODE7m2ReaSIJoarzynHYO3xfb5TTCaO0_gHwvsZKkMQTbX-Brw1rWNAxIBYcVeUvPyZpre5TQ8PsgJOps8sRXYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6220710705.mp4?token=nES6ZRux82sOIw1Fqqd0KtAmXrFRHm_02otW965giuPL9B7x0QyUHVbyaR1FbU-EGa-hbVSudk8jcOscj26VZGWsPLPmaVcdFOoXAeYZWNuZzbOfy-XKgDkcHvnSVeZ8grf5pVpbU8Sr8w1M3nYkit260YDYvhTDfUo8mCJr-cd_pJpW8e58sPEufQPelwlcb-CfxF_N26GeKXrhMTiTbnvfiBQr4UDUnmBwnarWPUaTGPPrXbx_bwb6skompyODE7m2ReaSIJoarzynHYO3xfb5TTCaO0_gHwvsZKkMQTbX-Brw1rWNAxIBYcVeUvPyZpre5TQ8PsgJOps8sRXYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با فاکس‌نیوز درباره ایران اعلام کرد: لایه اول و دوم حکومت آن‌ها از بین رفته و اکنون با لایه سوم روبه‌رو هستیم. شاید آن‌ها دیده‌اند برای بقیه چه اتفاقی افتاد و می‌بینند ترامپ آماده انجام چه اقداماتی است.
بسنت افزود: اگر ترامپ با این توافق موافقت کند، همین حالا به رهبران جمهوری اسلامی می‌گویم که او این توافق را هم از نظر نظامی و هم از نظر اقتصادی اجرا خواهد کرد. آزادی کشتیرانی در خلیج فارس از طریق تنگه هرمز باید به وضعیت پیشین بازگردد.
او درباره اینکه آیا ترامپ «کار را تمام خواهد کرد» گفت: اگر «تمام کردن کار» یعنی اطمینان از باز بودن تنگه هرمز، در اختیار گرفتن اورانیوم با غنای بالا و نداشتن سلاح هسته‌ای از سوی جمهوری اسلامی، پس کار تمام شده است.
بسنت تاکید کرد: چه از طریق مداخله نظامی، چه محاصره یا فشار اقتصادی، این نخستین بار در ۴۷ سال گذشته است که ایرانی‌ها درباره نداشتن سلاح هسته‌ای گفت‌وگو می‌کنند. این موضوع پیش‌تر ممنوعه بود و اکنون برای نخستین بار روی میز مذاکره قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75820" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهمند عليپور Farahmand Alipour</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=YR3G044eDjK6AdMoo9BAVUbvtjuLkztaf0ler7ZPxkMduVt5SxvLjdU0-Rtzfg4d4BkQGsOXzNzaZ4Drdwz1WUxSBC0Te8sIlR_IoescJcAgVvV4jV69sSQ56Fw5ypHz6eaTeRkrjFbckC4FDJgiFrCiq-xeTG9n1HUm53k_cz2seRwVgfHy3cYt0hiPbI5tCovhLcpCT3JdpsjnnDrQK58UbCO72Ww2mZHODdetG-r6qfByrT9UZTE9nX7g1LZKHAuMmqg6Pz3QvpMFwZOBcxNmxo5PH4Ta6-8WZ9KkKHGHjnbcNaXB_xCh0jPyWayZGhZy_Mdg_bI5Rz4Cfppw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=YR3G044eDjK6AdMoo9BAVUbvtjuLkztaf0ler7ZPxkMduVt5SxvLjdU0-Rtzfg4d4BkQGsOXzNzaZ4Drdwz1WUxSBC0Te8sIlR_IoescJcAgVvV4jV69sSQ56Fw5ypHz6eaTeRkrjFbckC4FDJgiFrCiq-xeTG9n1HUm53k_cz2seRwVgfHy3cYt0hiPbI5tCovhLcpCT3JdpsjnnDrQK58UbCO72Ww2mZHODdetG-r6qfByrT9UZTE9nX7g1LZKHAuMmqg6Pz3QvpMFwZOBcxNmxo5PH4Ta6-8WZ9KkKHGHjnbcNaXB_xCh0jPyWayZGhZy_Mdg_bI5Rz4Cfppw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴
در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته
«دو گزینه بیشتر نیست»
یا جنگ و خونریزی یا مذاکره مستقیم
«برای از بین بردن غنی‌سازی و موشکی»
این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات آمریکا و جمهوری اسلامی همچنان همون چیزهایی بودند که باعث یک جنگ شد، و این مصاحبه یک ماه پیش از آن بود که دست به قتل‌عام مردم در خیابان‌ها بزنید!
الان هم محور مذاکرات کاملا مشخصه!
همون چیزهایی است که جنگ ۱۲ روزه رو رقم زد. همون چیزهایی است که در آبان ماه عراقچی در تلویزیون گفت.
خون تک‌تک ایرانیان از جمله کودکان میناب پای شماست! شما طرف مذاکره بودید، شما انتخاب کننده و تصمیم گیر بودید.
و شما بین اورانیوم و موشک، و یا جان مردم، زیرساخت‌های کشور، فولاد و پتروشیمی و…
اورانیوم و موشک و دشمنی با اسرائیل و آمریکا رو انتخاب کردید! هنوز هم طرف مذاکره و تصمیم‌گیر شما هستید! و‌ جنگ ‌از سر گرفته بشه باز تصمیم و انتخاب شماست و مقصر شما هستید!
نمی‌توانید پشت کودکان میناب قایم بشید و از کشتار دیماه فرار کنید!
هر خون و ‌هر ویرانی ، همه پای شماست.</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/75819" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8rx0iTw4cssqahePG7fK3f9DcUY6XccNpf8qEfZRDQfF1Hqa-zfjE1alOzFd3QrxG81X4eYf5YKW2wN94FYQSJP3U7_R14FylV-kyCFXRk1M_zLQEPC8587x-3C_nitHrqBu5P3oZ1gw4DEPwxzLDHQdA3fJtyeIOgeaj2tc64DyuKZ0KoPHhCx5Nj9X1GVM41_aGh_kFwgG0g7PdtubyhXcZfhUVgEoy2OoCMl2gkfxcZoSQCkr_2lOCGd0cAQOVoGzJZeV4xnnr1ggPTdGAHlpHJdsRevaqsOXoDkrwKBHxsCyMzoylp4MnWcST1MEUmfc-bzp-P8BG0vGHzdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن و حسین امیری، دو برادر دوقلوی ۲۰ ساله محبوس در زندان قزلحصار کرج، از سوی شعبه ۲۶ دادگاه انقلاب تهران به ریاست قاضی ایمان افشاری به اعدام محکوم شدند.
بر اساس اطلاعات دریافتی هرانا، مبنای صدور این رای اتهام «جاسوسی برای اسراییل» عنوان شده است.
یک منبع مطلع در گفت‌وگو با هرانا اعلام کرد در کیفرخواست صادرشده علیه حسن و حسین امیری، مشاهده تصاویری از ساختمان‌های آسیب‌دیده به عنوان مستند اتهام «جاسوسی به نفع اسراییل» مورد استناد قرار گرفته است.
این منبع همچنین گفت: «حسن و حسین امیری به دستور بازپرس پرونده به صورت جداگانه در زندان قزلحصار نگهداری می‌شوند و از حق ملاقات با یکدیگر محروم هستند. این دو زندانی در حال حاضر در سوییت ۳۵ این زندان محبوس هستند.»
بر اساس این گزارش، این دو برادر پیشتر در یکی از ایست‌های بازرسی و پس از بررسی تلفن همراهشان بازداشت شدند.آن‌ها پس از بازداشت، به مدت دو ماه در وضعیت بلاتکلیف در زندان قزلحصار کرج نگهداری شدند.
👈
حسن و حسین امیری از دو سالگی در مراکز بهزیستی پرورش یافته‌اند و خانواده‌ای برای پیگیری وضعیت قضایی و حقوقی خود ندارند. به گفته آشنایان این دو جوان، نبود حامی خانوادگی بر نگرانی‌ها درباره روند رسیدگی به پرونده آنان افزوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/75818" target="_blank">📅 18:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6xKN3YRm2Zv-57FT2RJWjQ6ydKQagpgTWTwRLlbJD8O8oWvapVUrb8xoX3Ouf_p_Xu3WwHrZN_dchC8PCz3q8DMAbjaojOwEQVX4LWgB9okBZQRLMpxEg4-JWHhNrS3DFint_NfWTlzZLV5Qn85rES7C-Gi49rsRjaMKUzKXP9cXfkMt4larJruWWsHa4T8_ePJg0kBqTj0-uVoCti8HsmDBMc0_lci39sCkuWYTJVJ0A0mlzB_egaXBw9MhLo_MLVhRg9F98lU5kJKtL4XSbIg-Vs-EtftNHIfrFfzc1R1P7Y1Kk45aHl5c93u2OYH5CQ02nWDTxUOJzWLHKUa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران چندین ورودی تأسیسات موشکی زیرزمینی خود را بازگشایی کرده است
شبکه خبری سی‌ان‌ان روز یکشنبه ۱۰ خرداد با استناد به تصاویر ماهواره‌ای اعلام کرد ایران توانسته از زمان توقف جنگ شماری از زرادخانه‌های موشکی مدفون خود بر اثر حملات هوایی آمریکا و اسرائیل را از زیر خاک بیرون بیاورد.
حملات آمریکا و اسرائیل با تخریب جاده‌ها و مسدود کردن ورودی تونل‌ها، دسترسی ایران به پایگاه‌های موشکی زیرزمینی را محدود کرده بود.
سی‌ان‌ان ادعا کرده است که ایران تاکنون ۵۰ مورد از ۶۹ ورودی تونلی را که در ۱۸ تأسیسات موشکی زیرزمینی توسط آمریکا و اسرائیل هدف قرار گرفته بودند، بازگشایی کرده است، از جمله در پایگاه‌هایی در خارج از اصفهان و در اطراف خمین.
بر اساس گزارش این شبکه خبری، ایران همچنین بخش‌های دیگری از این پایگاه‌ها را نیز ترمیم کرده است؛ از جمله جاده‌هایی که آمریکا و اسرائیل برای جلوگیری از تردد پرتابگرهای موشکی بمباران کرده بودند. تصاویر ماهواره‌ای نشان می‌دهند که تقریباً تمامی گودال‌های ناشی از بمباران اکنون پر شده‌اند و در دو پایگاه، این جاده‌ها حتی دوباره آسفالت شده‌اند.
ایران شبکه پایگاه‌های زیرزمینی خود را در عمق خاک و در مواردی زیر کوه‌ها ساخته است تا در برابر حملات هوایی مصون باشند، به همین دلیل آمریکا و اسرائیل بسیاری از ورودی‌های این تأسیسات را بمباران کردند؛ اقدامی که در کنار تلاش برای شناسایی و نابود کردن پرتابگرهای موشکی، باعث شد توان ایران برای شلیک موشک به‌طور قابل توجهی محدود شود.
این حملات خسارت سنگینی به پایگاه‌ها وارد کرد؛ به‌گونه‌ای که بیشتر ورودی‌های تونل‌ها زیر حجم عظیمی از آوار مدفون شدند و جاده‌های منتهی به این سایت‌ها نیز به‌شدت تخریب شدند.
سی‌ان‌ان می‌گوید باز کردن ورودی تأسیسات موشکی زیرزمینی می‌تواند به ایران این قابلیت را دهد که در صورت وقوع دور جدیدی از درگیری‌ها، موشک‌های بالستیک بیشتری نسبت به اواخر جنگ ۴۰ روزه به سمت اسرائیل و کشورهای دیگر شلیک کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/75817" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C75a8REshYwZkyASCvJR8NZjTxBM6D9L7ADwoYzWuCvjmU8B6eZjYs5YT4RI7ZvRQc3zv_2k6uwhP6M-kWV86MsAKYFmzujX-EW3ul-SJicF8WFTDD9cz5bP2wjAYIltWIOSl5ZGHmJJGNpNA0-umbi-dj6GIRogQm6I3Okfo6jXQRyokKsT8leZvcD0zSZpJwKGLa59PVm-mQONzHoGK3xOpbFUBZq-S-m3koKxAOV-dThGQnjAjbJ-mAp6klHMBW0tvki52B91KD0iPzXqOyRIZ1ZKE-LHZLpkFkSiFTvK4T_emL1-vgQC--1l4b4fBLwji6N94H5KZ6Zb-ia2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس مصوبه جدید شورای شهر تهران، هزینه خدمات مرتبط با خاکسپاری در بهشت‌زهرا به‌طور میانگین حدود ۴۰ درصد افزایش یافته و در برخی موارد رشد تعرفه‌ها به ۵۰ درصد رسیده است.
روزنامه دنیای اقتصاد گزارش داد نرخ خدماتی از جمله حمل متوفی، تغسیل، تکفین، تدفین و برگزاری مراسم افزایش یافته است. بر اساس این مصوبه، هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری ۵۰ درصد افزایش داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75816" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CshAQo1Ho8OYNtQbQBQbYSh2dVxxWYWeRzVoUnFgJEYu_cfL-YQ6TRKDVoC7UHIjwiTTafaug0P07-XPEnBHKjD3q8iNAtGdTgrKm1vdmuNqrVHl08V0u7d_lAhy5kYUBZe00rnjsswfAKjEfsMmW-6x3bYwQWf5hMnft7naGNYNZqO16YTdKECfe8-R6LdgrVGyoU5YU6gd53DMTo6vpu0SnjZQuSz6uYSbhA6YQlMKqjVe5uovIw8BD2Z-a1a_qwQTWzYCcZ4AOSz6rRiCfD7QKmNl4TLk8h0pS5TXoVRtvPga-hQgtZ6iI1MrAzS11NTpgu4aG-ik7fTaw8pb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد زهرا شهباز طبری، زندانی سیاسی محبوس در زندان لاکان رشت، پس از نقض حکم پیشین در دیوان عالی کشور، بار دیگر از سوی شعبه دوم دادگاه انقلاب رشت به ریاست محمدعلی درویش‌گفتار، به اتهام «بغی از طریق عضویت و فعالیت در سازمان مجاهدین خلق» به اعدام محکوم شد.
این زندانی سیاسی ۶۸ ساله، در فروردین ۱۴۰۴ در منزل شخصی خود در رشت بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75815" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHWkEFK5dtRALD2XETRZpmYpcPf8XI7d4962mz_mUwHCHxu37HS4qGAdfJ-EQBPD0xKXJH2scmMw3MLkGpNdc9GjgNGdd5r4KDvq9qPdAP3XLdVaZTNX1W_uuwxbHLf0vDRe4cyaY5_c6zD6ijH3RI6exZCvBH547VpD_JXJ38f2QWiQkkxXVAv2g_OXEmOpqAt0teA_s2dbo7-7QCpo17AKdU8KktvWwb8Qpfhtnb8LgeA2QrlSKpunQyLHI2h-up1IHL7kD2XuhToIc0NzqKjLEdCq1c4GspafXlmWrN0k7YSqf5796jLjuApkpi83F5Vi-icnOrwS58Vy3BclrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز یک‌شنبه اعلام کرد‌ «طی شبانه‌روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینربَر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.»
ساعتی پیشتر روزنامه اسرائیلی «اسرائیل هیوم» نوشته بود که ده‌ها نفتکش حامل نفت و گاز طبیعی مایع در هفتهٔ گذشته با اجازه آمریکا و پرداخت عوارض به ایران از تنگهٔ هرمز عبور کرده‌اند.
این در حالی است که دولت آمریکا بارها اعلام کرده است با پرداخت عوارض به ایران برای عبور از تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/75814" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sf6FM1H8oa9FTeMaLgnUazc6lOhRWrmk7cSh6XQhOABjzbS7ar_MZ8JDPFmuj5lkVWS6YkINvrQOa-FVSLSfqrlkTmI3kkOAzwQTeuPDNWpt-uSOPBiWhD0qoCY-f15QsxO-VqggPNAW64p6-7XoOWnRO5k5VFLIJRV7aQDwfZ58PCIxLpCVZAhTHyXRRy8xxUWdYsuAjQxLP9oYfqnpJWO463T82nDSLSH8reHJF2tf8y8wY8-g-3W9IogoUuKWk-rw0W20iPBd1tYYn0gTu6qOtvJUsjVgRHdAwgWv7j0wk31nOpHZGl1cMzwgCX6XyoR1k1U7Kl3Q1qLNMQJQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=Ke-Ra8THEpqDoYznPgYi7Yy5JYb91Ekr51K7Y82S4r2EIlDrCNJXMhciabP0V1LCGVQf8oMOe1LS02XkG9A2pxm3MfFfVzqnVOo0gDKvBs2zPBL5XKaoBb3qNDvMxs__Y_TUwPlAV9ilz2P8Cgfz5kjSZ5FYy4c8hoL5Xwy1uCsC67qYO4DAP1UuqrE97WK0YHRyZevKoQ2z4GaxziTfQu8Gpm-_EAZvwemGgQ1DkumFrxZ-1E9jisamwAeJhYwIss45ZCAfFPOQFq8_8REMOcZ7Y-tSvKTxIPkIudRFx0Dva8UGEdbYg3vXBTKHlN5XAxTsj-fKqLPyW0b7OjB8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=Ke-Ra8THEpqDoYznPgYi7Yy5JYb91Ekr51K7Y82S4r2EIlDrCNJXMhciabP0V1LCGVQf8oMOe1LS02XkG9A2pxm3MfFfVzqnVOo0gDKvBs2zPBL5XKaoBb3qNDvMxs__Y_TUwPlAV9ilz2P8Cgfz5kjSZ5FYy4c8hoL5Xwy1uCsC67qYO4DAP1UuqrE97WK0YHRyZevKoQ2z4GaxziTfQu8Gpm-_EAZvwemGgQ1DkumFrxZ-1E9jisamwAeJhYwIss45ZCAfFPOQFq8_8REMOcZ7Y-tSvKTxIPkIudRFx0Dva8UGEdbYg3vXBTKHlN5XAxTsj-fKqLPyW0b7OjB8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه مجازی صحن مجلس شورای اسلامی به ریاست محمدباقر قالیباف و مشارکت آنلاین ۱۸۷ نماینده و حضور ۱۴ نماینده برگزار شد.
در این جلسه که اولین جلسه از سومین سال مجلس دوازدهم بود، اعضای جدید هیئت رئیسه مجلس سوگند یاد کردند.
جلسه روز یک‌شنبه، دهم خردادماه، همچون جلسات معدود گذشته در مکانی مخفی برگزار شد.
محمدباقر قالیباف در همین جلسه تأکید کرد که «تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی تأیید نمی‌شود».
قالیباف که از او به عنوان رئیس هیئت مذاکره‌کننده ایران نیز یاد می‌شود در این جلسه بیانیه‌ای را قرائت کرد و در آن ادعا کرد که «در حال عقب نشاندن دشمن در یک جنگ تاریخ‌ساز هستیم».
@
VahidHeadline
محمدباقر قالیباف، رییس مجلس شورای اسلامی گفت: «سومین سال مجلس دوازدهم را در حالی آغاز می‌کنیم که یاد و خاطره رهبر شهید با ماست و هنوز فقدان رهبر و پدر امت را باور نمی‌کنیم.»
او ادامه داد: «رهبرمان به ما آموخت مقابل زورگویی و تهدید، ذره‌ای سر خم نکنیم و با مشت‌های گره کرده مقابل خصم تا آخرین قطره خون مبارزه کنیم.»
قالیباف اضافه کرد: «دیدن جای خالی رهبری برایمان جانکاه است، ولی دلگرم به مدیریت و رهبری جدید هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75812" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4GxOvL0wLf2-zaR4SbkjVulpWHnnw94b_YgO9EPcL6OOnoiXW12cJVuzCe03_Eqo8nvTj8CGympvVlN_i2DacIQyVblUKgx4k1YfwkirmW20Gh6G6ATru-PhT1e08Va5eBu394-Gk4DBH6Gi-fHB5RVEZu1R5VLkWJ43LTfSHic25OAqi-Q4xvWLpUGmdANec8mVWKAiZ8NAb7wfohZAQkmRyDpwDxihZVe0neSg8V_OeOBjvvT80L3AUhMQ_FcbRl7nnEGccxZs8FhzYUfOwmc2RJ3TpsbmPtmTHH2UakReQSHh2eiYg9XId5ysI4fW-rotfTjAMp6HrNBh5-nag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=jKWrQUHo5GEYy_YPo4I4FMKz85ieK06oJVk7FQB90MIYvnYEt_Y0oxxWA7TxlLudANwSIqcg8BIWCFzGzRV-XIVP7UHEnc9HyO-jP0cB75iow-hkqtoW7kPL-NQsRtq4u1nNIFDL6d3GTb-y5ZLE9I78VZCspWSb0NlxcGKcy4Bcb8nRiJ_DAXnAF9I0lnCgqu5MfWY2fZWoqhre7PROVu81OiolahzwJd_Wc__xvajiUeg5RxbeqDWHyaDyrL-donNpBcDTD51pxqnlMr78QpX3QI6Cs4LK3--6DVdKIfbRdGMKkHbKwFsm-g4ut-Zd9lGyGVDaUs0VNb_dE61msQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=jKWrQUHo5GEYy_YPo4I4FMKz85ieK06oJVk7FQB90MIYvnYEt_Y0oxxWA7TxlLudANwSIqcg8BIWCFzGzRV-XIVP7UHEnc9HyO-jP0cB75iow-hkqtoW7kPL-NQsRtq4u1nNIFDL6d3GTb-y5ZLE9I78VZCspWSb0NlxcGKcy4Bcb8nRiJ_DAXnAF9I0lnCgqu5MfWY2fZWoqhre7PROVu81OiolahzwJd_Wc__xvajiUeg5RxbeqDWHyaDyrL-donNpBcDTD51pxqnlMr78QpX3QI6Cs4LK3--6DVdKIfbRdGMKkHbKwFsm-g4ut-Zd9lGyGVDaUs0VNb_dE61msQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی انتظامی تهران کافه‌ای در خیابان ولیعصر را که در آن برنامه‌های موسیقی اجرا می‌شد، به بهانه آن چه «فعالیت‌های مروج فرقه‌های انحرافی» خواند، پلمب کرد.
مرکز اطلاع‌رسانی پلیس جمهوری اسلامی در اطلاعیه‌ای نوشت: «این کافه با برگزاری برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار، و آنچه که ماموران توصیف کرده‌اند "تحرکات شیطانی" فراهم آورده بود.»
نیروی انتظامی جمهوری اسلامی نام این کافه را ذکر نکرد اما ادعا کرد که «مشتریان این کافه، شامل دختران و پسران جوان، در وضعیتی غیرطبیعی و با حرکاتی عجیب و غریب، که از آن به عنوان “شیطانی” یاد شده، مشاهده گردیدند.»
پیشتر نیز بسیاری از کافه‌ها و اماکن کسب و کار به اتهام‌های مشابه پلمب شده‌ بودند اما جمهوری اسلامی سرکوب‌ شهروندان را از زمان اعتراضات دی‌ماه گذشته تاکنون شدت بیشتری داده است.
موج تازه اعدام‌ها، صدور احکام سنگین و بازداشت‌ها نگرانی فعالان و نهادهای حقوق بشری را برانگیخته است.
@
VahidHeadline
ویدیوی بالا رو هم به عنوان "تحرکات شیطانی" در اون کافه منتشر کردند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75810" target="_blank">📅 15:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYlL1f8tW1JnXpNCOGRyC28BBWh-j6cncpm81_A7u181IJyTCduQGeiXf4XIkYlJfWqk-fjomvniteFDQWtxk8_TKgZimeMhQvOjmkpF8rCdtpbUH_b7S18iqbk_vWGodqCqB4_DRdNZbenA6BADuVQ5gqUp372kWVlQ6_Hn_C-oxwgnukwiEwTTD2DwiN4wULy8wl1dHLpvETkL_QTspexVTjV2AL8QRgJNllwdDJpoBY0H8xIyGxXKPtQ1ls2MpeGeXzzd5_nTxDBdfyMVD3m3RimlqraIwZ01DHUdN0OIsg2m221AMWfqmI17mtvWwj62dEgSAPrdkAoSPuHRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس، ترجمه ماشین:
رئیس‌جمهور ترامپ در جلسه‌ای که روز جمعه در اتاق وضعیت برگزار شد، خواستار چند اصلاح در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن رسیده بودند؛ این را یک مقام ارشد دولت و منبع دومی که در جریان موضوع قرار گرفته بود، گفته‌اند.
...
مقام‌های ایرانی به رسانه‌های دولتی گفتند که آن‌ها نیز متن نهایی را تأیید نکرده‌اند؛ هرچند دو مقام آمریکایی پیش‌تر در طول هفته مدعی شده بودند که تهران آماده امضاست و همه چیز به تصمیم ترامپ بستگی دارد.
به گفته این دو منبع، ترامپ از تیم خود خواست تغییراتی در پیش‌نویس مربوط به بندهای برنامه هسته‌ای ایران ایجاد کنند.
در شکل فعلی، این تفاهم‌نامه شامل تعهد ایران به دنبال نکردن سلاح هسته‌ای است، اما امتیاز مشخص دیگری فراتر از آن در آن نیامده است.
در این متن آمده است که یک بازه ۶۰ روزه برای مذاکره درباره تعهدات هسته‌ای ایران و کاهش تحریم‌ها از سوی آمریکا وجود خواهد داشت؛ نخستین موضوعات در دستور کار نیز چگونگی تعیین تکلیف ذخایر اورانیوم غنی‌شده ایران و محدود کردن غنی‌سازی بیشتر خواهد بود.
ترامپ می‌خواهد تلاش کند این بخش را اصلاح کند.
یک مقام ارشد دولت گفت: «موضوع، جزئیات بیشتر درباره این است که آمریکا چگونه مواد را دریافت می‌کند و زمان‌بندی آن چگونه خواهد بود»؛ منظور او اورانیوم غنی‌شده بود.
منبع دوم گفت ترامپ همچنین می‌خواهد برخی از عبارت‌ها درباره بازگشایی تنگه هرمز را اصلاح کند.
این مقام آمریکایی گفت به ترامپ گفته شده است حدود سه روز طول می‌کشد تا ایرانی‌ها با پاسخ برگردند. این مقام ارشد دولت گفت: «آن‌ها عملا در غارها هستند و از ایمیل استفاده نمی‌کنند.»
این مقام ارشد دولت گفت: «توافقی در کار خواهد بود. اینکه چقدر قریب‌الوقوع است، باید دید. ما حاضریم صبر کنیم تا رئیس‌جمهور آنچه را خواسته به دست بیاورد. ممکن است یک هفته طول بکشد. ممکن است کمتر باشد. ممکن است بیشتر باشد. امیدواریم در آغاز هفته چیزی داشته باشیم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75809" target="_blank">📅 05:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek3RvOYMTzB0GmtIEVUuqub6OyyueYNwFR7tGMNJSfkLvtPUb2eF7QffoR0SEvNo6nxXmo-ayoAm6Ex6ttGI6XTD-j3SV2tSZt4dW7pJgKxvxsaw0_9KTSfCy16zLqwWNtzwR2hfYThUxw9RxT8Xpwg7DPO4b7_Ds3i5ZFu-z4OOyXRsf-uIKCDPC5bavvVAh4JVkyw85b_ckH7g2oJbu4_46a8v90BWVod1niX4IJ6UtwAPn5AcJvQUabBebGy2T8G3aQrSYbmKIBkJDRFpi1h_BS4eveJWH0GCjn_gf8hmENXM3kTjxyhSzrmd4_IdEpYH3crY_ptrKSCcESEN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی سپاه بامداد یکشنبه، ۱۰ خردادماه، اعلام کرد یک پهپاد «ام‌کیو۱» (MQ1) ارتش آمریکا را منهدم کرده است.
خبرگزاری فارس نوشت: «این پهپاد با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت که بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75808" target="_blank">📅 04:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctvg9oKHcfYdYF_GTtdDJv85_b--lajgdGgbPY_ML4tDTxOgE2S18zPFgXOrIbgz8iUHE-WeHdI_kgOqwdkcLIeZK4_BTDRYGcmOfwktsxOEly950eZaiVAZrFneRUgWo6G07Cbf-DJ_IMNPTQ4KnjIy2DQ2HZ7zeQ54tzFCpsUy2njsTA2Ikn3rzAntpua26g_CHVn4fJ5zEW8tq0dX1wui7O1d6T4LFDi5i-4L3dPzCa8vugWLes3ACE_CBQe6DI9Vqm2rGJiy0vHZoWeD_TazixPp3E811djvCHlz8WKbyljAzQoK2kUb-EGFBsEWb6e3vVCzqcxWHAytEGGy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، اعلام کرد نیروهای این کشور یک کشتی تجاری با پرچم گامبیا را که به گفته واشینگتن در نقض محاصره دریایی به سمت یکی از بنادر ایران در حرکت بود، در خلیج عمان هدف قرار داده و از ادامه مسیر آن جلوگیری کرده‌اند.
سنتکام روز شنبه نهم خرداد در بیانیه‌ای گفت نیروهای آمریکایی روز هشتم خرداد کشتی «لیان استار» را هنگام حرکت در آب‌های بین‌المللی به سوی یکی از بنادر ایران شناسایی کردند و بیش از ۲۰ بار به خدمه آن هشدار دادند.
به گفته این نهاد نظامی، پس از آنکه خدمه کشتی به هشدارها توجه نکردند، یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت.
سنتکام افزود این کشتی دیگر به سمت ایران در حرکت نیست.
در این بیانیه آمده است که از زمان اجرای محاصره دریایی علیه ایران، نیروهای آمریکایی پنج کشتی تجاری را از کار انداخته و ۱۱۶ کشتی دیگر را وادار به تغییر مسیر کرده‌اند.
سنتکام جزئیات بیشتری درباره محموله کشتی یا مقصد دقیق آن در ایران ارائه نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/75807" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0XMchXGFZauoHhGUuSdcRYMTF7RDi1qTtRXBQTil9vZ3-qbKgp8QyvZZ1kUUt_ugC2-NDlO0GvYodgoj16HtugdzouOnDU_CXuB7r_3yy50UoW0QzlFiEhqMMWD-xATcPz4IjvPXjHrG7J_eJnHPZpwk7HoKMDBU5dh73lsXV2WtQ1EaA99NN-tpamrkPAYjBfTwTE4w3_KhS6XIuJhf3see_Qy2EecbR_exeCYz-OdtNozRegSH0yHdn9mU3y3BJeyYkt159a9EITCzCYyUI0AR6bfzjfy8pWXSAcLUJsTYFJu7hWj9JZlPmQRL9qOiacVxuU0BfSVbJXP-nOvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی در گزارشی درباره تفاهم احتمالی بین تهران و واشینگتن با عنوان «جزئیات غیررسمی»، اعلام کرد آمریکا متعهد شده در طول ۶۰ روز امکان دسترسی جمهوری اسلامی به ۱۲ میلیارد دلار از دارایی‌ها را به‌گونه‌ای فراهم کند که این منابع قابلیت انتقال و هزینه‌کرد در بانک‌های مقصد را بدون محدودیت داشته باشد.
این گزارش افزود که بر اساس این تفاهم، جمهوری اسلامی مرجع انحصاری تشخیص ماهیت شناورهای عبوری است و هر شناوری که محموله آن تهدیدآمیز شناخته شود یا بهره‌بردار نهایی آن در «خصومت» با جمهوری اسلامی باشد، به عنوان کشتی تجاری شناخته نشده و اجازه عبور از مسیرهای تعریف‌شده را ندارد.
صدا و سیما تاکید کرد که این رونوشت هنوز در حکم یک تفاهم غیررسمی است چون مسیر آن همچنان در چرخه بررسی، مذاکره و بازبینی قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/75806" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdmK4GkqOdX6guIWd9bOJTcJdwHki5tn4xNFF-F3PZIJvsZfANI0-MIFbuqeE9Qz2w41Bx1imPcDCtdzoIqojLcZx1Hhuvrb1T2qp2Hd2EviZOEEcLkiDfvP-URnmA2IWZ0IvNHmtqT-MMOXU9EjKlDklP2actG4_FUE6mEobExUQ4PtD3rNWClB2R0hGx-Q4tTrsM5rjlusW1NUCN4LKpXsOrgoEiz1bx0oqi-ei7PQOUn49EHnfCgrthR0YRUZiBzhwjfIBBV9F58cneHi0XkKSwUB4gDQMg3MgbtKvOB8j557Ka4x5YGoI0ZrU87FAcmkB9EKOSKkaCjO9KyEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش نیویورک‌پست، در پی حمله موشکی جمهوری اسلامی به یک پایگاه هوایی در کویت، چند نفر از نیروهای نظامی و پیمانکاران آمریکایی مجروح شدند. این حمله در حالی رخ می‌دهد که دونالد ترامپ، رئیس‌جمهوری آمریکا، در حال ارزیابی پذیرش آخرین پیشنهاد صلح تهران یا بازگشت به شرایط جنگی است.
یک منبع مطلع روز شنبه نهم خرداد، اعلام کرد که در پی رهگیری یک موشک «فاتح-۱۱۰» توسط پدافند هوایی کویت طی ۲۴ ساعت گذشته، قطعات و ترکش‌های ناشی از انهدام موشک بر فراز پایگاه هوایی «علی السالم» فرود آمده و منجر به جراحت سطحی چند آمریکایی شده است. این حادثه همچنین خسارت شدیدی به دو پهپاد «ام‌کیو-۹ ریپر» (MQ-9 Reaper) به ارزش تقریبی ۳۰ میلیون دلار وارد کرده است.
این حمله در شرایطی صورت گرفته که دونالد ترامپ روز جمعه با تیم امنیتی خود تشکیل جلسه داد و اعلام کرد که قصد دارد تصمیم نهایی را درباره توافق با ایران اتخاذ کند؛ توافقی که شامل تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و آغاز مذاکرات بیشتر درباره مواد هسته‌ای ایران در ازای لغو محاصره دریایی آمریکا می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75805" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nvl1ETdZegsIzIG8hcUeuV41MiQf7xcdBqtVWCxLhLANHZTcAytVye7dw3QGunHo1VANKX0fIlwEDJDzZbxOau8cF6_5tFVa1UpaowFlPIKnzrRYEP4XJbZ_LBRLvYZdsFwHTFIjwiDY1bpmXE4s-pozi-fjx7FBGVv66qNouVGTd_l5iqJwN6BXIxrV19SOdyYbAjv0zRBdgrY2D-oMUZlaa4EhoPxjUtRI6Mzd9wJb8CT7WblS_uQ14c1wVYbuHCTupxxl4VihIyUtCJYMlkCDmjYwUdxPmrAFJgwoB-NQ1v4wFw5oaeoTC9wrI3irAcllN_CwnVmrr-eJXYS4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/75804" target="_blank">📅 19:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=dH8p7OEI1vozQjVmZIajqZxcoAUyfr6ZZkw5NJEDmsoZGt0kWFClKCv19qoyK6qP9kfJYDSNdLO5SYRhv8EA4iKQLMV-6UD02aG3jU-XgiPvwVLVheEAOO646B8WzhVzhhZLcgyFu3sDuGYF3bFeTnAXsrzMDTljJTVCdAx0mAZeoB-jog5HjAC6JP3gL6S7Ji4wlgAyk1P8BcVNGEOjnOWUGM5HhLQusXwqL5bhbzIcHJrgcPeRhPtmdUVIci8ZeRSMiavIg8me2Rbqiki6m478VAhS9GUR_G_n30cxHJGBLkZEe-njoUlTgAKDSi1aM-J7BpUZo0EC2cLQun41KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=dH8p7OEI1vozQjVmZIajqZxcoAUyfr6ZZkw5NJEDmsoZGt0kWFClKCv19qoyK6qP9kfJYDSNdLO5SYRhv8EA4iKQLMV-6UD02aG3jU-XgiPvwVLVheEAOO646B8WzhVzhhZLcgyFu3sDuGYF3bFeTnAXsrzMDTljJTVCdAx0mAZeoB-jog5HjAC6JP3gL6S7Ji4wlgAyk1P8BcVNGEOjnOWUGM5HhLQusXwqL5bhbzIcHJrgcPeRhPtmdUVIci8ZeRSMiavIg8me2Rbqiki6m478VAhS9GUR_G_n30cxHJGBLkZEe-njoUlTgAKDSi1aM-J7BpUZo0EC2cLQun41KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز شنبه نهم خرداد گفت ایالات متحده در صورتی که مذاکرات با ایران به توافق منجر نشود، آماده ازسرگیری حملات علیه جمهوری اسلامی است.
هگست در جمع خبرنگاران گفت: «در حال حاضر تمرکز ما بر حفظ آمادگی و آماده بودن برای بازگشت به عملیات است، اگر لازم باشد.»
او افزود دونالد ترامپ «صبور» است و به دنبال دستیابی به «توافقی خوب» است که تضمین کند ایران هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
اظهارات وزیر دفاع آمریکا در حالی مطرح می‌شود که مذاکره‌کنندگان تهران و واشینگتن در تلاش‌اند اختلافات باقی‌مانده بر سر برنامه هسته‌ای ایران را برطرف کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75803" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jt1nRvc-c1TSzSHI1gFlj4LSp-O48plGshimqaNG4G5UZwpkd5O4IgpU1NmyhjyZHmbJlfNYEZkuRpGZjsPpIwcyJY_jN9dtgXaHl8RKKy4e3jFxHz6Cid7oTOppow8jRj6T9qiC9K6hi7fjF73Ge-7gPl5rXSxg1hk_7Dt5lAZfA3wDNNq_JsLr_kCDZGmC7pkzfP93fa_v41qjA59xiZW6vXVAXNzSJcXcmHo-AmACZ0_X3EBLPGZpW2vCN5qFU1eqU-Wo5nbB6XoVvFY1QU0LSCQgxJPb_FWFj6Vtp_7a6AtNJ47-JNztnBZJ-ZIP9smzy7mqsvHAyqUq0fhjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی نیلی، وکیل دادگستری، اعلام کرد شعبه اول دادگاه انقلاب شیراز بنیامین نقدی را با اتهام «افساد فی‌الارض» به اعدام محکوم کرده است.
نیلی در گفت‌وگو با امتداد گفت که بنیامین نقدی شامگاه ۱۳ دی‌ماه در شیراز به دلیل شعله‌ور کردن یک کپسول آتش‌نشانی به سمت ماموران نیروی انتظامی بازداشت شد.
به گفته این وکیل دادگستری، در ابتدا اتهام «شروع به قتل» به موکلش تفهیم شد، اما پس از آن اتهام وی به «محاربه» تغییر یافت.
او افزود پس از پایان تحقیقات مقدماتی، کیفرخواست بنیامین نقدی با اتهام‌های «محاربه»، «عضویت در گروه‌های برهم‌زننده امنیت کشور»، «اجتماع و تبانی به قصد ارتکاب جرم علیه امنیت کشور» و «فعالیت تبلیغی علیه نظام» صادر شد. به گفته نیلی، در خصوص اتهام‌های «ایراد صدمه جسمانی به ماموران» و «حمل سلاح سرد» قرار منع تعقیب صادر شده بود.
نیلی همچنین گفت قضات شعبه اول دادگاه انقلاب شیراز در جریان رسیدگی، مجموعه اتهام‌های مطرح‌شده را مصداق «افساد فی‌الارض» تشخیص داده و بر همین اساس حکم اعدام برای بنیامین نقدی صادر کرده‌اند.
وکیل بنیامین نقدی با اشاره به قصد خود و همکارانش برای اعتراض به این رای گفت که در مهلت قانونی درخواست فرجام‌خواهی خواهند کرد. او ابراز امیدواری کرد که با توجه به این که به گفته وی در جریان رخداد مورد اشاره هیچ فردی آسیب ندیده است و اقدامات موکلش مصداق افساد فی‌الارض نیست، حکم صادره در دیوان عالی کشور نقض شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75802" target="_blank">📅 18:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت.
انگاری که درِ ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشی‌تون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75801" target="_blank">📅 18:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeC2UoTXi35rTm_ExYSZ732fSwPsfNdyqKLWceC4RcDNnbn0jO9sYcO12lGZu2SQaviSYfymSGXFjttkSO_5m4T0tJ98CrYkLmA5BoyhHSpoDtIjDH_bM2nYAj7nTXz9WuIM1L2MJygpEvPz0FaET5Sqlr-K_QzWbRJeG-sYt4JOAfXuTMerH384QywIw77gHP_AjiZ0RF8XIPlelKazsYVcOj_ZXR2aMm_wiOlO53tTHG-y3QV_u_jg7fkVaCAjonOlzG6wio9ocDSMRu9B0YEmXWVpz6rnQSnuMceNYb6KIwjQGbA2S-mySGf_P7s4LU32YTnQyNZgu2E-gw_wSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی به نقل از سه منبع آگاه گزارش داد جنگنده اف-۱۵ای آمریکا که ماه گذشته در ایران سرنگون شد، احتمالا با یک موشک دوش‌پرتاب ساخت چین هدف قرار گرفته است.
به گفته یکی از این منابع و یک مقام آمریکایی آگاه، چین همچنین ممکن است در روزهای نخست درگیری، یک رادار هشداردهنده دوربرد را در اختیار ایران قرار داده باشد که این رادار توانایی شناسایی هواپیماهای رادارگریز را دارد.
ان‌بی‌سی نوشت مقام‌های آمریکایی همچنان در حال بررسی سرنگونی جنگنده اف-۱۵ای هستند و هنوز روشن نیست تجهیزات نظامی احتمالی چه زمانی به تهران تحویل داده شده است.
کاخ سفید به ان‌بی‌سی گفت شی جین‌پینگ به ترامپ اطمینان داده پکن تجهیزات نظامی به ایران نمی‌دهد. سخنگوی سفارت چین در واشینگتن نیز گفت پکن صادرات نظامی را «با احتیاط و مسئولیت‌پذیری» کنترل می‌کند و با «تهمت بی‌اساس» مخالف است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/75800" target="_blank">📅 07:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSOPH_mqsnMqXpKdJYBExYH5HIfVYoe6HnU6hqON5Ywu80JqK_qNDZjqhqZWrr7NodNVGKC7arMJOXFXnmhlUqxLSy0vwAFl1NYSmLYCL4d5bDm0BwcP-fnV4_tn22llIK0K9lbgXEtbF0sXwUUX4oq5P0u7ogbRbKxTXdUDP2oAt0dmZR5ZR0oG3e2Dh2GW6bqFkeH-fM2wS-DnfdP30jV2raK4fXlUEUOcjliDWSz2dG72aPSPSuL5qNr_Fvrv-XylPmJAWcqYKJ6AFMeSdhftayT-Sy6N6n_FMZkOeOhh1wqwRPxJH_z74VH4KIR_Onk0bQEddGu1LH6mcNYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'به جای پول نقد قطر موافقت کرده ۶ میلیارد دلار  اعتبار در اختیار تهران قرار بگیرد تا کالاها و محصولات اساسی را از قطر خریداری کند'
یک منبع آگاه از روند مذاکرات به ایران‌اینترنشنال گفت سفر قالیباف به قطر به شکستی دیپلماتیک منجر شد و با وجود درخواست تهران برای آزادسازی فوری و بی‌قید و شرط ۱۲ میلیارد دلار به صورت نقدی همزمان با امضای یک یادداشت تفاهم اولیه با آمریکا، مقام‌های قطری این درخواست را رد کردند.
به گفته این منبع، مقام‌های قطری تنها با آزادسازی نیمی از این مبلغ تحت محدودیت‌های سخت‌گیرانه موافقت کردند.
بر اساس گفته‌های یک منبع نزدیک به یک مقام قطری حاضر در این گفت‌وگوها، دوحه از انتقال مستقیم یا نقدی این منابع به ایران خودداری کرده است. در عوض، این پول تنها به صورت اعتبار در اختیار تهران قرار می‌گیرد تا کالاها و محصولات اساسی را مستقیما از قطر خریداری کند.
این محدودیت در شرایطی اعمال شده که آمریکا به شدت با اعطای دسترسی مستقیم و بدون محدودیت جمهوری اسلامی به دارایی‌های نقدی مخالفت کرده است.
آمریکا ابراز نگرانی کرده است که تزریق مستقیم پول نقد می‌تواند برای تهران فضای تنفسی اقتصادی حیاتی ایجاد کند و به آن اجازه دهد حقوق‌های معوقه بخش عمومی را پرداخت کرده و در دوره‌ای از تنش شدید منطقه‌ای، تجهیزات نظامی را از کشورهای دیگر تامین کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/75799" target="_blank">📅 03:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=J8oDmVUAE9ySM2CstWj3G4Cj27XOURazTc2fCnw5eFc0Cy1uo844-CfX_jfgy7AFNH8TPa52wvfr17Z-KN4QVkQOT1CKC6kTahRpu08GXjFXPTuHLTlnsGepk4Yg37bfZTNJXTv2-G-4v7VktfLhVgIyDoxZRLDFtufBPRKHbeSF-wI9lCgGy1vBBeqOg77M_HbaHQb3H9HgWe1wQ26RTM74_m1O1lnuGoV0JGiPZLF9UQS33TrLtWepam8bDNNkvkJB9DwEhNyIJskCRGyhLfjpV7fBKVQjyTzUTYsZx87WtJC2c0jLbqGc-oyhuc4Rbm09jilFPYMy_zyfj4ySMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=J8oDmVUAE9ySM2CstWj3G4Cj27XOURazTc2fCnw5eFc0Cy1uo844-CfX_jfgy7AFNH8TPa52wvfr17Z-KN4QVkQOT1CKC6kTahRpu08GXjFXPTuHLTlnsGepk4Yg37bfZTNJXTv2-G-4v7VktfLhVgIyDoxZRLDFtufBPRKHbeSF-wI9lCgGy1vBBeqOg77M_HbaHQb3H9HgWe1wQ26RTM74_m1O1lnuGoV0JGiPZLF9UQS33TrLtWepam8bDNNkvkJB9DwEhNyIJskCRGyhLfjpV7fBKVQjyTzUTYsZx87WtJC2c0jLbqGc-oyhuc4Rbm09jilFPYMy_zyfj4ySMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، بامداد شنبه ۹ خرداد با انتشار تصاویری مدعی شد بقایای یک پهپاد متعلق به آمریکا و اسرائیل که در حوالی قشم هدف قرار گرفته، کشف شده است.
تسنیم بیان کرد این پهپاد با واکنش پدافند هوایی ارتش هدف قرار گرفت و منهدم شد.
پیش از این خبرگزاری مهر به نقل از منابع محلی گزارش داد یک ریزپرنده در حوالی قشم از سوی پدافند هوایی هدف قرار گرفته و منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/75798" target="_blank">📅 02:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vLOtgjqq_dBi0qfecTbBWs4kVk96UO8b2bKewfWKTS_pBZlDvS3odfxtj0T7sFTE21MLw4BeYOqHYeMDEs-h24ZWuZ3gPxoGT-tYRUrlr9QbuUQjZ5mZXoclIHbvrfCVxYmFX3ob_L2L83FE2tnccCF9v2kY5fVfKScsEccYcYwpvkBQMqgoQ-gG_XCF-5F4zPyWFwqJ7LeJEAnP3MX-ruhow4tpH0dI_xP4Gq1ohbr37h3E-uhjkj7r1W2O9nnf3z-fs_kjSXCLgy_x_VnxCArELFxVV_Q9_UugcyNuMDvf2p4ZfeQ0wI9yHxpDo8srRijUFqvcCfA1XcHlu2X-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌پست، یکی از آخرین موارد اختلاف بر سر راه توافق احتمالی میان واشینگتن و تهران، چگونگی آزادسازی مرحله‌ای دارایی‌های ایران است که در قطر نگهداری می‌شود و برای اهداف بشردوستانه در نظر گرفته شده است.
بر اساس این گزارش، منابع مالی مورد بحث مستقیما در اختیار حکومت ایران قرار نخواهد گرفت، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده می‌شود و سپس این اقلام به ایران ارسال خواهد شد.
نیویورک‌پست به نقل از یک مقام دولت آمریکا نوشت پرداخت تدریجی این منابع به اجرای تعهدات از سوی ایران، از جمله بازگشایی تنگه هرمز و پاکسازی مین‌ها در تنگه هرمز، وابسته خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75797" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=HJuZEsE92X4zrbPtrPHhI4b2xENU-bFzgYlRCMajL8ogFqcjkNAjYR0UYFAxHMi0Wb_mcqJ93KNKgWCbKYExq8un_nFS9PeiDntT5268ci9Km8xWdj5kwF7fl9ddbUa6osFQYDiJ7-nUPRj1Ip_j6SGnsZllF4uCY0wSqJYb0VROVhDqTQBQImjFhyDlbonEwDd80d535H28nkCVOKqvYHk1jBECYfm3I24N6uxnMkoec89Inul7jUHlQibqLpRZHT2OR4z10qJPX-CUcMq7rr4e1baS0LHnJnTubSMc305zu7k9ScQnQ4sNc5M88RXw3BZl8cpK76x1xoXefbwRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=HJuZEsE92X4zrbPtrPHhI4b2xENU-bFzgYlRCMajL8ogFqcjkNAjYR0UYFAxHMi0Wb_mcqJ93KNKgWCbKYExq8un_nFS9PeiDntT5268ci9Km8xWdj5kwF7fl9ddbUa6osFQYDiJ7-nUPRj1Ip_j6SGnsZllF4uCY0wSqJYb0VROVhDqTQBQImjFhyDlbonEwDd80d535H28nkCVOKqvYHk1jBECYfm3I24N6uxnMkoec89Inul7jUHlQibqLpRZHT2OR4z10qJPX-CUcMq7rr4e1baS0LHnJnTubSMc305zu7k9ScQnQ4sNc5M88RXw3BZl8cpK76x1xoXefbwRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز جمعه هشتم خرداد در «مجمع اقتصادی ملی ریگان» اعلام کرد که واشنگتن حدود یک میلیارد دلار از دارایی‌های رمزارزی مرتبط با حکومت ایران را به طور مستقیم توقیف و کیف‌پول‌های دیجیتال آن‌ها را ضبط کرده است.
او با تاکید بر اینکه این اموال در واقع پول‌های دزدیده‌شده از مردم ایران است، اشاره کرد که بسیاری از صاحبان این حساب‌ها هنوز متوجه ضبط دارایی و کیف‌پول دیجیتال خود نشده‌اند.
وزیر خزانه‌داری آمریکا همچنین افزود واشنگتن با همکاری نزدیک متحدان اروپایی خود در حال ردیابی و توقیف املاک و مستغلات، از جمله ویلاها و خانه‌های متعلق به این افراد در سراسر اروپا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/75796" target="_blank">📅 23:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rnByf3ljTf8XP5U1sVKU3MbUUUVY9dkhs1H4dydJys9qzgkc3Em5-SqjevdDONSaDEeK3CCx0yN2OuUZ-frOD9o5pEmRl4tWj6hd_YBJBddHkpdE-QaMSTTH8opDxWCexpZ7qSjqonPXmhoJadUfqChM3MYf81KVjuOgHl1oyB2mWlSb9YbAIEUdp-hUZQFjAgCU6eJkUJIwO3FZXKLP1OkB93XfamZflGkZ37t8VBO-R9L53982i9S6ydwXAU8X79LQujBSeqK3BqmsWYmXU7X3T-jdNC_royQwBU7KxNrCHfEvPkKvoZFUVp6HHadzTTx9sK2If_fRTdIyeF0EOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از یک مقام ارشد آمریکایی گزارش داد نشست دونالد ترامپ در «اتاق وضعیت» کاخ سفید دو ساعت به طول انجامید، اما رییس‌جمهور آمریکا هنوز درباره هیچ توافق جدیدی با تهران به تصمیم نهایی نرسیده است.
این مقام افزود دولت آمریکا معتقد است به دستیابی به توافق نزدیک شده، اما برخی مسائل از جمله آزادسازی دارایی‌های مسدودشده همچنان محل بررسی و اختلاف‌نظر است.
@
VahidOOnLine
یک مقام ارشد به خبرگزاری آسوشیتدپرس گفت که این جلسه در حال بررسی چارچوب توافقی بود که آتش‌بس را به مدت ۶۰ روز تمدید می‌کرد و مذاکرات در مورد برنامه هسته‌ای ایران را پیش می‌برد.
این مقام رسمی در مورد اینکه آیا ترامپ پس از این جلسه تقریباً دو ساعته تصمیمی برای پذیرش این توافق اولیه گرفته است یا خیر، اظهار نظری نکرد.
sky
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75795" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVs7p4FVNRg4WnAe126BiFG4v6ENrKdPIN4ZziVWPrCwVs2iIxnrFzTvSCXPma6rxzVl_9-CzkvrP-dQRZ3Gu22fAvlWrvxcgVjKq1dilFyQldZ3I6Gw4FU0W79l0TW2syNWDrk27dwbZ3_3dNdjAelgTSY0dt7XULfRHu3cZZlq3XZRuQCA7809iQ8TOjqBJbEnxDAkd4KadIOK3PdbLCsRsVNVNc9pceV1O18WE9zF48Y8GdqfFp3Zk1GO1fGbC6gE7ELnnARTymacvesj5bsT4RqRJdufOvNWF8_aQSTIU_JB_6CD0ZSNTZ6hQo0h-d2QrD0s6RGeWBbWAObkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال روز جمعه هشتم خرداد، در گزارشی اختصاصی به نقل از منابع آگاه فاش کرد که امارات متحده عربی در طول جنگ، ده‌ها حمله هوایی را علیه مواضعی در ایران انجام داده است.
منابع وال‌استریت ژورنال می‌گویند نقش امارات در این کارزار نظامی، «بسیار عمیق‌تر» از آنچه که پیش‌تر گزارش شده، بوده است.
بر اساس این گزارش، این حملات با هماهنگی کامل واشنگتن و تل‌آویو و با اتکا به اطلاعات ارائه‌شده از سوی آن‌ها انجام شده است.
اهداف امارات شامل جزایر قشم و ابوموسی در تنگه هرمز، بندرعباس، پالایشگاه نفت جزیره لاوان و مجتمع پتروشیمی عسلویه بوده است.
حملات به عسلویه که به صورت مشترک با اسرائیل و در پاسخ به ضربات جمهوری اسلامی به زیرساخت‌های انرژی امارات انجام شد، واکنش‌های شدید بین‌المللی را برانگیخت و واشنگتن را وادار کرد از اسرائیل بخواهد حمله به تاسیسات انرژی را متوقف کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/75794" target="_blank">📅 22:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#قشم
پیام‌های دریافتی درباره فعالیت پدافند:
سلام وحید
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
21:26 هشتم خرداد جزیره
#قشم
صدای توافق خیلی بلند به گوشمون رسید. حدود یک دقیقه صدای شدید پدافند، احتمالا برخورد موفق با پهباد نفوذی.
درود همین پنج دقیقه پیش پدافند قشم داشت شلیک می کرد درگیری بود
ساعت 21:25
همین الان پدافند قشم فعال شد و یک چیزی رو زد
🔄
آپدیت:
تسنیم: "در پی رصد ریزپرنده متخاصم دشمن آمریکایی ـ صهیونی در حوالی قشم توسط پدافند هوایی ارتش، بلافاصله در عملیات موفق مورد اصابت قرار گرفت و منهدم شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/75793" target="_blank">📅 21:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RkqW-iA_5Sw1FYrMN56Acmzf-ovZqP2EJAbF8b5ouzd5uy3ETkUyHi9OP5iKJ86w2lYKZ_7KjLamv3BNgxQWut-tIHV7j6rGPT2Uq5g6vYGvEG6N_Ejg8OvBKjHWqKaC7WCC_Mg-hdijLqMrwOWdDGcFSgZRQb7Ssur9rYYPCXJUakUDZaNeqJMo6uwXRJDBNO5PGLQAEO_x6Vsc-HIu1roeAs5PIjF-6jY5oMS9SvPRvoAhX7d5ctkcR_sU3NYY5JoJMJmnmhPCQu_Y3zm5D6LN99ThjMSVZ76HQ-vOKXbrQhuxb26jvoDiccX1uWjMa42VoiwliySt5xvbHzCjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ پستی از نیوت گینگریچ، رییس پیشین مجلس نمایندگان آمریکا، را در تروث سوشال بازنشر کرد که در آن نوشته شده بود: پس از بررسی جنگ ایران در این هفته، متقاعد شدم ترامپ در آستانه یک پیروزی تاریخی قرار دارد
IranIntlbrk
پستی که گینگریچ ۸ ساعت پیش نوشته بود، ترجمه ماشین:
پس از آنکه این هفته را صرف بررسی جنگ ایران کردم، اکنون متقاعد شده‌ام که رئیس‌جمهور ترامپ در آستانه یک پیروزی تاریخی قرار دارد. نقطه عطف واقعی برای من زمانی رقم خورد که تصمیم‌ها و مانورهای رئیس‌جمهور ترامپ را نه از منظر یکجانبه‌گرایی آمریکا، بلکه از منظر رهبر یک ائتلاف تاریخی چشمگیر بررسی کردم؛ بزرگ‌ترین ائتلافی که تاکنون در خاورمیانه مدرن شکل گرفته است.
همه می‌دانند که اسرائیل متحد مهمی است. اما آنچه کمتر درباره آن صحبت می‌شود، عمق حمایت امارات متحده عربی، قطر، بحرین، عربستان سعودی و دیگر کشورهای منطقه است. برای دیکتاتوری ایران باید بسیار تأمل‌برانگیز باشد که دریابد حتی یک متحد ندارد که حاضر باشد محاصره دریایی آمریکا را به چالش بکشد. آرام‌آرام، به‌تدریج و با احتیاط، متحدان اروپایی ما نیز در حال صف‌آرایی برای کمک در خلیج فارس و تنگه هرمز هستند.
بخش بزرگی از مانورهای رئیس‌جمهور ترامپ علیه ایران زمانی معنا پیدا می‌کند که او را نه صرفاً یک رئیس‌جمهور یکجانبه‌گرای آمریکایی، بلکه رهبر یک ائتلاف ببینیم. من بخش زیادی از چند هفته گذشته را صرف بررسی گزینه‌های نظامی کردم؛ از جمله پیروزی در نبرد خلیج فارس و تنگه هرمز و، در صورت لزوم، استفاده از سطحی تکان‌دهنده و خردکننده از قدرت نظامی؛ مشابه آنچه رئیس‌جمهور نیکسون و وزیر خارجه کیسینجر در کریسمس ۱۹۷۲ علیه هانوی و هایفونگ به کار گرفتند؛ اقدامی که هر دو رهبر معتقد بودند ویتنام شمالی را به پذیرش آتش‌بس و آزادی اسرای آمریکایی متقاعد کرد.
اگر این یک کارزار یکجانبه آمریکایی بود، می‌توانستم با اشتیاق از یک کارزار نظامی تهاجمی‌تر حمایت کنم. اما در عین حال روشن است که چنین اقدامی ائتلاف را از هم می‌پاشاند، زیرا متحدان عرب ما متقاعدند که ایران هنوز می‌تواند خسارت عظیمی به میدان‌های نفتی و زیرساخت‌های آنان وارد کند. ائتلاف‌ها ذاتاً کندتر از کارزارهای یکجانبه عمل می‌کنند. با این حال، ائتلاف‌ها در نهایت قدرتی به‌مراتب بیشتر را وارد میدان می‌کنند.
من نیز مانند همه دیگران از سرعت گفت‌وگوها با این دیکتاتوری سرخورده‌ام؛ اما پس از بررسی توازن قوا و گزینه‌های در دسترس ائتلاف از یک سو، و دیکتاتوری مذهبیِ ایران از سوی دیگر، آماده‌ام بگویم که رهبری ائتلافیِ رئیس‌جمهور ترامپ ــ چیزی که تقریباً هیچ‌یک از منتقدان او نمی‌خواهند به آن اذعان کنند ــ در آستانه دستیابی به یک پیروزی عظیم تاریخی است.
و اگر دیکتاتوری ایران در نهایت ثابت کند که به شکلی نومیدانه به موضعی انتحاری پایبند است، زمان کافی برای یک کارزار نظامی با قدرت و اثربخشی عظیم وجود خواهد داشت. در هر صورت، ما در آستانه یک پیروزی شگفت‌انگیز برای ارزش‌های خود و برای خاورمیانه‌ای امن‌تر قرار داریم.
NewtGingrich
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75792" target="_blank">📅 21:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw6u8BDAwUPc1IvKpCGVYehkDbupabGlcltxgwqmRxrCEKHR6Mgtq141GxiZq0UNtB8_YscNPf27Ia5MJ1--QL9KVBNMVcuz7ZO-eaCLfas12t78mPNgEfd4-if6ukVDhsnLL43V8L45eiIPQ57i8W-Y2RwG3-IyTM1H4gdSBI-mM8CwOu-KFSC1C_AnxvV3yuZ8vClrBOUQ7RpvDMGA1wQOISBPMppE0e1PhJGoM8PQzQQGBiB9woQGIZzi6OWwZ53zDFQKGz_gTIidf91xRGlF7QMME3W1yAmyjRZ28XdYZS6obDQtWEQBC-IUyzx-RPIUtA_6oaCw0wPcnJLhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی خانعلی‌زاده، عضو تیم رسانه‌ای هیات مذاکره‌کننده جمهوری اسلامی، نوشت که در متن تفاهم احتمالی هشت بند از ۱۰ بند بیانیه شورای عالی امنیت ملی که به تایید مجتبی خامنه‌ای رسیده، رعایت نشده و زیر پا گذاشته شده است.
او افزود که تفاهم‌نامه کنونی برخلاف بیانیه آتش‌بس شورای عالی امنیت ملی است و مشخص شده که اساسا مذاکرات پسااسلام‌آباد، بر مبنای شروط رهبری انجام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75791" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uMwGMuodlRiB06O_EvpdC0getrKF6kY7SX6nhON_4tZJDlER7AEU5pFajhOxzI_yT0w0UnWWPnNzhVChuJOcWHSiKI3EiarLrCPLk7mw7YxscATTvDNHdujg-wd7tMmq-FXAfY3mAn-GlDuNXnKB0ldkidkOXApEMySHKbmW2iUB4NBVWQwrKt7oEfQCTyUD2_hX9tyvFERMfGOKh0LUXhk805HS8EVrHu_3gDwtppXsfCUwJK96Tk7G3hJPv5G3Fj_EYYpL61icR6uuj4nKSLM52gf1s90pvkfGEkaj3C66Ae-uWZAXj-S7kKv_ttPEUwZhphb_U9MCHfj8GvdF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه ایران در مصاحبه‌ای با صدا و سیما گفت که تبادل پیام‌ها ادامه دارد ولی هنوز هیچ توافقی نهایی نشده است و افزود که مدیریت تنگه هرمز باید توسط ایران و عمان تعیین شود.
او بار دیگر گفت: «در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد پرونده هسته‌ای هیچ مذاکره‌ای نداریم.»
این اظهارات در حالی از سوی ایران مطرح شده که آقای ترامپ فهرستی از خواسته‌هایی را که می‌گوید ایران باید برآورده کند، مطرح کرد که شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای، باز کردن تنگه هرمز بدون دریافت عوارض، مین‌روبی کامل این آبراه و خارج‌سازی ذخایر اورانیوم ‌غنی‌شده ایران با همکاری آمریکا و تحت نظارت آژانس و سپس از بین بردن این مواد است.
@
VahidHeadline
پیش‌تر: خبرگزاری فارس، نزدیک به سپاه پاسداران، نیز به نقل از یک منبع ایرانی دیگر اظهارنظر رئیس‌جمهور ایالات منحده دربارهٔ توافق احتمالی با ایران، را «آمیخته‌ای از راست و دروغ» خوانده است.
این منبع گفته که در متن توافق بندی درباره باز شدن تنگه هرمز بدون دریافت عوارض وجود ندارد و تفاهم بر سر نابودی دخایر اورانیوم ایران را نیز «بی‌اساس» دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75790" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SyO107v2rlOfgGv5kh_eq1MKvOSakH4w19Dk_pusKw3QIvysLasx3hkodqqmNDwPdqwJ3rdCOo_jOsm5HJliELNnNg2AckkEvqDcZfr6QFV__-7PSt5N9PzD7Nue-_KF3GQE7YhDkRULSr8k-Wu7lzkm53BouL8a-pihKpz5EsDpLnTvWKPI6JmkM-rq0d2nBUFPiKUCWlXfmKyOM0X6NRbq9d9WOsX8WY9yb5TKoE0RGy7NDt0jrkvuqYh__L5jTw9NgOj6IjErIFgShnWb5ORHbrTIPX4uI9IA82twKHxvmuLxOTsvEWIRCq6yKM0zMqTFnRMbdGevHEdG-GTH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
پست ترامپ، ترجمه ماشین:
ایران باید بپذیرد که هرگز سلاح یا بمب هسته‌ای نخواهد داشت.
تنگه هرمز باید فوراً، بدون عوارض، برای عبور و مرور آزادانه کشتی‌ها در هر دو جهت باز شود. همه مین‌های دریایی، اگر وجود داشته باشند، برچیده خواهند شد؛ ما با مین‌روب‌های زیرآبی فوق‌العاده خود، شمار زیادی از این مین‌ها را از طریق انفجار از بین برده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده‌ای را، که تعدادشان زیاد نخواهد بود، جمع‌آوری یا منفجر کند.
کشتی‌هایی که به‌دلیل محاصره دریایی شگفت‌انگیز و بی‌سابقه ما در تنگه گرفتار شده بودند ــ
❗️
محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدران، مادران و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده، که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده؛ در حالی که کوه‌هایی که عملاً بر اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فرو ریخته‌اند روی آن قرار دارند،
❗️
توسط ایالات متحده از زیر خاک بیرون آورده خواهد شد؛ کشوری که، طبق توافق، تنها کشور در کنار چین است که توان مکانیکی انجام چنین کاری را دارد.
این کار با هماهنگی و همکاری نزدیک با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و سپس این مواد نابود خواهد شد.
❗️
تا اطلاع ثانوی، هیچ پولی رد و بدل نخواهد شد.
درباره موارد دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
💥
اکنون در اتاق وضعیت جلسه خواهم داشت تا تصمیم نهایی را بگیرم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/75789" target="_blank">📅 18:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=DNyUnTXbcV2qp60Xr1C_gsjtQn0lECQyYO9gwxCDPWPRxgdXmOXveZXRbZ_TdPVzmeZg4cdfTdV9LeH4Q4HdMh39CPpGl-T7aXKVNdp3IrNPHfqclyjMYTT51eExT4XVamTl4Wn3uohvHSTuV9yZCB14zNujr2RmzODD04BOAFLLzHdAdyZ9EclZkSEmIh89vhlPkeMmTrs-swpw8P0TuM1URXZJkWGAMeqCxEQo_Vf6F4dOib3hmL3FQ7_GTZ3jKx5hZGLXhvjH7EIcnqt8lJLzNoQHVvhJTVY5fRY7dDINMFIJ7nA_7Re4EPPbZKg-KxTzixq9wdj0TC10v0P31g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=DNyUnTXbcV2qp60Xr1C_gsjtQn0lECQyYO9gwxCDPWPRxgdXmOXveZXRbZ_TdPVzmeZg4cdfTdV9LeH4Q4HdMh39CPpGl-T7aXKVNdp3IrNPHfqclyjMYTT51eExT4XVamTl4Wn3uohvHSTuV9yZCB14zNujr2RmzODD04BOAFLLzHdAdyZ9EclZkSEmIh89vhlPkeMmTrs-swpw8P0TuM1URXZJkWGAMeqCxEQo_Vf6F4dOib3hmL3FQ7_GTZ3jKx5hZGLXhvjH7EIcnqt8lJLzNoQHVvhJTVY5fRY7dDINMFIJ7nA_7Re4EPPbZKg-KxTzixq9wdj0TC10v0P31g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با شرح عبور موشک‌های تاماهاک در مرز عراق و ایران در شبکه‌های اجتماعی و چند رسانه منتشر شده و گفته می‌شود مربوط به روزهای نخست جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75788" target="_blank">📅 17:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=KHQH8tjocMNWIiLpFK1chsTCSTfBiGt-7_wzRJNgXNuQSg9pSP4IImXnY0j70YWQSQH-DxakIUUmWFcJKj2GJcv3gpcdKO8gXed2_u4mih--2UBSbk6oGLprXyatNPdNwKvczbKVQZ9P37MGc5wfvHT_lyIM-1X-CwG0MGSfPdVUJgyEa17YVY80UyGosajMQiBzyc-qJ3cAGx-qHDb6S65B5QbhVOfTxlUWMCimIXhHmEqpBFz-r9kXslWUuss4n9D_RHulqMNy_TN3CGpClONxXqpTOAJWiXgU4IwRoKhjUQHKzZb0Ay_Pw044Og1KNcqaxM167ASCAACk8DNpmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=KHQH8tjocMNWIiLpFK1chsTCSTfBiGt-7_wzRJNgXNuQSg9pSP4IImXnY0j70YWQSQH-DxakIUUmWFcJKj2GJcv3gpcdKO8gXed2_u4mih--2UBSbk6oGLprXyatNPdNwKvczbKVQZ9P37MGc5wfvHT_lyIM-1X-CwG0MGSfPdVUJgyEa17YVY80UyGosajMQiBzyc-qJ3cAGx-qHDb6S65B5QbhVOfTxlUWMCimIXhHmEqpBFz-r9kXslWUuss4n9D_RHulqMNy_TN3CGpClONxXqpTOAJWiXgU4IwRoKhjUQHKzZb0Ay_Pw044Og1KNcqaxM167ASCAACk8DNpmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه هفتم خرداد ماه اعلام کرد عمان پس از دریافت هشدار واشنگتن درباره پیامدهای احتمالی مشارکت در طرح دریافت عوارض از کشتی‌های عبوری از تنگه هرمز، به آمریکا اطمینان داده است که برنامه‌ای برای اجرای چنین طرحی ندارد.
بسنت روز پنجشنبه در نشست خبری کاخ سفید گفت که صبح همان روز با سفیر عمان گفتگو کرده و از او شنیده است که مسقط هیچ برنامه‌ای برای دریافت عوارض در تنگه هرمز ندارد.
او افزود: «به او گفتم این موضوع از اساس غیرقابل قبول است و او نیز نمی‌خواهد افراد عمانی یا موسسات مالی عمانی را در معرض خطر تحریم قرار دهد.»
بسنت ساعاتی پیش‌تر در پیامی در شبکه اجتماعی ایکس هشدار داده بود که وزارت خزانه‌داری آمریکا هر فرد یا نهادی را که به‌صورت مستقیم یا غیرمستقیم در تسهیل دریافت عوارض در تنگه هرمز نقش داشته باشد، هدف تحریم قرار خواهد داد. او تصریح کرده بود که هر شریک احتمالی این طرح نیز با مجازات و تحریم روبه‌رو خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75787" target="_blank">📅 17:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxVkW36EeIIFp-2Hs_moFEUQ4XSPWLc782GSFNSIWWUEEqOO7_cmyKKB4CkTse4iNw-ksssv539_veIFg9zME6UdFbCmLaczJZyNJwenCIY2DhSOPoZB8bK5qEZXVVI6JDc8r1LLtijdKmZcRBZSWoC8sddC19vTtfeDp2fL44OAGZclJPQvKNlalqdLALUwqYH7jMuQKvGf9MQZRlSnWDgpSfNlCZI-Ep01gf35yF06cXxfK3ZorSjVYkfnwg1DnASLhydKaYaVUXv3kO3mX4SYlMEWv4fqH_2tSCPbH6o_813aDyl0Q0S9N5QLHtoobvl30deA--muL9EcPlnuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
به گفته این منابع، بسیاری از نکات مرتبط با برنامه هسته‌ای جمهوری اسلامی در مذاکرات جاری حل‌وفصل شده است.
بر اساس این گزارش، جمهوری اسلامی با نظارت بین‌المللی بر تاسیسات هسته‌ای خود برای جلوگیری از تعطیل‌شدن آن‌ها موافقت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75786" target="_blank">📅 17:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtODyNb4z71EWPvGGyHtTqkbRhz75uWDPpYuwXXtrVG_G8kv6keMZA0Njb1-_8_HysuSSzcsGGWwZ-xm0oUdbDHabewi7WE7Jn6acpduZCrTox_WbQudVa1cxd1LmK9SQKeNHPIXuE8GUElPkmMNUy86Jrf18Ff-P7GZJzW5TGflrJ6UwDyTnkhPPgNr1QqOC0u3CkTjdNSi4My-SqKIJQ_9IhubiUrvUWtTG8AZHKfHmetvoacJAzT4hvjleMJOIR6ZmBI8u1puv7vGy4PifLEqxEPc9LFkX6PDmHnJjIsQJE22XYTvuHCPO6c0Ia0d27gWASeUqdogNKDysJgchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی با آمریکا، روز جمعه تهدید کرد که تهران امتیازات مورد نظر خود در توافق پایان دادن به جنگ را با «موشک» می‌گیرد و پیش از اقدام واشینگتن درباره این توافق اقدامی نخواهد کرد.
او در شبکه ایکس همچنین نوشت: «هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است.»
این موضع‌گیری یک روز پس از آن انجام شد که چند رسانه غربی خبر دادند آمریکا و ایران به تفاهمی برای تمدید آتش‌بس و رفع محدودیت عبور و مرور کشتی‌ها در تنگه هرمز رسیده‌اند، اما این توافق منتظر تصمیم و امضای نهایی دونالد ترامپ، رئیس‌جمهور ایالات متحده است.
قالیباف در پیام خود اعلام کرده که «اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد».
از سوی دیگر، رسانه‌های نزدیک به سپاه پاسداران می‌گویند گزارش‌ها درباره توافق تهران و واشنگتن صحیح نیست. خبرگزاری تسنیم در این مورد به نقل از یک «منبع مطلع» نوشت: «متن توافق تا این لحظه جمع‌بندی نهایی نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75785" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyF975DDi0sUIZoB8TUwODkJ-v_W_pT_p1PADRM2c2z7lyM62CEfjxUvTDF4eXTSRTeohmrG6uV_CxsZXLBKl9q8J5KhFjZozcCMHLU9uyBGwhuhUuw7iok9opaewsFywu9GMMDPwo3Tm2L_VQmzTjZylEQuSLcV_9H_tYFB8qrKm51Nq70cd6n1CPd_g1xHo93zhf0gTkVbNoj_p5YSO-Ltql68XO7vOj4LghWN8JT1r5QnW3UGr5RRbFJyqWv6sFrJykXETICEprU1uA8tCLcArFG-5M16rj7Tmasf1EBXgY1rIUxnWMbgTuihTSY3uAVjxpMVMBM0P5XaaErSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از ابتدای سال جاری تاکنون، اجرای ۶۶۰ مورد اعدام توسط جمهوری اسلامی را مستند کرده است. با این حال، به دلیل ماهیت پنهان‌کاری و غیرشفاف بودن سیستم قضایی ایران، آمار واقعی به احتمال زیاد بسیار بیشتر از این رقم است.
‏
🔸
از زمان آغاز جنگ، آمار اعدام معترضان و افرادی که به جاسوسی و اتهامات مشابه علیه امنیت ملی متهم شده‌اند، با سرعتی نگران‌کننده افزایش یافته است. «اعترافات اجباری»  قربانیان، اصلی‌ترین «مدرک» مورد استفاده در این احکام مرگبار بوده است.
‏
🔸
این اعترافات در شرایطی کاملا مبهم و تحت فشارهای شدید جسمی و روحی اخذ می‌شوند. جمهوری اسلامی به طور مستمر این اعترافات اجباری را در رسانه‌های دولتی پخش می‌کند تا از آن به عنوان ابزاری برای توجیه اعدام‌ها و سرکوب مخالفت‌های عمومی استفاده کند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75784" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRTMfiW7wThij--ZUI9ym3cBfEss_OSih4e92mLcw_YCwht26YVq2QS1YIAsydgKbi2nqToAGVzDGglEOPekfIRjDsjhlrG7SnhikVv3I7YWjfe6TdJr1S-zeSYNZvC_YxgIAo_v6cQ6ABaCBoR8T0zOKjya9XMY9DUeD8ygG58nIpFg0EDGuqxO9q2A_M0vvyN7ReTXBiUgANPO21WWfqXEzZ_yY4iM8YPppqqNZ_wfH8Ne_PyOQdqYAkOpA5g804lzvGtyuGomd72MHG4IurRfI-47VPKHS7IMbXBoxG7qvQUF8ZQnM3gzJRxJfDY60PX_ftypqvCxrhv-2xPhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
شیخ تمیم بن حمد آل ثانی، امیر قطر، در تماسی تلفنی با دونالد ترامپ، رئیس جمهور آمریکا، در مورد تحولات منطقه‌ای گفتگو کرد.
دفتر امیر قطر در گزارشی از این مکالمه تلفنی اعلام کرد که شیخ تمیم بر اهمیت اولویت دادن به راه‌حل‌های دیپلماتیک و گفت‌وگو بین همه طرف‌ها به امید جلوگیری از تنش‌ها و تشدید بیشتر در خاورمیانه تأکید کرد.
در این بیانیه آمده است که ترامپ نیز به نوبه خود از نقش قطر در حمایت از تلاش‌های میانجیگری پاکستان بین واشنگتن و تهران قدردانی کرد و «از تلاش‌های قطر برای رفع اختلافات و ترویج کاهش تنش در منطقه» تمجید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/75783" target="_blank">📅 02:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=S3grVchdV3Q06cq-sZNVdpAOTKUwN5WSCwSCbBW8R4LTStVkxOUvjqvOSJ6vfB57uCLTunwr0bmOvYObuNwR1je4uJBlRve0YWGxhIHnygXFLQIAw-ACMPrW2Hb1Zj8Uf67ZKU4nrY8xaJRF9-bsrji2D4aBopjaTwth2WTupp3TSbEFJ4I8QnfaAeWtCOtZC6OG_ok34EUlUxSFgwCE3dWJbY2b-sNyG4rkzWBMLUPst8vZNaRX1h9vtQ2uTqITcwWAacRpHK-m0CpbCFFFyCfcIfAZNbBrPZ9YbUSU7nF2I6TMtSARJom2znfDg5TT54NwLaMUniggk2f2GrW9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=S3grVchdV3Q06cq-sZNVdpAOTKUwN5WSCwSCbBW8R4LTStVkxOUvjqvOSJ6vfB57uCLTunwr0bmOvYObuNwR1je4uJBlRve0YWGxhIHnygXFLQIAw-ACMPrW2Hb1Zj8Uf67ZKU4nrY8xaJRF9-bsrji2D4aBopjaTwth2WTupp3TSbEFJ4I8QnfaAeWtCOtZC6OG_ok34EUlUxSFgwCE3dWJbY2b-sNyG4rkzWBMLUPst8vZNaRX1h9vtQ2uTqITcwWAacRpHK-m0CpbCFFFyCfcIfAZNbBrPZ9YbUSU7nF2I6TMtSARJom2znfDg5TT54NwLaMUniggk2f2GrW9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: جی‌دی ونس می‌گوید ایالات متحده در مذاکرات با ایران «پیشرفت زیادی» داشته و معتقد است تهران «حداقل تا حالا با حسن نیت در حال مذاکره است.»
جی‌دی ونس: خب، فکر می‌کنم گفتن دقیق اینکه رئیس‌جمهور دقیقاً چه زمانی یا اصلاً  تفاهم‌نامه را امضا خواهد کرد، سخت است. ما در حال رفت‌وآمد بر سر چند نکتهٔ زبانی هستیم.
کاملاً واضح است که به نظر من، ایرانی‌ها — آنها یک معامله می‌خواهند. آنها می‌خواهند تنگهٔ هرمز را باز کنند. ما هم می‌خواهیم تنگهٔ هرمز را باز کنیم.
🔸
چند مسئله در مورد موضوع هسته‌ای وجود دارد: ذخیرهٔ اورانیوم غنی‌شدهٔ بالا و همچنین مسئلهٔ غنی‌سازی.
پس می‌دانید، ما با آنها در حال چانه‌زنی و رفت‌وآمد هستیم. ما واقعاً فکر می‌کنیم آنها حداقل تا حالا با حسن نیت مذاکره می‌کنند.
داریم پیشرفت می‌کنیم و امیدواریم به این پیشرفت ادامه دهیم تا رئیس‌جمهور در موقعیتی قرار بگیرد که بتواند توافق را تأیید کند.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/75782" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbTNzyVSLVi1XqNZ-x9woLEtlWcpOs273Yz6Q0WuUjXTjSw_7h4XN3uJ8boYM4P2lp9Uxea4NkAarPhJQdRVb1bSfDhcjB9jTGXI61Lb-67tR3b-OaU-GhImj37O1kY3AU7P1S2_BYBSWa2YPJnapdkkCMEHnaPHKLZjRU86WBIr_oRQS8ELz5oH9-SldteXV4tEf7g7VQfw6k25p8IIT9BNISSj0wWrsmjmBjhHP7e-ygXubokRS1l16dr5i1FspgXdMQd-h96qwCr4-ToHWwcieziKWWRRWNpCgVgRhqyBh-Olu65hEYN4XswC-MMM-U4OpEo2LYV9D2SyxtbdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که نیروی دریایی سپاه شامگاه پنج‌شنبه در نزدیکی تنگه هرمز به ۴ «شناور خاطی» که قصد عبور بدون هماهنگی از تنگه هرمز را داشتند، «شلیک اخطار» کرده است.
همزمان، گزارش‌های منتشرشده در رسانه‌های اجتماعی از شنیده‌شدن صدای انفجار در هرمزگان و بوشهر حکایت دارد.
@
VahidOOnLine
ساعتی پیش پیامی دریافت کرده بودم که در پست قبلی نقلش کرده بودم و الان به اینجا منتقلش کردم. پیامی از شهروندی که درباره یکی از اعضای خانواده‌اش نوشته بود: الان قشم بود. پلاک موقت دادن بهشون گفتند فقط از جزیره خارج شید سریع
همزمان با خبر بالا هم پیام‌هایی داشتم:
صدای انفجارهایی در بندر عباس شنیده میشه.
صدای انفجار داره سمت قشم و دریا میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/75781" target="_blank">📅 23:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tB1Jt3fbns0iUUgwZKlmDXMm150PUeN8dXXtvVDGPj-W4yCiDgUuo_iE9eKB5Kk5TUVdn0m-QAQvc7DU1wzTreLV7ANgtt3jnjynDRV08emCbyr4CrWBFsdye6hM4wT0a_v2DO259DZZHSinFR18myCM4-1bnKe2AHmcQN7dcwz_h3PkVmhKG2vuAK4G8sE0yB6AtRO2StJjYvqg6Gexjo4Z5Jy9jCEXXWu4qsNBs-_MntbNNbniY0RfZQQQYltDAT72GyA1tH2CuNeQdep8tFoXY94L9xvdi4srWO3Nu5iSmN5gPlJrERQMwlmCNYjO8d-K_JVQIiSPES7vMGVZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
#جم
در استان بوشهر
پیام‌های دریافتی درباره شنیده شدن صداهایی
:
▪️
همین االان 10/42دقیقه موشک از جم پرتاب شد
▪️
الان جم رو زدن...صدای انفجار زیاد ۲۲:۴۰
▪️
سلام آقا وحید
امشب ساعت ۱۰:۴۶ ۷ خرداد
بوشهر شهرستان جم نمیدونم صدای پرتاب موشک بود یا جنگنده ولی خونه ها لرزید
[معمولا این دو صدا با هم اشتباه گرفته میشن.]
▪️
درود بر وحید جان آنلاین از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
🔄
آپدیت:
مسعود تنگستانی، فرماندار جم، به خبرگزاری صدا و سیما گفت نیروهای مسلح جمهوری اسلامی «یک هواگرد» را در آسمان این شهرستان در استان بوشهر هدف قرار داده‌اند و اکنون وضعیت منطقه عادی است.
@
VahidOOnLine
یک مقام آمریکایی ادعای صداوسیمای جمهوری اسلامی درباره سرنگونی یک هواگرد آمریکا در استان بوشهر را رد کرد.
به گزارش رویترز، این مقام آمریکایی که نخواست نامش فاش شود، گفت هیچ هواگرد آمریکایی در نزدیکی بوشهر سرنگون نشده است.
@
VahidOOnLine
آپدیت: تصویر بالا
به صور رسمی هم از طریق
سنتکام
تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/75780" target="_blank">📅 22:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGVmsstYqJwwhXZvAWbZ5QQaNAklLIU9hDW-cHjqL22egSKZvIJkG_StCA5q2oUnBHC2tqs4OwNIv_uPeMP4YNMZ44aBlLT4HnmTIb7rqLLAi4hzFr6qu_gQH3aOUF1aoYRR4GfMO_QchIGF9rjUpK7k9ERYAz9VwYutn1K-JF9Q03RTrD5VFlaT9aGJHPPCgkNB7l3pFS2V_lIt_ZXPVFl09SNIuT8-7-zpBAyjxyfKh8Ax8cTkne4HchfZZrlCjIGkPYjdpatw1v49nQXLPH7Ddh0zbrv84TNr4hLSL4R_mUA08_Zdk6Ic-jd4JDnmj81re3fgWsr967oSOTys3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارگان خبری مجموعه فعالان حقوق بشر در ایران خبر داد که تارا و کیمیا داوودی، دو خواهر محبوس در زندان اوین، توسط شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی در مجموع به ۱۶ سال حبس محکوم شده‌اند.
براساس این گزارش، کیمیا داوودی به اتهاماتی از جمله «ارتباط با گروه‌ها و شبکه‌های معاند» و «اجتماع و تبانی علیه امنیت کشور» به ۱۰ سال زندان و تارا داوودی نیز به اتهاماتی شامل «اجتماع و تبانی علیه امنیت کشور» و «تبلیغ علیه نظام» به شش سال حبس محکوم شده است.
این دو خواهر در تاریخ ۲۴ دی‌ماه ۱۴۰۴ در جریان اعتراضات سراسری در تهران بازداشت شدند و هم‌اکنون در بند زنان زندان اوین نگهداری می‌شوند. به گفته منابع حقوق بشری، بازداشت آن‌ها با خشونت نیروهای امنیتی همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/75779" target="_blank">📅 19:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OYKeg83YZCQdWpnV5xwA0FHUCOHSz5JdSQd9EILVPzVebWNoUVsMGzOH7o1181sVzyCmD-Le5RQflkC0_P-pJNcCUxedEAmJeFYPbXipFkE2EmWx1tRm_vEJppkJRV1FZniojlmNoymeOmsqptcX2jwpFI6-xLPsNh6sOIKlXezZrHVhshsmMJQNwPNgLuovN1kpbztBUu0tKKTTLft6kHMM1ZgOgdThrjO4-LiJYyactyKSvJG5gR_xvLLwDSFsU4xK5t89FiwfXjTwqaBiWnS5X3xToumjzh44k5xGnTgkb7jOt2O6Qie5gaUhLOd1JdbhqxfLiCs9bg9dDTgXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی گزارش داد که مذاکره‌کنندگان آمریکا و جمهوری اسلامی به یک یادداشت تفاهم با مدت ۶۰ روزه برای تمدید آتش‌بس و آغاز مذاکرات درباره برنامه هسته‌ای ایران رسیده‌اند، اما دونالد ترامپ، رییس‌جمهوری آمریکا، این متن را هنوز تایید نهایی نکرده است.
مقامات آمریکایی که نامشان فاش نشده به این رسانه گفتند که شرایط توافق تا سه‌شنبه تقریبا نهایی شده بود، اما هر دو طرف هنوز نیاز داشتند تایید مقامات ارشد خود را بگیرند.
مقامات آمریکایی افزودند که طرف ایرانی اعلام کرده که تاییدهای لازم را دریافت کرده و آماده امضا است.
تهران هنوز این موضوع را تایید نکرده است.
اکسیوس نوشت مذاکره‌کنندگان آمریکایی جزئیات توافق نهایی را به ترامپ گزارش دادند و او درخواست کرد چند روز برای فکر کردن زمان داشته باشد.
@
VahidOOnLine
بعدا
فاکس‌نیوز
هم خبر مشابهی منتشر کرد.
و گویا به همین دلیل هم می‌خواستند اینترنت را باز کنند. پیروزی جلوه دادن با اعلام جشن و پروپاگاندا در جو جام‌جهانی و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/75778" target="_blank">📅 19:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SmOYEvtzCQkpk1VwsidkIB4yOP_ufnN3_yi-eMQZQeAs_24kcJ6ONry-2iK0Vi161Hu8Sajr9FvWhXlYYUEVbwGJUqkdoorasXxjLr-Q1GIJrTffe7BQWzaKknxvHCVhqu7eftaLxc01qZqhv86AO00Hd02r8xux8fcqCChLvDyl1r2LGCtjOy0Hnq8C03ZAZ0k018LgRpTt0341-P-25p5jZpXjjFC5zQUl9K6Hv-pF-PFHNL5y0BunrZs8p9W11nV5wJiA_y9WLV9ztiQJNx_w6yWQbW4PpbqgETDuDb8ZSM_fk1jyu_A94mzf4CY5aHF29ETxTH82G90VMhWGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q5j9sJyMfm_3eYnLklCLra_2Dqf_weEMFpRucC3xZpo8HaKM1fTqSUfceoGcIxDPNhd77IhPBHp4uAiYPS9Gnr4gUudZqfZN6mFQ1u-itHFCgzaM5Mtk6yJJbjpmW8U9iFcLNMm3RumIyJWW1iKJdHeuOtOYSJKQOAemS7sVF-ULNTkDoOdwTkDCVOLyMTusIzbLVRjgGy47wVNT2F0kmvhgGVc2GDqfevj9bkvn9j6Pc2usYaW8SEyTTBpTS661WtcbJTrji_NmobmgVvuY8vo0cn9OFXADq3Wskb6_V-DSacdh8YECXJlG_jOVPtVyIW7YjftiyIQ4S1HWhouzow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس از انتشار پیامی منسوب به مجتبی خامنه‌ای درباره «نابودی اسرائیل تا ۱۵ سال آینده»، رسانه‌های ایران تصویری از دیوارنگاره جدید در میدان فلسطین تهران منتشر کردند که بر آن جمله «اسرائیل ۱۵ سال آینده را نخواهد دید» نوشته شده است.
در پیام منتسب به مجتبی خامنه‌ای که رسانه‌های ایران آن را منتشر کرده بودند، آمده است اسرائیل «به مراحل پایانی عمر منحوس خود نزدیک شده است.» در این پیام به سخنان علی خامنه‌ای در سال ۱۳۹۴ اشاره شده و تاکید شده است که اسرائیل «۲۵ سال بعد از آن تاریخ را نخواهد دید.»
@
VahidOOnLine
سپاه پاسداران روز پنجشنبه هفتم خردادماه با انتشار بیانیه‌ای به مناسبت کشته شدن محمد عوده  و عزالدین حداد، دو فرمانده حماس اعلام کرد منطقه جز با محو اسرائیل روی آرامش نمی‌بیند.
سپاه در این بیانیه از حمایت جمهوری اسلامی از «محور مقاومت» تاکید کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75776" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YCja4XVSenFwHNTGG4FOwKDQkVAwD6nO8BtsaUjcGl9vd_20AByD1FBYAYAdl7uyeH0Sq6WX-onpDDfbiqyQaLpEr4qCb8bZ1cN3TppC260o0jVxXR8JzCXoBNzsa79ISLzEcrZhVtJ5sHwtWPE8UWRJmeOztwf_336rRD7R3QBvK7aMs23mWgDGeK5DlsBrLseuufu2xPh2uLndYOLAqVj9jE_l-Coezaq0E5KQjhJ3IfPwEHhPQLCwnYH8KxuklCu7jY0i0T2nN0RdIip1yzqyi00xaZOWmlP9zBoDnGXzDcQAQD8Qpdql7LLK_K-1iYHn16bxqwpKo0eF0Ehjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qe1s3LlrnGVEwYOPFDrw8c_swXpq560GIpwBNxzh8ut-6hJkji8An7tUQAAe-Lj2laWCfpqwVjTbuQeLEyhFJrFYmCzkzgI3uEuUQEYxSS8AUghdotODkLgF5y4YP4MmHbU7nTIJOTW6ljDZIdbjEK0uansPYvY9jnQ4ABHBenlsiSoWxJEJkdJsF3zcH6y0vrqYL7Dqi2bBMn_FJufjvPnESCnCBhW7EmjVjUsPdnZ9p2zFy5vrI5OfCvsLaZIMpi2tP9yZ3WTjEiPrOaoG_ClJZtegO0wsxmnr9q9Xx-TbcM1pAt33xsNDix9a1DXD-LqJum55rpBKgsbiHNrGUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنج‌شنبه در پیامی در شبکه ایکس نوشت که ایالات متحده در راستای افزایش فشار بر تهران و باز نگه داشتن تنگه هرمز «دسترسی هر دو شرکت هواپیمایی ایرانی به اماکن فرود، سوخت‌گیری و فروش بلیت را متوقف خواهد کرد»، اما جزئیات بیشتری ارائه نداد و به نام دو شرکت اشاره نکرد.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، با تاکید بر اینکه این کشور به کارزار «خشم اقتصادی» علیه حکومت ایران ادامه می‌دهد، در شبکه ایکس نوشت نیروهای جمهوری اسلامی حقوق دریافت نمی‌کنند، پلیس‌ها سر کار حاضر نمی‌شوند و جزیره خارک تعطیل شده است و اقتصاد و ارزش پول ایران در سقوط آزاد قرار دارد.
او افزود سازمان مدیریت تنگه هرمز از سوی جمهوری اسلامی یک شوخی است و امروز وزارت خزانه‌داری آن را تحریم کرده است. ما به هر نهاد شرکتی یا دولتی درباره پرداخت عوارض یا پنهان کردن آن به‌عنوان کمک هشدار داده‌ایم.
بسنت اضافه کرد با تشکیل «دیوار فولادی»، محاصره دریایی آمریکا باعث شده میزان نفت خام ایران در دریا به پایین‌ترین سطح تاریخی برسد.
او تاکید کرد تنها یک نتیجه رضایت‌بخش در مذاکرات این روند نزولی را متوقف خواهد کرد.
@
VahidOOnLine
دولت دونالد ترامپ نهاد موسوم به «سازمان تنگه خلیج فارس» جمهوری اسلامی را تحریم کرد
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75774" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lXGMjTwxKyf-bqodQpgR7HNkZVOr7X6aVP9K6k562iFPT6qowEDqRbbVWiW4yodt2vdngJ0mNnrFCETHAd82QZQ9coLPqJKUjiMpvUiYYNrwQUttcxmAgjfmPPnlzoBFUff92dby7XMoyTsAN7dPLmViqClR0RwCcHV8D0zUe7OfG7LINI6bIZre1GFwWSXS1ricPbWsxwUZhGCi7mjLbW3DJ5dgBbU_83PcibuxVUsWp3zMJ36CCItOy8D80bmJyJSuA-_xo7zhWAgILl9b22vYArLxFRfGlrOqMCVTunp4C-w58qrC5v20aitmTzMk3HOEs2ja6ePOR0ztzYNSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H_hrF6TC0c7kur6KuXaLSqQFibNHq_OKplpQ7FVHKbwhrxQhN8hb8hGE8RnWiBvpKnJKLzJpYwQ5sRxaMg8i4WZXBXBdLKLzDk67MYfgph6puVoVmoGu6TnuD9xkUHtQm_44IArAdK0xOlxaedjobfLsEZIR_nZ1DfYAZqjr1qQntMOyG4nVItgqhrDiKEGECdFrouXWzsNziF7Ffk3i6uCmwM9-cph_5kW46eTQSRsuwOcYf6f-3T2rArcpU7gIkk7qkYbu4dD3_JL15JXjZ6ceVq0OlhJ3DqRrVIG6FV9GKXL0Zan4_skhVOgJPrpjbTJPavnFXPgZEwyL0rnAUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خارجه کویت حملات اخیر موشکی و پهپادی رژیم ایران به خاک کویت را به عنوان یک تشدید تنش جدی و نقض آشکار حاکمیت و امنیت محکوم کرد.
این وزارتخانه روز پنج‌شنبه اعلام کرد که تهران را کاملاً مسئول حملات اخیر می‌داند و حکومت ایران خواست فوراً و بدون قید و شرط حملات را متوقف کند.
@
VahidHeadline
اسماعیل بقائی سخنگوی وزارت خارجه ایران، حمله بامداد پنج‌شنبه آمریکا به مناطقی در بندرعباس، را «تجاوز» نامید و آن را محکوم کرد.
آقای بقائی این حمله را «نقض فاحش حقوق بین‌الملل و منشور ملل متحد» دانست و افزود: «شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخگو کردن متجاوزان آمریکایی است.»
سخنگوی وزارت خارجه ایران می‌گوید آمریکا «به‌طور مستمر»، آتش‌بس میان دو کشور را که از ۱۹ فروردین اجرایی شده، «نقض» می‌کند.
سنتکام با این حال تأکید کرده که این اقدامات «سنجیده، صرفاً دفاعی و با هدف حفظ آتش‌بس» انجام شد. این دومین بار در سه روز گذشته بود که آمریکا اهدافی را در ایران هدف حمله قرار داد.
@
VahidHeadline
فرماندهی مرکزی ارتش ایالات متحده، سنتکام، حمله موشکی ایران به کویت را «نفض فاحش» آتش‌بس خوانده است.
این نهاد در حساب رسمی خود در شبکه ایکس نوشته است: «ساعت ۱۰:۱۷ شب به وقت شرق آمریکا در تاریخ ۲۷ مه، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.»
سنتکام نوشته است «این نقض فاحش آتش‌بس توسط رژیم ایران، ساعاتی پس از آن رخ داد که نیروهای ایرانی پنج پهپاد تهاجمی یک‌طرفه را شلیک کردند که تهدیدی آشکار در تنگه هرمز و نزدیکی آن ایجاد کردند.»
فرماندهی مرکزی ارتش آمریکا می‌گوید: «تمام پهپادها با موفقیت توسط نیروهای آمریکایی رهگیری شدند و آنها همچنین از پرتاب ششمین پهپاد از یک سایت کنترل زمینی ایران در بندرعباس جلوگیری کردند.»
سنتکام در ادامه آورده است: «فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای کماکان هوشیار و محتاط هستند و ما همچنان به دفاع از نیروها و منافع خود در برابر تجاوز توجیه‌ناپذیر ایران ادامه می‌دهیم.»
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای در شبکه ایکس، حملات خصمانه با موشک و پهپاد به کویت را به‌شدت محکوم و تقبیح کرد.
@
VahidOOnLine
وزارت خارجه قطر در بیانیه‌ای هدف قرار گرفتن کویت با موشک و پهپاد را به‌شدت محکوم کرد و آن را «نقض آشکار حاکمیت» این کشور و «نقض فاحش قوانین بین‌المللی» دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75772" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmggxzoIKq5ilbbUATb57KMIfqyxfvvik9iseXyfOfAZhQWsFxr0Jwjbrdw-IkQBvcwKKH1QNdoHb4CCA4L-Y_NomTJF7z0xiZuBPvhp3miy_QfQdYBhg09ObCnv8n9CjhJf-ShH4Ua_autMs2rb1LhV5x4vYIOeDZFQ3GpgF9lE9n0AZeGjEd52LX8Ig0kBpJ7aRKLcn8-Vc6u89B0jGExK_SkMKdTeXshEwfOPzpOa5FucM6Ci0fa43QMKx48VRMZUQtREMjcHc9HJ6wIxLHiJ-ljPDZK6aaHnefnvJdbW4OBksVM2nEPaLzbDXgWA4bh3gyc89u9cbXsPWBSSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را خطاب به نمایندگان مجلس شورای اسلامی منتشر کردند که در آن می‌گوید «ایجاد تفرقه و تجزیه اجتماعی»، در کنار جنگ و فشار اقتصادی و محاصره، «طرح و نقشهٔ کور دشمن» است.
مجتبی خامنه‌ای در این پیام که روز پنجشنبه هفتم خرداد منتشر شد، همچنین به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داد که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
وزارت اطلاعات جمهوری اسلامی روز گذشته در بیانیه‌ای هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
وال‌استریت جورنال نیز روز پنجشنبه در گزارشی به نقل از تحلیلگران هشدار داد که ادامهٔ محاصرهٔ دریایی آمریکا علیه ایران که به کاهش ذخایر ارزی ایران انجامیده، می‌تواند احتمال بروز اعتراضات جدید در ایران را افزایش دهد.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75771" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f525YjOfgZKX2KYU709n6IBFpPovbSsUf1LkwKmSUzeA9PETh-1gys9pl8tTIxd2vKxHk9ApYqWD0FYq8ucG_4ZnYnrdN8QfzXUQGsL5bCHPYrp4JZZ_e53-MtvjcADQcz4rxjFddx5eRKRa2YRznGGMo2pCHPenSPiIhmvfZBQQ5bdkyygGdsWm7FJm6jq2vz6h5uL7Mps-aSU2LoWGoNA18vNraYTQExBuvagSh2mlTfGK_tkn0kf-1pznnELSWUXXVjEEJkx52NX-UfZKaBBE9xLhRHC_ifQBlc3pSm87Z4K3KXlQ2PagNKJVuUnO__gw_r6bM51q_Q9qHvETDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری آمریکا اعلام کرد «جاناتان لودهولت»، شهروند آمریکایی ساکن استاتن آیلند، به‌دلیل مشارکت در طرح «تعقیب و قتل» مسیح علی‌نژاد، فعال سیاسی ایرانی-آمریکایی، به ۱۰ سال زندان و سه سال آزادی تحت نظارت محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75770" target="_blank">📅 18:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hRAsJjyn9yodZvlkSXu9PmhiJl5JpCUh5csLhH4CSWoHlLiEXaLu6ke6a0bYfubiBDpR8oOWx5Y7GA4G4HStRs8VWK9qNhjcmAmGecqmD_o7EmuMAP-pqI-CS_fLG28q6ssJdqOJ-BZA-v1THPwssrWDRvkTPV4da7q65LmC4R3iJ2IB7jJejyd88QHoFRGfGY5gU0A6aQXvFG6mG_DcD8AL_AT6A5OoveYQ5SNyxI6ycHk1qqu0r2ThafbGyAcXdaN65dfiePd0SLOe-i3qm2qB6cwsX-ttsQCswjf-jUYAS8CqMFdNT3WgFigTOgyt9BiTPf2UKAHl_P_IvKWOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، در پیامی به «غلامحسین محسنی اژه‌ای»، رییس قوه قضاییه نوشت: «قوه قضاییه زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد با قاتلان داخلی و خائنین به ملت نکشید و خوش درخشید.»
این تمجید از عملکرد قوه قضاییه درحالی صورت گرفته که در طول روزهایی که از جنگ ایران با آمریکا و اسراییل می‌گذرد دستکم ۳۹زندانی سیاسی اعدام شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75769" target="_blank">📅 18:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0SOqvxmzZZG_m-UKzv4wWgGuG9oQlEGT0UV3DcSZQLfa7YDbrMthOI_SWXRTBpR8uT8l0xAs_xhqEoNvO_bx78HNcTgIVUU8uwuNQuMwqgFC6HIsTeRdjnK-ha0crPlvg4-NbqhwKdS1zurE2ex9Pj8jkWd-hn4XLGieJbpdPASgHsnwTOGDs16fLQb8FIFaoVBgxbHW0rclLiJ6Fy98fciYulHfEOJHkE-F6yfaVDOWv_yLj1De7Ed5lWSi0u8I-9o1RAQRu47GRXE9dwYbmcCSuyJv6AnMMUvOCfL-gQr9kOzSJQKJstGtRWKvG7KT5Z3ZsvT4wnQrClOIy3PLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس، نهاد ناظر بر اختلالات اینترنتی، اعلام کرد که علیرغم اینکه دسترسی به شبکه جهانی تا حد زیادی در ایران بازگشته است، اما شاخص‌ها نشان می‌دهند که کاربران همچنان با فیلترینگ شدید مواجه هستند.
نت‌بلاکس، این فیلترینگ شدید را مشابه دوره مابین اعتراضات سراسری دی ماه و آغاز عملیات نظامی علیه جمهوری اسلامی، حدفاصل دی ماه تا اسفند ۱۴۰۴ توصیف کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75768" target="_blank">📅 18:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2pR8g8Aq0Z4chreZrEK3_1C-s2CEMTOvDEAML6UHeXwqGoCaJwR_5QIzZuPTVr4EXoG9JWuOHA6ef9q_VaXChfuJf-u77vdlZXKUKl7lhRGvV6hnRVhUbO0hBGGVFqI-GeA-3sKxVed9x7_86n8AT84hOBDW9btSJEQCcS578r_VLpqRVHN6gbpK-PGYT7GfhYNVhKpe1SXrejza1Tv7-W1JDBGm-o9pq6JC5NLRdN5KzP9i_m1dOkCEBnBV-w6jEHWLJMgk75uzp3WzgP6ROwh7kyf9dUsN7IaI8NUlt4k8uIl0mJ4HnpAEdF7Io5OTiGg79FTdZV_MG7MJk5zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر پیکرهای بی‌جان و شیون مادر  تصاویر دریافتی از: 'بیمارستان الغدیر #تهران، بامداد جمعه ۱۹ دی' Vahid #بیمارسان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75767" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=cpet9meQ8sMbXFBOVfIZdqby-Ay4FC574bBJxVCJfxICIJNjo7RbBwXHzHaUaLZ0og9Slr1iFL5dNfNx6nm_QtTXYJwOilWhCJRmcmTXlyOAScXsA5urlp_LX1gchSwweBF8H733L7_osIM3YQLG41Emgu3htCZkIyGp81rWie4UfeQlGijWkUOnfK0uyeokoBzhWVMJwiKQiVObaaCoaGGYTs2kFkvNJMIWBEY7iRJ1qHv-TglADeDHobFSxtz3VsDIwS_WpUfZvX-eN8645f2cvPtZ8oRjPy9mhjH7rEqZYU3eiF4xfjtGAgpWptnHT45AZMpRXQK0JrccJg-7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=cpet9meQ8sMbXFBOVfIZdqby-Ay4FC574bBJxVCJfxICIJNjo7RbBwXHzHaUaLZ0og9Slr1iFL5dNfNx6nm_QtTXYJwOilWhCJRmcmTXlyOAScXsA5urlp_LX1gchSwweBF8H733L7_osIM3YQLG41Emgu3htCZkIyGp81rWie4UfeQlGijWkUOnfK0uyeokoBzhWVMJwiKQiVObaaCoaGGYTs2kFkvNJMIWBEY7iRJ1qHv-TglADeDHobFSxtz3VsDIwS_WpUfZvX-eN8645f2cvPtZ8oRjPy9mhjH7rEqZYU3eiF4xfjtGAgpWptnHT45AZMpRXQK0JrccJg-7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'رد موشک شلیک شده در آسمان
#امیدیه
خوزستان، پنج‌شنبه ۷ خرداد'
Vahid
☄️
سپاه اعلام کرد در واکنش به حمله‌های پرتابه‌های هوایی آمریکا در سحرگاه پنج‌شنبه به نقطه‌ای در حاشیه فرودگاه بندرعباس، یک پایگاه هوایی آمریکا را که مبدا این حملات بود در ساعت ۴:۵۰ هدف قرار داده است.
سپاه تاکید کرد در صورت تکرار حمله‌های آمریکا، پاسخ جمهوری اسلامی «قاطع‌تر» خواهد بود.
@
VahidOOnLine
رسانه‌هایی که بیانیه سپاه رو نقل کردند، از جمله خبرگزاری رسمی جمهوری اسلامی، ایرنا، نوشتند "ساعت ۴/۵۰" حمله کردند که یعنی چهار و نیم ولی با توجه به اینکه با دو رقم اعشار نوشتند احتمالا منظورشون چهار و پنجاه دقیقه بوده.
اما این هم عجیبه چون آژیر در کویت و پیام‌ها از امیدیه مربوط به ساعت ۵:۵۰ بودند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/75766" target="_blank">📅 06:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZzlnulAUiOrkJqj-T9voXbHtPkbjBJ5U5OzzaVmNoSCTzQzejG_Wh6_BlTzFCMhLyC5iuz-0_UjNFGfsFWcUQVxuMYUYCGClLoo2dHTkJ6QLA3MQXkd4Ew9eM89fgPRa6rGqW1E39msApvU0Qcjl0sgzKcqJaxxls4IhfdSzSfT-alUeceeqqpXcrGmoE7Oz8ZxlMcdgA1aT0prwjy44xl74tqh40Q0i_EAcOGo_Wwq2p1UfA--CFv44O4PecGyqqGg74yAnsfZTRrOPTYZTp9NRMf8tfg8s97N3vV54780o8eMQVZXVhrGEGk7-9EnZLiQHUx6PgGPHwYWo593MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HAUnL4xtUjC8noMjMwKQUR9bFYTRe9AHt4XziWYR1ImZ_6NXr44efoyTLA2UgoxmIovP43DqwXPZdmN8K0Wrydrn3SwJlErNvcMAlSVJB5yog_DNdKDUZVD34GRfoR5TLv0jjHDoTPli2gxnAA7B_qrGwZYN-W7qnYdzOmC759rBaMx6emPLgyvJ55TycvdYk4ZwcrkzZgoWAgpgceoj2ptuAhGG0XMZ3mKhI2sSox1SeRHNaJCfM6HS0CM7oKyPPn2NucgLhemDS2W-0wjmCNVOfC5dKY3aqQ1U33BO2Y0D1buTUUeoM4r-kciTfXYndmcfnGw-5zyzcFOTdyVV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b9tBiCCi2WzCRO2F7w-USyXCY_SXaq1_amBQptRt1JbQhcx7kbhhh6-cye2SL-gqnnA6pt4Cj7VktH-dSL3L069LaH9FoXQPzaGG8dAOIgkimOeBEZUKnBRiKTQw2uvJpHuMWKL6oT00L307OTORiPzBYdu6Jl1CuN7MCZYIjQ02ORACWzrNuwMN8LvgApwQlO7qbeHicF-ogAqVjQ_GX0qALBg-fzIDGfQjsEefxgRPrbeU_ntLcEkqAd_k-jQJvb4N7vEXdAw6X4InnHcEL3SJ4bXi4mDyyrULDpV4SAe30g8AZ7oa0UPapK2mTRudNetNbZ-2Thmvb0D5QUnK_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از
#امیدیه
در خوزستان پیام‌ها و تصاویری دریافت می‌کنم  که میگن حدود ساعت ۵:۵۰ موشکی شلیک شده و سمت تونل امیدیه میانکوه صدای انفجاری شنیده شده.
یکی نوشته لانچر هدف گرفته شده.
دقیقا میشه هم‌زمان با
شنیده شدن آژیر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/75763" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfPCdM_2tih_0sagu_NE29N7HvVv-bpdO2R4XmCZjprwaKRQJpezKMJ557bLp4jO7HRDXXw3Po7L6eau2D15Xt5bH1JoKTTlhol-1SwmFD7VjiymgHS1xYi78yQqWvEjVSzbi8or-AqNFRKJwABEZN28so4-dFYGCVXWpNeDBvyQwVI7SJI4kHYoNKrtmbAnJowKjyGxtYSoH_1C3-DRQcIPpBqTSsuOoYQYa9_2jnryYB9-Br_IF5nUBDNiV72RPY1QGlRy8YM3VL03zjinf5VpoRuHupsKdTIJpdFduI3EWxkmxoMXSmZP_S5Jzcnr3dLPN2D9tNP0TrAuzF1BhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید الان کویت رو زد ۵/۲۰
وحيد همين الان اژير كويت فعال شد
سلام صدای پدافند و تقریبا ۲ تا انفجار در کویت
درود وحید
🙋🏻‍♂️
اینجا ساعت ۵:۲۰ به وقت کویت صدای اژیر اومد و رو گوشی ها هشدار اومد
ولی هنوز هیچ رسانه‌ی کویتیی دلیل این اتفاقو نگفته
آپدیت:
ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور حملات موشکی و پهپادی «متخاصم» را رهگیری کرده‌اند، اما مشخص نکرد این تهدیدها از کجا منشأ گرفته‌اند.
ارتش کویت در بیانیه‌ای اعلام کرد صداهای انفجاری که در کشور شنیده شده است، ناشی از رهگیری این تهدیدها توسط سامانه‌های دفاع هوایی بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/75762" target="_blank">📅 05:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jeXzmQsE57BKiH8Aa5-kqWmpcqr8LgmYaeP29HcpmNfNVkQ2SBoFSOGOSCoflFq5isvUz7rbnQ92Le_l85IxFffmmc5gL52ttWMSRtahsi6J7jCzxvVHZelBpGiTE8dIM5EOIQGKBxuO49_5vnZUQsXH5idT8IzaGxkVmHE7j9OlwFeEHTdKMnt6198TeEmoT-3QWXlZyJfTvRriz62OUOydvCOlOhFPoZCENePOMANbb_bBdIRunHY1va5ZCvWbbtRvrF-KCEumT_DGnmW1eqh48eapyvP8pwZUPoiHXOrAPIyktv8XXeAWF8cIe42qRx4eByX28zL-n15mA5XADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسوشیتدپرس به نقل از مقامات آمریکایی گزارش داد که نیروهای فرماندهی مرکزی آمریکا چهار پهپاد تهاجمی یک‌طرفه ایران را که در نزدیکی تنگه هرمز تهدیدی ایجاد کرده بودند سرنگون کردند و یک ایستگاه کنترل زمینی را در بندر عباس هدف گرفتند که در آستانه پرتاب پنجمین پهپاد بود.
@
VahidOOnLine
در همین حال، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، به نقل از یک منبع آگاه نوشت: «ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.»
تسنیم درباره حمله هوایی آمریکا به نقاطی در شرق بندرعباس نوشته نیروهای آمریکایی «به زمین سوخته‌ای در اطراف بندرعباس شلیک کرد که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75761" target="_blank">📅 03:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی:
چهار تا صدای انفجار پشت سر هم اومد الان
ساعت ۱:۳۳ بندرعباس
درود آقا وحید همین الان سه تا صدای انفجار اومد تو بندرعباس ساعت ۱:۳۳ دقیقه
حاجی صدای انفجار دوباره شرق بندرعباس همین حالا  سه تا پشت سر هم ساعت1/43 دقیقه
سلام وحید
۰۱:۳۳ شب
همین الان بندرعباس صدای ۳ تا انفجار اومد
سمت بهشت بندر
احتمالا باز مثل سری قبل باند فرودگاهه
بندرعباس ساعت ۱:۳۰ هفتم خرداد صدای جنگنده بعدش سه تا صدا انفجار اومد
سه تا انفجار بندرعباس
ساعت 1 و 33 دقیقه بامداد پنجشنبه 7 خرداد صدای سه تا انفجار رو از بندر عباس کس دیگه ای هم گزارش کرده ؟
شبیه صدای موشک زمین به هوا بود
بندرعباس صدا اومد
سه بار
درود. ساعت ۱:۳۲ دقیقه صدای سه انفجار شدید در بندرعباس اومد و خونه شدید لرزید.
ساعت ۱:۴۷ باز هم صدای دو انفجار دیگه اومد
صدای سه انفجار بندرعباس همین الان
سلام وحید جان بندرعباس چند انفجار وحشتناک پنجره خونه لرزید 1.38
دباره زدن بندرعباس ساعت 1.49
۳تا صدای انفجار بعد صدای پدافند
سه انفجار پشت سر هم و یکی هم ده دقیقه بعدش بندرعباس رخ داده
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/75760" target="_blank">📅 01:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAggGfDFmaqdyo5U9_atGhbQn2sikM4ZkR1mij0gfeQTm97hyFJbR7EdIqIXSBwqV-TUOCm_HJHoci4CrEk9OsMLFm5YBm838_vyqCp4ofdK2PfM98WXMP8I5Hub03Fj0BSAf3g3aRCMwKQN4_Cfh673uF7ScHNIII3u1LKEDOtEU5fSatvefLczB96RMv1PxG1JY4l-7686t5Y6wIb5nVVVc5YVbNpI14qoucLi_hlWTCErMD5mmteObaeJRJ6odywYxC9ERSAI35-oJMCC0rxo_DDHXpW0p5y6-t5NAs65FQ0Y1vvBi3GVlToSp4M5Dh4ykcsj4tYzNPXMp6088g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=FbyUFtUdJ0IGFwyzndSMJsZ4rNGMbVX4Fg2NSuD8f1weLFJdPutzZJ4wMGv-uMEQ8YHenPdDiA3hFdmSA6hmXzcFx_BQfddEWEfrnBLzsIY5W9wv5aR4UT5RZeeZQrUTiOraNuKov7TXVrepkWJtYL-Sq4VpcCUPgmtOZSsHj9l4TuGc43H-CW3IuKfKcHwZzfGVHWgHxe_tTnLvI_fvvJn15bg2vyAK7ejKBBKn4vYZjT27HnAwzvxYSzruMA3v5Pd1V_1XhckYrYJUpfZs8Y-NHzm0itEtsep2gfL4peFTZHG_cziztr1A0JlBlpGDQsmLu8-ciK_y67Po1Sxd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=FbyUFtUdJ0IGFwyzndSMJsZ4rNGMbVX4Fg2NSuD8f1weLFJdPutzZJ4wMGv-uMEQ8YHenPdDiA3hFdmSA6hmXzcFx_BQfddEWEfrnBLzsIY5W9wv5aR4UT5RZeeZQrUTiOraNuKov7TXVrepkWJtYL-Sq4VpcCUPgmtOZSsHj9l4TuGc43H-CW3IuKfKcHwZzfGVHWgHxe_tTnLvI_fvvJn15bg2vyAK7ejKBBKn4vYZjT27HnAwzvxYSzruMA3v5Pd1V_1XhckYrYJUpfZs8Y-NHzm0itEtsep2gfL4peFTZHG_cziztr1A0JlBlpGDQsmLu8-ciK_y67Po1Sxd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره لغو یا کاهش تحریم‌های جمهوری اسلامی گفت واشینگتن «درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول» صحبت نمی‌کند و تاکید کرد: «هیچ تحریمی، هیچ پولی، هیچ چیزی.»
او افزود آمریکا کنترل پولی را که جمهوری اسلامی ادعا می‌کند متعلق به خود است در اختیار دارد و این کنترل را حفظ خواهد کرد. ترامپ گفت زمانی که جمهوری اسلامی «رفتار درستی» داشته باشد و «کار درست را انجام دهد»، اجازه دسترسی به این پول داده خواهد شد، اما «در حال حاضر چنین کاری انجام نمی‌دهیم» و «این دو موضوع به هم وابسته نیستند.»
ترامپ همچنین درباره انتقال اورانیوم غنی‌شده گفت با انتقال ذخایر اورانیوم غنی‌شده ایران به روسیه یا چین موافق نیست.
@
VahidOOnLine
دونالد ترامپ در پاسخ به سوالی درباره کنترل تنگه هرمز توسط تهران و عمان گفت این تنگه برای همه باز خواهد بود و آب‌های بین‌المللی محسوب می‌شود. او تاکید کرد هیچ‌کس آن را کنترل نخواهد کرد و آمریکا بر آن نظارت خواهد داشت.
ترامپ افزود کنترل تنگه بخشی از مذاکرات است و ایران تمایل دارد آن را در اختیار بگیرد، اما چنین اتفاقی نخواهد افتاد. او درباره عمان نیز گفت این کشور مانند دیگران رفتار خواهد کرد و در غیر این صورت آمریکا مجبور خواهد شد آن‌ها را منفجر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/75758" target="_blank">📅 21:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fssbIwtuj6rWoI3cwnaJAjavENwS0tQDtUOSbTr1b5aL2YeN48yt3vlqxyOJpwWDSkpKjkoJVB4x8RTPsL-1rjYB3IXFkdazwVF8-pDCq_BKwsRZYgfiOdq_faTZoG8ssE-DbGVfxXlyLQ_QY_fL0KyxPdshJj5dhTxWjAhvISOBWQhaG2Hty-i8GWamWTUqRQcaLQ_XZZNx14zkquOCkYZnhOyIzF2HLWWByP-p2OAKqIQBXcU1UXC-kpROvN0M6cNckGKEOauDgnBz0-VtveDEYFE0VNUWOoY5npLxZO5kGvH4leYRJ2H_RfM-Y2z9Lc1Xgl_CIEy8eFe0fxKOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه گفت که ایران در ازای کنار گذاشتن اورانیوم با غنای بالای خود، از لغو تحریم‌ها توسط واشینگتن برخوردار نخواهد شد و از پیشنهادات ایران برای توافق پایان جنگ ابراز نارضایتی کرد.
ترامپ پیش از برگزاری جلسه کابینه خود در یک تماس تلفنی کوتاه با شبکه پی‌بی‌اس نیوز، در پاسخ به این سوال که آیا توافق فعلی به این معناست که ایران در ازای لغو تحریم‌ها، اورانیوم با غنای بالای خود را واگذار خواهد کرد، گفت: «نه، نه، اصلاً. خبری از لغو تحریم‌ها نیست، نه.»
او اضافه کرد: «آن‌ها قرار است اورانیوم با غنای بالای خود را کنار بگذارند، نه در ازای لغو تحریم‌ها. نه، نه، اصلاً.»
ایران بیش از ۴۰۰ کیلو اورانیوم غنی شده تا حد ۶۰ درصد دارد که در تأسیسات زیرزمینی هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون است.
رئیس‌جمهور ایالات متحده ساعتی بعد در ابتدای نشست کابینه خود در کاخ سفید گفت که ایران بسیار مایل است به توافق برسد، اما آمریکا هنوز از توافق پیشنهادی رضایت ندارد.
ترامپ در این نشست در حضور خبرنگاران گفت: «ایران خیلی مصمم است، آن‌ها خیلی می‌خواهند که به توافق برسند. تا اینجا هنوز موفق نشده‌اند... ما از آن راضی نیستیم، اما خواهیم شد.»
او سپس بار دیگر ایران را به ازسرگیری حملات نظامی تهدید کرد: «یا به آن نقطه می‌رسیم، یا اینکه مجبور می‌شویم کار را یکسره کنیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/75757" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rJaB6EOs75iQPZn6GDTz8REAj7QuCsbUblD2weJs3j9mHAvzi0jxa67o7i2TWdmrE8KOga_84o5siKCE-5ZYvh0kTfYU6HUHT-WQavaI6w0byD_9CpEPNKLMMit7wbwHwj4HjgtR_Yv7AX8q5xPA2PR6xVYrtNKAUpG8h1bgcQ_x3XaqP-F2GLSNS-VhNmKr96U1MYHfzMkZXwsglHX90fNOmqrVo518wA9iGZKsHPVeCEK1viTLTReUFF8JPFy-AlYZlGYSKCkdutfItOr4t2FCH_LPZfWZtCcD4NuyVGojxCgrqZ7tDl31gMmU8uepuK34cqbERkdvAXWNzefR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر دلخراش از اجساد مردم کشته‌شده در بیمارستان تهرانپارس تهران
⚠️
دو روز پیش ویدیوی دوم رو با تردید منتشر کرده بودم و نوشته بودم نمی‌دونم درسته یا نه. حالا عکس‌هایی از بیمارستان تهرانپارس با شرح جان‌باختگان ۱۸ و ۱۹ دی دریافت کردم که نشون میدن اون ویدیو…</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75756" target="_blank">📅 20:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=lZbPX0fW2ineqpWCYopUP2Xa8dLBslgnSR6Dw_rTJSYJmodi_AZF6wCgGwgmafWdTnWFaHY3GtxqMxkTXzBbF_ea2ddHrhqwuM3En9-_My2elkfEc1F95iPDIne68pXGUS9YkV8zvitu9ZQzFmGImrx1JOrM6bh4yAc4HhMGE84u-4uPWbZrfVBcoDOInEJo870qAz3aDFvDCmmKb04zH4uJSdnLLfyOqwbAmR2O61nr0p9o_5CFw88CXuIgFv-bmiop5RHYjDaGqvRZjBkV2YB_3QadRdrsetOhNEENSG8AzhMKQynujIuJvtU1mCqPsO9YIdWgtVR9elPOV85EAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=lZbPX0fW2ineqpWCYopUP2Xa8dLBslgnSR6Dw_rTJSYJmodi_AZF6wCgGwgmafWdTnWFaHY3GtxqMxkTXzBbF_ea2ddHrhqwuM3En9-_My2elkfEc1F95iPDIne68pXGUS9YkV8zvitu9ZQzFmGImrx1JOrM6bh4yAc4HhMGE84u-4uPWbZrfVBcoDOInEJo870qAz3aDFvDCmmKb04zH4uJSdnLLfyOqwbAmR2O61nr0p9o_5CFw88CXuIgFv-bmiop5RHYjDaGqvRZjBkV2YB_3QadRdrsetOhNEENSG8AzhMKQynujIuJvtU1mCqPsO9YIdWgtVR9elPOV85EAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد، در نشست کابینه در کاخ سفید درباره مذاکرات با جمهوری اسلامی گفت تهران «بسیار مشتاق» توافق است، اما مذاکرات هنوز به نتیجه نهایی نرسیده است.
ترامپ گفت: ما از وضعیت فعلی راضی نیستیم ولی خواهیم شد.
رئیس‌جمهوری آمریکا همچنین جمهوری اسلامی را تحت فشار شدید توصیف کرد و گفت: «نیروی دریایی‌شان نابود شده، نیروی هوایی از بین رفته و همه‌چیزشان از دست رفته است.»
ترامپ افزود جمهوری اسلامی «در حالی مذاکره می‌کند که چیزی برایش باقی نمانده» و هشدار داد اگر توافق حاصل نشود، آمریکا ممکن است «برگردد و کار را تمام کند.»
ترامپ گفت: «آنها تازه دوباره به اینترنت برگشته‌اند، چون به‌شدت تحت فشار قرار گرفته‌اند.»
او همچنین گفت اقتصاد ایران «در حال سقوط آزاد» است و تهران به‌دلیل فشارهای سنگین، گزینه دیگری جز حرکت به‌سوی توافق ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75755" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری فارس به نقل از «منابع آگاه» گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، ممکن است در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق میان ایران و آمریکا نهایی شده است؛ اقدامی که به گفته این منابع می‌تواند با هدف اعمال فشار سیاسی و اثرگذاری بر افکار عمومی انجام شود، پیش از آنکه اختلافات باقی‌مانده به‌طور کامل برطرف شود.
بر اساس این گزارش، این سناریو در حالی مطرح شده که هنوز برخی موضوعات میان دو طرف حل‌نشده باقی مانده و روند مذاکرات به مرحله نهایی نرسیده است.
در همین زمینه، یک عضو تیم مذاکره‌کننده ایرانی در گفتگو با فارس تاکید کرده است که تا زمانی که همه موارد مورد نظر ایران حل و فصل نشود، هیچ توافقی قابل اعلام نخواهد بود.
به گفته این منبع، جمهوری اسلامی ایران تنها در صورتی که اختلافات به‌طور کامل برطرف شود، نتیجه مذاکرات را به‌صورت رسمی اعلام خواهد کرد و هیچ توافقی پیش از رسیدن به جمع‌بندی نهایی، مورد تایید تهران نخواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75753" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ffgNVr8IcoKbnMdk5fQyj9cbX0mEWXlCf0soI-CDZCvTjFBUV9-gw4cu-6K_u8tBO0t5ToxMVQuasSSF72xTkhVpBbMw2UqbkTA6t77VYOdvfCpmzK8j4cyxsVkjmTRX8U1JyvqAcIBhZYpsOl4JzD6R2VtWH3Buwm0qZciwiuutBOaIN6YBoYgXLv0gcIyTuD8Dn9VoOQLskRr79mqkcGeYrc76G608qbDVu0NNC2PGT7QiePjH7SacMqgJdqyIH0M1jIWrETURGdRwo2x-ET2byejEJDJ-ltleoACK_SaNuc--dVYte5kQ_qFmQpTCDOsLAlvWB7GOOTkqlmIszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=J1rhsCqR4YnM6rzD4fIyDcXtp0jaJ9ij2bqaA1VIljPq-M60OlVgv6EjKEorpWK1bQFgrVZcOrJnCLOwFpignIoKc4-pjsC_qhILfJLrRwPsnKpX51dFfIUPtZwkHF_EfYsmUI_KGBfc9UAf-UQcr-xqyH1LZE9YL3XhoW4Avc0IWLlJX3kBrq1UUoHMl4y97e9Gt9y7KrcUVerrcD-SMM_h26opptGT3BnXDmV7Sus6tStEC1oai93LT3kV_-WuRafFSVSx9GkKhS0GScmmkDBxSBQwuNriEYQdVDDyV5omolS3fLJykDzwFy_2zIB40bNp8-uini4j1q2I25qOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=J1rhsCqR4YnM6rzD4fIyDcXtp0jaJ9ij2bqaA1VIljPq-M60OlVgv6EjKEorpWK1bQFgrVZcOrJnCLOwFpignIoKc4-pjsC_qhILfJLrRwPsnKpX51dFfIUPtZwkHF_EfYsmUI_KGBfc9UAf-UQcr-xqyH1LZE9YL3XhoW4Avc0IWLlJX3kBrq1UUoHMl4y97e9Gt9y7KrcUVerrcD-SMM_h26opptGT3BnXDmV7Sus6tStEC1oai93LT3kV_-WuRafFSVSx9GkKhS0GScmmkDBxSBQwuNriEYQdVDDyV5omolS3fLJykDzwFy_2zIB40bNp8-uini4j1q2I25qOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آتش‌سوزی
در یکی از برج‌های مجتمع مسکونی پامچال در چیتگر
#تهران
تصاویر دریافتی + منتشرشده، چهارشنبه ۶ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75749" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPdI09hCaDRkyyUkac7WkF6FqKOoa7GW6qlNspMSGZ9iwrM4m8DxdMKYIXrkljuC55b74rSCHNSvaUxIcBLvdiRVa7ar3yvcp-TtYjyDrbA7-shwjRHmBGQsRiXlyPUaGhLspyHtieINDJK8BGDAEhYWbExygg1zFy9NIHvwZpwQHLIMi6d7NyprPyHyjraye929o4IbCYrJdIFu1sGLyU-hRBB03yWM5Qcqv5bDggWTRUOVYmzXOLl3HxBoMbevfkBRGxMnyKXrfZGm4YBUyYP3LQsMgUUZo6GrmjqT7oxYHYnfV2_nHiLiet8noBEaZXIFX6N1qGCZkx8sQZ8RBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید روز چهارشنبه اعلام کرد گزارشی که از سوی صداوسیمای جمهوری اسلامی منتشر شده و به پیش‌نویس یک چارچوب اولیه و غیررسمی برای تفاهم‌نامه میان ایران و ایالات متحده اشاره داشت، «صحیح نیست» و تفاهم‌نامه مورد اشاره «کاملاً ساختگی» است.
تلویزیون حکومتی ایران ساعتی قبل گزارش داده بود که پیش‌نویس یک توافق چارچوبی با ایالات متحده شامل تعهد به لغو محاصره دریایی ایران، بازگرداندن رفت‌وآمد در تنگه هرمز و خروج نیروهای آمریکایی از منطقه خلیج فارس است.
کاخ سفید در بیانیه‌ای اعلام کرد: «این گزارش رسانه‌های تحت کنترل ایران حقیقت ندارد و تفاهم‌نامه‌ای که آنها منتشر کرده‌اند کاملاً ساختگی است. هیچ‌کس نباید آنچه رسانه‌های دولتی ایران منتشر می‌کنند را باور کند. واقعیت‌ها اهمیت دارند.»
گزارش صداوسیما
مدعی شده بود که آمریکا متعهد به رفع محاصره دریایی ایران شده و در مقابل، ایران تعهد داده تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند.
تلویزیون جمهوری اسلامی همچنین گفته بود بر اساس این پیش‌نویس، «مدیریت و مسیر عبور و مرور» کشتی‌ها با ایران و همکاری عمان انجام خواهد شد و آمریکا تعهد داده نیروهای نظامی این کشور از «محیط پیرامونی ایران خارج شوند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75748" target="_blank">📅 18:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mvV08W4U7EeAlAk0c0LLJIH1nObkHgYTQ9l6K1JVPygqnvWIHVl7idQuke-ojMA-j9UN0KTfCLHq7ya84w4gFP0wWHIrkgQzmHzQugU09_v_96v3578olpuHSIDWGwCmoPCok69KH4IoZ6SbLNNjEWhtUbnqYJUNQ2prNXGNoX_COEqBnmf3Wfqahv4Xp22aIXW1cJT-N5pXm7JpXssB5YPbmXxDCQt8F9VRto8tQeKjfvP-ned-vyOdsE8Qt1XvdoP6mqGn94xhkfeSeN4QZnWvIBGhnDtGj-MgzhqfP_X88Gxq93uWRAkYqRUoYydbtRp5YPxjNSFluOWTRFcjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد در شبکه اجتماعی تروث سوشال با انتشار تصویری ساخته‌شده با هوش مصنوعی، از شبکه سی‌ان‌ان انتقاد کرد و نوشت این رسانه نیروی دریایی جمهوری اسلامی را قدرتمند نشان می‌دهد، در حالی که شناورهای ایران در اقیانوس غرق شده‌اند.
در این تصویر، جمله «سی‌ان‌ان: نیروی دریایی ایران قدرتمند است» در کنار تصویری از شناورهای غرق‌شده جمهوری اسلامی در کف اقیانوس دیده می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75747" target="_blank">📅 18:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXUkk4HXb5-hudQbotSSbau1jh7g2kKDflvxrq548ORm1-Uceiw0g25roGTvGWgurxPJRxD3STQhE67x27A-RPe7Qtwbb2LHAMrM4AjCTnUcbW148y0LsCQXA1YuTIU02QPFwojQmVgZgQths4DMD4QNb1s6T3FkJVl6vZEHDtRYJv7X08hcdr1Fju45L_G7AUs4mHo6LAfMxwory6rVEkvcy6i3kaFVbHqKdq63OmtwC5Np70yDdz8X7qTA10D4wBM-wvuVG2Z3RC1tWYravOUW2AFPURFjoFlLxYpYhIeySCuOW9rigGwDyTd5EL6VtZq--Tif1GCFtkjMxUTh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گروهی از کاربران در شبکه اجتماعی ایکس (توییتر سابق) پست‌های انتقادی گزارش‌گونه از تحولات و رویدادهای سیاسی خارج از ایران منتشر می‌کنند، خطاب به شهروندانی که پس از حدود سه ماه به‌طور تدریجی با فیلترشکن موفق می‌‌شوند به اینترنت وصل شوند.
‏این پست‌ها که با عبارت‌هایی مانند «
وقتی شما نبودید
» یا «بچه‌های ایران که تازه وصل شده‌اید» آغاز می‌شود، همزمان با کاهش تدریجی اختلال در دسترسی به اینترنت، به محلی برای مستندسازی و بازاندیشی انتقادی نسبت به تحولات سیاسی‌ ۸۸ روز گذشته تبدیل شده است.
@
VahidHeadline
دوستانی که تازه وصل شدن یدونه «
سلام وحید جان
» سرچ کنید آرشیو کامل از اندر احوالات ایرانی جماعت در زمان قطعی نت رو براتون میاره
iamroyaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75746" target="_blank">📅 18:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=AXKX94TQG0IiQpZKGgcK9Wlpm6BZO1ZOTexJkHATblfeRnQWTEicrp7I0PgLJukSXYiO9ULTnMAPFE7NgEnT7zWJoK_z6fQnkK7CbptqHlEnna3WijF8Z4_NDMY2xgPpFs297F82nE6Q8WI5lV7g4kZ3E-2XYNOUmREvp0oOYHdbSqyTp_2IL5T_v9GISm-xd7XMoKPvuE1B23HWuGIFc_op5STXHtywhlQ_z4xJKgI-p0bLw3vQQ3cORp0cjPPMUqlFM0nDSP-XwlnPh4SEohURj7h6gKLEoStxLw-0VXjsnHMZEAbU0WXlFlMWkFc7DvOCrFc6Bat25tRoOLHJEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=AXKX94TQG0IiQpZKGgcK9Wlpm6BZO1ZOTexJkHATblfeRnQWTEicrp7I0PgLJukSXYiO9ULTnMAPFE7NgEnT7zWJoK_z6fQnkK7CbptqHlEnna3WijF8Z4_NDMY2xgPpFs297F82nE6Q8WI5lV7g4kZ3E-2XYNOUmREvp0oOYHdbSqyTp_2IL5T_v9GISm-xd7XMoKPvuE1B23HWuGIFc_op5STXHtywhlQ_z4xJKgI-p0bLw3vQQ3cORp0cjPPMUqlFM0nDSP-XwlnPh4SEohURj7h6gKLEoStxLw-0VXjsnHMZEAbU0WXlFlMWkFc7DvOCrFc6Bat25tRoOLHJEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما اعلام کرد به یک سند غیررسمی اولیه از چارچوب ۱۴ بندی تفاهم احتمالی میان ایران و آمریکا دسترسی پیدا کرده، سندی که به گفته رسانه‌های ایرانی، هنوز نهایی نشده اما حاوی جزئیاتی درباره وضعیت تنگه هرمز و حضور نظامی آمریکا در منطقه است.
بر اساس این گزارش، در پیش‌نویس منتشرشده آمده است که آمریکا متعهد می‌شود نیروهای نظامی خود را از اطراف ایران خارج کرده و محاصره دریایی را متوقف کند. در مقابل، تهران نیز تعهد می‌دهد ظرف مدت یک ماه، عبور کشتی‌های تجاری از تنگه هرمز را به سطح پیش از جنگ بازگرداند.
طبق مفاد این سند، کشتی‌های نظامی مشمول توافق نخواهند بود و مدیریت مسیر حرکت کشتی‌های تجاری در تنگه هرمز با همکاری ایران و سلطنت عمان انجام می‌شود.
صداوسیما همچنین گزارش داد که هنوز چارچوب نهایی تفاهم تدوین نشده و ایران تاکید کرده بدون وجود «سازوکار راستی‌آزمایی» یا همان مکانیزم اطمینان، هیچ اقدام عملی انجام نخواهد داد.
در بخش دیگری از این گزارش آمده است که اگر دو طرف طی ۶۰ روز آینده به توافق نهایی برسند، این تفاهم می‌تواند در قالب یک قطعنامه الزام‌آور در شورای امنیت سازمان ملل تصویب شود.
@
VahidOOnLine
🔄
آپدیت:
کاخ سفید: گزارش رسانه‌های جمهوری اسلامی درباره تفاهم‌نامه تهران و واشینگتن کاملا ساختگی است
کاخ سفید گزارش رسانه‌های جمهوری اسلامی درباره بندهای تفاهم‌نامه احتمالی را «کاملا ساختگی» خواند و گفت نباید به روایت رسانه‌های جمهوری اسلامی اعتماد کرد
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75745" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HJYtxu8oe-CBKH1Wr8Vk-jDL8OFYAPTGhapVSiT5x_calttl0_eNgb47zvMVYqBTYcdR4RYoLw70wMnmuSrYapzroGTcS61GWUsaWzHHb5JAV9MHF1UvA9CwAWU_piorSvgaAaOOLqKZkanN2hZG3N2iya3TkBWbmBdZfVA3WcORdsIKT-HzgcV8KI6KyiN9zUFZFPsNZ71w9nR07HYsG7bDCSnbkiQlbaCRS0I45XM9OgAyVIRQUWEQ5e33B7BWmkUuqctDTVohm6pu1EUhbyIAtVatlTDEJb9HosB_ewq-VyIDwS_4U_aFyvtbw5jJHIYBpAyoGwFdpnBI91Blqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در تروث‌سوشال گزارشی از جروزالم‌پست را بازنشر کرد که بر اساس اطلاعات اختصاصی «مدیا لاین» نوشته است موارد آزار و تعرض جنسی به زنان بازداشت‌شده، به‌ویژه زنان جوان، در زندان‌ها و بازداشتگاه‌های جمهوری اسلامی در دوران آتش‌بس افزایش یافته است.
در این گزارش، زنی جوان به نام کاملیا گفته پس از بازداشت خشونت‌آمیز در خانه‌اش، دو هفته همراه هشت زن دیگر، از جمله دختری ۱۶ ساله که با ساچمه از ناحیه صورت زخمی شده بود، در اتاقی ۲۰ متری نگهداری شد.
به گفته کاملیا، او پس از انتقال به سلول انفرادی و خودداری از اعتراف اجباری، در اتاق بازجویی هدف خشونت قرار گرفت، لباس‌هایش پاره شد، با باتوم مورد تجاوز قرار گرفت، به‌شدت کتک خورد و به تجاوز گروهی تهدید شد.
جروزالم‌پست همچنین با اشاره به قطع گسترده اینترنت، بازداشت‌ها، ناپدیدسازی قهری، آدم‌ربایی، تهدید روزنامه‌نگاران و مخالفان در خارج از کشور و افزایش ناگهانی اعدام مخالفان نوشت سرکوب در ایران تشدید شده است.
دونالد ترامپ پیش‌تر نیز با انتشار پستی در تروث سوشال خواستار آزادی هشت زندانی سیاسی زن در ایران شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75744" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mNSB29sHKfu_6U02gnogd3vYkMmuz21VIXbqYfz3gKZ09SURJQ-mlbyisuBk01h3ceZRxs2up8wgoDjqyHJl53zJE8iXrd_ZPjIhamK4hGtBiDPrNYN5bMEz-aWvIVbZutuaVYUdeHcjuZuqrkyAhu39nSgiynRKv0qDMaTaZFCXoRHK80k6XF4CO6nJLozEHfjj0l2MtSNFaslKSlBPLSscmnC6FyOhAQJlt0sp6IC5wzRLKIXYWpkJaKD9w4uxKB7XJIT_Wzp-f3wf4CE_MvtN4fMrhJFwDWolC_jiQphBtYgpxeigXaPR0dUAzX6Xtv167s5BVFu7xw0_gjRGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e1ndxCTn-ITGVC2EN8SudpcDLbNRpqYrpMhXkoBREnQPmU27XFGAcnSVJ1T-h-fjDwdb15aHKbSFRC95o_aRW2EjKpO7CHSQaosvCbunSUbUXO0wXooFv0tTLhWDymOQkcYn_u1hFYCvowriaeTKDWva5lHCAGHE0N2vYU8ynmmpKn6YmjSWKriQbKZeF27g6clcJKnymjrkYHuwMFqeyQzzx4-g9ndIlT00xXmGfPcjAbbjxFTjd14DoencPjlgIwogeYep1CK1KwpcGnz7qtiItnAs9dEBV7jvPtFdxPhInIvasqV1-CNqCoAIea1zy0ydvwGMvOHuMXfJynzRAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز چهارشنبه ششم خرداد هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
این وزارتخانه در بیانیه‌ای مدعی شد که «تشدید فشارهای اقتصادی و متعاقب آن، انجام تحریکات گوناگون اجتماعی توسط عوامل دشمن و رسانه‌های مزدور فارسی‌زبان بیگانه، با سوء استفاده از برخی کمبودها و گرانی‌ها» یکی از محورهای مورد توجه آمریکا و اسرائیل است.
هشدار درباره احتمال ناآرامی همزمان با افزایش شدید نرخ تورم و و گرانی کالاها و همچنین انتشار گزارش‌هایی درباره کاهش شدید درآمدهای دولت جمهوری اسلامی در پی هفته‌ها محاصره دریایی آمریکا و سقوط شدید صادرات نفت ایران مطرح شده است.
این در حالی است که اعتراضات دی‌ماه سال گذشته نیز بعد از افزایش مداوم نرخ ارز در بازار و مناطق تجاری ایران آغاز و بعد از چند روز با افزایش تعداد معترضان، با خشونت شدید نیروهای امنیتی و کشتار هزاران نفر مواجه شد.
وزارت اطلاعات همچنین درباره «عملیات تروریستی و تجاوزات مرزی بویژه در شمال غرب و جنوب شرق ایران» و انواع عملیات «ترور و خرابکاری» هشدار داده و مدعی شده که آمریکا و اسرائیل به دنبال وارد کردن «انواع سلاح، مهمات و ابزار ارتباطی غیرقانونی، بویژه استارلینک» به ایران هستند.
ابراز نگرانی از رواج اینترنت ماهواره‌ای استارلینک در حالی است که بعد از ۸۸ روز قطع سراسری اینترنت در ایران، از روز سه‌شنبه شهروندان توانسته‌اند به شکل تدریجی و محدود به برخی سرویس‌های اینترنت جهانی دسترسی پیدا کنند.
@
VahidHeadline
این بیانیه که با عنوان «سخنی با ولی‌نعمتان و هشداری به دشمنان» در رسانه‌های داخلی ایران منتشر شده، ادعا می‌کند که «دشمن شکست خورده در جنگ نظامی، بدنبال تولید دستآورد برای خویش، گرچه از طریق جنگ نرم، می‌باشد.»
این بیانیه در حالی صادر می‌شود که اسماعیل خطیب، وزیر اطلاعات جمهوری اسلامی در سومین هفته جنگ در حمله اسرائیل کشته شد و دولت هنوز جانشینی برای او معرفی نکرده است.
وزارت اطلاعات در این بیانیه علاوه بر اسرائیل و آمریکا، بریتانیا و اروپا را به همراهی با این دو قدرت متهم و کشورهای عرب حاشیه خلیج فارس را به‌عنوان «غلامان متمول» مسئول تامین مالی «جنگ ترکیبی تمام عیار» علیه «مردم قهرمان ایران» معرفی کرده است.
وزارت اطلاعات در این بیانیه معترضان و مخالفان جمهوری اسلامی در خارج از ایران را تهدید کرد و نوشت: «مزدوران ضد انقلاب و تروریست‌های مقیم خارج کشور و حامیان آن‌ها نیز از آتشی که می‌افروزند در امان نخواهند بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75742" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dStQVuABIWdF0p4yF74yhdclewDgwu_v-MyKDSNg6FLA69d_zXMVe-q8Yl2rBqN0VmHAiA5bEaXxTCLHDz-nJt7CU4tf34PkEhzEH_sVnMNCq6KiRA4qeOIcH7c-7tEYI2nIg9Mbz8uqU1v7rNgcBMHubFDZWqACOixL1V97cGEV54XaG2YOMvdmf5dNB_7SJccSgcxvm-UJAWEvkcmY9iVpKIlX7o9SL7wV3NWIOjXzs8iAVEGLz0OK1TEUbytmRiD8bHUWzbVELoMu2pvIPIXQYeXdXzglxmUDJ904vgj5lrcqXtwnpaJcgfzM0lJvekGQwOQsx1jTT_CmwvACvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی در روز سه‌شنبه ۵ خرداد گزارش داد که حملات دوشنبه شب نظامی ایالات متحده به اهدافی در جنوب ایران پس از آن صورت گرفت که تحلیلگران اطلاعاتی، مجموعه‌ای از اقدامات نظامی بالقوه تهدیدآمیز جمهوری اسلامی را در ۲۴ ساعت منتهی به این حملات شناسایی کردند.
هواپیماهای جنگی آمریکا دو قایق تندرو سپاه پاسداران انقلاب اسلامی را که سعی در مین‌گذاری در تنگه هرمز داشتند، غرق کردند.
این مقامات که نخواستند نامشان فاش شود، همچنین گفتند که جمهوری اسلامی پهپادهای تهاجمی یک‌طرفه را به سمت حدود دوازده کشتی جنگی نیروی دریایی ایالات متحده که در خلیج عمان و دریای عرب یا اطراف آن هستند شلیک کرد. این کشتی‌ها در حال اعمال محاصره دریایی آمریکا علیه جمهوری اسلامی هستند.
طبق این گزارش تحلیلگران نظامی آمریکا همچنین فعالیت‌هایی را در برخی از سایت‌های موشکی زمین به هوای جمهوری اسلامی در نزدیکی تنگه هرمز شناسایی کردند؛ فعالیت‌هایی که امنیت هواپیماهای جنگی آمریکایی مستقر بر روی زمین و آن‌هایی که روی ناو هواپیمابر آمریکا در منطقه به عنوان بخشی از نیروی اعمال‌کننده محاصره دریایی حضور دارند، تهدید می‌کرد.
تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، روز دوشنبه در بیانیه‌ای گفت که ایالات متحده «برای محافظت از نیروهای خود در برابر تهدیدات نیروهای» جمهوری اسلامی حملاتی را به اهدافی در جنوب ایران انجام داد.
سایر مقامات پنتاگون گزارش‌های رسانه‌های داخلی در ایران را که در روز سه‌شنبه مدعی شدند یک پهپاد آمریکایی «ام-کیو۹ ریپر» توسط جمهوری اسلامی سرنگون شد، رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/75741" target="_blank">📅 04:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0QKR_m02vbLiCMUFL--cSHFYlYqnaqfaLyk7z8BR20mS8p0vY30rPi7L_xNLlaHLzNmpV3wLQ1VPbNvzvJFgHlRHA9VlvQ9q_jM_2hrULBmBY28Ih3E4mbgiQ00py4DySWymO9249M0z8fHllG2kc0hAHXzbjfLoLV8Rscn51rs03U5n9JoZLa0zwJaj3wN-xGfBjIHL_ZOcNvJ3MMewX37s65xjLFR0Acub1PqZVL4UjcWO1jjJZPnh1B8s26wR1UQIkCVi59u--Vr5Dq09mF2rr_7p0j4FrQuB0bDODGiGKs28WfOP7M6w1I04xldAfaGBvlskwMi-BFCRvWqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
با توجه به احتمال نامساعد بودن شرایط جوی در روز آینده، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/75740" target="_blank">📅 00:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3TpYDPeXQdFIRw5IXHrOeuSEtm7T27JvyYOi00fhj11WEhQIZ7mWdNJGiZ-D0nRWEwveUskIG5RDGpJhs4_X7qHBONoMw2UgpcpFCZEIRV4VUucFH655XTj2XxkfKblW5LylY_jxjlEG3AnLPIf23h42Jju8Lq3vLAYfhVq1ZNkEhB-oxE9y-9ZtJ4DX7HA1NxB0aDuApCLSD04vGCLZXPV3shObgy_nCTqaH47ScsFdfwsSvYfYvuXpqx4pWm2eQxZvLKnJ6vge9uqD64BqQVFu3Xkbgt2U2cB0QP9FFWIjt9aMMEzYv8DbPAvDT4dtLpstnFqG1eFcgDyDN0IPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ متنی که
۸ روز پیش
منتشر کرده بود رو دوباره پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر کل ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بگذارد و دست‌ها را بالا ببرد، در حالی که هر کدام فریاد می‌زنند «تسلیمم، تسلیمم» و با هیجان پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمز شکست‌خورده، چاینا استریت ژورنال، همان وال‌استریت ژورنال، سی‌ان‌ان فاسد و حالا بی‌اهمیت، و همه دیگر اعضای رسانه‌های جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و اصلاً هم رقابت نزدیک نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها به‌کلی دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/75739" target="_blank">📅 23:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK6angryglSh3e2n2Yi1jhfuOiYHx9Unnnp9TWA2CW_LAKAIy7SQQ-Y35tVlH36YBQBN_myaQ4Xa6ZjNYAnsrgWqC3i4jEwrsx7OaFw58wRAZ_-vcIQH77vOCkITnHWFnMWJc2p6_sMBzCcQ45z_7uL9qwn2vf3VzRfirbEch5UNrfFRuBEqsyIvhIS39zHxO5kwUo87gkVJ_ekJpD1YkgyAAr2I-PJCxhPQYkQ0-1UGFl2GclogPtcF8KrALWh6HSa-9wMNHlB695hwSIe7QoZushBx-1h_T4eH5VStqBnqe8MfOHIutTkuorLdS0ItAgPBKzWVJ6mcf-obfBkEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، قرار است روز چهارشنبه نشستی کم‌سابقه با اعضای کابینه خود در اقامتگاه ریاست‌جمهوری کمپ دیوید برگزار کند؛ نشستی که به گفته یک مقام کاخ سفید، همزمان با نزدیک شدن مذاکرات مربوط به ایران به مرحله‌ای حساس برگزار می‌شود.
خبرگزاری فرانسه با انتشار این خبر نوشت که انتخاب کمپ دیوید، اقامتگاهی دورافتاده در کوهستان‌های مریلند که ترامپ برخلاف بسیاری از رؤسای‌جمهور پیشین کمتر به آن رفت‌وآمد داشته، نشان‌دهنده حساسیت گفت‌وگوهای پیش رو ارزیابی شده است.
روزنامه نیویورک‌پست گزارش داده که موضوع ایران محور اصلی این نشست خواهد بود و همه اعضای کابینه  [
از جمله
تولسی گابارد، مدیر مستعفی اطلاعات ملی] در آن حضور خواهند داشت. بر اساس این گزارش، مسائل اقتصادی نیز در دستور کار قرار دارد.
کمپ دیوید در گذشته صحنه چند تحول مهم دیپلماتیک به رهبری آمریکا بوده، از جمله توافق‌های سال ۱۹۷۸ میان اسرائیل و مصر در دوره جیمی کارتر و نشست ناکام اسرائیلی‌ـفلسطینی در سال ۲۰۰۰ در دوره بیل کلینتون.
این دومین سفر ترامپ به کمپ دیوید در دوره دوم ریاست‌جمهوری او خواهد بود؛ نخستین بار چند روز پیش از حملات آمریکا به برنامه هسته‌ای ایران در خرداد ۱۴۰۴ بود.
@
VahidHeadline
🔄
آپدیت:
محل جلسه فردا عوض شد به کاخ سفید
چند پست پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/75738" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4zOkdHmbDuVhhFg4xwmNoUCIj24tfpk82_1KSlOkQQbdLspVoEwQ36-iTneDtWczNo8u0Of8br7bJE8wr5qDCGEjSmjLVRMwEYoLKGBlwrPf8zQPsF6u3mi_pErrRfyDJz5xbejvuzl1ChiUTKy33i970NLACuXCkTvo-wJGqUMvDZSOB10zEy-eV2dPRIFs4deq34_ur48XFdqTtOAl_Yh3VXxhPGuuxgqHFmEd8Dg_Zfcmao6x4LIGr4l-Kqh6MD_ZqMBj6-x4AMD7VmKS_Ei5sQzeYmf8h4a8agh7OtnM6k8UZ-F3OS9-NjfzlLdEsR2J1HE9nej29sAwD7oHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش فارس، خبرگزاری وابسته به سپاه، محمدباقر قالیباف، رئیس هیات مذاکره‌کننده جمهوری اسلامی ایران که روز دوشنبه در راس هیاتی با همراهی عباس عراقچی، وزیر امور خارجه و عبدالناصر همتی، رئیس بانک مرکزی، برای رایزنی با مقامات قطری به دوحه سفر کرده بود، عصر سه‌شنبه، پنجم خردادماه، به ایران بازگشت. بر اساس این گزارش، محور اصلی گفتگوهای میان مقامات عالی تهران و دوحه در این سفر، رایزنی درباره بازگشت پول‌های مسدودشده ایران بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/75737" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP1cen8Bqr0Wr2_EvGQJCHjwyg0kSzc3N86m9OpMqPFk55ILnJNFBWlYMOzmQg6PWw3lhN3qHBoiXJMVjxqnsxtC6cSkUPhUELWPNSJPlO9FDhMdG2n9uDIQhIUWjWQmLi89ZW14XD0WTPdfqjIZwbEvKophkvliIJpGhUGMprO1rgY2guJhaLB5x4SE2_nAbcdYv3q4pTAEjUqYqDEj9goKa-8bqqzQFYf1bADKjYhPEDpuTKl4YP-yIiQ3UfeEOOvcCidjqCigtKmDyCTR3wiItaT4NEWsaCIM3UrB3FxdkMbBXBJYiaqixg8LqB3n2zWw0BlpPF8xFylBCoa4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز سه‌شنبه، به نقل از منابع خود مدعی شد که طبق متن ۱۴ ماده‌ای یادداشت تفاهم بین ایران و آمریکا، منابع بلوکه‌شده ایران، به میزان ۲۴ میلیارد دلار باید در طول مذاکرات آزاد شود.
آنطور که این رسانه نزدیک به سپاه پاسداران از قول « یک منبع آگاه نزدیک به تیم مذاکره‌کننده» گزارش داده، ایران تأکید دارد که نصف این مبلغ باید با شروع مذاکرات، در دسترس قرار گیرد، و بقیه در طول ۶۰ روز منتقل شود.
این گزارش می‌گوید که سفر اخیر عباس عراقچی و محمدباقر قالیباف به قطر هم برای تفاهم دربارهٔ اجرایی‌سازی این مطالبه، و نحوه دسترسی به ۱۲ میلیارد دلار در گام اول و رفع موانع بوده است.
همزمان، احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد که چند روز پیش، قرار بود ۱۲ میلیارد دلار از منابع مسدودشده ایران، از طریق روسیه وارد شود، ولی آمریکایی‌ها مانع این انتقال شدند.
هنوز هیچ مقام رسمی در دولت آمریکا، این ادعاها را تأیید نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75736" target="_blank">📅 18:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gCAkrbT7xY6eeKJX18lDiU08hZDZArNFhmQhsKCmcV8M5SAu74DQU4k-Kl7DRw10JH7gdyoaqntJvZFOhcn-RyLNfbfFYmsoB-kG3UxML092smh-G-Gu6i993jMXfhOY8StANyGW7v4gmMOHuFKHqZmmH2WncYptHpNbWJb4zp89Cfs3R4ZXtImhJ21b1r9CHl0nHQvqRYejHSwkw2aA4O2Wk7LO6eudH9LUa-eY2uILHryXFYcE4IXYPrHT5yTCIjA0MPQfo5Y1BgR3zDoB4itXjhp8PpMopQyvLLuqQUzQxau5NvIT3-gnwzP2kWUZF6PTh0SGeZQeSNCiNauMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B_rvE88sXYH6QnR24--EpEF2wMIRjXqxmk0Bt7lLE3dprTB7CF0_aJ4clJjtGra3MZD8YjDz609rz47zI4na5BC59i1d9WWQ26BCh9Yy2Ldp7IBZx01kkZMf6Vy3kxvZRmeh-cFFPyb_Ny9v1c_IZj7u-q7zwu2-yM3br2BROONf160BGIiiS_qP88cRF0dQTgB08D78GCx0IuwvPeefLbmBrCzNRRr5D5iMYXvsmsYTb2W2Y4bB1PKv83X0N47tA_kOkaapUUh02gB0Sw5HJSgwqJUln3YHb_0IXGJo7yEb2Vs9MvvbfWJsoa8QWXnY0MjcAl_U33sdxAe7rtzScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vBZWsbpESKRMH8z9vviSfFZMDYXNzqN1DzZImf8Vqd8QWojvr96P_hWUDO96OiAoJSuiwIkmv00OR--fn_qpV4tbs9ENhoYkRKoTsLf5YtGUumiApsiFEGEd2_BVnWtM4yiYLeAjhh20aXZUF49jp5eAcKjY-moJwb8oyU377O1rwfkq5BwRZvW2Tpl_IYJehi-f1iIeEf4kVL_CZ1wiEWRBhR-yLkb9V2eZjAR5AKAwUyk82xHRdVXGq7dOmXX_rlMUHGyxT5lOerxHYI_A5b8UjSFPiM_fA0oikrzGAMwykcTR_1bTFnnq40QND0Jjwb-SNmCASDsYCYiOAcnXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WT0lmSkrQ6HJmEeYVPx2pwzdP27UEGP_vjF4kFtveb4G32-0TUKE5nIjvRJfttXTLn-khw0OitM-cvVb887Cpig4hTfLBMWzyVQGNC84hTjq7Yo7cd8Citp6aXq92Atq4AH_JxLP_F4xm4TWPoeSXL-L8coHTQnyUEyRuCkdR8JqRbtAZQasdgH-0g1pccDLZuYTAJbwYjdaxo-XCaeVN-JJxPdAld-2JTy7sAyyjY28uUzSnCsIZ8YH0-iZlwIR8-sCBlRYByO1oT6kZekAn1JLUVExDbcwdii54X2Momv23L8jmWAky0VS7-nrkP6CvkBVCQxb8bHeiC3memMiNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد پایش وضعیت اینترنت در جهان، اعلام کرد داده‌های زنده این مجموعه نشان می‌دهد اتصال اینترنت در ایران در هشتاد و هشتمین روز قطعی گسترده، به صورت نسبی در حال بازگشت است؛ هرچند هنوز مشخص نیست این وضعیت پایدار خواهد ماند یا نه.
@
VahidHeadline
ساعاتی پیش از این واقعه اخبار دیگری منتشر شده بود:
در حالی که مقام‌های دولت مسعود پزشکیان از آغاز روند اتصال کامل به اینترنت تا ۲۴ ساعت آینده خبر می‌دادند، دیوان عدالت اداری اعلام کرد دستور توقف اجرای مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» را صادر کرده است.
این دیوان ظهر سه‌شنبه پنجم خرداد اعلام کرد «به‌دنبال طرح شکایاتی، دستور به توقف مصوبهٔ ایجاد «ستاد ویژهٔ ساماندهی و راهبری فضای مجازی کشور» داده است» و افزود: «تا زمان رسیدگی نهایی به شکایات مطروحه، مصوبات و تصمیمات این ستاد قابل ترتیب اثر نخواهد بود.»
مرکز رسانه قوه قضاییه نیز اعلام کرد دستورات و مصوبات ستاد ویژه «به دلیل بررسی غیرقانونی بودن ساختار ستاد، تا زمان رسیدگی قانونی قابل اجرا نیست».
@
VahidHeadline
بعدش:
همزمان با اعلام دیوان عدالت اداری مبنی بر صدور دستور توقف بازگشت اینترنت، ایسنا به نقل از «یک منبع مطلع»، روز سه‌شنبه، پنجم خردادماه، گزارش داد که با صدور دستور اتصال اینترنت از وزیر ارتباطات و فناوری اطلاعات فرآیند اتصال در حال انجام است و طی ۲۴ ساعت این امکان برای همه فراهم خواهد شد.
این درحالی اتفاق افتاد که تنها یک روز پس از مصوبه «ستاد ویژه ساماندهی فضای مجازی» برای «بازگشت اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴»، دیوان عدالت اداری با صدور دستور موقت، «اجرای مصوبه ایجاد ستاد ویژه ساماندهی فضای مجاری» را متوقف و مصوبات این ستاد را تا زمان رسیدگی نهایی، غیرقابل اجرا اعلام کرد.
همزمان، انتخاب نوشت که کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری تحت راهبری یک مقام ابقا شده دولت ابراهیم رئیسی، «شاکی قضایی» اتصال اینترنت بین‌الملل هستند.
ایران از زمان آغاز جنگ در نهم اسفند، به مدت ۸۸ روز، در خاموشی دیجیتال به سر می‌برد.
@
VahidOOnLine
محمدرضا عارف، معاون اول پزشکیان، در شبکه ایکس نوشت پیرو دستور پزشکیان «گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد.»
او افزود: «با بازگشایی اینترنت، خدمات هوشمند هموار و مطالبات مردمی که این‌چنین پای کار نظام و ایران ایستادند محقق و موانع توسعه دانش‌بنیان و مرجعیت علمی برداشته می‌شود.»
عارف در متن خود درباره «گام نخست» و وصل شدن اینترنت برای شهروندان توضیحی ارائه نداد.
این در حالی است که پیش‌تر فارس، رسانه وابسته به سپاه نوشت دیوان عدالت اداری اعلام کرد که در پی طرح شکایاتی درباره ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»، هیات تخصصی صنایع و بازرگانی این دیوان، با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت صادر کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75732" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c30x5vGqG0eHWF__HWNFZYw9CQ2Y-ZeTK4kt8J3-v-vY19ks6ms_W7GD5NZaZOU7GhxYcAZGZRqiMD9JQHEIhoZu22WEwE-HtXf087AhtGjOLpE5nYJnNbZqLK_9mVLpyNHm4pwcKaKINs4FLoY-JkW1QQd12RDdUdlwIiFX9xNrwHDKatCtIXHDHKpPeswrJSCZSF6HbWzWL9A-zxUcRxYp5f-BYFOYS4ZPN9p-xsdZpnxTUOkfccjSFjWtjG9JdssKhP-GFX3kMinkRYTV77JLgU615fFnollFJrtRcPShHUFchrpHdroAEmaY6iwEIWW6OcLv6tsiR1EGBe8Ieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75731" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/snTZg4vu2kGb8GYP7b41bVKOaW2pWLU_U-iJGSyFuNorSWT9YojdyVFCeo9IJx2gRz8TpDiZuQRv2k3tn8exH01D1iRm6p05Wclc-VHU98W3f17OVEI8yXr0z4vdUjXV_ZT8aABHX0p19VvIE6BBjbkRF8pGhPY8U4Y7eewatVXBrueLXdWK2P9UYj5otgsmm02wGzU-wCrZi9UJR3zlra3qL-0ji2Ool_6HLix5zJSzzJJbqPCVrJXdLXcS6cMlZcYLKQ_U157cAAe5d0yMeiWYEv5q8JUACtVuF3Q3_OuY39n8lk6z18yCAdRPLwZtHe9lR9OZoAO07_SRbx0ggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GqSOWgnvFa49Cm_eoWrkXjjH6EPn1krSJVqoqAd4l8kCAES_Q1bPJHN2Pjb_mwSPqY3sWvLdjn7QYNmaxY6H1je0eWgUQCcS6iJ2PbM2sFyLOBs_pqhT8Cps9Pb_Fm9NiSe1Q57uCrFFjwPO_kYMZMiq7IDq1FQyqKoje-PcDw5RjIC72JGHsz5UT4ftEBWNO5hDOxVvhn_S_QeAgqGCRyryO36xs3nM0r30LEnyPb1kto9GXP2Ja3icoM-mCf4WoFexfuj3DFPVqW2sF0rL8TfetmdMaFNOuwPaqiWAst8_QeTDfAPuLhMwg2Z1eb_LjGUoc1FuTj7seenRaXdykQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران روز سه‌شنبه پنجم خرداد پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را به‌مناسبت برگزاری مراسم حج منتشر کردند که در آن می‌گوید آمریکا از این پس «نقطه امنی برای استقرار پایگاه نظامی در منطقه نخواهد داشت».
او در این پیام توضیحی دربارهٔ پایگاه‌های آمریکایی مستقر در کشورهای خلیج فارس نکرد اما هشدار داد که «سرزمین‌های منطقه دیگر سپر پایگاه‌های آمریکایی نخواهد بود».
مجتبی خامنه‌ای همچنین با یادآوری ادعای ۱۰ سال پیش پدرش علی خامنه‌ای درباره اسرائیل، مدعی شد این کشور نیز «به مراحل پایانی عمر» خود نزدیک شده و «۲۵ سال بعد از آن تاریخ را نخواهد دید».
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی را از او منتشر می‌کنند.
@
VahidHeadline
در پیام منتسب به مجتبی خامنه‌ای با اشاره به گفته‌های ۱۰ سال پیش علی خامنه‌ای، رهبر کشته شده جمهوری اسلامی، اسرائیل «رژیم متزلزل صهیونی و غده سرطانی» توصیف شده و آمده است: «اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله.»
این سخنان در حالی عنوان می‌شود که اسرائیل و آمریکا در یک سال گذشته در جریان دو جنگ، مقام‌های عالی‌رتبه  سیاسی و نظامی حکومت ازجمله علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، را کشتند، بخش بزرگی از برنامه هسته‌ای جمهوری اسلامی را نابود و تاسیسات و زیرساخت‌های نظامی و اقتصادی ایران را به‌شدت تضعیف کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75729" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETzfDNbAHODaRA-lxDHZ_lCnrDtP3LYKdU4KU-vYyKC8ust8gfGIjDQr1C76JgPlytYY9dF86HgdLxdWueIIcA5WETzczQR7W0ktC6bZbwQMIgj52ufw0My5wnVHoIi8KJnErSUnGnrpwg17tDyxExbiuxQ3SfPYUNyB7vBhuoouWtBIDYuMfzpSp_h3YNIYWDivKsOIGBA5sXKpePYieTsXVT91xvdV2k8TOaKT4-xHFLlQmrOqIIfWq7DzWVBKF1pcYC1Kvfhu-_s4FuNJMSoNeBOvu90cPrXJdVLz2vKY86GdN1qxug8ro1mGEsIZUt-M9I87YxjmmHPgjoA5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر می‌گوید گزارش‌هایی که ادعا می‌کنند دولت این کشور برای تضمین نهایی‌شدن توافق با ایران، ۱۲ میلیارد دلار به جمهوری اسلامی «پیشنهاد» داده، «کاملاً بی‌اساس» است.
ماجد الانصاری سه‌شنبه پنجم خرداد در شبکه ایکس نوشته که این گزارش‌ها «توسط طرف‌هایی منتشر می‌شوند که به دنبال برهم زدن توافق و تضعیف تلاش‌های دیپلماتیک با هدف کاهش تنش‌ها و تقویت ثبات در منطقه‌اند.»
او افزوده که تلاش‌های دیپلماتیک قطر که با «هماهنگی» شرکای منطقه‌ای انجام می‌شود، «شناخته‌شده و شفاف است».
ماجد الانصاری انتشار این دست روایت‌ها را «تلاش‌های مذبوحانه برای خدشه‌دار کردن اعتبار» دولت قطر نامیده که به گفته او به‌عنوان «یک بازیگر بین‌المللی قابل اعتماد در مسیر دستیابی به صلح» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75728" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QMT4P_rJWaokl_NamQCVbpuEkyOIMERMQbecPs1B0t9o1wR6YyNGirc03QXb5zlgT7PLtn4OKKpQFWklkME8ln3WPgMGhB3FUg_3nz3T6TFIEJHmqFtONlkCdbVVc9ygQz5Zs3rQ7bQfkqX4eXGL_N4H3VsMurccfmd7QvOFCYuBOB8bS6ZBzuGa8QuZ0QRhVW9f4EfoSUM9FpYCXLT8PsvrNBB3yxFLMhj6NrapzMYzEMzrxH41jMsJHRCnB_qXfkZc89-fbmkjq9ExFsluqXYLG63NZ_asb9ZXPT-AQz33CoJP82lEJQRCXXHT-a6mvqMg-hANk41zvjVpZu1pwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TQBH_6AZD1Xct45W5pRYpTNQn0a8LOPgc_Y6aivIy189xlRIk4FLb9APBRdsoSIqxsODBuBYYVoNNhZfiIPlkgzTV_-Ky99FS4acIpPXl_pBTSCMpRcKTWeyBv64IV9YWZ91P1_2yQjVuYNEfKhpgDynIstVM1UpYvTMoxkFo3EgxRhw9HA9eW9uvl5A2lSFv-518L9qQiFuvUW8S25bWz-fD23n02Q385YGFbpw0phLbP6fWWXkjsalG92ijSz2XlFE-0NSRB_ja1Jfd3hSunSwizDlM5EkjYVph7ExUU99GJfYklzU4Gi1-CxOQjvNsQVPxA6xKWZs7I9KrllR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X9CFsg5aFxmN2BacLQdKolbUCymObJE9rWEBa0EDeFnOOg4_10eRQUXxp_o0BTSmkUwyak1oIQD7IzTdrRfCM8PM4R7fUH1igx5hrFzW5W-5XyJ7EIIfOQrubA0eEAP1tfmdJ2htnR7r36tsnM6lefYpE2_6uuJwJSv9nZuKMF5H95RkvyX2nJG7atVcaxJWZE6qIxu4mxUGRdd4d7uXiwjIzXlSRl0_GFMIk7Tb-68yF8Uecc4uYi2T6LrwAsjE-XglRVagVNb2DHhi4w-vaFPeZC_8gqv2VxuJ6jJtw38v1sTSOKR6zNZCb7C80xpp5fTFZxaUTnE_E06uP1-jVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه، اعلام کرد غلامرضا خانی‌شکرآب به اتهام «همکاری اطلاعاتی و جاسوسی به نفع اسرائیل» اعدام شده است.
میزان مدعی شده او «سرشبکه عملیاتی موساد» بوده و پس از تأیید حکم در دیوان عالی کشور اعدام شده است.
در روایت قوه‌قضائیه، اتهام‌های سنگینی به او نسبت داده شده است؛ از جمله جذب افراد برای عملیات خرابکارانه، دریافت پول نقد و ارز دیجیتال، تعرض و اسیدپاشی به خودروهای افراد مورد نظر موساد، آتش‌زدن اموال عمومی، تهیه بمب و ارسال آن به تهران، تصویربرداری از نقاط هدف و حتی مأموریت برای فراهم‌کردن مقدمات ترور یک خاخام یهودی در یکی از کشورهای منطقه.
ابهام اصلی پرونده، نحوه انتقال خانی‌شکرآب به ایران است. میزان نوشته او در خارج از کشور شناسایی و با «فریب اطلاعاتی» به داخل کشور هدایت و بازداشت شد.
@
VahidHeadline
میزان نوشته است: بر اساس اعترافات متهم، یکی از مهم‌ترین مأموریت‌هایی که سرویس موساد برای وی طراحی کرده بود، اعزام او به یکی از کشورهای منطقه با هدف شناسایی و فراهم‌سازی مقدمات ترور یک خاخام یهودی بوده است.
@
VahidHeadline
گزارش دستگاه قضایی اشاره‌ای به تاریخ بازداشت و محاکمهٔ متهم نکرده و در عین حال وی را «از اراذل و اوباش یکی از استان‌های کشور و دارای سوابق نزاع و شرارت» خوانده و ادعا کرده است که او «به دنبال جذب افراد و به‌کارگیری آن‌ها در داخل کشور برای اجرای اقدامات ضد امنیتی بوده است».
از روند محاکمه این متهم گزارشی منتشر نشده و گزارش قوه قضاییه نیز مدارک و مستنداتی از اتهامات ارائه نداده است.
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75723" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qxjzEfxGADUeTOtytuqYqjgSjcvVl8c-XD63WF17yxtEURQRlR0_XiJvu4Zm5mt29DwL4yOoUSRqxdrXvE5hophMiT0AmlJkffW8RB2mRVU8xtsTgvQbkezEKNbYCBFCJ9JzJ8B77sM1enyuMweSePwuTzWoJ_f2hnS74EW4ftKbTODpEAobqpE7eSJ3yfJ9hNubUzR9OvbVJT15kY_3jfXH-xeTu5zUCLaugidCqmLdymBzWqz6febYq86Esuy_Y1Rz4i5vNxI9Xi-DArGuJqcxwH_bV6gUdgEKVi93v6c-zwy_DKE5_yoBJD4sp0wNR0AjhfU5YY1BMzMj5lhAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E02OXiuV1ECS7lu70UpwJdr_3w3d1P0kFVu2vqIbvOdPrZb2Fdnp_KHS-MUC8MgseXsZe3lskufjI42Vdw2e1iFsZaoItWRUcel_LaH5Zpa3nLl4M_4o11HdrmeVgI6izXaXssk6MkOz7-Cpal56OC3Y9lV-QfoWfbP642Q3i1riVVmV2UHpKE1nLo2sAimd5AI7xz-0Di331zBW3KLsSLmVfNI65kPTWUwSGMlPN4iIOEIpNwkeBonJQ_dVn1yvEvSiSsY4eOUTfc-zaT803V9JNa-kcMtcZHrWzCxKiX_R4qmip6M6hNMcap7QA_nj9sihbj0R0qI0xJ8GtBdlPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با وجود حملات اخیر آمریکا به سامانه‌های موشکی و قایق‌های ایران در خلیج فارس که وضعیت آتش‌بس شکننده را متزلزل‌تر کرده است،‌ مارکو روبیو، وزیر خارجه آمریکا روز سه‌شنبه گفت که توافق با ایران «همچنان امکان‌پذیر است.»
او در هند به خبرنگاران گفت: «امروز مذاکراتی در قطر در جریان بود،‌ و باید دید آیا می‌توانیم شاهد پیشرفتی باشیم یا خیر. فکر می‌کنم بخش زیادی از زمان صرف دقت در کلمات و واژه‌های به کار گرفته در متن اسناد می‌شود، بنابراین چند روز طول خواهد کشید.»
آقای روبیو افزود: «رئیس‌جمهور تمایل خود را برای انجام این کار ابراز کرده است. او یا به یک توافق خوب دست خواهد یافت یا هیچ توافقی نخواهد کرد.»
آقای روبیو به خبرنگاران گفت که تنگه هرمز باید باز باشد.
او گفت که آنها به هر حال این مسیر را باز خواهند کرد و افزود: «آنچه در آنجا اتفاق میافتد،‌ غیرقانونی است و باعث بی‌ثباتی برای جهان و غیرقابل قبول است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/75721" target="_blank">📅 07:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7mRbpvPWJlF3lhq9n0T2TbRAEtSUriLO_9XqipHq0b1Tu_ufXen-F-xyWV-jsovpXlrakiSqumiMhHAV7HVPG_MBmuicEzj2oDtYN_nHr8vqkZaYE6C8Bo7O762dwLnWbQgQdMSWRH019NxaENWY2IEp5t-UI87WsnZL0_lRZlyEZG-KOA4HDqhFpd75zM6yvR01Sax_09l-tpF9v-QOB477VEsO9ifCyh-Zcd_BZfO-XOhVevecKDTq4kIVXmiPgGo3o-Eq39BEgeQYkz3yJavUZE1ch-ei6BYKzKvJr0Jz_t6T2H5RnlLH07gs_tDRMg6XLAoTkXM5NnCdSAdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اواخر دوشنبه به وقت واشنگتن گفت مارکو روبیو وزیر امور خارجه، به در خواست همتای روس خود سرگئی لاوروف، با او صحبت کرد. در این تماس تلفنی، دو وزیر درباره جنگ روسیه و اوکراین، روابط دوجانبه و اوضاع ایران صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75720" target="_blank">📅 06:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYUGPzMkrSHp9GpY270j0cj15fAvYft4o15fnQKDFA7Pd0hxOacoXxqekGi_5_8EKPwwqSwKI4r1Lo0SDKPERXqwe7h6PNiaJq9rp5O1MThBEPtAL-jCTzGRUOl3TmHobVhc16EuiwNOgZ-DCLM_WRRNNd5QMCO6W2BNA5YT7YUSRNhjUEm87oq4iq6XvJqOtDqoevgxmcNvl_2Tro66WCTQOquMI6yAuheABee3gKMjXXvm5ZdFDoseOGfy7pum07ROSCWPtLiTs3vRkSHcGncNDxp31fsaSNYUj6a-rJnNGGpSRWjuawKWxAzu_chR8in7xvHtRQ74AxHcylcrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75719" target="_blank">📅 05:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXGbPspWN5i0Xoawakg8bcedxtuHH9F-ayKaMxN5Hq79zLy9y7ew65mGuH2hzYjC-OwhAsCaQY75J5jgIPWBzpZUQFX-QIRxx244SVxe-RyFA5lgUCXynS90oc6ThebxtrBs0zx15_KjBcCnCQYtEGG7ZmKdEqJo80aCjGxacW2oTrwxtDzp58VWIQOb-GOIlAp9ydnJj4bmweoGwsjJodIp51f27kZ4KSwkXX58EKAz9fWoqEANCFlw2YDLrCl_2KT-mQJTFbA9CjVBicuX5dHbhBSgaD2WpXCdOJnxtnmFUGeluUIESOkFE3UBAYgPLpbRyTqbWDY-AVq7gnAcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رماندهی مرکزی نیروهای آمریکا - سنتکام - در بیانیه‌ای اعلام کرده است: «نیروهای آمریکا امروز (دوشنبه) در جنوب ایران حملات دفاعی از خود انجام دادند تا از نیروهای ما در برابر تهدیدهای ناشی از نیروهای ایرانی محافظت شود»
در بیانیه سنتکام آمده: «اهداف این حملات شامل سایت های پرتاب موشک و قایق های ایرانی بود که تلاش می‌کردند مین‌گذاری کنند. فرماندهی مرکزی آمریکا ضمن خویشتن‌داری در طول آتش بس جاری، همچنان به دفاع از نیروهای خود ادامه می‌دهد.»
ایران هنوز واکنشی رسمی به این گزارش نشان نداده است، اما برخی از سایت‌های ایرانی از هدف قرار گرفتن دو قایق تندرو سپاه در نزدیکی سواحل خلیج فارس و کشته شدن چند نفر از سرنشینان این قایق‌ها خبر دادند.
نیمه شب دوشنبه به وقت ایران،‌ برخی از ساکنان بندرعباس و شهرهای حاشیه خلیج فارس، از شنیده شدن چند انفجار و فعالیت پدافند ضدهوایی خبر داده بودند.
رسانه‌های رسمی هم این گزارش‌ها را تایید کردند اما اعلام کرده بودند که علت این انفجارها مشخص نیست.
@
VahidHeadline
درباره همون وقایع ۲۴ ساعت پیشه که اخبارش تازه داره منتشر میشه ولی بسیاری از منابع جوری جلوه میدن انگار مربوط به ساعت‌های الانه.
احتمالا
اون پست ترامپ
هم که تصویری از قایق‌های مهندم شده با پرچم جمهوری اسلامی گذاشته بود و نوشته بود «خداحافظ»، در اشاره به همین واقعه همون موقع بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75718" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CGgsxihQFPIVC193LUFybPEcOOngMY8HJWVXO-wmfIqqvYlfiYwxVP6sXqa2Hb7Jh5H5pOvWsbG5e7cYrESjO-IGorlOT9MwWmPYtu5U1kX0Qc2Txy22rfrvkodkzQQoFxRksZLZJT_FNw5xK0g9irVU4rmhZtyqujAajDYXT-0ENm8SBnERh-85bxh3dfdCTwWpVqOFKnXCC2EvAqQUXywwR1Zq4AJ3-aRT_rjoQvOjqwUCVU52La9yQ2kr_do5Usbv1S95FvvCC4sqIN-fB-EEaYVIwfu2eTRF1Hb-71HPamPXFCWfZn6IRI1E8g_2vzuDjFOHkLZpckpjW7DsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s8UoR2hjBwYnq8RbZWBvOZH8bveEnnN2S-Pzjo7rztRwAiYM1AA8Tz7p4O2U7xeUCw80UFek0HdX4Fu1gVAtgtqo9NxRwiHwH98AGJ9GBH1UoDctmXQfi6ezSle7xEJDrL3XsXTRtIGM9D_NA5Hh19Hwv6go25yf-sgWMOs-oxd8Z9kaEpj4RdfnNRtvFLm6oqD82bk6zKciFtdx5BMp9gvMUf4bPc4_gGOgBVBa3Eys1bFHpTdeBNkv2SNqeq7QjlsTj7XjEaOkRyeueI2Qfb76fltZXMSIP8zM1RRijW-upEUf87ttQhnYxxkG4Zqq6lo8WI6zMkfwxWrdxli-kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری دانشجو گزارش داد که در ["حمله سحرگاه شب گذشته ۴ خرداد"] در جنوب جزیره لارکآمریکا و اسرائیل به جنوب جزیره لارک، عباس اسلامی، قدرت زرنگاری و عبدالرضا گلزاری، نیروهای سپاه پاسداران کشته شدند.
براساس این گزارش «تعداد دقیق کشته‌شدگان هنوز مشخص نشده است».
@
VahidOOnLine
گویا این واقعه مربوط به اولین ساعت‌های دوشنبه است. یعنی حدود ۲۴ ساعت قبل
ولی به نظر می‌رسه اون دسته از منابع جمهوری اسلامی که این خبر رو پخش کردند عمدا طوری گمراه‌کننده نوشتند که مربوط به صداهای شنیده شده الان به نظر بیاد.
ولی این توییت مربوط به ساعت ۷ شب دوشنبه است که درباره همین خبر به نظر می‌رسه:
دیشب یه قایق سپاه در حال مین ریزی در تنگه هرمز مورد اصابت یک جنگده که از خاک امارات بلند شده بود قرار میگیره و چهار نفر از نیروهای سپاه کشته میشن
YourAnon_Zeus
حالا این خبر درسته یا نه نمی‌دونم ولی مربوط به
صداهای شنیده شده ساعتی پیش
نیست. من هم ساعت سه چهار صبح دوشنبه پیام‌هایی داشتم از شنیده شدن صدا در قشم و بندرعباس
آپدیت:
پست بعدی: آمریکا اعلام کرد که ما بودیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75716" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAWyvRE8ICkES64XxLrhkBTzFRpme34BDglJDLoJ-HUcdaSMSGonD73zPe7PE0feQGTqsEQBD5y5zAu7sMj4MnonjiGckOXqkQcfakTx5A-lT9lPwnpZr1bi3l8Lhlv7d8AehJLSbQbW1FwBHXR7FK6LGxIfWVdmgsPC0TT4qPO6CuJ7JvyMJgL1FFV0GNWnCzVwI58HjGywyvZ5shm_VpKJEkTkbHdB1jFHODh1Xa9oJzcQuuWkUxkRrjMM8IOMCrThSvvmqoFdMdyJwoIHj3xF3QQ9WsMTD1dTekK5zV2Pi7FBUGhn91U2-g59wW57p7eUQB8K3f1P0S7QbhnypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اورانیوم می‌تواند در همان محل یا جای دیگری نابود شود
ترجمه ماشین:
غبار هسته‌ای، یعنی اورانیوم غنی‌شده، یا باید فوراً به ایالات متحده تحویل داده شود تا به کشورمان منتقل و نابود شود، یا ترجیحاً، در همکاری و هماهنگی با جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری نابود شود؛ در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، شاهد این روند و رویداد باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/75715" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی درباره صدای شنیده شدن صدای انفجار:
بندرعباس سه بار صدای شدید اومد الان
صدای بمب میاد.
بندرعباس ساعت ۲۳:۴۰
همین الان ساعت ۲۳:۴۰ صدای سه تا انفجار شدید توو بندرعباس اومد. نزدیک پایگاه شکاری یا همون فرودگاه بود به نظرم
سلام وحید جان
بندر عباس صدای آزاد سازی پول های بلوکه شده میاد
بندرعباس ۲۳:۴۰ سه تا انفجار شدید
حاجی۲۳/۴۰ سه تا انفجار شدید شرق بندرعباس
دقیقا صدای انفجار ۴۰روز جنگ بود
سلام همین الان بندرعباس صدای دوتا انفجار اومد
بندرعباس حدود ۲۳:۴۰ دقیقه سمت فرودگاه صدای سه انفجار اومد.
درود وحید جان
بندر عباس ۱۱:۴۲ سه تا صدای زدن اومد
بندرعباس، ساعت 11.40
صدای شدید انفجار و لرزش
سه تا صدای انفجار پشت هم شنیدیم بندرعباس
بندرعباس 11:40  شب 4 خرداد صدای انفجار
بندرعباس ۵ بار صدای انفجار
ما سمت پایگاه هوایی هستیم نسبتا شدید بود
پدافند سمت فرودگاه بندرعباس فعال شده ساعت ۲۳:۴۵
آپدیت:
رسانه‌های ایران شامگاه دوشنبه از شنیده‌شدن صداهای انفجار در بندرعباس و همزمان در خلیج فارس حوالی سیریک و جاسک خبر دادند.
معاون استاندار هرمزگان اعلام کرد منشا صدای انفجار در حال بررسی است.
@
VahidOOnLine
آپدیت:
کانال‌هایی غیررسمی نوشتند که به فرودگاه بندرعباس و اسکله باهنر حمله شده. منابعی مطرح هم با تاکید روی غیرقابل تایید بودنش نقل کردند ولی منابع رسمی چیزی ننوشتند که لابد مذاکره و توافق به خطر نیفته. تکذیب هم نکردند. حتی منابعی هم مدعی شدند حملاتی از سمت اسرائیل یا امارات بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/75714" target="_blank">📅 23:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=XBcQnasg2d5Ia_LAYTS0pqXdeAxf677bhBiikK-MVKHJPXf-ZegPo942qo4e6hSMcD9gBdUcRuIUxY4No-eS4JEP-UC8Zh43LJj96MUP86zvjOPPT5TGUQ9edgs99UJbbi4qDg0qATspkHQVeIoe3Q9VvBo-k64ZOKJNaUKP4yaS3ibMmlbE8YI8ZvNiASKXnnKNwB_KiNfdnG2DZ6SajRMIKtRCyeB4ViRNq-1AixmECf79EzM9pG3IP2pb8u8bn-IpGM0lBXWIfSKc25ThYkURuZW1eBlg5NHJ8HhlpQ2-cQnTiGyc1vjwHOhKbQyIThnHzrkZZYEyblDJz7psaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=XBcQnasg2d5Ia_LAYTS0pqXdeAxf677bhBiikK-MVKHJPXf-ZegPo942qo4e6hSMcD9gBdUcRuIUxY4No-eS4JEP-UC8Zh43LJj96MUP86zvjOPPT5TGUQ9edgs99UJbbi4qDg0qATspkHQVeIoe3Q9VvBo-k64ZOKJNaUKP4yaS3ibMmlbE8YI8ZvNiASKXnnKNwB_KiNfdnG2DZ6SajRMIKtRCyeB4ViRNq-1AixmECf79EzM9pG3IP2pb8u8bn-IpGM0lBXWIfSKc25ThYkURuZW1eBlg5NHJ8HhlpQ2-cQnTiGyc1vjwHOhKbQyIThnHzrkZZYEyblDJz7psaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه خبر داد که دستور حملات تازه به جنوب لبنان در تلاش برای «خرد کردن» گروه حزب‌الله را صادر کرده است.
ساعتی بعد خبرگزاری‌ها از چند حمله شدید اسرائیل به این منطقه خبر دادند.
نتانیاهو در ویدئویی که در شبکه تلگرام منتشر شد خبر داد که خواستار «سرعت بیشتر دادن» به حملات ارتش اسرائیل شده است.
او همچنین حزب‌الله را متهم کرد که با پهپاد نیروهای اسرائیلی را هدف گرفته است.
صدور دستور حمله بیشتر به لبنان، همزمان است با خواسته دو وزیر افراطی در کابینه اسرائیل که در همین روز خواستار تشدید حملات به جنوب لبنان و همین طور پایتخت، بیروت، شده بودند.
حمله اسرائیل به این منطقه در حالی رخ می‌دهد که در سوی دیگر تهران و واشینگتن از جمله درباره پایان جنگ در لبنان مذاکره می‌کنند.
حکومت ایران در هر دور از مذاکرات اخیر خود با آمریکا، پایان جنگ در لبنان را نیز خواستار شده است.
حملات متقابل اسرائیل و حزب‌الله در حالی رخ می‌دهد که دو طرف بیش از یک ماه است که به طور اسمی در آتش‌بس به سر می‌برند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75713" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kC_ZxVkL3hUM5n3QIXQjsZbWdoO9ue8GSskCWQCML0uclZeymaDUC5NslzKZ2N7dSOOLf01VjGrrzgm-25-U0f9yW01OdG_9L04gVoN4qwYD1EqTZkPOy6BBhfcV1KPBh32giTd4xpDoxshdGmgrY08N2pRpv1xKMB_ZnadDffVtgs5a7jcfqcr081dtSjP8bIycwIyDEK3Nwoiqv9RLGbTmZPdfifnO28nhHmW2JR2lgD6Kb_QMIOxIESMwn8WssP_BFY5UkJ6Iu_AqsjIw5-KnqwXsiK2eofp3IUNRu5d9ZiZtrDY9VAzj7SMxWf1eg7UzIUzPs5TJwwxA2CRuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره به نقل از یک منبع آگاه
گزارش
داد میانجی‌گری قطر به دستیابی به تفاهمی میان آمریکا و جمهوری اسلامی درباره دارایی‌های مسدودشده ایران منجر شده است.
این منبع افزود با توجه به اهمیت بالای این موضوع برای ایران، احتمال زیادی وجود دارد توافق میان آمریکا و جمهوری اسلامی فردا اعلام شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75712" target="_blank">📅 23:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJg0cmTQo1rtRLOmStUma6Rlq01YRnDEz_q-RkeS7m_5Itnu7vKtL4sn9rPFpiBP_Nn0smqSsc47mYeRBQ032ZxvfSwnzZJUKqOyyJUtTzW8_XXXXAo4ummvfh4oYgannR7Qg5KuRa5RjfsiukXpTgrX92pU7skI-oKJgtAcAc3yz4vYGQdqt6Abgxmm70P0-Y0o1BwKKrw2DbHK-WxVMlTPUmE5PT3oDi-tPy8Y21UA4Xok-wn4y60fjz18MuRrb3UJaXR8l8G6-HbuoSTJPju2JBm_GhUR3cD5pU1669U5S_c-1FXfEpnubWW_pMfn-Z31jRepCPFS5uxF9CaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پس از انتشار خبر تصویب تصمیم بازگشت اینترنت به خانه‌های مردم، چند رسانه در داخل کشور می‌گویند که مسعود پزشکیان، رئیس جمهور، این مصوبه را به طور رسمی ابلاغ کرده است.
رسانه‌ها در ایران روز دوشنبه از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌ بودند، مصوبه‌ای که برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، بود.
به گزارش سیتنا، پایگاه خبری فناوری اطلاعات، بر اساس این مصوبه، اینترنت عمومی باید «به وضعیت قبل از دی‌ماه ۱۴۰۴» بازگردد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75710" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RN7FRF5TcF7ZgcLyqTr__rfcEyD-1Oe5LQbacXHsy91NnWhs2Ukm4mztuBJjSwO5HZIJw-oLxpb-Pz5YMVLimLy5P-9doJjuZ1DL-9O-_J9Ku6QgRlh22Q0iHferv-NH--l9X_g3xUuE7VZluYVp2nTilW39-d1jBlGp-5jlGdpCps54dAczy9UyW3TX4VonA8rP-h0pXFJTKixFXi1QfdcRHaDrX5NZ00xMWbNpfPjC_BaLH3_-Z1ZhG1LXbiNuSv5aGSkfaCLJ31h7_Zl9-atrdTuhbxib5WF8VtNom84QdXG8B8rJKFnTI0dLNWUZe6LsozB7khgCfvdIRP7x0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از منابع آگاه گزارش داد پیش‌نویس یک یادداشت تفاهم اولیه و نهایی میان آمریکا و جمهوری اسلامی در حال بررسی است؛ تفاهمی که شامل بازگشایی تنگه هرمز، تمدید آتش‌بس و کاهش برخی محدودیت‌ها علیه ایران می‌شود.
بر اساس گزارش العربیه، در پیش‌نویس این تفاهم‌نامه آمده است تنگه هرمز بدون دریافت هزینه از کشتی‌ها بازگشایی خواهد شد و عملیات پاکسازی مین‌ها نیز انجام می‌شود.
این گزارش همچنین می‌گوید در چارچوب این تفاهم، به جمهوری اسلامی اجازه فروش و صادرات نفت داده خواهد شد.
العربیه افزود پیش‌نویس توافق شامل تمدید ۶۰ روزه آتش‌بس است و امکان تمدید دوباره آن نیز وجود دارد.
بر اساس این گزارش، آمریکا همچنین متعهد شده محدودیت‌ها علیه بنادر جنوب ایران را کاهش دهد.
منابع العربیه گفته‌اند بخشی از دارایی‌های مسدودشده ایران نیز بر اساس سازوکاری مشخص آزاد خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75709" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/medbFDeVCDe6dM46R5mT74gUzkExZxk-VypfUEqyhNqnpJhfVsKKKbQWt7sE3z7mAGkmO0AIUHuONJgAm6HA8hXDonDyw7ty8cjvwZI5di1P_0DOUkDwJmS9MxE6bxwkcT0JoaCNp9RKfskLN9vmjuOCYHh7XhhDac33z_yHV53JcFgY2q7lYPeztULzZYckz8TNi-gxRk8zjt9d3Fhd5XLduj6wUmAXk9nekYVx2WRGr2HSjJt1C9gVKwNoxsJaEYwLK42vJbtjtGCSX9A6oZUzNprYeUp2VLs_FeJwhPt-Zc8e5dcWm-DhhVI_ACuauJM6nz5EckaOc-rNtJqlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JDgzT7EcNbDxy9fHgE_6pL7X-TgEPR1v0RjpzzneCZiXo_n5uYtfcybk-ZN3vWY8OhmKfb2Ut3esgTQ8eE_uKIoUNY5hf9YFx3TBD5tkMPgL_Vx37h9g5Pb60EFcD0JXkQNhuprsENn7zknhHbdlaXvyq4mRh3lN4t7SZg977w3ciI4kl50Q8ezYwof4y2YZv8UqnTgYfesKRo5xK31-QWeKLsHHeMRHxy5sHpTr-gyRJn0d4_oI6EpMkdXn_5tvIE4Fb1H8Cnxe5eC5DNlw_aGCvEYGwrQgSvbdwe68Z958FQiYt_tkd54OLjeSUWJioD7XT7Bv6S6Hg0FWFYn1Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، در پیامی با اشاره به «میدان نظامی، میدان دیپلماسی و مردم مبعوث‌شده حاضر در خیابان» نوشت: عقب‌نشینی در کار نخواهد بود.
او تاکید کرد: بیش از هر زمان دیگری به وحدت و انسجام نیاز داریم تا آمریکایی‌ها و اسرائیلی‌ها مایوس شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75707" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T0DL-JoSJrKWHXIbFpzhN18VYHv91siYuIrqbYfo5SpNsHc0EKLSC_Ii8nujv0JIaNAruVcIEBZhm3ccCVdBZub61olu-TNbSirEiFl0IJtQ4FIhHb6Ti-IijbgLlz1bihxZXmlucI2gHwz-5D-kNk8OypvDyWkVYQCZZk3dJYsXFUKCoD_SClZQ64mBGouFwKJs48HxgZ8KTUeNg-ZHSpvulr07mq6oGBPvBuI_iT1bNLYg1xcLCaR07Yx1mtBDx23Id2i97OVZ4gk2ymjKje3tUeTPUB9ltm98LhP3BvK-gCPjsyMRrACh-4xS5jX_rKi5fhkc3pfn6dqkvO6S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uGuR4m3eZBmRETM3X4Q2bZbCXFGXOk9QtTn4gH2BABfFR97BKVn7HLZ7Lu_Iw16HBGWujWXEH6ZnqB1mSwSKe8y9tP_uF75YcNQf5rdx8m8mI2vMc0Mcg5xIIMwbyWEHtZkPgDsBL-qAotO5zqP70605iAbOQAikclekXRqtmjEwyWs-6wMkM8HSJhYSw80R-gWjbFgqX0WkEDdHCm0FzWNeJIA0K6ZOPalikuc3MVs7IN2kW6vbqRkwiQe5HStE0evLjsY_4dTbQKUM9uHM-Jno5w-W3wlR1KpYr__dZf12yk_0KFmoTtY3TuPQAyneFbDOUcQmwI6lrpQ8PYVvzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ از اکانت بقیه بازنشر کرده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75705" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GBOd7sErpPwhDKwRUM1PUVaqHlAFeD6M02PsT0Tq4UItVtt3xQT4tNLBghuSprZsbCc8kH9TO3tOBkOg0pUa1CfasZ3wXqK05ROcEg75ETdMK8TqPbfxh4tKb6D0l9fBTZDYKkTxOapSwVkzOnxsO7fLBZbhqF0jnJra4y_Rx5AJZUbZVfdxxZHXoEFI3AZJ9TBA6_KthMaSTgEoX7WUZhD7mFkMru4xsNbPLXZRZnoWoRxVOazYleGKxFBxe9-_mhl_rSbfVTDnlodwxRFIfQ7arYHBz6gJZTQ2RwwAO5nkyCBEf1hcpTeXSae2_w9IC27dLaNGFXpeVC91yQARtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YUQg5EXQ_ZhWxamo-52lQ5BMZtQgGt36VQQX6qOgBQoxjJL2ZyxnDRlMcfhguvST1hJjyHZtzV-J2d62gkDHZdHcSnlvIXKrblKL2edkPbe1ayWt146-G4eIzS61_EgNj2cFqBBKIAQUAqCMNRGFr5IHQy7HGWylQnhJ2n17x_fYip3h7zcxaCevBgzMvDfu2Y2yRwjFSnN-RhN8Z4g40exxiyhncGgQURO50O_Ykbvu55ODUw1vTdQh1gJ90ZfVKQI6cEdf_FLoI2OeQ4TZQbeoYjkwKEsqA1BqqSEHxKzqpIqCjQ4QYbiiSnySErmBxxYWhSBEgi_xFh8O6DF8QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه در تازه‌ترین پیام خود در شبکه اجتماعی‌اش ضمن خبر دادن از پیشرفت «خوب» در مذاکره با ایران، از تمام کشورهای دخیل در این مذاکرات خواست پس از حصول توافق با ایران، بلافاصله به پیمان‌های ابراهیم بپیوندند.
پیمان یا پیمان‌های ابراهیم طرحی بود که دونالد ترامپ در دوره اول خود برای تلاش در راه عادی‌سازی روابط میان اعراب و اسرائیل آغاز کرد و موفق شد تا چندین کشور از جمله بحرین و امارات متحده عربی را هم به این کار ترغیب کند.
حال رئیس جمهور آمریکا روند توافق با جمهوری اسلامی را به این طرح پیوند زده و به گفته خود این «خواسته اجباری» را با دیگر کشورهای عرب خلیج فارس و همین طور ترکیه مطرح کرده که به‌فوریت و همزمان به پیمان ابراهیم بپیوندند.
@
VahidHeadline
دونالد ترامپ در شبکه تروث سوشال نوشت که پیوستن جمهوری اسلامی به پیمان ابراهیم، می‌تواند به «اتفاقی تاریخی» تبدیل شود.
او افزود که در گفت‌وگو با سران عربستان سعودی، امارات متحده عربی، قطر، ترکیه، مصر، اردن و بحرین، تاکید کرده لازم است همه این کشورها به‌طور هم‌زمان پیمان ابراهیم را برای عادی‌سازی روابط با اسرائیل امضا کنند.
ترامپ نوشت: ««کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یکی دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند که این توافق با ایران را به رویدادی بسیار تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75703" target="_blank">📅 18:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uMbHKXG2TNoo6JW6wOfiNsg1HmN-kc_p1t8QaaMDD7XLW5qtXE29LmETqznbsH9crNkdWds2z1jZOfBiWYPviEkiqBWCqQc7IDWdcdAEmIrz8bbsFB6UBG4GjtidxofLfOO6XlHxS2HwatIegDDZjH1LV__zlkw9yiDs-Ih0ii0hQquFf3SV1anxgOgmRSAO8LL0G0XLVWdOSNIiDXdUfITBOCw2ZWAqhqsXjI9CUl3T_oJLXeiQf2uVqmItJQUKKkO5B7REfMLpBKHSOrInnJZG_PGRw3j0ozumBLCKzhXVNNIQSXcjbFv09hXXfAbnbtx4eKPyUjFt1URoEBSoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OLirTwYCf3tMsA1eNpgebop-uBeYeEbTcUWHY2ZtviuOrP66fKTASzw-XReJ5u6PQOJxRo6UvskExONE14sSL2ARZSMIxYjKQ1fEBmh-JgtAaBSB3HZOMseh0GOCtIqAyfLLBy8YHtc5pigIw-23xB68CgShuKKdDmBxqjPfoXfDbLJ9YM6SJbg8vqAeUvWIktsmX3vbDz0mLPQtw3hmtmQ_pV7gkzjhmgipXqd9gCeLroDl0slVVXWngmvHIIPcDYB2i7rLHMyPkzduLDIlbIeEZ602BalwY90Q-GS0u8n3Rlx9JNIrzZEgWOI_hbFW00akPZhCG7prJ1PrbjLrbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری‌های رویترز و فرانسه به نقل از یک مقام آگاه، از سفر غیر‌منتظره محمد باقر قالیباف و عباس عراقچی، مذاکره‌کنندگان ارشد ایران، به دوحه خبر داده‌اند.
بر اساس این گزارش‌ها، رئیس مجلس و وزیر خارجه ایران برای گفت‌وگو با نخست‌وزیر قطر به دوحه سفر کرده‌اند.
رویترز نوشت که این گفت‌و‌گوها عمدتا درباره «تنگه هرمز و ذخایر اورانیوم غنی‌شده» ایران است.
رسانه‌های ایران گزارش داده بودند که عبدالناصر همتی، رئیس کل بانک مرکزی ایران، برای «بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات» به قطر سفر کرده است.
هیئتی از قطر هفته پیش به ایران سفر کرده بود.
یکی از خواسته‌های ایران در مذاکره با آمریکا آزاد شدن منابع مالی مسدودشده‌اش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75701" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4cgO8swYfN3lLj0MMyMBy81kFqgdD3_-SMVU8JZ3SvwBVdm6sxnpL4RjGangyOCPsle-c_snBXiXF3OEb5pX9UNYuhf8h_bjphXOLK7enMwqJEfL4_Miqt-w51hGoXwFSWRG64n5Da1WBgBvP1PMSrvSB85CPbTiCLCPLvxCklt_dEQu1cShicrrBhnYtTFoaNL8lPpzdgA6JzKIyfvO2LVJUA20JUBDRIk_EZ1rnPpdPDJ0ruQ8EfX8o9SCHOjmw0RhX021expXpNKdA9pAlzv3bczGa2X0z_KcJ6ijNctHnLHj7gfSfymwWBBogNnWyCo8FQ5OjEdZMihEFYFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی در شبکه اجتماعی تروث سوشال گفت توافق احتمالی با ایران یا «عالی و معنادار» خواهد بود یا اساساً توافقی در کار نخواهد بود.
آقای ترامپ در این پیام، منتقدان خود در میان دموکرات‌ها و برخی جمهوری‌خواهان را به باد انتقاد گرفت و گفت آنان «هیچ چیز» دربارهٔ توافق احتمالی او با ایران نمی‌دانند و حتی دربارهٔ موضوعاتی اظهار نظر می‌کنند که به گفتهٔ او «هنوز مذاکره نشده‌اند».
ترامپ تأکید کرد توافق مورد نظر او با ایران «دقیقاً نقطهٔ مقابل» توافق هسته‌ای برجام خواهد بود؛ توافقی که او بار دیگر آن را «فاجعه» خواند و دولت باراک اوباما را به گشودن «مسیر مستقیم و آشکار» ایران به سوی جنگ‌افزار هسته‌ای متهم کرد.
او در پایان پیام خود نوشت: «من چنین توافق‌هایی نمی‌کنم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75700" target="_blank">📅 18:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPcx4lTO_UpGc0ij86NvXPgaCekEkX7JuwqqfdPm2HgWrnMPKrdoxciId5lFiyUvTJsxeSrMy8pjBHZBa6E240cW3ao0dcmdnR-rvDc5auWpuVnXiJAgx_mRS9pT3D4f5Fgu7qk2lH3iXhkNRqe0vZsL2wbsEOPIjMA98MU9UtSlm6PO1jBAY0h2gQ9W0P7fDY8aLexFHOwz0gXLJp7TGUo78yOBo2NfSHtpQGApTHc4Flrij0xY64HoWBMgnFpbc3DZ9WhrbIFi-Tkrs6XnkMPFN08mso16nETuP18dlz-QR0QQs6TH-W9AZMSalrVO2wX-s1eEefFj_N-cMxjwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌اند؛ مصوبه‌ای که هنوز برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، است.
خبرگزاری فارس روز دوشنبه چهارم خرداد گزارش داد چهارمین جلسه این ستاد به ریاست محمدرضا عارف، معاون اول رئیس‌جمهور، برگزار شد و در آن «مصوبات مهمی» دربارهٔ اتصال به اینترنت بین‌الملل به تصویب رسید.
فارس به نقل از یک منبع نوشت که «برقراری اتصال اینترنت بین‌الملل» با ۹ رأی موافق و سه رأی مخالف تصویب شده و برای تأیید به دفتر رئیس‌جمهور ارسال شده است.
خبرگزاری تسنیم نیز با انتشار گزارشی مشابه نوشت مصوبات این جلسه پس از تأیید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ خواهد شد.
در همین حال، سیتنا، رسانه تخصصی حوزه ارتباطات و فناوری اطلاعات، به نقل از «یک منبع آگاه» گزارش داد که در جلسه صبح دوشنبه «بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴» مصوب شده و در صورت تأیید مسعود پزشکیان، جهت اجرا به وزارت ارتباطات ابلاغ خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75699" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9LJRABqD8h4TgRRZmGWIQ7fPHdTNwRXm7xTfT0DsLNCsrXaA4Q1QyjwE9l-q0H6VqyjnXsV3pB6dhnNDCPkVDTn9fJg9UnDkHhRF6C8sCN8puZ1Xu6oIfW4IpLhAtLi4VCirMOt_O9F-s1qRc7X9RleWFAt_zcCP3crQKY1ZfyoOzNdRvl4bTCIW4ez_N5sy5m0gDA4jH5koQek1CP7OMdy_RDL-nTCYZc9c7epyUKrJ6tu3thlNJvQTDS_YLWhoSlbF6a-BfoHrLfDu4IeVD3c4RtK34T73BYpaAcQz8te1x1CUF7ZbUrlzOD64EEJQQbTdCGzmwB3tc5bOFHHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از «حسین کرمانپور»، رییس مرکز روابط عمومی وزارت بهداشت، گزارش دادند که جراحت‌های وارد شده به «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، در جریان حملات اخیر «سطحی» بوده و مشکل جدی برای او ایجاد نکرده است.
کرمانپور گفت رهبر جمهوری اسلامی تنها از ناحیه صورت، سر و پاها دچار جراحت شده و این آسیب‌ها «منجر به قطع عضو یا ناراحتی خاصی نشده است.»او همچنین مدعی شد که هنگام انتقال خامنه‌ای به بیمارستان، پزشکان از او خواسته‌اند روزه خود را بشکند، اما او تا زمان افطار روزه‌اش را ادامه داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75698" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUV1kdk_rGayeTurJtglsBFbwXeaJwoHwsrCNfX_yxBRazF4oS5JQ6xeKEM8hJ3GqrdkN6rEeYcT6Kr_DqMMEAqGXzLE3gk4zW1cETeVwRzUQ8GY9AS40UrNDSsQyVEM55H9Y2eeBvSnRixI9qSHeLfQ1BfRFLAUo5sSkKOCnUeaO5_qOJsRKlV9n7fUPJVTcgDx0sImJGYBRXD3T1Uee-6kRhjTwcVbeiNHBG3X5PG4nSRXTFH8KpJrSOkGsjJHevPXVC52mLiDLqfMg1SppkN9wNSy0-EhIZ70GKeFJxZ9CmLOmn0vZvZ6J7TCxaVOkIJk7L7FdyblU2bWunbO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید که سفر وزیر خارجه به نیویورک برای شرکت در نشست شورای امنیت «منتفی» شده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران، دلیل انجام نشدن سفر عباس عراقچی را «مشکل روادید» عنوان کرد.
آقای بقایی چهارشنبه هفته پیش درمورد حضور آقای عراقچی در این نشست گفته بود: «این سفر به نیویورک احتمال دارد انجام شود و البته ممکن هم هست انجام نشود، چون هنوز قطعی نیست. دلیلش هم این است که هم باید روادید صادر شود و هم ممکن است اولویت‌های دیگری داشته باشیم.»
چین به‌عنوان رئیس دوره‌ای شورای امنیت، سه‌شنبه ۲۶ مه یک بحث آزاد در سطح بالا با موضوع «حفظ اهداف و اصول منشور سازمان ملل و تقویت نظام بین‌المللی متمرکز بر سازمان ملل» برگزار خواهد کرد.
این جلسه به ریاست وانگ یی، عضو دفتر سیاسی کمیته مرکزی حزب کمونیست و وزیر امور خارجه چین، برگزار می‌شود.
چین این نشست را «فرصتی» برای همبستگی و اجماع کشورهای عضو توصیف کرد تا «تعهد راسخ خود را به حفظ اهداف و اصول منشور سازمان ملل متحد مجددا تصریح و نقش محوری این سازمان را در نظام بین‌المللی احیا کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75697" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1fu92mZffyfY_3I6XckbLbVqsQIJUeksQLJNsXH9ZPtkCjfIs0QiFK4LeHxy2F8VW5tA450Y_Y6stTwaA9pK8ao3vxlgUR7vzbcYsEIr2f-NpKpwg35DoRmpOSNBbQG2dyedKw43CW8VlsoeXq5nrQQBfZ341jOeBGeOX1g_4MOlPdVh_ImDsE5KoC1Ck6yFUYqolCaZ9aJ1e-r2166FzjSvKXfxPV-23xSs198mJroIseHW_m1EvB07PBFjdAa6xC7_i0Oroy_GubC4EHrpd0OjoLGlsHHVKslC9IiK8QWL5z7FAbQshYkCd6afebi9MS_zgJs-E3Mb-DYPDlrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۲۶ اردیبهشت‌ماه ۱۴۰۵، «جانا سعدوئی»، زن ۱۹ ساله، مادر دو کودک و اهل روستای تاریمیش از توابع بخش قطور شهرستان خوی، به دست همسر خود به قتل رسیده است.
به گفته منابع آگاه، همسر این زن پس از وارد کردن ضربات مرگبار، تلاش کرده است ماجرا را به‌عنوان «خودکشی» جلوه دهد.
با این حال، نتایج بررسی‌های پزشکی قانونی و تناقض‌های موجود در روایت‌ها و اظهارات مطرح‌شده، ابعاد این قتل و تلاش برای صحنه‌سازی را آشکار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75696" target="_blank">📅 18:42 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
